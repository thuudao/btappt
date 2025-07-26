n = int(input())
if n == 1:
    print(15000)
elif n <= 5:
    print(15000 + (n - 1) * 12000)
else:
    print(15000 + 48000 + (n - 5) * 10000)
