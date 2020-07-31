import json

def check(data):
    # 체온을 잰 시간순서대로 데이터를 뽑아 리스트로 만든다. 리스트의 이름은 listlist
    listlist = []
    for dt in data:
        listlist += dt
    # 그러면 listlist에 [36.7, 36.5, 36.9, 37.5, 37.8, 37.8, 36.7, 36.5, 36.3, 36.4, 36.5, 36.5, 36.8, 36.6] 이렇게 들어가 있음
    
    # 연속으로 3번 다 37.5 이상이면 바로 True 리턴하고 함수 종료.
    # 아니라면 끝까지 다 돌고 False를 반환한다.
    for i in range(0, len(listlist)):
        if listlist[i] >= 37.5 and listlist[i+1] >= 37.5 and listlist[i+2] >= 37.5:
            return True
    return False

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    temperature_json = open('problem02_data.json', encoding='UTF8')
    temperature_list = json.load(temperature_json)
    print(check(temperature_list))
    # => True