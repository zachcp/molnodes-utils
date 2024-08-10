bl_info = {
	"name" : "Attribute Map",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Attribute_Map(bpy.types.Operator):
	bl_idname = "node.attribute_map"
	bl_label = "Attribute Map"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize attribute_map node group
		def attribute_map_node_group():
			attribute_map = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Attribute Map")

			attribute_map.color_tag = 'CONVERTER'
			attribute_map.description = "Maps the range of values of the attribute on from the target atoms, to the range from min to max"

			
			#attribute_map interface
			#Socket Value
			value_socket = attribute_map.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			value_socket.subtype = 'NONE'
			value_socket.default_value = 0.0
			value_socket.min_value = -3.4028234663852886e+38
			value_socket.max_value = 3.4028234663852886e+38
			value_socket.attribute_domain = 'POINT'
			
			#Socket Sample Atoms
			sample_atoms_socket = attribute_map.interface.new_socket(name = "Sample Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			sample_atoms_socket.attribute_domain = 'POINT'
			
			#Socket Attribute
			attribute_socket = attribute_map.interface.new_socket(name = "Attribute", in_out='INPUT', socket_type = 'NodeSocketString')
			attribute_socket.attribute_domain = 'POINT'
			
			#Socket Value Min
			value_min_socket = attribute_map.interface.new_socket(name = "Value Min", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_min_socket.subtype = 'NONE'
			value_min_socket.default_value = 0.20000000298023224
			value_min_socket.min_value = -10000.0
			value_min_socket.max_value = 10000.0
			value_min_socket.attribute_domain = 'POINT'
			
			#Socket Value Max
			value_max_socket = attribute_map.interface.new_socket(name = "Value Max", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_max_socket.subtype = 'NONE'
			value_max_socket.default_value = 3.0
			value_max_socket.min_value = -10000.0
			value_max_socket.max_value = 10000.0
			value_max_socket.attribute_domain = 'POINT'
			
			
			#initialize attribute_map nodes
			#node Group Output
			group_output = attribute_map.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = attribute_map.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Map Range
			map_range = attribute_map.nodes.new("ShaderNodeMapRange")
			map_range.name = "Map Range"
			map_range.clamp = True
			map_range.data_type = 'FLOAT'
			map_range.interpolation_type = 'LINEAR'
			
			#node Named Attribute.004
			named_attribute_004 = attribute_map.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_004.name = "Named Attribute.004"
			named_attribute_004.data_type = 'FLOAT'
			
			#node Attribute Statistic
			attribute_statistic = attribute_map.nodes.new("GeometryNodeAttributeStatistic")
			attribute_statistic.name = "Attribute Statistic"
			attribute_statistic.data_type = 'FLOAT'
			attribute_statistic.domain = 'POINT'
			attribute_statistic.inputs[1].hide = True
			attribute_statistic.outputs[0].hide = True
			attribute_statistic.outputs[1].hide = True
			attribute_statistic.outputs[2].hide = True
			attribute_statistic.outputs[5].hide = True
			attribute_statistic.outputs[6].hide = True
			attribute_statistic.outputs[7].hide = True
			#Selection
			attribute_statistic.inputs[1].default_value = True
			
			
			
			
			#Set locations
			group_output.location = (270.0, 0.0)
			group_input.location = (-280.0, 0.0)
			map_range.location = (80.0, 70.0)
			named_attribute_004.location = (-80.0, 70.0)
			attribute_statistic.location = (-80.0, -70.0)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			map_range.width, map_range.height = 140.0, 100.0
			named_attribute_004.width, named_attribute_004.height = 140.0, 100.0
			attribute_statistic.width, attribute_statistic.height = 140.0, 100.0
			
			#initialize attribute_map links
			#attribute_statistic.Max -> map_range.From Max
			attribute_map.links.new(attribute_statistic.outputs[4], map_range.inputs[2])
			#named_attribute_004.Attribute -> attribute_statistic.Attribute
			attribute_map.links.new(named_attribute_004.outputs[0], attribute_statistic.inputs[2])
			#attribute_statistic.Min -> map_range.From Min
			attribute_map.links.new(attribute_statistic.outputs[3], map_range.inputs[1])
			#named_attribute_004.Attribute -> map_range.Value
			attribute_map.links.new(named_attribute_004.outputs[0], map_range.inputs[0])
			#group_input.Sample Atoms -> attribute_statistic.Geometry
			attribute_map.links.new(group_input.outputs[0], attribute_statistic.inputs[0])
			#map_range.Result -> group_output.Value
			attribute_map.links.new(map_range.outputs[0], group_output.inputs[0])
			#group_input.Attribute -> named_attribute_004.Name
			attribute_map.links.new(group_input.outputs[1], named_attribute_004.inputs[0])
			#group_input.Value Min -> map_range.To Min
			attribute_map.links.new(group_input.outputs[2], map_range.inputs[3])
			#group_input.Value Max -> map_range.To Max
			attribute_map.links.new(group_input.outputs[3], map_range.inputs[4])
			return attribute_map

		attribute_map = attribute_map_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Attribute Map", type = 'NODES')
		mod.node_group = attribute_map
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Attribute_Map.bl_idname)
			
def register():
	bpy.utils.register_class(Attribute_Map)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Attribute_Map)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
