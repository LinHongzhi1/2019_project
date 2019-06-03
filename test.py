import pymysql

a='5'
b='3'
conn=pymysql.connect('203.64.84.236','lin','105316144','2019_project')
cursor=conn.cursor()
try:
    sql="INSERT INTO 95_data(id,num) VALUES (%s,%s)" %\
    (a,b)
    cursor.execute(sql)
    conn.commit()
except:
    conn.rollback()

cursor.close()
conn.close()