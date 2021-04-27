from scripts.chp2.video3.mapmaker_exceptions_start import Point
import pytest


def test_make_one_point():
    p1 = Point("Dakar", 14.7167, 17.4677)
    assert p1.get_lat_long() == (14.7167, 17.4677)


def test_invalid_point_generation():  # TO DO
    with pytest.raises(Exception) as exp:
        Point("Paris", 45.23, -560.19)
    # checking the value raised by the exception
    assert str(exp.value) == "Invalid Coordinates"

    with pytest.raises(Exception) as exp:
        Point(2, 45.23, 122)
    assert str(exp.value) == "City name must be a string"
