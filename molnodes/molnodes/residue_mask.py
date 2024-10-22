bl_info = {
	"name" : "Residue Mask",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Residue_Mask(bpy.types.Operator):
	bl_idname = "node.residue_mask"
	bl_label = "Residue Mask"
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
			is_valid_socket.default_value = True
			is_valid_socket.attribute_domain = 'POINT'
			is_valid_socket.description = "Whether the pick is valid. Pick is only valid if a single item is picked in the Group ID"
			
			#Socket Index
			index_socket = group_pick.interface.new_socket(name = "Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			index_socket.default_value = 0
			index_socket.min_value = 0
			index_socket.max_value = 2147483647
			index_socket.subtype = 'NONE'
			index_socket.attribute_domain = 'POINT'
			index_socket.description = "Index of picked item. Returns -1 if not a valid pick."
			
			#Socket Pick
			pick_socket = group_pick.interface.new_socket(name = "Pick", in_out='INPUT', socket_type = 'NodeSocketBool')
			pick_socket.default_value = False
			pick_socket.attribute_domain = 'POINT'
			pick_socket.hide_value = True
			pick_socket.description = "True for the item to pick from the group. If number of picks is 0 or more than 1, not a valid pick"
			
			#Socket Group ID
			group_id_socket = group_pick.interface.new_socket(name = "Group ID", in_out='INPUT', socket_type = 'NodeSocketInt')
			group_id_socket.default_value = 0
			group_id_socket.min_value = -2147483648
			group_id_socket.max_value = 2147483647
			group_id_socket.subtype = 'NONE'
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

		#initialize group_pick_vector node group
		def group_pick_vector_node_group():
			group_pick_vector = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Group Pick Vector")

			group_pick_vector.color_tag = 'INPUT'
			group_pick_vector.description = ""

			
			#group_pick_vector interface
			#Socket Is Valid
			is_valid_socket_1 = group_pick_vector.interface.new_socket(name = "Is Valid", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_valid_socket_1.default_value = False
			is_valid_socket_1.attribute_domain = 'POINT'
			is_valid_socket_1.description = "The pick for this group is valid"
			
			#Socket Index
			index_socket_1 = group_pick_vector.interface.new_socket(name = "Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			index_socket_1.default_value = 0
			index_socket_1.min_value = -2147483648
			index_socket_1.max_value = 2147483647
			index_socket_1.subtype = 'NONE'
			index_socket_1.attribute_domain = 'POINT'
			index_socket_1.description = "Picked Index for the Group"
			
			#Socket Vector
			vector_socket = group_pick_vector.interface.new_socket(name = "Vector", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			vector_socket.default_value = (0.0, 0.0, 0.0)
			vector_socket.min_value = -3.4028234663852886e+38
			vector_socket.max_value = 3.4028234663852886e+38
			vector_socket.subtype = 'NONE'
			vector_socket.attribute_domain = 'POINT'
			vector_socket.description = "Picked vector for the group"
			
			#Socket Pick
			pick_socket_1 = group_pick_vector.interface.new_socket(name = "Pick", in_out='INPUT', socket_type = 'NodeSocketBool')
			pick_socket_1.default_value = False
			pick_socket_1.attribute_domain = 'POINT'
			pick_socket_1.hide_value = True
			
			#Socket Group ID
			group_id_socket_1 = group_pick_vector.interface.new_socket(name = "Group ID", in_out='INPUT', socket_type = 'NodeSocketInt')
			group_id_socket_1.default_value = 0
			group_id_socket_1.min_value = -2147483648
			group_id_socket_1.max_value = 2147483647
			group_id_socket_1.subtype = 'NONE'
			group_id_socket_1.attribute_domain = 'POINT'
			
			#Socket Position
			position_socket = group_pick_vector.interface.new_socket(name = "Position", in_out='INPUT', socket_type = 'NodeSocketVector')
			position_socket.default_value = (0.0, 0.0, 0.0)
			position_socket.min_value = -3.4028234663852886e+38
			position_socket.max_value = 3.4028234663852886e+38
			position_socket.subtype = 'NONE'
			position_socket.attribute_domain = 'POINT'
			position_socket.description = "Vector field to pick vlaue for, defaults to Position"
			
			
			#initialize group_pick_vector nodes
			#node Group Output
			group_output_1 = group_pick_vector.nodes.new("NodeGroupOutput")
			group_output_1.name = "Group Output"
			group_output_1.is_active_output = True
			
			#node Group Input
			group_input_1 = group_pick_vector.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			
			#node Evaluate at Index.001
			evaluate_at_index_001 = group_pick_vector.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001.name = "Evaluate at Index.001"
			evaluate_at_index_001.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_001.domain = 'POINT'
			
			#node Switch.002
			switch_002 = group_pick_vector.nodes.new("GeometryNodeSwitch")
			switch_002.name = "Switch.002"
			switch_002.input_type = 'VECTOR'
			#False
			switch_002.inputs[1].default_value = (0.0, 0.0, 0.0)
			
			#node Group
			group = group_pick_vector.nodes.new("GeometryNodeGroup")
			group.name = "Group"
			group.node_tree = group_pick
			
			
			
			
			#Set locations
			group_output_1.location = (-40.0, -20.0)
			group_input_1.location = (-740.0, -80.0)
			evaluate_at_index_001.location = (-380.0, -180.0)
			switch_002.location = (-220.0, -60.0)
			group.location = (-560.0, -20.0)
			
			#Set dimensions
			group_output_1.width, group_output_1.height = 140.0, 100.0
			group_input_1.width, group_input_1.height = 140.0, 100.0
			evaluate_at_index_001.width, evaluate_at_index_001.height = 132.09918212890625, 100.0
			switch_002.width, switch_002.height = 140.0, 100.0
			group.width, group.height = 140.0, 100.0
			
			#initialize group_pick_vector links
			#group.Is Valid -> switch_002.Switch
			group_pick_vector.links.new(group.outputs[0], switch_002.inputs[0])
			#group.Index -> evaluate_at_index_001.Index
			group_pick_vector.links.new(group.outputs[1], evaluate_at_index_001.inputs[0])
			#evaluate_at_index_001.Value -> switch_002.True
			group_pick_vector.links.new(evaluate_at_index_001.outputs[0], switch_002.inputs[2])
			#group.Index -> group_output_1.Index
			group_pick_vector.links.new(group.outputs[1], group_output_1.inputs[1])
			#group.Is Valid -> group_output_1.Is Valid
			group_pick_vector.links.new(group.outputs[0], group_output_1.inputs[0])
			#switch_002.Output -> group_output_1.Vector
			group_pick_vector.links.new(switch_002.outputs[0], group_output_1.inputs[2])
			#group_input_1.Group ID -> group.Group ID
			group_pick_vector.links.new(group_input_1.outputs[1], group.inputs[1])
			#group_input_1.Pick -> group.Pick
			group_pick_vector.links.new(group_input_1.outputs[0], group.inputs[0])
			#group_input_1.Position -> evaluate_at_index_001.Value
			group_pick_vector.links.new(group_input_1.outputs[2], evaluate_at_index_001.inputs[1])
			return group_pick_vector

		group_pick_vector = group_pick_vector_node_group()

		#initialize offset_integer node group
		def offset_integer_node_group():
			offset_integer = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Offset Integer")

			offset_integer.color_tag = 'CONVERTER'
			offset_integer.description = ""

			
			#offset_integer interface
			#Socket Value
			value_socket = offset_integer.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			value_socket.default_value = 0
			value_socket.min_value = -2147483648
			value_socket.max_value = 2147483647
			value_socket.subtype = 'NONE'
			value_socket.attribute_domain = 'POINT'
			
			#Socket Index
			index_socket_2 = offset_integer.interface.new_socket(name = "Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			index_socket_2.default_value = 0
			index_socket_2.min_value = 0
			index_socket_2.max_value = 2147483647
			index_socket_2.subtype = 'NONE'
			index_socket_2.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_1 = offset_integer.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketInt')
			value_socket_1.default_value = 0
			value_socket_1.min_value = -2147483648
			value_socket_1.max_value = 2147483647
			value_socket_1.subtype = 'NONE'
			value_socket_1.attribute_domain = 'POINT'
			value_socket_1.hide_value = True
			
			#Socket Offset
			offset_socket = offset_integer.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket.default_value = 0
			offset_socket.min_value = -2147483648
			offset_socket.max_value = 2147483647
			offset_socket.subtype = 'NONE'
			offset_socket.attribute_domain = 'POINT'
			
			
			#initialize offset_integer nodes
			#node Group Output
			group_output_2 = offset_integer.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Group Input
			group_input_2 = offset_integer.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
			#node Evaluate at Index
			evaluate_at_index = offset_integer.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index.name = "Evaluate at Index"
			evaluate_at_index.data_type = 'INT'
			evaluate_at_index.domain = 'POINT'
			
			#node Math
			math = offset_integer.nodes.new("ShaderNodeMath")
			math.name = "Math"
			math.operation = 'ADD'
			math.use_clamp = False
			
			
			
			
			#Set locations
			group_output_2.location = (190.0, 0.0)
			group_input_2.location = (-412.72760009765625, 0.2001800537109375)
			evaluate_at_index.location = (0.0, 0.0)
			math.location = (-217.90158081054688, 69.93922424316406)
			
			#Set dimensions
			group_output_2.width, group_output_2.height = 140.0, 100.0
			group_input_2.width, group_input_2.height = 140.0, 100.0
			evaluate_at_index.width, evaluate_at_index.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			
			#initialize offset_integer links
			#evaluate_at_index.Value -> group_output_2.Value
			offset_integer.links.new(evaluate_at_index.outputs[0], group_output_2.inputs[0])
			#group_input_2.Index -> math.Value
			offset_integer.links.new(group_input_2.outputs[0], math.inputs[0])
			#group_input_2.Offset -> math.Value
			offset_integer.links.new(group_input_2.outputs[2], math.inputs[1])
			#math.Value -> evaluate_at_index.Index
			offset_integer.links.new(math.outputs[0], evaluate_at_index.inputs[0])
			#group_input_2.Value -> evaluate_at_index.Value
			offset_integer.links.new(group_input_2.outputs[1], evaluate_at_index.inputs[1])
			return offset_integer

		offset_integer = offset_integer_node_group()

		#initialize res_group_id node group
		def res_group_id_node_group():
			res_group_id = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Res Group ID")

			res_group_id.color_tag = 'INPUT'
			res_group_id.description = ""

			
			#res_group_id interface
			#Socket Unique Group ID
			unique_group_id_socket = res_group_id.interface.new_socket(name = "Unique Group ID", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			unique_group_id_socket.default_value = 0
			unique_group_id_socket.min_value = -2147483648
			unique_group_id_socket.max_value = 2147483647
			unique_group_id_socket.subtype = 'NONE'
			unique_group_id_socket.attribute_domain = 'POINT'
			unique_group_id_socket.description = "A unique Group ID for eash residue"
			
			
			#initialize res_group_id nodes
			#node Group Output
			group_output_3 = res_group_id.nodes.new("NodeGroupOutput")
			group_output_3.name = "Group Output"
			group_output_3.is_active_output = True
			
			#node Group Input
			group_input_3 = res_group_id.nodes.new("NodeGroupInput")
			group_input_3.name = "Group Input"
			
			#node Named Attribute.001
			named_attribute_001 = res_group_id.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.data_type = 'INT'
			#Name
			named_attribute_001.inputs[0].default_value = "res_id"
			
			#node Named Attribute.002
			named_attribute_002 = res_group_id.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002.name = "Named Attribute.002"
			named_attribute_002.data_type = 'INT'
			#Name
			named_attribute_002.inputs[0].default_value = "atom_name"
			
			#node Compare.002
			compare_002 = res_group_id.nodes.new("FunctionNodeCompare")
			compare_002.name = "Compare.002"
			compare_002.data_type = 'INT'
			compare_002.mode = 'ELEMENT'
			compare_002.operation = 'EQUAL'
			#B_INT
			compare_002.inputs[3].default_value = 1
			
			#node Compare.001
			compare_001 = res_group_id.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'INT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'NOT_EQUAL'
			
			#node Boolean Math
			boolean_math = res_group_id.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'OR'
			
			#node Accumulate Field.001
			accumulate_field_001 = res_group_id.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_001.name = "Accumulate Field.001"
			accumulate_field_001.data_type = 'INT'
			accumulate_field_001.domain = 'POINT'
			#Group Index
			accumulate_field_001.inputs[1].default_value = 0
			
			#node Group.001
			group_001 = res_group_id.nodes.new("GeometryNodeGroup")
			group_001.name = "Group.001"
			group_001.node_tree = offset_integer
			#Socket_1
			group_001.inputs[0].default_value = 0
			#Socket_2
			group_001.inputs[2].default_value = -1
			
			#node Math
			math_1 = res_group_id.nodes.new("ShaderNodeMath")
			math_1.name = "Math"
			math_1.operation = 'SUBTRACT'
			math_1.use_clamp = False
			#Value_001
			math_1.inputs[1].default_value = 1.0
			
			#node Frame
			frame = res_group_id.nodes.new("NodeFrame")
			frame.name = "Frame"
			frame.label_size = 20
			frame.shrink = True
			
			#node Reroute
			reroute = res_group_id.nodes.new("NodeReroute")
			reroute.label = "subtracting 1 from the leading, but things don't work right"
			reroute.name = "Reroute"
			#node Reroute.001
			reroute_001_1 = res_group_id.nodes.new("NodeReroute")
			reroute_001_1.name = "Reroute.001"
			#node Reroute.002
			reroute_002_1 = res_group_id.nodes.new("NodeReroute")
			reroute_002_1.label = "In theory we can just use the trailing value instead of"
			reroute_002_1.name = "Reroute.002"
			#node Reroute.003
			reroute_003 = res_group_id.nodes.new("NodeReroute")
			reroute_003.name = "Reroute.003"
			
			
			#Set parents
			math_1.parent = frame
			reroute.parent = frame
			reroute_001_1.parent = frame
			reroute_002_1.parent = frame
			reroute_003.parent = frame
			
			#Set locations
			group_output_3.location = (900.0, 160.0)
			group_input_3.location = (-420.0, 160.0)
			named_attribute_001.location = (-240.0, 0.0)
			named_attribute_002.location = (-250.0, 160.0)
			compare_002.location = (-70.0, 160.0)
			compare_001.location = (-70.0, 0.0)
			boolean_math.location = (90.0, 160.0)
			accumulate_field_001.location = (250.0, 160.0)
			group_001.location = (-70.0, -160.0)
			math_1.location = (519.2361450195312, 166.28671264648438)
			frame.location = (95.0, -20.0)
			reroute.location = (554.4125366210938, 257.9646911621094)
			reroute_001_1.location = (739.2361450195312, 306.2867126464844)
			reroute_002_1.location = (551.13134765625, 297.3444519042969)
			reroute_003.location = (379.23614501953125, 306.2867126464844)
			
			#Set dimensions
			group_output_3.width, group_output_3.height = 140.0, 100.0
			group_input_3.width, group_input_3.height = 140.0, 100.0
			named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
			named_attribute_002.width, named_attribute_002.height = 140.0, 100.0
			compare_002.width, compare_002.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			accumulate_field_001.width, accumulate_field_001.height = 140.0, 100.0
			group_001.width, group_001.height = 140.0, 100.0
			math_1.width, math_1.height = 140.0, 100.0
			frame.width, frame.height = 436.0, 356.2867126464844
			reroute.width, reroute.height = 16.0, 100.0
			reroute_001_1.width, reroute_001_1.height = 16.0, 100.0
			reroute_002_1.width, reroute_002_1.height = 16.0, 100.0
			reroute_003.width, reroute_003.height = 16.0, 100.0
			
			#initialize res_group_id links
			#compare_002.Result -> boolean_math.Boolean
			res_group_id.links.new(compare_002.outputs[0], boolean_math.inputs[0])
			#named_attribute_001.Attribute -> compare_001.A
			res_group_id.links.new(named_attribute_001.outputs[0], compare_001.inputs[2])
			#named_attribute_001.Attribute -> group_001.Value
			res_group_id.links.new(named_attribute_001.outputs[0], group_001.inputs[1])
			#compare_001.Result -> boolean_math.Boolean
			res_group_id.links.new(compare_001.outputs[0], boolean_math.inputs[1])
			#named_attribute_002.Attribute -> compare_002.A
			res_group_id.links.new(named_attribute_002.outputs[0], compare_002.inputs[2])
			#group_001.Value -> compare_001.B
			res_group_id.links.new(group_001.outputs[0], compare_001.inputs[3])
			#accumulate_field_001.Leading -> math_1.Value
			res_group_id.links.new(accumulate_field_001.outputs[0], math_1.inputs[0])
			#math_1.Value -> group_output_3.Unique Group ID
			res_group_id.links.new(math_1.outputs[0], group_output_3.inputs[0])
			#boolean_math.Boolean -> accumulate_field_001.Value
			res_group_id.links.new(boolean_math.outputs[0], accumulate_field_001.inputs[0])
			return res_group_id

		res_group_id = res_group_id_node_group()

		#initialize residue_mask node group
		def residue_mask_node_group():
			residue_mask = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Residue Mask")

			residue_mask.color_tag = 'INPUT'
			residue_mask.description = ""

			
			#residue_mask interface
			#Socket Is Valid
			is_valid_socket_2 = residue_mask.interface.new_socket(name = "Is Valid", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_valid_socket_2.default_value = False
			is_valid_socket_2.attribute_domain = 'POINT'
			is_valid_socket_2.description = "Group contains only one occurrance of the selected atom. None or more than one returns False"
			
			#Socket Index
			index_socket_3 = residue_mask.interface.new_socket(name = "Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			index_socket_3.default_value = 0
			index_socket_3.min_value = -2147483648
			index_socket_3.max_value = 2147483647
			index_socket_3.subtype = 'NONE'
			index_socket_3.attribute_domain = 'POINT'
			index_socket_3.description = "Index for the group's atom with specified name, returns -1 if not valid"
			
			#Socket Position
			position_socket_1 = residue_mask.interface.new_socket(name = "Position", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			position_socket_1.default_value = (0.0, 0.0, 0.0)
			position_socket_1.min_value = -3.4028234663852886e+38
			position_socket_1.max_value = 3.4028234663852886e+38
			position_socket_1.subtype = 'NONE'
			position_socket_1.attribute_domain = 'POINT'
			position_socket_1.description = "Position of the picked point in the group, returns (0, 0, 0) if not valid"
			
			#Socket Group ID
			group_id_socket_2 = residue_mask.interface.new_socket(name = "Group ID", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			group_id_socket_2.default_value = 0
			group_id_socket_2.min_value = -2147483648
			group_id_socket_2.max_value = 2147483647
			group_id_socket_2.subtype = 'NONE'
			group_id_socket_2.attribute_domain = 'POINT'
			
			#Socket atom_name
			atom_name_socket = residue_mask.interface.new_socket(name = "atom_name", in_out='INPUT', socket_type = 'NodeSocketInt')
			atom_name_socket.default_value = 1
			atom_name_socket.min_value = 2
			atom_name_socket.max_value = 2147483647
			atom_name_socket.subtype = 'NONE'
			atom_name_socket.attribute_domain = 'POINT'
			atom_name_socket.description = "Atom to pick from the group"
			
			#Socket Use Fallback
			use_fallback_socket = residue_mask.interface.new_socket(name = "Use Fallback", in_out='INPUT', socket_type = 'NodeSocketBool')
			use_fallback_socket.default_value = True
			use_fallback_socket.attribute_domain = 'POINT'
			use_fallback_socket.description = "Uses a calculated Unique Group ID as a fallback. Disabling can increase performance if pre-computing a Group ID for multiple nodes"
			
			#Socket Group ID
			group_id_socket_3 = residue_mask.interface.new_socket(name = "Group ID", in_out='INPUT', socket_type = 'NodeSocketInt')
			group_id_socket_3.default_value = 0
			group_id_socket_3.min_value = -2147483648
			group_id_socket_3.max_value = 2147483647
			group_id_socket_3.subtype = 'NONE'
			group_id_socket_3.attribute_domain = 'POINT'
			
			
			#initialize residue_mask nodes
			#node Compare
			compare = residue_mask.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'EQUAL'
			
			#node Group Input
			group_input_4 = residue_mask.nodes.new("NodeGroupInput")
			group_input_4.name = "Group Input"
			
			#node Named Attribute
			named_attribute = residue_mask.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'INT'
			#Name
			named_attribute.inputs[0].default_value = "atom_name"
			
			#node Group Output
			group_output_4 = residue_mask.nodes.new("NodeGroupOutput")
			group_output_4.name = "Group Output"
			group_output_4.is_active_output = True
			
			#node Group
			group_1 = residue_mask.nodes.new("GeometryNodeGroup")
			group_1.name = "Group"
			group_1.node_tree = group_pick_vector
			#Socket_5
			group_1.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Group.002
			group_002 = residue_mask.nodes.new("GeometryNodeGroup")
			group_002.name = "Group.002"
			group_002.node_tree = res_group_id
			
			#node Switch
			switch_1 = residue_mask.nodes.new("GeometryNodeSwitch")
			switch_1.name = "Switch"
			switch_1.input_type = 'INT'
			
			
			
			
			#Set locations
			compare.location = (40.0, 340.0)
			group_input_4.location = (-140.0, 200.0)
			named_attribute.location = (-140.0, 340.0)
			group_output_4.location = (420.0, 340.0)
			group_1.location = (220.0, 340.0)
			group_002.location = (-140.0, 60.0)
			switch_1.location = (40.0, 180.0)
			
			#Set dimensions
			compare.width, compare.height = 140.0, 100.0
			group_input_4.width, group_input_4.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			group_output_4.width, group_output_4.height = 140.0, 100.0
			group_1.width, group_1.height = 164.60528564453125, 100.0
			group_002.width, group_002.height = 140.0, 100.0
			switch_1.width, switch_1.height = 140.0, 100.0
			
			#initialize residue_mask links
			#named_attribute.Attribute -> compare.A
			residue_mask.links.new(named_attribute.outputs[0], compare.inputs[2])
			#group_input_4.atom_name -> compare.B
			residue_mask.links.new(group_input_4.outputs[0], compare.inputs[3])
			#group_1.Index -> group_output_4.Index
			residue_mask.links.new(group_1.outputs[1], group_output_4.inputs[1])
			#group_1.Vector -> group_output_4.Position
			residue_mask.links.new(group_1.outputs[2], group_output_4.inputs[2])
			#group_1.Is Valid -> group_output_4.Is Valid
			residue_mask.links.new(group_1.outputs[0], group_output_4.inputs[0])
			#compare.Result -> group_1.Pick
			residue_mask.links.new(compare.outputs[0], group_1.inputs[0])
			#group_input_4.Use Fallback -> switch_1.Switch
			residue_mask.links.new(group_input_4.outputs[1], switch_1.inputs[0])
			#group_input_4.Group ID -> switch_1.False
			residue_mask.links.new(group_input_4.outputs[2], switch_1.inputs[1])
			#switch_1.Output -> group_1.Group ID
			residue_mask.links.new(switch_1.outputs[0], group_1.inputs[1])
			#group_002.Unique Group ID -> switch_1.True
			residue_mask.links.new(group_002.outputs[0], switch_1.inputs[2])
			#switch_1.Output -> group_output_4.Group ID
			residue_mask.links.new(switch_1.outputs[0], group_output_4.inputs[3])
			return residue_mask

		residue_mask = residue_mask_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Residue Mask", type = 'NODES')
		mod.node_group = residue_mask
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Residue_Mask.bl_idname)
			
def register():
	bpy.utils.register_class(Residue_Mask)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Residue_Mask)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
