bl_info = {
	"name" : "MN_utils_curve_resample",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class MN_utils_curve_resample(bpy.types.Operator):
	bl_idname = "node.mn_utils_curve_resample"
	bl_label = "MN_utils_curve_resample"
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

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "MN_utils_curve_resample", type = 'NODES')
		mod.node_group = mn_utils_curve_resample
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(MN_utils_curve_resample.bl_idname)
			
def register():
	bpy.utils.register_class(MN_utils_curve_resample)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(MN_utils_curve_resample)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
