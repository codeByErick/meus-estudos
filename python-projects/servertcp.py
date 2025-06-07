import socket
from sys import argv

port = int(argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET(IPV4) SOCK_STREM(TCP

s.bind(('0.0.0.0', port)) #0.0.0.0 QUER DIZER QUE QUALQUER IP PODE SE CONECTAR

s.listen(1) #QUANTAS CONEXOES IRA AGUARDAR

s2, endereco = s.accept() #CRIA UM NOVO SOCKET s2 = SOCKET 2, ENDERECO (CLIENT)

print('CONECTADO COM O HOST:', endereco[0])

while True:
	receive = s2.recv(1024).decode() #RECEBE A MENSAGEM DO NOVO SOCKET
	print('CLIENT:', receive)
	msg = input('>>>')
	s2.send(msg.encode())

