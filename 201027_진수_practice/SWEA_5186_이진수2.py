import sys
sys.stdin = open("123.txt", 'r')

def decimal_point(n):
    bit = [0] * 12
    idx = 0
    while n:
        if idx >= 12:
            return 0, 0

        tmp = n * 2
        bit[idx] = int(tmp // 1)
        n = tmp - bit[idx]
        idx += 1

    return bit, idx

for tc in range(1, int(input()) + 1):
    num = float(input())
    #print(num)
    decimal_point(num)
    result = []
    if decimal_point(num):
        result, index = decimal_point(num)

    print("#{}".format(tc), end=' ')
    if not index:
        print("overflow")
    else:
        for i in range(index):
            print(result[i], end = '')
        print()