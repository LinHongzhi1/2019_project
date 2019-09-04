import pandas as pd
import pymysql     

tra=pd.read_csv(r"C:\Users\user\Desktop\105316144\轉移率.csv",index_col=0)
san=pd.read_csv(r"C:\Users\user\Desktop\105316144\盛行率.csv",index_col=0)#盛行率

c=pd.DataFrame()
b=pd.DataFrame()

#去除英文
c=tra[tra['node1'].between("00000","99999")]

b=c[c['node2'].between("00000","99999")]

result=pd.merge(b,san,left_on='node1',right_on='Node',how='left')
##篩選患病率小於5
result=result[result['Sum']>5]
result=result.drop(['Node','M','F','U','Sum','Prate'],axis=1)
result=result.rename(columns={'node1':'ICD_9_1','node2':'ICD_9_2'})

val_list=result.values.tolist()

##資料庫連線
conn=pymysql.connect('localhost','root','h704h704','2019_project')
cursor=conn.cursor()
print("connection is ok")

##執行
cursor.executemany("INSERT INTO tra_rate (ICD_9_1,ICD_9_2,tra_value,Trate) values(%s,%s,%s,%s)",val_list)
conn.commit()
    
cursor.close()
conn.close()
#result.to_csv(r"C:\Users\user\Desktop\105316144\轉移率完整.csv")