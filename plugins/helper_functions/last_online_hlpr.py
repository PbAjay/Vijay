from pyrogram.types import User
from datetime import datetime


def last_online(from_user: User) -> str:
    time = ""
    if from_user.is_bot:
        time += "ʙᴏᴛ :("
    elif from_user.status == 'ʀᴇᴄᴇɴᴛʟʏ':
        time += "ʀᴇᴄᴇɴᴛʟʏ"
    elif from_user.status == 'within_week':
        time += "ᴡɪᴛʜɪɴ ᴛʜᴇ ʟᴀsᴛ ᴡᴇᴇᴋ"
    elif from_user.status == 'within_month':
        time += "ᴡɪᴛʜɪɴ ᴛʜᴇ ʟᴀsᴛ ᴍᴏɴᴛʜ"
    elif from_user.status == 'long_time_ago':
        time += "ᴀ ʟᴏɴɢ ᴛɪᴍᴇ ᴀɢᴏ :("
    elif from_user.status == 'online':
        time += "ᴏɴʟɪɴᴇ"
    elif from_user.status == 'offline':
        time += datetime.fromtimestamp(from_user.last_online_date).strftime("%a, %d %b %Y, %H:%M:%S")
    return time
