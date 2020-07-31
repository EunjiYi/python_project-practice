import requests
from kobis import URLMaker
from problem_b import get_movie_cd


def search_movie_info(movie_cd):
    url1 = URLMaker(URLMaker.key)
    url2 = url1.get_url(category='movie',feature='searchMovieInfo') #제공서비스 중 영화정보 중 영화상세정보
    #return url2
    
    datainfo = {
        'movieCd': movie_cd
    }
    r = requests.get(url2, params=datainfo)
    
    info_dict = r.json()
    info = info_dict.get('movieInfoResult').get('movieInfo')
    #return info #딕셔너리임.
    
    result = {}
   
    genre_li = []
    genre_li += [info.get('genres')[0].get('genreNm')]
    
    actor_str = ''
    if (info.get('actors') == 0):
        actor_str = 'noActor'
    else:
        actor_str = info.get('actors')[0].get('peopleNm')

    
    result.update( {'movieNm': info.get('movieNm'),
                    'openDt': info.get('openDt'),
                    'genres': genre_li,
                    'actors': actor_str })
                    #info 는 딕셔너리
                    #info.get('actors')는 리스트
                    #info.get('actors')[0]는 딕셔너리

    return result

if __name__ == '__main__':
    # 영화이름과 감독을 기준으로 영화코드를 검색하여 변수 movie_cd에 저장합니다.
    movie_cd = get_movie_cd('기생충', '봉준호')
    # movie_cd를 이용하여 상세정보를 조회하여 출력합니다.
    print(search_movie_info(movie_cd))
