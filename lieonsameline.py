x,y=map(int,input().split())
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
if x==y and x1==y1 and x2==y2:
    print('yes')
elif x==x1==x2 or y==y1==y2:
    print('yes')
else:
    print('no')
