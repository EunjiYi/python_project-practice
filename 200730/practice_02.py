class Point:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
    
class Rectangle(Point): 
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def get_area(self):
        return abs(self.p1.x - self.p2.x) * abs(self.p1.y - self.p2.y)   #self.p1.x # 쩜엑스, 쩜와이만 하면 됐다. 
        #다른 방법 튜플로 호출: self.p1(0)과 self.p1(1)
    
    def get_perimeter(self):
        return 2 * (abs(self.p1.x - self.p2.x) + abs(self.p1.y - self.p2.y))
    
    def is_square(self):
        if abs(self.p1.x - self.p2.x) == abs(self.p1.y - self.p2.y):
            return True
        else:
            return False


p1 = Point(1,3)   
p2 = Point(3,1)
r1 = Rectangle(p1, p2)   
print(r1.is_square())   #True
p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())     #4
print(r1.get_perimeter())   #8
print(r1.is_square())  #True
p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())   #9
print(r2.get_perimeter())  #12
print(r2.is_square())  #True
p5 = Point(6, 2)
p6 = Point(3, 4)
r2 = Rectangle(p5, p6)
print(r2.get_area())   #9
print(r2.get_perimeter())  #12
print(r2.is_square())  #False