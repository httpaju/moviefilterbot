<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com/?lines=Welcome+to+TorrentBot!" alt="Typing SVG"/>
</p>

<h1 align="center">
  Telegram Torrent Bot
</h1>

## Main Features
<b>
- [x] Upload files → auto-forward to file channel  
- [x] `/maketorrent` → create `.torrent` from your last upload  
- [x] `/download` → accept magnet or `.torrent` & start download  
- [x] `/status` → check active torrent download progress  
- [x] `/directlink` → generate direct download link  
- [x] MongoDB persistence for files & torrents  
- [x] Lightweight Flask server for direct downloads  
- [x] Friendly, guided user messages  
</b>

---

## Commands
```text
• /start              - Show welcome & help menu  
• (Upload file)       - Forward file to storage channel  
• /maketorrent        - Create torrent for last uploaded file  
• /download           - Reply to .torrent or magnet link to download  
• /status             - Show your active download statuses  
• /directlink <hash>  - Get direct download link for file  
Required Variables
BOT_TOKEN – Your bot token from @BotFather

API_ID – From https://my.telegram.org/apps

API_HASH – From https://my.telegram.org/apps

LOG_CHANNEL – Telegram channel ID for file storage (-100…)

MONGO_URI – Your MongoDB connection string

DB_NAME – Database name (e.g. torrent_bot)

HOST – Public URL of your Flask server (e.g. https://yourapp.onrender.com)

PORT – Port for Flask (default 8080)

DOWNLOAD_DIR – Local folder to store downloads (e.g. downloads)

<details> <summary><b>Deploy To Render</b></summary> <br> **1. Push your repo to GitHub** **2. Create a new Web Service on Render**
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
Environment Variables:
Set BOT_TOKEN, API_ID, API_HASH, LOG_CHANNEL, MONGO_URI, DB_NAME, HOST (https://yourapp.onrender.com), PORT (8080), DOWNLOAD_DIR

<br> **3. Confirm** your service is running and your bot responds. </details> <details> <summary><b>Deploy To VPS / Docker</b></summary> <br> ```bash git clone https://github.com/yourusername/telegram-torrent-bot.git cd telegram-torrent-bot pip3 install -r requirements.txt # Create config.env with required variables python3 main.py ``` </details>
License 🏷️
This project is licensed under the MIT License. See the LICENSE file for details.

Made with ❤️ by Ajmal

vbnet
Copy
Edit

```text
MIT License

Copyright (c) 2025 Ajmal

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
