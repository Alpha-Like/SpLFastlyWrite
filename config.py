import os

# mandatory vars
BOT_TOKEN = os.getenv("BOT_TOKEN", None) # Get it from @BotFather [Telegram]
MONGO_DB_URI = os.getenv("MONGO_DB_URI", None) # Get it from mongodb.com
OWNER_ID = int(os.getenv("OWNER_ID", '')) # Get it from @SpL_Levi_Ackerman_Bot [Telegram]
BACKGROUND_IMAGE_URL = os.getenv("BACKGROUND_IMAGE_URL", None) # use Telegraph 

# non-mandatory vars
API_ID = os.getenv("API_ID", None)
API_HASH = os.getenv("API_HASH", None)
WORD_SPAWN_TIME = os.getenv("WORD_SPAWN_TIME", None) # must be in seconds, Ex :- 900, Minimum :- 900
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", None) # Ex :- 'Spoiled_Community' 
SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", None) # Ex :- 'SpLBots'

def load_env():
  dic = os.environ
  dic['BOT_TOKEN'] = BOT_TOKEN
  dic['MONGO_DB_URI'] = MONGO_DB_URI
  dic['OWNER_ID'] = OWNER_ID
  dic['BACKGROUND_IMAGE_URL'] = BACKGROUND_IMAGE_URL
  dic['API_ID'] = API_ID
  dic['API_HASH'] = API_HASH
  dic['WORD_SPAWN_TIME'] = WORD_SPAWN_TIME
  dic['SUPPORT_GROUP'] = SUPPORT_GROUP
  dic['SUPPORT_CHANNEL'] = SUPPORT_CHANNEL
  os.environ = dic
