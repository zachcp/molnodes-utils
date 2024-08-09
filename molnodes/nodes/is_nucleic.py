bl_info = {
	"name" : "Is Nucleic",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Is_Nucleic(bpy.types.Operator):
	bl_idname = "node.is_nucleic"
	bl_label = "Is Nucleic"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _mn_constants_atom_name_nucleic node group
		def _mn_constants_atom_name_nucleic_node_group():
			_mn_constants_atom_name_nucleic = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_constants_atom_name_nucleic")

			_mn_constants_atom_name_nucleic.color_tag = 'NONE'
			_mn_constants_atom_name_nucleic.description = ""

			
			#_mn_constants_atom_name_nucleic interface
			#Socket Backbone Lower
			backbone_lower_socket = _mn_constants_atom_name_nucleic.interface.new_socket(name = "Backbone Lower", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			backbone_lower_socket.subtype = 'NONE'
			backbone_lower_socket.default_value = 0
			backbone_lower_socket.min_value = -2147483648
			backbone_lower_socket.max_value = 2147483647
			backbone_lower_socket.attribute_domain = 'POINT'
			
			#Socket Backbone Upper
			backbone_upper_socket = _mn_constants_atom_name_nucleic.interface.new_socket(name = "Backbone Upper", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			backbone_upper_socket.subtype = 'NONE'
			backbone_upper_socket.default_value = 0
			backbone_upper_socket.min_value = -2147483648
			backbone_upper_socket.max_value = 2147483647
			backbone_upper_socket.attribute_domain = 'POINT'
			
			#Socket Side Chain Lower
			side_chain_lower_socket = _mn_constants_atom_name_nucleic.interface.new_socket(name = "Side Chain Lower", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			side_chain_lower_socket.subtype = 'NONE'
			side_chain_lower_socket.default_value = 0
			side_chain_lower_socket.min_value = -2147483648
			side_chain_lower_socket.max_value = 2147483647
			side_chain_lower_socket.attribute_domain = 'POINT'
			
			#Socket Side Chain Upper
			side_chain_upper_socket = _mn_constants_atom_name_nucleic.interface.new_socket(name = "Side Chain Upper", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			side_chain_upper_socket.subtype = 'NONE'
			side_chain_upper_socket.default_value = 0
			side_chain_upper_socket.min_value = -2147483648
			side_chain_upper_socket.max_value = 2147483647
			side_chain_upper_socket.attribute_domain = 'POINT'
			
			#Socket Side Chain Joint Carbon
			side_chain_joint_carbon_socket = _mn_constants_atom_name_nucleic.interface.new_socket(name = "Side Chain Joint Carbon", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			side_chain_joint_carbon_socket.subtype = 'NONE'
			side_chain_joint_carbon_socket.default_value = 0
			side_chain_joint_carbon_socket.min_value = -2147483648
			side_chain_joint_carbon_socket.max_value = 2147483647
			side_chain_joint_carbon_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_constants_atom_name_nucleic nodes
			#node Group Output
			group_output = _mn_constants_atom_name_nucleic.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = _mn_constants_atom_name_nucleic.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Integer
			integer = _mn_constants_atom_name_nucleic.nodes.new("FunctionNodeInputInt")
			integer.name = "Integer"
			integer.integer = 61
			
			#node Integer.002
			integer_002 = _mn_constants_atom_name_nucleic.nodes.new("FunctionNodeInputInt")
			integer_002.name = "Integer.002"
			integer_002.integer = 50
			
			#node Integer.003
			integer_003 = _mn_constants_atom_name_nucleic.nodes.new("FunctionNodeInputInt")
			integer_003.name = "Integer.003"
			integer_003.integer = 61
			
			#node Integer.001
			integer_001 = _mn_constants_atom_name_nucleic.nodes.new("FunctionNodeInputInt")
			integer_001.name = "Integer.001"
			integer_001.integer = 77
			
			#node Integer.004
			integer_004 = _mn_constants_atom_name_nucleic.nodes.new("FunctionNodeInputInt")
			integer_004.name = "Integer.004"
			integer_004.integer = 54
			
			
			
			
			#Set locations
			group_output.location = (190.0, 0.0)
			group_input.location = (-200.0, 0.0)
			integer.location = (0.0, -100.0)
			integer_002.location = (0.0, 100.0)
			integer_003.location = (0.0, 0.0)
			integer_001.location = (0.0, -200.0)
			integer_004.location = (0.0, -300.0)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			integer.width, integer.height = 140.0, 100.0
			integer_002.width, integer_002.height = 140.0, 100.0
			integer_003.width, integer_003.height = 140.0, 100.0
			integer_001.width, integer_001.height = 140.0, 100.0
			integer_004.width, integer_004.height = 140.0, 100.0
			
			#initialize _mn_constants_atom_name_nucleic links
			#integer.Integer -> group_output.Side Chain Lower
			_mn_constants_atom_name_nucleic.links.new(integer.outputs[0], group_output.inputs[2])
			#integer_001.Integer -> group_output.Side Chain Upper
			_mn_constants_atom_name_nucleic.links.new(integer_001.outputs[0], group_output.inputs[3])
			#integer_002.Integer -> group_output.Backbone Lower
			_mn_constants_atom_name_nucleic.links.new(integer_002.outputs[0], group_output.inputs[0])
			#integer_003.Integer -> group_output.Backbone Upper
			_mn_constants_atom_name_nucleic.links.new(integer_003.outputs[0], group_output.inputs[1])
			#integer_004.Integer -> group_output.Side Chain Joint Carbon
			_mn_constants_atom_name_nucleic.links.new(integer_004.outputs[0], group_output.inputs[4])
			return _mn_constants_atom_name_nucleic

		_mn_constants_atom_name_nucleic = _mn_constants_atom_name_nucleic_node_group()

		#initialize _mn_select_nucleic node group
		def _mn_select_nucleic_node_group():
			_mn_select_nucleic = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_select_nucleic")

			_mn_select_nucleic.color_tag = 'NONE'
			_mn_select_nucleic.description = ""

			
			#_mn_select_nucleic interface
			#Socket Is Backbone
			is_backbone_socket = _mn_select_nucleic.interface.new_socket(name = "Is Backbone", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_backbone_socket.attribute_domain = 'POINT'
			is_backbone_socket.description = "True for atoms that are part of the sugar-phosphate backbone for the nucleotides"
			
			#Socket Is Side Chain
			is_side_chain_socket = _mn_select_nucleic.interface.new_socket(name = "Is Side Chain", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_side_chain_socket.attribute_domain = 'POINT'
			is_side_chain_socket.description = "True for atoms that are part of the bases for nucleotides."
			
			#Socket Is Nucleic
			is_nucleic_socket = _mn_select_nucleic.interface.new_socket(name = "Is Nucleic", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_nucleic_socket.attribute_domain = 'POINT'
			is_nucleic_socket.description = "True if the atoms are part of a nucleic acid"
			
			
			#initialize _mn_select_nucleic nodes
			#node Group Input
			group_input_1 = _mn_select_nucleic.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			
			#node Compare
			compare = _mn_select_nucleic.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'GREATER_EQUAL'
			
			#node Compare.001
			compare_001 = _mn_select_nucleic.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'INT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'LESS_EQUAL'
			
			#node Boolean Math.001
			boolean_math_001 = _mn_select_nucleic.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001.name = "Boolean Math.001"
			boolean_math_001.operation = 'AND'
			
			#node Group Output
			group_output_1 = _mn_select_nucleic.nodes.new("NodeGroupOutput")
			group_output_1.name = "Group Output"
			group_output_1.is_active_output = True
			
			#node Compare.002
			compare_002 = _mn_select_nucleic.nodes.new("FunctionNodeCompare")
			compare_002.name = "Compare.002"
			compare_002.data_type = 'INT'
			compare_002.mode = 'ELEMENT'
			compare_002.operation = 'GREATER_EQUAL'
			
			#node Compare.003
			compare_003 = _mn_select_nucleic.nodes.new("FunctionNodeCompare")
			compare_003.name = "Compare.003"
			compare_003.data_type = 'INT'
			compare_003.mode = 'ELEMENT'
			compare_003.operation = 'LESS_EQUAL'
			
			#node Boolean Math.002
			boolean_math_002 = _mn_select_nucleic.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002.name = "Boolean Math.002"
			boolean_math_002.operation = 'AND'
			
			#node Compare.004
			compare_004 = _mn_select_nucleic.nodes.new("FunctionNodeCompare")
			compare_004.name = "Compare.004"
			compare_004.data_type = 'INT'
			compare_004.mode = 'ELEMENT'
			compare_004.operation = 'GREATER_EQUAL'
			
			#node Compare.005
			compare_005 = _mn_select_nucleic.nodes.new("FunctionNodeCompare")
			compare_005.name = "Compare.005"
			compare_005.data_type = 'INT'
			compare_005.mode = 'ELEMENT'
			compare_005.operation = 'LESS_EQUAL'
			
			#node Boolean Math.003
			boolean_math_003 = _mn_select_nucleic.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003.name = "Boolean Math.003"
			boolean_math_003.operation = 'AND'
			
			#node Named Attribute
			named_attribute = _mn_select_nucleic.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'INT'
			#Name
			named_attribute.inputs[0].default_value = "atom_name"
			
			#node Group
			group = _mn_select_nucleic.nodes.new("GeometryNodeGroup")
			group.name = "Group"
			group.node_tree = _mn_constants_atom_name_nucleic
			
			
			
			
			#Set locations
			group_input_1.location = (-460.0, 0.0)
			compare.location = (80.0, 80.0)
			compare_001.location = (80.0, -80.0)
			boolean_math_001.location = (260.0, 80.0)
			group_output_1.location = (580.0, 60.0)
			compare_002.location = (80.0, -260.0)
			compare_003.location = (80.0, -420.0)
			boolean_math_002.location = (260.0, -260.0)
			compare_004.location = (80.0, -580.0)
			compare_005.location = (80.0, -740.0)
			boolean_math_003.location = (260.0, -580.0)
			named_attribute.location = (-260.0, -280.0)
			group.location = (-480.0, -100.0)
			
			#Set dimensions
			group_input_1.width, group_input_1.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
			group_output_1.width, group_output_1.height = 140.0, 100.0
			compare_002.width, compare_002.height = 140.0, 100.0
			compare_003.width, compare_003.height = 140.0, 100.0
			boolean_math_002.width, boolean_math_002.height = 140.0, 100.0
			compare_004.width, compare_004.height = 140.0, 100.0
			compare_005.width, compare_005.height = 140.0, 100.0
			boolean_math_003.width, boolean_math_003.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			group.width, group.height = 365.8858337402344, 100.0
			
			#initialize _mn_select_nucleic links
			#compare_001.Result -> boolean_math_001.Boolean
			_mn_select_nucleic.links.new(compare_001.outputs[0], boolean_math_001.inputs[1])
			#named_attribute.Attribute -> compare.A
			_mn_select_nucleic.links.new(named_attribute.outputs[0], compare.inputs[2])
			#compare.Result -> boolean_math_001.Boolean
			_mn_select_nucleic.links.new(compare.outputs[0], boolean_math_001.inputs[0])
			#named_attribute.Attribute -> compare_001.A
			_mn_select_nucleic.links.new(named_attribute.outputs[0], compare_001.inputs[2])
			#boolean_math_001.Boolean -> group_output_1.Is Backbone
			_mn_select_nucleic.links.new(boolean_math_001.outputs[0], group_output_1.inputs[0])
			#group.Backbone Lower -> compare.B
			_mn_select_nucleic.links.new(group.outputs[0], compare.inputs[3])
			#group.Backbone Upper -> compare_001.B
			_mn_select_nucleic.links.new(group.outputs[1], compare_001.inputs[3])
			#compare_003.Result -> boolean_math_002.Boolean
			_mn_select_nucleic.links.new(compare_003.outputs[0], boolean_math_002.inputs[1])
			#compare_002.Result -> boolean_math_002.Boolean
			_mn_select_nucleic.links.new(compare_002.outputs[0], boolean_math_002.inputs[0])
			#group.Side Chain Lower -> compare_002.B
			_mn_select_nucleic.links.new(group.outputs[2], compare_002.inputs[3])
			#group.Side Chain Upper -> compare_003.B
			_mn_select_nucleic.links.new(group.outputs[3], compare_003.inputs[3])
			#boolean_math_002.Boolean -> group_output_1.Is Side Chain
			_mn_select_nucleic.links.new(boolean_math_002.outputs[0], group_output_1.inputs[1])
			#named_attribute.Attribute -> compare_002.A
			_mn_select_nucleic.links.new(named_attribute.outputs[0], compare_002.inputs[2])
			#named_attribute.Attribute -> compare_003.A
			_mn_select_nucleic.links.new(named_attribute.outputs[0], compare_003.inputs[2])
			#compare_005.Result -> boolean_math_003.Boolean
			_mn_select_nucleic.links.new(compare_005.outputs[0], boolean_math_003.inputs[1])
			#compare_004.Result -> boolean_math_003.Boolean
			_mn_select_nucleic.links.new(compare_004.outputs[0], boolean_math_003.inputs[0])
			#group.Backbone Lower -> compare_004.B
			_mn_select_nucleic.links.new(group.outputs[0], compare_004.inputs[3])
			#named_attribute.Attribute -> compare_004.A
			_mn_select_nucleic.links.new(named_attribute.outputs[0], compare_004.inputs[2])
			#group.Side Chain Upper -> compare_005.B
			_mn_select_nucleic.links.new(group.outputs[3], compare_005.inputs[3])
			#named_attribute.Attribute -> compare_005.A
			_mn_select_nucleic.links.new(named_attribute.outputs[0], compare_005.inputs[2])
			#boolean_math_003.Boolean -> group_output_1.Is Nucleic
			_mn_select_nucleic.links.new(boolean_math_003.outputs[0], group_output_1.inputs[2])
			return _mn_select_nucleic

		_mn_select_nucleic = _mn_select_nucleic_node_group()

		#initialize fallback_boolean node group
		def fallback_boolean_node_group():
			fallback_boolean = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Fallback Boolean")

			fallback_boolean.color_tag = 'INPUT'
			fallback_boolean.description = "Computes the boolean field if the given attribute doesn't exist. If it doesn't exist it just uses the attribute instead"

			
			#fallback_boolean interface
			#Socket Boolean
			boolean_socket = fallback_boolean.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket.attribute_domain = 'POINT'
			
			#Socket Name
			name_socket = fallback_boolean.interface.new_socket(name = "Name", in_out='INPUT', socket_type = 'NodeSocketString')
			name_socket.attribute_domain = 'POINT'
			
			#Socket Fallback
			fallback_socket = fallback_boolean.interface.new_socket(name = "Fallback", in_out='INPUT', socket_type = 'NodeSocketBool')
			fallback_socket.attribute_domain = 'POINT'
			
			
			#initialize fallback_boolean nodes
			#node Group Output
			group_output_2 = fallback_boolean.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Group Input
			group_input_2 = fallback_boolean.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
			#node Named Attribute
			named_attribute_1 = fallback_boolean.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_1.name = "Named Attribute"
			named_attribute_1.data_type = 'BOOLEAN'
			
			#node Switch
			switch = fallback_boolean.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'BOOLEAN'
			
			
			
			
			#Set locations
			group_output_2.location = (276.6171569824219, 4.738137245178223)
			group_input_2.location = (-280.0, 0.0)
			named_attribute_1.location = (-94.73597717285156, 4.738137245178223)
			switch.location = (86.61715698242188, 4.738137245178223)
			
			#Set dimensions
			group_output_2.width, group_output_2.height = 140.0, 100.0
			group_input_2.width, group_input_2.height = 140.0, 100.0
			named_attribute_1.width, named_attribute_1.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			
			#initialize fallback_boolean links
			#named_attribute_1.Exists -> switch.Switch
			fallback_boolean.links.new(named_attribute_1.outputs[1], switch.inputs[0])
			#named_attribute_1.Attribute -> switch.True
			fallback_boolean.links.new(named_attribute_1.outputs[0], switch.inputs[2])
			#group_input_2.Fallback -> switch.False
			fallback_boolean.links.new(group_input_2.outputs[1], switch.inputs[1])
			#switch.Output -> group_output_2.Boolean
			fallback_boolean.links.new(switch.outputs[0], group_output_2.inputs[0])
			#group_input_2.Name -> named_attribute_1.Name
			fallback_boolean.links.new(group_input_2.outputs[0], named_attribute_1.inputs[0])
			return fallback_boolean

		fallback_boolean = fallback_boolean_node_group()

		#initialize is_nucleic node group
		def is_nucleic_node_group():
			is_nucleic = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Is Nucleic")

			is_nucleic.color_tag = 'INPUT'
			is_nucleic.description = ""

			
			#is_nucleic interface
			#Socket Selection
			selection_socket = is_nucleic.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket.attribute_domain = 'POINT'
			selection_socket.description = "True if atoms are part of a nucleic acid"
			
			#Socket Inverted
			inverted_socket = is_nucleic.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket.attribute_domain = 'POINT'
			
			#Socket And
			and_socket = is_nucleic.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket.attribute_domain = 'POINT'
			and_socket.hide_value = True
			
			#Socket Or
			or_socket = is_nucleic.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket.attribute_domain = 'POINT'
			or_socket.hide_value = True
			
			
			#initialize is_nucleic nodes
			#node Group Input
			group_input_3 = is_nucleic.nodes.new("NodeGroupInput")
			group_input_3.name = "Group Input"
			
			#node Boolean Math.001
			boolean_math_001_1 = is_nucleic.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_1.name = "Boolean Math.001"
			boolean_math_001_1.operation = 'AND'
			
			#node Group Output
			group_output_3 = is_nucleic.nodes.new("NodeGroupOutput")
			group_output_3.name = "Group Output"
			group_output_3.is_active_output = True
			
			#node Group
			group_1 = is_nucleic.nodes.new("GeometryNodeGroup")
			group_1.name = "Group"
			group_1.node_tree = _mn_select_nucleic
			
			#node Group.001
			group_001 = is_nucleic.nodes.new("GeometryNodeGroup")
			group_001.name = "Group.001"
			group_001.node_tree = fallback_boolean
			#Socket_2
			group_001.inputs[0].default_value = "is_nucleic"
			
			#node Boolean Math.002
			boolean_math_002_1 = is_nucleic.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_1.name = "Boolean Math.002"
			boolean_math_002_1.operation = 'OR'
			
			#node Boolean Math
			boolean_math = is_nucleic.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'NOT'
			
			
			
			
			#Set locations
			group_input_3.location = (-280.0, -40.0)
			boolean_math_001_1.location = (-40.0, 0.0)
			group_output_3.location = (320.0000305175781, 0.0)
			group_1.location = (-620.0, -160.0)
			group_001.location = (-340.0, -160.0)
			boolean_math_002_1.location = (140.0, 0.0)
			boolean_math.location = (140.0, -140.0)
			
			#Set dimensions
			group_input_3.width, group_input_3.height = 140.0, 100.0
			boolean_math_001_1.width, boolean_math_001_1.height = 140.0, 100.0
			group_output_3.width, group_output_3.height = 140.0, 100.0
			group_1.width, group_1.height = 247.90924072265625, 100.0
			group_001.width, group_001.height = 232.0133056640625, 100.0
			boolean_math_002_1.width, boolean_math_002_1.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			
			#initialize is_nucleic links
			#boolean_math_002_1.Boolean -> group_output_3.Selection
			is_nucleic.links.new(boolean_math_002_1.outputs[0], group_output_3.inputs[0])
			#group_input_3.And -> boolean_math_001_1.Boolean
			is_nucleic.links.new(group_input_3.outputs[0], boolean_math_001_1.inputs[0])
			#group_1.Is Nucleic -> group_001.Fallback
			is_nucleic.links.new(group_1.outputs[2], group_001.inputs[1])
			#group_001.Boolean -> boolean_math_001_1.Boolean
			is_nucleic.links.new(group_001.outputs[0], boolean_math_001_1.inputs[1])
			#boolean_math_001_1.Boolean -> boolean_math_002_1.Boolean
			is_nucleic.links.new(boolean_math_001_1.outputs[0], boolean_math_002_1.inputs[0])
			#group_input_3.Or -> boolean_math_002_1.Boolean
			is_nucleic.links.new(group_input_3.outputs[1], boolean_math_002_1.inputs[1])
			#boolean_math_002_1.Boolean -> boolean_math.Boolean
			is_nucleic.links.new(boolean_math_002_1.outputs[0], boolean_math.inputs[0])
			#boolean_math.Boolean -> group_output_3.Inverted
			is_nucleic.links.new(boolean_math.outputs[0], group_output_3.inputs[1])
			return is_nucleic

		is_nucleic = is_nucleic_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Is Nucleic", type = 'NODES')
		mod.node_group = is_nucleic
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Is_Nucleic.bl_idname)
			
def register():
	bpy.utils.register_class(Is_Nucleic)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Is_Nucleic)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
