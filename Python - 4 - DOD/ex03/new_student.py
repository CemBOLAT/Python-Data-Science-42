import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    """
    Generate a random id

    Returns:
        str: a random id
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))

@dataclass(order=True)
class Student:
    """
    Student class

    Args:
        name (str): student's name
        surname (str): student's surname
        id (str): student's id (automatically generated)
        login (str): student's login (automatically generated)
        active (bool): student's status
    
    All logic on fields.

    Field Parameters:
        - default (Any): A default value for the field.
        - default_factory (callable): A factory function that generates a default value for the field.
        - init (bool): If False, the field will not be included as a parameter to the generated __init__ method (default is True).
        - repr (bool): If False, the field will not be included in the __repr__ output (default is True).
        - compare (bool): If False, the field will not be used in comparison operations (default is True).
        - hash (bool | None): If False, the field will not be included in hash calculations; if None, it takes the value of compare.
    """
    name: str = field(init=True)
    surname: str = field(init=True)
    id: str = field(init=False, default_factory=generate_id)
    login: str = field(init=False)
    active: bool = field(default=True)

    def __post_init__(self):
        self.login = self.name[0].upper() + self.surname.lower()
