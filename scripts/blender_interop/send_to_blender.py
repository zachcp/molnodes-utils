
import socket
import sys

def send_to_blender(command):
    HOST = 'localhost'
    PORT = 5001

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            # Send the length of the command first
            s.sendall(len(command).to_bytes(4, byteorder='big'))
            # Then send the command itself
            s.sendall(command.encode('utf-8'))
            # Receive the response
            data = s.recv(1024)
            print(f"Received from Blender: {data.decode('utf-8')}")
    except ConnectionRefusedError:
        print("Error: Could not connect to Blender. Make sure the Blender REPL is running and the socket is open.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        script_path = sys.argv[-1]
        try:
            with open(script_path, 'r') as file:
                script_content = file.read()
            send_to_blender(script_content)
        except FileNotFoundError:
            print(f"Error: File {script_path} not found.")
    else:
        print("Usage: python send_to_blender.py <script_file_path>")
