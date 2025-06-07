import socket
from sys import argv

port = int(argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #AF_INET(IPV4) SOCK_DGRAM(UDP)

s.bind(('0.0.0.0', port)) #0.0.0.0 QUER DIZER QUE QUALQUER IP PODE SE CONECTAR

while True:
        data, endereco = s.recvfrom(1024) #RECV RECEBE E FROM MOSTRA DE QUEM>
        print('CLIENT:', data.decode())

        data = input('>>>')
        s.sendto(data.encode(), endereco)
        