class script(object):
    START_TXT = """👋 ʜᴇʟʟᴏ {},
ᴍʏ ɴᴀᴍᴇ ɪs {},\n ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇs, ʏᴏᴜ ᴊᴜsᴛ ᴊᴏɪɴ ᴍʏ ɢʀᴏᴜᴘ ᴀɴᴅ ᴇɴᴊᴏʏ..."""
    HELP_TXT = """ʜᴇʏ {}
ʜᴇʀᴇ ɪs ᴍʏ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs"""
    ABOUT_TXT = """✯ ᴍʏ ɴᴀᴍᴇ : {}
✯ ᴄʀᴇᴀᴛᴏʀ : <a href=https://t.me/Crude_X>ᴄʀᴜᴅᴇ_x </a>
✯ ʟɪʙʀᴀʀʏ : ᴘʏʀᴏɢʀᴀᴍ
✯ ʟᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ 3
✯ ᴅᴀᴛᴀ ʙᴀsᴇ : ᴍᴀɴɢᴏ-ᴅʙ
✯ ʙᴏᴛ sᴇʀᴠᴇʀ : ʜᴇʀᴏᴋᴜ
✯ ʙᴜɪʟᴅ sᴛᴀᴛᴜs : 𝚅1.0.43 [𝙼𝙰𝙹𝙾𝚁]"""
    SOURCE_TXT = """<b>NOTE:</b>
⪼ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/MalluHubGP>ᴍᴀʟʟᴜʜᴜʙʏᴛ</a>

<b>ᴅᴇᴠ:</b>
<a href=https://t.me/Crude_X>ᴄʀᴜᴅᴇ_x</a>"""
    FILE_TXT = """ʜᴇʟᴘ : ɪɴғᴏ

<b>ɪ ᴀᴍ ᴀ ᴀᴜᴛᴏ ғɪʟᴛᴇʀ ʙᴏᴛ ᴄᴏᴅᴇᴅ ʙʏ <a href=https://t.me/Crude_X>ᴘʙ ᴀᴊᴀʏ</a> </b>"""
    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- Give a user details
•/whois :-give a user full details"""
    FUN_TXT ="""<b>Gᴀᴍᴇs</b> 
    
<b>ᴊᴜsᴛ sᴏᴍᴇ ᴋɪɴᴅ ᴏғ ғᴜɴ ᴛʜɪɴɢs</b>
 
1. /dice - ʀᴏʟʟ ᴛʜᴇ ᴅɪᴄᴇ
2. /Throw ᴛᴏ ᴛʜʀᴏᴡ ᴀʀʀᴏᴡ
3. /Dart - ᴛᴏ ᴍᴀᴋᴇ ᴅᴀʀᴛ
4. /Runs - ʀᴀɴᴅᴏᴍ ᴅɪᴀʟᴏɢᴜᴇs
5. /Goal - ᴛᴏ ᴍᴀᴋᴇ ɢᴏᴀʟ
6. /Shoot - ᴛᴏ sʜᴏᴏᴛ
7. /luck - ᴛʀʏ ʏᴏᴜʀ ʟᴜᴄᴋ"""
    MANUELFILTER_TXT = """ʜᴇʟᴘ : <b>ғɪʟᴛᴇʀs</b>

⪼ ғɪʟᴛᴇʀ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜsᴇʀs ᴄᴀɴ sᴇᴛ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇs ғᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ ᴀɴᴅ ᴠɪᴊᴀʏ  ᴡɪʟʟ ʀᴇsᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪs ғᴏᴜɴᴅ ᴛʜᴇ ᴍᴇssᴀɢᴇ

<b>ɴᴏᴛᴇ :</b>
1. ᴛʜɪs ʙᴏᴛ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
2. ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴀᴅᴅ ғɪʟᴛᴇʀs ɪɴ ᴀ ᴄʜᴀᴛ.
3. ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴs ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏғ 64 ᴄʜᴀʀᴀᴄᴛᴇʀs.

<bᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ :</b>
⪼ /filter - ᴀᴅᴅ ᴀ ғɪʟᴛᴇʀ ɪɴ ᴄʜᴀᴛ
⪼ /filters - ʟɪsᴛ ᴀʟʟ ᴛʜᴇ ғɪʟᴛᴇʀs ᴏғ ᴀ ᴄʜᴀᴛ
⪼ /del - ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ғɪʟᴛᴇʀ ɪɴ ᴄʜᴀᴛ
⪼ /delall - ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ғɪʟᴛᴇʀs ɪɴ ᴀ ᴄʜᴀᴛ"""
    SONG_TXT = """sᴏɴɢ ᴅᴏᴡɴʟᴏᴀᴅ</b>

