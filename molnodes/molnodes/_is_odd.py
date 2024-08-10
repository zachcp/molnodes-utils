bl_info = {
	"name" : ".is_odd",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _is_odd(bpy.types.Operator):
	bl_idname = "node._is_odd"
	bl_label = ".is_odd"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _is_odd node group
		def _is_odd_node_group():
			_is_odd = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".is_odd")

			_is_odd.color_tag = 'NONE'
			_is_odd.description = ""

			
			#_is_odd interface
			#Socket is_even
			is_even_socket = _is_odd.interface.new_socket(name = "is_even", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_even_socket.attribute_domain = 'POINT'
			
			#Socket is_odd
			is_odd_socket = _is_odd.interface.new_socket(name = "is_odd", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_odd_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket = _is_odd.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketInt')
			value_socket.subtype = 'NONE'
			value_socket.default_value = 0
			value_socket.min_value = -2147483648
			value_socket.max_value = 2147483647
			value_socket.attribute_domain = 'POINT'
			
			
			#initialize _is_odd nodes
			#node Group Input
			group_input = _is_odd.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Group Output
			group_output = _is_odd.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Boolean Math
			boolean_math = _is_odd.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'NOT'
			
			#node Compare.011
			compare_011 = _is_odd.nodes.new("FunctionNodeCompare")
			compare_011.name = "Compare.011"
			compare_011.data_type = 'FLOAT'
			compare_011.mode = 'ELEMENT'
			compare_011.operation = 'EQUAL'
			#B
			compare_011.inputs[1].default_value = 0.0
			#Epsilon
			compare_011.inputs[12].default_value = 0.0010000000474974513
			
			#node Math.008
			math_008 = _is_odd.nodes.new("ShaderNodeMath")
			math_008.name = "Math.008"
			math_008.operation = 'FLOORED_MODULO'
			math_008.use_clamp = False
			#Value_001
			math_008.inputs[1].default_value = 2.0
			
			
			
			
			#Set locations
			group_input.location = (-300.0, 80.0)
			group_output.location = (240.0, 120.0)
			boolean_math.location = (240.0, 20.0)
			compare_011.location = (60.0, 120.0)
			math_008.location = (-100.0, 120.0)
			
			#Set dimensions
			group_input.width, group_input.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			compare_011.width, compare_011.height = 140.0, 100.0
			math_008.width, math_008.height = 140.0, 100.0
			
			#initialize _is_odd links
			#group_input.Value -> math_008.Value
			_is_odd.links.new(group_input.outputs[0], math_008.inputs[0])
			#compare_011.Result -> group_output.is_even
			_is_odd.links.new(compare_011.outputs[0], group_output.inputs[0])
			#compare_011.Result -> boolean_math.Boolean
			_is_odd.links.new(compare_011.outputs[0], boolean_math.inputs[0])
			#boolean_math.Boolean -> group_output.is_odd
			_is_odd.links.new(boolean_math.outputs[0], group_output.inputs[1])
			#math_008.Value -> compare_011.A
			_is_odd.links.new(math_008.outputs[0], compare_011.inputs[0])
			return _is_odd

		_is_odd = _is_odd_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".is_odd", type = 'NODES')
		mod.node_group = _is_odd
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_is_odd.bl_idname)
			
def register():
	bpy.utils.register_class(_is_odd)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_is_odd)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
