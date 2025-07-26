n = int(input())
if n >= 2:
    print(2, end= " ")
    for i in range(3, n + 1, 2):
        ok = True
        j = 2
        while j * j <= i:
            if i % j == 0:
                ok = False
                break
            j += 1
        if ok == True:
            print(i, end= " ")
