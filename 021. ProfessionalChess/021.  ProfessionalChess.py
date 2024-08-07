mylist = list(input().split(' '))
mylist = [int(_) for _ in mylist]
newlist = []
for i in range(6):
    if i == 0 or i == 1:
        newlist.append(1-mylist[i])
    elif i == 2 or i == 3 or i == 4:
        newlist.append(2-mylist[i])
    else:
        newlist.append(8-mylist[i])
for i in newlist:
    print(i, end=' ')
