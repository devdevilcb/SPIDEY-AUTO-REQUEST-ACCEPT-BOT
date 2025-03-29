# Don't Remove Credit @spideyofficial777
# Subscribe YouTube Channel For Amazing Bot @spidey_official_777
# Ask Doubt on telegram @hacker_x_official_777

from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "20650942"))
    API_HASH = getenv("API_HASH", "9744c99858433c55c279cce6827d36a4")
    BOT_TOKEN = getenv("BOT_TOKEN", "7221916419:AAHJ1nZ_Av7CDu82ThD2870AhEX5IFXwBLk")
    
    CHANNEL_IDS = list(map(int, getenv("CHANNEL_IDS", "-1001782414786").split(","))) # for the multiple forcesub
    
    REACTIONS = ["👀", "😱", "🔥", "😍", "🎉", "🥰", "😇", "⚡"]
    # Spidey
    ADMINS = list(map(int, getenv("ADMINS", "1947565279").split()))
    DATABASE_URI = getenv("DATABASE_URI", "mongodb+srv://shubhamm2233a:password1234@cluster0.0zi6k.mongodb.net/?retryWrites=true&w=majority")

    LOG_CHANNEL = int(getenv("LOG_CHANNEL", "-1001919010755")) 

class temp(object):    
    U_NAME = None
    B_NAME = None
      
Spidey = Config()

# Don't Remove Credit @spideyofficial777
# Subscribe YouTube Channel For Amazing Bot @spidey_official_777
# Ask Doubt on telegram @hacker_x_official_777
