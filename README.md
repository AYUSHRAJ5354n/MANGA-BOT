# 🎌 Manga Downloader & Uploader Bot

<div align="center">

![Manga Bot Banner](https://ibb.co/mVkSySr7)

**Advanced Manga Automation Bot for Telegram**

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-blue.svg)](https://telegram.org/)

</div>

---

## ✨ Features

- 🔄 **Multi-Source Support**: Download from MangaDex, MangaForest, Mangakakalot, AllManga, and WebCentral
- 📥 **Auto-Upload**: Automatically upload new chapters to your Telegram channel
- 🎨 **Custom Thumbnails**: Set custom cover images for your PDFs
- 💧 **Watermarking**: Add custom watermarks to protect your content
- 📄 **PDF/CBZ Generation**: Convert manga chapters to high-quality PDFs or CBZ files
- 🔍 **Smart Search**: Search across multiple manga sources with `/search` command
- 🎯 **Custom Downloads**: Download specific chapters or ranges
- 📊 **Progress Tracking**: Real-time upload/download progress display
- 🔐 **Force Subscribe**: Require users to join channels before downloading
- 👥 **Admin System**: Multi-admin support with role management
- 📢 **Broadcast**: Send announcements to all bot users
- ⚙️ **Advanced Settings**: Customize banners, captions, file formats, and more

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- Telegram Bot Token (from [@BotFather](https://t.me/BotFather))
- Telegram API ID & Hash (from [my.telegram.org](https://my.telegram.org))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/abhinai2244/MANGA-BOT.git
   cd MANGA-BOT
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the bot**
   
   Edit `config.py` with your credentials:
   ```python
   BOT_TOKEN = "your_bot_token"
   USER_ID = your_telegram_user_id
   API_ID = your_api_id
   API_HASH = "your_api_hash"
   ```

4. **Run the bot**
   ```bash
   python Bot.py
   ```

---

## 📋 Available Commands

### 👤 User Commands

| Command | Description |
|---------|-------------|
| `/start` | Start the bot and view main menu |
| `/search <query>` | Search for manga across all sources |
| `/help` | Display help information |

### 👮 Admin Commands

#### Channel Management
| Command | Description |
|---------|-------------|
| `/set_chnl <channel_id>` | Set default upload channel |
| `/view_chnl` | View current channel configuration |
| `/rem_chnl` | Remove channel configuration |

#### Media & Appearance
| Command | Description |
|---------|-------------|
| `/set_caption` | Set custom caption template |
| `/set_banner` | Add intro/outro banner images |
| `/set_watermark` | Add custom watermark to pages |
| `/view_watermark` | View current watermark settings |
| `/rem_watermark` | Remove watermark |

#### File & Format
| Command | Description |
|---------|-------------|
| `/set_format` | Set filename format template |
| `/view_format` | View current filename format |

#### Admin Control
| Command | Description |
|---------|-------------|
| `/add_admin <user_id>` | Add a new admin |
| `/deladmin <user_id>` | Remove an admin |
| `/admins` | List all admins |

#### Force Subscribe
| Command | Description |
|---------|-------------|
| `/fsub_mode` | Toggle force subscribe on/off |
| `/add_fsub_chnl <channel_id>` | Add channel to force subscribe list |
| `/rem_fsub_chnl <channel_id>` | Remove channel from force subscribe list |
| `/fsub_chnls` | List all force subscribe channels |

#### Utilities
| Command | Description |
|---------|-------------|
| `/broadcast <message>` | Send message to all bot users |
| `/makepost` | Create custom manga post |

---

## ⚙️ Configuration Options

Access settings via `/start` → **⚙️ Settings**

### Available Settings

- **📡 Manga Source**: Choose default source (MangaDex, MangaForest, etc.)
- **📄 File Type**: PDF or CBZ format
- **🖼️ Thumbnail**: Set custom thumbnail for uploads
- **💧 Watermark**: Configure text watermark (position, color, opacity)
- **🎨 Banners**: Add intro/outro images to chapters
- **📝 Caption Template**: Customize post captions
- **🎯 Compress**: Enable image compression
- **⏱️ Check Interval**: Set auto-update check frequency
- **🔔 Monitor Toggle**: Turn auto-monitoring on/off
- **📢 Channel Stickers**: Add stickers to channel posts

---

## 🎯 Usage Examples

### Searching for Manga
```
/search solo leveling
```
Select a source from the buttons, then choose chapters to download.

### Custom Range Download
1. Search for a manga
2. Click "⬇ Custom Download (Range)"
3. Enter range: `10-20` or single chapter: `15`

### Setting Watermark
```
/set_watermark
```
Follow the interactive menu to customize position, color, and opacity.

---

## 📁 Project Structure

```
MANGA-BOT/
├── Bot.py                 # Main bot logic
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies
├── Database/
│   └── database.py       # Database operations
└── Plugins/
    ├── start.py          # Start & help commands
    ├── search.py         # Search functionality
    ├── admin.py          # Admin commands
    ├── uploading.py      # Upload handler
    ├── downloading.py    # Download handler
    ├── Settings/         # Settings menu plugins
    └── Sites/            # Manga source APIs
        ├── mangadex.py
        ├── mangaforest.py
        ├── mangakakalot.py
        ├── allmanga.py
        └── webcentral.py
```

---

## 🤝 Contributors

A huge thanks to the developers who made this project possible:

<table>
  <tr>
    <td align="center">
      <img src="https://github.com/abhinai2244.png" width="100px;" alt="Abhi"/>
      <br />
      <sub><b>Abhi</b></sub>
      <br />
      <sub>Owner</sub>
    </td>
    <td align="center">
      <img src="https://via.placeholder.com/100" width="100px;" alt="Abhinav"/>
      <br />
      <sub><b>Abhinav</b></sub>
      <br />
      <sub>Developer</sub>
    </td>
    <td align="center">
      <img src="https://via.placeholder.com/100" width="100px;" alt="Bharath"/>
      <br />
      <sub><b>Bharath</b></sub>
      <br />
      <sub>Developer</sub>
    </td>
    <td align="center">
      <img src="https://via.placeholder.com/100" width="100px;" alt="Master"/>
      <br />
      <sub><b>Master</b></sub>
      <br />
      <sub>Developer</sub>
    </td>
  </tr>
</table>

---

## 📞 Support

For queries, feature requests, or bug reports, join our official channel:

<div align="center">

[![Telegram Channel](https://img.shields.io/badge/Telegram-Channel-blue?logo=telegram)](https://t.me/about_zani/195)
[![Support Group](https://img.shields.io/badge/Telegram-Support-blue?logo=telegram)](https://t.me/akaza7902)

**Official Channel:** [@REXBOTS_OFFICIAL](https://t.me/akaza7902)

</div>

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ⚠️ Disclaimer

This bot is for educational purposes only. Users are responsible for complying with copyright laws in their jurisdiction. The developers do not encourage piracy or copyright infringement.

---

<div align="center">

**Made with ❤️ by the REXBOTS Team**

⭐ **Star this repo if you find it useful!** ⭐

</div>
