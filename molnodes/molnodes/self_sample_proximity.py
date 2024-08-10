bl_info = {
	"name" : "Self Sample Proximity",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Self_Sample_Proximity(bpy.types.Operator):
	bl_idname = "node.self_sample_proximity"
	bl_label = "Self Sample Proximity"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize self_sample_proximity node group
		def self_sample_proximity_node_group():
			self_sample_proximity = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Self Sample Proximity")

			self_sample_proximity.color_tag = 'NONE'
			self_sample_proximity.description = ""

			
			#self_sample_proximity interface
			#Socket Closest Index
			closest_index_socket = self_sample_proximity.interface.new_socket(name = "Closest Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			closest_index_socket.subtype = 'NONE'
			closest_index_socket.default_value = 0
			closest_index_socket.min_value = -2147483648
			closest_index_socket.max_value = 2147483647
			closest_index_socket.attribute_domain = 'POINT'
			
			#Socket Input
			input_socket = self_sample_proximity.interface.new_socket(name = "Input", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			input_socket.attribute_domain = 'POINT'
			
			#Socket Target Position
			target_position_socket = self_sample_proximity.interface.new_socket(name = "Target Position", in_out='INPUT', socket_type = 'NodeSocketVector')
			target_position_socket.subtype = 'NONE'
			target_position_socket.default_value = (0.0, 0.0, 0.0)
			target_position_socket.min_value = -3.4028234663852886e+38
			target_position_socket.max_value = 3.4028234663852886e+38
			target_position_socket.attribute_domain = 'POINT'
			
			#Socket Self Position
			self_position_socket = self_sample_proximity.interface.new_socket(name = "Self Position", in_out='INPUT', socket_type = 'NodeSocketVector')
			self_position_socket.subtype = 'NONE'
			self_position_socket.default_value = (0.0, 0.0, 0.0)
			self_position_socket.min_value = -3.4028234663852886e+38
			self_position_socket.max_value = 3.4028234663852886e+38
			self_position_socket.attribute_domain = 'POINT'
			
			
			#initialize self_sample_proximity nodes
			#node Group Output
			group_output = self_sample_proximity.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = self_sample_proximity.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Set Position.002
			set_position_002 = self_sample_proximity.nodes.new("GeometryNodeSetPosition")
			set_position_002.name = "Set Position.002"
			#Selection
			set_position_002.inputs[1].default_value = True
			#Offset
			set_position_002.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Sample Nearest.001
			sample_nearest_001 = self_sample_proximity.nodes.new("GeometryNodeSampleNearest")
			sample_nearest_001.name = "Sample Nearest.001"
			sample_nearest_001.domain = 'POINT'
			
			
			
			
			#Set locations
			group_output.location = (4.068901062011719, 95.01506042480469)
			group_input.location = (-640.0, 20.0)
			set_position_002.location = (-380.0, -20.0)
			sample_nearest_001.location = (-220.0, -20.0)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			set_position_002.width, set_position_002.height = 140.0, 100.0
			sample_nearest_001.width, sample_nearest_001.height = 140.0, 100.0
			
			#initialize self_sample_proximity links
			#group_input.Input -> set_position_002.Geometry
			self_sample_proximity.links.new(group_input.outputs[0], set_position_002.inputs[0])
			#set_position_002.Geometry -> sample_nearest_001.Geometry
			self_sample_proximity.links.new(set_position_002.outputs[0], sample_nearest_001.inputs[0])
			#group_input.Target Position -> set_position_002.Position
			self_sample_proximity.links.new(group_input.outputs[1], set_position_002.inputs[2])
			#group_input.Self Position -> sample_nearest_001.Sample Position
			self_sample_proximity.links.new(group_input.outputs[2], sample_nearest_001.inputs[1])
			#sample_nearest_001.Index -> group_output.Closest Index
			self_sample_proximity.links.new(sample_nearest_001.outputs[0], group_output.inputs[0])
			return self_sample_proximity

		self_sample_proximity = self_sample_proximity_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Self Sample Proximity", type = 'NODES')
		mod.node_group = self_sample_proximity
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Self_Sample_Proximity.bl_idname)
			
def register():
	bpy.utils.register_class(Self_Sample_Proximity)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Self_Sample_Proximity)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
