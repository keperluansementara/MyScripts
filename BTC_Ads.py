import asyncio
import logging
import re
import time
import os
import sys
import random

logging.basicConfig(level=logging.ERROR)

from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from datetime import datetime
from colorama import Fore, init as color_ama
color_ama(autoreset=True)



try:
   import colorama
   from colorama import Fore, Back, Style
   colorama.init(autoreset=True)
   hijau = Style.RESET_ALL+Style.BRIGHT+Fore.GREEN
   res = Style.RESET_ALL
   abu2 = Style.DIM+Fore.WHITE
   putih = Style.RESET_ALL+Style.BRIGHT+Fore.WHITE
   ungu2 = Style.NORMAL+Fore.MAGENTA
   ungu = Style.RESET_ALL+Style.BRIGHT+Fore.MAGENTA
   hijau2 = Style.NORMAL+Fore.GREEN
   yellow2 = Style.NORMAL+Fore.YELLOW
   yellow = Style.RESET_ALL+Style.BRIGHT+Fore.YELLOW
   red2 = Style.NORMAL+Fore.RED
   red = Style.RESET_ALL+Style.BRIGHT+Fore.RED
   cyan = Style.RESET_ALL+Style.BRIGHT+Fore.CYAN
   cyan2 = Style.NORMAL+Fore.CYAN

except:
   print ("Please Install Modul Colorama!!\n\n\n")
   sys.exit()

try:
   import requests
   from bs4 import BeautifulSoup
except:
   print ("Please Install Modul Requests & BS4\n\n\n")
   sys.exit()

os.system('cls' if os.name=='nt' else 'clear')

# Get your own values from my.telegram.org
api_id = 1992530
api_hash = '5c8aeda6f752d74363769d456913665c'

banner = """
"""+Style.BRIGHT+Fore.CYAN+"""

\033[1;32m╔════════════════════════════════════════════════╗
\033[1;32m║Supported         : SHPC7BOT                    ║
\033[1;32m║Special Thanks    : ALL MY TEAMS                ║
\033[1;32m║Video channel     : SHPChannels                 ║
\033[1;32m║Telegram group    : SHPCorps7                   ║
\033[1;32m║Doge Donate       : Free                        ║
\033[1;32m╚════════════════════════════════════════════════╝
"""+Style.RESET_ALL+Style.BRIGHT+Fore.WHITE+"""              [Created by SHPC7 2020]  """

cname = '@BTC_Ads_de_bot'
crot = 'https://t.me/BTC_Ads_de_bot'

def print_msg_time(message):
	print('[' + Fore.CYAN + f'{datetime.now().strftime("%H:%M:%S")}' + Fore.RESET + f'] {message}')

async def main():
	print (banner)
	print(Fore.BLUE + ' ================================================= \n' + Fore.RESET)
	
	# Check if phone number is not specified

	if len(sys.argv) < 2:
		print('Usage: python start.py phone_number')
		print('-> Input number in international format (example: +62xxxxxxxxxx)\n')
		e = input('Press any key to exit...')
		exit(1)
		
	phone_number = sys.argv[1]
	choice = '🎯View Ads'
	
	if not os.path.exists("session"):
		os.mkdir("session")
   
    # Connect to client
	client = TelegramClient('session/' + phone_number, api_id, api_hash)
	await client.start(phone_number)
	me = await client.get_me()
	
	# Free_LTC_Robot
	print_msg_time(Fore.GREEN + f'Name    : @BTC_Ads_de_bot '  + Fore.RESET)
	print_msg_time(Fore.GREEN + f'Welcome : {me.first_name} - {me.last_name} '  + Fore.RESET)
	print(f'\n')
	print_msg_time(Fore.YELLOW + 'Start Bot' + '\n' + Fore.RESET)
	
	# Start command /balance

	i = 1
	while(True):
		await client.send_message(crot, choice)
		print_msg_time(Fore.GREEN + 'Click Success >> Lanjut >>  ' + choice + Fore.RESET)
		time.sleep(37) #waktu klik hitungan dalam detik
		i = 1
		
	
		# Message the bot
	@client.on(events.NewMessage(chats=cname, incoming=True))
	async def earned_amount(event):
		message = event.raw_text
		if 'Balance' in message:	
			print_msg_time(Fore.GREEN + event.raw_text + '\n' + Fore.RESET)
		
			
	await client.run_until_disconnected()
	
asyncio.get_event_loop().run_until_complete(main())
