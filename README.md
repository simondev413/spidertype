# SpiderType

SpiderType is a Python library designed for handling and managing data types with static typing, inspired by TypeScript. This library provides a foundation for creating and registering custom types, validating values against these types, and applying static type checks to class methods.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Registering Types](#registering-types)
  - [Retrieving Types](#retrieving-types)
  - [Validating Types](#validating-types)
  - [Static Type Checking](#static-type-checking)
- [Exceptions](#exceptions)
- [Classes and Methods](#classes-and-methods)

## Installation

Clone the GitHub repository and install the requirements:

```bash
git clone https://github.com/simondev413/spidertype.git
cd spidertype
pip install -r requirements.txt
```

## Usage

### Registering Types

To register a new custom type, use the `register_type` method of the `SpiderTypeMap` class:

```python
from spidertype.core import SpiderTypeMap
from spidertype.types import Type

class MyCustomType(Type):
    def validate(self, value):
        # Custom validation logic
        pass

type_map = SpiderTypeMap()
my_type = MyCustomType('CustomType')
type_map.register_type('CustomType', my_type)
```

### Retrieving Types

To retrieve a registered type, use the `get_type` method of the `SpiderTypeMap` class:

```python
retrieved_type = type_map.get_type('CustomType')
```

### Validating Types

To validate a value against an expected type, use the `validate` method of the `SpiderTypeMap` class:

```python
try:
    type_map.validate(value_to_validate, 'CustomType')
except TypeValidationError as e:
    print(e)
```

### Static Type Checking

To apply static type checking to class methods, use the `static_type_check` decorator:

```python
from spidertype.validation import static_type_check

class MyClass:
    @static_type_check
    def my_method(self, param: CustomType):
        pass
```

## Exceptions

The SpiderType library defines several exceptions for different errors:

- `SpiderTypeError`: Base exception for all errors in the SpiderType library.
- `TypeValidationError`: Exception raised when type validation fails.
- `RegistrationError`: Exception raised when an error occurs during type registration.
- `TypeNotFoundError`: Exception raised when a specified type is not found.
- `InvalidTypeError`: Exception raised when an invalid type is used.

## Classes and Methods

### SpiderTypeMap

- `register_type(name, type_def)`: Registers a new custom type.
- `get_type(name)`: Retrieves a registered custom type.
- `validate(value, type_name)`: Validates a value against an expected type.

### SpiderTypeError

- Base exception for all errors in the SpiderType library.

### TypeValidationError

- Exception raised when type validation fails.

### RegistrationError

- Exception raised when an error occurs during type registration.

### TypeNotFoundError

- Exception raised when a specified type is not found.

### InvalidTypeError

- Exception raised when an invalid type is used.

### StaticTyped

- Base class for custom static typed classes.

### Type

- `validate(value)`: Validates a value against the custom type.

### static_type_check

- Decorator to apply static type checking to class methods.

### validate_type

- Function to validate a value against an expected type.

---

For more details, refer to the full library documentation.
