class CompressionService:
    """
    Compression Strategy
    Simulates compression by multiplying values by 0.85
    """

    def __init__(self, factor=0.85):
        self.factor = factor

    def process(self, data):
        return [round(value * self.factor, 2) for value in data]
