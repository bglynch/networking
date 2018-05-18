import socket

IP ="127.0.0.1"
PORT = 1234
MAXIMUM_QUEUE_SIZE = 0
BUFFER_SIZE = 2048

listening_socket = socket.socket()  #call socket() function from socket library
listening_socket.bind((IP, PORT))

listening_socket.listen(MAXIMUM_QUEUE_SIZE)
print("Hello, I'm waiting for a connection")

while True:
    (client_socket, client_ip_port) = listening_socket.accept()  # unpacking a tuple
    (client_ip, client_port) = client_ip_port
    
    initial_response = "Hi there, whats up\n".encode() #encode() changes string to computer language
    client_socket.send(initial_response)
    
    
    client_message = client_socket.recv(BUFFER_SIZE).decode()
    echo_response = ("You said: " + client_message).encode()
    client_socket.send(echo_response)
    client_socket.close()
