import discord
import requests
from bs4 import BeautifulSoup
import random
import os

client = discord.Client(intents=discord.Intents.default())



@client.event
async def on_ready():
    print("I'm in")
    print(client.user)


@client.event
async def on_message(message):
    a = message.content
    if message.author != client.user:
       if a.find('/hr medium') != -1 or a.find('/hr hard') != -1 or a.find('/hr easy') != -1:
            links = []
            url = "https://www.hackerrank.com/domains/algorithms?filters%5Bdifficulty%5D%5B%5D=" + message.content.split()[1]
            r = requests.get(url)
            data = r.text
            soup = BeautifulSoup(data, features="html.parser")
            for link in soup.find_all('a', class_="js-track-click"):
                links.append(link.get('href'))
            await client.send_message(message.channel, "https://www.hackerrank.com"+random.choice(links))

       elif a.find('/cf medium') != -1 or a.find('/cf hard') != -1 or a.find('/cf easy') != -1 or a.find('/cf ultra') != -1:
            print("a")
            



client.run(access_token)
