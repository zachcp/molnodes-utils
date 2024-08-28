bl_info = {
	"name" : "Boolean Run Mask",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Boolean_Run_Mask(bpy.types.Operator):
	bl_idname = "node.boolean_run_mask"
	bl_label = "Boolean Run Mask"
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

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Boolean Run Mask", type = 'NODES')
		mod.node_group = boolean_run_mask
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Boolean_Run_Mask.bl_idname)
			
def register():
	bpy.utils.register_class(Boolean_Run_Mask)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Boolean_Run_Mask)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
