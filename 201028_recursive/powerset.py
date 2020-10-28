# 요소의 합이 0인 부분집합을 출력하라
N = 10
arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
# selected = [0] * N
selected = list()
def powerset(selected,idx):
    if idx == N:
        if sum(selected) == 0:
            print(*selected,sep=",")
        return
    selected.append(arr[idx])
    powerset(selected,idx+1)

    selected.pop()
    powerset(selected, idx + 1)

powerset(selected,0)
