bl_info = {
	"name" : ".MN_point_curve_trails",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _MN_point_curve_trails(bpy.types.Operator):
	bl_idname = "node._mn_point_curve_trails"
	bl_label = ".MN_point_curve_trails"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _mn_point_curve_trails node group
		def _mn_point_curve_trails_node_group():
			_mn_point_curve_trails = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_point_curve_trails")

			_mn_point_curve_trails.color_tag = 'NONE'
			_mn_point_curve_trails.description = ""

			
			#_mn_point_curve_trails interface
			#Socket Geometry
			geometry_socket = _mn_point_curve_trails.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_1 = _mn_point_curve_trails.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_1.attribute_domain = 'POINT'
			
			#Socket Selection
			selection_socket = _mn_point_curve_trails.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket.attribute_domain = 'POINT'
			selection_socket.hide_value = True
			
			#Socket Count
			count_socket = _mn_point_curve_trails.interface.new_socket(name = "Count", in_out='INPUT', socket_type = 'NodeSocketInt')
			count_socket.subtype = 'NONE'
			count_socket.default_value = 5
			count_socket.min_value = 1
			count_socket.max_value = 100000
			count_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_point_curve_trails nodes
			#node Group Output
			group_output = _mn_point_curve_trails.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = _mn_point_curve_trails.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Separate Geometry
			separate_geometry = _mn_point_curve_trails.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry.name = "Separate Geometry"
			separate_geometry.domain = 'POINT'
			
			#node Simulation Input
			simulation_input = _mn_point_curve_trails.nodes.new("GeometryNodeSimulationInput")
			simulation_input.name = "Simulation Input"
			#node Simulation Output
			simulation_output = _mn_point_curve_trails.nodes.new("GeometryNodeSimulationOutput")
			simulation_output.name = "Simulation Output"
			simulation_output.active_index = 1
			simulation_output.state_items.clear()
			# Create item "Geometry"
			simulation_output.state_items.new('GEOMETRY', "Geometry")
			simulation_output.state_items[0].attribute_domain = 'POINT'
			# Create item "Index"
			simulation_output.state_items.new('INT', "Index")
			simulation_output.state_items[1].attribute_domain = 'POINT'
			#Skip
			simulation_output.inputs[0].default_value = False
			
			#node Index
			index = _mn_point_curve_trails.nodes.new("GeometryNodeInputIndex")
			index.name = "Index"
			
			#node Instance on Points
			instance_on_points = _mn_point_curve_trails.nodes.new("GeometryNodeInstanceOnPoints")
			instance_on_points.name = "Instance on Points"
			#Selection
			instance_on_points.inputs[1].default_value = True
			#Pick Instance
			instance_on_points.inputs[3].default_value = False
			#Instance Index
			instance_on_points.inputs[4].default_value = 0
			#Rotation
			instance_on_points.inputs[5].default_value = (0.0, 0.0, 0.0)
			#Scale
			instance_on_points.inputs[6].default_value = (1.0, 1.0, 1.0)
			
			#node Curve Line
			curve_line = _mn_point_curve_trails.nodes.new("GeometryNodeCurvePrimitiveLine")
			curve_line.name = "Curve Line"
			curve_line.mode = 'POINTS'
			#Start
			curve_line.inputs[0].default_value = (0.0, 0.0, 0.0)
			#End
			curve_line.inputs[1].default_value = (0.0, 0.0, 0.0)
			
			#node Set Position
			set_position = _mn_point_curve_trails.nodes.new("GeometryNodeSetPosition")
			set_position.name = "Set Position"
			#Selection
			set_position.inputs[1].default_value = True
			#Offset
			set_position.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Switch
			switch = _mn_point_curve_trails.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'VECTOR'
			
			#node Endpoint Selection
			endpoint_selection = _mn_point_curve_trails.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection.name = "Endpoint Selection"
			#Start Size
			endpoint_selection.inputs[0].default_value = 0
			#End Size
			endpoint_selection.inputs[1].default_value = 1
			
			#node Sample Index
			sample_index = _mn_point_curve_trails.nodes.new("GeometryNodeSampleIndex")
			sample_index.name = "Sample Index"
			sample_index.clamp = False
			sample_index.data_type = 'FLOAT_VECTOR'
			sample_index.domain = 'POINT'
			
			#node Position.001
			position_001 = _mn_point_curve_trails.nodes.new("GeometryNodeInputPosition")
			position_001.name = "Position.001"
			
			#node Evaluate at Index
			evaluate_at_index = _mn_point_curve_trails.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index.name = "Evaluate at Index"
			evaluate_at_index.data_type = 'FLOAT_VECTOR'
			evaluate_at_index.domain = 'POINT'
			
			#node Offset Point in Curve
			offset_point_in_curve = _mn_point_curve_trails.nodes.new("GeometryNodeOffsetPointInCurve")
			offset_point_in_curve.name = "Offset Point in Curve"
			#Point Index
			offset_point_in_curve.inputs[0].default_value = 0
			#Offset
			offset_point_in_curve.inputs[1].default_value = 1
			
			#node Capture Attribute.001
			capture_attribute_001 = _mn_point_curve_trails.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute_001.name = "Capture Attribute.001"
			capture_attribute_001.active_index = 0
			capture_attribute_001.capture_items.clear()
			capture_attribute_001.capture_items.new('FLOAT', "Index")
			capture_attribute_001.capture_items["Index"].data_type = 'INT'
			capture_attribute_001.domain = 'POINT'
			
			#node Realize Instances.001
			realize_instances_001 = _mn_point_curve_trails.nodes.new("GeometryNodeRealizeInstances")
			realize_instances_001.name = "Realize Instances.001"
			#Selection
			realize_instances_001.inputs[1].default_value = True
			#Realize All
			realize_instances_001.inputs[2].default_value = True
			#Depth
			realize_instances_001.inputs[3].default_value = 0
			
			#node Reroute
			reroute = _mn_point_curve_trails.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Resample Curve.002
			resample_curve_002 = _mn_point_curve_trails.nodes.new("GeometryNodeResampleCurve")
			resample_curve_002.name = "Resample Curve.002"
			resample_curve_002.mode = 'COUNT'
			#Selection
			resample_curve_002.inputs[1].default_value = True
			
			#Process zone input Simulation Input
			simulation_input.pair_with_output(simulation_output)
			
			#Skip
			simulation_output.inputs[0].default_value = False
			
			
			
			
			#Set locations
			group_output.location = (1002.3253173828125, 0.0)
			group_input.location = (-1012.3253173828125, 0.0)
			separate_geometry.location = (-812.3253173828125, 210.2117919921875)
			simulation_input.location = (132.3253173828125, 240.0)
			simulation_output.location = (812.3253173828125, 240.0)
			index.location = (-627.6746826171875, 80.0)
			instance_on_points.location = (-207.6746826171875, 240.0)
			curve_line.location = (-389.73974609375, 178.92279052734375)
			set_position.location = (632.3253173828125, 240.0)
			switch.location = (632.3253173828125, -120.0)
			endpoint_selection.location = (632.3253173828125, 0.0)
			sample_index.location = (452.3253173828125, 80.0)
			position_001.location = (252.3253173828125, -240.0)
			evaluate_at_index.location = (452.3253173828125, -120.0)
			offset_point_in_curve.location = (252.3253173828125, -100.0)
			capture_attribute_001.location = (-633.4364013671875, 219.3778076171875)
			realize_instances_001.location = (-47.6746826171875, 240.0)
			reroute.location = (-427.6746826171875, -120.0)
			resample_curve_002.location = (312.3253173828125, 240.0)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			separate_geometry.width, separate_geometry.height = 140.0, 100.0
			simulation_input.width, simulation_input.height = 140.0, 100.0
			simulation_output.width, simulation_output.height = 140.0, 100.0
			index.width, index.height = 140.0, 100.0
			instance_on_points.width, instance_on_points.height = 140.0, 100.0
			curve_line.width, curve_line.height = 140.0, 100.0
			set_position.width, set_position.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			endpoint_selection.width, endpoint_selection.height = 140.0, 100.0
			sample_index.width, sample_index.height = 140.0, 100.0
			position_001.width, position_001.height = 140.0, 100.0
			evaluate_at_index.width, evaluate_at_index.height = 140.0, 100.0
			offset_point_in_curve.width, offset_point_in_curve.height = 140.0, 100.0
			capture_attribute_001.width, capture_attribute_001.height = 140.0, 100.0
			realize_instances_001.width, realize_instances_001.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			resample_curve_002.width, resample_curve_002.height = 140.0, 100.0
			
			#initialize _mn_point_curve_trails links
			#realize_instances_001.Geometry -> simulation_input.Geometry
			_mn_point_curve_trails.links.new(realize_instances_001.outputs[0], simulation_input.inputs[0])
			#switch.Output -> set_position.Position
			_mn_point_curve_trails.links.new(switch.outputs[0], set_position.inputs[2])
			#curve_line.Curve -> instance_on_points.Instance
			_mn_point_curve_trails.links.new(curve_line.outputs[0], instance_on_points.inputs[2])
			#sample_index.Value -> switch.True
			_mn_point_curve_trails.links.new(sample_index.outputs[0], switch.inputs[2])
			#instance_on_points.Instances -> realize_instances_001.Geometry
			_mn_point_curve_trails.links.new(instance_on_points.outputs[0], realize_instances_001.inputs[0])
			#position_001.Position -> evaluate_at_index.Value
			_mn_point_curve_trails.links.new(position_001.outputs[0], evaluate_at_index.inputs[1])
			#endpoint_selection.Selection -> switch.Switch
			_mn_point_curve_trails.links.new(endpoint_selection.outputs[0], switch.inputs[0])
			#set_position.Geometry -> simulation_output.Geometry
			_mn_point_curve_trails.links.new(set_position.outputs[0], simulation_output.inputs[1])
			#capture_attribute_001.Index -> simulation_input.Index
			_mn_point_curve_trails.links.new(capture_attribute_001.outputs[1], simulation_input.inputs[1])
			#simulation_input.Index -> simulation_output.Index
			_mn_point_curve_trails.links.new(simulation_input.outputs[2], simulation_output.inputs[2])
			#separate_geometry.Selection -> capture_attribute_001.Geometry
			_mn_point_curve_trails.links.new(separate_geometry.outputs[0], capture_attribute_001.inputs[0])
			#capture_attribute_001.Geometry -> reroute.Input
			_mn_point_curve_trails.links.new(capture_attribute_001.outputs[0], reroute.inputs[0])
			#index.Index -> capture_attribute_001.Index
			_mn_point_curve_trails.links.new(index.outputs[0], capture_attribute_001.inputs[1])
			#reroute.Output -> sample_index.Geometry
			_mn_point_curve_trails.links.new(reroute.outputs[0], sample_index.inputs[0])
			#evaluate_at_index.Value -> switch.False
			_mn_point_curve_trails.links.new(evaluate_at_index.outputs[0], switch.inputs[1])
			#capture_attribute_001.Geometry -> instance_on_points.Points
			_mn_point_curve_trails.links.new(capture_attribute_001.outputs[0], instance_on_points.inputs[0])
			#position_001.Position -> sample_index.Value
			_mn_point_curve_trails.links.new(position_001.outputs[0], sample_index.inputs[1])
			#simulation_input.Geometry -> resample_curve_002.Curve
			_mn_point_curve_trails.links.new(simulation_input.outputs[1], resample_curve_002.inputs[0])
			#simulation_input.Index -> sample_index.Index
			_mn_point_curve_trails.links.new(simulation_input.outputs[2], sample_index.inputs[2])
			#resample_curve_002.Curve -> set_position.Geometry
			_mn_point_curve_trails.links.new(resample_curve_002.outputs[0], set_position.inputs[0])
			#offset_point_in_curve.Point Index -> evaluate_at_index.Index
			_mn_point_curve_trails.links.new(offset_point_in_curve.outputs[1], evaluate_at_index.inputs[0])
			#group_input.Geometry -> separate_geometry.Geometry
			_mn_point_curve_trails.links.new(group_input.outputs[0], separate_geometry.inputs[0])
			#group_input.Count -> resample_curve_002.Count
			_mn_point_curve_trails.links.new(group_input.outputs[2], resample_curve_002.inputs[2])
			#group_input.Selection -> separate_geometry.Selection
			_mn_point_curve_trails.links.new(group_input.outputs[1], separate_geometry.inputs[1])
			#simulation_output.Geometry -> group_output.Geometry
			_mn_point_curve_trails.links.new(simulation_output.outputs[0], group_output.inputs[0])
			return _mn_point_curve_trails

		_mn_point_curve_trails = _mn_point_curve_trails_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".MN_point_curve_trails", type = 'NODES')
		mod.node_group = _mn_point_curve_trails
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_MN_point_curve_trails.bl_idname)
			
def register():
	bpy.utils.register_class(_MN_point_curve_trails)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_MN_point_curve_trails)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
