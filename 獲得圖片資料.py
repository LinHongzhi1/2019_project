import json
import pymysql
import pandas as pd

data=dict({
        "nodes":[],
        "links":[]
        })

node_dict=dict()

def push_link(x):
    link=dict(
            {
              "source":x.ICD_9_1,
              "target":x.ICD_9_2,
              "value":x.Trate
                    })
    data['links'].append(link)

def push_node(x):
    print(x['name'])
    node=dict(
            {
              "ICD_9":x.ICD_9,
              "name":x['name'],
              "group":x.group,
              "value":x.Prate
                    })
    data['nodes'].append(node)    
    
def get_node2(x):
    if x.ICD_9 in node_dict:
        pass
    else:
        node_dict.update({x.ICD_9:node[node['ICD_9']==x.ICD_9].group})
        
def drop_node2(x):
    del node_dict[x.ICD_9]
    

    
def get_node(x):
    if x.ICD_9_2 in node_dict:
        pass
    else:
        node_dict.update({x.ICD_9_2:node[node['ICD_9']==x.ICD_9_1].group})

conn=pymysql.connect('203.64.84.236','lin','105316144','2019_project')
data_icd=pd.read_excel(r"C:\Users\user\Downloads\4.1 ICD-9-CM2001年版與ICD-10-CM對應資料檔(106.07.19更新).xlsx")


data_icd=data_icd.drop(data_icd.columns[[3,4,5,6]],axis=1)
data_icd['ICD-9-CM代碼']=data_icd['ICD-9-CM代碼'].apply(lambda x:x[:3]+x[4:])
data_icd.drop_duplicates(keep='first',inplace=True)

sqlcmd_pre="select ICD_9,Prate from pre_rate order by Sum_count desc"
a=pd.read_sql(sqlcmd_pre,conn)

#去除v code
abool=a['ICD_9'].str.contains("V")
b=a[abool==False]

node=b.head(10)
node['group']=node.index

node.apply(get_node2,axis=1)

node_list=list(node['ICD_9'])

for line in node_list:
    sqlcmd_tra="select * from tra_rate where ICD_9_1 = "+line+" order by tra_value desc"
    c=pd.read_sql(sqlcmd_tra,conn)
    link=c.head(5)
    
    link.apply(push_link,axis=1)
    link.apply(get_node,axis=1)
    
    print(link)
    
    
node.apply(drop_node2,axis=1)

for line in node_dict.keys():
    print(line)
    cmd="select ICD_9,Prate from pre_rate where ICD_9 = "+line+" order by Sum_count desc"
    c=pd.read_sql(cmd,conn)
    c=c.head(1)
    c['group']=node_dict[line].values[0]
    node=node.append(c,ignore_index=True)

node=pd.merge(node,data_icd,left_on='ICD_9',right_on='ICD-9-CM代碼',how='left')
node=node.rename(columns={"ICD-9-CM中文名稱":"name"})
node.apply(push_node,axis=1)

with open('result.json', 'w',encoding='utf-8') as f:
    json.dump(data, f,ensure_ascii=False,indent = 4)

