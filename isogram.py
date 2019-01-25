import collections
a=input()
freq=collections.Counter(a)
c=0
for x,y in freq.items():
    if(y>1):
        c=c+1
    if(c>=1):
        print("no")
        break
    else:
        print("yes")
        break
