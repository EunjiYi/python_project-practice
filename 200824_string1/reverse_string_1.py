def str_rev(str):
    # str - > list
    arr = list(str)

    #swap
    for i in range(len(arr) // 2):
        arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]

    #list -> str
    str = "".join(arr)
    return str


str = "algorithm"
str = str_rev(str)
print(str)


# 더 쉽게
s = "algorithm"
s = s[::-1]
print(s)


#reverse 함수
str2 = "algorithm"
arr2 = list(str2)
arr2.reverse()
str2 = "".join(arr2)
print(str2)