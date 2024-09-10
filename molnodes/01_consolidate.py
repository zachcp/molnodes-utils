import os
import ast
import astor
from collections import defaultdict

def get_function_content(node):
    return astor.to_source(node).strip()

def scan_for_functions(directory):
    functions = defaultdict(list)
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    try:
                        tree = ast.parse(f.read())
                        for node in ast.walk(tree):
                            if isinstance(node, ast.FunctionDef):
                                content = get_function_content(node)
                                functions[content].append((file_path, node.name))
                    except SyntaxError:
                        print(f"Syntax error in file: {file_path}")
    return functions

def find_duplicates(functions):
    return {content: locations for content, locations in functions.items() if len(locations) > 1}

def create_consolidated_file(duplicates, output_file):
    with open(output_file, 'w') as f:
        for content, locations in duplicates.items():
            f.write(f"# Function from: {', '.join(loc[0] for loc in locations)}\n")
            f.write(f"def {locations[0][1]}:\n")
            f.write(content)
            f.write("\n\n")

def main():
    directory = "molnodes/molnodes2"
    functions = scan_for_functions(directory)
    duplicates = find_duplicates(functions)

    print("Duplicate functions found:")
    for content, locations in duplicates.items():
        print(f"\nFunction: {locations[0][1]}")
        print("Found in:")
        for loc in locations:
            print(f"  - {loc[0]}")

    create_consolidated = input("Create a consolidated file with unique functions? (y/n): ").lower() == 'y'
    if create_consolidated:
        output_file = "molnodes/molnodes3/consolidated_functions.py"
        create_consolidated_file(duplicates, output_file)
        print(f"Consolidated functions written to: {output_file}")

if __name__ == "__main__":
    main()
