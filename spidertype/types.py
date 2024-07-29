from functools import wraps
from .validation import validate_type
from .exceptions import TypeValidationError



def static_type_check(func):
    """
    This decorator verify the args´s type of a function in execution time using annotations of type. 
    """
    annotations = func.__annotations__

    @wraps
    def wrapper(*args,**kwargs):
        for arg_name,arg_value in kwargs.items():
            if arg_name in annotations:
                expeted_type =  annotations[arg_name]
                validate_type(arg_value,expeted_type)

        for i,(arg_value,(arg_name,expeted_type)) in enumerate(zip(args,annotations.items())):
            if i == 0 and arg_name == 'self':
                continue
            validate_type(arg_value,expeted_type)

        return func(*args,**kwargs)

    return wrapper

class StaticTyped:
    """
    This class allows to create static typed classes    
    """
    def __init_subclass__(cls,**kwargs):
        super().__init_subclass__(*kwargs)
        for name, method in cls.__dict__.items():
            if callable(method) and hasattr(method,'__annotations__'):
                setattr(cls,name,static_type_check(method))