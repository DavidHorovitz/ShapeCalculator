class Shape:

    def init(self):
        self.name="name"
    def get_area(self):
     pass
    def get_perimeter(self):
        pass
    def __str__(self):
       return self.name
    def __add__(self, self2):
        return self.get_area() + self2.get_area()




class Rectangle(Shape):
    '''
    a class thet calculate rectangle
    '''
    def __init__(self,length,width):
        self.length=length
        self.width=width
        self.name="rectangle"

    def get_area(self):
        ''' the '''
        return self.length*self.width

    def get_perimeter(self):
        return self.length*2+self.width*2

    # def __add__(self, self2):
    #     return self.get_area() +self2.get_area()

    # def __str__(self):
    #     return



class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)
        self.name ="square"

    # def get_area(self):
    #     return self.side*self.side

    # def __str__(self):
    #     return "Square"


class Triangle(Rectangle):
    def __init__(self,length,width):
        super().__init__(self.length,self.width)
        self.length=length
        self.width=width
        self.name ="triangle"

    def get_area(self):
        return (self.length * self.width)/2
    def get_perimeter(self):
        return self.length+self.width+math.sqrt(self.length**2+self.width**2)
    # def __str__(self):
    #     return "triangle"

import math

class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius
        self.name ="circle"
    def get_area(self):
        return math.pi*self.radius**2

    def get_perimeter(self):
        return (self.radius*2)*math.pi
    def __add__(self, self2):
        return self.get_area() +self2.get_area()
    # def __str__(self):---
    #     return "Circle"

class Hexagon(Shape):
    def __init__(self, side):
        self.side=side
        self.name ="hexagon"
    def get_area(self):
        return (3*math.sqrt(3)*(self.side**2)) / 2

    def get_perimeter(self):
        return self.side*6
    def __add__(self, self2):
        return self.get_area() +self2.get_area()
    # def __str__(self):
    #     return "Hexagon"





a=Rectangle(10,5)
# print(a.get_area())
# b=Square(12)
# print(b)
# c=Triangle(3,4)
# print(c.get_area())
# print(c)
# d=Square(4)
# f=Square(2)
# print(d+f)