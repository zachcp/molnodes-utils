bl_info = {
	"name" : "Select Chain_",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Select_Chain_(bpy.types.Operator):
	bl_idname = "node.select_chain_"
	bl_label = "Select Chain_"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize select_chain_ node group
		def select_chain__node_group():
			select_chain_ = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Select Chain_")

			select_chain_.color_tag = 'INPUT'
			select_chain_.description = ""

			
			#select_chain_ interface
			#Socket Selection
			selection_socket = select_chain_.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket.default_value = False
			selection_socket.attribute_domain = 'POINT'
			selection_socket.description = "The calculated selection"
			
			#Socket Inverted
			inverted_socket = select_chain_.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket.default_value = False
			inverted_socket.attribute_domain = 'POINT'
			inverted_socket.description = "The inverse of the calculated selection"
			
			#Socket Chain A
			chain_a_socket = select_chain_.interface.new_socket(name = "Chain A", in_out='INPUT', socket_type = 'NodeSocketBool')
			chain_a_socket.default_value = True
			chain_a_socket.attribute_domain = 'POINT'
			chain_a_socket.description = "Select the atoms in Chain A"
			
			#Socket Chain B
			chain_b_socket = select_chain_.interface.new_socket(name = "Chain B", in_out='INPUT', socket_type = 'NodeSocketBool')
			chain_b_socket.default_value = True
			chain_b_socket.attribute_domain = 'POINT'
			chain_b_socket.description = "Select the atoms in Chain B"
			
			#Socket Chain ...
			chain_____socket = select_chain_.interface.new_socket(name = "Chain ...", in_out='INPUT', socket_type = 'NodeSocketBool')
			chain_____socket.default_value = True
			chain_____socket.attribute_domain = 'POINT'
			chain_____socket.description = "Select the atoms in Chain ..."
			
			
			#initialize select_chain_ nodes
			#node Named Attribute
			named_attribute = select_chain_.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'INT'
			#Name
			named_attribute.inputs[0].default_value = "chaind_id"
			
			#node Group Output
			group_output = select_chain_.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Boolean Math.001
			boolean_math_001 = select_chain_.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001.name = "Boolean Math.001"
			boolean_math_001.operation = 'NOT'
			
			#node Group Input
			group_input = select_chain_.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Index Switch
			index_switch = select_chain_.nodes.new("GeometryNodeIndexSwitch")
			index_switch.name = "Index Switch"
			index_switch.data_type = 'BOOLEAN'
			index_switch.index_switch_items.clear()
			index_switch.index_switch_items.new()
			index_switch.index_switch_items.new()
			index_switch.index_switch_items.new()
			
			
			
			
			#Set locations
			named_attribute.location = (-780.0, -60.0)
			group_output.location = (-160.0, -180.0)
			boolean_math_001.location = (-320.0, -260.0)
			group_input.location = (-780.0, -240.0)
			index_switch.location = (-494.1487121582031, -182.76792907714844)
			
			#Set dimensions
			named_attribute.width, named_attribute.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			index_switch.width, index_switch.height = 140.0, 100.0
			
			#initialize select_chain_ links
			#index_switch.Output -> boolean_math_001.Boolean
			select_chain_.links.new(index_switch.outputs[0], boolean_math_001.inputs[0])
			#index_switch.Output -> group_output.Selection
			select_chain_.links.new(index_switch.outputs[0], group_output.inputs[0])
			#boolean_math_001.Boolean -> group_output.Inverted
			select_chain_.links.new(boolean_math_001.outputs[0], group_output.inputs[1])
			#named_attribute.Attribute -> index_switch.Index
			select_chain_.links.new(named_attribute.outputs[0], index_switch.inputs[0])
			#group_input.Chain A -> index_switch.0
			select_chain_.links.new(group_input.outputs[0], index_switch.inputs[1])
			#group_input.Chain B -> index_switch.1
			select_chain_.links.new(group_input.outputs[1], index_switch.inputs[2])
			#group_input.Chain ... -> index_switch.2
			select_chain_.links.new(group_input.outputs[2], index_switch.inputs[3])
			return select_chain_

		select_chain_ = select_chain__node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Select Chain_", type = 'NODES')
		mod.node_group = select_chain_
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Select_Chain_.bl_idname)
			
def register():
	bpy.utils.register_class(Select_Chain_)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Select_Chain_)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
