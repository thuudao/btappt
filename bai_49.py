a, b = map(int, input().split())
k = input()
if k == '+':
    print(f"{a + b:.1f}")
elif k == '-':
    print(f"{a - b:.1f}")
elif k == '*':
    print(f"{a * b:.1f}")
else:
    if b == 0:
        print("Phep toan khong hop le")
    else:
        print(f"{a / b:.1f}")
