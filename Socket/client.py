import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in range(0,9):
	print(data)
	s.sendto(data,('127.0.0.1',9990))
	print(s.recv(1024).decode('utf-8'))
s.close()