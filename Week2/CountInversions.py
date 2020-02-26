
def merge_splitinverstions(list1,list2):
    pointer_i, pointer_j=0,0
    count=0
    ans=list()
    while pointer_i<=len(list1)-1 and pointer_j<=len(list2)-1:
        if list1[pointer_i]<list2[pointer_j]:
            ans.append(list1[pointer_i])
            pointer_i+=1
            continue
        if list1[pointer_i]>list2[pointer_j]:
            ans.append(list2[pointer_j])
            count+=len(list1)-pointer_i
            pointer_j+=1
            continue
    ans+=list1[pointer_i:]
    ans+=list2[pointer_j:]
    return count

def mergesort_countinv(qlist,number=0):
    temp_list=qlist[:]
    if len(temp_list)==1:
        return 0
    if len(temp_list)==2:
        if temp_list[0]<temp_list[1]:
            return 0
        else:
            temp_list[0],temp_list[1]=temp_list[1],temp_list[0]
            return 1
    mid=len(qlist)//2
    return mergesort_countinv(qlist[:mid])+mergesort_countinv(qlist[mid:])+merge_splitinverstions(qlist[:mid],qlist[mid:])



filename="number.txt"
fh=open(filename)
numberlist=list()
for line in fh:
    numberlist.append(int(line))
print(numberlist[:10])
numberlist=[1,3,5,2,4,6,8,7,10,9]
print(mergesort_countinv(numberlist))