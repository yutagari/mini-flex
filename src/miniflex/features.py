from collections import deque

class RollingMean:
    def __init__(self,window: int):
        if window <= 0:
            raise ValueError(f"Window must be positive, currently: {window}")
        
        self._window = window
        self._history = deque(maxlen=window)

    def update(self,value: float) -> None:
        self._history.append(value)
        
    def evaluate(self) -> float | None:
        return sum(self._history)/len(self._history)



feature = RollingMean(6)

feature.update(2)
feature.update(3)
feature.update(1)
feature.update(6)
feature.update(5)
feature.update(4)
feature.update(7)
print(feature.evaluate())