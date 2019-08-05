import pandas as pd

# =============================================================================
# def addtwodimdict(thedict, key_a, key_b, val):
#      if key_a in alldata:
#          thedict[key_a].update({key_b: val})
#      else:
#          thedict.update({key_a:{key_b: val}})
#  
# alldata={}
# path=r"C:\Users\user\Desktop\105316144\盛行率.txt"
# for data in open(path,'r'):
#      data=data.strip()
#      data=data.split('\t')
#      print(data)
#      addtwodimdict(alldata,data[1],data[0],data[2])#dict包dict
#  
# 
# 
# for data in alldata.keys():
#     tot=0
#     for da in alldata[data].keys():
#         tot+=int(alldata[data][da])
#     alldata[data]['sum']=tot
#  
# pcount=1364661
# 
# for data in alldata.keys():
#     alldata[data]['Prate']=alldata[data]['sum']/pcount
# =============================================================================


# =============================================================================
# Man=list()
# Female=list()
# Uknow=list()
# Node=list()
# Sum=list()
# Prate=list()
# result_dict={
#             'Node':Node,
#             'M':Man,
#             'F':Female,
#             'U':Uknow,
#             'Sum':Sum,
#             'Prate':Prate
#         }    
# 
# for data in alldata.keys():
#     if 'M' in alldata[data]:
#         Man.append(alldata[data]['M'])
#     else:
#         Man.append(0)
#         
#     if 'F' in alldata[data]:
#         Female.append(alldata[data]['F'])
#     else:
#         Female.append(0)
#         
#     if 'U' in alldata[data]:
#         Uknow.append(alldata[data]['U'])
#     else:
#         Uknow.append(0)
#     
#     Sum.append(alldata[data]['sum'])
#     Node.append(data)
#     Prate.append(alldata[data]['Prate'])
#         
#     
# result_df=pd.DataFrame(result_dict)
# =============================================================================
