import discord
from discord.ext import commands, tasks
from Crawl import Bond
from datetime import datetime
from pytz import timezone
import aiocron
import configparser
import json


def readToken(name):
    config = configparser.ConfigParser()
    config.read('token.ini',encoding='utf-8')
    return config[name]['token']

def sendEmbed(ti,des):
    embed=discord.Embed(title=ti, description=des, color=0x00aaaa)
    return embed

def timeprint():
    a = datetime.now(timezone('Asia/Seoul')).strftime('%Y-%m-%d %H:%M:%S')
    return a

def log_write(author, command):
    f = open('./log.txt','a')
    data = f"KST : {timeprint()} // {author} 님이 =\"{command}\" 명령어를 사용하였습니다\n"
    f.write(data)
    f.close()

with open('channelData.json') as json_file:
    channelData = json.load(json_file)
    
# print(channelData["DAHUTA"]["cocodor"])


bot = commands.Bot(command_prefix='=')
token = readToken('server')


#-------------------------------------------------------------------------
#앱 재시작시 봇의 ID와 이름 그리고 코멘트를 설정
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    # 'comment'라는 게임 중으로 설정합니다.
    game = discord.Game("문제 발생시 jongsangkuun#8830으로 DM해주세요!")
    await bot.change_presence(status=discord.Status.online, activity=game)
    print("READY")

#-------------------------------------------------------------------------
#명령어를 봇이 보낸 경우 반응하지 않음

@bot.event
async def on_message(message):
    if message.author.bot:
        return None
    await bot.process_commands(message)

#-------------------------------------------------------------------------
#채권 크론탭 부분

@aiocron.crontab('2 0 * * *')
async def cornDahuta():
    server='다후타'
    channelNum = int(channelData[server]["cocodor"])
    aaa = Bond().Check_Server(server)
    channel = bot.get_channel(channelNum)
    test_Embed = sendEmbed(server,aaa)
    log_write("corntab", server)
    await channel.send(embed=test_Embed)

@aiocron.crontab('2 0 * * *')
async def cronMorpheus():
    server='모르페우스'
    channelNum = int(channelData[server]["sesame"])
    aaa = Bond().Check_Server(server)
    channel = bot.get_channel(channelNum)
    test_Embed = sendEmbed(server,aaa)
    log_write("corntab", server)
    await channel.send(embed=test_Embed)

#-------------------------------------------------------------------------
#채권 커맨드 부분

@bot.command(name='누이')
async def NUI(ctx):
    server = '누이'
    abc = Bond().Check_Server(server)
    log_write(ctx.author, server)
    test_Embed = sendEmbed(server,abc)
    await ctx.channel.send(embed=test_Embed)

@bot.command(name='다후타')
async def DAHUTA(ctx):
    server = '다후타'
    abc = Bond().Check_Server(server)
    log_write(ctx.author, server)
    test_Embed = sendEmbed(server,abc)
    await ctx.channel.send(embed=test_Embed)

@bot.command(name='몰페')
async def MORPHEUS(ctx):
    server = '모르페우스'
    abc = Bond().Check_Server(server)
    log_write(ctx.author, server)
    test_Embed = sendEmbed(server,abc)
    await ctx.channel.send(embed=test_Embed)

@bot.command(name='하제')
async def HAJE(ctx):
    server = '하제'
    abc = Bond().Check_Server(server)
    log_write(ctx.author, server)
    test_Embed = sendEmbed(server,abc)
    await ctx.channel.send(embed=test_Embed)

@bot.command(name='랑그')
async def RANGORA(ctx):
    server = '랑그'
    abc = Bond().Check_Server(server)
    log_write(ctx.author, server)
    test_Embed = sendEmbed(server,abc)
    await ctx.channel.send(embed=test_Embed)

#-------------------------------------------------------------------------



bot.run(token)
