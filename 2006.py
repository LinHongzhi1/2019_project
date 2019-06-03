import os
import pymysql

def comparecancer(a):
    if a[:3].isdigit():
        if int(a[:3])>140 and int(a[:3])<240:
            return True
        else :
            return False

def procdata(a):
    a=a.strip()
    if len(a[3:])==0:
        return "".join(a[:3])
    else:
        return "".join(a[:3]+'.'+a[3:])

def isnum(a):
    a="".join(a).strip()
    if a.isdigit():
        return True
    else:
        return False

datalink=r"F:\資料\2006"
##print(isnum('123 '))

##建立連線
conn=pymysql.connect('203.64.84.236','lin','105316144','2019_project')
cursor=conn.cursor()
print("connection is ok")

for file in os.listdir(datalink):
    datapath=os.path.join(datalink,file)
    ##print(datapath)
    
    for line in open(datapath):
        ##print(line)
        if comparecancer(line[190:195]) or comparecancer(line[195:200]) or comparecancer(line[200:205]) or comparecancer(line[205:210]) or comparecancer(line[210:215]):
            
            data={}
            
            ##費用年月
            data['cos']="".join(line[0:6])
            
            #身分證
            data['id']="".join(line[56:88])
            
            ##出生年月
            data['bir']="".join(line[88:96])
            
            ##就醫科別
            data['med']="".join(line[102:104])
            
            ##主診斷
            if isnum(line[190:195]):
                data['main']=procdata(line[190:195])
            else:
                data['main']=line[190:195]
            ##次診斷1
            if isnum(line[195:200]):
                data['sec1']=procdata(line[195:200])
            else:
                data['sec1']=line[195:200] 
            ##次診斷2
            if isnum(line[200:205]):
                data['sec2']=procdata(line[200:205])
            else:
                data['sec2']=line[200:205]
            ##次診斷3
            if isnum(line[205:210]):
                data['sec3']=procdata(line[205:210])
            else:
                data['sec3']=line[205:210]
            ##次診斷4
            if isnum(line[210:215]):
                data['sec4']=procdata(line[210:215])
            else:
                data['sec4']=line[210:205]
            
            ##性別
            data['sex']="".join(line[492:493])
            
            sql="INSERT INTO data_2006(cos,id,bir,med,main,sec1,sec2,sec3,sec4,sex) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%\
                (data['cos'],data['id'],data['bir'],data['med'],data['main'],data['sec1'],data['sec2'],data['sec3'],data['sec4'],data['sex'])
            
            try:
                cursor.execute(sql)
                conn.commit()
            except:
                conn.rollback()
                
    print(datapath+'is ok')
cursor.close()
conn.close()