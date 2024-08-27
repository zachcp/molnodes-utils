bl_info = {
	"name" : ".curve_ends_adjust_angle",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _curve_ends_adjust_angle(bpy.types.Operator):
	bl_idname = "node._curve_ends_adjust_angle"
	bl_label = ".curve_ends_adjust_angle"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
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
			group_input = _mn_world_scale.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Value
			value = _mn_world_scale.nodes.new("ShaderNodeValue")
			value.label = "world_scale"
			value.name = "Value"
			
			value.outputs[0].default_value = 0.009999999776482582
			#node Group Output
			group_output = _mn_world_scale.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			
			
			
			#Set locations
			group_input.location = (-200.0, 0.0)
			value.location = (0.0, 0.0)
			group_output.location = (190.0, 0.0)
			
			#Set dimensions
			group_input.width, group_input.height = 140.0, 100.0
			value.width, value.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			
			#initialize _mn_world_scale links
			#value.Value -> group_output.world_scale
			_mn_world_scale.links.new(value.outputs[0], group_output.inputs[0])
			return _mn_world_scale

		_mn_world_scale = _mn_world_scale_node_group()

		#initialize mn_units node group
		def mn_units_node_group():
			mn_units = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "MN Units")

			mn_units.color_tag = 'NONE'
			mn_units.description = ""

			
			#mn_units interface
			#Socket Angstrom
			angstrom_socket = mn_units.interface.new_socket(name = "Angstrom", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			angstrom_socket.default_value = 0.0
			angstrom_socket.min_value = -3.4028234663852886e+38
			angstrom_socket.max_value = 3.4028234663852886e+38
			angstrom_socket.subtype = 'NONE'
			angstrom_socket.attribute_domain = 'POINT'
			
			#Socket Nanometre
			nanometre_socket = mn_units.interface.new_socket(name = "Nanometre", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			nanometre_socket.default_value = 0.0
			nanometre_socket.min_value = -3.4028234663852886e+38
			nanometre_socket.max_value = 3.4028234663852886e+38
			nanometre_socket.subtype = 'NONE'
			nanometre_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket = mn_units.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket.default_value = 3.0
			value_socket.min_value = -10000.0
			value_socket.max_value = 10000.0
			value_socket.subtype = 'NONE'
			value_socket.attribute_domain = 'POINT'
			value_socket.description = "A value which will be scaled appropriately for the world"
			
			
			#initialize mn_units nodes
			#node Group Output
			group_output_1 = mn_units.nodes.new("NodeGroupOutput")
			group_output_1.name = "Group Output"
			group_output_1.is_active_output = True
			
			#node Group Input
			group_input_1 = mn_units.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			
			#node Math
			math = mn_units.nodes.new("ShaderNodeMath")
			math.name = "Math"
			math.operation = 'MULTIPLY'
			math.use_clamp = False
			
			#node Math.001
			math_001 = mn_units.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.operation = 'MULTIPLY'
			math_001.use_clamp = False
			#Value_001
			math_001.inputs[1].default_value = 10.0
			
			#node Group
			group = mn_units.nodes.new("GeometryNodeGroup")
			group.name = "Group"
			group.node_tree = _mn_world_scale
			
			
			
			
			#Set locations
			group_output_1.location = (190.0, 0.0)
			group_input_1.location = (-240.0, 0.0)
			math.location = (-60.0, 0.0)
			math_001.location = (-60.0, -160.0)
			group.location = (-304.00421142578125, -104.114013671875)
			
			#Set dimensions
			group_output_1.width, group_output_1.height = 140.0, 100.0
			group_input_1.width, group_input_1.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			group.width, group.height = 197.58424377441406, 100.0
			
			#initialize mn_units links
			#math.Value -> group_output_1.Angstrom
			mn_units.links.new(math.outputs[0], group_output_1.inputs[0])
			#group_input_1.Value -> math.Value
			mn_units.links.new(group_input_1.outputs[0], math.inputs[0])
			#group.world_scale -> math.Value
			mn_units.links.new(group.outputs[0], math.inputs[1])
			#math.Value -> math_001.Value
			mn_units.links.new(math.outputs[0], math_001.inputs[0])
			#math_001.Value -> group_output_1.Nanometre
			mn_units.links.new(math_001.outputs[0], group_output_1.inputs[1])
			return mn_units

		mn_units = mn_units_node_group()

		#initialize _field_offset_vec node group
		def _field_offset_vec_node_group():
			_field_offset_vec = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".field_offset_vec")

			_field_offset_vec.color_tag = 'NONE'
			_field_offset_vec.description = ""

			
			#_field_offset_vec interface
			#Socket Field
			field_socket = _field_offset_vec.interface.new_socket(name = "Field", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			field_socket.default_value = (0.0, 0.0, 0.0)
			field_socket.min_value = -3.4028234663852886e+38
			field_socket.max_value = 3.4028234663852886e+38
			field_socket.subtype = 'NONE'
			field_socket.attribute_domain = 'POINT'
			
			#Socket Field
			field_socket_1 = _field_offset_vec.interface.new_socket(name = "Field", in_out='INPUT', socket_type = 'NodeSocketVector')
			field_socket_1.default_value = (0.0, 0.0, 0.0)
			field_socket_1.min_value = -3.4028234663852886e+38
			field_socket_1.max_value = 3.4028234663852886e+38
			field_socket_1.subtype = 'NONE'
			field_socket_1.attribute_domain = 'POINT'
			field_socket_1.hide_value = True
			
			#Socket Offset
			offset_socket = _field_offset_vec.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket.default_value = 0
			offset_socket.min_value = -2147483648
			offset_socket.max_value = 2147483647
			offset_socket.subtype = 'NONE'
			offset_socket.attribute_domain = 'POINT'
			
			
			#initialize _field_offset_vec nodes
			#node Group Input
			group_input_2 = _field_offset_vec.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
			#node Evaluate at Index
			evaluate_at_index = _field_offset_vec.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index.name = "Evaluate at Index"
			evaluate_at_index.data_type = 'FLOAT_VECTOR'
			evaluate_at_index.domain = 'POINT'
			
			#node Group Output
			group_output_2 = _field_offset_vec.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Math.001
			math_001_1 = _field_offset_vec.nodes.new("ShaderNodeMath")
			math_001_1.name = "Math.001"
			math_001_1.operation = 'ADD'
			math_001_1.use_clamp = False
			
			#node Index
			index = _field_offset_vec.nodes.new("GeometryNodeInputIndex")
			index.name = "Index"
			
			
			
			
			#Set locations
			group_input_2.location = (-417.64404296875, 0.0)
			evaluate_at_index.location = (-220.0, 100.0)
			group_output_2.location = (20.0, 20.0)
			math_001_1.location = (-220.0, -80.0)
			index.location = (-400.0, -180.0)
			
			#Set dimensions
			group_input_2.width, group_input_2.height = 140.0, 100.0
			evaluate_at_index.width, evaluate_at_index.height = 140.0, 100.0
			group_output_2.width, group_output_2.height = 140.0, 100.0
			math_001_1.width, math_001_1.height = 140.0, 100.0
			index.width, index.height = 140.0, 100.0
			
			#initialize _field_offset_vec links
			#math_001_1.Value -> evaluate_at_index.Index
			_field_offset_vec.links.new(math_001_1.outputs[0], evaluate_at_index.inputs[0])
			#group_input_2.Field -> evaluate_at_index.Value
			_field_offset_vec.links.new(group_input_2.outputs[0], evaluate_at_index.inputs[1])
			#group_input_2.Offset -> math_001_1.Value
			_field_offset_vec.links.new(group_input_2.outputs[1], math_001_1.inputs[0])
			#evaluate_at_index.Value -> group_output_2.Field
			_field_offset_vec.links.new(evaluate_at_index.outputs[0], group_output_2.inputs[0])
			#index.Index -> math_001_1.Value
			_field_offset_vec.links.new(index.outputs[0], math_001_1.inputs[1])
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
			group_output_3 = _mn_select_sec_struct_id.nodes.new("NodeGroupOutput")
			group_output_3.name = "Group Output"
			group_output_3.is_active_output = True
			
			#node Compare.012
			compare_012 = _mn_select_sec_struct_id.nodes.new("FunctionNodeCompare")
			compare_012.name = "Compare.012"
			compare_012.data_type = 'INT'
			compare_012.mode = 'ELEMENT'
			compare_012.operation = 'EQUAL'
			
			#node Group Input
			group_input_3 = _mn_select_sec_struct_id.nodes.new("NodeGroupInput")
			group_input_3.name = "Group Input"
			
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
			group_output_3.location = (760.0, 200.0)
			compare_012.location = (240.0, 100.0)
			group_input_3.location = (80.0, 100.0)
			boolean_math_001.location = (579.9999389648438, 196.54164123535156)
			boolean_math_002.location = (580.0, 60.0)
			
			#Set dimensions
			named_attribute_002.width, named_attribute_002.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			group_output_3.width, group_output_3.height = 140.0, 100.0
			compare_012.width, compare_012.height = 140.0, 100.0
			group_input_3.width, group_input_3.height = 140.0, 100.0
			boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
			boolean_math_002.width, boolean_math_002.height = 140.0, 100.0
			
			#initialize _mn_select_sec_struct_id links
			#boolean_math_001.Boolean -> group_output_3.Selection
			_mn_select_sec_struct_id.links.new(boolean_math_001.outputs[0], group_output_3.inputs[0])
			#compare_012.Result -> boolean_math.Boolean
			_mn_select_sec_struct_id.links.new(compare_012.outputs[0], boolean_math.inputs[1])
			#group_input_3.id -> compare_012.A
			_mn_select_sec_struct_id.links.new(group_input_3.outputs[2], compare_012.inputs[2])
			#group_input_3.And -> boolean_math.Boolean
			_mn_select_sec_struct_id.links.new(group_input_3.outputs[0], boolean_math.inputs[0])
			#named_attribute_002.Attribute -> compare_012.B
			_mn_select_sec_struct_id.links.new(named_attribute_002.outputs[0], compare_012.inputs[3])
			#boolean_math.Boolean -> boolean_math_001.Boolean
			_mn_select_sec_struct_id.links.new(boolean_math.outputs[0], boolean_math_001.inputs[0])
			#group_input_3.Or -> boolean_math_001.Boolean
			_mn_select_sec_struct_id.links.new(group_input_3.outputs[1], boolean_math_001.inputs[1])
			#boolean_math_001.Boolean -> boolean_math_002.Boolean
			_mn_select_sec_struct_id.links.new(boolean_math_001.outputs[0], boolean_math_002.inputs[0])
			#boolean_math_002.Boolean -> group_output_3.Inverted
			_mn_select_sec_struct_id.links.new(boolean_math_002.outputs[0], group_output_3.inputs[1])
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
			group_output_4 = is_sheet.nodes.new("NodeGroupOutput")
			group_output_4.name = "Group Output"
			group_output_4.is_active_output = True
			
			#node Group Input
			group_input_4 = is_sheet.nodes.new("NodeGroupInput")
			group_input_4.name = "Group Input"
			
			#node MN_select_sec_struct.002
			mn_select_sec_struct_002 = is_sheet.nodes.new("GeometryNodeGroup")
			mn_select_sec_struct_002.label = "Select Sec Struct"
			mn_select_sec_struct_002.name = "MN_select_sec_struct.002"
			mn_select_sec_struct_002.node_tree = _mn_select_sec_struct_id
			#Socket_1
			mn_select_sec_struct_002.inputs[2].default_value = 2
			
			
			
			
			#Set locations
			group_output_4.location = (267.00146484375, 0.0)
			group_input_4.location = (-220.0, -80.0)
			mn_select_sec_struct_002.location = (0.0, 0.0)
			
			#Set dimensions
			group_output_4.width, group_output_4.height = 140.0, 100.0
			group_input_4.width, group_input_4.height = 140.0, 100.0
			mn_select_sec_struct_002.width, mn_select_sec_struct_002.height = 217.00146484375, 100.0
			
			#initialize is_sheet links
			#mn_select_sec_struct_002.Selection -> group_output_4.Selection
			is_sheet.links.new(mn_select_sec_struct_002.outputs[0], group_output_4.inputs[0])
			#group_input_4.And -> mn_select_sec_struct_002.And
			is_sheet.links.new(group_input_4.outputs[0], mn_select_sec_struct_002.inputs[0])
			#group_input_4.Or -> mn_select_sec_struct_002.Or
			is_sheet.links.new(group_input_4.outputs[1], mn_select_sec_struct_002.inputs[1])
			#mn_select_sec_struct_002.Inverted -> group_output_4.Inverted
			is_sheet.links.new(mn_select_sec_struct_002.outputs[1], group_output_4.inputs[1])
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
			group_output_5 = is_loop.nodes.new("NodeGroupOutput")
			group_output_5.name = "Group Output"
			group_output_5.is_active_output = True
			
			#node Group Input
			group_input_5 = is_loop.nodes.new("NodeGroupInput")
			group_input_5.name = "Group Input"
			
			#node MN_select_sec_struct.002
			mn_select_sec_struct_002_1 = is_loop.nodes.new("GeometryNodeGroup")
			mn_select_sec_struct_002_1.label = "Select Sec Struct"
			mn_select_sec_struct_002_1.name = "MN_select_sec_struct.002"
			mn_select_sec_struct_002_1.node_tree = _mn_select_sec_struct_id
			#Socket_1
			mn_select_sec_struct_002_1.inputs[2].default_value = 3
			
			
			
			
			#Set locations
			group_output_5.location = (267.00146484375, 0.0)
			group_input_5.location = (-200.0, 0.0)
			mn_select_sec_struct_002_1.location = (0.0, 0.0)
			
			#Set dimensions
			group_output_5.width, group_output_5.height = 140.0, 100.0
			group_input_5.width, group_input_5.height = 140.0, 100.0
			mn_select_sec_struct_002_1.width, mn_select_sec_struct_002_1.height = 217.00146484375, 100.0
			
			#initialize is_loop links
			#mn_select_sec_struct_002_1.Selection -> group_output_5.Selection
			is_loop.links.new(mn_select_sec_struct_002_1.outputs[0], group_output_5.inputs[0])
			#group_input_5.And -> mn_select_sec_struct_002_1.And
			is_loop.links.new(group_input_5.outputs[0], mn_select_sec_struct_002_1.inputs[0])
			#group_input_5.Or -> mn_select_sec_struct_002_1.Or
			is_loop.links.new(group_input_5.outputs[1], mn_select_sec_struct_002_1.inputs[1])
			#mn_select_sec_struct_002_1.Inverted -> group_output_5.Inverted
			is_loop.links.new(mn_select_sec_struct_002_1.outputs[1], group_output_5.inputs[1])
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
			group_output_6 = is_helix.nodes.new("NodeGroupOutput")
			group_output_6.name = "Group Output"
			group_output_6.is_active_output = True
			
			#node Group Input
			group_input_6 = is_helix.nodes.new("NodeGroupInput")
			group_input_6.name = "Group Input"
			
			#node MN_select_sec_struct.002
			mn_select_sec_struct_002_2 = is_helix.nodes.new("GeometryNodeGroup")
			mn_select_sec_struct_002_2.label = "Select Sec Struct"
			mn_select_sec_struct_002_2.name = "MN_select_sec_struct.002"
			mn_select_sec_struct_002_2.node_tree = _mn_select_sec_struct_id
			#Socket_1
			mn_select_sec_struct_002_2.inputs[2].default_value = 1
			
			
			
			
			#Set locations
			group_output_6.location = (267.00146484375, 0.0)
			group_input_6.location = (-200.0, 0.0)
			mn_select_sec_struct_002_2.location = (0.0, 0.0)
			
			#Set dimensions
			group_output_6.width, group_output_6.height = 140.0, 100.0
			group_input_6.width, group_input_6.height = 140.0, 100.0
			mn_select_sec_struct_002_2.width, mn_select_sec_struct_002_2.height = 217.00146484375, 100.0
			
			#initialize is_helix links
			#mn_select_sec_struct_002_2.Selection -> group_output_6.Selection
			is_helix.links.new(mn_select_sec_struct_002_2.outputs[0], group_output_6.inputs[0])
			#group_input_6.And -> mn_select_sec_struct_002_2.And
			is_helix.links.new(group_input_6.outputs[0], mn_select_sec_struct_002_2.inputs[0])
			#group_input_6.Or -> mn_select_sec_struct_002_2.Or
			is_helix.links.new(group_input_6.outputs[1], mn_select_sec_struct_002_2.inputs[1])
			#mn_select_sec_struct_002_2.Inverted -> group_output_6.Inverted
			is_helix.links.new(mn_select_sec_struct_002_2.outputs[1], group_output_6.inputs[1])
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
			group_1 = _mn_select_sec_struct.nodes.new("GeometryNodeGroup")
			group_1.name = "Group"
			group_1.node_tree = is_helix
			#Socket_3
			group_1.inputs[1].default_value = False
			
			#node Boolean Math.001
			boolean_math_001_1 = _mn_select_sec_struct.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_1.name = "Boolean Math.001"
			boolean_math_001_1.hide = True
			boolean_math_001_1.operation = 'NOT'
			
			#node Group Output
			group_output_7 = _mn_select_sec_struct.nodes.new("NodeGroupOutput")
			group_output_7.name = "Group Output"
			group_output_7.is_active_output = True
			
			#node Group Input
			group_input_7 = _mn_select_sec_struct.nodes.new("NodeGroupInput")
			group_input_7.name = "Group Input"
			group_input_7.outputs[1].hide = True
			
			
			
			
			#Set locations
			group_001.location = (120.0, -60.0)
			group_002.location = (120.0, -180.0)
			group_1.location = (120.0, 60.0)
			boolean_math_001_1.location = (300.0, -140.0)
			group_output_7.location = (540.0, -60.0)
			group_input_7.location = (-160.0, -40.0)
			
			#Set dimensions
			group_001.width, group_001.height = 140.0, 100.0
			group_002.width, group_002.height = 140.0, 100.0
			group_1.width, group_1.height = 140.0, 100.0
			boolean_math_001_1.width, boolean_math_001_1.height = 140.0, 100.0
			group_output_7.width, group_output_7.height = 140.0, 100.0
			group_input_7.width, group_input_7.height = 140.0, 100.0
			
			#initialize _mn_select_sec_struct links
			#group_002.Selection -> group_output_7.Is Loop
			_mn_select_sec_struct.links.new(group_002.outputs[0], group_output_7.inputs[3])
			#group_002.Selection -> boolean_math_001_1.Boolean
			_mn_select_sec_struct.links.new(group_002.outputs[0], boolean_math_001_1.inputs[0])
			#boolean_math_001_1.Boolean -> group_output_7.Is Structured
			_mn_select_sec_struct.links.new(boolean_math_001_1.outputs[0], group_output_7.inputs[2])
			#group_1.Selection -> group_output_7.Is Helix
			_mn_select_sec_struct.links.new(group_1.outputs[0], group_output_7.inputs[0])
			#group_001.Selection -> group_output_7.Is Sheet
			_mn_select_sec_struct.links.new(group_001.outputs[0], group_output_7.inputs[1])
			#group_input_7.And -> group_1.And
			_mn_select_sec_struct.links.new(group_input_7.outputs[0], group_1.inputs[0])
			#group_input_7.And -> group_001.And
			_mn_select_sec_struct.links.new(group_input_7.outputs[0], group_001.inputs[0])
			#group_input_7.And -> group_002.And
			_mn_select_sec_struct.links.new(group_input_7.outputs[0], group_002.inputs[0])
			return _mn_select_sec_struct

		_mn_select_sec_struct = _mn_select_sec_struct_node_group()

		#initialize _curve_ends_adjust_angle node group
		def _curve_ends_adjust_angle_node_group():
			_curve_ends_adjust_angle = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".curve_ends_adjust_angle")

			_curve_ends_adjust_angle.color_tag = 'NONE'
			_curve_ends_adjust_angle.description = ""

			_curve_ends_adjust_angle.is_modifier = True
			
			#_curve_ends_adjust_angle interface
			#Socket Curve
			curve_socket = _curve_ends_adjust_angle.interface.new_socket(name = "Curve", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			curve_socket.attribute_domain = 'POINT'
			
			#Socket Curve
			curve_socket_1 = _curve_ends_adjust_angle.interface.new_socket(name = "Curve", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			curve_socket_1.attribute_domain = 'POINT'
			
			#Socket Distance
			distance_socket = _curve_ends_adjust_angle.interface.new_socket(name = "Distance", in_out='INPUT', socket_type = 'NodeSocketFloat')
			distance_socket.default_value = 3.0
			distance_socket.min_value = -10000.0
			distance_socket.max_value = 10000.0
			distance_socket.subtype = 'NONE'
			distance_socket.attribute_domain = 'POINT'
			
			#Socket Distance
			distance_socket_1 = _curve_ends_adjust_angle.interface.new_socket(name = "Distance", in_out='INPUT', socket_type = 'NodeSocketFloat')
			distance_socket_1.default_value = 0.4200000762939453
			distance_socket_1.min_value = -10000.0
			distance_socket_1.max_value = 10000.0
			distance_socket_1.subtype = 'NONE'
			distance_socket_1.attribute_domain = 'POINT'
			
			
			#initialize _curve_ends_adjust_angle nodes
			#node Vector Math.001
			vector_math_001 = _curve_ends_adjust_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_001.name = "Vector Math.001"
			vector_math_001.operation = 'SCALE'
			
			#node Set Spline Type.001
			set_spline_type_001 = _curve_ends_adjust_angle.nodes.new("GeometryNodeCurveSplineType")
			set_spline_type_001.name = "Set Spline Type.001"
			set_spline_type_001.spline_type = 'BEZIER'
			#Selection
			set_spline_type_001.inputs[1].default_value = True
			
			#node Boolean Math.003
			boolean_math_003 = _curve_ends_adjust_angle.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003.name = "Boolean Math.003"
			boolean_math_003.operation = 'AND'
			
			#node Reroute.001
			reroute_001 = _curve_ends_adjust_angle.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			#node Endpoint Selection.006
			endpoint_selection_006 = _curve_ends_adjust_angle.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_006.name = "Endpoint Selection.006"
			#Start Size
			endpoint_selection_006.inputs[0].default_value = 1
			#End Size
			endpoint_selection_006.inputs[1].default_value = 0
			
			#node Boolean Math.004
			boolean_math_004 = _curve_ends_adjust_angle.nodes.new("FunctionNodeBooleanMath")
			boolean_math_004.name = "Boolean Math.004"
			boolean_math_004.operation = 'AND'
			
			#node Vector Math.011
			vector_math_011 = _curve_ends_adjust_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_011.name = "Vector Math.011"
			vector_math_011.operation = 'SCALE'
			
			#node Vector Math.013
			vector_math_013 = _curve_ends_adjust_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_013.name = "Vector Math.013"
			vector_math_013.operation = 'NORMALIZE'
			
			#node Group
			group_2 = _curve_ends_adjust_angle.nodes.new("GeometryNodeGroup")
			group_2.name = "Group"
			group_2.node_tree = mn_units
			
			#node Vector Math.007
			vector_math_007 = _curve_ends_adjust_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_007.name = "Vector Math.007"
			vector_math_007.operation = 'SUBTRACT'
			
			#node Vector Math.012
			vector_math_012 = _curve_ends_adjust_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_012.name = "Vector Math.012"
			vector_math_012.operation = 'NORMALIZE'
			
			#node Named Attribute
			named_attribute = _curve_ends_adjust_angle.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute.inputs[0].default_value = "forward"
			
			#node Position
			position = _curve_ends_adjust_angle.nodes.new("GeometryNodeInputPosition")
			position.name = "Position"
			
			#node Vector Math
			vector_math = _curve_ends_adjust_angle.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.operation = 'SUBTRACT'
			
			#node Vector Math.002
			vector_math_002 = _curve_ends_adjust_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_002.name = "Vector Math.002"
			vector_math_002.hide = True
			vector_math_002.operation = 'NORMALIZE'
			
			#node Group.001
			group_001_1 = _curve_ends_adjust_angle.nodes.new("GeometryNodeGroup")
			group_001_1.name = "Group.001"
			group_001_1.node_tree = mn_units
			#Input_1
			group_001_1.inputs[0].default_value = -2.0
			
			#node Vector Math.003
			vector_math_003 = _curve_ends_adjust_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_003.name = "Vector Math.003"
			vector_math_003.operation = 'SCALE'
			
			#node Group.009
			group_009 = _curve_ends_adjust_angle.nodes.new("GeometryNodeGroup")
			group_009.name = "Group.009"
			group_009.node_tree = _field_offset_vec
			#Input_1
			group_009.inputs[1].default_value = 1
			
			#node Vector Math.010
			vector_math_010 = _curve_ends_adjust_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_010.name = "Vector Math.010"
			vector_math_010.operation = 'SUBTRACT'
			
			#node Reroute
			reroute = _curve_ends_adjust_angle.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Named Attribute.001
			named_attribute_001 = _curve_ends_adjust_angle.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_001.inputs[0].default_value = "reverse"
			
			#node Position.001
			position_001 = _curve_ends_adjust_angle.nodes.new("GeometryNodeInputPosition")
			position_001.name = "Position.001"
			
			#node Vector Math.004
			vector_math_004 = _curve_ends_adjust_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_004.name = "Vector Math.004"
			vector_math_004.operation = 'SUBTRACT'
			
			#node Vector Math.005
			vector_math_005 = _curve_ends_adjust_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_005.name = "Vector Math.005"
			vector_math_005.hide = True
			vector_math_005.operation = 'NORMALIZE'
			
			#node Group.002
			group_002_1 = _curve_ends_adjust_angle.nodes.new("GeometryNodeGroup")
			group_002_1.name = "Group.002"
			group_002_1.node_tree = mn_units
			#Input_1
			group_002_1.inputs[0].default_value = -2.0
			
			#node Vector Math.006
			vector_math_006 = _curve_ends_adjust_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_006.name = "Vector Math.006"
			vector_math_006.operation = 'SCALE'
			
			#node Group Output
			group_output_8 = _curve_ends_adjust_angle.nodes.new("NodeGroupOutput")
			group_output_8.name = "Group Output"
			group_output_8.is_active_output = True
			
			#node Set Position
			set_position = _curve_ends_adjust_angle.nodes.new("GeometryNodeSetPosition")
			set_position.name = "Set Position"
			#Position
			set_position.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Endpoint Selection.008
			endpoint_selection_008 = _curve_ends_adjust_angle.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_008.name = "Endpoint Selection.008"
			#Start Size
			endpoint_selection_008.inputs[0].default_value = 0
			#End Size
			endpoint_selection_008.inputs[1].default_value = 1
			
			#node Group.003
			group_003 = _curve_ends_adjust_angle.nodes.new("GeometryNodeGroup")
			group_003.name = "Group.003"
			group_003.node_tree = _field_offset_vec
			#Input_1
			group_003.inputs[1].default_value = -1
			
			#node Group.019
			group_019 = _curve_ends_adjust_angle.nodes.new("GeometryNodeGroup")
			group_019.name = "Group.019"
			group_019.node_tree = _mn_select_sec_struct
			#Socket_1
			group_019.inputs[0].default_value = True
			
			#node Curve Handle Positions
			curve_handle_positions = _curve_ends_adjust_angle.nodes.new("GeometryNodeInputCurveHandlePositions")
			curve_handle_positions.name = "Curve Handle Positions"
			#Relative
			curve_handle_positions.inputs[0].default_value = False
			
			#node Vector Math.008
			vector_math_008 = _curve_ends_adjust_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_008.name = "Vector Math.008"
			vector_math_008.operation = 'NORMALIZE'
			
			#node Vector Math.009
			vector_math_009 = _curve_ends_adjust_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_009.name = "Vector Math.009"
			vector_math_009.operation = 'SCALE'
			
			#node Endpoint Selection.009
			endpoint_selection_009 = _curve_ends_adjust_angle.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_009.name = "Endpoint Selection.009"
			#Start Size
			endpoint_selection_009.inputs[0].default_value = 1
			#End Size
			endpoint_selection_009.inputs[1].default_value = 1
			
			#node Switch
			switch = _curve_ends_adjust_angle.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'VECTOR'
			
			#node Group.004
			group_004 = _curve_ends_adjust_angle.nodes.new("GeometryNodeGroup")
			group_004.name = "Group.004"
			group_004.node_tree = mn_units
			
			#node Curve Handle Positions.001
			curve_handle_positions_001 = _curve_ends_adjust_angle.nodes.new("GeometryNodeInputCurveHandlePositions")
			curve_handle_positions_001.name = "Curve Handle Positions.001"
			#Relative
			curve_handle_positions_001.inputs[0].default_value = True
			
			#node Endpoint Selection.010
			endpoint_selection_010 = _curve_ends_adjust_angle.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_010.name = "Endpoint Selection.010"
			#Start Size
			endpoint_selection_010.inputs[0].default_value = 0
			#End Size
			endpoint_selection_010.inputs[1].default_value = 1
			
			#node Set Handle Positions.001
			set_handle_positions_001 = _curve_ends_adjust_angle.nodes.new("GeometryNodeSetCurveHandlePositions")
			set_handle_positions_001.name = "Set Handle Positions.001"
			set_handle_positions_001.mode = 'LEFT'
			#Position
			set_handle_positions_001.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Set Handle Positions
			set_handle_positions = _curve_ends_adjust_angle.nodes.new("GeometryNodeSetCurveHandlePositions")
			set_handle_positions.name = "Set Handle Positions"
			set_handle_positions.mode = 'RIGHT'
			#Position
			set_handle_positions.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Group Input
			group_input_8 = _curve_ends_adjust_angle.nodes.new("NodeGroupInput")
			group_input_8.name = "Group Input"
			
			
			
			
			#Set locations
			vector_math_001.location = (-113.090576171875, -30.316802978515625)
			set_spline_type_001.location = (-457.7088623046875, 134.57489013671875)
			boolean_math_003.location = (-393.090576171875, 294.3201599121094)
			reroute_001.location = (-440.0, -200.0)
			endpoint_selection_006.location = (-620.0, 280.0)
			boolean_math_004.location = (340.0, 380.0)
			vector_math_011.location = (400.0, 80.0)
			vector_math_013.location = (220.0, 80.0)
			group_2.location = (-780.0, 80.0)
			vector_math_007.location = (-300.0, -80.0)
			vector_math_012.location = (-320.0, 40.0)
			named_attribute.location = (-1020.0, -80.0)
			position.location = (-1020.0, -220.0)
			vector_math.location = (-860.0, -140.0)
			vector_math_002.location = (-860.0, -100.0)
			group_001_1.location = (-1020.0, -280.0)
			vector_math_003.location = (-700.0, -100.0)
			group_009.location = (71.90267944335938, -263.45281982421875)
			vector_math_010.location = (71.90267944335938, -103.45283508300781)
			reroute.location = (-35.006744384765625, -353.1360168457031)
			named_attribute_001.location = (311.4145812988281, -130.00930786132812)
			position_001.location = (311.4145812988281, -270.0093688964844)
			vector_math_004.location = (471.4145812988281, -190.00936889648438)
			vector_math_005.location = (471.4145812988281, -150.00930786132812)
			group_002_1.location = (311.4145812988281, -330.0093688964844)
			vector_math_006.location = (631.41455078125, -150.00930786132812)
			group_output_8.location = (1649.9193115234375, 169.1092529296875)
			set_position.location = (1430.0023193359375, 203.44369506835938)
			endpoint_selection_008.location = (180.0, 400.0)
			group_003.location = (-300.0, -240.0)
			group_019.location = (-620.0, 440.0)
			curve_handle_positions.location = (-780.0, -320.0)
			vector_math_008.location = (1330.0, -120.0)
			vector_math_009.location = (1330.0, 20.0)
			endpoint_selection_009.location = (969.6704711914062, 303.7537841796875)
			switch.location = (1110.0, -124.58650970458984)
			group_004.location = (1120.0, 0.0)
			curve_handle_positions_001.location = (900.0, -200.0)
			endpoint_selection_010.location = (900.0, -80.0)
			set_handle_positions_001.location = (566.909423828125, 249.68319702148438)
			set_handle_positions.location = (-153.090576171875, 229.68319702148438)
			group_input_8.location = (-1054.2796630859375, 148.32730102539062)
			
			#Set dimensions
			vector_math_001.width, vector_math_001.height = 140.0, 100.0
			set_spline_type_001.width, set_spline_type_001.height = 140.0, 100.0
			boolean_math_003.width, boolean_math_003.height = 140.0, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			endpoint_selection_006.width, endpoint_selection_006.height = 140.0, 100.0
			boolean_math_004.width, boolean_math_004.height = 140.0, 100.0
			vector_math_011.width, vector_math_011.height = 140.0, 100.0
			vector_math_013.width, vector_math_013.height = 140.0, 100.0
			group_2.width, group_2.height = 140.0, 100.0
			vector_math_007.width, vector_math_007.height = 140.0, 100.0
			vector_math_012.width, vector_math_012.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			position.width, position.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			vector_math_002.width, vector_math_002.height = 140.0, 100.0
			group_001_1.width, group_001_1.height = 140.0, 100.0
			vector_math_003.width, vector_math_003.height = 140.0, 100.0
			group_009.width, group_009.height = 148.385009765625, 100.0
			vector_math_010.width, vector_math_010.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
			position_001.width, position_001.height = 140.0, 100.0
			vector_math_004.width, vector_math_004.height = 140.0, 100.0
			vector_math_005.width, vector_math_005.height = 140.0, 100.0
			group_002_1.width, group_002_1.height = 140.0, 100.0
			vector_math_006.width, vector_math_006.height = 140.0, 100.0
			group_output_8.width, group_output_8.height = 140.0, 100.0
			set_position.width, set_position.height = 140.0, 100.0
			endpoint_selection_008.width, endpoint_selection_008.height = 140.0, 100.0
			group_003.width, group_003.height = 148.385009765625, 100.0
			group_019.width, group_019.height = 158.9053955078125, 100.0
			curve_handle_positions.width, curve_handle_positions.height = 150.0, 100.0
			vector_math_008.width, vector_math_008.height = 140.0, 100.0
			vector_math_009.width, vector_math_009.height = 140.0, 100.0
			endpoint_selection_009.width, endpoint_selection_009.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			group_004.width, group_004.height = 140.0, 100.0
			curve_handle_positions_001.width, curve_handle_positions_001.height = 150.0, 100.0
			endpoint_selection_010.width, endpoint_selection_010.height = 140.0, 100.0
			set_handle_positions_001.width, set_handle_positions_001.height = 140.0, 100.0
			set_handle_positions.width, set_handle_positions.height = 140.0, 100.0
			group_input_8.width, group_input_8.height = 140.0, 100.0
			
			#initialize _curve_ends_adjust_angle links
			#reroute_001.Output -> vector_math_007.Vector
			_curve_ends_adjust_angle.links.new(reroute_001.outputs[0], vector_math_007.inputs[0])
			#reroute_001.Output -> group_003.Field
			_curve_ends_adjust_angle.links.new(reroute_001.outputs[0], group_003.inputs[0])
			#group_019.Is Structured -> boolean_math_003.Boolean
			_curve_ends_adjust_angle.links.new(group_019.outputs[2], boolean_math_003.inputs[1])
			#boolean_math_003.Boolean -> set_handle_positions.Selection
			_curve_ends_adjust_angle.links.new(boolean_math_003.outputs[0], set_handle_positions.inputs[1])
			#group_019.Is Structured -> boolean_math_004.Boolean
			_curve_ends_adjust_angle.links.new(group_019.outputs[2], boolean_math_004.inputs[1])
			#set_spline_type_001.Curve -> set_handle_positions.Curve
			_curve_ends_adjust_angle.links.new(set_spline_type_001.outputs[0], set_handle_positions.inputs[0])
			#vector_math_010.Vector -> vector_math_013.Vector
			_curve_ends_adjust_angle.links.new(vector_math_010.outputs[0], vector_math_013.inputs[0])
			#endpoint_selection_006.Selection -> boolean_math_003.Boolean
			_curve_ends_adjust_angle.links.new(endpoint_selection_006.outputs[0], boolean_math_003.inputs[0])
			#reroute.Output -> group_009.Field
			_curve_ends_adjust_angle.links.new(reroute.outputs[0], group_009.inputs[0])
			#vector_math_007.Vector -> vector_math_012.Vector
			_curve_ends_adjust_angle.links.new(vector_math_007.outputs[0], vector_math_012.inputs[0])
			#endpoint_selection_008.Selection -> boolean_math_004.Boolean
			_curve_ends_adjust_angle.links.new(endpoint_selection_008.outputs[0], boolean_math_004.inputs[0])
			#group_2.Angstrom -> vector_math_011.Scale
			_curve_ends_adjust_angle.links.new(group_2.outputs[0], vector_math_011.inputs[3])
			#reroute.Output -> vector_math_010.Vector
			_curve_ends_adjust_angle.links.new(reroute.outputs[0], vector_math_010.inputs[0])
			#vector_math_013.Vector -> vector_math_011.Vector
			_curve_ends_adjust_angle.links.new(vector_math_013.outputs[0], vector_math_011.inputs[0])
			#group_009.Field -> vector_math_010.Vector
			_curve_ends_adjust_angle.links.new(group_009.outputs[0], vector_math_010.inputs[1])
			#vector_math_012.Vector -> vector_math_001.Vector
			_curve_ends_adjust_angle.links.new(vector_math_012.outputs[0], vector_math_001.inputs[0])
			#set_handle_positions.Curve -> set_handle_positions_001.Curve
			_curve_ends_adjust_angle.links.new(set_handle_positions.outputs[0], set_handle_positions_001.inputs[0])
			#group_003.Field -> vector_math_007.Vector
			_curve_ends_adjust_angle.links.new(group_003.outputs[0], vector_math_007.inputs[1])
			#boolean_math_004.Boolean -> set_handle_positions_001.Selection
			_curve_ends_adjust_angle.links.new(boolean_math_004.outputs[0], set_handle_positions_001.inputs[1])
			#group_2.Angstrom -> vector_math_001.Scale
			_curve_ends_adjust_angle.links.new(group_2.outputs[0], vector_math_001.inputs[3])
			#group_input_8.Curve -> set_spline_type_001.Curve
			_curve_ends_adjust_angle.links.new(group_input_8.outputs[0], set_spline_type_001.inputs[0])
			#set_position.Geometry -> group_output_8.Curve
			_curve_ends_adjust_angle.links.new(set_position.outputs[0], group_output_8.inputs[0])
			#group_input_8.Distance -> group_2.Value
			_curve_ends_adjust_angle.links.new(group_input_8.outputs[1], group_2.inputs[0])
			#curve_handle_positions.Right -> reroute.Input
			_curve_ends_adjust_angle.links.new(curve_handle_positions.outputs[1], reroute.inputs[0])
			#curve_handle_positions.Left -> reroute_001.Input
			_curve_ends_adjust_angle.links.new(curve_handle_positions.outputs[0], reroute_001.inputs[0])
			#named_attribute.Attribute -> vector_math.Vector
			_curve_ends_adjust_angle.links.new(named_attribute.outputs[0], vector_math.inputs[0])
			#position.Position -> vector_math.Vector
			_curve_ends_adjust_angle.links.new(position.outputs[0], vector_math.inputs[1])
			#vector_math.Vector -> vector_math_002.Vector
			_curve_ends_adjust_angle.links.new(vector_math.outputs[0], vector_math_002.inputs[0])
			#vector_math_002.Vector -> vector_math_003.Vector
			_curve_ends_adjust_angle.links.new(vector_math_002.outputs[0], vector_math_003.inputs[0])
			#group_001_1.Angstrom -> vector_math_003.Scale
			_curve_ends_adjust_angle.links.new(group_001_1.outputs[0], vector_math_003.inputs[3])
			#vector_math_003.Vector -> set_handle_positions.Offset
			_curve_ends_adjust_angle.links.new(vector_math_003.outputs[0], set_handle_positions.inputs[3])
			#named_attribute_001.Attribute -> vector_math_004.Vector
			_curve_ends_adjust_angle.links.new(named_attribute_001.outputs[0], vector_math_004.inputs[0])
			#position_001.Position -> vector_math_004.Vector
			_curve_ends_adjust_angle.links.new(position_001.outputs[0], vector_math_004.inputs[1])
			#vector_math_004.Vector -> vector_math_005.Vector
			_curve_ends_adjust_angle.links.new(vector_math_004.outputs[0], vector_math_005.inputs[0])
			#vector_math_005.Vector -> vector_math_006.Vector
			_curve_ends_adjust_angle.links.new(vector_math_005.outputs[0], vector_math_006.inputs[0])
			#group_002_1.Angstrom -> vector_math_006.Scale
			_curve_ends_adjust_angle.links.new(group_002_1.outputs[0], vector_math_006.inputs[3])
			#vector_math_006.Vector -> set_handle_positions_001.Offset
			_curve_ends_adjust_angle.links.new(vector_math_006.outputs[0], set_handle_positions_001.inputs[3])
			#set_handle_positions_001.Curve -> set_position.Geometry
			_curve_ends_adjust_angle.links.new(set_handle_positions_001.outputs[0], set_position.inputs[0])
			#endpoint_selection_009.Selection -> set_position.Selection
			_curve_ends_adjust_angle.links.new(endpoint_selection_009.outputs[0], set_position.inputs[1])
			#vector_math_008.Vector -> vector_math_009.Vector
			_curve_ends_adjust_angle.links.new(vector_math_008.outputs[0], vector_math_009.inputs[0])
			#group_004.Angstrom -> vector_math_009.Scale
			_curve_ends_adjust_angle.links.new(group_004.outputs[0], vector_math_009.inputs[3])
			#vector_math_009.Vector -> set_position.Offset
			_curve_ends_adjust_angle.links.new(vector_math_009.outputs[0], set_position.inputs[3])
			#curve_handle_positions_001.Left -> switch.False
			_curve_ends_adjust_angle.links.new(curve_handle_positions_001.outputs[0], switch.inputs[1])
			#switch.Output -> vector_math_008.Vector
			_curve_ends_adjust_angle.links.new(switch.outputs[0], vector_math_008.inputs[0])
			#curve_handle_positions_001.Right -> switch.True
			_curve_ends_adjust_angle.links.new(curve_handle_positions_001.outputs[1], switch.inputs[2])
			#endpoint_selection_010.Selection -> switch.Switch
			_curve_ends_adjust_angle.links.new(endpoint_selection_010.outputs[0], switch.inputs[0])
			#group_input_8.Distance -> group_004.Value
			_curve_ends_adjust_angle.links.new(group_input_8.outputs[2], group_004.inputs[0])
			return _curve_ends_adjust_angle

		_curve_ends_adjust_angle = _curve_ends_adjust_angle_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".curve_ends_adjust_angle", type = 'NODES')
		mod.node_group = _curve_ends_adjust_angle
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_curve_ends_adjust_angle.bl_idname)
			
def register():
	bpy.utils.register_class(_curve_ends_adjust_angle)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_curve_ends_adjust_angle)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
