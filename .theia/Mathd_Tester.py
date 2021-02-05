import dmath

m, n = 11, 4

for i in range(1, m + 1):
    ans = dmath.getPower(i, n)
    print("{} ** {} = {}".format(i, n, ans))