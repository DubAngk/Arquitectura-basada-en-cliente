import socket

def iniciar_servidor():
    # Crear un socket para el servidor
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Definir la dirección y el puerto del servidor
    servidor_direccion = ('localhost', 65432)
    
    # Enlazar el socket del servidor a la dirección y puerto
    servidor_socket.bind(servidor_direccion)
    
    # Escuchar conexiones entrantes (máximo 5 conexiones en cola)
    servidor_socket.listen(5)
    print(f"Servidor iniciado en {servidor_direccion}")

    while True:
        # Esperar una conexión
        cliente_socket, cliente_direccion = servidor_socket.accept()
        print(f"Conexión aceptada de {cliente_direccion}")

        # Enviar un mensaje al cliente
        mensaje = "¡Hola, cliente! Gracias por conectarte."
        cliente_socket.sendall(mensaje.encode('utf-8'))
        
        # Cerrar la conexión con el cliente
        cliente_socket.close()

if __name__ == "__main__":
    iniciar_servidor()
