
import abc  # Python's built-in abstract class library


class RoarStrategyAbstract(object):
    """This is how you define abstract classes in Python."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def roar(self):
        """Required Method"""

class LoudRoarStrategy(RoarStrategyAbstract):
    def roar(self):
        print("ROAR!! ROAR!!")

class GentleRoarStrategy(RoarStrategyAbstract):
    def roar(self):
        print("roar!")


class LightStrategyAbstract(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def lights_on(self):
        """Required Method"""

class OnForTenSecondsStrategy(LightStrategyAbstract):
    def lights_on(self):
        print("Lights up for 10 seconds.")