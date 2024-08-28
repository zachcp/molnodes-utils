bl_info = {
	"name" : ".MN_animate_falloff_points",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _MN_animate_falloff_points(bpy.types.Operator):
	bl_idname = "node._mn_animate_falloff_points"
	bl_label = ".MN_animate_falloff_points"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _mn_animate_falloff_points node group
		def _mn_animate_falloff_points_node_group():
			_mn_animate_falloff_points = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_animate_falloff_points")

			_mn_animate_falloff_points.color_tag = 'NONE'
			_mn_animate_falloff_points.description = ""

			
			#_mn_animate_falloff_points interface
			#Socket Falloff
			falloff_socket = _mn_animate_falloff_points.interface.new_socket(name = "Falloff", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			falloff_socket.default_value = 0.0
			falloff_socket.min_value = -3.4028234663852886e+38
			falloff_socket.max_value = 3.4028234663852886e+38
			falloff_socket.subtype = 'NONE'
			falloff_socket.attribute_domain = 'POINT'
			
			#Socket Distance
			distance_socket = _mn_animate_falloff_points.interface.new_socket(name = "Distance", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			distance_socket.default_value = 0.0
			distance_socket.min_value = -3.4028234663852886e+38
			distance_socket.max_value = 3.4028234663852886e+38
			distance_socket.subtype = 'NONE'
			distance_socket.attribute_domain = 'POINT'
			
			#Socket Target
			target_socket = _mn_animate_falloff_points.interface.new_socket(name = "Target", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			target_socket.attribute_domain = 'POINT'
			
			#Socket Smoother Step
			smoother_step_socket = _mn_animate_falloff_points.interface.new_socket(name = "Smoother Step", in_out='INPUT', socket_type = 'NodeSocketBool')
			smoother_step_socket.default_value = False
			smoother_step_socket.attribute_domain = 'POINT'
			
			#Socket From Min
			from_min_socket = _mn_animate_falloff_points.interface.new_socket(name = "From Min", in_out='INPUT', socket_type = 'NodeSocketFloat')
			from_min_socket.default_value = 0.0
			from_min_socket.min_value = -10000.0
			from_min_socket.max_value = 10000.0
			from_min_socket.subtype = 'NONE'
			from_min_socket.attribute_domain = 'POINT'
			
			#Socket From Max
			from_max_socket = _mn_animate_falloff_points.interface.new_socket(name = "From Max", in_out='INPUT', socket_type = 'NodeSocketFloat')
			from_max_socket.default_value = 1.0
			from_max_socket.min_value = -10000.0
			from_max_socket.max_value = 10000.0
			from_max_socket.subtype = 'NONE'
			from_max_socket.attribute_domain = 'POINT'
			
			#Socket To Min
			to_min_socket = _mn_animate_falloff_points.interface.new_socket(name = "To Min", in_out='INPUT', socket_type = 'NodeSocketFloat')
			to_min_socket.default_value = 0.0
			to_min_socket.min_value = -10000.0
			to_min_socket.max_value = 10000.0
			to_min_socket.subtype = 'NONE'
			to_min_socket.attribute_domain = 'POINT'
			
			#Socket To Max
			to_max_socket = _mn_animate_falloff_points.interface.new_socket(name = "To Max", in_out='INPUT', socket_type = 'NodeSocketFloat')
			to_max_socket.default_value = 1.0
			to_max_socket.min_value = -10000.0
			to_max_socket.max_value = 10000.0
			to_max_socket.subtype = 'NONE'
			to_max_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_animate_falloff_points nodes
			#node Map Range.001
			map_range_001 = _mn_animate_falloff_points.nodes.new("ShaderNodeMapRange")
			map_range_001.name = "Map Range.001"
			map_range_001.clamp = True
			map_range_001.data_type = 'FLOAT'
			map_range_001.interpolation_type = 'SMOOTHERSTEP'
			
			#node Group Output
			group_output = _mn_animate_falloff_points.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Switch
			switch = _mn_animate_falloff_points.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'FLOAT'
			
			#node Map Range
			map_range = _mn_animate_falloff_points.nodes.new("ShaderNodeMapRange")
			map_range.name = "Map Range"
			map_range.clamp = True
			map_range.data_type = 'FLOAT'
			map_range.interpolation_type = 'LINEAR'
			
			#node Geometry Proximity
			geometry_proximity = _mn_animate_falloff_points.nodes.new("GeometryNodeProximity")
			geometry_proximity.name = "Geometry Proximity"
			geometry_proximity.target_element = 'POINTS'
			#Group ID
			geometry_proximity.inputs[1].default_value = 0
			#Source Position
			geometry_proximity.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Sample Group ID
			geometry_proximity.inputs[3].default_value = 0
			
			#node Group Input
			group_input = _mn_animate_falloff_points.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			
			
			
			#Set locations
			map_range_001.location = (360.0, -280.0)
			group_output.location = (830.3638305664062, 4.788317680358887)
			switch.location = (520.0, -20.0)
			map_range.location = (360.0, -20.0)
			geometry_proximity.location = (120.0, -20.0)
			group_input.location = (-180.0, -140.0)
			
			#Set dimensions
			map_range_001.width, map_range_001.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			map_range.width, map_range.height = 140.0, 100.0
			geometry_proximity.width, geometry_proximity.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			
			#initialize _mn_animate_falloff_points links
			#geometry_proximity.Distance -> map_range.Value
			_mn_animate_falloff_points.links.new(geometry_proximity.outputs[1], map_range.inputs[0])
			#group_input.From Min -> map_range.From Min
			_mn_animate_falloff_points.links.new(group_input.outputs[2], map_range.inputs[1])
			#group_input.From Max -> map_range.From Max
			_mn_animate_falloff_points.links.new(group_input.outputs[3], map_range.inputs[2])
			#geometry_proximity.Distance -> map_range_001.Value
			_mn_animate_falloff_points.links.new(geometry_proximity.outputs[1], map_range_001.inputs[0])
			#group_input.From Min -> map_range_001.From Min
			_mn_animate_falloff_points.links.new(group_input.outputs[2], map_range_001.inputs[1])
			#group_input.From Max -> map_range_001.From Max
			_mn_animate_falloff_points.links.new(group_input.outputs[3], map_range_001.inputs[2])
			#map_range_001.Result -> group_output.Distance
			_mn_animate_falloff_points.links.new(map_range_001.outputs[0], group_output.inputs[1])
			#map_range_001.Result -> switch.True
			_mn_animate_falloff_points.links.new(map_range_001.outputs[0], switch.inputs[2])
			#map_range.Result -> switch.False
			_mn_animate_falloff_points.links.new(map_range.outputs[0], switch.inputs[1])
			#switch.Output -> group_output.Falloff
			_mn_animate_falloff_points.links.new(switch.outputs[0], group_output.inputs[0])
			#group_input.Smoother Step -> switch.Switch
			_mn_animate_falloff_points.links.new(group_input.outputs[1], switch.inputs[0])
			#group_input.To Min -> map_range.To Min
			_mn_animate_falloff_points.links.new(group_input.outputs[4], map_range.inputs[3])
			#group_input.To Max -> map_range.To Max
			_mn_animate_falloff_points.links.new(group_input.outputs[5], map_range.inputs[4])
			#group_input.To Min -> map_range_001.To Min
			_mn_animate_falloff_points.links.new(group_input.outputs[4], map_range_001.inputs[3])
			#group_input.To Max -> map_range_001.To Max
			_mn_animate_falloff_points.links.new(group_input.outputs[5], map_range_001.inputs[4])
			#group_input.Target -> geometry_proximity.Geometry
			_mn_animate_falloff_points.links.new(group_input.outputs[0], geometry_proximity.inputs[0])
			return _mn_animate_falloff_points

		_mn_animate_falloff_points = _mn_animate_falloff_points_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".MN_animate_falloff_points", type = 'NODES')
		mod.node_group = _mn_animate_falloff_points
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_MN_animate_falloff_points.bl_idname)
			
def register():
	bpy.utils.register_class(_MN_animate_falloff_points)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_MN_animate_falloff_points)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
