from abc import ABC, abstractmethod
from contextlib import ContextDecorator

# Strategy interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} with Credit Card")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} with PayPal")

class CryptoPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} with Cryptocurrency")

# Context
class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy
    
    def make_payment(self, amount):
        self._strategy.pay(amount)

context = PaymentContext(CreditCardPayment())
context.make_payment(20)

context.set_strategy(PayPalPayment())
context.make_payment(40)

context.set_strategy(CryptoPayment())
context.make_payment(100)