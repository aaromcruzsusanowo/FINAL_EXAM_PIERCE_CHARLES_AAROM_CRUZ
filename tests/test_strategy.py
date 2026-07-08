from strategies import DataProcessor
from services.encryption_service import EncryptionService
from services.compression_service import CompressionService


def test_encryption_strategy():

    data = [78, 82, 91]

    processor = DataProcessor(EncryptionService())

    result = processor.execute(data)

    assert result != data


def test_compression_strategy():

    data = [100]

    processor = DataProcessor(CompressionService())

    result = processor.execute(data)

    assert result == [999]
