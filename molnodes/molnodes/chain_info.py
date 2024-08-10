bl_info = {
	"name" : "Chain Info",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Chain_Info(bpy.types.Operator):
	bl_idname = "node.chain_info"
	bl_label = "Chain Info"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize offset_integer node group
		def offset_integer_node_group():
			offset_integer = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Offset Integer")

			offset_integer.color_tag = 'CONVERTER'
			offset_integer.description = ""

			
			#offset_integer interface
			#Socket Value
			value_socket = offset_integer.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			value_socket.subtype = 'NONE'
			value_socket.default_value = 0
			value_socket.min_value = -2147483648
			value_socket.max_value = 2147483647
			value_socket.attribute_domain = 'POINT'
			
			#Socket Index
			index_socket = offset_integer.interface.new_socket(name = "Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			index_socket.subtype = 'NONE'
			index_socket.default_value = 0
			index_socket.min_value = 0
			index_socket.max_value = 2147483647
			index_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_1 = offset_integer.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketInt')
			value_socket_1.subtype = 'NONE'
			value_socket_1.default_value = 0
			value_socket_1.min_value = -2147483648
			value_socket_1.max_value = 2147483647
			value_socket_1.attribute_domain = 'POINT'
			value_socket_1.hide_value = True
			
			#Socket Offset
			offset_socket = offset_integer.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket.subtype = 'NONE'
			offset_socket.default_value = 0
			offset_socket.min_value = -2147483648
			offset_socket.max_value = 2147483647
			offset_socket.attribute_domain = 'POINT'
			
			
			#initialize offset_integer nodes
			#node Group Output
			group_output = offset_integer.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = offset_integer.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Evaluate at Index
			evaluate_at_index = offset_integer.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index.name = "Evaluate at Index"
			evaluate_at_index.data_type = 'INT'
			evaluate_at_index.domain = 'POINT'
			
			#node Math
			math = offset_integer.nodes.new("ShaderNodeMath")
			math.name = "Math"
			math.operation = 'ADD'
			math.use_clamp = False
			
			
			
			
			#Set locations
			group_output.location = (190.0, 0.0)
			group_input.location = (-412.72760009765625, 0.2001800537109375)
			evaluate_at_index.location = (0.0, 0.0)
			math.location = (-217.90158081054688, 69.93922424316406)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			evaluate_at_index.width, evaluate_at_index.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			
			#initialize offset_integer links
			#evaluate_at_index.Value -> group_output.Value
			offset_integer.links.new(evaluate_at_index.outputs[0], group_output.inputs[0])
			#group_input.Index -> math.Value
			offset_integer.links.new(group_input.outputs[0], math.inputs[0])
			#group_input.Offset -> math.Value
			offset_integer.links.new(group_input.outputs[2], math.inputs[1])
			#math.Value -> evaluate_at_index.Index
			offset_integer.links.new(math.outputs[0], evaluate_at_index.inputs[0])
			#group_input.Value -> evaluate_at_index.Value
			offset_integer.links.new(group_input.outputs[1], evaluate_at_index.inputs[1])
			return offset_integer

		offset_integer = offset_integer_node_group()

		#initialize group_info node group
		def group_info_node_group():
			group_info = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Group Info")

			group_info.color_tag = 'CONVERTER'
			group_info.description = ""

			
			#group_info interface
			#Socket First Index
			first_index_socket = group_info.interface.new_socket(name = "First Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			first_index_socket.subtype = 'NONE'
			first_index_socket.default_value = 0
			first_index_socket.min_value = -2147483648
			first_index_socket.max_value = 2147483647
			first_index_socket.attribute_domain = 'POINT'
			first_index_socket.description = "Index of the first point in the group"
			
			#Socket Last Index
			last_index_socket = group_info.interface.new_socket(name = "Last Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			last_index_socket.subtype = 'NONE'
			last_index_socket.default_value = 0
			last_index_socket.min_value = -2147483648
			last_index_socket.max_value = 2147483647
			last_index_socket.attribute_domain = 'POINT'
			last_index_socket.description = "Index of the last point in the group"
			
			#Socket Index in Group
			index_in_group_socket = group_info.interface.new_socket(name = "Index in Group", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			index_in_group_socket.subtype = 'NONE'
			index_in_group_socket.default_value = 0
			index_in_group_socket.min_value = -2147483648
			index_in_group_socket.max_value = 2147483647
			index_in_group_socket.attribute_domain = 'POINT'
			
			#Socket Size
			size_socket = group_info.interface.new_socket(name = "Size", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			size_socket.subtype = 'NONE'
			size_socket.default_value = 0
			size_socket.min_value = -2147483648
			size_socket.max_value = 2147483647
			size_socket.attribute_domain = 'POINT'
			size_socket.description = "Number of points in the group"
			
			#Socket Group ID
			group_id_socket = group_info.interface.new_socket(name = "Group ID", in_out='INPUT', socket_type = 'NodeSocketInt')
			group_id_socket.subtype = 'NONE'
			group_id_socket.default_value = 0
			group_id_socket.min_value = -2147483648
			group_id_socket.max_value = 2147483647
			group_id_socket.attribute_domain = 'POINT'
			
			
			#initialize group_info nodes
			#node Group Output
			group_output_1 = group_info.nodes.new("NodeGroupOutput")
			group_output_1.name = "Group Output"
			group_output_1.is_active_output = True
			
			#node Group Input
			group_input_1 = group_info.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			
			#node Accumulate Field.001
			accumulate_field_001 = group_info.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_001.name = "Accumulate Field.001"
			accumulate_field_001.data_type = 'INT'
			accumulate_field_001.domain = 'POINT'
			accumulate_field_001.outputs[0].hide = True
			accumulate_field_001.outputs[1].hide = True
			
			#node Index
			index = group_info.nodes.new("GeometryNodeInputIndex")
			index.name = "Index"
			
			#node Compare
			compare = group_info.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'EQUAL'
			#B_INT
			compare.inputs[3].default_value = 0
			
			#node Switch.001
			switch_001 = group_info.nodes.new("GeometryNodeSwitch")
			switch_001.name = "Switch.001"
			switch_001.input_type = 'INT'
			#False
			switch_001.inputs[1].default_value = 0
			
			#node Compare.002
			compare_002 = group_info.nodes.new("FunctionNodeCompare")
			compare_002.name = "Compare.002"
			compare_002.data_type = 'INT'
			compare_002.mode = 'ELEMENT'
			compare_002.operation = 'EQUAL'
			
			#node Switch.002
			switch_002 = group_info.nodes.new("GeometryNodeSwitch")
			switch_002.name = "Switch.002"
			switch_002.input_type = 'INT'
			#False
			switch_002.inputs[1].default_value = 0
			
			#node Accumulate Field.002
			accumulate_field_002 = group_info.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_002.name = "Accumulate Field.002"
			accumulate_field_002.data_type = 'INT'
			accumulate_field_002.domain = 'POINT'
			accumulate_field_002.outputs[0].hide = True
			accumulate_field_002.outputs[1].hide = True
			
			#node Reroute
			reroute = group_info.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Accumulate Field.003
			accumulate_field_003 = group_info.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_003.name = "Accumulate Field.003"
			accumulate_field_003.data_type = 'INT'
			accumulate_field_003.domain = 'POINT'
			#Value
			accumulate_field_003.inputs[0].default_value = 1
			
			#node Reroute.001
			reroute_001 = group_info.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			
			
			
			#Set locations
			group_output_1.location = (580.0, 100.0)
			group_input_1.location = (-540.0, 0.0)
			accumulate_field_001.location = (340.0, 140.0)
			index.location = (-40.0, -20.0)
			compare.location = (-40.0, 140.0)
			switch_001.location = (120.0, 140.0)
			compare_002.location = (-40.0, -80.0)
			switch_002.location = (120.0, -20.0)
			accumulate_field_002.location = (340.0, -78.97427368164062)
			reroute.location = (280.0, -300.0)
			accumulate_field_003.location = (-240.0, -80.0)
			reroute_001.location = (-320.0, -300.0)
			
			#Set dimensions
			group_output_1.width, group_output_1.height = 140.0, 100.0
			group_input_1.width, group_input_1.height = 140.0, 100.0
			accumulate_field_001.width, accumulate_field_001.height = 140.0, 100.0
			index.width, index.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			switch_001.width, switch_001.height = 140.0, 100.0
			compare_002.width, compare_002.height = 140.0, 100.0
			switch_002.width, switch_002.height = 140.0, 100.0
			accumulate_field_002.width, accumulate_field_002.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			accumulate_field_003.width, accumulate_field_003.height = 140.0, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			
			#initialize group_info links
			#reroute.Output -> accumulate_field_002.Group ID
			group_info.links.new(reroute.outputs[0], accumulate_field_002.inputs[1])
			#reroute_001.Output -> reroute.Input
			group_info.links.new(reroute_001.outputs[0], reroute.inputs[0])
			#index.Index -> switch_002.True
			group_info.links.new(index.outputs[0], switch_002.inputs[2])
			#accumulate_field_003.Trailing -> compare.A
			group_info.links.new(accumulate_field_003.outputs[1], compare.inputs[2])
			#compare.Result -> switch_001.Switch
			group_info.links.new(compare.outputs[0], switch_001.inputs[0])
			#accumulate_field_003.Total -> compare_002.B
			group_info.links.new(accumulate_field_003.outputs[2], compare_002.inputs[3])
			#switch_002.Output -> accumulate_field_002.Value
			group_info.links.new(switch_002.outputs[0], accumulate_field_002.inputs[0])
			#reroute_001.Output -> accumulate_field_003.Group ID
			group_info.links.new(reroute_001.outputs[0], accumulate_field_003.inputs[1])
			#index.Index -> switch_001.True
			group_info.links.new(index.outputs[0], switch_001.inputs[2])
			#switch_001.Output -> accumulate_field_001.Value
			group_info.links.new(switch_001.outputs[0], accumulate_field_001.inputs[0])
			#compare_002.Result -> switch_002.Switch
			group_info.links.new(compare_002.outputs[0], switch_002.inputs[0])
			#reroute.Output -> accumulate_field_001.Group ID
			group_info.links.new(reroute.outputs[0], accumulate_field_001.inputs[1])
			#group_input_1.Group ID -> reroute_001.Input
			group_info.links.new(group_input_1.outputs[0], reroute_001.inputs[0])
			#accumulate_field_001.Total -> group_output_1.First Index
			group_info.links.new(accumulate_field_001.outputs[2], group_output_1.inputs[0])
			#accumulate_field_002.Total -> group_output_1.Last Index
			group_info.links.new(accumulate_field_002.outputs[2], group_output_1.inputs[1])
			#accumulate_field_003.Total -> group_output_1.Size
			group_info.links.new(accumulate_field_003.outputs[2], group_output_1.inputs[3])
			#accumulate_field_003.Leading -> compare_002.A
			group_info.links.new(accumulate_field_003.outputs[0], compare_002.inputs[2])
			#accumulate_field_003.Trailing -> group_output_1.Index in Group
			group_info.links.new(accumulate_field_003.outputs[1], group_output_1.inputs[2])
			return group_info

		group_info = group_info_node_group()

		#initialize _topo_count_residues node group
		def _topo_count_residues_node_group():
			_topo_count_residues = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".Topo Count Residues")

			_topo_count_residues.color_tag = 'NONE'
			_topo_count_residues.description = ""

			
			#_topo_count_residues interface
			#Socket Counted Res ID
			counted_res_id_socket = _topo_count_residues.interface.new_socket(name = "Counted Res ID", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			counted_res_id_socket.subtype = 'NONE'
			counted_res_id_socket.default_value = 0
			counted_res_id_socket.min_value = -2147483648
			counted_res_id_socket.max_value = 2147483647
			counted_res_id_socket.attribute_domain = 'POINT'
			
			#Socket Total
			total_socket = _topo_count_residues.interface.new_socket(name = "Total", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			total_socket.subtype = 'NONE'
			total_socket.default_value = 0
			total_socket.min_value = -2147483648
			total_socket.max_value = 2147483647
			total_socket.attribute_domain = 'POINT'
			total_socket.description = "Total number of residues"
			
			#Socket First Res ID
			first_res_id_socket = _topo_count_residues.interface.new_socket(name = "First Res ID", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			first_res_id_socket.subtype = 'NONE'
			first_res_id_socket.default_value = 0
			first_res_id_socket.min_value = -2147483648
			first_res_id_socket.max_value = 2147483647
			first_res_id_socket.attribute_domain = 'POINT'
			first_res_id_socket.description = "Res ID value for the first residue"
			
			#Socket Last Res ID
			last_res_id_socket = _topo_count_residues.interface.new_socket(name = "Last Res ID", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			last_res_id_socket.subtype = 'NONE'
			last_res_id_socket.default_value = 0
			last_res_id_socket.min_value = -2147483648
			last_res_id_socket.max_value = 2147483647
			last_res_id_socket.attribute_domain = 'POINT'
			last_res_id_socket.description = "Res ID value for the last residue"
			
			#Socket Index First
			index_first_socket = _topo_count_residues.interface.new_socket(name = "Index First", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			index_first_socket.subtype = 'NONE'
			index_first_socket.default_value = 0
			index_first_socket.min_value = -2147483648
			index_first_socket.max_value = 2147483647
			index_first_socket.attribute_domain = 'POINT'
			
			#Socket Index Last
			index_last_socket = _topo_count_residues.interface.new_socket(name = "Index Last", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			index_last_socket.subtype = 'NONE'
			index_last_socket.default_value = 0
			index_last_socket.min_value = -2147483648
			index_last_socket.max_value = 2147483647
			index_last_socket.attribute_domain = 'POINT'
			
			#Socket Input
			input_socket = _topo_count_residues.interface.new_socket(name = "Input", in_out='INPUT', socket_type = 'NodeSocketInt')
			input_socket.subtype = 'NONE'
			input_socket.default_value = 0
			input_socket.min_value = -2147483648
			input_socket.max_value = 2147483647
			input_socket.attribute_domain = 'POINT'
			
			
			#initialize _topo_count_residues nodes
			#node Group Output
			group_output_2 = _topo_count_residues.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Group Input
			group_input_2 = _topo_count_residues.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
			#node Named Attribute
			named_attribute = _topo_count_residues.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'INT'
			#Name
			named_attribute.inputs[0].default_value = "res_id"
			
			#node Accumulate Field
			accumulate_field = _topo_count_residues.nodes.new("GeometryNodeAccumulateField")
			accumulate_field.name = "Accumulate Field"
			accumulate_field.data_type = 'INT'
			accumulate_field.domain = 'POINT'
			
			#node Group
			group = _topo_count_residues.nodes.new("GeometryNodeGroup")
			group.name = "Group"
			group.node_tree = offset_integer
			#Socket_1
			group.inputs[0].default_value = 0
			#Socket_2
			group.inputs[2].default_value = 1
			
			#node Compare.001
			compare_001 = _topo_count_residues.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'INT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'NOT_EQUAL'
			
			#node Group.001
			group_001 = _topo_count_residues.nodes.new("GeometryNodeGroup")
			group_001.name = "Group.001"
			group_001.node_tree = group_info
			
			#node Evaluate at Index
			evaluate_at_index_1 = _topo_count_residues.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_1.name = "Evaluate at Index"
			evaluate_at_index_1.data_type = 'INT'
			evaluate_at_index_1.domain = 'POINT'
			
			#node Evaluate at Index.001
			evaluate_at_index_001 = _topo_count_residues.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001.name = "Evaluate at Index.001"
			evaluate_at_index_001.data_type = 'INT'
			evaluate_at_index_001.domain = 'POINT'
			
			#node Named Attribute.002
			named_attribute_002 = _topo_count_residues.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002.name = "Named Attribute.002"
			named_attribute_002.data_type = 'INT'
			#Name
			named_attribute_002.inputs[0].default_value = "res_id"
			
			#node Reroute
			reroute_1 = _topo_count_residues.nodes.new("NodeReroute")
			reroute_1.name = "Reroute"
			
			
			
			#Set locations
			group_output_2.location = (935.2698974609375, 237.94854736328125)
			group_input_2.location = (-200.0, -40.0)
			named_attribute.location = (-380.0, 180.0)
			accumulate_field.location = (220.0, 300.0)
			group.location = (-200.0, 120.0)
			compare_001.location = (-20.0, 240.0)
			group_001.location = (220.0, 60.0)
			evaluate_at_index_1.location = (568.0663452148438, -10.300434112548828)
			evaluate_at_index_001.location = (568.0663452148438, -170.30044555664062)
			named_attribute_002.location = (220.0, -160.0)
			reroute_1.location = (149.45323181152344, -57.92286682128906)
			
			#Set dimensions
			group_output_2.width, group_output_2.height = 140.0, 100.0
			group_input_2.width, group_input_2.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			accumulate_field.width, accumulate_field.height = 156.1656494140625, 100.0
			group.width, group.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			group_001.width, group_001.height = 155.5599365234375, 100.0
			evaluate_at_index_1.width, evaluate_at_index_1.height = 140.0, 100.0
			evaluate_at_index_001.width, evaluate_at_index_001.height = 140.0, 100.0
			named_attribute_002.width, named_attribute_002.height = 140.0, 100.0
			reroute_1.width, reroute_1.height = 16.0, 100.0
			
			#initialize _topo_count_residues links
			#group.Value -> compare_001.B
			_topo_count_residues.links.new(group.outputs[0], compare_001.inputs[3])
			#compare_001.Result -> accumulate_field.Value
			_topo_count_residues.links.new(compare_001.outputs[0], accumulate_field.inputs[0])
			#reroute_1.Output -> accumulate_field.Group ID
			_topo_count_residues.links.new(reroute_1.outputs[0], accumulate_field.inputs[1])
			#named_attribute.Attribute -> group.Value
			_topo_count_residues.links.new(named_attribute.outputs[0], group.inputs[1])
			#named_attribute.Attribute -> compare_001.A
			_topo_count_residues.links.new(named_attribute.outputs[0], compare_001.inputs[2])
			#reroute_1.Output -> group_001.Group ID
			_topo_count_residues.links.new(reroute_1.outputs[0], group_001.inputs[0])
			#group_001.First Index -> evaluate_at_index_1.Index
			_topo_count_residues.links.new(group_001.outputs[0], evaluate_at_index_1.inputs[0])
			#group_001.Last Index -> evaluate_at_index_001.Index
			_topo_count_residues.links.new(group_001.outputs[1], evaluate_at_index_001.inputs[0])
			#evaluate_at_index_1.Value -> group_output_2.First Res ID
			_topo_count_residues.links.new(evaluate_at_index_1.outputs[0], group_output_2.inputs[2])
			#evaluate_at_index_001.Value -> group_output_2.Last Res ID
			_topo_count_residues.links.new(evaluate_at_index_001.outputs[0], group_output_2.inputs[3])
			#named_attribute_002.Attribute -> evaluate_at_index_1.Value
			_topo_count_residues.links.new(named_attribute_002.outputs[0], evaluate_at_index_1.inputs[1])
			#named_attribute_002.Attribute -> evaluate_at_index_001.Value
			_topo_count_residues.links.new(named_attribute_002.outputs[0], evaluate_at_index_001.inputs[1])
			#group_001.First Index -> group_output_2.Index First
			_topo_count_residues.links.new(group_001.outputs[0], group_output_2.inputs[4])
			#group_001.Last Index -> group_output_2.Index Last
			_topo_count_residues.links.new(group_001.outputs[1], group_output_2.inputs[5])
			#accumulate_field.Trailing -> group_output_2.Counted Res ID
			_topo_count_residues.links.new(accumulate_field.outputs[1], group_output_2.inputs[0])
			#accumulate_field.Total -> group_output_2.Total
			_topo_count_residues.links.new(accumulate_field.outputs[2], group_output_2.inputs[1])
			#group_input_2.Input -> reroute_1.Input
			_topo_count_residues.links.new(group_input_2.outputs[0], reroute_1.inputs[0])
			return _topo_count_residues

		_topo_count_residues = _topo_count_residues_node_group()

		#initialize chain_info node group
		def chain_info_node_group():
			chain_info = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Chain Info")

			chain_info.color_tag = 'INPUT'
			chain_info.description = ""

			
			#chain_info interface
			#Socket Factor
			factor_socket = chain_info.interface.new_socket(name = "Factor", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			factor_socket.subtype = 'FACTOR'
			factor_socket.default_value = 0.0
			factor_socket.min_value = 0.0
			factor_socket.max_value = 1.0
			factor_socket.attribute_domain = 'POINT'
			factor_socket.description = "A residues relative position along a chain. 0 being the first residue in a chain, 1 being the last"
			
			#Socket Length
			length_socket = chain_info.interface.new_socket(name = "Length", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			length_socket.subtype = 'NONE'
			length_socket.default_value = 0
			length_socket.min_value = -2147483648
			length_socket.max_value = 2147483647
			length_socket.attribute_domain = 'POINT'
			length_socket.description = "Number of residues in the chain"
			
			#Socket Counted Index
			counted_index_socket = chain_info.interface.new_socket(name = "Counted Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			counted_index_socket.subtype = 'NONE'
			counted_index_socket.default_value = 0
			counted_index_socket.min_value = -2147483648
			counted_index_socket.max_value = 2147483647
			counted_index_socket.attribute_domain = 'POINT'
			counted_index_socket.description = "Res ID along the chain if counting from 1"
			
			#Socket First Res ID
			first_res_id_socket_1 = chain_info.interface.new_socket(name = "First Res ID", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			first_res_id_socket_1.subtype = 'NONE'
			first_res_id_socket_1.default_value = 0
			first_res_id_socket_1.min_value = -2147483648
			first_res_id_socket_1.max_value = 2147483647
			first_res_id_socket_1.attribute_domain = 'POINT'
			first_res_id_socket_1.description = "The first Res ID in a chain (truncated chains start above 1)"
			
			#Socket Last Res ID
			last_res_id_socket_1 = chain_info.interface.new_socket(name = "Last Res ID", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			last_res_id_socket_1.subtype = 'NONE'
			last_res_id_socket_1.default_value = 0
			last_res_id_socket_1.min_value = -2147483648
			last_res_id_socket_1.max_value = 2147483647
			last_res_id_socket_1.attribute_domain = 'POINT'
			last_res_id_socket_1.description = "The Res ID of the last residue in chain (not equal to Length if chain is truncated)"
			
			#Socket Index First
			index_first_socket_1 = chain_info.interface.new_socket(name = "Index First", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			index_first_socket_1.subtype = 'NONE'
			index_first_socket_1.default_value = 0
			index_first_socket_1.min_value = -2147483648
			index_first_socket_1.max_value = 2147483647
			index_first_socket_1.attribute_domain = 'POINT'
			index_first_socket_1.description = "Index in whole structure of the first atom in the chain"
			
			#Socket Index Last
			index_last_socket_1 = chain_info.interface.new_socket(name = "Index Last", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			index_last_socket_1.subtype = 'NONE'
			index_last_socket_1.default_value = 0
			index_last_socket_1.min_value = -2147483648
			index_last_socket_1.max_value = 2147483647
			index_last_socket_1.attribute_domain = 'POINT'
			index_last_socket_1.description = "Index in the whole structure the last atom in the chain"
			
			#Socket Per Chain
			per_chain_socket = chain_info.interface.new_socket(name = "Per Chain", in_out='INPUT', socket_type = 'NodeSocketBool')
			per_chain_socket.attribute_domain = 'POINT'
			
			
			#initialize chain_info nodes
			#node Group Output
			group_output_3 = chain_info.nodes.new("NodeGroupOutput")
			group_output_3.name = "Group Output"
			group_output_3.is_active_output = True
			
			#node Group Input
			group_input_3 = chain_info.nodes.new("NodeGroupInput")
			group_input_3.name = "Group Input"
			
			#node Group.002
			group_002 = chain_info.nodes.new("GeometryNodeGroup")
			group_002.name = "Group.002"
			group_002.node_tree = _topo_count_residues
			
			#node Map Range.001
			map_range_001 = chain_info.nodes.new("ShaderNodeMapRange")
			map_range_001.name = "Map Range.001"
			map_range_001.clamp = True
			map_range_001.data_type = 'FLOAT'
			map_range_001.interpolation_type = 'LINEAR'
			#From Min
			map_range_001.inputs[1].default_value = 0.0
			#To Min
			map_range_001.inputs[3].default_value = 0.0
			#To Max
			map_range_001.inputs[4].default_value = 1.0
			
			#node Named Attribute
			named_attribute_1 = chain_info.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_1.name = "Named Attribute"
			named_attribute_1.data_type = 'INT'
			#Name
			named_attribute_1.inputs[0].default_value = "chain_id"
			
			#node Switch
			switch = chain_info.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'INT'
			#False
			switch.inputs[1].default_value = 0
			
			
			
			
			#Set locations
			group_output_3.location = (360.0, -40.0)
			group_input_3.location = (-460.0, -140.0)
			group_002.location = (-120.0, -60.0)
			map_range_001.location = (200.0, 100.0)
			named_attribute_1.location = (-460.0, -220.0)
			switch.location = (-283.28857421875, -154.70787048339844)
			
			#Set dimensions
			group_output_3.width, group_output_3.height = 140.0, 100.0
			group_input_3.width, group_input_3.height = 140.0, 100.0
			group_002.width, group_002.height = 240.44110107421875, 100.0
			map_range_001.width, map_range_001.height = 140.0, 100.0
			named_attribute_1.width, named_attribute_1.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			
			#initialize chain_info links
			#map_range_001.Result -> group_output_3.Factor
			chain_info.links.new(map_range_001.outputs[0], group_output_3.inputs[0])
			#group_002.Total -> map_range_001.From Max
			chain_info.links.new(group_002.outputs[1], map_range_001.inputs[2])
			#group_002.Counted Res ID -> map_range_001.Value
			chain_info.links.new(group_002.outputs[0], map_range_001.inputs[0])
			#group_002.First Res ID -> group_output_3.First Res ID
			chain_info.links.new(group_002.outputs[2], group_output_3.inputs[3])
			#group_002.Last Res ID -> group_output_3.Last Res ID
			chain_info.links.new(group_002.outputs[3], group_output_3.inputs[4])
			#group_002.Total -> group_output_3.Length
			chain_info.links.new(group_002.outputs[1], group_output_3.inputs[1])
			#group_002.Counted Res ID -> group_output_3.Counted Index
			chain_info.links.new(group_002.outputs[0], group_output_3.inputs[2])
			#group_002.Index First -> group_output_3.Index First
			chain_info.links.new(group_002.outputs[4], group_output_3.inputs[5])
			#group_002.Index Last -> group_output_3.Index Last
			chain_info.links.new(group_002.outputs[5], group_output_3.inputs[6])
			#named_attribute_1.Attribute -> switch.True
			chain_info.links.new(named_attribute_1.outputs[0], switch.inputs[2])
			#switch.Output -> group_002.Input
			chain_info.links.new(switch.outputs[0], group_002.inputs[0])
			#group_input_3.Per Chain -> switch.Switch
			chain_info.links.new(group_input_3.outputs[0], switch.inputs[0])
			return chain_info

		chain_info = chain_info_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Chain Info", type = 'NODES')
		mod.node_group = chain_info
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Chain_Info.bl_idname)
			
def register():
	bpy.utils.register_class(Chain_Info)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Chain_Info)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
