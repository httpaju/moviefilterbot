<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Telegram Torrent Bot README in Canvas</title>
<style>
  body {
    margin: 0; background: #111; color: #eee; display: flex; justify-content: center; align-items: flex-start; padding: 20px;
    font-family: Consolas, monospace;
  }
  canvas {
    border: 2px solid #5a5a5a;
    background-color: #1e1e1e;
  }
</style>
</head>
<body>
<canvas id="readmeCanvas" width="900" height="1600"></canvas>

<script>
const canvas = document.getElementById('readmeCanvas');
const ctx = canvas.getContext('2d');

const width = canvas.width;
const padding = 30;
let cursorY = padding;

ctx.fillStyle = '#eee';

function drawText(text, x, y, maxWidth, font = '16px Consolas', color = '#eee', align = 'left') {
  ctx.font = font;
  ctx.fillStyle = color;
  ctx.textAlign = align;

  // For multiline text wrapping
  const words = text.split(' ');
  let line = '';
  let lineHeight = parseInt(font) * 1.4;
  let curY = y;
  
  for (let n = 0; n < words.length; n++) {
    const testLine = line + words[n] + ' ';
    const metrics = ctx.measureText(testLine);
    const testWidth = metrics.width;
    if (testWidth > maxWidth && n > 0) {
      ctx.fillText(line, x, curY);
      line = words[n] + ' ';
      curY += lineHeight;
    } else {
      line = testLine;
    }
  }
  ctx.fillText(line, x, curY);
  return curY + lineHeight; // return new y position
}

function drawHeading(text, y) {
  ctx.font = 'bold 28px Consolas';
  ctx.fillStyle = '#00ccff';
  ctx.fillText(text, width / 2, y);
  return y + 40;
}

function drawSubHeading(text, y) {
  ctx.font = 'bold 20px Consolas';
  ctx.fillStyle = '#66d9ff';
  ctx.fillText(text, padding, y);
  return y + 30;
}

function drawBullet(text, y) {
  ctx.font = '16px Consolas';
  ctx.fillStyle = '#eee';
  const bullet = '\u2022 ';
  // Draw bullet
  ctx.fillText(bullet, padding + 10, y);
  // Draw text wrapped
  const textX = padding + 30;
  const maxTextWidth = width - textX - padding;
  return drawText(text, textX, y, maxTextWidth);
}

function drawCodeBlock(lines, y) {
  const lineHeight = 20;
  const blockPadding = 10;
  const blockWidth = width - padding * 2;

  // Background for code block
  ctx.fillStyle = '#222';
  ctx.fillRect(padding, y, blockWidth, lineHeight * lines.length + blockPadding * 2);

  ctx.fillStyle = '#90ee90'; // light green for code text
  ctx.font = '14px Consolas';

  let curY = y + blockPadding + 14;
  for (const line of lines) {
    ctx.fillText(line, padding + 10, curY);
    curY += lineHeight;
  }
  return y + lineHeight * lines.length + blockPadding * 2 + 10;
}

// Draw everything step by step
cursorY = drawHeading('Telegram Torrent Bot', cursorY + 20);

cursorY = drawSubHeading('Welcome to TorrentBot!', cursorY);

const introText = "Telegram Torrent Bot lets you upload files, create torrent files, download torrents via magnet or .torrent files, and generate direct download links—all from within Telegram. It uses MongoDB for data persistence and runs a lightweight Flask server to serve direct downloads.";
cursorY = drawText(introText, padding, cursorY, width - padding * 2);

cursorY += 20;
cursorY = drawSubHeading('Main Features', cursorY);

const features = [
  'Upload files and auto-forward to a dedicated storage channel',
  'Create `.torrent` files from your last uploaded file using `/maketorrent`',
  'Download torrents by replying with magnet links or `.torrent` files using `/download`',
  'Check active torrent download progress with `/status`',
  'Generate direct download links for files via `/directlink`',
  'Persistent storage with MongoDB',
  'Lightweight Flask server for hosting direct downloads',
  'Friendly, guided user messages'
];
for (const feat of features) {
  cursorY = drawBullet(feat, cursorY);
}

cursorY += 20;
cursorY = drawSubHeading('Commands', cursorY);

const commandText = 
`/start         - Show welcome and help menu
Upload file    - Forward file to storage channel
/maketorrent   - Create a torrent file from your last upload
/download     - Reply to .torrent or magnet link to start download
/status       - Show your active torrent download progress
/directlink   - Get direct download link for a file hash`;

cursorY = drawCodeBlock(commandText.split('\n'), cursorY);

cursorY += 20;
cursorY = drawSubHeading('Required Variables', cursorY);

const envVars = [
  '`BOT_TOKEN` – Your bot token from @BotFather',
  '`API_ID` – From https://my.telegram.org/apps',
  '`API_HASH` – From https://my.telegram.org/apps',
  '`LOG_CHANNEL` – Telegram channel ID for file storage (e.g., `-1001234567890`)',
  '`MONGO_URI` – Your MongoDB connection string',
  '`DB_NAME` – Database name (e.g., `torrent_bot`)',
  '`HOST` – Public URL of your Flask server (e.g., `https://yourapp.onrender.com`)',
  '`PORT` – Port for Flask server (default: `8080`)',
  '`DOWNLOAD_DIR` – Local folder path to store downloads (e.g., `downloads`)'
];
for (const v of envVars) {
  cursorY = drawBullet(v, cursorY);
}

cursorY += 20;
cursorY = drawSubHeading('Deploy to Render', cursorY);

const deployRenderText = 
`1. Push your repo to GitHub.
2. Create a new Web Service on Render.

Environment: Python 3.x

Build Command:
pip3 install -r requirements.txt

Start Command:
python3 main.py

Set environment variables:
BOT_TOKEN, API_ID, API_HASH, LOG_CHANNEL, MONGO_URI, DB_NAME, HOST, PORT, DOWNLOAD_DIR

Confirm your service is running and your bot responds.`;

cursorY = drawText(deployRenderText, padding, cursorY, width - padding * 2);

cursorY += 20;
cursorY = drawSubHeading('Deploy on VPS / Docker', cursorY);

const deployVPSCode = [
  'git clone https://github.com/yourusername/telegram-torrent-bot.git',
  'cd telegram-torrent-bot',
  'pip3 install -r requirements.txt',
  '',
  '# Create a config.env file with the required environment variables',
  '',
  'python3 main.py'
];
cursorY = drawCodeBlock(deployVPSCode, cursorY);

cursorY += 20;
cursorY = drawSubHeading('License', cursorY);

const licenseText = 
`MIT License

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
SOFTWARE.`;

cursorY = drawText(licenseText, padding, cursorY, width - padding * 2, '14px Consolas', '#aaa');

cursorY += 40;
ctx.font = 'italic 16px Consolas';
ctx.fillStyle = '#00ccff';
ctx.fillText('Made with ❤️ by Ajmal', width / 2, cursorY);
</script>
</body>
</html>
