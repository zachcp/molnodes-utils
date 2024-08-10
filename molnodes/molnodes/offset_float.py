bl_info = {
	"name" : "Offset Float",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Offset_Float(bpy.types.Operator):
	bl_idname = "node.offset_float"
	bl_label = "Offset Float"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize offset_float node group
		def offset_float_node_group():
			offset_float = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Offset Float")

			offset_float.color_tag = 'CONVERTER'
			offset_float.description = ""

			
			#offset_float interface
			#Socket Value
			value_socket = offset_float.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			value_socket.subtype = 'NONE'
			value_socket.default_value = 0.0
			value_socket.min_value = -3.4028234663852886e+38
			value_socket.max_value = 3.4028234663852886e+38
			value_socket.attribute_domain = 'POINT'
			
			#Socket Index
			index_socket = offset_float.interface.new_socket(name = "Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			index_socket.subtype = 'NONE'
			index_socket.default_value = 0
			index_socket.min_value = 0
			index_socket.max_value = 2147483647
			index_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_1 = offset_float.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket_1.subtype = 'NONE'
			value_socket_1.default_value = 0.0
			value_socket_1.min_value = -3.4028234663852886e+38
			value_socket_1.max_value = 3.4028234663852886e+38
			value_socket_1.attribute_domain = 'POINT'
			value_socket_1.hide_value = True
			
			#Socket Offset
			offset_socket = offset_float.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket.subtype = 'NONE'
			offset_socket.default_value = 0
			offset_socket.min_value = -2147483647
			offset_socket.max_value = 2147483647
			offset_socket.attribute_domain = 'POINT'
			
			
			#initialize offset_float nodes
			#node Group Output
			group_output = offset_float.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = offset_float.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Evaluate at Index
			evaluate_at_index = offset_float.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index.name = "Evaluate at Index"
			evaluate_at_index.data_type = 'FLOAT'
			evaluate_at_index.domain = 'POINT'
			
			#node Math
			math = offset_float.nodes.new("ShaderNodeMath")
			math.name = "Math"
			math.operation = 'ADD'
			math.use_clamp = False
			
			
			
			
			#Set locations
			group_output.location = (190.0, 0.0)
			group_input.location = (-344.3331298828125, -46.23834991455078)
			evaluate_at_index.location = (0.0, 0.0)
			math.location = (-160.0, 0.0)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			evaluate_at_index.width, evaluate_at_index.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			
			#initialize offset_float links
			#evaluate_at_index.Value -> group_output.Value
			offset_float.links.new(evaluate_at_index.outputs[0], group_output.inputs[0])
			#group_input.Value -> evaluate_at_index.Value
			offset_float.links.new(group_input.outputs[1], evaluate_at_index.inputs[1])
			#group_input.Index -> math.Value
			offset_float.links.new(group_input.outputs[0], math.inputs[1])
			#math.Value -> evaluate_at_index.Index
			offset_float.links.new(math.outputs[0], evaluate_at_index.inputs[0])
			#group_input.Offset -> math.Value
			offset_float.links.new(group_input.outputs[2], math.inputs[0])
			return offset_float

		offset_float = offset_float_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Offset Float", type = 'NODES')
		mod.node_group = offset_float
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Offset_Float.bl_idname)
			
def register():
	bpy.utils.register_class(Offset_Float)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Offset_Float)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
