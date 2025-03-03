
from os import environ 

class Config:
    API_ID = int(environ.get("API_ID", "21446074"))
    API_HASH = environ.get("API_HASH", "d858470de0403d3479bd1a0c1fbf2625")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7900068504:AAGXEA1jFXhoJOIdEVN-VzB55bqNFlWWqOw") 
    BOT_SESSION = environ.get("BOT_SESSION", "vjbot") 
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://amarjitpradhan1000:ZdHyuTVez6rYU78V@cluster0.qmkwu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "vj-forward-bot")
    BOT_OWNER = int(environ.get("BOT_OWNER", "7167357921"))


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
