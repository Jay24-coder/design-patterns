# System classes
class DVDPlayer:
    def play(self):
        print("DVD Player: Playing movie")
    def stop(self):
        print("DVD Player: Stopped")

class Projector:
    def turnOn(self):
        print("Turning on the projector")
    def turnOff(self):
        print("Turning off the projector")

class SoundSystem:
    def setVolume(self, level):
        print(f"Sound System: Volume set to {level}")
    def turnOff(self):
        print("Turning off the sound system")

# Facade class
class HomeTheatreFacade:
    def __init__(self,dvd, projector, sound):
        self.dvd = dvd
        self.projector = projector
        self.sound = sound

    def watchMovie(self):
        print("Facade: Setting up movie...")
        self.projector.turnOn()
        self.sound.setVolume(30)
        self.dvd.play()

    def endMovie(self):
        print("Facade: Shutting down...")
        self.dvd.stop()
        self.projector.turnOff()
        self.sound.turnOff()

# Client Code
dvd = DVDPlayer()
projector = Projector()
sound = SoundSystem()

# Using the facade
theatre = HomeTheatreFacade(dvd=dvd, projector=projector, sound=sound)
theatre.watchMovie()
print()
theatre.endMovie()