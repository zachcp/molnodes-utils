bl_info = {
	"name" : "Color Goodsell",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Color_Goodsell(bpy.types.Operator):
	bl_idname = "node.color_goodsell"
	bl_label = "Color Goodsell"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize color_goodsell node group
		def color_goodsell_node_group():
			color_goodsell = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Color Goodsell")

			color_goodsell.color_tag = 'COLOR'
			color_goodsell.description = ""

			
			#color_goodsell interface
			#Socket Color
			color_socket = color_goodsell.interface.new_socket(name = "Color", in_out='OUTPUT', socket_type = 'NodeSocketColor')
			color_socket.attribute_domain = 'POINT'
			
			#Socket Invert
			invert_socket = color_goodsell.interface.new_socket(name = "Invert", in_out='INPUT', socket_type = 'NodeSocketBool')
			invert_socket.attribute_domain = 'POINT'
			invert_socket.description = "Whether to invert the darkening of the colors"
			
			#Socket Factor
			factor_socket = color_goodsell.interface.new_socket(name = "Factor", in_out='INPUT', socket_type = 'NodeSocketFloat')
			factor_socket.subtype = 'FACTOR'
			factor_socket.default_value = 0.5
			factor_socket.min_value = 0.0
			factor_socket.max_value = 1.0
			factor_socket.attribute_domain = 'POINT'
			factor_socket.description = "Amount to apply the 'Goodsell Style' coloring to"
			
			#Socket Color
			color_socket_1 = color_goodsell.interface.new_socket(name = "Color", in_out='INPUT', socket_type = 'NodeSocketColor')
			color_socket_1.attribute_domain = 'POINT'
			color_socket_1.description = "Color to apply 'Goodsell' style colors to"
			
			
			#initialize color_goodsell nodes
			#node Group Output
			group_output = color_goodsell.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = color_goodsell.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Compare
			compare = color_goodsell.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'EQUAL'
			#B_INT
			compare.inputs[3].default_value = 6
			
			#node Named Attribute
			named_attribute = color_goodsell.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'INT'
			#Name
			named_attribute.inputs[0].default_value = "atomic_number"
			
			#node Mix
			mix = color_goodsell.nodes.new("ShaderNodeMix")
			mix.name = "Mix"
			mix.blend_type = 'MULTIPLY'
			mix.clamp_factor = False
			mix.clamp_result = False
			mix.data_type = 'RGBA'
			mix.factor_mode = 'UNIFORM'
			
			#node Mix.001
			mix_001 = color_goodsell.nodes.new("ShaderNodeMix")
			mix_001.name = "Mix.001"
			mix_001.blend_type = 'MULTIPLY'
			mix_001.clamp_factor = False
			mix_001.clamp_result = False
			mix_001.data_type = 'RGBA'
			mix_001.factor_mode = 'UNIFORM'
			
			#node Switch
			switch = color_goodsell.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'FLOAT'
			#False
			switch.inputs[1].default_value = 0.0
			
			#node Boolean Math
			boolean_math = color_goodsell.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'NOT'
			
			#node Switch.001
			switch_001 = color_goodsell.nodes.new("GeometryNodeSwitch")
			switch_001.name = "Switch.001"
			switch_001.input_type = 'BOOLEAN'
			
			
			
			
			#Set locations
			group_output.location = (440.0, -0.0)
			group_input.location = (-409.4183044433594, -118.92835998535156)
			compare.location = (-440.0, 100.0)
			named_attribute.location = (-600.0, 100.0)
			mix.location = (0.0, 0.0)
			mix_001.location = (160.0, 0.0)
			switch.location = (-196.15087890625, 16.81116485595703)
			boolean_math.location = (-440.0, 220.0)
			switch_001.location = (-213.6559295654297, 230.88919067382812)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			mix.width, mix.height = 140.0, 100.0
			mix_001.width, mix_001.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			switch_001.width, switch_001.height = 140.0, 100.0
			
			#initialize color_goodsell links
			#group_input.Color -> mix.A
			color_goodsell.links.new(group_input.outputs[2], mix.inputs[6])
			#mix_001.Result -> group_output.Color
			color_goodsell.links.new(mix_001.outputs[2], group_output.inputs[0])
			#group_input.Color -> mix.B
			color_goodsell.links.new(group_input.outputs[2], mix.inputs[7])
			#group_input.Factor -> switch.True
			color_goodsell.links.new(group_input.outputs[1], switch.inputs[2])
			#named_attribute.Attribute -> compare.A
			color_goodsell.links.new(named_attribute.outputs[0], compare.inputs[2])
			#switch.Output -> mix.Factor
			color_goodsell.links.new(switch.outputs[0], mix.inputs[0])
			#mix.Result -> mix_001.A
			color_goodsell.links.new(mix.outputs[2], mix_001.inputs[6])
			#mix.Result -> mix_001.B
			color_goodsell.links.new(mix.outputs[2], mix_001.inputs[7])
			#switch.Output -> mix_001.Factor
			color_goodsell.links.new(switch.outputs[0], mix_001.inputs[0])
			#compare.Result -> boolean_math.Boolean
			color_goodsell.links.new(compare.outputs[0], boolean_math.inputs[0])
			#switch_001.Output -> switch.Switch
			color_goodsell.links.new(switch_001.outputs[0], switch.inputs[0])
			#group_input.Invert -> switch_001.Switch
			color_goodsell.links.new(group_input.outputs[0], switch_001.inputs[0])
			#boolean_math.Boolean -> switch_001.False
			color_goodsell.links.new(boolean_math.outputs[0], switch_001.inputs[1])
			#compare.Result -> switch_001.True
			color_goodsell.links.new(compare.outputs[0], switch_001.inputs[2])
			return color_goodsell

		color_goodsell = color_goodsell_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Color Goodsell", type = 'NODES')
		mod.node_group = color_goodsell
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Color_Goodsell.bl_idname)
			
def register():
	bpy.utils.register_class(Color_Goodsell)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Color_Goodsell)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
