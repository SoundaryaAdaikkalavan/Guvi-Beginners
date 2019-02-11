a,b,c=map(int,input().split())#input
e=a+b+c
if a==0 or b==0 or c==0:
    print('no')
elif (e==180):
    print("yes")
else:
    print('no')
