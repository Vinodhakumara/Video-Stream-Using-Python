"""
This Program is for Voice less video Streaming using UDP protocol 
-------
This is a Client
    - Run Client Code first then Server Code
    - Configure IP and PORT number of your Server
    
Requirements
    - Outside Connection 
    - IP4v needed select unused port number
    - WebCamera needed
"""
import cv2, socket, pickle, os    # Import Modules


s=socket.socket(socket.AF_INET , socket.SOCK_DGRAM)  # Gives UDP protocol to follow
s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 10000000) # setSockoptTo open two protocols,SOL_SOCKET: Request applies to socket layer.
serverip="192.168.43.149"       # Server public IP
serverport=307                  # Server Port Number

cap = cv2.VideoCapture(0)       # Start Streaming video
while True:
    ret,photo = cap.read()      # Start Capturing a images/video
    cv2.imshow('my pic', photo) # Show Video/Stream
    ret, buffer = cv2.imencode(".jpg", photo, [int(cv2.IMWRITE_JPEG_QUALITY),30])  # Encode image from image to Buffer code(like [123,123,432....])
    x_as_bytes = pickle.dumps(buffer)       # Convert normal buffer Code(like [123,123,432....]) to Byte code(like b"\x00lOCI\xf6\xd4...")
    s.sendto(x_as_bytes,(serverip , serverport)) # Converted byte code is sending to server(serverip:serverport)
    if cv2.waitKey(10) == 13:    # Press Enter then window will close
        break                    
# Destroy all Windows/close
cv2.destroyAllWindows() 
cap.release()