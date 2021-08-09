from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"🤗Currently Only supports Youtube Single  (No playlist) Just Send Youtube Url🤓 🤡 **You Can youtube video links 🗣️search using @bidd inline mode🤗**   ❤️❤️A Bot By @omindas"
    await message.reply_text(helptxt)
