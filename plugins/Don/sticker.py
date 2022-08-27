#Made
#by
#Don_Sflix

from pyrogram import Client, filters

@Client.on_message(filters.command(["stickerid"]))
async def stickerid(bot, message):   
    if message.reply_to_message.sticker:
       await message.reply(f"**sᴛɪᴄᴋᴇʀ ɪᴅ ɪs **  \n `{message.reply_to_message.sticker.file_id}` \n \n ** ᴜɴɪǫᴜᴇ ɪᴅ ɪs ** \n\n`{message.reply_to_message.sticker.file_unique_id}`", quote=True)
    else: 
       await message.reply("ᴏᴏᴘs !! ɴᴏᴛ ᴀ sᴛɪᴄᴋᴇʀ ғɪʟᴇ")
