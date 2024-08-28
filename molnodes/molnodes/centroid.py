bl_info = {
	"name" : "Centroid",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Centroid(bpy.types.Operator):
	bl_idname = "node.centroid"
	bl_label = "Centroid"
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
			centroid_socket.default_value = (0.0, 0.0, 0.0)
			centroid_socket.min_value = -3.4028234663852886e+38
			centroid_socket.max_value = 3.4028234663852886e+38
			centroid_socket.subtype = 'NONE'
			centroid_socket.attribute_domain = 'POINT'
			centroid_socket.description = "Centroid point for the the points in the selectoin"
			
			#Socket Position
			position_socket = centroid.interface.new_socket(name = "Position", in_out='INPUT', socket_type = 'NodeSocketVector')
			position_socket.default_value = (0.0, 0.0, 0.0)
			position_socket.min_value = -3.4028234663852886e+38
			position_socket.max_value = 3.4028234663852886e+38
			position_socket.subtype = 'NONE'
			position_socket.attribute_domain = 'POINT'
			
			#Socket Selection
			selection_socket = centroid.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket.default_value = True
			selection_socket.attribute_domain = 'POINT'
			selection_socket.hide_value = True
			selection_socket.description = "Selection to use for calculating centroid value"
			
			#Socket Group ID
			group_id_socket = centroid.interface.new_socket(name = "Group ID", in_out='INPUT', socket_type = 'NodeSocketInt')
			group_id_socket.default_value = 0
			group_id_socket.min_value = -2147483648
			group_id_socket.max_value = 2147483647
			group_id_socket.subtype = 'NONE'
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

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Centroid", type = 'NODES')
		mod.node_group = centroid
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Centroid.bl_idname)
			
def register():
	bpy.utils.register_class(Centroid)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Centroid)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
