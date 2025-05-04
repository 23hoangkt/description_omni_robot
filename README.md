# Diff Drive Robot

Đây là dự án mô phỏng robot điều khiển vi sai (differential drive robot) sử dụng **ROS Noetic** và **Gazebo**. Dự án bao gồm các gói con để mô phỏng robot trong các tình huống như điều hướng, lập bản đồ SLAM và theo dõi con người. Robot có thể được điều khiển thông qua bàn phím hoặc các lệnh ROS, hỗ trợ các tác vụ như điều hướng và lập bản đồ.

---

## Yêu cầu

- Ubuntu 20.04
- ROS Noetic
- Python 3.8+ (yêu cầu cho `ultralytics`)

---

## Cài đặt và chạy dự án

1. Tạo và cấu hình không gian làm việc Catkin:
    ```bash
    mkdir -p ~/catkin_ws/src
    cd ~/catkin_ws/src
    ```

2. Sao chép repository:
    ```bash
    git clone https://github.com/23hoangkt/Diff_drive_robot.git
    ```

3. Cài đặt các gói phụ thuộc:
    ```bash
    cd ~/catkin_ws
    rosdep install --from-paths src --ignore-src -r -y
    ```

4. Biên dịch không gian làm việc:
    ```bash
    catkin_make
    source devel/setup.bash
    ```

5. Cài đặt các gói ROS bổ sung:
    ```bash
    sudo apt update
    sudo apt install ros-noetic-vision-msgs ros-noetic-hector-slam ros-noetic-slam-karto
    pip3 install ultralytics
    ```

---

## Khởi chạy dự án

### 1. Khởi động Gazebo với robot (gói `boe_bot`):
    ```bash
    roslaunch boe_bot gazebo.launch
    ```
    ![Gazebo with robot](https://raw.githubusercontent.com/23hoangkt/Diff_drive_robot/main/result/robot.png)

### 2. Khởi động SLAM với Hector SLAM (gói `boe_bot_slam`):
    ```bash
    roslaunch boe_bot_slam boe_bot_hector_slam.launch world_name:="turtlebot3_world.world"
    ```
    ![SLAM](https://raw.githubusercontent.com/23hoangkt/Diff_drive_robot/main/result/slam.png)

### 3. Điều khiển robot để quét bản đồ:
    ```bash
    rosrun teleop_twist_keyboard teleop_twist_keyboard.py
    ```

### 4. Lưu bản đồ:
    ```bash
    rosrun map_server map_saver -f my_map
    ```

### 5. Điều hướng (gói `boe_bot_navigation`):
    ```bash
    roslaunch boe_bot_navigation navigation.launch
    ```
    ![Navigation](https://raw.githubusercontent.com/23hoangkt/Diff_drive_robot/main/result/navigation.png)

### 6. Theo dõi con người (gói `boe_bot_human_tracking`):
    ```bash
    roslaunch boe_bot_human_tracking human_tracker.launch
    ```
    ![Human tracking](https://raw.githubusercontent.com/23hoangkt/Diff_drive_robot/main/result/human_follow.png)

---

## Cấu trúc thư mục

- `boe_bot/`: Mô phỏng robot trong Gazebo.
- `boe_bot_slam/`: Gói cho SLAM (Hector SLAM, Karto SLAM).
- `boe_bot_navigation/`: Gói cho điều hướng.
- `boe_bot_human_tracking/`: Gói cho theo dõi con người.
- `result/`: Chứa ảnh minh họa cho README.

---

## Giấy phép

Dự án này sử dụng giấy phép **MIT**.  
Xem file [LICENSE](LICENSE) để biết thêm chi tiết.

---

## Đóng góp

Mọi đóng góp đều được hoan nghênh! Bạn có thể:
- Tạo pull request
- Báo lỗi (issues)
- Cải tiến tài liệu hoặc tính năng mới

---

## Liên hệ

Nếu bạn có câu hỏi, vui lòng liên hệ qua GitHub hoặc email trong phần thông tin tài khoản.

---

**Lưu ý**: Nếu ảnh không hiển thị, kiểm tra:
- Đảm bảo bạn đang xem branch đúng (`master` hoặc branch mặc định).
- Làm mới trang hoặc thử mở trong chế độ ẩn danh.
