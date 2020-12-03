'''
    Simple socket server using threads
'''
 
import socket
import sys
import threading
import math
import json

files_matrix = {}
 
HOST = ''   # Symbolic name, meaning all available interfaces
PORT = 1033 # Arbitrary non-privileged port
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print ('Socket created')
 
#Bind socket to local host and port
try:
    serversocket.bind((HOST, PORT))
except socket.error as msg:
    print ('Bind failed. Error Code : ', str(msg[0]) , ' Message ' , msg[1])
    sys.exit()
     
print ('Socket bind complete')
 
#Start listening on socket
serversocket.listen(10)
print ('Socket now listening')

def receive(data):
    print("RECEIVE")
    files_matrix[data[0]] = data[1]

def ls(conn, addr):
    print(files_matrix)
    conn.send((json.dumps(files_matrix)).encode("UTF-8"))
    print("LIST")
    pass

def read(conn, addr):
    pass

def remove(conn, addr):
    pass

def error(conn, addr):
    pass

def handler(conn, addr):    
        data = conn . recv (1025).decode("UTF-8")
#       reply = 'OK...' + data + ';'
    

        data = json.loads(data)
        print("HOLA2", data)
        
        receive(data)
        
        data = conn . recv (1025).decode("UTF-8")
        data = json.loads(data)
        op = str(data[0]) 

        if op == "1":
            ls(conn, addr)
        elif op == "2":
            read(conn, addr)
        elif op == "3":
            remove(conn, addr)
        else: error(conn, addr)


        # data1 = conn . recv (1025).decode("UTF-8")
        # print(data1)

        # copy = open("backup.txt", "w+")
        # copy.write(data)
        # copy.close()
        # print("Saved copy of file under name: backup.txt")
        # ans = ""
        # for i in data:
        #     if i not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        #         ans = ans + i                
        # print ("Respuesta enviada: " , ans)
        # reply = str(ans)
        # conn.send(reply.encode("UTF-8"))
		
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = serversocket.accept()    
    print ('Connected with ' , addr[0] , ':' , str(addr[1]))
    thread1 = threading.Thread(target=handler, args=(conn,addr))
    thread1.start()
     
s.close() 