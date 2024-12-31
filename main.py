from robot import pepper
import time

robot_pepper = None


def surveillance_mode(r_pepper):
    """
    This is the surveillance mode.
    """
    r_pepper.exploration().explore(2)
    r_pepper.exploration().save_exploration()
    r_pepper.exploration().start_localization()

    r_pepper.people_perception().start_detection()

    while True:
        r_pepper.exploration().go_to_random()
        time.sleep(60)


def entrance_mode(r_pepper):
    """
    This is the entrance mode.
    """
    r_pepper.people_perception().start_detection()


if __name__ == '__main__':
    """
    Here we create the robot_pepper object. Which allows us to control the robot. By sending it commands and receiving 
    data.
    """
    robot_pepper = pepper.Pepper("mirai.robot.hva-robots.nl")

    robot_pepper.start()
    robot_pepper.motion().wake_up()
    robot_pepper.autonomous_ability().set_autonomous_ability(True)
    robot_pepper.tablet().show_website()

    while True:
        if robot_pepper.mqtt_msg == "entrance_mode":
            robot_pepper.mqtt_msg = None
            robot_pepper.mode = "entrance_mode"
            entrance_mode(robot_pepper)

        if robot_pepper.mqtt_msg == "surveillance_mode":
            robot_pepper.mqtt_msg = None
            robot_pepper.mode = "surveillance_mode"
            surveillance_mode(robot_pepper)

        if robot_pepper.mqtt_msg == "stop":
            robot_pepper.mqtt_msg = None
            robot_pepper.system().shutdown()
            break
