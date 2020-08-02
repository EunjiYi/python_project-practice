
class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0
    
    def __init__(self, name, breed, age=1):
        self.name = name
        self.breed = breed
        self.age = age
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1
    
    def __del__(self):
        Doggy.num_of_dogs -= 1
        
    def bark(self):
        return '왈왈!'
        
    @classmethod
    def get_status(cls):
        return f'Birth: {cls.birth_of_dogs}, Current: {cls.num_of_dogs}' 
        #print('Birth: %s' %cls.birth_of_dogs, end = ' ')  #python3.5라서 ㅋㅋㅋ 급하게 %s공부함.
        #print('Current: %s' %cls.num_of_dogs)

d1 = Doggy('초코', '푸들')
d2 = Doggy('꽁이', '말티즈')
d3 = Doggy('별이', '시츄')
d1 = Doggy('초코', '푸들')
d2 = Doggy('꽁이', '말티즈')
d3 = Doggy('별이', '시츄')

print(d1.bark()) #=> 왈왈!
print(d2.bark()) #=> 왈왈!
print(d3.bark()) #=> 왈왈!

print(Doggy.get_status()) #=> Birth: 6, Current: 3
      
