#-*-coding:utf-8-*-
import discord
from discord.channel import VoiceChannel
from discord.ext import commands
from selenium.webdriver.chrome import options
from Crawl import Bond
from datetime import datetime
from pytz import timezone
import aiocron
import configparser
import json
from youtube_dl import YoutubeDL
from discord import FFmpegPCMAudio
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from discord.utils import get


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
    data = "KST : {timeprint()} // {author} 님이 =\"{command}\" 명령어를 사용하였습니다\n"
    f.write(data)
    f.close()

with open('channelData.json') as json_file:
    channelData = json.load(json_file)
    
# print(channelData["DAHUTA"]["cocodor"])


bot = commands.Bot(command_prefix='=')
token = readToken('test')
client = discord.Client()

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

@bot.command()
async def 들어와(ctx):
   global vc
   vc = await ctx.message.author.voice.channel.connect()


bot.run(token)
