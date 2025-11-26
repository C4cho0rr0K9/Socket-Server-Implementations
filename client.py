import socket
import time

# 1. Configuración del Cliente
HOST = '127.0.0.1'  # Debe coincidir con la IP del servidor
PORT = 65432        # Debe coincidir con el puerto del servidor

def send_message(msg):
    """
    Función para crear una conexión y enviar un mensaje al servidor.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Conectar al servidor
        client_socket.connect((HOST, PORT))
        print(f"[CONEXIÓN] Conectado al servidor en {HOST}:{PORT}")

        # Enviar el mensaje
        message_bytes = msg.encode('utf-8')
        client_socket.sendall(message_bytes)
        print(f"[ENVIADO] Enviado: '{msg}'")

        # Esperar y recibir la respuesta del servidor
        data = client_socket.recv(1024)
        response = data.decode('utf-8')
        print(f"[RECIBIDO] Respuesta del servidor: '{response}'")
        
    except ConnectionRefusedError:
        print("[ERROR] No se pudo conectar. Asegúrate de que el servidor esté corriendo.")
    except Exception as e:
        print(f"[ERROR] Ocurrió un error: {e}")
        
    finally:
        # Cerrar la conexión
        client_socket.close()
        print("[DESCONEXIÓN] Conexión cerrada.")
        print("-" * 30)

if __name__ == "__main__":
    # Mensajes de prueba para enviar al servidor
    send_message("Hola Servidor!")
    time.sleep(1) # Espera un segundo antes del siguiente mensaje (para simular diferentes clientes)
    send_message("Este es el segundo mensaje.")
