from .validation import validate_type
from .exceptions import TypeValidationError,RegistrationError, TypeNotFoundError


class SpiderTypeSystem:
    def __init__(self):
        self.types = {}

    
    def register_type(self,name,type_def):
        """
        This method allows to register a new type.
        """
        try:
            if name in self.types:
                raise RegistrationError(f"Type {name} is already registered.")
            self.types[name] = type_def
        except RegistrationError:
            raise RegistrationError(f"Type don´t was registered.")

    def get_type(self,name):
        """ 
        This method return the type definitions of registered types.
        """
        try:
            return self.types.get(name)
        except TypeNotFoundError:
            raise TypeNotFoundError(f"Type not found: {name}")


    def validate(self,value,type_name):
        """
        This method verify if a value match with the type registered.
        """
        type_def = self.get_type(type_name)
        if not type_def:
            raise TypeValidationError(f"Type {type_name} is not registered.")
        validate_type(value,type_def)