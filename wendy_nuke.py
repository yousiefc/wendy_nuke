# Wendy Nuke Bot
# Counts the number of times a day the word "Wendys" is mentioned
#
# @author Shmazool

from dotenv import load_dotenv
import os
import discord
import re
from datetime import datetime
import time

load_dotenv()

#globals
#TOKEN = os.getenv('TOKEN')
TOKEN = os.environ['TOKEN']

wendys = 0
MAX = 5
wendys_left = MAX
date = datetime.today().date()


client = discord.Client();

#async def triggered on message in the chat
#counts the number of times 'wendys' has been said, if it is more than the MAX it will delete the message
@client.event
async def on_message(message):
    global wendys
    global wendys_left
    w_slur = re.compile('(?Ui)(w.*e.*n.*d.*y)')

    if message.author == client.user:
        return
    
    await checkDate()
    
    search = re.findall(w_slur,message.content)

    if len(search) > 0 :
        if wendys < MAX :      
            for slurs in search:
                wendys = wendys+1
                wendys_left = wendys_left-1
            msg = "Wendy's has now been mentioned {0} times in the chat today. You have {1} Wendy's remaining before any Wendy's messages are immediately deleted.".format(wendys, wendys_left)
            await message.channel.send(msg)

        else :
            await message.delete()
            await message.channel.send('Nuked')
            return

    if message.content == '!nuke' :
        msg = "There are {} left before nuking".format(wendys_left)
        await message.channel.send(msg)

#checks if date is the same as todays date
async def checkDate() :
    global date

    if date != datetime.today().date() :
        date = datetime.today().date()
        wendys_left = MAX
        return
    else :
        return


#on start message
@client.event
async def on_ready():
    print('Hello! Im Wendy_Nuke!')
    print('Type "!nuke" to see how many Wendys until nuking')
    
client.run(TOKEN)
