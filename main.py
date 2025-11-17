import asyncio
import os
from datetime import datetime
from telethon import TelegramClient, events

# --- VARIABLES RENDER ---
api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]

# Facultatif pour Render (uniquement si la session n'existe pas encore)
tg_phone = os.environ.get("TG_PHONE")
tg_code = os.environ.get("TG_CODE")

session_name = "session"

# --- CONFIG ---
SOURCE_CHANNELS = [
    -1003106567056,
    -1002251762728,
    -1002412715536,
]

DEST_CHANNEL = -1003232935717

client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage(chats=SOURCE_CHANNELS))
async def handler(event):
    try:
        if event.out:
            return

        await client.forward_messages(DEST_CHANNEL, event.message)

        print(f"{datetime.now()} - Message transféré depuis {event.chat_id}")
    except Exception as e:
        print(f"{datetime.now()} - Erreur : {e}")

async def main():
    print("Démarrage...")

    # 🔥 Si TG_PHONE et TG_CODE sont présents → login automatique
    if tg_phone and tg_code:
        await client.start(phone=tg_phone, code_callback=lambda: tg_code)
    else:
        # 🔥 Si la session existe déjà → pas besoin de phone/code
        await client.start()

    print("Bot actif.")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
