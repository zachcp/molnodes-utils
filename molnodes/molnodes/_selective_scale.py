bl_info = {
	"name" : ".selective_scale",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _selective_scale(bpy.types.Operator):
	bl_idname = "node._selective_scale"
	bl_label = ".selective_scale"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _selective_scale node group
		def _selective_scale_node_group():
			_selective_scale = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".selective_scale")

			_selective_scale.color_tag = 'NONE'
			_selective_scale.description = ""

			
			#_selective_scale interface
			#Socket Output
			output_socket = _selective_scale.interface.new_socket(name = "Output", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			output_socket.subtype = 'NONE'
			output_socket.default_value = 0.0
			output_socket.min_value = -3.4028234663852886e+38
			output_socket.max_value = 3.4028234663852886e+38
			output_socket.attribute_domain = 'POINT'
			
			#Socket Switch
			switch_socket = _selective_scale.interface.new_socket(name = "Switch", in_out='INPUT', socket_type = 'NodeSocketBool')
			switch_socket.attribute_domain = 'POINT'
			
			#Socket Input
			input_socket = _selective_scale.interface.new_socket(name = "Input", in_out='INPUT', socket_type = 'NodeSocketFloat')
			input_socket.subtype = 'NONE'
			input_socket.default_value = 0.0
			input_socket.min_value = -3.4028234663852886e+38
			input_socket.max_value = 3.4028234663852886e+38
			input_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket = _selective_scale.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket.subtype = 'NONE'
			value_socket.default_value = 0.800000011920929
			value_socket.min_value = -10000.0
			value_socket.max_value = 10000.0
			value_socket.attribute_domain = 'POINT'
			
			
			#initialize _selective_scale nodes
			#node Group Output
			group_output = _selective_scale.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = _selective_scale.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Switch.005
			switch_005 = _selective_scale.nodes.new("GeometryNodeSwitch")
			switch_005.name = "Switch.005"
			switch_005.input_type = 'FLOAT'
			
			#node Math
			math = _selective_scale.nodes.new("ShaderNodeMath")
			math.name = "Math"
			math.operation = 'MULTIPLY'
			math.use_clamp = False
			
			#node Reroute.010
			reroute_010 = _selective_scale.nodes.new("NodeReroute")
			reroute_010.name = "Reroute.010"
			
			
			
			#Set locations
			group_output.location = (200.0, 0.0)
			group_input.location = (-210.0, 0.0)
			switch_005.location = (10.0, 90.0)
			math.location = (10.0, -70.0)
			reroute_010.location = (-10.0, -90.0)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			switch_005.width, switch_005.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			reroute_010.width, reroute_010.height = 16.0, 100.0
			
			#initialize _selective_scale links
			#math.Value -> switch_005.True
			_selective_scale.links.new(math.outputs[0], switch_005.inputs[2])
			#reroute_010.Output -> switch_005.False
			_selective_scale.links.new(reroute_010.outputs[0], switch_005.inputs[1])
			#reroute_010.Output -> math.Value
			_selective_scale.links.new(reroute_010.outputs[0], math.inputs[0])
			#group_input.Switch -> switch_005.Switch
			_selective_scale.links.new(group_input.outputs[0], switch_005.inputs[0])
			#group_input.Input -> reroute_010.Input
			_selective_scale.links.new(group_input.outputs[1], reroute_010.inputs[0])
			#switch_005.Output -> group_output.Output
			_selective_scale.links.new(switch_005.outputs[0], group_output.inputs[0])
			#group_input.Value -> math.Value
			_selective_scale.links.new(group_input.outputs[2], math.inputs[1])
			return _selective_scale

		_selective_scale = _selective_scale_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".selective_scale", type = 'NODES')
		mod.node_group = _selective_scale
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_selective_scale.bl_idname)
			
def register():
	bpy.utils.register_class(_selective_scale)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_selective_scale)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
