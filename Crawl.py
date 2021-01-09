import requests
from bs4 import BeautifulSoup
import urllib3


# # print(trs[4].find('li'))
# rank = trs[1].find('li',class_='point')
# print(rank)
group = ['table-bond','table-bond right']
def Crwaling(server):
    target = 'https://archeage.xlgames.com/play/worldinfo/DAHUTA'
    url = requests.get(target)
    soup = BeautifulSoup(url.content,"html.parser")

    if(server == '다후타'):
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

    else:
        print('error')

Crwaling('다후타')