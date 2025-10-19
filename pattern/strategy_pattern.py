"""
Strategy Pattern Implementation

The Strategy pattern defines a family of algorithms, encapsulates each one, 
and makes them interchangeable. This implementation demonstrates a payment 
system where different payment methods can be selected at runtime.
"""

from abc import ABC, abstractmethod
from typing import Union
from loguru import logger


class PaymentStrategy(ABC):
    """
    Abstract base class defining the interface for payment strategies.
    
    All concrete payment strategies must implement the pay method.
    """
    
    @abstractmethod
    def pay(self, amount: Union[int, float]) -> None:
        """
        Process a payment with the given amount.
        
        Args:
            amount: The amount to be paid
        """
        pass


class CreditCardPayment(PaymentStrategy):
    """Concrete strategy for credit card payments."""
    
    def __init__(self) -> None:
        """Initialize the credit card payment strategy."""
        logger.info("Credit Card payment strategy initialized")
    
    def pay(self, amount: Union[int, float]) -> None:
        """
        Process a credit card payment.
        
        Args:
            amount: The amount to be paid
        """
        logger.info(f"Processing credit card payment for ${amount}")
        print(f"Paying {amount} with Credit Card")


class PayPalPayment(PaymentStrategy):
    """Concrete strategy for PayPal payments."""
    
    def __init__(self) -> None:
        """Initialize the PayPal payment strategy."""
        logger.info("PayPal payment strategy initialized")
    
    def pay(self, amount: Union[int, float]) -> None:
        """
        Process a PayPal payment.
        
        Args:
            amount: The amount to be paid
        """
        logger.info(f"Processing PayPal payment for ${amount}")
        print(f"Paying {amount} with PayPal")


class CryptoPayment(PaymentStrategy):
    """Concrete strategy for cryptocurrency payments."""
    
    def __init__(self) -> None:
        """Initialize the cryptocurrency payment strategy."""
        logger.info("Cryptocurrency payment strategy initialized")
    
    def pay(self, amount: Union[int, float]) -> None:
        """
        Process a cryptocurrency payment.
        
        Args:
            amount: The amount to be paid
        """
        logger.info(f"Processing cryptocurrency payment for ${amount}")
        print(f"Paying {amount} with Cryptocurrency")


class PaymentContext:
    """
    Context class that uses a payment strategy to process payments.
    
    The context maintains a reference to a strategy object and delegates
    payment processing to the current strategy.
    """
    
    def __init__(self, strategy: PaymentStrategy) -> None:
        """
        Initialize the payment context with a strategy.
        
        Args:
            strategy: The initial payment strategy to use
        """
        self._strategy = strategy
        logger.info(f"Payment context initialized with {strategy.__class__.__name__}")
    
    def set_strategy(self, strategy: PaymentStrategy) -> None:
        """
        Change the payment strategy at runtime.
        
        Args:
            strategy: The new payment strategy to use
        """
        old_strategy = self._strategy.__class__.__name__
        self._strategy = strategy
        logger.info(f"Payment strategy changed from {old_strategy} to {strategy.__class__.__name__}")
    
    def make_payment(self, amount: Union[int, float]) -> None:
        """
        Process a payment using the current strategy.
        
        Args:
            amount: The amount to be paid
        """
        if amount <= 0:
            logger.warning(f"Invalid payment amount: {amount}")
            raise ValueError("Payment amount must be positive")
        
        logger.info(f"Making payment of ${amount} using {self._strategy.__class__.__name__}")
        self._strategy.pay(amount)