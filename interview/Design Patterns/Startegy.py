"""
Use Case: Payment Processing System

In an e-commerce application, you might want to process payments using different strategies like credit card, PayPal, or Bitcoin.

why use payment context? 

there are other things that are related to payment
Single Responsibility: The PaymentContext class encapsulates the logic for selecting and switching between different payment strategies, adhering to the single responsibility principle. This keeps the payment processing logic separate from the rest of the application.
Centralized Management: All payment-related operations (payment, refund, logging, state management) are managed in one place, making the codebase easier to maintain and extend.
Reusability: Common operations like logging, state management, and auditing can be implemented once in the context class and reused across different strategies.
Maintainability: Changes to payment processing logic, logging, or state management can be made in the PaymentContext without altering the individual strategy implementations.
"""

class PaymentStrategy:
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid {amount} using Credit Card"

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid {amount} using PayPal"

class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid {amount} using Bitcoin"

class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def execute_payment(self, amount):
        return self._strategy.pay(amount)

# Usage
context = PaymentContext(CreditCardPayment())
print(context.execute_payment(100))  # Output: Paid 100 using Credit Card

context = PaymentContext(PayPalPayment())
print(context.execute_payment(200))  # Output: Paid 200 using PayPal
