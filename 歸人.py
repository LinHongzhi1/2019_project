import os 

path=r"D:\健保資料"
data=[]
for thispath in os.listdir(path):
    datapath=os.path.join(path,thispath)
    print(datapath)
    for line in open(datapath,'r'):
        line=line.split('\t')
        data.append(line)
    print(datapath+" is ok")
data.sort(key=lambda x:x[1])

for line in data:
    print(line)
    f=open(os.path.join('D:\處理完',line[1]+'.txt'),'a')
    f.write(line[0]+'\t'+line[2]+'\t'+line[9].strip()+'\t'+line[4]+'\t'+line[5]+'\t'+line[6]+'\t'+line[7]+'\t'+line[8]+'\n')
    f.close()
