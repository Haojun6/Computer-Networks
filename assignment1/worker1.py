# based on https://pythontic.com/modules/socket/udp-client-server-example
import socket

localIP     = "worker1"
localPort   = 51000
bufferSize  = 1024
ingressAddressPort   = ("ingress", 50000)

# Create a UDP socket at client side
UDPWorker1Socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind to address and ip
UDPWorker1Socket.bind((localIP, localPort))

print("Worker1 up and listening")


msgFromServer = UDPWorker1Socket.recvfrom(bufferSize)
msg = msgFromServer[0]
port = msgFromServer[1]
print(msg)

filename = input(">>>")

with open(filename, "rb") as file:
    while True:
        bytesToSend = file.read(bufferSize)
        if not bytesToSend:
            break #no more bytes left to send
        UDPWorker1Socket.sendto(bytesToSend, ingressAddressPort)
    print("Packet Send To Ingress!")
    
print("ACK Sent")
UDPWorker1Socket.sendto("SUCCESS!".encode('utf-8'), ingressAddressPort)