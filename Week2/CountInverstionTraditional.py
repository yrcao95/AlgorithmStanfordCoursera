filename="number.txt"
fh=open(filename)
numberlist=list()
for line in fh:
    numberlist.append(int(line))
# print(len(numberlist))
count=0
for dummy_i in range(len(numberlist)):
    for dummy_j in range(dummy_i+1,len(numberlist)):
        if numberlist[dummy_i]>numberlist[dummy_j]:
            count+=1
print(count)