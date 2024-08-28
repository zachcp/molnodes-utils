bl_info = {
	"name" : ".MN_animate_falloff_empty",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _MN_animate_falloff_empty(bpy.types.Operator):
	bl_idname = "node._mn_animate_falloff_empty"
	bl_label = ".MN_animate_falloff_empty"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _mn_animate_falloff_empty node group
		def _mn_animate_falloff_empty_node_group():
			_mn_animate_falloff_empty = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_animate_falloff_empty")

			_mn_animate_falloff_empty.color_tag = 'NONE'
			_mn_animate_falloff_empty.description = ""

			
			#_mn_animate_falloff_empty interface
			#Socket Falloff
			falloff_socket = _mn_animate_falloff_empty.interface.new_socket(name = "Falloff", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			falloff_socket.default_value = 0.0
			falloff_socket.min_value = -3.4028234663852886e+38
			falloff_socket.max_value = 3.4028234663852886e+38
			falloff_socket.subtype = 'NONE'
			falloff_socket.attribute_domain = 'POINT'
			
			#Socket Distance
			distance_socket = _mn_animate_falloff_empty.interface.new_socket(name = "Distance", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			distance_socket.default_value = 0.0
			distance_socket.min_value = -3.4028234663852886e+38
			distance_socket.max_value = 3.4028234663852886e+38
			distance_socket.subtype = 'NONE'
			distance_socket.attribute_domain = 'POINT'
			
			#Socket Object
			object_socket = _mn_animate_falloff_empty.interface.new_socket(name = "Object", in_out='INPUT', socket_type = 'NodeSocketObject')
			object_socket.attribute_domain = 'POINT'
			
			#Socket Smoother Step
			smoother_step_socket = _mn_animate_falloff_empty.interface.new_socket(name = "Smoother Step", in_out='INPUT', socket_type = 'NodeSocketBool')
			smoother_step_socket.default_value = False
			smoother_step_socket.attribute_domain = 'POINT'
			
			#Socket From Min
			from_min_socket = _mn_animate_falloff_empty.interface.new_socket(name = "From Min", in_out='INPUT', socket_type = 'NodeSocketFloat')
			from_min_socket.default_value = 0.0
			from_min_socket.min_value = -10000.0
			from_min_socket.max_value = 10000.0
			from_min_socket.subtype = 'NONE'
			from_min_socket.attribute_domain = 'POINT'
			
			#Socket From Max
			from_max_socket = _mn_animate_falloff_empty.interface.new_socket(name = "From Max", in_out='INPUT', socket_type = 'NodeSocketFloat')
			from_max_socket.default_value = 1.0
			from_max_socket.min_value = -10000.0
			from_max_socket.max_value = 10000.0
			from_max_socket.subtype = 'NONE'
			from_max_socket.attribute_domain = 'POINT'
			
			#Socket To Min
			to_min_socket = _mn_animate_falloff_empty.interface.new_socket(name = "To Min", in_out='INPUT', socket_type = 'NodeSocketFloat')
			to_min_socket.default_value = 0.0
			to_min_socket.min_value = -10000.0
			to_min_socket.max_value = 10000.0
			to_min_socket.subtype = 'NONE'
			to_min_socket.attribute_domain = 'POINT'
			
			#Socket To Max
			to_max_socket = _mn_animate_falloff_empty.interface.new_socket(name = "To Max", in_out='INPUT', socket_type = 'NodeSocketFloat')
			to_max_socket.default_value = 1.0
			to_max_socket.min_value = -10000.0
			to_max_socket.max_value = 10000.0
			to_max_socket.subtype = 'NONE'
			to_max_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_animate_falloff_empty nodes
			#node Points
			points = _mn_animate_falloff_empty.nodes.new("GeometryNodePoints")
			points.name = "Points"
			#Count
			points.inputs[0].default_value = 1
			#Radius
			points.inputs[2].default_value = 0.10000000149011612
			
			#node Geometry Proximity
			geometry_proximity = _mn_animate_falloff_empty.nodes.new("GeometryNodeProximity")
			geometry_proximity.name = "Geometry Proximity"
			geometry_proximity.target_element = 'POINTS'
			#Group ID
			geometry_proximity.inputs[1].default_value = 0
			#Source Position
			geometry_proximity.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Sample Group ID
			geometry_proximity.inputs[3].default_value = 0
			
			#node Map Range.001
			map_range_001 = _mn_animate_falloff_empty.nodes.new("ShaderNodeMapRange")
			map_range_001.name = "Map Range.001"
			map_range_001.clamp = True
			map_range_001.data_type = 'FLOAT'
			map_range_001.interpolation_type = 'SMOOTHERSTEP'
			
			#node Map Range
			map_range = _mn_animate_falloff_empty.nodes.new("ShaderNodeMapRange")
			map_range.name = "Map Range"
			map_range.clamp = True
			map_range.data_type = 'FLOAT'
			map_range.interpolation_type = 'LINEAR'
			
			#node Switch
			switch = _mn_animate_falloff_empty.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'FLOAT'
			
			#node Group Output
			group_output = _mn_animate_falloff_empty.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Reroute
			reroute = _mn_animate_falloff_empty.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Group Input
			group_input = _mn_animate_falloff_empty.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Reroute.001
			reroute_001 = _mn_animate_falloff_empty.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			#node Object Info
			object_info = _mn_animate_falloff_empty.nodes.new("GeometryNodeObjectInfo")
			object_info.name = "Object Info"
			object_info.transform_space = 'RELATIVE'
			#As Instance
			object_info.inputs[1].default_value = False
			
			#node Math.001
			math_001 = _mn_animate_falloff_empty.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.hide = True
			math_001.operation = 'MULTIPLY'
			math_001.use_clamp = False
			
			#node Math
			math = _mn_animate_falloff_empty.nodes.new("ShaderNodeMath")
			math.name = "Math"
			math.hide = True
			math.operation = 'MULTIPLY'
			math.use_clamp = False
			
			#node Vector Math
			vector_math = _mn_animate_falloff_empty.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.operation = 'ABSOLUTE'
			
			
			
			
			#Set locations
			points.location = (3.22705078125, -1.35943603515625)
			geometry_proximity.location = (163.22705078125, -1.35943603515625)
			map_range_001.location = (360.0, -280.0)
			map_range.location = (360.0, -20.0)
			switch.location = (520.0, -20.0)
			group_output.location = (948.807861328125, 9.793768882751465)
			reroute.location = (200.0, -280.0)
			group_input.location = (-340.0, -220.0)
			reroute_001.location = (220.0, -240.0)
			object_info.location = (-233.5631561279297, 2.2613203525543213)
			math_001.location = (-14.312219619750977, -252.5665740966797)
			math.location = (-12.089847564697266, -294.0532531738281)
			vector_math.location = (-133.5631561279297, -47.738677978515625)
			
			#Set dimensions
			points.width, points.height = 140.0, 100.0
			geometry_proximity.width, geometry_proximity.height = 140.0, 100.0
			map_range_001.width, map_range_001.height = 140.0, 100.0
			map_range.width, map_range.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			object_info.width, object_info.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			
			#initialize _mn_animate_falloff_empty links
			#object_info.Location -> points.Position
			_mn_animate_falloff_empty.links.new(object_info.outputs[1], points.inputs[1])
			#points.Points -> geometry_proximity.Geometry
			_mn_animate_falloff_empty.links.new(points.outputs[0], geometry_proximity.inputs[0])
			#group_input.Object -> object_info.Object
			_mn_animate_falloff_empty.links.new(group_input.outputs[0], object_info.inputs[0])
			#geometry_proximity.Distance -> map_range.Value
			_mn_animate_falloff_empty.links.new(geometry_proximity.outputs[1], map_range.inputs[0])
			#reroute_001.Output -> map_range.From Min
			_mn_animate_falloff_empty.links.new(reroute_001.outputs[0], map_range.inputs[1])
			#reroute.Output -> map_range.From Max
			_mn_animate_falloff_empty.links.new(reroute.outputs[0], map_range.inputs[2])
			#geometry_proximity.Distance -> map_range_001.Value
			_mn_animate_falloff_empty.links.new(geometry_proximity.outputs[1], map_range_001.inputs[0])
			#reroute_001.Output -> map_range_001.From Min
			_mn_animate_falloff_empty.links.new(reroute_001.outputs[0], map_range_001.inputs[1])
			#reroute.Output -> map_range_001.From Max
			_mn_animate_falloff_empty.links.new(reroute.outputs[0], map_range_001.inputs[2])
			#map_range_001.Result -> group_output.Distance
			_mn_animate_falloff_empty.links.new(map_range_001.outputs[0], group_output.inputs[1])
			#map_range_001.Result -> switch.True
			_mn_animate_falloff_empty.links.new(map_range_001.outputs[0], switch.inputs[2])
			#map_range.Result -> switch.False
			_mn_animate_falloff_empty.links.new(map_range.outputs[0], switch.inputs[1])
			#group_input.Smoother Step -> switch.Switch
			_mn_animate_falloff_empty.links.new(group_input.outputs[1], switch.inputs[0])
			#group_input.To Min -> map_range.To Min
			_mn_animate_falloff_empty.links.new(group_input.outputs[4], map_range.inputs[3])
			#group_input.To Max -> map_range.To Max
			_mn_animate_falloff_empty.links.new(group_input.outputs[5], map_range.inputs[4])
			#group_input.To Min -> map_range_001.To Min
			_mn_animate_falloff_empty.links.new(group_input.outputs[4], map_range_001.inputs[3])
			#group_input.To Max -> map_range_001.To Max
			_mn_animate_falloff_empty.links.new(group_input.outputs[5], map_range_001.inputs[4])
			#switch.Output -> group_output.Falloff
			_mn_animate_falloff_empty.links.new(switch.outputs[0], group_output.inputs[0])
			#group_input.From Max -> math.Value
			_mn_animate_falloff_empty.links.new(group_input.outputs[3], math.inputs[0])
			#math.Value -> reroute.Input
			_mn_animate_falloff_empty.links.new(math.outputs[0], reroute.inputs[0])
			#vector_math.Vector -> math.Value
			_mn_animate_falloff_empty.links.new(vector_math.outputs[0], math.inputs[1])
			#math_001.Value -> reroute_001.Input
			_mn_animate_falloff_empty.links.new(math_001.outputs[0], reroute_001.inputs[0])
			#group_input.From Min -> math_001.Value
			_mn_animate_falloff_empty.links.new(group_input.outputs[2], math_001.inputs[0])
			#vector_math.Vector -> math_001.Value
			_mn_animate_falloff_empty.links.new(vector_math.outputs[0], math_001.inputs[1])
			#object_info.Scale -> vector_math.Vector
			_mn_animate_falloff_empty.links.new(object_info.outputs[3], vector_math.inputs[0])
			return _mn_animate_falloff_empty

		_mn_animate_falloff_empty = _mn_animate_falloff_empty_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".MN_animate_falloff_empty", type = 'NODES')
		mod.node_group = _mn_animate_falloff_empty
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_MN_animate_falloff_empty.bl_idname)
			
def register():
	bpy.utils.register_class(_MN_animate_falloff_empty)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_MN_animate_falloff_empty)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
