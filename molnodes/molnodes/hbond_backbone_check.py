bl_info = {
	"name" : "HBond Backbone Check",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class HBond_Backbone_Check(bpy.types.Operator):
	bl_idname = "node.hbond_backbone_check"
	bl_label = "HBond Backbone Check"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _mn_world_scale node group
		def _mn_world_scale_node_group():
			_mn_world_scale = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_world_scale")

			_mn_world_scale.color_tag = 'NONE'
			_mn_world_scale.description = ""

			
			#_mn_world_scale interface
			#Socket world_scale
			world_scale_socket = _mn_world_scale.interface.new_socket(name = "world_scale", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			world_scale_socket.default_value = 0.009999999776482582
			world_scale_socket.min_value = -3.4028234663852886e+38
			world_scale_socket.max_value = 3.4028234663852886e+38
			world_scale_socket.subtype = 'NONE'
			world_scale_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_world_scale nodes
			#node Group Input
			group_input = _mn_world_scale.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Value
			value = _mn_world_scale.nodes.new("ShaderNodeValue")
			value.label = "world_scale"
			value.name = "Value"
			
			value.outputs[0].default_value = 0.009999999776482582
			#node Group Output
			group_output = _mn_world_scale.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			
			
			
			#Set locations
			group_input.location = (-200.0, 0.0)
			value.location = (0.0, 0.0)
			group_output.location = (190.0, 0.0)
			
			#Set dimensions
			group_input.width, group_input.height = 140.0, 100.0
			value.width, value.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			
			#initialize _mn_world_scale links
			#value.Value -> group_output.world_scale
			_mn_world_scale.links.new(value.outputs[0], group_output.inputs[0])
			return _mn_world_scale

		_mn_world_scale = _mn_world_scale_node_group()

		#initialize world_to_angstrom node group
		def world_to_angstrom_node_group():
			world_to_angstrom = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "World to Angstrom")

			world_to_angstrom.color_tag = 'NONE'
			world_to_angstrom.description = ""

			
			#world_to_angstrom interface
			#Socket Angstrom
			angstrom_socket = world_to_angstrom.interface.new_socket(name = "Angstrom", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			angstrom_socket.default_value = 0.0
			angstrom_socket.min_value = -3.4028234663852886e+38
			angstrom_socket.max_value = 3.4028234663852886e+38
			angstrom_socket.subtype = 'NONE'
			angstrom_socket.attribute_domain = 'POINT'
			
			#Socket World
			world_socket = world_to_angstrom.interface.new_socket(name = "World", in_out='INPUT', socket_type = 'NodeSocketFloat')
			world_socket.default_value = 0.5
			world_socket.min_value = -10000.0
			world_socket.max_value = 10000.0
			world_socket.subtype = 'NONE'
			world_socket.attribute_domain = 'POINT'
			
			
			#initialize world_to_angstrom nodes
			#node Group Output
			group_output_1 = world_to_angstrom.nodes.new("NodeGroupOutput")
			group_output_1.name = "Group Output"
			group_output_1.is_active_output = True
			
			#node Group Input
			group_input_1 = world_to_angstrom.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			
			#node Group
			group = world_to_angstrom.nodes.new("GeometryNodeGroup")
			group.name = "Group"
			group.node_tree = _mn_world_scale
			
			#node Math
			math = world_to_angstrom.nodes.new("ShaderNodeMath")
			math.name = "Math"
			math.operation = 'DIVIDE'
			math.use_clamp = False
			
			
			
			
			#Set locations
			group_output_1.location = (190.0, 0.0)
			group_input_1.location = (-200.0, 0.0)
			group.location = (0.0, -80.0)
			math.location = (0.0, 80.0)
			
			#Set dimensions
			group_output_1.width, group_output_1.height = 140.0, 100.0
			group_input_1.width, group_input_1.height = 140.0, 100.0
			group.width, group.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			
			#initialize world_to_angstrom links
			#group.world_scale -> math.Value
			world_to_angstrom.links.new(group.outputs[0], math.inputs[1])
			#group_input_1.World -> math.Value
			world_to_angstrom.links.new(group_input_1.outputs[0], math.inputs[0])
			#math.Value -> group_output_1.Angstrom
			world_to_angstrom.links.new(math.outputs[0], group_output_1.inputs[0])
			return world_to_angstrom

		world_to_angstrom = world_to_angstrom_node_group()

		#initialize nodegroup_001 node group
		def nodegroup_001_node_group():
			nodegroup_001 = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "NodeGroup.001")

			nodegroup_001.color_tag = 'NONE'
			nodegroup_001.description = ""

			
			#nodegroup_001 interface
			#Socket Value
			value_socket = nodegroup_001.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			value_socket.default_value = 0.0
			value_socket.min_value = -3.4028234663852886e+38
			value_socket.max_value = 3.4028234663852886e+38
			value_socket.subtype = 'NONE'
			value_socket.attribute_domain = 'POINT'
			
			#Socket Vector
			vector_socket = nodegroup_001.interface.new_socket(name = "Vector", in_out='INPUT', socket_type = 'NodeSocketVector')
			vector_socket.default_value = (0.0, 0.0, 0.0)
			vector_socket.min_value = -10000.0
			vector_socket.max_value = 10000.0
			vector_socket.subtype = 'NONE'
			vector_socket.attribute_domain = 'POINT'
			
			#Socket Vector
			vector_socket_1 = nodegroup_001.interface.new_socket(name = "Vector", in_out='INPUT', socket_type = 'NodeSocketVector')
			vector_socket_1.default_value = (0.0, 0.0, 0.0)
			vector_socket_1.min_value = -10000.0
			vector_socket_1.max_value = 10000.0
			vector_socket_1.subtype = 'NONE'
			vector_socket_1.attribute_domain = 'POINT'
			
			
			#initialize nodegroup_001 nodes
			#node Group Output
			group_output_2 = nodegroup_001.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Group Input
			group_input_2 = nodegroup_001.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
			#node Vector Math.002
			vector_math_002 = nodegroup_001.nodes.new("ShaderNodeVectorMath")
			vector_math_002.name = "Vector Math.002"
			vector_math_002.operation = 'DISTANCE'
			
			#node Math.002
			math_002 = nodegroup_001.nodes.new("ShaderNodeMath")
			math_002.name = "Math.002"
			math_002.operation = 'DIVIDE'
			math_002.use_clamp = False
			#Value
			math_002.inputs[0].default_value = 1.0
			
			#node Group.001
			group_001 = nodegroup_001.nodes.new("GeometryNodeGroup")
			group_001.name = "Group.001"
			group_001.node_tree = world_to_angstrom
			
			
			
			
			#Set locations
			group_output_2.location = (670.8533325195312, -4.1087493896484375)
			group_input_2.location = (-280.0, 0.0)
			vector_math_002.location = (-80.0, 0.0)
			math_002.location = (260.0, 0.0)
			group_001.location = (80.0, 0.0)
			
			#Set dimensions
			group_output_2.width, group_output_2.height = 140.0, 100.0
			group_input_2.width, group_input_2.height = 140.0, 100.0
			vector_math_002.width, vector_math_002.height = 140.0, 100.0
			math_002.width, math_002.height = 140.0, 100.0
			group_001.width, group_001.height = 152.50686645507812, 100.0
			
			#initialize nodegroup_001 links
			#group_001.Angstrom -> math_002.Value
			nodegroup_001.links.new(group_001.outputs[0], math_002.inputs[1])
			#group_input_2.Vector -> vector_math_002.Vector
			nodegroup_001.links.new(group_input_2.outputs[1], vector_math_002.inputs[1])
			#group_input_2.Vector -> vector_math_002.Vector
			nodegroup_001.links.new(group_input_2.outputs[0], vector_math_002.inputs[0])
			#math_002.Value -> group_output_2.Value
			nodegroup_001.links.new(math_002.outputs[0], group_output_2.inputs[0])
			#vector_math_002.Value -> group_001.World
			nodegroup_001.links.new(vector_math_002.outputs[1], group_001.inputs[0])
			return nodegroup_001

		nodegroup_001 = nodegroup_001_node_group()

		#initialize hbond_energy node group
		def hbond_energy_node_group():
			hbond_energy = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "HBond Energy")

			hbond_energy.color_tag = 'NONE'
			hbond_energy.description = ""

			
			#hbond_energy interface
			#Socket Is Bonded
			is_bonded_socket = hbond_energy.interface.new_socket(name = "Is Bonded", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_bonded_socket.default_value = False
			is_bonded_socket.attribute_domain = 'POINT'
			
			#Socket Bond Energy
			bond_energy_socket = hbond_energy.interface.new_socket(name = "Bond Energy", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			bond_energy_socket.default_value = 0.0
			bond_energy_socket.min_value = -3.4028234663852886e+38
			bond_energy_socket.max_value = 3.4028234663852886e+38
			bond_energy_socket.subtype = 'NONE'
			bond_energy_socket.attribute_domain = 'POINT'
			
			#Socket Bond Vector
			bond_vector_socket = hbond_energy.interface.new_socket(name = "Bond Vector", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			bond_vector_socket.default_value = (0.0, 0.0, 0.0)
			bond_vector_socket.min_value = -3.4028234663852886e+38
			bond_vector_socket.max_value = 3.4028234663852886e+38
			bond_vector_socket.subtype = 'NONE'
			bond_vector_socket.attribute_domain = 'POINT'
			
			#Socket O
			o_socket = hbond_energy.interface.new_socket(name = "O", in_out='INPUT', socket_type = 'NodeSocketVector')
			o_socket.default_value = (0.0, 0.0, 0.0)
			o_socket.min_value = -3.4028234663852886e+38
			o_socket.max_value = 3.4028234663852886e+38
			o_socket.subtype = 'NONE'
			o_socket.attribute_domain = 'POINT'
			
			#Socket C
			c_socket = hbond_energy.interface.new_socket(name = "C", in_out='INPUT', socket_type = 'NodeSocketVector')
			c_socket.default_value = (0.0, 0.0, 0.0)
			c_socket.min_value = -3.4028234663852886e+38
			c_socket.max_value = 3.4028234663852886e+38
			c_socket.subtype = 'NONE'
			c_socket.attribute_domain = 'POINT'
			
			#Socket N
			n_socket = hbond_energy.interface.new_socket(name = "N", in_out='INPUT', socket_type = 'NodeSocketVector')
			n_socket.default_value = (0.0, 0.0, 0.0)
			n_socket.min_value = -3.4028234663852886e+38
			n_socket.max_value = 3.4028234663852886e+38
			n_socket.subtype = 'NONE'
			n_socket.attribute_domain = 'POINT'
			
			#Socket H
			h_socket = hbond_energy.interface.new_socket(name = "H", in_out='INPUT', socket_type = 'NodeSocketVector')
			h_socket.default_value = (0.0, 0.0, 0.0)
			h_socket.min_value = -3.4028234663852886e+38
			h_socket.max_value = 3.4028234663852886e+38
			h_socket.subtype = 'NONE'
			h_socket.attribute_domain = 'POINT'
			
			
			#initialize hbond_energy nodes
			#node Group Output
			group_output_3 = hbond_energy.nodes.new("NodeGroupOutput")
			group_output_3.name = "Group Output"
			group_output_3.is_active_output = True
			
			#node Group Input
			group_input_3 = hbond_energy.nodes.new("NodeGroupInput")
			group_input_3.name = "Group Input"
			
			#node Group.003
			group_003 = hbond_energy.nodes.new("GeometryNodeGroup")
			group_003.label = "1/r(ON)"
			group_003.name = "Group.003"
			group_003.node_tree = nodegroup_001
			
			#node Group.008
			group_008 = hbond_energy.nodes.new("GeometryNodeGroup")
			group_008.label = "1/r(CH)"
			group_008.name = "Group.008"
			group_008.node_tree = nodegroup_001
			
			#node Group.009
			group_009 = hbond_energy.nodes.new("GeometryNodeGroup")
			group_009.label = "1/r(OH)"
			group_009.name = "Group.009"
			group_009.node_tree = nodegroup_001
			
			#node Group.010
			group_010 = hbond_energy.nodes.new("GeometryNodeGroup")
			group_010.label = "1/r(CN)"
			group_010.name = "Group.010"
			group_010.node_tree = nodegroup_001
			
			#node Math.002
			math_002_1 = hbond_energy.nodes.new("ShaderNodeMath")
			math_002_1.name = "Math.002"
			math_002_1.hide = True
			math_002_1.operation = 'ADD'
			math_002_1.use_clamp = False
			
			#node Math.003
			math_003 = hbond_energy.nodes.new("ShaderNodeMath")
			math_003.name = "Math.003"
			math_003.hide = True
			math_003.operation = 'SUBTRACT'
			math_003.use_clamp = False
			
			#node Math.004
			math_004 = hbond_energy.nodes.new("ShaderNodeMath")
			math_004.name = "Math.004"
			math_004.hide = True
			math_004.operation = 'SUBTRACT'
			math_004.use_clamp = False
			
			#node Math.005
			math_005 = hbond_energy.nodes.new("ShaderNodeMath")
			math_005.label = "* q1q2"
			math_005.name = "Math.005"
			math_005.operation = 'MULTIPLY'
			math_005.use_clamp = False
			#Value_001
			math_005.inputs[1].default_value = 0.08399999886751175
			
			#node Math.006
			math_006 = hbond_energy.nodes.new("ShaderNodeMath")
			math_006.label = "*f"
			math_006.name = "Math.006"
			math_006.operation = 'MULTIPLY'
			math_006.use_clamp = False
			#Value_001
			math_006.inputs[1].default_value = 332.0
			
			#node Vector Math
			vector_math = hbond_energy.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.operation = 'SUBTRACT'
			
			#node Math.007
			math_007 = hbond_energy.nodes.new("ShaderNodeMath")
			math_007.label = "*e"
			math_007.name = "Math.007"
			math_007.mute = True
			math_007.operation = 'MULTIPLY'
			math_007.use_clamp = False
			#Value_001
			math_007.inputs[1].default_value = -1.0
			
			#node Compare
			compare = hbond_energy.nodes.new("FunctionNodeCompare")
			compare.label = "Cutoff kcal/mol"
			compare.name = "Compare"
			compare.data_type = 'FLOAT'
			compare.mode = 'ELEMENT'
			compare.operation = 'LESS_THAN'
			#B
			compare.inputs[1].default_value = -0.5
			
			#node Group Input.001
			group_input_001 = hbond_energy.nodes.new("NodeGroupInput")
			group_input_001.name = "Group Input.001"
			
			
			
			
			#Set locations
			group_output_3.location = (900.0, 40.0)
			group_input_3.location = (-644.257568359375, 10.571624755859375)
			group_003.location = (-355.197021484375, 210.6334228515625)
			group_008.location = (-360.0, 69.3665771484375)
			group_009.location = (-360.0, -70.6334228515625)
			group_010.location = (-360.0, -210.6334228515625)
			math_002_1.location = (-180.0, 60.0)
			math_003.location = (-180.0, -80.0)
			math_004.location = (-180.0, -220.0)
			math_005.location = (320.0, 100.0)
			math_006.location = (480.0, 100.0)
			vector_math.location = (480.0, -60.0)
			math_007.location = (160.0, 100.0)
			compare.location = (720.0, 220.0)
			group_input_001.location = (320.0, -60.0)
			
			#Set dimensions
			group_output_3.width, group_output_3.height = 140.0, 100.0
			group_input_3.width, group_input_3.height = 140.0, 100.0
			group_003.width, group_003.height = 140.0, 100.0
			group_008.width, group_008.height = 140.0, 100.0
			group_009.width, group_009.height = 140.0, 100.0
			group_010.width, group_010.height = 140.0, 100.0
			math_002_1.width, math_002_1.height = 140.0, 100.0
			math_003.width, math_003.height = 140.0, 100.0
			math_004.width, math_004.height = 140.0, 100.0
			math_005.width, math_005.height = 140.0, 100.0
			math_006.width, math_006.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			math_007.width, math_007.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			group_input_001.width, group_input_001.height = 140.0, 100.0
			
			#initialize hbond_energy links
			#math_002_1.Value -> math_003.Value
			hbond_energy.links.new(math_002_1.outputs[0], math_003.inputs[0])
			#group_009.Value -> math_003.Value
			hbond_energy.links.new(group_009.outputs[0], math_003.inputs[1])
			#math_007.Value -> math_005.Value
			hbond_energy.links.new(math_007.outputs[0], math_005.inputs[0])
			#group_008.Value -> math_002_1.Value
			hbond_energy.links.new(group_008.outputs[0], math_002_1.inputs[1])
			#math_003.Value -> math_004.Value
			hbond_energy.links.new(math_003.outputs[0], math_004.inputs[0])
			#group_010.Value -> math_004.Value
			hbond_energy.links.new(group_010.outputs[0], math_004.inputs[1])
			#group_003.Value -> math_002_1.Value
			hbond_energy.links.new(group_003.outputs[0], math_002_1.inputs[0])
			#math_005.Value -> math_006.Value
			hbond_energy.links.new(math_005.outputs[0], math_006.inputs[0])
			#math_006.Value -> group_output_3.Bond Energy
			hbond_energy.links.new(math_006.outputs[0], group_output_3.inputs[1])
			#math_004.Value -> math_007.Value
			hbond_energy.links.new(math_004.outputs[0], math_007.inputs[0])
			#vector_math.Vector -> group_output_3.Bond Vector
			hbond_energy.links.new(vector_math.outputs[0], group_output_3.inputs[2])
			#math_006.Value -> compare.A
			hbond_energy.links.new(math_006.outputs[0], compare.inputs[0])
			#compare.Result -> group_output_3.Is Bonded
			hbond_energy.links.new(compare.outputs[0], group_output_3.inputs[0])
			#group_input_3.O -> group_003.Vector
			hbond_energy.links.new(group_input_3.outputs[0], group_003.inputs[0])
			#group_input_3.N -> group_003.Vector
			hbond_energy.links.new(group_input_3.outputs[2], group_003.inputs[1])
			#group_input_3.C -> group_008.Vector
			hbond_energy.links.new(group_input_3.outputs[1], group_008.inputs[0])
			#group_input_3.H -> group_008.Vector
			hbond_energy.links.new(group_input_3.outputs[3], group_008.inputs[1])
			#group_input_3.O -> group_009.Vector
			hbond_energy.links.new(group_input_3.outputs[0], group_009.inputs[0])
			#group_input_3.H -> group_009.Vector
			hbond_energy.links.new(group_input_3.outputs[3], group_009.inputs[1])
			#group_input_3.C -> group_010.Vector
			hbond_energy.links.new(group_input_3.outputs[1], group_010.inputs[0])
			#group_input_3.N -> group_010.Vector
			hbond_energy.links.new(group_input_3.outputs[2], group_010.inputs[1])
			#group_input_001.H -> vector_math.Vector
			hbond_energy.links.new(group_input_001.outputs[3], vector_math.inputs[1])
			#group_input_001.O -> vector_math.Vector
			hbond_energy.links.new(group_input_001.outputs[0], vector_math.inputs[0])
			return hbond_energy

		hbond_energy = hbond_energy_node_group()

		#initialize offset_vector node group
		def offset_vector_node_group():
			offset_vector = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Offset Vector")

			offset_vector.color_tag = 'CONVERTER'
			offset_vector.description = ""

			
			#offset_vector interface
			#Socket Value
			value_socket_1 = offset_vector.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			value_socket_1.default_value = (0.0, 0.0, 0.0)
			value_socket_1.min_value = -3.4028234663852886e+38
			value_socket_1.max_value = 3.4028234663852886e+38
			value_socket_1.subtype = 'NONE'
			value_socket_1.attribute_domain = 'POINT'
			
			#Socket Index
			index_socket = offset_vector.interface.new_socket(name = "Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			index_socket.default_value = 0
			index_socket.min_value = 0
			index_socket.max_value = 2147483647
			index_socket.subtype = 'NONE'
			index_socket.attribute_domain = 'POINT'
			
			#Socket Position
			position_socket = offset_vector.interface.new_socket(name = "Position", in_out='INPUT', socket_type = 'NodeSocketVector')
			position_socket.default_value = (0.0, 0.0, 0.0)
			position_socket.min_value = -3.4028234663852886e+38
			position_socket.max_value = 3.4028234663852886e+38
			position_socket.subtype = 'NONE'
			position_socket.attribute_domain = 'POINT'
			position_socket.hide_value = True
			
			#Socket Offset
			offset_socket = offset_vector.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket.default_value = 0
			offset_socket.min_value = -2147483647
			offset_socket.max_value = 2147483647
			offset_socket.subtype = 'NONE'
			offset_socket.attribute_domain = 'POINT'
			
			
			#initialize offset_vector nodes
			#node Group Output
			group_output_4 = offset_vector.nodes.new("NodeGroupOutput")
			group_output_4.name = "Group Output"
			group_output_4.is_active_output = True
			
			#node Group Input
			group_input_4 = offset_vector.nodes.new("NodeGroupInput")
			group_input_4.name = "Group Input"
			
			#node Evaluate at Index
			evaluate_at_index = offset_vector.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index.name = "Evaluate at Index"
			evaluate_at_index.data_type = 'FLOAT_VECTOR'
			evaluate_at_index.domain = 'POINT'
			
			#node Math
			math_1 = offset_vector.nodes.new("ShaderNodeMath")
			math_1.name = "Math"
			math_1.operation = 'ADD'
			math_1.use_clamp = False
			
			
			
			
			#Set locations
			group_output_4.location = (300.0, 20.0)
			group_input_4.location = (-273.81378173828125, 0.0)
			evaluate_at_index.location = (120.0, 20.0)
			math_1.location = (-60.0, 20.0)
			
			#Set dimensions
			group_output_4.width, group_output_4.height = 140.0, 100.0
			group_input_4.width, group_input_4.height = 140.0, 100.0
			evaluate_at_index.width, evaluate_at_index.height = 140.0, 100.0
			math_1.width, math_1.height = 140.0, 100.0
			
			#initialize offset_vector links
			#group_input_4.Position -> evaluate_at_index.Value
			offset_vector.links.new(group_input_4.outputs[1], evaluate_at_index.inputs[1])
			#evaluate_at_index.Value -> group_output_4.Value
			offset_vector.links.new(evaluate_at_index.outputs[0], group_output_4.inputs[0])
			#group_input_4.Index -> math_1.Value
			offset_vector.links.new(group_input_4.outputs[0], math_1.inputs[0])
			#group_input_4.Offset -> math_1.Value
			offset_vector.links.new(group_input_4.outputs[2], math_1.inputs[1])
			#math_1.Value -> evaluate_at_index.Index
			offset_vector.links.new(math_1.outputs[0], evaluate_at_index.inputs[0])
			return offset_vector

		offset_vector = offset_vector_node_group()

		#initialize mn_units node group
		def mn_units_node_group():
			mn_units = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "MN Units")

			mn_units.color_tag = 'NONE'
			mn_units.description = ""

			
			#mn_units interface
			#Socket Angstrom
			angstrom_socket_1 = mn_units.interface.new_socket(name = "Angstrom", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			angstrom_socket_1.default_value = 0.0
			angstrom_socket_1.min_value = -3.4028234663852886e+38
			angstrom_socket_1.max_value = 3.4028234663852886e+38
			angstrom_socket_1.subtype = 'NONE'
			angstrom_socket_1.attribute_domain = 'POINT'
			
			#Socket Nanometre
			nanometre_socket = mn_units.interface.new_socket(name = "Nanometre", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			nanometre_socket.default_value = 0.0
			nanometre_socket.min_value = -3.4028234663852886e+38
			nanometre_socket.max_value = 3.4028234663852886e+38
			nanometre_socket.subtype = 'NONE'
			nanometre_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_2 = mn_units.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket_2.default_value = 3.0
			value_socket_2.min_value = -10000.0
			value_socket_2.max_value = 10000.0
			value_socket_2.subtype = 'NONE'
			value_socket_2.attribute_domain = 'POINT'
			value_socket_2.description = "A value which will be scaled appropriately for the world"
			
			
			#initialize mn_units nodes
			#node Group Output
			group_output_5 = mn_units.nodes.new("NodeGroupOutput")
			group_output_5.name = "Group Output"
			group_output_5.is_active_output = True
			
			#node Group Input
			group_input_5 = mn_units.nodes.new("NodeGroupInput")
			group_input_5.name = "Group Input"
			
			#node Math
			math_2 = mn_units.nodes.new("ShaderNodeMath")
			math_2.name = "Math"
			math_2.operation = 'MULTIPLY'
			math_2.use_clamp = False
			
			#node Math.001
			math_001 = mn_units.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.operation = 'MULTIPLY'
			math_001.use_clamp = False
			#Value_001
			math_001.inputs[1].default_value = 10.0
			
			#node Group
			group_1 = mn_units.nodes.new("GeometryNodeGroup")
			group_1.name = "Group"
			group_1.node_tree = _mn_world_scale
			
			
			
			
			#Set locations
			group_output_5.location = (190.0, 0.0)
			group_input_5.location = (-240.0, 0.0)
			math_2.location = (-60.0, 0.0)
			math_001.location = (-60.0, -160.0)
			group_1.location = (-304.00421142578125, -104.114013671875)
			
			#Set dimensions
			group_output_5.width, group_output_5.height = 140.0, 100.0
			group_input_5.width, group_input_5.height = 140.0, 100.0
			math_2.width, math_2.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			group_1.width, group_1.height = 197.58424377441406, 100.0
			
			#initialize mn_units links
			#math_2.Value -> group_output_5.Angstrom
			mn_units.links.new(math_2.outputs[0], group_output_5.inputs[0])
			#group_input_5.Value -> math_2.Value
			mn_units.links.new(group_input_5.outputs[0], math_2.inputs[0])
			#group_1.world_scale -> math_2.Value
			mn_units.links.new(group_1.outputs[0], math_2.inputs[1])
			#math_2.Value -> math_001.Value
			mn_units.links.new(math_2.outputs[0], math_001.inputs[0])
			#math_001.Value -> group_output_5.Nanometre
			mn_units.links.new(math_001.outputs[0], group_output_5.inputs[1])
			return mn_units

		mn_units = mn_units_node_group()

		#initialize backbone_nh node group
		def backbone_nh_node_group():
			backbone_nh = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Backbone NH")

			backbone_nh.color_tag = 'NONE'
			backbone_nh.description = ""

			
			#backbone_nh interface
			#Socket H
			h_socket_1 = backbone_nh.interface.new_socket(name = "H", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			h_socket_1.default_value = (0.0, 0.0, 0.0)
			h_socket_1.min_value = -3.4028234663852886e+38
			h_socket_1.max_value = 3.4028234663852886e+38
			h_socket_1.subtype = 'NONE'
			h_socket_1.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_3 = backbone_nh.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket_3.default_value = 1.0
			value_socket_3.min_value = -10000.0
			value_socket_3.max_value = 10000.0
			value_socket_3.subtype = 'NONE'
			value_socket_3.attribute_domain = 'POINT'
			
			
			#initialize backbone_nh nodes
			#node Group Output
			group_output_6 = backbone_nh.nodes.new("NodeGroupOutput")
			group_output_6.name = "Group Output"
			group_output_6.is_active_output = True
			
			#node Group Input
			group_input_6 = backbone_nh.nodes.new("NodeGroupInput")
			group_input_6.name = "Group Input"
			
			#node Named Attribute
			named_attribute = backbone_nh.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute.inputs[0].default_value = "backbone_N"
			
			#node Named Attribute.001
			named_attribute_001 = backbone_nh.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_001.inputs[0].default_value = "backbone_CA"
			
			#node Named Attribute.002
			named_attribute_002 = backbone_nh.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002.name = "Named Attribute.002"
			named_attribute_002.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_002.inputs[0].default_value = "backbone_C"
			
			#node Group.002
			group_002 = backbone_nh.nodes.new("GeometryNodeGroup")
			group_002.name = "Group.002"
			group_002.node_tree = offset_vector
			#Socket_2
			group_002.inputs[0].default_value = 0
			#Socket_3
			group_002.inputs[2].default_value = -1
			
			#node Vector Math
			vector_math_1 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_1.name = "Vector Math"
			vector_math_1.operation = 'SUBTRACT'
			
			#node Vector Math.001
			vector_math_001 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_001.name = "Vector Math.001"
			vector_math_001.operation = 'SUBTRACT'
			
			#node Vector Math.002
			vector_math_002_1 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_002_1.name = "Vector Math.002"
			vector_math_002_1.operation = 'NORMALIZE'
			
			#node Vector Math.003
			vector_math_003 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_003.name = "Vector Math.003"
			vector_math_003.operation = 'NORMALIZE'
			
			#node Vector Math.005
			vector_math_005 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_005.name = "Vector Math.005"
			vector_math_005.operation = 'ADD'
			
			#node Vector Math.006
			vector_math_006 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_006.name = "Vector Math.006"
			vector_math_006.operation = 'ADD'
			
			#node Vector Math.004
			vector_math_004 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_004.name = "Vector Math.004"
			vector_math_004.operation = 'SCALE'
			
			#node Group.003
			group_003_1 = backbone_nh.nodes.new("GeometryNodeGroup")
			group_003_1.name = "Group.003"
			group_003_1.node_tree = mn_units
			
			#node Vector Math.007
			vector_math_007 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_007.name = "Vector Math.007"
			vector_math_007.operation = 'NORMALIZE'
			
			
			
			
			#Set locations
			group_output_6.location = (620.0, 0.0)
			group_input_6.location = (-630.0, 0.0)
			named_attribute.location = (-430.0, 140.0)
			named_attribute_001.location = (-430.0, 0.0)
			named_attribute_002.location = (-430.0, -140.0)
			group_002.location = (-210.0, -120.0)
			vector_math_1.location = (-50.0, 0.0)
			vector_math_001.location = (-50.0, 140.0)
			vector_math_002_1.location = (110.0, 140.0)
			vector_math_003.location = (110.0, 0.0)
			vector_math_005.location = (270.0, 140.0)
			vector_math_006.location = (430.0, 140.0)
			vector_math_004.location = (260.0, -120.0)
			group_003_1.location = (100.0, -120.0)
			vector_math_007.location = (260.0, 0.0)
			
			#Set dimensions
			group_output_6.width, group_output_6.height = 140.0, 100.0
			group_input_6.width, group_input_6.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 189.579833984375, 100.0
			named_attribute_001.width, named_attribute_001.height = 189.579833984375, 100.0
			named_attribute_002.width, named_attribute_002.height = 189.579833984375, 100.0
			group_002.width, group_002.height = 140.0, 100.0
			vector_math_1.width, vector_math_1.height = 140.0, 100.0
			vector_math_001.width, vector_math_001.height = 140.0, 100.0
			vector_math_002_1.width, vector_math_002_1.height = 140.0, 100.0
			vector_math_003.width, vector_math_003.height = 140.0, 100.0
			vector_math_005.width, vector_math_005.height = 140.0, 100.0
			vector_math_006.width, vector_math_006.height = 140.0, 100.0
			vector_math_004.width, vector_math_004.height = 140.0, 100.0
			group_003_1.width, group_003_1.height = 140.0, 100.0
			vector_math_007.width, vector_math_007.height = 140.0, 100.0
			
			#initialize backbone_nh links
			#vector_math_004.Vector -> vector_math_006.Vector
			backbone_nh.links.new(vector_math_004.outputs[0], vector_math_006.inputs[1])
			#named_attribute_001.Attribute -> vector_math_001.Vector
			backbone_nh.links.new(named_attribute_001.outputs[0], vector_math_001.inputs[1])
			#named_attribute_002.Attribute -> group_002.Position
			backbone_nh.links.new(named_attribute_002.outputs[0], group_002.inputs[1])
			#named_attribute.Attribute -> vector_math_1.Vector
			backbone_nh.links.new(named_attribute.outputs[0], vector_math_1.inputs[0])
			#vector_math_1.Vector -> vector_math_003.Vector
			backbone_nh.links.new(vector_math_1.outputs[0], vector_math_003.inputs[0])
			#group_003_1.Angstrom -> vector_math_004.Scale
			backbone_nh.links.new(group_003_1.outputs[0], vector_math_004.inputs[3])
			#vector_math_003.Vector -> vector_math_005.Vector
			backbone_nh.links.new(vector_math_003.outputs[0], vector_math_005.inputs[1])
			#group_002.Value -> vector_math_1.Vector
			backbone_nh.links.new(group_002.outputs[0], vector_math_1.inputs[1])
			#vector_math_002_1.Vector -> vector_math_005.Vector
			backbone_nh.links.new(vector_math_002_1.outputs[0], vector_math_005.inputs[0])
			#named_attribute.Attribute -> vector_math_001.Vector
			backbone_nh.links.new(named_attribute.outputs[0], vector_math_001.inputs[0])
			#vector_math_001.Vector -> vector_math_002_1.Vector
			backbone_nh.links.new(vector_math_001.outputs[0], vector_math_002_1.inputs[0])
			#named_attribute.Attribute -> vector_math_006.Vector
			backbone_nh.links.new(named_attribute.outputs[0], vector_math_006.inputs[0])
			#vector_math_006.Vector -> group_output_6.H
			backbone_nh.links.new(vector_math_006.outputs[0], group_output_6.inputs[0])
			#group_input_6.Value -> group_003_1.Value
			backbone_nh.links.new(group_input_6.outputs[0], group_003_1.inputs[0])
			#vector_math_005.Vector -> vector_math_007.Vector
			backbone_nh.links.new(vector_math_005.outputs[0], vector_math_007.inputs[0])
			#vector_math_007.Vector -> vector_math_004.Vector
			backbone_nh.links.new(vector_math_007.outputs[0], vector_math_004.inputs[0])
			return backbone_nh

		backbone_nh = backbone_nh_node_group()

		#initialize mn_topo_backbone node group
		def mn_topo_backbone_node_group():
			mn_topo_backbone = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "MN_topo_backbone")

			mn_topo_backbone.color_tag = 'NONE'
			mn_topo_backbone.description = ""

			
			#mn_topo_backbone interface
			#Socket O
			o_socket_1 = mn_topo_backbone.interface.new_socket(name = "O", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			o_socket_1.default_value = (0.0, 0.0, 0.0)
			o_socket_1.min_value = -3.4028234663852886e+38
			o_socket_1.max_value = 3.4028234663852886e+38
			o_socket_1.subtype = 'NONE'
			o_socket_1.attribute_domain = 'POINT'
			
			#Socket C
			c_socket_1 = mn_topo_backbone.interface.new_socket(name = "C", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			c_socket_1.default_value = (0.0, 0.0, 0.0)
			c_socket_1.min_value = -3.4028234663852886e+38
			c_socket_1.max_value = 3.4028234663852886e+38
			c_socket_1.subtype = 'NONE'
			c_socket_1.attribute_domain = 'POINT'
			
			#Socket CA
			ca_socket = mn_topo_backbone.interface.new_socket(name = "CA", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			ca_socket.default_value = (0.0, 0.0, 0.0)
			ca_socket.min_value = -3.4028234663852886e+38
			ca_socket.max_value = 3.4028234663852886e+38
			ca_socket.subtype = 'NONE'
			ca_socket.attribute_domain = 'POINT'
			
			#Socket N
			n_socket_1 = mn_topo_backbone.interface.new_socket(name = "N", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			n_socket_1.default_value = (0.0, 0.0, 0.0)
			n_socket_1.min_value = -3.4028234663852886e+38
			n_socket_1.max_value = 3.4028234663852886e+38
			n_socket_1.subtype = 'NONE'
			n_socket_1.attribute_domain = 'POINT'
			
			#Socket NH
			nh_socket = mn_topo_backbone.interface.new_socket(name = "NH", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			nh_socket.default_value = (0.0, 0.0, 0.0)
			nh_socket.min_value = -3.4028234663852886e+38
			nh_socket.max_value = 3.4028234663852886e+38
			nh_socket.subtype = 'NONE'
			nh_socket.attribute_domain = 'POINT'
			
			#Socket Offset
			offset_socket_1 = mn_topo_backbone.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket_1.default_value = 0
			offset_socket_1.min_value = -2147483648
			offset_socket_1.max_value = 2147483647
			offset_socket_1.subtype = 'NONE'
			offset_socket_1.attribute_domain = 'POINT'
			
			
			#initialize mn_topo_backbone nodes
			#node Group Output
			group_output_7 = mn_topo_backbone.nodes.new("NodeGroupOutput")
			group_output_7.name = "Group Output"
			group_output_7.is_active_output = True
			
			#node Group Input
			group_input_7 = mn_topo_backbone.nodes.new("NodeGroupInput")
			group_input_7.name = "Group Input"
			
			#node Named Attribute.001
			named_attribute_001_1 = mn_topo_backbone.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001_1.name = "Named Attribute.001"
			named_attribute_001_1.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_001_1.inputs[0].default_value = "backbone_O"
			
			#node Named Attribute.002
			named_attribute_002_1 = mn_topo_backbone.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002_1.name = "Named Attribute.002"
			named_attribute_002_1.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_002_1.inputs[0].default_value = "backbone_C"
			
			#node Evaluate at Index
			evaluate_at_index_1 = mn_topo_backbone.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_1.name = "Evaluate at Index"
			evaluate_at_index_1.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_1.domain = 'POINT'
			
			#node Math
			math_3 = mn_topo_backbone.nodes.new("ShaderNodeMath")
			math_3.name = "Math"
			math_3.operation = 'ADD'
			math_3.use_clamp = False
			
			#node Index
			index = mn_topo_backbone.nodes.new("GeometryNodeInputIndex")
			index.name = "Index"
			
			#node Evaluate at Index.001
			evaluate_at_index_001 = mn_topo_backbone.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001.name = "Evaluate at Index.001"
			evaluate_at_index_001.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_001.domain = 'POINT'
			
			#node Named Attribute.003
			named_attribute_003 = mn_topo_backbone.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_003.name = "Named Attribute.003"
			named_attribute_003.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_003.inputs[0].default_value = "backbone_CA"
			
			#node Evaluate at Index.002
			evaluate_at_index_002 = mn_topo_backbone.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_002.name = "Evaluate at Index.002"
			evaluate_at_index_002.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_002.domain = 'POINT'
			
			#node Evaluate at Index.003
			evaluate_at_index_003 = mn_topo_backbone.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_003.name = "Evaluate at Index.003"
			evaluate_at_index_003.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_003.domain = 'POINT'
			
			#node Named Attribute.004
			named_attribute_004 = mn_topo_backbone.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_004.name = "Named Attribute.004"
			named_attribute_004.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_004.inputs[0].default_value = "backbone_N"
			
			#node Reroute
			reroute = mn_topo_backbone.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Group
			group_2 = mn_topo_backbone.nodes.new("GeometryNodeGroup")
			group_2.name = "Group"
			group_2.node_tree = backbone_nh
			#Socket_1
			group_2.inputs[0].default_value = 1.0099999904632568
			
			#node Evaluate at Index.004
			evaluate_at_index_004 = mn_topo_backbone.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_004.name = "Evaluate at Index.004"
			evaluate_at_index_004.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_004.domain = 'POINT'
			
			#node Named Attribute.005
			named_attribute_005 = mn_topo_backbone.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_005.name = "Named Attribute.005"
			named_attribute_005.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_005.inputs[0].default_value = "backbone_NH"
			
			#node Switch
			switch = mn_topo_backbone.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'VECTOR'
			
			#node Boolean Math
			boolean_math = mn_topo_backbone.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'NOT'
			
			
			
			
			#Set locations
			group_output_7.location = (320.0, -220.0)
			group_input_7.location = (-520.0, -260.0)
			named_attribute_001_1.location = (-300.0, 40.0)
			named_attribute_002_1.location = (-300.0, -100.0)
			evaluate_at_index_1.location = (80.0, -14.04681396484375)
			math_3.location = (-260.0, -260.0)
			index.location = (-520.0, -360.0)
			evaluate_at_index_001.location = (80.0, -170.47593688964844)
			named_attribute_003.location = (-300.0, -460.0)
			evaluate_at_index_002.location = (80.0, -326.90509033203125)
			evaluate_at_index_003.location = (80.0, -480.0)
			named_attribute_004.location = (-300.0, -600.0)
			reroute.location = (20.0, -340.0)
			group_2.location = (-640.0, -920.0)
			evaluate_at_index_004.location = (77.81956481933594, -655.5125732421875)
			named_attribute_005.location = (-640.0, -780.0)
			switch.location = (-240.0, -780.0)
			boolean_math.location = (-420.0, -780.0)
			
			#Set dimensions
			group_output_7.width, group_output_7.height = 140.0, 100.0
			group_input_7.width, group_input_7.height = 140.0, 100.0
			named_attribute_001_1.width, named_attribute_001_1.height = 186.42977905273438, 100.0
			named_attribute_002_1.width, named_attribute_002_1.height = 186.42977905273438, 100.0
			evaluate_at_index_1.width, evaluate_at_index_1.height = 140.0, 100.0
			math_3.width, math_3.height = 140.0, 100.0
			index.width, index.height = 140.0, 100.0
			evaluate_at_index_001.width, evaluate_at_index_001.height = 140.0, 100.0
			named_attribute_003.width, named_attribute_003.height = 186.42977905273438, 100.0
			evaluate_at_index_002.width, evaluate_at_index_002.height = 140.0, 100.0
			evaluate_at_index_003.width, evaluate_at_index_003.height = 140.0, 100.0
			named_attribute_004.width, named_attribute_004.height = 186.42977905273438, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			group_2.width, group_2.height = 186.0294189453125, 100.0
			evaluate_at_index_004.width, evaluate_at_index_004.height = 140.0, 100.0
			named_attribute_005.width, named_attribute_005.height = 186.42977905273438, 100.0
			switch.width, switch.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			
			#initialize mn_topo_backbone links
			#named_attribute_001_1.Attribute -> evaluate_at_index_1.Value
			mn_topo_backbone.links.new(named_attribute_001_1.outputs[0], evaluate_at_index_1.inputs[1])
			#reroute.Output -> evaluate_at_index_1.Index
			mn_topo_backbone.links.new(reroute.outputs[0], evaluate_at_index_1.inputs[0])
			#group_input_7.Offset -> math_3.Value
			mn_topo_backbone.links.new(group_input_7.outputs[0], math_3.inputs[0])
			#reroute.Output -> evaluate_at_index_001.Index
			mn_topo_backbone.links.new(reroute.outputs[0], evaluate_at_index_001.inputs[0])
			#named_attribute_002_1.Attribute -> evaluate_at_index_001.Value
			mn_topo_backbone.links.new(named_attribute_002_1.outputs[0], evaluate_at_index_001.inputs[1])
			#reroute.Output -> evaluate_at_index_002.Index
			mn_topo_backbone.links.new(reroute.outputs[0], evaluate_at_index_002.inputs[0])
			#named_attribute_003.Attribute -> evaluate_at_index_002.Value
			mn_topo_backbone.links.new(named_attribute_003.outputs[0], evaluate_at_index_002.inputs[1])
			#reroute.Output -> evaluate_at_index_003.Index
			mn_topo_backbone.links.new(reroute.outputs[0], evaluate_at_index_003.inputs[0])
			#named_attribute_004.Attribute -> evaluate_at_index_003.Value
			mn_topo_backbone.links.new(named_attribute_004.outputs[0], evaluate_at_index_003.inputs[1])
			#index.Index -> math_3.Value
			mn_topo_backbone.links.new(index.outputs[0], math_3.inputs[1])
			#math_3.Value -> reroute.Input
			mn_topo_backbone.links.new(math_3.outputs[0], reroute.inputs[0])
			#evaluate_at_index_003.Value -> group_output_7.N
			mn_topo_backbone.links.new(evaluate_at_index_003.outputs[0], group_output_7.inputs[3])
			#evaluate_at_index_002.Value -> group_output_7.CA
			mn_topo_backbone.links.new(evaluate_at_index_002.outputs[0], group_output_7.inputs[2])
			#evaluate_at_index_001.Value -> group_output_7.C
			mn_topo_backbone.links.new(evaluate_at_index_001.outputs[0], group_output_7.inputs[1])
			#evaluate_at_index_1.Value -> group_output_7.O
			mn_topo_backbone.links.new(evaluate_at_index_1.outputs[0], group_output_7.inputs[0])
			#reroute.Output -> evaluate_at_index_004.Index
			mn_topo_backbone.links.new(reroute.outputs[0], evaluate_at_index_004.inputs[0])
			#evaluate_at_index_004.Value -> group_output_7.NH
			mn_topo_backbone.links.new(evaluate_at_index_004.outputs[0], group_output_7.inputs[4])
			#group_2.H -> switch.True
			mn_topo_backbone.links.new(group_2.outputs[0], switch.inputs[2])
			#switch.Output -> evaluate_at_index_004.Value
			mn_topo_backbone.links.new(switch.outputs[0], evaluate_at_index_004.inputs[1])
			#named_attribute_005.Exists -> boolean_math.Boolean
			mn_topo_backbone.links.new(named_attribute_005.outputs[1], boolean_math.inputs[0])
			#boolean_math.Boolean -> switch.Switch
			mn_topo_backbone.links.new(boolean_math.outputs[0], switch.inputs[0])
			#named_attribute_005.Attribute -> switch.False
			mn_topo_backbone.links.new(named_attribute_005.outputs[0], switch.inputs[1])
			return mn_topo_backbone

		mn_topo_backbone = mn_topo_backbone_node_group()

		#initialize hbond_backbone_check node group
		def hbond_backbone_check_node_group():
			hbond_backbone_check = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "HBond Backbone Check")

			hbond_backbone_check.color_tag = 'NONE'
			hbond_backbone_check.description = ""

			
			#hbond_backbone_check interface
			#Socket Is Bonded
			is_bonded_socket_1 = hbond_backbone_check.interface.new_socket(name = "Is Bonded", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_bonded_socket_1.default_value = False
			is_bonded_socket_1.attribute_domain = 'POINT'
			
			#Socket Bond Energy
			bond_energy_socket_1 = hbond_backbone_check.interface.new_socket(name = "Bond Energy", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			bond_energy_socket_1.default_value = 0.0
			bond_energy_socket_1.min_value = -3.4028234663852886e+38
			bond_energy_socket_1.max_value = 3.4028234663852886e+38
			bond_energy_socket_1.subtype = 'NONE'
			bond_energy_socket_1.attribute_domain = 'POINT'
			
			#Socket H->O
			h__o_socket = hbond_backbone_check.interface.new_socket(name = "H->O", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			h__o_socket.default_value = (0.0, 0.0, 0.0)
			h__o_socket.min_value = -3.4028234663852886e+38
			h__o_socket.max_value = 3.4028234663852886e+38
			h__o_socket.subtype = 'NONE'
			h__o_socket.attribute_domain = 'POINT'
			
			#Panel CO
			co_panel = hbond_backbone_check.interface.new_panel("CO")
			#Socket CO Index
			co_index_socket = hbond_backbone_check.interface.new_socket(name = "CO Index", in_out='INPUT', socket_type = 'NodeSocketInt', parent = co_panel)
			co_index_socket.default_value = 0
			co_index_socket.min_value = 0
			co_index_socket.max_value = 2147483647
			co_index_socket.subtype = 'NONE'
			co_index_socket.attribute_domain = 'POINT'
			
			#Socket CO Offset
			co_offset_socket = hbond_backbone_check.interface.new_socket(name = "CO Offset", in_out='INPUT', socket_type = 'NodeSocketInt', parent = co_panel)
			co_offset_socket.default_value = 0
			co_offset_socket.min_value = -2147483648
			co_offset_socket.max_value = 2147483647
			co_offset_socket.subtype = 'NONE'
			co_offset_socket.attribute_domain = 'POINT'
			
			
			#Panel NH
			nh_panel = hbond_backbone_check.interface.new_panel("NH")
			#Socket NH Index
			nh_index_socket = hbond_backbone_check.interface.new_socket(name = "NH Index", in_out='INPUT', socket_type = 'NodeSocketInt', parent = nh_panel)
			nh_index_socket.default_value = 0
			nh_index_socket.min_value = 0
			nh_index_socket.max_value = 2147483647
			nh_index_socket.subtype = 'NONE'
			nh_index_socket.attribute_domain = 'POINT'
			
			#Socket NH Offset
			nh_offset_socket = hbond_backbone_check.interface.new_socket(name = "NH Offset", in_out='INPUT', socket_type = 'NodeSocketInt', parent = nh_panel)
			nh_offset_socket.default_value = 0
			nh_offset_socket.min_value = -2147483648
			nh_offset_socket.max_value = 2147483647
			nh_offset_socket.subtype = 'NONE'
			nh_offset_socket.attribute_domain = 'POINT'
			
			
			
			#initialize hbond_backbone_check nodes
			#node Group Output
			group_output_8 = hbond_backbone_check.nodes.new("NodeGroupOutput")
			group_output_8.name = "Group Output"
			group_output_8.is_active_output = True
			
			#node Group Input
			group_input_8 = hbond_backbone_check.nodes.new("NodeGroupInput")
			group_input_8.name = "Group Input"
			
			#node Group.008
			group_008_1 = hbond_backbone_check.nodes.new("GeometryNodeGroup")
			group_008_1.name = "Group.008"
			group_008_1.node_tree = hbond_energy
			
			#node Group.009
			group_009_1 = hbond_backbone_check.nodes.new("GeometryNodeGroup")
			group_009_1.name = "Group.009"
			group_009_1.node_tree = mn_topo_backbone
			#Socket_3
			group_009_1.inputs[0].default_value = 0
			
			#node Evaluate at Index
			evaluate_at_index_2 = hbond_backbone_check.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_2.name = "Evaluate at Index"
			evaluate_at_index_2.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_2.domain = 'POINT'
			
			#node Evaluate at Index.001
			evaluate_at_index_001_1 = hbond_backbone_check.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001_1.name = "Evaluate at Index.001"
			evaluate_at_index_001_1.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_001_1.domain = 'POINT'
			
			#node Evaluate at Index.002
			evaluate_at_index_002_1 = hbond_backbone_check.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_002_1.name = "Evaluate at Index.002"
			evaluate_at_index_002_1.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_002_1.domain = 'POINT'
			
			#node Evaluate at Index.003
			evaluate_at_index_003_1 = hbond_backbone_check.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_003_1.name = "Evaluate at Index.003"
			evaluate_at_index_003_1.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_003_1.domain = 'POINT'
			
			#node Math
			math_4 = hbond_backbone_check.nodes.new("ShaderNodeMath")
			math_4.name = "Math"
			math_4.operation = 'ADD'
			math_4.use_clamp = False
			
			#node Math.001
			math_001_1 = hbond_backbone_check.nodes.new("ShaderNodeMath")
			math_001_1.name = "Math.001"
			math_001_1.operation = 'ADD'
			math_001_1.use_clamp = False
			
			#node Math.002
			math_002_2 = hbond_backbone_check.nodes.new("ShaderNodeMath")
			math_002_2.name = "Math.002"
			math_002_2.operation = 'SUBTRACT'
			math_002_2.use_clamp = False
			
			#node Math.003
			math_003_1 = hbond_backbone_check.nodes.new("ShaderNodeMath")
			math_003_1.name = "Math.003"
			math_003_1.operation = 'ABSOLUTE'
			math_003_1.use_clamp = False
			
			#node Compare
			compare_1 = hbond_backbone_check.nodes.new("FunctionNodeCompare")
			compare_1.name = "Compare"
			compare_1.data_type = 'FLOAT'
			compare_1.mode = 'ELEMENT'
			compare_1.operation = 'GREATER_THAN'
			
			#node Integer
			integer = hbond_backbone_check.nodes.new("FunctionNodeInputInt")
			integer.name = "Integer"
			integer.integer = 2
			
			#node Frame
			frame = hbond_backbone_check.nodes.new("NodeFrame")
			frame.label = "Check not bonded to +/- residues"
			frame.name = "Frame"
			frame.label_size = 20
			frame.shrink = True
			
			#node Switch
			switch_1 = hbond_backbone_check.nodes.new("GeometryNodeSwitch")
			switch_1.name = "Switch"
			switch_1.input_type = 'BOOLEAN'
			#False
			switch_1.inputs[1].default_value = False
			
			#node Compare.001
			compare_001 = hbond_backbone_check.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'FLOAT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'LESS_THAN'
			
			#node Vector Math
			vector_math_2 = hbond_backbone_check.nodes.new("ShaderNodeVectorMath")
			vector_math_2.name = "Vector Math"
			vector_math_2.operation = 'LENGTH'
			
			#node Group
			group_3 = hbond_backbone_check.nodes.new("GeometryNodeGroup")
			group_3.name = "Group"
			group_3.node_tree = mn_units
			#Input_1
			group_3.inputs[0].default_value = 3.0
			
			
			
			#Set parents
			math_002_2.parent = frame
			math_003_1.parent = frame
			compare_1.parent = frame
			integer.parent = frame
			
			#Set locations
			group_output_8.location = (820.0, 240.0)
			group_input_8.location = (-680.0, 140.0)
			group_008_1.location = (224.2731170654297, 240.0)
			group_009_1.location = (-480.0, 460.0)
			evaluate_at_index_2.location = (-20.0, 40.0)
			evaluate_at_index_001_1.location = (-20.0, -120.0)
			evaluate_at_index_002_1.location = (-20.0, 400.0)
			evaluate_at_index_003_1.location = (-20.0, 240.0)
			math_4.location = (-480.0, 240.0)
			math_001_1.location = (-480.0, 80.0)
			math_002_2.location = (70.0, 640.0)
			math_003_1.location = (240.0, 640.0)
			compare_1.location = (420.0, 640.0)
			integer.location = (240.0, 500.0)
			frame.location = (-70.0, 40.0)
			switch_1.location = (620.0, 340.0)
			compare_001.location = (520.0, 140.0)
			vector_math_2.location = (260.0, 20.0)
			group_3.location = (520.0, -20.0)
			
			#Set dimensions
			group_output_8.width, group_output_8.height = 140.0, 100.0
			group_input_8.width, group_input_8.height = 140.0, 100.0
			group_008_1.width, group_008_1.height = 184.92144775390625, 100.0
			group_009_1.width, group_009_1.height = 140.0, 100.0
			evaluate_at_index_2.width, evaluate_at_index_2.height = 140.0, 100.0
			evaluate_at_index_001_1.width, evaluate_at_index_001_1.height = 140.0, 100.0
			evaluate_at_index_002_1.width, evaluate_at_index_002_1.height = 140.0, 100.0
			evaluate_at_index_003_1.width, evaluate_at_index_003_1.height = 140.0, 100.0
			math_4.width, math_4.height = 140.0, 100.0
			math_001_1.width, math_001_1.height = 140.0, 100.0
			math_002_2.width, math_002_2.height = 140.0, 100.0
			math_003_1.width, math_003_1.height = 140.0, 100.0
			compare_1.width, compare_1.height = 140.0, 100.0
			integer.width, integer.height = 140.0, 100.0
			frame.width, frame.height = 550.0, 284.0
			switch_1.width, switch_1.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			vector_math_2.width, vector_math_2.height = 140.0, 100.0
			group_3.width, group_3.height = 140.0, 100.0
			
			#initialize hbond_backbone_check links
			#evaluate_at_index_001_1.Value -> group_008_1.H
			hbond_backbone_check.links.new(evaluate_at_index_001_1.outputs[0], group_008_1.inputs[3])
			#evaluate_at_index_2.Value -> group_008_1.N
			hbond_backbone_check.links.new(evaluate_at_index_2.outputs[0], group_008_1.inputs[2])
			#evaluate_at_index_002_1.Value -> group_008_1.O
			hbond_backbone_check.links.new(evaluate_at_index_002_1.outputs[0], group_008_1.inputs[0])
			#math_001_1.Value -> evaluate_at_index_001_1.Index
			hbond_backbone_check.links.new(math_001_1.outputs[0], evaluate_at_index_001_1.inputs[0])
			#math_001_1.Value -> evaluate_at_index_2.Index
			hbond_backbone_check.links.new(math_001_1.outputs[0], evaluate_at_index_2.inputs[0])
			#evaluate_at_index_003_1.Value -> group_008_1.C
			hbond_backbone_check.links.new(evaluate_at_index_003_1.outputs[0], group_008_1.inputs[1])
			#group_008_1.Bond Energy -> group_output_8.Bond Energy
			hbond_backbone_check.links.new(group_008_1.outputs[1], group_output_8.inputs[1])
			#group_008_1.Bond Vector -> group_output_8.H->O
			hbond_backbone_check.links.new(group_008_1.outputs[2], group_output_8.inputs[2])
			#math_4.Value -> evaluate_at_index_002_1.Index
			hbond_backbone_check.links.new(math_4.outputs[0], evaluate_at_index_002_1.inputs[0])
			#math_4.Value -> evaluate_at_index_003_1.Index
			hbond_backbone_check.links.new(math_4.outputs[0], evaluate_at_index_003_1.inputs[0])
			#group_input_8.CO Index -> math_4.Value
			hbond_backbone_check.links.new(group_input_8.outputs[0], math_4.inputs[0])
			#group_input_8.CO Offset -> math_4.Value
			hbond_backbone_check.links.new(group_input_8.outputs[1], math_4.inputs[1])
			#group_input_8.NH Index -> math_001_1.Value
			hbond_backbone_check.links.new(group_input_8.outputs[2], math_001_1.inputs[0])
			#group_input_8.NH Offset -> math_001_1.Value
			hbond_backbone_check.links.new(group_input_8.outputs[3], math_001_1.inputs[1])
			#math_4.Value -> math_002_2.Value
			hbond_backbone_check.links.new(math_4.outputs[0], math_002_2.inputs[0])
			#math_001_1.Value -> math_002_2.Value
			hbond_backbone_check.links.new(math_001_1.outputs[0], math_002_2.inputs[1])
			#math_002_2.Value -> math_003_1.Value
			hbond_backbone_check.links.new(math_002_2.outputs[0], math_003_1.inputs[0])
			#math_003_1.Value -> compare_1.A
			hbond_backbone_check.links.new(math_003_1.outputs[0], compare_1.inputs[0])
			#integer.Integer -> compare_1.B
			hbond_backbone_check.links.new(integer.outputs[0], compare_1.inputs[1])
			#compare_1.Result -> switch_1.Switch
			hbond_backbone_check.links.new(compare_1.outputs[0], switch_1.inputs[0])
			#group_008_1.Bond Vector -> vector_math_2.Vector
			hbond_backbone_check.links.new(group_008_1.outputs[2], vector_math_2.inputs[0])
			#vector_math_2.Value -> compare_001.A
			hbond_backbone_check.links.new(vector_math_2.outputs[1], compare_001.inputs[0])
			#group_3.Angstrom -> compare_001.B
			hbond_backbone_check.links.new(group_3.outputs[0], compare_001.inputs[1])
			#switch_1.Output -> group_output_8.Is Bonded
			hbond_backbone_check.links.new(switch_1.outputs[0], group_output_8.inputs[0])
			#group_008_1.Is Bonded -> switch_1.True
			hbond_backbone_check.links.new(group_008_1.outputs[0], switch_1.inputs[2])
			#group_009_1.O -> evaluate_at_index_002_1.Value
			hbond_backbone_check.links.new(group_009_1.outputs[0], evaluate_at_index_002_1.inputs[1])
			#group_009_1.C -> evaluate_at_index_003_1.Value
			hbond_backbone_check.links.new(group_009_1.outputs[1], evaluate_at_index_003_1.inputs[1])
			#group_009_1.N -> evaluate_at_index_2.Value
			hbond_backbone_check.links.new(group_009_1.outputs[3], evaluate_at_index_2.inputs[1])
			#group_009_1.NH -> evaluate_at_index_001_1.Value
			hbond_backbone_check.links.new(group_009_1.outputs[4], evaluate_at_index_001_1.inputs[1])
			return hbond_backbone_check

		hbond_backbone_check = hbond_backbone_check_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "HBond Backbone Check", type = 'NODES')
		mod.node_group = hbond_backbone_check
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(HBond_Backbone_Check.bl_idname)
			
def register():
	bpy.utils.register_class(HBond_Backbone_Check)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(HBond_Backbone_Check)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
