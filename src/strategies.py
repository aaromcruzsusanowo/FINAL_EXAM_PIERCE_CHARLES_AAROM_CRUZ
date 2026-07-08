class DataProcessor:

    def __init__(self, strategy):
        self.strategy = strategy

    def execute(self, data):
        return self.strategy.process(data)
