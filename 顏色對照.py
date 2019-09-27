import json
import pymysql
import pandas as pd

data=dict({
        "nodes":[],
        "links":[]
        })

node_dict=dict()

def change_group(x):
    ICD=x.ICD_9[:3]
    print(ICD)
    ICD=int(ICD)
    if ICD <139:
        return 1
        
    elif ICD <239:
        return 2
        
    elif ICD <278:
        return 3
        
    elif ICD <319:
        return 4
        
    elif ICD <389:
        return 5
        
    elif ICD <459:
        return 6
    
    elif ICD <519:
        return 7
        
    elif ICD <579:
        return 8
        
    elif ICD <629:
        return 9
        
    elif ICD <679:
        return 10
    
    elif ICD <709:
        return 11
        
    elif ICD <739:
        return 12
        
    elif ICD <759:
        return 13
    
    elif ICD <779:
        return 14
        
    elif ICD <799:
        return 15
        
    else:
        return 16

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
        node_dict.update({x.ICD_9:0})
        
def drop_node2(x):
    del node_dict[x.ICD_9]
    

    
def get_node(x):
    if x.ICD_9_2 in node_dict:
        pass
    else:
        node_dict.update({x.ICD_9_2:0})

conn=pymysql.connect('203.64.84.236','lin','105316144','2019_project')
data_icd=pd.read_excel(r"C:\Users\user\Downloads\4.1 ICD-9-CM2001年版與ICD-10-CM對應資料檔(106.07.19更新).xlsx")


data_icd=data_icd.drop(data_icd.columns[[3,4,5,6]],axis=1)
data_icd['ICD-9-CM代碼']=data_icd['ICD-9-CM代碼'].apply(lambda x:x[:3]+x[4:])
data_icd.drop_duplicates(keep='first',inplace=True)

sqlcmd_pre="select ICD_9,Prate from pre_rate_66_up WHERE ICD_9 BETWEEN 140 AND 240 OR ICD_9 BETWEEN 1400 AND 2400 OR ICD_9 BETWEEN 14000 AND 24000 order by Sum_count desc"
a=pd.read_sql(sqlcmd_pre,conn)

#去除v code
abool=a['ICD_9'].str.contains("V")
b=a[abool==False]

node=b.head(10)
node.apply(get_node2,axis=1)

node_list=list(node['ICD_9'])

for line in node_list:
    sqlcmd_tra="select * from tra_rate_66_up where ICD_9_1 = "+line+" order by tra_value desc"
    c=pd.read_sql(sqlcmd_tra,conn)
    link=c.head(5)
    
    link.apply(push_link,axis=1)
    link.apply(get_node,axis=1)
    
    print(link)
    
    
node.apply(drop_node2,axis=1)

for line in node_dict.keys():
    print(line)
    cmd="select ICD_9,Prate from pre_rate_66_up where ICD_9 = "+line+" order by Sum_count desc"
    c=pd.read_sql(cmd,conn)
    c=c.head(1)
    node=node.append(c,ignore_index=True)

node['group']=node.apply(change_group,axis=1)

node=pd.merge(node,data_icd,left_on='ICD_9',right_on='ICD-9-CM代碼',how='left')
node=node.rename(columns={"ICD-9-CM中文名稱":"name"})
node.apply(push_node,axis=1)

with open('tra_rate_66_up.json', 'w',encoding='utf-8') as f:
    json.dump(data, f,ensure_ascii=False,indent = 4)

