n = int(input())
ans = 1
i = 2
while i * i <= n:
    if n % i == 0 and n / i != i:
        ans += (i + n / i)
    elif n % i == 0:
        ans += i
    i += 1
if ans == n:
    print("La so hoan hao")
else:
    print("Khong phai so hoan hao")
