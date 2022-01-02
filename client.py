import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",6535))
print("connected")
while True:
	print("Msg: ",s.recv(1024).decode("utf-8"))
