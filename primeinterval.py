def isprime(n):
    if(n>1):
        for i in range(2,n):
            if(n%i==0):
                return False
        else:
            return True
a,b=map(int,input().split())
c=0
for i in range(a+1,b):
    if(isprime(i)):
        if(c!=0):
            print(" ",end="")
        print(i,end="") 
        c=c+1
