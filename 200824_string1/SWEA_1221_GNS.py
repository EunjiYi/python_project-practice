T = int(input())
for tc in range(1, T + 1):
    t, N = map(str, input().split())
    N = int(N)
    new_numbers = list(map(str,input().split()))
    old_numbers = [0] * N

    decode1 = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
    # 외계숫자 -> 우리가 아는 숫자로 만들기
    for i in range(N):
        old_numbers[i] = decode1[new_numbers[i]]


    # 정렬하기
    for i in range(len(old_numbers) - 1):
        idx = i #시작점잡기
        for j in range(i + 1, len(old_numbers)):
            if old_numbers[idx] > old_numbers[j]:
                idx = j
        old_numbers[i], old_numbers[idx] = old_numbers[idx], old_numbers[i]

    

    decode2 = {0: 'ZRO', 1: 'ONE', 2: 'TWO', 3: 'THR', 4: 'FOR', 5: 'FIV', 6: 'SIX', 7: 'SVN', 8: 'EGT', 9: 'NIN'}
    # 정렬한 것을 다시 외계숫자로 만들기
    for i in range(N):
        new_numbers[i] = decode2[old_numbers[i]]

    # 결과 출력
    print("#{}".format(tc))
    for i in range(N):
        print("{}".format(new_numbers[i]), end = " ")
