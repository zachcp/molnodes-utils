bl_info = {
	"name" : "Between Integer",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Between_Integer(bpy.types.Operator):
	bl_idname = "node.between_integer"
	bl_label = "Between Integer"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize between_integer node group
		def between_integer_node_group():
			between_integer = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Between Integer")

			between_integer.color_tag = 'CONVERTER'
			between_integer.description = ""

			
			#between_integer interface
			#Socket Boolean
			boolean_socket = between_integer.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket = between_integer.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketInt')
			value_socket.subtype = 'NONE'
			value_socket.default_value = 0
			value_socket.min_value = -2147483648
			value_socket.max_value = 2147483647
			value_socket.attribute_domain = 'POINT'
			
			#Socket Lower
			lower_socket = between_integer.interface.new_socket(name = "Lower", in_out='INPUT', socket_type = 'NodeSocketInt')
			lower_socket.subtype = 'NONE'
			lower_socket.default_value = 0
			lower_socket.min_value = -2147483648
			lower_socket.max_value = 2147483647
			lower_socket.attribute_domain = 'POINT'
			
			#Socket Upper
			upper_socket = between_integer.interface.new_socket(name = "Upper", in_out='INPUT', socket_type = 'NodeSocketInt')
			upper_socket.subtype = 'NONE'
			upper_socket.default_value = 19
			upper_socket.min_value = -2147483648
			upper_socket.max_value = 2147483647
			upper_socket.attribute_domain = 'POINT'
			
			
			#initialize between_integer nodes
			#node Group Output
			group_output = between_integer.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = between_integer.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Compare
			compare = between_integer.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'LESS_EQUAL'
			
			#node Compare.001
			compare_001 = between_integer.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'INT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'GREATER_EQUAL'
			
			#node Boolean Math
			boolean_math = between_integer.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'AND'
			
			
			
			
			#Set locations
			group_output.location = (270.0, 0.0)
			group_input.location = (-280.0, 0.0)
			compare.location = (-80.0, -80.0)
			compare_001.location = (-80.0, 80.0)
			boolean_math.location = (80.0, 80.0)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			
			#initialize between_integer links
			#compare.Result -> boolean_math.Boolean
			between_integer.links.new(compare.outputs[0], boolean_math.inputs[1])
			#compare_001.Result -> boolean_math.Boolean
			between_integer.links.new(compare_001.outputs[0], boolean_math.inputs[0])
			#group_input.Value -> compare.A
			between_integer.links.new(group_input.outputs[0], compare.inputs[2])
			#group_input.Value -> compare_001.A
			between_integer.links.new(group_input.outputs[0], compare_001.inputs[2])
			#boolean_math.Boolean -> group_output.Boolean
			between_integer.links.new(boolean_math.outputs[0], group_output.inputs[0])
			#group_input.Lower -> compare_001.B
			between_integer.links.new(group_input.outputs[1], compare_001.inputs[3])
			#group_input.Upper -> compare.B
			between_integer.links.new(group_input.outputs[2], compare.inputs[3])
			return between_integer

		between_integer = between_integer_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Between Integer", type = 'NODES')
		mod.node_group = between_integer
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Between_Integer.bl_idname)
			
def register():
	bpy.utils.register_class(Between_Integer)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Between_Integer)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
