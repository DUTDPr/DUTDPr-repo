from scipy.stats import mannwhitneyu
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

#data1 = [3,5,1,4,3,5]
#data2 = [4,8,6,2,1,9]

stat, p = mannwhitneyu(data1, data2, alternative = 'greater')
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably the same (not greater/not less than) distribution')
else:
	print('Probably X is a greater distribution')