class Bear(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


# Bear Behavior
class LoudRoar(Bear):
    def roar(self):
        print("ROAR!! ROAR!!")


class GentleRoar(Bear):
    def roar(self):
        print("roar!")


# Types of Bears
class RealBear(LoudRoar):
    def status(self):
        print("Roaming the woods.")


class ToyBear(GentleRoar):
    def lights(self):
        print("Lights up for 10 seconds.")


class RobotBear(GentleRoar):
    def status(self):
        print("Bleep Bleep Bloop.")

print("\n")

fred = RealBear("Fred", 200)
print(fred.name)
fred.status()
fred.roar()

print("\n")

ted = ToyBear("Ted", 10)
print(ted.name)
ted.lights()
ted.roar()