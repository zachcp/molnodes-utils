bl_info = {
	"name" : ".field_offset_vec",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _field_offset_vec(bpy.types.Operator):
	bl_idname = "node._field_offset_vec"
	bl_label = ".field_offset_vec"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _field_offset_vec node group
		def _field_offset_vec_node_group():
			_field_offset_vec = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".field_offset_vec")

			_field_offset_vec.color_tag = 'NONE'
			_field_offset_vec.description = ""

			
			#_field_offset_vec interface
			#Socket Field
			field_socket = _field_offset_vec.interface.new_socket(name = "Field", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			field_socket.subtype = 'NONE'
			field_socket.default_value = (0.0, 0.0, 0.0)
			field_socket.min_value = -3.4028234663852886e+38
			field_socket.max_value = 3.4028234663852886e+38
			field_socket.attribute_domain = 'POINT'
			
			#Socket Field
			field_socket_1 = _field_offset_vec.interface.new_socket(name = "Field", in_out='INPUT', socket_type = 'NodeSocketVector')
			field_socket_1.subtype = 'NONE'
			field_socket_1.default_value = (0.0, 0.0, 0.0)
			field_socket_1.min_value = -3.4028234663852886e+38
			field_socket_1.max_value = 3.4028234663852886e+38
			field_socket_1.attribute_domain = 'POINT'
			field_socket_1.hide_value = True
			
			#Socket Offset
			offset_socket = _field_offset_vec.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket.subtype = 'NONE'
			offset_socket.default_value = 0
			offset_socket.min_value = -2147483648
			offset_socket.max_value = 2147483647
			offset_socket.attribute_domain = 'POINT'
			
			
			#initialize _field_offset_vec nodes
			#node Group Input
			group_input = _field_offset_vec.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Evaluate at Index
			evaluate_at_index = _field_offset_vec.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index.name = "Evaluate at Index"
			evaluate_at_index.data_type = 'FLOAT_VECTOR'
			evaluate_at_index.domain = 'POINT'
			
			#node Group Output
			group_output = _field_offset_vec.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Math.001
			math_001 = _field_offset_vec.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.operation = 'ADD'
			math_001.use_clamp = False
			
			#node Index
			index = _field_offset_vec.nodes.new("GeometryNodeInputIndex")
			index.name = "Index"
			
			
			
			
			#Set locations
			group_input.location = (-417.64404296875, 0.0)
			evaluate_at_index.location = (-220.0, 100.0)
			group_output.location = (20.0, 20.0)
			math_001.location = (-220.0, -80.0)
			index.location = (-400.0, -180.0)
			
			#Set dimensions
			group_input.width, group_input.height = 140.0, 100.0
			evaluate_at_index.width, evaluate_at_index.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			index.width, index.height = 140.0, 100.0
			
			#initialize _field_offset_vec links
			#math_001.Value -> evaluate_at_index.Index
			_field_offset_vec.links.new(math_001.outputs[0], evaluate_at_index.inputs[0])
			#group_input.Field -> evaluate_at_index.Value
			_field_offset_vec.links.new(group_input.outputs[0], evaluate_at_index.inputs[1])
			#group_input.Offset -> math_001.Value
			_field_offset_vec.links.new(group_input.outputs[1], math_001.inputs[0])
			#evaluate_at_index.Value -> group_output.Field
			_field_offset_vec.links.new(evaluate_at_index.outputs[0], group_output.inputs[0])
			#index.Index -> math_001.Value
			_field_offset_vec.links.new(index.outputs[0], math_001.inputs[1])
			return _field_offset_vec

		_field_offset_vec = _field_offset_vec_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".field_offset_vec", type = 'NODES')
		mod.node_group = _field_offset_vec
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_field_offset_vec.bl_idname)
			
def register():
	bpy.utils.register_class(_field_offset_vec)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_field_offset_vec)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
