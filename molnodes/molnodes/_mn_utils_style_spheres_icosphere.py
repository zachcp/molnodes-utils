bl_info = {
	"name" : ".MN_utils_style_spheres_icosphere",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _MN_utils_style_spheres_icosphere(bpy.types.Operator):
	bl_idname = "node._mn_utils_style_spheres_icosphere"
	bl_label = ".MN_utils_style_spheres_icosphere"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _mn_utils_style_spheres_icosphere node group
		def _mn_utils_style_spheres_icosphere_node_group():
			_mn_utils_style_spheres_icosphere = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_utils_style_spheres_icosphere")

			_mn_utils_style_spheres_icosphere.color_tag = 'GEOMETRY'
			_mn_utils_style_spheres_icosphere.description = ""

			_mn_utils_style_spheres_icosphere.is_modifier = True
			
			#_mn_utils_style_spheres_icosphere interface
			#Socket Instances
			instances_socket = _mn_utils_style_spheres_icosphere.interface.new_socket(name = "Instances", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			instances_socket.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket = _mn_utils_style_spheres_icosphere.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket.attribute_domain = 'POINT'
			atoms_socket.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket = _mn_utils_style_spheres_icosphere.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket.attribute_domain = 'POINT'
			selection_socket.hide_value = True
			selection_socket.description = "Selection of atoms to apply this node to"
			
			#Socket Radii
			radii_socket = _mn_utils_style_spheres_icosphere.interface.new_socket(name = "Radii", in_out='INPUT', socket_type = 'NodeSocketFloat')
			radii_socket.subtype = 'NONE'
			radii_socket.default_value = 0.800000011920929
			radii_socket.min_value = 0.0
			radii_socket.max_value = 10000.0
			radii_socket.attribute_domain = 'POINT'
			radii_socket.description = "Scale the VDW radii of the atoms."
			
			#Socket Subdivisions
			subdivisions_socket = _mn_utils_style_spheres_icosphere.interface.new_socket(name = "Subdivisions", in_out='INPUT', socket_type = 'NodeSocketInt')
			subdivisions_socket.subtype = 'NONE'
			subdivisions_socket.default_value = 2
			subdivisions_socket.min_value = 0
			subdivisions_socket.max_value = 5
			subdivisions_socket.attribute_domain = 'POINT'
			
			#Socket Shade Smooth
			shade_smooth_socket = _mn_utils_style_spheres_icosphere.interface.new_socket(name = "Shade Smooth", in_out='INPUT', socket_type = 'NodeSocketBool')
			shade_smooth_socket.attribute_domain = 'POINT'
			shade_smooth_socket.description = "Apply smooth shading to the created geometry"
			
			#Socket Material
			material_socket = _mn_utils_style_spheres_icosphere.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial')
			material_socket.attribute_domain = 'POINT'
			material_socket.description = "Material to apply to the resulting geometry"
			
			
			#initialize _mn_utils_style_spheres_icosphere nodes
			#node Frame
			frame = _mn_utils_style_spheres_icosphere.nodes.new("NodeFrame")
			frame.label = "Different Levels of Detail."
			frame.name = "Frame"
			frame.label_size = 20
			frame.shrink = True
			
			#node Reroute
			reroute = _mn_utils_style_spheres_icosphere.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Math.001
			math_001 = _mn_utils_style_spheres_icosphere.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.operation = 'MINIMUM'
			math_001.use_clamp = False
			
			#node Group Output
			group_output = _mn_utils_style_spheres_icosphere.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input.002
			group_input_002 = _mn_utils_style_spheres_icosphere.nodes.new("NodeGroupInput")
			group_input_002.name = "Group Input.002"
			group_input_002.outputs[0].hide = True
			group_input_002.outputs[1].hide = True
			group_input_002.outputs[2].hide = True
			group_input_002.outputs[3].hide = True
			group_input_002.outputs[6].hide = True
			
			#node Set Shade Smooth
			set_shade_smooth = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeSetShadeSmooth")
			set_shade_smooth.name = "Set Shade Smooth"
			set_shade_smooth.domain = 'FACE'
			#Selection
			set_shade_smooth.inputs[1].default_value = True
			
			#node Set Material
			set_material = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeSetMaterial")
			set_material.name = "Set Material"
			#Selection
			set_material.inputs[1].default_value = True
			
			#node Group Input
			group_input = _mn_utils_style_spheres_icosphere.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			group_input.outputs[2].hide = True
			group_input.outputs[3].hide = True
			group_input.outputs[4].hide = True
			group_input.outputs[5].hide = True
			group_input.outputs[6].hide = True
			
			#node Reroute.001
			reroute_001 = _mn_utils_style_spheres_icosphere.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			#node Group Input.001
			group_input_001 = _mn_utils_style_spheres_icosphere.nodes.new("NodeGroupInput")
			group_input_001.name = "Group Input.001"
			group_input_001.outputs[0].hide = True
			group_input_001.outputs[1].hide = True
			group_input_001.outputs[2].hide = True
			group_input_001.outputs[4].hide = True
			group_input_001.outputs[5].hide = True
			group_input_001.outputs[6].hide = True
			
			#node Ico Sphere.001
			ico_sphere_001 = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeMeshIcoSphere")
			ico_sphere_001.name = "Ico Sphere.001"
			#Radius
			ico_sphere_001.inputs[0].default_value = 1.0
			#Subdivisions
			ico_sphere_001.inputs[1].default_value = 1
			
			#node Ico Sphere.002
			ico_sphere_002 = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeMeshIcoSphere")
			ico_sphere_002.name = "Ico Sphere.002"
			#Radius
			ico_sphere_002.inputs[0].default_value = 1.0
			#Subdivisions
			ico_sphere_002.inputs[1].default_value = 2
			
			#node Ico Sphere.003
			ico_sphere_003 = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeMeshIcoSphere")
			ico_sphere_003.name = "Ico Sphere.003"
			#Radius
			ico_sphere_003.inputs[0].default_value = 1.0
			#Subdivisions
			ico_sphere_003.inputs[1].default_value = 3
			
			#node Geometry to Instance
			geometry_to_instance = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeGeometryToInstance")
			geometry_to_instance.name = "Geometry to Instance"
			
			#node Ico Sphere.004
			ico_sphere_004 = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeMeshIcoSphere")
			ico_sphere_004.name = "Ico Sphere.004"
			#Radius
			ico_sphere_004.inputs[0].default_value = 1.0
			#Subdivisions
			ico_sphere_004.inputs[1].default_value = 4
			
			#node Ico Sphere.005
			ico_sphere_005 = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeMeshIcoSphere")
			ico_sphere_005.name = "Ico Sphere.005"
			#Radius
			ico_sphere_005.inputs[0].default_value = 1.0
			#Subdivisions
			ico_sphere_005.inputs[1].default_value = 5
			
			#node Reroute.002
			reroute_002 = _mn_utils_style_spheres_icosphere.nodes.new("NodeReroute")
			reroute_002.name = "Reroute.002"
			#node Transform Geometry
			transform_geometry = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeTransform")
			transform_geometry.name = "Transform Geometry"
			transform_geometry.mode = 'COMPONENTS'
			#Translation
			transform_geometry.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Rotation
			transform_geometry.inputs[2].default_value = (0.7853981852531433, 0.7853981852531433, 0.0)
			#Scale
			transform_geometry.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Cube
			cube = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeMeshCube")
			cube.name = "Cube"
			#Size
			cube.inputs[0].default_value = (1.0, 1.0, 1.0)
			#Vertices X
			cube.inputs[1].default_value = 2
			#Vertices Y
			cube.inputs[2].default_value = 2
			#Vertices Z
			cube.inputs[3].default_value = 2
			
			#node Named Attribute
			named_attribute = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'FLOAT'
			#Name
			named_attribute.inputs[0].default_value = "vdw_radii"
			
			#node Radius
			radius = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeInputRadius")
			radius.name = "Radius"
			
			#node Math
			math = _mn_utils_style_spheres_icosphere.nodes.new("ShaderNodeMath")
			math.name = "Math"
			math.operation = 'MAXIMUM'
			math.use_clamp = False
			
			#node Math.003
			math_003 = _mn_utils_style_spheres_icosphere.nodes.new("ShaderNodeMath")
			math_003.name = "Math.003"
			math_003.operation = 'MULTIPLY'
			math_003.use_clamp = False
			
			#node Group Input.003
			group_input_003 = _mn_utils_style_spheres_icosphere.nodes.new("NodeGroupInput")
			group_input_003.name = "Group Input.003"
			group_input_003.outputs[0].hide = True
			group_input_003.outputs[1].hide = True
			group_input_003.outputs[3].hide = True
			group_input_003.outputs[4].hide = True
			group_input_003.outputs[5].hide = True
			group_input_003.outputs[6].hide = True
			
			#node Math.002
			math_002 = _mn_utils_style_spheres_icosphere.nodes.new("ShaderNodeMath")
			math_002.name = "Math.002"
			math_002.operation = 'ADD'
			math_002.use_clamp = False
			
			#node Integer
			integer = _mn_utils_style_spheres_icosphere.nodes.new("FunctionNodeInputInt")
			integer.name = "Integer"
			integer.integer = -1
			
			#node Domain Size
			domain_size = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeAttributeDomainSize")
			domain_size.name = "Domain Size"
			domain_size.component = 'INSTANCES'
			
			#node Instance on Points
			instance_on_points = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeInstanceOnPoints")
			instance_on_points.name = "Instance on Points"
			#Pick Instance
			instance_on_points.inputs[3].default_value = True
			#Rotation
			instance_on_points.inputs[5].default_value = (0.0, 0.0, 0.0)
			
			
			
			#Set parents
			ico_sphere_001.parent = frame
			ico_sphere_002.parent = frame
			ico_sphere_003.parent = frame
			geometry_to_instance.parent = frame
			ico_sphere_004.parent = frame
			ico_sphere_005.parent = frame
			reroute_002.parent = frame
			transform_geometry.parent = frame
			cube.parent = frame
			
			#Set locations
			frame.location = (0.0, 0.0)
			reroute.location = (-560.0, -40.0)
			math_001.location = (-140.0, 60.0)
			group_output.location = (835.407470703125, 359.5566711425781)
			group_input_002.location = (320.0, 260.0)
			set_shade_smooth.location = (500.0, 340.0)
			set_material.location = (660.0, 340.0)
			group_input.location = (-160.0, 240.0)
			reroute_001.location = (-480.0, 120.0)
			group_input_001.location = (-300.0, 60.0)
			ico_sphere_001.location = (-1180.0, 120.0)
			ico_sphere_002.location = (-1180.0, -20.0)
			ico_sphere_003.location = (-1180.0, -160.0)
			geometry_to_instance.location = (-940.0, 0.0)
			ico_sphere_004.location = (-1180.0, -300.0)
			ico_sphere_005.location = (-1180.0, -440.0)
			reroute_002.location = (-1040.0, 160.0)
			transform_geometry.location = (-1360.0, 200.0)
			cube.location = (-1520.0, 200.0)
			named_attribute.location = (-240.0, -340.0)
			radius.location = (-240.0, -480.0)
			math.location = (-60.0, -340.0)
			math_003.location = (100.0, -340.0)
			group_input_003.location = (-60.0, -520.0)
			math_002.location = (-140.0, -100.0)
			integer.location = (-320.0, -220.0)
			domain_size.location = (-320.0, -100.0)
			instance_on_points.location = (91.33897399902344, 216.86837768554688)
			
			#Set dimensions
			frame.width, frame.height = 800.0, 829.0
			reroute.width, reroute.height = 16.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			group_input_002.width, group_input_002.height = 140.0, 100.0
			set_shade_smooth.width, set_shade_smooth.height = 140.0, 100.0
			set_material.width, set_material.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			group_input_001.width, group_input_001.height = 140.0, 100.0
			ico_sphere_001.width, ico_sphere_001.height = 140.0, 100.0
			ico_sphere_002.width, ico_sphere_002.height = 140.0, 100.0
			ico_sphere_003.width, ico_sphere_003.height = 140.0, 100.0
			geometry_to_instance.width, geometry_to_instance.height = 160.0, 100.0
			ico_sphere_004.width, ico_sphere_004.height = 140.0, 100.0
			ico_sphere_005.width, ico_sphere_005.height = 140.0, 100.0
			reroute_002.width, reroute_002.height = 16.0, 100.0
			transform_geometry.width, transform_geometry.height = 140.0, 100.0
			cube.width, cube.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			radius.width, radius.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			math_003.width, math_003.height = 140.0, 100.0
			group_input_003.width, group_input_003.height = 140.0, 100.0
			math_002.width, math_002.height = 140.0, 100.0
			integer.width, integer.height = 140.0, 100.0
			domain_size.width, domain_size.height = 140.0, 100.0
			instance_on_points.width, instance_on_points.height = 140.9404296875, 100.0
			
			#initialize _mn_utils_style_spheres_icosphere links
			#set_material.Geometry -> group_output.Instances
			_mn_utils_style_spheres_icosphere.links.new(set_material.outputs[0], group_output.inputs[0])
			#set_shade_smooth.Geometry -> set_material.Geometry
			_mn_utils_style_spheres_icosphere.links.new(set_shade_smooth.outputs[0], set_material.inputs[0])
			#group_input.Atoms -> instance_on_points.Points
			_mn_utils_style_spheres_icosphere.links.new(group_input.outputs[0], instance_on_points.inputs[0])
			#reroute_001.Output -> instance_on_points.Instance
			_mn_utils_style_spheres_icosphere.links.new(reroute_001.outputs[0], instance_on_points.inputs[2])
			#ico_sphere_005.Mesh -> geometry_to_instance.Geometry
			_mn_utils_style_spheres_icosphere.links.new(ico_sphere_005.outputs[0], geometry_to_instance.inputs[0])
			#math_001.Value -> instance_on_points.Instance Index
			_mn_utils_style_spheres_icosphere.links.new(math_001.outputs[0], instance_on_points.inputs[4])
			#group_input_001.Subdivisions -> math_001.Value
			_mn_utils_style_spheres_icosphere.links.new(group_input_001.outputs[3], math_001.inputs[0])
			#reroute.Output -> domain_size.Geometry
			_mn_utils_style_spheres_icosphere.links.new(reroute.outputs[0], domain_size.inputs[0])
			#geometry_to_instance.Instances -> reroute.Input
			_mn_utils_style_spheres_icosphere.links.new(geometry_to_instance.outputs[0], reroute.inputs[0])
			#named_attribute.Attribute -> math.Value
			_mn_utils_style_spheres_icosphere.links.new(named_attribute.outputs[0], math.inputs[0])
			#radius.Radius -> math.Value
			_mn_utils_style_spheres_icosphere.links.new(radius.outputs[0], math.inputs[1])
			#group_input_002.Material -> set_material.Material
			_mn_utils_style_spheres_icosphere.links.new(group_input_002.outputs[5], set_material.inputs[2])
			#instance_on_points.Instances -> set_shade_smooth.Geometry
			_mn_utils_style_spheres_icosphere.links.new(instance_on_points.outputs[0], set_shade_smooth.inputs[0])
			#group_input_002.Shade Smooth -> set_shade_smooth.Shade Smooth
			_mn_utils_style_spheres_icosphere.links.new(group_input_002.outputs[4], set_shade_smooth.inputs[2])
			#group_input.Selection -> instance_on_points.Selection
			_mn_utils_style_spheres_icosphere.links.new(group_input.outputs[1], instance_on_points.inputs[1])
			#math.Value -> math_003.Value
			_mn_utils_style_spheres_icosphere.links.new(math.outputs[0], math_003.inputs[0])
			#group_input_003.Radii -> math_003.Value
			_mn_utils_style_spheres_icosphere.links.new(group_input_003.outputs[2], math_003.inputs[1])
			#reroute.Output -> reroute_001.Input
			_mn_utils_style_spheres_icosphere.links.new(reroute.outputs[0], reroute_001.inputs[0])
			#math_003.Value -> instance_on_points.Scale
			_mn_utils_style_spheres_icosphere.links.new(math_003.outputs[0], instance_on_points.inputs[6])
			#cube.Mesh -> transform_geometry.Geometry
			_mn_utils_style_spheres_icosphere.links.new(cube.outputs[0], transform_geometry.inputs[0])
			#transform_geometry.Geometry -> reroute_002.Input
			_mn_utils_style_spheres_icosphere.links.new(transform_geometry.outputs[0], reroute_002.inputs[0])
			#domain_size.Instance Count -> math_002.Value
			_mn_utils_style_spheres_icosphere.links.new(domain_size.outputs[5], math_002.inputs[0])
			#integer.Integer -> math_002.Value
			_mn_utils_style_spheres_icosphere.links.new(integer.outputs[0], math_002.inputs[1])
			#math_002.Value -> math_001.Value
			_mn_utils_style_spheres_icosphere.links.new(math_002.outputs[0], math_001.inputs[1])
			#ico_sphere_004.Mesh -> geometry_to_instance.Geometry
			_mn_utils_style_spheres_icosphere.links.new(ico_sphere_004.outputs[0], geometry_to_instance.inputs[0])
			#ico_sphere_003.Mesh -> geometry_to_instance.Geometry
			_mn_utils_style_spheres_icosphere.links.new(ico_sphere_003.outputs[0], geometry_to_instance.inputs[0])
			#ico_sphere_002.Mesh -> geometry_to_instance.Geometry
			_mn_utils_style_spheres_icosphere.links.new(ico_sphere_002.outputs[0], geometry_to_instance.inputs[0])
			#ico_sphere_001.Mesh -> geometry_to_instance.Geometry
			_mn_utils_style_spheres_icosphere.links.new(ico_sphere_001.outputs[0], geometry_to_instance.inputs[0])
			#reroute_002.Output -> geometry_to_instance.Geometry
			_mn_utils_style_spheres_icosphere.links.new(reroute_002.outputs[0], geometry_to_instance.inputs[0])
			return _mn_utils_style_spheres_icosphere

		_mn_utils_style_spheres_icosphere = _mn_utils_style_spheres_icosphere_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".MN_utils_style_spheres_icosphere", type = 'NODES')
		mod.node_group = _mn_utils_style_spheres_icosphere
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_MN_utils_style_spheres_icosphere.bl_idname)
			
def register():
	bpy.utils.register_class(_MN_utils_style_spheres_icosphere)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_MN_utils_style_spheres_icosphere)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
