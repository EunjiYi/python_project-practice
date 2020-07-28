import json

def title_length(movie):
    #제목 글자수를 담을 변수 cnt, 초기값은 0
    cnt = 0
    for word in movie['title']: #보이후드면 보, 이, 후, 드 총 4번 돈다. 즉 cnt가 총 4 증가
        cnt += 1
    return cnt

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('problem01_data.json', encoding='UTF8')
    movie = json.load(movie_json)
    print(title_length(movie)) 
    # => 4