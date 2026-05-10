"""
Calculator Test Module

Tests for the Calculator class using pytest.

Test Coverage:
- Basic arithmetic operations (add, subtract, multiply, divide)
- Edge cases (negative numbers, zero, large numbers)
- Parametrized tests (data-driven)
- Error handling
- State tracking
- Complex calculations

Total Test Cases: 12
"""

import pytest
import logging
from src.calculator import Calculator

logger = logging.getLogger(__name__)


class TestCalculator:
    """
    Test class for Calculator.
    
    Inheriting from object and using pytest fixtures.
    """
    
    def test_calculator_initialization(self):
        """
        Test Case 1: Calculator Initialization
        
        Purpose: Verify that calculator initializes correctly
        Expected: Calculator created with mock library
        """
        calc = Calculator(use_mock=True)
        
        assert calc is not None, "Calculator should be initialized"
        assert calc.lib is not None, "Library should be loaded"
        assert calc.operation_count == 0, "Operation count should start at 0"
        
        logger.info("✓ Test 1 passed: Calculator initialization")
    
    def test_simple_arithmetic_add(self, calculator):
        """
        Test Case 2: Simple Addition
        
        Purpose: Test basic add operation
        Input: 10 + 20
        Expected: 30
        """
        result = calculator.add(10, 20)
        
        assert result == 30, f"Expected 30, got {result}"
        assert calculator.last_operation == 'add'
        assert calculator.get_operation_count() == 1
        
        logger.info(f"✓ Test 2 passed: Addition 10 + 20 = {result}")
    
    def test_simple_arithmetic_subtract(self, calculator):
        """
        Test Case 3: Simple Subtraction
        
        Purpose: Test basic subtract operation
        Input: 50 - 20
        Expected: 30
        """
        result = calculator.subtract(50, 20)
        
        assert result == 30, f"Expected 30, got {result}"
        assert calculator.last_operation == 'subtract'
        
        logger.info(f"✓ Test 3 passed: Subtraction 50 - 20 = {result}")
    
    def test_simple_arithmetic_multiply(self, calculator):
        """
        Test Case 4: Simple Multiplication
        
        Purpose: Test basic multiply operation
        Input: 5 * 6
        Expected: 30
        """
        result = calculator.multiply(5, 6)
        
        assert result == 30, f"Expected 30, got {result}"
        assert calculator.last_operation == 'multiply'
        
        logger.info(f"✓ Test 4 passed: Multiplication 5 * 6 = {result}")
    
    def test_simple_arithmetic_divide(self, calculator):
        """
        Test Case 5: Simple Division
        
        Purpose: Test basic divide operation
        Input: 60 / 2
        Expected: 30.0
        """
        result = calculator.divide(60, 2)
        
        assert result == 30.0, f"Expected 30.0, got {result}"
        assert calculator.last_operation == 'divide'
        
        logger.info(f"✓ Test 5 passed: Division 60 / 2 = {result}")
    
    def test_power_operation(self, calculator):
        """
        Test Case 6: Power Operation
        
        Purpose: Test exponentiation
        Input: 2 ** 10
        Expected: 1024
        """
        result = calculator.power(2, 10)
        
        assert result == 1024, f"Expected 1024, got {result}"
        assert calculator.last_operation == 'power'
        
        logger.info(f"✓ Test 6 passed: Power 2 ** 10 = {result}")
    
    def test_negative_numbers(self, calculator):
        """
        Test Case 7: Operations with Negative Numbers
        
        Purpose: Verify calculations with negative operands
        Input: -10 + 5
        Expected: -5
        """
        result = calculator.add(-10, 5)
        
        assert result == -5, f"Expected -5, got {result}"
        
        # Test more negative operations
        result2 = calculator.multiply(-3, 4)
        assert result2 == -12, f"Expected -12, got {result2}"
        
        logger.info(f"✓ Test 7 passed: Negative number operations")
    
    def test_zero_operations(self, calculator):
        """
        Test Case 8: Operations with Zero
        
        Purpose: Verify calculations with zero
        Expected: Proper handling of zero
        """
        # Add with zero
        result1 = calculator.add(10, 0)
        assert result1 == 10, f"Expected 10, got {result1}"
        
        # Multiply with zero
        result2 = calculator.multiply(100, 0)
        assert result2 == 0, f"Expected 0, got {result2}"
        
        logger.info(f"✓ Test 8 passed: Zero operations")
    
    def test_divide_by_zero_error(self, calculator):
        """
        Test Case 9: Division by Zero Error Handling
        
        Purpose: Verify proper error handling for division by zero
        Expected: Raises ValueError with specific message
        """
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calculator.divide(10, 0)
        
        logger.info(f"✓ Test 9 passed: Division by zero error handling")
    
    def test_invalid_operand_type(self, calculator):
        """
        Test Case 10: Invalid Operand Type
        
        Purpose: Verify type validation
        Expected: Raises TypeError
        """
        with pytest.raises(TypeError, match="must be numeric"):
            calculator.add("10", 20)
        
        with pytest.raises(TypeError, match="must be numeric"):
            calculator.multiply(10, [5])
        
        logger.info(f"✓ Test 10 passed: Invalid operand type handling")
    
    @pytest.mark.parametrize("a,b,expected", [
        (2, 3, 5),      # Simple addition
        (10, 20, 30),   # Larger numbers
        (-5, 5, 0),     # Negative and positive
        (0, 0, 0),      # Zero values
        (100, 200, 300),# Large numbers
    ])
    def test_add_parametrized(self, calculator, a, b, expected):
        """
        Test Case 11: Parametrized Addition Tests
        
        Purpose: Data-driven testing with multiple input combinations
        Expected: All combinations should work correctly
        """
        result = calculator.add(a, b)
        assert result == expected, f"add({a}, {b}): expected {expected}, got {result}"
        logger.debug(f"Parametrized add test: {a} + {b} = {result}")
    
    def test_multiple_operations_sequence(self, calculator):
        """
        Test Case 12: Multiple Operations in Sequence
        
        Purpose: Test calculator state tracking across multiple operations
        Expected: All operations succeed and state is properly maintained
        
        Calculation: ((10 + 20) * 2) - 10 = 50
        """
        # Start with 10 + 20 = 30
        result1 = calculator.add(10, 20)
        assert result1 == 30
        assert calculator.get_operation_count() == 1
        
        # Then 30 * 2 = 60
        result2 = calculator.multiply(result1, 2)
        assert result2 == 60
        assert calculator.get_operation_count() == 2
        
        # Finally 60 - 10 = 50
        result3 = calculator.subtract(result2, 10)
        assert result3 == 50
        assert calculator.get_operation_count() == 3
        
        # Verify state
        assert calculator.get_last_operation() == 'subtract'
        assert calculator.get_last_result() == 50
        
        logger.info(f"✓ Test 12 passed: Multiple operations sequence = {result3}")
