# stack 구현하기
# 우리가 해야할 일:   기능 / 변수 정리
# push/pop 함수작성
# 실제 데이터가 저장될 list 준비
# 마지막 데이터를 가리키는 top 변수
class Stack:
    #함수 2개 push/pop
    def __init__(self): #스택 구현에 필요한 데이터 2개 준비
        self.top = -1   #가장 뒤쪽에 있는 데이터의 인덱스
        self.s = list()

    # 데이터를 받아와서 저장하는 거니까 파라미터로 데이터를 받는다.
    def push(self,v):
        self.s.append(v)
        self.top += 1

    def pop(self):  #마지막 원소 삭제 및 반환
        value = None    #데이터가 없으면 아무것도 아닌것을 반환하기 위해서 None으로 초기화
        if self.top != -1:  # 데이터 가 있으면,
            value = self.s[self.top]
            self.s = self.s[:self.top]
            self.top -= 1
        return value

my_stack = Stack()

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
