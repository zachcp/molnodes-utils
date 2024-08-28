bl_info = {
	"name" : "Fallback Color",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Fallback_Color(bpy.types.Operator):
	bl_idname = "node.fallback_color"
	bl_label = "Fallback Color"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize fallback_color node group
		def fallback_color_node_group():
			fallback_color = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Fallback Color")

			fallback_color.color_tag = 'INPUT'
			fallback_color.description = ""

			
			#fallback_color interface
			#Socket Color
			color_socket = fallback_color.interface.new_socket(name = "Color", in_out='OUTPUT', socket_type = 'NodeSocketColor')
			color_socket.default_value = (0.0, 0.0, 0.0, 1.0)
			color_socket.attribute_domain = 'POINT'
			
			#Socket Name
			name_socket = fallback_color.interface.new_socket(name = "Name", in_out='INPUT', socket_type = 'NodeSocketString')
			name_socket.default_value = "Color"
			name_socket.attribute_domain = 'POINT'
			
			#Socket Fallback
			fallback_socket = fallback_color.interface.new_socket(name = "Fallback", in_out='INPUT', socket_type = 'NodeSocketColor')
			fallback_socket.default_value = (0.07164950668811798, 0.29542478919029236, 0.23565927147865295, 1.0)
			fallback_socket.attribute_domain = 'POINT'
			fallback_socket.description = "Fallback value if Field is 0"
			
			
			#initialize fallback_color nodes
			#node Group Output
			group_output = fallback_color.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = fallback_color.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Switch
			switch = fallback_color.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'RGBA'
			
			#node Named Attribute
			named_attribute = fallback_color.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'FLOAT_COLOR'
			
			
			
			
			#Set locations
			group_output.location = (288.23382568359375, 0.0)
			group_input.location = (-320.0, -40.0)
			switch.location = (98.23382568359375, 26.690887451171875)
			named_attribute.location = (-123.81201934814453, -87.02108001708984)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			
			#initialize fallback_color links
			#switch.Output -> group_output.Color
			fallback_color.links.new(switch.outputs[0], group_output.inputs[0])
			#named_attribute.Exists -> switch.Switch
			fallback_color.links.new(named_attribute.outputs[1], switch.inputs[0])
			#named_attribute.Attribute -> switch.True
			fallback_color.links.new(named_attribute.outputs[0], switch.inputs[2])
			#group_input.Fallback -> switch.False
			fallback_color.links.new(group_input.outputs[1], switch.inputs[1])
			#group_input.Name -> named_attribute.Name
			fallback_color.links.new(group_input.outputs[0], named_attribute.inputs[0])
			return fallback_color

		fallback_color = fallback_color_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Fallback Color", type = 'NODES')
		mod.node_group = fallback_color
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Fallback_Color.bl_idname)
			
def register():
	bpy.utils.register_class(Fallback_Color)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Fallback_Color)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
