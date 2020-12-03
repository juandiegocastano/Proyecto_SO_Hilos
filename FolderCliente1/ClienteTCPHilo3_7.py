import socket
import os
import json

ejemplo_dir = '/ArchivosCliente'
contenido = os.listdir(ejemplo_dir)
print(contenido)
#client example with threads

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 1033))

client_socket . send ((json.dumps(contenido)).encode("UTF-8"))

n0 = input ( "Type the name of the file: \n ")
text = open(n0, "r")

client_socket . send ((text.read()).encode("UTF-8"))
text.close()


# client_socket . send ((n1 + " " + n2 + " " + n3).encode("UTF-8"))
data = client_socket.recv(1024).decode("UTF-8")
# print ('Result: ' , data)
result = open("result.txt", "w+")
result.write(data)
print("The following text was saved under name: results.txt --> \n")
print("\n {}".format(data))
result.close()
# client_socket . close ()
