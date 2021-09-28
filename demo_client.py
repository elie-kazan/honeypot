import socket

Host = "127.0.0.1"
port = 3000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((Host, port))

