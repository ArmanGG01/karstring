from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("👑 Mulai Membuat string 👑", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🗿 Kembali Ke Awal 🗿", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("📥 Ini Grup ku  📥", url="https://t.me/obrolansuar")],
        [
            InlineKeyboardButton("Cara Pakeknya ❔", callback_data="help"),
            InlineKeyboardButton("📌 Apa Masalah Kau 📌", callback_data="about")
        ],
        [InlineKeyboardButton("🤖 Daftar Repo Bot 🤖", url="https://t.me/Karc0de")],
    ]

    START = """
𝙷𝙰𝙻𝙾 {}
𝚂𝙴𝙻𝙰𝙼𝙰𝚃 𝙳𝙰𝚃𝙰𝙽𝙶 𝙳𝙸 {}
𝙺𝙰𝙻𝙾 𝙺𝙰𝚄 𝙶𝙰𝙺 𝙿𝙴𝚁𝙲𝙰𝚈𝙰 𝚂𝙰𝙼𝙰 𝙱𝙾𝚃 𝙸𝙽𝙸, 
1) 𝙶𝙰𝚄𝚂𝙰𝙷 𝙱𝙰𝙲𝙰 𝙿𝙴𝚂𝙰𝙽 𝙸𝙽𝙸 𝙺𝙾𝙽𝚃𝙾𝙻
2) 𝙱𝙻𝙾𝙺𝙸𝚁 𝙱𝙾𝚃 𝙰𝚃𝙰𝚄 𝙳𝙴𝙻𝙰𝚃𝙴 𝙲𝙷𝙰𝚃 𝙼𝙴𝙼𝙴𝙺
Bot ini Bekerja Untuk Membantu Kamu Mendapatkan String Session Via Bot. Rekomendasi Jika Ingin Mengambil String Gunakan Akun Lain, Agar Tidak Delay. Terimakasih

By @Karc0de
    """

    HELP = """
✨ **Available Commands** ✨

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Generate Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    ABOUT = """
**About This Bot** 

Telegram Bot to generate Pyrogram and Telethon string session by @StarkBots

Source Code : [Click Here](https://github.com/ArmanGG01/karstring)

Framework : [Pyrogram](https://docs.pyrogram.org)

Language : [Python](https://www.python.org)

Developer : @PakkPoll
    """