<b>sᴏɴɢ ᴅᴏᴡɴʟᴏᴀᴅ ᴍᴏᴅᴜʟᴇ, ғᴏʀ ᴛʜᴏsᴇ ᴡʜᴏ ʟᴏᴠᴇ ᴍᴜsɪᴄ. ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ғᴇᴀᴛᴜᴇ ғᴏʀ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ sᴏɴɢ ᴡɪᴛʜ sᴜᴘᴇʀ ғᴀsᴛ sᴘᴇᴇᴅ.ᴡᴏʀᴋs ᴏɴʟʏ ᴏɴ ɢʀᴏᴜᴘs..</b>

<b>ᴄᴏᴍᴍᴀɴᴅ</b>

⪼  /song sᴏɴɢ ɴᴀᴍᴇ
ᴏɴʟʏ ᴡᴏʀᴋs ɪɴ ɢʀᴏᴜᴘ"""
    PIN_TXT ="""<b>ᴘɪɴ ᴍᴏᴅᴜʟᴇ</b>
<b>ᴘɪɴ ᴀ ᴍᴇssᴀɢᴇ..</b>

<b>ᴀʟʟ ᴛʜᴇ ᴘɪɴ ʀᴇᴘʟᴀᴛᴇᴅ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ғᴏᴜɴᴅ ʜᴇʀᴇ</b>

<b>ᴄᴏᴍᴍᴀɴᴅs</b>

⪼ /pin - ᴛᴏ ᴘɪɴ ᴛʜᴇ ᴍᴇssᴀɢᴇ ᴏɴ ʏᴏᴜʀ ᴄʜᴀᴛs
⪼ /unpin - ᴛᴏ ᴜɴᴘɪɴ ᴛʜᴇ ᴄᴜʀʀᴇᴇɴᴛ ᴘɪɴɴᴇᴅ ᴍᴇsᴀᴀɢᴇ"""
    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>

• /paste [text] - paste the given text on Pasty

<b>NOTE:</b>

• These commands works on both pm and group.
• These commands can be used by any group member."""
    TTS_TXT = """Help: <b> TTS 🎤 module:</b>

Translate text to speech

<b>Commands and Usage:</b>

• /tts <text> : convert text to speech

<b>NOTE:</b>

• IMDb should have admin privillage.
• These commands works on both pm and group.
• IMDb can translate texts to 200+ languages."""
    PINGS_TXT ="""ʜᴇʟᴘ : <b>ᴘɪɴɢ :</b>

ʜᴇʟᴘs ʏᴏᴜ ᴛᴏ ᴋɴᴏᴡ ʏᴏᴜʀ ᴘɪɴɢ 

<b>ᴄᴏᴍᴍᴀɴᴅs :</b>

⪼ /alive - ᴄʜᴇᴄᴋ ɴᴏᴛ ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ
⪼ /ping - ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴘɪɴɢ
<b>ᴜsᴀɢᴇ  :</b>

⪼ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ɪɴ ᴘᴍs ᴀɴᴅ ɢʀᴏᴜᴘs
⪼ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʙᴜʏ ᴇᴠᴇʀʏᴏɴᴇ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘs ᴀɴᴅ ʙᴏᴛs ᴘᴍ
⪼ sʜᴀʀᴇ ᴜs ғᴏʀ ᴍᴏʀᴇ ғᴇᴀᴛᴜʀᴇs"""
    TELE_TXT = """ʜᴇʟᴘ : <b>ᴛᴇʟᴇɢʀᴀᴘʜ</b>

ᴅᴏ ᴀs ʏᴏᴜ ᴡɪsʜ ᴡɪᴛʜ ᴛᴇʟᴇɢʀᴀ.ᴘʜ ᴍᴏᴅᴜʟᴇ!

</b>ᴜsᴀɢᴇ:</b>

/telegraph - sᴇɴᴅ ᴍᴇ ᴘɪᴄᴛᴜʀᴇ ᴏʀ ᴠɪᴅᴇᴏ ᴜɴᴅᴇʀ (5ᴍʙ)

<b>ɴᴏᴛᴇ :</b>

⪼ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ɢᴏᴜᴘs ᴀɴᴅ ᴘᴍs
⪼ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʙʏ ᴇᴠᴇʀʏᴏɴᴇ"""
    JSON_TXT ="""<b>JSON:</b>

Bot returns json for all replied messages with /json

<b>Features:</b>

Message Editting JSON
Pm Support
Group Support

<b>Note:</b>

Everyone can use this command , if spaming happens bot will automatically ban you from the group."""
    PURGE_TXT = """<b>Purge</b>
    
Delete A Lot Of Messages From Groups! 
    
 <b>ADMIN</b> 

◉ /purge :- Delete All Messages From The Replied To Message, To The Current Message"""
    BUTTON_TXT = """ʜᴇʟᴘ : <b>ʙᴜᴛᴛᴏɴs</b>

ᴛʜɪs ʙᴏᴛ sᴜᴘᴘᴏʀᴛs ʙᴏᴛʜ ᴜʀʟ ᴀɴᴅ ᴀʟᴇʀᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴs

<b>ɴᴏᴛᴇ:</b>
1. ᴛᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ sᴇɴᴅ ʙᴜᴛᴛᴏɴs ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, sᴏ ᴄᴏɴᴛᴇɴᴛ ɪs ᴍᴀɴᴅᴀᴛᴏʀʏ.
2. ᴛʜɪs ʙᴏᴛ sᴜᴘᴘᴏʀᴛs ʙᴜᴛᴛᴏɴs ᴡɪᴛʜ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
3. ʙᴜᴛᴛᴏɴs sʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴀʀsᴇᴅ ᴀs ᴍᴀʀᴋᴅᴏᴡɴ ғᴏʀᴍᴀᴛ

<b>ᴜʀʟ ʙᴜᴛᴛᴏɴs:</b>
<code>[Button Text](buttonurl:xxxxxxxxxxxx)</code>

<b>ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴs:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """ʜᴇʟᴘ : <b>ᴀᴜᴛᴏғɪʟᴛᴇʀ</b>
<u>ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ</u>

