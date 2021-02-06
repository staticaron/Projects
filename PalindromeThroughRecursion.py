def CheckPalindrome(_str):
    #Base
    if len(_str) == 1 or len(_str) == 0:
        return True

    if _str[0] == _str[len(_str) - 1]:
        return CheckPalindrome(_str[1:len(_str) - 1])
    else:
        return False

def main():
    listWords = ["abcdef", "akaka", "devgame", "jahaj"]
    for i in listWords:
        ans = CheckPalindrome(i)
        print("{} is a palindrome : {}".format(i, ans))

if __name__ == "__main__":
    main()