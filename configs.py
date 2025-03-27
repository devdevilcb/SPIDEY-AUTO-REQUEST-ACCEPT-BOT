# Don't Remove Credit @spideyofficial777
# Subscribe YouTube Channel For Amazing Bot @spidey_official_777
# Ask Doubt on telegram @hacker_x_official_777

from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "28519661"))
    API_HASH = getenv("API_HASH", "d47c74c8a596fd3048955b322304109d")
    BOT_TOKEN = getenv("BOT_TOKEN", "7236731343:AAHzJYfnwvBQDekYq8sSKY5cXS1GgJTQsgk")
    
    CHANNEL_IDS = list(map(int, getenv("CHANNEL_IDS", "-1001959922658,-1002470391435,-1002433552221").split(",")))
    
    REACTIONS = ["👀", "😱", "🔥", "😍", "🎉", "🥰", "😇", "⚡"]
    
    ADMINS = list(map(int, getenv("ADMINS", "5518489725").split()))
    DATABASE_URI = getenv("DATABASE_URI", "mongodb+srv://spideyofficial777:6FwYFNcgrAPL8nqq@spidey777.pykfj.mongodb.net/?retryWrites=true&w=majority&appName=SPIDEY777")

    LOG_CHANNEL = int(getenv("LOG_CHANNEL", "-1002294764885")) 

class temp(object):    
    U_NAME = None
    B_NAME = None
      
Spidey = Config()

# Don't Remove Credit @spideyofficial777
# Subscribe YouTube Channel For Amazing Bot @spidey_official_777
# Ask Doubt on telegram @hacker_x_official_777
