boxes = [7,4,2,0,0,6,0,7,0]

#착안점: 현재 오른쪽이 비어있거나 높이가 자신보다 작은 상자이면 낙차를 하나씩 더한다.
#모든 열의 낙차를 구하고, 그중에서 가장 큰 낙차를 반환(출력)한다.

#문제를 쪼개서 생각하자. - 가장 왼쪽에 있는 열의 낙차부터 구하자.
# target = boxes[0]
# cnt = 0
# for i in range(1, len(boxes)): #1번열부터 끝까지 순회
#     #target보다 작은 값을 가지는 열의 수를 계산
#     if boxes[i] < target:
#         cnt += 1
# print(cnt)

#max나 min값을 저장하는 변수를 선언할 때에는 분명한 이유가 있어야한다.
max_cnt = 0 # 0으로 초기화한 이유 = 만약 방안이 모두 박스로 가득차있다면 0이니가.
#하나 성공했으면 여러 열 해보자.
for j in range(len(boxes)): #마지막열은 항상 낙차가 0이기 때문에 len(boxes)-1해도 된다.
    target = boxes[j]
    cnt = 0
    for i in range(j+1, len(boxes)):
        if boxes[i] < target:
            cnt += 1
    #print(cnt)
    if cnt > max_cnt:
        max_cnt = cnt
    #반복문 돌 때마다 cnt값을 비교해서 더 큰 값을 남긴다.
print(max_cnt)


