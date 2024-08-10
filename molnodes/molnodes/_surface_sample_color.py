bl_info = {
	"name" : ".surface_sample_color",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _surface_sample_color(bpy.types.Operator):
	bl_idname = "node._surface_sample_color"
	bl_label = ".surface_sample_color"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _surface_sample_color node group
		def _surface_sample_color_node_group():
			_surface_sample_color = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".surface_sample_color")

			_surface_sample_color.color_tag = 'NONE'
			_surface_sample_color.description = ""

			
			#_surface_sample_color interface
			#Socket Color
			color_socket = _surface_sample_color.interface.new_socket(name = "Color", in_out='OUTPUT', socket_type = 'NodeSocketColor')
			color_socket.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket = _surface_sample_color.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket.attribute_domain = 'POINT'
			atoms_socket.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Sample CA
			sample_ca_socket = _surface_sample_color.interface.new_socket(name = "Sample CA", in_out='INPUT', socket_type = 'NodeSocketBool')
			sample_ca_socket.attribute_domain = 'POINT'
			
			
			#initialize _surface_sample_color nodes
			#node Group Output
			group_output = _surface_sample_color.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = _surface_sample_color.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Switch
			switch = _surface_sample_color.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'GEOMETRY'
			
			#node Sample Index.001
			sample_index_001 = _surface_sample_color.nodes.new("GeometryNodeSampleIndex")
			sample_index_001.name = "Sample Index.001"
			sample_index_001.clamp = False
			sample_index_001.data_type = 'FLOAT_COLOR'
			sample_index_001.domain = 'POINT'
			
			#node Named Attribute.002
			named_attribute_002 = _surface_sample_color.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002.name = "Named Attribute.002"
			named_attribute_002.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute_002.inputs[0].default_value = "Color"
			
			#node Sample Nearest.001
			sample_nearest_001 = _surface_sample_color.nodes.new("GeometryNodeSampleNearest")
			sample_nearest_001.name = "Sample Nearest.001"
			sample_nearest_001.domain = 'POINT'
			#Sample Position
			sample_nearest_001.inputs[1].default_value = (0.0, 0.0, 0.0)
			
			#node Separate Geometry.001
			separate_geometry_001 = _surface_sample_color.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_001.name = "Separate Geometry.001"
			separate_geometry_001.domain = 'POINT'
			
			#node Reroute.006
			reroute_006 = _surface_sample_color.nodes.new("NodeReroute")
			reroute_006.name = "Reroute.006"
			#node Compare
			compare = _surface_sample_color.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'EQUAL'
			#B_INT
			compare.inputs[3].default_value = 61
			
			#node Boolean Math
			boolean_math = _surface_sample_color.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'OR'
			
			#node Named Attribute.003
			named_attribute_003 = _surface_sample_color.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_003.name = "Named Attribute.003"
			named_attribute_003.data_type = 'INT'
			#Name
			named_attribute_003.inputs[0].default_value = "atom_name"
			
			#node Named Attribute.001
			named_attribute_001 = _surface_sample_color.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.data_type = 'BOOLEAN'
			#Name
			named_attribute_001.inputs[0].default_value = "is_alpha_carbon"
			
			
			
			
			#Set locations
			group_output.location = (366.8493957519531, 0.7877547144889832)
			group_input.location = (-383.1506042480469, 0.7877547144889832)
			switch.location = (-80.39474487304688, 78.26654815673828)
			sample_index_001.location = (176.84939575195312, 260.7877502441406)
			named_attribute_002.location = (176.84939575195312, 40.78775405883789)
			sample_nearest_001.location = (-83.15060424804688, 220.78775024414062)
			separate_geometry_001.location = (-83.15060424804688, -99.21224212646484)
			reroute_006.location = (-183.15060424804688, -99.21224212646484)
			compare.location = (-260.0, -380.0)
			boolean_math.location = (-80.0, -260.0)
			named_attribute_003.location = (-460.0, -380.0)
			named_attribute_001.location = (-455.15753173828125, -240.0)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			sample_index_001.width, sample_index_001.height = 140.0, 100.0
			named_attribute_002.width, named_attribute_002.height = 140.0, 100.0
			sample_nearest_001.width, sample_nearest_001.height = 140.0, 100.0
			separate_geometry_001.width, separate_geometry_001.height = 140.0, 100.0
			reroute_006.width, reroute_006.height = 16.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			named_attribute_003.width, named_attribute_003.height = 172.52069091796875, 100.0
			named_attribute_001.width, named_attribute_001.height = 162.8524169921875, 100.0
			
			#initialize _surface_sample_color links
			#reroute_006.Output -> switch.False
			_surface_sample_color.links.new(reroute_006.outputs[0], switch.inputs[1])
			#separate_geometry_001.Selection -> switch.True
			_surface_sample_color.links.new(separate_geometry_001.outputs[0], switch.inputs[2])
			#switch.Output -> sample_index_001.Geometry
			_surface_sample_color.links.new(switch.outputs[0], sample_index_001.inputs[0])
			#sample_nearest_001.Index -> sample_index_001.Index
			_surface_sample_color.links.new(sample_nearest_001.outputs[0], sample_index_001.inputs[2])
			#named_attribute_002.Attribute -> sample_index_001.Value
			_surface_sample_color.links.new(named_attribute_002.outputs[0], sample_index_001.inputs[1])
			#reroute_006.Output -> separate_geometry_001.Geometry
			_surface_sample_color.links.new(reroute_006.outputs[0], separate_geometry_001.inputs[0])
			#switch.Output -> sample_nearest_001.Geometry
			_surface_sample_color.links.new(switch.outputs[0], sample_nearest_001.inputs[0])
			#group_input.Atoms -> reroute_006.Input
			_surface_sample_color.links.new(group_input.outputs[0], reroute_006.inputs[0])
			#sample_index_001.Value -> group_output.Color
			_surface_sample_color.links.new(sample_index_001.outputs[0], group_output.inputs[0])
			#named_attribute_003.Attribute -> compare.A
			_surface_sample_color.links.new(named_attribute_003.outputs[0], compare.inputs[2])
			#compare.Result -> boolean_math.Boolean
			_surface_sample_color.links.new(compare.outputs[0], boolean_math.inputs[1])
			#named_attribute_001.Attribute -> boolean_math.Boolean
			_surface_sample_color.links.new(named_attribute_001.outputs[0], boolean_math.inputs[0])
			#boolean_math.Boolean -> separate_geometry_001.Selection
			_surface_sample_color.links.new(boolean_math.outputs[0], separate_geometry_001.inputs[1])
			#group_input.Sample CA -> switch.Switch
			_surface_sample_color.links.new(group_input.outputs[1], switch.inputs[0])
			return _surface_sample_color

		_surface_sample_color = _surface_sample_color_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".surface_sample_color", type = 'NODES')
		mod.node_group = _surface_sample_color
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_surface_sample_color.bl_idname)
			
def register():
	bpy.utils.register_class(_surface_sample_color)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_surface_sample_color)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
