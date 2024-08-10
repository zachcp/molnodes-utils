bl_info = {
	"name" : "HBond Energy",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class HBond_Energy(bpy.types.Operator):
	bl_idname = "node.hbond_energy"
	bl_label = "HBond Energy"
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
			world_scale_socket.subtype = 'NONE'
			world_scale_socket.default_value = 0.009999999776482582
			world_scale_socket.min_value = -3.4028234663852886e+38
			world_scale_socket.max_value = 3.4028234663852886e+38
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
			angstrom_socket.subtype = 'NONE'
			angstrom_socket.default_value = 0.0
			angstrom_socket.min_value = -3.4028234663852886e+38
			angstrom_socket.max_value = 3.4028234663852886e+38
			angstrom_socket.attribute_domain = 'POINT'
			
			#Socket World
			world_socket = world_to_angstrom.interface.new_socket(name = "World", in_out='INPUT', socket_type = 'NodeSocketFloat')
			world_socket.subtype = 'NONE'
			world_socket.default_value = 0.5
			world_socket.min_value = -10000.0
			world_socket.max_value = 10000.0
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
			value_socket.subtype = 'NONE'
			value_socket.default_value = 0.0
			value_socket.min_value = -3.4028234663852886e+38
			value_socket.max_value = 3.4028234663852886e+38
			value_socket.attribute_domain = 'POINT'
			
			#Socket Vector
			vector_socket = nodegroup_001.interface.new_socket(name = "Vector", in_out='INPUT', socket_type = 'NodeSocketVector')
			vector_socket.subtype = 'NONE'
			vector_socket.default_value = (0.0, 0.0, 0.0)
			vector_socket.min_value = -10000.0
			vector_socket.max_value = 10000.0
			vector_socket.attribute_domain = 'POINT'
			
			#Socket Vector
			vector_socket_1 = nodegroup_001.interface.new_socket(name = "Vector", in_out='INPUT', socket_type = 'NodeSocketVector')
			vector_socket_1.subtype = 'NONE'
			vector_socket_1.default_value = (0.0, 0.0, 0.0)
			vector_socket_1.min_value = -10000.0
			vector_socket_1.max_value = 10000.0
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
			is_bonded_socket.attribute_domain = 'POINT'
			
			#Socket Bond Energy
			bond_energy_socket = hbond_energy.interface.new_socket(name = "Bond Energy", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			bond_energy_socket.subtype = 'NONE'
			bond_energy_socket.default_value = 0.0
			bond_energy_socket.min_value = -3.4028234663852886e+38
			bond_energy_socket.max_value = 3.4028234663852886e+38
			bond_energy_socket.attribute_domain = 'POINT'
			
			#Socket Bond Vector
			bond_vector_socket = hbond_energy.interface.new_socket(name = "Bond Vector", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			bond_vector_socket.subtype = 'NONE'
			bond_vector_socket.default_value = (0.0, 0.0, 0.0)
			bond_vector_socket.min_value = -3.4028234663852886e+38
			bond_vector_socket.max_value = 3.4028234663852886e+38
			bond_vector_socket.attribute_domain = 'POINT'
			
			#Socket O
			o_socket = hbond_energy.interface.new_socket(name = "O", in_out='INPUT', socket_type = 'NodeSocketVector')
			o_socket.subtype = 'NONE'
			o_socket.default_value = (0.0, 0.0, 0.0)
			o_socket.min_value = -3.4028234663852886e+38
			o_socket.max_value = 3.4028234663852886e+38
			o_socket.attribute_domain = 'POINT'
			
			#Socket C
			c_socket = hbond_energy.interface.new_socket(name = "C", in_out='INPUT', socket_type = 'NodeSocketVector')
			c_socket.subtype = 'NONE'
			c_socket.default_value = (0.0, 0.0, 0.0)
			c_socket.min_value = -3.4028234663852886e+38
			c_socket.max_value = 3.4028234663852886e+38
			c_socket.attribute_domain = 'POINT'
			
			#Socket N
			n_socket = hbond_energy.interface.new_socket(name = "N", in_out='INPUT', socket_type = 'NodeSocketVector')
			n_socket.subtype = 'NONE'
			n_socket.default_value = (0.0, 0.0, 0.0)
			n_socket.min_value = -3.4028234663852886e+38
			n_socket.max_value = 3.4028234663852886e+38
			n_socket.attribute_domain = 'POINT'
			
			#Socket H
			h_socket = hbond_energy.interface.new_socket(name = "H", in_out='INPUT', socket_type = 'NodeSocketVector')
			h_socket.subtype = 'NONE'
			h_socket.default_value = (0.0, 0.0, 0.0)
			h_socket.min_value = -3.4028234663852886e+38
			h_socket.max_value = 3.4028234663852886e+38
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

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "HBond Energy", type = 'NODES')
		mod.node_group = hbond_energy
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(HBond_Energy.bl_idname)
			
def register():
	bpy.utils.register_class(HBond_Energy)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(HBond_Energy)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
