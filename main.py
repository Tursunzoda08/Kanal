import asyncio
from telethon import TelegramClient, events
import logging
import os

logging.basicConfig(level=logging.INFO)

# Ma'lumotlar
API_ID = '28240646'
API_HASH = 'ce9e1c38b6292318cbe1e7424d01ef57'
PHONE = '+998916455826'

SOURCE_CHANNELS = [
    'gorizont_uz',
    'azizhalikov', 
    'https://t.me/+eA4oGrRq1tU0YTFi',
    'https://t.me/+YnpPTGKcW_JhZGNi',
    'Sardorbekningkanali2'
]
TARGET_CHANNEL = 'Sardorbekningkanali'

async def main():
    client = TelegramClient('session', API_ID, API_HASH)
    await client.start(phone=PHONE)
    
    logging.info("Bot ishlayapti!")
    
    target = await client.get_entity(TARGET_CHANNEL)
    source_chats = []
    
    for channel in SOURCE_CHANNELS:
        try:
            entity = await client.get_entity(channel)
            source_chats.append(entity)
            logging.info(f"Kuzatilmoqda: {entity.title}")
        except:
            pass
    
    @client.on(events.NewMessage(chats=source_chats))
    async def handler(event):
        try:
            await client.forward_messages(target, event.message)
            logging.info("✅ Forward qilindi")
        except:
            try:
                await client.send_message(target, event.message.text)
                logging.info("✅ Nusxa qilindi")
            except:
                pass
    
    await client.run_until_disconnected()

asyncio.run(main())
