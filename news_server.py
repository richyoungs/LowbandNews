import socket
import time

HOST = "0.0.0.0"   # Accept connections on all interfaces
PORT = 2323        # Telnet-style port (can change later)

def serve_news():
    with open("news.txt", "r") as f:
        content = f.read()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Lowband.news now listening on port {PORT}.")
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                conn.sendall(content.encode("ascii", errors="ignore"))
                time.sleep()

serve_news()
