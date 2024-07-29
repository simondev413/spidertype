from .validation import static_type_check,validate_type
from .exceptions import TypeValidationError


class StaticTyped:
    """
    Base class for custom static typed classes.
    """
    def __init_subclass__(cls,**kwargs):
        super().__init_subclass__(*kwargs)
        for name, method in cls.__dict__.items():
            if callable(method) and hasattr(method,'__annotations__'):
                setattr(cls,name,static_type_check(method))


class Type:
    """
    Base class for custom type.

    Args:
        name (str): Name of the custom type.
    """
    def __init__(self,name):
        """
        Initialize a new instance of the type.
        """
        self.name = name

    def validate(self,value):
       """
       Validates a value against the custom type.

       Args:
            value: Value to be validated.
       """
       return validate_type(value,self.__class__)
    
    def __str__(self):
        return self.name

