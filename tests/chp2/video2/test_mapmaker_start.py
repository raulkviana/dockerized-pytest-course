from scripts.chp2.video2.mapmaker_start import Point
import pytest


def test_make_one_point():
    p1 = Point("Dakar", 14.7167, 17.4677)
    assert p1.get_lat_long() == (14.7167, 17.4677)


def test_invalid_point_generation():
    with pytest.raises(ValueError) as exp:
        Point("Buenos Aires", 12.11386, -555.08269)

    assert str(exp.value) == "Invalid latitude or longitude"


def test_point_name():
    with pytest.raises(ValueError) as err:
        Point(2, 12.11386, 12.11386)

    assert str(err.value) == "Wrong type for name attribute"
