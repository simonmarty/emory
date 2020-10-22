# THIS IS MY OWN WORK - Simon Marty
# Note I did not implement port handling in the request URL (ex: http://localhost:5000/google.com:587/)
# since it wasn't in the requirements. I might end up doing it on my own time to learn more about this

import socket
import sys

if __name__ == '__main__':
    HOST = 'localhost'
    PORT = int(sys.argv[1])
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break

                url = data.decode().split('\n', 1)[0]
                if url[:3] != "GET":
                    break

                # Kind of clunky, can be fixed with regexes for HTTP 2.0 etc
                url = url.replace("GET /", "").replace(" HTTP/1.1", "").replace(" HTTP/1.0", "")
                parts = url.split("/")
                for i, part in enumerate(parts):
                    if part:
                        domain = part.strip()
                        path = parts[i + 1:]
                        break
                request = f"GET {'/' + '/'.join(path).strip()} HTTP/1.1\r\nHost: {domain}\r\n\r\n"

                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
                    s2.connect((domain, 80))
                    s2.sendall(request.encode())

                    while True:
                        data = s2.recv(1024)
                        if data:
                            conn.send(data)
                        else:
                            break
