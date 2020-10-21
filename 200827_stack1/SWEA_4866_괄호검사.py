T = int(input())
for tc in range(1, T+1):

    strstr = input()
    stack = []

    def getResult():
        for s in strstr:
            if s == "(" or s == "{":
                stack.append(s)

            elif s == ")" or s=="}":
                if len(stack) == 0:
                    return 0
                elif (s == ")" and stack[-1] != "(") or (s == "}" and stack[-1] != "{"):
                    return 0
                else:
                    stack.pop()

        if len(stack) == 0:
            return 1
        else:
            return 0

    print("#{} {}".format(tc, getResult()))



