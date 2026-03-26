def receive_otp(phone_number: str) -> str | None:
    """Receive OTP for the given phone number."""
    # In a real implementation, you would connect to a service that can receive OTPs
    # This is a simple example that just returns a random 6-digit number
    return ''.join(random.choices('0123456789', k=6))
