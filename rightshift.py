n,k=map(str,input().split())
l=list(map(int,input().split()))
c=0
for i in k:
    temp=l[-1]
    del(l[-1])
    l.insert(0,temp)
for i in range(0,len(l)):
    if(c==0):
        print(l[i],end="")
        c=c+1
    else:
        print("",l[i],end="")
