n,m=map(int,input().split())#input
c=list(map(int,input().split()))#list1
a=list(map(int,input().split()))#list2
b=list(map(int,input().split()))#list3
d=0
for i in range(0,len(b)):
    a.append(b[i])
    if d==0:
        print(max(a),end="")
        d+=1
    else:
        print("",max(a),end="")
