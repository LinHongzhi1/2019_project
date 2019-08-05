import os
from collections import Counter
import pandas as pd
path=r"C:\Users\user\Desktop\105316144\轉移資料-1"
# =============================================================================
# alldata=list()
# for link in os.listdir(path):
#     datapath=os.path.join(path,link)
#     fileopen=open(datapath,'r')
#     fileopen.readline()
#     datalist=fileopen.readlines()
#     for index1 in range(0,len(datalist)):
#         data1=datalist[index1].strip().split()
#         for index2 in range(index1+1,len(datalist)):
#             data2=datalist[index2].strip().split()
#             for data1index in range(1,len(data1)):
#                 for data2index in range(1,len(data2)):
#                     alldata.append(data1[data1index]+','+data2[data2index])
#                     print(data1[data1index]+','+data2[data2index])
#     print(datapath)
#     fileopen.close()
#                 
# result=Counter(alldata)
# =============================================================================

# =============================================================================
# for data in result.keys():
#     second=data.split(',')
#     second=second[1]+','+second[0]
#     if second in result:
#         if result[second] > result[data]:
#             result[data]=0
#             print(second,result[second])
#         else:
#             result[second]=0
#             print(data,result[data])
# =============================================================================

# =============================================================================
# node1=list()
# node2=list()
# re_value=list()
# result_dict={
#         "node1":node1,
#         "node2":node2,
#         "re_value":re_value
#         }
# 
# 
# for data in result.keys():
#     if result[data]>0:
#         value_index=data.split(',')
#         
#         node1.append(value_index[0])
#         node2.append(value_index[1])
#         re_value.append(result[data])
#         print(value_index[0],value_index[1],result[data])
# =============================================================================

result_df=pd.DataFrame(result_dict)