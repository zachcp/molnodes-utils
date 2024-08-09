bl_info = {
	"name" : ".MN_utils_style_cartoon",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _MN_utils_style_cartoon(bpy.types.Operator):
	bl_idname = "node._mn_utils_style_cartoon"
	bl_label = ".MN_utils_style_cartoon"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _guide_rotation node group
		def _guide_rotation_node_group():
			_guide_rotation = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".guide_rotation")

			_guide_rotation.color_tag = 'NONE'
			_guide_rotation.description = ""

			
			#_guide_rotation interface
			#Socket Rotation
			rotation_socket = _guide_rotation.interface.new_socket(name = "Rotation", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			rotation_socket.subtype = 'EULER'
			rotation_socket.default_value = (0.0, 0.0, 0.0)
			rotation_socket.min_value = -3.4028234663852886e+38
			rotation_socket.max_value = 3.4028234663852886e+38
			rotation_socket.attribute_domain = 'POINT'
			
			#Socket Angle
			angle_socket = _guide_rotation.interface.new_socket(name = "Angle", in_out='INPUT', socket_type = 'NodeSocketFloat')
			angle_socket.subtype = 'ANGLE'
			angle_socket.default_value = 0.0
			angle_socket.min_value = -3.4028234663852886e+38
			angle_socket.max_value = 3.4028234663852886e+38
			angle_socket.attribute_domain = 'POINT'
			
			
			#initialize _guide_rotation nodes
			#node Align Euler to Vector.001
			align_euler_to_vector_001 = _guide_rotation.nodes.new("FunctionNodeAlignEulerToVector")
			align_euler_to_vector_001.name = "Align Euler to Vector.001"
			align_euler_to_vector_001.axis = 'X'
			align_euler_to_vector_001.pivot_axis = 'Z'
			#Factor
			align_euler_to_vector_001.inputs[1].default_value = 1.0
			
			#node Rotate Euler
			rotate_euler = _guide_rotation.nodes.new("FunctionNodeRotateEuler")
			rotate_euler.name = "Rotate Euler"
			rotate_euler.rotation_type = 'AXIS_ANGLE'
			rotate_euler.space = 'OBJECT'
			
			#node Align Euler to Vector
			align_euler_to_vector = _guide_rotation.nodes.new("FunctionNodeAlignEulerToVector")
			align_euler_to_vector.name = "Align Euler to Vector"
			align_euler_to_vector.axis = 'Z'
			align_euler_to_vector.pivot_axis = 'AUTO'
			#Rotation
			align_euler_to_vector.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Factor
			align_euler_to_vector.inputs[1].default_value = 1.0
			
			#node Group Output
			group_output = _guide_rotation.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Reroute
			reroute = _guide_rotation.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Named Attribute.001
			named_attribute_001 = _guide_rotation.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_001.inputs[0].default_value = "guide_X"
			
			#node Named Attribute
			named_attribute = _guide_rotation.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute.inputs[0].default_value = "guide_Z"
			
			#node Group Input.001
			group_input_001 = _guide_rotation.nodes.new("NodeGroupInput")
			group_input_001.name = "Group Input.001"
			
			
			
			
			#Set locations
			align_euler_to_vector_001.location = (177.053955078125, 186.16505432128906)
			rotate_euler.location = (356.9603271484375, 191.41680908203125)
			align_euler_to_vector.location = (20.0, 180.0)
			group_output.location = (540.0, 180.0)
			reroute.location = (140.0, -40.0)
			named_attribute_001.location = (-180.0, 40.0)
			named_attribute.location = (-180.0, 180.0)
			group_input_001.location = (180.0, -40.0)
			
			#Set dimensions
			align_euler_to_vector_001.width, align_euler_to_vector_001.height = 140.0, 100.0
			rotate_euler.width, rotate_euler.height = 140.0, 100.0
			align_euler_to_vector.width, align_euler_to_vector.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			named_attribute_001.width, named_attribute_001.height = 145.799072265625, 100.0
			named_attribute.width, named_attribute.height = 146.58917236328125, 100.0
			group_input_001.width, group_input_001.height = 140.0, 100.0
			
			#initialize _guide_rotation links
			#reroute.Output -> align_euler_to_vector_001.Vector
			_guide_rotation.links.new(reroute.outputs[0], align_euler_to_vector_001.inputs[2])
			#align_euler_to_vector.Rotation -> align_euler_to_vector_001.Rotation
			_guide_rotation.links.new(align_euler_to_vector.outputs[0], align_euler_to_vector_001.inputs[0])
			#rotate_euler.Rotation -> group_output.Rotation
			_guide_rotation.links.new(rotate_euler.outputs[0], group_output.inputs[0])
			#align_euler_to_vector_001.Rotation -> rotate_euler.Rotation
			_guide_rotation.links.new(align_euler_to_vector_001.outputs[0], rotate_euler.inputs[0])
			#group_input_001.Angle -> rotate_euler.Angle
			_guide_rotation.links.new(group_input_001.outputs[0], rotate_euler.inputs[3])
			#named_attribute.Attribute -> align_euler_to_vector.Vector
			_guide_rotation.links.new(named_attribute.outputs[0], align_euler_to_vector.inputs[2])
			#reroute.Output -> rotate_euler.Axis
			_guide_rotation.links.new(reroute.outputs[0], rotate_euler.inputs[2])
			#named_attribute_001.Attribute -> reroute.Input
			_guide_rotation.links.new(named_attribute_001.outputs[0], reroute.inputs[0])
			return _guide_rotation

		_guide_rotation = _guide_rotation_node_group()

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
			group_input = _mn_select_sec_struct_id.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
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
			group_input.location = (80.0, 100.0)
			boolean_math_001.location = (579.9999389648438, 196.54164123535156)
			boolean_math_002.location = (580.0, 60.0)
			
			#Set dimensions
			named_attribute_002.width, named_attribute_002.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			group_output_1.width, group_output_1.height = 140.0, 100.0
			compare_012.width, compare_012.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
			boolean_math_002.width, boolean_math_002.height = 140.0, 100.0
			
			#initialize _mn_select_sec_struct_id links
			#boolean_math_001.Boolean -> group_output_1.Selection
			_mn_select_sec_struct_id.links.new(boolean_math_001.outputs[0], group_output_1.inputs[0])
			#compare_012.Result -> boolean_math.Boolean
			_mn_select_sec_struct_id.links.new(compare_012.outputs[0], boolean_math.inputs[1])
			#group_input.id -> compare_012.A
			_mn_select_sec_struct_id.links.new(group_input.outputs[2], compare_012.inputs[2])
			#group_input.And -> boolean_math.Boolean
			_mn_select_sec_struct_id.links.new(group_input.outputs[0], boolean_math.inputs[0])
			#named_attribute_002.Attribute -> compare_012.B
			_mn_select_sec_struct_id.links.new(named_attribute_002.outputs[0], compare_012.inputs[3])
			#boolean_math.Boolean -> boolean_math_001.Boolean
			_mn_select_sec_struct_id.links.new(boolean_math.outputs[0], boolean_math_001.inputs[0])
			#group_input.Or -> boolean_math_001.Boolean
			_mn_select_sec_struct_id.links.new(group_input.outputs[1], boolean_math_001.inputs[1])
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
			group_input_1 = is_sheet.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			
			#node MN_select_sec_struct.002
			mn_select_sec_struct_002 = is_sheet.nodes.new("GeometryNodeGroup")
			mn_select_sec_struct_002.label = "Select Sec Struct"
			mn_select_sec_struct_002.name = "MN_select_sec_struct.002"
			mn_select_sec_struct_002.node_tree = _mn_select_sec_struct_id
			#Socket_1
			mn_select_sec_struct_002.inputs[2].default_value = 2
			
			
			
			
			#Set locations
			group_output_2.location = (267.00146484375, 0.0)
			group_input_1.location = (-220.0, -80.0)
			mn_select_sec_struct_002.location = (0.0, 0.0)
			
			#Set dimensions
			group_output_2.width, group_output_2.height = 140.0, 100.0
			group_input_1.width, group_input_1.height = 140.0, 100.0
			mn_select_sec_struct_002.width, mn_select_sec_struct_002.height = 217.00146484375, 100.0
			
			#initialize is_sheet links
			#mn_select_sec_struct_002.Selection -> group_output_2.Selection
			is_sheet.links.new(mn_select_sec_struct_002.outputs[0], group_output_2.inputs[0])
			#group_input_1.And -> mn_select_sec_struct_002.And
			is_sheet.links.new(group_input_1.outputs[0], mn_select_sec_struct_002.inputs[0])
			#group_input_1.Or -> mn_select_sec_struct_002.Or
			is_sheet.links.new(group_input_1.outputs[1], mn_select_sec_struct_002.inputs[1])
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
			group_input_2 = is_loop.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
			#node MN_select_sec_struct.002
			mn_select_sec_struct_002_1 = is_loop.nodes.new("GeometryNodeGroup")
			mn_select_sec_struct_002_1.label = "Select Sec Struct"
			mn_select_sec_struct_002_1.name = "MN_select_sec_struct.002"
			mn_select_sec_struct_002_1.node_tree = _mn_select_sec_struct_id
			#Socket_1
			mn_select_sec_struct_002_1.inputs[2].default_value = 3
			
			
			
			
			#Set locations
			group_output_3.location = (267.00146484375, 0.0)
			group_input_2.location = (-200.0, 0.0)
			mn_select_sec_struct_002_1.location = (0.0, 0.0)
			
			#Set dimensions
			group_output_3.width, group_output_3.height = 140.0, 100.0
			group_input_2.width, group_input_2.height = 140.0, 100.0
			mn_select_sec_struct_002_1.width, mn_select_sec_struct_002_1.height = 217.00146484375, 100.0
			
			#initialize is_loop links
			#mn_select_sec_struct_002_1.Selection -> group_output_3.Selection
			is_loop.links.new(mn_select_sec_struct_002_1.outputs[0], group_output_3.inputs[0])
			#group_input_2.And -> mn_select_sec_struct_002_1.And
			is_loop.links.new(group_input_2.outputs[0], mn_select_sec_struct_002_1.inputs[0])
			#group_input_2.Or -> mn_select_sec_struct_002_1.Or
			is_loop.links.new(group_input_2.outputs[1], mn_select_sec_struct_002_1.inputs[1])
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
			group_input_3 = is_helix.nodes.new("NodeGroupInput")
			group_input_3.name = "Group Input"
			
			#node MN_select_sec_struct.002
			mn_select_sec_struct_002_2 = is_helix.nodes.new("GeometryNodeGroup")
			mn_select_sec_struct_002_2.label = "Select Sec Struct"
			mn_select_sec_struct_002_2.name = "MN_select_sec_struct.002"
			mn_select_sec_struct_002_2.node_tree = _mn_select_sec_struct_id
			#Socket_1
			mn_select_sec_struct_002_2.inputs[2].default_value = 1
			
			
			
			
			#Set locations
			group_output_4.location = (267.00146484375, 0.0)
			group_input_3.location = (-200.0, 0.0)
			mn_select_sec_struct_002_2.location = (0.0, 0.0)
			
			#Set dimensions
			group_output_4.width, group_output_4.height = 140.0, 100.0
			group_input_3.width, group_input_3.height = 140.0, 100.0
			mn_select_sec_struct_002_2.width, mn_select_sec_struct_002_2.height = 217.00146484375, 100.0
			
			#initialize is_helix links
			#mn_select_sec_struct_002_2.Selection -> group_output_4.Selection
			is_helix.links.new(mn_select_sec_struct_002_2.outputs[0], group_output_4.inputs[0])
			#group_input_3.And -> mn_select_sec_struct_002_2.And
			is_helix.links.new(group_input_3.outputs[0], mn_select_sec_struct_002_2.inputs[0])
			#group_input_3.Or -> mn_select_sec_struct_002_2.Or
			is_helix.links.new(group_input_3.outputs[1], mn_select_sec_struct_002_2.inputs[1])
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
			group_input_4 = _mn_select_sec_struct.nodes.new("NodeGroupInput")
			group_input_4.name = "Group Input"
			group_input_4.outputs[1].hide = True
			
			
			
			
			#Set locations
			group_001.location = (120.0, -60.0)
			group_002.location = (120.0, -180.0)
			group.location = (120.0, 60.0)
			boolean_math_001_1.location = (300.0, -140.0)
			group_output_5.location = (540.0, -60.0)
			group_input_4.location = (-160.0, -40.0)
			
			#Set dimensions
			group_001.width, group_001.height = 140.0, 100.0
			group_002.width, group_002.height = 140.0, 100.0
			group.width, group.height = 140.0, 100.0
			boolean_math_001_1.width, boolean_math_001_1.height = 140.0, 100.0
			group_output_5.width, group_output_5.height = 140.0, 100.0
			group_input_4.width, group_input_4.height = 140.0, 100.0
			
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
			#group_input_4.And -> group.And
			_mn_select_sec_struct.links.new(group_input_4.outputs[0], group.inputs[0])
			#group_input_4.And -> group_001.And
			_mn_select_sec_struct.links.new(group_input_4.outputs[0], group_001.inputs[0])
			#group_input_4.And -> group_002.And
			_mn_select_sec_struct.links.new(group_input_4.outputs[0], group_002.inputs[0])
			return _mn_select_sec_struct

		_mn_select_sec_struct = _mn_select_sec_struct_node_group()

		#initialize _debug_arrows node group
		def _debug_arrows_node_group():
			_debug_arrows = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".DEBUG_arrows")

			_debug_arrows.color_tag = 'NONE'
			_debug_arrows.description = ""

			_debug_arrows.is_modifier = True
			
			#_debug_arrows interface
			#Socket Instances
			instances_socket = _debug_arrows.interface.new_socket(name = "Instances", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			instances_socket.attribute_domain = 'POINT'
			
			#Socket Points
			points_socket = _debug_arrows.interface.new_socket(name = "Points", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			points_socket.attribute_domain = 'POINT'
			
			#Socket Position
			position_socket = _debug_arrows.interface.new_socket(name = "Position", in_out='INPUT', socket_type = 'NodeSocketVector')
			position_socket.subtype = 'NONE'
			position_socket.default_value = (0.0, 0.0, 0.0)
			position_socket.min_value = -3.4028234663852886e+38
			position_socket.max_value = 3.4028234663852886e+38
			position_socket.attribute_domain = 'POINT'
			position_socket.hide_value = True
			
			#Socket Offset
			offset_socket = _debug_arrows.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketVector')
			offset_socket.subtype = 'TRANSLATION'
			offset_socket.default_value = (0.0, 0.0, 0.0)
			offset_socket.min_value = -3.4028234663852886e+38
			offset_socket.max_value = 3.4028234663852886e+38
			offset_socket.attribute_domain = 'POINT'
			
			#Socket Rotation
			rotation_socket_1 = _debug_arrows.interface.new_socket(name = "Rotation", in_out='INPUT', socket_type = 'NodeSocketVector')
			rotation_socket_1.subtype = 'EULER'
			rotation_socket_1.default_value = (0.0, 0.0, 0.0)
			rotation_socket_1.min_value = -3.4028234663852886e+38
			rotation_socket_1.max_value = 3.4028234663852886e+38
			rotation_socket_1.attribute_domain = 'POINT'
			
			#Socket Scale
			scale_socket = _debug_arrows.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketVector')
			scale_socket.subtype = 'XYZ'
			scale_socket.default_value = (0.33000001311302185, 0.36000001430511475, 0.75)
			scale_socket.min_value = -3.4028234663852886e+38
			scale_socket.max_value = 3.4028234663852886e+38
			scale_socket.attribute_domain = 'POINT'
			
			
			#initialize _debug_arrows nodes
			#node Group Output
			group_output_6 = _debug_arrows.nodes.new("NodeGroupOutput")
			group_output_6.name = "Group Output"
			group_output_6.is_active_output = True
			
			#node Instance on Points.002
			instance_on_points_002 = _debug_arrows.nodes.new("GeometryNodeInstanceOnPoints")
			instance_on_points_002.name = "Instance on Points.002"
			#Selection
			instance_on_points_002.inputs[1].default_value = True
			#Pick Instance
			instance_on_points_002.inputs[3].default_value = False
			#Instance Index
			instance_on_points_002.inputs[4].default_value = 0
			
			#node Reroute.003
			reroute_003 = _debug_arrows.nodes.new("NodeReroute")
			reroute_003.name = "Reroute.003"
			#node Reroute.009
			reroute_009 = _debug_arrows.nodes.new("NodeReroute")
			reroute_009.name = "Reroute.009"
			#node Join Geometry.001
			join_geometry_001 = _debug_arrows.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_001.name = "Join Geometry.001"
			join_geometry_001.hide = True
			
			#node Transform Geometry.002
			transform_geometry_002 = _debug_arrows.nodes.new("GeometryNodeTransform")
			transform_geometry_002.name = "Transform Geometry.002"
			transform_geometry_002.mode = 'COMPONENTS'
			#Rotation
			transform_geometry_002.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Scale
			transform_geometry_002.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Transform Geometry.001
			transform_geometry_001 = _debug_arrows.nodes.new("GeometryNodeTransform")
			transform_geometry_001.name = "Transform Geometry.001"
			transform_geometry_001.mode = 'COMPONENTS'
			#Translation
			transform_geometry_001.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Rotation
			transform_geometry_001.inputs[2].default_value = (0.0, 1.5707963705062866, 0.0)
			#Scale
			transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Transform Geometry.003
			transform_geometry_003 = _debug_arrows.nodes.new("GeometryNodeTransform")
			transform_geometry_003.name = "Transform Geometry.003"
			transform_geometry_003.mode = 'COMPONENTS'
			#Translation
			transform_geometry_003.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Rotation
			transform_geometry_003.inputs[2].default_value = (1.5707963705062866, 0.0, 0.0)
			#Scale
			transform_geometry_003.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Vector Math.008
			vector_math_008 = _debug_arrows.nodes.new("ShaderNodeVectorMath")
			vector_math_008.name = "Vector Math.008"
			vector_math_008.operation = 'SCALE'
			#Vector
			vector_math_008.inputs[0].default_value = (0.0, 0.0, 10.300000190734863)
			#Scale
			vector_math_008.inputs[3].default_value = 0.0010000000474974513
			
			#node Cone
			cone = _debug_arrows.nodes.new("GeometryNodeMeshCone")
			cone.name = "Cone"
			cone.fill_type = 'NGON'
			#Vertices
			cone.inputs[0].default_value = 6
			#Side Segments
			cone.inputs[1].default_value = 1
			#Fill Segments
			cone.inputs[2].default_value = 1
			#Radius Top
			cone.inputs[3].default_value = 0.0
			#Radius Bottom
			cone.inputs[4].default_value = 0.010000022128224373
			
			#node Math.003
			math_003 = _debug_arrows.nodes.new("ShaderNodeMath")
			math_003.name = "Math.003"
			math_003.operation = 'DIVIDE'
			math_003.use_clamp = False
			#Value
			math_003.inputs[0].default_value = 49.05999755859375
			#Value_001
			math_003.inputs[1].default_value = 1000.0
			
			#node Store Named Attribute.004
			store_named_attribute_004 = _debug_arrows.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_004.name = "Store Named Attribute.004"
			store_named_attribute_004.data_type = 'FLOAT_COLOR'
			store_named_attribute_004.domain = 'POINT'
			#Selection
			store_named_attribute_004.inputs[1].default_value = True
			#Name
			store_named_attribute_004.inputs[2].default_value = "Color"
			#Value
			store_named_attribute_004.inputs[3].default_value = (0.4605487287044525, 0.05103481188416481, 0.07814221829175949, 0.0)
			
			#node Store Named Attribute
			store_named_attribute = _debug_arrows.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute.name = "Store Named Attribute"
			store_named_attribute.data_type = 'FLOAT_COLOR'
			store_named_attribute.domain = 'POINT'
			#Selection
			store_named_attribute.inputs[1].default_value = True
			#Name
			store_named_attribute.inputs[2].default_value = "Color"
			#Value
			store_named_attribute.inputs[3].default_value = (0.059955447912216187, 0.21724288165569305, 0.4605487287044525, 0.0)
			
			#node Store Named Attribute.005
			store_named_attribute_005 = _debug_arrows.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_005.name = "Store Named Attribute.005"
			store_named_attribute_005.data_type = 'FLOAT_COLOR'
			store_named_attribute_005.domain = 'POINT'
			#Selection
			store_named_attribute_005.inputs[1].default_value = True
			#Name
			store_named_attribute_005.inputs[2].default_value = "Color"
			#Value
			store_named_attribute_005.inputs[3].default_value = (0.21280108392238617, 0.4605487287044525, 0.12887145578861237, 0.0)
			
			#node Set Position
			set_position = _debug_arrows.nodes.new("GeometryNodeSetPosition")
			set_position.name = "Set Position"
			#Selection
			set_position.inputs[1].default_value = True
			
			#node Attribute Statistic
			attribute_statistic = _debug_arrows.nodes.new("GeometryNodeAttributeStatistic")
			attribute_statistic.name = "Attribute Statistic"
			attribute_statistic.data_type = 'FLOAT_VECTOR'
			attribute_statistic.domain = 'POINT'
			#Selection
			attribute_statistic.inputs[1].default_value = True
			
			#node Compare
			compare = _debug_arrows.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'VECTOR'
			compare.mode = 'ELEMENT'
			compare.operation = 'NOT_EQUAL'
			#B_VEC3
			compare.inputs[5].default_value = (0.0, 0.0, 0.0)
			#Epsilon
			compare.inputs[12].default_value = 9.999999747378752e-05
			
			#node Position
			position = _debug_arrows.nodes.new("GeometryNodeInputPosition")
			position.name = "Position"
			
			#node Switch
			switch = _debug_arrows.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'VECTOR'
			
			#node Group Input
			group_input_5 = _debug_arrows.nodes.new("NodeGroupInput")
			group_input_5.name = "Group Input"
			
			#node Reroute
			reroute_1 = _debug_arrows.nodes.new("NodeReroute")
			reroute_1.name = "Reroute"
			
			
			
			#Set locations
			group_output_6.location = (1428.90478515625, 0.0)
			instance_on_points_002.location = (988.90478515625, 429.669189453125)
			reroute_003.location = (-276.560546875, 27.071929931640625)
			reroute_009.location = (-209.260498046875, 36.829681396484375)
			join_geometry_001.location = (208.553955078125, 85.46240234375)
			transform_geometry_002.location = (-504.560546875, -72.58740234375)
			transform_geometry_001.location = (-218.82080078125, 19.31646728515625)
			transform_geometry_003.location = (-224.560546875, -334.53759765625)
			vector_math_008.location = (-505.0859375, -418.4356689453125)
			cone.location = (-724.560546875, -214.53759765625)
			math_003.location = (-900.904541015625, -429.669189453125)
			store_named_attribute_004.location = (-20.0, -100.0)
			store_named_attribute.location = (-20.0, 120.0)
			store_named_attribute_005.location = (-20.0, -320.0)
			set_position.location = (578.2709350585938, 400.1163024902344)
			attribute_statistic.location = (-35.687705993652344, 679.48095703125)
			compare.location = (128.0, 680.0)
			position.location = (40.0, 420.0)
			switch.location = (308.0, 460.0)
			group_input_5.location = (-640.0, 320.0)
			reroute_1.location = (-192.0, 380.0)
			
			#Set dimensions
			group_output_6.width, group_output_6.height = 140.0, 100.0
			instance_on_points_002.width, instance_on_points_002.height = 140.0, 100.0
			reroute_003.width, reroute_003.height = 16.0, 100.0
			reroute_009.width, reroute_009.height = 16.0, 100.0
			join_geometry_001.width, join_geometry_001.height = 140.0, 100.0
			transform_geometry_002.width, transform_geometry_002.height = 140.0, 100.0
			transform_geometry_001.width, transform_geometry_001.height = 140.0, 100.0
			transform_geometry_003.width, transform_geometry_003.height = 140.0, 100.0
			vector_math_008.width, vector_math_008.height = 140.0, 100.0
			cone.width, cone.height = 140.0, 100.0
			math_003.width, math_003.height = 140.0, 100.0
			store_named_attribute_004.width, store_named_attribute_004.height = 140.0, 100.0
			store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
			store_named_attribute_005.width, store_named_attribute_005.height = 140.0, 100.0
			set_position.width, set_position.height = 140.0, 100.0
			attribute_statistic.width, attribute_statistic.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			position.width, position.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			group_input_5.width, group_input_5.height = 140.0, 100.0
			reroute_1.width, reroute_1.height = 16.0, 100.0
			
			#initialize _debug_arrows links
			#reroute_009.Output -> store_named_attribute.Geometry
			_debug_arrows.links.new(reroute_009.outputs[0], store_named_attribute.inputs[0])
			#math_003.Value -> cone.Depth
			_debug_arrows.links.new(math_003.outputs[0], cone.inputs[5])
			#transform_geometry_003.Geometry -> store_named_attribute_005.Geometry
			_debug_arrows.links.new(transform_geometry_003.outputs[0], store_named_attribute_005.inputs[0])
			#transform_geometry_001.Geometry -> store_named_attribute_004.Geometry
			_debug_arrows.links.new(transform_geometry_001.outputs[0], store_named_attribute_004.inputs[0])
			#vector_math_008.Vector -> transform_geometry_002.Translation
			_debug_arrows.links.new(vector_math_008.outputs[0], transform_geometry_002.inputs[1])
			#reroute_003.Output -> transform_geometry_003.Geometry
			_debug_arrows.links.new(reroute_003.outputs[0], transform_geometry_003.inputs[0])
			#cone.Mesh -> transform_geometry_002.Geometry
			_debug_arrows.links.new(cone.outputs[0], transform_geometry_002.inputs[0])
			#reroute_003.Output -> reroute_009.Input
			_debug_arrows.links.new(reroute_003.outputs[0], reroute_009.inputs[0])
			#store_named_attribute_004.Geometry -> join_geometry_001.Geometry
			_debug_arrows.links.new(store_named_attribute_004.outputs[0], join_geometry_001.inputs[0])
			#transform_geometry_002.Geometry -> reroute_003.Input
			_debug_arrows.links.new(transform_geometry_002.outputs[0], reroute_003.inputs[0])
			#reroute_003.Output -> transform_geometry_001.Geometry
			_debug_arrows.links.new(reroute_003.outputs[0], transform_geometry_001.inputs[0])
			#join_geometry_001.Geometry -> instance_on_points_002.Instance
			_debug_arrows.links.new(join_geometry_001.outputs[0], instance_on_points_002.inputs[2])
			#set_position.Geometry -> instance_on_points_002.Points
			_debug_arrows.links.new(set_position.outputs[0], instance_on_points_002.inputs[0])
			#group_input_5.Scale -> instance_on_points_002.Scale
			_debug_arrows.links.new(group_input_5.outputs[4], instance_on_points_002.inputs[6])
			#group_input_5.Rotation -> instance_on_points_002.Rotation
			_debug_arrows.links.new(group_input_5.outputs[3], instance_on_points_002.inputs[5])
			#instance_on_points_002.Instances -> group_output_6.Instances
			_debug_arrows.links.new(instance_on_points_002.outputs[0], group_output_6.inputs[0])
			#reroute_1.Output -> set_position.Geometry
			_debug_arrows.links.new(reroute_1.outputs[0], set_position.inputs[0])
			#group_input_5.Position -> attribute_statistic.Attribute
			_debug_arrows.links.new(group_input_5.outputs[1], attribute_statistic.inputs[2])
			#reroute_1.Output -> attribute_statistic.Geometry
			_debug_arrows.links.new(reroute_1.outputs[0], attribute_statistic.inputs[0])
			#attribute_statistic.Standard Deviation -> compare.A
			_debug_arrows.links.new(attribute_statistic.outputs[6], compare.inputs[4])
			#compare.Result -> switch.Switch
			_debug_arrows.links.new(compare.outputs[0], switch.inputs[0])
			#group_input_5.Position -> switch.True
			_debug_arrows.links.new(group_input_5.outputs[1], switch.inputs[2])
			#switch.Output -> set_position.Position
			_debug_arrows.links.new(switch.outputs[0], set_position.inputs[2])
			#position.Position -> switch.False
			_debug_arrows.links.new(position.outputs[0], switch.inputs[1])
			#group_input_5.Offset -> set_position.Offset
			_debug_arrows.links.new(group_input_5.outputs[2], set_position.inputs[3])
			#group_input_5.Points -> reroute_1.Input
			_debug_arrows.links.new(group_input_5.outputs[0], reroute_1.inputs[0])
			#store_named_attribute.Geometry -> join_geometry_001.Geometry
			_debug_arrows.links.new(store_named_attribute.outputs[0], join_geometry_001.inputs[0])
			#store_named_attribute_005.Geometry -> join_geometry_001.Geometry
			_debug_arrows.links.new(store_named_attribute_005.outputs[0], join_geometry_001.inputs[0])
			return _debug_arrows

		_debug_arrows = _debug_arrows_node_group()

		#initialize _selective_scale node group
		def _selective_scale_node_group():
			_selective_scale = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".selective_scale")

			_selective_scale.color_tag = 'NONE'
			_selective_scale.description = ""

			
			#_selective_scale interface
			#Socket Output
			output_socket = _selective_scale.interface.new_socket(name = "Output", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			output_socket.subtype = 'NONE'
			output_socket.default_value = 0.0
			output_socket.min_value = -3.4028234663852886e+38
			output_socket.max_value = 3.4028234663852886e+38
			output_socket.attribute_domain = 'POINT'
			
			#Socket Switch
			switch_socket = _selective_scale.interface.new_socket(name = "Switch", in_out='INPUT', socket_type = 'NodeSocketBool')
			switch_socket.attribute_domain = 'POINT'
			
			#Socket Input
			input_socket = _selective_scale.interface.new_socket(name = "Input", in_out='INPUT', socket_type = 'NodeSocketFloat')
			input_socket.subtype = 'NONE'
			input_socket.default_value = 0.0
			input_socket.min_value = -3.4028234663852886e+38
			input_socket.max_value = 3.4028234663852886e+38
			input_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket = _selective_scale.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket.subtype = 'NONE'
			value_socket.default_value = 0.800000011920929
			value_socket.min_value = -10000.0
			value_socket.max_value = 10000.0
			value_socket.attribute_domain = 'POINT'
			
			
			#initialize _selective_scale nodes
			#node Group Output
			group_output_7 = _selective_scale.nodes.new("NodeGroupOutput")
			group_output_7.name = "Group Output"
			group_output_7.is_active_output = True
			
			#node Group Input
			group_input_6 = _selective_scale.nodes.new("NodeGroupInput")
			group_input_6.name = "Group Input"
			
			#node Switch.005
			switch_005 = _selective_scale.nodes.new("GeometryNodeSwitch")
			switch_005.name = "Switch.005"
			switch_005.input_type = 'FLOAT'
			
			#node Math
			math = _selective_scale.nodes.new("ShaderNodeMath")
			math.name = "Math"
			math.operation = 'MULTIPLY'
			math.use_clamp = False
			
			#node Reroute.010
			reroute_010 = _selective_scale.nodes.new("NodeReroute")
			reroute_010.name = "Reroute.010"
			
			
			
			#Set locations
			group_output_7.location = (200.0, 0.0)
			group_input_6.location = (-210.0, 0.0)
			switch_005.location = (10.0, 90.0)
			math.location = (10.0, -70.0)
			reroute_010.location = (-10.0, -90.0)
			
			#Set dimensions
			group_output_7.width, group_output_7.height = 140.0, 100.0
			group_input_6.width, group_input_6.height = 140.0, 100.0
			switch_005.width, switch_005.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			reroute_010.width, reroute_010.height = 16.0, 100.0
			
			#initialize _selective_scale links
			#math.Value -> switch_005.True
			_selective_scale.links.new(math.outputs[0], switch_005.inputs[2])
			#reroute_010.Output -> switch_005.False
			_selective_scale.links.new(reroute_010.outputs[0], switch_005.inputs[1])
			#reroute_010.Output -> math.Value
			_selective_scale.links.new(reroute_010.outputs[0], math.inputs[0])
			#group_input_6.Switch -> switch_005.Switch
			_selective_scale.links.new(group_input_6.outputs[0], switch_005.inputs[0])
			#group_input_6.Input -> reroute_010.Input
			_selective_scale.links.new(group_input_6.outputs[1], reroute_010.inputs[0])
			#switch_005.Output -> group_output_7.Output
			_selective_scale.links.new(switch_005.outputs[0], group_output_7.inputs[0])
			#group_input_6.Value -> math.Value
			_selective_scale.links.new(group_input_6.outputs[2], math.inputs[1])
			return _selective_scale

		_selective_scale = _selective_scale_node_group()

		#initialize _mn_world_scale node group
		def _mn_world_scale_node_group():
			_mn_world_scale = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_world_scale")

			_mn_world_scale.color_tag = 'NONE'
			_mn_world_scale.description = ""

			
			#_mn_world_scale interface
			#Socket world_scale
			world_scale_socket = _mn_world_scale.interface.new_socket(name = "world_scale", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			world_scale_socket.subtype = 'NONE'
			world_scale_socket.default_value = 0.009999999776482582
			world_scale_socket.min_value = -3.4028234663852886e+38
			world_scale_socket.max_value = 3.4028234663852886e+38
			world_scale_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_world_scale nodes
			#node Group Input
			group_input_7 = _mn_world_scale.nodes.new("NodeGroupInput")
			group_input_7.name = "Group Input"
			
			#node Value
			value = _mn_world_scale.nodes.new("ShaderNodeValue")
			value.label = "world_scale"
			value.name = "Value"
			
			value.outputs[0].default_value = 0.009999999776482582
			#node Group Output
			group_output_8 = _mn_world_scale.nodes.new("NodeGroupOutput")
			group_output_8.name = "Group Output"
			group_output_8.is_active_output = True
			
			
			
			
			#Set locations
			group_input_7.location = (-200.0, 0.0)
			value.location = (0.0, 0.0)
			group_output_8.location = (190.0, 0.0)
			
			#Set dimensions
			group_input_7.width, group_input_7.height = 140.0, 100.0
			value.width, value.height = 140.0, 100.0
			group_output_8.width, group_output_8.height = 140.0, 100.0
			
			#initialize _mn_world_scale links
			#value.Value -> group_output_8.world_scale
			_mn_world_scale.links.new(value.outputs[0], group_output_8.inputs[0])
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
			angstrom_socket.subtype = 'NONE'
			angstrom_socket.default_value = 0.0
			angstrom_socket.min_value = -3.4028234663852886e+38
			angstrom_socket.max_value = 3.4028234663852886e+38
			angstrom_socket.attribute_domain = 'POINT'
			
			#Socket Nanometre
			nanometre_socket = mn_units.interface.new_socket(name = "Nanometre", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			nanometre_socket.subtype = 'NONE'
			nanometre_socket.default_value = 0.0
			nanometre_socket.min_value = -3.4028234663852886e+38
			nanometre_socket.max_value = 3.4028234663852886e+38
			nanometre_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_1 = mn_units.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket_1.subtype = 'NONE'
			value_socket_1.default_value = 3.0
			value_socket_1.min_value = -10000.0
			value_socket_1.max_value = 10000.0
			value_socket_1.attribute_domain = 'POINT'
			value_socket_1.description = "A value which will be scaled appropriately for the world"
			
			
			#initialize mn_units nodes
			#node Group Output
			group_output_9 = mn_units.nodes.new("NodeGroupOutput")
			group_output_9.name = "Group Output"
			group_output_9.is_active_output = True
			
			#node Group Input
			group_input_8 = mn_units.nodes.new("NodeGroupInput")
			group_input_8.name = "Group Input"
			
			#node Math
			math_1 = mn_units.nodes.new("ShaderNodeMath")
			math_1.name = "Math"
			math_1.operation = 'MULTIPLY'
			math_1.use_clamp = False
			
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
			group_output_9.location = (190.0, 0.0)
			group_input_8.location = (-240.0, 0.0)
			math_1.location = (-60.0, 0.0)
			math_001.location = (-60.0, -160.0)
			group_1.location = (-304.00421142578125, -104.114013671875)
			
			#Set dimensions
			group_output_9.width, group_output_9.height = 140.0, 100.0
			group_input_8.width, group_input_8.height = 140.0, 100.0
			math_1.width, math_1.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			group_1.width, group_1.height = 197.58424377441406, 100.0
			
			#initialize mn_units links
			#math_1.Value -> group_output_9.Angstrom
			mn_units.links.new(math_1.outputs[0], group_output_9.inputs[0])
			#group_input_8.Value -> math_1.Value
			mn_units.links.new(group_input_8.outputs[0], math_1.inputs[0])
			#group_1.world_scale -> math_1.Value
			mn_units.links.new(group_1.outputs[0], math_1.inputs[1])
			#math_1.Value -> math_001.Value
			mn_units.links.new(math_1.outputs[0], math_001.inputs[0])
			#math_001.Value -> group_output_9.Nanometre
			mn_units.links.new(math_001.outputs[0], group_output_9.inputs[1])
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
			offset_socket_1 = _field_offset_vec.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket_1.subtype = 'NONE'
			offset_socket_1.default_value = 0
			offset_socket_1.min_value = -2147483648
			offset_socket_1.max_value = 2147483647
			offset_socket_1.attribute_domain = 'POINT'
			
			
			#initialize _field_offset_vec nodes
			#node Group Input
			group_input_9 = _field_offset_vec.nodes.new("NodeGroupInput")
			group_input_9.name = "Group Input"
			
			#node Evaluate at Index
			evaluate_at_index = _field_offset_vec.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index.name = "Evaluate at Index"
			evaluate_at_index.data_type = 'FLOAT_VECTOR'
			evaluate_at_index.domain = 'POINT'
			
			#node Group Output
			group_output_10 = _field_offset_vec.nodes.new("NodeGroupOutput")
			group_output_10.name = "Group Output"
			group_output_10.is_active_output = True
			
			#node Math.001
			math_001_1 = _field_offset_vec.nodes.new("ShaderNodeMath")
			math_001_1.name = "Math.001"
			math_001_1.operation = 'ADD'
			math_001_1.use_clamp = False
			
			#node Index
			index = _field_offset_vec.nodes.new("GeometryNodeInputIndex")
			index.name = "Index"
			
			
			
			
			#Set locations
			group_input_9.location = (-417.64404296875, 0.0)
			evaluate_at_index.location = (-220.0, 100.0)
			group_output_10.location = (20.0, 20.0)
			math_001_1.location = (-220.0, -80.0)
			index.location = (-400.0, -180.0)
			
			#Set dimensions
			group_input_9.width, group_input_9.height = 140.0, 100.0
			evaluate_at_index.width, evaluate_at_index.height = 140.0, 100.0
			group_output_10.width, group_output_10.height = 140.0, 100.0
			math_001_1.width, math_001_1.height = 140.0, 100.0
			index.width, index.height = 140.0, 100.0
			
			#initialize _field_offset_vec links
			#math_001_1.Value -> evaluate_at_index.Index
			_field_offset_vec.links.new(math_001_1.outputs[0], evaluate_at_index.inputs[0])
			#group_input_9.Field -> evaluate_at_index.Value
			_field_offset_vec.links.new(group_input_9.outputs[0], evaluate_at_index.inputs[1])
			#group_input_9.Offset -> math_001_1.Value
			_field_offset_vec.links.new(group_input_9.outputs[1], math_001_1.inputs[0])
			#evaluate_at_index.Value -> group_output_10.Field
			_field_offset_vec.links.new(evaluate_at_index.outputs[0], group_output_10.inputs[0])
			#index.Index -> math_001_1.Value
			_field_offset_vec.links.new(index.outputs[0], math_001_1.inputs[1])
			return _field_offset_vec

		_field_offset_vec = _field_offset_vec_node_group()

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
			distance_socket.subtype = 'NONE'
			distance_socket.default_value = 3.0
			distance_socket.min_value = -10000.0
			distance_socket.max_value = 10000.0
			distance_socket.attribute_domain = 'POINT'
			
			#Socket Distance
			distance_socket_1 = _curve_ends_adjust_angle.interface.new_socket(name = "Distance", in_out='INPUT', socket_type = 'NodeSocketFloat')
			distance_socket_1.subtype = 'NONE'
			distance_socket_1.default_value = 0.4200000762939453
			distance_socket_1.min_value = -10000.0
			distance_socket_1.max_value = 10000.0
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
			named_attribute_1 = _curve_ends_adjust_angle.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_1.name = "Named Attribute"
			named_attribute_1.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_1.inputs[0].default_value = "forward"
			
			#node Position
			position_1 = _curve_ends_adjust_angle.nodes.new("GeometryNodeInputPosition")
			position_1.name = "Position"
			
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
			reroute_2 = _curve_ends_adjust_angle.nodes.new("NodeReroute")
			reroute_2.name = "Reroute"
			#node Named Attribute.001
			named_attribute_001_1 = _curve_ends_adjust_angle.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001_1.name = "Named Attribute.001"
			named_attribute_001_1.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_001_1.inputs[0].default_value = "reverse"
			
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
			group_output_11 = _curve_ends_adjust_angle.nodes.new("NodeGroupOutput")
			group_output_11.name = "Group Output"
			group_output_11.is_active_output = True
			
			#node Set Position
			set_position_1 = _curve_ends_adjust_angle.nodes.new("GeometryNodeSetPosition")
			set_position_1.name = "Set Position"
			#Position
			set_position_1.inputs[2].default_value = (0.0, 0.0, 0.0)
			
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
			vector_math_008_1 = _curve_ends_adjust_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_008_1.name = "Vector Math.008"
			vector_math_008_1.operation = 'NORMALIZE'
			
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
			switch_1 = _curve_ends_adjust_angle.nodes.new("GeometryNodeSwitch")
			switch_1.name = "Switch"
			switch_1.input_type = 'VECTOR'
			
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
			group_input_10 = _curve_ends_adjust_angle.nodes.new("NodeGroupInput")
			group_input_10.name = "Group Input"
			
			
			
			
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
			named_attribute_1.location = (-1020.0, -80.0)
			position_1.location = (-1020.0, -220.0)
			vector_math.location = (-860.0, -140.0)
			vector_math_002.location = (-860.0, -100.0)
			group_001_1.location = (-1020.0, -280.0)
			vector_math_003.location = (-700.0, -100.0)
			group_009.location = (71.90267944335938, -263.45281982421875)
			vector_math_010.location = (71.90267944335938, -103.45283508300781)
			reroute_2.location = (-35.006744384765625, -353.1360168457031)
			named_attribute_001_1.location = (311.4145812988281, -130.00930786132812)
			position_001.location = (311.4145812988281, -270.0093688964844)
			vector_math_004.location = (471.4145812988281, -190.00936889648438)
			vector_math_005.location = (471.4145812988281, -150.00930786132812)
			group_002_1.location = (311.4145812988281, -330.0093688964844)
			vector_math_006.location = (631.41455078125, -150.00930786132812)
			group_output_11.location = (1649.9193115234375, 169.1092529296875)
			set_position_1.location = (1430.0023193359375, 203.44369506835938)
			endpoint_selection_008.location = (180.0, 400.0)
			group_003.location = (-300.0, -240.0)
			group_019.location = (-620.0, 440.0)
			curve_handle_positions.location = (-780.0, -320.0)
			vector_math_008_1.location = (1330.0, -120.0)
			vector_math_009.location = (1330.0, 20.0)
			endpoint_selection_009.location = (969.6704711914062, 303.7537841796875)
			switch_1.location = (1110.0, -124.58650970458984)
			group_004.location = (1120.0, 0.0)
			curve_handle_positions_001.location = (900.0, -200.0)
			endpoint_selection_010.location = (900.0, -80.0)
			set_handle_positions_001.location = (566.909423828125, 249.68319702148438)
			set_handle_positions.location = (-153.090576171875, 229.68319702148438)
			group_input_10.location = (-1054.2796630859375, 148.32730102539062)
			
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
			named_attribute_1.width, named_attribute_1.height = 140.0, 100.0
			position_1.width, position_1.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			vector_math_002.width, vector_math_002.height = 140.0, 100.0
			group_001_1.width, group_001_1.height = 140.0, 100.0
			vector_math_003.width, vector_math_003.height = 140.0, 100.0
			group_009.width, group_009.height = 148.385009765625, 100.0
			vector_math_010.width, vector_math_010.height = 140.0, 100.0
			reroute_2.width, reroute_2.height = 16.0, 100.0
			named_attribute_001_1.width, named_attribute_001_1.height = 140.0, 100.0
			position_001.width, position_001.height = 140.0, 100.0
			vector_math_004.width, vector_math_004.height = 140.0, 100.0
			vector_math_005.width, vector_math_005.height = 140.0, 100.0
			group_002_1.width, group_002_1.height = 140.0, 100.0
			vector_math_006.width, vector_math_006.height = 140.0, 100.0
			group_output_11.width, group_output_11.height = 140.0, 100.0
			set_position_1.width, set_position_1.height = 140.0, 100.0
			endpoint_selection_008.width, endpoint_selection_008.height = 140.0, 100.0
			group_003.width, group_003.height = 148.385009765625, 100.0
			group_019.width, group_019.height = 158.9053955078125, 100.0
			curve_handle_positions.width, curve_handle_positions.height = 150.0, 100.0
			vector_math_008_1.width, vector_math_008_1.height = 140.0, 100.0
			vector_math_009.width, vector_math_009.height = 140.0, 100.0
			endpoint_selection_009.width, endpoint_selection_009.height = 140.0, 100.0
			switch_1.width, switch_1.height = 140.0, 100.0
			group_004.width, group_004.height = 140.0, 100.0
			curve_handle_positions_001.width, curve_handle_positions_001.height = 150.0, 100.0
			endpoint_selection_010.width, endpoint_selection_010.height = 140.0, 100.0
			set_handle_positions_001.width, set_handle_positions_001.height = 140.0, 100.0
			set_handle_positions.width, set_handle_positions.height = 140.0, 100.0
			group_input_10.width, group_input_10.height = 140.0, 100.0
			
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
			#reroute_2.Output -> group_009.Field
			_curve_ends_adjust_angle.links.new(reroute_2.outputs[0], group_009.inputs[0])
			#vector_math_007.Vector -> vector_math_012.Vector
			_curve_ends_adjust_angle.links.new(vector_math_007.outputs[0], vector_math_012.inputs[0])
			#endpoint_selection_008.Selection -> boolean_math_004.Boolean
			_curve_ends_adjust_angle.links.new(endpoint_selection_008.outputs[0], boolean_math_004.inputs[0])
			#group_2.Angstrom -> vector_math_011.Scale
			_curve_ends_adjust_angle.links.new(group_2.outputs[0], vector_math_011.inputs[3])
			#reroute_2.Output -> vector_math_010.Vector
			_curve_ends_adjust_angle.links.new(reroute_2.outputs[0], vector_math_010.inputs[0])
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
			#group_input_10.Curve -> set_spline_type_001.Curve
			_curve_ends_adjust_angle.links.new(group_input_10.outputs[0], set_spline_type_001.inputs[0])
			#set_position_1.Geometry -> group_output_11.Curve
			_curve_ends_adjust_angle.links.new(set_position_1.outputs[0], group_output_11.inputs[0])
			#group_input_10.Distance -> group_2.Value
			_curve_ends_adjust_angle.links.new(group_input_10.outputs[1], group_2.inputs[0])
			#curve_handle_positions.Right -> reroute_2.Input
			_curve_ends_adjust_angle.links.new(curve_handle_positions.outputs[1], reroute_2.inputs[0])
			#curve_handle_positions.Left -> reroute_001.Input
			_curve_ends_adjust_angle.links.new(curve_handle_positions.outputs[0], reroute_001.inputs[0])
			#named_attribute_1.Attribute -> vector_math.Vector
			_curve_ends_adjust_angle.links.new(named_attribute_1.outputs[0], vector_math.inputs[0])
			#position_1.Position -> vector_math.Vector
			_curve_ends_adjust_angle.links.new(position_1.outputs[0], vector_math.inputs[1])
			#vector_math.Vector -> vector_math_002.Vector
			_curve_ends_adjust_angle.links.new(vector_math.outputs[0], vector_math_002.inputs[0])
			#vector_math_002.Vector -> vector_math_003.Vector
			_curve_ends_adjust_angle.links.new(vector_math_002.outputs[0], vector_math_003.inputs[0])
			#group_001_1.Angstrom -> vector_math_003.Scale
			_curve_ends_adjust_angle.links.new(group_001_1.outputs[0], vector_math_003.inputs[3])
			#vector_math_003.Vector -> set_handle_positions.Offset
			_curve_ends_adjust_angle.links.new(vector_math_003.outputs[0], set_handle_positions.inputs[3])
			#named_attribute_001_1.Attribute -> vector_math_004.Vector
			_curve_ends_adjust_angle.links.new(named_attribute_001_1.outputs[0], vector_math_004.inputs[0])
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
			#set_handle_positions_001.Curve -> set_position_1.Geometry
			_curve_ends_adjust_angle.links.new(set_handle_positions_001.outputs[0], set_position_1.inputs[0])
			#endpoint_selection_009.Selection -> set_position_1.Selection
			_curve_ends_adjust_angle.links.new(endpoint_selection_009.outputs[0], set_position_1.inputs[1])
			#vector_math_008_1.Vector -> vector_math_009.Vector
			_curve_ends_adjust_angle.links.new(vector_math_008_1.outputs[0], vector_math_009.inputs[0])
			#group_004.Angstrom -> vector_math_009.Scale
			_curve_ends_adjust_angle.links.new(group_004.outputs[0], vector_math_009.inputs[3])
			#vector_math_009.Vector -> set_position_1.Offset
			_curve_ends_adjust_angle.links.new(vector_math_009.outputs[0], set_position_1.inputs[3])
			#curve_handle_positions_001.Left -> switch_1.False
			_curve_ends_adjust_angle.links.new(curve_handle_positions_001.outputs[0], switch_1.inputs[1])
			#switch_1.Output -> vector_math_008_1.Vector
			_curve_ends_adjust_angle.links.new(switch_1.outputs[0], vector_math_008_1.inputs[0])
			#curve_handle_positions_001.Right -> switch_1.True
			_curve_ends_adjust_angle.links.new(curve_handle_positions_001.outputs[1], switch_1.inputs[2])
			#endpoint_selection_010.Selection -> switch_1.Switch
			_curve_ends_adjust_angle.links.new(endpoint_selection_010.outputs[0], switch_1.inputs[0])
			#group_input_10.Distance -> group_004.Value
			_curve_ends_adjust_angle.links.new(group_input_10.outputs[2], group_004.inputs[0])
			return _curve_ends_adjust_angle

		_curve_ends_adjust_angle = _curve_ends_adjust_angle_node_group()

		#initialize _curve_ends_adjust_position node group
		def _curve_ends_adjust_position_node_group():
			_curve_ends_adjust_position = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "_curve_ends_adjust_position")

			_curve_ends_adjust_position.color_tag = 'NONE'
			_curve_ends_adjust_position.description = ""

			_curve_ends_adjust_position.is_modifier = True
			
			#_curve_ends_adjust_position interface
			#Socket Geometry
			geometry_socket = _curve_ends_adjust_position.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_1 = _curve_ends_adjust_position.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_1.attribute_domain = 'POINT'
			
			#Socket Distance
			distance_socket_2 = _curve_ends_adjust_position.interface.new_socket(name = "Distance", in_out='INPUT', socket_type = 'NodeSocketFloat')
			distance_socket_2.subtype = 'NONE'
			distance_socket_2.default_value = 0.30000001192092896
			distance_socket_2.min_value = -10000.0
			distance_socket_2.max_value = 10000.0
			distance_socket_2.attribute_domain = 'POINT'
			
			
			#initialize _curve_ends_adjust_position nodes
			#node Position
			position_2 = _curve_ends_adjust_position.nodes.new("GeometryNodeInputPosition")
			position_2.name = "Position"
			
			#node Group.026
			group_026 = _curve_ends_adjust_position.nodes.new("GeometryNodeGroup")
			group_026.name = "Group.026"
			group_026.node_tree = _field_offset_vec
			#Input_1
			group_026.inputs[1].default_value = -1
			
			#node Group.027
			group_027 = _curve_ends_adjust_position.nodes.new("GeometryNodeGroup")
			group_027.name = "Group.027"
			group_027.node_tree = _field_offset_vec
			#Input_1
			group_027.inputs[1].default_value = 1
			
			#node Vector Math.008
			vector_math_008_2 = _curve_ends_adjust_position.nodes.new("ShaderNodeVectorMath")
			vector_math_008_2.name = "Vector Math.008"
			vector_math_008_2.operation = 'SUBTRACT'
			
			#node Endpoint Selection.002
			endpoint_selection_002 = _curve_ends_adjust_position.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_002.name = "Endpoint Selection.002"
			#Start Size
			endpoint_selection_002.inputs[0].default_value = 0
			#End Size
			endpoint_selection_002.inputs[1].default_value = 1
			
			#node Switch.007
			switch_007 = _curve_ends_adjust_position.nodes.new("GeometryNodeSwitch")
			switch_007.name = "Switch.007"
			switch_007.input_type = 'VECTOR'
			#False
			switch_007.inputs[1].default_value = (0.0, 0.0, 0.0)
			
			#node Vector Math.009
			vector_math_009_1 = _curve_ends_adjust_position.nodes.new("ShaderNodeVectorMath")
			vector_math_009_1.name = "Vector Math.009"
			vector_math_009_1.operation = 'SUBTRACT'
			
			#node Endpoint Selection.001
			endpoint_selection_001 = _curve_ends_adjust_position.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_001.name = "Endpoint Selection.001"
			#Start Size
			endpoint_selection_001.inputs[0].default_value = 1
			#End Size
			endpoint_selection_001.inputs[1].default_value = 0
			
			#node Group Output
			group_output_12 = _curve_ends_adjust_position.nodes.new("NodeGroupOutput")
			group_output_12.name = "Group Output"
			group_output_12.is_active_output = True
			
			#node Group Input
			group_input_11 = _curve_ends_adjust_position.nodes.new("NodeGroupInput")
			group_input_11.name = "Group Input"
			
			#node Switch.010
			switch_010 = _curve_ends_adjust_position.nodes.new("GeometryNodeSwitch")
			switch_010.name = "Switch.010"
			switch_010.input_type = 'VECTOR'
			
			#node Vector Math
			vector_math_1 = _curve_ends_adjust_position.nodes.new("ShaderNodeVectorMath")
			vector_math_1.name = "Vector Math"
			vector_math_1.operation = 'NORMALIZE'
			
			#node Vector Math.003
			vector_math_003_1 = _curve_ends_adjust_position.nodes.new("ShaderNodeVectorMath")
			vector_math_003_1.name = "Vector Math.003"
			vector_math_003_1.operation = 'SCALE'
			
			#node Set Position.001
			set_position_001 = _curve_ends_adjust_position.nodes.new("GeometryNodeSetPosition")
			set_position_001.name = "Set Position.001"
			#Selection
			set_position_001.inputs[1].default_value = True
			#Position
			set_position_001.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Group.023
			group_023 = _curve_ends_adjust_position.nodes.new("GeometryNodeGroup")
			group_023.name = "Group.023"
			group_023.node_tree = mn_units
			
			
			
			
			#Set locations
			position_2.location = (-345.67303466796875, 21.96319580078125)
			group_026.location = (-165.67303466796875, -38.03680419921875)
			group_027.location = (-165.67303466796875, -318.03680419921875)
			vector_math_008_2.location = (-165.67303466796875, 101.96319580078125)
			endpoint_selection_002.location = (-365.67303466796875, -178.03680419921875)
			switch_007.location = (-5.67303466796875, 101.96319580078125)
			vector_math_009_1.location = (-165.67303466796875, -178.03680419921875)
			endpoint_selection_001.location = (-345.67303466796875, 141.96319580078125)
			group_output_12.location = (867.47216796875, 3.8314287662506104)
			group_input_11.location = (-500.0, 280.0)
			switch_010.location = (154.32696533203125, 101.96319580078125)
			vector_math_1.location = (300.0, 100.0)
			vector_math_003_1.location = (626.1260986328125, 105.79462432861328)
			set_position_001.location = (677.47216796875, 321.86822509765625)
			group_023.location = (154.32696533203125, -58.03680419921875)
			
			#Set dimensions
			position_2.width, position_2.height = 140.0, 100.0
			group_026.width, group_026.height = 140.0, 100.0
			group_027.width, group_027.height = 140.0, 100.0
			vector_math_008_2.width, vector_math_008_2.height = 140.0, 100.0
			endpoint_selection_002.width, endpoint_selection_002.height = 140.0, 100.0
			switch_007.width, switch_007.height = 140.0, 100.0
			vector_math_009_1.width, vector_math_009_1.height = 140.0, 100.0
			endpoint_selection_001.width, endpoint_selection_001.height = 140.0, 100.0
			group_output_12.width, group_output_12.height = 140.0, 100.0
			group_input_11.width, group_input_11.height = 140.0, 100.0
			switch_010.width, switch_010.height = 140.0, 100.0
			vector_math_1.width, vector_math_1.height = 140.0, 100.0
			vector_math_003_1.width, vector_math_003_1.height = 140.0, 100.0
			set_position_001.width, set_position_001.height = 140.0, 100.0
			group_023.width, group_023.height = 140.0, 100.0
			
			#initialize _curve_ends_adjust_position links
			#group_023.Angstrom -> vector_math_003_1.Scale
			_curve_ends_adjust_position.links.new(group_023.outputs[0], vector_math_003_1.inputs[3])
			#endpoint_selection_001.Selection -> switch_007.Switch
			_curve_ends_adjust_position.links.new(endpoint_selection_001.outputs[0], switch_007.inputs[0])
			#position_2.Position -> group_027.Field
			_curve_ends_adjust_position.links.new(position_2.outputs[0], group_027.inputs[0])
			#vector_math_008_2.Vector -> switch_007.True
			_curve_ends_adjust_position.links.new(vector_math_008_2.outputs[0], switch_007.inputs[2])
			#position_2.Position -> vector_math_009_1.Vector
			_curve_ends_adjust_position.links.new(position_2.outputs[0], vector_math_009_1.inputs[1])
			#position_2.Position -> vector_math_008_2.Vector
			_curve_ends_adjust_position.links.new(position_2.outputs[0], vector_math_008_2.inputs[1])
			#vector_math_009_1.Vector -> switch_010.True
			_curve_ends_adjust_position.links.new(vector_math_009_1.outputs[0], switch_010.inputs[2])
			#position_2.Position -> group_026.Field
			_curve_ends_adjust_position.links.new(position_2.outputs[0], group_026.inputs[0])
			#vector_math_003_1.Vector -> set_position_001.Offset
			_curve_ends_adjust_position.links.new(vector_math_003_1.outputs[0], set_position_001.inputs[3])
			#group_027.Field -> vector_math_009_1.Vector
			_curve_ends_adjust_position.links.new(group_027.outputs[0], vector_math_009_1.inputs[0])
			#switch_007.Output -> switch_010.False
			_curve_ends_adjust_position.links.new(switch_007.outputs[0], switch_010.inputs[1])
			#endpoint_selection_002.Selection -> switch_010.Switch
			_curve_ends_adjust_position.links.new(endpoint_selection_002.outputs[0], switch_010.inputs[0])
			#group_026.Field -> vector_math_008_2.Vector
			_curve_ends_adjust_position.links.new(group_026.outputs[0], vector_math_008_2.inputs[0])
			#group_input_11.Geometry -> set_position_001.Geometry
			_curve_ends_adjust_position.links.new(group_input_11.outputs[0], set_position_001.inputs[0])
			#set_position_001.Geometry -> group_output_12.Geometry
			_curve_ends_adjust_position.links.new(set_position_001.outputs[0], group_output_12.inputs[0])
			#switch_010.Output -> vector_math_1.Vector
			_curve_ends_adjust_position.links.new(switch_010.outputs[0], vector_math_1.inputs[0])
			#vector_math_1.Vector -> vector_math_003_1.Vector
			_curve_ends_adjust_position.links.new(vector_math_1.outputs[0], vector_math_003_1.inputs[0])
			#group_input_11.Distance -> group_023.Value
			_curve_ends_adjust_position.links.new(group_input_11.outputs[1], group_023.inputs[0])
			return _curve_ends_adjust_position

		_curve_ends_adjust_position = _curve_ends_adjust_position_node_group()

		#initialize _curve_to_mesh node group
		def _curve_to_mesh_node_group():
			_curve_to_mesh = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".curve_to_mesh")

			_curve_to_mesh.color_tag = 'NONE'
			_curve_to_mesh.description = ""

			_curve_to_mesh.is_modifier = True
			
			#_curve_to_mesh interface
			#Socket Mesh
			mesh_socket = _curve_to_mesh.interface.new_socket(name = "Mesh", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			mesh_socket.attribute_domain = 'POINT'
			
			#Socket Curve
			curve_socket_2 = _curve_to_mesh.interface.new_socket(name = "Curve", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			curve_socket_2.attribute_domain = 'POINT'
			
			#Socket Profile Curve
			profile_curve_socket = _curve_to_mesh.interface.new_socket(name = "Profile Curve", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			profile_curve_socket.attribute_domain = 'POINT'
			
			#Socket Resolution
			resolution_socket = _curve_to_mesh.interface.new_socket(name = "Resolution", in_out='INPUT', socket_type = 'NodeSocketInt')
			resolution_socket.subtype = 'NONE'
			resolution_socket.default_value = 12
			resolution_socket.min_value = 3
			resolution_socket.max_value = 512
			resolution_socket.attribute_domain = 'POINT'
			
			#Socket Fill Caps
			fill_caps_socket = _curve_to_mesh.interface.new_socket(name = "Fill Caps", in_out='INPUT', socket_type = 'NodeSocketBool')
			fill_caps_socket.attribute_domain = 'POINT'
			
			#Socket Radius (A)
			radius__a__socket = _curve_to_mesh.interface.new_socket(name = "Radius (A)", in_out='INPUT', socket_type = 'NodeSocketFloat')
			radius__a__socket.subtype = 'NONE'
			radius__a__socket.default_value = 0.20000000298023224
			radius__a__socket.min_value = 0.0
			radius__a__socket.max_value = 10000.0
			radius__a__socket.attribute_domain = 'POINT'
			
			
			#initialize _curve_to_mesh nodes
			#node Group Output
			group_output_13 = _curve_to_mesh.nodes.new("NodeGroupOutput")
			group_output_13.name = "Group Output"
			group_output_13.is_active_output = True
			
			#node Curve to Mesh
			curve_to_mesh = _curve_to_mesh.nodes.new("GeometryNodeCurveToMesh")
			curve_to_mesh.name = "Curve to Mesh"
			
			#node Group
			group_3 = _curve_to_mesh.nodes.new("GeometryNodeGroup")
			group_3.name = "Group"
			group_3.node_tree = mn_units
			
			#node Curve Circle
			curve_circle = _curve_to_mesh.nodes.new("GeometryNodeCurvePrimitiveCircle")
			curve_circle.name = "Curve Circle"
			curve_circle.mode = 'RADIUS'
			#Radius
			curve_circle.inputs[4].default_value = 1.0
			
			#node Domain Size
			domain_size = _curve_to_mesh.nodes.new("GeometryNodeAttributeDomainSize")
			domain_size.name = "Domain Size"
			domain_size.component = 'CURVE'
			
			#node Compare
			compare_1 = _curve_to_mesh.nodes.new("FunctionNodeCompare")
			compare_1.name = "Compare"
			compare_1.data_type = 'INT'
			compare_1.mode = 'ELEMENT'
			compare_1.operation = 'EQUAL'
			#B_INT
			compare_1.inputs[3].default_value = 0
			
			#node Switch
			switch_2 = _curve_to_mesh.nodes.new("GeometryNodeSwitch")
			switch_2.name = "Switch"
			switch_2.input_type = 'GEOMETRY'
			
			#node Group Input
			group_input_12 = _curve_to_mesh.nodes.new("NodeGroupInput")
			group_input_12.name = "Group Input"
			
			#node Set Curve Radius
			set_curve_radius = _curve_to_mesh.nodes.new("GeometryNodeSetCurveRadius")
			set_curve_radius.name = "Set Curve Radius"
			#Selection
			set_curve_radius.inputs[1].default_value = True
			
			
			
			
			#Set locations
			group_output_13.location = (190.0, 0.0)
			curve_to_mesh.location = (0.0, 0.0)
			group_3.location = (-577.7610473632812, -122.98338317871094)
			curve_circle.location = (-260.0, 40.0)
			domain_size.location = (-780.0, 120.0)
			compare_1.location = (-780.0, 280.0)
			switch_2.location = (-377.0369873046875, 349.30694580078125)
			group_input_12.location = (-780.0, -40.0)
			set_curve_radius.location = (-260.0, 180.0)
			
			#Set dimensions
			group_output_13.width, group_output_13.height = 140.0, 100.0
			curve_to_mesh.width, curve_to_mesh.height = 140.0, 100.0
			group_3.width, group_3.height = 261.9884033203125, 100.0
			curve_circle.width, curve_circle.height = 140.0, 100.0
			domain_size.width, domain_size.height = 140.0, 100.0
			compare_1.width, compare_1.height = 140.0, 100.0
			switch_2.width, switch_2.height = 140.0, 100.0
			group_input_12.width, group_input_12.height = 140.0, 100.0
			set_curve_radius.width, set_curve_radius.height = 140.0, 100.0
			
			#initialize _curve_to_mesh links
			#set_curve_radius.Curve -> curve_to_mesh.Curve
			_curve_to_mesh.links.new(set_curve_radius.outputs[0], curve_to_mesh.inputs[0])
			#curve_to_mesh.Mesh -> group_output_13.Mesh
			_curve_to_mesh.links.new(curve_to_mesh.outputs[0], group_output_13.inputs[0])
			#group_input_12.Fill Caps -> curve_to_mesh.Fill Caps
			_curve_to_mesh.links.new(group_input_12.outputs[3], curve_to_mesh.inputs[2])
			#group_input_12.Curve -> set_curve_radius.Curve
			_curve_to_mesh.links.new(group_input_12.outputs[0], set_curve_radius.inputs[0])
			#group_3.Angstrom -> set_curve_radius.Radius
			_curve_to_mesh.links.new(group_3.outputs[0], set_curve_radius.inputs[2])
			#group_input_12.Radius (A) -> group_3.Value
			_curve_to_mesh.links.new(group_input_12.outputs[4], group_3.inputs[0])
			#group_input_12.Resolution -> curve_circle.Resolution
			_curve_to_mesh.links.new(group_input_12.outputs[2], curve_circle.inputs[0])
			#group_input_12.Profile Curve -> domain_size.Geometry
			_curve_to_mesh.links.new(group_input_12.outputs[1], domain_size.inputs[0])
			#domain_size.Point Count -> compare_1.A
			_curve_to_mesh.links.new(domain_size.outputs[0], compare_1.inputs[2])
			#compare_1.Result -> switch_2.Switch
			_curve_to_mesh.links.new(compare_1.outputs[0], switch_2.inputs[0])
			#curve_circle.Curve -> switch_2.True
			_curve_to_mesh.links.new(curve_circle.outputs[0], switch_2.inputs[2])
			#switch_2.Output -> curve_to_mesh.Profile Curve
			_curve_to_mesh.links.new(switch_2.outputs[0], curve_to_mesh.inputs[1])
			#group_input_12.Profile Curve -> switch_2.False
			_curve_to_mesh.links.new(group_input_12.outputs[1], switch_2.inputs[1])
			return _curve_to_mesh

		_curve_to_mesh = _curve_to_mesh_node_group()

		#initialize offset_color node group
		def offset_color_node_group():
			offset_color = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Offset Color")

			offset_color.color_tag = 'NONE'
			offset_color.description = ""

			
			#offset_color interface
			#Socket Color
			color_socket = offset_color.interface.new_socket(name = "Color", in_out='OUTPUT', socket_type = 'NodeSocketColor')
			color_socket.attribute_domain = 'POINT'
			
			#Socket Index
			index_socket = offset_color.interface.new_socket(name = "Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			index_socket.subtype = 'NONE'
			index_socket.default_value = 0
			index_socket.min_value = -2147483648
			index_socket.max_value = 2147483647
			index_socket.attribute_domain = 'POINT'
			
			#Socket Offset
			offset_socket_2 = offset_color.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket_2.subtype = 'NONE'
			offset_socket_2.default_value = 0
			offset_socket_2.min_value = -2147483648
			offset_socket_2.max_value = 2147483647
			offset_socket_2.attribute_domain = 'POINT'
			
			
			#initialize offset_color nodes
			#node Group Input
			group_input_13 = offset_color.nodes.new("NodeGroupInput")
			group_input_13.name = "Group Input"
			
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
			group_output_14 = offset_color.nodes.new("NodeGroupOutput")
			group_output_14.name = "Group Output"
			group_output_14.is_active_output = True
			
			#node Named Attribute
			named_attribute_2 = offset_color.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_2.name = "Named Attribute"
			named_attribute_2.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute_2.inputs[0].default_value = "Color"
			
			
			
			
			#Set locations
			group_input_13.location = (-220.0, -20.0)
			math_012.location = (-40.0, 0.0)
			evaluate_at_index_004.location = (140.0, 0.0)
			group_output_14.location = (340.0, 0.0)
			named_attribute_2.location = (-40.0, -160.0)
			
			#Set dimensions
			group_input_13.width, group_input_13.height = 140.0, 100.0
			math_012.width, math_012.height = 140.0, 100.0
			evaluate_at_index_004.width, evaluate_at_index_004.height = 140.0, 100.0
			group_output_14.width, group_output_14.height = 140.0, 100.0
			named_attribute_2.width, named_attribute_2.height = 140.0, 100.0
			
			#initialize offset_color links
			#math_012.Value -> evaluate_at_index_004.Index
			offset_color.links.new(math_012.outputs[0], evaluate_at_index_004.inputs[0])
			#group_input_13.Offset -> math_012.Value
			offset_color.links.new(group_input_13.outputs[1], math_012.inputs[1])
			#evaluate_at_index_004.Value -> group_output_14.Color
			offset_color.links.new(evaluate_at_index_004.outputs[0], group_output_14.inputs[0])
			#named_attribute_2.Attribute -> evaluate_at_index_004.Value
			offset_color.links.new(named_attribute_2.outputs[0], evaluate_at_index_004.inputs[1])
			#group_input_13.Index -> math_012.Value
			offset_color.links.new(group_input_13.outputs[0], math_012.inputs[0])
			return offset_color

		offset_color = offset_color_node_group()

		#initialize _curve_end_fix_color node group
		def _curve_end_fix_color_node_group():
			_curve_end_fix_color = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".curve_end_fix_color")

			_curve_end_fix_color.color_tag = 'NONE'
			_curve_end_fix_color.description = ""

			_curve_end_fix_color.is_modifier = True
			
			#_curve_end_fix_color interface
			#Socket Geometry
			geometry_socket_2 = _curve_end_fix_color.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_2.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_3 = _curve_end_fix_color.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_3.attribute_domain = 'POINT'
			
			
			#initialize _curve_end_fix_color nodes
			#node Store Named Attribute
			store_named_attribute_1 = _curve_end_fix_color.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_1.name = "Store Named Attribute"
			store_named_attribute_1.data_type = 'FLOAT_COLOR'
			store_named_attribute_1.domain = 'POINT'
			#Name
			store_named_attribute_1.inputs[2].default_value = "Color"
			
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
			named_attribute_001_2 = _curve_end_fix_color.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001_2.name = "Named Attribute.001"
			named_attribute_001_2.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute_001_2.inputs[0].default_value = "Color"
			
			#node Group.030
			group_030 = _curve_end_fix_color.nodes.new("GeometryNodeGroup")
			group_030.name = "Group.030"
			group_030.node_tree = _mn_select_sec_struct
			#Socket_1
			group_030.inputs[0].default_value = True
			
			#node Group Output
			group_output_15 = _curve_end_fix_color.nodes.new("NodeGroupOutput")
			group_output_15.name = "Group Output"
			group_output_15.is_active_output = True
			
			#node Group Input
			group_input_14 = _curve_end_fix_color.nodes.new("NodeGroupInput")
			group_input_14.name = "Group Input"
			
			
			
			
			#Set locations
			store_named_attribute_1.location = (180.0, 270.0)
			switch_011.location = (-20.0, -110.0)
			group_029.location = (160.0, -270.0)
			endpoint_selection_004.location = (160.0, 10.0)
			endpoint_selection_003.location = (-20.0, 10.0)
			group_028.location = (-20.0, -270.0)
			switch_012.location = (160.0, -110.0)
			named_attribute_001_2.location = (-180.0, -250.0)
			group_030.location = (-60.0, 190.0)
			group_output_15.location = (360.0, 320.0)
			group_input_14.location = (-40.0, 300.0)
			
			#Set dimensions
			store_named_attribute_1.width, store_named_attribute_1.height = 140.0, 100.0
			switch_011.width, switch_011.height = 140.0, 100.0
			group_029.width, group_029.height = 140.0, 100.0
			endpoint_selection_004.width, endpoint_selection_004.height = 140.0, 100.0
			endpoint_selection_003.width, endpoint_selection_003.height = 140.0, 100.0
			group_028.width, group_028.height = 140.0, 100.0
			switch_012.width, switch_012.height = 140.0, 100.0
			named_attribute_001_2.width, named_attribute_001_2.height = 140.0, 100.0
			group_030.width, group_030.height = 158.9053955078125, 100.0
			group_output_15.width, group_output_15.height = 140.0, 100.0
			group_input_14.width, group_input_14.height = 140.0, 100.0
			
			#initialize _curve_end_fix_color links
			#switch_011.Output -> switch_012.False
			_curve_end_fix_color.links.new(switch_011.outputs[0], switch_012.inputs[1])
			#named_attribute_001_2.Attribute -> switch_011.False
			_curve_end_fix_color.links.new(named_attribute_001_2.outputs[0], switch_011.inputs[1])
			#endpoint_selection_003.Selection -> switch_011.Switch
			_curve_end_fix_color.links.new(endpoint_selection_003.outputs[0], switch_011.inputs[0])
			#group_028.Color -> switch_011.True
			_curve_end_fix_color.links.new(group_028.outputs[0], switch_011.inputs[2])
			#group_029.Color -> switch_012.True
			_curve_end_fix_color.links.new(group_029.outputs[0], switch_012.inputs[2])
			#switch_012.Output -> store_named_attribute_1.Value
			_curve_end_fix_color.links.new(switch_012.outputs[0], store_named_attribute_1.inputs[3])
			#group_030.Is Structured -> store_named_attribute_1.Selection
			_curve_end_fix_color.links.new(group_030.outputs[2], store_named_attribute_1.inputs[1])
			#endpoint_selection_004.Selection -> switch_012.Switch
			_curve_end_fix_color.links.new(endpoint_selection_004.outputs[0], switch_012.inputs[0])
			#group_input_14.Geometry -> store_named_attribute_1.Geometry
			_curve_end_fix_color.links.new(group_input_14.outputs[0], store_named_attribute_1.inputs[0])
			#store_named_attribute_1.Geometry -> group_output_15.Geometry
			_curve_end_fix_color.links.new(store_named_attribute_1.outputs[0], group_output_15.inputs[0])
			return _curve_end_fix_color

		_curve_end_fix_color = _curve_end_fix_color_node_group()

		#initialize _mn_cartoon_smooth_handles node group
		def _mn_cartoon_smooth_handles_node_group():
			_mn_cartoon_smooth_handles = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_cartoon_smooth_handles")

			_mn_cartoon_smooth_handles.color_tag = 'NONE'
			_mn_cartoon_smooth_handles.description = ""

			
			#_mn_cartoon_smooth_handles interface
			#Socket Vector
			vector_socket = _mn_cartoon_smooth_handles.interface.new_socket(name = "Vector", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			vector_socket.subtype = 'NONE'
			vector_socket.default_value = (0.0, 0.0, 0.0)
			vector_socket.min_value = -3.4028234663852886e+38
			vector_socket.max_value = 3.4028234663852886e+38
			vector_socket.attribute_domain = 'POINT'
			
			#Socket Scale
			scale_socket_1 = _mn_cartoon_smooth_handles.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
			scale_socket_1.subtype = 'NONE'
			scale_socket_1.default_value = 0.00800000037997961
			scale_socket_1.min_value = -10000.0
			scale_socket_1.max_value = 10000.0
			scale_socket_1.attribute_domain = 'POINT'
			
			
			#initialize _mn_cartoon_smooth_handles nodes
			#node Vector Math.005
			vector_math_005_1 = _mn_cartoon_smooth_handles.nodes.new("ShaderNodeVectorMath")
			vector_math_005_1.name = "Vector Math.005"
			vector_math_005_1.operation = 'NORMALIZE'
			
			#node Named Attribute.004
			named_attribute_004 = _mn_cartoon_smooth_handles.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_004.name = "Named Attribute.004"
			named_attribute_004.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_004.inputs[0].default_value = "guide_X"
			
			#node Vector Math.006
			vector_math_006_1 = _mn_cartoon_smooth_handles.nodes.new("ShaderNodeVectorMath")
			vector_math_006_1.name = "Vector Math.006"
			vector_math_006_1.operation = 'NORMALIZE'
			
			#node Named Attribute.003
			named_attribute_003 = _mn_cartoon_smooth_handles.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_003.name = "Named Attribute.003"
			named_attribute_003.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_003.inputs[0].default_value = "guide_Z"
			
			#node Vector Math.007
			vector_math_007_1 = _mn_cartoon_smooth_handles.nodes.new("ShaderNodeVectorMath")
			vector_math_007_1.name = "Vector Math.007"
			vector_math_007_1.operation = 'CROSS_PRODUCT'
			
			#node Vector Math.008
			vector_math_008_3 = _mn_cartoon_smooth_handles.nodes.new("ShaderNodeVectorMath")
			vector_math_008_3.name = "Vector Math.008"
			vector_math_008_3.operation = 'SCALE'
			
			#node Group Output
			group_output_16 = _mn_cartoon_smooth_handles.nodes.new("NodeGroupOutput")
			group_output_16.name = "Group Output"
			group_output_16.is_active_output = True
			
			#node Group
			group_4 = _mn_cartoon_smooth_handles.nodes.new("GeometryNodeGroup")
			group_4.name = "Group"
			group_4.node_tree = mn_units
			
			#node Group Input
			group_input_15 = _mn_cartoon_smooth_handles.nodes.new("NodeGroupInput")
			group_input_15.name = "Group Input"
			
			
			
			
			#Set locations
			vector_math_005_1.location = (-40.0, 120.0)
			named_attribute_004.location = (-200.0, 120.0)
			vector_math_006_1.location = (-40.0, -20.0)
			named_attribute_003.location = (-200.0, -20.0)
			vector_math_007_1.location = (120.0, 120.0)
			vector_math_008_3.location = (280.0, 120.0)
			group_output_16.location = (440.0, 120.0)
			group_4.location = (280.0, -20.0)
			group_input_15.location = (120.0, -20.0)
			
			#Set dimensions
			vector_math_005_1.width, vector_math_005_1.height = 140.0, 100.0
			named_attribute_004.width, named_attribute_004.height = 140.0, 100.0
			vector_math_006_1.width, vector_math_006_1.height = 140.0, 100.0
			named_attribute_003.width, named_attribute_003.height = 140.0, 100.0
			vector_math_007_1.width, vector_math_007_1.height = 140.0, 100.0
			vector_math_008_3.width, vector_math_008_3.height = 140.0, 100.0
			group_output_16.width, group_output_16.height = 140.0, 100.0
			group_4.width, group_4.height = 140.0, 100.0
			group_input_15.width, group_input_15.height = 140.0, 100.0
			
			#initialize _mn_cartoon_smooth_handles links
			#vector_math_007_1.Vector -> vector_math_008_3.Vector
			_mn_cartoon_smooth_handles.links.new(vector_math_007_1.outputs[0], vector_math_008_3.inputs[0])
			#named_attribute_004.Attribute -> vector_math_005_1.Vector
			_mn_cartoon_smooth_handles.links.new(named_attribute_004.outputs[0], vector_math_005_1.inputs[0])
			#vector_math_005_1.Vector -> vector_math_007_1.Vector
			_mn_cartoon_smooth_handles.links.new(vector_math_005_1.outputs[0], vector_math_007_1.inputs[0])
			#vector_math_006_1.Vector -> vector_math_007_1.Vector
			_mn_cartoon_smooth_handles.links.new(vector_math_006_1.outputs[0], vector_math_007_1.inputs[1])
			#named_attribute_003.Attribute -> vector_math_006_1.Vector
			_mn_cartoon_smooth_handles.links.new(named_attribute_003.outputs[0], vector_math_006_1.inputs[0])
			#vector_math_008_3.Vector -> group_output_16.Vector
			_mn_cartoon_smooth_handles.links.new(vector_math_008_3.outputs[0], group_output_16.inputs[0])
			#group_input_15.Scale -> group_4.Value
			_mn_cartoon_smooth_handles.links.new(group_input_15.outputs[0], group_4.inputs[0])
			#group_4.Angstrom -> vector_math_008_3.Scale
			_mn_cartoon_smooth_handles.links.new(group_4.outputs[0], vector_math_008_3.inputs[3])
			return _mn_cartoon_smooth_handles

		_mn_cartoon_smooth_handles = _mn_cartoon_smooth_handles_node_group()

		#initialize _field_offset_bool node group
		def _field_offset_bool_node_group():
			_field_offset_bool = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".field_offset_bool")

			_field_offset_bool.color_tag = 'NONE'
			_field_offset_bool.description = ""

			
			#_field_offset_bool interface
			#Socket Boolean
			boolean_socket = _field_offset_bool.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket.attribute_domain = 'POINT'
			
			#Socket Boolean
			boolean_socket_1 = _field_offset_bool.interface.new_socket(name = "Boolean", in_out='INPUT', socket_type = 'NodeSocketBool')
			boolean_socket_1.attribute_domain = 'POINT'
			boolean_socket_1.hide_value = True
			
			#Socket Offset
			offset_socket_3 = _field_offset_bool.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket_3.subtype = 'NONE'
			offset_socket_3.default_value = 0
			offset_socket_3.min_value = -2147483648
			offset_socket_3.max_value = 2147483647
			offset_socket_3.attribute_domain = 'POINT'
			
			
			#initialize _field_offset_bool nodes
			#node Group Input
			group_input_16 = _field_offset_bool.nodes.new("NodeGroupInput")
			group_input_16.name = "Group Input"
			
			#node Index
			index_1 = _field_offset_bool.nodes.new("GeometryNodeInputIndex")
			index_1.name = "Index"
			
			#node Math.001
			math_001_2 = _field_offset_bool.nodes.new("ShaderNodeMath")
			math_001_2.name = "Math.001"
			math_001_2.operation = 'ADD'
			math_001_2.use_clamp = False
			
			#node Evaluate at Index.001
			evaluate_at_index_001 = _field_offset_bool.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001.name = "Evaluate at Index.001"
			evaluate_at_index_001.data_type = 'BOOLEAN'
			evaluate_at_index_001.domain = 'POINT'
			
			#node Group Output
			group_output_17 = _field_offset_bool.nodes.new("NodeGroupOutput")
			group_output_17.name = "Group Output"
			group_output_17.is_active_output = True
			
			
			
			
			#Set locations
			group_input_16.location = (-417.64404296875, 0.0)
			index_1.location = (-420.0, -120.0)
			math_001_2.location = (-220.0, -120.0)
			evaluate_at_index_001.location = (-220.0, 40.0)
			group_output_17.location = (-60.0, 40.0)
			
			#Set dimensions
			group_input_16.width, group_input_16.height = 140.0, 100.0
			index_1.width, index_1.height = 140.0, 100.0
			math_001_2.width, math_001_2.height = 140.0, 100.0
			evaluate_at_index_001.width, evaluate_at_index_001.height = 140.0, 100.0
			group_output_17.width, group_output_17.height = 140.0, 100.0
			
			#initialize _field_offset_bool links
			#group_input_16.Offset -> math_001_2.Value
			_field_offset_bool.links.new(group_input_16.outputs[1], math_001_2.inputs[0])
			#math_001_2.Value -> evaluate_at_index_001.Index
			_field_offset_bool.links.new(math_001_2.outputs[0], evaluate_at_index_001.inputs[0])
			#group_input_16.Boolean -> evaluate_at_index_001.Value
			_field_offset_bool.links.new(group_input_16.outputs[0], evaluate_at_index_001.inputs[1])
			#evaluate_at_index_001.Value -> group_output_17.Boolean
			_field_offset_bool.links.new(evaluate_at_index_001.outputs[0], group_output_17.inputs[0])
			#index_1.Index -> math_001_2.Value
			_field_offset_bool.links.new(index_1.outputs[0], math_001_2.inputs[1])
			return _field_offset_bool

		_field_offset_bool = _field_offset_bool_node_group()

		#initialize _cartoon_arrows_scale node group
		def _cartoon_arrows_scale_node_group():
			_cartoon_arrows_scale = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".cartoon_arrows_scale")

			_cartoon_arrows_scale.color_tag = 'NONE'
			_cartoon_arrows_scale.description = ""

			
			#_cartoon_arrows_scale interface
			#Socket Result
			result_socket = _cartoon_arrows_scale.interface.new_socket(name = "Result", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			result_socket.attribute_domain = 'POINT'
			
			#Socket Output
			output_socket_1 = _cartoon_arrows_scale.interface.new_socket(name = "Output", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			output_socket_1.subtype = 'NONE'
			output_socket_1.default_value = 0.0
			output_socket_1.min_value = -3.4028234663852886e+38
			output_socket_1.max_value = 3.4028234663852886e+38
			output_socket_1.attribute_domain = 'POINT'
			
			#Socket Input
			input_socket_1 = _cartoon_arrows_scale.interface.new_socket(name = "Input", in_out='INPUT', socket_type = 'NodeSocketFloat')
			input_socket_1.subtype = 'NONE'
			input_socket_1.default_value = 0.0
			input_socket_1.min_value = -3.4028234663852886e+38
			input_socket_1.max_value = 3.4028234663852886e+38
			input_socket_1.attribute_domain = 'POINT'
			
			#Socket Input
			input_socket_2 = _cartoon_arrows_scale.interface.new_socket(name = "Input", in_out='INPUT', socket_type = 'NodeSocketFloat')
			input_socket_2.subtype = 'NONE'
			input_socket_2.default_value = 0.0
			input_socket_2.min_value = -3.4028234663852886e+38
			input_socket_2.max_value = 3.4028234663852886e+38
			input_socket_2.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_2 = _cartoon_arrows_scale.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket_2.subtype = 'NONE'
			value_socket_2.default_value = 2.8499999046325684
			value_socket_2.min_value = -10000.0
			value_socket_2.max_value = 10000.0
			value_socket_2.attribute_domain = 'POINT'
			
			
			#initialize _cartoon_arrows_scale nodes
			#node Group Output
			group_output_18 = _cartoon_arrows_scale.nodes.new("NodeGroupOutput")
			group_output_18.name = "Group Output"
			group_output_18.is_active_output = True
			
			#node Math.006
			math_006 = _cartoon_arrows_scale.nodes.new("ShaderNodeMath")
			math_006.name = "Math.006"
			math_006.hide = True
			math_006.operation = 'MAXIMUM'
			math_006.use_clamp = False
			#Value_001
			math_006.inputs[1].default_value = 0.0
			
			#node Spline Parameter
			spline_parameter = _cartoon_arrows_scale.nodes.new("GeometryNodeSplineParameter")
			spline_parameter.name = "Spline Parameter"
			
			#node Map Range
			map_range = _cartoon_arrows_scale.nodes.new("ShaderNodeMapRange")
			map_range.name = "Map Range"
			map_range.clamp = True
			map_range.data_type = 'FLOAT'
			map_range.interpolation_type = 'LINEAR'
			
			#node Math.003
			math_003_1 = _cartoon_arrows_scale.nodes.new("ShaderNodeMath")
			math_003_1.name = "Math.003"
			math_003_1.operation = 'SUBTRACT'
			math_003_1.use_clamp = False
			
			#node Reroute.001
			reroute_001_1 = _cartoon_arrows_scale.nodes.new("NodeReroute")
			reroute_001_1.name = "Reroute.001"
			#node Reroute.010
			reroute_010_1 = _cartoon_arrows_scale.nodes.new("NodeReroute")
			reroute_010_1.name = "Reroute.010"
			#node Switch.001
			switch_001 = _cartoon_arrows_scale.nodes.new("GeometryNodeSwitch")
			switch_001.name = "Switch.001"
			switch_001.input_type = 'FLOAT'
			
			#node Reroute
			reroute_3 = _cartoon_arrows_scale.nodes.new("NodeReroute")
			reroute_3.name = "Reroute"
			#node Spline Length
			spline_length = _cartoon_arrows_scale.nodes.new("GeometryNodeSplineLength")
			spline_length.name = "Spline Length"
			
			#node Group Input
			group_input_17 = _cartoon_arrows_scale.nodes.new("NodeGroupInput")
			group_input_17.name = "Group Input"
			
			#node Math.007
			math_007 = _cartoon_arrows_scale.nodes.new("ShaderNodeMath")
			math_007.name = "Math.007"
			math_007.operation = 'DIVIDE'
			math_007.use_clamp = False
			#Value_001
			math_007.inputs[1].default_value = 100.0
			
			#node Map Range.001
			map_range_001 = _cartoon_arrows_scale.nodes.new("ShaderNodeMapRange")
			map_range_001.name = "Map Range.001"
			map_range_001.clamp = True
			map_range_001.data_type = 'FLOAT'
			map_range_001.interpolation_type = 'LINEAR'
			#To Max
			map_range_001.inputs[4].default_value = 0.0
			
			#node Compare.001
			compare_001 = _cartoon_arrows_scale.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'FLOAT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'EQUAL'
			#Epsilon
			compare_001.inputs[12].default_value = 0.0010000000474974513
			
			#node Math.008
			math_008 = _cartoon_arrows_scale.nodes.new("ShaderNodeMath")
			math_008.name = "Math.008"
			math_008.operation = 'MULTIPLY'
			math_008.use_clamp = False
			#Value_001
			math_008.inputs[1].default_value = 2.0
			
			
			
			
			#Set locations
			group_output_18.location = (670.39453125, 0.0)
			math_006.location = (-283.53955078125, 120.8475341796875)
			spline_parameter.location = (-283.53955078125, 240.8475341796875)
			map_range.location = (-43.53955078125, 140.8475341796875)
			math_003_1.location = (-283.53955078125, 80.8475341796875)
			reroute_001_1.location = (-128.9521484375, -162.76467895507812)
			reroute_010_1.location = (120.39453125, -104.70928955078125)
			switch_001.location = (480.39453125, -44.70928955078125)
			reroute_3.location = (-126.4767837524414, -251.35455322265625)
			spline_length.location = (-480.0, 100.0)
			group_input_17.location = (-700.0, -200.0)
			math_007.location = (-480.0, 20.0)
			map_range_001.location = (160.0, 60.0)
			compare_001.location = (160.0, 240.0)
			math_008.location = (-80.0, -140.0)
			
			#Set dimensions
			group_output_18.width, group_output_18.height = 140.0, 100.0
			math_006.width, math_006.height = 140.0, 100.0
			spline_parameter.width, spline_parameter.height = 140.0, 100.0
			map_range.width, map_range.height = 140.0, 100.0
			math_003_1.width, math_003_1.height = 140.0, 100.0
			reroute_001_1.width, reroute_001_1.height = 16.0, 100.0
			reroute_010_1.width, reroute_010_1.height = 16.0, 100.0
			switch_001.width, switch_001.height = 140.0, 100.0
			reroute_3.width, reroute_3.height = 16.0, 100.0
			spline_length.width, spline_length.height = 140.0, 100.0
			group_input_17.width, group_input_17.height = 140.0, 100.0
			math_007.width, math_007.height = 140.0, 100.0
			map_range_001.width, map_range_001.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			math_008.width, math_008.height = 140.0, 100.0
			
			#initialize _cartoon_arrows_scale links
			#spline_parameter.Length -> map_range.Value
			_cartoon_arrows_scale.links.new(spline_parameter.outputs[1], map_range.inputs[0])
			#reroute_001_1.Output -> map_range.To Min
			_cartoon_arrows_scale.links.new(reroute_001_1.outputs[0], map_range.inputs[3])
			#spline_length.Length -> map_range.From Max
			_cartoon_arrows_scale.links.new(spline_length.outputs[0], map_range.inputs[2])
			#map_range.Result -> map_range_001.Value
			_cartoon_arrows_scale.links.new(map_range.outputs[0], map_range_001.inputs[0])
			#map_range_001.Result -> switch_001.False
			_cartoon_arrows_scale.links.new(map_range_001.outputs[0], switch_001.inputs[1])
			#math_006.Value -> map_range.From Min
			_cartoon_arrows_scale.links.new(math_006.outputs[0], map_range.inputs[1])
			#map_range.Result -> compare_001.A
			_cartoon_arrows_scale.links.new(map_range.outputs[0], compare_001.inputs[0])
			#math_007.Value -> math_003_1.Value
			_cartoon_arrows_scale.links.new(math_007.outputs[0], math_003_1.inputs[1])
			#reroute_3.Output -> map_range_001.From Max
			_cartoon_arrows_scale.links.new(reroute_3.outputs[0], map_range_001.inputs[2])
			#reroute_001_1.Output -> reroute_010_1.Input
			_cartoon_arrows_scale.links.new(reroute_001_1.outputs[0], reroute_010_1.inputs[0])
			#reroute_010_1.Output -> map_range_001.From Min
			_cartoon_arrows_scale.links.new(reroute_010_1.outputs[0], map_range_001.inputs[1])
			#reroute_001_1.Output -> math_008.Value
			_cartoon_arrows_scale.links.new(reroute_001_1.outputs[0], math_008.inputs[0])
			#reroute_010_1.Output -> compare_001.B
			_cartoon_arrows_scale.links.new(reroute_010_1.outputs[0], compare_001.inputs[1])
			#compare_001.Result -> switch_001.Switch
			_cartoon_arrows_scale.links.new(compare_001.outputs[0], switch_001.inputs[0])
			#reroute_010_1.Output -> switch_001.True
			_cartoon_arrows_scale.links.new(reroute_010_1.outputs[0], switch_001.inputs[2])
			#math_003_1.Value -> math_006.Value
			_cartoon_arrows_scale.links.new(math_003_1.outputs[0], math_006.inputs[0])
			#reroute_3.Output -> map_range.To Max
			_cartoon_arrows_scale.links.new(reroute_3.outputs[0], map_range.inputs[4])
			#math_008.Value -> map_range_001.To Min
			_cartoon_arrows_scale.links.new(math_008.outputs[0], map_range_001.inputs[3])
			#spline_length.Length -> math_003_1.Value
			_cartoon_arrows_scale.links.new(spline_length.outputs[0], math_003_1.inputs[0])
			#compare_001.Result -> group_output_18.Result
			_cartoon_arrows_scale.links.new(compare_001.outputs[0], group_output_18.inputs[0])
			#switch_001.Output -> group_output_18.Output
			_cartoon_arrows_scale.links.new(switch_001.outputs[0], group_output_18.inputs[1])
			#group_input_17.Input -> reroute_001_1.Input
			_cartoon_arrows_scale.links.new(group_input_17.outputs[0], reroute_001_1.inputs[0])
			#group_input_17.Input -> reroute_3.Input
			_cartoon_arrows_scale.links.new(group_input_17.outputs[1], reroute_3.inputs[0])
			#group_input_17.Value -> math_007.Value
			_cartoon_arrows_scale.links.new(group_input_17.outputs[2], math_007.inputs[0])
			return _cartoon_arrows_scale

		_cartoon_arrows_scale = _cartoon_arrows_scale_node_group()

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
			curve_socket_3 = _cartoon_arrow_instance.interface.new_socket(name = "Curve", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			curve_socket_3.attribute_domain = 'POINT'
			
			#Socket Instance
			instance_socket = _cartoon_arrow_instance.interface.new_socket(name = "Instance", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			instance_socket.attribute_domain = 'POINT'
			
			#Socket Rotation
			rotation_socket_2 = _cartoon_arrow_instance.interface.new_socket(name = "Rotation", in_out='INPUT', socket_type = 'NodeSocketVector')
			rotation_socket_2.subtype = 'EULER'
			rotation_socket_2.default_value = (0.0, 0.0, 0.0)
			rotation_socket_2.min_value = -3.4028234663852886e+38
			rotation_socket_2.max_value = 3.4028234663852886e+38
			rotation_socket_2.attribute_domain = 'POINT'
			rotation_socket_2.hide_value = True
			
			#Socket Scale
			scale_socket_2 = _cartoon_arrow_instance.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketVector')
			scale_socket_2.subtype = 'XYZ'
			scale_socket_2.default_value = (1.0, 1.0, 1.0)
			scale_socket_2.min_value = -3.4028234663852886e+38
			scale_socket_2.max_value = 3.4028234663852886e+38
			scale_socket_2.attribute_domain = 'POINT'
			
			
			#initialize _cartoon_arrow_instance nodes
			#node Boolean Math.004
			boolean_math_004_1 = _cartoon_arrow_instance.nodes.new("FunctionNodeBooleanMath")
			boolean_math_004_1.name = "Boolean Math.004"
			boolean_math_004_1.operation = 'AND'
			
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
			group_output_19 = _cartoon_arrow_instance.nodes.new("NodeGroupOutput")
			group_output_19.name = "Group Output"
			group_output_19.is_active_output = True
			
			#node Align Euler to Vector
			align_euler_to_vector_1 = _cartoon_arrow_instance.nodes.new("FunctionNodeAlignEulerToVector")
			align_euler_to_vector_1.name = "Align Euler to Vector"
			align_euler_to_vector_1.axis = 'X'
			align_euler_to_vector_1.pivot_axis = 'Y'
			#Factor
			align_euler_to_vector_1.inputs[1].default_value = 1.0
			
			#node Endpoint Selection.001
			endpoint_selection_001_1 = _cartoon_arrow_instance.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_001_1.name = "Endpoint Selection.001"
			#Start Size
			endpoint_selection_001_1.inputs[0].default_value = 0
			#End Size
			endpoint_selection_001_1.inputs[1].default_value = 1
			
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
			boolean_math_003_1 = _cartoon_arrow_instance.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003_1.name = "Boolean Math.003"
			boolean_math_003_1.operation = 'AND'
			
			#node Reroute
			reroute_4 = _cartoon_arrow_instance.nodes.new("NodeReroute")
			reroute_4.name = "Reroute"
			#node Position.001
			position_001_1 = _cartoon_arrow_instance.nodes.new("GeometryNodeInputPosition")
			position_001_1.name = "Position.001"
			
			#node Vector Math
			vector_math_2 = _cartoon_arrow_instance.nodes.new("ShaderNodeVectorMath")
			vector_math_2.name = "Vector Math"
			vector_math_2.operation = 'SUBTRACT'
			
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
			group_input_18 = _cartoon_arrow_instance.nodes.new("NodeGroupInput")
			group_input_18.name = "Group Input"
			
			#node Delete Geometry
			delete_geometry = _cartoon_arrow_instance.nodes.new("GeometryNodeDeleteGeometry")
			delete_geometry.name = "Delete Geometry"
			delete_geometry.domain = 'POINT'
			delete_geometry.mode = 'ALL'
			
			
			
			
			#Set locations
			boolean_math_004_1.location = (-239.0887451171875, 169.322998046875)
			boolean_math_005.location = (-240.0, 22.557861328125)
			reroute_007.location = (-420.0, -200.0)
			instance_on_points.location = (700.0, 180.0)
			group_output_19.location = (1140.0, -20.0)
			align_euler_to_vector_1.location = (260.0, 60.0)
			endpoint_selection_001_1.location = (-660.0, 280.0)
			endpoint_selection.location = (-660.0, 160.0)
			boolean_math_001_2.location = (-440.0, 340.0)
			boolean_math_003_1.location = (-440.0, 220.0)
			reroute_4.location = (-380.0, 0.0)
			position_001_1.location = (-40.0, -140.0)
			vector_math_2.location = (166.50079345703125, -140.0)
			group_006.location = (164.67938232421875, -280.0)
			group_018.location = (-700.0, 20.0)
			group_input_18.location = (-660.0, -180.0)
			delete_geometry.location = (108.09152221679688, -434.36468505859375)
			
			#Set dimensions
			boolean_math_004_1.width, boolean_math_004_1.height = 140.0, 100.0
			boolean_math_005.width, boolean_math_005.height = 140.0, 100.0
			reroute_007.width, reroute_007.height = 16.0, 100.0
			instance_on_points.width, instance_on_points.height = 140.0, 100.0
			group_output_19.width, group_output_19.height = 140.0, 100.0
			align_euler_to_vector_1.width, align_euler_to_vector_1.height = 140.0, 100.0
			endpoint_selection_001_1.width, endpoint_selection_001_1.height = 140.0, 100.0
			endpoint_selection.width, endpoint_selection.height = 140.0, 100.0
			boolean_math_001_2.width, boolean_math_001_2.height = 140.0, 100.0
			boolean_math_003_1.width, boolean_math_003_1.height = 140.0, 100.0
			reroute_4.width, reroute_4.height = 16.0, 100.0
			position_001_1.width, position_001_1.height = 140.0, 100.0
			vector_math_2.width, vector_math_2.height = 233.49920654296875, 100.0
			group_006.width, group_006.height = 235.32061767578125, 100.0
			group_018.width, group_018.height = 234.5810546875, 100.0
			group_input_18.width, group_input_18.height = 140.0, 100.0
			delete_geometry.width, delete_geometry.height = 140.0, 100.0
			
			#initialize _cartoon_arrow_instance links
			#reroute_007.Output -> instance_on_points.Points
			_cartoon_arrow_instance.links.new(reroute_007.outputs[0], instance_on_points.inputs[0])
			#position_001_1.Position -> vector_math_2.Vector
			_cartoon_arrow_instance.links.new(position_001_1.outputs[0], vector_math_2.inputs[0])
			#boolean_math_004_1.Boolean -> instance_on_points.Selection
			_cartoon_arrow_instance.links.new(boolean_math_004_1.outputs[0], instance_on_points.inputs[1])
			#endpoint_selection.Selection -> boolean_math_003_1.Boolean
			_cartoon_arrow_instance.links.new(endpoint_selection.outputs[0], boolean_math_003_1.inputs[1])
			#align_euler_to_vector_1.Rotation -> instance_on_points.Rotation
			_cartoon_arrow_instance.links.new(align_euler_to_vector_1.outputs[0], instance_on_points.inputs[5])
			#endpoint_selection_001_1.Selection -> boolean_math_001_2.Boolean
			_cartoon_arrow_instance.links.new(endpoint_selection_001_1.outputs[0], boolean_math_001_2.inputs[0])
			#boolean_math_005.Boolean -> delete_geometry.Selection
			_cartoon_arrow_instance.links.new(boolean_math_005.outputs[0], delete_geometry.inputs[1])
			#reroute_007.Output -> delete_geometry.Geometry
			_cartoon_arrow_instance.links.new(reroute_007.outputs[0], delete_geometry.inputs[0])
			#endpoint_selection_001_1.Selection -> boolean_math_005.Boolean
			_cartoon_arrow_instance.links.new(endpoint_selection_001_1.outputs[0], boolean_math_005.inputs[0])
			#boolean_math_003_1.Boolean -> boolean_math_004_1.Boolean
			_cartoon_arrow_instance.links.new(boolean_math_003_1.outputs[0], boolean_math_004_1.inputs[0])
			#position_001_1.Position -> group_006.Field
			_cartoon_arrow_instance.links.new(position_001_1.outputs[0], group_006.inputs[0])
			#boolean_math_001_2.Boolean -> boolean_math_003_1.Boolean
			_cartoon_arrow_instance.links.new(boolean_math_001_2.outputs[0], boolean_math_003_1.inputs[0])
			#vector_math_2.Vector -> align_euler_to_vector_1.Vector
			_cartoon_arrow_instance.links.new(vector_math_2.outputs[0], align_euler_to_vector_1.inputs[2])
			#group_input_18.Instance -> instance_on_points.Instance
			_cartoon_arrow_instance.links.new(group_input_18.outputs[1], instance_on_points.inputs[2])
			#group_input_18.Curve -> reroute_007.Input
			_cartoon_arrow_instance.links.new(group_input_18.outputs[0], reroute_007.inputs[0])
			#group_input_18.Rotation -> align_euler_to_vector_1.Rotation
			_cartoon_arrow_instance.links.new(group_input_18.outputs[2], align_euler_to_vector_1.inputs[0])
			#delete_geometry.Geometry -> group_output_19.Trimmed Curve
			_cartoon_arrow_instance.links.new(delete_geometry.outputs[0], group_output_19.inputs[0])
			#instance_on_points.Instances -> group_output_19.ArrowHeads
			_cartoon_arrow_instance.links.new(instance_on_points.outputs[0], group_output_19.inputs[1])
			#group_input_18.Scale -> instance_on_points.Scale
			_cartoon_arrow_instance.links.new(group_input_18.outputs[3], instance_on_points.inputs[6])
			#group_006.Field -> vector_math_2.Vector
			_cartoon_arrow_instance.links.new(group_006.outputs[0], vector_math_2.inputs[1])
			#reroute_4.Output -> boolean_math_004_1.Boolean
			_cartoon_arrow_instance.links.new(reroute_4.outputs[0], boolean_math_004_1.inputs[1])
			#reroute_4.Output -> boolean_math_005.Boolean
			_cartoon_arrow_instance.links.new(reroute_4.outputs[0], boolean_math_005.inputs[1])
			#group_018.Is Sheet -> reroute_4.Input
			_cartoon_arrow_instance.links.new(group_018.outputs[1], reroute_4.inputs[0])
			return _cartoon_arrow_instance

		_cartoon_arrow_instance = _cartoon_arrow_instance_node_group()

		#initialize _cartoon_arrow_primitive node group
		def _cartoon_arrow_primitive_node_group():
			_cartoon_arrow_primitive = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".cartoon.arrow_primitive")

			_cartoon_arrow_primitive.color_tag = 'NONE'
			_cartoon_arrow_primitive.description = ""

			_cartoon_arrow_primitive.is_modifier = True
			
			#_cartoon_arrow_primitive interface
			#Socket Geometry
			geometry_socket_4 = _cartoon_arrow_primitive.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_4.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_3 = _cartoon_arrow_primitive.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket_3.subtype = 'NONE'
			value_socket_3.default_value = 0.5
			value_socket_3.min_value = -10000.0
			value_socket_3.max_value = 10000.0
			value_socket_3.attribute_domain = 'POINT'
			
			
			#initialize _cartoon_arrow_primitive nodes
			#node Group Output
			group_output_20 = _cartoon_arrow_primitive.nodes.new("NodeGroupOutput")
			group_output_20.name = "Group Output"
			group_output_20.is_active_output = True
			
			#node Group Input
			group_input_19 = _cartoon_arrow_primitive.nodes.new("NodeGroupInput")
			group_input_19.name = "Group Input"
			
			#node Transform Geometry
			transform_geometry = _cartoon_arrow_primitive.nodes.new("GeometryNodeTransform")
			transform_geometry.name = "Transform Geometry"
			transform_geometry.mode = 'COMPONENTS'
			#Translation
			transform_geometry.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Rotation
			transform_geometry.inputs[2].default_value = (0.0, 3.1415927410125732, 0.0)
			
			#node Transform Geometry.002
			transform_geometry_002_1 = _cartoon_arrow_primitive.nodes.new("GeometryNodeTransform")
			transform_geometry_002_1.name = "Transform Geometry.002"
			transform_geometry_002_1.mode = 'COMPONENTS'
			#Rotation
			transform_geometry_002_1.inputs[2].default_value = (1.5707963705062866, 0.0, 0.0)
			#Scale
			transform_geometry_002_1.inputs[3].default_value = (1.0, 0.8299999833106995, 1.0)
			
			#node Group.005
			group_005 = _cartoon_arrow_primitive.nodes.new("GeometryNodeGroup")
			group_005.name = "Group.005"
			group_005.node_tree = mn_units
			#Input_1
			group_005.inputs[0].default_value = 3.390000104904175
			
			#node Join Geometry.001
			join_geometry_001_1 = _cartoon_arrow_primitive.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_001_1.name = "Join Geometry.001"
			join_geometry_001_1.hide = True
			
			#node Merge by Distance
			merge_by_distance = _cartoon_arrow_primitive.nodes.new("GeometryNodeMergeByDistance")
			merge_by_distance.name = "Merge by Distance"
			merge_by_distance.hide = True
			merge_by_distance.mode = 'ALL'
			#Selection
			merge_by_distance.inputs[1].default_value = True
			#Distance
			merge_by_distance.inputs[2].default_value = 0.0010000000474974513
			
			#node Mesh Circle
			mesh_circle = _cartoon_arrow_primitive.nodes.new("GeometryNodeMeshCircle")
			mesh_circle.name = "Mesh Circle"
			mesh_circle.fill_type = 'TRIANGLE_FAN'
			#Vertices
			mesh_circle.inputs[0].default_value = 3
			
			#node Combine XYZ.001
			combine_xyz_001 = _cartoon_arrow_primitive.nodes.new("ShaderNodeCombineXYZ")
			combine_xyz_001.name = "Combine XYZ.001"
			
			#node Group.001
			group_001_2 = _cartoon_arrow_primitive.nodes.new("GeometryNodeGroup")
			group_001_2.name = "Group.001"
			group_001_2.node_tree = mn_units
			#Input_1
			group_001_2.inputs[0].default_value = 2.130000114440918
			
			#node Group.011
			group_011 = _cartoon_arrow_primitive.nodes.new("GeometryNodeGroup")
			group_011.name = "Group.011"
			group_011.node_tree = mn_units
			#Input_1
			group_011.inputs[0].default_value = 1.2000000476837158
			
			#node Math.002
			math_002 = _cartoon_arrow_primitive.nodes.new("ShaderNodeMath")
			math_002.name = "Math.002"
			math_002.operation = 'MULTIPLY'
			math_002.use_clamp = False
			#Value_001
			math_002.inputs[1].default_value = 1.399999976158142
			
			#node Reroute
			reroute_5 = _cartoon_arrow_primitive.nodes.new("NodeReroute")
			reroute_5.name = "Reroute"
			#node Reroute.001
			reroute_001_2 = _cartoon_arrow_primitive.nodes.new("NodeReroute")
			reroute_001_2.name = "Reroute.001"
			#node Reroute.002
			reroute_002 = _cartoon_arrow_primitive.nodes.new("NodeReroute")
			reroute_002.name = "Reroute.002"
			#node Combine XYZ.002
			combine_xyz_002 = _cartoon_arrow_primitive.nodes.new("ShaderNodeCombineXYZ")
			combine_xyz_002.name = "Combine XYZ.002"
			#X
			combine_xyz_002.inputs[0].default_value = 1.0
			#Z
			combine_xyz_002.inputs[2].default_value = 1.0
			
			#node Math.001
			math_001_3 = _cartoon_arrow_primitive.nodes.new("ShaderNodeMath")
			math_001_3.label = "x / 2"
			math_001_3.name = "Math.001"
			math_001_3.hide = True
			math_001_3.operation = 'DIVIDE'
			math_001_3.use_clamp = False
			#Value_001
			math_001_3.inputs[1].default_value = 3.059999942779541
			
			#node Math
			math_2 = _cartoon_arrow_primitive.nodes.new("ShaderNodeMath")
			math_2.label = "x / -2"
			math_2.name = "Math"
			math_2.hide = True
			math_2.operation = 'DIVIDE'
			math_2.use_clamp = False
			#Value_001
			math_2.inputs[1].default_value = -19.440000534057617
			
			#node Extrude Mesh
			extrude_mesh = _cartoon_arrow_primitive.nodes.new("GeometryNodeExtrudeMesh")
			extrude_mesh.name = "Extrude Mesh"
			extrude_mesh.mode = 'FACES'
			#Selection
			extrude_mesh.inputs[1].default_value = True
			#Offset
			extrude_mesh.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Individual
			extrude_mesh.inputs[4].default_value = False
			
			
			
			
			#Set locations
			group_output_20.location = (686.1517333984375, 0.0)
			group_input_19.location = (-874.151611328125, 0.0)
			transform_geometry.location = (245.848388671875, -5.45166015625)
			transform_geometry_002_1.location = (-114.151611328125, -45.45166015625)
			group_005.location = (-674.151611328125, 14.54833984375)
			join_geometry_001_1.location = (-434.151611328125, -125.45166015625)
			merge_by_distance.location = (-434.151611328125, -165.45166015625)
			mesh_circle.location = (-674.151611328125, 154.54833984375)
			combine_xyz_001.location = (-274.151611328125, -185.45166015625)
			group_001_2.location = (-674.151611328125, -105.45166015625)
			group_011.location = (-674.151611328125, -245.45166015625)
			math_002.location = (-118.0, -320.0)
			reroute_5.location = (-718.0, -420.0)
			reroute_001_2.location = (-478.0, -600.0)
			reroute_002.location = (-178.0, -600.0)
			combine_xyz_002.location = (242.0, -280.0)
			math_001_3.location = (-438.0, -220.0)
			math_2.location = (-438.0, -300.0)
			extrude_mesh.location = (-434.151611328125, 134.54833984375)
			
			#Set dimensions
			group_output_20.width, group_output_20.height = 140.0, 100.0
			group_input_19.width, group_input_19.height = 140.0, 100.0
			transform_geometry.width, transform_geometry.height = 140.0, 100.0
			transform_geometry_002_1.width, transform_geometry_002_1.height = 140.0, 100.0
			group_005.width, group_005.height = 140.0, 100.0
			join_geometry_001_1.width, join_geometry_001_1.height = 140.0, 100.0
			merge_by_distance.width, merge_by_distance.height = 140.0, 100.0
			mesh_circle.width, mesh_circle.height = 140.0, 100.0
			combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
			group_001_2.width, group_001_2.height = 140.0, 100.0
			group_011.width, group_011.height = 140.0, 100.0
			math_002.width, math_002.height = 140.0, 100.0
			reroute_5.width, reroute_5.height = 16.0, 100.0
			reroute_001_2.width, reroute_001_2.height = 16.0, 100.0
			reroute_002.width, reroute_002.height = 16.0, 100.0
			combine_xyz_002.width, combine_xyz_002.height = 140.0, 100.0
			math_001_3.width, math_001_3.height = 140.0, 100.0
			math_2.width, math_2.height = 140.0, 100.0
			extrude_mesh.width, extrude_mesh.height = 140.0, 100.0
			
			#initialize _cartoon_arrow_primitive links
			#group_005.Angstrom -> math_001_3.Value
			_cartoon_arrow_primitive.links.new(group_005.outputs[0], math_001_3.inputs[0])
			#mesh_circle.Mesh -> extrude_mesh.Mesh
			_cartoon_arrow_primitive.links.new(mesh_circle.outputs[0], extrude_mesh.inputs[0])
			#group_005.Angstrom -> mesh_circle.Radius
			_cartoon_arrow_primitive.links.new(group_005.outputs[0], mesh_circle.inputs[1])
			#math_001_3.Value -> combine_xyz_001.X
			_cartoon_arrow_primitive.links.new(math_001_3.outputs[0], combine_xyz_001.inputs[0])
			#math_002.Value -> combine_xyz_002.Y
			_cartoon_arrow_primitive.links.new(math_002.outputs[0], combine_xyz_002.inputs[1])
			#group_001_2.Angstrom -> math_2.Value
			_cartoon_arrow_primitive.links.new(group_001_2.outputs[0], math_2.inputs[0])
			#math_2.Value -> combine_xyz_001.Z
			_cartoon_arrow_primitive.links.new(math_2.outputs[0], combine_xyz_001.inputs[2])
			#mesh_circle.Mesh -> join_geometry_001_1.Geometry
			_cartoon_arrow_primitive.links.new(mesh_circle.outputs[0], join_geometry_001_1.inputs[0])
			#combine_xyz_001.Vector -> transform_geometry_002_1.Translation
			_cartoon_arrow_primitive.links.new(combine_xyz_001.outputs[0], transform_geometry_002_1.inputs[1])
			#combine_xyz_002.Vector -> transform_geometry.Scale
			_cartoon_arrow_primitive.links.new(combine_xyz_002.outputs[0], transform_geometry.inputs[3])
			#merge_by_distance.Geometry -> transform_geometry_002_1.Geometry
			_cartoon_arrow_primitive.links.new(merge_by_distance.outputs[0], transform_geometry_002_1.inputs[0])
			#join_geometry_001_1.Geometry -> merge_by_distance.Geometry
			_cartoon_arrow_primitive.links.new(join_geometry_001_1.outputs[0], merge_by_distance.inputs[0])
			#group_001_2.Angstrom -> extrude_mesh.Offset Scale
			_cartoon_arrow_primitive.links.new(group_001_2.outputs[0], extrude_mesh.inputs[3])
			#transform_geometry_002_1.Geometry -> transform_geometry.Geometry
			_cartoon_arrow_primitive.links.new(transform_geometry_002_1.outputs[0], transform_geometry.inputs[0])
			#group_011.Angstrom -> combine_xyz_001.Y
			_cartoon_arrow_primitive.links.new(group_011.outputs[0], combine_xyz_001.inputs[1])
			#reroute_002.Output -> math_002.Value
			_cartoon_arrow_primitive.links.new(reroute_002.outputs[0], math_002.inputs[0])
			#transform_geometry.Geometry -> group_output_20.Geometry
			_cartoon_arrow_primitive.links.new(transform_geometry.outputs[0], group_output_20.inputs[0])
			#group_input_19.Value -> reroute_5.Input
			_cartoon_arrow_primitive.links.new(group_input_19.outputs[0], reroute_5.inputs[0])
			#reroute_5.Output -> reroute_001_2.Input
			_cartoon_arrow_primitive.links.new(reroute_5.outputs[0], reroute_001_2.inputs[0])
			#reroute_001_2.Output -> reroute_002.Input
			_cartoon_arrow_primitive.links.new(reroute_001_2.outputs[0], reroute_002.inputs[0])
			#extrude_mesh.Mesh -> join_geometry_001_1.Geometry
			_cartoon_arrow_primitive.links.new(extrude_mesh.outputs[0], join_geometry_001_1.inputs[0])
			return _cartoon_arrow_primitive

		_cartoon_arrow_primitive = _cartoon_arrow_primitive_node_group()

		#initialize _curve_profile_backup node group
		def _curve_profile_backup_node_group():
			_curve_profile_backup = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".curve_profile_backup")

			_curve_profile_backup.color_tag = 'NONE'
			_curve_profile_backup.description = ""

			_curve_profile_backup.is_modifier = True
			
			#_curve_profile_backup interface
			#Socket Output
			output_socket_2 = _curve_profile_backup.interface.new_socket(name = "Output", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			output_socket_2.attribute_domain = 'POINT'
			
			#Socket Input
			input_socket_3 = _curve_profile_backup.interface.new_socket(name = "Input", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			input_socket_3.attribute_domain = 'POINT'
			
			#Socket Resolution
			resolution_socket_1 = _curve_profile_backup.interface.new_socket(name = "Resolution", in_out='INPUT', socket_type = 'NodeSocketInt')
			resolution_socket_1.subtype = 'NONE'
			resolution_socket_1.default_value = 12
			resolution_socket_1.min_value = 3
			resolution_socket_1.max_value = 512
			resolution_socket_1.attribute_domain = 'POINT'
			
			#Socket Radius
			radius_socket = _curve_profile_backup.interface.new_socket(name = "Radius", in_out='INPUT', socket_type = 'NodeSocketFloat')
			radius_socket.subtype = 'DISTANCE'
			radius_socket.default_value = 0.009999999776482582
			radius_socket.min_value = 0.0
			radius_socket.max_value = 3.4028234663852886e+38
			radius_socket.attribute_domain = 'POINT'
			
			#Socket Rotation
			rotation_socket_3 = _curve_profile_backup.interface.new_socket(name = "Rotation", in_out='INPUT', socket_type = 'NodeSocketFloat')
			rotation_socket_3.subtype = 'NONE'
			rotation_socket_3.default_value = 0.0
			rotation_socket_3.min_value = -10000.0
			rotation_socket_3.max_value = 10000.0
			rotation_socket_3.attribute_domain = 'POINT'
			
			
			#initialize _curve_profile_backup nodes
			#node Group Output
			group_output_21 = _curve_profile_backup.nodes.new("NodeGroupOutput")
			group_output_21.name = "Group Output"
			group_output_21.is_active_output = True
			
			#node Compare
			compare_2 = _curve_profile_backup.nodes.new("FunctionNodeCompare")
			compare_2.name = "Compare"
			compare_2.hide = True
			compare_2.data_type = 'INT'
			compare_2.mode = 'ELEMENT'
			compare_2.operation = 'GREATER_THAN'
			#B_INT
			compare_2.inputs[3].default_value = 0
			
			#node Switch
			switch_3 = _curve_profile_backup.nodes.new("GeometryNodeSwitch")
			switch_3.name = "Switch"
			switch_3.input_type = 'GEOMETRY'
			
			#node Domain Size
			domain_size_1 = _curve_profile_backup.nodes.new("GeometryNodeAttributeDomainSize")
			domain_size_1.name = "Domain Size"
			domain_size_1.component = 'CURVE'
			
			#node Reroute.001
			reroute_001_3 = _curve_profile_backup.nodes.new("NodeReroute")
			reroute_001_3.name = "Reroute.001"
			#node Curve Circle
			curve_circle_1 = _curve_profile_backup.nodes.new("GeometryNodeCurvePrimitiveCircle")
			curve_circle_1.name = "Curve Circle"
			curve_circle_1.mode = 'RADIUS'
			
			#node Transform Geometry.001
			transform_geometry_001_1 = _curve_profile_backup.nodes.new("GeometryNodeTransform")
			transform_geometry_001_1.name = "Transform Geometry.001"
			transform_geometry_001_1.mode = 'COMPONENTS'
			#Translation
			transform_geometry_001_1.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Scale
			transform_geometry_001_1.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Combine XYZ
			combine_xyz = _curve_profile_backup.nodes.new("ShaderNodeCombineXYZ")
			combine_xyz.name = "Combine XYZ"
			#X
			combine_xyz.inputs[0].default_value = 0.0
			#Y
			combine_xyz.inputs[1].default_value = 0.0
			
			#node Group Input
			group_input_20 = _curve_profile_backup.nodes.new("NodeGroupInput")
			group_input_20.name = "Group Input"
			
			#node Group
			group_5 = _curve_profile_backup.nodes.new("GeometryNodeGroup")
			group_5.name = "Group"
			group_5.node_tree = mn_units
			
			
			
			
			#Set locations
			group_output_21.location = (320.278564453125, 0.0)
			compare_2.location = (-69.721435546875, 174.23248291015625)
			switch_3.location = (130.278564453125, 214.23248291015625)
			domain_size_1.location = (-77.112060546875, 125.76751708984375)
			reroute_001_3.location = (-130.278564453125, -81.5904541015625)
			curve_circle_1.location = (-77.112060546875, -214.23248291015625)
			transform_geometry_001_1.location = (130.278564453125, -45.76751708984375)
			combine_xyz.location = (-80.0, -360.0)
			group_input_20.location = (-392.2209777832031, -102.58642578125)
			group_5.location = (-380.0, -260.0)
			
			#Set dimensions
			group_output_21.width, group_output_21.height = 140.0, 100.0
			compare_2.width, compare_2.height = 137.39459228515625, 100.0
			switch_3.width, switch_3.height = 140.0, 100.0
			domain_size_1.width, domain_size_1.height = 140.0, 100.0
			reroute_001_3.width, reroute_001_3.height = 16.0, 100.0
			curve_circle_1.width, curve_circle_1.height = 140.0, 100.0
			transform_geometry_001_1.width, transform_geometry_001_1.height = 140.0, 100.0
			combine_xyz.width, combine_xyz.height = 140.0, 100.0
			group_input_20.width, group_input_20.height = 140.0, 100.0
			group_5.width, group_5.height = 140.0, 100.0
			
			#initialize _curve_profile_backup links
			#domain_size_1.Point Count -> compare_2.A
			_curve_profile_backup.links.new(domain_size_1.outputs[0], compare_2.inputs[2])
			#reroute_001_3.Output -> domain_size_1.Geometry
			_curve_profile_backup.links.new(reroute_001_3.outputs[0], domain_size_1.inputs[0])
			#curve_circle_1.Curve -> transform_geometry_001_1.Geometry
			_curve_profile_backup.links.new(curve_circle_1.outputs[0], transform_geometry_001_1.inputs[0])
			#compare_2.Result -> switch_3.Switch
			_curve_profile_backup.links.new(compare_2.outputs[0], switch_3.inputs[0])
			#reroute_001_3.Output -> switch_3.True
			_curve_profile_backup.links.new(reroute_001_3.outputs[0], switch_3.inputs[2])
			#transform_geometry_001_1.Geometry -> switch_3.False
			_curve_profile_backup.links.new(transform_geometry_001_1.outputs[0], switch_3.inputs[1])
			#group_input_20.Input -> reroute_001_3.Input
			_curve_profile_backup.links.new(group_input_20.outputs[0], reroute_001_3.inputs[0])
			#switch_3.Output -> group_output_21.Output
			_curve_profile_backup.links.new(switch_3.outputs[0], group_output_21.inputs[0])
			#group_input_20.Resolution -> curve_circle_1.Resolution
			_curve_profile_backup.links.new(group_input_20.outputs[1], curve_circle_1.inputs[0])
			#combine_xyz.Vector -> transform_geometry_001_1.Rotation
			_curve_profile_backup.links.new(combine_xyz.outputs[0], transform_geometry_001_1.inputs[2])
			#group_input_20.Rotation -> combine_xyz.Z
			_curve_profile_backup.links.new(group_input_20.outputs[3], combine_xyz.inputs[2])
			#group_input_20.Radius -> group_5.Value
			_curve_profile_backup.links.new(group_input_20.outputs[2], group_5.inputs[0])
			#group_5.Angstrom -> curve_circle_1.Radius
			_curve_profile_backup.links.new(group_5.outputs[0], curve_circle_1.inputs[4])
			return _curve_profile_backup

		_curve_profile_backup = _curve_profile_backup_node_group()

		#initialize _curve_custom_profile node group
		def _curve_custom_profile_node_group():
			_curve_custom_profile = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".curve_custom_profile")

			_curve_custom_profile.color_tag = 'NONE'
			_curve_custom_profile.description = ""

			_curve_custom_profile.is_modifier = True
			
			#_curve_custom_profile interface
			#Socket Geometry
			geometry_socket_5 = _curve_custom_profile.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_5.attribute_domain = 'POINT'
			
			#Socket Curve
			curve_socket_4 = _curve_custom_profile.interface.new_socket(name = "Curve", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			curve_socket_4.attribute_domain = 'POINT'
			
			#Socket Profile Resolution
			profile_resolution_socket = _curve_custom_profile.interface.new_socket(name = "Profile Resolution", in_out='INPUT', socket_type = 'NodeSocketInt')
			profile_resolution_socket.subtype = 'NONE'
			profile_resolution_socket.default_value = 4
			profile_resolution_socket.min_value = 3
			profile_resolution_socket.max_value = 512
			profile_resolution_socket.attribute_domain = 'POINT'
			
			#Socket Profile Radius
			profile_radius_socket = _curve_custom_profile.interface.new_socket(name = "Profile Radius", in_out='INPUT', socket_type = 'NodeSocketFloat')
			profile_radius_socket.subtype = 'DISTANCE'
			profile_radius_socket.default_value = 1.0
			profile_radius_socket.min_value = 0.0
			profile_radius_socket.max_value = 3.4028234663852886e+38
			profile_radius_socket.attribute_domain = 'POINT'
			
			#Socket Profile Rotation
			profile_rotation_socket = _curve_custom_profile.interface.new_socket(name = "Profile Rotation", in_out='INPUT', socket_type = 'NodeSocketFloat')
			profile_rotation_socket.subtype = 'NONE'
			profile_rotation_socket.default_value = 0.7853981852531433
			profile_rotation_socket.min_value = -10000.0
			profile_rotation_socket.max_value = 10000.0
			profile_rotation_socket.attribute_domain = 'POINT'
			
			#Socket Instance
			instance_socket_1 = _curve_custom_profile.interface.new_socket(name = "Instance", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			instance_socket_1.attribute_domain = 'POINT'
			
			#Socket Rotation X
			rotation_x_socket = _curve_custom_profile.interface.new_socket(name = "Rotation X", in_out='INPUT', socket_type = 'NodeSocketFloat')
			rotation_x_socket.subtype = 'ANGLE'
			rotation_x_socket.default_value = 0.0
			rotation_x_socket.min_value = -3.4028234663852886e+38
			rotation_x_socket.max_value = 3.4028234663852886e+38
			rotation_x_socket.attribute_domain = 'POINT'
			
			#Socket Scale
			scale_socket_3 = _curve_custom_profile.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketVector')
			scale_socket_3.subtype = 'XYZ'
			scale_socket_3.default_value = (0.33000001311302185, 0.36000001430511475, 0.75)
			scale_socket_3.min_value = -3.4028234663852886e+38
			scale_socket_3.max_value = 3.4028234663852886e+38
			scale_socket_3.attribute_domain = 'POINT'
			
			#Socket Factor
			factor_socket = _curve_custom_profile.interface.new_socket(name = "Factor", in_out='INPUT', socket_type = 'NodeSocketFloat')
			factor_socket.subtype = 'FACTOR'
			factor_socket.default_value = 0.0
			factor_socket.min_value = 0.0
			factor_socket.max_value = 1.0
			factor_socket.attribute_domain = 'POINT'
			
			#Socket Radius
			radius_socket_1 = _curve_custom_profile.interface.new_socket(name = "Radius", in_out='INPUT', socket_type = 'NodeSocketFloat')
			radius_socket_1.subtype = 'DISTANCE'
			radius_socket_1.default_value = 0.004999999888241291
			radius_socket_1.min_value = 0.0
			radius_socket_1.max_value = 3.4028234663852886e+38
			radius_socket_1.attribute_domain = 'POINT'
			
			#Socket Resolution
			resolution_socket_2 = _curve_custom_profile.interface.new_socket(name = "Resolution", in_out='INPUT', socket_type = 'NodeSocketInt')
			resolution_socket_2.subtype = 'NONE'
			resolution_socket_2.default_value = 6
			resolution_socket_2.min_value = 1
			resolution_socket_2.max_value = 2147483647
			resolution_socket_2.attribute_domain = 'POINT'
			
			#Socket Resample
			resample_socket = _curve_custom_profile.interface.new_socket(name = "Resample", in_out='INPUT', socket_type = 'NodeSocketBool')
			resample_socket.attribute_domain = 'POINT'
			
			
			#initialize _curve_custom_profile nodes
			#node Instance on Points.001
			instance_on_points_001 = _curve_custom_profile.nodes.new("GeometryNodeInstanceOnPoints")
			instance_on_points_001.name = "Instance on Points.001"
			#Selection
			instance_on_points_001.inputs[1].default_value = True
			#Pick Instance
			instance_on_points_001.inputs[3].default_value = False
			#Instance Index
			instance_on_points_001.inputs[4].default_value = 0
			
			#node Sample Index.001
			sample_index_001 = _curve_custom_profile.nodes.new("GeometryNodeSampleIndex")
			sample_index_001.name = "Sample Index.001"
			sample_index_001.clamp = False
			sample_index_001.data_type = 'FLOAT_VECTOR'
			sample_index_001.domain = 'POINT'
			
			#node Realize Instances
			realize_instances = _curve_custom_profile.nodes.new("GeometryNodeRealizeInstances")
			realize_instances.name = "Realize Instances"
			#Selection
			realize_instances.inputs[1].default_value = True
			#Realize All
			realize_instances.inputs[2].default_value = True
			#Depth
			realize_instances.inputs[3].default_value = 0
			
			#node Index.003
			index_003 = _curve_custom_profile.nodes.new("GeometryNodeInputIndex")
			index_003.name = "Index.003"
			
			#node Position.001
			position_001_2 = _curve_custom_profile.nodes.new("GeometryNodeInputPosition")
			position_001_2.name = "Position.001"
			
			#node Curve to Mesh
			curve_to_mesh_1 = _curve_custom_profile.nodes.new("GeometryNodeCurveToMesh")
			curve_to_mesh_1.name = "Curve to Mesh"
			#Fill Caps
			curve_to_mesh_1.inputs[2].default_value = True
			
			#node Set Position.002
			set_position_002 = _curve_custom_profile.nodes.new("GeometryNodeSetPosition")
			set_position_002.name = "Set Position.002"
			#Selection
			set_position_002.inputs[1].default_value = True
			#Offset
			set_position_002.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Transform Geometry
			transform_geometry_1 = _curve_custom_profile.nodes.new("GeometryNodeTransform")
			transform_geometry_1.name = "Transform Geometry"
			transform_geometry_1.hide = True
			transform_geometry_1.mode = 'COMPONENTS'
			#Translation
			transform_geometry_1.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Rotation
			transform_geometry_1.inputs[2].default_value = (0.0, 1.5707963705062866, 0.0)
			#Scale
			transform_geometry_1.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Mix.001
			mix_001 = _curve_custom_profile.nodes.new("ShaderNodeMix")
			mix_001.name = "Mix.001"
			mix_001.blend_type = 'MIX'
			mix_001.clamp_factor = True
			mix_001.clamp_result = False
			mix_001.data_type = 'VECTOR'
			mix_001.factor_mode = 'UNIFORM'
			
			#node Flip Faces
			flip_faces = _curve_custom_profile.nodes.new("GeometryNodeFlipFaces")
			flip_faces.name = "Flip Faces"
			#Selection
			flip_faces.inputs[1].default_value = True
			
			#node Group Output
			group_output_22 = _curve_custom_profile.nodes.new("NodeGroupOutput")
			group_output_22.name = "Group Output"
			group_output_22.is_active_output = True
			
			#node Reroute.001
			reroute_001_4 = _curve_custom_profile.nodes.new("NodeReroute")
			reroute_001_4.name = "Reroute.001"
			#node Reroute
			reroute_6 = _curve_custom_profile.nodes.new("NodeReroute")
			reroute_6.name = "Reroute"
			#node Set Curve Radius
			set_curve_radius_1 = _curve_custom_profile.nodes.new("GeometryNodeSetCurveRadius")
			set_curve_radius_1.name = "Set Curve Radius"
			#Selection
			set_curve_radius_1.inputs[1].default_value = True
			
			#node Reroute.002
			reroute_002_1 = _curve_custom_profile.nodes.new("NodeReroute")
			reroute_002_1.name = "Reroute.002"
			#node Spline Resolution
			spline_resolution = _curve_custom_profile.nodes.new("GeometryNodeInputSplineResolution")
			spline_resolution.name = "Spline Resolution"
			
			#node Spline Length
			spline_length_1 = _curve_custom_profile.nodes.new("GeometryNodeSplineLength")
			spline_length_1.name = "Spline Length"
			
			#node Spline Parameter
			spline_parameter_1 = _curve_custom_profile.nodes.new("GeometryNodeSplineParameter")
			spline_parameter_1.name = "Spline Parameter"
			
			#node Group.001
			group_001_3 = _curve_custom_profile.nodes.new("GeometryNodeGroup")
			group_001_3.name = "Group.001"
			group_001_3.node_tree = _curve_profile_backup
			
			#node Set Spline Resolution
			set_spline_resolution = _curve_custom_profile.nodes.new("GeometryNodeSetSplineResolution")
			set_spline_resolution.name = "Set Spline Resolution"
			#Selection
			set_spline_resolution.inputs[1].default_value = True
			
			#node Resample Curve
			resample_curve = _curve_custom_profile.nodes.new("GeometryNodeResampleCurve")
			resample_curve.name = "Resample Curve"
			resample_curve.mode = 'EVALUATED'
			#Selection
			resample_curve.inputs[1].default_value = True
			
			#node Switch
			switch_4 = _curve_custom_profile.nodes.new("GeometryNodeSwitch")
			switch_4.name = "Switch"
			switch_4.input_type = 'GEOMETRY'
			
			#node Group Input
			group_input_21 = _curve_custom_profile.nodes.new("NodeGroupInput")
			group_input_21.name = "Group Input"
			
			#node Group
			group_6 = _curve_custom_profile.nodes.new("GeometryNodeGroup")
			group_6.name = "Group"
			group_6.node_tree = _guide_rotation
			
			
			
			
			#Set locations
			instance_on_points_001.location = (-289.36962890625, 170.0)
			sample_index_001.location = (-89.36962890625, 290.0)
			realize_instances.location = (-89.36962890625, 70.0)
			index_003.location = (-290.0, 270.0)
			position_001_2.location = (-290.0, 330.0)
			curve_to_mesh_1.location = (-100.0, -100.0)
			set_position_002.location = (260.0, 280.0)
			transform_geometry_1.location = (-520.0, -120.0)
			mix_001.location = (70.63037109375, 290.0)
			flip_faces.location = (460.0, 280.0)
			group_output_22.location = (660.0, 280.0)
			reroute_001_4.location = (-140.0, -240.0)
			reroute_6.location = (-539.885986328125, -222.59783935546875)
			set_curve_radius_1.location = (-296.1637268066406, -66.46692657470703)
			reroute_002_1.location = (-635.73388671875, -6.497833251953125)
			spline_resolution.location = (-1100.0, 280.0)
			spline_length_1.location = (-1100.0, 220.0)
			spline_parameter_1.location = (-1100.0, 380.0)
			group_001_3.location = (-900.0, -100.0)
			set_spline_resolution.location = (-1292.002685546875, 99.56741333007812)
			resample_curve.location = (-1124.6309814453125, 107.74668884277344)
			switch_4.location = (-905.0, 111.8224105834961)
			group_input_21.location = (-1608.1519775390625, -81.00050354003906)
			group_6.location = (-500.0, 60.0)
			
			#Set dimensions
			instance_on_points_001.width, instance_on_points_001.height = 140.0, 100.0
			sample_index_001.width, sample_index_001.height = 140.0, 100.0
			realize_instances.width, realize_instances.height = 140.0, 100.0
			index_003.width, index_003.height = 140.0, 100.0
			position_001_2.width, position_001_2.height = 140.0, 100.0
			curve_to_mesh_1.width, curve_to_mesh_1.height = 140.0, 100.0
			set_position_002.width, set_position_002.height = 140.0, 100.0
			transform_geometry_1.width, transform_geometry_1.height = 140.0, 100.0
			mix_001.width, mix_001.height = 140.0, 100.0
			flip_faces.width, flip_faces.height = 140.0, 100.0
			group_output_22.width, group_output_22.height = 140.0, 100.0
			reroute_001_4.width, reroute_001_4.height = 16.0, 100.0
			reroute_6.width, reroute_6.height = 16.0, 100.0
			set_curve_radius_1.width, set_curve_radius_1.height = 140.0, 100.0
			reroute_002_1.width, reroute_002_1.height = 16.0, 100.0
			spline_resolution.width, spline_resolution.height = 140.0, 100.0
			spline_length_1.width, spline_length_1.height = 140.0, 100.0
			spline_parameter_1.width, spline_parameter_1.height = 140.0, 100.0
			group_001_3.width, group_001_3.height = 140.0, 100.0
			set_spline_resolution.width, set_spline_resolution.height = 140.0, 100.0
			resample_curve.width, resample_curve.height = 140.0, 100.0
			switch_4.width, switch_4.height = 140.0, 100.0
			group_input_21.width, group_input_21.height = 140.0, 100.0
			group_6.width, group_6.height = 140.0, 100.0
			
			#initialize _curve_custom_profile links
			#mix_001.Result -> set_position_002.Position
			_curve_custom_profile.links.new(mix_001.outputs[1], set_position_002.inputs[2])
			#index_003.Index -> sample_index_001.Index
			_curve_custom_profile.links.new(index_003.outputs[0], sample_index_001.inputs[2])
			#position_001_2.Position -> mix_001.B
			_curve_custom_profile.links.new(position_001_2.outputs[0], mix_001.inputs[5])
			#set_curve_radius_1.Curve -> curve_to_mesh_1.Curve
			_curve_custom_profile.links.new(set_curve_radius_1.outputs[0], curve_to_mesh_1.inputs[0])
			#curve_to_mesh_1.Mesh -> set_position_002.Geometry
			_curve_custom_profile.links.new(curve_to_mesh_1.outputs[0], set_position_002.inputs[0])
			#instance_on_points_001.Instances -> realize_instances.Geometry
			_curve_custom_profile.links.new(instance_on_points_001.outputs[0], realize_instances.inputs[0])
			#sample_index_001.Value -> mix_001.A
			_curve_custom_profile.links.new(sample_index_001.outputs[0], mix_001.inputs[4])
			#position_001_2.Position -> sample_index_001.Value
			_curve_custom_profile.links.new(position_001_2.outputs[0], sample_index_001.inputs[1])
			#realize_instances.Geometry -> sample_index_001.Geometry
			_curve_custom_profile.links.new(realize_instances.outputs[0], sample_index_001.inputs[0])
			#group_input_21.Radius -> set_curve_radius_1.Radius
			_curve_custom_profile.links.new(group_input_21.outputs[8], set_curve_radius_1.inputs[2])
			#group_input_21.Factor -> mix_001.Factor
			_curve_custom_profile.links.new(group_input_21.outputs[7], mix_001.inputs[0])
			#flip_faces.Mesh -> group_output_22.Geometry
			_curve_custom_profile.links.new(flip_faces.outputs[0], group_output_22.inputs[0])
			#reroute_6.Output -> transform_geometry_1.Geometry
			_curve_custom_profile.links.new(reroute_6.outputs[0], transform_geometry_1.inputs[0])
			#transform_geometry_1.Geometry -> instance_on_points_001.Instance
			_curve_custom_profile.links.new(transform_geometry_1.outputs[0], instance_on_points_001.inputs[2])
			#reroute_001_4.Output -> curve_to_mesh_1.Profile Curve
			_curve_custom_profile.links.new(reroute_001_4.outputs[0], curve_to_mesh_1.inputs[1])
			#group_input_21.Scale -> instance_on_points_001.Scale
			_curve_custom_profile.links.new(group_input_21.outputs[6], instance_on_points_001.inputs[6])
			#group_input_21.Rotation X -> group_6.Angle
			_curve_custom_profile.links.new(group_input_21.outputs[5], group_6.inputs[0])
			#group_001_3.Output -> reroute_6.Input
			_curve_custom_profile.links.new(group_001_3.outputs[0], reroute_6.inputs[0])
			#group_input_21.Instance -> group_001_3.Input
			_curve_custom_profile.links.new(group_input_21.outputs[4], group_001_3.inputs[0])
			#group_input_21.Profile Radius -> group_001_3.Radius
			_curve_custom_profile.links.new(group_input_21.outputs[2], group_001_3.inputs[2])
			#group_input_21.Profile Rotation -> group_001_3.Rotation
			_curve_custom_profile.links.new(group_input_21.outputs[3], group_001_3.inputs[3])
			#set_position_002.Geometry -> flip_faces.Mesh
			_curve_custom_profile.links.new(set_position_002.outputs[0], flip_faces.inputs[0])
			#reroute_002_1.Output -> set_curve_radius_1.Curve
			_curve_custom_profile.links.new(reroute_002_1.outputs[0], set_curve_radius_1.inputs[0])
			#reroute_6.Output -> reroute_001_4.Input
			_curve_custom_profile.links.new(reroute_6.outputs[0], reroute_001_4.inputs[0])
			#group_input_21.Curve -> set_spline_resolution.Geometry
			_curve_custom_profile.links.new(group_input_21.outputs[0], set_spline_resolution.inputs[0])
			#switch_4.Output -> reroute_002_1.Input
			_curve_custom_profile.links.new(switch_4.outputs[0], reroute_002_1.inputs[0])
			#group_input_21.Profile Resolution -> group_001_3.Resolution
			_curve_custom_profile.links.new(group_input_21.outputs[1], group_001_3.inputs[1])
			#reroute_002_1.Output -> instance_on_points_001.Points
			_curve_custom_profile.links.new(reroute_002_1.outputs[0], instance_on_points_001.inputs[0])
			#group_input_21.Resolution -> set_spline_resolution.Resolution
			_curve_custom_profile.links.new(group_input_21.outputs[9], set_spline_resolution.inputs[2])
			#set_spline_resolution.Geometry -> resample_curve.Curve
			_curve_custom_profile.links.new(set_spline_resolution.outputs[0], resample_curve.inputs[0])
			#group_6.Rotation -> instance_on_points_001.Rotation
			_curve_custom_profile.links.new(group_6.outputs[0], instance_on_points_001.inputs[5])
			#resample_curve.Curve -> switch_4.True
			_curve_custom_profile.links.new(resample_curve.outputs[0], switch_4.inputs[2])
			#group_input_21.Curve -> switch_4.False
			_curve_custom_profile.links.new(group_input_21.outputs[0], switch_4.inputs[1])
			#group_input_21.Resample -> switch_4.Switch
			_curve_custom_profile.links.new(group_input_21.outputs[10], switch_4.inputs[0])
			return _curve_custom_profile

		_curve_custom_profile = _curve_custom_profile_node_group()

		#initialize _field_offset node group
		def _field_offset_node_group():
			_field_offset = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".field_offset")

			_field_offset.color_tag = 'NONE'
			_field_offset.description = ""

			
			#_field_offset interface
			#Socket Field
			field_socket_2 = _field_offset.interface.new_socket(name = "Field", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			field_socket_2.subtype = 'NONE'
			field_socket_2.default_value = (0.0, 0.0, 0.0)
			field_socket_2.min_value = -3.4028234663852886e+38
			field_socket_2.max_value = 3.4028234663852886e+38
			field_socket_2.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_4 = _field_offset.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			value_socket_4.attribute_domain = 'POINT'
			
			#Socket Field
			field_socket_3 = _field_offset.interface.new_socket(name = "Field", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			field_socket_3.subtype = 'NONE'
			field_socket_3.default_value = 0
			field_socket_3.min_value = -2147483648
			field_socket_3.max_value = 2147483647
			field_socket_3.attribute_domain = 'POINT'
			
			#Socket Field
			field_socket_4 = _field_offset.interface.new_socket(name = "Field", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			field_socket_4.subtype = 'NONE'
			field_socket_4.default_value = 0.0
			field_socket_4.min_value = -3.4028234663852886e+38
			field_socket_4.max_value = 3.4028234663852886e+38
			field_socket_4.attribute_domain = 'POINT'
			
			#Socket Field
			field_socket_5 = _field_offset.interface.new_socket(name = "Field", in_out='INPUT', socket_type = 'NodeSocketVector')
			field_socket_5.subtype = 'NONE'
			field_socket_5.default_value = (0.0, 0.0, 0.0)
			field_socket_5.min_value = -3.4028234663852886e+38
			field_socket_5.max_value = 3.4028234663852886e+38
			field_socket_5.attribute_domain = 'POINT'
			field_socket_5.hide_value = True
			
			#Socket Value
			value_socket_5 = _field_offset.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketBool')
			value_socket_5.attribute_domain = 'POINT'
			value_socket_5.hide_value = True
			
			#Socket Field
			field_socket_6 = _field_offset.interface.new_socket(name = "Field", in_out='INPUT', socket_type = 'NodeSocketInt')
			field_socket_6.subtype = 'NONE'
			field_socket_6.default_value = 0
			field_socket_6.min_value = -2147483648
			field_socket_6.max_value = 2147483647
			field_socket_6.attribute_domain = 'POINT'
			field_socket_6.hide_value = True
			
			#Socket Field
			field_socket_7 = _field_offset.interface.new_socket(name = "Field", in_out='INPUT', socket_type = 'NodeSocketFloat')
			field_socket_7.subtype = 'NONE'
			field_socket_7.default_value = 0.0
			field_socket_7.min_value = -3.4028234663852886e+38
			field_socket_7.max_value = 3.4028234663852886e+38
			field_socket_7.attribute_domain = 'POINT'
			field_socket_7.hide_value = True
			
			#Socket Offset
			offset_socket_4 = _field_offset.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket_4.subtype = 'NONE'
			offset_socket_4.default_value = 0
			offset_socket_4.min_value = -2147483648
			offset_socket_4.max_value = 2147483647
			offset_socket_4.attribute_domain = 'POINT'
			
			
			#initialize _field_offset nodes
			#node Group Output
			group_output_23 = _field_offset.nodes.new("NodeGroupOutput")
			group_output_23.name = "Group Output"
			group_output_23.is_active_output = True
			
			#node Math.001
			math_001_4 = _field_offset.nodes.new("ShaderNodeMath")
			math_001_4.name = "Math.001"
			math_001_4.operation = 'ADD'
			math_001_4.use_clamp = False
			
			#node Evaluate at Index
			evaluate_at_index_1 = _field_offset.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_1.name = "Evaluate at Index"
			evaluate_at_index_1.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_1.domain = 'POINT'
			
			#node Group Input
			group_input_22 = _field_offset.nodes.new("NodeGroupInput")
			group_input_22.name = "Group Input"
			
			#node Evaluate at Index.001
			evaluate_at_index_001_1 = _field_offset.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001_1.name = "Evaluate at Index.001"
			evaluate_at_index_001_1.data_type = 'BOOLEAN'
			evaluate_at_index_001_1.domain = 'POINT'
			
			#node Index
			index_2 = _field_offset.nodes.new("GeometryNodeInputIndex")
			index_2.name = "Index"
			
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
			group_output_23.location = (407.6440124511719, 0.0)
			math_001_4.location = (0.5235366821289062, 15.3753662109375)
			evaluate_at_index_1.location = (217.64404296875, 102.376708984375)
			group_input_22.location = (-417.64404296875, 0.0)
			evaluate_at_index_001_1.location = (220.0, -60.0)
			index_2.location = (-260.0, -40.0)
			evaluate_at_index_002.location = (220.0, -220.0)
			evaluate_at_index_003.location = (220.0, -380.0)
			
			#Set dimensions
			group_output_23.width, group_output_23.height = 140.0, 100.0
			math_001_4.width, math_001_4.height = 140.0, 100.0
			evaluate_at_index_1.width, evaluate_at_index_1.height = 140.0, 100.0
			group_input_22.width, group_input_22.height = 140.0, 100.0
			evaluate_at_index_001_1.width, evaluate_at_index_001_1.height = 140.0, 100.0
			index_2.width, index_2.height = 140.0, 100.0
			evaluate_at_index_002.width, evaluate_at_index_002.height = 140.0, 100.0
			evaluate_at_index_003.width, evaluate_at_index_003.height = 140.0, 100.0
			
			#initialize _field_offset links
			#index_2.Index -> math_001_4.Value
			_field_offset.links.new(index_2.outputs[0], math_001_4.inputs[0])
			#math_001_4.Value -> evaluate_at_index_1.Index
			_field_offset.links.new(math_001_4.outputs[0], evaluate_at_index_1.inputs[0])
			#group_input_22.Field -> evaluate_at_index_1.Value
			_field_offset.links.new(group_input_22.outputs[0], evaluate_at_index_1.inputs[1])
			#group_input_22.Offset -> math_001_4.Value
			_field_offset.links.new(group_input_22.outputs[4], math_001_4.inputs[1])
			#evaluate_at_index_1.Value -> group_output_23.Field
			_field_offset.links.new(evaluate_at_index_1.outputs[0], group_output_23.inputs[0])
			#math_001_4.Value -> evaluate_at_index_001_1.Index
			_field_offset.links.new(math_001_4.outputs[0], evaluate_at_index_001_1.inputs[0])
			#group_input_22.Value -> evaluate_at_index_001_1.Value
			_field_offset.links.new(group_input_22.outputs[1], evaluate_at_index_001_1.inputs[1])
			#evaluate_at_index_001_1.Value -> group_output_23.Value
			_field_offset.links.new(evaluate_at_index_001_1.outputs[0], group_output_23.inputs[1])
			#math_001_4.Value -> evaluate_at_index_002.Index
			_field_offset.links.new(math_001_4.outputs[0], evaluate_at_index_002.inputs[0])
			#group_input_22.Field -> evaluate_at_index_002.Value
			_field_offset.links.new(group_input_22.outputs[2], evaluate_at_index_002.inputs[1])
			#evaluate_at_index_002.Value -> group_output_23.Field
			_field_offset.links.new(evaluate_at_index_002.outputs[0], group_output_23.inputs[2])
			#math_001_4.Value -> evaluate_at_index_003.Index
			_field_offset.links.new(math_001_4.outputs[0], evaluate_at_index_003.inputs[0])
			#group_input_22.Field -> evaluate_at_index_003.Value
			_field_offset.links.new(group_input_22.outputs[3], evaluate_at_index_003.inputs[1])
			#evaluate_at_index_003.Value -> group_output_23.Field
			_field_offset.links.new(evaluate_at_index_003.outputs[0], group_output_23.inputs[3])
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
			group_input_23 = _sec_struct_counter.nodes.new("NodeGroupInput")
			group_input_23.name = "Group Input"
			
			#node Reroute.005
			reroute_005 = _sec_struct_counter.nodes.new("NodeReroute")
			reroute_005.name = "Reroute.005"
			#node Named Attribute.001
			named_attribute_001_3 = _sec_struct_counter.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001_3.name = "Named Attribute.001"
			named_attribute_001_3.data_type = 'INT'
			#Name
			named_attribute_001_3.inputs[0].default_value = "sec_struct"
			
			#node Group.004
			group_004_1 = _sec_struct_counter.nodes.new("GeometryNodeGroup")
			group_004_1.name = "Group.004"
			group_004_1.node_tree = _field_offset
			#Input_0
			group_004_1.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Input_3
			group_004_1.inputs[1].default_value = False
			#Input_7
			group_004_1.inputs[3].default_value = 0.0
			#Input_1
			group_004_1.inputs[4].default_value = -1
			
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
			reroute_7 = _sec_struct_counter.nodes.new("NodeReroute")
			reroute_7.name = "Reroute"
			#node Boolean Math
			boolean_math_1 = _sec_struct_counter.nodes.new("FunctionNodeBooleanMath")
			boolean_math_1.name = "Boolean Math"
			boolean_math_1.operation = 'OR'
			#Boolean_001
			boolean_math_1.inputs[1].default_value = False
			
			#node Group Output
			group_output_24 = _sec_struct_counter.nodes.new("NodeGroupOutput")
			group_output_24.name = "Group Output"
			group_output_24.is_active_output = True
			
			#node Group.003
			group_003_1 = _sec_struct_counter.nodes.new("GeometryNodeGroup")
			group_003_1.name = "Group.003"
			group_003_1.node_tree = _field_offset
			#Input_0
			group_003_1.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Input_3
			group_003_1.inputs[1].default_value = False
			#Input_7
			group_003_1.inputs[3].default_value = 0.0
			#Input_1
			group_003_1.inputs[4].default_value = 1
			
			
			
			
			#Set locations
			group_input_23.location = (-500.1279296875, 0.0)
			reroute_005.location = (-119.8720703125, -60.0)
			named_attribute_001_3.location = (-300.0, 120.0)
			group_004_1.location = (-20.0, -220.0)
			compare_009.location = (140.1279296875, 60.0)
			accumulate_field_004.location = (460.0, 40.0)
			compare_010.location = (140.0, -140.0)
			reroute_7.location = (320.0, -60.0)
			boolean_math_1.location = (300.0, -140.0)
			group_output_24.location = (796.4706420898438, 27.943008422851562)
			group_003_1.location = (-19.8720703125, 60.0)
			
			#Set dimensions
			group_input_23.width, group_input_23.height = 140.0, 100.0
			reroute_005.width, reroute_005.height = 16.0, 100.0
			named_attribute_001_3.width, named_attribute_001_3.height = 140.0, 100.0
			group_004_1.width, group_004_1.height = 140.0, 100.0
			compare_009.width, compare_009.height = 140.0, 100.0
			accumulate_field_004.width, accumulate_field_004.height = 140.0, 100.0
			compare_010.width, compare_010.height = 140.0, 100.0
			reroute_7.width, reroute_7.height = 16.0, 100.0
			boolean_math_1.width, boolean_math_1.height = 140.0, 100.0
			group_output_24.width, group_output_24.height = 140.0, 100.0
			group_003_1.width, group_003_1.height = 140.0, 100.0
			
			#initialize _sec_struct_counter links
			#reroute_7.Output -> accumulate_field_004.Value
			_sec_struct_counter.links.new(reroute_7.outputs[0], accumulate_field_004.inputs[0])
			#reroute_005.Output -> group_003_1.Field
			_sec_struct_counter.links.new(reroute_005.outputs[0], group_003_1.inputs[2])
			#reroute_005.Output -> compare_009.A
			_sec_struct_counter.links.new(reroute_005.outputs[0], compare_009.inputs[2])
			#named_attribute_001_3.Attribute -> reroute_005.Input
			_sec_struct_counter.links.new(named_attribute_001_3.outputs[0], reroute_005.inputs[0])
			#group_003_1.Field -> compare_009.B
			_sec_struct_counter.links.new(group_003_1.outputs[2], compare_009.inputs[3])
			#accumulate_field_004.Trailing -> group_output_24.Trailing
			_sec_struct_counter.links.new(accumulate_field_004.outputs[1], group_output_24.inputs[1])
			#accumulate_field_004.Leading -> group_output_24.Leading
			_sec_struct_counter.links.new(accumulate_field_004.outputs[0], group_output_24.inputs[0])
			#accumulate_field_004.Total -> group_output_24.Total
			_sec_struct_counter.links.new(accumulate_field_004.outputs[2], group_output_24.inputs[2])
			#reroute_7.Output -> group_output_24.Border
			_sec_struct_counter.links.new(reroute_7.outputs[0], group_output_24.inputs[3])
			#reroute_005.Output -> group_004_1.Field
			_sec_struct_counter.links.new(reroute_005.outputs[0], group_004_1.inputs[2])
			#reroute_005.Output -> compare_010.A
			_sec_struct_counter.links.new(reroute_005.outputs[0], compare_010.inputs[2])
			#group_004_1.Field -> compare_010.B
			_sec_struct_counter.links.new(group_004_1.outputs[2], compare_010.inputs[3])
			#compare_009.Result -> reroute_7.Input
			_sec_struct_counter.links.new(compare_009.outputs[0], reroute_7.inputs[0])
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
			geometry_socket_6 = _bs_smooth.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_6.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_7 = _bs_smooth.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_7.attribute_domain = 'POINT'
			
			#Socket Factor
			factor_socket_1 = _bs_smooth.interface.new_socket(name = "Factor", in_out='INPUT', socket_type = 'NodeSocketFloat')
			factor_socket_1.subtype = 'FACTOR'
			factor_socket_1.default_value = 1.0
			factor_socket_1.min_value = 0.0
			factor_socket_1.max_value = 1.0
			factor_socket_1.attribute_domain = 'POINT'
			
			#Socket Iterations
			iterations_socket = _bs_smooth.interface.new_socket(name = "Iterations", in_out='INPUT', socket_type = 'NodeSocketInt')
			iterations_socket.subtype = 'NONE'
			iterations_socket.default_value = 2
			iterations_socket.min_value = 0
			iterations_socket.max_value = 2147483647
			iterations_socket.attribute_domain = 'POINT'
			
			
			#initialize _bs_smooth nodes
			#node Group Output
			group_output_25 = _bs_smooth.nodes.new("NodeGroupOutput")
			group_output_25.name = "Group Output"
			group_output_25.is_active_output = True
			
			#node Set Position
			set_position_2 = _bs_smooth.nodes.new("GeometryNodeSetPosition")
			set_position_2.name = "Set Position"
			#Offset
			set_position_2.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Mix.002
			mix_002 = _bs_smooth.nodes.new("ShaderNodeMix")
			mix_002.name = "Mix.002"
			mix_002.blend_type = 'MIX'
			mix_002.clamp_factor = True
			mix_002.clamp_result = False
			mix_002.data_type = 'VECTOR'
			mix_002.factor_mode = 'UNIFORM'
			
			#node Position.001
			position_001_3 = _bs_smooth.nodes.new("GeometryNodeInputPosition")
			position_001_3.name = "Position.001"
			
			#node Blur Attribute
			blur_attribute = _bs_smooth.nodes.new("GeometryNodeBlurAttribute")
			blur_attribute.name = "Blur Attribute"
			blur_attribute.data_type = 'FLOAT_VECTOR'
			
			#node Group Input
			group_input_24 = _bs_smooth.nodes.new("NodeGroupInput")
			group_input_24.name = "Group Input"
			
			#node Boolean Math.004
			boolean_math_004_2 = _bs_smooth.nodes.new("FunctionNodeBooleanMath")
			boolean_math_004_2.name = "Boolean Math.004"
			boolean_math_004_2.operation = 'NOT'
			
			#node Boolean Math.002
			boolean_math_002_1 = _bs_smooth.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_1.name = "Boolean Math.002"
			boolean_math_002_1.operation = 'AND'
			
			#node Group
			group_7 = _bs_smooth.nodes.new("GeometryNodeGroup")
			group_7.name = "Group"
			group_7.node_tree = _sec_struct_counter
			
			#node Endpoint Selection.004
			endpoint_selection_004_1 = _bs_smooth.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_004_1.name = "Endpoint Selection.004"
			#Start Size
			endpoint_selection_004_1.inputs[0].default_value = 1
			#End Size
			endpoint_selection_004_1.inputs[1].default_value = 1
			
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
			group_output_25.location = (591.18408203125, 0.0)
			set_position_2.location = (401.18408203125, 199.23532104492188)
			mix_002.location = (218.81591796875, 80.76467895507812)
			position_001_3.location = (-61.18408203125, -39.235321044921875)
			blur_attribute.location = (-58.81591796875, -120.76467895507812)
			group_input_24.location = (-615.6842041015625, 115.17381286621094)
			boolean_math_004_2.location = (-380.0, -160.0)
			boolean_math_002_1.location = (39.807212829589844, 161.80430603027344)
			group_7.location = (-620.0, -40.0)
			endpoint_selection_004_1.location = (-620.0, -280.0)
			boolean_math_2.location = (-120.0, 140.0)
			group_021.location = (40.0, 260.0)
			
			#Set dimensions
			group_output_25.width, group_output_25.height = 140.0, 100.0
			set_position_2.width, set_position_2.height = 140.0, 100.0
			mix_002.width, mix_002.height = 140.0, 100.0
			position_001_3.width, position_001_3.height = 140.0, 100.0
			blur_attribute.width, blur_attribute.height = 140.0, 100.0
			group_input_24.width, group_input_24.height = 140.0, 100.0
			boolean_math_004_2.width, boolean_math_004_2.height = 140.0, 100.0
			boolean_math_002_1.width, boolean_math_002_1.height = 140.0, 100.0
			group_7.width, group_7.height = 140.0, 100.0
			endpoint_selection_004_1.width, endpoint_selection_004_1.height = 140.0, 100.0
			boolean_math_2.width, boolean_math_2.height = 140.0, 100.0
			group_021.width, group_021.height = 140.0, 100.0
			
			#initialize _bs_smooth links
			#boolean_math_004_2.Boolean -> blur_attribute.Weight
			_bs_smooth.links.new(boolean_math_004_2.outputs[0], blur_attribute.inputs[2])
			#blur_attribute.Value -> mix_002.B
			_bs_smooth.links.new(blur_attribute.outputs[0], mix_002.inputs[5])
			#position_001_3.Position -> blur_attribute.Value
			_bs_smooth.links.new(position_001_3.outputs[0], blur_attribute.inputs[0])
			#mix_002.Result -> set_position_2.Position
			_bs_smooth.links.new(mix_002.outputs[1], set_position_2.inputs[2])
			#position_001_3.Position -> mix_002.A
			_bs_smooth.links.new(position_001_3.outputs[0], mix_002.inputs[4])
			#group_021.Is Sheet -> boolean_math_002_1.Boolean
			_bs_smooth.links.new(group_021.outputs[1], boolean_math_002_1.inputs[0])
			#group_input_24.Geometry -> set_position_2.Geometry
			_bs_smooth.links.new(group_input_24.outputs[0], set_position_2.inputs[0])
			#group_input_24.Factor -> mix_002.Factor
			_bs_smooth.links.new(group_input_24.outputs[1], mix_002.inputs[0])
			#set_position_2.Geometry -> group_output_25.Geometry
			_bs_smooth.links.new(set_position_2.outputs[0], group_output_25.inputs[0])
			#group_input_24.Iterations -> blur_attribute.Iterations
			_bs_smooth.links.new(group_input_24.outputs[2], blur_attribute.inputs[1])
			#group_7.Border -> boolean_math_2.Boolean
			_bs_smooth.links.new(group_7.outputs[3], boolean_math_2.inputs[0])
			#boolean_math_002_1.Boolean -> set_position_2.Selection
			_bs_smooth.links.new(boolean_math_002_1.outputs[0], set_position_2.inputs[1])
			#boolean_math_2.Boolean -> boolean_math_002_1.Boolean
			_bs_smooth.links.new(boolean_math_2.outputs[0], boolean_math_002_1.inputs[1])
			#group_7.Border -> boolean_math_004_2.Boolean
			_bs_smooth.links.new(group_7.outputs[3], boolean_math_004_2.inputs[0])
			return _bs_smooth

		_bs_smooth = _bs_smooth_node_group()

		#initialize _expand_selection node group
		def _expand_selection_node_group():
			_expand_selection = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".expand_selection")

			_expand_selection.color_tag = 'NONE'
			_expand_selection.description = ""

			
			#_expand_selection interface
			#Socket Boolean
			boolean_socket_2 = _expand_selection.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket_2.attribute_domain = 'POINT'
			
			#Socket Input
			input_socket_4 = _expand_selection.interface.new_socket(name = "Input", in_out='INPUT', socket_type = 'NodeSocketBool')
			input_socket_4.attribute_domain = 'POINT'
			
			#Socket Offset
			offset_socket_5 = _expand_selection.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket_5.subtype = 'NONE'
			offset_socket_5.default_value = 1
			offset_socket_5.min_value = -2147483648
			offset_socket_5.max_value = 2147483647
			offset_socket_5.attribute_domain = 'POINT'
			
			
			#initialize _expand_selection nodes
			#node Group Output
			group_output_26 = _expand_selection.nodes.new("NodeGroupOutput")
			group_output_26.name = "Group Output"
			group_output_26.is_active_output = True
			
			#node Boolean Math
			boolean_math_3 = _expand_selection.nodes.new("FunctionNodeBooleanMath")
			boolean_math_3.name = "Boolean Math"
			boolean_math_3.operation = 'OR'
			
			#node Boolean Math.001
			boolean_math_001_3 = _expand_selection.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_3.name = "Boolean Math.001"
			boolean_math_001_3.operation = 'OR'
			
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
			group_input_25 = _expand_selection.nodes.new("NodeGroupInput")
			group_input_25.name = "Group Input"
			
			#node Math
			math_3 = _expand_selection.nodes.new("ShaderNodeMath")
			math_3.name = "Math"
			math_3.operation = 'MULTIPLY'
			math_3.use_clamp = False
			#Value_001
			math_3.inputs[1].default_value = -1.0
			
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
			group_output_26.location = (420.0, 0.0)
			boolean_math_3.location = (-50.0, 0.0)
			boolean_math_001_3.location = (230.0, 60.0)
			group_025.location = (-230.0, -140.0)
			group_input_25.location = (-637.21630859375, 234.8535614013672)
			math_3.location = (-640.0, 120.0)
			group_024.location = (-230.0, 140.0)
			
			#Set dimensions
			group_output_26.width, group_output_26.height = 140.0, 100.0
			boolean_math_3.width, boolean_math_3.height = 140.0, 100.0
			boolean_math_001_3.width, boolean_math_001_3.height = 140.0, 100.0
			group_025.width, group_025.height = 140.0, 100.0
			group_input_25.width, group_input_25.height = 140.0, 100.0
			math_3.width, math_3.height = 140.0, 100.0
			group_024.width, group_024.height = 140.0, 100.0
			
			#initialize _expand_selection links
			#group_025.Value -> boolean_math_3.Boolean
			_expand_selection.links.new(group_025.outputs[1], boolean_math_3.inputs[1])
			#group_input_25.Input -> group_025.Value
			_expand_selection.links.new(group_input_25.outputs[0], group_025.inputs[1])
			#group_input_25.Input -> group_024.Value
			_expand_selection.links.new(group_input_25.outputs[0], group_024.inputs[1])
			#group_024.Value -> boolean_math_3.Boolean
			_expand_selection.links.new(group_024.outputs[1], boolean_math_3.inputs[0])
			#boolean_math_3.Boolean -> boolean_math_001_3.Boolean
			_expand_selection.links.new(boolean_math_3.outputs[0], boolean_math_001_3.inputs[1])
			#group_input_25.Input -> boolean_math_001_3.Boolean
			_expand_selection.links.new(group_input_25.outputs[0], boolean_math_001_3.inputs[0])
			#boolean_math_001_3.Boolean -> group_output_26.Boolean
			_expand_selection.links.new(boolean_math_001_3.outputs[0], group_output_26.inputs[0])
			#group_input_25.Offset -> group_024.Offset
			_expand_selection.links.new(group_input_25.outputs[1], group_024.inputs[4])
			#group_input_25.Offset -> math_3.Value
			_expand_selection.links.new(group_input_25.outputs[1], math_3.inputs[0])
			#math_3.Value -> group_025.Offset
			_expand_selection.links.new(math_3.outputs[0], group_025.inputs[4])
			return _expand_selection

		_expand_selection = _expand_selection_node_group()

		#initialize fallback_boolean node group
		def fallback_boolean_node_group():
			fallback_boolean = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Fallback Boolean")

			fallback_boolean.color_tag = 'INPUT'
			fallback_boolean.description = "Computes the boolean field if the given attribute doesn't exist. If it doesn't exist it just uses the attribute instead"

			
			#fallback_boolean interface
			#Socket Boolean
			boolean_socket_3 = fallback_boolean.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket_3.attribute_domain = 'POINT'
			
			#Socket Name
			name_socket = fallback_boolean.interface.new_socket(name = "Name", in_out='INPUT', socket_type = 'NodeSocketString')
			name_socket.attribute_domain = 'POINT'
			
			#Socket Fallback
			fallback_socket = fallback_boolean.interface.new_socket(name = "Fallback", in_out='INPUT', socket_type = 'NodeSocketBool')
			fallback_socket.attribute_domain = 'POINT'
			
			
			#initialize fallback_boolean nodes
			#node Group Output
			group_output_27 = fallback_boolean.nodes.new("NodeGroupOutput")
			group_output_27.name = "Group Output"
			group_output_27.is_active_output = True
			
			#node Group Input
			group_input_26 = fallback_boolean.nodes.new("NodeGroupInput")
			group_input_26.name = "Group Input"
			
			#node Named Attribute
			named_attribute_3 = fallback_boolean.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_3.name = "Named Attribute"
			named_attribute_3.data_type = 'BOOLEAN'
			
			#node Switch
			switch_5 = fallback_boolean.nodes.new("GeometryNodeSwitch")
			switch_5.name = "Switch"
			switch_5.input_type = 'BOOLEAN'
			
			
			
			
			#Set locations
			group_output_27.location = (276.6171569824219, 4.738137245178223)
			group_input_26.location = (-280.0, 0.0)
			named_attribute_3.location = (-94.73597717285156, 4.738137245178223)
			switch_5.location = (86.61715698242188, 4.738137245178223)
			
			#Set dimensions
			group_output_27.width, group_output_27.height = 140.0, 100.0
			group_input_26.width, group_input_26.height = 140.0, 100.0
			named_attribute_3.width, named_attribute_3.height = 140.0, 100.0
			switch_5.width, switch_5.height = 140.0, 100.0
			
			#initialize fallback_boolean links
			#named_attribute_3.Exists -> switch_5.Switch
			fallback_boolean.links.new(named_attribute_3.outputs[1], switch_5.inputs[0])
			#named_attribute_3.Attribute -> switch_5.True
			fallback_boolean.links.new(named_attribute_3.outputs[0], switch_5.inputs[2])
			#group_input_26.Fallback -> switch_5.False
			fallback_boolean.links.new(group_input_26.outputs[1], switch_5.inputs[1])
			#switch_5.Output -> group_output_27.Boolean
			fallback_boolean.links.new(switch_5.outputs[0], group_output_27.inputs[0])
			#group_input_26.Name -> named_attribute_3.Name
			fallback_boolean.links.new(group_input_26.outputs[0], named_attribute_3.inputs[0])
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
			backbone_lower_socket.subtype = 'NONE'
			backbone_lower_socket.default_value = 0
			backbone_lower_socket.min_value = -2147483648
			backbone_lower_socket.max_value = 2147483647
			backbone_lower_socket.attribute_domain = 'POINT'
			
			#Socket Backbone Upper
			backbone_upper_socket = _mn_constants_atom_name_peptide.interface.new_socket(name = "Backbone Upper", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			backbone_upper_socket.subtype = 'NONE'
			backbone_upper_socket.default_value = 0
			backbone_upper_socket.min_value = -2147483648
			backbone_upper_socket.max_value = 2147483647
			backbone_upper_socket.attribute_domain = 'POINT'
			
			#Socket Side Chain Lower
			side_chain_lower_socket = _mn_constants_atom_name_peptide.interface.new_socket(name = "Side Chain Lower", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			side_chain_lower_socket.subtype = 'NONE'
			side_chain_lower_socket.default_value = 0
			side_chain_lower_socket.min_value = -2147483648
			side_chain_lower_socket.max_value = 2147483647
			side_chain_lower_socket.attribute_domain = 'POINT'
			
			#Socket Side Chain Upper
			side_chain_upper_socket = _mn_constants_atom_name_peptide.interface.new_socket(name = "Side Chain Upper", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			side_chain_upper_socket.subtype = 'NONE'
			side_chain_upper_socket.default_value = 0
			side_chain_upper_socket.min_value = -2147483648
			side_chain_upper_socket.max_value = 2147483647
			side_chain_upper_socket.attribute_domain = 'POINT'
			
			#Socket Alpha Carbon
			alpha_carbon_socket = _mn_constants_atom_name_peptide.interface.new_socket(name = "Alpha Carbon", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			alpha_carbon_socket.subtype = 'NONE'
			alpha_carbon_socket.default_value = 0
			alpha_carbon_socket.min_value = -2147483648
			alpha_carbon_socket.max_value = 2147483647
			alpha_carbon_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_constants_atom_name_peptide nodes
			#node Group Input
			group_input_27 = _mn_constants_atom_name_peptide.nodes.new("NodeGroupInput")
			group_input_27.name = "Group Input"
			
			#node Group Output
			group_output_28 = _mn_constants_atom_name_peptide.nodes.new("NodeGroupOutput")
			group_output_28.name = "Group Output"
			group_output_28.is_active_output = True
			
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
			group_input_27.location = (-200.0, 0.0)
			group_output_28.location = (260.0, 180.0)
			integer_001.location = (0.0, -50.0)
			integer_004.location = (0.0, -140.0)
			integer.location = (0.0, 40.0)
			integer_003.location = (0.0, 240.0)
			integer_002.location = (0.0, 140.0)
			
			#Set dimensions
			group_input_27.width, group_input_27.height = 140.0, 100.0
			group_output_28.width, group_output_28.height = 140.0, 100.0
			integer_001.width, integer_001.height = 140.0, 100.0
			integer_004.width, integer_004.height = 140.0, 100.0
			integer.width, integer.height = 140.0, 100.0
			integer_003.width, integer_003.height = 140.0, 100.0
			integer_002.width, integer_002.height = 140.0, 100.0
			
			#initialize _mn_constants_atom_name_peptide links
			#integer_003.Integer -> group_output_28.Backbone Lower
			_mn_constants_atom_name_peptide.links.new(integer_003.outputs[0], group_output_28.inputs[0])
			#integer_002.Integer -> group_output_28.Backbone Upper
			_mn_constants_atom_name_peptide.links.new(integer_002.outputs[0], group_output_28.inputs[1])
			#integer.Integer -> group_output_28.Side Chain Lower
			_mn_constants_atom_name_peptide.links.new(integer.outputs[0], group_output_28.inputs[2])
			#integer_001.Integer -> group_output_28.Side Chain Upper
			_mn_constants_atom_name_peptide.links.new(integer_001.outputs[0], group_output_28.inputs[3])
			#integer_004.Integer -> group_output_28.Alpha Carbon
			_mn_constants_atom_name_peptide.links.new(integer_004.outputs[0], group_output_28.inputs[4])
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
			is_backbone_socket.attribute_domain = 'POINT'
			
			#Socket Is Side Chain
			is_side_chain_socket = _mn_select_peptide.interface.new_socket(name = "Is Side Chain", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_side_chain_socket.attribute_domain = 'POINT'
			
			#Socket Is Peptide
			is_peptide_socket = _mn_select_peptide.interface.new_socket(name = "Is Peptide", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_peptide_socket.attribute_domain = 'POINT'
			
			#Socket Is Alpha Carbon
			is_alpha_carbon_socket = _mn_select_peptide.interface.new_socket(name = "Is Alpha Carbon", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_alpha_carbon_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_select_peptide nodes
			#node Group Input
			group_input_28 = _mn_select_peptide.nodes.new("NodeGroupInput")
			group_input_28.name = "Group Input"
			
			#node Compare
			compare_3 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
			compare_3.name = "Compare"
			compare_3.data_type = 'INT'
			compare_3.mode = 'ELEMENT'
			compare_3.operation = 'GREATER_EQUAL'
			
			#node Compare.001
			compare_001_1 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
			compare_001_1.name = "Compare.001"
			compare_001_1.data_type = 'INT'
			compare_001_1.mode = 'ELEMENT'
			compare_001_1.operation = 'LESS_EQUAL'
			
			#node Boolean Math.001
			boolean_math_001_4 = _mn_select_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_4.name = "Boolean Math.001"
			boolean_math_001_4.operation = 'AND'
			
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
			named_attribute_4 = _mn_select_peptide.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_4.name = "Named Attribute"
			named_attribute_4.data_type = 'INT'
			#Name
			named_attribute_4.inputs[0].default_value = "atom_name"
			
			#node Boolean Math.003
			boolean_math_003_2 = _mn_select_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003_2.name = "Boolean Math.003"
			boolean_math_003_2.operation = 'AND'
			
			#node Group Output
			group_output_29 = _mn_select_peptide.nodes.new("NodeGroupOutput")
			group_output_29.name = "Group Output"
			group_output_29.is_active_output = True
			
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
			group_8 = _mn_select_peptide.nodes.new("GeometryNodeGroup")
			group_8.name = "Group"
			group_8.node_tree = _mn_constants_atom_name_peptide
			
			#node Boolean Math
			boolean_math_4 = _mn_select_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math_4.name = "Boolean Math"
			boolean_math_4.operation = 'OR'
			
			
			
			
			#Set locations
			group_input_28.location = (-460.0, 0.0)
			compare_3.location = (80.0, 80.0)
			compare_001_1.location = (80.0, -80.0)
			boolean_math_001_4.location = (260.0, 80.0)
			compare_002.location = (80.0, -240.0)
			compare_003.location = (80.0, -400.0)
			boolean_math_002_2.location = (260.0, -240.0)
			compare_004.location = (80.0, -560.0)
			named_attribute_4.location = (-360.0, -480.0)
			boolean_math_003_2.location = (260.0, -560.0)
			group_output_29.location = (666.1161499023438, -263.7054748535156)
			compare_005.location = (80.0, -720.0)
			compare_006.location = (260.0, -380.0)
			group_8.location = (-411.24090576171875, -312.71807861328125)
			boolean_math_4.location = (420.0, -240.0)
			
			#Set dimensions
			group_input_28.width, group_input_28.height = 140.0, 100.0
			compare_3.width, compare_3.height = 140.0, 100.0
			compare_001_1.width, compare_001_1.height = 140.0, 100.0
			boolean_math_001_4.width, boolean_math_001_4.height = 140.0, 100.0
			compare_002.width, compare_002.height = 153.86517333984375, 100.0
			compare_003.width, compare_003.height = 153.86517333984375, 100.0
			boolean_math_002_2.width, boolean_math_002_2.height = 140.0, 100.0
			compare_004.width, compare_004.height = 140.0, 100.0
			named_attribute_4.width, named_attribute_4.height = 140.0, 100.0
			boolean_math_003_2.width, boolean_math_003_2.height = 140.0, 100.0
			group_output_29.width, group_output_29.height = 140.0, 100.0
			compare_005.width, compare_005.height = 140.0, 100.0
			compare_006.width, compare_006.height = 140.0, 100.0
			group_8.width, group_8.height = 369.1165771484375, 100.0
			boolean_math_4.width, boolean_math_4.height = 140.0, 100.0
			
			#initialize _mn_select_peptide links
			#compare_001_1.Result -> boolean_math_001_4.Boolean
			_mn_select_peptide.links.new(compare_001_1.outputs[0], boolean_math_001_4.inputs[1])
			#group_8.Backbone Lower -> compare_3.B
			_mn_select_peptide.links.new(group_8.outputs[0], compare_3.inputs[3])
			#named_attribute_4.Attribute -> compare_3.A
			_mn_select_peptide.links.new(named_attribute_4.outputs[0], compare_3.inputs[2])
			#compare_3.Result -> boolean_math_001_4.Boolean
			_mn_select_peptide.links.new(compare_3.outputs[0], boolean_math_001_4.inputs[0])
			#named_attribute_4.Attribute -> compare_001_1.A
			_mn_select_peptide.links.new(named_attribute_4.outputs[0], compare_001_1.inputs[2])
			#group_8.Backbone Upper -> compare_001_1.B
			_mn_select_peptide.links.new(group_8.outputs[1], compare_001_1.inputs[3])
			#boolean_math_001_4.Boolean -> group_output_29.Is Backbone
			_mn_select_peptide.links.new(boolean_math_001_4.outputs[0], group_output_29.inputs[0])
			#compare_003.Result -> boolean_math_002_2.Boolean
			_mn_select_peptide.links.new(compare_003.outputs[0], boolean_math_002_2.inputs[1])
			#named_attribute_4.Attribute -> compare_002.A
			_mn_select_peptide.links.new(named_attribute_4.outputs[0], compare_002.inputs[2])
			#compare_002.Result -> boolean_math_002_2.Boolean
			_mn_select_peptide.links.new(compare_002.outputs[0], boolean_math_002_2.inputs[0])
			#named_attribute_4.Attribute -> compare_003.A
			_mn_select_peptide.links.new(named_attribute_4.outputs[0], compare_003.inputs[2])
			#group_8.Side Chain Lower -> compare_002.B
			_mn_select_peptide.links.new(group_8.outputs[2], compare_002.inputs[3])
			#group_8.Side Chain Upper -> compare_003.B
			_mn_select_peptide.links.new(group_8.outputs[3], compare_003.inputs[3])
			#compare_005.Result -> boolean_math_003_2.Boolean
			_mn_select_peptide.links.new(compare_005.outputs[0], boolean_math_003_2.inputs[1])
			#named_attribute_4.Attribute -> compare_004.A
			_mn_select_peptide.links.new(named_attribute_4.outputs[0], compare_004.inputs[2])
			#compare_004.Result -> boolean_math_003_2.Boolean
			_mn_select_peptide.links.new(compare_004.outputs[0], boolean_math_003_2.inputs[0])
			#named_attribute_4.Attribute -> compare_005.A
			_mn_select_peptide.links.new(named_attribute_4.outputs[0], compare_005.inputs[2])
			#group_8.Backbone Lower -> compare_004.B
			_mn_select_peptide.links.new(group_8.outputs[0], compare_004.inputs[3])
			#group_8.Side Chain Upper -> compare_005.B
			_mn_select_peptide.links.new(group_8.outputs[3], compare_005.inputs[3])
			#boolean_math_003_2.Boolean -> group_output_29.Is Peptide
			_mn_select_peptide.links.new(boolean_math_003_2.outputs[0], group_output_29.inputs[2])
			#named_attribute_4.Attribute -> compare_006.A
			_mn_select_peptide.links.new(named_attribute_4.outputs[0], compare_006.inputs[2])
			#group_8.Alpha Carbon -> compare_006.B
			_mn_select_peptide.links.new(group_8.outputs[4], compare_006.inputs[3])
			#compare_006.Result -> group_output_29.Is Alpha Carbon
			_mn_select_peptide.links.new(compare_006.outputs[0], group_output_29.inputs[3])
			#boolean_math_002_2.Boolean -> boolean_math_4.Boolean
			_mn_select_peptide.links.new(boolean_math_002_2.outputs[0], boolean_math_4.inputs[0])
			#compare_006.Result -> boolean_math_4.Boolean
			_mn_select_peptide.links.new(compare_006.outputs[0], boolean_math_4.inputs[1])
			#boolean_math_4.Boolean -> group_output_29.Is Side Chain
			_mn_select_peptide.links.new(boolean_math_4.outputs[0], group_output_29.inputs[1])
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
			selection_socket_4.attribute_domain = 'POINT'
			selection_socket_4.description = "True if atom is an alpha carbon of an amino acid"
			
			#Socket Inverted
			inverted_socket_4 = is_alpha_carbon.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket_4.attribute_domain = 'POINT'
			
			#Socket And
			and_socket_5 = is_alpha_carbon.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket_5.attribute_domain = 'POINT'
			and_socket_5.hide_value = True
			
			#Socket Or
			or_socket_4 = is_alpha_carbon.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket_4.attribute_domain = 'POINT'
			or_socket_4.hide_value = True
			
			
			#initialize is_alpha_carbon nodes
			#node Group Output
			group_output_30 = is_alpha_carbon.nodes.new("NodeGroupOutput")
			group_output_30.name = "Group Output"
			group_output_30.is_active_output = True
			
			#node Group Input
			group_input_29 = is_alpha_carbon.nodes.new("NodeGroupInput")
			group_input_29.name = "Group Input"
			
			#node Boolean Math.001
			boolean_math_001_5 = is_alpha_carbon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_5.name = "Boolean Math.001"
			boolean_math_001_5.operation = 'AND'
			
			#node Group.001
			group_001_4 = is_alpha_carbon.nodes.new("GeometryNodeGroup")
			group_001_4.name = "Group.001"
			group_001_4.node_tree = fallback_boolean
			#Socket_2
			group_001_4.inputs[0].default_value = "is_alpha_carbon"
			
			#node Group.002
			group_002_2 = is_alpha_carbon.nodes.new("GeometryNodeGroup")
			group_002_2.name = "Group.002"
			group_002_2.node_tree = _mn_select_peptide
			group_002_2.outputs[0].hide = True
			group_002_2.outputs[1].hide = True
			group_002_2.outputs[2].hide = True
			
			#node Boolean Math.002
			boolean_math_002_3 = is_alpha_carbon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_3.name = "Boolean Math.002"
			boolean_math_002_3.operation = 'OR'
			
			#node Boolean Math
			boolean_math_5 = is_alpha_carbon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_5.name = "Boolean Math"
			boolean_math_5.operation = 'NOT'
			
			
			
			
			#Set locations
			group_output_30.location = (520.0, 0.0)
			group_input_29.location = (-200.0, 0.0)
			boolean_math_001_5.location = (160.0, 0.0)
			group_001_4.location = (-88.33343505859375, -180.0)
			group_002_2.location = (-290.4490661621094, -180.0)
			boolean_math_002_3.location = (340.0, 0.0)
			boolean_math_5.location = (340.0, -140.0)
			
			#Set dimensions
			group_output_30.width, group_output_30.height = 140.0, 100.0
			group_input_29.width, group_input_29.height = 140.0, 100.0
			boolean_math_001_5.width, boolean_math_001_5.height = 140.0, 100.0
			group_001_4.width, group_001_4.height = 208.33343505859375, 100.0
			group_002_2.width, group_002_2.height = 170.44906616210938, 100.0
			boolean_math_002_3.width, boolean_math_002_3.height = 140.0, 100.0
			boolean_math_5.width, boolean_math_5.height = 140.0, 100.0
			
			#initialize is_alpha_carbon links
			#group_input_29.And -> boolean_math_001_5.Boolean
			is_alpha_carbon.links.new(group_input_29.outputs[0], boolean_math_001_5.inputs[0])
			#boolean_math_002_3.Boolean -> group_output_30.Selection
			is_alpha_carbon.links.new(boolean_math_002_3.outputs[0], group_output_30.inputs[0])
			#group_001_4.Boolean -> boolean_math_001_5.Boolean
			is_alpha_carbon.links.new(group_001_4.outputs[0], boolean_math_001_5.inputs[1])
			#group_002_2.Is Alpha Carbon -> group_001_4.Fallback
			is_alpha_carbon.links.new(group_002_2.outputs[3], group_001_4.inputs[1])
			#boolean_math_001_5.Boolean -> boolean_math_002_3.Boolean
			is_alpha_carbon.links.new(boolean_math_001_5.outputs[0], boolean_math_002_3.inputs[0])
			#group_input_29.Or -> boolean_math_002_3.Boolean
			is_alpha_carbon.links.new(group_input_29.outputs[1], boolean_math_002_3.inputs[1])
			#boolean_math_002_3.Boolean -> boolean_math_5.Boolean
			is_alpha_carbon.links.new(boolean_math_002_3.outputs[0], boolean_math_5.inputs[0])
			#boolean_math_5.Boolean -> group_output_30.Inverted
			is_alpha_carbon.links.new(boolean_math_5.outputs[0], group_output_30.inputs[1])
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
			is_valid_socket.attribute_domain = 'POINT'
			is_valid_socket.description = "Whether the pick is valid. Pick is only valid if a single item is picked in the Group ID"
			
			#Socket Index
			index_socket_1 = group_pick.interface.new_socket(name = "Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			index_socket_1.subtype = 'NONE'
			index_socket_1.default_value = 0
			index_socket_1.min_value = 0
			index_socket_1.max_value = 2147483647
			index_socket_1.attribute_domain = 'POINT'
			index_socket_1.description = "Index of picked item. Returns -1 if not a valid pick."
			
			#Socket Pick
			pick_socket = group_pick.interface.new_socket(name = "Pick", in_out='INPUT', socket_type = 'NodeSocketBool')
			pick_socket.attribute_domain = 'POINT'
			pick_socket.hide_value = True
			pick_socket.description = "True for the item to pick from the group. If number of picks is 0 or more than 1, not a valid pick"
			
			#Socket Group ID
			group_id_socket = group_pick.interface.new_socket(name = "Group ID", in_out='INPUT', socket_type = 'NodeSocketInt')
			group_id_socket.subtype = 'NONE'
			group_id_socket.default_value = 0
			group_id_socket.min_value = -2147483648
			group_id_socket.max_value = 2147483647
			group_id_socket.attribute_domain = 'POINT'
			group_id_socket.description = "Group ID inside which to pick the item"
			
			
			#initialize group_pick nodes
			#node Group Output
			group_output_31 = group_pick.nodes.new("NodeGroupOutput")
			group_output_31.name = "Group Output"
			group_output_31.is_active_output = True
			
			#node Group Input
			group_input_30 = group_pick.nodes.new("NodeGroupInput")
			group_input_30.name = "Group Input"
			
			#node Switch
			switch_6 = group_pick.nodes.new("GeometryNodeSwitch")
			switch_6.name = "Switch"
			switch_6.input_type = 'INT'
			#False
			switch_6.inputs[1].default_value = 0
			
			#node Index
			index_3 = group_pick.nodes.new("GeometryNodeInputIndex")
			index_3.name = "Index"
			
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
			switch_001_1 = group_pick.nodes.new("GeometryNodeSwitch")
			switch_001_1.name = "Switch.001"
			switch_001_1.input_type = 'INT'
			#False
			switch_001_1.inputs[1].default_value = -1
			
			#node Compare.003
			compare_003_1 = group_pick.nodes.new("FunctionNodeCompare")
			compare_003_1.name = "Compare.003"
			compare_003_1.data_type = 'INT'
			compare_003_1.mode = 'ELEMENT'
			compare_003_1.operation = 'EQUAL'
			#B_INT
			compare_003_1.inputs[3].default_value = 1
			
			#node Reroute.001
			reroute_001_5 = group_pick.nodes.new("NodeReroute")
			reroute_001_5.name = "Reroute.001"
			#node Reroute.002
			reroute_002_2 = group_pick.nodes.new("NodeReroute")
			reroute_002_2.name = "Reroute.002"
			
			
			
			#Set locations
			group_output_31.location = (462.9173889160156, 0.0)
			group_input_30.location = (-472.9173889160156, 0.0)
			switch_6.location = (-120.0, -20.0)
			index_3.location = (-480.0, -120.0)
			accumulate_field.location = (60.0, -20.0)
			accumulate_field_002.location = (-120.0, 180.0)
			switch_001_1.location = (240.0, -20.0)
			compare_003_1.location = (60.0, 180.0)
			reroute_001_5.location = (-260.0, -100.0)
			reroute_002_2.location = (-260.0, -60.0)
			
			#Set dimensions
			group_output_31.width, group_output_31.height = 140.0, 100.0
			group_input_30.width, group_input_30.height = 140.0, 100.0
			switch_6.width, switch_6.height = 140.0, 100.0
			index_3.width, index_3.height = 140.0, 100.0
			accumulate_field.width, accumulate_field.height = 140.0, 100.0
			accumulate_field_002.width, accumulate_field_002.height = 140.0, 100.0
			switch_001_1.width, switch_001_1.height = 140.0, 100.0
			compare_003_1.width, compare_003_1.height = 138.9921875, 100.0
			reroute_001_5.width, reroute_001_5.height = 16.0, 100.0
			reroute_002_2.width, reroute_002_2.height = 16.0, 100.0
			
			#initialize group_pick links
			#switch_6.Output -> accumulate_field.Value
			group_pick.links.new(switch_6.outputs[0], accumulate_field.inputs[0])
			#compare_003_1.Result -> switch_001_1.Switch
			group_pick.links.new(compare_003_1.outputs[0], switch_001_1.inputs[0])
			#accumulate_field.Total -> switch_001_1.True
			group_pick.links.new(accumulate_field.outputs[2], switch_001_1.inputs[2])
			#reroute_001_5.Output -> accumulate_field.Group ID
			group_pick.links.new(reroute_001_5.outputs[0], accumulate_field.inputs[1])
			#reroute_001_5.Output -> accumulate_field_002.Group ID
			group_pick.links.new(reroute_001_5.outputs[0], accumulate_field_002.inputs[1])
			#reroute_002_2.Output -> switch_6.Switch
			group_pick.links.new(reroute_002_2.outputs[0], switch_6.inputs[0])
			#reroute_002_2.Output -> accumulate_field_002.Value
			group_pick.links.new(reroute_002_2.outputs[0], accumulate_field_002.inputs[0])
			#index_3.Index -> switch_6.True
			group_pick.links.new(index_3.outputs[0], switch_6.inputs[2])
			#accumulate_field_002.Total -> compare_003_1.A
			group_pick.links.new(accumulate_field_002.outputs[2], compare_003_1.inputs[2])
			#group_input_30.Group ID -> reroute_001_5.Input
			group_pick.links.new(group_input_30.outputs[1], reroute_001_5.inputs[0])
			#group_input_30.Pick -> reroute_002_2.Input
			group_pick.links.new(group_input_30.outputs[0], reroute_002_2.inputs[0])
			#switch_001_1.Output -> group_output_31.Index
			group_pick.links.new(switch_001_1.outputs[0], group_output_31.inputs[1])
			#compare_003_1.Result -> group_output_31.Is Valid
			group_pick.links.new(compare_003_1.outputs[0], group_output_31.inputs[0])
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
			is_valid_socket_1.attribute_domain = 'POINT'
			is_valid_socket_1.description = "The pick for this group is valid"
			
			#Socket Index
			index_socket_2 = group_pick_vector.interface.new_socket(name = "Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			index_socket_2.subtype = 'NONE'
			index_socket_2.default_value = 0
			index_socket_2.min_value = -2147483648
			index_socket_2.max_value = 2147483647
			index_socket_2.attribute_domain = 'POINT'
			index_socket_2.description = "Picked Index for the Group"
			
			#Socket Vector
			vector_socket_1 = group_pick_vector.interface.new_socket(name = "Vector", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			vector_socket_1.subtype = 'NONE'
			vector_socket_1.default_value = (0.0, 0.0, 0.0)
			vector_socket_1.min_value = -3.4028234663852886e+38
			vector_socket_1.max_value = 3.4028234663852886e+38
			vector_socket_1.attribute_domain = 'POINT'
			vector_socket_1.description = "Picked vector for the group"
			
			#Socket Pick
			pick_socket_1 = group_pick_vector.interface.new_socket(name = "Pick", in_out='INPUT', socket_type = 'NodeSocketBool')
			pick_socket_1.attribute_domain = 'POINT'
			pick_socket_1.hide_value = True
			
			#Socket Group ID
			group_id_socket_1 = group_pick_vector.interface.new_socket(name = "Group ID", in_out='INPUT', socket_type = 'NodeSocketInt')
			group_id_socket_1.subtype = 'NONE'
			group_id_socket_1.default_value = 0
			group_id_socket_1.min_value = -2147483648
			group_id_socket_1.max_value = 2147483647
			group_id_socket_1.attribute_domain = 'POINT'
			
			#Socket Position
			position_socket_1 = group_pick_vector.interface.new_socket(name = "Position", in_out='INPUT', socket_type = 'NodeSocketVector')
			position_socket_1.subtype = 'NONE'
			position_socket_1.default_value = (0.0, 0.0, 0.0)
			position_socket_1.min_value = -3.4028234663852886e+38
			position_socket_1.max_value = 3.4028234663852886e+38
			position_socket_1.attribute_domain = 'POINT'
			position_socket_1.description = "Vector field to pick vlaue for, defaults to Position"
			
			
			#initialize group_pick_vector nodes
			#node Group Output
			group_output_32 = group_pick_vector.nodes.new("NodeGroupOutput")
			group_output_32.name = "Group Output"
			group_output_32.is_active_output = True
			
			#node Group Input
			group_input_31 = group_pick_vector.nodes.new("NodeGroupInput")
			group_input_31.name = "Group Input"
			
			#node Evaluate at Index.001
			evaluate_at_index_001_2 = group_pick_vector.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001_2.name = "Evaluate at Index.001"
			evaluate_at_index_001_2.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_001_2.domain = 'POINT'
			
			#node Switch.002
			switch_002 = group_pick_vector.nodes.new("GeometryNodeSwitch")
			switch_002.name = "Switch.002"
			switch_002.input_type = 'VECTOR'
			#False
			switch_002.inputs[1].default_value = (0.0, 0.0, 0.0)
			
			#node Group
			group_9 = group_pick_vector.nodes.new("GeometryNodeGroup")
			group_9.name = "Group"
			group_9.node_tree = group_pick
			
			
			
			
			#Set locations
			group_output_32.location = (-40.0, -20.0)
			group_input_31.location = (-740.0, -80.0)
			evaluate_at_index_001_2.location = (-380.0, -180.0)
			switch_002.location = (-220.0, -60.0)
			group_9.location = (-560.0, -20.0)
			
			#Set dimensions
			group_output_32.width, group_output_32.height = 140.0, 100.0
			group_input_31.width, group_input_31.height = 140.0, 100.0
			evaluate_at_index_001_2.width, evaluate_at_index_001_2.height = 132.09918212890625, 100.0
			switch_002.width, switch_002.height = 140.0, 100.0
			group_9.width, group_9.height = 140.0, 100.0
			
			#initialize group_pick_vector links
			#group_9.Is Valid -> switch_002.Switch
			group_pick_vector.links.new(group_9.outputs[0], switch_002.inputs[0])
			#group_9.Index -> evaluate_at_index_001_2.Index
			group_pick_vector.links.new(group_9.outputs[1], evaluate_at_index_001_2.inputs[0])
			#evaluate_at_index_001_2.Value -> switch_002.True
			group_pick_vector.links.new(evaluate_at_index_001_2.outputs[0], switch_002.inputs[2])
			#group_9.Index -> group_output_32.Index
			group_pick_vector.links.new(group_9.outputs[1], group_output_32.inputs[1])
			#group_9.Is Valid -> group_output_32.Is Valid
			group_pick_vector.links.new(group_9.outputs[0], group_output_32.inputs[0])
			#switch_002.Output -> group_output_32.Vector
			group_pick_vector.links.new(switch_002.outputs[0], group_output_32.inputs[2])
			#group_input_31.Group ID -> group_9.Group ID
			group_pick_vector.links.new(group_input_31.outputs[1], group_9.inputs[1])
			#group_input_31.Pick -> group_9.Pick
			group_pick_vector.links.new(group_input_31.outputs[0], group_9.inputs[0])
			#group_input_31.Position -> evaluate_at_index_001_2.Value
			group_pick_vector.links.new(group_input_31.outputs[2], evaluate_at_index_001_2.inputs[1])
			return group_pick_vector

		group_pick_vector = group_pick_vector_node_group()

		#initialize offset_integer node group
		def offset_integer_node_group():
			offset_integer = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Offset Integer")

			offset_integer.color_tag = 'CONVERTER'
			offset_integer.description = ""

			
			#offset_integer interface
			#Socket Value
			value_socket_6 = offset_integer.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			value_socket_6.subtype = 'NONE'
			value_socket_6.default_value = 0
			value_socket_6.min_value = -2147483648
			value_socket_6.max_value = 2147483647
			value_socket_6.attribute_domain = 'POINT'
			
			#Socket Index
			index_socket_3 = offset_integer.interface.new_socket(name = "Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			index_socket_3.subtype = 'NONE'
			index_socket_3.default_value = 0
			index_socket_3.min_value = 0
			index_socket_3.max_value = 2147483647
			index_socket_3.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_7 = offset_integer.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketInt')
			value_socket_7.subtype = 'NONE'
			value_socket_7.default_value = 0
			value_socket_7.min_value = -2147483648
			value_socket_7.max_value = 2147483647
			value_socket_7.attribute_domain = 'POINT'
			value_socket_7.hide_value = True
			
			#Socket Offset
			offset_socket_6 = offset_integer.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket_6.subtype = 'NONE'
			offset_socket_6.default_value = 0
			offset_socket_6.min_value = -2147483648
			offset_socket_6.max_value = 2147483647
			offset_socket_6.attribute_domain = 'POINT'
			
			
			#initialize offset_integer nodes
			#node Group Output
			group_output_33 = offset_integer.nodes.new("NodeGroupOutput")
			group_output_33.name = "Group Output"
			group_output_33.is_active_output = True
			
			#node Group Input
			group_input_32 = offset_integer.nodes.new("NodeGroupInput")
			group_input_32.name = "Group Input"
			
			#node Evaluate at Index
			evaluate_at_index_2 = offset_integer.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_2.name = "Evaluate at Index"
			evaluate_at_index_2.data_type = 'INT'
			evaluate_at_index_2.domain = 'POINT'
			
			#node Math
			math_4 = offset_integer.nodes.new("ShaderNodeMath")
			math_4.name = "Math"
			math_4.operation = 'ADD'
			math_4.use_clamp = False
			
			
			
			
			#Set locations
			group_output_33.location = (190.0, 0.0)
			group_input_32.location = (-412.72760009765625, 0.2001800537109375)
			evaluate_at_index_2.location = (0.0, 0.0)
			math_4.location = (-217.90158081054688, 69.93922424316406)
			
			#Set dimensions
			group_output_33.width, group_output_33.height = 140.0, 100.0
			group_input_32.width, group_input_32.height = 140.0, 100.0
			evaluate_at_index_2.width, evaluate_at_index_2.height = 140.0, 100.0
			math_4.width, math_4.height = 140.0, 100.0
			
			#initialize offset_integer links
			#evaluate_at_index_2.Value -> group_output_33.Value
			offset_integer.links.new(evaluate_at_index_2.outputs[0], group_output_33.inputs[0])
			#group_input_32.Index -> math_4.Value
			offset_integer.links.new(group_input_32.outputs[0], math_4.inputs[0])
			#group_input_32.Offset -> math_4.Value
			offset_integer.links.new(group_input_32.outputs[2], math_4.inputs[1])
			#math_4.Value -> evaluate_at_index_2.Index
			offset_integer.links.new(math_4.outputs[0], evaluate_at_index_2.inputs[0])
			#group_input_32.Value -> evaluate_at_index_2.Value
			offset_integer.links.new(group_input_32.outputs[1], evaluate_at_index_2.inputs[1])
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
			unique_group_id_socket.subtype = 'NONE'
			unique_group_id_socket.default_value = 0
			unique_group_id_socket.min_value = -2147483648
			unique_group_id_socket.max_value = 2147483647
			unique_group_id_socket.attribute_domain = 'POINT'
			unique_group_id_socket.description = "A unique Group ID for eash residue"
			
			
			#initialize res_group_id nodes
			#node Group Output
			group_output_34 = res_group_id.nodes.new("NodeGroupOutput")
			group_output_34.name = "Group Output"
			group_output_34.is_active_output = True
			
			#node Group Input
			group_input_33 = res_group_id.nodes.new("NodeGroupInput")
			group_input_33.name = "Group Input"
			
			#node Named Attribute.001
			named_attribute_001_4 = res_group_id.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001_4.name = "Named Attribute.001"
			named_attribute_001_4.data_type = 'INT'
			#Name
			named_attribute_001_4.inputs[0].default_value = "res_id"
			
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
			compare_001_2 = res_group_id.nodes.new("FunctionNodeCompare")
			compare_001_2.name = "Compare.001"
			compare_001_2.data_type = 'INT'
			compare_001_2.mode = 'ELEMENT'
			compare_001_2.operation = 'NOT_EQUAL'
			
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
			group_001_5 = res_group_id.nodes.new("GeometryNodeGroup")
			group_001_5.name = "Group.001"
			group_001_5.node_tree = offset_integer
			#Socket_1
			group_001_5.inputs[0].default_value = 0
			#Socket_2
			group_001_5.inputs[2].default_value = -1
			
			#node Math
			math_5 = res_group_id.nodes.new("ShaderNodeMath")
			math_5.name = "Math"
			math_5.operation = 'SUBTRACT'
			math_5.use_clamp = False
			#Value_001
			math_5.inputs[1].default_value = 1.0
			
			#node Frame
			frame = res_group_id.nodes.new("NodeFrame")
			frame.name = "Frame"
			frame.label_size = 20
			frame.shrink = True
			
			#node Reroute
			reroute_8 = res_group_id.nodes.new("NodeReroute")
			reroute_8.label = "subtracting 1 from the leading, but things don't work right"
			reroute_8.name = "Reroute"
			#node Reroute.001
			reroute_001_6 = res_group_id.nodes.new("NodeReroute")
			reroute_001_6.name = "Reroute.001"
			#node Reroute.002
			reroute_002_3 = res_group_id.nodes.new("NodeReroute")
			reroute_002_3.label = "In theory we can just use the trailing value instead of"
			reroute_002_3.name = "Reroute.002"
			#node Reroute.003
			reroute_003_1 = res_group_id.nodes.new("NodeReroute")
			reroute_003_1.name = "Reroute.003"
			
			
			#Set parents
			math_5.parent = frame
			reroute_8.parent = frame
			reroute_001_6.parent = frame
			reroute_002_3.parent = frame
			reroute_003_1.parent = frame
			
			#Set locations
			group_output_34.location = (900.0, 160.0)
			group_input_33.location = (-420.0, 160.0)
			named_attribute_001_4.location = (-240.0, 0.0)
			named_attribute_002_1.location = (-250.0, 160.0)
			compare_002_1.location = (-70.0, 160.0)
			compare_001_2.location = (-70.0, 0.0)
			boolean_math_6.location = (90.0, 160.0)
			accumulate_field_001.location = (250.0, 160.0)
			group_001_5.location = (-70.0, -160.0)
			math_5.location = (519.2361450195312, 166.28671264648438)
			frame.location = (95.0, -20.0)
			reroute_8.location = (554.4125366210938, 257.9646911621094)
			reroute_001_6.location = (739.2361450195312, 306.2867126464844)
			reroute_002_3.location = (551.13134765625, 297.3444519042969)
			reroute_003_1.location = (379.23614501953125, 306.2867126464844)
			
			#Set dimensions
			group_output_34.width, group_output_34.height = 140.0, 100.0
			group_input_33.width, group_input_33.height = 140.0, 100.0
			named_attribute_001_4.width, named_attribute_001_4.height = 140.0, 100.0
			named_attribute_002_1.width, named_attribute_002_1.height = 140.0, 100.0
			compare_002_1.width, compare_002_1.height = 140.0, 100.0
			compare_001_2.width, compare_001_2.height = 140.0, 100.0
			boolean_math_6.width, boolean_math_6.height = 140.0, 100.0
			accumulate_field_001.width, accumulate_field_001.height = 140.0, 100.0
			group_001_5.width, group_001_5.height = 140.0, 100.0
			math_5.width, math_5.height = 140.0, 100.0
			frame.width, frame.height = 436.0, 356.2867126464844
			reroute_8.width, reroute_8.height = 16.0, 100.0
			reroute_001_6.width, reroute_001_6.height = 16.0, 100.0
			reroute_002_3.width, reroute_002_3.height = 16.0, 100.0
			reroute_003_1.width, reroute_003_1.height = 16.0, 100.0
			
			#initialize res_group_id links
			#compare_002_1.Result -> boolean_math_6.Boolean
			res_group_id.links.new(compare_002_1.outputs[0], boolean_math_6.inputs[0])
			#named_attribute_001_4.Attribute -> compare_001_2.A
			res_group_id.links.new(named_attribute_001_4.outputs[0], compare_001_2.inputs[2])
			#named_attribute_001_4.Attribute -> group_001_5.Value
			res_group_id.links.new(named_attribute_001_4.outputs[0], group_001_5.inputs[1])
			#compare_001_2.Result -> boolean_math_6.Boolean
			res_group_id.links.new(compare_001_2.outputs[0], boolean_math_6.inputs[1])
			#named_attribute_002_1.Attribute -> compare_002_1.A
			res_group_id.links.new(named_attribute_002_1.outputs[0], compare_002_1.inputs[2])
			#group_001_5.Value -> compare_001_2.B
			res_group_id.links.new(group_001_5.outputs[0], compare_001_2.inputs[3])
			#accumulate_field_001.Leading -> math_5.Value
			res_group_id.links.new(accumulate_field_001.outputs[0], math_5.inputs[0])
			#math_5.Value -> group_output_34.Unique Group ID
			res_group_id.links.new(math_5.outputs[0], group_output_34.inputs[0])
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
			is_valid_socket_2.attribute_domain = 'POINT'
			is_valid_socket_2.description = "Group contains only one occurrance of the selected atom. None or more than one returns False"
			
			#Socket Index
			index_socket_4 = residue_mask.interface.new_socket(name = "Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			index_socket_4.subtype = 'NONE'
			index_socket_4.default_value = 0
			index_socket_4.min_value = -2147483648
			index_socket_4.max_value = 2147483647
			index_socket_4.attribute_domain = 'POINT'
			index_socket_4.description = "Index for the group's atom with specified name, returns -1 if not valid"
			
			#Socket Position
			position_socket_2 = residue_mask.interface.new_socket(name = "Position", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			position_socket_2.subtype = 'NONE'
			position_socket_2.default_value = (0.0, 0.0, 0.0)
			position_socket_2.min_value = -3.4028234663852886e+38
			position_socket_2.max_value = 3.4028234663852886e+38
			position_socket_2.attribute_domain = 'POINT'
			position_socket_2.description = "Position of the picked point in the group, returns (0, 0, 0) if not valid"
			
			#Socket Group ID
			group_id_socket_2 = residue_mask.interface.new_socket(name = "Group ID", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			group_id_socket_2.subtype = 'NONE'
			group_id_socket_2.default_value = 0
			group_id_socket_2.min_value = -2147483648
			group_id_socket_2.max_value = 2147483647
			group_id_socket_2.attribute_domain = 'POINT'
			
			#Socket atom_name
			atom_name_socket = residue_mask.interface.new_socket(name = "atom_name", in_out='INPUT', socket_type = 'NodeSocketInt')
			atom_name_socket.subtype = 'NONE'
			atom_name_socket.default_value = 1
			atom_name_socket.min_value = 2
			atom_name_socket.max_value = 2147483647
			atom_name_socket.attribute_domain = 'POINT'
			atom_name_socket.description = "Atom to pick from the group"
			
			#Socket Use Fallback
			use_fallback_socket = residue_mask.interface.new_socket(name = "Use Fallback", in_out='INPUT', socket_type = 'NodeSocketBool')
			use_fallback_socket.attribute_domain = 'POINT'
			use_fallback_socket.description = "Uses a calculated Unique Group ID as a fallback. Disabling can increase performance if pre-computing a Group ID for multiple nodes"
			
			#Socket Group ID
			group_id_socket_3 = residue_mask.interface.new_socket(name = "Group ID", in_out='INPUT', socket_type = 'NodeSocketInt')
			group_id_socket_3.subtype = 'NONE'
			group_id_socket_3.default_value = 0
			group_id_socket_3.min_value = -2147483648
			group_id_socket_3.max_value = 2147483647
			group_id_socket_3.attribute_domain = 'POINT'
			
			
			#initialize residue_mask nodes
			#node Compare
			compare_4 = residue_mask.nodes.new("FunctionNodeCompare")
			compare_4.name = "Compare"
			compare_4.data_type = 'INT'
			compare_4.mode = 'ELEMENT'
			compare_4.operation = 'EQUAL'
			
			#node Group Input
			group_input_34 = residue_mask.nodes.new("NodeGroupInput")
			group_input_34.name = "Group Input"
			
			#node Named Attribute
			named_attribute_5 = residue_mask.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_5.name = "Named Attribute"
			named_attribute_5.data_type = 'INT'
			#Name
			named_attribute_5.inputs[0].default_value = "atom_name"
			
			#node Group Output
			group_output_35 = residue_mask.nodes.new("NodeGroupOutput")
			group_output_35.name = "Group Output"
			group_output_35.is_active_output = True
			
			#node Group
			group_10 = residue_mask.nodes.new("GeometryNodeGroup")
			group_10.name = "Group"
			group_10.node_tree = group_pick_vector
			#Socket_5
			group_10.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Group.002
			group_002_3 = residue_mask.nodes.new("GeometryNodeGroup")
			group_002_3.name = "Group.002"
			group_002_3.node_tree = res_group_id
			
			#node Switch
			switch_7 = residue_mask.nodes.new("GeometryNodeSwitch")
			switch_7.name = "Switch"
			switch_7.input_type = 'INT'
			
			
			
			
			#Set locations
			compare_4.location = (40.0, 340.0)
			group_input_34.location = (-140.0, 200.0)
			named_attribute_5.location = (-140.0, 340.0)
			group_output_35.location = (420.0, 340.0)
			group_10.location = (220.0, 340.0)
			group_002_3.location = (-140.0, 60.0)
			switch_7.location = (40.0, 180.0)
			
			#Set dimensions
			compare_4.width, compare_4.height = 140.0, 100.0
			group_input_34.width, group_input_34.height = 140.0, 100.0
			named_attribute_5.width, named_attribute_5.height = 140.0, 100.0
			group_output_35.width, group_output_35.height = 140.0, 100.0
			group_10.width, group_10.height = 164.60528564453125, 100.0
			group_002_3.width, group_002_3.height = 140.0, 100.0
			switch_7.width, switch_7.height = 140.0, 100.0
			
			#initialize residue_mask links
			#named_attribute_5.Attribute -> compare_4.A
			residue_mask.links.new(named_attribute_5.outputs[0], compare_4.inputs[2])
			#group_input_34.atom_name -> compare_4.B
			residue_mask.links.new(group_input_34.outputs[0], compare_4.inputs[3])
			#group_10.Index -> group_output_35.Index
			residue_mask.links.new(group_10.outputs[1], group_output_35.inputs[1])
			#group_10.Vector -> group_output_35.Position
			residue_mask.links.new(group_10.outputs[2], group_output_35.inputs[2])
			#group_10.Is Valid -> group_output_35.Is Valid
			residue_mask.links.new(group_10.outputs[0], group_output_35.inputs[0])
			#compare_4.Result -> group_10.Pick
			residue_mask.links.new(compare_4.outputs[0], group_10.inputs[0])
			#group_input_34.Use Fallback -> switch_7.Switch
			residue_mask.links.new(group_input_34.outputs[1], switch_7.inputs[0])
			#group_input_34.Group ID -> switch_7.False
			residue_mask.links.new(group_input_34.outputs[2], switch_7.inputs[1])
			#switch_7.Output -> group_10.Group ID
			residue_mask.links.new(switch_7.outputs[0], group_10.inputs[1])
			#group_002_3.Unique Group ID -> switch_7.True
			residue_mask.links.new(group_002_3.outputs[0], switch_7.inputs[2])
			#switch_7.Output -> group_output_35.Group ID
			residue_mask.links.new(switch_7.outputs[0], group_output_35.inputs[3])
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
			unique_group_id_socket_1.subtype = 'NONE'
			unique_group_id_socket_1.default_value = 0
			unique_group_id_socket_1.min_value = -2147483648
			unique_group_id_socket_1.max_value = 2147483647
			unique_group_id_socket_1.attribute_domain = 'POINT'
			
			#Socket CA Atoms
			ca_atoms_socket = _mn_topo_assign_backbone.interface.new_socket(name = "CA Atoms", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			ca_atoms_socket.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket_1 = _mn_topo_assign_backbone.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_1.attribute_domain = 'POINT'
			
			
			#initialize _mn_topo_assign_backbone nodes
			#node Group Output
			group_output_36 = _mn_topo_assign_backbone.nodes.new("NodeGroupOutput")
			group_output_36.name = "Group Output"
			group_output_36.is_active_output = True
			
			#node Group Input
			group_input_35 = _mn_topo_assign_backbone.nodes.new("NodeGroupInput")
			group_input_35.name = "Group Input"
			
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
			store_named_attribute_004_1 = _mn_topo_assign_backbone.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_004_1.name = "Store Named Attribute.004"
			store_named_attribute_004_1.data_type = 'FLOAT_VECTOR'
			store_named_attribute_004_1.domain = 'POINT'
			#Name
			store_named_attribute_004_1.inputs[2].default_value = "backbone_CA"
			
			#node Store Named Attribute.005
			store_named_attribute_005_1 = _mn_topo_assign_backbone.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_005_1.name = "Store Named Attribute.005"
			store_named_attribute_005_1.data_type = 'FLOAT_VECTOR'
			store_named_attribute_005_1.domain = 'POINT'
			#Name
			store_named_attribute_005_1.inputs[2].default_value = "backbone_O"
			
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
			group_11 = _mn_topo_assign_backbone.nodes.new("GeometryNodeGroup")
			group_11.name = "Group"
			group_11.node_tree = res_group_id
			
			#node Reroute
			reroute_9 = _mn_topo_assign_backbone.nodes.new("NodeReroute")
			reroute_9.name = "Reroute"
			#node Reroute.001
			reroute_001_7 = _mn_topo_assign_backbone.nodes.new("NodeReroute")
			reroute_001_7.name = "Reroute.001"
			#node Reroute.002
			reroute_002_4 = _mn_topo_assign_backbone.nodes.new("NodeReroute")
			reroute_002_4.name = "Reroute.002"
			#node Reroute.003
			reroute_003_2 = _mn_topo_assign_backbone.nodes.new("NodeReroute")
			reroute_003_2.name = "Reroute.003"
			#node Separate Geometry
			separate_geometry = _mn_topo_assign_backbone.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry.name = "Separate Geometry"
			separate_geometry.domain = 'POINT'
			
			#node Group.001
			group_001_6 = _mn_topo_assign_backbone.nodes.new("GeometryNodeGroup")
			group_001_6.name = "Group.001"
			group_001_6.node_tree = is_alpha_carbon
			#Socket_1
			group_001_6.inputs[0].default_value = True
			#Socket_3
			group_001_6.inputs[1].default_value = False
			
			
			
			
			#Set locations
			group_output_36.location = (720.0, 100.0)
			group_input_35.location = (-1200.0, 100.0)
			store_named_attribute_002.location = (-400.0, 100.0)
			store_named_attribute_003.location = (60.0, 100.0)
			store_named_attribute_004_1.location = (-180.0, 100.0)
			store_named_attribute_005_1.location = (300.0, 100.0)
			mn_topo_point_mask_005.location = (60.0, -120.0)
			mn_topo_point_mask_006.location = (-180.0, -120.0)
			mn_topo_point_mask_007.location = (300.0, -120.0)
			mn_topo_point_mask_004.location = (-400.0, -120.0)
			capture_attribute.location = (-1020.0, 100.0)
			group_11.location = (-1200.0, 0.0)
			reroute_9.location = (-440.0, -340.0)
			reroute_001_7.location = (-200.0, -340.0)
			reroute_002_4.location = (40.0, -340.0)
			reroute_003_2.location = (280.0, -340.0)
			separate_geometry.location = (540.0, 20.0)
			group_001_6.location = (540.0, -160.0)
			
			#Set dimensions
			group_output_36.width, group_output_36.height = 140.0, 100.0
			group_input_35.width, group_input_35.height = 140.0, 100.0
			store_named_attribute_002.width, store_named_attribute_002.height = 172.44415283203125, 100.0
			store_named_attribute_003.width, store_named_attribute_003.height = 169.44052124023438, 100.0
			store_named_attribute_004_1.width, store_named_attribute_004_1.height = 184.14559936523438, 100.0
			store_named_attribute_005_1.width, store_named_attribute_005_1.height = 169.42654418945312, 100.0
			mn_topo_point_mask_005.width, mn_topo_point_mask_005.height = 172.76019287109375, 100.0
			mn_topo_point_mask_006.width, mn_topo_point_mask_006.height = 185.9674072265625, 100.0
			mn_topo_point_mask_007.width, mn_topo_point_mask_007.height = 168.1260986328125, 100.0
			mn_topo_point_mask_004.width, mn_topo_point_mask_004.height = 178.538330078125, 100.0
			capture_attribute.width, capture_attribute.height = 140.0, 100.0
			group_11.width, group_11.height = 140.0, 100.0
			reroute_9.width, reroute_9.height = 16.0, 100.0
			reroute_001_7.width, reroute_001_7.height = 16.0, 100.0
			reroute_002_4.width, reroute_002_4.height = 16.0, 100.0
			reroute_003_2.width, reroute_003_2.height = 16.0, 100.0
			separate_geometry.width, separate_geometry.height = 140.0, 100.0
			group_001_6.width, group_001_6.height = 140.0, 100.0
			
			#initialize _mn_topo_assign_backbone links
			#mn_topo_point_mask_007.Is Valid -> store_named_attribute_005_1.Selection
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_007.outputs[0], store_named_attribute_005_1.inputs[1])
			#mn_topo_point_mask_006.Position -> store_named_attribute_004_1.Value
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_006.outputs[2], store_named_attribute_004_1.inputs[3])
			#mn_topo_point_mask_005.Position -> store_named_attribute_003.Value
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_005.outputs[2], store_named_attribute_003.inputs[3])
			#store_named_attribute_004_1.Geometry -> store_named_attribute_003.Geometry
			_mn_topo_assign_backbone.links.new(store_named_attribute_004_1.outputs[0], store_named_attribute_003.inputs[0])
			#store_named_attribute_003.Geometry -> store_named_attribute_005_1.Geometry
			_mn_topo_assign_backbone.links.new(store_named_attribute_003.outputs[0], store_named_attribute_005_1.inputs[0])
			#store_named_attribute_002.Geometry -> store_named_attribute_004_1.Geometry
			_mn_topo_assign_backbone.links.new(store_named_attribute_002.outputs[0], store_named_attribute_004_1.inputs[0])
			#mn_topo_point_mask_007.Position -> store_named_attribute_005_1.Value
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_007.outputs[2], store_named_attribute_005_1.inputs[3])
			#mn_topo_point_mask_006.Is Valid -> store_named_attribute_004_1.Selection
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_006.outputs[0], store_named_attribute_004_1.inputs[1])
			#mn_topo_point_mask_005.Is Valid -> store_named_attribute_003.Selection
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_005.outputs[0], store_named_attribute_003.inputs[1])
			#capture_attribute.Geometry -> store_named_attribute_002.Geometry
			_mn_topo_assign_backbone.links.new(capture_attribute.outputs[0], store_named_attribute_002.inputs[0])
			#store_named_attribute_005_1.Geometry -> group_output_36.Atoms
			_mn_topo_assign_backbone.links.new(store_named_attribute_005_1.outputs[0], group_output_36.inputs[0])
			#group_input_35.Atoms -> capture_attribute.Geometry
			_mn_topo_assign_backbone.links.new(group_input_35.outputs[0], capture_attribute.inputs[0])
			#group_11.Unique Group ID -> capture_attribute.Unique Group ID
			_mn_topo_assign_backbone.links.new(group_11.outputs[0], capture_attribute.inputs[1])
			#reroute_001_7.Output -> mn_topo_point_mask_006.Group ID
			_mn_topo_assign_backbone.links.new(reroute_001_7.outputs[0], mn_topo_point_mask_006.inputs[2])
			#capture_attribute.Unique Group ID -> reroute_9.Input
			_mn_topo_assign_backbone.links.new(capture_attribute.outputs[1], reroute_9.inputs[0])
			#reroute_9.Output -> reroute_001_7.Input
			_mn_topo_assign_backbone.links.new(reroute_9.outputs[0], reroute_001_7.inputs[0])
			#reroute_002_4.Output -> mn_topo_point_mask_005.Group ID
			_mn_topo_assign_backbone.links.new(reroute_002_4.outputs[0], mn_topo_point_mask_005.inputs[2])
			#reroute_001_7.Output -> reroute_002_4.Input
			_mn_topo_assign_backbone.links.new(reroute_001_7.outputs[0], reroute_002_4.inputs[0])
			#reroute_003_2.Output -> mn_topo_point_mask_007.Group ID
			_mn_topo_assign_backbone.links.new(reroute_003_2.outputs[0], mn_topo_point_mask_007.inputs[2])
			#reroute_002_4.Output -> reroute_003_2.Input
			_mn_topo_assign_backbone.links.new(reroute_002_4.outputs[0], reroute_003_2.inputs[0])
			#capture_attribute.Unique Group ID -> group_output_36.Unique Group ID
			_mn_topo_assign_backbone.links.new(capture_attribute.outputs[1], group_output_36.inputs[1])
			#mn_topo_point_mask_004.Is Valid -> store_named_attribute_002.Selection
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_004.outputs[0], store_named_attribute_002.inputs[1])
			#mn_topo_point_mask_004.Position -> store_named_attribute_002.Value
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_004.outputs[2], store_named_attribute_002.inputs[3])
			#store_named_attribute_005_1.Geometry -> separate_geometry.Geometry
			_mn_topo_assign_backbone.links.new(store_named_attribute_005_1.outputs[0], separate_geometry.inputs[0])
			#separate_geometry.Selection -> group_output_36.CA Atoms
			_mn_topo_assign_backbone.links.new(separate_geometry.outputs[0], group_output_36.inputs[2])
			#group_001_6.Selection -> separate_geometry.Selection
			_mn_topo_assign_backbone.links.new(group_001_6.outputs[0], separate_geometry.inputs[1])
			#reroute_9.Output -> mn_topo_point_mask_004.Group ID
			_mn_topo_assign_backbone.links.new(reroute_9.outputs[0], mn_topo_point_mask_004.inputs[2])
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
			is_even_socket.attribute_domain = 'POINT'
			
			#Socket is_odd
			is_odd_socket = _is_odd.interface.new_socket(name = "is_odd", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_odd_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_8 = _is_odd.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketInt')
			value_socket_8.subtype = 'NONE'
			value_socket_8.default_value = 0
			value_socket_8.min_value = -2147483648
			value_socket_8.max_value = 2147483647
			value_socket_8.attribute_domain = 'POINT'
			
			
			#initialize _is_odd nodes
			#node Group Input
			group_input_36 = _is_odd.nodes.new("NodeGroupInput")
			group_input_36.name = "Group Input"
			
			#node Group Output
			group_output_37 = _is_odd.nodes.new("NodeGroupOutput")
			group_output_37.name = "Group Output"
			group_output_37.is_active_output = True
			
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
			math_008_1 = _is_odd.nodes.new("ShaderNodeMath")
			math_008_1.name = "Math.008"
			math_008_1.operation = 'FLOORED_MODULO'
			math_008_1.use_clamp = False
			#Value_001
			math_008_1.inputs[1].default_value = 2.0
			
			
			
			
			#Set locations
			group_input_36.location = (-300.0, 80.0)
			group_output_37.location = (240.0, 120.0)
			boolean_math_7.location = (240.0, 20.0)
			compare_011.location = (60.0, 120.0)
			math_008_1.location = (-100.0, 120.0)
			
			#Set dimensions
			group_input_36.width, group_input_36.height = 140.0, 100.0
			group_output_37.width, group_output_37.height = 140.0, 100.0
			boolean_math_7.width, boolean_math_7.height = 140.0, 100.0
			compare_011.width, compare_011.height = 140.0, 100.0
			math_008_1.width, math_008_1.height = 140.0, 100.0
			
			#initialize _is_odd links
			#group_input_36.Value -> math_008_1.Value
			_is_odd.links.new(group_input_36.outputs[0], math_008_1.inputs[0])
			#compare_011.Result -> group_output_37.is_even
			_is_odd.links.new(compare_011.outputs[0], group_output_37.inputs[0])
			#compare_011.Result -> boolean_math_7.Boolean
			_is_odd.links.new(compare_011.outputs[0], boolean_math_7.inputs[0])
			#boolean_math_7.Boolean -> group_output_37.is_odd
			_is_odd.links.new(boolean_math_7.outputs[0], group_output_37.inputs[1])
			#math_008_1.Value -> compare_011.A
			_is_odd.links.new(math_008_1.outputs[0], compare_011.inputs[0])
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
			frame_1 = _mn_cartoon_bs_alternate_axis.nodes.new("NodeFrame")
			frame_1.label = "Only the last AA in an AH is selected"
			frame_1.name = "Frame"
			frame_1.label_size = 20
			frame_1.shrink = True
			
			#node Vector Math.005
			vector_math_005_2 = _mn_cartoon_bs_alternate_axis.nodes.new("ShaderNodeVectorMath")
			vector_math_005_2.name = "Vector Math.005"
			vector_math_005_2.operation = 'SCALE'
			
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
			group_output_38 = _mn_cartoon_bs_alternate_axis.nodes.new("NodeGroupOutput")
			group_output_38.name = "Group Output"
			group_output_38.is_active_output = True
			
			#node Index.001
			index_001 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeInputIndex")
			index_001.name = "Index.001"
			
			#node Boolean Math.010
			boolean_math_010 = _mn_cartoon_bs_alternate_axis.nodes.new("FunctionNodeBooleanMath")
			boolean_math_010.name = "Boolean Math.010"
			boolean_math_010.operation = 'AND'
			
			#node Reroute.001
			reroute_001_8 = _mn_cartoon_bs_alternate_axis.nodes.new("NodeReroute")
			reroute_001_8.name = "Reroute.001"
			#node Vector Math.004
			vector_math_004_1 = _mn_cartoon_bs_alternate_axis.nodes.new("ShaderNodeVectorMath")
			vector_math_004_1.label = "N -> C"
			vector_math_004_1.name = "Vector Math.004"
			vector_math_004_1.operation = 'SUBTRACT'
			
			#node Group Input
			group_input_37 = _mn_cartoon_bs_alternate_axis.nodes.new("NodeGroupInput")
			group_input_37.name = "Group Input"
			
			#node Vector Math
			vector_math_3 = _mn_cartoon_bs_alternate_axis.nodes.new("ShaderNodeVectorMath")
			vector_math_3.label = "C --> O"
			vector_math_3.name = "Vector Math"
			vector_math_3.operation = 'SUBTRACT'
			
			#node Integer
			integer_1 = _mn_cartoon_bs_alternate_axis.nodes.new("FunctionNodeInputInt")
			integer_1.name = "Integer"
			integer_1.integer = -1
			
			#node Compare
			compare_5 = _mn_cartoon_bs_alternate_axis.nodes.new("FunctionNodeCompare")
			compare_5.name = "Compare"
			compare_5.data_type = 'INT'
			compare_5.mode = 'ELEMENT'
			compare_5.operation = 'GREATER_THAN'
			
			#node Group.014
			group_014 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeGroup")
			group_014.name = "Group.014"
			group_014.node_tree = _sec_struct_counter
			
			#node Boolean Math
			boolean_math_8 = _mn_cartoon_bs_alternate_axis.nodes.new("FunctionNodeBooleanMath")
			boolean_math_8.name = "Boolean Math"
			boolean_math_8.operation = 'AND'
			
			#node Switch
			switch_8 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeSwitch")
			switch_8.name = "Switch"
			switch_8.input_type = 'VECTOR'
			
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
			group_12 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeGroup")
			group_12.name = "Group"
			group_12.node_tree = _field_offset
			group_12.inputs[1].hide = True
			group_12.inputs[2].hide = True
			group_12.inputs[3].hide = True
			group_12.outputs[1].hide = True
			group_12.outputs[2].hide = True
			group_12.outputs[3].hide = True
			#Input_3
			group_12.inputs[1].default_value = False
			#Input_5
			group_12.inputs[2].default_value = 0
			#Input_7
			group_12.inputs[3].default_value = 0.0
			
			#node Group.011
			group_011_1 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeGroup")
			group_011_1.name = "Group.011"
			group_011_1.node_tree = _mn_select_sec_struct
			#Socket_1
			group_011_1.inputs[0].default_value = True
			
			#node Group.005
			group_005_1 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeGroup")
			group_005_1.name = "Group.005"
			group_005_1.node_tree = _is_odd
			
			
			
			#Set parents
			compare_5.parent = frame_1
			group_014.parent = frame_1
			boolean_math_8.parent = frame_1
			group_012.parent = frame_1
			
			#Set locations
			frame_1.location = (-86.11199951171875, 65.14605712890625)
			vector_math_005_2.location = (60.0, 440.0)
			blur_attribute_001.location = (220.0, 400.0)
			switch_002_1.location = (220.0, 580.0)
			group_output_38.location = (400.0, 580.0)
			index_001.location = (-381.36767578125, 1.1884498596191406)
			boolean_math_010.location = (-41.36767578125, 101.18844604492188)
			reroute_001_8.location = (-897.6007080078125, 360.3312683105469)
			vector_math_004_1.location = (-817.6007080078125, 540.3312377929688)
			group_input_37.location = (-1077.6007080078125, 420.3312683105469)
			vector_math_3.location = (-817.6007080078125, 400.3312683105469)
			integer_1.location = (-822.031982421875, 264.41668701171875)
			compare_5.location = (-526.031982421875, 831.0416870117188)
			group_014.location = (-854.4696655273438, 787.1783447265625)
			boolean_math_8.location = (-366.0320129394531, 831.0416870117188)
			switch_8.location = (-189.45494079589844, 480.51531982421875)
			group_012.location = (-666.031982421875, 651.0416870117188)
			switch_008.location = (120.0, 100.0)
			group_12.location = (-622.031982421875, 344.41668701171875)
			group_011_1.location = (-361.36767578125, 161.18844604492188)
			group_005_1.location = (-221.36767578125, 1.1884498596191406)
			
			#Set dimensions
			frame_1.width, frame_1.height = 688.7999877929688, 326.0
			vector_math_005_2.width, vector_math_005_2.height = 140.0, 100.0
			blur_attribute_001.width, blur_attribute_001.height = 140.0, 100.0
			switch_002_1.width, switch_002_1.height = 140.0, 100.0
			group_output_38.width, group_output_38.height = 140.0, 100.0
			index_001.width, index_001.height = 140.0, 100.0
			boolean_math_010.width, boolean_math_010.height = 140.0, 100.0
			reroute_001_8.width, reroute_001_8.height = 16.0, 100.0
			vector_math_004_1.width, vector_math_004_1.height = 140.0, 100.0
			group_input_37.width, group_input_37.height = 140.0, 100.0
			vector_math_3.width, vector_math_3.height = 140.0, 100.0
			integer_1.width, integer_1.height = 140.0, 100.0
			compare_5.width, compare_5.height = 140.0, 100.0
			group_014.width, group_014.height = 140.0, 100.0
			boolean_math_8.width, boolean_math_8.height = 140.0, 100.0
			switch_8.width, switch_8.height = 140.0, 100.0
			group_012.width, group_012.height = 277.2730712890625, 100.0
			switch_008.width, switch_008.height = 140.0, 100.0
			group_12.width, group_12.height = 196.1611328125, 100.0
			group_011_1.width, group_011_1.height = 277.2730712890625, 100.0
			group_005_1.width, group_005_1.height = 140.0, 100.0
			
			#initialize _mn_cartoon_bs_alternate_axis links
			#vector_math_005_2.Vector -> switch_002_1.False
			_mn_cartoon_bs_alternate_axis.links.new(vector_math_005_2.outputs[0], switch_002_1.inputs[1])
			#blur_attribute_001.Value -> switch_002_1.True
			_mn_cartoon_bs_alternate_axis.links.new(blur_attribute_001.outputs[0], switch_002_1.inputs[2])
			#group_011_1.Is Sheet -> switch_002_1.Switch
			_mn_cartoon_bs_alternate_axis.links.new(group_011_1.outputs[1], switch_002_1.inputs[0])
			#group_input_37.C -> reroute_001_8.Input
			_mn_cartoon_bs_alternate_axis.links.new(group_input_37.outputs[1], reroute_001_8.inputs[0])
			#boolean_math_010.Boolean -> switch_008.Switch
			_mn_cartoon_bs_alternate_axis.links.new(boolean_math_010.outputs[0], switch_008.inputs[0])
			#group_005_1.is_even -> boolean_math_010.Boolean
			_mn_cartoon_bs_alternate_axis.links.new(group_005_1.outputs[0], boolean_math_010.inputs[1])
			#index_001.Index -> group_005_1.Value
			_mn_cartoon_bs_alternate_axis.links.new(index_001.outputs[0], group_005_1.inputs[0])
			#reroute_001_8.Output -> vector_math_3.Vector
			_mn_cartoon_bs_alternate_axis.links.new(reroute_001_8.outputs[0], vector_math_3.inputs[0])
			#group_011_1.Is Sheet -> boolean_math_010.Boolean
			_mn_cartoon_bs_alternate_axis.links.new(group_011_1.outputs[1], boolean_math_010.inputs[0])
			#reroute_001_8.Output -> vector_math_004_1.Vector
			_mn_cartoon_bs_alternate_axis.links.new(reroute_001_8.outputs[0], vector_math_004_1.inputs[1])
			#vector_math_005_2.Vector -> blur_attribute_001.Value
			_mn_cartoon_bs_alternate_axis.links.new(vector_math_005_2.outputs[0], blur_attribute_001.inputs[0])
			#switch_008.Output -> vector_math_005_2.Scale
			_mn_cartoon_bs_alternate_axis.links.new(switch_008.outputs[0], vector_math_005_2.inputs[3])
			#group_input_37.O -> vector_math_3.Vector
			_mn_cartoon_bs_alternate_axis.links.new(group_input_37.outputs[2], vector_math_3.inputs[1])
			#switch_002_1.Output -> group_output_38.Z Vector for Euler
			_mn_cartoon_bs_alternate_axis.links.new(switch_002_1.outputs[0], group_output_38.inputs[0])
			#vector_math_004_1.Vector -> group_output_38.X Vector for Euler
			_mn_cartoon_bs_alternate_axis.links.new(vector_math_004_1.outputs[0], group_output_38.inputs[1])
			#group_input_37.N -> vector_math_004_1.Vector
			_mn_cartoon_bs_alternate_axis.links.new(group_input_37.outputs[0], vector_math_004_1.inputs[0])
			#switch_8.Output -> vector_math_005_2.Vector
			_mn_cartoon_bs_alternate_axis.links.new(switch_8.outputs[0], vector_math_005_2.inputs[0])
			#group_014.Leading -> compare_5.A
			_mn_cartoon_bs_alternate_axis.links.new(group_014.outputs[0], compare_5.inputs[2])
			#group_014.Trailing -> compare_5.B
			_mn_cartoon_bs_alternate_axis.links.new(group_014.outputs[1], compare_5.inputs[3])
			#compare_5.Result -> boolean_math_8.Boolean
			_mn_cartoon_bs_alternate_axis.links.new(compare_5.outputs[0], boolean_math_8.inputs[0])
			#group_012.Is Helix -> boolean_math_8.Boolean
			_mn_cartoon_bs_alternate_axis.links.new(group_012.outputs[0], boolean_math_8.inputs[1])
			#vector_math_3.Vector -> switch_8.False
			_mn_cartoon_bs_alternate_axis.links.new(vector_math_3.outputs[0], switch_8.inputs[1])
			#vector_math_3.Vector -> group_12.Field
			_mn_cartoon_bs_alternate_axis.links.new(vector_math_3.outputs[0], group_12.inputs[0])
			#group_12.Field -> switch_8.True
			_mn_cartoon_bs_alternate_axis.links.new(group_12.outputs[0], switch_8.inputs[2])
			#integer_1.Integer -> group_12.Offset
			_mn_cartoon_bs_alternate_axis.links.new(integer_1.outputs[0], group_12.inputs[4])
			#boolean_math_8.Boolean -> switch_8.Switch
			_mn_cartoon_bs_alternate_axis.links.new(boolean_math_8.outputs[0], switch_8.inputs[0])
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
			selection_socket_5.attribute_domain = 'POINT'
			selection_socket_5.hide_value = True
			selection_socket_5.description = "Selection of atoms to apply this node to"
			
			#Socket BS Smoothing
			bs_smoothing_socket = _atoms_to_curves.interface.new_socket(name = "BS Smoothing", in_out='INPUT', socket_type = 'NodeSocketFloat')
			bs_smoothing_socket.subtype = 'FACTOR'
			bs_smoothing_socket.default_value = 1.0
			bs_smoothing_socket.min_value = 0.0
			bs_smoothing_socket.max_value = 1.0
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
			compare_001_3 = _atoms_to_curves.nodes.new("FunctionNodeCompare")
			compare_001_3.name = "Compare.001"
			compare_001_3.data_type = 'INT'
			compare_001_3.mode = 'ELEMENT'
			compare_001_3.operation = 'NOT_EQUAL'
			
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
			evaluate_at_index_001_3 = _atoms_to_curves.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001_3.name = "Evaluate at Index.001"
			evaluate_at_index_001_3.data_type = 'INT'
			evaluate_at_index_001_3.domain = 'POINT'
			
			#node Reroute.021
			reroute_021 = _atoms_to_curves.nodes.new("NodeReroute")
			reroute_021.name = "Reroute.021"
			#node Edge Vertices
			edge_vertices = _atoms_to_curves.nodes.new("GeometryNodeInputMeshEdgeVertices")
			edge_vertices.name = "Edge Vertices"
			
			#node Vector Math
			vector_math_4 = _atoms_to_curves.nodes.new("ShaderNodeVectorMath")
			vector_math_4.name = "Vector Math"
			vector_math_4.operation = 'DISTANCE'
			
			#node Compare
			compare_6 = _atoms_to_curves.nodes.new("FunctionNodeCompare")
			compare_6.name = "Compare"
			compare_6.data_type = 'FLOAT'
			compare_6.mode = 'ELEMENT'
			compare_6.operation = 'GREATER_THAN'
			
			#node Math.001
			math_001_5 = _atoms_to_curves.nodes.new("ShaderNodeMath")
			math_001_5.name = "Math.001"
			math_001_5.operation = 'DIVIDE'
			math_001_5.use_clamp = False
			#Value
			math_001_5.inputs[0].default_value = 60.0
			#Value_001
			math_001_5.inputs[1].default_value = 1000.0
			
			#node Boolean Math.001
			boolean_math_001_6 = _atoms_to_curves.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_6.name = "Boolean Math.001"
			boolean_math_001_6.operation = 'OR'
			
			#node Delete Geometry
			delete_geometry_1 = _atoms_to_curves.nodes.new("GeometryNodeDeleteGeometry")
			delete_geometry_1.name = "Delete Geometry"
			delete_geometry_1.domain = 'EDGE'
			delete_geometry_1.mode = 'ALL'
			
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
			store_named_attribute_2 = _atoms_to_curves.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_2.name = "Store Named Attribute"
			store_named_attribute_2.data_type = 'FLOAT_VECTOR'
			store_named_attribute_2.domain = 'POINT'
			#Selection
			store_named_attribute_2.inputs[1].default_value = True
			#Name
			store_named_attribute_2.inputs[2].default_value = "forward"
			
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
			boolean_math_005_1 = _atoms_to_curves.nodes.new("FunctionNodeBooleanMath")
			boolean_math_005_1.name = "Boolean Math.005"
			boolean_math_005_1.operation = 'AND'
			
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
			boolean_math_004_3 = _atoms_to_curves.nodes.new("FunctionNodeBooleanMath")
			boolean_math_004_3.name = "Boolean Math.004"
			boolean_math_004_3.operation = 'OR'
			
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
			reroute_002_5 = _atoms_to_curves.nodes.new("NodeReroute")
			reroute_002_5.name = "Reroute.002"
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
			group_input_001_1 = _atoms_to_curves.nodes.new("NodeGroupInput")
			group_input_001_1.name = "Group Input.001"
			
			#node Group Output
			group_output_39 = _atoms_to_curves.nodes.new("NodeGroupOutput")
			group_output_39.name = "Group Output"
			group_output_39.is_active_output = True
			
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
			group_13 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_13.name = "Group"
			group_13.node_tree = _bs_smooth
			#Input_3
			group_13.inputs[2].default_value = 3
			
			#node Group.023
			group_023_1 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_023_1.name = "Group.023"
			group_023_1.node_tree = _expand_selection
			#Input_2
			group_023_1.inputs[1].default_value = 1
			
			#node Group.037
			group_037 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_037.name = "Group.037"
			group_037.node_tree = _mn_select_sec_struct
			#Socket_1
			group_037.inputs[0].default_value = True
			
			#node Group Input
			group_input_38 = _atoms_to_curves.nodes.new("NodeGroupInput")
			group_input_38.name = "Group Input"
			
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
			curve_to_mesh_2 = _atoms_to_curves.nodes.new("GeometryNodeCurveToMesh")
			curve_to_mesh_2.name = "Curve to Mesh"
			#Fill Caps
			curve_to_mesh_2.inputs[2].default_value = False
			
			#node Named Attribute.018
			named_attribute_018 = _atoms_to_curves.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_018.name = "Named Attribute.018"
			named_attribute_018.data_type = 'INT'
			#Name
			named_attribute_018.inputs[0].default_value = "chain_id"
			
			#node Group.001
			group_001_7 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_001_7.name = "Group.001"
			group_001_7.node_tree = is_alpha_carbon
			#Socket_1
			group_001_7.inputs[0].default_value = True
			#Socket_3
			group_001_7.inputs[1].default_value = False
			
			#node Group.006
			group_006_1 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_006_1.name = "Group.006"
			group_006_1.node_tree = _mn_topo_assign_backbone
			
			#node Group.008
			group_008 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_008.name = "Group.008"
			group_008.node_tree = _mn_cartoon_bs_alternate_axis
			
			
			
			#Set parents
			compare_001_3.parent = frame_006
			named_attribute_011.parent = frame_006
			evaluate_at_index_3.parent = frame_006
			evaluate_at_index_001_3.parent = frame_006
			reroute_021.parent = frame_006
			edge_vertices.parent = frame_006
			vector_math_4.parent = frame_006
			compare_6.parent = frame_006
			math_001_5.parent = frame_006
			boolean_math_001_6.parent = frame_006
			delete_geometry_1.parent = frame_006
			store_named_attribute_001.parent = frame_007
			store_named_attribute_2.parent = frame_007
			position_002.parent = frame_007
			store_named_attribute_015.parent = frame_008
			store_named_attribute_016.parent = frame_008
			store_named_attribute_017.parent = frame_008
			named_attribute_012.parent = frame_008
			named_attribute_013.parent = frame_008
			named_attribute_014.parent = frame_008
			group_022.parent = frame_2
			group_035.parent = frame_2
			boolean_math_005_1.parent = frame_2
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
			reroute_002_5.parent = frame_001
			separate_geometry_006.parent = frame_001
			separate_geometry_007.parent = frame_001
			separate_geometry_008.parent = frame_001
			group_012_1.parent = frame_007
			group_013.parent = frame_007
			separate_geometry_003.parent = frame_002
			separate_geometry_001.parent = frame_002
			mesh_to_points.parent = frame_002
			points_to_curves.parent = frame_002
			curve_to_mesh_2.parent = frame_002
			named_attribute_018.parent = frame_002
			group_001_7.parent = frame_002
			group_006_1.parent = frame_002
			group_008.parent = frame_008
			
			#Set locations
			frame_006.location = (-26.0, 380.0)
			frame_007.location = (-168.0, 46.0)
			frame_008.location = (-166.0, 3.0)
			frame_2.location = (6042.0, 80.0)
			frame_001.location = (458.0, -8.0)
			frame_002.location = (0.0, 0.0)
			compare_001_3.location = (-1907.6533203125, 300.176513671875)
			named_attribute_011.location = (-2304.4140625, 25.7803955078125)
			evaluate_at_index_3.location = (-2067.6533203125, 300.176513671875)
			evaluate_at_index_001_3.location = (-2067.6533203125, 120.176513671875)
			reroute_021.location = (-2087.6533203125, 100.176513671875)
			edge_vertices.location = (-2304.4140625, 165.7803955078125)
			vector_math_4.location = (-2064.4140625, -54.2196044921875)
			compare_6.location = (-1904.4140625, -54.2196044921875)
			math_001_5.location = (-2064.4140625, -194.2196044921875)
			boolean_math_001_6.location = (-1740.0, 300.0)
			delete_geometry_1.location = (-1740.0, 480.0)
			store_named_attribute_001.location = (-1062.2197265625, 834.4013671875)
			store_named_attribute_2.location = (-1222.2197265625, 834.4013671875)
			position_002.location = (-1222.2197265625, 474.4012451171875)
			store_named_attribute_015.location = (-563.97314453125, 856.68115234375)
			store_named_attribute_016.location = (-383.97314453125, 856.68115234375)
			store_named_attribute_017.location = (-203.97314453125, 856.68115234375)
			named_attribute_012.location = (-743.97314453125, 616.68115234375)
			named_attribute_013.location = (-743.97314453125, 336.68115234375)
			named_attribute_014.location = (-743.97314453125, 476.68115234375)
			group_022.location = (-5080.0, -580.0)
			group_035.location = (-5080.0, -860.0)
			boolean_math_005_1.location = (-4840.0, -660.0)
			boolean_math_009.location = (-4620.0, -660.0)
			boolean_math_007.location = (-4800.0, -60.0)
			group_036.location = (-5040.0, -180.0)
			boolean_math_010_1.location = (-4800.0, -220.0)
			boolean_math_006.location = (-4360.0, -320.0)
			boolean_math_008.location = (-4840.0, -820.0)
			boolean_math_011.location = (-4580.0, -100.0)
			group_034.location = (-5040.0, 100.0)
			group_024_1.location = (-5532.35107421875, -374.12896728515625)
			boolean_math_004_3.location = (1120.0, 520.0)
			mesh_to_curve_004.location = (1200.0, 940.0)
			mesh_to_curve_003.location = (1200.0, 820.0)
			mesh_to_curve_001.location = (1200.0, 700.0)
			mesh_to_curve.location = (1200.0, 580.0)
			reroute_023.location = (1260.0, 980.0)
			reroute_002_5.location = (960.0, 860.0)
			separate_geometry_006.location = (1040.0, 820.0)
			separate_geometry_007.location = (1040.0, 700.0)
			separate_geometry_008.location = (1040.0, 580.0)
			group_input_001_1.location = (-180.0, 720.0)
			group_output_39.location = (2120.0, 920.0)
			group_012_1.location = (-1222.2197265625, 614.4013671875)
			group_013.location = (-1062.2197265625, 614.4013671875)
			group_13.location = (60.0, 840.0)
			group_023_1.location = (960.0, 520.0)
			group_037.location = (880.0, 760.0)
			group_input_38.location = (-4220.0, 700.0)
			store_named_attribute_019.location = (-2860.0, 820.0)
			index_002.location = (-2860.0, 620.0)
			separate_geometry_003.location = (-3780.0, 780.0)
			separate_geometry_001.location = (-3600.0, 780.0)
			mesh_to_points.location = (-3420.0, 780.0)
			points_to_curves.location = (-3260.0, 780.0)
			curve_to_mesh_2.location = (-3100.0, 780.0)
			named_attribute_018.location = (-3420.0, 600.0)
			group_001_7.location = (-3780.0, 620.0)
			group_006_1.location = (-4020.0, 780.0)
			group_008.location = (-543.97314453125, 596.68115234375)
			
			#Set dimensions
			frame_006.width, frame_006.height = 764.5, 893.0
			frame_007.width, frame_007.height = 360.0, 480.0
			frame_008.width, frame_008.height = 740.0, 712.0
			frame_2.width, frame_2.height = 1372.5, 1282.0
			frame_001.width, frame_001.height = 444.0, 573.0
			frame_002.width, frame_002.height = 1120.0, 372.0
			compare_001_3.width, compare_001_3.height = 140.0, 100.0
			named_attribute_011.width, named_attribute_011.height = 140.0, 100.0
			evaluate_at_index_3.width, evaluate_at_index_3.height = 140.0, 100.0
			evaluate_at_index_001_3.width, evaluate_at_index_001_3.height = 140.0, 100.0
			reroute_021.width, reroute_021.height = 16.0, 100.0
			edge_vertices.width, edge_vertices.height = 140.0, 100.0
			vector_math_4.width, vector_math_4.height = 140.0, 100.0
			compare_6.width, compare_6.height = 140.0, 100.0
			math_001_5.width, math_001_5.height = 140.0, 100.0
			boolean_math_001_6.width, boolean_math_001_6.height = 140.0, 100.0
			delete_geometry_1.width, delete_geometry_1.height = 140.0, 100.0
			store_named_attribute_001.width, store_named_attribute_001.height = 140.0, 100.0
			store_named_attribute_2.width, store_named_attribute_2.height = 140.0, 100.0
			position_002.width, position_002.height = 140.0, 100.0
			store_named_attribute_015.width, store_named_attribute_015.height = 140.0, 100.0
			store_named_attribute_016.width, store_named_attribute_016.height = 140.0, 100.0
			store_named_attribute_017.width, store_named_attribute_017.height = 140.0, 100.0
			named_attribute_012.width, named_attribute_012.height = 140.0, 100.0
			named_attribute_013.width, named_attribute_013.height = 140.0, 100.0
			named_attribute_014.width, named_attribute_014.height = 140.0, 100.0
			group_022.width, group_022.height = 140.0, 100.0
			group_035.width, group_035.height = 140.0, 100.0
			boolean_math_005_1.width, boolean_math_005_1.height = 140.0, 100.0
			boolean_math_009.width, boolean_math_009.height = 140.0, 100.0
			boolean_math_007.width, boolean_math_007.height = 140.0, 100.0
			group_036.width, group_036.height = 140.0, 100.0
			boolean_math_010_1.width, boolean_math_010_1.height = 140.0, 100.0
			boolean_math_006.width, boolean_math_006.height = 140.0, 100.0
			boolean_math_008.width, boolean_math_008.height = 140.0, 100.0
			boolean_math_011.width, boolean_math_011.height = 140.0, 100.0
			group_034.width, group_034.height = 140.0, 100.0
			group_024_1.width, group_024_1.height = 158.9053955078125, 100.0
			boolean_math_004_3.width, boolean_math_004_3.height = 140.0, 100.0
			mesh_to_curve_004.width, mesh_to_curve_004.height = 140.0, 100.0
			mesh_to_curve_003.width, mesh_to_curve_003.height = 140.0, 100.0
			mesh_to_curve_001.width, mesh_to_curve_001.height = 140.0, 100.0
			mesh_to_curve.width, mesh_to_curve.height = 140.0, 100.0
			reroute_023.width, reroute_023.height = 16.0, 100.0
			reroute_002_5.width, reroute_002_5.height = 16.0, 100.0
			separate_geometry_006.width, separate_geometry_006.height = 140.0, 100.0
			separate_geometry_007.width, separate_geometry_007.height = 140.0, 100.0
			separate_geometry_008.width, separate_geometry_008.height = 140.0, 100.0
			group_input_001_1.width, group_input_001_1.height = 140.0, 100.0
			group_output_39.width, group_output_39.height = 140.0, 100.0
			group_012_1.width, group_012_1.height = 140.0, 100.0
			group_013.width, group_013.height = 140.0, 100.0
			group_13.width, group_13.height = 374.382080078125, 100.0
			group_023_1.width, group_023_1.height = 140.0, 100.0
			group_037.width, group_037.height = 233.448486328125, 100.0
			group_input_38.width, group_input_38.height = 140.0, 100.0
			store_named_attribute_019.width, store_named_attribute_019.height = 140.0, 100.0
			index_002.width, index_002.height = 140.0, 100.0
			separate_geometry_003.width, separate_geometry_003.height = 140.0, 100.0
			separate_geometry_001.width, separate_geometry_001.height = 140.0, 100.0
			mesh_to_points.width, mesh_to_points.height = 140.0, 100.0
			points_to_curves.width, points_to_curves.height = 140.0, 100.0
			curve_to_mesh_2.width, curve_to_mesh_2.height = 140.0, 100.0
			named_attribute_018.width, named_attribute_018.height = 140.0, 100.0
			group_001_7.width, group_001_7.height = 140.0, 100.0
			group_006_1.width, group_006_1.height = 206.7611083984375, 100.0
			group_008.width, group_008.height = 318.43975830078125, 100.0
			
			#initialize _atoms_to_curves links
			#group_023_1.Boolean -> boolean_math_004_3.Boolean
			_atoms_to_curves.links.new(group_023_1.outputs[0], boolean_math_004_3.inputs[0])
			#group_024_1.Is Helix -> boolean_math_010_1.Boolean
			_atoms_to_curves.links.new(group_024_1.outputs[0], boolean_math_010_1.inputs[1])
			#group_024_1.Is Sheet -> group_036.Value
			_atoms_to_curves.links.new(group_024_1.outputs[1], group_036.inputs[1])
			#group_024_1.Is Sheet -> boolean_math_005_1.Boolean
			_atoms_to_curves.links.new(group_024_1.outputs[1], boolean_math_005_1.inputs[0])
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
			#group_012_1.Field -> store_named_attribute_2.Value
			_atoms_to_curves.links.new(group_012_1.outputs[0], store_named_attribute_2.inputs[3])
			#group_037.Is Helix -> separate_geometry_006.Selection
			_atoms_to_curves.links.new(group_037.outputs[0], separate_geometry_006.inputs[1])
			#group_024_1.Is Helix -> group_035.Value
			_atoms_to_curves.links.new(group_024_1.outputs[0], group_035.inputs[1])
			#boolean_math_006.Boolean -> boolean_math_004_3.Boolean
			_atoms_to_curves.links.new(boolean_math_006.outputs[0], boolean_math_004_3.inputs[1])
			#group_024_1.Is Sheet -> boolean_math_008.Boolean
			_atoms_to_curves.links.new(group_024_1.outputs[1], boolean_math_008.inputs[0])
			#separate_geometry_008.Selection -> mesh_to_curve.Mesh
			_atoms_to_curves.links.new(separate_geometry_008.outputs[0], mesh_to_curve.inputs[0])
			#boolean_math_007.Boolean -> boolean_math_011.Boolean
			_atoms_to_curves.links.new(boolean_math_007.outputs[0], boolean_math_011.inputs[0])
			#group_022.Value -> boolean_math_005_1.Boolean
			_atoms_to_curves.links.new(group_022.outputs[1], boolean_math_005_1.inputs[1])
			#store_named_attribute_2.Geometry -> store_named_attribute_001.Geometry
			_atoms_to_curves.links.new(store_named_attribute_2.outputs[0], store_named_attribute_001.inputs[0])
			#group_024_1.Is Helix -> group_022.Value
			_atoms_to_curves.links.new(group_024_1.outputs[0], group_022.inputs[1])
			#boolean_math_009.Boolean -> boolean_math_006.Boolean
			_atoms_to_curves.links.new(boolean_math_009.outputs[0], boolean_math_006.inputs[1])
			#reroute_002_5.Output -> separate_geometry_006.Geometry
			_atoms_to_curves.links.new(reroute_002_5.outputs[0], separate_geometry_006.inputs[0])
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
			#boolean_math_005_1.Boolean -> boolean_math_009.Boolean
			_atoms_to_curves.links.new(boolean_math_005_1.outputs[0], boolean_math_009.inputs[0])
			#boolean_math_011.Boolean -> boolean_math_006.Boolean
			_atoms_to_curves.links.new(boolean_math_011.outputs[0], boolean_math_006.inputs[0])
			#reroute_023.Output -> group_output_39.CA Mesh Line
			_atoms_to_curves.links.new(reroute_023.outputs[0], group_output_39.inputs[0])
			#mesh_to_curve_001.Curve -> group_output_39.BS Splines
			_atoms_to_curves.links.new(mesh_to_curve_001.outputs[0], group_output_39.inputs[4])
			#mesh_to_curve.Curve -> group_output_39.Loop Splines
			_atoms_to_curves.links.new(mesh_to_curve.outputs[0], group_output_39.inputs[6])
			#mesh_to_curve_003.Curve -> group_output_39.AH Splines
			_atoms_to_curves.links.new(mesh_to_curve_003.outputs[0], group_output_39.inputs[2])
			#reroute_002_5.Output -> mesh_to_curve_004.Mesh
			_atoms_to_curves.links.new(reroute_002_5.outputs[0], mesh_to_curve_004.inputs[0])
			#mesh_to_curve_004.Curve -> group_output_39.CA Splines
			_atoms_to_curves.links.new(mesh_to_curve_004.outputs[0], group_output_39.inputs[1])
			#edge_vertices.Vertex Index 2 -> evaluate_at_index_001_3.Index
			_atoms_to_curves.links.new(edge_vertices.outputs[1], evaluate_at_index_001_3.inputs[0])
			#edge_vertices.Vertex Index 1 -> evaluate_at_index_3.Index
			_atoms_to_curves.links.new(edge_vertices.outputs[0], evaluate_at_index_3.inputs[0])
			#reroute_021.Output -> evaluate_at_index_001_3.Value
			_atoms_to_curves.links.new(reroute_021.outputs[0], evaluate_at_index_001_3.inputs[1])
			#evaluate_at_index_001_3.Value -> compare_001_3.B
			_atoms_to_curves.links.new(evaluate_at_index_001_3.outputs[0], compare_001_3.inputs[3])
			#evaluate_at_index_3.Value -> compare_001_3.A
			_atoms_to_curves.links.new(evaluate_at_index_3.outputs[0], compare_001_3.inputs[2])
			#reroute_021.Output -> evaluate_at_index_3.Value
			_atoms_to_curves.links.new(reroute_021.outputs[0], evaluate_at_index_3.inputs[1])
			#named_attribute_011.Attribute -> reroute_021.Input
			_atoms_to_curves.links.new(named_attribute_011.outputs[0], reroute_021.inputs[0])
			#compare_001_3.Result -> boolean_math_001_6.Boolean
			_atoms_to_curves.links.new(compare_001_3.outputs[0], boolean_math_001_6.inputs[0])
			#boolean_math_001_6.Boolean -> delete_geometry_1.Selection
			_atoms_to_curves.links.new(boolean_math_001_6.outputs[0], delete_geometry_1.inputs[1])
			#edge_vertices.Position 1 -> vector_math_4.Vector
			_atoms_to_curves.links.new(edge_vertices.outputs[2], vector_math_4.inputs[0])
			#edge_vertices.Position 2 -> vector_math_4.Vector
			_atoms_to_curves.links.new(edge_vertices.outputs[3], vector_math_4.inputs[1])
			#vector_math_4.Value -> compare_6.A
			_atoms_to_curves.links.new(vector_math_4.outputs[1], compare_6.inputs[0])
			#compare_6.Result -> boolean_math_001_6.Boolean
			_atoms_to_curves.links.new(compare_6.outputs[0], boolean_math_001_6.inputs[1])
			#math_001_5.Value -> compare_6.B
			_atoms_to_curves.links.new(math_001_5.outputs[0], compare_6.inputs[1])
			#store_named_attribute_019.Geometry -> delete_geometry_1.Geometry
			_atoms_to_curves.links.new(store_named_attribute_019.outputs[0], delete_geometry_1.inputs[0])
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
			#group_13.Geometry -> reroute_002_5.Input
			_atoms_to_curves.links.new(group_13.outputs[0], reroute_002_5.inputs[0])
			#reroute_002_5.Output -> reroute_023.Input
			_atoms_to_curves.links.new(reroute_002_5.outputs[0], reroute_023.inputs[0])
			#reroute_002_5.Output -> separate_geometry_007.Geometry
			_atoms_to_curves.links.new(reroute_002_5.outputs[0], separate_geometry_007.inputs[0])
			#reroute_002_5.Output -> separate_geometry_008.Geometry
			_atoms_to_curves.links.new(reroute_002_5.outputs[0], separate_geometry_008.inputs[0])
			#boolean_math_004_3.Boolean -> separate_geometry_008.Selection
			_atoms_to_curves.links.new(boolean_math_004_3.outputs[0], separate_geometry_008.inputs[1])
			#group_037.Is Sheet -> separate_geometry_007.Selection
			_atoms_to_curves.links.new(group_037.outputs[1], separate_geometry_007.inputs[1])
			#group_037.Is Loop -> group_023_1.Input
			_atoms_to_curves.links.new(group_037.outputs[3], group_023_1.inputs[0])
			#separate_geometry_006.Selection -> group_output_39.AH Mesh Line
			_atoms_to_curves.links.new(separate_geometry_006.outputs[0], group_output_39.inputs[3])
			#separate_geometry_007.Selection -> group_output_39.BS Mesh Line
			_atoms_to_curves.links.new(separate_geometry_007.outputs[0], group_output_39.inputs[5])
			#separate_geometry_008.Selection -> group_output_39.Loop Mesh Line
			_atoms_to_curves.links.new(separate_geometry_008.outputs[0], group_output_39.inputs[7])
			#store_named_attribute_017.Geometry -> group_13.Geometry
			_atoms_to_curves.links.new(store_named_attribute_017.outputs[0], group_13.inputs[0])
			#group_input_001_1.BS Smoothing -> group_13.Factor
			_atoms_to_curves.links.new(group_input_001_1.outputs[2], group_13.inputs[1])
			#index_002.Index -> store_named_attribute_019.Value
			_atoms_to_curves.links.new(index_002.outputs[0], store_named_attribute_019.inputs[3])
			#group_input_38.Atoms -> group_006_1.Atoms
			_atoms_to_curves.links.new(group_input_38.outputs[0], group_006_1.inputs[0])
			#separate_geometry_003.Selection -> separate_geometry_001.Geometry
			_atoms_to_curves.links.new(separate_geometry_003.outputs[0], separate_geometry_001.inputs[0])
			#separate_geometry_001.Selection -> mesh_to_points.Mesh
			_atoms_to_curves.links.new(separate_geometry_001.outputs[0], mesh_to_points.inputs[0])
			#mesh_to_points.Points -> points_to_curves.Points
			_atoms_to_curves.links.new(mesh_to_points.outputs[0], points_to_curves.inputs[0])
			#named_attribute_018.Attribute -> points_to_curves.Curve Group ID
			_atoms_to_curves.links.new(named_attribute_018.outputs[0], points_to_curves.inputs[1])
			#points_to_curves.Curves -> curve_to_mesh_2.Curve
			_atoms_to_curves.links.new(points_to_curves.outputs[0], curve_to_mesh_2.inputs[0])
			#delete_geometry_1.Geometry -> store_named_attribute_2.Geometry
			_atoms_to_curves.links.new(delete_geometry_1.outputs[0], store_named_attribute_2.inputs[0])
			#group_006_1.Atoms -> separate_geometry_003.Geometry
			_atoms_to_curves.links.new(group_006_1.outputs[0], separate_geometry_003.inputs[0])
			#group_input_38.Selection -> separate_geometry_003.Selection
			_atoms_to_curves.links.new(group_input_38.outputs[1], separate_geometry_003.inputs[1])
			#curve_to_mesh_2.Mesh -> store_named_attribute_019.Geometry
			_atoms_to_curves.links.new(curve_to_mesh_2.outputs[0], store_named_attribute_019.inputs[0])
			#group_001_7.Selection -> separate_geometry_001.Selection
			_atoms_to_curves.links.new(group_001_7.outputs[0], separate_geometry_001.inputs[1])
			return _atoms_to_curves

		_atoms_to_curves = _atoms_to_curves_node_group()

		#initialize _mn_utils_style_cartoon node group
		def _mn_utils_style_cartoon_node_group():
			_mn_utils_style_cartoon = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_utils_style_cartoon")

			_mn_utils_style_cartoon.color_tag = 'GEOMETRY'
			_mn_utils_style_cartoon.description = ""

			_mn_utils_style_cartoon.is_modifier = True
			
			#_mn_utils_style_cartoon interface
			#Socket Cartoon Mesh
			cartoon_mesh_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Cartoon Mesh", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			cartoon_mesh_socket.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket_3 = _mn_utils_style_cartoon.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_3.attribute_domain = 'POINT'
			atoms_socket_3.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket_6 = _mn_utils_style_cartoon.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_6.attribute_domain = 'POINT'
			selection_socket_6.hide_value = True
			selection_socket_6.description = "Selection of atoms to apply this node to"
			
			#Socket Shade Smooth
			shade_smooth_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Shade Smooth", in_out='INPUT', socket_type = 'NodeSocketBool')
			shade_smooth_socket.attribute_domain = 'POINT'
			shade_smooth_socket.description = "Apply smooth shading to the created geometry"
			
			#Socket Interpolate Color
			interpolate_color_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Interpolate Color", in_out='INPUT', socket_type = 'NodeSocketBool')
			interpolate_color_socket.attribute_domain = 'POINT'
			interpolate_color_socket.description = "Interpolate between distinct color selections"
			
			#Socket Material
			material_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial')
			material_socket.attribute_domain = 'POINT'
			material_socket.description = "Material to apply to the resulting geometry"
			
			#Panel Arrows
			arrows_panel = _mn_utils_style_cartoon.interface.new_panel("Arrows")
			#Socket As Arrows
			as_arrows_socket = _mn_utils_style_cartoon.interface.new_socket(name = "As Arrows", in_out='INPUT', socket_type = 'NodeSocketBool', parent = arrows_panel)
			as_arrows_socket.attribute_domain = 'POINT'
			as_arrows_socket.description = "Render beta-strands with directional arrows."
			
			#Socket Arrows Sharp
			arrows_sharp_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Arrows Sharp", in_out='INPUT', socket_type = 'NodeSocketBool', parent = arrows_panel)
			arrows_sharp_socket.attribute_domain = 'POINT'
			
			#Socket Arrows Point
			arrows_point_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Arrows Point", in_out='INPUT', socket_type = 'NodeSocketBool', parent = arrows_panel)
			arrows_point_socket.attribute_domain = 'POINT'
			
			#Socket Arrow Thickness Scale
			arrow_thickness_scale_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Arrow Thickness Scale", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = arrows_panel)
			arrow_thickness_scale_socket.subtype = 'NONE'
			arrow_thickness_scale_socket.default_value = 1.0
			arrow_thickness_scale_socket.min_value = 0.0
			arrow_thickness_scale_socket.max_value = 10000.0
			arrow_thickness_scale_socket.attribute_domain = 'POINT'
			
			#Socket Arrow Width Scale
			arrow_width_scale_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Arrow Width Scale", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = arrows_panel)
			arrow_width_scale_socket.subtype = 'NONE'
			arrow_width_scale_socket.default_value = 1.0
			arrow_width_scale_socket.min_value = -10000.0
			arrow_width_scale_socket.max_value = 10000.0
			arrow_width_scale_socket.attribute_domain = 'POINT'
			
			
			#Panel Profile
			profile_panel = _mn_utils_style_cartoon.interface.new_panel("Profile")
			#Socket Profile Curve
			profile_curve_socket_1 = _mn_utils_style_cartoon.interface.new_socket(name = "Profile Curve", in_out='INPUT', socket_type = 'NodeSocketGeometry', parent = profile_panel)
			profile_curve_socket_1.attribute_domain = 'POINT'
			profile_curve_socket_1.description = "A custom curve-cirlce making SS ribbons."
			
			#Socket Profile Resolution
			profile_resolution_socket_1 = _mn_utils_style_cartoon.interface.new_socket(name = "Profile Resolution", in_out='INPUT', socket_type = 'NodeSocketInt', parent = profile_panel)
			profile_resolution_socket_1.subtype = 'NONE'
			profile_resolution_socket_1.default_value = 4
			profile_resolution_socket_1.min_value = 4
			profile_resolution_socket_1.max_value = 100
			profile_resolution_socket_1.attribute_domain = 'POINT'
			
			
			#Panel Sheet
			sheet_panel = _mn_utils_style_cartoon.interface.new_panel("Sheet")
			#Socket Sheet Rotate
			sheet_rotate_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Sheet Rotate", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = sheet_panel)
			sheet_rotate_socket.subtype = 'NONE'
			sheet_rotate_socket.default_value = 0.0
			sheet_rotate_socket.min_value = -3.4028234663852886e+38
			sheet_rotate_socket.max_value = 3.4028234663852886e+38
			sheet_rotate_socket.attribute_domain = 'POINT'
			
			#Socket Sheet Thickness
			sheet_thickness_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Sheet Thickness", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = sheet_panel)
			sheet_thickness_socket.subtype = 'NONE'
			sheet_thickness_socket.default_value = 0.5
			sheet_thickness_socket.min_value = 0.0
			sheet_thickness_socket.max_value = 3.4028234663852886e+38
			sheet_thickness_socket.attribute_domain = 'POINT'
			
			#Socket Sheet Width
			sheet_width_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Sheet Width", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = sheet_panel)
			sheet_width_socket.subtype = 'NONE'
			sheet_width_socket.default_value = 2.0
			sheet_width_socket.min_value = 0.0
			sheet_width_socket.max_value = 10000.0
			sheet_width_socket.attribute_domain = 'POINT'
			
			#Socket Sheet Smoothing
			sheet_smoothing_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Sheet Smoothing", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = sheet_panel)
			sheet_smoothing_socket.subtype = 'NONE'
			sheet_smoothing_socket.default_value = 1.0
			sheet_smoothing_socket.min_value = 0.0
			sheet_smoothing_socket.max_value = 1.0
			sheet_smoothing_socket.attribute_domain = 'POINT'
			
			#Socket Sheet Subdivision
			sheet_subdivision_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Sheet Subdivision", in_out='INPUT', socket_type = 'NodeSocketInt', parent = sheet_panel)
			sheet_subdivision_socket.subtype = 'NONE'
			sheet_subdivision_socket.default_value = 3
			sheet_subdivision_socket.min_value = 1
			sheet_subdivision_socket.max_value = 20
			sheet_subdivision_socket.attribute_domain = 'POINT'
			
			
			#Panel Cylinder
			cylinder_panel = _mn_utils_style_cartoon.interface.new_panel("Cylinder")
			#Socket As Cylinders
			as_cylinders_socket = _mn_utils_style_cartoon.interface.new_socket(name = "As Cylinders", in_out='INPUT', socket_type = 'NodeSocketBool', parent = cylinder_panel)
			as_cylinders_socket.attribute_domain = 'POINT'
			
			#Socket Cylinder Curved
			cylinder_curved_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Cylinder Curved", in_out='INPUT', socket_type = 'NodeSocketBool', parent = cylinder_panel)
			cylinder_curved_socket.attribute_domain = 'POINT'
			
			#Socket Cylinder Radius
			cylinder_radius_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Cylinder Radius", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = cylinder_panel)
			cylinder_radius_socket.subtype = 'NONE'
			cylinder_radius_socket.default_value = 2.0
			cylinder_radius_socket.min_value = 0.0
			cylinder_radius_socket.max_value = 10000.0
			cylinder_radius_socket.attribute_domain = 'POINT'
			
			#Socket Cylinder Resolution
			cylinder_resolution_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Cylinder Resolution", in_out='INPUT', socket_type = 'NodeSocketInt', parent = cylinder_panel)
			cylinder_resolution_socket.subtype = 'NONE'
			cylinder_resolution_socket.default_value = 12
			cylinder_resolution_socket.min_value = 3
			cylinder_resolution_socket.max_value = 512
			cylinder_resolution_socket.attribute_domain = 'POINT'
			
			#Socket Cylinder Subdivisions
			cylinder_subdivisions_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Cylinder Subdivisions", in_out='INPUT', socket_type = 'NodeSocketInt', parent = cylinder_panel)
			cylinder_subdivisions_socket.subtype = 'NONE'
			cylinder_subdivisions_socket.default_value = 5
			cylinder_subdivisions_socket.min_value = 1
			cylinder_subdivisions_socket.max_value = 2147483647
			cylinder_subdivisions_socket.attribute_domain = 'POINT'
			
			
			#Panel Helix
			helix_panel = _mn_utils_style_cartoon.interface.new_panel("Helix")
			#Socket Helix Rotate
			helix_rotate_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Helix Rotate", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = helix_panel)
			helix_rotate_socket.subtype = 'NONE'
			helix_rotate_socket.default_value = 0.0
			helix_rotate_socket.min_value = -3.4028234663852886e+38
			helix_rotate_socket.max_value = 3.4028234663852886e+38
			helix_rotate_socket.attribute_domain = 'POINT'
			
			#Socket Helix Thickness
			helix_thickness_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Helix Thickness", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = helix_panel)
			helix_thickness_socket.subtype = 'NONE'
			helix_thickness_socket.default_value = 0.5
			helix_thickness_socket.min_value = 0.0
			helix_thickness_socket.max_value = 10000.0
			helix_thickness_socket.attribute_domain = 'POINT'
			
			#Socket Helix Width
			helix_width_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Helix Width", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = helix_panel)
			helix_width_socket.subtype = 'NONE'
			helix_width_socket.default_value = 2.0
			helix_width_socket.min_value = -3.4028234663852886e+38
			helix_width_socket.max_value = 3.4028234663852886e+38
			helix_width_socket.attribute_domain = 'POINT'
			
			#Socket Helix Subdivisions
			helix_subdivisions_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Helix Subdivisions", in_out='INPUT', socket_type = 'NodeSocketInt', parent = helix_panel)
			helix_subdivisions_socket.subtype = 'NONE'
			helix_subdivisions_socket.default_value = 5
			helix_subdivisions_socket.min_value = 1
			helix_subdivisions_socket.max_value = 20
			helix_subdivisions_socket.attribute_domain = 'POINT'
			
			#Socket Helix smoothing
			helix_smoothing_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Helix smoothing", in_out='INPUT', socket_type = 'NodeSocketBool', parent = helix_panel)
			helix_smoothing_socket.attribute_domain = 'POINT'
			helix_smoothing_socket.description = "Smoothen out AH to be more cylindrical."
			
			
			#Panel Loop
			loop_panel = _mn_utils_style_cartoon.interface.new_panel("Loop")
			#Socket Loop Subdivisions
			loop_subdivisions_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Loop Subdivisions", in_out='INPUT', socket_type = 'NodeSocketInt', parent = loop_panel)
			loop_subdivisions_socket.subtype = 'NONE'
			loop_subdivisions_socket.default_value = 6
			loop_subdivisions_socket.min_value = 1
			loop_subdivisions_socket.max_value = 2147483647
			loop_subdivisions_socket.attribute_domain = 'POINT'
			
			#Socket Loop Radius
			loop_radius_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Loop Radius", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = loop_panel)
			loop_radius_socket.subtype = 'NONE'
			loop_radius_socket.default_value = 0.30000001192092896
			loop_radius_socket.min_value = 0.0
			loop_radius_socket.max_value = 3.0
			loop_radius_socket.attribute_domain = 'POINT'
			
			#Socket Loop Resolution
			loop_resolution_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Loop Resolution", in_out='INPUT', socket_type = 'NodeSocketInt', parent = loop_panel)
			loop_resolution_socket.subtype = 'NONE'
			loop_resolution_socket.default_value = 8
			loop_resolution_socket.min_value = 3
			loop_resolution_socket.max_value = 512
			loop_resolution_socket.attribute_domain = 'POINT'
			
			
			
			#initialize _mn_utils_style_cartoon nodes
			#node Frame.006
			frame_006_1 = _mn_utils_style_cartoon.nodes.new("NodeFrame")
			frame_006_1.label = "Create Alpha-Helix Cylinder Geometry"
			frame_006_1.name = "Frame.006"
			frame_006_1.label_size = 20
			frame_006_1.shrink = True
			
			#node Frame.009
			frame_009 = _mn_utils_style_cartoon.nodes.new("NodeFrame")
			frame_009.label = "Straight cylinder if selected or less <= 4 AA"
			frame_009.name = "Frame.009"
			frame_009.label_size = 20
			frame_009.shrink = True
			
			#node Frame.008
			frame_008_1 = _mn_utils_style_cartoon.nodes.new("NodeFrame")
			frame_008_1.label = "Offset to be centre of helix"
			frame_008_1.name = "Frame.008"
			frame_008_1.label_size = 20
			frame_008_1.shrink = True
			
			#node Frame.005
			frame_005 = _mn_utils_style_cartoon.nodes.new("NodeFrame")
			frame_005.label = "Creating Alpha-helix Geometry"
			frame_005.name = "Frame.005"
			frame_005.label_size = 20
			frame_005.shrink = True
			
			#node Frame.007
			frame_007_1 = _mn_utils_style_cartoon.nodes.new("NodeFrame")
			frame_007_1.label = "DEBUG Arrows for Debugging"
			frame_007_1.name = "Frame.007"
			frame_007_1.label_size = 20
			frame_007_1.shrink = True
			
			#node Frame.003
			frame_003 = _mn_utils_style_cartoon.nodes.new("NodeFrame")
			frame_003.label = "Creating Loop Geometry"
			frame_003.name = "Frame.003"
			frame_003.label_size = 20
			frame_003.shrink = True
			
			#node Frame.004
			frame_004 = _mn_utils_style_cartoon.nodes.new("NodeFrame")
			frame_004.label = "Creating Beta-sheet Geometry"
			frame_004.name = "Frame.004"
			frame_004.label_size = 20
			frame_004.shrink = True
			
			#node Set Spline Resolution.002
			set_spline_resolution_002 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSetSplineResolution")
			set_spline_resolution_002.name = "Set Spline Resolution.002"
			#Selection
			set_spline_resolution_002.inputs[1].default_value = True
			
			#node Reroute.006
			reroute_006 = _mn_utils_style_cartoon.nodes.new("NodeReroute")
			reroute_006.name = "Reroute.006"
			#node Boolean Math.016
			boolean_math_016 = _mn_utils_style_cartoon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_016.name = "Boolean Math.016"
			boolean_math_016.operation = 'AND'
			
			#node Separate Geometry.005
			separate_geometry_005 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_005.label = "Selection + Alpha Helices Only"
			separate_geometry_005.name = "Separate Geometry.005"
			separate_geometry_005.domain = 'POINT'
			
			#node Group Input.002
			group_input_002 = _mn_utils_style_cartoon.nodes.new("NodeGroupInput")
			group_input_002.name = "Group Input.002"
			group_input_002.outputs[0].hide = True
			group_input_002.outputs[1].hide = True
			group_input_002.outputs[2].hide = True
			group_input_002.outputs[3].hide = True
			group_input_002.outputs[4].hide = True
			group_input_002.outputs[5].hide = True
			group_input_002.outputs[8].hide = True
			group_input_002.outputs[9].hide = True
			group_input_002.outputs[10].hide = True
			group_input_002.outputs[11].hide = True
			group_input_002.outputs[12].hide = True
			group_input_002.outputs[13].hide = True
			group_input_002.outputs[14].hide = True
			group_input_002.outputs[15].hide = True
			group_input_002.outputs[16].hide = True
			group_input_002.outputs[22].hide = True
			group_input_002.outputs[23].hide = True
			group_input_002.outputs[24].hide = True
			group_input_002.outputs[25].hide = True
			group_input_002.outputs[26].hide = True
			group_input_002.outputs[27].hide = True
			group_input_002.outputs[28].hide = True
			group_input_002.outputs[29].hide = True
			group_input_002.outputs[30].hide = True
			
			#node Mesh to Curve.002
			mesh_to_curve_002 = _mn_utils_style_cartoon.nodes.new("GeometryNodeMeshToCurve")
			mesh_to_curve_002.name = "Mesh to Curve.002"
			#Selection
			mesh_to_curve_002.inputs[1].default_value = True
			
			#node Set Position.004
			set_position_004 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSetPosition")
			set_position_004.name = "Set Position.004"
			#Position
			set_position_004.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Boolean Math.017
			boolean_math_017 = _mn_utils_style_cartoon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_017.name = "Boolean Math.017"
			boolean_math_017.operation = 'NOT'
			
			#node Endpoint Selection.001
			endpoint_selection_001_2 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_001_2.name = "Endpoint Selection.001"
			#Start Size
			endpoint_selection_001_2.inputs[0].default_value = 1
			#End Size
			endpoint_selection_001_2.inputs[1].default_value = 1
			
			#node Switch.003
			switch_003 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSwitch")
			switch_003.name = "Switch.003"
			switch_003.input_type = 'INT'
			#False
			switch_003.inputs[1].default_value = 2
			
			#node Math.004
			math_004 = _mn_utils_style_cartoon.nodes.new("ShaderNodeMath")
			math_004.name = "Math.004"
			math_004.operation = 'MAXIMUM'
			math_004.use_clamp = False
			#Value_001
			math_004.inputs[1].default_value = 2.0
			
			#node Math.005
			math_005 = _mn_utils_style_cartoon.nodes.new("ShaderNodeMath")
			math_005.name = "Math.005"
			math_005.operation = 'DIVIDE'
			math_005.use_clamp = False
			#Value_001
			math_005.inputs[1].default_value = 4.0
			
			#node Spline Length.001
			spline_length_001 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSplineLength")
			spline_length_001.name = "Spline Length.001"
			
			#node Vector Rotate
			vector_rotate = _mn_utils_style_cartoon.nodes.new("ShaderNodeVectorRotate")
			vector_rotate.name = "Vector Rotate"
			vector_rotate.invert = False
			vector_rotate.rotation_type = 'EULER_XYZ'
			#Center
			vector_rotate.inputs[1].default_value = (0.0, 0.0, 0.0)
			
			#node Vector
			vector = _mn_utils_style_cartoon.nodes.new("FunctionNodeInputVector")
			vector.name = "Vector"
			vector.vector = (0.0, 1.0, 0.0)
			
			#node Vector Math.001
			vector_math_001_1 = _mn_utils_style_cartoon.nodes.new("ShaderNodeVectorMath")
			vector_math_001_1.name = "Vector Math.001"
			vector_math_001_1.operation = 'SCALE'
			
			#node Reroute.007
			reroute_007_1 = _mn_utils_style_cartoon.nodes.new("NodeReroute")
			reroute_007_1.name = "Reroute.007"
			#node Group.008
			group_008_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_008_1.name = "Group.008"
			group_008_1.node_tree = _guide_rotation
			#Input_1
			group_008_1.inputs[0].default_value = 0.0
			
			#node Resample Curve.001
			resample_curve_001 = _mn_utils_style_cartoon.nodes.new("GeometryNodeResampleCurve")
			resample_curve_001.name = "Resample Curve.001"
			resample_curve_001.mode = 'COUNT'
			#Selection
			resample_curve_001.inputs[1].default_value = True
			
			#node Set Handle Type.002
			set_handle_type_002 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveSetHandles")
			set_handle_type_002.name = "Set Handle Type.002"
			set_handle_type_002.handle_type = 'AUTO'
			set_handle_type_002.mode = {'RIGHT', 'LEFT'}
			#Selection
			set_handle_type_002.inputs[1].default_value = True
			
			#node Set Spline Type
			set_spline_type = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveSplineType")
			set_spline_type.name = "Set Spline Type"
			set_spline_type.spline_type = 'BEZIER'
			#Selection
			set_spline_type.inputs[1].default_value = True
			
			#node Group.018
			group_018_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_018_1.name = "Group.018"
			group_018_1.node_tree = _mn_select_sec_struct
			#Socket_1
			group_018_1.inputs[0].default_value = True
			
			#node Boolean Math.003
			boolean_math_003_3 = _mn_utils_style_cartoon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003_3.name = "Boolean Math.003"
			boolean_math_003_3.operation = 'AND'
			
			#node Boolean Math.001
			boolean_math_001_7 = _mn_utils_style_cartoon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_7.name = "Boolean Math.001"
			boolean_math_001_7.operation = 'NOT'
			
			#node Group Input.010
			group_input_010 = _mn_utils_style_cartoon.nodes.new("NodeGroupInput")
			group_input_010.name = "Group Input.010"
			group_input_010.outputs[0].hide = True
			group_input_010.outputs[1].hide = True
			group_input_010.outputs[2].hide = True
			group_input_010.outputs[3].hide = True
			group_input_010.outputs[4].hide = True
			group_input_010.outputs[5].hide = True
			group_input_010.outputs[8].hide = True
			group_input_010.outputs[9].hide = True
			group_input_010.outputs[10].hide = True
			group_input_010.outputs[11].hide = True
			group_input_010.outputs[12].hide = True
			group_input_010.outputs[13].hide = True
			group_input_010.outputs[14].hide = True
			group_input_010.outputs[15].hide = True
			group_input_010.outputs[16].hide = True
			group_input_010.outputs[18].hide = True
			group_input_010.outputs[19].hide = True
			group_input_010.outputs[20].hide = True
			group_input_010.outputs[21].hide = True
			group_input_010.outputs[22].hide = True
			group_input_010.outputs[23].hide = True
			group_input_010.outputs[24].hide = True
			group_input_010.outputs[25].hide = True
			group_input_010.outputs[26].hide = True
			group_input_010.outputs[27].hide = True
			group_input_010.outputs[28].hide = True
			group_input_010.outputs[29].hide = True
			group_input_010.outputs[30].hide = True
			
			#node Combine XYZ.002
			combine_xyz_002_1 = _mn_utils_style_cartoon.nodes.new("ShaderNodeCombineXYZ")
			combine_xyz_002_1.name = "Combine XYZ.002"
			#X
			combine_xyz_002_1.inputs[0].default_value = 1.0
			
			#node Reroute.011
			reroute_011 = _mn_utils_style_cartoon.nodes.new("NodeReroute")
			reroute_011.name = "Reroute.011"
			#node Reroute.012
			reroute_012 = _mn_utils_style_cartoon.nodes.new("NodeReroute")
			reroute_012.name = "Reroute.012"
			#node Math.001
			math_001_6 = _mn_utils_style_cartoon.nodes.new("ShaderNodeMath")
			math_001_6.name = "Math.001"
			math_001_6.hide = True
			math_001_6.operation = 'ADD'
			math_001_6.use_clamp = False
			#Value_001
			math_001_6.inputs[1].default_value = 0.5
			
			#node Join Geometry.001
			join_geometry_001_2 = _mn_utils_style_cartoon.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_001_2.name = "Join Geometry.001"
			join_geometry_001_2.hide = True
			
			#node Separate Geometry.003
			separate_geometry_003_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_003_1.name = "Separate Geometry.003"
			separate_geometry_003_1.domain = 'POINT'
			
			#node Mesh to Curve
			mesh_to_curve_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeMeshToCurve")
			mesh_to_curve_1.name = "Mesh to Curve"
			#Selection
			mesh_to_curve_1.inputs[1].default_value = True
			
			#node Set Spline Type.002
			set_spline_type_002 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveSplineType")
			set_spline_type_002.name = "Set Spline Type.002"
			set_spline_type_002.spline_type = 'BEZIER'
			#Selection
			set_spline_type_002.inputs[1].default_value = True
			
			#node Set Handle Type
			set_handle_type = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveSetHandles")
			set_handle_type.name = "Set Handle Type"
			set_handle_type.handle_type = 'AUTO'
			set_handle_type.mode = {'RIGHT', 'LEFT'}
			#Selection
			set_handle_type.inputs[1].default_value = True
			
			#node Set Handle Positions.001
			set_handle_positions_001_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSetCurveHandlePositions")
			set_handle_positions_001_1.name = "Set Handle Positions.001"
			set_handle_positions_001_1.mode = 'RIGHT'
			#Position
			set_handle_positions_001_1.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Set Handle Positions.002
			set_handle_positions_002 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSetCurveHandlePositions")
			set_handle_positions_002.name = "Set Handle Positions.002"
			set_handle_positions_002.mode = 'LEFT'
			#Position
			set_handle_positions_002.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Reroute.002
			reroute_002_6 = _mn_utils_style_cartoon.nodes.new("NodeReroute")
			reroute_002_6.name = "Reroute.002"
			#node Reroute.008
			reroute_008 = _mn_utils_style_cartoon.nodes.new("NodeReroute")
			reroute_008.name = "Reroute.008"
			#node Endpoint Selection.002
			endpoint_selection_002_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_002_1.name = "Endpoint Selection.002"
			#Start Size
			endpoint_selection_002_1.inputs[0].default_value = 1
			#End Size
			endpoint_selection_002_1.inputs[1].default_value = 0
			
			#node Endpoint Selection.003
			endpoint_selection_003_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_003_1.name = "Endpoint Selection.003"
			#Start Size
			endpoint_selection_003_1.inputs[0].default_value = 0
			#End Size
			endpoint_selection_003_1.inputs[1].default_value = 1
			
			#node Store Named Attribute.002
			store_named_attribute_002_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_002_1.name = "Store Named Attribute.002"
			store_named_attribute_002_1.data_type = 'BOOLEAN'
			store_named_attribute_002_1.domain = 'EDGE'
			#Selection
			store_named_attribute_002_1.inputs[1].default_value = True
			#Name
			store_named_attribute_002_1.inputs[2].default_value = "sharp_edge"
			
			#node Group Input.004
			group_input_004 = _mn_utils_style_cartoon.nodes.new("NodeGroupInput")
			group_input_004.name = "Group Input.004"
			group_input_004.outputs[0].hide = True
			group_input_004.outputs[1].hide = True
			group_input_004.outputs[2].hide = True
			group_input_004.outputs[3].hide = True
			group_input_004.outputs[4].hide = True
			group_input_004.outputs[5].hide = True
			group_input_004.outputs[8].hide = True
			group_input_004.outputs[9].hide = True
			group_input_004.outputs[12].hide = True
			group_input_004.outputs[13].hide = True
			group_input_004.outputs[14].hide = True
			group_input_004.outputs[15].hide = True
			group_input_004.outputs[16].hide = True
			group_input_004.outputs[17].hide = True
			group_input_004.outputs[18].hide = True
			group_input_004.outputs[19].hide = True
			group_input_004.outputs[20].hide = True
			group_input_004.outputs[21].hide = True
			group_input_004.outputs[26].hide = True
			group_input_004.outputs[27].hide = True
			group_input_004.outputs[28].hide = True
			group_input_004.outputs[29].hide = True
			group_input_004.outputs[30].hide = True
			
			#node Group Input.007
			group_input_007 = _mn_utils_style_cartoon.nodes.new("NodeGroupInput")
			group_input_007.name = "Group Input.007"
			group_input_007.outputs[0].hide = True
			group_input_007.outputs[1].hide = True
			group_input_007.outputs[3].hide = True
			group_input_007.outputs[4].hide = True
			group_input_007.outputs[5].hide = True
			group_input_007.outputs[8].hide = True
			group_input_007.outputs[9].hide = True
			group_input_007.outputs[10].hide = True
			group_input_007.outputs[11].hide = True
			group_input_007.outputs[12].hide = True
			group_input_007.outputs[13].hide = True
			group_input_007.outputs[14].hide = True
			group_input_007.outputs[15].hide = True
			group_input_007.outputs[16].hide = True
			group_input_007.outputs[17].hide = True
			group_input_007.outputs[18].hide = True
			group_input_007.outputs[19].hide = True
			group_input_007.outputs[20].hide = True
			group_input_007.outputs[21].hide = True
			group_input_007.outputs[22].hide = True
			group_input_007.outputs[23].hide = True
			group_input_007.outputs[24].hide = True
			group_input_007.outputs[25].hide = True
			group_input_007.outputs[26].hide = True
			group_input_007.outputs[27].hide = True
			group_input_007.outputs[28].hide = True
			group_input_007.outputs[29].hide = True
			group_input_007.outputs[30].hide = True
			
			#node Boolean Math.004
			boolean_math_004_4 = _mn_utils_style_cartoon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_004_4.name = "Boolean Math.004"
			boolean_math_004_4.operation = 'NOT'
			boolean_math_004_4.inputs[1].hide = True
			
			#node Edge Angle.001
			edge_angle_001 = _mn_utils_style_cartoon.nodes.new("GeometryNodeInputMeshEdgeAngle")
			edge_angle_001.name = "Edge Angle.001"
			
			#node Compare.006
			compare_006_1 = _mn_utils_style_cartoon.nodes.new("FunctionNodeCompare")
			compare_006_1.name = "Compare.006"
			compare_006_1.data_type = 'FLOAT'
			compare_006_1.mode = 'ELEMENT'
			compare_006_1.operation = 'GREATER_THAN'
			#B
			compare_006_1.inputs[1].default_value = 1.0471975803375244
			
			#node Boolean Math.002
			boolean_math_002_4 = _mn_utils_style_cartoon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_4.name = "Boolean Math.002"
			boolean_math_002_4.operation = 'OR'
			
			#node Realize Instances
			realize_instances_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeRealizeInstances")
			realize_instances_1.name = "Realize Instances"
			realize_instances_1.hide = True
			#Selection
			realize_instances_1.inputs[1].default_value = True
			#Realize All
			realize_instances_1.inputs[2].default_value = True
			#Depth
			realize_instances_1.inputs[3].default_value = 0
			
			#node Position
			position_3 = _mn_utils_style_cartoon.nodes.new("GeometryNodeInputPosition")
			position_3.name = "Position"
			
			#node Group.033
			group_033 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_033.name = "Group.033"
			group_033.node_tree = _guide_rotation
			#Input_1
			group_033.inputs[0].default_value = 0.0
			
			#node Group.004
			group_004_2 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_004_2.name = "Group.004"
			group_004_2.node_tree = _debug_arrows
			#Input_5
			group_004_2.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Input_2
			group_004_2.inputs[4].default_value = (0.30000001192092896, 0.30000001192092896, 0.30000001192092896)
			
			#node Switch
			switch_9 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSwitch")
			switch_9.label = "DEBUG"
			switch_9.name = "Switch"
			switch_9.input_type = 'GEOMETRY'
			#Switch
			switch_9.inputs[0].default_value = False
			
			#node Reroute
			reroute_10 = _mn_utils_style_cartoon.nodes.new("NodeReroute")
			reroute_10.name = "Reroute"
			#node Reroute.004
			reroute_004 = _mn_utils_style_cartoon.nodes.new("NodeReroute")
			reroute_004.name = "Reroute.004"
			#node Endpoint Selection
			endpoint_selection_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_1.name = "Endpoint Selection"
			#Start Size
			endpoint_selection_1.inputs[0].default_value = 1
			#End Size
			endpoint_selection_1.inputs[1].default_value = 1
			
			#node Group.005
			group_005_2 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_005_2.name = "Group.005"
			group_005_2.node_tree = _selective_scale
			#Input_3
			group_005_2.inputs[2].default_value = 0.800000011920929
			
			#node Set Spline Resolution.001
			set_spline_resolution_001 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSetSplineResolution")
			set_spline_resolution_001.name = "Set Spline Resolution.001"
			#Selection
			set_spline_resolution_001.inputs[1].default_value = True
			
			#node Group.032
			group_032 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_032.name = "Group.032"
			group_032.node_tree = _curve_ends_adjust_angle
			#Input_2
			group_032.inputs[1].default_value = 3.0
			#Input_3
			group_032.inputs[2].default_value = 0.4200000762939453
			
			#node Group Input.006
			group_input_006 = _mn_utils_style_cartoon.nodes.new("NodeGroupInput")
			group_input_006.name = "Group Input.006"
			group_input_006.outputs[0].hide = True
			group_input_006.outputs[1].hide = True
			group_input_006.outputs[2].hide = True
			group_input_006.outputs[3].hide = True
			group_input_006.outputs[4].hide = True
			group_input_006.outputs[5].hide = True
			group_input_006.outputs[8].hide = True
			group_input_006.outputs[9].hide = True
			group_input_006.outputs[10].hide = True
			group_input_006.outputs[11].hide = True
			group_input_006.outputs[12].hide = True
			group_input_006.outputs[13].hide = True
			group_input_006.outputs[14].hide = True
			group_input_006.outputs[15].hide = True
			group_input_006.outputs[16].hide = True
			group_input_006.outputs[17].hide = True
			group_input_006.outputs[18].hide = True
			group_input_006.outputs[19].hide = True
			group_input_006.outputs[20].hide = True
			group_input_006.outputs[21].hide = True
			group_input_006.outputs[22].hide = True
			group_input_006.outputs[23].hide = True
			group_input_006.outputs[24].hide = True
			group_input_006.outputs[25].hide = True
			group_input_006.outputs[26].hide = True
			group_input_006.outputs[30].hide = True
			
			#node Group.029
			group_029_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_029_1.name = "Group.029"
			group_029_1.mute = True
			group_029_1.node_tree = _curve_ends_adjust_position
			#Input_2
			group_029_1.inputs[1].default_value = 0.30000001192092896
			
			#node Set Handle Type.003
			set_handle_type_003 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveSetHandles")
			set_handle_type_003.name = "Set Handle Type.003"
			set_handle_type_003.handle_type = 'AUTO'
			set_handle_type_003.mode = {'RIGHT', 'LEFT'}
			#Selection
			set_handle_type_003.inputs[1].default_value = True
			
			#node Set Spline Type.001
			set_spline_type_001_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveSplineType")
			set_spline_type_001_1.name = "Set Spline Type.001"
			set_spline_type_001_1.spline_type = 'BEZIER'
			#Selection
			set_spline_type_001_1.inputs[1].default_value = True
			
			#node Group.030
			group_030_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_030_1.name = "Group.030"
			group_030_1.node_tree = _curve_to_mesh
			#Input_3
			group_030_1.inputs[3].default_value = True
			
			#node Group.028
			group_028_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_028_1.name = "Group.028"
			group_028_1.node_tree = _curve_end_fix_color
			
			#node Set Spline Type.003
			set_spline_type_003 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveSplineType")
			set_spline_type_003.name = "Set Spline Type.003"
			set_spline_type_003.spline_type = 'BEZIER'
			#Selection
			set_spline_type_003.inputs[1].default_value = True
			
			#node Group.009
			group_009_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_009_1.name = "Group.009"
			group_009_1.node_tree = _guide_rotation
			#Input_1
			group_009_1.inputs[0].default_value = 0.0
			
			#node Join Geometry.002
			join_geometry_002 = _mn_utils_style_cartoon.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_002.name = "Join Geometry.002"
			
			#node Resample Curve
			resample_curve_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeResampleCurve")
			resample_curve_1.name = "Resample Curve"
			resample_curve_1.mode = 'EVALUATED'
			#Selection
			resample_curve_1.inputs[1].default_value = True
			
			#node Set Spline Resolution
			set_spline_resolution_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSetSplineResolution")
			set_spline_resolution_1.name = "Set Spline Resolution"
			#Selection
			set_spline_resolution_1.inputs[1].default_value = True
			
			#node Endpoint Selection.004
			endpoint_selection_004_2 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_004_2.name = "Endpoint Selection.004"
			#Start Size
			endpoint_selection_004_2.inputs[0].default_value = 1
			#End Size
			endpoint_selection_004_2.inputs[1].default_value = 0
			
			#node Group.011
			group_011_2 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_011_2.name = "Group.011"
			group_011_2.node_tree = _mn_cartoon_smooth_handles
			#Input_1
			group_011_2.inputs[0].default_value = -1.0
			
			#node Endpoint Selection.006
			endpoint_selection_006_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_006_1.name = "Endpoint Selection.006"
			#Start Size
			endpoint_selection_006_1.inputs[0].default_value = 1
			#End Size
			endpoint_selection_006_1.inputs[1].default_value = 0
			
			#node Group.014
			group_014_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_014_1.name = "Group.014"
			group_014_1.node_tree = _mn_cartoon_smooth_handles
			#Input_1
			group_014_1.inputs[0].default_value = -1.7000000476837158
			
			#node Endpoint Selection.005
			endpoint_selection_005 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_005.name = "Endpoint Selection.005"
			#Start Size
			endpoint_selection_005.inputs[0].default_value = 0
			#End Size
			endpoint_selection_005.inputs[1].default_value = 1
			
			#node Endpoint Selection.007
			endpoint_selection_007 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_007.name = "Endpoint Selection.007"
			#Start Size
			endpoint_selection_007.inputs[0].default_value = 0
			#End Size
			endpoint_selection_007.inputs[1].default_value = 1
			
			#node Group.007
			group_007 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_007.name = "Group.007"
			group_007.node_tree = _mn_cartoon_smooth_handles
			#Input_1
			group_007.inputs[0].default_value = 1.0
			
			#node Group.020
			group_020 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_020.name = "Group.020"
			group_020.node_tree = _mn_cartoon_smooth_handles
			#Input_1
			group_020.inputs[0].default_value = 0.699999988079071
			
			#node Endpoint Selection.008
			endpoint_selection_008_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_008_1.name = "Endpoint Selection.008"
			#Start Size
			endpoint_selection_008_1.inputs[0].default_value = 1
			#End Size
			endpoint_selection_008_1.inputs[1].default_value = 0
			
			#node Group.022
			group_022_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_022_1.name = "Group.022"
			group_022_1.node_tree = _mn_cartoon_smooth_handles
			#Input_1
			group_022_1.inputs[0].default_value = -1.0
			
			#node Endpoint Selection.009
			endpoint_selection_009_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_009_1.name = "Endpoint Selection.009"
			#Start Size
			endpoint_selection_009_1.inputs[0].default_value = 1
			#End Size
			endpoint_selection_009_1.inputs[1].default_value = 0
			
			#node Endpoint Selection.010
			endpoint_selection_010_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_010_1.name = "Endpoint Selection.010"
			#Start Size
			endpoint_selection_010_1.inputs[0].default_value = 0
			#End Size
			endpoint_selection_010_1.inputs[1].default_value = 1
			
			#node Endpoint Selection.011
			endpoint_selection_011 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_011.name = "Endpoint Selection.011"
			#Start Size
			endpoint_selection_011.inputs[0].default_value = 0
			#End Size
			endpoint_selection_011.inputs[1].default_value = 1
			
			#node Group.024
			group_024_2 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_024_2.name = "Group.024"
			group_024_2.node_tree = _mn_cartoon_smooth_handles
			#Input_1
			group_024_2.inputs[0].default_value = 1.0
			
			#node Group.025
			group_025_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_025_1.name = "Group.025"
			group_025_1.node_tree = _mn_cartoon_smooth_handles
			#Input_1
			group_025_1.inputs[0].default_value = 0.699999988079071
			
			#node Set Handle Type.001
			set_handle_type_001 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveSetHandles")
			set_handle_type_001.name = "Set Handle Type.001"
			set_handle_type_001.handle_type = 'AUTO'
			set_handle_type_001.mode = {'RIGHT', 'LEFT'}
			#Selection
			set_handle_type_001.inputs[1].default_value = True
			
			#node Vector Math
			vector_math_5 = _mn_utils_style_cartoon.nodes.new("ShaderNodeVectorMath")
			vector_math_5.name = "Vector Math"
			vector_math_5.operation = 'MULTIPLY'
			
			#node Reroute.001
			reroute_001_9 = _mn_utils_style_cartoon.nodes.new("NodeReroute")
			reroute_001_9.name = "Reroute.001"
			#node Reroute.013
			reroute_013 = _mn_utils_style_cartoon.nodes.new("NodeReroute")
			reroute_013.name = "Reroute.013"
			#node Boolean Math.007
			boolean_math_007_1 = _mn_utils_style_cartoon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_007_1.name = "Boolean Math.007"
			boolean_math_007_1.operation = 'NOT'
			
			#node Group.012
			group_012_2 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_012_2.name = "Group.012"
			group_012_2.node_tree = _field_offset_bool
			#Input_1
			group_012_2.inputs[1].default_value = -1
			
			#node Boolean Math.006
			boolean_math_006_1 = _mn_utils_style_cartoon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_006_1.name = "Boolean Math.006"
			boolean_math_006_1.operation = 'AND'
			
			#node Reroute.005
			reroute_005_1 = _mn_utils_style_cartoon.nodes.new("NodeReroute")
			reroute_005_1.name = "Reroute.005"
			#node Group.013
			group_013_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_013_1.name = "Group.013"
			group_013_1.node_tree = _field_offset_bool
			#Input_1
			group_013_1.inputs[1].default_value = 1
			
			#node Combine XYZ.001
			combine_xyz_001_1 = _mn_utils_style_cartoon.nodes.new("ShaderNodeCombineXYZ")
			combine_xyz_001_1.name = "Combine XYZ.001"
			#X
			combine_xyz_001_1.inputs[0].default_value = 1.0
			
			#node Combine XYZ
			combine_xyz_1 = _mn_utils_style_cartoon.nodes.new("ShaderNodeCombineXYZ")
			combine_xyz_1.name = "Combine XYZ"
			#X
			combine_xyz_1.inputs[0].default_value = 1.0
			
			#node Math.002
			math_002_1 = _mn_utils_style_cartoon.nodes.new("ShaderNodeMath")
			math_002_1.name = "Math.002"
			math_002_1.operation = 'MULTIPLY'
			math_002_1.use_clamp = False
			#Value_001
			math_002_1.inputs[1].default_value = 1.100000023841858
			
			#node Math
			math_6 = _mn_utils_style_cartoon.nodes.new("ShaderNodeMath")
			math_6.name = "Math"
			math_6.operation = 'MULTIPLY'
			math_6.use_clamp = False
			#Value_001
			math_6.inputs[1].default_value = 0.5
			
			#node Capture Attribute
			capture_attribute_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute_1.name = "Capture Attribute"
			capture_attribute_1.active_index = 0
			capture_attribute_1.capture_items.clear()
			capture_attribute_1.capture_items.new('FLOAT', "Value")
			capture_attribute_1.capture_items["Value"].data_type = 'FLOAT_VECTOR'
			capture_attribute_1.domain = 'POINT'
			
			#node Group.021
			group_021_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_021_1.name = "Group.021"
			group_021_1.node_tree = _cartoon_arrows_scale
			#Input_2
			group_021_1.inputs[0].default_value = 0.75
			#Input_3
			group_021_1.inputs[1].default_value = 3.0
			#Input_4
			group_021_1.inputs[2].default_value = 3.0
			
			#node Switch.004
			switch_004 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSwitch")
			switch_004.name = "Switch.004"
			switch_004.input_type = 'FLOAT'
			#False
			switch_004.inputs[1].default_value = 1.0
			
			#node Switch.002
			switch_002_2 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSwitch")
			switch_002_2.name = "Switch.002"
			switch_002_2.input_type = 'VECTOR'
			#Switch
			switch_002_2.inputs[0].default_value = False
			#True
			switch_002_2.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Boolean Math.009
			boolean_math_009_1 = _mn_utils_style_cartoon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_009_1.name = "Boolean Math.009"
			boolean_math_009_1.operation = 'AND'
			
			#node Boolean Math.008
			boolean_math_008_1 = _mn_utils_style_cartoon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_008_1.name = "Boolean Math.008"
			boolean_math_008_1.operation = 'NOT'
			
			#node Math.009
			math_009 = _mn_utils_style_cartoon.nodes.new("ShaderNodeMath")
			math_009.name = "Math.009"
			math_009.operation = 'MULTIPLY'
			math_009.use_clamp = False
			
			#node Switch.005
			switch_005_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSwitch")
			switch_005_1.name = "Switch.005"
			switch_005_1.input_type = 'FLOAT'
			#False
			switch_005_1.inputs[1].default_value = 1.0
			
			#node Math.010
			math_010 = _mn_utils_style_cartoon.nodes.new("ShaderNodeMath")
			math_010.name = "Math.010"
			math_010.operation = 'MULTIPLY'
			math_010.use_clamp = False
			
			#node Separate Geometry
			separate_geometry_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_1.name = "Separate Geometry"
			separate_geometry_1.domain = 'CURVE'
			
			#node Boolean Math
			boolean_math_9 = _mn_utils_style_cartoon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_9.name = "Boolean Math"
			boolean_math_9.hide = True
			boolean_math_9.operation = 'NOT'
			
			#node Boolean Math.005
			boolean_math_005_2 = _mn_utils_style_cartoon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_005_2.name = "Boolean Math.005"
			boolean_math_005_2.hide = True
			boolean_math_005_2.operation = 'AND'
			
			#node Group Input.008
			group_input_008 = _mn_utils_style_cartoon.nodes.new("NodeGroupInput")
			group_input_008.name = "Group Input.008"
			group_input_008.outputs[0].hide = True
			group_input_008.outputs[1].hide = True
			group_input_008.outputs[2].hide = True
			group_input_008.outputs[3].hide = True
			group_input_008.outputs[4].hide = True
			group_input_008.outputs[8].hide = True
			group_input_008.outputs[9].hide = True
			group_input_008.outputs[10].hide = True
			group_input_008.outputs[11].hide = True
			group_input_008.outputs[12].hide = True
			group_input_008.outputs[13].hide = True
			group_input_008.outputs[14].hide = True
			group_input_008.outputs[15].hide = True
			group_input_008.outputs[16].hide = True
			group_input_008.outputs[17].hide = True
			group_input_008.outputs[18].hide = True
			group_input_008.outputs[19].hide = True
			group_input_008.outputs[20].hide = True
			group_input_008.outputs[21].hide = True
			group_input_008.outputs[22].hide = True
			group_input_008.outputs[23].hide = True
			group_input_008.outputs[24].hide = True
			group_input_008.outputs[25].hide = True
			group_input_008.outputs[26].hide = True
			group_input_008.outputs[27].hide = True
			group_input_008.outputs[28].hide = True
			group_input_008.outputs[29].hide = True
			group_input_008.outputs[30].hide = True
			
			#node Join Geometry
			join_geometry = _mn_utils_style_cartoon.nodes.new("GeometryNodeJoinGeometry")
			join_geometry.name = "Join Geometry"
			join_geometry.hide = True
			
			#node Group.003
			group_003_2 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_003_2.name = "Group.003"
			group_003_2.node_tree = _cartoon_arrow_instance
			
			#node Group.023
			group_023_2 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_023_2.name = "Group.023"
			group_023_2.node_tree = _mn_cartoon_smooth_handles
			#Input_1
			group_023_2.inputs[0].default_value = -1.5
			
			#node Group.006
			group_006_2 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_006_2.name = "Group.006"
			group_006_2.node_tree = _cartoon_arrow_primitive
			#Input_0
			group_006_2.inputs[0].default_value = 0.7599999904632568
			
			#node Group.017
			group_017 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_017.name = "Group.017"
			group_017.node_tree = _curve_to_mesh
			#Input_3
			group_017.inputs[3].default_value = True
			
			#node Group Input.012
			group_input_012 = _mn_utils_style_cartoon.nodes.new("NodeGroupInput")
			group_input_012.name = "Group Input.012"
			group_input_012.outputs[0].hide = True
			group_input_012.outputs[1].hide = True
			group_input_012.outputs[2].hide = True
			group_input_012.outputs[3].hide = True
			group_input_012.outputs[4].hide = True
			group_input_012.outputs[5].hide = True
			group_input_012.outputs[6].hide = True
			group_input_012.outputs[7].hide = True
			group_input_012.outputs[8].hide = True
			group_input_012.outputs[9].hide = True
			group_input_012.outputs[10].hide = True
			group_input_012.outputs[11].hide = True
			group_input_012.outputs[12].hide = True
			group_input_012.outputs[13].hide = True
			group_input_012.outputs[14].hide = True
			group_input_012.outputs[15].hide = True
			group_input_012.outputs[17].hide = True
			group_input_012.outputs[18].hide = True
			group_input_012.outputs[19].hide = True
			group_input_012.outputs[20].hide = True
			group_input_012.outputs[21].hide = True
			group_input_012.outputs[22].hide = True
			group_input_012.outputs[23].hide = True
			group_input_012.outputs[24].hide = True
			group_input_012.outputs[25].hide = True
			group_input_012.outputs[26].hide = True
			group_input_012.outputs[27].hide = True
			group_input_012.outputs[28].hide = True
			group_input_012.outputs[29].hide = True
			group_input_012.outputs[30].hide = True
			
			#node Set Position
			set_position_3 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSetPosition")
			set_position_3.name = "Set Position"
			#Offset
			set_position_3.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Group.010
			group_010 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_010.name = "Group.010"
			group_010.node_tree = _field_offset_vec
			#Input_1
			group_010.inputs[1].default_value = 1
			
			#node Position.001
			position_001_4 = _mn_utils_style_cartoon.nodes.new("GeometryNodeInputPosition")
			position_001_4.name = "Position.001"
			
			#node Mix
			mix = _mn_utils_style_cartoon.nodes.new("ShaderNodeMix")
			mix.name = "Mix"
			mix.blend_type = 'MIX'
			mix.clamp_factor = True
			mix.clamp_result = False
			mix.data_type = 'VECTOR'
			mix.factor_mode = 'UNIFORM'
			#Factor_Float
			mix.inputs[0].default_value = 0.8704171180725098
			
			#node Reroute.009
			reroute_009_1 = _mn_utils_style_cartoon.nodes.new("NodeReroute")
			reroute_009_1.name = "Reroute.009"
			#node Reroute.003
			reroute_003_3 = _mn_utils_style_cartoon.nodes.new("NodeReroute")
			reroute_003_3.name = "Reroute.003"
			#node Group Input.011
			group_input_011 = _mn_utils_style_cartoon.nodes.new("NodeGroupInput")
			group_input_011.name = "Group Input.011"
			group_input_011.outputs[0].hide = True
			group_input_011.outputs[1].hide = True
			group_input_011.outputs[2].hide = True
			group_input_011.outputs[3].hide = True
			group_input_011.outputs[4].hide = True
			group_input_011.outputs[5].hide = True
			group_input_011.outputs[8].hide = True
			group_input_011.outputs[9].hide = True
			group_input_011.outputs[13].hide = True
			group_input_011.outputs[14].hide = True
			group_input_011.outputs[15].hide = True
			group_input_011.outputs[17].hide = True
			group_input_011.outputs[18].hide = True
			group_input_011.outputs[19].hide = True
			group_input_011.outputs[20].hide = True
			group_input_011.outputs[21].hide = True
			group_input_011.outputs[22].hide = True
			group_input_011.outputs[23].hide = True
			group_input_011.outputs[24].hide = True
			group_input_011.outputs[25].hide = True
			group_input_011.outputs[26].hide = True
			group_input_011.outputs[27].hide = True
			group_input_011.outputs[28].hide = True
			group_input_011.outputs[29].hide = True
			group_input_011.outputs[30].hide = True
			
			#node Group.026
			group_026_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_026_1.name = "Group.026"
			group_026_1.node_tree = _mn_select_sec_struct
			#Socket_1
			group_026_1.inputs[0].default_value = True
			
			#node Group.019
			group_019_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_019_1.name = "Group.019"
			group_019_1.node_tree = _curve_custom_profile
			#Input_13
			group_019_1.inputs[2].default_value = 1.0
			#Input_14
			group_019_1.inputs[3].default_value = 0.7853981852531433
			#Input_3
			group_019_1.inputs[7].default_value = 0.0
			#Input_5
			group_019_1.inputs[8].default_value = 1.0
			#Input_16
			group_019_1.inputs[10].default_value = False
			
			#node Group.015
			group_015 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_015.name = "Group.015"
			group_015.node_tree = mn_units
			#Input_1
			group_015.inputs[0].default_value = 2.200000047683716
			
			#node Store Named Attribute
			store_named_attribute_3 = _mn_utils_style_cartoon.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_3.name = "Store Named Attribute"
			store_named_attribute_3.data_type = 'INT'
			store_named_attribute_3.domain = 'POINT'
			#Selection
			store_named_attribute_3.inputs[1].default_value = True
			#Name
			store_named_attribute_3.inputs[2].default_value = "sec_struct"
			#Value
			store_named_attribute_3.inputs[3].default_value = 3
			
			#node Group.016
			group_016 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_016.name = "Group.016"
			group_016.node_tree = _curve_custom_profile
			#Input_13
			group_016.inputs[2].default_value = 1.0
			#Input_14
			group_016.inputs[3].default_value = 0.7853981852531433
			#Input_3
			group_016.inputs[7].default_value = 0.0
			#Input_5
			group_016.inputs[8].default_value = 0.625
			#Input_16
			group_016.inputs[10].default_value = True
			
			#node Named Attribute
			named_attribute_6 = _mn_utils_style_cartoon.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_6.name = "Named Attribute"
			named_attribute_6.data_type = 'INT'
			#Name
			named_attribute_6.inputs[0].default_value = "idx"
			
			#node Named Attribute.001
			named_attribute_001_5 = _mn_utils_style_cartoon.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001_5.name = "Named Attribute.001"
			named_attribute_001_5.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute_001_5.inputs[0].default_value = "Color"
			
			#node Store Named Attribute.001
			store_named_attribute_001_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_001_1.name = "Store Named Attribute.001"
			store_named_attribute_001_1.data_type = 'FLOAT_COLOR'
			store_named_attribute_001_1.domain = 'FACE'
			#Selection
			store_named_attribute_001_1.inputs[1].default_value = True
			#Name
			store_named_attribute_001_1.inputs[2].default_value = "Color"
			
			#node Group Output
			group_output_40 = _mn_utils_style_cartoon.nodes.new("NodeGroupOutput")
			group_output_40.name = "Group Output"
			group_output_40.is_active_output = True
			
			#node Set Material
			set_material = _mn_utils_style_cartoon.nodes.new("GeometryNodeSetMaterial")
			set_material.name = "Set Material"
			#Selection
			set_material.inputs[1].default_value = True
			
			#node Group Input.003
			group_input_003 = _mn_utils_style_cartoon.nodes.new("NodeGroupInput")
			group_input_003.name = "Group Input.003"
			group_input_003.outputs[0].hide = True
			group_input_003.outputs[1].hide = True
			group_input_003.outputs[2].hide = True
			group_input_003.outputs[3].hide = True
			group_input_003.outputs[5].hide = True
			group_input_003.outputs[8].hide = True
			group_input_003.outputs[9].hide = True
			group_input_003.outputs[10].hide = True
			group_input_003.outputs[11].hide = True
			group_input_003.outputs[12].hide = True
			group_input_003.outputs[13].hide = True
			group_input_003.outputs[14].hide = True
			group_input_003.outputs[15].hide = True
			group_input_003.outputs[16].hide = True
			group_input_003.outputs[17].hide = True
			group_input_003.outputs[18].hide = True
			group_input_003.outputs[19].hide = True
			group_input_003.outputs[20].hide = True
			group_input_003.outputs[21].hide = True
			group_input_003.outputs[22].hide = True
			group_input_003.outputs[23].hide = True
			group_input_003.outputs[24].hide = True
			group_input_003.outputs[25].hide = True
			group_input_003.outputs[26].hide = True
			group_input_003.outputs[27].hide = True
			group_input_003.outputs[28].hide = True
			group_input_003.outputs[29].hide = True
			group_input_003.outputs[30].hide = True
			
			#node Sample Index
			sample_index = _mn_utils_style_cartoon.nodes.new("GeometryNodeSampleIndex")
			sample_index.name = "Sample Index"
			sample_index.clamp = False
			sample_index.data_type = 'FLOAT_COLOR'
			sample_index.domain = 'POINT'
			
			#node Switch.001
			switch_001_2 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSwitch")
			switch_001_2.name = "Switch.001"
			switch_001_2.input_type = 'GEOMETRY'
			
			#node Group.001
			group_001_8 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_001_8.name = "Group.001"
			group_001_8.node_tree = _atoms_to_curves
			
			#node Group Input
			group_input_39 = _mn_utils_style_cartoon.nodes.new("NodeGroupInput")
			group_input_39.name = "Group Input"
			group_input_39.outputs[2].hide = True
			group_input_39.outputs[3].hide = True
			group_input_39.outputs[4].hide = True
			group_input_39.outputs[5].hide = True
			group_input_39.outputs[6].hide = True
			group_input_39.outputs[7].hide = True
			group_input_39.outputs[8].hide = True
			group_input_39.outputs[9].hide = True
			group_input_39.outputs[10].hide = True
			group_input_39.outputs[11].hide = True
			group_input_39.outputs[12].hide = True
			group_input_39.outputs[13].hide = True
			group_input_39.outputs[14].hide = True
			group_input_39.outputs[16].hide = True
			group_input_39.outputs[17].hide = True
			group_input_39.outputs[18].hide = True
			group_input_39.outputs[19].hide = True
			group_input_39.outputs[20].hide = True
			group_input_39.outputs[21].hide = True
			group_input_39.outputs[22].hide = True
			group_input_39.outputs[23].hide = True
			group_input_39.outputs[24].hide = True
			group_input_39.outputs[25].hide = True
			group_input_39.outputs[26].hide = True
			group_input_39.outputs[27].hide = True
			group_input_39.outputs[28].hide = True
			group_input_39.outputs[29].hide = True
			group_input_39.outputs[30].hide = True
			
			#node Group Input.005
			group_input_005 = _mn_utils_style_cartoon.nodes.new("NodeGroupInput")
			group_input_005.name = "Group Input.005"
			group_input_005.outputs[0].hide = True
			group_input_005.outputs[1].hide = True
			group_input_005.outputs[2].hide = True
			group_input_005.outputs[3].hide = True
			group_input_005.outputs[4].hide = True
			group_input_005.outputs[10].hide = True
			group_input_005.outputs[11].hide = True
			group_input_005.outputs[12].hide = True
			group_input_005.outputs[15].hide = True
			group_input_005.outputs[16].hide = True
			group_input_005.outputs[17].hide = True
			group_input_005.outputs[18].hide = True
			group_input_005.outputs[19].hide = True
			group_input_005.outputs[20].hide = True
			group_input_005.outputs[21].hide = True
			group_input_005.outputs[22].hide = True
			group_input_005.outputs[23].hide = True
			group_input_005.outputs[24].hide = True
			group_input_005.outputs[25].hide = True
			group_input_005.outputs[26].hide = True
			group_input_005.outputs[27].hide = True
			group_input_005.outputs[28].hide = True
			group_input_005.outputs[29].hide = True
			group_input_005.outputs[30].hide = True
			
			#node Group Input.001
			group_input_001_2 = _mn_utils_style_cartoon.nodes.new("NodeGroupInput")
			group_input_001_2.name = "Group Input.001"
			group_input_001_2.outputs[0].hide = True
			group_input_001_2.outputs[1].hide = True
			group_input_001_2.outputs[2].hide = True
			group_input_001_2.outputs[4].hide = True
			group_input_001_2.outputs[5].hide = True
			group_input_001_2.outputs[6].hide = True
			group_input_001_2.outputs[7].hide = True
			group_input_001_2.outputs[8].hide = True
			group_input_001_2.outputs[9].hide = True
			group_input_001_2.outputs[10].hide = True
			group_input_001_2.outputs[11].hide = True
			group_input_001_2.outputs[12].hide = True
			group_input_001_2.outputs[13].hide = True
			group_input_001_2.outputs[14].hide = True
			group_input_001_2.outputs[15].hide = True
			group_input_001_2.outputs[16].hide = True
			group_input_001_2.outputs[17].hide = True
			group_input_001_2.outputs[18].hide = True
			group_input_001_2.outputs[19].hide = True
			group_input_001_2.outputs[20].hide = True
			group_input_001_2.outputs[21].hide = True
			group_input_001_2.outputs[22].hide = True
			group_input_001_2.outputs[23].hide = True
			group_input_001_2.outputs[24].hide = True
			group_input_001_2.outputs[25].hide = True
			group_input_001_2.outputs[26].hide = True
			group_input_001_2.outputs[27].hide = True
			group_input_001_2.outputs[28].hide = True
			group_input_001_2.outputs[29].hide = True
			group_input_001_2.outputs[30].hide = True
			
			#node Remove Named Attribute
			remove_named_attribute = _mn_utils_style_cartoon.nodes.new("GeometryNodeRemoveAttribute")
			remove_named_attribute.name = "Remove Named Attribute"
			remove_named_attribute.pattern_mode = 'EXACT'
			#Name
			remove_named_attribute.inputs[1].default_value = "idx"
			
			#node Set Handle Positions.008
			set_handle_positions_008 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSetCurveHandlePositions")
			set_handle_positions_008.name = "Set Handle Positions.008"
			set_handle_positions_008.mode = 'LEFT'
			#Position
			set_handle_positions_008.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Set Handle Positions.007
			set_handle_positions_007 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSetCurveHandlePositions")
			set_handle_positions_007.name = "Set Handle Positions.007"
			set_handle_positions_007.mode = 'RIGHT'
			#Position
			set_handle_positions_007.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Set Handle Positions.009
			set_handle_positions_009 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSetCurveHandlePositions")
			set_handle_positions_009.name = "Set Handle Positions.009"
			set_handle_positions_009.mode = 'LEFT'
			#Position
			set_handle_positions_009.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Set Handle Positions.010
			set_handle_positions_010 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSetCurveHandlePositions")
			set_handle_positions_010.name = "Set Handle Positions.010"
			set_handle_positions_010.mode = 'RIGHT'
			#Position
			set_handle_positions_010.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Set Handle Positions.003
			set_handle_positions_003 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSetCurveHandlePositions")
			set_handle_positions_003.name = "Set Handle Positions.003"
			set_handle_positions_003.mode = 'RIGHT'
			#Position
			set_handle_positions_003.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Set Handle Positions.005
			set_handle_positions_005 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSetCurveHandlePositions")
			set_handle_positions_005.name = "Set Handle Positions.005"
			set_handle_positions_005.mode = 'LEFT'
			#Position
			set_handle_positions_005.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Set Handle Positions.004
			set_handle_positions_004 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSetCurveHandlePositions")
			set_handle_positions_004.name = "Set Handle Positions.004"
			set_handle_positions_004.mode = 'LEFT'
			#Position
			set_handle_positions_004.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Set Handle Positions.006
			set_handle_positions_006 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSetCurveHandlePositions")
			set_handle_positions_006.name = "Set Handle Positions.006"
			set_handle_positions_006.mode = 'RIGHT'
			#Position
			set_handle_positions_006.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Group.002
			group_002_4 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_002_4.name = "Group.002"
			group_002_4.node_tree = _mn_cartoon_smooth_handles
			#Input_1
			group_002_4.inputs[0].default_value = 1.0
			
			
			
			#Set parents
			group_input_002.parent = frame_006_1
			switch_003.parent = frame_009
			math_004.parent = frame_009
			math_005.parent = frame_009
			spline_length_001.parent = frame_009
			vector_rotate.parent = frame_008_1
			vector.parent = frame_008_1
			vector_math_001_1.parent = frame_008_1
			group_008_1.parent = frame_008_1
			group_018_1.parent = frame_005
			boolean_math_003_3.parent = frame_005
			boolean_math_001_7.parent = frame_005
			group_input_010.parent = frame_005
			combine_xyz_002_1.parent = frame_005
			reroute_011.parent = frame_005
			reroute_012.parent = frame_005
			math_001_6.parent = frame_005
			separate_geometry_003_1.parent = frame_005
			mesh_to_curve_1.parent = frame_005
			set_spline_type_002.parent = frame_005
			set_handle_type.parent = frame_005
			set_handle_positions_001_1.parent = frame_005
			set_handle_positions_002.parent = frame_005
			reroute_002_6.parent = frame_005
			reroute_008.parent = frame_005
			endpoint_selection_002_1.parent = frame_005
			endpoint_selection_003_1.parent = frame_005
			group_input_004.parent = frame_005
			position_3.parent = frame_007_1
			group_033.parent = frame_007_1
			group_004_2.parent = frame_007_1
			endpoint_selection_1.parent = frame_003
			group_005_2.parent = frame_003
			set_spline_resolution_001.parent = frame_003
			group_032.parent = frame_003
			group_input_006.parent = frame_003
			group_029_1.parent = frame_003
			set_handle_type_003.parent = frame_003
			set_spline_type_001_1.parent = frame_003
			group_030_1.parent = frame_003
			group_028_1.parent = frame_003
			set_spline_type_003.parent = frame_004
			group_009_1.parent = frame_004
			join_geometry_002.parent = frame_004
			resample_curve_1.parent = frame_004
			set_spline_resolution_1.parent = frame_004
			endpoint_selection_004_2.parent = frame_003
			group_011_2.parent = frame_003
			endpoint_selection_006_1.parent = frame_003
			group_014_1.parent = frame_003
			endpoint_selection_005.parent = frame_003
			endpoint_selection_007.parent = frame_003
			group_007.parent = frame_003
			group_020.parent = frame_003
			endpoint_selection_008_1.parent = frame_004
			group_022_1.parent = frame_004
			endpoint_selection_009_1.parent = frame_004
			endpoint_selection_010_1.parent = frame_004
			endpoint_selection_011.parent = frame_004
			group_024_2.parent = frame_004
			group_025_1.parent = frame_004
			set_handle_type_001.parent = frame_004
			vector_math_5.parent = frame_004
			reroute_001_9.parent = frame_004
			reroute_013.parent = frame_004
			boolean_math_007_1.parent = frame_004
			group_012_2.parent = frame_004
			boolean_math_006_1.parent = frame_004
			reroute_005_1.parent = frame_004
			group_013_1.parent = frame_004
			combine_xyz_001_1.parent = frame_004
			combine_xyz_1.parent = frame_004
			math_002_1.parent = frame_004
			math_6.parent = frame_004
			capture_attribute_1.parent = frame_004
			group_021_1.parent = frame_004
			switch_004.parent = frame_004
			switch_002_2.parent = frame_004
			boolean_math_009_1.parent = frame_004
			boolean_math_008_1.parent = frame_004
			math_009.parent = frame_004
			switch_005_1.parent = frame_004
			math_010.parent = frame_004
			separate_geometry_1.parent = frame_004
			boolean_math_9.parent = frame_004
			boolean_math_005_2.parent = frame_004
			group_input_008.parent = frame_004
			join_geometry.parent = frame_004
			group_003_2.parent = frame_004
			group_023_2.parent = frame_004
			group_006_2.parent = frame_004
			group_input_012.parent = frame_004
			set_position_3.parent = frame_004
			group_010.parent = frame_004
			position_001_4.parent = frame_004
			mix.parent = frame_004
			reroute_009_1.parent = frame_004
			reroute_003_3.parent = frame_004
			group_input_011.parent = frame_004
			group_019_1.parent = frame_004
			group_015.parent = frame_008_1
			store_named_attribute_3.parent = frame_003
			group_016.parent = frame_005
			group_input_005.parent = frame_004
			set_handle_positions_008.parent = frame_004
			set_handle_positions_007.parent = frame_004
			set_handle_positions_009.parent = frame_004
			set_handle_positions_010.parent = frame_004
			set_handle_positions_003.parent = frame_003
			set_handle_positions_005.parent = frame_003
			set_handle_positions_004.parent = frame_003
			set_handle_positions_006.parent = frame_003
			group_002_4.parent = frame_005
			
			#Set locations
			frame_006_1.location = (-1366.132568359375, 289.572265625)
			frame_009.location = (-2332.05859375, 1913.763916015625)
			frame_008_1.location = (-2354.582275390625, 2424.24951171875)
			frame_005.location = (-15.40618896484375, -250.0697021484375)
			frame_007_1.location = (394.45556640625, 400.14013671875)
			frame_003.location = (-317.85302734375, -1007.8157958984375)
			frame_004.location = (-841.83837890625, -199.314453125)
			set_spline_resolution_002.location = (-2100.099609375, 2721.916259765625)
			reroute_006.location = (-2126.0078125, 2486.323486328125)
			boolean_math_016.location = (-3669.412841796875, 2606.323486328125)
			separate_geometry_005.location = (-3489.412841796875, 2806.323486328125)
			group_input_002.location = (-2831.1396484375, 2082.99365234375)
			mesh_to_curve_002.location = (-3240.0, 2800.0)
			set_position_004.location = (-2980.0, 2820.0)
			boolean_math_017.location = (-3240.0, 2680.0)
			endpoint_selection_001_2.location = (-3240.0, 2560.0)
			switch_003.location = (-60.0, 380.0)
			math_004.location = (-60.0, 540.0)
			math_005.location = (-220.0, 540.0)
			spline_length_001.location = (-380.0, 540.0)
			vector_rotate.location = (-1040.0, -260.0)
			vector.location = (-1220.0, -260.0)
			vector_math_001_1.location = (-700.0, -280.0)
			reroute_007_1.location = (-6685.658203125, 1880.0)
			group_008_1.location = (-1385.417724609375, -444.24951171875)
			resample_curve_001.location = (-2757.201171875, 2731.029052734375)
			set_handle_type_002.location = (-2260.0, 2720.0)
			set_spline_type.location = (-2420.0, 2720.0)
			group_018_1.location = (-4324.76953125, 1520.286376953125)
			boolean_math_003_3.location = (-4138.7490234375, 1563.5899658203125)
			boolean_math_001_7.location = (-4123.6044921875, 1424.9202880859375)
			group_input_010.location = (-4303.732421875, 1353.47900390625)
			combine_xyz_002_1.location = (-2271.80615234375, 1601.967041015625)
			reroute_011.location = (-2291.80615234375, 1441.967041015625)
			reroute_012.location = (-2091.80615234375, 1441.967041015625)
			math_001_6.location = (-2271.80615234375, 1641.967041015625)
			join_geometry_001_2.location = (-967.3782958984375, 1480.0)
			separate_geometry_003_1.location = (-4267.439453125, 1743.5623779296875)
			mesh_to_curve_1.location = (-4093.024169921875, 1739.939453125)
			set_spline_type_002.location = (-3933.024169921875, 1739.939453125)
			set_handle_type.location = (-3773.024169921875, 1739.939453125)
			set_handle_positions_001_1.location = (-3402.251953125, 1710.0697021484375)
			set_handle_positions_002.location = (-3242.251953125, 1710.0697021484375)
			reroute_002_6.location = (-3349.703857421875, 1510.0697021484375)
			reroute_008.location = (-3189.703857421875, 1510.0697021484375)
			endpoint_selection_002_1.location = (-3329.703857421875, 1830.0697021484375)
			endpoint_selection_003_1.location = (-3169.703857421875, 1830.0697021484375)
			store_named_attribute_002_1.location = (-199.57374572753906, 1612.9656982421875)
			group_input_004.location = (-2564.354248046875, 1721.967041015625)
			group_input_007.location = (-760.0, 1440.0)
			boolean_math_004_4.location = (-600.0, 1440.0)
			edge_angle_001.location = (-600.0, 1300.0)
			compare_006_1.location = (-440.0, 1300.0)
			boolean_math_002_4.location = (-440.0, 1440.0)
			realize_instances_1.location = (-780.0, 1500.0)
			position_3.location = (-2360.0, 3040.0)
			group_033.location = (-2360.0, 2960.0)
			group_004_2.location = (-2180.0, 3160.0)
			switch_9.location = (-1522.8076171875, 3373.817138671875)
			reroute_10.location = (-4909.38330078125, 3288.636962890625)
			reroute_004.location = (-1140.0, -1640.0)
			endpoint_selection_1.location = (-2020.0, -780.0)
			group_005_2.location = (-1860.0, -780.0)
			set_spline_resolution_001.location = (-1723.6593017578125, -602.0430297851562)
			group_032.location = (-2353.30224609375, -600.0)
			group_input_006.location = (-2630.1416015625, -876.25244140625)
			group_029_1.location = (-2721.81103515625, -737.4035034179688)
			set_handle_type_003.location = (-4045.0, -657.0)
			set_spline_type_001_1.location = (-4205.0, -657.0)
			group_030_1.location = (-1560.0, -600.0)
			group_028_1.location = (-3865.0, -657.0)
			set_spline_type_003.location = (-4116.6328125, 785.1316528320312)
			group_009_1.location = (-2745.187255859375, 416.64630126953125)
			join_geometry_002.location = (-2413.2392578125, 776.6463012695312)
			resample_curve_1.location = (-1973.2392578125, 816.6463012695312)
			set_spline_resolution_1.location = (-2219.64794921875, 789.2409057617188)
			endpoint_selection_004_2.location = (-3322.8984375, -487.47149658203125)
			group_011_2.location = (-3322.8984375, -787.4714965820312)
			endpoint_selection_006_1.location = (-3482.8984375, -487.47149658203125)
			group_014_1.location = (-3482.8984375, -787.4714965820312)
			endpoint_selection_005.location = (-3162.8984375, -487.47149658203125)
			endpoint_selection_007.location = (-3002.8984375, -487.47149658203125)
			group_007.location = (-3162.8984375, -787.4714965820312)
			group_020.location = (-3002.8984375, -787.4714965820312)
			endpoint_selection_008_1.location = (-3505.1455078125, 849.3387451171875)
			group_022_1.location = (-3505.1455078125, 549.3387451171875)
			endpoint_selection_009_1.location = (-3665.1455078125, 849.3387451171875)
			endpoint_selection_010_1.location = (-3345.1455078125, 849.3387451171875)
			endpoint_selection_011.location = (-3185.145263671875, 849.3387451171875)
			group_024_2.location = (-3345.1455078125, 549.3387451171875)
			group_025_1.location = (-3185.145263671875, 549.3387451171875)
			set_handle_type_001.location = (-3936.6328125, 785.1316528320312)
			vector_math_5.location = (-2747.376708984375, -14.962554931640625)
			reroute_001_9.location = (-2468.4931640625, 59.305511474609375)
			reroute_013.location = (-3578.16162109375, 219.314453125)
			boolean_math_007_1.location = (-3518.16162109375, 359.314453125)
			group_012_2.location = (-3518.16162109375, 239.314453125)
			boolean_math_006_1.location = (-3358.16162109375, 359.314453125)
			reroute_005_1.location = (-2238.16162109375, 199.314453125)
			group_013_1.location = (-3358.16162109375, 199.314453125)
			combine_xyz_001_1.location = (-2738.16162109375, -180.685546875)
			combine_xyz_1.location = (-3158.16162109375, 39.314453125)
			math_002_1.location = (-2938.16162109375, -240.685546875)
			math_6.location = (-2938.16162109375, -400.685546875)
			capture_attribute_1.location = (-1798.16162109375, 819.314453125)
			group_021_1.location = (-4330.72509765625, 217.2227783203125)
			switch_004.location = (-3917.2177734375, 73.55532836914062)
			switch_002_2.location = (-2937.197998046875, -4.88739013671875)
			boolean_math_009_1.location = (-3918.16162109375, -100.685546875)
			boolean_math_008_1.location = (-3918.16162109375, -240.685546875)
			math_009.location = (-3738.16162109375, 79.314453125)
			switch_005_1.location = (-3738.16162109375, -100.685546875)
			math_010.location = (-3558.16162109375, -100.685546875)
			separate_geometry_1.location = (-2773.2392578125, 856.6463012695312)
			boolean_math_9.location = (-2998.16162109375, 619.314453125)
			boolean_math_005_2.location = (-2998.16162109375, 579.314453125)
			group_input_008.location = (-2998.16162109375, 539.314453125)
			join_geometry.location = (-806.4035034179688, 692.7628784179688)
			group_003_2.location = (-2425.187255859375, 636.6463012695312)
			group_023_2.location = (-3665.1455078125, 549.3387451171875)
			group_006_2.location = (-2745.187255859375, 556.6463012695312)
			group_017.location = (-1920.0997314453125, 2721.916259765625)
			group_input_012.location = (-2218.16162109375, 659.314453125)
			set_position_3.location = (-1318.16162109375, 859.314453125)
			group_010.location = (-1638.16162109375, 639.314453125)
			position_001_4.location = (-1638.16162109375, 719.314453125)
			mix.location = (-1478.16162109375, 719.314453125)
			reroute_009_1.location = (-1858.16162109375, 339.314453125)
			reroute_003_3.location = (-838.16162109375, 339.314453125)
			group_input_011.location = (-1318.16162109375, 639.314453125)
			group_026_1.location = (-4220.0, 2580.0)
			group_019_1.location = (-1089.0626220703125, 862.9052124023438)
			group_015.location = (-880.0, -400.0)
			store_named_attribute_3.location = (-1382.14697265625, -592.1842041015625)
			group_016.location = (-2121.642822265625, 1829.195556640625)
			named_attribute_6.location = (-620.0, 1680.0)
			named_attribute_001_5.location = (-620.0, 1820.0)
			store_named_attribute_001_1.location = (60.831932067871094, 1781.5216064453125)
			group_output_40.location = (924.4188842773438, 1754.622314453125)
			set_material.location = (772.8197021484375, 1751.5650634765625)
			group_input_003.location = (612.8197021484375, 1651.5650634765625)
			sample_index.location = (-380.0, 1980.0)
			switch_001_2.location = (220.0, 1800.0)
			group_001_8.location = (-7240.0, 1740.0)
			group_input_39.location = (-7460.0, 1540.0)
			group_input_005.location = (-4650.06201171875, -62.146148681640625)
			group_input_001_2.location = (220.0, 1880.0)
			remove_named_attribute.location = (380.0, 1800.0)
			set_handle_positions_008.location = (-3665.1455078125, 729.3387451171875)
			set_handle_positions_007.location = (-3504.087890625, 735.6434326171875)
			set_handle_positions_009.location = (-3344.087890625, 735.6434326171875)
			set_handle_positions_010.location = (-3185.145263671875, 729.3387451171875)
			set_handle_positions_003.location = (-3321.84130859375, -601.1668090820312)
			set_handle_positions_005.location = (-3482.8984375, -607.4714965820312)
			set_handle_positions_004.location = (-3161.84130859375, -601.1668090820312)
			set_handle_positions_006.location = (-3002.8984375, -607.4714965820312)
			group_002_4.location = (-3713.108642578125, 1510.0697021484375)
			
			#Set dimensions
			frame_006_1.width, frame_006_1.height = 200.0, 254.0
			frame_009.width, frame_009.height = 520.0, 374.0
			frame_008_1.width, frame_008_1.height = 885.5, 352.0
			frame_005.width, frame_005.height = 2507.548095703125, 642.5
			frame_007_1.width, frame_007_1.height = 380.0, 376.0
			frame_003.width, frame_003.height = 3023.0, 598.5
			frame_004.width, frame_004.height = 4044.0, 1482.5
			set_spline_resolution_002.width, set_spline_resolution_002.height = 140.0, 100.0
			reroute_006.width, reroute_006.height = 16.0, 100.0
			boolean_math_016.width, boolean_math_016.height = 140.0, 100.0
			separate_geometry_005.width, separate_geometry_005.height = 203.40496826171875, 100.0
			group_input_002.width, group_input_002.height = 140.0, 100.0
			mesh_to_curve_002.width, mesh_to_curve_002.height = 140.0, 100.0
			set_position_004.width, set_position_004.height = 140.0, 100.0
			boolean_math_017.width, boolean_math_017.height = 140.0, 100.0
			endpoint_selection_001_2.width, endpoint_selection_001_2.height = 140.0, 100.0
			switch_003.width, switch_003.height = 140.0, 100.0
			math_004.width, math_004.height = 140.0, 100.0
			math_005.width, math_005.height = 140.0, 100.0
			spline_length_001.width, spline_length_001.height = 140.0, 100.0
			vector_rotate.width, vector_rotate.height = 140.0, 100.0
			vector.width, vector.height = 140.0, 100.0
			vector_math_001_1.width, vector_math_001_1.height = 140.0, 100.0
			reroute_007_1.width, reroute_007_1.height = 16.0, 100.0
			group_008_1.width, group_008_1.height = 326.6707763671875, 100.0
			resample_curve_001.width, resample_curve_001.height = 140.0, 100.0
			set_handle_type_002.width, set_handle_type_002.height = 140.0, 100.0
			set_spline_type.width, set_spline_type.height = 140.0, 100.0
			group_018_1.width, group_018_1.height = 158.9053955078125, 100.0
			boolean_math_003_3.width, boolean_math_003_3.height = 140.0, 100.0
			boolean_math_001_7.width, boolean_math_001_7.height = 140.0, 100.0
			group_input_010.width, group_input_010.height = 140.0, 100.0
			combine_xyz_002_1.width, combine_xyz_002_1.height = 140.0, 100.0
			reroute_011.width, reroute_011.height = 16.0, 100.0
			reroute_012.width, reroute_012.height = 16.0, 100.0
			math_001_6.width, math_001_6.height = 140.0, 100.0
			join_geometry_001_2.width, join_geometry_001_2.height = 140.0, 100.0
			separate_geometry_003_1.width, separate_geometry_003_1.height = 140.0, 100.0
			mesh_to_curve_1.width, mesh_to_curve_1.height = 140.0, 100.0
			set_spline_type_002.width, set_spline_type_002.height = 140.0, 100.0
			set_handle_type.width, set_handle_type.height = 140.0, 100.0
			set_handle_positions_001_1.width, set_handle_positions_001_1.height = 140.0, 100.0
			set_handle_positions_002.width, set_handle_positions_002.height = 140.0, 100.0
			reroute_002_6.width, reroute_002_6.height = 16.0, 100.0
			reroute_008.width, reroute_008.height = 16.0, 100.0
			endpoint_selection_002_1.width, endpoint_selection_002_1.height = 140.0, 100.0
			endpoint_selection_003_1.width, endpoint_selection_003_1.height = 140.0, 100.0
			store_named_attribute_002_1.width, store_named_attribute_002_1.height = 176.01080322265625, 100.0
			group_input_004.width, group_input_004.height = 140.0, 100.0
			group_input_007.width, group_input_007.height = 140.0, 100.0
			boolean_math_004_4.width, boolean_math_004_4.height = 140.0, 100.0
			edge_angle_001.width, edge_angle_001.height = 140.0, 100.0
			compare_006_1.width, compare_006_1.height = 140.0, 100.0
			boolean_math_002_4.width, boolean_math_002_4.height = 140.0, 100.0
			realize_instances_1.width, realize_instances_1.height = 140.0, 100.0
			position_3.width, position_3.height = 140.0, 100.0
			group_033.width, group_033.height = 140.0, 100.0
			group_004_2.width, group_004_2.height = 140.0, 100.0
			switch_9.width, switch_9.height = 140.0, 100.0
			reroute_10.width, reroute_10.height = 16.0, 100.0
			reroute_004.width, reroute_004.height = 16.0, 100.0
			endpoint_selection_1.width, endpoint_selection_1.height = 140.0, 100.0
			group_005_2.width, group_005_2.height = 227.437255859375, 100.0
			set_spline_resolution_001.width, set_spline_resolution_001.height = 140.0, 100.0
			group_032.width, group_032.height = 329.30224609375, 100.0
			group_input_006.width, group_input_006.height = 140.0, 100.0
			group_029_1.width, group_029_1.height = 253.837646484375, 100.0
			set_handle_type_003.width, set_handle_type_003.height = 140.0, 100.0
			set_spline_type_001_1.width, set_spline_type_001_1.height = 140.0, 100.0
			group_030_1.width, group_030_1.height = 140.0, 100.0
			group_028_1.width, group_028_1.height = 312.298828125, 100.0
			set_spline_type_003.width, set_spline_type_003.height = 140.0, 100.0
			group_009_1.width, group_009_1.height = 205.1739501953125, 100.0
			join_geometry_002.width, join_geometry_002.height = 140.0, 100.0
			resample_curve_1.width, resample_curve_1.height = 140.0, 100.0
			set_spline_resolution_1.width, set_spline_resolution_1.height = 140.0, 100.0
			endpoint_selection_004_2.width, endpoint_selection_004_2.height = 140.0, 100.0
			group_011_2.width, group_011_2.height = 140.0, 100.0
			endpoint_selection_006_1.width, endpoint_selection_006_1.height = 140.0, 100.0
			group_014_1.width, group_014_1.height = 140.0, 100.0
			endpoint_selection_005.width, endpoint_selection_005.height = 140.0, 100.0
			endpoint_selection_007.width, endpoint_selection_007.height = 140.0, 100.0
			group_007.width, group_007.height = 140.0, 100.0
			group_020.width, group_020.height = 140.0, 100.0
			endpoint_selection_008_1.width, endpoint_selection_008_1.height = 140.0, 100.0
			group_022_1.width, group_022_1.height = 140.0, 100.0
			endpoint_selection_009_1.width, endpoint_selection_009_1.height = 140.0, 100.0
			endpoint_selection_010_1.width, endpoint_selection_010_1.height = 140.0, 100.0
			endpoint_selection_011.width, endpoint_selection_011.height = 140.0, 100.0
			group_024_2.width, group_024_2.height = 140.0, 100.0
			group_025_1.width, group_025_1.height = 140.0, 100.0
			set_handle_type_001.width, set_handle_type_001.height = 140.0, 100.0
			vector_math_5.width, vector_math_5.height = 140.0, 100.0
			reroute_001_9.width, reroute_001_9.height = 16.0, 100.0
			reroute_013.width, reroute_013.height = 16.0, 100.0
			boolean_math_007_1.width, boolean_math_007_1.height = 140.0, 100.0
			group_012_2.width, group_012_2.height = 140.0, 100.0
			boolean_math_006_1.width, boolean_math_006_1.height = 140.0, 100.0
			reroute_005_1.width, reroute_005_1.height = 16.0, 100.0
			group_013_1.width, group_013_1.height = 140.0, 100.0
			combine_xyz_001_1.width, combine_xyz_001_1.height = 140.0, 100.0
			combine_xyz_1.width, combine_xyz_1.height = 140.0, 100.0
			math_002_1.width, math_002_1.height = 140.0, 100.0
			math_6.width, math_6.height = 140.0, 100.0
			capture_attribute_1.width, capture_attribute_1.height = 140.0, 100.0
			group_021_1.width, group_021_1.height = 287.59326171875, 100.0
			switch_004.width, switch_004.height = 140.0, 100.0
			switch_002_2.width, switch_002_2.height = 140.0, 100.0
			boolean_math_009_1.width, boolean_math_009_1.height = 140.0, 100.0
			boolean_math_008_1.width, boolean_math_008_1.height = 140.0, 100.0
			math_009.width, math_009.height = 140.0, 100.0
			switch_005_1.width, switch_005_1.height = 140.0, 100.0
			math_010.width, math_010.height = 140.0, 100.0
			separate_geometry_1.width, separate_geometry_1.height = 140.0, 100.0
			boolean_math_9.width, boolean_math_9.height = 140.0, 100.0
			boolean_math_005_2.width, boolean_math_005_2.height = 140.0, 100.0
			group_input_008.width, group_input_008.height = 140.0, 100.0
			join_geometry.width, join_geometry.height = 140.0, 100.0
			group_003_2.width, group_003_2.height = 181.6624755859375, 100.0
			group_023_2.width, group_023_2.height = 140.0, 100.0
			group_006_2.width, group_006_2.height = 193.6337890625, 100.0
			group_017.width, group_017.height = 226.826904296875, 100.0
			group_input_012.width, group_input_012.height = 140.0, 100.0
			set_position_3.width, set_position_3.height = 140.0, 100.0
			group_010.width, group_010.height = 140.0, 100.0
			position_001_4.width, position_001_4.height = 140.0, 100.0
			mix.width, mix.height = 140.0, 100.0
			reroute_009_1.width, reroute_009_1.height = 16.0, 100.0
			reroute_003_3.width, reroute_003_3.height = 16.0, 100.0
			group_input_011.width, group_input_011.height = 140.0, 100.0
			group_026_1.width, group_026_1.height = 256.740478515625, 100.0
			group_019_1.width, group_019_1.height = 244.548095703125, 100.0
			group_015.width, group_015.height = 140.0, 100.0
			store_named_attribute_3.width, store_named_attribute_3.height = 140.0, 100.0
			group_016.width, group_016.height = 244.548095703125, 100.0
			named_attribute_6.width, named_attribute_6.height = 140.0, 100.0
			named_attribute_001_5.width, named_attribute_001_5.height = 140.0, 100.0
			store_named_attribute_001_1.width, store_named_attribute_001_1.height = 140.0, 100.0
			group_output_40.width, group_output_40.height = 140.0, 100.0
			set_material.width, set_material.height = 140.0, 100.0
			group_input_003.width, group_input_003.height = 140.0, 100.0
			sample_index.width, sample_index.height = 140.0, 100.0
			switch_001_2.width, switch_001_2.height = 140.0, 100.0
			group_001_8.width, group_001_8.height = 276.27490234375, 100.0
			group_input_39.width, group_input_39.height = 140.0, 100.0
			group_input_005.width, group_input_005.height = 140.0, 100.0
			group_input_001_2.width, group_input_001_2.height = 140.0, 100.0
			remove_named_attribute.width, remove_named_attribute.height = 134.0596923828125, 100.0
			set_handle_positions_008.width, set_handle_positions_008.height = 140.0, 100.0
			set_handle_positions_007.width, set_handle_positions_007.height = 140.0, 100.0
			set_handle_positions_009.width, set_handle_positions_009.height = 140.0, 100.0
			set_handle_positions_010.width, set_handle_positions_010.height = 140.0, 100.0
			set_handle_positions_003.width, set_handle_positions_003.height = 140.0, 100.0
			set_handle_positions_005.width, set_handle_positions_005.height = 140.0, 100.0
			set_handle_positions_004.width, set_handle_positions_004.height = 140.0, 100.0
			set_handle_positions_006.width, set_handle_positions_006.height = 140.0, 100.0
			group_002_4.width, group_002_4.height = 323.40478515625, 100.0
			
			#initialize _mn_utils_style_cartoon links
			#reroute_10.Output -> group_004_2.Points
			_mn_utils_style_cartoon.links.new(reroute_10.outputs[0], group_004_2.inputs[0])
			#position_3.Position -> group_004_2.Position
			_mn_utils_style_cartoon.links.new(position_3.outputs[0], group_004_2.inputs[1])
			#endpoint_selection_1.Selection -> group_005_2.Switch
			_mn_utils_style_cartoon.links.new(endpoint_selection_1.outputs[0], group_005_2.inputs[0])
			#group_input_004.Profile Curve -> group_016.Instance
			_mn_utils_style_cartoon.links.new(group_input_004.outputs[10], group_016.inputs[4])
			#reroute_007_1.Output -> separate_geometry_003_1.Geometry
			_mn_utils_style_cartoon.links.new(reroute_007_1.outputs[0], separate_geometry_003_1.inputs[0])
			#set_handle_positions_002.Curve -> group_016.Curve
			_mn_utils_style_cartoon.links.new(set_handle_positions_002.outputs[0], group_016.inputs[0])
			#set_spline_resolution_001.Geometry -> group_030_1.Curve
			_mn_utils_style_cartoon.links.new(set_spline_resolution_001.outputs[0], group_030_1.inputs[0])
			#group_032.Curve -> set_spline_resolution_001.Geometry
			_mn_utils_style_cartoon.links.new(group_032.outputs[0], set_spline_resolution_001.inputs[0])
			#set_handle_type_003.Curve -> group_028_1.Geometry
			_mn_utils_style_cartoon.links.new(set_handle_type_003.outputs[0], group_028_1.inputs[0])
			#group_005_2.Output -> group_030_1.Radius (A)
			_mn_utils_style_cartoon.links.new(group_005_2.outputs[0], group_030_1.inputs[4])
			#reroute_004.Output -> join_geometry_001_2.Geometry
			_mn_utils_style_cartoon.links.new(reroute_004.outputs[0], join_geometry_001_2.inputs[0])
			#set_material.Geometry -> group_output_40.Cartoon Mesh
			_mn_utils_style_cartoon.links.new(set_material.outputs[0], group_output_40.inputs[0])
			#group_018_1.Is Helix -> boolean_math_003_3.Boolean
			_mn_utils_style_cartoon.links.new(group_018_1.outputs[0], boolean_math_003_3.inputs[1])
			#boolean_math_001_7.Boolean -> boolean_math_003_3.Boolean
			_mn_utils_style_cartoon.links.new(boolean_math_001_7.outputs[0], boolean_math_003_3.inputs[0])
			#boolean_math_003_3.Boolean -> separate_geometry_003_1.Selection
			_mn_utils_style_cartoon.links.new(boolean_math_003_3.outputs[0], separate_geometry_003_1.inputs[1])
			#group_033.Rotation -> group_004_2.Rotation
			_mn_utils_style_cartoon.links.new(group_033.outputs[0], group_004_2.inputs[3])
			#group_006_2.Geometry -> group_003_2.Instance
			_mn_utils_style_cartoon.links.new(group_006_2.outputs[0], group_003_2.inputs[1])
			#group_003_2.Trimmed Curve -> join_geometry_002.Geometry
			_mn_utils_style_cartoon.links.new(group_003_2.outputs[0], join_geometry_002.inputs[0])
			#vector_math_5.Vector -> group_003_2.Scale
			_mn_utils_style_cartoon.links.new(vector_math_5.outputs[0], group_003_2.inputs[3])
			#math_002_1.Value -> combine_xyz_001_1.Y
			_mn_utils_style_cartoon.links.new(math_002_1.outputs[0], combine_xyz_001_1.inputs[1])
			#math_6.Value -> combine_xyz_001_1.Z
			_mn_utils_style_cartoon.links.new(math_6.outputs[0], combine_xyz_001_1.inputs[2])
			#group_input_005.Arrow Width Scale -> math_6.Value
			_mn_utils_style_cartoon.links.new(group_input_005.outputs[9], math_6.inputs[0])
			#group_input_004.Helix Rotate -> math_001_6.Value
			_mn_utils_style_cartoon.links.new(group_input_004.outputs[22], math_001_6.inputs[0])
			#group_input_004.Helix Thickness -> combine_xyz_002_1.Y
			_mn_utils_style_cartoon.links.new(group_input_004.outputs[23], combine_xyz_002_1.inputs[1])
			#group_input_004.Helix Width -> combine_xyz_002_1.Z
			_mn_utils_style_cartoon.links.new(group_input_004.outputs[24], combine_xyz_002_1.inputs[2])
			#combine_xyz_002_1.Vector -> group_016.Scale
			_mn_utils_style_cartoon.links.new(combine_xyz_002_1.outputs[0], group_016.inputs[6])
			#math_001_6.Value -> group_016.Rotation X
			_mn_utils_style_cartoon.links.new(math_001_6.outputs[0], group_016.inputs[5])
			#group_004_2.Instances -> switch_9.True
			_mn_utils_style_cartoon.links.new(group_004_2.outputs[0], switch_9.inputs[2])
			#group_009_1.Rotation -> group_003_2.Rotation
			_mn_utils_style_cartoon.links.new(group_009_1.outputs[0], group_003_2.inputs[2])
			#group_input_003.Material -> set_material.Material
			_mn_utils_style_cartoon.links.new(group_input_003.outputs[4], set_material.inputs[2])
			#group_input_006.Loop Subdivisions -> set_spline_resolution_001.Resolution
			_mn_utils_style_cartoon.links.new(group_input_006.outputs[27], set_spline_resolution_001.inputs[2])
			#group_input_006.Loop Radius -> group_005_2.Input
			_mn_utils_style_cartoon.links.new(group_input_006.outputs[28], group_005_2.inputs[1])
			#group_input_006.Loop Resolution -> group_030_1.Resolution
			_mn_utils_style_cartoon.links.new(group_input_006.outputs[29], group_030_1.inputs[2])
			#reroute_007_1.Output -> reroute_10.Input
			_mn_utils_style_cartoon.links.new(reroute_007_1.outputs[0], reroute_10.inputs[0])
			#group_input_004.Profile Resolution -> group_016.Profile Resolution
			_mn_utils_style_cartoon.links.new(group_input_004.outputs[11], group_016.inputs[1])
			#group_input_005.Arrow Thickness Scale -> math_002_1.Value
			_mn_utils_style_cartoon.links.new(group_input_005.outputs[8], math_002_1.inputs[0])
			#separate_geometry_1.Inverted -> group_003_2.Curve
			_mn_utils_style_cartoon.links.new(separate_geometry_1.outputs[1], group_003_2.inputs[0])
			#reroute_003_3.Output -> join_geometry.Geometry
			_mn_utils_style_cartoon.links.new(reroute_003_3.outputs[0], join_geometry.inputs[0])
			#reroute_009_1.Output -> reroute_003_3.Input
			_mn_utils_style_cartoon.links.new(reroute_009_1.outputs[0], reroute_003_3.inputs[0])
			#store_named_attribute_3.Geometry -> reroute_004.Input
			_mn_utils_style_cartoon.links.new(store_named_attribute_3.outputs[0], reroute_004.inputs[0])
			#combine_xyz_001_1.Vector -> vector_math_5.Vector
			_mn_utils_style_cartoon.links.new(combine_xyz_001_1.outputs[0], vector_math_5.inputs[1])
			#group_001_8.Loop Splines -> set_spline_type_001_1.Curve
			_mn_utils_style_cartoon.links.new(group_001_8.outputs[6], set_spline_type_001_1.inputs[0])
			#set_handle_type_002.Curve -> set_spline_resolution_002.Geometry
			_mn_utils_style_cartoon.links.new(set_handle_type_002.outputs[0], set_spline_resolution_002.inputs[0])
			#set_position_004.Geometry -> resample_curve_001.Curve
			_mn_utils_style_cartoon.links.new(set_position_004.outputs[0], resample_curve_001.inputs[0])
			#resample_curve_001.Curve -> set_spline_type.Curve
			_mn_utils_style_cartoon.links.new(resample_curve_001.outputs[0], set_spline_type.inputs[0])
			#set_spline_resolution_002.Geometry -> group_017.Curve
			_mn_utils_style_cartoon.links.new(set_spline_resolution_002.outputs[0], group_017.inputs[0])
			#reroute_007_1.Output -> separate_geometry_005.Geometry
			_mn_utils_style_cartoon.links.new(reroute_007_1.outputs[0], separate_geometry_005.inputs[0])
			#reroute_006.Output -> set_spline_resolution_002.Resolution
			_mn_utils_style_cartoon.links.new(reroute_006.outputs[0], set_spline_resolution_002.inputs[2])
			#math_004.Value -> switch_003.True
			_mn_utils_style_cartoon.links.new(math_004.outputs[0], switch_003.inputs[2])
			#group_input_002.Cylinder Curved -> switch_003.Switch
			_mn_utils_style_cartoon.links.new(group_input_002.outputs[18], switch_003.inputs[0])
			#spline_length_001.Point Count -> math_005.Value
			_mn_utils_style_cartoon.links.new(spline_length_001.outputs[1], math_005.inputs[0])
			#math_005.Value -> math_004.Value
			_mn_utils_style_cartoon.links.new(math_005.outputs[0], math_004.inputs[0])
			#vector.Vector -> vector_rotate.Vector
			_mn_utils_style_cartoon.links.new(vector.outputs[0], vector_rotate.inputs[0])
			#mesh_to_curve_002.Curve -> set_position_004.Geometry
			_mn_utils_style_cartoon.links.new(mesh_to_curve_002.outputs[0], set_position_004.inputs[0])
			#vector_rotate.Vector -> vector_math_001_1.Vector
			_mn_utils_style_cartoon.links.new(vector_rotate.outputs[0], vector_math_001_1.inputs[0])
			#group_015.Angstrom -> vector_math_001_1.Scale
			_mn_utils_style_cartoon.links.new(group_015.outputs[0], vector_math_001_1.inputs[3])
			#vector_math_001_1.Vector -> set_position_004.Offset
			_mn_utils_style_cartoon.links.new(vector_math_001_1.outputs[0], set_position_004.inputs[3])
			#boolean_math_016.Boolean -> separate_geometry_005.Selection
			_mn_utils_style_cartoon.links.new(boolean_math_016.outputs[0], separate_geometry_005.inputs[1])
			#group_026_1.Is Helix -> boolean_math_016.Boolean
			_mn_utils_style_cartoon.links.new(group_026_1.outputs[0], boolean_math_016.inputs[0])
			#switch_003.Output -> resample_curve_001.Count
			_mn_utils_style_cartoon.links.new(switch_003.outputs[0], resample_curve_001.inputs[2])
			#group_input_002.Cylinder Resolution -> group_017.Resolution
			_mn_utils_style_cartoon.links.new(group_input_002.outputs[20], group_017.inputs[2])
			#group_input_002.Cylinder Radius -> group_017.Radius (A)
			_mn_utils_style_cartoon.links.new(group_input_002.outputs[19], group_017.inputs[4])
			#group_input_002.Cylinder Subdivisions -> reroute_006.Input
			_mn_utils_style_cartoon.links.new(group_input_002.outputs[21], reroute_006.inputs[0])
			#group_008_1.Rotation -> vector_rotate.Rotation
			_mn_utils_style_cartoon.links.new(group_008_1.outputs[0], vector_rotate.inputs[4])
			#group_input_002.As Cylinders -> boolean_math_016.Boolean
			_mn_utils_style_cartoon.links.new(group_input_002.outputs[17], boolean_math_016.inputs[1])
			#endpoint_selection_001_2.Selection -> boolean_math_017.Boolean
			_mn_utils_style_cartoon.links.new(endpoint_selection_001_2.outputs[0], boolean_math_017.inputs[0])
			#boolean_math_017.Boolean -> set_position_004.Selection
			_mn_utils_style_cartoon.links.new(boolean_math_017.outputs[0], set_position_004.inputs[1])
			#separate_geometry_005.Selection -> mesh_to_curve_002.Mesh
			_mn_utils_style_cartoon.links.new(separate_geometry_005.outputs[0], mesh_to_curve_002.inputs[0])
			#group_001_8.CA Mesh Line -> reroute_007_1.Input
			_mn_utils_style_cartoon.links.new(group_001_8.outputs[0], reroute_007_1.inputs[0])
			#group_input_39.Atoms -> group_001_8.Atoms
			_mn_utils_style_cartoon.links.new(group_input_39.outputs[0], group_001_8.inputs[0])
			#group_input_39.Selection -> group_001_8.Selection
			_mn_utils_style_cartoon.links.new(group_input_39.outputs[1], group_001_8.inputs[1])
			#set_spline_type_002.Curve -> set_handle_type.Curve
			_mn_utils_style_cartoon.links.new(set_spline_type_002.outputs[0], set_handle_type.inputs[0])
			#set_handle_type.Curve -> set_handle_positions_001_1.Curve
			_mn_utils_style_cartoon.links.new(set_handle_type.outputs[0], set_handle_positions_001_1.inputs[0])
			#endpoint_selection_002_1.Selection -> set_handle_positions_001_1.Selection
			_mn_utils_style_cartoon.links.new(endpoint_selection_002_1.outputs[0], set_handle_positions_001_1.inputs[1])
			#set_handle_positions_001_1.Curve -> set_handle_positions_002.Curve
			_mn_utils_style_cartoon.links.new(set_handle_positions_001_1.outputs[0], set_handle_positions_002.inputs[0])
			#endpoint_selection_003_1.Selection -> set_handle_positions_002.Selection
			_mn_utils_style_cartoon.links.new(endpoint_selection_003_1.outputs[0], set_handle_positions_002.inputs[1])
			#group_input_010.As Cylinders -> boolean_math_001_7.Boolean
			_mn_utils_style_cartoon.links.new(group_input_010.outputs[17], boolean_math_001_7.inputs[0])
			#reroute_002_6.Output -> set_handle_positions_001_1.Offset
			_mn_utils_style_cartoon.links.new(reroute_002_6.outputs[0], set_handle_positions_001_1.inputs[3])
			#reroute_008.Output -> set_handle_positions_002.Offset
			_mn_utils_style_cartoon.links.new(reroute_008.outputs[0], set_handle_positions_002.inputs[3])
			#group_002_4.Vector -> reroute_002_6.Input
			_mn_utils_style_cartoon.links.new(group_002_4.outputs[0], reroute_002_6.inputs[0])
			#reroute_002_6.Output -> reroute_008.Input
			_mn_utils_style_cartoon.links.new(reroute_002_6.outputs[0], reroute_008.inputs[0])
			#set_position_3.Geometry -> group_019_1.Curve
			_mn_utils_style_cartoon.links.new(set_position_3.outputs[0], group_019_1.inputs[0])
			#group_input_011.Profile Resolution -> group_019_1.Profile Resolution
			_mn_utils_style_cartoon.links.new(group_input_011.outputs[11], group_019_1.inputs[1])
			#group_input_011.Profile Curve -> group_019_1.Instance
			_mn_utils_style_cartoon.links.new(group_input_011.outputs[10], group_019_1.inputs[4])
			#group_input_011.Sheet Rotate -> group_019_1.Rotation X
			_mn_utils_style_cartoon.links.new(group_input_011.outputs[12], group_019_1.inputs[5])
			#group_003_2.ArrowHeads -> reroute_009_1.Input
			_mn_utils_style_cartoon.links.new(group_003_2.outputs[1], reroute_009_1.inputs[0])
			#reroute_012.Output -> group_016.Resolution
			_mn_utils_style_cartoon.links.new(reroute_012.outputs[0], group_016.inputs[9])
			#group_input_004.Helix Subdivisions -> reroute_011.Input
			_mn_utils_style_cartoon.links.new(group_input_004.outputs[25], reroute_011.inputs[0])
			#reroute_011.Output -> reroute_012.Input
			_mn_utils_style_cartoon.links.new(reroute_011.outputs[0], reroute_012.inputs[0])
			#separate_geometry_003_1.Selection -> mesh_to_curve_1.Mesh
			_mn_utils_style_cartoon.links.new(separate_geometry_003_1.outputs[0], mesh_to_curve_1.inputs[0])
			#mesh_to_curve_1.Curve -> set_spline_type_002.Curve
			_mn_utils_style_cartoon.links.new(mesh_to_curve_1.outputs[0], set_spline_type_002.inputs[0])
			#set_spline_type_003.Curve -> set_handle_type_001.Curve
			_mn_utils_style_cartoon.links.new(set_spline_type_003.outputs[0], set_handle_type_001.inputs[0])
			#group_input_011.Sheet Subdivision -> group_019_1.Resolution
			_mn_utils_style_cartoon.links.new(group_input_011.outputs[16], group_019_1.inputs[9])
			#group_001_8.BS Splines -> set_spline_type_003.Curve
			_mn_utils_style_cartoon.links.new(group_001_8.outputs[4], set_spline_type_003.inputs[0])
			#set_spline_type.Curve -> set_handle_type_002.Curve
			_mn_utils_style_cartoon.links.new(set_spline_type.outputs[0], set_handle_type_002.inputs[0])
			#group_input_39.Sheet Smoothing -> group_001_8.BS Smoothing
			_mn_utils_style_cartoon.links.new(group_input_39.outputs[15], group_001_8.inputs[2])
			#set_spline_type_001_1.Curve -> set_handle_type_003.Curve
			_mn_utils_style_cartoon.links.new(set_spline_type_001_1.outputs[0], set_handle_type_003.inputs[0])
			#join_geometry_001_2.Geometry -> realize_instances_1.Geometry
			_mn_utils_style_cartoon.links.new(join_geometry_001_2.outputs[0], realize_instances_1.inputs[0])
			#edge_angle_001.Signed Angle -> compare_006_1.A
			_mn_utils_style_cartoon.links.new(edge_angle_001.outputs[1], compare_006_1.inputs[0])
			#endpoint_selection_004_2.Selection -> set_handle_positions_003.Selection
			_mn_utils_style_cartoon.links.new(endpoint_selection_004_2.outputs[0], set_handle_positions_003.inputs[1])
			#set_handle_positions_003.Curve -> set_handle_positions_004.Curve
			_mn_utils_style_cartoon.links.new(set_handle_positions_003.outputs[0], set_handle_positions_004.inputs[0])
			#endpoint_selection_005.Selection -> set_handle_positions_004.Selection
			_mn_utils_style_cartoon.links.new(endpoint_selection_005.outputs[0], set_handle_positions_004.inputs[1])
			#group_007.Vector -> set_handle_positions_004.Offset
			_mn_utils_style_cartoon.links.new(group_007.outputs[0], set_handle_positions_004.inputs[3])
			#set_handle_positions_006.Curve -> group_032.Curve
			_mn_utils_style_cartoon.links.new(set_handle_positions_006.outputs[0], group_032.inputs[0])
			#realize_instances_1.Geometry -> store_named_attribute_002_1.Geometry
			_mn_utils_style_cartoon.links.new(realize_instances_1.outputs[0], store_named_attribute_002_1.inputs[0])
			#group_input_007.Shade Smooth -> boolean_math_004_4.Boolean
			_mn_utils_style_cartoon.links.new(group_input_007.outputs[2], boolean_math_004_4.inputs[0])
			#boolean_math_004_4.Boolean -> boolean_math_002_4.Boolean
			_mn_utils_style_cartoon.links.new(boolean_math_004_4.outputs[0], boolean_math_002_4.inputs[0])
			#boolean_math_002_4.Boolean -> store_named_attribute_002_1.Value
			_mn_utils_style_cartoon.links.new(boolean_math_002_4.outputs[0], store_named_attribute_002_1.inputs[3])
			#compare_006_1.Result -> boolean_math_002_4.Boolean
			_mn_utils_style_cartoon.links.new(compare_006_1.outputs[0], boolean_math_002_4.inputs[1])
			#capture_attribute_1.Geometry -> set_position_3.Geometry
			_mn_utils_style_cartoon.links.new(capture_attribute_1.outputs[0], set_position_3.inputs[0])
			#position_001_4.Position -> group_010.Field
			_mn_utils_style_cartoon.links.new(position_001_4.outputs[0], group_010.inputs[0])
			#set_spline_resolution_1.Geometry -> resample_curve_1.Curve
			_mn_utils_style_cartoon.links.new(set_spline_resolution_1.outputs[0], resample_curve_1.inputs[0])
			#reroute_013.Output -> group_012_2.Boolean
			_mn_utils_style_cartoon.links.new(reroute_013.outputs[0], group_012_2.inputs[0])
			#group_012_2.Boolean -> boolean_math_006_1.Boolean
			_mn_utils_style_cartoon.links.new(group_012_2.outputs[0], boolean_math_006_1.inputs[1])
			#reroute_013.Output -> boolean_math_007_1.Boolean
			_mn_utils_style_cartoon.links.new(reroute_013.outputs[0], boolean_math_007_1.inputs[0])
			#boolean_math_007_1.Boolean -> boolean_math_006_1.Boolean
			_mn_utils_style_cartoon.links.new(boolean_math_007_1.outputs[0], boolean_math_006_1.inputs[0])
			#reroute_005_1.Output -> set_position_3.Selection
			_mn_utils_style_cartoon.links.new(reroute_005_1.outputs[0], set_position_3.inputs[1])
			#boolean_math_006_1.Boolean -> group_013_1.Boolean
			_mn_utils_style_cartoon.links.new(boolean_math_006_1.outputs[0], group_013_1.inputs[0])
			#position_001_4.Position -> mix.A
			_mn_utils_style_cartoon.links.new(position_001_4.outputs[0], mix.inputs[4])
			#group_010.Field -> mix.B
			_mn_utils_style_cartoon.links.new(group_010.outputs[0], mix.inputs[5])
			#mix.Result -> set_position_3.Position
			_mn_utils_style_cartoon.links.new(mix.outputs[1], set_position_3.inputs[2])
			#resample_curve_1.Curve -> capture_attribute_1.Geometry
			_mn_utils_style_cartoon.links.new(resample_curve_1.outputs[0], capture_attribute_1.inputs[0])
			#reroute_001_9.Output -> capture_attribute_1.Value
			_mn_utils_style_cartoon.links.new(reroute_001_9.outputs[0], capture_attribute_1.inputs[1])
			#join_geometry_002.Geometry -> set_spline_resolution_1.Geometry
			_mn_utils_style_cartoon.links.new(join_geometry_002.outputs[0], set_spline_resolution_1.inputs[0])
			#group_input_005.Sheet Width -> math_009.Value
			_mn_utils_style_cartoon.links.new(group_input_005.outputs[14], math_009.inputs[1])
			#group_011_2.Vector -> set_handle_positions_003.Offset
			_mn_utils_style_cartoon.links.new(group_011_2.outputs[0], set_handle_positions_003.inputs[3])
			#endpoint_selection_006_1.Selection -> set_handle_positions_005.Selection
			_mn_utils_style_cartoon.links.new(endpoint_selection_006_1.outputs[0], set_handle_positions_005.inputs[1])
			#group_014_1.Vector -> set_handle_positions_005.Offset
			_mn_utils_style_cartoon.links.new(group_014_1.outputs[0], set_handle_positions_005.inputs[3])
			#group_028_1.Geometry -> set_handle_positions_005.Curve
			_mn_utils_style_cartoon.links.new(group_028_1.outputs[0], set_handle_positions_005.inputs[0])
			#set_handle_positions_005.Curve -> set_handle_positions_003.Curve
			_mn_utils_style_cartoon.links.new(set_handle_positions_005.outputs[0], set_handle_positions_003.inputs[0])
			#set_handle_positions_004.Curve -> set_handle_positions_006.Curve
			_mn_utils_style_cartoon.links.new(set_handle_positions_004.outputs[0], set_handle_positions_006.inputs[0])
			#endpoint_selection_007.Selection -> set_handle_positions_006.Selection
			_mn_utils_style_cartoon.links.new(endpoint_selection_007.outputs[0], set_handle_positions_006.inputs[1])
			#group_020.Vector -> set_handle_positions_006.Offset
			_mn_utils_style_cartoon.links.new(group_020.outputs[0], set_handle_positions_006.inputs[3])
			#group_021_1.Result -> reroute_013.Input
			_mn_utils_style_cartoon.links.new(group_021_1.outputs[0], reroute_013.inputs[0])
			#endpoint_selection_008_1.Selection -> set_handle_positions_007.Selection
			_mn_utils_style_cartoon.links.new(endpoint_selection_008_1.outputs[0], set_handle_positions_007.inputs[1])
			#set_handle_positions_007.Curve -> set_handle_positions_009.Curve
			_mn_utils_style_cartoon.links.new(set_handle_positions_007.outputs[0], set_handle_positions_009.inputs[0])
			#endpoint_selection_010_1.Selection -> set_handle_positions_009.Selection
			_mn_utils_style_cartoon.links.new(endpoint_selection_010_1.outputs[0], set_handle_positions_009.inputs[1])
			#group_024_2.Vector -> set_handle_positions_009.Offset
			_mn_utils_style_cartoon.links.new(group_024_2.outputs[0], set_handle_positions_009.inputs[3])
			#group_022_1.Vector -> set_handle_positions_007.Offset
			_mn_utils_style_cartoon.links.new(group_022_1.outputs[0], set_handle_positions_007.inputs[3])
			#endpoint_selection_009_1.Selection -> set_handle_positions_008.Selection
			_mn_utils_style_cartoon.links.new(endpoint_selection_009_1.outputs[0], set_handle_positions_008.inputs[1])
			#group_023_2.Vector -> set_handle_positions_008.Offset
			_mn_utils_style_cartoon.links.new(group_023_2.outputs[0], set_handle_positions_008.inputs[3])
			#set_handle_positions_008.Curve -> set_handle_positions_007.Curve
			_mn_utils_style_cartoon.links.new(set_handle_positions_008.outputs[0], set_handle_positions_007.inputs[0])
			#set_handle_positions_009.Curve -> set_handle_positions_010.Curve
			_mn_utils_style_cartoon.links.new(set_handle_positions_009.outputs[0], set_handle_positions_010.inputs[0])
			#endpoint_selection_011.Selection -> set_handle_positions_010.Selection
			_mn_utils_style_cartoon.links.new(endpoint_selection_011.outputs[0], set_handle_positions_010.inputs[1])
			#group_025_1.Vector -> set_handle_positions_010.Offset
			_mn_utils_style_cartoon.links.new(group_025_1.outputs[0], set_handle_positions_010.inputs[3])
			#set_handle_type_001.Curve -> set_handle_positions_008.Curve
			_mn_utils_style_cartoon.links.new(set_handle_type_001.outputs[0], set_handle_positions_008.inputs[0])
			#set_handle_positions_010.Curve -> separate_geometry_1.Geometry
			_mn_utils_style_cartoon.links.new(set_handle_positions_010.outputs[0], separate_geometry_1.inputs[0])
			#combine_xyz_1.Vector -> reroute_001_9.Input
			_mn_utils_style_cartoon.links.new(combine_xyz_1.outputs[0], reroute_001_9.inputs[0])
			#capture_attribute_1.Value -> group_019_1.Scale
			_mn_utils_style_cartoon.links.new(capture_attribute_1.outputs[1], group_019_1.inputs[6])
			#math_009.Value -> combine_xyz_1.Z
			_mn_utils_style_cartoon.links.new(math_009.outputs[0], combine_xyz_1.inputs[2])
			#group_013_1.Boolean -> reroute_005_1.Input
			_mn_utils_style_cartoon.links.new(group_013_1.outputs[0], reroute_005_1.inputs[0])
			#switch_002_2.Output -> vector_math_5.Vector
			_mn_utils_style_cartoon.links.new(switch_002_2.outputs[0], vector_math_5.inputs[0])
			#combine_xyz_1.Vector -> switch_002_2.False
			_mn_utils_style_cartoon.links.new(combine_xyz_1.outputs[0], switch_002_2.inputs[1])
			#group_input_008.Arrows Sharp -> boolean_math_005_2.Boolean
			_mn_utils_style_cartoon.links.new(group_input_008.outputs[6], boolean_math_005_2.inputs[1])
			#boolean_math_005_2.Boolean -> boolean_math_9.Boolean
			_mn_utils_style_cartoon.links.new(boolean_math_005_2.outputs[0], boolean_math_9.inputs[0])
			#switch_004.Output -> math_009.Value
			_mn_utils_style_cartoon.links.new(switch_004.outputs[0], math_009.inputs[0])
			#group_021_1.Output -> switch_004.True
			_mn_utils_style_cartoon.links.new(group_021_1.outputs[1], switch_004.inputs[2])
			#group_input_005.Arrows Sharp -> boolean_math_008_1.Boolean
			_mn_utils_style_cartoon.links.new(group_input_005.outputs[6], boolean_math_008_1.inputs[0])
			#boolean_math_008_1.Boolean -> boolean_math_009_1.Boolean
			_mn_utils_style_cartoon.links.new(boolean_math_008_1.outputs[0], boolean_math_009_1.inputs[1])
			#group_input_005.As Arrows -> boolean_math_009_1.Boolean
			_mn_utils_style_cartoon.links.new(group_input_005.outputs[5], boolean_math_009_1.inputs[0])
			#boolean_math_009_1.Boolean -> switch_004.Switch
			_mn_utils_style_cartoon.links.new(boolean_math_009_1.outputs[0], switch_004.inputs[0])
			#switch_005_1.Output -> math_010.Value
			_mn_utils_style_cartoon.links.new(switch_005_1.outputs[0], math_010.inputs[0])
			#group_input_005.Sheet Thickness -> math_010.Value
			_mn_utils_style_cartoon.links.new(group_input_005.outputs[13], math_010.inputs[1])
			#math_010.Value -> combine_xyz_1.Y
			_mn_utils_style_cartoon.links.new(math_010.outputs[0], combine_xyz_1.inputs[1])
			#group_input_005.Arrows Point -> switch_005_1.Switch
			_mn_utils_style_cartoon.links.new(group_input_005.outputs[7], switch_005_1.inputs[0])
			#switch_004.Output -> switch_005_1.True
			_mn_utils_style_cartoon.links.new(switch_004.outputs[0], switch_005_1.inputs[2])
			#boolean_math_9.Boolean -> separate_geometry_1.Selection
			_mn_utils_style_cartoon.links.new(boolean_math_9.outputs[0], separate_geometry_1.inputs[1])
			#group_input_008.As Arrows -> boolean_math_005_2.Boolean
			_mn_utils_style_cartoon.links.new(group_input_008.outputs[5], boolean_math_005_2.inputs[0])
			#group_input_012.Sheet Subdivision -> set_spline_resolution_1.Resolution
			_mn_utils_style_cartoon.links.new(group_input_012.outputs[16], set_spline_resolution_1.inputs[2])
			#group_030_1.Mesh -> store_named_attribute_3.Geometry
			_mn_utils_style_cartoon.links.new(group_030_1.outputs[0], store_named_attribute_3.inputs[0])
			#named_attribute_6.Attribute -> sample_index.Index
			_mn_utils_style_cartoon.links.new(named_attribute_6.outputs[0], sample_index.inputs[2])
			#named_attribute_001_5.Attribute -> sample_index.Value
			_mn_utils_style_cartoon.links.new(named_attribute_001_5.outputs[0], sample_index.inputs[1])
			#reroute_007_1.Output -> sample_index.Geometry
			_mn_utils_style_cartoon.links.new(reroute_007_1.outputs[0], sample_index.inputs[0])
			#store_named_attribute_002_1.Geometry -> store_named_attribute_001_1.Geometry
			_mn_utils_style_cartoon.links.new(store_named_attribute_002_1.outputs[0], store_named_attribute_001_1.inputs[0])
			#store_named_attribute_002_1.Geometry -> switch_001_2.True
			_mn_utils_style_cartoon.links.new(store_named_attribute_002_1.outputs[0], switch_001_2.inputs[2])
			#store_named_attribute_001_1.Geometry -> switch_001_2.False
			_mn_utils_style_cartoon.links.new(store_named_attribute_001_1.outputs[0], switch_001_2.inputs[1])
			#group_input_001_2.Interpolate Color -> switch_001_2.Switch
			_mn_utils_style_cartoon.links.new(group_input_001_2.outputs[3], switch_001_2.inputs[0])
			#sample_index.Value -> store_named_attribute_001_1.Value
			_mn_utils_style_cartoon.links.new(sample_index.outputs[0], store_named_attribute_001_1.inputs[3])
			#switch_001_2.Output -> remove_named_attribute.Geometry
			_mn_utils_style_cartoon.links.new(switch_001_2.outputs[0], remove_named_attribute.inputs[0])
			#remove_named_attribute.Geometry -> set_material.Geometry
			_mn_utils_style_cartoon.links.new(remove_named_attribute.outputs[0], set_material.inputs[0])
			#separate_geometry_1.Selection -> join_geometry_002.Geometry
			_mn_utils_style_cartoon.links.new(separate_geometry_1.outputs[0], join_geometry_002.inputs[0])
			#group_016.Geometry -> join_geometry_001_2.Geometry
			_mn_utils_style_cartoon.links.new(group_016.outputs[0], join_geometry_001_2.inputs[0])
			#group_019_1.Geometry -> join_geometry.Geometry
			_mn_utils_style_cartoon.links.new(group_019_1.outputs[0], join_geometry.inputs[0])
			#join_geometry.Geometry -> join_geometry_001_2.Geometry
			_mn_utils_style_cartoon.links.new(join_geometry.outputs[0], join_geometry_001_2.inputs[0])
			#group_017.Mesh -> join_geometry_001_2.Geometry
			_mn_utils_style_cartoon.links.new(group_017.outputs[0], join_geometry_001_2.inputs[0])
			#switch_9.Output -> join_geometry_001_2.Geometry
			_mn_utils_style_cartoon.links.new(switch_9.outputs[0], join_geometry_001_2.inputs[0])
			return _mn_utils_style_cartoon

		_mn_utils_style_cartoon = _mn_utils_style_cartoon_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".MN_utils_style_cartoon", type = 'NODES')
		mod.node_group = _mn_utils_style_cartoon
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_MN_utils_style_cartoon.bl_idname)
			
def register():
	bpy.utils.register_class(_MN_utils_style_cartoon)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_MN_utils_style_cartoon)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
