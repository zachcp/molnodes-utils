bl_info = {
	"name" : "Fallback Integer",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Fallback_Integer(bpy.types.Operator):
	bl_idname = "node.fallback_integer"
	bl_label = "Fallback Integer"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize fallback_integer node group
		def fallback_integer_node_group():
			fallback_integer = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Fallback Integer")

			fallback_integer.color_tag = 'INPUT'
			fallback_integer.description = ""

			
			#fallback_integer interface
			#Socket Integer
			integer_socket = fallback_integer.interface.new_socket(name = "Integer", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			integer_socket.subtype = 'NONE'
			integer_socket.default_value = 0
			integer_socket.min_value = -2147483648
			integer_socket.max_value = 2147483647
			integer_socket.attribute_domain = 'POINT'
			
			#Socket Name
			name_socket = fallback_integer.interface.new_socket(name = "Name", in_out='INPUT', socket_type = 'NodeSocketString')
			name_socket.attribute_domain = 'POINT'
			
			#Socket Fallback
			fallback_socket = fallback_integer.interface.new_socket(name = "Fallback", in_out='INPUT', socket_type = 'NodeSocketInt')
			fallback_socket.subtype = 'NONE'
			fallback_socket.default_value = 0
			fallback_socket.min_value = -2147483648
			fallback_socket.max_value = 2147483647
			fallback_socket.attribute_domain = 'POINT'
			fallback_socket.description = "Fallback value if Field is 0"
			
			
			#initialize fallback_integer nodes
			#node Group Output
			group_output = fallback_integer.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = fallback_integer.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Switch
			switch = fallback_integer.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'INT'
			
			#node Named Attribute
			named_attribute = fallback_integer.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'INT'
			
			
			
			
			#Set locations
			group_output.location = (288.23382568359375, 0.0)
			group_input.location = (-320.0, -40.0)
			switch.location = (98.23382568359375, 26.690887451171875)
			named_attribute.location = (-120.0, -80.0)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			
			#initialize fallback_integer links
			#switch.Output -> group_output.Integer
			fallback_integer.links.new(switch.outputs[0], group_output.inputs[0])
			#group_input.Fallback -> switch.False
			fallback_integer.links.new(group_input.outputs[1], switch.inputs[1])
			#group_input.Name -> named_attribute.Name
			fallback_integer.links.new(group_input.outputs[0], named_attribute.inputs[0])
			#named_attribute.Exists -> switch.Switch
			fallback_integer.links.new(named_attribute.outputs[1], switch.inputs[0])
			#named_attribute.Attribute -> switch.True
			fallback_integer.links.new(named_attribute.outputs[0], switch.inputs[2])
			return fallback_integer

		fallback_integer = fallback_integer_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Fallback Integer", type = 'NODES')
		mod.node_group = fallback_integer
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Fallback_Integer.bl_idname)
			
def register():
	bpy.utils.register_class(Fallback_Integer)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Fallback_Integer)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
