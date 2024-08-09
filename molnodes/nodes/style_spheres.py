bl_info = {
	"name" : "Style Spheres",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Style_Spheres(bpy.types.Operator):
	bl_idname = "node.style_spheres"
	bl_label = "Style Spheres"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _mn_world_scale node group
		def _mn_world_scale_node_group():
			_mn_world_scale = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_world_scale")

			_mn_world_scale.color_tag = 'NONE'
			_mn_world_scale.description = ""

			
			#_mn_world_scale interface
			#Socket world_scale
			world_scale_socket = _mn_world_scale.interface.new_socket(name = "world_scale", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			world_scale_socket.subtype = 'NONE'
			world_scale_socket.default_value = 0.009999999776482582
			world_scale_socket.min_value = -3.4028234663852886e+38
			world_scale_socket.max_value = 3.4028234663852886e+38
			world_scale_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_world_scale nodes
			#node Group Input
			group_input = _mn_world_scale.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Value
			value = _mn_world_scale.nodes.new("ShaderNodeValue")
			value.label = "world_scale"
			value.name = "Value"
			
			value.outputs[0].default_value = 0.009999999776482582
			#node Group Output
			group_output = _mn_world_scale.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			
			
			
			#Set locations
			group_input.location = (-200.0, 0.0)
			value.location = (0.0, 0.0)
			group_output.location = (190.0, 0.0)
			
			#Set dimensions
			group_input.width, group_input.height = 140.0, 100.0
			value.width, value.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			
			#initialize _mn_world_scale links
			#value.Value -> group_output.world_scale
			_mn_world_scale.links.new(value.outputs[0], group_output.inputs[0])
			return _mn_world_scale

		_mn_world_scale = _mn_world_scale_node_group()

		#initialize mn_units node group
		def mn_units_node_group():
			mn_units = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "MN Units")

			mn_units.color_tag = 'NONE'
			mn_units.description = ""

			
			#mn_units interface
			#Socket Angstrom
			angstrom_socket = mn_units.interface.new_socket(name = "Angstrom", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			angstrom_socket.subtype = 'NONE'
			angstrom_socket.default_value = 0.0
			angstrom_socket.min_value = -3.4028234663852886e+38
			angstrom_socket.max_value = 3.4028234663852886e+38
			angstrom_socket.attribute_domain = 'POINT'
			
			#Socket Nanometre
			nanometre_socket = mn_units.interface.new_socket(name = "Nanometre", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			nanometre_socket.subtype = 'NONE'
			nanometre_socket.default_value = 0.0
			nanometre_socket.min_value = -3.4028234663852886e+38
			nanometre_socket.max_value = 3.4028234663852886e+38
			nanometre_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket = mn_units.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket.subtype = 'NONE'
			value_socket.default_value = 3.0
			value_socket.min_value = -10000.0
			value_socket.max_value = 10000.0
			value_socket.attribute_domain = 'POINT'
			value_socket.description = "A value which will be scaled appropriately for the world"
			
			
			#initialize mn_units nodes
			#node Group Output
			group_output_1 = mn_units.nodes.new("NodeGroupOutput")
			group_output_1.name = "Group Output"
			group_output_1.is_active_output = True
			
			#node Group Input
			group_input_1 = mn_units.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			
			#node Math
			math = mn_units.nodes.new("ShaderNodeMath")
			math.name = "Math"
			math.operation = 'MULTIPLY'
			math.use_clamp = False
			
			#node Math.001
			math_001 = mn_units.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.operation = 'MULTIPLY'
			math_001.use_clamp = False
			#Value_001
			math_001.inputs[1].default_value = 10.0
			
			#node Group
			group = mn_units.nodes.new("GeometryNodeGroup")
			group.name = "Group"
			group.node_tree = _mn_world_scale
			
			
			
			
			#Set locations
			group_output_1.location = (190.0, 0.0)
			group_input_1.location = (-240.0, 0.0)
			math.location = (-60.0, 0.0)
			math_001.location = (-60.0, -160.0)
			group.location = (-304.00421142578125, -104.114013671875)
			
			#Set dimensions
			group_output_1.width, group_output_1.height = 140.0, 100.0
			group_input_1.width, group_input_1.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			group.width, group.height = 197.58424377441406, 100.0
			
			#initialize mn_units links
			#math.Value -> group_output_1.Angstrom
			mn_units.links.new(math.outputs[0], group_output_1.inputs[0])
			#group_input_1.Value -> math.Value
			mn_units.links.new(group_input_1.outputs[0], math.inputs[0])
			#group.world_scale -> math.Value
			mn_units.links.new(group.outputs[0], math.inputs[1])
			#math.Value -> math_001.Value
			mn_units.links.new(math.outputs[0], math_001.inputs[0])
			#math_001.Value -> group_output_1.Nanometre
			mn_units.links.new(math_001.outputs[0], group_output_1.inputs[1])
			return mn_units

		mn_units = mn_units_node_group()

		#initialize _mn_utils_style_spheres_points node group
		def _mn_utils_style_spheres_points_node_group():
			_mn_utils_style_spheres_points = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_utils_style_spheres_points")

			_mn_utils_style_spheres_points.color_tag = 'GEOMETRY'
			_mn_utils_style_spheres_points.description = ""

			_mn_utils_style_spheres_points.is_modifier = True
			
			#_mn_utils_style_spheres_points interface
			#Socket Point Cloud
			point_cloud_socket = _mn_utils_style_spheres_points.interface.new_socket(name = "Point Cloud", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			point_cloud_socket.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket = _mn_utils_style_spheres_points.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket.attribute_domain = 'POINT'
			atoms_socket.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket = _mn_utils_style_spheres_points.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket.attribute_domain = 'POINT'
			selection_socket.hide_value = True
			selection_socket.description = "Selection of atoms to apply this node to"
			
			#Socket Radii
			radii_socket = _mn_utils_style_spheres_points.interface.new_socket(name = "Radii", in_out='INPUT', socket_type = 'NodeSocketFloat')
			radii_socket.subtype = 'NONE'
			radii_socket.default_value = 0.800000011920929
			radii_socket.min_value = 0.0
			radii_socket.max_value = 10000.0
			radii_socket.attribute_domain = 'POINT'
			
			#Socket Material
			material_socket = _mn_utils_style_spheres_points.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial')
			material_socket.attribute_domain = 'POINT'
			material_socket.description = "Material to apply to the resulting geometry"
			
			
			#initialize _mn_utils_style_spheres_points nodes
			#node Group Input
			group_input_2 = _mn_utils_style_spheres_points.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
			#node Mesh to Points
			mesh_to_points = _mn_utils_style_spheres_points.nodes.new("GeometryNodeMeshToPoints")
			mesh_to_points.name = "Mesh to Points"
			mesh_to_points.mode = 'VERTICES'
			#Position
			mesh_to_points.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Switch
			switch = _mn_utils_style_spheres_points.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'FLOAT'
			
			#node Named Attribute
			named_attribute = _mn_utils_style_spheres_points.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'FLOAT'
			#Name
			named_attribute.inputs[0].default_value = "vdw_radii"
			
			#node Group
			group_1 = _mn_utils_style_spheres_points.nodes.new("GeometryNodeGroup")
			group_1.name = "Group"
			group_1.node_tree = mn_units
			#Input_1
			group_1.inputs[0].default_value = 0.800000011920929
			
			#node Math
			math_1 = _mn_utils_style_spheres_points.nodes.new("ShaderNodeMath")
			math_1.name = "Math"
			math_1.operation = 'MULTIPLY'
			math_1.use_clamp = False
			
			#node Group Output
			group_output_2 = _mn_utils_style_spheres_points.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Set Material
			set_material = _mn_utils_style_spheres_points.nodes.new("GeometryNodeSetMaterial")
			set_material.name = "Set Material"
			#Selection
			set_material.inputs[1].default_value = True
			
			
			
			
			#Set locations
			group_input_2.location = (-1060.0, 60.0)
			mesh_to_points.location = (-540.0, 220.0)
			switch.location = (-900.0, -100.0)
			named_attribute.location = (-1080.0, -100.0)
			group_1.location = (-1080.0, -240.0)
			math_1.location = (-720.0, 40.0)
			group_output_2.location = (-220.0, 220.0)
			set_material.location = (-380.0, 220.0)
			
			#Set dimensions
			group_input_2.width, group_input_2.height = 140.0, 100.0
			mesh_to_points.width, mesh_to_points.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			group_1.width, group_1.height = 140.0, 100.0
			math_1.width, math_1.height = 140.0, 100.0
			group_output_2.width, group_output_2.height = 140.0, 100.0
			set_material.width, set_material.height = 140.0, 100.0
			
			#initialize _mn_utils_style_spheres_points links
			#set_material.Geometry -> group_output_2.Point Cloud
			_mn_utils_style_spheres_points.links.new(set_material.outputs[0], group_output_2.inputs[0])
			#group_input_2.Selection -> mesh_to_points.Selection
			_mn_utils_style_spheres_points.links.new(group_input_2.outputs[1], mesh_to_points.inputs[1])
			#group_input_2.Radii -> math_1.Value
			_mn_utils_style_spheres_points.links.new(group_input_2.outputs[2], math_1.inputs[0])
			#math_1.Value -> mesh_to_points.Radius
			_mn_utils_style_spheres_points.links.new(math_1.outputs[0], mesh_to_points.inputs[3])
			#group_input_2.Material -> set_material.Material
			_mn_utils_style_spheres_points.links.new(group_input_2.outputs[3], set_material.inputs[2])
			#named_attribute.Attribute -> switch.Switch
			_mn_utils_style_spheres_points.links.new(named_attribute.outputs[0], switch.inputs[0])
			#named_attribute.Attribute -> switch.True
			_mn_utils_style_spheres_points.links.new(named_attribute.outputs[0], switch.inputs[2])
			#switch.Output -> math_1.Value
			_mn_utils_style_spheres_points.links.new(switch.outputs[0], math_1.inputs[1])
			#group_input_2.Atoms -> mesh_to_points.Mesh
			_mn_utils_style_spheres_points.links.new(group_input_2.outputs[0], mesh_to_points.inputs[0])
			#mesh_to_points.Points -> set_material.Geometry
			_mn_utils_style_spheres_points.links.new(mesh_to_points.outputs[0], set_material.inputs[0])
			#group_1.Angstrom -> switch.False
			_mn_utils_style_spheres_points.links.new(group_1.outputs[0], switch.inputs[1])
			return _mn_utils_style_spheres_points

		_mn_utils_style_spheres_points = _mn_utils_style_spheres_points_node_group()

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
			atoms_socket_1 = _mn_utils_style_spheres_icosphere.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_1.attribute_domain = 'POINT'
			atoms_socket_1.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket_1 = _mn_utils_style_spheres_icosphere.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_1.attribute_domain = 'POINT'
			selection_socket_1.hide_value = True
			selection_socket_1.description = "Selection of atoms to apply this node to"
			
			#Socket Radii
			radii_socket_1 = _mn_utils_style_spheres_icosphere.interface.new_socket(name = "Radii", in_out='INPUT', socket_type = 'NodeSocketFloat')
			radii_socket_1.subtype = 'NONE'
			radii_socket_1.default_value = 0.800000011920929
			radii_socket_1.min_value = 0.0
			radii_socket_1.max_value = 10000.0
			radii_socket_1.attribute_domain = 'POINT'
			radii_socket_1.description = "Scale the VDW radii of the atoms."
			
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
			material_socket_1 = _mn_utils_style_spheres_icosphere.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial')
			material_socket_1.attribute_domain = 'POINT'
			material_socket_1.description = "Material to apply to the resulting geometry"
			
			
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
			math_001_1 = _mn_utils_style_spheres_icosphere.nodes.new("ShaderNodeMath")
			math_001_1.name = "Math.001"
			math_001_1.operation = 'MINIMUM'
			math_001_1.use_clamp = False
			
			#node Group Output
			group_output_3 = _mn_utils_style_spheres_icosphere.nodes.new("NodeGroupOutput")
			group_output_3.name = "Group Output"
			group_output_3.is_active_output = True
			
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
			set_material_1 = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeSetMaterial")
			set_material_1.name = "Set Material"
			#Selection
			set_material_1.inputs[1].default_value = True
			
			#node Group Input
			group_input_3 = _mn_utils_style_spheres_icosphere.nodes.new("NodeGroupInput")
			group_input_3.name = "Group Input"
			group_input_3.outputs[2].hide = True
			group_input_3.outputs[3].hide = True
			group_input_3.outputs[4].hide = True
			group_input_3.outputs[5].hide = True
			group_input_3.outputs[6].hide = True
			
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
			named_attribute_1 = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_1.name = "Named Attribute"
			named_attribute_1.data_type = 'FLOAT'
			#Name
			named_attribute_1.inputs[0].default_value = "vdw_radii"
			
			#node Radius
			radius = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeInputRadius")
			radius.name = "Radius"
			
			#node Math
			math_2 = _mn_utils_style_spheres_icosphere.nodes.new("ShaderNodeMath")
			math_2.name = "Math"
			math_2.operation = 'MAXIMUM'
			math_2.use_clamp = False
			
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
			math_001_1.location = (-140.0, 60.0)
			group_output_3.location = (835.407470703125, 359.5566711425781)
			group_input_002.location = (320.0, 260.0)
			set_shade_smooth.location = (500.0, 340.0)
			set_material_1.location = (660.0, 340.0)
			group_input_3.location = (-160.0, 240.0)
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
			named_attribute_1.location = (-240.0, -340.0)
			radius.location = (-240.0, -480.0)
			math_2.location = (-60.0, -340.0)
			math_003.location = (100.0, -340.0)
			group_input_003.location = (-60.0, -520.0)
			math_002.location = (-140.0, -100.0)
			integer.location = (-320.0, -220.0)
			domain_size.location = (-320.0, -100.0)
			instance_on_points.location = (91.33897399902344, 216.86837768554688)
			
			#Set dimensions
			frame.width, frame.height = 800.0, 829.0
			reroute.width, reroute.height = 16.0, 100.0
			math_001_1.width, math_001_1.height = 140.0, 100.0
			group_output_3.width, group_output_3.height = 140.0, 100.0
			group_input_002.width, group_input_002.height = 140.0, 100.0
			set_shade_smooth.width, set_shade_smooth.height = 140.0, 100.0
			set_material_1.width, set_material_1.height = 140.0, 100.0
			group_input_3.width, group_input_3.height = 140.0, 100.0
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
			named_attribute_1.width, named_attribute_1.height = 140.0, 100.0
			radius.width, radius.height = 140.0, 100.0
			math_2.width, math_2.height = 140.0, 100.0
			math_003.width, math_003.height = 140.0, 100.0
			group_input_003.width, group_input_003.height = 140.0, 100.0
			math_002.width, math_002.height = 140.0, 100.0
			integer.width, integer.height = 140.0, 100.0
			domain_size.width, domain_size.height = 140.0, 100.0
			instance_on_points.width, instance_on_points.height = 140.9404296875, 100.0
			
			#initialize _mn_utils_style_spheres_icosphere links
			#set_material_1.Geometry -> group_output_3.Instances
			_mn_utils_style_spheres_icosphere.links.new(set_material_1.outputs[0], group_output_3.inputs[0])
			#set_shade_smooth.Geometry -> set_material_1.Geometry
			_mn_utils_style_spheres_icosphere.links.new(set_shade_smooth.outputs[0], set_material_1.inputs[0])
			#group_input_3.Atoms -> instance_on_points.Points
			_mn_utils_style_spheres_icosphere.links.new(group_input_3.outputs[0], instance_on_points.inputs[0])
			#reroute_001.Output -> instance_on_points.Instance
			_mn_utils_style_spheres_icosphere.links.new(reroute_001.outputs[0], instance_on_points.inputs[2])
			#ico_sphere_005.Mesh -> geometry_to_instance.Geometry
			_mn_utils_style_spheres_icosphere.links.new(ico_sphere_005.outputs[0], geometry_to_instance.inputs[0])
			#math_001_1.Value -> instance_on_points.Instance Index
			_mn_utils_style_spheres_icosphere.links.new(math_001_1.outputs[0], instance_on_points.inputs[4])
			#group_input_001.Subdivisions -> math_001_1.Value
			_mn_utils_style_spheres_icosphere.links.new(group_input_001.outputs[3], math_001_1.inputs[0])
			#reroute.Output -> domain_size.Geometry
			_mn_utils_style_spheres_icosphere.links.new(reroute.outputs[0], domain_size.inputs[0])
			#geometry_to_instance.Instances -> reroute.Input
			_mn_utils_style_spheres_icosphere.links.new(geometry_to_instance.outputs[0], reroute.inputs[0])
			#named_attribute_1.Attribute -> math_2.Value
			_mn_utils_style_spheres_icosphere.links.new(named_attribute_1.outputs[0], math_2.inputs[0])
			#radius.Radius -> math_2.Value
			_mn_utils_style_spheres_icosphere.links.new(radius.outputs[0], math_2.inputs[1])
			#group_input_002.Material -> set_material_1.Material
			_mn_utils_style_spheres_icosphere.links.new(group_input_002.outputs[5], set_material_1.inputs[2])
			#instance_on_points.Instances -> set_shade_smooth.Geometry
			_mn_utils_style_spheres_icosphere.links.new(instance_on_points.outputs[0], set_shade_smooth.inputs[0])
			#group_input_002.Shade Smooth -> set_shade_smooth.Shade Smooth
			_mn_utils_style_spheres_icosphere.links.new(group_input_002.outputs[4], set_shade_smooth.inputs[2])
			#group_input_3.Selection -> instance_on_points.Selection
			_mn_utils_style_spheres_icosphere.links.new(group_input_3.outputs[1], instance_on_points.inputs[1])
			#math_2.Value -> math_003.Value
			_mn_utils_style_spheres_icosphere.links.new(math_2.outputs[0], math_003.inputs[0])
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
			#math_002.Value -> math_001_1.Value
			_mn_utils_style_spheres_icosphere.links.new(math_002.outputs[0], math_001_1.inputs[1])
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

		#initialize style_spheres node group
		def style_spheres_node_group():
			style_spheres = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Style Spheres")

			style_spheres.color_tag = 'GEOMETRY'
			style_spheres.description = ""

			style_spheres.is_modifier = True
			
			#style_spheres interface
			#Socket Geometry
			geometry_socket = style_spheres.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket_2 = style_spheres.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_2.attribute_domain = 'POINT'
			atoms_socket_2.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket_2 = style_spheres.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_2.attribute_domain = 'POINT'
			selection_socket_2.hide_value = True
			selection_socket_2.description = "Selection of atoms to apply this style to"
			
			#Panel Sphere
			sphere_panel = style_spheres.interface.new_panel("Sphere")
			#Socket Sphere As Mesh
			sphere_as_mesh_socket = style_spheres.interface.new_socket(name = "Sphere As Mesh", in_out='INPUT', socket_type = 'NodeSocketBool', parent = sphere_panel)
			sphere_as_mesh_socket.attribute_domain = 'POINT'
			sphere_as_mesh_socket.description = "Use Eevee or Cycles compatible atoms."
			
			#Socket Sphere Radii
			sphere_radii_socket = style_spheres.interface.new_socket(name = "Sphere Radii", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = sphere_panel)
			sphere_radii_socket.subtype = 'NONE'
			sphere_radii_socket.default_value = 0.800000011920929
			sphere_radii_socket.min_value = 0.0
			sphere_radii_socket.max_value = 2.0
			sphere_radii_socket.attribute_domain = 'POINT'
			sphere_radii_socket.description = "Scale the `vdw_radii` of the atoms."
			
			#Socket Sphere Subdivisions
			sphere_subdivisions_socket = style_spheres.interface.new_socket(name = "Sphere Subdivisions", in_out='INPUT', socket_type = 'NodeSocketInt', parent = sphere_panel)
			sphere_subdivisions_socket.subtype = 'NONE'
			sphere_subdivisions_socket.default_value = 2
			sphere_subdivisions_socket.min_value = 0
			sphere_subdivisions_socket.max_value = 5
			sphere_subdivisions_socket.attribute_domain = 'POINT'
			sphere_subdivisions_socket.description = "Subdivisions for Eevee compatible atoms."
			
			
			#Panel Material
			material_panel = style_spheres.interface.new_panel("Material", default_closed=True)
			#Socket Shade Smooth
			shade_smooth_socket_1 = style_spheres.interface.new_socket(name = "Shade Smooth", in_out='INPUT', socket_type = 'NodeSocketBool', parent = material_panel)
			shade_smooth_socket_1.attribute_domain = 'POINT'
			shade_smooth_socket_1.description = "Apply smooth shading to the created geometry"
			
			#Socket Material
			material_socket_2 = style_spheres.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial', parent = material_panel)
			material_socket_2.attribute_domain = 'POINT'
			material_socket_2.description = "Material to apply to the resulting geometry"
			
			
			
			#initialize style_spheres nodes
			#node Group Input
			group_input_4 = style_spheres.nodes.new("NodeGroupInput")
			group_input_4.name = "Group Input"
			
			#node Group Output
			group_output_4 = style_spheres.nodes.new("NodeGroupOutput")
			group_output_4.name = "Group Output"
			group_output_4.is_active_output = True
			
			#node Join Geometry
			join_geometry = style_spheres.nodes.new("GeometryNodeJoinGeometry")
			join_geometry.name = "Join Geometry"
			
			#node Separate Geometry
			separate_geometry = style_spheres.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry.name = "Separate Geometry"
			separate_geometry.domain = 'POINT'
			
			#node Group.014
			group_014 = style_spheres.nodes.new("GeometryNodeGroup")
			group_014.name = "Group.014"
			group_014.node_tree = _mn_utils_style_spheres_points
			
			#node Group.026
			group_026 = style_spheres.nodes.new("GeometryNodeGroup")
			group_026.name = "Group.026"
			group_026.node_tree = _mn_utils_style_spheres_icosphere
			
			#node Realize Instances
			realize_instances = style_spheres.nodes.new("GeometryNodeRealizeInstances")
			realize_instances.name = "Realize Instances"
			#Selection
			realize_instances.inputs[1].default_value = True
			#Realize All
			realize_instances.inputs[2].default_value = True
			#Depth
			realize_instances.inputs[3].default_value = 0
			
			
			
			
			#Set locations
			group_input_4.location = (-679.2061157226562, -54.561466217041016)
			group_output_4.location = (480.0, 40.0)
			join_geometry.location = (320.0, 40.0)
			separate_geometry.location = (-420.0, 80.0)
			group_014.location = (-200.0, -200.0)
			group_026.location = (-200.0, 60.0)
			realize_instances.location = (100.0, 60.0)
			
			#Set dimensions
			group_input_4.width, group_input_4.height = 140.0, 100.0
			group_output_4.width, group_output_4.height = 140.0, 100.0
			join_geometry.width, join_geometry.height = 140.0, 100.0
			separate_geometry.width, separate_geometry.height = 140.0, 100.0
			group_014.width, group_014.height = 277.9979248046875, 100.0
			group_026.width, group_026.height = 278.0207824707031, 100.0
			realize_instances.width, realize_instances.height = 140.0, 100.0
			
			#initialize style_spheres links
			#group_input_4.Atoms -> separate_geometry.Geometry
			style_spheres.links.new(group_input_4.outputs[0], separate_geometry.inputs[0])
			#group_input_4.Selection -> group_014.Selection
			style_spheres.links.new(group_input_4.outputs[1], group_014.inputs[1])
			#group_input_4.Selection -> group_026.Selection
			style_spheres.links.new(group_input_4.outputs[1], group_026.inputs[1])
			#group_input_4.Sphere As Mesh -> separate_geometry.Selection
			style_spheres.links.new(group_input_4.outputs[2], separate_geometry.inputs[1])
			#group_input_4.Sphere Radii -> group_014.Radii
			style_spheres.links.new(group_input_4.outputs[3], group_014.inputs[2])
			#group_input_4.Sphere Radii -> group_026.Radii
			style_spheres.links.new(group_input_4.outputs[3], group_026.inputs[2])
			#group_input_4.Sphere Subdivisions -> group_026.Subdivisions
			style_spheres.links.new(group_input_4.outputs[4], group_026.inputs[3])
			#group_input_4.Shade Smooth -> group_026.Shade Smooth
			style_spheres.links.new(group_input_4.outputs[5], group_026.inputs[4])
			#group_input_4.Material -> group_014.Material
			style_spheres.links.new(group_input_4.outputs[6], group_014.inputs[3])
			#group_input_4.Material -> group_026.Material
			style_spheres.links.new(group_input_4.outputs[6], group_026.inputs[5])
			#join_geometry.Geometry -> group_output_4.Geometry
			style_spheres.links.new(join_geometry.outputs[0], group_output_4.inputs[0])
			#realize_instances.Geometry -> join_geometry.Geometry
			style_spheres.links.new(realize_instances.outputs[0], join_geometry.inputs[0])
			#group_026.Instances -> realize_instances.Geometry
			style_spheres.links.new(group_026.outputs[0], realize_instances.inputs[0])
			#separate_geometry.Inverted -> group_014.Atoms
			style_spheres.links.new(separate_geometry.outputs[1], group_014.inputs[0])
			#separate_geometry.Selection -> group_026.Atoms
			style_spheres.links.new(separate_geometry.outputs[0], group_026.inputs[0])
			#group_014.Point Cloud -> join_geometry.Geometry
			style_spheres.links.new(group_014.outputs[0], join_geometry.inputs[0])
			return style_spheres

		style_spheres = style_spheres_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Style Spheres", type = 'NODES')
		mod.node_group = style_spheres
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Style_Spheres.bl_idname)
			
def register():
	bpy.utils.register_class(Style_Spheres)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Style_Spheres)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
