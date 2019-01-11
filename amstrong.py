abc = int(input("")) #input
a = abc
res =0
while(abc>=1):
    rem = abc%10
    abc = abc//10
    res = res+(rem**3)
if(res == a):
    print("yes")
else:
    print("no")
