n = int(input())
tot = 0
lst = list(map(float, input().split()))
for i in range(n):
    tot += lst[i]
print(f"Diem TB: {tot / n:.2f}, Xep loai:", end= " ")
n = tot / n
if n >= 9.0:
    print("Xuat sac")
elif n >= 8.0:
    print("Gioi")
elif n >= 6.5:
    print("Kha")
elif n >= 5.0:
    print("Trung binh")
else:
    print("Yeu")
