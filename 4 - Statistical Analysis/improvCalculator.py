import re

def improvCalculator(value_a, value_b):
    return value_a/value_b

#File Reader
input_a =  "jaccard_Result.txt"
#input_a =  "totalTDS_Result.txt"
f = open(input_a,"r", encoding='utf-8')
lines = f.readlines()

#Dictionary Creator
data1 = []
for i in range(0,len(lines)):
    text_ = re.sub("\n", " ", lines[i])
    data1.append(float(text_))

#File Reader
input_b =  "jaccard_Santised_VARs.txt"
#input_b =  "totalTDS_Santised_VARs.txt"
f = open(input_b,"r", encoding='utf-8')
lines = f.readlines()

#Dictionary Creator
data2 = []
for i in range(0,len(lines)):
    text_ = re.sub("\n", " ", lines[i])
    data2.append(float(text_))

CONTINUE = False
start = 444 #Input Checkpoint Index Here (In case an out-of-memory crash)

if CONTINUE == False:
    list_file = open("improv_"+input_a,"w", encoding='utf-8')
    list_file.write("")
    list_file.close()
    start = 0

for i in range(start,len(data1)):
    sum = 0
    for k in range(len(data2)):
        #print(str(list[k])+"/"+str(list[i]))
        sum = sum + improvCalculator(data2[k],data1[i])
    res = sum/len(data2)
    print(str(data1[i])+": "+str(res))
    ##Exporter - Population  
    list_file = open("improv_"+input_a,"a", encoding='utf-8')
    list_file.write("\n"+str(i)+": "+str(res))
    list_file.close()

print("Done")