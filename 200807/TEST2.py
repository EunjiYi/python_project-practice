#map = [ for _ in range(9)]
# map1 = [[0] * 9 for _ in range(13)]
# map2 = list(map(int, input().split())).append(0)
#
# map2.append(0)

N = 9

map1 = list(map(int, input().split()))
map1.append(0)
list(map1).append([0,0,0,0,0,0,0,0,0,0,0,0,0])
print(map1)


