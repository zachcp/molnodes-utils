bl_info = {
	"name" : "Select Res ID_",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Select_Res_ID_(bpy.types.Operator):
	bl_idname = "node.select_res_id_"
	bl_label = "Select Res ID_"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize select_res_id_ node group
		def select_res_id__node_group():
			select_res_id_ = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Select Res ID_")

			select_res_id_.color_tag = 'INPUT'
			select_res_id_.description = ""

			
			#select_res_id_ interface
			#Socket Selection
			selection_socket = select_res_id_.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket.attribute_domain = 'POINT'
			selection_socket.description = "The calculated selection"
			
			#Socket Inverted
			inverted_socket = select_res_id_.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket.attribute_domain = 'POINT'
			inverted_socket.description = "The inverse of the calculated selection"
			
			#Socket res_id
			res_id_socket = select_res_id_.interface.new_socket(name = "res_id", in_out='INPUT', socket_type = 'NodeSocketInt')
			res_id_socket.subtype = 'NONE'
			res_id_socket.default_value = 10
			res_id_socket.min_value = 0
			res_id_socket.max_value = 2147483647
			res_id_socket.attribute_domain = 'POINT'
			res_id_socket.description = "A single `res_id` selection"
			
			#Socket res_id
			res_id_socket_1 = select_res_id_.interface.new_socket(name = "res_id", in_out='INPUT', socket_type = 'NodeSocketInt')
			res_id_socket_1.subtype = 'NONE'
			res_id_socket_1.default_value = 15
			res_id_socket_1.min_value = -2147483648
			res_id_socket_1.max_value = 2147483647
			res_id_socket_1.attribute_domain = 'POINT'
			res_id_socket_1.description = "A single `res_id` selection"
			
			#Socket res_id: Min
			res_id__min_socket = select_res_id_.interface.new_socket(name = "res_id: Min", in_out='INPUT', socket_type = 'NodeSocketInt')
			res_id__min_socket.subtype = 'NONE'
			res_id__min_socket.default_value = 20
			res_id__min_socket.min_value = -2147483648
			res_id__min_socket.max_value = 2147483647
			res_id__min_socket.attribute_domain = 'POINT'
			res_id__min_socket.description = "Minimum of a `res_id` range selection"
			
			#Socket res_id: Max
			res_id__max_socket = select_res_id_.interface.new_socket(name = "res_id: Max", in_out='INPUT', socket_type = 'NodeSocketInt')
			res_id__max_socket.subtype = 'NONE'
			res_id__max_socket.default_value = 100
			res_id__max_socket.min_value = 1
			res_id__max_socket.max_value = 2147483647
			res_id__max_socket.attribute_domain = 'POINT'
			res_id__max_socket.description = "Maximum of a `res_id` range selection"
			
			
			#initialize select_res_id_ nodes
			#node Named Attribute
			named_attribute = select_res_id_.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'INT'
			#Name
			named_attribute.inputs[0].default_value = "res_id"
			
			#node Boolean Math.001
			boolean_math_001 = select_res_id_.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001.name = "Boolean Math.001"
			boolean_math_001.operation = 'AND'
			
			#node Compare
			compare = select_res_id_.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'GREATER_EQUAL'
			
			#node Compare.001
			compare_001 = select_res_id_.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'INT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'LESS_EQUAL'
			
			#node Group Input
			group_input = select_res_id_.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Boolean Math
			boolean_math = select_res_id_.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'NOT'
			
			#node Group Output
			group_output = select_res_id_.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			
			
			
			#Set locations
			named_attribute.location = (-360.0, 0.0)
			boolean_math_001.location = (20.0, -21.7943115234375)
			compare.location = (-200.0, 0.0)
			compare_001.location = (-200.0, -160.0)
			group_input.location = (-360.0, -140.0)
			boolean_math.location = (220.0, -100.0)
			group_output.location = (380.0, -20.0)
			
			#Set dimensions
			named_attribute.width, named_attribute.height = 140.0, 100.0
			boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			
			#initialize select_res_id_ links
			#named_attribute.Attribute -> compare.A
			select_res_id_.links.new(named_attribute.outputs[0], compare.inputs[2])
			#boolean_math_001.Boolean -> boolean_math.Boolean
			select_res_id_.links.new(boolean_math_001.outputs[0], boolean_math.inputs[0])
			#group_input.res_id -> compare.B
			select_res_id_.links.new(group_input.outputs[0], compare.inputs[3])
			#boolean_math_001.Boolean -> group_output.Selection
			select_res_id_.links.new(boolean_math_001.outputs[0], group_output.inputs[0])
			#boolean_math.Boolean -> group_output.Inverted
			select_res_id_.links.new(boolean_math.outputs[0], group_output.inputs[1])
			#compare.Result -> boolean_math_001.Boolean
			select_res_id_.links.new(compare.outputs[0], boolean_math_001.inputs[0])
			#named_attribute.Attribute -> compare_001.A
			select_res_id_.links.new(named_attribute.outputs[0], compare_001.inputs[2])
			#group_input.res_id: Max -> compare_001.B
			select_res_id_.links.new(group_input.outputs[3], compare_001.inputs[3])
			#compare_001.Result -> boolean_math_001.Boolean
			select_res_id_.links.new(compare_001.outputs[0], boolean_math_001.inputs[1])
			return select_res_id_

		select_res_id_ = select_res_id__node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Select Res ID_", type = 'NODES')
		mod.node_group = select_res_id_
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Select_Res_ID_.bl_idname)
			
def register():
	bpy.utils.register_class(Select_Res_ID_)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Select_Res_ID_)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
