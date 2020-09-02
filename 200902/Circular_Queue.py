# front, rear를 이용
SIZE = 4
# 초기 공백큐 생성
# 크기가 SIZE인 1차원 배열 생성
# front와 rear를 0으로 초기화
Q = [0] * SIZE
front, rear = 0, 0

def enQueue(item):
    global rear
    if (rear + 1) % SIZE == front:  # full
        print("Queue Full")
    else:
        rear = (rear + 1) % SIZE  # rear += 1
        Q[rear] = item

def deQueue():
    global front
    if front == rear: #rear는 읽기(read)만 하니까 global 설정 안해도됨
        print("Queue Empty")

    else:
        front = (front + 1) % SIZE
        return Q[front]

def Qpeek():
    if front == rear:
        print("Queue Empty")
    else:
        return Q[(front + 1) % SIZE]


# 파이썬에서는 append(), pop(0)쓴다.
# 파이썬에서는 선형큐와 원형큐의 차이가 별로 없다.

enQueue(1)
enQueue(2)
enQueue(3)
print(deQueue())
print(deQueue())
print(deQueue()) # 여기까지 찍었을 때 [0, 1, 2, 3] 맨 앞 front를 비우고 채웠다.

enQueue(4)
print(deQueue())

enQueue(5)
print(deQueue())

print(Q)
