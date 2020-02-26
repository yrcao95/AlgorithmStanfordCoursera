import random
import math
import copy

class graph():
    def __init__(self,filename):
        fh=open(filename)
        fh=fh.readlines()
        self.vertex=list()
        self.edge=[[0 for dummy_i in range(len(fh))] for dummy_j in range(len(fh))]
        for line in fh:
            linenumber=line.split()
            self.vertex.append(int(linenumber[0]))
        for line in fh:
            linenumber=line.split()
            linenumber=list(map(int,linenumber))
            row=self.vertex.index(linenumber[0])
            for item in linenumber:
                col=self.vertex.index(item)
                self.edge[row][col]+=1
    
    def show_vertex(self):
        return self.vertex
    
    def find_index(self,value):
        return self.vertex.index(value)
    
    def clone(self):
        return graph(filename)

    def mergenode(self,index_a,index_b):
        index_list=[index_a,index_b]
        index_keep=min(index_list)
        index_list.remove(index_keep)
        index_del=index_list[0]
        self.vertex.pop(index_del)
        for col in range(len(self.edge)):
            self.edge[index_keep][col]+=self.edge[index_del][col]
        for row in range(len(self.edge)):
            self.edge[row][index_keep]+=self.edge[row][index_del]
        for row in range(len(self.edge)):
            self.edge[row].pop(index_del)
        self.edge.pop(index_del)
        for item in range(len(self.vertex)):
            self.edge[item][item]=1    
    
def choosenode(list):
    index_1,index_2=0,0
    while index_1==index_2:
        index_1,index_2=random.randint(0,len(list)-1),random.randint(0,len(list)-1)
    return index_1,index_2
    
                    


# filename="_f370cd8b4d3482c940e4a57f489a200b_kargerMinCut.txt"
filename="test.txt"
graph1=graph(filename)
length=len(graph1.vertex)
times=int((length*(length-1)*(math.log(length)//1+1))//2+1)
smallest=1000
for counter in range(times):
    temp_graph=copy.deepcopy(graph1)
    
    while len(temp_graph.vertex)>2:
        index_1,index_2=choosenode(temp_graph.vertex)
        # print(index_1,index_2)
        temp_graph.mergenode(index_1,index_2)
        # print(temp_graph.vertex)
        # print(temp_graph.edge)
    cut=temp_graph.edge[0][1]
    if smallest>cut:
        smallest=cut
    # if counter%1000==0:
    # print("The current smallest is %d" % (smallest))

print("The smallest is: %d" % (smallest))
a=input()