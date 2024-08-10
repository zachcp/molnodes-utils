bl_info = {
	"name" : "Animate Trails",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Animate_Trails(bpy.types.Operator):
	bl_idname = "node.animate_trails"
	bl_label = "Animate Trails"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _mn_world_scale node group
		def _mn_world_scale_node_group():
			_mn_world_scale = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_world_scale")

			_mn_world_scale.color_tag = 'NONE'
			_mn_world_scale.description = ""

			
			#_mn_world_scale interface
			#Socket world_scale
			world_scale_socket = _mn_world_scale.interface.new_socket(name = "world_scale", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			world_scale_socket.subtype = 'NONE'
			world_scale_socket.default_value = 0.009999999776482582
			world_scale_socket.min_value = -3.4028234663852886e+38
			world_scale_socket.max_value = 3.4028234663852886e+38
			world_scale_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_world_scale nodes
			#node Group Input
			group_input = _mn_world_scale.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Value
			value = _mn_world_scale.nodes.new("ShaderNodeValue")
			value.label = "world_scale"
			value.name = "Value"
			
			value.outputs[0].default_value = 0.009999999776482582
			#node Group Output
			group_output = _mn_world_scale.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			
			
			
			#Set locations
			group_input.location = (-200.0, 0.0)
			value.location = (0.0, 0.0)
			group_output.location = (190.0, 0.0)
			
			#Set dimensions
			group_input.width, group_input.height = 140.0, 100.0
			value.width, value.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			
			#initialize _mn_world_scale links
			#value.Value -> group_output.world_scale
			_mn_world_scale.links.new(value.outputs[0], group_output.inputs[0])
			return _mn_world_scale

		_mn_world_scale = _mn_world_scale_node_group()

		#initialize mn_units node group
		def mn_units_node_group():
			mn_units = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "MN Units")

			mn_units.color_tag = 'NONE'
			mn_units.description = ""

			
			#mn_units interface
			#Socket Angstrom
			angstrom_socket = mn_units.interface.new_socket(name = "Angstrom", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			angstrom_socket.subtype = 'NONE'
			angstrom_socket.default_value = 0.0
			angstrom_socket.min_value = -3.4028234663852886e+38
			angstrom_socket.max_value = 3.4028234663852886e+38
			angstrom_socket.attribute_domain = 'POINT'
			
			#Socket Nanometre
			nanometre_socket = mn_units.interface.new_socket(name = "Nanometre", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			nanometre_socket.subtype = 'NONE'
			nanometre_socket.default_value = 0.0
			nanometre_socket.min_value = -3.4028234663852886e+38
			nanometre_socket.max_value = 3.4028234663852886e+38
			nanometre_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket = mn_units.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket.subtype = 'NONE'
			value_socket.default_value = 3.0
			value_socket.min_value = -10000.0
			value_socket.max_value = 10000.0
			value_socket.attribute_domain = 'POINT'
			value_socket.description = "A value which will be scaled appropriately for the world"
			
			
			#initialize mn_units nodes
			#node Group Output
			group_output_1 = mn_units.nodes.new("NodeGroupOutput")
			group_output_1.name = "Group Output"
			group_output_1.is_active_output = True
			
			#node Group Input
			group_input_1 = mn_units.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			
			#node Math
			math = mn_units.nodes.new("ShaderNodeMath")
			math.name = "Math"
			math.operation = 'MULTIPLY'
			math.use_clamp = False
			
			#node Math.001
			math_001 = mn_units.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.operation = 'MULTIPLY'
			math_001.use_clamp = False
			#Value_001
			math_001.inputs[1].default_value = 10.0
			
			#node Group
			group = mn_units.nodes.new("GeometryNodeGroup")
			group.name = "Group"
			group.node_tree = _mn_world_scale
			
			
			
			
			#Set locations
			group_output_1.location = (190.0, 0.0)
			group_input_1.location = (-240.0, 0.0)
			math.location = (-60.0, 0.0)
			math_001.location = (-60.0, -160.0)
			group.location = (-304.00421142578125, -104.114013671875)
			
			#Set dimensions
			group_output_1.width, group_output_1.height = 140.0, 100.0
			group_input_1.width, group_input_1.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			group.width, group.height = 197.58424377441406, 100.0
			
			#initialize mn_units links
			#math.Value -> group_output_1.Angstrom
			mn_units.links.new(math.outputs[0], group_output_1.inputs[0])
			#group_input_1.Value -> math.Value
			mn_units.links.new(group_input_1.outputs[0], math.inputs[0])
			#group.world_scale -> math.Value
			mn_units.links.new(group.outputs[0], math.inputs[1])
			#math.Value -> math_001.Value
			mn_units.links.new(math.outputs[0], math_001.inputs[0])
			#math_001.Value -> group_output_1.Nanometre
			mn_units.links.new(math_001.outputs[0], group_output_1.inputs[1])
			return mn_units

		mn_units = mn_units_node_group()

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
			group_output_2 = _mn_point_curve_trails.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Group Input
			group_input_2 = _mn_point_curve_trails.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
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
			group_output_2.location = (1002.3253173828125, 0.0)
			group_input_2.location = (-1012.3253173828125, 0.0)
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
			group_output_2.width, group_output_2.height = 140.0, 100.0
			group_input_2.width, group_input_2.height = 140.0, 100.0
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
			#group_input_2.Geometry -> separate_geometry.Geometry
			_mn_point_curve_trails.links.new(group_input_2.outputs[0], separate_geometry.inputs[0])
			#group_input_2.Count -> resample_curve_002.Count
			_mn_point_curve_trails.links.new(group_input_2.outputs[2], resample_curve_002.inputs[2])
			#group_input_2.Selection -> separate_geometry.Selection
			_mn_point_curve_trails.links.new(group_input_2.outputs[1], separate_geometry.inputs[1])
			#simulation_output.Geometry -> group_output_2.Geometry
			_mn_point_curve_trails.links.new(simulation_output.outputs[0], group_output_2.inputs[0])
			return _mn_point_curve_trails

		_mn_point_curve_trails = _mn_point_curve_trails_node_group()

		#initialize animate_trails node group
		def animate_trails_node_group():
			animate_trails = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Animate Trails")

			animate_trails.color_tag = 'GEOMETRY'
			animate_trails.description = ""

			
			#animate_trails interface
			#Socket Geometry
			geometry_socket_2 = animate_trails.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_2.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket = animate_trails.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket.attribute_domain = 'POINT'
			atoms_socket.description = "Atoms to add trails to"
			
			#Socket Selection
			selection_socket_1 = animate_trails.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_1.attribute_domain = 'POINT'
			selection_socket_1.hide_value = True
			selection_socket_1.description = "Selection of atoms to apply this node to"
			
			#Panel Trail
			trail_panel = animate_trails.interface.new_panel("Trail")
			#Socket Trail Frames
			trail_frames_socket = animate_trails.interface.new_socket(name = "Trail Frames", in_out='INPUT', socket_type = 'NodeSocketInt', parent = trail_panel)
			trail_frames_socket.subtype = 'NONE'
			trail_frames_socket.default_value = 5
			trail_frames_socket.min_value = 1
			trail_frames_socket.max_value = 100000
			trail_frames_socket.attribute_domain = 'POINT'
			trail_frames_socket.description = "Number of previous frames from the trajectory to display"
			
			#Socket Trail Radius
			trail_radius_socket = animate_trails.interface.new_socket(name = "Trail Radius", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = trail_panel)
			trail_radius_socket.subtype = 'NONE'
			trail_radius_socket.default_value = 1.0
			trail_radius_socket.min_value = 0.0
			trail_radius_socket.max_value = 10000.0
			trail_radius_socket.attribute_domain = 'POINT'
			
			#Socket Trail Cutoff (A)
			trail_cutoff__a__socket = animate_trails.interface.new_socket(name = "Trail Cutoff (A)", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = trail_panel)
			trail_cutoff__a__socket.subtype = 'NONE'
			trail_cutoff__a__socket.default_value = 10.0
			trail_cutoff__a__socket.min_value = 0.0
			trail_cutoff__a__socket.max_value = 10000.0
			trail_cutoff__a__socket.attribute_domain = 'POINT'
			
			#Socket Trail Subdivisions
			trail_subdivisions_socket = animate_trails.interface.new_socket(name = "Trail Subdivisions", in_out='INPUT', socket_type = 'NodeSocketInt', parent = trail_panel)
			trail_subdivisions_socket.subtype = 'NONE'
			trail_subdivisions_socket.default_value = 6
			trail_subdivisions_socket.min_value = 1
			trail_subdivisions_socket.max_value = 16
			trail_subdivisions_socket.attribute_domain = 'POINT'
			
			#Socket Trail Resolution
			trail_resolution_socket = animate_trails.interface.new_socket(name = "Trail Resolution", in_out='INPUT', socket_type = 'NodeSocketInt', parent = trail_panel)
			trail_resolution_socket.subtype = 'NONE'
			trail_resolution_socket.default_value = 6
			trail_resolution_socket.min_value = 3
			trail_resolution_socket.max_value = 32
			trail_resolution_socket.attribute_domain = 'POINT'
			trail_resolution_socket.description = "Tail radial resolution"
			
			
			#Panel Material
			material_panel = animate_trails.interface.new_panel("Material")
			#Socket Shade Smooth
			shade_smooth_socket = animate_trails.interface.new_socket(name = "Shade Smooth", in_out='INPUT', socket_type = 'NodeSocketBool', parent = material_panel)
			shade_smooth_socket.attribute_domain = 'POINT'
			
			#Socket Material
			material_socket = animate_trails.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial', parent = material_panel)
			material_socket.attribute_domain = 'POINT'
			
			
			
			#initialize animate_trails nodes
			#node Group Output
			group_output_3 = animate_trails.nodes.new("NodeGroupOutput")
			group_output_3.name = "Group Output"
			group_output_3.is_active_output = True
			
			#node Group Input
			group_input_3 = animate_trails.nodes.new("NodeGroupInput")
			group_input_3.name = "Group Input"
			group_input_3.outputs[3].hide = True
			group_input_3.outputs[4].hide = True
			group_input_3.outputs[5].hide = True
			group_input_3.outputs[6].hide = True
			group_input_3.outputs[8].hide = True
			
			#node Set Spline Type
			set_spline_type = animate_trails.nodes.new("GeometryNodeCurveSplineType")
			set_spline_type.name = "Set Spline Type"
			set_spline_type.spline_type = 'BEZIER'
			#Selection
			set_spline_type.inputs[1].default_value = True
			
			#node Curve to Mesh
			curve_to_mesh = animate_trails.nodes.new("GeometryNodeCurveToMesh")
			curve_to_mesh.name = "Curve to Mesh"
			#Fill Caps
			curve_to_mesh.inputs[2].default_value = True
			
			#node Curve Circle
			curve_circle = animate_trails.nodes.new("GeometryNodeCurvePrimitiveCircle")
			curve_circle.name = "Curve Circle"
			curve_circle.mode = 'RADIUS'
			#Radius
			curve_circle.inputs[4].default_value = 1.0
			
			#node Curve to Mesh.001
			curve_to_mesh_001 = animate_trails.nodes.new("GeometryNodeCurveToMesh")
			curve_to_mesh_001.name = "Curve to Mesh.001"
			#Fill Caps
			curve_to_mesh_001.inputs[2].default_value = False
			
			#node Delete Geometry
			delete_geometry = animate_trails.nodes.new("GeometryNodeDeleteGeometry")
			delete_geometry.name = "Delete Geometry"
			delete_geometry.domain = 'EDGE'
			delete_geometry.mode = 'ALL'
			
			#node Compare
			compare = animate_trails.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'FLOAT'
			compare.mode = 'ELEMENT'
			compare.operation = 'GREATER_THAN'
			
			#node Vector Math
			vector_math = animate_trails.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.operation = 'DISTANCE'
			
			#node Edge Vertices
			edge_vertices = animate_trails.nodes.new("GeometryNodeInputMeshEdgeVertices")
			edge_vertices.name = "Edge Vertices"
			
			#node Mesh to Curve
			mesh_to_curve = animate_trails.nodes.new("GeometryNodeMeshToCurve")
			mesh_to_curve.name = "Mesh to Curve"
			#Selection
			mesh_to_curve.inputs[1].default_value = True
			
			#node Set Curve Radius
			set_curve_radius = animate_trails.nodes.new("GeometryNodeSetCurveRadius")
			set_curve_radius.name = "Set Curve Radius"
			#Selection
			set_curve_radius.inputs[1].default_value = True
			
			#node Spline Parameter
			spline_parameter = animate_trails.nodes.new("GeometryNodeSplineParameter")
			spline_parameter.name = "Spline Parameter"
			spline_parameter.outputs[1].hide = True
			spline_parameter.outputs[2].hide = True
			
			#node Set Material
			set_material = animate_trails.nodes.new("GeometryNodeSetMaterial")
			set_material.name = "Set Material"
			#Selection
			set_material.inputs[1].default_value = True
			
			#node Math
			math_1 = animate_trails.nodes.new("ShaderNodeMath")
			math_1.name = "Math"
			math_1.operation = 'MULTIPLY'
			math_1.use_clamp = False
			
			#node Math.001
			math_001_1 = animate_trails.nodes.new("ShaderNodeMath")
			math_001_1.name = "Math.001"
			math_001_1.operation = 'MULTIPLY'
			math_001_1.use_clamp = False
			
			#node Capture Attribute
			capture_attribute = animate_trails.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute.name = "Capture Attribute"
			capture_attribute.active_index = 1
			capture_attribute.capture_items.clear()
			capture_attribute.capture_items.new('FLOAT', "Factor")
			capture_attribute.capture_items["Factor"].data_type = 'FLOAT'
			capture_attribute.capture_items.new('FLOAT', "Attribute")
			capture_attribute.capture_items["Attribute"].data_type = 'FLOAT'
			capture_attribute.domain = 'POINT'
			
			#node Named Attribute.003
			named_attribute_003 = animate_trails.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_003.name = "Named Attribute.003"
			named_attribute_003.data_type = 'FLOAT'
			#Name
			named_attribute_003.inputs[0].default_value = "vdw_radii"
			
			#node Group Input.002
			group_input_002 = animate_trails.nodes.new("NodeGroupInput")
			group_input_002.name = "Group Input.002"
			group_input_002.outputs[0].hide = True
			group_input_002.outputs[1].hide = True
			group_input_002.outputs[2].hide = True
			group_input_002.outputs[3].hide = True
			group_input_002.outputs[5].hide = True
			group_input_002.outputs[6].hide = True
			group_input_002.outputs[7].hide = True
			group_input_002.outputs[8].hide = True
			group_input_002.outputs[9].hide = True
			
			#node Group
			group_1 = animate_trails.nodes.new("GeometryNodeGroup")
			group_1.name = "Group"
			group_1.node_tree = mn_units
			
			#node Set Shade Smooth
			set_shade_smooth = animate_trails.nodes.new("GeometryNodeSetShadeSmooth")
			set_shade_smooth.name = "Set Shade Smooth"
			set_shade_smooth.domain = 'FACE'
			#Selection
			set_shade_smooth.inputs[1].default_value = True
			
			#node Group Input.003
			group_input_003 = animate_trails.nodes.new("NodeGroupInput")
			group_input_003.name = "Group Input.003"
			group_input_003.outputs[0].hide = True
			group_input_003.outputs[1].hide = True
			group_input_003.outputs[2].hide = True
			group_input_003.outputs[3].hide = True
			group_input_003.outputs[4].hide = True
			group_input_003.outputs[5].hide = True
			group_input_003.outputs[6].hide = True
			group_input_003.outputs[9].hide = True
			
			#node Group Input.001
			group_input_001 = animate_trails.nodes.new("NodeGroupInput")
			group_input_001.name = "Group Input.001"
			group_input_001.outputs[0].hide = True
			group_input_001.outputs[1].hide = True
			group_input_001.outputs[2].hide = True
			group_input_001.outputs[3].hide = True
			group_input_001.outputs[4].hide = True
			group_input_001.outputs[5].hide = True
			group_input_001.outputs[7].hide = True
			group_input_001.outputs[8].hide = True
			group_input_001.outputs[9].hide = True
			
			#node Group Input.004
			group_input_004 = animate_trails.nodes.new("NodeGroupInput")
			group_input_004.name = "Group Input.004"
			group_input_004.outputs[0].hide = True
			group_input_004.outputs[1].hide = True
			group_input_004.outputs[2].hide = True
			group_input_004.outputs[4].hide = True
			group_input_004.outputs[5].hide = True
			group_input_004.outputs[6].hide = True
			group_input_004.outputs[7].hide = True
			group_input_004.outputs[8].hide = True
			group_input_004.outputs[9].hide = True
			
			#node Set Spline Resolution
			set_spline_resolution = animate_trails.nodes.new("GeometryNodeSetSplineResolution")
			set_spline_resolution.name = "Set Spline Resolution"
			#Selection
			set_spline_resolution.inputs[1].default_value = True
			
			#node Set Handle Type
			set_handle_type = animate_trails.nodes.new("GeometryNodeCurveSetHandles")
			set_handle_type.name = "Set Handle Type"
			set_handle_type.handle_type = 'AUTO'
			set_handle_type.mode = {'RIGHT', 'LEFT'}
			#Selection
			set_handle_type.inputs[1].default_value = True
			
			#node Group Input.005
			group_input_005 = animate_trails.nodes.new("NodeGroupInput")
			group_input_005.name = "Group Input.005"
			group_input_005.outputs[0].hide = True
			group_input_005.outputs[1].hide = True
			group_input_005.outputs[2].hide = True
			group_input_005.outputs[3].hide = True
			group_input_005.outputs[4].hide = True
			group_input_005.outputs[6].hide = True
			group_input_005.outputs[7].hide = True
			group_input_005.outputs[8].hide = True
			group_input_005.outputs[9].hide = True
			
			#node Store Named Attribute
			store_named_attribute = animate_trails.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute.name = "Store Named Attribute"
			store_named_attribute.data_type = 'FLOAT'
			store_named_attribute.domain = 'POINT'
			#Selection
			store_named_attribute.inputs[1].default_value = True
			#Name
			store_named_attribute.inputs[2].default_value = "Factor"
			
			#node Group.001
			group_001 = animate_trails.nodes.new("GeometryNodeGroup")
			group_001.name = "Group.001"
			group_001.node_tree = _mn_point_curve_trails
			
			
			
			
			#Set locations
			group_output_3.location = (1080.0, 80.0)
			group_input_3.location = (-1360.0, 140.0)
			set_spline_type.location = (-160.0, 100.0)
			curve_to_mesh.location = (560.0, 80.0)
			curve_circle.location = (360.0, -40.0)
			curve_to_mesh_001.location = (-640.0, 520.0)
			delete_geometry.location = (-480.0, 520.0)
			compare.location = (-680.0, 360.0)
			vector_math.location = (-840.0, 360.0)
			edge_vertices.location = (-1000.0, 360.0)
			mesh_to_curve.location = (-320.0, 520.0)
			set_curve_radius.location = (380.0, 80.0)
			spline_parameter.location = (-1020.0, -40.0)
			set_material.location = (920.0, 80.0)
			math_1.location = (180.0, -120.0)
			math_001_1.location = (180.0, -280.0)
			capture_attribute.location = (-840.0, 140.0)
			named_attribute_003.location = (-1020.0, -100.0)
			group_input_002.location = (-840.0, 220.0)
			group_1.location = (-680.0, 200.0)
			set_shade_smooth.location = (760.0, 80.0)
			group_input_003.location = (540.0, -80.0)
			group_input_001.location = (360.0, -180.0)
			group_input_004.location = (-180.0, -400.0)
			set_spline_resolution.location = (160.0, 100.0)
			set_handle_type.location = (0.0, 100.0)
			group_input_005.location = (-200.0, -60.0)
			store_named_attribute.location = (-1020.0, 160.0)
			group_001.location = (-1180.0, 140.0)
			
			#Set dimensions
			group_output_3.width, group_output_3.height = 140.0, 100.0
			group_input_3.width, group_input_3.height = 140.0, 100.0
			set_spline_type.width, set_spline_type.height = 140.0, 100.0
			curve_to_mesh.width, curve_to_mesh.height = 140.0, 100.0
			curve_circle.width, curve_circle.height = 140.0, 100.0
			curve_to_mesh_001.width, curve_to_mesh_001.height = 140.0, 100.0
			delete_geometry.width, delete_geometry.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			edge_vertices.width, edge_vertices.height = 140.0, 100.0
			mesh_to_curve.width, mesh_to_curve.height = 140.0, 100.0
			set_curve_radius.width, set_curve_radius.height = 140.0, 100.0
			spline_parameter.width, spline_parameter.height = 140.0, 100.0
			set_material.width, set_material.height = 140.0, 100.0
			math_1.width, math_1.height = 140.0, 100.0
			math_001_1.width, math_001_1.height = 140.0, 100.0
			capture_attribute.width, capture_attribute.height = 140.0, 100.0
			named_attribute_003.width, named_attribute_003.height = 140.0, 100.0
			group_input_002.width, group_input_002.height = 140.0, 100.0
			group_1.width, group_1.height = 140.0, 100.0
			set_shade_smooth.width, set_shade_smooth.height = 140.0, 100.0
			group_input_003.width, group_input_003.height = 140.0, 100.0
			group_input_001.width, group_input_001.height = 140.0, 100.0
			group_input_004.width, group_input_004.height = 140.0, 100.0
			set_spline_resolution.width, set_spline_resolution.height = 140.0, 100.0
			set_handle_type.width, set_handle_type.height = 140.0, 100.0
			group_input_005.width, group_input_005.height = 140.0, 100.0
			store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
			group_001.width, group_001.height = 140.0, 100.0
			
			#initialize animate_trails links
			#compare.Result -> delete_geometry.Selection
			animate_trails.links.new(compare.outputs[0], delete_geometry.inputs[1])
			#vector_math.Value -> compare.A
			animate_trails.links.new(vector_math.outputs[1], compare.inputs[0])
			#edge_vertices.Position 1 -> vector_math.Vector
			animate_trails.links.new(edge_vertices.outputs[2], vector_math.inputs[0])
			#edge_vertices.Position 2 -> vector_math.Vector
			animate_trails.links.new(edge_vertices.outputs[3], vector_math.inputs[1])
			#delete_geometry.Geometry -> mesh_to_curve.Mesh
			animate_trails.links.new(delete_geometry.outputs[0], mesh_to_curve.inputs[0])
			#set_spline_resolution.Geometry -> set_curve_radius.Curve
			animate_trails.links.new(set_spline_resolution.outputs[0], set_curve_radius.inputs[0])
			#set_shade_smooth.Geometry -> set_material.Geometry
			animate_trails.links.new(set_shade_smooth.outputs[0], set_material.inputs[0])
			#math_1.Value -> set_curve_radius.Radius
			animate_trails.links.new(math_1.outputs[0], set_curve_radius.inputs[2])
			#math_001_1.Value -> math_1.Value
			animate_trails.links.new(math_001_1.outputs[0], math_1.inputs[1])
			#set_curve_radius.Curve -> curve_to_mesh.Curve
			animate_trails.links.new(set_curve_radius.outputs[0], curve_to_mesh.inputs[0])
			#curve_circle.Curve -> curve_to_mesh.Profile Curve
			animate_trails.links.new(curve_circle.outputs[0], curve_to_mesh.inputs[1])
			#capture_attribute.Geometry -> curve_to_mesh_001.Curve
			animate_trails.links.new(capture_attribute.outputs[0], curve_to_mesh_001.inputs[0])
			#curve_to_mesh_001.Mesh -> delete_geometry.Geometry
			animate_trails.links.new(curve_to_mesh_001.outputs[0], delete_geometry.inputs[0])
			#mesh_to_curve.Curve -> set_spline_type.Curve
			animate_trails.links.new(mesh_to_curve.outputs[0], set_spline_type.inputs[0])
			#set_material.Geometry -> group_output_3.Geometry
			animate_trails.links.new(set_material.outputs[0], group_output_3.inputs[0])
			#capture_attribute.Factor -> math_1.Value
			animate_trails.links.new(capture_attribute.outputs[1], math_1.inputs[0])
			#store_named_attribute.Geometry -> capture_attribute.Geometry
			animate_trails.links.new(store_named_attribute.outputs[0], capture_attribute.inputs[0])
			#named_attribute_003.Attribute -> capture_attribute.Attribute
			animate_trails.links.new(named_attribute_003.outputs[0], capture_attribute.inputs[2])
			#capture_attribute.Attribute -> math_001_1.Value
			animate_trails.links.new(capture_attribute.outputs[2], math_001_1.inputs[0])
			#spline_parameter.Factor -> capture_attribute.Factor
			animate_trails.links.new(spline_parameter.outputs[0], capture_attribute.inputs[1])
			#group_input_002.Trail Cutoff (A) -> group_1.Value
			animate_trails.links.new(group_input_002.outputs[4], group_1.inputs[0])
			#group_1.Angstrom -> compare.B
			animate_trails.links.new(group_1.outputs[0], compare.inputs[1])
			#curve_to_mesh.Mesh -> set_shade_smooth.Geometry
			animate_trails.links.new(curve_to_mesh.outputs[0], set_shade_smooth.inputs[0])
			#group_input_003.Material -> set_material.Material
			animate_trails.links.new(group_input_003.outputs[8], set_material.inputs[2])
			#group_input_001.Trail Resolution -> curve_circle.Resolution
			animate_trails.links.new(group_input_001.outputs[6], curve_circle.inputs[0])
			#group_input_004.Trail Radius -> math_001_1.Value
			animate_trails.links.new(group_input_004.outputs[3], math_001_1.inputs[1])
			#set_handle_type.Curve -> set_spline_resolution.Geometry
			animate_trails.links.new(set_handle_type.outputs[0], set_spline_resolution.inputs[0])
			#set_spline_type.Curve -> set_handle_type.Curve
			animate_trails.links.new(set_spline_type.outputs[0], set_handle_type.inputs[0])
			#group_input_005.Trail Subdivisions -> set_spline_resolution.Resolution
			animate_trails.links.new(group_input_005.outputs[5], set_spline_resolution.inputs[2])
			#group_input_003.Shade Smooth -> set_shade_smooth.Shade Smooth
			animate_trails.links.new(group_input_003.outputs[7], set_shade_smooth.inputs[2])
			#spline_parameter.Factor -> store_named_attribute.Value
			animate_trails.links.new(spline_parameter.outputs[0], store_named_attribute.inputs[3])
			#group_001.Geometry -> store_named_attribute.Geometry
			animate_trails.links.new(group_001.outputs[0], store_named_attribute.inputs[0])
			#group_input_3.Atoms -> group_001.Geometry
			animate_trails.links.new(group_input_3.outputs[0], group_001.inputs[0])
			#group_input_3.Trail Frames -> group_001.Count
			animate_trails.links.new(group_input_3.outputs[2], group_001.inputs[2])
			#group_input_3.Selection -> group_001.Selection
			animate_trails.links.new(group_input_3.outputs[1], group_001.inputs[1])
			return animate_trails

		animate_trails = animate_trails_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Animate Trails", type = 'NODES')
		mod.node_group = animate_trails
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Animate_Trails.bl_idname)
			
def register():
	bpy.utils.register_class(Animate_Trails)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Animate_Trails)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
