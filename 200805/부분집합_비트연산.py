arr = [1,2,3]

N = len(arr)

for i in range(1 << N):  #다른 언어는 거듭제곱을 나타내는 연산자가 없는데 파이썬은 있어서
                        # 이게 된다. for i in range(2 ** N):
    for j in range(N):
        if i & (1 << j):
            print(arr[j], end = " ")
    print()
print()