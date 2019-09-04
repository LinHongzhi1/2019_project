import pandas as pd

san=pd.read_csv(r"C:\Users\user\Desktop\105316144\盛行率.csv",index_col=0)
tra=pd.read_csv(r"C:\Users\user\Desktop\105316144\轉移率.csv",index_col=0)

tra['re_rate']=tra.apply(lambda x:int(x['re_value'])/int(san[san['Node']==x['node1']]['Sum']),axis=1)