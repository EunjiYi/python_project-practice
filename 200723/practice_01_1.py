def my_abs(x):
    if type(x) == complex:
        #print(x.real, x.imag)
        return (x.real**2 + x.imag**2) ** 0.5
    else:
        if x < 0:
            return x * -1
        elif x == 0:
            return x ** 2    #my_abs(-0.0) => 0.0 이걸 어떡하나 했는데 그냥 제곱해버리면 됐군!
        else:
            return x

print(my_abs(3+4j))  # 5.0
print(my_abs(-0.0))  # 0.0
print(my_abs(0.0))  #0.0
print(my_abs(-5))  #5
print(abs(3+4j), abs(-0.0), abs(-5))  #5.0   0.0   5