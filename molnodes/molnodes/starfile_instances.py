bl_info = {
	"name" : "Starfile Instances",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Starfile_Instances(bpy.types.Operator):
	bl_idname = "node.starfile_instances"
	bl_label = "Starfile Instances"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize utils_zyz_to_rotation node group
		def utils_zyz_to_rotation_node_group():
			utils_zyz_to_rotation = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Utils ZYZ to Rotation")

			utils_zyz_to_rotation.color_tag = 'CONVERTER'
			utils_zyz_to_rotation.description = ""

			
			#utils_zyz_to_rotation interface
			#Socket Rotation
			rotation_socket = utils_zyz_to_rotation.interface.new_socket(name = "Rotation", in_out='OUTPUT', socket_type = 'NodeSocketRotation')
			rotation_socket.attribute_domain = 'POINT'
			
			#Socket Phi
			phi_socket = utils_zyz_to_rotation.interface.new_socket(name = "Phi", in_out='INPUT', socket_type = 'NodeSocketFloat')
			phi_socket.subtype = 'NONE'
			phi_socket.default_value = 0.5
			phi_socket.min_value = -10000.0
			phi_socket.max_value = 10000.0
			phi_socket.attribute_domain = 'POINT'
			
			#Socket Theta
			theta_socket = utils_zyz_to_rotation.interface.new_socket(name = "Theta", in_out='INPUT', socket_type = 'NodeSocketFloat')
			theta_socket.subtype = 'NONE'
			theta_socket.default_value = 0.5
			theta_socket.min_value = -10000.0
			theta_socket.max_value = 10000.0
			theta_socket.attribute_domain = 'POINT'
			
			#Socket Psi
			psi_socket = utils_zyz_to_rotation.interface.new_socket(name = "Psi", in_out='INPUT', socket_type = 'NodeSocketFloat')
			psi_socket.subtype = 'NONE'
			psi_socket.default_value = 0.5
			psi_socket.min_value = -10000.0
			psi_socket.max_value = 10000.0
			psi_socket.attribute_domain = 'POINT'
			
			
			#initialize utils_zyz_to_rotation nodes
			#node Math.002
			math_002 = utils_zyz_to_rotation.nodes.new("ShaderNodeMath")
			math_002.name = "Math.002"
			math_002.operation = 'RADIANS'
			math_002.use_clamp = False
			
			#node Rotation to Euler.001
			rotation_to_euler_001 = utils_zyz_to_rotation.nodes.new("FunctionNodeRotationToEuler")
			rotation_to_euler_001.name = "Rotation to Euler.001"
			
			#node Axis Angle to Rotation.001
			axis_angle_to_rotation_001 = utils_zyz_to_rotation.nodes.new("FunctionNodeAxisAngleToRotation")
			axis_angle_to_rotation_001.name = "Axis Angle to Rotation.001"
			#Axis
			axis_angle_to_rotation_001.inputs[0].default_value = (0.0, 1.0, 0.0)
			
			#node Math.003
			math_003 = utils_zyz_to_rotation.nodes.new("ShaderNodeMath")
			math_003.name = "Math.003"
			math_003.operation = 'MULTIPLY'
			math_003.use_clamp = False
			#Value_001
			math_003.inputs[1].default_value = -1.0
			
			#node Rotate Euler
			rotate_euler = utils_zyz_to_rotation.nodes.new("FunctionNodeRotateEuler")
			rotate_euler.name = "Rotate Euler"
			rotate_euler.rotation_type = 'EULER'
			rotate_euler.space = 'OBJECT'
			
			#node Rotation to Euler
			rotation_to_euler = utils_zyz_to_rotation.nodes.new("FunctionNodeRotationToEuler")
			rotation_to_euler.name = "Rotation to Euler"
			
			#node Axis Angle to Rotation
			axis_angle_to_rotation = utils_zyz_to_rotation.nodes.new("FunctionNodeAxisAngleToRotation")
			axis_angle_to_rotation.name = "Axis Angle to Rotation"
			#Axis
			axis_angle_to_rotation.inputs[0].default_value = (0.0, 0.0, 1.0)
			
			#node Math.004
			math_004 = utils_zyz_to_rotation.nodes.new("ShaderNodeMath")
			math_004.name = "Math.004"
			math_004.operation = 'MULTIPLY'
			math_004.use_clamp = False
			#Value_001
			math_004.inputs[1].default_value = -1.0
			
			#node Math.005
			math_005 = utils_zyz_to_rotation.nodes.new("ShaderNodeMath")
			math_005.name = "Math.005"
			math_005.operation = 'RADIANS'
			math_005.use_clamp = False
			
			#node Rotation to Euler.002
			rotation_to_euler_002 = utils_zyz_to_rotation.nodes.new("FunctionNodeRotationToEuler")
			rotation_to_euler_002.name = "Rotation to Euler.002"
			
			#node Axis Angle to Rotation.002
			axis_angle_to_rotation_002 = utils_zyz_to_rotation.nodes.new("FunctionNodeAxisAngleToRotation")
			axis_angle_to_rotation_002.name = "Axis Angle to Rotation.002"
			#Axis
			axis_angle_to_rotation_002.inputs[0].default_value = (0.0, 0.0, 1.0)
			
			#node Math.006
			math_006 = utils_zyz_to_rotation.nodes.new("ShaderNodeMath")
			math_006.name = "Math.006"
			math_006.operation = 'MULTIPLY'
			math_006.use_clamp = False
			#Value_001
			math_006.inputs[1].default_value = -1.0
			
			#node Rotate Euler.001
			rotate_euler_001 = utils_zyz_to_rotation.nodes.new("FunctionNodeRotateEuler")
			rotate_euler_001.name = "Rotate Euler.001"
			rotate_euler_001.rotation_type = 'EULER'
			rotate_euler_001.space = 'OBJECT'
			
			#node Group Output
			group_output = utils_zyz_to_rotation.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Euler to Rotation
			euler_to_rotation = utils_zyz_to_rotation.nodes.new("FunctionNodeEulerToRotation")
			euler_to_rotation.name = "Euler to Rotation"
			
			#node Math.001
			math_001 = utils_zyz_to_rotation.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.operation = 'RADIANS'
			math_001.use_clamp = False
			
			#node Group Input
			group_input = utils_zyz_to_rotation.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			
			
			
			#Set locations
			math_002.location = (-694.4244995117188, -84.2993392944336)
			rotation_to_euler_001.location = (-10.165328979492188, 35.051002502441406)
			axis_angle_to_rotation_001.location = (-253.7509002685547, -19.897422790527344)
			math_003.location = (-474.16217041015625, -123.19185638427734)
			rotate_euler.location = (164.9982452392578, 342.89154052734375)
			rotation_to_euler.location = (-93.54765319824219, 256.75140380859375)
			axis_angle_to_rotation.location = (-258.35333251953125, 220.27224731445312)
			math_004.location = (-478.16180419921875, 154.58316040039062)
			math_005.location = (-658.0630493164062, -378.8916931152344)
			rotation_to_euler_002.location = (-53.87699890136719, -285.2621765136719)
			axis_angle_to_rotation_002.location = (-218.6826629638672, -321.7413024902344)
			math_006.location = (-438.49114990234375, -387.4303894042969)
			rotate_euler_001.location = (430.89129638671875, 252.57174682617188)
			group_output.location = (1071.1878662109375, 143.63784790039062)
			euler_to_rotation.location = (641.1380615234375, 110.34000396728516)
			math_001.location = (-697.7337036132812, 163.12179565429688)
			group_input.location = (-924.5353393554688, -5.580089569091797)
			
			#Set dimensions
			math_002.width, math_002.height = 140.0, 100.0
			rotation_to_euler_001.width, rotation_to_euler_001.height = 140.0, 100.0
			axis_angle_to_rotation_001.width, axis_angle_to_rotation_001.height = 140.0, 100.0
			math_003.width, math_003.height = 140.0, 100.0
			rotate_euler.width, rotate_euler.height = 140.0, 100.0
			rotation_to_euler.width, rotation_to_euler.height = 140.0, 100.0
			axis_angle_to_rotation.width, axis_angle_to_rotation.height = 140.0, 100.0
			math_004.width, math_004.height = 140.0, 100.0
			math_005.width, math_005.height = 140.0, 100.0
			rotation_to_euler_002.width, rotation_to_euler_002.height = 140.0, 100.0
			axis_angle_to_rotation_002.width, axis_angle_to_rotation_002.height = 140.0, 100.0
			math_006.width, math_006.height = 140.0, 100.0
			rotate_euler_001.width, rotate_euler_001.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			euler_to_rotation.width, euler_to_rotation.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			
			#initialize utils_zyz_to_rotation links
			#math_006.Value -> axis_angle_to_rotation_002.Angle
			utils_zyz_to_rotation.links.new(math_006.outputs[0], axis_angle_to_rotation_002.inputs[1])
			#rotation_to_euler.Euler -> rotate_euler.Rotation
			utils_zyz_to_rotation.links.new(rotation_to_euler.outputs[0], rotate_euler.inputs[0])
			#axis_angle_to_rotation_002.Rotation -> rotation_to_euler_002.Rotation
			utils_zyz_to_rotation.links.new(axis_angle_to_rotation_002.outputs[0], rotation_to_euler_002.inputs[0])
			#rotate_euler.Rotation -> rotate_euler_001.Rotation
			utils_zyz_to_rotation.links.new(rotate_euler.outputs[0], rotate_euler_001.inputs[0])
			#rotation_to_euler_002.Euler -> rotate_euler_001.Rotate By
			utils_zyz_to_rotation.links.new(rotation_to_euler_002.outputs[0], rotate_euler_001.inputs[1])
			#math_005.Value -> math_006.Value
			utils_zyz_to_rotation.links.new(math_005.outputs[0], math_006.inputs[0])
			#axis_angle_to_rotation_001.Rotation -> rotation_to_euler_001.Rotation
			utils_zyz_to_rotation.links.new(axis_angle_to_rotation_001.outputs[0], rotation_to_euler_001.inputs[0])
			#math_003.Value -> axis_angle_to_rotation_001.Angle
			utils_zyz_to_rotation.links.new(math_003.outputs[0], axis_angle_to_rotation_001.inputs[1])
			#math_004.Value -> axis_angle_to_rotation.Angle
			utils_zyz_to_rotation.links.new(math_004.outputs[0], axis_angle_to_rotation.inputs[1])
			#math_001.Value -> math_004.Value
			utils_zyz_to_rotation.links.new(math_001.outputs[0], math_004.inputs[0])
			#rotation_to_euler_001.Euler -> rotate_euler.Rotate By
			utils_zyz_to_rotation.links.new(rotation_to_euler_001.outputs[0], rotate_euler.inputs[1])
			#axis_angle_to_rotation.Rotation -> rotation_to_euler.Rotation
			utils_zyz_to_rotation.links.new(axis_angle_to_rotation.outputs[0], rotation_to_euler.inputs[0])
			#math_002.Value -> math_003.Value
			utils_zyz_to_rotation.links.new(math_002.outputs[0], math_003.inputs[0])
			#rotate_euler_001.Rotation -> euler_to_rotation.Euler
			utils_zyz_to_rotation.links.new(rotate_euler_001.outputs[0], euler_to_rotation.inputs[0])
			#euler_to_rotation.Rotation -> group_output.Rotation
			utils_zyz_to_rotation.links.new(euler_to_rotation.outputs[0], group_output.inputs[0])
			#group_input.Theta -> math_002.Value
			utils_zyz_to_rotation.links.new(group_input.outputs[1], math_002.inputs[0])
			#group_input.Phi -> math_001.Value
			utils_zyz_to_rotation.links.new(group_input.outputs[0], math_001.inputs[0])
			#group_input.Psi -> math_005.Value
			utils_zyz_to_rotation.links.new(group_input.outputs[2], math_005.inputs[0])
			return utils_zyz_to_rotation

		utils_zyz_to_rotation = utils_zyz_to_rotation_node_group()

		#initialize mn_starfile_micrograph node group
		def mn_starfile_micrograph_node_group():
			mn_starfile_micrograph = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "MN_Starfile_Micrograph")

			mn_starfile_micrograph.color_tag = 'NONE'
			mn_starfile_micrograph.description = ""

			
			#mn_starfile_micrograph interface
			#Socket Output
			output_socket = mn_starfile_micrograph.interface.new_socket(name = "Output", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			output_socket.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket = mn_starfile_micrograph.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket.attribute_domain = 'POINT'
			
			#Socket Switch
			switch_socket = mn_starfile_micrograph.interface.new_socket(name = "Switch", in_out='INPUT', socket_type = 'NodeSocketBool')
			switch_socket.attribute_domain = 'POINT'
			
			#Socket Image
			image_socket = mn_starfile_micrograph.interface.new_socket(name = "Image", in_out='INPUT', socket_type = 'NodeSocketImage')
			image_socket.attribute_domain = 'POINT'
			
			#Socket A
			a_socket = mn_starfile_micrograph.interface.new_socket(name = "A", in_out='INPUT', socket_type = 'NodeSocketFloat')
			a_socket.subtype = 'NONE'
			a_socket.default_value = 0.0
			a_socket.min_value = -10000.0
			a_socket.max_value = 10000.0
			a_socket.attribute_domain = 'POINT'
			
			#Socket Z
			z_socket = mn_starfile_micrograph.interface.new_socket(name = "Z", in_out='INPUT', socket_type = 'NodeSocketFloat')
			z_socket.subtype = 'NONE'
			z_socket.default_value = 0.0
			z_socket.min_value = -10000.0
			z_socket.max_value = 10000.0
			z_socket.attribute_domain = 'POINT'
			
			#Socket Brightness
			brightness_socket = mn_starfile_micrograph.interface.new_socket(name = "Brightness", in_out='INPUT', socket_type = 'NodeSocketFloat')
			brightness_socket.subtype = 'NONE'
			brightness_socket.default_value = 0.0
			brightness_socket.min_value = -3.4028234663852886e+38
			brightness_socket.max_value = 3.4028234663852886e+38
			brightness_socket.attribute_domain = 'POINT'
			
			#Socket Contrast
			contrast_socket = mn_starfile_micrograph.interface.new_socket(name = "Contrast", in_out='INPUT', socket_type = 'NodeSocketFloat')
			contrast_socket.subtype = 'NONE'
			contrast_socket.default_value = 0.0
			contrast_socket.min_value = -3.4028234663852886e+38
			contrast_socket.max_value = 3.4028234663852886e+38
			contrast_socket.attribute_domain = 'POINT'
			
			
			#initialize mn_starfile_micrograph nodes
			#node Grid
			grid = mn_starfile_micrograph.nodes.new("GeometryNodeMeshGrid")
			grid.name = "Grid"
			#Size X
			grid.inputs[0].default_value = 1.0
			#Size Y
			grid.inputs[1].default_value = 1.0
			#Vertices X
			grid.inputs[2].default_value = 2
			#Vertices Y
			grid.inputs[3].default_value = 2
			
			#node Transform Geometry.006
			transform_geometry_006 = mn_starfile_micrograph.nodes.new("GeometryNodeTransform")
			transform_geometry_006.name = "Transform Geometry.006"
			transform_geometry_006.mode = 'COMPONENTS'
			#Translation
			transform_geometry_006.inputs[1].default_value = (0.5, 0.5, 0.0)
			#Rotation
			transform_geometry_006.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Scale
			transform_geometry_006.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Transform Geometry.007
			transform_geometry_007 = mn_starfile_micrograph.nodes.new("GeometryNodeTransform")
			transform_geometry_007.name = "Transform Geometry.007"
			transform_geometry_007.mode = 'COMPONENTS'
			#Translation
			transform_geometry_007.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Rotation
			transform_geometry_007.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Transform Geometry.008
			transform_geometry_008 = mn_starfile_micrograph.nodes.new("GeometryNodeTransform")
			transform_geometry_008.name = "Transform Geometry.008"
			transform_geometry_008.mode = 'COMPONENTS'
			#Rotation
			transform_geometry_008.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Scale
			transform_geometry_008.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Image Info
			image_info = mn_starfile_micrograph.nodes.new("GeometryNodeImageInfo")
			image_info.name = "Image Info"
			#Frame
			image_info.inputs[1].default_value = 0
			
			#node Combine XYZ.002
			combine_xyz_002 = mn_starfile_micrograph.nodes.new("ShaderNodeCombineXYZ")
			combine_xyz_002.name = "Combine XYZ.002"
			#X
			combine_xyz_002.inputs[0].default_value = 0.0
			#Y
			combine_xyz_002.inputs[1].default_value = 0.0
			
			#node Combine XYZ.001
			combine_xyz_001 = mn_starfile_micrograph.nodes.new("ShaderNodeCombineXYZ")
			combine_xyz_001.name = "Combine XYZ.001"
			#Z
			combine_xyz_001.inputs[2].default_value = 0.0
			
			#node Named Attribute.004
			named_attribute_004 = mn_starfile_micrograph.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_004.name = "Named Attribute.004"
			named_attribute_004.data_type = 'FLOAT'
			#Name
			named_attribute_004.inputs[0].default_value = "MNPixelSize"
			
			#node Attribute Statistic.002
			attribute_statistic_002 = mn_starfile_micrograph.nodes.new("GeometryNodeAttributeStatistic")
			attribute_statistic_002.name = "Attribute Statistic.002"
			attribute_statistic_002.data_type = 'FLOAT'
			attribute_statistic_002.domain = 'POINT'
			#Selection
			attribute_statistic_002.inputs[1].default_value = True
			
			#node Attribute Statistic.001
			attribute_statistic_001 = mn_starfile_micrograph.nodes.new("GeometryNodeAttributeStatistic")
			attribute_statistic_001.name = "Attribute Statistic.001"
			attribute_statistic_001.data_type = 'FLOAT'
			attribute_statistic_001.domain = 'POINT'
			#Selection
			attribute_statistic_001.inputs[1].default_value = True
			
			#node Switch.003
			switch_003 = mn_starfile_micrograph.nodes.new("GeometryNodeSwitch")
			switch_003.name = "Switch.003"
			switch_003.input_type = 'FLOAT'
			#False
			switch_003.inputs[1].default_value = 1.0
			
			#node Compare.002
			compare_002 = mn_starfile_micrograph.nodes.new("FunctionNodeCompare")
			compare_002.name = "Compare.002"
			compare_002.data_type = 'FLOAT'
			compare_002.mode = 'ELEMENT'
			compare_002.operation = 'GREATER_THAN'
			#B
			compare_002.inputs[1].default_value = 0.0
			
			#node Switch.004
			switch_004 = mn_starfile_micrograph.nodes.new("GeometryNodeSwitch")
			switch_004.name = "Switch.004"
			switch_004.input_type = 'FLOAT'
			
			#node Math.001
			math_001_1 = mn_starfile_micrograph.nodes.new("ShaderNodeMath")
			math_001_1.name = "Math.001"
			math_001_1.operation = 'DIVIDE'
			math_001_1.use_clamp = False
			#Value_001
			math_001_1.inputs[1].default_value = 100.0
			
			#node Vector Math
			vector_math = mn_starfile_micrograph.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.operation = 'MULTIPLY'
			
			#node Group Output
			group_output_1 = mn_starfile_micrograph.nodes.new("NodeGroupOutput")
			group_output_1.name = "Group Output"
			group_output_1.is_active_output = True
			
			#node Switch.002
			switch_002 = mn_starfile_micrograph.nodes.new("GeometryNodeSwitch")
			switch_002.name = "Switch.002"
			switch_002.input_type = 'GEOMETRY'
			
			#node Set Material
			set_material = mn_starfile_micrograph.nodes.new("GeometryNodeSetMaterial")
			set_material.name = "Set Material"
			#Selection
			set_material.inputs[1].default_value = True
			if "MN_micrograph_material" in bpy.data.materials:
				set_material.inputs[2].default_value = bpy.data.materials["MN_micrograph_material"]
			
			#node Store Named Attribute.001
			store_named_attribute_001 = mn_starfile_micrograph.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_001.name = "Store Named Attribute.001"
			store_named_attribute_001.data_type = 'FLOAT'
			store_named_attribute_001.domain = 'POINT'
			#Selection
			store_named_attribute_001.inputs[1].default_value = True
			#Name
			store_named_attribute_001.inputs[2].default_value = "MNContrast"
			
			#node Group Input
			group_input_1 = mn_starfile_micrograph.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			
			#node Store Named Attribute
			store_named_attribute = mn_starfile_micrograph.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute.name = "Store Named Attribute"
			store_named_attribute.data_type = 'FLOAT'
			store_named_attribute.domain = 'POINT'
			#Selection
			store_named_attribute.inputs[1].default_value = True
			#Name
			store_named_attribute.inputs[2].default_value = "MNBrightness"
			
			
			
			
			#Set locations
			grid.location = (-999.37109375, 99.62265014648438)
			transform_geometry_006.location = (-818.5869140625, 126.43045806884766)
			transform_geometry_007.location = (-631.0038452148438, 120.99168395996094)
			transform_geometry_008.location = (-280.42913818359375, 127.88481903076172)
			image_info.location = (-1585.4774169921875, -457.0034484863281)
			combine_xyz_002.location = (-463.28271484375, 19.085479736328125)
			combine_xyz_001.location = (-922.6502075195312, -307.76483154296875)
			named_attribute_004.location = (-1683.5006103515625, -1052.9495849609375)
			attribute_statistic_002.location = (-1112.16845703125, -966.6381225585938)
			attribute_statistic_001.location = (-1105.0552978515625, -612.5789184570312)
			switch_003.location = (-887.4561767578125, -835.5484619140625)
			compare_002.location = (-875.1576538085938, -657.2496948242188)
			switch_004.location = (-661.568359375, -714.772216796875)
			math_001_1.location = (-466.16815185546875, -596.7671508789062)
			vector_math.location = (-592.4921875, -338.4251403808594)
			group_output_1.location = (754.4419555664062, 429.34814453125)
			switch_002.location = (502.57647705078125, 427.40423583984375)
			set_material.location = (380.0, 200.0)
			store_named_attribute_001.location = (160.0, 140.0)
			group_input_1.location = (-1467.8316650390625, -14.638721466064453)
			store_named_attribute.location = (-60.0, 160.0)
			
			#Set dimensions
			grid.width, grid.height = 140.0, 100.0
			transform_geometry_006.width, transform_geometry_006.height = 140.0, 100.0
			transform_geometry_007.width, transform_geometry_007.height = 140.0, 100.0
			transform_geometry_008.width, transform_geometry_008.height = 140.0, 100.0
			image_info.width, image_info.height = 240.0, 100.0
			combine_xyz_002.width, combine_xyz_002.height = 140.0, 100.0
			combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
			named_attribute_004.width, named_attribute_004.height = 140.0, 100.0
			attribute_statistic_002.width, attribute_statistic_002.height = 140.0, 100.0
			attribute_statistic_001.width, attribute_statistic_001.height = 140.0, 100.0
			switch_003.width, switch_003.height = 140.0, 100.0
			compare_002.width, compare_002.height = 140.0, 100.0
			switch_004.width, switch_004.height = 140.0, 100.0
			math_001_1.width, math_001_1.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			group_output_1.width, group_output_1.height = 140.0, 100.0
			switch_002.width, switch_002.height = 140.0, 100.0
			set_material.width, set_material.height = 140.0, 100.0
			store_named_attribute_001.width, store_named_attribute_001.height = 140.0, 100.0
			group_input_1.width, group_input_1.height = 140.0, 100.0
			store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
			
			#initialize mn_starfile_micrograph links
			#switch_004.Output -> math_001_1.Value
			mn_starfile_micrograph.links.new(switch_004.outputs[0], math_001_1.inputs[0])
			#attribute_statistic_001.Mean -> switch_003.True
			mn_starfile_micrograph.links.new(attribute_statistic_001.outputs[0], switch_003.inputs[2])
			#compare_002.Result -> switch_004.Switch
			mn_starfile_micrograph.links.new(compare_002.outputs[0], switch_004.inputs[0])
			#combine_xyz_001.Vector -> vector_math.Vector
			mn_starfile_micrograph.links.new(combine_xyz_001.outputs[0], vector_math.inputs[0])
			#switch_003.Output -> switch_004.False
			mn_starfile_micrograph.links.new(switch_003.outputs[0], switch_004.inputs[1])
			#set_material.Geometry -> switch_002.True
			mn_starfile_micrograph.links.new(set_material.outputs[0], switch_002.inputs[2])
			#attribute_statistic_002.Mean -> switch_003.Switch
			mn_starfile_micrograph.links.new(attribute_statistic_002.outputs[0], switch_003.inputs[0])
			#math_001_1.Value -> vector_math.Vector
			mn_starfile_micrograph.links.new(math_001_1.outputs[0], vector_math.inputs[1])
			#transform_geometry_007.Geometry -> transform_geometry_008.Geometry
			mn_starfile_micrograph.links.new(transform_geometry_007.outputs[0], transform_geometry_008.inputs[0])
			#vector_math.Vector -> transform_geometry_007.Scale
			mn_starfile_micrograph.links.new(vector_math.outputs[0], transform_geometry_007.inputs[3])
			#named_attribute_004.Exists -> attribute_statistic_002.Attribute
			mn_starfile_micrograph.links.new(named_attribute_004.outputs[1], attribute_statistic_002.inputs[2])
			#grid.Mesh -> transform_geometry_006.Geometry
			mn_starfile_micrograph.links.new(grid.outputs[0], transform_geometry_006.inputs[0])
			#transform_geometry_006.Geometry -> transform_geometry_007.Geometry
			mn_starfile_micrograph.links.new(transform_geometry_006.outputs[0], transform_geometry_007.inputs[0])
			#image_info.Width -> combine_xyz_001.X
			mn_starfile_micrograph.links.new(image_info.outputs[0], combine_xyz_001.inputs[0])
			#image_info.Height -> combine_xyz_001.Y
			mn_starfile_micrograph.links.new(image_info.outputs[1], combine_xyz_001.inputs[1])
			#combine_xyz_002.Vector -> transform_geometry_008.Translation
			mn_starfile_micrograph.links.new(combine_xyz_002.outputs[0], transform_geometry_008.inputs[1])
			#named_attribute_004.Attribute -> attribute_statistic_001.Attribute
			mn_starfile_micrograph.links.new(named_attribute_004.outputs[0], attribute_statistic_001.inputs[2])
			#group_input_1.A -> compare_002.A
			mn_starfile_micrograph.links.new(group_input_1.outputs[3], compare_002.inputs[0])
			#group_input_1.A -> switch_004.True
			mn_starfile_micrograph.links.new(group_input_1.outputs[3], switch_004.inputs[2])
			#group_input_1.Switch -> switch_002.Switch
			mn_starfile_micrograph.links.new(group_input_1.outputs[1], switch_002.inputs[0])
			#group_input_1.Z -> combine_xyz_002.Z
			mn_starfile_micrograph.links.new(group_input_1.outputs[4], combine_xyz_002.inputs[2])
			#group_input_1.Image -> image_info.Image
			mn_starfile_micrograph.links.new(group_input_1.outputs[2], image_info.inputs[0])
			#group_input_1.Geometry -> attribute_statistic_001.Geometry
			mn_starfile_micrograph.links.new(group_input_1.outputs[0], attribute_statistic_001.inputs[0])
			#group_input_1.Geometry -> attribute_statistic_002.Geometry
			mn_starfile_micrograph.links.new(group_input_1.outputs[0], attribute_statistic_002.inputs[0])
			#switch_002.Output -> group_output_1.Output
			mn_starfile_micrograph.links.new(switch_002.outputs[0], group_output_1.inputs[0])
			#store_named_attribute_001.Geometry -> set_material.Geometry
			mn_starfile_micrograph.links.new(store_named_attribute_001.outputs[0], set_material.inputs[0])
			#transform_geometry_008.Geometry -> store_named_attribute.Geometry
			mn_starfile_micrograph.links.new(transform_geometry_008.outputs[0], store_named_attribute.inputs[0])
			#store_named_attribute.Geometry -> store_named_attribute_001.Geometry
			mn_starfile_micrograph.links.new(store_named_attribute.outputs[0], store_named_attribute_001.inputs[0])
			#group_input_1.Brightness -> store_named_attribute.Value
			mn_starfile_micrograph.links.new(group_input_1.outputs[5], store_named_attribute.inputs[3])
			#group_input_1.Contrast -> store_named_attribute_001.Value
			mn_starfile_micrograph.links.new(group_input_1.outputs[6], store_named_attribute_001.inputs[3])
			return mn_starfile_micrograph

		mn_starfile_micrograph = mn_starfile_micrograph_node_group()

		#initialize starfile_instances node group
		def starfile_instances_node_group():
			starfile_instances = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Starfile Instances")

			starfile_instances.color_tag = 'GEOMETRY'
			starfile_instances.description = ""

			
			#starfile_instances interface
			#Socket Instances
			instances_socket = starfile_instances.interface.new_socket(name = "Instances", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			instances_socket.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_1 = starfile_instances.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_1.attribute_domain = 'POINT'
			
			#Socket Molecule
			molecule_socket = starfile_instances.interface.new_socket(name = "Molecule", in_out='INPUT', socket_type = 'NodeSocketObject')
			molecule_socket.attribute_domain = 'POINT'
			molecule_socket.description = "The object that should be placed at each instance"
			
			#Socket Image
			image_socket_1 = starfile_instances.interface.new_socket(name = "Image", in_out='INPUT', socket_type = 'NodeSocketInt')
			image_socket_1.subtype = 'NONE'
			image_socket_1.default_value = 1
			image_socket_1.min_value = 1
			image_socket_1.max_value = 2147483647
			image_socket_1.attribute_domain = 'POINT'
			image_socket_1.description = "The ID of the image that should be shown"
			
			#Socket Simplify
			simplify_socket = starfile_instances.interface.new_socket(name = "Simplify", in_out='INPUT', socket_type = 'NodeSocketBool')
			simplify_socket.attribute_domain = 'POINT'
			simplify_socket.description = "Place axes instead of Molecule on each instance"
			
			#Socket Show Micrograph
			show_micrograph_socket = starfile_instances.interface.new_socket(name = "Show Micrograph", in_out='INPUT', socket_type = 'NodeSocketBool')
			show_micrograph_socket.attribute_domain = 'POINT'
			show_micrograph_socket.description = "Show the micrograph in addition to the instances"
			
			#Panel Micrograph Options
			micrograph_options_panel = starfile_instances.interface.new_panel("Micrograph Options", default_closed=True)
			#Socket Micrograph
			micrograph_socket = starfile_instances.interface.new_socket(name = "Micrograph", in_out='INPUT', socket_type = 'NodeSocketImage', parent = micrograph_options_panel)
			micrograph_socket.attribute_domain = 'POINT'
			micrograph_socket.description = "The image object used for the micrograph (should be set automatically)"
			
			#Socket Micrograph Pixelsize
			micrograph_pixelsize_socket = starfile_instances.interface.new_socket(name = "Micrograph Pixelsize", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = micrograph_options_panel)
			micrograph_pixelsize_socket.subtype = 'NONE'
			micrograph_pixelsize_socket.default_value = -1.0
			micrograph_pixelsize_socket.min_value = -3.4028234663852886e+38
			micrograph_pixelsize_socket.max_value = 3.4028234663852886e+38
			micrograph_pixelsize_socket.attribute_domain = 'POINT'
			micrograph_pixelsize_socket.description = "Pixelsize of the micrograph (enter a negative number to use value from starfile)"
			
			#Socket Micrograph Z
			micrograph_z_socket = starfile_instances.interface.new_socket(name = "Micrograph Z", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = micrograph_options_panel)
			micrograph_z_socket.subtype = 'NONE'
			micrograph_z_socket.default_value = -10.0
			micrograph_z_socket.min_value = -3.4028234663852886e+38
			micrograph_z_socket.max_value = 3.4028234663852886e+38
			micrograph_z_socket.attribute_domain = 'POINT'
			micrograph_z_socket.description = "Position of the micrograph along the Z axis"
			
			#Socket Brightness
			brightness_socket_1 = starfile_instances.interface.new_socket(name = "Brightness", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = micrograph_options_panel)
			brightness_socket_1.subtype = 'NONE'
			brightness_socket_1.default_value = 0.5
			brightness_socket_1.min_value = 0.0
			brightness_socket_1.max_value = 1.0
			brightness_socket_1.attribute_domain = 'POINT'
			brightness_socket_1.description = "Adjust micrograph brightness"
			
			#Socket Contrast
			contrast_socket_1 = starfile_instances.interface.new_socket(name = "Contrast", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = micrograph_options_panel)
			contrast_socket_1.subtype = 'NONE'
			contrast_socket_1.default_value = 1.0
			contrast_socket_1.min_value = -3.4028234663852886e+38
			contrast_socket_1.max_value = 3.4028234663852886e+38
			contrast_socket_1.attribute_domain = 'POINT'
			contrast_socket_1.description = "Adjust micrograph contrast"
			
			
			
			#initialize starfile_instances nodes
			#node Group Input
			group_input_2 = starfile_instances.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
			#node Math
			math = starfile_instances.nodes.new("ShaderNodeMath")
			math.name = "Math"
			math.operation = 'SUBTRACT'
			math.use_clamp = False
			#Value_001
			math.inputs[1].default_value = 1.0
			
			#node Object Info
			object_info = starfile_instances.nodes.new("GeometryNodeObjectInfo")
			object_info.name = "Object Info"
			object_info.transform_space = 'ORIGINAL'
			#As Instance
			object_info.inputs[1].default_value = False
			
			#node ID
			id = starfile_instances.nodes.new("GeometryNodeInputID")
			id.name = "ID"
			
			#node Attribute Statistic
			attribute_statistic = starfile_instances.nodes.new("GeometryNodeAttributeStatistic")
			attribute_statistic.name = "Attribute Statistic"
			attribute_statistic.data_type = 'FLOAT'
			attribute_statistic.domain = 'POINT'
			#Selection
			attribute_statistic.inputs[1].default_value = True
			
			#node Compare.001
			compare_001 = starfile_instances.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'FLOAT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'EQUAL'
			#B
			compare_001.inputs[1].default_value = 0.0
			#Epsilon
			compare_001.inputs[12].default_value = 0.0010000000474974513
			
			#node Boolean Math
			boolean_math = starfile_instances.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'OR'
			
			#node Switch
			switch = starfile_instances.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'GEOMETRY'
			
			#node Join Geometry.002
			join_geometry_002 = starfile_instances.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_002.name = "Join Geometry.002"
			
			#node Cone.001
			cone_001 = starfile_instances.nodes.new("GeometryNodeMeshCone")
			cone_001.name = "Cone.001"
			cone_001.fill_type = 'NGON'
			#Vertices
			cone_001.inputs[0].default_value = 32
			#Side Segments
			cone_001.inputs[1].default_value = 1
			#Fill Segments
			cone_001.inputs[2].default_value = 1
			#Radius Top
			cone_001.inputs[3].default_value = 0.0
			#Radius Bottom
			cone_001.inputs[4].default_value = 0.30000001192092896
			#Depth
			cone_001.inputs[5].default_value = 0.5
			
			#node Transform Geometry.002
			transform_geometry_002 = starfile_instances.nodes.new("GeometryNodeTransform")
			transform_geometry_002.name = "Transform Geometry.002"
			transform_geometry_002.mode = 'COMPONENTS'
			#Translation
			transform_geometry_002.inputs[1].default_value = (1.0, 0.0, 0.0)
			#Rotation
			transform_geometry_002.inputs[2].default_value = (0.0, 1.5707963705062866, 0.0)
			#Scale
			transform_geometry_002.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Cylinder.001
			cylinder_001 = starfile_instances.nodes.new("GeometryNodeMeshCylinder")
			cylinder_001.name = "Cylinder.001"
			cylinder_001.fill_type = 'NGON'
			#Vertices
			cylinder_001.inputs[0].default_value = 32
			#Side Segments
			cylinder_001.inputs[1].default_value = 1
			#Fill Segments
			cylinder_001.inputs[2].default_value = 1
			#Radius
			cylinder_001.inputs[3].default_value = 0.10000000149011612
			#Depth
			cylinder_001.inputs[4].default_value = 1.0
			
			#node Transform Geometry.003
			transform_geometry_003 = starfile_instances.nodes.new("GeometryNodeTransform")
			transform_geometry_003.name = "Transform Geometry.003"
			transform_geometry_003.mode = 'COMPONENTS'
			#Translation
			transform_geometry_003.inputs[1].default_value = (0.5, 0.0, 0.0)
			#Rotation
			transform_geometry_003.inputs[2].default_value = (0.0, 1.5707963705062866, 0.0)
			#Scale
			transform_geometry_003.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Join Geometry
			join_geometry = starfile_instances.nodes.new("GeometryNodeJoinGeometry")
			join_geometry.name = "Join Geometry"
			
			#node Cone
			cone = starfile_instances.nodes.new("GeometryNodeMeshCone")
			cone.name = "Cone"
			cone.fill_type = 'NGON'
			#Vertices
			cone.inputs[0].default_value = 32
			#Side Segments
			cone.inputs[1].default_value = 1
			#Fill Segments
			cone.inputs[2].default_value = 1
			#Radius Top
			cone.inputs[3].default_value = 0.0
			#Radius Bottom
			cone.inputs[4].default_value = 0.30000001192092896
			#Depth
			cone.inputs[5].default_value = 0.5
			
			#node Transform Geometry.001
			transform_geometry_001 = starfile_instances.nodes.new("GeometryNodeTransform")
			transform_geometry_001.name = "Transform Geometry.001"
			transform_geometry_001.mode = 'COMPONENTS'
			#Translation
			transform_geometry_001.inputs[1].default_value = (0.0, 1.0, 0.0)
			#Rotation
			transform_geometry_001.inputs[2].default_value = (-1.5707963705062866, 0.0, 0.0)
			#Scale
			transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Cylinder
			cylinder = starfile_instances.nodes.new("GeometryNodeMeshCylinder")
			cylinder.name = "Cylinder"
			cylinder.fill_type = 'NGON'
			#Vertices
			cylinder.inputs[0].default_value = 32
			#Side Segments
			cylinder.inputs[1].default_value = 1
			#Fill Segments
			cylinder.inputs[2].default_value = 1
			#Radius
			cylinder.inputs[3].default_value = 0.10000000149011612
			#Depth
			cylinder.inputs[4].default_value = 1.0
			
			#node Transform Geometry
			transform_geometry = starfile_instances.nodes.new("GeometryNodeTransform")
			transform_geometry.name = "Transform Geometry"
			transform_geometry.mode = 'COMPONENTS'
			#Translation
			transform_geometry.inputs[1].default_value = (0.0, 0.5, 0.0)
			#Rotation
			transform_geometry.inputs[2].default_value = (1.5707963705062866, 0.0, 0.0)
			#Scale
			transform_geometry.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Join Geometry.003
			join_geometry_003 = starfile_instances.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_003.name = "Join Geometry.003"
			
			#node Cone.002
			cone_002 = starfile_instances.nodes.new("GeometryNodeMeshCone")
			cone_002.name = "Cone.002"
			cone_002.fill_type = 'NGON'
			#Vertices
			cone_002.inputs[0].default_value = 32
			#Side Segments
			cone_002.inputs[1].default_value = 1
			#Fill Segments
			cone_002.inputs[2].default_value = 1
			#Radius Top
			cone_002.inputs[3].default_value = 0.0
			#Radius Bottom
			cone_002.inputs[4].default_value = 0.30000001192092896
			#Depth
			cone_002.inputs[5].default_value = 0.5
			
			#node Transform Geometry.004
			transform_geometry_004 = starfile_instances.nodes.new("GeometryNodeTransform")
			transform_geometry_004.name = "Transform Geometry.004"
			transform_geometry_004.mode = 'COMPONENTS'
			#Translation
			transform_geometry_004.inputs[1].default_value = (0.0, 0.0, 1.0)
			#Rotation
			transform_geometry_004.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Scale
			transform_geometry_004.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Cylinder.002
			cylinder_002 = starfile_instances.nodes.new("GeometryNodeMeshCylinder")
			cylinder_002.name = "Cylinder.002"
			cylinder_002.fill_type = 'NGON'
			#Vertices
			cylinder_002.inputs[0].default_value = 32
			#Side Segments
			cylinder_002.inputs[1].default_value = 1
			#Fill Segments
			cylinder_002.inputs[2].default_value = 1
			#Radius
			cylinder_002.inputs[3].default_value = 0.10000000149011612
			#Depth
			cylinder_002.inputs[4].default_value = 1.0
			
			#node Transform Geometry.005
			transform_geometry_005 = starfile_instances.nodes.new("GeometryNodeTransform")
			transform_geometry_005.name = "Transform Geometry.005"
			transform_geometry_005.mode = 'COMPONENTS'
			#Translation
			transform_geometry_005.inputs[1].default_value = (0.0, 0.0, 0.5)
			#Rotation
			transform_geometry_005.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Scale
			transform_geometry_005.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Set Material
			set_material_1 = starfile_instances.nodes.new("GeometryNodeSetMaterial")
			set_material_1.name = "Set Material"
			#Selection
			set_material_1.inputs[1].default_value = True
			
			#node Set Shade Smooth
			set_shade_smooth = starfile_instances.nodes.new("GeometryNodeSetShadeSmooth")
			set_shade_smooth.name = "Set Shade Smooth"
			set_shade_smooth.domain = 'FACE'
			#Selection
			set_shade_smooth.inputs[1].default_value = True
			#Shade Smooth
			set_shade_smooth.inputs[2].default_value = True
			
			#node Named Attribute
			named_attribute = starfile_instances.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'INT'
			#Name
			named_attribute.inputs[0].default_value = "MNImageId"
			
			#node Named Attribute.001
			named_attribute_001 = starfile_instances.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.data_type = 'FLOAT'
			#Name
			named_attribute_001.inputs[0].default_value = "MNAnglePhi"
			
			#node Named Attribute.002
			named_attribute_002 = starfile_instances.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002.name = "Named Attribute.002"
			named_attribute_002.data_type = 'FLOAT'
			#Name
			named_attribute_002.inputs[0].default_value = "MNAngleTheta"
			
			#node Compare
			compare = starfile_instances.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'NOT_EQUAL'
			
			#node Named Attribute.003
			named_attribute_003 = starfile_instances.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_003.name = "Named Attribute.003"
			named_attribute_003.data_type = 'FLOAT'
			#Name
			named_attribute_003.inputs[0].default_value = "MNAnglePsi"
			
			#node Instance on Points
			instance_on_points = starfile_instances.nodes.new("GeometryNodeInstanceOnPoints")
			instance_on_points.name = "Instance on Points"
			#Selection
			instance_on_points.inputs[1].default_value = True
			#Pick Instance
			instance_on_points.inputs[3].default_value = False
			#Instance Index
			instance_on_points.inputs[4].default_value = 0
			#Scale
			instance_on_points.inputs[6].default_value = (1.0, 1.0, 1.0)
			
			#node Store Named Attribute
			store_named_attribute_1 = starfile_instances.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_1.name = "Store Named Attribute"
			store_named_attribute_1.data_type = 'QUATERNION'
			store_named_attribute_1.domain = 'POINT'
			#Selection
			store_named_attribute_1.inputs[1].default_value = True
			#Name
			store_named_attribute_1.inputs[2].default_value = "MNDEBUGEuler"
			
			#node Delete Geometry
			delete_geometry = starfile_instances.nodes.new("GeometryNodeDeleteGeometry")
			delete_geometry.name = "Delete Geometry"
			delete_geometry.domain = 'POINT'
			delete_geometry.mode = 'ALL'
			
			#node Rotation to Euler
			rotation_to_euler_1 = starfile_instances.nodes.new("FunctionNodeRotationToEuler")
			rotation_to_euler_1.name = "Rotation to Euler"
			
			#node Switch.001
			switch_001 = starfile_instances.nodes.new("GeometryNodeSwitch")
			switch_001.label = "MNDebug"
			switch_001.name = "Switch.001"
			switch_001.input_type = 'GEOMETRY'
			#Switch
			switch_001.inputs[0].default_value = False
			
			#node Group
			group = starfile_instances.nodes.new("GeometryNodeGroup")
			group.name = "Group"
			group.node_tree = utils_zyz_to_rotation
			
			#node Group Output
			group_output_2 = starfile_instances.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Join Geometry.004
			join_geometry_004 = starfile_instances.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_004.name = "Join Geometry.004"
			
			#node Group.001
			group_001 = starfile_instances.nodes.new("GeometryNodeGroup")
			group_001.name = "Group.001"
			group_001.node_tree = mn_starfile_micrograph
			
			#node Join Geometry.001
			join_geometry_001 = starfile_instances.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_001.name = "Join Geometry.001"
			
			#node Group Input.001
			group_input_001 = starfile_instances.nodes.new("NodeGroupInput")
			group_input_001.name = "Group Input.001"
			
			#node Store Named Attribute.001
			store_named_attribute_001_1 = starfile_instances.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_001_1.name = "Store Named Attribute.001"
			store_named_attribute_001_1.data_type = 'FLOAT_COLOR'
			store_named_attribute_001_1.domain = 'POINT'
			#Selection
			store_named_attribute_001_1.inputs[1].default_value = True
			#Name
			store_named_attribute_001_1.inputs[2].default_value = "Color"
			#Value
			store_named_attribute_001_1.inputs[3].default_value = (0.6239680051803589, 0.010329999960958958, 0.06301099807024002, 1.0)
			
			#node Store Named Attribute.002
			store_named_attribute_002 = starfile_instances.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_002.name = "Store Named Attribute.002"
			store_named_attribute_002.data_type = 'FLOAT_COLOR'
			store_named_attribute_002.domain = 'POINT'
			#Selection
			store_named_attribute_002.inputs[1].default_value = True
			#Name
			store_named_attribute_002.inputs[2].default_value = "Color"
			#Value
			store_named_attribute_002.inputs[3].default_value = (0.07618500292301178, 0.6239680051803589, 0.08437500149011612, 1.0)
			
			#node Store Named Attribute.003
			store_named_attribute_003 = starfile_instances.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_003.name = "Store Named Attribute.003"
			store_named_attribute_003.data_type = 'FLOAT_COLOR'
			store_named_attribute_003.domain = 'POINT'
			#Selection
			store_named_attribute_003.inputs[1].default_value = True
			#Name
			store_named_attribute_003.inputs[2].default_value = "Color"
			#Value
			store_named_attribute_003.inputs[3].default_value = (0.0, 0.000910000002477318, 0.6239680051803589, 1.0)
			
			
			
			
			#Set locations
			group_input_2.location = (-19.999996185302734, 0.0)
			math.location = (140.0, 200.0)
			object_info.location = (180.0, -200.0)
			id.location = (-19.999996185302734, -200.0)
			attribute_statistic.location = (180.0, -400.0)
			compare_001.location = (380.0000305175781, -400.0)
			boolean_math.location = (580.0000610351562, -400.0)
			switch.location = (867.3298950195312, -400.0)
			join_geometry_002.location = (2.329805612564087, -1440.0)
			cone_001.location = (-1045.0001220703125, -360.0)
			transform_geometry_002.location = (-865.0, -360.0)
			cylinder_001.location = (-1045.0001220703125, -720.0)
			transform_geometry_003.location = (-865.0, -720.0)
			join_geometry.location = (-584.9999389648438, -1400.0)
			cone.location = (-1045.0001220703125, -1080.0)
			transform_geometry_001.location = (-865.0, -1080.0)
			cylinder.location = (-1045.0001220703125, -1440.0)
			transform_geometry.location = (-865.0, -1440.0)
			join_geometry_003.location = (-625.0, -2140.0)
			cone_002.location = (-1065.0, -1820.0)
			transform_geometry_004.location = (-905.0, -1820.0)
			cylinder_002.location = (-1085.0, -2180.0)
			transform_geometry_005.location = (-905.0, -2180.0)
			set_material_1.location = (442.2983093261719, -1408.9595947265625)
			set_shade_smooth.location = (222.3297882080078, -1426.9024658203125)
			named_attribute.location = (-19.999996185302734, 200.0)
			named_attribute_001.location = (20.0, 800.0)
			named_attribute_002.location = (20.0, 660.0)
			compare.location = (300.0000305175781, 200.0)
			named_attribute_003.location = (20.0, 520.0)
			instance_on_points.location = (1030.2874755859375, 31.402042388916016)
			store_named_attribute_1.location = (958.349853515625, 431.1212158203125)
			delete_geometry.location = (480.0000305175781, 0.0)
			rotation_to_euler_1.location = (609.8578491210938, 448.5572509765625)
			switch_001.location = (1269.211181640625, 151.81256103515625)
			group.location = (200.0, 720.0)
			group_output_2.location = (2267.6865234375, 202.171875)
			join_geometry_004.location = (1912.7755126953125, 172.54151916503906)
			group_001.location = (1574.0758056640625, 33.9083251953125)
			join_geometry_001.location = (-584.9999389648438, -680.0)
			group_input_001.location = (1395.191650390625, 30.3790283203125)
			store_named_attribute_001_1.location = (-180.0, -1140.0)
			store_named_attribute_002.location = (-177.67018127441406, -1347.7293701171875)
			store_named_attribute_003.location = (-180.0, -1560.0)
			
			#Set dimensions
			group_input_2.width, group_input_2.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			object_info.width, object_info.height = 140.0, 100.0
			id.width, id.height = 140.0, 100.0
			attribute_statistic.width, attribute_statistic.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			join_geometry_002.width, join_geometry_002.height = 140.0, 100.0
			cone_001.width, cone_001.height = 140.0, 100.0
			transform_geometry_002.width, transform_geometry_002.height = 140.0, 100.0
			cylinder_001.width, cylinder_001.height = 140.0, 100.0
			transform_geometry_003.width, transform_geometry_003.height = 140.0, 100.0
			join_geometry.width, join_geometry.height = 140.0, 100.0
			cone.width, cone.height = 140.0, 100.0
			transform_geometry_001.width, transform_geometry_001.height = 140.0, 100.0
			cylinder.width, cylinder.height = 140.0, 100.0
			transform_geometry.width, transform_geometry.height = 140.0, 100.0
			join_geometry_003.width, join_geometry_003.height = 140.0, 100.0
			cone_002.width, cone_002.height = 140.0, 100.0
			transform_geometry_004.width, transform_geometry_004.height = 140.0, 100.0
			cylinder_002.width, cylinder_002.height = 140.0, 100.0
			transform_geometry_005.width, transform_geometry_005.height = 140.0, 100.0
			set_material_1.width, set_material_1.height = 140.0, 100.0
			set_shade_smooth.width, set_shade_smooth.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
			named_attribute_002.width, named_attribute_002.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			named_attribute_003.width, named_attribute_003.height = 140.0, 100.0
			instance_on_points.width, instance_on_points.height = 140.0, 100.0
			store_named_attribute_1.width, store_named_attribute_1.height = 140.0, 100.0
			delete_geometry.width, delete_geometry.height = 140.0, 100.0
			rotation_to_euler_1.width, rotation_to_euler_1.height = 140.0, 100.0
			switch_001.width, switch_001.height = 140.0, 100.0
			group.width, group.height = 210.0706787109375, 100.0
			group_output_2.width, group_output_2.height = 140.0, 100.0
			join_geometry_004.width, join_geometry_004.height = 140.0, 100.0
			group_001.width, group_001.height = 140.0, 100.0
			join_geometry_001.width, join_geometry_001.height = 140.0, 100.0
			group_input_001.width, group_input_001.height = 80.0, 100.0
			store_named_attribute_001_1.width, store_named_attribute_001_1.height = 140.0, 100.0
			store_named_attribute_002.width, store_named_attribute_002.height = 140.0, 100.0
			store_named_attribute_003.width, store_named_attribute_003.height = 140.0, 100.0
			
			#initialize starfile_instances links
			#group_input_2.Geometry -> delete_geometry.Geometry
			starfile_instances.links.new(group_input_2.outputs[0], delete_geometry.inputs[0])
			#delete_geometry.Geometry -> instance_on_points.Points
			starfile_instances.links.new(delete_geometry.outputs[0], instance_on_points.inputs[0])
			#group_input_2.Molecule -> object_info.Object
			starfile_instances.links.new(group_input_2.outputs[1], object_info.inputs[0])
			#group_input_2.Image -> math.Value
			starfile_instances.links.new(group_input_2.outputs[2], math.inputs[0])
			#group_input_2.Simplify -> boolean_math.Boolean
			starfile_instances.links.new(group_input_2.outputs[3], boolean_math.inputs[0])
			#math.Value -> compare.A
			starfile_instances.links.new(math.outputs[0], compare.inputs[2])
			#named_attribute.Attribute -> compare.B
			starfile_instances.links.new(named_attribute.outputs[0], compare.inputs[3])
			#compare.Result -> delete_geometry.Selection
			starfile_instances.links.new(compare.outputs[0], delete_geometry.inputs[1])
			#attribute_statistic.Max -> compare_001.A
			starfile_instances.links.new(attribute_statistic.outputs[4], compare_001.inputs[0])
			#compare_001.Result -> boolean_math.Boolean
			starfile_instances.links.new(compare_001.outputs[0], boolean_math.inputs[1])
			#id.ID -> attribute_statistic.Attribute
			starfile_instances.links.new(id.outputs[0], attribute_statistic.inputs[2])
			#object_info.Geometry -> attribute_statistic.Geometry
			starfile_instances.links.new(object_info.outputs[4], attribute_statistic.inputs[0])
			#boolean_math.Boolean -> switch.Switch
			starfile_instances.links.new(boolean_math.outputs[0], switch.inputs[0])
			#object_info.Geometry -> switch.False
			starfile_instances.links.new(object_info.outputs[4], switch.inputs[1])
			#set_material_1.Geometry -> switch.True
			starfile_instances.links.new(set_material_1.outputs[0], switch.inputs[2])
			#switch.Output -> instance_on_points.Instance
			starfile_instances.links.new(switch.outputs[0], instance_on_points.inputs[2])
			#set_shade_smooth.Geometry -> set_material_1.Geometry
			starfile_instances.links.new(set_shade_smooth.outputs[0], set_material_1.inputs[0])
			#transform_geometry.Geometry -> join_geometry.Geometry
			starfile_instances.links.new(transform_geometry.outputs[0], join_geometry.inputs[0])
			#cylinder.Mesh -> transform_geometry.Geometry
			starfile_instances.links.new(cylinder.outputs[0], transform_geometry.inputs[0])
			#cone.Mesh -> transform_geometry_001.Geometry
			starfile_instances.links.new(cone.outputs[0], transform_geometry_001.inputs[0])
			#transform_geometry_003.Geometry -> join_geometry_001.Geometry
			starfile_instances.links.new(transform_geometry_003.outputs[0], join_geometry_001.inputs[0])
			#cylinder_001.Mesh -> transform_geometry_003.Geometry
			starfile_instances.links.new(cylinder_001.outputs[0], transform_geometry_003.inputs[0])
			#cone_001.Mesh -> transform_geometry_002.Geometry
			starfile_instances.links.new(cone_001.outputs[0], transform_geometry_002.inputs[0])
			#transform_geometry_005.Geometry -> join_geometry_003.Geometry
			starfile_instances.links.new(transform_geometry_005.outputs[0], join_geometry_003.inputs[0])
			#cylinder_002.Mesh -> transform_geometry_005.Geometry
			starfile_instances.links.new(cylinder_002.outputs[0], transform_geometry_005.inputs[0])
			#cone_002.Mesh -> transform_geometry_004.Geometry
			starfile_instances.links.new(cone_002.outputs[0], transform_geometry_004.inputs[0])
			#join_geometry_002.Geometry -> set_shade_smooth.Geometry
			starfile_instances.links.new(join_geometry_002.outputs[0], set_shade_smooth.inputs[0])
			#rotation_to_euler_1.Euler -> instance_on_points.Rotation
			starfile_instances.links.new(rotation_to_euler_1.outputs[0], instance_on_points.inputs[5])
			#group.Rotation -> rotation_to_euler_1.Rotation
			starfile_instances.links.new(group.outputs[0], rotation_to_euler_1.inputs[0])
			#named_attribute_001.Attribute -> group.Phi
			starfile_instances.links.new(named_attribute_001.outputs[0], group.inputs[0])
			#named_attribute_002.Attribute -> group.Theta
			starfile_instances.links.new(named_attribute_002.outputs[0], group.inputs[1])
			#named_attribute_003.Attribute -> group.Psi
			starfile_instances.links.new(named_attribute_003.outputs[0], group.inputs[2])
			#join_geometry_004.Geometry -> group_output_2.Instances
			starfile_instances.links.new(join_geometry_004.outputs[0], group_output_2.inputs[0])
			#delete_geometry.Geometry -> store_named_attribute_1.Geometry
			starfile_instances.links.new(delete_geometry.outputs[0], store_named_attribute_1.inputs[0])
			#instance_on_points.Instances -> switch_001.False
			starfile_instances.links.new(instance_on_points.outputs[0], switch_001.inputs[1])
			#store_named_attribute_1.Geometry -> switch_001.True
			starfile_instances.links.new(store_named_attribute_1.outputs[0], switch_001.inputs[2])
			#group.Rotation -> store_named_attribute_1.Value
			starfile_instances.links.new(group.outputs[0], store_named_attribute_1.inputs[3])
			#group_001.Output -> join_geometry_004.Geometry
			starfile_instances.links.new(group_001.outputs[0], join_geometry_004.inputs[0])
			#group_input_001.Micrograph Pixelsize -> group_001.A
			starfile_instances.links.new(group_input_001.outputs[6], group_001.inputs[3])
			#group_input_001.Show Micrograph -> group_001.Switch
			starfile_instances.links.new(group_input_001.outputs[4], group_001.inputs[1])
			#group_input_001.Micrograph Z -> group_001.Z
			starfile_instances.links.new(group_input_001.outputs[7], group_001.inputs[4])
			#group_input_001.Micrograph -> group_001.Image
			starfile_instances.links.new(group_input_001.outputs[5], group_001.inputs[2])
			#group_input_001.Geometry -> group_001.Geometry
			starfile_instances.links.new(group_input_001.outputs[0], group_001.inputs[0])
			#group_input_001.Brightness -> group_001.Brightness
			starfile_instances.links.new(group_input_001.outputs[8], group_001.inputs[5])
			#group_input_001.Contrast -> group_001.Contrast
			starfile_instances.links.new(group_input_001.outputs[9], group_001.inputs[6])
			#store_named_attribute_003.Geometry -> join_geometry_002.Geometry
			starfile_instances.links.new(store_named_attribute_003.outputs[0], join_geometry_002.inputs[0])
			#join_geometry_001.Geometry -> store_named_attribute_001_1.Geometry
			starfile_instances.links.new(join_geometry_001.outputs[0], store_named_attribute_001_1.inputs[0])
			#join_geometry.Geometry -> store_named_attribute_002.Geometry
			starfile_instances.links.new(join_geometry.outputs[0], store_named_attribute_002.inputs[0])
			#join_geometry_003.Geometry -> store_named_attribute_003.Geometry
			starfile_instances.links.new(join_geometry_003.outputs[0], store_named_attribute_003.inputs[0])
			#transform_geometry_001.Geometry -> join_geometry.Geometry
			starfile_instances.links.new(transform_geometry_001.outputs[0], join_geometry.inputs[0])
			#transform_geometry_002.Geometry -> join_geometry_001.Geometry
			starfile_instances.links.new(transform_geometry_002.outputs[0], join_geometry_001.inputs[0])
			#transform_geometry_004.Geometry -> join_geometry_003.Geometry
			starfile_instances.links.new(transform_geometry_004.outputs[0], join_geometry_003.inputs[0])
			#switch_001.Output -> join_geometry_004.Geometry
			starfile_instances.links.new(switch_001.outputs[0], join_geometry_004.inputs[0])
			#store_named_attribute_002.Geometry -> join_geometry_002.Geometry
			starfile_instances.links.new(store_named_attribute_002.outputs[0], join_geometry_002.inputs[0])
			#store_named_attribute_001_1.Geometry -> join_geometry_002.Geometry
			starfile_instances.links.new(store_named_attribute_001_1.outputs[0], join_geometry_002.inputs[0])
			return starfile_instances

		starfile_instances = starfile_instances_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Starfile Instances", type = 'NODES')
		mod.node_group = starfile_instances
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Starfile_Instances.bl_idname)
			
def register():
	bpy.utils.register_class(Starfile_Instances)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Starfile_Instances)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
