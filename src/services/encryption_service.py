class EncryptionService:
    """
    Encryption Strategy
    XOR Encryption using key 0x4F
    """

    def __init__(self, key=0x4F):
        self.key = key

    def process(self, data):
        return [value ^ self.key for value in data]
