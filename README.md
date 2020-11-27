# rebuild
. prepare.sh
cd ~/continuous-ros
catkin build ros_wr_path_planning --no-deps

# draw
. prepare.sh
cd ~/continuous-ros
./surf_world_start.sh 
rosrun kin_model gazebo_spawn_node
rosrun ros_wr_path_planning rspawner_example.py
