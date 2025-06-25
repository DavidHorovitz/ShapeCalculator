from calculator import Rectangle, Square, Triangle, Circle, Hexagon


# class Menu():
def re():
    user_param1=input("enter the length")
    user_param2=input("enter the width")
    return user_param1,user_param2
def sq():
    user_param=input("enter 1 parameters")
def menu():
       myInput=input("What do you want to calculate?\nRectangle click 1\nSquare click 2\nTriangle click 3\nCircle click 4\nHexagon click 5\n")
       match myInput:

           case "1":
               p1, p2 = re()
               return Rectangle(int(p1) ,int(p2))
           case "2":
               return Square()
           case "3":
               return Triangle()
           case "4":
               return Circle()
           case "5":
               return Hexagon()
           case default:
               return "nothing"
print(menu())