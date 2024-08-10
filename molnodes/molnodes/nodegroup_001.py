bl_info = {
	"name" : "NodeGroup.001",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class NodeGroup_001(bpy.types.Operator):
	bl_idname = "node.nodegroup_001"
	bl_label = "NodeGroup.001"
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

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "NodeGroup.001", type = 'NODES')
		mod.node_group = nodegroup_001
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(NodeGroup_001.bl_idname)
			
def register():
	bpy.utils.register_class(NodeGroup_001)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(NodeGroup_001)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
