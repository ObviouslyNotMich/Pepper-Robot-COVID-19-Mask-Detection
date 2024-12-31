import time


class Motion:
    """This class is used by pepper.py to load the motion functions for the robot"""
    session = motion_service = posture_service = animation_service = None
    pepper = None

    """This is where the class variables are initialized"""
    def __init__(self, session):
        self.session = session
        self.motion_service = self.session.service("ALMotion")
        self.posture_service = self.session.service("ALRobotPosture")
        self.animation_service = self.session.service("ALAnimationPlayer")

        self.motion_service.setIdlePostureEnabled("Arms", False)
        self.motion_service.moveInit()

    """This is where the robot will stand"""
    def stand(self, speed=0.1):
        self.posture_service.goToPosture("StandInit", speed)
        self.set_head(0, 0)
        return self

    """This is where the robot will sleep"""
    def sleep(self):
        self.motion_service.rest()
        return self

    """This is where the robot will wake up"""
    def wake_up(self):
        self.motion_service.wakeUp()
        return self

    """This is where the robot will set his head to the position you gave"""
    def set_head(self, x, y, speed=0.1):
        self.motion_service.setStiffnesses("Head", 1.0)

        self.motion_service.setAngles("HeadYaw", x, speed)
        self.motion_service.setAngles("HeadPitch", y, speed)
        return self

    """This is where the robot will move his head"""
    def head_move_1(self):
        names = ["HeadYaw", "HeadPitch"]
        angleLists = [[1.0, 0.0], [0.4, 0.0, 0.1]]
        times = [[3, 5], [4, 5, 6]]
        isAbsolute = True
        self.motion_service.angleInterpolation(names, angleLists, times, isAbsolute)
        return self

        # http://doc.aldebaran.com/2-4/naoqi/motion/control-joint.html :: angleInterpolation

    """This is where the robot will move his head to the left"""
    def move_head_left(self, speed=1.0):
        names = ["HeadYaw", "HeadPitch"]
        angleLists = [[1.0], [0.0]]
        times = [[speed], [speed]]
        isAbsolute = True
        self.motion_service.angleInterpolation(names, angleLists, times, isAbsolute)

        return self

        # http://doc.aldebaran.com/2-4/naoqi/motion/control-joint.html :: angleInterpolation

    """This is where the robot will move his head to the right"""
    def move_head_right(self, speed=1.0):
        names = ["HeadYaw", "HeadPitch"]
        angleLists = [[-1.0], [0.0]]
        times = [[speed], [speed]]
        isAbsolute = True
        self.motion_service.angleInterpolation(names, angleLists, times, isAbsolute)

        return self

        # http://doc.aldebaran.com/2-4/naoqi/motion/control-joint.html :: angleInterpolation

    """This is where the robot will move his head to the center"""
    def move_head_center(self, speed=1.0):
        names = ["HeadYaw", "HeadPitch"]
        angleLists = [[0.0], [0.0]]
        times = [[speed], [speed]]
        isAbsolute = True
        self.motion_service.angleInterpolation(names, angleLists, times, isAbsolute)

        return self

    """This is where the robot will set his hand to the position you gave"""
    def set_hand(self, side, shoulder_pitch=None, shoulder_roll=None, speed=0.3, wait_time=None):
        # determine the arm to rotate
        if side in ['left', 'l', 'lf', 'lft']:
            side = 'L'
        else:
            side = 'R'

        self.motion_service.setStiffnesses("Arms", 1)
        if shoulder_pitch:
            self.motion_service.setAngles(side + "ShoulderPitch", shoulder_pitch, speed)
        if wait_time:
            time.sleep(wait_time)
        if shoulder_roll:
            self.motion_service.setAngles(side + "ShoulderRoll", shoulder_roll, speed)
        return self

    """This is where the robot will rotate his wrist to the side you gave"""
    def rotate_wrist(self, side, rotation=1.0, speed=0.3):
        # determine the wrist to rotate
        if side in ['left', 'l', 'lf', 'lft']:
            side = 'L'
        else:
            side = 'R'

        self.motion_service.setAngles(side + "WristYaw", rotation, speed)
        return self

    """This is where the robot will move his elbow to the position you gave"""
    def move_elbow(self, side, rotation=1.0, speed=0.3):
        # determine the wrist to rotate
        if side in ['left', 'l', 'lf', 'lft']:
            side = 'L'
        else:
            side = 'R'

        self.motion_service.setAngles(side + "ElbowRoll", rotation, speed)
        return self

    """This is where the robot will rotate his elbow to the position you gave"""
    def rotate_elbow(self, side, rotation=1.0, speed=0.3):
        # determine the wrist to rotate
        if side in ['left', 'l', 'lf', 'lft']:
            side = 'L'
        else:
            side = 'R'

        self.motion_service.setAngles(side + "ElbowYaw", rotation, speed)
        return self

    """This is where the robot will move his arm up"""
    def arm_up(self, side, speed=0.3):
        return self.set_hand(side, -1, 0, speed)

    """This is where the robot will move his arm down"""
    def arm_down(self, side, speed=0.3):
        return self.set_hand(side, 1, 0, speed)

    """This is where the whole robot will rotate to the right"""
    def rotate_right(self):
        self.motion_service.moveTo(0, 0, -1.57)
        # self.motion_service.waitUntilMoveIsFinished()

        return self

    """This is where the whole robot will rotate to the left"""
    def rotate_left(self):
        self.motion_service.moveTo(0, 0, -1.57)
        # self.motion_service.waitUntilMoveIsFinished()

        return self

    """This is where the robot will wave"""
    def wave(self):
        self.animation_service.run("animations/Stand/Gestures/Hey_1")

    """This is where the robot will dab"""
    def dab(self):
        # Here the robot will move his hands and elbow to the specific cordinates
        self.set_hand("left", -1.5, 3, 1)
        self.set_head(-1, 0.4)
        self.set_hand("right", -0.3, 0, 0.3)
        self.move_elbow("right", 2.5, 0.3)

        time.sleep(.5)

        self.rotate_elbow("right", 0.5, 0.3)
        # time.sleep(.5)

        time.sleep(3)

        # back to begin position
        self.posture_service.goToPosture("StandInit", 0.5)
        self.set_head(0, 0)

        return self

    """This is where the robot will move"""
    def move(self):
        print("move")

    """This is where the robot will move his head"""
    def move_head(self):
        names = "HeadYaw"
        angleLists = [1.0, -1.0, 1.0, -1.0, 0.0]
        times = [1.0, 2.0, 3.0, 4.0, 5.0]
        isAbsolute = True
        self.motion_service.angleInterpolation(names, angleLists, times, isAbsolute)

        return self

    """This is where the robot will wave"""
    def run(self, animation_file, delay=None):
        if delay:
            time.sleep(delay)
        self.animation_service.run(animation_file)

    """This is where the robot will point his hand to the left"""
    def pointing_left(self):
        self.set_hand("left", -1.5, 5, 1)
        time.sleep(4)
        self.posture_service.goToPosture("StandInit", 0.5)
        return self

    """This is where the robot will point his hand to the right"""
    def pointing_right(self):
        self.set_hand("right", -1.5, 5, 1)
        time.sleep(4)
        self.posture_service.goToPosture("StandInit", 0.5)
        return self

    """This is where the robot will blink his eyes"""
    def blink_eyes(self, rgb):

        self.blink_eyes([255, 0, 0])

        self.led_service.fadeRGB('AllLeds', rgb[0], rgb[1], rgb[2], 1.0)

    """This is where the robot will dance"""
    def dance(self):
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append(
            [1.52, 2.36, 3.32, 4.16, 5.08, 5.92, 6.88, 7.72, 8.16, 8.84, 9.68, 10.64, 11.48, 12.4, 13.24, 14.2, 15.04,
             16.24])
        keys.append(
            [-0.476475, 0.338594, -0.476475, 0.338594, -0.476475, 0.338594, -0.476475, 0.338594, 0.0680678, -0.476475,
             0.338594, -0.476475, 0.338594, -0.476475, 0.338594, -0.476475, 0.338594, -0.17185])

        names.append("HeadYaw")
        times.append(
            [1.52, 2.36, 3.32, 4.16, 5.08, 5.92, 6.88, 7.72, 8.16, 8.84, 9.68, 10.64, 11.48, 12.4, 13.24, 14.2, 15.04,
             16.24])
        keys.append(
            [-0.745256, 0.0411095, -0.745256, 0.0411095, -0.745256, 0.018508, -0.745256, 0.289725, 0.425684, 0.745256,
             -0.0411095, 0.745256, -0.0411095, 0.745256, -0.018508, 0.745256, -0.289725, 0.00916195])

        names.append("HipPitch")
        times.append(
            [0.68, 1.52, 2.36, 3.32, 4.16, 5.08, 5.92, 6.88, 7.72, 8.84, 9.68, 10.64, 11.48, 12.4, 13.24, 14.2, 15.04,
             16.24])
        keys.append([-0.376033, -0.036954, -0.344024, -0.0404086, -0.339835, -0.038321, -0.341769, -0.0367355, -0.34817,
                     -0.035085, -0.341769, -0.0382761, -0.339629, -0.0396041, -0.341605, -0.0362713, -0.343065,
                     -0.0495279])

        names.append("HipRoll")
        times.append(
            [1.52, 2.36, 3.32, 4.16, 5.08, 5.92, 6.88, 7.72, 8.84, 9.68, 10.64, 11.48, 12.4, 13.24, 14.2, 15.04, 16.24])
        keys.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        names.append("KneePitch")
        times.append(
            [0.68, 1.52, 2.36, 3.32, 4.16, 5.08, 5.92, 6.88, 7.72, 8.84, 9.68, 10.64, 11.48, 12.4, 13.24, 14.2, 15.04,
             16.24])
        keys.append(
            [0.166965, -0.00379234, 0.185949, -0.0129339, 0.180821, -0.00320919, 0.187035, -0.00931236, 0.182162,
             -0.0111253, 0.187035, -0.00683206, 0.184441, -0.0119436, 0.179202, -0.0114876, 0.187691, -0.013167])

        names.append("LElbowRoll")
        times.append(
            [0.68, 1.04, 1.48, 2.32, 3.28, 4.12, 5.04, 5.88, 6.84, 7.68, 8.12, 8.48, 8.8, 9.2, 9.64, 10.12, 10.6, 11,
             11.44, 11.92, 12.36, 12.76, 13.2, 13.68, 14.16, 14.56, 15, 15.6, 16.2, 16.4])
        keys.append(
            [-1.37289, -1.12923, -0.369652, -0.202446, -0.369652, -0.202446, -0.369652, -0.202446, -0.369652, -0.202446,
             -0.820305, -0.23305, -0.138102, -1.309, -0.257754, -1.4591, -0.138102, -1.309, -0.257754, -1.4591,
             -0.138102, -1.309, -0.257754, -1.4591, -0.138102, -1.309, -0.257754, -0.984366, -0.513992, -0.424876])

        names.append("LElbowYaw")
        times.append(
            [0.68, 1.48, 2.32, 3.28, 4.12, 5.04, 5.88, 6.84, 7.68, 8.12, 8.48, 8.8, 9.2, 9.64, 10.12, 10.6, 11, 11.44,
             11.92, 12.36, 12.76, 13.2, 13.68, 14.16, 14.56, 15, 15.6, 16.2, 16.4])
        keys.append(
            [-0.65506, -0.380475, -0.618244, -0.380475, -0.618244, -0.380475, -0.618244, -0.380475, -0.618244, 0.410152,
             0.818273, 0.851412, 0.0750492, 0.00157596, 0.460767, 0.851412, 0.0750492, 0.00157596, 0.460767, 0.851412,
             0.0750492, 0.00157596, 0.460767, 0.851412, 0.0750492, 0.00157596, -1.34565, -1.22484, -1.21037])

        names.append("LHand")
        times.append(
            [0.68, 1.04, 1.48, 2.32, 3.28, 4.12, 5.04, 5.88, 6.84, 7.68, 8.48, 8.8, 9.2, 9.64, 10.12, 10.6, 11, 11.44,
             11.92, 12.36, 12.76, 13.2, 13.68, 14.16, 14.56, 15, 15.6, 16.2, 16.4])
        keys.append(
            [0.2, 0.6, 0.2648, 0.264, 0.2648, 0.264, 0.2648, 0.264, 0.2648, 0.264, 0.663802, 0.928, 0.3, 0.0283999,
             0.75, 0.928, 0.3, 0.0283999, 0.75, 0.928, 0.3, 0.0283999, 0.75, 0.928, 0.3, 0.5284, 0.936396, 0.950347,
             0.2968])

        names.append("LShoulderPitch")
        times.append(
            [0.68, 1.48, 2.32, 3.28, 4.12, 5.04, 5.88, 6.84, 7.68, 8.12, 8.48, 8.8, 9.64, 10.6, 11.44, 12.36, 13.2,
             14.16, 15, 16.4])
        keys.append(
            [0.97784, 1.29573, 1.40466, 1.29573, 1.40466, 1.29573, 1.40466, 1.29573, 1.40466, 0.172788, -1.04904,
             -1.19188, 0.995607, -1.19188, 0.995607, -1.19188, 0.995607, -1.19188, 0.995607, 1.47106])

        names.append("LShoulderRoll")
        times.append(
            [0.68, 1.48, 2.32, 3.28, 4.12, 5.04, 5.88, 6.84, 7.68, 8.48, 8.8, 9.2, 9.64, 10.12, 10.6, 11, 11.44, 11.92,
             12.36, 12.76, 13.2, 13.68, 14.16, 14.56, 15, 15.6, 16.2])
        keys.append(
            [0.500047, 0.401871, 0.35585, 0.401871, 0.35585, 0.401871, 0.35585, 0.401871, 0.35585, 0.886453, 0.966481,
             1.23332, 0.324005, 1.23332, 0.966481, 1.23332, 0.324005, 1.23332, 0.966481, 1.23332, 0.324005, 1.23332,
             0.966481, 1.23332, 0.324005, 0.407503, 0.146991])

        names.append("LWristYaw")
        times.append(
            [0.68, 1.04, 1.48, 2.32, 3.28, 4.12, 5.04, 5.88, 6.84, 7.68, 8.48, 8.8, 9.64, 10.6, 11.44, 12.36, 13.2,
             14.16, 15, 16.2, 16.4])
        keys.append(
            [0.11961, -0.289725, -0.395814, -0.420357, -0.395814, -0.420357, -0.395814, -0.420357, -0.395814, -0.420357,
             -0.122946, -0.107338, -0.400331, -0.107338, -0.400331, -0.107338, -0.400331, -0.107338, -0.400331,
             0.000370312, 0.0827939])

        names.append("RElbowRoll")
        times.append(
            [0.68, 1.08, 1.52, 1.92, 2.36, 2.84, 3.32, 3.72, 4.16, 4.64, 5.08, 5.48, 5.92, 6.4, 6.88, 7.28, 7.72, 8.52,
             8.84, 9.68, 10.64, 11.48, 12.4, 13.24, 14.2, 15.04, 15.64, 16.24, 16.44])
        keys.append(
            [1.34689, 1.1205, 0.138102, 1.309, 0.257754, 1.4591, 0.138102, 1.309, 0.257754, 1.4591, 0.138102, 1.309,
             0.257754, 1.4591, 0.138102, 1.309, 0.257754, 0.372085, 0.369652, 0.202446, 0.369652, 0.202446, 0.369652,
             0.202446, 0.369652, 0.202446, 0.82205, 0.519567, 0.429562])

        names.append("RElbowYaw")
        times.append(
            [0.68, 1.08, 1.52, 1.92, 2.36, 2.84, 3.32, 3.72, 4.16, 4.64, 5.08, 5.48, 5.92, 6.4, 6.88, 7.28, 7.72, 8.52,
             8.84, 9.68, 10.64, 11.48, 12.4, 13.24, 14.2, 15.04, 15.64, 16.24, 16.44])
        keys.append(
            [0.59515, 0.567232, -0.851412, -0.0750492, -0.00157596, -0.460767, -0.851412, -0.0750492, -0.00157596,
             -0.460767, -0.851412, -0.0750492, -0.00157596, -0.460767, -0.851412, -0.0750492, -0.00157596, 0.352279,
             0.380475, 0.618244, 0.380475, 0.618244, 0.380475, 0.618244, 0.380475, 0.618244, 1.26711, 1.23132, 1.21028])

        names.append("RHand")
        times.append(
            [0.68, 1.08, 1.52, 1.92, 2.36, 2.84, 3.32, 3.72, 4.16, 4.64, 5.08, 5.48, 5.92, 6.4, 6.88, 7.28, 7.72, 8.52,
             8.84, 9.68, 10.64, 11.48, 12.4, 13.24, 14.2, 15.04, 16.24, 16.44])
        keys.append(
            [0.2, 0.95, 0.928, 0.3, 0.0283999, 0.75, 0.928, 0.3, 0.0283999, 0.75, 0.928, 0.3, 0.0283999, 0.75, 0.928,
             0.3, 0.5284, 0.271478, 0.2648, 0.264, 0.2648, 0.264, 0.2648, 0.264, 0.2648, 0.264, 0.596785, 0.2976])

        names.append("RShoulderPitch")
        times.append(
            [0.68, 1.52, 2.36, 3.32, 4.16, 5.08, 5.92, 6.88, 7.72, 8.52, 8.84, 9.68, 10.64, 11.48, 12.4, 13.24, 14.2,
             15.04, 16.24])
        keys.append(
            [0.915841, -1.19188, 0.995607, -1.19188, 0.995607, -1.19188, 0.995607, -1.19188, 0.995607, 1.281, 1.29573,
             1.40466, 1.29573, 1.40466, 1.29573, 1.40466, 1.29573, 1.40466, 1.47268])

        names.append("RShoulderRoll")
        times.append(
            [0.68, 1.08, 1.52, 1.92, 2.36, 2.84, 3.32, 3.72, 4.16, 4.64, 5.08, 5.48, 5.92, 6.4, 6.88, 7.28, 7.72, 8.52,
             8.84, 9.68, 10.64, 11.48, 12.4, 13.24, 14.2, 15.04, 15.64, 16.44])
        keys.append(
            [-0.905123, -1.30837, -0.966481, -1.23332, -0.324005, -1.23332, -0.966481, -1.23332, -0.324005, -1.23332,
             -0.966481, -1.23332, -0.324005, -1.23332, -0.966481, -1.23332, -0.324005, -0.397371, -0.401871, -0.35585,
             -0.401871, -0.35585, -0.401871, -0.35585, -0.401871, -0.35585, -0.310669, -0.174533])

        names.append("RWristYaw")
        times.append(
            [0.68, 1.52, 2.36, 3.32, 4.16, 5.08, 5.92, 6.88, 7.72, 8.52, 8.84, 9.68, 10.64, 11.48, 12.4, 13.24, 14.2,
             15.04, 16.24, 16.44])
        keys.append(
            [-0.401949, 0.107338, 0.400331, 0.107338, 0.400331, 0.107338, 0.400331, 0.107338, 0.400331, 0.391888,
             0.395814, 0.420357, 0.395814, 0.420357, 0.395814, 0.420357, 0.395814, 0.420357, 0.00501826, 0.108872])

        self.motion_service.angleInterpolation(names, keys, times, True)
        return self
