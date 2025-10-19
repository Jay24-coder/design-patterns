# Design Patterns

A Python project demonstrating various design patterns with practical implementations.

## Overview

This repository contains implementations of common design patterns in Python, showcasing how these patterns can be used to solve real-world programming problems and improve code organization, maintainability, and reusability.

## Project Structure

```
Design Patterns/
├── README.md           # This file
├── pyproject.toml      # Project configuration
├── main.py            # Main entry point
└── facade_pattern.py  # Facade pattern implementation
```

## Design Patterns Implemented

### 1. Facade Pattern

**File:** `facade_pattern.py`

The Facade pattern provides a simplified interface to a complex subsystem. In this implementation, we demonstrate a home theater system where multiple components (DVD player, projector, sound system) are coordinated through a single facade interface.

#### Key Components:
- **DVDPlayer**: Handles movie playback operations
- **Projector**: Manages projector on/off functionality  
- **SoundSystem**: Controls volume and system power
- **HomeTheatreFacade**: Provides a unified interface to coordinate all components

#### Usage Example:
```python
# Create system components
dvd = DVDPlayer()
projector = Projector()
sound = SoundSystem()

# Use the facade for simplified control
theatre = HomeTheatreFacade(dvd=dvd, projector=projector, sound=sound)
theatre.watchMovie()  # Automatically coordinates all components
theatre.endMovie()    # Cleanly shuts down all components
```

#### Benefits:
- **Simplified Interface**: Clients only need to interact with the facade
- **Decoupling**: Reduces dependencies between client code and subsystem
- **Easier Maintenance**: Changes to subsystem don't affect client code

## Requirements

- Python 3.12 or higher
- No external dependencies required

## Getting Started

1. Clone or download this repository
2. Navigate to the project directory
3. Run the examples:

```bash
# Run the main entry point
python main.py

# Run the facade pattern example
python facade_pattern.py
```

## Running the Examples

### Facade Pattern Example
```bash
python facade_pattern.py
```

Expected output:
```
Facade: Setting up movie...
Turning on the projector
Sound System: Volume set to 30
DVD Player: Playing movie

Facade: Shutting down...
DVD Player: Stopped
Turning off the projector
Turning off the sound system
```

## Contributing

This project is designed for educational purposes. Feel free to:
- Add new design pattern implementations
- Improve existing examples
- Add more comprehensive documentation
- Suggest additional patterns to implement

## Design Patterns to Implement

Future implementations may include:
- Singleton Pattern
- Observer Pattern
- Strategy Pattern
- Factory Pattern
- Builder Pattern
- Command Pattern
- Adapter Pattern
- Decorator Pattern
