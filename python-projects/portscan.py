import socket
import sys

portas = [20, 21, 22, 23, 25, 53, 67, 68, 80, 110, 143, 161, 162, 194, 443, 465, 514, 587, 993, 995, 1080, 1433, 3306, 3389, 5432, 5900, 8080,27015, 27017, 8081, 8443, 9000, 9001]
try:
	host = sys.argv[1]
except:
	host = str(input("host: "))

for porta in portas:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(0.5)
	code = s.connect_ex((host, porta)) #CONECT_EX CONECTA E RETORNA UM CODIGO
	if code == 0:
		try:
			banner = s.recv(1024).decode()
		except:
			banner = 'NAO IDENTIFICADO'
		print(f'PORTA ABERTA {host}:', porta, banner)
		s.close()
