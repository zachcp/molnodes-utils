bl_info = {
	"name" : ".MN_utils_rotate_res",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _MN_utils_rotate_res(bpy.types.Operator):
	bl_idname = "node._mn_utils_rotate_res"
	bl_label = ".MN_utils_rotate_res"
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

		#initialize _utils_group_field_at_selection node group
		def _utils_group_field_at_selection_node_group():
			_utils_group_field_at_selection = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".utils_group_field_at_selection")

			_utils_group_field_at_selection.color_tag = 'NONE'
			_utils_group_field_at_selection.description = ""

			
			#_utils_group_field_at_selection interface
			#Socket Group Index
			group_index_socket = _utils_group_field_at_selection.interface.new_socket(name = "Group Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			group_index_socket.default_value = 0
			group_index_socket.min_value = -2147483648
			group_index_socket.max_value = 2147483647
			group_index_socket.subtype = 'NONE'
			group_index_socket.attribute_domain = 'POINT'
			
			#Socket Float
			float_socket = _utils_group_field_at_selection.interface.new_socket(name = "Float", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			float_socket.default_value = 0.0
			float_socket.min_value = -3.4028234663852886e+38
			float_socket.max_value = 3.4028234663852886e+38
			float_socket.subtype = 'NONE'
			float_socket.attribute_domain = 'POINT'
			
			#Socket Vector
			vector_socket_1 = _utils_group_field_at_selection.interface.new_socket(name = "Vector", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			vector_socket_1.default_value = (0.0, 0.0, 0.0)
			vector_socket_1.min_value = -3.4028234663852886e+38
			vector_socket_1.max_value = 3.4028234663852886e+38
			vector_socket_1.subtype = 'NONE'
			vector_socket_1.attribute_domain = 'POINT'
			
			#Socket Boolean
			boolean_socket = _utils_group_field_at_selection.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket.default_value = False
			boolean_socket.attribute_domain = 'POINT'
			
			#Socket Color
			color_socket = _utils_group_field_at_selection.interface.new_socket(name = "Color", in_out='OUTPUT', socket_type = 'NodeSocketColor')
			color_socket.default_value = (0.0, 0.0, 0.0, 0.0)
			color_socket.attribute_domain = 'POINT'
			
			#Socket Integer
			integer_socket = _utils_group_field_at_selection.interface.new_socket(name = "Integer", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			integer_socket.default_value = 0
			integer_socket.min_value = -2147483648
			integer_socket.max_value = 2147483647
			integer_socket.subtype = 'NONE'
			integer_socket.attribute_domain = 'POINT'
			
			#Socket Selection
			selection_socket = _utils_group_field_at_selection.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket.default_value = False
			selection_socket.attribute_domain = 'POINT'
			selection_socket.description = "Selection of atoms to apply this node to"
			
			#Socket Group Index
			group_index_socket_1 = _utils_group_field_at_selection.interface.new_socket(name = "Group Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			group_index_socket_1.default_value = 0
			group_index_socket_1.min_value = -2147483648
			group_index_socket_1.max_value = 2147483647
			group_index_socket_1.subtype = 'NONE'
			group_index_socket_1.attribute_domain = 'POINT'
			
			#Socket Float
			float_socket_1 = _utils_group_field_at_selection.interface.new_socket(name = "Float", in_out='INPUT', socket_type = 'NodeSocketFloat')
			float_socket_1.default_value = 0.0
			float_socket_1.min_value = -3.4028234663852886e+38
			float_socket_1.max_value = 3.4028234663852886e+38
			float_socket_1.subtype = 'NONE'
			float_socket_1.attribute_domain = 'POINT'
			float_socket_1.hide_value = True
			
			#Socket Vector
			vector_socket_2 = _utils_group_field_at_selection.interface.new_socket(name = "Vector", in_out='INPUT', socket_type = 'NodeSocketVector')
			vector_socket_2.default_value = (0.0, 0.0, 0.0)
			vector_socket_2.min_value = -3.4028234663852886e+38
			vector_socket_2.max_value = 3.4028234663852886e+38
			vector_socket_2.subtype = 'NONE'
			vector_socket_2.attribute_domain = 'POINT'
			vector_socket_2.hide_value = True
			
			#Socket Boolean
			boolean_socket_1 = _utils_group_field_at_selection.interface.new_socket(name = "Boolean", in_out='INPUT', socket_type = 'NodeSocketBool')
			boolean_socket_1.default_value = False
			boolean_socket_1.attribute_domain = 'POINT'
			boolean_socket_1.hide_value = True
			
			#Socket Color
			color_socket_1 = _utils_group_field_at_selection.interface.new_socket(name = "Color", in_out='INPUT', socket_type = 'NodeSocketColor')
			color_socket_1.default_value = (0.0, 0.0, 0.0, 0.0)
			color_socket_1.attribute_domain = 'POINT'
			color_socket_1.hide_value = True
			
			#Socket Integer
			integer_socket_1 = _utils_group_field_at_selection.interface.new_socket(name = "Integer", in_out='INPUT', socket_type = 'NodeSocketInt')
			integer_socket_1.default_value = 0
			integer_socket_1.min_value = -2147483648
			integer_socket_1.max_value = 2147483647
			integer_socket_1.subtype = 'NONE'
			integer_socket_1.attribute_domain = 'POINT'
			integer_socket_1.hide_value = True
			
			
			#initialize _utils_group_field_at_selection nodes
			#node Switch.006
			switch_006 = _utils_group_field_at_selection.nodes.new("GeometryNodeSwitch")
			switch_006.name = "Switch.006"
			switch_006.input_type = 'INT'
			#False
			switch_006.inputs[1].default_value = 0
			
			#node Accumulate Field.002
			accumulate_field_002 = _utils_group_field_at_selection.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_002.name = "Accumulate Field.002"
			accumulate_field_002.data_type = 'INT'
			accumulate_field_002.domain = 'POINT'
			
			#node Index
			index = _utils_group_field_at_selection.nodes.new("GeometryNodeInputIndex")
			index.name = "Index"
			
			#node Group Output
			group_output_1 = _utils_group_field_at_selection.nodes.new("NodeGroupOutput")
			group_output_1.name = "Group Output"
			group_output_1.is_active_output = True
			
			#node Field at Index
			field_at_index = _utils_group_field_at_selection.nodes.new("GeometryNodeFieldAtIndex")
			field_at_index.name = "Field at Index"
			field_at_index.data_type = 'FLOAT'
			field_at_index.domain = 'POINT'
			
			#node Field at Index.001
			field_at_index_001 = _utils_group_field_at_selection.nodes.new("GeometryNodeFieldAtIndex")
			field_at_index_001.name = "Field at Index.001"
			field_at_index_001.data_type = 'FLOAT_VECTOR'
			field_at_index_001.domain = 'POINT'
			
			#node Field at Index.002
			field_at_index_002 = _utils_group_field_at_selection.nodes.new("GeometryNodeFieldAtIndex")
			field_at_index_002.name = "Field at Index.002"
			field_at_index_002.data_type = 'BOOLEAN'
			field_at_index_002.domain = 'POINT'
			
			#node Field at Index.003
			field_at_index_003 = _utils_group_field_at_selection.nodes.new("GeometryNodeFieldAtIndex")
			field_at_index_003.name = "Field at Index.003"
			field_at_index_003.data_type = 'FLOAT_COLOR'
			field_at_index_003.domain = 'POINT'
			
			#node Group Input
			group_input_1 = _utils_group_field_at_selection.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			
			#node Field at Index.004
			field_at_index_004 = _utils_group_field_at_selection.nodes.new("GeometryNodeFieldAtIndex")
			field_at_index_004.name = "Field at Index.004"
			field_at_index_004.data_type = 'INT'
			field_at_index_004.domain = 'POINT'
			
			
			
			
			#Set locations
			switch_006.location = (-80.0, 80.0)
			accumulate_field_002.location = (80.0, 80.0)
			index.location = (-80.0, -80.0)
			group_output_1.location = (477.87579345703125, 6.6051177978515625)
			field_at_index.location = (280.0, -20.0)
			field_at_index_001.location = (280.0, -180.0)
			field_at_index_002.location = (280.0, -340.0)
			field_at_index_003.location = (280.0, -500.0)
			group_input_1.location = (-280.0, -0.0)
			field_at_index_004.location = (280.0, -660.0)
			
			#Set dimensions
			switch_006.width, switch_006.height = 140.0, 100.0
			accumulate_field_002.width, accumulate_field_002.height = 140.0, 100.0
			index.width, index.height = 140.0, 100.0
			group_output_1.width, group_output_1.height = 140.0, 100.0
			field_at_index.width, field_at_index.height = 140.0, 100.0
			field_at_index_001.width, field_at_index_001.height = 140.0, 100.0
			field_at_index_002.width, field_at_index_002.height = 140.0, 100.0
			field_at_index_003.width, field_at_index_003.height = 140.0, 100.0
			group_input_1.width, group_input_1.height = 140.0, 100.0
			field_at_index_004.width, field_at_index_004.height = 140.0, 100.0
			
			#initialize _utils_group_field_at_selection links
			#group_input_1.Selection -> switch_006.Switch
			_utils_group_field_at_selection.links.new(group_input_1.outputs[0], switch_006.inputs[0])
			#accumulate_field_002.Total -> group_output_1.Group Index
			_utils_group_field_at_selection.links.new(accumulate_field_002.outputs[2], group_output_1.inputs[0])
			#group_input_1.Group Index -> accumulate_field_002.Group ID
			_utils_group_field_at_selection.links.new(group_input_1.outputs[1], accumulate_field_002.inputs[1])
			#index.Index -> switch_006.True
			_utils_group_field_at_selection.links.new(index.outputs[0], switch_006.inputs[2])
			#switch_006.Output -> accumulate_field_002.Value
			_utils_group_field_at_selection.links.new(switch_006.outputs[0], accumulate_field_002.inputs[0])
			#accumulate_field_002.Total -> field_at_index.Index
			_utils_group_field_at_selection.links.new(accumulate_field_002.outputs[2], field_at_index.inputs[0])
			#group_input_1.Float -> field_at_index.Value
			_utils_group_field_at_selection.links.new(group_input_1.outputs[2], field_at_index.inputs[1])
			#field_at_index.Value -> group_output_1.Float
			_utils_group_field_at_selection.links.new(field_at_index.outputs[0], group_output_1.inputs[1])
			#accumulate_field_002.Total -> field_at_index_001.Index
			_utils_group_field_at_selection.links.new(accumulate_field_002.outputs[2], field_at_index_001.inputs[0])
			#group_input_1.Vector -> field_at_index_001.Value
			_utils_group_field_at_selection.links.new(group_input_1.outputs[3], field_at_index_001.inputs[1])
			#field_at_index_001.Value -> group_output_1.Vector
			_utils_group_field_at_selection.links.new(field_at_index_001.outputs[0], group_output_1.inputs[2])
			#accumulate_field_002.Total -> field_at_index_002.Index
			_utils_group_field_at_selection.links.new(accumulate_field_002.outputs[2], field_at_index_002.inputs[0])
			#group_input_1.Boolean -> field_at_index_002.Value
			_utils_group_field_at_selection.links.new(group_input_1.outputs[4], field_at_index_002.inputs[1])
			#field_at_index_002.Value -> group_output_1.Boolean
			_utils_group_field_at_selection.links.new(field_at_index_002.outputs[0], group_output_1.inputs[3])
			#accumulate_field_002.Total -> field_at_index_003.Index
			_utils_group_field_at_selection.links.new(accumulate_field_002.outputs[2], field_at_index_003.inputs[0])
			#group_input_1.Color -> field_at_index_003.Value
			_utils_group_field_at_selection.links.new(group_input_1.outputs[5], field_at_index_003.inputs[1])
			#field_at_index_003.Value -> group_output_1.Color
			_utils_group_field_at_selection.links.new(field_at_index_003.outputs[0], group_output_1.inputs[4])
			#accumulate_field_002.Total -> field_at_index_004.Index
			_utils_group_field_at_selection.links.new(accumulate_field_002.outputs[2], field_at_index_004.inputs[0])
			#group_input_1.Integer -> field_at_index_004.Value
			_utils_group_field_at_selection.links.new(group_input_1.outputs[6], field_at_index_004.inputs[1])
			#field_at_index_004.Value -> group_output_1.Integer
			_utils_group_field_at_selection.links.new(field_at_index_004.outputs[0], group_output_1.inputs[5])
			return _utils_group_field_at_selection

		_utils_group_field_at_selection = _utils_group_field_at_selection_node_group()

		#initialize _mn_utils_aa_atom_pos node group
		def _mn_utils_aa_atom_pos_node_group():
			_mn_utils_aa_atom_pos = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_utils_aa_atom_pos")

			_mn_utils_aa_atom_pos.color_tag = 'NONE'
			_mn_utils_aa_atom_pos.description = ""

			
			#_mn_utils_aa_atom_pos interface
			#Socket Position
			position_socket = _mn_utils_aa_atom_pos.interface.new_socket(name = "Position", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			position_socket.default_value = (0.0, 0.0, 0.0)
			position_socket.min_value = -3.4028234663852886e+38
			position_socket.max_value = 3.4028234663852886e+38
			position_socket.subtype = 'NONE'
			position_socket.attribute_domain = 'POINT'
			
			#Socket Group Index
			group_index_socket_2 = _mn_utils_aa_atom_pos.interface.new_socket(name = "Group Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			group_index_socket_2.default_value = 0
			group_index_socket_2.min_value = -2147483648
			group_index_socket_2.max_value = 2147483647
			group_index_socket_2.subtype = 'NONE'
			group_index_socket_2.attribute_domain = 'POINT'
			
			#Socket b_factor
			b_factor_socket = _mn_utils_aa_atom_pos.interface.new_socket(name = "b_factor", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			b_factor_socket.default_value = 0.0
			b_factor_socket.min_value = -3.4028234663852886e+38
			b_factor_socket.max_value = 3.4028234663852886e+38
			b_factor_socket.subtype = 'NONE'
			b_factor_socket.attribute_domain = 'POINT'
			
			#Socket Integer
			integer_socket_2 = _mn_utils_aa_atom_pos.interface.new_socket(name = "Integer", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			integer_socket_2.default_value = 0
			integer_socket_2.min_value = -2147483648
			integer_socket_2.max_value = 2147483647
			integer_socket_2.subtype = 'NONE'
			integer_socket_2.attribute_domain = 'POINT'
			
			#Socket atom_name
			atom_name_socket = _mn_utils_aa_atom_pos.interface.new_socket(name = "atom_name", in_out='INPUT', socket_type = 'NodeSocketInt')
			atom_name_socket.default_value = 5
			atom_name_socket.min_value = -2147483648
			atom_name_socket.max_value = 2147483647
			atom_name_socket.subtype = 'NONE'
			atom_name_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_utils_aa_atom_pos nodes
			#node Frame
			frame = _mn_utils_aa_atom_pos.nodes.new("NodeFrame")
			frame.label = "If atom_name is 0, return midpoint of backbone N and C"
			frame.name = "Frame"
			frame.label_size = 20
			frame.shrink = True
			
			#node Group Input
			group_input_2 = _mn_utils_aa_atom_pos.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
			#node Named Attribute
			named_attribute = _mn_utils_aa_atom_pos.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'INT'
			#Name
			named_attribute.inputs[0].default_value = "atom_name"
			
			#node Compare.002
			compare_002 = _mn_utils_aa_atom_pos.nodes.new("FunctionNodeCompare")
			compare_002.name = "Compare.002"
			compare_002.data_type = 'INT'
			compare_002.mode = 'ELEMENT'
			compare_002.operation = 'EQUAL'
			#B_INT
			compare_002.inputs[3].default_value = 1
			
			#node Compare
			compare = _mn_utils_aa_atom_pos.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.hide = True
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'EQUAL'
			
			#node Named Attribute.001
			named_attribute_001 = _mn_utils_aa_atom_pos.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.label = "b_factor"
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.hide = True
			named_attribute_001.data_type = 'FLOAT'
			#Name
			named_attribute_001.inputs[0].default_value = "b_factor"
			
			#node Position.001
			position_001 = _mn_utils_aa_atom_pos.nodes.new("GeometryNodeInputPosition")
			position_001.name = "Position.001"
			
			#node Reroute
			reroute_1 = _mn_utils_aa_atom_pos.nodes.new("NodeReroute")
			reroute_1.name = "Reroute"
			#node Position.002
			position_002 = _mn_utils_aa_atom_pos.nodes.new("GeometryNodeInputPosition")
			position_002.name = "Position.002"
			
			#node Compare.001
			compare_001 = _mn_utils_aa_atom_pos.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'INT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'EQUAL'
			#B_INT
			compare_001.inputs[3].default_value = 3
			
			#node Compare.003
			compare_003 = _mn_utils_aa_atom_pos.nodes.new("FunctionNodeCompare")
			compare_003.name = "Compare.003"
			compare_003.data_type = 'INT'
			compare_003.mode = 'ELEMENT'
			compare_003.operation = 'EQUAL'
			#B_INT
			compare_003.inputs[3].default_value = 1
			
			#node Switch.005
			switch_005 = _mn_utils_aa_atom_pos.nodes.new("GeometryNodeSwitch")
			switch_005.name = "Switch.005"
			switch_005.input_type = 'VECTOR'
			
			#node Compare.004
			compare_004 = _mn_utils_aa_atom_pos.nodes.new("FunctionNodeCompare")
			compare_004.name = "Compare.004"
			compare_004.data_type = 'INT'
			compare_004.mode = 'ELEMENT'
			compare_004.operation = 'NOT_EQUAL'
			#B_INT
			compare_004.inputs[3].default_value = 0
			
			#node Mix
			mix = _mn_utils_aa_atom_pos.nodes.new("ShaderNodeMix")
			mix.name = "Mix"
			mix.blend_type = 'MIX'
			mix.clamp_factor = True
			mix.clamp_result = False
			mix.data_type = 'VECTOR'
			mix.factor_mode = 'UNIFORM'
			#Factor_Float
			mix.inputs[0].default_value = 0.5
			
			#node Index
			index_1 = _mn_utils_aa_atom_pos.nodes.new("GeometryNodeInputIndex")
			index_1.name = "Index"
			
			#node Edges of Vertex
			edges_of_vertex = _mn_utils_aa_atom_pos.nodes.new("GeometryNodeEdgesOfVertex")
			edges_of_vertex.name = "Edges of Vertex"
			#Weights
			edges_of_vertex.inputs[1].default_value = 0.0
			#Sort Index
			edges_of_vertex.inputs[2].default_value = 0
			
			#node Group.002
			group_002 = _mn_utils_aa_atom_pos.nodes.new("GeometryNodeGroup")
			group_002.name = "Group.002"
			group_002.node_tree = _utils_group_field_at_selection
			group_002.inputs[2].hide = True
			group_002.inputs[4].hide = True
			group_002.inputs[5].hide = True
			group_002.inputs[6].hide = True
			group_002.outputs[0].hide = True
			group_002.outputs[1].hide = True
			group_002.outputs[3].hide = True
			group_002.outputs[4].hide = True
			group_002.outputs[5].hide = True
			#Input_3
			group_002.inputs[2].default_value = 0.0
			#Input_7
			group_002.inputs[4].default_value = False
			#Input_9
			group_002.inputs[5].default_value = (0.0, 0.0, 0.0, 0.0)
			#Input_11
			group_002.inputs[6].default_value = 0
			
			#node Group.001
			group_001 = _mn_utils_aa_atom_pos.nodes.new("GeometryNodeGroup")
			group_001.name = "Group.001"
			group_001.node_tree = _utils_group_field_at_selection
			group_001.inputs[2].hide = True
			group_001.inputs[4].hide = True
			group_001.inputs[5].hide = True
			group_001.inputs[6].hide = True
			group_001.outputs[0].hide = True
			group_001.outputs[1].hide = True
			group_001.outputs[3].hide = True
			group_001.outputs[4].hide = True
			group_001.outputs[5].hide = True
			#Input_3
			group_001.inputs[2].default_value = 0.0
			#Input_7
			group_001.inputs[4].default_value = False
			#Input_9
			group_001.inputs[5].default_value = (0.0, 0.0, 0.0, 0.0)
			#Input_11
			group_001.inputs[6].default_value = 0
			
			#node Group Output
			group_output_2 = _mn_utils_aa_atom_pos.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Accumulate Field.001
			accumulate_field_001 = _mn_utils_aa_atom_pos.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_001.name = "Accumulate Field.001"
			accumulate_field_001.data_type = 'INT'
			accumulate_field_001.domain = 'POINT'
			#Group Index
			accumulate_field_001.inputs[1].default_value = 0
			
			#node Group
			group = _mn_utils_aa_atom_pos.nodes.new("GeometryNodeGroup")
			group.name = "Group"
			group.node_tree = _utils_group_field_at_selection
			#Input_7
			group.inputs[4].default_value = False
			#Input_9
			group.inputs[5].default_value = (0.0, 0.0, 0.0, 0.0)
			
			
			
			#Set parents
			position_002.parent = frame
			compare_001.parent = frame
			compare_003.parent = frame
			switch_005.parent = frame
			compare_004.parent = frame
			mix.parent = frame
			group_002.parent = frame
			group_001.parent = frame
			
			#Set locations
			frame.location = (0.0, 0.0)
			group_input_2.location = (-580.0, 200.0)
			named_attribute.location = (-580.0, 320.0)
			compare_002.location = (-580.0, 20.0)
			compare.location = (-85.78459167480469, -98.68995666503906)
			named_attribute_001.location = (-80.0, -200.0)
			position_001.location = (-80.0, -140.0)
			reroute_1.location = (60.0, 80.0)
			position_002.location = (-100.0, 440.0)
			compare_001.location = (-100.0, 380.0)
			compare_003.location = (-100.0, 600.0)
			switch_005.location = (620.0, 360.0)
			compare_004.location = (420.0, 340.0)
			mix.location = (420.0, 560.0)
			index_1.location = (-240.0, -260.0)
			edges_of_vertex.location = (-80.0, -260.0)
			group_002.location = (160.0, 400.0)
			group_001.location = (160.0, 580.0)
			group_output_2.location = (1178.18603515625, 91.78607177734375)
			accumulate_field_001.location = (-420.0, 20.0)
			group.location = (141.92819213867188, 23.15901756286621)
			
			#Set dimensions
			frame.width, frame.height = 920.0, 479.0
			group_input_2.width, group_input_2.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 218.64825439453125, 100.0
			compare_002.width, compare_002.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
			position_001.width, position_001.height = 140.0, 100.0
			reroute_1.width, reroute_1.height = 16.0, 100.0
			position_002.width, position_002.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			compare_003.width, compare_003.height = 140.0, 100.0
			switch_005.width, switch_005.height = 140.0, 100.0
			compare_004.width, compare_004.height = 140.0, 100.0
			mix.width, mix.height = 140.0, 100.0
			index_1.width, index_1.height = 140.0, 100.0
			edges_of_vertex.width, edges_of_vertex.height = 140.0, 100.0
			group_002.width, group_002.height = 180.198486328125, 100.0
			group_001.width, group_001.height = 180.198486328125, 100.0
			group_output_2.width, group_output_2.height = 140.0, 100.0
			accumulate_field_001.width, accumulate_field_001.height = 140.0, 100.0
			group.width, group.height = 282.89483642578125, 100.0
			
			#initialize _mn_utils_aa_atom_pos links
			#group_input_2.atom_name -> compare.B
			_mn_utils_aa_atom_pos.links.new(group_input_2.outputs[0], compare.inputs[3])
			#named_attribute.Attribute -> compare.A
			_mn_utils_aa_atom_pos.links.new(named_attribute.outputs[0], compare.inputs[2])
			#reroute_1.Output -> group_output_2.Group Index
			_mn_utils_aa_atom_pos.links.new(reroute_1.outputs[0], group_output_2.inputs[1])
			#named_attribute.Attribute -> compare_002.A
			_mn_utils_aa_atom_pos.links.new(named_attribute.outputs[0], compare_002.inputs[2])
			#compare_002.Result -> accumulate_field_001.Value
			_mn_utils_aa_atom_pos.links.new(compare_002.outputs[0], accumulate_field_001.inputs[0])
			#named_attribute.Attribute -> compare_001.A
			_mn_utils_aa_atom_pos.links.new(named_attribute.outputs[0], compare_001.inputs[2])
			#named_attribute.Attribute -> compare_003.A
			_mn_utils_aa_atom_pos.links.new(named_attribute.outputs[0], compare_003.inputs[2])
			#group_input_2.atom_name -> compare_004.A
			_mn_utils_aa_atom_pos.links.new(group_input_2.outputs[0], compare_004.inputs[2])
			#compare_004.Result -> switch_005.Switch
			_mn_utils_aa_atom_pos.links.new(compare_004.outputs[0], switch_005.inputs[0])
			#mix.Result -> switch_005.False
			_mn_utils_aa_atom_pos.links.new(mix.outputs[1], switch_005.inputs[1])
			#switch_005.Output -> group_output_2.Position
			_mn_utils_aa_atom_pos.links.new(switch_005.outputs[0], group_output_2.inputs[0])
			#compare.Result -> group.Selection
			_mn_utils_aa_atom_pos.links.new(compare.outputs[0], group.inputs[0])
			#reroute_1.Output -> group.Group Index
			_mn_utils_aa_atom_pos.links.new(reroute_1.outputs[0], group.inputs[1])
			#named_attribute_001.Attribute -> group.Float
			_mn_utils_aa_atom_pos.links.new(named_attribute_001.outputs[0], group.inputs[2])
			#group.Float -> group_output_2.b_factor
			_mn_utils_aa_atom_pos.links.new(group.outputs[1], group_output_2.inputs[2])
			#position_001.Position -> group.Vector
			_mn_utils_aa_atom_pos.links.new(position_001.outputs[0], group.inputs[3])
			#group.Vector -> switch_005.True
			_mn_utils_aa_atom_pos.links.new(group.outputs[2], switch_005.inputs[2])
			#compare_003.Result -> group_001.Selection
			_mn_utils_aa_atom_pos.links.new(compare_003.outputs[0], group_001.inputs[0])
			#reroute_1.Output -> group_001.Group Index
			_mn_utils_aa_atom_pos.links.new(reroute_1.outputs[0], group_001.inputs[1])
			#group_001.Vector -> mix.A
			_mn_utils_aa_atom_pos.links.new(group_001.outputs[2], mix.inputs[4])
			#reroute_1.Output -> group_002.Group Index
			_mn_utils_aa_atom_pos.links.new(reroute_1.outputs[0], group_002.inputs[1])
			#compare_001.Result -> group_002.Selection
			_mn_utils_aa_atom_pos.links.new(compare_001.outputs[0], group_002.inputs[0])
			#group_002.Vector -> mix.B
			_mn_utils_aa_atom_pos.links.new(group_002.outputs[2], mix.inputs[5])
			#position_002.Position -> group_001.Vector
			_mn_utils_aa_atom_pos.links.new(position_002.outputs[0], group_001.inputs[3])
			#position_002.Position -> group_002.Vector
			_mn_utils_aa_atom_pos.links.new(position_002.outputs[0], group_002.inputs[3])
			#index_1.Index -> edges_of_vertex.Vertex Index
			_mn_utils_aa_atom_pos.links.new(index_1.outputs[0], edges_of_vertex.inputs[0])
			#edges_of_vertex.Total -> group.Integer
			_mn_utils_aa_atom_pos.links.new(edges_of_vertex.outputs[1], group.inputs[6])
			#group.Integer -> group_output_2.Integer
			_mn_utils_aa_atom_pos.links.new(group.outputs[5], group_output_2.inputs[3])
			#accumulate_field_001.Leading -> reroute_1.Input
			_mn_utils_aa_atom_pos.links.new(accumulate_field_001.outputs[0], reroute_1.inputs[0])
			return _mn_utils_aa_atom_pos

		_mn_utils_aa_atom_pos = _mn_utils_aa_atom_pos_node_group()

		#initialize _mn_constants_atom_name_peptide node group
		def _mn_constants_atom_name_peptide_node_group():
			_mn_constants_atom_name_peptide = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_constants_atom_name_peptide")

			_mn_constants_atom_name_peptide.color_tag = 'NONE'
			_mn_constants_atom_name_peptide.description = ""

			
			#_mn_constants_atom_name_peptide interface
			#Socket Backbone Lower
			backbone_lower_socket = _mn_constants_atom_name_peptide.interface.new_socket(name = "Backbone Lower", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			backbone_lower_socket.default_value = 0
			backbone_lower_socket.min_value = -2147483648
			backbone_lower_socket.max_value = 2147483647
			backbone_lower_socket.subtype = 'NONE'
			backbone_lower_socket.attribute_domain = 'POINT'
			
			#Socket Backbone Upper
			backbone_upper_socket = _mn_constants_atom_name_peptide.interface.new_socket(name = "Backbone Upper", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			backbone_upper_socket.default_value = 0
			backbone_upper_socket.min_value = -2147483648
			backbone_upper_socket.max_value = 2147483647
			backbone_upper_socket.subtype = 'NONE'
			backbone_upper_socket.attribute_domain = 'POINT'
			
			#Socket Side Chain Lower
			side_chain_lower_socket = _mn_constants_atom_name_peptide.interface.new_socket(name = "Side Chain Lower", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			side_chain_lower_socket.default_value = 0
			side_chain_lower_socket.min_value = -2147483648
			side_chain_lower_socket.max_value = 2147483647
			side_chain_lower_socket.subtype = 'NONE'
			side_chain_lower_socket.attribute_domain = 'POINT'
			
			#Socket Side Chain Upper
			side_chain_upper_socket = _mn_constants_atom_name_peptide.interface.new_socket(name = "Side Chain Upper", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			side_chain_upper_socket.default_value = 0
			side_chain_upper_socket.min_value = -2147483648
			side_chain_upper_socket.max_value = 2147483647
			side_chain_upper_socket.subtype = 'NONE'
			side_chain_upper_socket.attribute_domain = 'POINT'
			
			#Socket Alpha Carbon
			alpha_carbon_socket = _mn_constants_atom_name_peptide.interface.new_socket(name = "Alpha Carbon", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			alpha_carbon_socket.default_value = 0
			alpha_carbon_socket.min_value = -2147483648
			alpha_carbon_socket.max_value = 2147483647
			alpha_carbon_socket.subtype = 'NONE'
			alpha_carbon_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_constants_atom_name_peptide nodes
			#node Group Input
			group_input_3 = _mn_constants_atom_name_peptide.nodes.new("NodeGroupInput")
			group_input_3.name = "Group Input"
			
			#node Group Output
			group_output_3 = _mn_constants_atom_name_peptide.nodes.new("NodeGroupOutput")
			group_output_3.name = "Group Output"
			group_output_3.is_active_output = True
			
			#node Integer.001
			integer_001 = _mn_constants_atom_name_peptide.nodes.new("FunctionNodeInputInt")
			integer_001.name = "Integer.001"
			integer_001.integer = 49
			
			#node Integer.004
			integer_004 = _mn_constants_atom_name_peptide.nodes.new("FunctionNodeInputInt")
			integer_004.name = "Integer.004"
			integer_004.integer = 2
			
			#node Integer
			integer = _mn_constants_atom_name_peptide.nodes.new("FunctionNodeInputInt")
			integer.name = "Integer"
			integer.integer = 5
			
			#node Integer.003
			integer_003 = _mn_constants_atom_name_peptide.nodes.new("FunctionNodeInputInt")
			integer_003.name = "Integer.003"
			integer_003.integer = 1
			
			#node Integer.002
			integer_002 = _mn_constants_atom_name_peptide.nodes.new("FunctionNodeInputInt")
			integer_002.name = "Integer.002"
			integer_002.integer = 4
			
			
			
			
			#Set locations
			group_input_3.location = (-200.0, 0.0)
			group_output_3.location = (260.0, 180.0)
			integer_001.location = (0.0, -50.0)
			integer_004.location = (0.0, -140.0)
			integer.location = (0.0, 40.0)
			integer_003.location = (0.0, 240.0)
			integer_002.location = (0.0, 140.0)
			
			#Set dimensions
			group_input_3.width, group_input_3.height = 140.0, 100.0
			group_output_3.width, group_output_3.height = 140.0, 100.0
			integer_001.width, integer_001.height = 140.0, 100.0
			integer_004.width, integer_004.height = 140.0, 100.0
			integer.width, integer.height = 140.0, 100.0
			integer_003.width, integer_003.height = 140.0, 100.0
			integer_002.width, integer_002.height = 140.0, 100.0
			
			#initialize _mn_constants_atom_name_peptide links
			#integer_003.Integer -> group_output_3.Backbone Lower
			_mn_constants_atom_name_peptide.links.new(integer_003.outputs[0], group_output_3.inputs[0])
			#integer_002.Integer -> group_output_3.Backbone Upper
			_mn_constants_atom_name_peptide.links.new(integer_002.outputs[0], group_output_3.inputs[1])
			#integer.Integer -> group_output_3.Side Chain Lower
			_mn_constants_atom_name_peptide.links.new(integer.outputs[0], group_output_3.inputs[2])
			#integer_001.Integer -> group_output_3.Side Chain Upper
			_mn_constants_atom_name_peptide.links.new(integer_001.outputs[0], group_output_3.inputs[3])
			#integer_004.Integer -> group_output_3.Alpha Carbon
			_mn_constants_atom_name_peptide.links.new(integer_004.outputs[0], group_output_3.inputs[4])
			return _mn_constants_atom_name_peptide

		_mn_constants_atom_name_peptide = _mn_constants_atom_name_peptide_node_group()

		#initialize _mn_select_peptide node group
		def _mn_select_peptide_node_group():
			_mn_select_peptide = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_select_peptide")

			_mn_select_peptide.color_tag = 'NONE'
			_mn_select_peptide.description = ""

			
			#_mn_select_peptide interface
			#Socket Is Backbone
			is_backbone_socket = _mn_select_peptide.interface.new_socket(name = "Is Backbone", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_backbone_socket.default_value = False
			is_backbone_socket.attribute_domain = 'POINT'
			
			#Socket Is Side Chain
			is_side_chain_socket = _mn_select_peptide.interface.new_socket(name = "Is Side Chain", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_side_chain_socket.default_value = False
			is_side_chain_socket.attribute_domain = 'POINT'
			
			#Socket Is Peptide
			is_peptide_socket = _mn_select_peptide.interface.new_socket(name = "Is Peptide", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_peptide_socket.default_value = False
			is_peptide_socket.attribute_domain = 'POINT'
			
			#Socket Is Alpha Carbon
			is_alpha_carbon_socket = _mn_select_peptide.interface.new_socket(name = "Is Alpha Carbon", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_alpha_carbon_socket.default_value = False
			is_alpha_carbon_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_select_peptide nodes
			#node Group Input
			group_input_4 = _mn_select_peptide.nodes.new("NodeGroupInput")
			group_input_4.name = "Group Input"
			
			#node Compare
			compare_1 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
			compare_1.name = "Compare"
			compare_1.data_type = 'INT'
			compare_1.mode = 'ELEMENT'
			compare_1.operation = 'GREATER_EQUAL'
			
			#node Compare.001
			compare_001_1 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
			compare_001_1.name = "Compare.001"
			compare_001_1.data_type = 'INT'
			compare_001_1.mode = 'ELEMENT'
			compare_001_1.operation = 'LESS_EQUAL'
			
			#node Boolean Math.001
			boolean_math_001 = _mn_select_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001.name = "Boolean Math.001"
			boolean_math_001.operation = 'AND'
			
			#node Compare.002
			compare_002_1 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
			compare_002_1.name = "Compare.002"
			compare_002_1.data_type = 'INT'
			compare_002_1.mode = 'ELEMENT'
			compare_002_1.operation = 'GREATER_EQUAL'
			
			#node Compare.003
			compare_003_1 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
			compare_003_1.name = "Compare.003"
			compare_003_1.data_type = 'INT'
			compare_003_1.mode = 'ELEMENT'
			compare_003_1.operation = 'LESS_EQUAL'
			
			#node Boolean Math.002
			boolean_math_002 = _mn_select_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002.name = "Boolean Math.002"
			boolean_math_002.operation = 'AND'
			
			#node Compare.004
			compare_004_1 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
			compare_004_1.name = "Compare.004"
			compare_004_1.data_type = 'INT'
			compare_004_1.mode = 'ELEMENT'
			compare_004_1.operation = 'GREATER_EQUAL'
			
			#node Named Attribute
			named_attribute_1 = _mn_select_peptide.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_1.name = "Named Attribute"
			named_attribute_1.data_type = 'INT'
			#Name
			named_attribute_1.inputs[0].default_value = "atom_name"
			
			#node Boolean Math.003
			boolean_math_003 = _mn_select_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003.name = "Boolean Math.003"
			boolean_math_003.operation = 'AND'
			
			#node Group Output
			group_output_4 = _mn_select_peptide.nodes.new("NodeGroupOutput")
			group_output_4.name = "Group Output"
			group_output_4.is_active_output = True
			
			#node Compare.005
			compare_005 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
			compare_005.name = "Compare.005"
			compare_005.data_type = 'INT'
			compare_005.mode = 'ELEMENT'
			compare_005.operation = 'LESS_EQUAL'
			
			#node Compare.006
			compare_006 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
			compare_006.name = "Compare.006"
			compare_006.data_type = 'INT'
			compare_006.mode = 'ELEMENT'
			compare_006.operation = 'EQUAL'
			
			#node Group
			group_1 = _mn_select_peptide.nodes.new("GeometryNodeGroup")
			group_1.name = "Group"
			group_1.node_tree = _mn_constants_atom_name_peptide
			
			#node Boolean Math
			boolean_math = _mn_select_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'OR'
			
			
			
			
			#Set locations
			group_input_4.location = (-460.0, 0.0)
			compare_1.location = (80.0, 80.0)
			compare_001_1.location = (80.0, -80.0)
			boolean_math_001.location = (260.0, 80.0)
			compare_002_1.location = (80.0, -240.0)
			compare_003_1.location = (80.0, -400.0)
			boolean_math_002.location = (260.0, -240.0)
			compare_004_1.location = (80.0, -560.0)
			named_attribute_1.location = (-360.0, -480.0)
			boolean_math_003.location = (260.0, -560.0)
			group_output_4.location = (666.1161499023438, -263.7054748535156)
			compare_005.location = (80.0, -720.0)
			compare_006.location = (260.0, -380.0)
			group_1.location = (-411.24090576171875, -312.71807861328125)
			boolean_math.location = (420.0, -240.0)
			
			#Set dimensions
			group_input_4.width, group_input_4.height = 140.0, 100.0
			compare_1.width, compare_1.height = 140.0, 100.0
			compare_001_1.width, compare_001_1.height = 140.0, 100.0
			boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
			compare_002_1.width, compare_002_1.height = 153.86517333984375, 100.0
			compare_003_1.width, compare_003_1.height = 153.86517333984375, 100.0
			boolean_math_002.width, boolean_math_002.height = 140.0, 100.0
			compare_004_1.width, compare_004_1.height = 140.0, 100.0
			named_attribute_1.width, named_attribute_1.height = 140.0, 100.0
			boolean_math_003.width, boolean_math_003.height = 140.0, 100.0
			group_output_4.width, group_output_4.height = 140.0, 100.0
			compare_005.width, compare_005.height = 140.0, 100.0
			compare_006.width, compare_006.height = 140.0, 100.0
			group_1.width, group_1.height = 369.1165771484375, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			
			#initialize _mn_select_peptide links
			#compare_001_1.Result -> boolean_math_001.Boolean
			_mn_select_peptide.links.new(compare_001_1.outputs[0], boolean_math_001.inputs[1])
			#group_1.Backbone Lower -> compare_1.B
			_mn_select_peptide.links.new(group_1.outputs[0], compare_1.inputs[3])
			#named_attribute_1.Attribute -> compare_1.A
			_mn_select_peptide.links.new(named_attribute_1.outputs[0], compare_1.inputs[2])
			#compare_1.Result -> boolean_math_001.Boolean
			_mn_select_peptide.links.new(compare_1.outputs[0], boolean_math_001.inputs[0])
			#named_attribute_1.Attribute -> compare_001_1.A
			_mn_select_peptide.links.new(named_attribute_1.outputs[0], compare_001_1.inputs[2])
			#group_1.Backbone Upper -> compare_001_1.B
			_mn_select_peptide.links.new(group_1.outputs[1], compare_001_1.inputs[3])
			#boolean_math_001.Boolean -> group_output_4.Is Backbone
			_mn_select_peptide.links.new(boolean_math_001.outputs[0], group_output_4.inputs[0])
			#compare_003_1.Result -> boolean_math_002.Boolean
			_mn_select_peptide.links.new(compare_003_1.outputs[0], boolean_math_002.inputs[1])
			#named_attribute_1.Attribute -> compare_002_1.A
			_mn_select_peptide.links.new(named_attribute_1.outputs[0], compare_002_1.inputs[2])
			#compare_002_1.Result -> boolean_math_002.Boolean
			_mn_select_peptide.links.new(compare_002_1.outputs[0], boolean_math_002.inputs[0])
			#named_attribute_1.Attribute -> compare_003_1.A
			_mn_select_peptide.links.new(named_attribute_1.outputs[0], compare_003_1.inputs[2])
			#group_1.Side Chain Lower -> compare_002_1.B
			_mn_select_peptide.links.new(group_1.outputs[2], compare_002_1.inputs[3])
			#group_1.Side Chain Upper -> compare_003_1.B
			_mn_select_peptide.links.new(group_1.outputs[3], compare_003_1.inputs[3])
			#compare_005.Result -> boolean_math_003.Boolean
			_mn_select_peptide.links.new(compare_005.outputs[0], boolean_math_003.inputs[1])
			#named_attribute_1.Attribute -> compare_004_1.A
			_mn_select_peptide.links.new(named_attribute_1.outputs[0], compare_004_1.inputs[2])
			#compare_004_1.Result -> boolean_math_003.Boolean
			_mn_select_peptide.links.new(compare_004_1.outputs[0], boolean_math_003.inputs[0])
			#named_attribute_1.Attribute -> compare_005.A
			_mn_select_peptide.links.new(named_attribute_1.outputs[0], compare_005.inputs[2])
			#group_1.Backbone Lower -> compare_004_1.B
			_mn_select_peptide.links.new(group_1.outputs[0], compare_004_1.inputs[3])
			#group_1.Side Chain Upper -> compare_005.B
			_mn_select_peptide.links.new(group_1.outputs[3], compare_005.inputs[3])
			#boolean_math_003.Boolean -> group_output_4.Is Peptide
			_mn_select_peptide.links.new(boolean_math_003.outputs[0], group_output_4.inputs[2])
			#named_attribute_1.Attribute -> compare_006.A
			_mn_select_peptide.links.new(named_attribute_1.outputs[0], compare_006.inputs[2])
			#group_1.Alpha Carbon -> compare_006.B
			_mn_select_peptide.links.new(group_1.outputs[4], compare_006.inputs[3])
			#compare_006.Result -> group_output_4.Is Alpha Carbon
			_mn_select_peptide.links.new(compare_006.outputs[0], group_output_4.inputs[3])
			#boolean_math_002.Boolean -> boolean_math.Boolean
			_mn_select_peptide.links.new(boolean_math_002.outputs[0], boolean_math.inputs[0])
			#compare_006.Result -> boolean_math.Boolean
			_mn_select_peptide.links.new(compare_006.outputs[0], boolean_math.inputs[1])
			#boolean_math.Boolean -> group_output_4.Is Side Chain
			_mn_select_peptide.links.new(boolean_math.outputs[0], group_output_4.inputs[1])
			return _mn_select_peptide

		_mn_select_peptide = _mn_select_peptide_node_group()

		#initialize fallback_boolean node group
		def fallback_boolean_node_group():
			fallback_boolean = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Fallback Boolean")

			fallback_boolean.color_tag = 'INPUT'
			fallback_boolean.description = "Computes the boolean field if the given attribute doesn't exist. If it doesn't exist it just uses the attribute instead"

			
			#fallback_boolean interface
			#Socket Boolean
			boolean_socket_2 = fallback_boolean.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket_2.default_value = False
			boolean_socket_2.attribute_domain = 'POINT'
			
			#Socket Name
			name_socket = fallback_boolean.interface.new_socket(name = "Name", in_out='INPUT', socket_type = 'NodeSocketString')
			name_socket.default_value = ""
			name_socket.attribute_domain = 'POINT'
			
			#Socket Fallback
			fallback_socket = fallback_boolean.interface.new_socket(name = "Fallback", in_out='INPUT', socket_type = 'NodeSocketBool')
			fallback_socket.default_value = False
			fallback_socket.attribute_domain = 'POINT'
			
			
			#initialize fallback_boolean nodes
			#node Group Output
			group_output_5 = fallback_boolean.nodes.new("NodeGroupOutput")
			group_output_5.name = "Group Output"
			group_output_5.is_active_output = True
			
			#node Group Input
			group_input_5 = fallback_boolean.nodes.new("NodeGroupInput")
			group_input_5.name = "Group Input"
			
			#node Named Attribute
			named_attribute_2 = fallback_boolean.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_2.name = "Named Attribute"
			named_attribute_2.data_type = 'BOOLEAN'
			
			#node Switch
			switch = fallback_boolean.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'BOOLEAN'
			
			
			
			
			#Set locations
			group_output_5.location = (276.6171569824219, 4.738137245178223)
			group_input_5.location = (-280.0, 0.0)
			named_attribute_2.location = (-94.73597717285156, 4.738137245178223)
			switch.location = (86.61715698242188, 4.738137245178223)
			
			#Set dimensions
			group_output_5.width, group_output_5.height = 140.0, 100.0
			group_input_5.width, group_input_5.height = 140.0, 100.0
			named_attribute_2.width, named_attribute_2.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			
			#initialize fallback_boolean links
			#named_attribute_2.Exists -> switch.Switch
			fallback_boolean.links.new(named_attribute_2.outputs[1], switch.inputs[0])
			#named_attribute_2.Attribute -> switch.True
			fallback_boolean.links.new(named_attribute_2.outputs[0], switch.inputs[2])
			#group_input_5.Fallback -> switch.False
			fallback_boolean.links.new(group_input_5.outputs[1], switch.inputs[1])
			#switch.Output -> group_output_5.Boolean
			fallback_boolean.links.new(switch.outputs[0], group_output_5.inputs[0])
			#group_input_5.Name -> named_attribute_2.Name
			fallback_boolean.links.new(group_input_5.outputs[0], named_attribute_2.inputs[0])
			return fallback_boolean

		fallback_boolean = fallback_boolean_node_group()

		#initialize is_peptide node group
		def is_peptide_node_group():
			is_peptide = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Is Peptide")

			is_peptide.color_tag = 'INPUT'
			is_peptide.description = ""

			
			#is_peptide interface
			#Socket Selection
			selection_socket_1 = is_peptide.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket_1.default_value = False
			selection_socket_1.attribute_domain = 'POINT'
			selection_socket_1.description = "True if atoms are part of a peptide"
			
			#Socket Inverted
			inverted_socket = is_peptide.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket.default_value = False
			inverted_socket.attribute_domain = 'POINT'
			
			#Socket And
			and_socket = is_peptide.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket.default_value = True
			and_socket.attribute_domain = 'POINT'
			and_socket.hide_value = True
			
			#Socket Or
			or_socket = is_peptide.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket.default_value = False
			or_socket.attribute_domain = 'POINT'
			or_socket.hide_value = True
			
			
			#initialize is_peptide nodes
			#node Group Input
			group_input_6 = is_peptide.nodes.new("NodeGroupInput")
			group_input_6.name = "Group Input"
			
			#node Boolean Math.001
			boolean_math_001_1 = is_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_1.name = "Boolean Math.001"
			boolean_math_001_1.operation = 'AND'
			
			#node Group
			group_2 = is_peptide.nodes.new("GeometryNodeGroup")
			group_2.name = "Group"
			group_2.node_tree = _mn_select_peptide
			
			#node Group Output
			group_output_6 = is_peptide.nodes.new("NodeGroupOutput")
			group_output_6.name = "Group Output"
			group_output_6.is_active_output = True
			
			#node Group.001
			group_001_1 = is_peptide.nodes.new("GeometryNodeGroup")
			group_001_1.name = "Group.001"
			group_001_1.node_tree = fallback_boolean
			#Socket_2
			group_001_1.inputs[0].default_value = "is_peptide"
			
			#node Boolean Math.002
			boolean_math_002_1 = is_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_1.name = "Boolean Math.002"
			boolean_math_002_1.operation = 'OR'
			
			#node Boolean Math
			boolean_math_1 = is_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math_1.name = "Boolean Math"
			boolean_math_1.operation = 'NOT'
			
			
			
			
			#Set locations
			group_input_6.location = (-200.0, 0.0)
			boolean_math_001_1.location = (-40.0, 0.0)
			group_2.location = (-340.0, -140.0)
			group_output_6.location = (320.0, 0.0)
			group_001_1.location = (-40.0, -140.0)
			boolean_math_002_1.location = (140.0, 5.243539333343506)
			boolean_math_1.location = (140.0, -120.0)
			
			#Set dimensions
			group_input_6.width, group_input_6.height = 140.0, 100.0
			boolean_math_001_1.width, boolean_math_001_1.height = 140.0, 100.0
			group_2.width, group_2.height = 247.90924072265625, 100.0
			group_output_6.width, group_output_6.height = 140.0, 100.0
			group_001_1.width, group_001_1.height = 140.0, 100.0
			boolean_math_002_1.width, boolean_math_002_1.height = 140.0, 100.0
			boolean_math_1.width, boolean_math_1.height = 140.0, 100.0
			
			#initialize is_peptide links
			#boolean_math_002_1.Boolean -> group_output_6.Selection
			is_peptide.links.new(boolean_math_002_1.outputs[0], group_output_6.inputs[0])
			#group_input_6.And -> boolean_math_001_1.Boolean
			is_peptide.links.new(group_input_6.outputs[0], boolean_math_001_1.inputs[0])
			#group_2.Is Peptide -> group_001_1.Fallback
			is_peptide.links.new(group_2.outputs[2], group_001_1.inputs[1])
			#group_001_1.Boolean -> boolean_math_001_1.Boolean
			is_peptide.links.new(group_001_1.outputs[0], boolean_math_001_1.inputs[1])
			#boolean_math_001_1.Boolean -> boolean_math_002_1.Boolean
			is_peptide.links.new(boolean_math_001_1.outputs[0], boolean_math_002_1.inputs[0])
			#group_input_6.Or -> boolean_math_002_1.Boolean
			is_peptide.links.new(group_input_6.outputs[1], boolean_math_002_1.inputs[1])
			#boolean_math_002_1.Boolean -> boolean_math_1.Boolean
			is_peptide.links.new(boolean_math_002_1.outputs[0], boolean_math_1.inputs[0])
			#boolean_math_1.Boolean -> group_output_6.Inverted
			is_peptide.links.new(boolean_math_1.outputs[0], group_output_6.inputs[1])
			return is_peptide

		is_peptide = is_peptide_node_group()

		#initialize _mn_utils_rotate_res node group
		def _mn_utils_rotate_res_node_group():
			_mn_utils_rotate_res = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_utils_rotate_res")

			_mn_utils_rotate_res.color_tag = 'NONE'
			_mn_utils_rotate_res.description = ""

			
			#_mn_utils_rotate_res interface
			#Socket Selection
			selection_socket_2 = _mn_utils_rotate_res.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket_2.default_value = False
			selection_socket_2.attribute_domain = 'POINT'
			selection_socket_2.description = "The calculated selection"
			
			#Socket Position
			position_socket_1 = _mn_utils_rotate_res.interface.new_socket(name = "Position", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			position_socket_1.default_value = (0.0, 0.0, 0.0)
			position_socket_1.min_value = -3.4028234663852886e+38
			position_socket_1.max_value = 3.4028234663852886e+38
			position_socket_1.subtype = 'NONE'
			position_socket_1.attribute_domain = 'POINT'
			
			#Socket Selection
			selection_socket_3 = _mn_utils_rotate_res.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_3.default_value = False
			selection_socket_3.attribute_domain = 'POINT'
			selection_socket_3.description = "Selection of atoms to apply this node to"
			
			#Socket atom_name rotation
			atom_name_rotation_socket = _mn_utils_rotate_res.interface.new_socket(name = "atom_name rotation", in_out='INPUT', socket_type = 'NodeSocketInt')
			atom_name_rotation_socket.default_value = 0
			atom_name_rotation_socket.min_value = -2147483648
			atom_name_rotation_socket.max_value = 2147483647
			atom_name_rotation_socket.subtype = 'NONE'
			atom_name_rotation_socket.attribute_domain = 'POINT'
			
			#Socket atom_name axis
			atom_name_axis_socket = _mn_utils_rotate_res.interface.new_socket(name = "atom_name axis", in_out='INPUT', socket_type = 'NodeSocketInt')
			atom_name_axis_socket.default_value = 2
			atom_name_axis_socket.min_value = -2147483648
			atom_name_axis_socket.max_value = 2147483647
			atom_name_axis_socket.subtype = 'NONE'
			atom_name_axis_socket.attribute_domain = 'POINT'
			
			#Socket Scale b_factor
			scale_b_factor_socket = _mn_utils_rotate_res.interface.new_socket(name = "Scale b_factor", in_out='INPUT', socket_type = 'NodeSocketFloat')
			scale_b_factor_socket.default_value = 0.0
			scale_b_factor_socket.min_value = -3.4028234663852886e+38
			scale_b_factor_socket.max_value = 3.4028234663852886e+38
			scale_b_factor_socket.subtype = 'FACTOR'
			scale_b_factor_socket.attribute_domain = 'POINT'
			
			#Socket Amplitude
			amplitude_socket_1 = _mn_utils_rotate_res.interface.new_socket(name = "Amplitude", in_out='INPUT', socket_type = 'NodeSocketFloat')
			amplitude_socket_1.default_value = 1.0
			amplitude_socket_1.min_value = 0.0
			amplitude_socket_1.max_value = 10.0
			amplitude_socket_1.subtype = 'NONE'
			amplitude_socket_1.attribute_domain = 'POINT'
			
			#Socket Amp. Axis
			amp__axis_socket = _mn_utils_rotate_res.interface.new_socket(name = "Amp. Axis", in_out='INPUT', socket_type = 'NodeSocketFloat')
			amp__axis_socket.default_value = 1.0
			amp__axis_socket.min_value = -10000.0
			amp__axis_socket.max_value = 10000.0
			amp__axis_socket.subtype = 'NONE'
			amp__axis_socket.attribute_domain = 'POINT'
			
			#Socket Amp. Euler
			amp__euler_socket = _mn_utils_rotate_res.interface.new_socket(name = "Amp. Euler", in_out='INPUT', socket_type = 'NodeSocketFloat')
			amp__euler_socket.default_value = 1.0
			amp__euler_socket.min_value = -10000.0
			amp__euler_socket.max_value = 10000.0
			amp__euler_socket.subtype = 'NONE'
			amp__euler_socket.attribute_domain = 'POINT'
			
			#Socket Speed
			speed_socket_1 = _mn_utils_rotate_res.interface.new_socket(name = "Speed", in_out='INPUT', socket_type = 'NodeSocketFloat')
			speed_socket_1.default_value = 10.0
			speed_socket_1.min_value = -10000.0
			speed_socket_1.max_value = 10000.0
			speed_socket_1.subtype = 'NONE'
			speed_socket_1.attribute_domain = 'POINT'
			
			#Socket Animate 0..1
			animate_0__1_socket_1 = _mn_utils_rotate_res.interface.new_socket(name = "Animate 0..1", in_out='INPUT', socket_type = 'NodeSocketFloat')
			animate_0__1_socket_1.default_value = 0.5
			animate_0__1_socket_1.min_value = -10000.0
			animate_0__1_socket_1.max_value = 10000.0
			animate_0__1_socket_1.subtype = 'NONE'
			animate_0__1_socket_1.attribute_domain = 'POINT'
			
			
			#initialize _mn_utils_rotate_res nodes
			#node Named Attribute.001
			named_attribute_001_1 = _mn_utils_rotate_res.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001_1.name = "Named Attribute.001"
			named_attribute_001_1.data_type = 'INT'
			#Name
			named_attribute_001_1.inputs[0].default_value = "atom_name"
			
			#node Reroute.001
			reroute_001 = _mn_utils_rotate_res.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			#node Reroute.002
			reroute_002 = _mn_utils_rotate_res.nodes.new("NodeReroute")
			reroute_002.name = "Reroute.002"
			#node Reroute.003
			reroute_003 = _mn_utils_rotate_res.nodes.new("NodeReroute")
			reroute_003.name = "Reroute.003"
			#node Boolean Math
			boolean_math_2 = _mn_utils_rotate_res.nodes.new("FunctionNodeBooleanMath")
			boolean_math_2.name = "Boolean Math"
			boolean_math_2.operation = 'AND'
			
			#node Compare.001
			compare_001_2 = _mn_utils_rotate_res.nodes.new("FunctionNodeCompare")
			compare_001_2.name = "Compare.001"
			compare_001_2.data_type = 'INT'
			compare_001_2.mode = 'ELEMENT'
			compare_001_2.operation = 'GREATER_THAN'
			
			#node Random Value
			random_value_1 = _mn_utils_rotate_res.nodes.new("FunctionNodeRandomValue")
			random_value_1.name = "Random Value"
			random_value_1.hide = True
			random_value_1.data_type = 'FLOAT_VECTOR'
			#Min
			random_value_1.inputs[0].default_value = (-13.0, -13.0, -13.0)
			#Max
			random_value_1.inputs[1].default_value = (13.899999618530273, 13.899999618530273, 13.899999618530273)
			
			#node Boolean Math.001
			boolean_math_001_2 = _mn_utils_rotate_res.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_2.name = "Boolean Math.001"
			boolean_math_001_2.operation = 'AND'
			
			#node Position
			position = _mn_utils_rotate_res.nodes.new("GeometryNodeInputPosition")
			position.name = "Position"
			
			#node Vector Rotate
			vector_rotate = _mn_utils_rotate_res.nodes.new("ShaderNodeVectorRotate")
			vector_rotate.name = "Vector Rotate"
			vector_rotate.invert = False
			vector_rotate.rotation_type = 'AXIS_ANGLE'
			
			#node Reroute.004
			reroute_004 = _mn_utils_rotate_res.nodes.new("NodeReroute")
			reroute_004.name = "Reroute.004"
			#node Group Output
			group_output_7 = _mn_utils_rotate_res.nodes.new("NodeGroupOutput")
			group_output_7.name = "Group Output"
			group_output_7.is_active_output = True
			
			#node Vector Rotate.002
			vector_rotate_002 = _mn_utils_rotate_res.nodes.new("ShaderNodeVectorRotate")
			vector_rotate_002.name = "Vector Rotate.002"
			vector_rotate_002.invert = False
			vector_rotate_002.rotation_type = 'EULER_XYZ'
			
			#node Vector Math.001
			vector_math_001_1 = _mn_utils_rotate_res.nodes.new("ShaderNodeVectorMath")
			vector_math_001_1.name = "Vector Math.001"
			vector_math_001_1.operation = 'SCALE'
			
			#node Group.004
			group_004 = _mn_utils_rotate_res.nodes.new("GeometryNodeGroup")
			group_004.name = "Group.004"
			group_004.node_tree = mn_animate_noise_repeat
			#Input_3
			group_004.inputs[1].default_value = 1.0
			#Input_4
			group_004.inputs[2].default_value = 1.0
			#Input_5
			group_004.inputs[3].default_value = 1.9799998998641968
			
			#node Vector Math.002
			vector_math_002_1 = _mn_utils_rotate_res.nodes.new("ShaderNodeVectorMath")
			vector_math_002_1.name = "Vector Math.002"
			vector_math_002_1.mute = True
			vector_math_002_1.operation = 'SCALE'
			
			#node Compare
			compare_2 = _mn_utils_rotate_res.nodes.new("FunctionNodeCompare")
			compare_2.name = "Compare"
			compare_2.data_type = 'INT'
			compare_2.mode = 'ELEMENT'
			compare_2.operation = 'EQUAL'
			#B_INT
			compare_2.inputs[3].default_value = 3
			
			#node Group
			group_3 = _mn_utils_rotate_res.nodes.new("GeometryNodeGroup")
			group_3.name = "Group"
			group_3.node_tree = mn_animate_noise_repeat
			#Input_1
			group_3.inputs[0].default_value = 1.0
			#Input_3
			group_3.inputs[1].default_value = 2.0
			#Input_4
			group_3.inputs[2].default_value = 1.0
			#Input_5
			group_3.inputs[3].default_value = 1.9799998998641968
			
			#node Compare.002
			compare_002_2 = _mn_utils_rotate_res.nodes.new("FunctionNodeCompare")
			compare_002_2.name = "Compare.002"
			compare_002_2.data_type = 'INT'
			compare_002_2.mode = 'ELEMENT'
			compare_002_2.operation = 'GREATER_THAN'
			#B_INT
			compare_002_2.inputs[3].default_value = 4
			
			#node Compare.003
			compare_003_2 = _mn_utils_rotate_res.nodes.new("FunctionNodeCompare")
			compare_003_2.name = "Compare.003"
			compare_003_2.data_type = 'INT'
			compare_003_2.mode = 'ELEMENT'
			compare_003_2.operation = 'NOT_EQUAL'
			#B_INT
			compare_003_2.inputs[3].default_value = 38
			
			#node Boolean Math.002
			boolean_math_002_2 = _mn_utils_rotate_res.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_2.name = "Boolean Math.002"
			boolean_math_002_2.operation = 'AND'
			
			#node Boolean Math.003
			boolean_math_003_1 = _mn_utils_rotate_res.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003_1.name = "Boolean Math.003"
			boolean_math_003_1.operation = 'AND'
			
			#node Reroute.005
			reroute_005 = _mn_utils_rotate_res.nodes.new("NodeReroute")
			reroute_005.name = "Reroute.005"
			#node Vector Math
			vector_math_1 = _mn_utils_rotate_res.nodes.new("ShaderNodeVectorMath")
			vector_math_1.name = "Vector Math"
			vector_math_1.hide = True
			vector_math_1.operation = 'SUBTRACT'
			
			#node Math.001
			math_001_1 = _mn_utils_rotate_res.nodes.new("ShaderNodeMath")
			math_001_1.name = "Math.001"
			math_001_1.hide = True
			math_001_1.operation = 'MULTIPLY'
			math_001_1.use_clamp = False
			
			#node Math.002
			math_002_1 = _mn_utils_rotate_res.nodes.new("ShaderNodeMath")
			math_002_1.name = "Math.002"
			math_002_1.hide = True
			math_002_1.operation = 'MULTIPLY'
			math_002_1.use_clamp = False
			
			#node Reroute.007
			reroute_007 = _mn_utils_rotate_res.nodes.new("NodeReroute")
			reroute_007.name = "Reroute.007"
			#node Reroute.006
			reroute_006 = _mn_utils_rotate_res.nodes.new("NodeReroute")
			reroute_006.name = "Reroute.006"
			#node Group Input
			group_input_7 = _mn_utils_rotate_res.nodes.new("NodeGroupInput")
			group_input_7.name = "Group Input"
			
			#node Math
			math_1 = _mn_utils_rotate_res.nodes.new("ShaderNodeMath")
			math_1.name = "Math"
			math_1.operation = 'MULTIPLY'
			math_1.use_clamp = False
			
			#node Mix
			mix_1 = _mn_utils_rotate_res.nodes.new("ShaderNodeMix")
			mix_1.name = "Mix"
			mix_1.blend_type = 'MIX'
			mix_1.clamp_factor = True
			mix_1.clamp_result = False
			mix_1.data_type = 'FLOAT'
			mix_1.factor_mode = 'UNIFORM'
			#A_Float
			mix_1.inputs[2].default_value = 1.0
			
			#node Map Range
			map_range_1 = _mn_utils_rotate_res.nodes.new("ShaderNodeMapRange")
			map_range_1.name = "Map Range"
			map_range_1.hide = True
			map_range_1.clamp = True
			map_range_1.data_type = 'FLOAT'
			map_range_1.interpolation_type = 'SMOOTHERSTEP'
			#From Min
			map_range_1.inputs[1].default_value = 1.0
			#From Max
			map_range_1.inputs[2].default_value = 100.0
			#To Min
			map_range_1.inputs[3].default_value = 0.0
			#To Max
			map_range_1.inputs[4].default_value = 1.0
			
			#node Reroute
			reroute_2 = _mn_utils_rotate_res.nodes.new("NodeReroute")
			reroute_2.name = "Reroute"
			#node Group.002
			group_002_1 = _mn_utils_rotate_res.nodes.new("GeometryNodeGroup")
			group_002_1.name = "Group.002"
			group_002_1.node_tree = _mn_utils_aa_atom_pos
			
			#node Group.003
			group_003 = _mn_utils_rotate_res.nodes.new("GeometryNodeGroup")
			group_003.name = "Group.003"
			group_003.hide = True
			group_003.node_tree = _mn_utils_aa_atom_pos
			
			#node Group.001
			group_001_2 = _mn_utils_rotate_res.nodes.new("GeometryNodeGroup")
			group_001_2.name = "Group.001"
			group_001_2.node_tree = is_peptide
			#Socket_1
			group_001_2.inputs[0].default_value = True
			#Socket_3
			group_001_2.inputs[1].default_value = False
			
			
			
			
			#Set locations
			named_attribute_001_1.location = (-900.0, 580.0)
			reroute_001.location = (-23.38579559326172, -430.73773193359375)
			reroute_002.location = (-825.0, -440.0)
			reroute_003.location = (-5.0, -460.0)
			boolean_math_2.location = (-480.0, 320.0)
			compare_001_2.location = (-640.0, 320.0)
			random_value_1.location = (-205.0, -420.0)
			boolean_math_001_2.location = (440.0, 280.0)
			position.location = (440.0, 120.0)
			vector_rotate.location = (680.0, 160.0)
			reroute_004.location = (640.0, 40.0)
			group_output_7.location = (1233.2698974609375, 262.38323974609375)
			vector_rotate_002.location = (993.2698364257812, 182.3832244873047)
			vector_math_001_1.location = (553.43408203125, -62.642765045166016)
			group_004.location = (300.0, -140.0)
			vector_math_002_1.location = (773.0, -45.8553466796875)
			compare_2.location = (780.0, -200.0)
			group_3.location = (80.0, -140.0)
			compare_002_2.location = (-640.0, 480.0)
			compare_003_2.location = (-640.0, 640.0)
			boolean_math_002_2.location = (-280.5462951660156, 430.50006103515625)
			boolean_math_003_1.location = (-87.18310546875, 553.9082641601562)
			reroute_005.location = (320.0, 20.0)
			vector_math_1.location = (360.0, 0.0)
			math_001_1.location = (360.0, -40.0)
			math_002_1.location = (140.00001525878906, -59.452919006347656)
			reroute_007.location = (20.0, -200.0)
			reroute_006.location = (20.0, -120.0)
			group_input_7.location = (-1261.5419921875, 0.30535888671875)
			math_1.location = (-152.04693603515625, -27.359119415283203)
			mix_1.location = (-361.2230224609375, 52.487037658691406)
			map_range_1.location = (-361.6744384765625, -140.6511688232422)
			reroute_2.location = (-980.0, 0.0)
			group_002_1.location = (-840.0, -60.0)
			group_003.location = (-840.0, -20.0)
			group_001_2.location = (-640.0, 160.0)
			
			#Set dimensions
			named_attribute_001_1.width, named_attribute_001_1.height = 140.0, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			reroute_002.width, reroute_002.height = 16.0, 100.0
			reroute_003.width, reroute_003.height = 16.0, 100.0
			boolean_math_2.width, boolean_math_2.height = 140.0, 100.0
			compare_001_2.width, compare_001_2.height = 140.0, 100.0
			random_value_1.width, random_value_1.height = 140.0, 100.0
			boolean_math_001_2.width, boolean_math_001_2.height = 140.0, 100.0
			position.width, position.height = 140.0, 100.0
			vector_rotate.width, vector_rotate.height = 140.0, 100.0
			reroute_004.width, reroute_004.height = 16.0, 100.0
			group_output_7.width, group_output_7.height = 140.0, 100.0
			vector_rotate_002.width, vector_rotate_002.height = 140.0, 100.0
			vector_math_001_1.width, vector_math_001_1.height = 140.0, 100.0
			group_004.width, group_004.height = 200.0, 100.0
			vector_math_002_1.width, vector_math_002_1.height = 140.0, 100.0
			compare_2.width, compare_2.height = 140.0, 100.0
			group_3.width, group_3.height = 200.0, 100.0
			compare_002_2.width, compare_002_2.height = 140.0, 100.0
			compare_003_2.width, compare_003_2.height = 140.0, 100.0
			boolean_math_002_2.width, boolean_math_002_2.height = 140.0, 100.0
			boolean_math_003_1.width, boolean_math_003_1.height = 140.0, 100.0
			reroute_005.width, reroute_005.height = 16.0, 100.0
			vector_math_1.width, vector_math_1.height = 140.0, 100.0
			math_001_1.width, math_001_1.height = 140.0, 100.0
			math_002_1.width, math_002_1.height = 140.0, 100.0
			reroute_007.width, reroute_007.height = 16.0, 100.0
			reroute_006.width, reroute_006.height = 16.0, 100.0
			group_input_7.width, group_input_7.height = 140.0, 100.0
			math_1.width, math_1.height = 140.0, 100.0
			mix_1.width, mix_1.height = 140.0, 100.0
			map_range_1.width, map_range_1.height = 140.0, 100.0
			reroute_2.width, reroute_2.height = 16.0, 100.0
			group_002_1.width, group_002_1.height = 239.87417602539062, 100.0
			group_003.width, group_003.height = 246.31427001953125, 100.0
			group_001_2.width, group_001_2.height = 140.0, 100.0
			
			#initialize _mn_utils_rotate_res links
			#boolean_math_001_2.Boolean -> group_output_7.Selection
			_mn_utils_rotate_res.links.new(boolean_math_001_2.outputs[0], group_output_7.inputs[0])
			#group_input_7.Selection -> boolean_math_001_2.Boolean
			_mn_utils_rotate_res.links.new(group_input_7.outputs[0], boolean_math_001_2.inputs[1])
			#position.Position -> vector_rotate.Vector
			_mn_utils_rotate_res.links.new(position.outputs[0], vector_rotate.inputs[0])
			#reroute_004.Output -> vector_rotate.Center
			_mn_utils_rotate_res.links.new(reroute_004.outputs[0], vector_rotate.inputs[1])
			#named_attribute_001_1.Attribute -> compare_001_2.A
			_mn_utils_rotate_res.links.new(named_attribute_001_1.outputs[0], compare_001_2.inputs[2])
			#reroute_2.Output -> compare_001_2.B
			_mn_utils_rotate_res.links.new(reroute_2.outputs[0], compare_001_2.inputs[3])
			#compare_001_2.Result -> boolean_math_2.Boolean
			_mn_utils_rotate_res.links.new(compare_001_2.outputs[0], boolean_math_2.inputs[0])
			#group_input_7.atom_name rotation -> reroute_2.Input
			_mn_utils_rotate_res.links.new(group_input_7.outputs[1], reroute_2.inputs[0])
			#vector_math_1.Vector -> vector_rotate.Axis
			_mn_utils_rotate_res.links.new(vector_math_1.outputs[0], vector_rotate.inputs[2])
			#reroute_001.Output -> group_3.Vector
			_mn_utils_rotate_res.links.new(reroute_001.outputs[0], group_3.inputs[4])
			#reroute_001.Output -> group_004.Vector
			_mn_utils_rotate_res.links.new(reroute_001.outputs[0], group_004.inputs[4])
			#vector_rotate_002.Vector -> group_output_7.Position
			_mn_utils_rotate_res.links.new(vector_rotate_002.outputs[0], group_output_7.inputs[1])
			#group_003.Position -> vector_math_1.Vector
			_mn_utils_rotate_res.links.new(group_003.outputs[0], vector_math_1.inputs[1])
			#reroute_005.Output -> vector_math_1.Vector
			_mn_utils_rotate_res.links.new(reroute_005.outputs[0], vector_math_1.inputs[0])
			#reroute_2.Output -> group_002_1.atom_name
			_mn_utils_rotate_res.links.new(reroute_2.outputs[0], group_002_1.inputs[0])
			#group_input_7.atom_name axis -> group_003.atom_name
			_mn_utils_rotate_res.links.new(group_input_7.outputs[2], group_003.inputs[0])
			#vector_rotate.Vector -> vector_rotate_002.Vector
			_mn_utils_rotate_res.links.new(vector_rotate.outputs[0], vector_rotate_002.inputs[0])
			#reroute_004.Output -> vector_rotate_002.Center
			_mn_utils_rotate_res.links.new(reroute_004.outputs[0], vector_rotate_002.inputs[1])
			#reroute_003.Output -> group_3.Animate 0..1
			_mn_utils_rotate_res.links.new(reroute_003.outputs[0], group_3.inputs[6])
			#reroute_003.Output -> group_004.Animate 0..1
			_mn_utils_rotate_res.links.new(reroute_003.outputs[0], group_004.inputs[6])
			#group_002_1.Group Index -> random_value_1.ID
			_mn_utils_rotate_res.links.new(group_002_1.outputs[1], random_value_1.inputs[7])
			#random_value_1.Value -> reroute_001.Input
			_mn_utils_rotate_res.links.new(random_value_1.outputs[0], reroute_001.inputs[0])
			#group_input_7.Animate 0..1 -> reroute_002.Input
			_mn_utils_rotate_res.links.new(group_input_7.outputs[8], reroute_002.inputs[0])
			#reroute_002.Output -> reroute_003.Input
			_mn_utils_rotate_res.links.new(reroute_002.outputs[0], reroute_003.inputs[0])
			#reroute_2.Output -> random_value_1.Seed
			_mn_utils_rotate_res.links.new(reroute_2.outputs[0], random_value_1.inputs[8])
			#boolean_math_2.Boolean -> boolean_math_002_2.Boolean
			_mn_utils_rotate_res.links.new(boolean_math_2.outputs[0], boolean_math_002_2.inputs[1])
			#named_attribute_001_1.Attribute -> compare_002_2.A
			_mn_utils_rotate_res.links.new(named_attribute_001_1.outputs[0], compare_002_2.inputs[2])
			#compare_002_2.Result -> boolean_math_002_2.Boolean
			_mn_utils_rotate_res.links.new(compare_002_2.outputs[0], boolean_math_002_2.inputs[0])
			#reroute_005.Output -> reroute_004.Input
			_mn_utils_rotate_res.links.new(reroute_005.outputs[0], reroute_004.inputs[0])
			#group_002_1.Position -> reroute_005.Input
			_mn_utils_rotate_res.links.new(group_002_1.outputs[0], reroute_005.inputs[0])
			#group_input_7.Amplitude -> math_1.Value
			_mn_utils_rotate_res.links.new(group_input_7.outputs[4], math_1.inputs[1])
			#group_3.Noise Float -> math_001_1.Value
			_mn_utils_rotate_res.links.new(group_3.outputs[0], math_001_1.inputs[1])
			#math_001_1.Value -> vector_rotate.Angle
			_mn_utils_rotate_res.links.new(math_001_1.outputs[0], vector_rotate.inputs[3])
			#group_input_7.Speed -> group_3.Speed
			_mn_utils_rotate_res.links.new(group_input_7.outputs[7], group_3.inputs[5])
			#group_input_7.Speed -> group_004.Speed
			_mn_utils_rotate_res.links.new(group_input_7.outputs[7], group_004.inputs[5])
			#group_input_7.Amp. Euler -> group_004.Amplitude
			_mn_utils_rotate_res.links.new(group_input_7.outputs[6], group_004.inputs[0])
			#group_004.Noise Vector -> vector_math_001_1.Vector
			_mn_utils_rotate_res.links.new(group_004.outputs[1], vector_math_001_1.inputs[0])
			#reroute_006.Output -> vector_math_001_1.Scale
			_mn_utils_rotate_res.links.new(reroute_006.outputs[0], vector_math_001_1.inputs[3])
			#vector_math_002_1.Vector -> vector_rotate_002.Rotation
			_mn_utils_rotate_res.links.new(vector_math_002_1.outputs[0], vector_rotate_002.inputs[4])
			#math_002_1.Value -> math_001_1.Value
			_mn_utils_rotate_res.links.new(math_002_1.outputs[0], math_001_1.inputs[0])
			#math_1.Value -> reroute_006.Input
			_mn_utils_rotate_res.links.new(math_1.outputs[0], reroute_006.inputs[0])
			#group_002_1.b_factor -> map_range_1.Value
			_mn_utils_rotate_res.links.new(group_002_1.outputs[2], map_range_1.inputs[0])
			#vector_math_001_1.Vector -> vector_math_002_1.Vector
			_mn_utils_rotate_res.links.new(vector_math_001_1.outputs[0], vector_math_002_1.inputs[0])
			#compare_2.Result -> vector_math_002_1.Scale
			_mn_utils_rotate_res.links.new(compare_2.outputs[0], vector_math_002_1.inputs[3])
			#group_002_1.Integer -> compare_2.A
			_mn_utils_rotate_res.links.new(group_002_1.outputs[3], compare_2.inputs[2])
			#named_attribute_001_1.Attribute -> compare_003_2.A
			_mn_utils_rotate_res.links.new(named_attribute_001_1.outputs[0], compare_003_2.inputs[2])
			#boolean_math_002_2.Boolean -> boolean_math_003_1.Boolean
			_mn_utils_rotate_res.links.new(boolean_math_002_2.outputs[0], boolean_math_003_1.inputs[1])
			#compare_003_2.Result -> boolean_math_003_1.Boolean
			_mn_utils_rotate_res.links.new(compare_003_2.outputs[0], boolean_math_003_1.inputs[0])
			#boolean_math_003_1.Boolean -> boolean_math_001_2.Boolean
			_mn_utils_rotate_res.links.new(boolean_math_003_1.outputs[0], boolean_math_001_2.inputs[0])
			#reroute_006.Output -> math_002_1.Value
			_mn_utils_rotate_res.links.new(reroute_006.outputs[0], math_002_1.inputs[0])
			#reroute_007.Output -> math_002_1.Value
			_mn_utils_rotate_res.links.new(reroute_007.outputs[0], math_002_1.inputs[1])
			#group_input_7.Amp. Axis -> reroute_007.Input
			_mn_utils_rotate_res.links.new(group_input_7.outputs[5], reroute_007.inputs[0])
			#map_range_1.Result -> mix_1.B
			_mn_utils_rotate_res.links.new(map_range_1.outputs[0], mix_1.inputs[3])
			#mix_1.Result -> math_1.Value
			_mn_utils_rotate_res.links.new(mix_1.outputs[0], math_1.inputs[0])
			#group_input_7.Scale b_factor -> mix_1.Factor
			_mn_utils_rotate_res.links.new(group_input_7.outputs[3], mix_1.inputs[0])
			#group_001_2.Selection -> boolean_math_2.Boolean
			_mn_utils_rotate_res.links.new(group_001_2.outputs[0], boolean_math_2.inputs[1])
			return _mn_utils_rotate_res

		_mn_utils_rotate_res = _mn_utils_rotate_res_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".MN_utils_rotate_res", type = 'NODES')
		mod.node_group = _mn_utils_rotate_res
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_MN_utils_rotate_res.bl_idname)
			
def register():
	bpy.utils.register_class(_MN_utils_rotate_res)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_MN_utils_rotate_res)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
