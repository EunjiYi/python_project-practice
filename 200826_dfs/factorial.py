

def fact(n):
    if n == 1:  #기저조건, basic 파트
        return 1
    else:       # inductive 파트(유도파트)
        return n * fact(n-1)

print(fact(4))