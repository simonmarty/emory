# Echo client program
import socket

if __name__ == '__main__':
    HOST = 'localhost'    # The remote host
    PORT = 5000              # The same port as used by the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'Hello, world')
        data = s.recv(1024)
    print(f"Received: {data.decode()}")