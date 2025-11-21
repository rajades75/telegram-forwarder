import asyncio
from datetime import datetime
from telethon import TelegramClient, events

# === CONFIGURATION ===
api_id = 20652662
api_hash = "22b91e5c11d32a3f0762ee3f25c7a1ee"
session_name = "render_session"   # fichier déjà uploadé !

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
        print(f"[{now}] ✅ Transféré depuis {event.chat_id} → {DEST_CHANNEL}")

    except Exception as e:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{now}] ⚠️ Erreur : {e}")

async def main():
    print("🚀 Render démarre…")

    # Démarre directement sans demander de code
    await client.start()

    print("🎉 Connecté — relay en fonctionnement")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
