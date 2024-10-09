# src/hdeval/yaml2yamls.py

def main():
    import argparse
    import yaml
    import os

    parser = argparse.ArgumentParser(description="Process YAML files.")
    parser.add_argument('input_yaml', type=str, help='Input YAML file to process')
    args = parser.parse_args()

    input_yaml = args.input_yaml
    output_dir = os.path.join(os.path.dirname(input_yaml), 'yaml_files_pipe')
    os.makedirs(output_dir, exist_ok=True)
    print(f"Output directory: {output_dir}")

    with open(input_yaml, 'r') as file:
        data = yaml.safe_load(file)
        print("YAML file loaded successfully.")
    #Added for the responce section
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
    #end here
    for problem in data.get('verilog_problems', []):
        bench_name = problem.get('bench_name', 'unknown')
        output_filename = os.path.join(output_dir, f"{bench_name}_spec.yaml")
        with open(output_filename, 'w') as outfile:
            yaml.dump({
                'description': problem.get('description', ''),
                'interface': problem.get('interface', ''),
                'bench_response': problem.get('bench_response', '')
            }, outfile, Dumper=FoldedDumper, default_flow_style=False, sort_keys=False)
        print(f"File written: {output_filename}")

    print("All files have been successfully created.")

if __name__ == "__main__":
    main()

