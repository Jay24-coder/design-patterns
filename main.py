"""
Design Patterns Interactive Demo

This is the main entry point for the Design Patterns project.
It provides an interactive menu system to demonstrate various design patterns.
"""

import sys
from typing import Optional
from loguru import logger

# Configure logging
logger.remove()  # Remove default handler
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="INFO"
)

from examples.facade_example import run_facade_example
from examples.strategy_example import run_strategy_example


def display_menu() -> None:
    """Display the main menu options."""
    print("\n" + "="*60)
    print("           DESIGN PATTERNS INTERACTIVE DEMO")
    print("="*60)
    print("1. Facade Pattern - Home Theater System")
    print("2. Strategy Pattern - Payment System")
    print("3. Run All Examples")
    print("4. Exit")
    print("="*60)


def get_user_choice() -> Optional[int]:
    """
    Get user's menu choice.
    
    Returns:
        User's choice as integer, or None if invalid input
    """
    try:
        choice = input("\nEnter your choice (1-4): ").strip()
        return int(choice)
    except ValueError:
        logger.warning("Invalid input: Please enter a number")
        return None


def run_facade_demo() -> None:
    """Run the facade pattern demonstration."""
    logger.info("Starting Facade Pattern Demo")
    run_facade_example()


def run_strategy_demo() -> None:
    """Run the strategy pattern demonstration."""
    logger.info("Starting Strategy Pattern Demo")
    run_strategy_example()


def run_all_examples() -> None:
    """Run all available pattern examples."""
    logger.info("Running all pattern examples")
    run_facade_demo()
    run_strategy_demo()


def main() -> None:
    """Main application entry point."""
    logger.info("Design Patterns Demo Application Started")
    
    print("Welcome to the Design Patterns Interactive Demo!")
    print("This application demonstrates various design patterns with practical examples.")
    
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice is None:
            print("Please enter a valid number (1-4)")
            continue
        
        if choice == 1:
            run_facade_demo()
        elif choice == 2:
            run_strategy_demo()
        elif choice == 3:
            run_all_examples()
        elif choice == 4:
            logger.info("Application terminated by user")
            print("\nThank you for using the Design Patterns Demo!")
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
    
    logger.info("Design Patterns Demo Application Ended")


if __name__ == "__main__":
    main()