
class AutonomousAbility:
    """
    This is an AutonomousAbility class. The goal of this class is to enable Autonomous life functions of the robot to
    make it look alive.
    """
    session = pepper = life_service = None

    def __init__(self, pepper):
        self.pepper = pepper

        self.session = pepper.session
        self.life_service = self.session.service("ALAutonomousLife")

    """Set the autonomous abilities on or off by providing a true or false arg"""
    def set_autonomous_ability(self, set_bool):
        self.life_service.setAutonomousAbilityEnabled("All", set_bool)
        return self
