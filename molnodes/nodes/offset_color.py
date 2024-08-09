bl_info = {
	"name" : "Offset Color",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Offset_Color(bpy.types.Operator):
	bl_idname = "node.offset_color"
	bl_label = "Offset Color"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize offset_color node group
		def offset_color_node_group():
			offset_color = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Offset Color")

			offset_color.color_tag = 'NONE'
			offset_color.description = ""

			
			#offset_color interface
			#Socket Color
			color_socket = offset_color.interface.new_socket(name = "Color", in_out='OUTPUT', socket_type = 'NodeSocketColor')
			color_socket.attribute_domain = 'POINT'
			
			#Socket Index
			index_socket = offset_color.interface.new_socket(name = "Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			index_socket.subtype = 'NONE'
			index_socket.default_value = 0
			index_socket.min_value = -2147483648
			index_socket.max_value = 2147483647
			index_socket.attribute_domain = 'POINT'
			
			#Socket Offset
			offset_socket = offset_color.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket.subtype = 'NONE'
			offset_socket.default_value = 0
			offset_socket.min_value = -2147483648
			offset_socket.max_value = 2147483647
			offset_socket.attribute_domain = 'POINT'
			
			
			#initialize offset_color nodes
			#node Group Input
			group_input = offset_color.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Math.012
			math_012 = offset_color.nodes.new("ShaderNodeMath")
			math_012.name = "Math.012"
			math_012.operation = 'ADD'
			math_012.use_clamp = False
			
			#node Evaluate at Index.004
			evaluate_at_index_004 = offset_color.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_004.name = "Evaluate at Index.004"
			evaluate_at_index_004.data_type = 'FLOAT_COLOR'
			evaluate_at_index_004.domain = 'POINT'
			
			#node Group Output
			group_output = offset_color.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Named Attribute
			named_attribute = offset_color.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute.inputs[0].default_value = "Color"
			
			
			
			
			#Set locations
			group_input.location = (-220.0, -20.0)
			math_012.location = (-40.0, 0.0)
			evaluate_at_index_004.location = (140.0, 0.0)
			group_output.location = (340.0, 0.0)
			named_attribute.location = (-40.0, -160.0)
			
			#Set dimensions
			group_input.width, group_input.height = 140.0, 100.0
			math_012.width, math_012.height = 140.0, 100.0
			evaluate_at_index_004.width, evaluate_at_index_004.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			
			#initialize offset_color links
			#math_012.Value -> evaluate_at_index_004.Index
			offset_color.links.new(math_012.outputs[0], evaluate_at_index_004.inputs[0])
			#group_input.Offset -> math_012.Value
			offset_color.links.new(group_input.outputs[1], math_012.inputs[1])
			#evaluate_at_index_004.Value -> group_output.Color
			offset_color.links.new(evaluate_at_index_004.outputs[0], group_output.inputs[0])
			#named_attribute.Attribute -> evaluate_at_index_004.Value
			offset_color.links.new(named_attribute.outputs[0], evaluate_at_index_004.inputs[1])
			#group_input.Index -> math_012.Value
			offset_color.links.new(group_input.outputs[0], math_012.inputs[0])
			return offset_color

		offset_color = offset_color_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Offset Color", type = 'NODES')
		mod.node_group = offset_color
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Offset_Color.bl_idname)
			
def register():
	bpy.utils.register_class(Offset_Color)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Offset_Color)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
