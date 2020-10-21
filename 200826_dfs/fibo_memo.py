def fibo2(n):
    #global memo # memo는 전역변수인데 참조형이라서 global에 안적어도 된다.
    if n >= 2 and len(memo) <= n:
        memo.append(fibo2(n-1) + fibo2(n-2))
    return memo[n]

memo = [0, 1] # memo는 전역변수인데 참조형이라서 global에 안적어도 된다.

print(fibo2(1000)) # 1000을 못돌린다. ㅜㅜ 더 좋은방법 찾자 = > DP 해봅시다.