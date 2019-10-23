import pymysql
import pandas as pd

conn=pymysql.connect('203.64.84.236','lin','105316144','polysearch2_cancer')


table_list=["`anal cancer`","`bladder cancer`","`bone cancer`","`brain cancer`","`cervical cancer`",
            "`cholangiocarcinoma`","`colorectal cancer`","`esophageal cancer`","`eye cancer`","`female breast cancer`",
            "`gallbladder cancer`","`heart cancer`","`hypopharyngeal cancer`","`laryngeal cancer`","`lip cancer`",
            "`liver cancer`","`lung cancer`","`nasal cancer`","`nasopharyngeal cancer`","`oral cancer`",
            "`oropharyngeal cancer`","`ovary cancer`","`pancreatic cancer`","`penis cancer`","`peritoneal cancer`",
            "`placenta cancer`","`pleural cancer`","`prostate cancer`","`rectal cancer`","`salivary gland cancer`",
            "`skin cancer`","`small intestine cancer`","`stomach cancer`","`testicular cancer`","`thymic cancer`",
            "`thyroid gland cancer`","`tongue cancer`","`tracheal cancer`","`uterus cancer`","`vaginal cancer`",
            "`lymphoma`"]

sour_list=list()
target_list=list()
count_list=list()
rate_list=list()
rate_list_2=list()

data_dict={
        'source':sour_list,
        'target':target_list,
        'count':count_list,
        'rate':rate_list,
        'rate_2':rate_list_2
        }

for index in range(0,len(table_list)):
    for index2 in range(index,len(table_list)):
        if index !=index2:
            
            sql_cmd_1="select * from "+table_list[index]
            sql_cmd_2="select * from "+table_list[index2]
            
            data_1=pd.read_sql(sql_cmd_1,conn)
            data_2=pd.read_sql(sql_cmd_2,conn)
            
            result_data=pd.merge(data_1,data_2,left_on='node',right_on='node',how='inner')
            if len(result_data)>0:
                
                sour_list.append(table_list[index][1:-1])
                target_list.append(table_list[index2][1:-1])
                count_list.append(len(result_data))
                rate_list.append(len(result_data)/len(data_1))
                rate_list_2.append(len(result_data)*2/(len(data_1)+len(data_2)))
                
                print(table_list[index],table_list[index2],result_data,len(result_data),"\n")
           
            
data_df=pd.DataFrame(data_dict)


#data_df.to_excel("癌症對癌症的關聯.xlsx",index=False)

data_list=data_df.values.tolist()

##資料庫連線

conn2=pymysql.connect('203.64.84.236','lin','105316144','polysearch2_visual')
cursor=conn2.cursor()
print("connection is ok")

##執行
cursor.executemany("INSERT INTO cancer_to_cancer (source,target,COUNT,rate,rate_2) values(%s,%s,%s,%s,%s)",data_list)
conn2.commit()
    
cursor.close()
conn2.close()

