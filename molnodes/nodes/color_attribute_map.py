bl_info = {
	"name" : "Color Attribute Map",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Color_Attribute_Map(bpy.types.Operator):
	bl_idname = "node.color_attribute_map"
	bl_label = "Color Attribute Map"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize color_attribute_map node group
		def color_attribute_map_node_group():
			color_attribute_map = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Color Attribute Map")

			color_attribute_map.color_tag = 'COLOR'
			color_attribute_map.description = ""

			
			#color_attribute_map interface
			#Socket Color
			color_socket = color_attribute_map.interface.new_socket(name = "Color", in_out='OUTPUT', socket_type = 'NodeSocketColor')
			color_socket.attribute_domain = 'POINT'
			color_socket.description = "The mapped color value based on the attribute."
			
			#Panel Attribute
			attribute_panel = color_attribute_map.interface.new_panel("Attribute")
			#Socket Attribute Name
			attribute_name_socket = color_attribute_map.interface.new_socket(name = "Attribute Name", in_out='INPUT', socket_type = 'NodeSocketString', parent = attribute_panel)
			attribute_name_socket.attribute_domain = 'POINT'
			attribute_name_socket.description = "Name of the attribute to map colors to"
			
			#Socket Attribute Min
			attribute_min_socket = color_attribute_map.interface.new_socket(name = "Attribute Min", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = attribute_panel)
			attribute_min_socket.subtype = 'NONE'
			attribute_min_socket.default_value = 0.0
			attribute_min_socket.min_value = -10000.0
			attribute_min_socket.max_value = 10000.0
			attribute_min_socket.attribute_domain = 'POINT'
			attribute_min_socket.description = "Value for the attribute to be the minimum color"
			
			#Socket Attribute Max
			attribute_max_socket = color_attribute_map.interface.new_socket(name = "Attribute Max", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = attribute_panel)
			attribute_max_socket.subtype = 'NONE'
			attribute_max_socket.default_value = 150.0
			attribute_max_socket.min_value = -10000.0
			attribute_max_socket.max_value = 10000.0
			attribute_max_socket.attribute_domain = 'POINT'
			attribute_max_socket.description = "Value for the attribute to be the maxium color"
			
			
			#Panel Color
			color_panel = color_attribute_map.interface.new_panel("Color")
			#Socket Color Use Mid
			color_use_mid_socket = color_attribute_map.interface.new_socket(name = "Color Use Mid", in_out='INPUT', socket_type = 'NodeSocketBool', parent = color_panel)
			color_use_mid_socket.attribute_domain = 'POINT'
			color_use_mid_socket.description = "Wheter to interpolate through the 'Mid' color."
			
			#Socket Color Min
			color_min_socket = color_attribute_map.interface.new_socket(name = "Color Min", in_out='INPUT', socket_type = 'NodeSocketColor', parent = color_panel)
			color_min_socket.attribute_domain = 'POINT'
			color_min_socket.description = "Color mapped to the minimum value of the attribute"
			
			#Socket Color Mid
			color_mid_socket = color_attribute_map.interface.new_socket(name = "Color Mid", in_out='INPUT', socket_type = 'NodeSocketColor', parent = color_panel)
			color_mid_socket.attribute_domain = 'POINT'
			color_mid_socket.description = "Color mapped to the middle value of the attribute"
			
			#Socket Color Max
			color_max_socket = color_attribute_map.interface.new_socket(name = "Color Max", in_out='INPUT', socket_type = 'NodeSocketColor', parent = color_panel)
			color_max_socket.attribute_domain = 'POINT'
			color_max_socket.description = "Color mapped t othe maximum value of the attribute"
			
			
			
			#initialize color_attribute_map nodes
			#node Named Attribute.001
			named_attribute_001 = color_attribute_map.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.data_type = 'FLOAT'
			
			#node Map Range
			map_range = color_attribute_map.nodes.new("ShaderNodeMapRange")
			map_range.name = "Map Range"
			map_range.clamp = True
			map_range.data_type = 'FLOAT'
			map_range.interpolation_type = 'LINEAR'
			#To Min
			map_range.inputs[3].default_value = 0.0
			#To Max
			map_range.inputs[4].default_value = 1.0
			
			#node Group Output
			group_output = color_attribute_map.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Switch
			switch = color_attribute_map.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'RGBA'
			
			#node Group Input
			group_input = color_attribute_map.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Mix.001
			mix_001 = color_attribute_map.nodes.new("ShaderNodeMix")
			mix_001.name = "Mix.001"
			mix_001.blend_type = 'MIX'
			mix_001.clamp_factor = True
			mix_001.clamp_result = False
			mix_001.data_type = 'RGBA'
			mix_001.factor_mode = 'UNIFORM'
			
			#node Mix
			mix = color_attribute_map.nodes.new("ShaderNodeMix")
			mix.name = "Mix"
			mix.blend_type = 'MIX'
			mix.clamp_factor = True
			mix.clamp_result = False
			mix.data_type = 'RGBA'
			mix.factor_mode = 'UNIFORM'
			
			#node Mix.002
			mix_002 = color_attribute_map.nodes.new("ShaderNodeMix")
			mix_002.name = "Mix.002"
			mix_002.blend_type = 'MIX'
			mix_002.clamp_factor = True
			mix_002.clamp_result = False
			mix_002.data_type = 'RGBA'
			mix_002.factor_mode = 'UNIFORM'
			
			#node Mix.003
			mix_003 = color_attribute_map.nodes.new("ShaderNodeMix")
			mix_003.name = "Mix.003"
			mix_003.blend_type = 'MIX'
			mix_003.clamp_factor = True
			mix_003.clamp_result = False
			mix_003.data_type = 'RGBA'
			mix_003.factor_mode = 'UNIFORM'
			
			
			
			
			#Set locations
			named_attribute_001.location = (-271.3536376953125, 110.04327392578125)
			map_range.location = (-111.3536376953125, 110.04327392578125)
			group_output.location = (743.28857421875, 6.896442890167236)
			switch.location = (480.0, 60.0)
			group_input.location = (-440.0, -60.0)
			mix_001.location = (100.0, -120.0)
			mix.location = (100.0, 120.0)
			mix_002.location = (260.0, 120.0)
			mix_003.location = (260.0, -120.0)
			
			#Set dimensions
			named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
			map_range.width, map_range.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			mix_001.width, mix_001.height = 140.0, 100.0
			mix.width, mix.height = 140.0, 100.0
			mix_002.width, mix_002.height = 140.0, 100.0
			mix_003.width, mix_003.height = 140.0, 100.0
			
			#initialize color_attribute_map links
			#map_range.Result -> mix_001.Factor
			color_attribute_map.links.new(map_range.outputs[0], mix_001.inputs[0])
			#named_attribute_001.Attribute -> map_range.Value
			color_attribute_map.links.new(named_attribute_001.outputs[0], map_range.inputs[0])
			#mix.Result -> mix_002.A
			color_attribute_map.links.new(mix.outputs[2], mix_002.inputs[6])
			#mix_001.Result -> mix_002.B
			color_attribute_map.links.new(mix_001.outputs[2], mix_002.inputs[7])
			#map_range.Result -> mix_002.Factor
			color_attribute_map.links.new(map_range.outputs[0], mix_002.inputs[0])
			#map_range.Result -> mix.Factor
			color_attribute_map.links.new(map_range.outputs[0], mix.inputs[0])
			#group_input.Color Min -> mix.A
			color_attribute_map.links.new(group_input.outputs[4], mix.inputs[6])
			#group_input.Color Mid -> mix.B
			color_attribute_map.links.new(group_input.outputs[5], mix.inputs[7])
			#group_input.Color Max -> mix_001.B
			color_attribute_map.links.new(group_input.outputs[6], mix_001.inputs[7])
			#group_input.Attribute Min -> map_range.From Min
			color_attribute_map.links.new(group_input.outputs[1], map_range.inputs[1])
			#group_input.Attribute Max -> map_range.From Max
			color_attribute_map.links.new(group_input.outputs[2], map_range.inputs[2])
			#group_input.Color Mid -> mix_001.A
			color_attribute_map.links.new(group_input.outputs[5], mix_001.inputs[6])
			#group_input.Attribute Name -> named_attribute_001.Name
			color_attribute_map.links.new(group_input.outputs[0], named_attribute_001.inputs[0])
			#map_range.Result -> mix_003.Factor
			color_attribute_map.links.new(map_range.outputs[0], mix_003.inputs[0])
			#mix_002.Result -> switch.True
			color_attribute_map.links.new(mix_002.outputs[2], switch.inputs[2])
			#mix_003.Result -> switch.False
			color_attribute_map.links.new(mix_003.outputs[2], switch.inputs[1])
			#switch.Output -> group_output.Color
			color_attribute_map.links.new(switch.outputs[0], group_output.inputs[0])
			#group_input.Color Use Mid -> switch.Switch
			color_attribute_map.links.new(group_input.outputs[3], switch.inputs[0])
			#group_input.Color Min -> mix_003.A
			color_attribute_map.links.new(group_input.outputs[4], mix_003.inputs[6])
			#group_input.Color Max -> mix_003.B
			color_attribute_map.links.new(group_input.outputs[6], mix_003.inputs[7])
			return color_attribute_map

		color_attribute_map = color_attribute_map_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Color Attribute Map", type = 'NODES')
		mod.node_group = color_attribute_map
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Color_Attribute_Map.bl_idname)
			
def register():
	bpy.utils.register_class(Color_Attribute_Map)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Color_Attribute_Map)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
