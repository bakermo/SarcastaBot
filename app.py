import discord
import os
import random
from flask import Flask
app = Flask(__name__)

client = discord.Client()

@app.route("/")
def hello():
    client.run(os.getenv('TOKEN'))
    return "Sarcasta BOT Initialized"

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user: 
    return
  
  sarcasta = "\"";
  if message.content.startswith('!sarcasta'):
    message.content = message.content[9:]
    message.content = message.content.strip()
    for character in message.content:
      if bool(random.getrandbits(1)):
        sarcasta+= character.upper()
      else:
        sarcasta+= character
    sarcasta+= "\""
    await message.channel.send(sarcasta)
client.run(os.getenv('TOKEN'))
