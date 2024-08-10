bl_info = {
	"name" : "Boolean Run Fill",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Boolean_Run_Fill(bpy.types.Operator):
	bl_idname = "node.boolean_run_fill"
	bl_label = "Boolean Run Fill"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize boolean_run_fill node group
		def boolean_run_fill_node_group():
			boolean_run_fill = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Boolean Run Fill")

			boolean_run_fill.color_tag = 'CONVERTER'
			boolean_run_fill.description = ""

			
			#boolean_run_fill interface
			#Socket Boolean
			boolean_socket = boolean_run_fill.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket.attribute_domain = 'POINT'
			
			#Socket Boolean
			boolean_socket_1 = boolean_run_fill.interface.new_socket(name = "Boolean", in_out='INPUT', socket_type = 'NodeSocketBool')
			boolean_socket_1.attribute_domain = 'POINT'
			boolean_socket_1.description = "Boolean array to fill runs of False"
			
			#Socket Fill Size
			fill_size_socket = boolean_run_fill.interface.new_socket(name = "Fill Size", in_out='INPUT', socket_type = 'NodeSocketInt')
			fill_size_socket.subtype = 'NONE'
			fill_size_socket.default_value = 3
			fill_size_socket.min_value = -2147483648
			fill_size_socket.max_value = 2147483647
			fill_size_socket.attribute_domain = 'POINT'
			fill_size_socket.description = "Set a run of False to True if length equal or less than Fill Size"
			
			
			#initialize boolean_run_fill nodes
			#node Group Output
			group_output = boolean_run_fill.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = boolean_run_fill.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Accumulate Field
			accumulate_field = boolean_run_fill.nodes.new("GeometryNodeAccumulateField")
			accumulate_field.name = "Accumulate Field"
			accumulate_field.data_type = 'INT'
			accumulate_field.domain = 'POINT'
			#Group Index
			accumulate_field.inputs[1].default_value = 0
			
			#node Accumulate Field.001
			accumulate_field_001 = boolean_run_fill.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_001.name = "Accumulate Field.001"
			accumulate_field_001.data_type = 'INT'
			accumulate_field_001.domain = 'POINT'
			#Value
			accumulate_field_001.inputs[0].default_value = 1
			
			#node Compare
			compare = boolean_run_fill.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'LESS_EQUAL'
			
			#node Compare.001
			compare_001 = boolean_run_fill.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'INT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'LESS_EQUAL'
			
			#node Boolean Math.010
			boolean_math_010 = boolean_run_fill.nodes.new("FunctionNodeBooleanMath")
			boolean_math_010.name = "Boolean Math.010"
			boolean_math_010.operation = 'AND'
			
			#node Boolean Math
			boolean_math = boolean_run_fill.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'OR'
			
			#node Reroute
			reroute = boolean_run_fill.nodes.new("NodeReroute")
			reroute.name = "Reroute"
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
			group_output.location = (430.0, 0.0)
			group_input.location = (-480.0, -20.0)
			accumulate_field.location = (-220.0, -120.0)
			accumulate_field_001.location = (-60.0, -120.0)
			compare.location = (100.0, -120.0)
			compare_001.location = (100.0, -280.0)
			boolean_math_010.location = (260.0, -120.0)
			boolean_math.location = (260.0, 20.0)
			reroute.location = (60.0, -380.0)
			reroute_001.location = (-280.0, -380.0)
			reroute_003.location = (-300.0, -80.0)
			reroute_002.location = (-240.0, -60.0)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			accumulate_field.width, accumulate_field.height = 140.0, 100.0
			accumulate_field_001.width, accumulate_field_001.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			boolean_math_010.width, boolean_math_010.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			reroute_003.width, reroute_003.height = 16.0, 100.0
			reroute_002.width, reroute_002.height = 16.0, 100.0
			
			#initialize boolean_run_fill links
			#accumulate_field_001.Trailing -> compare.A
			boolean_run_fill.links.new(accumulate_field_001.outputs[1], compare.inputs[2])
			#accumulate_field.Leading -> accumulate_field_001.Group ID
			boolean_run_fill.links.new(accumulate_field.outputs[0], accumulate_field_001.inputs[1])
			#compare_001.Result -> boolean_math_010.Boolean
			boolean_run_fill.links.new(compare_001.outputs[0], boolean_math_010.inputs[1])
			#compare.Result -> boolean_math_010.Boolean
			boolean_run_fill.links.new(compare.outputs[0], boolean_math_010.inputs[0])
			#accumulate_field_001.Total -> compare_001.A
			boolean_run_fill.links.new(accumulate_field_001.outputs[2], compare_001.inputs[2])
			#reroute.Output -> compare.B
			boolean_run_fill.links.new(reroute.outputs[0], compare.inputs[3])
			#reroute.Output -> compare_001.B
			boolean_run_fill.links.new(reroute.outputs[0], compare_001.inputs[3])
			#reroute_002.Output -> accumulate_field.Value
			boolean_run_fill.links.new(reroute_002.outputs[0], accumulate_field.inputs[0])
			#reroute_002.Output -> boolean_math.Boolean
			boolean_run_fill.links.new(reroute_002.outputs[0], boolean_math.inputs[0])
			#boolean_math_010.Boolean -> boolean_math.Boolean
			boolean_run_fill.links.new(boolean_math_010.outputs[0], boolean_math.inputs[1])
			#boolean_math.Boolean -> group_output.Boolean
			boolean_run_fill.links.new(boolean_math.outputs[0], group_output.inputs[0])
			#reroute_001.Output -> reroute.Input
			boolean_run_fill.links.new(reroute_001.outputs[0], reroute.inputs[0])
			#reroute_003.Output -> reroute_001.Input
			boolean_run_fill.links.new(reroute_003.outputs[0], reroute_001.inputs[0])
			#group_input.Fill Size -> reroute_003.Input
			boolean_run_fill.links.new(group_input.outputs[1], reroute_003.inputs[0])
			#group_input.Boolean -> reroute_002.Input
			boolean_run_fill.links.new(group_input.outputs[0], reroute_002.inputs[0])
			return boolean_run_fill

		boolean_run_fill = boolean_run_fill_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Boolean Run Fill", type = 'NODES')
		mod.node_group = boolean_run_fill
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Boolean_Run_Fill.bl_idname)
			
def register():
	bpy.utils.register_class(Boolean_Run_Fill)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Boolean_Run_Fill)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
