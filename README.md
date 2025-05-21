<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=35&pause=1000&color=64F72E&center=true&vCenter=true&random=true&width=435&lines=Welcome+To+AJ+BOTS!" alt="Typing SVG"/>
</p>

<h1 align="center">Telegram Torrent Bot</h1>

---

## Main Features

- ✅ Upload files → auto-forward to file channel  
- ✅ `/maketorrent` → create `.torrent` from your last upload  
- ✅ `/download` → accept magnet or `.torrent` & start download  
- ✅ `/status` → check active torrent download progress  
- ✅ `/directlink` → generate direct download link  
- ✅ MongoDB persistence for files & torrents  
- ✅ Lightweight Flask server for direct downloads  
- ✅ Friendly, guided user messages  

---

## Commands

```text
/start              - Show welcome & help menu  
(Upload file)       - Forward file to storage channel  
/maketorrent        - Create torrent for last uploaded file  
/download           - Reply to .torrent or magnet link to download  
/status             - Show your active download statuses  
/directlink <hash>  - Get direct download link for file  
Required Environment Variables
Variable	Description
BOT_TOKEN	Your bot token from @BotFather
API_ID	From my.telegram.org/apps
API_HASH	From my.telegram.org/apps
LOG_CHANNEL	Telegram channel ID for file storage (-100...)
MONGO_URI	Your MongoDB connection string
DB_NAME	Database name (e.g. torrent_bot)
HOST	Public URL of your Flask server (e.g. https://yourapp.onrender.com)
PORT	Port for Flask server (default: 8080)
DOWNLOAD_DIR	Local folder to store downloads (e.g. downloads)

<details> <summary><b>Deploy to Render</b></summary>
Push your repo to GitHub.

Create a new Web Service on Render.

Environment: Python 3.x

Build Command:

bash
Copy
Edit
pip3 install -r requirements.txt
Start Command:

bash
Copy
Edit
python3 main.py
Set the environment variables (BOT_TOKEN, API_ID, API_HASH, LOG_CHANNEL, MONGO_URI, DB_NAME, HOST, PORT, DOWNLOAD_DIR).

Confirm your service is running and your bot responds.

</details> <details> <summary><b>Deploy to VPS / Docker</b></summary>
bash
Copy
Edit
git clone https://github.com/yourusername/telegram-torrent-bot.git
cd telegram-torrent-bot
pip3 install -r requirements.txt

# Create a config.env with required environment variables

python3 main.py
</details>
License
This project is licensed under the MIT License. See the LICENSE file for details.

Made with ❤️ by Ajmal

yaml
Copy
Edit

---

### Explanation:
- Used markdown best practices for GitHub README
- Added tables for environment variables for clarity
- Collapsible `<details>` blocks for deployment instructions to keep README clean
- Consistent bullet checkmarks with emojis (✅) for features
- Proper fenced code blocks for commands and scripts
- Aligned headings and separators for readability
- Preserved your signature at the end

