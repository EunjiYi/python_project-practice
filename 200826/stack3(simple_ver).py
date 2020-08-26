stack = []
# 리스트를 만들어놓고 스택처럼 쓰면 된다.

stack.append(1) #push
stack.append(2)
stack.append(3)

if stack:  #len(stack) != 0
    print(stack.pop())
if stack:  #len(stack) != 0
    print(stack.pop())
if stack:  #len(stack) != 0
    print(stack.pop())
if stack:  #len(stack) != 0
    print(stack.pop()) # -> 마지막껀 실행안됨.
