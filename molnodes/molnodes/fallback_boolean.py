bl_info = {
	"name" : "Fallback Boolean",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Fallback_Boolean(bpy.types.Operator):
	bl_idname = "node.fallback_boolean"
	bl_label = "Fallback Boolean"
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
			boolean_socket.attribute_domain = 'POINT'
			
			#Socket Name
			name_socket = fallback_boolean.interface.new_socket(name = "Name", in_out='INPUT', socket_type = 'NodeSocketString')
			name_socket.attribute_domain = 'POINT'
			
			#Socket Fallback
			fallback_socket = fallback_boolean.interface.new_socket(name = "Fallback", in_out='INPUT', socket_type = 'NodeSocketBool')
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

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Fallback Boolean", type = 'NODES')
		mod.node_group = fallback_boolean
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Fallback_Boolean.bl_idname)
			
def register():
	bpy.utils.register_class(Fallback_Boolean)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Fallback_Boolean)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
