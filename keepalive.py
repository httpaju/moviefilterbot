

import os
import requests
import time
import atexit
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import pytz
import telebot  # The user-friendly bot library

# Load environment variables from a .env file
load_dotenv()

app = Flask(__name__, static_folder='public')
CORS(app)

# --- Configuration ---
# Add the websites you want to monitor here
SITES_TO_MONITOR = [
    'https://google.com',
    'https://github.com',

    'https://ajweyahub.ajapplications.in.net' # A test site that might be down
]

# --- Telegram Bot Configuration ---
TELEGRAM_BOT_TOKEN = os.environ.get('BOT_TOKEN')
TELEGRAM_CHAT_ID = os.environ.get('ADMIN')

# --- INITIALIZE THE BOT ---
bot = None
if TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID:
    bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
    print("[Uptime Bot] Telegram bot initialized. Alerts are active.", flush=True)
else:
    print("[Uptime Bot] Telegram Token or Chat ID not found. Alerts are DISABLED.", flush=True)
# --------------------------

# This dictionary will store the status of each site in memory
site_statuses = {}
IST = pytz.timezone('Asia/Kolkata')

# Initialize the status dictionary for all sites
for url in SITES_TO_MONITOR:
    site_statuses[url] = {
        'status': 'Checking...', # Initial status
        'lastChecked': None
    }

def send_telegram_alert(message):
    """Sends a message using the pyTelegramBotAPI (telebot)."""
    if not bot:
        print('[Uptime Bot] Telegram bot is not initialized. Skipping alert.', flush=True)
        return

    try:
        # The user-friendly way to send a message:
        bot.send_message(TELEGRAM_CHAT_ID, message, parse_mode='Markdown')
        print(f"[Uptime Bot] Telegram alert sent: {message}", flush=True)
    except Exception as error:
        print(f"[Uptime Bot] Failed to send Telegram alert: {error}", flush=True)

def check_site_status(url):
    """Checks a single site's status."""
    start_time = time.time()
    # Get the status before the check
    old_status = site_statuses.get(url, {}).get('status', 'Checking...') 
    new_status = 'DOWN'
    status_code = None

    try:
        response = requests.get(url, timeout=10, allow_redirects=True)
        if 200 <= response.status_code < 400:
            new_status = 'UP'
            status_code = response.status_code
        else:
            new_status = 'DOWN'
            status_code = response.status_code

    except requests.exceptions.Timeout:
        new_status = 'DOWN'
        status_code = 'Timeout'
        print(f"[Uptime Bot] Error checking {url}: Request timed out", flush=True)
    except requests.exceptions.RequestException as error:
        new_status = 'DOWN'
        status_code = 'Error'
        print(f"[Uptime Bot] Error checking {url}: {error}", flush=True)

    end_time = time.time()
    response_time = round((end_time - start_time) * 1000)

    # --- Alerting Logic ---
    if new_status == 'DOWN' and old_status == 'UP':
        message = f"🔴 *SITE DOWN* \n\nYour site *{url}* is unresponsive. \nStatus: {status_code or 'Error'}"
        send_telegram_alert(message)
    elif new_status == 'UP' and old_status == 'DOWN':
        message = f"✅ *SITE RECOVERED* \n\nYour site *{url}* is back online!"
        send_telegram_alert(message)

    # Update the status in memory
    site_statuses[url] = {
        'status': new_status,
        'statusCode': status_code,
        'responseTime': f"{response_time}ms",
        'lastChecked': datetime.now(IST).strftime('%Y-%m-%d %I:%M:%S %p')
    }
    print(f"[Uptime Bot] Checked {url}: {new_status} ({status_code})", flush=True)

def check_all_sites():
    """Triggers a status check for all monitored sites."""
    print("[Uptime Bot] Running scheduled site checks...", flush=True)
    for url in SITES_TO_MONITOR:
        check_site_status(url)

# --- API Endpoint ---
@app.route('/api/status')
def get_status():
    """This is the API endpoint where the frontend will get its data."""
    return jsonify(site_statuses)

# --- Serve Frontend ---
@app.route('/')
def serve_index():
    """Serves the index.html frontend."""
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    """Serves other static files (if any)."""
    return send_from_directory(app.static_folder, path)

# --- Main execution ---
if __name__ == '__main__':
    # 1. Start the scheduler
    scheduler = BackgroundScheduler(timezone=str(IST))
    scheduler.add_job(check_all_sites, 'interval', minutes=1)
    scheduler.start()
    print("[Uptime Bot] Scheduler started. Checks will run every minute.", flush=True)
    
    # 2. Run one check immediately on startup
    print("[Uptime Bot] Running initial site check on startup...", flush=True)
    check_all_sites()
    
    # 3. Make sure scheduler shuts down nicely when the app exits
    atexit.register(lambda: scheduler.shutdown())
    
  
