from functools import wraps
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

def validate_type(value,expected_type):        
    if not isinstance(value,expected_type):
        raise TypeValidationError(f"Expected type {expected_type.__name__}, got {type(value).__name__}.")
