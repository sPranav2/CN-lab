from socket import *
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect(('127.0.0.1',12000))
data=input('enter name')
clientSocket.send(data.encode())
fc=clientSocket.recv(1024).decode()
print(fc)
clientSocket.close()