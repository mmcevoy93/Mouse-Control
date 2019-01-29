import socket
import pyautogui

HOST = '10.0.0.118'  # Standard loopback interface address (localhost)
PORT = 8000       # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
conn, addr = s.accept()
print('Connected by', addr)
size = pyautogui.size()

while True:

    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)
    x = int(data.split(',')[0])
    y = int(data.split(',')[1])
    pyautogui.moveTo(x, y)
