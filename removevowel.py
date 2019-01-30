n=int(input())#input
x=input()#input
d=""
b=['a','e','i','o','u']
for i in x:
    if(i not in b):
        d=d+i
print(d[::-1]) 
