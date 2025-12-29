# Rexbots
# Don't Remove Credit
# Telegram Channel @RexBots_Official 
#Supoort group @rexbotschat


import os

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    USER_ID = int(os.getenv("USER_ID", ""))
    API_ID = int(os.getenv("API_ID", ""))
    API_HASH = os.getenv("API_HASH", "")
    DB_NAME = os.getenv("DB_NAME", "")
    DB_URL = os.getenv("DB_URL", "")
    CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", ""))
    MAX_CHAPTERS_PER_CHECK = int(os.getenv("MAX_CHAPTERS", "5"))
    DOWNLOAD_DIR = "downloads"
    STATE_FILE = "bot_state.json"
    CACHE_FILE = "manga_ids_cache.json"
    API_BASE = "https://api.mangadex.org"
    WEB_BASE = "https://mangadex.org"
    LOOKBACK_HOURS = 24
    MAX_IMAGE_SIZE = 10 * 1024 * 1024
    MAX_PDF_SIZE = 50 * 1024 * 1024
    USE_DATABASE = os.getenv("USE_DATABASE", "true").lower() == "true"
    
    PORT = int(os.getenv("PORT", "8080"))
    TG_BOT_WORKERS = int(os.getenv("TG_BOT_WORKERS", "4"))

    PICS = [
        "","","","","","","","" 
    ]

    DEFAULT_FILENAME_FORMAT = "{manga_name} [Ch-{chapter}]"


# Rexbots
# Don't Remove Credit
# Telegram Channel @RexBots_Official 
#Supoort group @rexbotschat