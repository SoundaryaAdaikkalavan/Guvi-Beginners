def isarm(abc):
    a = abc
    res =0
    while(abc>=1):
        rem = abc%10
        abc = abc//10
        res = res+(rem**3)
    if(res == a):
        return True
    else:
        return False
a,b = map(int,input().split())
c=0
for i in range(a+1,b):
    if(isarm(i)):
        if(c == 0):
            print(i,end="")
            c+=1
        else:
            print(" "+i,end = "")

