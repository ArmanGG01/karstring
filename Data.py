from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
𝙷𝙰𝙻𝙾 {}

𝚂𝙴𝙻𝙰𝙼𝙰𝚃 𝙳𝙰𝚃𝙰𝙽𝙶 𝙳𝙸 {}

𝙺𝙰𝙻𝙾 𝙺𝙰𝚄 𝙶𝙰𝙺 𝙿𝙴𝚁𝙲𝙰𝚈𝙰 𝚂𝙰𝙼𝙰 𝙱𝙾𝚃 𝙸𝙽𝙸, 
1) 𝙶𝙰𝚄𝚂𝙰𝙷 𝙱𝙰𝙲𝙰 𝙿𝙴𝚂𝙰𝙽 𝙸𝙽𝙸 𝙺𝙾𝙽𝚃𝙾𝙻
2) 𝙱𝙻𝙾𝙺𝙸𝚁 𝙱𝙾𝚃 𝙰𝚃𝙰𝚄 𝙳𝙴𝙻𝙰𝚃𝙴 𝙲𝙷𝙰𝚃 𝙼𝙴𝙼𝙴𝙺

Bot ini Bekerja Untuk Membantu Kamu Mendapatkan String Session Via Bot. Rekomendasi Jika Ingin Mengambil String Gunakan Akun Lain, Agar Tidak Delay. Terimakasih
By @PakkPoll
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ​", callback_data="generate")],
        [InlineKeyboardButton(text="ʙᴀᴄᴋ​", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ", callback_data="generate")],
        [InlineKeyboardButton("ᴍᴀɪɴᴛᴀɴᴇᴅ ʙʏ​", url="https://t.me/PakkPoll")],
        [
            InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ​​", callback_data="help"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ​", callback_data="about")
        ],
        [InlineKeyboardButton("ɪɴꜰᴏ ʙᴏᴛ ʟᴀɪɴɴʏᴀ​", url="https://t.me/DeployBot01")],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - Tentang Bot ini
/help - This Message
/start - Mulai Bot
/generate - Mulai Generating Session
/cancel - Membatalkan process
/restart - Membatalkan process
"""

    # About Message
    ABOUT = """
**About This Bot** 

Sebuah telegram bot untuk mengambil pyrogram dan telethon string session by @karstring_bot

Group Support : [Gabung](https://t.me/obrolansuar)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @PakkPoll
    """
