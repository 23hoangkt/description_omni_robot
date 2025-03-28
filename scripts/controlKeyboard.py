#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
import sys
import tty
import termios

class OmniKeyboardControl:
    def __init__(self):
        # Initialize ROS node
        rospy.init_node('omni_keyboard_control', anonymous=True)

        # Publishers for wheel velocity commands (4 wheels)
        self.pub_wheel_1 = rospy.Publisher('/wheel_1_joint_controller/command', Float64, queue_size=10)
        self.pub_wheel_2 = rospy.Publisher('/wheel_2_joint_controller/command', Float64, queue_size=10)
        self.pub_wheel_3 = rospy.Publisher('/wheel_3_joint_controller/command', Float64, queue_size=10)
        self.pub_wheel_4 = rospy.Publisher('/wheel_4_joint_controller/command', Float64, queue_size=10)

        # Maximum speed (radians/s)
        self.max_speed = 10.0  # Adjustable based on requirements

        # Current speed of each wheel
        self.wheel_1_speed = 0.0  # Left (Wheel 1)
        self.wheel_2_speed = 0.0  # Right (Wheel 2)
        self.wheel_3_speed = 0.0  # Bottom (Wheel 3)
        self.wheel_4_speed = 0.0  # Top (Wheel 4)

        # Distance from center to wheel (for rotation calculation)
        self.L = 1.0  # Normalized, adjust if needed

    def get_key(self):
        # Read a key from the keyboard without requiring Enter
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            key = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return key

    def run(self):
        rospy.loginfo("Controlling 4-wheel omni robot with keyboard:")
        rospy.loginfo("w: Forward, s: Backward, a: Left, d: Right, q: Rotate left, e: Rotate right")
        rospy.loginfo("x: Stop, Ctrl+C: Exit")

        while not rospy.is_shutdown():
            key = self.get_key()

            # Reset speeds to 0 before calculating new values
            self.wheel_1_speed = 0.0
            self.wheel_2_speed = 0.0
            self.wheel_3_speed = 0.0
            self.wheel_4_speed = 0.0

            # Define desired velocities (vx, vy, omega)
            vx = 0.0  # Linear velocity in x (left/right)
            vy = 0.0  # Linear velocity in y (forward/backward)
            omega = 0.0  # Angular velocity (rotation)

            # Map keyboard inputs to desired velocities
            if key == 'w':  # Forward
                vy = self.max_speed
            elif key == 's':  # Backward
                vy = -self.max_speed
            elif key == 'a':  # Left
                vx = -self.max_speed
            elif key == 'd':  # Right
                vx = self.max_speed
            elif key == 'q':  # Rotate left
                omega = self.max_speed
            elif key == 'e':  # Rotate right
                omega = -self.max_speed
            elif key == 'x':  # Stop
                vx = 0.0
                vy = 0.0
                omega = 0.0
            elif key == '\x03':  # Ctrl+C (ASCII code 3)
                self.wheel_1_speed = 0.0
                self.wheel_2_speed = 0.0
                self.wheel_3_speed = 0.0
                self.wheel_4_speed = 0.0
                self.pub_wheel_1.publish(self.wheel_1_speed)
                self.pub_wheel_2.publish(self.wheel_2_speed)
                self.pub_wheel_3.publish(self.wheel_3_speed)
                self.pub_wheel_4.publish(self.wheel_4_speed)
                rospy.loginfo("Stopping robot and exiting")
                break

            # Calculate wheel speeds for omni wheels (with corrected directions)
            self.wheel_1_speed = -vy + omega * self.L
            self.wheel_2_speed = vy + omega * self.L
            self.wheel_3_speed = -vx + omega * self.L
            self.wheel_4_speed = vx + omega * self.L

            # Publish velocity commands
            self.pub_wheel_1.publish(self.wheel_1_speed)
            self.pub_wheel_2.publish(self.wheel_2_speed)
            self.pub_wheel_3.publish(self.wheel_3_speed)
            self.pub_wheel_4.publish(self.wheel_4_speed)

            # Display current status
            rospy.loginfo(f"Wheel 1 (Left): {self.wheel_1_speed:.2f}, Wheel 2 (Right): {self.wheel_2_speed:.2f}, "
                          f"Wheel 3 (Bottom): {self.wheel_3_speed:.2f}, Wheel 4 (Top): {self.wheel_4_speed:.2f}")

            rospy.sleep(0.1)  # Prevent reading keys too quickly

if __name__ == '__main__':
    try:
        controller = OmniKeyboardControl()
        controller.run()
    except rospy.ROSInterruptException:
        pass