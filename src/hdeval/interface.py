import os
import subprocess
import yaml

# interface.py
print(f"Importing interface.py from: {__file__}")

class HDEvalInterface:
    def __init__(self, hdeval_repo_path=None):
        # Use the provided path or default to '~/hdeval'
        self.hdeval_repo_path = hdeval_repo_path or os.path.expanduser('~/hdeval')
        print(f"Using interface.py from: {__file__}")
        print(f"Initialized HDEvalInterface with hdeval_repo_path: {self.hdeval_repo_path}")

    def hdeval_open(self, benchmark_name):
        # Path to the decrypted YAML file
        print(f"hdeval_open called with benchmark_name: {benchmark_name}")
        yaml_file_path = os.path.join(
            self.hdeval_repo_path, 'src', 'hdeval', 'hdeval-comb', f'{benchmark_name}.yaml'
        )

        if not os.path.exists(yaml_file_path):
            print(f"YAML file {yaml_file_path} not found. Attempting to run the decrypt script.")

            # Path to the decrypt script
            decrypt_script_path = os.path.join(self.hdeval_repo_path, 'src', 'decrypt')
            print(f"Looking for decrypt script at: {decrypt_script_path}")  # Debugging

            # Ensure the decrypt script exists and is executable
            if not os.path.exists(decrypt_script_path):
                print(f"Error: Decrypt script not found at {decrypt_script_path}.")
                exit(1)

            # Make sure the decrypt script is executable
            os.chmod(decrypt_script_path, 0o755)

            # Command to run the decrypt script
            decrypt_command = [decrypt_script_path, f'hdeval/hdeval-comb/{benchmark_name}']

            # Run the decrypt script, allowing user interaction
            try:
                subprocess.run(
                    decrypt_command,
                    cwd=os.path.join(self.hdeval_repo_path, 'src'),
                    check=True
                )
            except subprocess.CalledProcessError as e:
                print(f"Error running decrypt script: {e}")
                exit(1)

            # Check again if the YAML file exists after decryption
            if not os.path.exists(yaml_file_path):
                print(f"Error: YAML file {yaml_file_path} still not found after decryption.")
                exit(1)

            # Path to the yaml2yaml.py script
            yaml2yaml_script_path = os.path.join(self.hdeval_repo_path, 'src', 'hdeval', 'yaml2yamls.py')
            print(f"Looking for yaml2yamls.py at: {yaml2yaml_script_path}")  # Debugging

            # Ensure the yaml2yaml.py script exists
            if not os.path.exists(yaml2yaml_script_path):
                print(f"Error: yaml2yamls.py script not found at {yaml2yaml_script_path}.")
                exit(1)

            # Ensure yaml2yaml.py is executable
            os.chmod(yaml2yaml_script_path, 0o755)

            # Command to run the yaml2yaml.py script
            # Using relative path since cwd is set to 'hdeval'
            relative_yaml_file_path = os.path.join('hdeval-comb', f'{benchmark_name}.yaml')
            yaml2yaml_command = ['./yaml2yamls.py', relative_yaml_file_path]

            print(f"Running yaml2yamls.py with command: {' '.join(yaml2yaml_command)}")  # Debugging

            # Run the yaml2yaml.py script
            try:
                subprocess.run(
                    yaml2yaml_command,
                    cwd=os.path.join(self.hdeval_repo_path, 'src', 'hdeval'),
                    check=True
                )
            except subprocess.CalledProcessError as e:
                print(f"Error running yaml2yamls.py script: {e}")
                exit(1)

            # Confirmation message
            print(f"Successfully decrypted and processed {benchmark_name}.yaml")

        # After processing, list all YAML files in yaml_files_pipe
        yaml_files_pipe_dir = os.path.join(self.hdeval_repo_path, 'src', 'hdeval', 'hdeval-comb', 'yaml_files_pipe')
        print(f"Looking for generated YAML files in: {yaml_files_pipe_dir}")  # Debugging

        if not os.path.exists(yaml_files_pipe_dir):
            print(f"Error: YAML files pipe directory '{yaml_files_pipe_dir}' does not exist.")
            exit(1)

        # List all YAML files in the pipe directory
        yaml_files = [
            os.path.join(yaml_files_pipe_dir, f)
            for f in os.listdir(yaml_files_pipe_dir)
            if f.endswith('.yaml')
        ]

        if not yaml_files:
            print(f"No YAML files found in '{yaml_files_pipe_dir}'.")
            exit(1)

        print(f"Found {len(yaml_files)} YAML files in '{yaml_files_pipe_dir}'.")
        return yaml_files

