import requests
from kobis import URLMaker


def filmo_count(people, movie):
    url1 = URLMaker(URLMaker.key)
    url2 = url1.get_url(category='people',feature='searchPeopleList') # 제공서비스 중 영화인정보
    
    datainfo = {
        'peopleNm': people,
        'filmoNames': movie
    }
    r = requests.get(url2, params=datainfo)
    info_dict = r.json()
    info = info_dict.get('peopleListResult').get('peopleList')

    result = ''
    for i in info:
        result += i.get('filmoNames')
    
    for i in result:
        return result.count('|')+1

if __name__ == '__main__':
    # 배우 이름과 작품을 이용하여 총 해당 배우가 몇 작품에 출연했는지 출력합니다.
    print(filmo_count('다우니', '아이언맨'))