# Omni robot 4 wheel with gazebo 
# Khởi động gazebo cùng rviz

```roslaunch description_omni_robot gazebo.launch```
# Cấp quyền truy cập cho các file để rosrun 
``chmod +x "file_name"```
# Điều khiển bánh xe thông qua teleop_keyboard

```rosrun description_omni_robot controlKeyboard.py```

# Điều khiển tay máy thông qua teleop_keyboard 

```rosrun description_omni_robot arm_control.py```

# Hiển thị encoder 

```rosrun description display_encoders.py```


