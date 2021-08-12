#!/usr/bin/python3
import cv2,socket,pickle,struct  # Import Libraries

#TCP Socket Creation
try:
    # AF_INET refers to the address of family of ip4v
    # SOCK_DGRAM means connection oriented TCP protocol
    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created Now Show …")
except socket.error as err:
    print("Socket creation failed with error {}".formatat(err))
    
ip="192.168.43.149"   # Server public IP
port=2323            # Server port number
# Bind the IP:port to connect 
skt.connect((server_ip,port))
data = b""
payload_size = struct.calcsize("Q")   # Setup type,Size
try:
    while True:
        # If data size exeeds "Q" 
        while len(data) < payload_size:
            packet = skt.recv(4*1024)
            if not packet: break
            data += packet
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q",packed_msg_size)[0]
        while len(data) < msg_size:
            data+= skt.recv(4*1024)
        img_data = data[:msg_size]
        data = data[msg_size:]
        frame= pickle.loads(img_data)
        cv2.imshow("Recieving video", frame)
        if cv2.waitKey(10) == 13:
            cv2.destroyAllWindows()
            break
    skt.close()
except:
    cv2.destroyAllWindows()
    skt.close()