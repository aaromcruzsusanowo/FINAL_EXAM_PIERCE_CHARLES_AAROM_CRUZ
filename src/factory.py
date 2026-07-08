from services.encryption_service import EncryptionService
from services.compression_service import CompressionService


class ServiceFactory:

    @staticmethod
    def create_service(service_name):

        if service_name.lower() == "encryption":
            return EncryptionService()

        elif service_name.lower() == "compression":
            return CompressionService()

        raise ValueError(f"Unknown service: {service_name}")