"""
Facade Pattern Implementation

The Facade pattern provides a simplified interface to a complex subsystem.
This implementation demonstrates a home theater system where multiple components
(DVD player, projector, sound system) are coordinated through a single facade interface.
"""

from typing import Optional
from loguru import logger


class DVDPlayer:
    """DVD Player component for the home theater system."""
    
    def __init__(self) -> None:
        """Initialize the DVD player."""
        logger.info("DVD Player initialized")
    
    def play(self) -> None:
        """Start playing the movie."""
        logger.info("DVD Player: Playing movie")
        print("DVD Player: Playing movie")
    
    def stop(self) -> None:
        """Stop the movie playback."""
        logger.info("DVD Player: Stopped")
        print("DVD Player: Stopped")


class Projector:
    """Projector component for the home theater system."""
    
    def __init__(self) -> None:
        """Initialize the projector."""
        logger.info("Projector initialized")
    
    def turn_on(self) -> None:
        """Turn on the projector."""
        logger.info("Turning on the projector")
        print("Turning on the projector")
    
    def turn_off(self) -> None:
        """Turn off the projector."""
        logger.info("Turning off the projector")
        print("Turning off the projector")


class SoundSystem:
    """Sound system component for the home theater system."""
    
    def __init__(self) -> None:
        """Initialize the sound system."""
        logger.info("Sound System initialized")
    
    def set_volume(self, level: int) -> None:
        """
        Set the volume level of the sound system.
        
        Args:
            level: Volume level (0-100)
        """
        if not 0 <= level <= 100:
            logger.warning(f"Volume level {level} is out of range (0-100)")
            level = max(0, min(100, level))
        
        logger.info(f"Sound System: Volume set to {level}")
        print(f"Sound System: Volume set to {level}")
    
    def turn_off(self) -> None:
        """Turn off the sound system."""
        logger.info("Turning off the sound system")
        print("Turning off the sound system")


class HomeTheatreFacade:
    """
    Facade class that provides a simplified interface to the home theater system.
    
    This facade coordinates multiple complex subsystems (DVD player, projector, 
    sound system) and provides simple methods for common operations.
    """
    
    def __init__(self, dvd: DVDPlayer, projector: Projector, sound: SoundSystem) -> None:
        """
        Initialize the home theater facade.
        
        Args:
            dvd: DVD player instance
            projector: Projector instance
            sound: Sound system instance
        """
        self.dvd = dvd
        self.projector = projector
        self.sound = sound
        logger.info("Home Theater Facade initialized")
    
    def watch_movie(self) -> None:
        """
        Set up the home theater system for movie watching.
        
        This method coordinates all components to prepare for movie viewing:
        - Turns on the projector
        - Sets appropriate volume level
        - Starts DVD playback
        """
        logger.info("Facade: Setting up movie...")
        print("Facade: Setting up movie...")
        
        self.projector.turn_on()
        self.sound.set_volume(30)
        self.dvd.play()
        
        logger.info("Movie setup completed")
    
    def end_movie(self) -> None:
        """
        Shut down the home theater system after movie watching.
        
        This method coordinates all components to cleanly shut down:
        - Stops DVD playback
        - Turns off the projector
        - Turns off the sound system
        """
        logger.info("Facade: Shutting down...")
        print("Facade: Shutting down...")
        
        self.dvd.stop()
        self.projector.turn_off()
        self.sound.turn_off()
        
        logger.info("Home theater shutdown completed")