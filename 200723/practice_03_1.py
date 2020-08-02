def snail(height, day, night):
    return int(height / (day-night))

#처음에 이렇게 짜놓고 '쉽네' 했다 ㅋㅋㅋ
#생각해보니 가장 마지막에는 미끄러지지 않는데 그걸 고려하지 않았다.
#practice_03_2.py에 다시 해봤다. 

print(snail(104, 5, 2)) #34
print(snail(100, 5, 2)) #33