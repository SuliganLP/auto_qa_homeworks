import pytest

from simple_math import SimpleMath


@pytest.fixture
def simple_math():
    return SimpleMath()


def test_square_positive(simple_math):
    assert simple_math.square(2) == 4


def test_square_negative(simple_math):
    assert simple_math.square(-5) == 25


def test_square_zero(simple_math):
    assert simple_math.square(0) == 0


def test_square_one(simple_math):
    assert simple_math.square(1) == 1


def test_cube_positive(simple_math):
    assert simple_math.cube(3) == 27


def test_cube_negative(simple_math):
    assert simple_math.cube(-5) == -125


def test_cube_zero(simple_math):
    assert simple_math.cube(0) == 0


def test_cube_one(simple_math):
    assert simple_math.cube(1) == 1
