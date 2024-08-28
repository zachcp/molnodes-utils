bl_info = {
	"name" : "Topology DSSP",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Topology_DSSP(bpy.types.Operator):
	bl_idname = "node.topology_dssp"
	bl_label = "Topology DSSP"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize boolean_run_mask node group
		def boolean_run_mask_node_group():
			boolean_run_mask = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Boolean Run Mask")

			boolean_run_mask.color_tag = 'CONVERTER'
			boolean_run_mask.description = ""

			
			#boolean_run_mask interface
			#Socket Boolean
			boolean_socket = boolean_run_mask.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket.default_value = False
			boolean_socket.attribute_domain = 'POINT'
			
			#Socket Boolean
			boolean_socket_1 = boolean_run_mask.interface.new_socket(name = "Boolean", in_out='INPUT', socket_type = 'NodeSocketBool')
			boolean_socket_1.default_value = False
			boolean_socket_1.attribute_domain = 'POINT'
			
			#Socket Lag Start
			lag_start_socket = boolean_run_mask.interface.new_socket(name = "Lag Start", in_out='INPUT', socket_type = 'NodeSocketInt')
			lag_start_socket.default_value = 0
			lag_start_socket.min_value = 0
			lag_start_socket.max_value = 2147483647
			lag_start_socket.subtype = 'NONE'
			lag_start_socket.attribute_domain = 'POINT'
			lag_start_socket.description = "The first N values in a run are made to be false"
			
			#Socket Min Length
			min_length_socket = boolean_run_mask.interface.new_socket(name = "Min Length", in_out='INPUT', socket_type = 'NodeSocketInt')
			min_length_socket.default_value = 0
			min_length_socket.min_value = 0
			min_length_socket.max_value = 2147483647
			min_length_socket.subtype = 'NONE'
			min_length_socket.attribute_domain = 'POINT'
			min_length_socket.description = "Run is only valid if it contains at least N values"
			
			#Socket Trim End
			trim_end_socket = boolean_run_mask.interface.new_socket(name = "Trim End", in_out='INPUT', socket_type = 'NodeSocketInt')
			trim_end_socket.default_value = 0
			trim_end_socket.min_value = -2147483648
			trim_end_socket.max_value = 2147483647
			trim_end_socket.subtype = 'NONE'
			trim_end_socket.attribute_domain = 'POINT'
			
			
			#initialize boolean_run_mask nodes
			#node Group Output
			group_output = boolean_run_mask.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = boolean_run_mask.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			group_input.outputs[3].hide = True
			
			#node Accumulate Field
			accumulate_field = boolean_run_mask.nodes.new("GeometryNodeAccumulateField")
			accumulate_field.name = "Accumulate Field"
			accumulate_field.data_type = 'INT'
			accumulate_field.domain = 'POINT'
			#Group Index
			accumulate_field.inputs[1].default_value = 0
			
			#node Boolean Math.001
			boolean_math_001 = boolean_run_mask.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001.name = "Boolean Math.001"
			boolean_math_001.operation = 'NOT'
			
			#node Accumulate Field.001
			accumulate_field_001 = boolean_run_mask.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_001.name = "Accumulate Field.001"
			accumulate_field_001.data_type = 'INT'
			accumulate_field_001.domain = 'POINT'
			#Value
			accumulate_field_001.inputs[0].default_value = 1
			
			#node Compare
			compare = boolean_run_mask.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'GREATER_THAN'
			
			#node Boolean Math.002
			boolean_math_002 = boolean_run_mask.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002.name = "Boolean Math.002"
			boolean_math_002.operation = 'AND'
			
			#node Reroute
			reroute = boolean_run_mask.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Boolean Math.003
			boolean_math_003 = boolean_run_mask.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003.name = "Boolean Math.003"
			boolean_math_003.operation = 'AND'
			
			#node Compare.001
			compare_001 = boolean_run_mask.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'INT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'GREATER_THAN'
			
			#node Boolean Math.004
			boolean_math_004 = boolean_run_mask.nodes.new("FunctionNodeBooleanMath")
			boolean_math_004.name = "Boolean Math.004"
			boolean_math_004.operation = 'AND'
			
			#node Compare.002
			compare_002 = boolean_run_mask.nodes.new("FunctionNodeCompare")
			compare_002.name = "Compare.002"
			compare_002.data_type = 'INT'
			compare_002.mode = 'ELEMENT'
			compare_002.operation = 'GREATER_THAN'
			
			#node Math
			math = boolean_run_mask.nodes.new("ShaderNodeMath")
			math.name = "Math"
			math.operation = 'SUBTRACT'
			math.use_clamp = False
			
			#node Group Input.001
			group_input_001 = boolean_run_mask.nodes.new("NodeGroupInput")
			group_input_001.name = "Group Input.001"
			group_input_001.outputs[0].hide = True
			group_input_001.outputs[1].hide = True
			group_input_001.outputs[2].hide = True
			group_input_001.outputs[4].hide = True
			
			
			
			
			#Set locations
			group_output.location = (860.0001220703125, 60.0)
			group_input.location = (-460.0031433105469, 0.0)
			accumulate_field.location = (-100.0, -300.0)
			boolean_math_001.location = (-260.0, -300.0)
			accumulate_field_001.location = (60.0, -300.0)
			compare.location = (260.0031433105469, -80.0)
			boolean_math_002.location = (260.0, 60.0)
			reroute.location = (-260.0031433105469, -29.36541748046875)
			boolean_math_003.location = (420.0, 60.0)
			compare_001.location = (420.0, -80.0)
			boolean_math_004.location = (580.0, 60.0)
			compare_002.location = (580.0, -80.0)
			math.location = (420.0, -240.0)
			group_input_001.location = (580.0, -240.0)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			accumulate_field.width, accumulate_field.height = 140.0, 100.0
			boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
			accumulate_field_001.width, accumulate_field_001.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			boolean_math_002.width, boolean_math_002.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			boolean_math_003.width, boolean_math_003.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			boolean_math_004.width, boolean_math_004.height = 140.0, 100.0
			compare_002.width, compare_002.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			group_input_001.width, group_input_001.height = 140.0, 100.0
			
			#initialize boolean_run_mask links
			#boolean_math_001.Boolean -> accumulate_field.Value
			boolean_run_mask.links.new(boolean_math_001.outputs[0], accumulate_field.inputs[0])
			#reroute.Output -> boolean_math_001.Boolean
			boolean_run_mask.links.new(reroute.outputs[0], boolean_math_001.inputs[0])
			#compare.Result -> boolean_math_002.Boolean
			boolean_run_mask.links.new(compare.outputs[0], boolean_math_002.inputs[1])
			#group_input.Boolean -> reroute.Input
			boolean_run_mask.links.new(group_input.outputs[0], reroute.inputs[0])
			#boolean_math_004.Boolean -> group_output.Boolean
			boolean_run_mask.links.new(boolean_math_004.outputs[0], group_output.inputs[0])
			#group_input.Lag Start -> compare.B
			boolean_run_mask.links.new(group_input.outputs[1], compare.inputs[3])
			#boolean_math_002.Boolean -> boolean_math_003.Boolean
			boolean_run_mask.links.new(boolean_math_002.outputs[0], boolean_math_003.inputs[0])
			#accumulate_field_001.Total -> compare_001.A
			boolean_run_mask.links.new(accumulate_field_001.outputs[2], compare_001.inputs[2])
			#group_input.Min Length -> compare_001.B
			boolean_run_mask.links.new(group_input.outputs[2], compare_001.inputs[3])
			#compare_001.Result -> boolean_math_003.Boolean
			boolean_run_mask.links.new(compare_001.outputs[0], boolean_math_003.inputs[1])
			#reroute.Output -> boolean_math_002.Boolean
			boolean_run_mask.links.new(reroute.outputs[0], boolean_math_002.inputs[0])
			#accumulate_field.Trailing -> accumulate_field_001.Group ID
			boolean_run_mask.links.new(accumulate_field.outputs[1], accumulate_field_001.inputs[1])
			#boolean_math_003.Boolean -> boolean_math_004.Boolean
			boolean_run_mask.links.new(boolean_math_003.outputs[0], boolean_math_004.inputs[0])
			#accumulate_field_001.Total -> math.Value
			boolean_run_mask.links.new(accumulate_field_001.outputs[2], math.inputs[0])
			#accumulate_field_001.Leading -> math.Value
			boolean_run_mask.links.new(accumulate_field_001.outputs[0], math.inputs[1])
			#math.Value -> compare_002.A
			boolean_run_mask.links.new(math.outputs[0], compare_002.inputs[2])
			#group_input_001.Trim End -> compare_002.B
			boolean_run_mask.links.new(group_input_001.outputs[3], compare_002.inputs[3])
			#compare_002.Result -> boolean_math_004.Boolean
			boolean_run_mask.links.new(compare_002.outputs[0], boolean_math_004.inputs[1])
			#accumulate_field_001.Leading -> compare.A
			boolean_run_mask.links.new(accumulate_field_001.outputs[0], compare.inputs[2])
			return boolean_run_mask

		boolean_run_mask = boolean_run_mask_node_group()

		#initialize _mn_world_scale node group
		def _mn_world_scale_node_group():
			_mn_world_scale = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_world_scale")

			_mn_world_scale.color_tag = 'NONE'
			_mn_world_scale.description = ""

			
			#_mn_world_scale interface
			#Socket world_scale
			world_scale_socket = _mn_world_scale.interface.new_socket(name = "world_scale", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			world_scale_socket.default_value = 0.009999999776482582
			world_scale_socket.min_value = -3.4028234663852886e+38
			world_scale_socket.max_value = 3.4028234663852886e+38
			world_scale_socket.subtype = 'NONE'
			world_scale_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_world_scale nodes
			#node Group Input
			group_input_1 = _mn_world_scale.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			
			#node Value
			value = _mn_world_scale.nodes.new("ShaderNodeValue")
			value.label = "world_scale"
			value.name = "Value"
			
			value.outputs[0].default_value = 0.009999999776482582
			#node Group Output
			group_output_1 = _mn_world_scale.nodes.new("NodeGroupOutput")
			group_output_1.name = "Group Output"
			group_output_1.is_active_output = True
			
			
			
			
			#Set locations
			group_input_1.location = (-200.0, 0.0)
			value.location = (0.0, 0.0)
			group_output_1.location = (190.0, 0.0)
			
			#Set dimensions
			group_input_1.width, group_input_1.height = 140.0, 100.0
			value.width, value.height = 140.0, 100.0
			group_output_1.width, group_output_1.height = 140.0, 100.0
			
			#initialize _mn_world_scale links
			#value.Value -> group_output_1.world_scale
			_mn_world_scale.links.new(value.outputs[0], group_output_1.inputs[0])
			return _mn_world_scale

		_mn_world_scale = _mn_world_scale_node_group()

		#initialize world_to_angstrom node group
		def world_to_angstrom_node_group():
			world_to_angstrom = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "World to Angstrom")

			world_to_angstrom.color_tag = 'NONE'
			world_to_angstrom.description = ""

			
			#world_to_angstrom interface
			#Socket Angstrom
			angstrom_socket = world_to_angstrom.interface.new_socket(name = "Angstrom", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			angstrom_socket.default_value = 0.0
			angstrom_socket.min_value = -3.4028234663852886e+38
			angstrom_socket.max_value = 3.4028234663852886e+38
			angstrom_socket.subtype = 'NONE'
			angstrom_socket.attribute_domain = 'POINT'
			
			#Socket World
			world_socket = world_to_angstrom.interface.new_socket(name = "World", in_out='INPUT', socket_type = 'NodeSocketFloat')
			world_socket.default_value = 0.5
			world_socket.min_value = -10000.0
			world_socket.max_value = 10000.0
			world_socket.subtype = 'NONE'
			world_socket.attribute_domain = 'POINT'
			
			
			#initialize world_to_angstrom nodes
			#node Group Output
			group_output_2 = world_to_angstrom.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Group Input
			group_input_2 = world_to_angstrom.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
			#node Group
			group = world_to_angstrom.nodes.new("GeometryNodeGroup")
			group.name = "Group"
			group.node_tree = _mn_world_scale
			
			#node Math
			math_1 = world_to_angstrom.nodes.new("ShaderNodeMath")
			math_1.name = "Math"
			math_1.operation = 'DIVIDE'
			math_1.use_clamp = False
			
			
			
			
			#Set locations
			group_output_2.location = (190.0, 0.0)
			group_input_2.location = (-200.0, 0.0)
			group.location = (0.0, -80.0)
			math_1.location = (0.0, 80.0)
			
			#Set dimensions
			group_output_2.width, group_output_2.height = 140.0, 100.0
			group_input_2.width, group_input_2.height = 140.0, 100.0
			group.width, group.height = 140.0, 100.0
			math_1.width, math_1.height = 140.0, 100.0
			
			#initialize world_to_angstrom links
			#group.world_scale -> math_1.Value
			world_to_angstrom.links.new(group.outputs[0], math_1.inputs[1])
			#group_input_2.World -> math_1.Value
			world_to_angstrom.links.new(group_input_2.outputs[0], math_1.inputs[0])
			#math_1.Value -> group_output_2.Angstrom
			world_to_angstrom.links.new(math_1.outputs[0], group_output_2.inputs[0])
			return world_to_angstrom

		world_to_angstrom = world_to_angstrom_node_group()

		#initialize nodegroup_001 node group
		def nodegroup_001_node_group():
			nodegroup_001 = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "NodeGroup.001")

			nodegroup_001.color_tag = 'NONE'
			nodegroup_001.description = ""

			
			#nodegroup_001 interface
			#Socket Value
			value_socket = nodegroup_001.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			value_socket.default_value = 0.0
			value_socket.min_value = -3.4028234663852886e+38
			value_socket.max_value = 3.4028234663852886e+38
			value_socket.subtype = 'NONE'
			value_socket.attribute_domain = 'POINT'
			
			#Socket Vector
			vector_socket = nodegroup_001.interface.new_socket(name = "Vector", in_out='INPUT', socket_type = 'NodeSocketVector')
			vector_socket.default_value = (0.0, 0.0, 0.0)
			vector_socket.min_value = -10000.0
			vector_socket.max_value = 10000.0
			vector_socket.subtype = 'NONE'
			vector_socket.attribute_domain = 'POINT'
			
			#Socket Vector
			vector_socket_1 = nodegroup_001.interface.new_socket(name = "Vector", in_out='INPUT', socket_type = 'NodeSocketVector')
			vector_socket_1.default_value = (0.0, 0.0, 0.0)
			vector_socket_1.min_value = -10000.0
			vector_socket_1.max_value = 10000.0
			vector_socket_1.subtype = 'NONE'
			vector_socket_1.attribute_domain = 'POINT'
			
			
			#initialize nodegroup_001 nodes
			#node Group Output
			group_output_3 = nodegroup_001.nodes.new("NodeGroupOutput")
			group_output_3.name = "Group Output"
			group_output_3.is_active_output = True
			
			#node Group Input
			group_input_3 = nodegroup_001.nodes.new("NodeGroupInput")
			group_input_3.name = "Group Input"
			
			#node Vector Math.002
			vector_math_002 = nodegroup_001.nodes.new("ShaderNodeVectorMath")
			vector_math_002.name = "Vector Math.002"
			vector_math_002.operation = 'DISTANCE'
			
			#node Math.002
			math_002 = nodegroup_001.nodes.new("ShaderNodeMath")
			math_002.name = "Math.002"
			math_002.operation = 'DIVIDE'
			math_002.use_clamp = False
			#Value
			math_002.inputs[0].default_value = 1.0
			
			#node Group.001
			group_001 = nodegroup_001.nodes.new("GeometryNodeGroup")
			group_001.name = "Group.001"
			group_001.node_tree = world_to_angstrom
			
			
			
			
			#Set locations
			group_output_3.location = (670.8533325195312, -4.1087493896484375)
			group_input_3.location = (-280.0, 0.0)
			vector_math_002.location = (-80.0, 0.0)
			math_002.location = (260.0, 0.0)
			group_001.location = (80.0, 0.0)
			
			#Set dimensions
			group_output_3.width, group_output_3.height = 140.0, 100.0
			group_input_3.width, group_input_3.height = 140.0, 100.0
			vector_math_002.width, vector_math_002.height = 140.0, 100.0
			math_002.width, math_002.height = 140.0, 100.0
			group_001.width, group_001.height = 152.50686645507812, 100.0
			
			#initialize nodegroup_001 links
			#group_001.Angstrom -> math_002.Value
			nodegroup_001.links.new(group_001.outputs[0], math_002.inputs[1])
			#group_input_3.Vector -> vector_math_002.Vector
			nodegroup_001.links.new(group_input_3.outputs[1], vector_math_002.inputs[1])
			#group_input_3.Vector -> vector_math_002.Vector
			nodegroup_001.links.new(group_input_3.outputs[0], vector_math_002.inputs[0])
			#math_002.Value -> group_output_3.Value
			nodegroup_001.links.new(math_002.outputs[0], group_output_3.inputs[0])
			#vector_math_002.Value -> group_001.World
			nodegroup_001.links.new(vector_math_002.outputs[1], group_001.inputs[0])
			return nodegroup_001

		nodegroup_001 = nodegroup_001_node_group()

		#initialize hbond_energy node group
		def hbond_energy_node_group():
			hbond_energy = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "HBond Energy")

			hbond_energy.color_tag = 'NONE'
			hbond_energy.description = ""

			
			#hbond_energy interface
			#Socket Is Bonded
			is_bonded_socket = hbond_energy.interface.new_socket(name = "Is Bonded", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_bonded_socket.default_value = False
			is_bonded_socket.attribute_domain = 'POINT'
			
			#Socket Bond Energy
			bond_energy_socket = hbond_energy.interface.new_socket(name = "Bond Energy", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			bond_energy_socket.default_value = 0.0
			bond_energy_socket.min_value = -3.4028234663852886e+38
			bond_energy_socket.max_value = 3.4028234663852886e+38
			bond_energy_socket.subtype = 'NONE'
			bond_energy_socket.attribute_domain = 'POINT'
			
			#Socket Bond Vector
			bond_vector_socket = hbond_energy.interface.new_socket(name = "Bond Vector", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			bond_vector_socket.default_value = (0.0, 0.0, 0.0)
			bond_vector_socket.min_value = -3.4028234663852886e+38
			bond_vector_socket.max_value = 3.4028234663852886e+38
			bond_vector_socket.subtype = 'NONE'
			bond_vector_socket.attribute_domain = 'POINT'
			
			#Socket O
			o_socket = hbond_energy.interface.new_socket(name = "O", in_out='INPUT', socket_type = 'NodeSocketVector')
			o_socket.default_value = (0.0, 0.0, 0.0)
			o_socket.min_value = -3.4028234663852886e+38
			o_socket.max_value = 3.4028234663852886e+38
			o_socket.subtype = 'NONE'
			o_socket.attribute_domain = 'POINT'
			
			#Socket C
			c_socket = hbond_energy.interface.new_socket(name = "C", in_out='INPUT', socket_type = 'NodeSocketVector')
			c_socket.default_value = (0.0, 0.0, 0.0)
			c_socket.min_value = -3.4028234663852886e+38
			c_socket.max_value = 3.4028234663852886e+38
			c_socket.subtype = 'NONE'
			c_socket.attribute_domain = 'POINT'
			
			#Socket N
			n_socket = hbond_energy.interface.new_socket(name = "N", in_out='INPUT', socket_type = 'NodeSocketVector')
			n_socket.default_value = (0.0, 0.0, 0.0)
			n_socket.min_value = -3.4028234663852886e+38
			n_socket.max_value = 3.4028234663852886e+38
			n_socket.subtype = 'NONE'
			n_socket.attribute_domain = 'POINT'
			
			#Socket H
			h_socket = hbond_energy.interface.new_socket(name = "H", in_out='INPUT', socket_type = 'NodeSocketVector')
			h_socket.default_value = (0.0, 0.0, 0.0)
			h_socket.min_value = -3.4028234663852886e+38
			h_socket.max_value = 3.4028234663852886e+38
			h_socket.subtype = 'NONE'
			h_socket.attribute_domain = 'POINT'
			
			
			#initialize hbond_energy nodes
			#node Group Output
			group_output_4 = hbond_energy.nodes.new("NodeGroupOutput")
			group_output_4.name = "Group Output"
			group_output_4.is_active_output = True
			
			#node Group Input
			group_input_4 = hbond_energy.nodes.new("NodeGroupInput")
			group_input_4.name = "Group Input"
			
			#node Group.003
			group_003 = hbond_energy.nodes.new("GeometryNodeGroup")
			group_003.label = "1/r(ON)"
			group_003.name = "Group.003"
			group_003.node_tree = nodegroup_001
			
			#node Group.008
			group_008 = hbond_energy.nodes.new("GeometryNodeGroup")
			group_008.label = "1/r(CH)"
			group_008.name = "Group.008"
			group_008.node_tree = nodegroup_001
			
			#node Group.009
			group_009 = hbond_energy.nodes.new("GeometryNodeGroup")
			group_009.label = "1/r(OH)"
			group_009.name = "Group.009"
			group_009.node_tree = nodegroup_001
			
			#node Group.010
			group_010 = hbond_energy.nodes.new("GeometryNodeGroup")
			group_010.label = "1/r(CN)"
			group_010.name = "Group.010"
			group_010.node_tree = nodegroup_001
			
			#node Math.002
			math_002_1 = hbond_energy.nodes.new("ShaderNodeMath")
			math_002_1.name = "Math.002"
			math_002_1.hide = True
			math_002_1.operation = 'ADD'
			math_002_1.use_clamp = False
			
			#node Math.003
			math_003 = hbond_energy.nodes.new("ShaderNodeMath")
			math_003.name = "Math.003"
			math_003.hide = True
			math_003.operation = 'SUBTRACT'
			math_003.use_clamp = False
			
			#node Math.004
			math_004 = hbond_energy.nodes.new("ShaderNodeMath")
			math_004.name = "Math.004"
			math_004.hide = True
			math_004.operation = 'SUBTRACT'
			math_004.use_clamp = False
			
			#node Math.005
			math_005 = hbond_energy.nodes.new("ShaderNodeMath")
			math_005.label = "* q1q2"
			math_005.name = "Math.005"
			math_005.operation = 'MULTIPLY'
			math_005.use_clamp = False
			#Value_001
			math_005.inputs[1].default_value = 0.08399999886751175
			
			#node Math.006
			math_006 = hbond_energy.nodes.new("ShaderNodeMath")
			math_006.label = "*f"
			math_006.name = "Math.006"
			math_006.operation = 'MULTIPLY'
			math_006.use_clamp = False
			#Value_001
			math_006.inputs[1].default_value = 332.0
			
			#node Vector Math
			vector_math = hbond_energy.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.operation = 'SUBTRACT'
			
			#node Math.007
			math_007 = hbond_energy.nodes.new("ShaderNodeMath")
			math_007.label = "*e"
			math_007.name = "Math.007"
			math_007.mute = True
			math_007.operation = 'MULTIPLY'
			math_007.use_clamp = False
			#Value_001
			math_007.inputs[1].default_value = -1.0
			
			#node Compare
			compare_1 = hbond_energy.nodes.new("FunctionNodeCompare")
			compare_1.label = "Cutoff kcal/mol"
			compare_1.name = "Compare"
			compare_1.data_type = 'FLOAT'
			compare_1.mode = 'ELEMENT'
			compare_1.operation = 'LESS_THAN'
			#B
			compare_1.inputs[1].default_value = -0.5
			
			#node Group Input.001
			group_input_001_1 = hbond_energy.nodes.new("NodeGroupInput")
			group_input_001_1.name = "Group Input.001"
			
			
			
			
			#Set locations
			group_output_4.location = (900.0, 40.0)
			group_input_4.location = (-644.257568359375, 10.571624755859375)
			group_003.location = (-355.197021484375, 210.6334228515625)
			group_008.location = (-360.0, 69.3665771484375)
			group_009.location = (-360.0, -70.6334228515625)
			group_010.location = (-360.0, -210.6334228515625)
			math_002_1.location = (-180.0, 60.0)
			math_003.location = (-180.0, -80.0)
			math_004.location = (-180.0, -220.0)
			math_005.location = (320.0, 100.0)
			math_006.location = (480.0, 100.0)
			vector_math.location = (480.0, -60.0)
			math_007.location = (160.0, 100.0)
			compare_1.location = (720.0, 220.0)
			group_input_001_1.location = (320.0, -60.0)
			
			#Set dimensions
			group_output_4.width, group_output_4.height = 140.0, 100.0
			group_input_4.width, group_input_4.height = 140.0, 100.0
			group_003.width, group_003.height = 140.0, 100.0
			group_008.width, group_008.height = 140.0, 100.0
			group_009.width, group_009.height = 140.0, 100.0
			group_010.width, group_010.height = 140.0, 100.0
			math_002_1.width, math_002_1.height = 140.0, 100.0
			math_003.width, math_003.height = 140.0, 100.0
			math_004.width, math_004.height = 140.0, 100.0
			math_005.width, math_005.height = 140.0, 100.0
			math_006.width, math_006.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			math_007.width, math_007.height = 140.0, 100.0
			compare_1.width, compare_1.height = 140.0, 100.0
			group_input_001_1.width, group_input_001_1.height = 140.0, 100.0
			
			#initialize hbond_energy links
			#math_002_1.Value -> math_003.Value
			hbond_energy.links.new(math_002_1.outputs[0], math_003.inputs[0])
			#group_009.Value -> math_003.Value
			hbond_energy.links.new(group_009.outputs[0], math_003.inputs[1])
			#math_007.Value -> math_005.Value
			hbond_energy.links.new(math_007.outputs[0], math_005.inputs[0])
			#group_008.Value -> math_002_1.Value
			hbond_energy.links.new(group_008.outputs[0], math_002_1.inputs[1])
			#math_003.Value -> math_004.Value
			hbond_energy.links.new(math_003.outputs[0], math_004.inputs[0])
			#group_010.Value -> math_004.Value
			hbond_energy.links.new(group_010.outputs[0], math_004.inputs[1])
			#group_003.Value -> math_002_1.Value
			hbond_energy.links.new(group_003.outputs[0], math_002_1.inputs[0])
			#math_005.Value -> math_006.Value
			hbond_energy.links.new(math_005.outputs[0], math_006.inputs[0])
			#math_006.Value -> group_output_4.Bond Energy
			hbond_energy.links.new(math_006.outputs[0], group_output_4.inputs[1])
			#math_004.Value -> math_007.Value
			hbond_energy.links.new(math_004.outputs[0], math_007.inputs[0])
			#vector_math.Vector -> group_output_4.Bond Vector
			hbond_energy.links.new(vector_math.outputs[0], group_output_4.inputs[2])
			#math_006.Value -> compare_1.A
			hbond_energy.links.new(math_006.outputs[0], compare_1.inputs[0])
			#compare_1.Result -> group_output_4.Is Bonded
			hbond_energy.links.new(compare_1.outputs[0], group_output_4.inputs[0])
			#group_input_4.O -> group_003.Vector
			hbond_energy.links.new(group_input_4.outputs[0], group_003.inputs[0])
			#group_input_4.N -> group_003.Vector
			hbond_energy.links.new(group_input_4.outputs[2], group_003.inputs[1])
			#group_input_4.C -> group_008.Vector
			hbond_energy.links.new(group_input_4.outputs[1], group_008.inputs[0])
			#group_input_4.H -> group_008.Vector
			hbond_energy.links.new(group_input_4.outputs[3], group_008.inputs[1])
			#group_input_4.O -> group_009.Vector
			hbond_energy.links.new(group_input_4.outputs[0], group_009.inputs[0])
			#group_input_4.H -> group_009.Vector
			hbond_energy.links.new(group_input_4.outputs[3], group_009.inputs[1])
			#group_input_4.C -> group_010.Vector
			hbond_energy.links.new(group_input_4.outputs[1], group_010.inputs[0])
			#group_input_4.N -> group_010.Vector
			hbond_energy.links.new(group_input_4.outputs[2], group_010.inputs[1])
			#group_input_001_1.H -> vector_math.Vector
			hbond_energy.links.new(group_input_001_1.outputs[3], vector_math.inputs[1])
			#group_input_001_1.O -> vector_math.Vector
			hbond_energy.links.new(group_input_001_1.outputs[0], vector_math.inputs[0])
			return hbond_energy

		hbond_energy = hbond_energy_node_group()

		#initialize offset_vector node group
		def offset_vector_node_group():
			offset_vector = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Offset Vector")

			offset_vector.color_tag = 'CONVERTER'
			offset_vector.description = ""

			
			#offset_vector interface
			#Socket Value
			value_socket_1 = offset_vector.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			value_socket_1.default_value = (0.0, 0.0, 0.0)
			value_socket_1.min_value = -3.4028234663852886e+38
			value_socket_1.max_value = 3.4028234663852886e+38
			value_socket_1.subtype = 'NONE'
			value_socket_1.attribute_domain = 'POINT'
			
			#Socket Index
			index_socket = offset_vector.interface.new_socket(name = "Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			index_socket.default_value = 0
			index_socket.min_value = 0
			index_socket.max_value = 2147483647
			index_socket.subtype = 'NONE'
			index_socket.attribute_domain = 'POINT'
			
			#Socket Position
			position_socket = offset_vector.interface.new_socket(name = "Position", in_out='INPUT', socket_type = 'NodeSocketVector')
			position_socket.default_value = (0.0, 0.0, 0.0)
			position_socket.min_value = -3.4028234663852886e+38
			position_socket.max_value = 3.4028234663852886e+38
			position_socket.subtype = 'NONE'
			position_socket.attribute_domain = 'POINT'
			position_socket.hide_value = True
			
			#Socket Offset
			offset_socket = offset_vector.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket.default_value = 0
			offset_socket.min_value = -2147483647
			offset_socket.max_value = 2147483647
			offset_socket.subtype = 'NONE'
			offset_socket.attribute_domain = 'POINT'
			
			
			#initialize offset_vector nodes
			#node Group Output
			group_output_5 = offset_vector.nodes.new("NodeGroupOutput")
			group_output_5.name = "Group Output"
			group_output_5.is_active_output = True
			
			#node Group Input
			group_input_5 = offset_vector.nodes.new("NodeGroupInput")
			group_input_5.name = "Group Input"
			
			#node Evaluate at Index
			evaluate_at_index = offset_vector.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index.name = "Evaluate at Index"
			evaluate_at_index.data_type = 'FLOAT_VECTOR'
			evaluate_at_index.domain = 'POINT'
			
			#node Math
			math_2 = offset_vector.nodes.new("ShaderNodeMath")
			math_2.name = "Math"
			math_2.operation = 'ADD'
			math_2.use_clamp = False
			
			
			
			
			#Set locations
			group_output_5.location = (300.0, 20.0)
			group_input_5.location = (-273.81378173828125, 0.0)
			evaluate_at_index.location = (120.0, 20.0)
			math_2.location = (-60.0, 20.0)
			
			#Set dimensions
			group_output_5.width, group_output_5.height = 140.0, 100.0
			group_input_5.width, group_input_5.height = 140.0, 100.0
			evaluate_at_index.width, evaluate_at_index.height = 140.0, 100.0
			math_2.width, math_2.height = 140.0, 100.0
			
			#initialize offset_vector links
			#group_input_5.Position -> evaluate_at_index.Value
			offset_vector.links.new(group_input_5.outputs[1], evaluate_at_index.inputs[1])
			#evaluate_at_index.Value -> group_output_5.Value
			offset_vector.links.new(evaluate_at_index.outputs[0], group_output_5.inputs[0])
			#group_input_5.Index -> math_2.Value
			offset_vector.links.new(group_input_5.outputs[0], math_2.inputs[0])
			#group_input_5.Offset -> math_2.Value
			offset_vector.links.new(group_input_5.outputs[2], math_2.inputs[1])
			#math_2.Value -> evaluate_at_index.Index
			offset_vector.links.new(math_2.outputs[0], evaluate_at_index.inputs[0])
			return offset_vector

		offset_vector = offset_vector_node_group()

		#initialize mn_units node group
		def mn_units_node_group():
			mn_units = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "MN Units")

			mn_units.color_tag = 'NONE'
			mn_units.description = ""

			
			#mn_units interface
			#Socket Angstrom
			angstrom_socket_1 = mn_units.interface.new_socket(name = "Angstrom", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			angstrom_socket_1.default_value = 0.0
			angstrom_socket_1.min_value = -3.4028234663852886e+38
			angstrom_socket_1.max_value = 3.4028234663852886e+38
			angstrom_socket_1.subtype = 'NONE'
			angstrom_socket_1.attribute_domain = 'POINT'
			
			#Socket Nanometre
			nanometre_socket = mn_units.interface.new_socket(name = "Nanometre", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			nanometre_socket.default_value = 0.0
			nanometre_socket.min_value = -3.4028234663852886e+38
			nanometre_socket.max_value = 3.4028234663852886e+38
			nanometre_socket.subtype = 'NONE'
			nanometre_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_2 = mn_units.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket_2.default_value = 3.0
			value_socket_2.min_value = -10000.0
			value_socket_2.max_value = 10000.0
			value_socket_2.subtype = 'NONE'
			value_socket_2.attribute_domain = 'POINT'
			value_socket_2.description = "A value which will be scaled appropriately for the world"
			
			
			#initialize mn_units nodes
			#node Group Output
			group_output_6 = mn_units.nodes.new("NodeGroupOutput")
			group_output_6.name = "Group Output"
			group_output_6.is_active_output = True
			
			#node Group Input
			group_input_6 = mn_units.nodes.new("NodeGroupInput")
			group_input_6.name = "Group Input"
			
			#node Math
			math_3 = mn_units.nodes.new("ShaderNodeMath")
			math_3.name = "Math"
			math_3.operation = 'MULTIPLY'
			math_3.use_clamp = False
			
			#node Math.001
			math_001 = mn_units.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.operation = 'MULTIPLY'
			math_001.use_clamp = False
			#Value_001
			math_001.inputs[1].default_value = 10.0
			
			#node Group
			group_1 = mn_units.nodes.new("GeometryNodeGroup")
			group_1.name = "Group"
			group_1.node_tree = _mn_world_scale
			
			
			
			
			#Set locations
			group_output_6.location = (190.0, 0.0)
			group_input_6.location = (-240.0, 0.0)
			math_3.location = (-60.0, 0.0)
			math_001.location = (-60.0, -160.0)
			group_1.location = (-304.00421142578125, -104.114013671875)
			
			#Set dimensions
			group_output_6.width, group_output_6.height = 140.0, 100.0
			group_input_6.width, group_input_6.height = 140.0, 100.0
			math_3.width, math_3.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			group_1.width, group_1.height = 197.58424377441406, 100.0
			
			#initialize mn_units links
			#math_3.Value -> group_output_6.Angstrom
			mn_units.links.new(math_3.outputs[0], group_output_6.inputs[0])
			#group_input_6.Value -> math_3.Value
			mn_units.links.new(group_input_6.outputs[0], math_3.inputs[0])
			#group_1.world_scale -> math_3.Value
			mn_units.links.new(group_1.outputs[0], math_3.inputs[1])
			#math_3.Value -> math_001.Value
			mn_units.links.new(math_3.outputs[0], math_001.inputs[0])
			#math_001.Value -> group_output_6.Nanometre
			mn_units.links.new(math_001.outputs[0], group_output_6.inputs[1])
			return mn_units

		mn_units = mn_units_node_group()

		#initialize backbone_nh node group
		def backbone_nh_node_group():
			backbone_nh = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Backbone NH")

			backbone_nh.color_tag = 'NONE'
			backbone_nh.description = ""

			
			#backbone_nh interface
			#Socket H
			h_socket_1 = backbone_nh.interface.new_socket(name = "H", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			h_socket_1.default_value = (0.0, 0.0, 0.0)
			h_socket_1.min_value = -3.4028234663852886e+38
			h_socket_1.max_value = 3.4028234663852886e+38
			h_socket_1.subtype = 'NONE'
			h_socket_1.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_3 = backbone_nh.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket_3.default_value = 1.0
			value_socket_3.min_value = -10000.0
			value_socket_3.max_value = 10000.0
			value_socket_3.subtype = 'NONE'
			value_socket_3.attribute_domain = 'POINT'
			
			
			#initialize backbone_nh nodes
			#node Group Output
			group_output_7 = backbone_nh.nodes.new("NodeGroupOutput")
			group_output_7.name = "Group Output"
			group_output_7.is_active_output = True
			
			#node Group Input
			group_input_7 = backbone_nh.nodes.new("NodeGroupInput")
			group_input_7.name = "Group Input"
			
			#node Named Attribute
			named_attribute = backbone_nh.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute.inputs[0].default_value = "backbone_N"
			
			#node Named Attribute.001
			named_attribute_001 = backbone_nh.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_001.inputs[0].default_value = "backbone_CA"
			
			#node Named Attribute.002
			named_attribute_002 = backbone_nh.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002.name = "Named Attribute.002"
			named_attribute_002.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_002.inputs[0].default_value = "backbone_C"
			
			#node Group.002
			group_002 = backbone_nh.nodes.new("GeometryNodeGroup")
			group_002.name = "Group.002"
			group_002.node_tree = offset_vector
			#Socket_2
			group_002.inputs[0].default_value = 0
			#Socket_3
			group_002.inputs[2].default_value = -1
			
			#node Vector Math
			vector_math_1 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_1.name = "Vector Math"
			vector_math_1.operation = 'SUBTRACT'
			
			#node Vector Math.001
			vector_math_001 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_001.name = "Vector Math.001"
			vector_math_001.operation = 'SUBTRACT'
			
			#node Vector Math.002
			vector_math_002_1 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_002_1.name = "Vector Math.002"
			vector_math_002_1.operation = 'NORMALIZE'
			
			#node Vector Math.003
			vector_math_003 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_003.name = "Vector Math.003"
			vector_math_003.operation = 'NORMALIZE'
			
			#node Vector Math.005
			vector_math_005 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_005.name = "Vector Math.005"
			vector_math_005.operation = 'ADD'
			
			#node Vector Math.006
			vector_math_006 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_006.name = "Vector Math.006"
			vector_math_006.operation = 'ADD'
			
			#node Vector Math.004
			vector_math_004 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_004.name = "Vector Math.004"
			vector_math_004.operation = 'SCALE'
			
			#node Group.003
			group_003_1 = backbone_nh.nodes.new("GeometryNodeGroup")
			group_003_1.name = "Group.003"
			group_003_1.node_tree = mn_units
			
			#node Vector Math.007
			vector_math_007 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_007.name = "Vector Math.007"
			vector_math_007.operation = 'NORMALIZE'
			
			
			
			
			#Set locations
			group_output_7.location = (620.0, 0.0)
			group_input_7.location = (-630.0, 0.0)
			named_attribute.location = (-430.0, 140.0)
			named_attribute_001.location = (-430.0, 0.0)
			named_attribute_002.location = (-430.0, -140.0)
			group_002.location = (-210.0, -120.0)
			vector_math_1.location = (-50.0, 0.0)
			vector_math_001.location = (-50.0, 140.0)
			vector_math_002_1.location = (110.0, 140.0)
			vector_math_003.location = (110.0, 0.0)
			vector_math_005.location = (270.0, 140.0)
			vector_math_006.location = (430.0, 140.0)
			vector_math_004.location = (260.0, -120.0)
			group_003_1.location = (100.0, -120.0)
			vector_math_007.location = (260.0, 0.0)
			
			#Set dimensions
			group_output_7.width, group_output_7.height = 140.0, 100.0
			group_input_7.width, group_input_7.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 189.579833984375, 100.0
			named_attribute_001.width, named_attribute_001.height = 189.579833984375, 100.0
			named_attribute_002.width, named_attribute_002.height = 189.579833984375, 100.0
			group_002.width, group_002.height = 140.0, 100.0
			vector_math_1.width, vector_math_1.height = 140.0, 100.0
			vector_math_001.width, vector_math_001.height = 140.0, 100.0
			vector_math_002_1.width, vector_math_002_1.height = 140.0, 100.0
			vector_math_003.width, vector_math_003.height = 140.0, 100.0
			vector_math_005.width, vector_math_005.height = 140.0, 100.0
			vector_math_006.width, vector_math_006.height = 140.0, 100.0
			vector_math_004.width, vector_math_004.height = 140.0, 100.0
			group_003_1.width, group_003_1.height = 140.0, 100.0
			vector_math_007.width, vector_math_007.height = 140.0, 100.0
			
			#initialize backbone_nh links
			#vector_math_004.Vector -> vector_math_006.Vector
			backbone_nh.links.new(vector_math_004.outputs[0], vector_math_006.inputs[1])
			#named_attribute_001.Attribute -> vector_math_001.Vector
			backbone_nh.links.new(named_attribute_001.outputs[0], vector_math_001.inputs[1])
			#named_attribute_002.Attribute -> group_002.Position
			backbone_nh.links.new(named_attribute_002.outputs[0], group_002.inputs[1])
			#named_attribute.Attribute -> vector_math_1.Vector
			backbone_nh.links.new(named_attribute.outputs[0], vector_math_1.inputs[0])
			#vector_math_1.Vector -> vector_math_003.Vector
			backbone_nh.links.new(vector_math_1.outputs[0], vector_math_003.inputs[0])
			#group_003_1.Angstrom -> vector_math_004.Scale
			backbone_nh.links.new(group_003_1.outputs[0], vector_math_004.inputs[3])
			#vector_math_003.Vector -> vector_math_005.Vector
			backbone_nh.links.new(vector_math_003.outputs[0], vector_math_005.inputs[1])
			#group_002.Value -> vector_math_1.Vector
			backbone_nh.links.new(group_002.outputs[0], vector_math_1.inputs[1])
			#vector_math_002_1.Vector -> vector_math_005.Vector
			backbone_nh.links.new(vector_math_002_1.outputs[0], vector_math_005.inputs[0])
			#named_attribute.Attribute -> vector_math_001.Vector
			backbone_nh.links.new(named_attribute.outputs[0], vector_math_001.inputs[0])
			#vector_math_001.Vector -> vector_math_002_1.Vector
			backbone_nh.links.new(vector_math_001.outputs[0], vector_math_002_1.inputs[0])
			#named_attribute.Attribute -> vector_math_006.Vector
			backbone_nh.links.new(named_attribute.outputs[0], vector_math_006.inputs[0])
			#vector_math_006.Vector -> group_output_7.H
			backbone_nh.links.new(vector_math_006.outputs[0], group_output_7.inputs[0])
			#group_input_7.Value -> group_003_1.Value
			backbone_nh.links.new(group_input_7.outputs[0], group_003_1.inputs[0])
			#vector_math_005.Vector -> vector_math_007.Vector
			backbone_nh.links.new(vector_math_005.outputs[0], vector_math_007.inputs[0])
			#vector_math_007.Vector -> vector_math_004.Vector
			backbone_nh.links.new(vector_math_007.outputs[0], vector_math_004.inputs[0])
			return backbone_nh

		backbone_nh = backbone_nh_node_group()

		#initialize mn_topo_backbone node group
		def mn_topo_backbone_node_group():
			mn_topo_backbone = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "MN_topo_backbone")

			mn_topo_backbone.color_tag = 'NONE'
			mn_topo_backbone.description = ""

			
			#mn_topo_backbone interface
			#Socket O
			o_socket_1 = mn_topo_backbone.interface.new_socket(name = "O", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			o_socket_1.default_value = (0.0, 0.0, 0.0)
			o_socket_1.min_value = -3.4028234663852886e+38
			o_socket_1.max_value = 3.4028234663852886e+38
			o_socket_1.subtype = 'NONE'
			o_socket_1.attribute_domain = 'POINT'
			
			#Socket C
			c_socket_1 = mn_topo_backbone.interface.new_socket(name = "C", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			c_socket_1.default_value = (0.0, 0.0, 0.0)
			c_socket_1.min_value = -3.4028234663852886e+38
			c_socket_1.max_value = 3.4028234663852886e+38
			c_socket_1.subtype = 'NONE'
			c_socket_1.attribute_domain = 'POINT'
			
			#Socket CA
			ca_socket = mn_topo_backbone.interface.new_socket(name = "CA", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			ca_socket.default_value = (0.0, 0.0, 0.0)
			ca_socket.min_value = -3.4028234663852886e+38
			ca_socket.max_value = 3.4028234663852886e+38
			ca_socket.subtype = 'NONE'
			ca_socket.attribute_domain = 'POINT'
			
			#Socket N
			n_socket_1 = mn_topo_backbone.interface.new_socket(name = "N", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			n_socket_1.default_value = (0.0, 0.0, 0.0)
			n_socket_1.min_value = -3.4028234663852886e+38
			n_socket_1.max_value = 3.4028234663852886e+38
			n_socket_1.subtype = 'NONE'
			n_socket_1.attribute_domain = 'POINT'
			
			#Socket NH
			nh_socket = mn_topo_backbone.interface.new_socket(name = "NH", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			nh_socket.default_value = (0.0, 0.0, 0.0)
			nh_socket.min_value = -3.4028234663852886e+38
			nh_socket.max_value = 3.4028234663852886e+38
			nh_socket.subtype = 'NONE'
			nh_socket.attribute_domain = 'POINT'
			
			#Socket Offset
			offset_socket_1 = mn_topo_backbone.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket_1.default_value = 0
			offset_socket_1.min_value = -2147483648
			offset_socket_1.max_value = 2147483647
			offset_socket_1.subtype = 'NONE'
			offset_socket_1.attribute_domain = 'POINT'
			
			
			#initialize mn_topo_backbone nodes
			#node Group Output
			group_output_8 = mn_topo_backbone.nodes.new("NodeGroupOutput")
			group_output_8.name = "Group Output"
			group_output_8.is_active_output = True
			
			#node Group Input
			group_input_8 = mn_topo_backbone.nodes.new("NodeGroupInput")
			group_input_8.name = "Group Input"
			
			#node Named Attribute.001
			named_attribute_001_1 = mn_topo_backbone.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001_1.name = "Named Attribute.001"
			named_attribute_001_1.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_001_1.inputs[0].default_value = "backbone_O"
			
			#node Named Attribute.002
			named_attribute_002_1 = mn_topo_backbone.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002_1.name = "Named Attribute.002"
			named_attribute_002_1.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_002_1.inputs[0].default_value = "backbone_C"
			
			#node Evaluate at Index
			evaluate_at_index_1 = mn_topo_backbone.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_1.name = "Evaluate at Index"
			evaluate_at_index_1.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_1.domain = 'POINT'
			
			#node Math
			math_4 = mn_topo_backbone.nodes.new("ShaderNodeMath")
			math_4.name = "Math"
			math_4.operation = 'ADD'
			math_4.use_clamp = False
			
			#node Index
			index = mn_topo_backbone.nodes.new("GeometryNodeInputIndex")
			index.name = "Index"
			
			#node Evaluate at Index.001
			evaluate_at_index_001 = mn_topo_backbone.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001.name = "Evaluate at Index.001"
			evaluate_at_index_001.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_001.domain = 'POINT'
			
			#node Named Attribute.003
			named_attribute_003 = mn_topo_backbone.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_003.name = "Named Attribute.003"
			named_attribute_003.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_003.inputs[0].default_value = "backbone_CA"
			
			#node Evaluate at Index.002
			evaluate_at_index_002 = mn_topo_backbone.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_002.name = "Evaluate at Index.002"
			evaluate_at_index_002.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_002.domain = 'POINT'
			
			#node Evaluate at Index.003
			evaluate_at_index_003 = mn_topo_backbone.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_003.name = "Evaluate at Index.003"
			evaluate_at_index_003.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_003.domain = 'POINT'
			
			#node Named Attribute.004
			named_attribute_004 = mn_topo_backbone.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_004.name = "Named Attribute.004"
			named_attribute_004.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_004.inputs[0].default_value = "backbone_N"
			
			#node Reroute
			reroute_1 = mn_topo_backbone.nodes.new("NodeReroute")
			reroute_1.name = "Reroute"
			#node Group
			group_2 = mn_topo_backbone.nodes.new("GeometryNodeGroup")
			group_2.name = "Group"
			group_2.node_tree = backbone_nh
			#Socket_1
			group_2.inputs[0].default_value = 1.0099999904632568
			
			#node Evaluate at Index.004
			evaluate_at_index_004 = mn_topo_backbone.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_004.name = "Evaluate at Index.004"
			evaluate_at_index_004.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_004.domain = 'POINT'
			
			#node Named Attribute.005
			named_attribute_005 = mn_topo_backbone.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_005.name = "Named Attribute.005"
			named_attribute_005.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_005.inputs[0].default_value = "backbone_NH"
			
			#node Switch
			switch = mn_topo_backbone.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'VECTOR'
			
			#node Boolean Math
			boolean_math = mn_topo_backbone.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'NOT'
			
			
			
			
			#Set locations
			group_output_8.location = (320.0, -220.0)
			group_input_8.location = (-520.0, -260.0)
			named_attribute_001_1.location = (-300.0, 40.0)
			named_attribute_002_1.location = (-300.0, -100.0)
			evaluate_at_index_1.location = (80.0, -14.04681396484375)
			math_4.location = (-260.0, -260.0)
			index.location = (-520.0, -360.0)
			evaluate_at_index_001.location = (80.0, -170.47593688964844)
			named_attribute_003.location = (-300.0, -460.0)
			evaluate_at_index_002.location = (80.0, -326.90509033203125)
			evaluate_at_index_003.location = (80.0, -480.0)
			named_attribute_004.location = (-300.0, -600.0)
			reroute_1.location = (20.0, -340.0)
			group_2.location = (-640.0, -920.0)
			evaluate_at_index_004.location = (77.81956481933594, -655.5125732421875)
			named_attribute_005.location = (-640.0, -780.0)
			switch.location = (-240.0, -780.0)
			boolean_math.location = (-420.0, -780.0)
			
			#Set dimensions
			group_output_8.width, group_output_8.height = 140.0, 100.0
			group_input_8.width, group_input_8.height = 140.0, 100.0
			named_attribute_001_1.width, named_attribute_001_1.height = 186.42977905273438, 100.0
			named_attribute_002_1.width, named_attribute_002_1.height = 186.42977905273438, 100.0
			evaluate_at_index_1.width, evaluate_at_index_1.height = 140.0, 100.0
			math_4.width, math_4.height = 140.0, 100.0
			index.width, index.height = 140.0, 100.0
			evaluate_at_index_001.width, evaluate_at_index_001.height = 140.0, 100.0
			named_attribute_003.width, named_attribute_003.height = 186.42977905273438, 100.0
			evaluate_at_index_002.width, evaluate_at_index_002.height = 140.0, 100.0
			evaluate_at_index_003.width, evaluate_at_index_003.height = 140.0, 100.0
			named_attribute_004.width, named_attribute_004.height = 186.42977905273438, 100.0
			reroute_1.width, reroute_1.height = 16.0, 100.0
			group_2.width, group_2.height = 186.0294189453125, 100.0
			evaluate_at_index_004.width, evaluate_at_index_004.height = 140.0, 100.0
			named_attribute_005.width, named_attribute_005.height = 186.42977905273438, 100.0
			switch.width, switch.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			
			#initialize mn_topo_backbone links
			#named_attribute_001_1.Attribute -> evaluate_at_index_1.Value
			mn_topo_backbone.links.new(named_attribute_001_1.outputs[0], evaluate_at_index_1.inputs[1])
			#reroute_1.Output -> evaluate_at_index_1.Index
			mn_topo_backbone.links.new(reroute_1.outputs[0], evaluate_at_index_1.inputs[0])
			#group_input_8.Offset -> math_4.Value
			mn_topo_backbone.links.new(group_input_8.outputs[0], math_4.inputs[0])
			#reroute_1.Output -> evaluate_at_index_001.Index
			mn_topo_backbone.links.new(reroute_1.outputs[0], evaluate_at_index_001.inputs[0])
			#named_attribute_002_1.Attribute -> evaluate_at_index_001.Value
			mn_topo_backbone.links.new(named_attribute_002_1.outputs[0], evaluate_at_index_001.inputs[1])
			#reroute_1.Output -> evaluate_at_index_002.Index
			mn_topo_backbone.links.new(reroute_1.outputs[0], evaluate_at_index_002.inputs[0])
			#named_attribute_003.Attribute -> evaluate_at_index_002.Value
			mn_topo_backbone.links.new(named_attribute_003.outputs[0], evaluate_at_index_002.inputs[1])
			#reroute_1.Output -> evaluate_at_index_003.Index
			mn_topo_backbone.links.new(reroute_1.outputs[0], evaluate_at_index_003.inputs[0])
			#named_attribute_004.Attribute -> evaluate_at_index_003.Value
			mn_topo_backbone.links.new(named_attribute_004.outputs[0], evaluate_at_index_003.inputs[1])
			#index.Index -> math_4.Value
			mn_topo_backbone.links.new(index.outputs[0], math_4.inputs[1])
			#math_4.Value -> reroute_1.Input
			mn_topo_backbone.links.new(math_4.outputs[0], reroute_1.inputs[0])
			#evaluate_at_index_003.Value -> group_output_8.N
			mn_topo_backbone.links.new(evaluate_at_index_003.outputs[0], group_output_8.inputs[3])
			#evaluate_at_index_002.Value -> group_output_8.CA
			mn_topo_backbone.links.new(evaluate_at_index_002.outputs[0], group_output_8.inputs[2])
			#evaluate_at_index_001.Value -> group_output_8.C
			mn_topo_backbone.links.new(evaluate_at_index_001.outputs[0], group_output_8.inputs[1])
			#evaluate_at_index_1.Value -> group_output_8.O
			mn_topo_backbone.links.new(evaluate_at_index_1.outputs[0], group_output_8.inputs[0])
			#reroute_1.Output -> evaluate_at_index_004.Index
			mn_topo_backbone.links.new(reroute_1.outputs[0], evaluate_at_index_004.inputs[0])
			#evaluate_at_index_004.Value -> group_output_8.NH
			mn_topo_backbone.links.new(evaluate_at_index_004.outputs[0], group_output_8.inputs[4])
			#group_2.H -> switch.True
			mn_topo_backbone.links.new(group_2.outputs[0], switch.inputs[2])
			#switch.Output -> evaluate_at_index_004.Value
			mn_topo_backbone.links.new(switch.outputs[0], evaluate_at_index_004.inputs[1])
			#named_attribute_005.Exists -> boolean_math.Boolean
			mn_topo_backbone.links.new(named_attribute_005.outputs[1], boolean_math.inputs[0])
			#boolean_math.Boolean -> switch.Switch
			mn_topo_backbone.links.new(boolean_math.outputs[0], switch.inputs[0])
			#named_attribute_005.Attribute -> switch.False
			mn_topo_backbone.links.new(named_attribute_005.outputs[0], switch.inputs[1])
			return mn_topo_backbone

		mn_topo_backbone = mn_topo_backbone_node_group()

		#initialize hbond_backbone_check node group
		def hbond_backbone_check_node_group():
			hbond_backbone_check = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "HBond Backbone Check")

			hbond_backbone_check.color_tag = 'NONE'
			hbond_backbone_check.description = ""

			
			#hbond_backbone_check interface
			#Socket Is Bonded
			is_bonded_socket_1 = hbond_backbone_check.interface.new_socket(name = "Is Bonded", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_bonded_socket_1.default_value = False
			is_bonded_socket_1.attribute_domain = 'POINT'
			
			#Socket Bond Energy
			bond_energy_socket_1 = hbond_backbone_check.interface.new_socket(name = "Bond Energy", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			bond_energy_socket_1.default_value = 0.0
			bond_energy_socket_1.min_value = -3.4028234663852886e+38
			bond_energy_socket_1.max_value = 3.4028234663852886e+38
			bond_energy_socket_1.subtype = 'NONE'
			bond_energy_socket_1.attribute_domain = 'POINT'
			
			#Socket H->O
			h__o_socket = hbond_backbone_check.interface.new_socket(name = "H->O", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			h__o_socket.default_value = (0.0, 0.0, 0.0)
			h__o_socket.min_value = -3.4028234663852886e+38
			h__o_socket.max_value = 3.4028234663852886e+38
			h__o_socket.subtype = 'NONE'
			h__o_socket.attribute_domain = 'POINT'
			
			#Panel CO
			co_panel = hbond_backbone_check.interface.new_panel("CO")
			#Socket CO Index
			co_index_socket = hbond_backbone_check.interface.new_socket(name = "CO Index", in_out='INPUT', socket_type = 'NodeSocketInt', parent = co_panel)
			co_index_socket.default_value = 0
			co_index_socket.min_value = 0
			co_index_socket.max_value = 2147483647
			co_index_socket.subtype = 'NONE'
			co_index_socket.attribute_domain = 'POINT'
			
			#Socket CO Offset
			co_offset_socket = hbond_backbone_check.interface.new_socket(name = "CO Offset", in_out='INPUT', socket_type = 'NodeSocketInt', parent = co_panel)
			co_offset_socket.default_value = 0
			co_offset_socket.min_value = -2147483648
			co_offset_socket.max_value = 2147483647
			co_offset_socket.subtype = 'NONE'
			co_offset_socket.attribute_domain = 'POINT'
			
			
			#Panel NH
			nh_panel = hbond_backbone_check.interface.new_panel("NH")
			#Socket NH Index
			nh_index_socket = hbond_backbone_check.interface.new_socket(name = "NH Index", in_out='INPUT', socket_type = 'NodeSocketInt', parent = nh_panel)
			nh_index_socket.default_value = 0
			nh_index_socket.min_value = 0
			nh_index_socket.max_value = 2147483647
			nh_index_socket.subtype = 'NONE'
			nh_index_socket.attribute_domain = 'POINT'
			
			#Socket NH Offset
			nh_offset_socket = hbond_backbone_check.interface.new_socket(name = "NH Offset", in_out='INPUT', socket_type = 'NodeSocketInt', parent = nh_panel)
			nh_offset_socket.default_value = 0
			nh_offset_socket.min_value = -2147483648
			nh_offset_socket.max_value = 2147483647
			nh_offset_socket.subtype = 'NONE'
			nh_offset_socket.attribute_domain = 'POINT'
			
			
			
			#initialize hbond_backbone_check nodes
			#node Group Output
			group_output_9 = hbond_backbone_check.nodes.new("NodeGroupOutput")
			group_output_9.name = "Group Output"
			group_output_9.is_active_output = True
			
			#node Group Input
			group_input_9 = hbond_backbone_check.nodes.new("NodeGroupInput")
			group_input_9.name = "Group Input"
			
			#node Group.008
			group_008_1 = hbond_backbone_check.nodes.new("GeometryNodeGroup")
			group_008_1.name = "Group.008"
			group_008_1.node_tree = hbond_energy
			
			#node Group.009
			group_009_1 = hbond_backbone_check.nodes.new("GeometryNodeGroup")
			group_009_1.name = "Group.009"
			group_009_1.node_tree = mn_topo_backbone
			#Socket_3
			group_009_1.inputs[0].default_value = 0
			
			#node Evaluate at Index
			evaluate_at_index_2 = hbond_backbone_check.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_2.name = "Evaluate at Index"
			evaluate_at_index_2.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_2.domain = 'POINT'
			
			#node Evaluate at Index.001
			evaluate_at_index_001_1 = hbond_backbone_check.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001_1.name = "Evaluate at Index.001"
			evaluate_at_index_001_1.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_001_1.domain = 'POINT'
			
			#node Evaluate at Index.002
			evaluate_at_index_002_1 = hbond_backbone_check.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_002_1.name = "Evaluate at Index.002"
			evaluate_at_index_002_1.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_002_1.domain = 'POINT'
			
			#node Evaluate at Index.003
			evaluate_at_index_003_1 = hbond_backbone_check.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_003_1.name = "Evaluate at Index.003"
			evaluate_at_index_003_1.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_003_1.domain = 'POINT'
			
			#node Math
			math_5 = hbond_backbone_check.nodes.new("ShaderNodeMath")
			math_5.name = "Math"
			math_5.operation = 'ADD'
			math_5.use_clamp = False
			
			#node Math.001
			math_001_1 = hbond_backbone_check.nodes.new("ShaderNodeMath")
			math_001_1.name = "Math.001"
			math_001_1.operation = 'ADD'
			math_001_1.use_clamp = False
			
			#node Math.002
			math_002_2 = hbond_backbone_check.nodes.new("ShaderNodeMath")
			math_002_2.name = "Math.002"
			math_002_2.operation = 'SUBTRACT'
			math_002_2.use_clamp = False
			
			#node Math.003
			math_003_1 = hbond_backbone_check.nodes.new("ShaderNodeMath")
			math_003_1.name = "Math.003"
			math_003_1.operation = 'ABSOLUTE'
			math_003_1.use_clamp = False
			
			#node Compare
			compare_2 = hbond_backbone_check.nodes.new("FunctionNodeCompare")
			compare_2.name = "Compare"
			compare_2.data_type = 'FLOAT'
			compare_2.mode = 'ELEMENT'
			compare_2.operation = 'GREATER_THAN'
			
			#node Integer
			integer = hbond_backbone_check.nodes.new("FunctionNodeInputInt")
			integer.name = "Integer"
			integer.integer = 2
			
			#node Frame
			frame = hbond_backbone_check.nodes.new("NodeFrame")
			frame.label = "Check not bonded to +/- residues"
			frame.name = "Frame"
			frame.label_size = 20
			frame.shrink = True
			
			#node Switch
			switch_1 = hbond_backbone_check.nodes.new("GeometryNodeSwitch")
			switch_1.name = "Switch"
			switch_1.input_type = 'BOOLEAN'
			#False
			switch_1.inputs[1].default_value = False
			
			#node Compare.001
			compare_001_1 = hbond_backbone_check.nodes.new("FunctionNodeCompare")
			compare_001_1.name = "Compare.001"
			compare_001_1.data_type = 'FLOAT'
			compare_001_1.mode = 'ELEMENT'
			compare_001_1.operation = 'LESS_THAN'
			
			#node Vector Math
			vector_math_2 = hbond_backbone_check.nodes.new("ShaderNodeVectorMath")
			vector_math_2.name = "Vector Math"
			vector_math_2.operation = 'LENGTH'
			
			#node Group
			group_3 = hbond_backbone_check.nodes.new("GeometryNodeGroup")
			group_3.name = "Group"
			group_3.node_tree = mn_units
			#Input_1
			group_3.inputs[0].default_value = 3.0
			
			
			
			#Set parents
			math_002_2.parent = frame
			math_003_1.parent = frame
			compare_2.parent = frame
			integer.parent = frame
			
			#Set locations
			group_output_9.location = (820.0, 240.0)
			group_input_9.location = (-680.0, 140.0)
			group_008_1.location = (224.2731170654297, 240.0)
			group_009_1.location = (-480.0, 460.0)
			evaluate_at_index_2.location = (-20.0, 40.0)
			evaluate_at_index_001_1.location = (-20.0, -120.0)
			evaluate_at_index_002_1.location = (-20.0, 400.0)
			evaluate_at_index_003_1.location = (-20.0, 240.0)
			math_5.location = (-480.0, 240.0)
			math_001_1.location = (-480.0, 80.0)
			math_002_2.location = (70.0, 640.0)
			math_003_1.location = (240.0, 640.0)
			compare_2.location = (420.0, 640.0)
			integer.location = (240.0, 500.0)
			frame.location = (-70.0, 40.0)
			switch_1.location = (620.0, 340.0)
			compare_001_1.location = (520.0, 140.0)
			vector_math_2.location = (260.0, 20.0)
			group_3.location = (520.0, -20.0)
			
			#Set dimensions
			group_output_9.width, group_output_9.height = 140.0, 100.0
			group_input_9.width, group_input_9.height = 140.0, 100.0
			group_008_1.width, group_008_1.height = 184.92144775390625, 100.0
			group_009_1.width, group_009_1.height = 140.0, 100.0
			evaluate_at_index_2.width, evaluate_at_index_2.height = 140.0, 100.0
			evaluate_at_index_001_1.width, evaluate_at_index_001_1.height = 140.0, 100.0
			evaluate_at_index_002_1.width, evaluate_at_index_002_1.height = 140.0, 100.0
			evaluate_at_index_003_1.width, evaluate_at_index_003_1.height = 140.0, 100.0
			math_5.width, math_5.height = 140.0, 100.0
			math_001_1.width, math_001_1.height = 140.0, 100.0
			math_002_2.width, math_002_2.height = 140.0, 100.0
			math_003_1.width, math_003_1.height = 140.0, 100.0
			compare_2.width, compare_2.height = 140.0, 100.0
			integer.width, integer.height = 140.0, 100.0
			frame.width, frame.height = 550.0, 284.0
			switch_1.width, switch_1.height = 140.0, 100.0
			compare_001_1.width, compare_001_1.height = 140.0, 100.0
			vector_math_2.width, vector_math_2.height = 140.0, 100.0
			group_3.width, group_3.height = 140.0, 100.0
			
			#initialize hbond_backbone_check links
			#evaluate_at_index_001_1.Value -> group_008_1.H
			hbond_backbone_check.links.new(evaluate_at_index_001_1.outputs[0], group_008_1.inputs[3])
			#evaluate_at_index_2.Value -> group_008_1.N
			hbond_backbone_check.links.new(evaluate_at_index_2.outputs[0], group_008_1.inputs[2])
			#evaluate_at_index_002_1.Value -> group_008_1.O
			hbond_backbone_check.links.new(evaluate_at_index_002_1.outputs[0], group_008_1.inputs[0])
			#math_001_1.Value -> evaluate_at_index_001_1.Index
			hbond_backbone_check.links.new(math_001_1.outputs[0], evaluate_at_index_001_1.inputs[0])
			#math_001_1.Value -> evaluate_at_index_2.Index
			hbond_backbone_check.links.new(math_001_1.outputs[0], evaluate_at_index_2.inputs[0])
			#evaluate_at_index_003_1.Value -> group_008_1.C
			hbond_backbone_check.links.new(evaluate_at_index_003_1.outputs[0], group_008_1.inputs[1])
			#group_008_1.Bond Energy -> group_output_9.Bond Energy
			hbond_backbone_check.links.new(group_008_1.outputs[1], group_output_9.inputs[1])
			#group_008_1.Bond Vector -> group_output_9.H->O
			hbond_backbone_check.links.new(group_008_1.outputs[2], group_output_9.inputs[2])
			#math_5.Value -> evaluate_at_index_002_1.Index
			hbond_backbone_check.links.new(math_5.outputs[0], evaluate_at_index_002_1.inputs[0])
			#math_5.Value -> evaluate_at_index_003_1.Index
			hbond_backbone_check.links.new(math_5.outputs[0], evaluate_at_index_003_1.inputs[0])
			#group_input_9.CO Index -> math_5.Value
			hbond_backbone_check.links.new(group_input_9.outputs[0], math_5.inputs[0])
			#group_input_9.CO Offset -> math_5.Value
			hbond_backbone_check.links.new(group_input_9.outputs[1], math_5.inputs[1])
			#group_input_9.NH Index -> math_001_1.Value
			hbond_backbone_check.links.new(group_input_9.outputs[2], math_001_1.inputs[0])
			#group_input_9.NH Offset -> math_001_1.Value
			hbond_backbone_check.links.new(group_input_9.outputs[3], math_001_1.inputs[1])
			#math_5.Value -> math_002_2.Value
			hbond_backbone_check.links.new(math_5.outputs[0], math_002_2.inputs[0])
			#math_001_1.Value -> math_002_2.Value
			hbond_backbone_check.links.new(math_001_1.outputs[0], math_002_2.inputs[1])
			#math_002_2.Value -> math_003_1.Value
			hbond_backbone_check.links.new(math_002_2.outputs[0], math_003_1.inputs[0])
			#math_003_1.Value -> compare_2.A
			hbond_backbone_check.links.new(math_003_1.outputs[0], compare_2.inputs[0])
			#integer.Integer -> compare_2.B
			hbond_backbone_check.links.new(integer.outputs[0], compare_2.inputs[1])
			#compare_2.Result -> switch_1.Switch
			hbond_backbone_check.links.new(compare_2.outputs[0], switch_1.inputs[0])
			#group_008_1.Bond Vector -> vector_math_2.Vector
			hbond_backbone_check.links.new(group_008_1.outputs[2], vector_math_2.inputs[0])
			#vector_math_2.Value -> compare_001_1.A
			hbond_backbone_check.links.new(vector_math_2.outputs[1], compare_001_1.inputs[0])
			#group_3.Angstrom -> compare_001_1.B
			hbond_backbone_check.links.new(group_3.outputs[0], compare_001_1.inputs[1])
			#switch_1.Output -> group_output_9.Is Bonded
			hbond_backbone_check.links.new(switch_1.outputs[0], group_output_9.inputs[0])
			#group_008_1.Is Bonded -> switch_1.True
			hbond_backbone_check.links.new(group_008_1.outputs[0], switch_1.inputs[2])
			#group_009_1.O -> evaluate_at_index_002_1.Value
			hbond_backbone_check.links.new(group_009_1.outputs[0], evaluate_at_index_002_1.inputs[1])
			#group_009_1.C -> evaluate_at_index_003_1.Value
			hbond_backbone_check.links.new(group_009_1.outputs[1], evaluate_at_index_003_1.inputs[1])
			#group_009_1.N -> evaluate_at_index_2.Value
			hbond_backbone_check.links.new(group_009_1.outputs[3], evaluate_at_index_2.inputs[1])
			#group_009_1.NH -> evaluate_at_index_001_1.Value
			hbond_backbone_check.links.new(group_009_1.outputs[4], evaluate_at_index_001_1.inputs[1])
			return hbond_backbone_check

		hbond_backbone_check = hbond_backbone_check_node_group()

		#initialize boolean_run_fill node group
		def boolean_run_fill_node_group():
			boolean_run_fill = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Boolean Run Fill")

			boolean_run_fill.color_tag = 'CONVERTER'
			boolean_run_fill.description = ""

			
			#boolean_run_fill interface
			#Socket Boolean
			boolean_socket_2 = boolean_run_fill.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket_2.default_value = False
			boolean_socket_2.attribute_domain = 'POINT'
			
			#Socket Boolean
			boolean_socket_3 = boolean_run_fill.interface.new_socket(name = "Boolean", in_out='INPUT', socket_type = 'NodeSocketBool')
			boolean_socket_3.default_value = False
			boolean_socket_3.attribute_domain = 'POINT'
			boolean_socket_3.description = "Boolean array to fill runs of False"
			
			#Socket Fill Size
			fill_size_socket = boolean_run_fill.interface.new_socket(name = "Fill Size", in_out='INPUT', socket_type = 'NodeSocketInt')
			fill_size_socket.default_value = 3
			fill_size_socket.min_value = -2147483648
			fill_size_socket.max_value = 2147483647
			fill_size_socket.subtype = 'NONE'
			fill_size_socket.attribute_domain = 'POINT'
			fill_size_socket.description = "Set a run of False to True if length equal or less than Fill Size"
			
			
			#initialize boolean_run_fill nodes
			#node Group Output
			group_output_10 = boolean_run_fill.nodes.new("NodeGroupOutput")
			group_output_10.name = "Group Output"
			group_output_10.is_active_output = True
			
			#node Group Input
			group_input_10 = boolean_run_fill.nodes.new("NodeGroupInput")
			group_input_10.name = "Group Input"
			
			#node Accumulate Field
			accumulate_field_1 = boolean_run_fill.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_1.name = "Accumulate Field"
			accumulate_field_1.data_type = 'INT'
			accumulate_field_1.domain = 'POINT'
			#Group Index
			accumulate_field_1.inputs[1].default_value = 0
			
			#node Accumulate Field.001
			accumulate_field_001_1 = boolean_run_fill.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_001_1.name = "Accumulate Field.001"
			accumulate_field_001_1.data_type = 'INT'
			accumulate_field_001_1.domain = 'POINT'
			#Value
			accumulate_field_001_1.inputs[0].default_value = 1
			
			#node Compare
			compare_3 = boolean_run_fill.nodes.new("FunctionNodeCompare")
			compare_3.name = "Compare"
			compare_3.data_type = 'INT'
			compare_3.mode = 'ELEMENT'
			compare_3.operation = 'LESS_EQUAL'
			
			#node Compare.001
			compare_001_2 = boolean_run_fill.nodes.new("FunctionNodeCompare")
			compare_001_2.name = "Compare.001"
			compare_001_2.data_type = 'INT'
			compare_001_2.mode = 'ELEMENT'
			compare_001_2.operation = 'LESS_EQUAL'
			
			#node Boolean Math.010
			boolean_math_010 = boolean_run_fill.nodes.new("FunctionNodeBooleanMath")
			boolean_math_010.name = "Boolean Math.010"
			boolean_math_010.operation = 'AND'
			
			#node Boolean Math
			boolean_math_1 = boolean_run_fill.nodes.new("FunctionNodeBooleanMath")
			boolean_math_1.name = "Boolean Math"
			boolean_math_1.operation = 'OR'
			
			#node Reroute
			reroute_2 = boolean_run_fill.nodes.new("NodeReroute")
			reroute_2.name = "Reroute"
			#node Reroute.001
			reroute_001 = boolean_run_fill.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			#node Reroute.003
			reroute_003 = boolean_run_fill.nodes.new("NodeReroute")
			reroute_003.name = "Reroute.003"
			#node Reroute.002
			reroute_002 = boolean_run_fill.nodes.new("NodeReroute")
			reroute_002.name = "Reroute.002"
			
			
			
			#Set locations
			group_output_10.location = (430.0, 0.0)
			group_input_10.location = (-480.0, -20.0)
			accumulate_field_1.location = (-220.0, -120.0)
			accumulate_field_001_1.location = (-60.0, -120.0)
			compare_3.location = (100.0, -120.0)
			compare_001_2.location = (100.0, -280.0)
			boolean_math_010.location = (260.0, -120.0)
			boolean_math_1.location = (260.0, 20.0)
			reroute_2.location = (60.0, -380.0)
			reroute_001.location = (-280.0, -380.0)
			reroute_003.location = (-300.0, -80.0)
			reroute_002.location = (-240.0, -60.0)
			
			#Set dimensions
			group_output_10.width, group_output_10.height = 140.0, 100.0
			group_input_10.width, group_input_10.height = 140.0, 100.0
			accumulate_field_1.width, accumulate_field_1.height = 140.0, 100.0
			accumulate_field_001_1.width, accumulate_field_001_1.height = 140.0, 100.0
			compare_3.width, compare_3.height = 140.0, 100.0
			compare_001_2.width, compare_001_2.height = 140.0, 100.0
			boolean_math_010.width, boolean_math_010.height = 140.0, 100.0
			boolean_math_1.width, boolean_math_1.height = 140.0, 100.0
			reroute_2.width, reroute_2.height = 16.0, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			reroute_003.width, reroute_003.height = 16.0, 100.0
			reroute_002.width, reroute_002.height = 16.0, 100.0
			
			#initialize boolean_run_fill links
			#accumulate_field_001_1.Trailing -> compare_3.A
			boolean_run_fill.links.new(accumulate_field_001_1.outputs[1], compare_3.inputs[2])
			#accumulate_field_1.Leading -> accumulate_field_001_1.Group ID
			boolean_run_fill.links.new(accumulate_field_1.outputs[0], accumulate_field_001_1.inputs[1])
			#compare_001_2.Result -> boolean_math_010.Boolean
			boolean_run_fill.links.new(compare_001_2.outputs[0], boolean_math_010.inputs[1])
			#compare_3.Result -> boolean_math_010.Boolean
			boolean_run_fill.links.new(compare_3.outputs[0], boolean_math_010.inputs[0])
			#accumulate_field_001_1.Total -> compare_001_2.A
			boolean_run_fill.links.new(accumulate_field_001_1.outputs[2], compare_001_2.inputs[2])
			#reroute_2.Output -> compare_3.B
			boolean_run_fill.links.new(reroute_2.outputs[0], compare_3.inputs[3])
			#reroute_2.Output -> compare_001_2.B
			boolean_run_fill.links.new(reroute_2.outputs[0], compare_001_2.inputs[3])
			#reroute_002.Output -> accumulate_field_1.Value
			boolean_run_fill.links.new(reroute_002.outputs[0], accumulate_field_1.inputs[0])
			#reroute_002.Output -> boolean_math_1.Boolean
			boolean_run_fill.links.new(reroute_002.outputs[0], boolean_math_1.inputs[0])
			#boolean_math_010.Boolean -> boolean_math_1.Boolean
			boolean_run_fill.links.new(boolean_math_010.outputs[0], boolean_math_1.inputs[1])
			#boolean_math_1.Boolean -> group_output_10.Boolean
			boolean_run_fill.links.new(boolean_math_1.outputs[0], group_output_10.inputs[0])
			#reroute_001.Output -> reroute_2.Input
			boolean_run_fill.links.new(reroute_001.outputs[0], reroute_2.inputs[0])
			#reroute_003.Output -> reroute_001.Input
			boolean_run_fill.links.new(reroute_003.outputs[0], reroute_001.inputs[0])
			#group_input_10.Fill Size -> reroute_003.Input
			boolean_run_fill.links.new(group_input_10.outputs[1], reroute_003.inputs[0])
			#group_input_10.Boolean -> reroute_002.Input
			boolean_run_fill.links.new(group_input_10.outputs[0], reroute_002.inputs[0])
			return boolean_run_fill

		boolean_run_fill = boolean_run_fill_node_group()

		#initialize offset_boolean node group
		def offset_boolean_node_group():
			offset_boolean = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Offset Boolean")

			offset_boolean.color_tag = 'CONVERTER'
			offset_boolean.description = ""

			
			#offset_boolean interface
			#Socket Boolean
			boolean_socket_4 = offset_boolean.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket_4.default_value = False
			boolean_socket_4.attribute_domain = 'POINT'
			
			#Socket Index
			index_socket_1 = offset_boolean.interface.new_socket(name = "Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			index_socket_1.default_value = 0
			index_socket_1.min_value = 0
			index_socket_1.max_value = 2147483647
			index_socket_1.subtype = 'NONE'
			index_socket_1.attribute_domain = 'POINT'
			
			#Socket Boolean
			boolean_socket_5 = offset_boolean.interface.new_socket(name = "Boolean", in_out='INPUT', socket_type = 'NodeSocketBool')
			boolean_socket_5.default_value = False
			boolean_socket_5.attribute_domain = 'POINT'
			boolean_socket_5.hide_value = True
			
			#Socket Offset
			offset_socket_2 = offset_boolean.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket_2.default_value = 0
			offset_socket_2.min_value = -2147483647
			offset_socket_2.max_value = 2147483647
			offset_socket_2.subtype = 'NONE'
			offset_socket_2.attribute_domain = 'POINT'
			
			
			#initialize offset_boolean nodes
			#node Group Output
			group_output_11 = offset_boolean.nodes.new("NodeGroupOutput")
			group_output_11.name = "Group Output"
			group_output_11.is_active_output = True
			
			#node Group Input
			group_input_11 = offset_boolean.nodes.new("NodeGroupInput")
			group_input_11.name = "Group Input"
			
			#node Evaluate at Index
			evaluate_at_index_3 = offset_boolean.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_3.name = "Evaluate at Index"
			evaluate_at_index_3.data_type = 'BOOLEAN'
			evaluate_at_index_3.domain = 'POINT'
			
			#node Math
			math_6 = offset_boolean.nodes.new("ShaderNodeMath")
			math_6.name = "Math"
			math_6.operation = 'ADD'
			math_6.use_clamp = False
			
			
			
			
			#Set locations
			group_output_11.location = (190.0, 0.0)
			group_input_11.location = (-344.3331298828125, -46.23834991455078)
			evaluate_at_index_3.location = (0.0, 0.0)
			math_6.location = (-160.0, 0.0)
			
			#Set dimensions
			group_output_11.width, group_output_11.height = 140.0, 100.0
			group_input_11.width, group_input_11.height = 140.0, 100.0
			evaluate_at_index_3.width, evaluate_at_index_3.height = 140.0, 100.0
			math_6.width, math_6.height = 140.0, 100.0
			
			#initialize offset_boolean links
			#evaluate_at_index_3.Value -> group_output_11.Boolean
			offset_boolean.links.new(evaluate_at_index_3.outputs[0], group_output_11.inputs[0])
			#group_input_11.Boolean -> evaluate_at_index_3.Value
			offset_boolean.links.new(group_input_11.outputs[1], evaluate_at_index_3.inputs[1])
			#group_input_11.Index -> math_6.Value
			offset_boolean.links.new(group_input_11.outputs[0], math_6.inputs[1])
			#math_6.Value -> evaluate_at_index_3.Index
			offset_boolean.links.new(math_6.outputs[0], evaluate_at_index_3.inputs[0])
			#group_input_11.Offset -> math_6.Value
			offset_boolean.links.new(group_input_11.outputs[2], math_6.inputs[0])
			return offset_boolean

		offset_boolean = offset_boolean_node_group()

		#initialize vector_angle node group
		def vector_angle_node_group():
			vector_angle = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Vector Angle")

			vector_angle.color_tag = 'VECTOR'
			vector_angle.description = ""

			
			#vector_angle interface
			#Socket Angle
			angle_socket = vector_angle.interface.new_socket(name = "Angle", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			angle_socket.default_value = 0.0
			angle_socket.min_value = -3.4028234663852886e+38
			angle_socket.max_value = 3.4028234663852886e+38
			angle_socket.subtype = 'ANGLE'
			angle_socket.attribute_domain = 'POINT'
			angle_socket.description = "Angle between the two given vectors in radians"
			
			#Socket A
			a_socket = vector_angle.interface.new_socket(name = "A", in_out='INPUT', socket_type = 'NodeSocketVector')
			a_socket.default_value = (0.0, 0.0, 0.0)
			a_socket.min_value = -10000.0
			a_socket.max_value = 10000.0
			a_socket.subtype = 'NONE'
			a_socket.attribute_domain = 'POINT'
			
			#Socket B
			b_socket = vector_angle.interface.new_socket(name = "B", in_out='INPUT', socket_type = 'NodeSocketVector')
			b_socket.default_value = (0.0, 0.0, 0.0)
			b_socket.min_value = -10000.0
			b_socket.max_value = 10000.0
			b_socket.subtype = 'NONE'
			b_socket.attribute_domain = 'POINT'
			
			
			#initialize vector_angle nodes
			#node Group Input
			group_input_12 = vector_angle.nodes.new("NodeGroupInput")
			group_input_12.name = "Group Input"
			
			#node Vector Math.002
			vector_math_002_2 = vector_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_002_2.name = "Vector Math.002"
			vector_math_002_2.operation = 'NORMALIZE'
			
			#node Vector Math.001
			vector_math_001_1 = vector_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_001_1.name = "Vector Math.001"
			vector_math_001_1.operation = 'NORMALIZE'
			
			#node Vector Math
			vector_math_3 = vector_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_3.name = "Vector Math"
			vector_math_3.operation = 'DOT_PRODUCT'
			
			#node Math
			math_7 = vector_angle.nodes.new("ShaderNodeMath")
			math_7.name = "Math"
			math_7.operation = 'ARCCOSINE'
			math_7.use_clamp = False
			
			#node Group Output
			group_output_12 = vector_angle.nodes.new("NodeGroupOutput")
			group_output_12.name = "Group Output"
			group_output_12.is_active_output = True
			
			
			
			
			#Set locations
			group_input_12.location = (-360.0, 0.0)
			vector_math_002_2.location = (-160.0, -60.0)
			vector_math_001_1.location = (-160.0, 60.0)
			vector_math_3.location = (0.0, 60.0)
			math_7.location = (160.0, 60.0)
			group_output_12.location = (340.0, 60.0)
			
			#Set dimensions
			group_input_12.width, group_input_12.height = 140.0, 100.0
			vector_math_002_2.width, vector_math_002_2.height = 140.0, 100.0
			vector_math_001_1.width, vector_math_001_1.height = 140.0, 100.0
			vector_math_3.width, vector_math_3.height = 140.0, 100.0
			math_7.width, math_7.height = 140.0, 100.0
			group_output_12.width, group_output_12.height = 140.0, 100.0
			
			#initialize vector_angle links
			#vector_math_3.Value -> math_7.Value
			vector_angle.links.new(vector_math_3.outputs[1], math_7.inputs[0])
			#vector_math_002_2.Vector -> vector_math_3.Vector
			vector_angle.links.new(vector_math_002_2.outputs[0], vector_math_3.inputs[1])
			#vector_math_001_1.Vector -> vector_math_3.Vector
			vector_angle.links.new(vector_math_001_1.outputs[0], vector_math_3.inputs[0])
			#math_7.Value -> group_output_12.Angle
			vector_angle.links.new(math_7.outputs[0], group_output_12.inputs[0])
			#group_input_12.A -> vector_math_001_1.Vector
			vector_angle.links.new(group_input_12.outputs[0], vector_math_001_1.inputs[0])
			#group_input_12.B -> vector_math_002_2.Vector
			vector_angle.links.new(group_input_12.outputs[1], vector_math_002_2.inputs[0])
			return vector_angle

		vector_angle = vector_angle_node_group()

		#initialize dihedral_angle node group
		def dihedral_angle_node_group():
			dihedral_angle = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Dihedral Angle")

			dihedral_angle.color_tag = 'VECTOR'
			dihedral_angle.description = ""

			
			#dihedral_angle interface
			#Socket Angle
			angle_socket_1 = dihedral_angle.interface.new_socket(name = "Angle", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			angle_socket_1.default_value = 0.0
			angle_socket_1.min_value = -3.4028234663852886e+38
			angle_socket_1.max_value = 3.4028234663852886e+38
			angle_socket_1.subtype = 'ANGLE'
			angle_socket_1.attribute_domain = 'POINT'
			angle_socket_1.description = "The angle between the vectors AB and CD, when made perpendicular to BC."
			
			#Socket BA⟂(BC)
			ba__bc__socket = dihedral_angle.interface.new_socket(name = "BA⟂(BC)", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			ba__bc__socket.default_value = (0.0, 0.0, 0.0)
			ba__bc__socket.min_value = -3.4028234663852886e+38
			ba__bc__socket.max_value = 3.4028234663852886e+38
			ba__bc__socket.subtype = 'NONE'
			ba__bc__socket.attribute_domain = 'POINT'
			ba__bc__socket.description = "The vector BA when made perpendicular to  the axis BC"
			
			#Socket CD⟂(BC)
			cd__bc__socket = dihedral_angle.interface.new_socket(name = "CD⟂(BC)", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			cd__bc__socket.default_value = (0.0, 0.0, 0.0)
			cd__bc__socket.min_value = -3.4028234663852886e+38
			cd__bc__socket.max_value = 3.4028234663852886e+38
			cd__bc__socket.subtype = 'NONE'
			cd__bc__socket.attribute_domain = 'POINT'
			cd__bc__socket.description = "The Vector CD when makde perpendicular to the axis BC"
			
			#Socket BC
			bc_socket = dihedral_angle.interface.new_socket(name = "BC", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			bc_socket.default_value = (0.0, 0.0, 0.0)
			bc_socket.min_value = -3.4028234663852886e+38
			bc_socket.max_value = 3.4028234663852886e+38
			bc_socket.subtype = 'NONE'
			bc_socket.attribute_domain = 'POINT'
			bc_socket.description = "The axis vector BC"
			
			#Socket A
			a_socket_1 = dihedral_angle.interface.new_socket(name = "A", in_out='INPUT', socket_type = 'NodeSocketVector')
			a_socket_1.default_value = (0.0, 0.0, 0.0)
			a_socket_1.min_value = -3.4028234663852886e+38
			a_socket_1.max_value = 3.4028234663852886e+38
			a_socket_1.subtype = 'NONE'
			a_socket_1.attribute_domain = 'POINT'
			a_socket_1.description = "First vector for the calculation, which draws a line to B"
			
			#Socket B
			b_socket_1 = dihedral_angle.interface.new_socket(name = "B", in_out='INPUT', socket_type = 'NodeSocketVector')
			b_socket_1.default_value = (0.0, 0.0, 0.0)
			b_socket_1.min_value = -3.4028234663852886e+38
			b_socket_1.max_value = 3.4028234663852886e+38
			b_socket_1.subtype = 'NONE'
			b_socket_1.attribute_domain = 'POINT'
			b_socket_1.description = "Second vector for the calculation, which receives a line from A and draws a line to C"
			
			#Socket C
			c_socket_2 = dihedral_angle.interface.new_socket(name = "C", in_out='INPUT', socket_type = 'NodeSocketVector')
			c_socket_2.default_value = (0.0, 0.0, 0.0)
			c_socket_2.min_value = -3.4028234663852886e+38
			c_socket_2.max_value = 3.4028234663852886e+38
			c_socket_2.subtype = 'NONE'
			c_socket_2.attribute_domain = 'POINT'
			c_socket_2.description = "Third vector for the calculation, which receives a line from B and draws a line to D"
			
			#Socket D
			d_socket = dihedral_angle.interface.new_socket(name = "D", in_out='INPUT', socket_type = 'NodeSocketVector')
			d_socket.default_value = (0.0, 0.0, 0.0)
			d_socket.min_value = -3.4028234663852886e+38
			d_socket.max_value = 3.4028234663852886e+38
			d_socket.subtype = 'NONE'
			d_socket.attribute_domain = 'POINT'
			d_socket.description = "Last vector for the calculation, which is the end point of the line from D"
			
			
			#initialize dihedral_angle nodes
			#node Vector Math.003
			vector_math_003_1 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_003_1.name = "Vector Math.003"
			vector_math_003_1.operation = 'SUBTRACT'
			
			#node Vector Math.004
			vector_math_004_1 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_004_1.name = "Vector Math.004"
			vector_math_004_1.operation = 'SUBTRACT'
			
			#node Vector Math.006
			vector_math_006_1 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_006_1.name = "Vector Math.006"
			vector_math_006_1.operation = 'SUBTRACT'
			
			#node Vector Math.007
			vector_math_007_1 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_007_1.name = "Vector Math.007"
			vector_math_007_1.operation = 'PROJECT'
			
			#node Vector Math.009
			vector_math_009 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_009.name = "Vector Math.009"
			vector_math_009.operation = 'PROJECT'
			
			#node Vector Math.008
			vector_math_008 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_008.name = "Vector Math.008"
			vector_math_008.operation = 'SUBTRACT'
			
			#node Vector Math.010
			vector_math_010 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_010.name = "Vector Math.010"
			vector_math_010.operation = 'SUBTRACT'
			
			#node MN_utils_vector_angle.002
			mn_utils_vector_angle_002 = dihedral_angle.nodes.new("GeometryNodeGroup")
			mn_utils_vector_angle_002.label = "Vector Angle"
			mn_utils_vector_angle_002.name = "MN_utils_vector_angle.002"
			mn_utils_vector_angle_002.node_tree = vector_angle
			
			#node Group Output
			group_output_13 = dihedral_angle.nodes.new("NodeGroupOutput")
			group_output_13.name = "Group Output"
			group_output_13.is_active_output = True
			
			#node Reroute.002
			reroute_002_1 = dihedral_angle.nodes.new("NodeReroute")
			reroute_002_1.name = "Reroute.002"
			#node Reroute.001
			reroute_001_1 = dihedral_angle.nodes.new("NodeReroute")
			reroute_001_1.name = "Reroute.001"
			#node Vector Math
			vector_math_4 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_4.name = "Vector Math"
			vector_math_4.operation = 'CROSS_PRODUCT'
			
			#node Vector Math.001
			vector_math_001_2 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_001_2.name = "Vector Math.001"
			vector_math_001_2.operation = 'DOT_PRODUCT'
			
			#node Math.001
			math_001_2 = dihedral_angle.nodes.new("ShaderNodeMath")
			math_001_2.name = "Math.001"
			math_001_2.operation = 'SIGN'
			math_001_2.use_clamp = False
			
			#node Reroute
			reroute_3 = dihedral_angle.nodes.new("NodeReroute")
			reroute_3.name = "Reroute"
			#node Math
			math_8 = dihedral_angle.nodes.new("ShaderNodeMath")
			math_8.name = "Math"
			math_8.operation = 'MULTIPLY'
			math_8.use_clamp = False
			
			#node Group Input.003
			group_input_003 = dihedral_angle.nodes.new("NodeGroupInput")
			group_input_003.name = "Group Input.003"
			group_input_003.outputs[0].hide = True
			group_input_003.outputs[1].hide = True
			group_input_003.outputs[2].hide = True
			group_input_003.outputs[4].hide = True
			
			#node Group Input.001
			group_input_001_2 = dihedral_angle.nodes.new("NodeGroupInput")
			group_input_001_2.name = "Group Input.001"
			group_input_001_2.outputs[1].hide = True
			group_input_001_2.outputs[2].hide = True
			group_input_001_2.outputs[3].hide = True
			group_input_001_2.outputs[4].hide = True
			
			#node Group Input
			group_input_13 = dihedral_angle.nodes.new("NodeGroupInput")
			group_input_13.name = "Group Input"
			group_input_13.outputs[0].hide = True
			group_input_13.outputs[2].hide = True
			group_input_13.outputs[3].hide = True
			group_input_13.outputs[4].hide = True
			
			#node Group Input.002
			group_input_002 = dihedral_angle.nodes.new("NodeGroupInput")
			group_input_002.name = "Group Input.002"
			group_input_002.outputs[0].hide = True
			group_input_002.outputs[1].hide = True
			group_input_002.outputs[3].hide = True
			group_input_002.outputs[4].hide = True
			
			
			
			
			#Set locations
			vector_math_003_1.location = (-142.68453979492188, 25.911895751953125)
			vector_math_004_1.location = (-140.0, 440.0)
			vector_math_006_1.location = (-140.0, 180.0)
			vector_math_007_1.location = (80.0, 320.0)
			vector_math_009.location = (80.0, -80.0)
			vector_math_008.location = (80.0, 460.0)
			vector_math_010.location = (80.0, 60.0)
			mn_utils_vector_angle_002.location = (420.0, 420.0)
			group_output_13.location = (920.0, 320.0)
			reroute_002_1.location = (300.0, 260.0)
			reroute_001_1.location = (300.0, 240.0)
			vector_math_4.location = (420.0, 180.0)
			vector_math_001_2.location = (420.0, 40.0)
			math_001_2.location = (580.0, 40.0)
			reroute_3.location = (300.0, 220.0)
			math_8.location = (640.0, 420.0)
			group_input_003.location = (-440.0, 0.0)
			group_input_001_2.location = (-440.0, 420.0)
			group_input_13.location = (-440.0, 280.0)
			group_input_002.location = (-440.0, 140.0)
			
			#Set dimensions
			vector_math_003_1.width, vector_math_003_1.height = 140.0, 100.0
			vector_math_004_1.width, vector_math_004_1.height = 140.0, 100.0
			vector_math_006_1.width, vector_math_006_1.height = 140.0, 100.0
			vector_math_007_1.width, vector_math_007_1.height = 140.0, 100.0
			vector_math_009.width, vector_math_009.height = 140.0, 100.0
			vector_math_008.width, vector_math_008.height = 140.0, 100.0
			vector_math_010.width, vector_math_010.height = 140.0, 100.0
			mn_utils_vector_angle_002.width, mn_utils_vector_angle_002.height = 200.0, 100.0
			group_output_13.width, group_output_13.height = 140.0, 100.0
			reroute_002_1.width, reroute_002_1.height = 16.0, 100.0
			reroute_001_1.width, reroute_001_1.height = 16.0, 100.0
			vector_math_4.width, vector_math_4.height = 140.0, 100.0
			vector_math_001_2.width, vector_math_001_2.height = 140.0, 100.0
			math_001_2.width, math_001_2.height = 140.0, 100.0
			reroute_3.width, reroute_3.height = 16.0, 100.0
			math_8.width, math_8.height = 140.0, 100.0
			group_input_003.width, group_input_003.height = 140.0, 100.0
			group_input_001_2.width, group_input_001_2.height = 140.0, 100.0
			group_input_13.width, group_input_13.height = 140.0, 100.0
			group_input_002.width, group_input_002.height = 140.0, 100.0
			
			#initialize dihedral_angle links
			#vector_math_007_1.Vector -> vector_math_008.Vector
			dihedral_angle.links.new(vector_math_007_1.outputs[0], vector_math_008.inputs[1])
			#vector_math_009.Vector -> vector_math_010.Vector
			dihedral_angle.links.new(vector_math_009.outputs[0], vector_math_010.inputs[1])
			#vector_math_004_1.Vector -> vector_math_007_1.Vector
			dihedral_angle.links.new(vector_math_004_1.outputs[0], vector_math_007_1.inputs[0])
			#vector_math_006_1.Vector -> vector_math_007_1.Vector
			dihedral_angle.links.new(vector_math_006_1.outputs[0], vector_math_007_1.inputs[1])
			#reroute_002_1.Output -> mn_utils_vector_angle_002.A
			dihedral_angle.links.new(reroute_002_1.outputs[0], mn_utils_vector_angle_002.inputs[0])
			#vector_math_004_1.Vector -> vector_math_008.Vector
			dihedral_angle.links.new(vector_math_004_1.outputs[0], vector_math_008.inputs[0])
			#vector_math_003_1.Vector -> vector_math_010.Vector
			dihedral_angle.links.new(vector_math_003_1.outputs[0], vector_math_010.inputs[0])
			#vector_math_003_1.Vector -> vector_math_009.Vector
			dihedral_angle.links.new(vector_math_003_1.outputs[0], vector_math_009.inputs[0])
			#vector_math_006_1.Vector -> vector_math_009.Vector
			dihedral_angle.links.new(vector_math_006_1.outputs[0], vector_math_009.inputs[1])
			#vector_math_006_1.Vector -> reroute_3.Input
			dihedral_angle.links.new(vector_math_006_1.outputs[0], reroute_3.inputs[0])
			#reroute_001_1.Output -> mn_utils_vector_angle_002.B
			dihedral_angle.links.new(reroute_001_1.outputs[0], mn_utils_vector_angle_002.inputs[1])
			#vector_math_4.Vector -> vector_math_001_2.Vector
			dihedral_angle.links.new(vector_math_4.outputs[0], vector_math_001_2.inputs[0])
			#reroute_3.Output -> vector_math_001_2.Vector
			dihedral_angle.links.new(reroute_3.outputs[0], vector_math_001_2.inputs[1])
			#mn_utils_vector_angle_002.Angle -> math_8.Value
			dihedral_angle.links.new(mn_utils_vector_angle_002.outputs[0], math_8.inputs[0])
			#reroute_001_1.Output -> vector_math_4.Vector
			dihedral_angle.links.new(reroute_001_1.outputs[0], vector_math_4.inputs[1])
			#group_input_002.C -> vector_math_003_1.Vector
			dihedral_angle.links.new(group_input_002.outputs[2], vector_math_003_1.inputs[1])
			#group_input_13.B -> vector_math_004_1.Vector
			dihedral_angle.links.new(group_input_13.outputs[1], vector_math_004_1.inputs[1])
			#group_input_13.B -> vector_math_006_1.Vector
			dihedral_angle.links.new(group_input_13.outputs[1], vector_math_006_1.inputs[1])
			#group_input_002.C -> vector_math_006_1.Vector
			dihedral_angle.links.new(group_input_002.outputs[2], vector_math_006_1.inputs[0])
			#math_8.Value -> group_output_13.Angle
			dihedral_angle.links.new(math_8.outputs[0], group_output_13.inputs[0])
			#reroute_002_1.Output -> group_output_13.BA⟂(BC)
			dihedral_angle.links.new(reroute_002_1.outputs[0], group_output_13.inputs[1])
			#reroute_3.Output -> group_output_13.BC
			dihedral_angle.links.new(reroute_3.outputs[0], group_output_13.inputs[3])
			#reroute_001_1.Output -> group_output_13.CD⟂(BC)
			dihedral_angle.links.new(reroute_001_1.outputs[0], group_output_13.inputs[2])
			#reroute_002_1.Output -> vector_math_4.Vector
			dihedral_angle.links.new(reroute_002_1.outputs[0], vector_math_4.inputs[0])
			#vector_math_001_2.Value -> math_001_2.Value
			dihedral_angle.links.new(vector_math_001_2.outputs[1], math_001_2.inputs[0])
			#math_001_2.Value -> math_8.Value
			dihedral_angle.links.new(math_001_2.outputs[0], math_8.inputs[1])
			#vector_math_010.Vector -> reroute_001_1.Input
			dihedral_angle.links.new(vector_math_010.outputs[0], reroute_001_1.inputs[0])
			#vector_math_008.Vector -> reroute_002_1.Input
			dihedral_angle.links.new(vector_math_008.outputs[0], reroute_002_1.inputs[0])
			#group_input_001_2.A -> vector_math_004_1.Vector
			dihedral_angle.links.new(group_input_001_2.outputs[0], vector_math_004_1.inputs[0])
			#group_input_003.D -> vector_math_003_1.Vector
			dihedral_angle.links.new(group_input_003.outputs[3], vector_math_003_1.inputs[0])
			return dihedral_angle

		dihedral_angle = dihedral_angle_node_group()

		#initialize _mn_topo_phi_psi node group
		def _mn_topo_phi_psi_node_group():
			_mn_topo_phi_psi = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_topo_phi_psi")

			_mn_topo_phi_psi.color_tag = 'NONE'
			_mn_topo_phi_psi.description = ""

			
			#_mn_topo_phi_psi interface
			#Socket Angle
			angle_socket_2 = _mn_topo_phi_psi.interface.new_socket(name = "Angle", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			angle_socket_2.default_value = 0.0
			angle_socket_2.min_value = -3.4028234663852886e+38
			angle_socket_2.max_value = 3.4028234663852886e+38
			angle_socket_2.subtype = 'ANGLE'
			angle_socket_2.attribute_domain = 'POINT'
			
			#Socket BA⟂(BC)
			ba__bc__socket_1 = _mn_topo_phi_psi.interface.new_socket(name = "BA⟂(BC)", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			ba__bc__socket_1.default_value = (0.0, 0.0, 0.0)
			ba__bc__socket_1.min_value = -3.4028234663852886e+38
			ba__bc__socket_1.max_value = 3.4028234663852886e+38
			ba__bc__socket_1.subtype = 'NONE'
			ba__bc__socket_1.attribute_domain = 'POINT'
			
			#Socket CD⟂(BC)
			cd__bc__socket_1 = _mn_topo_phi_psi.interface.new_socket(name = "CD⟂(BC)", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			cd__bc__socket_1.default_value = (0.0, 0.0, 0.0)
			cd__bc__socket_1.min_value = -3.4028234663852886e+38
			cd__bc__socket_1.max_value = 3.4028234663852886e+38
			cd__bc__socket_1.subtype = 'NONE'
			cd__bc__socket_1.attribute_domain = 'POINT'
			
			#Socket BC
			bc_socket_1 = _mn_topo_phi_psi.interface.new_socket(name = "BC", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			bc_socket_1.default_value = (0.0, 0.0, 0.0)
			bc_socket_1.min_value = -3.4028234663852886e+38
			bc_socket_1.max_value = 3.4028234663852886e+38
			bc_socket_1.subtype = 'NONE'
			bc_socket_1.attribute_domain = 'POINT'
			
			#Socket A
			a_socket_2 = _mn_topo_phi_psi.interface.new_socket(name = "A", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			a_socket_2.default_value = (0.0, 0.0, 0.0)
			a_socket_2.min_value = -3.4028234663852886e+38
			a_socket_2.max_value = 3.4028234663852886e+38
			a_socket_2.subtype = 'NONE'
			a_socket_2.attribute_domain = 'POINT'
			
			#Socket B
			b_socket_2 = _mn_topo_phi_psi.interface.new_socket(name = "B", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			b_socket_2.default_value = (0.0, 0.0, 0.0)
			b_socket_2.min_value = -3.4028234663852886e+38
			b_socket_2.max_value = 3.4028234663852886e+38
			b_socket_2.subtype = 'NONE'
			b_socket_2.attribute_domain = 'POINT'
			
			#Socket C
			c_socket_3 = _mn_topo_phi_psi.interface.new_socket(name = "C", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			c_socket_3.default_value = (0.0, 0.0, 0.0)
			c_socket_3.min_value = -3.4028234663852886e+38
			c_socket_3.max_value = 3.4028234663852886e+38
			c_socket_3.subtype = 'NONE'
			c_socket_3.attribute_domain = 'POINT'
			
			#Socket D
			d_socket_1 = _mn_topo_phi_psi.interface.new_socket(name = "D", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			d_socket_1.default_value = (0.0, 0.0, 0.0)
			d_socket_1.min_value = -3.4028234663852886e+38
			d_socket_1.max_value = 3.4028234663852886e+38
			d_socket_1.subtype = 'NONE'
			d_socket_1.attribute_domain = 'POINT'
			
			#Socket Menu
			menu_socket = _mn_topo_phi_psi.interface.new_socket(name = "Menu", in_out='INPUT', socket_type = 'NodeSocketMenu')
			menu_socket.default_value = "Phi"
			menu_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_topo_phi_psi nodes
			#node Group Output
			group_output_14 = _mn_topo_phi_psi.nodes.new("NodeGroupOutput")
			group_output_14.name = "Group Output"
			group_output_14.is_active_output = True
			
			#node Group Input
			group_input_14 = _mn_topo_phi_psi.nodes.new("NodeGroupInput")
			group_input_14.name = "Group Input"
			
			#node Group.005
			group_005 = _mn_topo_phi_psi.nodes.new("GeometryNodeGroup")
			group_005.name = "Group.005"
			group_005.node_tree = mn_topo_backbone
			#Socket_3
			group_005.inputs[0].default_value = 1
			
			#node Group.007
			group_007 = _mn_topo_phi_psi.nodes.new("GeometryNodeGroup")
			group_007.name = "Group.007"
			group_007.node_tree = mn_topo_backbone
			#Socket_3
			group_007.inputs[0].default_value = -1
			
			#node Group.008
			group_008_2 = _mn_topo_phi_psi.nodes.new("GeometryNodeGroup")
			group_008_2.name = "Group.008"
			group_008_2.node_tree = mn_topo_backbone
			#Socket_3
			group_008_2.inputs[0].default_value = 0
			
			#node Group.009
			group_009_2 = _mn_topo_phi_psi.nodes.new("GeometryNodeGroup")
			group_009_2.name = "Group.009"
			group_009_2.node_tree = dihedral_angle
			
			#node Menu Switch
			menu_switch = _mn_topo_phi_psi.nodes.new("GeometryNodeMenuSwitch")
			menu_switch.name = "Menu Switch"
			menu_switch.active_index = 1
			menu_switch.data_type = 'INT'
			menu_switch.enum_items.clear()
			menu_switch.enum_items.new("Phi")
			menu_switch.enum_items[0].description = ""
			menu_switch.enum_items.new("Psi")
			menu_switch.enum_items[1].description = ""
			#Item_0
			menu_switch.inputs[1].default_value = 0
			#Item_1
			menu_switch.inputs[2].default_value = 1
			
			#node Index Switch
			index_switch = _mn_topo_phi_psi.nodes.new("GeometryNodeIndexSwitch")
			index_switch.name = "Index Switch"
			index_switch.data_type = 'VECTOR'
			index_switch.index_switch_items.clear()
			index_switch.index_switch_items.new()
			index_switch.index_switch_items.new()
			
			#node Index Switch.001
			index_switch_001 = _mn_topo_phi_psi.nodes.new("GeometryNodeIndexSwitch")
			index_switch_001.name = "Index Switch.001"
			index_switch_001.data_type = 'VECTOR'
			index_switch_001.index_switch_items.clear()
			index_switch_001.index_switch_items.new()
			index_switch_001.index_switch_items.new()
			
			#node Index Switch.002
			index_switch_002 = _mn_topo_phi_psi.nodes.new("GeometryNodeIndexSwitch")
			index_switch_002.name = "Index Switch.002"
			index_switch_002.data_type = 'VECTOR'
			index_switch_002.index_switch_items.clear()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			
			
			
			
			#Set locations
			group_output_14.location = (698.508544921875, 198.78929138183594)
			group_input_14.location = (-520.0, 280.0)
			group_005.location = (-380.0, -320.0)
			group_007.location = (-380.0, -120.0)
			group_008_2.location = (-380.0, 80.0)
			group_009_2.location = (272.33380126953125, 98.96731567382812)
			menu_switch.location = (-340.0, 260.0)
			index_switch.location = (-20.0, 140.0)
			index_switch_001.location = (-20.0, -100.0)
			index_switch_002.location = (-20.0, -280.0)
			
			#Set dimensions
			group_output_14.width, group_output_14.height = 140.0, 100.0
			group_input_14.width, group_input_14.height = 140.0, 100.0
			group_005.width, group_005.height = 171.90289306640625, 100.0
			group_007.width, group_007.height = 171.90289306640625, 100.0
			group_008_2.width, group_008_2.height = 171.90289306640625, 100.0
			group_009_2.width, group_009_2.height = 299.8184509277344, 100.0
			menu_switch.width, menu_switch.height = 140.0, 100.0
			index_switch.width, index_switch.height = 140.0, 100.0
			index_switch_001.width, index_switch_001.height = 140.0, 100.0
			index_switch_002.width, index_switch_002.height = 140.0, 100.0
			
			#initialize _mn_topo_phi_psi links
			#group_008_2.CA -> group_009_2.B
			_mn_topo_phi_psi.links.new(group_008_2.outputs[2], group_009_2.inputs[1])
			#index_switch_002.Output -> group_009_2.D
			_mn_topo_phi_psi.links.new(index_switch_002.outputs[0], group_009_2.inputs[3])
			#index_switch.Output -> group_009_2.A
			_mn_topo_phi_psi.links.new(index_switch.outputs[0], group_009_2.inputs[0])
			#index_switch_001.Output -> group_009_2.C
			_mn_topo_phi_psi.links.new(index_switch_001.outputs[0], group_009_2.inputs[2])
			#group_009_2.Angle -> group_output_14.Angle
			_mn_topo_phi_psi.links.new(group_009_2.outputs[0], group_output_14.inputs[0])
			#group_009_2.BA⟂(BC) -> group_output_14.BA⟂(BC)
			_mn_topo_phi_psi.links.new(group_009_2.outputs[1], group_output_14.inputs[1])
			#group_009_2.BC -> group_output_14.BC
			_mn_topo_phi_psi.links.new(group_009_2.outputs[3], group_output_14.inputs[3])
			#index_switch.Output -> group_output_14.A
			_mn_topo_phi_psi.links.new(index_switch.outputs[0], group_output_14.inputs[4])
			#group_008_2.CA -> group_output_14.B
			_mn_topo_phi_psi.links.new(group_008_2.outputs[2], group_output_14.inputs[5])
			#index_switch_001.Output -> group_output_14.C
			_mn_topo_phi_psi.links.new(index_switch_001.outputs[0], group_output_14.inputs[6])
			#index_switch_002.Output -> group_output_14.D
			_mn_topo_phi_psi.links.new(index_switch_002.outputs[0], group_output_14.inputs[7])
			#group_009_2.CD⟂(BC) -> group_output_14.CD⟂(BC)
			_mn_topo_phi_psi.links.new(group_009_2.outputs[2], group_output_14.inputs[2])
			#menu_switch.Output -> index_switch.Index
			_mn_topo_phi_psi.links.new(menu_switch.outputs[0], index_switch.inputs[0])
			#group_input_14.Menu -> menu_switch.Menu
			_mn_topo_phi_psi.links.new(group_input_14.outputs[0], menu_switch.inputs[0])
			#group_008_2.C -> index_switch.0
			_mn_topo_phi_psi.links.new(group_008_2.outputs[1], index_switch.inputs[1])
			#menu_switch.Output -> index_switch_001.Index
			_mn_topo_phi_psi.links.new(menu_switch.outputs[0], index_switch_001.inputs[0])
			#group_008_2.N -> index_switch_001.0
			_mn_topo_phi_psi.links.new(group_008_2.outputs[3], index_switch_001.inputs[1])
			#group_008_2.C -> index_switch_001.1
			_mn_topo_phi_psi.links.new(group_008_2.outputs[1], index_switch_001.inputs[2])
			#menu_switch.Output -> index_switch_002.Index
			_mn_topo_phi_psi.links.new(menu_switch.outputs[0], index_switch_002.inputs[0])
			#group_007.C -> index_switch_002.0
			_mn_topo_phi_psi.links.new(group_007.outputs[1], index_switch_002.inputs[1])
			#group_005.N -> index_switch_002.1
			_mn_topo_phi_psi.links.new(group_005.outputs[3], index_switch_002.inputs[2])
			#group_008_2.N -> index_switch.1
			_mn_topo_phi_psi.links.new(group_008_2.outputs[3], index_switch.inputs[2])
			return _mn_topo_phi_psi

		_mn_topo_phi_psi = _mn_topo_phi_psi_node_group()

		#initialize between_float node group
		def between_float_node_group():
			between_float = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Between Float")

			between_float.color_tag = 'CONVERTER'
			between_float.description = ""

			
			#between_float interface
			#Socket Boolean
			boolean_socket_6 = between_float.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket_6.default_value = False
			boolean_socket_6.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_4 = between_float.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket_4.default_value = 0.0
			value_socket_4.min_value = -3.4028234663852886e+38
			value_socket_4.max_value = 3.4028234663852886e+38
			value_socket_4.subtype = 'NONE'
			value_socket_4.attribute_domain = 'POINT'
			
			#Socket Lower
			lower_socket = between_float.interface.new_socket(name = "Lower", in_out='INPUT', socket_type = 'NodeSocketFloat')
			lower_socket.default_value = 0.0
			lower_socket.min_value = -3.4028234663852886e+38
			lower_socket.max_value = 3.4028234663852886e+38
			lower_socket.subtype = 'NONE'
			lower_socket.attribute_domain = 'POINT'
			
			#Socket Upper
			upper_socket = between_float.interface.new_socket(name = "Upper", in_out='INPUT', socket_type = 'NodeSocketFloat')
			upper_socket.default_value = 0.0
			upper_socket.min_value = -3.4028234663852886e+38
			upper_socket.max_value = 3.4028234663852886e+38
			upper_socket.subtype = 'NONE'
			upper_socket.attribute_domain = 'POINT'
			
			
			#initialize between_float nodes
			#node Group Output
			group_output_15 = between_float.nodes.new("NodeGroupOutput")
			group_output_15.name = "Group Output"
			group_output_15.is_active_output = True
			
			#node Group Input
			group_input_15 = between_float.nodes.new("NodeGroupInput")
			group_input_15.name = "Group Input"
			
			#node Compare
			compare_4 = between_float.nodes.new("FunctionNodeCompare")
			compare_4.name = "Compare"
			compare_4.data_type = 'FLOAT'
			compare_4.mode = 'ELEMENT'
			compare_4.operation = 'LESS_EQUAL'
			
			#node Compare.001
			compare_001_3 = between_float.nodes.new("FunctionNodeCompare")
			compare_001_3.name = "Compare.001"
			compare_001_3.data_type = 'FLOAT'
			compare_001_3.mode = 'ELEMENT'
			compare_001_3.operation = 'GREATER_EQUAL'
			
			#node Boolean Math
			boolean_math_2 = between_float.nodes.new("FunctionNodeBooleanMath")
			boolean_math_2.name = "Boolean Math"
			boolean_math_2.operation = 'AND'
			
			
			
			
			#Set locations
			group_output_15.location = (270.0, 0.0)
			group_input_15.location = (-280.0, 0.0)
			compare_4.location = (-80.0, -80.0)
			compare_001_3.location = (-80.0, 80.0)
			boolean_math_2.location = (80.0, 80.0)
			
			#Set dimensions
			group_output_15.width, group_output_15.height = 140.0, 100.0
			group_input_15.width, group_input_15.height = 140.0, 100.0
			compare_4.width, compare_4.height = 140.0, 100.0
			compare_001_3.width, compare_001_3.height = 140.0, 100.0
			boolean_math_2.width, boolean_math_2.height = 140.0, 100.0
			
			#initialize between_float links
			#compare_4.Result -> boolean_math_2.Boolean
			between_float.links.new(compare_4.outputs[0], boolean_math_2.inputs[1])
			#compare_001_3.Result -> boolean_math_2.Boolean
			between_float.links.new(compare_001_3.outputs[0], boolean_math_2.inputs[0])
			#group_input_15.Value -> compare_4.A
			between_float.links.new(group_input_15.outputs[0], compare_4.inputs[2])
			#group_input_15.Value -> compare_001_3.A
			between_float.links.new(group_input_15.outputs[0], compare_001_3.inputs[2])
			#boolean_math_2.Boolean -> group_output_15.Boolean
			between_float.links.new(boolean_math_2.outputs[0], group_output_15.inputs[0])
			#group_input_15.Lower -> compare_001_3.B
			between_float.links.new(group_input_15.outputs[1], compare_001_3.inputs[3])
			#group_input_15.Upper -> compare_4.B
			between_float.links.new(group_input_15.outputs[2], compare_4.inputs[3])
			#group_input_15.Value -> compare_001_3.A
			between_float.links.new(group_input_15.outputs[0], compare_001_3.inputs[0])
			#group_input_15.Value -> compare_4.A
			between_float.links.new(group_input_15.outputs[0], compare_4.inputs[0])
			#group_input_15.Lower -> compare_001_3.B
			between_float.links.new(group_input_15.outputs[1], compare_001_3.inputs[1])
			#group_input_15.Upper -> compare_4.B
			between_float.links.new(group_input_15.outputs[2], compare_4.inputs[1])
			return between_float

		between_float = between_float_node_group()

		#initialize helix_detect node group
		def helix_detect_node_group():
			helix_detect = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Helix Detect")

			helix_detect.color_tag = 'NONE'
			helix_detect.description = ""

			
			#helix_detect interface
			#Socket Boolean
			boolean_socket_7 = helix_detect.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket_7.default_value = False
			boolean_socket_7.attribute_domain = 'POINT'
			
			#Socket Helix Size
			helix_size_socket = helix_detect.interface.new_socket(name = "Helix Size", in_out='INPUT', socket_type = 'NodeSocketInt')
			helix_size_socket.default_value = 3
			helix_size_socket.min_value = -2147483648
			helix_size_socket.max_value = 2147483647
			helix_size_socket.subtype = 'NONE'
			helix_size_socket.attribute_domain = 'POINT'
			
			
			#initialize helix_detect nodes
			#node Group Output
			group_output_16 = helix_detect.nodes.new("NodeGroupOutput")
			group_output_16.name = "Group Output"
			group_output_16.is_active_output = True
			
			#node Group Input
			group_input_16 = helix_detect.nodes.new("NodeGroupInput")
			group_input_16.name = "Group Input"
			
			#node Group.003
			group_003_2 = helix_detect.nodes.new("GeometryNodeGroup")
			group_003_2.name = "Group.003"
			group_003_2.node_tree = hbond_backbone_check
			#Socket_3
			group_003_2.inputs[0].default_value = 0
			#Socket_5
			group_003_2.inputs[1].default_value = 0
			#Socket_0
			group_003_2.inputs[2].default_value = 0
			
			#node Group.017
			group_017 = helix_detect.nodes.new("GeometryNodeGroup")
			group_017.name = "Group.017"
			group_017.node_tree = boolean_run_fill
			
			#node Math
			math_9 = helix_detect.nodes.new("ShaderNodeMath")
			math_9.name = "Math"
			math_9.operation = 'MULTIPLY'
			math_9.use_clamp = False
			#Value_001
			math_9.inputs[1].default_value = -1.0
			
			#node Reroute
			reroute_4 = helix_detect.nodes.new("NodeReroute")
			reroute_4.name = "Reroute"
			#node Group
			group_4 = helix_detect.nodes.new("GeometryNodeGroup")
			group_4.name = "Group"
			group_4.node_tree = offset_boolean
			#Socket_1
			group_4.inputs[0].default_value = 0
			#Socket_3
			group_4.inputs[2].default_value = -1
			
			#node Boolean Math
			boolean_math_3 = helix_detect.nodes.new("FunctionNodeBooleanMath")
			boolean_math_3.name = "Boolean Math"
			boolean_math_3.operation = 'AND'
			
			#node Boolean Math.001
			boolean_math_001_1 = helix_detect.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_1.name = "Boolean Math.001"
			boolean_math_001_1.operation = 'OR'
			
			#node Group.001
			group_001_1 = helix_detect.nodes.new("GeometryNodeGroup")
			group_001_1.name = "Group.001"
			group_001_1.node_tree = offset_boolean
			#Socket_1
			group_001_1.inputs[0].default_value = 0
			
			#node Frame
			frame_1 = helix_detect.nodes.new("NodeFrame")
			frame_1.label = "Look to see if bonded with i - n residue, being end of helix"
			frame_1.name = "Frame"
			frame_1.label_size = 20
			frame_1.shrink = True
			
			#node Frame.001
			frame_001 = helix_detect.nodes.new("NodeFrame")
			frame_001.label = "i and i-1 are both Hbonded n residues ahead (i..i+n are helix)"
			frame_001.name = "Frame.001"
			frame_001.label_size = 20
			frame_001.shrink = True
			
			#node Frame.002
			frame_002 = helix_detect.nodes.new("NodeFrame")
			frame_002.label = "Assign to in-between residues"
			frame_002.name = "Frame.002"
			frame_002.label_size = 20
			frame_002.shrink = True
			
			#node Group.002
			group_002_1 = helix_detect.nodes.new("GeometryNodeGroup")
			group_002_1.name = "Group.002"
			group_002_1.node_tree = _mn_topo_phi_psi
			#Socket_11
			group_002_1.inputs[0].default_value = 'Phi'
			
			#node Boolean Math.003
			boolean_math_003_1 = helix_detect.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003_1.name = "Boolean Math.003"
			boolean_math_003_1.operation = 'AND'
			
			#node Group.004
			group_004 = helix_detect.nodes.new("GeometryNodeGroup")
			group_004.name = "Group.004"
			group_004.node_tree = _mn_topo_phi_psi
			#Socket_11
			group_004.inputs[0].default_value = 'Psi'
			
			#node Group.005
			group_005_1 = helix_detect.nodes.new("GeometryNodeGroup")
			group_005_1.name = "Group.005"
			group_005_1.node_tree = between_float
			#Socket_2
			group_005_1.inputs[1].default_value = -120.0
			#Socket_3
			group_005_1.inputs[2].default_value = 45.0
			
			#node Math.002
			math_002_3 = helix_detect.nodes.new("ShaderNodeMath")
			math_002_3.name = "Math.002"
			math_002_3.operation = 'DEGREES'
			math_002_3.use_clamp = False
			
			#node Group.006
			group_006 = helix_detect.nodes.new("GeometryNodeGroup")
			group_006.name = "Group.006"
			group_006.node_tree = between_float
			#Socket_2
			group_006.inputs[1].default_value = -180.0
			#Socket_3
			group_006.inputs[2].default_value = 10.0
			
			#node Math.003
			math_003_2 = helix_detect.nodes.new("ShaderNodeMath")
			math_003_2.name = "Math.003"
			math_003_2.operation = 'DEGREES'
			math_003_2.use_clamp = False
			
			#node Boolean Math.002
			boolean_math_002_1 = helix_detect.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_1.name = "Boolean Math.002"
			boolean_math_002_1.operation = 'AND'
			
			#node Frame.003
			frame_003 = helix_detect.nodes.new("NodeFrame")
			frame_003.label = "extra dihedral check, to discard turns in helix-turn-helix"
			frame_003.name = "Frame.003"
			frame_003.label_size = 20
			frame_003.shrink = True
			
			
			
			#Set parents
			group_003_2.parent = frame_001
			group_017.parent = frame_002
			group_4.parent = frame_001
			boolean_math_3.parent = frame_001
			group_001_1.parent = frame_1
			group_002_1.parent = frame_003
			group_004.parent = frame_003
			group_005_1.parent = frame_003
			math_002_3.parent = frame_003
			group_006.parent = frame_003
			math_003_2.parent = frame_003
			boolean_math_002_1.parent = frame_003
			
			#Set locations
			group_output_16.location = (680.0, 180.0)
			group_input_16.location = (-800.0, -260.0)
			group_003_2.location = (-500.0, 100.0)
			group_017.location = (320.0, -20.0)
			math_9.location = (-300.0, -180.0)
			reroute_4.location = (-540.0, -200.0)
			group_4.location = (-500.0, 240.0)
			boolean_math_3.location = (-340.0, 240.0)
			boolean_math_001_1.location = (-40.0, 240.0)
			group_001_1.location = (-40.0, 20.0)
			frame_1.location = (-10.0, -20.0)
			frame_001.location = (10.0, 40.0)
			frame_002.location = (-30.0, 200.0)
			group_002_1.location = (254.93621826171875, -98.54428100585938)
			boolean_math_003_1.location = (500.0, 180.0)
			group_004.location = (254.93621826171875, -378.5442810058594)
			group_005_1.location = (574.9362182617188, -98.54428100585938)
			math_002_3.location = (414.93621826171875, -98.54428100585938)
			group_006.location = (574.9362182617188, -378.5442810058594)
			math_003_2.location = (414.93621826171875, -378.5442810058594)
			boolean_math_002_1.location = (774.9362182617188, -98.54428100585938)
			frame_003.location = (35.0, 99.0)
			
			#Set dimensions
			group_output_16.width, group_output_16.height = 140.0, 100.0
			group_input_16.width, group_input_16.height = 140.0, 100.0
			group_003_2.width, group_003_2.height = 140.0, 100.0
			group_017.width, group_017.height = 144.84217834472656, 100.0
			math_9.width, math_9.height = 140.0, 100.0
			reroute_4.width, reroute_4.height = 16.0, 100.0
			group_4.width, group_4.height = 140.0, 100.0
			boolean_math_3.width, boolean_math_3.height = 140.0, 100.0
			boolean_math_001_1.width, boolean_math_001_1.height = 140.0, 100.0
			group_001_1.width, group_001_1.height = 140.0, 100.0
			frame_1.width, frame_1.height = 200.0, 187.0
			frame_001.width, frame_001.height = 360.0, 474.0
			frame_002.width, frame_002.height = 204.8421630859375, 165.0
			group_002_1.width, group_002_1.height = 140.0, 100.0
			boolean_math_003_1.width, boolean_math_003_1.height = 140.0, 100.0
			group_004.width, group_004.height = 140.0, 100.0
			group_005_1.width, group_005_1.height = 176.237548828125, 100.0
			math_002_3.width, math_002_3.height = 140.0, 100.0
			group_006.width, group_006.height = 176.237548828125, 100.0
			math_003_2.width, math_003_2.height = 140.0, 100.0
			boolean_math_002_1.width, boolean_math_002_1.height = 140.0, 100.0
			frame_003.width, frame_003.height = 720.0, 602.0
			
			#initialize helix_detect links
			#group_input_16.Helix Size -> math_9.Value
			helix_detect.links.new(group_input_16.outputs[0], math_9.inputs[0])
			#group_input_16.Helix Size -> reroute_4.Input
			helix_detect.links.new(group_input_16.outputs[0], reroute_4.inputs[0])
			#reroute_4.Output -> group_003_2.NH Offset
			helix_detect.links.new(reroute_4.outputs[0], group_003_2.inputs[3])
			#group_003_2.Is Bonded -> group_4.Boolean
			helix_detect.links.new(group_003_2.outputs[0], group_4.inputs[1])
			#group_4.Boolean -> boolean_math_3.Boolean
			helix_detect.links.new(group_4.outputs[0], boolean_math_3.inputs[0])
			#group_003_2.Is Bonded -> boolean_math_3.Boolean
			helix_detect.links.new(group_003_2.outputs[0], boolean_math_3.inputs[1])
			#boolean_math_001_1.Boolean -> group_017.Boolean
			helix_detect.links.new(boolean_math_001_1.outputs[0], group_017.inputs[0])
			#boolean_math_3.Boolean -> boolean_math_001_1.Boolean
			helix_detect.links.new(boolean_math_3.outputs[0], boolean_math_001_1.inputs[0])
			#boolean_math_3.Boolean -> group_001_1.Boolean
			helix_detect.links.new(boolean_math_3.outputs[0], group_001_1.inputs[1])
			#group_001_1.Boolean -> boolean_math_001_1.Boolean
			helix_detect.links.new(group_001_1.outputs[0], boolean_math_001_1.inputs[1])
			#math_9.Value -> group_001_1.Offset
			helix_detect.links.new(math_9.outputs[0], group_001_1.inputs[2])
			#reroute_4.Output -> group_017.Fill Size
			helix_detect.links.new(reroute_4.outputs[0], group_017.inputs[1])
			#group_017.Boolean -> boolean_math_003_1.Boolean
			helix_detect.links.new(group_017.outputs[0], boolean_math_003_1.inputs[0])
			#boolean_math_003_1.Boolean -> group_output_16.Boolean
			helix_detect.links.new(boolean_math_003_1.outputs[0], group_output_16.inputs[0])
			#boolean_math_002_1.Boolean -> boolean_math_003_1.Boolean
			helix_detect.links.new(boolean_math_002_1.outputs[0], boolean_math_003_1.inputs[1])
			#group_002_1.Angle -> math_002_3.Value
			helix_detect.links.new(group_002_1.outputs[0], math_002_3.inputs[0])
			#math_002_3.Value -> group_005_1.Value
			helix_detect.links.new(math_002_3.outputs[0], group_005_1.inputs[0])
			#math_003_2.Value -> group_006.Value
			helix_detect.links.new(math_003_2.outputs[0], group_006.inputs[0])
			#group_004.Angle -> math_003_2.Value
			helix_detect.links.new(group_004.outputs[0], math_003_2.inputs[0])
			#group_005_1.Boolean -> boolean_math_002_1.Boolean
			helix_detect.links.new(group_005_1.outputs[0], boolean_math_002_1.inputs[0])
			#group_006.Boolean -> boolean_math_002_1.Boolean
			helix_detect.links.new(group_006.outputs[0], boolean_math_002_1.inputs[1])
			return helix_detect

		helix_detect = helix_detect_node_group()

		#initialize offset_integer node group
		def offset_integer_node_group():
			offset_integer = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Offset Integer")

			offset_integer.color_tag = 'CONVERTER'
			offset_integer.description = ""

			
			#offset_integer interface
			#Socket Value
			value_socket_5 = offset_integer.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			value_socket_5.default_value = 0
			value_socket_5.min_value = -2147483648
			value_socket_5.max_value = 2147483647
			value_socket_5.subtype = 'NONE'
			value_socket_5.attribute_domain = 'POINT'
			
			#Socket Index
			index_socket_2 = offset_integer.interface.new_socket(name = "Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			index_socket_2.default_value = 0
			index_socket_2.min_value = 0
			index_socket_2.max_value = 2147483647
			index_socket_2.subtype = 'NONE'
			index_socket_2.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_6 = offset_integer.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketInt')
			value_socket_6.default_value = 0
			value_socket_6.min_value = -2147483648
			value_socket_6.max_value = 2147483647
			value_socket_6.subtype = 'NONE'
			value_socket_6.attribute_domain = 'POINT'
			value_socket_6.hide_value = True
			
			#Socket Offset
			offset_socket_3 = offset_integer.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket_3.default_value = 0
			offset_socket_3.min_value = -2147483648
			offset_socket_3.max_value = 2147483647
			offset_socket_3.subtype = 'NONE'
			offset_socket_3.attribute_domain = 'POINT'
			
			
			#initialize offset_integer nodes
			#node Group Output
			group_output_17 = offset_integer.nodes.new("NodeGroupOutput")
			group_output_17.name = "Group Output"
			group_output_17.is_active_output = True
			
			#node Group Input
			group_input_17 = offset_integer.nodes.new("NodeGroupInput")
			group_input_17.name = "Group Input"
			
			#node Evaluate at Index
			evaluate_at_index_4 = offset_integer.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_4.name = "Evaluate at Index"
			evaluate_at_index_4.data_type = 'INT'
			evaluate_at_index_4.domain = 'POINT'
			
			#node Math
			math_10 = offset_integer.nodes.new("ShaderNodeMath")
			math_10.name = "Math"
			math_10.operation = 'ADD'
			math_10.use_clamp = False
			
			
			
			
			#Set locations
			group_output_17.location = (190.0, 0.0)
			group_input_17.location = (-412.72760009765625, 0.2001800537109375)
			evaluate_at_index_4.location = (0.0, 0.0)
			math_10.location = (-217.90158081054688, 69.93922424316406)
			
			#Set dimensions
			group_output_17.width, group_output_17.height = 140.0, 100.0
			group_input_17.width, group_input_17.height = 140.0, 100.0
			evaluate_at_index_4.width, evaluate_at_index_4.height = 140.0, 100.0
			math_10.width, math_10.height = 140.0, 100.0
			
			#initialize offset_integer links
			#evaluate_at_index_4.Value -> group_output_17.Value
			offset_integer.links.new(evaluate_at_index_4.outputs[0], group_output_17.inputs[0])
			#group_input_17.Index -> math_10.Value
			offset_integer.links.new(group_input_17.outputs[0], math_10.inputs[0])
			#group_input_17.Offset -> math_10.Value
			offset_integer.links.new(group_input_17.outputs[2], math_10.inputs[1])
			#math_10.Value -> evaluate_at_index_4.Index
			offset_integer.links.new(math_10.outputs[0], evaluate_at_index_4.inputs[0])
			#group_input_17.Value -> evaluate_at_index_4.Value
			offset_integer.links.new(group_input_17.outputs[1], evaluate_at_index_4.inputs[1])
			return offset_integer

		offset_integer = offset_integer_node_group()

		#initialize _mn_topo_calc_helix node group
		def _mn_topo_calc_helix_node_group():
			_mn_topo_calc_helix = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_topo_calc_helix")

			_mn_topo_calc_helix.color_tag = 'NONE'
			_mn_topo_calc_helix.description = ""

			
			#_mn_topo_calc_helix interface
			#Socket Is Helix
			is_helix_socket = _mn_topo_calc_helix.interface.new_socket(name = "Is Helix", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_helix_socket.default_value = False
			is_helix_socket.attribute_domain = 'POINT'
			
			#Socket Bonded Index
			bonded_index_socket = _mn_topo_calc_helix.interface.new_socket(name = "Bonded Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			bonded_index_socket.default_value = 0
			bonded_index_socket.min_value = -2147483648
			bonded_index_socket.max_value = 2147483647
			bonded_index_socket.subtype = 'NONE'
			bonded_index_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_topo_calc_helix nodes
			#node Group Output
			group_output_18 = _mn_topo_calc_helix.nodes.new("NodeGroupOutput")
			group_output_18.name = "Group Output"
			group_output_18.is_active_output = True
			
			#node Group.001
			group_001_2 = _mn_topo_calc_helix.nodes.new("GeometryNodeGroup")
			group_001_2.name = "Group.001"
			group_001_2.node_tree = boolean_run_mask
			#Socket_2
			group_001_2.inputs[1].default_value = 0
			#Socket_3
			group_001_2.inputs[2].default_value = 5
			#Socket_6
			group_001_2.inputs[3].default_value = 0
			
			#node Boolean Math.004
			boolean_math_004_1 = _mn_topo_calc_helix.nodes.new("FunctionNodeBooleanMath")
			boolean_math_004_1.name = "Boolean Math.004"
			boolean_math_004_1.operation = 'OR'
			
			#node Boolean Math.005
			boolean_math_005 = _mn_topo_calc_helix.nodes.new("FunctionNodeBooleanMath")
			boolean_math_005.name = "Boolean Math.005"
			boolean_math_005.operation = 'OR'
			
			#node Group
			group_5 = _mn_topo_calc_helix.nodes.new("GeometryNodeGroup")
			group_5.name = "Group"
			group_5.node_tree = helix_detect
			#Socket_1
			group_5.inputs[0].default_value = 3
			
			#node Group.002
			group_002_2 = _mn_topo_calc_helix.nodes.new("GeometryNodeGroup")
			group_002_2.name = "Group.002"
			group_002_2.node_tree = helix_detect
			#Socket_1
			group_002_2.inputs[0].default_value = 4
			
			#node Group.003
			group_003_3 = _mn_topo_calc_helix.nodes.new("GeometryNodeGroup")
			group_003_3.name = "Group.003"
			group_003_3.node_tree = helix_detect
			#Socket_1
			group_003_3.inputs[0].default_value = 5
			
			#node Group.004
			group_004_1 = _mn_topo_calc_helix.nodes.new("GeometryNodeGroup")
			group_004_1.name = "Group.004"
			group_004_1.node_tree = offset_integer
			#Socket_1
			group_004_1.inputs[0].default_value = 0
			#Socket_2
			group_004_1.inputs[2].default_value = 3
			
			#node Index
			index_1 = _mn_topo_calc_helix.nodes.new("GeometryNodeInputIndex")
			index_1.name = "Index"
			
			#node Switch
			switch_2 = _mn_topo_calc_helix.nodes.new("GeometryNodeSwitch")
			switch_2.name = "Switch"
			switch_2.input_type = 'INT'
			#False
			switch_2.inputs[1].default_value = -1
			
			#node Switch.001
			switch_001 = _mn_topo_calc_helix.nodes.new("GeometryNodeSwitch")
			switch_001.name = "Switch.001"
			switch_001.input_type = 'INT'
			
			#node Group.005
			group_005_2 = _mn_topo_calc_helix.nodes.new("GeometryNodeGroup")
			group_005_2.name = "Group.005"
			group_005_2.node_tree = offset_integer
			#Socket_1
			group_005_2.inputs[0].default_value = 0
			#Socket_2
			group_005_2.inputs[2].default_value = 4
			
			#node Switch.002
			switch_002 = _mn_topo_calc_helix.nodes.new("GeometryNodeSwitch")
			switch_002.name = "Switch.002"
			switch_002.input_type = 'INT'
			
			#node Group.006
			group_006_1 = _mn_topo_calc_helix.nodes.new("GeometryNodeGroup")
			group_006_1.name = "Group.006"
			group_006_1.node_tree = offset_integer
			#Socket_1
			group_006_1.inputs[0].default_value = 0
			#Socket_2
			group_006_1.inputs[2].default_value = 5
			
			#node Frame
			frame_2 = _mn_topo_calc_helix.nodes.new("NodeFrame")
			frame_2.label = "If part of a helix, return the Index of the CA that is bonded"
			frame_2.name = "Frame"
			frame_2.label_size = 20
			frame_2.shrink = True
			
			
			
			#Set parents
			group_004_1.parent = frame_2
			index_1.parent = frame_2
			switch_2.parent = frame_2
			switch_001.parent = frame_2
			group_005_2.parent = frame_2
			switch_002.parent = frame_2
			group_006_1.parent = frame_2
			
			#Set locations
			group_output_18.location = (900.0, 620.0)
			group_001_2.location = (660.0, 620.0)
			boolean_math_004_1.location = (320.0, 620.0)
			boolean_math_005.location = (500.0, 620.0)
			group_5.location = (137.64556884765625, 620.0)
			group_002_2.location = (140.0, 500.0)
			group_003_3.location = (320.0, 480.0)
			group_004_1.location = (320.0, 840.0)
			index_1.location = (140.0, 820.0)
			switch_2.location = (320.0, 1000.0)
			switch_001.location = (480.0, 1000.0)
			group_005_2.location = (480.0, 840.0)
			switch_002.location = (640.0, 1000.0)
			group_006_1.location = (640.0, 840.0)
			frame_2.location = (0.0, 0.0)
			
			#Set dimensions
			group_output_18.width, group_output_18.height = 140.0, 100.0
			group_001_2.width, group_001_2.height = 208.096435546875, 100.0
			boolean_math_004_1.width, boolean_math_004_1.height = 140.0, 100.0
			boolean_math_005.width, boolean_math_005.height = 140.0, 100.0
			group_5.width, group_5.height = 142.35443115234375, 100.0
			group_002_2.width, group_002_2.height = 140.0, 100.0
			group_003_3.width, group_003_3.height = 140.0, 100.0
			group_004_1.width, group_004_1.height = 140.0, 100.0
			index_1.width, index_1.height = 140.0, 100.0
			switch_2.width, switch_2.height = 140.0, 100.0
			switch_001.width, switch_001.height = 140.0, 100.0
			group_005_2.width, group_005_2.height = 140.0, 100.0
			switch_002.width, switch_002.height = 140.0, 100.0
			group_006_1.width, group_006_1.height = 140.0, 100.0
			frame_2.width, frame_2.height = 700.0, 372.0
			
			#initialize _mn_topo_calc_helix links
			#boolean_math_004_1.Boolean -> boolean_math_005.Boolean
			_mn_topo_calc_helix.links.new(boolean_math_004_1.outputs[0], boolean_math_005.inputs[0])
			#group_001_2.Boolean -> group_output_18.Is Helix
			_mn_topo_calc_helix.links.new(group_001_2.outputs[0], group_output_18.inputs[0])
			#group_5.Boolean -> boolean_math_004_1.Boolean
			_mn_topo_calc_helix.links.new(group_5.outputs[0], boolean_math_004_1.inputs[0])
			#group_002_2.Boolean -> boolean_math_004_1.Boolean
			_mn_topo_calc_helix.links.new(group_002_2.outputs[0], boolean_math_004_1.inputs[1])
			#group_003_3.Boolean -> boolean_math_005.Boolean
			_mn_topo_calc_helix.links.new(group_003_3.outputs[0], boolean_math_005.inputs[1])
			#boolean_math_005.Boolean -> group_001_2.Boolean
			_mn_topo_calc_helix.links.new(boolean_math_005.outputs[0], group_001_2.inputs[0])
			#index_1.Index -> group_004_1.Value
			_mn_topo_calc_helix.links.new(index_1.outputs[0], group_004_1.inputs[1])
			#group_004_1.Value -> switch_2.True
			_mn_topo_calc_helix.links.new(group_004_1.outputs[0], switch_2.inputs[2])
			#group_5.Boolean -> switch_2.Switch
			_mn_topo_calc_helix.links.new(group_5.outputs[0], switch_2.inputs[0])
			#switch_2.Output -> switch_001.False
			_mn_topo_calc_helix.links.new(switch_2.outputs[0], switch_001.inputs[1])
			#group_002_2.Boolean -> switch_001.Switch
			_mn_topo_calc_helix.links.new(group_002_2.outputs[0], switch_001.inputs[0])
			#group_005_2.Value -> switch_001.True
			_mn_topo_calc_helix.links.new(group_005_2.outputs[0], switch_001.inputs[2])
			#switch_001.Output -> switch_002.False
			_mn_topo_calc_helix.links.new(switch_001.outputs[0], switch_002.inputs[1])
			#group_003_3.Boolean -> switch_002.Switch
			_mn_topo_calc_helix.links.new(group_003_3.outputs[0], switch_002.inputs[0])
			#index_1.Index -> group_005_2.Value
			_mn_topo_calc_helix.links.new(index_1.outputs[0], group_005_2.inputs[1])
			#index_1.Index -> group_006_1.Value
			_mn_topo_calc_helix.links.new(index_1.outputs[0], group_006_1.inputs[1])
			#group_006_1.Value -> switch_002.True
			_mn_topo_calc_helix.links.new(group_006_1.outputs[0], switch_002.inputs[2])
			#switch_002.Output -> group_output_18.Bonded Index
			_mn_topo_calc_helix.links.new(switch_002.outputs[0], group_output_18.inputs[1])
			return _mn_topo_calc_helix

		_mn_topo_calc_helix = _mn_topo_calc_helix_node_group()

		#initialize self_sample_proximity node group
		def self_sample_proximity_node_group():
			self_sample_proximity = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Self Sample Proximity")

			self_sample_proximity.color_tag = 'NONE'
			self_sample_proximity.description = ""

			
			#self_sample_proximity interface
			#Socket Closest Index
			closest_index_socket = self_sample_proximity.interface.new_socket(name = "Closest Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			closest_index_socket.default_value = 0
			closest_index_socket.min_value = -2147483648
			closest_index_socket.max_value = 2147483647
			closest_index_socket.subtype = 'NONE'
			closest_index_socket.attribute_domain = 'POINT'
			
			#Socket Input
			input_socket = self_sample_proximity.interface.new_socket(name = "Input", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			input_socket.attribute_domain = 'POINT'
			
			#Socket Target Position
			target_position_socket = self_sample_proximity.interface.new_socket(name = "Target Position", in_out='INPUT', socket_type = 'NodeSocketVector')
			target_position_socket.default_value = (0.0, 0.0, 0.0)
			target_position_socket.min_value = -3.4028234663852886e+38
			target_position_socket.max_value = 3.4028234663852886e+38
			target_position_socket.subtype = 'NONE'
			target_position_socket.attribute_domain = 'POINT'
			
			#Socket Self Position
			self_position_socket = self_sample_proximity.interface.new_socket(name = "Self Position", in_out='INPUT', socket_type = 'NodeSocketVector')
			self_position_socket.default_value = (0.0, 0.0, 0.0)
			self_position_socket.min_value = -3.4028234663852886e+38
			self_position_socket.max_value = 3.4028234663852886e+38
			self_position_socket.subtype = 'NONE'
			self_position_socket.attribute_domain = 'POINT'
			
			
			#initialize self_sample_proximity nodes
			#node Group Output
			group_output_19 = self_sample_proximity.nodes.new("NodeGroupOutput")
			group_output_19.name = "Group Output"
			group_output_19.is_active_output = True
			
			#node Group Input
			group_input_18 = self_sample_proximity.nodes.new("NodeGroupInput")
			group_input_18.name = "Group Input"
			
			#node Set Position.002
			set_position_002 = self_sample_proximity.nodes.new("GeometryNodeSetPosition")
			set_position_002.name = "Set Position.002"
			#Selection
			set_position_002.inputs[1].default_value = True
			#Offset
			set_position_002.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Sample Nearest.001
			sample_nearest_001 = self_sample_proximity.nodes.new("GeometryNodeSampleNearest")
			sample_nearest_001.name = "Sample Nearest.001"
			sample_nearest_001.domain = 'POINT'
			
			
			
			
			#Set locations
			group_output_19.location = (4.068901062011719, 95.01506042480469)
			group_input_18.location = (-640.0, 20.0)
			set_position_002.location = (-380.0, -20.0)
			sample_nearest_001.location = (-220.0, -20.0)
			
			#Set dimensions
			group_output_19.width, group_output_19.height = 140.0, 100.0
			group_input_18.width, group_input_18.height = 140.0, 100.0
			set_position_002.width, set_position_002.height = 140.0, 100.0
			sample_nearest_001.width, sample_nearest_001.height = 140.0, 100.0
			
			#initialize self_sample_proximity links
			#group_input_18.Input -> set_position_002.Geometry
			self_sample_proximity.links.new(group_input_18.outputs[0], set_position_002.inputs[0])
			#set_position_002.Geometry -> sample_nearest_001.Geometry
			self_sample_proximity.links.new(set_position_002.outputs[0], sample_nearest_001.inputs[0])
			#group_input_18.Target Position -> set_position_002.Position
			self_sample_proximity.links.new(group_input_18.outputs[1], set_position_002.inputs[2])
			#group_input_18.Self Position -> sample_nearest_001.Sample Position
			self_sample_proximity.links.new(group_input_18.outputs[2], sample_nearest_001.inputs[1])
			#sample_nearest_001.Index -> group_output_19.Closest Index
			self_sample_proximity.links.new(sample_nearest_001.outputs[0], group_output_19.inputs[0])
			return self_sample_proximity

		self_sample_proximity = self_sample_proximity_node_group()

		#initialize hbond_backbone_check_backup node group
		def hbond_backbone_check_backup_node_group():
			hbond_backbone_check_backup = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "HBond Backbone Check_backup")

			hbond_backbone_check_backup.color_tag = 'NONE'
			hbond_backbone_check_backup.description = ""

			
			#hbond_backbone_check_backup interface
			#Socket Is Bonded
			is_bonded_socket_2 = hbond_backbone_check_backup.interface.new_socket(name = "Is Bonded", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_bonded_socket_2.default_value = False
			is_bonded_socket_2.attribute_domain = 'POINT'
			
			#Socket Bond Energy
			bond_energy_socket_2 = hbond_backbone_check_backup.interface.new_socket(name = "Bond Energy", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			bond_energy_socket_2.default_value = 0.0
			bond_energy_socket_2.min_value = -3.4028234663852886e+38
			bond_energy_socket_2.max_value = 3.4028234663852886e+38
			bond_energy_socket_2.subtype = 'NONE'
			bond_energy_socket_2.attribute_domain = 'POINT'
			
			#Socket H->O
			h__o_socket_1 = hbond_backbone_check_backup.interface.new_socket(name = "H->O", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			h__o_socket_1.default_value = (0.0, 0.0, 0.0)
			h__o_socket_1.min_value = -3.4028234663852886e+38
			h__o_socket_1.max_value = 3.4028234663852886e+38
			h__o_socket_1.subtype = 'NONE'
			h__o_socket_1.attribute_domain = 'POINT'
			
			#Panel CO
			co_panel_1 = hbond_backbone_check_backup.interface.new_panel("CO")
			#Socket CO Index
			co_index_socket_1 = hbond_backbone_check_backup.interface.new_socket(name = "CO Index", in_out='INPUT', socket_type = 'NodeSocketInt', parent = co_panel_1)
			co_index_socket_1.default_value = 0
			co_index_socket_1.min_value = 0
			co_index_socket_1.max_value = 2147483647
			co_index_socket_1.subtype = 'NONE'
			co_index_socket_1.attribute_domain = 'POINT'
			
			#Socket CO Offset
			co_offset_socket_1 = hbond_backbone_check_backup.interface.new_socket(name = "CO Offset", in_out='INPUT', socket_type = 'NodeSocketInt', parent = co_panel_1)
			co_offset_socket_1.default_value = 0
			co_offset_socket_1.min_value = -2147483648
			co_offset_socket_1.max_value = 2147483647
			co_offset_socket_1.subtype = 'NONE'
			co_offset_socket_1.attribute_domain = 'POINT'
			
			
			#Panel NH
			nh_panel_1 = hbond_backbone_check_backup.interface.new_panel("NH")
			#Socket NH Index
			nh_index_socket_1 = hbond_backbone_check_backup.interface.new_socket(name = "NH Index", in_out='INPUT', socket_type = 'NodeSocketInt', parent = nh_panel_1)
			nh_index_socket_1.default_value = 0
			nh_index_socket_1.min_value = 0
			nh_index_socket_1.max_value = 2147483647
			nh_index_socket_1.subtype = 'NONE'
			nh_index_socket_1.attribute_domain = 'POINT'
			
			#Socket NH Offset
			nh_offset_socket_1 = hbond_backbone_check_backup.interface.new_socket(name = "NH Offset", in_out='INPUT', socket_type = 'NodeSocketInt', parent = nh_panel_1)
			nh_offset_socket_1.default_value = 0
			nh_offset_socket_1.min_value = -2147483648
			nh_offset_socket_1.max_value = 2147483647
			nh_offset_socket_1.subtype = 'NONE'
			nh_offset_socket_1.attribute_domain = 'POINT'
			
			
			
			#initialize hbond_backbone_check_backup nodes
			#node Group Output
			group_output_20 = hbond_backbone_check_backup.nodes.new("NodeGroupOutput")
			group_output_20.name = "Group Output"
			group_output_20.is_active_output = True
			
			#node Group Input
			group_input_19 = hbond_backbone_check_backup.nodes.new("NodeGroupInput")
			group_input_19.name = "Group Input"
			
			#node Group.008
			group_008_3 = hbond_backbone_check_backup.nodes.new("GeometryNodeGroup")
			group_008_3.name = "Group.008"
			group_008_3.node_tree = hbond_energy
			
			#node Group.009
			group_009_3 = hbond_backbone_check_backup.nodes.new("GeometryNodeGroup")
			group_009_3.name = "Group.009"
			group_009_3.node_tree = mn_topo_backbone
			#Socket_3
			group_009_3.inputs[0].default_value = 0
			
			#node Evaluate at Index
			evaluate_at_index_5 = hbond_backbone_check_backup.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_5.name = "Evaluate at Index"
			evaluate_at_index_5.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_5.domain = 'POINT'
			
			#node Evaluate at Index.001
			evaluate_at_index_001_2 = hbond_backbone_check_backup.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001_2.name = "Evaluate at Index.001"
			evaluate_at_index_001_2.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_001_2.domain = 'POINT'
			
			#node Evaluate at Index.002
			evaluate_at_index_002_2 = hbond_backbone_check_backup.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_002_2.name = "Evaluate at Index.002"
			evaluate_at_index_002_2.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_002_2.domain = 'POINT'
			
			#node Evaluate at Index.003
			evaluate_at_index_003_2 = hbond_backbone_check_backup.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_003_2.name = "Evaluate at Index.003"
			evaluate_at_index_003_2.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_003_2.domain = 'POINT'
			
			#node Math
			math_11 = hbond_backbone_check_backup.nodes.new("ShaderNodeMath")
			math_11.name = "Math"
			math_11.operation = 'ADD'
			math_11.use_clamp = False
			
			#node Math.001
			math_001_3 = hbond_backbone_check_backup.nodes.new("ShaderNodeMath")
			math_001_3.name = "Math.001"
			math_001_3.operation = 'ADD'
			math_001_3.use_clamp = False
			
			#node Math.002
			math_002_4 = hbond_backbone_check_backup.nodes.new("ShaderNodeMath")
			math_002_4.name = "Math.002"
			math_002_4.operation = 'SUBTRACT'
			math_002_4.use_clamp = False
			
			#node Math.003
			math_003_3 = hbond_backbone_check_backup.nodes.new("ShaderNodeMath")
			math_003_3.name = "Math.003"
			math_003_3.operation = 'ABSOLUTE'
			math_003_3.use_clamp = False
			
			#node Compare
			compare_5 = hbond_backbone_check_backup.nodes.new("FunctionNodeCompare")
			compare_5.name = "Compare"
			compare_5.data_type = 'FLOAT'
			compare_5.mode = 'ELEMENT'
			compare_5.operation = 'GREATER_THAN'
			
			#node Integer
			integer_1 = hbond_backbone_check_backup.nodes.new("FunctionNodeInputInt")
			integer_1.name = "Integer"
			integer_1.integer = 1
			
			#node Frame
			frame_3 = hbond_backbone_check_backup.nodes.new("NodeFrame")
			frame_3.label = "Check not bonded to +/- residues"
			frame_3.name = "Frame"
			frame_3.label_size = 20
			frame_3.shrink = True
			
			#node Switch
			switch_3 = hbond_backbone_check_backup.nodes.new("GeometryNodeSwitch")
			switch_3.name = "Switch"
			switch_3.input_type = 'BOOLEAN'
			#False
			switch_3.inputs[1].default_value = False
			
			#node Compare.001
			compare_001_4 = hbond_backbone_check_backup.nodes.new("FunctionNodeCompare")
			compare_001_4.name = "Compare.001"
			compare_001_4.data_type = 'FLOAT'
			compare_001_4.mode = 'ELEMENT'
			compare_001_4.operation = 'LESS_THAN'
			
			#node Vector Math
			vector_math_5 = hbond_backbone_check_backup.nodes.new("ShaderNodeVectorMath")
			vector_math_5.name = "Vector Math"
			vector_math_5.operation = 'LENGTH'
			
			#node Group
			group_6 = hbond_backbone_check_backup.nodes.new("GeometryNodeGroup")
			group_6.name = "Group"
			group_6.node_tree = mn_units
			#Input_1
			group_6.inputs[0].default_value = 3.0
			
			
			
			#Set parents
			math_002_4.parent = frame_3
			math_003_3.parent = frame_3
			compare_5.parent = frame_3
			integer_1.parent = frame_3
			
			#Set locations
			group_output_20.location = (820.0, 240.0)
			group_input_19.location = (-680.0, 140.0)
			group_008_3.location = (224.2731170654297, 240.0)
			group_009_3.location = (-480.0, 460.0)
			evaluate_at_index_5.location = (-20.0, 40.0)
			evaluate_at_index_001_2.location = (-20.0, -120.0)
			evaluate_at_index_002_2.location = (-20.0, 400.0)
			evaluate_at_index_003_2.location = (-20.0, 240.0)
			math_11.location = (-480.0, 240.0)
			math_001_3.location = (-480.0, 80.0)
			math_002_4.location = (70.0, 640.0)
			math_003_3.location = (240.0, 640.0)
			compare_5.location = (420.0, 640.0)
			integer_1.location = (240.0, 500.0)
			frame_3.location = (-70.0, 40.0)
			switch_3.location = (620.0, 340.0)
			compare_001_4.location = (520.0, 140.0)
			vector_math_5.location = (260.0, 20.0)
			group_6.location = (520.0, -20.0)
			
			#Set dimensions
			group_output_20.width, group_output_20.height = 140.0, 100.0
			group_input_19.width, group_input_19.height = 140.0, 100.0
			group_008_3.width, group_008_3.height = 184.92144775390625, 100.0
			group_009_3.width, group_009_3.height = 140.0, 100.0
			evaluate_at_index_5.width, evaluate_at_index_5.height = 140.0, 100.0
			evaluate_at_index_001_2.width, evaluate_at_index_001_2.height = 140.0, 100.0
			evaluate_at_index_002_2.width, evaluate_at_index_002_2.height = 140.0, 100.0
			evaluate_at_index_003_2.width, evaluate_at_index_003_2.height = 140.0, 100.0
			math_11.width, math_11.height = 140.0, 100.0
			math_001_3.width, math_001_3.height = 140.0, 100.0
			math_002_4.width, math_002_4.height = 140.0, 100.0
			math_003_3.width, math_003_3.height = 140.0, 100.0
			compare_5.width, compare_5.height = 140.0, 100.0
			integer_1.width, integer_1.height = 140.0, 100.0
			frame_3.width, frame_3.height = 550.0, 285.0
			switch_3.width, switch_3.height = 140.0, 100.0
			compare_001_4.width, compare_001_4.height = 140.0, 100.0
			vector_math_5.width, vector_math_5.height = 140.0, 100.0
			group_6.width, group_6.height = 140.0, 100.0
			
			#initialize hbond_backbone_check_backup links
			#evaluate_at_index_001_2.Value -> group_008_3.H
			hbond_backbone_check_backup.links.new(evaluate_at_index_001_2.outputs[0], group_008_3.inputs[3])
			#evaluate_at_index_5.Value -> group_008_3.N
			hbond_backbone_check_backup.links.new(evaluate_at_index_5.outputs[0], group_008_3.inputs[2])
			#evaluate_at_index_002_2.Value -> group_008_3.O
			hbond_backbone_check_backup.links.new(evaluate_at_index_002_2.outputs[0], group_008_3.inputs[0])
			#math_001_3.Value -> evaluate_at_index_001_2.Index
			hbond_backbone_check_backup.links.new(math_001_3.outputs[0], evaluate_at_index_001_2.inputs[0])
			#math_001_3.Value -> evaluate_at_index_5.Index
			hbond_backbone_check_backup.links.new(math_001_3.outputs[0], evaluate_at_index_5.inputs[0])
			#evaluate_at_index_003_2.Value -> group_008_3.C
			hbond_backbone_check_backup.links.new(evaluate_at_index_003_2.outputs[0], group_008_3.inputs[1])
			#group_009_3.NH -> evaluate_at_index_001_2.Value
			hbond_backbone_check_backup.links.new(group_009_3.outputs[4], evaluate_at_index_001_2.inputs[1])
			#group_009_3.N -> evaluate_at_index_5.Value
			hbond_backbone_check_backup.links.new(group_009_3.outputs[3], evaluate_at_index_5.inputs[1])
			#group_008_3.Bond Energy -> group_output_20.Bond Energy
			hbond_backbone_check_backup.links.new(group_008_3.outputs[1], group_output_20.inputs[1])
			#group_008_3.Bond Vector -> group_output_20.H->O
			hbond_backbone_check_backup.links.new(group_008_3.outputs[2], group_output_20.inputs[2])
			#group_009_3.O -> evaluate_at_index_002_2.Value
			hbond_backbone_check_backup.links.new(group_009_3.outputs[0], evaluate_at_index_002_2.inputs[1])
			#group_009_3.C -> evaluate_at_index_003_2.Value
			hbond_backbone_check_backup.links.new(group_009_3.outputs[1], evaluate_at_index_003_2.inputs[1])
			#math_11.Value -> evaluate_at_index_002_2.Index
			hbond_backbone_check_backup.links.new(math_11.outputs[0], evaluate_at_index_002_2.inputs[0])
			#math_11.Value -> evaluate_at_index_003_2.Index
			hbond_backbone_check_backup.links.new(math_11.outputs[0], evaluate_at_index_003_2.inputs[0])
			#group_input_19.CO Index -> math_11.Value
			hbond_backbone_check_backup.links.new(group_input_19.outputs[0], math_11.inputs[0])
			#group_input_19.CO Offset -> math_11.Value
			hbond_backbone_check_backup.links.new(group_input_19.outputs[1], math_11.inputs[1])
			#group_input_19.NH Index -> math_001_3.Value
			hbond_backbone_check_backup.links.new(group_input_19.outputs[2], math_001_3.inputs[0])
			#group_input_19.NH Offset -> math_001_3.Value
			hbond_backbone_check_backup.links.new(group_input_19.outputs[3], math_001_3.inputs[1])
			#math_11.Value -> math_002_4.Value
			hbond_backbone_check_backup.links.new(math_11.outputs[0], math_002_4.inputs[0])
			#math_001_3.Value -> math_002_4.Value
			hbond_backbone_check_backup.links.new(math_001_3.outputs[0], math_002_4.inputs[1])
			#math_002_4.Value -> math_003_3.Value
			hbond_backbone_check_backup.links.new(math_002_4.outputs[0], math_003_3.inputs[0])
			#math_003_3.Value -> compare_5.A
			hbond_backbone_check_backup.links.new(math_003_3.outputs[0], compare_5.inputs[0])
			#integer_1.Integer -> compare_5.B
			hbond_backbone_check_backup.links.new(integer_1.outputs[0], compare_5.inputs[1])
			#compare_5.Result -> switch_3.Switch
			hbond_backbone_check_backup.links.new(compare_5.outputs[0], switch_3.inputs[0])
			#group_008_3.Bond Vector -> vector_math_5.Vector
			hbond_backbone_check_backup.links.new(group_008_3.outputs[2], vector_math_5.inputs[0])
			#vector_math_5.Value -> compare_001_4.A
			hbond_backbone_check_backup.links.new(vector_math_5.outputs[1], compare_001_4.inputs[0])
			#group_6.Angstrom -> compare_001_4.B
			hbond_backbone_check_backup.links.new(group_6.outputs[0], compare_001_4.inputs[1])
			#switch_3.Output -> group_output_20.Is Bonded
			hbond_backbone_check_backup.links.new(switch_3.outputs[0], group_output_20.inputs[0])
			#group_008_3.Is Bonded -> switch_3.True
			hbond_backbone_check_backup.links.new(group_008_3.outputs[0], switch_3.inputs[2])
			return hbond_backbone_check_backup

		hbond_backbone_check_backup = hbond_backbone_check_backup_node_group()

		#initialize _hbond_i__j__and_hbond_j__i_ node group
		def _hbond_i__j__and_hbond_j__i__node_group():
			_hbond_i__j__and_hbond_j__i_ = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".HBond(i, j) and HBond(j, i)")

			_hbond_i__j__and_hbond_j__i_.color_tag = 'NONE'
			_hbond_i__j__and_hbond_j__i_.description = ""

			
			#_hbond_i__j__and_hbond_j__i_ interface
			#Socket Boolean
			boolean_socket_8 = _hbond_i__j__and_hbond_j__i_.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket_8.default_value = False
			boolean_socket_8.attribute_domain = 'POINT'
			
			#Socket i
			i_socket = _hbond_i__j__and_hbond_j__i_.interface.new_socket(name = "i", in_out='INPUT', socket_type = 'NodeSocketInt')
			i_socket.default_value = 0
			i_socket.min_value = 0
			i_socket.max_value = 2147483647
			i_socket.subtype = 'NONE'
			i_socket.attribute_domain = 'POINT'
			i_socket.hide_value = True
			
			#Socket j
			j_socket = _hbond_i__j__and_hbond_j__i_.interface.new_socket(name = "j", in_out='INPUT', socket_type = 'NodeSocketInt')
			j_socket.default_value = 0
			j_socket.min_value = 0
			j_socket.max_value = 2147483647
			j_socket.subtype = 'NONE'
			j_socket.attribute_domain = 'POINT'
			j_socket.hide_value = True
			
			
			#initialize _hbond_i__j__and_hbond_j__i_ nodes
			#node Group Output
			group_output_21 = _hbond_i__j__and_hbond_j__i_.nodes.new("NodeGroupOutput")
			group_output_21.name = "Group Output"
			group_output_21.is_active_output = True
			
			#node Group Input
			group_input_20 = _hbond_i__j__and_hbond_j__i_.nodes.new("NodeGroupInput")
			group_input_20.name = "Group Input"
			
			#node Group.010
			group_010_1 = _hbond_i__j__and_hbond_j__i_.nodes.new("GeometryNodeGroup")
			group_010_1.name = "Group.010"
			group_010_1.node_tree = hbond_backbone_check
			#Socket_5
			group_010_1.inputs[1].default_value = 0
			#Socket_6
			group_010_1.inputs[3].default_value = 0
			
			#node Group.011
			group_011 = _hbond_i__j__and_hbond_j__i_.nodes.new("GeometryNodeGroup")
			group_011.name = "Group.011"
			group_011.node_tree = hbond_backbone_check
			#Socket_5
			group_011.inputs[1].default_value = 0
			#Socket_6
			group_011.inputs[3].default_value = 0
			
			#node Frame
			frame_4 = _hbond_i__j__and_hbond_j__i_.nodes.new("NodeFrame")
			frame_4.label = "Check Backbone O is bonded to an NH"
			frame_4.name = "Frame"
			frame_4.label_size = 20
			frame_4.shrink = True
			
			#node Frame.001
			frame_001_1 = _hbond_i__j__and_hbond_j__i_.nodes.new("NodeFrame")
			frame_001_1.label = "Check Backbone NH is bonded to an O"
			frame_001_1.name = "Frame.001"
			frame_001_1.label_size = 20
			frame_001_1.shrink = True
			
			#node Boolean Math.003
			boolean_math_003_2 = _hbond_i__j__and_hbond_j__i_.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003_2.name = "Boolean Math.003"
			boolean_math_003_2.operation = 'AND'
			
			#node Group.012
			group_012 = _hbond_i__j__and_hbond_j__i_.nodes.new("GeometryNodeGroup")
			group_012.name = "Group.012"
			group_012.node_tree = hbond_backbone_check_backup
			#Socket_3
			group_012.inputs[0].default_value = 0
			#Socket_5
			group_012.inputs[1].default_value = 0
			#Socket_0
			group_012.inputs[2].default_value = 0
			#Socket_6
			group_012.inputs[3].default_value = 0
			
			
			
			#Set parents
			group_010_1.parent = frame_001_1
			group_011.parent = frame_4
			
			#Set locations
			group_output_21.location = (640.0, 180.0)
			group_input_20.location = (-235.75640869140625, 47.462432861328125)
			group_010_1.location = (-640.0, 40.0)
			group_011.location = (-640.0, -220.0)
			frame_4.location = (635.0, 20.0)
			frame_001_1.location = (630.0, 140.0)
			boolean_math_003_2.location = (435.0, 180.0)
			group_012.location = (-20.0, 520.0)
			
			#Set dimensions
			group_output_21.width, group_output_21.height = 140.0, 100.0
			group_input_20.width, group_input_20.height = 140.0, 100.0
			group_010_1.width, group_010_1.height = 267.0645751953125, 100.0
			group_011.width, group_011.height = 267.0645751953125, 100.0
			frame_4.width, frame_4.height = 327.0645751953125, 309.0
			frame_001_1.width, frame_001_1.height = 327.0645751953125, 309.0
			boolean_math_003_2.width, boolean_math_003_2.height = 140.0, 100.0
			group_012.width, group_012.height = 267.0645751953125, 100.0
			
			#initialize _hbond_i__j__and_hbond_j__i_ links
			#group_010_1.Is Bonded -> boolean_math_003_2.Boolean
			_hbond_i__j__and_hbond_j__i_.links.new(group_010_1.outputs[0], boolean_math_003_2.inputs[0])
			#group_011.Is Bonded -> boolean_math_003_2.Boolean
			_hbond_i__j__and_hbond_j__i_.links.new(group_011.outputs[0], boolean_math_003_2.inputs[1])
			#boolean_math_003_2.Boolean -> group_output_21.Boolean
			_hbond_i__j__and_hbond_j__i_.links.new(boolean_math_003_2.outputs[0], group_output_21.inputs[0])
			#group_input_20.j -> group_010_1.NH Index
			_hbond_i__j__and_hbond_j__i_.links.new(group_input_20.outputs[1], group_010_1.inputs[2])
			#group_input_20.j -> group_011.CO Index
			_hbond_i__j__and_hbond_j__i_.links.new(group_input_20.outputs[1], group_011.inputs[0])
			#group_input_20.i -> group_010_1.CO Index
			_hbond_i__j__and_hbond_j__i_.links.new(group_input_20.outputs[0], group_010_1.inputs[0])
			#group_input_20.i -> group_011.NH Index
			_hbond_i__j__and_hbond_j__i_.links.new(group_input_20.outputs[0], group_011.inputs[2])
			return _hbond_i__j__and_hbond_j__i_

		_hbond_i__j__and_hbond_j__i_ = _hbond_i__j__and_hbond_j__i__node_group()

		#initialize _hbond_i___1__j___1__and_hbond_j___1__i___1_ node group
		def _hbond_i___1__j___1__and_hbond_j___1__i___1__node_group():
			_hbond_i___1__j___1__and_hbond_j___1__i___1_ = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".HBond(i - 1, j + 1) and HBond(j - 1, i + 1)")

			_hbond_i___1__j___1__and_hbond_j___1__i___1_.color_tag = 'NONE'
			_hbond_i___1__j___1__and_hbond_j___1__i___1_.description = ""

			
			#_hbond_i___1__j___1__and_hbond_j___1__i___1_ interface
			#Socket Boolean
			boolean_socket_9 = _hbond_i___1__j___1__and_hbond_j___1__i___1_.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket_9.default_value = False
			boolean_socket_9.attribute_domain = 'POINT'
			
			#Socket i
			i_socket_1 = _hbond_i___1__j___1__and_hbond_j___1__i___1_.interface.new_socket(name = "i", in_out='INPUT', socket_type = 'NodeSocketInt')
			i_socket_1.default_value = 0
			i_socket_1.min_value = 0
			i_socket_1.max_value = 2147483647
			i_socket_1.subtype = 'NONE'
			i_socket_1.attribute_domain = 'POINT'
			i_socket_1.hide_value = True
			
			#Socket j
			j_socket_1 = _hbond_i___1__j___1__and_hbond_j___1__i___1_.interface.new_socket(name = "j", in_out='INPUT', socket_type = 'NodeSocketInt')
			j_socket_1.default_value = 0
			j_socket_1.min_value = 0
			j_socket_1.max_value = 2147483647
			j_socket_1.subtype = 'NONE'
			j_socket_1.attribute_domain = 'POINT'
			j_socket_1.hide_value = True
			
			
			#initialize _hbond_i___1__j___1__and_hbond_j___1__i___1_ nodes
			#node Group Output
			group_output_22 = _hbond_i___1__j___1__and_hbond_j___1__i___1_.nodes.new("NodeGroupOutput")
			group_output_22.name = "Group Output"
			group_output_22.is_active_output = True
			
			#node Group Input
			group_input_21 = _hbond_i___1__j___1__and_hbond_j___1__i___1_.nodes.new("NodeGroupInput")
			group_input_21.name = "Group Input"
			
			#node Group.010
			group_010_2 = _hbond_i___1__j___1__and_hbond_j___1__i___1_.nodes.new("GeometryNodeGroup")
			group_010_2.name = "Group.010"
			group_010_2.node_tree = hbond_backbone_check
			#Socket_5
			group_010_2.inputs[1].default_value = -1
			#Socket_6
			group_010_2.inputs[3].default_value = 1
			
			#node Group.011
			group_011_1 = _hbond_i___1__j___1__and_hbond_j___1__i___1_.nodes.new("GeometryNodeGroup")
			group_011_1.name = "Group.011"
			group_011_1.node_tree = hbond_backbone_check
			#Socket_5
			group_011_1.inputs[1].default_value = -1
			#Socket_6
			group_011_1.inputs[3].default_value = 1
			
			#node Frame
			frame_5 = _hbond_i___1__j___1__and_hbond_j___1__i___1_.nodes.new("NodeFrame")
			frame_5.label = "Check Backbone O is bonded to an NH"
			frame_5.name = "Frame"
			frame_5.label_size = 20
			frame_5.shrink = True
			
			#node Frame.001
			frame_001_2 = _hbond_i___1__j___1__and_hbond_j___1__i___1_.nodes.new("NodeFrame")
			frame_001_2.label = "Check Backbone NH is bonded to an O"
			frame_001_2.name = "Frame.001"
			frame_001_2.label_size = 20
			frame_001_2.shrink = True
			
			#node Boolean Math.003
			boolean_math_003_3 = _hbond_i___1__j___1__and_hbond_j___1__i___1_.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003_3.name = "Boolean Math.003"
			boolean_math_003_3.operation = 'AND'
			
			
			
			#Set parents
			group_010_2.parent = frame_001_2
			group_011_1.parent = frame_5
			
			#Set locations
			group_output_22.location = (625.0, 0.0)
			group_input_21.location = (-394.84100341796875, -236.38262939453125)
			group_010_2.location = (-655.0, 40.0)
			group_011_1.location = (-640.0, -220.0)
			frame_5.location = (635.0, 20.0)
			frame_001_2.location = (655.0, 120.0)
			boolean_math_003_3.location = (435.0, 180.0)
			
			#Set dimensions
			group_output_22.width, group_output_22.height = 140.0, 100.0
			group_input_21.width, group_input_21.height = 140.0, 100.0
			group_010_2.width, group_010_2.height = 267.0645751953125, 100.0
			group_011_1.width, group_011_1.height = 267.0645751953125, 100.0
			frame_5.width, frame_5.height = 327.0645751953125, 309.0
			frame_001_2.width, frame_001_2.height = 327.0645751953125, 309.0
			boolean_math_003_3.width, boolean_math_003_3.height = 140.0, 100.0
			
			#initialize _hbond_i___1__j___1__and_hbond_j___1__i___1_ links
			#group_010_2.Is Bonded -> boolean_math_003_3.Boolean
			_hbond_i___1__j___1__and_hbond_j___1__i___1_.links.new(group_010_2.outputs[0], boolean_math_003_3.inputs[0])
			#group_011_1.Is Bonded -> boolean_math_003_3.Boolean
			_hbond_i___1__j___1__and_hbond_j___1__i___1_.links.new(group_011_1.outputs[0], boolean_math_003_3.inputs[1])
			#boolean_math_003_3.Boolean -> group_output_22.Boolean
			_hbond_i___1__j___1__and_hbond_j___1__i___1_.links.new(boolean_math_003_3.outputs[0], group_output_22.inputs[0])
			#group_input_21.j -> group_010_2.NH Index
			_hbond_i___1__j___1__and_hbond_j___1__i___1_.links.new(group_input_21.outputs[1], group_010_2.inputs[2])
			#group_input_21.j -> group_011_1.CO Index
			_hbond_i___1__j___1__and_hbond_j___1__i___1_.links.new(group_input_21.outputs[1], group_011_1.inputs[0])
			#group_input_21.i -> group_010_2.CO Index
			_hbond_i___1__j___1__and_hbond_j___1__i___1_.links.new(group_input_21.outputs[0], group_010_2.inputs[0])
			#group_input_21.i -> group_011_1.NH Index
			_hbond_i___1__j___1__and_hbond_j___1__i___1_.links.new(group_input_21.outputs[0], group_011_1.inputs[2])
			return _hbond_i___1__j___1__and_hbond_j___1__i___1_

		_hbond_i___1__j___1__and_hbond_j___1__i___1_ = _hbond_i___1__j___1__and_hbond_j___1__i___1__node_group()

		#initialize _hbond_i___1_j__and_hbond_j_i___1_ node group
		def _hbond_i___1_j__and_hbond_j_i___1__node_group():
			_hbond_i___1_j__and_hbond_j_i___1_ = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".Hbond(i - 1,j) and Hbond(j,i + 1)")

			_hbond_i___1_j__and_hbond_j_i___1_.color_tag = 'NONE'
			_hbond_i___1_j__and_hbond_j_i___1_.description = ""

			
			#_hbond_i___1_j__and_hbond_j_i___1_ interface
			#Socket Boolean
			boolean_socket_10 = _hbond_i___1_j__and_hbond_j_i___1_.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket_10.default_value = False
			boolean_socket_10.attribute_domain = 'POINT'
			
			#Socket i
			i_socket_2 = _hbond_i___1_j__and_hbond_j_i___1_.interface.new_socket(name = "i", in_out='INPUT', socket_type = 'NodeSocketInt')
			i_socket_2.default_value = 0
			i_socket_2.min_value = 0
			i_socket_2.max_value = 2147483647
			i_socket_2.subtype = 'NONE'
			i_socket_2.attribute_domain = 'POINT'
			i_socket_2.hide_value = True
			
			#Socket j
			j_socket_2 = _hbond_i___1_j__and_hbond_j_i___1_.interface.new_socket(name = "j", in_out='INPUT', socket_type = 'NodeSocketInt')
			j_socket_2.default_value = 0
			j_socket_2.min_value = 0
			j_socket_2.max_value = 2147483647
			j_socket_2.subtype = 'NONE'
			j_socket_2.attribute_domain = 'POINT'
			j_socket_2.hide_value = True
			
			
			#initialize _hbond_i___1_j__and_hbond_j_i___1_ nodes
			#node Group Output
			group_output_23 = _hbond_i___1_j__and_hbond_j_i___1_.nodes.new("NodeGroupOutput")
			group_output_23.name = "Group Output"
			group_output_23.is_active_output = True
			
			#node Group Input
			group_input_22 = _hbond_i___1_j__and_hbond_j_i___1_.nodes.new("NodeGroupInput")
			group_input_22.name = "Group Input"
			
			#node Group.010
			group_010_3 = _hbond_i___1_j__and_hbond_j_i___1_.nodes.new("GeometryNodeGroup")
			group_010_3.name = "Group.010"
			group_010_3.node_tree = hbond_backbone_check
			#Socket_5
			group_010_3.inputs[1].default_value = -1
			#Socket_6
			group_010_3.inputs[3].default_value = 0
			
			#node Group.011
			group_011_2 = _hbond_i___1_j__and_hbond_j_i___1_.nodes.new("GeometryNodeGroup")
			group_011_2.name = "Group.011"
			group_011_2.node_tree = hbond_backbone_check
			#Socket_5
			group_011_2.inputs[1].default_value = 0
			#Socket_6
			group_011_2.inputs[3].default_value = 1
			
			#node Frame
			frame_6 = _hbond_i___1_j__and_hbond_j_i___1_.nodes.new("NodeFrame")
			frame_6.label = "Check Backbone O is bonded to an NH"
			frame_6.name = "Frame"
			frame_6.label_size = 20
			frame_6.shrink = True
			
			#node Frame.001
			frame_001_3 = _hbond_i___1_j__and_hbond_j_i___1_.nodes.new("NodeFrame")
			frame_001_3.label = "Check Backbone NH is bonded to an O"
			frame_001_3.name = "Frame.001"
			frame_001_3.label_size = 20
			frame_001_3.shrink = True
			
			#node Boolean Math.003
			boolean_math_003_4 = _hbond_i___1_j__and_hbond_j_i___1_.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003_4.name = "Boolean Math.003"
			boolean_math_003_4.operation = 'AND'
			
			
			
			#Set parents
			group_010_3.parent = frame_001_3
			group_011_2.parent = frame_6
			
			#Set locations
			group_output_23.location = (625.0, 0.0)
			group_input_22.location = (-373.2626953125, 13.94732666015625)
			group_010_3.location = (-640.0, 40.0)
			group_011_2.location = (-640.0, -220.0)
			frame_6.location = (635.0, 20.0)
			frame_001_3.location = (655.0, 120.0)
			boolean_math_003_4.location = (435.0, 180.0)
			
			#Set dimensions
			group_output_23.width, group_output_23.height = 140.0, 100.0
			group_input_22.width, group_input_22.height = 140.0, 100.0
			group_010_3.width, group_010_3.height = 267.0645751953125, 100.0
			group_011_2.width, group_011_2.height = 267.0645751953125, 100.0
			frame_6.width, frame_6.height = 327.0645751953125, 309.0
			frame_001_3.width, frame_001_3.height = 327.0645751953125, 309.0
			boolean_math_003_4.width, boolean_math_003_4.height = 140.0, 100.0
			
			#initialize _hbond_i___1_j__and_hbond_j_i___1_ links
			#group_010_3.Is Bonded -> boolean_math_003_4.Boolean
			_hbond_i___1_j__and_hbond_j_i___1_.links.new(group_010_3.outputs[0], boolean_math_003_4.inputs[0])
			#group_011_2.Is Bonded -> boolean_math_003_4.Boolean
			_hbond_i___1_j__and_hbond_j_i___1_.links.new(group_011_2.outputs[0], boolean_math_003_4.inputs[1])
			#boolean_math_003_4.Boolean -> group_output_23.Boolean
			_hbond_i___1_j__and_hbond_j_i___1_.links.new(boolean_math_003_4.outputs[0], group_output_23.inputs[0])
			#group_input_22.j -> group_010_3.NH Index
			_hbond_i___1_j__and_hbond_j_i___1_.links.new(group_input_22.outputs[1], group_010_3.inputs[2])
			#group_input_22.j -> group_011_2.CO Index
			_hbond_i___1_j__and_hbond_j_i___1_.links.new(group_input_22.outputs[1], group_011_2.inputs[0])
			#group_input_22.i -> group_010_3.CO Index
			_hbond_i___1_j__and_hbond_j_i___1_.links.new(group_input_22.outputs[0], group_010_3.inputs[0])
			#group_input_22.i -> group_011_2.NH Index
			_hbond_i___1_j__and_hbond_j_i___1_.links.new(group_input_22.outputs[0], group_011_2.inputs[2])
			return _hbond_i___1_j__and_hbond_j_i___1_

		_hbond_i___1_j__and_hbond_j_i___1_ = _hbond_i___1_j__and_hbond_j_i___1__node_group()

		#initialize _hbond_j___1_i_and_hbond_i_j___1_ node group
		def _hbond_j___1_i_and_hbond_i_j___1__node_group():
			_hbond_j___1_i_and_hbond_i_j___1_ = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".Hbond(j - 1,i)and Hbond(i,j + 1)")

			_hbond_j___1_i_and_hbond_i_j___1_.color_tag = 'NONE'
			_hbond_j___1_i_and_hbond_i_j___1_.description = ""

			
			#_hbond_j___1_i_and_hbond_i_j___1_ interface
			#Socket Boolean
			boolean_socket_11 = _hbond_j___1_i_and_hbond_i_j___1_.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket_11.default_value = False
			boolean_socket_11.attribute_domain = 'POINT'
			
			#Socket i
			i_socket_3 = _hbond_j___1_i_and_hbond_i_j___1_.interface.new_socket(name = "i", in_out='INPUT', socket_type = 'NodeSocketInt')
			i_socket_3.default_value = 0
			i_socket_3.min_value = 0
			i_socket_3.max_value = 2147483647
			i_socket_3.subtype = 'NONE'
			i_socket_3.attribute_domain = 'POINT'
			i_socket_3.hide_value = True
			
			#Socket j
			j_socket_3 = _hbond_j___1_i_and_hbond_i_j___1_.interface.new_socket(name = "j", in_out='INPUT', socket_type = 'NodeSocketInt')
			j_socket_3.default_value = 0
			j_socket_3.min_value = 0
			j_socket_3.max_value = 2147483647
			j_socket_3.subtype = 'NONE'
			j_socket_3.attribute_domain = 'POINT'
			j_socket_3.hide_value = True
			
			
			#initialize _hbond_j___1_i_and_hbond_i_j___1_ nodes
			#node Group Output
			group_output_24 = _hbond_j___1_i_and_hbond_i_j___1_.nodes.new("NodeGroupOutput")
			group_output_24.name = "Group Output"
			group_output_24.is_active_output = True
			
			#node Group Input
			group_input_23 = _hbond_j___1_i_and_hbond_i_j___1_.nodes.new("NodeGroupInput")
			group_input_23.name = "Group Input"
			
			#node Group.010
			group_010_4 = _hbond_j___1_i_and_hbond_i_j___1_.nodes.new("GeometryNodeGroup")
			group_010_4.name = "Group.010"
			group_010_4.node_tree = hbond_backbone_check
			#Socket_5
			group_010_4.inputs[1].default_value = -1
			#Socket_6
			group_010_4.inputs[3].default_value = 0
			
			#node Group.011
			group_011_3 = _hbond_j___1_i_and_hbond_i_j___1_.nodes.new("GeometryNodeGroup")
			group_011_3.name = "Group.011"
			group_011_3.node_tree = hbond_backbone_check
			#Socket_5
			group_011_3.inputs[1].default_value = 0
			#Socket_6
			group_011_3.inputs[3].default_value = 1
			
			#node Frame
			frame_7 = _hbond_j___1_i_and_hbond_i_j___1_.nodes.new("NodeFrame")
			frame_7.label = "Check Backbone O is bonded to an NH"
			frame_7.name = "Frame"
			frame_7.label_size = 20
			frame_7.shrink = True
			
			#node Frame.001
			frame_001_4 = _hbond_j___1_i_and_hbond_i_j___1_.nodes.new("NodeFrame")
			frame_001_4.label = "Check Backbone NH is bonded to an O"
			frame_001_4.name = "Frame.001"
			frame_001_4.label_size = 20
			frame_001_4.shrink = True
			
			#node Boolean Math.003
			boolean_math_003_5 = _hbond_j___1_i_and_hbond_i_j___1_.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003_5.name = "Boolean Math.003"
			boolean_math_003_5.operation = 'AND'
			
			
			
			#Set parents
			group_010_4.parent = frame_001_4
			group_011_3.parent = frame_7
			
			#Set locations
			group_output_24.location = (625.0, 0.0)
			group_input_23.location = (-360.0, 120.0)
			group_010_4.location = (-640.0, 40.0)
			group_011_3.location = (-640.0, -220.0)
			frame_7.location = (635.0, 20.0)
			frame_001_4.location = (655.0, 120.0)
			boolean_math_003_5.location = (435.0, 180.0)
			
			#Set dimensions
			group_output_24.width, group_output_24.height = 140.0, 100.0
			group_input_23.width, group_input_23.height = 140.0, 100.0
			group_010_4.width, group_010_4.height = 267.0645751953125, 100.0
			group_011_3.width, group_011_3.height = 267.0645751953125, 100.0
			frame_7.width, frame_7.height = 327.0645751953125, 309.0
			frame_001_4.width, frame_001_4.height = 327.0645751953125, 309.0
			boolean_math_003_5.width, boolean_math_003_5.height = 140.0, 100.0
			
			#initialize _hbond_j___1_i_and_hbond_i_j___1_ links
			#group_010_4.Is Bonded -> boolean_math_003_5.Boolean
			_hbond_j___1_i_and_hbond_i_j___1_.links.new(group_010_4.outputs[0], boolean_math_003_5.inputs[0])
			#group_011_3.Is Bonded -> boolean_math_003_5.Boolean
			_hbond_j___1_i_and_hbond_i_j___1_.links.new(group_011_3.outputs[0], boolean_math_003_5.inputs[1])
			#boolean_math_003_5.Boolean -> group_output_24.Boolean
			_hbond_j___1_i_and_hbond_i_j___1_.links.new(boolean_math_003_5.outputs[0], group_output_24.inputs[0])
			#group_input_23.j -> group_011_3.NH Index
			_hbond_j___1_i_and_hbond_i_j___1_.links.new(group_input_23.outputs[1], group_011_3.inputs[2])
			#group_input_23.j -> group_010_4.CO Index
			_hbond_j___1_i_and_hbond_i_j___1_.links.new(group_input_23.outputs[1], group_010_4.inputs[0])
			#group_input_23.i -> group_010_4.NH Index
			_hbond_j___1_i_and_hbond_i_j___1_.links.new(group_input_23.outputs[0], group_010_4.inputs[2])
			#group_input_23.i -> group_011_3.CO Index
			_hbond_j___1_i_and_hbond_i_j___1_.links.new(group_input_23.outputs[0], group_011_3.inputs[0])
			return _hbond_j___1_i_and_hbond_i_j___1_

		_hbond_j___1_i_and_hbond_i_j___1_ = _hbond_j___1_i_and_hbond_i_j___1__node_group()

		#initialize _dssp_sheet_checks node group
		def _dssp_sheet_checks_node_group():
			_dssp_sheet_checks = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".DSSP Sheet Checks")

			_dssp_sheet_checks.color_tag = 'NONE'
			_dssp_sheet_checks.description = ""

			
			#_dssp_sheet_checks interface
			#Socket Boolean
			boolean_socket_12 = _dssp_sheet_checks.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket_12.default_value = False
			boolean_socket_12.attribute_domain = 'POINT'
			
			#Socket j
			j_socket_4 = _dssp_sheet_checks.interface.new_socket(name = "j", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			j_socket_4.default_value = 0
			j_socket_4.min_value = -2147483648
			j_socket_4.max_value = 2147483647
			j_socket_4.subtype = 'NONE'
			j_socket_4.attribute_domain = 'POINT'
			
			#Socket Index
			index_socket_3 = _dssp_sheet_checks.interface.new_socket(name = "Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			index_socket_3.default_value = 0
			index_socket_3.min_value = 0
			index_socket_3.max_value = 2147483647
			index_socket_3.subtype = 'NONE'
			index_socket_3.attribute_domain = 'POINT'
			index_socket_3.hide_value = True
			
			#Socket j
			j_socket_5 = _dssp_sheet_checks.interface.new_socket(name = "j", in_out='INPUT', socket_type = 'NodeSocketInt')
			j_socket_5.default_value = 0
			j_socket_5.min_value = -2147483648
			j_socket_5.max_value = 2147483647
			j_socket_5.subtype = 'NONE'
			j_socket_5.attribute_domain = 'POINT'
			
			
			#initialize _dssp_sheet_checks nodes
			#node Group Output
			group_output_25 = _dssp_sheet_checks.nodes.new("NodeGroupOutput")
			group_output_25.name = "Group Output"
			group_output_25.is_active_output = True
			
			#node Group Input
			group_input_24 = _dssp_sheet_checks.nodes.new("NodeGroupInput")
			group_input_24.name = "Group Input"
			
			#node Group.001
			group_001_3 = _dssp_sheet_checks.nodes.new("GeometryNodeGroup")
			group_001_3.name = "Group.001"
			group_001_3.node_tree = _hbond_i__j__and_hbond_j__i_
			
			#node Group.002
			group_002_3 = _dssp_sheet_checks.nodes.new("GeometryNodeGroup")
			group_002_3.name = "Group.002"
			group_002_3.node_tree = _hbond_i___1__j___1__and_hbond_j___1__i___1_
			
			#node Boolean Math
			boolean_math_4 = _dssp_sheet_checks.nodes.new("FunctionNodeBooleanMath")
			boolean_math_4.name = "Boolean Math"
			boolean_math_4.operation = 'OR'
			
			#node Group.004
			group_004_2 = _dssp_sheet_checks.nodes.new("GeometryNodeGroup")
			group_004_2.name = "Group.004"
			group_004_2.node_tree = _hbond_i___1_j__and_hbond_j_i___1_
			
			#node Frame
			frame_8 = _dssp_sheet_checks.nodes.new("NodeFrame")
			frame_8.label = "Anti-parallel Bridge"
			frame_8.name = "Frame"
			frame_8.label_size = 20
			frame_8.shrink = True
			
			#node Frame.001
			frame_001_5 = _dssp_sheet_checks.nodes.new("NodeFrame")
			frame_001_5.label = "Paralell Bridge"
			frame_001_5.name = "Frame.001"
			frame_001_5.label_size = 20
			frame_001_5.shrink = True
			
			#node Boolean Math.001
			boolean_math_001_2 = _dssp_sheet_checks.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_2.name = "Boolean Math.001"
			boolean_math_001_2.operation = 'OR'
			
			#node Boolean Math.002
			boolean_math_002_2 = _dssp_sheet_checks.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_2.name = "Boolean Math.002"
			boolean_math_002_2.operation = 'OR'
			
			#node Group.005
			group_005_3 = _dssp_sheet_checks.nodes.new("GeometryNodeGroup")
			group_005_3.name = "Group.005"
			group_005_3.node_tree = _hbond_j___1_i_and_hbond_i_j___1_
			
			
			
			#Set parents
			group_001_3.parent = frame_8
			group_002_3.parent = frame_8
			boolean_math_4.parent = frame_8
			group_004_2.parent = frame_001_5
			boolean_math_001_2.parent = frame_001_5
			group_005_3.parent = frame_001_5
			
			#Set locations
			group_output_25.location = (570.0, 0.0)
			group_input_24.location = (-657.7005004882812, 1.8694610595703125)
			group_001_3.location = (-800.0, 160.0)
			group_002_3.location = (-800.0, 0.0)
			boolean_math_4.location = (-440.0, 160.0)
			group_004_2.location = (-800.0, -300.0)
			frame_8.location = (580.0, 180.0)
			frame_001_5.location = (580.0, 180.0)
			boolean_math_001_2.location = (-440.0, -300.0)
			boolean_math_002_2.location = (380.0, 140.0)
			group_005_3.location = (-800.0, -460.0)
			
			#Set dimensions
			group_output_25.width, group_output_25.height = 140.0, 100.0
			group_input_24.width, group_input_24.height = 140.0, 100.0
			group_001_3.width, group_001_3.height = 333.0748291015625, 100.0
			group_002_3.width, group_002_3.height = 333.0748291015625, 100.0
			boolean_math_4.width, boolean_math_4.height = 140.0, 100.0
			group_004_2.width, group_004_2.height = 333.0748291015625, 100.0
			frame_8.width, frame_8.height = 560.0, 350.0
			frame_001_5.width, frame_001_5.height = 560.0, 350.0
			boolean_math_001_2.width, boolean_math_001_2.height = 140.0, 100.0
			boolean_math_002_2.width, boolean_math_002_2.height = 140.0, 100.0
			group_005_3.width, group_005_3.height = 333.0748291015625, 100.0
			
			#initialize _dssp_sheet_checks links
			#group_001_3.Boolean -> boolean_math_4.Boolean
			_dssp_sheet_checks.links.new(group_001_3.outputs[0], boolean_math_4.inputs[0])
			#group_input_24.j -> group_002_3.j
			_dssp_sheet_checks.links.new(group_input_24.outputs[1], group_002_3.inputs[1])
			#boolean_math_001_2.Boolean -> boolean_math_002_2.Boolean
			_dssp_sheet_checks.links.new(boolean_math_001_2.outputs[0], boolean_math_002_2.inputs[1])
			#group_004_2.Boolean -> boolean_math_001_2.Boolean
			_dssp_sheet_checks.links.new(group_004_2.outputs[0], boolean_math_001_2.inputs[0])
			#group_input_24.j -> group_005_3.j
			_dssp_sheet_checks.links.new(group_input_24.outputs[1], group_005_3.inputs[1])
			#group_002_3.Boolean -> boolean_math_4.Boolean
			_dssp_sheet_checks.links.new(group_002_3.outputs[0], boolean_math_4.inputs[1])
			#group_input_24.j -> group_001_3.j
			_dssp_sheet_checks.links.new(group_input_24.outputs[1], group_001_3.inputs[1])
			#boolean_math_4.Boolean -> boolean_math_002_2.Boolean
			_dssp_sheet_checks.links.new(boolean_math_4.outputs[0], boolean_math_002_2.inputs[0])
			#group_005_3.Boolean -> boolean_math_001_2.Boolean
			_dssp_sheet_checks.links.new(group_005_3.outputs[0], boolean_math_001_2.inputs[1])
			#group_input_24.j -> group_004_2.j
			_dssp_sheet_checks.links.new(group_input_24.outputs[1], group_004_2.inputs[1])
			#boolean_math_002_2.Boolean -> group_output_25.Boolean
			_dssp_sheet_checks.links.new(boolean_math_002_2.outputs[0], group_output_25.inputs[0])
			#group_input_24.Index -> group_001_3.i
			_dssp_sheet_checks.links.new(group_input_24.outputs[0], group_001_3.inputs[0])
			#group_input_24.Index -> group_002_3.i
			_dssp_sheet_checks.links.new(group_input_24.outputs[0], group_002_3.inputs[0])
			#group_input_24.Index -> group_004_2.i
			_dssp_sheet_checks.links.new(group_input_24.outputs[0], group_004_2.inputs[0])
			#group_input_24.Index -> group_005_3.i
			_dssp_sheet_checks.links.new(group_input_24.outputs[0], group_005_3.inputs[0])
			#group_input_24.j -> group_output_25.j
			_dssp_sheet_checks.links.new(group_input_24.outputs[1], group_output_25.inputs[1])
			return _dssp_sheet_checks

		_dssp_sheet_checks = _dssp_sheet_checks_node_group()

		#initialize _mn_topo_calc_sheet node group
		def _mn_topo_calc_sheet_node_group():
			_mn_topo_calc_sheet = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_topo_calc_sheet")

			_mn_topo_calc_sheet.color_tag = 'NONE'
			_mn_topo_calc_sheet.description = ""

			
			#_mn_topo_calc_sheet interface
			#Socket Geometry
			geometry_socket = _mn_topo_calc_sheet.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket.attribute_domain = 'POINT'
			
			#Socket Attribute
			attribute_socket = _mn_topo_calc_sheet.interface.new_socket(name = "Attribute", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			attribute_socket.default_value = False
			attribute_socket.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_1 = _mn_topo_calc_sheet.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_1.attribute_domain = 'POINT'
			
			
			#initialize _mn_topo_calc_sheet nodes
			#node Group Output
			group_output_26 = _mn_topo_calc_sheet.nodes.new("NodeGroupOutput")
			group_output_26.name = "Group Output"
			group_output_26.is_active_output = True
			
			#node Group Input
			group_input_25 = _mn_topo_calc_sheet.nodes.new("NodeGroupInput")
			group_input_25.name = "Group Input"
			
			#node Capture Attribute.002
			capture_attribute_002 = _mn_topo_calc_sheet.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute_002.name = "Capture Attribute.002"
			capture_attribute_002.active_index = 0
			capture_attribute_002.capture_items.clear()
			capture_attribute_002.capture_items.new('FLOAT', "Value")
			capture_attribute_002.capture_items["Value"].data_type = 'BOOLEAN'
			capture_attribute_002.domain = 'POINT'
			
			#node Group.003
			group_003_4 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_003_4.name = "Group.003"
			group_003_4.node_tree = boolean_run_mask
			#Socket_2
			group_003_4.inputs[1].default_value = 0
			#Socket_3
			group_003_4.inputs[2].default_value = 3
			#Socket_6
			group_003_4.inputs[3].default_value = 0
			
			#node Group
			group_7 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_7.name = "Group"
			group_7.mute = True
			group_7.node_tree = boolean_run_fill
			#Socket_2
			group_7.inputs[1].default_value = 1
			
			#node Group.006
			group_006_2 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_006_2.name = "Group.006"
			group_006_2.node_tree = self_sample_proximity
			
			#node Group.007
			group_007_1 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_007_1.name = "Group.007"
			group_007_1.node_tree = mn_topo_backbone
			#Socket_3
			group_007_1.inputs[0].default_value = 0
			
			#node Capture Attribute
			capture_attribute = _mn_topo_calc_sheet.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute.name = "Capture Attribute"
			capture_attribute.active_index = 3
			capture_attribute.capture_items.clear()
			capture_attribute.capture_items.new('FLOAT', "Value")
			capture_attribute.capture_items["Value"].data_type = 'INT'
			capture_attribute.capture_items.new('FLOAT', "Closest Index")
			capture_attribute.capture_items["Closest Index"].data_type = 'INT'
			capture_attribute.capture_items.new('FLOAT', "Closest Index.001")
			capture_attribute.capture_items["Closest Index.001"].data_type = 'INT'
			capture_attribute.capture_items.new('FLOAT', "Closest Index.002")
			capture_attribute.capture_items["Closest Index.002"].data_type = 'INT'
			capture_attribute.domain = 'POINT'
			
			#node Group.008
			group_008_4 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_008_4.name = "Group.008"
			group_008_4.node_tree = _dssp_sheet_checks
			#Socket_3
			group_008_4.inputs[0].default_value = 0
			
			#node Group.009
			group_009_4 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_009_4.name = "Group.009"
			group_009_4.node_tree = _dssp_sheet_checks
			#Socket_3
			group_009_4.inputs[0].default_value = 0
			
			#node Boolean Math
			boolean_math_5 = _mn_topo_calc_sheet.nodes.new("FunctionNodeBooleanMath")
			boolean_math_5.name = "Boolean Math"
			boolean_math_5.operation = 'OR'
			
			#node Group.010
			group_010_5 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_010_5.name = "Group.010"
			group_010_5.node_tree = _dssp_sheet_checks
			#Socket_3
			group_010_5.inputs[0].default_value = 0
			
			#node Boolean Math.001
			boolean_math_001_3 = _mn_topo_calc_sheet.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_3.name = "Boolean Math.001"
			boolean_math_001_3.operation = 'OR'
			
			#node Group.011
			group_011_4 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_011_4.name = "Group.011"
			group_011_4.node_tree = self_sample_proximity
			
			#node Group.012
			group_012_1 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_012_1.name = "Group.012"
			group_012_1.node_tree = mn_topo_backbone
			#Socket_3
			group_012_1.inputs[0].default_value = 0
			
			#node Vector Math
			vector_math_6 = _mn_topo_calc_sheet.nodes.new("ShaderNodeVectorMath")
			vector_math_6.name = "Vector Math"
			vector_math_6.operation = 'SUBTRACT'
			
			#node Vector Math.001
			vector_math_001_3 = _mn_topo_calc_sheet.nodes.new("ShaderNodeVectorMath")
			vector_math_001_3.name = "Vector Math.001"
			vector_math_001_3.operation = 'ADD'
			
			#node Vector Math.002
			vector_math_002_3 = _mn_topo_calc_sheet.nodes.new("ShaderNodeVectorMath")
			vector_math_002_3.name = "Vector Math.002"
			vector_math_002_3.operation = 'SCALE'
			#Scale
			vector_math_002_3.inputs[3].default_value = 3.0
			
			#node Group.013
			group_013 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_013.name = "Group.013"
			group_013.node_tree = self_sample_proximity
			
			#node Group.014
			group_014 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_014.name = "Group.014"
			group_014.node_tree = self_sample_proximity
			
			#node Vector Math.003
			vector_math_003_2 = _mn_topo_calc_sheet.nodes.new("ShaderNodeVectorMath")
			vector_math_003_2.name = "Vector Math.003"
			vector_math_003_2.operation = 'SUBTRACT'
			
			#node Group.015
			group_015 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_015.name = "Group.015"
			group_015.node_tree = _dssp_sheet_checks
			#Socket_3
			group_015.inputs[0].default_value = 0
			
			#node Boolean Math.002
			boolean_math_002_3 = _mn_topo_calc_sheet.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_3.name = "Boolean Math.002"
			boolean_math_002_3.operation = 'OR'
			
			#node Group.016
			group_016 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_016.name = "Group.016"
			group_016.node_tree = _dssp_sheet_checks
			#Socket_3
			group_016.inputs[0].default_value = 0
			
			#node Boolean Math.003
			boolean_math_003_6 = _mn_topo_calc_sheet.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003_6.name = "Boolean Math.003"
			boolean_math_003_6.operation = 'OR'
			
			#node Group.017
			group_017_1 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_017_1.name = "Group.017"
			group_017_1.node_tree = _dssp_sheet_checks
			#Socket_3
			group_017_1.inputs[0].default_value = 0
			
			#node Reroute
			reroute_5 = _mn_topo_calc_sheet.nodes.new("NodeReroute")
			reroute_5.name = "Reroute"
			#node Boolean Math.004
			boolean_math_004_2 = _mn_topo_calc_sheet.nodes.new("FunctionNodeBooleanMath")
			boolean_math_004_2.name = "Boolean Math.004"
			boolean_math_004_2.operation = 'OR'
			
			#node Store Named Attribute
			store_named_attribute = _mn_topo_calc_sheet.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute.name = "Store Named Attribute"
			store_named_attribute.data_type = 'INT'
			store_named_attribute.domain = 'POINT'
			#Name
			store_named_attribute.inputs[2].default_value = "tmp_bonded_idx"
			
			#node Store Named Attribute.001
			store_named_attribute_001 = _mn_topo_calc_sheet.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_001.name = "Store Named Attribute.001"
			store_named_attribute_001.data_type = 'INT'
			store_named_attribute_001.domain = 'POINT'
			#Name
			store_named_attribute_001.inputs[2].default_value = "tmp_bonded_idx"
			
			#node Store Named Attribute.002
			store_named_attribute_002 = _mn_topo_calc_sheet.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_002.name = "Store Named Attribute.002"
			store_named_attribute_002.data_type = 'INT'
			store_named_attribute_002.domain = 'POINT'
			#Selection
			store_named_attribute_002.inputs[1].default_value = True
			#Name
			store_named_attribute_002.inputs[2].default_value = "tmp_bonded_idx"
			#Value
			store_named_attribute_002.inputs[3].default_value = -1
			
			#node Store Named Attribute.003
			store_named_attribute_003 = _mn_topo_calc_sheet.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_003.name = "Store Named Attribute.003"
			store_named_attribute_003.data_type = 'INT'
			store_named_attribute_003.domain = 'POINT'
			#Name
			store_named_attribute_003.inputs[2].default_value = "tmp_bonded_idx"
			
			#node Store Named Attribute.004
			store_named_attribute_004 = _mn_topo_calc_sheet.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_004.name = "Store Named Attribute.004"
			store_named_attribute_004.data_type = 'INT'
			store_named_attribute_004.domain = 'POINT'
			#Name
			store_named_attribute_004.inputs[2].default_value = "tmp_bonded_idx"
			
			#node Store Named Attribute.005
			store_named_attribute_005 = _mn_topo_calc_sheet.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_005.name = "Store Named Attribute.005"
			store_named_attribute_005.data_type = 'INT'
			store_named_attribute_005.domain = 'POINT'
			#Name
			store_named_attribute_005.inputs[2].default_value = "tmp_bonded_idx"
			
			#node Store Named Attribute.006
			store_named_attribute_006 = _mn_topo_calc_sheet.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_006.name = "Store Named Attribute.006"
			store_named_attribute_006.data_type = 'INT'
			store_named_attribute_006.domain = 'POINT'
			#Name
			store_named_attribute_006.inputs[2].default_value = "tmp_bonded_idx"
			
			#node Group.001
			group_001_4 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_001_4.name = "Group.001"
			group_001_4.node_tree = offset_integer
			#Socket_1
			group_001_4.inputs[0].default_value = 0
			#Socket_2
			group_001_4.inputs[2].default_value = 1
			
			#node Math
			math_12 = _mn_topo_calc_sheet.nodes.new("ShaderNodeMath")
			math_12.name = "Math"
			math_12.operation = 'ADD'
			math_12.use_clamp = False
			#Value_001
			math_12.inputs[1].default_value = -1.0
			
			#node Group.002
			group_002_4 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_002_4.name = "Group.002"
			group_002_4.node_tree = offset_integer
			#Socket_1
			group_002_4.inputs[0].default_value = 0
			#Socket_2
			group_002_4.inputs[2].default_value = 1
			
			#node Math.001
			math_001_4 = _mn_topo_calc_sheet.nodes.new("ShaderNodeMath")
			math_001_4.name = "Math.001"
			math_001_4.operation = 'ADD'
			math_001_4.use_clamp = False
			#Value_001
			math_001_4.inputs[1].default_value = -1.0
			
			
			
			
			#Set locations
			group_output_26.location = (1360.0, 240.0)
			group_input_25.location = (-1780.0, 80.0)
			capture_attribute_002.location = (960.0, 240.0)
			group_003_4.location = (960.0, -80.0)
			group_7.location = (960.0, 60.0)
			group_006_2.location = (-1520.0, 20.0)
			group_007_1.location = (-2100.0, -60.0)
			capture_attribute.location = (-1240.0, 100.0)
			group_008_4.location = (-340.0, 20.0)
			group_009_4.location = (-340.0, -120.0)
			boolean_math_5.location = (40.0, 0.0)
			group_010_5.location = (-340.0, -260.0)
			boolean_math_001_3.location = (40.0, -140.0)
			group_011_4.location = (-1520.0, -320.0)
			group_012_1.location = (-2300.0, -280.0)
			vector_math_6.location = (-2060.0, -600.0)
			vector_math_001_3.location = (-1740.0, -600.0)
			vector_math_002_3.location = (-1900.0, -600.0)
			group_013.location = (-1520.0, -140.0)
			group_014.location = (-1520.0, -480.0)
			vector_math_003_2.location = (-1740.0, -740.0)
			group_015.location = (-340.0, -400.0)
			boolean_math_002_3.location = (40.0, -280.0)
			group_016.location = (-344.5273742675781, -540.385498046875)
			boolean_math_003_6.location = (40.0, -440.0)
			group_017_1.location = (-340.0, -680.0)
			reroute_5.location = (-740.0, -640.0)
			boolean_math_004_2.location = (40.0, -600.0)
			store_named_attribute.location = (-180.0, 240.0)
			store_named_attribute_001.location = (-20.0, 240.0)
			store_named_attribute_002.location = (-340.0, 240.0)
			store_named_attribute_003.location = (140.0, 240.0)
			store_named_attribute_004.location = (300.0, 240.0)
			store_named_attribute_005.location = (460.0, 240.0)
			store_named_attribute_006.location = (620.0, 240.0)
			group_001_4.location = (-680.0, -540.0)
			math_12.location = (-520.0, -540.0)
			group_002_4.location = (-680.0, -720.0)
			math_001_4.location = (-520.0, -720.0)
			
			#Set dimensions
			group_output_26.width, group_output_26.height = 140.0, 100.0
			group_input_25.width, group_input_25.height = 140.0, 100.0
			capture_attribute_002.width, capture_attribute_002.height = 140.0, 100.0
			group_003_4.width, group_003_4.height = 167.49020385742188, 100.0
			group_7.width, group_7.height = 140.0, 100.0
			group_006_2.width, group_006_2.height = 140.0, 100.0
			group_007_1.width, group_007_1.height = 140.0, 100.0
			capture_attribute.width, capture_attribute.height = 140.0, 100.0
			group_008_4.width, group_008_4.height = 140.0, 100.0
			group_009_4.width, group_009_4.height = 140.0, 100.0
			boolean_math_5.width, boolean_math_5.height = 140.0, 100.0
			group_010_5.width, group_010_5.height = 140.0, 100.0
			boolean_math_001_3.width, boolean_math_001_3.height = 140.0, 100.0
			group_011_4.width, group_011_4.height = 140.0, 100.0
			group_012_1.width, group_012_1.height = 140.0, 100.0
			vector_math_6.width, vector_math_6.height = 140.0, 100.0
			vector_math_001_3.width, vector_math_001_3.height = 140.0, 100.0
			vector_math_002_3.width, vector_math_002_3.height = 140.0, 100.0
			group_013.width, group_013.height = 140.0, 100.0
			group_014.width, group_014.height = 140.0, 100.0
			vector_math_003_2.width, vector_math_003_2.height = 140.0, 100.0
			group_015.width, group_015.height = 140.0, 100.0
			boolean_math_002_3.width, boolean_math_002_3.height = 140.0, 100.0
			group_016.width, group_016.height = 140.0, 100.0
			boolean_math_003_6.width, boolean_math_003_6.height = 140.0, 100.0
			group_017_1.width, group_017_1.height = 140.0, 100.0
			reroute_5.width, reroute_5.height = 16.0, 100.0
			boolean_math_004_2.width, boolean_math_004_2.height = 140.0, 100.0
			store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
			store_named_attribute_001.width, store_named_attribute_001.height = 140.0, 100.0
			store_named_attribute_002.width, store_named_attribute_002.height = 140.0, 100.0
			store_named_attribute_003.width, store_named_attribute_003.height = 140.0, 100.0
			store_named_attribute_004.width, store_named_attribute_004.height = 140.0, 100.0
			store_named_attribute_005.width, store_named_attribute_005.height = 140.0, 100.0
			store_named_attribute_006.width, store_named_attribute_006.height = 140.0, 100.0
			group_001_4.width, group_001_4.height = 140.0, 100.0
			math_12.width, math_12.height = 140.0, 100.0
			group_002_4.width, group_002_4.height = 140.0, 100.0
			math_001_4.width, math_001_4.height = 140.0, 100.0
			
			#initialize _mn_topo_calc_sheet links
			#store_named_attribute_006.Geometry -> capture_attribute_002.Geometry
			_mn_topo_calc_sheet.links.new(store_named_attribute_006.outputs[0], capture_attribute_002.inputs[0])
			#capture_attribute_002.Geometry -> group_output_26.Geometry
			_mn_topo_calc_sheet.links.new(capture_attribute_002.outputs[0], group_output_26.inputs[0])
			#capture_attribute_002.Value -> group_output_26.Attribute
			_mn_topo_calc_sheet.links.new(capture_attribute_002.outputs[1], group_output_26.inputs[1])
			#group_7.Boolean -> capture_attribute_002.Value
			_mn_topo_calc_sheet.links.new(group_7.outputs[0], capture_attribute_002.inputs[1])
			#group_input_25.Geometry -> group_006_2.Input
			_mn_topo_calc_sheet.links.new(group_input_25.outputs[0], group_006_2.inputs[0])
			#group_007_1.NH -> group_006_2.Target Position
			_mn_topo_calc_sheet.links.new(group_007_1.outputs[4], group_006_2.inputs[1])
			#group_007_1.O -> group_006_2.Self Position
			_mn_topo_calc_sheet.links.new(group_007_1.outputs[0], group_006_2.inputs[2])
			#group_input_25.Geometry -> capture_attribute.Geometry
			_mn_topo_calc_sheet.links.new(group_input_25.outputs[0], capture_attribute.inputs[0])
			#group_006_2.Closest Index -> capture_attribute.Value
			_mn_topo_calc_sheet.links.new(group_006_2.outputs[0], capture_attribute.inputs[1])
			#capture_attribute.Value -> group_008_4.j
			_mn_topo_calc_sheet.links.new(capture_attribute.outputs[1], group_008_4.inputs[1])
			#group_008_4.Boolean -> boolean_math_5.Boolean
			_mn_topo_calc_sheet.links.new(group_008_4.outputs[0], boolean_math_5.inputs[0])
			#group_003_4.Boolean -> group_7.Boolean
			_mn_topo_calc_sheet.links.new(group_003_4.outputs[0], group_7.inputs[0])
			#boolean_math_5.Boolean -> boolean_math_001_3.Boolean
			_mn_topo_calc_sheet.links.new(boolean_math_5.outputs[0], boolean_math_001_3.inputs[0])
			#group_input_25.Geometry -> group_011_4.Input
			_mn_topo_calc_sheet.links.new(group_input_25.outputs[0], group_011_4.inputs[0])
			#capture_attribute.Closest Index -> group_009_4.j
			_mn_topo_calc_sheet.links.new(capture_attribute.outputs[2], group_009_4.inputs[1])
			#group_012_1.O -> vector_math_6.Vector
			_mn_topo_calc_sheet.links.new(group_012_1.outputs[0], vector_math_6.inputs[1])
			#group_012_1.CA -> vector_math_001_3.Vector
			_mn_topo_calc_sheet.links.new(group_012_1.outputs[2], vector_math_001_3.inputs[0])
			#vector_math_6.Vector -> vector_math_002_3.Vector
			_mn_topo_calc_sheet.links.new(vector_math_6.outputs[0], vector_math_002_3.inputs[0])
			#vector_math_002_3.Vector -> vector_math_001_3.Vector
			_mn_topo_calc_sheet.links.new(vector_math_002_3.outputs[0], vector_math_001_3.inputs[1])
			#group_012_1.CA -> group_011_4.Target Position
			_mn_topo_calc_sheet.links.new(group_012_1.outputs[2], group_011_4.inputs[1])
			#vector_math_001_3.Vector -> group_011_4.Self Position
			_mn_topo_calc_sheet.links.new(vector_math_001_3.outputs[0], group_011_4.inputs[2])
			#group_012_1.C -> vector_math_6.Vector
			_mn_topo_calc_sheet.links.new(group_012_1.outputs[1], vector_math_6.inputs[0])
			#group_input_25.Geometry -> group_013.Input
			_mn_topo_calc_sheet.links.new(group_input_25.outputs[0], group_013.inputs[0])
			#capture_attribute.Closest Index.001 -> group_010_5.j
			_mn_topo_calc_sheet.links.new(capture_attribute.outputs[3], group_010_5.inputs[1])
			#group_012_1.NH -> group_013.Self Position
			_mn_topo_calc_sheet.links.new(group_012_1.outputs[4], group_013.inputs[2])
			#group_012_1.O -> group_013.Target Position
			_mn_topo_calc_sheet.links.new(group_012_1.outputs[0], group_013.inputs[1])
			#group_010_5.Boolean -> boolean_math_001_3.Boolean
			_mn_topo_calc_sheet.links.new(group_010_5.outputs[0], boolean_math_001_3.inputs[1])
			#group_009_4.Boolean -> boolean_math_5.Boolean
			_mn_topo_calc_sheet.links.new(group_009_4.outputs[0], boolean_math_5.inputs[1])
			#group_input_25.Geometry -> group_014.Input
			_mn_topo_calc_sheet.links.new(group_input_25.outputs[0], group_014.inputs[0])
			#group_012_1.CA -> group_014.Target Position
			_mn_topo_calc_sheet.links.new(group_012_1.outputs[2], group_014.inputs[1])
			#group_012_1.CA -> vector_math_003_2.Vector
			_mn_topo_calc_sheet.links.new(group_012_1.outputs[2], vector_math_003_2.inputs[0])
			#vector_math_002_3.Vector -> vector_math_003_2.Vector
			_mn_topo_calc_sheet.links.new(vector_math_002_3.outputs[0], vector_math_003_2.inputs[1])
			#vector_math_003_2.Vector -> group_014.Self Position
			_mn_topo_calc_sheet.links.new(vector_math_003_2.outputs[0], group_014.inputs[2])
			#capture_attribute.Closest Index.002 -> group_015.j
			_mn_topo_calc_sheet.links.new(capture_attribute.outputs[4], group_015.inputs[1])
			#boolean_math_001_3.Boolean -> boolean_math_002_3.Boolean
			_mn_topo_calc_sheet.links.new(boolean_math_001_3.outputs[0], boolean_math_002_3.inputs[0])
			#group_015.Boolean -> boolean_math_002_3.Boolean
			_mn_topo_calc_sheet.links.new(group_015.outputs[0], boolean_math_002_3.inputs[1])
			#boolean_math_002_3.Boolean -> boolean_math_003_6.Boolean
			_mn_topo_calc_sheet.links.new(boolean_math_002_3.outputs[0], boolean_math_003_6.inputs[0])
			#group_016.Boolean -> boolean_math_003_6.Boolean
			_mn_topo_calc_sheet.links.new(group_016.outputs[0], boolean_math_003_6.inputs[1])
			#capture_attribute.Value -> reroute_5.Input
			_mn_topo_calc_sheet.links.new(capture_attribute.outputs[1], reroute_5.inputs[0])
			#boolean_math_003_6.Boolean -> boolean_math_004_2.Boolean
			_mn_topo_calc_sheet.links.new(boolean_math_003_6.outputs[0], boolean_math_004_2.inputs[0])
			#group_017_1.Boolean -> boolean_math_004_2.Boolean
			_mn_topo_calc_sheet.links.new(group_017_1.outputs[0], boolean_math_004_2.inputs[1])
			#boolean_math_004_2.Boolean -> group_003_4.Boolean
			_mn_topo_calc_sheet.links.new(boolean_math_004_2.outputs[0], group_003_4.inputs[0])
			#store_named_attribute_002.Geometry -> store_named_attribute.Geometry
			_mn_topo_calc_sheet.links.new(store_named_attribute_002.outputs[0], store_named_attribute.inputs[0])
			#group_008_4.j -> store_named_attribute.Value
			_mn_topo_calc_sheet.links.new(group_008_4.outputs[1], store_named_attribute.inputs[3])
			#group_008_4.Boolean -> store_named_attribute.Selection
			_mn_topo_calc_sheet.links.new(group_008_4.outputs[0], store_named_attribute.inputs[1])
			#store_named_attribute.Geometry -> store_named_attribute_001.Geometry
			_mn_topo_calc_sheet.links.new(store_named_attribute.outputs[0], store_named_attribute_001.inputs[0])
			#group_009_4.Boolean -> store_named_attribute_001.Selection
			_mn_topo_calc_sheet.links.new(group_009_4.outputs[0], store_named_attribute_001.inputs[1])
			#group_009_4.j -> store_named_attribute_001.Value
			_mn_topo_calc_sheet.links.new(group_009_4.outputs[1], store_named_attribute_001.inputs[3])
			#capture_attribute.Geometry -> store_named_attribute_002.Geometry
			_mn_topo_calc_sheet.links.new(capture_attribute.outputs[0], store_named_attribute_002.inputs[0])
			#store_named_attribute_001.Geometry -> store_named_attribute_003.Geometry
			_mn_topo_calc_sheet.links.new(store_named_attribute_001.outputs[0], store_named_attribute_003.inputs[0])
			#group_010_5.Boolean -> store_named_attribute_003.Selection
			_mn_topo_calc_sheet.links.new(group_010_5.outputs[0], store_named_attribute_003.inputs[1])
			#group_010_5.j -> store_named_attribute_003.Value
			_mn_topo_calc_sheet.links.new(group_010_5.outputs[1], store_named_attribute_003.inputs[3])
			#store_named_attribute_003.Geometry -> store_named_attribute_004.Geometry
			_mn_topo_calc_sheet.links.new(store_named_attribute_003.outputs[0], store_named_attribute_004.inputs[0])
			#group_015.Boolean -> store_named_attribute_004.Selection
			_mn_topo_calc_sheet.links.new(group_015.outputs[0], store_named_attribute_004.inputs[1])
			#group_015.j -> store_named_attribute_004.Value
			_mn_topo_calc_sheet.links.new(group_015.outputs[1], store_named_attribute_004.inputs[3])
			#store_named_attribute_004.Geometry -> store_named_attribute_005.Geometry
			_mn_topo_calc_sheet.links.new(store_named_attribute_004.outputs[0], store_named_attribute_005.inputs[0])
			#group_016.Boolean -> store_named_attribute_005.Selection
			_mn_topo_calc_sheet.links.new(group_016.outputs[0], store_named_attribute_005.inputs[1])
			#group_016.j -> store_named_attribute_005.Value
			_mn_topo_calc_sheet.links.new(group_016.outputs[1], store_named_attribute_005.inputs[3])
			#store_named_attribute_005.Geometry -> store_named_attribute_006.Geometry
			_mn_topo_calc_sheet.links.new(store_named_attribute_005.outputs[0], store_named_attribute_006.inputs[0])
			#group_017_1.Boolean -> store_named_attribute_006.Selection
			_mn_topo_calc_sheet.links.new(group_017_1.outputs[0], store_named_attribute_006.inputs[1])
			#group_017_1.j -> store_named_attribute_006.Value
			_mn_topo_calc_sheet.links.new(group_017_1.outputs[1], store_named_attribute_006.inputs[3])
			#group_001_4.Value -> math_12.Value
			_mn_topo_calc_sheet.links.new(group_001_4.outputs[0], math_12.inputs[0])
			#reroute_5.Output -> group_001_4.Value
			_mn_topo_calc_sheet.links.new(reroute_5.outputs[0], group_001_4.inputs[1])
			#math_12.Value -> group_016.j
			_mn_topo_calc_sheet.links.new(math_12.outputs[0], group_016.inputs[1])
			#group_002_4.Value -> math_001_4.Value
			_mn_topo_calc_sheet.links.new(group_002_4.outputs[0], math_001_4.inputs[0])
			#reroute_5.Output -> group_002_4.Value
			_mn_topo_calc_sheet.links.new(reroute_5.outputs[0], group_002_4.inputs[1])
			#math_001_4.Value -> group_017_1.j
			_mn_topo_calc_sheet.links.new(math_001_4.outputs[0], group_017_1.inputs[1])
			#group_013.Closest Index -> capture_attribute.Closest Index
			_mn_topo_calc_sheet.links.new(group_013.outputs[0], capture_attribute.inputs[2])
			#group_011_4.Closest Index -> capture_attribute.Closest Index.001
			_mn_topo_calc_sheet.links.new(group_011_4.outputs[0], capture_attribute.inputs[3])
			#group_014.Closest Index -> capture_attribute.Closest Index.002
			_mn_topo_calc_sheet.links.new(group_014.outputs[0], capture_attribute.inputs[4])
			return _mn_topo_calc_sheet

		_mn_topo_calc_sheet = _mn_topo_calc_sheet_node_group()

		#initialize group_pick node group
		def group_pick_node_group():
			group_pick = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Group Pick")

			group_pick.color_tag = 'INPUT'
			group_pick.description = ""

			
			#group_pick interface
			#Socket Is Valid
			is_valid_socket = group_pick.interface.new_socket(name = "Is Valid", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_valid_socket.default_value = True
			is_valid_socket.attribute_domain = 'POINT'
			is_valid_socket.description = "Whether the pick is valid. Pick is only valid if a single item is picked in the Group ID"
			
			#Socket Index
			index_socket_4 = group_pick.interface.new_socket(name = "Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			index_socket_4.default_value = 0
			index_socket_4.min_value = 0
			index_socket_4.max_value = 2147483647
			index_socket_4.subtype = 'NONE'
			index_socket_4.attribute_domain = 'POINT'
			index_socket_4.description = "Index of picked item. Returns -1 if not a valid pick."
			
			#Socket Pick
			pick_socket = group_pick.interface.new_socket(name = "Pick", in_out='INPUT', socket_type = 'NodeSocketBool')
			pick_socket.default_value = False
			pick_socket.attribute_domain = 'POINT'
			pick_socket.hide_value = True
			pick_socket.description = "True for the item to pick from the group. If number of picks is 0 or more than 1, not a valid pick"
			
			#Socket Group ID
			group_id_socket = group_pick.interface.new_socket(name = "Group ID", in_out='INPUT', socket_type = 'NodeSocketInt')
			group_id_socket.default_value = 0
			group_id_socket.min_value = -2147483648
			group_id_socket.max_value = 2147483647
			group_id_socket.subtype = 'NONE'
			group_id_socket.attribute_domain = 'POINT'
			group_id_socket.description = "Group ID inside which to pick the item"
			
			
			#initialize group_pick nodes
			#node Group Output
			group_output_27 = group_pick.nodes.new("NodeGroupOutput")
			group_output_27.name = "Group Output"
			group_output_27.is_active_output = True
			
			#node Group Input
			group_input_26 = group_pick.nodes.new("NodeGroupInput")
			group_input_26.name = "Group Input"
			
			#node Switch
			switch_4 = group_pick.nodes.new("GeometryNodeSwitch")
			switch_4.name = "Switch"
			switch_4.input_type = 'INT'
			#False
			switch_4.inputs[1].default_value = 0
			
			#node Index
			index_2 = group_pick.nodes.new("GeometryNodeInputIndex")
			index_2.name = "Index"
			
			#node Accumulate Field
			accumulate_field_2 = group_pick.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_2.name = "Accumulate Field"
			accumulate_field_2.data_type = 'INT'
			accumulate_field_2.domain = 'POINT'
			
			#node Accumulate Field.002
			accumulate_field_002 = group_pick.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_002.name = "Accumulate Field.002"
			accumulate_field_002.data_type = 'INT'
			accumulate_field_002.domain = 'POINT'
			
			#node Switch.001
			switch_001_1 = group_pick.nodes.new("GeometryNodeSwitch")
			switch_001_1.name = "Switch.001"
			switch_001_1.input_type = 'INT'
			#False
			switch_001_1.inputs[1].default_value = -1
			
			#node Compare.003
			compare_003 = group_pick.nodes.new("FunctionNodeCompare")
			compare_003.name = "Compare.003"
			compare_003.data_type = 'INT'
			compare_003.mode = 'ELEMENT'
			compare_003.operation = 'EQUAL'
			#B_INT
			compare_003.inputs[3].default_value = 1
			
			#node Reroute.001
			reroute_001_2 = group_pick.nodes.new("NodeReroute")
			reroute_001_2.name = "Reroute.001"
			#node Reroute.002
			reroute_002_2 = group_pick.nodes.new("NodeReroute")
			reroute_002_2.name = "Reroute.002"
			
			
			
			#Set locations
			group_output_27.location = (462.9173889160156, 0.0)
			group_input_26.location = (-472.9173889160156, 0.0)
			switch_4.location = (-120.0, -20.0)
			index_2.location = (-480.0, -120.0)
			accumulate_field_2.location = (60.0, -20.0)
			accumulate_field_002.location = (-120.0, 180.0)
			switch_001_1.location = (240.0, -20.0)
			compare_003.location = (60.0, 180.0)
			reroute_001_2.location = (-260.0, -100.0)
			reroute_002_2.location = (-260.0, -60.0)
			
			#Set dimensions
			group_output_27.width, group_output_27.height = 140.0, 100.0
			group_input_26.width, group_input_26.height = 140.0, 100.0
			switch_4.width, switch_4.height = 140.0, 100.0
			index_2.width, index_2.height = 140.0, 100.0
			accumulate_field_2.width, accumulate_field_2.height = 140.0, 100.0
			accumulate_field_002.width, accumulate_field_002.height = 140.0, 100.0
			switch_001_1.width, switch_001_1.height = 140.0, 100.0
			compare_003.width, compare_003.height = 138.9921875, 100.0
			reroute_001_2.width, reroute_001_2.height = 16.0, 100.0
			reroute_002_2.width, reroute_002_2.height = 16.0, 100.0
			
			#initialize group_pick links
			#switch_4.Output -> accumulate_field_2.Value
			group_pick.links.new(switch_4.outputs[0], accumulate_field_2.inputs[0])
			#compare_003.Result -> switch_001_1.Switch
			group_pick.links.new(compare_003.outputs[0], switch_001_1.inputs[0])
			#accumulate_field_2.Total -> switch_001_1.True
			group_pick.links.new(accumulate_field_2.outputs[2], switch_001_1.inputs[2])
			#reroute_001_2.Output -> accumulate_field_2.Group ID
			group_pick.links.new(reroute_001_2.outputs[0], accumulate_field_2.inputs[1])
			#reroute_001_2.Output -> accumulate_field_002.Group ID
			group_pick.links.new(reroute_001_2.outputs[0], accumulate_field_002.inputs[1])
			#reroute_002_2.Output -> switch_4.Switch
			group_pick.links.new(reroute_002_2.outputs[0], switch_4.inputs[0])
			#reroute_002_2.Output -> accumulate_field_002.Value
			group_pick.links.new(reroute_002_2.outputs[0], accumulate_field_002.inputs[0])
			#index_2.Index -> switch_4.True
			group_pick.links.new(index_2.outputs[0], switch_4.inputs[2])
			#accumulate_field_002.Total -> compare_003.A
			group_pick.links.new(accumulate_field_002.outputs[2], compare_003.inputs[2])
			#group_input_26.Group ID -> reroute_001_2.Input
			group_pick.links.new(group_input_26.outputs[1], reroute_001_2.inputs[0])
			#group_input_26.Pick -> reroute_002_2.Input
			group_pick.links.new(group_input_26.outputs[0], reroute_002_2.inputs[0])
			#switch_001_1.Output -> group_output_27.Index
			group_pick.links.new(switch_001_1.outputs[0], group_output_27.inputs[1])
			#compare_003.Result -> group_output_27.Is Valid
			group_pick.links.new(compare_003.outputs[0], group_output_27.inputs[0])
			return group_pick

		group_pick = group_pick_node_group()

		#initialize group_pick_vector node group
		def group_pick_vector_node_group():
			group_pick_vector = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Group Pick Vector")

			group_pick_vector.color_tag = 'INPUT'
			group_pick_vector.description = ""

			
			#group_pick_vector interface
			#Socket Is Valid
			is_valid_socket_1 = group_pick_vector.interface.new_socket(name = "Is Valid", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_valid_socket_1.default_value = False
			is_valid_socket_1.attribute_domain = 'POINT'
			is_valid_socket_1.description = "The pick for this group is valid"
			
			#Socket Index
			index_socket_5 = group_pick_vector.interface.new_socket(name = "Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			index_socket_5.default_value = 0
			index_socket_5.min_value = -2147483648
			index_socket_5.max_value = 2147483647
			index_socket_5.subtype = 'NONE'
			index_socket_5.attribute_domain = 'POINT'
			index_socket_5.description = "Picked Index for the Group"
			
			#Socket Vector
			vector_socket_2 = group_pick_vector.interface.new_socket(name = "Vector", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			vector_socket_2.default_value = (0.0, 0.0, 0.0)
			vector_socket_2.min_value = -3.4028234663852886e+38
			vector_socket_2.max_value = 3.4028234663852886e+38
			vector_socket_2.subtype = 'NONE'
			vector_socket_2.attribute_domain = 'POINT'
			vector_socket_2.description = "Picked vector for the group"
			
			#Socket Pick
			pick_socket_1 = group_pick_vector.interface.new_socket(name = "Pick", in_out='INPUT', socket_type = 'NodeSocketBool')
			pick_socket_1.default_value = False
			pick_socket_1.attribute_domain = 'POINT'
			pick_socket_1.hide_value = True
			
			#Socket Group ID
			group_id_socket_1 = group_pick_vector.interface.new_socket(name = "Group ID", in_out='INPUT', socket_type = 'NodeSocketInt')
			group_id_socket_1.default_value = 0
			group_id_socket_1.min_value = -2147483648
			group_id_socket_1.max_value = 2147483647
			group_id_socket_1.subtype = 'NONE'
			group_id_socket_1.attribute_domain = 'POINT'
			
			#Socket Position
			position_socket_1 = group_pick_vector.interface.new_socket(name = "Position", in_out='INPUT', socket_type = 'NodeSocketVector')
			position_socket_1.default_value = (0.0, 0.0, 0.0)
			position_socket_1.min_value = -3.4028234663852886e+38
			position_socket_1.max_value = 3.4028234663852886e+38
			position_socket_1.subtype = 'NONE'
			position_socket_1.attribute_domain = 'POINT'
			position_socket_1.description = "Vector field to pick vlaue for, defaults to Position"
			
			
			#initialize group_pick_vector nodes
			#node Group Output
			group_output_28 = group_pick_vector.nodes.new("NodeGroupOutput")
			group_output_28.name = "Group Output"
			group_output_28.is_active_output = True
			
			#node Group Input
			group_input_27 = group_pick_vector.nodes.new("NodeGroupInput")
			group_input_27.name = "Group Input"
			
			#node Evaluate at Index.001
			evaluate_at_index_001_3 = group_pick_vector.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001_3.name = "Evaluate at Index.001"
			evaluate_at_index_001_3.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_001_3.domain = 'POINT'
			
			#node Switch.002
			switch_002_1 = group_pick_vector.nodes.new("GeometryNodeSwitch")
			switch_002_1.name = "Switch.002"
			switch_002_1.input_type = 'VECTOR'
			#False
			switch_002_1.inputs[1].default_value = (0.0, 0.0, 0.0)
			
			#node Group
			group_8 = group_pick_vector.nodes.new("GeometryNodeGroup")
			group_8.name = "Group"
			group_8.node_tree = group_pick
			
			
			
			
			#Set locations
			group_output_28.location = (-40.0, -20.0)
			group_input_27.location = (-740.0, -80.0)
			evaluate_at_index_001_3.location = (-380.0, -180.0)
			switch_002_1.location = (-220.0, -60.0)
			group_8.location = (-560.0, -20.0)
			
			#Set dimensions
			group_output_28.width, group_output_28.height = 140.0, 100.0
			group_input_27.width, group_input_27.height = 140.0, 100.0
			evaluate_at_index_001_3.width, evaluate_at_index_001_3.height = 132.09918212890625, 100.0
			switch_002_1.width, switch_002_1.height = 140.0, 100.0
			group_8.width, group_8.height = 140.0, 100.0
			
			#initialize group_pick_vector links
			#group_8.Is Valid -> switch_002_1.Switch
			group_pick_vector.links.new(group_8.outputs[0], switch_002_1.inputs[0])
			#group_8.Index -> evaluate_at_index_001_3.Index
			group_pick_vector.links.new(group_8.outputs[1], evaluate_at_index_001_3.inputs[0])
			#evaluate_at_index_001_3.Value -> switch_002_1.True
			group_pick_vector.links.new(evaluate_at_index_001_3.outputs[0], switch_002_1.inputs[2])
			#group_8.Index -> group_output_28.Index
			group_pick_vector.links.new(group_8.outputs[1], group_output_28.inputs[1])
			#group_8.Is Valid -> group_output_28.Is Valid
			group_pick_vector.links.new(group_8.outputs[0], group_output_28.inputs[0])
			#switch_002_1.Output -> group_output_28.Vector
			group_pick_vector.links.new(switch_002_1.outputs[0], group_output_28.inputs[2])
			#group_input_27.Group ID -> group_8.Group ID
			group_pick_vector.links.new(group_input_27.outputs[1], group_8.inputs[1])
			#group_input_27.Pick -> group_8.Pick
			group_pick_vector.links.new(group_input_27.outputs[0], group_8.inputs[0])
			#group_input_27.Position -> evaluate_at_index_001_3.Value
			group_pick_vector.links.new(group_input_27.outputs[2], evaluate_at_index_001_3.inputs[1])
			return group_pick_vector

		group_pick_vector = group_pick_vector_node_group()

		#initialize res_group_id node group
		def res_group_id_node_group():
			res_group_id = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Res Group ID")

			res_group_id.color_tag = 'INPUT'
			res_group_id.description = ""

			
			#res_group_id interface
			#Socket Unique Group ID
			unique_group_id_socket = res_group_id.interface.new_socket(name = "Unique Group ID", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			unique_group_id_socket.default_value = 0
			unique_group_id_socket.min_value = -2147483648
			unique_group_id_socket.max_value = 2147483647
			unique_group_id_socket.subtype = 'NONE'
			unique_group_id_socket.attribute_domain = 'POINT'
			unique_group_id_socket.description = "A unique Group ID for eash residue"
			
			
			#initialize res_group_id nodes
			#node Group Output
			group_output_29 = res_group_id.nodes.new("NodeGroupOutput")
			group_output_29.name = "Group Output"
			group_output_29.is_active_output = True
			
			#node Group Input
			group_input_28 = res_group_id.nodes.new("NodeGroupInput")
			group_input_28.name = "Group Input"
			
			#node Named Attribute.001
			named_attribute_001_2 = res_group_id.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001_2.name = "Named Attribute.001"
			named_attribute_001_2.data_type = 'INT'
			#Name
			named_attribute_001_2.inputs[0].default_value = "res_id"
			
			#node Named Attribute.002
			named_attribute_002_2 = res_group_id.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002_2.name = "Named Attribute.002"
			named_attribute_002_2.data_type = 'INT'
			#Name
			named_attribute_002_2.inputs[0].default_value = "atom_name"
			
			#node Compare.002
			compare_002_1 = res_group_id.nodes.new("FunctionNodeCompare")
			compare_002_1.name = "Compare.002"
			compare_002_1.data_type = 'INT'
			compare_002_1.mode = 'ELEMENT'
			compare_002_1.operation = 'EQUAL'
			#B_INT
			compare_002_1.inputs[3].default_value = 1
			
			#node Compare.001
			compare_001_5 = res_group_id.nodes.new("FunctionNodeCompare")
			compare_001_5.name = "Compare.001"
			compare_001_5.data_type = 'INT'
			compare_001_5.mode = 'ELEMENT'
			compare_001_5.operation = 'NOT_EQUAL'
			
			#node Boolean Math
			boolean_math_6 = res_group_id.nodes.new("FunctionNodeBooleanMath")
			boolean_math_6.name = "Boolean Math"
			boolean_math_6.operation = 'OR'
			
			#node Accumulate Field.001
			accumulate_field_001_2 = res_group_id.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_001_2.name = "Accumulate Field.001"
			accumulate_field_001_2.data_type = 'INT'
			accumulate_field_001_2.domain = 'POINT'
			#Group Index
			accumulate_field_001_2.inputs[1].default_value = 0
			
			#node Group.001
			group_001_5 = res_group_id.nodes.new("GeometryNodeGroup")
			group_001_5.name = "Group.001"
			group_001_5.node_tree = offset_integer
			#Socket_1
			group_001_5.inputs[0].default_value = 0
			#Socket_2
			group_001_5.inputs[2].default_value = -1
			
			#node Math
			math_13 = res_group_id.nodes.new("ShaderNodeMath")
			math_13.name = "Math"
			math_13.operation = 'SUBTRACT'
			math_13.use_clamp = False
			#Value_001
			math_13.inputs[1].default_value = 1.0
			
			#node Frame
			frame_9 = res_group_id.nodes.new("NodeFrame")
			frame_9.name = "Frame"
			frame_9.label_size = 20
			frame_9.shrink = True
			
			#node Reroute
			reroute_6 = res_group_id.nodes.new("NodeReroute")
			reroute_6.label = "subtracting 1 from the leading, but things don't work right"
			reroute_6.name = "Reroute"
			#node Reroute.001
			reroute_001_3 = res_group_id.nodes.new("NodeReroute")
			reroute_001_3.name = "Reroute.001"
			#node Reroute.002
			reroute_002_3 = res_group_id.nodes.new("NodeReroute")
			reroute_002_3.label = "In theory we can just use the trailing value instead of"
			reroute_002_3.name = "Reroute.002"
			#node Reroute.003
			reroute_003_1 = res_group_id.nodes.new("NodeReroute")
			reroute_003_1.name = "Reroute.003"
			
			
			#Set parents
			math_13.parent = frame_9
			reroute_6.parent = frame_9
			reroute_001_3.parent = frame_9
			reroute_002_3.parent = frame_9
			reroute_003_1.parent = frame_9
			
			#Set locations
			group_output_29.location = (900.0, 160.0)
			group_input_28.location = (-420.0, 160.0)
			named_attribute_001_2.location = (-240.0, 0.0)
			named_attribute_002_2.location = (-250.0, 160.0)
			compare_002_1.location = (-70.0, 160.0)
			compare_001_5.location = (-70.0, 0.0)
			boolean_math_6.location = (90.0, 160.0)
			accumulate_field_001_2.location = (250.0, 160.0)
			group_001_5.location = (-70.0, -160.0)
			math_13.location = (519.2361450195312, 166.28671264648438)
			frame_9.location = (95.0, -20.0)
			reroute_6.location = (554.4125366210938, 257.9646911621094)
			reroute_001_3.location = (739.2361450195312, 306.2867126464844)
			reroute_002_3.location = (551.13134765625, 297.3444519042969)
			reroute_003_1.location = (379.23614501953125, 306.2867126464844)
			
			#Set dimensions
			group_output_29.width, group_output_29.height = 140.0, 100.0
			group_input_28.width, group_input_28.height = 140.0, 100.0
			named_attribute_001_2.width, named_attribute_001_2.height = 140.0, 100.0
			named_attribute_002_2.width, named_attribute_002_2.height = 140.0, 100.0
			compare_002_1.width, compare_002_1.height = 140.0, 100.0
			compare_001_5.width, compare_001_5.height = 140.0, 100.0
			boolean_math_6.width, boolean_math_6.height = 140.0, 100.0
			accumulate_field_001_2.width, accumulate_field_001_2.height = 140.0, 100.0
			group_001_5.width, group_001_5.height = 140.0, 100.0
			math_13.width, math_13.height = 140.0, 100.0
			frame_9.width, frame_9.height = 436.0, 356.2867126464844
			reroute_6.width, reroute_6.height = 16.0, 100.0
			reroute_001_3.width, reroute_001_3.height = 16.0, 100.0
			reroute_002_3.width, reroute_002_3.height = 16.0, 100.0
			reroute_003_1.width, reroute_003_1.height = 16.0, 100.0
			
			#initialize res_group_id links
			#compare_002_1.Result -> boolean_math_6.Boolean
			res_group_id.links.new(compare_002_1.outputs[0], boolean_math_6.inputs[0])
			#named_attribute_001_2.Attribute -> compare_001_5.A
			res_group_id.links.new(named_attribute_001_2.outputs[0], compare_001_5.inputs[2])
			#named_attribute_001_2.Attribute -> group_001_5.Value
			res_group_id.links.new(named_attribute_001_2.outputs[0], group_001_5.inputs[1])
			#compare_001_5.Result -> boolean_math_6.Boolean
			res_group_id.links.new(compare_001_5.outputs[0], boolean_math_6.inputs[1])
			#named_attribute_002_2.Attribute -> compare_002_1.A
			res_group_id.links.new(named_attribute_002_2.outputs[0], compare_002_1.inputs[2])
			#group_001_5.Value -> compare_001_5.B
			res_group_id.links.new(group_001_5.outputs[0], compare_001_5.inputs[3])
			#accumulate_field_001_2.Leading -> math_13.Value
			res_group_id.links.new(accumulate_field_001_2.outputs[0], math_13.inputs[0])
			#math_13.Value -> group_output_29.Unique Group ID
			res_group_id.links.new(math_13.outputs[0], group_output_29.inputs[0])
			#boolean_math_6.Boolean -> accumulate_field_001_2.Value
			res_group_id.links.new(boolean_math_6.outputs[0], accumulate_field_001_2.inputs[0])
			return res_group_id

		res_group_id = res_group_id_node_group()

		#initialize residue_mask node group
		def residue_mask_node_group():
			residue_mask = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Residue Mask")

			residue_mask.color_tag = 'INPUT'
			residue_mask.description = ""

			
			#residue_mask interface
			#Socket Is Valid
			is_valid_socket_2 = residue_mask.interface.new_socket(name = "Is Valid", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_valid_socket_2.default_value = False
			is_valid_socket_2.attribute_domain = 'POINT'
			is_valid_socket_2.description = "Group contains only one occurrance of the selected atom. None or more than one returns False"
			
			#Socket Index
			index_socket_6 = residue_mask.interface.new_socket(name = "Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			index_socket_6.default_value = 0
			index_socket_6.min_value = -2147483648
			index_socket_6.max_value = 2147483647
			index_socket_6.subtype = 'NONE'
			index_socket_6.attribute_domain = 'POINT'
			index_socket_6.description = "Index for the group's atom with specified name, returns -1 if not valid"
			
			#Socket Position
			position_socket_2 = residue_mask.interface.new_socket(name = "Position", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			position_socket_2.default_value = (0.0, 0.0, 0.0)
			position_socket_2.min_value = -3.4028234663852886e+38
			position_socket_2.max_value = 3.4028234663852886e+38
			position_socket_2.subtype = 'NONE'
			position_socket_2.attribute_domain = 'POINT'
			position_socket_2.description = "Position of the picked point in the group, returns (0, 0, 0) if not valid"
			
			#Socket Group ID
			group_id_socket_2 = residue_mask.interface.new_socket(name = "Group ID", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			group_id_socket_2.default_value = 0
			group_id_socket_2.min_value = -2147483648
			group_id_socket_2.max_value = 2147483647
			group_id_socket_2.subtype = 'NONE'
			group_id_socket_2.attribute_domain = 'POINT'
			
			#Socket atom_name
			atom_name_socket = residue_mask.interface.new_socket(name = "atom_name", in_out='INPUT', socket_type = 'NodeSocketInt')
			atom_name_socket.default_value = 1
			atom_name_socket.min_value = 2
			atom_name_socket.max_value = 2147483647
			atom_name_socket.subtype = 'NONE'
			atom_name_socket.attribute_domain = 'POINT'
			atom_name_socket.description = "Atom to pick from the group"
			
			#Socket Use Fallback
			use_fallback_socket = residue_mask.interface.new_socket(name = "Use Fallback", in_out='INPUT', socket_type = 'NodeSocketBool')
			use_fallback_socket.default_value = True
			use_fallback_socket.attribute_domain = 'POINT'
			use_fallback_socket.description = "Uses a calculated Unique Group ID as a fallback. Disabling can increase performance if pre-computing a Group ID for multiple nodes"
			
			#Socket Group ID
			group_id_socket_3 = residue_mask.interface.new_socket(name = "Group ID", in_out='INPUT', socket_type = 'NodeSocketInt')
			group_id_socket_3.default_value = 0
			group_id_socket_3.min_value = -2147483648
			group_id_socket_3.max_value = 2147483647
			group_id_socket_3.subtype = 'NONE'
			group_id_socket_3.attribute_domain = 'POINT'
			
			
			#initialize residue_mask nodes
			#node Compare
			compare_6 = residue_mask.nodes.new("FunctionNodeCompare")
			compare_6.name = "Compare"
			compare_6.data_type = 'INT'
			compare_6.mode = 'ELEMENT'
			compare_6.operation = 'EQUAL'
			
			#node Group Input
			group_input_29 = residue_mask.nodes.new("NodeGroupInput")
			group_input_29.name = "Group Input"
			
			#node Named Attribute
			named_attribute_1 = residue_mask.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_1.name = "Named Attribute"
			named_attribute_1.data_type = 'INT'
			#Name
			named_attribute_1.inputs[0].default_value = "atom_name"
			
			#node Group Output
			group_output_30 = residue_mask.nodes.new("NodeGroupOutput")
			group_output_30.name = "Group Output"
			group_output_30.is_active_output = True
			
			#node Group
			group_9 = residue_mask.nodes.new("GeometryNodeGroup")
			group_9.name = "Group"
			group_9.node_tree = group_pick_vector
			#Socket_5
			group_9.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Group.002
			group_002_5 = residue_mask.nodes.new("GeometryNodeGroup")
			group_002_5.name = "Group.002"
			group_002_5.node_tree = res_group_id
			
			#node Switch
			switch_5 = residue_mask.nodes.new("GeometryNodeSwitch")
			switch_5.name = "Switch"
			switch_5.input_type = 'INT'
			
			
			
			
			#Set locations
			compare_6.location = (40.0, 340.0)
			group_input_29.location = (-140.0, 200.0)
			named_attribute_1.location = (-140.0, 340.0)
			group_output_30.location = (420.0, 340.0)
			group_9.location = (220.0, 340.0)
			group_002_5.location = (-140.0, 60.0)
			switch_5.location = (40.0, 180.0)
			
			#Set dimensions
			compare_6.width, compare_6.height = 140.0, 100.0
			group_input_29.width, group_input_29.height = 140.0, 100.0
			named_attribute_1.width, named_attribute_1.height = 140.0, 100.0
			group_output_30.width, group_output_30.height = 140.0, 100.0
			group_9.width, group_9.height = 164.60528564453125, 100.0
			group_002_5.width, group_002_5.height = 140.0, 100.0
			switch_5.width, switch_5.height = 140.0, 100.0
			
			#initialize residue_mask links
			#named_attribute_1.Attribute -> compare_6.A
			residue_mask.links.new(named_attribute_1.outputs[0], compare_6.inputs[2])
			#group_input_29.atom_name -> compare_6.B
			residue_mask.links.new(group_input_29.outputs[0], compare_6.inputs[3])
			#group_9.Index -> group_output_30.Index
			residue_mask.links.new(group_9.outputs[1], group_output_30.inputs[1])
			#group_9.Vector -> group_output_30.Position
			residue_mask.links.new(group_9.outputs[2], group_output_30.inputs[2])
			#group_9.Is Valid -> group_output_30.Is Valid
			residue_mask.links.new(group_9.outputs[0], group_output_30.inputs[0])
			#compare_6.Result -> group_9.Pick
			residue_mask.links.new(compare_6.outputs[0], group_9.inputs[0])
			#group_input_29.Use Fallback -> switch_5.Switch
			residue_mask.links.new(group_input_29.outputs[1], switch_5.inputs[0])
			#group_input_29.Group ID -> switch_5.False
			residue_mask.links.new(group_input_29.outputs[2], switch_5.inputs[1])
			#switch_5.Output -> group_9.Group ID
			residue_mask.links.new(switch_5.outputs[0], group_9.inputs[1])
			#group_002_5.Unique Group ID -> switch_5.True
			residue_mask.links.new(group_002_5.outputs[0], switch_5.inputs[2])
			#switch_5.Output -> group_output_30.Group ID
			residue_mask.links.new(switch_5.outputs[0], group_output_30.inputs[3])
			return residue_mask

		residue_mask = residue_mask_node_group()

		#initialize fallback_boolean node group
		def fallback_boolean_node_group():
			fallback_boolean = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Fallback Boolean")

			fallback_boolean.color_tag = 'INPUT'
			fallback_boolean.description = "Computes the boolean field if the given attribute doesn't exist. If it doesn't exist it just uses the attribute instead"

			
			#fallback_boolean interface
			#Socket Boolean
			boolean_socket_13 = fallback_boolean.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket_13.default_value = False
			boolean_socket_13.attribute_domain = 'POINT'
			
			#Socket Name
			name_socket = fallback_boolean.interface.new_socket(name = "Name", in_out='INPUT', socket_type = 'NodeSocketString')
			name_socket.default_value = ""
			name_socket.attribute_domain = 'POINT'
			
			#Socket Fallback
			fallback_socket = fallback_boolean.interface.new_socket(name = "Fallback", in_out='INPUT', socket_type = 'NodeSocketBool')
			fallback_socket.default_value = False
			fallback_socket.attribute_domain = 'POINT'
			
			
			#initialize fallback_boolean nodes
			#node Group Output
			group_output_31 = fallback_boolean.nodes.new("NodeGroupOutput")
			group_output_31.name = "Group Output"
			group_output_31.is_active_output = True
			
			#node Group Input
			group_input_30 = fallback_boolean.nodes.new("NodeGroupInput")
			group_input_30.name = "Group Input"
			
			#node Named Attribute
			named_attribute_2 = fallback_boolean.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_2.name = "Named Attribute"
			named_attribute_2.data_type = 'BOOLEAN'
			
			#node Switch
			switch_6 = fallback_boolean.nodes.new("GeometryNodeSwitch")
			switch_6.name = "Switch"
			switch_6.input_type = 'BOOLEAN'
			
			
			
			
			#Set locations
			group_output_31.location = (276.6171569824219, 4.738137245178223)
			group_input_30.location = (-280.0, 0.0)
			named_attribute_2.location = (-94.73597717285156, 4.738137245178223)
			switch_6.location = (86.61715698242188, 4.738137245178223)
			
			#Set dimensions
			group_output_31.width, group_output_31.height = 140.0, 100.0
			group_input_30.width, group_input_30.height = 140.0, 100.0
			named_attribute_2.width, named_attribute_2.height = 140.0, 100.0
			switch_6.width, switch_6.height = 140.0, 100.0
			
			#initialize fallback_boolean links
			#named_attribute_2.Exists -> switch_6.Switch
			fallback_boolean.links.new(named_attribute_2.outputs[1], switch_6.inputs[0])
			#named_attribute_2.Attribute -> switch_6.True
			fallback_boolean.links.new(named_attribute_2.outputs[0], switch_6.inputs[2])
			#group_input_30.Fallback -> switch_6.False
			fallback_boolean.links.new(group_input_30.outputs[1], switch_6.inputs[1])
			#switch_6.Output -> group_output_31.Boolean
			fallback_boolean.links.new(switch_6.outputs[0], group_output_31.inputs[0])
			#group_input_30.Name -> named_attribute_2.Name
			fallback_boolean.links.new(group_input_30.outputs[0], named_attribute_2.inputs[0])
			return fallback_boolean

		fallback_boolean = fallback_boolean_node_group()

		#initialize _mn_constants_atom_name_peptide node group
		def _mn_constants_atom_name_peptide_node_group():
			_mn_constants_atom_name_peptide = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_constants_atom_name_peptide")

			_mn_constants_atom_name_peptide.color_tag = 'NONE'
			_mn_constants_atom_name_peptide.description = ""

			
			#_mn_constants_atom_name_peptide interface
			#Socket Backbone Lower
			backbone_lower_socket = _mn_constants_atom_name_peptide.interface.new_socket(name = "Backbone Lower", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			backbone_lower_socket.default_value = 0
			backbone_lower_socket.min_value = -2147483648
			backbone_lower_socket.max_value = 2147483647
			backbone_lower_socket.subtype = 'NONE'
			backbone_lower_socket.attribute_domain = 'POINT'
			
			#Socket Backbone Upper
			backbone_upper_socket = _mn_constants_atom_name_peptide.interface.new_socket(name = "Backbone Upper", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			backbone_upper_socket.default_value = 0
			backbone_upper_socket.min_value = -2147483648
			backbone_upper_socket.max_value = 2147483647
			backbone_upper_socket.subtype = 'NONE'
			backbone_upper_socket.attribute_domain = 'POINT'
			
			#Socket Side Chain Lower
			side_chain_lower_socket = _mn_constants_atom_name_peptide.interface.new_socket(name = "Side Chain Lower", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			side_chain_lower_socket.default_value = 0
			side_chain_lower_socket.min_value = -2147483648
			side_chain_lower_socket.max_value = 2147483647
			side_chain_lower_socket.subtype = 'NONE'
			side_chain_lower_socket.attribute_domain = 'POINT'
			
			#Socket Side Chain Upper
			side_chain_upper_socket = _mn_constants_atom_name_peptide.interface.new_socket(name = "Side Chain Upper", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			side_chain_upper_socket.default_value = 0
			side_chain_upper_socket.min_value = -2147483648
			side_chain_upper_socket.max_value = 2147483647
			side_chain_upper_socket.subtype = 'NONE'
			side_chain_upper_socket.attribute_domain = 'POINT'
			
			#Socket Alpha Carbon
			alpha_carbon_socket = _mn_constants_atom_name_peptide.interface.new_socket(name = "Alpha Carbon", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			alpha_carbon_socket.default_value = 0
			alpha_carbon_socket.min_value = -2147483648
			alpha_carbon_socket.max_value = 2147483647
			alpha_carbon_socket.subtype = 'NONE'
			alpha_carbon_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_constants_atom_name_peptide nodes
			#node Group Input
			group_input_31 = _mn_constants_atom_name_peptide.nodes.new("NodeGroupInput")
			group_input_31.name = "Group Input"
			
			#node Group Output
			group_output_32 = _mn_constants_atom_name_peptide.nodes.new("NodeGroupOutput")
			group_output_32.name = "Group Output"
			group_output_32.is_active_output = True
			
			#node Integer.001
			integer_001 = _mn_constants_atom_name_peptide.nodes.new("FunctionNodeInputInt")
			integer_001.name = "Integer.001"
			integer_001.integer = 49
			
			#node Integer.004
			integer_004 = _mn_constants_atom_name_peptide.nodes.new("FunctionNodeInputInt")
			integer_004.name = "Integer.004"
			integer_004.integer = 2
			
			#node Integer
			integer_2 = _mn_constants_atom_name_peptide.nodes.new("FunctionNodeInputInt")
			integer_2.name = "Integer"
			integer_2.integer = 5
			
			#node Integer.003
			integer_003 = _mn_constants_atom_name_peptide.nodes.new("FunctionNodeInputInt")
			integer_003.name = "Integer.003"
			integer_003.integer = 1
			
			#node Integer.002
			integer_002 = _mn_constants_atom_name_peptide.nodes.new("FunctionNodeInputInt")
			integer_002.name = "Integer.002"
			integer_002.integer = 4
			
			
			
			
			#Set locations
			group_input_31.location = (-200.0, 0.0)
			group_output_32.location = (260.0, 180.0)
			integer_001.location = (0.0, -50.0)
			integer_004.location = (0.0, -140.0)
			integer_2.location = (0.0, 40.0)
			integer_003.location = (0.0, 240.0)
			integer_002.location = (0.0, 140.0)
			
			#Set dimensions
			group_input_31.width, group_input_31.height = 140.0, 100.0
			group_output_32.width, group_output_32.height = 140.0, 100.0
			integer_001.width, integer_001.height = 140.0, 100.0
			integer_004.width, integer_004.height = 140.0, 100.0
			integer_2.width, integer_2.height = 140.0, 100.0
			integer_003.width, integer_003.height = 140.0, 100.0
			integer_002.width, integer_002.height = 140.0, 100.0
			
			#initialize _mn_constants_atom_name_peptide links
			#integer_003.Integer -> group_output_32.Backbone Lower
			_mn_constants_atom_name_peptide.links.new(integer_003.outputs[0], group_output_32.inputs[0])
			#integer_002.Integer -> group_output_32.Backbone Upper
			_mn_constants_atom_name_peptide.links.new(integer_002.outputs[0], group_output_32.inputs[1])
			#integer_2.Integer -> group_output_32.Side Chain Lower
			_mn_constants_atom_name_peptide.links.new(integer_2.outputs[0], group_output_32.inputs[2])
			#integer_001.Integer -> group_output_32.Side Chain Upper
			_mn_constants_atom_name_peptide.links.new(integer_001.outputs[0], group_output_32.inputs[3])
			#integer_004.Integer -> group_output_32.Alpha Carbon
			_mn_constants_atom_name_peptide.links.new(integer_004.outputs[0], group_output_32.inputs[4])
			return _mn_constants_atom_name_peptide

		_mn_constants_atom_name_peptide = _mn_constants_atom_name_peptide_node_group()

		#initialize _mn_select_peptide node group
		def _mn_select_peptide_node_group():
			_mn_select_peptide = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_select_peptide")

			_mn_select_peptide.color_tag = 'NONE'
			_mn_select_peptide.description = ""

			
			#_mn_select_peptide interface
			#Socket Is Backbone
			is_backbone_socket = _mn_select_peptide.interface.new_socket(name = "Is Backbone", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_backbone_socket.default_value = False
			is_backbone_socket.attribute_domain = 'POINT'
			
			#Socket Is Side Chain
			is_side_chain_socket = _mn_select_peptide.interface.new_socket(name = "Is Side Chain", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_side_chain_socket.default_value = False
			is_side_chain_socket.attribute_domain = 'POINT'
			
			#Socket Is Peptide
			is_peptide_socket = _mn_select_peptide.interface.new_socket(name = "Is Peptide", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_peptide_socket.default_value = False
			is_peptide_socket.attribute_domain = 'POINT'
			
			#Socket Is Alpha Carbon
			is_alpha_carbon_socket = _mn_select_peptide.interface.new_socket(name = "Is Alpha Carbon", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_alpha_carbon_socket.default_value = False
			is_alpha_carbon_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_select_peptide nodes
			#node Group Input
			group_input_32 = _mn_select_peptide.nodes.new("NodeGroupInput")
			group_input_32.name = "Group Input"
			
			#node Compare
			compare_7 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
			compare_7.name = "Compare"
			compare_7.data_type = 'INT'
			compare_7.mode = 'ELEMENT'
			compare_7.operation = 'GREATER_EQUAL'
			
			#node Compare.001
			compare_001_6 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
			compare_001_6.name = "Compare.001"
			compare_001_6.data_type = 'INT'
			compare_001_6.mode = 'ELEMENT'
			compare_001_6.operation = 'LESS_EQUAL'
			
			#node Boolean Math.001
			boolean_math_001_4 = _mn_select_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_4.name = "Boolean Math.001"
			boolean_math_001_4.operation = 'AND'
			
			#node Compare.002
			compare_002_2 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
			compare_002_2.name = "Compare.002"
			compare_002_2.data_type = 'INT'
			compare_002_2.mode = 'ELEMENT'
			compare_002_2.operation = 'GREATER_EQUAL'
			
			#node Compare.003
			compare_003_1 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
			compare_003_1.name = "Compare.003"
			compare_003_1.data_type = 'INT'
			compare_003_1.mode = 'ELEMENT'
			compare_003_1.operation = 'LESS_EQUAL'
			
			#node Boolean Math.002
			boolean_math_002_4 = _mn_select_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_4.name = "Boolean Math.002"
			boolean_math_002_4.operation = 'AND'
			
			#node Compare.004
			compare_004 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
			compare_004.name = "Compare.004"
			compare_004.data_type = 'INT'
			compare_004.mode = 'ELEMENT'
			compare_004.operation = 'GREATER_EQUAL'
			
			#node Named Attribute
			named_attribute_3 = _mn_select_peptide.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_3.name = "Named Attribute"
			named_attribute_3.data_type = 'INT'
			#Name
			named_attribute_3.inputs[0].default_value = "atom_name"
			
			#node Boolean Math.003
			boolean_math_003_7 = _mn_select_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003_7.name = "Boolean Math.003"
			boolean_math_003_7.operation = 'AND'
			
			#node Group Output
			group_output_33 = _mn_select_peptide.nodes.new("NodeGroupOutput")
			group_output_33.name = "Group Output"
			group_output_33.is_active_output = True
			
			#node Compare.005
			compare_005 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
			compare_005.name = "Compare.005"
			compare_005.data_type = 'INT'
			compare_005.mode = 'ELEMENT'
			compare_005.operation = 'LESS_EQUAL'
			
			#node Compare.006
			compare_006 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
			compare_006.name = "Compare.006"
			compare_006.data_type = 'INT'
			compare_006.mode = 'ELEMENT'
			compare_006.operation = 'EQUAL'
			
			#node Group
			group_10 = _mn_select_peptide.nodes.new("GeometryNodeGroup")
			group_10.name = "Group"
			group_10.node_tree = _mn_constants_atom_name_peptide
			
			#node Boolean Math
			boolean_math_7 = _mn_select_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math_7.name = "Boolean Math"
			boolean_math_7.operation = 'OR'
			
			
			
			
			#Set locations
			group_input_32.location = (-460.0, 0.0)
			compare_7.location = (80.0, 80.0)
			compare_001_6.location = (80.0, -80.0)
			boolean_math_001_4.location = (260.0, 80.0)
			compare_002_2.location = (80.0, -240.0)
			compare_003_1.location = (80.0, -400.0)
			boolean_math_002_4.location = (260.0, -240.0)
			compare_004.location = (80.0, -560.0)
			named_attribute_3.location = (-360.0, -480.0)
			boolean_math_003_7.location = (260.0, -560.0)
			group_output_33.location = (666.1161499023438, -263.7054748535156)
			compare_005.location = (80.0, -720.0)
			compare_006.location = (260.0, -380.0)
			group_10.location = (-411.24090576171875, -312.71807861328125)
			boolean_math_7.location = (420.0, -240.0)
			
			#Set dimensions
			group_input_32.width, group_input_32.height = 140.0, 100.0
			compare_7.width, compare_7.height = 140.0, 100.0
			compare_001_6.width, compare_001_6.height = 140.0, 100.0
			boolean_math_001_4.width, boolean_math_001_4.height = 140.0, 100.0
			compare_002_2.width, compare_002_2.height = 153.86517333984375, 100.0
			compare_003_1.width, compare_003_1.height = 153.86517333984375, 100.0
			boolean_math_002_4.width, boolean_math_002_4.height = 140.0, 100.0
			compare_004.width, compare_004.height = 140.0, 100.0
			named_attribute_3.width, named_attribute_3.height = 140.0, 100.0
			boolean_math_003_7.width, boolean_math_003_7.height = 140.0, 100.0
			group_output_33.width, group_output_33.height = 140.0, 100.0
			compare_005.width, compare_005.height = 140.0, 100.0
			compare_006.width, compare_006.height = 140.0, 100.0
			group_10.width, group_10.height = 369.1165771484375, 100.0
			boolean_math_7.width, boolean_math_7.height = 140.0, 100.0
			
			#initialize _mn_select_peptide links
			#compare_001_6.Result -> boolean_math_001_4.Boolean
			_mn_select_peptide.links.new(compare_001_6.outputs[0], boolean_math_001_4.inputs[1])
			#group_10.Backbone Lower -> compare_7.B
			_mn_select_peptide.links.new(group_10.outputs[0], compare_7.inputs[3])
			#named_attribute_3.Attribute -> compare_7.A
			_mn_select_peptide.links.new(named_attribute_3.outputs[0], compare_7.inputs[2])
			#compare_7.Result -> boolean_math_001_4.Boolean
			_mn_select_peptide.links.new(compare_7.outputs[0], boolean_math_001_4.inputs[0])
			#named_attribute_3.Attribute -> compare_001_6.A
			_mn_select_peptide.links.new(named_attribute_3.outputs[0], compare_001_6.inputs[2])
			#group_10.Backbone Upper -> compare_001_6.B
			_mn_select_peptide.links.new(group_10.outputs[1], compare_001_6.inputs[3])
			#boolean_math_001_4.Boolean -> group_output_33.Is Backbone
			_mn_select_peptide.links.new(boolean_math_001_4.outputs[0], group_output_33.inputs[0])
			#compare_003_1.Result -> boolean_math_002_4.Boolean
			_mn_select_peptide.links.new(compare_003_1.outputs[0], boolean_math_002_4.inputs[1])
			#named_attribute_3.Attribute -> compare_002_2.A
			_mn_select_peptide.links.new(named_attribute_3.outputs[0], compare_002_2.inputs[2])
			#compare_002_2.Result -> boolean_math_002_4.Boolean
			_mn_select_peptide.links.new(compare_002_2.outputs[0], boolean_math_002_4.inputs[0])
			#named_attribute_3.Attribute -> compare_003_1.A
			_mn_select_peptide.links.new(named_attribute_3.outputs[0], compare_003_1.inputs[2])
			#group_10.Side Chain Lower -> compare_002_2.B
			_mn_select_peptide.links.new(group_10.outputs[2], compare_002_2.inputs[3])
			#group_10.Side Chain Upper -> compare_003_1.B
			_mn_select_peptide.links.new(group_10.outputs[3], compare_003_1.inputs[3])
			#compare_005.Result -> boolean_math_003_7.Boolean
			_mn_select_peptide.links.new(compare_005.outputs[0], boolean_math_003_7.inputs[1])
			#named_attribute_3.Attribute -> compare_004.A
			_mn_select_peptide.links.new(named_attribute_3.outputs[0], compare_004.inputs[2])
			#compare_004.Result -> boolean_math_003_7.Boolean
			_mn_select_peptide.links.new(compare_004.outputs[0], boolean_math_003_7.inputs[0])
			#named_attribute_3.Attribute -> compare_005.A
			_mn_select_peptide.links.new(named_attribute_3.outputs[0], compare_005.inputs[2])
			#group_10.Backbone Lower -> compare_004.B
			_mn_select_peptide.links.new(group_10.outputs[0], compare_004.inputs[3])
			#group_10.Side Chain Upper -> compare_005.B
			_mn_select_peptide.links.new(group_10.outputs[3], compare_005.inputs[3])
			#boolean_math_003_7.Boolean -> group_output_33.Is Peptide
			_mn_select_peptide.links.new(boolean_math_003_7.outputs[0], group_output_33.inputs[2])
			#named_attribute_3.Attribute -> compare_006.A
			_mn_select_peptide.links.new(named_attribute_3.outputs[0], compare_006.inputs[2])
			#group_10.Alpha Carbon -> compare_006.B
			_mn_select_peptide.links.new(group_10.outputs[4], compare_006.inputs[3])
			#compare_006.Result -> group_output_33.Is Alpha Carbon
			_mn_select_peptide.links.new(compare_006.outputs[0], group_output_33.inputs[3])
			#boolean_math_002_4.Boolean -> boolean_math_7.Boolean
			_mn_select_peptide.links.new(boolean_math_002_4.outputs[0], boolean_math_7.inputs[0])
			#compare_006.Result -> boolean_math_7.Boolean
			_mn_select_peptide.links.new(compare_006.outputs[0], boolean_math_7.inputs[1])
			#boolean_math_7.Boolean -> group_output_33.Is Side Chain
			_mn_select_peptide.links.new(boolean_math_7.outputs[0], group_output_33.inputs[1])
			return _mn_select_peptide

		_mn_select_peptide = _mn_select_peptide_node_group()

		#initialize is_alpha_carbon node group
		def is_alpha_carbon_node_group():
			is_alpha_carbon = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Is Alpha Carbon")

			is_alpha_carbon.color_tag = 'INPUT'
			is_alpha_carbon.description = ""

			
			#is_alpha_carbon interface
			#Socket Selection
			selection_socket = is_alpha_carbon.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket.default_value = False
			selection_socket.attribute_domain = 'POINT'
			selection_socket.description = "True if atom is an alpha carbon of an amino acid"
			
			#Socket Inverted
			inverted_socket = is_alpha_carbon.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket.default_value = False
			inverted_socket.attribute_domain = 'POINT'
			
			#Socket And
			and_socket = is_alpha_carbon.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket.default_value = True
			and_socket.attribute_domain = 'POINT'
			and_socket.hide_value = True
			
			#Socket Or
			or_socket = is_alpha_carbon.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket.default_value = False
			or_socket.attribute_domain = 'POINT'
			or_socket.hide_value = True
			
			
			#initialize is_alpha_carbon nodes
			#node Group Output
			group_output_34 = is_alpha_carbon.nodes.new("NodeGroupOutput")
			group_output_34.name = "Group Output"
			group_output_34.is_active_output = True
			
			#node Group Input
			group_input_33 = is_alpha_carbon.nodes.new("NodeGroupInput")
			group_input_33.name = "Group Input"
			
			#node Boolean Math.001
			boolean_math_001_5 = is_alpha_carbon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_5.name = "Boolean Math.001"
			boolean_math_001_5.operation = 'AND'
			
			#node Group.001
			group_001_6 = is_alpha_carbon.nodes.new("GeometryNodeGroup")
			group_001_6.name = "Group.001"
			group_001_6.node_tree = fallback_boolean
			#Socket_2
			group_001_6.inputs[0].default_value = "is_alpha_carbon"
			
			#node Group.002
			group_002_6 = is_alpha_carbon.nodes.new("GeometryNodeGroup")
			group_002_6.name = "Group.002"
			group_002_6.node_tree = _mn_select_peptide
			group_002_6.outputs[0].hide = True
			group_002_6.outputs[1].hide = True
			group_002_6.outputs[2].hide = True
			
			#node Boolean Math.002
			boolean_math_002_5 = is_alpha_carbon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_5.name = "Boolean Math.002"
			boolean_math_002_5.operation = 'OR'
			
			#node Boolean Math
			boolean_math_8 = is_alpha_carbon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_8.name = "Boolean Math"
			boolean_math_8.operation = 'NOT'
			
			
			
			
			#Set locations
			group_output_34.location = (520.0, 0.0)
			group_input_33.location = (-200.0, 0.0)
			boolean_math_001_5.location = (160.0, 0.0)
			group_001_6.location = (-88.33343505859375, -180.0)
			group_002_6.location = (-290.4490661621094, -180.0)
			boolean_math_002_5.location = (340.0, 0.0)
			boolean_math_8.location = (340.0, -140.0)
			
			#Set dimensions
			group_output_34.width, group_output_34.height = 140.0, 100.0
			group_input_33.width, group_input_33.height = 140.0, 100.0
			boolean_math_001_5.width, boolean_math_001_5.height = 140.0, 100.0
			group_001_6.width, group_001_6.height = 208.33343505859375, 100.0
			group_002_6.width, group_002_6.height = 170.44906616210938, 100.0
			boolean_math_002_5.width, boolean_math_002_5.height = 140.0, 100.0
			boolean_math_8.width, boolean_math_8.height = 140.0, 100.0
			
			#initialize is_alpha_carbon links
			#group_input_33.And -> boolean_math_001_5.Boolean
			is_alpha_carbon.links.new(group_input_33.outputs[0], boolean_math_001_5.inputs[0])
			#boolean_math_002_5.Boolean -> group_output_34.Selection
			is_alpha_carbon.links.new(boolean_math_002_5.outputs[0], group_output_34.inputs[0])
			#group_001_6.Boolean -> boolean_math_001_5.Boolean
			is_alpha_carbon.links.new(group_001_6.outputs[0], boolean_math_001_5.inputs[1])
			#group_002_6.Is Alpha Carbon -> group_001_6.Fallback
			is_alpha_carbon.links.new(group_002_6.outputs[3], group_001_6.inputs[1])
			#boolean_math_001_5.Boolean -> boolean_math_002_5.Boolean
			is_alpha_carbon.links.new(boolean_math_001_5.outputs[0], boolean_math_002_5.inputs[0])
			#group_input_33.Or -> boolean_math_002_5.Boolean
			is_alpha_carbon.links.new(group_input_33.outputs[1], boolean_math_002_5.inputs[1])
			#boolean_math_002_5.Boolean -> boolean_math_8.Boolean
			is_alpha_carbon.links.new(boolean_math_002_5.outputs[0], boolean_math_8.inputs[0])
			#boolean_math_8.Boolean -> group_output_34.Inverted
			is_alpha_carbon.links.new(boolean_math_8.outputs[0], group_output_34.inputs[1])
			return is_alpha_carbon

		is_alpha_carbon = is_alpha_carbon_node_group()

		#initialize _mn_topo_assign_backbone node group
		def _mn_topo_assign_backbone_node_group():
			_mn_topo_assign_backbone = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_topo_assign_backbone")

			_mn_topo_assign_backbone.color_tag = 'NONE'
			_mn_topo_assign_backbone.description = ""

			
			#_mn_topo_assign_backbone interface
			#Socket Atoms
			atoms_socket = _mn_topo_assign_backbone.interface.new_socket(name = "Atoms", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket.attribute_domain = 'POINT'
			
			#Socket Unique Group ID
			unique_group_id_socket_1 = _mn_topo_assign_backbone.interface.new_socket(name = "Unique Group ID", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			unique_group_id_socket_1.default_value = 0
			unique_group_id_socket_1.min_value = -2147483648
			unique_group_id_socket_1.max_value = 2147483647
			unique_group_id_socket_1.subtype = 'NONE'
			unique_group_id_socket_1.attribute_domain = 'POINT'
			
			#Socket CA Atoms
			ca_atoms_socket = _mn_topo_assign_backbone.interface.new_socket(name = "CA Atoms", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			ca_atoms_socket.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket_1 = _mn_topo_assign_backbone.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_1.attribute_domain = 'POINT'
			
			
			#initialize _mn_topo_assign_backbone nodes
			#node Group Output
			group_output_35 = _mn_topo_assign_backbone.nodes.new("NodeGroupOutput")
			group_output_35.name = "Group Output"
			group_output_35.is_active_output = True
			
			#node Group Input
			group_input_34 = _mn_topo_assign_backbone.nodes.new("NodeGroupInput")
			group_input_34.name = "Group Input"
			
			#node Store Named Attribute.002
			store_named_attribute_002_1 = _mn_topo_assign_backbone.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_002_1.name = "Store Named Attribute.002"
			store_named_attribute_002_1.data_type = 'FLOAT_VECTOR'
			store_named_attribute_002_1.domain = 'POINT'
			#Name
			store_named_attribute_002_1.inputs[2].default_value = "backbone_N"
			
			#node Store Named Attribute.003
			store_named_attribute_003_1 = _mn_topo_assign_backbone.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_003_1.name = "Store Named Attribute.003"
			store_named_attribute_003_1.data_type = 'FLOAT_VECTOR'
			store_named_attribute_003_1.domain = 'POINT'
			#Name
			store_named_attribute_003_1.inputs[2].default_value = "backbone_C"
			
			#node Store Named Attribute.004
			store_named_attribute_004_1 = _mn_topo_assign_backbone.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_004_1.name = "Store Named Attribute.004"
			store_named_attribute_004_1.data_type = 'FLOAT_VECTOR'
			store_named_attribute_004_1.domain = 'POINT'
			#Name
			store_named_attribute_004_1.inputs[2].default_value = "backbone_CA"
			
			#node Store Named Attribute.005
			store_named_attribute_005_1 = _mn_topo_assign_backbone.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_005_1.name = "Store Named Attribute.005"
			store_named_attribute_005_1.data_type = 'FLOAT_VECTOR'
			store_named_attribute_005_1.domain = 'POINT'
			#Name
			store_named_attribute_005_1.inputs[2].default_value = "backbone_O"
			
			#node MN_topo_point_mask.005
			mn_topo_point_mask_005 = _mn_topo_assign_backbone.nodes.new("GeometryNodeGroup")
			mn_topo_point_mask_005.label = "Topology Point Mask"
			mn_topo_point_mask_005.name = "MN_topo_point_mask.005"
			mn_topo_point_mask_005.node_tree = residue_mask
			#Socket_1
			mn_topo_point_mask_005.inputs[0].default_value = 3
			#Socket_5
			mn_topo_point_mask_005.inputs[1].default_value = False
			
			#node MN_topo_point_mask.006
			mn_topo_point_mask_006 = _mn_topo_assign_backbone.nodes.new("GeometryNodeGroup")
			mn_topo_point_mask_006.label = "Topology Point Mask"
			mn_topo_point_mask_006.name = "MN_topo_point_mask.006"
			mn_topo_point_mask_006.node_tree = residue_mask
			#Socket_1
			mn_topo_point_mask_006.inputs[0].default_value = 2
			#Socket_5
			mn_topo_point_mask_006.inputs[1].default_value = False
			
			#node MN_topo_point_mask.007
			mn_topo_point_mask_007 = _mn_topo_assign_backbone.nodes.new("GeometryNodeGroup")
			mn_topo_point_mask_007.label = "Topology Point Mask"
			mn_topo_point_mask_007.name = "MN_topo_point_mask.007"
			mn_topo_point_mask_007.node_tree = residue_mask
			#Socket_1
			mn_topo_point_mask_007.inputs[0].default_value = 4
			#Socket_5
			mn_topo_point_mask_007.inputs[1].default_value = False
			
			#node MN_topo_point_mask.004
			mn_topo_point_mask_004 = _mn_topo_assign_backbone.nodes.new("GeometryNodeGroup")
			mn_topo_point_mask_004.label = "Topology Point Mask"
			mn_topo_point_mask_004.name = "MN_topo_point_mask.004"
			mn_topo_point_mask_004.node_tree = residue_mask
			#Socket_1
			mn_topo_point_mask_004.inputs[0].default_value = 1
			#Socket_5
			mn_topo_point_mask_004.inputs[1].default_value = False
			
			#node Capture Attribute
			capture_attribute_1 = _mn_topo_assign_backbone.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute_1.name = "Capture Attribute"
			capture_attribute_1.active_index = 0
			capture_attribute_1.capture_items.clear()
			capture_attribute_1.capture_items.new('FLOAT', "Unique Group ID")
			capture_attribute_1.capture_items["Unique Group ID"].data_type = 'INT'
			capture_attribute_1.domain = 'POINT'
			
			#node Group
			group_11 = _mn_topo_assign_backbone.nodes.new("GeometryNodeGroup")
			group_11.name = "Group"
			group_11.node_tree = res_group_id
			
			#node Reroute
			reroute_7 = _mn_topo_assign_backbone.nodes.new("NodeReroute")
			reroute_7.name = "Reroute"
			#node Reroute.001
			reroute_001_4 = _mn_topo_assign_backbone.nodes.new("NodeReroute")
			reroute_001_4.name = "Reroute.001"
			#node Reroute.002
			reroute_002_4 = _mn_topo_assign_backbone.nodes.new("NodeReroute")
			reroute_002_4.name = "Reroute.002"
			#node Reroute.003
			reroute_003_2 = _mn_topo_assign_backbone.nodes.new("NodeReroute")
			reroute_003_2.name = "Reroute.003"
			#node Separate Geometry
			separate_geometry = _mn_topo_assign_backbone.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry.name = "Separate Geometry"
			separate_geometry.domain = 'POINT'
			
			#node Group.001
			group_001_7 = _mn_topo_assign_backbone.nodes.new("GeometryNodeGroup")
			group_001_7.name = "Group.001"
			group_001_7.node_tree = is_alpha_carbon
			#Socket_1
			group_001_7.inputs[0].default_value = True
			#Socket_3
			group_001_7.inputs[1].default_value = False
			
			
			
			
			#Set locations
			group_output_35.location = (720.0, 100.0)
			group_input_34.location = (-1200.0, 100.0)
			store_named_attribute_002_1.location = (-400.0, 100.0)
			store_named_attribute_003_1.location = (60.0, 100.0)
			store_named_attribute_004_1.location = (-180.0, 100.0)
			store_named_attribute_005_1.location = (300.0, 100.0)
			mn_topo_point_mask_005.location = (60.0, -120.0)
			mn_topo_point_mask_006.location = (-180.0, -120.0)
			mn_topo_point_mask_007.location = (300.0, -120.0)
			mn_topo_point_mask_004.location = (-400.0, -120.0)
			capture_attribute_1.location = (-1020.0, 100.0)
			group_11.location = (-1200.0, 0.0)
			reroute_7.location = (-440.0, -340.0)
			reroute_001_4.location = (-200.0, -340.0)
			reroute_002_4.location = (40.0, -340.0)
			reroute_003_2.location = (280.0, -340.0)
			separate_geometry.location = (540.0, 20.0)
			group_001_7.location = (540.0, -160.0)
			
			#Set dimensions
			group_output_35.width, group_output_35.height = 140.0, 100.0
			group_input_34.width, group_input_34.height = 140.0, 100.0
			store_named_attribute_002_1.width, store_named_attribute_002_1.height = 172.44415283203125, 100.0
			store_named_attribute_003_1.width, store_named_attribute_003_1.height = 169.44052124023438, 100.0
			store_named_attribute_004_1.width, store_named_attribute_004_1.height = 184.14559936523438, 100.0
			store_named_attribute_005_1.width, store_named_attribute_005_1.height = 169.42654418945312, 100.0
			mn_topo_point_mask_005.width, mn_topo_point_mask_005.height = 172.76019287109375, 100.0
			mn_topo_point_mask_006.width, mn_topo_point_mask_006.height = 185.9674072265625, 100.0
			mn_topo_point_mask_007.width, mn_topo_point_mask_007.height = 168.1260986328125, 100.0
			mn_topo_point_mask_004.width, mn_topo_point_mask_004.height = 178.538330078125, 100.0
			capture_attribute_1.width, capture_attribute_1.height = 140.0, 100.0
			group_11.width, group_11.height = 140.0, 100.0
			reroute_7.width, reroute_7.height = 16.0, 100.0
			reroute_001_4.width, reroute_001_4.height = 16.0, 100.0
			reroute_002_4.width, reroute_002_4.height = 16.0, 100.0
			reroute_003_2.width, reroute_003_2.height = 16.0, 100.0
			separate_geometry.width, separate_geometry.height = 140.0, 100.0
			group_001_7.width, group_001_7.height = 140.0, 100.0
			
			#initialize _mn_topo_assign_backbone links
			#mn_topo_point_mask_007.Is Valid -> store_named_attribute_005_1.Selection
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_007.outputs[0], store_named_attribute_005_1.inputs[1])
			#mn_topo_point_mask_006.Position -> store_named_attribute_004_1.Value
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_006.outputs[2], store_named_attribute_004_1.inputs[3])
			#mn_topo_point_mask_005.Position -> store_named_attribute_003_1.Value
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_005.outputs[2], store_named_attribute_003_1.inputs[3])
			#store_named_attribute_004_1.Geometry -> store_named_attribute_003_1.Geometry
			_mn_topo_assign_backbone.links.new(store_named_attribute_004_1.outputs[0], store_named_attribute_003_1.inputs[0])
			#store_named_attribute_003_1.Geometry -> store_named_attribute_005_1.Geometry
			_mn_topo_assign_backbone.links.new(store_named_attribute_003_1.outputs[0], store_named_attribute_005_1.inputs[0])
			#store_named_attribute_002_1.Geometry -> store_named_attribute_004_1.Geometry
			_mn_topo_assign_backbone.links.new(store_named_attribute_002_1.outputs[0], store_named_attribute_004_1.inputs[0])
			#mn_topo_point_mask_007.Position -> store_named_attribute_005_1.Value
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_007.outputs[2], store_named_attribute_005_1.inputs[3])
			#mn_topo_point_mask_006.Is Valid -> store_named_attribute_004_1.Selection
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_006.outputs[0], store_named_attribute_004_1.inputs[1])
			#mn_topo_point_mask_005.Is Valid -> store_named_attribute_003_1.Selection
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_005.outputs[0], store_named_attribute_003_1.inputs[1])
			#capture_attribute_1.Geometry -> store_named_attribute_002_1.Geometry
			_mn_topo_assign_backbone.links.new(capture_attribute_1.outputs[0], store_named_attribute_002_1.inputs[0])
			#store_named_attribute_005_1.Geometry -> group_output_35.Atoms
			_mn_topo_assign_backbone.links.new(store_named_attribute_005_1.outputs[0], group_output_35.inputs[0])
			#group_input_34.Atoms -> capture_attribute_1.Geometry
			_mn_topo_assign_backbone.links.new(group_input_34.outputs[0], capture_attribute_1.inputs[0])
			#group_11.Unique Group ID -> capture_attribute_1.Unique Group ID
			_mn_topo_assign_backbone.links.new(group_11.outputs[0], capture_attribute_1.inputs[1])
			#reroute_001_4.Output -> mn_topo_point_mask_006.Group ID
			_mn_topo_assign_backbone.links.new(reroute_001_4.outputs[0], mn_topo_point_mask_006.inputs[2])
			#capture_attribute_1.Unique Group ID -> reroute_7.Input
			_mn_topo_assign_backbone.links.new(capture_attribute_1.outputs[1], reroute_7.inputs[0])
			#reroute_7.Output -> reroute_001_4.Input
			_mn_topo_assign_backbone.links.new(reroute_7.outputs[0], reroute_001_4.inputs[0])
			#reroute_002_4.Output -> mn_topo_point_mask_005.Group ID
			_mn_topo_assign_backbone.links.new(reroute_002_4.outputs[0], mn_topo_point_mask_005.inputs[2])
			#reroute_001_4.Output -> reroute_002_4.Input
			_mn_topo_assign_backbone.links.new(reroute_001_4.outputs[0], reroute_002_4.inputs[0])
			#reroute_003_2.Output -> mn_topo_point_mask_007.Group ID
			_mn_topo_assign_backbone.links.new(reroute_003_2.outputs[0], mn_topo_point_mask_007.inputs[2])
			#reroute_002_4.Output -> reroute_003_2.Input
			_mn_topo_assign_backbone.links.new(reroute_002_4.outputs[0], reroute_003_2.inputs[0])
			#capture_attribute_1.Unique Group ID -> group_output_35.Unique Group ID
			_mn_topo_assign_backbone.links.new(capture_attribute_1.outputs[1], group_output_35.inputs[1])
			#mn_topo_point_mask_004.Is Valid -> store_named_attribute_002_1.Selection
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_004.outputs[0], store_named_attribute_002_1.inputs[1])
			#mn_topo_point_mask_004.Position -> store_named_attribute_002_1.Value
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_004.outputs[2], store_named_attribute_002_1.inputs[3])
			#store_named_attribute_005_1.Geometry -> separate_geometry.Geometry
			_mn_topo_assign_backbone.links.new(store_named_attribute_005_1.outputs[0], separate_geometry.inputs[0])
			#separate_geometry.Selection -> group_output_35.CA Atoms
			_mn_topo_assign_backbone.links.new(separate_geometry.outputs[0], group_output_35.inputs[2])
			#group_001_7.Selection -> separate_geometry.Selection
			_mn_topo_assign_backbone.links.new(group_001_7.outputs[0], separate_geometry.inputs[1])
			#reroute_7.Output -> mn_topo_point_mask_004.Group ID
			_mn_topo_assign_backbone.links.new(reroute_7.outputs[0], mn_topo_point_mask_004.inputs[2])
			return _mn_topo_assign_backbone

		_mn_topo_assign_backbone = _mn_topo_assign_backbone_node_group()

		#initialize topology_dssp node group
		def topology_dssp_node_group():
			topology_dssp = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Topology DSSP")

			topology_dssp.color_tag = 'GEOMETRY'
			topology_dssp.description = "Calculate the secondary structure attributes for the protein chains, based on the 1983 Kabsch algorithm"

			
			#topology_dssp interface
			#Socket Atoms
			atoms_socket_2 = topology_dssp.interface.new_socket(name = "Atoms", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_2.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket_3 = topology_dssp.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_3.attribute_domain = 'POINT'
			
			#Socket Selection
			selection_socket_1 = topology_dssp.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_1.default_value = True
			selection_socket_1.attribute_domain = 'POINT'
			selection_socket_1.hide_value = True
			
			
			#initialize topology_dssp nodes
			#node Group Output
			group_output_36 = topology_dssp.nodes.new("NodeGroupOutput")
			group_output_36.name = "Group Output"
			group_output_36.is_active_output = True
			
			#node Group Input
			group_input_35 = topology_dssp.nodes.new("NodeGroupInput")
			group_input_35.name = "Group Input"
			
			#node Group.002
			group_002_7 = topology_dssp.nodes.new("GeometryNodeGroup")
			group_002_7.name = "Group.002"
			group_002_7.node_tree = _mn_topo_calc_helix
			
			#node Store Named Attribute.003
			store_named_attribute_003_2 = topology_dssp.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_003_2.label = "store helix"
			store_named_attribute_003_2.name = "Store Named Attribute.003"
			store_named_attribute_003_2.data_type = 'INT'
			store_named_attribute_003_2.domain = 'POINT'
			#Name
			store_named_attribute_003_2.inputs[2].default_value = "sec_struct"
			
			#node Sample Index
			sample_index = topology_dssp.nodes.new("GeometryNodeSampleIndex")
			sample_index.name = "Sample Index"
			sample_index.clamp = False
			sample_index.data_type = 'BOOLEAN'
			sample_index.domain = 'POINT'
			
			#node Group.005
			group_005_4 = topology_dssp.nodes.new("GeometryNodeGroup")
			group_005_4.name = "Group.005"
			group_005_4.node_tree = _mn_topo_calc_sheet
			
			#node Sample Index.001
			sample_index_001 = topology_dssp.nodes.new("GeometryNodeSampleIndex")
			sample_index_001.name = "Sample Index.001"
			sample_index_001.clamp = False
			sample_index_001.data_type = 'BOOLEAN'
			sample_index_001.domain = 'POINT'
			
			#node Sample Index.002
			sample_index_002 = topology_dssp.nodes.new("GeometryNodeSampleIndex")
			sample_index_002.name = "Sample Index.002"
			sample_index_002.hide = True
			sample_index_002.clamp = False
			sample_index_002.data_type = 'INT'
			sample_index_002.domain = 'POINT'
			
			#node Index
			index_3 = topology_dssp.nodes.new("GeometryNodeInputIndex")
			index_3.name = "Index"
			
			#node Switch
			switch_7 = topology_dssp.nodes.new("GeometryNodeSwitch")
			switch_7.name = "Switch"
			switch_7.input_type = 'INT'
			#False
			switch_7.inputs[1].default_value = 3
			#True
			switch_7.inputs[2].default_value = 2
			
			#node Switch.001
			switch_001_2 = topology_dssp.nodes.new("GeometryNodeSwitch")
			switch_001_2.name = "Switch.001"
			switch_001_2.input_type = 'INT'
			#True
			switch_001_2.inputs[2].default_value = 1
			
			#node Reroute.003
			reroute_003_3 = topology_dssp.nodes.new("NodeReroute")
			reroute_003_3.name = "Reroute.003"
			#node Sample Index.003
			sample_index_003 = topology_dssp.nodes.new("GeometryNodeSampleIndex")
			sample_index_003.name = "Sample Index.003"
			sample_index_003.clamp = False
			sample_index_003.data_type = 'INT'
			sample_index_003.domain = 'POINT'
			
			#node Index.002
			index_002 = topology_dssp.nodes.new("GeometryNodeInputIndex")
			index_002.name = "Index.002"
			
			#node MN_topo_compute_backbone.001
			mn_topo_compute_backbone_001 = topology_dssp.nodes.new("GeometryNodeGroup")
			mn_topo_compute_backbone_001.label = "Topology Compute Backbone"
			mn_topo_compute_backbone_001.name = "MN_topo_compute_backbone.001"
			mn_topo_compute_backbone_001.node_tree = _mn_topo_assign_backbone
			
			#node Frame
			frame_10 = topology_dssp.nodes.new("NodeFrame")
			frame_10.label = "Compute Helix"
			frame_10.name = "Frame"
			frame_10.label_size = 20
			frame_10.shrink = True
			
			#node Frame.001
			frame_001_6 = topology_dssp.nodes.new("NodeFrame")
			frame_001_6.label = "Compute Sheet"
			frame_001_6.name = "Frame.001"
			frame_001_6.label_size = 20
			frame_001_6.shrink = True
			
			
			
			#Set parents
			group_002_7.parent = frame_10
			sample_index.parent = frame_10
			group_005_4.parent = frame_001_6
			sample_index_001.parent = frame_001_6
			
			#Set locations
			group_output_36.location = (676.5311889648438, 311.6835632324219)
			group_input_35.location = (-1820.0, 380.0)
			group_002_7.location = (-1140.0, -80.0)
			store_named_attribute_003_2.location = (-520.0, 480.0)
			sample_index.location = (-740.0, -60.0)
			group_005_4.location = (-1140.0, -380.0)
			sample_index_001.location = (-740.0, -380.0)
			sample_index_002.location = (-720.0, 120.0)
			index_3.location = (-920.0, 120.0)
			switch_7.location = (-520.0, -120.0)
			switch_001_2.location = (-520.0, 40.0)
			reroute_003_3.location = (-1300.0, -120.0)
			sample_index_003.location = (-520.0, 280.0)
			index_002.location = (-940.0, -200.0)
			mn_topo_compute_backbone_001.location = (-1560.0, 300.0)
			frame_10.location = (-10.0, 80.0)
			frame_001_6.location = (-10.0, 80.0)
			
			#Set dimensions
			group_output_36.width, group_output_36.height = 140.0, 100.0
			group_input_35.width, group_input_35.height = 140.0, 100.0
			group_002_7.width, group_002_7.height = 238.041015625, 100.0
			store_named_attribute_003_2.width, store_named_attribute_003_2.height = 140.0, 100.0
			sample_index.width, sample_index.height = 140.0, 100.0
			group_005_4.width, group_005_4.height = 210.28070068359375, 100.0
			sample_index_001.width, sample_index_001.height = 140.0, 100.0
			sample_index_002.width, sample_index_002.height = 140.0, 100.0
			index_3.width, index_3.height = 140.0, 100.0
			switch_7.width, switch_7.height = 140.0, 100.0
			switch_001_2.width, switch_001_2.height = 140.0, 100.0
			reroute_003_3.width, reroute_003_3.height = 16.0, 100.0
			sample_index_003.width, sample_index_003.height = 140.0, 100.0
			index_002.width, index_002.height = 140.0, 100.0
			mn_topo_compute_backbone_001.width, mn_topo_compute_backbone_001.height = 207.010986328125, 100.0
			frame_10.width, frame_10.height = 600.0, 264.0
			frame_001_6.width, frame_001_6.height = 600.0, 264.0
			
			#initialize topology_dssp links
			#group_input_35.Atoms -> store_named_attribute_003_2.Geometry
			topology_dssp.links.new(group_input_35.outputs[0], store_named_attribute_003_2.inputs[0])
			#reroute_003_3.Output -> sample_index.Geometry
			topology_dssp.links.new(reroute_003_3.outputs[0], sample_index.inputs[0])
			#store_named_attribute_003_2.Geometry -> group_output_36.Atoms
			topology_dssp.links.new(store_named_attribute_003_2.outputs[0], group_output_36.inputs[0])
			#reroute_003_3.Output -> group_005_4.Geometry
			topology_dssp.links.new(reroute_003_3.outputs[0], group_005_4.inputs[0])
			#mn_topo_compute_backbone_001.Atoms -> sample_index_002.Geometry
			topology_dssp.links.new(mn_topo_compute_backbone_001.outputs[0], sample_index_002.inputs[0])
			#index_3.Index -> sample_index_002.Index
			topology_dssp.links.new(index_3.outputs[0], sample_index_002.inputs[2])
			#group_005_4.Geometry -> sample_index_001.Geometry
			topology_dssp.links.new(group_005_4.outputs[0], sample_index_001.inputs[0])
			#sample_index_001.Value -> switch_7.Switch
			topology_dssp.links.new(sample_index_001.outputs[0], switch_7.inputs[0])
			#switch_7.Output -> switch_001_2.False
			topology_dssp.links.new(switch_7.outputs[0], switch_001_2.inputs[1])
			#sample_index.Value -> switch_001_2.Switch
			topology_dssp.links.new(sample_index.outputs[0], switch_001_2.inputs[0])
			#mn_topo_compute_backbone_001.CA Atoms -> reroute_003_3.Input
			topology_dssp.links.new(mn_topo_compute_backbone_001.outputs[2], reroute_003_3.inputs[0])
			#group_002_7.Is Helix -> sample_index.Value
			topology_dssp.links.new(group_002_7.outputs[0], sample_index.inputs[1])
			#group_005_4.Attribute -> sample_index_001.Value
			topology_dssp.links.new(group_005_4.outputs[1], sample_index_001.inputs[1])
			#mn_topo_compute_backbone_001.Unique Group ID -> sample_index_002.Value
			topology_dssp.links.new(mn_topo_compute_backbone_001.outputs[1], sample_index_002.inputs[1])
			#sample_index_002.Value -> sample_index_003.Index
			topology_dssp.links.new(sample_index_002.outputs[0], sample_index_003.inputs[2])
			#mn_topo_compute_backbone_001.CA Atoms -> sample_index_003.Geometry
			topology_dssp.links.new(mn_topo_compute_backbone_001.outputs[2], sample_index_003.inputs[0])
			#switch_001_2.Output -> sample_index_003.Value
			topology_dssp.links.new(switch_001_2.outputs[0], sample_index_003.inputs[1])
			#sample_index_003.Value -> store_named_attribute_003_2.Value
			topology_dssp.links.new(sample_index_003.outputs[0], store_named_attribute_003_2.inputs[3])
			#index_002.Index -> sample_index.Index
			topology_dssp.links.new(index_002.outputs[0], sample_index.inputs[2])
			#group_input_35.Selection -> store_named_attribute_003_2.Selection
			topology_dssp.links.new(group_input_35.outputs[1], store_named_attribute_003_2.inputs[1])
			#group_input_35.Atoms -> mn_topo_compute_backbone_001.Atoms
			topology_dssp.links.new(group_input_35.outputs[0], mn_topo_compute_backbone_001.inputs[0])
			#index_002.Index -> sample_index_001.Index
			topology_dssp.links.new(index_002.outputs[0], sample_index_001.inputs[2])
			return topology_dssp

		topology_dssp = topology_dssp_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Topology DSSP", type = 'NODES')
		mod.node_group = topology_dssp
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Topology_DSSP.bl_idname)
			
def register():
	bpy.utils.register_class(Topology_DSSP)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Topology_DSSP)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
