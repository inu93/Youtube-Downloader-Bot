from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/katakatauntukmu")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/ebnudoang")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help untuk info lebih lanjut"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
