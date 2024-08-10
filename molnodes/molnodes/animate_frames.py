bl_info = {
	"name" : "Animate Frames",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Animate_Frames(bpy.types.Operator):
	bl_idname = "node.animate_frames"
	bl_label = "Animate Frames"
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

		#initialize animate_collection_pick node group
		def animate_collection_pick_node_group():
			animate_collection_pick = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Animate Collection Pick")

			animate_collection_pick.color_tag = 'INPUT'
			animate_collection_pick.description = "Pick items from a collection based on the index given. The current and next items in the collection are given for interpolation"

			
			#animate_collection_pick interface
			#Socket Current
			current_socket = animate_collection_pick.interface.new_socket(name = "Current", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			current_socket.attribute_domain = 'POINT'
			
			#Socket Next
			next_socket = animate_collection_pick.interface.new_socket(name = "Next", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			next_socket.attribute_domain = 'POINT'
			
			#Socket Collection
			collection_socket = animate_collection_pick.interface.new_socket(name = "Collection", in_out='INPUT', socket_type = 'NodeSocketCollection')
			collection_socket.attribute_domain = 'POINT'
			
			#Socket Realize Instances
			realize_instances_socket = animate_collection_pick.interface.new_socket(name = "Realize Instances", in_out='INPUT', socket_type = 'NodeSocketBool')
			realize_instances_socket.attribute_domain = 'POINT'
			
			#Socket Item
			item_socket = animate_collection_pick.interface.new_socket(name = "Item", in_out='INPUT', socket_type = 'NodeSocketFloat')
			item_socket.subtype = 'NONE'
			item_socket.default_value = 1.0
			item_socket.min_value = 0.0
			item_socket.max_value = 10000.0
			item_socket.attribute_domain = 'POINT'
			
			
			#initialize animate_collection_pick nodes
			#node Compare
			compare = animate_collection_pick.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'EQUAL'
			
			#node Separate Geometry
			separate_geometry = animate_collection_pick.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry.name = "Separate Geometry"
			separate_geometry.domain = 'INSTANCE'
			
			#node Compare.001
			compare_001 = animate_collection_pick.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'INT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'EQUAL'
			
			#node Separate Geometry.001
			separate_geometry_001 = animate_collection_pick.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_001.name = "Separate Geometry.001"
			separate_geometry_001.domain = 'INSTANCE'
			
			#node Index.001
			index_001 = animate_collection_pick.nodes.new("GeometryNodeInputIndex")
			index_001.name = "Index.001"
			
			#node Reroute.001
			reroute_001 = animate_collection_pick.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			#node Index
			index = animate_collection_pick.nodes.new("GeometryNodeInputIndex")
			index.name = "Index"
			
			#node Math.006
			math_006 = animate_collection_pick.nodes.new("ShaderNodeMath")
			math_006.name = "Math.006"
			math_006.operation = 'MINIMUM'
			math_006.use_clamp = False
			
			#node Group Output
			group_output_1 = animate_collection_pick.nodes.new("NodeGroupOutput")
			group_output_1.name = "Group Output"
			group_output_1.is_active_output = True
			
			#node Realize Instances
			realize_instances = animate_collection_pick.nodes.new("GeometryNodeRealizeInstances")
			realize_instances.name = "Realize Instances"
			#Selection
			realize_instances.inputs[1].default_value = True
			#Depth
			realize_instances.inputs[3].default_value = 0
			
			#node Realize Instances.001
			realize_instances_001 = animate_collection_pick.nodes.new("GeometryNodeRealizeInstances")
			realize_instances_001.name = "Realize Instances.001"
			#Selection
			realize_instances_001.inputs[1].default_value = True
			#Depth
			realize_instances_001.inputs[3].default_value = 0
			
			#node Domain Size
			domain_size = animate_collection_pick.nodes.new("GeometryNodeAttributeDomainSize")
			domain_size.name = "Domain Size"
			domain_size.component = 'INSTANCES'
			
			#node Math.003
			math_003 = animate_collection_pick.nodes.new("ShaderNodeMath")
			math_003.label = "x - 1"
			math_003.name = "Math.003"
			math_003.hide = True
			math_003.operation = 'SUBTRACT'
			math_003.use_clamp = False
			#Value_001
			math_003.inputs[1].default_value = 1.0
			
			#node Math
			math = animate_collection_pick.nodes.new("ShaderNodeMath")
			math.label = "x + 1"
			math.name = "Math"
			math.hide = True
			math.operation = 'ADD'
			math.use_clamp = False
			#Value_001
			math.inputs[1].default_value = 1.0
			
			#node Math.002
			math_002 = animate_collection_pick.nodes.new("ShaderNodeMath")
			math_002.name = "Math.002"
			math_002.operation = 'FLOOR'
			math_002.use_clamp = False
			
			#node Float to Integer
			float_to_integer = animate_collection_pick.nodes.new("FunctionNodeFloatToInt")
			float_to_integer.name = "Float to Integer"
			float_to_integer.rounding_mode = 'ROUND'
			
			#node Collection Info
			collection_info = animate_collection_pick.nodes.new("GeometryNodeCollectionInfo")
			collection_info.name = "Collection Info"
			collection_info.transform_space = 'RELATIVE'
			#Separate Children
			collection_info.inputs[1].default_value = True
			#Reset Children
			collection_info.inputs[2].default_value = False
			
			#node Group Input
			group_input_1 = animate_collection_pick.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			
			
			
			
			#Set locations
			compare.location = (328.0, -140.0)
			separate_geometry.location = (328.0, 20.0)
			compare_001.location = (160.0, -500.0)
			separate_geometry_001.location = (328.0, -380.0)
			index_001.location = (-20.0, -560.0)
			reroute_001.location = (100.0, -240.0)
			index.location = (160.0, -220.0)
			math_006.location = (-20.0, -620.0)
			group_output_1.location = (791.573974609375, 55.48637390136719)
			realize_instances.location = (488.0, 20.0)
			realize_instances_001.location = (488.0, -380.0)
			domain_size.location = (-200.0, -780.0)
			math_003.location = (-200.0, -740.0)
			math.location = (-200.0, -680.0)
			math_002.location = (-600.0, -340.0)
			float_to_integer.location = (-420.0, -340.0)
			collection_info.location = (-420.0, -460.0)
			group_input_1.location = (-787.5955810546875, -365.5730895996094)
			
			#Set dimensions
			compare.width, compare.height = 140.0, 100.0
			separate_geometry.width, separate_geometry.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			separate_geometry_001.width, separate_geometry_001.height = 140.0, 100.0
			index_001.width, index_001.height = 140.0, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			index.width, index.height = 140.0, 100.0
			math_006.width, math_006.height = 140.0, 100.0
			group_output_1.width, group_output_1.height = 140.0, 100.0
			realize_instances.width, realize_instances.height = 134.7681884765625, 100.0
			realize_instances_001.width, realize_instances_001.height = 140.0, 100.0
			domain_size.width, domain_size.height = 140.0, 100.0
			math_003.width, math_003.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			math_002.width, math_002.height = 140.0, 100.0
			float_to_integer.width, float_to_integer.height = 140.0, 100.0
			collection_info.width, collection_info.height = 140.0, 100.0
			group_input_1.width, group_input_1.height = 140.0, 100.0
			
			#initialize animate_collection_pick links
			#group_input_1.Collection -> collection_info.Collection
			animate_collection_pick.links.new(group_input_1.outputs[0], collection_info.inputs[0])
			#reroute_001.Output -> separate_geometry.Geometry
			animate_collection_pick.links.new(reroute_001.outputs[0], separate_geometry.inputs[0])
			#index.Index -> compare.A
			animate_collection_pick.links.new(index.outputs[0], compare.inputs[2])
			#compare.Result -> separate_geometry.Selection
			animate_collection_pick.links.new(compare.outputs[0], separate_geometry.inputs[1])
			#separate_geometry.Selection -> realize_instances.Geometry
			animate_collection_pick.links.new(separate_geometry.outputs[0], realize_instances.inputs[0])
			#float_to_integer.Integer -> compare.B
			animate_collection_pick.links.new(float_to_integer.outputs[0], compare.inputs[3])
			#float_to_integer.Integer -> math.Value
			animate_collection_pick.links.new(float_to_integer.outputs[0], math.inputs[0])
			#reroute_001.Output -> separate_geometry_001.Geometry
			animate_collection_pick.links.new(reroute_001.outputs[0], separate_geometry_001.inputs[0])
			#index_001.Index -> compare_001.A
			animate_collection_pick.links.new(index_001.outputs[0], compare_001.inputs[2])
			#compare_001.Result -> separate_geometry_001.Selection
			animate_collection_pick.links.new(compare_001.outputs[0], separate_geometry_001.inputs[1])
			#separate_geometry_001.Selection -> realize_instances_001.Geometry
			animate_collection_pick.links.new(separate_geometry_001.outputs[0], realize_instances_001.inputs[0])
			#collection_info.Instances -> reroute_001.Input
			animate_collection_pick.links.new(collection_info.outputs[0], reroute_001.inputs[0])
			#collection_info.Instances -> domain_size.Geometry
			animate_collection_pick.links.new(collection_info.outputs[0], domain_size.inputs[0])
			#domain_size.Instance Count -> math_003.Value
			animate_collection_pick.links.new(domain_size.outputs[5], math_003.inputs[0])
			#math_003.Value -> math_006.Value
			animate_collection_pick.links.new(math_003.outputs[0], math_006.inputs[0])
			#math.Value -> math_006.Value
			animate_collection_pick.links.new(math.outputs[0], math_006.inputs[1])
			#math_006.Value -> compare_001.B
			animate_collection_pick.links.new(math_006.outputs[0], compare_001.inputs[3])
			#realize_instances.Geometry -> group_output_1.Current
			animate_collection_pick.links.new(realize_instances.outputs[0], group_output_1.inputs[0])
			#realize_instances_001.Geometry -> group_output_1.Next
			animate_collection_pick.links.new(realize_instances_001.outputs[0], group_output_1.inputs[1])
			#group_input_1.Item -> math_002.Value
			animate_collection_pick.links.new(group_input_1.outputs[2], math_002.inputs[0])
			#math_002.Value -> float_to_integer.Float
			animate_collection_pick.links.new(math_002.outputs[0], float_to_integer.inputs[0])
			#group_input_1.Realize Instances -> realize_instances.Realize All
			animate_collection_pick.links.new(group_input_1.outputs[1], realize_instances.inputs[2])
			#group_input_1.Realize Instances -> realize_instances_001.Realize All
			animate_collection_pick.links.new(group_input_1.outputs[1], realize_instances_001.inputs[2])
			return animate_collection_pick

		animate_collection_pick = animate_collection_pick_node_group()

		#initialize animate_fraction node group
		def animate_fraction_node_group():
			animate_fraction = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Animate Fraction")

			animate_fraction.color_tag = 'CONVERTER'
			animate_fraction.description = "Interpolate the fraction component of a float"

			
			#animate_fraction interface
			#Socket Float
			float_socket = animate_fraction.interface.new_socket(name = "Float", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			float_socket.subtype = 'NONE'
			float_socket.default_value = 0.0
			float_socket.min_value = -3.4028234663852886e+38
			float_socket.max_value = 3.4028234663852886e+38
			float_socket.attribute_domain = 'POINT'
			
			#Socket Interpolate
			interpolate_socket = animate_fraction.interface.new_socket(name = "Interpolate", in_out='INPUT', socket_type = 'NodeSocketBool')
			interpolate_socket.attribute_domain = 'POINT'
			
			#Socket Smoother Step
			smoother_step_socket = animate_fraction.interface.new_socket(name = "Smoother Step", in_out='INPUT', socket_type = 'NodeSocketBool')
			smoother_step_socket.attribute_domain = 'POINT'
			
			#Socket Float
			float_socket_1 = animate_fraction.interface.new_socket(name = "Float", in_out='INPUT', socket_type = 'NodeSocketFloat')
			float_socket_1.subtype = 'NONE'
			float_socket_1.default_value = 0.0
			float_socket_1.min_value = -3.4028234663852886e+38
			float_socket_1.max_value = 3.4028234663852886e+38
			float_socket_1.attribute_domain = 'POINT'
			
			
			#initialize animate_fraction nodes
			#node Group Output
			group_output_2 = animate_fraction.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Switch
			switch = animate_fraction.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'FLOAT'
			
			#node Group Input
			group_input_2 = animate_fraction.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
			#node Switch.001
			switch_001 = animate_fraction.nodes.new("GeometryNodeSwitch")
			switch_001.name = "Switch.001"
			switch_001.input_type = 'FLOAT'
			
			#node Map Range
			map_range = animate_fraction.nodes.new("ShaderNodeMapRange")
			map_range.name = "Map Range"
			map_range.clamp = True
			map_range.data_type = 'FLOAT'
			map_range.interpolation_type = 'SMOOTHERSTEP'
			#From Min
			map_range.inputs[1].default_value = 0.0
			#From Max
			map_range.inputs[2].default_value = 1.0
			#To Min
			map_range.inputs[3].default_value = 0.0
			#To Max
			map_range.inputs[4].default_value = 1.0
			
			#node Math
			math_1 = animate_fraction.nodes.new("ShaderNodeMath")
			math_1.name = "Math"
			math_1.operation = 'FLOOR'
			math_1.use_clamp = False
			
			#node Math.001
			math_001 = animate_fraction.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.operation = 'FRACT'
			math_001.use_clamp = False
			
			
			
			
			#Set locations
			group_output_2.location = (-80.0, 160.0)
			switch.location = (-460.0, -80.0)
			group_input_2.location = (-860.0, 120.0)
			switch_001.location = (-260.0, 160.0)
			map_range.location = (-460.0, -240.0)
			math_1.location = (-460.0, 80.0)
			math_001.location = (-640.0, -140.0)
			
			#Set dimensions
			group_output_2.width, group_output_2.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			group_input_2.width, group_input_2.height = 140.0, 100.0
			switch_001.width, switch_001.height = 140.0, 100.0
			map_range.width, map_range.height = 140.0, 100.0
			math_1.width, math_1.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			
			#initialize animate_fraction links
			#group_input_2.Float -> math_001.Value
			animate_fraction.links.new(group_input_2.outputs[2], math_001.inputs[0])
			#math_001.Value -> map_range.Value
			animate_fraction.links.new(math_001.outputs[0], map_range.inputs[0])
			#map_range.Result -> switch.True
			animate_fraction.links.new(map_range.outputs[0], switch.inputs[2])
			#group_input_2.Smoother Step -> switch.Switch
			animate_fraction.links.new(group_input_2.outputs[1], switch.inputs[0])
			#math_001.Value -> switch.False
			animate_fraction.links.new(math_001.outputs[0], switch.inputs[1])
			#switch.Output -> switch_001.True
			animate_fraction.links.new(switch.outputs[0], switch_001.inputs[2])
			#group_input_2.Interpolate -> switch_001.Switch
			animate_fraction.links.new(group_input_2.outputs[0], switch_001.inputs[0])
			#group_input_2.Float -> math_1.Value
			animate_fraction.links.new(group_input_2.outputs[2], math_1.inputs[0])
			#math_1.Value -> switch_001.False
			animate_fraction.links.new(math_1.outputs[0], switch_001.inputs[1])
			#switch_001.Output -> group_output_2.Float
			animate_fraction.links.new(switch_001.outputs[0], group_output_2.inputs[0])
			return animate_fraction

		animate_fraction = animate_fraction_node_group()

		#initialize sample_mix_float node group
		def sample_mix_float_node_group():
			sample_mix_float = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Sample Mix Float")

			sample_mix_float.color_tag = 'GEOMETRY'
			sample_mix_float.description = ""

			
			#sample_mix_float interface
			#Socket Value
			value_socket = sample_mix_float.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			value_socket.subtype = 'NONE'
			value_socket.default_value = 0.0
			value_socket.min_value = -3.4028234663852886e+38
			value_socket.max_value = 3.4028234663852886e+38
			value_socket.attribute_domain = 'POINT'
			
			#Socket A
			a_socket_1 = sample_mix_float.interface.new_socket(name = "A", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			a_socket_1.attribute_domain = 'POINT'
			
			#Socket B
			b_socket_1 = sample_mix_float.interface.new_socket(name = "B", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			b_socket_1.attribute_domain = 'POINT'
			
			#Socket Factor
			factor_socket_1 = sample_mix_float.interface.new_socket(name = "Factor", in_out='INPUT', socket_type = 'NodeSocketFloat')
			factor_socket_1.subtype = 'FACTOR'
			factor_socket_1.default_value = 0.5
			factor_socket_1.min_value = 0.0
			factor_socket_1.max_value = 1.0
			factor_socket_1.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_1 = sample_mix_float.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket_1.subtype = 'NONE'
			value_socket_1.default_value = 0.0
			value_socket_1.min_value = -3.4028234663852886e+38
			value_socket_1.max_value = 3.4028234663852886e+38
			value_socket_1.attribute_domain = 'POINT'
			value_socket_1.hide_value = True
			
			#Socket Index
			index_socket_1 = sample_mix_float.interface.new_socket(name = "Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			index_socket_1.subtype = 'NONE'
			index_socket_1.default_value = 0
			index_socket_1.min_value = -2147483648
			index_socket_1.max_value = 2147483647
			index_socket_1.attribute_domain = 'POINT'
			
			
			#initialize sample_mix_float nodes
			#node Group Output
			group_output_3 = sample_mix_float.nodes.new("NodeGroupOutput")
			group_output_3.name = "Group Output"
			group_output_3.is_active_output = True
			
			#node Sample Index.002
			sample_index_002_1 = sample_mix_float.nodes.new("GeometryNodeSampleIndex")
			sample_index_002_1.name = "Sample Index.002"
			sample_index_002_1.clamp = False
			sample_index_002_1.data_type = 'FLOAT'
			sample_index_002_1.domain = 'POINT'
			
			#node Sample Index.003
			sample_index_003_1 = sample_mix_float.nodes.new("GeometryNodeSampleIndex")
			sample_index_003_1.name = "Sample Index.003"
			sample_index_003_1.clamp = False
			sample_index_003_1.data_type = 'FLOAT'
			sample_index_003_1.domain = 'POINT'
			
			#node Group Input
			group_input_3 = sample_mix_float.nodes.new("NodeGroupInput")
			group_input_3.name = "Group Input"
			
			#node Mix
			mix = sample_mix_float.nodes.new("ShaderNodeMix")
			mix.name = "Mix"
			mix.blend_type = 'MIX'
			mix.clamp_factor = True
			mix.clamp_result = False
			mix.data_type = 'FLOAT'
			mix.factor_mode = 'UNIFORM'
			
			
			
			
			#Set locations
			group_output_3.location = (360.0, 180.0)
			sample_index_002_1.location = (-40.0, 260.0)
			sample_index_003_1.location = (-40.0, 60.0)
			group_input_3.location = (-492.72479248046875, -5.606773376464844)
			mix.location = (160.8731689453125, 214.3348846435547)
			
			#Set dimensions
			group_output_3.width, group_output_3.height = 140.0, 100.0
			sample_index_002_1.width, sample_index_002_1.height = 140.0, 100.0
			sample_index_003_1.width, sample_index_003_1.height = 140.0, 100.0
			group_input_3.width, group_input_3.height = 140.0, 100.0
			mix.width, mix.height = 140.0, 100.0
			
			#initialize sample_mix_float links
			#group_input_3.A -> sample_index_002_1.Geometry
			sample_mix_float.links.new(group_input_3.outputs[0], sample_index_002_1.inputs[0])
			#group_input_3.B -> sample_index_003_1.Geometry
			sample_mix_float.links.new(group_input_3.outputs[1], sample_index_003_1.inputs[0])
			#group_input_3.Value -> sample_index_002_1.Value
			sample_mix_float.links.new(group_input_3.outputs[3], sample_index_002_1.inputs[1])
			#group_input_3.Value -> sample_index_003_1.Value
			sample_mix_float.links.new(group_input_3.outputs[3], sample_index_003_1.inputs[1])
			#sample_index_002_1.Value -> mix.A
			sample_mix_float.links.new(sample_index_002_1.outputs[0], mix.inputs[2])
			#sample_index_003_1.Value -> mix.B
			sample_mix_float.links.new(sample_index_003_1.outputs[0], mix.inputs[3])
			#group_input_3.Factor -> mix.Factor
			sample_mix_float.links.new(group_input_3.outputs[2], mix.inputs[0])
			#mix.Result -> group_output_3.Value
			sample_mix_float.links.new(mix.outputs[0], group_output_3.inputs[0])
			#group_input_3.Index -> sample_index_002_1.Index
			sample_mix_float.links.new(group_input_3.outputs[4], sample_index_002_1.inputs[2])
			#group_input_3.Index -> sample_index_003_1.Index
			sample_mix_float.links.new(group_input_3.outputs[4], sample_index_003_1.inputs[2])
			return sample_mix_float

		sample_mix_float = sample_mix_float_node_group()

		#initialize animate_frames node group
		def animate_frames_node_group():
			animate_frames = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Animate Frames")

			animate_frames.color_tag = 'GEOMETRY'
			animate_frames.description = ""

			animate_frames.is_modifier = True
			
			#animate_frames interface
			#Socket Atoms
			atoms_socket = animate_frames.interface.new_socket(name = "Atoms", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket.attribute_domain = 'POINT'
			atoms_socket.description = "Atomic geometry with new positions based on the trajectory"
			
			#Socket Atoms
			atoms_socket_1 = animate_frames.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_1.attribute_domain = 'POINT'
			atoms_socket_1.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket = animate_frames.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket.attribute_domain = 'POINT'
			selection_socket.hide_value = True
			selection_socket.description = "Selection of atoms to apply this node to"
			
			#Socket Frames
			frames_socket = animate_frames.interface.new_socket(name = "Frames", in_out='INPUT', socket_type = 'NodeSocketCollection')
			frames_socket.attribute_domain = 'POINT'
			frames_socket.description = "Collection which holds the frames of the trajectory"
			
			#Socket Smoother Step
			smoother_step_socket_1 = animate_frames.interface.new_socket(name = "Smoother Step", in_out='INPUT', socket_type = 'NodeSocketBool')
			smoother_step_socket_1.attribute_domain = 'POINT'
			smoother_step_socket_1.description = "Ease in and out of the individual frames if interpolating"
			
			#Socket Interpolate
			interpolate_socket_1 = animate_frames.interface.new_socket(name = "Interpolate", in_out='INPUT', socket_type = 'NodeSocketBool')
			interpolate_socket_1.attribute_domain = 'POINT'
			interpolate_socket_1.description = "Whether to interpolate between frames of a trajectory or snap"
			
			#Socket Frame
			frame_socket = animate_frames.interface.new_socket(name = "Frame", in_out='INPUT', socket_type = 'NodeSocketFloat')
			frame_socket.subtype = 'NONE'
			frame_socket.default_value = 0.0
			frame_socket.min_value = 0.0
			frame_socket.max_value = 10000.0
			frame_socket.attribute_domain = 'POINT'
			frame_socket.description = "Which frame to select from the collection. The fraction component of the float is how much to interpolate between the current and next frame"
			
			
			#initialize animate_frames nodes
			#node Named Attribute.001
			named_attribute_001 = animate_frames.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.data_type = 'FLOAT'
			#Name
			named_attribute_001.inputs[0].default_value = "b_factor"
			
			#node Group Input
			group_input_4 = animate_frames.nodes.new("NodeGroupInput")
			group_input_4.name = "Group Input"
			
			#node Object Info
			object_info = animate_frames.nodes.new("GeometryNodeObjectInfo")
			object_info.name = "Object Info"
			object_info.transform_space = 'ORIGINAL'
			#As Instance
			object_info.inputs[1].default_value = False
			
			#node Transform
			transform = animate_frames.nodes.new("GeometryNodeTransform")
			transform.name = "Transform"
			transform.mode = 'COMPONENTS'
			
			#node Self Object
			self_object = animate_frames.nodes.new("GeometryNodeSelfObject")
			self_object.name = "Self Object"
			
			#node Group Output
			group_output_4 = animate_frames.nodes.new("NodeGroupOutput")
			group_output_4.name = "Group Output"
			group_output_4.is_active_output = True
			
			#node Group.002
			group_002 = animate_frames.nodes.new("GeometryNodeGroup")
			group_002.name = "Group.002"
			group_002.node_tree = sample_mix_vector
			#Socket_6
			group_002.inputs[3].default_value = (0.0, 0.0, 0.0)
			#Socket_9
			group_002.inputs[4].default_value = 0
			
			#node Set Position
			set_position = animate_frames.nodes.new("GeometryNodeSetPosition")
			set_position.name = "Set Position"
			#Offset
			set_position.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Group.001
			group_001 = animate_frames.nodes.new("GeometryNodeGroup")
			group_001.name = "Group.001"
			group_001.node_tree = animate_collection_pick
			#Socket_2
			group_001.inputs[1].default_value = True
			
			#node Group
			group = animate_frames.nodes.new("GeometryNodeGroup")
			group.name = "Group"
			group.node_tree = animate_fraction
			
			#node Vector Math
			vector_math = animate_frames.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.operation = 'ABSOLUTE'
			
			#node Group.003
			group_003 = animate_frames.nodes.new("GeometryNodeGroup")
			group_003.name = "Group.003"
			group_003.node_tree = sample_mix_float
			#Socket_9
			group_003.inputs[4].default_value = 0
			
			#node Store Named Attribute
			store_named_attribute = animate_frames.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute.name = "Store Named Attribute"
			store_named_attribute.data_type = 'FLOAT'
			store_named_attribute.domain = 'POINT'
			#Selection
			store_named_attribute.inputs[1].default_value = True
			#Name
			store_named_attribute.inputs[2].default_value = "b_factor"
			
			
			
			
			#Set locations
			named_attribute_001.location = (-320.0, -220.0)
			group_input_4.location = (-720.0, 260.0)
			object_info.location = (540.0, 200.0)
			transform.location = (740.0, 300.0)
			self_object.location = (380.0, 40.0)
			group_output_4.location = (960.0, 280.0)
			group_002.location = (-100.0, 160.0)
			set_position.location = (180.0, 280.0)
			group_001.location = (-400.0, 100.0)
			group.location = (-400.0, -60.0)
			vector_math.location = (740.0, 120.0)
			group_003.location = (-100.0, -60.0)
			store_named_attribute.location = (360.0, 280.0)
			
			#Set dimensions
			named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
			group_input_4.width, group_input_4.height = 140.0, 100.0
			object_info.width, object_info.height = 140.0, 100.0
			transform.width, transform.height = 140.0, 100.0
			self_object.width, self_object.height = 140.0, 100.0
			group_output_4.width, group_output_4.height = 140.0, 100.0
			group_002.width, group_002.height = 235.44537353515625, 100.0
			set_position.width, set_position.height = 140.0, 100.0
			group_001.width, group_001.height = 222.0662841796875, 100.0
			group.width, group.height = 214.65057373046875, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			group_003.width, group_003.height = 235.44537353515625, 100.0
			store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
			
			#initialize animate_frames links
			#transform.Geometry -> group_output_4.Atoms
			animate_frames.links.new(transform.outputs[0], group_output_4.inputs[0])
			#self_object.Self Object -> object_info.Object
			animate_frames.links.new(self_object.outputs[0], object_info.inputs[0])
			#object_info.Location -> transform.Translation
			animate_frames.links.new(object_info.outputs[1], transform.inputs[1])
			#object_info.Rotation -> transform.Rotation
			animate_frames.links.new(object_info.outputs[2], transform.inputs[2])
			#vector_math.Vector -> transform.Scale
			animate_frames.links.new(vector_math.outputs[0], transform.inputs[3])
			#store_named_attribute.Geometry -> transform.Geometry
			animate_frames.links.new(store_named_attribute.outputs[0], transform.inputs[0])
			#group_input_4.Atoms -> set_position.Geometry
			animate_frames.links.new(group_input_4.outputs[0], set_position.inputs[0])
			#group_input_4.Selection -> set_position.Selection
			animate_frames.links.new(group_input_4.outputs[1], set_position.inputs[1])
			#group_001.Current -> group_002.A
			animate_frames.links.new(group_001.outputs[0], group_002.inputs[0])
			#group_001.Next -> group_002.B
			animate_frames.links.new(group_001.outputs[1], group_002.inputs[1])
			#group_input_4.Frame -> group_001.Item
			animate_frames.links.new(group_input_4.outputs[5], group_001.inputs[2])
			#group_002.Vector -> set_position.Position
			animate_frames.links.new(group_002.outputs[0], set_position.inputs[2])
			#group.Float -> group_002.Factor
			animate_frames.links.new(group.outputs[0], group_002.inputs[2])
			#group_input_4.Frame -> group.Float
			animate_frames.links.new(group_input_4.outputs[5], group.inputs[2])
			#group_input_4.Interpolate -> group.Interpolate
			animate_frames.links.new(group_input_4.outputs[4], group.inputs[0])
			#group_input_4.Smoother Step -> group.Smoother Step
			animate_frames.links.new(group_input_4.outputs[3], group.inputs[1])
			#object_info.Scale -> vector_math.Vector
			animate_frames.links.new(object_info.outputs[3], vector_math.inputs[0])
			#group_001.Current -> group_003.A
			animate_frames.links.new(group_001.outputs[0], group_003.inputs[0])
			#group_001.Next -> group_003.B
			animate_frames.links.new(group_001.outputs[1], group_003.inputs[1])
			#group.Float -> group_003.Factor
			animate_frames.links.new(group.outputs[0], group_003.inputs[2])
			#group_input_4.Frames -> group_001.Collection
			animate_frames.links.new(group_input_4.outputs[2], group_001.inputs[0])
			#named_attribute_001.Attribute -> group_003.Value
			animate_frames.links.new(named_attribute_001.outputs[0], group_003.inputs[3])
			#set_position.Geometry -> store_named_attribute.Geometry
			animate_frames.links.new(set_position.outputs[0], store_named_attribute.inputs[0])
			#group_003.Value -> store_named_attribute.Value
			animate_frames.links.new(group_003.outputs[0], store_named_attribute.inputs[3])
			return animate_frames

		animate_frames = animate_frames_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Animate Frames", type = 'NODES')
		mod.node_group = animate_frames
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Animate_Frames.bl_idname)
			
def register():
	bpy.utils.register_class(Animate_Frames)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Animate_Frames)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
