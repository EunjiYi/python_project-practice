def gns_sort():
    global numbers
    numbers_dic={"ZRO" : 0, "ONE" : 1, "TWO": 2, "THR":3 , "FOR": 4, "FIV": 5, "SIX": 6, "SVN" : 7, "EGT": 8, "NIN": 9}
    #버블 정렬
    for i in range(len(numbers)-1):
        for j in range(len(numbers)-1-i):
            if numbers_dic[numbers[j]] > numbers_dic[numbers[j+1]]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

#GNS
T = int(input())
for t in range(T):
    tc, N = input().split()
    N = int(N)
    #정렬을 하기 위해서는 대소 비교를 해야 하는데....
    # 글자를 그냥 그대로 가지고는 대소비교가 안됨
    # 대소비교를 위해서 dictionary를 사용
    #{"ZRO" : 0 , "ONE" : 1.....}
    numbers = input().split()
    gns_sort()
    print(tc,*numbers)