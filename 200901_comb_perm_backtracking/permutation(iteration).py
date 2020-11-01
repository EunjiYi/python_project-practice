arr = [1, 2, 3]
N = len(arr)
for i in range(0, N):
    arr[0], arr[i] = arr[i], arr[0]

    for j in range(1, N):
        arr[1], arr[j] = arr[j], arr[1]

        for k in range(2, N):
            arr[2], arr[k] = arr[k], arr[2]
            print(arr)
            arr[2], arr[k] = arr[k], arr[2]

        arr[1], arr[j] = arr[j], arr[1]

    arr[0], arr[i] = arr[i], arr[0]