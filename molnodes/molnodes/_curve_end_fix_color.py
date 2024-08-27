bl_info = {
	"name" : ".curve_end_fix_color",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _curve_end_fix_color(bpy.types.Operator):
	bl_idname = "node._curve_end_fix_color"
	bl_label = ".curve_end_fix_color"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize offset_color node group
		def offset_color_node_group():
			offset_color = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Offset Color")

			offset_color.color_tag = 'NONE'
			offset_color.description = ""

			
			#offset_color interface
			#Socket Color
			color_socket = offset_color.interface.new_socket(name = "Color", in_out='OUTPUT', socket_type = 'NodeSocketColor')
			color_socket.default_value = (0.0, 0.0, 0.0, 0.0)
			color_socket.attribute_domain = 'POINT'
			
			#Socket Index
			index_socket = offset_color.interface.new_socket(name = "Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			index_socket.default_value = 0
			index_socket.min_value = -2147483648
			index_socket.max_value = 2147483647
			index_socket.subtype = 'NONE'
			index_socket.attribute_domain = 'POINT'
			
			#Socket Offset
			offset_socket = offset_color.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket.default_value = 0
			offset_socket.min_value = -2147483648
			offset_socket.max_value = 2147483647
			offset_socket.subtype = 'NONE'
			offset_socket.attribute_domain = 'POINT'
			
			
			#initialize offset_color nodes
			#node Group Input
			group_input = offset_color.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Math.012
			math_012 = offset_color.nodes.new("ShaderNodeMath")
			math_012.name = "Math.012"
			math_012.operation = 'ADD'
			math_012.use_clamp = False
			
			#node Evaluate at Index.004
			evaluate_at_index_004 = offset_color.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_004.name = "Evaluate at Index.004"
			evaluate_at_index_004.data_type = 'FLOAT_COLOR'
			evaluate_at_index_004.domain = 'POINT'
			
			#node Group Output
			group_output = offset_color.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Named Attribute
			named_attribute = offset_color.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute.inputs[0].default_value = "Color"
			
			
			
			
			#Set locations
			group_input.location = (-220.0, -20.0)
			math_012.location = (-40.0, 0.0)
			evaluate_at_index_004.location = (140.0, 0.0)
			group_output.location = (340.0, 0.0)
			named_attribute.location = (-40.0, -160.0)
			
			#Set dimensions
			group_input.width, group_input.height = 140.0, 100.0
			math_012.width, math_012.height = 140.0, 100.0
			evaluate_at_index_004.width, evaluate_at_index_004.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			
			#initialize offset_color links
			#math_012.Value -> evaluate_at_index_004.Index
			offset_color.links.new(math_012.outputs[0], evaluate_at_index_004.inputs[0])
			#group_input.Offset -> math_012.Value
			offset_color.links.new(group_input.outputs[1], math_012.inputs[1])
			#evaluate_at_index_004.Value -> group_output.Color
			offset_color.links.new(evaluate_at_index_004.outputs[0], group_output.inputs[0])
			#named_attribute.Attribute -> evaluate_at_index_004.Value
			offset_color.links.new(named_attribute.outputs[0], evaluate_at_index_004.inputs[1])
			#group_input.Index -> math_012.Value
			offset_color.links.new(group_input.outputs[0], math_012.inputs[0])
			return offset_color

		offset_color = offset_color_node_group()

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

		#initialize _curve_end_fix_color node group
		def _curve_end_fix_color_node_group():
			_curve_end_fix_color = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".curve_end_fix_color")

			_curve_end_fix_color.color_tag = 'NONE'
			_curve_end_fix_color.description = ""

			_curve_end_fix_color.is_modifier = True
			
			#_curve_end_fix_color interface
			#Socket Geometry
			geometry_socket = _curve_end_fix_color.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_1 = _curve_end_fix_color.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_1.attribute_domain = 'POINT'
			
			
			#initialize _curve_end_fix_color nodes
			#node Store Named Attribute
			store_named_attribute = _curve_end_fix_color.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute.name = "Store Named Attribute"
			store_named_attribute.data_type = 'FLOAT_COLOR'
			store_named_attribute.domain = 'POINT'
			#Name
			store_named_attribute.inputs[2].default_value = "Color"
			
			#node Switch.011
			switch_011 = _curve_end_fix_color.nodes.new("GeometryNodeSwitch")
			switch_011.name = "Switch.011"
			switch_011.input_type = 'RGBA'
			
			#node Group.029
			group_029 = _curve_end_fix_color.nodes.new("GeometryNodeGroup")
			group_029.name = "Group.029"
			group_029.node_tree = offset_color
			#Socket_0
			group_029.inputs[0].default_value = 0
			#Input_0
			group_029.inputs[1].default_value = -1
			
			#node Endpoint Selection.004
			endpoint_selection_004 = _curve_end_fix_color.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_004.name = "Endpoint Selection.004"
			#Start Size
			endpoint_selection_004.inputs[0].default_value = 0
			#End Size
			endpoint_selection_004.inputs[1].default_value = 1
			
			#node Endpoint Selection.003
			endpoint_selection_003 = _curve_end_fix_color.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_003.name = "Endpoint Selection.003"
			#Start Size
			endpoint_selection_003.inputs[0].default_value = 1
			#End Size
			endpoint_selection_003.inputs[1].default_value = 0
			
			#node Group.028
			group_028 = _curve_end_fix_color.nodes.new("GeometryNodeGroup")
			group_028.name = "Group.028"
			group_028.node_tree = offset_color
			#Socket_0
			group_028.inputs[0].default_value = 0
			#Input_0
			group_028.inputs[1].default_value = 1
			
			#node Switch.012
			switch_012 = _curve_end_fix_color.nodes.new("GeometryNodeSwitch")
			switch_012.name = "Switch.012"
			switch_012.input_type = 'RGBA'
			
			#node Named Attribute.001
			named_attribute_001 = _curve_end_fix_color.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute_001.inputs[0].default_value = "Color"
			
			#node Group.030
			group_030 = _curve_end_fix_color.nodes.new("GeometryNodeGroup")
			group_030.name = "Group.030"
			group_030.node_tree = _mn_select_sec_struct
			#Socket_1
			group_030.inputs[0].default_value = True
			
			#node Group Output
			group_output_6 = _curve_end_fix_color.nodes.new("NodeGroupOutput")
			group_output_6.name = "Group Output"
			group_output_6.is_active_output = True
			
			#node Group Input
			group_input_6 = _curve_end_fix_color.nodes.new("NodeGroupInput")
			group_input_6.name = "Group Input"
			
			
			
			
			#Set locations
			store_named_attribute.location = (180.0, 270.0)
			switch_011.location = (-20.0, -110.0)
			group_029.location = (160.0, -270.0)
			endpoint_selection_004.location = (160.0, 10.0)
			endpoint_selection_003.location = (-20.0, 10.0)
			group_028.location = (-20.0, -270.0)
			switch_012.location = (160.0, -110.0)
			named_attribute_001.location = (-180.0, -250.0)
			group_030.location = (-60.0, 190.0)
			group_output_6.location = (360.0, 320.0)
			group_input_6.location = (-40.0, 300.0)
			
			#Set dimensions
			store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
			switch_011.width, switch_011.height = 140.0, 100.0
			group_029.width, group_029.height = 140.0, 100.0
			endpoint_selection_004.width, endpoint_selection_004.height = 140.0, 100.0
			endpoint_selection_003.width, endpoint_selection_003.height = 140.0, 100.0
			group_028.width, group_028.height = 140.0, 100.0
			switch_012.width, switch_012.height = 140.0, 100.0
			named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
			group_030.width, group_030.height = 158.9053955078125, 100.0
			group_output_6.width, group_output_6.height = 140.0, 100.0
			group_input_6.width, group_input_6.height = 140.0, 100.0
			
			#initialize _curve_end_fix_color links
			#switch_011.Output -> switch_012.False
			_curve_end_fix_color.links.new(switch_011.outputs[0], switch_012.inputs[1])
			#named_attribute_001.Attribute -> switch_011.False
			_curve_end_fix_color.links.new(named_attribute_001.outputs[0], switch_011.inputs[1])
			#endpoint_selection_003.Selection -> switch_011.Switch
			_curve_end_fix_color.links.new(endpoint_selection_003.outputs[0], switch_011.inputs[0])
			#group_028.Color -> switch_011.True
			_curve_end_fix_color.links.new(group_028.outputs[0], switch_011.inputs[2])
			#group_029.Color -> switch_012.True
			_curve_end_fix_color.links.new(group_029.outputs[0], switch_012.inputs[2])
			#switch_012.Output -> store_named_attribute.Value
			_curve_end_fix_color.links.new(switch_012.outputs[0], store_named_attribute.inputs[3])
			#group_030.Is Structured -> store_named_attribute.Selection
			_curve_end_fix_color.links.new(group_030.outputs[2], store_named_attribute.inputs[1])
			#endpoint_selection_004.Selection -> switch_012.Switch
			_curve_end_fix_color.links.new(endpoint_selection_004.outputs[0], switch_012.inputs[0])
			#group_input_6.Geometry -> store_named_attribute.Geometry
			_curve_end_fix_color.links.new(group_input_6.outputs[0], store_named_attribute.inputs[0])
			#store_named_attribute.Geometry -> group_output_6.Geometry
			_curve_end_fix_color.links.new(store_named_attribute.outputs[0], group_output_6.inputs[0])
			return _curve_end_fix_color

		_curve_end_fix_color = _curve_end_fix_color_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".curve_end_fix_color", type = 'NODES')
		mod.node_group = _curve_end_fix_color
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_curve_end_fix_color.bl_idname)
			
def register():
	bpy.utils.register_class(_curve_end_fix_color)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_curve_end_fix_color)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
