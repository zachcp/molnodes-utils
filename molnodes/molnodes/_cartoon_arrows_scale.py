bl_info = {
	"name" : ".cartoon_arrows_scale",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _cartoon_arrows_scale(bpy.types.Operator):
	bl_idname = "node._cartoon_arrows_scale"
	bl_label = ".cartoon_arrows_scale"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _cartoon_arrows_scale node group
		def _cartoon_arrows_scale_node_group():
			_cartoon_arrows_scale = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".cartoon_arrows_scale")

			_cartoon_arrows_scale.color_tag = 'NONE'
			_cartoon_arrows_scale.description = ""

			
			#_cartoon_arrows_scale interface
			#Socket Result
			result_socket = _cartoon_arrows_scale.interface.new_socket(name = "Result", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			result_socket.attribute_domain = 'POINT'
			
			#Socket Output
			output_socket = _cartoon_arrows_scale.interface.new_socket(name = "Output", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			output_socket.subtype = 'NONE'
			output_socket.default_value = 0.0
			output_socket.min_value = -3.4028234663852886e+38
			output_socket.max_value = 3.4028234663852886e+38
			output_socket.attribute_domain = 'POINT'
			
			#Socket Input
			input_socket = _cartoon_arrows_scale.interface.new_socket(name = "Input", in_out='INPUT', socket_type = 'NodeSocketFloat')
			input_socket.subtype = 'NONE'
			input_socket.default_value = 0.0
			input_socket.min_value = -3.4028234663852886e+38
			input_socket.max_value = 3.4028234663852886e+38
			input_socket.attribute_domain = 'POINT'
			
			#Socket Input
			input_socket_1 = _cartoon_arrows_scale.interface.new_socket(name = "Input", in_out='INPUT', socket_type = 'NodeSocketFloat')
			input_socket_1.subtype = 'NONE'
			input_socket_1.default_value = 0.0
			input_socket_1.min_value = -3.4028234663852886e+38
			input_socket_1.max_value = 3.4028234663852886e+38
			input_socket_1.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket = _cartoon_arrows_scale.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket.subtype = 'NONE'
			value_socket.default_value = 2.8499999046325684
			value_socket.min_value = -10000.0
			value_socket.max_value = 10000.0
			value_socket.attribute_domain = 'POINT'
			
			
			#initialize _cartoon_arrows_scale nodes
			#node Group Output
			group_output = _cartoon_arrows_scale.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Math.006
			math_006 = _cartoon_arrows_scale.nodes.new("ShaderNodeMath")
			math_006.name = "Math.006"
			math_006.hide = True
			math_006.operation = 'MAXIMUM'
			math_006.use_clamp = False
			#Value_001
			math_006.inputs[1].default_value = 0.0
			
			#node Spline Parameter
			spline_parameter = _cartoon_arrows_scale.nodes.new("GeometryNodeSplineParameter")
			spline_parameter.name = "Spline Parameter"
			
			#node Map Range
			map_range = _cartoon_arrows_scale.nodes.new("ShaderNodeMapRange")
			map_range.name = "Map Range"
			map_range.clamp = True
			map_range.data_type = 'FLOAT'
			map_range.interpolation_type = 'LINEAR'
			
			#node Math.003
			math_003 = _cartoon_arrows_scale.nodes.new("ShaderNodeMath")
			math_003.name = "Math.003"
			math_003.operation = 'SUBTRACT'
			math_003.use_clamp = False
			
			#node Reroute.001
			reroute_001 = _cartoon_arrows_scale.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			#node Reroute.010
			reroute_010 = _cartoon_arrows_scale.nodes.new("NodeReroute")
			reroute_010.name = "Reroute.010"
			#node Switch.001
			switch_001 = _cartoon_arrows_scale.nodes.new("GeometryNodeSwitch")
			switch_001.name = "Switch.001"
			switch_001.input_type = 'FLOAT'
			
			#node Reroute
			reroute = _cartoon_arrows_scale.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Spline Length
			spline_length = _cartoon_arrows_scale.nodes.new("GeometryNodeSplineLength")
			spline_length.name = "Spline Length"
			
			#node Group Input
			group_input = _cartoon_arrows_scale.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Math.007
			math_007 = _cartoon_arrows_scale.nodes.new("ShaderNodeMath")
			math_007.name = "Math.007"
			math_007.operation = 'DIVIDE'
			math_007.use_clamp = False
			#Value_001
			math_007.inputs[1].default_value = 100.0
			
			#node Map Range.001
			map_range_001 = _cartoon_arrows_scale.nodes.new("ShaderNodeMapRange")
			map_range_001.name = "Map Range.001"
			map_range_001.clamp = True
			map_range_001.data_type = 'FLOAT'
			map_range_001.interpolation_type = 'LINEAR'
			#To Max
			map_range_001.inputs[4].default_value = 0.0
			
			#node Compare.001
			compare_001 = _cartoon_arrows_scale.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'FLOAT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'EQUAL'
			#Epsilon
			compare_001.inputs[12].default_value = 0.0010000000474974513
			
			#node Math.008
			math_008 = _cartoon_arrows_scale.nodes.new("ShaderNodeMath")
			math_008.name = "Math.008"
			math_008.operation = 'MULTIPLY'
			math_008.use_clamp = False
			#Value_001
			math_008.inputs[1].default_value = 2.0
			
			
			
			
			#Set locations
			group_output.location = (670.39453125, 0.0)
			math_006.location = (-283.53955078125, 120.8475341796875)
			spline_parameter.location = (-283.53955078125, 240.8475341796875)
			map_range.location = (-43.53955078125, 140.8475341796875)
			math_003.location = (-283.53955078125, 80.8475341796875)
			reroute_001.location = (-128.9521484375, -162.76467895507812)
			reroute_010.location = (120.39453125, -104.70928955078125)
			switch_001.location = (480.39453125, -44.70928955078125)
			reroute.location = (-126.4767837524414, -251.35455322265625)
			spline_length.location = (-480.0, 100.0)
			group_input.location = (-700.0, -200.0)
			math_007.location = (-480.0, 20.0)
			map_range_001.location = (160.0, 60.0)
			compare_001.location = (160.0, 240.0)
			math_008.location = (-80.0, -140.0)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			math_006.width, math_006.height = 140.0, 100.0
			spline_parameter.width, spline_parameter.height = 140.0, 100.0
			map_range.width, map_range.height = 140.0, 100.0
			math_003.width, math_003.height = 140.0, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			reroute_010.width, reroute_010.height = 16.0, 100.0
			switch_001.width, switch_001.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			spline_length.width, spline_length.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			math_007.width, math_007.height = 140.0, 100.0
			map_range_001.width, map_range_001.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			math_008.width, math_008.height = 140.0, 100.0
			
			#initialize _cartoon_arrows_scale links
			#spline_parameter.Length -> map_range.Value
			_cartoon_arrows_scale.links.new(spline_parameter.outputs[1], map_range.inputs[0])
			#reroute_001.Output -> map_range.To Min
			_cartoon_arrows_scale.links.new(reroute_001.outputs[0], map_range.inputs[3])
			#spline_length.Length -> map_range.From Max
			_cartoon_arrows_scale.links.new(spline_length.outputs[0], map_range.inputs[2])
			#map_range.Result -> map_range_001.Value
			_cartoon_arrows_scale.links.new(map_range.outputs[0], map_range_001.inputs[0])
			#map_range_001.Result -> switch_001.False
			_cartoon_arrows_scale.links.new(map_range_001.outputs[0], switch_001.inputs[1])
			#math_006.Value -> map_range.From Min
			_cartoon_arrows_scale.links.new(math_006.outputs[0], map_range.inputs[1])
			#map_range.Result -> compare_001.A
			_cartoon_arrows_scale.links.new(map_range.outputs[0], compare_001.inputs[0])
			#math_007.Value -> math_003.Value
			_cartoon_arrows_scale.links.new(math_007.outputs[0], math_003.inputs[1])
			#reroute.Output -> map_range_001.From Max
			_cartoon_arrows_scale.links.new(reroute.outputs[0], map_range_001.inputs[2])
			#reroute_001.Output -> reroute_010.Input
			_cartoon_arrows_scale.links.new(reroute_001.outputs[0], reroute_010.inputs[0])
			#reroute_010.Output -> map_range_001.From Min
			_cartoon_arrows_scale.links.new(reroute_010.outputs[0], map_range_001.inputs[1])
			#reroute_001.Output -> math_008.Value
			_cartoon_arrows_scale.links.new(reroute_001.outputs[0], math_008.inputs[0])
			#reroute_010.Output -> compare_001.B
			_cartoon_arrows_scale.links.new(reroute_010.outputs[0], compare_001.inputs[1])
			#compare_001.Result -> switch_001.Switch
			_cartoon_arrows_scale.links.new(compare_001.outputs[0], switch_001.inputs[0])
			#reroute_010.Output -> switch_001.True
			_cartoon_arrows_scale.links.new(reroute_010.outputs[0], switch_001.inputs[2])
			#math_003.Value -> math_006.Value
			_cartoon_arrows_scale.links.new(math_003.outputs[0], math_006.inputs[0])
			#reroute.Output -> map_range.To Max
			_cartoon_arrows_scale.links.new(reroute.outputs[0], map_range.inputs[4])
			#math_008.Value -> map_range_001.To Min
			_cartoon_arrows_scale.links.new(math_008.outputs[0], map_range_001.inputs[3])
			#spline_length.Length -> math_003.Value
			_cartoon_arrows_scale.links.new(spline_length.outputs[0], math_003.inputs[0])
			#compare_001.Result -> group_output.Result
			_cartoon_arrows_scale.links.new(compare_001.outputs[0], group_output.inputs[0])
			#switch_001.Output -> group_output.Output
			_cartoon_arrows_scale.links.new(switch_001.outputs[0], group_output.inputs[1])
			#group_input.Input -> reroute_001.Input
			_cartoon_arrows_scale.links.new(group_input.outputs[0], reroute_001.inputs[0])
			#group_input.Input -> reroute.Input
			_cartoon_arrows_scale.links.new(group_input.outputs[1], reroute.inputs[0])
			#group_input.Value -> math_007.Value
			_cartoon_arrows_scale.links.new(group_input.outputs[2], math_007.inputs[0])
			return _cartoon_arrows_scale

		_cartoon_arrows_scale = _cartoon_arrows_scale_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".cartoon_arrows_scale", type = 'NODES')
		mod.node_group = _cartoon_arrows_scale
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_cartoon_arrows_scale.bl_idname)
			
def register():
	bpy.utils.register_class(_cartoon_arrows_scale)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_cartoon_arrows_scale)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
