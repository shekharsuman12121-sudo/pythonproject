# Python CTypes Mini Project with Pytest

A complete, production-ready project demonstrating Python `ctypes` integration with comprehensive pytest test cases.

## 📋 Project Overview

This project demonstrates:
- ✅ Loading and interfacing with C libraries using ctypes
- ✅ Data type mapping (c_int, c_float, c_char_p, structures, pointers)
- ✅ Function binding and calling
- ✅ Comprehensive pytest test suite with fixtures
- ✅ Error handling and validation
- ✅ Real-world use cases (Math operations, String processing, Memory management)
- ✅ Mock library for testing without real .dll/.so files

## 📁 Project Structure

```
ctypes_mini_project/
├── src/                              # Source code
│   ├── __init__.py
│   ├── c_library_wrapper.py          # Main ctypes wrapper
│   ├── data_types.py                 # Custom data types & structures
│   └── calculator.py                 # Example implementation (Math)
├── tests/                            # Test suite
│   ├── __init__.py
│   ├── conftest.py                   # Pytest fixtures & configuration
│   ├── test_calculator.py            # Test Calculator class
│   ├── test_ctypes_data_types.py     # Test ctypes data types
│   ├── test_string_operations.py     # Test string operations
│   └── test_error_handling.py        # Test error handling
├── c_library/                        # Sample C library source (for reference)
│   ├── math_lib.c                    # C library source
│   └── README.md                     # How to compile
├── requirements.txt                  # Python dependencies
├── pytest.ini                        # Pytest configuration
├── setup.py                          # Package setup
└── README.md                         # This file
```

## 🚀 Quick Start

### 1. Clone and Setup

```bash
# Clone repository
git clone https://github.com/shekharsuman12121-sudo/pythonproject.git
cd pythonproject/ctypes_mini_project

# Install dependencies
pip install -r requirements.txt
```

### 2. Run Tests

```bash
# Run all tests
pytest tests/ -v -s

# Run specific test file
pytest tests/test_calculator.py -v -s

# Run specific test case
pytest tests/test_calculator.py::TestCalculator::test_add_two_numbers -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html

# Run with detailed logging
pytest tests/ -v -s --log-cli-level=DEBUG
```

### 3. Expected Output

```
================================ test session starts =================================
platform win32 -- Python 3.9.0, pytest-7.0.0
collected 22 items

tests/test_calculator.py::TestCalculator::test_add_two_numbers PASSED        [ 4%]
tests/test_calculator.py::TestCalculator::test_subtract_numbers PASSED       [ 9%]
tests/test_calculator.py::TestCalculator::test_multiply_numbers PASSED       [13%]
tests/test_calculator.py::TestCalculator::test_divide_numbers PASSED         [18%]
tests/test_ctypes_data_types.py::TestCTypesDataTypes::test_c_int_type PASSED [22%]
tests/test_ctypes_data_types.py::TestCTypesDataTypes::test_c_float_type PASSED [27%]
tests/test_ctypes_data_types.py::TestCTypesDataTypes::test_structure_creation PASSED [31%]
tests/test_string_operations.py::TestStringOperations::test_reverse_string PASSED [36%]
tests/test_string_operations.py::TestStringOperations::test_string_length PASSED [40%]
tests/test_error_handling.py::TestErrorHandling::test_divide_by_zero PASSED [45%]
tests/test_error_handling.py::TestErrorHandling::test_invalid_function_call PASSED [50%]
... (11 more tests)

================================ 22 passed in 1.23s ==================================
```

## 📚 Key Files Explanation

### `src/c_library_wrapper.py`
Core wrapper class for loading and interfacing with C libraries using ctypes.

**Features:**
- Load .dll/.so/.dylib files
- Bind and call C functions
- Type validation and conversion
- Error handling
- Call history tracking

**Example:**
```python
from src.c_library_wrapper import CLibraryWrapper

# Create wrapper instance
wrapper = CLibraryWrapper()

# Load library (mock for testing)
lib = wrapper.load_library('math_lib')

# Bind function
wrapper.bind_function(lib, 'add', [c_int, c_int], c_int)

# Call function
result = lib.add(10, 20)
print(result)  # Output: 30
```

