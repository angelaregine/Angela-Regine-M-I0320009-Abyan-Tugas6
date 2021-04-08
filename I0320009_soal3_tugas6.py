n = 24
for a in range(10, n + 1):
    if a > 1:
        for i in range(2,a):
            if (a % i) == 0:
                print(a, "bukan bilangan prima")
                break
        else:
            print(a, "adalah bilangan prima")