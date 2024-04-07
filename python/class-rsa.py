from Crypto.PublicKey import RSA
import time

class SimpleRSAKeyGenerator:
    def __init__(self, key_size=1024):
        self.key_size = key_size
        self.private_key = None
        self.public_key = None
        self.total_time = None

    def generate_keys(self):
        """
        Generate RSA public and private keys.
        """
        start_time = time.time()
        key = RSA.generate(self.key_size)
        self.private_key = key.export_key("PEM")
        self.public_key = key.publickey().export_key("PEM")
        end_time = time.time()
        self.total_time = end_time - start_time

    def print_keys(self):
        """
        Print generated RSA public and private keys.
        """
        print("Public key:")
        print(self.public_key.decode())
        print("\nPrivate key:")
        print(self.private_key.decode())

    def get_generation_time(self):
        """
        Return time taken for key generation.
        """
        return self.total_time

# Test the SimpleRSAKeyGenerator class
if __name__ == "__main__":
    rsa_key_generator = SimpleRSAKeyGenerator()
    rsa_key_generator.generate_keys()
    rsa_key_generator.print_keys()
    print("\nTime taken for key generation:", rsa_key_generator.get_generation_time(), "seconds")
