T = 10
for tc in range(1,T+1):
    N = int(input())
    formula = input()

    stack = []
    numbers = []

    icp = {'*':2, '+':1, '(':3}
    isp = {'*':2, '+':1, '(':0}

    for i in range(N):
        if formula[i].isdigit():
            numbers.append(formula[i])

        else:
            if not stack:
                stack.append(formula[i])
                continue
            elif stack:
                if formula[i] == ')':
                   while stack[-1] != '(':
                       numbers.append(stack.pop())
                   stack.pop()
                elif icp[formula[i]] > isp[stack[-1]]:
                    stack.append(formula[i])
                else:
                    while icp[formula[i]] <= isp[stack[-1]]:
                        numbers.append(stack.pop())
                    stack.append(formula[i])

    for i in range(len(numbers)):
        if numbers[i].isdigit():
            stack.append(numbers[i])
        else:
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            if numbers[i] == "+":
                result = num1 + num2
            elif numbers[i] == "*":
                result = num1 * num2

            stack.append(str(result))

    print(f'#{tc} {stack[0]}')