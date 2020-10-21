def powerset(idx, sum): #tall 각 부분집합의 합을 구해서 B 보다 크면 result에 넣는 함수
     global B
     if sum >= B:
         result.append(sum)
        #여기서 return하면 안됨. 다른 경우의 수들도 다 구해야함.
     if idx >= N:
         return # 부분집합 다 구하면 이때 return

     selected[idx] = 1
     powerset(idx+1, sum + tall[idx])
     selected[idx] = 0
     powerset(idx+1, sum)


if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        N, B = map(int, input().split())
        tall = list(map(int, input().split()))
        selected = [0] * N
        result = []
        powerset(0, 0)
        minmin = min(result)
        print(f'#{tc} {abs(minmin-B)}')