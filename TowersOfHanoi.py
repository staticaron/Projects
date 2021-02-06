def Hanoi(n, _from, _to, _spare):
    if len(n) == 1:
        print("{} was transfered from {} to {}".format(n[0], _from, _to))
        return

    Hanoi(n[:len(n) - 1], _from, _spare, _to)
    Hanoi(n[len(n) - 1:len(n)], _from, _to, _spare)
    Hanoi(n[:len(n) - 1], _spare, _to, _from)

frm = "BaseTower"
to = "To tower"
spr = "Spare tower"
lst = [1, 2, 3]

def main():
    Hanoi(lst, frm, to, spr)
    print("To Tower is {}".format(to))
if __name__ == "__main__":
    main()