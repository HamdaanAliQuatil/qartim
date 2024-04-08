import socket
import sys
import binascii

def calculate_crc(data):
    crc = binascii.crc32(data.encode())
    return crc & 0xFFFFFFFF

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 8000
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")
    while True:
        message = input("Enter a string or 'Quit' to exit: ")
        crc = calculate_crc(message)
        message = f"{message} {crc}"
        client_socket.send(message.encode())
        if message.split()[0].lower() == 'quit':
            print("Exiting client.")
        sys.exit(0)
        result = client_socket.recv(1024).decode()
        print(f"Server response: {result}")

    client_socket.close()

if __name__ == "__main__":
    main()