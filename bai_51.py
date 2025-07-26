a, b, c = map(float, input().split())
delta = b * b - 4 * a * c
if delta < 0:
    print("Vo nghiem")
elif delta == 0:
    print("Nghiem kep:", -b/ (2 * a))
else:
    print(f"x1 = {(-b - delta **0.5)/ (2 * a)}, x2 = {(-b + delta **0.5)/ (2 * a)}")
