calculation = { '+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y}

def postorder(node):
    if node:
        left = postorder(int(tree[node][2]))
        right = postorder(int(tree[node][3]))
        if left and right: # 연산자니까 계산해서 반환
            return calculation[tree[node][1]](left, right)
        else: # 피연산자 그대로 반환
            return int(tree[node][1])

T = 10
for tc in range(1,T+1):
    N = int(input())
    tree = [[0] * 4] + [input().split() for _ in range(N)]
    for node in range(1, N + 1):
        if len(tree[node][:]) <= 2:
            tree[node].append(0)
            tree[node].append(0)

    print("#{} {}".format(tc, int(postorder(1))))