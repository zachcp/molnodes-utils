bl_info = {
	"name" : ".MN_animate_wiggle_mask_length",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _MN_animate_wiggle_mask_length(bpy.types.Operator):
	bl_idname = "node._mn_animate_wiggle_mask_length"
	bl_label = ".MN_animate_wiggle_mask_length"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _mn_animate_wiggle_mask_length node group
		def _mn_animate_wiggle_mask_length_node_group():
			_mn_animate_wiggle_mask_length = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_animate_wiggle_mask_length")

			_mn_animate_wiggle_mask_length.color_tag = 'NONE'
			_mn_animate_wiggle_mask_length.description = ""

			
			#_mn_animate_wiggle_mask_length interface
			#Socket Result
			result_socket = _mn_animate_wiggle_mask_length.interface.new_socket(name = "Result", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			result_socket.default_value = 0
			result_socket.min_value = -2147483648
			result_socket.max_value = 2147483647
			result_socket.subtype = 'NONE'
			result_socket.attribute_domain = 'POINT'
			
			#Socket A
			a_socket = _mn_animate_wiggle_mask_length.interface.new_socket(name = "A", in_out='INPUT', socket_type = 'NodeSocketInt')
			a_socket.default_value = 0
			a_socket.min_value = -2147483648
			a_socket.max_value = 2147483647
			a_socket.subtype = 'NONE'
			a_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_animate_wiggle_mask_length nodes
			#node Group Output
			group_output = _mn_animate_wiggle_mask_length.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = _mn_animate_wiggle_mask_length.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Index Switch
			index_switch = _mn_animate_wiggle_mask_length.nodes.new("GeometryNodeIndexSwitch")
			index_switch.name = "Index Switch"
			index_switch.data_type = 'INT'
			index_switch.index_switch_items.clear()
			index_switch.index_switch_items.new()
			index_switch.index_switch_items.new()
			index_switch.index_switch_items.new()
			index_switch.index_switch_items.new()
			index_switch.index_switch_items.new()
			#Item_0
			index_switch.inputs[1].default_value = 2
			#Item_1
			index_switch.inputs[2].default_value = 5
			#Item_2
			index_switch.inputs[3].default_value = 6
			#Item_3
			index_switch.inputs[4].default_value = 12
			#Item_4
			index_switch.inputs[5].default_value = 20
			
			
			
			
			#Set locations
			group_output.location = (80.0, 560.0)
			group_input.location = (-300.0, 560.0)
			index_switch.location = (-120.55677795410156, 554.9675903320312)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			index_switch.width, index_switch.height = 140.0, 100.0
			
			#initialize _mn_animate_wiggle_mask_length links
			#group_input.A -> index_switch.Index
			_mn_animate_wiggle_mask_length.links.new(group_input.outputs[0], index_switch.inputs[0])
			#index_switch.Output -> group_output.Result
			_mn_animate_wiggle_mask_length.links.new(index_switch.outputs[0], group_output.inputs[0])
			return _mn_animate_wiggle_mask_length

		_mn_animate_wiggle_mask_length = _mn_animate_wiggle_mask_length_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".MN_animate_wiggle_mask_length", type = 'NODES')
		mod.node_group = _mn_animate_wiggle_mask_length
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_MN_animate_wiggle_mask_length.bl_idname)
			
def register():
	bpy.utils.register_class(_MN_animate_wiggle_mask_length)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_MN_animate_wiggle_mask_length)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
