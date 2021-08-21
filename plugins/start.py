from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("⚡Add Me To Your Group⚡", url="https://t.me/YT_Downloader_SD_Bot?startgroup=true")],
        [InlineKeyboardButton(
            "🎈Update Channal🎈", url="https://t.me/sdprojectupdates")]
        [InlineKeyboardButton(
            "🎈Update Group 🎈" , url="https://t.me/sdbotworld")]
    ])
    welcomed = "👋Hello <b>{message.from_user.first_name}</b>\n/

You are Warmly welcome to @YT_Downloader_SD_Bot 🇱🇰

If you want to know how i works just hit on /help command 🙂"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
