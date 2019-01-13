import array
N=int(input())
K=int(input())
sum=0
arr=array.array('i',[])
for j in range(0,N):
    a=int(input())
    arr.append(a);
for m in range(0,K):
    sum=int(sum+arr[m])
print(sum)
