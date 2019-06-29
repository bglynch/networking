import socket   #import the socket library

# 

IP ="127.0.0.1"
PORT = 8080
MAXIMUM_QUEUE_SIZE = 0  # for TCP socket to set queue size
BUFFER_SIZE = 2048

def respond(client_socket, client_ip_and_port):
    initial_response = "Hi there, whats up\n".encode() #encode() changes string to computer language
    client_socket.send(initial_response)
    
    client_message = client_socket.recv(BUFFER_SIZE).decode() # recieved data from socket up to the BUFFER SIZE
    echo_response = ("You said: " + client_message).encode()
    client_socket.send(echo_response)

def serverloop():
    listening_socket = socket.socket()  #call socket() function from socket library
    listening_socket.bind((IP, PORT))   #get socket to use IP and PORT numbers
    listening_socket.listen(MAXIMUM_QUEUE_SIZE)
    
    print("Hello, I'm waiting for a connection")
    
    while True:
        (client_socket, client_ip_port) = listening_socket.accept()  # unpacking a tuple
        respond(client_socket, client_ip_and_port)
        client_socket.close()

        
    

if __name__ == '__main__':  # is this file executed directly (not just imported)
    print('Server launched on %s:%s, press ctrl+c to kill the server'
          % (IP, PORT))
    serverloop()
