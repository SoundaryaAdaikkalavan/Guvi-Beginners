def isodd(n):
      if n%2!=0:
            return 1
      else:
           return 0
v=[]
n=int(input())
for i in range(1,n+1):
    if n%i==0:
        if isodd(i)==1:
            v.append(i)
for i in range(len(v)):
    if i==0:
        print(v[i],end="")
    else:
        print("",v[i],end="")
