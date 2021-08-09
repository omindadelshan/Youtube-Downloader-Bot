from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔥Channel🔥", url="https://t.me/sdprojectupdates")],
        [InlineKeyboardButton(
            "👨‍💻 Developer 👨‍💻", url="https://t.me/omindas")]
    ])
    welcomed = f"👨‍💻Hey <b>{message.from_user.first_name}</b>\n/💎 I Am Powerfull Telegram youtube video downloader bo 🤓 Please send youtube video url link nto me.. i Am send video ✳️✳️ Sea more help ❤️ send A /help command or cick a  help Butto🎈🔥"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