### `src/calculator.py`
Example implementation using ctypes - Calculator class for math operations.

**Features:**
- Add, subtract, multiply, divide operations
- Input validation
- Error handling
- Mock mode for testing

**Example:**
```python
from src.calculator import Calculator

calc = Calculator(use_mock=True)  # Use mock library for testing
result = calc.add(15, 25)
print(result)  # Output: 40
```

### `src/data_types.py`
Custom data types and structures for ctypes.

**Includes:**
- Basic types: c_int, c_float, c_char_p, c_bool
- Complex structures: Point, Rectangle, Person
- Type validators and converters

### `tests/conftest.py`
Pytest configuration and fixtures.

**Provides:**
- Logger fixture
- Calculator fixture
- Library wrapper fixture
- Test data fixtures
- Automatic setup/teardown

### `tests/test_calculator.py`
Test cases for Calculator class (12 test cases).

**Coverage:**
- Basic arithmetic operations
- Edge cases (divide by zero, negative numbers)
- Parametrized tests (data-driven)
- Type validation
- Complex calculations

### `tests/test_ctypes_data_types.py`
Test cases for ctypes data types (5 test cases).

**Coverage:**
- Integer operations
- Float operations
- String handling
- Structure creation and manipulation
- Pointer operations

### `tests/test_string_operations.py`
Test cases for string operations using ctypes (4 test cases).

**Coverage:**
- String reversal
- String length
- String concatenation
- String validation

### `tests/test_error_handling.py`
Test cases for error handling (3 test cases).

**Coverage:**
- Division by zero
- Invalid function calls
- Type mismatch errors
- Exception handling

## 🧪 Test Case Examples

### Example 1: Simple Addition Test

```python
def test_add_two_numbers(self, calculator):
    """
    Test Case: Simple Addition
    Purpose: Verify that add operation works correctly
    Input: 10, 20
    Expected Output: 30
    """
    # Arrange
    num1, num2 = 10, 20
    
    # Act
    result = calculator.add(num1, num2)
    
    # Assert
    assert result == 30, f"Expected 30, got {result}"
    assert calculator.last_operation == 'add'
```

### Example 2: Parametrized Test (Data-Driven)

```python
@pytest.mark.parametrize("a,b,expected", [
    (5, 3, 8),
    (10, 20, 30),
    (-5, 5, 0),
    (0, 0, 0),
])
def test_add_parametrized(self, calculator, a, b, expected):
    """
    Test Case: Parametrized Addition
    Tests multiple input combinations in one test
    """
    result = calculator.add(a, b)
    assert result == expected
```

### Example 3: Error Handling Test

```python
def test_divide_by_zero(self, calculator):
    """
    Test Case: Division by Zero Error
    Purpose: Verify proper error handling
    Expected: Raises ValueError
    """
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(10, 0)
```

### Example 4: ctypes Data Type Test

```python
def test_c_int_type(self):
    """
    Test Case: C Integer Type
    Purpose: Verify ctypes c_int behavior
    """
    # Create c_int
    value = c_int(42)
    
    # Assert
    assert value.value == 42
    assert isinstance(value, c_int)
    
    # Modify value
    value.value = 100
    assert value.value == 100
```

## 🔧 ctypes Concepts Covered

| Concept | Implementation | Test Case |
|---------|-----------------|----------|
| **Loading Libraries** | `ctypes.CDLL()`, `ctypes.WinDLL()` | test_calculator.py |
| **Function Binding** | `lib.function_name.argtypes`, `restype` | test_calculator.py |
| **Data Types** | c_int, c_float, c_char_p, c_bool | test_ctypes_data_types.py |
| **Structures** | `Structure` class, fields definition | test_ctypes_data_types.py |
| **Pointers** | `POINTER()`, `byref()`, `pointer()` | test_ctypes_data_types.py |
| **Error Handling** | Exception handling, validation | test_error_handling.py |
| **Type Validation** | Custom validators, type checking | All test files |
| **Mock Testing** | Mock library without real .dll/.so | conftest.py |

