"""
Pytest Configuration and Fixtures

This module provides:
- Pytest configuration
- Fixtures for tests (Calculator, Logger, Test Data)
- Setup and teardown hooks
- Shared test utilities
"""

import pytest
import logging
import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from src.calculator import Calculator
from src.c_library_wrapper import MockMathLibrary, CLibraryWrapper
from src.data_types import Point, Rectangle, Person

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('test_results.log')
    ]
)

logger = logging.getLogger(__name__)


# ==================== Fixtures ====================

@pytest.fixture(scope="function")
def calculator():
    """
    Fixture: Calculator instance.
    
    Provides a fresh Calculator instance for each test.
    Uses mock library for testing without real C library.
    
    Yields:
        Calculator: Initialized calculator instance
    """
    logger.info("\n" + "="*60)
    logger.info("Setting up Calculator fixture")
    calc = Calculator(use_mock=True)
    
    yield calc
    
    # Teardown
    logger.info(f"Tearing down Calculator (operations: {calc.get_operation_count()})")
    calc.reset()
    logger.info("="*60)


@pytest.fixture(scope="function")
def mock_library():
    """
    Fixture: Mock Math Library instance.
    
    Provides a fresh MockMathLibrary instance for each test.
    
    Yields:
        MockMathLibrary: Mock library instance
    """
    logger.info("Setting up MockMathLibrary fixture")
    lib = MockMathLibrary()
    
    yield lib
    
    logger.info(f"Tearing down MockMathLibrary (calls: {lib.get_call_count()})")
    lib.reset_call_count()


@pytest.fixture(scope="function")
def library_wrapper():
    """
    Fixture: CLibraryWrapper instance.
    
    Provides a fresh CLibraryWrapper instance for each test.
    
    Yields:
        CLibraryWrapper: Library wrapper instance
    """
    logger.info("Setting up CLibraryWrapper fixture")
    wrapper = CLibraryWrapper()
    
    yield wrapper
    
    logger.info(f"Tearing down CLibraryWrapper (errors: {wrapper.get_error_count()})")


@pytest.fixture(scope="function")
def test_point():
    """
    Fixture: Point data structure.
    
    Provides a Point structure instance.
    
    Yields:
        Point: Point at (3, 4)
    """
    point = Point(x=3, y=4)
    logger.info(f"Created test point: {point}")
    yield point


@pytest.fixture(scope="function")
def test_rectangle():
    """
    Fixture: Rectangle data structure.
    
    Provides a Rectangle structure instance.
    
    Yields:
        Rectangle: Rectangle with width=5.0, height=10.0
    """
    rect = Rectangle(width=5.0, height=10.0, x=0, y=0)
    logger.info(f"Created test rectangle: {rect}")
    yield rect


@pytest.fixture(scope="function")
def test_person():
    """
    Fixture: Person data structure.
    
    Provides a Person structure instance.
    
    Yields:
        Person: Person record
    """
    person = Person(name=b"John Doe", age=30, height=5.9)
    logger.info(f"Created test person: {person}")
    yield person


@pytest.fixture(scope="function")
def test_data():
    """
    Fixture: Test data dictionary.
    
    Provides various test data for parametrized tests.
    
    Yields:
        dict: Test data
    """
    data = {
        'numbers': [1, 2, 3, 4, 5, 10, 20, 100],
        'pairs': [(2, 3), (10, 5), (100, 10)],
        'strings': ['hello', 'world', 'test', 'ctypes'],
        'operations': ['add', 'subtract', 'multiply', 'divide']
    }
    logger.info("Created test data fixture")
    yield data


@pytest.fixture(scope="session")
def logger_fixture():
    """
    Fixture: Logger instance (session scope).
    
    Provides logger for use in tests.
    
    Yields:
        logging.Logger: Logger instance
    """
    return logger


# ==================== Hooks ====================

def pytest_configure(config):
    """
    Pytest hook: Configure pytest before tests run.
    
    Registers custom markers.
    
    Args:
        config: Pytest config object
    """
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line(
        "markers", "parametrize: marks tests with parametrize"
    )
    logger.info("\n" + "="*60)
    logger.info("PYTEST CONFIGURATION COMPLETE")
    logger.info("="*60)


def pytest_collection_modifyitems(config, items):
    """
    Pytest hook: Modify test items after collection.
    
    Args:
        config: Pytest config object
        items: List of test items
    """
    logger.info(f"Collected {len(items)} test items")


# ==================== Assertions ====================

def assert_in_range(value, min_val, max_val, message=""):
    """
    Custom assertion: Check if value is in range.
    
    Args:
        value: Value to check
        min_val: Minimum value (inclusive)
        max_val: Maximum value (inclusive)
        message: Custom error message
    
    Raises:
        AssertionError: If value is out of range
    """
    assert min_val <= value <= max_val, \
        f"{message}\nValue {value} not in range [{min_val}, {max_val}]"


def assert_positive(value, message=""):
    """
    Custom assertion: Check if value is positive.
    
    Args:
        value: Value to check
        message: Custom error message
    
    Raises:
        AssertionError: If value is not positive
    """
    assert value > 0, f"{message}\nValue {value} is not positive"


def assert_non_negative(value, message=""):
    """
    Custom assertion: Check if value is non-negative.
    
    Args:
        value: Value to check
        message: Custom error message
    
    Raises:
        AssertionError: If value is negative
    """
    assert value >= 0, f"{message}\nValue {value} is negative"
