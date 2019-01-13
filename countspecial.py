string=input()
count=0
for i in range(0,len(string)):
    if(string[i].isalpha()==False):
        if(string[i].isnumeric()==False):
            count=count+1
print(count)
