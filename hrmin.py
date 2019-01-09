x=list(map(int,input().split()))
y=list(map(int,input().split()))
d=x[0]*60+x[1]
f=y[0]*60+y[1]
e=abs(d-f)
print(str(e//60)+" "+str(e%60))
