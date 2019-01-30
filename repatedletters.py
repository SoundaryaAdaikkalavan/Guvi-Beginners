n=input()#input
d={}
a=[]
for i in n:
    c=n.count(i)
    d.update({i:c})
    a.append(c)
w=max(a)
for x,y in d.items():
    if y==w:
        print(x)
