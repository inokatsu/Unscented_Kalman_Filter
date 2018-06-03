# Unscented Kalman Filter 


In this project utilize an Unscented Kalman Filter to estimate the state of a moving object of interest with noisy lidar and radar measurements. Passing the project requires obtaining RMSE values that are lower that the tolerance outlined in the project rubric. 

This project involves the Term 2 Simulator which can be downloaded [here](https://github.com/udacity/self-driving-car-sim/releases)

This repository includes two files that can be used to set up and intall [uWebSocketIO](https://github.com/uWebSockets/uWebSockets) for either Linux or Mac systems. For windows you can use either Docker, VMware, or even [Windows 10 Bash on Ubuntu](https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/) to install uWebSocketIO. Please see [this concept in the classroom](https://classroom.udacity.com/nanodegrees/nd013/parts/40f38239-66b6-46ec-ae68-03afd8a601c8/modules/0949fca6-b379-42af-a919-ee50aa304e6a/lessons/f758c44c-5e40-4e01-93b5-1a82aa4e044f/concepts/16cf4a78-4fc7-49e1-8621-3450ca938b77) for the required version and installation scripts.

Once the install for uWebSocketIO is complete, the main program can be built and ran by doing the following from the project top directory.

1. mkdir build
2. cd build
3. cmake ..
4. make
5. ./UnscentedKF



Here is the main protcol that main.cpp uses for uWebSocketIO in communicating with the simulator.


INPUT: values provided by the simulator to the c++ program

["sensor_measurement"] => the measurment that the simulator observed (either lidar or radar)


OUTPUT: values provided by the c++ program to the simulator

["estimate_x"] <= kalman filter estimated position x
["estimate_y"] <= kalman filter estimated position y
["rmse_x"]
["rmse_y"]
["rmse_vx"]
["rmse_vy"]


[//]: # (Image References)

[image1]: ./pic/example_pic.png "Result"
[image2]: ./pic/NIS1.png "NIS formula"
[image3]: ./pic/NIS_table.png "NIS table"
[image4]: ./pic/NIS_lidar.png "NIS lidar"
[image5]: ./pic/NIS_radar.png "NIS radar"


---

## Other Important Dependencies
* cmake >= 3.5
  * All OSes: [click here for installation instructions](https://cmake.org/install/)
* make >= 4.1 (Linux, Mac), 3.81 (Windows)
  * Linux: make is installed by default on most Linux distros
  * Mac: [install Xcode command line tools to get make](https://developer.apple.com/xcode/features/)
  * Windows: [Click here for installation instructions](http://gnuwin32.sourceforge.net/packages/make.htm)
* gcc/g++ >= 5.4
  * Linux: gcc / g++ is installed by default on most Linux distros
  * Mac: same deal as make - [install Xcode command line tools](https://developer.apple.com/xcode/features/)
  * Windows: recommend using [MinGW](http://www.mingw.org/)

## Basic Build Instructions

1. Clone this repo.
2. Make a build directory: `mkdir build && cd build`
3. Compile: `cmake .. && make`
4. Run it: `./UnscentedKF` Previous versions use i/o from text files.  The current state uses i/o
from the simulator.

---

## Result
The image below is an image of the simulator.
![alt text][image1]

### RMSE(Root Mean Square Error)
The final RMSE values are following:

- X: 0.0712
- Y: 0.0819
- VX: 0.3394
- VY: 0.2233
</br>
</br>

## NIS (Normalized Innvation Squared)

One of the methods for testing accurary and consistancy was to use NIS(Normalized Innovation Squared).   

![alt text][image2]
##### cited from Udacity lecture
<br />

![alt text][image3]
##### cited from Udacity lecture
<br />
<br />

 To calculate NIS, this method first measures the innovation, which is the difference between the estimated positions and the ground truth value. This difference is then normalized by the inverse of the vector S. NIS says that in a 3 dimentional space, approximately 5% of the NIS values should be over 7.8 which is shown in table above.


![alt text][image4]
![alt text][image5]
