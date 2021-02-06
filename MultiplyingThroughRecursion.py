def Multiply(num1, num2):
    #Base
    if num2 == 1:
        return num1
    
    return Multiply(num1, num2 - 1) + num1

def main():
    ans = Multiply(2838, 4)
    print(ans)

if __name__ == "__main__":
    main()