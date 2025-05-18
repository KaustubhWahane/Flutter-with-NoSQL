import sqlite3
conn = sqlite3.connect('sqlitedb');
ins = '''
INSERT INTO users (st_name, st_class, st_email) values ('ziprya', '12th', "ziprya@gmail.com")
'''
conn.execute(ins)
conn.commit()
conn.close()