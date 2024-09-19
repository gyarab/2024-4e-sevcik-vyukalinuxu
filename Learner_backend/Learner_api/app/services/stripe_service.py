import stripe
import os

stripe.api_key = os.getenv("STRIPE_API_KEY")

__all__ = ['stripe']