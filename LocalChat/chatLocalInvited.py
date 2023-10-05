import time, socket, sys
 
socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 8080
 
print('Esse é o seu IP: ',ip)
server_host = input('Digite o IP do seu amigo:')
name = input('Digite seu nome: ')
 
 
socket_server.connect((server_host, sport))
 
socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()
 
print(server_name,' Entrou.')
while True:
    message = (socket_server.recv(1024)).decode()
    print(server_name, ":", message)
    message = input(name + ": ")
    socket_server.send(message.encode())  
