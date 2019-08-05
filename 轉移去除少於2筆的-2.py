import os
path=r"C:\Users\user\Desktop\105316144\轉移資料-1"
for link in os.listdir(path):
    datapath=os.path.join(path,link)
    fileopen=open(datapath,'r')
    fileopen.readline()
    a=fileopen.readlines()
    fileopen.close()
    if len(a)<=1:
        os.remove(datapath)
        
