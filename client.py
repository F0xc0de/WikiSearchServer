import socket

client = socket.socket()
client.connect(("localhost", 9080))

while True:
    queston = input("Введите ваш вопрос: ")
    client.send(queston.encode())
    answer = client.recv(10000).decode()
    print(answer)
