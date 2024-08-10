bl_info = {
	"name" : "Animate Fraction",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Animate_Fraction(bpy.types.Operator):
	bl_idname = "node.animate_fraction"
	bl_label = "Animate Fraction"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize animate_fraction node group
		def animate_fraction_node_group():
			animate_fraction = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Animate Fraction")

			animate_fraction.color_tag = 'CONVERTER'
			animate_fraction.description = "Interpolate the fraction component of a float"

			
			#animate_fraction interface
			#Socket Float
			float_socket = animate_fraction.interface.new_socket(name = "Float", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			float_socket.subtype = 'NONE'
			float_socket.default_value = 0.0
			float_socket.min_value = -3.4028234663852886e+38
			float_socket.max_value = 3.4028234663852886e+38
			float_socket.attribute_domain = 'POINT'
			
			#Socket Interpolate
			interpolate_socket = animate_fraction.interface.new_socket(name = "Interpolate", in_out='INPUT', socket_type = 'NodeSocketBool')
			interpolate_socket.attribute_domain = 'POINT'
			
			#Socket Smoother Step
			smoother_step_socket = animate_fraction.interface.new_socket(name = "Smoother Step", in_out='INPUT', socket_type = 'NodeSocketBool')
			smoother_step_socket.attribute_domain = 'POINT'
			
			#Socket Float
			float_socket_1 = animate_fraction.interface.new_socket(name = "Float", in_out='INPUT', socket_type = 'NodeSocketFloat')
			float_socket_1.subtype = 'NONE'
			float_socket_1.default_value = 0.0
			float_socket_1.min_value = -3.4028234663852886e+38
			float_socket_1.max_value = 3.4028234663852886e+38
			float_socket_1.attribute_domain = 'POINT'
			
			
			#initialize animate_fraction nodes
			#node Group Output
			group_output = animate_fraction.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Switch
			switch = animate_fraction.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'FLOAT'
			
			#node Group Input
			group_input = animate_fraction.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Switch.001
			switch_001 = animate_fraction.nodes.new("GeometryNodeSwitch")
			switch_001.name = "Switch.001"
			switch_001.input_type = 'FLOAT'
			
			#node Map Range
			map_range = animate_fraction.nodes.new("ShaderNodeMapRange")
			map_range.name = "Map Range"
			map_range.clamp = True
			map_range.data_type = 'FLOAT'
			map_range.interpolation_type = 'SMOOTHERSTEP'
			#From Min
			map_range.inputs[1].default_value = 0.0
			#From Max
			map_range.inputs[2].default_value = 1.0
			#To Min
			map_range.inputs[3].default_value = 0.0
			#To Max
			map_range.inputs[4].default_value = 1.0
			
			#node Math
			math = animate_fraction.nodes.new("ShaderNodeMath")
			math.name = "Math"
			math.operation = 'FLOOR'
			math.use_clamp = False
			
			#node Math.001
			math_001 = animate_fraction.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.operation = 'FRACT'
			math_001.use_clamp = False
			
			
			
			
			#Set locations
			group_output.location = (-80.0, 160.0)
			switch.location = (-460.0, -80.0)
			group_input.location = (-860.0, 120.0)
			switch_001.location = (-260.0, 160.0)
			map_range.location = (-460.0, -240.0)
			math.location = (-460.0, 80.0)
			math_001.location = (-640.0, -140.0)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			switch_001.width, switch_001.height = 140.0, 100.0
			map_range.width, map_range.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			
			#initialize animate_fraction links
			#group_input.Float -> math_001.Value
			animate_fraction.links.new(group_input.outputs[2], math_001.inputs[0])
			#math_001.Value -> map_range.Value
			animate_fraction.links.new(math_001.outputs[0], map_range.inputs[0])
			#map_range.Result -> switch.True
			animate_fraction.links.new(map_range.outputs[0], switch.inputs[2])
			#group_input.Smoother Step -> switch.Switch
			animate_fraction.links.new(group_input.outputs[1], switch.inputs[0])
			#math_001.Value -> switch.False
			animate_fraction.links.new(math_001.outputs[0], switch.inputs[1])
			#switch.Output -> switch_001.True
			animate_fraction.links.new(switch.outputs[0], switch_001.inputs[2])
			#group_input.Interpolate -> switch_001.Switch
			animate_fraction.links.new(group_input.outputs[0], switch_001.inputs[0])
			#group_input.Float -> math.Value
			animate_fraction.links.new(group_input.outputs[2], math.inputs[0])
			#math.Value -> switch_001.False
			animate_fraction.links.new(math.outputs[0], switch_001.inputs[1])
			#switch_001.Output -> group_output.Float
			animate_fraction.links.new(switch_001.outputs[0], group_output.inputs[0])
			return animate_fraction

		animate_fraction = animate_fraction_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Animate Fraction", type = 'NODES')
		mod.node_group = animate_fraction
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Animate_Fraction.bl_idname)
			
def register():
	bpy.utils.register_class(Animate_Fraction)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Animate_Fraction)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
