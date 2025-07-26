m, y = map(int, input().split())
if m == 2:
    if y % 400 == 0 or(y % 4 == 0 and y % 100 != 0):
        print(29)
    else:
        print(28)
else:
    if y == 1 or y == 3 or y == 5 or y == 7 or y == 8 or y == 10 or y == 12:
        print(31)
    else:
        print(30)
