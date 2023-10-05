import time, socket, sys
 
new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)

port = 8080

new_socket.bind((host_name, port))
print("Conectado com sucesso!")
print("Esse é o seu IP: ", s_ip)

name = input('Digite seu nome: ')

new_socket.listen(1)

conn, add = new_socket.accept()
 
print("Recebendo conexão de ", add[0])
print('Conexão estabelecida. Conectado de: ',add[0])
 
client = (conn.recv(1024)).decode()
print(client + ' Entrou.')
 
conn.send(name.encode())
while True:
    message = input(name + ': ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ':', message)