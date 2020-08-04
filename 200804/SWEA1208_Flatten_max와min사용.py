for tc in range(1, 11):
    count = int(input()) #덤프횟수
    grounds = list(map(int, input().split()))
    for _ in range(count):
        max_index, min_index = grounds.index(max(grounds)), grounds.index(min(grounds))
        grounds[max_index] -= 1
        grounds[min_index] += 1

    #print('#{} {}'.format(tc, grounds[max_index] - grounds[min_index])) ->이렇게 하니까 결과값이 다 2만큼 작게나옴!
    print('#{} {}'.format(tc, max(grounds)-min(grounds)))  #위에서 grounds[max_index] -= 1하고 max값이 바뀌었을 수도 있음. 그러니 grounds[max_index]로 하지말고 max(grounds)로 해야함


'''
답
#1 13
#2 32
#3 54
#4 25
#5 87
#6 14
#7 39
#8 26
#9 13
#10 29
'''
