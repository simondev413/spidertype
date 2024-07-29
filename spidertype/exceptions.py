class SpiderTypeError(Exception):
    def __init__(self,message):
        super().__init__(message)

class TypeValidationError(SpiderTypeError):
    """
    Excepetion raised when a type validation fail.
    """
    def __init__(self,message):
        super().__init__(message)

class RegistrationError(SpiderTypeError):
    """
    Exception raised when occur an error during type registation.
    """
    def __init__(self, message):
        super().__init__(message)

class TypeNotFoundError(SpiderTypeError):
    """
    Exception raised when a specific type is not found
    """
    def __init__(self, message):
        super().__init__(message)
    

class InvalidTypeError(SpiderTypeError):
    """
    Exception raised when an invalid type is used.
    """
    def __init__(self, message):
        super().__init__(message)