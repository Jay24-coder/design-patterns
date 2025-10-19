"""
Design Patterns Package

This package contains implementations of various design patterns in Python.
Each pattern is implemented with proper documentation, type hints, and logging.
"""

from .facade_pattern import (
    DVDPlayer,
    Projector, 
    SoundSystem,
    HomeTheatreFacade
)

from .strategy_pattern import (
    PaymentStrategy,
    CreditCardPayment,
    PayPalPayment,
    CryptoPayment,
    PaymentContext
)

__all__ = [
    # Facade Pattern
    'DVDPlayer',
    'Projector',
    'SoundSystem', 
    'HomeTheatreFacade',
    
    # Strategy Pattern
    'PaymentStrategy',
    'CreditCardPayment',
    'PayPalPayment',
    'CryptoPayment',
    'PaymentContext'
]

__version__ = "1.0.0"
