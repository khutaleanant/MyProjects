from abc import ABC, abstractmethod

# Abstract Base Class for Payment Methods
class PaymentMethod(ABC):

    @abstractmethod
    def process_payment(self, amount: float):
        pass


# Concrete class for Credit Card Payment
class CreditCardPayment(PaymentMethod):
    
    def process_payment(self, amount: float):
        print(f"Processing credit card payment of ${amount:.2f}.")


# Concrete class for PayPal Payment
class PayPalPayment(PaymentMethod):
    
    def process_payment(self, amount: float):
        print(f"Processing PayPal payment of ${amount:.2f}.")


# Example usage1
payments = [CreditCardPayment(), PayPalPayment()]

for payment in payments:
    payment.process_payment(100.26)
    
# Example usage regular
PayPalPayment1=CreditCardPayment()
PayPalPayment2=PayPalPayment()
PayPalPayment2.process_payment(2000)
PayPalPayment1.process_payment(1000)
