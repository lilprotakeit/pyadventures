"""
Abstract Class in Python
--------------------------
In Python, an abstract class acts as a blueprint or template for other classes.
It defines a common interface—a mandatory set of methods—that any subclass must
implement, ensuring consistency across different parts of your application.
"""

from abc import ABC, abstractmethod


# abstract class
class Payment_Processor(ABC):
    @abstractmethod  # This decorator indicates that the method is abstract and must be implemented by any subclass.
    def process_payment(self, amount: float) -> bool:
        """process a payment of given amount"""
        pass

    @abstractmethod  # This decorator indicates that the method is abstract and must be implemented by any subclass.
    def refund_payment(self, transaction_id: str) -> bool:
        """refund a payment of given amount"""
        pass

    # if a subclass does not implement all the abstract methods, it will also be considered an abstract class and cannot be instantiated.


class StripePaymentProcessor(Payment_Processor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing payment of {amount} through Stripe")
        return True

    def refund_payment(self, transaction_id: str) -> bool:
        print(f"Refunding payment with transaction ID {transaction_id} through Stripe")
        return True


class PayPalPaymentProcessor(Payment_Processor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing payment of {amount} through PayPal")
        return True

    def refund_payment(self, transaction_id: str) -> bool:
        print(f"Refunding payment with transaction ID {transaction_id} through PayPal")
        return True


def main():
    stripe_processor = StripePaymentProcessor()
    paypal_processor = PayPalPaymentProcessor()

    stripe_processor.process_payment(100.0)
    stripe_processor.refund_payment("txn_12345")
    paypal_processor.process_payment(200.0)
    paypal_processor.refund_payment("txn_67890")


if __name__ == "__main__":
    main()
