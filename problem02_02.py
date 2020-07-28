import json

def rotate(data):
    # 오전, 오후 체온데이터를 담아올 빈 리스트를 각각 생성한다. 
    am = []
    pm = []
    for dt in data:
        am += [dt[0]] # 오전 데이터만 담는다. 
        pm += [dt[1]] # 오후 데이터만 담는다. 
    dictdict = { 'am': am , 'pm': pm } # 딕셔너리 형태로 만든다. 
    return dictdict

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    temperature_json = open('problem02_data.json', encoding='UTF8')
    temperature_list = json.load(temperature_json)
    print(rotate(temperature_list))
    # => {
    #     'am': [36.7, 36.9, 37.8, 36.7, 36.3, 36.5, 36.8], 
    #     'pm': [36.5, 37.5, 37.8, 36.5, 36.4, 36.5, 36.6]
    # }
