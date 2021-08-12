"""
This Program is for Voice less video Streaming using UDP protocol 
-------
This is a Server
    - Run Client Code first then run Server Code
    - Configure IP and PORT number of your Server
    
Requirements
    - Outside Connection 
    - IP4v needed select unused port number
    - WebCamera needed
"""
import cv2, socket, numpy, pickle    # Import Modules

s=socket.socket(socket.AF_INET , socket.SOCK_DGRAM)  # Gives UDP protocol to follow
ip="192.168.43.149"   # Server public IP
port=307              # Server port number
s.bind((ip,port))     # Bind the IP:port to connect 

while True:
    x=s.recvfrom(100000000)    # Recieve byte code sent by client using recvfrom
    clientip = x[1][0]         # x[1][0] in this client details stored,x[0][0] Client message Stored
    data=x[0]                  # Data sent by client
    data=pickle.loads(data)    # All byte code is converted to Numpy Code 
    data = cv2.imdecode(data, cv2.IMREAD_COLOR)  # Decode 
    cv2.imshow('my pic', data) # Show Video/Stream
    if cv2.waitKey(10) == 13:  # Press Enter then window will close
        break
cv2.destroyAllWindows()        # Close all windows