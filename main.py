import cv2
import time
from socket_connection import UnityClient
from openpose import init_openpose_import, create_openpose_wrapper

# init socket connection
unity_server_ip = "127.0.0.1"
unity_server_port = 13000

client = UnityClient(unity_server_ip, unity_server_port)
client.connect()


# init openpose
op_import = init_openpose_import()  # encapsulates objects / classes
op_wrapper = create_openpose_wrapper(op_import)  # encapsulates funtionality / api
datum = op_import.Datum()

cap = cv2.VideoCapture(0)
if not cap.isOpened():
        print("Cannot open camera")
        exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Process Image
    imageToProcess = frame
    datum.cvInputData = imageToProcess
    # print("datum: ", datum.poseKeypoints)
    op_wrapper.emplaceAndPop(op_import.VectorDatum([datum]))
    # break
    # cv2.imshow('frame', datum.cvOutputData)
    # print("Left wrist: ", datum.poseKeypoints[0][7][1])
    # print("Right wrist: ", datum.poseKeypoints[1][4][1])
    client.send_pose_keypoints(datum.poseKeypoints)
    if cv2.waitKey(1) == ord('q'):
        client.disconnect()
        break




