x1, y1, x2, y2 = map(float, input().split())
x = x1 - x2
y = y1 - y2
if x < 0:
    x *= (-1)
if y < 0:
    y *= (-1)
print((x * x + y * y) ** 0.5)
