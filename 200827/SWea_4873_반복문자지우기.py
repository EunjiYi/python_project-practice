T = int(input())

for tc in range(1, T+1):
    strstr = list(input())
    stack = []


    for s in strstr:
        #stack이 비었거나, 문자와 스택 제일 위의 값이 다르면 push
        if not stack or s != stack[-1]:
            stack.append(s)

        #stack에 값이 있고, 그 값과 문자가 같으면 pop
        elif stack and s == stack[-1]:
            stack.pop()

    print('#{} {}'.format(tc, len(stack)))