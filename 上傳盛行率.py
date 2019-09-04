import pandas as pd
import pymysql

san=pd.read_csv(r"C:\Users\user\Desktop\105316144\盛行率.csv",index_col=0)

conn=pymysql.connect('localhost','root','h704h704','2019_project')
cursor=conn.cursor()
print("connection is ok")

val_list=san.values.tolist()

# =============================================================================
# cursor.executemany("INSERT INTO pre_rate (ICD_9,Man_count,Woman_count,Uknow_count,Sum_count,Prate) values(%s,%s,%s,%s,%s,%s)",val_list)
# conn.commit()
# 
# cursor.close()
# conn.close()
# =============================================================================
