bl_info = {
	"name" : ".cartoon_arrow_instance",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _cartoon_arrow_instance(bpy.types.Operator):
	bl_idname = "node._cartoon_arrow_instance"
	bl_label = ".cartoon_arrow_instance"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _field_offset_vec node group
		def _field_offset_vec_node_group():
			_field_offset_vec = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".field_offset_vec")

			_field_offset_vec.color_tag = 'NONE'
			_field_offset_vec.description = ""

			
			#_field_offset_vec interface
			#Socket Field
			field_socket = _field_offset_vec.interface.new_socket(name = "Field", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			field_socket.subtype = 'NONE'
			field_socket.default_value = (0.0, 0.0, 0.0)
			field_socket.min_value = -3.4028234663852886e+38
			field_socket.max_value = 3.4028234663852886e+38
			field_socket.attribute_domain = 'POINT'
			
			#Socket Field
			field_socket_1 = _field_offset_vec.interface.new_socket(name = "Field", in_out='INPUT', socket_type = 'NodeSocketVector')
			field_socket_1.subtype = 'NONE'
			field_socket_1.default_value = (0.0, 0.0, 0.0)
			field_socket_1.min_value = -3.4028234663852886e+38
			field_socket_1.max_value = 3.4028234663852886e+38
			field_socket_1.attribute_domain = 'POINT'
			field_socket_1.hide_value = True
			
			#Socket Offset
			offset_socket = _field_offset_vec.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket.subtype = 'NONE'
			offset_socket.default_value = 0
			offset_socket.min_value = -2147483648
			offset_socket.max_value = 2147483647
			offset_socket.attribute_domain = 'POINT'
			
			
			#initialize _field_offset_vec nodes
			#node Group Input
			group_input = _field_offset_vec.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Evaluate at Index
			evaluate_at_index = _field_offset_vec.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index.name = "Evaluate at Index"
			evaluate_at_index.data_type = 'FLOAT_VECTOR'
			evaluate_at_index.domain = 'POINT'
			
			#node Group Output
			group_output = _field_offset_vec.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Math.001
			math_001 = _field_offset_vec.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.operation = 'ADD'
			math_001.use_clamp = False
			
			#node Index
			index = _field_offset_vec.nodes.new("GeometryNodeInputIndex")
			index.name = "Index"
			
			
			
			
			#Set locations
			group_input.location = (-417.64404296875, 0.0)
			evaluate_at_index.location = (-220.0, 100.0)
			group_output.location = (20.0, 20.0)
			math_001.location = (-220.0, -80.0)
			index.location = (-400.0, -180.0)
			
			#Set dimensions
			group_input.width, group_input.height = 140.0, 100.0
			evaluate_at_index.width, evaluate_at_index.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			index.width, index.height = 140.0, 100.0
			
			#initialize _field_offset_vec links
			#math_001.Value -> evaluate_at_index.Index
			_field_offset_vec.links.new(math_001.outputs[0], evaluate_at_index.inputs[0])
			#group_input.Field -> evaluate_at_index.Value
			_field_offset_vec.links.new(group_input.outputs[0], evaluate_at_index.inputs[1])
			#group_input.Offset -> math_001.Value
			_field_offset_vec.links.new(group_input.outputs[1], math_001.inputs[0])
			#evaluate_at_index.Value -> group_output.Field
			_field_offset_vec.links.new(evaluate_at_index.outputs[0], group_output.inputs[0])
			#index.Index -> math_001.Value
			_field_offset_vec.links.new(index.outputs[0], math_001.inputs[1])
			return _field_offset_vec

		_field_offset_vec = _field_offset_vec_node_group()

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

		#initialize _cartoon_arrow_instance node group
		def _cartoon_arrow_instance_node_group():
			_cartoon_arrow_instance = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".cartoon_arrow_instance")

			_cartoon_arrow_instance.color_tag = 'NONE'
			_cartoon_arrow_instance.description = ""

			_cartoon_arrow_instance.is_modifier = True
			
			#_cartoon_arrow_instance interface
			#Socket Trimmed Curve
			trimmed_curve_socket = _cartoon_arrow_instance.interface.new_socket(name = "Trimmed Curve", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			trimmed_curve_socket.attribute_domain = 'POINT'
			
			#Socket ArrowHeads
			arrowheads_socket = _cartoon_arrow_instance.interface.new_socket(name = "ArrowHeads", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			arrowheads_socket.attribute_domain = 'POINT'
			
			#Socket Curve
			curve_socket = _cartoon_arrow_instance.interface.new_socket(name = "Curve", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			curve_socket.attribute_domain = 'POINT'
			
			#Socket Instance
			instance_socket = _cartoon_arrow_instance.interface.new_socket(name = "Instance", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			instance_socket.attribute_domain = 'POINT'
			
			#Socket Rotation
			rotation_socket = _cartoon_arrow_instance.interface.new_socket(name = "Rotation", in_out='INPUT', socket_type = 'NodeSocketVector')
			rotation_socket.subtype = 'EULER'
			rotation_socket.default_value = (0.0, 0.0, 0.0)
			rotation_socket.min_value = -3.4028234663852886e+38
			rotation_socket.max_value = 3.4028234663852886e+38
			rotation_socket.attribute_domain = 'POINT'
			rotation_socket.hide_value = True
			
			#Socket Scale
			scale_socket = _cartoon_arrow_instance.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketVector')
			scale_socket.subtype = 'XYZ'
			scale_socket.default_value = (1.0, 1.0, 1.0)
			scale_socket.min_value = -3.4028234663852886e+38
			scale_socket.max_value = 3.4028234663852886e+38
			scale_socket.attribute_domain = 'POINT'
			
			
			#initialize _cartoon_arrow_instance nodes
			#node Boolean Math.004
			boolean_math_004 = _cartoon_arrow_instance.nodes.new("FunctionNodeBooleanMath")
			boolean_math_004.name = "Boolean Math.004"
			boolean_math_004.operation = 'AND'
			
			#node Boolean Math.005
			boolean_math_005 = _cartoon_arrow_instance.nodes.new("FunctionNodeBooleanMath")
			boolean_math_005.name = "Boolean Math.005"
			boolean_math_005.operation = 'AND'
			
			#node Reroute.007
			reroute_007 = _cartoon_arrow_instance.nodes.new("NodeReroute")
			reroute_007.name = "Reroute.007"
			#node Instance on Points
			instance_on_points = _cartoon_arrow_instance.nodes.new("GeometryNodeInstanceOnPoints")
			instance_on_points.name = "Instance on Points"
			#Pick Instance
			instance_on_points.inputs[3].default_value = False
			#Instance Index
			instance_on_points.inputs[4].default_value = 0
			
			#node Group Output
			group_output_6 = _cartoon_arrow_instance.nodes.new("NodeGroupOutput")
			group_output_6.name = "Group Output"
			group_output_6.is_active_output = True
			
			#node Align Euler to Vector
			align_euler_to_vector = _cartoon_arrow_instance.nodes.new("FunctionNodeAlignEulerToVector")
			align_euler_to_vector.name = "Align Euler to Vector"
			align_euler_to_vector.axis = 'X'
			align_euler_to_vector.pivot_axis = 'Y'
			#Factor
			align_euler_to_vector.inputs[1].default_value = 1.0
			
			#node Endpoint Selection.001
			endpoint_selection_001 = _cartoon_arrow_instance.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_001.name = "Endpoint Selection.001"
			#Start Size
			endpoint_selection_001.inputs[0].default_value = 0
			#End Size
			endpoint_selection_001.inputs[1].default_value = 1
			
			#node Endpoint Selection
			endpoint_selection = _cartoon_arrow_instance.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection.name = "Endpoint Selection"
			#Start Size
			endpoint_selection.inputs[0].default_value = 0
			#End Size
			endpoint_selection.inputs[1].default_value = 2
			
			#node Boolean Math.001
			boolean_math_001_2 = _cartoon_arrow_instance.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_2.name = "Boolean Math.001"
			boolean_math_001_2.operation = 'NOT'
			
			#node Boolean Math.003
			boolean_math_003 = _cartoon_arrow_instance.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003.name = "Boolean Math.003"
			boolean_math_003.operation = 'AND'
			
			#node Reroute
			reroute = _cartoon_arrow_instance.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Position.001
			position_001 = _cartoon_arrow_instance.nodes.new("GeometryNodeInputPosition")
			position_001.name = "Position.001"
			
			#node Vector Math
			vector_math = _cartoon_arrow_instance.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.operation = 'SUBTRACT'
			
			#node Group.006
			group_006 = _cartoon_arrow_instance.nodes.new("GeometryNodeGroup")
			group_006.name = "Group.006"
			group_006.node_tree = _field_offset_vec
			#Input_1
			group_006.inputs[1].default_value = 1
			
			#node Group.018
			group_018 = _cartoon_arrow_instance.nodes.new("GeometryNodeGroup")
			group_018.name = "Group.018"
			group_018.node_tree = _mn_select_sec_struct
			#Socket_1
			group_018.inputs[0].default_value = True
			
			#node Group Input
			group_input_6 = _cartoon_arrow_instance.nodes.new("NodeGroupInput")
			group_input_6.name = "Group Input"
			
			#node Delete Geometry
			delete_geometry = _cartoon_arrow_instance.nodes.new("GeometryNodeDeleteGeometry")
			delete_geometry.name = "Delete Geometry"
			delete_geometry.domain = 'POINT'
			delete_geometry.mode = 'ALL'
			
			
			
			
			#Set locations
			boolean_math_004.location = (-239.0887451171875, 169.322998046875)
			boolean_math_005.location = (-240.0, 22.557861328125)
			reroute_007.location = (-420.0, -200.0)
			instance_on_points.location = (700.0, 180.0)
			group_output_6.location = (1140.0, -20.0)
			align_euler_to_vector.location = (260.0, 60.0)
			endpoint_selection_001.location = (-660.0, 280.0)
			endpoint_selection.location = (-660.0, 160.0)
			boolean_math_001_2.location = (-440.0, 340.0)
			boolean_math_003.location = (-440.0, 220.0)
			reroute.location = (-380.0, 0.0)
			position_001.location = (-40.0, -140.0)
			vector_math.location = (166.50079345703125, -140.0)
			group_006.location = (164.67938232421875, -280.0)
			group_018.location = (-700.0, 20.0)
			group_input_6.location = (-660.0, -180.0)
			delete_geometry.location = (108.09152221679688, -434.36468505859375)
			
			#Set dimensions
			boolean_math_004.width, boolean_math_004.height = 140.0, 100.0
			boolean_math_005.width, boolean_math_005.height = 140.0, 100.0
			reroute_007.width, reroute_007.height = 16.0, 100.0
			instance_on_points.width, instance_on_points.height = 140.0, 100.0
			group_output_6.width, group_output_6.height = 140.0, 100.0
			align_euler_to_vector.width, align_euler_to_vector.height = 140.0, 100.0
			endpoint_selection_001.width, endpoint_selection_001.height = 140.0, 100.0
			endpoint_selection.width, endpoint_selection.height = 140.0, 100.0
			boolean_math_001_2.width, boolean_math_001_2.height = 140.0, 100.0
			boolean_math_003.width, boolean_math_003.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			position_001.width, position_001.height = 140.0, 100.0
			vector_math.width, vector_math.height = 233.49920654296875, 100.0
			group_006.width, group_006.height = 235.32061767578125, 100.0
			group_018.width, group_018.height = 234.5810546875, 100.0
			group_input_6.width, group_input_6.height = 140.0, 100.0
			delete_geometry.width, delete_geometry.height = 140.0, 100.0
			
			#initialize _cartoon_arrow_instance links
			#reroute_007.Output -> instance_on_points.Points
			_cartoon_arrow_instance.links.new(reroute_007.outputs[0], instance_on_points.inputs[0])
			#position_001.Position -> vector_math.Vector
			_cartoon_arrow_instance.links.new(position_001.outputs[0], vector_math.inputs[0])
			#boolean_math_004.Boolean -> instance_on_points.Selection
			_cartoon_arrow_instance.links.new(boolean_math_004.outputs[0], instance_on_points.inputs[1])
			#endpoint_selection.Selection -> boolean_math_003.Boolean
			_cartoon_arrow_instance.links.new(endpoint_selection.outputs[0], boolean_math_003.inputs[1])
			#align_euler_to_vector.Rotation -> instance_on_points.Rotation
			_cartoon_arrow_instance.links.new(align_euler_to_vector.outputs[0], instance_on_points.inputs[5])
			#endpoint_selection_001.Selection -> boolean_math_001_2.Boolean
			_cartoon_arrow_instance.links.new(endpoint_selection_001.outputs[0], boolean_math_001_2.inputs[0])
			#boolean_math_005.Boolean -> delete_geometry.Selection
			_cartoon_arrow_instance.links.new(boolean_math_005.outputs[0], delete_geometry.inputs[1])
			#reroute_007.Output -> delete_geometry.Geometry
			_cartoon_arrow_instance.links.new(reroute_007.outputs[0], delete_geometry.inputs[0])
			#endpoint_selection_001.Selection -> boolean_math_005.Boolean
			_cartoon_arrow_instance.links.new(endpoint_selection_001.outputs[0], boolean_math_005.inputs[0])
			#boolean_math_003.Boolean -> boolean_math_004.Boolean
			_cartoon_arrow_instance.links.new(boolean_math_003.outputs[0], boolean_math_004.inputs[0])
			#position_001.Position -> group_006.Field
			_cartoon_arrow_instance.links.new(position_001.outputs[0], group_006.inputs[0])
			#boolean_math_001_2.Boolean -> boolean_math_003.Boolean
			_cartoon_arrow_instance.links.new(boolean_math_001_2.outputs[0], boolean_math_003.inputs[0])
			#vector_math.Vector -> align_euler_to_vector.Vector
			_cartoon_arrow_instance.links.new(vector_math.outputs[0], align_euler_to_vector.inputs[2])
			#group_input_6.Instance -> instance_on_points.Instance
			_cartoon_arrow_instance.links.new(group_input_6.outputs[1], instance_on_points.inputs[2])
			#group_input_6.Curve -> reroute_007.Input
			_cartoon_arrow_instance.links.new(group_input_6.outputs[0], reroute_007.inputs[0])
			#group_input_6.Rotation -> align_euler_to_vector.Rotation
			_cartoon_arrow_instance.links.new(group_input_6.outputs[2], align_euler_to_vector.inputs[0])
			#delete_geometry.Geometry -> group_output_6.Trimmed Curve
			_cartoon_arrow_instance.links.new(delete_geometry.outputs[0], group_output_6.inputs[0])
			#instance_on_points.Instances -> group_output_6.ArrowHeads
			_cartoon_arrow_instance.links.new(instance_on_points.outputs[0], group_output_6.inputs[1])
			#group_input_6.Scale -> instance_on_points.Scale
			_cartoon_arrow_instance.links.new(group_input_6.outputs[3], instance_on_points.inputs[6])
			#group_006.Field -> vector_math.Vector
			_cartoon_arrow_instance.links.new(group_006.outputs[0], vector_math.inputs[1])
			#reroute.Output -> boolean_math_004.Boolean
			_cartoon_arrow_instance.links.new(reroute.outputs[0], boolean_math_004.inputs[1])
			#reroute.Output -> boolean_math_005.Boolean
			_cartoon_arrow_instance.links.new(reroute.outputs[0], boolean_math_005.inputs[1])
			#group_018.Is Sheet -> reroute.Input
			_cartoon_arrow_instance.links.new(group_018.outputs[1], reroute.inputs[0])
			return _cartoon_arrow_instance

		_cartoon_arrow_instance = _cartoon_arrow_instance_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".cartoon_arrow_instance", type = 'NODES')
		mod.node_group = _cartoon_arrow_instance
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_cartoon_arrow_instance.bl_idname)
			
def register():
	bpy.utils.register_class(_cartoon_arrow_instance)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_cartoon_arrow_instance)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
