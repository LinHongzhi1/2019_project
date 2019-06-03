import os

dirpath=r"D:\課業\專題\處理前"
wdirpath=r"D:\課業\專題\處理後"
for name in os.listdir(dirpath):
    a=[]
    datapath=os.path.join(dirpath,name)
    print(datapath)
    for line in open(datapath,'r'):
        line=line.split('\t')
        a.append(line)
    
    writepath=os.path.join(wdirpath,name)
    print(writepath)
    f=open(writepath,'a')
    f.write(name[:-4]+'\t'+a[0][2]+'\t'+a[0][1]+'\n')
    for c in range(0,len(a)):
        f.write(a[c][0]+'\t'+a[c][3]+'\t'+a[c][4]+'\t'+a[c][5]+'\t'+a[c][6]+'\t'+a[c][7])
    f.close()