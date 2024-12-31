
class System:
    """
    This is a system class that is used by the pepper class.
    To control the reboot and shutdown functions of the robot.
    """
    session = system_service = None

    def __init__(self, session):
        self.session = session
        self.system_service = self.session.service("ALSystem")

    def reboot(self):
        self.system_service.reboot()
        return self

    def shutdown(self):
        self.system_service.shutdown()
        return self
