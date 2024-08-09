bl_info = {
	"name" : ".field_offset_bool",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _field_offset_bool(bpy.types.Operator):
	bl_idname = "node._field_offset_bool"
	bl_label = ".field_offset_bool"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _field_offset_bool node group
		def _field_offset_bool_node_group():
			_field_offset_bool = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".field_offset_bool")

			_field_offset_bool.color_tag = 'NONE'
			_field_offset_bool.description = ""

			
			#_field_offset_bool interface
			#Socket Boolean
			boolean_socket = _field_offset_bool.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket.attribute_domain = 'POINT'
			
			#Socket Boolean
			boolean_socket_1 = _field_offset_bool.interface.new_socket(name = "Boolean", in_out='INPUT', socket_type = 'NodeSocketBool')
			boolean_socket_1.attribute_domain = 'POINT'
			boolean_socket_1.hide_value = True
			
			#Socket Offset
			offset_socket = _field_offset_bool.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket.subtype = 'NONE'
			offset_socket.default_value = 0
			offset_socket.min_value = -2147483648
			offset_socket.max_value = 2147483647
			offset_socket.attribute_domain = 'POINT'
			
			
			#initialize _field_offset_bool nodes
			#node Group Input
			group_input = _field_offset_bool.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Index
			index = _field_offset_bool.nodes.new("GeometryNodeInputIndex")
			index.name = "Index"
			
			#node Math.001
			math_001 = _field_offset_bool.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.operation = 'ADD'
			math_001.use_clamp = False
			
			#node Evaluate at Index.001
			evaluate_at_index_001 = _field_offset_bool.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001.name = "Evaluate at Index.001"
			evaluate_at_index_001.data_type = 'BOOLEAN'
			evaluate_at_index_001.domain = 'POINT'
			
			#node Group Output
			group_output = _field_offset_bool.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			
			
			
			#Set locations
			group_input.location = (-417.64404296875, 0.0)
			index.location = (-420.0, -120.0)
			math_001.location = (-220.0, -120.0)
			evaluate_at_index_001.location = (-220.0, 40.0)
			group_output.location = (-60.0, 40.0)
			
			#Set dimensions
			group_input.width, group_input.height = 140.0, 100.0
			index.width, index.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			evaluate_at_index_001.width, evaluate_at_index_001.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			
			#initialize _field_offset_bool links
			#group_input.Offset -> math_001.Value
			_field_offset_bool.links.new(group_input.outputs[1], math_001.inputs[0])
			#math_001.Value -> evaluate_at_index_001.Index
			_field_offset_bool.links.new(math_001.outputs[0], evaluate_at_index_001.inputs[0])
			#group_input.Boolean -> evaluate_at_index_001.Value
			_field_offset_bool.links.new(group_input.outputs[0], evaluate_at_index_001.inputs[1])
			#evaluate_at_index_001.Value -> group_output.Boolean
			_field_offset_bool.links.new(evaluate_at_index_001.outputs[0], group_output.inputs[0])
			#index.Index -> math_001.Value
			_field_offset_bool.links.new(index.outputs[0], math_001.inputs[1])
			return _field_offset_bool

		_field_offset_bool = _field_offset_bool_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".field_offset_bool", type = 'NODES')
		mod.node_group = _field_offset_bool
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_field_offset_bool.bl_idname)
			
def register():
	bpy.utils.register_class(_field_offset_bool)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_field_offset_bool)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
