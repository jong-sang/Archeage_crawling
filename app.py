from Crawl import Bond
import discord
import asyncio

client = discord.Client()



def log_write(author, command):
    f = open('./log.txt','a')
    data = f"{author}님이 {command} 명령어를 사용하였습니다"
    f.write(data)
    f.close()

@client.event
async def on_ready():
    print('Logged in as')
    print('봇 이름 : ',client.user.name)
    print('봇 고유 넘버 :',client.user.id)
    print('------')


@client.event
async def on_message(message):
    channel = message.channel

    if message.content == '=test':
        await channel.send('test~!')
        print(f"{message.author}님이 test 명령어를 사용하였습니다")
        log_write(message.author,'=test')
    
    if message.content == '=채권 누이':
        abc = Bond().Check_Server('누이')
        await channel.send(abc)
        print(f"{message.author}님이 =채권 누이 명령어를 사용하였습니다")
        log_write(message.author, '=채권 누이')

    if message.content == '=채권 다후타':
        abc = Bond().Check_Server('다후타')
        await channel.send(abc)
        print(f"{message.author}님이 =채권 다후타 명령어를 사용하였습니다")
        log_write(message.author, '=채권 다후타')

    if message.content == '=채권 모르페우스':
        abc = Bond().Check_Server('모르페우스')
        await channel.send(abc)
        print(f"{message.author}님이 =채권 모르페우스 명령어를 사용하였습니다")
        log_write(message.author, '=채권 모르페우스')

    if message.content == '=채권 정원':
        abc = Bond().Check_Server('정원')
        await channel.send(abc)
        print(f"{message.author}님이 =채권 정원 명령어를 사용하였습니다")
        log_write(message.author, '=채권 정원')

    if message.content == '=채권 정원2':
        abc = Bond().Check_Server('정원2')
        await channel.send(abc)
        print(f"{message.author}님이 =채권 정원2 명령어를 사용하였습니다")
        log_write(message.author, '=채권 정원2')

    if message.content == '=채권 하제':
        abc = Bond().Check_Server('하제')
        await channel.send(abc)
        print(f"{str(message.author)}님이 =채권 하제 명령어를 사용하였습니다")
        log_write(message.author, '=채권 하제')

    if message.content.startswith('=청소'):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 메세지 삭제 완료!")
        print(f"{message.author}님이 =청소 명령어를 사용하였습니다")
        log_write(message.author, '=청소')

    if message.content.startswith('=정리'):
        print(f"{message.author}님이 =정리 명령어를 사용하였습니다")
        log_write(message.author, '=정리')
            number = int(message.content.split(" ")[1])
            user_name = str(message.author)[:-5]
            user = message.author

            # user = 메세지를 보낸 사람
            #
            delete_counter = 0
            counter = 0
            print('number : ', number)
            # print('mention_id : ',mention_id)
            print('user_name : ', user_name)
            print('user : ', user)
            print(message.content)
            # print('mention_id_type : ',type(mention_id))
            await message.delete()
            if user != client.user.id:
                if 0 < number and number < 100:
                    msg = await channel.history(limit=number).flatten()
                    async for i in channel.history(limit=number):
                        if i.author == user:
                            await i.delete()
                            delete_counter += 1
                        counter += 1
                    await channel.send(f"```{counter}개의 메세지 중 {user_name}님의 메세지 {delete_counter}만큼 삭제했습니다```")
                    print('count : ',counter)
                else:
                    await channel.send('```1 ~ 99사이 숫자만 가능합니다```')
            else:
                await channel.send('```봇은 안된다 이놈아```')

        except IndexError as error:
            await channel.send('```=정리 {숫자} 이렇게 사용해주세요!```')



# async def clear(ctx, number):
#     number = int(number) #Converting the amount of messages to delete to an integer
#     counter = 0
#     async for x in Client.logs_from(ctx.message.channel, limit = number):
#         if counter < number:
#             await Client.delete_message(x)
#             counter += 1
#             await asyncio.sleep(1.2) #1.2 second timer so the deleting process can be even





    
    



client.run(token)

# Bond().Check_Server('누이')