⪼ /autofilter on - ᴀᴜᴛᴏғɪʟᴛᴇʀ ᴇɴᴀʙʟᴇ ɪɴ ʏᴏʀ ᴄʜᴀᴛ
⪼ /autofilter off - ᴀᴜᴛᴏғɪʟᴛᴇʀ ᴅɪsᴀʙʟᴇ ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ

ᴀᴜᴛᴏ ғɪʟᴛᴇʀ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴛᴏ ғɪʟᴛᴇʀ ᴀɴᴅ sᴀᴠᴇ  ᴛʜᴇ ғɪʟᴇs ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ғʀᴏᴍ ᴄʜᴀɴɴᴇʟ ᴛᴏ ɢʀᴏᴜᴘ. ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ᴄᴏᴍᴍᴀɴᴅs ᴛᴏ ᴏɴ ᴀɴᴅ ᴏғғ ᴛʜᴇ ᴀᴜᴛᴏғɪʟᴛᴇʀ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ..

ᴄᴏᴍᴍᴀɴᴅs :
⪼ /set_template - sᴇᴛ ᴄᴜsᴛᴏᴍ ɪᴍᴅʙ ᴛᴇᴍᴘʟᴀᴛᴇ ғᴏʀ ᴀᴜᴛᴏ ғɪʟᴛᴇʀ
⪼ /get_template - ɢᴇᴛ ᴄᴜʀʀᴇɴᴛ ɪᴍᴅʙ ᴛᴇᴍᴘʟᴀᴛᴇ ᴏғ ᴀᴜᴛᴏ ғɪʟᴛᴇʀ"""
    CONNECTION_TXT = """ʜᴇʟᴘ: <b>ᴄᴏɴɴᴇᴄᴛɪᴏɴs</b>

⪼ ᴜsᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʙᴏᴛ ᴛᴏ ᴘᴍ ғᴏʀ ᴍᴀɴᴀɢɪɴɢ ғɪʟᴛᴇʀs 
⪼ ɪᴛ ʜᴇʟᴘs ᴛᴏ ᴀᴠᴏɪᴅ sᴘᴀᴍᴍɪɴɢ ɪɴ ɢʀᴏᴜᴘs

