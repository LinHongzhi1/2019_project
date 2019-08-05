import os
from collections import Counter

mypath=r"C:\Users\user\Desktop\105316144\歸人處理後"

count={'M':[],'F':[],'U':[]}
result=[]

for path in os.listdir(mypath):
    datapath=os.path.join(mypath,path)
    f=open(datapath,'r')
    
    data=f.readline()##抓取生日
    data=data.split('\t')
    sex=data[1]
    born=data[2]
    
    data=f.readline()##第一次得癌
    data=data.split('\t')
    first=data[0]
    
    f.close()
    
    year=int(first[:4])-int(born[:4])
    month=int(first[4:])-int(born[4:])
    if month<0:
        year=year-1
    count[sex].append(year)

for line in count.keys():
    result.append(Counter(count[line]))

#fopen=open(r"C:\Users\user\Desktop\105316144\old2.txt",'w')
#for a in range(0,len(result)):
#    fopen.write(str(a)+'\t'+str(result[a])+'\n')
#fopen.close()
   
#fopen=open(r"C:\Users\user\Desktop\105316144\old2.txt",'w')
#for a in range(0,len(result)):
#   for b in result[a]:
#      if result[a][b]!=0:
#         fopen.write(str(a)+'\t'+str(b)+'\t'+str(result[a][b])+'\n')
#fopen.close()