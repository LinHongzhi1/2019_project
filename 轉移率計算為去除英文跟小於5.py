import os
from collections import Counter
import pandas as pd

san=pd.read_csv(r"C:\Users\user\Desktop\2019_proj\盛行率_csv\M_66_up.csv")

path=r"C:\Users\user\Desktop\2019_proj\data\Tra_M_66_up"

spath=r"C:\Users\user\Desktop\2019_proj\轉移率為去除英文小於5\Tra_M_66_up.csv"
alldata=list()
for link in os.listdir(path):
    datapath=os.path.join(path,link)
    fileopen=open(datapath,'r')
    fileopen.readline()
    datalist=fileopen.readlines()
    for index1 in range(0,len(datalist)):
        data1=datalist[index1].strip().split()
        for index2 in range(index1+1,len(datalist)):
            data2=datalist[index2].strip().split()
            for data1index in range(1,len(data1)):
                for data2index in range(1,len(data2)):
                    alldata.append(data1[data1index]+','+data2[data2index])
                    print(data1[data1index]+','+data2[data2index])
    print(datapath)
    fileopen.close()
                
result=Counter(alldata)

for data in result.keys():
    second=data.split(',')
    second=second[1]+','+second[0]
    if second in result:
        if result[second] > result[data]:
            result[data]=0
            print(second,result[second])
        else:
            result[second]=0
            print(data,result[data])

node1=list()
node2=list()
re_value=list()
result_dict={
        "node1":node1,
        "node2":node2,
        "re_value":re_value
        }


for data in result.keys():
    if result[data]>0:
        value_index=data.split(',')
        
        node1.append(value_index[0])
        node2.append(value_index[1])
        re_value.append(result[data])
        print(value_index[0],value_index[1],result[data])

result_df=pd.DataFrame(result_dict)
result_df['re_rate']=result_df.apply(lambda x:int(x['re_value'])/int(san[san['Node']==x['node1']]['count']),axis=1 )

result_df.to_csv(spath,index=False)