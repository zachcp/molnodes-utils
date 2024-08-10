bl_info = {
	"name" : "Centre on Selection",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Centre_on_Selection(bpy.types.Operator):
	bl_idname = "node.centre_on_selection"
	bl_label = "Centre on Selection"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize centroid node group
		def centroid_node_group():
			centroid = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Centroid")

			centroid.color_tag = 'CONVERTER'
			centroid.description = ""

			
			#centroid interface
			#Socket Centroid
			centroid_socket = centroid.interface.new_socket(name = "Centroid", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			centroid_socket.subtype = 'NONE'
			centroid_socket.default_value = (0.0, 0.0, 0.0)
			centroid_socket.min_value = -3.4028234663852886e+38
			centroid_socket.max_value = 3.4028234663852886e+38
			centroid_socket.attribute_domain = 'POINT'
			centroid_socket.description = "Centroid point for the the points in the selectoin"
			
			#Socket Position
			position_socket = centroid.interface.new_socket(name = "Position", in_out='INPUT', socket_type = 'NodeSocketVector')
			position_socket.subtype = 'NONE'
			position_socket.default_value = (0.0, 0.0, 0.0)
			position_socket.min_value = -3.4028234663852886e+38
			position_socket.max_value = 3.4028234663852886e+38
			position_socket.attribute_domain = 'POINT'
			
			#Socket Selection
			selection_socket = centroid.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket.attribute_domain = 'POINT'
			selection_socket.hide_value = True
			selection_socket.description = "Selection to use for calculating centroid value"
			
			#Socket Group ID
			group_id_socket = centroid.interface.new_socket(name = "Group ID", in_out='INPUT', socket_type = 'NodeSocketInt')
			group_id_socket.subtype = 'NONE'
			group_id_socket.default_value = 0
			group_id_socket.min_value = -2147483648
			group_id_socket.max_value = 2147483647
			group_id_socket.attribute_domain = 'POINT'
			group_id_socket.description = "ID to calculate on a per-group basis"
			
			
			#initialize centroid nodes
			#node Group Output
			group_output = centroid.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = centroid.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Accumulate Field
			accumulate_field = centroid.nodes.new("GeometryNodeAccumulateField")
			accumulate_field.name = "Accumulate Field"
			accumulate_field.data_type = 'FLOAT_VECTOR'
			accumulate_field.domain = 'POINT'
			
			#node Accumulate Field.001
			accumulate_field_001 = centroid.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_001.name = "Accumulate Field.001"
			accumulate_field_001.data_type = 'INT'
			accumulate_field_001.domain = 'POINT'
			
			#node Vector Math
			vector_math = centroid.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.operation = 'DIVIDE'
			
			#node Switch
			switch = centroid.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'VECTOR'
			#False
			switch.inputs[1].default_value = (0.0, 0.0, 0.0)
			
			
			
			
			#Set locations
			group_output.location = (260.0, 60.0)
			group_input.location = (-500.0, -40.0)
			accumulate_field.location = (-80.0, 60.0)
			accumulate_field_001.location = (-80.0, -160.0)
			vector_math.location = (80.0, 60.0)
			switch.location = (-260.0, 60.0)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			accumulate_field.width, accumulate_field.height = 140.0, 100.0
			accumulate_field_001.width, accumulate_field_001.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			
			#initialize centroid links
			#group_input.Selection -> accumulate_field_001.Value
			centroid.links.new(group_input.outputs[1], accumulate_field_001.inputs[0])
			#accumulate_field.Total -> vector_math.Vector
			centroid.links.new(accumulate_field.outputs[2], vector_math.inputs[0])
			#accumulate_field_001.Total -> vector_math.Vector
			centroid.links.new(accumulate_field_001.outputs[2], vector_math.inputs[1])
			#group_input.Selection -> switch.Switch
			centroid.links.new(group_input.outputs[1], switch.inputs[0])
			#vector_math.Vector -> group_output.Centroid
			centroid.links.new(vector_math.outputs[0], group_output.inputs[0])
			#switch.Output -> accumulate_field.Value
			centroid.links.new(switch.outputs[0], accumulate_field.inputs[0])
			#group_input.Group ID -> accumulate_field.Group ID
			centroid.links.new(group_input.outputs[2], accumulate_field.inputs[1])
			#group_input.Group ID -> accumulate_field_001.Group ID
			centroid.links.new(group_input.outputs[2], accumulate_field_001.inputs[1])
			#group_input.Position -> switch.True
			centroid.links.new(group_input.outputs[0], switch.inputs[2])
			return centroid

		centroid = centroid_node_group()

		#initialize centre_on_selection node group
		def centre_on_selection_node_group():
			centre_on_selection = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Centre on Selection")

			centre_on_selection.color_tag = 'GEOMETRY'
			centre_on_selection.description = ""

			
			#centre_on_selection interface
			#Socket Atoms
			atoms_socket = centre_on_selection.interface.new_socket(name = "Atoms", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket.attribute_domain = 'POINT'
			atoms_socket.description = "Atoms that have been moved to object origin based on their group's calculated centroid"
			
			#Socket Offset
			offset_socket = centre_on_selection.interface.new_socket(name = "Offset", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			offset_socket.subtype = 'NONE'
			offset_socket.default_value = (0.0, 0.0, 0.0)
			offset_socket.min_value = -3.4028234663852886e+38
			offset_socket.max_value = 3.4028234663852886e+38
			offset_socket.attribute_domain = 'POINT'
			offset_socket.description = "The calculated vector offset applied to centre the points"
			
			#Socket Atoms
			atoms_socket_1 = centre_on_selection.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_1.attribute_domain = 'POINT'
			
			#Socket Selection
			selection_socket_1 = centre_on_selection.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_1.attribute_domain = 'POINT'
			selection_socket_1.hide_value = True
			selection_socket_1.description = "Selection within the groups to calculate the centroid for, which then affects all other points in the group"
			
			#Socket Group ID
			group_id_socket_1 = centre_on_selection.interface.new_socket(name = "Group ID", in_out='INPUT', socket_type = 'NodeSocketInt')
			group_id_socket_1.subtype = 'NONE'
			group_id_socket_1.default_value = 0
			group_id_socket_1.min_value = -2147483648
			group_id_socket_1.max_value = 2147483647
			group_id_socket_1.attribute_domain = 'POINT'
			group_id_socket_1.hide_value = True
			group_id_socket_1.description = "An optional `Group ID` value to calculate the centroid and offset points on a per-group basis"
			
			
			#initialize centre_on_selection nodes
			#node Group Output
			group_output_1 = centre_on_selection.nodes.new("NodeGroupOutput")
			group_output_1.name = "Group Output"
			group_output_1.is_active_output = True
			
			#node Group Input
			group_input_1 = centre_on_selection.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			
			#node Set Position
			set_position = centre_on_selection.nodes.new("GeometryNodeSetPosition")
			set_position.name = "Set Position"
			#Selection
			set_position.inputs[1].default_value = True
			#Position
			set_position.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Vector Math.001
			vector_math_001 = centre_on_selection.nodes.new("ShaderNodeVectorMath")
			vector_math_001.name = "Vector Math.001"
			vector_math_001.operation = 'SCALE'
			#Scale
			vector_math_001.inputs[3].default_value = -1.0
			
			#node Group
			group = centre_on_selection.nodes.new("GeometryNodeGroup")
			group.name = "Group"
			group.node_tree = centroid
			#Socket_4
			group.inputs[0].default_value = (0.0, 0.0, 0.0)
			
			
			
			
			#Set locations
			group_output_1.location = (80.0, 120.0)
			group_input_1.location = (-520.0, 100.0)
			set_position.location = (-100.0, 120.0)
			vector_math_001.location = (-100.0, -40.0)
			group.location = (-283.7733154296875, -40.0)
			
			#Set dimensions
			group_output_1.width, group_output_1.height = 140.0, 100.0
			group_input_1.width, group_input_1.height = 140.0, 100.0
			set_position.width, set_position.height = 140.0, 100.0
			vector_math_001.width, vector_math_001.height = 140.0, 100.0
			group.width, group.height = 163.9580078125, 100.0
			
			#initialize centre_on_selection links
			#group_input_1.Atoms -> set_position.Geometry
			centre_on_selection.links.new(group_input_1.outputs[0], set_position.inputs[0])
			#set_position.Geometry -> group_output_1.Atoms
			centre_on_selection.links.new(set_position.outputs[0], group_output_1.inputs[0])
			#group.Centroid -> vector_math_001.Vector
			centre_on_selection.links.new(group.outputs[0], vector_math_001.inputs[0])
			#group_input_1.Selection -> group.Selection
			centre_on_selection.links.new(group_input_1.outputs[1], group.inputs[1])
			#vector_math_001.Vector -> set_position.Offset
			centre_on_selection.links.new(vector_math_001.outputs[0], set_position.inputs[3])
			#vector_math_001.Vector -> group_output_1.Offset
			centre_on_selection.links.new(vector_math_001.outputs[0], group_output_1.inputs[1])
			#group_input_1.Group ID -> group.Group ID
			centre_on_selection.links.new(group_input_1.outputs[2], group.inputs[2])
			return centre_on_selection

		centre_on_selection = centre_on_selection_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Centre on Selection", type = 'NODES')
		mod.node_group = centre_on_selection
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Centre_on_Selection.bl_idname)
			
def register():
	bpy.utils.register_class(Centre_on_Selection)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Centre_on_Selection)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
