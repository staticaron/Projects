def Staircase(n):
    #Base
    if n == 1 or n == 0:
        return 1
    if n < 0:
        return 0

    return Staircase(n-1) + Staircase(n-2) + Staircase(n-3)

#__main__

def main():
    n = 3
    ans = Staircase(n)
    print(ans)

if __name__ == "__main__":
    main()