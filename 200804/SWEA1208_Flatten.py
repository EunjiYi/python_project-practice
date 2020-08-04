for tc in range(1, 11):
    cnt = int(input()) #덤프횟수
    grounds = list(map(int, input().split()))

    #파이썬에 기본적으로 max min이라는 함수가 있기 때문에 변수이름 max랑 min으로 하지 말자.

    for _ in range(cnt):

        def get_max(target_list):
            max_value = target_list[0]
            for i in range(len(target_list)):
                if target_list[i] > max_value:
                    max_value = target_list[i]
            return max_value

        def get_min(target_list):
            min_value = target_list[0]
            for i in range(len(target_list)):
                if target_list[i] < min_value:
                    min_value = target_list[i]
            return min_value

        max_index, min_index = grounds.index(get_max(grounds)), grounds.index(get_min(grounds))
        grounds[max_index] -= 1
        grounds[min_index] += 1

    print('#{} {}'.format(tc, get_max(grounds)-get_min(grounds)))