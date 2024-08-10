bl_info = {
	"name" : "MN_animate_noise_field",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class MN_animate_noise_field(bpy.types.Operator):
	bl_idname = "node.mn_animate_noise_field"
	bl_label = "MN_animate_noise_field"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize mn_animate_noise_field node group
		def mn_animate_noise_field_node_group():
			mn_animate_noise_field = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "MN_animate_noise_field")

			mn_animate_noise_field.color_tag = 'TEXTURE'
			mn_animate_noise_field.description = ""

			
			#mn_animate_noise_field interface
			#Socket Noise
			noise_socket = mn_animate_noise_field.interface.new_socket(name = "Noise", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			noise_socket.subtype = 'NONE'
			noise_socket.default_value = (0.0, 0.0, 0.0)
			noise_socket.min_value = -3.4028234663852886e+38
			noise_socket.max_value = 3.4028234663852886e+38
			noise_socket.attribute_domain = 'POINT'
			
			#Socket Fac
			fac_socket = mn_animate_noise_field.interface.new_socket(name = "Fac", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			fac_socket.subtype = 'NONE'
			fac_socket.default_value = 0.0
			fac_socket.min_value = -3.4028234663852886e+38
			fac_socket.max_value = 3.4028234663852886e+38
			fac_socket.attribute_domain = 'POINT'
			
			#Socket Field
			field_socket = mn_animate_noise_field.interface.new_socket(name = "Field", in_out='INPUT', socket_type = 'NodeSocketVector')
			field_socket.subtype = 'NONE'
			field_socket.default_value = (0.0, 0.0, 0.0)
			field_socket.min_value = -3.4028234663852886e+38
			field_socket.max_value = 3.4028234663852886e+38
			field_socket.attribute_domain = 'POINT'
			field_socket.hide_value = True
			
			#Socket Amplitude
			amplitude_socket = mn_animate_noise_field.interface.new_socket(name = "Amplitude", in_out='INPUT', socket_type = 'NodeSocketFloat')
			amplitude_socket.subtype = 'NONE'
			amplitude_socket.default_value = 0.25
			amplitude_socket.min_value = -10000.0
			amplitude_socket.max_value = 10000.0
			amplitude_socket.attribute_domain = 'POINT'
			
			#Socket Animate
			animate_socket = mn_animate_noise_field.interface.new_socket(name = "Animate", in_out='INPUT', socket_type = 'NodeSocketFloat')
			animate_socket.subtype = 'NONE'
			animate_socket.default_value = 0.0
			animate_socket.min_value = -1000.0
			animate_socket.max_value = 1000.0
			animate_socket.attribute_domain = 'POINT'
			
			#Socket Scale
			scale_socket = mn_animate_noise_field.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
			scale_socket.subtype = 'NONE'
			scale_socket.default_value = 1.0
			scale_socket.min_value = -1000.0
			scale_socket.max_value = 1000.0
			scale_socket.attribute_domain = 'POINT'
			
			#Socket Detail
			detail_socket = mn_animate_noise_field.interface.new_socket(name = "Detail", in_out='INPUT', socket_type = 'NodeSocketFloat')
			detail_socket.subtype = 'NONE'
			detail_socket.default_value = 3.0
			detail_socket.min_value = 0.0
			detail_socket.max_value = 15.0
			detail_socket.attribute_domain = 'POINT'
			
			#Socket Roughness
			roughness_socket = mn_animate_noise_field.interface.new_socket(name = "Roughness", in_out='INPUT', socket_type = 'NodeSocketFloat')
			roughness_socket.subtype = 'FACTOR'
			roughness_socket.default_value = 1.0
			roughness_socket.min_value = 0.0
			roughness_socket.max_value = 1.0
			roughness_socket.attribute_domain = 'POINT'
			
			#Socket Distortion
			distortion_socket = mn_animate_noise_field.interface.new_socket(name = "Distortion", in_out='INPUT', socket_type = 'NodeSocketFloat')
			distortion_socket.subtype = 'NONE'
			distortion_socket.default_value = 0.0
			distortion_socket.min_value = -1000.0
			distortion_socket.max_value = 1000.0
			distortion_socket.attribute_domain = 'POINT'
			
			
			#initialize mn_animate_noise_field nodes
			#node Vector Math
			vector_math = mn_animate_noise_field.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.operation = 'SUBTRACT'
			#Vector_001
			vector_math.inputs[1].default_value = (0.5, 0.5, 0.5)
			
			#node Vector Math.001
			vector_math_001 = mn_animate_noise_field.nodes.new("ShaderNodeVectorMath")
			vector_math_001.name = "Vector Math.001"
			vector_math_001.operation = 'SCALE'
			
			#node Group Input
			group_input = mn_animate_noise_field.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Group Output
			group_output = mn_animate_noise_field.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Noise Texture
			noise_texture = mn_animate_noise_field.nodes.new("ShaderNodeTexNoise")
			noise_texture.name = "Noise Texture"
			noise_texture.noise_dimensions = '4D'
			noise_texture.noise_type = 'FBM'
			noise_texture.normalize = True
			#Lacunarity
			noise_texture.inputs[5].default_value = 2.0
			
			#node Clamp
			clamp = mn_animate_noise_field.nodes.new("ShaderNodeClamp")
			clamp.name = "Clamp"
			clamp.hide = True
			clamp.clamp_type = 'MINMAX'
			#Min
			clamp.inputs[1].default_value = 0.0
			#Max
			clamp.inputs[2].default_value = 1.0
			
			
			
			
			#Set locations
			vector_math.location = (0.0, 0.0)
			vector_math_001.location = (160.0, 0.0)
			group_input.location = (-360.0, -0.0)
			group_output.location = (340.0, 0.0)
			noise_texture.location = (-160.0, 0.0)
			clamp.location = (-160.0, -300.0)
			
			#Set dimensions
			vector_math.width, vector_math.height = 140.0, 100.0
			vector_math_001.width, vector_math_001.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			noise_texture.width, noise_texture.height = 140.0, 100.0
			clamp.width, clamp.height = 140.0, 100.0
			
			#initialize mn_animate_noise_field links
			#vector_math_001.Vector -> group_output.Noise
			mn_animate_noise_field.links.new(vector_math_001.outputs[0], group_output.inputs[0])
			#noise_texture.Color -> vector_math.Vector
			mn_animate_noise_field.links.new(noise_texture.outputs[1], vector_math.inputs[0])
			#vector_math.Vector -> vector_math_001.Vector
			mn_animate_noise_field.links.new(vector_math.outputs[0], vector_math_001.inputs[0])
			#group_input.Amplitude -> vector_math_001.Scale
			mn_animate_noise_field.links.new(group_input.outputs[1], vector_math_001.inputs[3])
			#group_input.Animate -> noise_texture.W
			mn_animate_noise_field.links.new(group_input.outputs[2], noise_texture.inputs[1])
			#group_input.Scale -> noise_texture.Scale
			mn_animate_noise_field.links.new(group_input.outputs[3], noise_texture.inputs[2])
			#group_input.Detail -> noise_texture.Detail
			mn_animate_noise_field.links.new(group_input.outputs[4], noise_texture.inputs[3])
			#group_input.Distortion -> noise_texture.Distortion
			mn_animate_noise_field.links.new(group_input.outputs[6], noise_texture.inputs[8])
			#noise_texture.Fac -> group_output.Fac
			mn_animate_noise_field.links.new(noise_texture.outputs[0], group_output.inputs[1])
			#group_input.Field -> noise_texture.Vector
			mn_animate_noise_field.links.new(group_input.outputs[0], noise_texture.inputs[0])
			#group_input.Roughness -> clamp.Value
			mn_animate_noise_field.links.new(group_input.outputs[5], clamp.inputs[0])
			#clamp.Result -> noise_texture.Roughness
			mn_animate_noise_field.links.new(clamp.outputs[0], noise_texture.inputs[4])
			return mn_animate_noise_field

		mn_animate_noise_field = mn_animate_noise_field_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "MN_animate_noise_field", type = 'NODES')
		mod.node_group = mn_animate_noise_field
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(MN_animate_noise_field.bl_idname)
			
def register():
	bpy.utils.register_class(MN_animate_noise_field)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(MN_animate_noise_field)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
