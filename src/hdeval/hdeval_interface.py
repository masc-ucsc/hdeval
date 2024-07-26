import subprocess
import os

class HDEvalInterface:
    def __init__(self, src_path):
        # Ensure the path to the src directory containing the decrypt and encrypt scripts is correct
        self.src_path = src_path

    def decrypt_file(self, encrypted_file_path, output_file_path):
        decrypt_script_path = os.path.join(self.src_path, 'decrypt')
        # Call the decrypt script with the necessary arguments
        result = subprocess.run([decrypt_script_path, encrypted_file_path, output_file_path], capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(f"Decryption failed: {result.stderr}")
        return output_file_path

    def encrypt_file(self, file_path, output_file_path):
        encrypt_script_path = os.path.join(self.src_path, 'encrypt')
        # Call the encrypt script with the necessary arguments
        result = subprocess.run([encrypt_script_path, file_path, output_file_path], capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(f"Encryption failed: {result.stderr}")
        return output_file_path

