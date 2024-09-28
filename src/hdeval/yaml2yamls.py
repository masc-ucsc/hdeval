#!/usr/bin/env python3

import yaml
import os
import sys

class FoldedDumper(yaml.SafeDumper):
    """
    A YAML dumper that forces folded style for multi-line strings.
    """

def folded_representer(dumper, data):
    """
    This representer will convert multiline strings to folded style.
    """
    if '\n' in data:
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='>')
    else:
        return dumper.represent_scalar('tag:yaml.org,2002:str', data)

FoldedDumper.add_representer(str, folded_representer)

def split_yaml_sections(input_file):
    try:
        base_dir = os.path.dirname(input_file)
        output_dir = os.path.join(base_dir, 'yaml_files_pipe')
        os.makedirs(output_dir, exist_ok=True)
        print(f"Output directory: {output_dir}")

        with open(input_file, 'r') as file:
            data = yaml.safe_load(file)
            print("YAML file loaded successfully.")

        # Process each entry under 'verilog_problems'
        for problem in data['verilog_problems']:
            output_filename = os.path.join(output_dir, f"{problem['bench_name']}_spec.yaml")
            print(f"Processing {problem['bench_name']}...")

            selected_data = {
                'description': problem['description'],
                'interface': problem['interface']
            }

            with open(output_filename, 'w') as outfile:
                yaml.dump(selected_data, outfile, Dumper=FoldedDumper, default_flow_style=False, sort_keys=False)
            print(f"File written: {output_filename}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./yaml2yamls.py <input_file.yaml>")
    else:
        input_file = sys.argv[1]
        print(f"Starting the YAML splitting process for {input_file}")
        split_yaml_sections(input_file)
        print("All files have been successfully created.")

