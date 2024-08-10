bl_info = {
	"name" : "Style Sticks",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Style_Sticks(bpy.types.Operator):
	bl_idname = "node.style_sticks"
	bl_label = "Style Sticks"
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

		#initialize _mn_utils_style_sticks node group
		def _mn_utils_style_sticks_node_group():
			_mn_utils_style_sticks = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_utils_style_sticks")

			_mn_utils_style_sticks.color_tag = 'GEOMETRY'
			_mn_utils_style_sticks.description = ""

			_mn_utils_style_sticks.is_modifier = True
			
			#_mn_utils_style_sticks interface
			#Socket Geometry
			geometry_socket_1 = _mn_utils_style_sticks.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_1.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket_3 = _mn_utils_style_sticks.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_3.attribute_domain = 'POINT'
			atoms_socket_3.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket_3 = _mn_utils_style_sticks.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_3.attribute_domain = 'POINT'
			selection_socket_3.hide_value = True
			selection_socket_3.description = "Selection of atoms to apply this node to"
			
			#Socket Radius
			radius_socket = _mn_utils_style_sticks.interface.new_socket(name = "Radius", in_out='INPUT', socket_type = 'NodeSocketFloat')
			radius_socket.subtype = 'NONE'
			radius_socket.default_value = 0.30000001192092896
			radius_socket.min_value = 0.0
			radius_socket.max_value = 1.0
			radius_socket.attribute_domain = 'POINT'
			radius_socket.description = "Radius of the bond mesh."
			
			#Socket Resolution
			resolution_socket = _mn_utils_style_sticks.interface.new_socket(name = "Resolution", in_out='INPUT', socket_type = 'NodeSocketInt')
			resolution_socket.subtype = 'NONE'
			resolution_socket.default_value = 6
			resolution_socket.min_value = 3
			resolution_socket.max_value = 512
			resolution_socket.attribute_domain = 'POINT'
			resolution_socket.description = "Resolution of the created bond cylinders."
			
			#Socket Fill Caps
			fill_caps_socket = _mn_utils_style_sticks.interface.new_socket(name = "Fill Caps", in_out='INPUT', socket_type = 'NodeSocketBool')
			fill_caps_socket.attribute_domain = 'POINT'
			fill_caps_socket.description = "Fill the caps at each end of the bonds."
			
			#Socket Interpolate Color
			interpolate_color_socket = _mn_utils_style_sticks.interface.new_socket(name = "Interpolate Color", in_out='INPUT', socket_type = 'NodeSocketBool')
			interpolate_color_socket.attribute_domain = 'POINT'
			
			#Panel Material
			material_panel_1 = _mn_utils_style_sticks.interface.new_panel("Material")
			#Socket Shade Smooth
			shade_smooth_socket_2 = _mn_utils_style_sticks.interface.new_socket(name = "Shade Smooth", in_out='INPUT', socket_type = 'NodeSocketBool', parent = material_panel_1)
			shade_smooth_socket_2.attribute_domain = 'POINT'
			shade_smooth_socket_2.description = "Apply smooth shading to the created geometry"
			
			#Socket Material
			material_socket_3 = _mn_utils_style_sticks.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial', parent = material_panel_1)
			material_socket_3.attribute_domain = 'POINT'
			material_socket_3.description = "Material to apply to the resulting geometry"
			
			
			
			#initialize _mn_utils_style_sticks nodes
			#node Frame
			frame_1 = _mn_utils_style_sticks.nodes.new("NodeFrame")
			frame_1.label = "Bonds to Mesh"
			frame_1.name = "Frame"
			frame_1.label_size = 20
			frame_1.shrink = True
			
			#node Frame.001
			frame_001 = _mn_utils_style_sticks.nodes.new("NodeFrame")
			frame_001.label = "Capture index for pulling colors from atoms"
			frame_001.name = "Frame.001"
			frame_001.label_size = 20
			frame_001.shrink = True
			
			#node Frame.003
			frame_003 = _mn_utils_style_sticks.nodes.new("NodeFrame")
			frame_003.label = "Set up materials"
			frame_003.name = "Frame.003"
			frame_003.label_size = 20
			frame_003.shrink = True
			
			#node Frame.002
			frame_002 = _mn_utils_style_sticks.nodes.new("NodeFrame")
			frame_002.label = "Store correct color on the new bond mesh"
			frame_002.name = "Frame.002"
			frame_002.label_size = 20
			frame_002.shrink = True
			
			#node Mesh to Curve
			mesh_to_curve = _mn_utils_style_sticks.nodes.new("GeometryNodeMeshToCurve")
			mesh_to_curve.name = "Mesh to Curve"
			#Selection
			mesh_to_curve.inputs[1].default_value = True
			
			#node Set Curve Radius
			set_curve_radius = _mn_utils_style_sticks.nodes.new("GeometryNodeSetCurveRadius")
			set_curve_radius.name = "Set Curve Radius"
			#Selection
			set_curve_radius.inputs[1].default_value = True
			
			#node Subdivide Curve
			subdivide_curve = _mn_utils_style_sticks.nodes.new("GeometryNodeSubdivideCurve")
			subdivide_curve.name = "Subdivide Curve"
			#Cuts
			subdivide_curve.inputs[1].default_value = 1
			
			#node Group
			group_2 = _mn_utils_style_sticks.nodes.new("GeometryNodeGroup")
			group_2.name = "Group"
			group_2.node_tree = mn_units
			
			#node Group Input.002
			group_input_002_1 = _mn_utils_style_sticks.nodes.new("NodeGroupInput")
			group_input_002_1.name = "Group Input.002"
			group_input_002_1.outputs[0].hide = True
			group_input_002_1.outputs[3].hide = True
			group_input_002_1.outputs[5].hide = True
			group_input_002_1.outputs[6].hide = True
			group_input_002_1.outputs[7].hide = True
			group_input_002_1.outputs[8].hide = True
			
			#node Curve Circle
			curve_circle = _mn_utils_style_sticks.nodes.new("GeometryNodeCurvePrimitiveCircle")
			curve_circle.name = "Curve Circle"
			curve_circle.mode = 'RADIUS'
			#Radius
			curve_circle.inputs[4].default_value = 1.0
			
			#node Curve to Mesh
			curve_to_mesh = _mn_utils_style_sticks.nodes.new("GeometryNodeCurveToMesh")
			curve_to_mesh.name = "Curve to Mesh"
			
			#node Group Input.001
			group_input_001_1 = _mn_utils_style_sticks.nodes.new("NodeGroupInput")
			group_input_001_1.name = "Group Input.001"
			group_input_001_1.outputs[0].hide = True
			group_input_001_1.outputs[2].hide = True
			group_input_001_1.outputs[4].hide = True
			group_input_001_1.outputs[5].hide = True
			group_input_001_1.outputs[6].hide = True
			group_input_001_1.outputs[7].hide = True
			group_input_001_1.outputs[8].hide = True
			
			#node Duplicate Elements
			duplicate_elements = _mn_utils_style_sticks.nodes.new("GeometryNodeDuplicateElements")
			duplicate_elements.name = "Duplicate Elements"
			duplicate_elements.domain = 'EDGE'
			#Selection
			duplicate_elements.inputs[1].default_value = True
			#Amount
			duplicate_elements.inputs[2].default_value = 1
			
			#node Mesh Island.001
			mesh_island_001 = _mn_utils_style_sticks.nodes.new("GeometryNodeInputMeshIsland")
			mesh_island_001.name = "Mesh Island.001"
			
			#node Accumulate Field.001
			accumulate_field_001 = _mn_utils_style_sticks.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_001.name = "Accumulate Field.001"
			accumulate_field_001.data_type = 'INT'
			accumulate_field_001.domain = 'POINT'
			#Value
			accumulate_field_001.inputs[0].default_value = 1
			
			#node Capture Attribute
			capture_attribute = _mn_utils_style_sticks.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute.name = "Capture Attribute"
			capture_attribute.active_index = 0
			capture_attribute.capture_items.clear()
			capture_attribute.capture_items.new('FLOAT', "Value")
			capture_attribute.capture_items["Value"].data_type = 'BOOLEAN'
			capture_attribute.domain = 'POINT'
			
			#node Capture Attribute.003
			capture_attribute_003 = _mn_utils_style_sticks.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute_003.name = "Capture Attribute.003"
			capture_attribute_003.active_index = 0
			capture_attribute_003.capture_items.clear()
			capture_attribute_003.capture_items.new('FLOAT', "Vertex Index 1")
			capture_attribute_003.capture_items["Vertex Index 1"].data_type = 'INT'
			capture_attribute_003.capture_items.new('FLOAT', "Vertex Index 2")
			capture_attribute_003.capture_items["Vertex Index 2"].data_type = 'INT'
			capture_attribute_003.domain = 'EDGE'
			
			#node Edge Vertices
			edge_vertices = _mn_utils_style_sticks.nodes.new("GeometryNodeInputMeshEdgeVertices")
			edge_vertices.name = "Edge Vertices"
			
			#node Group Input.003
			group_input_003_1 = _mn_utils_style_sticks.nodes.new("NodeGroupInput")
			group_input_003_1.name = "Group Input.003"
			group_input_003_1.outputs[0].hide = True
			group_input_003_1.outputs[2].hide = True
			group_input_003_1.outputs[3].hide = True
			group_input_003_1.outputs[4].hide = True
			group_input_003_1.outputs[5].hide = True
			group_input_003_1.outputs[6].hide = True
			group_input_003_1.outputs[8].hide = True
			
			#node Set Material
			set_material_2 = _mn_utils_style_sticks.nodes.new("GeometryNodeSetMaterial")
			set_material_2.name = "Set Material"
			#Selection
			set_material_2.inputs[1].default_value = True
			
			#node Set Shade Smooth
			set_shade_smooth_1 = _mn_utils_style_sticks.nodes.new("GeometryNodeSetShadeSmooth")
			set_shade_smooth_1.name = "Set Shade Smooth"
			set_shade_smooth_1.domain = 'FACE'
			#Selection
			set_shade_smooth_1.inputs[1].default_value = True
			
			#node Group Input.004
			group_input_004 = _mn_utils_style_sticks.nodes.new("NodeGroupInput")
			group_input_004.name = "Group Input.004"
			group_input_004.outputs[0].hide = True
			group_input_004.outputs[2].hide = True
			group_input_004.outputs[3].hide = True
			group_input_004.outputs[4].hide = True
			group_input_004.outputs[5].hide = True
			group_input_004.outputs[7].hide = True
			group_input_004.outputs[8].hide = True
			
			#node Group Output
			group_output_5 = _mn_utils_style_sticks.nodes.new("NodeGroupOutput")
			group_output_5.name = "Group Output"
			group_output_5.is_active_output = True
			
			#node Capture Attribute.001
			capture_attribute_001 = _mn_utils_style_sticks.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute_001.name = "Capture Attribute.001"
			capture_attribute_001.active_index = 0
			capture_attribute_001.capture_items.clear()
			capture_attribute_001.capture_items.new('FLOAT', "Value")
			capture_attribute_001.capture_items["Value"].data_type = 'BOOLEAN'
			capture_attribute_001.domain = 'FACE'
			
			#node Sample Index.001
			sample_index_001 = _mn_utils_style_sticks.nodes.new("GeometryNodeSampleIndex")
			sample_index_001.name = "Sample Index.001"
			sample_index_001.hide = True
			sample_index_001.clamp = False
			sample_index_001.data_type = 'FLOAT_COLOR'
			sample_index_001.domain = 'POINT'
			
			#node Evaluate on Domain.003
			evaluate_on_domain_003 = _mn_utils_style_sticks.nodes.new("GeometryNodeFieldOnDomain")
			evaluate_on_domain_003.name = "Evaluate on Domain.003"
			evaluate_on_domain_003.hide = True
			evaluate_on_domain_003.data_type = 'FLOAT_COLOR'
			evaluate_on_domain_003.domain = 'FACE'
			
			#node Named Attribute.002
			named_attribute_002 = _mn_utils_style_sticks.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002.name = "Named Attribute.002"
			named_attribute_002.hide = True
			named_attribute_002.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute_002.inputs[0].default_value = "Color"
			
			#node Switch.001
			switch_001 = _mn_utils_style_sticks.nodes.new("GeometryNodeSwitch")
			switch_001.name = "Switch.001"
			switch_001.hide = True
			switch_001.input_type = 'INT'
			
			#node Evaluate on Domain
			evaluate_on_domain = _mn_utils_style_sticks.nodes.new("GeometryNodeFieldOnDomain")
			evaluate_on_domain.name = "Evaluate on Domain"
			evaluate_on_domain.hide = True
			evaluate_on_domain.data_type = 'FLOAT_COLOR'
			evaluate_on_domain.domain = 'POINT'
			
			#node Switch
			switch_1 = _mn_utils_style_sticks.nodes.new("GeometryNodeSwitch")
			switch_1.name = "Switch"
			switch_1.input_type = 'RGBA'
			
			#node Group Input.005
			group_input_005 = _mn_utils_style_sticks.nodes.new("NodeGroupInput")
			group_input_005.name = "Group Input.005"
			group_input_005.outputs[0].hide = True
			group_input_005.outputs[2].hide = True
			group_input_005.outputs[3].hide = True
			group_input_005.outputs[4].hide = True
			group_input_005.outputs[6].hide = True
			group_input_005.outputs[7].hide = True
			group_input_005.outputs[8].hide = True
			
			#node Store Named Attribute
			store_named_attribute = _mn_utils_style_sticks.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute.name = "Store Named Attribute"
			store_named_attribute.data_type = 'FLOAT_COLOR'
			store_named_attribute.domain = 'CORNER'
			#Selection
			store_named_attribute.inputs[1].default_value = True
			#Name
			store_named_attribute.inputs[2].default_value = "Color"
			
			#node Group Input
			group_input_5 = _mn_utils_style_sticks.nodes.new("NodeGroupInput")
			group_input_5.name = "Group Input"
			
			#node Separate Geometry
			separate_geometry_1 = _mn_utils_style_sticks.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_1.name = "Separate Geometry"
			separate_geometry_1.domain = 'POINT'
			
			
			
			#Set parents
			mesh_to_curve.parent = frame_1
			set_curve_radius.parent = frame_1
			subdivide_curve.parent = frame_1
			group_2.parent = frame_1
			group_input_002_1.parent = frame_1
			curve_circle.parent = frame_1
			curve_to_mesh.parent = frame_1
			group_input_001_1.parent = frame_1
			duplicate_elements.parent = frame_001
			mesh_island_001.parent = frame_001
			accumulate_field_001.parent = frame_001
			capture_attribute.parent = frame_001
			capture_attribute_003.parent = frame_001
			group_input_003_1.parent = frame_003
			set_material_2.parent = frame_003
			set_shade_smooth_1.parent = frame_003
			group_input_004.parent = frame_003
			capture_attribute_001.parent = frame_002
			sample_index_001.parent = frame_002
			evaluate_on_domain_003.parent = frame_002
			named_attribute_002.parent = frame_002
			switch_001.parent = frame_002
			evaluate_on_domain.parent = frame_002
			switch_1.parent = frame_002
			group_input_005.parent = frame_002
			store_named_attribute.parent = frame_002
			
			#Set locations
			frame_1.location = (-20.0, -180.0)
			frame_001.location = (-40.0, 115.0)
			frame_003.location = (230.0, 120.0)
			frame_002.location = (0.0, 0.0)
			mesh_to_curve.location = (-1560.0, 0.0)
			set_curve_radius.location = (-1400.0, 0.0)
			subdivide_curve.location = (-1240.0, 0.0)
			group_2.location = (-1560.0, -120.0)
			group_input_002_1.location = (-1570.0, -270.0)
			curve_circle.location = (-1080.0, -140.0)
			curve_to_mesh.location = (-1080.0, 0.0)
			group_input_001_1.location = (-1080.0, -280.0)
			duplicate_elements.location = (-2000.0, -20.0)
			mesh_island_001.location = (-2000.0, -195.0)
			accumulate_field_001.location = (-1840.0, -155.0)
			capture_attribute.location = (-1840.0, -20.0)
			capture_attribute_003.location = (-2190.0, 125.0)
			edge_vertices.location = (-2460.0, 80.0)
			group_input_003_1.location = (-80.0, -40.0)
			set_material_2.location = (-80.0, 100.0)
			set_shade_smooth_1.location = (110.0, 100.0)
			group_input_004.location = (110.0, -60.0)
			group_output_5.location = (620.0, 220.0)
			capture_attribute_001.location = (-920.0, 60.0)
			sample_index_001.location = (-480.0, 180.0)
			evaluate_on_domain_003.location = (-480.0, 140.0)
			named_attribute_002.location = (-660.0, 160.0)
			switch_001.location = (-660.0, 120.0)
			evaluate_on_domain.location = (-480.0, 100.0)
			switch_1.location = (-300.0, 220.0)
			group_input_005.location = (-480.0, 60.0)
			store_named_attribute.location = (-120.0, 120.0)
			group_input_5.location = (-2680.0, 240.0)
			separate_geometry_1.location = (-2460.0, 240.0)
			
			#Set dimensions
			frame_1.width, frame_1.height = 690.4000244140625, 434.79998779296875
			frame_001.width, frame_001.height = 550.39990234375, 538.7999877929688
			frame_003.width, frame_003.height = 389.6000061035156, 303.6000061035156
			frame_002.width, frame_002.height = 1000.0, 358.79998779296875
			mesh_to_curve.width, mesh_to_curve.height = 140.0, 100.0
			set_curve_radius.width, set_curve_radius.height = 140.0, 100.0
			subdivide_curve.width, subdivide_curve.height = 140.0, 100.0
			group_2.width, group_2.height = 140.0, 100.0
			group_input_002_1.width, group_input_002_1.height = 140.0, 100.0
			curve_circle.width, curve_circle.height = 140.0, 100.0
			curve_to_mesh.width, curve_to_mesh.height = 140.0, 100.0
			group_input_001_1.width, group_input_001_1.height = 140.0, 100.0
			duplicate_elements.width, duplicate_elements.height = 140.0, 100.0
			mesh_island_001.width, mesh_island_001.height = 140.0, 100.0
			accumulate_field_001.width, accumulate_field_001.height = 140.0, 100.0
			capture_attribute.width, capture_attribute.height = 140.0, 100.0
			capture_attribute_003.width, capture_attribute_003.height = 140.0, 100.0
			edge_vertices.width, edge_vertices.height = 140.0, 100.0
			group_input_003_1.width, group_input_003_1.height = 140.0, 100.0
			set_material_2.width, set_material_2.height = 140.0, 100.0
			set_shade_smooth_1.width, set_shade_smooth_1.height = 140.0, 100.0
			group_input_004.width, group_input_004.height = 140.0, 100.0
			group_output_5.width, group_output_5.height = 140.0, 100.0
			capture_attribute_001.width, capture_attribute_001.height = 140.0, 100.0
			sample_index_001.width, sample_index_001.height = 140.0, 100.0
			evaluate_on_domain_003.width, evaluate_on_domain_003.height = 140.0, 100.0
			named_attribute_002.width, named_attribute_002.height = 140.0, 100.0
			switch_001.width, switch_001.height = 140.0, 100.0
			evaluate_on_domain.width, evaluate_on_domain.height = 140.0, 100.0
			switch_1.width, switch_1.height = 140.0, 100.0
			group_input_005.width, group_input_005.height = 140.0, 100.0
			store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
			group_input_5.width, group_input_5.height = 140.0, 100.0
			separate_geometry_1.width, separate_geometry_1.height = 140.0, 100.0
			
			#initialize _mn_utils_style_sticks links
			#capture_attribute.Geometry -> mesh_to_curve.Mesh
			_mn_utils_style_sticks.links.new(capture_attribute.outputs[0], mesh_to_curve.inputs[0])
			#set_shade_smooth_1.Geometry -> group_output_5.Geometry
			_mn_utils_style_sticks.links.new(set_shade_smooth_1.outputs[0], group_output_5.inputs[0])
			#curve_circle.Curve -> curve_to_mesh.Profile Curve
			_mn_utils_style_sticks.links.new(curve_circle.outputs[0], curve_to_mesh.inputs[1])
			#mesh_to_curve.Curve -> set_curve_radius.Curve
			_mn_utils_style_sticks.links.new(mesh_to_curve.outputs[0], set_curve_radius.inputs[0])
			#group_2.Angstrom -> set_curve_radius.Radius
			_mn_utils_style_sticks.links.new(group_2.outputs[0], set_curve_radius.inputs[2])
			#set_curve_radius.Curve -> subdivide_curve.Curve
			_mn_utils_style_sticks.links.new(set_curve_radius.outputs[0], subdivide_curve.inputs[0])
			#capture_attribute_003.Geometry -> duplicate_elements.Geometry
			_mn_utils_style_sticks.links.new(capture_attribute_003.outputs[0], duplicate_elements.inputs[0])
			#group_input_001_1.Resolution -> curve_circle.Resolution
			_mn_utils_style_sticks.links.new(group_input_001_1.outputs[3], curve_circle.inputs[0])
			#group_input_003_1.Material -> set_material_2.Material
			_mn_utils_style_sticks.links.new(group_input_003_1.outputs[7], set_material_2.inputs[2])
			#set_material_2.Geometry -> set_shade_smooth_1.Geometry
			_mn_utils_style_sticks.links.new(set_material_2.outputs[0], set_shade_smooth_1.inputs[0])
			#group_input_004.Shade Smooth -> set_shade_smooth_1.Shade Smooth
			_mn_utils_style_sticks.links.new(group_input_004.outputs[6], set_shade_smooth_1.inputs[2])
			#capture_attribute_003.Geometry -> sample_index_001.Geometry
			_mn_utils_style_sticks.links.new(capture_attribute_003.outputs[0], sample_index_001.inputs[0])
			#named_attribute_002.Attribute -> sample_index_001.Value
			_mn_utils_style_sticks.links.new(named_attribute_002.outputs[0], sample_index_001.inputs[1])
			#subdivide_curve.Curve -> curve_to_mesh.Curve
			_mn_utils_style_sticks.links.new(subdivide_curve.outputs[0], curve_to_mesh.inputs[0])
			#switch_001.Output -> sample_index_001.Index
			_mn_utils_style_sticks.links.new(switch_001.outputs[0], sample_index_001.inputs[2])
			#capture_attribute_001.Geometry -> store_named_attribute.Geometry
			_mn_utils_style_sticks.links.new(capture_attribute_001.outputs[0], store_named_attribute.inputs[0])
			#capture_attribute_003.Vertex Index 1 -> switch_001.False
			_mn_utils_style_sticks.links.new(capture_attribute_003.outputs[1], switch_001.inputs[1])
			#duplicate_elements.Geometry -> capture_attribute.Geometry
			_mn_utils_style_sticks.links.new(duplicate_elements.outputs[0], capture_attribute.inputs[0])
			#accumulate_field_001.Trailing -> capture_attribute.Value
			_mn_utils_style_sticks.links.new(accumulate_field_001.outputs[1], capture_attribute.inputs[1])
			#mesh_island_001.Island Index -> accumulate_field_001.Group ID
			_mn_utils_style_sticks.links.new(mesh_island_001.outputs[0], accumulate_field_001.inputs[1])
			#capture_attribute_003.Vertex Index 2 -> switch_001.True
			_mn_utils_style_sticks.links.new(capture_attribute_003.outputs[2], switch_001.inputs[2])
			#curve_to_mesh.Mesh -> capture_attribute_001.Geometry
			_mn_utils_style_sticks.links.new(curve_to_mesh.outputs[0], capture_attribute_001.inputs[0])
			#capture_attribute_001.Value -> switch_001.Switch
			_mn_utils_style_sticks.links.new(capture_attribute_001.outputs[1], switch_001.inputs[0])
			#capture_attribute.Value -> capture_attribute_001.Value
			_mn_utils_style_sticks.links.new(capture_attribute.outputs[1], capture_attribute_001.inputs[1])
			#sample_index_001.Value -> evaluate_on_domain_003.Value
			_mn_utils_style_sticks.links.new(sample_index_001.outputs[0], evaluate_on_domain_003.inputs[0])
			#store_named_attribute.Geometry -> set_material_2.Geometry
			_mn_utils_style_sticks.links.new(store_named_attribute.outputs[0], set_material_2.inputs[0])
			#group_input_002_1.Radius -> group_2.Value
			_mn_utils_style_sticks.links.new(group_input_002_1.outputs[2], group_2.inputs[0])
			#group_input_002_1.Fill Caps -> curve_to_mesh.Fill Caps
			_mn_utils_style_sticks.links.new(group_input_002_1.outputs[4], curve_to_mesh.inputs[2])
			#evaluate_on_domain_003.Value -> evaluate_on_domain.Value
			_mn_utils_style_sticks.links.new(evaluate_on_domain_003.outputs[0], evaluate_on_domain.inputs[0])
			#evaluate_on_domain.Value -> switch_1.True
			_mn_utils_style_sticks.links.new(evaluate_on_domain.outputs[0], switch_1.inputs[2])
			#switch_1.Output -> store_named_attribute.Value
			_mn_utils_style_sticks.links.new(switch_1.outputs[0], store_named_attribute.inputs[3])
			#evaluate_on_domain_003.Value -> switch_1.False
			_mn_utils_style_sticks.links.new(evaluate_on_domain_003.outputs[0], switch_1.inputs[1])
			#group_input_005.Interpolate Color -> switch_1.Switch
			_mn_utils_style_sticks.links.new(group_input_005.outputs[5], switch_1.inputs[0])
			#group_input_5.Atoms -> separate_geometry_1.Geometry
			_mn_utils_style_sticks.links.new(group_input_5.outputs[0], separate_geometry_1.inputs[0])
			#separate_geometry_1.Selection -> capture_attribute_003.Geometry
			_mn_utils_style_sticks.links.new(separate_geometry_1.outputs[0], capture_attribute_003.inputs[0])
			#group_input_5.Selection -> separate_geometry_1.Selection
			_mn_utils_style_sticks.links.new(group_input_5.outputs[1], separate_geometry_1.inputs[1])
			#edge_vertices.Vertex Index 2 -> capture_attribute_003.Vertex Index 2
			_mn_utils_style_sticks.links.new(edge_vertices.outputs[1], capture_attribute_003.inputs[2])
			#edge_vertices.Vertex Index 1 -> capture_attribute_003.Vertex Index 1
			_mn_utils_style_sticks.links.new(edge_vertices.outputs[0], capture_attribute_003.inputs[1])
			return _mn_utils_style_sticks

		_mn_utils_style_sticks = _mn_utils_style_sticks_node_group()

		#initialize style_sticks node group
		def style_sticks_node_group():
			style_sticks = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Style Sticks")

			style_sticks.color_tag = 'GEOMETRY'
			style_sticks.description = ""

			
			#style_sticks interface
			#Socket Geometry
			geometry_socket_2 = style_sticks.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_2.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket_4 = style_sticks.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_4.attribute_domain = 'POINT'
			atoms_socket_4.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket_4 = style_sticks.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_4.attribute_domain = 'POINT'
			selection_socket_4.hide_value = True
			selection_socket_4.description = "Selection of atoms to apply this style to"
			
			#Socket Quality
			quality_socket = style_sticks.interface.new_socket(name = "Quality", in_out='INPUT', socket_type = 'NodeSocketInt')
			quality_socket.subtype = 'NONE'
			quality_socket.default_value = 2
			quality_socket.min_value = 0
			quality_socket.max_value = 5
			quality_socket.attribute_domain = 'POINT'
			
			#Socket Radius
			radius_socket_1 = style_sticks.interface.new_socket(name = "Radius", in_out='INPUT', socket_type = 'NodeSocketFloat')
			radius_socket_1.subtype = 'NONE'
			radius_socket_1.default_value = 0.20000000298023224
			radius_socket_1.min_value = 0.0
			radius_socket_1.max_value = 1.0
			radius_socket_1.attribute_domain = 'POINT'
			
			#Panel Material
			material_panel_2 = style_sticks.interface.new_panel("Material", default_closed=True)
			#Socket Color Blur
			color_blur_socket = style_sticks.interface.new_socket(name = "Color Blur", in_out='INPUT', socket_type = 'NodeSocketBool', parent = material_panel_2)
			color_blur_socket.attribute_domain = 'POINT'
			
			#Socket Shade Smooth
			shade_smooth_socket_3 = style_sticks.interface.new_socket(name = "Shade Smooth", in_out='INPUT', socket_type = 'NodeSocketBool', parent = material_panel_2)
			shade_smooth_socket_3.attribute_domain = 'POINT'
			shade_smooth_socket_3.description = "Apply smooth shading to the created geometry"
			
			#Socket Material
			material_socket_4 = style_sticks.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial', parent = material_panel_2)
			material_socket_4.attribute_domain = 'POINT'
			material_socket_4.description = "Material to apply to the resulting geometry"
			
			
			
			#initialize style_sticks nodes
			#node Group Output
			group_output_6 = style_sticks.nodes.new("NodeGroupOutput")
			group_output_6.name = "Group Output"
			group_output_6.is_active_output = True
			
			#node Join Geometry
			join_geometry_1 = style_sticks.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_1.name = "Join Geometry"
			
			#node MN_style_spheres
			mn_style_spheres = style_sticks.nodes.new("GeometryNodeGroup")
			mn_style_spheres.label = "Style Spheres"
			mn_style_spheres.name = "MN_style_spheres"
			mn_style_spheres.node_tree = style_spheres
			#Input_1
			mn_style_spheres.inputs[1].default_value = True
			#Input_2
			mn_style_spheres.inputs[2].default_value = True
			
			#node Separate Geometry
			separate_geometry_2 = style_sticks.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_2.name = "Separate Geometry"
			separate_geometry_2.domain = 'POINT'
			
			#node Reroute
			reroute_1 = style_sticks.nodes.new("NodeReroute")
			reroute_1.name = "Reroute"
			#node Store Named Attribute
			store_named_attribute_1 = style_sticks.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_1.name = "Store Named Attribute"
			store_named_attribute_1.data_type = 'FLOAT'
			store_named_attribute_1.domain = 'POINT'
			#Selection
			store_named_attribute_1.inputs[1].default_value = True
			#Name
			store_named_attribute_1.inputs[2].default_value = "vdw_radii"
			#Value
			store_named_attribute_1.inputs[3].default_value = 0.009999999776482582
			
			#node Reroute.001
			reroute_001_1 = style_sticks.nodes.new("NodeReroute")
			reroute_001_1.name = "Reroute.001"
			#node .MN_utils_style_sticks
			_mn_utils_style_sticks_1 = style_sticks.nodes.new("GeometryNodeGroup")
			_mn_utils_style_sticks_1.name = ".MN_utils_style_sticks"
			_mn_utils_style_sticks_1.node_tree = _mn_utils_style_sticks
			#Socket_0
			_mn_utils_style_sticks_1.inputs[1].default_value = True
			#Input_15
			_mn_utils_style_sticks_1.inputs[4].default_value = False
			
			#node Integer
			integer_1 = style_sticks.nodes.new("FunctionNodeInputInt")
			integer_1.name = "Integer"
			integer_1.integer = 8
			
			#node Group Input
			group_input_6 = style_sticks.nodes.new("NodeGroupInput")
			group_input_6.name = "Group Input"
			
			#node Math
			math_3 = style_sticks.nodes.new("ShaderNodeMath")
			math_3.name = "Math"
			math_3.operation = 'MULTIPLY'
			math_3.use_clamp = False
			
			
			
			
			#Set locations
			group_output_6.location = (140.0, 120.0)
			join_geometry_1.location = (-20.0, 120.0)
			mn_style_spheres.location = (-260.0, 200.0)
			separate_geometry_2.location = (-660.0, 140.0)
			reroute_1.location = (-480.0, -60.0)
			store_named_attribute_1.location = (-440.0, 200.0)
			reroute_001_1.location = (-660.0, -40.0)
			_mn_utils_style_sticks_1.location = (-260.0, -120.0)
			integer_1.location = (-640.0, -340.0)
			group_input_6.location = (-860.0, 60.0)
			math_3.location = (-440.0, -220.0)
			
			#Set dimensions
			group_output_6.width, group_output_6.height = 140.0, 100.0
			join_geometry_1.width, join_geometry_1.height = 140.0, 100.0
			mn_style_spheres.width, mn_style_spheres.height = 200.0, 100.0
			separate_geometry_2.width, separate_geometry_2.height = 140.0, 100.0
			reroute_1.width, reroute_1.height = 16.0, 100.0
			store_named_attribute_1.width, store_named_attribute_1.height = 140.0, 100.0
			reroute_001_1.width, reroute_001_1.height = 16.0, 100.0
			_mn_utils_style_sticks_1.width, _mn_utils_style_sticks_1.height = 207.9752197265625, 100.0
			integer_1.width, integer_1.height = 140.0, 100.0
			group_input_6.width, group_input_6.height = 140.0, 100.0
			math_3.width, math_3.height = 140.0, 100.0
			
			#initialize style_sticks links
			#group_input_6.Atoms -> separate_geometry_2.Geometry
			style_sticks.links.new(group_input_6.outputs[0], separate_geometry_2.inputs[0])
			#store_named_attribute_1.Geometry -> mn_style_spheres.Atoms
			style_sticks.links.new(store_named_attribute_1.outputs[0], mn_style_spheres.inputs[0])
			#group_input_6.Selection -> separate_geometry_2.Selection
			style_sticks.links.new(group_input_6.outputs[1], separate_geometry_2.inputs[1])
			#separate_geometry_2.Selection -> _mn_utils_style_sticks_1.Atoms
			style_sticks.links.new(separate_geometry_2.outputs[0], _mn_utils_style_sticks_1.inputs[0])
			#_mn_utils_style_sticks_1.Geometry -> join_geometry_1.Geometry
			style_sticks.links.new(_mn_utils_style_sticks_1.outputs[0], join_geometry_1.inputs[0])
			#join_geometry_1.Geometry -> group_output_6.Geometry
			style_sticks.links.new(join_geometry_1.outputs[0], group_output_6.inputs[0])
			#separate_geometry_2.Selection -> store_named_attribute_1.Geometry
			style_sticks.links.new(separate_geometry_2.outputs[0], store_named_attribute_1.inputs[0])
			#reroute_1.Output -> mn_style_spheres.Sphere Radii
			style_sticks.links.new(reroute_1.outputs[0], mn_style_spheres.inputs[3])
			#reroute_1.Output -> _mn_utils_style_sticks_1.Radius
			style_sticks.links.new(reroute_1.outputs[0], _mn_utils_style_sticks_1.inputs[2])
			#group_input_6.Radius -> reroute_1.Input
			style_sticks.links.new(group_input_6.outputs[3], reroute_1.inputs[0])
			#reroute_001_1.Output -> mn_style_spheres.Sphere Subdivisions
			style_sticks.links.new(reroute_001_1.outputs[0], mn_style_spheres.inputs[4])
			#group_input_6.Quality -> reroute_001_1.Input
			style_sticks.links.new(group_input_6.outputs[2], reroute_001_1.inputs[0])
			#reroute_001_1.Output -> math_3.Value
			style_sticks.links.new(reroute_001_1.outputs[0], math_3.inputs[0])
			#math_3.Value -> _mn_utils_style_sticks_1.Resolution
			style_sticks.links.new(math_3.outputs[0], _mn_utils_style_sticks_1.inputs[3])
			#integer_1.Integer -> math_3.Value
			style_sticks.links.new(integer_1.outputs[0], math_3.inputs[1])
			#group_input_6.Shade Smooth -> mn_style_spheres.Shade Smooth
			style_sticks.links.new(group_input_6.outputs[5], mn_style_spheres.inputs[5])
			#group_input_6.Material -> mn_style_spheres.Material
			style_sticks.links.new(group_input_6.outputs[6], mn_style_spheres.inputs[6])
			#group_input_6.Material -> _mn_utils_style_sticks_1.Material
			style_sticks.links.new(group_input_6.outputs[6], _mn_utils_style_sticks_1.inputs[7])
			#group_input_6.Shade Smooth -> _mn_utils_style_sticks_1.Shade Smooth
			style_sticks.links.new(group_input_6.outputs[5], _mn_utils_style_sticks_1.inputs[6])
			#group_input_6.Color Blur -> _mn_utils_style_sticks_1.Interpolate Color
			style_sticks.links.new(group_input_6.outputs[4], _mn_utils_style_sticks_1.inputs[5])
			#mn_style_spheres.Geometry -> join_geometry_1.Geometry
			style_sticks.links.new(mn_style_spheres.outputs[0], join_geometry_1.inputs[0])
			return style_sticks

		style_sticks = style_sticks_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Style Sticks", type = 'NODES')
		mod.node_group = style_sticks
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Style_Sticks.bl_idname)
			
def register():
	bpy.utils.register_class(Style_Sticks)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Style_Sticks)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
