from http.client import CONTINUE
from TD import TD,S

def indexer(keyword,list):
    idx = []
    for i in range(len(list)):        
        if int(list[i]) == int(keyword):
            idx.append(i)    
    return idx

def jaccard(list_a, list_b):
    len_intersect = len(set(list_a).intersection(set(list_b)))
    len_union = len(set(list_a).union(set(list_b)))
    return len_intersect/len_union

#File Reader - Population A
input = "Result_VARs.txt"
#input = "Santised_VARs.txt"
f = open(input,"r")
lines = f.readlines()

#Population Creator - Population
pop = []
for i in range(0,len(lines)):
    pop.append(lines[i].split(','))

idx_pop = []
for i in pop:
    idx_pop.append(indexer(1,i))

CONTINUE = False
start = 444 #Input Checkpoint Index Here (In case an out-of-memory crash)

#Create an empty file
if CONTINUE == False:
    list_file = open("jaccard_"+input,"w", encoding='utf-8')
    list_file.write("")
    list_file.close()
    start = 0

for i in range(start,len(idx_pop)):
    sum = 0
    for j in range(len(idx_pop)):       
        sum = sum + jaccard(idx_pop[i],idx_pop[j])
    res = sum/len(idx_pop)
    print(str(i)+": "+str(res))
    ##Exporter - Population  
    list_file = open("jaccard_"+input,"a", encoding='utf-8')
    list_file.write("\n"+str(i)+": "+str(res))
    list_file.close()

print("Done")


