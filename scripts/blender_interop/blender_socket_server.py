import bpy


import socket
import threading

def socket_server():
    HOST = 'localhost'
    PORT = 5001

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Blender socket server listening on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                # Receive the length of the command
                data_length = int.from_bytes(conn.recv(4), byteorder='big')
                # Receive the full command
                command = b''
                while len(command) < data_length:
                    chunk = conn.recv(min(1024, data_length - len(command)))
                    if not chunk:
                        break
                    command += chunk
                command = command.decode('utf-8')
                print(f"Received command:\n{command}")
                try:
                    exec(command)
                    conn.sendall(b"Command executed successfully")
                except Exception as e:
                    error_msg = f"Error executing command: {str(e)}"
                    print(error_msg)
                    conn.sendall(error_msg.encode('utf-8'))

# Start the socket server in a separate thread
threading.Thread(target=socket_server, daemon=True).start()

print("Blender socket server started")
