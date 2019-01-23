n=str(input())
s=['a','e','i','o','u']
for i in n:
    if(i in s):
        print("yes")
        break
else:
    print("no")
