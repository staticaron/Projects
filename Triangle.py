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

        #Sides
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

        #Angles
        try:
            self.angle1 = math.degrees((  math.acos((math.pow(side2, 2) + math.pow(side3, 2) - math.pow(side1, 2))/(2*side2*side3))  ))
            self.angle2 = math.degrees((  math.acos((math.pow(side1, 2) + math.pow(side3, 2) - math.pow(side2, 2))/(2*side1*side3))  ))
            self.angle3 = math.degrees((  math.acos((math.pow(side1, 2) + math.pow(side2, 2) - math.pow(side3, 2))/(2*side1*side2))  ))
        except:
            print("Can't determine angles")
            print("Please check that sum of smaller side is always greater than the largest side")
            print("Triangle was not created.")
            return

        #Area
        s = (side1 + side2 + side3) * 0.5
        a = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
        self.area = a
    
    def printDetails(self):
        print("Sides : ")
        print("\t", self.side1, "\n\t", self.side2, "\n\t", self.side3)
        print("Angles :")
        print("\t", self.angle1, "\n\t", self.angle2, "\n\t", self.angle3)
        print("Area   :\n\t", self.area)

    def __eq__(self, value):
        thisSides = {self.side1 : 0, self.side2 : 0, self.side3 : 0}
        otherSides = {value.side1 : 0, value.side2 : 0, value.side3 : 0}
        _equality = True

        for i in thisSides.keys():

            if thisSides[i] == 1:
                continue
            
            _equalFound = False

            for j in otherSides.keys():

                if otherSides[j] == 1:
                    continue

                if i == j:
                    thisSides[i] = 1
                    otherSides[j] = 1
                    _equalFound = True
                    break
            
            _equality = _equality and _equalFound

        return _equality

#__main__


tri_1 = Triangle(10, 20, 25)
tri_2 = Triangle(22, 10, 10)

tri_2.printDetails()

ans = tri_1 == tri_2

print("Triangles are congruent {}".format(ans))



