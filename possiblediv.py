a,b=map(int,input().split())#input
for i in range(1,1000):
    if i%a==0 and i%b==0:
        print(i)
        break
