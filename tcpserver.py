from socket import *
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('127.0.0.1',12000))
serverSocket.listen(1)
while True:
    conn,addr=serverSocket.accept()
    data=conn.recv(1024).decode()
    file=open(data,'r')
    l=file.read(1024)
    conn.send(l.encode())
    file.close()
    conn.close()