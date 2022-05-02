from scipy.stats import shapiro
import matplotlib.pyplot as plt
import re

#File Reader
input =  "totalTDS_Santised_VARs.txt"
#input =  "totalTDS_Result_VARs.txt"
#input =  "jaccard_Santised_VARs.txt"
#input =  "jaccard_Result_VARs.txt"
#input = "improv_totalTDS_Santised_VARs.txt"
#input = "improv_totalTDS_Result_VARs.txt"
#input = "improv_jaccard_Santised_VARs.txt"
#input = "improv_jaccard_Result_VARs.txt"

f = open(input,"r", encoding='utf-8')
lines = f.readlines()

#Dictionary Creator
data = []
for i in range(0,len(lines)):
    text_ = re.sub("\n", " ", lines[i])
    data.append(float(text_))

stat, p = shapiro(data)
print('stat=%.5f, p=%.5f' % (stat, p))
if p > 0.05:
	print('Probably Gaussian')
else:
	print('Probably not Gaussian')

plt.hist(data, 30, histtype='bar')
#plt.show()