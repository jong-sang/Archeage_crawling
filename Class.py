from Crawl import Bond


class Log:
    def log_write(author, command):
        f = open('./log.txt','a')
        data = f"{author}님이","=","{command} 명령어를 사용하였습니다\n"
        f.write(data)
        f.close()

