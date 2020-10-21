#c style



def push(item):
    global top
    if top > 100 - 1:
        return
    else:
        top += 1
        stack[top] = item

def pop(): #isEmpty
    global top
    if top == -1:
        print("Stack is Empty!!!")
        return
    else:
        result = stack[top]
        top -= 1
        return result

#python 전역변수
# top: 값형 R -> 그래서 값형을 변경하고 싶으면 glbal 설정을 해줘야한다.
# stack: 참조형 RW

top = -1
stack = [0] * 100

push(1)
push(2)
push(3)
print(pop())
print(pop())
print(pop())