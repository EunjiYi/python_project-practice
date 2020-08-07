#x<y<z<50

# 반복문 - 3중 for문
result = []
for i in range(1, 50):
    for j in range(i,50): #나는 다 1~50까지로 했는데 생각해보니 x<y<z<50이었네. 조금이라도 반복횟수 줄이자.
        for k in range(j, 50):
            if i**2 + j**2 == k**2:
                result.append((i, j, k)) #어팬드 괄호 치는거 계속 틀림. 주의
print(result)

# list comprehension
#result가 리스트니까 대괄호 !
result = [(i, j, k) for i in range(1, 50) for j in range(i, 50) for k in range(j, 50) if i**2 + j**2 == k**2]

print(result)