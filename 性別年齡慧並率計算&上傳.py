import os
import pandas as pd
import os
import pymysql


path=r"C:\Users\user\Desktop\2019_proj\盛行率\M.txt"
datapath=[r"C:\Users\user\Desktop\2019_proj\data\M_0_18",
          r"C:\Users\user\Desktop\2019_proj\data\M_19_40",
          r"C:\Users\user\Desktop\2019_proj\data\M_41_65",
          r"C:\Users\user\Desktop\2019_proj\data\M_66_up"]

spath=r"C:\Users\user\Desktop\2019_proj\盛行率_csv\M.csv"
#opath=r"C:\Users\user\Desktop\2019_proj\盛行率_csv\0_18.csv"
acount=0
for a in datapath:
    acount+=len(os.listdir(a))


icd_9=list()
count=list()
result_dict={
            'Node':icd_9,
            'count':count            
            }
fopen=open(path,'r')
fopen.readline()
for data in fopen.readlines():
    data=data.strip()
    data=data.split('\t')
    
    icd_9.append(data[0])
    count.append(int(data[1]))
    print(data)
    
result_df=pd.DataFrame(result_dict)
    
result_df['Prate']=result_df.apply(lambda x:x['count']/acount,axis=1)


result_df.to_csv(spath,index=False)

val_list=result_df.values.tolist()

# =============================================================================
# ##資料庫連線
# 
# conn=pymysql.connect('localhost','root','h704h704','2019_project')
# cursor=conn.cursor()
# print("connection is ok")
# 
# ##執行
# cursor.executemany("INSERT INTO pre_rate_m (ICD_9,Sum_count,Prate) values(%s,%s,%s)",val_list)
# conn.commit()
#     
# cursor.close()
# conn.close()
# =============================================================================
