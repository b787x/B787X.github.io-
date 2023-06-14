import socket

HOST = '2409:895a:3249:4afb:4070:b54c:235e:841b'
PORT = 8080

server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server listening on [{HOST}]:{PORT}")
