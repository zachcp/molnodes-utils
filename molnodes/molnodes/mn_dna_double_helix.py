bl_info = {
	"name" : "MN_dna_double_helix",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class MN_dna_double_helix(bpy.types.Operator):
	bl_idname = "node.mn_dna_double_helix"
	bl_label = "MN_dna_double_helix"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize mn_utils_curve_resample node group
		def mn_utils_curve_resample_node_group():
			mn_utils_curve_resample = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "MN_utils_curve_resample")

			mn_utils_curve_resample.color_tag = 'NONE'
			mn_utils_curve_resample.description = ""

			mn_utils_curve_resample.is_modifier = True
			
			#mn_utils_curve_resample interface
			#Socket Geometry
			geometry_socket = mn_utils_curve_resample.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket.attribute_domain = 'POINT'
			
			#Socket Position
			position_socket = mn_utils_curve_resample.interface.new_socket(name = "Position", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			position_socket.subtype = 'NONE'
			position_socket.default_value = (0.0, 0.0, 0.0)
			position_socket.min_value = -3.4028234663852886e+38
			position_socket.max_value = 3.4028234663852886e+38
			position_socket.attribute_domain = 'POINT'
			
			#Socket Tangent
			tangent_socket = mn_utils_curve_resample.interface.new_socket(name = "Tangent", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			tangent_socket.subtype = 'NONE'
			tangent_socket.default_value = (0.0, 0.0, 0.0)
			tangent_socket.min_value = -3.4028234663852886e+38
			tangent_socket.max_value = 3.4028234663852886e+38
			tangent_socket.attribute_domain = 'POINT'
			
			#Socket Normal
			normal_socket = mn_utils_curve_resample.interface.new_socket(name = "Normal", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			normal_socket.subtype = 'NONE'
			normal_socket.default_value = (0.0, 0.0, 0.0)
			normal_socket.min_value = -3.4028234663852886e+38
			normal_socket.max_value = 3.4028234663852886e+38
			normal_socket.attribute_domain = 'POINT'
			
			#Socket Field Float
			field_float_socket = mn_utils_curve_resample.interface.new_socket(name = "Field Float", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			field_float_socket.subtype = 'NONE'
			field_float_socket.default_value = 0.0
			field_float_socket.min_value = -3.4028234663852886e+38
			field_float_socket.max_value = 3.4028234663852886e+38
			field_float_socket.attribute_domain = 'POINT'
			
			#Socket Field Int
			field_int_socket = mn_utils_curve_resample.interface.new_socket(name = "Field Int", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			field_int_socket.subtype = 'NONE'
			field_int_socket.default_value = 0
			field_int_socket.min_value = -2147483648
			field_int_socket.max_value = 2147483647
			field_int_socket.attribute_domain = 'POINT'
			
			#Socket Field Vec
			field_vec_socket = mn_utils_curve_resample.interface.new_socket(name = "Field Vec", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			field_vec_socket.subtype = 'NONE'
			field_vec_socket.default_value = (0.0, 0.0, 0.0)
			field_vec_socket.min_value = -3.4028234663852886e+38
			field_vec_socket.max_value = 3.4028234663852886e+38
			field_vec_socket.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_1 = mn_utils_curve_resample.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_1.attribute_domain = 'POINT'
			
			#Socket Offset
			offset_socket = mn_utils_curve_resample.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketFloat')
			offset_socket.subtype = 'NONE'
			offset_socket.default_value = 2.299999952316284
			offset_socket.min_value = -10000.0
			offset_socket.max_value = 10000.0
			offset_socket.attribute_domain = 'POINT'
			
			#Socket Length
			length_socket = mn_utils_curve_resample.interface.new_socket(name = "Length", in_out='INPUT', socket_type = 'NodeSocketFloat')
			length_socket.subtype = 'DISTANCE'
			length_socket.default_value = 0.36000001430511475
			length_socket.min_value = 0.009999999776482582
			length_socket.max_value = 3.4028234663852886e+38
			length_socket.attribute_domain = 'POINT'
			
			#Socket Field Float
			field_float_socket_1 = mn_utils_curve_resample.interface.new_socket(name = "Field Float", in_out='INPUT', socket_type = 'NodeSocketFloat')
			field_float_socket_1.subtype = 'NONE'
			field_float_socket_1.default_value = 0.0
			field_float_socket_1.min_value = -3.4028234663852886e+38
			field_float_socket_1.max_value = 3.4028234663852886e+38
			field_float_socket_1.attribute_domain = 'POINT'
			field_float_socket_1.hide_value = True
			
			#Socket Field Int
			field_int_socket_1 = mn_utils_curve_resample.interface.new_socket(name = "Field Int", in_out='INPUT', socket_type = 'NodeSocketInt')
			field_int_socket_1.subtype = 'NONE'
			field_int_socket_1.default_value = 0
			field_int_socket_1.min_value = -2147483648
			field_int_socket_1.max_value = 2147483647
			field_int_socket_1.attribute_domain = 'POINT'
			field_int_socket_1.hide_value = True
			
			#Socket Field Vec
			field_vec_socket_1 = mn_utils_curve_resample.interface.new_socket(name = "Field Vec", in_out='INPUT', socket_type = 'NodeSocketVector')
			field_vec_socket_1.subtype = 'NONE'
			field_vec_socket_1.default_value = (0.0, 0.0, 0.0)
			field_vec_socket_1.min_value = -3.4028234663852886e+38
			field_vec_socket_1.max_value = 3.4028234663852886e+38
			field_vec_socket_1.attribute_domain = 'POINT'
			field_vec_socket_1.hide_value = True
			
			
			#initialize mn_utils_curve_resample nodes
			#node Sample Curve.001
			sample_curve_001 = mn_utils_curve_resample.nodes.new("GeometryNodeSampleCurve")
			sample_curve_001.name = "Sample Curve.001"
			sample_curve_001.data_type = 'INT'
			sample_curve_001.mode = 'LENGTH'
			sample_curve_001.use_all_curves = False
			
			#node Reroute.001
			reroute_001 = mn_utils_curve_resample.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			#node Sample Curve.002
			sample_curve_002 = mn_utils_curve_resample.nodes.new("GeometryNodeSampleCurve")
			sample_curve_002.name = "Sample Curve.002"
			sample_curve_002.data_type = 'FLOAT_VECTOR'
			sample_curve_002.mode = 'LENGTH'
			sample_curve_002.use_all_curves = False
			
			#node Index
			index = mn_utils_curve_resample.nodes.new("GeometryNodeInputIndex")
			index.name = "Index"
			
			#node Capture Attribute
			capture_attribute = mn_utils_curve_resample.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute.name = "Capture Attribute"
			capture_attribute.active_index = 0
			capture_attribute.capture_items.clear()
			capture_attribute.capture_items.new('FLOAT', "Value")
			capture_attribute.capture_items["Value"].data_type = 'INT'
			capture_attribute.domain = 'CURVE'
			
			#node Reroute.002
			reroute_002 = mn_utils_curve_resample.nodes.new("NodeReroute")
			reroute_002.name = "Reroute.002"
			#node Resample Curve
			resample_curve = mn_utils_curve_resample.nodes.new("GeometryNodeResampleCurve")
			resample_curve.name = "Resample Curve"
			resample_curve.mode = 'LENGTH'
			#Selection
			resample_curve.inputs[1].default_value = True
			
			#node Group Output
			group_output = mn_utils_curve_resample.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Set Position
			set_position = mn_utils_curve_resample.nodes.new("GeometryNodeSetPosition")
			set_position.name = "Set Position"
			#Selection
			set_position.inputs[1].default_value = True
			#Offset
			set_position.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Reroute
			reroute = mn_utils_curve_resample.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Resample Curve.001
			resample_curve_001 = mn_utils_curve_resample.nodes.new("GeometryNodeResampleCurve")
			resample_curve_001.name = "Resample Curve.001"
			resample_curve_001.mode = 'COUNT'
			#Selection
			resample_curve_001.inputs[1].default_value = True
			
			#node Sample Curve
			sample_curve = mn_utils_curve_resample.nodes.new("GeometryNodeSampleCurve")
			sample_curve.name = "Sample Curve"
			sample_curve.data_type = 'FLOAT'
			sample_curve.mode = 'LENGTH'
			sample_curve.use_all_curves = False
			
			#node Group Input
			group_input = mn_utils_curve_resample.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Reroute.003
			reroute_003 = mn_utils_curve_resample.nodes.new("NodeReroute")
			reroute_003.name = "Reroute.003"
			#node Spline Length.001
			spline_length_001 = mn_utils_curve_resample.nodes.new("GeometryNodeSplineLength")
			spline_length_001.name = "Spline Length.001"
			
			#node Math
			math = mn_utils_curve_resample.nodes.new("ShaderNodeMath")
			math.label = "x - 1"
			math.name = "Math"
			math.hide = True
			math.operation = 'SUBTRACT'
			math.use_clamp = False
			#Value_001
			math.inputs[1].default_value = 1.0
			
			#node Math.001
			math_001 = mn_utils_curve_resample.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.operation = 'WRAP'
			math_001.use_clamp = False
			#Value_002
			math_001.inputs[2].default_value = 0.0
			
			#node Spline Length
			spline_length = mn_utils_curve_resample.nodes.new("GeometryNodeSplineLength")
			spline_length.name = "Spline Length"
			
			#node Math.002
			math_002 = mn_utils_curve_resample.nodes.new("ShaderNodeMath")
			math_002.name = "Math.002"
			math_002.operation = 'ADD'
			math_002.use_clamp = False
			
			#node Compare
			compare = mn_utils_curve_resample.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'FLOAT'
			compare.mode = 'ELEMENT'
			compare.operation = 'EQUAL'
			#B
			compare.inputs[1].default_value = 0.0
			#Epsilon
			compare.inputs[12].default_value = 0.0010000000474974513
			
			#node Switch
			switch = mn_utils_curve_resample.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'FLOAT'
			
			#node Accumulate Field
			accumulate_field = mn_utils_curve_resample.nodes.new("GeometryNodeAccumulateField")
			accumulate_field.name = "Accumulate Field"
			accumulate_field.data_type = 'FLOAT'
			accumulate_field.domain = 'POINT'
			
			
			
			
			#Set locations
			sample_curve_001.location = (280.0, -160.0)
			reroute_001.location = (170.41610717773438, 56.029422760009766)
			sample_curve_002.location = (280.0, -460.0)
			index.location = (-468.85321044921875, -335.7737121582031)
			capture_attribute.location = (-466.8502197265625, -142.71517944335938)
			reroute_002.location = (-754.80029296875, -226.68231201171875)
			resample_curve.location = (-641.0833129882812, -111.3865966796875)
			group_output.location = (1082.3330078125, -91.4212875366211)
			set_position.location = (800.173095703125, -100.55831909179688)
			reroute.location = (75.4967041015625, -163.95921325683594)
			resample_curve_001.location = (526.7703247070312, -109.56268310546875)
			sample_curve.location = (260.0, 220.0)
			group_input.location = (-1054.9755859375, -86.68230438232422)
			reroute_003.location = (-498.3427429199219, 182.15419006347656)
			spline_length_001.location = (520.0, -320.0)
			math.location = (540.0, -280.0)
			math_001.location = (-60.0, 640.0)
			spline_length.location = (-60.0, 720.0)
			math_002.location = (-280.0, 620.0)
			compare.location = (-316.9455871582031, 279.42132568359375)
			switch.location = (-40.0, 280.0)
			accumulate_field.location = (-523.4389038085938, 432.5602722167969)
			
			#Set dimensions
			sample_curve_001.width, sample_curve_001.height = 140.0, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			sample_curve_002.width, sample_curve_002.height = 140.0, 100.0
			index.width, index.height = 140.0, 100.0
			capture_attribute.width, capture_attribute.height = 140.0, 100.0
			reroute_002.width, reroute_002.height = 16.0, 100.0
			resample_curve.width, resample_curve.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			set_position.width, set_position.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			resample_curve_001.width, resample_curve_001.height = 140.0, 100.0
			sample_curve.width, sample_curve.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			reroute_003.width, reroute_003.height = 16.0, 100.0
			spline_length_001.width, spline_length_001.height = 151.61087036132812, 100.0
			math.width, math.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			spline_length.width, spline_length.height = 140.0, 100.0
			math_002.width, math_002.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			accumulate_field.width, accumulate_field.height = 140.0, 100.0
			
			#initialize mn_utils_curve_resample links
			#group_input.Geometry -> resample_curve.Curve
			mn_utils_curve_resample.links.new(group_input.outputs[0], resample_curve.inputs[0])
			#set_position.Geometry -> group_output.Geometry
			mn_utils_curve_resample.links.new(set_position.outputs[0], group_output.inputs[0])
			#group_input.Length -> reroute_002.Input
			mn_utils_curve_resample.links.new(group_input.outputs[2], reroute_002.inputs[0])
			#reroute.Output -> sample_curve.Curves
			mn_utils_curve_resample.links.new(reroute.outputs[0], sample_curve.inputs[0])
			#reroute_001.Output -> sample_curve.Length
			mn_utils_curve_resample.links.new(reroute_001.outputs[0], sample_curve.inputs[3])
			#sample_curve.Position -> set_position.Position
			mn_utils_curve_resample.links.new(sample_curve.outputs[1], set_position.inputs[2])
			#resample_curve.Curve -> capture_attribute.Geometry
			mn_utils_curve_resample.links.new(resample_curve.outputs[0], capture_attribute.inputs[0])
			#index.Index -> capture_attribute.Value
			mn_utils_curve_resample.links.new(index.outputs[0], capture_attribute.inputs[1])
			#capture_attribute.Geometry -> reroute.Input
			mn_utils_curve_resample.links.new(capture_attribute.outputs[0], reroute.inputs[0])
			#capture_attribute.Value -> sample_curve.Curve Index
			mn_utils_curve_resample.links.new(capture_attribute.outputs[1], sample_curve.inputs[4])
			#capture_attribute.Value -> accumulate_field.Group ID
			mn_utils_curve_resample.links.new(capture_attribute.outputs[1], accumulate_field.inputs[1])
			#reroute_002.Output -> resample_curve.Length
			mn_utils_curve_resample.links.new(reroute_002.outputs[0], resample_curve.inputs[3])
			#reroute_002.Output -> accumulate_field.Value
			mn_utils_curve_resample.links.new(reroute_002.outputs[0], accumulate_field.inputs[0])
			#reroute.Output -> sample_curve_001.Curves
			mn_utils_curve_resample.links.new(reroute.outputs[0], sample_curve_001.inputs[0])
			#reroute_001.Output -> sample_curve_001.Length
			mn_utils_curve_resample.links.new(reroute_001.outputs[0], sample_curve_001.inputs[3])
			#capture_attribute.Value -> sample_curve_001.Curve Index
			mn_utils_curve_resample.links.new(capture_attribute.outputs[1], sample_curve_001.inputs[4])
			#sample_curve.Position -> group_output.Position
			mn_utils_curve_resample.links.new(sample_curve.outputs[1], group_output.inputs[1])
			#sample_curve.Tangent -> group_output.Tangent
			mn_utils_curve_resample.links.new(sample_curve.outputs[2], group_output.inputs[2])
			#sample_curve.Normal -> group_output.Normal
			mn_utils_curve_resample.links.new(sample_curve.outputs[3], group_output.inputs[3])
			#sample_curve.Value -> group_output.Field Float
			mn_utils_curve_resample.links.new(sample_curve.outputs[0], group_output.inputs[4])
			#group_input.Field Float -> sample_curve.Value
			mn_utils_curve_resample.links.new(group_input.outputs[3], sample_curve.inputs[1])
			#sample_curve_001.Value -> group_output.Field Int
			mn_utils_curve_resample.links.new(sample_curve_001.outputs[0], group_output.inputs[5])
			#group_input.Field Int -> sample_curve_001.Value
			mn_utils_curve_resample.links.new(group_input.outputs[4], sample_curve_001.inputs[1])
			#reroute.Output -> sample_curve_002.Curves
			mn_utils_curve_resample.links.new(reroute.outputs[0], sample_curve_002.inputs[0])
			#reroute_001.Output -> sample_curve_002.Length
			mn_utils_curve_resample.links.new(reroute_001.outputs[0], sample_curve_002.inputs[3])
			#capture_attribute.Value -> sample_curve_002.Curve Index
			mn_utils_curve_resample.links.new(capture_attribute.outputs[1], sample_curve_002.inputs[4])
			#sample_curve_002.Value -> group_output.Field Vec
			mn_utils_curve_resample.links.new(sample_curve_002.outputs[0], group_output.inputs[6])
			#group_input.Field Vec -> sample_curve_002.Value
			mn_utils_curve_resample.links.new(group_input.outputs[5], sample_curve_002.inputs[1])
			#reroute.Output -> resample_curve_001.Curve
			mn_utils_curve_resample.links.new(reroute.outputs[0], resample_curve_001.inputs[0])
			#resample_curve_001.Curve -> set_position.Geometry
			mn_utils_curve_resample.links.new(resample_curve_001.outputs[0], set_position.inputs[0])
			#math.Value -> resample_curve_001.Count
			mn_utils_curve_resample.links.new(math.outputs[0], resample_curve_001.inputs[2])
			#math_002.Value -> math_001.Value
			mn_utils_curve_resample.links.new(math_002.outputs[0], math_001.inputs[0])
			#spline_length.Length -> math_001.Value
			mn_utils_curve_resample.links.new(spline_length.outputs[0], math_001.inputs[1])
			#accumulate_field.Trailing -> math_002.Value
			mn_utils_curve_resample.links.new(accumulate_field.outputs[1], math_002.inputs[0])
			#reroute_003.Output -> math_002.Value
			mn_utils_curve_resample.links.new(reroute_003.outputs[0], math_002.inputs[1])
			#compare.Result -> switch.Switch
			mn_utils_curve_resample.links.new(compare.outputs[0], switch.inputs[0])
			#group_input.Offset -> reroute_003.Input
			mn_utils_curve_resample.links.new(group_input.outputs[1], reroute_003.inputs[0])
			#reroute_003.Output -> compare.A
			mn_utils_curve_resample.links.new(reroute_003.outputs[0], compare.inputs[0])
			#spline_length_001.Point Count -> math.Value
			mn_utils_curve_resample.links.new(spline_length_001.outputs[1], math.inputs[0])
			#switch.Output -> reroute_001.Input
			mn_utils_curve_resample.links.new(switch.outputs[0], reroute_001.inputs[0])
			#math_001.Value -> switch.False
			mn_utils_curve_resample.links.new(math_001.outputs[0], switch.inputs[1])
			#accumulate_field.Trailing -> switch.True
			mn_utils_curve_resample.links.new(accumulate_field.outputs[1], switch.inputs[2])
			return mn_utils_curve_resample

		mn_utils_curve_resample = mn_utils_curve_resample_node_group()

		#initialize mn_utils_helix node group
		def mn_utils_helix_node_group():
			mn_utils_helix = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "MN_utils_helix")

			mn_utils_helix.color_tag = 'NONE'
			mn_utils_helix.description = ""

			mn_utils_helix.is_modifier = True
			
			#mn_utils_helix interface
			#Socket Curve
			curve_socket = mn_utils_helix.interface.new_socket(name = "Curve", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			curve_socket.attribute_domain = 'POINT'
			
			#Socket pos_old - pos_new
			pos_old___pos_new_socket = mn_utils_helix.interface.new_socket(name = "pos_old - pos_new", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			pos_old___pos_new_socket.subtype = 'NONE'
			pos_old___pos_new_socket.default_value = (0.0, 0.0, 0.0)
			pos_old___pos_new_socket.min_value = -3.4028234663852886e+38
			pos_old___pos_new_socket.max_value = 3.4028234663852886e+38
			pos_old___pos_new_socket.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_2 = mn_utils_helix.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_2.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket = mn_utils_helix.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket.subtype = 'NONE'
			value_socket.default_value = 0.5711986422538757
			value_socket.min_value = -3.4028234663852886e+38
			value_socket.max_value = 3.4028234663852886e+38
			value_socket.attribute_domain = 'POINT'
			
			#Socket Scale
			scale_socket = mn_utils_helix.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
			scale_socket.subtype = 'NONE'
			scale_socket.default_value = 0.10000000149011612
			scale_socket.min_value = -10000.0
			scale_socket.max_value = 10000.0
			scale_socket.attribute_domain = 'POINT'
			
			#Socket Rotation
			rotation_socket = mn_utils_helix.interface.new_socket(name = "Rotation", in_out='INPUT', socket_type = 'NodeSocketFloat')
			rotation_socket.subtype = 'NONE'
			rotation_socket.default_value = 0.5
			rotation_socket.min_value = -10000.0
			rotation_socket.max_value = 10000.0
			rotation_socket.attribute_domain = 'POINT'
			
			#Socket Angle
			angle_socket = mn_utils_helix.interface.new_socket(name = "Angle", in_out='INPUT', socket_type = 'NodeSocketFloat')
			angle_socket.subtype = 'ANGLE'
			angle_socket.default_value = -0.8028512597084045
			angle_socket.min_value = -3.4028234663852886e+38
			angle_socket.max_value = 3.4028234663852886e+38
			angle_socket.attribute_domain = 'POINT'
			
			#Socket Unwind
			unwind_socket = mn_utils_helix.interface.new_socket(name = "Unwind", in_out='INPUT', socket_type = 'NodeSocketFloat')
			unwind_socket.subtype = 'NONE'
			unwind_socket.default_value = 1.0
			unwind_socket.min_value = -10000.0
			unwind_socket.max_value = 10000.0
			unwind_socket.attribute_domain = 'POINT'
			
			#Socket Offset
			offset_socket_1 = mn_utils_helix.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketFloat')
			offset_socket_1.subtype = 'NONE'
			offset_socket_1.default_value = 0.009999999776482582
			offset_socket_1.min_value = -10000.0
			offset_socket_1.max_value = 10000.0
			offset_socket_1.attribute_domain = 'POINT'
			
			#Socket Length
			length_socket_1 = mn_utils_helix.interface.new_socket(name = "Length", in_out='INPUT', socket_type = 'NodeSocketFloat')
			length_socket_1.subtype = 'DISTANCE'
			length_socket_1.default_value = 0.04000002145767212
			length_socket_1.min_value = 0.009999999776482582
			length_socket_1.max_value = 3.4028234663852886e+38
			length_socket_1.attribute_domain = 'POINT'
			
			#Socket Offset
			offset_socket_2 = mn_utils_helix.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket_2.subtype = 'NONE'
			offset_socket_2.default_value = 2
			offset_socket_2.min_value = -2147483648
			offset_socket_2.max_value = 2147483647
			offset_socket_2.attribute_domain = 'POINT'
			
			
			#initialize mn_utils_helix nodes
			#node Index
			index_1 = mn_utils_helix.nodes.new("GeometryNodeInputIndex")
			index_1.name = "Index"
			
			#node Capture Attribute
			capture_attribute_1 = mn_utils_helix.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute_1.name = "Capture Attribute"
			capture_attribute_1.active_index = 0
			capture_attribute_1.capture_items.clear()
			capture_attribute_1.capture_items.new('FLOAT', "Value")
			capture_attribute_1.capture_items["Value"].data_type = 'INT'
			capture_attribute_1.domain = 'CURVE'
			
			#node Group Output
			group_output_1 = mn_utils_helix.nodes.new("NodeGroupOutput")
			group_output_1.name = "Group Output"
			group_output_1.is_active_output = True
			
			#node Store Named Attribute
			store_named_attribute = mn_utils_helix.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute.name = "Store Named Attribute"
			store_named_attribute.data_type = 'FLOAT_VECTOR'
			store_named_attribute.domain = 'POINT'
			#Selection
			store_named_attribute.inputs[1].default_value = True
			#Name
			store_named_attribute.inputs[2].default_value = "rot"
			
			#node Vector Math.003
			vector_math_003 = mn_utils_helix.nodes.new("ShaderNodeVectorMath")
			vector_math_003.name = "Vector Math.003"
			vector_math_003.operation = 'SUBTRACT'
			
			#node Align Euler to Vector.002
			align_euler_to_vector_002 = mn_utils_helix.nodes.new("FunctionNodeAlignEulerToVector")
			align_euler_to_vector_002.name = "Align Euler to Vector.002"
			align_euler_to_vector_002.axis = 'X'
			align_euler_to_vector_002.pivot_axis = 'AUTO'
			#Rotation
			align_euler_to_vector_002.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Factor
			align_euler_to_vector_002.inputs[1].default_value = 1.0
			
			#node Align Euler to Vector.001
			align_euler_to_vector_001 = mn_utils_helix.nodes.new("FunctionNodeAlignEulerToVector")
			align_euler_to_vector_001.name = "Align Euler to Vector.001"
			align_euler_to_vector_001.axis = 'Z'
			align_euler_to_vector_001.pivot_axis = 'AUTO'
			#Factor
			align_euler_to_vector_001.inputs[1].default_value = 1.0
			
			#node Position.001
			position_001 = mn_utils_helix.nodes.new("GeometryNodeInputPosition")
			position_001.name = "Position.001"
			
			#node Set Curve Tilt
			set_curve_tilt = mn_utils_helix.nodes.new("GeometryNodeSetCurveTilt")
			set_curve_tilt.name = "Set Curve Tilt"
			#Selection
			set_curve_tilt.inputs[1].default_value = True
			
			#node Capture Attribute.001
			capture_attribute_001 = mn_utils_helix.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute_001.name = "Capture Attribute.001"
			capture_attribute_001.active_index = 0
			capture_attribute_001.capture_items.clear()
			capture_attribute_001.capture_items.new('FLOAT', "Value")
			capture_attribute_001.capture_items["Value"].data_type = 'FLOAT_VECTOR'
			capture_attribute_001.domain = 'POINT'
			
			#node Capture Attribute.003
			capture_attribute_003 = mn_utils_helix.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute_003.name = "Capture Attribute.003"
			capture_attribute_003.active_index = 0
			capture_attribute_003.capture_items.clear()
			capture_attribute_003.capture_items.new('FLOAT', "Value")
			capture_attribute_003.capture_items["Value"].data_type = 'FLOAT_VECTOR'
			capture_attribute_003.domain = 'POINT'
			
			#node Vector Math.001
			vector_math_001 = mn_utils_helix.nodes.new("ShaderNodeVectorMath")
			vector_math_001.name = "Vector Math.001"
			vector_math_001.operation = 'SCALE'
			
			#node Curve Tangent
			curve_tangent = mn_utils_helix.nodes.new("GeometryNodeInputTangent")
			curve_tangent.name = "Curve Tangent"
			
			#node Capture Attribute.002
			capture_attribute_002 = mn_utils_helix.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute_002.name = "Capture Attribute.002"
			capture_attribute_002.active_index = 0
			capture_attribute_002.capture_items.clear()
			capture_attribute_002.capture_items.new('FLOAT', "Value")
			capture_attribute_002.capture_items["Value"].data_type = 'FLOAT_VECTOR'
			capture_attribute_002.domain = 'POINT'
			
			#node Vector Math
			vector_math = mn_utils_helix.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.operation = 'SUBTRACT'
			
			#node Position
			position = mn_utils_helix.nodes.new("GeometryNodeInputPosition")
			position.name = "Position"
			
			#node Normal
			normal = mn_utils_helix.nodes.new("GeometryNodeInputNormal")
			normal.name = "Normal"
			
			#node Reroute
			reroute_1 = mn_utils_helix.nodes.new("NodeReroute")
			reroute_1.name = "Reroute"
			#node Vector Math.002
			vector_math_002 = mn_utils_helix.nodes.new("ShaderNodeVectorMath")
			vector_math_002.name = "Vector Math.002"
			vector_math_002.operation = 'SCALE'
			#Scale
			vector_math_002.inputs[3].default_value = -1.0
			
			#node Math
			math_1 = mn_utils_helix.nodes.new("ShaderNodeMath")
			math_1.name = "Math"
			math_1.operation = 'ADD'
			math_1.use_clamp = False
			
			#node Math.002
			math_002_1 = mn_utils_helix.nodes.new("ShaderNodeMath")
			math_002_1.name = "Math.002"
			math_002_1.operation = 'RADIANS'
			math_002_1.use_clamp = False
			#Value
			math_002_1.inputs[0].default_value = -38.29999923706055
			
			#node Group Input.001
			group_input_001 = mn_utils_helix.nodes.new("NodeGroupInput")
			group_input_001.name = "Group Input.001"
			
			#node Rotate Euler
			rotate_euler = mn_utils_helix.nodes.new("FunctionNodeRotateEuler")
			rotate_euler.name = "Rotate Euler"
			rotate_euler.rotation_type = 'AXIS_ANGLE'
			rotate_euler.space = 'OBJECT'
			
			#node Accumulate Field
			accumulate_field_1 = mn_utils_helix.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_1.name = "Accumulate Field"
			accumulate_field_1.data_type = 'FLOAT'
			accumulate_field_1.domain = 'POINT'
			
			#node Math.001
			math_001_1 = mn_utils_helix.nodes.new("ShaderNodeMath")
			math_001_1.name = "Math.001"
			math_001_1.operation = 'ADD'
			math_001_1.use_clamp = False
			
			#node Math.003
			math_003 = mn_utils_helix.nodes.new("ShaderNodeMath")
			math_003.name = "Math.003"
			math_003.operation = 'MULTIPLY'
			math_003.use_clamp = False
			
			#node Group
			group = mn_utils_helix.nodes.new("GeometryNodeGroup")
			group.name = "Group"
			group.node_tree = mn_utils_curve_resample
			#Input_7
			group.inputs[3].default_value = 0.0
			#Input_9
			group.inputs[4].default_value = 0
			#Input_11
			group.inputs[5].default_value = (0.0, 0.0, 0.0)
			
			#node Set Position
			set_position_1 = mn_utils_helix.nodes.new("GeometryNodeSetPosition")
			set_position_1.name = "Set Position"
			#Selection
			set_position_1.inputs[1].default_value = True
			#Position
			set_position_1.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Field at Index
			field_at_index = mn_utils_helix.nodes.new("GeometryNodeFieldAtIndex")
			field_at_index.name = "Field at Index"
			field_at_index.data_type = 'FLOAT_VECTOR'
			field_at_index.domain = 'POINT'
			
			#node Group Input
			group_input_1 = mn_utils_helix.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			
			#node Group Input.002
			group_input_002 = mn_utils_helix.nodes.new("NodeGroupInput")
			group_input_002.name = "Group Input.002"
			
			#node Offset Point in Curve
			offset_point_in_curve = mn_utils_helix.nodes.new("GeometryNodeOffsetPointInCurve")
			offset_point_in_curve.name = "Offset Point in Curve"
			#Point Index
			offset_point_in_curve.inputs[0].default_value = 0
			
			#node Position.002
			position_002 = mn_utils_helix.nodes.new("GeometryNodeInputPosition")
			position_002.name = "Position.002"
			
			#node Set Position.001
			set_position_001 = mn_utils_helix.nodes.new("GeometryNodeSetPosition")
			set_position_001.name = "Set Position.001"
			#Selection
			set_position_001.inputs[1].default_value = True
			#Offset
			set_position_001.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			
			
			
			#Set locations
			index_1.location = (-560.0, 20.0)
			capture_attribute_1.location = (-560.0, 200.0)
			group_output_1.location = (2257.435546875, 345.3393249511719)
			store_named_attribute.location = (1994.75, 344.0044860839844)
			vector_math_003.location = (1301.4031982421875, -185.31683349609375)
			align_euler_to_vector_002.location = (1380.0, 160.0)
			align_euler_to_vector_001.location = (1540.0, 100.0)
			position_001.location = (1140.0, -180.0)
			set_curve_tilt.location = (40.0, 320.0)
			capture_attribute_001.location = (200.0, 320.0)
			capture_attribute_003.location = (600.0, 420.0)
			vector_math_001.location = (600.0, 580.0)
			curve_tangent.location = (920.0, 260.0)
			capture_attribute_002.location = (920.0, 460.0)
			vector_math.location = (1124.8154296875, 255.56277465820312)
			position.location = (217.16098022460938, 21.72336196899414)
			normal.location = (200.0, 120.0)
			reroute_1.location = (520.0, 80.0)
			vector_math_002.location = (980.0, 0.0)
			math_1.location = (1878.1685791015625, -206.32203674316406)
			math_002_1.location = (1880.0, -380.0)
			group_input_001.location = (1700.0, -220.0)
			rotate_euler.location = (2076.991455078125, 26.95979881286621)
			accumulate_field_1.location = (-320.0, 120.0)
			math_001_1.location = (-120.0, 40.0)
			math_003.location = (-560.0, -40.0)
			group.location = (-1056.075439453125, 420.99871826171875)
			set_position_1.location = (1140.0, 460.0)
			field_at_index.location = (1223.470947265625, 713.5252685546875)
			group_input_1.location = (-1289.128662109375, 9.68197250366211)
			group_input_002.location = (533.52392578125, 971.9088134765625)
			offset_point_in_curve.location = (1015.572509765625, 759.9798583984375)
			position_002.location = (1020.0, 620.0)
			set_position_001.location = (1340.0, 480.0)
			
			#Set dimensions
			index_1.width, index_1.height = 140.0, 100.0
			capture_attribute_1.width, capture_attribute_1.height = 140.0, 100.0
			group_output_1.width, group_output_1.height = 140.0, 100.0
			store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
			vector_math_003.width, vector_math_003.height = 140.0, 100.0
			align_euler_to_vector_002.width, align_euler_to_vector_002.height = 140.0, 100.0
			align_euler_to_vector_001.width, align_euler_to_vector_001.height = 140.0, 100.0
			position_001.width, position_001.height = 140.0, 100.0
			set_curve_tilt.width, set_curve_tilt.height = 140.0, 100.0
			capture_attribute_001.width, capture_attribute_001.height = 140.0, 100.0
			capture_attribute_003.width, capture_attribute_003.height = 140.0, 100.0
			vector_math_001.width, vector_math_001.height = 140.0, 100.0
			curve_tangent.width, curve_tangent.height = 140.0, 100.0
			capture_attribute_002.width, capture_attribute_002.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			position.width, position.height = 140.0, 100.0
			normal.width, normal.height = 140.0, 100.0
			reroute_1.width, reroute_1.height = 16.0, 100.0
			vector_math_002.width, vector_math_002.height = 140.0, 100.0
			math_1.width, math_1.height = 140.0, 100.0
			math_002_1.width, math_002_1.height = 140.0, 100.0
			group_input_001.width, group_input_001.height = 140.0, 100.0
			rotate_euler.width, rotate_euler.height = 140.0, 100.0
			accumulate_field_1.width, accumulate_field_1.height = 140.0, 100.0
			math_001_1.width, math_001_1.height = 140.0, 100.0
			math_003.width, math_003.height = 140.0, 100.0
			group.width, group.height = 315.14581298828125, 100.0
			set_position_1.width, set_position_1.height = 140.0, 100.0
			field_at_index.width, field_at_index.height = 140.0, 100.0
			group_input_1.width, group_input_1.height = 140.0, 100.0
			group_input_002.width, group_input_002.height = 140.0, 100.0
			offset_point_in_curve.width, offset_point_in_curve.height = 140.0, 100.0
			position_002.width, position_002.height = 140.0, 100.0
			set_position_001.width, set_position_001.height = 140.0, 100.0
			
			#initialize mn_utils_helix links
			#capture_attribute_1.Geometry -> set_curve_tilt.Curve
			mn_utils_helix.links.new(capture_attribute_1.outputs[0], set_curve_tilt.inputs[0])
			#math_001_1.Value -> set_curve_tilt.Tilt
			mn_utils_helix.links.new(math_001_1.outputs[0], set_curve_tilt.inputs[2])
			#capture_attribute_002.Geometry -> set_position_1.Geometry
			mn_utils_helix.links.new(capture_attribute_002.outputs[0], set_position_1.inputs[0])
			#vector_math_001.Vector -> set_position_1.Offset
			mn_utils_helix.links.new(vector_math_001.outputs[0], set_position_1.inputs[3])
			#normal.Normal -> vector_math_001.Vector
			mn_utils_helix.links.new(normal.outputs[0], vector_math_001.inputs[0])
			#store_named_attribute.Geometry -> group_output_1.Curve
			mn_utils_helix.links.new(store_named_attribute.outputs[0], group_output_1.inputs[0])
			#index_1.Index -> capture_attribute_1.Value
			mn_utils_helix.links.new(index_1.outputs[0], capture_attribute_1.inputs[1])
			#capture_attribute_1.Value -> accumulate_field_1.Group ID
			mn_utils_helix.links.new(capture_attribute_1.outputs[1], accumulate_field_1.inputs[1])
			#math_003.Value -> accumulate_field_1.Value
			mn_utils_helix.links.new(math_003.outputs[0], accumulate_field_1.inputs[0])
			#group_input_1.Scale -> vector_math_001.Scale
			mn_utils_helix.links.new(group_input_1.outputs[2], vector_math_001.inputs[3])
			#accumulate_field_1.Leading -> math_001_1.Value
			mn_utils_helix.links.new(accumulate_field_1.outputs[0], math_001_1.inputs[0])
			#group_input_1.Rotation -> math_001_1.Value
			mn_utils_helix.links.new(group_input_1.outputs[3], math_001_1.inputs[1])
			#set_curve_tilt.Curve -> capture_attribute_001.Geometry
			mn_utils_helix.links.new(set_curve_tilt.outputs[0], capture_attribute_001.inputs[0])
			#vector_math.Vector -> group_output_1.pos_old - pos_new
			mn_utils_helix.links.new(vector_math.outputs[0], group_output_1.inputs[1])
			#set_position_001.Geometry -> store_named_attribute.Geometry
			mn_utils_helix.links.new(set_position_001.outputs[0], store_named_attribute.inputs[0])
			#reroute_1.Output -> vector_math.Vector
			mn_utils_helix.links.new(reroute_1.outputs[0], vector_math.inputs[0])
			#rotate_euler.Rotation -> store_named_attribute.Value
			mn_utils_helix.links.new(rotate_euler.outputs[0], store_named_attribute.inputs[3])
			#align_euler_to_vector_002.Rotation -> align_euler_to_vector_001.Rotation
			mn_utils_helix.links.new(align_euler_to_vector_002.outputs[0], align_euler_to_vector_001.inputs[0])
			#capture_attribute_003.Geometry -> capture_attribute_002.Geometry
			mn_utils_helix.links.new(capture_attribute_003.outputs[0], capture_attribute_002.inputs[0])
			#curve_tangent.Tangent -> capture_attribute_002.Value
			mn_utils_helix.links.new(curve_tangent.outputs[0], capture_attribute_002.inputs[1])
			#capture_attribute_002.Value -> align_euler_to_vector_002.Vector
			mn_utils_helix.links.new(capture_attribute_002.outputs[1], align_euler_to_vector_002.inputs[2])
			#capture_attribute_001.Value -> reroute_1.Input
			mn_utils_helix.links.new(capture_attribute_001.outputs[1], reroute_1.inputs[0])
			#align_euler_to_vector_001.Rotation -> rotate_euler.Rotation
			mn_utils_helix.links.new(align_euler_to_vector_001.outputs[0], rotate_euler.inputs[0])
			#position_001.Position -> vector_math_003.Vector
			mn_utils_helix.links.new(position_001.outputs[0], vector_math_003.inputs[0])
			#capture_attribute_001.Geometry -> capture_attribute_003.Geometry
			mn_utils_helix.links.new(capture_attribute_001.outputs[0], capture_attribute_003.inputs[0])
			#position.Position -> capture_attribute_003.Value
			mn_utils_helix.links.new(position.outputs[0], capture_attribute_003.inputs[1])
			#capture_attribute_003.Value -> vector_math_003.Vector
			mn_utils_helix.links.new(capture_attribute_003.outputs[1], vector_math_003.inputs[1])
			#vector_math_003.Vector -> rotate_euler.Axis
			mn_utils_helix.links.new(vector_math_003.outputs[0], rotate_euler.inputs[2])
			#normal.Normal -> capture_attribute_001.Value
			mn_utils_helix.links.new(normal.outputs[0], capture_attribute_001.inputs[1])
			#position.Position -> vector_math.Vector
			mn_utils_helix.links.new(position.outputs[0], vector_math.inputs[1])
			#reroute_1.Output -> vector_math_002.Vector
			mn_utils_helix.links.new(reroute_1.outputs[0], vector_math_002.inputs[0])
			#vector_math_002.Vector -> align_euler_to_vector_001.Vector
			mn_utils_helix.links.new(vector_math_002.outputs[0], align_euler_to_vector_001.inputs[2])
			#math_1.Value -> rotate_euler.Angle
			mn_utils_helix.links.new(math_1.outputs[0], rotate_euler.inputs[3])
			#math_002_1.Value -> math_1.Value
			mn_utils_helix.links.new(math_002_1.outputs[0], math_1.inputs[1])
			#group_input_001.Angle -> math_1.Value
			mn_utils_helix.links.new(group_input_001.outputs[4], math_1.inputs[0])
			#group_input_1.Value -> math_003.Value
			mn_utils_helix.links.new(group_input_1.outputs[1], math_003.inputs[0])
			#group_input_1.Unwind -> math_003.Value
			mn_utils_helix.links.new(group_input_1.outputs[5], math_003.inputs[1])
			#group_input_1.Geometry -> group.Geometry
			mn_utils_helix.links.new(group_input_1.outputs[0], group.inputs[0])
			#group_input_1.Offset -> group.Offset
			mn_utils_helix.links.new(group_input_1.outputs[6], group.inputs[1])
			#group_input_1.Length -> group.Length
			mn_utils_helix.links.new(group_input_1.outputs[7], group.inputs[2])
			#group_input_1.Geometry -> capture_attribute_1.Geometry
			mn_utils_helix.links.new(group_input_1.outputs[0], capture_attribute_1.inputs[0])
			#set_position_1.Geometry -> set_position_001.Geometry
			mn_utils_helix.links.new(set_position_1.outputs[0], set_position_001.inputs[0])
			#position_002.Position -> field_at_index.Value
			mn_utils_helix.links.new(position_002.outputs[0], field_at_index.inputs[1])
			#offset_point_in_curve.Point Index -> field_at_index.Index
			mn_utils_helix.links.new(offset_point_in_curve.outputs[1], field_at_index.inputs[0])
			#field_at_index.Value -> set_position_001.Position
			mn_utils_helix.links.new(field_at_index.outputs[0], set_position_001.inputs[2])
			#group_input_002.Offset -> offset_point_in_curve.Offset
			mn_utils_helix.links.new(group_input_002.outputs[8], offset_point_in_curve.inputs[1])
			return mn_utils_helix

		mn_utils_helix = mn_utils_helix_node_group()

		#initialize mn_dna_double_helix node group
		def mn_dna_double_helix_node_group():
			mn_dna_double_helix = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "MN_dna_double_helix")

			mn_dna_double_helix.color_tag = 'NONE'
			mn_dna_double_helix.description = ""

			mn_dna_double_helix.is_modifier = True
			
			#mn_dna_double_helix interface
			#Socket Base Instances
			base_instances_socket = mn_dna_double_helix.interface.new_socket(name = "Base Instances", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			base_instances_socket.attribute_domain = 'POINT'
			
			#Socket Helix Curve
			helix_curve_socket = mn_dna_double_helix.interface.new_socket(name = "Helix Curve", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			helix_curve_socket.attribute_domain = 'POINT'
			
			#Socket Curve
			curve_socket_1 = mn_dna_double_helix.interface.new_socket(name = "Curve", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			curve_socket_1.attribute_domain = 'POINT'
			
			#Socket Bases
			bases_socket = mn_dna_double_helix.interface.new_socket(name = "Bases", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			bases_socket.attribute_domain = 'POINT'
			
			#Socket Rot. Sec. Strand
			rot__sec__strand_socket = mn_dna_double_helix.interface.new_socket(name = "Rot. Sec. Strand", in_out='INPUT', socket_type = 'NodeSocketFloat')
			rot__sec__strand_socket.subtype = 'NONE'
			rot__sec__strand_socket.default_value = 0.0
			rot__sec__strand_socket.min_value = -10000.0
			rot__sec__strand_socket.max_value = 10000.0
			rot__sec__strand_socket.attribute_domain = 'POINT'
			
			#Socket Unzip
			unzip_socket = mn_dna_double_helix.interface.new_socket(name = "Unzip", in_out='INPUT', socket_type = 'NodeSocketFloat')
			unzip_socket.subtype = 'NONE'
			unzip_socket.default_value = 1.0
			unzip_socket.min_value = -10000.0
			unzip_socket.max_value = 10000.0
			unzip_socket.attribute_domain = 'POINT'
			
			#Socket Rotation
			rotation_socket_1 = mn_dna_double_helix.interface.new_socket(name = "Rotation", in_out='INPUT', socket_type = 'NodeSocketFloat')
			rotation_socket_1.subtype = 'NONE'
			rotation_socket_1.default_value = 0.0
			rotation_socket_1.min_value = -3.4028234663852886e+38
			rotation_socket_1.max_value = 3.4028234663852886e+38
			rotation_socket_1.attribute_domain = 'POINT'
			
			#Socket Unwind
			unwind_socket_1 = mn_dna_double_helix.interface.new_socket(name = "Unwind", in_out='INPUT', socket_type = 'NodeSocketFloat')
			unwind_socket_1.subtype = 'NONE'
			unwind_socket_1.default_value = 1.0
			unwind_socket_1.min_value = -10000.0
			unwind_socket_1.max_value = 10000.0
			unwind_socket_1.attribute_domain = 'POINT'
			
			
			#initialize mn_dna_double_helix nodes
			#node Reroute.002
			reroute_002_1 = mn_dna_double_helix.nodes.new("NodeReroute")
			reroute_002_1.name = "Reroute.002"
			#node Instance on Points.001
			instance_on_points_001 = mn_dna_double_helix.nodes.new("GeometryNodeInstanceOnPoints")
			instance_on_points_001.name = "Instance on Points.001"
			#Selection
			instance_on_points_001.inputs[1].default_value = True
			#Pick Instance
			instance_on_points_001.inputs[3].default_value = True
			#Scale
			instance_on_points_001.inputs[6].default_value = (1.0, 1.0, 1.0)
			
			#node Named Attribute
			named_attribute = mn_dna_double_helix.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute.inputs[0].default_value = "rot"
			
			#node Reroute
			reroute_2 = mn_dna_double_helix.nodes.new("NodeReroute")
			reroute_2.name = "Reroute"
			#node Value.001
			value_001 = mn_dna_double_helix.nodes.new("ShaderNodeValue")
			value_001.label = "tau / 11"
			value_001.name = "Value.001"
			
			value_001.outputs[0].default_value = 0.5711986422538757
			#node Math.004
			math_004 = mn_dna_double_helix.nodes.new("ShaderNodeMath")
			math_004.name = "Math.004"
			math_004.operation = 'MULTIPLY'
			math_004.use_clamp = False
			
			#node Math.003
			math_003_1 = mn_dna_double_helix.nodes.new("ShaderNodeMath")
			math_003_1.name = "Math.003"
			math_003_1.operation = 'DIVIDE'
			math_003_1.use_clamp = False
			#Value
			math_003_1.inputs[0].default_value = 0.9200000166893005
			#Value_001
			math_003_1.inputs[1].default_value = 10.0
			
			#node Value.004
			value_004 = mn_dna_double_helix.nodes.new("ShaderNodeValue")
			value_004.name = "Value.004"
			
			value_004.outputs[0].default_value = 1.6766369342803955
			#node Math.002
			math_002_2 = mn_dna_double_helix.nodes.new("ShaderNodeMath")
			math_002_2.name = "Math.002"
			math_002_2.operation = 'ADD'
			math_002_2.use_clamp = False
			
			#node Math.001
			math_001_2 = mn_dna_double_helix.nodes.new("ShaderNodeMath")
			math_001_2.name = "Math.001"
			math_001_2.operation = 'ADD'
			math_001_2.use_clamp = False
			
			#node Math.005
			math_005 = mn_dna_double_helix.nodes.new("ShaderNodeMath")
			math_005.name = "Math.005"
			math_005.operation = 'DIVIDE'
			math_005.use_clamp = False
			#Value_001
			math_005.inputs[1].default_value = 100.0
			
			#node Group
			group_1 = mn_dna_double_helix.nodes.new("GeometryNodeGroup")
			group_1.name = "Group"
			group_1.node_tree = mn_utils_curve_resample
			#Input_12
			group_1.inputs[1].default_value = 0.0
			#Input_7
			group_1.inputs[3].default_value = 0.0
			#Input_9
			group_1.inputs[4].default_value = 0
			#Input_11
			group_1.inputs[5].default_value = (0.0, 0.0, 0.0)
			
			#node Random Value
			random_value = mn_dna_double_helix.nodes.new("FunctionNodeRandomValue")
			random_value.name = "Random Value"
			random_value.data_type = 'INT'
			#Min_002
			random_value.inputs[4].default_value = 0
			#Max_002
			random_value.inputs[5].default_value = 3
			#ID
			random_value.inputs[7].default_value = 0
			#Seed
			random_value.inputs[8].default_value = 1
			
			#node Join Geometry.001
			join_geometry_001 = mn_dna_double_helix.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_001.name = "Join Geometry.001"
			join_geometry_001.hide = True
			
			#node Index.001
			index_001 = mn_dna_double_helix.nodes.new("GeometryNodeInputIndex")
			index_001.name = "Index.001"
			
			#node Capture Attribute
			capture_attribute_2 = mn_dna_double_helix.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute_2.name = "Capture Attribute"
			capture_attribute_2.active_index = 0
			capture_attribute_2.capture_items.clear()
			capture_attribute_2.capture_items.new('FLOAT', "Value")
			capture_attribute_2.capture_items["Value"].data_type = 'INT'
			capture_attribute_2.domain = 'CURVE'
			
			#node Group Input.001
			group_input_001_1 = mn_dna_double_helix.nodes.new("NodeGroupInput")
			group_input_001_1.name = "Group Input.001"
			
			#node Capture Attribute.001
			capture_attribute_001_1 = mn_dna_double_helix.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute_001_1.name = "Capture Attribute.001"
			capture_attribute_001_1.active_index = 0
			capture_attribute_001_1.capture_items.clear()
			capture_attribute_001_1.capture_items.new('FLOAT', "Value")
			capture_attribute_001_1.capture_items["Value"].data_type = 'INT'
			capture_attribute_001_1.domain = 'POINT'
			
			#node Switch
			switch_1 = mn_dna_double_helix.nodes.new("GeometryNodeSwitch")
			switch_1.name = "Switch"
			switch_1.input_type = 'INT'
			
			#node Named Attribute.001
			named_attribute_001 = mn_dna_double_helix.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.data_type = 'INT'
			#Name
			named_attribute_001.inputs[0].default_value = "chain_id"
			
			#node Compare.001
			compare_001 = mn_dna_double_helix.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'INT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'EQUAL'
			#B_INT
			compare_001.inputs[3].default_value = 0
			
			#node Reroute.001
			reroute_001_1 = mn_dna_double_helix.nodes.new("NodeReroute")
			reroute_001_1.name = "Reroute.001"
			#node Math.007
			math_007 = mn_dna_double_helix.nodes.new("ShaderNodeMath")
			math_007.name = "Math.007"
			math_007.operation = 'SUBTRACT'
			math_007.use_clamp = False
			#Value_001
			math_007.inputs[1].default_value = 3.0
			
			#node Math.008
			math_008 = mn_dna_double_helix.nodes.new("ShaderNodeMath")
			math_008.name = "Math.008"
			math_008.operation = 'ABSOLUTE'
			math_008.use_clamp = False
			
			#node Math.006
			math_006 = mn_dna_double_helix.nodes.new("ShaderNodeMath")
			math_006.name = "Math.006"
			math_006.operation = 'DIVIDE'
			math_006.use_clamp = False
			#Value
			math_006.inputs[0].default_value = -3.0
			#Value_001
			math_006.inputs[1].default_value = 100.0
			
			#node Group Input
			group_input_2 = mn_dna_double_helix.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
			#node Math
			math_2 = mn_dna_double_helix.nodes.new("ShaderNodeMath")
			math_2.name = "Math"
			math_2.operation = 'DIVIDE'
			math_2.use_clamp = False
			#Value_001
			math_2.inputs[1].default_value = 100.0
			
			#node Value
			value = mn_dna_double_helix.nodes.new("ShaderNodeValue")
			value.name = "Value"
			
			value.outputs[0].default_value = 3.780000686645508
			#node Group.001
			group_001 = mn_dna_double_helix.nodes.new("GeometryNodeGroup")
			group_001.name = "Group.001"
			group_001.node_tree = mn_utils_helix
			#Input_8
			group_001.inputs[4].default_value = 0.0
			#Input_10
			group_001.inputs[6].default_value = 0.009999999776482582
			#Input_12
			group_001.inputs[8].default_value = 0
			
			#node Group Output
			group_output_2 = mn_dna_double_helix.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Named Attribute.002
			named_attribute_002 = mn_dna_double_helix.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002.name = "Named Attribute.002"
			named_attribute_002.data_type = 'INT'
			#Name
			named_attribute_002.inputs[0].default_value = "chain_id"
			
			#node Compare
			compare_1 = mn_dna_double_helix.nodes.new("FunctionNodeCompare")
			compare_1.name = "Compare"
			compare_1.data_type = 'INT'
			compare_1.mode = 'ELEMENT'
			compare_1.operation = 'EQUAL'
			#B_INT
			compare_1.inputs[3].default_value = 0
			
			#node Translate Instances
			translate_instances = mn_dna_double_helix.nodes.new("GeometryNodeTranslateInstances")
			translate_instances.name = "Translate Instances"
			#Local Space
			translate_instances.inputs[3].default_value = True
			
			#node Vector Math
			vector_math_1 = mn_dna_double_helix.nodes.new("ShaderNodeVectorMath")
			vector_math_1.name = "Vector Math"
			vector_math_1.operation = 'SCALE'
			#Vector
			vector_math_1.inputs[0].default_value = (-3.5799994468688965, -3.2300000190734863, 0.010000228881835938)
			#Scale
			vector_math_1.inputs[3].default_value = 0.009999999776482582
			
			#node Rotate Instances
			rotate_instances = mn_dna_double_helix.nodes.new("GeometryNodeRotateInstances")
			rotate_instances.name = "Rotate Instances"
			#Selection
			rotate_instances.inputs[1].default_value = True
			#Rotation
			rotate_instances.inputs[2].default_value = (0.2010618895292282, 0.24678947031497955, 1.8921113014221191)
			#Pivot Point
			rotate_instances.inputs[3].default_value = (0.0, 0.0, 0.0)
			#Local Space
			rotate_instances.inputs[4].default_value = True
			
			#node Group.002
			group_002 = mn_dna_double_helix.nodes.new("GeometryNodeGroup")
			group_002.name = "Group.002"
			group_002.node_tree = mn_utils_helix
			#Input_8
			group_002.inputs[4].default_value = 3.148574113845825
			#Input_12
			group_002.inputs[8].default_value = 0
			
			#node Store Named Attribute
			store_named_attribute_1 = mn_dna_double_helix.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_1.name = "Store Named Attribute"
			store_named_attribute_1.data_type = 'INT'
			store_named_attribute_1.domain = 'POINT'
			#Selection
			store_named_attribute_1.inputs[1].default_value = True
			#Name
			store_named_attribute_1.inputs[2].default_value = "chain_id"
			
			
			
			
			#Set locations
			reroute_002_1.location = (-402.0, 120.0)
			instance_on_points_001.location = (798.0, 260.0)
			named_attribute.location = (798.0, -20.0)
			reroute_2.location = (-464.8250732421875, -118.33726501464844)
			value_001.location = (-622.0, 240.0)
			math_004.location = (-682.0, 80.0)
			math_003_1.location = (-682.0, -80.0)
			value_004.location = (-882.0, -260.0)
			math_002_2.location = (-682.0, -260.0)
			math_001_2.location = (-502.0, -260.0)
			math_005.location = (-504.94775390625, -435.8669128417969)
			group_1.location = (-1162.56884765625, 195.8053741455078)
			random_value.location = (-1060.4847412109375, 435.9537048339844)
			join_geometry_001.location = (18.0, 260.0)
			index_001.location = (18.0, 220.0)
			capture_attribute_2.location = (198.0, 360.0)
			group_input_001_1.location = (358.0, 160.0)
			capture_attribute_001_1.location = (-813.2508544921875, 494.56048583984375)
			switch_1.location = (518.0, -40.0)
			named_attribute_001.location = (158.0, -40.0)
			compare_001.location = (318.0, -40.0)
			reroute_001_1.location = (142.068115234375, -25.483333587646484)
			math_007.location = (318.0, -220.0)
			math_008.location = (518.0, -220.0)
			math_006.location = (-502.0, -620.0)
			group_input_2.location = (-1574.67822265625, 110.0733642578125)
			math_2.location = (-1422.0, -100.0)
			value.location = (-1582.0, -100.0)
			group_001.location = (-262.0, 280.0)
			group_output_2.location = (1780.26904296875, 177.51312255859375)
			named_attribute_002.location = (1043.337158203125, -57.230098724365234)
			compare_1.location = (1201.8712158203125, -58.711971282958984)
			translate_instances.location = (1340.243896484375, 257.7772216796875)
			vector_math_1.location = (1168.5482177734375, 170.97555541992188)
			rotate_instances.location = (966.5189208984375, 263.74462890625)
			group_002.location = (-262.0, -80.0)
			store_named_attribute_1.location = (358.0, 360.0)
			
			#Set dimensions
			reroute_002_1.width, reroute_002_1.height = 16.0, 100.0
			instance_on_points_001.width, instance_on_points_001.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			reroute_2.width, reroute_2.height = 16.0, 100.0
			value_001.width, value_001.height = 140.0, 100.0
			math_004.width, math_004.height = 140.0, 100.0
			math_003_1.width, math_003_1.height = 140.0, 100.0
			value_004.width, value_004.height = 140.0, 100.0
			math_002_2.width, math_002_2.height = 140.0, 100.0
			math_001_2.width, math_001_2.height = 140.0, 100.0
			math_005.width, math_005.height = 140.0, 100.0
			group_1.width, group_1.height = 277.358154296875, 100.0
			random_value.width, random_value.height = 140.0, 100.0
			join_geometry_001.width, join_geometry_001.height = 140.0, 100.0
			index_001.width, index_001.height = 140.0, 100.0
			capture_attribute_2.width, capture_attribute_2.height = 140.0, 100.0
			group_input_001_1.width, group_input_001_1.height = 140.0, 100.0
			capture_attribute_001_1.width, capture_attribute_001_1.height = 140.0, 100.0
			switch_1.width, switch_1.height = 140.0, 100.0
			named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			reroute_001_1.width, reroute_001_1.height = 16.0, 100.0
			math_007.width, math_007.height = 140.0, 100.0
			math_008.width, math_008.height = 140.0, 100.0
			math_006.width, math_006.height = 140.0, 100.0
			group_input_2.width, group_input_2.height = 140.0, 100.0
			math_2.width, math_2.height = 140.0, 100.0
			value.width, value.height = 140.0, 100.0
			group_001.width, group_001.height = 229.2681884765625, 100.0
			group_output_2.width, group_output_2.height = 140.0, 100.0
			named_attribute_002.width, named_attribute_002.height = 140.0, 100.0
			compare_1.width, compare_1.height = 140.0, 100.0
			translate_instances.width, translate_instances.height = 140.0, 100.0
			vector_math_1.width, vector_math_1.height = 140.0, 100.0
			rotate_instances.width, rotate_instances.height = 140.0, 100.0
			group_002.width, group_002.height = 232.57440185546875, 100.0
			store_named_attribute_1.width, store_named_attribute_1.height = 140.0, 100.0
			
			#initialize mn_dna_double_helix links
			#group_input_2.Curve -> group_1.Geometry
			mn_dna_double_helix.links.new(group_input_2.outputs[0], group_1.inputs[0])
			#translate_instances.Instances -> group_output_2.Base Instances
			mn_dna_double_helix.links.new(translate_instances.outputs[0], group_output_2.inputs[0])
			#reroute_002_1.Output -> group_001.Geometry
			mn_dna_double_helix.links.new(reroute_002_1.outputs[0], group_001.inputs[0])
			#math_2.Value -> group_1.Length
			mn_dna_double_helix.links.new(math_2.outputs[0], group_1.inputs[2])
			#value.Value -> math_2.Value
			mn_dna_double_helix.links.new(value.outputs[0], math_2.inputs[0])
			#reroute_002_1.Output -> group_002.Geometry
			mn_dna_double_helix.links.new(reroute_002_1.outputs[0], group_002.inputs[0])
			#group_002.Curve -> join_geometry_001.Geometry
			mn_dna_double_helix.links.new(group_002.outputs[0], join_geometry_001.inputs[0])
			#value_001.Value -> group_001.Value
			mn_dna_double_helix.links.new(value_001.outputs[0], group_001.inputs[1])
			#value_001.Value -> group_002.Value
			mn_dna_double_helix.links.new(value_001.outputs[0], group_002.inputs[1])
			#math_004.Value -> group_001.Scale
			mn_dna_double_helix.links.new(math_004.outputs[0], group_001.inputs[2])
			#math_004.Value -> group_002.Scale
			mn_dna_double_helix.links.new(math_004.outputs[0], group_002.inputs[2])
			#reroute_2.Output -> group_001.Rotation
			mn_dna_double_helix.links.new(reroute_2.outputs[0], group_001.inputs[3])
			#reroute_2.Output -> math_001_2.Value
			mn_dna_double_helix.links.new(reroute_2.outputs[0], math_001_2.inputs[0])
			#math_001_2.Value -> group_002.Rotation
			mn_dna_double_helix.links.new(math_001_2.outputs[0], group_002.inputs[3])
			#math_002_2.Value -> math_001_2.Value
			mn_dna_double_helix.links.new(math_002_2.outputs[0], math_001_2.inputs[1])
			#store_named_attribute_1.Geometry -> instance_on_points_001.Points
			mn_dna_double_helix.links.new(store_named_attribute_1.outputs[0], instance_on_points_001.inputs[0])
			#named_attribute.Attribute -> instance_on_points_001.Rotation
			mn_dna_double_helix.links.new(named_attribute.outputs[0], instance_on_points_001.inputs[5])
			#join_geometry_001.Geometry -> capture_attribute_2.Geometry
			mn_dna_double_helix.links.new(join_geometry_001.outputs[0], capture_attribute_2.inputs[0])
			#index_001.Index -> capture_attribute_2.Value
			mn_dna_double_helix.links.new(index_001.outputs[0], capture_attribute_2.inputs[1])
			#capture_attribute_2.Geometry -> store_named_attribute_1.Geometry
			mn_dna_double_helix.links.new(capture_attribute_2.outputs[0], store_named_attribute_1.inputs[0])
			#capture_attribute_2.Value -> store_named_attribute_1.Value
			mn_dna_double_helix.links.new(capture_attribute_2.outputs[1], store_named_attribute_1.inputs[3])
			#group_input_001_1.Bases -> instance_on_points_001.Instance
			mn_dna_double_helix.links.new(group_input_001_1.outputs[1], instance_on_points_001.inputs[2])
			#value_004.Value -> math_002_2.Value
			mn_dna_double_helix.links.new(value_004.outputs[0], math_002_2.inputs[0])
			#group_input_2.Rot. Sec. Strand -> math_002_2.Value
			mn_dna_double_helix.links.new(group_input_2.outputs[2], math_002_2.inputs[1])
			#group_input_2.Unzip -> math_004.Value
			mn_dna_double_helix.links.new(group_input_2.outputs[3], math_004.inputs[1])
			#group_input_2.Rotation -> reroute_2.Input
			mn_dna_double_helix.links.new(group_input_2.outputs[4], reroute_2.inputs[0])
			#group_input_2.Unwind -> group_001.Unwind
			mn_dna_double_helix.links.new(group_input_2.outputs[5], group_001.inputs[5])
			#group_input_2.Unwind -> group_002.Unwind
			mn_dna_double_helix.links.new(group_input_2.outputs[5], group_002.inputs[5])
			#math_003_1.Value -> math_004.Value
			mn_dna_double_helix.links.new(math_003_1.outputs[0], math_004.inputs[0])
			#math_005.Value -> group_001.Length
			mn_dna_double_helix.links.new(math_005.outputs[0], group_001.inputs[7])
			#math_005.Value -> group_002.Length
			mn_dna_double_helix.links.new(math_005.outputs[0], group_002.inputs[7])
			#value.Value -> math_005.Value
			mn_dna_double_helix.links.new(value.outputs[0], math_005.inputs[0])
			#math_006.Value -> group_002.Offset
			mn_dna_double_helix.links.new(math_006.outputs[0], group_002.inputs[6])
			#group_1.Geometry -> capture_attribute_001_1.Geometry
			mn_dna_double_helix.links.new(group_1.outputs[0], capture_attribute_001_1.inputs[0])
			#random_value.Value -> capture_attribute_001_1.Value
			mn_dna_double_helix.links.new(random_value.outputs[2], capture_attribute_001_1.inputs[1])
			#capture_attribute_001_1.Geometry -> reroute_002_1.Input
			mn_dna_double_helix.links.new(capture_attribute_001_1.outputs[0], reroute_002_1.inputs[0])
			#named_attribute_001.Attribute -> compare_001.A
			mn_dna_double_helix.links.new(named_attribute_001.outputs[0], compare_001.inputs[2])
			#compare_001.Result -> switch_1.Switch
			mn_dna_double_helix.links.new(compare_001.outputs[0], switch_1.inputs[0])
			#reroute_001_1.Output -> switch_1.False
			mn_dna_double_helix.links.new(reroute_001_1.outputs[0], switch_1.inputs[1])
			#switch_1.Output -> instance_on_points_001.Instance Index
			mn_dna_double_helix.links.new(switch_1.outputs[0], instance_on_points_001.inputs[4])
			#capture_attribute_001_1.Value -> reroute_001_1.Input
			mn_dna_double_helix.links.new(capture_attribute_001_1.outputs[1], reroute_001_1.inputs[0])
			#reroute_001_1.Output -> math_007.Value
			mn_dna_double_helix.links.new(reroute_001_1.outputs[0], math_007.inputs[0])
			#math_007.Value -> math_008.Value
			mn_dna_double_helix.links.new(math_007.outputs[0], math_008.inputs[0])
			#math_008.Value -> switch_1.True
			mn_dna_double_helix.links.new(math_008.outputs[0], switch_1.inputs[2])
			#rotate_instances.Instances -> translate_instances.Instances
			mn_dna_double_helix.links.new(rotate_instances.outputs[0], translate_instances.inputs[0])
			#named_attribute_002.Attribute -> compare_1.A
			mn_dna_double_helix.links.new(named_attribute_002.outputs[0], compare_1.inputs[2])
			#compare_1.Result -> translate_instances.Selection
			mn_dna_double_helix.links.new(compare_1.outputs[0], translate_instances.inputs[1])
			#vector_math_1.Vector -> translate_instances.Translation
			mn_dna_double_helix.links.new(vector_math_1.outputs[0], translate_instances.inputs[2])
			#instance_on_points_001.Instances -> rotate_instances.Instances
			mn_dna_double_helix.links.new(instance_on_points_001.outputs[0], rotate_instances.inputs[0])
			#store_named_attribute_1.Geometry -> group_output_2.Helix Curve
			mn_dna_double_helix.links.new(store_named_attribute_1.outputs[0], group_output_2.inputs[1])
			#group_001.Curve -> join_geometry_001.Geometry
			mn_dna_double_helix.links.new(group_001.outputs[0], join_geometry_001.inputs[0])
			return mn_dna_double_helix

		mn_dna_double_helix = mn_dna_double_helix_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "MN_dna_double_helix", type = 'NODES')
		mod.node_group = mn_dna_double_helix
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(MN_dna_double_helix.bl_idname)
			
def register():
	bpy.utils.register_class(MN_dna_double_helix)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(MN_dna_double_helix)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
