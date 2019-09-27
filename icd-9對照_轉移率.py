import pymysql
import pandas as pd
import re

def change(boo):
    if boo==True:
        return False
    else:
        return True

conn=pymysql.connect('203.64.84.236','lin','105316144','2019_project')

data_icd=pd.read_excel(r"C:\Users\user\Downloads\4.1 ICD-9-CM2001年版與ICD-10-CM對應資料檔(106.07.19更新).xlsx")

datalist=["pre_rate","pre_rate_0_18","pre_rate_19_40","pre_rate_41_65","pre_rate_66_up",
          "pre_rate_f","pre_rate_f_0_18","pre_rate_f_19_40","pre_rate_f_41_65","pre_rate_f_66_up",
          "pre_rate_m","pre_rate_m_0_18","pre_rate_m_19_40","pre_rate_m_41_65","pre_rate_m_66_up"]

alldata=list()
sqlcmd="select ICD_9_1,ICD_9_2 from tra_rate_f where ICD_9_1=486 order by tra_value desc"

for line in datalist:
    sqlcmd_pre="select ICD_9 from "+line+" order by Sum_count desc"
    a=pd.read_sql(sqlcmd_pre,conn)
    
    ##去除V code
    abool=a['ICD_9'].str.contains("V")
    b=a[abool==False]
    
    #取前10的疾病
    node=b.head(10)
    node=list(node['ICD_9'])
    for line2 in node:
        alldata.append(line2)
        sqlcmd="select ICD_9_2 from tra"+line[3:]+" where ICD_9_1 = "+line2+" order by tra_value desc"
        
        c=pd.read_sql(sqlcmd,conn)
        d=c.head(5)
        d=list(d['ICD_9_2'])
        for e in d:
            alldata.append(e)
        
        
        print(sqlcmd)
    
    

data={}.fromkeys(alldata).keys()
data=pd.DataFrame(data)
data=data.rename(columns={0:'ICD_9'})

data_icd=data_icd.drop(data_icd.columns[[3,4,5,6]],axis=1)
data_icd['ICD-9-CM代碼']=data_icd['ICD-9-CM代碼'].apply(lambda x:x[:3]+x[4:])
data_icd.drop_duplicates(keep='first',inplace=True)

result=pd.merge(data,data_icd,left_on='ICD_9',right_on='ICD-9-CM代碼',how='left')
# =============================================================================
# a=pd.read_sql(sqlcmd,conn)
# b=a.head(5)
# =============================================================================
