import http.client
import json
import time

with open('./config.json') as f:
    config_data = json.load(f)
    channel_id = config_data['Config'][0]['channelid']
    token = config_data['Config'][0]['token']
    message = config_data['Config'][0]['message']

header_data = {"Content-Type": "application/json", "User-Agent": "DiscordBot", "Authorization": token}

def get_connection():
    return http.client.HTTPSConnection("discord.com", 443)

def send_message(conn, channel_id, message_data, count):
    try:
        conn.request("POST", f"/api/v10/channels/{channel_id}/messages", message_data, header_data)
        resp = conn.getresponse()
        if 199 < resp.status < 300:
            print(f"Message {count} Sent.")
        else:
            print(f"HTTP {resp.status}: {resp.reason}")
    except:
        print("Error.")

def main():
    message_data = {"content": message, "tts": False}
    send_message(get_connection(), channel_id, json.dumps(message_data), main.count)
    main.count += 1

if __name__ == '__main__':
    main.count = 1
    while True:
        main()
        time.sleep(2)  # Change The Wait Time i did 2s because im grinding message and to avoid soft ban
