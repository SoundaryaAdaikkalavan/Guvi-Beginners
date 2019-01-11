a,b=map(int,input().split())
c=0
for i in range(a+1,b):
    if(i%2!=0):
        if(c!=0):
            print(" ",end="")
        print(i,end="") 
        c=c+1
