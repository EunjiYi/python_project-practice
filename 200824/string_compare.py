def strcmp(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        i = 0
        while i < len(s1) and i < len(s2):
            if s1[i] != s2[i]:
                return False
            i += 1 #증감
    return True

a = "abc"
b = "abd"

print(strcmp(a, b)) # True False

#한 자씩 한 자씩 비교를 해나간다. 