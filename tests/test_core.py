import os
import sys

for root, dirs, files in os.walk(os.path.dirname(os.path.abspath('..'))):
    for dir in dirs:
        sys.path.append(dir)


import pytest
from spidertype.core import SpiderTypeSystem
from spidertype.exceptions import TypeValidationError



@pytest.fixture
def type_system():
    system = SpiderTypeSystem()
    system.register_type('String',str)
    system.register_type('Integer',int)
    return system

def test_register_and_get_type(type_sytem):
    """
    Verify if the types are registered and retrieved propely.
    """
    assert type_system.get_type('String') == str
    assert type_system.get_type('Integer') == int

def test_validate_corret_type(type_system):
    """
    Test the validation of values with corret types.
    """
    type_system.validate('Hello','String')
    type_system.validate(123,'Integer')
