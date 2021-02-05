def calcPower(num, power):
        if power == 0:
            return 1
        
        return num * self.calcPower(num, power - 1)


def calcSum(num1, num2):
    return num1 + num2
