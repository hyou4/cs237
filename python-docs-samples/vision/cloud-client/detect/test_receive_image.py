# -*- coding: utf-8 -*-
import socket
import os
import json
import base64
import time


def recvall(sock):
    BUFF_SIZE = 256 # 4 KiB
    data = b''
    while True:
        part = sock.recv(BUFF_SIZE)
        data += part
        time.sleep(0.01)
        if len(part) < BUFF_SIZE:
            # either 0 or end of data
            break
    return data

TCP_IP = '0.0.0.0'

TCP_PORT = 8002

BUFFER_SIZE = 1000000


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((TCP_IP, TCP_PORT))

count=0

while 1:
    
    s.listen(10000)
    
    conn, addr = s.accept()
    
    print ('Connection address:', addr)
    
    # data = conn.recv(BUFFER_SIZE)
    data = recvall(conn)
    data = str(data)
    # print ("received data:", data)
    strg=str(data.split(',')[2])
    #print (strg)
    result = "" + strg 
    missing_padding = len(result) % 4
    temp=result[0:-3]
    #print(temp)
    if missing_padding != 0:
         temp += '='* (4 - missing_padding-2)
    result=temp+'\\n\n'

    # name="/home/pi/CS237/folder1/testfile"+str(count)+".txt"
    # file = open(name,"a") 
    # file.write(str(result[0])+"\n")
    # file.write(str(result[1])+"\n")
    # file.write(str(result[2])+"\n")
    # print(repr(result[2]))
    # #file.write(data)
    # file.close()
    print (result)
    print (type(result))
    img_data = base64.b64decode((repr(result)))
    imagename="./imageToSave.png"
    with open(imagename, "wb") as fh:
        fh.write(img_data)
    conn.close()
    count+=1
    if(count>2):
        break

s.close()
print("close connection")
