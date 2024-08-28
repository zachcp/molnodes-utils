bl_info = {
	"name" : "MN_utils_helix",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class MN_utils_helix(bpy.types.Operator):
	bl_idname = "node.mn_utils_helix"
	bl_label = "MN_utils_helix"
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
			position_socket.default_value = (0.0, 0.0, 0.0)
			position_socket.min_value = -3.4028234663852886e+38
			position_socket.max_value = 3.4028234663852886e+38
			position_socket.subtype = 'NONE'
			position_socket.attribute_domain = 'POINT'
			
			#Socket Tangent
			tangent_socket = mn_utils_curve_resample.interface.new_socket(name = "Tangent", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			tangent_socket.default_value = (0.0, 0.0, 0.0)
			tangent_socket.min_value = -3.4028234663852886e+38
			tangent_socket.max_value = 3.4028234663852886e+38
			tangent_socket.subtype = 'NONE'
			tangent_socket.attribute_domain = 'POINT'
			
			#Socket Normal
			normal_socket = mn_utils_curve_resample.interface.new_socket(name = "Normal", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			normal_socket.default_value = (0.0, 0.0, 0.0)
			normal_socket.min_value = -3.4028234663852886e+38
			normal_socket.max_value = 3.4028234663852886e+38
			normal_socket.subtype = 'NONE'
			normal_socket.attribute_domain = 'POINT'
			
			#Socket Field Float
			field_float_socket = mn_utils_curve_resample.interface.new_socket(name = "Field Float", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			field_float_socket.default_value = 0.0
			field_float_socket.min_value = -3.4028234663852886e+38
			field_float_socket.max_value = 3.4028234663852886e+38
			field_float_socket.subtype = 'NONE'
			field_float_socket.attribute_domain = 'POINT'
			
			#Socket Field Int
			field_int_socket = mn_utils_curve_resample.interface.new_socket(name = "Field Int", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			field_int_socket.default_value = 0
			field_int_socket.min_value = -2147483648
			field_int_socket.max_value = 2147483647
			field_int_socket.subtype = 'NONE'
			field_int_socket.attribute_domain = 'POINT'
			
			#Socket Field Vec
			field_vec_socket = mn_utils_curve_resample.interface.new_socket(name = "Field Vec", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			field_vec_socket.default_value = (0.0, 0.0, 0.0)
			field_vec_socket.min_value = -3.4028234663852886e+38
			field_vec_socket.max_value = 3.4028234663852886e+38
			field_vec_socket.subtype = 'NONE'
			field_vec_socket.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_1 = mn_utils_curve_resample.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_1.attribute_domain = 'POINT'
			
			#Socket Offset
			offset_socket = mn_utils_curve_resample.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketFloat')
			offset_socket.default_value = 2.299999952316284
			offset_socket.min_value = -10000.0
			offset_socket.max_value = 10000.0
			offset_socket.subtype = 'NONE'
			offset_socket.attribute_domain = 'POINT'
			
			#Socket Length
			length_socket = mn_utils_curve_resample.interface.new_socket(name = "Length", in_out='INPUT', socket_type = 'NodeSocketFloat')
			length_socket.default_value = 0.36000001430511475
			length_socket.min_value = 0.009999999776482582
			length_socket.max_value = 3.4028234663852886e+38
			length_socket.subtype = 'DISTANCE'
			length_socket.attribute_domain = 'POINT'
			
			#Socket Field Float
			field_float_socket_1 = mn_utils_curve_resample.interface.new_socket(name = "Field Float", in_out='INPUT', socket_type = 'NodeSocketFloat')
			field_float_socket_1.default_value = 0.0
			field_float_socket_1.min_value = -3.4028234663852886e+38
			field_float_socket_1.max_value = 3.4028234663852886e+38
			field_float_socket_1.subtype = 'NONE'
			field_float_socket_1.attribute_domain = 'POINT'
			field_float_socket_1.hide_value = True
			
			#Socket Field Int
			field_int_socket_1 = mn_utils_curve_resample.interface.new_socket(name = "Field Int", in_out='INPUT', socket_type = 'NodeSocketInt')
			field_int_socket_1.default_value = 0
			field_int_socket_1.min_value = -2147483648
			field_int_socket_1.max_value = 2147483647
			field_int_socket_1.subtype = 'NONE'
			field_int_socket_1.attribute_domain = 'POINT'
			field_int_socket_1.hide_value = True
			
			#Socket Field Vec
			field_vec_socket_1 = mn_utils_curve_resample.interface.new_socket(name = "Field Vec", in_out='INPUT', socket_type = 'NodeSocketVector')
			field_vec_socket_1.default_value = (0.0, 0.0, 0.0)
			field_vec_socket_1.min_value = -3.4028234663852886e+38
			field_vec_socket_1.max_value = 3.4028234663852886e+38
			field_vec_socket_1.subtype = 'NONE'
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
			pos_old___pos_new_socket.default_value = (0.0, 0.0, 0.0)
			pos_old___pos_new_socket.min_value = -3.4028234663852886e+38
			pos_old___pos_new_socket.max_value = 3.4028234663852886e+38
			pos_old___pos_new_socket.subtype = 'NONE'
			pos_old___pos_new_socket.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_2 = mn_utils_helix.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_2.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket = mn_utils_helix.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket.default_value = 0.5711986422538757
			value_socket.min_value = -3.4028234663852886e+38
			value_socket.max_value = 3.4028234663852886e+38
			value_socket.subtype = 'NONE'
			value_socket.attribute_domain = 'POINT'
			
			#Socket Scale
			scale_socket = mn_utils_helix.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
			scale_socket.default_value = 0.10000000149011612
			scale_socket.min_value = -10000.0
			scale_socket.max_value = 10000.0
			scale_socket.subtype = 'NONE'
			scale_socket.attribute_domain = 'POINT'
			
			#Socket Rotation
			rotation_socket = mn_utils_helix.interface.new_socket(name = "Rotation", in_out='INPUT', socket_type = 'NodeSocketFloat')
			rotation_socket.default_value = 0.5
			rotation_socket.min_value = -10000.0
			rotation_socket.max_value = 10000.0
			rotation_socket.subtype = 'NONE'
			rotation_socket.attribute_domain = 'POINT'
			
			#Socket Angle
			angle_socket = mn_utils_helix.interface.new_socket(name = "Angle", in_out='INPUT', socket_type = 'NodeSocketFloat')
			angle_socket.default_value = -0.8028512597084045
			angle_socket.min_value = -3.4028234663852886e+38
			angle_socket.max_value = 3.4028234663852886e+38
			angle_socket.subtype = 'ANGLE'
			angle_socket.attribute_domain = 'POINT'
			
			#Socket Unwind
			unwind_socket = mn_utils_helix.interface.new_socket(name = "Unwind", in_out='INPUT', socket_type = 'NodeSocketFloat')
			unwind_socket.default_value = 1.0
			unwind_socket.min_value = -10000.0
			unwind_socket.max_value = 10000.0
			unwind_socket.subtype = 'NONE'
			unwind_socket.attribute_domain = 'POINT'
			
			#Socket Offset
			offset_socket_1 = mn_utils_helix.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketFloat')
			offset_socket_1.default_value = 0.009999999776482582
			offset_socket_1.min_value = -10000.0
			offset_socket_1.max_value = 10000.0
			offset_socket_1.subtype = 'NONE'
			offset_socket_1.attribute_domain = 'POINT'
			
			#Socket Length
			length_socket_1 = mn_utils_helix.interface.new_socket(name = "Length", in_out='INPUT', socket_type = 'NodeSocketFloat')
			length_socket_1.default_value = 0.04000002145767212
			length_socket_1.min_value = 0.009999999776482582
			length_socket_1.max_value = 3.4028234663852886e+38
			length_socket_1.subtype = 'DISTANCE'
			length_socket_1.attribute_domain = 'POINT'
			
			#Socket Offset
			offset_socket_2 = mn_utils_helix.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket_2.default_value = 2
			offset_socket_2.min_value = -2147483648
			offset_socket_2.max_value = 2147483647
			offset_socket_2.subtype = 'NONE'
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

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "MN_utils_helix", type = 'NODES')
		mod.node_group = mn_utils_helix
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(MN_utils_helix.bl_idname)
			
def register():
	bpy.utils.register_class(MN_utils_helix)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(MN_utils_helix)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
