import sys
import cv2
import os
from sys import platform
import argparse
from time import time
from pathlib import Path

base_dir_path = str(Path("C:/Users/Marit/KI/openpose/build"))  # Path to openpose build folder, needed to import pyopenpose
model_dir_path = str(Path("C:/Users/Marit/KI/openpose/models"))  # Path to openpose models folder

def init_openpose_import():
    try:
        # Windows Import
        if platform == "win32":
            # Change these variables to point to the correct folder (Release/x64 etc.)
            sys.path.append(f"{base_dir_path}{str(Path('/python/openpose/Release'))}")
            os.environ['PATH']  = os.environ['PATH'] + f";{base_dir_path}{str(Path('/x64/Release;'))}{base_dir_path}{str(Path('/bin;'))}"
            import pyopenpose as op
        else:
            # Change these variables to point to the correct folder (Release/x64 etc.)
            sys.path.append('../../python')
            # If you run `make install` (default path is `/usr/local/python` for Ubuntu), you can also access the OpenPose/python module from there. This will install OpenPose and the python library at your desired installation path. Ensure that this is in your python path in order to use it.
            # sys.path.append('/usr/local/python')
            from openpose import pyopenpose as op
    except ImportError as e:
        print('Error: OpenPose library could not be found. Did you enable `BUILD_PYTHON` in CMake and have this Python script in the right folder?')
        raise e
    return op 

def create_openpose_wrapper(openpose_import):
    # Custom Params (refer to include/openpose/flags.hpp for more parameters)
    params = dict()
    params["model_folder"] = model_dir_path
    params["logging_level"] = 3
    params["number_people_max"] = 2
    params["fps_max"] = -1
    params["disable_blending"] = True
    params["keypoint_scale"] = 3

    # Starting OpenPose
    op_wrapper = openpose_import.WrapperPython()
    op_wrapper.configure(params)
    op_wrapper.start()
    return op_wrapper    
