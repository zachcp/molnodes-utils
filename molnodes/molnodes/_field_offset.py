bl_info = {
	"name" : ".field_offset",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _field_offset(bpy.types.Operator):
	bl_idname = "node._field_offset"
	bl_label = ".field_offset"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _field_offset node group
		def _field_offset_node_group():
			_field_offset = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".field_offset")

			_field_offset.color_tag = 'NONE'
			_field_offset.description = ""

			
			#_field_offset interface
			#Socket Field
			field_socket = _field_offset.interface.new_socket(name = "Field", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			field_socket.default_value = (0.0, 0.0, 0.0)
			field_socket.min_value = -3.4028234663852886e+38
			field_socket.max_value = 3.4028234663852886e+38
			field_socket.subtype = 'NONE'
			field_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket = _field_offset.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			value_socket.default_value = False
			value_socket.attribute_domain = 'POINT'
			
			#Socket Field
			field_socket_1 = _field_offset.interface.new_socket(name = "Field", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			field_socket_1.default_value = 0
			field_socket_1.min_value = -2147483648
			field_socket_1.max_value = 2147483647
			field_socket_1.subtype = 'NONE'
			field_socket_1.attribute_domain = 'POINT'
			
			#Socket Field
			field_socket_2 = _field_offset.interface.new_socket(name = "Field", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			field_socket_2.default_value = 0.0
			field_socket_2.min_value = -3.4028234663852886e+38
			field_socket_2.max_value = 3.4028234663852886e+38
			field_socket_2.subtype = 'NONE'
			field_socket_2.attribute_domain = 'POINT'
			
			#Socket Field
			field_socket_3 = _field_offset.interface.new_socket(name = "Field", in_out='INPUT', socket_type = 'NodeSocketVector')
			field_socket_3.default_value = (0.0, 0.0, 0.0)
			field_socket_3.min_value = -3.4028234663852886e+38
			field_socket_3.max_value = 3.4028234663852886e+38
			field_socket_3.subtype = 'NONE'
			field_socket_3.attribute_domain = 'POINT'
			field_socket_3.hide_value = True
			
			#Socket Value
			value_socket_1 = _field_offset.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketBool')
			value_socket_1.default_value = False
			value_socket_1.attribute_domain = 'POINT'
			value_socket_1.hide_value = True
			
			#Socket Field
			field_socket_4 = _field_offset.interface.new_socket(name = "Field", in_out='INPUT', socket_type = 'NodeSocketInt')
			field_socket_4.default_value = 0
			field_socket_4.min_value = -2147483648
			field_socket_4.max_value = 2147483647
			field_socket_4.subtype = 'NONE'
			field_socket_4.attribute_domain = 'POINT'
			field_socket_4.hide_value = True
			
			#Socket Field
			field_socket_5 = _field_offset.interface.new_socket(name = "Field", in_out='INPUT', socket_type = 'NodeSocketFloat')
			field_socket_5.default_value = 0.0
			field_socket_5.min_value = -3.4028234663852886e+38
			field_socket_5.max_value = 3.4028234663852886e+38
			field_socket_5.subtype = 'NONE'
			field_socket_5.attribute_domain = 'POINT'
			field_socket_5.hide_value = True
			
			#Socket Offset
			offset_socket = _field_offset.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket.default_value = 0
			offset_socket.min_value = -2147483648
			offset_socket.max_value = 2147483647
			offset_socket.subtype = 'NONE'
			offset_socket.attribute_domain = 'POINT'
			
			
			#initialize _field_offset nodes
			#node Group Output
			group_output = _field_offset.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Math.001
			math_001 = _field_offset.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.operation = 'ADD'
			math_001.use_clamp = False
			
			#node Evaluate at Index
			evaluate_at_index = _field_offset.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index.name = "Evaluate at Index"
			evaluate_at_index.data_type = 'FLOAT_VECTOR'
			evaluate_at_index.domain = 'POINT'
			
			#node Group Input
			group_input = _field_offset.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Evaluate at Index.001
			evaluate_at_index_001 = _field_offset.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001.name = "Evaluate at Index.001"
			evaluate_at_index_001.data_type = 'BOOLEAN'
			evaluate_at_index_001.domain = 'POINT'
			
			#node Index
			index = _field_offset.nodes.new("GeometryNodeInputIndex")
			index.name = "Index"
			
			#node Evaluate at Index.002
			evaluate_at_index_002 = _field_offset.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_002.name = "Evaluate at Index.002"
			evaluate_at_index_002.data_type = 'INT'
			evaluate_at_index_002.domain = 'POINT'
			
			#node Evaluate at Index.003
			evaluate_at_index_003 = _field_offset.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_003.name = "Evaluate at Index.003"
			evaluate_at_index_003.data_type = 'FLOAT'
			evaluate_at_index_003.domain = 'POINT'
			
			
			
			
			#Set locations
			group_output.location = (407.6440124511719, 0.0)
			math_001.location = (0.5235366821289062, 15.3753662109375)
			evaluate_at_index.location = (217.64404296875, 102.376708984375)
			group_input.location = (-417.64404296875, 0.0)
			evaluate_at_index_001.location = (220.0, -60.0)
			index.location = (-260.0, -40.0)
			evaluate_at_index_002.location = (220.0, -220.0)
			evaluate_at_index_003.location = (220.0, -380.0)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			evaluate_at_index.width, evaluate_at_index.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			evaluate_at_index_001.width, evaluate_at_index_001.height = 140.0, 100.0
			index.width, index.height = 140.0, 100.0
			evaluate_at_index_002.width, evaluate_at_index_002.height = 140.0, 100.0
			evaluate_at_index_003.width, evaluate_at_index_003.height = 140.0, 100.0
			
			#initialize _field_offset links
			#index.Index -> math_001.Value
			_field_offset.links.new(index.outputs[0], math_001.inputs[0])
			#math_001.Value -> evaluate_at_index.Index
			_field_offset.links.new(math_001.outputs[0], evaluate_at_index.inputs[0])
			#group_input.Field -> evaluate_at_index.Value
			_field_offset.links.new(group_input.outputs[0], evaluate_at_index.inputs[1])
			#group_input.Offset -> math_001.Value
			_field_offset.links.new(group_input.outputs[4], math_001.inputs[1])
			#evaluate_at_index.Value -> group_output.Field
			_field_offset.links.new(evaluate_at_index.outputs[0], group_output.inputs[0])
			#math_001.Value -> evaluate_at_index_001.Index
			_field_offset.links.new(math_001.outputs[0], evaluate_at_index_001.inputs[0])
			#group_input.Value -> evaluate_at_index_001.Value
			_field_offset.links.new(group_input.outputs[1], evaluate_at_index_001.inputs[1])
			#evaluate_at_index_001.Value -> group_output.Value
			_field_offset.links.new(evaluate_at_index_001.outputs[0], group_output.inputs[1])
			#math_001.Value -> evaluate_at_index_002.Index
			_field_offset.links.new(math_001.outputs[0], evaluate_at_index_002.inputs[0])
			#group_input.Field -> evaluate_at_index_002.Value
			_field_offset.links.new(group_input.outputs[2], evaluate_at_index_002.inputs[1])
			#evaluate_at_index_002.Value -> group_output.Field
			_field_offset.links.new(evaluate_at_index_002.outputs[0], group_output.inputs[2])
			#math_001.Value -> evaluate_at_index_003.Index
			_field_offset.links.new(math_001.outputs[0], evaluate_at_index_003.inputs[0])
			#group_input.Field -> evaluate_at_index_003.Value
			_field_offset.links.new(group_input.outputs[3], evaluate_at_index_003.inputs[1])
			#evaluate_at_index_003.Value -> group_output.Field
			_field_offset.links.new(evaluate_at_index_003.outputs[0], group_output.inputs[3])
			return _field_offset

		_field_offset = _field_offset_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".field_offset", type = 'NODES')
		mod.node_group = _field_offset
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_field_offset.bl_idname)
			
def register():
	bpy.utils.register_class(_field_offset)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_field_offset)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
