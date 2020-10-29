import sys
sys.stdin = open('123.txt', 'r')

for tc in range(1, int(input())+1):
    tmp1, tmp2 = input().split()
    card = list(map(int, tmp1))
    num = int(tmp2)

    

    print("#{}".format(tc))
