#-*-coding:utf-8-*-
import discord
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

user = [] # 유저가 입력한 노래 정보
musictitle = [] # 가공된 정보의 노래 제목
song_queue = [] # 가공된 정보의 노래 링크
musicnow = [] # 현재 출력되는 노래 배열

def title(msg):
    global music

    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    chromeDriver_dir='./ChromeDriver/chromedriver_mac'
    driver = webdriver.Chrome(chromeDriver_dir, options = options)
    driver.get("https://www.youtube.com/results?search_query="+msg+"+lyrics")
    source = driver.page_source
    bs = bs4.BeautifulSoup(source, 'lxml')
    entire = bs.find_all('a', {'id': 'video-title'})
    entireNum = entire[0]
    music = entireNum.text.strip()
    
    musictitle.append(music)
    musicnow.append(music)
    test1 = entireNum.get('href')
    url = 'https://www.youtube.com'+test1
    with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
    URL = info['formats'][0]['url']

    driver.quit()
    
    return music, URL

def play(ctx):
    global vc
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    URL = song_queue[0]
    del user[0]
    del musictitle[0]
    del song_queue[0]
    vc = get(bot.voice_clients, guild=ctx.guild)
    if not vc.is_playing():
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), after=lambda e: play_next(ctx)) 

def play_next(ctx):
    if len(musicnow) - len(user) >= 2:
        for i in range(len(musicnow) - len(user) - 1):
            del musicnow[0]
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    if len(user) >= 1:
        if not vc.is_playing():
            del musicnow[0]
            URL = song_queue[0]
            del user[0]
            del musictitle[0]
            del song_queue[0]
            vc.play(discord.FFmpegPCMAudio(URL,**FFMPEG_OPTIONS), after=lambda e: play_next(ctx))

    else:
        if not vc.is_playing():
            client.loop.create_task(vc.disconnect())

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

@bot.command(name='join')
async def join(ctx):
    try:
        global vc
        vc = await ctx.message.author.voice.channel.connect()
    except:
        try:
            await vs.move_to(ctx.message.author.voice.channel)
        except:
            await ctx.send("채널에 유저가 없습니다")

@bot.command(name='out')
async def out(ctx):
    try:
        await vc.disconnect()
    except:
        await ctx.send('이미 그 채널에 없습니다!')

@bot.command(name='url')
async def urlPlay(ctx, *, url):
    try:
        global vc
        vc = await ctx.message.author.voice.channel.connect()
    except:
        try:
            await vs.move_to(ctx.message.author.voice.channel)
        except:
            await ctx.send("채널에 유저가 없습니다")

    YDL_OPTIONS= {'format':'bestaudio','noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5'}

    if not vc.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        await ctx.send(embed = discord.Embed(title= "노래 재생", description = "현재 " + url + "을(를) 재생하고 있습니다.", color = 0x00ff00))
    else:
        await ctx.send("노래가 이미 재생되고 있습니다!")

@bot.command(name='play')
async def musicPlay(ctx, *, msg):
    try:
        global vc
        vc = await ctx.message.author.voice.channel.connect()
    except:
        try:
            await vs.move_to(ctx.message.author.voice.channel)
        except:
            await ctx.send("채널에 유저가 없습니다")

    if not vc.is_playing():
        global entireText
        
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        web_options = webdriver.ChromeOptions()
        web_options.add_argument('headless')
        
        
        chromeDriver_dir='./ChromeDriver/chromedriver_mac'
        driver = webdriver.Chrome(chromeDriver_dir,options=web_options)
        driver.get("https://www.youtube.com/results?search_query="+msg+"+lyrics")
        source = driver.page_source
        bs = bs4.BeautifulSoup(source, 'lxml')
        entire = bs.find_all('a', {'id': 'video-title'})
        entireNum = entire[0]
        entireText = entireNum.text.strip()
        musicurl = entireNum.get('href')
        url = 'https://www.youtube.com'+musicurl 

        driver.quit()

        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        await ctx.send(embed = discord.Embed(title= "노래 재생", description = "현재 " + entireText + "을(를) 재생하고 있습니다.", color = 0x00ff00))
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
    else:
        await ctx.send("이미 노래가 재생 중이라 노래를 재생할 수 없어요!")

@bot.command(name='pause')
async def musicPause(ctx):
    if vc.is_playing():
        vc.pause()
        await ctx.send(embed = discord.Embed(title= "일시 정지", description = entireText + "을(를) 일시정지 했습니다.", color = 0x00ff00))
    else:
        await ctx.send("지금 노래가 재생되지 않네요")

