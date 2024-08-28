bl_info = {
	"name" : "Fallback Vector",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Fallback_Vector(bpy.types.Operator):
	bl_idname = "node.fallback_vector"
	bl_label = "Fallback Vector"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
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
			group_output = fallback_vector.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = fallback_vector.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Named Attribute.001
			named_attribute_001 = fallback_vector.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.data_type = 'FLOAT_VECTOR'
			
			#node Switch
			switch = fallback_vector.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'VECTOR'
			
			
			
			
			#Set locations
			group_output.location = (260.0, 140.0)
			group_input.location = (-320.0, 80.0)
			named_attribute_001.location = (-134.38072204589844, 30.303295135498047)
			switch.location = (100.0, 140.0)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			named_attribute_001.width, named_attribute_001.height = 147.09487915039062, 100.0
			switch.width, switch.height = 140.0, 100.0
			
			#initialize fallback_vector links
			#named_attribute_001.Attribute -> switch.True
			fallback_vector.links.new(named_attribute_001.outputs[0], switch.inputs[2])
			#named_attribute_001.Exists -> switch.Switch
			fallback_vector.links.new(named_attribute_001.outputs[1], switch.inputs[0])
			#group_input.Fallback -> switch.False
			fallback_vector.links.new(group_input.outputs[1], switch.inputs[1])
			#switch.Output -> group_output.Output
			fallback_vector.links.new(switch.outputs[0], group_output.inputs[0])
			#group_input.Name -> named_attribute_001.Name
			fallback_vector.links.new(group_input.outputs[0], named_attribute_001.inputs[0])
			return fallback_vector

		fallback_vector = fallback_vector_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Fallback Vector", type = 'NODES')
		mod.node_group = fallback_vector
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Fallback_Vector.bl_idname)
			
def register():
	bpy.utils.register_class(Fallback_Vector)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Fallback_Vector)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
