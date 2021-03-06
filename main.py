import os
import sys
import time
import requests
import json
import discord
import asyncio
from colorama import Fore
import threading
from discord.ext import commands
from dhooks import Webhook

os.system('mode 85, 20')
 

banlogs = input(Fore.RED + "[>] Account Token: ")

os.system('cls')

intents = discord.Intents.all()
intents.members = True

headers = {'Authorization': f'{banlogs}'}
client = commands.Bot(command_prefix="l", case_insensitive=False, self_bot=True, intents=intents)
client.remove_command("help")


i = 0
membercount = 0

print(Fore.RED + "[...] Loading")

@client.event
async def on_ready():
    await guild()

async def menuban():
    guild = guildid
    txt = open('Scraped/userscrape.txt')
    for member in txt:
        threading.Thread(target=massban, args=(guild, member,)).start()
    txt.close()
    time.sleep(4)

def massban(guild, member):
    global i, membercount
    while True:
        r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{member}", headers=headers)
        if 'retry_after' in r.text:
            time.sleep(r.json()['retry_after'])
        else:
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                while i < membercount:
                    i+=1
                    if i == 1:
                        print("[>] %dst user has been banned"%(i))
                    elif i == 2:
                        print("[>] %dnd user has been banned"%(i))
                    elif i == 3:
                        print("[>] %drd user has been banned"%(i))
                    else:
                        print("[>] %dth user has been banned"%(i))
                break
            else:
                break


async def main():
    if len(sys.argv) < 2:
        sys.stdout.write(f''' 
[+] Connected as: {client.user}
[+] Guild: {guildid}

''')

    option = input('''[>] Mass ban? (y/n): ''')
    print("")
    if option == 'y':
        await menuban()
        await guild()
    if option == 'n':
        await guild()
    else:
        print('''
[-] Invalid option''')
time.sleep(3)


async def guild():
    global membercount, guildid
    os.system('cls & mode 85, 20')
    guildid = int(input('''[>] Guild id: '''))
    await client.wait_until_ready()
    ob = client.get_guild(guildid)
    members = await ob.chunk()
    os.remove("Scraped/userscrape.txt")

    with open('Scraped/userscrape.txt', 'a') as txt:
        for member in members:
            txt.write(str(member.id) + "\n")
            membercount += 1
        if membercount == 1:
            print(f'''
[+] Scraped {membercount} member in total''')
        else:
            print(f'''
[+] Scraped {membercount} members in total''')
        txt.close()
        time.sleep(1)
        await main()


def check():
   os.system('cls & mode 85, 20')
   try:
       client.run(banlogs, bot=False)
   except:
       print('''[-] Invalid Token''')
       time.sleep(3)

check()