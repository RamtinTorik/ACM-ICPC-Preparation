a = int(input())
confrim = False
if a!=0:
    confrim = True

l = list()
l.append(a) 

while confrim:
    a = int(input())
    if a == 0:
        break
    else:
        l.append(a)

for i in range(len(l)):
    print(l[-i-1])