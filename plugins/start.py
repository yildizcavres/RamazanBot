# CODED BY :d

import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command('start'))
async def start(bot, message):
    name = message.from_user.first_name
    url = "https://t.me/Kelebekfedkurucuu"
    text = f"Merhaba {name}\n\nBu bot sayesinde yașadığın yerdeki iftar ve sahur saatlerini ve ne kadar kaldığını öğrenebilirsin 😁.\n\n`/sahur Ankara mamak`\n`/iftar Ankara mamak`\n\nHayırlı Ramazanlar [:Destek]({url})"
    photo = ""
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo, 
        caption=text, 
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"Beni Yapan Mübarek ", url="https://t.me/Nazaramigeldikdersin")]]))
        
