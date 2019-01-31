s=input()
b=""
for i in s:
      if i =='X' or i=='Y' or i=='Z':
            c=chr(ord(i)-23)
            b=b+c
      else:
            d=chr(ord(i)+3)
            b=b+d
print(b)    
