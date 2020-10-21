# 괄호가 정상적이면 True, 아니면 False
# target: 괄호 검사 대상 문자열
def check_bracket(target):
    #여는 괄호가 나오면, stack에 push
    #닫는 괄호가 나오면 stack에서 pop
    #문장이 끝났을 때, stack이 비어있으면 정상적인 괄호
    #아니라면 비정상 괄호
    #abcde(def(ef)eadfadsf)asdfadsf
    stack = list()
    for i in range(len(target)):
        #문자가 여는괄호라면 push
        #닫는괄호면 pop, pop 했는데 비어있으면 False
        if target[i] == '(':
            stack.append(target[i])
        elif target[i] == ')':
            if len(stack) == 0: # 비어있음
                return False
            stack.pop() # 비어있지 않으면 pop

    #반복문이 끝났을 때 stack이 비어있으면 True
    #아니면 False
    if len(stack) != 0:
        return False
    else:
        return True


str = "(()()())"
result = check_bracket(str)
print(result)



