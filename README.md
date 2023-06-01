This is a fork of the [original repository](https://github.com/AssafUni/rl_nav.git) under the project [Smart_POV](https://github.com/hamidrezafahimi/Smart_POV.git) which funds basics for intelligence development on simulated voyager agents. The original code is editted such that it simply interacts - and may be evaluated - with our developed professional (D)RL-evaluation platform [MIIO2V](https://github.com/mohammadr-kaz/MIIO2V.git). A comparison of this project with [other similar works]() id documented [here]().

## Prerequisites

- Ubuntu 20.04
- ROS Noetic
- Anaconda

"Note: You may encounter some errors during running the simulation. Make sure the rospkg and defusedxml package is installed."

Install the following packages:
```sh
sudo apt-get install ros-noetic-map-server
sudo apt-get install ros-noetic-move-base
sudo apt-get install ros-noetic-navigation
pip install rospkg
pip install defusedxml
```


## How to Run

1. Create a ROS workspace.
```sh
source /opt/ros/noetic/setup.bash
mkdir -p ~/rl_nav/src
cd ~/rl_nav/
catkin_make
```
2. Clone these repositories inside src directory.
```sh
cd src
git clone https://github.com/spov-research/rl_nav.git
git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3.git
```
3. Make the ros package.
```sh
cd ..
catkin_make
```
4. Create a conda environment with python 3.7 and tensorflow 2.1. then activate it.
```sh
conda create -n rlnav python=3.7 tensorflow=2.1
activate rlnav
```
5. Install the following packages inside the conda environment.
```sh
pip install keras==2.3.1
```
----------------------------
- Training Stage 1:
6. Open a terminal inside the workspace. then run:
```sh
source devel/setup.bash
export TURTLEBOT3_MODEL=burger
roslaunch rl_nav turtlebot3_stage_1.launch
```
Open another terminal in workspace then run:
```sh
source devel/setup.bash
roslaunch rl_nav navigation_123.launch
```
Open another terminal in workspace then run:
```sh
source devel/setup.bash
export TURTLEBOT3_MODEL=burger
chmod +x src/rl_nav/src/turtlebot3_dqn.py
roslaunch rl_nav turtlebot3_dqn_stage_1.launch
```
Once done, run next stage(end all terminals first)

----------------------------
- Training Stage 2:
Teminal 1:
```sh
source devel/setup.bash
export TURTLEBOT3_MODEL=burger
roslaunch rl_nav turtlebot3_stage_2.launch
```
Teminal 2:
```sh
source devel/setup.bash
roslaunch rl_nav navigation_123.launch
```
Teminal 3:
```sh
source devel/setup.bash
export TURTLEBOT3_MODEL=burger
roslaunch rl_nav turtlebot3_dqn_stage_2.launch
```
Once done, run next stage(end all terminals first)

----------------------------

- Training Stage 3:
Teminal 1:
```sh
source devel/setup.bash
export TURTLEBOT3_MODEL=burger
roslaunch rl_nav turtlebot3_stage_3.launch
```
Teminal 2:
```sh
source devel/setup.bash
roslaunch rl_nav navigation_123.launch
```
Teminal 3:
```sh
source devel/setup.bash
export TURTLEBOT3_MODEL=burger
roslaunch rl_nav turtlebot3_dqn_stage_3.launch
```
----------------------------
Once done, we can run a trained agent with a global planner:
Teminal 1:
```sh
source devel/setup.bash
export TURTLEBOT3_MODEL=burger
roslaunch rl_nav turtlebot3_stage_4.launch
```
Teminal 2:
```sh
source devel/setup.bash
roslaunch rl_nav navigation_4.launch
```
Teminal 3:
```sh
source devel/setup.bash
export TURTLEBOT3_MODEL=burger
roslaunch rl_nav turtlebot3_dqn_stage_4_run_global.launch
```