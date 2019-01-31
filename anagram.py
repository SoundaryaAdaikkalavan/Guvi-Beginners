
s="kabali"
a=int(input())
l=[]
d=0#count
for i in range(0,a):
    l.append(input())
for j in l:
    c=0
    for k in j:
        if(k in s):
            if(j.count(k)==s.count(k)):
                c=c+1
    if(c==len(j)):
       d=d+1
print(d)
