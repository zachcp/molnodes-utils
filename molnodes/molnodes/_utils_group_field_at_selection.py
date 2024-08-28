bl_info = {
	"name" : ".utils_group_field_at_selection",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _utils_group_field_at_selection(bpy.types.Operator):
	bl_idname = "node._utils_group_field_at_selection"
	bl_label = ".utils_group_field_at_selection"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _utils_group_field_at_selection node group
		def _utils_group_field_at_selection_node_group():
			_utils_group_field_at_selection = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".utils_group_field_at_selection")

			_utils_group_field_at_selection.color_tag = 'NONE'
			_utils_group_field_at_selection.description = ""

			
			#_utils_group_field_at_selection interface
			#Socket Group Index
			group_index_socket = _utils_group_field_at_selection.interface.new_socket(name = "Group Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			group_index_socket.default_value = 0
			group_index_socket.min_value = -2147483648
			group_index_socket.max_value = 2147483647
			group_index_socket.subtype = 'NONE'
			group_index_socket.attribute_domain = 'POINT'
			
			#Socket Float
			float_socket = _utils_group_field_at_selection.interface.new_socket(name = "Float", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			float_socket.default_value = 0.0
			float_socket.min_value = -3.4028234663852886e+38
			float_socket.max_value = 3.4028234663852886e+38
			float_socket.subtype = 'NONE'
			float_socket.attribute_domain = 'POINT'
			
			#Socket Vector
			vector_socket = _utils_group_field_at_selection.interface.new_socket(name = "Vector", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			vector_socket.default_value = (0.0, 0.0, 0.0)
			vector_socket.min_value = -3.4028234663852886e+38
			vector_socket.max_value = 3.4028234663852886e+38
			vector_socket.subtype = 'NONE'
			vector_socket.attribute_domain = 'POINT'
			
			#Socket Boolean
			boolean_socket = _utils_group_field_at_selection.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket.default_value = False
			boolean_socket.attribute_domain = 'POINT'
			
			#Socket Color
			color_socket = _utils_group_field_at_selection.interface.new_socket(name = "Color", in_out='OUTPUT', socket_type = 'NodeSocketColor')
			color_socket.default_value = (0.0, 0.0, 0.0, 0.0)
			color_socket.attribute_domain = 'POINT'
			
			#Socket Integer
			integer_socket = _utils_group_field_at_selection.interface.new_socket(name = "Integer", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			integer_socket.default_value = 0
			integer_socket.min_value = -2147483648
			integer_socket.max_value = 2147483647
			integer_socket.subtype = 'NONE'
			integer_socket.attribute_domain = 'POINT'
			
			#Socket Selection
			selection_socket = _utils_group_field_at_selection.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket.default_value = False
			selection_socket.attribute_domain = 'POINT'
			selection_socket.description = "Selection of atoms to apply this node to"
			
			#Socket Group Index
			group_index_socket_1 = _utils_group_field_at_selection.interface.new_socket(name = "Group Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			group_index_socket_1.default_value = 0
			group_index_socket_1.min_value = -2147483648
			group_index_socket_1.max_value = 2147483647
			group_index_socket_1.subtype = 'NONE'
			group_index_socket_1.attribute_domain = 'POINT'
			
			#Socket Float
			float_socket_1 = _utils_group_field_at_selection.interface.new_socket(name = "Float", in_out='INPUT', socket_type = 'NodeSocketFloat')
			float_socket_1.default_value = 0.0
			float_socket_1.min_value = -3.4028234663852886e+38
			float_socket_1.max_value = 3.4028234663852886e+38
			float_socket_1.subtype = 'NONE'
			float_socket_1.attribute_domain = 'POINT'
			float_socket_1.hide_value = True
			
			#Socket Vector
			vector_socket_1 = _utils_group_field_at_selection.interface.new_socket(name = "Vector", in_out='INPUT', socket_type = 'NodeSocketVector')
			vector_socket_1.default_value = (0.0, 0.0, 0.0)
			vector_socket_1.min_value = -3.4028234663852886e+38
			vector_socket_1.max_value = 3.4028234663852886e+38
			vector_socket_1.subtype = 'NONE'
			vector_socket_1.attribute_domain = 'POINT'
			vector_socket_1.hide_value = True
			
			#Socket Boolean
			boolean_socket_1 = _utils_group_field_at_selection.interface.new_socket(name = "Boolean", in_out='INPUT', socket_type = 'NodeSocketBool')
			boolean_socket_1.default_value = False
			boolean_socket_1.attribute_domain = 'POINT'
			boolean_socket_1.hide_value = True
			
			#Socket Color
			color_socket_1 = _utils_group_field_at_selection.interface.new_socket(name = "Color", in_out='INPUT', socket_type = 'NodeSocketColor')
			color_socket_1.default_value = (0.0, 0.0, 0.0, 0.0)
			color_socket_1.attribute_domain = 'POINT'
			color_socket_1.hide_value = True
			
			#Socket Integer
			integer_socket_1 = _utils_group_field_at_selection.interface.new_socket(name = "Integer", in_out='INPUT', socket_type = 'NodeSocketInt')
			integer_socket_1.default_value = 0
			integer_socket_1.min_value = -2147483648
			integer_socket_1.max_value = 2147483647
			integer_socket_1.subtype = 'NONE'
			integer_socket_1.attribute_domain = 'POINT'
			integer_socket_1.hide_value = True
			
			
			#initialize _utils_group_field_at_selection nodes
			#node Switch.006
			switch_006 = _utils_group_field_at_selection.nodes.new("GeometryNodeSwitch")
			switch_006.name = "Switch.006"
			switch_006.input_type = 'INT'
			#False
			switch_006.inputs[1].default_value = 0
			
			#node Accumulate Field.002
			accumulate_field_002 = _utils_group_field_at_selection.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_002.name = "Accumulate Field.002"
			accumulate_field_002.data_type = 'INT'
			accumulate_field_002.domain = 'POINT'
			
			#node Index
			index = _utils_group_field_at_selection.nodes.new("GeometryNodeInputIndex")
			index.name = "Index"
			
			#node Group Output
			group_output = _utils_group_field_at_selection.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Field at Index
			field_at_index = _utils_group_field_at_selection.nodes.new("GeometryNodeFieldAtIndex")
			field_at_index.name = "Field at Index"
			field_at_index.data_type = 'FLOAT'
			field_at_index.domain = 'POINT'
			
			#node Field at Index.001
			field_at_index_001 = _utils_group_field_at_selection.nodes.new("GeometryNodeFieldAtIndex")
			field_at_index_001.name = "Field at Index.001"
			field_at_index_001.data_type = 'FLOAT_VECTOR'
			field_at_index_001.domain = 'POINT'
			
			#node Field at Index.002
			field_at_index_002 = _utils_group_field_at_selection.nodes.new("GeometryNodeFieldAtIndex")
			field_at_index_002.name = "Field at Index.002"
			field_at_index_002.data_type = 'BOOLEAN'
			field_at_index_002.domain = 'POINT'
			
			#node Field at Index.003
			field_at_index_003 = _utils_group_field_at_selection.nodes.new("GeometryNodeFieldAtIndex")
			field_at_index_003.name = "Field at Index.003"
			field_at_index_003.data_type = 'FLOAT_COLOR'
			field_at_index_003.domain = 'POINT'
			
			#node Group Input
			group_input = _utils_group_field_at_selection.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Field at Index.004
			field_at_index_004 = _utils_group_field_at_selection.nodes.new("GeometryNodeFieldAtIndex")
			field_at_index_004.name = "Field at Index.004"
			field_at_index_004.data_type = 'INT'
			field_at_index_004.domain = 'POINT'
			
			
			
			
			#Set locations
			switch_006.location = (-80.0, 80.0)
			accumulate_field_002.location = (80.0, 80.0)
			index.location = (-80.0, -80.0)
			group_output.location = (477.87579345703125, 6.6051177978515625)
			field_at_index.location = (280.0, -20.0)
			field_at_index_001.location = (280.0, -180.0)
			field_at_index_002.location = (280.0, -340.0)
			field_at_index_003.location = (280.0, -500.0)
			group_input.location = (-280.0, -0.0)
			field_at_index_004.location = (280.0, -660.0)
			
			#Set dimensions
			switch_006.width, switch_006.height = 140.0, 100.0
			accumulate_field_002.width, accumulate_field_002.height = 140.0, 100.0
			index.width, index.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			field_at_index.width, field_at_index.height = 140.0, 100.0
			field_at_index_001.width, field_at_index_001.height = 140.0, 100.0
			field_at_index_002.width, field_at_index_002.height = 140.0, 100.0
			field_at_index_003.width, field_at_index_003.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			field_at_index_004.width, field_at_index_004.height = 140.0, 100.0
			
			#initialize _utils_group_field_at_selection links
			#group_input.Selection -> switch_006.Switch
			_utils_group_field_at_selection.links.new(group_input.outputs[0], switch_006.inputs[0])
			#accumulate_field_002.Total -> group_output.Group Index
			_utils_group_field_at_selection.links.new(accumulate_field_002.outputs[2], group_output.inputs[0])
			#group_input.Group Index -> accumulate_field_002.Group ID
			_utils_group_field_at_selection.links.new(group_input.outputs[1], accumulate_field_002.inputs[1])
			#index.Index -> switch_006.True
			_utils_group_field_at_selection.links.new(index.outputs[0], switch_006.inputs[2])
			#switch_006.Output -> accumulate_field_002.Value
			_utils_group_field_at_selection.links.new(switch_006.outputs[0], accumulate_field_002.inputs[0])
			#accumulate_field_002.Total -> field_at_index.Index
			_utils_group_field_at_selection.links.new(accumulate_field_002.outputs[2], field_at_index.inputs[0])
			#group_input.Float -> field_at_index.Value
			_utils_group_field_at_selection.links.new(group_input.outputs[2], field_at_index.inputs[1])
			#field_at_index.Value -> group_output.Float
			_utils_group_field_at_selection.links.new(field_at_index.outputs[0], group_output.inputs[1])
			#accumulate_field_002.Total -> field_at_index_001.Index
			_utils_group_field_at_selection.links.new(accumulate_field_002.outputs[2], field_at_index_001.inputs[0])
			#group_input.Vector -> field_at_index_001.Value
			_utils_group_field_at_selection.links.new(group_input.outputs[3], field_at_index_001.inputs[1])
			#field_at_index_001.Value -> group_output.Vector
			_utils_group_field_at_selection.links.new(field_at_index_001.outputs[0], group_output.inputs[2])
			#accumulate_field_002.Total -> field_at_index_002.Index
			_utils_group_field_at_selection.links.new(accumulate_field_002.outputs[2], field_at_index_002.inputs[0])
			#group_input.Boolean -> field_at_index_002.Value
			_utils_group_field_at_selection.links.new(group_input.outputs[4], field_at_index_002.inputs[1])
			#field_at_index_002.Value -> group_output.Boolean
			_utils_group_field_at_selection.links.new(field_at_index_002.outputs[0], group_output.inputs[3])
			#accumulate_field_002.Total -> field_at_index_003.Index
			_utils_group_field_at_selection.links.new(accumulate_field_002.outputs[2], field_at_index_003.inputs[0])
			#group_input.Color -> field_at_index_003.Value
			_utils_group_field_at_selection.links.new(group_input.outputs[5], field_at_index_003.inputs[1])
			#field_at_index_003.Value -> group_output.Color
			_utils_group_field_at_selection.links.new(field_at_index_003.outputs[0], group_output.inputs[4])
			#accumulate_field_002.Total -> field_at_index_004.Index
			_utils_group_field_at_selection.links.new(accumulate_field_002.outputs[2], field_at_index_004.inputs[0])
			#group_input.Integer -> field_at_index_004.Value
			_utils_group_field_at_selection.links.new(group_input.outputs[6], field_at_index_004.inputs[1])
			#field_at_index_004.Value -> group_output.Integer
			_utils_group_field_at_selection.links.new(field_at_index_004.outputs[0], group_output.inputs[5])
			return _utils_group_field_at_selection

		_utils_group_field_at_selection = _utils_group_field_at_selection_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".utils_group_field_at_selection", type = 'NODES')
		mod.node_group = _utils_group_field_at_selection
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_utils_group_field_at_selection.bl_idname)
			
def register():
	bpy.utils.register_class(_utils_group_field_at_selection)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_utils_group_field_at_selection)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
