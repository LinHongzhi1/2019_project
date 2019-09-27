import os
import pandas as pd
import pymysql

mypath=r"C:\Users\user\Desktop\2019_proj\data\M_66_up"
datapath=r"C:\Users\user\Desktop\2019_proj\盛行率_csv\M_66_up.csv"


a=len(os.listdir(mypath))

result_df=pd.read_csv(datapath)

result_df['Prate']=result_df.apply(lambda x:x['count']/a,axis=1)

result_df.to_csv(datapath,index=False)



val_list=result_df.values.tolist()

##資料庫連線

conn=pymysql.connect('localhost','root','h704h704','2019_project')
cursor=conn.cursor()
print("connection is ok")

##執行
cursor.executemany("INSERT INTO pre_rate_m_66_up (ICD_9,Sum_count,Prate) values(%s,%s,%s)",val_list)
conn.commit()
    
cursor.close()
conn.close()
