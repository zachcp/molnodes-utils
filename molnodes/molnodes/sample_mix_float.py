bl_info = {
	"name" : "Sample Mix Float",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Sample_Mix_Float(bpy.types.Operator):
	bl_idname = "node.sample_mix_float"
	bl_label = "Sample Mix Float"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize sample_mix_float node group
		def sample_mix_float_node_group():
			sample_mix_float = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Sample Mix Float")

			sample_mix_float.color_tag = 'GEOMETRY'
			sample_mix_float.description = ""

			
			#sample_mix_float interface
			#Socket Value
			value_socket = sample_mix_float.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			value_socket.default_value = 0.0
			value_socket.min_value = -3.4028234663852886e+38
			value_socket.max_value = 3.4028234663852886e+38
			value_socket.subtype = 'NONE'
			value_socket.attribute_domain = 'POINT'
			
			#Socket A
			a_socket = sample_mix_float.interface.new_socket(name = "A", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			a_socket.attribute_domain = 'POINT'
			
			#Socket B
			b_socket = sample_mix_float.interface.new_socket(name = "B", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			b_socket.attribute_domain = 'POINT'
			
			#Socket Factor
			factor_socket = sample_mix_float.interface.new_socket(name = "Factor", in_out='INPUT', socket_type = 'NodeSocketFloat')
			factor_socket.default_value = 0.5
			factor_socket.min_value = 0.0
			factor_socket.max_value = 1.0
			factor_socket.subtype = 'FACTOR'
			factor_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_1 = sample_mix_float.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket_1.default_value = 0.0
			value_socket_1.min_value = -3.4028234663852886e+38
			value_socket_1.max_value = 3.4028234663852886e+38
			value_socket_1.subtype = 'NONE'
			value_socket_1.attribute_domain = 'POINT'
			value_socket_1.hide_value = True
			
			#Socket Index
			index_socket = sample_mix_float.interface.new_socket(name = "Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			index_socket.default_value = 0
			index_socket.min_value = -2147483648
			index_socket.max_value = 2147483647
			index_socket.subtype = 'NONE'
			index_socket.attribute_domain = 'POINT'
			
			
			#initialize sample_mix_float nodes
			#node Group Output
			group_output = sample_mix_float.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Sample Index.002
			sample_index_002 = sample_mix_float.nodes.new("GeometryNodeSampleIndex")
			sample_index_002.name = "Sample Index.002"
			sample_index_002.clamp = False
			sample_index_002.data_type = 'FLOAT'
			sample_index_002.domain = 'POINT'
			
			#node Sample Index.003
			sample_index_003 = sample_mix_float.nodes.new("GeometryNodeSampleIndex")
			sample_index_003.name = "Sample Index.003"
			sample_index_003.clamp = False
			sample_index_003.data_type = 'FLOAT'
			sample_index_003.domain = 'POINT'
			
			#node Group Input
			group_input = sample_mix_float.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Mix
			mix = sample_mix_float.nodes.new("ShaderNodeMix")
			mix.name = "Mix"
			mix.blend_type = 'MIX'
			mix.clamp_factor = True
			mix.clamp_result = False
			mix.data_type = 'FLOAT'
			mix.factor_mode = 'UNIFORM'
			
			
			
			
			#Set locations
			group_output.location = (360.0, 180.0)
			sample_index_002.location = (-40.0, 260.0)
			sample_index_003.location = (-40.0, 60.0)
			group_input.location = (-492.72479248046875, -5.606773376464844)
			mix.location = (160.8731689453125, 214.3348846435547)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			sample_index_002.width, sample_index_002.height = 140.0, 100.0
			sample_index_003.width, sample_index_003.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			mix.width, mix.height = 140.0, 100.0
			
			#initialize sample_mix_float links
			#group_input.A -> sample_index_002.Geometry
			sample_mix_float.links.new(group_input.outputs[0], sample_index_002.inputs[0])
			#group_input.B -> sample_index_003.Geometry
			sample_mix_float.links.new(group_input.outputs[1], sample_index_003.inputs[0])
			#group_input.Value -> sample_index_002.Value
			sample_mix_float.links.new(group_input.outputs[3], sample_index_002.inputs[1])
			#group_input.Value -> sample_index_003.Value
			sample_mix_float.links.new(group_input.outputs[3], sample_index_003.inputs[1])
			#sample_index_002.Value -> mix.A
			sample_mix_float.links.new(sample_index_002.outputs[0], mix.inputs[2])
			#sample_index_003.Value -> mix.B
			sample_mix_float.links.new(sample_index_003.outputs[0], mix.inputs[3])
			#group_input.Factor -> mix.Factor
			sample_mix_float.links.new(group_input.outputs[2], mix.inputs[0])
			#mix.Result -> group_output.Value
			sample_mix_float.links.new(mix.outputs[0], group_output.inputs[0])
			#group_input.Index -> sample_index_002.Index
			sample_mix_float.links.new(group_input.outputs[4], sample_index_002.inputs[2])
			#group_input.Index -> sample_index_003.Index
			sample_mix_float.links.new(group_input.outputs[4], sample_index_003.inputs[2])
			return sample_mix_float

		sample_mix_float = sample_mix_float_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Sample Mix Float", type = 'NODES')
		mod.node_group = sample_mix_float
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Sample_Mix_Float.bl_idname)
			
def register():
	bpy.utils.register_class(Sample_Mix_Float)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Sample_Mix_Float)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
