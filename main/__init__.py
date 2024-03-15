#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", "26569252", cast=int)
API_HASH = config("API_HASH", "6e7bea542d5a4f15edad630067b338fa")
BOT_TOKEN = config("BOT_TOKEN", "7126329790:AAEh3mfxqGlCL1kQTWh31jOZfC0g5j1ST2Q")
SESSION = config("SESSION", "BQGVaiQAZXKYiTktItSb1GthH_0hl-xKRqgH9b_6F1HnIw6Kkm6P6Y3CkzqTyDnR4IPPdT3CZYy20xu9CZenWkXt25pRfA0gtL7LjVcxvJZHtnCqCcj5HPJqCGyP-zSKp8dL723FkwThyW4WABFkuftXUFVyGdX9nx7s4p3w2rcI5wsbRoZi8KGOG6sA1au69dtnMTyK9UnS9nI9utimxcijSdnSD6swFiBAgAdkJuNscIGEGydObaT3-zspbaYS_3SuyNNjk8-iUhFF9Wc8Uwnt1w50q1C9DWQXTDz2wJoM-zJt-G_1z89dpm3-NbBHwufvbQhZdf25R7dNDZv-U2Ia1IZhxwAAAABK7NJ7AA")
FORCESUB = config("FORCESUB", "THE1onefed")
AUTH = config("AUTH", "1257034363", cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
