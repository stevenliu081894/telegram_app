from telethon import TelegramClient, events
import requests
import json

# 🔹 你的 Telegram API ID & Hash（從 my.telegram.org 獲取）
api_id = "21126131"
api_hash = "ecf27e18d7e360b0ae698bc99a92d9fe"

# 🔹 你的 Telegram 電話號碼（用來登入）
phone_number = "+886930704917"

channel_access_token = "W1IoWOAaemIvU/goJfrBpYI+5hqifav/tpVlSWcCR6BpGrC7jJfXsQRiDf3r2CB0l+EG4jXHsY91wCW+MMU/kJAzc+yPY2KO56aoyfcG+m6GOqY6k/DaciEe2tS+h14rO9c0F+2ha/QJ0smo3o3haQdB04t89/1O/w1cDnyilFU="  # Replace with your Channel Access Token
user_id = "U41a8702d9d4455adec6737ca0782f805"  # The user or group ID you want to send the message to

# 🔹 監聽的 Telegram 頻道用戶名（例如 @yourchannel）
telegram_channel = "@BWEnews"

# 初始化 Telegram 客戶端
client = TelegramClient("session_name", api_id, api_hash)

# 發送訊息到 LINE Notify
def send_message_to_line_channel(channel_access_token, user_id, message):
    url = "https://api.line.me/v2/bot/message/push"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {channel_access_token}"
    }
    
    # Prepare the payload for sending the message
    print(user_id)
    payload = {
        "to": user_id,  # The user ID to send the message to
        "messages": [
            {
                "type": "text",
                "text": message
            }
        ]
    }
    
    # Send POST request to Line API
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    # Check the response
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")

# 當有新訊息時觸發
@client.on(events.NewMessage(chats=telegram_channel))
async def handler(event):
    message = event.message.message  # 取得訊息內容
    print(f"📩 收到新訊息：\n {message}")
    send_message_to_line_channel(channel_access_token, user_id, f"Telegram 頻道新訊息：{message}")
    
import asyncio
async def main():
    await client.start(phone_number)
    print("正在監聽 Telegram 頻道訊息...")
    await client.run_until_disconnected()  # 一直監聽直到中斷

# 修改為檢查是否已有事件循環運行
def run():
    loop = asyncio.get_event_loop()
    if loop.is_running():
        print("事件循環已經在運行中...")
        # 若事件循環已運行，使用以下方式來啟動 Telegram 客戶端
        loop.create_task(main())
    else:
        # 若沒有事件循環，則創建並運行
        loop.run_until_complete(main())

run()