'''
from miniflex.features import RollingMean


def test_rolling_mean():
    # Arrange
    mean = RollingMean(window=3)

    # Act
    mean.update(2)
    mean.update(4)
    mean.update(6)

    # Assert
    assert mean.evaluate() == 4.0

def test_rolling_mean_window():
    mean = RollingMean(window=3)
    
    mean.update(2)
    mean.update(4)
    mean.update(6)
    mean.update(12)

    assert mean.evaluate() == 22 / 3

'''
