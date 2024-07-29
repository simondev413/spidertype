from .validation import validate_type
from .exceptions import TypeValidationError,RegistrationError, TypeNotFoundError


class SpiderTypeMap:
    def __init__(self):
        self.types = {}

    
    def register_type(self,name,type_def):
        """
        Registers a new custom type.

        Args:
            name (str): Name of the type.
            type_def (SpiderType): Instance of the custom type.
        """
        try:
            if name in self.types:
                raise RegistrationError(f"Type {name} is already registered.")
            self.types[name] = type_def
        except RegistrationError:
            raise RegistrationError(f"Type don´t was registered.")

    def get_type(self,name):
        """ 
        Retrieves a registered custom type by name.

        Args:
            name (str): Name of the custom type.

        Return:
            SpiderType: Instance os the custom type.
        """
        try:
            return self.types.get(name)
        except TypeNotFoundError:
            raise TypeNotFoundError(f"Type not found: {name}")


    def validate(self,value,type_name):
        """
        Validate a value against an expected type.

        Args:
            value: Value to be validated.
            type_name (SpiderType): Expected type to validate against. 
        """
        type_def = self.get_type(type_name)
        if not type_def:
            raise TypeValidationError(f"Type {type_name} is not registered.")
        validate_type(value,type_def)