bl_info = {
	"name" : "Animate Value",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Animate_Value(bpy.types.Operator):
	bl_idname = "node.animate_value"
	bl_label = "Animate Value"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize animate_value node group
		def animate_value_node_group():
			animate_value = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Animate Value")

			animate_value.color_tag = 'INPUT'
			animate_value.description = ""

			
			#animate_value interface
			#Socket Value
			value_socket = animate_value.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			value_socket.default_value = 0.0
			value_socket.min_value = -3.4028234663852886e+38
			value_socket.max_value = 3.4028234663852886e+38
			value_socket.subtype = 'NONE'
			value_socket.attribute_domain = 'POINT'
			value_socket.description = "Animated value that interpolates from min to max over frames"
			
			#Socket Smoother Step
			smoother_step_socket = animate_value.interface.new_socket(name = "Smoother Step", in_out='INPUT', socket_type = 'NodeSocketBool')
			smoother_step_socket.default_value = False
			smoother_step_socket.attribute_domain = 'POINT'
			smoother_step_socket.description = "Ease out and in from the min and max values"
			
			#Socket Clamped
			clamped_socket = animate_value.interface.new_socket(name = "Clamped", in_out='INPUT', socket_type = 'NodeSocketBool')
			clamped_socket.default_value = False
			clamped_socket.attribute_domain = 'POINT'
			clamped_socket.description = "Whether to clamp the interpolated value to the max"
			
			#Panel Frame
			frame_panel = animate_value.interface.new_panel("Frame")
			#Socket Frame Start
			frame_start_socket = animate_value.interface.new_socket(name = "Frame Start", in_out='INPUT', socket_type = 'NodeSocketInt', parent = frame_panel)
			frame_start_socket.default_value = 1
			frame_start_socket.min_value = 1
			frame_start_socket.max_value = 2147483647
			frame_start_socket.subtype = 'NONE'
			frame_start_socket.attribute_domain = 'POINT'
			frame_start_socket.description = "Frame to start the animation on"
			
			#Socket Frame End
			frame_end_socket = animate_value.interface.new_socket(name = "Frame End", in_out='INPUT', socket_type = 'NodeSocketInt', parent = frame_panel)
			frame_end_socket.default_value = 250
			frame_end_socket.min_value = 1
			frame_end_socket.max_value = 2147483647
			frame_end_socket.subtype = 'NONE'
			frame_end_socket.attribute_domain = 'POINT'
			frame_end_socket.description = "Frame to finish the animation on"
			
			
			#Panel Value
			value_panel = animate_value.interface.new_panel("Value")
			#Socket Value Min
			value_min_socket = animate_value.interface.new_socket(name = "Value Min", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = value_panel)
			value_min_socket.default_value = 0.0
			value_min_socket.min_value = -10000.0
			value_min_socket.max_value = 10000.0
			value_min_socket.subtype = 'NONE'
			value_min_socket.attribute_domain = 'POINT'
			value_min_socket.description = "Value to start animation from"
			
			#Socket Value Max
			value_max_socket = animate_value.interface.new_socket(name = "Value Max", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = value_panel)
			value_max_socket.default_value = 1.0
			value_max_socket.min_value = -10000.0
			value_max_socket.max_value = 10000.0
			value_max_socket.subtype = 'NONE'
			value_max_socket.attribute_domain = 'POINT'
			value_max_socket.description = "Value to end animation at"
			
			
			
			#initialize animate_value nodes
			#node Group Input
			group_input = animate_value.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Scene Time
			scene_time = animate_value.nodes.new("GeometryNodeInputSceneTime")
			scene_time.name = "Scene Time"
			
			#node Map Range.002
			map_range_002 = animate_value.nodes.new("ShaderNodeMapRange")
			map_range_002.name = "Map Range.002"
			map_range_002.clamp = True
			map_range_002.data_type = 'FLOAT'
			map_range_002.interpolation_type = 'LINEAR'
			
			#node Map Range
			map_range = animate_value.nodes.new("ShaderNodeMapRange")
			map_range.name = "Map Range"
			map_range.clamp = False
			map_range.data_type = 'FLOAT'
			map_range.interpolation_type = 'LINEAR'
			
			#node Switch.001
			switch_001 = animate_value.nodes.new("GeometryNodeSwitch")
			switch_001.name = "Switch.001"
			switch_001.input_type = 'FLOAT'
			
			#node Group Output
			group_output = animate_value.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Map Range.001
			map_range_001 = animate_value.nodes.new("ShaderNodeMapRange")
			map_range_001.name = "Map Range.001"
			map_range_001.clamp = False
			map_range_001.data_type = 'FLOAT'
			map_range_001.interpolation_type = 'SMOOTHERSTEP'
			
			#node Switch.002
			switch_002 = animate_value.nodes.new("GeometryNodeSwitch")
			switch_002.name = "Switch.002"
			switch_002.input_type = 'FLOAT'
			
			
			
			
			#Set locations
			group_input.location = (-620.0, -180.0)
			scene_time.location = (-620.0, -80.0)
			map_range_002.location = (-60.0, 100.0)
			map_range.location = (-60.0, -160.0)
			switch_001.location = (120.0, 100.0)
			group_output.location = (779.9998779296875, 40.0)
			map_range_001.location = (-60.0, -420.0)
			switch_002.location = (349.49884033203125, 7.68292236328125)
			
			#Set dimensions
			group_input.width, group_input.height = 140.0, 100.0
			scene_time.width, scene_time.height = 140.0, 100.0
			map_range_002.width, map_range_002.height = 140.0, 100.0
			map_range.width, map_range.height = 140.0, 100.0
			switch_001.width, switch_001.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			map_range_001.width, map_range_001.height = 140.0, 100.0
			switch_002.width, switch_002.height = 140.0, 100.0
			
			#initialize animate_value links
			#scene_time.Frame -> map_range.Value
			animate_value.links.new(scene_time.outputs[1], map_range.inputs[0])
			#group_input.Frame Start -> map_range.From Min
			animate_value.links.new(group_input.outputs[2], map_range.inputs[1])
			#group_input.Frame End -> map_range.From Max
			animate_value.links.new(group_input.outputs[3], map_range.inputs[2])
			#group_input.Value Min -> map_range.To Min
			animate_value.links.new(group_input.outputs[4], map_range.inputs[3])
			#group_input.Value Max -> map_range.To Max
			animate_value.links.new(group_input.outputs[5], map_range.inputs[4])
			#scene_time.Frame -> map_range_002.Value
			animate_value.links.new(scene_time.outputs[1], map_range_002.inputs[0])
			#group_input.Frame Start -> map_range_002.From Min
			animate_value.links.new(group_input.outputs[2], map_range_002.inputs[1])
			#group_input.Frame End -> map_range_002.From Max
			animate_value.links.new(group_input.outputs[3], map_range_002.inputs[2])
			#group_input.Value Min -> map_range_002.To Min
			animate_value.links.new(group_input.outputs[4], map_range_002.inputs[3])
			#group_input.Value Max -> map_range_002.To Max
			animate_value.links.new(group_input.outputs[5], map_range_002.inputs[4])
			#group_input.Clamped -> switch_001.Switch
			animate_value.links.new(group_input.outputs[1], switch_001.inputs[0])
			#map_range_002.Result -> switch_001.True
			animate_value.links.new(map_range_002.outputs[0], switch_001.inputs[2])
			#map_range.Result -> switch_001.False
			animate_value.links.new(map_range.outputs[0], switch_001.inputs[1])
			#scene_time.Frame -> map_range_001.Value
			animate_value.links.new(scene_time.outputs[1], map_range_001.inputs[0])
			#group_input.Frame Start -> map_range_001.From Min
			animate_value.links.new(group_input.outputs[2], map_range_001.inputs[1])
			#group_input.Frame End -> map_range_001.From Max
			animate_value.links.new(group_input.outputs[3], map_range_001.inputs[2])
			#group_input.Value Min -> map_range_001.To Min
			animate_value.links.new(group_input.outputs[4], map_range_001.inputs[3])
			#group_input.Value Max -> map_range_001.To Max
			animate_value.links.new(group_input.outputs[5], map_range_001.inputs[4])
			#map_range_001.Result -> switch_002.True
			animate_value.links.new(map_range_001.outputs[0], switch_002.inputs[2])
			#switch_001.Output -> switch_002.False
			animate_value.links.new(switch_001.outputs[0], switch_002.inputs[1])
			#group_input.Smoother Step -> switch_002.Switch
			animate_value.links.new(group_input.outputs[0], switch_002.inputs[0])
			#switch_002.Output -> group_output.Value
			animate_value.links.new(switch_002.outputs[0], group_output.inputs[0])
			return animate_value

		animate_value = animate_value_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Animate Value", type = 'NODES')
		mod.node_group = animate_value
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Animate_Value.bl_idname)
			
def register():
	bpy.utils.register_class(Animate_Value)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Animate_Value)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
