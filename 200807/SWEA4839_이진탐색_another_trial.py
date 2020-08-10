

def binarySearch(s, e, key):
    l, r = s
    cnt = 0
    while l <= r:
        middle = int((l + r) / 2)
        cnt += 1
        if key == middle:
            break
        elif key < middle:
            r = middle
        else:
            l = middle
    return cnt

