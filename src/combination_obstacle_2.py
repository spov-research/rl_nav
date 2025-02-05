#!/usr/bin/env python3

import rospy
import time
from gazebo_msgs.msg import ModelState, ModelStates

class Combination():
    def __init__(self):
        self.pub_model = rospy.Publisher('gazebo/set_model_state', ModelState, queue_size=1)
        self.moving()

    def moving(self):
        state = 0
        while not rospy.is_shutdown():
            model = rospy.wait_for_message('gazebo/model_states', ModelStates)
            for i in range(len(model.name)):
                if model.name[i] == 'obstacle_2':
                    obstacle_2 = ModelState()
                    obstacle_2.model_name = model.name[i]
                    obstacle_2.pose = model.pose[i]
                    if abs(obstacle_2.pose.position.x + 2) < 0.05 and abs(obstacle_2.pose.position.y + 2) < 0.05:
                        state = 0

                    if state == 0:
                        obstacle_2.pose.position.x += 0.007
                        obstacle_2.pose.position.y -= 0.001
                        if abs(obstacle_2.pose.position.x + 1.3) < 0.05 and abs(obstacle_2.pose.position.y + 2.1) < 0.05:
                            state = 1

                    elif state == 1:
                        obstacle_2.pose.position.x += 0.009
                        obstacle_2.pose.position.y += 0.009
                        if abs(obstacle_2.pose.position.x + 0.4) < 0.05 and abs(obstacle_2.pose.position.y + 1.2) < 0.05:
                            state = 2

                    elif state == 2:
                        obstacle_2.pose.position.x -= 0.006
                        obstacle_2.pose.position.y += 0.006
                        if abs(obstacle_2.pose.position.x + 1) < 0.05 and abs(obstacle_2.pose.position.y + 0.6) < 0.05:
                            state = 3

                    elif state == 3:
                        obstacle_2.pose.position.x += 0.008
                        obstacle_2.pose.position.y -= 0.001
                        if abs(obstacle_2.pose.position.x + 0.2) < 0.05 and abs(obstacle_2.pose.position.y + 0.7) < 0.05:
                            state = 4

                    elif state == 4:
                        obstacle_2.pose.position.x += 0.013
                        obstacle_2.pose.position.y -= 0.013
                        if abs(obstacle_2.pose.position.x - 1.1) < 0.05 and abs(obstacle_2.pose.position.y + 2) < 0.05:
                            state = 5

                    elif state == 5:
                        obstacle_2.pose.position.x += 0.009
                        obstacle_2.pose.position.y += 0.01
                        if abs(obstacle_2.pose.position.x - 2) < 0.05 and abs(obstacle_2.pose.position.y + 1) < 0.05:
                            state = 6

                    elif state == 6:
                        obstacle_2.pose.position.x -= 0.008
                        obstacle_2.pose.position.y += 0.01
                        if abs(obstacle_2.pose.position.x - 1.2) < 0.05 and abs(obstacle_2.pose.position.y + 0) < 0.05:
                            state = 7

                    elif state == 7:
                        obstacle_2.pose.position.x -= 0.007
                        obstacle_2.pose.position.y += 0.02
                        if abs(obstacle_2.pose.position.x - 0.5) < 0.05 and abs(obstacle_2.pose.position.y - 2) < 0.05:
                            state = 8

                    elif state == 8:
                        obstacle_2.pose.position.x -= 0.026 * 0.5
                        obstacle_2.pose.position.y -= 0.002 * 0.5
                        if abs(obstacle_2.pose.position.x + 2.1) < 0.05 and abs(obstacle_2.pose.position.y - 1.8) < 0.05:
                            state = 9

                    elif state == 9:
                        obstacle_2.pose.position.x += 0.016 * 0.5
                        obstacle_2.pose.position.y -= 0.016 * 0.5
                        if abs(obstacle_2.pose.position.x + 0.5) < 0.05 and abs(obstacle_2.pose.position.y - 0.2) < 0.05:
                            state = 10

                    elif state == 10:
                        obstacle_2.pose.position.x -= 0.004 * 0.5
                        obstacle_2.pose.position.y -= 0.023 * 0.5
                        if abs(obstacle_2.pose.position.x + 0.9) < 0.05 and abs(obstacle_2.pose.position.y + 2.1) < 0.05:
                            state = 11

                    elif state == 11:
                        obstacle_2.pose.position.x -= 0.011
                        obstacle_2.pose.position.y += 0.001
                        if abs(obstacle_2.pose.position.x + 2) < 0.05 and abs(obstacle_2.pose.position.y + 2) < 0.05:
                            state = 0

                    self.pub_model.publish(obstacle_2)
                    time.sleep(0.1)

def main():
    rospy.init_node('combination_obstacle_2')
    try:
        combination = Combination()
    except rospy.ROSInterruptException:
        pass

if __name__ == '__main__':
    main()