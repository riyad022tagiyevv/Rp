import re
import random
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", None))

# Get this value from @MissRose_Bot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", None))

# Fill Queue Limit . Example - 15
QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", "10"))

## Fill these variables if you're deploying on heroku.
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# --- FIXED & CLEANED GIT VARIABLES ---
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/riyad022tagiyevv/Rp",
)

# default main — GitHub da main-dir
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

# your git token (if private repo)
GIT_TOKEN = getenv("GIT_TOKEN", None)
# --------------------------------------

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/roserobotlar")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/rosexmusic")

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Spotify Settings
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

# Telegram audio/video file size limits
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))

# Pyrogram v2 user session strings
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# Images
START_IMG_URL = ["https://i.postimg.cc/vZ5wdk4g/stylish-rose-logo-4cf77d1d-c697-47bc.jpg"]
PING_IMG_URL = ["https://i.postimg.cc/vZ5wdk4g/stylish-rose-logo-4cf77d1d-c697-47bc.jpg"]
STATS_IMG_URL = ["https://i.postimg.cc/vZ5wdk4g/stylish-rose-logo-4cf77d1d-c697-47bc.jpg"]

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL", "https://i.postimg.cc/pTV02skt/ROSEX-LOGO.jpg"
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL", "https://i.postimg.cc/pTV02skt/ROSEX-LOGO.jpg"
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL", "https://i.postimg.cc/pTV02skt/ROSEX-LOGO.jpg"
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL", "https://i.postimg.cc/pTV02skt/ROSEX-LOGO.jpg"
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL", "https://files.catbox.moe/9jj5w8.jpg"
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL", "https://files.catbox.moe/9jj5w8.jpg"
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL", "https://files.catbox.moe/9jj5w8.jpg"
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL", "https://files.catbox.moe/9jj5w8.jpg"
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL", "https://files.catbox.moe/9jj5w8.jpg"
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


# URL validation
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. It must start with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. It must start with https://"
        )
