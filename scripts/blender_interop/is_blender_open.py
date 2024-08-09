
import socket
import sys

def is_blender_socket_open():
    HOST = 'localhost'
    PORT = 5001

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
        return True
    except ConnectionRefusedError:
        return False

# You can then use this function in your script
if is_blender_socket_open():
    print("Blender socket is open")
else:
    print("Blender socket is closed")
