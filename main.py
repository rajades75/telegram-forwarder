import asyncio
from datetime import datetime
from telethon import TelegramClient, events

# === CONFIGURATION ===
api_id = 20652662  # ton api_id doit être un entier, pas une chaîne
api_hash = '22b91e5c11d32a3f0762ee3f25c7a1ee'
session_name = 'my_session2'

# Liste des canaux sources
SOURCE_CHANNELS = [
    -1003106567056,  # canal source 1
    -1002251762728,  # canal source 1
    -1002412715536,  # canal source 2
]

# Canal de destination
DEST_CHANNEL = -1003232935717

# === INITIALISATION ===
client = TelegramClient(session_name, api_id, api_hash)

# === ÉCOUTE DES NOUVEAUX MESSAGES SUR LES CANAUX SOURCES ===
@client.on(events.NewMessage(chats=SOURCE_CHANNELS))
async def handler(event):
    try:
        # ignore les messages envoyés par toi-même (évite les boucles)
        if event.out:
            return
        
        # transfère le message vers le canal de destination
        await client.forward_messages(DEST_CHANNEL, event.message)
        
        # récupère la date et heure actuelle
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # affiche avec timestamp
        print(f"[{now}] ✅ Message transféré depuis {event.chat_id} → {DEST_CHANNEL}")

    except Exception as e:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{now}] ⚠️ Erreur lors du transfert : {e}")

# === LANCEMENT DU CLIENT ===
async def main():
    await client.start()
    print("🚀 Bot démarré — en attente de nouveaux messages...")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())