import pandas as pd
import pymysql

san=pd.read_csv(r"C:\Users\user\Desktop\轉移率完整.csv",index_col=0)

conn=pymysql.connect('localhost','root','h704h704','2019_project')
cursor=conn.cursor()
print("connection is ok")

val_list=san.values.tolist()

cursor.executemany("INSERT INTO tra_rate (ICD_9_1,ICD_9_2,tra_value,Trate) values(%s,%s,%s,%s)",val_list)
conn.commit()
    
cursor.close()
conn.close()
