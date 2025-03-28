cmake_minimum_required(VERSION 2.8.3)

project(description_omni_robot)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  urdf
)

catkin_package()

find_package(roslaunch)

foreach(dir config launch meshes urdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)

catkin_install_python(PROGRAMS scripts/controlKeyboard.py scripts/arm_control.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})