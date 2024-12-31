import qi
import time
from autonomous_ability import AutonomousAbility
from robot.tablet import Tablet
from speech import Speech
from motion import Motion
from people_perception import PeoplePerception
from system import System
from exploration import Exploration
from tools.paho_mqtt import PahoMqtt


class Pepper:
    """Main pepper robot class which initializes all the other classes when the pepper object is made"""
    ip = port = _speech = _exploration = _motion = _autonomous_ability = _people_perception = _system =\
        _tablet = _paho_mqtt = session = None

    """Loads all the modules when the start method is called"""
    def load_modules(self):
        self._autonomous_ability = AutonomousAbility(self)
        self._people_perception = PeoplePerception(self)
        self._speech = Speech(self.session)
        self._motion = Motion(self.session)
        self._tablet = Tablet(self.session)
        self._system = System(self.session)
        self._exploration = Exploration(self.session)

    """Loads all the tools when the start method is called"""
    def load_tools(self):
        self._paho_mqtt = PahoMqtt(self)

    def __init__(self, ip, port=9559):
        self.ip = ip
        self.port = port
        self.mqtt_msg = None
        self.detection_callback = False
        self.mode = None

    """Makes an connection with the robot and initializes all the tools and modules"""
    def start(self):
        self.connect()
        self.load_modules()
        self.load_tools()

    """Connect method that tries to connect to the robot if it fails it prints a message with the ip and the port of
    the robot that it tried to connect to"""
    def connect(self):
        self.session = qi.Session()
        try:
            self.session.connect("tcp://" + self.ip + ":" + str(self.port))
            self.load_modules()
        except RuntimeError:
            print ("Can't connect to Naoqi at ip \"" + self.ip + "\" on port " + str(self.port))
            self.check_connection()

    """A method which checks the connection and tries to reconnect if the status was false"""
    def check_connection(self):
        connected = self.session.isConnected()

        print("Connection status: " + str(connected))

        if not connected:
            time.sleep(.1)
            print("Trying to reconnect...")
            self.connect()

    """returns AutonomousAbility class after checking the connection"""
    def autonomous_ability(self):
        self.check_connection()
        return self._autonomous_ability

    """returns PeoplePerception class after checking the connection"""
    def people_perception(self):
        self.check_connection()
        return self._people_perception

    """returns Speech class after checking the connection"""
    def speech(self):
        self.check_connection()
        return self._speech

    """returns Motion class after checking the connection"""
    def motion(self):
        self.check_connection()
        return self._motion

    """returns Exploration class after checking the connection"""
    def exploration(self):
        self.check_connection()
        return self._exploration

    """returns Tablet class after checking the connection"""
    def tablet(self):
        self.check_connection()
        return self._tablet

    """returns System class after checking the connection"""
    def system(self):
        self.check_connection()
        return self._system

    """returns Speech class"""
    def mqtt(self):
        return self._paho_mqtt
