a = input()
r = 0
y = 0
g = 0
for i in a:
    if i == 'R':
        r += 1
    elif i == 'Y':
        y += 1
    else:
        g += 1

if (r == 3) or (r == 2 and y == 2) or (g == 0):
    print('nakhor lite')
else:
    print('rahat baash')
