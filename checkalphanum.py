n=input()
count_alpha=0
count_num=0
for i in range(0,len(n)):
    if(n[i].isalpha()):
        count_alpha=count_alpha+1
    elif(n[i].isnumeric()):
        count_num=count_num+1
if(count_alpha>0 and count_num>0):
    print("yes")
else:
    print("no")
