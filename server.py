import socket
from threading import Thread
import wikipedia

wikipedia.set_lang("ru")

server = socket.socket()
server.bind(("localhost", 9080))

def listen_user(conn):
    while True:
        queston = conn.recv(100000000).decode()
        try:
            result = wikipedia.summary(queston)
            conn.send(result.encode())
        except Exception as exc:
            conn.send(f"Error! {exc}".encode())

print("[+]Server listen...")

while True:
    server.listen()
    conn, addr = server.accept()
    Thread(target=listen_user, args=(conn,)).run()
