import socket
import pyautogui

HOST = '10.0.0.118'  # The server's hostname or IP address
PORT = 8000        # The port used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    mouseXY = str(pyautogui.position()[0]) + "," + str(pyautogui.position()[1])
    s.sendall(bytes(mouseXY))
    data = s.recv(1024)


    print('Received', repr(data))
