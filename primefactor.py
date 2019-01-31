def isprime(x):#prime
    c=0
    for i in range(2,x):
        if x%i==0:
            break
    else:
        c=c+1
    if c==1:
        return 1
    else:
        return 0
v=[]
n=int(input())
for i in range(2,n+1):
    if n%i==0:
        if isprime(i)==1:
            v.append(i)
for i in range(len(v)):
    if i==0:
        print(v[i],end="")
    else:
        print("",v[i],end="")
