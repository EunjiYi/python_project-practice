#  이번 연습은 최적화
#리스트가 null/nil/None이거나 비어 있는 경우 빈 리스트를 반환한다.

#처음에 짠 코드
'''
def change_rotten_fruit(fruit_bag):
    result = []
    for fruit in fruit_bag:
        #print(fruit)
        
        if 'rotten' in fruit:
            result += [fruit.replace('rotten', '').lower()]
            # rotten이 앞에 있으니까 len('rotten')만큼 슬라이싱 쌱
            #왜 나는 이런 생각을 못하는가
        else:
            result += [fruit.lower()]
    return result
'''


# 위의 코드 최적화
def change_rotten_fruit(fruit_bag):
    result = []
    for fruit in fruit_bag: 
        fruit = fruit.replace('rotten','') # if 문을 안써도됨. rotten 없으면 어차피 아무것도 안 바뀜
        fruit = fruit.lower()
        result.append(fruit)
    return result

print(change_rotten_fruit([]))     #[]     
print(change_rotten_fruit(['apple', 'rottenBanana', 'apple'] ))    #['apple', 'banana', 'apple']
print(change_rotten_fruit(['rottenapple', 'rottenBanana', 'apple', 'rottenGrape']))     #['apple', 'banana', 'apple', 'grape']