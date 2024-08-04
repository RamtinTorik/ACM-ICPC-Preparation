a = input()
b = input()

c = int(a[::-1])
d = int(b[::-1])
if c < d:
    print(f"{a} < {b}")
elif c == d:
    print(f"{a} = {b}")
else:
    print(f"{b} < {a}")
