bl_info = {
	"name" : "Color Atomic Number",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Color_Atomic_Number(bpy.types.Operator):
	bl_idname = "node.color_atomic_number"
	bl_label = "Color Atomic Number"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize color_atomic_number node group
		def color_atomic_number_node_group():
			color_atomic_number = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Color Atomic Number")

			color_atomic_number.color_tag = 'COLOR'
			color_atomic_number.description = ""

			
			#color_atomic_number interface
			#Socket Color
			color_socket = color_atomic_number.interface.new_socket(name = "Color", in_out='OUTPUT', socket_type = 'NodeSocketColor')
			color_socket.attribute_domain = 'POINT'
			
			#Socket atomic_number
			atomic_number_socket = color_atomic_number.interface.new_socket(name = "atomic_number", in_out='INPUT', socket_type = 'NodeSocketInt')
			atomic_number_socket.subtype = 'NONE'
			atomic_number_socket.default_value = 6
			atomic_number_socket.min_value = 1
			atomic_number_socket.max_value = 140
			atomic_number_socket.attribute_domain = 'POINT'
			
			#Socket Color
			color_socket_1 = color_atomic_number.interface.new_socket(name = "Color", in_out='INPUT', socket_type = 'NodeSocketColor')
			color_socket_1.attribute_domain = 'POINT'
			
			
			#initialize color_atomic_number nodes
			#node Group Input
			group_input = color_atomic_number.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Group Output
			group_output = color_atomic_number.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Compare
			compare = color_atomic_number.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'EQUAL'
			
			#node Switch
			switch = color_atomic_number.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'RGBA'
			
			#node Named Attribute
			named_attribute = color_atomic_number.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'INT'
			#Name
			named_attribute.inputs[0].default_value = "atomic_number"
			
			#node Named Attribute.001
			named_attribute_001 = color_atomic_number.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute_001.inputs[0].default_value = "Color"
			
			
			
			
			#Set locations
			group_input.location = (-360.0, -120.0)
			group_output.location = (160.0, 0.0)
			compare.location = (-200.0, 0.0)
			switch.location = (-5.954658508300781, 130.74545288085938)
			named_attribute.location = (-360.0, 0.0)
			named_attribute_001.location = (-360.0, 140.0)
			
			#Set dimensions
			group_input.width, group_input.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
			
			#initialize color_atomic_number links
			#named_attribute.Attribute -> compare.A
			color_atomic_number.links.new(named_attribute.outputs[0], compare.inputs[2])
			#group_input.atomic_number -> compare.B
			color_atomic_number.links.new(group_input.outputs[0], compare.inputs[3])
			#compare.Result -> switch.Switch
			color_atomic_number.links.new(compare.outputs[0], switch.inputs[0])
			#group_input.Color -> switch.True
			color_atomic_number.links.new(group_input.outputs[1], switch.inputs[2])
			#switch.Output -> group_output.Color
			color_atomic_number.links.new(switch.outputs[0], group_output.inputs[0])
			#named_attribute_001.Attribute -> switch.False
			color_atomic_number.links.new(named_attribute_001.outputs[0], switch.inputs[1])
			return color_atomic_number

		color_atomic_number = color_atomic_number_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Color Atomic Number", type = 'NODES')
		mod.node_group = color_atomic_number
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Color_Atomic_Number.bl_idname)
			
def register():
	bpy.utils.register_class(Color_Atomic_Number)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Color_Atomic_Number)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
