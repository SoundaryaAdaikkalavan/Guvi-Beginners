n=int(input())#input
c=0
while(n>0):
    r=n%10
    c=c+r*r
    n=n//10
print(c)