## 📝 Test Execution Flow

```
┌─────────────────────────────────────┐
│   pytest test execution starts      │
└──────────────┬──────────────────────┘
               │
               ├─ Load conftest.py
               │  └─ Create fixtures (logger, calculator, etc.)
               │
               ├─ Discover tests (test_*.py)
               │
               ├─ Test 1: test_add_two_numbers
               │  ├─ Setup (fixture)
               │  ├─ Execute test
               │  ├─ Assert results
               │  └─ Teardown
               │
               ├─ Test 2: test_parametrized (multiple runs)
               │  ├─ Run with (5, 3, 8)
               │  ├─ Run with (10, 20, 30)
               │  └─ Run with (-5, 5, 0)
               │
               ├─ Test 3-22: (other tests)
               │
               └─ Generate Report
                  ├─ 22 passed
                  ├─ 0 failed
                  └─ Execution time
```

## 🎯 Running Specific Tests

```bash
# Run only calculator tests
pytest tests/test_calculator.py -v

# Run only parametrized tests
pytest tests/test_calculator.py::TestCalculator::test_add_parametrized -v

# Run tests matching pattern
pytest tests/ -k "add" -v

# Run with specific marker
pytest tests/ -m "slow" -v

# Run with detailed failure info
pytest tests/ -v --tb=long

# Run and stop on first failure
pytest tests/ -x -v
```

## 📊 Test Coverage

```bash
# Generate coverage report
pytest tests/ --cov=src --cov-report=html

# View coverage in terminal
pytest tests/ --cov=src --cov-report=term-missing
```

Expected coverage: **90%+**

## 🔌 Using Real C Library

To use a real compiled C library instead of mock:

1. Compile your C library (.dll, .so, or .dylib)
2. Update `src/calculator.py`:

```python
class Calculator:
    def __init__(self, use_mock=False, lib_path=None):
        if use_mock:
            # Use mock library (for testing)
            self.lib = MockMathLibrary()
        else:
            # Load real library
            self.lib = ctypes.CDLL(lib_path)  # Windows: '.dll', Linux: '.so'
```

3. Update test conftest.py fixture:

```python
@pytest.fixture
def calculator():
    return Calculator(use_mock=False, lib_path='./path/to/library.dll')
```

## 📋 Requirements

- Python 3.7+
- pytest >= 7.0.0
- pytest-cov >= 3.0.0 (for coverage)
- pytest-html >= 3.0.0 (for HTML reports)

All listed in `requirements.txt`

## ✅ Checklist

- ✅ Complete project structure
- ✅ Core ctypes wrapper class
- ✅ Example implementation (Calculator)
- ✅ Custom data types and structures
- ✅ 22 comprehensive test cases
- ✅ Pytest fixtures and configuration
- ✅ Parametrized tests (data-driven)
- ✅ Error handling tests
- ✅ Mock library for testing
- ✅ Detailed documentation
- ✅ Quick start guide
- ✅ Real library integration support

## 📚 Additional Resources

- [ctypes Documentation](https://docs.python.org/3/library/ctypes.html)
- [pytest Documentation](https://docs.pytest.org/)
- [Python CTypes Tutorial](https://realpython.com/ctypes-foreign-functions-libraries/)

## 🎓 Learning Path

1. Start with `test_calculator.py` - Simple use cases
2. Read `src/calculator.py` - Implementation details
3. Study `test_ctypes_data_types.py` - Data type mapping
4. Explore `src/c_library_wrapper.py` - Core wrapper
5. Review `tests/conftest.py` - Pytest configuration
6. Check `tests/test_error_handling.py` - Error scenarios

## 🤝 Contributing

To add new test cases:
1. Create new test file in `tests/` directory
2. Follow naming convention: `test_*.py`
3. Use fixtures from `conftest.py`
4. Add docstrings to test functions
5. Run `pytest` to validate

## 📞 Support

For issues or questions:
1. Check test output for error details
2. Review documentation in each file
3. Examine similar test cases for patterns
4. Enable debug logging: `pytest tests/ -v -s --log-cli-level=DEBUG`

---

**Happy Testing!** 🚀
