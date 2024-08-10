bl_info = {
	"name" : "Group Info",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Group_Info(bpy.types.Operator):
	bl_idname = "node.group_info"
	bl_label = "Group Info"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize group_info node group
		def group_info_node_group():
			group_info = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Group Info")

			group_info.color_tag = 'CONVERTER'
			group_info.description = ""

			
			#group_info interface
			#Socket First Index
			first_index_socket = group_info.interface.new_socket(name = "First Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			first_index_socket.subtype = 'NONE'
			first_index_socket.default_value = 0
			first_index_socket.min_value = -2147483648
			first_index_socket.max_value = 2147483647
			first_index_socket.attribute_domain = 'POINT'
			first_index_socket.description = "Index of the first point in the group"
			
			#Socket Last Index
			last_index_socket = group_info.interface.new_socket(name = "Last Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			last_index_socket.subtype = 'NONE'
			last_index_socket.default_value = 0
			last_index_socket.min_value = -2147483648
			last_index_socket.max_value = 2147483647
			last_index_socket.attribute_domain = 'POINT'
			last_index_socket.description = "Index of the last point in the group"
			
			#Socket Index in Group
			index_in_group_socket = group_info.interface.new_socket(name = "Index in Group", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			index_in_group_socket.subtype = 'NONE'
			index_in_group_socket.default_value = 0
			index_in_group_socket.min_value = -2147483648
			index_in_group_socket.max_value = 2147483647
			index_in_group_socket.attribute_domain = 'POINT'
			
			#Socket Size
			size_socket = group_info.interface.new_socket(name = "Size", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			size_socket.subtype = 'NONE'
			size_socket.default_value = 0
			size_socket.min_value = -2147483648
			size_socket.max_value = 2147483647
			size_socket.attribute_domain = 'POINT'
			size_socket.description = "Number of points in the group"
			
			#Socket Group ID
			group_id_socket = group_info.interface.new_socket(name = "Group ID", in_out='INPUT', socket_type = 'NodeSocketInt')
			group_id_socket.subtype = 'NONE'
			group_id_socket.default_value = 0
			group_id_socket.min_value = -2147483648
			group_id_socket.max_value = 2147483647
			group_id_socket.attribute_domain = 'POINT'
			
			
			#initialize group_info nodes
			#node Group Output
			group_output = group_info.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = group_info.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Accumulate Field.001
			accumulate_field_001 = group_info.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_001.name = "Accumulate Field.001"
			accumulate_field_001.data_type = 'INT'
			accumulate_field_001.domain = 'POINT'
			accumulate_field_001.outputs[0].hide = True
			accumulate_field_001.outputs[1].hide = True
			
			#node Index
			index = group_info.nodes.new("GeometryNodeInputIndex")
			index.name = "Index"
			
			#node Compare
			compare = group_info.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'EQUAL'
			#B_INT
			compare.inputs[3].default_value = 0
			
			#node Switch.001
			switch_001 = group_info.nodes.new("GeometryNodeSwitch")
			switch_001.name = "Switch.001"
			switch_001.input_type = 'INT'
			#False
			switch_001.inputs[1].default_value = 0
			
			#node Compare.002
			compare_002 = group_info.nodes.new("FunctionNodeCompare")
			compare_002.name = "Compare.002"
			compare_002.data_type = 'INT'
			compare_002.mode = 'ELEMENT'
			compare_002.operation = 'EQUAL'
			
			#node Switch.002
			switch_002 = group_info.nodes.new("GeometryNodeSwitch")
			switch_002.name = "Switch.002"
			switch_002.input_type = 'INT'
			#False
			switch_002.inputs[1].default_value = 0
			
			#node Accumulate Field.002
			accumulate_field_002 = group_info.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_002.name = "Accumulate Field.002"
			accumulate_field_002.data_type = 'INT'
			accumulate_field_002.domain = 'POINT'
			accumulate_field_002.outputs[0].hide = True
			accumulate_field_002.outputs[1].hide = True
			
			#node Reroute
			reroute = group_info.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Accumulate Field.003
			accumulate_field_003 = group_info.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_003.name = "Accumulate Field.003"
			accumulate_field_003.data_type = 'INT'
			accumulate_field_003.domain = 'POINT'
			#Value
			accumulate_field_003.inputs[0].default_value = 1
			
			#node Reroute.001
			reroute_001 = group_info.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			
			
			
			#Set locations
			group_output.location = (580.0, 100.0)
			group_input.location = (-540.0, 0.0)
			accumulate_field_001.location = (340.0, 140.0)
			index.location = (-40.0, -20.0)
			compare.location = (-40.0, 140.0)
			switch_001.location = (120.0, 140.0)
			compare_002.location = (-40.0, -80.0)
			switch_002.location = (120.0, -20.0)
			accumulate_field_002.location = (340.0, -78.97427368164062)
			reroute.location = (280.0, -300.0)
			accumulate_field_003.location = (-240.0, -80.0)
			reroute_001.location = (-320.0, -300.0)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			accumulate_field_001.width, accumulate_field_001.height = 140.0, 100.0
			index.width, index.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			switch_001.width, switch_001.height = 140.0, 100.0
			compare_002.width, compare_002.height = 140.0, 100.0
			switch_002.width, switch_002.height = 140.0, 100.0
			accumulate_field_002.width, accumulate_field_002.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			accumulate_field_003.width, accumulate_field_003.height = 140.0, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			
			#initialize group_info links
			#reroute.Output -> accumulate_field_002.Group ID
			group_info.links.new(reroute.outputs[0], accumulate_field_002.inputs[1])
			#reroute_001.Output -> reroute.Input
			group_info.links.new(reroute_001.outputs[0], reroute.inputs[0])
			#index.Index -> switch_002.True
			group_info.links.new(index.outputs[0], switch_002.inputs[2])
			#accumulate_field_003.Trailing -> compare.A
			group_info.links.new(accumulate_field_003.outputs[1], compare.inputs[2])
			#compare.Result -> switch_001.Switch
			group_info.links.new(compare.outputs[0], switch_001.inputs[0])
			#accumulate_field_003.Total -> compare_002.B
			group_info.links.new(accumulate_field_003.outputs[2], compare_002.inputs[3])
			#switch_002.Output -> accumulate_field_002.Value
			group_info.links.new(switch_002.outputs[0], accumulate_field_002.inputs[0])
			#reroute_001.Output -> accumulate_field_003.Group ID
			group_info.links.new(reroute_001.outputs[0], accumulate_field_003.inputs[1])
			#index.Index -> switch_001.True
			group_info.links.new(index.outputs[0], switch_001.inputs[2])
			#switch_001.Output -> accumulate_field_001.Value
			group_info.links.new(switch_001.outputs[0], accumulate_field_001.inputs[0])
			#compare_002.Result -> switch_002.Switch
			group_info.links.new(compare_002.outputs[0], switch_002.inputs[0])
			#reroute.Output -> accumulate_field_001.Group ID
			group_info.links.new(reroute.outputs[0], accumulate_field_001.inputs[1])
			#group_input.Group ID -> reroute_001.Input
			group_info.links.new(group_input.outputs[0], reroute_001.inputs[0])
			#accumulate_field_001.Total -> group_output.First Index
			group_info.links.new(accumulate_field_001.outputs[2], group_output.inputs[0])
			#accumulate_field_002.Total -> group_output.Last Index
			group_info.links.new(accumulate_field_002.outputs[2], group_output.inputs[1])
			#accumulate_field_003.Total -> group_output.Size
			group_info.links.new(accumulate_field_003.outputs[2], group_output.inputs[3])
			#accumulate_field_003.Leading -> compare_002.A
			group_info.links.new(accumulate_field_003.outputs[0], compare_002.inputs[2])
			#accumulate_field_003.Trailing -> group_output.Index in Group
			group_info.links.new(accumulate_field_003.outputs[1], group_output.inputs[2])
			return group_info

		group_info = group_info_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Group Info", type = 'NODES')
		mod.node_group = group_info
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Group_Info.bl_idname)
			
def register():
	bpy.utils.register_class(Group_Info)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Group_Info)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
