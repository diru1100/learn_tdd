from scripts.chp2.video2.mapmaker_start import Point


def test_make_one_point():
    p1 = Point("Hyderabad", 75.23, 90.23)
    assert p1.get_lat_long() == (75.23, 90.23)
