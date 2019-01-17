N=int(input())
K=int(input())
a=list(map(int,input().split()))
count=0
for i in range (0,len(a)):
    if(a[i]==K):
        count=count+1
if(count>0):
    print("yes")
else:
    print("no")
