class dmath:
    def __init__(self):
        pass

    def calcPower(self, num, power):
        if power == 0:
            return 1
        
        return num * self.calcPower(num, power - 1)


def Sum(num1, num2):
    return num1 + num2