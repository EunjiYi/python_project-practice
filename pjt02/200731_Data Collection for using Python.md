200731 Python을 활용한 데이터 수집

두번째 프로젝트

---------



컴퓨터가 통신할 수 있는 약속 



요청보내기 

cmd 창에서 curl [http://www.naver.com](http://www.naver.com/)

우리가 보기 젤 편한 요청(http) / 응답(xml, json 등): 웹브라우저



**API**

외부서비스를 가져오기 위한 규약/규칙

> 인터페이스: 프로그램끼리 서로 어떻게 얘기할지 규칙을 정해놓은 것



일별박스오피스 API서비스를 통해서 특정일자 상영작들의 박스오피스 정보를 조회할거다.

조회 = 리퀘스트 보내는 것(요청)

응답을 xml과 json으로 보내줌

url = 어디로 여청을 보낼지에 대한 정보 

파라미터=매개변수: 무엇을 가지고 요청을 보낼지에 대한 정보  ex.어떤 책 찾아주세요.



json viewer 설치그리고 json url 클릭(크롬에서 깔끔하게 볼 수 있음)

json url = 요청과 응답의 구조는 url을 통해서 생성을 할 수 있다. 

url 구조가 어떻게 만들어져있는지 분석 및 수정해보자. `?와 & 사용`

`&요청변수명=요청할내용`

&peopleNm=다우니

&filmoNames=아이언맨



----------



#### requests 라이브러리

구글 python requests 검색

requests.readthedocs.io/en/master/usr/quickstart/

```python
test.py

import requests -> 오류나면 설치 필요

pip install reqeusts

url = 'https://블라블라'
r = requests.get(url)  
# r = Responce의 약자 by 공식문서. res responce 다 가능.
# 응답이 되었다는 리스폰스 객체임
```



r =  requests.get(url, parms=payload)

print(r.text)

찍어봤는데, print(type(r.text)) -> str임! 가져온 데이터 타입이 불편함



파이썬에서 json decoder를 가지고 있으니, 

_json responce 일때는 이렇게 찍어라. ~ JSON Response Content 가이드라인 있음_

print(r.json()) -> 이러면 딕셔너리로 나옴

print(type(r.json())) -> `<class 'dict'>`출력됨



*팁*1

get() : 딕셔너리의 키 값에 접근. 키에 오류가 있어도 None 반환 - KeyError 있어도 넘어감.

원하는 데이터 받아올 때 get 쓰면 값이 비어있어도 오류 안나고 None 반환한다.



*팁2*

요청 url 만들고나서 꼭 print로 찍어서 필히 확인할 것

최종적으로 만든 url을 복사해서 크롬에 붙여넣기해서 데이터가 나오는지 확인(with json viewer)

그리고 request에 요청해서 데이터를 처리한다. !