import os
import matplotlib.pyplot as plt

mypath=r"D:\課業\專題\處理後"
sex={'M':0,'F':0,'U':0}

for path in os.listdir(mypath):
    datapath=os.path.join(mypath,path)
    f=open(datapath,'r')
    data=f.readline()
    data=data.split('\t')
    sex[data[1]]=sex[data[1]]+1
    f.close()

fopen=open(r"D:\課業\專題\sex.txt",'w')
for a in sex:
    fopen.write(a+'\t'+str(sex[a])+'\n')
fopen.close()

#plt.pie(sex.values(),labels=sex,autopct='%1.1f%%')
#plt.axis('equal')
#plt.show()