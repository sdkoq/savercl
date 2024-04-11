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
SESSION = config("SESSION", "BQGVaiQAqjRfNX7JxwtwTN2l9l4PPVUun7FIQDVSkLIUWXdc03p6zSRSsFx8RJGxDt4-TGGyzsxWCok06J0yPEzyU1rhG3V7LA4-xwXrzZveD_mRkOIRB3Mc3WaTnHvFyCIG4y-Z-hNgPVCfMn8Vggj2FxyGEah17X5hU6X8--ua6SxgWO8cWJcSJZvbIFOOineTnYZqCs_zAtDiKvhSEEtSnILGyS-zxTXIKULUcdiu33BIF_fE2-hVHzvXpKzcfOy1T3Ec9Kx94OqMiWc1BsIxq10ZyxykOiOssR7_hwrfbJZSkjxgbrx6lL8iTUS98eZzFzhnmD4n6rw7OoF5FiobzfCNEgAAAABK7NJ7AA")
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
