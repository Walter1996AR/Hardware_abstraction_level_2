# Minor Adaptive Robotics: hardware abstraction
Assignment for the minor Adaptive robotics 2018/2019.


## Level 2 
This assignment depends on the rosserial package.
To install this package navigate to your src folder in your catkin workspace and clone this repository. Make sure you also do this on the raspberry pi. 


`cd ~/<your catkin workspace>/src/`

`git clone https://github.com/Walter1996AR/hardware_abstraction_level_2.git`

After that compile your workspace 
 
` cd/<your catkin workspace>/ `   

` catkin_make ` 

### Running the package 
first, launch `roscore` 

After that, start the masternode. 

` rosrun hardware_abstraction_2 Masternode.py ` 

Then start the serial communication with the arduino 

` roslaunch rosserial_python arduino_launch_node.launch ` 

Start the node on the raspberry

` rosrun hardware_abstraction_2 raspberry_node.py ` 


 check communication via: 
 
 ` rostopic echo /<thing you want to check> ` 

