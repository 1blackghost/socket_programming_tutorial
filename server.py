import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("127.0.0.1",6535))
print("listening for connections...")
s.listen(5)
a,c=s.accept()
print(f"connection from {a} accepted")
while True:
	msg=input(">")
	a.send(msg.encode("utf-8"))
