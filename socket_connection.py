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
