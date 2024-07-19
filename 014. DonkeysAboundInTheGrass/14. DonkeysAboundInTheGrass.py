a ,b ,l = map(int, input().split())

# a = int(input())
# b = int(input())
# l = int(input())

if l%2==0:
    o = (a+b)*(l/2)
else:
    o = (a+b)*((l-1)/2)+a
    
print(int(o))