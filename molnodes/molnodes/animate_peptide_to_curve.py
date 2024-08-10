bl_info = {
	"name" : "Animate Peptide to Curve",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Animate_Peptide_to_Curve(bpy.types.Operator):
	bl_idname = "node.animate_peptide_to_curve"
	bl_label = "Animate Peptide to Curve"
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

		#initialize mn_utils_curve_resample node group
		def mn_utils_curve_resample_node_group():
			mn_utils_curve_resample = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "MN_utils_curve_resample")

			mn_utils_curve_resample.color_tag = 'NONE'
			mn_utils_curve_resample.description = ""

			mn_utils_curve_resample.is_modifier = True
			
			#mn_utils_curve_resample interface
			#Socket Geometry
			geometry_socket = mn_utils_curve_resample.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket.attribute_domain = 'POINT'
			
			#Socket Position
			position_socket_1 = mn_utils_curve_resample.interface.new_socket(name = "Position", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			position_socket_1.subtype = 'NONE'
			position_socket_1.default_value = (0.0, 0.0, 0.0)
			position_socket_1.min_value = -3.4028234663852886e+38
			position_socket_1.max_value = 3.4028234663852886e+38
			position_socket_1.attribute_domain = 'POINT'
			
			#Socket Tangent
			tangent_socket = mn_utils_curve_resample.interface.new_socket(name = "Tangent", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			tangent_socket.subtype = 'NONE'
			tangent_socket.default_value = (0.0, 0.0, 0.0)
			tangent_socket.min_value = -3.4028234663852886e+38
			tangent_socket.max_value = 3.4028234663852886e+38
			tangent_socket.attribute_domain = 'POINT'
			
			#Socket Normal
			normal_socket = mn_utils_curve_resample.interface.new_socket(name = "Normal", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			normal_socket.subtype = 'NONE'
			normal_socket.default_value = (0.0, 0.0, 0.0)
			normal_socket.min_value = -3.4028234663852886e+38
			normal_socket.max_value = 3.4028234663852886e+38
			normal_socket.attribute_domain = 'POINT'
			
			#Socket Field Float
			field_float_socket = mn_utils_curve_resample.interface.new_socket(name = "Field Float", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			field_float_socket.subtype = 'NONE'
			field_float_socket.default_value = 0.0
			field_float_socket.min_value = -3.4028234663852886e+38
			field_float_socket.max_value = 3.4028234663852886e+38
			field_float_socket.attribute_domain = 'POINT'
			
			#Socket Field Int
			field_int_socket = mn_utils_curve_resample.interface.new_socket(name = "Field Int", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			field_int_socket.subtype = 'NONE'
			field_int_socket.default_value = 0
			field_int_socket.min_value = -2147483648
			field_int_socket.max_value = 2147483647
			field_int_socket.attribute_domain = 'POINT'
			
			#Socket Field Vec
			field_vec_socket = mn_utils_curve_resample.interface.new_socket(name = "Field Vec", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			field_vec_socket.subtype = 'NONE'
			field_vec_socket.default_value = (0.0, 0.0, 0.0)
			field_vec_socket.min_value = -3.4028234663852886e+38
			field_vec_socket.max_value = 3.4028234663852886e+38
			field_vec_socket.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_1 = mn_utils_curve_resample.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_1.attribute_domain = 'POINT'
			
			#Socket Offset
			offset_socket = mn_utils_curve_resample.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketFloat')
			offset_socket.subtype = 'NONE'
			offset_socket.default_value = 2.299999952316284
			offset_socket.min_value = -10000.0
			offset_socket.max_value = 10000.0
			offset_socket.attribute_domain = 'POINT'
			
			#Socket Length
			length_socket = mn_utils_curve_resample.interface.new_socket(name = "Length", in_out='INPUT', socket_type = 'NodeSocketFloat')
			length_socket.subtype = 'DISTANCE'
			length_socket.default_value = 0.36000001430511475
			length_socket.min_value = 0.009999999776482582
			length_socket.max_value = 3.4028234663852886e+38
			length_socket.attribute_domain = 'POINT'
			
			#Socket Field Float
			field_float_socket_1 = mn_utils_curve_resample.interface.new_socket(name = "Field Float", in_out='INPUT', socket_type = 'NodeSocketFloat')
			field_float_socket_1.subtype = 'NONE'
			field_float_socket_1.default_value = 0.0
			field_float_socket_1.min_value = -3.4028234663852886e+38
			field_float_socket_1.max_value = 3.4028234663852886e+38
			field_float_socket_1.attribute_domain = 'POINT'
			field_float_socket_1.hide_value = True
			
			#Socket Field Int
			field_int_socket_1 = mn_utils_curve_resample.interface.new_socket(name = "Field Int", in_out='INPUT', socket_type = 'NodeSocketInt')
			field_int_socket_1.subtype = 'NONE'
			field_int_socket_1.default_value = 0
			field_int_socket_1.min_value = -2147483648
			field_int_socket_1.max_value = 2147483647
			field_int_socket_1.attribute_domain = 'POINT'
			field_int_socket_1.hide_value = True
			
			#Socket Field Vec
			field_vec_socket_1 = mn_utils_curve_resample.interface.new_socket(name = "Field Vec", in_out='INPUT', socket_type = 'NodeSocketVector')
			field_vec_socket_1.subtype = 'NONE'
			field_vec_socket_1.default_value = (0.0, 0.0, 0.0)
			field_vec_socket_1.min_value = -3.4028234663852886e+38
			field_vec_socket_1.max_value = 3.4028234663852886e+38
			field_vec_socket_1.attribute_domain = 'POINT'
			field_vec_socket_1.hide_value = True
			
			
			#initialize mn_utils_curve_resample nodes
			#node Sample Curve.001
			sample_curve_001 = mn_utils_curve_resample.nodes.new("GeometryNodeSampleCurve")
			sample_curve_001.name = "Sample Curve.001"
			sample_curve_001.data_type = 'INT'
			sample_curve_001.mode = 'LENGTH'
			sample_curve_001.use_all_curves = False
			
			#node Reroute.001
			reroute_001 = mn_utils_curve_resample.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			#node Sample Curve.002
			sample_curve_002 = mn_utils_curve_resample.nodes.new("GeometryNodeSampleCurve")
			sample_curve_002.name = "Sample Curve.002"
			sample_curve_002.data_type = 'FLOAT_VECTOR'
			sample_curve_002.mode = 'LENGTH'
			sample_curve_002.use_all_curves = False
			
			#node Index
			index_2 = mn_utils_curve_resample.nodes.new("GeometryNodeInputIndex")
			index_2.name = "Index"
			
			#node Capture Attribute
			capture_attribute = mn_utils_curve_resample.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute.name = "Capture Attribute"
			capture_attribute.active_index = 0
			capture_attribute.capture_items.clear()
			capture_attribute.capture_items.new('FLOAT', "Value")
			capture_attribute.capture_items["Value"].data_type = 'INT'
			capture_attribute.domain = 'CURVE'
			
			#node Reroute.002
			reroute_002 = mn_utils_curve_resample.nodes.new("NodeReroute")
			reroute_002.name = "Reroute.002"
			#node Resample Curve
			resample_curve = mn_utils_curve_resample.nodes.new("GeometryNodeResampleCurve")
			resample_curve.name = "Resample Curve"
			resample_curve.mode = 'LENGTH'
			#Selection
			resample_curve.inputs[1].default_value = True
			
			#node Group Output
			group_output_2 = mn_utils_curve_resample.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Set Position
			set_position = mn_utils_curve_resample.nodes.new("GeometryNodeSetPosition")
			set_position.name = "Set Position"
			#Selection
			set_position.inputs[1].default_value = True
			#Offset
			set_position.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Reroute
			reroute_1 = mn_utils_curve_resample.nodes.new("NodeReroute")
			reroute_1.name = "Reroute"
			#node Resample Curve.001
			resample_curve_001 = mn_utils_curve_resample.nodes.new("GeometryNodeResampleCurve")
			resample_curve_001.name = "Resample Curve.001"
			resample_curve_001.mode = 'COUNT'
			#Selection
			resample_curve_001.inputs[1].default_value = True
			
			#node Sample Curve
			sample_curve = mn_utils_curve_resample.nodes.new("GeometryNodeSampleCurve")
			sample_curve.name = "Sample Curve"
			sample_curve.data_type = 'FLOAT'
			sample_curve.mode = 'LENGTH'
			sample_curve.use_all_curves = False
			
			#node Group Input
			group_input_2 = mn_utils_curve_resample.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
			#node Reroute.003
			reroute_003 = mn_utils_curve_resample.nodes.new("NodeReroute")
			reroute_003.name = "Reroute.003"
			#node Spline Length.001
			spline_length_001 = mn_utils_curve_resample.nodes.new("GeometryNodeSplineLength")
			spline_length_001.name = "Spline Length.001"
			
			#node Math
			math = mn_utils_curve_resample.nodes.new("ShaderNodeMath")
			math.label = "x - 1"
			math.name = "Math"
			math.hide = True
			math.operation = 'SUBTRACT'
			math.use_clamp = False
			#Value_001
			math.inputs[1].default_value = 1.0
			
			#node Math.001
			math_001 = mn_utils_curve_resample.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.operation = 'WRAP'
			math_001.use_clamp = False
			#Value_002
			math_001.inputs[2].default_value = 0.0
			
			#node Spline Length
			spline_length = mn_utils_curve_resample.nodes.new("GeometryNodeSplineLength")
			spline_length.name = "Spline Length"
			
			#node Math.002
			math_002 = mn_utils_curve_resample.nodes.new("ShaderNodeMath")
			math_002.name = "Math.002"
			math_002.operation = 'ADD'
			math_002.use_clamp = False
			
			#node Compare
			compare_1 = mn_utils_curve_resample.nodes.new("FunctionNodeCompare")
			compare_1.name = "Compare"
			compare_1.data_type = 'FLOAT'
			compare_1.mode = 'ELEMENT'
			compare_1.operation = 'EQUAL'
			#B
			compare_1.inputs[1].default_value = 0.0
			#Epsilon
			compare_1.inputs[12].default_value = 0.0010000000474974513
			
			#node Switch
			switch = mn_utils_curve_resample.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'FLOAT'
			
			#node Accumulate Field
			accumulate_field = mn_utils_curve_resample.nodes.new("GeometryNodeAccumulateField")
			accumulate_field.name = "Accumulate Field"
			accumulate_field.data_type = 'FLOAT'
			accumulate_field.domain = 'POINT'
			
			
			
			
			#Set locations
			sample_curve_001.location = (280.0, -160.0)
			reroute_001.location = (170.41610717773438, 56.029422760009766)
			sample_curve_002.location = (280.0, -460.0)
			index_2.location = (-468.85321044921875, -335.7737121582031)
			capture_attribute.location = (-466.8502197265625, -142.71517944335938)
			reroute_002.location = (-754.80029296875, -226.68231201171875)
			resample_curve.location = (-641.0833129882812, -111.3865966796875)
			group_output_2.location = (1082.3330078125, -91.4212875366211)
			set_position.location = (800.173095703125, -100.55831909179688)
			reroute_1.location = (75.4967041015625, -163.95921325683594)
			resample_curve_001.location = (526.7703247070312, -109.56268310546875)
			sample_curve.location = (260.0, 220.0)
			group_input_2.location = (-1054.9755859375, -86.68230438232422)
			reroute_003.location = (-498.3427429199219, 182.15419006347656)
			spline_length_001.location = (520.0, -320.0)
			math.location = (540.0, -280.0)
			math_001.location = (-60.0, 640.0)
			spline_length.location = (-60.0, 720.0)
			math_002.location = (-280.0, 620.0)
			compare_1.location = (-316.9455871582031, 279.42132568359375)
			switch.location = (-40.0, 280.0)
			accumulate_field.location = (-523.4389038085938, 432.5602722167969)
			
			#Set dimensions
			sample_curve_001.width, sample_curve_001.height = 140.0, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			sample_curve_002.width, sample_curve_002.height = 140.0, 100.0
			index_2.width, index_2.height = 140.0, 100.0
			capture_attribute.width, capture_attribute.height = 140.0, 100.0
			reroute_002.width, reroute_002.height = 16.0, 100.0
			resample_curve.width, resample_curve.height = 140.0, 100.0
			group_output_2.width, group_output_2.height = 140.0, 100.0
			set_position.width, set_position.height = 140.0, 100.0
			reroute_1.width, reroute_1.height = 16.0, 100.0
			resample_curve_001.width, resample_curve_001.height = 140.0, 100.0
			sample_curve.width, sample_curve.height = 140.0, 100.0
			group_input_2.width, group_input_2.height = 140.0, 100.0
			reroute_003.width, reroute_003.height = 16.0, 100.0
			spline_length_001.width, spline_length_001.height = 151.61087036132812, 100.0
			math.width, math.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			spline_length.width, spline_length.height = 140.0, 100.0
			math_002.width, math_002.height = 140.0, 100.0
			compare_1.width, compare_1.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			accumulate_field.width, accumulate_field.height = 140.0, 100.0
			
			#initialize mn_utils_curve_resample links
			#group_input_2.Geometry -> resample_curve.Curve
			mn_utils_curve_resample.links.new(group_input_2.outputs[0], resample_curve.inputs[0])
			#set_position.Geometry -> group_output_2.Geometry
			mn_utils_curve_resample.links.new(set_position.outputs[0], group_output_2.inputs[0])
			#group_input_2.Length -> reroute_002.Input
			mn_utils_curve_resample.links.new(group_input_2.outputs[2], reroute_002.inputs[0])
			#reroute_1.Output -> sample_curve.Curves
			mn_utils_curve_resample.links.new(reroute_1.outputs[0], sample_curve.inputs[0])
			#reroute_001.Output -> sample_curve.Length
			mn_utils_curve_resample.links.new(reroute_001.outputs[0], sample_curve.inputs[3])
			#sample_curve.Position -> set_position.Position
			mn_utils_curve_resample.links.new(sample_curve.outputs[1], set_position.inputs[2])
			#resample_curve.Curve -> capture_attribute.Geometry
			mn_utils_curve_resample.links.new(resample_curve.outputs[0], capture_attribute.inputs[0])
			#index_2.Index -> capture_attribute.Value
			mn_utils_curve_resample.links.new(index_2.outputs[0], capture_attribute.inputs[1])
			#capture_attribute.Geometry -> reroute_1.Input
			mn_utils_curve_resample.links.new(capture_attribute.outputs[0], reroute_1.inputs[0])
			#capture_attribute.Value -> sample_curve.Curve Index
			mn_utils_curve_resample.links.new(capture_attribute.outputs[1], sample_curve.inputs[4])
			#capture_attribute.Value -> accumulate_field.Group ID
			mn_utils_curve_resample.links.new(capture_attribute.outputs[1], accumulate_field.inputs[1])
			#reroute_002.Output -> resample_curve.Length
			mn_utils_curve_resample.links.new(reroute_002.outputs[0], resample_curve.inputs[3])
			#reroute_002.Output -> accumulate_field.Value
			mn_utils_curve_resample.links.new(reroute_002.outputs[0], accumulate_field.inputs[0])
			#reroute_1.Output -> sample_curve_001.Curves
			mn_utils_curve_resample.links.new(reroute_1.outputs[0], sample_curve_001.inputs[0])
			#reroute_001.Output -> sample_curve_001.Length
			mn_utils_curve_resample.links.new(reroute_001.outputs[0], sample_curve_001.inputs[3])
			#capture_attribute.Value -> sample_curve_001.Curve Index
			mn_utils_curve_resample.links.new(capture_attribute.outputs[1], sample_curve_001.inputs[4])
			#sample_curve.Position -> group_output_2.Position
			mn_utils_curve_resample.links.new(sample_curve.outputs[1], group_output_2.inputs[1])
			#sample_curve.Tangent -> group_output_2.Tangent
			mn_utils_curve_resample.links.new(sample_curve.outputs[2], group_output_2.inputs[2])
			#sample_curve.Normal -> group_output_2.Normal
			mn_utils_curve_resample.links.new(sample_curve.outputs[3], group_output_2.inputs[3])
			#sample_curve.Value -> group_output_2.Field Float
			mn_utils_curve_resample.links.new(sample_curve.outputs[0], group_output_2.inputs[4])
			#group_input_2.Field Float -> sample_curve.Value
			mn_utils_curve_resample.links.new(group_input_2.outputs[3], sample_curve.inputs[1])
			#sample_curve_001.Value -> group_output_2.Field Int
			mn_utils_curve_resample.links.new(sample_curve_001.outputs[0], group_output_2.inputs[5])
			#group_input_2.Field Int -> sample_curve_001.Value
			mn_utils_curve_resample.links.new(group_input_2.outputs[4], sample_curve_001.inputs[1])
			#reroute_1.Output -> sample_curve_002.Curves
			mn_utils_curve_resample.links.new(reroute_1.outputs[0], sample_curve_002.inputs[0])
			#reroute_001.Output -> sample_curve_002.Length
			mn_utils_curve_resample.links.new(reroute_001.outputs[0], sample_curve_002.inputs[3])
			#capture_attribute.Value -> sample_curve_002.Curve Index
			mn_utils_curve_resample.links.new(capture_attribute.outputs[1], sample_curve_002.inputs[4])
			#sample_curve_002.Value -> group_output_2.Field Vec
			mn_utils_curve_resample.links.new(sample_curve_002.outputs[0], group_output_2.inputs[6])
			#group_input_2.Field Vec -> sample_curve_002.Value
			mn_utils_curve_resample.links.new(group_input_2.outputs[5], sample_curve_002.inputs[1])
			#reroute_1.Output -> resample_curve_001.Curve
			mn_utils_curve_resample.links.new(reroute_1.outputs[0], resample_curve_001.inputs[0])
			#resample_curve_001.Curve -> set_position.Geometry
			mn_utils_curve_resample.links.new(resample_curve_001.outputs[0], set_position.inputs[0])
			#math.Value -> resample_curve_001.Count
			mn_utils_curve_resample.links.new(math.outputs[0], resample_curve_001.inputs[2])
			#math_002.Value -> math_001.Value
			mn_utils_curve_resample.links.new(math_002.outputs[0], math_001.inputs[0])
			#spline_length.Length -> math_001.Value
			mn_utils_curve_resample.links.new(spline_length.outputs[0], math_001.inputs[1])
			#accumulate_field.Trailing -> math_002.Value
			mn_utils_curve_resample.links.new(accumulate_field.outputs[1], math_002.inputs[0])
			#reroute_003.Output -> math_002.Value
			mn_utils_curve_resample.links.new(reroute_003.outputs[0], math_002.inputs[1])
			#compare_1.Result -> switch.Switch
			mn_utils_curve_resample.links.new(compare_1.outputs[0], switch.inputs[0])
			#group_input_2.Offset -> reroute_003.Input
			mn_utils_curve_resample.links.new(group_input_2.outputs[1], reroute_003.inputs[0])
			#reroute_003.Output -> compare_1.A
			mn_utils_curve_resample.links.new(reroute_003.outputs[0], compare_1.inputs[0])
			#spline_length_001.Point Count -> math.Value
			mn_utils_curve_resample.links.new(spline_length_001.outputs[1], math.inputs[0])
			#switch.Output -> reroute_001.Input
			mn_utils_curve_resample.links.new(switch.outputs[0], reroute_001.inputs[0])
			#math_001.Value -> switch.False
			mn_utils_curve_resample.links.new(math_001.outputs[0], switch.inputs[1])
			#accumulate_field.Trailing -> switch.True
			mn_utils_curve_resample.links.new(accumulate_field.outputs[1], switch.inputs[2])
			return mn_utils_curve_resample

		mn_utils_curve_resample = mn_utils_curve_resample_node_group()

		#initialize animate_peptide_to_curve node group
		def animate_peptide_to_curve_node_group():
			animate_peptide_to_curve = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Animate Peptide to Curve")

			animate_peptide_to_curve.color_tag = 'GEOMETRY'
			animate_peptide_to_curve.description = ""

			animate_peptide_to_curve.is_modifier = True
			
			#animate_peptide_to_curve interface
			#Socket Atoms
			atoms_socket = animate_peptide_to_curve.interface.new_socket(name = "Atoms", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket_1 = animate_peptide_to_curve.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_1.attribute_domain = 'POINT'
			atoms_socket_1.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Curve
			curve_socket = animate_peptide_to_curve.interface.new_socket(name = "Curve", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			curve_socket.attribute_domain = 'POINT'
			
			#Socket Offset
			offset_socket_1 = animate_peptide_to_curve.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketFloat')
			offset_socket_1.subtype = 'NONE'
			offset_socket_1.default_value = 0.0
			offset_socket_1.min_value = -10000.0
			offset_socket_1.max_value = 10000.0
			offset_socket_1.attribute_domain = 'POINT'
			
			#Socket Start
			start_socket = animate_peptide_to_curve.interface.new_socket(name = "Start", in_out='INPUT', socket_type = 'NodeSocketFloat')
			start_socket.subtype = 'FACTOR'
			start_socket.default_value = 0.0
			start_socket.min_value = 0.0
			start_socket.max_value = 1.0
			start_socket.attribute_domain = 'POINT'
			
			#Socket End
			end_socket = animate_peptide_to_curve.interface.new_socket(name = "End", in_out='INPUT', socket_type = 'NodeSocketFloat')
			end_socket.subtype = 'FACTOR'
			end_socket.default_value = 1.0
			end_socket.min_value = 0.0
			end_socket.max_value = 1.0
			end_socket.attribute_domain = 'POINT'
			
			#Socket Rotate
			rotate_socket = animate_peptide_to_curve.interface.new_socket(name = "Rotate", in_out='INPUT', socket_type = 'NodeSocketFloat')
			rotate_socket.subtype = 'NONE'
			rotate_socket.default_value = 0.5
			rotate_socket.min_value = -10000.0
			rotate_socket.max_value = 10000.0
			rotate_socket.attribute_domain = 'POINT'
			
			#Socket Twist
			twist_socket = animate_peptide_to_curve.interface.new_socket(name = "Twist", in_out='INPUT', socket_type = 'NodeSocketFloat')
			twist_socket.subtype = 'NONE'
			twist_socket.default_value = 1.0
			twist_socket.min_value = -10000.0
			twist_socket.max_value = 10000.0
			twist_socket.attribute_domain = 'POINT'
			
			
			#initialize animate_peptide_to_curve nodes
			#node Frame
			frame_1 = animate_peptide_to_curve.nodes.new("NodeFrame")
			frame_1.label = "Initial setup and alignment of amino acids"
			frame_1.name = "Frame"
			frame_1.label_size = 20
			frame_1.shrink = True
			
			#node Frame.001
			frame_001 = animate_peptide_to_curve.nodes.new("NodeFrame")
			frame_001.label = "Placing and Aligning AA Along the Curve"
			frame_001.name = "Frame.001"
			frame_001.label_size = 20
			frame_001.shrink = True
			
			#node Group Output
			group_output_3 = animate_peptide_to_curve.nodes.new("NodeGroupOutput")
			group_output_3.name = "Group Output"
			group_output_3.is_active_output = True
			
			#node Vector Math
			vector_math = animate_peptide_to_curve.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.operation = 'SCALE'
			#Scale
			vector_math.inputs[3].default_value = -1.0
			
			#node Position
			position = animate_peptide_to_curve.nodes.new("GeometryNodeInputPosition")
			position.name = "Position"
			
			#node Vector Rotate.005
			vector_rotate_005 = animate_peptide_to_curve.nodes.new("ShaderNodeVectorRotate")
			vector_rotate_005.name = "Vector Rotate.005"
			vector_rotate_005.invert = True
			vector_rotate_005.rotation_type = 'Y_AXIS'
			#Center
			vector_rotate_005.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Angle
			vector_rotate_005.inputs[3].default_value = -0.5574581623077393
			
			#node Group.007
			group_007 = animate_peptide_to_curve.nodes.new("GeometryNodeGroup")
			group_007.name = "Group.007"
			group_007.node_tree = _mn_utils_aa_atom_pos
			#Input_2
			group_007.inputs[0].default_value = 1
			
			#node Set Position.006
			set_position_006 = animate_peptide_to_curve.nodes.new("GeometryNodeSetPosition")
			set_position_006.name = "Set Position.006"
			#Selection
			set_position_006.inputs[1].default_value = True
			#Offset
			set_position_006.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Set Position.005
			set_position_005 = animate_peptide_to_curve.nodes.new("GeometryNodeSetPosition")
			set_position_005.name = "Set Position.005"
			#Selection
			set_position_005.inputs[1].default_value = True
			#Offset
			set_position_005.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Group.011
			group_011 = animate_peptide_to_curve.nodes.new("GeometryNodeGroup")
			group_011.name = "Group.011"
			group_011.node_tree = _mn_utils_aa_atom_pos
			#Input_2
			group_011.inputs[0].default_value = 4
			
			#node Align Euler to Vector.002
			align_euler_to_vector_002 = animate_peptide_to_curve.nodes.new("FunctionNodeAlignEulerToVector")
			align_euler_to_vector_002.name = "Align Euler to Vector.002"
			align_euler_to_vector_002.axis = 'Z'
			align_euler_to_vector_002.pivot_axis = 'X'
			#Rotation
			align_euler_to_vector_002.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Factor
			align_euler_to_vector_002.inputs[1].default_value = 1.0
			
			#node Vector Rotate.004
			vector_rotate_004 = animate_peptide_to_curve.nodes.new("ShaderNodeVectorRotate")
			vector_rotate_004.name = "Vector Rotate.004"
			vector_rotate_004.invert = True
			vector_rotate_004.rotation_type = 'EULER_XYZ'
			#Center
			vector_rotate_004.inputs[1].default_value = (0.0, 0.0, 0.0)
			
			#node Vector Rotate
			vector_rotate = animate_peptide_to_curve.nodes.new("ShaderNodeVectorRotate")
			vector_rotate.name = "Vector Rotate"
			vector_rotate.invert = True
			vector_rotate.rotation_type = 'EULER_XYZ'
			#Center
			vector_rotate.inputs[1].default_value = (0.0, 0.0, 0.0)
			
			#node Set Position.004
			set_position_004 = animate_peptide_to_curve.nodes.new("GeometryNodeSetPosition")
			set_position_004.name = "Set Position.004"
			#Selection
			set_position_004.inputs[1].default_value = True
			#Offset
			set_position_004.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Vector Math.001
			vector_math_001 = animate_peptide_to_curve.nodes.new("ShaderNodeVectorMath")
			vector_math_001.name = "Vector Math.001"
			vector_math_001.operation = 'SUBTRACT'
			
			#node Align Euler to Vector
			align_euler_to_vector = animate_peptide_to_curve.nodes.new("FunctionNodeAlignEulerToVector")
			align_euler_to_vector.name = "Align Euler to Vector"
			align_euler_to_vector.axis = 'X'
			align_euler_to_vector.pivot_axis = 'AUTO'
			#Rotation
			align_euler_to_vector.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Factor
			align_euler_to_vector.inputs[1].default_value = 1.0
			
			#node Set Position
			set_position_1 = animate_peptide_to_curve.nodes.new("GeometryNodeSetPosition")
			set_position_1.name = "Set Position"
			#Selection
			set_position_1.inputs[1].default_value = True
			#Position
			set_position_1.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Reroute.001
			reroute_001_1 = animate_peptide_to_curve.nodes.new("NodeReroute")
			reroute_001_1.name = "Reroute.001"
			#node Separate Geometry.001
			separate_geometry_001 = animate_peptide_to_curve.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_001.name = "Separate Geometry.001"
			separate_geometry_001.domain = 'POINT'
			
			#node Compare.001
			compare_001_1 = animate_peptide_to_curve.nodes.new("FunctionNodeCompare")
			compare_001_1.name = "Compare.001"
			compare_001_1.hide = True
			compare_001_1.data_type = 'INT'
			compare_001_1.mode = 'ELEMENT'
			compare_001_1.operation = 'LESS_THAN'
			
			#node Group Input
			group_input_3 = animate_peptide_to_curve.nodes.new("NodeGroupInput")
			group_input_3.name = "Group Input"
			
			#node Trim Curve
			trim_curve = animate_peptide_to_curve.nodes.new("GeometryNodeTrimCurve")
			trim_curve.name = "Trim Curve"
			trim_curve.mode = 'FACTOR'
			#Selection
			trim_curve.inputs[1].default_value = True
			
			#node Math.002
			math_002_1 = animate_peptide_to_curve.nodes.new("ShaderNodeMath")
			math_002_1.name = "Math.002"
			math_002_1.operation = 'DIVIDE'
			math_002_1.use_clamp = False
			#Value
			math_002_1.inputs[0].default_value = 3.129999876022339
			#Value_001
			math_002_1.inputs[1].default_value = 100.0
			
			#node Sample Index
			sample_index = animate_peptide_to_curve.nodes.new("GeometryNodeSampleIndex")
			sample_index.name = "Sample Index"
			sample_index.hide = True
			sample_index.clamp = False
			sample_index.data_type = 'FLOAT_VECTOR'
			sample_index.domain = 'POINT'
			
			#node Reroute.002
			reroute_002_1 = animate_peptide_to_curve.nodes.new("NodeReroute")
			reroute_002_1.name = "Reroute.002"
			#node Sample Index.001
			sample_index_001 = animate_peptide_to_curve.nodes.new("GeometryNodeSampleIndex")
			sample_index_001.name = "Sample Index.001"
			sample_index_001.hide = True
			sample_index_001.clamp = False
			sample_index_001.data_type = 'FLOAT_VECTOR'
			sample_index_001.domain = 'POINT'
			
			#node Set Curve Tilt
			set_curve_tilt = animate_peptide_to_curve.nodes.new("GeometryNodeSetCurveTilt")
			set_curve_tilt.name = "Set Curve Tilt"
			#Selection
			set_curve_tilt.inputs[1].default_value = True
			
			#node Curve Tilt
			curve_tilt = animate_peptide_to_curve.nodes.new("GeometryNodeInputCurveTilt")
			curve_tilt.name = "Curve Tilt"
			
			#node Sample Index.002
			sample_index_002 = animate_peptide_to_curve.nodes.new("GeometryNodeSampleIndex")
			sample_index_002.name = "Sample Index.002"
			sample_index_002.clamp = False
			sample_index_002.data_type = 'FLOAT'
			sample_index_002.domain = 'POINT'
			
			#node Math
			math_1 = animate_peptide_to_curve.nodes.new("ShaderNodeMath")
			math_1.name = "Math"
			math_1.operation = 'ADD'
			math_1.use_clamp = False
			
			#node Domain Size
			domain_size = animate_peptide_to_curve.nodes.new("GeometryNodeAttributeDomainSize")
			domain_size.name = "Domain Size"
			domain_size.hide = True
			domain_size.component = 'CURVE'
			
			#node Accumulate Field.002
			accumulate_field_002_1 = animate_peptide_to_curve.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_002_1.name = "Accumulate Field.002"
			accumulate_field_002_1.data_type = 'FLOAT'
			accumulate_field_002_1.domain = 'POINT'
			#Group Index
			accumulate_field_002_1.inputs[1].default_value = 0
			
			#node Math.001
			math_001_1 = animate_peptide_to_curve.nodes.new("ShaderNodeMath")
			math_001_1.name = "Math.001"
			math_001_1.operation = 'MULTIPLY'
			math_001_1.use_clamp = False
			#Value
			math_001_1.inputs[0].default_value = 1.5707963705062866
			
			#node Reroute
			reroute_2 = animate_peptide_to_curve.nodes.new("NodeReroute")
			reroute_2.name = "Reroute"
			#node Reroute.003
			reroute_003_1 = animate_peptide_to_curve.nodes.new("NodeReroute")
			reroute_003_1.name = "Reroute.003"
			#node Reroute.004
			reroute_004 = animate_peptide_to_curve.nodes.new("NodeReroute")
			reroute_004.name = "Reroute.004"
			#node Vector Rotate.007
			vector_rotate_007 = animate_peptide_to_curve.nodes.new("ShaderNodeVectorRotate")
			vector_rotate_007.name = "Vector Rotate.007"
			vector_rotate_007.invert = False
			vector_rotate_007.rotation_type = 'AXIS_ANGLE'
			
			#node Align Euler to Vector.003
			align_euler_to_vector_003 = animate_peptide_to_curve.nodes.new("FunctionNodeAlignEulerToVector")
			align_euler_to_vector_003.name = "Align Euler to Vector.003"
			align_euler_to_vector_003.axis = 'X'
			align_euler_to_vector_003.pivot_axis = 'AUTO'
			#Rotation
			align_euler_to_vector_003.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Factor
			align_euler_to_vector_003.inputs[1].default_value = 1.0
			
			#node Vector Rotate.006
			vector_rotate_006 = animate_peptide_to_curve.nodes.new("ShaderNodeVectorRotate")
			vector_rotate_006.name = "Vector Rotate.006"
			vector_rotate_006.invert = False
			vector_rotate_006.rotation_type = 'EULER_XYZ'
			
			#node Set Position.009
			set_position_009 = animate_peptide_to_curve.nodes.new("GeometryNodeSetPosition")
			set_position_009.name = "Set Position.009"
			#Selection
			set_position_009.inputs[1].default_value = True
			#Offset
			set_position_009.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Set Position.008
			set_position_008 = animate_peptide_to_curve.nodes.new("GeometryNodeSetPosition")
			set_position_008.name = "Set Position.008"
			#Selection
			set_position_008.inputs[1].default_value = True
			#Offset
			set_position_008.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Vector Math.006
			vector_math_006 = animate_peptide_to_curve.nodes.new("ShaderNodeVectorMath")
			vector_math_006.name = "Vector Math.006"
			vector_math_006.hide = True
			vector_math_006.operation = 'SCALE'
			#Scale
			vector_math_006.inputs[3].default_value = -1.0
			
			#node Position.002
			position_002_1 = animate_peptide_to_curve.nodes.new("GeometryNodeInputPosition")
			position_002_1.name = "Position.002"
			
			#node Set Position.007
			set_position_007 = animate_peptide_to_curve.nodes.new("GeometryNodeSetPosition")
			set_position_007.name = "Set Position.007"
			#Selection
			set_position_007.inputs[1].default_value = True
			#Position
			set_position_007.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Vector Math.003
			vector_math_003 = animate_peptide_to_curve.nodes.new("ShaderNodeVectorMath")
			vector_math_003.name = "Vector Math.003"
			vector_math_003.operation = 'SUBTRACT'
			
			#node Group
			group_1 = animate_peptide_to_curve.nodes.new("GeometryNodeGroup")
			group_1.name = "Group"
			group_1.node_tree = mn_utils_curve_resample
			#Input_7
			group_1.inputs[3].default_value = 0.0
			#Input_9
			group_1.inputs[4].default_value = 0
			#Input_11
			group_1.inputs[5].default_value = (0.0, 0.0, 0.0)
			
			#node Group.008
			group_008 = animate_peptide_to_curve.nodes.new("GeometryNodeGroup")
			group_008.name = "Group.008"
			group_008.node_tree = _mn_utils_aa_atom_pos
			#Input_2
			group_008.inputs[0].default_value = 3
			
			
			
			#Set parents
			vector_math.parent = frame_1
			position.parent = frame_1
			vector_rotate_005.parent = frame_1
			group_007.parent = frame_1
			set_position_006.parent = frame_1
			set_position_005.parent = frame_1
			group_011.parent = frame_1
			align_euler_to_vector_002.parent = frame_1
			vector_rotate_004.parent = frame_1
			vector_rotate.parent = frame_1
			set_position_004.parent = frame_1
			vector_math_001.parent = frame_1
			align_euler_to_vector.parent = frame_1
			set_position_1.parent = frame_1
			reroute_001_1.parent = frame_1
			separate_geometry_001.parent = frame_1
			compare_001_1.parent = frame_1
			reroute_004.parent = frame_001
			vector_rotate_007.parent = frame_001
			align_euler_to_vector_003.parent = frame_001
			vector_rotate_006.parent = frame_001
			set_position_009.parent = frame_001
			set_position_008.parent = frame_001
			vector_math_006.parent = frame_001
			position_002_1.parent = frame_001
			set_position_007.parent = frame_001
			vector_math_003.parent = frame_001
			group_008.parent = frame_1
			
			#Set locations
			frame_1.location = (-27.07716941833496, -126.43952178955078)
			frame_001.location = (-4.24030876159668, 199.41973876953125)
			group_output_3.location = (2359.086181640625, 944.0341796875)
			vector_math.location = (-20.0, 400.0)
			position.location = (180.0, 240.0)
			vector_rotate_005.location = (820.0, 280.0)
			group_007.location = (-440.0, -20.0)
			set_position_006.location = (820.0, 500.0)
			set_position_005.location = (661.3526000976562, 501.8488464355469)
			group_011.location = (80.0, -20.0)
			align_euler_to_vector_002.location = (340.0, -20.0)
			vector_rotate_004.location = (500.0, 240.0)
			vector_rotate.location = (340.0, 240.0)
			set_position_004.location = (180.0, 540.0)
			vector_math_001.location = (-40.0, 135.8946990966797)
			align_euler_to_vector.location = (179.33258056640625, 170.79183959960938)
			set_position_1.location = (-20.0, 540.0)
			reroute_001_1.location = (-453.18798828125, 412.61907958984375)
			separate_geometry_001.location = (-200.0, 540.0)
			compare_001_1.location = (-192.92283630371094, 366.43951416015625)
			group_input_3.location = (-1060.0, 820.0)
			trim_curve.location = (-640.0, 840.0)
			math_002_1.location = (-640.0, 680.0)
			sample_index.location = (20.0, 760.0)
			reroute_002_1.location = (-40.0, 700.0)
			sample_index_001.location = (20.0, 680.0)
			set_curve_tilt.location = (-145.8927001953125, 1117.4552001953125)
			curve_tilt.location = (-145.8927001953125, 977.4552612304688)
			sample_index_002.location = (14.1072998046875, 1117.4552001953125)
			math_1.location = (-425.8927001953125, 1177.4552001953125)
			domain_size.location = (-400.0, 560.0)
			accumulate_field_002_1.location = (-640.0, 1180.0)
			math_001_1.location = (-800.0, 1180.0)
			reroute_2.location = (1260.0, 540.0)
			reroute_003_1.location = (1340.0, 440.0)
			reroute_004.location = (1860.0, 240.0)
			vector_rotate_007.location = (1980.0, 540.0)
			align_euler_to_vector_003.location = (1480.0, 520.0)
			vector_rotate_006.location = (1640.0, 580.0)
			set_position_009.location = (1980.0, 760.0)
			set_position_008.location = (1800.0, 760.0)
			vector_math_006.location = (1480.0, 320.0)
			position_002_1.location = (1480.0, 580.0)
			set_position_007.location = (1620.0, 760.0)
			vector_math_003.location = (1440.0, 780.0)
			group_1.location = (-400.0, 940.0)
			group_008.location = (-440.0, 180.0)
			
			#Set dimensions
			frame_1.width, frame_1.height = 1479.465087890625, 797.2000732421875
			frame_001.width, frame_001.height = 739.9998779296875, 616.1802978515625
			group_output_3.width, group_output_3.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			position.width, position.height = 140.0, 100.0
			vector_rotate_005.width, vector_rotate_005.height = 140.0, 100.0
			group_007.width, group_007.height = 217.1441650390625, 100.0
			set_position_006.width, set_position_006.height = 140.0, 100.0
			set_position_005.width, set_position_005.height = 140.0, 100.0
			group_011.width, group_011.height = 228.5245361328125, 100.0
			align_euler_to_vector_002.width, align_euler_to_vector_002.height = 140.0, 100.0
			vector_rotate_004.width, vector_rotate_004.height = 140.0, 100.0
			vector_rotate.width, vector_rotate.height = 140.0, 100.0
			set_position_004.width, set_position_004.height = 140.0, 100.0
			vector_math_001.width, vector_math_001.height = 140.0, 100.0
			align_euler_to_vector.width, align_euler_to_vector.height = 125.64166259765625, 100.0
			set_position_1.width, set_position_1.height = 140.0, 100.0
			reroute_001_1.width, reroute_001_1.height = 16.0, 100.0
			separate_geometry_001.width, separate_geometry_001.height = 140.0, 100.0
			compare_001_1.width, compare_001_1.height = 140.0, 100.0
			group_input_3.width, group_input_3.height = 140.0, 100.0
			trim_curve.width, trim_curve.height = 140.0, 100.0
			math_002_1.width, math_002_1.height = 140.0, 100.0
			sample_index.width, sample_index.height = 140.0, 100.0
			reroute_002_1.width, reroute_002_1.height = 16.0, 100.0
			sample_index_001.width, sample_index_001.height = 140.0, 100.0
			set_curve_tilt.width, set_curve_tilt.height = 140.0, 100.0
			curve_tilt.width, curve_tilt.height = 140.0, 100.0
			sample_index_002.width, sample_index_002.height = 140.0, 100.0
			math_1.width, math_1.height = 140.0, 100.0
			domain_size.width, domain_size.height = 140.0, 100.0
			accumulate_field_002_1.width, accumulate_field_002_1.height = 140.0, 100.0
			math_001_1.width, math_001_1.height = 140.0, 100.0
			reroute_2.width, reroute_2.height = 16.0, 100.0
			reroute_003_1.width, reroute_003_1.height = 16.0, 100.0
			reroute_004.width, reroute_004.height = 16.0, 100.0
			vector_rotate_007.width, vector_rotate_007.height = 140.0, 100.0
			align_euler_to_vector_003.width, align_euler_to_vector_003.height = 140.0, 100.0
			vector_rotate_006.width, vector_rotate_006.height = 140.0, 100.0
			set_position_009.width, set_position_009.height = 140.0, 100.0
			set_position_008.width, set_position_008.height = 140.0, 100.0
			vector_math_006.width, vector_math_006.height = 140.0, 100.0
			position_002_1.width, position_002_1.height = 140.0, 100.0
			set_position_007.width, set_position_007.height = 140.0, 100.0
			vector_math_003.width, vector_math_003.height = 140.0, 100.0
			group_1.width, group_1.height = 200.0, 100.0
			group_008.width, group_008.height = 228.5245361328125, 100.0
			
			#initialize animate_peptide_to_curve links
			#set_position_009.Geometry -> group_output_3.Atoms
			animate_peptide_to_curve.links.new(set_position_009.outputs[0], group_output_3.inputs[0])
			#separate_geometry_001.Selection -> set_position_1.Geometry
			animate_peptide_to_curve.links.new(separate_geometry_001.outputs[0], set_position_1.inputs[0])
			#compare_001_1.Result -> separate_geometry_001.Selection
			animate_peptide_to_curve.links.new(compare_001_1.outputs[0], separate_geometry_001.inputs[1])
			#group_input_3.Atoms -> separate_geometry_001.Geometry
			animate_peptide_to_curve.links.new(group_input_3.outputs[0], separate_geometry_001.inputs[0])
			#group_1.Position -> sample_index.Value
			animate_peptide_to_curve.links.new(group_1.outputs[1], sample_index.inputs[1])
			#group_1.Geometry -> sample_index.Geometry
			animate_peptide_to_curve.links.new(group_1.outputs[0], sample_index.inputs[0])
			#reroute_002_1.Output -> sample_index.Index
			animate_peptide_to_curve.links.new(reroute_002_1.outputs[0], sample_index.inputs[2])
			#group_007.Group Index -> reroute_001_1.Input
			animate_peptide_to_curve.links.new(group_007.outputs[1], reroute_001_1.inputs[0])
			#reroute_001_1.Output -> compare_001_1.A
			animate_peptide_to_curve.links.new(reroute_001_1.outputs[0], compare_001_1.inputs[2])
			#math_002_1.Value -> group_1.Length
			animate_peptide_to_curve.links.new(math_002_1.outputs[0], group_1.inputs[2])
			#group_1.Geometry -> sample_index_001.Geometry
			animate_peptide_to_curve.links.new(group_1.outputs[0], sample_index_001.inputs[0])
			#reroute_002_1.Output -> sample_index_001.Index
			animate_peptide_to_curve.links.new(reroute_002_1.outputs[0], sample_index_001.inputs[2])
			#group_1.Tangent -> sample_index_001.Value
			animate_peptide_to_curve.links.new(group_1.outputs[2], sample_index_001.inputs[1])
			#group_007.Position -> vector_math.Vector
			animate_peptide_to_curve.links.new(group_007.outputs[0], vector_math.inputs[0])
			#vector_math.Vector -> set_position_1.Offset
			animate_peptide_to_curve.links.new(vector_math.outputs[0], set_position_1.inputs[3])
			#group_1.Geometry -> domain_size.Geometry
			animate_peptide_to_curve.links.new(group_1.outputs[0], domain_size.inputs[0])
			#set_position_1.Geometry -> set_position_004.Geometry
			animate_peptide_to_curve.links.new(set_position_1.outputs[0], set_position_004.inputs[0])
			#group_007.Position -> vector_math_001.Vector
			animate_peptide_to_curve.links.new(group_007.outputs[0], vector_math_001.inputs[0])
			#vector_math_001.Vector -> align_euler_to_vector.Vector
			animate_peptide_to_curve.links.new(vector_math_001.outputs[0], align_euler_to_vector.inputs[2])
			#align_euler_to_vector.Rotation -> vector_rotate.Axis
			animate_peptide_to_curve.links.new(align_euler_to_vector.outputs[0], vector_rotate.inputs[2])
			#position.Position -> vector_rotate.Vector
			animate_peptide_to_curve.links.new(position.outputs[0], vector_rotate.inputs[0])
			#align_euler_to_vector.Rotation -> vector_rotate.Rotation
			animate_peptide_to_curve.links.new(align_euler_to_vector.outputs[0], vector_rotate.inputs[4])
			#vector_rotate.Vector -> set_position_004.Position
			animate_peptide_to_curve.links.new(vector_rotate.outputs[0], set_position_004.inputs[2])
			#group_008.Position -> vector_math_001.Vector
			animate_peptide_to_curve.links.new(group_008.outputs[0], vector_math_001.inputs[1])
			#set_position_004.Geometry -> set_position_005.Geometry
			animate_peptide_to_curve.links.new(set_position_004.outputs[0], set_position_005.inputs[0])
			#vector_rotate_004.Vector -> set_position_005.Position
			animate_peptide_to_curve.links.new(vector_rotate_004.outputs[0], set_position_005.inputs[2])
			#position.Position -> vector_rotate_004.Vector
			animate_peptide_to_curve.links.new(position.outputs[0], vector_rotate_004.inputs[0])
			#group_011.Position -> align_euler_to_vector_002.Vector
			animate_peptide_to_curve.links.new(group_011.outputs[0], align_euler_to_vector_002.inputs[2])
			#align_euler_to_vector_002.Rotation -> vector_rotate_004.Rotation
			animate_peptide_to_curve.links.new(align_euler_to_vector_002.outputs[0], vector_rotate_004.inputs[4])
			#set_position_005.Geometry -> set_position_006.Geometry
			animate_peptide_to_curve.links.new(set_position_005.outputs[0], set_position_006.inputs[0])
			#position.Position -> vector_rotate_005.Vector
			animate_peptide_to_curve.links.new(position.outputs[0], vector_rotate_005.inputs[0])
			#vector_rotate_005.Vector -> set_position_006.Position
			animate_peptide_to_curve.links.new(vector_rotate_005.outputs[0], set_position_006.inputs[2])
			#domain_size.Point Count -> compare_001_1.B
			animate_peptide_to_curve.links.new(domain_size.outputs[0], compare_001_1.inputs[3])
			#set_position_006.Geometry -> set_position_007.Geometry
			animate_peptide_to_curve.links.new(set_position_006.outputs[0], set_position_007.inputs[0])
			#sample_index.Value -> vector_math_003.Vector
			animate_peptide_to_curve.links.new(sample_index.outputs[0], vector_math_003.inputs[0])
			#group_007.Position -> vector_math_003.Vector
			animate_peptide_to_curve.links.new(group_007.outputs[0], vector_math_003.inputs[1])
			#vector_math_003.Vector -> set_position_007.Offset
			animate_peptide_to_curve.links.new(vector_math_003.outputs[0], set_position_007.inputs[3])
			#set_position_007.Geometry -> set_position_008.Geometry
			animate_peptide_to_curve.links.new(set_position_007.outputs[0], set_position_008.inputs[0])
			#position_002_1.Position -> vector_rotate_006.Vector
			animate_peptide_to_curve.links.new(position_002_1.outputs[0], vector_rotate_006.inputs[0])
			#vector_rotate_006.Vector -> set_position_008.Position
			animate_peptide_to_curve.links.new(vector_rotate_006.outputs[0], set_position_008.inputs[2])
			#align_euler_to_vector_003.Rotation -> vector_rotate_006.Rotation
			animate_peptide_to_curve.links.new(align_euler_to_vector_003.outputs[0], vector_rotate_006.inputs[4])
			#group_007.Position -> vector_rotate_006.Center
			animate_peptide_to_curve.links.new(group_007.outputs[0], vector_rotate_006.inputs[1])
			#reroute_2.Output -> vector_math_006.Vector
			animate_peptide_to_curve.links.new(reroute_2.outputs[0], vector_math_006.inputs[0])
			#vector_math_006.Vector -> align_euler_to_vector_003.Vector
			animate_peptide_to_curve.links.new(vector_math_006.outputs[0], align_euler_to_vector_003.inputs[2])
			#group_1.Geometry -> set_curve_tilt.Curve
			animate_peptide_to_curve.links.new(group_1.outputs[0], set_curve_tilt.inputs[0])
			#set_curve_tilt.Curve -> sample_index_002.Geometry
			animate_peptide_to_curve.links.new(set_curve_tilt.outputs[0], sample_index_002.inputs[0])
			#reroute_001_1.Output -> reroute_002_1.Input
			animate_peptide_to_curve.links.new(reroute_001_1.outputs[0], reroute_002_1.inputs[0])
			#reroute_002_1.Output -> sample_index_002.Index
			animate_peptide_to_curve.links.new(reroute_002_1.outputs[0], sample_index_002.inputs[2])
			#set_position_008.Geometry -> set_position_009.Geometry
			animate_peptide_to_curve.links.new(set_position_008.outputs[0], set_position_009.inputs[0])
			#position_002_1.Position -> vector_rotate_007.Vector
			animate_peptide_to_curve.links.new(position_002_1.outputs[0], vector_rotate_007.inputs[0])
			#group_007.Position -> vector_rotate_007.Center
			animate_peptide_to_curve.links.new(group_007.outputs[0], vector_rotate_007.inputs[1])
			#vector_rotate_007.Vector -> set_position_009.Position
			animate_peptide_to_curve.links.new(vector_rotate_007.outputs[0], set_position_009.inputs[2])
			#curve_tilt.Tilt -> sample_index_002.Value
			animate_peptide_to_curve.links.new(curve_tilt.outputs[0], sample_index_002.inputs[1])
			#sample_index_002.Value -> vector_rotate_007.Angle
			animate_peptide_to_curve.links.new(sample_index_002.outputs[0], vector_rotate_007.inputs[3])
			#reroute_004.Output -> vector_rotate_007.Axis
			animate_peptide_to_curve.links.new(reroute_004.outputs[0], vector_rotate_007.inputs[2])
			#group_input_3.Offset -> group_1.Offset
			animate_peptide_to_curve.links.new(group_input_3.outputs[2], group_1.inputs[1])
			#group_input_3.Curve -> trim_curve.Curve
			animate_peptide_to_curve.links.new(group_input_3.outputs[1], trim_curve.inputs[0])
			#trim_curve.Curve -> group_1.Geometry
			animate_peptide_to_curve.links.new(trim_curve.outputs[0], group_1.inputs[0])
			#group_input_3.Start -> trim_curve.Start
			animate_peptide_to_curve.links.new(group_input_3.outputs[3], trim_curve.inputs[2])
			#group_input_3.End -> trim_curve.End
			animate_peptide_to_curve.links.new(group_input_3.outputs[4], trim_curve.inputs[3])
			#accumulate_field_002_1.Leading -> math_1.Value
			animate_peptide_to_curve.links.new(accumulate_field_002_1.outputs[0], math_1.inputs[0])
			#math_1.Value -> set_curve_tilt.Tilt
			animate_peptide_to_curve.links.new(math_1.outputs[0], set_curve_tilt.inputs[2])
			#group_input_3.Rotate -> math_1.Value
			animate_peptide_to_curve.links.new(group_input_3.outputs[5], math_1.inputs[1])
			#sample_index_001.Value -> reroute_2.Input
			animate_peptide_to_curve.links.new(sample_index_001.outputs[0], reroute_2.inputs[0])
			#reroute_2.Output -> reroute_003_1.Input
			animate_peptide_to_curve.links.new(reroute_2.outputs[0], reroute_003_1.inputs[0])
			#reroute_003_1.Output -> reroute_004.Input
			animate_peptide_to_curve.links.new(reroute_003_1.outputs[0], reroute_004.inputs[0])
			#math_001_1.Value -> accumulate_field_002_1.Value
			animate_peptide_to_curve.links.new(math_001_1.outputs[0], accumulate_field_002_1.inputs[0])
			#group_input_3.Twist -> math_001_1.Value
			animate_peptide_to_curve.links.new(group_input_3.outputs[6], math_001_1.inputs[1])
			return animate_peptide_to_curve

		animate_peptide_to_curve = animate_peptide_to_curve_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Animate Peptide to Curve", type = 'NODES')
		mod.node_group = animate_peptide_to_curve
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Animate_Peptide_to_Curve.bl_idname)
			
def register():
	bpy.utils.register_class(Animate_Peptide_to_Curve)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Animate_Peptide_to_Curve)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
