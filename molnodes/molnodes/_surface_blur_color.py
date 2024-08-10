bl_info = {
	"name" : ".surface_blur_color",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _surface_blur_color(bpy.types.Operator):
	bl_idname = "node._surface_blur_color"
	bl_label = ".surface_blur_color"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _surface_blur_color node group
		def _surface_blur_color_node_group():
			_surface_blur_color = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".surface_blur_color")

			_surface_blur_color.color_tag = 'NONE'
			_surface_blur_color.description = ""

			_surface_blur_color.is_modifier = True
			
			#_surface_blur_color interface
			#Socket Geometry
			geometry_socket = _surface_blur_color.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_1 = _surface_blur_color.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_1.attribute_domain = 'POINT'
			
			#Socket Blur Iterations
			blur_iterations_socket = _surface_blur_color.interface.new_socket(name = "Blur Iterations", in_out='INPUT', socket_type = 'NodeSocketInt')
			blur_iterations_socket.subtype = 'NONE'
			blur_iterations_socket.default_value = 0
			blur_iterations_socket.min_value = -2147483648
			blur_iterations_socket.max_value = 2147483647
			blur_iterations_socket.attribute_domain = 'POINT'
			
			#Socket Color
			color_socket = _surface_blur_color.interface.new_socket(name = "Color", in_out='INPUT', socket_type = 'NodeSocketColor')
			color_socket.attribute_domain = 'POINT'
			color_socket.hide_value = True
			
			
			#initialize _surface_blur_color nodes
			#node Group Output
			group_output = _surface_blur_color.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = _surface_blur_color.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Store Named Attribute
			store_named_attribute = _surface_blur_color.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute.name = "Store Named Attribute"
			store_named_attribute.data_type = 'FLOAT_COLOR'
			store_named_attribute.domain = 'POINT'
			#Selection
			store_named_attribute.inputs[1].default_value = True
			#Name
			store_named_attribute.inputs[2].default_value = "Color"
			
			#node Store Named Attribute.001
			store_named_attribute_001 = _surface_blur_color.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_001.name = "Store Named Attribute.001"
			store_named_attribute_001.data_type = 'FLOAT_COLOR'
			store_named_attribute_001.domain = 'FACE'
			#Selection
			store_named_attribute_001.inputs[1].default_value = True
			#Name
			store_named_attribute_001.inputs[2].default_value = "Color"
			
			#node Reroute.005
			reroute_005 = _surface_blur_color.nodes.new("NodeReroute")
			reroute_005.name = "Reroute.005"
			#node Blur Attribute.002
			blur_attribute_002 = _surface_blur_color.nodes.new("GeometryNodeBlurAttribute")
			blur_attribute_002.name = "Blur Attribute.002"
			blur_attribute_002.data_type = 'FLOAT_COLOR'
			#Weight
			blur_attribute_002.inputs[2].default_value = 1.0
			
			#node Reroute.009
			reroute_009 = _surface_blur_color.nodes.new("NodeReroute")
			reroute_009.name = "Reroute.009"
			#node Reroute.010
			reroute_010 = _surface_blur_color.nodes.new("NodeReroute")
			reroute_010.name = "Reroute.010"
			#node Switch.002
			switch_002 = _surface_blur_color.nodes.new("GeometryNodeSwitch")
			switch_002.name = "Switch.002"
			switch_002.input_type = 'GEOMETRY'
			
			#node Compare.003
			compare_003 = _surface_blur_color.nodes.new("FunctionNodeCompare")
			compare_003.name = "Compare.003"
			compare_003.data_type = 'INT'
			compare_003.mode = 'ELEMENT'
			compare_003.operation = 'NOT_EQUAL'
			#B_INT
			compare_003.inputs[3].default_value = 0
			
			#node Math
			math = _surface_blur_color.nodes.new("ShaderNodeMath")
			math.name = "Math"
			math.operation = 'SUBTRACT'
			math.use_clamp = False
			#Value_001
			math.inputs[1].default_value = 1.0
			
			
			
			
			#Set locations
			group_output.location = (490.0, 0.0)
			group_input.location = (-500.0, 0.0)
			store_named_attribute.location = (68.0, -120.0)
			store_named_attribute_001.location = (68.0, 100.0)
			reroute_005.location = (0.0, -120.0)
			blur_attribute_002.location = (-180.0, -100.0)
			reroute_009.location = (-20.0, -60.0)
			reroute_010.location = (-300.0, -80.0)
			switch_002.location = (300.0, 20.0)
			compare_003.location = (-180.0, 120.0)
			math.location = (-480.0, -140.0)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
			store_named_attribute_001.width, store_named_attribute_001.height = 140.0, 100.0
			reroute_005.width, reroute_005.height = 16.0, 100.0
			blur_attribute_002.width, blur_attribute_002.height = 140.0, 100.0
			reroute_009.width, reroute_009.height = 16.0, 100.0
			reroute_010.width, reroute_010.height = 16.0, 100.0
			switch_002.width, switch_002.height = 140.0, 100.0
			compare_003.width, compare_003.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			
			#initialize _surface_blur_color links
			#reroute_010.Output -> compare_003.A
			_surface_blur_color.links.new(reroute_010.outputs[0], compare_003.inputs[2])
			#reroute_009.Output -> store_named_attribute_001.Geometry
			_surface_blur_color.links.new(reroute_009.outputs[0], store_named_attribute_001.inputs[0])
			#store_named_attribute.Geometry -> switch_002.True
			_surface_blur_color.links.new(store_named_attribute.outputs[0], switch_002.inputs[2])
			#store_named_attribute_001.Geometry -> switch_002.False
			_surface_blur_color.links.new(store_named_attribute_001.outputs[0], switch_002.inputs[1])
			#blur_attribute_002.Value -> reroute_005.Input
			_surface_blur_color.links.new(blur_attribute_002.outputs[0], reroute_005.inputs[0])
			#reroute_009.Output -> store_named_attribute.Geometry
			_surface_blur_color.links.new(reroute_009.outputs[0], store_named_attribute.inputs[0])
			#reroute_005.Output -> store_named_attribute_001.Value
			_surface_blur_color.links.new(reroute_005.outputs[0], store_named_attribute_001.inputs[3])
			#compare_003.Result -> switch_002.Switch
			_surface_blur_color.links.new(compare_003.outputs[0], switch_002.inputs[0])
			#reroute_005.Output -> store_named_attribute.Value
			_surface_blur_color.links.new(reroute_005.outputs[0], store_named_attribute.inputs[3])
			#group_input.Color -> blur_attribute_002.Value
			_surface_blur_color.links.new(group_input.outputs[2], blur_attribute_002.inputs[0])
			#group_input.Blur Iterations -> reroute_010.Input
			_surface_blur_color.links.new(group_input.outputs[1], reroute_010.inputs[0])
			#group_input.Geometry -> reroute_009.Input
			_surface_blur_color.links.new(group_input.outputs[0], reroute_009.inputs[0])
			#switch_002.Output -> group_output.Geometry
			_surface_blur_color.links.new(switch_002.outputs[0], group_output.inputs[0])
			#reroute_010.Output -> math.Value
			_surface_blur_color.links.new(reroute_010.outputs[0], math.inputs[0])
			#math.Value -> blur_attribute_002.Iterations
			_surface_blur_color.links.new(math.outputs[0], blur_attribute_002.inputs[1])
			return _surface_blur_color

		_surface_blur_color = _surface_blur_color_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".surface_blur_color", type = 'NODES')
		mod.node_group = _surface_blur_color
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_surface_blur_color.bl_idname)
			
def register():
	bpy.utils.register_class(_surface_blur_color)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_surface_blur_color)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
