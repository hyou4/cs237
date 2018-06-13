# A lambda function to interact with AWS RDS MySQL
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
import sys
from time import gmtime, strftime
import time
import random

# import numpy as np
# from keras import layers
# from keras.layers import Input, Add, Dense, Activation, ZeroPadding2D, BatchNormalization, Flatten, Conv2D, AveragePooling2D, MaxPooling2D, GlobalMaxPooling2D
# from keras.models import Model, load_model
# from keras.preprocessing import image
# from keras.utils import layer_utils
# from keras.utils.data_utils import get_file
# from keras.applications.imagenet_utils import preprocess_input
# import pydot
# from IPython.display import SVG
# from keras.utils.vis_utils import model_to_dot
# from keras.utils import plot_model
# from resnets_utils import *
# from keras.initializers import glorot_uniform
# import scipy.misc
# from matplotlib.pyplot import imshow
# import matplotlib.pyplot as plt
# import pylab


# import paho.mqtt.client as mqtt #import the client1

# import keras.backend as K

# RDS parameters
REGION = 'us-east-2'
rds_host  = "http://ec2-54-183-26-41.us-west-1.compute.amazonaws.com/"
name = "root"
password = "qwertyu"
db_name = "info"
conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)


def fetch_result():
    # collect data from database about two lights
    # Time interval : 1 day +- 5 minutes
    result = []

    with conn.cursor() as cur1:
        #cur1.execute("""select * from projectdata.input_data WHERE time < NOW() - INTERVAL 5 MINUTE """)
        cur1.execute("""select * from image WHERE machine=0 and time='now' """)
        conn.commit()
        cur1.close()
        for row in cur1:
            light1.append(list(row))
    print (light1)

    # with conn.cursor() as cur2:
    #     #cur1.execute("""select * from projectdata.input_data WHERE time < NOW() - INTERVAL 5 MINUTE """)
    #     cur2.execute("""select * from projectdata.input_data WHERE '/test/light2' AND time < NOW() - INTERVAL 1 DAY """)
    #     conn.commit()
    #     cur2.close()
    #     for row in cur2:
    #         light2.append(list(row))
    # result.append(light2)
    # print (light2)

    return result


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




