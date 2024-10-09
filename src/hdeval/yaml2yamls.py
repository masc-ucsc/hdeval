# src/hdeval/yaml2yamls.py

import argparse
import os
import re
import ruamel.yaml

def clean_bench_response(response):
    """
    Cleans the bench_response string by removing backslashes used for line continuations
    and any remaining backslashes.
    """
    # Replace backslash followed by newline and optional spaces with a newline
    response = re.sub(r'\\\s*\n\s*', '\n', response)
    # Remove any remaining backslashes
    response = response.replace('\\', '')
    return response

def main():
    parser = argparse.ArgumentParser(description="Process YAML files.")
    parser.add_argument('input_yaml', type=str, help='Input YAML file to process')
    args = parser.parse_args()

    input_yaml = args.input_yaml
    output_dir = os.path.join(os.path.dirname(input_yaml), 'yaml_files_pipe')
    os.makedirs(output_dir, exist_ok=True)
    print(f"Output directory: {output_dir}")

    yaml = ruamel.yaml.YAML()
    yaml.preserve_quotes = True
    yaml.indent(mapping=2, sequence=4, offset=2)
    yaml.width = 4096  # Prevent line wrapping

    with open(input_yaml, 'r') as file:
        data = yaml.load(file)
        print("YAML file loaded successfully.")

    for problem in data.get('verilog_problems', []):
        bench_name = problem.get('bench_name', 'unknown')
        output_filename = os.path.join(output_dir, f"{bench_name}_spec.yaml")

        # Clean and prepare 'bench_response'
        bench_response = problem.get('bench_response', '')
        bench_response = clean_bench_response(bench_response)
        bench_response = ruamel.yaml.scalarstring.LiteralScalarString(bench_response)

        # Clean and prepare 'interface' (optional)
        interface = problem.get('interface', '')
        interface = ruamel.yaml.scalarstring.LiteralScalarString(interface)

        with open(output_filename, 'w') as outfile:
            yaml.dump({
                'description': problem.get('description', ''),
                'interface': interface,
                'bench_response': bench_response
            }, outfile)
            print(f"File written: {output_filename}")

    print("All files have been successfully created.")

if __name__ == "__main__":
    main()
