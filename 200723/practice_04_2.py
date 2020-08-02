#형변환 이용 - 와 이 생각을 못했다. 

def sum_of_digit2(number):
    total =0
    
    for w in str(number):  # str 은 순회가능하니까!
        total += int(w) #연산할 때는 int로
    return total

print(sum_of_digit2(1234)) #=> 10
print(sum_of_digit2(4321)) #=> 10