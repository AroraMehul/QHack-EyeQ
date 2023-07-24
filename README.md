# TODO
# eyeQ - Your Visionary Assistant


eyeQ is an innovative device that aims to empower visually impaired individuals with a comprehensive set of functionalities, enabling them to navigate their surroundings independently and access information effortlessly. Leveraging the power of the Oak-D camera, eyeQ utilizes cutting-edge hardware and software capabilities, including the IMU and depth cameras, to provide an enhanced and inclusive user experience.

## Hardware - Oak-D Camera

The Oak-D camera serves as the core hardware component of eyeQ. This powerful camera module is equipped with an integrated depth camera and an IMU (Inertial Measurement Unit). The depth camera enables accurate depth perception and object detection, while the IMU provides essential data for fall detection and precise positioning. By harnessing these features, eyeQ can create a holistic view of the environment, facilitating seamless navigation and interaction.

## Installation

To get started with eyeQ, follow these simple installation instructions:

1. Clone the depthai repository from Luxonis:
```
git clone https://github.com/luxonis/depthai.git
cd depthai
python install_requirements.py
```
2. Install the required packages using the provided script:
```
pip install -r requirements.txt
```
## Functionality

eyeQ is an advanced assistive technology device designed to empower visually impaired individuals with a comprehensive set of functionalities, enabling them to navigate their surroundings independently and access crucial information effortlessly. The project encompasses cutting-edge technologies, including depth estimation, object detection, point cloud building, IMU (Inertial Measurement Unit) odometry, path planning, and occupancy map building.

### Depth Estimation

Depth estimation is a fundamental feature of eyeQ, enabling accurate perception of the distance between objects and the camera. The depth estimation is achieved through sophisticated algorithms and neural networks running on the Oak-D camera's integrated depth sensor. By interpreting the depth information, eyeQ creates a detailed representation of the user's environment, facilitating object recognition and navigation.
### Object Detection

Object detection plays a crucial role in enhancing the safety and autonomy of visually impaired users. eyeQ leverages state-of-the-art object detection models to recognize and classify various objects, such as obstacles, doors, and other important landmarks. The detection results are then combined with depth estimation to provide real-time feedback to the user and facilitate safe and efficient navigation.
### Point Cloud Building

To create a holistic view of the surrounding environment, eyeQ utilizes point cloud building techniques. By combining the depth information from the camera's depth sensor, eyeQ generates a 3D point cloud representation of the scene. This 3D point cloud enhances the user's understanding of the environment, enabling them to navigate with more confidence and avoid potential obstacles.
### IMU Odometry

The IMU (Inertial Measurement Unit) data from the Oak-D camera is utilized for odometry calculations. By analyzing the IMU data, eyeQ can estimate the device's position and orientation changes over time. This information is crucial for updating the user's position during navigation and facilitating accurate path planning.
### Path Planning

Path planning is a vital component of eyeQ, ensuring that visually impaired users can navigate efficiently and safely in complex environments. By combining the depth information, object detection results, and IMU odometry, eyeQ devises optimal paths for the user to reach their desired destinations. The path planning algorithm considers obstacles, landmarks, and user preferences to provide seamless and collision-free navigation.
### Occupancy Map Building

eyeQ constructs an occupancy map, representing the user's environment as a grid where each cell indicates whether it is occupied or free. The occupancy map is continuously updated using depth information and object detection results. This map is instrumental in collision avoidance and enables eyeQ to provide real-time feedback to the user about the safe and accessible paths.
