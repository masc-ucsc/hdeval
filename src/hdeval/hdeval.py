import os
import subprocess
import yaml

class HDEvalInterface:
    def __init__(self, repo_url='https://github.com/masc-ucsc/hdeval.git'):
        self.repo_url = repo_url
        self.cache_dir = os.path.expanduser('~/.cache/hdeval')

    def download_repository(self):
        if os.path.exists(self.cache_dir):
            # If repository already exists, do a git pull to update it
            subprocess.run(['git', '-C', self.cache_dir, 'pull'], check=True)
        else:
            subprocess.run(['git', 'clone', self.repo_url, self.cache_dir], check=True)

    def hdeval_open(self, benchmark_name, version=None):
        # Ensure the repository is downloaded
        self.download_repository()

        # Path to the .hdeval file
        hdeval_file_path = os.path.join(self.cache_dir, 'src', 'hdeval', 'hdeval-comb', f'{benchmark_name}.hdeval')
        if not os.path.exists(hdeval_file_path):
            print(f"Error: hdeval file {hdeval_file_path} not found.")
            exit(1)

        # Path to the decrypt script
        decrypt_script = os.path.join(self.cache_dir, 'src', 'decrypt')
        if not os.path.exists(decrypt_script):
            print(f"Error: decrypt script {decrypt_script} not found.")
            exit(1)

        # Ensure the decrypt script is executable
        subprocess.run(['chmod', '+x', decrypt_script], check=True)

        # Run the decrypt script on the .hdeval file
        result = subprocess.run([decrypt_script, hdeval_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)

        if result.returncode != 0:
            print(f"Error decrypting {hdeval_file_path}: {result.stderr}")
            exit(1)

        # The decrypted content is in result.stdout
        decrypted_content = result.stdout

        # Parse the YAML content
        benchmark_data = yaml.safe_load(decrypted_content)
        return benchmark_data

