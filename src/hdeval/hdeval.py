import os
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

    def hdeval_open(self, benchmark_name):
        # Ensure the repository is downloaded
        self.download_repository()

        # Path to the decrypted YAML file
        yaml_file_path = os.path.join(self.cache_dir, 'src', 'hdeval', 'hdeval-comb', f'{benchmark_name}.yaml')

        if not os.path.exists(yaml_file_path):
            print(f"Error: YAML file {yaml_file_path} not found. Please run the decrypt script manually.")
            exit(1)

        # Read and parse the YAML content
        with open(yaml_file_path, 'r') as file:
            benchmark_data = yaml.safe_load(file)

        return benchmark_data

