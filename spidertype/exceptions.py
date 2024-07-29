class SpiderTypeError(Exception):
    """
    Base exception for all erros in the SpiderType Library.
    """
    def __init__(self,message):
        super().__init__(message)

class TypeValidationError(SpiderTypeError):
    """
    Excepetion raised when a type validation fails.
    """
    def __init__(self,message):
        super().__init__(message)

class RegistrationError(SpiderTypeError):
    """
    Exception raised when an error occurs during type registration.
    """
    def __init__(self, message):
        super().__init__(message)

class TypeNotFoundError(SpiderTypeError):
    """
    Exception raised when a specified type is not found.
    """
    def __init__(self, message):
        super().__init__(message)
    

class InvalidTypeError(SpiderTypeError):
    """
    Exception raised when an invalid type is used.
    """
    def __init__(self, message):
        super().__init__(message)