import random
def sorting(array, first, last):
    pivot =random.choice(array)
    #pivot =array[last]
    i=first-1
    j=first
    temp=0
    while(j<=last):
        if(array[j]>=pivot):
            j=j+1
        else:
            i=i+1
            temp=array[i]
            array[i]=array[j]
            array[j]=temp
            j=j+1
        if(array.index(pivot)==j):
            i=i+1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
    return array.index(pivot)
def quick_sort(array,start,end):
    if(end<=start):
        return
    p=sorting(array,start,end)
    quick_sort(array,start,p-1)
    quick_sort(array, p+1, end)

x=[8,2,4,7,1,3,9,6,5]
quick_sort(x,0,len(x)-1)
print(x)





