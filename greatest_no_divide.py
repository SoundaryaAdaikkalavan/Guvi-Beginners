x,y=map(int,input().split())
a=[]
for i in range(y,0,-1):
    if x%i==0 and y%i==0:
        a.append(i)
print(max(a))  
