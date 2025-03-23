cmake_minimum_required(VERSION 3.0.2)
project(docking_controller_wheel)


find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  roscpp
  rospy
  std_msgs
)

catkin_package(
  CATKIN_DEPENDS
  std_msgs
  geometry_msgs
)
catkin_install_python(
  PROGRAMS
  scripts/testcontroller.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)
