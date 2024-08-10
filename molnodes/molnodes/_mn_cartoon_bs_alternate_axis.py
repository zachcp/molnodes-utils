bl_info = {
	"name" : ".MN_cartoon_bs_alternate_axis",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _MN_cartoon_bs_alternate_axis(bpy.types.Operator):
	bl_idname = "node._mn_cartoon_bs_alternate_axis"
	bl_label = ".MN_cartoon_bs_alternate_axis"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _field_offset node group
		def _field_offset_node_group():
			_field_offset = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".field_offset")

			_field_offset.color_tag = 'NONE'
			_field_offset.description = ""

			
			#_field_offset interface
			#Socket Field
			field_socket = _field_offset.interface.new_socket(name = "Field", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			field_socket.subtype = 'NONE'
			field_socket.default_value = (0.0, 0.0, 0.0)
			field_socket.min_value = -3.4028234663852886e+38
			field_socket.max_value = 3.4028234663852886e+38
			field_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket = _field_offset.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			value_socket.attribute_domain = 'POINT'
			
			#Socket Field
			field_socket_1 = _field_offset.interface.new_socket(name = "Field", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			field_socket_1.subtype = 'NONE'
			field_socket_1.default_value = 0
			field_socket_1.min_value = -2147483648
			field_socket_1.max_value = 2147483647
			field_socket_1.attribute_domain = 'POINT'
			
			#Socket Field
			field_socket_2 = _field_offset.interface.new_socket(name = "Field", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			field_socket_2.subtype = 'NONE'
			field_socket_2.default_value = 0.0
			field_socket_2.min_value = -3.4028234663852886e+38
			field_socket_2.max_value = 3.4028234663852886e+38
			field_socket_2.attribute_domain = 'POINT'
			
			#Socket Field
			field_socket_3 = _field_offset.interface.new_socket(name = "Field", in_out='INPUT', socket_type = 'NodeSocketVector')
			field_socket_3.subtype = 'NONE'
			field_socket_3.default_value = (0.0, 0.0, 0.0)
			field_socket_3.min_value = -3.4028234663852886e+38
			field_socket_3.max_value = 3.4028234663852886e+38
			field_socket_3.attribute_domain = 'POINT'
			field_socket_3.hide_value = True
			
			#Socket Value
			value_socket_1 = _field_offset.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketBool')
			value_socket_1.attribute_domain = 'POINT'
			value_socket_1.hide_value = True
			
			#Socket Field
			field_socket_4 = _field_offset.interface.new_socket(name = "Field", in_out='INPUT', socket_type = 'NodeSocketInt')
			field_socket_4.subtype = 'NONE'
			field_socket_4.default_value = 0
			field_socket_4.min_value = -2147483648
			field_socket_4.max_value = 2147483647
			field_socket_4.attribute_domain = 'POINT'
			field_socket_4.hide_value = True
			
			#Socket Field
			field_socket_5 = _field_offset.interface.new_socket(name = "Field", in_out='INPUT', socket_type = 'NodeSocketFloat')
			field_socket_5.subtype = 'NONE'
			field_socket_5.default_value = 0.0
			field_socket_5.min_value = -3.4028234663852886e+38
			field_socket_5.max_value = 3.4028234663852886e+38
			field_socket_5.attribute_domain = 'POINT'
			field_socket_5.hide_value = True
			
			#Socket Offset
			offset_socket = _field_offset.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket.subtype = 'NONE'
			offset_socket.default_value = 0
			offset_socket.min_value = -2147483648
			offset_socket.max_value = 2147483647
			offset_socket.attribute_domain = 'POINT'
			
			
			#initialize _field_offset nodes
			#node Group Output
			group_output = _field_offset.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Math.001
			math_001 = _field_offset.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.operation = 'ADD'
			math_001.use_clamp = False
			
			#node Evaluate at Index
			evaluate_at_index = _field_offset.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index.name = "Evaluate at Index"
			evaluate_at_index.data_type = 'FLOAT_VECTOR'
			evaluate_at_index.domain = 'POINT'
			
			#node Group Input
			group_input = _field_offset.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Evaluate at Index.001
			evaluate_at_index_001 = _field_offset.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001.name = "Evaluate at Index.001"
			evaluate_at_index_001.data_type = 'BOOLEAN'
			evaluate_at_index_001.domain = 'POINT'
			
			#node Index
			index = _field_offset.nodes.new("GeometryNodeInputIndex")
			index.name = "Index"
			
			#node Evaluate at Index.002
			evaluate_at_index_002 = _field_offset.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_002.name = "Evaluate at Index.002"
			evaluate_at_index_002.data_type = 'INT'
			evaluate_at_index_002.domain = 'POINT'
			
			#node Evaluate at Index.003
			evaluate_at_index_003 = _field_offset.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_003.name = "Evaluate at Index.003"
			evaluate_at_index_003.data_type = 'FLOAT'
			evaluate_at_index_003.domain = 'POINT'
			
			
			
			
			#Set locations
			group_output.location = (407.6440124511719, 0.0)
			math_001.location = (0.5235366821289062, 15.3753662109375)
			evaluate_at_index.location = (217.64404296875, 102.376708984375)
			group_input.location = (-417.64404296875, 0.0)
			evaluate_at_index_001.location = (220.0, -60.0)
			index.location = (-260.0, -40.0)
			evaluate_at_index_002.location = (220.0, -220.0)
			evaluate_at_index_003.location = (220.0, -380.0)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			evaluate_at_index.width, evaluate_at_index.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			evaluate_at_index_001.width, evaluate_at_index_001.height = 140.0, 100.0
			index.width, index.height = 140.0, 100.0
			evaluate_at_index_002.width, evaluate_at_index_002.height = 140.0, 100.0
			evaluate_at_index_003.width, evaluate_at_index_003.height = 140.0, 100.0
			
			#initialize _field_offset links
			#index.Index -> math_001.Value
			_field_offset.links.new(index.outputs[0], math_001.inputs[0])
			#math_001.Value -> evaluate_at_index.Index
			_field_offset.links.new(math_001.outputs[0], evaluate_at_index.inputs[0])
			#group_input.Field -> evaluate_at_index.Value
			_field_offset.links.new(group_input.outputs[0], evaluate_at_index.inputs[1])
			#group_input.Offset -> math_001.Value
			_field_offset.links.new(group_input.outputs[4], math_001.inputs[1])
			#evaluate_at_index.Value -> group_output.Field
			_field_offset.links.new(evaluate_at_index.outputs[0], group_output.inputs[0])
			#math_001.Value -> evaluate_at_index_001.Index
			_field_offset.links.new(math_001.outputs[0], evaluate_at_index_001.inputs[0])
			#group_input.Value -> evaluate_at_index_001.Value
			_field_offset.links.new(group_input.outputs[1], evaluate_at_index_001.inputs[1])
			#evaluate_at_index_001.Value -> group_output.Value
			_field_offset.links.new(evaluate_at_index_001.outputs[0], group_output.inputs[1])
			#math_001.Value -> evaluate_at_index_002.Index
			_field_offset.links.new(math_001.outputs[0], evaluate_at_index_002.inputs[0])
			#group_input.Field -> evaluate_at_index_002.Value
			_field_offset.links.new(group_input.outputs[2], evaluate_at_index_002.inputs[1])
			#evaluate_at_index_002.Value -> group_output.Field
			_field_offset.links.new(evaluate_at_index_002.outputs[0], group_output.inputs[2])
			#math_001.Value -> evaluate_at_index_003.Index
			_field_offset.links.new(math_001.outputs[0], evaluate_at_index_003.inputs[0])
			#group_input.Field -> evaluate_at_index_003.Value
			_field_offset.links.new(group_input.outputs[3], evaluate_at_index_003.inputs[1])
			#evaluate_at_index_003.Value -> group_output.Field
			_field_offset.links.new(evaluate_at_index_003.outputs[0], group_output.inputs[3])
			return _field_offset

		_field_offset = _field_offset_node_group()

		#initialize _sec_struct_counter node group
		def _sec_struct_counter_node_group():
			_sec_struct_counter = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".sec_struct_counter")

			_sec_struct_counter.color_tag = 'NONE'
			_sec_struct_counter.description = ""

			
			#_sec_struct_counter interface
			#Socket Leading
			leading_socket = _sec_struct_counter.interface.new_socket(name = "Leading", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			leading_socket.subtype = 'NONE'
			leading_socket.default_value = 0
			leading_socket.min_value = -2147483648
			leading_socket.max_value = 2147483647
			leading_socket.attribute_domain = 'POINT'
			
			#Socket Trailing
			trailing_socket = _sec_struct_counter.interface.new_socket(name = "Trailing", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			trailing_socket.subtype = 'NONE'
			trailing_socket.default_value = 0
			trailing_socket.min_value = -2147483648
			trailing_socket.max_value = 2147483647
			trailing_socket.attribute_domain = 'POINT'
			
			#Socket Total
			total_socket = _sec_struct_counter.interface.new_socket(name = "Total", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			total_socket.subtype = 'NONE'
			total_socket.default_value = 0
			total_socket.min_value = -2147483648
			total_socket.max_value = 2147483647
			total_socket.attribute_domain = 'POINT'
			
			#Socket Border
			border_socket = _sec_struct_counter.interface.new_socket(name = "Border", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			border_socket.attribute_domain = 'POINT'
			
			
			#initialize _sec_struct_counter nodes
			#node Group Input
			group_input_1 = _sec_struct_counter.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			
			#node Reroute.005
			reroute_005 = _sec_struct_counter.nodes.new("NodeReroute")
			reroute_005.name = "Reroute.005"
			#node Named Attribute.001
			named_attribute_001 = _sec_struct_counter.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.data_type = 'INT'
			#Name
			named_attribute_001.inputs[0].default_value = "sec_struct"
			
			#node Group.004
			group_004 = _sec_struct_counter.nodes.new("GeometryNodeGroup")
			group_004.name = "Group.004"
			group_004.node_tree = _field_offset
			#Input_0
			group_004.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Input_3
			group_004.inputs[1].default_value = False
			#Input_7
			group_004.inputs[3].default_value = 0.0
			#Input_1
			group_004.inputs[4].default_value = -1
			
			#node Compare.009
			compare_009 = _sec_struct_counter.nodes.new("FunctionNodeCompare")
			compare_009.name = "Compare.009"
			compare_009.data_type = 'INT'
			compare_009.mode = 'ELEMENT'
			compare_009.operation = 'NOT_EQUAL'
			
			#node Accumulate Field.004
			accumulate_field_004 = _sec_struct_counter.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_004.name = "Accumulate Field.004"
			accumulate_field_004.data_type = 'INT'
			accumulate_field_004.domain = 'POINT'
			#Group Index
			accumulate_field_004.inputs[1].default_value = 0
			
			#node Compare.010
			compare_010 = _sec_struct_counter.nodes.new("FunctionNodeCompare")
			compare_010.name = "Compare.010"
			compare_010.data_type = 'INT'
			compare_010.mode = 'ELEMENT'
			compare_010.operation = 'NOT_EQUAL'
			
			#node Reroute
			reroute = _sec_struct_counter.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Boolean Math
			boolean_math = _sec_struct_counter.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'OR'
			#Boolean_001
			boolean_math.inputs[1].default_value = False
			
			#node Group Output
			group_output_1 = _sec_struct_counter.nodes.new("NodeGroupOutput")
			group_output_1.name = "Group Output"
			group_output_1.is_active_output = True
			
			#node Group.003
			group_003 = _sec_struct_counter.nodes.new("GeometryNodeGroup")
			group_003.name = "Group.003"
			group_003.node_tree = _field_offset
			#Input_0
			group_003.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Input_3
			group_003.inputs[1].default_value = False
			#Input_7
			group_003.inputs[3].default_value = 0.0
			#Input_1
			group_003.inputs[4].default_value = 1
			
			
			
			
			#Set locations
			group_input_1.location = (-500.1279296875, 0.0)
			reroute_005.location = (-119.8720703125, -60.0)
			named_attribute_001.location = (-300.0, 120.0)
			group_004.location = (-20.0, -220.0)
			compare_009.location = (140.1279296875, 60.0)
			accumulate_field_004.location = (460.0, 40.0)
			compare_010.location = (140.0, -140.0)
			reroute.location = (320.0, -60.0)
			boolean_math.location = (300.0, -140.0)
			group_output_1.location = (796.4706420898438, 27.943008422851562)
			group_003.location = (-19.8720703125, 60.0)
			
			#Set dimensions
			group_input_1.width, group_input_1.height = 140.0, 100.0
			reroute_005.width, reroute_005.height = 16.0, 100.0
			named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
			group_004.width, group_004.height = 140.0, 100.0
			compare_009.width, compare_009.height = 140.0, 100.0
			accumulate_field_004.width, accumulate_field_004.height = 140.0, 100.0
			compare_010.width, compare_010.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			group_output_1.width, group_output_1.height = 140.0, 100.0
			group_003.width, group_003.height = 140.0, 100.0
			
			#initialize _sec_struct_counter links
			#reroute.Output -> accumulate_field_004.Value
			_sec_struct_counter.links.new(reroute.outputs[0], accumulate_field_004.inputs[0])
			#reroute_005.Output -> group_003.Field
			_sec_struct_counter.links.new(reroute_005.outputs[0], group_003.inputs[2])
			#reroute_005.Output -> compare_009.A
			_sec_struct_counter.links.new(reroute_005.outputs[0], compare_009.inputs[2])
			#named_attribute_001.Attribute -> reroute_005.Input
			_sec_struct_counter.links.new(named_attribute_001.outputs[0], reroute_005.inputs[0])
			#group_003.Field -> compare_009.B
			_sec_struct_counter.links.new(group_003.outputs[2], compare_009.inputs[3])
			#accumulate_field_004.Trailing -> group_output_1.Trailing
			_sec_struct_counter.links.new(accumulate_field_004.outputs[1], group_output_1.inputs[1])
			#accumulate_field_004.Leading -> group_output_1.Leading
			_sec_struct_counter.links.new(accumulate_field_004.outputs[0], group_output_1.inputs[0])
			#accumulate_field_004.Total -> group_output_1.Total
			_sec_struct_counter.links.new(accumulate_field_004.outputs[2], group_output_1.inputs[2])
			#reroute.Output -> group_output_1.Border
			_sec_struct_counter.links.new(reroute.outputs[0], group_output_1.inputs[3])
			#reroute_005.Output -> group_004.Field
			_sec_struct_counter.links.new(reroute_005.outputs[0], group_004.inputs[2])
			#reroute_005.Output -> compare_010.A
			_sec_struct_counter.links.new(reroute_005.outputs[0], compare_010.inputs[2])
			#group_004.Field -> compare_010.B
			_sec_struct_counter.links.new(group_004.outputs[2], compare_010.inputs[3])
			#compare_009.Result -> reroute.Input
			_sec_struct_counter.links.new(compare_009.outputs[0], reroute.inputs[0])
			#compare_010.Result -> boolean_math.Boolean
			_sec_struct_counter.links.new(compare_010.outputs[0], boolean_math.inputs[0])
			return _sec_struct_counter

		_sec_struct_counter = _sec_struct_counter_node_group()

		#initialize _mn_select_sec_struct_id node group
		def _mn_select_sec_struct_id_node_group():
			_mn_select_sec_struct_id = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_select_sec_struct_id")

			_mn_select_sec_struct_id.color_tag = 'NONE'
			_mn_select_sec_struct_id.description = ""

			
			#_mn_select_sec_struct_id interface
			#Socket Selection
			selection_socket = _mn_select_sec_struct_id.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket.attribute_domain = 'POINT'
			selection_socket.description = "The calculated selection"
			
			#Socket Inverted
			inverted_socket = _mn_select_sec_struct_id.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket.attribute_domain = 'POINT'
			
			#Socket And
			and_socket = _mn_select_sec_struct_id.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket.attribute_domain = 'POINT'
			and_socket.hide_value = True
			
			#Socket Or
			or_socket = _mn_select_sec_struct_id.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket.attribute_domain = 'POINT'
			or_socket.hide_value = True
			
			#Socket id
			id_socket = _mn_select_sec_struct_id.interface.new_socket(name = "id", in_out='INPUT', socket_type = 'NodeSocketInt')
			id_socket.subtype = 'NONE'
			id_socket.default_value = 1
			id_socket.min_value = -2147483648
			id_socket.max_value = 2147483647
			id_socket.attribute_domain = 'POINT'
			id_socket.description = "Secondary structure component to select"
			
			
			#initialize _mn_select_sec_struct_id nodes
			#node Named Attribute.002
			named_attribute_002 = _mn_select_sec_struct_id.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002.name = "Named Attribute.002"
			named_attribute_002.data_type = 'INT'
			#Name
			named_attribute_002.inputs[0].default_value = "sec_struct"
			
			#node Boolean Math
			boolean_math_1 = _mn_select_sec_struct_id.nodes.new("FunctionNodeBooleanMath")
			boolean_math_1.name = "Boolean Math"
			boolean_math_1.operation = 'AND'
			
			#node Group Output
			group_output_2 = _mn_select_sec_struct_id.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Compare.012
			compare_012 = _mn_select_sec_struct_id.nodes.new("FunctionNodeCompare")
			compare_012.name = "Compare.012"
			compare_012.data_type = 'INT'
			compare_012.mode = 'ELEMENT'
			compare_012.operation = 'EQUAL'
			
			#node Group Input
			group_input_2 = _mn_select_sec_struct_id.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
			#node Boolean Math.001
			boolean_math_001 = _mn_select_sec_struct_id.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001.name = "Boolean Math.001"
			boolean_math_001.operation = 'OR'
			
			#node Boolean Math.002
			boolean_math_002 = _mn_select_sec_struct_id.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002.name = "Boolean Math.002"
			boolean_math_002.operation = 'NOT'
			
			
			
			
			#Set locations
			named_attribute_002.location = (80.0, 0.0)
			boolean_math_1.location = (400.0, 200.0)
			group_output_2.location = (760.0, 200.0)
			compare_012.location = (240.0, 100.0)
			group_input_2.location = (80.0, 100.0)
			boolean_math_001.location = (579.9999389648438, 196.54164123535156)
			boolean_math_002.location = (580.0, 60.0)
			
			#Set dimensions
			named_attribute_002.width, named_attribute_002.height = 140.0, 100.0
			boolean_math_1.width, boolean_math_1.height = 140.0, 100.0
			group_output_2.width, group_output_2.height = 140.0, 100.0
			compare_012.width, compare_012.height = 140.0, 100.0
			group_input_2.width, group_input_2.height = 140.0, 100.0
			boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
			boolean_math_002.width, boolean_math_002.height = 140.0, 100.0
			
			#initialize _mn_select_sec_struct_id links
			#boolean_math_001.Boolean -> group_output_2.Selection
			_mn_select_sec_struct_id.links.new(boolean_math_001.outputs[0], group_output_2.inputs[0])
			#compare_012.Result -> boolean_math_1.Boolean
			_mn_select_sec_struct_id.links.new(compare_012.outputs[0], boolean_math_1.inputs[1])
			#group_input_2.id -> compare_012.A
			_mn_select_sec_struct_id.links.new(group_input_2.outputs[2], compare_012.inputs[2])
			#group_input_2.And -> boolean_math_1.Boolean
			_mn_select_sec_struct_id.links.new(group_input_2.outputs[0], boolean_math_1.inputs[0])
			#named_attribute_002.Attribute -> compare_012.B
			_mn_select_sec_struct_id.links.new(named_attribute_002.outputs[0], compare_012.inputs[3])
			#boolean_math_1.Boolean -> boolean_math_001.Boolean
			_mn_select_sec_struct_id.links.new(boolean_math_1.outputs[0], boolean_math_001.inputs[0])
			#group_input_2.Or -> boolean_math_001.Boolean
			_mn_select_sec_struct_id.links.new(group_input_2.outputs[1], boolean_math_001.inputs[1])
			#boolean_math_001.Boolean -> boolean_math_002.Boolean
			_mn_select_sec_struct_id.links.new(boolean_math_001.outputs[0], boolean_math_002.inputs[0])
			#boolean_math_002.Boolean -> group_output_2.Inverted
			_mn_select_sec_struct_id.links.new(boolean_math_002.outputs[0], group_output_2.inputs[1])
			return _mn_select_sec_struct_id

		_mn_select_sec_struct_id = _mn_select_sec_struct_id_node_group()

		#initialize is_sheet node group
		def is_sheet_node_group():
			is_sheet = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Is Sheet")

			is_sheet.color_tag = 'INPUT'
			is_sheet.description = ""

			
			#is_sheet interface
			#Socket Selection
			selection_socket_1 = is_sheet.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket_1.attribute_domain = 'POINT'
			selection_socket_1.description = "Selected atoms form part of a sheet"
			
			#Socket Inverted
			inverted_socket_1 = is_sheet.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket_1.attribute_domain = 'POINT'
			
			#Socket And
			and_socket_1 = is_sheet.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket_1.attribute_domain = 'POINT'
			and_socket_1.hide_value = True
			
			#Socket Or
			or_socket_1 = is_sheet.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket_1.attribute_domain = 'POINT'
			or_socket_1.hide_value = True
			
			
			#initialize is_sheet nodes
			#node Group Output
			group_output_3 = is_sheet.nodes.new("NodeGroupOutput")
			group_output_3.name = "Group Output"
			group_output_3.is_active_output = True
			
			#node Group Input
			group_input_3 = is_sheet.nodes.new("NodeGroupInput")
			group_input_3.name = "Group Input"
			
			#node MN_select_sec_struct.002
			mn_select_sec_struct_002 = is_sheet.nodes.new("GeometryNodeGroup")
			mn_select_sec_struct_002.label = "Select Sec Struct"
			mn_select_sec_struct_002.name = "MN_select_sec_struct.002"
			mn_select_sec_struct_002.node_tree = _mn_select_sec_struct_id
			#Socket_1
			mn_select_sec_struct_002.inputs[2].default_value = 2
			
			
			
			
			#Set locations
			group_output_3.location = (267.00146484375, 0.0)
			group_input_3.location = (-220.0, -80.0)
			mn_select_sec_struct_002.location = (0.0, 0.0)
			
			#Set dimensions
			group_output_3.width, group_output_3.height = 140.0, 100.0
			group_input_3.width, group_input_3.height = 140.0, 100.0
			mn_select_sec_struct_002.width, mn_select_sec_struct_002.height = 217.00146484375, 100.0
			
			#initialize is_sheet links
			#mn_select_sec_struct_002.Selection -> group_output_3.Selection
			is_sheet.links.new(mn_select_sec_struct_002.outputs[0], group_output_3.inputs[0])
			#group_input_3.And -> mn_select_sec_struct_002.And
			is_sheet.links.new(group_input_3.outputs[0], mn_select_sec_struct_002.inputs[0])
			#group_input_3.Or -> mn_select_sec_struct_002.Or
			is_sheet.links.new(group_input_3.outputs[1], mn_select_sec_struct_002.inputs[1])
			#mn_select_sec_struct_002.Inverted -> group_output_3.Inverted
			is_sheet.links.new(mn_select_sec_struct_002.outputs[1], group_output_3.inputs[1])
			return is_sheet

		is_sheet = is_sheet_node_group()

		#initialize is_loop node group
		def is_loop_node_group():
			is_loop = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Is Loop")

			is_loop.color_tag = 'INPUT'
			is_loop.description = ""

			
			#is_loop interface
			#Socket Selection
			selection_socket_2 = is_loop.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket_2.attribute_domain = 'POINT'
			selection_socket_2.description = "Selected atoms form part of a loop, and not part of any secondary structure"
			
			#Socket Inverted
			inverted_socket_2 = is_loop.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket_2.attribute_domain = 'POINT'
			
			#Socket And
			and_socket_2 = is_loop.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket_2.attribute_domain = 'POINT'
			and_socket_2.hide_value = True
			
			#Socket Or
			or_socket_2 = is_loop.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket_2.attribute_domain = 'POINT'
			or_socket_2.hide_value = True
			
			
			#initialize is_loop nodes
			#node Group Output
			group_output_4 = is_loop.nodes.new("NodeGroupOutput")
			group_output_4.name = "Group Output"
			group_output_4.is_active_output = True
			
			#node Group Input
			group_input_4 = is_loop.nodes.new("NodeGroupInput")
			group_input_4.name = "Group Input"
			
			#node MN_select_sec_struct.002
			mn_select_sec_struct_002_1 = is_loop.nodes.new("GeometryNodeGroup")
			mn_select_sec_struct_002_1.label = "Select Sec Struct"
			mn_select_sec_struct_002_1.name = "MN_select_sec_struct.002"
			mn_select_sec_struct_002_1.node_tree = _mn_select_sec_struct_id
			#Socket_1
			mn_select_sec_struct_002_1.inputs[2].default_value = 3
			
			
			
			
			#Set locations
			group_output_4.location = (267.00146484375, 0.0)
			group_input_4.location = (-200.0, 0.0)
			mn_select_sec_struct_002_1.location = (0.0, 0.0)
			
			#Set dimensions
			group_output_4.width, group_output_4.height = 140.0, 100.0
			group_input_4.width, group_input_4.height = 140.0, 100.0
			mn_select_sec_struct_002_1.width, mn_select_sec_struct_002_1.height = 217.00146484375, 100.0
			
			#initialize is_loop links
			#mn_select_sec_struct_002_1.Selection -> group_output_4.Selection
			is_loop.links.new(mn_select_sec_struct_002_1.outputs[0], group_output_4.inputs[0])
			#group_input_4.And -> mn_select_sec_struct_002_1.And
			is_loop.links.new(group_input_4.outputs[0], mn_select_sec_struct_002_1.inputs[0])
			#group_input_4.Or -> mn_select_sec_struct_002_1.Or
			is_loop.links.new(group_input_4.outputs[1], mn_select_sec_struct_002_1.inputs[1])
			#mn_select_sec_struct_002_1.Inverted -> group_output_4.Inverted
			is_loop.links.new(mn_select_sec_struct_002_1.outputs[1], group_output_4.inputs[1])
			return is_loop

		is_loop = is_loop_node_group()

		#initialize is_helix node group
		def is_helix_node_group():
			is_helix = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Is Helix")

			is_helix.color_tag = 'INPUT'
			is_helix.description = ""

			
			#is_helix interface
			#Socket Selection
			selection_socket_3 = is_helix.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket_3.attribute_domain = 'POINT'
			selection_socket_3.description = "Selected atoms form part of an helix"
			
			#Socket Inverted
			inverted_socket_3 = is_helix.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket_3.attribute_domain = 'POINT'
			
			#Socket And
			and_socket_3 = is_helix.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket_3.attribute_domain = 'POINT'
			and_socket_3.hide_value = True
			
			#Socket Or
			or_socket_3 = is_helix.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket_3.attribute_domain = 'POINT'
			or_socket_3.hide_value = True
			
			
			#initialize is_helix nodes
			#node Group Output
			group_output_5 = is_helix.nodes.new("NodeGroupOutput")
			group_output_5.name = "Group Output"
			group_output_5.is_active_output = True
			
			#node Group Input
			group_input_5 = is_helix.nodes.new("NodeGroupInput")
			group_input_5.name = "Group Input"
			
			#node MN_select_sec_struct.002
			mn_select_sec_struct_002_2 = is_helix.nodes.new("GeometryNodeGroup")
			mn_select_sec_struct_002_2.label = "Select Sec Struct"
			mn_select_sec_struct_002_2.name = "MN_select_sec_struct.002"
			mn_select_sec_struct_002_2.node_tree = _mn_select_sec_struct_id
			#Socket_1
			mn_select_sec_struct_002_2.inputs[2].default_value = 1
			
			
			
			
			#Set locations
			group_output_5.location = (267.00146484375, 0.0)
			group_input_5.location = (-200.0, 0.0)
			mn_select_sec_struct_002_2.location = (0.0, 0.0)
			
			#Set dimensions
			group_output_5.width, group_output_5.height = 140.0, 100.0
			group_input_5.width, group_input_5.height = 140.0, 100.0
			mn_select_sec_struct_002_2.width, mn_select_sec_struct_002_2.height = 217.00146484375, 100.0
			
			#initialize is_helix links
			#mn_select_sec_struct_002_2.Selection -> group_output_5.Selection
			is_helix.links.new(mn_select_sec_struct_002_2.outputs[0], group_output_5.inputs[0])
			#group_input_5.And -> mn_select_sec_struct_002_2.And
			is_helix.links.new(group_input_5.outputs[0], mn_select_sec_struct_002_2.inputs[0])
			#group_input_5.Or -> mn_select_sec_struct_002_2.Or
			is_helix.links.new(group_input_5.outputs[1], mn_select_sec_struct_002_2.inputs[1])
			#mn_select_sec_struct_002_2.Inverted -> group_output_5.Inverted
			is_helix.links.new(mn_select_sec_struct_002_2.outputs[1], group_output_5.inputs[1])
			return is_helix

		is_helix = is_helix_node_group()

		#initialize _mn_select_sec_struct node group
		def _mn_select_sec_struct_node_group():
			_mn_select_sec_struct = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_select_sec_struct")

			_mn_select_sec_struct.color_tag = 'NONE'
			_mn_select_sec_struct.description = ""

			
			#_mn_select_sec_struct interface
			#Socket Is Helix
			is_helix_socket = _mn_select_sec_struct.interface.new_socket(name = "Is Helix", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_helix_socket.attribute_domain = 'POINT'
			
			#Socket Is Sheet
			is_sheet_socket = _mn_select_sec_struct.interface.new_socket(name = "Is Sheet", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_sheet_socket.attribute_domain = 'POINT'
			
			#Socket Is Structured
			is_structured_socket = _mn_select_sec_struct.interface.new_socket(name = "Is Structured", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_structured_socket.attribute_domain = 'POINT'
			
			#Socket Is Loop
			is_loop_socket = _mn_select_sec_struct.interface.new_socket(name = "Is Loop", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_loop_socket.attribute_domain = 'POINT'
			
			#Socket And
			and_socket_4 = _mn_select_sec_struct.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket_4.attribute_domain = 'POINT'
			and_socket_4.hide_value = True
			
			
			#initialize _mn_select_sec_struct nodes
			#node Group.001
			group_001 = _mn_select_sec_struct.nodes.new("GeometryNodeGroup")
			group_001.name = "Group.001"
			group_001.node_tree = is_sheet
			#Socket_3
			group_001.inputs[1].default_value = False
			
			#node Group.002
			group_002 = _mn_select_sec_struct.nodes.new("GeometryNodeGroup")
			group_002.name = "Group.002"
			group_002.node_tree = is_loop
			#Socket_3
			group_002.inputs[1].default_value = False
			
			#node Group
			group = _mn_select_sec_struct.nodes.new("GeometryNodeGroup")
			group.name = "Group"
			group.node_tree = is_helix
			#Socket_3
			group.inputs[1].default_value = False
			
			#node Boolean Math.001
			boolean_math_001_1 = _mn_select_sec_struct.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_1.name = "Boolean Math.001"
			boolean_math_001_1.hide = True
			boolean_math_001_1.operation = 'NOT'
			
			#node Group Output
			group_output_6 = _mn_select_sec_struct.nodes.new("NodeGroupOutput")
			group_output_6.name = "Group Output"
			group_output_6.is_active_output = True
			
			#node Group Input
			group_input_6 = _mn_select_sec_struct.nodes.new("NodeGroupInput")
			group_input_6.name = "Group Input"
			group_input_6.outputs[1].hide = True
			
			
			
			
			#Set locations
			group_001.location = (120.0, -60.0)
			group_002.location = (120.0, -180.0)
			group.location = (120.0, 60.0)
			boolean_math_001_1.location = (300.0, -140.0)
			group_output_6.location = (540.0, -60.0)
			group_input_6.location = (-160.0, -40.0)
			
			#Set dimensions
			group_001.width, group_001.height = 140.0, 100.0
			group_002.width, group_002.height = 140.0, 100.0
			group.width, group.height = 140.0, 100.0
			boolean_math_001_1.width, boolean_math_001_1.height = 140.0, 100.0
			group_output_6.width, group_output_6.height = 140.0, 100.0
			group_input_6.width, group_input_6.height = 140.0, 100.0
			
			#initialize _mn_select_sec_struct links
			#group_002.Selection -> group_output_6.Is Loop
			_mn_select_sec_struct.links.new(group_002.outputs[0], group_output_6.inputs[3])
			#group_002.Selection -> boolean_math_001_1.Boolean
			_mn_select_sec_struct.links.new(group_002.outputs[0], boolean_math_001_1.inputs[0])
			#boolean_math_001_1.Boolean -> group_output_6.Is Structured
			_mn_select_sec_struct.links.new(boolean_math_001_1.outputs[0], group_output_6.inputs[2])
			#group.Selection -> group_output_6.Is Helix
			_mn_select_sec_struct.links.new(group.outputs[0], group_output_6.inputs[0])
			#group_001.Selection -> group_output_6.Is Sheet
			_mn_select_sec_struct.links.new(group_001.outputs[0], group_output_6.inputs[1])
			#group_input_6.And -> group.And
			_mn_select_sec_struct.links.new(group_input_6.outputs[0], group.inputs[0])
			#group_input_6.And -> group_001.And
			_mn_select_sec_struct.links.new(group_input_6.outputs[0], group_001.inputs[0])
			#group_input_6.And -> group_002.And
			_mn_select_sec_struct.links.new(group_input_6.outputs[0], group_002.inputs[0])
			return _mn_select_sec_struct

		_mn_select_sec_struct = _mn_select_sec_struct_node_group()

		#initialize _is_odd node group
		def _is_odd_node_group():
			_is_odd = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".is_odd")

			_is_odd.color_tag = 'NONE'
			_is_odd.description = ""

			
			#_is_odd interface
			#Socket is_even
			is_even_socket = _is_odd.interface.new_socket(name = "is_even", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_even_socket.attribute_domain = 'POINT'
			
			#Socket is_odd
			is_odd_socket = _is_odd.interface.new_socket(name = "is_odd", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_odd_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_2 = _is_odd.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketInt')
			value_socket_2.subtype = 'NONE'
			value_socket_2.default_value = 0
			value_socket_2.min_value = -2147483648
			value_socket_2.max_value = 2147483647
			value_socket_2.attribute_domain = 'POINT'
			
			
			#initialize _is_odd nodes
			#node Group Input
			group_input_7 = _is_odd.nodes.new("NodeGroupInput")
			group_input_7.name = "Group Input"
			
			#node Group Output
			group_output_7 = _is_odd.nodes.new("NodeGroupOutput")
			group_output_7.name = "Group Output"
			group_output_7.is_active_output = True
			
			#node Boolean Math
			boolean_math_2 = _is_odd.nodes.new("FunctionNodeBooleanMath")
			boolean_math_2.name = "Boolean Math"
			boolean_math_2.operation = 'NOT'
			
			#node Compare.011
			compare_011 = _is_odd.nodes.new("FunctionNodeCompare")
			compare_011.name = "Compare.011"
			compare_011.data_type = 'FLOAT'
			compare_011.mode = 'ELEMENT'
			compare_011.operation = 'EQUAL'
			#B
			compare_011.inputs[1].default_value = 0.0
			#Epsilon
			compare_011.inputs[12].default_value = 0.0010000000474974513
			
			#node Math.008
			math_008 = _is_odd.nodes.new("ShaderNodeMath")
			math_008.name = "Math.008"
			math_008.operation = 'FLOORED_MODULO'
			math_008.use_clamp = False
			#Value_001
			math_008.inputs[1].default_value = 2.0
			
			
			
			
			#Set locations
			group_input_7.location = (-300.0, 80.0)
			group_output_7.location = (240.0, 120.0)
			boolean_math_2.location = (240.0, 20.0)
			compare_011.location = (60.0, 120.0)
			math_008.location = (-100.0, 120.0)
			
			#Set dimensions
			group_input_7.width, group_input_7.height = 140.0, 100.0
			group_output_7.width, group_output_7.height = 140.0, 100.0
			boolean_math_2.width, boolean_math_2.height = 140.0, 100.0
			compare_011.width, compare_011.height = 140.0, 100.0
			math_008.width, math_008.height = 140.0, 100.0
			
			#initialize _is_odd links
			#group_input_7.Value -> math_008.Value
			_is_odd.links.new(group_input_7.outputs[0], math_008.inputs[0])
			#compare_011.Result -> group_output_7.is_even
			_is_odd.links.new(compare_011.outputs[0], group_output_7.inputs[0])
			#compare_011.Result -> boolean_math_2.Boolean
			_is_odd.links.new(compare_011.outputs[0], boolean_math_2.inputs[0])
			#boolean_math_2.Boolean -> group_output_7.is_odd
			_is_odd.links.new(boolean_math_2.outputs[0], group_output_7.inputs[1])
			#math_008.Value -> compare_011.A
			_is_odd.links.new(math_008.outputs[0], compare_011.inputs[0])
			return _is_odd

		_is_odd = _is_odd_node_group()

		#initialize _mn_cartoon_bs_alternate_axis node group
		def _mn_cartoon_bs_alternate_axis_node_group():
			_mn_cartoon_bs_alternate_axis = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_cartoon_bs_alternate_axis")

			_mn_cartoon_bs_alternate_axis.color_tag = 'NONE'
			_mn_cartoon_bs_alternate_axis.description = ""

			
			#_mn_cartoon_bs_alternate_axis interface
			#Socket Z Vector for Euler
			z_vector_for_euler_socket = _mn_cartoon_bs_alternate_axis.interface.new_socket(name = "Z Vector for Euler", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			z_vector_for_euler_socket.subtype = 'NONE'
			z_vector_for_euler_socket.default_value = (0.0, 0.0, 0.0)
			z_vector_for_euler_socket.min_value = -3.4028234663852886e+38
			z_vector_for_euler_socket.max_value = 3.4028234663852886e+38
			z_vector_for_euler_socket.attribute_domain = 'POINT'
			
			#Socket X Vector for Euler
			x_vector_for_euler_socket = _mn_cartoon_bs_alternate_axis.interface.new_socket(name = "X Vector for Euler", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			x_vector_for_euler_socket.subtype = 'NONE'
			x_vector_for_euler_socket.default_value = (0.0, 0.0, 0.0)
			x_vector_for_euler_socket.min_value = -3.4028234663852886e+38
			x_vector_for_euler_socket.max_value = 3.4028234663852886e+38
			x_vector_for_euler_socket.attribute_domain = 'POINT'
			
			#Socket N
			n_socket = _mn_cartoon_bs_alternate_axis.interface.new_socket(name = "N", in_out='INPUT', socket_type = 'NodeSocketVector')
			n_socket.subtype = 'NONE'
			n_socket.default_value = (0.0, 0.0, 0.0)
			n_socket.min_value = -3.4028234663852886e+38
			n_socket.max_value = 3.4028234663852886e+38
			n_socket.attribute_domain = 'POINT'
			
			#Socket C
			c_socket = _mn_cartoon_bs_alternate_axis.interface.new_socket(name = "C", in_out='INPUT', socket_type = 'NodeSocketVector')
			c_socket.subtype = 'NONE'
			c_socket.default_value = (0.0, 0.0, 0.0)
			c_socket.min_value = -3.4028234663852886e+38
			c_socket.max_value = 3.4028234663852886e+38
			c_socket.attribute_domain = 'POINT'
			
			#Socket O
			o_socket = _mn_cartoon_bs_alternate_axis.interface.new_socket(name = "O", in_out='INPUT', socket_type = 'NodeSocketVector')
			o_socket.subtype = 'NONE'
			o_socket.default_value = (0.0, 0.0, 0.0)
			o_socket.min_value = -3.4028234663852886e+38
			o_socket.max_value = 3.4028234663852886e+38
			o_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_cartoon_bs_alternate_axis nodes
			#node Frame
			frame = _mn_cartoon_bs_alternate_axis.nodes.new("NodeFrame")
			frame.label = "Only the last AA in an AH is selected"
			frame.name = "Frame"
			frame.label_size = 20
			frame.shrink = True
			
			#node Vector Math.005
			vector_math_005 = _mn_cartoon_bs_alternate_axis.nodes.new("ShaderNodeVectorMath")
			vector_math_005.name = "Vector Math.005"
			vector_math_005.operation = 'SCALE'
			
			#node Blur Attribute.001
			blur_attribute_001 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeBlurAttribute")
			blur_attribute_001.name = "Blur Attribute.001"
			blur_attribute_001.data_type = 'FLOAT_VECTOR'
			#Iterations
			blur_attribute_001.inputs[1].default_value = 3
			#Weight
			blur_attribute_001.inputs[2].default_value = 1.0
			
			#node Switch.002
			switch_002 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeSwitch")
			switch_002.name = "Switch.002"
			switch_002.input_type = 'VECTOR'
			
			#node Group Output
			group_output_8 = _mn_cartoon_bs_alternate_axis.nodes.new("NodeGroupOutput")
			group_output_8.name = "Group Output"
			group_output_8.is_active_output = True
			
			#node Index.001
			index_001 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeInputIndex")
			index_001.name = "Index.001"
			
			#node Boolean Math.010
			boolean_math_010 = _mn_cartoon_bs_alternate_axis.nodes.new("FunctionNodeBooleanMath")
			boolean_math_010.name = "Boolean Math.010"
			boolean_math_010.operation = 'AND'
			
			#node Reroute.001
			reroute_001 = _mn_cartoon_bs_alternate_axis.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			#node Vector Math.004
			vector_math_004 = _mn_cartoon_bs_alternate_axis.nodes.new("ShaderNodeVectorMath")
			vector_math_004.label = "N -> C"
			vector_math_004.name = "Vector Math.004"
			vector_math_004.operation = 'SUBTRACT'
			
			#node Group Input
			group_input_8 = _mn_cartoon_bs_alternate_axis.nodes.new("NodeGroupInput")
			group_input_8.name = "Group Input"
			
			#node Vector Math
			vector_math = _mn_cartoon_bs_alternate_axis.nodes.new("ShaderNodeVectorMath")
			vector_math.label = "C --> O"
			vector_math.name = "Vector Math"
			vector_math.operation = 'SUBTRACT'
			
			#node Integer
			integer = _mn_cartoon_bs_alternate_axis.nodes.new("FunctionNodeInputInt")
			integer.name = "Integer"
			integer.integer = -1
			
			#node Compare
			compare = _mn_cartoon_bs_alternate_axis.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'GREATER_THAN'
			
			#node Group.014
			group_014 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeGroup")
			group_014.name = "Group.014"
			group_014.node_tree = _sec_struct_counter
			
			#node Boolean Math
			boolean_math_3 = _mn_cartoon_bs_alternate_axis.nodes.new("FunctionNodeBooleanMath")
			boolean_math_3.name = "Boolean Math"
			boolean_math_3.operation = 'AND'
			
			#node Switch
			switch = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'VECTOR'
			
			#node Group.012
			group_012 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeGroup")
			group_012.name = "Group.012"
			group_012.node_tree = _mn_select_sec_struct
			group_012.outputs[1].hide = True
			group_012.outputs[2].hide = True
			group_012.outputs[3].hide = True
			#Socket_1
			group_012.inputs[0].default_value = True
			
			#node Switch.008
			switch_008 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeSwitch")
			switch_008.name = "Switch.008"
			switch_008.input_type = 'INT'
			#False
			switch_008.inputs[1].default_value = 1
			#True
			switch_008.inputs[2].default_value = -1
			
			#node Group
			group_1 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeGroup")
			group_1.name = "Group"
			group_1.node_tree = _field_offset
			group_1.inputs[1].hide = True
			group_1.inputs[2].hide = True
			group_1.inputs[3].hide = True
			group_1.outputs[1].hide = True
			group_1.outputs[2].hide = True
			group_1.outputs[3].hide = True
			#Input_3
			group_1.inputs[1].default_value = False
			#Input_5
			group_1.inputs[2].default_value = 0
			#Input_7
			group_1.inputs[3].default_value = 0.0
			
			#node Group.011
			group_011 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeGroup")
			group_011.name = "Group.011"
			group_011.node_tree = _mn_select_sec_struct
			#Socket_1
			group_011.inputs[0].default_value = True
			
			#node Group.005
			group_005 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeGroup")
			group_005.name = "Group.005"
			group_005.node_tree = _is_odd
			
			
			
			#Set parents
			compare.parent = frame
			group_014.parent = frame
			boolean_math_3.parent = frame
			group_012.parent = frame
			
			#Set locations
			frame.location = (-86.11199951171875, 65.14605712890625)
			vector_math_005.location = (60.0, 440.0)
			blur_attribute_001.location = (220.0, 400.0)
			switch_002.location = (220.0, 580.0)
			group_output_8.location = (400.0, 580.0)
			index_001.location = (-381.36767578125, 1.1884498596191406)
			boolean_math_010.location = (-41.36767578125, 101.18844604492188)
			reroute_001.location = (-897.6007080078125, 360.3312683105469)
			vector_math_004.location = (-817.6007080078125, 540.3312377929688)
			group_input_8.location = (-1077.6007080078125, 420.3312683105469)
			vector_math.location = (-817.6007080078125, 400.3312683105469)
			integer.location = (-822.031982421875, 264.41668701171875)
			compare.location = (-526.031982421875, 831.0416870117188)
			group_014.location = (-854.4696655273438, 787.1783447265625)
			boolean_math_3.location = (-366.0320129394531, 831.0416870117188)
			switch.location = (-189.45494079589844, 480.51531982421875)
			group_012.location = (-666.031982421875, 651.0416870117188)
			switch_008.location = (120.0, 100.0)
			group_1.location = (-622.031982421875, 344.41668701171875)
			group_011.location = (-361.36767578125, 161.18844604492188)
			group_005.location = (-221.36767578125, 1.1884498596191406)
			
			#Set dimensions
			frame.width, frame.height = 688.7999877929688, 326.0
			vector_math_005.width, vector_math_005.height = 140.0, 100.0
			blur_attribute_001.width, blur_attribute_001.height = 140.0, 100.0
			switch_002.width, switch_002.height = 140.0, 100.0
			group_output_8.width, group_output_8.height = 140.0, 100.0
			index_001.width, index_001.height = 140.0, 100.0
			boolean_math_010.width, boolean_math_010.height = 140.0, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			vector_math_004.width, vector_math_004.height = 140.0, 100.0
			group_input_8.width, group_input_8.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			integer.width, integer.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			group_014.width, group_014.height = 140.0, 100.0
			boolean_math_3.width, boolean_math_3.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			group_012.width, group_012.height = 277.2730712890625, 100.0
			switch_008.width, switch_008.height = 140.0, 100.0
			group_1.width, group_1.height = 196.1611328125, 100.0
			group_011.width, group_011.height = 277.2730712890625, 100.0
			group_005.width, group_005.height = 140.0, 100.0
			
			#initialize _mn_cartoon_bs_alternate_axis links
			#vector_math_005.Vector -> switch_002.False
			_mn_cartoon_bs_alternate_axis.links.new(vector_math_005.outputs[0], switch_002.inputs[1])
			#blur_attribute_001.Value -> switch_002.True
			_mn_cartoon_bs_alternate_axis.links.new(blur_attribute_001.outputs[0], switch_002.inputs[2])
			#group_011.Is Sheet -> switch_002.Switch
			_mn_cartoon_bs_alternate_axis.links.new(group_011.outputs[1], switch_002.inputs[0])
			#group_input_8.C -> reroute_001.Input
			_mn_cartoon_bs_alternate_axis.links.new(group_input_8.outputs[1], reroute_001.inputs[0])
			#boolean_math_010.Boolean -> switch_008.Switch
			_mn_cartoon_bs_alternate_axis.links.new(boolean_math_010.outputs[0], switch_008.inputs[0])
			#group_005.is_even -> boolean_math_010.Boolean
			_mn_cartoon_bs_alternate_axis.links.new(group_005.outputs[0], boolean_math_010.inputs[1])
			#index_001.Index -> group_005.Value
			_mn_cartoon_bs_alternate_axis.links.new(index_001.outputs[0], group_005.inputs[0])
			#reroute_001.Output -> vector_math.Vector
			_mn_cartoon_bs_alternate_axis.links.new(reroute_001.outputs[0], vector_math.inputs[0])
			#group_011.Is Sheet -> boolean_math_010.Boolean
			_mn_cartoon_bs_alternate_axis.links.new(group_011.outputs[1], boolean_math_010.inputs[0])
			#reroute_001.Output -> vector_math_004.Vector
			_mn_cartoon_bs_alternate_axis.links.new(reroute_001.outputs[0], vector_math_004.inputs[1])
			#vector_math_005.Vector -> blur_attribute_001.Value
			_mn_cartoon_bs_alternate_axis.links.new(vector_math_005.outputs[0], blur_attribute_001.inputs[0])
			#switch_008.Output -> vector_math_005.Scale
			_mn_cartoon_bs_alternate_axis.links.new(switch_008.outputs[0], vector_math_005.inputs[3])
			#group_input_8.O -> vector_math.Vector
			_mn_cartoon_bs_alternate_axis.links.new(group_input_8.outputs[2], vector_math.inputs[1])
			#switch_002.Output -> group_output_8.Z Vector for Euler
			_mn_cartoon_bs_alternate_axis.links.new(switch_002.outputs[0], group_output_8.inputs[0])
			#vector_math_004.Vector -> group_output_8.X Vector for Euler
			_mn_cartoon_bs_alternate_axis.links.new(vector_math_004.outputs[0], group_output_8.inputs[1])
			#group_input_8.N -> vector_math_004.Vector
			_mn_cartoon_bs_alternate_axis.links.new(group_input_8.outputs[0], vector_math_004.inputs[0])
			#switch.Output -> vector_math_005.Vector
			_mn_cartoon_bs_alternate_axis.links.new(switch.outputs[0], vector_math_005.inputs[0])
			#group_014.Leading -> compare.A
			_mn_cartoon_bs_alternate_axis.links.new(group_014.outputs[0], compare.inputs[2])
			#group_014.Trailing -> compare.B
			_mn_cartoon_bs_alternate_axis.links.new(group_014.outputs[1], compare.inputs[3])
			#compare.Result -> boolean_math_3.Boolean
			_mn_cartoon_bs_alternate_axis.links.new(compare.outputs[0], boolean_math_3.inputs[0])
			#group_012.Is Helix -> boolean_math_3.Boolean
			_mn_cartoon_bs_alternate_axis.links.new(group_012.outputs[0], boolean_math_3.inputs[1])
			#vector_math.Vector -> switch.False
			_mn_cartoon_bs_alternate_axis.links.new(vector_math.outputs[0], switch.inputs[1])
			#vector_math.Vector -> group_1.Field
			_mn_cartoon_bs_alternate_axis.links.new(vector_math.outputs[0], group_1.inputs[0])
			#group_1.Field -> switch.True
			_mn_cartoon_bs_alternate_axis.links.new(group_1.outputs[0], switch.inputs[2])
			#integer.Integer -> group_1.Offset
			_mn_cartoon_bs_alternate_axis.links.new(integer.outputs[0], group_1.inputs[4])
			#boolean_math_3.Boolean -> switch.Switch
			_mn_cartoon_bs_alternate_axis.links.new(boolean_math_3.outputs[0], switch.inputs[0])
			return _mn_cartoon_bs_alternate_axis

		_mn_cartoon_bs_alternate_axis = _mn_cartoon_bs_alternate_axis_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".MN_cartoon_bs_alternate_axis", type = 'NODES')
		mod.node_group = _mn_cartoon_bs_alternate_axis
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_MN_cartoon_bs_alternate_axis.bl_idname)
			
def register():
	bpy.utils.register_class(_MN_cartoon_bs_alternate_axis)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_MN_cartoon_bs_alternate_axis)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
