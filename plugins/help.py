from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Bot ini dapat membantu anda untuk mengunduh video/audio dari YouTube,untuk saat ini Hanya mendukung Youtube Single  (Bukan playlist).Cukup Kirimkan Url dari Youtube"
    await message.reply_text(helptxt)
