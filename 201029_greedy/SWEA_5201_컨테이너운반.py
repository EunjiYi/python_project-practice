import sys
sys.stdin = open('123.txt', 'r')

for tc in range(1, int(input())+1):

    n, m = map(int, input().split())
    haw = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    result = 0
    while len(haw) and len(truck):
        if max(haw) <= max(truck):
            result += max(haw)
            haw.remove(max(haw))
            truck.remove(max(truck))
        else:
            haw.remove(max(haw))

    print("#{} {}".format(tc, result))