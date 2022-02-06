from pyrogram import Client
import os

API_ID = 2919867
API_HASH = "90dd95178a8d13a69bfdbc7da68d23a4"
BOT_TOKEN = "5015207309:AAEoifISfnyTYGGZkPLWnXpMQVGM7mEkGf8"
AUTH_CHAT = -1001652493076

NYAA = Client("Nyaa", api_id = API_ID, api_hash = API_HASH, bot_token = BOT_TOKEN)
with NYAA:
    botname = NYAA.get_me().username
