r ,c = map(int, input().split())

if c > 10:
    direction = "Left"
else:
    direction = "Right"
    
a = 11 - r

if direction == "Left":
    b = 11 - (20 - c)
else:
    b = c
    
print(direction, a, b, end=" ")

