def generate_fake_number() -> str:
    """Generate a random fake phone number."""
    country_codes = ["+1", "+44", "+91", "+61", "+33", "+92", "+32", "+49", "+58"]
    country_code = random.choice(country_codes)
    number = ''.join(random.choices('0123456789', k=10))
    return f"{country_code}{number}"
