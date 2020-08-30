###아이디어
### 괄호를 딕셔너리로 만든다.

paren = { '(': ')', '{':'}', ')':'(', '}':'{'}
for tc in range(1, int(input()) + 1):
    arr = input()

    S = []
    #한 문자씩 읽어서 처리
    ans = 1
    for ch in arr:
        if ch == '(' or ch == '{': #여는 괄호
            S.append(ch)
        if ch == ')' or ch == '}': #닫는 괄호
            #빈 스택일 경우
            if len(S) == 0:
                ans = 0; break
            t = S.pop()
            if paren[ch] != t:
                ans = 0; break

    # 빈스택인지 조사하기
    if len(S) != 0:
        ans = 0

    print(f'#{tc} {ans}')
