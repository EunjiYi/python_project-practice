# import sys
# sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1, T+1):
    data = list(input().split())

    stack = []

    def forth():
        for i in range(len(data)):
            #print(stack)
            if i == len(data)-1 and data[i] == '.':
                if len(stack) == 1:
                    return stack[0]
                else:
                    return 'error'

            # 숫자면 append
            elif data[i].isdigit():
                stack.append(data[i])

            # 연산자면 숫자 2개 pop
            else:
                # 스택에 아무것도 없거나 하나밖에 없을때
                if not stack or len(stack) == 1:
                    return 'error'
                else:
                    num2 = int(stack.pop())
                    num1 = int(stack.pop())
                    if data[i] == '+':
                        result = num1 + num2
                    elif data[i] == '*':
                        result = num1 * num2
                    elif data[i] == '-':
                        result = num1 - num2
                    else:
                        result = num1 // num2
                    stack.append(str(result))

    print(f"#{tc} {forth()}")