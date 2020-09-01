import sys
sys.stdin = open('input.txt', 'r')
T = 10
for tc in range(1,T+1):
    N = int(input())
    Data = input()

    stack = []
    num = []

    # 우선순위가 헷갈려서 먼저 적어놓음
    icp = {'*':2, '+':1, '(':3} #넣을때
    isp = {'*':2, '+':1, '(':0} #스택안

    #Step 1: 중위 => 후위 표기법 변경
    for i in range(N):
        #피연산자인 경우: 숫자 리스트 넣기
        if Data[i].isdigit():
            num_lst.append(Data[i])

        #연산자인 경우
        else:
            #stack이 빈 경우 => 무조건 append(여는 괄호의 case)
            if not stack:
                stack.append(Data[i])
                continue

            #stack이 비지 않은 경우
            elif stack:
                #닫는 괄호인 경우, 여는 괄호가 나올 때 까지 pop
                if Data[i] == ')':
                   while stack[-1] != '(':
                       num_lst.append(stack.pop())
                   stack.pop()

                #icp & isp 비교
                elif icp[Data[i]] > isp[stack[-1]]:
                    stack.append(Data[i])

                else:
                    #icp가 isp 보다 작으면 계속 pop & 연산자 리스트에 append
                    while icp[Data[i]] <= isp[stack[-1]]:
                        num_lst.append(stack.pop())
                    stack.append(Data[i])

    #print(num_lst)

    #step 2: 계산
    for i in range(len(num_lst)):
        if num_lst[i].isdigit():
            stack.append(num_lst[i])

        else:
            num2 = int(stack.pop())
            num1 = int(stack.pop())

            if num_lst[i] == "+":
                result = num1 + num2
            elif num_lst[i] == "*":
                result = num1 * num2

            stack.append(str(result))

    print(f'#{tc} {stack[0]}')