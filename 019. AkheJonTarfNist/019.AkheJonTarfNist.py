mylist = ["shanbe", "1shanbe", "2shanbe", "3shanbe", "4shanbe", "5shanbe", "jome"]
for i in range(3):
    a = int(input())
    b = list(input().split(" "))
    for _ in b:
        if _ in mylist:
            mylist.remove(_)
print(len(mylist))

