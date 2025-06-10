from telethon import TelegramClient, events
from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument

api_id = 24434188
api_hash = '1383c40a8af22a2a0ca3abdba62c9c19'

source_channel = 'agdsizbxh'
target_channels = ['channel_bcto', 'channelc_cto']

client = TelegramClient('copybot_user', api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def forward_post(event):
    for target in target_channels:
        try:
            if event.message.media:
                await client.send_file(target, event.message.media, caption=event.message.text or "")
            else:
                await client.send_message(target, event.message.text)
            print(f"✅ Sent to {target}")
        except Exception as e:
            print(f"Error sending to {target}: {e}")

client.start()
print("📡 Listening for messages...")
client.run_until_disconnected()
