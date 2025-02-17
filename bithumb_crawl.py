from bs4 import BeautifulSoup
import time
import cloudscraper
import time
from datetime import datetime
import re
import requests

test_html = """
<!DOCTYPE html>
<html lang="ko">

<head>
"""

notify_group_token = "JyBbcigUcucMOgPud1qwmyIkDd5orgtN0SsZkm9Kdvd"

def send_message_to_notify(message):
    headers = {"Authorization": f"Bearer {notify_group_token}"}
    data = {"message": message}
    requests.post("https://notify-api.line.me/api/notify", headers=headers, data=data)


def parse(html_content, key_word):
    past_time = time.time()
    

    # Find the first item with class 'NoticeContentList_notice-list__link__LAkAV'
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all <a> tags with the class containing "NoticeContentList_notice-list__link__LAkAV"
    all_items = soup.find_all('a', class_='NoticeContentList_notice-list__link__LAkAV')

    # Now filter them by checking the class exactly matches the one you're looking for
    # Iterate through the found items and return the first one with the correct class
    first_item = None
    for item in all_items:
        if len(item.get('class', [])) == 1:
            first_item = item
            break

    previos_coin = ""
    if first_item:
        # Check if the category is "마켓 추가"
        category = first_item.find('span', class_='NoticeContentList_notice-list__category__cBqMf').text
        if  key_word in category:
            # Extract the title
            title = first_item.find('span', class_='NoticeContentList_notice-list__link-title__nlmSC').text
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Found '마켓 추가': {title} at {current_time}")
             # Parse the market name (i.e., "THE" from "테나(THE) 원화 마켓 추가")
            market_name_match = re.search(r'\((.*?)\)', title)
            if market_name_match:
                coin_name = market_name_match.group(1)
                if coin_name != previos_coin:
                    send_message_to_notify(f"爬蟲監測bithumb 上幣: {coin_name}")
                    print(f"Coin Name: {coin_name}") 
                previos_coin = coin_name
            else:
                print("Coin Name not found.")
        else:
            print("The first item is not '마켓 추가'.")
        
        # Measure time elapsed
    # time_elapse = time.time() - past_time
    # print(f"time cost: {time_elapse}")
    
upcoin_keyword = "마켓 추가"

def main():
    URL = "https://feed.bithumb.com/notice"

    # Set up headers to mimic a real browser
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
    }

    # Define the proxy list (replace with actual proxy IP & port)
    # Define the proxy (replace with a real proxy IP & port)
    proxies = [
        {"http": "http://23.82.137.161:80"},   # Replace with actual proxy IP & port
        {"http": "http://203.57.51.53:80"},
        {"http": "http://188.166.56.246:80"},
        {"http": "http://146.83.216.227:80"},
        {"http": "http://8.220.205.172:5060"},
        {"http": "http://159.54.187.233:8080"},
        {"http": "http://146.83.216.227:80"},
        {"http": "http://3.124.133.93:3128"},
        {"http": "http://34.135.166.24:80"},
        {"http": "http://202.61.204.51:80"}
    ]

    # Create a scraper session
    scraper = cloudscraper.create_scraper()
    interval = 0.8  # 1 second interval

    # Loop through proxies
    past_time = time.time()
    while True:
        for proxy in proxies:
            try:
                # Make the request using the current proxy
                response = scraper.get(URL, headers=headers, proxies = proxy)

                # Print the status code and latency for each request
                # print(f"Status Code: {response.status_code}")

                # Print response text if successful (optional)
                if response.status_code == 200:
                    html_content = response.text
                    parse(html_content, key_word="마켓 추가")
                else:
                    print(response)
                    print(response.headers)
                    print(response.text)
                # print(f"Latency: {time.time() - past_time:.3f} seconds")
                past_time = time.time()
            except Exception as e:
                print(f"Error with proxy: {e}")

            # Wait for the next request (1 second) before continuing to the next proxy
            time.sleep(interval)
            break
        break

if __name__ == "__main__":
    print("test")
    main()
        