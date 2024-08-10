bl_info = {
	"name" : "Group Pick",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Group_Pick(bpy.types.Operator):
	bl_idname = "node.group_pick"
	bl_label = "Group Pick"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize group_pick node group
		def group_pick_node_group():
			group_pick = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Group Pick")

			group_pick.color_tag = 'INPUT'
			group_pick.description = ""

			
			#group_pick interface
			#Socket Is Valid
			is_valid_socket = group_pick.interface.new_socket(name = "Is Valid", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_valid_socket.attribute_domain = 'POINT'
			is_valid_socket.description = "Whether the pick is valid. Pick is only valid if a single item is picked in the Group ID"
			
			#Socket Index
			index_socket = group_pick.interface.new_socket(name = "Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			index_socket.subtype = 'NONE'
			index_socket.default_value = 0
			index_socket.min_value = 0
			index_socket.max_value = 2147483647
			index_socket.attribute_domain = 'POINT'
			index_socket.description = "Index of picked item. Returns -1 if not a valid pick."
			
			#Socket Pick
			pick_socket = group_pick.interface.new_socket(name = "Pick", in_out='INPUT', socket_type = 'NodeSocketBool')
			pick_socket.attribute_domain = 'POINT'
			pick_socket.hide_value = True
			pick_socket.description = "True for the item to pick from the group. If number of picks is 0 or more than 1, not a valid pick"
			
			#Socket Group ID
			group_id_socket = group_pick.interface.new_socket(name = "Group ID", in_out='INPUT', socket_type = 'NodeSocketInt')
			group_id_socket.subtype = 'NONE'
			group_id_socket.default_value = 0
			group_id_socket.min_value = -2147483648
			group_id_socket.max_value = 2147483647
			group_id_socket.attribute_domain = 'POINT'
			group_id_socket.description = "Group ID inside which to pick the item"
			
			
			#initialize group_pick nodes
			#node Group Output
			group_output = group_pick.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = group_pick.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Switch
			switch = group_pick.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'INT'
			#False
			switch.inputs[1].default_value = 0
			
			#node Index
			index = group_pick.nodes.new("GeometryNodeInputIndex")
			index.name = "Index"
			
			#node Accumulate Field
			accumulate_field = group_pick.nodes.new("GeometryNodeAccumulateField")
			accumulate_field.name = "Accumulate Field"
			accumulate_field.data_type = 'INT'
			accumulate_field.domain = 'POINT'
			
			#node Accumulate Field.002
			accumulate_field_002 = group_pick.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_002.name = "Accumulate Field.002"
			accumulate_field_002.data_type = 'INT'
			accumulate_field_002.domain = 'POINT'
			
			#node Switch.001
			switch_001 = group_pick.nodes.new("GeometryNodeSwitch")
			switch_001.name = "Switch.001"
			switch_001.input_type = 'INT'
			#False
			switch_001.inputs[1].default_value = -1
			
			#node Compare.003
			compare_003 = group_pick.nodes.new("FunctionNodeCompare")
			compare_003.name = "Compare.003"
			compare_003.data_type = 'INT'
			compare_003.mode = 'ELEMENT'
			compare_003.operation = 'EQUAL'
			#B_INT
			compare_003.inputs[3].default_value = 1
			
			#node Reroute.001
			reroute_001 = group_pick.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			#node Reroute.002
			reroute_002 = group_pick.nodes.new("NodeReroute")
			reroute_002.name = "Reroute.002"
			
			
			
			#Set locations
			group_output.location = (462.9173889160156, 0.0)
			group_input.location = (-472.9173889160156, 0.0)
			switch.location = (-120.0, -20.0)
			index.location = (-480.0, -120.0)
			accumulate_field.location = (60.0, -20.0)
			accumulate_field_002.location = (-120.0, 180.0)
			switch_001.location = (240.0, -20.0)
			compare_003.location = (60.0, 180.0)
			reroute_001.location = (-260.0, -100.0)
			reroute_002.location = (-260.0, -60.0)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			index.width, index.height = 140.0, 100.0
			accumulate_field.width, accumulate_field.height = 140.0, 100.0
			accumulate_field_002.width, accumulate_field_002.height = 140.0, 100.0
			switch_001.width, switch_001.height = 140.0, 100.0
			compare_003.width, compare_003.height = 138.9921875, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			reroute_002.width, reroute_002.height = 16.0, 100.0
			
			#initialize group_pick links
			#switch.Output -> accumulate_field.Value
			group_pick.links.new(switch.outputs[0], accumulate_field.inputs[0])
			#compare_003.Result -> switch_001.Switch
			group_pick.links.new(compare_003.outputs[0], switch_001.inputs[0])
			#accumulate_field.Total -> switch_001.True
			group_pick.links.new(accumulate_field.outputs[2], switch_001.inputs[2])
			#reroute_001.Output -> accumulate_field.Group ID
			group_pick.links.new(reroute_001.outputs[0], accumulate_field.inputs[1])
			#reroute_001.Output -> accumulate_field_002.Group ID
			group_pick.links.new(reroute_001.outputs[0], accumulate_field_002.inputs[1])
			#reroute_002.Output -> switch.Switch
			group_pick.links.new(reroute_002.outputs[0], switch.inputs[0])
			#reroute_002.Output -> accumulate_field_002.Value
			group_pick.links.new(reroute_002.outputs[0], accumulate_field_002.inputs[0])
			#index.Index -> switch.True
			group_pick.links.new(index.outputs[0], switch.inputs[2])
			#accumulate_field_002.Total -> compare_003.A
			group_pick.links.new(accumulate_field_002.outputs[2], compare_003.inputs[2])
			#group_input.Group ID -> reroute_001.Input
			group_pick.links.new(group_input.outputs[1], reroute_001.inputs[0])
			#group_input.Pick -> reroute_002.Input
			group_pick.links.new(group_input.outputs[0], reroute_002.inputs[0])
			#switch_001.Output -> group_output.Index
			group_pick.links.new(switch_001.outputs[0], group_output.inputs[1])
			#compare_003.Result -> group_output.Is Valid
			group_pick.links.new(compare_003.outputs[0], group_output.inputs[0])
			return group_pick

		group_pick = group_pick_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Group Pick", type = 'NODES')
		mod.node_group = group_pick
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Group_Pick.bl_idname)
			
def register():
	bpy.utils.register_class(Group_Pick)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Group_Pick)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
