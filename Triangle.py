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
        area = a

    def __init__(self, side1, side2, angle1):
        self.side1 = side1
        self.side2 = side2
        self.angle1 = angle1
    
    def printDetails(self):
        print("Sides : ")
        print("\t", self.side1, "\n\t", self.side2, "\n\t", self.side3, "\n")
        print("Area :", self.area)

#__main__

tri_1 = Triangle(10, 20, 30)
tri_1.printDetails()