bl_info = {
	"name" : "Color Attribute Random",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Color_Attribute_Random(bpy.types.Operator):
	bl_idname = "node.color_attribute_random"
	bl_label = "Color Attribute Random"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize color_attribute_random node group
		def color_attribute_random_node_group():
			color_attribute_random = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Color Attribute Random")

			color_attribute_random.color_tag = 'COLOR'
			color_attribute_random.description = ""

			
			#color_attribute_random interface
			#Socket Color
			color_socket = color_attribute_random.interface.new_socket(name = "Color", in_out='OUTPUT', socket_type = 'NodeSocketColor')
			color_socket.attribute_domain = 'POINT'
			color_socket.description = "The randomly generated color based on the input attribute"
			
			#Socket Name
			name_socket = color_attribute_random.interface.new_socket(name = "Name", in_out='INPUT', socket_type = 'NodeSocketString')
			name_socket.attribute_domain = 'POINT'
			name_socket.description = "Attribute to base the random color generation on "
			
			#Panel Color
			color_panel = color_attribute_random.interface.new_panel("Color", default_closed=True)
			#Socket Color Saturation
			color_saturation_socket = color_attribute_random.interface.new_socket(name = "Color Saturation", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = color_panel)
			color_saturation_socket.subtype = 'FACTOR'
			color_saturation_socket.default_value = 0.6000000238418579
			color_saturation_socket.min_value = 0.0
			color_saturation_socket.max_value = 1.0
			color_saturation_socket.attribute_domain = 'POINT'
			color_saturation_socket.description = "Saturlation level for the random color"
			
			#Socket Color Lightness
			color_lightness_socket = color_attribute_random.interface.new_socket(name = "Color Lightness", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = color_panel)
			color_lightness_socket.subtype = 'FACTOR'
			color_lightness_socket.default_value = 0.6000000238418579
			color_lightness_socket.min_value = 0.0
			color_lightness_socket.max_value = 1.0
			color_lightness_socket.attribute_domain = 'POINT'
			color_lightness_socket.description = "Lightness value for the generated random color"
			
			#Socket Color Seed
			color_seed_socket = color_attribute_random.interface.new_socket(name = "Color Seed", in_out='INPUT', socket_type = 'NodeSocketInt', parent = color_panel)
			color_seed_socket.subtype = 'NONE'
			color_seed_socket.default_value = 0
			color_seed_socket.min_value = -10000
			color_seed_socket.max_value = 10000
			color_seed_socket.attribute_domain = 'POINT'
			color_seed_socket.description = "Seed value for the random generation of the colors"
			
			
			
			#initialize color_attribute_random nodes
			#node Group Output
			group_output = color_attribute_random.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Combine Color
			combine_color = color_attribute_random.nodes.new("FunctionNodeCombineColor")
			combine_color.name = "Combine Color"
			combine_color.mode = 'HSL'
			#Alpha
			combine_color.inputs[3].default_value = 1.0
			
			#node Named Attribute
			named_attribute = color_attribute_random.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'INT'
			
			#node Random Value
			random_value = color_attribute_random.nodes.new("FunctionNodeRandomValue")
			random_value.name = "Random Value"
			random_value.data_type = 'FLOAT'
			#Min_001
			random_value.inputs[2].default_value = 0.0
			#Max_001
			random_value.inputs[3].default_value = 1.0
			
			#node Group Input
			group_input = color_attribute_random.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Math
			math = color_attribute_random.nodes.new("ShaderNodeMath")
			math.name = "Math"
			math.operation = 'ADD'
			math.use_clamp = False
			
			#node Integer
			integer = color_attribute_random.nodes.new("FunctionNodeInputInt")
			integer.name = "Integer"
			integer.integer = 6
			
			
			
			
			#Set locations
			group_output.location = (272.6910400390625, 0.0)
			combine_color.location = (100.0, 0.0)
			named_attribute.location = (-220.0, 0.0)
			random_value.location = (-60.0, 0.0)
			group_input.location = (-400.0, -80.0)
			math.location = (-220.0, -180.0)
			integer.location = (-400.0, -280.0)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			combine_color.width, combine_color.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			random_value.width, random_value.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			integer.width, integer.height = 140.0, 100.0
			
			#initialize color_attribute_random links
			#random_value.Value -> combine_color.Red
			color_attribute_random.links.new(random_value.outputs[1], combine_color.inputs[0])
			#named_attribute.Attribute -> random_value.ID
			color_attribute_random.links.new(named_attribute.outputs[0], random_value.inputs[7])
			#group_input.Name -> named_attribute.Name
			color_attribute_random.links.new(group_input.outputs[0], named_attribute.inputs[0])
			#combine_color.Color -> group_output.Color
			color_attribute_random.links.new(combine_color.outputs[0], group_output.inputs[0])
			#group_input.Color Saturation -> combine_color.Green
			color_attribute_random.links.new(group_input.outputs[1], combine_color.inputs[1])
			#group_input.Color Lightness -> combine_color.Blue
			color_attribute_random.links.new(group_input.outputs[2], combine_color.inputs[2])
			#group_input.Color Seed -> math.Value
			color_attribute_random.links.new(group_input.outputs[3], math.inputs[0])
			#math.Value -> random_value.Seed
			color_attribute_random.links.new(math.outputs[0], random_value.inputs[8])
			#integer.Integer -> math.Value
			color_attribute_random.links.new(integer.outputs[0], math.inputs[1])
			return color_attribute_random

		color_attribute_random = color_attribute_random_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Color Attribute Random", type = 'NODES')
		mod.node_group = color_attribute_random
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Color_Attribute_Random.bl_idname)
			
def register():
	bpy.utils.register_class(Color_Attribute_Random)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Color_Attribute_Random)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
