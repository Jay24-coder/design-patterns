"""
Strategy Pattern Example

This example demonstrates the Strategy pattern with a payment system.
Different payment methods can be selected and used at runtime.
"""

from pattern.strategy_pattern import (
    PaymentContext, 
    CreditCardPayment, 
    PayPalPayment, 
    CryptoPayment
)


def run_strategy_example():
    """Run the strategy pattern demonstration."""
    print("=== Strategy Pattern Example: Payment System ===\n")
    
    # Create payment context with credit card strategy
    context = PaymentContext(CreditCardPayment())
    
    print("Processing payments with different strategies:")
    print("-" * 50)
    
    # Pay with credit card
    context.make_payment(20)
    
    # Switch to PayPal strategy
    context.set_strategy(PayPalPayment())
    context.make_payment(40)
    
    # Switch to crypto strategy
    context.set_strategy(CryptoPayment())
    context.make_payment(100)
    
    print("\n=== Strategy Pattern Example Complete ===\n")


if __name__ == "__main__":
    run_strategy_example()
