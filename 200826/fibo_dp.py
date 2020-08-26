#
# f = [0, 1]
# for i in range(2, 7 + 1):
#     f.append(f[i-1] + f[i-2])
# print(f[7])

def fibo3(n):
    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[i-1]+f[i-2])
    return f[n]

print(fibo3(1000))

#와 바로 나온다...
#파이썬은 big integer를 지원한다. 그래서 바로 큰 수가 잘 나옴.