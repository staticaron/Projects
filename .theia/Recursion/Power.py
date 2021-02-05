class Power:
    def __init__(self):
        pass

    def calcPower(self, m, n):
        #Base
        if n == 0:
            return 1

        return m * self.calcPower(m, n - 1)


#__main__
print("Welcome to the power command")
power = Power()

#m, n = [int(x) for x in input().split()]
m, n = 5, 7

for i in range(1, m classclasss+ 1):
    ans = power.calcPower(i, n)
    print("{} ** {} = {}".format(m, n, ans))