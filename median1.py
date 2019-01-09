
x=int(input()) #get input
a=list(map(int,input().split()))
b=sorted(a)
d=(len(b)+1)//2
print(b[d-1])
