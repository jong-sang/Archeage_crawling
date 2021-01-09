import requests
from bs4 import BeautifulSoup
import urllib3


# # print(trs[4].find('li'))
# rank = trs[1].find('li',class_='point')
# print(rank)


class Bond:

    def Bond_server(target):
        group = ['table-bond','table-bond right']
        url = requests.get(target)
        soup = BeautifulSoup(url.content,"html.parser")
        for i in group:
            if(i == 'table-bond'):
                print('서대륙')
            if(i == 'table-bond right'):
                print('동대륙')

            point = soup.find('table',class_= i)
            trs = point.tbody.find_all('tr')
            items = ['옷감','가죽','목재','철 주괴']

            for j in range(0,4):
                print(items[j])
                try:
                    rank = trs[j].find('li',class_='point').string
                    print(rank)
                    print('')
                except:
                    print('')


    def Chcek_Server(server):
        url = 'https://archeage.xlgames.com/play/worldinfo/'
        if(server == '다후타'):
            target = url + 'DAHUTA'
            Bond.Bond_server(target)

        elif(server == '누이'):
            target = url + 'NUI'
            print(target)
            Bond.Bond_server(target)

        elif(server == '하제'):
            target = url + 'HAJE'
            Bond.Bond_server(target)

        elif(server == '정원'):
            target = url + 'GARDEN'
            Bond.Bond_server(target)

        elif(server == '정원2'):
            target = url + 'GARDEN2'
            Bond.Bond_server(target)

        elif(server == '모르페우스'):
            target = url + 'MORPHEUS'
            Bond.Bond_server(target)      

        else:
            print('error')

Bond.Chcek_Server('누이')