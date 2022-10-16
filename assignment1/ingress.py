# based on https://pythontic.com/modules/socket/udp-client-server-example
import socket
import os


localIP     = "ingress"
localPort   = 50000
bufferSize  = 1024

worker1AddressPort = ('worker1', 51000)
worker2AddressPort = ('worker2', 52000)


# Create a datagram socket
UDPIngressSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPIngressSocket.bind((localIP, localPort))

print("UDP server up and listening")

# Listen for incoming datagrams

msgFromClient = UDPIngressSocket.recvfrom(bufferSize)
message = msgFromClient[0]
address = msgFromClient[1]
clientMsg = "Message from Client:{}".format(message)
clientIP  = "Client IP Address:{}".format(address)
print(clientMsg)
print(clientIP)

if "{}".format(message) == "b'worker1'":
    targetPort = worker1AddressPort
    print("worker 1 has been requested")
    print('targetPort:',targetPort)
if "{}".format(message) == "b'worker2'":
    targetPort = worker2AddressPort
    print("worker 2 has been requested")
    print('targetPort:',targetPort)
    #print(bytesAddressPair)

requestFile = 'Please enter the file name:'
requestFile = str.encode(requestFile,'utf-8')
# Sending a reply to client
UDPIngressSocket.sendto(requestFile, targetPort)

# Recieve the file
while True:
    msgFromWorker = UDPIngressSocket.recvfrom(bufferSize)
    msg = msgFromWorker[0]
    port = msgFromWorker[1]
    if ("{}".format(port[1]) == "51000"):
        if ("{}".format(msg) == "b'SUCCESS!'"):
            break
        with open("worker1File.txt", "a") as file:
            file.write(msg.decode('utf-8'))
    if ("{}".format(port[1]) == "52000"):
        if ("{}".format(msg) == "b'SUCCESS!'"):
            break
        with open("worker2File.txt", "a") as file:
            file.write(msg.decode('utf-8'))


if "{}".format(message) == "b'worker1'":
    with open("worker1File.txt", "rb") as file:
        while True:
            bytesToSend = file.read(bufferSize)
            if not bytesToSend:
                break  # no more bytes left to send
            UDPIngressSocket.sendto(bytesToSend, address)
        print("Packet Sent To Client")
    os.remove('worker1File.txt')
    UDPIngressSocket.sendto("SUCCESS!".encode(), address)
    print("worker1 file sent to client")


if "{}".format(message) == "b'worker2'":
    with open("worker2File.txt", "rb") as file:
        while True:
            bytesToSend = file.read(bufferSize)
            if not bytesToSend:
                break  # no more bytes left to send
            UDPIngressSocket.sendto(bytesToSend, address)
            print("Packet Sent To Client")
    os.remove('worker2File.txt')
    UDPIngressSocket.sendto("SUCCESS".encode(), address)
    print("worker2 file sent to client")

