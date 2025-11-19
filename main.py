import asyncio 
import os
from datetime import datetime
from telethon import TelegramClient, events

# === CONFIGURATION ===
api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
session_name = 'render_session'

# Liste des canaux sources
SOURCE_CHANNELS = [
    -1003106567056,
    -1002251762728,
    -1002412715536,
]

# Canal de destination
DEST_CHANNEL = -1003232935717

client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage(chats=SOURCE_CHANNELS))
async def handler(event):
    try:
        if event.out:
            return

        await client.forward_messages(DEST_CHANNEL, event.message)

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{now}] ✅ Message transféré depuis {event.chat_id} → {DEST_CHANNEL}")

    except Exception as e:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{now}] ⚠️ Erreur : {e}")

async def main():
    print("🚀 Démarrage Render…")

    phone = os.environ.get("TG_PHONE")
    code = os.environ.get("TG_CODE")   # Pour la toute première connexion seulement

    if not phone:
        raise Exception("❌ TG_PHONE manquant dans Render")

    await client.start(
        phone=phone,
        code_callback=lambda: code
    )

    print("🎉 Render connecté — bot opérationnel")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())

