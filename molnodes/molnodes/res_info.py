bl_info = {
	"name" : "Res Info",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Res_Info(bpy.types.Operator):
	bl_idname = "node.res_info"
	bl_label = "Res Info"
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

		#initialize _topo_count_atoms node group
		def _topo_count_atoms_node_group():
			_topo_count_atoms = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".Topo Count Atoms")

			_topo_count_atoms.color_tag = 'NONE'
			_topo_count_atoms.description = ""

			
			#_topo_count_atoms interface
			#Socket Total
			total_socket = _topo_count_atoms.interface.new_socket(name = "Total", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			total_socket.subtype = 'NONE'
			total_socket.default_value = 0
			total_socket.min_value = -2147483648
			total_socket.max_value = 2147483647
			total_socket.attribute_domain = 'POINT'
			total_socket.description = "Total number of residues"
			
			#Socket Counted Index
			counted_index_socket = _topo_count_atoms.interface.new_socket(name = "Counted Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			counted_index_socket.subtype = 'NONE'
			counted_index_socket.default_value = 0
			counted_index_socket.min_value = -2147483648
			counted_index_socket.max_value = 2147483647
			counted_index_socket.attribute_domain = 'POINT'
			
			#Socket First atom_name
			first_atom_name_socket = _topo_count_atoms.interface.new_socket(name = "First atom_name", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			first_atom_name_socket.subtype = 'NONE'
			first_atom_name_socket.default_value = 0
			first_atom_name_socket.min_value = -2147483648
			first_atom_name_socket.max_value = 2147483647
			first_atom_name_socket.attribute_domain = 'POINT'
			first_atom_name_socket.description = "Res ID value for the first residue"
			
			#Socket Last atom_name
			last_atom_name_socket = _topo_count_atoms.interface.new_socket(name = "Last atom_name", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			last_atom_name_socket.subtype = 'NONE'
			last_atom_name_socket.default_value = 0
			last_atom_name_socket.min_value = -2147483648
			last_atom_name_socket.max_value = 2147483647
			last_atom_name_socket.attribute_domain = 'POINT'
			last_atom_name_socket.description = "Res ID value for the last residue"
			
			#Socket Index First
			index_first_socket = _topo_count_atoms.interface.new_socket(name = "Index First", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			index_first_socket.subtype = 'NONE'
			index_first_socket.default_value = 0
			index_first_socket.min_value = -2147483648
			index_first_socket.max_value = 2147483647
			index_first_socket.attribute_domain = 'POINT'
			
			#Socket Index Last
			index_last_socket = _topo_count_atoms.interface.new_socket(name = "Index Last", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			index_last_socket.subtype = 'NONE'
			index_last_socket.default_value = 0
			index_last_socket.min_value = -2147483648
			index_last_socket.max_value = 2147483647
			index_last_socket.attribute_domain = 'POINT'
			
			
			#initialize _topo_count_atoms nodes
			#node Group Output
			group_output_2 = _topo_count_atoms.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Group Input
			group_input_2 = _topo_count_atoms.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
			#node Named Attribute
			named_attribute = _topo_count_atoms.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'INT'
			#Name
			named_attribute.inputs[0].default_value = "res_id"
			
			#node Group
			group = _topo_count_atoms.nodes.new("GeometryNodeGroup")
			group.name = "Group"
			group.node_tree = offset_integer
			#Socket_1
			group.inputs[0].default_value = 0
			#Socket_2
			group.inputs[2].default_value = -1
			
			#node Compare.001
			compare_001 = _topo_count_atoms.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'INT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'NOT_EQUAL'
			
			#node Group.001
			group_001 = _topo_count_atoms.nodes.new("GeometryNodeGroup")
			group_001.name = "Group.001"
			group_001.node_tree = group_info
			
			#node Evaluate at Index
			evaluate_at_index_1 = _topo_count_atoms.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_1.name = "Evaluate at Index"
			evaluate_at_index_1.data_type = 'INT'
			evaluate_at_index_1.domain = 'POINT'
			
			#node Evaluate at Index.001
			evaluate_at_index_001 = _topo_count_atoms.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001.name = "Evaluate at Index.001"
			evaluate_at_index_001.data_type = 'INT'
			evaluate_at_index_001.domain = 'POINT'
			
			#node Named Attribute.002
			named_attribute_002 = _topo_count_atoms.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002.name = "Named Attribute.002"
			named_attribute_002.data_type = 'INT'
			#Name
			named_attribute_002.inputs[0].default_value = "atom_name"
			
			#node Accumulate Field.001
			accumulate_field_001_1 = _topo_count_atoms.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_001_1.name = "Accumulate Field.001"
			accumulate_field_001_1.data_type = 'INT'
			accumulate_field_001_1.domain = 'POINT'
			#Group Index
			accumulate_field_001_1.inputs[1].default_value = 0
			
			
			
			
			#Set locations
			group_output_2.location = (860.0, 340.0)
			group_input_2.location = (-488.64056396484375, -107.26788330078125)
			named_attribute.location = (-620.0, 120.0)
			group.location = (-440.0, 60.0)
			compare_001.location = (-260.0, 180.0)
			group_001.location = (220.0, 240.0)
			evaluate_at_index_1.location = (540.0, 160.0)
			evaluate_at_index_001.location = (540.0, 0.0)
			named_attribute_002.location = (220.0, 40.0)
			accumulate_field_001_1.location = (20.0, 240.0)
			
			#Set dimensions
			group_output_2.width, group_output_2.height = 140.0, 100.0
			group_input_2.width, group_input_2.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			group.width, group.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			group_001.width, group_001.height = 155.5599365234375, 100.0
			evaluate_at_index_1.width, evaluate_at_index_1.height = 140.0, 100.0
			evaluate_at_index_001.width, evaluate_at_index_001.height = 140.0, 100.0
			named_attribute_002.width, named_attribute_002.height = 140.0, 100.0
			accumulate_field_001_1.width, accumulate_field_001_1.height = 156.1656494140625, 100.0
			
			#initialize _topo_count_atoms links
			#group.Value -> compare_001.B
			_topo_count_atoms.links.new(group.outputs[0], compare_001.inputs[3])
			#named_attribute.Attribute -> group.Value
			_topo_count_atoms.links.new(named_attribute.outputs[0], group.inputs[1])
			#named_attribute.Attribute -> compare_001.A
			_topo_count_atoms.links.new(named_attribute.outputs[0], compare_001.inputs[2])
			#accumulate_field_001_1.Leading -> group_001.Group ID
			_topo_count_atoms.links.new(accumulate_field_001_1.outputs[0], group_001.inputs[0])
			#group_001.First Index -> evaluate_at_index_1.Index
			_topo_count_atoms.links.new(group_001.outputs[0], evaluate_at_index_1.inputs[0])
			#group_001.Last Index -> evaluate_at_index_001.Index
			_topo_count_atoms.links.new(group_001.outputs[1], evaluate_at_index_001.inputs[0])
			#evaluate_at_index_1.Value -> group_output_2.First atom_name
			_topo_count_atoms.links.new(evaluate_at_index_1.outputs[0], group_output_2.inputs[2])
			#evaluate_at_index_001.Value -> group_output_2.Last atom_name
			_topo_count_atoms.links.new(evaluate_at_index_001.outputs[0], group_output_2.inputs[3])
			#named_attribute_002.Attribute -> evaluate_at_index_1.Value
			_topo_count_atoms.links.new(named_attribute_002.outputs[0], evaluate_at_index_1.inputs[1])
			#named_attribute_002.Attribute -> evaluate_at_index_001.Value
			_topo_count_atoms.links.new(named_attribute_002.outputs[0], evaluate_at_index_001.inputs[1])
			#group_001.First Index -> group_output_2.Index First
			_topo_count_atoms.links.new(group_001.outputs[0], group_output_2.inputs[4])
			#group_001.Last Index -> group_output_2.Index Last
			_topo_count_atoms.links.new(group_001.outputs[1], group_output_2.inputs[5])
			#compare_001.Result -> accumulate_field_001_1.Value
			_topo_count_atoms.links.new(compare_001.outputs[0], accumulate_field_001_1.inputs[0])
			#group_001.Size -> group_output_2.Total
			_topo_count_atoms.links.new(group_001.outputs[3], group_output_2.inputs[0])
			#group_001.Index in Group -> group_output_2.Counted Index
			_topo_count_atoms.links.new(group_001.outputs[2], group_output_2.inputs[1])
			return _topo_count_atoms

		_topo_count_atoms = _topo_count_atoms_node_group()

		#initialize res_info node group
		def res_info_node_group():
			res_info = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Res Info")

			res_info.color_tag = 'INPUT'
			res_info.description = ""

			
			#res_info interface
			#Socket Factor
			factor_socket = res_info.interface.new_socket(name = "Factor", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			factor_socket.subtype = 'FACTOR'
			factor_socket.default_value = 0.0
			factor_socket.min_value = 0.0
			factor_socket.max_value = 1.0
			factor_socket.attribute_domain = 'POINT'
			factor_socket.description = "An atom's relative position in a residue, with the first atom being 0 and the last atom being 1"
			
			#Socket Length
			length_socket = res_info.interface.new_socket(name = "Length", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			length_socket.subtype = 'NONE'
			length_socket.default_value = 0
			length_socket.min_value = -2147483648
			length_socket.max_value = 2147483647
			length_socket.attribute_domain = 'POINT'
			length_socket.description = "Number of  atoms in a residue"
			
			#Socket Counted Index
			counted_index_socket_1 = res_info.interface.new_socket(name = "Counted Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			counted_index_socket_1.subtype = 'NONE'
			counted_index_socket_1.default_value = 0
			counted_index_socket_1.min_value = -2147483648
			counted_index_socket_1.max_value = 2147483647
			counted_index_socket_1.attribute_domain = 'POINT'
			counted_index_socket_1.description = "Index of an atom in a residue when counting from 0"
			
			#Socket First atom_name
			first_atom_name_socket_1 = res_info.interface.new_socket(name = "First atom_name", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			first_atom_name_socket_1.subtype = 'NONE'
			first_atom_name_socket_1.default_value = 0
			first_atom_name_socket_1.min_value = -2147483648
			first_atom_name_socket_1.max_value = 2147483647
			first_atom_name_socket_1.attribute_domain = 'POINT'
			first_atom_name_socket_1.description = "the atom_name for the first atom in a residue"
			
			#Socket Last atom_name
			last_atom_name_socket_1 = res_info.interface.new_socket(name = "Last atom_name", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			last_atom_name_socket_1.subtype = 'NONE'
			last_atom_name_socket_1.default_value = 0
			last_atom_name_socket_1.min_value = -2147483648
			last_atom_name_socket_1.max_value = 2147483647
			last_atom_name_socket_1.attribute_domain = 'POINT'
			last_atom_name_socket_1.description = "The atom_name for the last atom in a residue"
			
			#Socket First Index
			first_index_socket_1 = res_info.interface.new_socket(name = "First Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			first_index_socket_1.subtype = 'NONE'
			first_index_socket_1.default_value = 0
			first_index_socket_1.min_value = -2147483648
			first_index_socket_1.max_value = 2147483647
			first_index_socket_1.attribute_domain = 'POINT'
			first_index_socket_1.description = "Index (in the whole structure) for the first atom in a  residue"
			
			#Socket Last Index
			last_index_socket_1 = res_info.interface.new_socket(name = "Last Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			last_index_socket_1.subtype = 'NONE'
			last_index_socket_1.default_value = 0
			last_index_socket_1.min_value = -2147483648
			last_index_socket_1.max_value = 2147483647
			last_index_socket_1.attribute_domain = 'POINT'
			last_index_socket_1.description = "Index (in the whole structure) for the last atom in a  residue"
			
			
			#initialize res_info nodes
			#node Group Output
			group_output_3 = res_info.nodes.new("NodeGroupOutput")
			group_output_3.name = "Group Output"
			group_output_3.is_active_output = True
			
			#node Group Input
			group_input_3 = res_info.nodes.new("NodeGroupInput")
			group_input_3.name = "Group Input"
			
			#node Group.002
			group_002 = res_info.nodes.new("GeometryNodeGroup")
			group_002.name = "Group.002"
			group_002.node_tree = _topo_count_atoms
			
			#node Map Range.001
			map_range_001 = res_info.nodes.new("ShaderNodeMapRange")
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
			
			
			
			
			#Set locations
			group_output_3.location = (374.8729553222656, -40.41082000732422)
			group_input_3.location = (-330.0, 0.0)
			group_002.location = (-120.0, -60.0)
			map_range_001.location = (200.0, 180.0)
			
			#Set dimensions
			group_output_3.width, group_output_3.height = 140.0, 100.0
			group_input_3.width, group_input_3.height = 140.0, 100.0
			group_002.width, group_002.height = 240.44110107421875, 100.0
			map_range_001.width, map_range_001.height = 140.0, 100.0
			
			#initialize res_info links
			#map_range_001.Result -> group_output_3.Factor
			res_info.links.new(map_range_001.outputs[0], group_output_3.inputs[0])
			#group_002.Total -> map_range_001.From Max
			res_info.links.new(group_002.outputs[0], map_range_001.inputs[2])
			#group_002.Counted Index -> map_range_001.Value
			res_info.links.new(group_002.outputs[1], map_range_001.inputs[0])
			#group_002.First atom_name -> group_output_3.First atom_name
			res_info.links.new(group_002.outputs[2], group_output_3.inputs[3])
			#group_002.Last atom_name -> group_output_3.Last atom_name
			res_info.links.new(group_002.outputs[3], group_output_3.inputs[4])
			#group_002.Total -> group_output_3.Length
			res_info.links.new(group_002.outputs[0], group_output_3.inputs[1])
			#group_002.Counted Index -> group_output_3.Counted Index
			res_info.links.new(group_002.outputs[1], group_output_3.inputs[2])
			#group_002.Index First -> group_output_3.First Index
			res_info.links.new(group_002.outputs[4], group_output_3.inputs[5])
			#group_002.Index Last -> group_output_3.Last Index
			res_info.links.new(group_002.outputs[5], group_output_3.inputs[6])
			return res_info

		res_info = res_info_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Res Info", type = 'NODES')
		mod.node_group = res_info
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Res_Info.bl_idname)
			
def register():
	bpy.utils.register_class(Res_Info)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Res_Info)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
