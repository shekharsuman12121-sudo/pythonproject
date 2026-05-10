"""
C Library Wrapper Module

Provides a wrapper class for loading and interfacing with C libraries using ctypes.

Features:
- Load .dll, .so, .dylib files
- Bind and call C functions
- Type validation and conversion
- Error handling and recovery
- Call history tracking
- Mock library support for testing
"""

import ctypes
from ctypes import c_int, c_float, c_char_p, CDLL, WinDLL
import logging
from typing import Optional, Any, List, Tuple, Callable
import platform

# Logger setup
logger = logging.getLogger(__name__)


class CLibraryWrapper:
    """
    Wrapper class for loading and interfacing with C libraries using ctypes.
    
    This class provides:
    - Library loading (platform-specific: .dll, .so, .dylib)
    - Function binding with type signatures
    - Type validation
    - Error handling
    - Call tracking
    """
    
    def __init__(self, library_path: Optional[str] = None):
        """
        Initialize the C Library Wrapper.
        
        Args:
            library_path: Path to the C library file (.dll, .so, .dylib)
        """
        self.library_path = library_path
        self.lib = None
        self.functions = {}
        self.call_history = []
        self.error_count = 0
        logger.info(f"CLibraryWrapper initialized with path: {library_path}")
    
    def load_library(self, lib_path: str, use_win_dll: bool = False) -> Optional[Any]:
        """
        Load a C library (platform-specific).
        
        Args:
            lib_path: Path to library file
            use_win_dll: Use WinDLL instead of CDLL (Windows only)
        
        Returns:
            Loaded library object, or None if failed
        
        Raises:
            OSError: If library cannot be found or loaded
        """
        try:
            if use_win_dll and platform.system() == 'Windows':
                self.lib = WinDLL(lib_path)
                logger.info(f"Loaded library (WinDLL): {lib_path}")
            else:
                self.lib = CDLL(lib_path)
                logger.info(f"Loaded library (CDLL): {lib_path}")
            return self.lib
        except OSError as e:
            logger.error(f"Failed to load library {lib_path}: {e}")
            self.error_count += 1
            raise
    
    def bind_function(self, lib: Any, func_name: str, 
                     arg_types: List[Any], return_type: Any) -> Callable:
        """
        Bind a C function with its type signature.
        
        Args:
            lib: Library object
            func_name: Name of the function in the library
            arg_types: List of argument types (ctypes)
            return_type: Return type (ctypes)
        
        Returns:
            Bound function
        
        Raises:
            AttributeError: If function not found in library
        """
        try:
            func = getattr(lib, func_name)
            func.argtypes = arg_types
            func.restype = return_type
            self.functions[func_name] = {
                'function': func,
                'arg_types': arg_types,
                'return_type': return_type
            }
            logger.info(f"Bound function: {func_name}({arg_types}) -> {return_type}")
            return func
        except AttributeError as e:
            logger.error(f"Function {func_name} not found in library: {e}")
            self.error_count += 1
            raise
    
    def call_function(self, func_name: str, *args) -> Any:
        """
        Call a bound function with arguments.
        
        Args:
            func_name: Name of the function to call
            *args: Arguments to pass to the function
        
        Returns:
            Result from the function call
        
        Raises:
            KeyError: If function not bound
            ctypes.ArgumentError: If argument types don't match
        """
        try:
            if func_name not in self.functions:
                raise KeyError(f"Function {func_name} not bound")
            
            func = self.functions[func_name]['function']
            result = func(*args)
            
            # Track call
            self.call_history.append({
                'function': func_name,
                'args': args,
                'result': result
            })
            
            logger.debug(f"Called {func_name}({args}) -> {result}")
            return result
        except (KeyError, ctypes.ArgumentError) as e:
            logger.error(f"Error calling {func_name}: {e}")
            self.error_count += 1
            raise
    
    def get_call_history(self) -> List[Tuple]:
        """
        Get history of all function calls made.
        
        Returns:
            List of call records
        """
        return self.call_history
    
    def clear_call_history(self) -> None:
        """
        Clear the call history.
        """
        self.call_history = []
        logger.info("Call history cleared")
    
    def get_error_count(self) -> int:
        """
        Get total number of errors encountered.
        
        Returns:
            Error count
        """
        return self.error_count
    
    def reset_error_count(self) -> None:
        """
        Reset error counter.
        """
        self.error_count = 0
        logger.info("Error counter reset")


class MockMathLibrary:
    """
    Mock C library for testing without requiring a real compiled library.
    
    Simulates basic math operations:
    - add(a, b) -> a + b
    - subtract(a, b) -> a - b
    - multiply(a, b) -> a * b
    - divide(a, b) -> a / b (with division by zero check)
    - power(a, b) -> a ** b
    """
    
    def __init__(self):
        """
        Initialize the mock library.
        """
        self.call_count = 0
        logger.info("MockMathLibrary initialized")
    
    def add(self, a: int, b: int) -> int:
        """
        Add two numbers.
        
        Args:
            a: First number
            b: Second number
        
        Returns:
            Sum of a and b
        """
        self.call_count += 1
        result = a + b
        logger.debug(f"Mock add({a}, {b}) = {result}")
        return result
    
    def subtract(self, a: int, b: int) -> int:
        """
        Subtract two numbers.
        
        Args:
            a: First number
            b: Second number
        
        Returns:
            Difference of a and b
        """
        self.call_count += 1
        result = a - b
        logger.debug(f"Mock subtract({a}, {b}) = {result}")
        return result
    
    def multiply(self, a: int, b: int) -> int:
        """
        Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
        
        Returns:
            Product of a and b
        """
        self.call_count += 1
        result = a * b
        logger.debug(f"Mock multiply({a}, {b}) = {result}")
        return result
    
    def divide(self, a: int, b: int) -> float:
        """
        Divide two numbers with error handling.
        
        Args:
            a: Dividend
            b: Divisor
        
        Returns:
            Quotient of a and b
        
        Raises:
            ValueError: If attempting to divide by zero
        """
        self.call_count += 1
        if b == 0:
            logger.error("Division by zero attempted")
            raise ValueError("Cannot divide by zero")
        result = a / b
        logger.debug(f"Mock divide({a}, {b}) = {result}")
        return result
    
    def power(self, a: int, b: int) -> int:
        """
        Raise a number to a power.
        
        Args:
            a: Base number
            b: Exponent
        
        Returns:
            a raised to the power of b
        """
        self.call_count += 1
        result = a ** b
        logger.debug(f"Mock power({a}, {b}) = {result}")
        return result
    
    def get_call_count(self) -> int:
        """
        Get total number of function calls made.
        
        Returns:
            Call count
        """
        return self.call_count
    
    def reset_call_count(self) -> None:
        """
        Reset the call counter.
        """
        self.call_count = 0
        logger.info("Mock library call count reset")
