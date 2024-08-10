bl_info = {
	"name" : ".MN_utils_int_multiply",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _MN_utils_int_multiply(bpy.types.Operator):
	bl_idname = "node._mn_utils_int_multiply"
	bl_label = ".MN_utils_int_multiply"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _mn_utils_int_multiply node group
		def _mn_utils_int_multiply_node_group():
			_mn_utils_int_multiply = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_utils_int_multiply")

			_mn_utils_int_multiply.color_tag = 'CONVERTER'
			_mn_utils_int_multiply.description = ""

			
			#_mn_utils_int_multiply interface
			#Socket Value
			value_socket = _mn_utils_int_multiply.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			value_socket.subtype = 'NONE'
			value_socket.default_value = 0
			value_socket.min_value = -2147483648
			value_socket.max_value = 2147483647
			value_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_1 = _mn_utils_int_multiply.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketInt')
			value_socket_1.subtype = 'NONE'
			value_socket_1.default_value = 0
			value_socket_1.min_value = -2147483648
			value_socket_1.max_value = 2147483647
			value_socket_1.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_2 = _mn_utils_int_multiply.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketInt')
			value_socket_2.subtype = 'NONE'
			value_socket_2.default_value = 0
			value_socket_2.min_value = -2147483648
			value_socket_2.max_value = 2147483647
			value_socket_2.attribute_domain = 'POINT'
			
			
			#initialize _mn_utils_int_multiply nodes
			#node Group Output
			group_output = _mn_utils_int_multiply.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Math.001
			math_001 = _mn_utils_int_multiply.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.operation = 'MULTIPLY'
			math_001.use_clamp = False
			
			#node Group Input
			group_input = _mn_utils_int_multiply.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			
			
			
			#Set locations
			group_output.location = (190.0, 0.0)
			math_001.location = (0.0, 0.0)
			group_input.location = (-235.15338134765625, -44.40943145751953)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			
			#initialize _mn_utils_int_multiply links
			#group_input.Value -> math_001.Value
			_mn_utils_int_multiply.links.new(group_input.outputs[0], math_001.inputs[0])
			#group_input.Value -> math_001.Value
			_mn_utils_int_multiply.links.new(group_input.outputs[1], math_001.inputs[1])
			#math_001.Value -> group_output.Value
			_mn_utils_int_multiply.links.new(math_001.outputs[0], group_output.inputs[0])
			return _mn_utils_int_multiply

		_mn_utils_int_multiply = _mn_utils_int_multiply_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".MN_utils_int_multiply", type = 'NODES')
		mod.node_group = _mn_utils_int_multiply
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_MN_utils_int_multiply.bl_idname)
			
def register():
	bpy.utils.register_class(_MN_utils_int_multiply)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_MN_utils_int_multiply)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