<b>ɴᴏᴛᴇ :</b>
1. ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴀᴅᴅ ᴀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ
2. sᴇɴᴅ <code>/connect</code> ғᴏʀ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴍᴇ ᴛᴏ ᴜʀ ᴘᴍ

<b>ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ :</b>
⪼ /connect  - ᴄᴏɴɴᴇᴄᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴛᴏ ʏᴏᴜʀ ᴘᴍ
⪼ /disconnect  - ᴅɪsᴄᴏɴɴᴇᴄᴛ ғʀᴏᴍ ᴀ ᴄʜᴀᴛ
⪼ /connections - ʟɪsᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴs"""
    EXTRAMOD_TXT = """ʜᴇʟᴘ : <b>ᴇxᴛʀᴀ</b>

<b>ɴᴏᴛᴇ :</b>
ᴛʜᴇsᴇ ᴀʀᴇ ᴛʜᴇ ᴇxᴛʀᴀ ғᴇᴀᴛᴜʀᴇs ᴏғ ᴛʜɪs ʙᴏᴛ

<b>ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ :</b>
⪼ /id - ɢᴇᴛ ɪᴅ ᴏғ ᴀ sᴘᴇᴄɪғᴇᴅ ᴜsᴇʀ
⪼ /info  - ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜsᴇʀ
⪼ /imdb  - ɢᴇᴛ ᴛʜᴇ ғɪʟᴍ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ғʀᴏᴍ ɪᴍᴅʙ sᴏᴜʀᴄᴇ
⪼ /search  - ɢᴇᴛ ᴛʜᴇ ғɪʟᴍ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ғʀᴏᴍ ᴠᴀʀɪᴏᴜs sᴏᴜʀᴄᴇs"""
    ADMIN_TXT = """ ʜᴇʟᴘ: <b>ᴀᴅᴍɪɴ</b>

<b>ɴᴏᴛᴇ:</b>
ᴛʜɪs ᴍᴏᴅᴜʟᴇ ᴏɴʟʏ ᴡᴏʀᴋs ғᴏʀ ᴍʏ ᴀᴅᴍɪɴs

<b>ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ :</b>
⪼ /logs - ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʀᴇsᴄᴇɴᴛ ᴇʀʀᴏʀs
⪼ /stats - ᴛᴏ ɢᴇᴛ sᴛᴀᴛᴜs ᴏғ ғɪʟᴇs ɪɴ ᴅʙ
⪼ /delete - ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ғɪʟᴇ ғʀᴏᴍ ᴅʙ
⪼ /users - ᴛᴏ ɢᴇᴛ ʟɪsᴛ ᴏғ ᴍʏ ᴜsᴇʀs ᴀɴᴅ ɪᴅs
⪼ /chats - ᴛᴏ ɢᴇᴛ ʟɪsᴛ ᴏғ ᴛʜᴇ ᴍʏ ᴄʜᴀᴛs ᴀɴᴅ ɪᴅs
⪼ /leave  - ᴛᴏ ʟᴇᴀᴠᴇ ғʀᴏᴍ ᴀ ᴄʜᴀᴛ
⪼ /disable  -  ᴅᴏ ᴅɪsᴀʙʟᴇ ᴀ ᴄʜᴀᴛ
⪼ /ban_user  - ᴛᴏ ʙᴀɴ ᴀ ᴜsᴇʀ
⪼ /unban_user  - ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴜsᴇʀ
⪼ /channel - ᴛᴏ ɢᴇᴛ ʟɪsᴛ ᴏғ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴄʜᴀɴɴᴇʟs
⪼ /broadcast - ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜsᴇʀs"""
    STATUS_TXT = """<b>᚛› ᴛᴏᴛᴀʟ ғɪʟᴇs: <code>{}</code></b>
<b>᚛› ᴛᴏᴛᴀʟ ᴜsᴇʀs: <code>{}</code></b>
<b>᚛› ᴛᴏᴛᴀʟ ᴄʜᴀᴛs: <code>{}</code></b>
<b>᚛› ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ: <code>{}</code> </b>
<b>᚛› ғʀᴇᴇ sᴛᴏʀᴀɢᴇ: <code>{}</code> </b>"""
    LOG_TEXT_G = """#ɴᴇᴡɢʀᴏᴜᴘ
    
<b>᚛› ɢʀᴏᴜᴘ ⪼ {}(<code>{}</code>)</b>
<b>᚛› ɢʀᴏᴜᴘʙɪᴅ ⪼ @{}
<b>᚛› ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀs ⪼ {}</b>
<b>᚛› ᴀᴅᴅᴇᴅ ʙʏ ⪼ {}</b>

