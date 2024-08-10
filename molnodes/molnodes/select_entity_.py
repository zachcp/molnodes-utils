bl_info = {
	"name" : "Select Entity_",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Select_Entity_(bpy.types.Operator):
	bl_idname = "node.select_entity_"
	bl_label = "Select Entity_"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize select_entity_ node group
		def select_entity__node_group():
			select_entity_ = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Select Entity_")

			select_entity_.color_tag = 'INPUT'
			select_entity_.description = ""

			
			#select_entity_ interface
			#Socket Selection
			selection_socket = select_entity_.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket.attribute_domain = 'POINT'
			selection_socket.description = "The calculated selection"
			
			#Socket Inverted
			inverted_socket = select_entity_.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket.attribute_domain = 'POINT'
			inverted_socket.description = "The inverse of the calculated selection"
			
			#Socket Entity A
			entity_a_socket = select_entity_.interface.new_socket(name = "Entity A", in_out='INPUT', socket_type = 'NodeSocketBool')
			entity_a_socket.attribute_domain = 'POINT'
			entity_a_socket.description = "Select the atoms in Entity A"
			
			#Socket Entity B
			entity_b_socket = select_entity_.interface.new_socket(name = "Entity B", in_out='INPUT', socket_type = 'NodeSocketBool')
			entity_b_socket.attribute_domain = 'POINT'
			entity_b_socket.description = "Select the atoms in Entity B"
			
			#Socket Entity ...
			entity_____socket = select_entity_.interface.new_socket(name = "Entity ...", in_out='INPUT', socket_type = 'NodeSocketBool')
			entity_____socket.attribute_domain = 'POINT'
			entity_____socket.description = "Select the atoms in Entity ..."
			
			
			#initialize select_entity_ nodes
			#node Named Attribute
			named_attribute = select_entity_.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'INT'
			#Name
			named_attribute.inputs[0].default_value = "chaind_id"
			
			#node Reroute.018
			reroute_018 = select_entity_.nodes.new("NodeReroute")
			reroute_018.name = "Reroute.018"
			#node Group Output
			group_output = select_entity_.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Boolean Math.001
			boolean_math_001 = select_entity_.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001.name = "Boolean Math.001"
			boolean_math_001.operation = 'NOT'
			
			#node Group Input
			group_input = select_entity_.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Index Switch
			index_switch = select_entity_.nodes.new("GeometryNodeIndexSwitch")
			index_switch.name = "Index Switch"
			index_switch.data_type = 'BOOLEAN'
			index_switch.index_switch_items.clear()
			index_switch.index_switch_items.new()
			index_switch.index_switch_items.new()
			index_switch.index_switch_items.new()
			
			
			
			
			#Set locations
			named_attribute.location = (-780.0, -60.0)
			reroute_018.location = (-420.0, -220.0)
			group_output.location = (-200.0, -180.0)
			boolean_math_001.location = (-380.0, -240.0)
			group_input.location = (-780.0, -240.0)
			index_switch.location = (-600.0, -180.0)
			
			#Set dimensions
			named_attribute.width, named_attribute.height = 140.0, 100.0
			reroute_018.width, reroute_018.height = 16.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			index_switch.width, index_switch.height = 140.0, 100.0
			
			#initialize select_entity_ links
			#reroute_018.Output -> boolean_math_001.Boolean
			select_entity_.links.new(reroute_018.outputs[0], boolean_math_001.inputs[0])
			#reroute_018.Output -> group_output.Selection
			select_entity_.links.new(reroute_018.outputs[0], group_output.inputs[0])
			#boolean_math_001.Boolean -> group_output.Inverted
			select_entity_.links.new(boolean_math_001.outputs[0], group_output.inputs[1])
			#named_attribute.Attribute -> index_switch.Index
			select_entity_.links.new(named_attribute.outputs[0], index_switch.inputs[0])
			#group_input.Entity A -> index_switch.0
			select_entity_.links.new(group_input.outputs[0], index_switch.inputs[1])
			#group_input.Entity B -> index_switch.1
			select_entity_.links.new(group_input.outputs[1], index_switch.inputs[2])
			#group_input.Entity ... -> index_switch.2
			select_entity_.links.new(group_input.outputs[2], index_switch.inputs[3])
			#index_switch.Output -> reroute_018.Input
			select_entity_.links.new(index_switch.outputs[0], reroute_018.inputs[0])
			return select_entity_

		select_entity_ = select_entity__node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Select Entity_", type = 'NODES')
		mod.node_group = select_entity_
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Select_Entity_.bl_idname)
			
def register():
	bpy.utils.register_class(Select_Entity_)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Select_Entity_)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
