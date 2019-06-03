import os
import pymysql

def comparecancer(a):
    a=a.strip()
    if a[:3].isdigit():
        if int(a[:3])>140 and int(a[:3])<240:
            return True
        else :
            return False

def procdata(a):
    a=a.strip()
    if len(a[3:])==0:
        return a[:3]
    else:
        return a[:3]+'.'+a[3:]

def isnum(a):
    a="".join(a).strip()
    if a.isdigit():
        return True
    else:
        return False

datalink=r"F:\資料\2012"

conn=pymysql.connect('203.64.84.236','lin','105316144','2019_project')
cursor=conn.cursor()
print("connection is ok")

##print(procdata('123  '))

for file in os.listdir(datalink):
    datapath=os.path.join(datalink,file)
    ##print(datapath)
    
    for line in open(datapath):
        ##print(line)
        if comparecancer(line[211:226]) or comparecancer(line[226:241]) or comparecancer(line[241:256]) or comparecancer(line[256:271]) or comparecancer(line[271:286]):
            
            data={}
            ##print(line[191:196],line[196:201],line[201:206],line[206:211],line[211:216])
            
            ##費用年月
            data['cos']=line[0:6]
            
            ##身分證號
            data['id']=line[57:89]
            
            ##出生年月
            data['bir']=line[89:97]
            
            ##就醫科別
            data['med']=line[103:105]
            
            ##主診斷
            if isnum(line[211:226]):
                data['main']=procdata(line[211:226])
            else:
                data['main']=line[211:226]
            ##次診斷1
            if isnum(line[226:241]):
                data['sec1']=procdata(line[226:241])
            else:
                data['sec1']=line[226:241] 
            ##次診斷2
            if isnum(line[241:256]):
                data['sec2']=procdata(line[241:256])
            else:
                data['sec2']=line[241:256]
            ##次診斷3
            if isnum(line[256:271]):
                data['sec3']=procdata(line[256:271])
            else:
                data['sec3']=line[256:271]
            ##次診斷4
            if isnum(line[271:286]):
                data['sec4']=procdata(line[271:286])
            else:
                data['sec4']=line[271:286]

            ##性別
            data['sex']=line[618:619]
            
            sql="INSERT INTO data_2012(cos,id,bir,med,main,sec1,sec2,sec3,sec4,sex) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%\
                (data['cos'],data['id'],data['bir'],data['med'],data['main'],data['sec1'],data['sec2'],data['sec3'],data['sec4'],data['sex'])
            
            try:
                ##cursor.execute(sql)
                ##conn.commit()
            except:
                conn.rollback()
    print(datapath+'is ok')
cursor.close()
conn.close()