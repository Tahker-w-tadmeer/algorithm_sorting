import random
def sorting(array, first, last):
    pivot =array[last]
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
    i=i+1
    temp = array[i]
    array[i] = array[last]
    array[last] = temp
    return i
def quick_sort(array,start,end):
    if(end<=start):
        return
    p=sorting(array,start,end)
    quick_sort(array,start,p-1)
    quick_sort(array, p+1, end)
def element_finder(array,k):
    quick_sort(array,0,len(array)-1)
    return array[k-1]
x= [0 for i in range(50)]
for i in range(0,49):
    x[i]=random.randint(0,222)
print(x)
print(len(x))
print(element_finder(x,8))
print(x)








