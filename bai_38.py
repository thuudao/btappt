n = int(input())
lst = list(map(int, input().split()))
ans = 0
for i in range(n):
    if i == 0:
        ans = lst[0]
    else:
        ans = max(ans, lst[i])
print(ans)
