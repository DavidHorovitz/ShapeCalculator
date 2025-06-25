from calculator import Shape
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
        self.name="rectangle"

    def get_area(self):
        return self.length*self.width

    def get_perimeter(self):
        return self.length*2+self.width*2