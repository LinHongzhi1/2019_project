import os
import shutil

mypath=r"C:\Users\user\Desktop\105316144\轉移資料-1"

M_0_18=r"C:\Users\user\Desktop\2019_proj\data\Tra_M_0_18"
F_0_18=r"C:\Users\user\Desktop\2019_proj\data\Tra_F_0_18"

M_19_40=r"C:\Users\user\Desktop\2019_proj\data\Tra_M_19_40"
F_19_40=r"C:\Users\user\Desktop\2019_proj\data\Tra_F_19_40"

M_41_65=r"C:\Users\user\Desktop\2019_proj\data\Tra_M_41_65"
F_41_65=r"C:\Users\user\Desktop\2019_proj\data\Tra_F_41_65"

M_66_up=r"C:\Users\user\Desktop\2019_proj\data\Tra_M_66_up"
F_66_up=r"C:\Users\user\Desktop\2019_proj\data\Tra_F_66_up"


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
    #print(year,datapath,sex)
    if sex=='F':
        if year<19:
            shutil.copy(datapath,F_0_18)
            print("小於18F",year,datapath,sex)
        elif year<41:
            shutil.copy(datapath,F_19_40)
            print("小於40F",year,datapath,sex)
        elif year<66:
            shutil.copy(datapath,F_41_65)
            print("小於65F",year,datapath,sex)
        else:
            shutil.copy(datapath,F_66_up)
            print("大於65F",year,datapath,sex)
    elif sex=='M':
        if year<19:
            shutil.copy(datapath,M_0_18)
            print("小於18M",year,datapath,sex)
        elif year<41:
            shutil.copy(datapath,M_19_40)
            print("小於40M",year,datapath,sex)
        elif year<66:
            shutil.copy(datapath,M_41_65)
            print("小於65M",year,datapath,sex)
        else:
            shutil.copy(datapath,M_66_up)
            print("大於65M",year,datapath,sex)
    
    