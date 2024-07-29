from .exceptions import TypeValidationError

def validate_type(value,expected_type):
    if not isinstance(value,expected_type):
        raise TypeValidationError(f"Expected type {expected_type.__name__}, got {type(value).__name__}.")