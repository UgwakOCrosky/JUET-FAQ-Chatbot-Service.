import sqlite3
con=sqlite3.Connection('tempdb')
cur=con.cursor()
cur.execute('create table if not exists socket(flag int(5),data varchar(10000))')
cur.execute('insert into socket values(?,?)',(0,'NULL'))
con.commit()

a=input()

cur.execute("update socket set data='"+a+"' where flag=0")
cur.execute('update socket set flag=1 where flag=0')
con.commit()

cur.close()
