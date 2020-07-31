import requests
from kobis import URLMaker


def get_movie_cd(title, director):

    url1 = URLMaker(URLMaker.key)
    url2 = url1.get_url(category='movie',feature='searchMovieList') #제공서비스 중 영화정보
    #return url2

    datainfo = {
        'movieNm': title,
        'directorNm': director
    }
    r = requests.get(url2, params=datainfo)
    
    info_dict = r.json()
    info = info_dict.get('movieListResult').get('movieList')
    #return type(info) #타입은 list

    #info 자체는 list, list는 get을 쓸 수 없으니 for문 돌려서 i에 get을 쓰자.
    result = ''
    for i in info:
        result = i.get('movieCd')
    if len(result) == 0:
        return 0
    else:
        return result

if __name__ == '__main__':
    # 영화이름과 감독을 기준으로 영화코드를 검색합니다.
    print(get_movie_cd('기생충', '봉준호'))