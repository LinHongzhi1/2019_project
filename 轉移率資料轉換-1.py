import os

##dict包dict的新增
def addtwodimdict(thedict, key_a, key_b):
     if key_a in unpro:
         thedict[key_a].update({key_b:0})##有KEY就UPADATE
     else:
         thedict.update({key_a:{key_b:0}})


path=r"C:\Users\user\Desktop\105316144\歸人處理後"
for linkpath in os.listdir(path):
    datapath=os.path.join(path,linkpath)
    fileopen=open(datapath,'r')
    people=fileopen.readline()
    
    datalist=fileopen.readlines()
    
    if len(datalist)>1:
        unpro={}
        for data in datalist:
            data=data.split('\t')
            temp=list()
            for count in range(1,4):
                if data[count]!=" ":
                    addtwodimdict(unpro,data[0],data[count])
                    
        pro=dict()
        for data in unpro.keys():
            temp=list()
            for da in unpro[data].keys():
                temp.append(da)
            pro[data]=temp
    
        lodict=list()
        realy=dict()

        for prokey in pro.keys():
            temp=list()
            for data in pro[prokey]:
                if data not in lodict:
                    lodict.append(data)
                    temp.append(data)
            if len(temp)!=0:    
                realy[prokey]=temp
                
        wrpath=r"C:\Users\user\Desktop\105316144\轉移資料-1"
        writepath=os.path.join(wrpath,linkpath)
        fwrite=open(writepath,'w')
        fwrite.write(people)
        for link in realy.keys():
            fwrite.write(link)
            for data in realy[link]:
                fwrite.write('\t'+data)
            fwrite.write('\n')
        
        fwrite.close()
                
    
    