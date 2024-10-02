import os
import subprocess
import yaml
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class HDEvalInterface:
    def __init__(self):
        """
        Initialize the HDEvalInterface.
        Assumes that hdeval is located at './hdeval' relative to this file.
        """
        # Get the path to the directory containing this file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Set hdeval_repo_path to the 'hdeval' submodule
        self.hdeval_repo_path = os.path.join(current_dir, 'hdeval')
        logger.info(f"Initialized HDEvalInterface with hdeval_repo_path: {self.hdeval_repo_path}")

    def hdeval_open(self, benchmark_name):
        """
        Open and process the specified benchmark.

        :param benchmark_name: Name of the benchmark to process (e.g., '24a').
        :return: List of YAML file paths generated by yaml2yamls.py.
        """
        logger.info(f"hdeval_open called with benchmark_name: {benchmark_name}")
        yaml_file_path = os.path.join(
            self.hdeval_repo_path, 'src', 'hdeval', 'hdeval-comb', f'{benchmark_name}.yaml'
        )

        if not os.path.exists(yaml_file_path):
            logger.info(f"YAML file {yaml_file_path} not found. Attempting to run the decrypt script.")

            # Path to the decrypt script
            decrypt_script_path = os.path.join(self.hdeval_repo_path, 'src', 'decrypt')
            logger.debug(f"Looking for decrypt script at: {decrypt_script_path}")

            # Ensure the decrypt script exists and is executable
            if not os.path.exists(decrypt_script_path):
                logger.error(f"Error: Decrypt script not found at {decrypt_script_path}.")
                sys.exit(1)

            # Make sure the decrypt script is executable
            os.chmod(decrypt_script_path, 0o755)

            # Command to run the decrypt script
            # Using './decrypt' and setting cwd to 'src' where decrypt script is located
            decrypt_command = ['./decrypt', f'hdeval/hdeval-comb/{benchmark_name}']

            logger.info(f"Running decrypt script with command: {' '.join(decrypt_command)}")

            # Run the decrypt script
            try:
                subprocess.run(
                    decrypt_command,
                    cwd=os.path.join(self.hdeval_repo_path, 'src'),
                    check=True
                )
            except subprocess.CalledProcessError as e:
                logger.error(f"Error running decrypt script: {e}")
                sys.exit(1)

            # Check again if the YAML file exists after decryption
            if not os.path.exists(yaml_file_path):
                logger.error(f"Error: YAML file {yaml_file_path} still not found after decryption.")
                sys.exit(1)

            # Path to the yaml2yamls.py script
            yaml2yamls_script_path = os.path.join(self.hdeval_repo_path, 'src', 'hdeval', 'yaml2yamls.py')
            logger.debug(f"Looking for yaml2yamls.py at: {yaml2yamls_script_path}")

            # Ensure the yaml2yamls.py script exists
            if not os.path.exists(yaml2yamls_script_path):
                logger.error(f"Error: yaml2yamls.py script not found at {yaml2yamls_script_path}.")
                sys.exit(1)

            # Make sure yaml2yamls.py is executable
            os.chmod(yaml2yamls_script_path, 0o755)

            # Command to run the yaml2yamls.py script
            # Using './yaml2yamls.py' and setting cwd to 'hdeval' directory
            relative_yaml_file_path = os.path.join('hdeval-comb', f'{benchmark_name}.yaml')
            yaml2yamls_command = ['./yaml2yamls.py', relative_yaml_file_path]

            logger.info(f"Running yaml2yamls.py with command: {' '.join(yaml2yamls_command)}")

            # Run the yaml2yamls.py script
            try:
                subprocess.run(
                    yaml2yamls_command,
                    cwd=os.path.join(self.hdeval_repo_path, 'src', 'hdeval'),
                    check=True
                )
            except subprocess.CalledProcessError as e:
                logger.error(f"Error running yaml2yamls.py script: {e}")
                sys.exit(1)

            # Confirmation message
            logger.info(f"Successfully decrypted and processed {benchmark_name}.yaml")

        # After processing, list all YAML files in yaml_files_pipe
        yaml_files_pipe_dir = os.path.join(self.hdeval_repo_path, 'src', 'hdeval', 'hdeval-comb', 'yaml_files_pipe')
        logger.debug(f"Looking for generated YAML files in: {yaml_files_pipe_dir}")

        if not os.path.exists(yaml_files_pipe_dir):
            logger.error(f"Error: YAML files pipe directory '{yaml_files_pipe_dir}' does not exist.")
            sys.exit(1)

        # List all YAML files in the pipe directory
        yaml_files = [
            os.path.join(yaml_files_pipe_dir, f)
            for f in os.listdir(yaml_files_pipe_dir)
            if f.endswith('.yaml')
        ]

        if not yaml_files:
            logger.error(f"No YAML files found in '{yaml_files_pipe_dir}'.")
            sys.exit(1)

        logger.info(f"Found {len(yaml_files)} YAML files in '{yaml_files_pipe_dir}'.")
        return yaml_files

