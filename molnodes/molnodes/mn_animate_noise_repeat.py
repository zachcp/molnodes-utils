bl_info = {
	"name" : "MN_animate_noise_repeat",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class MN_animate_noise_repeat(bpy.types.Operator):
	bl_idname = "node.mn_animate_noise_repeat"
	bl_label = "MN_animate_noise_repeat"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize mn_animate_noise_repeat node group
		def mn_animate_noise_repeat_node_group():
			mn_animate_noise_repeat = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "MN_animate_noise_repeat")

			mn_animate_noise_repeat.color_tag = 'TEXTURE'
			mn_animate_noise_repeat.description = ""

			
			#mn_animate_noise_repeat interface
			#Socket Noise Float
			noise_float_socket = mn_animate_noise_repeat.interface.new_socket(name = "Noise Float", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			noise_float_socket.default_value = 0.0
			noise_float_socket.min_value = -3.4028234663852886e+38
			noise_float_socket.max_value = 3.4028234663852886e+38
			noise_float_socket.subtype = 'NONE'
			noise_float_socket.attribute_domain = 'POINT'
			
			#Socket Noise Vector
			noise_vector_socket = mn_animate_noise_repeat.interface.new_socket(name = "Noise Vector", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			noise_vector_socket.default_value = (0.0, 0.0, 0.0)
			noise_vector_socket.min_value = -3.4028234663852886e+38
			noise_vector_socket.max_value = 3.4028234663852886e+38
			noise_vector_socket.subtype = 'NONE'
			noise_vector_socket.attribute_domain = 'POINT'
			
			#Socket Amplitude
			amplitude_socket = mn_animate_noise_repeat.interface.new_socket(name = "Amplitude", in_out='INPUT', socket_type = 'NodeSocketFloat')
			amplitude_socket.default_value = 1.0
			amplitude_socket.min_value = -10000.0
			amplitude_socket.max_value = 10000.0
			amplitude_socket.subtype = 'NONE'
			amplitude_socket.attribute_domain = 'POINT'
			
			#Socket Detail
			detail_socket = mn_animate_noise_repeat.interface.new_socket(name = "Detail", in_out='INPUT', socket_type = 'NodeSocketFloat')
			detail_socket.default_value = 0.5
			detail_socket.min_value = 0.0
			detail_socket.max_value = 15.0
			detail_socket.subtype = 'NONE'
			detail_socket.attribute_domain = 'POINT'
			
			#Socket Roughness
			roughness_socket = mn_animate_noise_repeat.interface.new_socket(name = "Roughness", in_out='INPUT', socket_type = 'NodeSocketFloat')
			roughness_socket.default_value = 0.5
			roughness_socket.min_value = 0.0
			roughness_socket.max_value = 1.0
			roughness_socket.subtype = 'FACTOR'
			roughness_socket.attribute_domain = 'POINT'
			
			#Socket Distortion
			distortion_socket = mn_animate_noise_repeat.interface.new_socket(name = "Distortion", in_out='INPUT', socket_type = 'NodeSocketFloat')
			distortion_socket.default_value = 0.0
			distortion_socket.min_value = -1000.0
			distortion_socket.max_value = 1000.0
			distortion_socket.subtype = 'NONE'
			distortion_socket.attribute_domain = 'POINT'
			
			#Socket Vector
			vector_socket = mn_animate_noise_repeat.interface.new_socket(name = "Vector", in_out='INPUT', socket_type = 'NodeSocketVector')
			vector_socket.default_value = (0.0, 0.0, 0.0)
			vector_socket.min_value = -10000.0
			vector_socket.max_value = 10000.0
			vector_socket.subtype = 'NONE'
			vector_socket.default_attribute_name = "position"
			vector_socket.attribute_domain = 'POINT'
			vector_socket.hide_value = True
			
			#Socket Speed
			speed_socket = mn_animate_noise_repeat.interface.new_socket(name = "Speed", in_out='INPUT', socket_type = 'NodeSocketFloat')
			speed_socket.default_value = 0.5
			speed_socket.min_value = -10000.0
			speed_socket.max_value = 10000.0
			speed_socket.subtype = 'NONE'
			speed_socket.attribute_domain = 'POINT'
			
			#Socket Animate 0..1
			animate_0__1_socket = mn_animate_noise_repeat.interface.new_socket(name = "Animate 0..1", in_out='INPUT', socket_type = 'NodeSocketFloat')
			animate_0__1_socket.default_value = 0.5
			animate_0__1_socket.min_value = -10000.0
			animate_0__1_socket.max_value = 10000.0
			animate_0__1_socket.subtype = 'NONE'
			animate_0__1_socket.attribute_domain = 'POINT'
			
			
			#initialize mn_animate_noise_repeat nodes
			#node Combine XYZ
			combine_xyz = mn_animate_noise_repeat.nodes.new("ShaderNodeCombineXYZ")
			combine_xyz.name = "Combine XYZ"
			#Y
			combine_xyz.inputs[1].default_value = 0.0
			#Z
			combine_xyz.inputs[2].default_value = 0.0
			
			#node Vector Math.003
			vector_math_003 = mn_animate_noise_repeat.nodes.new("ShaderNodeVectorMath")
			vector_math_003.name = "Vector Math.003"
			vector_math_003.operation = 'SCALE'
			
			#node Math
			math = mn_animate_noise_repeat.nodes.new("ShaderNodeMath")
			math.name = "Math"
			math.operation = 'DIVIDE'
			math.use_clamp = False
			#Value
			math.inputs[0].default_value = 6.2831854820251465
			
			#node Math.003
			math_003 = mn_animate_noise_repeat.nodes.new("ShaderNodeMath")
			math_003.name = "Math.003"
			math_003.operation = 'COSINE'
			math_003.use_clamp = False
			
			#node Math.002
			math_002 = mn_animate_noise_repeat.nodes.new("ShaderNodeMath")
			math_002.name = "Math.002"
			math_002.operation = 'SINE'
			math_002.use_clamp = False
			
			#node Math.004
			math_004 = mn_animate_noise_repeat.nodes.new("ShaderNodeMath")
			math_004.name = "Math.004"
			math_004.operation = 'SINE'
			math_004.use_clamp = False
			
			#node Separate XYZ
			separate_xyz = mn_animate_noise_repeat.nodes.new("ShaderNodeSeparateXYZ")
			separate_xyz.name = "Separate XYZ"
			
			#node Math.005
			math_005 = mn_animate_noise_repeat.nodes.new("ShaderNodeMath")
			math_005.name = "Math.005"
			math_005.operation = 'COSINE'
			math_005.use_clamp = False
			
			#node Math.001
			math_001 = mn_animate_noise_repeat.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.operation = 'MULTIPLY'
			math_001.use_clamp = False
			
			#node Value.001
			value_001 = mn_animate_noise_repeat.nodes.new("ShaderNodeValue")
			value_001.name = "Value.001"
			
			value_001.outputs[0].default_value = 0.20000000298023224
			#node Vector Math.002
			vector_math_002 = mn_animate_noise_repeat.nodes.new("ShaderNodeVectorMath")
			vector_math_002.name = "Vector Math.002"
			vector_math_002.operation = 'ADD'
			
			#node Group Output
			group_output = mn_animate_noise_repeat.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Math.006
			math_006 = mn_animate_noise_repeat.nodes.new("ShaderNodeMath")
			math_006.name = "Math.006"
			math_006.operation = 'MULTIPLY'
			math_006.use_clamp = False
			
			#node Vector Math
			vector_math = mn_animate_noise_repeat.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.operation = 'SCALE'
			
			#node Map Range
			map_range = mn_animate_noise_repeat.nodes.new("ShaderNodeMapRange")
			map_range.name = "Map Range"
			map_range.clamp = True
			map_range.data_type = 'FLOAT'
			map_range.interpolation_type = 'LINEAR'
			#From Min
			map_range.inputs[1].default_value = 0.0
			#From Max
			map_range.inputs[2].default_value = 1.0
			#To Min
			map_range.inputs[3].default_value = -1.0
			#To Max
			map_range.inputs[4].default_value = 1.0
			
			#node Map Range.001
			map_range_001 = mn_animate_noise_repeat.nodes.new("ShaderNodeMapRange")
			map_range_001.name = "Map Range.001"
			map_range_001.clamp = True
			map_range_001.data_type = 'FLOAT_VECTOR'
			map_range_001.interpolation_type = 'LINEAR'
			#From_Min_FLOAT3
			map_range_001.inputs[7].default_value = (0.0, 0.0, 0.0)
			#From_Max_FLOAT3
			map_range_001.inputs[8].default_value = (1.0, 1.0, 1.0)
			#To_Min_FLOAT3
			map_range_001.inputs[9].default_value = (-1.0, -1.0, -1.0)
			#To_Max_FLOAT3
			map_range_001.inputs[10].default_value = (1.0, 1.0, 1.0)
			
			#node Noise Texture
			noise_texture = mn_animate_noise_repeat.nodes.new("ShaderNodeTexNoise")
			noise_texture.name = "Noise Texture"
			noise_texture.noise_dimensions = '4D'
			noise_texture.noise_type = 'FBM'
			noise_texture.normalize = True
			#Lacunarity
			noise_texture.inputs[5].default_value = 2.0
			
			#node Combine XYZ.001
			combine_xyz_001 = mn_animate_noise_repeat.nodes.new("ShaderNodeCombineXYZ")
			combine_xyz_001.name = "Combine XYZ.001"
			
			#node Value
			value = mn_animate_noise_repeat.nodes.new("ShaderNodeValue")
			value.name = "Value"
			
			value.outputs[0].default_value = 4.0
			#node Random Value
			random_value = mn_animate_noise_repeat.nodes.new("FunctionNodeRandomValue")
			random_value.name = "Random Value"
			random_value.data_type = 'FLOAT_VECTOR'
			#Min
			random_value.inputs[0].default_value = (-10.0, -10.0, -10.0)
			#Max
			random_value.inputs[1].default_value = (-1.0, 10.0, 10.0)
			#Seed
			random_value.inputs[8].default_value = 0
			
			#node Math.009
			math_009 = mn_animate_noise_repeat.nodes.new("ShaderNodeMath")
			math_009.name = "Math.009"
			math_009.operation = 'MULTIPLY'
			math_009.use_clamp = False
			
			#node Vector Math.001
			vector_math_001 = mn_animate_noise_repeat.nodes.new("ShaderNodeVectorMath")
			vector_math_001.name = "Vector Math.001"
			vector_math_001.operation = 'ADD'
			
			#node Reroute
			reroute = mn_animate_noise_repeat.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Group Input
			group_input = mn_animate_noise_repeat.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Clamp
			clamp = mn_animate_noise_repeat.nodes.new("ShaderNodeClamp")
			clamp.name = "Clamp"
			clamp.hide = True
			clamp.clamp_type = 'MINMAX'
			#Min
			clamp.inputs[1].default_value = 0.0
			#Max
			clamp.inputs[2].default_value = 1.0
			
			
			
			
			#Set locations
			combine_xyz.location = (0.0001220703125, 110.0)
			vector_math_003.location = (320.0001220703125, 190.0)
			math.location = (160.0, 40.0)
			math_003.location = (700.0, 240.0)
			math_002.location = (700.0, 380.0)
			math_004.location = (700.0, 100.0)
			separate_xyz.location = (480.0001220703125, 190.0)
			math_005.location = (700.0, -40.0)
			math_001.location = (164.15023803710938, -158.06997680664062)
			value_001.location = (-480.0, -320.0)
			vector_math_002.location = (160.0001220703125, 190.0)
			group_output.location = (1768.860595703125, 286.24639892578125)
			math_006.location = (1543.8201904296875, 306.56878662109375)
			vector_math.location = (1543.8201904296875, 146.56878662109375)
			map_range.location = (1340.0, 300.0)
			map_range_001.location = (1340.0, 40.0)
			noise_texture.location = (1142.486328125, 289.14031982421875)
			combine_xyz_001.location = (880.0, 300.0)
			value.location = (-480.0, -228.98846435546875)
			random_value.location = (-146.0265655517578, 430.21173095703125)
			math_009.location = (-159.9998779296875, 110.0)
			vector_math_001.location = (45.413909912109375, 436.6630859375)
			reroute.location = (-200.3484344482422, -201.43125915527344)
			group_input.location = (-480.0, 0.0)
			clamp.location = (1142.486328125, -10.85968017578125)
			
			#Set dimensions
			combine_xyz.width, combine_xyz.height = 140.0, 100.0
			vector_math_003.width, vector_math_003.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			math_003.width, math_003.height = 140.0, 100.0
			math_002.width, math_002.height = 140.0, 100.0
			math_004.width, math_004.height = 140.0, 100.0
			separate_xyz.width, separate_xyz.height = 140.0, 100.0
			math_005.width, math_005.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			value_001.width, value_001.height = 140.0, 100.0
			vector_math_002.width, vector_math_002.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			math_006.width, math_006.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			map_range.width, map_range.height = 140.0, 100.0
			map_range_001.width, map_range_001.height = 140.0, 100.0
			noise_texture.width, noise_texture.height = 140.0, 100.0
			combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
			value.width, value.height = 140.0, 100.0
			random_value.width, random_value.height = 140.0, 100.0
			math_009.width, math_009.height = 140.0, 100.0
			vector_math_001.width, vector_math_001.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			clamp.width, clamp.height = 140.0, 100.0
			
			#initialize mn_animate_noise_repeat links
			#math_009.Value -> combine_xyz.X
			mn_animate_noise_repeat.links.new(math_009.outputs[0], combine_xyz.inputs[0])
			#combine_xyz.Vector -> vector_math_002.Vector
			mn_animate_noise_repeat.links.new(combine_xyz.outputs[0], vector_math_002.inputs[1])
			#vector_math_003.Vector -> separate_xyz.Vector
			mn_animate_noise_repeat.links.new(vector_math_003.outputs[0], separate_xyz.inputs[0])
			#reroute.Output -> math.Value
			mn_animate_noise_repeat.links.new(reroute.outputs[0], math.inputs[1])
			#math.Value -> vector_math_003.Scale
			mn_animate_noise_repeat.links.new(math.outputs[0], vector_math_003.inputs[3])
			#reroute.Output -> math_001.Value
			mn_animate_noise_repeat.links.new(reroute.outputs[0], math_001.inputs[0])
			#value_001.Value -> math_001.Value
			mn_animate_noise_repeat.links.new(value_001.outputs[0], math_001.inputs[1])
			#separate_xyz.X -> math_002.Value
			mn_animate_noise_repeat.links.new(separate_xyz.outputs[0], math_002.inputs[0])
			#separate_xyz.X -> math_003.Value
			mn_animate_noise_repeat.links.new(separate_xyz.outputs[0], math_003.inputs[0])
			#math_002.Value -> combine_xyz_001.X
			mn_animate_noise_repeat.links.new(math_002.outputs[0], combine_xyz_001.inputs[0])
			#math_003.Value -> combine_xyz_001.Y
			mn_animate_noise_repeat.links.new(math_003.outputs[0], combine_xyz_001.inputs[1])
			#separate_xyz.Y -> math_004.Value
			mn_animate_noise_repeat.links.new(separate_xyz.outputs[1], math_004.inputs[0])
			#math_004.Value -> combine_xyz_001.Z
			mn_animate_noise_repeat.links.new(math_004.outputs[0], combine_xyz_001.inputs[2])
			#separate_xyz.Y -> math_005.Value
			mn_animate_noise_repeat.links.new(separate_xyz.outputs[1], math_005.inputs[0])
			#math_005.Value -> noise_texture.W
			mn_animate_noise_repeat.links.new(math_005.outputs[0], noise_texture.inputs[1])
			#math_001.Value -> noise_texture.Scale
			mn_animate_noise_repeat.links.new(math_001.outputs[0], noise_texture.inputs[2])
			#noise_texture.Fac -> map_range.Value
			mn_animate_noise_repeat.links.new(noise_texture.outputs[0], map_range.inputs[0])
			#map_range.Result -> math_006.Value
			mn_animate_noise_repeat.links.new(map_range.outputs[0], math_006.inputs[0])
			#math_006.Value -> group_output.Noise Float
			mn_animate_noise_repeat.links.new(math_006.outputs[0], group_output.inputs[0])
			#group_input.Amplitude -> math_006.Value
			mn_animate_noise_repeat.links.new(group_input.outputs[0], math_006.inputs[1])
			#noise_texture.Color -> map_range_001.Vector
			mn_animate_noise_repeat.links.new(noise_texture.outputs[1], map_range_001.inputs[6])
			#map_range_001.Vector -> vector_math.Vector
			mn_animate_noise_repeat.links.new(map_range_001.outputs[1], vector_math.inputs[0])
			#group_input.Amplitude -> vector_math.Scale
			mn_animate_noise_repeat.links.new(group_input.outputs[0], vector_math.inputs[3])
			#vector_math.Vector -> group_output.Noise Vector
			mn_animate_noise_repeat.links.new(vector_math.outputs[0], group_output.inputs[1])
			#group_input.Detail -> noise_texture.Detail
			mn_animate_noise_repeat.links.new(group_input.outputs[1], noise_texture.inputs[3])
			#group_input.Distortion -> noise_texture.Distortion
			mn_animate_noise_repeat.links.new(group_input.outputs[3], noise_texture.inputs[8])
			#group_input.Vector -> vector_math_002.Vector
			mn_animate_noise_repeat.links.new(group_input.outputs[4], vector_math_002.inputs[0])
			#vector_math_002.Vector -> vector_math_001.Vector
			mn_animate_noise_repeat.links.new(vector_math_002.outputs[0], vector_math_001.inputs[0])
			#random_value.Value -> vector_math_001.Vector
			mn_animate_noise_repeat.links.new(random_value.outputs[0], vector_math_001.inputs[1])
			#vector_math_001.Vector -> vector_math_003.Vector
			mn_animate_noise_repeat.links.new(vector_math_001.outputs[0], vector_math_003.inputs[0])
			#combine_xyz_001.Vector -> noise_texture.Vector
			mn_animate_noise_repeat.links.new(combine_xyz_001.outputs[0], noise_texture.inputs[0])
			#reroute.Output -> math_009.Value
			mn_animate_noise_repeat.links.new(reroute.outputs[0], math_009.inputs[1])
			#group_input.Vector -> random_value.ID
			mn_animate_noise_repeat.links.new(group_input.outputs[4], random_value.inputs[7])
			#group_input.Animate 0..1 -> math_009.Value
			mn_animate_noise_repeat.links.new(group_input.outputs[6], math_009.inputs[0])
			#group_input.Speed -> reroute.Input
			mn_animate_noise_repeat.links.new(group_input.outputs[5], reroute.inputs[0])
			#group_input.Roughness -> clamp.Value
			mn_animate_noise_repeat.links.new(group_input.outputs[2], clamp.inputs[0])
			#clamp.Result -> noise_texture.Roughness
			mn_animate_noise_repeat.links.new(clamp.outputs[0], noise_texture.inputs[4])
			return mn_animate_noise_repeat

		mn_animate_noise_repeat = mn_animate_noise_repeat_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "MN_animate_noise_repeat", type = 'NODES')
		mod.node_group = mn_animate_noise_repeat
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(MN_animate_noise_repeat.bl_idname)
			
def register():
	bpy.utils.register_class(MN_animate_noise_repeat)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(MN_animate_noise_repeat)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
