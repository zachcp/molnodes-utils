#!/usr/bin/env python

#
# process_directory('/path/to/your/directory')
#
import ast
import astor
import os
import shutil


class FunctionExtractor(ast.NodeTransformer):
    def __init__(self):
        self.extracted_functions = []
        self.class_name = ""

    def visit_ClassDef(self, node):
        self.class_name = node.name
        self.generic_visit(node)
        return node

    def visit_FunctionDef(self, node):
        if node.name == 'execute':
            new_body = []
            for stmt in node.body:
                if isinstance(stmt, ast.FunctionDef):
                    # Move function to module level
                    new_func = ast.FunctionDef(
                        name=f"{self.class_name.lower()}_{stmt.name}",
                        args=stmt.args,
                        body=stmt.body,
                        decorator_list=[],
                        returns=stmt.returns
                    )
                    self.extracted_functions.append(new_func)

                    # Replace function definition with function call
                    new_body.append(ast.Assign(
                        targets=[ast.Name(id=stmt.name.strip('_'), ctx=ast.Store())],
                        value=ast.Call(
                            func=ast.Name(id=new_func.name, ctx=ast.Load()),
                            args=[],
                            keywords=[]
                        )
                    ))
                else:
                    new_body.append(stmt)
            node.body = new_body
        return node


def transform_file(input_path, output_path):
    with open(input_path, 'r') as file:
        tree = ast.parse(file.read())

    extractor = FunctionExtractor()
    new_tree = extractor.visit(tree)

    # Add extracted functions to the beginning of the module
    new_tree.body = extractor.extracted_functions + new_tree.body

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Write the transformed AST to the new file
    with open(output_path, 'w') as file:
        file.write(astor.to_source(new_tree))

def process_directory(input_directory, output_directory):
    for root, dirs, files in os.walk(input_directory):
        for file in files:
            if file.endswith('.py'):
                input_path = os.path.join(root, file)
                relative_path = os.path.relpath(input_path, input_directory)
                output_path = os.path.join(output_directory, relative_path)
                transform_file(input_path, output_path)


# class NestedFunctionTransformer(ast.NodeTransformer):
#     def __init__(self):
#         self.class_methods = []

#     def visit_ClassDef(self, node):
#         self.class_methods = []
#         self.generic_visit(node)
#         node.body = self.class_methods + node.body
#         return node

#     def visit_FunctionDef(self, node):
#         if node.name == 'execute':
#             new_body = []
#             for stmt in node.body:
#                 if isinstance(stmt, ast.FunctionDef):
#                     # Move nested function to class level
#                     new_method = ast.FunctionDef(
#                         name=stmt.name,
#                         args=ast.arguments(
#                             args=[ast.arg(arg='self', annotation=None)] + stmt.args.args,
#                             vararg=stmt.args.vararg,
#                             kwonlyargs=stmt.args.kwonlyargs,
#                             kw_defaults=stmt.args.kw_defaults,
#                             kwarg=stmt.args.kwarg,
#                             defaults=stmt.args.defaults
#                         ),
#                         body=stmt.body,
#                         decorator_list=[],
#                         returns=stmt.returns
#                     )
#                     self.class_methods.append(new_method)

#                     # Replace function definition with method call
#                     new_body.append(ast.Assign(
#                         targets=[ast.Name(id=stmt.name.strip('_'), ctx=ast.Store())],
#                         value=ast.Call(
#                             func=ast.Attribute(
#                                 value=ast.Name(id='self', ctx=ast.Load()),
#                                 attr=stmt.name,
#                                 ctx=ast.Load()
#                             ),
#                             args=[],
#                             keywords=[]
#                         )
#                     ))
#                 else:
#                     new_body.append(stmt)
#             node.body = new_body
#         return node


# def transform_file(input_path, output_path):
#     with open(input_path, 'r') as file:
#         tree = ast.parse(file.read())

#     transformer = NestedFunctionTransformer()
#     new_tree = transformer.visit(tree)

