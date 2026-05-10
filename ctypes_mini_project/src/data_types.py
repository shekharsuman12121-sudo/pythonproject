"""
Custom Data Types and Structures Module

Defines custom ctypes data structures and type validators for use with C libraries.

Structures:
- Point: 2D coordinate (x, y)
- Rectangle: Rectangle with dimensions (width, height, x, y)
- Person: Person record (name, age, height)

Validators:
- validate_integer: Validate integer input
- validate_float: Validate float input
- validate_string: Validate string input
"""

from ctypes import Structure, c_int, c_float, c_char_p, c_bool, POINTER
import logging

# Logger setup
logger = logging.getLogger(__name__)


class Point(Structure):
    """
    2D Point structure mapping to C struct.
    
    C equivalent:
        struct Point {
            int x;
            int y;
        };
    """
    _fields_ = [
        ('x', c_int),
        ('y', c_int),
    ]
    
    def __repr__(self) -> str:
        """
        String representation of Point.
        
        Returns:
            String representation
        """
        return f"Point(x={self.x}, y={self.y})"
    
    def distance_from_origin(self) -> float:
        """
        Calculate distance from origin (0, 0).
        
        Returns:
            Distance value
        """
        return (self.x ** 2 + self.y ** 2) ** 0.5


class Rectangle(Structure):
    """
    Rectangle structure mapping to C struct.
    
    C equivalent:
        struct Rectangle {
            float width;
            float height;
            int x;
            int y;
        };
    """
    _fields_ = [
        ('width', c_float),
        ('height', c_float),
        ('x', c_int),
        ('y', c_int),
    ]
    
    def __repr__(self) -> str:
        """
        String representation of Rectangle.
        
        Returns:
            String representation
        """
        return (f"Rectangle(width={self.width}, height={self.height}, "
                f"x={self.x}, y={self.y})")
    
    def area(self) -> float:
        """
        Calculate area of rectangle.
        
        Returns:
            Area value
        """
        return self.width * self.height
    
    def perimeter(self) -> float:
        """
        Calculate perimeter of rectangle.
        
        Returns:
            Perimeter value
        """
        return 2 * (self.width + self.height)


class Person(Structure):
    """
    Person record structure mapping to C struct.
    
    C equivalent:
        struct Person {
            char *name;
            int age;
            float height;
        };
    """
    _fields_ = [
        ('name', c_char_p),
        ('age', c_int),
        ('height', c_float),
    ]
    
    def __repr__(self) -> str:
        """
        String representation of Person.
        
        Returns:
            String representation
        """
        name = self.name.decode('utf-8') if isinstance(self.name, bytes) else self.name
        return f"Person(name={name}, age={self.age}, height={self.height})"


def validate_integer(value: any, min_val: int = None, max_val: int = None) -> bool:
    """
    Validate integer input with optional range checking.
    
    Args:
        value: Value to validate
        min_val: Minimum allowed value (inclusive)
        max_val: Maximum allowed value (inclusive)
    
    Returns:
        True if valid, False otherwise
    
    Raises:
        TypeError: If value is not an integer
        ValueError: If value is out of range
    """
    if not isinstance(value, int):
        raise TypeError(f"Expected integer, got {type(value).__name__}")
    
    if min_val is not None and value < min_val:
        raise ValueError(f"Value {value} is less than minimum {min_val}")
    
    if max_val is not None and value > max_val:
        raise ValueError(f"Value {value} is greater than maximum {max_val}")
    
    return True


def validate_float(value: any, min_val: float = None, max_val: float = None) -> bool:
    """
    Validate float input with optional range checking.
    
    Args:
        value: Value to validate
        min_val: Minimum allowed value (inclusive)
        max_val: Maximum allowed value (inclusive)
    
    Returns:
        True if valid, False otherwise
    
    Raises:
        TypeError: If value is not numeric
        ValueError: If value is out of range
    """
    if not isinstance(value, (int, float)):
        raise TypeError(f"Expected numeric, got {type(value).__name__}")
    
    value = float(value)
    
    if min_val is not None and value < min_val:
        raise ValueError(f"Value {value} is less than minimum {min_val}")
    
    if max_val is not None and value > max_val:
        raise ValueError(f"Value {value} is greater than maximum {max_val}")
    
    return True


def validate_string(value: any, min_length: int = 0, max_length: int = None) -> bool:
    """
    Validate string input with optional length checking.
    
    Args:
        value: Value to validate
        min_length: Minimum string length (inclusive)
        max_length: Maximum string length (inclusive)
    
    Returns:
        True if valid, False otherwise
    
    Raises:
        TypeError: If value is not a string
        ValueError: If length is out of range
    """
    if not isinstance(value, (str, bytes)):
        raise TypeError(f"Expected string, got {type(value).__name__}")
    
    if isinstance(value, bytes):
        value = value.decode('utf-8')
    
    if len(value) < min_length:
        raise ValueError(f"String length {len(value)} is less than minimum {min_length}")
    
    if max_length is not None and len(value) > max_length:
        raise ValueError(f"String length {len(value)} is greater than maximum {max_length}")
    
    return True
