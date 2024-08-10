bl_info = {
	"name" : "Between Vector",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Between_Vector(bpy.types.Operator):
	bl_idname = "node.between_vector"
	bl_label = "Between Vector"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize between_vector node group
		def between_vector_node_group():
			between_vector = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Between Vector")

			between_vector.color_tag = 'CONVERTER'
			between_vector.description = ""

			
			#between_vector interface
			#Socket Boolean
			boolean_socket = between_vector.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket = between_vector.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketVector')
			value_socket.subtype = 'NONE'
			value_socket.default_value = (0.0, 0.0, 0.0)
			value_socket.min_value = -3.4028234663852886e+38
			value_socket.max_value = 3.4028234663852886e+38
			value_socket.attribute_domain = 'POINT'
			
			#Socket Lower
			lower_socket = between_vector.interface.new_socket(name = "Lower", in_out='INPUT', socket_type = 'NodeSocketVector')
			lower_socket.subtype = 'NONE'
			lower_socket.default_value = (0.0, 0.0, 0.0)
			lower_socket.min_value = -3.4028234663852886e+38
			lower_socket.max_value = 3.4028234663852886e+38
			lower_socket.attribute_domain = 'POINT'
			
			#Socket Upper
			upper_socket = between_vector.interface.new_socket(name = "Upper", in_out='INPUT', socket_type = 'NodeSocketVector')
			upper_socket.subtype = 'NONE'
			upper_socket.default_value = (0.0, 0.0, 0.0)
			upper_socket.min_value = -3.4028234663852886e+38
			upper_socket.max_value = 3.4028234663852886e+38
			upper_socket.attribute_domain = 'POINT'
			
			
			#initialize between_vector nodes
			#node Group Output
			group_output = between_vector.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = between_vector.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Compare
			compare = between_vector.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'VECTOR'
			compare.mode = 'ELEMENT'
			compare.operation = 'LESS_EQUAL'
			
			#node Compare.001
			compare_001 = between_vector.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'VECTOR'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'GREATER_EQUAL'
			
			#node Boolean Math
			boolean_math = between_vector.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'AND'
			
			
			
			
			#Set locations
			group_output.location = (260.0, 0.0)
			group_input.location = (-280.0, 0.0)
			compare.location = (-80.0, -20.0)
			compare_001.location = (-80.0, 180.0)
			boolean_math.location = (80.0, 180.0)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			
			#initialize between_vector links
			#compare.Result -> boolean_math.Boolean
			between_vector.links.new(compare.outputs[0], boolean_math.inputs[1])
			#compare_001.Result -> boolean_math.Boolean
			between_vector.links.new(compare_001.outputs[0], boolean_math.inputs[0])
			#group_input.Value -> compare.A
			between_vector.links.new(group_input.outputs[0], compare.inputs[2])
			#group_input.Value -> compare_001.A
			between_vector.links.new(group_input.outputs[0], compare_001.inputs[2])
			#boolean_math.Boolean -> group_output.Boolean
			between_vector.links.new(boolean_math.outputs[0], group_output.inputs[0])
			#group_input.Lower -> compare_001.B
			between_vector.links.new(group_input.outputs[1], compare_001.inputs[3])
			#group_input.Upper -> compare.B
			between_vector.links.new(group_input.outputs[2], compare.inputs[3])
			#group_input.Value -> compare_001.A
			between_vector.links.new(group_input.outputs[0], compare_001.inputs[0])
			#group_input.Value -> compare.A
			between_vector.links.new(group_input.outputs[0], compare.inputs[0])
			#group_input.Lower -> compare_001.B
			between_vector.links.new(group_input.outputs[1], compare_001.inputs[1])
			#group_input.Upper -> compare.B
			between_vector.links.new(group_input.outputs[2], compare.inputs[1])
			#group_input.Value -> compare_001.A
			between_vector.links.new(group_input.outputs[0], compare_001.inputs[4])
			#group_input.Lower -> compare_001.B
			between_vector.links.new(group_input.outputs[1], compare_001.inputs[5])
			#group_input.Value -> compare.A
			between_vector.links.new(group_input.outputs[0], compare.inputs[4])
			#group_input.Upper -> compare.B
			between_vector.links.new(group_input.outputs[2], compare.inputs[5])
			return between_vector

		between_vector = between_vector_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Between Vector", type = 'NODES')
		mod.node_group = between_vector
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Between_Vector.bl_idname)
			
def register():
	bpy.utils.register_class(Between_Vector)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Between_Vector)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
