n=int(input())
a=list(map(int,input().split()))
b=sorted(a)
c=(len(b)+1)//2
print(b[c-1])
