# based on https://pythontic.com/modules/socket/udp-client-server-example
import socket

localIP     = "worker2"
localPort   = 52000
bufferSize  = 1024
ingressAddressPort   = ("ingress", 50000)

# Create a UDP socket at client side
UDPWorker2Socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind to address and ip
UDPWorker2Socket.bind((localIP, localPort))

print("Worker2 up and listening")


msgFromServer = UDPWorker2Socket.recvfrom(bufferSize)
msg = msgFromServer[0]
port = msgFromServer[1]
print(msg)

filename = input(">>>")

with open(filename, "rb") as file:
    while True:
        bytesToSend = file.read(bufferSize)
        if not bytesToSend:
            break #no more bytes left to send
        UDPWorker2Socket.sendto(bytesToSend, ingressAddressPort)
    print("Packet Sent To Ingress!")
    
print("ACK Send")
UDPWorker2Socket.sendto("SUCCESS!".encode('utf-8'), ingressAddressPort)