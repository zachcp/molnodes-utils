bl_info = {
	"name" : "Select Res ID Range",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Select_Res_ID_Range(bpy.types.Operator):
	bl_idname = "node.select_res_id_range"
	bl_label = "Select Res ID Range"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize select_res_id_range node group
		def select_res_id_range_node_group():
			select_res_id_range = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Select Res ID Range")

			select_res_id_range.color_tag = 'INPUT'
			select_res_id_range.description = ""

			
			#select_res_id_range interface
			#Socket Selection
			selection_socket = select_res_id_range.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket.default_value = False
			selection_socket.attribute_domain = 'POINT'
			selection_socket.description = "The calculated selection"
			
			#Socket Inverted
			inverted_socket = select_res_id_range.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket.default_value = False
			inverted_socket.attribute_domain = 'POINT'
			inverted_socket.description = "The inverse of the calculated selection"
			
			#Socket And
			and_socket = select_res_id_range.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket.default_value = True
			and_socket.attribute_domain = 'POINT'
			and_socket.hide_value = True
			
			#Socket Or
			or_socket = select_res_id_range.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket.default_value = False
			or_socket.attribute_domain = 'POINT'
			or_socket.hide_value = True
			
			#Panel Res ID
			res_id_panel = select_res_id_range.interface.new_panel("Res ID")
			#Socket Min
			min_socket = select_res_id_range.interface.new_socket(name = "Min", in_out='INPUT', socket_type = 'NodeSocketInt', parent = res_id_panel)
			min_socket.default_value = 10
			min_socket.min_value = 0
			min_socket.max_value = 2147483647
			min_socket.subtype = 'NONE'
			min_socket.attribute_domain = 'POINT'
			min_socket.description = "Minimum of a `res_id` range selection"
			
			#Socket Max
			max_socket = select_res_id_range.interface.new_socket(name = "Max", in_out='INPUT', socket_type = 'NodeSocketInt', parent = res_id_panel)
			max_socket.default_value = 100
			max_socket.min_value = 1
			max_socket.max_value = 2147483647
			max_socket.subtype = 'NONE'
			max_socket.attribute_domain = 'POINT'
			max_socket.description = "Maximum of a `res_id` range selection"
			
			
			
			#initialize select_res_id_range nodes
			#node Named Attribute
			named_attribute = select_res_id_range.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'INT'
			#Name
			named_attribute.inputs[0].default_value = "res_id"
			
			#node Boolean Math.001
			boolean_math_001 = select_res_id_range.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001.name = "Boolean Math.001"
			boolean_math_001.operation = 'AND'
			
			#node Compare
			compare = select_res_id_range.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'GREATER_EQUAL'
			
			#node Compare.001
			compare_001 = select_res_id_range.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'INT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'LESS_EQUAL'
			
			#node Group Input
			group_input = select_res_id_range.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			group_input.outputs[0].hide = True
			
			#node Boolean Math
			boolean_math = select_res_id_range.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'NOT'
			
			#node Group Output
			group_output = select_res_id_range.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Reroute
			reroute = select_res_id_range.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Boolean Math.002
			boolean_math_002 = select_res_id_range.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002.name = "Boolean Math.002"
			boolean_math_002.operation = 'AND'
			
			#node Group Input.001
			group_input_001 = select_res_id_range.nodes.new("NodeGroupInput")
			group_input_001.name = "Group Input.001"
			group_input_001.outputs[2].hide = True
			group_input_001.outputs[3].hide = True
			group_input_001.outputs[4].hide = True
			
			#node Boolean Math.003
			boolean_math_003 = select_res_id_range.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003.name = "Boolean Math.003"
			boolean_math_003.operation = 'OR'
			
			
			
			
			#Set locations
			named_attribute.location = (-607.6740112304688, 0.0)
			boolean_math_001.location = (-287.6739807128906, 0.0)
			compare.location = (-447.6739807128906, 0.0)
			compare_001.location = (-447.6739807128906, -160.0)
			group_input.location = (-667.6740112304688, -120.0)
			boolean_math.location = (307.6740417480469, -100.0)
			group_output.location = (467.67401123046875, -20.0)
			reroute.location = (248.0, -69.88695526123047)
			boolean_math_002.location = (-120.0, 0.0)
			group_input_001.location = (-280.0, 100.0)
			boolean_math_003.location = (40.0, 0.0)
			
			#Set dimensions
			named_attribute.width, named_attribute.height = 140.0, 100.0
			boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			boolean_math_002.width, boolean_math_002.height = 140.0, 100.0
			group_input_001.width, group_input_001.height = 140.0, 100.0
			boolean_math_003.width, boolean_math_003.height = 140.0, 100.0
			
			#initialize select_res_id_range links
			#named_attribute.Attribute -> compare.A
			select_res_id_range.links.new(named_attribute.outputs[0], compare.inputs[2])
			#reroute.Output -> boolean_math.Boolean
			select_res_id_range.links.new(reroute.outputs[0], boolean_math.inputs[0])
			#group_input.Min -> compare.B
			select_res_id_range.links.new(group_input.outputs[2], compare.inputs[3])
			#reroute.Output -> group_output.Selection
			select_res_id_range.links.new(reroute.outputs[0], group_output.inputs[0])
			#boolean_math.Boolean -> group_output.Inverted
			select_res_id_range.links.new(boolean_math.outputs[0], group_output.inputs[1])
			#compare.Result -> boolean_math_001.Boolean
			select_res_id_range.links.new(compare.outputs[0], boolean_math_001.inputs[0])
			#named_attribute.Attribute -> compare_001.A
			select_res_id_range.links.new(named_attribute.outputs[0], compare_001.inputs[2])
			#group_input.Max -> compare_001.B
			select_res_id_range.links.new(group_input.outputs[3], compare_001.inputs[3])
			#compare_001.Result -> boolean_math_001.Boolean
			select_res_id_range.links.new(compare_001.outputs[0], boolean_math_001.inputs[1])
			#boolean_math_003.Boolean -> reroute.Input
			select_res_id_range.links.new(boolean_math_003.outputs[0], reroute.inputs[0])
			#boolean_math_001.Boolean -> boolean_math_002.Boolean
			select_res_id_range.links.new(boolean_math_001.outputs[0], boolean_math_002.inputs[1])
			#group_input_001.And -> boolean_math_002.Boolean
			select_res_id_range.links.new(group_input_001.outputs[0], boolean_math_002.inputs[0])
			#boolean_math_002.Boolean -> boolean_math_003.Boolean
			select_res_id_range.links.new(boolean_math_002.outputs[0], boolean_math_003.inputs[0])
			#group_input_001.Or -> boolean_math_003.Boolean
			select_res_id_range.links.new(group_input_001.outputs[1], boolean_math_003.inputs[1])
			return select_res_id_range

		select_res_id_range = select_res_id_range_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Select Res ID Range", type = 'NODES')
		mod.node_group = select_res_id_range
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Select_Res_ID_Range.bl_idname)
			
def register():
	bpy.utils.register_class(Select_Res_ID_Range)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Select_Res_ID_Range)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
