bl_info = {
	"name" : ".MN_select_nucleic",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _MN_select_nucleic(bpy.types.Operator):
	bl_idname = "node._mn_select_nucleic"
	bl_label = ".MN_select_nucleic"
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
			backbone_lower_socket.default_value = 0
			backbone_lower_socket.min_value = -2147483648
			backbone_lower_socket.max_value = 2147483647
			backbone_lower_socket.subtype = 'NONE'
			backbone_lower_socket.attribute_domain = 'POINT'
			
			#Socket Backbone Upper
			backbone_upper_socket = _mn_constants_atom_name_nucleic.interface.new_socket(name = "Backbone Upper", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			backbone_upper_socket.default_value = 0
			backbone_upper_socket.min_value = -2147483648
			backbone_upper_socket.max_value = 2147483647
			backbone_upper_socket.subtype = 'NONE'
			backbone_upper_socket.attribute_domain = 'POINT'
			
			#Socket Side Chain Lower
			side_chain_lower_socket = _mn_constants_atom_name_nucleic.interface.new_socket(name = "Side Chain Lower", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			side_chain_lower_socket.default_value = 0
			side_chain_lower_socket.min_value = -2147483648
			side_chain_lower_socket.max_value = 2147483647
			side_chain_lower_socket.subtype = 'NONE'
			side_chain_lower_socket.attribute_domain = 'POINT'
			
			#Socket Side Chain Upper
			side_chain_upper_socket = _mn_constants_atom_name_nucleic.interface.new_socket(name = "Side Chain Upper", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			side_chain_upper_socket.default_value = 0
			side_chain_upper_socket.min_value = -2147483648
			side_chain_upper_socket.max_value = 2147483647
			side_chain_upper_socket.subtype = 'NONE'
			side_chain_upper_socket.attribute_domain = 'POINT'
			
			#Socket Side Chain Joint Carbon
			side_chain_joint_carbon_socket = _mn_constants_atom_name_nucleic.interface.new_socket(name = "Side Chain Joint Carbon", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			side_chain_joint_carbon_socket.default_value = 0
			side_chain_joint_carbon_socket.min_value = -2147483648
			side_chain_joint_carbon_socket.max_value = 2147483647
			side_chain_joint_carbon_socket.subtype = 'NONE'
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
			is_backbone_socket.default_value = False
			is_backbone_socket.attribute_domain = 'POINT'
			is_backbone_socket.description = "True for atoms that are part of the sugar-phosphate backbone for the nucleotides"
			
			#Socket Is Side Chain
			is_side_chain_socket = _mn_select_nucleic.interface.new_socket(name = "Is Side Chain", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_side_chain_socket.default_value = False
			is_side_chain_socket.attribute_domain = 'POINT'
			is_side_chain_socket.description = "True for atoms that are part of the bases for nucleotides."
			
			#Socket Is Nucleic
			is_nucleic_socket = _mn_select_nucleic.interface.new_socket(name = "Is Nucleic", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_nucleic_socket.default_value = False
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

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".MN_select_nucleic", type = 'NODES')
		mod.node_group = _mn_select_nucleic
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_MN_select_nucleic.bl_idname)
			
def register():
	bpy.utils.register_class(_MN_select_nucleic)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_MN_select_nucleic)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
