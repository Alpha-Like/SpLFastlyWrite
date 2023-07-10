import os

# mandatory vars
BOT_TOKEN = os.getenv("BOT_TOKEN", None) # Get it from @BotFather [Telegram].
MONGO_DB_URI = os.getenv("MONGO_DB_URI", None) # Get it from mongodb.com
OWNER_ID = int(os.getenv("OWNER_ID", '')) # Get it from @SpL_Levi_Ackerman_Bot [Telegram].
LOAD_ENV: bool = False # Set this to 'True' if you are filling your vars in this file itself.

# non-mandatory vars
API_ID = os.getenv("API_ID", None)
API_HASH = os.getenv("API_HASH", None)
BACKGROUND_IMAGE_URL = os.getenv("BACKGROUND_IMAGE_URL", None) # use Telegraph .
WORD_SPAWN_TIME = os.getenv("WORD_SPAWN_TIME", None) # must be in seconds, Ex :- 900, Minimum :- 900.
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", None) # Ex :- 'Spoiled_Community'.
SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", None) # Ex :- 'SpLBots'.

# Do not change codes below !

def load_env():
  if LOAD_ENV:
    dic = os.environ
    dic["API_ID"] = API_ID
    dic["API_HASH"] = API_HASH
    dic["BACKGROUND_IMAGE_URL"] = BACKGROUND_IMAGE_URL
    dic["WORD_SPAWN_TIME"] = WORD_SPAWN_TIME
    dic["SUPPORT_GROUP"] = SUPPORT_GROUP
    dic["SUPPORT_CHANNEL"] = SUPPORT_CHANNEL
    dic["OWNER_ID"] = OWNER_ID
    dic["MONGO_DB_URI"] = MONGO_DB_URI
    dic["BOT_TOKEN"] = BOT_TOKEN
    os.environ = dic
