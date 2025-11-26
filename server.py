import socket
import threading

# 1. Configuración del Servidor
HOST = '127.0.0.1'  # La IP de tu máquina local (localhost)
PORT = 65432        # Un puerto no privilegiado (> 1023)

def handle_client(conn, addr):
    """
    Función que maneja la comunicación con un cliente específico.
    Se ejecuta en un hilo separado para cada cliente.
    """
    print(f"[NUEVA CONEXIÓN] Cliente conectado desde {addr}")

    try:
        while True:
            # Recibir datos (máximo 1024 bytes)
            data = conn.recv(1024)
            if not data:
                # Si no hay datos, el cliente se desconectó
                break

            # Decodificar el mensaje para poder imprimirlo
            message = data.decode('utf-8')
            print(f"[{addr}] Mensaje recibido: {message}")

            # Enviar la respuesta (función 'Echo'):
            # El servidor devuelve el mismo mensaje que recibió.
            response = f"Echo: {message}"
            conn.sendall(response.encode('utf-8'))

    except Exception as e:
        print(f"[ERROR] Ocurrió un error con el cliente {addr}: {e}")

    finally:
        # Cerrar la conexión
        print(f"[DESCONEXIÓN] Cerrando conexión con {addr}")
        conn.close()

def start_server():
    """
    Función principal para iniciar el socket del servidor y escuchar.
    """
    # Crea el objeto socket: AF_INET (IPv4), SOCK_STREAM (TCP)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Permite reusar la dirección (útil para pruebas rápidas)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Enlaza el socket a la dirección y puerto
    server_socket.bind((HOST, PORT))

    # Pone el servidor en modo escucha (máximo 5 conexiones pendientes)
    server_socket.listen(5)

    print(f"[INICIADO] Servidor TCP escuchando en {HOST}:{PORT}")
    print("[ESPERANDO] Esperando conexiones de clientes...")

    while True:
        # Aceptar la conexión entrante
        # 'conn' es el socket para la conexión, 'addr' es la dirección del cliente
        conn, addr = server_socket.accept()

        # Iniciar un nuevo hilo para manejar la conexión del cliente
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

        # Muestra el número de hilos (clientes activos + el hilo principal)
        print(f"[ACTIVOS] Número de hilos activos: {threading.active_count() - 1}")


if __name__ == "__main__":
    start_server()
