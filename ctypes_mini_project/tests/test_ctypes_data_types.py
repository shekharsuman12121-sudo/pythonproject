"""
CTypes Data Types Test Module

Tests for ctypes data structures and custom types.

Test Coverage:
- Point structure (2D coordinates)
- Rectangle structure (dimensions)
- Person structure (record)
- Type validation
- Structure methods

Total Test Cases: 5
"""

import pytest
import logging
from ctypes import c_int, c_float, c_char_p
from src.data_types import Point, Rectangle, Person, validate_integer, validate_float, validate_string

logger = logging.getLogger(__name__)


class TestCTypesDataTypes:
    """
    Test class for ctypes data types and structures.
    """
    
    def test_point_structure_creation(self, test_point):
        """
        Test Case 1: Point Structure Creation
        
        Purpose: Verify Point structure initialization and attributes
        Expected: Point created with correct x, y coordinates
        """
        assert test_point.x == 3, f"Expected x=3, got {test_point.x}"
        assert test_point.y == 4, f"Expected y=4, got {test_point.y}"
        
        # Test string representation
        point_str = str(test_point)
        assert "3" in point_str and "4" in point_str
        
        logger.info(f"✓ Test 1 passed: Point structure {test_point}")
    
    def test_point_distance_calculation(self, test_point):
        """
        Test Case 2: Point Distance from Origin
        
        Purpose: Test Point.distance_from_origin() method
        Input: Point(3, 4)
        Expected: distance = 5.0 (3-4-5 triangle)
        """
        distance = test_point.distance_from_origin()
        
        # 3-4-5 right triangle
        assert distance == 5.0, f"Expected 5.0, got {distance}"
        
        logger.info(f"✓ Test 2 passed: Point distance = {distance}")
    
    def test_rectangle_structure_creation(self, test_rectangle):
        """
        Test Case 3: Rectangle Structure Creation and Methods
        
        Purpose: Verify Rectangle structure and calculation methods
        Input: Rectangle(width=5.0, height=10.0)
        Expected: Area=50.0, Perimeter=30.0
        """
        # Test attributes
        assert test_rectangle.width == 5.0
        assert test_rectangle.height == 10.0
        assert test_rectangle.x == 0
        assert test_rectangle.y == 0
        
        # Test area calculation
        area = test_rectangle.area()
        assert area == 50.0, f"Expected area 50.0, got {area}"
        
        # Test perimeter calculation
        perimeter = test_rectangle.perimeter()
        assert perimeter == 30.0, f"Expected perimeter 30.0, got {perimeter}"
        
        logger.info(f"✓ Test 3 passed: Rectangle area={area}, perimeter={perimeter}")
    
    def test_person_structure_creation(self, test_person):
        """
        Test Case 4: Person Structure Creation
        
        Purpose: Verify Person structure with string handling
        Input: Person(name=b'John Doe', age=30, height=5.9)
        Expected: Correct attributes and string conversion
        """
        # Test attributes
        assert test_person.age == 30, f"Expected age 30, got {test_person.age}"
        assert test_person.height == 5.9, f"Expected height 5.9, got {test_person.height}"
        
        # Test name (bytes vs string)
        assert test_person.name == b"John Doe"
        
        # Test string representation
        person_str = str(test_person)
        assert "John" in person_str or "john" in person_str.lower()
        
        logger.info(f"✓ Test 4 passed: Person structure {test_person}")
    
    def test_integer_validation(self):
        """
        Test Case 5: Integer Type Validation
        
        Purpose: Test validate_integer function with range checking
        Expected: Proper validation with error handling
        """
        # Valid integer
        assert validate_integer(42) is True
        assert validate_integer(0) is True
        assert validate_integer(-10) is True
        
        # Invalid type
        with pytest.raises(TypeError):
            validate_integer("42")
        
        with pytest.raises(TypeError):
            validate_integer(3.14)
        
        # Range validation
        assert validate_integer(50, min_val=0, max_val=100) is True
        
        with pytest.raises(ValueError):
            validate_integer(150, min_val=0, max_val=100)
        
        with pytest.raises(ValueError):
            validate_integer(-5, min_val=0, max_val=100)
        
        logger.info(f"✓ Test 5 passed: Integer validation")
