class Stack:

    def __init__(self,n):
        self.top = -1
        self.s = [0] * n
    def push(self,data):

        self.s[self.top+1] = data
        self.top += 1

    def pop(self):
        if self.top == -1:
            return None
        value = self.s[self.top]
        self.s[self.top] = 0
        self.top -= 1
        return value

my_stack = Stack(5)
my_stack.push(5)
my_stack.push(4)
my_stack.push(3)
my_stack.push(2)
my_stack.push(1)
print(my_stack.pop())
my_stack.push(1)
print(my_stack.pop())
my_stack.push(1)
print(my_stack.pop())


tmp = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]
adj = [[] for _ in range(7+1)]
visit = [0] * (7+1)

for i in range():
    

stack = Stack(7)
stack.push(1)



