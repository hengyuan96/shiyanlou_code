a = 0
while a < 100:
    a += 1
    b = int(a % 7)
    c = int(a % 10)
    d = int(a // 10)
    if b == 0:
        continue
    elif c == 7:
        continue
    elif d == 7:
        continue
    print(a)
