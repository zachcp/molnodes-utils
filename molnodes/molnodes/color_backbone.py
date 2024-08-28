bl_info = {
	"name" : "Color Backbone",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Color_Backbone(bpy.types.Operator):
	bl_idname = "node.color_backbone"
	bl_label = "Color Backbone"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize fallback_boolean node group
		def fallback_boolean_node_group():
			fallback_boolean = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Fallback Boolean")

			fallback_boolean.color_tag = 'INPUT'
			fallback_boolean.description = "Computes the boolean field if the given attribute doesn't exist. If it doesn't exist it just uses the attribute instead"

			
			#fallback_boolean interface
			#Socket Boolean
			boolean_socket = fallback_boolean.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket.default_value = False
			boolean_socket.attribute_domain = 'POINT'
			
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
			group_output = fallback_boolean.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = fallback_boolean.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Named Attribute
			named_attribute = fallback_boolean.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'BOOLEAN'
			
			#node Switch
			switch = fallback_boolean.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'BOOLEAN'
			
			
			
			
			#Set locations
			group_output.location = (276.6171569824219, 4.738137245178223)
			group_input.location = (-280.0, 0.0)
			named_attribute.location = (-94.73597717285156, 4.738137245178223)
			switch.location = (86.61715698242188, 4.738137245178223)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			
			#initialize fallback_boolean links
			#named_attribute.Exists -> switch.Switch
			fallback_boolean.links.new(named_attribute.outputs[1], switch.inputs[0])
			#named_attribute.Attribute -> switch.True
			fallback_boolean.links.new(named_attribute.outputs[0], switch.inputs[2])
			#group_input.Fallback -> switch.False
			fallback_boolean.links.new(group_input.outputs[1], switch.inputs[1])
			#switch.Output -> group_output.Boolean
			fallback_boolean.links.new(switch.outputs[0], group_output.inputs[0])
			#group_input.Name -> named_attribute.Name
			fallback_boolean.links.new(group_input.outputs[0], named_attribute.inputs[0])
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
			group_input_1 = _mn_constants_atom_name_peptide.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			
			#node Group Output
			group_output_1 = _mn_constants_atom_name_peptide.nodes.new("NodeGroupOutput")
			group_output_1.name = "Group Output"
			group_output_1.is_active_output = True
			
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
			group_input_1.location = (-200.0, 0.0)
			group_output_1.location = (260.0, 180.0)
			integer_001.location = (0.0, -50.0)
			integer_004.location = (0.0, -140.0)
			integer.location = (0.0, 40.0)
			integer_003.location = (0.0, 240.0)
			integer_002.location = (0.0, 140.0)
			
			#Set dimensions
			group_input_1.width, group_input_1.height = 140.0, 100.0
			group_output_1.width, group_output_1.height = 140.0, 100.0
			integer_001.width, integer_001.height = 140.0, 100.0
			integer_004.width, integer_004.height = 140.0, 100.0
			integer.width, integer.height = 140.0, 100.0
			integer_003.width, integer_003.height = 140.0, 100.0
			integer_002.width, integer_002.height = 140.0, 100.0
			
			#initialize _mn_constants_atom_name_peptide links
			#integer_003.Integer -> group_output_1.Backbone Lower
			_mn_constants_atom_name_peptide.links.new(integer_003.outputs[0], group_output_1.inputs[0])
			#integer_002.Integer -> group_output_1.Backbone Upper
			_mn_constants_atom_name_peptide.links.new(integer_002.outputs[0], group_output_1.inputs[1])
			#integer.Integer -> group_output_1.Side Chain Lower
			_mn_constants_atom_name_peptide.links.new(integer.outputs[0], group_output_1.inputs[2])
			#integer_001.Integer -> group_output_1.Side Chain Upper
			_mn_constants_atom_name_peptide.links.new(integer_001.outputs[0], group_output_1.inputs[3])
			#integer_004.Integer -> group_output_1.Alpha Carbon
			_mn_constants_atom_name_peptide.links.new(integer_004.outputs[0], group_output_1.inputs[4])
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
			group_input_2 = _mn_select_peptide.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
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
			boolean_math_001 = _mn_select_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001.name = "Boolean Math.001"
			boolean_math_001.operation = 'AND'
			
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
			boolean_math_002 = _mn_select_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002.name = "Boolean Math.002"
			boolean_math_002.operation = 'AND'
			
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
			group_output_2 = _mn_select_peptide.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
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
			group = _mn_select_peptide.nodes.new("GeometryNodeGroup")
			group.name = "Group"
			group.node_tree = _mn_constants_atom_name_peptide
			
			#node Boolean Math
			boolean_math = _mn_select_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'OR'
			
			
			
			
			#Set locations
			group_input_2.location = (-460.0, 0.0)
			compare.location = (80.0, 80.0)
			compare_001.location = (80.0, -80.0)
			boolean_math_001.location = (260.0, 80.0)
			compare_002.location = (80.0, -240.0)
			compare_003.location = (80.0, -400.0)
			boolean_math_002.location = (260.0, -240.0)
			compare_004.location = (80.0, -560.0)
			named_attribute_1.location = (-360.0, -480.0)
			boolean_math_003.location = (260.0, -560.0)
			group_output_2.location = (666.1161499023438, -263.7054748535156)
			compare_005.location = (80.0, -720.0)
			compare_006.location = (260.0, -380.0)
			group.location = (-411.24090576171875, -312.71807861328125)
			boolean_math.location = (420.0, -240.0)
			
			#Set dimensions
			group_input_2.width, group_input_2.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
			compare_002.width, compare_002.height = 153.86517333984375, 100.0
			compare_003.width, compare_003.height = 153.86517333984375, 100.0
			boolean_math_002.width, boolean_math_002.height = 140.0, 100.0
			compare_004.width, compare_004.height = 140.0, 100.0
			named_attribute_1.width, named_attribute_1.height = 140.0, 100.0
			boolean_math_003.width, boolean_math_003.height = 140.0, 100.0
			group_output_2.width, group_output_2.height = 140.0, 100.0
			compare_005.width, compare_005.height = 140.0, 100.0
			compare_006.width, compare_006.height = 140.0, 100.0
			group.width, group.height = 369.1165771484375, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			
			#initialize _mn_select_peptide links
			#compare_001.Result -> boolean_math_001.Boolean
			_mn_select_peptide.links.new(compare_001.outputs[0], boolean_math_001.inputs[1])
			#group.Backbone Lower -> compare.B
			_mn_select_peptide.links.new(group.outputs[0], compare.inputs[3])
			#named_attribute_1.Attribute -> compare.A
			_mn_select_peptide.links.new(named_attribute_1.outputs[0], compare.inputs[2])
			#compare.Result -> boolean_math_001.Boolean
			_mn_select_peptide.links.new(compare.outputs[0], boolean_math_001.inputs[0])
			#named_attribute_1.Attribute -> compare_001.A
			_mn_select_peptide.links.new(named_attribute_1.outputs[0], compare_001.inputs[2])
			#group.Backbone Upper -> compare_001.B
			_mn_select_peptide.links.new(group.outputs[1], compare_001.inputs[3])
			#boolean_math_001.Boolean -> group_output_2.Is Backbone
			_mn_select_peptide.links.new(boolean_math_001.outputs[0], group_output_2.inputs[0])
			#compare_003.Result -> boolean_math_002.Boolean
			_mn_select_peptide.links.new(compare_003.outputs[0], boolean_math_002.inputs[1])
			#named_attribute_1.Attribute -> compare_002.A
			_mn_select_peptide.links.new(named_attribute_1.outputs[0], compare_002.inputs[2])
			#compare_002.Result -> boolean_math_002.Boolean
			_mn_select_peptide.links.new(compare_002.outputs[0], boolean_math_002.inputs[0])
			#named_attribute_1.Attribute -> compare_003.A
			_mn_select_peptide.links.new(named_attribute_1.outputs[0], compare_003.inputs[2])
			#group.Side Chain Lower -> compare_002.B
			_mn_select_peptide.links.new(group.outputs[2], compare_002.inputs[3])
			#group.Side Chain Upper -> compare_003.B
			_mn_select_peptide.links.new(group.outputs[3], compare_003.inputs[3])
			#compare_005.Result -> boolean_math_003.Boolean
			_mn_select_peptide.links.new(compare_005.outputs[0], boolean_math_003.inputs[1])
			#named_attribute_1.Attribute -> compare_004.A
			_mn_select_peptide.links.new(named_attribute_1.outputs[0], compare_004.inputs[2])
			#compare_004.Result -> boolean_math_003.Boolean
			_mn_select_peptide.links.new(compare_004.outputs[0], boolean_math_003.inputs[0])
			#named_attribute_1.Attribute -> compare_005.A
			_mn_select_peptide.links.new(named_attribute_1.outputs[0], compare_005.inputs[2])
			#group.Backbone Lower -> compare_004.B
			_mn_select_peptide.links.new(group.outputs[0], compare_004.inputs[3])
			#group.Side Chain Upper -> compare_005.B
			_mn_select_peptide.links.new(group.outputs[3], compare_005.inputs[3])
			#boolean_math_003.Boolean -> group_output_2.Is Peptide
			_mn_select_peptide.links.new(boolean_math_003.outputs[0], group_output_2.inputs[2])
			#named_attribute_1.Attribute -> compare_006.A
			_mn_select_peptide.links.new(named_attribute_1.outputs[0], compare_006.inputs[2])
			#group.Alpha Carbon -> compare_006.B
			_mn_select_peptide.links.new(group.outputs[4], compare_006.inputs[3])
			#compare_006.Result -> group_output_2.Is Alpha Carbon
			_mn_select_peptide.links.new(compare_006.outputs[0], group_output_2.inputs[3])
			#boolean_math_002.Boolean -> boolean_math.Boolean
			_mn_select_peptide.links.new(boolean_math_002.outputs[0], boolean_math.inputs[0])
			#compare_006.Result -> boolean_math.Boolean
			_mn_select_peptide.links.new(compare_006.outputs[0], boolean_math.inputs[1])
			#boolean_math.Boolean -> group_output_2.Is Side Chain
			_mn_select_peptide.links.new(boolean_math.outputs[0], group_output_2.inputs[1])
			return _mn_select_peptide

		_mn_select_peptide = _mn_select_peptide_node_group()

		#initialize is_alpha_carbon node group
		def is_alpha_carbon_node_group():
			is_alpha_carbon = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Is Alpha Carbon")

			is_alpha_carbon.color_tag = 'INPUT'
			is_alpha_carbon.description = ""

			
			#is_alpha_carbon interface
			#Socket Selection
			selection_socket = is_alpha_carbon.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket.default_value = False
			selection_socket.attribute_domain = 'POINT'
			selection_socket.description = "True if atom is an alpha carbon of an amino acid"
			
			#Socket Inverted
			inverted_socket = is_alpha_carbon.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket.default_value = False
			inverted_socket.attribute_domain = 'POINT'
			
			#Socket And
			and_socket = is_alpha_carbon.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket.default_value = True
			and_socket.attribute_domain = 'POINT'
			and_socket.hide_value = True
			
			#Socket Or
			or_socket = is_alpha_carbon.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket.default_value = False
			or_socket.attribute_domain = 'POINT'
			or_socket.hide_value = True
			
			
			#initialize is_alpha_carbon nodes
			#node Group Output
			group_output_3 = is_alpha_carbon.nodes.new("NodeGroupOutput")
			group_output_3.name = "Group Output"
			group_output_3.is_active_output = True
			
			#node Group Input
			group_input_3 = is_alpha_carbon.nodes.new("NodeGroupInput")
			group_input_3.name = "Group Input"
			
			#node Boolean Math.001
			boolean_math_001_1 = is_alpha_carbon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_1.name = "Boolean Math.001"
			boolean_math_001_1.operation = 'AND'
			
			#node Group.001
			group_001 = is_alpha_carbon.nodes.new("GeometryNodeGroup")
			group_001.name = "Group.001"
			group_001.node_tree = fallback_boolean
			#Socket_2
			group_001.inputs[0].default_value = "is_alpha_carbon"
			
			#node Group.002
			group_002 = is_alpha_carbon.nodes.new("GeometryNodeGroup")
			group_002.name = "Group.002"
			group_002.node_tree = _mn_select_peptide
			group_002.outputs[0].hide = True
			group_002.outputs[1].hide = True
			group_002.outputs[2].hide = True
			
			#node Boolean Math.002
			boolean_math_002_1 = is_alpha_carbon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_1.name = "Boolean Math.002"
			boolean_math_002_1.operation = 'OR'
			
			#node Boolean Math
			boolean_math_1 = is_alpha_carbon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_1.name = "Boolean Math"
			boolean_math_1.operation = 'NOT'
			
			
			
			
			#Set locations
			group_output_3.location = (520.0, 0.0)
			group_input_3.location = (-200.0, 0.0)
			boolean_math_001_1.location = (160.0, 0.0)
			group_001.location = (-88.33343505859375, -180.0)
			group_002.location = (-290.4490661621094, -180.0)
			boolean_math_002_1.location = (340.0, 0.0)
			boolean_math_1.location = (340.0, -140.0)
			
			#Set dimensions
			group_output_3.width, group_output_3.height = 140.0, 100.0
			group_input_3.width, group_input_3.height = 140.0, 100.0
			boolean_math_001_1.width, boolean_math_001_1.height = 140.0, 100.0
			group_001.width, group_001.height = 208.33343505859375, 100.0
			group_002.width, group_002.height = 170.44906616210938, 100.0
			boolean_math_002_1.width, boolean_math_002_1.height = 140.0, 100.0
			boolean_math_1.width, boolean_math_1.height = 140.0, 100.0
			
			#initialize is_alpha_carbon links
			#group_input_3.And -> boolean_math_001_1.Boolean
			is_alpha_carbon.links.new(group_input_3.outputs[0], boolean_math_001_1.inputs[0])
			#boolean_math_002_1.Boolean -> group_output_3.Selection
			is_alpha_carbon.links.new(boolean_math_002_1.outputs[0], group_output_3.inputs[0])
			#group_001.Boolean -> boolean_math_001_1.Boolean
			is_alpha_carbon.links.new(group_001.outputs[0], boolean_math_001_1.inputs[1])
			#group_002.Is Alpha Carbon -> group_001.Fallback
			is_alpha_carbon.links.new(group_002.outputs[3], group_001.inputs[1])
			#boolean_math_001_1.Boolean -> boolean_math_002_1.Boolean
			is_alpha_carbon.links.new(boolean_math_001_1.outputs[0], boolean_math_002_1.inputs[0])
			#group_input_3.Or -> boolean_math_002_1.Boolean
			is_alpha_carbon.links.new(group_input_3.outputs[1], boolean_math_002_1.inputs[1])
			#boolean_math_002_1.Boolean -> boolean_math_1.Boolean
			is_alpha_carbon.links.new(boolean_math_002_1.outputs[0], boolean_math_1.inputs[0])
			#boolean_math_1.Boolean -> group_output_3.Inverted
			is_alpha_carbon.links.new(boolean_math_1.outputs[0], group_output_3.inputs[1])
			return is_alpha_carbon

		is_alpha_carbon = is_alpha_carbon_node_group()

		#initialize _mn_constants_atom_name_nucleic node group
		def _mn_constants_atom_name_nucleic_node_group():
			_mn_constants_atom_name_nucleic = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_constants_atom_name_nucleic")

			_mn_constants_atom_name_nucleic.color_tag = 'NONE'
			_mn_constants_atom_name_nucleic.description = ""

			
			#_mn_constants_atom_name_nucleic interface
			#Socket Backbone Lower
			backbone_lower_socket_1 = _mn_constants_atom_name_nucleic.interface.new_socket(name = "Backbone Lower", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			backbone_lower_socket_1.default_value = 0
			backbone_lower_socket_1.min_value = -2147483648
			backbone_lower_socket_1.max_value = 2147483647
			backbone_lower_socket_1.subtype = 'NONE'
			backbone_lower_socket_1.attribute_domain = 'POINT'
			
			#Socket Backbone Upper
			backbone_upper_socket_1 = _mn_constants_atom_name_nucleic.interface.new_socket(name = "Backbone Upper", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			backbone_upper_socket_1.default_value = 0
			backbone_upper_socket_1.min_value = -2147483648
			backbone_upper_socket_1.max_value = 2147483647
			backbone_upper_socket_1.subtype = 'NONE'
			backbone_upper_socket_1.attribute_domain = 'POINT'
			
			#Socket Side Chain Lower
			side_chain_lower_socket_1 = _mn_constants_atom_name_nucleic.interface.new_socket(name = "Side Chain Lower", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			side_chain_lower_socket_1.default_value = 0
			side_chain_lower_socket_1.min_value = -2147483648
			side_chain_lower_socket_1.max_value = 2147483647
			side_chain_lower_socket_1.subtype = 'NONE'
			side_chain_lower_socket_1.attribute_domain = 'POINT'
			
			#Socket Side Chain Upper
			side_chain_upper_socket_1 = _mn_constants_atom_name_nucleic.interface.new_socket(name = "Side Chain Upper", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			side_chain_upper_socket_1.default_value = 0
			side_chain_upper_socket_1.min_value = -2147483648
			side_chain_upper_socket_1.max_value = 2147483647
			side_chain_upper_socket_1.subtype = 'NONE'
			side_chain_upper_socket_1.attribute_domain = 'POINT'
			
			#Socket Side Chain Joint Carbon
			side_chain_joint_carbon_socket = _mn_constants_atom_name_nucleic.interface.new_socket(name = "Side Chain Joint Carbon", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			side_chain_joint_carbon_socket.default_value = 0
			side_chain_joint_carbon_socket.min_value = -2147483648
			side_chain_joint_carbon_socket.max_value = 2147483647
			side_chain_joint_carbon_socket.subtype = 'NONE'
			side_chain_joint_carbon_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_constants_atom_name_nucleic nodes
			#node Group Output
			group_output_4 = _mn_constants_atom_name_nucleic.nodes.new("NodeGroupOutput")
			group_output_4.name = "Group Output"
			group_output_4.is_active_output = True
			
			#node Group Input
			group_input_4 = _mn_constants_atom_name_nucleic.nodes.new("NodeGroupInput")
			group_input_4.name = "Group Input"
			
			#node Integer
			integer_1 = _mn_constants_atom_name_nucleic.nodes.new("FunctionNodeInputInt")
			integer_1.name = "Integer"
			integer_1.integer = 61
			
			#node Integer.002
			integer_002_1 = _mn_constants_atom_name_nucleic.nodes.new("FunctionNodeInputInt")
			integer_002_1.name = "Integer.002"
			integer_002_1.integer = 50
			
			#node Integer.003
			integer_003_1 = _mn_constants_atom_name_nucleic.nodes.new("FunctionNodeInputInt")
			integer_003_1.name = "Integer.003"
			integer_003_1.integer = 61
			
			#node Integer.001
			integer_001_1 = _mn_constants_atom_name_nucleic.nodes.new("FunctionNodeInputInt")
			integer_001_1.name = "Integer.001"
			integer_001_1.integer = 77
			
			#node Integer.004
			integer_004_1 = _mn_constants_atom_name_nucleic.nodes.new("FunctionNodeInputInt")
			integer_004_1.name = "Integer.004"
			integer_004_1.integer = 54
			
			
			
			
			#Set locations
			group_output_4.location = (190.0, 0.0)
			group_input_4.location = (-200.0, 0.0)
			integer_1.location = (0.0, -100.0)
			integer_002_1.location = (0.0, 100.0)
			integer_003_1.location = (0.0, 0.0)
			integer_001_1.location = (0.0, -200.0)
			integer_004_1.location = (0.0, -300.0)
			
			#Set dimensions
			group_output_4.width, group_output_4.height = 140.0, 100.0
			group_input_4.width, group_input_4.height = 140.0, 100.0
			integer_1.width, integer_1.height = 140.0, 100.0
			integer_002_1.width, integer_002_1.height = 140.0, 100.0
			integer_003_1.width, integer_003_1.height = 140.0, 100.0
			integer_001_1.width, integer_001_1.height = 140.0, 100.0
			integer_004_1.width, integer_004_1.height = 140.0, 100.0
			
			#initialize _mn_constants_atom_name_nucleic links
			#integer_1.Integer -> group_output_4.Side Chain Lower
			_mn_constants_atom_name_nucleic.links.new(integer_1.outputs[0], group_output_4.inputs[2])
			#integer_001_1.Integer -> group_output_4.Side Chain Upper
			_mn_constants_atom_name_nucleic.links.new(integer_001_1.outputs[0], group_output_4.inputs[3])
			#integer_002_1.Integer -> group_output_4.Backbone Lower
			_mn_constants_atom_name_nucleic.links.new(integer_002_1.outputs[0], group_output_4.inputs[0])
			#integer_003_1.Integer -> group_output_4.Backbone Upper
			_mn_constants_atom_name_nucleic.links.new(integer_003_1.outputs[0], group_output_4.inputs[1])
			#integer_004_1.Integer -> group_output_4.Side Chain Joint Carbon
			_mn_constants_atom_name_nucleic.links.new(integer_004_1.outputs[0], group_output_4.inputs[4])
			return _mn_constants_atom_name_nucleic

		_mn_constants_atom_name_nucleic = _mn_constants_atom_name_nucleic_node_group()

		#initialize _mn_select_nucleic node group
		def _mn_select_nucleic_node_group():
			_mn_select_nucleic = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_select_nucleic")

			_mn_select_nucleic.color_tag = 'NONE'
			_mn_select_nucleic.description = ""

			
			#_mn_select_nucleic interface
			#Socket Is Backbone
			is_backbone_socket_1 = _mn_select_nucleic.interface.new_socket(name = "Is Backbone", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_backbone_socket_1.default_value = False
			is_backbone_socket_1.attribute_domain = 'POINT'
			is_backbone_socket_1.description = "True for atoms that are part of the sugar-phosphate backbone for the nucleotides"
			
			#Socket Is Side Chain
			is_side_chain_socket_1 = _mn_select_nucleic.interface.new_socket(name = "Is Side Chain", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_side_chain_socket_1.default_value = False
			is_side_chain_socket_1.attribute_domain = 'POINT'
			is_side_chain_socket_1.description = "True for atoms that are part of the bases for nucleotides."
			
			#Socket Is Nucleic
			is_nucleic_socket = _mn_select_nucleic.interface.new_socket(name = "Is Nucleic", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_nucleic_socket.default_value = False
			is_nucleic_socket.attribute_domain = 'POINT'
			is_nucleic_socket.description = "True if the atoms are part of a nucleic acid"
			
			
			#initialize _mn_select_nucleic nodes
			#node Group Input
			group_input_5 = _mn_select_nucleic.nodes.new("NodeGroupInput")
			group_input_5.name = "Group Input"
			
			#node Compare
			compare_1 = _mn_select_nucleic.nodes.new("FunctionNodeCompare")
			compare_1.name = "Compare"
			compare_1.data_type = 'INT'
			compare_1.mode = 'ELEMENT'
			compare_1.operation = 'GREATER_EQUAL'
			
			#node Compare.001
			compare_001_1 = _mn_select_nucleic.nodes.new("FunctionNodeCompare")
			compare_001_1.name = "Compare.001"
			compare_001_1.data_type = 'INT'
			compare_001_1.mode = 'ELEMENT'
			compare_001_1.operation = 'LESS_EQUAL'
			
			#node Boolean Math.001
			boolean_math_001_2 = _mn_select_nucleic.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_2.name = "Boolean Math.001"
			boolean_math_001_2.operation = 'AND'
			
			#node Group Output
			group_output_5 = _mn_select_nucleic.nodes.new("NodeGroupOutput")
			group_output_5.name = "Group Output"
			group_output_5.is_active_output = True
			
			#node Compare.002
			compare_002_1 = _mn_select_nucleic.nodes.new("FunctionNodeCompare")
			compare_002_1.name = "Compare.002"
			compare_002_1.data_type = 'INT'
			compare_002_1.mode = 'ELEMENT'
			compare_002_1.operation = 'GREATER_EQUAL'
			
			#node Compare.003
			compare_003_1 = _mn_select_nucleic.nodes.new("FunctionNodeCompare")
			compare_003_1.name = "Compare.003"
			compare_003_1.data_type = 'INT'
			compare_003_1.mode = 'ELEMENT'
			compare_003_1.operation = 'LESS_EQUAL'
			
			#node Boolean Math.002
			boolean_math_002_2 = _mn_select_nucleic.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_2.name = "Boolean Math.002"
			boolean_math_002_2.operation = 'AND'
			
			#node Compare.004
			compare_004_1 = _mn_select_nucleic.nodes.new("FunctionNodeCompare")
			compare_004_1.name = "Compare.004"
			compare_004_1.data_type = 'INT'
			compare_004_1.mode = 'ELEMENT'
			compare_004_1.operation = 'GREATER_EQUAL'
			
			#node Compare.005
			compare_005_1 = _mn_select_nucleic.nodes.new("FunctionNodeCompare")
			compare_005_1.name = "Compare.005"
			compare_005_1.data_type = 'INT'
			compare_005_1.mode = 'ELEMENT'
			compare_005_1.operation = 'LESS_EQUAL'
			
			#node Boolean Math.003
			boolean_math_003_1 = _mn_select_nucleic.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003_1.name = "Boolean Math.003"
			boolean_math_003_1.operation = 'AND'
			
			#node Named Attribute
			named_attribute_2 = _mn_select_nucleic.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_2.name = "Named Attribute"
			named_attribute_2.data_type = 'INT'
			#Name
			named_attribute_2.inputs[0].default_value = "atom_name"
			
			#node Group
			group_1 = _mn_select_nucleic.nodes.new("GeometryNodeGroup")
			group_1.name = "Group"
			group_1.node_tree = _mn_constants_atom_name_nucleic
			
			
			
			
			#Set locations
			group_input_5.location = (-460.0, 0.0)
			compare_1.location = (80.0, 80.0)
			compare_001_1.location = (80.0, -80.0)
			boolean_math_001_2.location = (260.0, 80.0)
			group_output_5.location = (580.0, 60.0)
			compare_002_1.location = (80.0, -260.0)
			compare_003_1.location = (80.0, -420.0)
			boolean_math_002_2.location = (260.0, -260.0)
			compare_004_1.location = (80.0, -580.0)
			compare_005_1.location = (80.0, -740.0)
			boolean_math_003_1.location = (260.0, -580.0)
			named_attribute_2.location = (-260.0, -280.0)
			group_1.location = (-480.0, -100.0)
			
			#Set dimensions
			group_input_5.width, group_input_5.height = 140.0, 100.0
			compare_1.width, compare_1.height = 140.0, 100.0
			compare_001_1.width, compare_001_1.height = 140.0, 100.0
			boolean_math_001_2.width, boolean_math_001_2.height = 140.0, 100.0
			group_output_5.width, group_output_5.height = 140.0, 100.0
			compare_002_1.width, compare_002_1.height = 140.0, 100.0
			compare_003_1.width, compare_003_1.height = 140.0, 100.0
			boolean_math_002_2.width, boolean_math_002_2.height = 140.0, 100.0
			compare_004_1.width, compare_004_1.height = 140.0, 100.0
			compare_005_1.width, compare_005_1.height = 140.0, 100.0
			boolean_math_003_1.width, boolean_math_003_1.height = 140.0, 100.0
			named_attribute_2.width, named_attribute_2.height = 140.0, 100.0
			group_1.width, group_1.height = 365.8858337402344, 100.0
			
			#initialize _mn_select_nucleic links
			#compare_001_1.Result -> boolean_math_001_2.Boolean
			_mn_select_nucleic.links.new(compare_001_1.outputs[0], boolean_math_001_2.inputs[1])
			#named_attribute_2.Attribute -> compare_1.A
			_mn_select_nucleic.links.new(named_attribute_2.outputs[0], compare_1.inputs[2])
			#compare_1.Result -> boolean_math_001_2.Boolean
			_mn_select_nucleic.links.new(compare_1.outputs[0], boolean_math_001_2.inputs[0])
			#named_attribute_2.Attribute -> compare_001_1.A
			_mn_select_nucleic.links.new(named_attribute_2.outputs[0], compare_001_1.inputs[2])
			#boolean_math_001_2.Boolean -> group_output_5.Is Backbone
			_mn_select_nucleic.links.new(boolean_math_001_2.outputs[0], group_output_5.inputs[0])
			#group_1.Backbone Lower -> compare_1.B
			_mn_select_nucleic.links.new(group_1.outputs[0], compare_1.inputs[3])
			#group_1.Backbone Upper -> compare_001_1.B
			_mn_select_nucleic.links.new(group_1.outputs[1], compare_001_1.inputs[3])
			#compare_003_1.Result -> boolean_math_002_2.Boolean
			_mn_select_nucleic.links.new(compare_003_1.outputs[0], boolean_math_002_2.inputs[1])
			#compare_002_1.Result -> boolean_math_002_2.Boolean
			_mn_select_nucleic.links.new(compare_002_1.outputs[0], boolean_math_002_2.inputs[0])
			#group_1.Side Chain Lower -> compare_002_1.B
			_mn_select_nucleic.links.new(group_1.outputs[2], compare_002_1.inputs[3])
			#group_1.Side Chain Upper -> compare_003_1.B
			_mn_select_nucleic.links.new(group_1.outputs[3], compare_003_1.inputs[3])
			#boolean_math_002_2.Boolean -> group_output_5.Is Side Chain
			_mn_select_nucleic.links.new(boolean_math_002_2.outputs[0], group_output_5.inputs[1])
			#named_attribute_2.Attribute -> compare_002_1.A
			_mn_select_nucleic.links.new(named_attribute_2.outputs[0], compare_002_1.inputs[2])
			#named_attribute_2.Attribute -> compare_003_1.A
			_mn_select_nucleic.links.new(named_attribute_2.outputs[0], compare_003_1.inputs[2])
			#compare_005_1.Result -> boolean_math_003_1.Boolean
			_mn_select_nucleic.links.new(compare_005_1.outputs[0], boolean_math_003_1.inputs[1])
			#compare_004_1.Result -> boolean_math_003_1.Boolean
			_mn_select_nucleic.links.new(compare_004_1.outputs[0], boolean_math_003_1.inputs[0])
			#group_1.Backbone Lower -> compare_004_1.B
			_mn_select_nucleic.links.new(group_1.outputs[0], compare_004_1.inputs[3])
			#named_attribute_2.Attribute -> compare_004_1.A
			_mn_select_nucleic.links.new(named_attribute_2.outputs[0], compare_004_1.inputs[2])
			#group_1.Side Chain Upper -> compare_005_1.B
			_mn_select_nucleic.links.new(group_1.outputs[3], compare_005_1.inputs[3])
			#named_attribute_2.Attribute -> compare_005_1.A
			_mn_select_nucleic.links.new(named_attribute_2.outputs[0], compare_005_1.inputs[2])
			#boolean_math_003_1.Boolean -> group_output_5.Is Nucleic
			_mn_select_nucleic.links.new(boolean_math_003_1.outputs[0], group_output_5.inputs[2])
			return _mn_select_nucleic

		_mn_select_nucleic = _mn_select_nucleic_node_group()

		#initialize is_side_chain node group
		def is_side_chain_node_group():
			is_side_chain = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Is Side Chain")

			is_side_chain.color_tag = 'INPUT'
			is_side_chain.description = ""

			
			#is_side_chain interface
			#Socket Selection
			selection_socket_1 = is_side_chain.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket_1.default_value = False
			selection_socket_1.attribute_domain = 'POINT'
			selection_socket_1.description = "True if atom is part of the side chain for either an amino acid or a nucleic acid"
			
			#Socket Inverted
			inverted_socket_1 = is_side_chain.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket_1.default_value = False
			inverted_socket_1.attribute_domain = 'POINT'
			
			#Socket And
			and_socket_1 = is_side_chain.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket_1.default_value = True
			and_socket_1.attribute_domain = 'POINT'
			and_socket_1.hide_value = True
			
			#Socket Or
			or_socket_1 = is_side_chain.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket_1.default_value = False
			or_socket_1.attribute_domain = 'POINT'
			or_socket_1.hide_value = True
			
			
			#initialize is_side_chain nodes
			#node Boolean Math.001
			boolean_math_001_3 = is_side_chain.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_3.name = "Boolean Math.001"
			boolean_math_001_3.operation = 'OR'
			
			#node Group Input
			group_input_6 = is_side_chain.nodes.new("NodeGroupInput")
			group_input_6.name = "Group Input"
			
			#node Boolean Math
			boolean_math_2 = is_side_chain.nodes.new("FunctionNodeBooleanMath")
			boolean_math_2.name = "Boolean Math"
			boolean_math_2.operation = 'AND'
			
			#node Group Output
			group_output_6 = is_side_chain.nodes.new("NodeGroupOutput")
			group_output_6.name = "Group Output"
			group_output_6.is_active_output = True
			
			#node Group.001
			group_001_1 = is_side_chain.nodes.new("GeometryNodeGroup")
			group_001_1.name = "Group.001"
			group_001_1.node_tree = _mn_select_nucleic
			
			#node Group.002
			group_002_1 = is_side_chain.nodes.new("GeometryNodeGroup")
			group_002_1.name = "Group.002"
			group_002_1.node_tree = _mn_select_peptide
			
			#node Group
			group_2 = is_side_chain.nodes.new("GeometryNodeGroup")
			group_2.name = "Group"
			group_2.node_tree = fallback_boolean
			#Socket_2
			group_2.inputs[0].default_value = "is_side_chain"
			
			#node Boolean Math.002
			boolean_math_002_3 = is_side_chain.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_3.name = "Boolean Math.002"
			boolean_math_002_3.operation = 'OR'
			
			#node Boolean Math.003
			boolean_math_003_2 = is_side_chain.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003_2.name = "Boolean Math.003"
			boolean_math_003_2.operation = 'NOT'
			
			
			
			
			#Set locations
			boolean_math_001_3.location = (-460.0, -80.0)
			group_input_6.location = (-280.0, 20.0)
			boolean_math_2.location = (-120.0, 20.0)
			group_output_6.location = (240.00001525878906, 20.0)
			group_001_1.location = (-740.0, -80.0)
			group_002_1.location = (-740.0, -220.0)
			group_2.location = (-300.0, -80.0)
			boolean_math_002_3.location = (59.99999237060547, 20.0)
			boolean_math_003_2.location = (60.0, -120.0)
			
			#Set dimensions
			boolean_math_001_3.width, boolean_math_001_3.height = 140.0, 100.0
			group_input_6.width, group_input_6.height = 140.0, 100.0
			boolean_math_2.width, boolean_math_2.height = 140.0, 100.0
			group_output_6.width, group_output_6.height = 140.0, 100.0
			group_001_1.width, group_001_1.height = 244.02914428710938, 100.0
			group_002_1.width, group_002_1.height = 244.02914428710938, 100.0
			group_2.width, group_2.height = 140.0, 100.0
			boolean_math_002_3.width, boolean_math_002_3.height = 140.0, 100.0
			boolean_math_003_2.width, boolean_math_003_2.height = 140.0, 100.0
			
			#initialize is_side_chain links
			#group_input_6.And -> boolean_math_2.Boolean
			is_side_chain.links.new(group_input_6.outputs[0], boolean_math_2.inputs[0])
			#group_001_1.Is Side Chain -> boolean_math_001_3.Boolean
			is_side_chain.links.new(group_001_1.outputs[1], boolean_math_001_3.inputs[0])
			#group_002_1.Is Side Chain -> boolean_math_001_3.Boolean
			is_side_chain.links.new(group_002_1.outputs[1], boolean_math_001_3.inputs[1])
			#boolean_math_001_3.Boolean -> group_2.Fallback
			is_side_chain.links.new(boolean_math_001_3.outputs[0], group_2.inputs[1])
			#group_2.Boolean -> boolean_math_2.Boolean
			is_side_chain.links.new(group_2.outputs[0], boolean_math_2.inputs[1])
			#boolean_math_002_3.Boolean -> group_output_6.Selection
			is_side_chain.links.new(boolean_math_002_3.outputs[0], group_output_6.inputs[0])
			#boolean_math_2.Boolean -> boolean_math_002_3.Boolean
			is_side_chain.links.new(boolean_math_2.outputs[0], boolean_math_002_3.inputs[0])
			#group_input_6.Or -> boolean_math_002_3.Boolean
			is_side_chain.links.new(group_input_6.outputs[1], boolean_math_002_3.inputs[1])
			#boolean_math_002_3.Boolean -> boolean_math_003_2.Boolean
			is_side_chain.links.new(boolean_math_002_3.outputs[0], boolean_math_003_2.inputs[0])
			#boolean_math_003_2.Boolean -> group_output_6.Inverted
			is_side_chain.links.new(boolean_math_003_2.outputs[0], group_output_6.inputs[1])
			return is_side_chain

		is_side_chain = is_side_chain_node_group()

		#initialize is_backbone node group
		def is_backbone_node_group():
			is_backbone = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Is Backbone")

			is_backbone.color_tag = 'INPUT'
			is_backbone.description = ""

			
			#is_backbone interface
			#Socket Selection
			selection_socket_2 = is_backbone.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket_2.default_value = False
			selection_socket_2.attribute_domain = 'POINT'
			selection_socket_2.description = "True if the atom is part of the backbone for either an amino acid or a peptide chain"
			
			#Socket Inverted
			inverted_socket_2 = is_backbone.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket_2.default_value = False
			inverted_socket_2.attribute_domain = 'POINT'
			
			#Socket And
			and_socket_2 = is_backbone.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket_2.default_value = True
			and_socket_2.attribute_domain = 'POINT'
			and_socket_2.hide_value = True
			
			#Socket Or
			or_socket_2 = is_backbone.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket_2.default_value = False
			or_socket_2.attribute_domain = 'POINT'
			or_socket_2.hide_value = True
			
			
			#initialize is_backbone nodes
			#node Group Input
			group_input_7 = is_backbone.nodes.new("NodeGroupInput")
			group_input_7.name = "Group Input"
			
			#node Boolean Math
			boolean_math_3 = is_backbone.nodes.new("FunctionNodeBooleanMath")
			boolean_math_3.name = "Boolean Math"
			boolean_math_3.operation = 'AND'
			
			#node Group Output
			group_output_7 = is_backbone.nodes.new("NodeGroupOutput")
			group_output_7.name = "Group Output"
			group_output_7.is_active_output = True
			
			#node Boolean Math.001
			boolean_math_001_4 = is_backbone.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_4.name = "Boolean Math.001"
			boolean_math_001_4.operation = 'OR'
			
			#node Group.001
			group_001_2 = is_backbone.nodes.new("GeometryNodeGroup")
			group_001_2.name = "Group.001"
			group_001_2.node_tree = _mn_select_nucleic
			
			#node Group.002
			group_002_2 = is_backbone.nodes.new("GeometryNodeGroup")
			group_002_2.name = "Group.002"
			group_002_2.node_tree = _mn_select_peptide
			
			#node Group
			group_3 = is_backbone.nodes.new("GeometryNodeGroup")
			group_3.name = "Group"
			group_3.node_tree = fallback_boolean
			#Socket_2
			group_3.inputs[0].default_value = "is_backbone"
			
			#node Boolean Math.002
			boolean_math_002_4 = is_backbone.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_4.name = "Boolean Math.002"
			boolean_math_002_4.operation = 'OR'
			
			#node Boolean Math.003
			boolean_math_003_3 = is_backbone.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003_3.name = "Boolean Math.003"
			boolean_math_003_3.operation = 'NOT'
			
			
			
			
			#Set locations
			group_input_7.location = (-240.0, 20.0)
			boolean_math_3.location = (-60.0, 20.0)
			group_output_7.location = (300.0000305175781, 20.0)
			boolean_math_001_4.location = (-400.0, -80.0)
			group_001_2.location = (-680.0, -80.0)
			group_002_2.location = (-680.0, -220.0)
			group_3.location = (-240.0, -80.0)
			boolean_math_002_4.location = (120.0, 22.075050354003906)
			boolean_math_003_3.location = (120.0, -120.0)
			
			#Set dimensions
			group_input_7.width, group_input_7.height = 140.0, 100.0
			boolean_math_3.width, boolean_math_3.height = 140.0, 100.0
			group_output_7.width, group_output_7.height = 140.0, 100.0
			boolean_math_001_4.width, boolean_math_001_4.height = 140.0, 100.0
			group_001_2.width, group_001_2.height = 244.02914428710938, 100.0
			group_002_2.width, group_002_2.height = 244.02914428710938, 100.0
			group_3.width, group_3.height = 140.0, 100.0
			boolean_math_002_4.width, boolean_math_002_4.height = 140.0, 100.0
			boolean_math_003_3.width, boolean_math_003_3.height = 140.0, 100.0
			
			#initialize is_backbone links
			#group_input_7.And -> boolean_math_3.Boolean
			is_backbone.links.new(group_input_7.outputs[0], boolean_math_3.inputs[0])
			#boolean_math_002_4.Boolean -> group_output_7.Selection
			is_backbone.links.new(boolean_math_002_4.outputs[0], group_output_7.inputs[0])
			#group_001_2.Is Backbone -> boolean_math_001_4.Boolean
			is_backbone.links.new(group_001_2.outputs[0], boolean_math_001_4.inputs[0])
			#group_002_2.Is Backbone -> boolean_math_001_4.Boolean
			is_backbone.links.new(group_002_2.outputs[0], boolean_math_001_4.inputs[1])
			#boolean_math_001_4.Boolean -> group_3.Fallback
			is_backbone.links.new(boolean_math_001_4.outputs[0], group_3.inputs[1])
			#group_3.Boolean -> boolean_math_3.Boolean
			is_backbone.links.new(group_3.outputs[0], boolean_math_3.inputs[1])
			#boolean_math_3.Boolean -> boolean_math_002_4.Boolean
			is_backbone.links.new(boolean_math_3.outputs[0], boolean_math_002_4.inputs[0])
			#group_input_7.Or -> boolean_math_002_4.Boolean
			is_backbone.links.new(group_input_7.outputs[1], boolean_math_002_4.inputs[1])
			#boolean_math_002_4.Boolean -> boolean_math_003_3.Boolean
			is_backbone.links.new(boolean_math_002_4.outputs[0], boolean_math_003_3.inputs[0])
			#boolean_math_003_3.Boolean -> group_output_7.Inverted
			is_backbone.links.new(boolean_math_003_3.outputs[0], group_output_7.inputs[1])
			return is_backbone

		is_backbone = is_backbone_node_group()

		#initialize color_backbone node group
		def color_backbone_node_group():
			color_backbone = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Color Backbone")

			color_backbone.color_tag = 'COLOR'
			color_backbone.description = ""

			
			#color_backbone interface
			#Socket Color
			color_socket = color_backbone.interface.new_socket(name = "Color", in_out='OUTPUT', socket_type = 'NodeSocketColor')
			color_socket.default_value = (0.0, 0.0, 0.0, 0.0)
			color_socket.attribute_domain = 'POINT'
			
			#Socket Backbone
			backbone_socket = color_backbone.interface.new_socket(name = "Backbone", in_out='INPUT', socket_type = 'NodeSocketColor')
			backbone_socket.default_value = (0.4694809913635254, 0.23999999463558197, 0.6000000238418579, 1.0)
			backbone_socket.attribute_domain = 'POINT'
			
			#Socket Side Chain
			side_chain_socket = color_backbone.interface.new_socket(name = "Side Chain", in_out='INPUT', socket_type = 'NodeSocketColor')
			side_chain_socket.default_value = (0.5255190134048462, 0.6000000238418579, 0.23999999463558197, 1.0)
			side_chain_socket.attribute_domain = 'POINT'
			
			
			#initialize color_backbone nodes
			#node Group Output
			group_output_8 = color_backbone.nodes.new("NodeGroupOutput")
			group_output_8.name = "Group Output"
			group_output_8.is_active_output = True
			
			#node Boolean Math
			boolean_math_4 = color_backbone.nodes.new("FunctionNodeBooleanMath")
			boolean_math_4.name = "Boolean Math"
			boolean_math_4.operation = 'NOT'
			
			#node Boolean Math.001
			boolean_math_001_5 = color_backbone.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_5.name = "Boolean Math.001"
			boolean_math_001_5.operation = 'AND'
			
			#node Named Attribute
			named_attribute_3 = color_backbone.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_3.name = "Named Attribute"
			named_attribute_3.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute_3.inputs[0].default_value = "Color"
			
			#node Group Input
			group_input_8 = color_backbone.nodes.new("NodeGroupInput")
			group_input_8.name = "Group Input"
			
			#node Switch
			switch_1 = color_backbone.nodes.new("GeometryNodeSwitch")
			switch_1.name = "Switch"
			switch_1.input_type = 'RGBA'
			
			#node Switch.001
			switch_001 = color_backbone.nodes.new("GeometryNodeSwitch")
			switch_001.name = "Switch.001"
			switch_001.input_type = 'RGBA'
			
			#node MN Select Alpha Carbon
			mn_select_alpha_carbon = color_backbone.nodes.new("GeometryNodeGroup")
			mn_select_alpha_carbon.label = " Select Alpha Carbon"
			mn_select_alpha_carbon.name = "MN Select Alpha Carbon"
			mn_select_alpha_carbon.node_tree = is_alpha_carbon
			#Socket_1
			mn_select_alpha_carbon.inputs[0].default_value = True
			#Socket_3
			mn_select_alpha_carbon.inputs[1].default_value = False
			
			#node MN Select Side Chain
			mn_select_side_chain = color_backbone.nodes.new("GeometryNodeGroup")
			mn_select_side_chain.label = " Select Side Chain"
			mn_select_side_chain.name = "MN Select Side Chain"
			mn_select_side_chain.node_tree = is_side_chain
			#Socket_1
			mn_select_side_chain.inputs[0].default_value = True
			#Socket_3
			mn_select_side_chain.inputs[1].default_value = False
			
			#node MN Select Backbone
			mn_select_backbone = color_backbone.nodes.new("GeometryNodeGroup")
			mn_select_backbone.label = " Select Backbone"
			mn_select_backbone.name = "MN Select Backbone"
			mn_select_backbone.node_tree = is_backbone
			#Socket_1
			mn_select_backbone.inputs[0].default_value = True
			#Socket_3
			mn_select_backbone.inputs[1].default_value = False
			
			#node Reroute
			reroute = color_backbone.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			
			
			
			#Set locations
			group_output_8.location = (260.0, 20.0)
			boolean_math_4.location = (-440.0, 20.0)
			boolean_math_001_5.location = (-280.0, 20.0)
			named_attribute_3.location = (-280.0, -240.0)
			group_input_8.location = (-280.0, -380.0)
			switch_1.location = (-100.0, -180.0)
			switch_001.location = (100.0, 20.0)
			mn_select_alpha_carbon.location = (-603.0540161132812, 20.0)
			mn_select_side_chain.location = (-440.0, -100.0)
			mn_select_backbone.location = (-279.925048828125, -120.0)
			reroute.location = (80.0, -380.0)
			
			#Set dimensions
			group_output_8.width, group_output_8.height = 140.0, 100.0
			boolean_math_4.width, boolean_math_4.height = 140.0, 100.0
			boolean_math_001_5.width, boolean_math_001_5.height = 140.0, 100.0
			named_attribute_3.width, named_attribute_3.height = 140.0, 100.0
			group_input_8.width, group_input_8.height = 140.0, 100.0
			switch_1.width, switch_1.height = 140.0, 100.0
			switch_001.width, switch_001.height = 140.0, 100.0
			mn_select_alpha_carbon.width, mn_select_alpha_carbon.height = 143.05401611328125, 100.0
			mn_select_side_chain.width, mn_select_side_chain.height = 144.931396484375, 100.0
			mn_select_backbone.width, mn_select_backbone.height = 139.925048828125, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			
			#initialize color_backbone links
			#group_input_8.Backbone -> switch_1.True
			color_backbone.links.new(group_input_8.outputs[0], switch_1.inputs[2])
			#switch_001.Output -> group_output_8.Color
			color_backbone.links.new(switch_001.outputs[0], group_output_8.inputs[0])
			#switch_1.Output -> switch_001.False
			color_backbone.links.new(switch_1.outputs[0], switch_001.inputs[1])
			#reroute.Output -> switch_001.True
			color_backbone.links.new(reroute.outputs[0], switch_001.inputs[2])
			#boolean_math_4.Boolean -> boolean_math_001_5.Boolean
			color_backbone.links.new(boolean_math_4.outputs[0], boolean_math_001_5.inputs[0])
			#boolean_math_001_5.Boolean -> switch_001.Switch
			color_backbone.links.new(boolean_math_001_5.outputs[0], switch_001.inputs[0])
			#named_attribute_3.Attribute -> switch_1.False
			color_backbone.links.new(named_attribute_3.outputs[0], switch_1.inputs[1])
			#mn_select_alpha_carbon.Selection -> boolean_math_4.Boolean
			color_backbone.links.new(mn_select_alpha_carbon.outputs[0], boolean_math_4.inputs[0])
			#mn_select_side_chain.Selection -> boolean_math_001_5.Boolean
			color_backbone.links.new(mn_select_side_chain.outputs[0], boolean_math_001_5.inputs[1])
			#mn_select_backbone.Selection -> switch_1.Switch
			color_backbone.links.new(mn_select_backbone.outputs[0], switch_1.inputs[0])
			#group_input_8.Side Chain -> reroute.Input
			color_backbone.links.new(group_input_8.outputs[1], reroute.inputs[0])
			return color_backbone

		color_backbone = color_backbone_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Color Backbone", type = 'NODES')
		mod.node_group = color_backbone
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Color_Backbone.bl_idname)
			
def register():
	bpy.utils.register_class(Color_Backbone)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Color_Backbone)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
