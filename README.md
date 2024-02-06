# python-keypoint-tracking
This script implements keypoint tracking logic using ![OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose?tab=readme-ov-file) and a simple socket implementation to send keypoint-data.

# Prerequisites
### OpenPose *(refer to the official OpenPose ![docs](https://cmu-perceptual-computing-lab.github.io/openpose/web/html/doc/index.html) for detailed instructions)*
We chose the "Compiling and running OpenPose from source" option for our installation.

Our System:
- Windows 10
- ZOTAC GAMING GeForce RTX 4090 Trinity (NVIDIA)

There are some known issues with installing OpenPose. After some trial and error, this is the combination of dependencies that worked for us:
  - CUDA 11.1.1
  - cuDNN 8.1.0
  - Visual Studio Enterprise 2019 (Version - 16.11.32)
  - opencv 4.9.0.80
  - Python 3.7.0
  - CMake 3.28.3

The links within getModels.bat file in the OpenPose repository no longer work. As of January 2024, ![this](https://drive.google.com/drive/folders/1USEdy_7uvwO4PIqsQJq8kT0sX4H4f7nn) Google Drive folder provides all necessary models to run OpenPose.\
After downloading, they have to be manually placed in the correct folder within the repository. 

# Install and run
1. Install OpenPose\
   Follow ![these instructions](https://cmu-perceptual-computing-lab.github.io/openpose/web/html/doc/md_doc_installation_0_index.html#compiling-and-running-openpose-from-source) for installation. Importantly, check the "BUILD_PYTHON" flag in CMake configuration.
2. Within openpose.py, change the base directory path to point to your local OpenPose build and the model directory path to point to your local folder containing all models:\
  `base_dir_path = str(Path("C:/Users/Marit/KI/openpose/build"))`\
  `model_dir_path = str(Path("C:/Users/Marit/KI/openpose/models"))`
3. Run main.py

