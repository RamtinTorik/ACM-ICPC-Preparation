def jam(num):
    mysum = 0
    while num!=0:
        mysum += num % 10
        num = num // 10
    return mysum
    
a = int(input())
current = jam(a)
while True:
    if len(str(current)) > 1:
        current = jam(current)
    else:
        print(current)
        break
    






