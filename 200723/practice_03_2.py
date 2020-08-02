def snail(height, day, night):
    count = 0
    
    while height > 0:
        count += 1
        height -= day
        if height <= 0: 
            return count
        height += night
    return count

#착안점
#시간이 지날때마다 = 움직였을 때마다 heiht를 줄여라. 이게 0보다 작아지면 완주.

print(snail(104, 5, 2)) #34
print(snail(100, 5, 2)) #33