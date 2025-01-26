import socket

def main():
    server_address = ('localhost', 65432)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(server_address)
        while True:
            command = input("Введите команду (Например: Поздоровайся с Петров, Сложи 3 4, Отсортируй 5 3 8): ")
            sock.sendall(command.encode())
            data = sock.recv(1024)
            print('Ответ от сервера:', data.decode())

if __name__ == "__main__":
    main()