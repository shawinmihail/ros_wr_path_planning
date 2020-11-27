cmake_minimum_required(VERSION 2.8.3)
project(ros_wr_path_planning)
find_package(catkin REQUIRED COMPONENTS)
catkin_package()
catkin_python_setup()

catkin_install_python(PROGRAMS src/ros_wr_path_planning/rspawner_example.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
