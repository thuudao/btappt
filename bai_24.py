a, b, c = map(float, input().split())
s = (a + b + c) / 2
print(f"{(s * (s - a) * (s - b) * (s - c)) **0.5:.1f}")
