bl_info = {
	"name" : "Dihedral Psi",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Dihedral_Psi(bpy.types.Operator):
	bl_idname = "node.dihedral_psi"
	bl_label = "Dihedral Psi"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize vector_angle node group
		def vector_angle_node_group():
			vector_angle = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Vector Angle")

			vector_angle.color_tag = 'VECTOR'
			vector_angle.description = ""

			
			#vector_angle interface
			#Socket Angle
			angle_socket = vector_angle.interface.new_socket(name = "Angle", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			angle_socket.default_value = 0.0
			angle_socket.min_value = -3.4028234663852886e+38
			angle_socket.max_value = 3.4028234663852886e+38
			angle_socket.subtype = 'ANGLE'
			angle_socket.attribute_domain = 'POINT'
			angle_socket.description = "Angle between the two given vectors in radians"
			
			#Socket A
			a_socket = vector_angle.interface.new_socket(name = "A", in_out='INPUT', socket_type = 'NodeSocketVector')
			a_socket.default_value = (0.0, 0.0, 0.0)
			a_socket.min_value = -10000.0
			a_socket.max_value = 10000.0
			a_socket.subtype = 'NONE'
			a_socket.attribute_domain = 'POINT'
			
			#Socket B
			b_socket = vector_angle.interface.new_socket(name = "B", in_out='INPUT', socket_type = 'NodeSocketVector')
			b_socket.default_value = (0.0, 0.0, 0.0)
			b_socket.min_value = -10000.0
			b_socket.max_value = 10000.0
			b_socket.subtype = 'NONE'
			b_socket.attribute_domain = 'POINT'
			
			
			#initialize vector_angle nodes
			#node Group Input
			group_input = vector_angle.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Vector Math.002
			vector_math_002 = vector_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_002.name = "Vector Math.002"
			vector_math_002.operation = 'NORMALIZE'
			
			#node Vector Math.001
			vector_math_001 = vector_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_001.name = "Vector Math.001"
			vector_math_001.operation = 'NORMALIZE'
			
			#node Vector Math
			vector_math = vector_angle.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.operation = 'DOT_PRODUCT'
			
			#node Math
			math = vector_angle.nodes.new("ShaderNodeMath")
			math.name = "Math"
			math.operation = 'ARCCOSINE'
			math.use_clamp = False
			
			#node Group Output
			group_output = vector_angle.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			
			
			
			#Set locations
			group_input.location = (-360.0, 0.0)
			vector_math_002.location = (-160.0, -60.0)
			vector_math_001.location = (-160.0, 60.0)
			vector_math.location = (0.0, 60.0)
			math.location = (160.0, 60.0)
			group_output.location = (340.0, 60.0)
			
			#Set dimensions
			group_input.width, group_input.height = 140.0, 100.0
			vector_math_002.width, vector_math_002.height = 140.0, 100.0
			vector_math_001.width, vector_math_001.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			
			#initialize vector_angle links
			#vector_math.Value -> math.Value
			vector_angle.links.new(vector_math.outputs[1], math.inputs[0])
			#vector_math_002.Vector -> vector_math.Vector
			vector_angle.links.new(vector_math_002.outputs[0], vector_math.inputs[1])
			#vector_math_001.Vector -> vector_math.Vector
			vector_angle.links.new(vector_math_001.outputs[0], vector_math.inputs[0])
			#math.Value -> group_output.Angle
			vector_angle.links.new(math.outputs[0], group_output.inputs[0])
			#group_input.A -> vector_math_001.Vector
			vector_angle.links.new(group_input.outputs[0], vector_math_001.inputs[0])
			#group_input.B -> vector_math_002.Vector
			vector_angle.links.new(group_input.outputs[1], vector_math_002.inputs[0])
			return vector_angle

		vector_angle = vector_angle_node_group()

		#initialize dihedral_angle node group
		def dihedral_angle_node_group():
			dihedral_angle = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Dihedral Angle")

			dihedral_angle.color_tag = 'VECTOR'
			dihedral_angle.description = ""

			
			#dihedral_angle interface
			#Socket Angle
			angle_socket_1 = dihedral_angle.interface.new_socket(name = "Angle", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			angle_socket_1.default_value = 0.0
			angle_socket_1.min_value = -3.4028234663852886e+38
			angle_socket_1.max_value = 3.4028234663852886e+38
			angle_socket_1.subtype = 'ANGLE'
			angle_socket_1.attribute_domain = 'POINT'
			angle_socket_1.description = "The angle between the vectors AB and CD, when made perpendicular to BC."
			
			#Socket BA⟂(BC)
			ba__bc__socket = dihedral_angle.interface.new_socket(name = "BA⟂(BC)", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			ba__bc__socket.default_value = (0.0, 0.0, 0.0)
			ba__bc__socket.min_value = -3.4028234663852886e+38
			ba__bc__socket.max_value = 3.4028234663852886e+38
			ba__bc__socket.subtype = 'NONE'
			ba__bc__socket.attribute_domain = 'POINT'
			ba__bc__socket.description = "The vector BA when made perpendicular to  the axis BC"
			
			#Socket CD⟂(BC)
			cd__bc__socket = dihedral_angle.interface.new_socket(name = "CD⟂(BC)", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			cd__bc__socket.default_value = (0.0, 0.0, 0.0)
			cd__bc__socket.min_value = -3.4028234663852886e+38
			cd__bc__socket.max_value = 3.4028234663852886e+38
			cd__bc__socket.subtype = 'NONE'
			cd__bc__socket.attribute_domain = 'POINT'
			cd__bc__socket.description = "The Vector CD when makde perpendicular to the axis BC"
			
			#Socket BC
			bc_socket = dihedral_angle.interface.new_socket(name = "BC", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			bc_socket.default_value = (0.0, 0.0, 0.0)
			bc_socket.min_value = -3.4028234663852886e+38
			bc_socket.max_value = 3.4028234663852886e+38
			bc_socket.subtype = 'NONE'
			bc_socket.attribute_domain = 'POINT'
			bc_socket.description = "The axis vector BC"
			
			#Socket A
			a_socket_1 = dihedral_angle.interface.new_socket(name = "A", in_out='INPUT', socket_type = 'NodeSocketVector')
			a_socket_1.default_value = (0.0, 0.0, 0.0)
			a_socket_1.min_value = -3.4028234663852886e+38
			a_socket_1.max_value = 3.4028234663852886e+38
			a_socket_1.subtype = 'NONE'
			a_socket_1.attribute_domain = 'POINT'
			a_socket_1.description = "First vector for the calculation, which draws a line to B"
			
			#Socket B
			b_socket_1 = dihedral_angle.interface.new_socket(name = "B", in_out='INPUT', socket_type = 'NodeSocketVector')
			b_socket_1.default_value = (0.0, 0.0, 0.0)
			b_socket_1.min_value = -3.4028234663852886e+38
			b_socket_1.max_value = 3.4028234663852886e+38
			b_socket_1.subtype = 'NONE'
			b_socket_1.attribute_domain = 'POINT'
			b_socket_1.description = "Second vector for the calculation, which receives a line from A and draws a line to C"
			
			#Socket C
			c_socket = dihedral_angle.interface.new_socket(name = "C", in_out='INPUT', socket_type = 'NodeSocketVector')
			c_socket.default_value = (0.0, 0.0, 0.0)
			c_socket.min_value = -3.4028234663852886e+38
			c_socket.max_value = 3.4028234663852886e+38
			c_socket.subtype = 'NONE'
			c_socket.attribute_domain = 'POINT'
			c_socket.description = "Third vector for the calculation, which receives a line from B and draws a line to D"
			
			#Socket D
			d_socket = dihedral_angle.interface.new_socket(name = "D", in_out='INPUT', socket_type = 'NodeSocketVector')
			d_socket.default_value = (0.0, 0.0, 0.0)
			d_socket.min_value = -3.4028234663852886e+38
			d_socket.max_value = 3.4028234663852886e+38
			d_socket.subtype = 'NONE'
			d_socket.attribute_domain = 'POINT'
			d_socket.description = "Last vector for the calculation, which is the end point of the line from D"
			
			
			#initialize dihedral_angle nodes
			#node Vector Math.003
			vector_math_003 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_003.name = "Vector Math.003"
			vector_math_003.operation = 'SUBTRACT'
			
			#node Vector Math.004
			vector_math_004 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_004.name = "Vector Math.004"
			vector_math_004.operation = 'SUBTRACT'
			
			#node Vector Math.006
			vector_math_006 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_006.name = "Vector Math.006"
			vector_math_006.operation = 'SUBTRACT'
			
			#node Vector Math.007
			vector_math_007 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_007.name = "Vector Math.007"
			vector_math_007.operation = 'PROJECT'
			
			#node Vector Math.009
			vector_math_009 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_009.name = "Vector Math.009"
			vector_math_009.operation = 'PROJECT'
			
			#node Vector Math.008
			vector_math_008 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_008.name = "Vector Math.008"
			vector_math_008.operation = 'SUBTRACT'
			
			#node Vector Math.010
			vector_math_010 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_010.name = "Vector Math.010"
			vector_math_010.operation = 'SUBTRACT'
			
			#node MN_utils_vector_angle.002
			mn_utils_vector_angle_002 = dihedral_angle.nodes.new("GeometryNodeGroup")
			mn_utils_vector_angle_002.label = "Vector Angle"
			mn_utils_vector_angle_002.name = "MN_utils_vector_angle.002"
			mn_utils_vector_angle_002.node_tree = vector_angle
			
			#node Group Output
			group_output_1 = dihedral_angle.nodes.new("NodeGroupOutput")
			group_output_1.name = "Group Output"
			group_output_1.is_active_output = True
			
			#node Reroute.002
			reroute_002 = dihedral_angle.nodes.new("NodeReroute")
			reroute_002.name = "Reroute.002"
			#node Reroute.001
			reroute_001 = dihedral_angle.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			#node Vector Math
			vector_math_1 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_1.name = "Vector Math"
			vector_math_1.operation = 'CROSS_PRODUCT'
			
			#node Vector Math.001
			vector_math_001_1 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_001_1.name = "Vector Math.001"
			vector_math_001_1.operation = 'DOT_PRODUCT'
			
			#node Math.001
			math_001 = dihedral_angle.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.operation = 'SIGN'
			math_001.use_clamp = False
			
			#node Reroute
			reroute = dihedral_angle.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Math
			math_1 = dihedral_angle.nodes.new("ShaderNodeMath")
			math_1.name = "Math"
			math_1.operation = 'MULTIPLY'
			math_1.use_clamp = False
			
			#node Group Input.003
			group_input_003 = dihedral_angle.nodes.new("NodeGroupInput")
			group_input_003.name = "Group Input.003"
			group_input_003.outputs[0].hide = True
			group_input_003.outputs[1].hide = True
			group_input_003.outputs[2].hide = True
			group_input_003.outputs[4].hide = True
			
			#node Group Input.001
			group_input_001 = dihedral_angle.nodes.new("NodeGroupInput")
			group_input_001.name = "Group Input.001"
			group_input_001.outputs[1].hide = True
			group_input_001.outputs[2].hide = True
			group_input_001.outputs[3].hide = True
			group_input_001.outputs[4].hide = True
			
			#node Group Input
			group_input_1 = dihedral_angle.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			group_input_1.outputs[0].hide = True
			group_input_1.outputs[2].hide = True
			group_input_1.outputs[3].hide = True
			group_input_1.outputs[4].hide = True
			
			#node Group Input.002
			group_input_002 = dihedral_angle.nodes.new("NodeGroupInput")
			group_input_002.name = "Group Input.002"
			group_input_002.outputs[0].hide = True
			group_input_002.outputs[1].hide = True
			group_input_002.outputs[3].hide = True
			group_input_002.outputs[4].hide = True
			
			
			
			
			#Set locations
			vector_math_003.location = (-142.68453979492188, 25.911895751953125)
			vector_math_004.location = (-140.0, 440.0)
			vector_math_006.location = (-140.0, 180.0)
			vector_math_007.location = (80.0, 320.0)
			vector_math_009.location = (80.0, -80.0)
			vector_math_008.location = (80.0, 460.0)
			vector_math_010.location = (80.0, 60.0)
			mn_utils_vector_angle_002.location = (420.0, 420.0)
			group_output_1.location = (920.0, 320.0)
			reroute_002.location = (300.0, 260.0)
			reroute_001.location = (300.0, 240.0)
			vector_math_1.location = (420.0, 180.0)
			vector_math_001_1.location = (420.0, 40.0)
			math_001.location = (580.0, 40.0)
			reroute.location = (300.0, 220.0)
			math_1.location = (640.0, 420.0)
			group_input_003.location = (-440.0, 0.0)
			group_input_001.location = (-440.0, 420.0)
			group_input_1.location = (-440.0, 280.0)
			group_input_002.location = (-440.0, 140.0)
			
			#Set dimensions
			vector_math_003.width, vector_math_003.height = 140.0, 100.0
			vector_math_004.width, vector_math_004.height = 140.0, 100.0
			vector_math_006.width, vector_math_006.height = 140.0, 100.0
			vector_math_007.width, vector_math_007.height = 140.0, 100.0
			vector_math_009.width, vector_math_009.height = 140.0, 100.0
			vector_math_008.width, vector_math_008.height = 140.0, 100.0
			vector_math_010.width, vector_math_010.height = 140.0, 100.0
			mn_utils_vector_angle_002.width, mn_utils_vector_angle_002.height = 200.0, 100.0
			group_output_1.width, group_output_1.height = 140.0, 100.0
			reroute_002.width, reroute_002.height = 16.0, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			vector_math_1.width, vector_math_1.height = 140.0, 100.0
			vector_math_001_1.width, vector_math_001_1.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			math_1.width, math_1.height = 140.0, 100.0
			group_input_003.width, group_input_003.height = 140.0, 100.0
			group_input_001.width, group_input_001.height = 140.0, 100.0
			group_input_1.width, group_input_1.height = 140.0, 100.0
			group_input_002.width, group_input_002.height = 140.0, 100.0
			
			#initialize dihedral_angle links
			#vector_math_007.Vector -> vector_math_008.Vector
			dihedral_angle.links.new(vector_math_007.outputs[0], vector_math_008.inputs[1])
			#vector_math_009.Vector -> vector_math_010.Vector
			dihedral_angle.links.new(vector_math_009.outputs[0], vector_math_010.inputs[1])
			#vector_math_004.Vector -> vector_math_007.Vector
			dihedral_angle.links.new(vector_math_004.outputs[0], vector_math_007.inputs[0])
			#vector_math_006.Vector -> vector_math_007.Vector
			dihedral_angle.links.new(vector_math_006.outputs[0], vector_math_007.inputs[1])
			#reroute_002.Output -> mn_utils_vector_angle_002.A
			dihedral_angle.links.new(reroute_002.outputs[0], mn_utils_vector_angle_002.inputs[0])
			#vector_math_004.Vector -> vector_math_008.Vector
			dihedral_angle.links.new(vector_math_004.outputs[0], vector_math_008.inputs[0])
			#vector_math_003.Vector -> vector_math_010.Vector
			dihedral_angle.links.new(vector_math_003.outputs[0], vector_math_010.inputs[0])
			#vector_math_003.Vector -> vector_math_009.Vector
			dihedral_angle.links.new(vector_math_003.outputs[0], vector_math_009.inputs[0])
			#vector_math_006.Vector -> vector_math_009.Vector
			dihedral_angle.links.new(vector_math_006.outputs[0], vector_math_009.inputs[1])
			#vector_math_006.Vector -> reroute.Input
			dihedral_angle.links.new(vector_math_006.outputs[0], reroute.inputs[0])
			#reroute_001.Output -> mn_utils_vector_angle_002.B
			dihedral_angle.links.new(reroute_001.outputs[0], mn_utils_vector_angle_002.inputs[1])
			#vector_math_1.Vector -> vector_math_001_1.Vector
			dihedral_angle.links.new(vector_math_1.outputs[0], vector_math_001_1.inputs[0])
			#reroute.Output -> vector_math_001_1.Vector
			dihedral_angle.links.new(reroute.outputs[0], vector_math_001_1.inputs[1])
			#mn_utils_vector_angle_002.Angle -> math_1.Value
			dihedral_angle.links.new(mn_utils_vector_angle_002.outputs[0], math_1.inputs[0])
			#reroute_001.Output -> vector_math_1.Vector
			dihedral_angle.links.new(reroute_001.outputs[0], vector_math_1.inputs[1])
			#group_input_002.C -> vector_math_003.Vector
			dihedral_angle.links.new(group_input_002.outputs[2], vector_math_003.inputs[1])
			#group_input_1.B -> vector_math_004.Vector
			dihedral_angle.links.new(group_input_1.outputs[1], vector_math_004.inputs[1])
			#group_input_1.B -> vector_math_006.Vector
			dihedral_angle.links.new(group_input_1.outputs[1], vector_math_006.inputs[1])
			#group_input_002.C -> vector_math_006.Vector
			dihedral_angle.links.new(group_input_002.outputs[2], vector_math_006.inputs[0])
			#math_1.Value -> group_output_1.Angle
			dihedral_angle.links.new(math_1.outputs[0], group_output_1.inputs[0])
			#reroute_002.Output -> group_output_1.BA⟂(BC)
			dihedral_angle.links.new(reroute_002.outputs[0], group_output_1.inputs[1])
			#reroute.Output -> group_output_1.BC
			dihedral_angle.links.new(reroute.outputs[0], group_output_1.inputs[3])
			#reroute_001.Output -> group_output_1.CD⟂(BC)
			dihedral_angle.links.new(reroute_001.outputs[0], group_output_1.inputs[2])
			#reroute_002.Output -> vector_math_1.Vector
			dihedral_angle.links.new(reroute_002.outputs[0], vector_math_1.inputs[0])
			#vector_math_001_1.Value -> math_001.Value
			dihedral_angle.links.new(vector_math_001_1.outputs[1], math_001.inputs[0])
			#math_001.Value -> math_1.Value
			dihedral_angle.links.new(math_001.outputs[0], math_1.inputs[1])
			#vector_math_010.Vector -> reroute_001.Input
			dihedral_angle.links.new(vector_math_010.outputs[0], reroute_001.inputs[0])
			#vector_math_008.Vector -> reroute_002.Input
			dihedral_angle.links.new(vector_math_008.outputs[0], reroute_002.inputs[0])
			#group_input_001.A -> vector_math_004.Vector
			dihedral_angle.links.new(group_input_001.outputs[0], vector_math_004.inputs[0])
			#group_input_003.D -> vector_math_003.Vector
			dihedral_angle.links.new(group_input_003.outputs[3], vector_math_003.inputs[0])
			return dihedral_angle

		dihedral_angle = dihedral_angle_node_group()

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
			group_output_2 = group_pick.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Group Input
			group_input_2 = group_pick.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
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
			reroute_001_1 = group_pick.nodes.new("NodeReroute")
			reroute_001_1.name = "Reroute.001"
			#node Reroute.002
			reroute_002_1 = group_pick.nodes.new("NodeReroute")
			reroute_002_1.name = "Reroute.002"
			
			
			
			#Set locations
			group_output_2.location = (462.9173889160156, 0.0)
			group_input_2.location = (-472.9173889160156, 0.0)
			switch.location = (-120.0, -20.0)
			index.location = (-480.0, -120.0)
			accumulate_field.location = (60.0, -20.0)
			accumulate_field_002.location = (-120.0, 180.0)
			switch_001.location = (240.0, -20.0)
			compare_003.location = (60.0, 180.0)
			reroute_001_1.location = (-260.0, -100.0)
			reroute_002_1.location = (-260.0, -60.0)
			
			#Set dimensions
			group_output_2.width, group_output_2.height = 140.0, 100.0
			group_input_2.width, group_input_2.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			index.width, index.height = 140.0, 100.0
			accumulate_field.width, accumulate_field.height = 140.0, 100.0
			accumulate_field_002.width, accumulate_field_002.height = 140.0, 100.0
			switch_001.width, switch_001.height = 140.0, 100.0
			compare_003.width, compare_003.height = 138.9921875, 100.0
			reroute_001_1.width, reroute_001_1.height = 16.0, 100.0
			reroute_002_1.width, reroute_002_1.height = 16.0, 100.0
			
			#initialize group_pick links
			#switch.Output -> accumulate_field.Value
			group_pick.links.new(switch.outputs[0], accumulate_field.inputs[0])
			#compare_003.Result -> switch_001.Switch
			group_pick.links.new(compare_003.outputs[0], switch_001.inputs[0])
			#accumulate_field.Total -> switch_001.True
			group_pick.links.new(accumulate_field.outputs[2], switch_001.inputs[2])
			#reroute_001_1.Output -> accumulate_field.Group ID
			group_pick.links.new(reroute_001_1.outputs[0], accumulate_field.inputs[1])
			#reroute_001_1.Output -> accumulate_field_002.Group ID
			group_pick.links.new(reroute_001_1.outputs[0], accumulate_field_002.inputs[1])
			#reroute_002_1.Output -> switch.Switch
			group_pick.links.new(reroute_002_1.outputs[0], switch.inputs[0])
			#reroute_002_1.Output -> accumulate_field_002.Value
			group_pick.links.new(reroute_002_1.outputs[0], accumulate_field_002.inputs[0])
			#index.Index -> switch.True
			group_pick.links.new(index.outputs[0], switch.inputs[2])
			#accumulate_field_002.Total -> compare_003.A
			group_pick.links.new(accumulate_field_002.outputs[2], compare_003.inputs[2])
			#group_input_2.Group ID -> reroute_001_1.Input
			group_pick.links.new(group_input_2.outputs[1], reroute_001_1.inputs[0])
			#group_input_2.Pick -> reroute_002_1.Input
			group_pick.links.new(group_input_2.outputs[0], reroute_002_1.inputs[0])
			#switch_001.Output -> group_output_2.Index
			group_pick.links.new(switch_001.outputs[0], group_output_2.inputs[1])
			#compare_003.Result -> group_output_2.Is Valid
			group_pick.links.new(compare_003.outputs[0], group_output_2.inputs[0])
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
			group_output_3 = group_pick_vector.nodes.new("NodeGroupOutput")
			group_output_3.name = "Group Output"
			group_output_3.is_active_output = True
			
			#node Group Input
			group_input_3 = group_pick_vector.nodes.new("NodeGroupInput")
			group_input_3.name = "Group Input"
			
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
			group_output_3.location = (-40.0, -20.0)
			group_input_3.location = (-740.0, -80.0)
			evaluate_at_index_001.location = (-380.0, -180.0)
			switch_002.location = (-220.0, -60.0)
			group.location = (-560.0, -20.0)
			
			#Set dimensions
			group_output_3.width, group_output_3.height = 140.0, 100.0
			group_input_3.width, group_input_3.height = 140.0, 100.0
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
			#group.Index -> group_output_3.Index
			group_pick_vector.links.new(group.outputs[1], group_output_3.inputs[1])
			#group.Is Valid -> group_output_3.Is Valid
			group_pick_vector.links.new(group.outputs[0], group_output_3.inputs[0])
			#switch_002.Output -> group_output_3.Vector
			group_pick_vector.links.new(switch_002.outputs[0], group_output_3.inputs[2])
			#group_input_3.Group ID -> group.Group ID
			group_pick_vector.links.new(group_input_3.outputs[1], group.inputs[1])
			#group_input_3.Pick -> group.Pick
			group_pick_vector.links.new(group_input_3.outputs[0], group.inputs[0])
			#group_input_3.Position -> evaluate_at_index_001.Value
			group_pick_vector.links.new(group_input_3.outputs[2], evaluate_at_index_001.inputs[1])
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
			group_output_4 = offset_integer.nodes.new("NodeGroupOutput")
			group_output_4.name = "Group Output"
			group_output_4.is_active_output = True
			
			#node Group Input
			group_input_4 = offset_integer.nodes.new("NodeGroupInput")
			group_input_4.name = "Group Input"
			
			#node Evaluate at Index
			evaluate_at_index = offset_integer.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index.name = "Evaluate at Index"
			evaluate_at_index.data_type = 'INT'
			evaluate_at_index.domain = 'POINT'
			
			#node Math
			math_2 = offset_integer.nodes.new("ShaderNodeMath")
			math_2.name = "Math"
			math_2.operation = 'ADD'
			math_2.use_clamp = False
			
			
			
			
			#Set locations
			group_output_4.location = (190.0, 0.0)
			group_input_4.location = (-412.72760009765625, 0.2001800537109375)
			evaluate_at_index.location = (0.0, 0.0)
			math_2.location = (-217.90158081054688, 69.93922424316406)
			
			#Set dimensions
			group_output_4.width, group_output_4.height = 140.0, 100.0
			group_input_4.width, group_input_4.height = 140.0, 100.0
			evaluate_at_index.width, evaluate_at_index.height = 140.0, 100.0
			math_2.width, math_2.height = 140.0, 100.0
			
			#initialize offset_integer links
			#evaluate_at_index.Value -> group_output_4.Value
			offset_integer.links.new(evaluate_at_index.outputs[0], group_output_4.inputs[0])
			#group_input_4.Index -> math_2.Value
			offset_integer.links.new(group_input_4.outputs[0], math_2.inputs[0])
			#group_input_4.Offset -> math_2.Value
			offset_integer.links.new(group_input_4.outputs[2], math_2.inputs[1])
			#math_2.Value -> evaluate_at_index.Index
			offset_integer.links.new(math_2.outputs[0], evaluate_at_index.inputs[0])
			#group_input_4.Value -> evaluate_at_index.Value
			offset_integer.links.new(group_input_4.outputs[1], evaluate_at_index.inputs[1])
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
			group_output_5 = res_group_id.nodes.new("NodeGroupOutput")
			group_output_5.name = "Group Output"
			group_output_5.is_active_output = True
			
			#node Group Input
			group_input_5 = res_group_id.nodes.new("NodeGroupInput")
			group_input_5.name = "Group Input"
			
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
			math_3 = res_group_id.nodes.new("ShaderNodeMath")
			math_3.name = "Math"
			math_3.operation = 'SUBTRACT'
			math_3.use_clamp = False
			#Value_001
			math_3.inputs[1].default_value = 1.0
			
			#node Frame
			frame = res_group_id.nodes.new("NodeFrame")
			frame.name = "Frame"
			frame.label_size = 20
			frame.shrink = True
			
			#node Reroute
			reroute_1 = res_group_id.nodes.new("NodeReroute")
			reroute_1.label = "subtracting 1 from the leading, but things don't work right"
			reroute_1.name = "Reroute"
			#node Reroute.001
			reroute_001_2 = res_group_id.nodes.new("NodeReroute")
			reroute_001_2.name = "Reroute.001"
			#node Reroute.002
			reroute_002_2 = res_group_id.nodes.new("NodeReroute")
			reroute_002_2.label = "In theory we can just use the trailing value instead of"
			reroute_002_2.name = "Reroute.002"
			#node Reroute.003
			reroute_003 = res_group_id.nodes.new("NodeReroute")
			reroute_003.name = "Reroute.003"
			
			
			#Set parents
			math_3.parent = frame
			reroute_1.parent = frame
			reroute_001_2.parent = frame
			reroute_002_2.parent = frame
			reroute_003.parent = frame
			
			#Set locations
			group_output_5.location = (900.0, 160.0)
			group_input_5.location = (-420.0, 160.0)
			named_attribute_001.location = (-240.0, 0.0)
			named_attribute_002.location = (-250.0, 160.0)
			compare_002.location = (-70.0, 160.0)
			compare_001.location = (-70.0, 0.0)
			boolean_math.location = (90.0, 160.0)
			accumulate_field_001.location = (250.0, 160.0)
			group_001.location = (-70.0, -160.0)
			math_3.location = (519.2361450195312, 166.28671264648438)
			frame.location = (95.0, -20.0)
			reroute_1.location = (554.4125366210938, 257.9646911621094)
			reroute_001_2.location = (739.2361450195312, 306.2867126464844)
			reroute_002_2.location = (551.13134765625, 297.3444519042969)
			reroute_003.location = (379.23614501953125, 306.2867126464844)
			
			#Set dimensions
			group_output_5.width, group_output_5.height = 140.0, 100.0
			group_input_5.width, group_input_5.height = 140.0, 100.0
			named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
			named_attribute_002.width, named_attribute_002.height = 140.0, 100.0
			compare_002.width, compare_002.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			accumulate_field_001.width, accumulate_field_001.height = 140.0, 100.0
			group_001.width, group_001.height = 140.0, 100.0
			math_3.width, math_3.height = 140.0, 100.0
			frame.width, frame.height = 436.0, 356.2867126464844
			reroute_1.width, reroute_1.height = 16.0, 100.0
			reroute_001_2.width, reroute_001_2.height = 16.0, 100.0
			reroute_002_2.width, reroute_002_2.height = 16.0, 100.0
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
			#accumulate_field_001.Leading -> math_3.Value
			res_group_id.links.new(accumulate_field_001.outputs[0], math_3.inputs[0])
			#math_3.Value -> group_output_5.Unique Group ID
			res_group_id.links.new(math_3.outputs[0], group_output_5.inputs[0])
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
			group_input_6 = residue_mask.nodes.new("NodeGroupInput")
			group_input_6.name = "Group Input"
			
			#node Named Attribute
			named_attribute = residue_mask.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'INT'
			#Name
			named_attribute.inputs[0].default_value = "atom_name"
			
			#node Group Output
			group_output_6 = residue_mask.nodes.new("NodeGroupOutput")
			group_output_6.name = "Group Output"
			group_output_6.is_active_output = True
			
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
			group_input_6.location = (-140.0, 200.0)
			named_attribute.location = (-140.0, 340.0)
			group_output_6.location = (420.0, 340.0)
			group_1.location = (220.0, 340.0)
			group_002.location = (-140.0, 60.0)
			switch_1.location = (40.0, 180.0)
			
			#Set dimensions
			compare.width, compare.height = 140.0, 100.0
			group_input_6.width, group_input_6.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			group_output_6.width, group_output_6.height = 140.0, 100.0
			group_1.width, group_1.height = 164.60528564453125, 100.0
			group_002.width, group_002.height = 140.0, 100.0
			switch_1.width, switch_1.height = 140.0, 100.0
			
			#initialize residue_mask links
			#named_attribute.Attribute -> compare.A
			residue_mask.links.new(named_attribute.outputs[0], compare.inputs[2])
			#group_input_6.atom_name -> compare.B
			residue_mask.links.new(group_input_6.outputs[0], compare.inputs[3])
			#group_1.Index -> group_output_6.Index
			residue_mask.links.new(group_1.outputs[1], group_output_6.inputs[1])
			#group_1.Vector -> group_output_6.Position
			residue_mask.links.new(group_1.outputs[2], group_output_6.inputs[2])
			#group_1.Is Valid -> group_output_6.Is Valid
			residue_mask.links.new(group_1.outputs[0], group_output_6.inputs[0])
			#compare.Result -> group_1.Pick
			residue_mask.links.new(compare.outputs[0], group_1.inputs[0])
			#group_input_6.Use Fallback -> switch_1.Switch
			residue_mask.links.new(group_input_6.outputs[1], switch_1.inputs[0])
			#group_input_6.Group ID -> switch_1.False
			residue_mask.links.new(group_input_6.outputs[2], switch_1.inputs[1])
			#switch_1.Output -> group_1.Group ID
			residue_mask.links.new(switch_1.outputs[0], group_1.inputs[1])
			#group_002.Unique Group ID -> switch_1.True
			residue_mask.links.new(group_002.outputs[0], switch_1.inputs[2])
			#switch_1.Output -> group_output_6.Group ID
			residue_mask.links.new(switch_1.outputs[0], group_output_6.inputs[3])
			return residue_mask

		residue_mask = residue_mask_node_group()

		#initialize fallback_vector node group
		def fallback_vector_node_group():
			fallback_vector = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Fallback Vector")

			fallback_vector.color_tag = 'INPUT'
			fallback_vector.description = ""

			
			#fallback_vector interface
			#Socket Output
			output_socket = fallback_vector.interface.new_socket(name = "Output", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			output_socket.default_value = (0.0, 0.0, 0.0)
			output_socket.min_value = -3.4028234663852886e+38
			output_socket.max_value = 3.4028234663852886e+38
			output_socket.subtype = 'NONE'
			output_socket.attribute_domain = 'POINT'
			
			#Socket Name
			name_socket = fallback_vector.interface.new_socket(name = "Name", in_out='INPUT', socket_type = 'NodeSocketString')
			name_socket.default_value = ""
			name_socket.attribute_domain = 'POINT'
			
			#Socket Fallback
			fallback_socket = fallback_vector.interface.new_socket(name = "Fallback", in_out='INPUT', socket_type = 'NodeSocketVector')
			fallback_socket.default_value = (0.0, 0.0, 0.0)
			fallback_socket.min_value = -3.4028234663852886e+38
			fallback_socket.max_value = 3.4028234663852886e+38
			fallback_socket.subtype = 'NONE'
			fallback_socket.attribute_domain = 'POINT'
			
			
			#initialize fallback_vector nodes
			#node Group Output
			group_output_7 = fallback_vector.nodes.new("NodeGroupOutput")
			group_output_7.name = "Group Output"
			group_output_7.is_active_output = True
			
			#node Group Input
			group_input_7 = fallback_vector.nodes.new("NodeGroupInput")
			group_input_7.name = "Group Input"
			
			#node Named Attribute.001
			named_attribute_001_1 = fallback_vector.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001_1.name = "Named Attribute.001"
			named_attribute_001_1.data_type = 'FLOAT_VECTOR'
			
			#node Switch
			switch_2 = fallback_vector.nodes.new("GeometryNodeSwitch")
			switch_2.name = "Switch"
			switch_2.input_type = 'VECTOR'
			
			
			
			
			#Set locations
			group_output_7.location = (260.0, 140.0)
			group_input_7.location = (-320.0, 80.0)
			named_attribute_001_1.location = (-134.38072204589844, 30.303295135498047)
			switch_2.location = (100.0, 140.0)
			
			#Set dimensions
			group_output_7.width, group_output_7.height = 140.0, 100.0
			group_input_7.width, group_input_7.height = 140.0, 100.0
			named_attribute_001_1.width, named_attribute_001_1.height = 147.09487915039062, 100.0
			switch_2.width, switch_2.height = 140.0, 100.0
			
			#initialize fallback_vector links
			#named_attribute_001_1.Attribute -> switch_2.True
			fallback_vector.links.new(named_attribute_001_1.outputs[0], switch_2.inputs[2])
			#named_attribute_001_1.Exists -> switch_2.Switch
			fallback_vector.links.new(named_attribute_001_1.outputs[1], switch_2.inputs[0])
			#group_input_7.Fallback -> switch_2.False
			fallback_vector.links.new(group_input_7.outputs[1], switch_2.inputs[1])
			#switch_2.Output -> group_output_7.Output
			fallback_vector.links.new(switch_2.outputs[0], group_output_7.inputs[0])
			#group_input_7.Name -> named_attribute_001_1.Name
			fallback_vector.links.new(group_input_7.outputs[0], named_attribute_001_1.inputs[0])
			return fallback_vector

		fallback_vector = fallback_vector_node_group()

		#initialize offset_vector node group
		def offset_vector_node_group():
			offset_vector = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Offset Vector")

			offset_vector.color_tag = 'CONVERTER'
			offset_vector.description = ""

			
			#offset_vector interface
			#Socket Value
			value_socket_2 = offset_vector.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			value_socket_2.default_value = (0.0, 0.0, 0.0)
			value_socket_2.min_value = -3.4028234663852886e+38
			value_socket_2.max_value = 3.4028234663852886e+38
			value_socket_2.subtype = 'NONE'
			value_socket_2.attribute_domain = 'POINT'
			
			#Socket Index
			index_socket_4 = offset_vector.interface.new_socket(name = "Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			index_socket_4.default_value = 0
			index_socket_4.min_value = 0
			index_socket_4.max_value = 2147483647
			index_socket_4.subtype = 'NONE'
			index_socket_4.attribute_domain = 'POINT'
			
			#Socket Position
			position_socket_2 = offset_vector.interface.new_socket(name = "Position", in_out='INPUT', socket_type = 'NodeSocketVector')
			position_socket_2.default_value = (0.0, 0.0, 0.0)
			position_socket_2.min_value = -3.4028234663852886e+38
			position_socket_2.max_value = 3.4028234663852886e+38
			position_socket_2.subtype = 'NONE'
			position_socket_2.attribute_domain = 'POINT'
			position_socket_2.hide_value = True
			
			#Socket Offset
			offset_socket_1 = offset_vector.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket_1.default_value = 0
			offset_socket_1.min_value = -2147483647
			offset_socket_1.max_value = 2147483647
			offset_socket_1.subtype = 'NONE'
			offset_socket_1.attribute_domain = 'POINT'
			
			
			#initialize offset_vector nodes
			#node Group Output
			group_output_8 = offset_vector.nodes.new("NodeGroupOutput")
			group_output_8.name = "Group Output"
			group_output_8.is_active_output = True
			
			#node Group Input
			group_input_8 = offset_vector.nodes.new("NodeGroupInput")
			group_input_8.name = "Group Input"
			
			#node Evaluate at Index
			evaluate_at_index_1 = offset_vector.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_1.name = "Evaluate at Index"
			evaluate_at_index_1.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_1.domain = 'POINT'
			
			#node Math
			math_4 = offset_vector.nodes.new("ShaderNodeMath")
			math_4.name = "Math"
			math_4.operation = 'ADD'
			math_4.use_clamp = False
			
			
			
			
			#Set locations
			group_output_8.location = (300.0, 20.0)
			group_input_8.location = (-273.81378173828125, 0.0)
			evaluate_at_index_1.location = (120.0, 20.0)
			math_4.location = (-60.0, 20.0)
			
			#Set dimensions
			group_output_8.width, group_output_8.height = 140.0, 100.0
			group_input_8.width, group_input_8.height = 140.0, 100.0
			evaluate_at_index_1.width, evaluate_at_index_1.height = 140.0, 100.0
			math_4.width, math_4.height = 140.0, 100.0
			
			#initialize offset_vector links
			#group_input_8.Position -> evaluate_at_index_1.Value
			offset_vector.links.new(group_input_8.outputs[1], evaluate_at_index_1.inputs[1])
			#evaluate_at_index_1.Value -> group_output_8.Value
			offset_vector.links.new(evaluate_at_index_1.outputs[0], group_output_8.inputs[0])
			#group_input_8.Index -> math_4.Value
			offset_vector.links.new(group_input_8.outputs[0], math_4.inputs[0])
			#group_input_8.Offset -> math_4.Value
			offset_vector.links.new(group_input_8.outputs[2], math_4.inputs[1])
			#math_4.Value -> evaluate_at_index_1.Index
			offset_vector.links.new(math_4.outputs[0], evaluate_at_index_1.inputs[0])
			return offset_vector

		offset_vector = offset_vector_node_group()

		#initialize group_info node group
		def group_info_node_group():
			group_info = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Group Info")

			group_info.color_tag = 'CONVERTER'
			group_info.description = ""

			
			#group_info interface
			#Socket First Index
			first_index_socket = group_info.interface.new_socket(name = "First Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			first_index_socket.default_value = 0
			first_index_socket.min_value = -2147483648
			first_index_socket.max_value = 2147483647
			first_index_socket.subtype = 'NONE'
			first_index_socket.attribute_domain = 'POINT'
			first_index_socket.description = "Index of the first point in the group"
			
			#Socket Last Index
			last_index_socket = group_info.interface.new_socket(name = "Last Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			last_index_socket.default_value = 0
			last_index_socket.min_value = -2147483648
			last_index_socket.max_value = 2147483647
			last_index_socket.subtype = 'NONE'
			last_index_socket.attribute_domain = 'POINT'
			last_index_socket.description = "Index of the last point in the group"
			
			#Socket Index in Group
			index_in_group_socket = group_info.interface.new_socket(name = "Index in Group", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			index_in_group_socket.default_value = 0
			index_in_group_socket.min_value = -2147483648
			index_in_group_socket.max_value = 2147483647
			index_in_group_socket.subtype = 'NONE'
			index_in_group_socket.attribute_domain = 'POINT'
			
			#Socket Size
			size_socket = group_info.interface.new_socket(name = "Size", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			size_socket.default_value = 0
			size_socket.min_value = -2147483648
			size_socket.max_value = 2147483647
			size_socket.subtype = 'NONE'
			size_socket.attribute_domain = 'POINT'
			size_socket.description = "Number of points in the group"
			
			#Socket Group ID
			group_id_socket_4 = group_info.interface.new_socket(name = "Group ID", in_out='INPUT', socket_type = 'NodeSocketInt')
			group_id_socket_4.default_value = 0
			group_id_socket_4.min_value = -2147483648
			group_id_socket_4.max_value = 2147483647
			group_id_socket_4.subtype = 'NONE'
			group_id_socket_4.attribute_domain = 'POINT'
			
			
			#initialize group_info nodes
			#node Group Output
			group_output_9 = group_info.nodes.new("NodeGroupOutput")
			group_output_9.name = "Group Output"
			group_output_9.is_active_output = True
			
			#node Group Input
			group_input_9 = group_info.nodes.new("NodeGroupInput")
			group_input_9.name = "Group Input"
			
			#node Accumulate Field.001
			accumulate_field_001_1 = group_info.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_001_1.name = "Accumulate Field.001"
			accumulate_field_001_1.data_type = 'INT'
			accumulate_field_001_1.domain = 'POINT'
			accumulate_field_001_1.outputs[0].hide = True
			accumulate_field_001_1.outputs[1].hide = True
			
			#node Index
			index_1 = group_info.nodes.new("GeometryNodeInputIndex")
			index_1.name = "Index"
			
			#node Compare
			compare_1 = group_info.nodes.new("FunctionNodeCompare")
			compare_1.name = "Compare"
			compare_1.data_type = 'INT'
			compare_1.mode = 'ELEMENT'
			compare_1.operation = 'EQUAL'
			#B_INT
			compare_1.inputs[3].default_value = 0
			
			#node Switch.001
			switch_001_1 = group_info.nodes.new("GeometryNodeSwitch")
			switch_001_1.name = "Switch.001"
			switch_001_1.input_type = 'INT'
			#False
			switch_001_1.inputs[1].default_value = 0
			
			#node Compare.002
			compare_002_1 = group_info.nodes.new("FunctionNodeCompare")
			compare_002_1.name = "Compare.002"
			compare_002_1.data_type = 'INT'
			compare_002_1.mode = 'ELEMENT'
			compare_002_1.operation = 'EQUAL'
			
			#node Switch.002
			switch_002_1 = group_info.nodes.new("GeometryNodeSwitch")
			switch_002_1.name = "Switch.002"
			switch_002_1.input_type = 'INT'
			#False
			switch_002_1.inputs[1].default_value = 0
			
			#node Accumulate Field.002
			accumulate_field_002_1 = group_info.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_002_1.name = "Accumulate Field.002"
			accumulate_field_002_1.data_type = 'INT'
			accumulate_field_002_1.domain = 'POINT'
			accumulate_field_002_1.outputs[0].hide = True
			accumulate_field_002_1.outputs[1].hide = True
			
			#node Reroute
			reroute_2 = group_info.nodes.new("NodeReroute")
			reroute_2.name = "Reroute"
			#node Accumulate Field.003
			accumulate_field_003 = group_info.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_003.name = "Accumulate Field.003"
			accumulate_field_003.data_type = 'INT'
			accumulate_field_003.domain = 'POINT'
			#Value
			accumulate_field_003.inputs[0].default_value = 1
			
			#node Reroute.001
			reroute_001_3 = group_info.nodes.new("NodeReroute")
			reroute_001_3.name = "Reroute.001"
			
			
			
			#Set locations
			group_output_9.location = (580.0, 100.0)
			group_input_9.location = (-540.0, 0.0)
			accumulate_field_001_1.location = (340.0, 140.0)
			index_1.location = (-40.0, -20.0)
			compare_1.location = (-40.0, 140.0)
			switch_001_1.location = (120.0, 140.0)
			compare_002_1.location = (-40.0, -80.0)
			switch_002_1.location = (120.0, -20.0)
			accumulate_field_002_1.location = (340.0, -78.97427368164062)
			reroute_2.location = (280.0, -300.0)
			accumulate_field_003.location = (-240.0, -80.0)
			reroute_001_3.location = (-320.0, -300.0)
			
			#Set dimensions
			group_output_9.width, group_output_9.height = 140.0, 100.0
			group_input_9.width, group_input_9.height = 140.0, 100.0
			accumulate_field_001_1.width, accumulate_field_001_1.height = 140.0, 100.0
			index_1.width, index_1.height = 140.0, 100.0
			compare_1.width, compare_1.height = 140.0, 100.0
			switch_001_1.width, switch_001_1.height = 140.0, 100.0
			compare_002_1.width, compare_002_1.height = 140.0, 100.0
			switch_002_1.width, switch_002_1.height = 140.0, 100.0
			accumulate_field_002_1.width, accumulate_field_002_1.height = 140.0, 100.0
			reroute_2.width, reroute_2.height = 16.0, 100.0
			accumulate_field_003.width, accumulate_field_003.height = 140.0, 100.0
			reroute_001_3.width, reroute_001_3.height = 16.0, 100.0
			
			#initialize group_info links
			#reroute_2.Output -> accumulate_field_002_1.Group ID
			group_info.links.new(reroute_2.outputs[0], accumulate_field_002_1.inputs[1])
			#reroute_001_3.Output -> reroute_2.Input
			group_info.links.new(reroute_001_3.outputs[0], reroute_2.inputs[0])
			#index_1.Index -> switch_002_1.True
			group_info.links.new(index_1.outputs[0], switch_002_1.inputs[2])
			#accumulate_field_003.Trailing -> compare_1.A
			group_info.links.new(accumulate_field_003.outputs[1], compare_1.inputs[2])
			#compare_1.Result -> switch_001_1.Switch
			group_info.links.new(compare_1.outputs[0], switch_001_1.inputs[0])
			#accumulate_field_003.Total -> compare_002_1.B
			group_info.links.new(accumulate_field_003.outputs[2], compare_002_1.inputs[3])
			#switch_002_1.Output -> accumulate_field_002_1.Value
			group_info.links.new(switch_002_1.outputs[0], accumulate_field_002_1.inputs[0])
			#reroute_001_3.Output -> accumulate_field_003.Group ID
			group_info.links.new(reroute_001_3.outputs[0], accumulate_field_003.inputs[1])
			#index_1.Index -> switch_001_1.True
			group_info.links.new(index_1.outputs[0], switch_001_1.inputs[2])
			#switch_001_1.Output -> accumulate_field_001_1.Value
			group_info.links.new(switch_001_1.outputs[0], accumulate_field_001_1.inputs[0])
			#compare_002_1.Result -> switch_002_1.Switch
			group_info.links.new(compare_002_1.outputs[0], switch_002_1.inputs[0])
			#reroute_2.Output -> accumulate_field_001_1.Group ID
			group_info.links.new(reroute_2.outputs[0], accumulate_field_001_1.inputs[1])
			#group_input_9.Group ID -> reroute_001_3.Input
			group_info.links.new(group_input_9.outputs[0], reroute_001_3.inputs[0])
			#accumulate_field_001_1.Total -> group_output_9.First Index
			group_info.links.new(accumulate_field_001_1.outputs[2], group_output_9.inputs[0])
			#accumulate_field_002_1.Total -> group_output_9.Last Index
			group_info.links.new(accumulate_field_002_1.outputs[2], group_output_9.inputs[1])
			#accumulate_field_003.Total -> group_output_9.Size
			group_info.links.new(accumulate_field_003.outputs[2], group_output_9.inputs[3])
			#accumulate_field_003.Leading -> compare_002_1.A
			group_info.links.new(accumulate_field_003.outputs[0], compare_002_1.inputs[2])
			#accumulate_field_003.Trailing -> group_output_9.Index in Group
			group_info.links.new(accumulate_field_003.outputs[1], group_output_9.inputs[2])
			return group_info

		group_info = group_info_node_group()

		#initialize backbone_position node group
		def backbone_position_node_group():
			backbone_position = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Backbone Position")

			backbone_position.color_tag = 'INPUT'
			backbone_position.description = ""

			
			#backbone_position interface
			#Socket Position
			position_socket_3 = backbone_position.interface.new_socket(name = "Position", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			position_socket_3.default_value = (0.0, 0.0, 0.0)
			position_socket_3.min_value = -3.4028234663852886e+38
			position_socket_3.max_value = 3.4028234663852886e+38
			position_socket_3.subtype = 'NONE'
			position_socket_3.attribute_domain = 'POINT'
			
			#Socket Index
			index_socket_5 = backbone_position.interface.new_socket(name = "Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			index_socket_5.default_value = 0
			index_socket_5.min_value = 0
			index_socket_5.max_value = 2147483647
			index_socket_5.subtype = 'NONE'
			index_socket_5.attribute_domain = 'POINT'
			index_socket_5.hide_value = True
			
			#Socket Menu
			menu_socket = backbone_position.interface.new_socket(name = "Menu", in_out='INPUT', socket_type = 'NodeSocketMenu')
			menu_socket.default_value = "backbone_N"
			menu_socket.attribute_domain = 'POINT'
			
			#Socket Offset
			offset_socket_2 = backbone_position.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket_2.default_value = 0
			offset_socket_2.min_value = -1
			offset_socket_2.max_value = 1
			offset_socket_2.subtype = 'NONE'
			offset_socket_2.attribute_domain = 'POINT'
			
			
			#initialize backbone_position nodes
			#node Group Output
			group_output_10 = backbone_position.nodes.new("NodeGroupOutput")
			group_output_10.name = "Group Output"
			group_output_10.is_active_output = True
			
			#node Group Input
			group_input_10 = backbone_position.nodes.new("NodeGroupInput")
			group_input_10.name = "Group Input"
			group_input_10.outputs[0].hide = True
			group_input_10.outputs[2].hide = True
			group_input_10.outputs[3].hide = True
			
			#node Group
			group_2 = backbone_position.nodes.new("GeometryNodeGroup")
			group_2.name = "Group"
			group_2.node_tree = residue_mask
			#Socket_5
			group_2.inputs[1].default_value = True
			#Socket_4
			group_2.inputs[2].default_value = 0
			
			#node Group.001
			group_001_1 = backbone_position.nodes.new("GeometryNodeGroup")
			group_001_1.name = "Group.001"
			group_001_1.node_tree = fallback_vector
			
			#node Index Switch
			index_switch = backbone_position.nodes.new("GeometryNodeIndexSwitch")
			index_switch.name = "Index Switch"
			index_switch.data_type = 'STRING'
			index_switch.index_switch_items.clear()
			index_switch.index_switch_items.new()
			index_switch.index_switch_items.new()
			index_switch.index_switch_items.new()
			index_switch.index_switch_items.new()
			index_switch.index_switch_items.new()
			#Item_0
			index_switch.inputs[1].default_value = ""
			#Item_1
			index_switch.inputs[2].default_value = "backbone_N"
			#Item_2
			index_switch.inputs[3].default_value = "backbone_CA"
			#Item_3
			index_switch.inputs[4].default_value = "backbone_C"
			#Item_4
			index_switch.inputs[5].default_value = "backbone_O"
			
			#node Menu Switch
			menu_switch = backbone_position.nodes.new("GeometryNodeMenuSwitch")
			menu_switch.name = "Menu Switch"
			menu_switch.active_index = 3
			menu_switch.data_type = 'INT'
			menu_switch.enum_items.clear()
			menu_switch.enum_items.new("backbone_N")
			menu_switch.enum_items[0].description = ""
			menu_switch.enum_items.new("backbone_CA")
			menu_switch.enum_items[1].description = ""
			menu_switch.enum_items.new("backbone_C")
			menu_switch.enum_items[2].description = ""
			menu_switch.enum_items.new("backbone_O")
			menu_switch.enum_items[3].description = ""
			#Item_0
			menu_switch.inputs[1].default_value = 1
			#Item_1
			menu_switch.inputs[2].default_value = 2
			#Item_2
			menu_switch.inputs[3].default_value = 3
			#Item_3
			menu_switch.inputs[4].default_value = 4
			
			#node Group.002
			group_002_1 = backbone_position.nodes.new("GeometryNodeGroup")
			group_002_1.name = "Group.002"
			group_002_1.node_tree = offset_vector
			
			#node Group Input.001
			group_input_001_1 = backbone_position.nodes.new("NodeGroupInput")
			group_input_001_1.name = "Group Input.001"
			group_input_001_1.outputs[1].hide = True
			group_input_001_1.outputs[3].hide = True
			
			#node Group.003
			group_003 = backbone_position.nodes.new("GeometryNodeGroup")
			group_003.name = "Group.003"
			group_003.node_tree = group_info
			
			#node Math
			math_5 = backbone_position.nodes.new("ShaderNodeMath")
			math_5.name = "Math"
			math_5.operation = 'MULTIPLY'
			math_5.use_clamp = False
			
			
			
			
			#Set locations
			group_output_10.location = (640.0, 100.0)
			group_input_10.location = (-560.0, 100.0)
			group_2.location = (-194.45651245117188, 100.0)
			group_001_1.location = (60.0, 120.0)
			index_switch.location = (-200.0, -140.0)
			menu_switch.location = (-380.0, 100.0)
			group_002_1.location = (460.0, 100.0)
			group_input_001_1.location = (60.0, 0.0)
			group_003.location = (60.0, -100.0)
			math_5.location = (260.0, -100.0)
			
			#Set dimensions
			group_output_10.width, group_output_10.height = 140.0, 100.0
			group_input_10.width, group_input_10.height = 140.0, 100.0
			group_2.width, group_2.height = 174.45651245117188, 100.0
			group_001_1.width, group_001_1.height = 141.8542938232422, 100.0
			index_switch.width, index_switch.height = 184.38287353515625, 100.0
			menu_switch.width, menu_switch.height = 140.0, 100.0
			group_002_1.width, group_002_1.height = 140.0, 100.0
			group_input_001_1.width, group_input_001_1.height = 140.0, 100.0
			group_003.width, group_003.height = 140.0, 100.0
			math_5.width, math_5.height = 140.0, 100.0
			
			#initialize backbone_position links
			#index_switch.Output -> group_001_1.Name
			backbone_position.links.new(index_switch.outputs[0], group_001_1.inputs[0])
			#menu_switch.Output -> index_switch.Index
			backbone_position.links.new(menu_switch.outputs[0], index_switch.inputs[0])
			#group_input_10.Menu -> menu_switch.Menu
			backbone_position.links.new(group_input_10.outputs[1], menu_switch.inputs[0])
			#group_input_001_1.Index -> group_002_1.Index
			backbone_position.links.new(group_input_001_1.outputs[0], group_002_1.inputs[0])
			#menu_switch.Output -> group_2.atom_name
			backbone_position.links.new(menu_switch.outputs[0], group_2.inputs[0])
			#group_002_1.Value -> group_output_10.Position
			backbone_position.links.new(group_002_1.outputs[0], group_output_10.inputs[0])
			#group_001_1.Output -> group_002_1.Position
			backbone_position.links.new(group_001_1.outputs[0], group_002_1.inputs[1])
			#group_2.Position -> group_001_1.Fallback
			backbone_position.links.new(group_2.outputs[2], group_001_1.inputs[1])
			#group_2.Group ID -> group_003.Group ID
			backbone_position.links.new(group_2.outputs[3], group_003.inputs[0])
			#group_input_001_1.Offset -> math_5.Value
			backbone_position.links.new(group_input_001_1.outputs[2], math_5.inputs[0])
			#group_003.Size -> math_5.Value
			backbone_position.links.new(group_003.outputs[3], math_5.inputs[1])
			#math_5.Value -> group_002_1.Offset
			backbone_position.links.new(math_5.outputs[0], group_002_1.inputs[2])
			return backbone_position

		backbone_position = backbone_position_node_group()

		#initialize fallback_float node group
		def fallback_float_node_group():
			fallback_float = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Fallback Float")

			fallback_float.color_tag = 'INPUT'
			fallback_float.description = ""

			
			#fallback_float interface
			#Socket Value
			value_socket_3 = fallback_float.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			value_socket_3.default_value = 0.0
			value_socket_3.min_value = -3.4028234663852886e+38
			value_socket_3.max_value = 3.4028234663852886e+38
			value_socket_3.subtype = 'NONE'
			value_socket_3.attribute_domain = 'POINT'
			
			#Socket Name
			name_socket_1 = fallback_float.interface.new_socket(name = "Name", in_out='INPUT', socket_type = 'NodeSocketString')
			name_socket_1.default_value = ""
			name_socket_1.attribute_domain = 'POINT'
			
			#Socket Fallback
			fallback_socket_1 = fallback_float.interface.new_socket(name = "Fallback", in_out='INPUT', socket_type = 'NodeSocketFloat')
			fallback_socket_1.default_value = 0.0
			fallback_socket_1.min_value = -3.4028234663852886e+38
			fallback_socket_1.max_value = 3.4028234663852886e+38
			fallback_socket_1.subtype = 'NONE'
			fallback_socket_1.attribute_domain = 'POINT'
			
			
			#initialize fallback_float nodes
			#node Group Output
			group_output_11 = fallback_float.nodes.new("NodeGroupOutput")
			group_output_11.name = "Group Output"
			group_output_11.is_active_output = True
			
			#node Group Input
			group_input_11 = fallback_float.nodes.new("NodeGroupInput")
			group_input_11.name = "Group Input"
			
			#node Named Attribute
			named_attribute_1 = fallback_float.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_1.name = "Named Attribute"
			named_attribute_1.data_type = 'FLOAT'
			
			#node Switch
			switch_3 = fallback_float.nodes.new("GeometryNodeSwitch")
			switch_3.name = "Switch"
			switch_3.input_type = 'FLOAT'
			
			
			
			
			#Set locations
			group_output_11.location = (306.3518981933594, 0.0)
			group_input_11.location = (-316.3518981933594, 0.0)
			named_attribute_1.location = (-136.0193634033203, 58.357723236083984)
			switch_3.location = (116.35189819335938, 12.828765869140625)
			
			#Set dimensions
			group_output_11.width, group_output_11.height = 140.0, 100.0
			group_input_11.width, group_input_11.height = 140.0, 100.0
			named_attribute_1.width, named_attribute_1.height = 168.09637451171875, 100.0
			switch_3.width, switch_3.height = 140.0, 100.0
			
			#initialize fallback_float links
			#named_attribute_1.Exists -> switch_3.Switch
			fallback_float.links.new(named_attribute_1.outputs[1], switch_3.inputs[0])
			#named_attribute_1.Attribute -> switch_3.True
			fallback_float.links.new(named_attribute_1.outputs[0], switch_3.inputs[2])
			#group_input_11.Name -> named_attribute_1.Name
			fallback_float.links.new(group_input_11.outputs[0], named_attribute_1.inputs[0])
			#group_input_11.Fallback -> switch_3.False
			fallback_float.links.new(group_input_11.outputs[1], switch_3.inputs[1])
			#switch_3.Output -> group_output_11.Value
			fallback_float.links.new(switch_3.outputs[0], group_output_11.inputs[0])
			return fallback_float

		fallback_float = fallback_float_node_group()

		#initialize dihedral_psi node group
		def dihedral_psi_node_group():
			dihedral_psi = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Dihedral Psi")

			dihedral_psi.color_tag = 'INPUT'
			dihedral_psi.description = ""

			
			#dihedral_psi interface
			#Socket Psi
			psi_socket = dihedral_psi.interface.new_socket(name = "Psi", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			psi_socket.default_value = 0.0
			psi_socket.min_value = -3.4028234663852886e+38
			psi_socket.max_value = 3.4028234663852886e+38
			psi_socket.subtype = 'ANGLE'
			psi_socket.attribute_domain = 'POINT'
			
			#Socket BA⟂(BC)
			ba__bc__socket_1 = dihedral_psi.interface.new_socket(name = "BA⟂(BC)", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			ba__bc__socket_1.default_value = (0.0, 0.0, 0.0)
			ba__bc__socket_1.min_value = -3.4028234663852886e+38
			ba__bc__socket_1.max_value = 3.4028234663852886e+38
			ba__bc__socket_1.subtype = 'NONE'
			ba__bc__socket_1.attribute_domain = 'POINT'
			
			#Socket CD⟂(BC)
			cd__bc__socket_1 = dihedral_psi.interface.new_socket(name = "CD⟂(BC)", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			cd__bc__socket_1.default_value = (0.0, 0.0, 0.0)
			cd__bc__socket_1.min_value = -3.4028234663852886e+38
			cd__bc__socket_1.max_value = 3.4028234663852886e+38
			cd__bc__socket_1.subtype = 'NONE'
			cd__bc__socket_1.attribute_domain = 'POINT'
			
			#Socket BC
			bc_socket_1 = dihedral_psi.interface.new_socket(name = "BC", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			bc_socket_1.default_value = (0.0, 0.0, 0.0)
			bc_socket_1.min_value = -3.4028234663852886e+38
			bc_socket_1.max_value = 3.4028234663852886e+38
			bc_socket_1.subtype = 'NONE'
			bc_socket_1.attribute_domain = 'POINT'
			
			
			#initialize dihedral_psi nodes
			#node Group Output
			group_output_12 = dihedral_psi.nodes.new("NodeGroupOutput")
			group_output_12.name = "Group Output"
			group_output_12.is_active_output = True
			
			#node Group.009
			group_009 = dihedral_psi.nodes.new("GeometryNodeGroup")
			group_009.name = "Group.009"
			group_009.node_tree = dihedral_angle
			
			#node Group
			group_3 = dihedral_psi.nodes.new("GeometryNodeGroup")
			group_3.name = "Group"
			group_3.node_tree = backbone_position
			#Socket_3
			group_3.inputs[0].default_value = 0
			#Socket_2
			group_3.inputs[1].default_value = 'backbone_N'
			#Socket_4
			group_3.inputs[2].default_value = 0
			
			#node Group.001
			group_001_2 = dihedral_psi.nodes.new("GeometryNodeGroup")
			group_001_2.name = "Group.001"
			group_001_2.node_tree = backbone_position
			#Socket_3
			group_001_2.inputs[0].default_value = 0
			#Socket_2
			group_001_2.inputs[1].default_value = 'backbone_CA'
			#Socket_4
			group_001_2.inputs[2].default_value = 0
			
			#node Group.002
			group_002_2 = dihedral_psi.nodes.new("GeometryNodeGroup")
			group_002_2.name = "Group.002"
			group_002_2.node_tree = backbone_position
			#Socket_3
			group_002_2.inputs[0].default_value = 0
			#Socket_2
			group_002_2.inputs[1].default_value = 'backbone_C'
			#Socket_4
			group_002_2.inputs[2].default_value = 0
			
			#node Group.003
			group_003_1 = dihedral_psi.nodes.new("GeometryNodeGroup")
			group_003_1.name = "Group.003"
			group_003_1.node_tree = backbone_position
			#Socket_3
			group_003_1.inputs[0].default_value = 0
			#Socket_2
			group_003_1.inputs[1].default_value = 'backbone_N'
			#Socket_4
			group_003_1.inputs[2].default_value = 1
			
			#node Group.004
			group_004 = dihedral_psi.nodes.new("GeometryNodeGroup")
			group_004.name = "Group.004"
			group_004.node_tree = fallback_float
			#Socket_0
			group_004.inputs[0].default_value = "Psi"
			
			
			
			
			#Set locations
			group_output_12.location = (845.9104614257812, 244.38949584960938)
			group_009.location = (300.0, 240.0)
			group_3.location = (60.0, 340.0)
			group_001_2.location = (60.0, 200.0)
			group_002_2.location = (60.0, 60.0)
			group_003_1.location = (60.0, -80.0)
			group_004.location = (640.0, 320.0)
			
			#Set dimensions
			group_output_12.width, group_output_12.height = 140.0, 100.0
			group_009.width, group_009.height = 299.8184509277344, 100.0
			group_3.width, group_3.height = 140.0, 100.0
			group_001_2.width, group_001_2.height = 140.0, 100.0
			group_002_2.width, group_002_2.height = 140.0, 100.0
			group_003_1.width, group_003_1.height = 140.0, 100.0
			group_004.width, group_004.height = 140.0, 100.0
			
			#initialize dihedral_psi links
			#group_009.BA⟂(BC) -> group_output_12.BA⟂(BC)
			dihedral_psi.links.new(group_009.outputs[1], group_output_12.inputs[1])
			#group_009.BC -> group_output_12.BC
			dihedral_psi.links.new(group_009.outputs[3], group_output_12.inputs[3])
			#group_009.CD⟂(BC) -> group_output_12.CD⟂(BC)
			dihedral_psi.links.new(group_009.outputs[2], group_output_12.inputs[2])
			#group_3.Position -> group_009.A
			dihedral_psi.links.new(group_3.outputs[0], group_009.inputs[0])
			#group_001_2.Position -> group_009.B
			dihedral_psi.links.new(group_001_2.outputs[0], group_009.inputs[1])
			#group_002_2.Position -> group_009.C
			dihedral_psi.links.new(group_002_2.outputs[0], group_009.inputs[2])
			#group_003_1.Position -> group_009.D
			dihedral_psi.links.new(group_003_1.outputs[0], group_009.inputs[3])
			#group_004.Value -> group_output_12.Psi
			dihedral_psi.links.new(group_004.outputs[0], group_output_12.inputs[0])
			#group_009.Angle -> group_004.Fallback
			dihedral_psi.links.new(group_009.outputs[0], group_004.inputs[1])
			return dihedral_psi

		dihedral_psi = dihedral_psi_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Dihedral Psi", type = 'NODES')
		mod.node_group = dihedral_psi
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Dihedral_Psi.bl_idname)
			
def register():
	bpy.utils.register_class(Dihedral_Psi)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Dihedral_Psi)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
