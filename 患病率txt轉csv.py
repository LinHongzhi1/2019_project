import os
import pandas as pd


path=r"C:\Users\user\Desktop\2019_proj\盛行率"
opath=r"C:\Users\user\Desktop\2019_proj\盛行率_csv"

for line in os.listdir(path):
    icd_9=list()
    count=list()
    result_dict={
            'Node':icd_9,
            'count':count            
            }
    datapath=os.path.join(path,line)
    fopen=open(datapath,'r')
    fopen.readline()
    for data in fopen.readlines():
        data=data.strip()
        data=data.split('\t')
        
        icd_9.append(data[0])
        count.append(data[1])
        print(data)
    
    result_df=pd.DataFrame(result_dict)
    break
# =============================================================================
#     outpath=os.path.join(opath,line[:-3]+"csv")
#     result_df.to_csv(outpath,index=False)
#     print(outpath)
# =============================================================================
