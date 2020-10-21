# 이 라이브러리는 최소힙만 지원한다.
import heapq
heap = [7, 2, 5, 3, 4, 6] #list
print(heap) #[7, 2, 5, 3, 4, 6]
heapq.heapify(heap)
print(heap) #[2, 3, 5, 7, 4, 6]

heapq.heappush(heap, 1)
print(heap) #[1, 3, 2, 7, 4, 6, 5]

while heap: #하나씩 순서대로 빼보자.
    print(heapq.heappop(heap), end = " ")  #1 2 3 4 5 6 7
print()

##################최대힙만들어보자
temp = [7, 2, 5, 3, 4, 6]
heap2 = []
for i in range(len(temp)):
    heapq.heappush(heap2, (-temp[i]))  #이 라이브러리가 최소힙을 지원하니까 -1붙여서 최소힙처럼 구하고, -1곱해서 리턴해주면 된다.
heapq.heappush(heap2, (-1))
print(heap2) #[(-7, 7), (-4, 4), (-6, 6), (-2, 2), (-3, 3), (-5, 5), (-1, 1)]

while heap2:
    print(heapq.heappop(heap2) * -1, end = " ")  #7 6 5 4 3 2 1