a=input()
n=len(a)
res=""
if(n%2==0):
    mid2=len(a)//2
    mid1=mid2-1
    for i in range (0,n):
        if(i==mid1 or i==mid2):
            res=res+'*'
        else:
            res=res+a[i]
if(n%2!=0):
    mid2=len(a)//2
    for i in range (0,n):
        if(i==mid2):
            res=res+'*'
        else:
            res=res+a[i]
print(res)
