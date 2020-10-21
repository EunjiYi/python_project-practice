# import sys
# sys.stdin = open('input.txt', 'r')
T = 10
for tc in range(1,T+1):
    N = int(input())
    formula = input()

    # 연산자를 넣을 스택
    stack = []
    # 피연산자+스택에서 빠진 연산자를 넣을 숫자리스트
    numbers = []

    # 우선순위가 헷갈려서 딕셔너리로 먼저 적어놓음
    # 우선순위 = 숫자가 클수록 우선순위가 높은 것.
    icp = {'*':2, '+':1, '(':3} #토큰상태일때, 즉 스택 넣기전 바깥에서 우선순위
    isp = {'*':2, '+':1, '(':0} #스택안에서의 우선순위

    #Step 1: 중위표기법 -> 후위표기법 바꾸기
    # 중위표기법에서,
    # 숫자(피연산자면) numbers에 넣기
    # 연산자라면 stack에 넣기
    for i in range(len(formula)):
        #피연산자인 경우: 숫자 리스트 넣기
        if formula[i].isdigit():
            numbers.append(formula[i])

        #연산자인 경우: stack에 넣을 수 있는지 아닌지 우선순위로 판단하기
        else:
            # stack이 빈 경우 => 무조건 append
            # 맨 처음 시작이 여는 괄호니까 여는 괄호가 들어간다.
            if not stack:
                stack.append(formula[i])
                continue

            #stack에 무언가 들어있을 때
            elif stack:
                #닫는 괄호인 경우, 여는 괄호가 나올 때까지 pop한다.
                if formula[i] == ')':
                   while stack[-1] != '(':
                       numbers.append(stack.pop())
                   stack.pop()

                #닫는 괄호가 아닌 경우에는, 우선순위 비교하기
                # 넣으려는 것이 스택 제일 위에 있는 것보다 우선순위가 높으면 바로 넣으면 된다.
                elif icp[formula[i]] > isp[stack[-1]]:
                    stack.append(formula[i])

                # 넣으려는 것이 스택 제일 위에 있는 것보다 우선순위가 낮으면 계속 pop한다.
                # 이때 우선순위가 같아도 pop해야한다.
                # 무조건 넣으려는 것이 우선순위가 높아야함.
                else:
                    while icp[formula[i]] <= isp[stack[-1]]:
                        numbers.append(stack.pop())
                    stack.append(formula[i])

    #print(numbers)

    #step 2: 후위표기법으로 계산한다.
    # 후위표기법에서,
    # 숫자(피연산자면) stack에 넣기
    # 연산자라면 numbers에 넣기
    for i in range(len(numbers)):
        # numbers에 들어있는 값이 수라면(피연산자라면)
        if numbers[i].isdigit():
            stack.append(numbers[i]) #스택에 넣는다.
        # numbers에 들어있는 값이 연산자라면, 스택에서 2개를 뽑는다.
        # +, -, * , /가 이항연산자라서 2개를 뽑는 것임.
        else:
            # 이 때 주의사항은 나중에 뽑는 것이 뒤로 가야함!!! 그래서 연산순서가 맞다 조심하기
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            #실제계산시작
            if numbers[i] == "+":
                result = num1 + num2
            elif numbers[i] == "*":
                result = num1 * num2

            # 이거 자꾸 까먹는다 ㅜㅜㅜㅜ 계산했으면 그 결과 다시 스택에 넣어야함!!!!!
            stack.append(str(result))

    print(f'#{tc} {stack[0]}')