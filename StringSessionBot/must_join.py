from env import MUST_JOIN
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = f"https://t.me/{MUST_JOIN}"
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"𝙺𝙰𝚄 𝙹𝙾𝙸𝙽 𝙳𝚄𝙻𝚄 [GROUP KU]({link}) 𝚄𝙽𝚃𝚄𝙺 𝙼𝙰𝙺𝙴𝙺 𝙱𝙾𝚃 𝙺𝚄. 𝙰𝙱𝙸𝚂 𝙹𝙾𝙸𝙽 𝙱𝙰𝚁𝚄 𝙲𝙾𝙱𝙰𝙺 𝙻𝙰𝙶𝙸 /start",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ​", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I'm not admin in the MUST_JOIN chat : {MUST_JOIN} !")
