x = int(input())
y = int(input())
z = int(input())


if (x**2 + y**2 == z**2 or x**2 + z**2 == y**2 or z**2 + y**2 == x**2) and (x!=0 and y!=0 and z !=0):
    print("Yes")
else:
    print("No")