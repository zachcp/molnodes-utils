bl_info = {
	"name" : ".MN_utils_aa_atom_pos",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _MN_utils_aa_atom_pos(bpy.types.Operator):
	bl_idname = "node._mn_utils_aa_atom_pos"
	bl_label = ".MN_utils_aa_atom_pos"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _utils_group_field_at_selection node group
		def _utils_group_field_at_selection_node_group():
			_utils_group_field_at_selection = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".utils_group_field_at_selection")

			_utils_group_field_at_selection.color_tag = 'NONE'
			_utils_group_field_at_selection.description = ""

			
			#_utils_group_field_at_selection interface
			#Socket Group Index
			group_index_socket = _utils_group_field_at_selection.interface.new_socket(name = "Group Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			group_index_socket.subtype = 'NONE'
			group_index_socket.default_value = 0
			group_index_socket.min_value = -2147483648
			group_index_socket.max_value = 2147483647
			group_index_socket.attribute_domain = 'POINT'
			
			#Socket Float
			float_socket = _utils_group_field_at_selection.interface.new_socket(name = "Float", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			float_socket.subtype = 'NONE'
			float_socket.default_value = 0.0
			float_socket.min_value = -3.4028234663852886e+38
			float_socket.max_value = 3.4028234663852886e+38
			float_socket.attribute_domain = 'POINT'
			
			#Socket Vector
			vector_socket = _utils_group_field_at_selection.interface.new_socket(name = "Vector", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			vector_socket.subtype = 'NONE'
			vector_socket.default_value = (0.0, 0.0, 0.0)
			vector_socket.min_value = -3.4028234663852886e+38
			vector_socket.max_value = 3.4028234663852886e+38
			vector_socket.attribute_domain = 'POINT'
			
			#Socket Boolean
			boolean_socket = _utils_group_field_at_selection.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket.attribute_domain = 'POINT'
			
			#Socket Color
			color_socket = _utils_group_field_at_selection.interface.new_socket(name = "Color", in_out='OUTPUT', socket_type = 'NodeSocketColor')
			color_socket.attribute_domain = 'POINT'
			
			#Socket Integer
			integer_socket = _utils_group_field_at_selection.interface.new_socket(name = "Integer", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			integer_socket.subtype = 'NONE'
			integer_socket.default_value = 0
			integer_socket.min_value = -2147483648
			integer_socket.max_value = 2147483647
			integer_socket.attribute_domain = 'POINT'
			
			#Socket Selection
			selection_socket = _utils_group_field_at_selection.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket.attribute_domain = 'POINT'
			selection_socket.description = "Selection of atoms to apply this node to"
			
			#Socket Group Index
			group_index_socket_1 = _utils_group_field_at_selection.interface.new_socket(name = "Group Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			group_index_socket_1.subtype = 'NONE'
			group_index_socket_1.default_value = 0
			group_index_socket_1.min_value = -2147483648
			group_index_socket_1.max_value = 2147483647
			group_index_socket_1.attribute_domain = 'POINT'
			
			#Socket Float
			float_socket_1 = _utils_group_field_at_selection.interface.new_socket(name = "Float", in_out='INPUT', socket_type = 'NodeSocketFloat')
			float_socket_1.subtype = 'NONE'
			float_socket_1.default_value = 0.0
			float_socket_1.min_value = -3.4028234663852886e+38
			float_socket_1.max_value = 3.4028234663852886e+38
			float_socket_1.attribute_domain = 'POINT'
			float_socket_1.hide_value = True
			
			#Socket Vector
			vector_socket_1 = _utils_group_field_at_selection.interface.new_socket(name = "Vector", in_out='INPUT', socket_type = 'NodeSocketVector')
			vector_socket_1.subtype = 'NONE'
			vector_socket_1.default_value = (0.0, 0.0, 0.0)
			vector_socket_1.min_value = -3.4028234663852886e+38
			vector_socket_1.max_value = 3.4028234663852886e+38
			vector_socket_1.attribute_domain = 'POINT'
			vector_socket_1.hide_value = True
			
			#Socket Boolean
			boolean_socket_1 = _utils_group_field_at_selection.interface.new_socket(name = "Boolean", in_out='INPUT', socket_type = 'NodeSocketBool')
			boolean_socket_1.attribute_domain = 'POINT'
			boolean_socket_1.hide_value = True
			
			#Socket Color
			color_socket_1 = _utils_group_field_at_selection.interface.new_socket(name = "Color", in_out='INPUT', socket_type = 'NodeSocketColor')
			color_socket_1.attribute_domain = 'POINT'
			color_socket_1.hide_value = True
			
			#Socket Integer
			integer_socket_1 = _utils_group_field_at_selection.interface.new_socket(name = "Integer", in_out='INPUT', socket_type = 'NodeSocketInt')
			integer_socket_1.subtype = 'NONE'
			integer_socket_1.default_value = 0
			integer_socket_1.min_value = -2147483648
			integer_socket_1.max_value = 2147483647
			integer_socket_1.attribute_domain = 'POINT'
			integer_socket_1.hide_value = True
			
			
			#initialize _utils_group_field_at_selection nodes
			#node Switch.006
			switch_006 = _utils_group_field_at_selection.nodes.new("GeometryNodeSwitch")
			switch_006.name = "Switch.006"
			switch_006.input_type = 'INT'
			#False
			switch_006.inputs[1].default_value = 0
			
			#node Accumulate Field.002
			accumulate_field_002 = _utils_group_field_at_selection.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_002.name = "Accumulate Field.002"
			accumulate_field_002.data_type = 'INT'
			accumulate_field_002.domain = 'POINT'
			
			#node Index
			index = _utils_group_field_at_selection.nodes.new("GeometryNodeInputIndex")
			index.name = "Index"
			
			#node Group Output
			group_output = _utils_group_field_at_selection.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Field at Index
			field_at_index = _utils_group_field_at_selection.nodes.new("GeometryNodeFieldAtIndex")
			field_at_index.name = "Field at Index"
			field_at_index.data_type = 'FLOAT'
			field_at_index.domain = 'POINT'
			
			#node Field at Index.001
			field_at_index_001 = _utils_group_field_at_selection.nodes.new("GeometryNodeFieldAtIndex")
			field_at_index_001.name = "Field at Index.001"
			field_at_index_001.data_type = 'FLOAT_VECTOR'
			field_at_index_001.domain = 'POINT'
			
			#node Field at Index.002
			field_at_index_002 = _utils_group_field_at_selection.nodes.new("GeometryNodeFieldAtIndex")
			field_at_index_002.name = "Field at Index.002"
			field_at_index_002.data_type = 'BOOLEAN'
			field_at_index_002.domain = 'POINT'
			
			#node Field at Index.003
			field_at_index_003 = _utils_group_field_at_selection.nodes.new("GeometryNodeFieldAtIndex")
			field_at_index_003.name = "Field at Index.003"
			field_at_index_003.data_type = 'FLOAT_COLOR'
			field_at_index_003.domain = 'POINT'
			
			#node Group Input
			group_input = _utils_group_field_at_selection.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Field at Index.004
			field_at_index_004 = _utils_group_field_at_selection.nodes.new("GeometryNodeFieldAtIndex")
			field_at_index_004.name = "Field at Index.004"
			field_at_index_004.data_type = 'INT'
			field_at_index_004.domain = 'POINT'
			
			
			
			
			#Set locations
			switch_006.location = (-80.0, 80.0)
			accumulate_field_002.location = (80.0, 80.0)
			index.location = (-80.0, -80.0)
			group_output.location = (477.87579345703125, 6.6051177978515625)
			field_at_index.location = (280.0, -20.0)
			field_at_index_001.location = (280.0, -180.0)
			field_at_index_002.location = (280.0, -340.0)
			field_at_index_003.location = (280.0, -500.0)
			group_input.location = (-280.0, -0.0)
			field_at_index_004.location = (280.0, -660.0)
			
			#Set dimensions
			switch_006.width, switch_006.height = 140.0, 100.0
			accumulate_field_002.width, accumulate_field_002.height = 140.0, 100.0
			index.width, index.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			field_at_index.width, field_at_index.height = 140.0, 100.0
			field_at_index_001.width, field_at_index_001.height = 140.0, 100.0
			field_at_index_002.width, field_at_index_002.height = 140.0, 100.0
			field_at_index_003.width, field_at_index_003.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			field_at_index_004.width, field_at_index_004.height = 140.0, 100.0
			
			#initialize _utils_group_field_at_selection links
			#group_input.Selection -> switch_006.Switch
			_utils_group_field_at_selection.links.new(group_input.outputs[0], switch_006.inputs[0])
			#accumulate_field_002.Total -> group_output.Group Index
			_utils_group_field_at_selection.links.new(accumulate_field_002.outputs[2], group_output.inputs[0])
			#group_input.Group Index -> accumulate_field_002.Group ID
			_utils_group_field_at_selection.links.new(group_input.outputs[1], accumulate_field_002.inputs[1])
			#index.Index -> switch_006.True
			_utils_group_field_at_selection.links.new(index.outputs[0], switch_006.inputs[2])
			#switch_006.Output -> accumulate_field_002.Value
			_utils_group_field_at_selection.links.new(switch_006.outputs[0], accumulate_field_002.inputs[0])
			#accumulate_field_002.Total -> field_at_index.Index
			_utils_group_field_at_selection.links.new(accumulate_field_002.outputs[2], field_at_index.inputs[0])
			#group_input.Float -> field_at_index.Value
			_utils_group_field_at_selection.links.new(group_input.outputs[2], field_at_index.inputs[1])
			#field_at_index.Value -> group_output.Float
			_utils_group_field_at_selection.links.new(field_at_index.outputs[0], group_output.inputs[1])
			#accumulate_field_002.Total -> field_at_index_001.Index
			_utils_group_field_at_selection.links.new(accumulate_field_002.outputs[2], field_at_index_001.inputs[0])
			#group_input.Vector -> field_at_index_001.Value
			_utils_group_field_at_selection.links.new(group_input.outputs[3], field_at_index_001.inputs[1])
			#field_at_index_001.Value -> group_output.Vector
			_utils_group_field_at_selection.links.new(field_at_index_001.outputs[0], group_output.inputs[2])
			#accumulate_field_002.Total -> field_at_index_002.Index
			_utils_group_field_at_selection.links.new(accumulate_field_002.outputs[2], field_at_index_002.inputs[0])
			#group_input.Boolean -> field_at_index_002.Value
			_utils_group_field_at_selection.links.new(group_input.outputs[4], field_at_index_002.inputs[1])
			#field_at_index_002.Value -> group_output.Boolean
			_utils_group_field_at_selection.links.new(field_at_index_002.outputs[0], group_output.inputs[3])
			#accumulate_field_002.Total -> field_at_index_003.Index
			_utils_group_field_at_selection.links.new(accumulate_field_002.outputs[2], field_at_index_003.inputs[0])
			#group_input.Color -> field_at_index_003.Value
			_utils_group_field_at_selection.links.new(group_input.outputs[5], field_at_index_003.inputs[1])
			#field_at_index_003.Value -> group_output.Color
			_utils_group_field_at_selection.links.new(field_at_index_003.outputs[0], group_output.inputs[4])
			#accumulate_field_002.Total -> field_at_index_004.Index
			_utils_group_field_at_selection.links.new(accumulate_field_002.outputs[2], field_at_index_004.inputs[0])
			#group_input.Integer -> field_at_index_004.Value
			_utils_group_field_at_selection.links.new(group_input.outputs[6], field_at_index_004.inputs[1])
			#field_at_index_004.Value -> group_output.Integer
			_utils_group_field_at_selection.links.new(field_at_index_004.outputs[0], group_output.inputs[5])
			return _utils_group_field_at_selection

		_utils_group_field_at_selection = _utils_group_field_at_selection_node_group()

		#initialize _mn_utils_aa_atom_pos node group
		def _mn_utils_aa_atom_pos_node_group():
			_mn_utils_aa_atom_pos = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_utils_aa_atom_pos")

			_mn_utils_aa_atom_pos.color_tag = 'NONE'
			_mn_utils_aa_atom_pos.description = ""

			
			#_mn_utils_aa_atom_pos interface
			#Socket Position
			position_socket = _mn_utils_aa_atom_pos.interface.new_socket(name = "Position", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			position_socket.subtype = 'NONE'
			position_socket.default_value = (0.0, 0.0, 0.0)
			position_socket.min_value = -3.4028234663852886e+38
			position_socket.max_value = 3.4028234663852886e+38
			position_socket.attribute_domain = 'POINT'
			
			#Socket Group Index
			group_index_socket_2 = _mn_utils_aa_atom_pos.interface.new_socket(name = "Group Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			group_index_socket_2.subtype = 'NONE'
			group_index_socket_2.default_value = 0
			group_index_socket_2.min_value = -2147483648
			group_index_socket_2.max_value = 2147483647
			group_index_socket_2.attribute_domain = 'POINT'
			
			#Socket b_factor
			b_factor_socket = _mn_utils_aa_atom_pos.interface.new_socket(name = "b_factor", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			b_factor_socket.subtype = 'NONE'
			b_factor_socket.default_value = 0.0
			b_factor_socket.min_value = -3.4028234663852886e+38
			b_factor_socket.max_value = 3.4028234663852886e+38
			b_factor_socket.attribute_domain = 'POINT'
			
			#Socket Integer
			integer_socket_2 = _mn_utils_aa_atom_pos.interface.new_socket(name = "Integer", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			integer_socket_2.subtype = 'NONE'
			integer_socket_2.default_value = 0
			integer_socket_2.min_value = -2147483648
			integer_socket_2.max_value = 2147483647
			integer_socket_2.attribute_domain = 'POINT'
			
			#Socket atom_name
			atom_name_socket = _mn_utils_aa_atom_pos.interface.new_socket(name = "atom_name", in_out='INPUT', socket_type = 'NodeSocketInt')
			atom_name_socket.subtype = 'NONE'
			atom_name_socket.default_value = 5
			atom_name_socket.min_value = -2147483648
			atom_name_socket.max_value = 2147483647
			atom_name_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_utils_aa_atom_pos nodes
			#node Frame
			frame = _mn_utils_aa_atom_pos.nodes.new("NodeFrame")
			frame.label = "If atom_name is 0, return midpoint of backbone N and C"
			frame.name = "Frame"
			frame.label_size = 20
			frame.shrink = True
			
			#node Group Input
			group_input_1 = _mn_utils_aa_atom_pos.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			
			#node Named Attribute
			named_attribute = _mn_utils_aa_atom_pos.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'INT'
			#Name
			named_attribute.inputs[0].default_value = "atom_name"
			
			#node Compare.002
			compare_002 = _mn_utils_aa_atom_pos.nodes.new("FunctionNodeCompare")
			compare_002.name = "Compare.002"
			compare_002.data_type = 'INT'
			compare_002.mode = 'ELEMENT'
			compare_002.operation = 'EQUAL'
			#B_INT
			compare_002.inputs[3].default_value = 1
			
			#node Compare
			compare = _mn_utils_aa_atom_pos.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.hide = True
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'EQUAL'
			
			#node Named Attribute.001
			named_attribute_001 = _mn_utils_aa_atom_pos.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.label = "b_factor"
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.hide = True
			named_attribute_001.data_type = 'FLOAT'
			#Name
			named_attribute_001.inputs[0].default_value = "b_factor"
			
			#node Position.001
			position_001 = _mn_utils_aa_atom_pos.nodes.new("GeometryNodeInputPosition")
			position_001.name = "Position.001"
			
			#node Reroute
			reroute = _mn_utils_aa_atom_pos.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Position.002
			position_002 = _mn_utils_aa_atom_pos.nodes.new("GeometryNodeInputPosition")
			position_002.name = "Position.002"
			
			#node Compare.001
			compare_001 = _mn_utils_aa_atom_pos.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'INT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'EQUAL'
			#B_INT
			compare_001.inputs[3].default_value = 3
			
			#node Compare.003
			compare_003 = _mn_utils_aa_atom_pos.nodes.new("FunctionNodeCompare")
			compare_003.name = "Compare.003"
			compare_003.data_type = 'INT'
			compare_003.mode = 'ELEMENT'
			compare_003.operation = 'EQUAL'
			#B_INT
			compare_003.inputs[3].default_value = 1
			
			#node Switch.005
			switch_005 = _mn_utils_aa_atom_pos.nodes.new("GeometryNodeSwitch")
			switch_005.name = "Switch.005"
			switch_005.input_type = 'VECTOR'
			
			#node Compare.004
			compare_004 = _mn_utils_aa_atom_pos.nodes.new("FunctionNodeCompare")
			compare_004.name = "Compare.004"
			compare_004.data_type = 'INT'
			compare_004.mode = 'ELEMENT'
			compare_004.operation = 'NOT_EQUAL'
			#B_INT
			compare_004.inputs[3].default_value = 0
			
			#node Mix
			mix = _mn_utils_aa_atom_pos.nodes.new("ShaderNodeMix")
			mix.name = "Mix"
			mix.blend_type = 'MIX'
			mix.clamp_factor = True
			mix.clamp_result = False
			mix.data_type = 'VECTOR'
			mix.factor_mode = 'UNIFORM'
			#Factor_Float
			mix.inputs[0].default_value = 0.5
			
			#node Index
			index_1 = _mn_utils_aa_atom_pos.nodes.new("GeometryNodeInputIndex")
			index_1.name = "Index"
			
			#node Edges of Vertex
			edges_of_vertex = _mn_utils_aa_atom_pos.nodes.new("GeometryNodeEdgesOfVertex")
			edges_of_vertex.name = "Edges of Vertex"
			#Weights
			edges_of_vertex.inputs[1].default_value = 0.0
			#Sort Index
			edges_of_vertex.inputs[2].default_value = 0
			
			#node Group.002
			group_002 = _mn_utils_aa_atom_pos.nodes.new("GeometryNodeGroup")
			group_002.name = "Group.002"
			group_002.node_tree = _utils_group_field_at_selection
			group_002.inputs[2].hide = True
			group_002.inputs[4].hide = True
			group_002.inputs[5].hide = True
			group_002.inputs[6].hide = True
			group_002.outputs[0].hide = True
			group_002.outputs[1].hide = True
			group_002.outputs[3].hide = True
			group_002.outputs[4].hide = True
			group_002.outputs[5].hide = True
			#Input_3
			group_002.inputs[2].default_value = 0.0
			#Input_7
			group_002.inputs[4].default_value = False
			#Input_9
			group_002.inputs[5].default_value = (0.0, 0.0, 0.0, 0.0)
			#Input_11
			group_002.inputs[6].default_value = 0
			
			#node Group.001
			group_001 = _mn_utils_aa_atom_pos.nodes.new("GeometryNodeGroup")
			group_001.name = "Group.001"
			group_001.node_tree = _utils_group_field_at_selection
			group_001.inputs[2].hide = True
			group_001.inputs[4].hide = True
			group_001.inputs[5].hide = True
			group_001.inputs[6].hide = True
			group_001.outputs[0].hide = True
			group_001.outputs[1].hide = True
			group_001.outputs[3].hide = True
			group_001.outputs[4].hide = True
			group_001.outputs[5].hide = True
			#Input_3
			group_001.inputs[2].default_value = 0.0
			#Input_7
			group_001.inputs[4].default_value = False
			#Input_9
			group_001.inputs[5].default_value = (0.0, 0.0, 0.0, 0.0)
			#Input_11
			group_001.inputs[6].default_value = 0
			
			#node Group Output
			group_output_1 = _mn_utils_aa_atom_pos.nodes.new("NodeGroupOutput")
			group_output_1.name = "Group Output"
			group_output_1.is_active_output = True
			
			#node Accumulate Field.001
			accumulate_field_001 = _mn_utils_aa_atom_pos.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_001.name = "Accumulate Field.001"
			accumulate_field_001.data_type = 'INT'
			accumulate_field_001.domain = 'POINT'
			#Group Index
			accumulate_field_001.inputs[1].default_value = 0
			
			#node Group
			group = _mn_utils_aa_atom_pos.nodes.new("GeometryNodeGroup")
			group.name = "Group"
			group.node_tree = _utils_group_field_at_selection
			#Input_7
			group.inputs[4].default_value = False
			#Input_9
			group.inputs[5].default_value = (0.0, 0.0, 0.0, 0.0)
			
			
			
			#Set parents
			position_002.parent = frame
			compare_001.parent = frame
			compare_003.parent = frame
			switch_005.parent = frame
			compare_004.parent = frame
			mix.parent = frame
			group_002.parent = frame
			group_001.parent = frame
			
			#Set locations
			frame.location = (0.0, 0.0)
			group_input_1.location = (-580.0, 200.0)
			named_attribute.location = (-580.0, 320.0)
			compare_002.location = (-580.0, 20.0)
			compare.location = (-85.78459167480469, -98.68995666503906)
			named_attribute_001.location = (-80.0, -200.0)
			position_001.location = (-80.0, -140.0)
			reroute.location = (60.0, 80.0)
			position_002.location = (-100.0, 440.0)
			compare_001.location = (-100.0, 380.0)
			compare_003.location = (-100.0, 600.0)
			switch_005.location = (620.0, 360.0)
			compare_004.location = (420.0, 340.0)
			mix.location = (420.0, 560.0)
			index_1.location = (-240.0, -260.0)
			edges_of_vertex.location = (-80.0, -260.0)
			group_002.location = (160.0, 400.0)
			group_001.location = (160.0, 580.0)
			group_output_1.location = (1178.18603515625, 91.78607177734375)
			accumulate_field_001.location = (-420.0, 20.0)
			group.location = (141.92819213867188, 23.15901756286621)
			
			#Set dimensions
			frame.width, frame.height = 920.0, 479.0
			group_input_1.width, group_input_1.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 218.64825439453125, 100.0
			compare_002.width, compare_002.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
			position_001.width, position_001.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			position_002.width, position_002.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			compare_003.width, compare_003.height = 140.0, 100.0
			switch_005.width, switch_005.height = 140.0, 100.0
			compare_004.width, compare_004.height = 140.0, 100.0
			mix.width, mix.height = 140.0, 100.0
			index_1.width, index_1.height = 140.0, 100.0
			edges_of_vertex.width, edges_of_vertex.height = 140.0, 100.0
			group_002.width, group_002.height = 180.198486328125, 100.0
			group_001.width, group_001.height = 180.198486328125, 100.0
			group_output_1.width, group_output_1.height = 140.0, 100.0
			accumulate_field_001.width, accumulate_field_001.height = 140.0, 100.0
			group.width, group.height = 282.89483642578125, 100.0
			
			#initialize _mn_utils_aa_atom_pos links
			#group_input_1.atom_name -> compare.B
			_mn_utils_aa_atom_pos.links.new(group_input_1.outputs[0], compare.inputs[3])
			#named_attribute.Attribute -> compare.A
			_mn_utils_aa_atom_pos.links.new(named_attribute.outputs[0], compare.inputs[2])
			#reroute.Output -> group_output_1.Group Index
			_mn_utils_aa_atom_pos.links.new(reroute.outputs[0], group_output_1.inputs[1])
			#named_attribute.Attribute -> compare_002.A
			_mn_utils_aa_atom_pos.links.new(named_attribute.outputs[0], compare_002.inputs[2])
			#compare_002.Result -> accumulate_field_001.Value
			_mn_utils_aa_atom_pos.links.new(compare_002.outputs[0], accumulate_field_001.inputs[0])
			#named_attribute.Attribute -> compare_001.A
			_mn_utils_aa_atom_pos.links.new(named_attribute.outputs[0], compare_001.inputs[2])
			#named_attribute.Attribute -> compare_003.A
			_mn_utils_aa_atom_pos.links.new(named_attribute.outputs[0], compare_003.inputs[2])
			#group_input_1.atom_name -> compare_004.A
			_mn_utils_aa_atom_pos.links.new(group_input_1.outputs[0], compare_004.inputs[2])
			#compare_004.Result -> switch_005.Switch
			_mn_utils_aa_atom_pos.links.new(compare_004.outputs[0], switch_005.inputs[0])
			#mix.Result -> switch_005.False
			_mn_utils_aa_atom_pos.links.new(mix.outputs[1], switch_005.inputs[1])
			#switch_005.Output -> group_output_1.Position
			_mn_utils_aa_atom_pos.links.new(switch_005.outputs[0], group_output_1.inputs[0])
			#compare.Result -> group.Selection
			_mn_utils_aa_atom_pos.links.new(compare.outputs[0], group.inputs[0])
			#reroute.Output -> group.Group Index
			_mn_utils_aa_atom_pos.links.new(reroute.outputs[0], group.inputs[1])
			#named_attribute_001.Attribute -> group.Float
			_mn_utils_aa_atom_pos.links.new(named_attribute_001.outputs[0], group.inputs[2])
			#group.Float -> group_output_1.b_factor
			_mn_utils_aa_atom_pos.links.new(group.outputs[1], group_output_1.inputs[2])
			#position_001.Position -> group.Vector
			_mn_utils_aa_atom_pos.links.new(position_001.outputs[0], group.inputs[3])
			#group.Vector -> switch_005.True
			_mn_utils_aa_atom_pos.links.new(group.outputs[2], switch_005.inputs[2])
			#compare_003.Result -> group_001.Selection
			_mn_utils_aa_atom_pos.links.new(compare_003.outputs[0], group_001.inputs[0])
			#reroute.Output -> group_001.Group Index
			_mn_utils_aa_atom_pos.links.new(reroute.outputs[0], group_001.inputs[1])
			#group_001.Vector -> mix.A
			_mn_utils_aa_atom_pos.links.new(group_001.outputs[2], mix.inputs[4])
			#reroute.Output -> group_002.Group Index
			_mn_utils_aa_atom_pos.links.new(reroute.outputs[0], group_002.inputs[1])
			#compare_001.Result -> group_002.Selection
			_mn_utils_aa_atom_pos.links.new(compare_001.outputs[0], group_002.inputs[0])
			#group_002.Vector -> mix.B
			_mn_utils_aa_atom_pos.links.new(group_002.outputs[2], mix.inputs[5])
			#position_002.Position -> group_001.Vector
			_mn_utils_aa_atom_pos.links.new(position_002.outputs[0], group_001.inputs[3])
			#position_002.Position -> group_002.Vector
			_mn_utils_aa_atom_pos.links.new(position_002.outputs[0], group_002.inputs[3])
			#index_1.Index -> edges_of_vertex.Vertex Index
			_mn_utils_aa_atom_pos.links.new(index_1.outputs[0], edges_of_vertex.inputs[0])
			#edges_of_vertex.Total -> group.Integer
			_mn_utils_aa_atom_pos.links.new(edges_of_vertex.outputs[1], group.inputs[6])
			#group.Integer -> group_output_1.Integer
			_mn_utils_aa_atom_pos.links.new(group.outputs[5], group_output_1.inputs[3])
			#accumulate_field_001.Leading -> reroute.Input
			_mn_utils_aa_atom_pos.links.new(accumulate_field_001.outputs[0], reroute.inputs[0])
			return _mn_utils_aa_atom_pos

		_mn_utils_aa_atom_pos = _mn_utils_aa_atom_pos_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".MN_utils_aa_atom_pos", type = 'NODES')
		mod.node_group = _mn_utils_aa_atom_pos
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_MN_utils_aa_atom_pos.bl_idname)
			
def register():
	bpy.utils.register_class(_MN_utils_aa_atom_pos)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_MN_utils_aa_atom_pos)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
