from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from InflexMusic import app

@app.on_message(filters.command("rm") & (filters.private | filters.group))
async def rm_handler(client, message):
    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🧑‍💻 Owner", url="https://t.me/CwaX7")],
            [InlineKeyboardButton("✅ Rəsmi Bot", url="https://t.me/RespublicMusicBot")],
            [InlineKeyboardButton("🚀 Yaradıcı Support", url="https://t.me/RespublicSupport")],
            [InlineKeyboardButton("🥷 Yaradıcı", url="https://t.me/RespublicOwner")],
        ]
    )

    text = "🎧 <b>Musiqi botunun reposu haqqında məlumat 🚀</b>"
    await message.reply(text, reply_markup=buttons, parse_mode=ParseMode.HTML)
