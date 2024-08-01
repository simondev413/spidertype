Usage
=====

To use SpiderType, first install it using pip:

.. code-block:: shell

   pip install spider_type

Here is a basic example of how to use the library:

.. code-block:: python

   from spider_type import SpiderTypeMap, Type

   # Define a custom type
   class PositiveInteger(Type):
       def validate(self, value):
           if not isinstance(value, int) or value <= 0:
               raise TypeValidationError("Must be a positive integer.")

   # Register the custom type
   type_map = SpiderTypeMap()
   type_map.register_type('PositiveInteger', PositiveInteger('PositiveInteger'))

   # Validate a value
   type_map.validate(10, 'PositiveInteger')  # No exception
   type_map.validate(-5, 'PositiveInteger')  # Raises TypeValidationError
