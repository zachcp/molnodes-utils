import bpy

## obj = bpy.context.active_object
## obj
## bpy.data.objects['1FAP']
## group = obj.modifiers.get('MolecularNodes').node_group
## bpy.data.node_groups['MN_1FAP'].nodes["Color Attribute Random"]
## obj.modifiers['MolecularNodes'].node_group

def load_MN(blend_file_path =  "./assets/MN_data_file_4.2.blend"):
    bpy.ops.wm.open_mainfile(filepath=blend_file_path)
    bpy.utils.refresh_script_paths()


load_MN()


def is_molecular_node_group(node_group):
    # Check if the node group is likely from the Molecular Nodes extension
    return 'molecular' in node_group.name.lower()

def inspect_geometry_node_groups():
    node_groups = bpy.data.node_groups
    geometry_node_groups = [ng for ng in node_groups if ng.bl_idname == 'GeometryNodeTree']

    molecular_groups = []
    other_groups = []

    for group in geometry_node_groups:
        if is_molecular_node_group(group):
            molecular_groups.append(group)
        else:
            other_groups.append(group)

    return molecular_groups, other_groups

# Get Molecular Node groups and other Geometry Node groups
molecular_groups, other_groups = inspect_geometry_node_groups()

# Print Molecular Node groups
print("Molecular Node Groups:")
for group in molecular_groups:
    print(f"- {group.name}")
    # Optionally, print nodes within each group
    # for node in group.nodes:
    #     print(f"  - Node: {node.name} (Type: {node.bl_idname})")

print(f"\nTotal number of Molecular Node groups: {len(molecular_groups)}")

# Print other Geometry Node groups
print("\nOther Geometry Node Groups:")
for group in other_groups:
    print(f"- {group.name}")

print(f"\nTotal number of other Geometry Node groups: {len(other_groups)}")

def print_node_tree(node_tree, indent=""):
    for node in node_tree.nodes:
        print(f"{indent}{node.name} ({node.type})")
        # Print inputs
        for input in node.inputs:
            if input.is_linked:
                for link in input.links:
                    print(f"{indent}  ↳ Input: {input.name} <- {link.from_node.name}.{link.from_socket.name}")
            else:
                value = get_socket_value(input)
                print(f"{indent}  ↳ Input: {input.name} = {value}")
        # Print outputs
        for output in node.outputs:
            if output.is_linked:
                for link in output.links:
                    print(f"{indent}  ↳ Output: {output.name} -> {link.to_node.name}.{link.to_socket.name}")
            else:
                print(f"{indent}  ↳ Output: {output.name} (not connected)")
        # If this is a group node, print its internal node tree
        if node.type == 'GROUP':
            print(f"{indent}  Internal Node Tree:")
            print_node_tree(node.node_tree, indent + "    ")

def list_geometry_nodes():
    geometry_nodes = []
    for attr_name in dir(bpy.types):
        attr = getattr(bpy.types, attr_name)
        if isinstance(attr, type) and issubclass(attr, bpy.types.Node):
            if hasattr(attr, 'bl_rna') and hasattr(attr.bl_rna, 'name'):
                if attr.bl_rna.name.startswith('Geometry Node'):
                    geometry_nodes.append(attr)
    return geometry_nodes

# Get all Geometry Node types
geometry_node_types = list_geometry_nodes()


def find_node_by_name(name, node_tree):
    for node in node_tree.nodes:
        if node.name == name:
            return node
    return None
