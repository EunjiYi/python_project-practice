def brute(t, p):
    i, j = 0, 0
    while j < len(p) and i < len(t):
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == len(p):
        return i - len(p)
    else:
        return -1

text = "TTTTTAACCA"
pattern = "TTA"
print(brute(text, pattern))

#사실 이 한 줄로 끝남 ㅋㅋ
print(text.find(pattern))