def two_func(one, two):
    a = int(input())
    b = int(input())
    if a < b:
        for i in range(a, b + 1):
            print(i)
    else:
        for i in range(a, b - 1, -1):
            print(i)
two_func(2,5)