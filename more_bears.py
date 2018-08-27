
from strategy import LoudRoarStrategy
from strategy import GentleRoarStrategy
from strategy import OnForTenSecondsStrategy

loud_roar = LoudRoarStrategy()
gentle_roar = GentleRoarStrategy()
ten_seconds = OnForTenSecondsStrategy()


class Bear(object):
    def __init__(self, roar_strategy, light_strategy):
        self._roar_strategy = roar_strategy
        self._light_strategy = light_strategy

    def roar(self):
        self._roar_strategy.roar()

    def lights_on(self):
        self._light_strategy.lights_on()


# Types of Bears
class RealBear(Bear):
    def __init__(self):
        super(RealBear, self).__init__(loud_roar, None)

    def status(self):
        print("Wandering the forrest")


class ToyBear(Bear):
    def __init__(self):
        super(ToyBear, self).__init__(gentle_roar, ten_seconds)


class RobotBear(Bear):
    def __init__(self):
        super(RobotBear, self).__init__(loud_roar, ten_seconds)


# Note: Calling lights_on() on RealBear or ToyBear will result in AttributeError
robo = RobotBear()
robo.name = "Robo"
print(robo.name)
robo.roar()
robo.lights_on()