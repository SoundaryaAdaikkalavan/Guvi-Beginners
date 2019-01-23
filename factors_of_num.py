n=int(input())
value=1

while(value<=n):
    if(n%value==0):
        print(format(value),end=" ")
    value=value+1
