from .. import Riz, SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
    
HELP_PIC = "https://te.legra.ph/file/8f38c2a68e7a4c2e3f6c9.jpg"

Riz_Help = "🔥 𝗣𝗥𝗢𝗙𝗘𝗦𝗦𝗢𝗥 𝗦𝗣𝗔𝗠𝗦𝗧𝗘𝗥𝗦 🔥\n\n"
 
Riz_Help += f"__ᴄᴍᴅs ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ʀɪᴢᴏᴇʟ x sᴘᴀᴍ__\n\n"

Riz_Help += f" ↧ 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙲𝙼𝙳𝚂 ↧\n\n"

Riz_Help += f" `.ping` - to check ping\n `.alive` - to check bot alive/version (only main userbot will reply)\n .`restart` - to restart all spam bots\n\n"
 
Riz_Help += f" ↧ 𝙻𝙴𝙰𝚅𝙴 𝙲𝙼𝙳 ↧\n\n"

Riz_Help += f" `.leave` - to leave public/private channel/groups\n\n"
 
Riz_Help += f" ↧ 𝚂𝙿𝙰𝙼 𝙲𝙼𝙳𝚂 ↧\n\n"

Riz_Help += f" `.raid` - to raid\n `.replyraid` - to active reply raid\n `.dreplyraid` - to de-active reply raid\n `.spam` - this cmd use for Normal spam\n `.bigspam` - this cmd use for big spam\n `.uspam` - this cmd use for unlimited Spam until You restart the bots!!\n `.delayspam` - this cmd use for delay spam\n\n"
 
Riz_Help += f"ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏ.\n\n"

Riz_Help += f"© @Agoraswamy_Professor | @Agora_Spam_Official\n"


@Riz.on(events.NewMessage(pattern=".help"))
async def help(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=Riz_Help,
                                  buttons=[
        [
        Button.url("ᴀʟʟ ᴄᴍᴅs", "https://te.legra.ph/%F0%9D%97%A3%F0%9D%97%A5%F0%9D%97%A2%F0%9D%97%99%F0%9D%97%98%F0%9D%97%A6%F0%9D%97%A6%F0%9D%97%A2%F0%9D%97%A5-%F0%9D%97%A6%F0%9D%97%A3%F0%9D%97%94%F0%9D%97%A0%F0%9D%97%A6%F0%9D%97%A7%F0%9D%97%98%F0%9D%97%A5%F0%9D%97%A6-01-22"
        ],
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/Agoraswamy_Professor")
        ] 
        ]
        )                                                         
