class InvalidEmailError(Exception):
    """Raised when an email address does not meet the expected format."""


class InvalidDurationError(Exception):
    """Raised when an internship duration is missing or invalid."""


def validate_intern(email, duration):
    if "@" not in email or "." not in email:
        raise InvalidEmailError("Enter a valid email address.")

    if int(duration) <= 0:
        raise InvalidDurationError("Duration must be greater than zero months.")

    return True