#     # Ensure the output directory exists
#     os.makedirs(os.path.dirname(output_path), exist_ok=True)

#     # Write the transformed AST to the new file
#     with open(output_path, 'w') as file:
#         file.write(astor.to_source(new_tree))

# def process_directory(input_directory, output_directory):
#     for root, dirs, files in os.walk(input_directory):
#         for file in files:
#             if file.endswith('.py'):
#                 input_path = os.path.join(root, file)
#                 relative_path = os.path.relpath(input_path, input_directory)
#                 output_path = os.path.join(output_directory, relative_path)
#                 transform_file(input_path, output_path)


# def transform_class(node):
#     new_methods = []
#     execute_method = next((m for m in node.body if isinstance(m, ast.FunctionDef) and m.name == 'execute'), None)

#     if execute_method:
#         new_body = []
#         for stmt in execute_method.body:
#             if isinstance(stmt, ast.FunctionDef):
#                 # This is a nested function definition
#                 new_method = ast.FunctionDef(
#                     name=stmt.name,
#                     args=ast.arguments(
#                         args=[ast.arg(arg='self', annotation=None)] + stmt.args.args,
#                         vararg=stmt.args.vararg,
#                         kwonlyargs=stmt.args.kwonlyargs,
#                         kw_defaults=stmt.args.kw_defaults,
#                         kwarg=stmt.args.kwarg,
#                         defaults=stmt.args.defaults
#                     ),
#                     body=stmt.body,
#                     decorator_list=[],
#                     returns=stmt.returns
#                 )
#                 new_methods.append(new_method)

#                 # Replace the original function definition with a method call
#                 new_body.append(ast.Assign(
#                     targets=[ast.Name(id=stmt.name.strip('_'), ctx=ast.Store())],
#                     value=ast.Call(
#                         func=ast.Attribute(
#                             value=ast.Name(id='self', ctx=ast.Load()),
#                             attr=stmt.name,
#                             ctx=ast.Load()
#                         ),
#                         args=[],
#                         keywords=[]
#                     )
#                 ))
#             else:
#                 new_body.append(stmt)

#         execute_method.body = new_body

#     # Add new methods to the class
#     node.body = [m for m in node.body if m != execute_method] + new_methods + [execute_method]

#     # Add type hints to all methods
#     for method in node.body:
#         if isinstance(method, ast.FunctionDef):
#             if method.name == 'execute':
#                 method.returns = ast.Name(id='Set[str]', ctx=ast.Load())
#             if not method.args.args[0].annotation:
#                 method.args.args[0].annotation = ast.Name(id='bpy.types.Context', ctx=ast.Load())

#     return node



# def transform_file(input_path, output_path):
#     with open(input_path, 'r') as file:
#         tree = ast.parse(file.read())

#     for node in ast.walk(tree):
#         if isinstance(node, ast.ClassDef):
#             is_operator = any(
#                 (isinstance(base, ast.Name) and base.id == 'Operator') or
#                 (isinstance(base, ast.Attribute) and
#                  isinstance(base.value, ast.Name) and
#                  base.value.id == 'bpy' and
#                  base.attr == 'types.Operator')
#                 for base in node.bases
#             )
#             if is_operator:
#                 transform_class(node)

#     # Ensure the output directory exists
#     os.makedirs(os.path.dirname(output_path), exist_ok=True)

#     # Write the transformed AST to the new file
#     with open(output_path, 'w') as file:
#         file.write(astor.to_source(tree))



# def process_directory(input_directory, output_directory):
#     for root, dirs, files in os.walk(input_directory):
#         for file in files:
#             if file.endswith('.py'):
#                 input_path = os.path.join(root, file)

#                 # Create the corresponding output path
#                 relative_path = os.path.relpath(input_path, input_directory)
#                 output_path = os.path.join(output_directory, relative_path)

#                 transform_file(input_path, output_path)

# Usage
input_directory = 'molnodes/molnodes'
output_directory = 'molnodes/molnodes2'

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

process_directory(input_directory, output_directory)

print(f"Transformed files have been saved to: {output_directory}")