By @{}
"""
    LOG_TEXT_P = """#ɴᴇᴡᴜsᴇʀ
    
<b>᚛› ɪᴅ - <code>{}</code></b>
<b>᚛› ɴᴀᴍᴇ - {}</b>
<b>᚛› ᴜɴ - @{}</b>

By @{}
"""
    REPORT_TXT = """➤ 𝐇𝐞𝐥𝐩: Rᴇᴘᴏʀᴛ ⚠️

𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚛𝚎𝚙𝚘𝚛𝚝 𝚊 𝚖𝚎𝚜𝚜𝚊𝚐𝚎 𝚘𝚛 𝚊 𝚞𝚜𝚎𝚛 𝚝𝚘 𝚝𝚑𝚎 𝚊𝚍𝚖𝚒𝚗𝚜 𝚘𝚏 𝚝𝚑𝚎 𝚛𝚎𝚜𝚙𝚎𝚌𝚝𝚒𝚟𝚎 𝚐𝚛𝚘𝚞𝚙. 𝙳𝚘𝚗'𝚝 𝚖𝚒𝚜𝚞𝚜𝚎 𝚝𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍.

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪/report 𝗈𝗋 @admins - 𝖳𝗈 𝗋𝖾𝗉𝗈𝗋𝗍 𝖺 𝗎𝗌𝖾𝗋 𝗍𝗈 𝗍𝗁𝖾 𝖺𝖽𝗆𝗂𝗇𝗌 (𝗋𝖾𝗉𝗅𝗒 𝗍𝗈 𝖺 𝗆𝖾𝗌𝗌𝖺𝗀𝖾)."""

    CORONA_TXT = """ʜᴇʟᴘ : ᴅʏɴᴏ

ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅs ʜᴇʟᴘs ʏᴏᴜ ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ʜᴇʀᴏᴋᴜ ᴅʏɴᴏ ᴀᴅᴍɪɴ ᴏɴʟʏ

⪼ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ:

⪼ /dyno - ᴛᴏ ɢᴇᴛ ʜᴇʀᴏᴋᴜ ᴅʏɴᴏ"""

    URLSHORT_TXT = """ʜᴇʟᴘ : <b> ᴜʀʟ sʜᴏʀᴛɴᴇʀ </b>

ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ʜᴇʟᴘs ʏᴏᴜ ᴛᴏ sʜᴏʀᴛ ᴀ ᴜʀʟ 

ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ :

⪼ /short - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜ ʏᴏᴜʀ ʟɪɴᴋ ᴛᴏ ɢᴇᴛ sʜᴏʀᴛᴇᴅ ʟɪɴᴋs,


⪼ 𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/short https://t.me/Crude_X</code>"""

    VIDEO_TXT ="""ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ

⪼ ᴜsᴀɢᴇ
ʏᴏᴜ ᴄᴀɴ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ ᴠɪᴅᴇᴏ ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ 

**ʜᴏᴡ ᴛᴏ ᴜsᴇ**
⪼ ᴛʏᴘᴇ /video or /mp4 ᴀɴᴅ (https://t.me/MalluHubGP)
⪼ ᴇxᴀᴍᴘʟᴇ:
<code>/mp4 https://xxxxxxxxxx</code>
<code>/video https://xxxxxxxxx</code>"""
    ZOMBIES_TXT = """𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝙺𝙸𝙲𝙺 𝚄𝚂𝙴𝚁𝚂

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
• /inkick - command with required arguments and i will kick members from group.
• /instatus - to check current status of chat member from group.
• /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
• /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
• /dkick - to kick deleted accounts."""

    IMAGE_TXT = """➤ 𝐇𝐞𝐥𝐩: Iᴍᴀɢᴇ

𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚎𝚍𝚒𝚝 𝚒𝚖𝚊𝚐𝚎 𝚟𝚎𝚛𝚢 𝚎𝚊𝚜𝚒𝚕𝚢 

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪ 𝖩𝗎𝗌𝗍 𝗌𝖾𝗇𝖽 𝗆𝖾 𝖺 𝗂𝗆𝖺𝗀𝖾 𝗍𝗈 𝖾𝖽𝗂𝗍 ✨

𝖬𝖺𝖽𝖾 𝖻𝗒 <a href=https://t.me/mr_MKN>Mr.MKN TG</a>"""

    STICKER_TXT = """ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴍᴏᴅᴜʟᴇ ᴛᴏ ғɪɴᴅ ᴀɴʏ sᴛɪᴄᴋᴇʀs ɪᴅ
⪼ ᴜsᴀɢᴇ
ᴛᴏ ɢᴇᴛ sᴛɪᴄᴋᴇᴛ ɪᴅ
 
  ʜᴏᴡ ᴛᴏ ᴜsᴇ
 
⪼ ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ sᴛɪᴄᴋᴇʀ /stickerid"""
    YTTHUMB_TXT = """𝙷𝙴𝙻𝙿𝚂 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙰𝙽𝚈 𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝚅𝙸𝙳𝙴𝙾 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻
    
⭕𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
𝘛𝘺𝘱𝘦 /ytthumb 𝘈𝘯𝘥 𝘝𝘪𝘥𝘦𝘰 𝘓𝘪𝘯𝘬

• 𝘌𝘹𝘢𝘮𝘱𝘭𝘦
<code>/ytthumb https://youtu.xxxxxxx</code>"""

    ABOOK_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖠𝗎𝖽𝗂𝗈𝖻𝗈𝗈𝗄

