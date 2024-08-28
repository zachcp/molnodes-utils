bl_info = {
	"name" : ".MN_topo_calc_sheet",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _MN_topo_calc_sheet(bpy.types.Operator):
	bl_idname = "node._mn_topo_calc_sheet"
	bl_label = ".MN_topo_calc_sheet"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize boolean_run_mask node group
		def boolean_run_mask_node_group():
			boolean_run_mask = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Boolean Run Mask")

			boolean_run_mask.color_tag = 'CONVERTER'
			boolean_run_mask.description = ""

			
			#boolean_run_mask interface
			#Socket Boolean
			boolean_socket = boolean_run_mask.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket.default_value = False
			boolean_socket.attribute_domain = 'POINT'
			
			#Socket Boolean
			boolean_socket_1 = boolean_run_mask.interface.new_socket(name = "Boolean", in_out='INPUT', socket_type = 'NodeSocketBool')
			boolean_socket_1.default_value = False
			boolean_socket_1.attribute_domain = 'POINT'
			
			#Socket Lag Start
			lag_start_socket = boolean_run_mask.interface.new_socket(name = "Lag Start", in_out='INPUT', socket_type = 'NodeSocketInt')
			lag_start_socket.default_value = 0
			lag_start_socket.min_value = 0
			lag_start_socket.max_value = 2147483647
			lag_start_socket.subtype = 'NONE'
			lag_start_socket.attribute_domain = 'POINT'
			lag_start_socket.description = "The first N values in a run are made to be false"
			
			#Socket Min Length
			min_length_socket = boolean_run_mask.interface.new_socket(name = "Min Length", in_out='INPUT', socket_type = 'NodeSocketInt')
			min_length_socket.default_value = 0
			min_length_socket.min_value = 0
			min_length_socket.max_value = 2147483647
			min_length_socket.subtype = 'NONE'
			min_length_socket.attribute_domain = 'POINT'
			min_length_socket.description = "Run is only valid if it contains at least N values"
			
			#Socket Trim End
			trim_end_socket = boolean_run_mask.interface.new_socket(name = "Trim End", in_out='INPUT', socket_type = 'NodeSocketInt')
			trim_end_socket.default_value = 0
			trim_end_socket.min_value = -2147483648
			trim_end_socket.max_value = 2147483647
			trim_end_socket.subtype = 'NONE'
			trim_end_socket.attribute_domain = 'POINT'
			
			
			#initialize boolean_run_mask nodes
			#node Group Output
			group_output = boolean_run_mask.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = boolean_run_mask.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			group_input.outputs[3].hide = True
			
			#node Accumulate Field
			accumulate_field = boolean_run_mask.nodes.new("GeometryNodeAccumulateField")
			accumulate_field.name = "Accumulate Field"
			accumulate_field.data_type = 'INT'
			accumulate_field.domain = 'POINT'
			#Group Index
			accumulate_field.inputs[1].default_value = 0
			
			#node Boolean Math.001
			boolean_math_001 = boolean_run_mask.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001.name = "Boolean Math.001"
			boolean_math_001.operation = 'NOT'
			
			#node Accumulate Field.001
			accumulate_field_001 = boolean_run_mask.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_001.name = "Accumulate Field.001"
			accumulate_field_001.data_type = 'INT'
			accumulate_field_001.domain = 'POINT'
			#Value
			accumulate_field_001.inputs[0].default_value = 1
			
			#node Compare
			compare = boolean_run_mask.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'GREATER_THAN'
			
			#node Boolean Math.002
			boolean_math_002 = boolean_run_mask.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002.name = "Boolean Math.002"
			boolean_math_002.operation = 'AND'
			
			#node Reroute
			reroute = boolean_run_mask.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Boolean Math.003
			boolean_math_003 = boolean_run_mask.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003.name = "Boolean Math.003"
			boolean_math_003.operation = 'AND'
			
			#node Compare.001
			compare_001 = boolean_run_mask.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'INT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'GREATER_THAN'
			
			#node Boolean Math.004
			boolean_math_004 = boolean_run_mask.nodes.new("FunctionNodeBooleanMath")
			boolean_math_004.name = "Boolean Math.004"
			boolean_math_004.operation = 'AND'
			
			#node Compare.002
			compare_002 = boolean_run_mask.nodes.new("FunctionNodeCompare")
			compare_002.name = "Compare.002"
			compare_002.data_type = 'INT'
			compare_002.mode = 'ELEMENT'
			compare_002.operation = 'GREATER_THAN'
			
			#node Math
			math = boolean_run_mask.nodes.new("ShaderNodeMath")
			math.name = "Math"
			math.operation = 'SUBTRACT'
			math.use_clamp = False
			
			#node Group Input.001
			group_input_001 = boolean_run_mask.nodes.new("NodeGroupInput")
			group_input_001.name = "Group Input.001"
			group_input_001.outputs[0].hide = True
			group_input_001.outputs[1].hide = True
			group_input_001.outputs[2].hide = True
			group_input_001.outputs[4].hide = True
			
			
			
			
			#Set locations
			group_output.location = (860.0001220703125, 60.0)
			group_input.location = (-460.0031433105469, 0.0)
			accumulate_field.location = (-100.0, -300.0)
			boolean_math_001.location = (-260.0, -300.0)
			accumulate_field_001.location = (60.0, -300.0)
			compare.location = (260.0031433105469, -80.0)
			boolean_math_002.location = (260.0, 60.0)
			reroute.location = (-260.0031433105469, -29.36541748046875)
			boolean_math_003.location = (420.0, 60.0)
			compare_001.location = (420.0, -80.0)
			boolean_math_004.location = (580.0, 60.0)
			compare_002.location = (580.0, -80.0)
			math.location = (420.0, -240.0)
			group_input_001.location = (580.0, -240.0)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			accumulate_field.width, accumulate_field.height = 140.0, 100.0
			boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
			accumulate_field_001.width, accumulate_field_001.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			boolean_math_002.width, boolean_math_002.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			boolean_math_003.width, boolean_math_003.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			boolean_math_004.width, boolean_math_004.height = 140.0, 100.0
			compare_002.width, compare_002.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			group_input_001.width, group_input_001.height = 140.0, 100.0
			
			#initialize boolean_run_mask links
			#boolean_math_001.Boolean -> accumulate_field.Value
			boolean_run_mask.links.new(boolean_math_001.outputs[0], accumulate_field.inputs[0])
			#reroute.Output -> boolean_math_001.Boolean
			boolean_run_mask.links.new(reroute.outputs[0], boolean_math_001.inputs[0])
			#compare.Result -> boolean_math_002.Boolean
			boolean_run_mask.links.new(compare.outputs[0], boolean_math_002.inputs[1])
			#group_input.Boolean -> reroute.Input
			boolean_run_mask.links.new(group_input.outputs[0], reroute.inputs[0])
			#boolean_math_004.Boolean -> group_output.Boolean
			boolean_run_mask.links.new(boolean_math_004.outputs[0], group_output.inputs[0])
			#group_input.Lag Start -> compare.B
			boolean_run_mask.links.new(group_input.outputs[1], compare.inputs[3])
			#boolean_math_002.Boolean -> boolean_math_003.Boolean
			boolean_run_mask.links.new(boolean_math_002.outputs[0], boolean_math_003.inputs[0])
			#accumulate_field_001.Total -> compare_001.A
			boolean_run_mask.links.new(accumulate_field_001.outputs[2], compare_001.inputs[2])
			#group_input.Min Length -> compare_001.B
			boolean_run_mask.links.new(group_input.outputs[2], compare_001.inputs[3])
			#compare_001.Result -> boolean_math_003.Boolean
			boolean_run_mask.links.new(compare_001.outputs[0], boolean_math_003.inputs[1])
			#reroute.Output -> boolean_math_002.Boolean
			boolean_run_mask.links.new(reroute.outputs[0], boolean_math_002.inputs[0])
			#accumulate_field.Trailing -> accumulate_field_001.Group ID
			boolean_run_mask.links.new(accumulate_field.outputs[1], accumulate_field_001.inputs[1])
			#boolean_math_003.Boolean -> boolean_math_004.Boolean
			boolean_run_mask.links.new(boolean_math_003.outputs[0], boolean_math_004.inputs[0])
			#accumulate_field_001.Total -> math.Value
			boolean_run_mask.links.new(accumulate_field_001.outputs[2], math.inputs[0])
			#accumulate_field_001.Leading -> math.Value
			boolean_run_mask.links.new(accumulate_field_001.outputs[0], math.inputs[1])
			#math.Value -> compare_002.A
			boolean_run_mask.links.new(math.outputs[0], compare_002.inputs[2])
			#group_input_001.Trim End -> compare_002.B
			boolean_run_mask.links.new(group_input_001.outputs[3], compare_002.inputs[3])
			#compare_002.Result -> boolean_math_004.Boolean
			boolean_run_mask.links.new(compare_002.outputs[0], boolean_math_004.inputs[1])
			#accumulate_field_001.Leading -> compare.A
			boolean_run_mask.links.new(accumulate_field_001.outputs[0], compare.inputs[2])
			return boolean_run_mask

		boolean_run_mask = boolean_run_mask_node_group()

		#initialize boolean_run_fill node group
		def boolean_run_fill_node_group():
			boolean_run_fill = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Boolean Run Fill")

			boolean_run_fill.color_tag = 'CONVERTER'
			boolean_run_fill.description = ""

			
			#boolean_run_fill interface
			#Socket Boolean
			boolean_socket_2 = boolean_run_fill.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket_2.default_value = False
			boolean_socket_2.attribute_domain = 'POINT'
			
			#Socket Boolean
			boolean_socket_3 = boolean_run_fill.interface.new_socket(name = "Boolean", in_out='INPUT', socket_type = 'NodeSocketBool')
			boolean_socket_3.default_value = False
			boolean_socket_3.attribute_domain = 'POINT'
			boolean_socket_3.description = "Boolean array to fill runs of False"
			
			#Socket Fill Size
			fill_size_socket = boolean_run_fill.interface.new_socket(name = "Fill Size", in_out='INPUT', socket_type = 'NodeSocketInt')
			fill_size_socket.default_value = 3
			fill_size_socket.min_value = -2147483648
			fill_size_socket.max_value = 2147483647
			fill_size_socket.subtype = 'NONE'
			fill_size_socket.attribute_domain = 'POINT'
			fill_size_socket.description = "Set a run of False to True if length equal or less than Fill Size"
			
			
			#initialize boolean_run_fill nodes
			#node Group Output
			group_output_1 = boolean_run_fill.nodes.new("NodeGroupOutput")
			group_output_1.name = "Group Output"
			group_output_1.is_active_output = True
			
			#node Group Input
			group_input_1 = boolean_run_fill.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			
			#node Accumulate Field
			accumulate_field_1 = boolean_run_fill.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_1.name = "Accumulate Field"
			accumulate_field_1.data_type = 'INT'
			accumulate_field_1.domain = 'POINT'
			#Group Index
			accumulate_field_1.inputs[1].default_value = 0
			
			#node Accumulate Field.001
			accumulate_field_001_1 = boolean_run_fill.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_001_1.name = "Accumulate Field.001"
			accumulate_field_001_1.data_type = 'INT'
			accumulate_field_001_1.domain = 'POINT'
			#Value
			accumulate_field_001_1.inputs[0].default_value = 1
			
			#node Compare
			compare_1 = boolean_run_fill.nodes.new("FunctionNodeCompare")
			compare_1.name = "Compare"
			compare_1.data_type = 'INT'
			compare_1.mode = 'ELEMENT'
			compare_1.operation = 'LESS_EQUAL'
			
			#node Compare.001
			compare_001_1 = boolean_run_fill.nodes.new("FunctionNodeCompare")
			compare_001_1.name = "Compare.001"
			compare_001_1.data_type = 'INT'
			compare_001_1.mode = 'ELEMENT'
			compare_001_1.operation = 'LESS_EQUAL'
			
			#node Boolean Math.010
			boolean_math_010 = boolean_run_fill.nodes.new("FunctionNodeBooleanMath")
			boolean_math_010.name = "Boolean Math.010"
			boolean_math_010.operation = 'AND'
			
			#node Boolean Math
			boolean_math = boolean_run_fill.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'OR'
			
			#node Reroute
			reroute_1 = boolean_run_fill.nodes.new("NodeReroute")
			reroute_1.name = "Reroute"
			#node Reroute.001
			reroute_001 = boolean_run_fill.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			#node Reroute.003
			reroute_003 = boolean_run_fill.nodes.new("NodeReroute")
			reroute_003.name = "Reroute.003"
			#node Reroute.002
			reroute_002 = boolean_run_fill.nodes.new("NodeReroute")
			reroute_002.name = "Reroute.002"
			
			
			
			#Set locations
			group_output_1.location = (430.0, 0.0)
			group_input_1.location = (-480.0, -20.0)
			accumulate_field_1.location = (-220.0, -120.0)
			accumulate_field_001_1.location = (-60.0, -120.0)
			compare_1.location = (100.0, -120.0)
			compare_001_1.location = (100.0, -280.0)
			boolean_math_010.location = (260.0, -120.0)
			boolean_math.location = (260.0, 20.0)
			reroute_1.location = (60.0, -380.0)
			reroute_001.location = (-280.0, -380.0)
			reroute_003.location = (-300.0, -80.0)
			reroute_002.location = (-240.0, -60.0)
			
			#Set dimensions
			group_output_1.width, group_output_1.height = 140.0, 100.0
			group_input_1.width, group_input_1.height = 140.0, 100.0
			accumulate_field_1.width, accumulate_field_1.height = 140.0, 100.0
			accumulate_field_001_1.width, accumulate_field_001_1.height = 140.0, 100.0
			compare_1.width, compare_1.height = 140.0, 100.0
			compare_001_1.width, compare_001_1.height = 140.0, 100.0
			boolean_math_010.width, boolean_math_010.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			reroute_1.width, reroute_1.height = 16.0, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			reroute_003.width, reroute_003.height = 16.0, 100.0
			reroute_002.width, reroute_002.height = 16.0, 100.0
			
			#initialize boolean_run_fill links
			#accumulate_field_001_1.Trailing -> compare_1.A
			boolean_run_fill.links.new(accumulate_field_001_1.outputs[1], compare_1.inputs[2])
			#accumulate_field_1.Leading -> accumulate_field_001_1.Group ID
			boolean_run_fill.links.new(accumulate_field_1.outputs[0], accumulate_field_001_1.inputs[1])
			#compare_001_1.Result -> boolean_math_010.Boolean
			boolean_run_fill.links.new(compare_001_1.outputs[0], boolean_math_010.inputs[1])
			#compare_1.Result -> boolean_math_010.Boolean
			boolean_run_fill.links.new(compare_1.outputs[0], boolean_math_010.inputs[0])
			#accumulate_field_001_1.Total -> compare_001_1.A
			boolean_run_fill.links.new(accumulate_field_001_1.outputs[2], compare_001_1.inputs[2])
			#reroute_1.Output -> compare_1.B
			boolean_run_fill.links.new(reroute_1.outputs[0], compare_1.inputs[3])
			#reroute_1.Output -> compare_001_1.B
			boolean_run_fill.links.new(reroute_1.outputs[0], compare_001_1.inputs[3])
			#reroute_002.Output -> accumulate_field_1.Value
			boolean_run_fill.links.new(reroute_002.outputs[0], accumulate_field_1.inputs[0])
			#reroute_002.Output -> boolean_math.Boolean
			boolean_run_fill.links.new(reroute_002.outputs[0], boolean_math.inputs[0])
			#boolean_math_010.Boolean -> boolean_math.Boolean
			boolean_run_fill.links.new(boolean_math_010.outputs[0], boolean_math.inputs[1])
			#boolean_math.Boolean -> group_output_1.Boolean
			boolean_run_fill.links.new(boolean_math.outputs[0], group_output_1.inputs[0])
			#reroute_001.Output -> reroute_1.Input
			boolean_run_fill.links.new(reroute_001.outputs[0], reroute_1.inputs[0])
			#reroute_003.Output -> reroute_001.Input
			boolean_run_fill.links.new(reroute_003.outputs[0], reroute_001.inputs[0])
			#group_input_1.Fill Size -> reroute_003.Input
			boolean_run_fill.links.new(group_input_1.outputs[1], reroute_003.inputs[0])
			#group_input_1.Boolean -> reroute_002.Input
			boolean_run_fill.links.new(group_input_1.outputs[0], reroute_002.inputs[0])
			return boolean_run_fill

		boolean_run_fill = boolean_run_fill_node_group()

		#initialize self_sample_proximity node group
		def self_sample_proximity_node_group():
			self_sample_proximity = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Self Sample Proximity")

			self_sample_proximity.color_tag = 'NONE'
			self_sample_proximity.description = ""

			
			#self_sample_proximity interface
			#Socket Closest Index
			closest_index_socket = self_sample_proximity.interface.new_socket(name = "Closest Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			closest_index_socket.default_value = 0
			closest_index_socket.min_value = -2147483648
			closest_index_socket.max_value = 2147483647
			closest_index_socket.subtype = 'NONE'
			closest_index_socket.attribute_domain = 'POINT'
			
			#Socket Input
			input_socket = self_sample_proximity.interface.new_socket(name = "Input", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			input_socket.attribute_domain = 'POINT'
			
			#Socket Target Position
			target_position_socket = self_sample_proximity.interface.new_socket(name = "Target Position", in_out='INPUT', socket_type = 'NodeSocketVector')
			target_position_socket.default_value = (0.0, 0.0, 0.0)
			target_position_socket.min_value = -3.4028234663852886e+38
			target_position_socket.max_value = 3.4028234663852886e+38
			target_position_socket.subtype = 'NONE'
			target_position_socket.attribute_domain = 'POINT'
			
			#Socket Self Position
			self_position_socket = self_sample_proximity.interface.new_socket(name = "Self Position", in_out='INPUT', socket_type = 'NodeSocketVector')
			self_position_socket.default_value = (0.0, 0.0, 0.0)
			self_position_socket.min_value = -3.4028234663852886e+38
			self_position_socket.max_value = 3.4028234663852886e+38
			self_position_socket.subtype = 'NONE'
			self_position_socket.attribute_domain = 'POINT'
			
			
			#initialize self_sample_proximity nodes
			#node Group Output
			group_output_2 = self_sample_proximity.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Group Input
			group_input_2 = self_sample_proximity.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
			#node Set Position.002
			set_position_002 = self_sample_proximity.nodes.new("GeometryNodeSetPosition")
			set_position_002.name = "Set Position.002"
			#Selection
			set_position_002.inputs[1].default_value = True
			#Offset
			set_position_002.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Sample Nearest.001
			sample_nearest_001 = self_sample_proximity.nodes.new("GeometryNodeSampleNearest")
			sample_nearest_001.name = "Sample Nearest.001"
			sample_nearest_001.domain = 'POINT'
			
			
			
			
			#Set locations
			group_output_2.location = (4.068901062011719, 95.01506042480469)
			group_input_2.location = (-640.0, 20.0)
			set_position_002.location = (-380.0, -20.0)
			sample_nearest_001.location = (-220.0, -20.0)
			
			#Set dimensions
			group_output_2.width, group_output_2.height = 140.0, 100.0
			group_input_2.width, group_input_2.height = 140.0, 100.0
			set_position_002.width, set_position_002.height = 140.0, 100.0
			sample_nearest_001.width, sample_nearest_001.height = 140.0, 100.0
			
			#initialize self_sample_proximity links
			#group_input_2.Input -> set_position_002.Geometry
			self_sample_proximity.links.new(group_input_2.outputs[0], set_position_002.inputs[0])
			#set_position_002.Geometry -> sample_nearest_001.Geometry
			self_sample_proximity.links.new(set_position_002.outputs[0], sample_nearest_001.inputs[0])
			#group_input_2.Target Position -> set_position_002.Position
			self_sample_proximity.links.new(group_input_2.outputs[1], set_position_002.inputs[2])
			#group_input_2.Self Position -> sample_nearest_001.Sample Position
			self_sample_proximity.links.new(group_input_2.outputs[2], sample_nearest_001.inputs[1])
			#sample_nearest_001.Index -> group_output_2.Closest Index
			self_sample_proximity.links.new(sample_nearest_001.outputs[0], group_output_2.inputs[0])
			return self_sample_proximity

		self_sample_proximity = self_sample_proximity_node_group()

		#initialize offset_vector node group
		def offset_vector_node_group():
			offset_vector = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Offset Vector")

			offset_vector.color_tag = 'CONVERTER'
			offset_vector.description = ""

			
			#offset_vector interface
			#Socket Value
			value_socket = offset_vector.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			value_socket.default_value = (0.0, 0.0, 0.0)
			value_socket.min_value = -3.4028234663852886e+38
			value_socket.max_value = 3.4028234663852886e+38
			value_socket.subtype = 'NONE'
			value_socket.attribute_domain = 'POINT'
			
			#Socket Index
			index_socket = offset_vector.interface.new_socket(name = "Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			index_socket.default_value = 0
			index_socket.min_value = 0
			index_socket.max_value = 2147483647
			index_socket.subtype = 'NONE'
			index_socket.attribute_domain = 'POINT'
			
			#Socket Position
			position_socket = offset_vector.interface.new_socket(name = "Position", in_out='INPUT', socket_type = 'NodeSocketVector')
			position_socket.default_value = (0.0, 0.0, 0.0)
			position_socket.min_value = -3.4028234663852886e+38
			position_socket.max_value = 3.4028234663852886e+38
			position_socket.subtype = 'NONE'
			position_socket.attribute_domain = 'POINT'
			position_socket.hide_value = True
			
			#Socket Offset
			offset_socket = offset_vector.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket.default_value = 0
			offset_socket.min_value = -2147483647
			offset_socket.max_value = 2147483647
			offset_socket.subtype = 'NONE'
			offset_socket.attribute_domain = 'POINT'
			
			
			#initialize offset_vector nodes
			#node Group Output
			group_output_3 = offset_vector.nodes.new("NodeGroupOutput")
			group_output_3.name = "Group Output"
			group_output_3.is_active_output = True
			
			#node Group Input
			group_input_3 = offset_vector.nodes.new("NodeGroupInput")
			group_input_3.name = "Group Input"
			
			#node Evaluate at Index
			evaluate_at_index = offset_vector.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index.name = "Evaluate at Index"
			evaluate_at_index.data_type = 'FLOAT_VECTOR'
			evaluate_at_index.domain = 'POINT'
			
			#node Math
			math_1 = offset_vector.nodes.new("ShaderNodeMath")
			math_1.name = "Math"
			math_1.operation = 'ADD'
			math_1.use_clamp = False
			
			
			
			
			#Set locations
			group_output_3.location = (300.0, 20.0)
			group_input_3.location = (-273.81378173828125, 0.0)
			evaluate_at_index.location = (120.0, 20.0)
			math_1.location = (-60.0, 20.0)
			
			#Set dimensions
			group_output_3.width, group_output_3.height = 140.0, 100.0
			group_input_3.width, group_input_3.height = 140.0, 100.0
			evaluate_at_index.width, evaluate_at_index.height = 140.0, 100.0
			math_1.width, math_1.height = 140.0, 100.0
			
			#initialize offset_vector links
			#group_input_3.Position -> evaluate_at_index.Value
			offset_vector.links.new(group_input_3.outputs[1], evaluate_at_index.inputs[1])
			#evaluate_at_index.Value -> group_output_3.Value
			offset_vector.links.new(evaluate_at_index.outputs[0], group_output_3.inputs[0])
			#group_input_3.Index -> math_1.Value
			offset_vector.links.new(group_input_3.outputs[0], math_1.inputs[0])
			#group_input_3.Offset -> math_1.Value
			offset_vector.links.new(group_input_3.outputs[2], math_1.inputs[1])
			#math_1.Value -> evaluate_at_index.Index
			offset_vector.links.new(math_1.outputs[0], evaluate_at_index.inputs[0])
			return offset_vector

		offset_vector = offset_vector_node_group()

		#initialize _mn_world_scale node group
		def _mn_world_scale_node_group():
			_mn_world_scale = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_world_scale")

			_mn_world_scale.color_tag = 'NONE'
			_mn_world_scale.description = ""

			
			#_mn_world_scale interface
			#Socket world_scale
			world_scale_socket = _mn_world_scale.interface.new_socket(name = "world_scale", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			world_scale_socket.default_value = 0.009999999776482582
			world_scale_socket.min_value = -3.4028234663852886e+38
			world_scale_socket.max_value = 3.4028234663852886e+38
			world_scale_socket.subtype = 'NONE'
			world_scale_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_world_scale nodes
			#node Group Input
			group_input_4 = _mn_world_scale.nodes.new("NodeGroupInput")
			group_input_4.name = "Group Input"
			
			#node Value
			value = _mn_world_scale.nodes.new("ShaderNodeValue")
			value.label = "world_scale"
			value.name = "Value"
			
			value.outputs[0].default_value = 0.009999999776482582
			#node Group Output
			group_output_4 = _mn_world_scale.nodes.new("NodeGroupOutput")
			group_output_4.name = "Group Output"
			group_output_4.is_active_output = True
			
			
			
			
			#Set locations
			group_input_4.location = (-200.0, 0.0)
			value.location = (0.0, 0.0)
			group_output_4.location = (190.0, 0.0)
			
			#Set dimensions
			group_input_4.width, group_input_4.height = 140.0, 100.0
			value.width, value.height = 140.0, 100.0
			group_output_4.width, group_output_4.height = 140.0, 100.0
			
			#initialize _mn_world_scale links
			#value.Value -> group_output_4.world_scale
			_mn_world_scale.links.new(value.outputs[0], group_output_4.inputs[0])
			return _mn_world_scale

		_mn_world_scale = _mn_world_scale_node_group()

		#initialize mn_units node group
		def mn_units_node_group():
			mn_units = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "MN Units")

			mn_units.color_tag = 'NONE'
			mn_units.description = ""

			
			#mn_units interface
			#Socket Angstrom
			angstrom_socket = mn_units.interface.new_socket(name = "Angstrom", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			angstrom_socket.default_value = 0.0
			angstrom_socket.min_value = -3.4028234663852886e+38
			angstrom_socket.max_value = 3.4028234663852886e+38
			angstrom_socket.subtype = 'NONE'
			angstrom_socket.attribute_domain = 'POINT'
			
			#Socket Nanometre
			nanometre_socket = mn_units.interface.new_socket(name = "Nanometre", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			nanometre_socket.default_value = 0.0
			nanometre_socket.min_value = -3.4028234663852886e+38
			nanometre_socket.max_value = 3.4028234663852886e+38
			nanometre_socket.subtype = 'NONE'
			nanometre_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_1 = mn_units.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket_1.default_value = 3.0
			value_socket_1.min_value = -10000.0
			value_socket_1.max_value = 10000.0
			value_socket_1.subtype = 'NONE'
			value_socket_1.attribute_domain = 'POINT'
			value_socket_1.description = "A value which will be scaled appropriately for the world"
			
			
			#initialize mn_units nodes
			#node Group Output
			group_output_5 = mn_units.nodes.new("NodeGroupOutput")
			group_output_5.name = "Group Output"
			group_output_5.is_active_output = True
			
			#node Group Input
			group_input_5 = mn_units.nodes.new("NodeGroupInput")
			group_input_5.name = "Group Input"
			
			#node Math
			math_2 = mn_units.nodes.new("ShaderNodeMath")
			math_2.name = "Math"
			math_2.operation = 'MULTIPLY'
			math_2.use_clamp = False
			
			#node Math.001
			math_001 = mn_units.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.operation = 'MULTIPLY'
			math_001.use_clamp = False
			#Value_001
			math_001.inputs[1].default_value = 10.0
			
			#node Group
			group = mn_units.nodes.new("GeometryNodeGroup")
			group.name = "Group"
			group.node_tree = _mn_world_scale
			
			
			
			
			#Set locations
			group_output_5.location = (190.0, 0.0)
			group_input_5.location = (-240.0, 0.0)
			math_2.location = (-60.0, 0.0)
			math_001.location = (-60.0, -160.0)
			group.location = (-304.00421142578125, -104.114013671875)
			
			#Set dimensions
			group_output_5.width, group_output_5.height = 140.0, 100.0
			group_input_5.width, group_input_5.height = 140.0, 100.0
			math_2.width, math_2.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			group.width, group.height = 197.58424377441406, 100.0
			
			#initialize mn_units links
			#math_2.Value -> group_output_5.Angstrom
			mn_units.links.new(math_2.outputs[0], group_output_5.inputs[0])
			#group_input_5.Value -> math_2.Value
			mn_units.links.new(group_input_5.outputs[0], math_2.inputs[0])
			#group.world_scale -> math_2.Value
			mn_units.links.new(group.outputs[0], math_2.inputs[1])
			#math_2.Value -> math_001.Value
			mn_units.links.new(math_2.outputs[0], math_001.inputs[0])
			#math_001.Value -> group_output_5.Nanometre
			mn_units.links.new(math_001.outputs[0], group_output_5.inputs[1])
			return mn_units

		mn_units = mn_units_node_group()

		#initialize backbone_nh node group
		def backbone_nh_node_group():
			backbone_nh = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Backbone NH")

			backbone_nh.color_tag = 'NONE'
			backbone_nh.description = ""

			
			#backbone_nh interface
			#Socket H
			h_socket = backbone_nh.interface.new_socket(name = "H", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			h_socket.default_value = (0.0, 0.0, 0.0)
			h_socket.min_value = -3.4028234663852886e+38
			h_socket.max_value = 3.4028234663852886e+38
			h_socket.subtype = 'NONE'
			h_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_2 = backbone_nh.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket_2.default_value = 1.0
			value_socket_2.min_value = -10000.0
			value_socket_2.max_value = 10000.0
			value_socket_2.subtype = 'NONE'
			value_socket_2.attribute_domain = 'POINT'
			
			
			#initialize backbone_nh nodes
			#node Group Output
			group_output_6 = backbone_nh.nodes.new("NodeGroupOutput")
			group_output_6.name = "Group Output"
			group_output_6.is_active_output = True
			
			#node Group Input
			group_input_6 = backbone_nh.nodes.new("NodeGroupInput")
			group_input_6.name = "Group Input"
			
			#node Named Attribute
			named_attribute = backbone_nh.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute.inputs[0].default_value = "backbone_N"
			
			#node Named Attribute.001
			named_attribute_001 = backbone_nh.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_001.inputs[0].default_value = "backbone_CA"
			
			#node Named Attribute.002
			named_attribute_002 = backbone_nh.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002.name = "Named Attribute.002"
			named_attribute_002.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_002.inputs[0].default_value = "backbone_C"
			
			#node Group.002
			group_002 = backbone_nh.nodes.new("GeometryNodeGroup")
			group_002.name = "Group.002"
			group_002.node_tree = offset_vector
			#Socket_2
			group_002.inputs[0].default_value = 0
			#Socket_3
			group_002.inputs[2].default_value = -1
			
			#node Vector Math
			vector_math = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.operation = 'SUBTRACT'
			
			#node Vector Math.001
			vector_math_001 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_001.name = "Vector Math.001"
			vector_math_001.operation = 'SUBTRACT'
			
			#node Vector Math.002
			vector_math_002 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_002.name = "Vector Math.002"
			vector_math_002.operation = 'NORMALIZE'
			
			#node Vector Math.003
			vector_math_003 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_003.name = "Vector Math.003"
			vector_math_003.operation = 'NORMALIZE'
			
			#node Vector Math.005
			vector_math_005 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_005.name = "Vector Math.005"
			vector_math_005.operation = 'ADD'
			
			#node Vector Math.006
			vector_math_006 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_006.name = "Vector Math.006"
			vector_math_006.operation = 'ADD'
			
			#node Vector Math.004
			vector_math_004 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_004.name = "Vector Math.004"
			vector_math_004.operation = 'SCALE'
			
			#node Group.003
			group_003 = backbone_nh.nodes.new("GeometryNodeGroup")
			group_003.name = "Group.003"
			group_003.node_tree = mn_units
			
			#node Vector Math.007
			vector_math_007 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_007.name = "Vector Math.007"
			vector_math_007.operation = 'NORMALIZE'
			
			
			
			
			#Set locations
			group_output_6.location = (620.0, 0.0)
			group_input_6.location = (-630.0, 0.0)
			named_attribute.location = (-430.0, 140.0)
			named_attribute_001.location = (-430.0, 0.0)
			named_attribute_002.location = (-430.0, -140.0)
			group_002.location = (-210.0, -120.0)
			vector_math.location = (-50.0, 0.0)
			vector_math_001.location = (-50.0, 140.0)
			vector_math_002.location = (110.0, 140.0)
			vector_math_003.location = (110.0, 0.0)
			vector_math_005.location = (270.0, 140.0)
			vector_math_006.location = (430.0, 140.0)
			vector_math_004.location = (260.0, -120.0)
			group_003.location = (100.0, -120.0)
			vector_math_007.location = (260.0, 0.0)
			
			#Set dimensions
			group_output_6.width, group_output_6.height = 140.0, 100.0
			group_input_6.width, group_input_6.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 189.579833984375, 100.0
			named_attribute_001.width, named_attribute_001.height = 189.579833984375, 100.0
			named_attribute_002.width, named_attribute_002.height = 189.579833984375, 100.0
			group_002.width, group_002.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			vector_math_001.width, vector_math_001.height = 140.0, 100.0
			vector_math_002.width, vector_math_002.height = 140.0, 100.0
			vector_math_003.width, vector_math_003.height = 140.0, 100.0
			vector_math_005.width, vector_math_005.height = 140.0, 100.0
			vector_math_006.width, vector_math_006.height = 140.0, 100.0
			vector_math_004.width, vector_math_004.height = 140.0, 100.0
			group_003.width, group_003.height = 140.0, 100.0
			vector_math_007.width, vector_math_007.height = 140.0, 100.0
			
			#initialize backbone_nh links
			#vector_math_004.Vector -> vector_math_006.Vector
			backbone_nh.links.new(vector_math_004.outputs[0], vector_math_006.inputs[1])
			#named_attribute_001.Attribute -> vector_math_001.Vector
			backbone_nh.links.new(named_attribute_001.outputs[0], vector_math_001.inputs[1])
			#named_attribute_002.Attribute -> group_002.Position
			backbone_nh.links.new(named_attribute_002.outputs[0], group_002.inputs[1])
			#named_attribute.Attribute -> vector_math.Vector
			backbone_nh.links.new(named_attribute.outputs[0], vector_math.inputs[0])
			#vector_math.Vector -> vector_math_003.Vector
			backbone_nh.links.new(vector_math.outputs[0], vector_math_003.inputs[0])
			#group_003.Angstrom -> vector_math_004.Scale
			backbone_nh.links.new(group_003.outputs[0], vector_math_004.inputs[3])
			#vector_math_003.Vector -> vector_math_005.Vector
			backbone_nh.links.new(vector_math_003.outputs[0], vector_math_005.inputs[1])
			#group_002.Value -> vector_math.Vector
			backbone_nh.links.new(group_002.outputs[0], vector_math.inputs[1])
			#vector_math_002.Vector -> vector_math_005.Vector
			backbone_nh.links.new(vector_math_002.outputs[0], vector_math_005.inputs[0])
			#named_attribute.Attribute -> vector_math_001.Vector
			backbone_nh.links.new(named_attribute.outputs[0], vector_math_001.inputs[0])
			#vector_math_001.Vector -> vector_math_002.Vector
			backbone_nh.links.new(vector_math_001.outputs[0], vector_math_002.inputs[0])
			#named_attribute.Attribute -> vector_math_006.Vector
			backbone_nh.links.new(named_attribute.outputs[0], vector_math_006.inputs[0])
			#vector_math_006.Vector -> group_output_6.H
			backbone_nh.links.new(vector_math_006.outputs[0], group_output_6.inputs[0])
			#group_input_6.Value -> group_003.Value
			backbone_nh.links.new(group_input_6.outputs[0], group_003.inputs[0])
			#vector_math_005.Vector -> vector_math_007.Vector
			backbone_nh.links.new(vector_math_005.outputs[0], vector_math_007.inputs[0])
			#vector_math_007.Vector -> vector_math_004.Vector
			backbone_nh.links.new(vector_math_007.outputs[0], vector_math_004.inputs[0])
			return backbone_nh

		backbone_nh = backbone_nh_node_group()

		#initialize mn_topo_backbone node group
		def mn_topo_backbone_node_group():
			mn_topo_backbone = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "MN_topo_backbone")

			mn_topo_backbone.color_tag = 'NONE'
			mn_topo_backbone.description = ""

			
			#mn_topo_backbone interface
			#Socket O
			o_socket = mn_topo_backbone.interface.new_socket(name = "O", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			o_socket.default_value = (0.0, 0.0, 0.0)
			o_socket.min_value = -3.4028234663852886e+38
			o_socket.max_value = 3.4028234663852886e+38
			o_socket.subtype = 'NONE'
			o_socket.attribute_domain = 'POINT'
			
			#Socket C
			c_socket = mn_topo_backbone.interface.new_socket(name = "C", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			c_socket.default_value = (0.0, 0.0, 0.0)
			c_socket.min_value = -3.4028234663852886e+38
			c_socket.max_value = 3.4028234663852886e+38
			c_socket.subtype = 'NONE'
			c_socket.attribute_domain = 'POINT'
			
			#Socket CA
			ca_socket = mn_topo_backbone.interface.new_socket(name = "CA", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			ca_socket.default_value = (0.0, 0.0, 0.0)
			ca_socket.min_value = -3.4028234663852886e+38
			ca_socket.max_value = 3.4028234663852886e+38
			ca_socket.subtype = 'NONE'
			ca_socket.attribute_domain = 'POINT'
			
			#Socket N
			n_socket = mn_topo_backbone.interface.new_socket(name = "N", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			n_socket.default_value = (0.0, 0.0, 0.0)
			n_socket.min_value = -3.4028234663852886e+38
			n_socket.max_value = 3.4028234663852886e+38
			n_socket.subtype = 'NONE'
			n_socket.attribute_domain = 'POINT'
			
			#Socket NH
			nh_socket = mn_topo_backbone.interface.new_socket(name = "NH", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			nh_socket.default_value = (0.0, 0.0, 0.0)
			nh_socket.min_value = -3.4028234663852886e+38
			nh_socket.max_value = 3.4028234663852886e+38
			nh_socket.subtype = 'NONE'
			nh_socket.attribute_domain = 'POINT'
			
			#Socket Offset
			offset_socket_1 = mn_topo_backbone.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket_1.default_value = 0
			offset_socket_1.min_value = -2147483648
			offset_socket_1.max_value = 2147483647
			offset_socket_1.subtype = 'NONE'
			offset_socket_1.attribute_domain = 'POINT'
			
			
			#initialize mn_topo_backbone nodes
			#node Group Output
			group_output_7 = mn_topo_backbone.nodes.new("NodeGroupOutput")
			group_output_7.name = "Group Output"
			group_output_7.is_active_output = True
			
			#node Group Input
			group_input_7 = mn_topo_backbone.nodes.new("NodeGroupInput")
			group_input_7.name = "Group Input"
			
			#node Named Attribute.001
			named_attribute_001_1 = mn_topo_backbone.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001_1.name = "Named Attribute.001"
			named_attribute_001_1.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_001_1.inputs[0].default_value = "backbone_O"
			
			#node Named Attribute.002
			named_attribute_002_1 = mn_topo_backbone.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002_1.name = "Named Attribute.002"
			named_attribute_002_1.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_002_1.inputs[0].default_value = "backbone_C"
			
			#node Evaluate at Index
			evaluate_at_index_1 = mn_topo_backbone.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_1.name = "Evaluate at Index"
			evaluate_at_index_1.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_1.domain = 'POINT'
			
			#node Math
			math_3 = mn_topo_backbone.nodes.new("ShaderNodeMath")
			math_3.name = "Math"
			math_3.operation = 'ADD'
			math_3.use_clamp = False
			
			#node Index
			index = mn_topo_backbone.nodes.new("GeometryNodeInputIndex")
			index.name = "Index"
			
			#node Evaluate at Index.001
			evaluate_at_index_001 = mn_topo_backbone.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001.name = "Evaluate at Index.001"
			evaluate_at_index_001.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_001.domain = 'POINT'
			
			#node Named Attribute.003
			named_attribute_003 = mn_topo_backbone.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_003.name = "Named Attribute.003"
			named_attribute_003.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_003.inputs[0].default_value = "backbone_CA"
			
			#node Evaluate at Index.002
			evaluate_at_index_002 = mn_topo_backbone.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_002.name = "Evaluate at Index.002"
			evaluate_at_index_002.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_002.domain = 'POINT'
			
			#node Evaluate at Index.003
			evaluate_at_index_003 = mn_topo_backbone.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_003.name = "Evaluate at Index.003"
			evaluate_at_index_003.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_003.domain = 'POINT'
			
			#node Named Attribute.004
			named_attribute_004 = mn_topo_backbone.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_004.name = "Named Attribute.004"
			named_attribute_004.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_004.inputs[0].default_value = "backbone_N"
			
			#node Reroute
			reroute_2 = mn_topo_backbone.nodes.new("NodeReroute")
			reroute_2.name = "Reroute"
			#node Group
			group_1 = mn_topo_backbone.nodes.new("GeometryNodeGroup")
			group_1.name = "Group"
			group_1.node_tree = backbone_nh
			#Socket_1
			group_1.inputs[0].default_value = 1.0099999904632568
			
			#node Evaluate at Index.004
			evaluate_at_index_004 = mn_topo_backbone.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_004.name = "Evaluate at Index.004"
			evaluate_at_index_004.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_004.domain = 'POINT'
			
			#node Named Attribute.005
			named_attribute_005 = mn_topo_backbone.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_005.name = "Named Attribute.005"
			named_attribute_005.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_005.inputs[0].default_value = "backbone_NH"
			
			#node Switch
			switch = mn_topo_backbone.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'VECTOR'
			
			#node Boolean Math
			boolean_math_1 = mn_topo_backbone.nodes.new("FunctionNodeBooleanMath")
			boolean_math_1.name = "Boolean Math"
			boolean_math_1.operation = 'NOT'
			
			
			
			
			#Set locations
			group_output_7.location = (320.0, -220.0)
			group_input_7.location = (-520.0, -260.0)
			named_attribute_001_1.location = (-300.0, 40.0)
			named_attribute_002_1.location = (-300.0, -100.0)
			evaluate_at_index_1.location = (80.0, -14.04681396484375)
			math_3.location = (-260.0, -260.0)
			index.location = (-520.0, -360.0)
			evaluate_at_index_001.location = (80.0, -170.47593688964844)
			named_attribute_003.location = (-300.0, -460.0)
			evaluate_at_index_002.location = (80.0, -326.90509033203125)
			evaluate_at_index_003.location = (80.0, -480.0)
			named_attribute_004.location = (-300.0, -600.0)
			reroute_2.location = (20.0, -340.0)
			group_1.location = (-640.0, -920.0)
			evaluate_at_index_004.location = (77.81956481933594, -655.5125732421875)
			named_attribute_005.location = (-640.0, -780.0)
			switch.location = (-240.0, -780.0)
			boolean_math_1.location = (-420.0, -780.0)
			
			#Set dimensions
			group_output_7.width, group_output_7.height = 140.0, 100.0
			group_input_7.width, group_input_7.height = 140.0, 100.0
			named_attribute_001_1.width, named_attribute_001_1.height = 186.42977905273438, 100.0
			named_attribute_002_1.width, named_attribute_002_1.height = 186.42977905273438, 100.0
			evaluate_at_index_1.width, evaluate_at_index_1.height = 140.0, 100.0
			math_3.width, math_3.height = 140.0, 100.0
			index.width, index.height = 140.0, 100.0
			evaluate_at_index_001.width, evaluate_at_index_001.height = 140.0, 100.0
			named_attribute_003.width, named_attribute_003.height = 186.42977905273438, 100.0
			evaluate_at_index_002.width, evaluate_at_index_002.height = 140.0, 100.0
			evaluate_at_index_003.width, evaluate_at_index_003.height = 140.0, 100.0
			named_attribute_004.width, named_attribute_004.height = 186.42977905273438, 100.0
			reroute_2.width, reroute_2.height = 16.0, 100.0
			group_1.width, group_1.height = 186.0294189453125, 100.0
			evaluate_at_index_004.width, evaluate_at_index_004.height = 140.0, 100.0
			named_attribute_005.width, named_attribute_005.height = 186.42977905273438, 100.0
			switch.width, switch.height = 140.0, 100.0
			boolean_math_1.width, boolean_math_1.height = 140.0, 100.0
			
			#initialize mn_topo_backbone links
			#named_attribute_001_1.Attribute -> evaluate_at_index_1.Value
			mn_topo_backbone.links.new(named_attribute_001_1.outputs[0], evaluate_at_index_1.inputs[1])
			#reroute_2.Output -> evaluate_at_index_1.Index
			mn_topo_backbone.links.new(reroute_2.outputs[0], evaluate_at_index_1.inputs[0])
			#group_input_7.Offset -> math_3.Value
			mn_topo_backbone.links.new(group_input_7.outputs[0], math_3.inputs[0])
			#reroute_2.Output -> evaluate_at_index_001.Index
			mn_topo_backbone.links.new(reroute_2.outputs[0], evaluate_at_index_001.inputs[0])
			#named_attribute_002_1.Attribute -> evaluate_at_index_001.Value
			mn_topo_backbone.links.new(named_attribute_002_1.outputs[0], evaluate_at_index_001.inputs[1])
			#reroute_2.Output -> evaluate_at_index_002.Index
			mn_topo_backbone.links.new(reroute_2.outputs[0], evaluate_at_index_002.inputs[0])
			#named_attribute_003.Attribute -> evaluate_at_index_002.Value
			mn_topo_backbone.links.new(named_attribute_003.outputs[0], evaluate_at_index_002.inputs[1])
			#reroute_2.Output -> evaluate_at_index_003.Index
			mn_topo_backbone.links.new(reroute_2.outputs[0], evaluate_at_index_003.inputs[0])
			#named_attribute_004.Attribute -> evaluate_at_index_003.Value
			mn_topo_backbone.links.new(named_attribute_004.outputs[0], evaluate_at_index_003.inputs[1])
			#index.Index -> math_3.Value
			mn_topo_backbone.links.new(index.outputs[0], math_3.inputs[1])
			#math_3.Value -> reroute_2.Input
			mn_topo_backbone.links.new(math_3.outputs[0], reroute_2.inputs[0])
			#evaluate_at_index_003.Value -> group_output_7.N
			mn_topo_backbone.links.new(evaluate_at_index_003.outputs[0], group_output_7.inputs[3])
			#evaluate_at_index_002.Value -> group_output_7.CA
			mn_topo_backbone.links.new(evaluate_at_index_002.outputs[0], group_output_7.inputs[2])
			#evaluate_at_index_001.Value -> group_output_7.C
			mn_topo_backbone.links.new(evaluate_at_index_001.outputs[0], group_output_7.inputs[1])
			#evaluate_at_index_1.Value -> group_output_7.O
			mn_topo_backbone.links.new(evaluate_at_index_1.outputs[0], group_output_7.inputs[0])
			#reroute_2.Output -> evaluate_at_index_004.Index
			mn_topo_backbone.links.new(reroute_2.outputs[0], evaluate_at_index_004.inputs[0])
			#evaluate_at_index_004.Value -> group_output_7.NH
			mn_topo_backbone.links.new(evaluate_at_index_004.outputs[0], group_output_7.inputs[4])
			#group_1.H -> switch.True
			mn_topo_backbone.links.new(group_1.outputs[0], switch.inputs[2])
			#switch.Output -> evaluate_at_index_004.Value
			mn_topo_backbone.links.new(switch.outputs[0], evaluate_at_index_004.inputs[1])
			#named_attribute_005.Exists -> boolean_math_1.Boolean
			mn_topo_backbone.links.new(named_attribute_005.outputs[1], boolean_math_1.inputs[0])
			#boolean_math_1.Boolean -> switch.Switch
			mn_topo_backbone.links.new(boolean_math_1.outputs[0], switch.inputs[0])
			#named_attribute_005.Attribute -> switch.False
			mn_topo_backbone.links.new(named_attribute_005.outputs[0], switch.inputs[1])
			return mn_topo_backbone

		mn_topo_backbone = mn_topo_backbone_node_group()

		#initialize world_to_angstrom node group
		def world_to_angstrom_node_group():
			world_to_angstrom = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "World to Angstrom")

			world_to_angstrom.color_tag = 'NONE'
			world_to_angstrom.description = ""

			
			#world_to_angstrom interface
			#Socket Angstrom
			angstrom_socket_1 = world_to_angstrom.interface.new_socket(name = "Angstrom", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			angstrom_socket_1.default_value = 0.0
			angstrom_socket_1.min_value = -3.4028234663852886e+38
			angstrom_socket_1.max_value = 3.4028234663852886e+38
			angstrom_socket_1.subtype = 'NONE'
			angstrom_socket_1.attribute_domain = 'POINT'
			
			#Socket World
			world_socket = world_to_angstrom.interface.new_socket(name = "World", in_out='INPUT', socket_type = 'NodeSocketFloat')
			world_socket.default_value = 0.5
			world_socket.min_value = -10000.0
			world_socket.max_value = 10000.0
			world_socket.subtype = 'NONE'
			world_socket.attribute_domain = 'POINT'
			
			
			#initialize world_to_angstrom nodes
			#node Group Output
			group_output_8 = world_to_angstrom.nodes.new("NodeGroupOutput")
			group_output_8.name = "Group Output"
			group_output_8.is_active_output = True
			
			#node Group Input
			group_input_8 = world_to_angstrom.nodes.new("NodeGroupInput")
			group_input_8.name = "Group Input"
			
			#node Group
			group_2 = world_to_angstrom.nodes.new("GeometryNodeGroup")
			group_2.name = "Group"
			group_2.node_tree = _mn_world_scale
			
			#node Math
			math_4 = world_to_angstrom.nodes.new("ShaderNodeMath")
			math_4.name = "Math"
			math_4.operation = 'DIVIDE'
			math_4.use_clamp = False
			
			
			
			
			#Set locations
			group_output_8.location = (190.0, 0.0)
			group_input_8.location = (-200.0, 0.0)
			group_2.location = (0.0, -80.0)
			math_4.location = (0.0, 80.0)
			
			#Set dimensions
			group_output_8.width, group_output_8.height = 140.0, 100.0
			group_input_8.width, group_input_8.height = 140.0, 100.0
			group_2.width, group_2.height = 140.0, 100.0
			math_4.width, math_4.height = 140.0, 100.0
			
			#initialize world_to_angstrom links
			#group_2.world_scale -> math_4.Value
			world_to_angstrom.links.new(group_2.outputs[0], math_4.inputs[1])
			#group_input_8.World -> math_4.Value
			world_to_angstrom.links.new(group_input_8.outputs[0], math_4.inputs[0])
			#math_4.Value -> group_output_8.Angstrom
			world_to_angstrom.links.new(math_4.outputs[0], group_output_8.inputs[0])
			return world_to_angstrom

		world_to_angstrom = world_to_angstrom_node_group()

		#initialize nodegroup_001 node group
		def nodegroup_001_node_group():
			nodegroup_001 = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "NodeGroup.001")

			nodegroup_001.color_tag = 'NONE'
			nodegroup_001.description = ""

			
			#nodegroup_001 interface
			#Socket Value
			value_socket_3 = nodegroup_001.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			value_socket_3.default_value = 0.0
			value_socket_3.min_value = -3.4028234663852886e+38
			value_socket_3.max_value = 3.4028234663852886e+38
			value_socket_3.subtype = 'NONE'
			value_socket_3.attribute_domain = 'POINT'
			
			#Socket Vector
			vector_socket = nodegroup_001.interface.new_socket(name = "Vector", in_out='INPUT', socket_type = 'NodeSocketVector')
			vector_socket.default_value = (0.0, 0.0, 0.0)
			vector_socket.min_value = -10000.0
			vector_socket.max_value = 10000.0
			vector_socket.subtype = 'NONE'
			vector_socket.attribute_domain = 'POINT'
			
			#Socket Vector
			vector_socket_1 = nodegroup_001.interface.new_socket(name = "Vector", in_out='INPUT', socket_type = 'NodeSocketVector')
			vector_socket_1.default_value = (0.0, 0.0, 0.0)
			vector_socket_1.min_value = -10000.0
			vector_socket_1.max_value = 10000.0
			vector_socket_1.subtype = 'NONE'
			vector_socket_1.attribute_domain = 'POINT'
			
			
			#initialize nodegroup_001 nodes
			#node Group Output
			group_output_9 = nodegroup_001.nodes.new("NodeGroupOutput")
			group_output_9.name = "Group Output"
			group_output_9.is_active_output = True
			
			#node Group Input
			group_input_9 = nodegroup_001.nodes.new("NodeGroupInput")
			group_input_9.name = "Group Input"
			
			#node Vector Math.002
			vector_math_002_1 = nodegroup_001.nodes.new("ShaderNodeVectorMath")
			vector_math_002_1.name = "Vector Math.002"
			vector_math_002_1.operation = 'DISTANCE'
			
			#node Math.002
			math_002 = nodegroup_001.nodes.new("ShaderNodeMath")
			math_002.name = "Math.002"
			math_002.operation = 'DIVIDE'
			math_002.use_clamp = False
			#Value
			math_002.inputs[0].default_value = 1.0
			
			#node Group.001
			group_001 = nodegroup_001.nodes.new("GeometryNodeGroup")
			group_001.name = "Group.001"
			group_001.node_tree = world_to_angstrom
			
			
			
			
			#Set locations
			group_output_9.location = (670.8533325195312, -4.1087493896484375)
			group_input_9.location = (-280.0, 0.0)
			vector_math_002_1.location = (-80.0, 0.0)
			math_002.location = (260.0, 0.0)
			group_001.location = (80.0, 0.0)
			
			#Set dimensions
			group_output_9.width, group_output_9.height = 140.0, 100.0
			group_input_9.width, group_input_9.height = 140.0, 100.0
			vector_math_002_1.width, vector_math_002_1.height = 140.0, 100.0
			math_002.width, math_002.height = 140.0, 100.0
			group_001.width, group_001.height = 152.50686645507812, 100.0
			
			#initialize nodegroup_001 links
			#group_001.Angstrom -> math_002.Value
			nodegroup_001.links.new(group_001.outputs[0], math_002.inputs[1])
			#group_input_9.Vector -> vector_math_002_1.Vector
			nodegroup_001.links.new(group_input_9.outputs[1], vector_math_002_1.inputs[1])
			#group_input_9.Vector -> vector_math_002_1.Vector
			nodegroup_001.links.new(group_input_9.outputs[0], vector_math_002_1.inputs[0])
			#math_002.Value -> group_output_9.Value
			nodegroup_001.links.new(math_002.outputs[0], group_output_9.inputs[0])
			#vector_math_002_1.Value -> group_001.World
			nodegroup_001.links.new(vector_math_002_1.outputs[1], group_001.inputs[0])
			return nodegroup_001

		nodegroup_001 = nodegroup_001_node_group()

		#initialize hbond_energy node group
		def hbond_energy_node_group():
			hbond_energy = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "HBond Energy")

			hbond_energy.color_tag = 'NONE'
			hbond_energy.description = ""

			
			#hbond_energy interface
			#Socket Is Bonded
			is_bonded_socket = hbond_energy.interface.new_socket(name = "Is Bonded", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_bonded_socket.default_value = False
			is_bonded_socket.attribute_domain = 'POINT'
			
			#Socket Bond Energy
			bond_energy_socket = hbond_energy.interface.new_socket(name = "Bond Energy", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			bond_energy_socket.default_value = 0.0
			bond_energy_socket.min_value = -3.4028234663852886e+38
			bond_energy_socket.max_value = 3.4028234663852886e+38
			bond_energy_socket.subtype = 'NONE'
			bond_energy_socket.attribute_domain = 'POINT'
			
			#Socket Bond Vector
			bond_vector_socket = hbond_energy.interface.new_socket(name = "Bond Vector", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			bond_vector_socket.default_value = (0.0, 0.0, 0.0)
			bond_vector_socket.min_value = -3.4028234663852886e+38
			bond_vector_socket.max_value = 3.4028234663852886e+38
			bond_vector_socket.subtype = 'NONE'
			bond_vector_socket.attribute_domain = 'POINT'
			
			#Socket O
			o_socket_1 = hbond_energy.interface.new_socket(name = "O", in_out='INPUT', socket_type = 'NodeSocketVector')
			o_socket_1.default_value = (0.0, 0.0, 0.0)
			o_socket_1.min_value = -3.4028234663852886e+38
			o_socket_1.max_value = 3.4028234663852886e+38
			o_socket_1.subtype = 'NONE'
			o_socket_1.attribute_domain = 'POINT'
			
			#Socket C
			c_socket_1 = hbond_energy.interface.new_socket(name = "C", in_out='INPUT', socket_type = 'NodeSocketVector')
			c_socket_1.default_value = (0.0, 0.0, 0.0)
			c_socket_1.min_value = -3.4028234663852886e+38
			c_socket_1.max_value = 3.4028234663852886e+38
			c_socket_1.subtype = 'NONE'
			c_socket_1.attribute_domain = 'POINT'
			
			#Socket N
			n_socket_1 = hbond_energy.interface.new_socket(name = "N", in_out='INPUT', socket_type = 'NodeSocketVector')
			n_socket_1.default_value = (0.0, 0.0, 0.0)
			n_socket_1.min_value = -3.4028234663852886e+38
			n_socket_1.max_value = 3.4028234663852886e+38
			n_socket_1.subtype = 'NONE'
			n_socket_1.attribute_domain = 'POINT'
			
			#Socket H
			h_socket_1 = hbond_energy.interface.new_socket(name = "H", in_out='INPUT', socket_type = 'NodeSocketVector')
			h_socket_1.default_value = (0.0, 0.0, 0.0)
			h_socket_1.min_value = -3.4028234663852886e+38
			h_socket_1.max_value = 3.4028234663852886e+38
			h_socket_1.subtype = 'NONE'
			h_socket_1.attribute_domain = 'POINT'
			
			
			#initialize hbond_energy nodes
			#node Group Output
			group_output_10 = hbond_energy.nodes.new("NodeGroupOutput")
			group_output_10.name = "Group Output"
			group_output_10.is_active_output = True
			
			#node Group Input
			group_input_10 = hbond_energy.nodes.new("NodeGroupInput")
			group_input_10.name = "Group Input"
			
			#node Group.003
			group_003_1 = hbond_energy.nodes.new("GeometryNodeGroup")
			group_003_1.label = "1/r(ON)"
			group_003_1.name = "Group.003"
			group_003_1.node_tree = nodegroup_001
			
			#node Group.008
			group_008 = hbond_energy.nodes.new("GeometryNodeGroup")
			group_008.label = "1/r(CH)"
			group_008.name = "Group.008"
			group_008.node_tree = nodegroup_001
			
			#node Group.009
			group_009 = hbond_energy.nodes.new("GeometryNodeGroup")
			group_009.label = "1/r(OH)"
			group_009.name = "Group.009"
			group_009.node_tree = nodegroup_001
			
			#node Group.010
			group_010 = hbond_energy.nodes.new("GeometryNodeGroup")
			group_010.label = "1/r(CN)"
			group_010.name = "Group.010"
			group_010.node_tree = nodegroup_001
			
			#node Math.002
			math_002_1 = hbond_energy.nodes.new("ShaderNodeMath")
			math_002_1.name = "Math.002"
			math_002_1.hide = True
			math_002_1.operation = 'ADD'
			math_002_1.use_clamp = False
			
			#node Math.003
			math_003 = hbond_energy.nodes.new("ShaderNodeMath")
			math_003.name = "Math.003"
			math_003.hide = True
			math_003.operation = 'SUBTRACT'
			math_003.use_clamp = False
			
			#node Math.004
			math_004 = hbond_energy.nodes.new("ShaderNodeMath")
			math_004.name = "Math.004"
			math_004.hide = True
			math_004.operation = 'SUBTRACT'
			math_004.use_clamp = False
			
			#node Math.005
			math_005 = hbond_energy.nodes.new("ShaderNodeMath")
			math_005.label = "* q1q2"
			math_005.name = "Math.005"
			math_005.operation = 'MULTIPLY'
			math_005.use_clamp = False
			#Value_001
			math_005.inputs[1].default_value = 0.08399999886751175
			
			#node Math.006
			math_006 = hbond_energy.nodes.new("ShaderNodeMath")
			math_006.label = "*f"
			math_006.name = "Math.006"
			math_006.operation = 'MULTIPLY'
			math_006.use_clamp = False
			#Value_001
			math_006.inputs[1].default_value = 332.0
			
			#node Vector Math
			vector_math_1 = hbond_energy.nodes.new("ShaderNodeVectorMath")
			vector_math_1.name = "Vector Math"
			vector_math_1.operation = 'SUBTRACT'
			
			#node Math.007
			math_007 = hbond_energy.nodes.new("ShaderNodeMath")
			math_007.label = "*e"
			math_007.name = "Math.007"
			math_007.mute = True
			math_007.operation = 'MULTIPLY'
			math_007.use_clamp = False
			#Value_001
			math_007.inputs[1].default_value = -1.0
			
			#node Compare
			compare_2 = hbond_energy.nodes.new("FunctionNodeCompare")
			compare_2.label = "Cutoff kcal/mol"
			compare_2.name = "Compare"
			compare_2.data_type = 'FLOAT'
			compare_2.mode = 'ELEMENT'
			compare_2.operation = 'LESS_THAN'
			#B
			compare_2.inputs[1].default_value = -0.5
			
			#node Group Input.001
			group_input_001_1 = hbond_energy.nodes.new("NodeGroupInput")
			group_input_001_1.name = "Group Input.001"
			
			
			
			
			#Set locations
			group_output_10.location = (900.0, 40.0)
			group_input_10.location = (-644.257568359375, 10.571624755859375)
			group_003_1.location = (-355.197021484375, 210.6334228515625)
			group_008.location = (-360.0, 69.3665771484375)
			group_009.location = (-360.0, -70.6334228515625)
			group_010.location = (-360.0, -210.6334228515625)
			math_002_1.location = (-180.0, 60.0)
			math_003.location = (-180.0, -80.0)
			math_004.location = (-180.0, -220.0)
			math_005.location = (320.0, 100.0)
			math_006.location = (480.0, 100.0)
			vector_math_1.location = (480.0, -60.0)
			math_007.location = (160.0, 100.0)
			compare_2.location = (720.0, 220.0)
			group_input_001_1.location = (320.0, -60.0)
			
			#Set dimensions
			group_output_10.width, group_output_10.height = 140.0, 100.0
			group_input_10.width, group_input_10.height = 140.0, 100.0
			group_003_1.width, group_003_1.height = 140.0, 100.0
			group_008.width, group_008.height = 140.0, 100.0
			group_009.width, group_009.height = 140.0, 100.0
			group_010.width, group_010.height = 140.0, 100.0
			math_002_1.width, math_002_1.height = 140.0, 100.0
			math_003.width, math_003.height = 140.0, 100.0
			math_004.width, math_004.height = 140.0, 100.0
			math_005.width, math_005.height = 140.0, 100.0
			math_006.width, math_006.height = 140.0, 100.0
			vector_math_1.width, vector_math_1.height = 140.0, 100.0
			math_007.width, math_007.height = 140.0, 100.0
			compare_2.width, compare_2.height = 140.0, 100.0
			group_input_001_1.width, group_input_001_1.height = 140.0, 100.0
			
			#initialize hbond_energy links
			#math_002_1.Value -> math_003.Value
			hbond_energy.links.new(math_002_1.outputs[0], math_003.inputs[0])
			#group_009.Value -> math_003.Value
			hbond_energy.links.new(group_009.outputs[0], math_003.inputs[1])
			#math_007.Value -> math_005.Value
			hbond_energy.links.new(math_007.outputs[0], math_005.inputs[0])
			#group_008.Value -> math_002_1.Value
			hbond_energy.links.new(group_008.outputs[0], math_002_1.inputs[1])
			#math_003.Value -> math_004.Value
			hbond_energy.links.new(math_003.outputs[0], math_004.inputs[0])
			#group_010.Value -> math_004.Value
			hbond_energy.links.new(group_010.outputs[0], math_004.inputs[1])
			#group_003_1.Value -> math_002_1.Value
			hbond_energy.links.new(group_003_1.outputs[0], math_002_1.inputs[0])
			#math_005.Value -> math_006.Value
			hbond_energy.links.new(math_005.outputs[0], math_006.inputs[0])
			#math_006.Value -> group_output_10.Bond Energy
			hbond_energy.links.new(math_006.outputs[0], group_output_10.inputs[1])
			#math_004.Value -> math_007.Value
			hbond_energy.links.new(math_004.outputs[0], math_007.inputs[0])
			#vector_math_1.Vector -> group_output_10.Bond Vector
			hbond_energy.links.new(vector_math_1.outputs[0], group_output_10.inputs[2])
			#math_006.Value -> compare_2.A
			hbond_energy.links.new(math_006.outputs[0], compare_2.inputs[0])
			#compare_2.Result -> group_output_10.Is Bonded
			hbond_energy.links.new(compare_2.outputs[0], group_output_10.inputs[0])
			#group_input_10.O -> group_003_1.Vector
			hbond_energy.links.new(group_input_10.outputs[0], group_003_1.inputs[0])
			#group_input_10.N -> group_003_1.Vector
			hbond_energy.links.new(group_input_10.outputs[2], group_003_1.inputs[1])
			#group_input_10.C -> group_008.Vector
			hbond_energy.links.new(group_input_10.outputs[1], group_008.inputs[0])
			#group_input_10.H -> group_008.Vector
			hbond_energy.links.new(group_input_10.outputs[3], group_008.inputs[1])
			#group_input_10.O -> group_009.Vector
			hbond_energy.links.new(group_input_10.outputs[0], group_009.inputs[0])
			#group_input_10.H -> group_009.Vector
			hbond_energy.links.new(group_input_10.outputs[3], group_009.inputs[1])
			#group_input_10.C -> group_010.Vector
			hbond_energy.links.new(group_input_10.outputs[1], group_010.inputs[0])
			#group_input_10.N -> group_010.Vector
			hbond_energy.links.new(group_input_10.outputs[2], group_010.inputs[1])
			#group_input_001_1.H -> vector_math_1.Vector
			hbond_energy.links.new(group_input_001_1.outputs[3], vector_math_1.inputs[1])
			#group_input_001_1.O -> vector_math_1.Vector
			hbond_energy.links.new(group_input_001_1.outputs[0], vector_math_1.inputs[0])
			return hbond_energy

		hbond_energy = hbond_energy_node_group()

		#initialize hbond_backbone_check node group
		def hbond_backbone_check_node_group():
			hbond_backbone_check = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "HBond Backbone Check")

			hbond_backbone_check.color_tag = 'NONE'
			hbond_backbone_check.description = ""

			
			#hbond_backbone_check interface
			#Socket Is Bonded
			is_bonded_socket_1 = hbond_backbone_check.interface.new_socket(name = "Is Bonded", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_bonded_socket_1.default_value = False
			is_bonded_socket_1.attribute_domain = 'POINT'
			
			#Socket Bond Energy
			bond_energy_socket_1 = hbond_backbone_check.interface.new_socket(name = "Bond Energy", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			bond_energy_socket_1.default_value = 0.0
			bond_energy_socket_1.min_value = -3.4028234663852886e+38
			bond_energy_socket_1.max_value = 3.4028234663852886e+38
			bond_energy_socket_1.subtype = 'NONE'
			bond_energy_socket_1.attribute_domain = 'POINT'
			
			#Socket H->O
			h__o_socket = hbond_backbone_check.interface.new_socket(name = "H->O", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			h__o_socket.default_value = (0.0, 0.0, 0.0)
			h__o_socket.min_value = -3.4028234663852886e+38
			h__o_socket.max_value = 3.4028234663852886e+38
			h__o_socket.subtype = 'NONE'
			h__o_socket.attribute_domain = 'POINT'
			
			#Panel CO
			co_panel = hbond_backbone_check.interface.new_panel("CO")
			#Socket CO Index
			co_index_socket = hbond_backbone_check.interface.new_socket(name = "CO Index", in_out='INPUT', socket_type = 'NodeSocketInt', parent = co_panel)
			co_index_socket.default_value = 0
			co_index_socket.min_value = 0
			co_index_socket.max_value = 2147483647
			co_index_socket.subtype = 'NONE'
			co_index_socket.attribute_domain = 'POINT'
			
			#Socket CO Offset
			co_offset_socket = hbond_backbone_check.interface.new_socket(name = "CO Offset", in_out='INPUT', socket_type = 'NodeSocketInt', parent = co_panel)
			co_offset_socket.default_value = 0
			co_offset_socket.min_value = -2147483648
			co_offset_socket.max_value = 2147483647
			co_offset_socket.subtype = 'NONE'
			co_offset_socket.attribute_domain = 'POINT'
			
			
			#Panel NH
			nh_panel = hbond_backbone_check.interface.new_panel("NH")
			#Socket NH Index
			nh_index_socket = hbond_backbone_check.interface.new_socket(name = "NH Index", in_out='INPUT', socket_type = 'NodeSocketInt', parent = nh_panel)
			nh_index_socket.default_value = 0
			nh_index_socket.min_value = 0
			nh_index_socket.max_value = 2147483647
			nh_index_socket.subtype = 'NONE'
			nh_index_socket.attribute_domain = 'POINT'
			
			#Socket NH Offset
			nh_offset_socket = hbond_backbone_check.interface.new_socket(name = "NH Offset", in_out='INPUT', socket_type = 'NodeSocketInt', parent = nh_panel)
			nh_offset_socket.default_value = 0
			nh_offset_socket.min_value = -2147483648
			nh_offset_socket.max_value = 2147483647
			nh_offset_socket.subtype = 'NONE'
			nh_offset_socket.attribute_domain = 'POINT'
			
			
			
			#initialize hbond_backbone_check nodes
			#node Group Output
			group_output_11 = hbond_backbone_check.nodes.new("NodeGroupOutput")
			group_output_11.name = "Group Output"
			group_output_11.is_active_output = True
			
			#node Group Input
			group_input_11 = hbond_backbone_check.nodes.new("NodeGroupInput")
			group_input_11.name = "Group Input"
			
			#node Group.008
			group_008_1 = hbond_backbone_check.nodes.new("GeometryNodeGroup")
			group_008_1.name = "Group.008"
			group_008_1.node_tree = hbond_energy
			
			#node Group.009
			group_009_1 = hbond_backbone_check.nodes.new("GeometryNodeGroup")
			group_009_1.name = "Group.009"
			group_009_1.node_tree = mn_topo_backbone
			#Socket_3
			group_009_1.inputs[0].default_value = 0
			
			#node Evaluate at Index
			evaluate_at_index_2 = hbond_backbone_check.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_2.name = "Evaluate at Index"
			evaluate_at_index_2.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_2.domain = 'POINT'
			
			#node Evaluate at Index.001
			evaluate_at_index_001_1 = hbond_backbone_check.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001_1.name = "Evaluate at Index.001"
			evaluate_at_index_001_1.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_001_1.domain = 'POINT'
			
			#node Evaluate at Index.002
			evaluate_at_index_002_1 = hbond_backbone_check.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_002_1.name = "Evaluate at Index.002"
			evaluate_at_index_002_1.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_002_1.domain = 'POINT'
			
			#node Evaluate at Index.003
			evaluate_at_index_003_1 = hbond_backbone_check.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_003_1.name = "Evaluate at Index.003"
			evaluate_at_index_003_1.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_003_1.domain = 'POINT'
			
			#node Math
			math_5 = hbond_backbone_check.nodes.new("ShaderNodeMath")
			math_5.name = "Math"
			math_5.operation = 'ADD'
			math_5.use_clamp = False
			
			#node Math.001
			math_001_1 = hbond_backbone_check.nodes.new("ShaderNodeMath")
			math_001_1.name = "Math.001"
			math_001_1.operation = 'ADD'
			math_001_1.use_clamp = False
			
			#node Math.002
			math_002_2 = hbond_backbone_check.nodes.new("ShaderNodeMath")
			math_002_2.name = "Math.002"
			math_002_2.operation = 'SUBTRACT'
			math_002_2.use_clamp = False
			
			#node Math.003
			math_003_1 = hbond_backbone_check.nodes.new("ShaderNodeMath")
			math_003_1.name = "Math.003"
			math_003_1.operation = 'ABSOLUTE'
			math_003_1.use_clamp = False
			
			#node Compare
			compare_3 = hbond_backbone_check.nodes.new("FunctionNodeCompare")
			compare_3.name = "Compare"
			compare_3.data_type = 'FLOAT'
			compare_3.mode = 'ELEMENT'
			compare_3.operation = 'GREATER_THAN'
			
			#node Integer
			integer = hbond_backbone_check.nodes.new("FunctionNodeInputInt")
			integer.name = "Integer"
			integer.integer = 2
			
			#node Frame
			frame = hbond_backbone_check.nodes.new("NodeFrame")
			frame.label = "Check not bonded to +/- residues"
			frame.name = "Frame"
			frame.label_size = 20
			frame.shrink = True
			
			#node Switch
			switch_1 = hbond_backbone_check.nodes.new("GeometryNodeSwitch")
			switch_1.name = "Switch"
			switch_1.input_type = 'BOOLEAN'
			#False
			switch_1.inputs[1].default_value = False
			
			#node Compare.001
			compare_001_2 = hbond_backbone_check.nodes.new("FunctionNodeCompare")
			compare_001_2.name = "Compare.001"
			compare_001_2.data_type = 'FLOAT'
			compare_001_2.mode = 'ELEMENT'
			compare_001_2.operation = 'LESS_THAN'
			
			#node Vector Math
			vector_math_2 = hbond_backbone_check.nodes.new("ShaderNodeVectorMath")
			vector_math_2.name = "Vector Math"
			vector_math_2.operation = 'LENGTH'
			
			#node Group
			group_3 = hbond_backbone_check.nodes.new("GeometryNodeGroup")
			group_3.name = "Group"
			group_3.node_tree = mn_units
			#Input_1
			group_3.inputs[0].default_value = 3.0
			
			
			
			#Set parents
			math_002_2.parent = frame
			math_003_1.parent = frame
			compare_3.parent = frame
			integer.parent = frame
			
			#Set locations
			group_output_11.location = (820.0, 240.0)
			group_input_11.location = (-680.0, 140.0)
			group_008_1.location = (224.2731170654297, 240.0)
			group_009_1.location = (-480.0, 460.0)
			evaluate_at_index_2.location = (-20.0, 40.0)
			evaluate_at_index_001_1.location = (-20.0, -120.0)
			evaluate_at_index_002_1.location = (-20.0, 400.0)
			evaluate_at_index_003_1.location = (-20.0, 240.0)
			math_5.location = (-480.0, 240.0)
			math_001_1.location = (-480.0, 80.0)
			math_002_2.location = (70.0, 640.0)
			math_003_1.location = (240.0, 640.0)
			compare_3.location = (420.0, 640.0)
			integer.location = (240.0, 500.0)
			frame.location = (-70.0, 40.0)
			switch_1.location = (620.0, 340.0)
			compare_001_2.location = (520.0, 140.0)
			vector_math_2.location = (260.0, 20.0)
			group_3.location = (520.0, -20.0)
			
			#Set dimensions
			group_output_11.width, group_output_11.height = 140.0, 100.0
			group_input_11.width, group_input_11.height = 140.0, 100.0
			group_008_1.width, group_008_1.height = 184.92144775390625, 100.0
			group_009_1.width, group_009_1.height = 140.0, 100.0
			evaluate_at_index_2.width, evaluate_at_index_2.height = 140.0, 100.0
			evaluate_at_index_001_1.width, evaluate_at_index_001_1.height = 140.0, 100.0
			evaluate_at_index_002_1.width, evaluate_at_index_002_1.height = 140.0, 100.0
			evaluate_at_index_003_1.width, evaluate_at_index_003_1.height = 140.0, 100.0
			math_5.width, math_5.height = 140.0, 100.0
			math_001_1.width, math_001_1.height = 140.0, 100.0
			math_002_2.width, math_002_2.height = 140.0, 100.0
			math_003_1.width, math_003_1.height = 140.0, 100.0
			compare_3.width, compare_3.height = 140.0, 100.0
			integer.width, integer.height = 140.0, 100.0
			frame.width, frame.height = 550.0, 284.0
			switch_1.width, switch_1.height = 140.0, 100.0
			compare_001_2.width, compare_001_2.height = 140.0, 100.0
			vector_math_2.width, vector_math_2.height = 140.0, 100.0
			group_3.width, group_3.height = 140.0, 100.0
			
			#initialize hbond_backbone_check links
			#evaluate_at_index_001_1.Value -> group_008_1.H
			hbond_backbone_check.links.new(evaluate_at_index_001_1.outputs[0], group_008_1.inputs[3])
			#evaluate_at_index_2.Value -> group_008_1.N
			hbond_backbone_check.links.new(evaluate_at_index_2.outputs[0], group_008_1.inputs[2])
			#evaluate_at_index_002_1.Value -> group_008_1.O
			hbond_backbone_check.links.new(evaluate_at_index_002_1.outputs[0], group_008_1.inputs[0])
			#math_001_1.Value -> evaluate_at_index_001_1.Index
			hbond_backbone_check.links.new(math_001_1.outputs[0], evaluate_at_index_001_1.inputs[0])
			#math_001_1.Value -> evaluate_at_index_2.Index
			hbond_backbone_check.links.new(math_001_1.outputs[0], evaluate_at_index_2.inputs[0])
			#evaluate_at_index_003_1.Value -> group_008_1.C
			hbond_backbone_check.links.new(evaluate_at_index_003_1.outputs[0], group_008_1.inputs[1])
			#group_008_1.Bond Energy -> group_output_11.Bond Energy
			hbond_backbone_check.links.new(group_008_1.outputs[1], group_output_11.inputs[1])
			#group_008_1.Bond Vector -> group_output_11.H->O
			hbond_backbone_check.links.new(group_008_1.outputs[2], group_output_11.inputs[2])
			#math_5.Value -> evaluate_at_index_002_1.Index
			hbond_backbone_check.links.new(math_5.outputs[0], evaluate_at_index_002_1.inputs[0])
			#math_5.Value -> evaluate_at_index_003_1.Index
			hbond_backbone_check.links.new(math_5.outputs[0], evaluate_at_index_003_1.inputs[0])
			#group_input_11.CO Index -> math_5.Value
			hbond_backbone_check.links.new(group_input_11.outputs[0], math_5.inputs[0])
			#group_input_11.CO Offset -> math_5.Value
			hbond_backbone_check.links.new(group_input_11.outputs[1], math_5.inputs[1])
			#group_input_11.NH Index -> math_001_1.Value
			hbond_backbone_check.links.new(group_input_11.outputs[2], math_001_1.inputs[0])
			#group_input_11.NH Offset -> math_001_1.Value
			hbond_backbone_check.links.new(group_input_11.outputs[3], math_001_1.inputs[1])
			#math_5.Value -> math_002_2.Value
			hbond_backbone_check.links.new(math_5.outputs[0], math_002_2.inputs[0])
			#math_001_1.Value -> math_002_2.Value
			hbond_backbone_check.links.new(math_001_1.outputs[0], math_002_2.inputs[1])
			#math_002_2.Value -> math_003_1.Value
			hbond_backbone_check.links.new(math_002_2.outputs[0], math_003_1.inputs[0])
			#math_003_1.Value -> compare_3.A
			hbond_backbone_check.links.new(math_003_1.outputs[0], compare_3.inputs[0])
			#integer.Integer -> compare_3.B
			hbond_backbone_check.links.new(integer.outputs[0], compare_3.inputs[1])
			#compare_3.Result -> switch_1.Switch
			hbond_backbone_check.links.new(compare_3.outputs[0], switch_1.inputs[0])
			#group_008_1.Bond Vector -> vector_math_2.Vector
			hbond_backbone_check.links.new(group_008_1.outputs[2], vector_math_2.inputs[0])
			#vector_math_2.Value -> compare_001_2.A
			hbond_backbone_check.links.new(vector_math_2.outputs[1], compare_001_2.inputs[0])
			#group_3.Angstrom -> compare_001_2.B
			hbond_backbone_check.links.new(group_3.outputs[0], compare_001_2.inputs[1])
			#switch_1.Output -> group_output_11.Is Bonded
			hbond_backbone_check.links.new(switch_1.outputs[0], group_output_11.inputs[0])
			#group_008_1.Is Bonded -> switch_1.True
			hbond_backbone_check.links.new(group_008_1.outputs[0], switch_1.inputs[2])
			#group_009_1.O -> evaluate_at_index_002_1.Value
			hbond_backbone_check.links.new(group_009_1.outputs[0], evaluate_at_index_002_1.inputs[1])
			#group_009_1.C -> evaluate_at_index_003_1.Value
			hbond_backbone_check.links.new(group_009_1.outputs[1], evaluate_at_index_003_1.inputs[1])
			#group_009_1.N -> evaluate_at_index_2.Value
			hbond_backbone_check.links.new(group_009_1.outputs[3], evaluate_at_index_2.inputs[1])
			#group_009_1.NH -> evaluate_at_index_001_1.Value
			hbond_backbone_check.links.new(group_009_1.outputs[4], evaluate_at_index_001_1.inputs[1])
			return hbond_backbone_check

		hbond_backbone_check = hbond_backbone_check_node_group()

		#initialize hbond_backbone_check_backup node group
		def hbond_backbone_check_backup_node_group():
			hbond_backbone_check_backup = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "HBond Backbone Check_backup")

			hbond_backbone_check_backup.color_tag = 'NONE'
			hbond_backbone_check_backup.description = ""

			
			#hbond_backbone_check_backup interface
			#Socket Is Bonded
			is_bonded_socket_2 = hbond_backbone_check_backup.interface.new_socket(name = "Is Bonded", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_bonded_socket_2.default_value = False
			is_bonded_socket_2.attribute_domain = 'POINT'
			
			#Socket Bond Energy
			bond_energy_socket_2 = hbond_backbone_check_backup.interface.new_socket(name = "Bond Energy", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			bond_energy_socket_2.default_value = 0.0
			bond_energy_socket_2.min_value = -3.4028234663852886e+38
			bond_energy_socket_2.max_value = 3.4028234663852886e+38
			bond_energy_socket_2.subtype = 'NONE'
			bond_energy_socket_2.attribute_domain = 'POINT'
			
			#Socket H->O
			h__o_socket_1 = hbond_backbone_check_backup.interface.new_socket(name = "H->O", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			h__o_socket_1.default_value = (0.0, 0.0, 0.0)
			h__o_socket_1.min_value = -3.4028234663852886e+38
			h__o_socket_1.max_value = 3.4028234663852886e+38
			h__o_socket_1.subtype = 'NONE'
			h__o_socket_1.attribute_domain = 'POINT'
			
			#Panel CO
			co_panel_1 = hbond_backbone_check_backup.interface.new_panel("CO")
			#Socket CO Index
			co_index_socket_1 = hbond_backbone_check_backup.interface.new_socket(name = "CO Index", in_out='INPUT', socket_type = 'NodeSocketInt', parent = co_panel_1)
			co_index_socket_1.default_value = 0
			co_index_socket_1.min_value = 0
			co_index_socket_1.max_value = 2147483647
			co_index_socket_1.subtype = 'NONE'
			co_index_socket_1.attribute_domain = 'POINT'
			
			#Socket CO Offset
			co_offset_socket_1 = hbond_backbone_check_backup.interface.new_socket(name = "CO Offset", in_out='INPUT', socket_type = 'NodeSocketInt', parent = co_panel_1)
			co_offset_socket_1.default_value = 0
			co_offset_socket_1.min_value = -2147483648
			co_offset_socket_1.max_value = 2147483647
			co_offset_socket_1.subtype = 'NONE'
			co_offset_socket_1.attribute_domain = 'POINT'
			
			
			#Panel NH
			nh_panel_1 = hbond_backbone_check_backup.interface.new_panel("NH")
			#Socket NH Index
			nh_index_socket_1 = hbond_backbone_check_backup.interface.new_socket(name = "NH Index", in_out='INPUT', socket_type = 'NodeSocketInt', parent = nh_panel_1)
			nh_index_socket_1.default_value = 0
			nh_index_socket_1.min_value = 0
			nh_index_socket_1.max_value = 2147483647
			nh_index_socket_1.subtype = 'NONE'
			nh_index_socket_1.attribute_domain = 'POINT'
			
			#Socket NH Offset
			nh_offset_socket_1 = hbond_backbone_check_backup.interface.new_socket(name = "NH Offset", in_out='INPUT', socket_type = 'NodeSocketInt', parent = nh_panel_1)
			nh_offset_socket_1.default_value = 0
			nh_offset_socket_1.min_value = -2147483648
			nh_offset_socket_1.max_value = 2147483647
			nh_offset_socket_1.subtype = 'NONE'
			nh_offset_socket_1.attribute_domain = 'POINT'
			
			
			
			#initialize hbond_backbone_check_backup nodes
			#node Group Output
			group_output_12 = hbond_backbone_check_backup.nodes.new("NodeGroupOutput")
			group_output_12.name = "Group Output"
			group_output_12.is_active_output = True
			
			#node Group Input
			group_input_12 = hbond_backbone_check_backup.nodes.new("NodeGroupInput")
			group_input_12.name = "Group Input"
			
			#node Group.008
			group_008_2 = hbond_backbone_check_backup.nodes.new("GeometryNodeGroup")
			group_008_2.name = "Group.008"
			group_008_2.node_tree = hbond_energy
			
			#node Group.009
			group_009_2 = hbond_backbone_check_backup.nodes.new("GeometryNodeGroup")
			group_009_2.name = "Group.009"
			group_009_2.node_tree = mn_topo_backbone
			#Socket_3
			group_009_2.inputs[0].default_value = 0
			
			#node Evaluate at Index
			evaluate_at_index_3 = hbond_backbone_check_backup.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_3.name = "Evaluate at Index"
			evaluate_at_index_3.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_3.domain = 'POINT'
			
			#node Evaluate at Index.001
			evaluate_at_index_001_2 = hbond_backbone_check_backup.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001_2.name = "Evaluate at Index.001"
			evaluate_at_index_001_2.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_001_2.domain = 'POINT'
			
			#node Evaluate at Index.002
			evaluate_at_index_002_2 = hbond_backbone_check_backup.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_002_2.name = "Evaluate at Index.002"
			evaluate_at_index_002_2.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_002_2.domain = 'POINT'
			
			#node Evaluate at Index.003
			evaluate_at_index_003_2 = hbond_backbone_check_backup.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_003_2.name = "Evaluate at Index.003"
			evaluate_at_index_003_2.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_003_2.domain = 'POINT'
			
			#node Math
			math_6 = hbond_backbone_check_backup.nodes.new("ShaderNodeMath")
			math_6.name = "Math"
			math_6.operation = 'ADD'
			math_6.use_clamp = False
			
			#node Math.001
			math_001_2 = hbond_backbone_check_backup.nodes.new("ShaderNodeMath")
			math_001_2.name = "Math.001"
			math_001_2.operation = 'ADD'
			math_001_2.use_clamp = False
			
			#node Math.002
			math_002_3 = hbond_backbone_check_backup.nodes.new("ShaderNodeMath")
			math_002_3.name = "Math.002"
			math_002_3.operation = 'SUBTRACT'
			math_002_3.use_clamp = False
			
			#node Math.003
			math_003_2 = hbond_backbone_check_backup.nodes.new("ShaderNodeMath")
			math_003_2.name = "Math.003"
			math_003_2.operation = 'ABSOLUTE'
			math_003_2.use_clamp = False
			
			#node Compare
			compare_4 = hbond_backbone_check_backup.nodes.new("FunctionNodeCompare")
			compare_4.name = "Compare"
			compare_4.data_type = 'FLOAT'
			compare_4.mode = 'ELEMENT'
			compare_4.operation = 'GREATER_THAN'
			
			#node Integer
			integer_1 = hbond_backbone_check_backup.nodes.new("FunctionNodeInputInt")
			integer_1.name = "Integer"
			integer_1.integer = 1
			
			#node Frame
			frame_1 = hbond_backbone_check_backup.nodes.new("NodeFrame")
			frame_1.label = "Check not bonded to +/- residues"
			frame_1.name = "Frame"
			frame_1.label_size = 20
			frame_1.shrink = True
			
			#node Switch
			switch_2 = hbond_backbone_check_backup.nodes.new("GeometryNodeSwitch")
			switch_2.name = "Switch"
			switch_2.input_type = 'BOOLEAN'
			#False
			switch_2.inputs[1].default_value = False
			
			#node Compare.001
			compare_001_3 = hbond_backbone_check_backup.nodes.new("FunctionNodeCompare")
			compare_001_3.name = "Compare.001"
			compare_001_3.data_type = 'FLOAT'
			compare_001_3.mode = 'ELEMENT'
			compare_001_3.operation = 'LESS_THAN'
			
			#node Vector Math
			vector_math_3 = hbond_backbone_check_backup.nodes.new("ShaderNodeVectorMath")
			vector_math_3.name = "Vector Math"
			vector_math_3.operation = 'LENGTH'
			
			#node Group
			group_4 = hbond_backbone_check_backup.nodes.new("GeometryNodeGroup")
			group_4.name = "Group"
			group_4.node_tree = mn_units
			#Input_1
			group_4.inputs[0].default_value = 3.0
			
			
			
			#Set parents
			math_002_3.parent = frame_1
			math_003_2.parent = frame_1
			compare_4.parent = frame_1
			integer_1.parent = frame_1
			
			#Set locations
			group_output_12.location = (820.0, 240.0)
			group_input_12.location = (-680.0, 140.0)
			group_008_2.location = (224.2731170654297, 240.0)
			group_009_2.location = (-480.0, 460.0)
			evaluate_at_index_3.location = (-20.0, 40.0)
			evaluate_at_index_001_2.location = (-20.0, -120.0)
			evaluate_at_index_002_2.location = (-20.0, 400.0)
			evaluate_at_index_003_2.location = (-20.0, 240.0)
			math_6.location = (-480.0, 240.0)
			math_001_2.location = (-480.0, 80.0)
			math_002_3.location = (70.0, 640.0)
			math_003_2.location = (240.0, 640.0)
			compare_4.location = (420.0, 640.0)
			integer_1.location = (240.0, 500.0)
			frame_1.location = (-70.0, 40.0)
			switch_2.location = (620.0, 340.0)
			compare_001_3.location = (520.0, 140.0)
			vector_math_3.location = (260.0, 20.0)
			group_4.location = (520.0, -20.0)
			
			#Set dimensions
			group_output_12.width, group_output_12.height = 140.0, 100.0
			group_input_12.width, group_input_12.height = 140.0, 100.0
			group_008_2.width, group_008_2.height = 184.92144775390625, 100.0
			group_009_2.width, group_009_2.height = 140.0, 100.0
			evaluate_at_index_3.width, evaluate_at_index_3.height = 140.0, 100.0
			evaluate_at_index_001_2.width, evaluate_at_index_001_2.height = 140.0, 100.0
			evaluate_at_index_002_2.width, evaluate_at_index_002_2.height = 140.0, 100.0
			evaluate_at_index_003_2.width, evaluate_at_index_003_2.height = 140.0, 100.0
			math_6.width, math_6.height = 140.0, 100.0
			math_001_2.width, math_001_2.height = 140.0, 100.0
			math_002_3.width, math_002_3.height = 140.0, 100.0
			math_003_2.width, math_003_2.height = 140.0, 100.0
			compare_4.width, compare_4.height = 140.0, 100.0
			integer_1.width, integer_1.height = 140.0, 100.0
			frame_1.width, frame_1.height = 550.0, 285.0
			switch_2.width, switch_2.height = 140.0, 100.0
			compare_001_3.width, compare_001_3.height = 140.0, 100.0
			vector_math_3.width, vector_math_3.height = 140.0, 100.0
			group_4.width, group_4.height = 140.0, 100.0
			
			#initialize hbond_backbone_check_backup links
			#evaluate_at_index_001_2.Value -> group_008_2.H
			hbond_backbone_check_backup.links.new(evaluate_at_index_001_2.outputs[0], group_008_2.inputs[3])
			#evaluate_at_index_3.Value -> group_008_2.N
			hbond_backbone_check_backup.links.new(evaluate_at_index_3.outputs[0], group_008_2.inputs[2])
			#evaluate_at_index_002_2.Value -> group_008_2.O
			hbond_backbone_check_backup.links.new(evaluate_at_index_002_2.outputs[0], group_008_2.inputs[0])
			#math_001_2.Value -> evaluate_at_index_001_2.Index
			hbond_backbone_check_backup.links.new(math_001_2.outputs[0], evaluate_at_index_001_2.inputs[0])
			#math_001_2.Value -> evaluate_at_index_3.Index
			hbond_backbone_check_backup.links.new(math_001_2.outputs[0], evaluate_at_index_3.inputs[0])
			#evaluate_at_index_003_2.Value -> group_008_2.C
			hbond_backbone_check_backup.links.new(evaluate_at_index_003_2.outputs[0], group_008_2.inputs[1])
			#group_009_2.NH -> evaluate_at_index_001_2.Value
			hbond_backbone_check_backup.links.new(group_009_2.outputs[4], evaluate_at_index_001_2.inputs[1])
			#group_009_2.N -> evaluate_at_index_3.Value
			hbond_backbone_check_backup.links.new(group_009_2.outputs[3], evaluate_at_index_3.inputs[1])
			#group_008_2.Bond Energy -> group_output_12.Bond Energy
			hbond_backbone_check_backup.links.new(group_008_2.outputs[1], group_output_12.inputs[1])
			#group_008_2.Bond Vector -> group_output_12.H->O
			hbond_backbone_check_backup.links.new(group_008_2.outputs[2], group_output_12.inputs[2])
			#group_009_2.O -> evaluate_at_index_002_2.Value
			hbond_backbone_check_backup.links.new(group_009_2.outputs[0], evaluate_at_index_002_2.inputs[1])
			#group_009_2.C -> evaluate_at_index_003_2.Value
			hbond_backbone_check_backup.links.new(group_009_2.outputs[1], evaluate_at_index_003_2.inputs[1])
			#math_6.Value -> evaluate_at_index_002_2.Index
			hbond_backbone_check_backup.links.new(math_6.outputs[0], evaluate_at_index_002_2.inputs[0])
			#math_6.Value -> evaluate_at_index_003_2.Index
			hbond_backbone_check_backup.links.new(math_6.outputs[0], evaluate_at_index_003_2.inputs[0])
			#group_input_12.CO Index -> math_6.Value
			hbond_backbone_check_backup.links.new(group_input_12.outputs[0], math_6.inputs[0])
			#group_input_12.CO Offset -> math_6.Value
			hbond_backbone_check_backup.links.new(group_input_12.outputs[1], math_6.inputs[1])
			#group_input_12.NH Index -> math_001_2.Value
			hbond_backbone_check_backup.links.new(group_input_12.outputs[2], math_001_2.inputs[0])
			#group_input_12.NH Offset -> math_001_2.Value
			hbond_backbone_check_backup.links.new(group_input_12.outputs[3], math_001_2.inputs[1])
			#math_6.Value -> math_002_3.Value
			hbond_backbone_check_backup.links.new(math_6.outputs[0], math_002_3.inputs[0])
			#math_001_2.Value -> math_002_3.Value
			hbond_backbone_check_backup.links.new(math_001_2.outputs[0], math_002_3.inputs[1])
			#math_002_3.Value -> math_003_2.Value
			hbond_backbone_check_backup.links.new(math_002_3.outputs[0], math_003_2.inputs[0])
			#math_003_2.Value -> compare_4.A
			hbond_backbone_check_backup.links.new(math_003_2.outputs[0], compare_4.inputs[0])
			#integer_1.Integer -> compare_4.B
			hbond_backbone_check_backup.links.new(integer_1.outputs[0], compare_4.inputs[1])
			#compare_4.Result -> switch_2.Switch
			hbond_backbone_check_backup.links.new(compare_4.outputs[0], switch_2.inputs[0])
			#group_008_2.Bond Vector -> vector_math_3.Vector
			hbond_backbone_check_backup.links.new(group_008_2.outputs[2], vector_math_3.inputs[0])
			#vector_math_3.Value -> compare_001_3.A
			hbond_backbone_check_backup.links.new(vector_math_3.outputs[1], compare_001_3.inputs[0])
			#group_4.Angstrom -> compare_001_3.B
			hbond_backbone_check_backup.links.new(group_4.outputs[0], compare_001_3.inputs[1])
			#switch_2.Output -> group_output_12.Is Bonded
			hbond_backbone_check_backup.links.new(switch_2.outputs[0], group_output_12.inputs[0])
			#group_008_2.Is Bonded -> switch_2.True
			hbond_backbone_check_backup.links.new(group_008_2.outputs[0], switch_2.inputs[2])
			return hbond_backbone_check_backup

		hbond_backbone_check_backup = hbond_backbone_check_backup_node_group()

		#initialize _hbond_i__j__and_hbond_j__i_ node group
		def _hbond_i__j__and_hbond_j__i__node_group():
			_hbond_i__j__and_hbond_j__i_ = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".HBond(i, j) and HBond(j, i)")

			_hbond_i__j__and_hbond_j__i_.color_tag = 'NONE'
			_hbond_i__j__and_hbond_j__i_.description = ""

			
			#_hbond_i__j__and_hbond_j__i_ interface
			#Socket Boolean
			boolean_socket_4 = _hbond_i__j__and_hbond_j__i_.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket_4.default_value = False
			boolean_socket_4.attribute_domain = 'POINT'
			
			#Socket i
			i_socket = _hbond_i__j__and_hbond_j__i_.interface.new_socket(name = "i", in_out='INPUT', socket_type = 'NodeSocketInt')
			i_socket.default_value = 0
			i_socket.min_value = 0
			i_socket.max_value = 2147483647
			i_socket.subtype = 'NONE'
			i_socket.attribute_domain = 'POINT'
			i_socket.hide_value = True
			
			#Socket j
			j_socket = _hbond_i__j__and_hbond_j__i_.interface.new_socket(name = "j", in_out='INPUT', socket_type = 'NodeSocketInt')
			j_socket.default_value = 0
			j_socket.min_value = 0
			j_socket.max_value = 2147483647
			j_socket.subtype = 'NONE'
			j_socket.attribute_domain = 'POINT'
			j_socket.hide_value = True
			
			
			#initialize _hbond_i__j__and_hbond_j__i_ nodes
			#node Group Output
			group_output_13 = _hbond_i__j__and_hbond_j__i_.nodes.new("NodeGroupOutput")
			group_output_13.name = "Group Output"
			group_output_13.is_active_output = True
			
			#node Group Input
			group_input_13 = _hbond_i__j__and_hbond_j__i_.nodes.new("NodeGroupInput")
			group_input_13.name = "Group Input"
			
			#node Group.010
			group_010_1 = _hbond_i__j__and_hbond_j__i_.nodes.new("GeometryNodeGroup")
			group_010_1.name = "Group.010"
			group_010_1.node_tree = hbond_backbone_check
			#Socket_5
			group_010_1.inputs[1].default_value = 0
			#Socket_6
			group_010_1.inputs[3].default_value = 0
			
			#node Group.011
			group_011 = _hbond_i__j__and_hbond_j__i_.nodes.new("GeometryNodeGroup")
			group_011.name = "Group.011"
			group_011.node_tree = hbond_backbone_check
			#Socket_5
			group_011.inputs[1].default_value = 0
			#Socket_6
			group_011.inputs[3].default_value = 0
			
			#node Frame
			frame_2 = _hbond_i__j__and_hbond_j__i_.nodes.new("NodeFrame")
			frame_2.label = "Check Backbone O is bonded to an NH"
			frame_2.name = "Frame"
			frame_2.label_size = 20
			frame_2.shrink = True
			
			#node Frame.001
			frame_001 = _hbond_i__j__and_hbond_j__i_.nodes.new("NodeFrame")
			frame_001.label = "Check Backbone NH is bonded to an O"
			frame_001.name = "Frame.001"
			frame_001.label_size = 20
			frame_001.shrink = True
			
			#node Boolean Math.003
			boolean_math_003_1 = _hbond_i__j__and_hbond_j__i_.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003_1.name = "Boolean Math.003"
			boolean_math_003_1.operation = 'AND'
			
			#node Group.012
			group_012 = _hbond_i__j__and_hbond_j__i_.nodes.new("GeometryNodeGroup")
			group_012.name = "Group.012"
			group_012.node_tree = hbond_backbone_check_backup
			#Socket_3
			group_012.inputs[0].default_value = 0
			#Socket_5
			group_012.inputs[1].default_value = 0
			#Socket_0
			group_012.inputs[2].default_value = 0
			#Socket_6
			group_012.inputs[3].default_value = 0
			
			
			
			#Set parents
			group_010_1.parent = frame_001
			group_011.parent = frame_2
			
			#Set locations
			group_output_13.location = (640.0, 180.0)
			group_input_13.location = (-235.75640869140625, 47.462432861328125)
			group_010_1.location = (-640.0, 40.0)
			group_011.location = (-640.0, -220.0)
			frame_2.location = (635.0, 20.0)
			frame_001.location = (630.0, 140.0)
			boolean_math_003_1.location = (435.0, 180.0)
			group_012.location = (-20.0, 520.0)
			
			#Set dimensions
			group_output_13.width, group_output_13.height = 140.0, 100.0
			group_input_13.width, group_input_13.height = 140.0, 100.0
			group_010_1.width, group_010_1.height = 267.0645751953125, 100.0
			group_011.width, group_011.height = 267.0645751953125, 100.0
			frame_2.width, frame_2.height = 327.0645751953125, 309.0
			frame_001.width, frame_001.height = 327.0645751953125, 309.0
			boolean_math_003_1.width, boolean_math_003_1.height = 140.0, 100.0
			group_012.width, group_012.height = 267.0645751953125, 100.0
			
			#initialize _hbond_i__j__and_hbond_j__i_ links
			#group_010_1.Is Bonded -> boolean_math_003_1.Boolean
			_hbond_i__j__and_hbond_j__i_.links.new(group_010_1.outputs[0], boolean_math_003_1.inputs[0])
			#group_011.Is Bonded -> boolean_math_003_1.Boolean
			_hbond_i__j__and_hbond_j__i_.links.new(group_011.outputs[0], boolean_math_003_1.inputs[1])
			#boolean_math_003_1.Boolean -> group_output_13.Boolean
			_hbond_i__j__and_hbond_j__i_.links.new(boolean_math_003_1.outputs[0], group_output_13.inputs[0])
			#group_input_13.j -> group_010_1.NH Index
			_hbond_i__j__and_hbond_j__i_.links.new(group_input_13.outputs[1], group_010_1.inputs[2])
			#group_input_13.j -> group_011.CO Index
			_hbond_i__j__and_hbond_j__i_.links.new(group_input_13.outputs[1], group_011.inputs[0])
			#group_input_13.i -> group_010_1.CO Index
			_hbond_i__j__and_hbond_j__i_.links.new(group_input_13.outputs[0], group_010_1.inputs[0])
			#group_input_13.i -> group_011.NH Index
			_hbond_i__j__and_hbond_j__i_.links.new(group_input_13.outputs[0], group_011.inputs[2])
			return _hbond_i__j__and_hbond_j__i_

		_hbond_i__j__and_hbond_j__i_ = _hbond_i__j__and_hbond_j__i__node_group()

		#initialize _hbond_i___1__j___1__and_hbond_j___1__i___1_ node group
		def _hbond_i___1__j___1__and_hbond_j___1__i___1__node_group():
			_hbond_i___1__j___1__and_hbond_j___1__i___1_ = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".HBond(i - 1, j + 1) and HBond(j - 1, i + 1)")

			_hbond_i___1__j___1__and_hbond_j___1__i___1_.color_tag = 'NONE'
			_hbond_i___1__j___1__and_hbond_j___1__i___1_.description = ""

			
			#_hbond_i___1__j___1__and_hbond_j___1__i___1_ interface
			#Socket Boolean
			boolean_socket_5 = _hbond_i___1__j___1__and_hbond_j___1__i___1_.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket_5.default_value = False
			boolean_socket_5.attribute_domain = 'POINT'
			
			#Socket i
			i_socket_1 = _hbond_i___1__j___1__and_hbond_j___1__i___1_.interface.new_socket(name = "i", in_out='INPUT', socket_type = 'NodeSocketInt')
			i_socket_1.default_value = 0
			i_socket_1.min_value = 0
			i_socket_1.max_value = 2147483647
			i_socket_1.subtype = 'NONE'
			i_socket_1.attribute_domain = 'POINT'
			i_socket_1.hide_value = True
			
			#Socket j
			j_socket_1 = _hbond_i___1__j___1__and_hbond_j___1__i___1_.interface.new_socket(name = "j", in_out='INPUT', socket_type = 'NodeSocketInt')
			j_socket_1.default_value = 0
			j_socket_1.min_value = 0
			j_socket_1.max_value = 2147483647
			j_socket_1.subtype = 'NONE'
			j_socket_1.attribute_domain = 'POINT'
			j_socket_1.hide_value = True
			
			
			#initialize _hbond_i___1__j___1__and_hbond_j___1__i___1_ nodes
			#node Group Output
			group_output_14 = _hbond_i___1__j___1__and_hbond_j___1__i___1_.nodes.new("NodeGroupOutput")
			group_output_14.name = "Group Output"
			group_output_14.is_active_output = True
			
			#node Group Input
			group_input_14 = _hbond_i___1__j___1__and_hbond_j___1__i___1_.nodes.new("NodeGroupInput")
			group_input_14.name = "Group Input"
			
			#node Group.010
			group_010_2 = _hbond_i___1__j___1__and_hbond_j___1__i___1_.nodes.new("GeometryNodeGroup")
			group_010_2.name = "Group.010"
			group_010_2.node_tree = hbond_backbone_check
			#Socket_5
			group_010_2.inputs[1].default_value = -1
			#Socket_6
			group_010_2.inputs[3].default_value = 1
			
			#node Group.011
			group_011_1 = _hbond_i___1__j___1__and_hbond_j___1__i___1_.nodes.new("GeometryNodeGroup")
			group_011_1.name = "Group.011"
			group_011_1.node_tree = hbond_backbone_check
			#Socket_5
			group_011_1.inputs[1].default_value = -1
			#Socket_6
			group_011_1.inputs[3].default_value = 1
			
			#node Frame
			frame_3 = _hbond_i___1__j___1__and_hbond_j___1__i___1_.nodes.new("NodeFrame")
			frame_3.label = "Check Backbone O is bonded to an NH"
			frame_3.name = "Frame"
			frame_3.label_size = 20
			frame_3.shrink = True
			
			#node Frame.001
			frame_001_1 = _hbond_i___1__j___1__and_hbond_j___1__i___1_.nodes.new("NodeFrame")
			frame_001_1.label = "Check Backbone NH is bonded to an O"
			frame_001_1.name = "Frame.001"
			frame_001_1.label_size = 20
			frame_001_1.shrink = True
			
			#node Boolean Math.003
			boolean_math_003_2 = _hbond_i___1__j___1__and_hbond_j___1__i___1_.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003_2.name = "Boolean Math.003"
			boolean_math_003_2.operation = 'AND'
			
			
			
			#Set parents
			group_010_2.parent = frame_001_1
			group_011_1.parent = frame_3
			
			#Set locations
			group_output_14.location = (625.0, 0.0)
			group_input_14.location = (-394.84100341796875, -236.38262939453125)
			group_010_2.location = (-655.0, 40.0)
			group_011_1.location = (-640.0, -220.0)
			frame_3.location = (635.0, 20.0)
			frame_001_1.location = (655.0, 120.0)
			boolean_math_003_2.location = (435.0, 180.0)
			
			#Set dimensions
			group_output_14.width, group_output_14.height = 140.0, 100.0
			group_input_14.width, group_input_14.height = 140.0, 100.0
			group_010_2.width, group_010_2.height = 267.0645751953125, 100.0
			group_011_1.width, group_011_1.height = 267.0645751953125, 100.0
			frame_3.width, frame_3.height = 327.0645751953125, 309.0
			frame_001_1.width, frame_001_1.height = 327.0645751953125, 309.0
			boolean_math_003_2.width, boolean_math_003_2.height = 140.0, 100.0
			
			#initialize _hbond_i___1__j___1__and_hbond_j___1__i___1_ links
			#group_010_2.Is Bonded -> boolean_math_003_2.Boolean
			_hbond_i___1__j___1__and_hbond_j___1__i___1_.links.new(group_010_2.outputs[0], boolean_math_003_2.inputs[0])
			#group_011_1.Is Bonded -> boolean_math_003_2.Boolean
			_hbond_i___1__j___1__and_hbond_j___1__i___1_.links.new(group_011_1.outputs[0], boolean_math_003_2.inputs[1])
			#boolean_math_003_2.Boolean -> group_output_14.Boolean
			_hbond_i___1__j___1__and_hbond_j___1__i___1_.links.new(boolean_math_003_2.outputs[0], group_output_14.inputs[0])
			#group_input_14.j -> group_010_2.NH Index
			_hbond_i___1__j___1__and_hbond_j___1__i___1_.links.new(group_input_14.outputs[1], group_010_2.inputs[2])
			#group_input_14.j -> group_011_1.CO Index
			_hbond_i___1__j___1__and_hbond_j___1__i___1_.links.new(group_input_14.outputs[1], group_011_1.inputs[0])
			#group_input_14.i -> group_010_2.CO Index
			_hbond_i___1__j___1__and_hbond_j___1__i___1_.links.new(group_input_14.outputs[0], group_010_2.inputs[0])
			#group_input_14.i -> group_011_1.NH Index
			_hbond_i___1__j___1__and_hbond_j___1__i___1_.links.new(group_input_14.outputs[0], group_011_1.inputs[2])
			return _hbond_i___1__j___1__and_hbond_j___1__i___1_

		_hbond_i___1__j___1__and_hbond_j___1__i___1_ = _hbond_i___1__j___1__and_hbond_j___1__i___1__node_group()

		#initialize _hbond_i___1_j__and_hbond_j_i___1_ node group
		def _hbond_i___1_j__and_hbond_j_i___1__node_group():
			_hbond_i___1_j__and_hbond_j_i___1_ = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".Hbond(i - 1,j) and Hbond(j,i + 1)")

			_hbond_i___1_j__and_hbond_j_i___1_.color_tag = 'NONE'
			_hbond_i___1_j__and_hbond_j_i___1_.description = ""

			
			#_hbond_i___1_j__and_hbond_j_i___1_ interface
			#Socket Boolean
			boolean_socket_6 = _hbond_i___1_j__and_hbond_j_i___1_.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket_6.default_value = False
			boolean_socket_6.attribute_domain = 'POINT'
			
			#Socket i
			i_socket_2 = _hbond_i___1_j__and_hbond_j_i___1_.interface.new_socket(name = "i", in_out='INPUT', socket_type = 'NodeSocketInt')
			i_socket_2.default_value = 0
			i_socket_2.min_value = 0
			i_socket_2.max_value = 2147483647
			i_socket_2.subtype = 'NONE'
			i_socket_2.attribute_domain = 'POINT'
			i_socket_2.hide_value = True
			
			#Socket j
			j_socket_2 = _hbond_i___1_j__and_hbond_j_i___1_.interface.new_socket(name = "j", in_out='INPUT', socket_type = 'NodeSocketInt')
			j_socket_2.default_value = 0
			j_socket_2.min_value = 0
			j_socket_2.max_value = 2147483647
			j_socket_2.subtype = 'NONE'
			j_socket_2.attribute_domain = 'POINT'
			j_socket_2.hide_value = True
			
			
			#initialize _hbond_i___1_j__and_hbond_j_i___1_ nodes
			#node Group Output
			group_output_15 = _hbond_i___1_j__and_hbond_j_i___1_.nodes.new("NodeGroupOutput")
			group_output_15.name = "Group Output"
			group_output_15.is_active_output = True
			
			#node Group Input
			group_input_15 = _hbond_i___1_j__and_hbond_j_i___1_.nodes.new("NodeGroupInput")
			group_input_15.name = "Group Input"
			
			#node Group.010
			group_010_3 = _hbond_i___1_j__and_hbond_j_i___1_.nodes.new("GeometryNodeGroup")
			group_010_3.name = "Group.010"
			group_010_3.node_tree = hbond_backbone_check
			#Socket_5
			group_010_3.inputs[1].default_value = -1
			#Socket_6
			group_010_3.inputs[3].default_value = 0
			
			#node Group.011
			group_011_2 = _hbond_i___1_j__and_hbond_j_i___1_.nodes.new("GeometryNodeGroup")
			group_011_2.name = "Group.011"
			group_011_2.node_tree = hbond_backbone_check
			#Socket_5
			group_011_2.inputs[1].default_value = 0
			#Socket_6
			group_011_2.inputs[3].default_value = 1
			
			#node Frame
			frame_4 = _hbond_i___1_j__and_hbond_j_i___1_.nodes.new("NodeFrame")
			frame_4.label = "Check Backbone O is bonded to an NH"
			frame_4.name = "Frame"
			frame_4.label_size = 20
			frame_4.shrink = True
			
			#node Frame.001
			frame_001_2 = _hbond_i___1_j__and_hbond_j_i___1_.nodes.new("NodeFrame")
			frame_001_2.label = "Check Backbone NH is bonded to an O"
			frame_001_2.name = "Frame.001"
			frame_001_2.label_size = 20
			frame_001_2.shrink = True
			
			#node Boolean Math.003
			boolean_math_003_3 = _hbond_i___1_j__and_hbond_j_i___1_.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003_3.name = "Boolean Math.003"
			boolean_math_003_3.operation = 'AND'
			
			
			
			#Set parents
			group_010_3.parent = frame_001_2
			group_011_2.parent = frame_4
			
			#Set locations
			group_output_15.location = (625.0, 0.0)
			group_input_15.location = (-373.2626953125, 13.94732666015625)
			group_010_3.location = (-640.0, 40.0)
			group_011_2.location = (-640.0, -220.0)
			frame_4.location = (635.0, 20.0)
			frame_001_2.location = (655.0, 120.0)
			boolean_math_003_3.location = (435.0, 180.0)
			
			#Set dimensions
			group_output_15.width, group_output_15.height = 140.0, 100.0
			group_input_15.width, group_input_15.height = 140.0, 100.0
			group_010_3.width, group_010_3.height = 267.0645751953125, 100.0
			group_011_2.width, group_011_2.height = 267.0645751953125, 100.0
			frame_4.width, frame_4.height = 327.0645751953125, 309.0
			frame_001_2.width, frame_001_2.height = 327.0645751953125, 309.0
			boolean_math_003_3.width, boolean_math_003_3.height = 140.0, 100.0
			
			#initialize _hbond_i___1_j__and_hbond_j_i___1_ links
			#group_010_3.Is Bonded -> boolean_math_003_3.Boolean
			_hbond_i___1_j__and_hbond_j_i___1_.links.new(group_010_3.outputs[0], boolean_math_003_3.inputs[0])
			#group_011_2.Is Bonded -> boolean_math_003_3.Boolean
			_hbond_i___1_j__and_hbond_j_i___1_.links.new(group_011_2.outputs[0], boolean_math_003_3.inputs[1])
			#boolean_math_003_3.Boolean -> group_output_15.Boolean
			_hbond_i___1_j__and_hbond_j_i___1_.links.new(boolean_math_003_3.outputs[0], group_output_15.inputs[0])
			#group_input_15.j -> group_010_3.NH Index
			_hbond_i___1_j__and_hbond_j_i___1_.links.new(group_input_15.outputs[1], group_010_3.inputs[2])
			#group_input_15.j -> group_011_2.CO Index
			_hbond_i___1_j__and_hbond_j_i___1_.links.new(group_input_15.outputs[1], group_011_2.inputs[0])
			#group_input_15.i -> group_010_3.CO Index
			_hbond_i___1_j__and_hbond_j_i___1_.links.new(group_input_15.outputs[0], group_010_3.inputs[0])
			#group_input_15.i -> group_011_2.NH Index
			_hbond_i___1_j__and_hbond_j_i___1_.links.new(group_input_15.outputs[0], group_011_2.inputs[2])
			return _hbond_i___1_j__and_hbond_j_i___1_

		_hbond_i___1_j__and_hbond_j_i___1_ = _hbond_i___1_j__and_hbond_j_i___1__node_group()

		#initialize _hbond_j___1_i_and_hbond_i_j___1_ node group
		def _hbond_j___1_i_and_hbond_i_j___1__node_group():
			_hbond_j___1_i_and_hbond_i_j___1_ = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".Hbond(j - 1,i)and Hbond(i,j + 1)")

			_hbond_j___1_i_and_hbond_i_j___1_.color_tag = 'NONE'
			_hbond_j___1_i_and_hbond_i_j___1_.description = ""

			
			#_hbond_j___1_i_and_hbond_i_j___1_ interface
			#Socket Boolean
			boolean_socket_7 = _hbond_j___1_i_and_hbond_i_j___1_.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket_7.default_value = False
			boolean_socket_7.attribute_domain = 'POINT'
			
			#Socket i
			i_socket_3 = _hbond_j___1_i_and_hbond_i_j___1_.interface.new_socket(name = "i", in_out='INPUT', socket_type = 'NodeSocketInt')
			i_socket_3.default_value = 0
			i_socket_3.min_value = 0
			i_socket_3.max_value = 2147483647
			i_socket_3.subtype = 'NONE'
			i_socket_3.attribute_domain = 'POINT'
			i_socket_3.hide_value = True
			
			#Socket j
			j_socket_3 = _hbond_j___1_i_and_hbond_i_j___1_.interface.new_socket(name = "j", in_out='INPUT', socket_type = 'NodeSocketInt')
			j_socket_3.default_value = 0
			j_socket_3.min_value = 0
			j_socket_3.max_value = 2147483647
			j_socket_3.subtype = 'NONE'
			j_socket_3.attribute_domain = 'POINT'
			j_socket_3.hide_value = True
			
			
			#initialize _hbond_j___1_i_and_hbond_i_j___1_ nodes
			#node Group Output
			group_output_16 = _hbond_j___1_i_and_hbond_i_j___1_.nodes.new("NodeGroupOutput")
			group_output_16.name = "Group Output"
			group_output_16.is_active_output = True
			
			#node Group Input
			group_input_16 = _hbond_j___1_i_and_hbond_i_j___1_.nodes.new("NodeGroupInput")
			group_input_16.name = "Group Input"
			
			#node Group.010
			group_010_4 = _hbond_j___1_i_and_hbond_i_j___1_.nodes.new("GeometryNodeGroup")
			group_010_4.name = "Group.010"
			group_010_4.node_tree = hbond_backbone_check
			#Socket_5
			group_010_4.inputs[1].default_value = -1
			#Socket_6
			group_010_4.inputs[3].default_value = 0
			
			#node Group.011
			group_011_3 = _hbond_j___1_i_and_hbond_i_j___1_.nodes.new("GeometryNodeGroup")
			group_011_3.name = "Group.011"
			group_011_3.node_tree = hbond_backbone_check
			#Socket_5
			group_011_3.inputs[1].default_value = 0
			#Socket_6
			group_011_3.inputs[3].default_value = 1
			
			#node Frame
			frame_5 = _hbond_j___1_i_and_hbond_i_j___1_.nodes.new("NodeFrame")
			frame_5.label = "Check Backbone O is bonded to an NH"
			frame_5.name = "Frame"
			frame_5.label_size = 20
			frame_5.shrink = True
			
			#node Frame.001
			frame_001_3 = _hbond_j___1_i_and_hbond_i_j___1_.nodes.new("NodeFrame")
			frame_001_3.label = "Check Backbone NH is bonded to an O"
			frame_001_3.name = "Frame.001"
			frame_001_3.label_size = 20
			frame_001_3.shrink = True
			
			#node Boolean Math.003
			boolean_math_003_4 = _hbond_j___1_i_and_hbond_i_j___1_.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003_4.name = "Boolean Math.003"
			boolean_math_003_4.operation = 'AND'
			
			
			
			#Set parents
			group_010_4.parent = frame_001_3
			group_011_3.parent = frame_5
			
			#Set locations
			group_output_16.location = (625.0, 0.0)
			group_input_16.location = (-360.0, 120.0)
			group_010_4.location = (-640.0, 40.0)
			group_011_3.location = (-640.0, -220.0)
			frame_5.location = (635.0, 20.0)
			frame_001_3.location = (655.0, 120.0)
			boolean_math_003_4.location = (435.0, 180.0)
			
			#Set dimensions
			group_output_16.width, group_output_16.height = 140.0, 100.0
			group_input_16.width, group_input_16.height = 140.0, 100.0
			group_010_4.width, group_010_4.height = 267.0645751953125, 100.0
			group_011_3.width, group_011_3.height = 267.0645751953125, 100.0
			frame_5.width, frame_5.height = 327.0645751953125, 309.0
			frame_001_3.width, frame_001_3.height = 327.0645751953125, 309.0
			boolean_math_003_4.width, boolean_math_003_4.height = 140.0, 100.0
			
			#initialize _hbond_j___1_i_and_hbond_i_j___1_ links
			#group_010_4.Is Bonded -> boolean_math_003_4.Boolean
			_hbond_j___1_i_and_hbond_i_j___1_.links.new(group_010_4.outputs[0], boolean_math_003_4.inputs[0])
			#group_011_3.Is Bonded -> boolean_math_003_4.Boolean
			_hbond_j___1_i_and_hbond_i_j___1_.links.new(group_011_3.outputs[0], boolean_math_003_4.inputs[1])
			#boolean_math_003_4.Boolean -> group_output_16.Boolean
			_hbond_j___1_i_and_hbond_i_j___1_.links.new(boolean_math_003_4.outputs[0], group_output_16.inputs[0])
			#group_input_16.j -> group_011_3.NH Index
			_hbond_j___1_i_and_hbond_i_j___1_.links.new(group_input_16.outputs[1], group_011_3.inputs[2])
			#group_input_16.j -> group_010_4.CO Index
			_hbond_j___1_i_and_hbond_i_j___1_.links.new(group_input_16.outputs[1], group_010_4.inputs[0])
			#group_input_16.i -> group_010_4.NH Index
			_hbond_j___1_i_and_hbond_i_j___1_.links.new(group_input_16.outputs[0], group_010_4.inputs[2])
			#group_input_16.i -> group_011_3.CO Index
			_hbond_j___1_i_and_hbond_i_j___1_.links.new(group_input_16.outputs[0], group_011_3.inputs[0])
			return _hbond_j___1_i_and_hbond_i_j___1_

		_hbond_j___1_i_and_hbond_i_j___1_ = _hbond_j___1_i_and_hbond_i_j___1__node_group()

		#initialize _dssp_sheet_checks node group
		def _dssp_sheet_checks_node_group():
			_dssp_sheet_checks = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".DSSP Sheet Checks")

			_dssp_sheet_checks.color_tag = 'NONE'
			_dssp_sheet_checks.description = ""

			
			#_dssp_sheet_checks interface
			#Socket Boolean
			boolean_socket_8 = _dssp_sheet_checks.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket_8.default_value = False
			boolean_socket_8.attribute_domain = 'POINT'
			
			#Socket j
			j_socket_4 = _dssp_sheet_checks.interface.new_socket(name = "j", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			j_socket_4.default_value = 0
			j_socket_4.min_value = -2147483648
			j_socket_4.max_value = 2147483647
			j_socket_4.subtype = 'NONE'
			j_socket_4.attribute_domain = 'POINT'
			
			#Socket Index
			index_socket_1 = _dssp_sheet_checks.interface.new_socket(name = "Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			index_socket_1.default_value = 0
			index_socket_1.min_value = 0
			index_socket_1.max_value = 2147483647
			index_socket_1.subtype = 'NONE'
			index_socket_1.attribute_domain = 'POINT'
			index_socket_1.hide_value = True
			
			#Socket j
			j_socket_5 = _dssp_sheet_checks.interface.new_socket(name = "j", in_out='INPUT', socket_type = 'NodeSocketInt')
			j_socket_5.default_value = 0
			j_socket_5.min_value = -2147483648
			j_socket_5.max_value = 2147483647
			j_socket_5.subtype = 'NONE'
			j_socket_5.attribute_domain = 'POINT'
			
			
			#initialize _dssp_sheet_checks nodes
			#node Group Output
			group_output_17 = _dssp_sheet_checks.nodes.new("NodeGroupOutput")
			group_output_17.name = "Group Output"
			group_output_17.is_active_output = True
			
			#node Group Input
			group_input_17 = _dssp_sheet_checks.nodes.new("NodeGroupInput")
			group_input_17.name = "Group Input"
			
			#node Group.001
			group_001_1 = _dssp_sheet_checks.nodes.new("GeometryNodeGroup")
			group_001_1.name = "Group.001"
			group_001_1.node_tree = _hbond_i__j__and_hbond_j__i_
			
			#node Group.002
			group_002_1 = _dssp_sheet_checks.nodes.new("GeometryNodeGroup")
			group_002_1.name = "Group.002"
			group_002_1.node_tree = _hbond_i___1__j___1__and_hbond_j___1__i___1_
			
			#node Boolean Math
			boolean_math_2 = _dssp_sheet_checks.nodes.new("FunctionNodeBooleanMath")
			boolean_math_2.name = "Boolean Math"
			boolean_math_2.operation = 'OR'
			
			#node Group.004
			group_004 = _dssp_sheet_checks.nodes.new("GeometryNodeGroup")
			group_004.name = "Group.004"
			group_004.node_tree = _hbond_i___1_j__and_hbond_j_i___1_
			
			#node Frame
			frame_6 = _dssp_sheet_checks.nodes.new("NodeFrame")
			frame_6.label = "Anti-parallel Bridge"
			frame_6.name = "Frame"
			frame_6.label_size = 20
			frame_6.shrink = True
			
			#node Frame.001
			frame_001_4 = _dssp_sheet_checks.nodes.new("NodeFrame")
			frame_001_4.label = "Paralell Bridge"
			frame_001_4.name = "Frame.001"
			frame_001_4.label_size = 20
			frame_001_4.shrink = True
			
			#node Boolean Math.001
			boolean_math_001_1 = _dssp_sheet_checks.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_1.name = "Boolean Math.001"
			boolean_math_001_1.operation = 'OR'
			
			#node Boolean Math.002
			boolean_math_002_1 = _dssp_sheet_checks.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_1.name = "Boolean Math.002"
			boolean_math_002_1.operation = 'OR'
			
			#node Group.005
			group_005 = _dssp_sheet_checks.nodes.new("GeometryNodeGroup")
			group_005.name = "Group.005"
			group_005.node_tree = _hbond_j___1_i_and_hbond_i_j___1_
			
			
			
			#Set parents
			group_001_1.parent = frame_6
			group_002_1.parent = frame_6
			boolean_math_2.parent = frame_6
			group_004.parent = frame_001_4
			boolean_math_001_1.parent = frame_001_4
			group_005.parent = frame_001_4
			
			#Set locations
			group_output_17.location = (570.0, 0.0)
			group_input_17.location = (-657.7005004882812, 1.8694610595703125)
			group_001_1.location = (-800.0, 160.0)
			group_002_1.location = (-800.0, 0.0)
			boolean_math_2.location = (-440.0, 160.0)
			group_004.location = (-800.0, -300.0)
			frame_6.location = (580.0, 180.0)
			frame_001_4.location = (580.0, 180.0)
			boolean_math_001_1.location = (-440.0, -300.0)
			boolean_math_002_1.location = (380.0, 140.0)
			group_005.location = (-800.0, -460.0)
			
			#Set dimensions
			group_output_17.width, group_output_17.height = 140.0, 100.0
			group_input_17.width, group_input_17.height = 140.0, 100.0
			group_001_1.width, group_001_1.height = 333.0748291015625, 100.0
			group_002_1.width, group_002_1.height = 333.0748291015625, 100.0
			boolean_math_2.width, boolean_math_2.height = 140.0, 100.0
			group_004.width, group_004.height = 333.0748291015625, 100.0
			frame_6.width, frame_6.height = 560.0, 350.0
			frame_001_4.width, frame_001_4.height = 560.0, 350.0
			boolean_math_001_1.width, boolean_math_001_1.height = 140.0, 100.0
			boolean_math_002_1.width, boolean_math_002_1.height = 140.0, 100.0
			group_005.width, group_005.height = 333.0748291015625, 100.0
			
			#initialize _dssp_sheet_checks links
			#group_001_1.Boolean -> boolean_math_2.Boolean
			_dssp_sheet_checks.links.new(group_001_1.outputs[0], boolean_math_2.inputs[0])
			#group_input_17.j -> group_002_1.j
			_dssp_sheet_checks.links.new(group_input_17.outputs[1], group_002_1.inputs[1])
			#boolean_math_001_1.Boolean -> boolean_math_002_1.Boolean
			_dssp_sheet_checks.links.new(boolean_math_001_1.outputs[0], boolean_math_002_1.inputs[1])
			#group_004.Boolean -> boolean_math_001_1.Boolean
			_dssp_sheet_checks.links.new(group_004.outputs[0], boolean_math_001_1.inputs[0])
			#group_input_17.j -> group_005.j
			_dssp_sheet_checks.links.new(group_input_17.outputs[1], group_005.inputs[1])
			#group_002_1.Boolean -> boolean_math_2.Boolean
			_dssp_sheet_checks.links.new(group_002_1.outputs[0], boolean_math_2.inputs[1])
			#group_input_17.j -> group_001_1.j
			_dssp_sheet_checks.links.new(group_input_17.outputs[1], group_001_1.inputs[1])
			#boolean_math_2.Boolean -> boolean_math_002_1.Boolean
			_dssp_sheet_checks.links.new(boolean_math_2.outputs[0], boolean_math_002_1.inputs[0])
			#group_005.Boolean -> boolean_math_001_1.Boolean
			_dssp_sheet_checks.links.new(group_005.outputs[0], boolean_math_001_1.inputs[1])
			#group_input_17.j -> group_004.j
			_dssp_sheet_checks.links.new(group_input_17.outputs[1], group_004.inputs[1])
			#boolean_math_002_1.Boolean -> group_output_17.Boolean
			_dssp_sheet_checks.links.new(boolean_math_002_1.outputs[0], group_output_17.inputs[0])
			#group_input_17.Index -> group_001_1.i
			_dssp_sheet_checks.links.new(group_input_17.outputs[0], group_001_1.inputs[0])
			#group_input_17.Index -> group_002_1.i
			_dssp_sheet_checks.links.new(group_input_17.outputs[0], group_002_1.inputs[0])
			#group_input_17.Index -> group_004.i
			_dssp_sheet_checks.links.new(group_input_17.outputs[0], group_004.inputs[0])
			#group_input_17.Index -> group_005.i
			_dssp_sheet_checks.links.new(group_input_17.outputs[0], group_005.inputs[0])
			#group_input_17.j -> group_output_17.j
			_dssp_sheet_checks.links.new(group_input_17.outputs[1], group_output_17.inputs[1])
			return _dssp_sheet_checks

		_dssp_sheet_checks = _dssp_sheet_checks_node_group()

		#initialize offset_integer node group
		def offset_integer_node_group():
			offset_integer = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Offset Integer")

			offset_integer.color_tag = 'CONVERTER'
			offset_integer.description = ""

			
			#offset_integer interface
			#Socket Value
			value_socket_4 = offset_integer.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			value_socket_4.default_value = 0
			value_socket_4.min_value = -2147483648
			value_socket_4.max_value = 2147483647
			value_socket_4.subtype = 'NONE'
			value_socket_4.attribute_domain = 'POINT'
			
			#Socket Index
			index_socket_2 = offset_integer.interface.new_socket(name = "Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			index_socket_2.default_value = 0
			index_socket_2.min_value = 0
			index_socket_2.max_value = 2147483647
			index_socket_2.subtype = 'NONE'
			index_socket_2.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_5 = offset_integer.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketInt')
			value_socket_5.default_value = 0
			value_socket_5.min_value = -2147483648
			value_socket_5.max_value = 2147483647
			value_socket_5.subtype = 'NONE'
			value_socket_5.attribute_domain = 'POINT'
			value_socket_5.hide_value = True
			
			#Socket Offset
			offset_socket_2 = offset_integer.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket_2.default_value = 0
			offset_socket_2.min_value = -2147483648
			offset_socket_2.max_value = 2147483647
			offset_socket_2.subtype = 'NONE'
			offset_socket_2.attribute_domain = 'POINT'
			
			
			#initialize offset_integer nodes
			#node Group Output
			group_output_18 = offset_integer.nodes.new("NodeGroupOutput")
			group_output_18.name = "Group Output"
			group_output_18.is_active_output = True
			
			#node Group Input
			group_input_18 = offset_integer.nodes.new("NodeGroupInput")
			group_input_18.name = "Group Input"
			
			#node Evaluate at Index
			evaluate_at_index_4 = offset_integer.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_4.name = "Evaluate at Index"
			evaluate_at_index_4.data_type = 'INT'
			evaluate_at_index_4.domain = 'POINT'
			
			#node Math
			math_7 = offset_integer.nodes.new("ShaderNodeMath")
			math_7.name = "Math"
			math_7.operation = 'ADD'
			math_7.use_clamp = False
			
			
			
			
			#Set locations
			group_output_18.location = (190.0, 0.0)
			group_input_18.location = (-412.72760009765625, 0.2001800537109375)
			evaluate_at_index_4.location = (0.0, 0.0)
			math_7.location = (-217.90158081054688, 69.93922424316406)
			
			#Set dimensions
			group_output_18.width, group_output_18.height = 140.0, 100.0
			group_input_18.width, group_input_18.height = 140.0, 100.0
			evaluate_at_index_4.width, evaluate_at_index_4.height = 140.0, 100.0
			math_7.width, math_7.height = 140.0, 100.0
			
			#initialize offset_integer links
			#evaluate_at_index_4.Value -> group_output_18.Value
			offset_integer.links.new(evaluate_at_index_4.outputs[0], group_output_18.inputs[0])
			#group_input_18.Index -> math_7.Value
			offset_integer.links.new(group_input_18.outputs[0], math_7.inputs[0])
			#group_input_18.Offset -> math_7.Value
			offset_integer.links.new(group_input_18.outputs[2], math_7.inputs[1])
			#math_7.Value -> evaluate_at_index_4.Index
			offset_integer.links.new(math_7.outputs[0], evaluate_at_index_4.inputs[0])
			#group_input_18.Value -> evaluate_at_index_4.Value
			offset_integer.links.new(group_input_18.outputs[1], evaluate_at_index_4.inputs[1])
			return offset_integer

		offset_integer = offset_integer_node_group()

		#initialize _mn_topo_calc_sheet node group
		def _mn_topo_calc_sheet_node_group():
			_mn_topo_calc_sheet = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_topo_calc_sheet")

			_mn_topo_calc_sheet.color_tag = 'NONE'
			_mn_topo_calc_sheet.description = ""

			
			#_mn_topo_calc_sheet interface
			#Socket Geometry
			geometry_socket = _mn_topo_calc_sheet.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket.attribute_domain = 'POINT'
			
			#Socket Attribute
			attribute_socket = _mn_topo_calc_sheet.interface.new_socket(name = "Attribute", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			attribute_socket.default_value = False
			attribute_socket.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_1 = _mn_topo_calc_sheet.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_1.attribute_domain = 'POINT'
			
			
			#initialize _mn_topo_calc_sheet nodes
			#node Group Output
			group_output_19 = _mn_topo_calc_sheet.nodes.new("NodeGroupOutput")
			group_output_19.name = "Group Output"
			group_output_19.is_active_output = True
			
			#node Group Input
			group_input_19 = _mn_topo_calc_sheet.nodes.new("NodeGroupInput")
			group_input_19.name = "Group Input"
			
			#node Capture Attribute.002
			capture_attribute_002 = _mn_topo_calc_sheet.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute_002.name = "Capture Attribute.002"
			capture_attribute_002.active_index = 0
			capture_attribute_002.capture_items.clear()
			capture_attribute_002.capture_items.new('FLOAT', "Value")
			capture_attribute_002.capture_items["Value"].data_type = 'BOOLEAN'
			capture_attribute_002.domain = 'POINT'
			
			#node Group.003
			group_003_2 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_003_2.name = "Group.003"
			group_003_2.node_tree = boolean_run_mask
			#Socket_2
			group_003_2.inputs[1].default_value = 0
			#Socket_3
			group_003_2.inputs[2].default_value = 3
			#Socket_6
			group_003_2.inputs[3].default_value = 0
			
			#node Group
			group_5 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_5.name = "Group"
			group_5.mute = True
			group_5.node_tree = boolean_run_fill
			#Socket_2
			group_5.inputs[1].default_value = 1
			
			#node Group.006
			group_006 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_006.name = "Group.006"
			group_006.node_tree = self_sample_proximity
			
			#node Group.007
			group_007 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_007.name = "Group.007"
			group_007.node_tree = mn_topo_backbone
			#Socket_3
			group_007.inputs[0].default_value = 0
			
			#node Capture Attribute
			capture_attribute = _mn_topo_calc_sheet.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute.name = "Capture Attribute"
			capture_attribute.active_index = 3
			capture_attribute.capture_items.clear()
			capture_attribute.capture_items.new('FLOAT', "Value")
			capture_attribute.capture_items["Value"].data_type = 'INT'
			capture_attribute.capture_items.new('FLOAT', "Closest Index")
			capture_attribute.capture_items["Closest Index"].data_type = 'INT'
			capture_attribute.capture_items.new('FLOAT', "Closest Index.001")
			capture_attribute.capture_items["Closest Index.001"].data_type = 'INT'
			capture_attribute.capture_items.new('FLOAT', "Closest Index.002")
			capture_attribute.capture_items["Closest Index.002"].data_type = 'INT'
			capture_attribute.domain = 'POINT'
			
			#node Group.008
			group_008_3 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_008_3.name = "Group.008"
			group_008_3.node_tree = _dssp_sheet_checks
			#Socket_3
			group_008_3.inputs[0].default_value = 0
			
			#node Group.009
			group_009_3 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_009_3.name = "Group.009"
			group_009_3.node_tree = _dssp_sheet_checks
			#Socket_3
			group_009_3.inputs[0].default_value = 0
			
			#node Boolean Math
			boolean_math_3 = _mn_topo_calc_sheet.nodes.new("FunctionNodeBooleanMath")
			boolean_math_3.name = "Boolean Math"
			boolean_math_3.operation = 'OR'
			
			#node Group.010
			group_010_5 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_010_5.name = "Group.010"
			group_010_5.node_tree = _dssp_sheet_checks
			#Socket_3
			group_010_5.inputs[0].default_value = 0
			
			#node Boolean Math.001
			boolean_math_001_2 = _mn_topo_calc_sheet.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_2.name = "Boolean Math.001"
			boolean_math_001_2.operation = 'OR'
			
			#node Group.011
			group_011_4 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_011_4.name = "Group.011"
			group_011_4.node_tree = self_sample_proximity
			
			#node Group.012
			group_012_1 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_012_1.name = "Group.012"
			group_012_1.node_tree = mn_topo_backbone
			#Socket_3
			group_012_1.inputs[0].default_value = 0
			
			#node Vector Math
			vector_math_4 = _mn_topo_calc_sheet.nodes.new("ShaderNodeVectorMath")
			vector_math_4.name = "Vector Math"
			vector_math_4.operation = 'SUBTRACT'
			
			#node Vector Math.001
			vector_math_001_1 = _mn_topo_calc_sheet.nodes.new("ShaderNodeVectorMath")
			vector_math_001_1.name = "Vector Math.001"
			vector_math_001_1.operation = 'ADD'
			
			#node Vector Math.002
			vector_math_002_2 = _mn_topo_calc_sheet.nodes.new("ShaderNodeVectorMath")
			vector_math_002_2.name = "Vector Math.002"
			vector_math_002_2.operation = 'SCALE'
			#Scale
			vector_math_002_2.inputs[3].default_value = 3.0
			
			#node Group.013
			group_013 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_013.name = "Group.013"
			group_013.node_tree = self_sample_proximity
			
			#node Group.014
			group_014 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_014.name = "Group.014"
			group_014.node_tree = self_sample_proximity
			
			#node Vector Math.003
			vector_math_003_1 = _mn_topo_calc_sheet.nodes.new("ShaderNodeVectorMath")
			vector_math_003_1.name = "Vector Math.003"
			vector_math_003_1.operation = 'SUBTRACT'
			
			#node Group.015
			group_015 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_015.name = "Group.015"
			group_015.node_tree = _dssp_sheet_checks
			#Socket_3
			group_015.inputs[0].default_value = 0
			
			#node Boolean Math.002
			boolean_math_002_2 = _mn_topo_calc_sheet.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_2.name = "Boolean Math.002"
			boolean_math_002_2.operation = 'OR'
			
			#node Group.016
			group_016 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_016.name = "Group.016"
			group_016.node_tree = _dssp_sheet_checks
			#Socket_3
			group_016.inputs[0].default_value = 0
			
			#node Boolean Math.003
			boolean_math_003_5 = _mn_topo_calc_sheet.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003_5.name = "Boolean Math.003"
			boolean_math_003_5.operation = 'OR'
			
			#node Group.017
			group_017 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_017.name = "Group.017"
			group_017.node_tree = _dssp_sheet_checks
			#Socket_3
			group_017.inputs[0].default_value = 0
			
			#node Reroute
			reroute_3 = _mn_topo_calc_sheet.nodes.new("NodeReroute")
			reroute_3.name = "Reroute"
			#node Boolean Math.004
			boolean_math_004_1 = _mn_topo_calc_sheet.nodes.new("FunctionNodeBooleanMath")
			boolean_math_004_1.name = "Boolean Math.004"
			boolean_math_004_1.operation = 'OR'
			
			#node Store Named Attribute
			store_named_attribute = _mn_topo_calc_sheet.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute.name = "Store Named Attribute"
			store_named_attribute.data_type = 'INT'
			store_named_attribute.domain = 'POINT'
			#Name
			store_named_attribute.inputs[2].default_value = "tmp_bonded_idx"
			
			#node Store Named Attribute.001
			store_named_attribute_001 = _mn_topo_calc_sheet.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_001.name = "Store Named Attribute.001"
			store_named_attribute_001.data_type = 'INT'
			store_named_attribute_001.domain = 'POINT'
			#Name
			store_named_attribute_001.inputs[2].default_value = "tmp_bonded_idx"
			
			#node Store Named Attribute.002
			store_named_attribute_002 = _mn_topo_calc_sheet.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_002.name = "Store Named Attribute.002"
			store_named_attribute_002.data_type = 'INT'
			store_named_attribute_002.domain = 'POINT'
			#Selection
			store_named_attribute_002.inputs[1].default_value = True
			#Name
			store_named_attribute_002.inputs[2].default_value = "tmp_bonded_idx"
			#Value
			store_named_attribute_002.inputs[3].default_value = -1
			
			#node Store Named Attribute.003
			store_named_attribute_003 = _mn_topo_calc_sheet.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_003.name = "Store Named Attribute.003"
			store_named_attribute_003.data_type = 'INT'
			store_named_attribute_003.domain = 'POINT'
			#Name
			store_named_attribute_003.inputs[2].default_value = "tmp_bonded_idx"
			
			#node Store Named Attribute.004
			store_named_attribute_004 = _mn_topo_calc_sheet.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_004.name = "Store Named Attribute.004"
			store_named_attribute_004.data_type = 'INT'
			store_named_attribute_004.domain = 'POINT'
			#Name
			store_named_attribute_004.inputs[2].default_value = "tmp_bonded_idx"
			
			#node Store Named Attribute.005
			store_named_attribute_005 = _mn_topo_calc_sheet.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_005.name = "Store Named Attribute.005"
			store_named_attribute_005.data_type = 'INT'
			store_named_attribute_005.domain = 'POINT'
			#Name
			store_named_attribute_005.inputs[2].default_value = "tmp_bonded_idx"
			
			#node Store Named Attribute.006
			store_named_attribute_006 = _mn_topo_calc_sheet.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_006.name = "Store Named Attribute.006"
			store_named_attribute_006.data_type = 'INT'
			store_named_attribute_006.domain = 'POINT'
			#Name
			store_named_attribute_006.inputs[2].default_value = "tmp_bonded_idx"
			
			#node Group.001
			group_001_2 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_001_2.name = "Group.001"
			group_001_2.node_tree = offset_integer
			#Socket_1
			group_001_2.inputs[0].default_value = 0
			#Socket_2
			group_001_2.inputs[2].default_value = 1
			
			#node Math
			math_8 = _mn_topo_calc_sheet.nodes.new("ShaderNodeMath")
			math_8.name = "Math"
			math_8.operation = 'ADD'
			math_8.use_clamp = False
			#Value_001
			math_8.inputs[1].default_value = -1.0
			
			#node Group.002
			group_002_2 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_002_2.name = "Group.002"
			group_002_2.node_tree = offset_integer
			#Socket_1
			group_002_2.inputs[0].default_value = 0
			#Socket_2
			group_002_2.inputs[2].default_value = 1
			
			#node Math.001
			math_001_3 = _mn_topo_calc_sheet.nodes.new("ShaderNodeMath")
			math_001_3.name = "Math.001"
			math_001_3.operation = 'ADD'
			math_001_3.use_clamp = False
			#Value_001
			math_001_3.inputs[1].default_value = -1.0
			
			
			
			
			#Set locations
			group_output_19.location = (1360.0, 240.0)
			group_input_19.location = (-1780.0, 80.0)
			capture_attribute_002.location = (960.0, 240.0)
			group_003_2.location = (960.0, -80.0)
			group_5.location = (960.0, 60.0)
			group_006.location = (-1520.0, 20.0)
			group_007.location = (-2100.0, -60.0)
			capture_attribute.location = (-1240.0, 100.0)
			group_008_3.location = (-340.0, 20.0)
			group_009_3.location = (-340.0, -120.0)
			boolean_math_3.location = (40.0, 0.0)
			group_010_5.location = (-340.0, -260.0)
			boolean_math_001_2.location = (40.0, -140.0)
			group_011_4.location = (-1520.0, -320.0)
			group_012_1.location = (-2300.0, -280.0)
			vector_math_4.location = (-2060.0, -600.0)
			vector_math_001_1.location = (-1740.0, -600.0)
			vector_math_002_2.location = (-1900.0, -600.0)
			group_013.location = (-1520.0, -140.0)
			group_014.location = (-1520.0, -480.0)
			vector_math_003_1.location = (-1740.0, -740.0)
			group_015.location = (-340.0, -400.0)
			boolean_math_002_2.location = (40.0, -280.0)
			group_016.location = (-344.5273742675781, -540.385498046875)
			boolean_math_003_5.location = (40.0, -440.0)
			group_017.location = (-340.0, -680.0)
			reroute_3.location = (-740.0, -640.0)
			boolean_math_004_1.location = (40.0, -600.0)
			store_named_attribute.location = (-180.0, 240.0)
			store_named_attribute_001.location = (-20.0, 240.0)
			store_named_attribute_002.location = (-340.0, 240.0)
			store_named_attribute_003.location = (140.0, 240.0)
			store_named_attribute_004.location = (300.0, 240.0)
			store_named_attribute_005.location = (460.0, 240.0)
			store_named_attribute_006.location = (620.0, 240.0)
			group_001_2.location = (-680.0, -540.0)
			math_8.location = (-520.0, -540.0)
			group_002_2.location = (-680.0, -720.0)
			math_001_3.location = (-520.0, -720.0)
			
			#Set dimensions
			group_output_19.width, group_output_19.height = 140.0, 100.0
			group_input_19.width, group_input_19.height = 140.0, 100.0
			capture_attribute_002.width, capture_attribute_002.height = 140.0, 100.0
			group_003_2.width, group_003_2.height = 167.49020385742188, 100.0
			group_5.width, group_5.height = 140.0, 100.0
			group_006.width, group_006.height = 140.0, 100.0
			group_007.width, group_007.height = 140.0, 100.0
			capture_attribute.width, capture_attribute.height = 140.0, 100.0
			group_008_3.width, group_008_3.height = 140.0, 100.0
			group_009_3.width, group_009_3.height = 140.0, 100.0
			boolean_math_3.width, boolean_math_3.height = 140.0, 100.0
			group_010_5.width, group_010_5.height = 140.0, 100.0
			boolean_math_001_2.width, boolean_math_001_2.height = 140.0, 100.0
			group_011_4.width, group_011_4.height = 140.0, 100.0
			group_012_1.width, group_012_1.height = 140.0, 100.0
			vector_math_4.width, vector_math_4.height = 140.0, 100.0
			vector_math_001_1.width, vector_math_001_1.height = 140.0, 100.0
			vector_math_002_2.width, vector_math_002_2.height = 140.0, 100.0
			group_013.width, group_013.height = 140.0, 100.0
			group_014.width, group_014.height = 140.0, 100.0
			vector_math_003_1.width, vector_math_003_1.height = 140.0, 100.0
			group_015.width, group_015.height = 140.0, 100.0
			boolean_math_002_2.width, boolean_math_002_2.height = 140.0, 100.0
			group_016.width, group_016.height = 140.0, 100.0
			boolean_math_003_5.width, boolean_math_003_5.height = 140.0, 100.0
			group_017.width, group_017.height = 140.0, 100.0
			reroute_3.width, reroute_3.height = 16.0, 100.0
			boolean_math_004_1.width, boolean_math_004_1.height = 140.0, 100.0
			store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
			store_named_attribute_001.width, store_named_attribute_001.height = 140.0, 100.0
			store_named_attribute_002.width, store_named_attribute_002.height = 140.0, 100.0
			store_named_attribute_003.width, store_named_attribute_003.height = 140.0, 100.0
			store_named_attribute_004.width, store_named_attribute_004.height = 140.0, 100.0
			store_named_attribute_005.width, store_named_attribute_005.height = 140.0, 100.0
			store_named_attribute_006.width, store_named_attribute_006.height = 140.0, 100.0
			group_001_2.width, group_001_2.height = 140.0, 100.0
			math_8.width, math_8.height = 140.0, 100.0
			group_002_2.width, group_002_2.height = 140.0, 100.0
			math_001_3.width, math_001_3.height = 140.0, 100.0
			
			#initialize _mn_topo_calc_sheet links
			#store_named_attribute_006.Geometry -> capture_attribute_002.Geometry
			_mn_topo_calc_sheet.links.new(store_named_attribute_006.outputs[0], capture_attribute_002.inputs[0])
			#capture_attribute_002.Geometry -> group_output_19.Geometry
			_mn_topo_calc_sheet.links.new(capture_attribute_002.outputs[0], group_output_19.inputs[0])
			#capture_attribute_002.Value -> group_output_19.Attribute
			_mn_topo_calc_sheet.links.new(capture_attribute_002.outputs[1], group_output_19.inputs[1])
			#group_5.Boolean -> capture_attribute_002.Value
			_mn_topo_calc_sheet.links.new(group_5.outputs[0], capture_attribute_002.inputs[1])
			#group_input_19.Geometry -> group_006.Input
			_mn_topo_calc_sheet.links.new(group_input_19.outputs[0], group_006.inputs[0])
			#group_007.NH -> group_006.Target Position
			_mn_topo_calc_sheet.links.new(group_007.outputs[4], group_006.inputs[1])
			#group_007.O -> group_006.Self Position
			_mn_topo_calc_sheet.links.new(group_007.outputs[0], group_006.inputs[2])
			#group_input_19.Geometry -> capture_attribute.Geometry
			_mn_topo_calc_sheet.links.new(group_input_19.outputs[0], capture_attribute.inputs[0])
			#group_006.Closest Index -> capture_attribute.Value
			_mn_topo_calc_sheet.links.new(group_006.outputs[0], capture_attribute.inputs[1])
			#capture_attribute.Value -> group_008_3.j
			_mn_topo_calc_sheet.links.new(capture_attribute.outputs[1], group_008_3.inputs[1])
			#group_008_3.Boolean -> boolean_math_3.Boolean
			_mn_topo_calc_sheet.links.new(group_008_3.outputs[0], boolean_math_3.inputs[0])
			#group_003_2.Boolean -> group_5.Boolean
			_mn_topo_calc_sheet.links.new(group_003_2.outputs[0], group_5.inputs[0])
			#boolean_math_3.Boolean -> boolean_math_001_2.Boolean
			_mn_topo_calc_sheet.links.new(boolean_math_3.outputs[0], boolean_math_001_2.inputs[0])
			#group_input_19.Geometry -> group_011_4.Input
			_mn_topo_calc_sheet.links.new(group_input_19.outputs[0], group_011_4.inputs[0])
			#capture_attribute.Closest Index -> group_009_3.j
			_mn_topo_calc_sheet.links.new(capture_attribute.outputs[2], group_009_3.inputs[1])
			#group_012_1.O -> vector_math_4.Vector
			_mn_topo_calc_sheet.links.new(group_012_1.outputs[0], vector_math_4.inputs[1])
			#group_012_1.CA -> vector_math_001_1.Vector
			_mn_topo_calc_sheet.links.new(group_012_1.outputs[2], vector_math_001_1.inputs[0])
			#vector_math_4.Vector -> vector_math_002_2.Vector
			_mn_topo_calc_sheet.links.new(vector_math_4.outputs[0], vector_math_002_2.inputs[0])
			#vector_math_002_2.Vector -> vector_math_001_1.Vector
			_mn_topo_calc_sheet.links.new(vector_math_002_2.outputs[0], vector_math_001_1.inputs[1])
			#group_012_1.CA -> group_011_4.Target Position
			_mn_topo_calc_sheet.links.new(group_012_1.outputs[2], group_011_4.inputs[1])
			#vector_math_001_1.Vector -> group_011_4.Self Position
			_mn_topo_calc_sheet.links.new(vector_math_001_1.outputs[0], group_011_4.inputs[2])
			#group_012_1.C -> vector_math_4.Vector
			_mn_topo_calc_sheet.links.new(group_012_1.outputs[1], vector_math_4.inputs[0])
			#group_input_19.Geometry -> group_013.Input
			_mn_topo_calc_sheet.links.new(group_input_19.outputs[0], group_013.inputs[0])
			#capture_attribute.Closest Index.001 -> group_010_5.j
			_mn_topo_calc_sheet.links.new(capture_attribute.outputs[3], group_010_5.inputs[1])
			#group_012_1.NH -> group_013.Self Position
			_mn_topo_calc_sheet.links.new(group_012_1.outputs[4], group_013.inputs[2])
			#group_012_1.O -> group_013.Target Position
			_mn_topo_calc_sheet.links.new(group_012_1.outputs[0], group_013.inputs[1])
			#group_010_5.Boolean -> boolean_math_001_2.Boolean
			_mn_topo_calc_sheet.links.new(group_010_5.outputs[0], boolean_math_001_2.inputs[1])
			#group_009_3.Boolean -> boolean_math_3.Boolean
			_mn_topo_calc_sheet.links.new(group_009_3.outputs[0], boolean_math_3.inputs[1])
			#group_input_19.Geometry -> group_014.Input
			_mn_topo_calc_sheet.links.new(group_input_19.outputs[0], group_014.inputs[0])
			#group_012_1.CA -> group_014.Target Position
			_mn_topo_calc_sheet.links.new(group_012_1.outputs[2], group_014.inputs[1])
			#group_012_1.CA -> vector_math_003_1.Vector
			_mn_topo_calc_sheet.links.new(group_012_1.outputs[2], vector_math_003_1.inputs[0])
			#vector_math_002_2.Vector -> vector_math_003_1.Vector
			_mn_topo_calc_sheet.links.new(vector_math_002_2.outputs[0], vector_math_003_1.inputs[1])
			#vector_math_003_1.Vector -> group_014.Self Position
			_mn_topo_calc_sheet.links.new(vector_math_003_1.outputs[0], group_014.inputs[2])
			#capture_attribute.Closest Index.002 -> group_015.j
			_mn_topo_calc_sheet.links.new(capture_attribute.outputs[4], group_015.inputs[1])
			#boolean_math_001_2.Boolean -> boolean_math_002_2.Boolean
			_mn_topo_calc_sheet.links.new(boolean_math_001_2.outputs[0], boolean_math_002_2.inputs[0])
			#group_015.Boolean -> boolean_math_002_2.Boolean
			_mn_topo_calc_sheet.links.new(group_015.outputs[0], boolean_math_002_2.inputs[1])
			#boolean_math_002_2.Boolean -> boolean_math_003_5.Boolean
			_mn_topo_calc_sheet.links.new(boolean_math_002_2.outputs[0], boolean_math_003_5.inputs[0])
			#group_016.Boolean -> boolean_math_003_5.Boolean
			_mn_topo_calc_sheet.links.new(group_016.outputs[0], boolean_math_003_5.inputs[1])
			#capture_attribute.Value -> reroute_3.Input
			_mn_topo_calc_sheet.links.new(capture_attribute.outputs[1], reroute_3.inputs[0])
			#boolean_math_003_5.Boolean -> boolean_math_004_1.Boolean
			_mn_topo_calc_sheet.links.new(boolean_math_003_5.outputs[0], boolean_math_004_1.inputs[0])
			#group_017.Boolean -> boolean_math_004_1.Boolean
			_mn_topo_calc_sheet.links.new(group_017.outputs[0], boolean_math_004_1.inputs[1])
			#boolean_math_004_1.Boolean -> group_003_2.Boolean
			_mn_topo_calc_sheet.links.new(boolean_math_004_1.outputs[0], group_003_2.inputs[0])
			#store_named_attribute_002.Geometry -> store_named_attribute.Geometry
			_mn_topo_calc_sheet.links.new(store_named_attribute_002.outputs[0], store_named_attribute.inputs[0])
			#group_008_3.j -> store_named_attribute.Value
			_mn_topo_calc_sheet.links.new(group_008_3.outputs[1], store_named_attribute.inputs[3])
			#group_008_3.Boolean -> store_named_attribute.Selection
			_mn_topo_calc_sheet.links.new(group_008_3.outputs[0], store_named_attribute.inputs[1])
			#store_named_attribute.Geometry -> store_named_attribute_001.Geometry
			_mn_topo_calc_sheet.links.new(store_named_attribute.outputs[0], store_named_attribute_001.inputs[0])
			#group_009_3.Boolean -> store_named_attribute_001.Selection
			_mn_topo_calc_sheet.links.new(group_009_3.outputs[0], store_named_attribute_001.inputs[1])
			#group_009_3.j -> store_named_attribute_001.Value
			_mn_topo_calc_sheet.links.new(group_009_3.outputs[1], store_named_attribute_001.inputs[3])
			#capture_attribute.Geometry -> store_named_attribute_002.Geometry
			_mn_topo_calc_sheet.links.new(capture_attribute.outputs[0], store_named_attribute_002.inputs[0])
			#store_named_attribute_001.Geometry -> store_named_attribute_003.Geometry
			_mn_topo_calc_sheet.links.new(store_named_attribute_001.outputs[0], store_named_attribute_003.inputs[0])
			#group_010_5.Boolean -> store_named_attribute_003.Selection
			_mn_topo_calc_sheet.links.new(group_010_5.outputs[0], store_named_attribute_003.inputs[1])
			#group_010_5.j -> store_named_attribute_003.Value
			_mn_topo_calc_sheet.links.new(group_010_5.outputs[1], store_named_attribute_003.inputs[3])
			#store_named_attribute_003.Geometry -> store_named_attribute_004.Geometry
			_mn_topo_calc_sheet.links.new(store_named_attribute_003.outputs[0], store_named_attribute_004.inputs[0])
			#group_015.Boolean -> store_named_attribute_004.Selection
			_mn_topo_calc_sheet.links.new(group_015.outputs[0], store_named_attribute_004.inputs[1])
			#group_015.j -> store_named_attribute_004.Value
			_mn_topo_calc_sheet.links.new(group_015.outputs[1], store_named_attribute_004.inputs[3])
			#store_named_attribute_004.Geometry -> store_named_attribute_005.Geometry
			_mn_topo_calc_sheet.links.new(store_named_attribute_004.outputs[0], store_named_attribute_005.inputs[0])
			#group_016.Boolean -> store_named_attribute_005.Selection
			_mn_topo_calc_sheet.links.new(group_016.outputs[0], store_named_attribute_005.inputs[1])
			#group_016.j -> store_named_attribute_005.Value
			_mn_topo_calc_sheet.links.new(group_016.outputs[1], store_named_attribute_005.inputs[3])
			#store_named_attribute_005.Geometry -> store_named_attribute_006.Geometry
			_mn_topo_calc_sheet.links.new(store_named_attribute_005.outputs[0], store_named_attribute_006.inputs[0])
			#group_017.Boolean -> store_named_attribute_006.Selection
			_mn_topo_calc_sheet.links.new(group_017.outputs[0], store_named_attribute_006.inputs[1])
			#group_017.j -> store_named_attribute_006.Value
			_mn_topo_calc_sheet.links.new(group_017.outputs[1], store_named_attribute_006.inputs[3])
			#group_001_2.Value -> math_8.Value
			_mn_topo_calc_sheet.links.new(group_001_2.outputs[0], math_8.inputs[0])
			#reroute_3.Output -> group_001_2.Value
			_mn_topo_calc_sheet.links.new(reroute_3.outputs[0], group_001_2.inputs[1])
			#math_8.Value -> group_016.j
			_mn_topo_calc_sheet.links.new(math_8.outputs[0], group_016.inputs[1])
			#group_002_2.Value -> math_001_3.Value
			_mn_topo_calc_sheet.links.new(group_002_2.outputs[0], math_001_3.inputs[0])
			#reroute_3.Output -> group_002_2.Value
			_mn_topo_calc_sheet.links.new(reroute_3.outputs[0], group_002_2.inputs[1])
			#math_001_3.Value -> group_017.j
			_mn_topo_calc_sheet.links.new(math_001_3.outputs[0], group_017.inputs[1])
			#group_013.Closest Index -> capture_attribute.Closest Index
			_mn_topo_calc_sheet.links.new(group_013.outputs[0], capture_attribute.inputs[2])
			#group_011_4.Closest Index -> capture_attribute.Closest Index.001
			_mn_topo_calc_sheet.links.new(group_011_4.outputs[0], capture_attribute.inputs[3])
			#group_014.Closest Index -> capture_attribute.Closest Index.002
			_mn_topo_calc_sheet.links.new(group_014.outputs[0], capture_attribute.inputs[4])
			return _mn_topo_calc_sheet

		_mn_topo_calc_sheet = _mn_topo_calc_sheet_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".MN_topo_calc_sheet", type = 'NODES')
		mod.node_group = _mn_topo_calc_sheet
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_MN_topo_calc_sheet.bl_idname)
			
def register():
	bpy.utils.register_class(_MN_topo_calc_sheet)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_MN_topo_calc_sheet)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
