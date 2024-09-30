import socket

def iniciar_cliente():
    # Crear un socket para el cliente
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Definir la dirección del servidor al que nos conectaremos
    servidor_direccion = ('localhost', 65432)
    
    # Conectar al servidor
    cliente_socket.connect(servidor_direccion)
    print(f"Conectado al servidor en {servidor_direccion}")

    # Recibir el mensaje del servidor
    mensaje = cliente_socket.recv(1024).decode('utf-8')
    print(f"Mensaje del servidor: {mensaje}")

    # Cerrar la conexión
    cliente_socket.close()

if __name__ == "__main__":
    iniciar_cliente()