𝚈𝚘𝚞 𝚌𝚊𝚗 𝚌𝚘𝚗𝚟𝚎𝚛𝚝 𝚊 𝙿𝙳𝙵 𝚏𝚒𝚕𝚎 𝚝𝚘 𝚊 𝚊𝚞𝚍𝚒𝚘 𝚏𝚒𝚕𝚎 𝚠𝚒𝚝𝚑 𝚝𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 ✯

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪ /audiobook: 𝖱𝖾𝗉𝗅𝗒 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗍𝗈 𝖺𝗇𝗒 𝖯𝖣𝖥 𝗍𝗈 𝗀𝖾𝗇𝖾𝗋𝖺𝗍𝖾 𝗍𝗁𝖾 𝖺𝗎𝖽𝗂𝗈"""

    GTRANS_TXT = """ʜᴇʟᴘ : <b>ɢᴏᴏɢʟᴇ ᴛʀᴀɴsʟᴀᴛᴇʀ</b>

ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ʜᴇʟᴘs ʏᴏᴜ ᴛᴏ ᴛʀᴀɴsʟᴀᴛᴇ ᴀ ᴛᴇxᴛ ᴛᴏ ᴀɴʏ ʟᴀɴɢᴜᴀɢᴇs ʏᴏᴜ ᴡᴀɴᴛ. ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡᴏʀᴋs ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ

ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ :

⪼ /tr - ᴛᴏ ᴛʀᴀɴsʟᴀᴛᴇʀ ᴛᴇxᴛs ᴛᴏ ᴀ sᴘᴇᴄɪғᴄ ʟᴀɴɢᴜᴀɢᴇ

⪼ ɴᴏᴛᴇ :
ᴡʜɪʟᴇ ᴜsɪɴɢ /tr ʏᴏᴜ sʜᴏᴜʟᴅ sᴘᴇᴄɪғʏ ᴛʜᴇ ʟᴀɴɢᴜᴀɢᴇ ᴄᴏᴅᴇ

⪼ ᴇxᴀᴍᴘʟᴇ : /𝗍𝗋 𝗆𝗅
• 𝖾𝗇 = ᴇɴɢʟɪsʜ
• 𝗆𝗅 = ᴍᴀʟᴀʏᴀʟᴀᴍ
• 𝗁𝗂 = ʜɪɴᴅɪ"""

    RESTRIC_TXT = """➤ 𝐇𝐞𝐥𝐩: Mᴜᴛᴇ 🚫

𝚃𝚑𝚎𝚜𝚎 𝚊𝚛𝚎 𝚝𝚑𝚎 𝚌𝚘𝚖𝚖𝚊𝚗𝚍𝚜 𝚊 𝚐𝚛𝚘𝚞𝚙 𝚊𝚍𝚖𝚒𝚗 𝚌𝚊𝚗 𝚞𝚜𝚎 𝚝𝚘 𝚖𝚊𝚗𝚊𝚐𝚎 𝚝𝚑𝚎𝚒𝚛 𝚐𝚛𝚘𝚞𝚙 𝚖𝚘𝚛𝚎 𝚎𝚏𝚏𝚒𝚌𝚒𝚎𝚗𝚝𝚕𝚢.

