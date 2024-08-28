bl_info = {
	"name" : ".curve_custom_profile",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _curve_custom_profile(bpy.types.Operator):
	bl_idname = "node._curve_custom_profile"
	bl_label = ".curve_custom_profile"
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
			world_scale_socket.default_value = 0.009999999776482582
			world_scale_socket.min_value = -3.4028234663852886e+38
			world_scale_socket.max_value = 3.4028234663852886e+38
			world_scale_socket.subtype = 'NONE'
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
			angstrom_socket.default_value = 0.0
			angstrom_socket.min_value = -3.4028234663852886e+38
			angstrom_socket.max_value = 3.4028234663852886e+38
			angstrom_socket.subtype = 'NONE'
			angstrom_socket.attribute_domain = 'POINT'
			
			#Socket Nanometre
			nanometre_socket = mn_units.interface.new_socket(name = "Nanometre", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			nanometre_socket.default_value = 0.0
			nanometre_socket.min_value = -3.4028234663852886e+38
			nanometre_socket.max_value = 3.4028234663852886e+38
			nanometre_socket.subtype = 'NONE'
			nanometre_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket = mn_units.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket.default_value = 3.0
			value_socket.min_value = -10000.0
			value_socket.max_value = 10000.0
			value_socket.subtype = 'NONE'
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

		#initialize _curve_profile_backup node group
		def _curve_profile_backup_node_group():
			_curve_profile_backup = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".curve_profile_backup")

			_curve_profile_backup.color_tag = 'NONE'
			_curve_profile_backup.description = ""

			_curve_profile_backup.is_modifier = True
			
			#_curve_profile_backup interface
			#Socket Output
			output_socket = _curve_profile_backup.interface.new_socket(name = "Output", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			output_socket.attribute_domain = 'POINT'
			
			#Socket Input
			input_socket = _curve_profile_backup.interface.new_socket(name = "Input", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			input_socket.attribute_domain = 'POINT'
			
			#Socket Resolution
			resolution_socket = _curve_profile_backup.interface.new_socket(name = "Resolution", in_out='INPUT', socket_type = 'NodeSocketInt')
			resolution_socket.default_value = 12
			resolution_socket.min_value = 3
			resolution_socket.max_value = 512
			resolution_socket.subtype = 'NONE'
			resolution_socket.attribute_domain = 'POINT'
			
			#Socket Radius
			radius_socket = _curve_profile_backup.interface.new_socket(name = "Radius", in_out='INPUT', socket_type = 'NodeSocketFloat')
			radius_socket.default_value = 0.009999999776482582
			radius_socket.min_value = 0.0
			radius_socket.max_value = 3.4028234663852886e+38
			radius_socket.subtype = 'DISTANCE'
			radius_socket.attribute_domain = 'POINT'
			
			#Socket Rotation
			rotation_socket = _curve_profile_backup.interface.new_socket(name = "Rotation", in_out='INPUT', socket_type = 'NodeSocketFloat')
			rotation_socket.default_value = 0.0
			rotation_socket.min_value = -10000.0
			rotation_socket.max_value = 10000.0
			rotation_socket.subtype = 'NONE'
			rotation_socket.attribute_domain = 'POINT'
			
			
			#initialize _curve_profile_backup nodes
			#node Group Output
			group_output_2 = _curve_profile_backup.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Compare
			compare = _curve_profile_backup.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.hide = True
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'GREATER_THAN'
			#B_INT
			compare.inputs[3].default_value = 0
			
			#node Switch
			switch = _curve_profile_backup.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'GEOMETRY'
			
			#node Domain Size
			domain_size = _curve_profile_backup.nodes.new("GeometryNodeAttributeDomainSize")
			domain_size.name = "Domain Size"
			domain_size.component = 'CURVE'
			
			#node Reroute.001
			reroute_001 = _curve_profile_backup.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			#node Curve Circle
			curve_circle = _curve_profile_backup.nodes.new("GeometryNodeCurvePrimitiveCircle")
			curve_circle.name = "Curve Circle"
			curve_circle.mode = 'RADIUS'
			
			#node Transform Geometry.001
			transform_geometry_001 = _curve_profile_backup.nodes.new("GeometryNodeTransform")
			transform_geometry_001.name = "Transform Geometry.001"
			transform_geometry_001.mode = 'COMPONENTS'
			#Translation
			transform_geometry_001.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Scale
			transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Combine XYZ
			combine_xyz = _curve_profile_backup.nodes.new("ShaderNodeCombineXYZ")
			combine_xyz.name = "Combine XYZ"
			#X
			combine_xyz.inputs[0].default_value = 0.0
			#Y
			combine_xyz.inputs[1].default_value = 0.0
			
			#node Group Input
			group_input_2 = _curve_profile_backup.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
			#node Group
			group_1 = _curve_profile_backup.nodes.new("GeometryNodeGroup")
			group_1.name = "Group"
			group_1.node_tree = mn_units
			
			
			
			
			#Set locations
			group_output_2.location = (320.278564453125, 0.0)
			compare.location = (-69.721435546875, 174.23248291015625)
			switch.location = (130.278564453125, 214.23248291015625)
			domain_size.location = (-77.112060546875, 125.76751708984375)
			reroute_001.location = (-130.278564453125, -81.5904541015625)
			curve_circle.location = (-77.112060546875, -214.23248291015625)
			transform_geometry_001.location = (130.278564453125, -45.76751708984375)
			combine_xyz.location = (-80.0, -360.0)
			group_input_2.location = (-392.2209777832031, -102.58642578125)
			group_1.location = (-380.0, -260.0)
			
			#Set dimensions
			group_output_2.width, group_output_2.height = 140.0, 100.0
			compare.width, compare.height = 137.39459228515625, 100.0
			switch.width, switch.height = 140.0, 100.0
			domain_size.width, domain_size.height = 140.0, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			curve_circle.width, curve_circle.height = 140.0, 100.0
			transform_geometry_001.width, transform_geometry_001.height = 140.0, 100.0
			combine_xyz.width, combine_xyz.height = 140.0, 100.0
			group_input_2.width, group_input_2.height = 140.0, 100.0
			group_1.width, group_1.height = 140.0, 100.0
			
			#initialize _curve_profile_backup links
			#domain_size.Point Count -> compare.A
			_curve_profile_backup.links.new(domain_size.outputs[0], compare.inputs[2])
			#reroute_001.Output -> domain_size.Geometry
			_curve_profile_backup.links.new(reroute_001.outputs[0], domain_size.inputs[0])
			#curve_circle.Curve -> transform_geometry_001.Geometry
			_curve_profile_backup.links.new(curve_circle.outputs[0], transform_geometry_001.inputs[0])
			#compare.Result -> switch.Switch
			_curve_profile_backup.links.new(compare.outputs[0], switch.inputs[0])
			#reroute_001.Output -> switch.True
			_curve_profile_backup.links.new(reroute_001.outputs[0], switch.inputs[2])
			#transform_geometry_001.Geometry -> switch.False
			_curve_profile_backup.links.new(transform_geometry_001.outputs[0], switch.inputs[1])
			#group_input_2.Input -> reroute_001.Input
			_curve_profile_backup.links.new(group_input_2.outputs[0], reroute_001.inputs[0])
			#switch.Output -> group_output_2.Output
			_curve_profile_backup.links.new(switch.outputs[0], group_output_2.inputs[0])
			#group_input_2.Resolution -> curve_circle.Resolution
			_curve_profile_backup.links.new(group_input_2.outputs[1], curve_circle.inputs[0])
			#combine_xyz.Vector -> transform_geometry_001.Rotation
			_curve_profile_backup.links.new(combine_xyz.outputs[0], transform_geometry_001.inputs[2])
			#group_input_2.Rotation -> combine_xyz.Z
			_curve_profile_backup.links.new(group_input_2.outputs[3], combine_xyz.inputs[2])
			#group_input_2.Radius -> group_1.Value
			_curve_profile_backup.links.new(group_input_2.outputs[2], group_1.inputs[0])
			#group_1.Angstrom -> curve_circle.Radius
			_curve_profile_backup.links.new(group_1.outputs[0], curve_circle.inputs[4])
			return _curve_profile_backup

		_curve_profile_backup = _curve_profile_backup_node_group()

		#initialize _guide_rotation node group
		def _guide_rotation_node_group():
			_guide_rotation = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".guide_rotation")

			_guide_rotation.color_tag = 'NONE'
			_guide_rotation.description = ""

			
			#_guide_rotation interface
			#Socket Rotation
			rotation_socket_1 = _guide_rotation.interface.new_socket(name = "Rotation", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			rotation_socket_1.default_value = (0.0, 0.0, 0.0)
			rotation_socket_1.min_value = -3.4028234663852886e+38
			rotation_socket_1.max_value = 3.4028234663852886e+38
			rotation_socket_1.subtype = 'EULER'
			rotation_socket_1.attribute_domain = 'POINT'
			
			#Socket Angle
			angle_socket = _guide_rotation.interface.new_socket(name = "Angle", in_out='INPUT', socket_type = 'NodeSocketFloat')
			angle_socket.default_value = 0.0
			angle_socket.min_value = -3.4028234663852886e+38
			angle_socket.max_value = 3.4028234663852886e+38
			angle_socket.subtype = 'ANGLE'
			angle_socket.attribute_domain = 'POINT'
			
			
			#initialize _guide_rotation nodes
			#node Align Euler to Vector.001
			align_euler_to_vector_001 = _guide_rotation.nodes.new("FunctionNodeAlignEulerToVector")
			align_euler_to_vector_001.name = "Align Euler to Vector.001"
			align_euler_to_vector_001.axis = 'X'
			align_euler_to_vector_001.pivot_axis = 'Z'
			#Factor
			align_euler_to_vector_001.inputs[1].default_value = 1.0
			
			#node Rotate Euler
			rotate_euler = _guide_rotation.nodes.new("FunctionNodeRotateEuler")
			rotate_euler.name = "Rotate Euler"
			rotate_euler.rotation_type = 'AXIS_ANGLE'
			rotate_euler.space = 'OBJECT'
			
			#node Align Euler to Vector
			align_euler_to_vector = _guide_rotation.nodes.new("FunctionNodeAlignEulerToVector")
			align_euler_to_vector.name = "Align Euler to Vector"
			align_euler_to_vector.axis = 'Z'
			align_euler_to_vector.pivot_axis = 'AUTO'
			#Rotation
			align_euler_to_vector.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Factor
			align_euler_to_vector.inputs[1].default_value = 1.0
			
			#node Group Output
			group_output_3 = _guide_rotation.nodes.new("NodeGroupOutput")
			group_output_3.name = "Group Output"
			group_output_3.is_active_output = True
			
			#node Reroute
			reroute = _guide_rotation.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Named Attribute.001
			named_attribute_001 = _guide_rotation.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_001.inputs[0].default_value = "guide_X"
			
			#node Named Attribute
			named_attribute = _guide_rotation.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute.inputs[0].default_value = "guide_Z"
			
			#node Group Input.001
			group_input_001 = _guide_rotation.nodes.new("NodeGroupInput")
			group_input_001.name = "Group Input.001"
			
			
			
			
			#Set locations
			align_euler_to_vector_001.location = (177.053955078125, 186.16505432128906)
			rotate_euler.location = (356.9603271484375, 191.41680908203125)
			align_euler_to_vector.location = (20.0, 180.0)
			group_output_3.location = (540.0, 180.0)
			reroute.location = (140.0, -40.0)
			named_attribute_001.location = (-180.0, 40.0)
			named_attribute.location = (-180.0, 180.0)
			group_input_001.location = (180.0, -40.0)
			
			#Set dimensions
			align_euler_to_vector_001.width, align_euler_to_vector_001.height = 140.0, 100.0
			rotate_euler.width, rotate_euler.height = 140.0, 100.0
			align_euler_to_vector.width, align_euler_to_vector.height = 140.0, 100.0
			group_output_3.width, group_output_3.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			named_attribute_001.width, named_attribute_001.height = 145.799072265625, 100.0
			named_attribute.width, named_attribute.height = 146.58917236328125, 100.0
			group_input_001.width, group_input_001.height = 140.0, 100.0
			
			#initialize _guide_rotation links
			#reroute.Output -> align_euler_to_vector_001.Vector
			_guide_rotation.links.new(reroute.outputs[0], align_euler_to_vector_001.inputs[2])
			#align_euler_to_vector.Rotation -> align_euler_to_vector_001.Rotation
			_guide_rotation.links.new(align_euler_to_vector.outputs[0], align_euler_to_vector_001.inputs[0])
			#rotate_euler.Rotation -> group_output_3.Rotation
			_guide_rotation.links.new(rotate_euler.outputs[0], group_output_3.inputs[0])
			#align_euler_to_vector_001.Rotation -> rotate_euler.Rotation
			_guide_rotation.links.new(align_euler_to_vector_001.outputs[0], rotate_euler.inputs[0])
			#group_input_001.Angle -> rotate_euler.Angle
			_guide_rotation.links.new(group_input_001.outputs[0], rotate_euler.inputs[3])
			#named_attribute.Attribute -> align_euler_to_vector.Vector
			_guide_rotation.links.new(named_attribute.outputs[0], align_euler_to_vector.inputs[2])
			#reroute.Output -> rotate_euler.Axis
			_guide_rotation.links.new(reroute.outputs[0], rotate_euler.inputs[2])
			#named_attribute_001.Attribute -> reroute.Input
			_guide_rotation.links.new(named_attribute_001.outputs[0], reroute.inputs[0])
			return _guide_rotation

		_guide_rotation = _guide_rotation_node_group()

		#initialize _curve_custom_profile node group
		def _curve_custom_profile_node_group():
			_curve_custom_profile = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".curve_custom_profile")

			_curve_custom_profile.color_tag = 'NONE'
			_curve_custom_profile.description = ""

			_curve_custom_profile.is_modifier = True
			
			#_curve_custom_profile interface
			#Socket Geometry
			geometry_socket = _curve_custom_profile.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket.attribute_domain = 'POINT'
			
			#Socket Curve
			curve_socket = _curve_custom_profile.interface.new_socket(name = "Curve", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			curve_socket.attribute_domain = 'POINT'
			
			#Socket Profile Resolution
			profile_resolution_socket = _curve_custom_profile.interface.new_socket(name = "Profile Resolution", in_out='INPUT', socket_type = 'NodeSocketInt')
			profile_resolution_socket.default_value = 4
			profile_resolution_socket.min_value = 3
			profile_resolution_socket.max_value = 512
			profile_resolution_socket.subtype = 'NONE'
			profile_resolution_socket.attribute_domain = 'POINT'
			
			#Socket Profile Radius
			profile_radius_socket = _curve_custom_profile.interface.new_socket(name = "Profile Radius", in_out='INPUT', socket_type = 'NodeSocketFloat')
			profile_radius_socket.default_value = 1.0
			profile_radius_socket.min_value = 0.0
			profile_radius_socket.max_value = 3.4028234663852886e+38
			profile_radius_socket.subtype = 'DISTANCE'
			profile_radius_socket.attribute_domain = 'POINT'
			
			#Socket Profile Rotation
			profile_rotation_socket = _curve_custom_profile.interface.new_socket(name = "Profile Rotation", in_out='INPUT', socket_type = 'NodeSocketFloat')
			profile_rotation_socket.default_value = 0.7853981852531433
			profile_rotation_socket.min_value = -10000.0
			profile_rotation_socket.max_value = 10000.0
			profile_rotation_socket.subtype = 'NONE'
			profile_rotation_socket.attribute_domain = 'POINT'
			
			#Socket Instance
			instance_socket = _curve_custom_profile.interface.new_socket(name = "Instance", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			instance_socket.attribute_domain = 'POINT'
			
			#Socket Rotation X
			rotation_x_socket = _curve_custom_profile.interface.new_socket(name = "Rotation X", in_out='INPUT', socket_type = 'NodeSocketFloat')
			rotation_x_socket.default_value = 0.0
			rotation_x_socket.min_value = -3.4028234663852886e+38
			rotation_x_socket.max_value = 3.4028234663852886e+38
			rotation_x_socket.subtype = 'ANGLE'
			rotation_x_socket.attribute_domain = 'POINT'
			
			#Socket Scale
			scale_socket = _curve_custom_profile.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketVector')
			scale_socket.default_value = (0.33000001311302185, 0.36000001430511475, 0.75)
			scale_socket.min_value = -3.4028234663852886e+38
			scale_socket.max_value = 3.4028234663852886e+38
			scale_socket.subtype = 'XYZ'
			scale_socket.attribute_domain = 'POINT'
			
			#Socket Factor
			factor_socket = _curve_custom_profile.interface.new_socket(name = "Factor", in_out='INPUT', socket_type = 'NodeSocketFloat')
			factor_socket.default_value = 0.0
			factor_socket.min_value = 0.0
			factor_socket.max_value = 1.0
			factor_socket.subtype = 'FACTOR'
			factor_socket.attribute_domain = 'POINT'
			
			#Socket Radius
			radius_socket_1 = _curve_custom_profile.interface.new_socket(name = "Radius", in_out='INPUT', socket_type = 'NodeSocketFloat')
			radius_socket_1.default_value = 0.004999999888241291
			radius_socket_1.min_value = 0.0
			radius_socket_1.max_value = 3.4028234663852886e+38
			radius_socket_1.subtype = 'DISTANCE'
			radius_socket_1.attribute_domain = 'POINT'
			
			#Socket Resolution
			resolution_socket_1 = _curve_custom_profile.interface.new_socket(name = "Resolution", in_out='INPUT', socket_type = 'NodeSocketInt')
			resolution_socket_1.default_value = 6
			resolution_socket_1.min_value = 1
			resolution_socket_1.max_value = 2147483647
			resolution_socket_1.subtype = 'NONE'
			resolution_socket_1.attribute_domain = 'POINT'
			
			#Socket Resample
			resample_socket = _curve_custom_profile.interface.new_socket(name = "Resample", in_out='INPUT', socket_type = 'NodeSocketBool')
			resample_socket.default_value = False
			resample_socket.attribute_domain = 'POINT'
			
			
			#initialize _curve_custom_profile nodes
			#node Instance on Points.001
			instance_on_points_001 = _curve_custom_profile.nodes.new("GeometryNodeInstanceOnPoints")
			instance_on_points_001.name = "Instance on Points.001"
			#Selection
			instance_on_points_001.inputs[1].default_value = True
			#Pick Instance
			instance_on_points_001.inputs[3].default_value = False
			#Instance Index
			instance_on_points_001.inputs[4].default_value = 0
			
			#node Sample Index.001
			sample_index_001 = _curve_custom_profile.nodes.new("GeometryNodeSampleIndex")
			sample_index_001.name = "Sample Index.001"
			sample_index_001.clamp = False
			sample_index_001.data_type = 'FLOAT_VECTOR'
			sample_index_001.domain = 'POINT'
			
			#node Realize Instances
			realize_instances = _curve_custom_profile.nodes.new("GeometryNodeRealizeInstances")
			realize_instances.name = "Realize Instances"
			#Selection
			realize_instances.inputs[1].default_value = True
			#Realize All
			realize_instances.inputs[2].default_value = True
			#Depth
			realize_instances.inputs[3].default_value = 0
			
			#node Index.003
			index_003 = _curve_custom_profile.nodes.new("GeometryNodeInputIndex")
			index_003.name = "Index.003"
			
			#node Position.001
			position_001 = _curve_custom_profile.nodes.new("GeometryNodeInputPosition")
			position_001.name = "Position.001"
			
			#node Curve to Mesh
			curve_to_mesh = _curve_custom_profile.nodes.new("GeometryNodeCurveToMesh")
			curve_to_mesh.name = "Curve to Mesh"
			#Fill Caps
			curve_to_mesh.inputs[2].default_value = True
			
			#node Set Position.002
			set_position_002 = _curve_custom_profile.nodes.new("GeometryNodeSetPosition")
			set_position_002.name = "Set Position.002"
			#Selection
			set_position_002.inputs[1].default_value = True
			#Offset
			set_position_002.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Transform Geometry
			transform_geometry = _curve_custom_profile.nodes.new("GeometryNodeTransform")
			transform_geometry.name = "Transform Geometry"
			transform_geometry.hide = True
			transform_geometry.mode = 'COMPONENTS'
			#Translation
			transform_geometry.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Rotation
			transform_geometry.inputs[2].default_value = (0.0, 1.5707963705062866, 0.0)
			#Scale
			transform_geometry.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Mix.001
			mix_001 = _curve_custom_profile.nodes.new("ShaderNodeMix")
			mix_001.name = "Mix.001"
			mix_001.blend_type = 'MIX'
			mix_001.clamp_factor = True
			mix_001.clamp_result = False
			mix_001.data_type = 'VECTOR'
			mix_001.factor_mode = 'UNIFORM'
			
			#node Flip Faces
			flip_faces = _curve_custom_profile.nodes.new("GeometryNodeFlipFaces")
			flip_faces.name = "Flip Faces"
			#Selection
			flip_faces.inputs[1].default_value = True
			
			#node Group Output
			group_output_4 = _curve_custom_profile.nodes.new("NodeGroupOutput")
			group_output_4.name = "Group Output"
			group_output_4.is_active_output = True
			
			#node Reroute.001
			reroute_001_1 = _curve_custom_profile.nodes.new("NodeReroute")
			reroute_001_1.name = "Reroute.001"
			#node Reroute
			reroute_1 = _curve_custom_profile.nodes.new("NodeReroute")
			reroute_1.name = "Reroute"
			#node Set Curve Radius
			set_curve_radius = _curve_custom_profile.nodes.new("GeometryNodeSetCurveRadius")
			set_curve_radius.name = "Set Curve Radius"
			#Selection
			set_curve_radius.inputs[1].default_value = True
			
			#node Reroute.002
			reroute_002 = _curve_custom_profile.nodes.new("NodeReroute")
			reroute_002.name = "Reroute.002"
			#node Spline Resolution
			spline_resolution = _curve_custom_profile.nodes.new("GeometryNodeInputSplineResolution")
			spline_resolution.name = "Spline Resolution"
			
			#node Spline Length
			spline_length = _curve_custom_profile.nodes.new("GeometryNodeSplineLength")
			spline_length.name = "Spline Length"
			
			#node Spline Parameter
			spline_parameter = _curve_custom_profile.nodes.new("GeometryNodeSplineParameter")
			spline_parameter.name = "Spline Parameter"
			
			#node Group.001
			group_001 = _curve_custom_profile.nodes.new("GeometryNodeGroup")
			group_001.name = "Group.001"
			group_001.node_tree = _curve_profile_backup
			
			#node Set Spline Resolution
			set_spline_resolution = _curve_custom_profile.nodes.new("GeometryNodeSetSplineResolution")
			set_spline_resolution.name = "Set Spline Resolution"
			#Selection
			set_spline_resolution.inputs[1].default_value = True
			
			#node Resample Curve
			resample_curve = _curve_custom_profile.nodes.new("GeometryNodeResampleCurve")
			resample_curve.name = "Resample Curve"
			resample_curve.mode = 'EVALUATED'
			#Selection
			resample_curve.inputs[1].default_value = True
			
			#node Switch
			switch_1 = _curve_custom_profile.nodes.new("GeometryNodeSwitch")
			switch_1.name = "Switch"
			switch_1.input_type = 'GEOMETRY'
			
			#node Group Input
			group_input_3 = _curve_custom_profile.nodes.new("NodeGroupInput")
			group_input_3.name = "Group Input"
			
			#node Group
			group_2 = _curve_custom_profile.nodes.new("GeometryNodeGroup")
			group_2.name = "Group"
			group_2.node_tree = _guide_rotation
			
			
			
			
			#Set locations
			instance_on_points_001.location = (-289.36962890625, 170.0)
			sample_index_001.location = (-89.36962890625, 290.0)
			realize_instances.location = (-89.36962890625, 70.0)
			index_003.location = (-290.0, 270.0)
			position_001.location = (-290.0, 330.0)
			curve_to_mesh.location = (-100.0, -100.0)
			set_position_002.location = (260.0, 280.0)
			transform_geometry.location = (-520.0, -120.0)
			mix_001.location = (70.63037109375, 290.0)
			flip_faces.location = (460.0, 280.0)
			group_output_4.location = (660.0, 280.0)
			reroute_001_1.location = (-140.0, -240.0)
			reroute_1.location = (-539.885986328125, -222.59783935546875)
			set_curve_radius.location = (-296.1637268066406, -66.46692657470703)
			reroute_002.location = (-635.73388671875, -6.497833251953125)
			spline_resolution.location = (-1100.0, 280.0)
			spline_length.location = (-1100.0, 220.0)
			spline_parameter.location = (-1100.0, 380.0)
			group_001.location = (-900.0, -100.0)
			set_spline_resolution.location = (-1292.002685546875, 99.56741333007812)
			resample_curve.location = (-1124.6309814453125, 107.74668884277344)
			switch_1.location = (-905.0, 111.8224105834961)
			group_input_3.location = (-1608.1519775390625, -81.00050354003906)
			group_2.location = (-500.0, 60.0)
			
			#Set dimensions
			instance_on_points_001.width, instance_on_points_001.height = 140.0, 100.0
			sample_index_001.width, sample_index_001.height = 140.0, 100.0
			realize_instances.width, realize_instances.height = 140.0, 100.0
			index_003.width, index_003.height = 140.0, 100.0
			position_001.width, position_001.height = 140.0, 100.0
			curve_to_mesh.width, curve_to_mesh.height = 140.0, 100.0
			set_position_002.width, set_position_002.height = 140.0, 100.0
			transform_geometry.width, transform_geometry.height = 140.0, 100.0
			mix_001.width, mix_001.height = 140.0, 100.0
			flip_faces.width, flip_faces.height = 140.0, 100.0
			group_output_4.width, group_output_4.height = 140.0, 100.0
			reroute_001_1.width, reroute_001_1.height = 16.0, 100.0
			reroute_1.width, reroute_1.height = 16.0, 100.0
			set_curve_radius.width, set_curve_radius.height = 140.0, 100.0
			reroute_002.width, reroute_002.height = 16.0, 100.0
			spline_resolution.width, spline_resolution.height = 140.0, 100.0
			spline_length.width, spline_length.height = 140.0, 100.0
			spline_parameter.width, spline_parameter.height = 140.0, 100.0
			group_001.width, group_001.height = 140.0, 100.0
			set_spline_resolution.width, set_spline_resolution.height = 140.0, 100.0
			resample_curve.width, resample_curve.height = 140.0, 100.0
			switch_1.width, switch_1.height = 140.0, 100.0
			group_input_3.width, group_input_3.height = 140.0, 100.0
			group_2.width, group_2.height = 140.0, 100.0
			
			#initialize _curve_custom_profile links
			#mix_001.Result -> set_position_002.Position
			_curve_custom_profile.links.new(mix_001.outputs[1], set_position_002.inputs[2])
			#index_003.Index -> sample_index_001.Index
			_curve_custom_profile.links.new(index_003.outputs[0], sample_index_001.inputs[2])
			#position_001.Position -> mix_001.B
			_curve_custom_profile.links.new(position_001.outputs[0], mix_001.inputs[5])
			#set_curve_radius.Curve -> curve_to_mesh.Curve
			_curve_custom_profile.links.new(set_curve_radius.outputs[0], curve_to_mesh.inputs[0])
			#curve_to_mesh.Mesh -> set_position_002.Geometry
			_curve_custom_profile.links.new(curve_to_mesh.outputs[0], set_position_002.inputs[0])
			#instance_on_points_001.Instances -> realize_instances.Geometry
			_curve_custom_profile.links.new(instance_on_points_001.outputs[0], realize_instances.inputs[0])
			#sample_index_001.Value -> mix_001.A
			_curve_custom_profile.links.new(sample_index_001.outputs[0], mix_001.inputs[4])
			#position_001.Position -> sample_index_001.Value
			_curve_custom_profile.links.new(position_001.outputs[0], sample_index_001.inputs[1])
			#realize_instances.Geometry -> sample_index_001.Geometry
			_curve_custom_profile.links.new(realize_instances.outputs[0], sample_index_001.inputs[0])
			#group_input_3.Radius -> set_curve_radius.Radius
			_curve_custom_profile.links.new(group_input_3.outputs[8], set_curve_radius.inputs[2])
			#group_input_3.Factor -> mix_001.Factor
			_curve_custom_profile.links.new(group_input_3.outputs[7], mix_001.inputs[0])
			#flip_faces.Mesh -> group_output_4.Geometry
			_curve_custom_profile.links.new(flip_faces.outputs[0], group_output_4.inputs[0])
			#reroute_1.Output -> transform_geometry.Geometry
			_curve_custom_profile.links.new(reroute_1.outputs[0], transform_geometry.inputs[0])
			#transform_geometry.Geometry -> instance_on_points_001.Instance
			_curve_custom_profile.links.new(transform_geometry.outputs[0], instance_on_points_001.inputs[2])
			#reroute_001_1.Output -> curve_to_mesh.Profile Curve
			_curve_custom_profile.links.new(reroute_001_1.outputs[0], curve_to_mesh.inputs[1])
			#group_input_3.Scale -> instance_on_points_001.Scale
			_curve_custom_profile.links.new(group_input_3.outputs[6], instance_on_points_001.inputs[6])
			#group_input_3.Rotation X -> group_2.Angle
			_curve_custom_profile.links.new(group_input_3.outputs[5], group_2.inputs[0])
			#group_001.Output -> reroute_1.Input
			_curve_custom_profile.links.new(group_001.outputs[0], reroute_1.inputs[0])
			#group_input_3.Instance -> group_001.Input
			_curve_custom_profile.links.new(group_input_3.outputs[4], group_001.inputs[0])
			#group_input_3.Profile Radius -> group_001.Radius
			_curve_custom_profile.links.new(group_input_3.outputs[2], group_001.inputs[2])
			#group_input_3.Profile Rotation -> group_001.Rotation
			_curve_custom_profile.links.new(group_input_3.outputs[3], group_001.inputs[3])
			#set_position_002.Geometry -> flip_faces.Mesh
			_curve_custom_profile.links.new(set_position_002.outputs[0], flip_faces.inputs[0])
			#reroute_002.Output -> set_curve_radius.Curve
			_curve_custom_profile.links.new(reroute_002.outputs[0], set_curve_radius.inputs[0])
			#reroute_1.Output -> reroute_001_1.Input
			_curve_custom_profile.links.new(reroute_1.outputs[0], reroute_001_1.inputs[0])
			#group_input_3.Curve -> set_spline_resolution.Geometry
			_curve_custom_profile.links.new(group_input_3.outputs[0], set_spline_resolution.inputs[0])
			#switch_1.Output -> reroute_002.Input
			_curve_custom_profile.links.new(switch_1.outputs[0], reroute_002.inputs[0])
			#group_input_3.Profile Resolution -> group_001.Resolution
			_curve_custom_profile.links.new(group_input_3.outputs[1], group_001.inputs[1])
			#reroute_002.Output -> instance_on_points_001.Points
			_curve_custom_profile.links.new(reroute_002.outputs[0], instance_on_points_001.inputs[0])
			#group_input_3.Resolution -> set_spline_resolution.Resolution
			_curve_custom_profile.links.new(group_input_3.outputs[9], set_spline_resolution.inputs[2])
			#set_spline_resolution.Geometry -> resample_curve.Curve
			_curve_custom_profile.links.new(set_spline_resolution.outputs[0], resample_curve.inputs[0])
			#group_2.Rotation -> instance_on_points_001.Rotation
			_curve_custom_profile.links.new(group_2.outputs[0], instance_on_points_001.inputs[5])
			#resample_curve.Curve -> switch_1.True
			_curve_custom_profile.links.new(resample_curve.outputs[0], switch_1.inputs[2])
			#group_input_3.Curve -> switch_1.False
			_curve_custom_profile.links.new(group_input_3.outputs[0], switch_1.inputs[1])
			#group_input_3.Resample -> switch_1.Switch
			_curve_custom_profile.links.new(group_input_3.outputs[10], switch_1.inputs[0])
			return _curve_custom_profile

		_curve_custom_profile = _curve_custom_profile_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".curve_custom_profile", type = 'NODES')
		mod.node_group = _curve_custom_profile
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_curve_custom_profile.bl_idname)
			
def register():
	bpy.utils.register_class(_curve_custom_profile)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_curve_custom_profile)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
