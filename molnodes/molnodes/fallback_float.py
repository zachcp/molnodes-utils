bl_info = {
	"name" : "Fallback Float",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Fallback_Float(bpy.types.Operator):
	bl_idname = "node.fallback_float"
	bl_label = "Fallback Float"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize fallback_float node group
		def fallback_float_node_group():
			fallback_float = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Fallback Float")

			fallback_float.color_tag = 'INPUT'
			fallback_float.description = ""

			
			#fallback_float interface
			#Socket Value
			value_socket = fallback_float.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			value_socket.default_value = 0.0
			value_socket.min_value = -3.4028234663852886e+38
			value_socket.max_value = 3.4028234663852886e+38
			value_socket.subtype = 'NONE'
			value_socket.attribute_domain = 'POINT'
			
			#Socket Name
			name_socket = fallback_float.interface.new_socket(name = "Name", in_out='INPUT', socket_type = 'NodeSocketString')
			name_socket.default_value = ""
			name_socket.attribute_domain = 'POINT'
			
			#Socket Fallback
			fallback_socket = fallback_float.interface.new_socket(name = "Fallback", in_out='INPUT', socket_type = 'NodeSocketFloat')
			fallback_socket.default_value = 0.0
			fallback_socket.min_value = -3.4028234663852886e+38
			fallback_socket.max_value = 3.4028234663852886e+38
			fallback_socket.subtype = 'NONE'
			fallback_socket.attribute_domain = 'POINT'
			
			
			#initialize fallback_float nodes
			#node Group Output
			group_output = fallback_float.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = fallback_float.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Named Attribute
			named_attribute = fallback_float.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'FLOAT'
			
			#node Switch
			switch = fallback_float.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'FLOAT'
			
			
			
			
			#Set locations
			group_output.location = (306.3518981933594, 0.0)
			group_input.location = (-316.3518981933594, 0.0)
			named_attribute.location = (-136.0193634033203, 58.357723236083984)
			switch.location = (116.35189819335938, 12.828765869140625)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 168.09637451171875, 100.0
			switch.width, switch.height = 140.0, 100.0
			
			#initialize fallback_float links
			#named_attribute.Exists -> switch.Switch
			fallback_float.links.new(named_attribute.outputs[1], switch.inputs[0])
			#named_attribute.Attribute -> switch.True
			fallback_float.links.new(named_attribute.outputs[0], switch.inputs[2])
			#group_input.Name -> named_attribute.Name
			fallback_float.links.new(group_input.outputs[0], named_attribute.inputs[0])
			#group_input.Fallback -> switch.False
			fallback_float.links.new(group_input.outputs[1], switch.inputs[1])
			#switch.Output -> group_output.Value
			fallback_float.links.new(switch.outputs[0], group_output.inputs[0])
			return fallback_float

		fallback_float = fallback_float_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Fallback Float", type = 'NODES')
		mod.node_group = fallback_float
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Fallback_Float.bl_idname)
			
def register():
	bpy.utils.register_class(Fallback_Float)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Fallback_Float)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
