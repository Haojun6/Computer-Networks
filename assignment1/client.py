# based on https://pythontic.com/modules/socket/udp-client-server-example
import socket

serverAddressPort   = ("ingress", 50000)
bufferSize          = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
print("Client up and listening")
worker = input('Please input the worker you request: e.g.worker1/worker2')
bytesToSend = str.encode(worker,'utf-8')

# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
while True:
    msgFromWorker = UDPClientSocket.recvfrom(bufferSize)
    msg = msgFromWorker[0]
    port = msgFromWorker[1]
    if '{}'.format(worker) == 'worker1':
        if '{}'.format(msg) == "b'SUCCESS!'":
            print(msg)
            break
        with open ('worker1Recieve.txt','a') as file:
            file.write(msg.decode('utf-8'))
    if '{}'.format(worker) == 'worker2':
        if '{}'.format(msg) == "b'SUCCESS!'":
            print(msg)
            break
        with open ('worker2Recieve.txt','a') as file:
            file.write(msg.decode('utf-8'))

