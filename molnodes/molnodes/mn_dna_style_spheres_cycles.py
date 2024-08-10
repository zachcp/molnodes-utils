bl_info = {
	"name" : "MN_dna_style_spheres_cycles",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class MN_dna_style_spheres_cycles(bpy.types.Operator):
	bl_idname = "node.mn_dna_style_spheres_cycles"
	bl_label = "MN_dna_style_spheres_cycles"
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

		#initialize mn_dna_style_spheres_cycles node group
		def mn_dna_style_spheres_cycles_node_group():
			mn_dna_style_spheres_cycles = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "MN_dna_style_spheres_cycles")

			mn_dna_style_spheres_cycles.color_tag = 'NONE'
			mn_dna_style_spheres_cycles.description = ""

			mn_dna_style_spheres_cycles.is_modifier = True
			
			#mn_dna_style_spheres_cycles interface
			#Socket Bases
			bases_socket = mn_dna_style_spheres_cycles.interface.new_socket(name = "Bases", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			bases_socket.attribute_domain = 'POINT'
			
			#Socket Bases
			bases_socket_1 = mn_dna_style_spheres_cycles.interface.new_socket(name = "Bases", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			bases_socket_1.attribute_domain = 'POINT'
			
			#Socket Selection
			selection_socket_1 = mn_dna_style_spheres_cycles.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_1.attribute_domain = 'POINT'
			selection_socket_1.hide_value = True
			selection_socket_1.description = "Selection of atoms to apply this node to"
			
			#Socket Scale Radii
			scale_radii_socket = mn_dna_style_spheres_cycles.interface.new_socket(name = "Scale Radii", in_out='INPUT', socket_type = 'NodeSocketFloat')
			scale_radii_socket.subtype = 'NONE'
			scale_radii_socket.default_value = 1.0
			scale_radii_socket.min_value = -10000.0
			scale_radii_socket.max_value = 10000.0
			scale_radii_socket.attribute_domain = 'POINT'
			
			#Socket Material
			material_socket_1 = mn_dna_style_spheres_cycles.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial')
			material_socket_1.attribute_domain = 'POINT'
			material_socket_1.description = "Material to apply to the resulting geometry"
			
			
			#initialize mn_dna_style_spheres_cycles nodes
			#node Named Attribute.002
			named_attribute_002 = mn_dna_style_spheres_cycles.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002.name = "Named Attribute.002"
			named_attribute_002.data_type = 'INT'
			#Name
			named_attribute_002.inputs[0].default_value = "res_name"
			
			#node Compare.001
			compare_001 = mn_dna_style_spheres_cycles.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'INT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'EQUAL'
			#B_INT
			compare_001.inputs[3].default_value = 30
			
			#node Compare.002
			compare_002 = mn_dna_style_spheres_cycles.nodes.new("FunctionNodeCompare")
			compare_002.name = "Compare.002"
			compare_002.data_type = 'INT'
			compare_002.mode = 'ELEMENT'
			compare_002.operation = 'EQUAL'
			#B_INT
			compare_002.inputs[3].default_value = 31
			
			#node Compare.003
			compare_003 = mn_dna_style_spheres_cycles.nodes.new("FunctionNodeCompare")
			compare_003.name = "Compare.003"
			compare_003.data_type = 'INT'
			compare_003.mode = 'ELEMENT'
			compare_003.operation = 'EQUAL'
			#B_INT
			compare_003.inputs[3].default_value = 32
			
			#node Compare.004
			compare_004 = mn_dna_style_spheres_cycles.nodes.new("FunctionNodeCompare")
			compare_004.name = "Compare.004"
			compare_004.data_type = 'INT'
			compare_004.mode = 'ELEMENT'
			compare_004.operation = 'EQUAL'
			#B_INT
			compare_004.inputs[3].default_value = 33
			
			#node Group.005
			group_005 = mn_dna_style_spheres_cycles.nodes.new("GeometryNodeGroup")
			group_005.name = "Group.005"
			group_005.node_tree = _mn_utils_style_spheres_points
			
			#node Group Input
			group_input_3 = mn_dna_style_spheres_cycles.nodes.new("NodeGroupInput")
			group_input_3.name = "Group Input"
			
			#node Group.006
			group_006 = mn_dna_style_spheres_cycles.nodes.new("GeometryNodeGroup")
			group_006.name = "Group.006"
			group_006.node_tree = _mn_utils_style_spheres_points
			
			#node Group.007
			group_007 = mn_dna_style_spheres_cycles.nodes.new("GeometryNodeGroup")
			group_007.name = "Group.007"
			group_007.node_tree = _mn_utils_style_spheres_points
			
			#node Geometry to Instance
			geometry_to_instance = mn_dna_style_spheres_cycles.nodes.new("GeometryNodeGeometryToInstance")
			geometry_to_instance.name = "Geometry to Instance"
			
			#node Group Output
			group_output_3 = mn_dna_style_spheres_cycles.nodes.new("NodeGroupOutput")
			group_output_3.name = "Group Output"
			group_output_3.is_active_output = True
			
			#node Realize Instances
			realize_instances = mn_dna_style_spheres_cycles.nodes.new("GeometryNodeRealizeInstances")
			realize_instances.name = "Realize Instances"
			#Selection
			realize_instances.inputs[1].default_value = True
			#Realize All
			realize_instances.inputs[2].default_value = True
			#Depth
			realize_instances.inputs[3].default_value = 0
			
			#node Group.004
			group_004 = mn_dna_style_spheres_cycles.nodes.new("GeometryNodeGroup")
			group_004.name = "Group.004"
			group_004.node_tree = _mn_utils_style_spheres_points
			
			#node Separate Geometry.004
			separate_geometry_004 = mn_dna_style_spheres_cycles.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_004.name = "Separate Geometry.004"
			separate_geometry_004.domain = 'POINT'
			
			#node Separate Geometry.003
			separate_geometry_003 = mn_dna_style_spheres_cycles.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_003.name = "Separate Geometry.003"
			separate_geometry_003.domain = 'POINT'
			
			#node Separate Geometry.002
			separate_geometry_002 = mn_dna_style_spheres_cycles.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_002.name = "Separate Geometry.002"
			separate_geometry_002.domain = 'POINT'
			
			#node Separate Geometry.001
			separate_geometry_001 = mn_dna_style_spheres_cycles.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_001.name = "Separate Geometry.001"
			separate_geometry_001.domain = 'POINT'
			
			
			
			
			#Set locations
			named_attribute_002.location = (-271.8153076171875, 270.0)
			compare_001.location = (-73.56605529785156, 281.95001220703125)
			compare_002.location = (-71.81532287597656, 110.0)
			compare_003.location = (-71.81532287597656, -70.0)
			compare_004.location = (-71.81532287597656, -250.0)
			group_005.location = (308.1846923828125, 90.0)
			group_input_3.location = (-508.1846923828125, -0.0)
			group_006.location = (308.1846923828125, -110.0)
			group_007.location = (308.1846923828125, -290.0)
			geometry_to_instance.location = (600.0, 100.0)
			group_output_3.location = (947.1314086914062, 66.40379333496094)
			realize_instances.location = (-280.0, 120.0)
			group_004.location = (308.1846923828125, 290.0)
			separate_geometry_004.location = (108.18467712402344, -230.0)
			separate_geometry_003.location = (108.18467712402344, -50.0)
			separate_geometry_002.location = (108.18467712402344, 130.0)
			separate_geometry_001.location = (108.18467712402344, 290.0)
			
			#Set dimensions
			named_attribute_002.width, named_attribute_002.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			compare_002.width, compare_002.height = 140.0, 100.0
			compare_003.width, compare_003.height = 140.0, 100.0
			compare_004.width, compare_004.height = 140.0, 100.0
			group_005.width, group_005.height = 140.0, 100.0
			group_input_3.width, group_input_3.height = 140.0, 100.0
			group_006.width, group_006.height = 140.0, 100.0
			group_007.width, group_007.height = 140.0, 100.0
			geometry_to_instance.width, geometry_to_instance.height = 160.0, 100.0
			group_output_3.width, group_output_3.height = 140.0, 100.0
			realize_instances.width, realize_instances.height = 140.0, 100.0
			group_004.width, group_004.height = 140.0, 100.0
			separate_geometry_004.width, separate_geometry_004.height = 140.0, 100.0
			separate_geometry_003.width, separate_geometry_003.height = 140.0, 100.0
			separate_geometry_002.width, separate_geometry_002.height = 140.0, 100.0
			separate_geometry_001.width, separate_geometry_001.height = 140.0, 100.0
			
			#initialize mn_dna_style_spheres_cycles links
			#group_input_3.Bases -> realize_instances.Geometry
			mn_dna_style_spheres_cycles.links.new(group_input_3.outputs[0], realize_instances.inputs[0])
			#realize_instances.Geometry -> separate_geometry_001.Geometry
			mn_dna_style_spheres_cycles.links.new(realize_instances.outputs[0], separate_geometry_001.inputs[0])
			#compare_001.Result -> separate_geometry_001.Selection
			mn_dna_style_spheres_cycles.links.new(compare_001.outputs[0], separate_geometry_001.inputs[1])
			#named_attribute_002.Attribute -> compare_001.A
			mn_dna_style_spheres_cycles.links.new(named_attribute_002.outputs[0], compare_001.inputs[2])
			#realize_instances.Geometry -> separate_geometry_002.Geometry
			mn_dna_style_spheres_cycles.links.new(realize_instances.outputs[0], separate_geometry_002.inputs[0])
			#compare_002.Result -> separate_geometry_002.Selection
			mn_dna_style_spheres_cycles.links.new(compare_002.outputs[0], separate_geometry_002.inputs[1])
			#named_attribute_002.Attribute -> compare_002.A
			mn_dna_style_spheres_cycles.links.new(named_attribute_002.outputs[0], compare_002.inputs[2])
			#realize_instances.Geometry -> separate_geometry_003.Geometry
			mn_dna_style_spheres_cycles.links.new(realize_instances.outputs[0], separate_geometry_003.inputs[0])
			#compare_003.Result -> separate_geometry_003.Selection
			mn_dna_style_spheres_cycles.links.new(compare_003.outputs[0], separate_geometry_003.inputs[1])
			#named_attribute_002.Attribute -> compare_003.A
			mn_dna_style_spheres_cycles.links.new(named_attribute_002.outputs[0], compare_003.inputs[2])
			#realize_instances.Geometry -> separate_geometry_004.Geometry
			mn_dna_style_spheres_cycles.links.new(realize_instances.outputs[0], separate_geometry_004.inputs[0])
			#compare_004.Result -> separate_geometry_004.Selection
			mn_dna_style_spheres_cycles.links.new(compare_004.outputs[0], separate_geometry_004.inputs[1])
			#named_attribute_002.Attribute -> compare_004.A
			mn_dna_style_spheres_cycles.links.new(named_attribute_002.outputs[0], compare_004.inputs[2])
			#separate_geometry_001.Selection -> group_004.Atoms
			mn_dna_style_spheres_cycles.links.new(separate_geometry_001.outputs[0], group_004.inputs[0])
			#separate_geometry_004.Selection -> group_007.Atoms
			mn_dna_style_spheres_cycles.links.new(separate_geometry_004.outputs[0], group_007.inputs[0])
			#group_input_3.Selection -> group_004.Selection
			mn_dna_style_spheres_cycles.links.new(group_input_3.outputs[1], group_004.inputs[1])
			#group_input_3.Selection -> group_005.Selection
			mn_dna_style_spheres_cycles.links.new(group_input_3.outputs[1], group_005.inputs[1])
			#group_input_3.Selection -> group_006.Selection
			mn_dna_style_spheres_cycles.links.new(group_input_3.outputs[1], group_006.inputs[1])
			#group_input_3.Scale Radii -> group_004.Radii
			mn_dna_style_spheres_cycles.links.new(group_input_3.outputs[2], group_004.inputs[2])
			#group_input_3.Scale Radii -> group_005.Radii
			mn_dna_style_spheres_cycles.links.new(group_input_3.outputs[2], group_005.inputs[2])
			#group_input_3.Selection -> group_007.Selection
			mn_dna_style_spheres_cycles.links.new(group_input_3.outputs[1], group_007.inputs[1])
			#group_input_3.Material -> group_004.Material
			mn_dna_style_spheres_cycles.links.new(group_input_3.outputs[3], group_004.inputs[3])
			#group_input_3.Material -> group_005.Material
			mn_dna_style_spheres_cycles.links.new(group_input_3.outputs[3], group_005.inputs[3])
			#group_input_3.Scale Radii -> group_007.Radii
			mn_dna_style_spheres_cycles.links.new(group_input_3.outputs[2], group_007.inputs[2])
			#group_input_3.Scale Radii -> group_006.Radii
			mn_dna_style_spheres_cycles.links.new(group_input_3.outputs[2], group_006.inputs[2])
			#group_input_3.Material -> group_006.Material
			mn_dna_style_spheres_cycles.links.new(group_input_3.outputs[3], group_006.inputs[3])
			#group_input_3.Material -> group_007.Material
			mn_dna_style_spheres_cycles.links.new(group_input_3.outputs[3], group_007.inputs[3])
			#geometry_to_instance.Instances -> group_output_3.Bases
			mn_dna_style_spheres_cycles.links.new(geometry_to_instance.outputs[0], group_output_3.inputs[0])
			#group_007.Point Cloud -> geometry_to_instance.Geometry
			mn_dna_style_spheres_cycles.links.new(group_007.outputs[0], geometry_to_instance.inputs[0])
			#separate_geometry_002.Selection -> group_005.Atoms
			mn_dna_style_spheres_cycles.links.new(separate_geometry_002.outputs[0], group_005.inputs[0])
			#separate_geometry_003.Selection -> group_006.Atoms
			mn_dna_style_spheres_cycles.links.new(separate_geometry_003.outputs[0], group_006.inputs[0])
			#group_006.Point Cloud -> geometry_to_instance.Geometry
			mn_dna_style_spheres_cycles.links.new(group_006.outputs[0], geometry_to_instance.inputs[0])
			#group_005.Point Cloud -> geometry_to_instance.Geometry
			mn_dna_style_spheres_cycles.links.new(group_005.outputs[0], geometry_to_instance.inputs[0])
			#group_004.Point Cloud -> geometry_to_instance.Geometry
			mn_dna_style_spheres_cycles.links.new(group_004.outputs[0], geometry_to_instance.inputs[0])
			return mn_dna_style_spheres_cycles

		mn_dna_style_spheres_cycles = mn_dna_style_spheres_cycles_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "MN_dna_style_spheres_cycles", type = 'NODES')
		mod.node_group = mn_dna_style_spheres_cycles
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(MN_dna_style_spheres_cycles.bl_idname)
			
def register():
	bpy.utils.register_class(MN_dna_style_spheres_cycles)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(MN_dna_style_spheres_cycles)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
