from scipy.stats import kendalltau
import re

#File Reader
input_a =  "totalTDS_Result_VARs.txt"
#input_a =  "jaccard_Result_VARs.txt"
#input_a = "improv_totalTDS_Result_VARs.txt"
#input_a = "improv_jaccard_Result_VARs.txt"

f = open(input_a,"r", encoding='utf-8')
lines = f.readlines()

#Dictionary Creator
data1 = []
for i in range(0,len(lines)):
    text_ = re.sub("\n", " ", lines[i])
    data1.append(float(text_))

#File Reader
input_b =  "totalTDS_Santised_VARs.txt"
#input_b =  "jaccard_Santised_VARs.txt"
#input_b = "improv_totalTDS_Santised_VARs.txt"
#input_b = "improv_jaccard_Santised_VARs.txt"
f = open(input_b,"r", encoding='utf-8')
lines = f.readlines()

#Dictionary Creator
data2 = []
for i in range(0,len(lines)):
    text_ = re.sub("\n", " ", lines[i])
    data2.append(float(text_))

#Dictionary Creator
data2 = []
for i in range(0,len(lines)):
    text_ = re.sub("\n", " ", lines[i])
    data2.append(float(text_))

stat, p = kendalltau(data1, data2)
print('stat=%.5f, p=%.5f' % (stat, p))
if p > 0.05:
	print('Probably independent')
else:
	print('Probably dependent')