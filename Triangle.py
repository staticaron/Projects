import math

class Triangle:
    side1 = 0
    side2 = 0
    side3 = 0

    angle1 = 0
    angle2 = 0
    angle3 = 0

    area = 0

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

        #Area
        s = (side1 + side2 + side3) * 0.5
        a = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
        self.area = a
    
    def printDetails(self):
        print("Sides : ")
        print("\t", self.side1, "\n\t", self.side2, "\n\t", self.side3)
        print("Angles :")
        print("\t", self.angle1, "\n\t", self.angle2, "\n\t", self.angle3)
        print("Area :", self.area)

    def __eq__(self, value):
        if self.side1 == value.side1 and self.side2  == value.side2 and self.side3 == value.side3:
            return True
        else:
            return False


#__main__

tri_1 = Triangle(side1=10, side2=20, side3=25)
tri_2 = Triangle(10, 20, 25)
tri_1.printDetails()