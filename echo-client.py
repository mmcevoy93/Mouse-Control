import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    x = raw_input('XX: ')
    s.sendall(bytes(x))
    data = s.recv(1024)

    print('Received', repr(data))
