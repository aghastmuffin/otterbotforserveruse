import discord
from time import sleep
from random import randrange
users = []
messages = []
cmessage = str('')
user = str('')
ran = int()
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
#        await message.channel.send('SYNTAX ERROR{0.author} CAUSE: {0.content}'.format(message))
#        user = ('{0.author}'.format(message))
#        users.append(user)
#        cmessage = ('{0.content}'.format(cmessage))
#        messages.append(cmessage)
        if message.content == 'i':
            await message.channel.send('?')
#        if message.content == '-User':
 #           if user == ('Kingve#0032'):
 #               await message.channel.send(users)
#            else:
#                await message.channel.send('Yes! You are a user, {0.author}'.format(message))
#                if message.content == '-Messages':
#                    await message.channel.send(messages)
#                elif message.content == '-Message & User':
#                    await message.channel.send(users)
#                    await message.channel.send(messages)
#            print(users)
        if message.content == '-info':
            await message.channel.send(':otter:')
        elif message.content == 'otterog':
            await message.channel.send('https://images-ext-1.discordapp.net/external/J2aSwe0Nd6c3DYtlQJqMsHBLIfM3EcZsRFXsFRah3Ic/https/i.imgur.com/STQBmM5.gif')
        else:
            if message.content == 'otter':
                ran = int(0)
                ran = (randrange(1, 3))
                if ran == (1):
                    await message.channel.send('https://images-ext-1.discordapp.net/external/J2aSwe0Nd6c3DYtlQJqMsHBLIfM3EcZsRFXsFRah3Ic/https/i.imgur.com/STQBmM5.gif')
                elif ran == (2):
                    await message.channel.send('https://tenor.com/view/otter-cute-gif-18081789')
                else: 
                    if ran == (3):
                        await message.channel.send('https://tenor.com/view/shook-otter-funny-animals-get-otter-here-shocked-gif-11113562')
            elif message.content == 'doge':
                await message.channel.send('https://tenor.com/view/shibe-snow-shibe-shaking-shiba-inu-shiba-inu-cute-shiba-gif-19856803')
            
#            elif message.content == '-Help':
                
#            embedVar = discord.Embed(title='-Help ')
#            embedVar.add_field(name = '-User', value= "Yes! You are a user, _______", inline = True)
#            embedVar.add_field(name = 'Check if banned', value = "{userbanned}", inline = True)
#            embedVar.add_field(name = 'User join date (in days)', value = "{userjoin}", inline = True)

#        exit()
#        discord.activity('1232123213')
sleep(0.5)
client = MyClient()
