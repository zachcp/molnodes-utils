bl_info = {
	"name" : ".atoms_to_curves",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _atoms_to_curves(bpy.types.Operator):
	bl_idname = "node._atoms_to_curves"
	bl_label = ".atoms_to_curves"
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
			field_socket.default_value = (0.0, 0.0, 0.0)
			field_socket.min_value = -3.4028234663852886e+38
			field_socket.max_value = 3.4028234663852886e+38
			field_socket.subtype = 'NONE'
			field_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket = _field_offset.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			value_socket.default_value = False
			value_socket.attribute_domain = 'POINT'
			
			#Socket Field
			field_socket_1 = _field_offset.interface.new_socket(name = "Field", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			field_socket_1.default_value = 0
			field_socket_1.min_value = -2147483648
			field_socket_1.max_value = 2147483647
			field_socket_1.subtype = 'NONE'
			field_socket_1.attribute_domain = 'POINT'
			
			#Socket Field
			field_socket_2 = _field_offset.interface.new_socket(name = "Field", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			field_socket_2.default_value = 0.0
			field_socket_2.min_value = -3.4028234663852886e+38
			field_socket_2.max_value = 3.4028234663852886e+38
			field_socket_2.subtype = 'NONE'
			field_socket_2.attribute_domain = 'POINT'
			
			#Socket Field
			field_socket_3 = _field_offset.interface.new_socket(name = "Field", in_out='INPUT', socket_type = 'NodeSocketVector')
			field_socket_3.default_value = (0.0, 0.0, 0.0)
			field_socket_3.min_value = -3.4028234663852886e+38
			field_socket_3.max_value = 3.4028234663852886e+38
			field_socket_3.subtype = 'NONE'
			field_socket_3.attribute_domain = 'POINT'
			field_socket_3.hide_value = True
			
			#Socket Value
			value_socket_1 = _field_offset.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketBool')
			value_socket_1.default_value = False
			value_socket_1.attribute_domain = 'POINT'
			value_socket_1.hide_value = True
			
			#Socket Field
			field_socket_4 = _field_offset.interface.new_socket(name = "Field", in_out='INPUT', socket_type = 'NodeSocketInt')
			field_socket_4.default_value = 0
			field_socket_4.min_value = -2147483648
			field_socket_4.max_value = 2147483647
			field_socket_4.subtype = 'NONE'
			field_socket_4.attribute_domain = 'POINT'
			field_socket_4.hide_value = True
			
			#Socket Field
			field_socket_5 = _field_offset.interface.new_socket(name = "Field", in_out='INPUT', socket_type = 'NodeSocketFloat')
			field_socket_5.default_value = 0.0
			field_socket_5.min_value = -3.4028234663852886e+38
			field_socket_5.max_value = 3.4028234663852886e+38
			field_socket_5.subtype = 'NONE'
			field_socket_5.attribute_domain = 'POINT'
			field_socket_5.hide_value = True
			
			#Socket Offset
			offset_socket = _field_offset.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket.default_value = 0
			offset_socket.min_value = -2147483648
			offset_socket.max_value = 2147483647
			offset_socket.subtype = 'NONE'
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

		#initialize _mn_select_sec_struct_id node group
		def _mn_select_sec_struct_id_node_group():
			_mn_select_sec_struct_id = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_select_sec_struct_id")

			_mn_select_sec_struct_id.color_tag = 'NONE'
			_mn_select_sec_struct_id.description = ""

			
			#_mn_select_sec_struct_id interface
			#Socket Selection
			selection_socket = _mn_select_sec_struct_id.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket.default_value = False
			selection_socket.attribute_domain = 'POINT'
			selection_socket.description = "The calculated selection"
			
			#Socket Inverted
			inverted_socket = _mn_select_sec_struct_id.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket.default_value = False
			inverted_socket.attribute_domain = 'POINT'
			
			#Socket And
			and_socket = _mn_select_sec_struct_id.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket.default_value = True
			and_socket.attribute_domain = 'POINT'
			and_socket.hide_value = True
			
			#Socket Or
			or_socket = _mn_select_sec_struct_id.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket.default_value = False
			or_socket.attribute_domain = 'POINT'
			or_socket.hide_value = True
			
			#Socket id
			id_socket = _mn_select_sec_struct_id.interface.new_socket(name = "id", in_out='INPUT', socket_type = 'NodeSocketInt')
			id_socket.default_value = 1
			id_socket.min_value = -2147483648
			id_socket.max_value = 2147483647
			id_socket.subtype = 'NONE'
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
			boolean_math = _mn_select_sec_struct_id.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'AND'
			
			#node Group Output
			group_output_1 = _mn_select_sec_struct_id.nodes.new("NodeGroupOutput")
			group_output_1.name = "Group Output"
			group_output_1.is_active_output = True
			
			#node Compare.012
			compare_012 = _mn_select_sec_struct_id.nodes.new("FunctionNodeCompare")
			compare_012.name = "Compare.012"
			compare_012.data_type = 'INT'
			compare_012.mode = 'ELEMENT'
			compare_012.operation = 'EQUAL'
			
			#node Group Input
			group_input_1 = _mn_select_sec_struct_id.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			
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
			boolean_math.location = (400.0, 200.0)
			group_output_1.location = (760.0, 200.0)
			compare_012.location = (240.0, 100.0)
			group_input_1.location = (80.0, 100.0)
			boolean_math_001.location = (579.9999389648438, 196.54164123535156)
			boolean_math_002.location = (580.0, 60.0)
			
			#Set dimensions
			named_attribute_002.width, named_attribute_002.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			group_output_1.width, group_output_1.height = 140.0, 100.0
			compare_012.width, compare_012.height = 140.0, 100.0
			group_input_1.width, group_input_1.height = 140.0, 100.0
			boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
			boolean_math_002.width, boolean_math_002.height = 140.0, 100.0
			
			#initialize _mn_select_sec_struct_id links
			#boolean_math_001.Boolean -> group_output_1.Selection
			_mn_select_sec_struct_id.links.new(boolean_math_001.outputs[0], group_output_1.inputs[0])
			#compare_012.Result -> boolean_math.Boolean
			_mn_select_sec_struct_id.links.new(compare_012.outputs[0], boolean_math.inputs[1])
			#group_input_1.id -> compare_012.A
			_mn_select_sec_struct_id.links.new(group_input_1.outputs[2], compare_012.inputs[2])
			#group_input_1.And -> boolean_math.Boolean
			_mn_select_sec_struct_id.links.new(group_input_1.outputs[0], boolean_math.inputs[0])
			#named_attribute_002.Attribute -> compare_012.B
			_mn_select_sec_struct_id.links.new(named_attribute_002.outputs[0], compare_012.inputs[3])
			#boolean_math.Boolean -> boolean_math_001.Boolean
			_mn_select_sec_struct_id.links.new(boolean_math.outputs[0], boolean_math_001.inputs[0])
			#group_input_1.Or -> boolean_math_001.Boolean
			_mn_select_sec_struct_id.links.new(group_input_1.outputs[1], boolean_math_001.inputs[1])
			#boolean_math_001.Boolean -> boolean_math_002.Boolean
			_mn_select_sec_struct_id.links.new(boolean_math_001.outputs[0], boolean_math_002.inputs[0])
			#boolean_math_002.Boolean -> group_output_1.Inverted
			_mn_select_sec_struct_id.links.new(boolean_math_002.outputs[0], group_output_1.inputs[1])
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
			selection_socket_1.default_value = False
			selection_socket_1.attribute_domain = 'POINT'
			selection_socket_1.description = "Selected atoms form part of a sheet"
			
			#Socket Inverted
			inverted_socket_1 = is_sheet.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket_1.default_value = False
			inverted_socket_1.attribute_domain = 'POINT'
			
			#Socket And
			and_socket_1 = is_sheet.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket_1.default_value = True
			and_socket_1.attribute_domain = 'POINT'
			and_socket_1.hide_value = True
			
			#Socket Or
			or_socket_1 = is_sheet.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket_1.default_value = False
			or_socket_1.attribute_domain = 'POINT'
			or_socket_1.hide_value = True
			
			
			#initialize is_sheet nodes
			#node Group Output
			group_output_2 = is_sheet.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Group Input
			group_input_2 = is_sheet.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
			#node MN_select_sec_struct.002
			mn_select_sec_struct_002 = is_sheet.nodes.new("GeometryNodeGroup")
			mn_select_sec_struct_002.label = "Select Sec Struct"
			mn_select_sec_struct_002.name = "MN_select_sec_struct.002"
			mn_select_sec_struct_002.node_tree = _mn_select_sec_struct_id
			#Socket_1
			mn_select_sec_struct_002.inputs[2].default_value = 2
			
			
			
			
			#Set locations
			group_output_2.location = (267.00146484375, 0.0)
			group_input_2.location = (-220.0, -80.0)
			mn_select_sec_struct_002.location = (0.0, 0.0)
			
			#Set dimensions
			group_output_2.width, group_output_2.height = 140.0, 100.0
			group_input_2.width, group_input_2.height = 140.0, 100.0
			mn_select_sec_struct_002.width, mn_select_sec_struct_002.height = 217.00146484375, 100.0
			
			#initialize is_sheet links
			#mn_select_sec_struct_002.Selection -> group_output_2.Selection
			is_sheet.links.new(mn_select_sec_struct_002.outputs[0], group_output_2.inputs[0])
			#group_input_2.And -> mn_select_sec_struct_002.And
			is_sheet.links.new(group_input_2.outputs[0], mn_select_sec_struct_002.inputs[0])
			#group_input_2.Or -> mn_select_sec_struct_002.Or
			is_sheet.links.new(group_input_2.outputs[1], mn_select_sec_struct_002.inputs[1])
			#mn_select_sec_struct_002.Inverted -> group_output_2.Inverted
			is_sheet.links.new(mn_select_sec_struct_002.outputs[1], group_output_2.inputs[1])
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
			selection_socket_2.default_value = False
			selection_socket_2.attribute_domain = 'POINT'
			selection_socket_2.description = "Selected atoms form part of a loop, and not part of any secondary structure"
			
			#Socket Inverted
			inverted_socket_2 = is_loop.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket_2.default_value = False
			inverted_socket_2.attribute_domain = 'POINT'
			
			#Socket And
			and_socket_2 = is_loop.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket_2.default_value = True
			and_socket_2.attribute_domain = 'POINT'
			and_socket_2.hide_value = True
			
			#Socket Or
			or_socket_2 = is_loop.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket_2.default_value = False
			or_socket_2.attribute_domain = 'POINT'
			or_socket_2.hide_value = True
			
			
			#initialize is_loop nodes
			#node Group Output
			group_output_3 = is_loop.nodes.new("NodeGroupOutput")
			group_output_3.name = "Group Output"
			group_output_3.is_active_output = True
			
			#node Group Input
			group_input_3 = is_loop.nodes.new("NodeGroupInput")
			group_input_3.name = "Group Input"
			
			#node MN_select_sec_struct.002
			mn_select_sec_struct_002_1 = is_loop.nodes.new("GeometryNodeGroup")
			mn_select_sec_struct_002_1.label = "Select Sec Struct"
			mn_select_sec_struct_002_1.name = "MN_select_sec_struct.002"
			mn_select_sec_struct_002_1.node_tree = _mn_select_sec_struct_id
			#Socket_1
			mn_select_sec_struct_002_1.inputs[2].default_value = 3
			
			
			
			
			#Set locations
			group_output_3.location = (267.00146484375, 0.0)
			group_input_3.location = (-200.0, 0.0)
			mn_select_sec_struct_002_1.location = (0.0, 0.0)
			
			#Set dimensions
			group_output_3.width, group_output_3.height = 140.0, 100.0
			group_input_3.width, group_input_3.height = 140.0, 100.0
			mn_select_sec_struct_002_1.width, mn_select_sec_struct_002_1.height = 217.00146484375, 100.0
			
			#initialize is_loop links
			#mn_select_sec_struct_002_1.Selection -> group_output_3.Selection
			is_loop.links.new(mn_select_sec_struct_002_1.outputs[0], group_output_3.inputs[0])
			#group_input_3.And -> mn_select_sec_struct_002_1.And
			is_loop.links.new(group_input_3.outputs[0], mn_select_sec_struct_002_1.inputs[0])
			#group_input_3.Or -> mn_select_sec_struct_002_1.Or
			is_loop.links.new(group_input_3.outputs[1], mn_select_sec_struct_002_1.inputs[1])
			#mn_select_sec_struct_002_1.Inverted -> group_output_3.Inverted
			is_loop.links.new(mn_select_sec_struct_002_1.outputs[1], group_output_3.inputs[1])
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
			selection_socket_3.default_value = False
			selection_socket_3.attribute_domain = 'POINT'
			selection_socket_3.description = "Selected atoms form part of an helix"
			
			#Socket Inverted
			inverted_socket_3 = is_helix.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket_3.default_value = False
			inverted_socket_3.attribute_domain = 'POINT'
			
			#Socket And
			and_socket_3 = is_helix.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket_3.default_value = True
			and_socket_3.attribute_domain = 'POINT'
			and_socket_3.hide_value = True
			
			#Socket Or
			or_socket_3 = is_helix.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket_3.default_value = False
			or_socket_3.attribute_domain = 'POINT'
			or_socket_3.hide_value = True
			
			
			#initialize is_helix nodes
			#node Group Output
			group_output_4 = is_helix.nodes.new("NodeGroupOutput")
			group_output_4.name = "Group Output"
			group_output_4.is_active_output = True
			
			#node Group Input
			group_input_4 = is_helix.nodes.new("NodeGroupInput")
			group_input_4.name = "Group Input"
			
			#node MN_select_sec_struct.002
			mn_select_sec_struct_002_2 = is_helix.nodes.new("GeometryNodeGroup")
			mn_select_sec_struct_002_2.label = "Select Sec Struct"
			mn_select_sec_struct_002_2.name = "MN_select_sec_struct.002"
			mn_select_sec_struct_002_2.node_tree = _mn_select_sec_struct_id
			#Socket_1
			mn_select_sec_struct_002_2.inputs[2].default_value = 1
			
			
			
			
			#Set locations
			group_output_4.location = (267.00146484375, 0.0)
			group_input_4.location = (-200.0, 0.0)
			mn_select_sec_struct_002_2.location = (0.0, 0.0)
			
			#Set dimensions
			group_output_4.width, group_output_4.height = 140.0, 100.0
			group_input_4.width, group_input_4.height = 140.0, 100.0
			mn_select_sec_struct_002_2.width, mn_select_sec_struct_002_2.height = 217.00146484375, 100.0
			
			#initialize is_helix links
			#mn_select_sec_struct_002_2.Selection -> group_output_4.Selection
			is_helix.links.new(mn_select_sec_struct_002_2.outputs[0], group_output_4.inputs[0])
			#group_input_4.And -> mn_select_sec_struct_002_2.And
			is_helix.links.new(group_input_4.outputs[0], mn_select_sec_struct_002_2.inputs[0])
			#group_input_4.Or -> mn_select_sec_struct_002_2.Or
			is_helix.links.new(group_input_4.outputs[1], mn_select_sec_struct_002_2.inputs[1])
			#mn_select_sec_struct_002_2.Inverted -> group_output_4.Inverted
			is_helix.links.new(mn_select_sec_struct_002_2.outputs[1], group_output_4.inputs[1])
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
			is_helix_socket.default_value = False
			is_helix_socket.attribute_domain = 'POINT'
			
			#Socket Is Sheet
			is_sheet_socket = _mn_select_sec_struct.interface.new_socket(name = "Is Sheet", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_sheet_socket.default_value = False
			is_sheet_socket.attribute_domain = 'POINT'
			
			#Socket Is Structured
			is_structured_socket = _mn_select_sec_struct.interface.new_socket(name = "Is Structured", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_structured_socket.default_value = False
			is_structured_socket.attribute_domain = 'POINT'
			
			#Socket Is Loop
			is_loop_socket = _mn_select_sec_struct.interface.new_socket(name = "Is Loop", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_loop_socket.default_value = False
			is_loop_socket.attribute_domain = 'POINT'
			
			#Socket And
			and_socket_4 = _mn_select_sec_struct.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket_4.default_value = True
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
			group_output_5 = _mn_select_sec_struct.nodes.new("NodeGroupOutput")
			group_output_5.name = "Group Output"
			group_output_5.is_active_output = True
			
			#node Group Input
			group_input_5 = _mn_select_sec_struct.nodes.new("NodeGroupInput")
			group_input_5.name = "Group Input"
			group_input_5.outputs[1].hide = True
			
			
			
			
			#Set locations
			group_001.location = (120.0, -60.0)
			group_002.location = (120.0, -180.0)
			group.location = (120.0, 60.0)
			boolean_math_001_1.location = (300.0, -140.0)
			group_output_5.location = (540.0, -60.0)
			group_input_5.location = (-160.0, -40.0)
			
			#Set dimensions
			group_001.width, group_001.height = 140.0, 100.0
			group_002.width, group_002.height = 140.0, 100.0
			group.width, group.height = 140.0, 100.0
			boolean_math_001_1.width, boolean_math_001_1.height = 140.0, 100.0
			group_output_5.width, group_output_5.height = 140.0, 100.0
			group_input_5.width, group_input_5.height = 140.0, 100.0
			
			#initialize _mn_select_sec_struct links
			#group_002.Selection -> group_output_5.Is Loop
			_mn_select_sec_struct.links.new(group_002.outputs[0], group_output_5.inputs[3])
			#group_002.Selection -> boolean_math_001_1.Boolean
			_mn_select_sec_struct.links.new(group_002.outputs[0], boolean_math_001_1.inputs[0])
			#boolean_math_001_1.Boolean -> group_output_5.Is Structured
			_mn_select_sec_struct.links.new(boolean_math_001_1.outputs[0], group_output_5.inputs[2])
			#group.Selection -> group_output_5.Is Helix
			_mn_select_sec_struct.links.new(group.outputs[0], group_output_5.inputs[0])
			#group_001.Selection -> group_output_5.Is Sheet
			_mn_select_sec_struct.links.new(group_001.outputs[0], group_output_5.inputs[1])
			#group_input_5.And -> group.And
			_mn_select_sec_struct.links.new(group_input_5.outputs[0], group.inputs[0])
			#group_input_5.And -> group_001.And
			_mn_select_sec_struct.links.new(group_input_5.outputs[0], group_001.inputs[0])
			#group_input_5.And -> group_002.And
			_mn_select_sec_struct.links.new(group_input_5.outputs[0], group_002.inputs[0])
			return _mn_select_sec_struct

		_mn_select_sec_struct = _mn_select_sec_struct_node_group()

		#initialize _field_offset_vec node group
		def _field_offset_vec_node_group():
			_field_offset_vec = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".field_offset_vec")

			_field_offset_vec.color_tag = 'NONE'
			_field_offset_vec.description = ""

			
			#_field_offset_vec interface
			#Socket Field
			field_socket_6 = _field_offset_vec.interface.new_socket(name = "Field", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			field_socket_6.default_value = (0.0, 0.0, 0.0)
			field_socket_6.min_value = -3.4028234663852886e+38
			field_socket_6.max_value = 3.4028234663852886e+38
			field_socket_6.subtype = 'NONE'
			field_socket_6.attribute_domain = 'POINT'
			
			#Socket Field
			field_socket_7 = _field_offset_vec.interface.new_socket(name = "Field", in_out='INPUT', socket_type = 'NodeSocketVector')
			field_socket_7.default_value = (0.0, 0.0, 0.0)
			field_socket_7.min_value = -3.4028234663852886e+38
			field_socket_7.max_value = 3.4028234663852886e+38
			field_socket_7.subtype = 'NONE'
			field_socket_7.attribute_domain = 'POINT'
			field_socket_7.hide_value = True
			
			#Socket Offset
			offset_socket_1 = _field_offset_vec.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket_1.default_value = 0
			offset_socket_1.min_value = -2147483648
			offset_socket_1.max_value = 2147483647
			offset_socket_1.subtype = 'NONE'
			offset_socket_1.attribute_domain = 'POINT'
			
			
			#initialize _field_offset_vec nodes
			#node Group Input
			group_input_6 = _field_offset_vec.nodes.new("NodeGroupInput")
			group_input_6.name = "Group Input"
			
			#node Evaluate at Index
			evaluate_at_index_1 = _field_offset_vec.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_1.name = "Evaluate at Index"
			evaluate_at_index_1.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_1.domain = 'POINT'
			
			#node Group Output
			group_output_6 = _field_offset_vec.nodes.new("NodeGroupOutput")
			group_output_6.name = "Group Output"
			group_output_6.is_active_output = True
			
			#node Math.001
			math_001_1 = _field_offset_vec.nodes.new("ShaderNodeMath")
			math_001_1.name = "Math.001"
			math_001_1.operation = 'ADD'
			math_001_1.use_clamp = False
			
			#node Index
			index_1 = _field_offset_vec.nodes.new("GeometryNodeInputIndex")
			index_1.name = "Index"
			
			
			
			
			#Set locations
			group_input_6.location = (-417.64404296875, 0.0)
			evaluate_at_index_1.location = (-220.0, 100.0)
			group_output_6.location = (20.0, 20.0)
			math_001_1.location = (-220.0, -80.0)
			index_1.location = (-400.0, -180.0)
			
			#Set dimensions
			group_input_6.width, group_input_6.height = 140.0, 100.0
			evaluate_at_index_1.width, evaluate_at_index_1.height = 140.0, 100.0
			group_output_6.width, group_output_6.height = 140.0, 100.0
			math_001_1.width, math_001_1.height = 140.0, 100.0
			index_1.width, index_1.height = 140.0, 100.0
			
			#initialize _field_offset_vec links
			#math_001_1.Value -> evaluate_at_index_1.Index
			_field_offset_vec.links.new(math_001_1.outputs[0], evaluate_at_index_1.inputs[0])
			#group_input_6.Field -> evaluate_at_index_1.Value
			_field_offset_vec.links.new(group_input_6.outputs[0], evaluate_at_index_1.inputs[1])
			#group_input_6.Offset -> math_001_1.Value
			_field_offset_vec.links.new(group_input_6.outputs[1], math_001_1.inputs[0])
			#evaluate_at_index_1.Value -> group_output_6.Field
			_field_offset_vec.links.new(evaluate_at_index_1.outputs[0], group_output_6.inputs[0])
			#index_1.Index -> math_001_1.Value
			_field_offset_vec.links.new(index_1.outputs[0], math_001_1.inputs[1])
			return _field_offset_vec

		_field_offset_vec = _field_offset_vec_node_group()

		#initialize _sec_struct_counter node group
		def _sec_struct_counter_node_group():
			_sec_struct_counter = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".sec_struct_counter")

			_sec_struct_counter.color_tag = 'NONE'
			_sec_struct_counter.description = ""

			
			#_sec_struct_counter interface
			#Socket Leading
			leading_socket = _sec_struct_counter.interface.new_socket(name = "Leading", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			leading_socket.default_value = 0
			leading_socket.min_value = -2147483648
			leading_socket.max_value = 2147483647
			leading_socket.subtype = 'NONE'
			leading_socket.attribute_domain = 'POINT'
			
			#Socket Trailing
			trailing_socket = _sec_struct_counter.interface.new_socket(name = "Trailing", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			trailing_socket.default_value = 0
			trailing_socket.min_value = -2147483648
			trailing_socket.max_value = 2147483647
			trailing_socket.subtype = 'NONE'
			trailing_socket.attribute_domain = 'POINT'
			
			#Socket Total
			total_socket = _sec_struct_counter.interface.new_socket(name = "Total", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			total_socket.default_value = 0
			total_socket.min_value = -2147483648
			total_socket.max_value = 2147483647
			total_socket.subtype = 'NONE'
			total_socket.attribute_domain = 'POINT'
			
			#Socket Border
			border_socket = _sec_struct_counter.interface.new_socket(name = "Border", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			border_socket.default_value = False
			border_socket.attribute_domain = 'POINT'
			
			
			#initialize _sec_struct_counter nodes
			#node Group Input
			group_input_7 = _sec_struct_counter.nodes.new("NodeGroupInput")
			group_input_7.name = "Group Input"
			
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
			boolean_math_1 = _sec_struct_counter.nodes.new("FunctionNodeBooleanMath")
			boolean_math_1.name = "Boolean Math"
			boolean_math_1.operation = 'OR'
			#Boolean_001
			boolean_math_1.inputs[1].default_value = False
			
			#node Group Output
			group_output_7 = _sec_struct_counter.nodes.new("NodeGroupOutput")
			group_output_7.name = "Group Output"
			group_output_7.is_active_output = True
			
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
			group_input_7.location = (-500.1279296875, 0.0)
			reroute_005.location = (-119.8720703125, -60.0)
			named_attribute_001.location = (-300.0, 120.0)
			group_004.location = (-20.0, -220.0)
			compare_009.location = (140.1279296875, 60.0)
			accumulate_field_004.location = (460.0, 40.0)
			compare_010.location = (140.0, -140.0)
			reroute.location = (320.0, -60.0)
			boolean_math_1.location = (300.0, -140.0)
			group_output_7.location = (796.4706420898438, 27.943008422851562)
			group_003.location = (-19.8720703125, 60.0)
			
			#Set dimensions
			group_input_7.width, group_input_7.height = 140.0, 100.0
			reroute_005.width, reroute_005.height = 16.0, 100.0
			named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
			group_004.width, group_004.height = 140.0, 100.0
			compare_009.width, compare_009.height = 140.0, 100.0
			accumulate_field_004.width, accumulate_field_004.height = 140.0, 100.0
			compare_010.width, compare_010.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			boolean_math_1.width, boolean_math_1.height = 140.0, 100.0
			group_output_7.width, group_output_7.height = 140.0, 100.0
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
			#accumulate_field_004.Trailing -> group_output_7.Trailing
			_sec_struct_counter.links.new(accumulate_field_004.outputs[1], group_output_7.inputs[1])
			#accumulate_field_004.Leading -> group_output_7.Leading
			_sec_struct_counter.links.new(accumulate_field_004.outputs[0], group_output_7.inputs[0])
			#accumulate_field_004.Total -> group_output_7.Total
			_sec_struct_counter.links.new(accumulate_field_004.outputs[2], group_output_7.inputs[2])
			#reroute.Output -> group_output_7.Border
			_sec_struct_counter.links.new(reroute.outputs[0], group_output_7.inputs[3])
			#reroute_005.Output -> group_004.Field
			_sec_struct_counter.links.new(reroute_005.outputs[0], group_004.inputs[2])
			#reroute_005.Output -> compare_010.A
			_sec_struct_counter.links.new(reroute_005.outputs[0], compare_010.inputs[2])
			#group_004.Field -> compare_010.B
			_sec_struct_counter.links.new(group_004.outputs[2], compare_010.inputs[3])
			#compare_009.Result -> reroute.Input
			_sec_struct_counter.links.new(compare_009.outputs[0], reroute.inputs[0])
			#compare_010.Result -> boolean_math_1.Boolean
			_sec_struct_counter.links.new(compare_010.outputs[0], boolean_math_1.inputs[0])
			return _sec_struct_counter

		_sec_struct_counter = _sec_struct_counter_node_group()

		#initialize _bs_smooth node group
		def _bs_smooth_node_group():
			_bs_smooth = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".bs_smooth")

			_bs_smooth.color_tag = 'NONE'
			_bs_smooth.description = ""

			_bs_smooth.is_modifier = True
			
			#_bs_smooth interface
			#Socket Geometry
			geometry_socket = _bs_smooth.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_1 = _bs_smooth.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_1.attribute_domain = 'POINT'
			
			#Socket Factor
			factor_socket = _bs_smooth.interface.new_socket(name = "Factor", in_out='INPUT', socket_type = 'NodeSocketFloat')
			factor_socket.default_value = 1.0
			factor_socket.min_value = 0.0
			factor_socket.max_value = 1.0
			factor_socket.subtype = 'FACTOR'
			factor_socket.attribute_domain = 'POINT'
			
			#Socket Iterations
			iterations_socket = _bs_smooth.interface.new_socket(name = "Iterations", in_out='INPUT', socket_type = 'NodeSocketInt')
			iterations_socket.default_value = 2
			iterations_socket.min_value = 0
			iterations_socket.max_value = 2147483647
			iterations_socket.subtype = 'NONE'
			iterations_socket.attribute_domain = 'POINT'
			
			
			#initialize _bs_smooth nodes
			#node Group Output
			group_output_8 = _bs_smooth.nodes.new("NodeGroupOutput")
			group_output_8.name = "Group Output"
			group_output_8.is_active_output = True
			
			#node Set Position
			set_position = _bs_smooth.nodes.new("GeometryNodeSetPosition")
			set_position.name = "Set Position"
			#Offset
			set_position.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Mix.002
			mix_002 = _bs_smooth.nodes.new("ShaderNodeMix")
			mix_002.name = "Mix.002"
			mix_002.blend_type = 'MIX'
			mix_002.clamp_factor = True
			mix_002.clamp_result = False
			mix_002.data_type = 'VECTOR'
			mix_002.factor_mode = 'UNIFORM'
			
			#node Position.001
			position_001 = _bs_smooth.nodes.new("GeometryNodeInputPosition")
			position_001.name = "Position.001"
			
			#node Blur Attribute
			blur_attribute = _bs_smooth.nodes.new("GeometryNodeBlurAttribute")
			blur_attribute.name = "Blur Attribute"
			blur_attribute.data_type = 'FLOAT_VECTOR'
			
			#node Group Input
			group_input_8 = _bs_smooth.nodes.new("NodeGroupInput")
			group_input_8.name = "Group Input"
			
			#node Boolean Math.004
			boolean_math_004 = _bs_smooth.nodes.new("FunctionNodeBooleanMath")
			boolean_math_004.name = "Boolean Math.004"
			boolean_math_004.operation = 'NOT'
			
			#node Boolean Math.002
			boolean_math_002_1 = _bs_smooth.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_1.name = "Boolean Math.002"
			boolean_math_002_1.operation = 'AND'
			
			#node Group
			group_1 = _bs_smooth.nodes.new("GeometryNodeGroup")
			group_1.name = "Group"
			group_1.node_tree = _sec_struct_counter
			
			#node Endpoint Selection.004
			endpoint_selection_004 = _bs_smooth.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_004.name = "Endpoint Selection.004"
			#Start Size
			endpoint_selection_004.inputs[0].default_value = 1
			#End Size
			endpoint_selection_004.inputs[1].default_value = 1
			
			#node Boolean Math
			boolean_math_2 = _bs_smooth.nodes.new("FunctionNodeBooleanMath")
			boolean_math_2.name = "Boolean Math"
			boolean_math_2.operation = 'NOT'
			
			#node Group.021
			group_021 = _bs_smooth.nodes.new("GeometryNodeGroup")
			group_021.name = "Group.021"
			group_021.node_tree = _mn_select_sec_struct
			group_021.outputs[0].hide = True
			group_021.outputs[2].hide = True
			group_021.outputs[3].hide = True
			#Socket_1
			group_021.inputs[0].default_value = True
			
			
			
			
			#Set locations
			group_output_8.location = (591.18408203125, 0.0)
			set_position.location = (401.18408203125, 199.23532104492188)
			mix_002.location = (218.81591796875, 80.76467895507812)
			position_001.location = (-61.18408203125, -39.235321044921875)
			blur_attribute.location = (-58.81591796875, -120.76467895507812)
			group_input_8.location = (-615.6842041015625, 115.17381286621094)
			boolean_math_004.location = (-380.0, -160.0)
			boolean_math_002_1.location = (39.807212829589844, 161.80430603027344)
			group_1.location = (-620.0, -40.0)
			endpoint_selection_004.location = (-620.0, -280.0)
			boolean_math_2.location = (-120.0, 140.0)
			group_021.location = (40.0, 260.0)
			
			#Set dimensions
			group_output_8.width, group_output_8.height = 140.0, 100.0
			set_position.width, set_position.height = 140.0, 100.0
			mix_002.width, mix_002.height = 140.0, 100.0
			position_001.width, position_001.height = 140.0, 100.0
			blur_attribute.width, blur_attribute.height = 140.0, 100.0
			group_input_8.width, group_input_8.height = 140.0, 100.0
			boolean_math_004.width, boolean_math_004.height = 140.0, 100.0
			boolean_math_002_1.width, boolean_math_002_1.height = 140.0, 100.0
			group_1.width, group_1.height = 140.0, 100.0
			endpoint_selection_004.width, endpoint_selection_004.height = 140.0, 100.0
			boolean_math_2.width, boolean_math_2.height = 140.0, 100.0
			group_021.width, group_021.height = 140.0, 100.0
			
			#initialize _bs_smooth links
			#boolean_math_004.Boolean -> blur_attribute.Weight
			_bs_smooth.links.new(boolean_math_004.outputs[0], blur_attribute.inputs[2])
			#blur_attribute.Value -> mix_002.B
			_bs_smooth.links.new(blur_attribute.outputs[0], mix_002.inputs[5])
			#position_001.Position -> blur_attribute.Value
			_bs_smooth.links.new(position_001.outputs[0], blur_attribute.inputs[0])
			#mix_002.Result -> set_position.Position
			_bs_smooth.links.new(mix_002.outputs[1], set_position.inputs[2])
			#position_001.Position -> mix_002.A
			_bs_smooth.links.new(position_001.outputs[0], mix_002.inputs[4])
			#group_021.Is Sheet -> boolean_math_002_1.Boolean
			_bs_smooth.links.new(group_021.outputs[1], boolean_math_002_1.inputs[0])
			#group_input_8.Geometry -> set_position.Geometry
			_bs_smooth.links.new(group_input_8.outputs[0], set_position.inputs[0])
			#group_input_8.Factor -> mix_002.Factor
			_bs_smooth.links.new(group_input_8.outputs[1], mix_002.inputs[0])
			#set_position.Geometry -> group_output_8.Geometry
			_bs_smooth.links.new(set_position.outputs[0], group_output_8.inputs[0])
			#group_input_8.Iterations -> blur_attribute.Iterations
			_bs_smooth.links.new(group_input_8.outputs[2], blur_attribute.inputs[1])
			#group_1.Border -> boolean_math_2.Boolean
			_bs_smooth.links.new(group_1.outputs[3], boolean_math_2.inputs[0])
			#boolean_math_002_1.Boolean -> set_position.Selection
			_bs_smooth.links.new(boolean_math_002_1.outputs[0], set_position.inputs[1])
			#boolean_math_2.Boolean -> boolean_math_002_1.Boolean
			_bs_smooth.links.new(boolean_math_2.outputs[0], boolean_math_002_1.inputs[1])
			#group_1.Border -> boolean_math_004.Boolean
			_bs_smooth.links.new(group_1.outputs[3], boolean_math_004.inputs[0])
			return _bs_smooth

		_bs_smooth = _bs_smooth_node_group()

		#initialize _expand_selection node group
		def _expand_selection_node_group():
			_expand_selection = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".expand_selection")

			_expand_selection.color_tag = 'NONE'
			_expand_selection.description = ""

			
			#_expand_selection interface
			#Socket Boolean
			boolean_socket = _expand_selection.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket.default_value = False
			boolean_socket.attribute_domain = 'POINT'
			
			#Socket Input
			input_socket = _expand_selection.interface.new_socket(name = "Input", in_out='INPUT', socket_type = 'NodeSocketBool')
			input_socket.default_value = False
			input_socket.attribute_domain = 'POINT'
			
			#Socket Offset
			offset_socket_2 = _expand_selection.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket_2.default_value = 1
			offset_socket_2.min_value = -2147483648
			offset_socket_2.max_value = 2147483647
			offset_socket_2.subtype = 'NONE'
			offset_socket_2.attribute_domain = 'POINT'
			
			
			#initialize _expand_selection nodes
			#node Group Output
			group_output_9 = _expand_selection.nodes.new("NodeGroupOutput")
			group_output_9.name = "Group Output"
			group_output_9.is_active_output = True
			
			#node Boolean Math
			boolean_math_3 = _expand_selection.nodes.new("FunctionNodeBooleanMath")
			boolean_math_3.name = "Boolean Math"
			boolean_math_3.operation = 'OR'
			
			#node Boolean Math.001
			boolean_math_001_2 = _expand_selection.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_2.name = "Boolean Math.001"
			boolean_math_001_2.operation = 'OR'
			
			#node Group.025
			group_025 = _expand_selection.nodes.new("GeometryNodeGroup")
			group_025.name = "Group.025"
			group_025.node_tree = _field_offset
			#Input_0
			group_025.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Input_5
			group_025.inputs[2].default_value = 0
			#Input_7
			group_025.inputs[3].default_value = 0.0
			
			#node Group Input
			group_input_9 = _expand_selection.nodes.new("NodeGroupInput")
			group_input_9.name = "Group Input"
			
			#node Math
			math = _expand_selection.nodes.new("ShaderNodeMath")
			math.name = "Math"
			math.operation = 'MULTIPLY'
			math.use_clamp = False
			#Value_001
			math.inputs[1].default_value = -1.0
			
			#node Group.024
			group_024 = _expand_selection.nodes.new("GeometryNodeGroup")
			group_024.name = "Group.024"
			group_024.node_tree = _field_offset
			#Input_0
			group_024.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Input_5
			group_024.inputs[2].default_value = 0
			#Input_7
			group_024.inputs[3].default_value = 0.0
			
			
			
			
			#Set locations
			group_output_9.location = (420.0, 0.0)
			boolean_math_3.location = (-50.0, 0.0)
			boolean_math_001_2.location = (230.0, 60.0)
			group_025.location = (-230.0, -140.0)
			group_input_9.location = (-637.21630859375, 234.8535614013672)
			math.location = (-640.0, 120.0)
			group_024.location = (-230.0, 140.0)
			
			#Set dimensions
			group_output_9.width, group_output_9.height = 140.0, 100.0
			boolean_math_3.width, boolean_math_3.height = 140.0, 100.0
			boolean_math_001_2.width, boolean_math_001_2.height = 140.0, 100.0
			group_025.width, group_025.height = 140.0, 100.0
			group_input_9.width, group_input_9.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			group_024.width, group_024.height = 140.0, 100.0
			
			#initialize _expand_selection links
			#group_025.Value -> boolean_math_3.Boolean
			_expand_selection.links.new(group_025.outputs[1], boolean_math_3.inputs[1])
			#group_input_9.Input -> group_025.Value
			_expand_selection.links.new(group_input_9.outputs[0], group_025.inputs[1])
			#group_input_9.Input -> group_024.Value
			_expand_selection.links.new(group_input_9.outputs[0], group_024.inputs[1])
			#group_024.Value -> boolean_math_3.Boolean
			_expand_selection.links.new(group_024.outputs[1], boolean_math_3.inputs[0])
			#boolean_math_3.Boolean -> boolean_math_001_2.Boolean
			_expand_selection.links.new(boolean_math_3.outputs[0], boolean_math_001_2.inputs[1])
			#group_input_9.Input -> boolean_math_001_2.Boolean
			_expand_selection.links.new(group_input_9.outputs[0], boolean_math_001_2.inputs[0])
			#boolean_math_001_2.Boolean -> group_output_9.Boolean
			_expand_selection.links.new(boolean_math_001_2.outputs[0], group_output_9.inputs[0])
			#group_input_9.Offset -> group_024.Offset
			_expand_selection.links.new(group_input_9.outputs[1], group_024.inputs[4])
			#group_input_9.Offset -> math.Value
			_expand_selection.links.new(group_input_9.outputs[1], math.inputs[0])
			#math.Value -> group_025.Offset
			_expand_selection.links.new(math.outputs[0], group_025.inputs[4])
			return _expand_selection

		_expand_selection = _expand_selection_node_group()

		#initialize fallback_boolean node group
		def fallback_boolean_node_group():
			fallback_boolean = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Fallback Boolean")

			fallback_boolean.color_tag = 'INPUT'
			fallback_boolean.description = "Computes the boolean field if the given attribute doesn't exist. If it doesn't exist it just uses the attribute instead"

			
			#fallback_boolean interface
			#Socket Boolean
			boolean_socket_1 = fallback_boolean.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket_1.default_value = False
			boolean_socket_1.attribute_domain = 'POINT'
			
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
			group_output_10 = fallback_boolean.nodes.new("NodeGroupOutput")
			group_output_10.name = "Group Output"
			group_output_10.is_active_output = True
			
			#node Group Input
			group_input_10 = fallback_boolean.nodes.new("NodeGroupInput")
			group_input_10.name = "Group Input"
			
			#node Named Attribute
			named_attribute = fallback_boolean.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'BOOLEAN'
			
			#node Switch
			switch = fallback_boolean.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'BOOLEAN'
			
			
			
			
			#Set locations
			group_output_10.location = (276.6171569824219, 4.738137245178223)
			group_input_10.location = (-280.0, 0.0)
			named_attribute.location = (-94.73597717285156, 4.738137245178223)
			switch.location = (86.61715698242188, 4.738137245178223)
			
			#Set dimensions
			group_output_10.width, group_output_10.height = 140.0, 100.0
			group_input_10.width, group_input_10.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			
			#initialize fallback_boolean links
			#named_attribute.Exists -> switch.Switch
			fallback_boolean.links.new(named_attribute.outputs[1], switch.inputs[0])
			#named_attribute.Attribute -> switch.True
			fallback_boolean.links.new(named_attribute.outputs[0], switch.inputs[2])
			#group_input_10.Fallback -> switch.False
			fallback_boolean.links.new(group_input_10.outputs[1], switch.inputs[1])
			#switch.Output -> group_output_10.Boolean
			fallback_boolean.links.new(switch.outputs[0], group_output_10.inputs[0])
			#group_input_10.Name -> named_attribute.Name
			fallback_boolean.links.new(group_input_10.outputs[0], named_attribute.inputs[0])
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
			group_input_11 = _mn_constants_atom_name_peptide.nodes.new("NodeGroupInput")
			group_input_11.name = "Group Input"
			
			#node Group Output
			group_output_11 = _mn_constants_atom_name_peptide.nodes.new("NodeGroupOutput")
			group_output_11.name = "Group Output"
			group_output_11.is_active_output = True
			
			#node Integer.001
			integer_001 = _mn_constants_atom_name_peptide.nodes.new("FunctionNodeInputInt")
			integer_001.name = "Integer.001"
			integer_001.integer = 49
			
			#node Integer.004
			integer_004 = _mn_constants_atom_name_peptide.nodes.new("FunctionNodeInputInt")
			integer_004.name = "Integer.004"
			integer_004.integer = 2
			
			#node Integer
			integer = _mn_constants_atom_name_peptide.nodes.new("FunctionNodeInputInt")
			integer.name = "Integer"
			integer.integer = 5
			
			#node Integer.003
			integer_003 = _mn_constants_atom_name_peptide.nodes.new("FunctionNodeInputInt")
			integer_003.name = "Integer.003"
			integer_003.integer = 1
			
			#node Integer.002
			integer_002 = _mn_constants_atom_name_peptide.nodes.new("FunctionNodeInputInt")
			integer_002.name = "Integer.002"
			integer_002.integer = 4
			
			
			
			
			#Set locations
			group_input_11.location = (-200.0, 0.0)
			group_output_11.location = (260.0, 180.0)
			integer_001.location = (0.0, -50.0)
			integer_004.location = (0.0, -140.0)
			integer.location = (0.0, 40.0)
			integer_003.location = (0.0, 240.0)
			integer_002.location = (0.0, 140.0)
			
			#Set dimensions
			group_input_11.width, group_input_11.height = 140.0, 100.0
			group_output_11.width, group_output_11.height = 140.0, 100.0
			integer_001.width, integer_001.height = 140.0, 100.0
			integer_004.width, integer_004.height = 140.0, 100.0
			integer.width, integer.height = 140.0, 100.0
			integer_003.width, integer_003.height = 140.0, 100.0
			integer_002.width, integer_002.height = 140.0, 100.0
			
			#initialize _mn_constants_atom_name_peptide links
			#integer_003.Integer -> group_output_11.Backbone Lower
			_mn_constants_atom_name_peptide.links.new(integer_003.outputs[0], group_output_11.inputs[0])
			#integer_002.Integer -> group_output_11.Backbone Upper
			_mn_constants_atom_name_peptide.links.new(integer_002.outputs[0], group_output_11.inputs[1])
			#integer.Integer -> group_output_11.Side Chain Lower
			_mn_constants_atom_name_peptide.links.new(integer.outputs[0], group_output_11.inputs[2])
			#integer_001.Integer -> group_output_11.Side Chain Upper
			_mn_constants_atom_name_peptide.links.new(integer_001.outputs[0], group_output_11.inputs[3])
			#integer_004.Integer -> group_output_11.Alpha Carbon
			_mn_constants_atom_name_peptide.links.new(integer_004.outputs[0], group_output_11.inputs[4])
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
			group_input_12 = _mn_select_peptide.nodes.new("NodeGroupInput")
			group_input_12.name = "Group Input"
			
			#node Compare
			compare = _mn_select_peptide.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'GREATER_EQUAL'
			
			#node Compare.001
			compare_001 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'INT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'LESS_EQUAL'
			
			#node Boolean Math.001
			boolean_math_001_3 = _mn_select_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_3.name = "Boolean Math.001"
			boolean_math_001_3.operation = 'AND'
			
			#node Compare.002
			compare_002 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
			compare_002.name = "Compare.002"
			compare_002.data_type = 'INT'
			compare_002.mode = 'ELEMENT'
			compare_002.operation = 'GREATER_EQUAL'
			
			#node Compare.003
			compare_003 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
			compare_003.name = "Compare.003"
			compare_003.data_type = 'INT'
			compare_003.mode = 'ELEMENT'
			compare_003.operation = 'LESS_EQUAL'
			
			#node Boolean Math.002
			boolean_math_002_2 = _mn_select_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_2.name = "Boolean Math.002"
			boolean_math_002_2.operation = 'AND'
			
			#node Compare.004
			compare_004 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
			compare_004.name = "Compare.004"
			compare_004.data_type = 'INT'
			compare_004.mode = 'ELEMENT'
			compare_004.operation = 'GREATER_EQUAL'
			
			#node Named Attribute
			named_attribute_1 = _mn_select_peptide.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_1.name = "Named Attribute"
			named_attribute_1.data_type = 'INT'
			#Name
			named_attribute_1.inputs[0].default_value = "atom_name"
			
			#node Boolean Math.003
			boolean_math_003 = _mn_select_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003.name = "Boolean Math.003"
			boolean_math_003.operation = 'AND'
			
			#node Group Output
			group_output_12 = _mn_select_peptide.nodes.new("NodeGroupOutput")
			group_output_12.name = "Group Output"
			group_output_12.is_active_output = True
			
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
			group_2 = _mn_select_peptide.nodes.new("GeometryNodeGroup")
			group_2.name = "Group"
			group_2.node_tree = _mn_constants_atom_name_peptide
			
			#node Boolean Math
			boolean_math_4 = _mn_select_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math_4.name = "Boolean Math"
			boolean_math_4.operation = 'OR'
			
			
			
			
			#Set locations
			group_input_12.location = (-460.0, 0.0)
			compare.location = (80.0, 80.0)
			compare_001.location = (80.0, -80.0)
			boolean_math_001_3.location = (260.0, 80.0)
			compare_002.location = (80.0, -240.0)
			compare_003.location = (80.0, -400.0)
			boolean_math_002_2.location = (260.0, -240.0)
			compare_004.location = (80.0, -560.0)
			named_attribute_1.location = (-360.0, -480.0)
			boolean_math_003.location = (260.0, -560.0)
			group_output_12.location = (666.1161499023438, -263.7054748535156)
			compare_005.location = (80.0, -720.0)
			compare_006.location = (260.0, -380.0)
			group_2.location = (-411.24090576171875, -312.71807861328125)
			boolean_math_4.location = (420.0, -240.0)
			
			#Set dimensions
			group_input_12.width, group_input_12.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			boolean_math_001_3.width, boolean_math_001_3.height = 140.0, 100.0
			compare_002.width, compare_002.height = 153.86517333984375, 100.0
			compare_003.width, compare_003.height = 153.86517333984375, 100.0
			boolean_math_002_2.width, boolean_math_002_2.height = 140.0, 100.0
			compare_004.width, compare_004.height = 140.0, 100.0
			named_attribute_1.width, named_attribute_1.height = 140.0, 100.0
			boolean_math_003.width, boolean_math_003.height = 140.0, 100.0
			group_output_12.width, group_output_12.height = 140.0, 100.0
			compare_005.width, compare_005.height = 140.0, 100.0
			compare_006.width, compare_006.height = 140.0, 100.0
			group_2.width, group_2.height = 369.1165771484375, 100.0
			boolean_math_4.width, boolean_math_4.height = 140.0, 100.0
			
			#initialize _mn_select_peptide links
			#compare_001.Result -> boolean_math_001_3.Boolean
			_mn_select_peptide.links.new(compare_001.outputs[0], boolean_math_001_3.inputs[1])
			#group_2.Backbone Lower -> compare.B
			_mn_select_peptide.links.new(group_2.outputs[0], compare.inputs[3])
			#named_attribute_1.Attribute -> compare.A
			_mn_select_peptide.links.new(named_attribute_1.outputs[0], compare.inputs[2])
			#compare.Result -> boolean_math_001_3.Boolean
			_mn_select_peptide.links.new(compare.outputs[0], boolean_math_001_3.inputs[0])
			#named_attribute_1.Attribute -> compare_001.A
			_mn_select_peptide.links.new(named_attribute_1.outputs[0], compare_001.inputs[2])
			#group_2.Backbone Upper -> compare_001.B
			_mn_select_peptide.links.new(group_2.outputs[1], compare_001.inputs[3])
			#boolean_math_001_3.Boolean -> group_output_12.Is Backbone
			_mn_select_peptide.links.new(boolean_math_001_3.outputs[0], group_output_12.inputs[0])
			#compare_003.Result -> boolean_math_002_2.Boolean
			_mn_select_peptide.links.new(compare_003.outputs[0], boolean_math_002_2.inputs[1])
			#named_attribute_1.Attribute -> compare_002.A
			_mn_select_peptide.links.new(named_attribute_1.outputs[0], compare_002.inputs[2])
			#compare_002.Result -> boolean_math_002_2.Boolean
			_mn_select_peptide.links.new(compare_002.outputs[0], boolean_math_002_2.inputs[0])
			#named_attribute_1.Attribute -> compare_003.A
			_mn_select_peptide.links.new(named_attribute_1.outputs[0], compare_003.inputs[2])
			#group_2.Side Chain Lower -> compare_002.B
			_mn_select_peptide.links.new(group_2.outputs[2], compare_002.inputs[3])
			#group_2.Side Chain Upper -> compare_003.B
			_mn_select_peptide.links.new(group_2.outputs[3], compare_003.inputs[3])
			#compare_005.Result -> boolean_math_003.Boolean
			_mn_select_peptide.links.new(compare_005.outputs[0], boolean_math_003.inputs[1])
			#named_attribute_1.Attribute -> compare_004.A
			_mn_select_peptide.links.new(named_attribute_1.outputs[0], compare_004.inputs[2])
			#compare_004.Result -> boolean_math_003.Boolean
			_mn_select_peptide.links.new(compare_004.outputs[0], boolean_math_003.inputs[0])
			#named_attribute_1.Attribute -> compare_005.A
			_mn_select_peptide.links.new(named_attribute_1.outputs[0], compare_005.inputs[2])
			#group_2.Backbone Lower -> compare_004.B
			_mn_select_peptide.links.new(group_2.outputs[0], compare_004.inputs[3])
			#group_2.Side Chain Upper -> compare_005.B
			_mn_select_peptide.links.new(group_2.outputs[3], compare_005.inputs[3])
			#boolean_math_003.Boolean -> group_output_12.Is Peptide
			_mn_select_peptide.links.new(boolean_math_003.outputs[0], group_output_12.inputs[2])
			#named_attribute_1.Attribute -> compare_006.A
			_mn_select_peptide.links.new(named_attribute_1.outputs[0], compare_006.inputs[2])
			#group_2.Alpha Carbon -> compare_006.B
			_mn_select_peptide.links.new(group_2.outputs[4], compare_006.inputs[3])
			#compare_006.Result -> group_output_12.Is Alpha Carbon
			_mn_select_peptide.links.new(compare_006.outputs[0], group_output_12.inputs[3])
			#boolean_math_002_2.Boolean -> boolean_math_4.Boolean
			_mn_select_peptide.links.new(boolean_math_002_2.outputs[0], boolean_math_4.inputs[0])
			#compare_006.Result -> boolean_math_4.Boolean
			_mn_select_peptide.links.new(compare_006.outputs[0], boolean_math_4.inputs[1])
			#boolean_math_4.Boolean -> group_output_12.Is Side Chain
			_mn_select_peptide.links.new(boolean_math_4.outputs[0], group_output_12.inputs[1])
			return _mn_select_peptide

		_mn_select_peptide = _mn_select_peptide_node_group()

		#initialize is_alpha_carbon node group
		def is_alpha_carbon_node_group():
			is_alpha_carbon = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Is Alpha Carbon")

			is_alpha_carbon.color_tag = 'INPUT'
			is_alpha_carbon.description = ""

			
			#is_alpha_carbon interface
			#Socket Selection
			selection_socket_4 = is_alpha_carbon.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket_4.default_value = False
			selection_socket_4.attribute_domain = 'POINT'
			selection_socket_4.description = "True if atom is an alpha carbon of an amino acid"
			
			#Socket Inverted
			inverted_socket_4 = is_alpha_carbon.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket_4.default_value = False
			inverted_socket_4.attribute_domain = 'POINT'
			
			#Socket And
			and_socket_5 = is_alpha_carbon.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket_5.default_value = True
			and_socket_5.attribute_domain = 'POINT'
			and_socket_5.hide_value = True
			
			#Socket Or
			or_socket_4 = is_alpha_carbon.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket_4.default_value = False
			or_socket_4.attribute_domain = 'POINT'
			or_socket_4.hide_value = True
			
			
			#initialize is_alpha_carbon nodes
			#node Group Output
			group_output_13 = is_alpha_carbon.nodes.new("NodeGroupOutput")
			group_output_13.name = "Group Output"
			group_output_13.is_active_output = True
			
			#node Group Input
			group_input_13 = is_alpha_carbon.nodes.new("NodeGroupInput")
			group_input_13.name = "Group Input"
			
			#node Boolean Math.001
			boolean_math_001_4 = is_alpha_carbon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_4.name = "Boolean Math.001"
			boolean_math_001_4.operation = 'AND'
			
			#node Group.001
			group_001_1 = is_alpha_carbon.nodes.new("GeometryNodeGroup")
			group_001_1.name = "Group.001"
			group_001_1.node_tree = fallback_boolean
			#Socket_2
			group_001_1.inputs[0].default_value = "is_alpha_carbon"
			
			#node Group.002
			group_002_1 = is_alpha_carbon.nodes.new("GeometryNodeGroup")
			group_002_1.name = "Group.002"
			group_002_1.node_tree = _mn_select_peptide
			group_002_1.outputs[0].hide = True
			group_002_1.outputs[1].hide = True
			group_002_1.outputs[2].hide = True
			
			#node Boolean Math.002
			boolean_math_002_3 = is_alpha_carbon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_3.name = "Boolean Math.002"
			boolean_math_002_3.operation = 'OR'
			
			#node Boolean Math
			boolean_math_5 = is_alpha_carbon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_5.name = "Boolean Math"
			boolean_math_5.operation = 'NOT'
			
			
			
			
			#Set locations
			group_output_13.location = (520.0, 0.0)
			group_input_13.location = (-200.0, 0.0)
			boolean_math_001_4.location = (160.0, 0.0)
			group_001_1.location = (-88.33343505859375, -180.0)
			group_002_1.location = (-290.4490661621094, -180.0)
			boolean_math_002_3.location = (340.0, 0.0)
			boolean_math_5.location = (340.0, -140.0)
			
			#Set dimensions
			group_output_13.width, group_output_13.height = 140.0, 100.0
			group_input_13.width, group_input_13.height = 140.0, 100.0
			boolean_math_001_4.width, boolean_math_001_4.height = 140.0, 100.0
			group_001_1.width, group_001_1.height = 208.33343505859375, 100.0
			group_002_1.width, group_002_1.height = 170.44906616210938, 100.0
			boolean_math_002_3.width, boolean_math_002_3.height = 140.0, 100.0
			boolean_math_5.width, boolean_math_5.height = 140.0, 100.0
			
			#initialize is_alpha_carbon links
			#group_input_13.And -> boolean_math_001_4.Boolean
			is_alpha_carbon.links.new(group_input_13.outputs[0], boolean_math_001_4.inputs[0])
			#boolean_math_002_3.Boolean -> group_output_13.Selection
			is_alpha_carbon.links.new(boolean_math_002_3.outputs[0], group_output_13.inputs[0])
			#group_001_1.Boolean -> boolean_math_001_4.Boolean
			is_alpha_carbon.links.new(group_001_1.outputs[0], boolean_math_001_4.inputs[1])
			#group_002_1.Is Alpha Carbon -> group_001_1.Fallback
			is_alpha_carbon.links.new(group_002_1.outputs[3], group_001_1.inputs[1])
			#boolean_math_001_4.Boolean -> boolean_math_002_3.Boolean
			is_alpha_carbon.links.new(boolean_math_001_4.outputs[0], boolean_math_002_3.inputs[0])
			#group_input_13.Or -> boolean_math_002_3.Boolean
			is_alpha_carbon.links.new(group_input_13.outputs[1], boolean_math_002_3.inputs[1])
			#boolean_math_002_3.Boolean -> boolean_math_5.Boolean
			is_alpha_carbon.links.new(boolean_math_002_3.outputs[0], boolean_math_5.inputs[0])
			#boolean_math_5.Boolean -> group_output_13.Inverted
			is_alpha_carbon.links.new(boolean_math_5.outputs[0], group_output_13.inputs[1])
			return is_alpha_carbon

		is_alpha_carbon = is_alpha_carbon_node_group()

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
			index_socket = group_pick.interface.new_socket(name = "Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			index_socket.default_value = 0
			index_socket.min_value = 0
			index_socket.max_value = 2147483647
			index_socket.subtype = 'NONE'
			index_socket.attribute_domain = 'POINT'
			index_socket.description = "Index of picked item. Returns -1 if not a valid pick."
			
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
			group_output_14 = group_pick.nodes.new("NodeGroupOutput")
			group_output_14.name = "Group Output"
			group_output_14.is_active_output = True
			
			#node Group Input
			group_input_14 = group_pick.nodes.new("NodeGroupInput")
			group_input_14.name = "Group Input"
			
			#node Switch
			switch_1 = group_pick.nodes.new("GeometryNodeSwitch")
			switch_1.name = "Switch"
			switch_1.input_type = 'INT'
			#False
			switch_1.inputs[1].default_value = 0
			
			#node Index
			index_2 = group_pick.nodes.new("GeometryNodeInputIndex")
			index_2.name = "Index"
			
			#node Accumulate Field
			accumulate_field = group_pick.nodes.new("GeometryNodeAccumulateField")
			accumulate_field.name = "Accumulate Field"
			accumulate_field.data_type = 'INT'
			accumulate_field.domain = 'POINT'
			
			#node Accumulate Field.002
			accumulate_field_002 = group_pick.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_002.name = "Accumulate Field.002"
			accumulate_field_002.data_type = 'INT'
			accumulate_field_002.domain = 'POINT'
			
			#node Switch.001
			switch_001 = group_pick.nodes.new("GeometryNodeSwitch")
			switch_001.name = "Switch.001"
			switch_001.input_type = 'INT'
			#False
			switch_001.inputs[1].default_value = -1
			
			#node Compare.003
			compare_003_1 = group_pick.nodes.new("FunctionNodeCompare")
			compare_003_1.name = "Compare.003"
			compare_003_1.data_type = 'INT'
			compare_003_1.mode = 'ELEMENT'
			compare_003_1.operation = 'EQUAL'
			#B_INT
			compare_003_1.inputs[3].default_value = 1
			
			#node Reroute.001
			reroute_001 = group_pick.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			#node Reroute.002
			reroute_002 = group_pick.nodes.new("NodeReroute")
			reroute_002.name = "Reroute.002"
			
			
			
			#Set locations
			group_output_14.location = (462.9173889160156, 0.0)
			group_input_14.location = (-472.9173889160156, 0.0)
			switch_1.location = (-120.0, -20.0)
			index_2.location = (-480.0, -120.0)
			accumulate_field.location = (60.0, -20.0)
			accumulate_field_002.location = (-120.0, 180.0)
			switch_001.location = (240.0, -20.0)
			compare_003_1.location = (60.0, 180.0)
			reroute_001.location = (-260.0, -100.0)
			reroute_002.location = (-260.0, -60.0)
			
			#Set dimensions
			group_output_14.width, group_output_14.height = 140.0, 100.0
			group_input_14.width, group_input_14.height = 140.0, 100.0
			switch_1.width, switch_1.height = 140.0, 100.0
			index_2.width, index_2.height = 140.0, 100.0
			accumulate_field.width, accumulate_field.height = 140.0, 100.0
			accumulate_field_002.width, accumulate_field_002.height = 140.0, 100.0
			switch_001.width, switch_001.height = 140.0, 100.0
			compare_003_1.width, compare_003_1.height = 138.9921875, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			reroute_002.width, reroute_002.height = 16.0, 100.0
			
			#initialize group_pick links
			#switch_1.Output -> accumulate_field.Value
			group_pick.links.new(switch_1.outputs[0], accumulate_field.inputs[0])
			#compare_003_1.Result -> switch_001.Switch
			group_pick.links.new(compare_003_1.outputs[0], switch_001.inputs[0])
			#accumulate_field.Total -> switch_001.True
			group_pick.links.new(accumulate_field.outputs[2], switch_001.inputs[2])
			#reroute_001.Output -> accumulate_field.Group ID
			group_pick.links.new(reroute_001.outputs[0], accumulate_field.inputs[1])
			#reroute_001.Output -> accumulate_field_002.Group ID
			group_pick.links.new(reroute_001.outputs[0], accumulate_field_002.inputs[1])
			#reroute_002.Output -> switch_1.Switch
			group_pick.links.new(reroute_002.outputs[0], switch_1.inputs[0])
			#reroute_002.Output -> accumulate_field_002.Value
			group_pick.links.new(reroute_002.outputs[0], accumulate_field_002.inputs[0])
			#index_2.Index -> switch_1.True
			group_pick.links.new(index_2.outputs[0], switch_1.inputs[2])
			#accumulate_field_002.Total -> compare_003_1.A
			group_pick.links.new(accumulate_field_002.outputs[2], compare_003_1.inputs[2])
			#group_input_14.Group ID -> reroute_001.Input
			group_pick.links.new(group_input_14.outputs[1], reroute_001.inputs[0])
			#group_input_14.Pick -> reroute_002.Input
			group_pick.links.new(group_input_14.outputs[0], reroute_002.inputs[0])
			#switch_001.Output -> group_output_14.Index
			group_pick.links.new(switch_001.outputs[0], group_output_14.inputs[1])
			#compare_003_1.Result -> group_output_14.Is Valid
			group_pick.links.new(compare_003_1.outputs[0], group_output_14.inputs[0])
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
			index_socket_1 = group_pick_vector.interface.new_socket(name = "Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			index_socket_1.default_value = 0
			index_socket_1.min_value = -2147483648
			index_socket_1.max_value = 2147483647
			index_socket_1.subtype = 'NONE'
			index_socket_1.attribute_domain = 'POINT'
			index_socket_1.description = "Picked Index for the Group"
			
			#Socket Vector
			vector_socket = group_pick_vector.interface.new_socket(name = "Vector", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			vector_socket.default_value = (0.0, 0.0, 0.0)
			vector_socket.min_value = -3.4028234663852886e+38
			vector_socket.max_value = 3.4028234663852886e+38
			vector_socket.subtype = 'NONE'
			vector_socket.attribute_domain = 'POINT'
			vector_socket.description = "Picked vector for the group"
			
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
			position_socket = group_pick_vector.interface.new_socket(name = "Position", in_out='INPUT', socket_type = 'NodeSocketVector')
			position_socket.default_value = (0.0, 0.0, 0.0)
			position_socket.min_value = -3.4028234663852886e+38
			position_socket.max_value = 3.4028234663852886e+38
			position_socket.subtype = 'NONE'
			position_socket.attribute_domain = 'POINT'
			position_socket.description = "Vector field to pick vlaue for, defaults to Position"
			
			
			#initialize group_pick_vector nodes
			#node Group Output
			group_output_15 = group_pick_vector.nodes.new("NodeGroupOutput")
			group_output_15.name = "Group Output"
			group_output_15.is_active_output = True
			
			#node Group Input
			group_input_15 = group_pick_vector.nodes.new("NodeGroupInput")
			group_input_15.name = "Group Input"
			
			#node Evaluate at Index.001
			evaluate_at_index_001_1 = group_pick_vector.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001_1.name = "Evaluate at Index.001"
			evaluate_at_index_001_1.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_001_1.domain = 'POINT'
			
			#node Switch.002
			switch_002 = group_pick_vector.nodes.new("GeometryNodeSwitch")
			switch_002.name = "Switch.002"
			switch_002.input_type = 'VECTOR'
			#False
			switch_002.inputs[1].default_value = (0.0, 0.0, 0.0)
			
			#node Group
			group_3 = group_pick_vector.nodes.new("GeometryNodeGroup")
			group_3.name = "Group"
			group_3.node_tree = group_pick
			
			
			
			
			#Set locations
			group_output_15.location = (-40.0, -20.0)
			group_input_15.location = (-740.0, -80.0)
			evaluate_at_index_001_1.location = (-380.0, -180.0)
			switch_002.location = (-220.0, -60.0)
			group_3.location = (-560.0, -20.0)
			
			#Set dimensions
			group_output_15.width, group_output_15.height = 140.0, 100.0
			group_input_15.width, group_input_15.height = 140.0, 100.0
			evaluate_at_index_001_1.width, evaluate_at_index_001_1.height = 132.09918212890625, 100.0
			switch_002.width, switch_002.height = 140.0, 100.0
			group_3.width, group_3.height = 140.0, 100.0
			
			#initialize group_pick_vector links
			#group_3.Is Valid -> switch_002.Switch
			group_pick_vector.links.new(group_3.outputs[0], switch_002.inputs[0])
			#group_3.Index -> evaluate_at_index_001_1.Index
			group_pick_vector.links.new(group_3.outputs[1], evaluate_at_index_001_1.inputs[0])
			#evaluate_at_index_001_1.Value -> switch_002.True
			group_pick_vector.links.new(evaluate_at_index_001_1.outputs[0], switch_002.inputs[2])
			#group_3.Index -> group_output_15.Index
			group_pick_vector.links.new(group_3.outputs[1], group_output_15.inputs[1])
			#group_3.Is Valid -> group_output_15.Is Valid
			group_pick_vector.links.new(group_3.outputs[0], group_output_15.inputs[0])
			#switch_002.Output -> group_output_15.Vector
			group_pick_vector.links.new(switch_002.outputs[0], group_output_15.inputs[2])
			#group_input_15.Group ID -> group_3.Group ID
			group_pick_vector.links.new(group_input_15.outputs[1], group_3.inputs[1])
			#group_input_15.Pick -> group_3.Pick
			group_pick_vector.links.new(group_input_15.outputs[0], group_3.inputs[0])
			#group_input_15.Position -> evaluate_at_index_001_1.Value
			group_pick_vector.links.new(group_input_15.outputs[2], evaluate_at_index_001_1.inputs[1])
			return group_pick_vector

		group_pick_vector = group_pick_vector_node_group()

		#initialize offset_integer node group
		def offset_integer_node_group():
			offset_integer = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Offset Integer")

			offset_integer.color_tag = 'CONVERTER'
			offset_integer.description = ""

			
			#offset_integer interface
			#Socket Value
			value_socket_2 = offset_integer.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			value_socket_2.default_value = 0
			value_socket_2.min_value = -2147483648
			value_socket_2.max_value = 2147483647
			value_socket_2.subtype = 'NONE'
			value_socket_2.attribute_domain = 'POINT'
			
			#Socket Index
			index_socket_2 = offset_integer.interface.new_socket(name = "Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			index_socket_2.default_value = 0
			index_socket_2.min_value = 0
			index_socket_2.max_value = 2147483647
			index_socket_2.subtype = 'NONE'
			index_socket_2.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_3 = offset_integer.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketInt')
			value_socket_3.default_value = 0
			value_socket_3.min_value = -2147483648
			value_socket_3.max_value = 2147483647
			value_socket_3.subtype = 'NONE'
			value_socket_3.attribute_domain = 'POINT'
			value_socket_3.hide_value = True
			
			#Socket Offset
			offset_socket_3 = offset_integer.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket_3.default_value = 0
			offset_socket_3.min_value = -2147483648
			offset_socket_3.max_value = 2147483647
			offset_socket_3.subtype = 'NONE'
			offset_socket_3.attribute_domain = 'POINT'
			
			
			#initialize offset_integer nodes
			#node Group Output
			group_output_16 = offset_integer.nodes.new("NodeGroupOutput")
			group_output_16.name = "Group Output"
			group_output_16.is_active_output = True
			
			#node Group Input
			group_input_16 = offset_integer.nodes.new("NodeGroupInput")
			group_input_16.name = "Group Input"
			
			#node Evaluate at Index
			evaluate_at_index_2 = offset_integer.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_2.name = "Evaluate at Index"
			evaluate_at_index_2.data_type = 'INT'
			evaluate_at_index_2.domain = 'POINT'
			
			#node Math
			math_1 = offset_integer.nodes.new("ShaderNodeMath")
			math_1.name = "Math"
			math_1.operation = 'ADD'
			math_1.use_clamp = False
			
			
			
			
			#Set locations
			group_output_16.location = (190.0, 0.0)
			group_input_16.location = (-412.72760009765625, 0.2001800537109375)
			evaluate_at_index_2.location = (0.0, 0.0)
			math_1.location = (-217.90158081054688, 69.93922424316406)
			
			#Set dimensions
			group_output_16.width, group_output_16.height = 140.0, 100.0
			group_input_16.width, group_input_16.height = 140.0, 100.0
			evaluate_at_index_2.width, evaluate_at_index_2.height = 140.0, 100.0
			math_1.width, math_1.height = 140.0, 100.0
			
			#initialize offset_integer links
			#evaluate_at_index_2.Value -> group_output_16.Value
			offset_integer.links.new(evaluate_at_index_2.outputs[0], group_output_16.inputs[0])
			#group_input_16.Index -> math_1.Value
			offset_integer.links.new(group_input_16.outputs[0], math_1.inputs[0])
			#group_input_16.Offset -> math_1.Value
			offset_integer.links.new(group_input_16.outputs[2], math_1.inputs[1])
			#math_1.Value -> evaluate_at_index_2.Index
			offset_integer.links.new(math_1.outputs[0], evaluate_at_index_2.inputs[0])
			#group_input_16.Value -> evaluate_at_index_2.Value
			offset_integer.links.new(group_input_16.outputs[1], evaluate_at_index_2.inputs[1])
			return offset_integer

		offset_integer = offset_integer_node_group()

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
			group_output_17 = res_group_id.nodes.new("NodeGroupOutput")
			group_output_17.name = "Group Output"
			group_output_17.is_active_output = True
			
			#node Group Input
			group_input_17 = res_group_id.nodes.new("NodeGroupInput")
			group_input_17.name = "Group Input"
			
			#node Named Attribute.001
			named_attribute_001_1 = res_group_id.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001_1.name = "Named Attribute.001"
			named_attribute_001_1.data_type = 'INT'
			#Name
			named_attribute_001_1.inputs[0].default_value = "res_id"
			
			#node Named Attribute.002
			named_attribute_002_1 = res_group_id.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002_1.name = "Named Attribute.002"
			named_attribute_002_1.data_type = 'INT'
			#Name
			named_attribute_002_1.inputs[0].default_value = "atom_name"
			
			#node Compare.002
			compare_002_1 = res_group_id.nodes.new("FunctionNodeCompare")
			compare_002_1.name = "Compare.002"
			compare_002_1.data_type = 'INT'
			compare_002_1.mode = 'ELEMENT'
			compare_002_1.operation = 'EQUAL'
			#B_INT
			compare_002_1.inputs[3].default_value = 1
			
			#node Compare.001
			compare_001_1 = res_group_id.nodes.new("FunctionNodeCompare")
			compare_001_1.name = "Compare.001"
			compare_001_1.data_type = 'INT'
			compare_001_1.mode = 'ELEMENT'
			compare_001_1.operation = 'NOT_EQUAL'
			
			#node Boolean Math
			boolean_math_6 = res_group_id.nodes.new("FunctionNodeBooleanMath")
			boolean_math_6.name = "Boolean Math"
			boolean_math_6.operation = 'OR'
			
			#node Accumulate Field.001
			accumulate_field_001 = res_group_id.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_001.name = "Accumulate Field.001"
			accumulate_field_001.data_type = 'INT'
			accumulate_field_001.domain = 'POINT'
			#Group Index
			accumulate_field_001.inputs[1].default_value = 0
			
			#node Group.001
			group_001_2 = res_group_id.nodes.new("GeometryNodeGroup")
			group_001_2.name = "Group.001"
			group_001_2.node_tree = offset_integer
			#Socket_1
			group_001_2.inputs[0].default_value = 0
			#Socket_2
			group_001_2.inputs[2].default_value = -1
			
			#node Math
			math_2 = res_group_id.nodes.new("ShaderNodeMath")
			math_2.name = "Math"
			math_2.operation = 'SUBTRACT'
			math_2.use_clamp = False
			#Value_001
			math_2.inputs[1].default_value = 1.0
			
			#node Frame
			frame = res_group_id.nodes.new("NodeFrame")
			frame.name = "Frame"
			frame.label_size = 20
			frame.shrink = True
			
			#node Reroute
			reroute_1 = res_group_id.nodes.new("NodeReroute")
			reroute_1.label = "subtracting 1 from the leading, but things don't work right"
			reroute_1.name = "Reroute"
			#node Reroute.001
			reroute_001_1 = res_group_id.nodes.new("NodeReroute")
			reroute_001_1.name = "Reroute.001"
			#node Reroute.002
			reroute_002_1 = res_group_id.nodes.new("NodeReroute")
			reroute_002_1.label = "In theory we can just use the trailing value instead of"
			reroute_002_1.name = "Reroute.002"
			#node Reroute.003
			reroute_003 = res_group_id.nodes.new("NodeReroute")
			reroute_003.name = "Reroute.003"
			
			
			#Set parents
			math_2.parent = frame
			reroute_1.parent = frame
			reroute_001_1.parent = frame
			reroute_002_1.parent = frame
			reroute_003.parent = frame
			
			#Set locations
			group_output_17.location = (900.0, 160.0)
			group_input_17.location = (-420.0, 160.0)
			named_attribute_001_1.location = (-240.0, 0.0)
			named_attribute_002_1.location = (-250.0, 160.0)
			compare_002_1.location = (-70.0, 160.0)
			compare_001_1.location = (-70.0, 0.0)
			boolean_math_6.location = (90.0, 160.0)
			accumulate_field_001.location = (250.0, 160.0)
			group_001_2.location = (-70.0, -160.0)
			math_2.location = (519.2361450195312, 166.28671264648438)
			frame.location = (95.0, -20.0)
			reroute_1.location = (554.4125366210938, 257.9646911621094)
			reroute_001_1.location = (739.2361450195312, 306.2867126464844)
			reroute_002_1.location = (551.13134765625, 297.3444519042969)
			reroute_003.location = (379.23614501953125, 306.2867126464844)
			
			#Set dimensions
			group_output_17.width, group_output_17.height = 140.0, 100.0
			group_input_17.width, group_input_17.height = 140.0, 100.0
			named_attribute_001_1.width, named_attribute_001_1.height = 140.0, 100.0
			named_attribute_002_1.width, named_attribute_002_1.height = 140.0, 100.0
			compare_002_1.width, compare_002_1.height = 140.0, 100.0
			compare_001_1.width, compare_001_1.height = 140.0, 100.0
			boolean_math_6.width, boolean_math_6.height = 140.0, 100.0
			accumulate_field_001.width, accumulate_field_001.height = 140.0, 100.0
			group_001_2.width, group_001_2.height = 140.0, 100.0
			math_2.width, math_2.height = 140.0, 100.0
			frame.width, frame.height = 436.0, 356.2867126464844
			reroute_1.width, reroute_1.height = 16.0, 100.0
			reroute_001_1.width, reroute_001_1.height = 16.0, 100.0
			reroute_002_1.width, reroute_002_1.height = 16.0, 100.0
			reroute_003.width, reroute_003.height = 16.0, 100.0
			
			#initialize res_group_id links
			#compare_002_1.Result -> boolean_math_6.Boolean
			res_group_id.links.new(compare_002_1.outputs[0], boolean_math_6.inputs[0])
			#named_attribute_001_1.Attribute -> compare_001_1.A
			res_group_id.links.new(named_attribute_001_1.outputs[0], compare_001_1.inputs[2])
			#named_attribute_001_1.Attribute -> group_001_2.Value
			res_group_id.links.new(named_attribute_001_1.outputs[0], group_001_2.inputs[1])
			#compare_001_1.Result -> boolean_math_6.Boolean
			res_group_id.links.new(compare_001_1.outputs[0], boolean_math_6.inputs[1])
			#named_attribute_002_1.Attribute -> compare_002_1.A
			res_group_id.links.new(named_attribute_002_1.outputs[0], compare_002_1.inputs[2])
			#group_001_2.Value -> compare_001_1.B
			res_group_id.links.new(group_001_2.outputs[0], compare_001_1.inputs[3])
			#accumulate_field_001.Leading -> math_2.Value
			res_group_id.links.new(accumulate_field_001.outputs[0], math_2.inputs[0])
			#math_2.Value -> group_output_17.Unique Group ID
			res_group_id.links.new(math_2.outputs[0], group_output_17.inputs[0])
			#boolean_math_6.Boolean -> accumulate_field_001.Value
			res_group_id.links.new(boolean_math_6.outputs[0], accumulate_field_001.inputs[0])
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
			index_socket_3 = residue_mask.interface.new_socket(name = "Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			index_socket_3.default_value = 0
			index_socket_3.min_value = -2147483648
			index_socket_3.max_value = 2147483647
			index_socket_3.subtype = 'NONE'
			index_socket_3.attribute_domain = 'POINT'
			index_socket_3.description = "Index for the group's atom with specified name, returns -1 if not valid"
			
			#Socket Position
			position_socket_1 = residue_mask.interface.new_socket(name = "Position", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			position_socket_1.default_value = (0.0, 0.0, 0.0)
			position_socket_1.min_value = -3.4028234663852886e+38
			position_socket_1.max_value = 3.4028234663852886e+38
			position_socket_1.subtype = 'NONE'
			position_socket_1.attribute_domain = 'POINT'
			position_socket_1.description = "Position of the picked point in the group, returns (0, 0, 0) if not valid"
			
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
			compare_1 = residue_mask.nodes.new("FunctionNodeCompare")
			compare_1.name = "Compare"
			compare_1.data_type = 'INT'
			compare_1.mode = 'ELEMENT'
			compare_1.operation = 'EQUAL'
			
			#node Group Input
			group_input_18 = residue_mask.nodes.new("NodeGroupInput")
			group_input_18.name = "Group Input"
			
			#node Named Attribute
			named_attribute_2 = residue_mask.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_2.name = "Named Attribute"
			named_attribute_2.data_type = 'INT'
			#Name
			named_attribute_2.inputs[0].default_value = "atom_name"
			
			#node Group Output
			group_output_18 = residue_mask.nodes.new("NodeGroupOutput")
			group_output_18.name = "Group Output"
			group_output_18.is_active_output = True
			
			#node Group
			group_4 = residue_mask.nodes.new("GeometryNodeGroup")
			group_4.name = "Group"
			group_4.node_tree = group_pick_vector
			#Socket_5
			group_4.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Group.002
			group_002_2 = residue_mask.nodes.new("GeometryNodeGroup")
			group_002_2.name = "Group.002"
			group_002_2.node_tree = res_group_id
			
			#node Switch
			switch_2 = residue_mask.nodes.new("GeometryNodeSwitch")
			switch_2.name = "Switch"
			switch_2.input_type = 'INT'
			
			
			
			
			#Set locations
			compare_1.location = (40.0, 340.0)
			group_input_18.location = (-140.0, 200.0)
			named_attribute_2.location = (-140.0, 340.0)
			group_output_18.location = (420.0, 340.0)
			group_4.location = (220.0, 340.0)
			group_002_2.location = (-140.0, 60.0)
			switch_2.location = (40.0, 180.0)
			
			#Set dimensions
			compare_1.width, compare_1.height = 140.0, 100.0
			group_input_18.width, group_input_18.height = 140.0, 100.0
			named_attribute_2.width, named_attribute_2.height = 140.0, 100.0
			group_output_18.width, group_output_18.height = 140.0, 100.0
			group_4.width, group_4.height = 164.60528564453125, 100.0
			group_002_2.width, group_002_2.height = 140.0, 100.0
			switch_2.width, switch_2.height = 140.0, 100.0
			
			#initialize residue_mask links
			#named_attribute_2.Attribute -> compare_1.A
			residue_mask.links.new(named_attribute_2.outputs[0], compare_1.inputs[2])
			#group_input_18.atom_name -> compare_1.B
			residue_mask.links.new(group_input_18.outputs[0], compare_1.inputs[3])
			#group_4.Index -> group_output_18.Index
			residue_mask.links.new(group_4.outputs[1], group_output_18.inputs[1])
			#group_4.Vector -> group_output_18.Position
			residue_mask.links.new(group_4.outputs[2], group_output_18.inputs[2])
			#group_4.Is Valid -> group_output_18.Is Valid
			residue_mask.links.new(group_4.outputs[0], group_output_18.inputs[0])
			#compare_1.Result -> group_4.Pick
			residue_mask.links.new(compare_1.outputs[0], group_4.inputs[0])
			#group_input_18.Use Fallback -> switch_2.Switch
			residue_mask.links.new(group_input_18.outputs[1], switch_2.inputs[0])
			#group_input_18.Group ID -> switch_2.False
			residue_mask.links.new(group_input_18.outputs[2], switch_2.inputs[1])
			#switch_2.Output -> group_4.Group ID
			residue_mask.links.new(switch_2.outputs[0], group_4.inputs[1])
			#group_002_2.Unique Group ID -> switch_2.True
			residue_mask.links.new(group_002_2.outputs[0], switch_2.inputs[2])
			#switch_2.Output -> group_output_18.Group ID
			residue_mask.links.new(switch_2.outputs[0], group_output_18.inputs[3])
			return residue_mask

		residue_mask = residue_mask_node_group()

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
			group_output_19 = _mn_topo_assign_backbone.nodes.new("NodeGroupOutput")
			group_output_19.name = "Group Output"
			group_output_19.is_active_output = True
			
			#node Group Input
			group_input_19 = _mn_topo_assign_backbone.nodes.new("NodeGroupInput")
			group_input_19.name = "Group Input"
			
			#node Store Named Attribute.002
			store_named_attribute_002 = _mn_topo_assign_backbone.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_002.name = "Store Named Attribute.002"
			store_named_attribute_002.data_type = 'FLOAT_VECTOR'
			store_named_attribute_002.domain = 'POINT'
			#Name
			store_named_attribute_002.inputs[2].default_value = "backbone_N"
			
			#node Store Named Attribute.003
			store_named_attribute_003 = _mn_topo_assign_backbone.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_003.name = "Store Named Attribute.003"
			store_named_attribute_003.data_type = 'FLOAT_VECTOR'
			store_named_attribute_003.domain = 'POINT'
			#Name
			store_named_attribute_003.inputs[2].default_value = "backbone_C"
			
			#node Store Named Attribute.004
			store_named_attribute_004 = _mn_topo_assign_backbone.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_004.name = "Store Named Attribute.004"
			store_named_attribute_004.data_type = 'FLOAT_VECTOR'
			store_named_attribute_004.domain = 'POINT'
			#Name
			store_named_attribute_004.inputs[2].default_value = "backbone_CA"
			
			#node Store Named Attribute.005
			store_named_attribute_005 = _mn_topo_assign_backbone.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_005.name = "Store Named Attribute.005"
			store_named_attribute_005.data_type = 'FLOAT_VECTOR'
			store_named_attribute_005.domain = 'POINT'
			#Name
			store_named_attribute_005.inputs[2].default_value = "backbone_O"
			
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
			capture_attribute = _mn_topo_assign_backbone.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute.name = "Capture Attribute"
			capture_attribute.active_index = 0
			capture_attribute.capture_items.clear()
			capture_attribute.capture_items.new('FLOAT', "Unique Group ID")
			capture_attribute.capture_items["Unique Group ID"].data_type = 'INT'
			capture_attribute.domain = 'POINT'
			
			#node Group
			group_5 = _mn_topo_assign_backbone.nodes.new("GeometryNodeGroup")
			group_5.name = "Group"
			group_5.node_tree = res_group_id
			
			#node Reroute
			reroute_2 = _mn_topo_assign_backbone.nodes.new("NodeReroute")
			reroute_2.name = "Reroute"
			#node Reroute.001
			reroute_001_2 = _mn_topo_assign_backbone.nodes.new("NodeReroute")
			reroute_001_2.name = "Reroute.001"
			#node Reroute.002
			reroute_002_2 = _mn_topo_assign_backbone.nodes.new("NodeReroute")
			reroute_002_2.name = "Reroute.002"
			#node Reroute.003
			reroute_003_1 = _mn_topo_assign_backbone.nodes.new("NodeReroute")
			reroute_003_1.name = "Reroute.003"
			#node Separate Geometry
			separate_geometry = _mn_topo_assign_backbone.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry.name = "Separate Geometry"
			separate_geometry.domain = 'POINT'
			
			#node Group.001
			group_001_3 = _mn_topo_assign_backbone.nodes.new("GeometryNodeGroup")
			group_001_3.name = "Group.001"
			group_001_3.node_tree = is_alpha_carbon
			#Socket_1
			group_001_3.inputs[0].default_value = True
			#Socket_3
			group_001_3.inputs[1].default_value = False
			
			
			
			
			#Set locations
			group_output_19.location = (720.0, 100.0)
			group_input_19.location = (-1200.0, 100.0)
			store_named_attribute_002.location = (-400.0, 100.0)
			store_named_attribute_003.location = (60.0, 100.0)
			store_named_attribute_004.location = (-180.0, 100.0)
			store_named_attribute_005.location = (300.0, 100.0)
			mn_topo_point_mask_005.location = (60.0, -120.0)
			mn_topo_point_mask_006.location = (-180.0, -120.0)
			mn_topo_point_mask_007.location = (300.0, -120.0)
			mn_topo_point_mask_004.location = (-400.0, -120.0)
			capture_attribute.location = (-1020.0, 100.0)
			group_5.location = (-1200.0, 0.0)
			reroute_2.location = (-440.0, -340.0)
			reroute_001_2.location = (-200.0, -340.0)
			reroute_002_2.location = (40.0, -340.0)
			reroute_003_1.location = (280.0, -340.0)
			separate_geometry.location = (540.0, 20.0)
			group_001_3.location = (540.0, -160.0)
			
			#Set dimensions
			group_output_19.width, group_output_19.height = 140.0, 100.0
			group_input_19.width, group_input_19.height = 140.0, 100.0
			store_named_attribute_002.width, store_named_attribute_002.height = 172.44415283203125, 100.0
			store_named_attribute_003.width, store_named_attribute_003.height = 169.44052124023438, 100.0
			store_named_attribute_004.width, store_named_attribute_004.height = 184.14559936523438, 100.0
			store_named_attribute_005.width, store_named_attribute_005.height = 169.42654418945312, 100.0
			mn_topo_point_mask_005.width, mn_topo_point_mask_005.height = 172.76019287109375, 100.0
			mn_topo_point_mask_006.width, mn_topo_point_mask_006.height = 185.9674072265625, 100.0
			mn_topo_point_mask_007.width, mn_topo_point_mask_007.height = 168.1260986328125, 100.0
			mn_topo_point_mask_004.width, mn_topo_point_mask_004.height = 178.538330078125, 100.0
			capture_attribute.width, capture_attribute.height = 140.0, 100.0
			group_5.width, group_5.height = 140.0, 100.0
			reroute_2.width, reroute_2.height = 16.0, 100.0
			reroute_001_2.width, reroute_001_2.height = 16.0, 100.0
			reroute_002_2.width, reroute_002_2.height = 16.0, 100.0
			reroute_003_1.width, reroute_003_1.height = 16.0, 100.0
			separate_geometry.width, separate_geometry.height = 140.0, 100.0
			group_001_3.width, group_001_3.height = 140.0, 100.0
			
			#initialize _mn_topo_assign_backbone links
			#mn_topo_point_mask_007.Is Valid -> store_named_attribute_005.Selection
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_007.outputs[0], store_named_attribute_005.inputs[1])
			#mn_topo_point_mask_006.Position -> store_named_attribute_004.Value
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_006.outputs[2], store_named_attribute_004.inputs[3])
			#mn_topo_point_mask_005.Position -> store_named_attribute_003.Value
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_005.outputs[2], store_named_attribute_003.inputs[3])
			#store_named_attribute_004.Geometry -> store_named_attribute_003.Geometry
			_mn_topo_assign_backbone.links.new(store_named_attribute_004.outputs[0], store_named_attribute_003.inputs[0])
			#store_named_attribute_003.Geometry -> store_named_attribute_005.Geometry
			_mn_topo_assign_backbone.links.new(store_named_attribute_003.outputs[0], store_named_attribute_005.inputs[0])
			#store_named_attribute_002.Geometry -> store_named_attribute_004.Geometry
			_mn_topo_assign_backbone.links.new(store_named_attribute_002.outputs[0], store_named_attribute_004.inputs[0])
			#mn_topo_point_mask_007.Position -> store_named_attribute_005.Value
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_007.outputs[2], store_named_attribute_005.inputs[3])
			#mn_topo_point_mask_006.Is Valid -> store_named_attribute_004.Selection
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_006.outputs[0], store_named_attribute_004.inputs[1])
			#mn_topo_point_mask_005.Is Valid -> store_named_attribute_003.Selection
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_005.outputs[0], store_named_attribute_003.inputs[1])
			#capture_attribute.Geometry -> store_named_attribute_002.Geometry
			_mn_topo_assign_backbone.links.new(capture_attribute.outputs[0], store_named_attribute_002.inputs[0])
			#store_named_attribute_005.Geometry -> group_output_19.Atoms
			_mn_topo_assign_backbone.links.new(store_named_attribute_005.outputs[0], group_output_19.inputs[0])
			#group_input_19.Atoms -> capture_attribute.Geometry
			_mn_topo_assign_backbone.links.new(group_input_19.outputs[0], capture_attribute.inputs[0])
			#group_5.Unique Group ID -> capture_attribute.Unique Group ID
			_mn_topo_assign_backbone.links.new(group_5.outputs[0], capture_attribute.inputs[1])
			#reroute_001_2.Output -> mn_topo_point_mask_006.Group ID
			_mn_topo_assign_backbone.links.new(reroute_001_2.outputs[0], mn_topo_point_mask_006.inputs[2])
			#capture_attribute.Unique Group ID -> reroute_2.Input
			_mn_topo_assign_backbone.links.new(capture_attribute.outputs[1], reroute_2.inputs[0])
			#reroute_2.Output -> reroute_001_2.Input
			_mn_topo_assign_backbone.links.new(reroute_2.outputs[0], reroute_001_2.inputs[0])
			#reroute_002_2.Output -> mn_topo_point_mask_005.Group ID
			_mn_topo_assign_backbone.links.new(reroute_002_2.outputs[0], mn_topo_point_mask_005.inputs[2])
			#reroute_001_2.Output -> reroute_002_2.Input
			_mn_topo_assign_backbone.links.new(reroute_001_2.outputs[0], reroute_002_2.inputs[0])
			#reroute_003_1.Output -> mn_topo_point_mask_007.Group ID
			_mn_topo_assign_backbone.links.new(reroute_003_1.outputs[0], mn_topo_point_mask_007.inputs[2])
			#reroute_002_2.Output -> reroute_003_1.Input
			_mn_topo_assign_backbone.links.new(reroute_002_2.outputs[0], reroute_003_1.inputs[0])
			#capture_attribute.Unique Group ID -> group_output_19.Unique Group ID
			_mn_topo_assign_backbone.links.new(capture_attribute.outputs[1], group_output_19.inputs[1])
			#mn_topo_point_mask_004.Is Valid -> store_named_attribute_002.Selection
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_004.outputs[0], store_named_attribute_002.inputs[1])
			#mn_topo_point_mask_004.Position -> store_named_attribute_002.Value
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_004.outputs[2], store_named_attribute_002.inputs[3])
			#store_named_attribute_005.Geometry -> separate_geometry.Geometry
			_mn_topo_assign_backbone.links.new(store_named_attribute_005.outputs[0], separate_geometry.inputs[0])
			#separate_geometry.Selection -> group_output_19.CA Atoms
			_mn_topo_assign_backbone.links.new(separate_geometry.outputs[0], group_output_19.inputs[2])
			#group_001_3.Selection -> separate_geometry.Selection
			_mn_topo_assign_backbone.links.new(group_001_3.outputs[0], separate_geometry.inputs[1])
			#reroute_2.Output -> mn_topo_point_mask_004.Group ID
			_mn_topo_assign_backbone.links.new(reroute_2.outputs[0], mn_topo_point_mask_004.inputs[2])
			return _mn_topo_assign_backbone

		_mn_topo_assign_backbone = _mn_topo_assign_backbone_node_group()

		#initialize _is_odd node group
		def _is_odd_node_group():
			_is_odd = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".is_odd")

			_is_odd.color_tag = 'NONE'
			_is_odd.description = ""

			
			#_is_odd interface
			#Socket is_even
			is_even_socket = _is_odd.interface.new_socket(name = "is_even", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_even_socket.default_value = False
			is_even_socket.attribute_domain = 'POINT'
			
			#Socket is_odd
			is_odd_socket = _is_odd.interface.new_socket(name = "is_odd", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_odd_socket.default_value = False
			is_odd_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_4 = _is_odd.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketInt')
			value_socket_4.default_value = 0
			value_socket_4.min_value = -2147483648
			value_socket_4.max_value = 2147483647
			value_socket_4.subtype = 'NONE'
			value_socket_4.attribute_domain = 'POINT'
			
			
			#initialize _is_odd nodes
			#node Group Input
			group_input_20 = _is_odd.nodes.new("NodeGroupInput")
			group_input_20.name = "Group Input"
			
			#node Group Output
			group_output_20 = _is_odd.nodes.new("NodeGroupOutput")
			group_output_20.name = "Group Output"
			group_output_20.is_active_output = True
			
			#node Boolean Math
			boolean_math_7 = _is_odd.nodes.new("FunctionNodeBooleanMath")
			boolean_math_7.name = "Boolean Math"
			boolean_math_7.operation = 'NOT'
			
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
			group_input_20.location = (-300.0, 80.0)
			group_output_20.location = (240.0, 120.0)
			boolean_math_7.location = (240.0, 20.0)
			compare_011.location = (60.0, 120.0)
			math_008.location = (-100.0, 120.0)
			
			#Set dimensions
			group_input_20.width, group_input_20.height = 140.0, 100.0
			group_output_20.width, group_output_20.height = 140.0, 100.0
			boolean_math_7.width, boolean_math_7.height = 140.0, 100.0
			compare_011.width, compare_011.height = 140.0, 100.0
			math_008.width, math_008.height = 140.0, 100.0
			
			#initialize _is_odd links
			#group_input_20.Value -> math_008.Value
			_is_odd.links.new(group_input_20.outputs[0], math_008.inputs[0])
			#compare_011.Result -> group_output_20.is_even
			_is_odd.links.new(compare_011.outputs[0], group_output_20.inputs[0])
			#compare_011.Result -> boolean_math_7.Boolean
			_is_odd.links.new(compare_011.outputs[0], boolean_math_7.inputs[0])
			#boolean_math_7.Boolean -> group_output_20.is_odd
			_is_odd.links.new(boolean_math_7.outputs[0], group_output_20.inputs[1])
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
			z_vector_for_euler_socket.default_value = (0.0, 0.0, 0.0)
			z_vector_for_euler_socket.min_value = -3.4028234663852886e+38
			z_vector_for_euler_socket.max_value = 3.4028234663852886e+38
			z_vector_for_euler_socket.subtype = 'NONE'
			z_vector_for_euler_socket.attribute_domain = 'POINT'
			
			#Socket X Vector for Euler
			x_vector_for_euler_socket = _mn_cartoon_bs_alternate_axis.interface.new_socket(name = "X Vector for Euler", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			x_vector_for_euler_socket.default_value = (0.0, 0.0, 0.0)
			x_vector_for_euler_socket.min_value = -3.4028234663852886e+38
			x_vector_for_euler_socket.max_value = 3.4028234663852886e+38
			x_vector_for_euler_socket.subtype = 'NONE'
			x_vector_for_euler_socket.attribute_domain = 'POINT'
			
			#Socket N
			n_socket = _mn_cartoon_bs_alternate_axis.interface.new_socket(name = "N", in_out='INPUT', socket_type = 'NodeSocketVector')
			n_socket.default_value = (0.0, 0.0, 0.0)
			n_socket.min_value = -3.4028234663852886e+38
			n_socket.max_value = 3.4028234663852886e+38
			n_socket.subtype = 'NONE'
			n_socket.attribute_domain = 'POINT'
			
			#Socket C
			c_socket = _mn_cartoon_bs_alternate_axis.interface.new_socket(name = "C", in_out='INPUT', socket_type = 'NodeSocketVector')
			c_socket.default_value = (0.0, 0.0, 0.0)
			c_socket.min_value = -3.4028234663852886e+38
			c_socket.max_value = 3.4028234663852886e+38
			c_socket.subtype = 'NONE'
			c_socket.attribute_domain = 'POINT'
			
			#Socket O
			o_socket = _mn_cartoon_bs_alternate_axis.interface.new_socket(name = "O", in_out='INPUT', socket_type = 'NodeSocketVector')
			o_socket.default_value = (0.0, 0.0, 0.0)
			o_socket.min_value = -3.4028234663852886e+38
			o_socket.max_value = 3.4028234663852886e+38
			o_socket.subtype = 'NONE'
			o_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_cartoon_bs_alternate_axis nodes
			#node Frame
			frame_1 = _mn_cartoon_bs_alternate_axis.nodes.new("NodeFrame")
			frame_1.label = "Only the last AA in an AH is selected"
			frame_1.name = "Frame"
			frame_1.label_size = 20
			frame_1.shrink = True
			
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
			switch_002_1 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeSwitch")
			switch_002_1.name = "Switch.002"
			switch_002_1.input_type = 'VECTOR'
			
			#node Group Output
			group_output_21 = _mn_cartoon_bs_alternate_axis.nodes.new("NodeGroupOutput")
			group_output_21.name = "Group Output"
			group_output_21.is_active_output = True
			
			#node Index.001
			index_001 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeInputIndex")
			index_001.name = "Index.001"
			
			#node Boolean Math.010
			boolean_math_010 = _mn_cartoon_bs_alternate_axis.nodes.new("FunctionNodeBooleanMath")
			boolean_math_010.name = "Boolean Math.010"
			boolean_math_010.operation = 'AND'
			
			#node Reroute.001
			reroute_001_3 = _mn_cartoon_bs_alternate_axis.nodes.new("NodeReroute")
			reroute_001_3.name = "Reroute.001"
			#node Vector Math.004
			vector_math_004 = _mn_cartoon_bs_alternate_axis.nodes.new("ShaderNodeVectorMath")
			vector_math_004.label = "N -> C"
			vector_math_004.name = "Vector Math.004"
			vector_math_004.operation = 'SUBTRACT'
			
			#node Group Input
			group_input_21 = _mn_cartoon_bs_alternate_axis.nodes.new("NodeGroupInput")
			group_input_21.name = "Group Input"
			
			#node Vector Math
			vector_math = _mn_cartoon_bs_alternate_axis.nodes.new("ShaderNodeVectorMath")
			vector_math.label = "C --> O"
			vector_math.name = "Vector Math"
			vector_math.operation = 'SUBTRACT'
			
			#node Integer
			integer_1 = _mn_cartoon_bs_alternate_axis.nodes.new("FunctionNodeInputInt")
			integer_1.name = "Integer"
			integer_1.integer = -1
			
			#node Compare
			compare_2 = _mn_cartoon_bs_alternate_axis.nodes.new("FunctionNodeCompare")
			compare_2.name = "Compare"
			compare_2.data_type = 'INT'
			compare_2.mode = 'ELEMENT'
			compare_2.operation = 'GREATER_THAN'
			
			#node Group.014
			group_014 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeGroup")
			group_014.name = "Group.014"
			group_014.node_tree = _sec_struct_counter
			
			#node Boolean Math
			boolean_math_8 = _mn_cartoon_bs_alternate_axis.nodes.new("FunctionNodeBooleanMath")
			boolean_math_8.name = "Boolean Math"
			boolean_math_8.operation = 'AND'
			
			#node Switch
			switch_3 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeSwitch")
			switch_3.name = "Switch"
			switch_3.input_type = 'VECTOR'
			
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
			group_6 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeGroup")
			group_6.name = "Group"
			group_6.node_tree = _field_offset
			group_6.inputs[1].hide = True
			group_6.inputs[2].hide = True
			group_6.inputs[3].hide = True
			group_6.outputs[1].hide = True
			group_6.outputs[2].hide = True
			group_6.outputs[3].hide = True
			#Input_3
			group_6.inputs[1].default_value = False
			#Input_5
			group_6.inputs[2].default_value = 0
			#Input_7
			group_6.inputs[3].default_value = 0.0
			
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
			compare_2.parent = frame_1
			group_014.parent = frame_1
			boolean_math_8.parent = frame_1
			group_012.parent = frame_1
			
			#Set locations
			frame_1.location = (-86.11199951171875, 65.14605712890625)
			vector_math_005.location = (60.0, 440.0)
			blur_attribute_001.location = (220.0, 400.0)
			switch_002_1.location = (220.0, 580.0)
			group_output_21.location = (400.0, 580.0)
			index_001.location = (-381.36767578125, 1.1884498596191406)
			boolean_math_010.location = (-41.36767578125, 101.18844604492188)
			reroute_001_3.location = (-897.6007080078125, 360.3312683105469)
			vector_math_004.location = (-817.6007080078125, 540.3312377929688)
			group_input_21.location = (-1077.6007080078125, 420.3312683105469)
			vector_math.location = (-817.6007080078125, 400.3312683105469)
			integer_1.location = (-822.031982421875, 264.41668701171875)
			compare_2.location = (-526.031982421875, 831.0416870117188)
			group_014.location = (-854.4696655273438, 787.1783447265625)
			boolean_math_8.location = (-366.0320129394531, 831.0416870117188)
			switch_3.location = (-189.45494079589844, 480.51531982421875)
			group_012.location = (-666.031982421875, 651.0416870117188)
			switch_008.location = (120.0, 100.0)
			group_6.location = (-622.031982421875, 344.41668701171875)
			group_011.location = (-361.36767578125, 161.18844604492188)
			group_005.location = (-221.36767578125, 1.1884498596191406)
			
			#Set dimensions
			frame_1.width, frame_1.height = 688.7999877929688, 326.0
			vector_math_005.width, vector_math_005.height = 140.0, 100.0
			blur_attribute_001.width, blur_attribute_001.height = 140.0, 100.0
			switch_002_1.width, switch_002_1.height = 140.0, 100.0
			group_output_21.width, group_output_21.height = 140.0, 100.0
			index_001.width, index_001.height = 140.0, 100.0
			boolean_math_010.width, boolean_math_010.height = 140.0, 100.0
			reroute_001_3.width, reroute_001_3.height = 16.0, 100.0
			vector_math_004.width, vector_math_004.height = 140.0, 100.0
			group_input_21.width, group_input_21.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			integer_1.width, integer_1.height = 140.0, 100.0
			compare_2.width, compare_2.height = 140.0, 100.0
			group_014.width, group_014.height = 140.0, 100.0
			boolean_math_8.width, boolean_math_8.height = 140.0, 100.0
			switch_3.width, switch_3.height = 140.0, 100.0
			group_012.width, group_012.height = 277.2730712890625, 100.0
			switch_008.width, switch_008.height = 140.0, 100.0
			group_6.width, group_6.height = 196.1611328125, 100.0
			group_011.width, group_011.height = 277.2730712890625, 100.0
			group_005.width, group_005.height = 140.0, 100.0
			
			#initialize _mn_cartoon_bs_alternate_axis links
			#vector_math_005.Vector -> switch_002_1.False
			_mn_cartoon_bs_alternate_axis.links.new(vector_math_005.outputs[0], switch_002_1.inputs[1])
			#blur_attribute_001.Value -> switch_002_1.True
			_mn_cartoon_bs_alternate_axis.links.new(blur_attribute_001.outputs[0], switch_002_1.inputs[2])
			#group_011.Is Sheet -> switch_002_1.Switch
			_mn_cartoon_bs_alternate_axis.links.new(group_011.outputs[1], switch_002_1.inputs[0])
			#group_input_21.C -> reroute_001_3.Input
			_mn_cartoon_bs_alternate_axis.links.new(group_input_21.outputs[1], reroute_001_3.inputs[0])
			#boolean_math_010.Boolean -> switch_008.Switch
			_mn_cartoon_bs_alternate_axis.links.new(boolean_math_010.outputs[0], switch_008.inputs[0])
			#group_005.is_even -> boolean_math_010.Boolean
			_mn_cartoon_bs_alternate_axis.links.new(group_005.outputs[0], boolean_math_010.inputs[1])
			#index_001.Index -> group_005.Value
			_mn_cartoon_bs_alternate_axis.links.new(index_001.outputs[0], group_005.inputs[0])
			#reroute_001_3.Output -> vector_math.Vector
			_mn_cartoon_bs_alternate_axis.links.new(reroute_001_3.outputs[0], vector_math.inputs[0])
			#group_011.Is Sheet -> boolean_math_010.Boolean
			_mn_cartoon_bs_alternate_axis.links.new(group_011.outputs[1], boolean_math_010.inputs[0])
			#reroute_001_3.Output -> vector_math_004.Vector
			_mn_cartoon_bs_alternate_axis.links.new(reroute_001_3.outputs[0], vector_math_004.inputs[1])
			#vector_math_005.Vector -> blur_attribute_001.Value
			_mn_cartoon_bs_alternate_axis.links.new(vector_math_005.outputs[0], blur_attribute_001.inputs[0])
			#switch_008.Output -> vector_math_005.Scale
			_mn_cartoon_bs_alternate_axis.links.new(switch_008.outputs[0], vector_math_005.inputs[3])
			#group_input_21.O -> vector_math.Vector
			_mn_cartoon_bs_alternate_axis.links.new(group_input_21.outputs[2], vector_math.inputs[1])
			#switch_002_1.Output -> group_output_21.Z Vector for Euler
			_mn_cartoon_bs_alternate_axis.links.new(switch_002_1.outputs[0], group_output_21.inputs[0])
			#vector_math_004.Vector -> group_output_21.X Vector for Euler
			_mn_cartoon_bs_alternate_axis.links.new(vector_math_004.outputs[0], group_output_21.inputs[1])
			#group_input_21.N -> vector_math_004.Vector
			_mn_cartoon_bs_alternate_axis.links.new(group_input_21.outputs[0], vector_math_004.inputs[0])
			#switch_3.Output -> vector_math_005.Vector
			_mn_cartoon_bs_alternate_axis.links.new(switch_3.outputs[0], vector_math_005.inputs[0])
			#group_014.Leading -> compare_2.A
			_mn_cartoon_bs_alternate_axis.links.new(group_014.outputs[0], compare_2.inputs[2])
			#group_014.Trailing -> compare_2.B
			_mn_cartoon_bs_alternate_axis.links.new(group_014.outputs[1], compare_2.inputs[3])
			#compare_2.Result -> boolean_math_8.Boolean
			_mn_cartoon_bs_alternate_axis.links.new(compare_2.outputs[0], boolean_math_8.inputs[0])
			#group_012.Is Helix -> boolean_math_8.Boolean
			_mn_cartoon_bs_alternate_axis.links.new(group_012.outputs[0], boolean_math_8.inputs[1])
			#vector_math.Vector -> switch_3.False
			_mn_cartoon_bs_alternate_axis.links.new(vector_math.outputs[0], switch_3.inputs[1])
			#vector_math.Vector -> group_6.Field
			_mn_cartoon_bs_alternate_axis.links.new(vector_math.outputs[0], group_6.inputs[0])
			#group_6.Field -> switch_3.True
			_mn_cartoon_bs_alternate_axis.links.new(group_6.outputs[0], switch_3.inputs[2])
			#integer_1.Integer -> group_6.Offset
			_mn_cartoon_bs_alternate_axis.links.new(integer_1.outputs[0], group_6.inputs[4])
			#boolean_math_8.Boolean -> switch_3.Switch
			_mn_cartoon_bs_alternate_axis.links.new(boolean_math_8.outputs[0], switch_3.inputs[0])
			return _mn_cartoon_bs_alternate_axis

		_mn_cartoon_bs_alternate_axis = _mn_cartoon_bs_alternate_axis_node_group()

		#initialize _atoms_to_curves node group
		def _atoms_to_curves_node_group():
			_atoms_to_curves = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".atoms_to_curves")

			_atoms_to_curves.color_tag = 'NONE'
			_atoms_to_curves.description = ""

			_atoms_to_curves.is_modifier = True
			
			#_atoms_to_curves interface
			#Socket CA Mesh Line
			ca_mesh_line_socket = _atoms_to_curves.interface.new_socket(name = "CA Mesh Line", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			ca_mesh_line_socket.attribute_domain = 'POINT'
			
			#Socket CA Splines
			ca_splines_socket = _atoms_to_curves.interface.new_socket(name = "CA Splines", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			ca_splines_socket.attribute_domain = 'POINT'
			
			#Socket AH Splines
			ah_splines_socket = _atoms_to_curves.interface.new_socket(name = "AH Splines", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			ah_splines_socket.attribute_domain = 'POINT'
			
			#Socket AH Mesh Line
			ah_mesh_line_socket = _atoms_to_curves.interface.new_socket(name = "AH Mesh Line", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			ah_mesh_line_socket.attribute_domain = 'POINT'
			
			#Socket BS Splines
			bs_splines_socket = _atoms_to_curves.interface.new_socket(name = "BS Splines", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			bs_splines_socket.attribute_domain = 'POINT'
			
			#Socket BS Mesh Line
			bs_mesh_line_socket = _atoms_to_curves.interface.new_socket(name = "BS Mesh Line", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			bs_mesh_line_socket.attribute_domain = 'POINT'
			
			#Socket Loop Splines
			loop_splines_socket = _atoms_to_curves.interface.new_socket(name = "Loop Splines", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			loop_splines_socket.attribute_domain = 'POINT'
			
			#Socket Loop Mesh Line
			loop_mesh_line_socket = _atoms_to_curves.interface.new_socket(name = "Loop Mesh Line", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			loop_mesh_line_socket.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket_2 = _atoms_to_curves.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_2.attribute_domain = 'POINT'
			atoms_socket_2.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket_5 = _atoms_to_curves.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_5.default_value = True
			selection_socket_5.attribute_domain = 'POINT'
			selection_socket_5.hide_value = True
			selection_socket_5.description = "Selection of atoms to apply this node to"
			
			#Socket BS Smoothing
			bs_smoothing_socket = _atoms_to_curves.interface.new_socket(name = "BS Smoothing", in_out='INPUT', socket_type = 'NodeSocketFloat')
			bs_smoothing_socket.default_value = 1.0
			bs_smoothing_socket.min_value = 0.0
			bs_smoothing_socket.max_value = 1.0
			bs_smoothing_socket.subtype = 'FACTOR'
			bs_smoothing_socket.attribute_domain = 'POINT'
			
			
			#initialize _atoms_to_curves nodes
			#node Frame.006
			frame_006 = _atoms_to_curves.nodes.new("NodeFrame")
			frame_006.label = "Break mesh where chain_id mismatch or distance cutoff"
			frame_006.name = "Frame.006"
			frame_006.label_size = 20
			frame_006.shrink = True
			
			#node Frame.007
			frame_007 = _atoms_to_curves.nodes.new("NodeFrame")
			frame_007.label = "Get immediate + and -- AA CA positions"
			frame_007.name = "Frame.007"
			frame_007.label_size = 20
			frame_007.shrink = True
			
			#node Frame.008
			frame_008 = _atoms_to_curves.nodes.new("NodeFrame")
			frame_008.label = "Calculate guide vectors for orientations"
			frame_008.name = "Frame.008"
			frame_008.label_size = 20
			frame_008.shrink = True
			
			#node Frame
			frame_2 = _atoms_to_curves.nodes.new("NodeFrame")
			frame_2.label = "Catch where it changes straight from AH to BS, could be better"
			frame_2.name = "Frame"
			frame_2.label_size = 20
			frame_2.shrink = True
			
			#node Frame.001
			frame_001 = _atoms_to_curves.nodes.new("NodeFrame")
			frame_001.label = "Split by Secondary Structure"
			frame_001.name = "Frame.001"
			frame_001.label_size = 20
			frame_001.shrink = True
			
			#node Frame.002
			frame_002 = _atoms_to_curves.nodes.new("NodeFrame")
			frame_002.label = "Turn backboen points to curves"
			frame_002.name = "Frame.002"
			frame_002.label_size = 20
			frame_002.shrink = True
			
			#node Compare.001
			compare_001_2 = _atoms_to_curves.nodes.new("FunctionNodeCompare")
			compare_001_2.name = "Compare.001"
			compare_001_2.data_type = 'INT'
			compare_001_2.mode = 'ELEMENT'
			compare_001_2.operation = 'NOT_EQUAL'
			
			#node Named Attribute.011
			named_attribute_011 = _atoms_to_curves.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_011.name = "Named Attribute.011"
			named_attribute_011.data_type = 'INT'
			#Name
			named_attribute_011.inputs[0].default_value = "chain_id"
			
			#node Evaluate at Index
			evaluate_at_index_3 = _atoms_to_curves.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_3.name = "Evaluate at Index"
			evaluate_at_index_3.data_type = 'INT'
			evaluate_at_index_3.domain = 'POINT'
			
			#node Evaluate at Index.001
			evaluate_at_index_001_2 = _atoms_to_curves.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001_2.name = "Evaluate at Index.001"
			evaluate_at_index_001_2.data_type = 'INT'
			evaluate_at_index_001_2.domain = 'POINT'
			
			#node Reroute.021
			reroute_021 = _atoms_to_curves.nodes.new("NodeReroute")
			reroute_021.name = "Reroute.021"
			#node Edge Vertices
			edge_vertices = _atoms_to_curves.nodes.new("GeometryNodeInputMeshEdgeVertices")
			edge_vertices.name = "Edge Vertices"
			
			#node Vector Math
			vector_math_1 = _atoms_to_curves.nodes.new("ShaderNodeVectorMath")
			vector_math_1.name = "Vector Math"
			vector_math_1.operation = 'DISTANCE'
			
			#node Compare
			compare_3 = _atoms_to_curves.nodes.new("FunctionNodeCompare")
			compare_3.name = "Compare"
			compare_3.data_type = 'FLOAT'
			compare_3.mode = 'ELEMENT'
			compare_3.operation = 'GREATER_THAN'
			
			#node Math.001
			math_001_2 = _atoms_to_curves.nodes.new("ShaderNodeMath")
			math_001_2.name = "Math.001"
			math_001_2.operation = 'DIVIDE'
			math_001_2.use_clamp = False
			#Value
			math_001_2.inputs[0].default_value = 60.0
			#Value_001
			math_001_2.inputs[1].default_value = 1000.0
			
			#node Boolean Math.001
			boolean_math_001_5 = _atoms_to_curves.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_5.name = "Boolean Math.001"
			boolean_math_001_5.operation = 'OR'
			
			#node Delete Geometry
			delete_geometry = _atoms_to_curves.nodes.new("GeometryNodeDeleteGeometry")
			delete_geometry.name = "Delete Geometry"
			delete_geometry.domain = 'EDGE'
			delete_geometry.mode = 'ALL'
			
			#node Store Named Attribute.001
			store_named_attribute_001 = _atoms_to_curves.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_001.name = "Store Named Attribute.001"
			store_named_attribute_001.data_type = 'FLOAT_VECTOR'
			store_named_attribute_001.domain = 'POINT'
			#Selection
			store_named_attribute_001.inputs[1].default_value = True
			#Name
			store_named_attribute_001.inputs[2].default_value = "reverse"
			
			#node Store Named Attribute
			store_named_attribute = _atoms_to_curves.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute.name = "Store Named Attribute"
			store_named_attribute.data_type = 'FLOAT_VECTOR'
			store_named_attribute.domain = 'POINT'
			#Selection
			store_named_attribute.inputs[1].default_value = True
			#Name
			store_named_attribute.inputs[2].default_value = "forward"
			
			#node Position.002
			position_002 = _atoms_to_curves.nodes.new("GeometryNodeInputPosition")
			position_002.name = "Position.002"
			
			#node Store Named Attribute.015
			store_named_attribute_015 = _atoms_to_curves.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_015.name = "Store Named Attribute.015"
			store_named_attribute_015.data_type = 'FLOAT_VECTOR'
			store_named_attribute_015.domain = 'POINT'
			#Selection
			store_named_attribute_015.inputs[1].default_value = True
			#Name
			store_named_attribute_015.inputs[2].default_value = "guide_Z"
			
			#node Store Named Attribute.016
			store_named_attribute_016 = _atoms_to_curves.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_016.name = "Store Named Attribute.016"
			store_named_attribute_016.data_type = 'FLOAT_VECTOR'
			store_named_attribute_016.domain = 'POINT'
			#Selection
			store_named_attribute_016.inputs[1].default_value = True
			#Name
			store_named_attribute_016.inputs[2].default_value = "guide_X"
			
			#node Store Named Attribute.017
			store_named_attribute_017 = _atoms_to_curves.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_017.name = "Store Named Attribute.017"
			store_named_attribute_017.mute = True
			store_named_attribute_017.data_type = 'FLOAT_VECTOR'
			store_named_attribute_017.domain = 'POINT'
			#Selection
			store_named_attribute_017.inputs[1].default_value = True
			#Name
			store_named_attribute_017.inputs[2].default_value = "guide_Y"
			#Value
			store_named_attribute_017.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Named Attribute.012
			named_attribute_012 = _atoms_to_curves.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_012.name = "Named Attribute.012"
			named_attribute_012.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_012.inputs[0].default_value = "backbone_N"
			
			#node Named Attribute.013
			named_attribute_013 = _atoms_to_curves.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_013.name = "Named Attribute.013"
			named_attribute_013.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_013.inputs[0].default_value = "backbone_O"
			
			#node Named Attribute.014
			named_attribute_014 = _atoms_to_curves.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_014.name = "Named Attribute.014"
			named_attribute_014.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_014.inputs[0].default_value = "backbone_C"
			
			#node Group.022
			group_022 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_022.name = "Group.022"
			group_022.node_tree = _field_offset
			#Input_0
			group_022.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Input_5
			group_022.inputs[2].default_value = 0
			#Input_7
			group_022.inputs[3].default_value = 0.0
			#Input_1
			group_022.inputs[4].default_value = -1
			
			#node Group.035
			group_035 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_035.name = "Group.035"
			group_035.node_tree = _field_offset
			#Input_0
			group_035.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Input_5
			group_035.inputs[2].default_value = 0
			#Input_7
			group_035.inputs[3].default_value = 0.0
			#Input_1
			group_035.inputs[4].default_value = 1
			
			#node Boolean Math.005
			boolean_math_005 = _atoms_to_curves.nodes.new("FunctionNodeBooleanMath")
			boolean_math_005.name = "Boolean Math.005"
			boolean_math_005.operation = 'AND'
			
			#node Boolean Math.009
			boolean_math_009 = _atoms_to_curves.nodes.new("FunctionNodeBooleanMath")
			boolean_math_009.name = "Boolean Math.009"
			boolean_math_009.operation = 'OR'
			
			#node Boolean Math.007
			boolean_math_007 = _atoms_to_curves.nodes.new("FunctionNodeBooleanMath")
			boolean_math_007.name = "Boolean Math.007"
			boolean_math_007.operation = 'AND'
			
			#node Group.036
			group_036 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_036.name = "Group.036"
			group_036.node_tree = _field_offset
			#Input_0
			group_036.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Input_5
			group_036.inputs[2].default_value = 0
			#Input_7
			group_036.inputs[3].default_value = 0.0
			#Input_1
			group_036.inputs[4].default_value = -1
			
			#node Boolean Math.010
			boolean_math_010_1 = _atoms_to_curves.nodes.new("FunctionNodeBooleanMath")
			boolean_math_010_1.name = "Boolean Math.010"
			boolean_math_010_1.operation = 'AND'
			
			#node Boolean Math.006
			boolean_math_006 = _atoms_to_curves.nodes.new("FunctionNodeBooleanMath")
			boolean_math_006.name = "Boolean Math.006"
			boolean_math_006.operation = 'OR'
			
			#node Boolean Math.008
			boolean_math_008 = _atoms_to_curves.nodes.new("FunctionNodeBooleanMath")
			boolean_math_008.name = "Boolean Math.008"
			boolean_math_008.operation = 'AND'
			
			#node Boolean Math.011
			boolean_math_011 = _atoms_to_curves.nodes.new("FunctionNodeBooleanMath")
			boolean_math_011.name = "Boolean Math.011"
			boolean_math_011.operation = 'OR'
			
			#node Group.034
			group_034 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_034.name = "Group.034"
			group_034.node_tree = _field_offset
			#Input_0
			group_034.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Input_5
			group_034.inputs[2].default_value = 0
			#Input_7
			group_034.inputs[3].default_value = 0.0
			#Input_1
			group_034.inputs[4].default_value = 1
			
			#node Group.024
			group_024_1 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_024_1.name = "Group.024"
			group_024_1.node_tree = _mn_select_sec_struct
			#Socket_1
			group_024_1.inputs[0].default_value = True
			
			#node Boolean Math.004
			boolean_math_004_1 = _atoms_to_curves.nodes.new("FunctionNodeBooleanMath")
			boolean_math_004_1.name = "Boolean Math.004"
			boolean_math_004_1.operation = 'OR'
			
			#node Mesh to Curve.004
			mesh_to_curve_004 = _atoms_to_curves.nodes.new("GeometryNodeMeshToCurve")
			mesh_to_curve_004.name = "Mesh to Curve.004"
			#Selection
			mesh_to_curve_004.inputs[1].default_value = True
			
			#node Mesh to Curve.003
			mesh_to_curve_003 = _atoms_to_curves.nodes.new("GeometryNodeMeshToCurve")
			mesh_to_curve_003.name = "Mesh to Curve.003"
			#Selection
			mesh_to_curve_003.inputs[1].default_value = True
			
			#node Mesh to Curve.001
			mesh_to_curve_001 = _atoms_to_curves.nodes.new("GeometryNodeMeshToCurve")
			mesh_to_curve_001.name = "Mesh to Curve.001"
			#Selection
			mesh_to_curve_001.inputs[1].default_value = True
			
			#node Mesh to Curve
			mesh_to_curve = _atoms_to_curves.nodes.new("GeometryNodeMeshToCurve")
			mesh_to_curve.name = "Mesh to Curve"
			#Selection
			mesh_to_curve.inputs[1].default_value = True
			
			#node Reroute.023
			reroute_023 = _atoms_to_curves.nodes.new("NodeReroute")
			reroute_023.name = "Reroute.023"
			#node Reroute.002
			reroute_002_3 = _atoms_to_curves.nodes.new("NodeReroute")
			reroute_002_3.name = "Reroute.002"
			#node Separate Geometry.006
			separate_geometry_006 = _atoms_to_curves.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_006.name = "Separate Geometry.006"
			separate_geometry_006.domain = 'POINT'
			separate_geometry_006.outputs[1].hide = True
			
			#node Separate Geometry.007
			separate_geometry_007 = _atoms_to_curves.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_007.name = "Separate Geometry.007"
			separate_geometry_007.domain = 'POINT'
			separate_geometry_007.outputs[1].hide = True
			
			#node Separate Geometry.008
			separate_geometry_008 = _atoms_to_curves.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_008.name = "Separate Geometry.008"
			separate_geometry_008.domain = 'POINT'
			separate_geometry_008.outputs[1].hide = True
			
			#node Group Input.001
			group_input_001 = _atoms_to_curves.nodes.new("NodeGroupInput")
			group_input_001.name = "Group Input.001"
			
			#node Group Output
			group_output_22 = _atoms_to_curves.nodes.new("NodeGroupOutput")
			group_output_22.name = "Group Output"
			group_output_22.is_active_output = True
			
			#node Group.012
			group_012_1 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_012_1.name = "Group.012"
			group_012_1.node_tree = _field_offset_vec
			#Input_1
			group_012_1.inputs[1].default_value = -1
			
			#node Group.013
			group_013 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_013.name = "Group.013"
			group_013.node_tree = _field_offset_vec
			#Input_1
			group_013.inputs[1].default_value = 1
			
			#node Group
			group_7 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_7.name = "Group"
			group_7.node_tree = _bs_smooth
			#Input_3
			group_7.inputs[2].default_value = 3
			
			#node Group.023
			group_023 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_023.name = "Group.023"
			group_023.node_tree = _expand_selection
			#Input_2
			group_023.inputs[1].default_value = 1
			
			#node Group.037
			group_037 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_037.name = "Group.037"
			group_037.node_tree = _mn_select_sec_struct
			#Socket_1
			group_037.inputs[0].default_value = True
			
			#node Group Input
			group_input_22 = _atoms_to_curves.nodes.new("NodeGroupInput")
			group_input_22.name = "Group Input"
			
			#node Store Named Attribute.019
			store_named_attribute_019 = _atoms_to_curves.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_019.name = "Store Named Attribute.019"
			store_named_attribute_019.data_type = 'INT'
			store_named_attribute_019.domain = 'POINT'
			#Selection
			store_named_attribute_019.inputs[1].default_value = True
			#Name
			store_named_attribute_019.inputs[2].default_value = "idx"
			
			#node Index.002
			index_002 = _atoms_to_curves.nodes.new("GeometryNodeInputIndex")
			index_002.name = "Index.002"
			
			#node Separate Geometry.003
			separate_geometry_003 = _atoms_to_curves.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_003.name = "Separate Geometry.003"
			separate_geometry_003.domain = 'POINT'
			
			#node Separate Geometry.001
			separate_geometry_001 = _atoms_to_curves.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_001.name = "Separate Geometry.001"
			separate_geometry_001.domain = 'POINT'
			
			#node Mesh to Points
			mesh_to_points = _atoms_to_curves.nodes.new("GeometryNodeMeshToPoints")
			mesh_to_points.name = "Mesh to Points"
			mesh_to_points.mode = 'VERTICES'
			#Selection
			mesh_to_points.inputs[1].default_value = True
			#Position
			mesh_to_points.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Radius
			mesh_to_points.inputs[3].default_value = 0.05000000074505806
			
			#node Points to Curves
			points_to_curves = _atoms_to_curves.nodes.new("GeometryNodePointsToCurves")
			points_to_curves.name = "Points to Curves"
			#Weight
			points_to_curves.inputs[2].default_value = 0.0
			
			#node Curve to Mesh
			curve_to_mesh = _atoms_to_curves.nodes.new("GeometryNodeCurveToMesh")
			curve_to_mesh.name = "Curve to Mesh"
			#Fill Caps
			curve_to_mesh.inputs[2].default_value = False
			
			#node Named Attribute.018
			named_attribute_018 = _atoms_to_curves.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_018.name = "Named Attribute.018"
			named_attribute_018.data_type = 'INT'
			#Name
			named_attribute_018.inputs[0].default_value = "chain_id"
			
			#node Group.001
			group_001_4 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_001_4.name = "Group.001"
			group_001_4.node_tree = is_alpha_carbon
			#Socket_1
			group_001_4.inputs[0].default_value = True
			#Socket_3
			group_001_4.inputs[1].default_value = False
			
			#node Group.006
			group_006 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_006.name = "Group.006"
			group_006.node_tree = _mn_topo_assign_backbone
			
			#node Group.008
			group_008 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_008.name = "Group.008"
			group_008.node_tree = _mn_cartoon_bs_alternate_axis
			
			
			
			#Set parents
			compare_001_2.parent = frame_006
			named_attribute_011.parent = frame_006
			evaluate_at_index_3.parent = frame_006
			evaluate_at_index_001_2.parent = frame_006
			reroute_021.parent = frame_006
			edge_vertices.parent = frame_006
			vector_math_1.parent = frame_006
			compare_3.parent = frame_006
			math_001_2.parent = frame_006
			boolean_math_001_5.parent = frame_006
			delete_geometry.parent = frame_006
			store_named_attribute_001.parent = frame_007
			store_named_attribute.parent = frame_007
			position_002.parent = frame_007
			store_named_attribute_015.parent = frame_008
			store_named_attribute_016.parent = frame_008
			store_named_attribute_017.parent = frame_008
			named_attribute_012.parent = frame_008
			named_attribute_013.parent = frame_008
			named_attribute_014.parent = frame_008
			group_022.parent = frame_2
			group_035.parent = frame_2
			boolean_math_005.parent = frame_2
			boolean_math_009.parent = frame_2
			boolean_math_007.parent = frame_2
			group_036.parent = frame_2
			boolean_math_010_1.parent = frame_2
			boolean_math_006.parent = frame_2
			boolean_math_008.parent = frame_2
			boolean_math_011.parent = frame_2
			group_034.parent = frame_2
			group_024_1.parent = frame_2
			mesh_to_curve_004.parent = frame_001
			mesh_to_curve_003.parent = frame_001
			mesh_to_curve_001.parent = frame_001
			mesh_to_curve.parent = frame_001
			reroute_023.parent = frame_001
			reroute_002_3.parent = frame_001
			separate_geometry_006.parent = frame_001
			separate_geometry_007.parent = frame_001
			separate_geometry_008.parent = frame_001
			group_012_1.parent = frame_007
			group_013.parent = frame_007
			separate_geometry_003.parent = frame_002
			separate_geometry_001.parent = frame_002
			mesh_to_points.parent = frame_002
			points_to_curves.parent = frame_002
			curve_to_mesh.parent = frame_002
			named_attribute_018.parent = frame_002
			group_001_4.parent = frame_002
			group_006.parent = frame_002
			group_008.parent = frame_008
			
			#Set locations
			frame_006.location = (-26.0, 380.0)
			frame_007.location = (-168.0, 46.0)
			frame_008.location = (-166.0, 3.0)
			frame_2.location = (6042.0, 80.0)
			frame_001.location = (458.0, -8.0)
			frame_002.location = (0.0, 0.0)
			compare_001_2.location = (-1907.6533203125, 300.176513671875)
			named_attribute_011.location = (-2304.4140625, 25.7803955078125)
			evaluate_at_index_3.location = (-2067.6533203125, 300.176513671875)
			evaluate_at_index_001_2.location = (-2067.6533203125, 120.176513671875)
			reroute_021.location = (-2087.6533203125, 100.176513671875)
			edge_vertices.location = (-2304.4140625, 165.7803955078125)
			vector_math_1.location = (-2064.4140625, -54.2196044921875)
			compare_3.location = (-1904.4140625, -54.2196044921875)
			math_001_2.location = (-2064.4140625, -194.2196044921875)
			boolean_math_001_5.location = (-1740.0, 300.0)
			delete_geometry.location = (-1740.0, 480.0)
			store_named_attribute_001.location = (-1062.2197265625, 834.4013671875)
			store_named_attribute.location = (-1222.2197265625, 834.4013671875)
			position_002.location = (-1222.2197265625, 474.4012451171875)
			store_named_attribute_015.location = (-563.97314453125, 856.68115234375)
			store_named_attribute_016.location = (-383.97314453125, 856.68115234375)
			store_named_attribute_017.location = (-203.97314453125, 856.68115234375)
			named_attribute_012.location = (-743.97314453125, 616.68115234375)
			named_attribute_013.location = (-743.97314453125, 336.68115234375)
			named_attribute_014.location = (-743.97314453125, 476.68115234375)
			group_022.location = (-5080.0, -580.0)
			group_035.location = (-5080.0, -860.0)
			boolean_math_005.location = (-4840.0, -660.0)
			boolean_math_009.location = (-4620.0, -660.0)
			boolean_math_007.location = (-4800.0, -60.0)
			group_036.location = (-5040.0, -180.0)
			boolean_math_010_1.location = (-4800.0, -220.0)
			boolean_math_006.location = (-4360.0, -320.0)
			boolean_math_008.location = (-4840.0, -820.0)
			boolean_math_011.location = (-4580.0, -100.0)
			group_034.location = (-5040.0, 100.0)
			group_024_1.location = (-5532.35107421875, -374.12896728515625)
			boolean_math_004_1.location = (1120.0, 520.0)
			mesh_to_curve_004.location = (1200.0, 940.0)
			mesh_to_curve_003.location = (1200.0, 820.0)
			mesh_to_curve_001.location = (1200.0, 700.0)
			mesh_to_curve.location = (1200.0, 580.0)
			reroute_023.location = (1260.0, 980.0)
			reroute_002_3.location = (960.0, 860.0)
			separate_geometry_006.location = (1040.0, 820.0)
			separate_geometry_007.location = (1040.0, 700.0)
			separate_geometry_008.location = (1040.0, 580.0)
			group_input_001.location = (-180.0, 720.0)
			group_output_22.location = (2120.0, 920.0)
			group_012_1.location = (-1222.2197265625, 614.4013671875)
			group_013.location = (-1062.2197265625, 614.4013671875)
			group_7.location = (60.0, 840.0)
			group_023.location = (960.0, 520.0)
			group_037.location = (880.0, 760.0)
			group_input_22.location = (-4220.0, 700.0)
			store_named_attribute_019.location = (-2860.0, 820.0)
			index_002.location = (-2860.0, 620.0)
			separate_geometry_003.location = (-3780.0, 780.0)
			separate_geometry_001.location = (-3600.0, 780.0)
			mesh_to_points.location = (-3420.0, 780.0)
			points_to_curves.location = (-3260.0, 780.0)
			curve_to_mesh.location = (-3100.0, 780.0)
			named_attribute_018.location = (-3420.0, 600.0)
			group_001_4.location = (-3780.0, 620.0)
			group_006.location = (-4020.0, 780.0)
			group_008.location = (-543.97314453125, 596.68115234375)
			
			#Set dimensions
			frame_006.width, frame_006.height = 764.5, 893.0
			frame_007.width, frame_007.height = 360.0, 480.0
			frame_008.width, frame_008.height = 740.0, 712.0
			frame_2.width, frame_2.height = 1372.5, 1282.0
			frame_001.width, frame_001.height = 444.0, 573.0
			frame_002.width, frame_002.height = 1120.0, 372.0
			compare_001_2.width, compare_001_2.height = 140.0, 100.0
			named_attribute_011.width, named_attribute_011.height = 140.0, 100.0
			evaluate_at_index_3.width, evaluate_at_index_3.height = 140.0, 100.0
			evaluate_at_index_001_2.width, evaluate_at_index_001_2.height = 140.0, 100.0
			reroute_021.width, reroute_021.height = 16.0, 100.0
			edge_vertices.width, edge_vertices.height = 140.0, 100.0
			vector_math_1.width, vector_math_1.height = 140.0, 100.0
			compare_3.width, compare_3.height = 140.0, 100.0
			math_001_2.width, math_001_2.height = 140.0, 100.0
			boolean_math_001_5.width, boolean_math_001_5.height = 140.0, 100.0
			delete_geometry.width, delete_geometry.height = 140.0, 100.0
			store_named_attribute_001.width, store_named_attribute_001.height = 140.0, 100.0
			store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
			position_002.width, position_002.height = 140.0, 100.0
			store_named_attribute_015.width, store_named_attribute_015.height = 140.0, 100.0
			store_named_attribute_016.width, store_named_attribute_016.height = 140.0, 100.0
			store_named_attribute_017.width, store_named_attribute_017.height = 140.0, 100.0
			named_attribute_012.width, named_attribute_012.height = 140.0, 100.0
			named_attribute_013.width, named_attribute_013.height = 140.0, 100.0
			named_attribute_014.width, named_attribute_014.height = 140.0, 100.0
			group_022.width, group_022.height = 140.0, 100.0
			group_035.width, group_035.height = 140.0, 100.0
			boolean_math_005.width, boolean_math_005.height = 140.0, 100.0
			boolean_math_009.width, boolean_math_009.height = 140.0, 100.0
			boolean_math_007.width, boolean_math_007.height = 140.0, 100.0
			group_036.width, group_036.height = 140.0, 100.0
			boolean_math_010_1.width, boolean_math_010_1.height = 140.0, 100.0
			boolean_math_006.width, boolean_math_006.height = 140.0, 100.0
			boolean_math_008.width, boolean_math_008.height = 140.0, 100.0
			boolean_math_011.width, boolean_math_011.height = 140.0, 100.0
			group_034.width, group_034.height = 140.0, 100.0
			group_024_1.width, group_024_1.height = 158.9053955078125, 100.0
			boolean_math_004_1.width, boolean_math_004_1.height = 140.0, 100.0
			mesh_to_curve_004.width, mesh_to_curve_004.height = 140.0, 100.0
			mesh_to_curve_003.width, mesh_to_curve_003.height = 140.0, 100.0
			mesh_to_curve_001.width, mesh_to_curve_001.height = 140.0, 100.0
			mesh_to_curve.width, mesh_to_curve.height = 140.0, 100.0
			reroute_023.width, reroute_023.height = 16.0, 100.0
			reroute_002_3.width, reroute_002_3.height = 16.0, 100.0
			separate_geometry_006.width, separate_geometry_006.height = 140.0, 100.0
			separate_geometry_007.width, separate_geometry_007.height = 140.0, 100.0
			separate_geometry_008.width, separate_geometry_008.height = 140.0, 100.0
			group_input_001.width, group_input_001.height = 140.0, 100.0
			group_output_22.width, group_output_22.height = 140.0, 100.0
			group_012_1.width, group_012_1.height = 140.0, 100.0
			group_013.width, group_013.height = 140.0, 100.0
			group_7.width, group_7.height = 374.382080078125, 100.0
			group_023.width, group_023.height = 140.0, 100.0
			group_037.width, group_037.height = 233.448486328125, 100.0
			group_input_22.width, group_input_22.height = 140.0, 100.0
			store_named_attribute_019.width, store_named_attribute_019.height = 140.0, 100.0
			index_002.width, index_002.height = 140.0, 100.0
			separate_geometry_003.width, separate_geometry_003.height = 140.0, 100.0
			separate_geometry_001.width, separate_geometry_001.height = 140.0, 100.0
			mesh_to_points.width, mesh_to_points.height = 140.0, 100.0
			points_to_curves.width, points_to_curves.height = 140.0, 100.0
			curve_to_mesh.width, curve_to_mesh.height = 140.0, 100.0
			named_attribute_018.width, named_attribute_018.height = 140.0, 100.0
			group_001_4.width, group_001_4.height = 140.0, 100.0
			group_006.width, group_006.height = 206.7611083984375, 100.0
			group_008.width, group_008.height = 318.43975830078125, 100.0
			
			#initialize _atoms_to_curves links
			#group_023.Boolean -> boolean_math_004_1.Boolean
			_atoms_to_curves.links.new(group_023.outputs[0], boolean_math_004_1.inputs[0])
			#group_024_1.Is Helix -> boolean_math_010_1.Boolean
			_atoms_to_curves.links.new(group_024_1.outputs[0], boolean_math_010_1.inputs[1])
			#group_024_1.Is Sheet -> group_036.Value
			_atoms_to_curves.links.new(group_024_1.outputs[1], group_036.inputs[1])
			#group_024_1.Is Sheet -> boolean_math_005.Boolean
			_atoms_to_curves.links.new(group_024_1.outputs[1], boolean_math_005.inputs[0])
			#group_034.Value -> boolean_math_007.Boolean
			_atoms_to_curves.links.new(group_034.outputs[1], boolean_math_007.inputs[0])
			#group_024_1.Is Sheet -> group_034.Value
			_atoms_to_curves.links.new(group_024_1.outputs[1], group_034.inputs[1])
			#boolean_math_008.Boolean -> boolean_math_009.Boolean
			_atoms_to_curves.links.new(boolean_math_008.outputs[0], boolean_math_009.inputs[1])
			#position_002.Position -> group_013.Field
			_atoms_to_curves.links.new(position_002.outputs[0], group_013.inputs[0])
			#position_002.Position -> group_012_1.Field
			_atoms_to_curves.links.new(position_002.outputs[0], group_012_1.inputs[0])
			#group_012_1.Field -> store_named_attribute.Value
			_atoms_to_curves.links.new(group_012_1.outputs[0], store_named_attribute.inputs[3])
			#group_037.Is Helix -> separate_geometry_006.Selection
			_atoms_to_curves.links.new(group_037.outputs[0], separate_geometry_006.inputs[1])
			#group_024_1.Is Helix -> group_035.Value
			_atoms_to_curves.links.new(group_024_1.outputs[0], group_035.inputs[1])
			#boolean_math_006.Boolean -> boolean_math_004_1.Boolean
			_atoms_to_curves.links.new(boolean_math_006.outputs[0], boolean_math_004_1.inputs[1])
			#group_024_1.Is Sheet -> boolean_math_008.Boolean
			_atoms_to_curves.links.new(group_024_1.outputs[1], boolean_math_008.inputs[0])
			#separate_geometry_008.Selection -> mesh_to_curve.Mesh
			_atoms_to_curves.links.new(separate_geometry_008.outputs[0], mesh_to_curve.inputs[0])
			#boolean_math_007.Boolean -> boolean_math_011.Boolean
			_atoms_to_curves.links.new(boolean_math_007.outputs[0], boolean_math_011.inputs[0])
			#group_022.Value -> boolean_math_005.Boolean
			_atoms_to_curves.links.new(group_022.outputs[1], boolean_math_005.inputs[1])
			#store_named_attribute.Geometry -> store_named_attribute_001.Geometry
			_atoms_to_curves.links.new(store_named_attribute.outputs[0], store_named_attribute_001.inputs[0])
			#group_024_1.Is Helix -> group_022.Value
			_atoms_to_curves.links.new(group_024_1.outputs[0], group_022.inputs[1])
			#boolean_math_009.Boolean -> boolean_math_006.Boolean
			_atoms_to_curves.links.new(boolean_math_009.outputs[0], boolean_math_006.inputs[1])
			#reroute_002_3.Output -> separate_geometry_006.Geometry
			_atoms_to_curves.links.new(reroute_002_3.outputs[0], separate_geometry_006.inputs[0])
			#separate_geometry_006.Selection -> mesh_to_curve_003.Mesh
			_atoms_to_curves.links.new(separate_geometry_006.outputs[0], mesh_to_curve_003.inputs[0])
			#group_013.Field -> store_named_attribute_001.Value
			_atoms_to_curves.links.new(group_013.outputs[0], store_named_attribute_001.inputs[3])
			#group_035.Value -> boolean_math_008.Boolean
			_atoms_to_curves.links.new(group_035.outputs[1], boolean_math_008.inputs[1])
			#group_024_1.Is Helix -> boolean_math_007.Boolean
			_atoms_to_curves.links.new(group_024_1.outputs[0], boolean_math_007.inputs[1])
			#group_036.Value -> boolean_math_010_1.Boolean
			_atoms_to_curves.links.new(group_036.outputs[1], boolean_math_010_1.inputs[0])
			#separate_geometry_007.Selection -> mesh_to_curve_001.Mesh
			_atoms_to_curves.links.new(separate_geometry_007.outputs[0], mesh_to_curve_001.inputs[0])
			#boolean_math_010_1.Boolean -> boolean_math_011.Boolean
			_atoms_to_curves.links.new(boolean_math_010_1.outputs[0], boolean_math_011.inputs[1])
			#boolean_math_005.Boolean -> boolean_math_009.Boolean
			_atoms_to_curves.links.new(boolean_math_005.outputs[0], boolean_math_009.inputs[0])
			#boolean_math_011.Boolean -> boolean_math_006.Boolean
			_atoms_to_curves.links.new(boolean_math_011.outputs[0], boolean_math_006.inputs[0])
			#reroute_023.Output -> group_output_22.CA Mesh Line
			_atoms_to_curves.links.new(reroute_023.outputs[0], group_output_22.inputs[0])
			#mesh_to_curve_001.Curve -> group_output_22.BS Splines
			_atoms_to_curves.links.new(mesh_to_curve_001.outputs[0], group_output_22.inputs[4])
			#mesh_to_curve.Curve -> group_output_22.Loop Splines
			_atoms_to_curves.links.new(mesh_to_curve.outputs[0], group_output_22.inputs[6])
			#mesh_to_curve_003.Curve -> group_output_22.AH Splines
			_atoms_to_curves.links.new(mesh_to_curve_003.outputs[0], group_output_22.inputs[2])
			#reroute_002_3.Output -> mesh_to_curve_004.Mesh
			_atoms_to_curves.links.new(reroute_002_3.outputs[0], mesh_to_curve_004.inputs[0])
			#mesh_to_curve_004.Curve -> group_output_22.CA Splines
			_atoms_to_curves.links.new(mesh_to_curve_004.outputs[0], group_output_22.inputs[1])
			#edge_vertices.Vertex Index 2 -> evaluate_at_index_001_2.Index
			_atoms_to_curves.links.new(edge_vertices.outputs[1], evaluate_at_index_001_2.inputs[0])
			#edge_vertices.Vertex Index 1 -> evaluate_at_index_3.Index
			_atoms_to_curves.links.new(edge_vertices.outputs[0], evaluate_at_index_3.inputs[0])
			#reroute_021.Output -> evaluate_at_index_001_2.Value
			_atoms_to_curves.links.new(reroute_021.outputs[0], evaluate_at_index_001_2.inputs[1])
			#evaluate_at_index_001_2.Value -> compare_001_2.B
			_atoms_to_curves.links.new(evaluate_at_index_001_2.outputs[0], compare_001_2.inputs[3])
			#evaluate_at_index_3.Value -> compare_001_2.A
			_atoms_to_curves.links.new(evaluate_at_index_3.outputs[0], compare_001_2.inputs[2])
			#reroute_021.Output -> evaluate_at_index_3.Value
			_atoms_to_curves.links.new(reroute_021.outputs[0], evaluate_at_index_3.inputs[1])
			#named_attribute_011.Attribute -> reroute_021.Input
			_atoms_to_curves.links.new(named_attribute_011.outputs[0], reroute_021.inputs[0])
			#compare_001_2.Result -> boolean_math_001_5.Boolean
			_atoms_to_curves.links.new(compare_001_2.outputs[0], boolean_math_001_5.inputs[0])
			#boolean_math_001_5.Boolean -> delete_geometry.Selection
			_atoms_to_curves.links.new(boolean_math_001_5.outputs[0], delete_geometry.inputs[1])
			#edge_vertices.Position 1 -> vector_math_1.Vector
			_atoms_to_curves.links.new(edge_vertices.outputs[2], vector_math_1.inputs[0])
			#edge_vertices.Position 2 -> vector_math_1.Vector
			_atoms_to_curves.links.new(edge_vertices.outputs[3], vector_math_1.inputs[1])
			#vector_math_1.Value -> compare_3.A
			_atoms_to_curves.links.new(vector_math_1.outputs[1], compare_3.inputs[0])
			#compare_3.Result -> boolean_math_001_5.Boolean
			_atoms_to_curves.links.new(compare_3.outputs[0], boolean_math_001_5.inputs[1])
			#math_001_2.Value -> compare_3.B
			_atoms_to_curves.links.new(math_001_2.outputs[0], compare_3.inputs[1])
			#store_named_attribute_019.Geometry -> delete_geometry.Geometry
			_atoms_to_curves.links.new(store_named_attribute_019.outputs[0], delete_geometry.inputs[0])
			#named_attribute_012.Attribute -> group_008.N
			_atoms_to_curves.links.new(named_attribute_012.outputs[0], group_008.inputs[0])
			#named_attribute_014.Attribute -> group_008.C
			_atoms_to_curves.links.new(named_attribute_014.outputs[0], group_008.inputs[1])
			#named_attribute_013.Attribute -> group_008.O
			_atoms_to_curves.links.new(named_attribute_013.outputs[0], group_008.inputs[2])
			#store_named_attribute_015.Geometry -> store_named_attribute_016.Geometry
			_atoms_to_curves.links.new(store_named_attribute_015.outputs[0], store_named_attribute_016.inputs[0])
			#group_008.Z Vector for Euler -> store_named_attribute_015.Value
			_atoms_to_curves.links.new(group_008.outputs[0], store_named_attribute_015.inputs[3])
			#group_008.X Vector for Euler -> store_named_attribute_016.Value
			_atoms_to_curves.links.new(group_008.outputs[1], store_named_attribute_016.inputs[3])
			#store_named_attribute_016.Geometry -> store_named_attribute_017.Geometry
			_atoms_to_curves.links.new(store_named_attribute_016.outputs[0], store_named_attribute_017.inputs[0])
			#store_named_attribute_001.Geometry -> store_named_attribute_015.Geometry
			_atoms_to_curves.links.new(store_named_attribute_001.outputs[0], store_named_attribute_015.inputs[0])
			#group_7.Geometry -> reroute_002_3.Input
			_atoms_to_curves.links.new(group_7.outputs[0], reroute_002_3.inputs[0])
			#reroute_002_3.Output -> reroute_023.Input
			_atoms_to_curves.links.new(reroute_002_3.outputs[0], reroute_023.inputs[0])
			#reroute_002_3.Output -> separate_geometry_007.Geometry
			_atoms_to_curves.links.new(reroute_002_3.outputs[0], separate_geometry_007.inputs[0])
			#reroute_002_3.Output -> separate_geometry_008.Geometry
			_atoms_to_curves.links.new(reroute_002_3.outputs[0], separate_geometry_008.inputs[0])
			#boolean_math_004_1.Boolean -> separate_geometry_008.Selection
			_atoms_to_curves.links.new(boolean_math_004_1.outputs[0], separate_geometry_008.inputs[1])
			#group_037.Is Sheet -> separate_geometry_007.Selection
			_atoms_to_curves.links.new(group_037.outputs[1], separate_geometry_007.inputs[1])
			#group_037.Is Loop -> group_023.Input
			_atoms_to_curves.links.new(group_037.outputs[3], group_023.inputs[0])
			#separate_geometry_006.Selection -> group_output_22.AH Mesh Line
			_atoms_to_curves.links.new(separate_geometry_006.outputs[0], group_output_22.inputs[3])
			#separate_geometry_007.Selection -> group_output_22.BS Mesh Line
			_atoms_to_curves.links.new(separate_geometry_007.outputs[0], group_output_22.inputs[5])
			#separate_geometry_008.Selection -> group_output_22.Loop Mesh Line
			_atoms_to_curves.links.new(separate_geometry_008.outputs[0], group_output_22.inputs[7])
			#store_named_attribute_017.Geometry -> group_7.Geometry
			_atoms_to_curves.links.new(store_named_attribute_017.outputs[0], group_7.inputs[0])
			#group_input_001.BS Smoothing -> group_7.Factor
			_atoms_to_curves.links.new(group_input_001.outputs[2], group_7.inputs[1])
			#index_002.Index -> store_named_attribute_019.Value
			_atoms_to_curves.links.new(index_002.outputs[0], store_named_attribute_019.inputs[3])
			#group_input_22.Atoms -> group_006.Atoms
			_atoms_to_curves.links.new(group_input_22.outputs[0], group_006.inputs[0])
			#separate_geometry_003.Selection -> separate_geometry_001.Geometry
			_atoms_to_curves.links.new(separate_geometry_003.outputs[0], separate_geometry_001.inputs[0])
			#separate_geometry_001.Selection -> mesh_to_points.Mesh
			_atoms_to_curves.links.new(separate_geometry_001.outputs[0], mesh_to_points.inputs[0])
			#mesh_to_points.Points -> points_to_curves.Points
			_atoms_to_curves.links.new(mesh_to_points.outputs[0], points_to_curves.inputs[0])
			#named_attribute_018.Attribute -> points_to_curves.Curve Group ID
			_atoms_to_curves.links.new(named_attribute_018.outputs[0], points_to_curves.inputs[1])
			#points_to_curves.Curves -> curve_to_mesh.Curve
			_atoms_to_curves.links.new(points_to_curves.outputs[0], curve_to_mesh.inputs[0])
			#delete_geometry.Geometry -> store_named_attribute.Geometry
			_atoms_to_curves.links.new(delete_geometry.outputs[0], store_named_attribute.inputs[0])
			#group_006.Atoms -> separate_geometry_003.Geometry
			_atoms_to_curves.links.new(group_006.outputs[0], separate_geometry_003.inputs[0])
			#group_input_22.Selection -> separate_geometry_003.Selection
			_atoms_to_curves.links.new(group_input_22.outputs[1], separate_geometry_003.inputs[1])
			#curve_to_mesh.Mesh -> store_named_attribute_019.Geometry
			_atoms_to_curves.links.new(curve_to_mesh.outputs[0], store_named_attribute_019.inputs[0])
			#group_001_4.Selection -> separate_geometry_001.Selection
			_atoms_to_curves.links.new(group_001_4.outputs[0], separate_geometry_001.inputs[1])
			return _atoms_to_curves

		_atoms_to_curves = _atoms_to_curves_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".atoms_to_curves", type = 'NODES')
		mod.node_group = _atoms_to_curves
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_atoms_to_curves.bl_idname)
			
def register():
	bpy.utils.register_class(_atoms_to_curves)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_atoms_to_curves)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
