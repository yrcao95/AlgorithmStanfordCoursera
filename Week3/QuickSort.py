def swap(lst,sub1,sub2):
    lst[sub1],lst[sub2]=lst[sub2],lst[sub1]

def partition(unsortetlst,left,right,pivot=0):
    swap(unsortetlst,left,pivot)
    pointer=left
    for dummy_i in range(left,right+1):
        if unsortetlst[dummy_i]<unsortetlst[left]:
            swap(unsortetlst,dummy_i,pointer+1)
            pointer+=1
    swap(unsortetlst,left,pointer)
    return pointer

def quicksort(unsortlst,left,right,pivot=0):
    if left<right:
        loc=partition(unsortlst,left,right,left)
        quicksort(unsortlst,left,loc-1)
        quicksort(unsortlst,loc+1,right)



fhandle=open("_32387ba40b36359a38625cbb397eee65_QuickSort.txt")
input_array=list()
for line in fhandle:
    # print(int(line))
    input_array.append(int(line))

# print(input_array)
# print("After Sorting")
quicksort(input_array,0,9999)
# print(input_array)
ans=list()
for dummy_i in range(1,10001):
    ans.append(dummy_i)
assert input_array==ans