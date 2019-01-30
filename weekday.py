s=input()
a=['Monday','Tuesday','Wednesday','Thrusday','Friday']
for i in range(0,len(a)):
    if s==a[i]:
        print("no")
        break
else:
    print("yes")
