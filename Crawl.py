import requests
from bs4 import BeautifulSoup
import urllib3


# # print(trs[4].find('li'))
# rank = trs[1].find('li',class_='point')
# print(rank)


class Bond:
    def Bond_server(self,target):
        group = ['table-bond','table-bond right']
        url = requests.get(target)
        soup = BeautifulSoup(url.content,"html.parser")
        result = '```\n'
        cloth = ''
        leather = ''
        wood = ''
        iron = ''

        for i in group:
            # if(i == 'table-bond'):
            #     continent = '-서대륙'
            #     # print('서대륙')
            # if(i == 'table-bond right'):
            #     # print('동대륙')
            #     continent = '+동대륙'

            point = soup.find('table',class_= i)
            trs = point.tbody.find_all('tr')
            items = ['옷감','가죽','목재','철 주괴']

            for j in range(0,4):
                # print(items[j])
                try:
                    rank = trs[j].find('li',class_='point').string
                    if items[j] == items[0]:
                        cloth += rank
                        cloth += '\n'
                    elif items[j] == items[1]:
                        leather += rank
                        leather += '\n'
                    elif items[j] == items[2]:
                        wood += rank
                        wood += '\n'
                    elif items[j] == items[3]:
                        iron += rank  
                        iron += '\n' 
                    else:
                        print('') 
                    # 
                    # print(rank)
                    # result += items[j]
                    # result += '\n'
                    # result += rank
                    # result += '\n'
                    # result += '\n'
                    print('')
                    
                except:
                    print('')
        for z in items:
            result += z
            result += '\n'
            if z == items[0]:
                result += cloth
                result += '\n'
            if z == items[1]:
                result += leather
                result += '\n'
            if z == items[2]:
                result += wood
                result += '\n'
            if z == items[3]:
                result += iron
                result += '\n'

        result += '```'
        return result


    def Check_Server(self,server):
        url = 'https://archeage.xlgames.com/play/worldinfo/'
        if(server == '다후타'):
            target = url + 'DAHUTA'
            result = Bond().Bond_server(target)
            return result

        elif(server == '누이'):
            target = url + 'NUI'
            result = Bond().Bond_server(target)
            return result

        elif(server == '하제'):
            target = url + 'HAJE'
            result = Bond().Bond_server(target)
            return result

        elif(server == '정원'):
            target = url + 'GARDEN'
            result = Bond().Bond_server(target)
            return result

        elif(server == '정원2'):
            target = url + 'GARDEN2'
            result = Bond().Bond_server(target)
            return result

        elif(server == '모르페우스'):
            target = url + 'MORPHEUS'
            result = Bond().Bond_server(target)
            return result     

        else:
            print('error')

a = Bond().Check_Server('다후타')

