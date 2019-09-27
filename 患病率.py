import os
from collections import Counter

mypath=r"C:\Users\user\Desktop\2019_proj\data\M_66_up"

result=[]

for path in os.listdir(mypath):
    count=[]
    datapath=os.path.join(mypath,path)
    f=open(datapath,'r')
    sex=f.readline()##抓取生日
    sex=sex.split('\t')
    sex=sex[1]
    for line in f.readlines():
        data=line.split('\t')
        if data[1]!=" ":
            count.append(data[1])
        if data[2]!=" ":
            count.append(data[2])
        if data[3]!=" ":
            count.append(data[3])
    count={}.fromkeys(count).keys()
    for line in count:
        result.append(line)
result=(Counter(result))

fopen=open(r"C:\Users\user\Desktop\2019_proj\盛行率\M_66_up.txt",'w')
fopen.write("ICD_9"+'\t'+"count"+'\n')
for line in result:
    fopen.write(str(line)+'\t'+str(result[line])+'\n')
fopen.close()