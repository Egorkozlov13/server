import socket
from core import handle_command

def start_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Сервер запущен на {host}:{port}. Ожидание подключения...")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Подключено к {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    command = data.decode('utf-8')
                    response = handle_command(command)
                    conn.sendall(response.encode('utf-8'))

if __name__ == "__main__":
    start_server()