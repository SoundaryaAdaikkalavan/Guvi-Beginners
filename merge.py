def mergeSort(li):
    if len(li)>1:
        mid = len(li)//2
        le = li[:mid]
        ri = li[mid:]
        mergeSort(le)
        mergeSort(ri)
        i=0
        j=0
        k=0
        while i < len(le) and j < len(ri):
            if le[i] < ri[j]:
                li[k]=le[i]
                i=i+1
            else:
                li[k]=ri[j]
                j=j+1
            k=k+1
        while i < len(le):
            li[k]=le[i]
            i=i+1
            k=k+1

        while j < len(ri):
            li[k]=ri[j]
            j=j+1
            k=k+1
    print(li)
n=int(input())
li = list(map(int,input().split()))
mergeSort(li)
print(li)