➪/ban: 𝖳𝗈 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝖿𝗋𝗈𝗆 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/unban: 𝖳𝗈 𝗎𝗇𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/tban: 𝖳𝗈 𝗍𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋.
➪/mute: 𝖳𝗈 𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/unmute: 𝖳𝗈 𝗎𝗇𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/tmute: 𝖳𝗈 𝗍𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋.

➤ 𝖭𝗈𝗍𝖾:
𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tmute 𝗈𝗋 /tban 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗍𝗂𝗆𝖾 𝗅𝗂𝗆𝗂𝗍.

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝖻𝖺𝗇 2𝖽 𝗈𝗋 /𝗍𝗆𝗎𝗍𝖾 2𝖽.
𝖸𝗈𝗎 𝖼𝖺𝗇 𝗎𝗌𝖾 𝗏𝖺𝗅𝗎𝖾𝗌: 𝗆/𝗁/𝖽. 
 • 𝗆 = 𝗆𝗂𝗇𝗎𝗍𝖾𝗌
 • 𝗁 = 𝗁𝗈𝗎𝗋𝗌
 • 𝖽 = 𝖽𝖺𝗒𝗌"""
    CREATOR_REQUIRED = """❗<b>You have To Be The Group Creator To Do That.</b>"""
      
    INPUT_REQUIRED = "❗ **Arguments Required**"
      
    KICKED = """✔️ Successfully Kicked {} Members According To The Arguments Provided."""
      
    START_KICK = """🚮 Removing Inactive Members This May Take A While..."""
      
    ADMIN_REQUIRED = """❗<b>എന്നെ Admin ആക്കത്ത സ്ഥലത്ത് ഞാൻ നിക്കില്ല പോകുവാ Bii..Add Me Again with all admin rights.</b>"""
      
    DKICK = """✔️ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """<b>ഇപ്പൊ എല്ലാം അടിച്ചുമാറ്റി തരാം...</b>"""
      
    STATUS = """{}\n<b>Chat Member Status</b>**\n\n```<i>Recently``` - {}\n```Within Week``` - {}\n```Within Month``` - {}\n```Long Time Ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}</i>
"""
    CARB_TXT = """☾︎𝗛𝗘𝗟𝗣 𝗙𝗢𝗥 𝗖𝗔𝗥𝗕𝗢𝗡☽︎
𝙲𝙰𝚁𝙱𝙾𝙽 𝙸𝚂 𝙰 𝙵𝙴𝚄𝚃𝚄𝚁𝙴 𝚃𝙾 𝙼𝙰𝙺𝙴 𝚃𝙷𝙴 𝙸𝙼𝙰𝙶𝙴 𝙰𝚂 𝚂𝙷𝙾𝚆𝙽 𝙸𝙽 𝚃𝙷𝙴 𝚃𝙾𝙿 𝚆𝙸𝚃𝙷 𝚈𝙾𝚄𝚁𝙴 𝚃𝙴𝚇𝚃𝚂.
𝙵𝙾𝚁 𝚄𝚂𝙸𝙽𝙶 𝚃𝙷𝙴 𝙼𝙾𝙳𝚄𝙻𝙴 𝙹𝚄𝚂𝚃 𝚂𝙴𝙽𝙳 𝚃𝙷𝙴 𝚃𝙴𝚇𝚃 𝙰𝙽𝙳 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙸𝚃 𝚆𝙸𝚃𝙷 /carbon 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝚃𝙷𝙴 𝙱𝙾𝚃 𝚆𝙸𝙻𝙻 𝚁𝙴𝙿𝙻𝚈 𝚆𝙸𝚃𝙷 𝚃𝙷𝙴 𝙲𝙰𝚁𝙱𝙾𝙽 𝙸𝙼𝙰𝙶𝙴
"""

    FOND_TXT = """ʜᴇʟᴘ : ғᴏɴᴛ
ғᴏɴᴛ ɪs ᴀ ᴍᴏᴅᴜʟᴇ ғᴏʀ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴛᴇxᴛ sᴛʏʟɪsʜ
ғᴏʀ ᴜsᴇ ᴛʜᴀᴛ ғᴇᴜᴛᴜʀᴇ ᴛʏᴘᴇ /font <your text> ᴛʜᴇɴ ʏᴏᴜʀ ᴛᴇxᴛ ɪs ʀᴇᴀᴅʏ"""

    

