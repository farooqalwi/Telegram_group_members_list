import configparser
import os
import json
from telethon import TelegramClient



# telegram development credentials in telegram API Development Tools
config = configparser.ConfigParser()

if not os.path.exists('config.ini'):
    api_id_from_user = input("Enter API ID first time: ")
    api_hash_from_user = input("Enter API HASH first time: ")
    # Writing Configs
    config['Telegram'] = {'api_id': api_id_from_user, 'api_hash': api_hash_from_user}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)


# Reading Configs
config.read("config.ini")
# Setting configuration values
api_id = int(config['Telegram']['api_id'])
api_hash = config['Telegram']['api_hash']

client = TelegramClient('test_session', api_id, api_hash)
client.start()

# to store json dict data in a list
json_list = list()

for member in client.iter_participants('membersTesting', 3):
    print("User Name: ", member.username)
    print("First Name: ", member.first_name)
    print("Last Name: ", member.last_name)
    print("Phone Number: ", member.phone)
    print("--------------------------------")

    json_dict = dict()
    json_dict["User Name: "] = member.username
    json_dict["First Name: "] = member.first_name
    json_dict["Last Name: "] = member.last_name
    json_dict["Phone Number: "] = member.phone

    # insert dict into list
    json_list.append(json_dict)

# putting list to obtain result.json file
with open('custom_result.json', 'w', encoding='utf-8') as file:
    json.dump(json_list, file, ensure_ascii=False, indent=1)
