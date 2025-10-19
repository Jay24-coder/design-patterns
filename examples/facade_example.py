"""
Facade Pattern Example

This example demonstrates the Facade pattern with a home theater system.
The facade provides a simplified interface to coordinate multiple complex subsystems.
"""

from pattern.facade_pattern import DVDPlayer, Projector, SoundSystem, HomeTheatreFacade


def run_facade_example():
    """Run the facade pattern demonstration."""
    print("=== Facade Pattern Example: Home Theater System ===\n")
    
    # Create system components
    dvd = DVDPlayer()
    projector = Projector()
    sound = SoundSystem()
    
    # Create facade to coordinate all components
    theatre = HomeTheatreFacade(dvd=dvd, projector=projector, sound=sound)
    
    # Use the facade for simplified control
    print("Starting movie experience...")
    theatre.watch_movie()
    
    print("\nEnding movie experience...")
    theatre.end_movie()
    
    print("\n=== Facade Pattern Example Complete ===\n")


if __name__ == "__main__":
    run_facade_example()
