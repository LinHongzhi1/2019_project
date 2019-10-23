import pymysql
table_list=["`anal cancer`","`bladder cancer`","`bone cancer`","`brain cancer`","`cervical cancer`",
            "`cholangiocarcinoma`","`colorectal cancer`","`esophageal cancer`","`eye cancer`","`female breast cancer`",
            "`gallbladder cancer`","`heart cancer`","`hypopharyngeal cancer`","`laryngeal cancer`","`lip cancer`",
            "`liver cancer`","`lung cancer`","`nasal cancer`","`nasopharyngeal cancer`","`oral cancer`",
            "`oropharyngeal cancer`","`ovary cancer`","`pancreatic cancer`","`penis cancer`","`peritoneal cancer`",
            "`placenta cancer`","`pleural cancer`","`prostate cancer`","`rectal cancer`","`salivary gland cancer`",
            "`skin cancer`","`small intestine cancer`","`stomach cancer`","`testicular cancer`","`thymic cancer`",
            "`thyroid gland cancer`","`tongue cancer`","`tracheal cancer`","`uterus cancer`","`vaginal cancer`",
            "`lymphoma`"]
data_list=list()
for line in table_list:
    data_list.append(line[1:-1])
    
    
conn2=pymysql.connect('203.64.84.236','lin','105316144','polysearch2_visual')
cursor=conn2.cursor()
print("connection is ok")

##執行
cursor.executemany("INSERT INTO cancer_node (name) values(%s)",data_list)
conn2.commit()
    
cursor.close()
conn2.close()
