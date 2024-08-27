bl_info = {
	"name" : ".MN_topo_calc_helix",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _MN_topo_calc_helix(bpy.types.Operator):
	bl_idname = "node._mn_topo_calc_helix"
	bl_label = ".MN_topo_calc_helix"
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

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".MN_topo_calc_helix", type = 'NODES')
		mod.node_group = _mn_topo_calc_helix
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_MN_topo_calc_helix.bl_idname)
			
def register():
	bpy.utils.register_class(_MN_topo_calc_helix)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_MN_topo_calc_helix)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
