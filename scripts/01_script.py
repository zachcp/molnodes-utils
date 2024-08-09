import bpy
import math
from geometry_script import *

## This defines the
@tree("Repeat Grid")
def repeat_grid(geometry: Geometry, width: Int, height: Int):
    g = grid(
        size_x=width, size_y=height, vertices_x=width, vertices_y=height
    ).mesh.mesh_to_points()
    return g.instance_on_points(instance=geometry)




# Clear existing objects
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete()

# Create a cube
bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 0))
cube = bpy.context.active_object


# Create a new Geometry Nodes modifier
modifier = cube.modifiers.new(name="GeometryNodes", type="NODES")

# Create a new node group
node_group = bpy.data.node_groups.new(name="CubeModifier", type="GeometryNodeTree")
modifier.node_group = node_group

# g = repeat_grid(cub(), 200, 400);
g = repeat_grid(node_group);

# Create input and output nodes
input_node = node_group.nodes.new("NodeGroupInput")
output_node = node_group.nodes.new("NodeGroupOutput")

# Add a Subdivision Surface node
subdiv_node = node_group.nodes.new("GeometryNodeSubdivisionSurface")
subdiv_node.inputs[2].default_value = 2  # Subdivision level

# Add a Noise Texture node
noise_node = node_group.nodes.new("ShaderNodeTexNoise")
noise_node.inputs["Scale"].default_value = 1.0
noise_node.inputs["Detail"].default_value = 10.0

# Add a Set Position node
set_position_node = node_group.nodes.new("GeometryNodeSetPosition")

# Link nodes
node_group.links.new(input_node.outputs[0], subdiv_node.inputs[0])
node_group.links.new(subdiv_node.outputs[0], set_position_node.inputs[0])
node_group.links.new(noise_node.outputs[0], set_position_node.inputs[2])
node_group.links.new(set_position_node.outputs[0], output_node.inputs[0])

# Add a light
light_data = bpy.data.lights.new(name="Light", type="SUN")
light_object = bpy.data.objects.new(name="Light", object_data=light_data)
bpy.context.collection.objects.link(light_object)
light_object.location = (5, 5, 5)

# Add a camera
camera_data = bpy.data.cameras.new(name="Camera")
camera_object = bpy.data.objects.new(name="Camera", object_data=camera_data)
bpy.context.collection.objects.link(camera_object)
camera_object.location = (5, -5, 5)
# camera_object.rotation_euler = (math.radians(60), 0, math.radians(45))
bpy.context.scene.camera = camera_object

# Set render settings
bpy.context.scene.render.engine = "CYCLES"
bpy.context.scene.render.resolution_x = 800
bpy.context.scene.render.resolution_y = 600

# Set output path
bpy.context.scene.render.filepath = "./outputs/01_render.png"

# Render
bpy.ops.render.render(write_still=True)
