from pyrogram import Client
import os

API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("TOKEM", "")
AUTH_CHAT = int(os.environ.get("AUTH_CHAT", ""))

NYAA = Client("Nyaa", api_id = API_ID, api_hash = API_HASH, bot_token = BOT_TOKEN)
with NYAA:
    botname = NYAA.get_me().username
