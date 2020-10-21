# front, rear를 이용
Q = [0] * 100
front, rear = -1, -1

def enQueue(item):
    global rear
    if rear == len(Q) -1:
        print("Queue Full")
    else:
        rear = rear + 1 # rear += 1
        Q[rear] = item

def deQueue():
    global front
    if front == rear: #rear는 읽기(read)만 하니까 global 설정 안해도됨
        print("Queue Empty")

    else:
        front += 1
        return Q[front]

def Qpeek():
    if front == rear:
        print("Queue Empty")
    else:
        return Q[front + 1]

enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())  # 이걸 찍었을 때
### Queue Empty만 나오는게 아니고 None도 나오는 이유
# 함수의 경우에는 마지막 문장에는'항상' return 문장이 있어요
# 마지막 return은 안써도 되요. 생략하면 함수가 종료되면서 None을 리턴합니다.
# 그냥 return 이라고 쓰는거랑 같은거에요
# 17번째 줄에 deQueue() 함수의 return이 생략되어 있는거고, if에 걸리게 되면 아무것도 반환하지 않는 return문장에 의해서 함수가 종료되니까 deQueue 함수는 None을 반환합니다.

### 아~ 이해됐어요! 그러면 None 안나오게는 못하는거죠? return을 적어도 나오니까요 ㅜㅜ
# 그렇죠. 그런데 일반적인 함수들도 저렇게 인덱스가 없을때 뭔가를 실행하려고 하면, None이나 예외 발생 둘중에 하나에요

print(Q)