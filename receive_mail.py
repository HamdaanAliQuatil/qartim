import socket
import sys

def encrypt_decrypt(message, key):
    key = key * (len(message) // len(key)) + key[:len(message) % len(key)]
    encrypted_message = ''.join(chr(ord(message_char) ^ ord(key_char)) for message_char, key_char in zip(message, key))
    return encrypted_message

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 8000
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")

    with open('key.txt', 'r') as file:
        KEY_SEQUENCE = file.read()

    while True:
        message = input("Enter a string or 'Quit' to exit: ")
        
        if message.lower() == 'quit':
            print("Exiting client.")
            client_socket.send(message.encode())
            sys.exit(0)

        encrypted_message = encrypt_decrypt(message, KEY_SEQUENCE)
        message_to_send = f"{encrypted_message} {KEY_SEQUENCE}"
        
        client_socket.send(message_to_send.encode())
        
        result = client_socket.recv(1024).decode()
        print(f"Server response: {result}")

    client_socket.close()

if __name__ == "__main__":
    main()
