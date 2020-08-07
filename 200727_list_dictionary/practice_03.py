words = 'Life is too short, you need python!'

#  첨에 w == 'a' or or or w == 'u'하고 리플레이스 '' 하려고 함
#내가 생각하는 수준이란... ㅠ
#근데 이렇게 하니까 깔끔하넹

vowels = 'aeiou'
words = 'Life is too short, you need python!'

result = []
for x in words:
    if x not in vowels:
        result.append(x)

print(result) # 주의할 것!!! 이렇게 출력하면 ['L', 'f', ' ', 's', ' ', 't', ' ', 's', 'h', 'r', 't', ',', ' ', 'y', ' ', 'n', 'd', ' ', 'p', 'y', 't', 'h', 'n', '!']
print(''.join(result)) #조인해주기 Lf s t shrt, y nd pythn!


#또다른 방법
#list comprehension
result = [x for x in words if x not in vowels]
print(''.join(result))