#!/usr/bin/python3
import socket
import cv2
import pickle
import struct
#TCP Socket Creation
# AF_INET refers to the address of family of ip4v
# SOCK_DGRAM means connection oriented TCP protocol
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # setSockoptTo open two protocols,SOL_SOCKET: Request applies to socket layer.

ip="192.168.43.149"   # Server public IP
port=307              # Server port number
# Bind the IP:port to connect 
tcp_sock.bind(("192.168.43.149", 2323))
# Listening To Connections(clients), this typically used by server, where 
# "listen()" means can have multiple, Even we can limit client like this "listen(Number_of_clients)" Ex.-> "listen(5)"
tcp_sock.listen()
print("Accepting Connections…")

while True:
    # s ->Stores Client data in the form of bytes
    # addr -> Stores Client details(ip,port)
    # accept simply does accepts the request from client and stores data sent by client
    s, addr = tcp_sock.accept()
    print(f"Connected to {addr}!!")
    cap = cv2.VideoCapture(0)    # Start Streaming video, will return video from your first webcam
    while(cap.isOpened()):
        ret, frame= cap.read()

        #Serialise/flattening Data
        data = pickle.dumps(frame)

        # Bytes Conversion... Stores huge byte data into packet variable
        packet = struct.pack("Q", len(data))+data
        s.sendall(packet)     # keep on Sending back packets
        cv2.imshow("Server Side Streaming…",frame)  # Show Image
        if cv2.waitKey(10) == 13:
            cv2.destroyAllWindows()
            cap.release()
            break
tcp_sock.close()