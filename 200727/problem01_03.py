import json

def history(movie):
    if '과거' in movie['overview']: #줄거리에 과거에 들어가 있느냐?
        return True # 포함되어 있으면 True
    else:
        return False # 포함되어 있지 않으면 False

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('problem01_data.json', encoding='UTF8')
    movie = json.load(movie_json)
    print(history(movie)) 
    # => False