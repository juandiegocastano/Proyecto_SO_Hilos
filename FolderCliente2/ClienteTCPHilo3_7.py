import socket
import os
import json

ejemplo_dir = 'ArchivosClientes'
contenido = os.listdir(ejemplo_dir)
print(contenido)

#client example with threads

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 1033))

data =   [os.path.basename(os.getcwd()) , contenido ]
print(data)
client_socket . send ((json.dumps(data)).encode("UTF-8"))

op = input("Choose an option [1: list, 2: read, 3: remove]: \n")

if op == "1":
  data =  ["1" , ]
  print(data)
  client_socket . send ((json.dumps(data)).encode("UTF-8"))
else:
  n0 = input ( "Type the name of the folder: \n ")
  n1 = input ( "Type the name of the file: \n ")
  info = json.dumps([str(op) , {
    "folder": n0,
    "file": n1,
  }])
  client_socket . send (info).encode("UTF-8")

# client_socket . send ((n1 + " " + n2 + " " + n3).encode("UTF-8"))
data = client_socket.recv(1024).decode("UTF-8")
data = json.loads(data)
print ('Result: ' , data)

client_socket . close ()
