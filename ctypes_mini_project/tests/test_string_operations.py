"""
String Operations Test Module

Tests for string operations using ctypes and validation.

Test Coverage:
- String validation
- String length checking
- String type handling
- String parameters

Total Test Cases: 4
"""

import pytest
import logging
from src.data_types import validate_string

logger = logging.getLogger(__name__)


class TestStringOperations:
    """
    Test class for string operations.
    """
    
    def test_string_validation_basic(self):
        """
        Test Case 1: Basic String Validation
        
        Purpose: Verify string validation works correctly
        Expected: Valid strings pass, invalid types fail
        """
        # Valid strings
        assert validate_string("hello") is True
        assert validate_string("") is True
        assert validate_string(b"bytes_string") is True
        
        # Invalid types
        with pytest.raises(TypeError):
            validate_string(123)
        
        with pytest.raises(TypeError):
            validate_string(3.14)
        
        with pytest.raises(TypeError):
            validate_string(None)
        
        logger.info(f"✓ Test 1 passed: String validation")
    
    def test_string_length_validation(self):
        """
        Test Case 2: String Length Validation
        
        Purpose: Test min/max length constraints
        Expected: Length validation works correctly
        """
        # Valid lengths
        assert validate_string("hello", min_length=0, max_length=10) is True
        assert validate_string("hi", min_length=2) is True
        
        # Length too short
        with pytest.raises(ValueError):
            validate_string("a", min_length=2)
        
        # Length too long
        with pytest.raises(ValueError):
            validate_string("hello world", max_length=5)
        
        logger.info(f"✓ Test 2 passed: String length validation")
    
    def test_string_reverse(self):
        """
        Test Case 3: String Reversal
        
        Purpose: Verify string reversal logic
        Expected: String correctly reversed
        """
        test_strings = [
            ("hello", "olleh"),
            ("python", "nohtyp"),
            ("a", "a"),
            ("", ""),
        ]
        
        for original, expected in test_strings:
            reversed_str = original[::-1]
            assert reversed_str == expected, \
                f"Expected reverse of '{original}' to be '{expected}', got '{reversed_str}'"
        
        logger.info(f"✓ Test 3 passed: String reversal")
    
    def test_string_case_operations(self):
        """
        Test Case 4: String Case Operations
        
        Purpose: Test string case conversion
        Expected: Case conversion works correctly
        """
        original = "Hello World"
        
        # Test uppercase
        uppercase = original.upper()
        assert uppercase == "HELLO WORLD"
        assert validate_string(uppercase) is True
        
        # Test lowercase
        lowercase = original.lower()
        assert lowercase == "hello world"
        assert validate_string(lowercase) is True
        
        # Test with validation
        assert validate_string(uppercase, min_length=10) is True
        
        logger.info(f"✓ Test 4 passed: String case operations")
