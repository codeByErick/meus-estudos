import socket
import sys

try:
	arg = sys.argv #ARGUMENTOS PARA PASSAR COMO PARAMETRO
	host = arg[1]
	port =int(arg[2]) #PEGA O TERCEIRO ARGUMENTO QUE E A PORTA

except:
	host = str(input("host: "))
	port = int(input("porta: "))

s = socket.socket() #CRIA A CONEXAO
s.connect((host, port)) #CONECTA COM O HOST NA PORTA DEFINIDA
print(f'CONECTADO COM O HOST: {host}') #MENSAGEM DE AVISO

while True: #MANTEM A CONEXAO ATIVA
	msg = input('>>>')
	s.send(msg.encode()) #ENVIA A MENSAGEM, PRECISA CODIFICAR PORQUE NAO ACEITA STRING
	receive = s.recv(1024).decode()
	print('SERVER:', receive)
