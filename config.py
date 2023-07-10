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
