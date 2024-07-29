from .validation import static_type_check
from .exceptions import TypeValidationError


class StaticTyped:
    """
    This class allows to create static typed classes    
    """
    def __init_subclass__(cls,**kwargs):
        super().__init_subclass__(*kwargs)
        for name, method in cls.__dict__.items():
            if callable(method) and hasattr(method,'__annotations__'):
                setattr(cls,name,static_type_check(method))


class Type:
    def __init__(self,name):
        self.name = name

    def validate(self,value):
        if not isinstance(value,self.__class__):
            raise TypeValidationError(f"Expected type {self.__class__.__name__.lower()}, got {type(value).__name__}.")
            
    
    def __str__(self):
        return self.name

