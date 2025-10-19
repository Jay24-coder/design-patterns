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
└── pattern/           # Design pattern implementations
    ├── facade_pattern.py    # Facade pattern implementation
    └── strategy_pattern.py  # Strategy pattern implementation
```

## Design Patterns Implemented

### 1. Facade Pattern

**File:** `pattern/facade_pattern.py`

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

### 2. Strategy Pattern

**File:** `pattern/strategy_pattern.py`

The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. This implementation demonstrates a payment system where different payment methods can be selected at runtime.

#### Key Components:
- **PaymentStrategy**: Abstract base class defining the payment interface
- **CreditCardPayment**: Concrete strategy for credit card payments
- **PayPalPayment**: Concrete strategy for PayPal payments
- **CryptoPayment**: Concrete strategy for cryptocurrency payments
- **PaymentContext**: Context class that uses a payment strategy

#### Usage Example:
```python
# Create payment context with credit card strategy
context = PaymentContext(CreditCardPayment())
context.make_payment(20)  # Pay $20 with credit card

# Switch to PayPal strategy
context.set_strategy(PayPalPayment())
context.make_payment(40)  # Pay $40 with PayPal

# Switch to crypto strategy
context.set_strategy(CryptoPayment())
context.make_payment(100)  # Pay $100 with cryptocurrency
```

#### Benefits:
- **Runtime Flexibility**: Can change algorithms at runtime
- **Open/Closed Principle**: Easy to add new payment methods without modifying existing code
- **Single Responsibility**: Each strategy handles one payment method
- **Eliminates Conditional Logic**: No need for if/else chains to select payment methods

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
python pattern/facade_pattern.py

# Run the strategy pattern example
python pattern/strategy_pattern.py
```

## Running the Examples

### Facade Pattern Example
```bash
python pattern/facade_pattern.py
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

### Strategy Pattern Example
```bash
python pattern/strategy_pattern.py
```

Expected output:
```
Paying 20 with Credit Card
Paying 40 with PayPal
Paying 100 with Cryptocurrency
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
