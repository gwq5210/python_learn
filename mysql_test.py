#!/usr/bin/env python
# coding=utf-8

import mysql.connector
conn = mysql.connector.connect(user = 'root', password = '1234', database = 'gwq', use_unicode = True)
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', '1')
values = cursor.fetchall()
print values
cursor.close()
conn.commit()
conn.close()