@bot.command(name='con')
async def musicContinuous(ctx):
    try:
        vc.resume()
    except:
        await ctx.send("지금 노래가 재생되지 않네요")
    else:
        await ctx.send(embed = discord.Embed(title= "다시재생", description = entireText  + "을(를) 다시 재생했습니다.", color = 0x00ff00))

@bot.command(name='stop')
async def musicStop(ctx):
    if vc.is_playing():
        vc.stop()
        await ctx.send(embed = discord.Embed(title= "노래끄기", description = entireText  + "을(를) 종료했습니다.", color = 0x00ff00))
    else:
        await ctx.send("지금 노래가 재생되지 않네요.")

@bot.command(name='now')
async def playNow(ctx):
    if vc.is_playing():
        await ctx.send(embed = discord.Embed(title= "지금노래", description = '현재' + entireText  + "을(를) 재생중입니다.", color = 0x00ff00))
    else:
        await ctx.send("지금 노래가 재생되지 않네요.")

@bot.command(name='melon')
async def playMelon(ctx):
    if not vc.is_playing():
        
        options = webdriver.ChromeOptions()
        options.add_argument("headless")

        global entireText
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            
        chromeDriver_dir='./ChromeDriver/chromedriver_mac'
        driver = webdriver.Chrome(chromeDriver_dir, options = options)
        driver.get("https://www.youtube.com/results?search_query=멜론차트")
        source = driver.page_source
        bs = bs4.BeautifulSoup(source, 'lxml')
        entire = bs.find_all('a', {'id': 'video-title'})
        entireNum = entire[0]
        entireText = entireNum.text.strip()
        musicurl = entireNum.get('href')
        url = 'https://www.youtube.com'+musicurl 

        driver.quit()

        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        await ctx.send(embed = discord.Embed(title= "노래 재생", description = "현재 " + entireText + "을(를) 재생하고 있습니다.", color = 0x00ff00))
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
    else:
        await ctx.send("이미 노래가 재생 중이라 노래를 재생할 수 없어요!")

@bot.command(name='add')
async def 대기열추가(ctx, *, msg):
    user.append(msg)
    result, URLTEST = title(msg)
    song_queue.append(URLTEST)
    await ctx.send(result + "를 재생목록에 추가했어요!")

@bot.command(name='del')
async def 대기열삭제(ctx, *, number):
    try:
        ex = len(musicnow) - len(user)
        del user[int(number) - 1]
        del musictitle[int(number) - 1]
        del song_queue[int(number)-1]
        del musicnow[int(number)-1+ex]
            
        await ctx.send("대기열이 정상적으로 삭제되었습니다.")
    except:
        if len(list) == 0:
            await ctx.send("대기열에 노래가 없어 삭제할 수 없어요!")
        else:
            if len(list) < int(number):
                await ctx.send("숫자의 범위가 목록개수를 벗어났습니다!")
            else:
                await ctx.send("숫자를 입력해주세요!")

@bot.command(name='list')
async def 목록(ctx):
    if len(musictitle) == 0:
        await ctx.send("아직 아무노래도 등록하지 않았어요.")
    else:
        global Text
        Text = ""
        for i in range(len(musictitle)):
            Text = Text + "\n" + str(i + 1) + ". " + str(musictitle[i])
            
        await ctx.send(embed = discord.Embed(title= "노래목록", description = Text.strip(), color = 0x00ff00))

@bot.command(name='clearlist')
async def 목록초기화(ctx):
    try:
        ex = len(musicnow) - len(user)
        del user[:]
        del musictitle[:]
        del song_queue[:]
        while True:
            try:
                del musicnow[ex]
            except:
                break
        await ctx.send(embed = discord.Embed(title= "목록초기화", description = """목록이 정상적으로 초기화되었습니다. 이제 노래를 등록해볼까요?""", color = 0x00ff00))
    except:
        await ctx.send("아직 아무노래도 등록하지 않았어요.")

@bot.command(name='playlist')
async def 목록재생(ctx):

    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    
    if len(user) == 0:
        await ctx.send("아직 아무노래도 등록하지 않았어요.")
    else:
        if len(musicnow) - len(user) >= 1:
            for i in range(len(musicnow) - len(user)):
                del musicnow[0]
        if not vc.is_playing():
            play(ctx)
        else:
            await ctx.send("노래가 이미 재생되고 있어요!")



bot.run(token)
