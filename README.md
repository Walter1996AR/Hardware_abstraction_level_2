# Minor Adaptive Robotics: hardware abstraction
Assignment for the minor Adaptive robotics 2018/2019.


## Dependencies 
This assignment depends on the rosserial package.
To install this package navigate to your src folder in your catkin workspace and clone this repository. Make sure you also do this on the raspberry pi. 


`cd ~/<your catkin workspace>/src/`

`git clone git clone https://github.com/ros-drivers/rosserial.git`

Make sure to clone this package into your workspace aswell: 

` cd ~/<your catkin workspace>/src/ `

` git clone https://github.com/Walter1996AR/hardware_abstraction_level_2 `

After that, build your workspace 
 
` cd/<your catkin workspace>/ `   

` catkin_make ` 

On your raspberry make sure you have ros kinetic up and running: 

Follow http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Kinetic%20on%20the%20Raspberry%20Pi to do this. 

Make sure you set up your pc as rosmaster and the raspberry as rosslave.


## Running this package 
first, launch roscore with:

`roscore` 

After that, start the masternode: 

` rosrun hardware_abstraction_2 Masternode.py ` 

Then start the serial communication with the arduino:

` roslaunch rosserial_python arduino_launch_node.launch ` 

Start the node on the raspberry:

` rosrun hardware_abstraction_2 raspberry_node.py ` 


 check communication via: 
 
 ` rostopic echo /<thing you want to check> ` 

