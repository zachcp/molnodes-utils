bl_info = {
	"name" : "Sample Mix Vector",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Sample_Mix_Vector(bpy.types.Operator):
	bl_idname = "node.sample_mix_vector"
	bl_label = "Sample Mix Vector"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize sample_mix_vector node group
		def sample_mix_vector_node_group():
			sample_mix_vector = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Sample Mix Vector")

			sample_mix_vector.color_tag = 'GEOMETRY'
			sample_mix_vector.description = ""

			
			#sample_mix_vector interface
			#Socket Vector
			vector_socket = sample_mix_vector.interface.new_socket(name = "Vector", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			vector_socket.subtype = 'NONE'
			vector_socket.default_value = (0.0, 0.0, 0.0)
			vector_socket.min_value = -3.4028234663852886e+38
			vector_socket.max_value = 3.4028234663852886e+38
			vector_socket.attribute_domain = 'POINT'
			
			#Socket A
			a_socket = sample_mix_vector.interface.new_socket(name = "A", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			a_socket.attribute_domain = 'POINT'
			
			#Socket B
			b_socket = sample_mix_vector.interface.new_socket(name = "B", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			b_socket.attribute_domain = 'POINT'
			
			#Socket Factor
			factor_socket = sample_mix_vector.interface.new_socket(name = "Factor", in_out='INPUT', socket_type = 'NodeSocketFloat')
			factor_socket.subtype = 'FACTOR'
			factor_socket.default_value = 0.5
			factor_socket.min_value = 0.0
			factor_socket.max_value = 1.0
			factor_socket.attribute_domain = 'POINT'
			
			#Socket Position
			position_socket = sample_mix_vector.interface.new_socket(name = "Position", in_out='INPUT', socket_type = 'NodeSocketVector')
			position_socket.subtype = 'NONE'
			position_socket.default_value = (0.0, 0.0, 0.0)
			position_socket.min_value = -3.4028234663852886e+38
			position_socket.max_value = 3.4028234663852886e+38
			position_socket.attribute_domain = 'POINT'
			position_socket.hide_value = True
			
			#Socket Index
			index_socket = sample_mix_vector.interface.new_socket(name = "Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			index_socket.subtype = 'NONE'
			index_socket.default_value = 0
			index_socket.min_value = -2147483648
			index_socket.max_value = 2147483647
			index_socket.attribute_domain = 'POINT'
			
			
			#initialize sample_mix_vector nodes
			#node Group Output
			group_output = sample_mix_vector.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Sample Index.002
			sample_index_002 = sample_mix_vector.nodes.new("GeometryNodeSampleIndex")
			sample_index_002.name = "Sample Index.002"
			sample_index_002.clamp = False
			sample_index_002.data_type = 'FLOAT_VECTOR'
			sample_index_002.domain = 'POINT'
			
			#node Sample Index.003
			sample_index_003 = sample_mix_vector.nodes.new("GeometryNodeSampleIndex")
			sample_index_003.name = "Sample Index.003"
			sample_index_003.clamp = False
			sample_index_003.data_type = 'FLOAT_VECTOR'
			sample_index_003.domain = 'POINT'
			
			#node Group Input
			group_input = sample_mix_vector.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Mix.001
			mix_001 = sample_mix_vector.nodes.new("ShaderNodeMix")
			mix_001.name = "Mix.001"
			mix_001.blend_type = 'MIX'
			mix_001.clamp_factor = True
			mix_001.clamp_result = False
			mix_001.data_type = 'VECTOR'
			mix_001.factor_mode = 'UNIFORM'
			
			
			
			
			#Set locations
			group_output.location = (360.0, 180.0)
			sample_index_002.location = (-40.0, 260.0)
			sample_index_003.location = (-40.0, 60.0)
			group_input.location = (-492.72479248046875, -5.606773376464844)
			mix_001.location = (140.0, 260.0)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			sample_index_002.width, sample_index_002.height = 140.0, 100.0
			sample_index_003.width, sample_index_003.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			mix_001.width, mix_001.height = 140.0, 100.0
			
			#initialize sample_mix_vector links
			#group_input.A -> sample_index_002.Geometry
			sample_mix_vector.links.new(group_input.outputs[0], sample_index_002.inputs[0])
			#group_input.B -> sample_index_003.Geometry
			sample_mix_vector.links.new(group_input.outputs[1], sample_index_003.inputs[0])
			#group_input.Position -> sample_index_002.Value
			sample_mix_vector.links.new(group_input.outputs[3], sample_index_002.inputs[1])
			#group_input.Position -> sample_index_003.Value
			sample_mix_vector.links.new(group_input.outputs[3], sample_index_003.inputs[1])
			#sample_index_002.Value -> mix_001.A
			sample_mix_vector.links.new(sample_index_002.outputs[0], mix_001.inputs[4])
			#sample_index_003.Value -> mix_001.B
			sample_mix_vector.links.new(sample_index_003.outputs[0], mix_001.inputs[5])
			#group_input.Factor -> mix_001.Factor
			sample_mix_vector.links.new(group_input.outputs[2], mix_001.inputs[0])
			#mix_001.Result -> group_output.Vector
			sample_mix_vector.links.new(mix_001.outputs[1], group_output.inputs[0])
			#group_input.Index -> sample_index_002.Index
			sample_mix_vector.links.new(group_input.outputs[4], sample_index_002.inputs[2])
			#group_input.Index -> sample_index_003.Index
			sample_mix_vector.links.new(group_input.outputs[4], sample_index_003.inputs[2])
			return sample_mix_vector

		sample_mix_vector = sample_mix_vector_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Sample Mix Vector", type = 'NODES')
		mod.node_group = sample_mix_vector
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Sample_Mix_Vector.bl_idname)
			
def register():
	bpy.utils.register_class(Sample_Mix_Vector)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Sample_Mix_Vector)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
