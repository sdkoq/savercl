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
SESSION = config("SESSION", "BQGVaiQAK4BcHO-vA1Ny2HAn0d1ilnxlgqxyClyfifCAA4d25RBp-TKxYzmXgCf1-u1D_pc_Ilm1ffxQmUqpLQcpZmGk1PfUyWWHBc_Bn1CR3ClJJF07gUyBiHCyLtN45uQog7Gm7G6c76ZMmRNYT7Nk5rZSw2yOwHk07RvVTCa6LV30zyBJHp5MgO5vdeFzTMo_wGZ5BNyUZJImB-SYurTDc8jaZGgntZBElc9U74ui_EULeH9z_iEciiTuSRRCkowMTNDJ4szAhMo6Jd5DFUmInsXLShZwyP8q4U9178uumy1gpwowVWBlGpLBut2SQSRvbO7-LjftnkOZIKPT4_e2i7yJRgAAAAGowym-AQ")
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
