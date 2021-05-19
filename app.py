import discord
from discord.ext import commands, tasks
from Crawl import Bond
from datetime import datetime
from pytz import timezone
import aiocron

bot = commands.Bot(command_prefix='=')


def test(ti,des):
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


#-------------------------------------------------------------------------
#앱 재시작시 봇의 ID와 이름 그리고 코멘트를 설정
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    # 'comment'라는 게임 중으로 설정합니다.
    game = discord.Game("갓겜 아키에이지")
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
#스케쥴러로 매 자정 12시5분에 채권 내용을 메세지로 전송

# send_time='10:48' #time is in 24hr format
# message_channel_id=797984230377259012 #channel ID to send images to

# @bot.event
# async def time_check():
#     await bot.wait_until_ready()
#     message_channel=bot.get_channel(message_channel_id)
#     while not bot.is_closed:
#         now=datetime.strftime(datetime.now(timezone('Asia/Seoul')),'%H:%M')
#         if now.hour() == 10 and now.minute() == 52:
#             message= '타이머응애'
#             await message_channel.send(message)


# bot.loop.create_task(time_check())

@aiocron.crontab('2 0 * * *')
async def cornjob1():
    server='다후타'
    aaa = Bond().Check_Server(server)
    channel = bot.get_channel(797984230377259012)
    test_Embed = test(server,aaa)
    await channel.send(embed=test_Embed)

@aiocron.crontab('2 0 * * *')
async def cornjob2():
    server='모르페우스'
    aaa = Bond().Check_Server(server)
    channel = bot.get_channel(502821365934587907)
    test_Embed = test(server,aaa)
    await channel.send(embed=test_Embed)

#-------------------------------------------------------------------------
#채권 커맨드 부분

@bot.command(name='누이')
async def NUI(ctx):
    server = '누이'
    abc = Bond().Check_Server(server)
    log_write(ctx.author, server)
    test_Embed = test(server,abc)
    log_write('크론탭','=다후타')
    await ctx.channel.send(embed=test_Embed)

@bot.command(name='다후타')
async def DAHUTA(ctx):
    server = '다후타'
    abc = Bond().Check_Server(server)
    log_write(ctx.author, server)
    test_Embed = test(server,abc)
    await ctx.channel.send(embed=test_Embed)

@bot.command(name='몰페')
async def MORPHEUS(ctx):
    server = '모르페우스'
    abc = Bond().Check_Server(server)
    log_write(ctx.author, server)
    test_Embed = test(server,abc)
    await ctx.channel.send(embed=test_Embed)

@bot.command(name='하제')
async def HAJE(ctx):
    server = '하제'
    abc = Bond().Check_Server(server)
    log_write(ctx.author, server)
    test_Embed = test(server,abc)
    await ctx.channel.send(embed=test_Embed)

@bot.command(name='랑그')
async def RANGORA(ctx):
    server = '랑그'
    abc = Bond().Check_Server(server)
    log_write(ctx.author, server)
    test_Embed = test(server,abc)
    await ctx.channel.send(embed=test_Embed)

#-------------------------------------------------------------------------



bot.run(token)