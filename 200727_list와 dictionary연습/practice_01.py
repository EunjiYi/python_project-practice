girls = ['jane', 'ashley', 'mary']
boys = ['justin', 'eric', 'david']

#먼저 반복문으로 
result = []
for boy in boys:
    for girl in girls:
        result.append((boy,girl))  #(boy, girl)을 튜플로 어팬드
print(result)

#list comprehension 활용
result = [(boy, girl) for boy in boys for girl in girls]  #다 적고 대괄호 빼먹지 말기
print(result)