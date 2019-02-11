n,m=map(int,input().split())
c=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
d=0
for i in range(0,len(b)):
    a.append(b[i])
    if d==0:
        print(max(a),end="")
        d+=1
    else:
        print("",max(a),end="")
