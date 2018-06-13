# A lambda function to interact with AWS RDS MySQL
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
import sys
from time import gmtime, strftime
import time
import random


# RDS parameters
REGION = 'us-east-2'
rds_host  = "54.183.26.41"
name = "root"
password = "qwertyu"
db_name = "info"
conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)


def fetch_result():
    # collect data from database about two lights
    # Time interval : 1 day +- 5 minutes
    result = []

    with conn.cursor() as cur1:
  
        cur1.execute("""select * from message where machine=1 and time='now' """)
        conn.commit()
        cur1.close()
        for row in cur1:
            result.append(list(row))
    # result.append(light1)
    print (result)


def insert_result(acticity,category,distance,pattern,time_now):
    with conn.cursor() as cur:
        act = acticity
        cat = category
        dis = distance
        pat = pattern
        tim = time_now
        # cur.execute("insert into projectdata.actdata (act, cat, dis, pat, time) values (%s,%s,%s,%s,%s)")
        cur.execute("insert into projectdata.actdata (act, cat, dis, pat, time) values ( %s , %s , %s , %s , %s)",(act,cat,dis,pat,tim))
        conn.commit()
        cur.close()

fetch_result()