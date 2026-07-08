from factory import ServiceFactory
from services.encryption_service import EncryptionService
from services.compression_service import CompressionService


def test_create_encryption_service():
    service = ServiceFactory.create_service("encryption")
    assert isinstance(service, EncryptionService)


def test_create_compression_service():
    service = ServiceFactory.create_service("compression")
    assert isinstance(service, CompressionService)


def test_invalid_service():
    import pytest

    with pytest.raises(ValueError):
        ServiceFactory.create_service("invalid")
