"""
Calculator Module

Example implementation using ctypes. Provides a Calculator class that performs
arithmetic operations using a mock C library.

Features:
- Basic arithmetic (add, subtract, multiply, divide)
- Power calculation
- Input validation
- Error handling
- Operation tracking
"""

import logging
from typing import Union
from src.c_library_wrapper import MockMathLibrary

# Logger setup
logger = logging.getLogger(__name__)


class Calculator:
    """
    Calculator class using ctypes for arithmetic operations.
    
    Uses MockMathLibrary for testing without requiring a real C library.
    Can be extended to use real C libraries by replacing MockMathLibrary
    with actual ctypes-based library loading.
    """
    
    def __init__(self, use_mock: bool = True):
        """
        Initialize the Calculator.
        
        Args:
            use_mock: Use mock library (True) or real library (False)
        """
        self.use_mock = use_mock
        self.lib = MockMathLibrary() if use_mock else None
        self.last_operation = None
        self.last_result = None
        self.operation_count = 0
        logger.info(f"Calculator initialized (use_mock={use_mock})")
    
    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Add two numbers.
        
        Args:
            a: First operand
            b: Second operand
        
        Returns:
            Sum of a and b
        
        Raises:
            TypeError: If operands are not numeric
        """
        self._validate_operands(a, b)
        result = self.lib.add(int(a), int(b))
        self._update_state('add', result)
        return result
    
    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Subtract two numbers.
        
        Args:
            a: Minuend
            b: Subtrahend
        
        Returns:
            Difference of a and b
        
        Raises:
            TypeError: If operands are not numeric
        """
        self._validate_operands(a, b)
        result = self.lib.subtract(int(a), int(b))
        self._update_state('subtract', result)
        return result
    
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Multiply two numbers.
        
        Args:
            a: First operand
            b: Second operand
        
        Returns:
            Product of a and b
        
        Raises:
            TypeError: If operands are not numeric
        """
        self._validate_operands(a, b)
        result = self.lib.multiply(int(a), int(b))
        self._update_state('multiply', result)
        return result
    
    def divide(self, a: Union[int, float], b: Union[int, float]) -> float:
        """
        Divide two numbers with error handling.
        
        Args:
            a: Dividend
            b: Divisor
        
        Returns:
            Quotient of a and b
        
        Raises:
            TypeError: If operands are not numeric
            ValueError: If attempting to divide by zero
        """
        self._validate_operands(a, b)
        if b == 0:
            logger.error("Division by zero attempted")
            raise ValueError("Cannot divide by zero")
        result = self.lib.divide(int(a), int(b))
        self._update_state('divide', result)
        return result
    
    def power(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Raise a number to a power.
        
        Args:
            a: Base
            b: Exponent
        
        Returns:
            a raised to the power of b
        
        Raises:
            TypeError: If operands are not numeric
        """
        self._validate_operands(a, b)
        result = self.lib.power(int(a), int(b))
        self._update_state('power', result)
        return result
    
    def _validate_operands(self, a: any, b: any) -> None:
        """
        Validate that operands are numeric.
        
        Args:
            a: First operand
            b: Second operand
        
        Raises:
            TypeError: If either operand is not numeric
        """
        if not isinstance(a, (int, float)):
            raise TypeError(f"First operand must be numeric, got {type(a).__name__}")
        if not isinstance(b, (int, float)):
            raise TypeError(f"Second operand must be numeric, got {type(b).__name__}")
    
    def _update_state(self, operation: str, result: Union[int, float]) -> None:
        """
        Update internal state after operation.
        
        Args:
            operation: Name of the operation performed
            result: Result of the operation
        """
        self.last_operation = operation
        self.last_result = result
        self.operation_count += 1
        logger.debug(f"Operation {operation} completed: result={result}")
    
    def get_operation_count(self) -> int:
        """
        Get total number of operations performed.
        
        Returns:
            Operation count
        """
        return self.operation_count
    
    def get_last_operation(self) -> str:
        """
        Get the last operation performed.
        
        Returns:
            Name of last operation
        """
        return self.last_operation
    
    def get_last_result(self) -> Union[int, float]:
        """
        Get the result of the last operation.
        
        Returns:
            Result of last operation
        """
        return self.last_result
    
    def reset(self) -> None:
        """
        Reset calculator state.
        """
        self.last_operation = None
        self.last_result = None
        self.operation_count = 0
        if self.lib:
            self.lib.reset_call_count()
        logger.info("Calculator reset")
