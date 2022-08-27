import socket
import encrypt


def main():
    # specify the IP address of the machine that you would like to send to
    TO_IP = "192.168.1.9"
    # specify the IP port that you would like to send messages out
    IP_PORT = 8080
    
    # encrypt the message using Caesar Cipher
    encrypted_msg = encrypt.caesar_cipher_encrypt(encrypt.MESSAGE, encrypt.SHIFT)
    
    print('IP address: ', TO_IP)
    print('Port number: ', IP_PORT)
    print('Encrypted message: ', encrypted_msg)

    # send out the enrypted message
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(encrypted_msg.encode(), (TO_IP, IP_PORT))
    
    print('Encrypted msg is sent!')
    

if __name__ == "__main__":
    main()
