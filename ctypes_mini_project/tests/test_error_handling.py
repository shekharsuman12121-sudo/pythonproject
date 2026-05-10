"""
Error Handling Test Module

Tests for error handling and edge cases.

Test Coverage:
- Division by zero
- Invalid function calls
- Type mismatch errors
- Error recovery

Total Test Cases: 3
"""

import pytest
import logging
from src.calculator import Calculator
from src.c_library_wrapper import MockMathLibrary

logger = logging.getLogger(__name__)


class TestErrorHandling:
    """
    Test class for error handling and edge cases.
    """
    
    def test_divide_by_zero_error(self, calculator):
        """
        Test Case 1: Division by Zero Error
        
        Purpose: Verify proper handling of division by zero
        Expected: ValueError raised with appropriate message
        """
        with pytest.raises(ValueError) as exc_info:
            calculator.divide(10, 0)
        
        assert "Cannot divide by zero" in str(exc_info.value)
        
        logger.info(f"✓ Test 1 passed: Division by zero error caught")
    
    def test_invalid_type_error(self, calculator):
        """
        Test Case 2: Invalid Type Error
        
        Purpose: Verify type validation in operations
        Expected: TypeError raised for non-numeric types
        """
        # String instead of number
        with pytest.raises(TypeError):
            calculator.add("10", 20)
        
        # List instead of number
        with pytest.raises(TypeError):
            calculator.multiply(10, [5])
        
        # None instead of number
        with pytest.raises(TypeError):
            calculator.subtract(10, None)
        
        logger.info(f"✓ Test 2 passed: Invalid type errors caught")
    
    def test_mock_library_error_handling(self, mock_library):
        """
        Test Case 3: Mock Library Error Handling
        
        Purpose: Verify mock library error handling
        Expected: Proper error handling for invalid operations
        """
        # Division by zero in mock library
        with pytest.raises(ValueError):
            mock_library.divide(10, 0)
        
        # Verify call count still increments despite error
        initial_count = mock_library.get_call_count()
        
        try:
            mock_library.divide(5, 0)
        except ValueError:
            pass
        
        # Call count should still increment
        final_count = mock_library.get_call_count()
        assert final_count > initial_count, "Call count should increment even on error"
        
        logger.info(f"✓ Test 3 passed: Mock library error handling")
