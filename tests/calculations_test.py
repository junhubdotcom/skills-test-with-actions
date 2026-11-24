# System Modules
import sys
import os

# Installed Modules
import pytest

# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from calculations import area_of_circle, get_nth_fibonacci  # noqa: E402


def test_area_of_circle_positive_radius():
    """Test with a positive radius."""
    # Arrange
    radius = 1

    # Act
    result = area_of_circle(radius)

    # Assert
    assert abs(result - 3.14159) < 1e-5


def test_area_of_circle_zero_radius():
    """Test with a radius of zero."""
    # Arrange
    radius = 0

    # Act
    result = area_of_circle(radius)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_zero():
    """Test with n=0."""
    # Arrange
    n = 0

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_one():
    """Test with n=1."""
    # Arrange
    n = 1

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 1


def test_get_nth_fibonacci_ten():
    """Test with n=10."""
    # Arrange
    n = 10

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 55


def test_area_of_circle_negative_radius():
    """A negative radius has the same area as its positive magnitude."""
    assert area_of_circle(-2) == area_of_circle(2)


@pytest.mark.parametrize(
    ("n", "expected"),
    [(2, 1), (5, 5), (15, 610)],
)
def test_get_nth_fibonacci_additional_values(n, expected):
    """Test additional values across the iterative Fibonacci calculation."""
    assert get_nth_fibonacci(n) == expected


def test_get_nth_fibonacci_negative():
    """Negative indices are rejected."""
    with pytest.raises(ValueError):
        get_nth_fibonacci(-1)
