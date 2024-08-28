bl_info = {
	"name" : ".sec_struct_counter",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _sec_struct_counter(bpy.types.Operator):
	bl_idname = "node._sec_struct_counter"
	bl_label = ".sec_struct_counter"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _field_offset node group
		def _field_offset_node_group():
			_field_offset = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".field_offset")

			_field_offset.color_tag = 'NONE'
			_field_offset.description = ""

			
			#_field_offset interface
			#Socket Field
			field_socket = _field_offset.interface.new_socket(name = "Field", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			field_socket.default_value = (0.0, 0.0, 0.0)
			field_socket.min_value = -3.4028234663852886e+38
			field_socket.max_value = 3.4028234663852886e+38
			field_socket.subtype = 'NONE'
			field_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket = _field_offset.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			value_socket.default_value = False
			value_socket.attribute_domain = 'POINT'
			
			#Socket Field
			field_socket_1 = _field_offset.interface.new_socket(name = "Field", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			field_socket_1.default_value = 0
			field_socket_1.min_value = -2147483648
			field_socket_1.max_value = 2147483647
			field_socket_1.subtype = 'NONE'
			field_socket_1.attribute_domain = 'POINT'
			
			#Socket Field
			field_socket_2 = _field_offset.interface.new_socket(name = "Field", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			field_socket_2.default_value = 0.0
			field_socket_2.min_value = -3.4028234663852886e+38
			field_socket_2.max_value = 3.4028234663852886e+38
			field_socket_2.subtype = 'NONE'
			field_socket_2.attribute_domain = 'POINT'
			
			#Socket Field
			field_socket_3 = _field_offset.interface.new_socket(name = "Field", in_out='INPUT', socket_type = 'NodeSocketVector')
			field_socket_3.default_value = (0.0, 0.0, 0.0)
			field_socket_3.min_value = -3.4028234663852886e+38
			field_socket_3.max_value = 3.4028234663852886e+38
			field_socket_3.subtype = 'NONE'
			field_socket_3.attribute_domain = 'POINT'
			field_socket_3.hide_value = True
			
			#Socket Value
			value_socket_1 = _field_offset.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketBool')
			value_socket_1.default_value = False
			value_socket_1.attribute_domain = 'POINT'
			value_socket_1.hide_value = True
			
			#Socket Field
			field_socket_4 = _field_offset.interface.new_socket(name = "Field", in_out='INPUT', socket_type = 'NodeSocketInt')
			field_socket_4.default_value = 0
			field_socket_4.min_value = -2147483648
			field_socket_4.max_value = 2147483647
			field_socket_4.subtype = 'NONE'
			field_socket_4.attribute_domain = 'POINT'
			field_socket_4.hide_value = True
			
			#Socket Field
			field_socket_5 = _field_offset.interface.new_socket(name = "Field", in_out='INPUT', socket_type = 'NodeSocketFloat')
			field_socket_5.default_value = 0.0
			field_socket_5.min_value = -3.4028234663852886e+38
			field_socket_5.max_value = 3.4028234663852886e+38
			field_socket_5.subtype = 'NONE'
			field_socket_5.attribute_domain = 'POINT'
			field_socket_5.hide_value = True
			
			#Socket Offset
			offset_socket = _field_offset.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket.default_value = 0
			offset_socket.min_value = -2147483648
			offset_socket.max_value = 2147483647
			offset_socket.subtype = 'NONE'
			offset_socket.attribute_domain = 'POINT'
			
			
			#initialize _field_offset nodes
			#node Group Output
			group_output = _field_offset.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Math.001
			math_001 = _field_offset.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.operation = 'ADD'
			math_001.use_clamp = False
			
			#node Evaluate at Index
			evaluate_at_index = _field_offset.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index.name = "Evaluate at Index"
			evaluate_at_index.data_type = 'FLOAT_VECTOR'
			evaluate_at_index.domain = 'POINT'
			
			#node Group Input
			group_input = _field_offset.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Evaluate at Index.001
			evaluate_at_index_001 = _field_offset.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001.name = "Evaluate at Index.001"
			evaluate_at_index_001.data_type = 'BOOLEAN'
			evaluate_at_index_001.domain = 'POINT'
			
			#node Index
			index = _field_offset.nodes.new("GeometryNodeInputIndex")
			index.name = "Index"
			
			#node Evaluate at Index.002
			evaluate_at_index_002 = _field_offset.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_002.name = "Evaluate at Index.002"
			evaluate_at_index_002.data_type = 'INT'
			evaluate_at_index_002.domain = 'POINT'
			
			#node Evaluate at Index.003
			evaluate_at_index_003 = _field_offset.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_003.name = "Evaluate at Index.003"
			evaluate_at_index_003.data_type = 'FLOAT'
			evaluate_at_index_003.domain = 'POINT'
			
			
			
			
			#Set locations
			group_output.location = (407.6440124511719, 0.0)
			math_001.location = (0.5235366821289062, 15.3753662109375)
			evaluate_at_index.location = (217.64404296875, 102.376708984375)
			group_input.location = (-417.64404296875, 0.0)
			evaluate_at_index_001.location = (220.0, -60.0)
			index.location = (-260.0, -40.0)
			evaluate_at_index_002.location = (220.0, -220.0)
			evaluate_at_index_003.location = (220.0, -380.0)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			evaluate_at_index.width, evaluate_at_index.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			evaluate_at_index_001.width, evaluate_at_index_001.height = 140.0, 100.0
			index.width, index.height = 140.0, 100.0
			evaluate_at_index_002.width, evaluate_at_index_002.height = 140.0, 100.0
			evaluate_at_index_003.width, evaluate_at_index_003.height = 140.0, 100.0
			
			#initialize _field_offset links
			#index.Index -> math_001.Value
			_field_offset.links.new(index.outputs[0], math_001.inputs[0])
			#math_001.Value -> evaluate_at_index.Index
			_field_offset.links.new(math_001.outputs[0], evaluate_at_index.inputs[0])
			#group_input.Field -> evaluate_at_index.Value
			_field_offset.links.new(group_input.outputs[0], evaluate_at_index.inputs[1])
			#group_input.Offset -> math_001.Value
			_field_offset.links.new(group_input.outputs[4], math_001.inputs[1])
			#evaluate_at_index.Value -> group_output.Field
			_field_offset.links.new(evaluate_at_index.outputs[0], group_output.inputs[0])
			#math_001.Value -> evaluate_at_index_001.Index
			_field_offset.links.new(math_001.outputs[0], evaluate_at_index_001.inputs[0])
			#group_input.Value -> evaluate_at_index_001.Value
			_field_offset.links.new(group_input.outputs[1], evaluate_at_index_001.inputs[1])
			#evaluate_at_index_001.Value -> group_output.Value
			_field_offset.links.new(evaluate_at_index_001.outputs[0], group_output.inputs[1])
			#math_001.Value -> evaluate_at_index_002.Index
			_field_offset.links.new(math_001.outputs[0], evaluate_at_index_002.inputs[0])
			#group_input.Field -> evaluate_at_index_002.Value
			_field_offset.links.new(group_input.outputs[2], evaluate_at_index_002.inputs[1])
			#evaluate_at_index_002.Value -> group_output.Field
			_field_offset.links.new(evaluate_at_index_002.outputs[0], group_output.inputs[2])
			#math_001.Value -> evaluate_at_index_003.Index
			_field_offset.links.new(math_001.outputs[0], evaluate_at_index_003.inputs[0])
			#group_input.Field -> evaluate_at_index_003.Value
			_field_offset.links.new(group_input.outputs[3], evaluate_at_index_003.inputs[1])
			#evaluate_at_index_003.Value -> group_output.Field
			_field_offset.links.new(evaluate_at_index_003.outputs[0], group_output.inputs[3])
			return _field_offset

		_field_offset = _field_offset_node_group()

		#initialize _sec_struct_counter node group
		def _sec_struct_counter_node_group():
			_sec_struct_counter = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".sec_struct_counter")

			_sec_struct_counter.color_tag = 'NONE'
			_sec_struct_counter.description = ""

			
			#_sec_struct_counter interface
			#Socket Leading
			leading_socket = _sec_struct_counter.interface.new_socket(name = "Leading", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			leading_socket.default_value = 0
			leading_socket.min_value = -2147483648
			leading_socket.max_value = 2147483647
			leading_socket.subtype = 'NONE'
			leading_socket.attribute_domain = 'POINT'
			
			#Socket Trailing
			trailing_socket = _sec_struct_counter.interface.new_socket(name = "Trailing", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			trailing_socket.default_value = 0
			trailing_socket.min_value = -2147483648
			trailing_socket.max_value = 2147483647
			trailing_socket.subtype = 'NONE'
			trailing_socket.attribute_domain = 'POINT'
			
			#Socket Total
			total_socket = _sec_struct_counter.interface.new_socket(name = "Total", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			total_socket.default_value = 0
			total_socket.min_value = -2147483648
			total_socket.max_value = 2147483647
			total_socket.subtype = 'NONE'
			total_socket.attribute_domain = 'POINT'
			
			#Socket Border
			border_socket = _sec_struct_counter.interface.new_socket(name = "Border", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			border_socket.default_value = False
			border_socket.attribute_domain = 'POINT'
			
			
			#initialize _sec_struct_counter nodes
			#node Group Input
			group_input_1 = _sec_struct_counter.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			
			#node Reroute.005
			reroute_005 = _sec_struct_counter.nodes.new("NodeReroute")
			reroute_005.name = "Reroute.005"
			#node Named Attribute.001
			named_attribute_001 = _sec_struct_counter.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.data_type = 'INT'
			#Name
			named_attribute_001.inputs[0].default_value = "sec_struct"
			
			#node Group.004
			group_004 = _sec_struct_counter.nodes.new("GeometryNodeGroup")
			group_004.name = "Group.004"
			group_004.node_tree = _field_offset
			#Input_0
			group_004.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Input_3
			group_004.inputs[1].default_value = False
			#Input_7
			group_004.inputs[3].default_value = 0.0
			#Input_1
			group_004.inputs[4].default_value = -1
			
			#node Compare.009
			compare_009 = _sec_struct_counter.nodes.new("FunctionNodeCompare")
			compare_009.name = "Compare.009"
			compare_009.data_type = 'INT'
			compare_009.mode = 'ELEMENT'
			compare_009.operation = 'NOT_EQUAL'
			
			#node Accumulate Field.004
			accumulate_field_004 = _sec_struct_counter.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_004.name = "Accumulate Field.004"
			accumulate_field_004.data_type = 'INT'
			accumulate_field_004.domain = 'POINT'
			#Group Index
			accumulate_field_004.inputs[1].default_value = 0
			
			#node Compare.010
			compare_010 = _sec_struct_counter.nodes.new("FunctionNodeCompare")
			compare_010.name = "Compare.010"
			compare_010.data_type = 'INT'
			compare_010.mode = 'ELEMENT'
			compare_010.operation = 'NOT_EQUAL'
			
			#node Reroute
			reroute = _sec_struct_counter.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Boolean Math
			boolean_math = _sec_struct_counter.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'OR'
			#Boolean_001
			boolean_math.inputs[1].default_value = False
			
			#node Group Output
			group_output_1 = _sec_struct_counter.nodes.new("NodeGroupOutput")
			group_output_1.name = "Group Output"
			group_output_1.is_active_output = True
			
			#node Group.003
			group_003 = _sec_struct_counter.nodes.new("GeometryNodeGroup")
			group_003.name = "Group.003"
			group_003.node_tree = _field_offset
			#Input_0
			group_003.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Input_3
			group_003.inputs[1].default_value = False
			#Input_7
			group_003.inputs[3].default_value = 0.0
			#Input_1
			group_003.inputs[4].default_value = 1
			
			
			
			
			#Set locations
			group_input_1.location = (-500.1279296875, 0.0)
			reroute_005.location = (-119.8720703125, -60.0)
			named_attribute_001.location = (-300.0, 120.0)
			group_004.location = (-20.0, -220.0)
			compare_009.location = (140.1279296875, 60.0)
			accumulate_field_004.location = (460.0, 40.0)
			compare_010.location = (140.0, -140.0)
			reroute.location = (320.0, -60.0)
			boolean_math.location = (300.0, -140.0)
			group_output_1.location = (796.4706420898438, 27.943008422851562)
			group_003.location = (-19.8720703125, 60.0)
			
			#Set dimensions
			group_input_1.width, group_input_1.height = 140.0, 100.0
			reroute_005.width, reroute_005.height = 16.0, 100.0
			named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
			group_004.width, group_004.height = 140.0, 100.0
			compare_009.width, compare_009.height = 140.0, 100.0
			accumulate_field_004.width, accumulate_field_004.height = 140.0, 100.0
			compare_010.width, compare_010.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			group_output_1.width, group_output_1.height = 140.0, 100.0
			group_003.width, group_003.height = 140.0, 100.0
			
			#initialize _sec_struct_counter links
			#reroute.Output -> accumulate_field_004.Value
			_sec_struct_counter.links.new(reroute.outputs[0], accumulate_field_004.inputs[0])
			#reroute_005.Output -> group_003.Field
			_sec_struct_counter.links.new(reroute_005.outputs[0], group_003.inputs[2])
			#reroute_005.Output -> compare_009.A
			_sec_struct_counter.links.new(reroute_005.outputs[0], compare_009.inputs[2])
			#named_attribute_001.Attribute -> reroute_005.Input
			_sec_struct_counter.links.new(named_attribute_001.outputs[0], reroute_005.inputs[0])
			#group_003.Field -> compare_009.B
			_sec_struct_counter.links.new(group_003.outputs[2], compare_009.inputs[3])
			#accumulate_field_004.Trailing -> group_output_1.Trailing
			_sec_struct_counter.links.new(accumulate_field_004.outputs[1], group_output_1.inputs[1])
			#accumulate_field_004.Leading -> group_output_1.Leading
			_sec_struct_counter.links.new(accumulate_field_004.outputs[0], group_output_1.inputs[0])
			#accumulate_field_004.Total -> group_output_1.Total
			_sec_struct_counter.links.new(accumulate_field_004.outputs[2], group_output_1.inputs[2])
			#reroute.Output -> group_output_1.Border
			_sec_struct_counter.links.new(reroute.outputs[0], group_output_1.inputs[3])
			#reroute_005.Output -> group_004.Field
			_sec_struct_counter.links.new(reroute_005.outputs[0], group_004.inputs[2])
			#reroute_005.Output -> compare_010.A
			_sec_struct_counter.links.new(reroute_005.outputs[0], compare_010.inputs[2])
			#group_004.Field -> compare_010.B
			_sec_struct_counter.links.new(group_004.outputs[2], compare_010.inputs[3])
			#compare_009.Result -> reroute.Input
			_sec_struct_counter.links.new(compare_009.outputs[0], reroute.inputs[0])
			#compare_010.Result -> boolean_math.Boolean
			_sec_struct_counter.links.new(compare_010.outputs[0], boolean_math.inputs[0])
			return _sec_struct_counter

		_sec_struct_counter = _sec_struct_counter_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".sec_struct_counter", type = 'NODES')
		mod.node_group = _sec_struct_counter
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_sec_struct_counter.bl_idname)
			
def register():
	bpy.utils.register_class(_sec_struct_counter)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_sec_struct_counter)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
