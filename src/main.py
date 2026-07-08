from factory import ServiceFactory
from strategies import DataProcessor


def main():

    data_stream = [78, 82, 91, 65, 40, 99, 88]

    print("Original Dataset")
    print(data_stream)

    print("\nApplying Encryption Strategy...")
    encryption = ServiceFactory.create_service("encryption")
    encrypted = DataProcessor(encryption).execute(data_stream)
    print(encrypted)

    print("\nApplying Compression Strategy...")
    compression = ServiceFactory.create_service("compression")
    compressed = DataProcessor(compression).execute(data_stream)
    print(compressed)


if __name__ == "__main__":
    main()
