x = int(input())
sum = 0

for i in range(1,x):
    if x % i == 0:
        sum += i

if sum == x:
    print("YES")
else:
    print("NO")