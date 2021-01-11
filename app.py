from Crawl import Bond
import discord
import asyncio

client = discord.Client()
token = '???'


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    channel = message.channel

    if message.content == '=test':
        await channel.send('test~!')
    
    if message.content == '=채권 누이':
        abc = Bond().Check_Server('누이')
        await channel.send(abc)

    if message.content == '=채권 다후타':
        abc = Bond().Check_Server('다후타')
        await channel.send(abc)

    if message.content == '=채권 모르페우스':
        abc = Bond().Check_Server('모르페우스')
        await channel.send(abc)

    if message.content == '=채권 정원':
        abc = Bond().Check_Server('정원')
        await channel.send(abc)

    if message.content == '=채권 정원2':
        abc = Bond().Check_Server('정원2')
        await channel.send(abc)

    if message.content == '=채권 하제':
        abc = Bond().Check_Server('하제')
        await channel.send(abc)



client.run(token)

# Bond().Check_Server('누이')
