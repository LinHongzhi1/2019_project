import os
from collections import Counter

mypath=r"C:\Users\user\Desktop\105316144\歸人處理後"

alldata={'M':[],'F':[],'U':[]}
result={}

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
        alldata[sex].append(line)
for line in alldata.keys():
    result[line]=(Counter(alldata[line]))

#fopen=open(r"C:\Users\user\Desktop\105316144\try.txt",'w')
#for a in result.keys():
#   for b in result[a]:
#     fopen.write(str(a)+'\t'+str(b)+'\t'+str(result[a][b])+'\n')
#fopen.close()