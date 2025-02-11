from telethon import TelegramClient, events
import requests
import json
import tweepy
from datetime import datetime

# 🔹 你的 Telegram API ID & Hash（從 my.telegram.org 獲取）
api_id = "21126131"
api_hash = "ecf27e18d7e360b0ae698bc99a92d9fe"
# 🔹 監聽的 Telegram 頻道用戶名（例如 @yourchannel）
bwe_telegram_channel = "@BWEnews"
bithumb_telegram_channel = "@BithumbExchange"

twitter_bear_token = "AAAAAAAAAAAAAAAAAAAAAFVCywEAAAAAtp%2F%2B8o0ymg1MY7T0ewdqxcHIX20%3DiVLMk5y1v6mNb8gUcTF3ZsxVbExCZQlbI3sPN8fBZzwp9wwf0e"      # Twitter API Bearer Token
twitter_target_username = "bwenews" # 目標 Twitter 帳號（例如：elonmusk，不含 @）


# 初始化 Telegram 客戶端
client = TelegramClient("session_name", api_id, api_hash)
# 🔹 你的 Telegram 電話號碼（用來登入）
phone_number = "+886930704917"



# for line 官方帳號
channel_access_token = "W1IoWOAaemIvU/goJfrBpYI+5hqifav/tpVlSWcCR6BpGrC7jJfXsQRiDf3r2CB0l+EG4jXHsY91wCW+MMU/kJAzc+yPY2KO56aoyfcG+m6GOqY6k/DaciEe2tS+h14rO9c0F+2ha/QJ0smo3o3haQdB04t89/1O/w1cDnyilFU="  # Replace with your Channel Access Token
notify_group_token = "JyBbcigUcucMOgPud1qwmyIkDd5orgtN0SsZkm9Kdvd"


import json

def send_message_to_notify(message):
    headers = {"Authorization": f"Bearer {notify_group_token}"}
    data = {"message": message}
    requests.post("https://notify-api.line.me/api/notify", headers=headers, data=data)


def send_broadcast_message(channel_access_token, message):
    url = "https://api.line.me/v2/bot/message/broadcast"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {channel_access_token}"
    }
    
    # 設置發送的訊息
    payload = {
        "messages": [
            {
                "type": "text",
                "text": message
            }
        ]
    }
    
    # 發送請求到 LINE API
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    # 顯示回應結果
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")


# 當有新訊息時觸發
@client.on(events.NewMessage(chats=bwe_telegram_channel))
async def handler(event):
    pre_message = event.message.message  # 取得訊息內容
    message = f"From bwe: \n {datetime.now()} \n {pre_message}"
    send_message_to_notify(message)
    send_broadcast_message(channel_access_token, message)
    
@client.on(events.NewMessage(chats=bithumb_telegram_channel))
async def handler(event):
    pre_message = event.message.message  # 取得訊息內容
    message = f"From bithumb: \n {datetime.now()} \n {pre_message}"
    send_message_to_notify(message)
    

# def twitter_process():
#     # 建立 Client 取得目標使用者資訊，並取得其 user id
#     client = tweepy.Client(bearer_token=twitter_bear_token)
#     user_response = client.get_user(username=twitter_target_username)
#     if user_response.data is None:
#         print("找不到用戶:", twitter_target_username)
#         return
#     target_user_id = str(user_response.data.id)
#     print(f"目標用戶 {twitter_target_username} 的 user id：{target_user_id}")

#     # 初始化 Streaming Client
#     stream = MyTweetStream(bearer_token=twitter_bear_token, target_user_id=target_user_id)
    
#     # 清除現有規則（若有的話）
#     current_rules = stream.get_rules().data
#     if current_rules is not None:
#         rule_ids = [rule.id for rule in current_rules]
#         stream.delete_rules(rule_ids)
    
#     # 新增規則：監控來自 TARGET_USERNAME 的貼文
#     # 這裡的規則使用 "from:帳號名稱" 進行過濾
#     rule_value = f"from:{twitter_target_username}"
#     stream.add_rules(tweepy.StreamRule(value=rule_value, tag="target_user_rule"))
#     print(f"已新增監聽規則：{rule_value}")
    
#     # 開始過濾資料流，並要求附帶作者資訊
#     print("開始監聽貼文，等待新貼文中...")
#     stream.filter(tweet_fields=["author_id", "created_at"])

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