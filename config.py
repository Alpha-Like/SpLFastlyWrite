import os

# DO NOT FILL ANYTHING HERE, FILL EVERYTHING IN ENVIRONMENT ITSELF !

# mandatory vars
BOT_TOKEN = os.getenv("BOT_TOKEN", None) # Get it from @BotFather [Telegram]
MONGO_DB_URI = os.getenv("MONGO_DB_URI", None) # Get it from mongodb.com
OWNER_ID = int(os.getenv("OWNER_ID", '')) # Get it from @SpL_Levi_Ackerman_Bot [Telegram]

# non-mandatory vars
API_ID = os.getenv("API_ID", None)
API_HASH = os.getenv("API_HASH", None)
BACKGROUND_IMAGE_URL = os.getenv("BACKGROUND_IMAGE_URL", None) # use Telegraph 
WORD_SPAWN_TIME = os.getenv("WORD_SPAWN_TIME", None) # must be in seconds, Ex :- 900, Minimum :- 900
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", None) # Ex :- 'Spoiled_Community' 
SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", None) # Ex :- 'SpLBots'

# do not change code below
if API_ID:
  API_ID = int(API_ID)
  
if WORD_SPAWN_TIME:
  try:
    WORD_SPAWN_TIME = int(WORD_SPAWN_TIME)
    if WORD_SPAWN_TIME < 900:
      WORD_SPAWN_TIME = 900
  except:
    WORD_SPAWN_TIME = 900
else:
  WORD_SPAWN_TIME = 900

if SUPPORT_GROUP:
  if SUPPORT_GROUP[0] == '@':
    SUPPORT_GROUP = SUPPORT_GROUP[1:]
else:
  SUPPORT_GROUP = 'Spoiled_Community'
  
if SUPPORT_CHANNEL:
  if SUPPORT_CHANNEL[0] == '@':
    SUPPORT_CHANNEL = SUPPORT_GROUP[1:]
else:
  SUPPORT_CHANNEL = 'SpLBots'

if not BACKGROUND_IMAGE_URL:
  print('Using Default Background Image...')
  BACKGROUND_IMAGE_URL = 'https://telegra.ph/file/fe73eca247a491d4a6927.jpg'
