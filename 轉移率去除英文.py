import pandas as pd
import re

def compare (data):
    if re.search(r"^V",data['node1']):
        print(data)
    if re.search(r"^V",data['node2']):
        print(data)
        
san=pd.read_csv(r"C:\Users\user\Desktop\105316144\轉移率.csv",index_col=0)

#san.apply(compare,axis=1)
#san.apply(lambda x:re.search(r"^V",x['node1']),axis=1)
c=pd.DataFrame()
b=pd.DataFrame()

c=san[san['node1'].between("00000","99999")]

b=c[c['node2'].between("00000","99999")]