import os
import shutil
import tempfile
import zipfile
import bpy
import molecularnodes
import nodetopython
from molecularnodes.entities.molecule import Molecule
from molecularnodes.entities.molecule.ui import load_local


# need this to load the NTP
try:
    nodetopython.register()
    molecularnodes.register()
except:
    pass


def fix_name(name):
    return name.replace(".", "_").replace(" ", "_").lower()


def convert_Molecular_Nodes_to_python(
    blendfile="assets/MN_data_file_4.2.blend",
    output_dir="molnodes/molnodes",
    version=(4, 2, 0),
):
    """
    using NodetoPython to create python classes for each GemoetryNodeTree in MolecularNodes

    # geometry_nodes_object = create_geometry_nodes_object()
    # print(f"Created Geometry Nodes object: {geometry_nodes_object.name}")
    #
    # mol1 = load_local("assets/1BNA.pdb", name="1BNA")
    # mol1.create_object()
    #
    # Save set_color
    # bpy.ops.node.ntp_geo_nodes(geo_nodes_group_name="Set Color")
    # Save polymers
    # bpy.ops.node.ntp_geo_nodes(geo_nodes_group_name="Separate Polymers")

    """
    # Load the .blend file
    bpy.ops.wm.open_mainfile(filepath=blendfile)
    # set the required options
    # bpy.context.scene.ntp_options
    # set required values
    bpy.context.scene.ntp_options.mode = "ADDON"
    bpy.context.scene.ntp_options.author_name = "Brady Johnson"
    bpy.context.scene.ntp_options.version = version
    bpy.context.scene.ntp_options.license = "SPDX:MIT"
    bpy.context.scene.ntp_options.menu_id = "NODE_MT_add"
    # list MN Nodes
    node_groups = bpy.data.node_groups
    molecular_nodes = [ng for ng in node_groups if ng.bl_idname == "GeometryNodeTree"]
    # NodetoPython creates a single output
    # for each of the
    print("Molecular Nodes:")
    temp_dir = tempfile.mkdtemp()

    classes = []
    for node in molecular_nodes:
        name = fix_name(node.name)
        try:
            # print(f"- {node.bl_description} (ID: {name})")
            bpy.context.scene.ntp_options.dir_path = temp_dir
            # bpy.context.scene.ntp_options.description = "Test Description"
            bpy.ops.node.ntp_geo_nodes(geo_nodes_group_name=node.name)
            zip_path = os.path.join(temp_dir, f"{name}.zip")
            if os.path.exists(zip_path):
                with zipfile.ZipFile(zip_path, "r") as zip_ref:
                    zip_ref.extract(f"{name}/__init__.py", temp_dir)
                    os.rename(
                        os.path.join(temp_dir, name, "__init__.py"),
                        f"{output_dir}/{name}.py",
                    )
            # we want to aggregate the tidy name, `name`, as well as the name used by the nodes
            classes.append((name, node.name))
        except:
            raise ValueError(f"Issue with {name}")
    shutil.rmtree(temp_dir)

    with open(f'{output_dir}/__init__.py', 'w') as f:
        for name, nodename in classes:
            f.write(f"from {name} import {nodename}\n")

convert_Molecular_Nodes_to_python()
