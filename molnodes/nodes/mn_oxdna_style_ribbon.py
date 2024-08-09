bl_info = {
	"name" : "MN_oxdna_style_ribbon",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class MN_oxdna_style_ribbon(bpy.types.Operator):
	bl_idname = "node.mn_oxdna_style_ribbon"
	bl_label = "MN_oxdna_style_ribbon"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _utils_oxdna_base node group
		def _utils_oxdna_base_node_group():
			_utils_oxdna_base = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".utils_oxdna_base")

			_utils_oxdna_base.color_tag = 'NONE'
			_utils_oxdna_base.description = ""

			_utils_oxdna_base.is_modifier = True
			
			#_utils_oxdna_base interface
			#Socket Geometry
			geometry_socket = _utils_oxdna_base.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket = _utils_oxdna_base.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket.subtype = 'NONE'
			value_socket.default_value = 0.5
			value_socket.min_value = -10000.0
			value_socket.max_value = 10000.0
			value_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_1 = _utils_oxdna_base.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket_1.subtype = 'NONE'
			value_socket_1.default_value = 0.5
			value_socket_1.min_value = -10000.0
			value_socket_1.max_value = 10000.0
			value_socket_1.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_2 = _utils_oxdna_base.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket_2.subtype = 'NONE'
			value_socket_2.default_value = 0.5
			value_socket_2.min_value = -10000.0
			value_socket_2.max_value = 10000.0
			value_socket_2.attribute_domain = 'POINT'
			
			
			#initialize _utils_oxdna_base nodes
			#node Group Output
			group_output = _utils_oxdna_base.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = _utils_oxdna_base.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Math
			math = _utils_oxdna_base.nodes.new("ShaderNodeMath")
			math.name = "Math"
			math.operation = 'DIVIDE'
			math.use_clamp = False
			#Value_001
			math.inputs[1].default_value = 2.0
			
			#node Transform Geometry
			transform_geometry = _utils_oxdna_base.nodes.new("GeometryNodeTransform")
			transform_geometry.name = "Transform Geometry"
			transform_geometry.mode = 'COMPONENTS'
			#Rotation
			transform_geometry.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Scale
			transform_geometry.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Cylinder
			cylinder = _utils_oxdna_base.nodes.new("GeometryNodeMeshCylinder")
			cylinder.name = "Cylinder"
			cylinder.fill_type = 'NGON'
			#Vertices
			cylinder.inputs[0].default_value = 4
			#Side Segments
			cylinder.inputs[1].default_value = 1
			#Fill Segments
			cylinder.inputs[2].default_value = 1
			
			#node Combine XYZ
			combine_xyz = _utils_oxdna_base.nodes.new("ShaderNodeCombineXYZ")
			combine_xyz.name = "Combine XYZ"
			#X
			combine_xyz.inputs[0].default_value = 0.0
			#Y
			combine_xyz.inputs[1].default_value = 0.0
			
			#node Reroute
			reroute = _utils_oxdna_base.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Math.002
			math_002 = _utils_oxdna_base.nodes.new("ShaderNodeMath")
			math_002.name = "Math.002"
			math_002.operation = 'DIVIDE'
			math_002.use_clamp = False
			#Value_001
			math_002.inputs[1].default_value = 100.0
			
			#node Math.001
			math_001 = _utils_oxdna_base.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.operation = 'DIVIDE'
			math_001.use_clamp = False
			#Value_001
			math_001.inputs[1].default_value = 100.0
			
			#node Math.003
			math_003 = _utils_oxdna_base.nodes.new("ShaderNodeMath")
			math_003.name = "Math.003"
			math_003.operation = 'DIVIDE'
			math_003.use_clamp = False
			#Value_001
			math_003.inputs[1].default_value = 10.0
			
			#node Transform Geometry.001
			transform_geometry_001 = _utils_oxdna_base.nodes.new("GeometryNodeTransform")
			transform_geometry_001.name = "Transform Geometry.001"
			transform_geometry_001.mode = 'COMPONENTS'
			#Translation
			transform_geometry_001.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Rotation
			transform_geometry_001.inputs[2].default_value = (0.0, 0.0, 0.7853981852531433)
			#Scale
			transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Combine XYZ.001
			combine_xyz_001 = _utils_oxdna_base.nodes.new("ShaderNodeCombineXYZ")
			combine_xyz_001.name = "Combine XYZ.001"
			#Y
			combine_xyz_001.inputs[1].default_value = 1.0
			#Z
			combine_xyz_001.inputs[2].default_value = 1.0
			
			#node Transform Geometry.002
			transform_geometry_002 = _utils_oxdna_base.nodes.new("GeometryNodeTransform")
			transform_geometry_002.name = "Transform Geometry.002"
			transform_geometry_002.mode = 'COMPONENTS'
			#Translation
			transform_geometry_002.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Rotation
			transform_geometry_002.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			
			
			
			#Set locations
			group_output.location = (623.913818359375, 0.0)
			group_input.location = (-633.9136962890625, 0.0)
			math.location = (-39.2435302734375, -142.93002319335938)
			transform_geometry.location = (115.4232177734375, 243.7366180419922)
			cylinder.location = (-39.2435302734375, 243.7366180419922)
			combine_xyz.location = (-39.2435302734375, -26.9300537109375)
			reroute.location = (-210.3306884765625, -78.89993286132812)
			math_002.location = (-433.9136962890625, 97.47659301757812)
			math_001.location = (-430.997314453125, -65.59671020507812)
			math_003.location = (-432.2694091796875, -243.73660278320312)
			transform_geometry_001.location = (270.08984375, 243.7366180419922)
			combine_xyz_001.location = (265.00262451171875, -65.59671020507812)
			transform_geometry_002.location = (433.913818359375, 194.11192321777344)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			transform_geometry.width, transform_geometry.height = 140.0, 100.0
			cylinder.width, cylinder.height = 140.0, 100.0
			combine_xyz.width, combine_xyz.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			math_002.width, math_002.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			math_003.width, math_003.height = 140.0, 100.0
			transform_geometry_001.width, transform_geometry_001.height = 140.0, 100.0
			combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
			transform_geometry_002.width, transform_geometry_002.height = 140.0, 100.0
			
			#initialize _utils_oxdna_base links
			#reroute.Output -> cylinder.Depth
			_utils_oxdna_base.links.new(reroute.outputs[0], cylinder.inputs[4])
			#transform_geometry.Geometry -> transform_geometry_001.Geometry
			_utils_oxdna_base.links.new(transform_geometry.outputs[0], transform_geometry_001.inputs[0])
			#combine_xyz_001.Vector -> transform_geometry_002.Scale
			_utils_oxdna_base.links.new(combine_xyz_001.outputs[0], transform_geometry_002.inputs[3])
			#cylinder.Mesh -> transform_geometry.Geometry
			_utils_oxdna_base.links.new(cylinder.outputs[0], transform_geometry.inputs[0])
			#math_001.Value -> reroute.Input
			_utils_oxdna_base.links.new(math_001.outputs[0], reroute.inputs[0])
			#math_002.Value -> cylinder.Radius
			_utils_oxdna_base.links.new(math_002.outputs[0], cylinder.inputs[3])
			#combine_xyz.Vector -> transform_geometry.Translation
			_utils_oxdna_base.links.new(combine_xyz.outputs[0], transform_geometry.inputs[1])
			#transform_geometry_001.Geometry -> transform_geometry_002.Geometry
			_utils_oxdna_base.links.new(transform_geometry_001.outputs[0], transform_geometry_002.inputs[0])
			#math_003.Value -> combine_xyz_001.X
			_utils_oxdna_base.links.new(math_003.outputs[0], combine_xyz_001.inputs[0])
			#reroute.Output -> math.Value
			_utils_oxdna_base.links.new(reroute.outputs[0], math.inputs[0])
			#math.Value -> combine_xyz.Z
			_utils_oxdna_base.links.new(math.outputs[0], combine_xyz.inputs[2])
			#group_input.Value -> math_002.Value
			_utils_oxdna_base.links.new(group_input.outputs[0], math_002.inputs[0])
			#group_input.Value -> math_001.Value
			_utils_oxdna_base.links.new(group_input.outputs[1], math_001.inputs[0])
			#group_input.Value -> math_003.Value
			_utils_oxdna_base.links.new(group_input.outputs[2], math_003.inputs[0])
			#transform_geometry_002.Geometry -> group_output.Geometry
			_utils_oxdna_base.links.new(transform_geometry_002.outputs[0], group_output.inputs[0])
			return _utils_oxdna_base

		_utils_oxdna_base = _utils_oxdna_base_node_group()

		#initialize color_res_name_nucleic node group
		def color_res_name_nucleic_node_group():
			color_res_name_nucleic = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Color Res Name Nucleic")

			color_res_name_nucleic.color_tag = 'NONE'
			color_res_name_nucleic.description = ""

			
			#color_res_name_nucleic interface
			#Socket Color
			color_socket = color_res_name_nucleic.interface.new_socket(name = "Color", in_out='OUTPUT', socket_type = 'NodeSocketColor')
			color_socket.attribute_domain = 'POINT'
			
			#Socket A
			a_socket = color_res_name_nucleic.interface.new_socket(name = "A", in_out='INPUT', socket_type = 'NodeSocketColor')
			a_socket.attribute_domain = 'POINT'
			
			#Socket C
			c_socket = color_res_name_nucleic.interface.new_socket(name = "C", in_out='INPUT', socket_type = 'NodeSocketColor')
			c_socket.attribute_domain = 'POINT'
			
			#Socket G
			g_socket = color_res_name_nucleic.interface.new_socket(name = "G", in_out='INPUT', socket_type = 'NodeSocketColor')
			g_socket.attribute_domain = 'POINT'
			
			#Socket T / U
			t___u_socket = color_res_name_nucleic.interface.new_socket(name = "T / U", in_out='INPUT', socket_type = 'NodeSocketColor')
			t___u_socket.attribute_domain = 'POINT'
			
			
			#initialize color_res_name_nucleic nodes
			#node Group Output
			group_output_1 = color_res_name_nucleic.nodes.new("NodeGroupOutput")
			group_output_1.name = "Group Output"
			group_output_1.is_active_output = True
			
			#node Switch.004
			switch_004 = color_res_name_nucleic.nodes.new("GeometryNodeSwitch")
			switch_004.name = "Switch.004"
			switch_004.input_type = 'RGBA'
			
			#node Switch.001
			switch_001 = color_res_name_nucleic.nodes.new("GeometryNodeSwitch")
			switch_001.name = "Switch.001"
			switch_001.input_type = 'RGBA'
			
			#node Switch.002
			switch_002 = color_res_name_nucleic.nodes.new("GeometryNodeSwitch")
			switch_002.name = "Switch.002"
			switch_002.input_type = 'RGBA'
			
			#node Switch.003
			switch_003 = color_res_name_nucleic.nodes.new("GeometryNodeSwitch")
			switch_003.name = "Switch.003"
			switch_003.input_type = 'RGBA'
			
			#node Boolean Math.017
			boolean_math_017 = color_res_name_nucleic.nodes.new("FunctionNodeBooleanMath")
			boolean_math_017.name = "Boolean Math.017"
			boolean_math_017.operation = 'OR'
			
			#node Compare.013
			compare_013 = color_res_name_nucleic.nodes.new("FunctionNodeCompare")
			compare_013.name = "Compare.013"
			compare_013.data_type = 'INT'
			compare_013.mode = 'ELEMENT'
			compare_013.operation = 'EQUAL'
			#B_INT
			compare_013.inputs[3].default_value = 33
			
			#node Compare.020
			compare_020 = color_res_name_nucleic.nodes.new("FunctionNodeCompare")
			compare_020.name = "Compare.020"
			compare_020.data_type = 'INT'
			compare_020.mode = 'ELEMENT'
			compare_020.operation = 'EQUAL'
			#B_INT
			compare_020.inputs[3].default_value = 43
			
			#node Boolean Math.016
			boolean_math_016 = color_res_name_nucleic.nodes.new("FunctionNodeBooleanMath")
			boolean_math_016.name = "Boolean Math.016"
			boolean_math_016.operation = 'OR'
			
			#node Compare.019
			compare_019 = color_res_name_nucleic.nodes.new("FunctionNodeCompare")
			compare_019.name = "Compare.019"
			compare_019.data_type = 'INT'
			compare_019.mode = 'ELEMENT'
			compare_019.operation = 'EQUAL'
			#B_INT
			compare_019.inputs[3].default_value = 42
			
			#node Boolean Math.015
			boolean_math_015 = color_res_name_nucleic.nodes.new("FunctionNodeBooleanMath")
			boolean_math_015.name = "Boolean Math.015"
			boolean_math_015.operation = 'OR'
			
			#node Compare.018
			compare_018 = color_res_name_nucleic.nodes.new("FunctionNodeCompare")
			compare_018.name = "Compare.018"
			compare_018.data_type = 'INT'
			compare_018.mode = 'ELEMENT'
			compare_018.operation = 'EQUAL'
			#B_INT
			compare_018.inputs[3].default_value = 41
			
			#node Boolean Math.014
			boolean_math_014 = color_res_name_nucleic.nodes.new("FunctionNodeBooleanMath")
			boolean_math_014.name = "Boolean Math.014"
			boolean_math_014.operation = 'OR'
			
			#node Compare.017
			compare_017 = color_res_name_nucleic.nodes.new("FunctionNodeCompare")
			compare_017.name = "Compare.017"
			compare_017.data_type = 'INT'
			compare_017.mode = 'ELEMENT'
			compare_017.operation = 'EQUAL'
			#B_INT
			compare_017.inputs[3].default_value = 40
			
			#node Compare.010
			compare_010 = color_res_name_nucleic.nodes.new("FunctionNodeCompare")
			compare_010.name = "Compare.010"
			compare_010.data_type = 'INT'
			compare_010.mode = 'ELEMENT'
			compare_010.operation = 'EQUAL'
			#B_INT
			compare_010.inputs[3].default_value = 30
			
			#node Compare.012
			compare_012 = color_res_name_nucleic.nodes.new("FunctionNodeCompare")
			compare_012.name = "Compare.012"
			compare_012.data_type = 'INT'
			compare_012.mode = 'ELEMENT'
			compare_012.operation = 'EQUAL'
			#B_INT
			compare_012.inputs[3].default_value = 32
			
			#node Compare.011
			compare_011 = color_res_name_nucleic.nodes.new("FunctionNodeCompare")
			compare_011.name = "Compare.011"
			compare_011.data_type = 'INT'
			compare_011.mode = 'ELEMENT'
			compare_011.operation = 'EQUAL'
			#B_INT
			compare_011.inputs[3].default_value = 31
			
			#node Named Attribute.009
			named_attribute_009 = color_res_name_nucleic.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_009.name = "Named Attribute.009"
			named_attribute_009.data_type = 'INT'
			#Name
			named_attribute_009.inputs[0].default_value = "res_name"
			
			#node Group Input
			group_input_1 = color_res_name_nucleic.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			
			#node Named Attribute
			named_attribute = color_res_name_nucleic.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute.inputs[0].default_value = "Color"
			
			
			
			
			#Set locations
			group_output_1.location = (643.794677734375, 0.0)
			switch_004.location = (453.7947082519531, -246.83526611328125)
			switch_001.location = (286.0763854980469, -248.0322265625)
			switch_002.location = (99.95280456542969, -253.164794921875)
			switch_003.location = (-80.04719543457031, -253.164794921875)
			boolean_math_017.location = (293.7947082519531, 253.16473388671875)
			compare_013.location = (293.7947082519531, -66.83526611328125)
			compare_020.location = (293.7947082519531, 113.16473388671875)
			boolean_math_016.location = (93.79472351074219, 253.16473388671875)
			compare_019.location = (93.79472351074219, 113.16473388671875)
			boolean_math_015.location = (-86.20527648925781, 253.16473388671875)
			compare_018.location = (-86.20527648925781, 113.16473388671875)
			boolean_math_014.location = (-266.20526123046875, 253.16473388671875)
			compare_017.location = (-266.20526123046875, 113.16473388671875)
			compare_010.location = (-266.20526123046875, -66.83526611328125)
			compare_012.location = (106.20527648925781, -70.5985107421875)
			compare_011.location = (-73.79472351074219, -70.5985107421875)
			named_attribute_009.location = (-453.7947082519531, -70.5985107421875)
			group_input_1.location = (-460.0, -440.0)
			named_attribute.location = (-460.0, -300.0)
			
			#Set dimensions
			group_output_1.width, group_output_1.height = 140.0, 100.0
			switch_004.width, switch_004.height = 140.0, 100.0
			switch_001.width, switch_001.height = 140.0, 100.0
			switch_002.width, switch_002.height = 140.0, 100.0
			switch_003.width, switch_003.height = 140.0, 100.0
			boolean_math_017.width, boolean_math_017.height = 140.0, 100.0
			compare_013.width, compare_013.height = 140.0, 100.0
			compare_020.width, compare_020.height = 140.0, 100.0
			boolean_math_016.width, boolean_math_016.height = 140.0, 100.0
			compare_019.width, compare_019.height = 140.0, 100.0
			boolean_math_015.width, boolean_math_015.height = 140.0, 100.0
			compare_018.width, compare_018.height = 140.0, 100.0
			boolean_math_014.width, boolean_math_014.height = 140.0, 100.0
			compare_017.width, compare_017.height = 140.0, 100.0
			compare_010.width, compare_010.height = 140.0, 100.0
			compare_012.width, compare_012.height = 140.0, 100.0
			compare_011.width, compare_011.height = 140.0, 100.0
			named_attribute_009.width, named_attribute_009.height = 140.0, 100.0
			group_input_1.width, group_input_1.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			
			#initialize color_res_name_nucleic links
			#switch_003.Output -> switch_002.False
			color_res_name_nucleic.links.new(switch_003.outputs[0], switch_002.inputs[1])
			#named_attribute_009.Attribute -> compare_011.A
			color_res_name_nucleic.links.new(named_attribute_009.outputs[0], compare_011.inputs[2])
			#switch_002.Output -> switch_001.False
			color_res_name_nucleic.links.new(switch_002.outputs[0], switch_001.inputs[1])
			#boolean_math_015.Boolean -> switch_002.Switch
			color_res_name_nucleic.links.new(boolean_math_015.outputs[0], switch_002.inputs[0])
			#named_attribute_009.Attribute -> compare_019.A
			color_res_name_nucleic.links.new(named_attribute_009.outputs[0], compare_019.inputs[2])
			#compare_011.Result -> boolean_math_015.Boolean
			color_res_name_nucleic.links.new(compare_011.outputs[0], boolean_math_015.inputs[1])
			#compare_018.Result -> boolean_math_015.Boolean
			color_res_name_nucleic.links.new(compare_018.outputs[0], boolean_math_015.inputs[0])
			#compare_013.Result -> boolean_math_017.Boolean
			color_res_name_nucleic.links.new(compare_013.outputs[0], boolean_math_017.inputs[1])
			#named_attribute_009.Attribute -> compare_018.A
			color_res_name_nucleic.links.new(named_attribute_009.outputs[0], compare_018.inputs[2])
			#boolean_math_014.Boolean -> switch_003.Switch
			color_res_name_nucleic.links.new(boolean_math_014.outputs[0], switch_003.inputs[0])
			#compare_010.Result -> boolean_math_014.Boolean
			color_res_name_nucleic.links.new(compare_010.outputs[0], boolean_math_014.inputs[1])
			#named_attribute_009.Attribute -> compare_012.A
			color_res_name_nucleic.links.new(named_attribute_009.outputs[0], compare_012.inputs[2])
			#compare_017.Result -> boolean_math_014.Boolean
			color_res_name_nucleic.links.new(compare_017.outputs[0], boolean_math_014.inputs[0])
			#named_attribute_009.Attribute -> compare_017.A
			color_res_name_nucleic.links.new(named_attribute_009.outputs[0], compare_017.inputs[2])
			#named_attribute_009.Attribute -> compare_010.A
			color_res_name_nucleic.links.new(named_attribute_009.outputs[0], compare_010.inputs[2])
			#named_attribute_009.Attribute -> compare_013.A
			color_res_name_nucleic.links.new(named_attribute_009.outputs[0], compare_013.inputs[2])
			#switch_001.Output -> switch_004.False
			color_res_name_nucleic.links.new(switch_001.outputs[0], switch_004.inputs[1])
			#compare_020.Result -> boolean_math_017.Boolean
			color_res_name_nucleic.links.new(compare_020.outputs[0], boolean_math_017.inputs[0])
			#named_attribute_009.Attribute -> compare_020.A
			color_res_name_nucleic.links.new(named_attribute_009.outputs[0], compare_020.inputs[2])
			#compare_019.Result -> boolean_math_016.Boolean
			color_res_name_nucleic.links.new(compare_019.outputs[0], boolean_math_016.inputs[0])
			#boolean_math_016.Boolean -> switch_001.Switch
			color_res_name_nucleic.links.new(boolean_math_016.outputs[0], switch_001.inputs[0])
			#compare_012.Result -> boolean_math_016.Boolean
			color_res_name_nucleic.links.new(compare_012.outputs[0], boolean_math_016.inputs[1])
			#boolean_math_017.Boolean -> switch_004.Switch
			color_res_name_nucleic.links.new(boolean_math_017.outputs[0], switch_004.inputs[0])
			#switch_004.Output -> group_output_1.Color
			color_res_name_nucleic.links.new(switch_004.outputs[0], group_output_1.inputs[0])
			#group_input_1.A -> switch_003.True
			color_res_name_nucleic.links.new(group_input_1.outputs[0], switch_003.inputs[2])
			#group_input_1.C -> switch_002.True
			color_res_name_nucleic.links.new(group_input_1.outputs[1], switch_002.inputs[2])
			#group_input_1.G -> switch_001.True
			color_res_name_nucleic.links.new(group_input_1.outputs[2], switch_001.inputs[2])
			#group_input_1.T / U -> switch_004.True
			color_res_name_nucleic.links.new(group_input_1.outputs[3], switch_004.inputs[2])
			#named_attribute.Attribute -> switch_003.False
			color_res_name_nucleic.links.new(named_attribute.outputs[0], switch_003.inputs[1])
			return color_res_name_nucleic

		color_res_name_nucleic = color_res_name_nucleic_node_group()

		#initialize mn_oxdna_style_ribbon node group
		def mn_oxdna_style_ribbon_node_group():
			mn_oxdna_style_ribbon = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "MN_oxdna_style_ribbon")

			mn_oxdna_style_ribbon.color_tag = 'NONE'
			mn_oxdna_style_ribbon.description = ""

			
			#mn_oxdna_style_ribbon interface
			#Socket DNA Mesh
			dna_mesh_socket = mn_oxdna_style_ribbon.interface.new_socket(name = "DNA Mesh", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			dna_mesh_socket.attribute_domain = 'POINT'
			
			#Socket DNA Bases
			dna_bases_socket = mn_oxdna_style_ribbon.interface.new_socket(name = "DNA Bases", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			dna_bases_socket.attribute_domain = 'POINT'
			
			#Socket Selection
			selection_socket = mn_oxdna_style_ribbon.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket.attribute_domain = 'POINT'
			selection_socket.hide_value = True
			selection_socket.description = "Selection of atoms to apply this node to"
			
			#Socket Material
			material_socket = mn_oxdna_style_ribbon.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial')
			material_socket.attribute_domain = 'POINT'
			material_socket.description = "Material to apply to the resulting geometry"
			
			#Panel Base
			base_panel = mn_oxdna_style_ribbon.interface.new_panel("Base")
			#Socket A
			a_socket_1 = mn_oxdna_style_ribbon.interface.new_socket(name = "A", in_out='INPUT', socket_type = 'NodeSocketColor', parent = base_panel)
			a_socket_1.attribute_domain = 'POINT'
			
			#Socket C
			c_socket_1 = mn_oxdna_style_ribbon.interface.new_socket(name = "C", in_out='INPUT', socket_type = 'NodeSocketColor', parent = base_panel)
			c_socket_1.attribute_domain = 'POINT'
			
			#Socket G
			g_socket_1 = mn_oxdna_style_ribbon.interface.new_socket(name = "G", in_out='INPUT', socket_type = 'NodeSocketColor', parent = base_panel)
			g_socket_1.attribute_domain = 'POINT'
			
			#Socket T / U
			t___u_socket_1 = mn_oxdna_style_ribbon.interface.new_socket(name = "T / U", in_out='INPUT', socket_type = 'NodeSocketColor', parent = base_panel)
			t___u_socket_1.attribute_domain = 'POINT'
			
			#Socket Base Scale
			base_scale_socket = mn_oxdna_style_ribbon.interface.new_socket(name = "Base Scale", in_out='INPUT', socket_type = 'NodeSocketVector', parent = base_panel)
			base_scale_socket.subtype = 'XYZ'
			base_scale_socket.default_value = (1.0, 1.0, 1.0)
			base_scale_socket.min_value = -3.4028234663852886e+38
			base_scale_socket.max_value = 3.4028234663852886e+38
			base_scale_socket.attribute_domain = 'POINT'
			
			
			#Panel Backbone
			backbone_panel = mn_oxdna_style_ribbon.interface.new_panel("Backbone")
			#Socket Backbone Resolution
			backbone_resolution_socket = mn_oxdna_style_ribbon.interface.new_socket(name = "Backbone Resolution", in_out='INPUT', socket_type = 'NodeSocketInt', parent = backbone_panel)
			backbone_resolution_socket.subtype = 'NONE'
			backbone_resolution_socket.default_value = 6
			backbone_resolution_socket.min_value = 3
			backbone_resolution_socket.max_value = 512
			backbone_resolution_socket.attribute_domain = 'POINT'
			
			#Socket Backbone Subdivisions
			backbone_subdivisions_socket = mn_oxdna_style_ribbon.interface.new_socket(name = "Backbone Subdivisions", in_out='INPUT', socket_type = 'NodeSocketInt', parent = backbone_panel)
			backbone_subdivisions_socket.subtype = 'NONE'
			backbone_subdivisions_socket.default_value = 1
			backbone_subdivisions_socket.min_value = 1
			backbone_subdivisions_socket.max_value = 2147483647
			backbone_subdivisions_socket.attribute_domain = 'POINT'
			
			#Socket Backbone Radius
			backbone_radius_socket = mn_oxdna_style_ribbon.interface.new_socket(name = "Backbone Radius", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = backbone_panel)
			backbone_radius_socket.subtype = 'NONE'
			backbone_radius_socket.default_value = 2.0
			backbone_radius_socket.min_value = 0.0
			backbone_radius_socket.max_value = 10000.0
			backbone_radius_socket.attribute_domain = 'POINT'
			
			#Socket Backbone Shade Smooth
			backbone_shade_smooth_socket = mn_oxdna_style_ribbon.interface.new_socket(name = "Backbone Shade Smooth", in_out='INPUT', socket_type = 'NodeSocketBool', parent = backbone_panel)
			backbone_shade_smooth_socket.attribute_domain = 'POINT'
			
			
			
			#initialize mn_oxdna_style_ribbon nodes
			#node Frame
			frame = mn_oxdna_style_ribbon.nodes.new("NodeFrame")
			frame.label = "calculate backbone offset"
			frame.name = "Frame"
			frame.label_size = 20
			frame.shrink = True
			
			#node Group Output
			group_output_2 = mn_oxdna_style_ribbon.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Set Material
			set_material = mn_oxdna_style_ribbon.nodes.new("GeometryNodeSetMaterial")
			set_material.name = "Set Material"
			#Selection
			set_material.inputs[1].default_value = True
			
			#node Join Geometry
			join_geometry = mn_oxdna_style_ribbon.nodes.new("GeometryNodeJoinGeometry")
			join_geometry.name = "Join Geometry"
			join_geometry.hide = True
			
			#node Group Input.003
			group_input_003 = mn_oxdna_style_ribbon.nodes.new("NodeGroupInput")
			group_input_003.name = "Group Input.003"
			group_input_003.outputs[0].hide = True
			group_input_003.outputs[1].hide = True
			group_input_003.outputs[3].hide = True
			group_input_003.outputs[4].hide = True
			group_input_003.outputs[5].hide = True
			group_input_003.outputs[6].hide = True
			group_input_003.outputs[7].hide = True
			group_input_003.outputs[8].hide = True
			group_input_003.outputs[9].hide = True
			group_input_003.outputs[10].hide = True
			group_input_003.outputs[11].hide = True
			group_input_003.outputs[12].hide = True
			
			#node Capture Attribute
			capture_attribute = mn_oxdna_style_ribbon.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute.name = "Capture Attribute"
			capture_attribute.active_index = 0
			capture_attribute.capture_items.clear()
			capture_attribute.capture_items.new('FLOAT', "Value")
			capture_attribute.capture_items["Value"].data_type = 'FLOAT_VECTOR'
			capture_attribute.domain = 'POINT'
			
			#node Separate Geometry
			separate_geometry = mn_oxdna_style_ribbon.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry.name = "Separate Geometry"
			separate_geometry.domain = 'POINT'
			
			#node Reroute
			reroute_1 = mn_oxdna_style_ribbon.nodes.new("NodeReroute")
			reroute_1.name = "Reroute"
			#node Set Position.001
			set_position_001 = mn_oxdna_style_ribbon.nodes.new("GeometryNodeSetPosition")
			set_position_001.name = "Set Position.001"
			#Selection
			set_position_001.inputs[1].default_value = True
			#Position
			set_position_001.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Vector Math.004
			vector_math_004 = mn_oxdna_style_ribbon.nodes.new("ShaderNodeVectorMath")
			vector_math_004.name = "Vector Math.004"
			vector_math_004.operation = 'CROSS_PRODUCT'
			
			#node Vector Math.005
			vector_math_005 = mn_oxdna_style_ribbon.nodes.new("ShaderNodeVectorMath")
			vector_math_005.name = "Vector Math.005"
			vector_math_005.operation = 'SCALE'
			#Scale
			vector_math_005.inputs[3].default_value = 3.4079999923706055
			
			#node Vector Math.002
			vector_math_002 = mn_oxdna_style_ribbon.nodes.new("ShaderNodeVectorMath")
			vector_math_002.name = "Vector Math.002"
			vector_math_002.operation = 'ADD'
			
			#node Named Attribute.004
			named_attribute_004 = mn_oxdna_style_ribbon.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_004.name = "Named Attribute.004"
			named_attribute_004.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_004.inputs[0].default_value = "base_normal"
			
			#node Vector Math.003
			vector_math_003 = mn_oxdna_style_ribbon.nodes.new("ShaderNodeVectorMath")
			vector_math_003.name = "Vector Math.003"
			vector_math_003.operation = 'SCALE'
			#Scale
			vector_math_003.inputs[3].default_value = -0.3400000035762787
			
			#node Named Attribute.003
			named_attribute_003 = mn_oxdna_style_ribbon.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_003.name = "Named Attribute.003"
			named_attribute_003.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_003.inputs[0].default_value = "base_vector"
			
			#node Set Curve Radius
			set_curve_radius = mn_oxdna_style_ribbon.nodes.new("GeometryNodeSetCurveRadius")
			set_curve_radius.name = "Set Curve Radius"
			#Selection
			set_curve_radius.inputs[1].default_value = True
			
			#node Math
			math_1 = mn_oxdna_style_ribbon.nodes.new("ShaderNodeMath")
			math_1.name = "Math"
			math_1.operation = 'DIVIDE'
			math_1.use_clamp = False
			#Value_001
			math_1.inputs[1].default_value = 100.0
			
			#node Points to Curves
			points_to_curves = mn_oxdna_style_ribbon.nodes.new("GeometryNodePointsToCurves")
			points_to_curves.name = "Points to Curves"
			#Weight
			points_to_curves.inputs[2].default_value = 0.0
			
			#node Mesh to Points
			mesh_to_points = mn_oxdna_style_ribbon.nodes.new("GeometryNodeMeshToPoints")
			mesh_to_points.name = "Mesh to Points"
			mesh_to_points.mode = 'VERTICES'
			#Selection
			mesh_to_points.inputs[1].default_value = True
			#Position
			mesh_to_points.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Radius
			mesh_to_points.inputs[3].default_value = 1.0
			
			#node Set Spline Type
			set_spline_type = mn_oxdna_style_ribbon.nodes.new("GeometryNodeCurveSplineType")
			set_spline_type.name = "Set Spline Type"
			set_spline_type.spline_type = 'BEZIER'
			#Selection
			set_spline_type.inputs[1].default_value = True
			
			#node Set Handle Type
			set_handle_type = mn_oxdna_style_ribbon.nodes.new("GeometryNodeCurveSetHandles")
			set_handle_type.name = "Set Handle Type"
			set_handle_type.handle_type = 'AUTO'
			set_handle_type.mode = {'RIGHT', 'LEFT'}
			#Selection
			set_handle_type.inputs[1].default_value = True
			
			#node Curve to Mesh
			curve_to_mesh = mn_oxdna_style_ribbon.nodes.new("GeometryNodeCurveToMesh")
			curve_to_mesh.name = "Curve to Mesh"
			#Fill Caps
			curve_to_mesh.inputs[2].default_value = True
			
			#node Set Spline Resolution
			set_spline_resolution = mn_oxdna_style_ribbon.nodes.new("GeometryNodeSetSplineResolution")
			set_spline_resolution.name = "Set Spline Resolution"
			#Selection
			set_spline_resolution.inputs[1].default_value = True
			
			#node Curve Circle
			curve_circle = mn_oxdna_style_ribbon.nodes.new("GeometryNodeCurvePrimitiveCircle")
			curve_circle.name = "Curve Circle"
			curve_circle.mode = 'RADIUS'
			#Radius
			curve_circle.inputs[4].default_value = 1.0
			
			#node Named Attribute.002
			named_attribute_002 = mn_oxdna_style_ribbon.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002.name = "Named Attribute.002"
			named_attribute_002.data_type = 'INT'
			#Name
			named_attribute_002.inputs[0].default_value = "chain_id"
			
			#node Group Input.005
			group_input_005 = mn_oxdna_style_ribbon.nodes.new("NodeGroupInput")
			group_input_005.name = "Group Input.005"
			group_input_005.outputs[0].hide = True
			group_input_005.outputs[1].hide = True
			group_input_005.outputs[2].hide = True
			group_input_005.outputs[3].hide = True
			group_input_005.outputs[4].hide = True
			group_input_005.outputs[5].hide = True
			group_input_005.outputs[6].hide = True
			group_input_005.outputs[7].hide = True
			group_input_005.outputs[8].hide = True
			group_input_005.outputs[9].hide = True
			group_input_005.outputs[11].hide = True
			group_input_005.outputs[12].hide = True
			
			#node Group Input.006
			group_input_006 = mn_oxdna_style_ribbon.nodes.new("NodeGroupInput")
			group_input_006.name = "Group Input.006"
			group_input_006.outputs[0].hide = True
			group_input_006.outputs[1].hide = True
			group_input_006.outputs[2].hide = True
			group_input_006.outputs[3].hide = True
			group_input_006.outputs[4].hide = True
			group_input_006.outputs[5].hide = True
			group_input_006.outputs[6].hide = True
			group_input_006.outputs[7].hide = True
			group_input_006.outputs[8].hide = True
			group_input_006.outputs[10].hide = True
			group_input_006.outputs[11].hide = True
			group_input_006.outputs[12].hide = True
			
			#node Group Input.002
			group_input_002 = mn_oxdna_style_ribbon.nodes.new("NodeGroupInput")
			group_input_002.name = "Group Input.002"
			group_input_002.outputs[0].hide = True
			group_input_002.outputs[1].hide = True
			group_input_002.outputs[2].hide = True
			group_input_002.outputs[3].hide = True
			group_input_002.outputs[4].hide = True
			group_input_002.outputs[5].hide = True
			group_input_002.outputs[6].hide = True
			group_input_002.outputs[7].hide = True
			group_input_002.outputs[9].hide = True
			group_input_002.outputs[10].hide = True
			group_input_002.outputs[11].hide = True
			group_input_002.outputs[12].hide = True
			
			#node Set Shade Smooth
			set_shade_smooth = mn_oxdna_style_ribbon.nodes.new("GeometryNodeSetShadeSmooth")
			set_shade_smooth.name = "Set Shade Smooth"
			set_shade_smooth.domain = 'FACE'
			#Selection
			set_shade_smooth.inputs[1].default_value = True
			
			#node Group Input.001
			group_input_001 = mn_oxdna_style_ribbon.nodes.new("NodeGroupInput")
			group_input_001.name = "Group Input.001"
			group_input_001.outputs[0].hide = True
			group_input_001.outputs[1].hide = True
			group_input_001.outputs[2].hide = True
			group_input_001.outputs[3].hide = True
			group_input_001.outputs[4].hide = True
			group_input_001.outputs[5].hide = True
			group_input_001.outputs[6].hide = True
			group_input_001.outputs[7].hide = True
			group_input_001.outputs[8].hide = True
			group_input_001.outputs[9].hide = True
			group_input_001.outputs[10].hide = True
			group_input_001.outputs[12].hide = True
			
			#node Instance on Points.001
			instance_on_points_001 = mn_oxdna_style_ribbon.nodes.new("GeometryNodeInstanceOnPoints")
			instance_on_points_001.name = "Instance on Points.001"
			#Selection
			instance_on_points_001.inputs[1].default_value = True
			#Pick Instance
			instance_on_points_001.inputs[3].default_value = False
			#Instance Index
			instance_on_points_001.inputs[4].default_value = 0
			#Scale
			instance_on_points_001.inputs[6].default_value = (1.0, 1.0, 1.0)
			
			#node Align Euler to Vector.002
			align_euler_to_vector_002 = mn_oxdna_style_ribbon.nodes.new("FunctionNodeAlignEulerToVector")
			align_euler_to_vector_002.name = "Align Euler to Vector.002"
			align_euler_to_vector_002.axis = 'X'
			align_euler_to_vector_002.pivot_axis = 'AUTO'
			#Factor
			align_euler_to_vector_002.inputs[1].default_value = 1.0
			
			#node Align Euler to Vector.003
			align_euler_to_vector_003 = mn_oxdna_style_ribbon.nodes.new("FunctionNodeAlignEulerToVector")
			align_euler_to_vector_003.name = "Align Euler to Vector.003"
			align_euler_to_vector_003.axis = 'Z'
			align_euler_to_vector_003.pivot_axis = 'AUTO'
			#Rotation
			align_euler_to_vector_003.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Factor
			align_euler_to_vector_003.inputs[1].default_value = 1.0
			
			#node Vector Math
			vector_math = mn_oxdna_style_ribbon.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.operation = 'SCALE'
			#Scale
			vector_math.inputs[3].default_value = -1.0
			
			#node Group Input
			group_input_2 = mn_oxdna_style_ribbon.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			group_input_2.outputs[2].hide = True
			group_input_2.outputs[8].hide = True
			group_input_2.outputs[11].hide = True
			
			#node Group
			group = mn_oxdna_style_ribbon.nodes.new("GeometryNodeGroup")
			group.name = "Group"
			group.node_tree = _utils_oxdna_base
			#Input_0
			group.inputs[0].default_value = 4.139998912811279
			#Input_1
			group.inputs[1].default_value = 5.420000076293945
			#Input_2
			group.inputs[2].default_value = 3.320000171661377
			
			#node Instance on Points
			instance_on_points = mn_oxdna_style_ribbon.nodes.new("GeometryNodeInstanceOnPoints")
			instance_on_points.name = "Instance on Points"
			#Selection
			instance_on_points.inputs[1].default_value = True
			#Pick Instance
			instance_on_points.inputs[3].default_value = False
			#Instance Index
			instance_on_points.inputs[4].default_value = 0
			
			#node Align Euler to Vector
			align_euler_to_vector = mn_oxdna_style_ribbon.nodes.new("FunctionNodeAlignEulerToVector")
			align_euler_to_vector.name = "Align Euler to Vector"
			align_euler_to_vector.axis = 'X'
			align_euler_to_vector.pivot_axis = 'AUTO'
			#Factor
			align_euler_to_vector.inputs[1].default_value = 1.0
			
			#node Align Euler to Vector.001
			align_euler_to_vector_001 = mn_oxdna_style_ribbon.nodes.new("FunctionNodeAlignEulerToVector")
			align_euler_to_vector_001.name = "Align Euler to Vector.001"
			align_euler_to_vector_001.axis = 'Z'
			align_euler_to_vector_001.pivot_axis = 'AUTO'
			#Rotation
			align_euler_to_vector_001.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Factor
			align_euler_to_vector_001.inputs[1].default_value = 1.0
			
			#node Named Attribute.001
			named_attribute_001 = mn_oxdna_style_ribbon.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_001.inputs[0].default_value = "base_normal"
			
			#node Named Attribute
			named_attribute_1 = mn_oxdna_style_ribbon.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_1.name = "Named Attribute"
			named_attribute_1.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_1.inputs[0].default_value = "base_vector"
			
			#node Group Input.007
			group_input_007 = mn_oxdna_style_ribbon.nodes.new("NodeGroupInput")
			group_input_007.name = "Group Input.007"
			group_input_007.outputs[0].hide = True
			group_input_007.outputs[1].hide = True
			group_input_007.outputs[2].hide = True
			group_input_007.outputs[3].hide = True
			group_input_007.outputs[4].hide = True
			group_input_007.outputs[5].hide = True
			group_input_007.outputs[6].hide = True
			group_input_007.outputs[8].hide = True
			group_input_007.outputs[9].hide = True
			group_input_007.outputs[10].hide = True
			group_input_007.outputs[11].hide = True
			group_input_007.outputs[12].hide = True
			
			#node Group.002
			group_002 = mn_oxdna_style_ribbon.nodes.new("GeometryNodeGroup")
			group_002.name = "Group.002"
			group_002.node_tree = _utils_oxdna_base
			#Input_0
			group_002.inputs[0].default_value = 1.4999992847442627
			#Input_1
			group_002.inputs[1].default_value = 6.119998931884766
			#Input_2
			group_002.inputs[2].default_value = 5.0
			
			#node Group Input.004
			group_input_004 = mn_oxdna_style_ribbon.nodes.new("NodeGroupInput")
			group_input_004.name = "Group Input.004"
			group_input_004.outputs[0].hide = True
			group_input_004.outputs[1].hide = True
			group_input_004.outputs[2].hide = True
			group_input_004.outputs[7].hide = True
			group_input_004.outputs[8].hide = True
			group_input_004.outputs[9].hide = True
			group_input_004.outputs[10].hide = True
			group_input_004.outputs[11].hide = True
			group_input_004.outputs[12].hide = True
			
			#node Group.001
			group_001 = mn_oxdna_style_ribbon.nodes.new("GeometryNodeGroup")
			group_001.label = "Res Name Nucleic"
			group_001.name = "Group.001"
			group_001.node_tree = color_res_name_nucleic
			
			#node Store Named Attribute
			store_named_attribute = mn_oxdna_style_ribbon.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute.name = "Store Named Attribute"
			store_named_attribute.data_type = 'FLOAT_COLOR'
			store_named_attribute.domain = 'POINT'
			#Selection
			store_named_attribute.inputs[1].default_value = True
			#Name
			store_named_attribute.inputs[2].default_value = "Color"
			
			#node Named Attribute.006
			named_attribute_006 = mn_oxdna_style_ribbon.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_006.name = "Named Attribute.006"
			named_attribute_006.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_006.inputs[0].default_value = "base_normal"
			
			
			
			#Set parents
			vector_math_004.parent = frame
			vector_math_005.parent = frame
			vector_math_002.parent = frame
			named_attribute_004.parent = frame
			vector_math_003.parent = frame
			named_attribute_003.parent = frame
			
			#Set locations
			frame.location = (0.0, 0.0)
			group_output_2.location = (1850.05322265625, 0.0)
			set_material.location = (1660.05322265625, 118.50094604492188)
			join_geometry.location = (1140.0, 80.0)
			group_input_003.location = (1459.3980712890625, -5.569933891296387)
			capture_attribute.location = (-1220.0, 140.0)
			separate_geometry.location = (-1460.0, 20.0)
			reroute_1.location = (-920.0, 120.0)
			set_position_001.location = (-760.0, 420.0)
			vector_math_004.location = (-1760.0, 360.0)
			vector_math_005.location = (-1600.0, 360.0)
			vector_math_002.location = (-1600.0, 500.0)
			named_attribute_004.location = (-1980.0, 360.0)
			vector_math_003.location = (-1760.0, 500.0)
			named_attribute_003.location = (-1980.0, 500.0)
			set_curve_radius.location = (-40.0, 660.0)
			math_1.location = (-40.0, 520.0)
			points_to_curves.location = (-220.0, 660.0)
			mesh_to_points.location = (-380.0, 660.0)
			set_spline_type.location = (120.0, 660.0)
			set_handle_type.location = (300.0, 660.0)
			curve_to_mesh.location = (640.0, 660.0)
			set_spline_resolution.location = (460.0, 660.0)
			curve_circle.location = (640.0, 520.0)
			named_attribute_002.location = (-380.0, 480.0)
			group_input_005.location = (-200.0, 500.0)
			group_input_006.location = (460.0, 520.0)
			group_input_002.location = (460.0, 440.0)
			set_shade_smooth.location = (860.0, 660.0)
			group_input_001.location = (860.0, 500.0)
			instance_on_points_001.location = (660.0, 200.0)
			align_euler_to_vector_002.location = (220.0, 100.0)
			align_euler_to_vector_003.location = (40.0, 60.0)
			vector_math.location = (-140.0, 0.0)
			group_input_2.location = (-1660.0, 20.0)
			group.location = (700.0, -360.0)
			instance_on_points.location = (920.0, -260.0)
			align_euler_to_vector.location = (700.0, -520.0)
			align_euler_to_vector_001.location = (540.0, -520.0)
			named_attribute_001.location = (700.0, -700.0)
			named_attribute_1.location = (540.0, -720.0)
			group_input_007.location = (920.0, -480.0)
			group_002.location = (220.0, 260.0)
			group_input_004.location = (-116.71331787109375, -364.2935791015625)
			group_001.location = (80.0, -400.0)
			store_named_attribute.location = (480.0, -200.0)
			named_attribute_006.location = (180.28485107421875, -100.0)
			
			#Set dimensions
			frame.width, frame.height = 580.0, 336.0
			group_output_2.width, group_output_2.height = 140.0, 100.0
			set_material.width, set_material.height = 140.0, 100.0
			join_geometry.width, join_geometry.height = 140.0, 100.0
			group_input_003.width, group_input_003.height = 140.0, 100.0
			capture_attribute.width, capture_attribute.height = 140.0, 100.0
			separate_geometry.width, separate_geometry.height = 140.0, 100.0
			reroute_1.width, reroute_1.height = 16.0, 100.0
			set_position_001.width, set_position_001.height = 140.0, 100.0
			vector_math_004.width, vector_math_004.height = 140.0, 100.0
			vector_math_005.width, vector_math_005.height = 140.0, 100.0
			vector_math_002.width, vector_math_002.height = 140.0, 100.0
			named_attribute_004.width, named_attribute_004.height = 188.748779296875, 100.0
			vector_math_003.width, vector_math_003.height = 140.0, 100.0
			named_attribute_003.width, named_attribute_003.height = 188.748779296875, 100.0
			set_curve_radius.width, set_curve_radius.height = 140.0, 100.0
			math_1.width, math_1.height = 140.0, 100.0
			points_to_curves.width, points_to_curves.height = 140.0, 100.0
			mesh_to_points.width, mesh_to_points.height = 140.0, 100.0
			set_spline_type.width, set_spline_type.height = 140.0, 100.0
			set_handle_type.width, set_handle_type.height = 140.0, 100.0
			curve_to_mesh.width, curve_to_mesh.height = 140.0, 100.0
			set_spline_resolution.width, set_spline_resolution.height = 140.0, 100.0
			curve_circle.width, curve_circle.height = 140.0, 100.0
			named_attribute_002.width, named_attribute_002.height = 140.0, 100.0
			group_input_005.width, group_input_005.height = 141.8651123046875, 100.0
			group_input_006.width, group_input_006.height = 141.8651123046875, 100.0
			group_input_002.width, group_input_002.height = 140.0, 100.0
			set_shade_smooth.width, set_shade_smooth.height = 140.0, 100.0
			group_input_001.width, group_input_001.height = 140.0, 100.0
			instance_on_points_001.width, instance_on_points_001.height = 140.0, 100.0
			align_euler_to_vector_002.width, align_euler_to_vector_002.height = 140.0, 100.0
			align_euler_to_vector_003.width, align_euler_to_vector_003.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			group_input_2.width, group_input_2.height = 141.8651123046875, 100.0
			group.width, group.height = 140.0, 100.0
			instance_on_points.width, instance_on_points.height = 125.27001953125, 100.0
			align_euler_to_vector.width, align_euler_to_vector.height = 140.0, 100.0
			align_euler_to_vector_001.width, align_euler_to_vector_001.height = 140.0, 100.0
			named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
			named_attribute_1.width, named_attribute_1.height = 140.0, 100.0
			group_input_007.width, group_input_007.height = 122.67431640625, 100.0
			group_002.width, group_002.height = 214.42431640625, 100.0
			group_input_004.width, group_input_004.height = 154.56005859375, 100.0
			group_001.width, group_001.height = 298.75079345703125, 100.0
			store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
			named_attribute_006.width, named_attribute_006.height = 179.71514892578125, 100.0
			
			#initialize mn_oxdna_style_ribbon links
			#join_geometry.Geometry -> set_material.Geometry
			mn_oxdna_style_ribbon.links.new(join_geometry.outputs[0], set_material.inputs[0])
			#math_1.Value -> set_curve_radius.Radius
			mn_oxdna_style_ribbon.links.new(math_1.outputs[0], set_curve_radius.inputs[2])
			#group.Geometry -> instance_on_points.Instance
			mn_oxdna_style_ribbon.links.new(group.outputs[0], instance_on_points.inputs[2])
			#set_spline_resolution.Geometry -> curve_to_mesh.Curve
			mn_oxdna_style_ribbon.links.new(set_spline_resolution.outputs[0], curve_to_mesh.inputs[0])
			#instance_on_points.Instances -> join_geometry.Geometry
			mn_oxdna_style_ribbon.links.new(instance_on_points.outputs[0], join_geometry.inputs[0])
			#set_position_001.Geometry -> mesh_to_points.Mesh
			mn_oxdna_style_ribbon.links.new(set_position_001.outputs[0], mesh_to_points.inputs[0])
			#align_euler_to_vector.Rotation -> instance_on_points.Rotation
			mn_oxdna_style_ribbon.links.new(align_euler_to_vector.outputs[0], instance_on_points.inputs[5])
			#points_to_curves.Curves -> set_curve_radius.Curve
			mn_oxdna_style_ribbon.links.new(points_to_curves.outputs[0], set_curve_radius.inputs[0])
			#mesh_to_points.Points -> points_to_curves.Points
			mn_oxdna_style_ribbon.links.new(mesh_to_points.outputs[0], points_to_curves.inputs[0])
			#curve_circle.Curve -> curve_to_mesh.Profile Curve
			mn_oxdna_style_ribbon.links.new(curve_circle.outputs[0], curve_to_mesh.inputs[1])
			#named_attribute_002.Attribute -> points_to_curves.Curve Group ID
			mn_oxdna_style_ribbon.links.new(named_attribute_002.outputs[0], points_to_curves.inputs[1])
			#align_euler_to_vector_001.Rotation -> align_euler_to_vector.Rotation
			mn_oxdna_style_ribbon.links.new(align_euler_to_vector_001.outputs[0], align_euler_to_vector.inputs[0])
			#set_material.Geometry -> group_output_2.DNA Mesh
			mn_oxdna_style_ribbon.links.new(set_material.outputs[0], group_output_2.inputs[0])
			#set_curve_radius.Curve -> set_spline_type.Curve
			mn_oxdna_style_ribbon.links.new(set_curve_radius.outputs[0], set_spline_type.inputs[0])
			#set_handle_type.Curve -> set_spline_resolution.Geometry
			mn_oxdna_style_ribbon.links.new(set_handle_type.outputs[0], set_spline_resolution.inputs[0])
			#set_spline_type.Curve -> set_handle_type.Curve
			mn_oxdna_style_ribbon.links.new(set_spline_type.outputs[0], set_handle_type.inputs[0])
			#curve_to_mesh.Mesh -> set_shade_smooth.Geometry
			mn_oxdna_style_ribbon.links.new(curve_to_mesh.outputs[0], set_shade_smooth.inputs[0])
			#group_input_001.Backbone Shade Smooth -> set_shade_smooth.Shade Smooth
			mn_oxdna_style_ribbon.links.new(group_input_001.outputs[11], set_shade_smooth.inputs[2])
			#group_input_2.DNA Bases -> separate_geometry.Geometry
			mn_oxdna_style_ribbon.links.new(group_input_2.outputs[0], separate_geometry.inputs[0])
			#group_input_2.Selection -> separate_geometry.Selection
			mn_oxdna_style_ribbon.links.new(group_input_2.outputs[1], separate_geometry.inputs[1])
			#group_input_002.Backbone Resolution -> curve_circle.Resolution
			mn_oxdna_style_ribbon.links.new(group_input_002.outputs[8], curve_circle.inputs[0])
			#group_input_003.Material -> set_material.Material
			mn_oxdna_style_ribbon.links.new(group_input_003.outputs[2], set_material.inputs[2])
			#named_attribute_001.Attribute -> align_euler_to_vector.Vector
			mn_oxdna_style_ribbon.links.new(named_attribute_001.outputs[0], align_euler_to_vector.inputs[2])
			#named_attribute_1.Attribute -> align_euler_to_vector_001.Vector
			mn_oxdna_style_ribbon.links.new(named_attribute_1.outputs[0], align_euler_to_vector_001.inputs[2])
			#store_named_attribute.Geometry -> instance_on_points.Points
			mn_oxdna_style_ribbon.links.new(store_named_attribute.outputs[0], instance_on_points.inputs[0])
			#reroute_1.Output -> set_position_001.Geometry
			mn_oxdna_style_ribbon.links.new(reroute_1.outputs[0], set_position_001.inputs[0])
			#vector_math_003.Vector -> vector_math_002.Vector
			mn_oxdna_style_ribbon.links.new(vector_math_003.outputs[0], vector_math_002.inputs[0])
			#vector_math_005.Vector -> vector_math_002.Vector
			mn_oxdna_style_ribbon.links.new(vector_math_005.outputs[0], vector_math_002.inputs[1])
			#named_attribute_003.Attribute -> vector_math_003.Vector
			mn_oxdna_style_ribbon.links.new(named_attribute_003.outputs[0], vector_math_003.inputs[0])
			#named_attribute_004.Attribute -> vector_math_004.Vector
			mn_oxdna_style_ribbon.links.new(named_attribute_004.outputs[0], vector_math_004.inputs[1])
			#named_attribute_003.Attribute -> vector_math_004.Vector
			mn_oxdna_style_ribbon.links.new(named_attribute_003.outputs[0], vector_math_004.inputs[0])
			#vector_math_004.Vector -> vector_math_005.Vector
			mn_oxdna_style_ribbon.links.new(vector_math_004.outputs[0], vector_math_005.inputs[0])
			#group_input_004.A -> group_001.A
			mn_oxdna_style_ribbon.links.new(group_input_004.outputs[3], group_001.inputs[0])
			#group_input_004.C -> group_001.C
			mn_oxdna_style_ribbon.links.new(group_input_004.outputs[4], group_001.inputs[1])
			#group_input_004.G -> group_001.G
			mn_oxdna_style_ribbon.links.new(group_input_004.outputs[5], group_001.inputs[2])
			#group_input_004.T / U -> group_001.T / U
			mn_oxdna_style_ribbon.links.new(group_input_004.outputs[6], group_001.inputs[3])
			#set_position_001.Geometry -> instance_on_points_001.Points
			mn_oxdna_style_ribbon.links.new(set_position_001.outputs[0], instance_on_points_001.inputs[0])
			#group_002.Geometry -> instance_on_points_001.Instance
			mn_oxdna_style_ribbon.links.new(group_002.outputs[0], instance_on_points_001.inputs[2])
			#align_euler_to_vector_003.Rotation -> align_euler_to_vector_002.Rotation
			mn_oxdna_style_ribbon.links.new(align_euler_to_vector_003.outputs[0], align_euler_to_vector_002.inputs[0])
			#named_attribute_006.Attribute -> align_euler_to_vector_002.Vector
			mn_oxdna_style_ribbon.links.new(named_attribute_006.outputs[0], align_euler_to_vector_002.inputs[2])
			#align_euler_to_vector_002.Rotation -> instance_on_points_001.Rotation
			mn_oxdna_style_ribbon.links.new(align_euler_to_vector_002.outputs[0], instance_on_points_001.inputs[5])
			#vector_math.Vector -> align_euler_to_vector_003.Vector
			mn_oxdna_style_ribbon.links.new(vector_math.outputs[0], align_euler_to_vector_003.inputs[2])
			#group_input_005.Backbone Radius -> math_1.Value
			mn_oxdna_style_ribbon.links.new(group_input_005.outputs[10], math_1.inputs[0])
			#group_input_006.Backbone Subdivisions -> set_spline_resolution.Resolution
			mn_oxdna_style_ribbon.links.new(group_input_006.outputs[9], set_spline_resolution.inputs[2])
			#capture_attribute.Geometry -> reroute_1.Input
			mn_oxdna_style_ribbon.links.new(capture_attribute.outputs[0], reroute_1.inputs[0])
			#separate_geometry.Selection -> capture_attribute.Geometry
			mn_oxdna_style_ribbon.links.new(separate_geometry.outputs[0], capture_attribute.inputs[0])
			#vector_math_002.Vector -> capture_attribute.Value
			mn_oxdna_style_ribbon.links.new(vector_math_002.outputs[0], capture_attribute.inputs[1])
			#capture_attribute.Value -> set_position_001.Offset
			mn_oxdna_style_ribbon.links.new(capture_attribute.outputs[1], set_position_001.inputs[3])
			#capture_attribute.Value -> vector_math.Vector
			mn_oxdna_style_ribbon.links.new(capture_attribute.outputs[1], vector_math.inputs[0])
			#group_input_007.Base Scale -> instance_on_points.Scale
			mn_oxdna_style_ribbon.links.new(group_input_007.outputs[7], instance_on_points.inputs[6])
			#reroute_1.Output -> store_named_attribute.Geometry
			mn_oxdna_style_ribbon.links.new(reroute_1.outputs[0], store_named_attribute.inputs[0])
			#group_001.Color -> store_named_attribute.Value
			mn_oxdna_style_ribbon.links.new(group_001.outputs[0], store_named_attribute.inputs[3])
			#set_shade_smooth.Geometry -> join_geometry.Geometry
			mn_oxdna_style_ribbon.links.new(set_shade_smooth.outputs[0], join_geometry.inputs[0])
			#instance_on_points_001.Instances -> join_geometry.Geometry
			mn_oxdna_style_ribbon.links.new(instance_on_points_001.outputs[0], join_geometry.inputs[0])
			return mn_oxdna_style_ribbon

		mn_oxdna_style_ribbon = mn_oxdna_style_ribbon_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "MN_oxdna_style_ribbon", type = 'NODES')
		mod.node_group = mn_oxdna_style_ribbon
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(MN_oxdna_style_ribbon.bl_idname)
			
def register():
	bpy.utils.register_class(MN_oxdna_style_ribbon)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(MN_oxdna_style_ribbon)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
