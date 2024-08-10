bl_info = {
	"name" : ".MN_select_attribute",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _MN_select_attribute(bpy.types.Operator):
	bl_idname = "node._mn_select_attribute"
	bl_label = ".MN_select_attribute"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _mn_select_attribute node group
		def _mn_select_attribute_node_group():
			_mn_select_attribute = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_select_attribute")

			_mn_select_attribute.color_tag = 'NONE'
			_mn_select_attribute.description = ""

			
			#_mn_select_attribute interface
			#Socket Selection
			selection_socket = _mn_select_attribute.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket.attribute_domain = 'POINT'
			
			#Socket Inverted
			inverted_socket = _mn_select_attribute.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket.attribute_domain = 'POINT'
			
			#Socket And
			and_socket = _mn_select_attribute.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket.attribute_domain = 'POINT'
			and_socket.hide_value = True
			
			#Socket Or
			or_socket = _mn_select_attribute.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket.attribute_domain = 'POINT'
			or_socket.hide_value = True
			
			#Socket Name
			name_socket = _mn_select_attribute.interface.new_socket(name = "Name", in_out='INPUT', socket_type = 'NodeSocketString')
			name_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_select_attribute nodes
			#node Named Attribute
			named_attribute = _mn_select_attribute.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'BOOLEAN'
			
			#node Group Input
			group_input = _mn_select_attribute.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Boolean Math
			boolean_math = _mn_select_attribute.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'AND'
			
			#node Group Output
			group_output = _mn_select_attribute.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Boolean Math.001
			boolean_math_001 = _mn_select_attribute.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001.name = "Boolean Math.001"
			boolean_math_001.operation = 'OR'
			
			#node Boolean Math.002
			boolean_math_002 = _mn_select_attribute.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002.name = "Boolean Math.002"
			boolean_math_002.operation = 'NOT'
			
			
			
			
			#Set locations
			named_attribute.location = (-120.0, 40.0)
			group_input.location = (-300.0, 40.0)
			boolean_math.location = (40.0, 40.0)
			group_output.location = (400.00006103515625, 40.0)
			boolean_math_001.location = (220.0, 40.0)
			boolean_math_002.location = (220.0, -100.0)
			
			#Set dimensions
			named_attribute.width, named_attribute.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
			boolean_math_002.width, boolean_math_002.height = 140.0, 100.0
			
			#initialize _mn_select_attribute links
			#named_attribute.Attribute -> boolean_math.Boolean
			_mn_select_attribute.links.new(named_attribute.outputs[0], boolean_math.inputs[0])
			#group_input.And -> boolean_math.Boolean
			_mn_select_attribute.links.new(group_input.outputs[0], boolean_math.inputs[1])
			#boolean_math_001.Boolean -> group_output.Selection
			_mn_select_attribute.links.new(boolean_math_001.outputs[0], group_output.inputs[0])
			#group_input.Name -> named_attribute.Name
			_mn_select_attribute.links.new(group_input.outputs[2], named_attribute.inputs[0])
			#boolean_math.Boolean -> boolean_math_001.Boolean
			_mn_select_attribute.links.new(boolean_math.outputs[0], boolean_math_001.inputs[0])
			#group_input.Or -> boolean_math_001.Boolean
			_mn_select_attribute.links.new(group_input.outputs[1], boolean_math_001.inputs[1])
			#boolean_math_001.Boolean -> boolean_math_002.Boolean
			_mn_select_attribute.links.new(boolean_math_001.outputs[0], boolean_math_002.inputs[0])
			#boolean_math_002.Boolean -> group_output.Inverted
			_mn_select_attribute.links.new(boolean_math_002.outputs[0], group_output.inputs[1])
			return _mn_select_attribute

		_mn_select_attribute = _mn_select_attribute_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".MN_select_attribute", type = 'NODES')
		mod.node_group = _mn_select_attribute
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_MN_select_attribute.bl_idname)
			
def register():
	bpy.utils.register_class(_MN_select_attribute)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_MN_select_attribute)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
