import socket
import struct
class UnityClient:
    def __init__(self, ip, port):
        self.host = ip
        self.port = port
        self.sock = None

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        
    def send_pose_keypoints(self, pose_data):    
        if pose_data is None:
            return
        pose_data_flattened = [item for sublist1 in pose_data for sublist2 in sublist1 for item in sublist2]
        self.sock.sendall(struct.pack('%sf' % len(pose_data_flattened), *pose_data_flattened))
        
    def disconnect(self):
        self.sock.shutdown(socket.SHUT_RDWR)
        self.sock.close()
        if self.sock:
            self.sock = None




# host, port = "127.0.0.1", 13000
# data = ["Beatiful day in the neighborhood", "a beautiful day if a neighbor could", "won't you be mine?"]

# # SOCK_STREAM means TCP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# try:
#     # Connect to the server and send the data
#     sock.connect((host, port))
#     sock.sendall(data[0].encode("utf-8"))
#     sock.sendall(data[1].encode("utf-8"))
#     sock.sendall(data[2].encode("utf-8"))
#     # response = sock.recv(1024).decode("utf-8")
#     # print (response)

# finally:
#     sock.close()