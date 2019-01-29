s,s1=map(str,input().split())
a=[]
b=[]
c=0
if(len(s)==len(s1)):
    for i in s:
        t=s.count(i)
        a.append(t)
    for j in s:
        u=s1.count(j)
        b.append(u)
    for m in range(0,len(a)):
        for n in range(0,len(b)):
            if(m==n):
                if(a[m]==b[n]):
                    c=c+1
    if(c==len(a)):
        print("yes")
    else:
        print("no")
else:
    print("no")
