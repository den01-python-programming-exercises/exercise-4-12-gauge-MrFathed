class Gauge:
    def __init__(self, value):
        self.value = value

    def increase(self):
        self.value += 1

    def decrease(self):
        if self.value >= 1:
            self.value -= 1

    def value(self):
        return self.value

    def full(self):
        return self.value == 5