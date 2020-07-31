요청하는 url만들기

url1 = URLMaker(URLMaker.key)
일단 키 값을 가져와서 url1이라 한다.

url2 = url1.get_url(category='movie',feature='searchMovieInfo') #제공서비스 중 영화정보 중 영화상세정보
그 중에 상세하게 들어갈 category와 feature를 지정한다.
인자 이름 들어갈 필요없이 'movie'만 적어도 되는데,내가 구분하기 편하려고 category='movie'형태로 적었다.

  datainfo = {
        'movieCd': movie_cd
    }
요청할 데이터를 딕셔너리 형태로 집어넣어서 requests할 때 파라미터로 같이 넣어 보낸다. 

info_dict = r.json()
requests 받아온 것을 우리가 알아볼 수 있는 json 형태로 만들고, 

info = info_dict.get('movieInfoResult').get('movieInfo')
json형태로 받아온 자료 중에서 정말 필요한 딕셔너리의 키 값만 불러온다. 연속으로 get메소드를 두 번 쓰면 해당 키 속 벨류가 딕셔너리일 때, 그 딕셔너리의 키에 해당하는 벨류값을 가져온다.

return type(info)
이때 받아온 info의 타입을 꼭 찍어봤는데, 이렇게 해야 데이터를 가공할 때 사용할 메소드를 결정할 수 있다. 실제 코드는 아니고 디버깅용.

총평: 딕셔너리 메소드와 리스트 메소드가 자꾸 헷갈린다 ㅜ 개념을 확실히 해야겠다. 
