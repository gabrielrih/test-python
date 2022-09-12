'''
    Socket testing
    Client side
    Reference: 
        https://www.geeksforgeeks.org/socket-programming-python/
        https://docs.python.org/3/library/socket.html#example
'''
import socket

# default port for socket
port = 50007
ip = '127.0.0.1'

try:
    # ipv4 TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, port))
        while True:
            messageToBeSent = input('> ')
            s.sendall(bytes(messageToBeSent, 'utf-8'))
        #print("Waiting for a response...")
        #data = s.recv(1024)
        #print('Received', repr(data))    
except socket.herror as err:
    print ("Error: %s" %(err))