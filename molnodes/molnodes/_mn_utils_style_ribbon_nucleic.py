bl_info = {
	"name" : ".MN_utils_style_ribbon_nucleic",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _MN_utils_style_ribbon_nucleic(bpy.types.Operator):
	bl_idname = "node._mn_utils_style_ribbon_nucleic"
	bl_label = ".MN_utils_style_ribbon_nucleic"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _sampleatomvalue node group
		def _sampleatomvalue_node_group():
			_sampleatomvalue = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".SampleAtomValue")

			_sampleatomvalue.color_tag = 'NONE'
			_sampleatomvalue.description = ""

			_sampleatomvalue.is_modifier = True
			
			#_sampleatomvalue interface
			#Socket Atoms
			atoms_socket = _sampleatomvalue.interface.new_socket(name = "Atoms", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket = _sampleatomvalue.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			value_socket.default_value = (0.0, 0.0, 0.0)
			value_socket.min_value = -3.4028234663852886e+38
			value_socket.max_value = 3.4028234663852886e+38
			value_socket.subtype = 'NONE'
			value_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_1 = _sampleatomvalue.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketColor')
			value_socket_1.default_value = (0.0, 0.0, 0.0, 0.0)
			value_socket_1.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket = _sampleatomvalue.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket.attribute_domain = 'POINT'
			
			#Socket B
			b_socket = _sampleatomvalue.interface.new_socket(name = "B", in_out='INPUT', socket_type = 'NodeSocketInt')
			b_socket.default_value = 57
			b_socket.min_value = -2147483648
			b_socket.max_value = 2147483647
			b_socket.subtype = 'NONE'
			b_socket.attribute_domain = 'POINT'
			
			
			#initialize _sampleatomvalue nodes
			#node Group Output
			group_output = _sampleatomvalue.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Named Attribute.009
			named_attribute_009 = _sampleatomvalue.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_009.name = "Named Attribute.009"
			named_attribute_009.data_type = 'INT'
			#Name
			named_attribute_009.inputs[0].default_value = "atom_name"
			
			#node Index.005
			index_005 = _sampleatomvalue.nodes.new("GeometryNodeInputIndex")
			index_005.name = "Index.005"
			
			#node Position.002
			position_002 = _sampleatomvalue.nodes.new("GeometryNodeInputPosition")
			position_002.name = "Position.002"
			
			#node Compare.003
			compare_003 = _sampleatomvalue.nodes.new("FunctionNodeCompare")
			compare_003.name = "Compare.003"
			compare_003.data_type = 'INT'
			compare_003.mode = 'ELEMENT'
			compare_003.operation = 'EQUAL'
			
			#node Group Input
			group_input = _sampleatomvalue.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Sample Index.009
			sample_index_009 = _sampleatomvalue.nodes.new("GeometryNodeSampleIndex")
			sample_index_009.name = "Sample Index.009"
			sample_index_009.clamp = False
			sample_index_009.data_type = 'FLOAT_VECTOR'
			sample_index_009.domain = 'POINT'
			
			#node Named Attribute
			named_attribute = _sampleatomvalue.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute.inputs[0].default_value = "Color"
			
			#node Sample Index.010
			sample_index_010 = _sampleatomvalue.nodes.new("GeometryNodeSampleIndex")
			sample_index_010.name = "Sample Index.010"
			sample_index_010.clamp = False
			sample_index_010.data_type = 'FLOAT_COLOR'
			sample_index_010.domain = 'POINT'
			
			#node Separate Geometry.002
			separate_geometry_002 = _sampleatomvalue.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_002.name = "Separate Geometry.002"
			separate_geometry_002.domain = 'POINT'
			
			
			
			
			#Set locations
			group_output.location = (390.0, 0.0)
			named_attribute_009.location = (-200.0, -107.52880859375)
			index_005.location = (40.0, -47.52880859375)
			position_002.location = (40.0, 12.47119140625)
			compare_003.location = (40.2109375, -112.47119140625)
			group_input.location = (-170.3642578125, -265.140380859375)
			sample_index_009.location = (200.0, 112.47119140625)
			named_attribute.location = (40.0, -380.0)
			sample_index_010.location = (200.0, -280.0)
			separate_geometry_002.location = (200.0, -107.52880859375)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			named_attribute_009.width, named_attribute_009.height = 206.99917602539062, 100.0
			index_005.width, index_005.height = 140.0, 100.0
			position_002.width, position_002.height = 140.0, 100.0
			compare_003.width, compare_003.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			sample_index_009.width, sample_index_009.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			sample_index_010.width, sample_index_010.height = 140.0, 100.0
			separate_geometry_002.width, separate_geometry_002.height = 140.0, 100.0
			
			#initialize _sampleatomvalue links
			#index_005.Index -> sample_index_009.Index
			_sampleatomvalue.links.new(index_005.outputs[0], sample_index_009.inputs[2])
			#compare_003.Result -> separate_geometry_002.Selection
			_sampleatomvalue.links.new(compare_003.outputs[0], separate_geometry_002.inputs[1])
			#named_attribute_009.Attribute -> compare_003.A
			_sampleatomvalue.links.new(named_attribute_009.outputs[0], compare_003.inputs[2])
			#separate_geometry_002.Selection -> sample_index_009.Geometry
			_sampleatomvalue.links.new(separate_geometry_002.outputs[0], sample_index_009.inputs[0])
			#position_002.Position -> sample_index_009.Value
			_sampleatomvalue.links.new(position_002.outputs[0], sample_index_009.inputs[1])
			#group_input.Geometry -> separate_geometry_002.Geometry
			_sampleatomvalue.links.new(group_input.outputs[0], separate_geometry_002.inputs[0])
			#group_input.B -> compare_003.B
			_sampleatomvalue.links.new(group_input.outputs[1], compare_003.inputs[3])
			#sample_index_009.Value -> group_output.Value
			_sampleatomvalue.links.new(sample_index_009.outputs[0], group_output.inputs[1])
			#index_005.Index -> sample_index_010.Index
			_sampleatomvalue.links.new(index_005.outputs[0], sample_index_010.inputs[2])
			#separate_geometry_002.Selection -> sample_index_010.Geometry
			_sampleatomvalue.links.new(separate_geometry_002.outputs[0], sample_index_010.inputs[0])
			#named_attribute.Attribute -> sample_index_010.Value
			_sampleatomvalue.links.new(named_attribute.outputs[0], sample_index_010.inputs[1])
			#sample_index_010.Value -> group_output.Value
			_sampleatomvalue.links.new(sample_index_010.outputs[0], group_output.inputs[2])
			#separate_geometry_002.Selection -> group_output.Atoms
			_sampleatomvalue.links.new(separate_geometry_002.outputs[0], group_output.inputs[0])
			return _sampleatomvalue

		_sampleatomvalue = _sampleatomvalue_node_group()

		#initialize mn_select_nucleic_type node group
		def mn_select_nucleic_type_node_group():
			mn_select_nucleic_type = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "MN_select_nucleic_type")

			mn_select_nucleic_type.color_tag = 'NONE'
			mn_select_nucleic_type.description = ""

			
			#mn_select_nucleic_type interface
			#Socket is_purine
			is_purine_socket = mn_select_nucleic_type.interface.new_socket(name = "is_purine", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_purine_socket.default_value = False
			is_purine_socket.attribute_domain = 'POINT'
			
			#Socket is_pyrimidine
			is_pyrimidine_socket = mn_select_nucleic_type.interface.new_socket(name = "is_pyrimidine", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_pyrimidine_socket.default_value = False
			is_pyrimidine_socket.attribute_domain = 'POINT'
			
			
			#initialize mn_select_nucleic_type nodes
			#node Group Input
			group_input_1 = mn_select_nucleic_type.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			
			#node Reroute.015
			reroute_015 = mn_select_nucleic_type.nodes.new("NodeReroute")
			reroute_015.name = "Reroute.015"
			#node Named Attribute.010
			named_attribute_010 = mn_select_nucleic_type.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_010.name = "Named Attribute.010"
			named_attribute_010.data_type = 'INT'
			#Name
			named_attribute_010.inputs[0].default_value = "res_name"
			
			#node Compare.007
			compare_007 = mn_select_nucleic_type.nodes.new("FunctionNodeCompare")
			compare_007.name = "Compare.007"
			compare_007.data_type = 'INT'
			compare_007.mode = 'ELEMENT'
			compare_007.operation = 'EQUAL'
			#B_INT
			compare_007.inputs[3].default_value = 33
			
			#node Compare.016
			compare_016 = mn_select_nucleic_type.nodes.new("FunctionNodeCompare")
			compare_016.name = "Compare.016"
			compare_016.data_type = 'INT'
			compare_016.mode = 'ELEMENT'
			compare_016.operation = 'EQUAL'
			#B_INT
			compare_016.inputs[3].default_value = 43
			
			#node Compare.008
			compare_008 = mn_select_nucleic_type.nodes.new("FunctionNodeCompare")
			compare_008.name = "Compare.008"
			compare_008.data_type = 'INT'
			compare_008.mode = 'ELEMENT'
			compare_008.operation = 'EQUAL'
			#B_INT
			compare_008.inputs[3].default_value = 31
			
			#node Compare.015
			compare_015 = mn_select_nucleic_type.nodes.new("FunctionNodeCompare")
			compare_015.name = "Compare.015"
			compare_015.data_type = 'INT'
			compare_015.mode = 'ELEMENT'
			compare_015.operation = 'EQUAL'
			#B_INT
			compare_015.inputs[3].default_value = 41
			
			#node Boolean Math.012
			boolean_math_012 = mn_select_nucleic_type.nodes.new("FunctionNodeBooleanMath")
			boolean_math_012.name = "Boolean Math.012"
			boolean_math_012.operation = 'OR'
			
			#node Boolean Math.013
			boolean_math_013 = mn_select_nucleic_type.nodes.new("FunctionNodeBooleanMath")
			boolean_math_013.name = "Boolean Math.013"
			boolean_math_013.operation = 'OR'
			
			#node Boolean Math.007
			boolean_math_007 = mn_select_nucleic_type.nodes.new("FunctionNodeBooleanMath")
			boolean_math_007.name = "Boolean Math.007"
			boolean_math_007.operation = 'OR'
			
			#node Group Output
			group_output_1 = mn_select_nucleic_type.nodes.new("NodeGroupOutput")
			group_output_1.name = "Group Output"
			group_output_1.is_active_output = True
			
			#node Compare.017
			compare_017 = mn_select_nucleic_type.nodes.new("FunctionNodeCompare")
			compare_017.name = "Compare.017"
			compare_017.data_type = 'INT'
			compare_017.mode = 'ELEMENT'
			compare_017.operation = 'EQUAL'
			#B_INT
			compare_017.inputs[3].default_value = 42
			
			#node Compare.010
			compare_010 = mn_select_nucleic_type.nodes.new("FunctionNodeCompare")
			compare_010.name = "Compare.010"
			compare_010.data_type = 'INT'
			compare_010.mode = 'ELEMENT'
			compare_010.operation = 'EQUAL'
			#B_INT
			compare_010.inputs[3].default_value = 30
			
			#node Compare.018
			compare_018 = mn_select_nucleic_type.nodes.new("FunctionNodeCompare")
			compare_018.name = "Compare.018"
			compare_018.data_type = 'INT'
			compare_018.mode = 'ELEMENT'
			compare_018.operation = 'EQUAL'
			#B_INT
			compare_018.inputs[3].default_value = 40
			
			#node Boolean Math.014
			boolean_math_014 = mn_select_nucleic_type.nodes.new("FunctionNodeBooleanMath")
			boolean_math_014.name = "Boolean Math.014"
			boolean_math_014.operation = 'OR'
			
			#node Boolean Math.015
			boolean_math_015 = mn_select_nucleic_type.nodes.new("FunctionNodeBooleanMath")
			boolean_math_015.name = "Boolean Math.015"
			boolean_math_015.operation = 'OR'
			
			#node Compare.009
			compare_009 = mn_select_nucleic_type.nodes.new("FunctionNodeCompare")
			compare_009.name = "Compare.009"
			compare_009.data_type = 'INT'
			compare_009.mode = 'ELEMENT'
			compare_009.operation = 'EQUAL'
			#B_INT
			compare_009.inputs[3].default_value = 32
			
			#node Boolean Math.008
			boolean_math_008 = mn_select_nucleic_type.nodes.new("FunctionNodeBooleanMath")
			boolean_math_008.name = "Boolean Math.008"
			boolean_math_008.operation = 'OR'
			
			
			
			
			#Set locations
			group_input_1.location = (-570.0, 0.0)
			reroute_015.location = (-150.0, -97.31201171875)
			named_attribute_010.location = (-420.0, -60.0)
			compare_007.location = (-30.0, -90.0)
			compare_016.location = (-30.0, -250.0)
			compare_008.location = (-30.0, 249.9998779296875)
			compare_015.location = (-30.0, 89.9998779296875)
			boolean_math_012.location = (170.0, 249.9998779296875)
			boolean_math_013.location = (150.0, -90.0)
			boolean_math_007.location = (370.0, 249.9998779296875)
			group_output_1.location = (580.0, 240.0)
			compare_017.location = (-40.0, -940.0)
			compare_010.location = (-40.0, -440.0)
			compare_018.location = (-40.0, -600.0)
			boolean_math_014.location = (160.0, -440.0)
			boolean_math_015.location = (140.0, -780.0)
			compare_009.location = (-40.0, -780.0)
			boolean_math_008.location = (360.0, -440.0)
			
			#Set dimensions
			group_input_1.width, group_input_1.height = 140.0, 100.0
			reroute_015.width, reroute_015.height = 16.0, 100.0
			named_attribute_010.width, named_attribute_010.height = 206.99917602539062, 100.0
			compare_007.width, compare_007.height = 140.0, 100.0
			compare_016.width, compare_016.height = 140.0, 100.0
			compare_008.width, compare_008.height = 140.0, 100.0
			compare_015.width, compare_015.height = 140.0, 100.0
			boolean_math_012.width, boolean_math_012.height = 140.0, 100.0
			boolean_math_013.width, boolean_math_013.height = 140.0, 100.0
			boolean_math_007.width, boolean_math_007.height = 140.0, 100.0
			group_output_1.width, group_output_1.height = 140.0, 100.0
			compare_017.width, compare_017.height = 140.0, 100.0
			compare_010.width, compare_010.height = 140.0, 100.0
			compare_018.width, compare_018.height = 140.0, 100.0
			boolean_math_014.width, boolean_math_014.height = 140.0, 100.0
			boolean_math_015.width, boolean_math_015.height = 140.0, 100.0
			compare_009.width, compare_009.height = 140.0, 100.0
			boolean_math_008.width, boolean_math_008.height = 140.0, 100.0
			
			#initialize mn_select_nucleic_type links
			#compare_016.Result -> boolean_math_013.Boolean
			mn_select_nucleic_type.links.new(compare_016.outputs[0], boolean_math_013.inputs[1])
			#reroute_015.Output -> compare_016.A
			mn_select_nucleic_type.links.new(reroute_015.outputs[0], compare_016.inputs[2])
			#boolean_math_012.Boolean -> boolean_math_007.Boolean
			mn_select_nucleic_type.links.new(boolean_math_012.outputs[0], boolean_math_007.inputs[0])
			#boolean_math_013.Boolean -> boolean_math_007.Boolean
			mn_select_nucleic_type.links.new(boolean_math_013.outputs[0], boolean_math_007.inputs[1])
			#reroute_015.Output -> compare_008.A
			mn_select_nucleic_type.links.new(reroute_015.outputs[0], compare_008.inputs[2])
			#compare_008.Result -> boolean_math_012.Boolean
			mn_select_nucleic_type.links.new(compare_008.outputs[0], boolean_math_012.inputs[0])
			#compare_007.Result -> boolean_math_013.Boolean
			mn_select_nucleic_type.links.new(compare_007.outputs[0], boolean_math_013.inputs[0])
			#reroute_015.Output -> compare_007.A
			mn_select_nucleic_type.links.new(reroute_015.outputs[0], compare_007.inputs[2])
			#reroute_015.Output -> compare_015.A
			mn_select_nucleic_type.links.new(reroute_015.outputs[0], compare_015.inputs[2])
			#compare_015.Result -> boolean_math_012.Boolean
			mn_select_nucleic_type.links.new(compare_015.outputs[0], boolean_math_012.inputs[1])
			#named_attribute_010.Attribute -> reroute_015.Input
			mn_select_nucleic_type.links.new(named_attribute_010.outputs[0], reroute_015.inputs[0])
			#boolean_math_007.Boolean -> group_output_1.is_pyrimidine
			mn_select_nucleic_type.links.new(boolean_math_007.outputs[0], group_output_1.inputs[1])
			#compare_017.Result -> boolean_math_015.Boolean
			mn_select_nucleic_type.links.new(compare_017.outputs[0], boolean_math_015.inputs[1])
			#reroute_015.Output -> compare_017.A
			mn_select_nucleic_type.links.new(reroute_015.outputs[0], compare_017.inputs[2])
			#boolean_math_014.Boolean -> boolean_math_008.Boolean
			mn_select_nucleic_type.links.new(boolean_math_014.outputs[0], boolean_math_008.inputs[0])
			#boolean_math_015.Boolean -> boolean_math_008.Boolean
			mn_select_nucleic_type.links.new(boolean_math_015.outputs[0], boolean_math_008.inputs[1])
			#reroute_015.Output -> compare_010.A
			mn_select_nucleic_type.links.new(reroute_015.outputs[0], compare_010.inputs[2])
			#compare_010.Result -> boolean_math_014.Boolean
			mn_select_nucleic_type.links.new(compare_010.outputs[0], boolean_math_014.inputs[0])
			#compare_009.Result -> boolean_math_015.Boolean
			mn_select_nucleic_type.links.new(compare_009.outputs[0], boolean_math_015.inputs[0])
			#reroute_015.Output -> compare_009.A
			mn_select_nucleic_type.links.new(reroute_015.outputs[0], compare_009.inputs[2])
			#reroute_015.Output -> compare_018.A
			mn_select_nucleic_type.links.new(reroute_015.outputs[0], compare_018.inputs[2])
			#compare_018.Result -> boolean_math_014.Boolean
			mn_select_nucleic_type.links.new(compare_018.outputs[0], boolean_math_014.inputs[1])
			#boolean_math_008.Boolean -> group_output_1.is_purine
			mn_select_nucleic_type.links.new(boolean_math_008.outputs[0], group_output_1.inputs[0])
			return mn_select_nucleic_type

		mn_select_nucleic_type = mn_select_nucleic_type_node_group()

		#initialize _base_align node group
		def _base_align_node_group():
			_base_align = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".Base align")

			_base_align.color_tag = 'NONE'
			_base_align.description = ""

			
			#_base_align interface
			#Socket Base Interface
			base_interface_socket = _base_align.interface.new_socket(name = "Base Interface", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			base_interface_socket.default_value = (0.0, 0.0, 0.0)
			base_interface_socket.min_value = -3.4028234663852886e+38
			base_interface_socket.max_value = 3.4028234663852886e+38
			base_interface_socket.subtype = 'NONE'
			base_interface_socket.attribute_domain = 'POINT'
			
			#Socket Base Pivot
			base_pivot_socket = _base_align.interface.new_socket(name = "Base Pivot", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			base_pivot_socket.default_value = (0.0, 0.0, 0.0)
			base_pivot_socket.min_value = -3.4028234663852886e+38
			base_pivot_socket.max_value = 3.4028234663852886e+38
			base_pivot_socket.subtype = 'NONE'
			base_pivot_socket.attribute_domain = 'POINT'
			
			#Socket Align Vertical
			align_vertical_socket = _base_align.interface.new_socket(name = "Align Vertical", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			align_vertical_socket.default_value = (0.0, 0.0, 0.0)
			align_vertical_socket.min_value = -3.4028234663852886e+38
			align_vertical_socket.max_value = 3.4028234663852886e+38
			align_vertical_socket.subtype = 'NONE'
			align_vertical_socket.attribute_domain = 'POINT'
			
			#Socket Align Horizontal
			align_horizontal_socket = _base_align.interface.new_socket(name = "Align Horizontal", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			align_horizontal_socket.default_value = (0.0, 0.0, 0.0)
			align_horizontal_socket.min_value = -3.4028234663852886e+38
			align_horizontal_socket.max_value = 3.4028234663852886e+38
			align_horizontal_socket.subtype = 'NONE'
			align_horizontal_socket.attribute_domain = 'POINT'
			
			#Socket Input
			input_socket = _base_align.interface.new_socket(name = "Input", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			input_socket.attribute_domain = 'POINT'
			
			
			#initialize _base_align nodes
			#node Switch.008
			switch_008 = _base_align.nodes.new("GeometryNodeSwitch")
			switch_008.name = "Switch.008"
			switch_008.input_type = 'INT'
			#False
			switch_008.inputs[1].default_value = 65
			#True
			switch_008.inputs[2].default_value = 68
			
			#node Reroute.018
			reroute_018 = _base_align.nodes.new("NodeReroute")
			reroute_018.name = "Reroute.018"
			#node Switch.009
			switch_009 = _base_align.nodes.new("GeometryNodeSwitch")
			switch_009.name = "Switch.009"
			switch_009.input_type = 'INT'
			#False
			switch_009.inputs[1].default_value = 62
			#True
			switch_009.inputs[2].default_value = 64
			
			#node Reroute.020
			reroute_020 = _base_align.nodes.new("NodeReroute")
			reroute_020.name = "Reroute.020"
			#node Group.007
			group_007 = _base_align.nodes.new("GeometryNodeGroup")
			group_007.name = "Group.007"
			group_007.node_tree = mn_select_nucleic_type
			
			#node Group Input
			group_input_2 = _base_align.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
			#node Group.009
			group_009 = _base_align.nodes.new("GeometryNodeGroup")
			group_009.name = "Group.009"
			group_009.node_tree = _sampleatomvalue
			
			#node Group.010
			group_010 = _base_align.nodes.new("GeometryNodeGroup")
			group_010.name = "Group.010"
			group_010.node_tree = _sampleatomvalue
			
			#node Group.008
			group_008 = _base_align.nodes.new("GeometryNodeGroup")
			group_008.name = "Group.008"
			group_008.node_tree = _sampleatomvalue
			#Input_1
			group_008.inputs[1].default_value = 61
			
			#node Vector Math.002
			vector_math_002 = _base_align.nodes.new("ShaderNodeVectorMath")
			vector_math_002.name = "Vector Math.002"
			vector_math_002.operation = 'SUBTRACT'
			
			#node Vector Math.004
			vector_math_004 = _base_align.nodes.new("ShaderNodeVectorMath")
			vector_math_004.name = "Vector Math.004"
			vector_math_004.operation = 'SUBTRACT'
			
			#node Group Output
			group_output_2 = _base_align.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			
			
			
			#Set locations
			switch_008.location = (-30.387451171875, 0.0)
			reroute_018.location = (-150.387451171875, -200.0)
			switch_009.location = (-30.387451171875, -180.0)
			reroute_020.location = (-180.0, 80.0)
			group_007.location = (-433.26495361328125, -188.3114776611328)
			group_input_2.location = (-400.0, 120.0)
			group_009.location = (160.0, -200.0)
			group_010.location = (160.0, 40.0)
			group_008.location = (160.0, 280.0)
			vector_math_002.location = (400.0, -60.0)
			vector_math_004.location = (400.0, 100.0)
			group_output_2.location = (700.0, 140.0)
			
			#Set dimensions
			switch_008.width, switch_008.height = 145.0830078125, 100.0
			reroute_018.width, reroute_018.height = 16.0, 100.0
			switch_009.width, switch_009.height = 145.0830078125, 100.0
			reroute_020.width, reroute_020.height = 16.0, 100.0
			group_007.width, group_007.height = 221.22412109375, 100.0
			group_input_2.width, group_input_2.height = 140.0, 100.0
			group_009.width, group_009.height = 140.0, 100.0
			group_010.width, group_010.height = 140.0, 100.0
			group_008.width, group_008.height = 140.0, 100.0
			vector_math_002.width, vector_math_002.height = 140.0, 100.0
			vector_math_004.width, vector_math_004.height = 140.0, 100.0
			group_output_2.width, group_output_2.height = 140.0, 100.0
			
			#initialize _base_align links
			#switch_008.Output -> group_010.B
			_base_align.links.new(switch_008.outputs[0], group_010.inputs[1])
			#reroute_018.Output -> group_010.Geometry
			_base_align.links.new(reroute_018.outputs[0], group_010.inputs[0])
			#group_009.Value -> vector_math_002.Vector
			_base_align.links.new(group_009.outputs[1], vector_math_002.inputs[1])
			#group_007.is_pyrimidine -> switch_008.Switch
			_base_align.links.new(group_007.outputs[1], switch_008.inputs[0])
			#group_007.is_pyrimidine -> switch_009.Switch
			_base_align.links.new(group_007.outputs[1], switch_009.inputs[0])
			#reroute_018.Output -> group_009.Geometry
			_base_align.links.new(reroute_018.outputs[0], group_009.inputs[0])
			#reroute_020.Output -> reroute_018.Input
			_base_align.links.new(reroute_020.outputs[0], reroute_018.inputs[0])
			#switch_009.Output -> group_009.B
			_base_align.links.new(switch_009.outputs[0], group_009.inputs[1])
			#group_008.Value -> vector_math_004.Vector
			_base_align.links.new(group_008.outputs[1], vector_math_004.inputs[1])
			#reroute_020.Output -> group_008.Geometry
			_base_align.links.new(reroute_020.outputs[0], group_008.inputs[0])
			#group_009.Value -> vector_math_004.Vector
			_base_align.links.new(group_009.outputs[1], vector_math_004.inputs[0])
			#group_010.Value -> vector_math_002.Vector
			_base_align.links.new(group_010.outputs[1], vector_math_002.inputs[0])
			#group_input_2.Input -> reroute_020.Input
			_base_align.links.new(group_input_2.outputs[0], reroute_020.inputs[0])
			#group_009.Value -> group_output_2.Base Interface
			_base_align.links.new(group_009.outputs[1], group_output_2.inputs[0])
			#group_008.Value -> group_output_2.Base Pivot
			_base_align.links.new(group_008.outputs[1], group_output_2.inputs[1])
			#vector_math_004.Vector -> group_output_2.Align Vertical
			_base_align.links.new(vector_math_004.outputs[0], group_output_2.inputs[2])
			#vector_math_002.Vector -> group_output_2.Align Horizontal
			_base_align.links.new(vector_math_002.outputs[0], group_output_2.inputs[3])
			return _base_align

		_base_align = _base_align_node_group()

		#initialize group_pick node group
		def group_pick_node_group():
			group_pick = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Group Pick")

			group_pick.color_tag = 'INPUT'
			group_pick.description = ""

			
			#group_pick interface
			#Socket Is Valid
			is_valid_socket = group_pick.interface.new_socket(name = "Is Valid", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_valid_socket.default_value = True
			is_valid_socket.attribute_domain = 'POINT'
			is_valid_socket.description = "Whether the pick is valid. Pick is only valid if a single item is picked in the Group ID"
			
			#Socket Index
			index_socket = group_pick.interface.new_socket(name = "Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			index_socket.default_value = 0
			index_socket.min_value = 0
			index_socket.max_value = 2147483647
			index_socket.subtype = 'NONE'
			index_socket.attribute_domain = 'POINT'
			index_socket.description = "Index of picked item. Returns -1 if not a valid pick."
			
			#Socket Pick
			pick_socket = group_pick.interface.new_socket(name = "Pick", in_out='INPUT', socket_type = 'NodeSocketBool')
			pick_socket.default_value = False
			pick_socket.attribute_domain = 'POINT'
			pick_socket.hide_value = True
			pick_socket.description = "True for the item to pick from the group. If number of picks is 0 or more than 1, not a valid pick"
			
			#Socket Group ID
			group_id_socket = group_pick.interface.new_socket(name = "Group ID", in_out='INPUT', socket_type = 'NodeSocketInt')
			group_id_socket.default_value = 0
			group_id_socket.min_value = -2147483648
			group_id_socket.max_value = 2147483647
			group_id_socket.subtype = 'NONE'
			group_id_socket.attribute_domain = 'POINT'
			group_id_socket.description = "Group ID inside which to pick the item"
			
			
			#initialize group_pick nodes
			#node Group Output
			group_output_3 = group_pick.nodes.new("NodeGroupOutput")
			group_output_3.name = "Group Output"
			group_output_3.is_active_output = True
			
			#node Group Input
			group_input_3 = group_pick.nodes.new("NodeGroupInput")
			group_input_3.name = "Group Input"
			
			#node Switch
			switch = group_pick.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'INT'
			#False
			switch.inputs[1].default_value = 0
			
			#node Index
			index = group_pick.nodes.new("GeometryNodeInputIndex")
			index.name = "Index"
			
			#node Accumulate Field
			accumulate_field = group_pick.nodes.new("GeometryNodeAccumulateField")
			accumulate_field.name = "Accumulate Field"
			accumulate_field.data_type = 'INT'
			accumulate_field.domain = 'POINT'
			
			#node Accumulate Field.002
			accumulate_field_002 = group_pick.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_002.name = "Accumulate Field.002"
			accumulate_field_002.data_type = 'INT'
			accumulate_field_002.domain = 'POINT'
			
			#node Switch.001
			switch_001 = group_pick.nodes.new("GeometryNodeSwitch")
			switch_001.name = "Switch.001"
			switch_001.input_type = 'INT'
			#False
			switch_001.inputs[1].default_value = -1
			
			#node Compare.003
			compare_003_1 = group_pick.nodes.new("FunctionNodeCompare")
			compare_003_1.name = "Compare.003"
			compare_003_1.data_type = 'INT'
			compare_003_1.mode = 'ELEMENT'
			compare_003_1.operation = 'EQUAL'
			#B_INT
			compare_003_1.inputs[3].default_value = 1
			
			#node Reroute.001
			reroute_001 = group_pick.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			#node Reroute.002
			reroute_002 = group_pick.nodes.new("NodeReroute")
			reroute_002.name = "Reroute.002"
			
			
			
			#Set locations
			group_output_3.location = (462.9173889160156, 0.0)
			group_input_3.location = (-472.9173889160156, 0.0)
			switch.location = (-120.0, -20.0)
			index.location = (-480.0, -120.0)
			accumulate_field.location = (60.0, -20.0)
			accumulate_field_002.location = (-120.0, 180.0)
			switch_001.location = (240.0, -20.0)
			compare_003_1.location = (60.0, 180.0)
			reroute_001.location = (-260.0, -100.0)
			reroute_002.location = (-260.0, -60.0)
			
			#Set dimensions
			group_output_3.width, group_output_3.height = 140.0, 100.0
			group_input_3.width, group_input_3.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			index.width, index.height = 140.0, 100.0
			accumulate_field.width, accumulate_field.height = 140.0, 100.0
			accumulate_field_002.width, accumulate_field_002.height = 140.0, 100.0
			switch_001.width, switch_001.height = 140.0, 100.0
			compare_003_1.width, compare_003_1.height = 138.9921875, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			reroute_002.width, reroute_002.height = 16.0, 100.0
			
			#initialize group_pick links
			#switch.Output -> accumulate_field.Value
			group_pick.links.new(switch.outputs[0], accumulate_field.inputs[0])
			#compare_003_1.Result -> switch_001.Switch
			group_pick.links.new(compare_003_1.outputs[0], switch_001.inputs[0])
			#accumulate_field.Total -> switch_001.True
			group_pick.links.new(accumulate_field.outputs[2], switch_001.inputs[2])
			#reroute_001.Output -> accumulate_field.Group ID
			group_pick.links.new(reroute_001.outputs[0], accumulate_field.inputs[1])
			#reroute_001.Output -> accumulate_field_002.Group ID
			group_pick.links.new(reroute_001.outputs[0], accumulate_field_002.inputs[1])
			#reroute_002.Output -> switch.Switch
			group_pick.links.new(reroute_002.outputs[0], switch.inputs[0])
			#reroute_002.Output -> accumulate_field_002.Value
			group_pick.links.new(reroute_002.outputs[0], accumulate_field_002.inputs[0])
			#index.Index -> switch.True
			group_pick.links.new(index.outputs[0], switch.inputs[2])
			#accumulate_field_002.Total -> compare_003_1.A
			group_pick.links.new(accumulate_field_002.outputs[2], compare_003_1.inputs[2])
			#group_input_3.Group ID -> reroute_001.Input
			group_pick.links.new(group_input_3.outputs[1], reroute_001.inputs[0])
			#group_input_3.Pick -> reroute_002.Input
			group_pick.links.new(group_input_3.outputs[0], reroute_002.inputs[0])
			#switch_001.Output -> group_output_3.Index
			group_pick.links.new(switch_001.outputs[0], group_output_3.inputs[1])
			#compare_003_1.Result -> group_output_3.Is Valid
			group_pick.links.new(compare_003_1.outputs[0], group_output_3.inputs[0])
			return group_pick

		group_pick = group_pick_node_group()

		#initialize group_pick_vector node group
		def group_pick_vector_node_group():
			group_pick_vector = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Group Pick Vector")

			group_pick_vector.color_tag = 'INPUT'
			group_pick_vector.description = ""

			
			#group_pick_vector interface
			#Socket Is Valid
			is_valid_socket_1 = group_pick_vector.interface.new_socket(name = "Is Valid", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_valid_socket_1.default_value = False
			is_valid_socket_1.attribute_domain = 'POINT'
			is_valid_socket_1.description = "The pick for this group is valid"
			
			#Socket Index
			index_socket_1 = group_pick_vector.interface.new_socket(name = "Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			index_socket_1.default_value = 0
			index_socket_1.min_value = -2147483648
			index_socket_1.max_value = 2147483647
			index_socket_1.subtype = 'NONE'
			index_socket_1.attribute_domain = 'POINT'
			index_socket_1.description = "Picked Index for the Group"
			
			#Socket Vector
			vector_socket = group_pick_vector.interface.new_socket(name = "Vector", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			vector_socket.default_value = (0.0, 0.0, 0.0)
			vector_socket.min_value = -3.4028234663852886e+38
			vector_socket.max_value = 3.4028234663852886e+38
			vector_socket.subtype = 'NONE'
			vector_socket.attribute_domain = 'POINT'
			vector_socket.description = "Picked vector for the group"
			
			#Socket Pick
			pick_socket_1 = group_pick_vector.interface.new_socket(name = "Pick", in_out='INPUT', socket_type = 'NodeSocketBool')
			pick_socket_1.default_value = False
			pick_socket_1.attribute_domain = 'POINT'
			pick_socket_1.hide_value = True
			
			#Socket Group ID
			group_id_socket_1 = group_pick_vector.interface.new_socket(name = "Group ID", in_out='INPUT', socket_type = 'NodeSocketInt')
			group_id_socket_1.default_value = 0
			group_id_socket_1.min_value = -2147483648
			group_id_socket_1.max_value = 2147483647
			group_id_socket_1.subtype = 'NONE'
			group_id_socket_1.attribute_domain = 'POINT'
			
			#Socket Position
			position_socket = group_pick_vector.interface.new_socket(name = "Position", in_out='INPUT', socket_type = 'NodeSocketVector')
			position_socket.default_value = (0.0, 0.0, 0.0)
			position_socket.min_value = -3.4028234663852886e+38
			position_socket.max_value = 3.4028234663852886e+38
			position_socket.subtype = 'NONE'
			position_socket.attribute_domain = 'POINT'
			position_socket.description = "Vector field to pick vlaue for, defaults to Position"
			
			
			#initialize group_pick_vector nodes
			#node Group Output
			group_output_4 = group_pick_vector.nodes.new("NodeGroupOutput")
			group_output_4.name = "Group Output"
			group_output_4.is_active_output = True
			
			#node Group Input
			group_input_4 = group_pick_vector.nodes.new("NodeGroupInput")
			group_input_4.name = "Group Input"
			
			#node Evaluate at Index.001
			evaluate_at_index_001 = group_pick_vector.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001.name = "Evaluate at Index.001"
			evaluate_at_index_001.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_001.domain = 'POINT'
			
			#node Switch.002
			switch_002 = group_pick_vector.nodes.new("GeometryNodeSwitch")
			switch_002.name = "Switch.002"
			switch_002.input_type = 'VECTOR'
			#False
			switch_002.inputs[1].default_value = (0.0, 0.0, 0.0)
			
			#node Group
			group = group_pick_vector.nodes.new("GeometryNodeGroup")
			group.name = "Group"
			group.node_tree = group_pick
			
			
			
			
			#Set locations
			group_output_4.location = (-40.0, -20.0)
			group_input_4.location = (-740.0, -80.0)
			evaluate_at_index_001.location = (-380.0, -180.0)
			switch_002.location = (-220.0, -60.0)
			group.location = (-560.0, -20.0)
			
			#Set dimensions
			group_output_4.width, group_output_4.height = 140.0, 100.0
			group_input_4.width, group_input_4.height = 140.0, 100.0
			evaluate_at_index_001.width, evaluate_at_index_001.height = 132.09918212890625, 100.0
			switch_002.width, switch_002.height = 140.0, 100.0
			group.width, group.height = 140.0, 100.0
			
			#initialize group_pick_vector links
			#group.Is Valid -> switch_002.Switch
			group_pick_vector.links.new(group.outputs[0], switch_002.inputs[0])
			#group.Index -> evaluate_at_index_001.Index
			group_pick_vector.links.new(group.outputs[1], evaluate_at_index_001.inputs[0])
			#evaluate_at_index_001.Value -> switch_002.True
			group_pick_vector.links.new(evaluate_at_index_001.outputs[0], switch_002.inputs[2])
			#group.Index -> group_output_4.Index
			group_pick_vector.links.new(group.outputs[1], group_output_4.inputs[1])
			#group.Is Valid -> group_output_4.Is Valid
			group_pick_vector.links.new(group.outputs[0], group_output_4.inputs[0])
			#switch_002.Output -> group_output_4.Vector
			group_pick_vector.links.new(switch_002.outputs[0], group_output_4.inputs[2])
			#group_input_4.Group ID -> group.Group ID
			group_pick_vector.links.new(group_input_4.outputs[1], group.inputs[1])
			#group_input_4.Pick -> group.Pick
			group_pick_vector.links.new(group_input_4.outputs[0], group.inputs[0])
			#group_input_4.Position -> evaluate_at_index_001.Value
			group_pick_vector.links.new(group_input_4.outputs[2], evaluate_at_index_001.inputs[1])
			return group_pick_vector

		group_pick_vector = group_pick_vector_node_group()

		#initialize offset_integer node group
		def offset_integer_node_group():
			offset_integer = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Offset Integer")

			offset_integer.color_tag = 'CONVERTER'
			offset_integer.description = ""

			
			#offset_integer interface
			#Socket Value
			value_socket_2 = offset_integer.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			value_socket_2.default_value = 0
			value_socket_2.min_value = -2147483648
			value_socket_2.max_value = 2147483647
			value_socket_2.subtype = 'NONE'
			value_socket_2.attribute_domain = 'POINT'
			
			#Socket Index
			index_socket_2 = offset_integer.interface.new_socket(name = "Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			index_socket_2.default_value = 0
			index_socket_2.min_value = 0
			index_socket_2.max_value = 2147483647
			index_socket_2.subtype = 'NONE'
			index_socket_2.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_3 = offset_integer.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketInt')
			value_socket_3.default_value = 0
			value_socket_3.min_value = -2147483648
			value_socket_3.max_value = 2147483647
			value_socket_3.subtype = 'NONE'
			value_socket_3.attribute_domain = 'POINT'
			value_socket_3.hide_value = True
			
			#Socket Offset
			offset_socket = offset_integer.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket.default_value = 0
			offset_socket.min_value = -2147483648
			offset_socket.max_value = 2147483647
			offset_socket.subtype = 'NONE'
			offset_socket.attribute_domain = 'POINT'
			
			
			#initialize offset_integer nodes
			#node Group Output
			group_output_5 = offset_integer.nodes.new("NodeGroupOutput")
			group_output_5.name = "Group Output"
			group_output_5.is_active_output = True
			
			#node Group Input
			group_input_5 = offset_integer.nodes.new("NodeGroupInput")
			group_input_5.name = "Group Input"
			
			#node Evaluate at Index
			evaluate_at_index = offset_integer.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index.name = "Evaluate at Index"
			evaluate_at_index.data_type = 'INT'
			evaluate_at_index.domain = 'POINT'
			
			#node Math
			math = offset_integer.nodes.new("ShaderNodeMath")
			math.name = "Math"
			math.operation = 'ADD'
			math.use_clamp = False
			
			
			
			
			#Set locations
			group_output_5.location = (190.0, 0.0)
			group_input_5.location = (-412.72760009765625, 0.2001800537109375)
			evaluate_at_index.location = (0.0, 0.0)
			math.location = (-217.90158081054688, 69.93922424316406)
			
			#Set dimensions
			group_output_5.width, group_output_5.height = 140.0, 100.0
			group_input_5.width, group_input_5.height = 140.0, 100.0
			evaluate_at_index.width, evaluate_at_index.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			
			#initialize offset_integer links
			#evaluate_at_index.Value -> group_output_5.Value
			offset_integer.links.new(evaluate_at_index.outputs[0], group_output_5.inputs[0])
			#group_input_5.Index -> math.Value
			offset_integer.links.new(group_input_5.outputs[0], math.inputs[0])
			#group_input_5.Offset -> math.Value
			offset_integer.links.new(group_input_5.outputs[2], math.inputs[1])
			#math.Value -> evaluate_at_index.Index
			offset_integer.links.new(math.outputs[0], evaluate_at_index.inputs[0])
			#group_input_5.Value -> evaluate_at_index.Value
			offset_integer.links.new(group_input_5.outputs[1], evaluate_at_index.inputs[1])
			return offset_integer

		offset_integer = offset_integer_node_group()

		#initialize res_group_id node group
		def res_group_id_node_group():
			res_group_id = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Res Group ID")

			res_group_id.color_tag = 'INPUT'
			res_group_id.description = ""

			
			#res_group_id interface
			#Socket Unique Group ID
			unique_group_id_socket = res_group_id.interface.new_socket(name = "Unique Group ID", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			unique_group_id_socket.default_value = 0
			unique_group_id_socket.min_value = -2147483648
			unique_group_id_socket.max_value = 2147483647
			unique_group_id_socket.subtype = 'NONE'
			unique_group_id_socket.attribute_domain = 'POINT'
			unique_group_id_socket.description = "A unique Group ID for eash residue"
			
			
			#initialize res_group_id nodes
			#node Group Output
			group_output_6 = res_group_id.nodes.new("NodeGroupOutput")
			group_output_6.name = "Group Output"
			group_output_6.is_active_output = True
			
			#node Group Input
			group_input_6 = res_group_id.nodes.new("NodeGroupInput")
			group_input_6.name = "Group Input"
			
			#node Named Attribute.001
			named_attribute_001 = res_group_id.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.data_type = 'INT'
			#Name
			named_attribute_001.inputs[0].default_value = "res_id"
			
			#node Named Attribute.002
			named_attribute_002 = res_group_id.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002.name = "Named Attribute.002"
			named_attribute_002.data_type = 'INT'
			#Name
			named_attribute_002.inputs[0].default_value = "atom_name"
			
			#node Compare.002
			compare_002 = res_group_id.nodes.new("FunctionNodeCompare")
			compare_002.name = "Compare.002"
			compare_002.data_type = 'INT'
			compare_002.mode = 'ELEMENT'
			compare_002.operation = 'EQUAL'
			#B_INT
			compare_002.inputs[3].default_value = 1
			
			#node Compare.001
			compare_001 = res_group_id.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'INT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'NOT_EQUAL'
			
			#node Boolean Math
			boolean_math = res_group_id.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'OR'
			
			#node Accumulate Field.001
			accumulate_field_001 = res_group_id.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_001.name = "Accumulate Field.001"
			accumulate_field_001.data_type = 'INT'
			accumulate_field_001.domain = 'POINT'
			#Group Index
			accumulate_field_001.inputs[1].default_value = 0
			
			#node Group.001
			group_001 = res_group_id.nodes.new("GeometryNodeGroup")
			group_001.name = "Group.001"
			group_001.node_tree = offset_integer
			#Socket_1
			group_001.inputs[0].default_value = 0
			#Socket_2
			group_001.inputs[2].default_value = -1
			
			#node Math
			math_1 = res_group_id.nodes.new("ShaderNodeMath")
			math_1.name = "Math"
			math_1.operation = 'SUBTRACT'
			math_1.use_clamp = False
			#Value_001
			math_1.inputs[1].default_value = 1.0
			
			#node Frame
			frame = res_group_id.nodes.new("NodeFrame")
			frame.name = "Frame"
			frame.label_size = 20
			frame.shrink = True
			
			#node Reroute
			reroute = res_group_id.nodes.new("NodeReroute")
			reroute.label = "subtracting 1 from the leading, but things don't work right"
			reroute.name = "Reroute"
			#node Reroute.001
			reroute_001_1 = res_group_id.nodes.new("NodeReroute")
			reroute_001_1.name = "Reroute.001"
			#node Reroute.002
			reroute_002_1 = res_group_id.nodes.new("NodeReroute")
			reroute_002_1.label = "In theory we can just use the trailing value instead of"
			reroute_002_1.name = "Reroute.002"
			#node Reroute.003
			reroute_003 = res_group_id.nodes.new("NodeReroute")
			reroute_003.name = "Reroute.003"
			
			
			#Set parents
			math_1.parent = frame
			reroute.parent = frame
			reroute_001_1.parent = frame
			reroute_002_1.parent = frame
			reroute_003.parent = frame
			
			#Set locations
			group_output_6.location = (900.0, 160.0)
			group_input_6.location = (-420.0, 160.0)
			named_attribute_001.location = (-240.0, 0.0)
			named_attribute_002.location = (-250.0, 160.0)
			compare_002.location = (-70.0, 160.0)
			compare_001.location = (-70.0, 0.0)
			boolean_math.location = (90.0, 160.0)
			accumulate_field_001.location = (250.0, 160.0)
			group_001.location = (-70.0, -160.0)
			math_1.location = (519.2361450195312, 166.28671264648438)
			frame.location = (95.0, -20.0)
			reroute.location = (554.4125366210938, 257.9646911621094)
			reroute_001_1.location = (739.2361450195312, 306.2867126464844)
			reroute_002_1.location = (551.13134765625, 297.3444519042969)
			reroute_003.location = (379.23614501953125, 306.2867126464844)
			
			#Set dimensions
			group_output_6.width, group_output_6.height = 140.0, 100.0
			group_input_6.width, group_input_6.height = 140.0, 100.0
			named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
			named_attribute_002.width, named_attribute_002.height = 140.0, 100.0
			compare_002.width, compare_002.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			accumulate_field_001.width, accumulate_field_001.height = 140.0, 100.0
			group_001.width, group_001.height = 140.0, 100.0
			math_1.width, math_1.height = 140.0, 100.0
			frame.width, frame.height = 436.0, 356.2867126464844
			reroute.width, reroute.height = 16.0, 100.0
			reroute_001_1.width, reroute_001_1.height = 16.0, 100.0
			reroute_002_1.width, reroute_002_1.height = 16.0, 100.0
			reroute_003.width, reroute_003.height = 16.0, 100.0
			
			#initialize res_group_id links
			#compare_002.Result -> boolean_math.Boolean
			res_group_id.links.new(compare_002.outputs[0], boolean_math.inputs[0])
			#named_attribute_001.Attribute -> compare_001.A
			res_group_id.links.new(named_attribute_001.outputs[0], compare_001.inputs[2])
			#named_attribute_001.Attribute -> group_001.Value
			res_group_id.links.new(named_attribute_001.outputs[0], group_001.inputs[1])
			#compare_001.Result -> boolean_math.Boolean
			res_group_id.links.new(compare_001.outputs[0], boolean_math.inputs[1])
			#named_attribute_002.Attribute -> compare_002.A
			res_group_id.links.new(named_attribute_002.outputs[0], compare_002.inputs[2])
			#group_001.Value -> compare_001.B
			res_group_id.links.new(group_001.outputs[0], compare_001.inputs[3])
			#accumulate_field_001.Leading -> math_1.Value
			res_group_id.links.new(accumulate_field_001.outputs[0], math_1.inputs[0])
			#math_1.Value -> group_output_6.Unique Group ID
			res_group_id.links.new(math_1.outputs[0], group_output_6.inputs[0])
			#boolean_math.Boolean -> accumulate_field_001.Value
			res_group_id.links.new(boolean_math.outputs[0], accumulate_field_001.inputs[0])
			return res_group_id

		res_group_id = res_group_id_node_group()

		#initialize residue_mask node group
		def residue_mask_node_group():
			residue_mask = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Residue Mask")

			residue_mask.color_tag = 'INPUT'
			residue_mask.description = ""

			
			#residue_mask interface
			#Socket Is Valid
			is_valid_socket_2 = residue_mask.interface.new_socket(name = "Is Valid", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_valid_socket_2.default_value = False
			is_valid_socket_2.attribute_domain = 'POINT'
			is_valid_socket_2.description = "Group contains only one occurrance of the selected atom. None or more than one returns False"
			
			#Socket Index
			index_socket_3 = residue_mask.interface.new_socket(name = "Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			index_socket_3.default_value = 0
			index_socket_3.min_value = -2147483648
			index_socket_3.max_value = 2147483647
			index_socket_3.subtype = 'NONE'
			index_socket_3.attribute_domain = 'POINT'
			index_socket_3.description = "Index for the group's atom with specified name, returns -1 if not valid"
			
			#Socket Position
			position_socket_1 = residue_mask.interface.new_socket(name = "Position", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			position_socket_1.default_value = (0.0, 0.0, 0.0)
			position_socket_1.min_value = -3.4028234663852886e+38
			position_socket_1.max_value = 3.4028234663852886e+38
			position_socket_1.subtype = 'NONE'
			position_socket_1.attribute_domain = 'POINT'
			position_socket_1.description = "Position of the picked point in the group, returns (0, 0, 0) if not valid"
			
			#Socket Group ID
			group_id_socket_2 = residue_mask.interface.new_socket(name = "Group ID", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			group_id_socket_2.default_value = 0
			group_id_socket_2.min_value = -2147483648
			group_id_socket_2.max_value = 2147483647
			group_id_socket_2.subtype = 'NONE'
			group_id_socket_2.attribute_domain = 'POINT'
			
			#Socket atom_name
			atom_name_socket = residue_mask.interface.new_socket(name = "atom_name", in_out='INPUT', socket_type = 'NodeSocketInt')
			atom_name_socket.default_value = 1
			atom_name_socket.min_value = 2
			atom_name_socket.max_value = 2147483647
			atom_name_socket.subtype = 'NONE'
			atom_name_socket.attribute_domain = 'POINT'
			atom_name_socket.description = "Atom to pick from the group"
			
			#Socket Use Fallback
			use_fallback_socket = residue_mask.interface.new_socket(name = "Use Fallback", in_out='INPUT', socket_type = 'NodeSocketBool')
			use_fallback_socket.default_value = True
			use_fallback_socket.attribute_domain = 'POINT'
			use_fallback_socket.description = "Uses a calculated Unique Group ID as a fallback. Disabling can increase performance if pre-computing a Group ID for multiple nodes"
			
			#Socket Group ID
			group_id_socket_3 = residue_mask.interface.new_socket(name = "Group ID", in_out='INPUT', socket_type = 'NodeSocketInt')
			group_id_socket_3.default_value = 0
			group_id_socket_3.min_value = -2147483648
			group_id_socket_3.max_value = 2147483647
			group_id_socket_3.subtype = 'NONE'
			group_id_socket_3.attribute_domain = 'POINT'
			
			
			#initialize residue_mask nodes
			#node Compare
			compare = residue_mask.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'EQUAL'
			
			#node Group Input
			group_input_7 = residue_mask.nodes.new("NodeGroupInput")
			group_input_7.name = "Group Input"
			
			#node Named Attribute
			named_attribute_1 = residue_mask.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_1.name = "Named Attribute"
			named_attribute_1.data_type = 'INT'
			#Name
			named_attribute_1.inputs[0].default_value = "atom_name"
			
			#node Group Output
			group_output_7 = residue_mask.nodes.new("NodeGroupOutput")
			group_output_7.name = "Group Output"
			group_output_7.is_active_output = True
			
			#node Group
			group_1 = residue_mask.nodes.new("GeometryNodeGroup")
			group_1.name = "Group"
			group_1.node_tree = group_pick_vector
			#Socket_5
			group_1.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Group.002
			group_002 = residue_mask.nodes.new("GeometryNodeGroup")
			group_002.name = "Group.002"
			group_002.node_tree = res_group_id
			
			#node Switch
			switch_1 = residue_mask.nodes.new("GeometryNodeSwitch")
			switch_1.name = "Switch"
			switch_1.input_type = 'INT'
			
			
			
			
			#Set locations
			compare.location = (40.0, 340.0)
			group_input_7.location = (-140.0, 200.0)
			named_attribute_1.location = (-140.0, 340.0)
			group_output_7.location = (420.0, 340.0)
			group_1.location = (220.0, 340.0)
			group_002.location = (-140.0, 60.0)
			switch_1.location = (40.0, 180.0)
			
			#Set dimensions
			compare.width, compare.height = 140.0, 100.0
			group_input_7.width, group_input_7.height = 140.0, 100.0
			named_attribute_1.width, named_attribute_1.height = 140.0, 100.0
			group_output_7.width, group_output_7.height = 140.0, 100.0
			group_1.width, group_1.height = 164.60528564453125, 100.0
			group_002.width, group_002.height = 140.0, 100.0
			switch_1.width, switch_1.height = 140.0, 100.0
			
			#initialize residue_mask links
			#named_attribute_1.Attribute -> compare.A
			residue_mask.links.new(named_attribute_1.outputs[0], compare.inputs[2])
			#group_input_7.atom_name -> compare.B
			residue_mask.links.new(group_input_7.outputs[0], compare.inputs[3])
			#group_1.Index -> group_output_7.Index
			residue_mask.links.new(group_1.outputs[1], group_output_7.inputs[1])
			#group_1.Vector -> group_output_7.Position
			residue_mask.links.new(group_1.outputs[2], group_output_7.inputs[2])
			#group_1.Is Valid -> group_output_7.Is Valid
			residue_mask.links.new(group_1.outputs[0], group_output_7.inputs[0])
			#compare.Result -> group_1.Pick
			residue_mask.links.new(compare.outputs[0], group_1.inputs[0])
			#group_input_7.Use Fallback -> switch_1.Switch
			residue_mask.links.new(group_input_7.outputs[1], switch_1.inputs[0])
			#group_input_7.Group ID -> switch_1.False
			residue_mask.links.new(group_input_7.outputs[2], switch_1.inputs[1])
			#switch_1.Output -> group_1.Group ID
			residue_mask.links.new(switch_1.outputs[0], group_1.inputs[1])
			#group_002.Unique Group ID -> switch_1.True
			residue_mask.links.new(group_002.outputs[0], switch_1.inputs[2])
			#switch_1.Output -> group_output_7.Group ID
			residue_mask.links.new(switch_1.outputs[0], group_output_7.inputs[3])
			return residue_mask

		residue_mask = residue_mask_node_group()

		#initialize _mn_constants_atom_name_nucleic node group
		def _mn_constants_atom_name_nucleic_node_group():
			_mn_constants_atom_name_nucleic = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_constants_atom_name_nucleic")

			_mn_constants_atom_name_nucleic.color_tag = 'NONE'
			_mn_constants_atom_name_nucleic.description = ""

			
			#_mn_constants_atom_name_nucleic interface
			#Socket Backbone Lower
			backbone_lower_socket = _mn_constants_atom_name_nucleic.interface.new_socket(name = "Backbone Lower", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			backbone_lower_socket.default_value = 0
			backbone_lower_socket.min_value = -2147483648
			backbone_lower_socket.max_value = 2147483647
			backbone_lower_socket.subtype = 'NONE'
			backbone_lower_socket.attribute_domain = 'POINT'
			
			#Socket Backbone Upper
			backbone_upper_socket = _mn_constants_atom_name_nucleic.interface.new_socket(name = "Backbone Upper", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			backbone_upper_socket.default_value = 0
			backbone_upper_socket.min_value = -2147483648
			backbone_upper_socket.max_value = 2147483647
			backbone_upper_socket.subtype = 'NONE'
			backbone_upper_socket.attribute_domain = 'POINT'
			
			#Socket Side Chain Lower
			side_chain_lower_socket = _mn_constants_atom_name_nucleic.interface.new_socket(name = "Side Chain Lower", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			side_chain_lower_socket.default_value = 0
			side_chain_lower_socket.min_value = -2147483648
			side_chain_lower_socket.max_value = 2147483647
			side_chain_lower_socket.subtype = 'NONE'
			side_chain_lower_socket.attribute_domain = 'POINT'
			
			#Socket Side Chain Upper
			side_chain_upper_socket = _mn_constants_atom_name_nucleic.interface.new_socket(name = "Side Chain Upper", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			side_chain_upper_socket.default_value = 0
			side_chain_upper_socket.min_value = -2147483648
			side_chain_upper_socket.max_value = 2147483647
			side_chain_upper_socket.subtype = 'NONE'
			side_chain_upper_socket.attribute_domain = 'POINT'
			
			#Socket Side Chain Joint Carbon
			side_chain_joint_carbon_socket = _mn_constants_atom_name_nucleic.interface.new_socket(name = "Side Chain Joint Carbon", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			side_chain_joint_carbon_socket.default_value = 0
			side_chain_joint_carbon_socket.min_value = -2147483648
			side_chain_joint_carbon_socket.max_value = 2147483647
			side_chain_joint_carbon_socket.subtype = 'NONE'
			side_chain_joint_carbon_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_constants_atom_name_nucleic nodes
			#node Group Output
			group_output_8 = _mn_constants_atom_name_nucleic.nodes.new("NodeGroupOutput")
			group_output_8.name = "Group Output"
			group_output_8.is_active_output = True
			
			#node Group Input
			group_input_8 = _mn_constants_atom_name_nucleic.nodes.new("NodeGroupInput")
			group_input_8.name = "Group Input"
			
			#node Integer
			integer = _mn_constants_atom_name_nucleic.nodes.new("FunctionNodeInputInt")
			integer.name = "Integer"
			integer.integer = 61
			
			#node Integer.002
			integer_002 = _mn_constants_atom_name_nucleic.nodes.new("FunctionNodeInputInt")
			integer_002.name = "Integer.002"
			integer_002.integer = 50
			
			#node Integer.003
			integer_003 = _mn_constants_atom_name_nucleic.nodes.new("FunctionNodeInputInt")
			integer_003.name = "Integer.003"
			integer_003.integer = 61
			
			#node Integer.001
			integer_001 = _mn_constants_atom_name_nucleic.nodes.new("FunctionNodeInputInt")
			integer_001.name = "Integer.001"
			integer_001.integer = 77
			
			#node Integer.004
			integer_004 = _mn_constants_atom_name_nucleic.nodes.new("FunctionNodeInputInt")
			integer_004.name = "Integer.004"
			integer_004.integer = 54
			
			
			
			
			#Set locations
			group_output_8.location = (190.0, 0.0)
			group_input_8.location = (-200.0, 0.0)
			integer.location = (0.0, -100.0)
			integer_002.location = (0.0, 100.0)
			integer_003.location = (0.0, 0.0)
			integer_001.location = (0.0, -200.0)
			integer_004.location = (0.0, -300.0)
			
			#Set dimensions
			group_output_8.width, group_output_8.height = 140.0, 100.0
			group_input_8.width, group_input_8.height = 140.0, 100.0
			integer.width, integer.height = 140.0, 100.0
			integer_002.width, integer_002.height = 140.0, 100.0
			integer_003.width, integer_003.height = 140.0, 100.0
			integer_001.width, integer_001.height = 140.0, 100.0
			integer_004.width, integer_004.height = 140.0, 100.0
			
			#initialize _mn_constants_atom_name_nucleic links
			#integer.Integer -> group_output_8.Side Chain Lower
			_mn_constants_atom_name_nucleic.links.new(integer.outputs[0], group_output_8.inputs[2])
			#integer_001.Integer -> group_output_8.Side Chain Upper
			_mn_constants_atom_name_nucleic.links.new(integer_001.outputs[0], group_output_8.inputs[3])
			#integer_002.Integer -> group_output_8.Backbone Lower
			_mn_constants_atom_name_nucleic.links.new(integer_002.outputs[0], group_output_8.inputs[0])
			#integer_003.Integer -> group_output_8.Backbone Upper
			_mn_constants_atom_name_nucleic.links.new(integer_003.outputs[0], group_output_8.inputs[1])
			#integer_004.Integer -> group_output_8.Side Chain Joint Carbon
			_mn_constants_atom_name_nucleic.links.new(integer_004.outputs[0], group_output_8.inputs[4])
			return _mn_constants_atom_name_nucleic

		_mn_constants_atom_name_nucleic = _mn_constants_atom_name_nucleic_node_group()

		#initialize _mn_select_nucleic node group
		def _mn_select_nucleic_node_group():
			_mn_select_nucleic = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_select_nucleic")

			_mn_select_nucleic.color_tag = 'NONE'
			_mn_select_nucleic.description = ""

			
			#_mn_select_nucleic interface
			#Socket Is Backbone
			is_backbone_socket = _mn_select_nucleic.interface.new_socket(name = "Is Backbone", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_backbone_socket.default_value = False
			is_backbone_socket.attribute_domain = 'POINT'
			is_backbone_socket.description = "True for atoms that are part of the sugar-phosphate backbone for the nucleotides"
			
			#Socket Is Side Chain
			is_side_chain_socket = _mn_select_nucleic.interface.new_socket(name = "Is Side Chain", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_side_chain_socket.default_value = False
			is_side_chain_socket.attribute_domain = 'POINT'
			is_side_chain_socket.description = "True for atoms that are part of the bases for nucleotides."
			
			#Socket Is Nucleic
			is_nucleic_socket = _mn_select_nucleic.interface.new_socket(name = "Is Nucleic", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_nucleic_socket.default_value = False
			is_nucleic_socket.attribute_domain = 'POINT'
			is_nucleic_socket.description = "True if the atoms are part of a nucleic acid"
			
			
			#initialize _mn_select_nucleic nodes
			#node Group Input
			group_input_9 = _mn_select_nucleic.nodes.new("NodeGroupInput")
			group_input_9.name = "Group Input"
			
			#node Compare
			compare_1 = _mn_select_nucleic.nodes.new("FunctionNodeCompare")
			compare_1.name = "Compare"
			compare_1.data_type = 'INT'
			compare_1.mode = 'ELEMENT'
			compare_1.operation = 'GREATER_EQUAL'
			
			#node Compare.001
			compare_001_1 = _mn_select_nucleic.nodes.new("FunctionNodeCompare")
			compare_001_1.name = "Compare.001"
			compare_001_1.data_type = 'INT'
			compare_001_1.mode = 'ELEMENT'
			compare_001_1.operation = 'LESS_EQUAL'
			
			#node Boolean Math.001
			boolean_math_001 = _mn_select_nucleic.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001.name = "Boolean Math.001"
			boolean_math_001.operation = 'AND'
			
			#node Group Output
			group_output_9 = _mn_select_nucleic.nodes.new("NodeGroupOutput")
			group_output_9.name = "Group Output"
			group_output_9.is_active_output = True
			
			#node Compare.002
			compare_002_1 = _mn_select_nucleic.nodes.new("FunctionNodeCompare")
			compare_002_1.name = "Compare.002"
			compare_002_1.data_type = 'INT'
			compare_002_1.mode = 'ELEMENT'
			compare_002_1.operation = 'GREATER_EQUAL'
			
			#node Compare.003
			compare_003_2 = _mn_select_nucleic.nodes.new("FunctionNodeCompare")
			compare_003_2.name = "Compare.003"
			compare_003_2.data_type = 'INT'
			compare_003_2.mode = 'ELEMENT'
			compare_003_2.operation = 'LESS_EQUAL'
			
			#node Boolean Math.002
			boolean_math_002 = _mn_select_nucleic.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002.name = "Boolean Math.002"
			boolean_math_002.operation = 'AND'
			
			#node Compare.004
			compare_004 = _mn_select_nucleic.nodes.new("FunctionNodeCompare")
			compare_004.name = "Compare.004"
			compare_004.data_type = 'INT'
			compare_004.mode = 'ELEMENT'
			compare_004.operation = 'GREATER_EQUAL'
			
			#node Compare.005
			compare_005 = _mn_select_nucleic.nodes.new("FunctionNodeCompare")
			compare_005.name = "Compare.005"
			compare_005.data_type = 'INT'
			compare_005.mode = 'ELEMENT'
			compare_005.operation = 'LESS_EQUAL'
			
			#node Boolean Math.003
			boolean_math_003 = _mn_select_nucleic.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003.name = "Boolean Math.003"
			boolean_math_003.operation = 'AND'
			
			#node Named Attribute
			named_attribute_2 = _mn_select_nucleic.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_2.name = "Named Attribute"
			named_attribute_2.data_type = 'INT'
			#Name
			named_attribute_2.inputs[0].default_value = "atom_name"
			
			#node Group
			group_2 = _mn_select_nucleic.nodes.new("GeometryNodeGroup")
			group_2.name = "Group"
			group_2.node_tree = _mn_constants_atom_name_nucleic
			
			
			
			
			#Set locations
			group_input_9.location = (-460.0, 0.0)
			compare_1.location = (80.0, 80.0)
			compare_001_1.location = (80.0, -80.0)
			boolean_math_001.location = (260.0, 80.0)
			group_output_9.location = (580.0, 60.0)
			compare_002_1.location = (80.0, -260.0)
			compare_003_2.location = (80.0, -420.0)
			boolean_math_002.location = (260.0, -260.0)
			compare_004.location = (80.0, -580.0)
			compare_005.location = (80.0, -740.0)
			boolean_math_003.location = (260.0, -580.0)
			named_attribute_2.location = (-260.0, -280.0)
			group_2.location = (-480.0, -100.0)
			
			#Set dimensions
			group_input_9.width, group_input_9.height = 140.0, 100.0
			compare_1.width, compare_1.height = 140.0, 100.0
			compare_001_1.width, compare_001_1.height = 140.0, 100.0
			boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
			group_output_9.width, group_output_9.height = 140.0, 100.0
			compare_002_1.width, compare_002_1.height = 140.0, 100.0
			compare_003_2.width, compare_003_2.height = 140.0, 100.0
			boolean_math_002.width, boolean_math_002.height = 140.0, 100.0
			compare_004.width, compare_004.height = 140.0, 100.0
			compare_005.width, compare_005.height = 140.0, 100.0
			boolean_math_003.width, boolean_math_003.height = 140.0, 100.0
			named_attribute_2.width, named_attribute_2.height = 140.0, 100.0
			group_2.width, group_2.height = 365.8858337402344, 100.0
			
			#initialize _mn_select_nucleic links
			#compare_001_1.Result -> boolean_math_001.Boolean
			_mn_select_nucleic.links.new(compare_001_1.outputs[0], boolean_math_001.inputs[1])
			#named_attribute_2.Attribute -> compare_1.A
			_mn_select_nucleic.links.new(named_attribute_2.outputs[0], compare_1.inputs[2])
			#compare_1.Result -> boolean_math_001.Boolean
			_mn_select_nucleic.links.new(compare_1.outputs[0], boolean_math_001.inputs[0])
			#named_attribute_2.Attribute -> compare_001_1.A
			_mn_select_nucleic.links.new(named_attribute_2.outputs[0], compare_001_1.inputs[2])
			#boolean_math_001.Boolean -> group_output_9.Is Backbone
			_mn_select_nucleic.links.new(boolean_math_001.outputs[0], group_output_9.inputs[0])
			#group_2.Backbone Lower -> compare_1.B
			_mn_select_nucleic.links.new(group_2.outputs[0], compare_1.inputs[3])
			#group_2.Backbone Upper -> compare_001_1.B
			_mn_select_nucleic.links.new(group_2.outputs[1], compare_001_1.inputs[3])
			#compare_003_2.Result -> boolean_math_002.Boolean
			_mn_select_nucleic.links.new(compare_003_2.outputs[0], boolean_math_002.inputs[1])
			#compare_002_1.Result -> boolean_math_002.Boolean
			_mn_select_nucleic.links.new(compare_002_1.outputs[0], boolean_math_002.inputs[0])
			#group_2.Side Chain Lower -> compare_002_1.B
			_mn_select_nucleic.links.new(group_2.outputs[2], compare_002_1.inputs[3])
			#group_2.Side Chain Upper -> compare_003_2.B
			_mn_select_nucleic.links.new(group_2.outputs[3], compare_003_2.inputs[3])
			#boolean_math_002.Boolean -> group_output_9.Is Side Chain
			_mn_select_nucleic.links.new(boolean_math_002.outputs[0], group_output_9.inputs[1])
			#named_attribute_2.Attribute -> compare_002_1.A
			_mn_select_nucleic.links.new(named_attribute_2.outputs[0], compare_002_1.inputs[2])
			#named_attribute_2.Attribute -> compare_003_2.A
			_mn_select_nucleic.links.new(named_attribute_2.outputs[0], compare_003_2.inputs[2])
			#compare_005.Result -> boolean_math_003.Boolean
			_mn_select_nucleic.links.new(compare_005.outputs[0], boolean_math_003.inputs[1])
			#compare_004.Result -> boolean_math_003.Boolean
			_mn_select_nucleic.links.new(compare_004.outputs[0], boolean_math_003.inputs[0])
			#group_2.Backbone Lower -> compare_004.B
			_mn_select_nucleic.links.new(group_2.outputs[0], compare_004.inputs[3])
			#named_attribute_2.Attribute -> compare_004.A
			_mn_select_nucleic.links.new(named_attribute_2.outputs[0], compare_004.inputs[2])
			#group_2.Side Chain Upper -> compare_005.B
			_mn_select_nucleic.links.new(group_2.outputs[3], compare_005.inputs[3])
			#named_attribute_2.Attribute -> compare_005.A
			_mn_select_nucleic.links.new(named_attribute_2.outputs[0], compare_005.inputs[2])
			#boolean_math_003.Boolean -> group_output_9.Is Nucleic
			_mn_select_nucleic.links.new(boolean_math_003.outputs[0], group_output_9.inputs[2])
			return _mn_select_nucleic

		_mn_select_nucleic = _mn_select_nucleic_node_group()

		#initialize fallback_boolean node group
		def fallback_boolean_node_group():
			fallback_boolean = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Fallback Boolean")

			fallback_boolean.color_tag = 'INPUT'
			fallback_boolean.description = "Computes the boolean field if the given attribute doesn't exist. If it doesn't exist it just uses the attribute instead"

			
			#fallback_boolean interface
			#Socket Boolean
			boolean_socket = fallback_boolean.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket.default_value = False
			boolean_socket.attribute_domain = 'POINT'
			
			#Socket Name
			name_socket = fallback_boolean.interface.new_socket(name = "Name", in_out='INPUT', socket_type = 'NodeSocketString')
			name_socket.default_value = ""
			name_socket.attribute_domain = 'POINT'
			
			#Socket Fallback
			fallback_socket = fallback_boolean.interface.new_socket(name = "Fallback", in_out='INPUT', socket_type = 'NodeSocketBool')
			fallback_socket.default_value = False
			fallback_socket.attribute_domain = 'POINT'
			
			
			#initialize fallback_boolean nodes
			#node Group Output
			group_output_10 = fallback_boolean.nodes.new("NodeGroupOutput")
			group_output_10.name = "Group Output"
			group_output_10.is_active_output = True
			
			#node Group Input
			group_input_10 = fallback_boolean.nodes.new("NodeGroupInput")
			group_input_10.name = "Group Input"
			
			#node Named Attribute
			named_attribute_3 = fallback_boolean.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_3.name = "Named Attribute"
			named_attribute_3.data_type = 'BOOLEAN'
			
			#node Switch
			switch_2 = fallback_boolean.nodes.new("GeometryNodeSwitch")
			switch_2.name = "Switch"
			switch_2.input_type = 'BOOLEAN'
			
			
			
			
			#Set locations
			group_output_10.location = (276.6171569824219, 4.738137245178223)
			group_input_10.location = (-280.0, 0.0)
			named_attribute_3.location = (-94.73597717285156, 4.738137245178223)
			switch_2.location = (86.61715698242188, 4.738137245178223)
			
			#Set dimensions
			group_output_10.width, group_output_10.height = 140.0, 100.0
			group_input_10.width, group_input_10.height = 140.0, 100.0
			named_attribute_3.width, named_attribute_3.height = 140.0, 100.0
			switch_2.width, switch_2.height = 140.0, 100.0
			
			#initialize fallback_boolean links
			#named_attribute_3.Exists -> switch_2.Switch
			fallback_boolean.links.new(named_attribute_3.outputs[1], switch_2.inputs[0])
			#named_attribute_3.Attribute -> switch_2.True
			fallback_boolean.links.new(named_attribute_3.outputs[0], switch_2.inputs[2])
			#group_input_10.Fallback -> switch_2.False
			fallback_boolean.links.new(group_input_10.outputs[1], switch_2.inputs[1])
			#switch_2.Output -> group_output_10.Boolean
			fallback_boolean.links.new(switch_2.outputs[0], group_output_10.inputs[0])
			#group_input_10.Name -> named_attribute_3.Name
			fallback_boolean.links.new(group_input_10.outputs[0], named_attribute_3.inputs[0])
			return fallback_boolean

		fallback_boolean = fallback_boolean_node_group()

		#initialize is_nucleic node group
		def is_nucleic_node_group():
			is_nucleic = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Is Nucleic")

			is_nucleic.color_tag = 'INPUT'
			is_nucleic.description = ""

			
			#is_nucleic interface
			#Socket Selection
			selection_socket = is_nucleic.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket.default_value = False
			selection_socket.attribute_domain = 'POINT'
			selection_socket.description = "True if atoms are part of a nucleic acid"
			
			#Socket Inverted
			inverted_socket = is_nucleic.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket.default_value = False
			inverted_socket.attribute_domain = 'POINT'
			
			#Socket And
			and_socket = is_nucleic.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket.default_value = True
			and_socket.attribute_domain = 'POINT'
			and_socket.hide_value = True
			
			#Socket Or
			or_socket = is_nucleic.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket.default_value = False
			or_socket.attribute_domain = 'POINT'
			or_socket.hide_value = True
			
			
			#initialize is_nucleic nodes
			#node Group Input
			group_input_11 = is_nucleic.nodes.new("NodeGroupInput")
			group_input_11.name = "Group Input"
			
			#node Boolean Math.001
			boolean_math_001_1 = is_nucleic.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_1.name = "Boolean Math.001"
			boolean_math_001_1.operation = 'AND'
			
			#node Group Output
			group_output_11 = is_nucleic.nodes.new("NodeGroupOutput")
			group_output_11.name = "Group Output"
			group_output_11.is_active_output = True
			
			#node Group
			group_3 = is_nucleic.nodes.new("GeometryNodeGroup")
			group_3.name = "Group"
			group_3.node_tree = _mn_select_nucleic
			
			#node Group.001
			group_001_1 = is_nucleic.nodes.new("GeometryNodeGroup")
			group_001_1.name = "Group.001"
			group_001_1.node_tree = fallback_boolean
			#Socket_2
			group_001_1.inputs[0].default_value = "is_nucleic"
			
			#node Boolean Math.002
			boolean_math_002_1 = is_nucleic.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_1.name = "Boolean Math.002"
			boolean_math_002_1.operation = 'OR'
			
			#node Boolean Math
			boolean_math_1 = is_nucleic.nodes.new("FunctionNodeBooleanMath")
			boolean_math_1.name = "Boolean Math"
			boolean_math_1.operation = 'NOT'
			
			
			
			
			#Set locations
			group_input_11.location = (-280.0, -40.0)
			boolean_math_001_1.location = (-40.0, 0.0)
			group_output_11.location = (320.0000305175781, 0.0)
			group_3.location = (-620.0, -160.0)
			group_001_1.location = (-340.0, -160.0)
			boolean_math_002_1.location = (140.0, 0.0)
			boolean_math_1.location = (140.0, -140.0)
			
			#Set dimensions
			group_input_11.width, group_input_11.height = 140.0, 100.0
			boolean_math_001_1.width, boolean_math_001_1.height = 140.0, 100.0
			group_output_11.width, group_output_11.height = 140.0, 100.0
			group_3.width, group_3.height = 247.90924072265625, 100.0
			group_001_1.width, group_001_1.height = 232.0133056640625, 100.0
			boolean_math_002_1.width, boolean_math_002_1.height = 140.0, 100.0
			boolean_math_1.width, boolean_math_1.height = 140.0, 100.0
			
			#initialize is_nucleic links
			#boolean_math_002_1.Boolean -> group_output_11.Selection
			is_nucleic.links.new(boolean_math_002_1.outputs[0], group_output_11.inputs[0])
			#group_input_11.And -> boolean_math_001_1.Boolean
			is_nucleic.links.new(group_input_11.outputs[0], boolean_math_001_1.inputs[0])
			#group_3.Is Nucleic -> group_001_1.Fallback
			is_nucleic.links.new(group_3.outputs[2], group_001_1.inputs[1])
			#group_001_1.Boolean -> boolean_math_001_1.Boolean
			is_nucleic.links.new(group_001_1.outputs[0], boolean_math_001_1.inputs[1])
			#boolean_math_001_1.Boolean -> boolean_math_002_1.Boolean
			is_nucleic.links.new(boolean_math_001_1.outputs[0], boolean_math_002_1.inputs[0])
			#group_input_11.Or -> boolean_math_002_1.Boolean
			is_nucleic.links.new(group_input_11.outputs[1], boolean_math_002_1.inputs[1])
			#boolean_math_002_1.Boolean -> boolean_math_1.Boolean
			is_nucleic.links.new(boolean_math_002_1.outputs[0], boolean_math_1.inputs[0])
			#boolean_math_1.Boolean -> group_output_11.Inverted
			is_nucleic.links.new(boolean_math_1.outputs[0], group_output_11.inputs[1])
			return is_nucleic

		is_nucleic = is_nucleic_node_group()

		#initialize _mn_utils_style_ribbon_nucleic node group
		def _mn_utils_style_ribbon_nucleic_node_group():
			_mn_utils_style_ribbon_nucleic = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_utils_style_ribbon_nucleic")

			_mn_utils_style_ribbon_nucleic.color_tag = 'GEOMETRY'
			_mn_utils_style_ribbon_nucleic.description = ""

			_mn_utils_style_ribbon_nucleic.is_modifier = True
			
			#_mn_utils_style_ribbon_nucleic interface
			#Socket Ribbon + Bases
			ribbon___bases_socket = _mn_utils_style_ribbon_nucleic.interface.new_socket(name = "Ribbon + Bases", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			ribbon___bases_socket.attribute_domain = 'POINT'
			
			#Socket Ribbon Curve
			ribbon_curve_socket = _mn_utils_style_ribbon_nucleic.interface.new_socket(name = "Ribbon Curve", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			ribbon_curve_socket.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket_1 = _mn_utils_style_ribbon_nucleic.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_1.attribute_domain = 'POINT'
			atoms_socket_1.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket_1 = _mn_utils_style_ribbon_nucleic.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_1.default_value = True
			selection_socket_1.attribute_domain = 'POINT'
			selection_socket_1.hide_value = True
			selection_socket_1.description = "Selection of atoms to apply this node to"
			
			#Socket Material
			material_socket = _mn_utils_style_ribbon_nucleic.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial')
			material_socket.attribute_domain = 'POINT'
			material_socket.description = "Material to apply to the resulting geometry"
			
			#Socket Intepolate Color
			intepolate_color_socket = _mn_utils_style_ribbon_nucleic.interface.new_socket(name = "Intepolate Color", in_out='INPUT', socket_type = 'NodeSocketBool')
			intepolate_color_socket.default_value = False
			intepolate_color_socket.attribute_domain = 'POINT'
			
			#Panel Backbone
			backbone_panel = _mn_utils_style_ribbon_nucleic.interface.new_panel("Backbone")
			#Socket Backbone Subdivisions
			backbone_subdivisions_socket = _mn_utils_style_ribbon_nucleic.interface.new_socket(name = "Backbone Subdivisions", in_out='INPUT', socket_type = 'NodeSocketInt', parent = backbone_panel)
			backbone_subdivisions_socket.default_value = 3
			backbone_subdivisions_socket.min_value = 1
			backbone_subdivisions_socket.max_value = 10
			backbone_subdivisions_socket.subtype = 'NONE'
			backbone_subdivisions_socket.attribute_domain = 'POINT'
			
			#Socket Backbone Resolution
			backbone_resolution_socket = _mn_utils_style_ribbon_nucleic.interface.new_socket(name = "Backbone Resolution", in_out='INPUT', socket_type = 'NodeSocketInt', parent = backbone_panel)
			backbone_resolution_socket.default_value = 8
			backbone_resolution_socket.min_value = 3
			backbone_resolution_socket.max_value = 50
			backbone_resolution_socket.subtype = 'NONE'
			backbone_resolution_socket.attribute_domain = 'POINT'
			
			#Socket Backbone Radius
			backbone_radius_socket = _mn_utils_style_ribbon_nucleic.interface.new_socket(name = "Backbone Radius", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = backbone_panel)
			backbone_radius_socket.default_value = 2.0
			backbone_radius_socket.min_value = 0.0
			backbone_radius_socket.max_value = 3.4028234663852886e+38
			backbone_radius_socket.subtype = 'DISTANCE'
			backbone_radius_socket.attribute_domain = 'POINT'
			
			#Socket Backbone Shade Smooth
			backbone_shade_smooth_socket = _mn_utils_style_ribbon_nucleic.interface.new_socket(name = "Backbone Shade Smooth", in_out='INPUT', socket_type = 'NodeSocketBool', parent = backbone_panel)
			backbone_shade_smooth_socket.default_value = True
			backbone_shade_smooth_socket.attribute_domain = 'POINT'
			
			
			#Panel Base
			base_panel = _mn_utils_style_ribbon_nucleic.interface.new_panel("Base")
			#Socket Base Radius
			base_radius_socket = _mn_utils_style_ribbon_nucleic.interface.new_socket(name = "Base Radius", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = base_panel)
			base_radius_socket.default_value = 0.20000000298023224
			base_radius_socket.min_value = 0.0
			base_radius_socket.max_value = 3.4028234663852886e+38
			base_radius_socket.subtype = 'DISTANCE'
			base_radius_socket.attribute_domain = 'POINT'
			
			#Socket Base Resolution
			base_resolution_socket = _mn_utils_style_ribbon_nucleic.interface.new_socket(name = "Base Resolution", in_out='INPUT', socket_type = 'NodeSocketInt', parent = base_panel)
			base_resolution_socket.default_value = 6
			base_resolution_socket.min_value = 3
			base_resolution_socket.max_value = 512
			base_resolution_socket.subtype = 'NONE'
			base_resolution_socket.attribute_domain = 'POINT'
			
			
			
			#initialize _mn_utils_style_ribbon_nucleic nodes
			#node Frame.002
			frame_002 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeFrame")
			frame_002.label = "Transfer attributes to new curve / mesh from alpha carbons"
			frame_002.name = "Frame.002"
			frame_002.label_size = 20
			frame_002.shrink = True
			
			#node Frame
			frame_1 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeFrame")
			frame_1.label = "Delete between chains and distance too large"
			frame_1.name = "Frame"
			frame_1.label_size = 20
			frame_1.shrink = True
			
			#node Frame.001
			frame_001 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeFrame")
			frame_001.label = "Create New mesh line through all CA"
			frame_001.name = "Frame.001"
			frame_001.label_size = 20
			frame_001.shrink = True
			
			#node Frame.006
			frame_006 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeFrame")
			frame_006.label = "Slightly Extend Curve Ends"
			frame_006.name = "Frame.006"
			frame_006.label_size = 20
			frame_006.shrink = True
			
			#node Frame.004
			frame_004 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeFrame")
			frame_004.label = "Convert Mesh Backbone to Curve"
			frame_004.name = "Frame.004"
			frame_004.label_size = 20
			frame_004.shrink = True
			
			#node Frame.005
			frame_005 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeFrame")
			frame_005.label = "Instance simple base cylinder"
			frame_005.name = "Frame.005"
			frame_005.label_size = 20
			frame_005.shrink = True
			
			#node Frame.007
			frame_007 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeFrame")
			frame_007.label = "Align Base"
			frame_007.name = "Frame.007"
			frame_007.label_size = 20
			frame_007.shrink = True
			
			#node Frame.003
			frame_003 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeFrame")
			frame_003.label = "Create mesh from curve"
			frame_003.name = "Frame.003"
			frame_003.label_size = 20
			frame_003.shrink = True
			
			#node Sample Index
			sample_index = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSampleIndex")
			sample_index.name = "Sample Index"
			sample_index.hide = True
			sample_index.clamp = True
			sample_index.data_type = 'INT'
			sample_index.domain = 'POINT'
			
			#node Named Attribute.002
			named_attribute_002_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002_1.label = "chain_id"
			named_attribute_002_1.name = "Named Attribute.002"
			named_attribute_002_1.hide = True
			named_attribute_002_1.data_type = 'INT'
			#Name
			named_attribute_002_1.inputs[0].default_value = "chain_id"
			
			#node Sample Index.004
			sample_index_004 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSampleIndex")
			sample_index_004.name = "Sample Index.004"
			sample_index_004.hide = True
			sample_index_004.clamp = True
			sample_index_004.data_type = 'INT'
			sample_index_004.domain = 'POINT'
			
			#node Named Attribute.004
			named_attribute_004 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_004.label = "res_id"
			named_attribute_004.name = "Named Attribute.004"
			named_attribute_004.hide = True
			named_attribute_004.data_type = 'INT'
			#Name
			named_attribute_004.inputs[0].default_value = "res_id"
			
			#node Sample Index.001
			sample_index_001 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSampleIndex")
			sample_index_001.name = "Sample Index.001"
			sample_index_001.hide = True
			sample_index_001.clamp = True
			sample_index_001.data_type = 'FLOAT_COLOR'
			sample_index_001.domain = 'POINT'
			
			#node Named Attribute
			named_attribute_4 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_4.label = "Color"
			named_attribute_4.name = "Named Attribute"
			named_attribute_4.hide = True
			named_attribute_4.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute_4.inputs[0].default_value = "Color"
			
			#node Reroute.003
			reroute_003_1 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_003_1.name = "Reroute.003"
			#node Sample Index.003
			sample_index_003 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSampleIndex")
			sample_index_003.name = "Sample Index.003"
			sample_index_003.hide = True
			sample_index_003.clamp = True
			sample_index_003.data_type = 'INT'
			sample_index_003.domain = 'POINT'
			
			#node Named Attribute.003
			named_attribute_003 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_003.label = "res_name"
			named_attribute_003.name = "Named Attribute.003"
			named_attribute_003.hide = True
			named_attribute_003.data_type = 'INT'
			#Name
			named_attribute_003.inputs[0].default_value = "res_name"
			
			#node Index.003
			index_003 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputIndex")
			index_003.name = "Index.003"
			
			#node Named Attribute.005
			named_attribute_005 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_005.label = "b_factor"
			named_attribute_005.name = "Named Attribute.005"
			named_attribute_005.hide = True
			named_attribute_005.data_type = 'FLOAT'
			#Name
			named_attribute_005.inputs[0].default_value = "b_factor"
			
			#node Sample Index.005
			sample_index_005 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSampleIndex")
			sample_index_005.name = "Sample Index.005"
			sample_index_005.hide = True
			sample_index_005.clamp = True
			sample_index_005.data_type = 'FLOAT'
			sample_index_005.domain = 'POINT'
			
			#node Reroute.001
			reroute_001_2 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_001_2.name = "Reroute.001"
			#node Reroute.010
			reroute_010 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_010.name = "Reroute.010"
			#node Sample Index.008
			sample_index_008 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSampleIndex")
			sample_index_008.name = "Sample Index.008"
			sample_index_008.hide = True
			sample_index_008.clamp = True
			sample_index_008.data_type = 'INT'
			sample_index_008.domain = 'POINT'
			
			#node Named Attribute.006
			named_attribute_006 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_006.label = "chain_id"
			named_attribute_006.name = "Named Attribute.006"
			named_attribute_006.hide = True
			named_attribute_006.data_type = 'INT'
			#Name
			named_attribute_006.inputs[0].default_value = "chain_id"
			
			#node Index.004
			index_004 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputIndex")
			index_004.name = "Index.004"
			
			#node Reroute.002
			reroute_002_2 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_002_2.name = "Reroute.002"
			#node Edge Vertices
			edge_vertices = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputMeshEdgeVertices")
			edge_vertices.name = "Edge Vertices"
			
			#node Field at Index
			field_at_index = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeFieldAtIndex")
			field_at_index.name = "Field at Index"
			field_at_index.data_type = 'INT'
			field_at_index.domain = 'POINT'
			
			#node Field at Index.001
			field_at_index_001 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeFieldAtIndex")
			field_at_index_001.name = "Field at Index.001"
			field_at_index_001.data_type = 'INT'
			field_at_index_001.domain = 'POINT'
			
			#node Vector Math
			vector_math = _mn_utils_style_ribbon_nucleic.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.operation = 'DISTANCE'
			
			#node Compare.001
			compare_001_2 = _mn_utils_style_ribbon_nucleic.nodes.new("FunctionNodeCompare")
			compare_001_2.name = "Compare.001"
			compare_001_2.data_type = 'FLOAT'
			compare_001_2.mode = 'ELEMENT'
			compare_001_2.operation = 'GREATER_THAN'
			#B
			compare_001_2.inputs[1].default_value = 0.10000000149011612
			
			#node Compare
			compare_2 = _mn_utils_style_ribbon_nucleic.nodes.new("FunctionNodeCompare")
			compare_2.name = "Compare"
			compare_2.data_type = 'INT'
			compare_2.mode = 'ELEMENT'
			compare_2.operation = 'NOT_EQUAL'
			
			#node Boolean Math
			boolean_math_2 = _mn_utils_style_ribbon_nucleic.nodes.new("FunctionNodeBooleanMath")
			boolean_math_2.name = "Boolean Math"
			boolean_math_2.operation = 'OR'
			
			#node Reroute.009
			reroute_009 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_009.name = "Reroute.009"
			#node Reroute.012
			reroute_012 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_012.name = "Reroute.012"
			#node Mesh Line
			mesh_line = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeMeshLine")
			mesh_line.name = "Mesh Line"
			mesh_line.hide = True
			mesh_line.count_mode = 'TOTAL'
			mesh_line.mode = 'END_POINTS'
			#Start Location
			mesh_line.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Offset
			mesh_line.inputs[3].default_value = (0.0, 0.0, 1.0)
			
			#node Set Position
			set_position = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSetPosition")
			set_position.name = "Set Position"
			set_position.hide = True
			#Selection
			set_position.inputs[1].default_value = True
			#Offset
			set_position.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Domain Size
			domain_size = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeAttributeDomainSize")
			domain_size.name = "Domain Size"
			domain_size.hide = True
			domain_size.component = 'MESH'
			domain_size.outputs[1].hide = True
			domain_size.outputs[2].hide = True
			domain_size.outputs[3].hide = True
			domain_size.outputs[4].hide = True
			domain_size.outputs[5].hide = True
			
			#node Delete Geometry
			delete_geometry = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeDeleteGeometry")
			delete_geometry.name = "Delete Geometry"
			delete_geometry.domain = 'EDGE'
			delete_geometry.mode = 'ALL'
			
			#node Sample Index.009
			sample_index_009_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSampleIndex")
			sample_index_009_1.name = "Sample Index.009"
			sample_index_009_1.hide = True
			sample_index_009_1.clamp = True
			sample_index_009_1.data_type = 'BOOLEAN'
			sample_index_009_1.domain = 'POINT'
			
			#node Group Input.006
			group_input_006 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeGroupInput")
			group_input_006.name = "Group Input.006"
			group_input_006.outputs[0].hide = True
			group_input_006.outputs[1].hide = True
			group_input_006.outputs[2].hide = True
			group_input_006.outputs[3].hide = True
			group_input_006.outputs[4].hide = True
			group_input_006.outputs[5].hide = True
			group_input_006.outputs[8].hide = True
			group_input_006.outputs[9].hide = True
			group_input_006.outputs[10].hide = True
			
			#node Sample Index.007
			sample_index_007 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSampleIndex")
			sample_index_007.name = "Sample Index.007"
			sample_index_007.hide = True
			sample_index_007.clamp = True
			sample_index_007.data_type = 'FLOAT'
			sample_index_007.domain = 'POINT'
			
			#node Group Output
			group_output_12 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeGroupOutput")
			group_output_12.name = "Group Output"
			group_output_12.is_active_output = True
			
			#node Offset Point in Curve
			offset_point_in_curve = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeOffsetPointInCurve")
			offset_point_in_curve.name = "Offset Point in Curve"
			#Point Index
			offset_point_in_curve.inputs[0].default_value = 0
			
			#node Evaluate at Index
			evaluate_at_index_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_1.name = "Evaluate at Index"
			evaluate_at_index_1.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_1.domain = 'POINT'
			
			#node Position.002
			position_002_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputPosition")
			position_002_1.name = "Position.002"
			
			#node Vector Math.002
			vector_math_002_1 = _mn_utils_style_ribbon_nucleic.nodes.new("ShaderNodeVectorMath")
			vector_math_002_1.name = "Vector Math.002"
			vector_math_002_1.operation = 'SUBTRACT'
			
			#node Vector Math.004
			vector_math_004_1 = _mn_utils_style_ribbon_nucleic.nodes.new("ShaderNodeVectorMath")
			vector_math_004_1.name = "Vector Math.004"
			vector_math_004_1.operation = 'SCALE'
			#Scale
			vector_math_004_1.inputs[3].default_value = -0.5
			
			#node Endpoint Selection
			endpoint_selection = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection.name = "Endpoint Selection"
			#Start Size
			endpoint_selection.inputs[0].default_value = 1
			#End Size
			endpoint_selection.inputs[1].default_value = 1
			
			#node Switch
			switch_3 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSwitch")
			switch_3.name = "Switch"
			switch_3.input_type = 'INT'
			#False
			switch_3.inputs[1].default_value = -1
			#True
			switch_3.inputs[2].default_value = 1
			
			#node Endpoint Selection.001
			endpoint_selection_001 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_001.name = "Endpoint Selection.001"
			#Start Size
			endpoint_selection_001.inputs[0].default_value = 1
			#End Size
			endpoint_selection_001.inputs[1].default_value = 0
			
			#node Set Position.001
			set_position_001 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSetPosition")
			set_position_001.name = "Set Position.001"
			#Position
			set_position_001.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Store Named Attribute.001
			store_named_attribute_001 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_001.name = "Store Named Attribute.001"
			store_named_attribute_001.data_type = 'INT'
			store_named_attribute_001.domain = 'POINT'
			#Selection
			store_named_attribute_001.inputs[1].default_value = True
			#Name
			store_named_attribute_001.inputs[2].default_value = "chain_id"
			
			#node Store Named Attribute.002
			store_named_attribute_002 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_002.name = "Store Named Attribute.002"
			store_named_attribute_002.data_type = 'INT'
			store_named_attribute_002.domain = 'POINT'
			#Selection
			store_named_attribute_002.inputs[1].default_value = True
			#Name
			store_named_attribute_002.inputs[2].default_value = "res_id"
			
			#node Store Named Attribute.003
			store_named_attribute_003 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_003.name = "Store Named Attribute.003"
			store_named_attribute_003.data_type = 'INT'
			store_named_attribute_003.domain = 'POINT'
			#Selection
			store_named_attribute_003.inputs[1].default_value = True
			#Name
			store_named_attribute_003.inputs[2].default_value = "res_name"
			
			#node Store Named Attribute.004
			store_named_attribute_004 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_004.name = "Store Named Attribute.004"
			store_named_attribute_004.data_type = 'FLOAT'
			store_named_attribute_004.domain = 'POINT'
			#Selection
			store_named_attribute_004.inputs[1].default_value = True
			#Name
			store_named_attribute_004.inputs[2].default_value = "b_factor"
			
			#node Capture Attribute
			capture_attribute = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute.name = "Capture Attribute"
			capture_attribute.active_index = 0
			capture_attribute.capture_items.clear()
			capture_attribute.capture_items.new('FLOAT', "Value")
			capture_attribute.capture_items["Value"].data_type = 'BOOLEAN'
			capture_attribute.domain = 'POINT'
			
			#node Set Handle Type
			set_handle_type = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeCurveSetHandles")
			set_handle_type.name = "Set Handle Type"
			set_handle_type.handle_type = 'AUTO'
			set_handle_type.mode = {'LEFT', 'RIGHT'}
			#Selection
			set_handle_type.inputs[1].default_value = True
			
			#node Set Spline Type
			set_spline_type = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeCurveSplineType")
			set_spline_type.name = "Set Spline Type"
			set_spline_type.spline_type = 'BEZIER'
			#Selection
			set_spline_type.inputs[1].default_value = True
			
			#node Group Input.004
			group_input_004 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeGroupInput")
			group_input_004.name = "Group Input.004"
			group_input_004.outputs[0].hide = True
			group_input_004.outputs[1].hide = True
			group_input_004.outputs[2].hide = True
			group_input_004.outputs[3].hide = True
			group_input_004.outputs[5].hide = True
			group_input_004.outputs[6].hide = True
			group_input_004.outputs[7].hide = True
			group_input_004.outputs[8].hide = True
			group_input_004.outputs[9].hide = True
			group_input_004.outputs[10].hide = True
			
			#node Mesh to Curve
			mesh_to_curve = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeMeshToCurve")
			mesh_to_curve.name = "Mesh to Curve"
			#Selection
			mesh_to_curve.inputs[1].default_value = True
			
			#node Set Spline Resolution
			set_spline_resolution = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSetSplineResolution")
			set_spline_resolution.name = "Set Spline Resolution"
			#Selection
			set_spline_resolution.inputs[1].default_value = True
			
			#node Store Named Attribute
			store_named_attribute = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute.name = "Store Named Attribute"
			store_named_attribute.data_type = 'FLOAT_COLOR'
			store_named_attribute.domain = 'POINT'
			#Selection
			store_named_attribute.inputs[1].default_value = True
			#Name
			store_named_attribute.inputs[2].default_value = "Color"
			
			#node Store Named Attribute.007
			store_named_attribute_007 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_007.name = "Store Named Attribute.007"
			store_named_attribute_007.data_type = 'FLOAT_VECTOR'
			store_named_attribute_007.domain = 'POINT'
			#Selection
			store_named_attribute_007.inputs[1].default_value = True
			#Name
			store_named_attribute_007.inputs[2].default_value = "vec_horizontal"
			
			#node Store Named Attribute.008
			store_named_attribute_008 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_008.name = "Store Named Attribute.008"
			store_named_attribute_008.data_type = 'FLOAT_VECTOR'
			store_named_attribute_008.domain = 'POINT'
			#Selection
			store_named_attribute_008.inputs[1].default_value = True
			#Name
			store_named_attribute_008.inputs[2].default_value = "vec_vertical"
			
			#node Store Named Attribute.009
			store_named_attribute_009 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_009.name = "Store Named Attribute.009"
			store_named_attribute_009.data_type = 'FLOAT_VECTOR'
			store_named_attribute_009.domain = 'POINT'
			#Selection
			store_named_attribute_009.inputs[1].default_value = True
			#Name
			store_named_attribute_009.inputs[2].default_value = "atom_interface"
			
			#node Store Named Attribute.010
			store_named_attribute_010 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_010.name = "Store Named Attribute.010"
			store_named_attribute_010.data_type = 'FLOAT_VECTOR'
			store_named_attribute_010.domain = 'POINT'
			#Selection
			store_named_attribute_010.inputs[1].default_value = True
			#Name
			store_named_attribute_010.inputs[2].default_value = "atom_pivot"
			
			#node Combine XYZ
			combine_xyz = _mn_utils_style_ribbon_nucleic.nodes.new("ShaderNodeCombineXYZ")
			combine_xyz.name = "Combine XYZ"
			#X
			combine_xyz.inputs[0].default_value = 0.0
			#Y
			combine_xyz.inputs[1].default_value = 0.0
			
			#node Math
			math_2 = _mn_utils_style_ribbon_nucleic.nodes.new("ShaderNodeMath")
			math_2.name = "Math"
			math_2.operation = 'DIVIDE'
			math_2.use_clamp = False
			#Value_001
			math_2.inputs[1].default_value = 2.0
			
			#node Cylinder
			cylinder = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeMeshCylinder")
			cylinder.name = "Cylinder"
			cylinder.fill_type = 'NGON'
			#Side Segments
			cylinder.inputs[1].default_value = 1
			#Fill Segments
			cylinder.inputs[2].default_value = 1
			
			#node Value
			value = _mn_utils_style_ribbon_nucleic.nodes.new("ShaderNodeValue")
			value.name = "Value"
			
			value.outputs[0].default_value = 1.0
			#node Group Input.005
			group_input_005 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeGroupInput")
			group_input_005.name = "Group Input.005"
			group_input_005.outputs[0].hide = True
			group_input_005.outputs[1].hide = True
			group_input_005.outputs[2].hide = True
			group_input_005.outputs[3].hide = True
			group_input_005.outputs[4].hide = True
			group_input_005.outputs[5].hide = True
			group_input_005.outputs[6].hide = True
			group_input_005.outputs[7].hide = True
			group_input_005.outputs[10].hide = True
			
			#node Store Named Attribute.006
			store_named_attribute_006 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_006.name = "Store Named Attribute.006"
			store_named_attribute_006.data_type = 'FLOAT_VECTOR'
			store_named_attribute_006.domain = 'CORNER'
			#Selection
			store_named_attribute_006.inputs[1].default_value = True
			#Name
			store_named_attribute_006.inputs[2].default_value = "uv_map"
			
			#node Position.001
			position_001 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputPosition")
			position_001.name = "Position.001"
			
			#node Store Named Attribute.005
			store_named_attribute_005 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_005.name = "Store Named Attribute.005"
			store_named_attribute_005.data_type = 'FLOAT_COLOR'
			store_named_attribute_005.domain = 'POINT'
			#Selection
			store_named_attribute_005.inputs[1].default_value = True
			#Name
			store_named_attribute_005.inputs[2].default_value = "Color"
			
			#node Separate Geometry
			separate_geometry = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry.name = "Separate Geometry"
			separate_geometry.domain = 'POINT'
			
			#node Group Input
			group_input_12 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeGroupInput")
			group_input_12.name = "Group Input"
			group_input_12.outputs[3].hide = True
			
			#node Group.004
			group_004 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeGroup")
			group_004.name = "Group.004"
			group_004.node_tree = _sampleatomvalue
			#Input_1
			group_004.inputs[1].default_value = 67
			
			#node Reroute.006
			reroute_006 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_006.name = "Reroute.006"
			#node Reroute.011
			reroute_011 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_011.name = "Reroute.011"
			#node Group.006
			group_006 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeGroup")
			group_006.name = "Group.006"
			group_006.node_tree = _base_align
			
			#node Transform
			transform = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeTransform")
			transform.name = "Transform"
			transform.mode = 'COMPONENTS'
			#Rotation
			transform.inputs[2].default_value = (0.0, 0.0, 0.7853981852531433)
			#Scale
			transform.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Instance on Points
			instance_on_points = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInstanceOnPoints")
			instance_on_points.name = "Instance on Points"
			#Selection
			instance_on_points.inputs[1].default_value = True
			#Pick Instance
			instance_on_points.inputs[3].default_value = False
			#Instance Index
			instance_on_points.inputs[4].default_value = 0
			
			#node Group.003
			group_003 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeGroup")
			group_003.name = "Group.003"
			group_003.node_tree = _sampleatomvalue
			#Input_1
			group_003.inputs[1].default_value = 55
			
			#node Combine XYZ.001
			combine_xyz_001 = _mn_utils_style_ribbon_nucleic.nodes.new("ShaderNodeCombineXYZ")
			combine_xyz_001.name = "Combine XYZ.001"
			#X
			combine_xyz_001.inputs[0].default_value = 0.019999999552965164
			#Y
			combine_xyz_001.inputs[1].default_value = 0.10000000149011612
			
			#node Vector Math.003
			vector_math_003 = _mn_utils_style_ribbon_nucleic.nodes.new("ShaderNodeVectorMath")
			vector_math_003.name = "Vector Math.003"
			vector_math_003.operation = 'LENGTH'
			
			#node Vector Math.001
			vector_math_001 = _mn_utils_style_ribbon_nucleic.nodes.new("ShaderNodeVectorMath")
			vector_math_001.name = "Vector Math.001"
			vector_math_001.operation = 'SUBTRACT'
			
			#node Align Euler to Vector.001
			align_euler_to_vector_001 = _mn_utils_style_ribbon_nucleic.nodes.new("FunctionNodeAlignEulerToVector")
			align_euler_to_vector_001.name = "Align Euler to Vector.001"
			align_euler_to_vector_001.axis = 'Y'
			align_euler_to_vector_001.pivot_axis = 'Z'
			#Factor
			align_euler_to_vector_001.inputs[1].default_value = 1.0
			
			#node Align Euler to Vector
			align_euler_to_vector = _mn_utils_style_ribbon_nucleic.nodes.new("FunctionNodeAlignEulerToVector")
			align_euler_to_vector.name = "Align Euler to Vector"
			align_euler_to_vector.axis = 'Z'
			align_euler_to_vector.pivot_axis = 'AUTO'
			#Rotation
			align_euler_to_vector.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Factor
			align_euler_to_vector.inputs[1].default_value = 1.0
			
			#node Named Attribute.007
			named_attribute_007 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_007.name = "Named Attribute.007"
			named_attribute_007.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_007.inputs[0].default_value = "vec_horizontal"
			
			#node Named Attribute.008
			named_attribute_008 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_008.name = "Named Attribute.008"
			named_attribute_008.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_008.inputs[0].default_value = "atom_interface"
			
			#node Capture Attribute.001
			capture_attribute_001 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute_001.name = "Capture Attribute.001"
			capture_attribute_001.active_index = 0
			capture_attribute_001.capture_items.clear()
			capture_attribute_001.capture_items.new('FLOAT', "Value")
			capture_attribute_001.capture_items["Value"].data_type = 'INT'
			capture_attribute_001.domain = 'POINT'
			
			#node Index
			index_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputIndex")
			index_1.name = "Index"
			
			#node Named Attribute.009
			named_attribute_009_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_009_1.name = "Named Attribute.009"
			named_attribute_009_1.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute_009_1.inputs[0].default_value = "Color"
			
			#node Sample Index.002
			sample_index_002 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSampleIndex")
			sample_index_002.name = "Sample Index.002"
			sample_index_002.clamp = False
			sample_index_002.data_type = 'FLOAT_COLOR'
			sample_index_002.domain = 'POINT'
			
			#node Reroute.004
			reroute_004 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_004.name = "Reroute.004"
			#node Set Shade Smooth
			set_shade_smooth = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSetShadeSmooth")
			set_shade_smooth.name = "Set Shade Smooth"
			set_shade_smooth.domain = 'FACE'
			#Selection
			set_shade_smooth.inputs[1].default_value = True
			
			#node Reroute.007
			reroute_007 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_007.name = "Reroute.007"
			#node Curve Circle
			curve_circle = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeCurvePrimitiveCircle")
			curve_circle.name = "Curve Circle"
			curve_circle.hide = True
			curve_circle.mode = 'RADIUS'
			#Radius
			curve_circle.inputs[4].default_value = 0.009999999776482582
			
			#node Group Input.003
			group_input_003 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeGroupInput")
			group_input_003.name = "Group Input.003"
			group_input_003.outputs[0].hide = True
			group_input_003.outputs[1].hide = True
			group_input_003.outputs[2].hide = True
			group_input_003.outputs[3].hide = True
			group_input_003.outputs[4].hide = True
			group_input_003.outputs[6].hide = True
			group_input_003.outputs[7].hide = True
			group_input_003.outputs[8].hide = True
			group_input_003.outputs[9].hide = True
			group_input_003.outputs[10].hide = True
			
			#node Set Material
			set_material = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSetMaterial")
			set_material.name = "Set Material"
			#Selection
			set_material.inputs[1].default_value = True
			
			#node Reroute.005
			reroute_005 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_005.name = "Reroute.005"
			#node Reroute.008
			reroute_008 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_008.name = "Reroute.008"
			#node Curve to Mesh
			curve_to_mesh = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeCurveToMesh")
			curve_to_mesh.name = "Curve to Mesh"
			#Fill Caps
			curve_to_mesh.inputs[2].default_value = True
			
			#node Set Curve Radius
			set_curve_radius = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSetCurveRadius")
			set_curve_radius.name = "Set Curve Radius"
			#Selection
			set_curve_radius.inputs[1].default_value = True
			
			#node Group Input.002
			group_input_002 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeGroupInput")
			group_input_002.name = "Group Input.002"
			group_input_002.outputs[0].hide = True
			group_input_002.outputs[1].hide = True
			group_input_002.outputs[3].hide = True
			group_input_002.outputs[4].hide = True
			group_input_002.outputs[5].hide = True
			group_input_002.outputs[6].hide = True
			group_input_002.outputs[7].hide = True
			group_input_002.outputs[8].hide = True
			group_input_002.outputs[9].hide = True
			group_input_002.outputs[10].hide = True
			
			#node Join Geometry.001
			join_geometry_001 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_001.name = "Join Geometry.001"
			join_geometry_001.hide = True
			
			#node Reroute.013
			reroute_013 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_013.name = "Reroute.013"
			#node Store Named Attribute.011
			store_named_attribute_011 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_011.name = "Store Named Attribute.011"
			store_named_attribute_011.data_type = 'FLOAT_COLOR'
			store_named_attribute_011.domain = 'FACE'
			#Selection
			store_named_attribute_011.inputs[1].default_value = True
			#Name
			store_named_attribute_011.inputs[2].default_value = "Color"
			
			#node Switch.001
			switch_001_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSwitch")
			switch_001_1.name = "Switch.001"
			switch_001_1.input_type = 'GEOMETRY'
			
			#node Group Input.001
			group_input_001 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeGroupInput")
			group_input_001.name = "Group Input.001"
			group_input_001.outputs[0].hide = True
			group_input_001.outputs[1].hide = True
			group_input_001.outputs[2].hide = True
			group_input_001.outputs[4].hide = True
			group_input_001.outputs[5].hide = True
			group_input_001.outputs[6].hide = True
			group_input_001.outputs[7].hide = True
			group_input_001.outputs[8].hide = True
			group_input_001.outputs[9].hide = True
			group_input_001.outputs[10].hide = True
			
			#node Group
			group_4 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeGroup")
			group_4.name = "Group"
			group_4.node_tree = residue_mask
			#Socket_1
			group_4.inputs[0].default_value = 1
			#Socket_5
			group_4.inputs[1].default_value = True
			#Socket_4
			group_4.inputs[2].default_value = 0
			
			#node Is Nucleic
			is_nucleic_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeGroup")
			is_nucleic_1.label = "Is Nucleic"
			is_nucleic_1.name = "Is Nucleic"
			is_nucleic_1.node_tree = is_nucleic
			#Socket_3
			is_nucleic_1.inputs[1].default_value = False
			
			#node Group.005
			group_005 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeGroup")
			group_005.name = "Group.005"
			group_005.node_tree = _sampleatomvalue
			#Input_1
			group_005.inputs[1].default_value = 57
			
			#node Reroute
			reroute_1 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_1.name = "Reroute"
			#node Mix
			mix = _mn_utils_style_ribbon_nucleic.nodes.new("ShaderNodeMix")
			mix.name = "Mix"
			mix.blend_type = 'MIX'
			mix.clamp_factor = True
			mix.clamp_result = False
			mix.data_type = 'VECTOR'
			mix.factor_mode = 'UNIFORM'
			#Factor_Float
			mix.inputs[0].default_value = 1.0
			
			
			
			#Set parents
			sample_index.parent = frame_002
			named_attribute_002_1.parent = frame_002
			sample_index_004.parent = frame_002
			named_attribute_004.parent = frame_002
			sample_index_001.parent = frame_002
			named_attribute_4.parent = frame_002
			reroute_003_1.parent = frame_002
			sample_index_003.parent = frame_002
			named_attribute_003.parent = frame_002
			index_003.parent = frame_002
			named_attribute_005.parent = frame_002
			sample_index_005.parent = frame_002
			reroute_001_2.parent = frame_002
			sample_index_008.parent = frame_1
			named_attribute_006.parent = frame_1
			index_004.parent = frame_1
			reroute_002_2.parent = frame_1
			edge_vertices.parent = frame_1
			field_at_index.parent = frame_1
			field_at_index_001.parent = frame_1
			vector_math.parent = frame_1
			compare_001_2.parent = frame_1
			compare_2.parent = frame_1
			boolean_math_2.parent = frame_1
			mesh_line.parent = frame_001
			set_position.parent = frame_001
			domain_size.parent = frame_001
			delete_geometry.parent = frame_1
			offset_point_in_curve.parent = frame_006
			evaluate_at_index_1.parent = frame_006
			position_002_1.parent = frame_006
			vector_math_002_1.parent = frame_006
			vector_math_004_1.parent = frame_006
			endpoint_selection.parent = frame_006
			switch_3.parent = frame_006
			endpoint_selection_001.parent = frame_006
			set_position_001.parent = frame_006
			set_handle_type.parent = frame_004
			set_spline_type.parent = frame_004
			group_input_004.parent = frame_004
			mesh_to_curve.parent = frame_004
			set_spline_resolution.parent = frame_004
			combine_xyz.parent = frame_005
			math_2.parent = frame_005
			cylinder.parent = frame_005
			value.parent = frame_005
			group_input_005.parent = frame_005
			store_named_attribute_006.parent = frame_005
			position_001.parent = frame_007
			transform.parent = frame_005
			instance_on_points.parent = frame_005
			combine_xyz_001.parent = frame_007
			vector_math_003.parent = frame_007
			vector_math_001.parent = frame_007
			align_euler_to_vector_001.parent = frame_007
			align_euler_to_vector.parent = frame_007
			named_attribute_007.parent = frame_007
			named_attribute_008.parent = frame_007
			reroute_004.parent = frame_003
			set_shade_smooth.parent = frame_003
			reroute_007.parent = frame_003
			curve_circle.parent = frame_003
			group_input_003.parent = frame_003
			reroute_005.parent = frame_003
			reroute_008.parent = frame_003
			curve_to_mesh.parent = frame_003
			set_curve_radius.parent = frame_003
			group_input_002.parent = frame_003
			join_geometry_001.parent = frame_003
			reroute_013.parent = frame_003
			
			#Set locations
			frame_002.location = (1158.6292724609375, -29.90658187866211)
			frame_1.location = (-740.1123657226562, 293.3905944824219)
			frame_001.location = (-721.0, 75.0)
			frame_006.location = (252.1446533203125, -22.4365234375)
			frame_004.location = (-210.0, 260.0)
			frame_005.location = (397.0, 475.0)
			frame_007.location = (2083.0, 37.0)
			frame_003.location = (58.0, -11.0)
			sample_index.location = (-660.0, 820.0)
			named_attribute_002_1.location = (-660.0, 780.0)
			sample_index_004.location = (-660.0, 880.0)
			named_attribute_004.location = (-660.0, 920.0)
			sample_index_001.location = (-664.6292724609375, 689.9065551757812)
			named_attribute_4.location = (-664.6292724609375, 729.9065551757812)
			reroute_003_1.location = (-784.6292724609375, 869.9065551757812)
			sample_index_003.location = (-660.0, 980.0)
			named_attribute_003.location = (-660.0, 1020.0)
			index_003.location = (-964.6292724609375, 909.9065551757812)
			named_attribute_005.location = (-664.6292724609375, 1109.9066162109375)
			sample_index_005.location = (-664.6292724609375, 1069.9066162109375)
			reroute_001_2.location = (-804.6292724609375, 969.9065551757812)
			reroute_010.location = (-6.0, 640.0)
			sample_index_008.location = (-259.96295166015625, -143.635009765625)
			named_attribute_006.location = (-439.96295166015625, -143.635009765625)
			index_004.location = (-439.96295166015625, -183.635009765625)
			reroute_002_2.location = (-100.0, -140.0)
			edge_vertices.location = (-220.0, -220.0)
			field_at_index.location = (0.0, 0.0)
			field_at_index_001.location = (0.0, -160.0)
			vector_math.location = (0.0, -320.0)
			compare_001_2.location = (160.0, -160.0)
			compare_2.location = (160.0, 0.0)
			boolean_math_2.location = (320.0, 0.0)
			reroute_009.location = (-1531.0, 160.0)
			reroute_012.location = (-1691.0, 640.0)
			mesh_line.location = (-690.0, 385.0)
			set_position.location = (-690.0, 345.0)
			domain_size.location = (-690.0, 425.0)
			delete_geometry.location = (320.0, 220.0)
			sample_index_009_1.location = (500.0, 1180.0)
			group_input_006.location = (280.0, 1260.0)
			sample_index_007.location = (500.0, 1240.0)
			group_output_12.location = (4000.0, 540.0)
			offset_point_in_curve.location = (1740.0, 1060.0)
			evaluate_at_index_1.location = (1900.0, 1060.0)
			position_002_1.location = (1740.0, 940.0)
			vector_math_002_1.location = (2060.0, 1060.0)
			vector_math_004_1.location = (1900.0, 900.0)
			endpoint_selection.location = (2067.57958984375, 912.9168701171875)
			switch_3.location = (1580.0, 1060.0)
			endpoint_selection_001.location = (1420.0, 1060.0)
			set_position_001.location = (2240.0, 1060.0)
			store_named_attribute_001.location = (1280.0, 620.0)
			store_named_attribute_002.location = (1440.0, 620.0)
			store_named_attribute_003.location = (1600.0, 620.0)
			store_named_attribute_004.location = (1760.0, 620.0)
			capture_attribute.location = (1940.0, 620.0)
			set_handle_type.location = (840.0, 260.0)
			set_spline_type.location = (670.0, 260.0)
			group_input_004.location = (1010.0, 120.0)
			mesh_to_curve.location = (510.0, 260.0)
			set_spline_resolution.location = (1010.0, 260.0)
			store_named_attribute.location = (1120.0, 620.0)
			store_named_attribute_007.location = (360.0, 40.0)
			store_named_attribute_008.location = (180.0, 40.0)
			store_named_attribute_009.location = (20.0, 40.0)
			store_named_attribute_010.location = (-140.0, 40.0)
			combine_xyz.location = (114.9571533203125, -1317.4541015625)
			math_2.location = (114.9571533203125, -1457.4541015625)
			cylinder.location = (-45.042877197265625, -1237.4541015625)
			value.location = (-59.143829345703125, -1534.919921875)
			group_input_005.location = (-246.84564208984375, -1389.357421875)
			store_named_attribute_006.location = (120.856201171875, -1094.919921875)
			position_001.location = (-1639.0, -1617.0)
			store_named_attribute_005.location = (540.0, 40.0)
			separate_geometry.location = (-2960.0, 0.0)
			group_input_12.location = (-3360.0, -60.0)
			group_004.location = (340.0, -200.0)
			reroute_006.location = (-260.0, -380.0)
			reroute_011.location = (240.0, -380.0)
			group_006.location = (-220.0, -180.0)
			transform.location = (314.9571533203125, -1217.4541015625)
			instance_on_points.location = (827.0, -1386.0)
			group_003.location = (-2100.0, 660.0)
			combine_xyz_001.location = (-1123.0, -1517.0)
			vector_math_003.location = (-1283.0, -1517.0)
			vector_math_001.location = (-1443.0, -1517.0)
			align_euler_to_vector_001.location = (-1123.0, -1297.0)
			align_euler_to_vector.location = (-1283.0, -1297.0)
			named_attribute_007.location = (-1678.014892578125, -1337.0)
			named_attribute_008.location = (-1679.2340087890625, -1477.0)
			capture_attribute_001.location = (2806.529052734375, 1155.515625)
			index_1.location = (2800.0, 960.0)
			named_attribute_009_1.location = (3040.0, 1000.0)
			sample_index_002.location = (3040.0, 1220.0)
			reroute_004.location = (2300.0, 400.0)
			set_shade_smooth.location = (2885.609130859375, 590.6487426757812)
			reroute_007.location = (2846.0, 400.0)
			curve_circle.location = (2546.0, 500.0)
			group_input_003.location = (2546.0, 460.0)
			set_material.location = (3380.0, 660.0)
			reroute_005.location = (3462.0, 231.0)
			reroute_008.location = (2862.0, 231.0)
			curve_to_mesh.location = (2722.0, 591.0)
			set_curve_radius.location = (2162.0, 631.0)
			group_input_002.location = (3322.0, 531.0)
			join_geometry_001.location = (3122.0, 551.0)
			reroute_013.location = (3074.18017578125, 548.1685791015625)
			store_named_attribute_011.location = (2940.4248046875, 856.4732666015625)
			switch_001_1.location = (3100.0, 860.0)
			group_input_001.location = (3100.0, 940.0)
			group_4.location = (-2840.0, 520.0)
			is_nucleic_1.location = (-3180.0, -120.0)
			group_005.location = (-2100.0, 480.0)
			reroute_1.location = (-2180.0, 540.0)
			mix.location = (-1827.638427734375, 608.8980102539062)
			
			#Set dimensions
			frame_002.width, frame_002.height = 504.5, 520.0000610351562
			frame_1.width, frame_1.height = 960.0, 734.0
			frame_001.width, frame_001.height = 200.0, 180.0
			frame_006.width, frame_006.height = 1020.0001220703125, 354.0
			frame_004.width, frame_004.height = 700.0, 262.0
			frame_005.width, frame_005.height = 1274.0, 590.0
			frame_007.width, frame_007.height = 756.0, 440.0
			frame_003.width, frame_003.height = 1364.0, 474.0
			sample_index.width, sample_index.height = 140.0, 100.0
			named_attribute_002_1.width, named_attribute_002_1.height = 140.0, 100.0
			sample_index_004.width, sample_index_004.height = 140.0, 100.0
			named_attribute_004.width, named_attribute_004.height = 140.0, 100.0
			sample_index_001.width, sample_index_001.height = 140.0, 100.0
			named_attribute_4.width, named_attribute_4.height = 140.0, 100.0
			reroute_003_1.width, reroute_003_1.height = 16.0, 100.0
			sample_index_003.width, sample_index_003.height = 140.0, 100.0
			named_attribute_003.width, named_attribute_003.height = 140.0, 100.0
			index_003.width, index_003.height = 140.0, 100.0
			named_attribute_005.width, named_attribute_005.height = 140.0, 100.0
			sample_index_005.width, sample_index_005.height = 140.0, 100.0
			reroute_001_2.width, reroute_001_2.height = 16.0, 100.0
			reroute_010.width, reroute_010.height = 16.0, 100.0
			sample_index_008.width, sample_index_008.height = 140.0, 100.0
			named_attribute_006.width, named_attribute_006.height = 140.0, 100.0
			index_004.width, index_004.height = 140.0, 100.0
			reroute_002_2.width, reroute_002_2.height = 16.0, 100.0
			edge_vertices.width, edge_vertices.height = 140.0, 100.0
			field_at_index.width, field_at_index.height = 140.0, 100.0
			field_at_index_001.width, field_at_index_001.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			compare_001_2.width, compare_001_2.height = 140.0, 100.0
			compare_2.width, compare_2.height = 140.0, 100.0
			boolean_math_2.width, boolean_math_2.height = 140.0, 100.0
			reroute_009.width, reroute_009.height = 16.0, 100.0
			reroute_012.width, reroute_012.height = 16.0, 100.0
			mesh_line.width, mesh_line.height = 140.0, 100.0
			set_position.width, set_position.height = 140.0, 100.0
			domain_size.width, domain_size.height = 140.0, 100.0
			delete_geometry.width, delete_geometry.height = 140.0, 100.0
			sample_index_009_1.width, sample_index_009_1.height = 140.0, 100.0
			group_input_006.width, group_input_006.height = 140.0, 100.0
			sample_index_007.width, sample_index_007.height = 140.0, 100.0
			group_output_12.width, group_output_12.height = 140.0, 100.0
			offset_point_in_curve.width, offset_point_in_curve.height = 140.0, 100.0
			evaluate_at_index_1.width, evaluate_at_index_1.height = 140.0, 100.0
			position_002_1.width, position_002_1.height = 140.0, 100.0
			vector_math_002_1.width, vector_math_002_1.height = 140.0, 100.0
			vector_math_004_1.width, vector_math_004_1.height = 140.0, 100.0
			endpoint_selection.width, endpoint_selection.height = 140.0, 100.0
			switch_3.width, switch_3.height = 140.0, 100.0
			endpoint_selection_001.width, endpoint_selection_001.height = 140.0, 100.0
			set_position_001.width, set_position_001.height = 140.0, 100.0
			store_named_attribute_001.width, store_named_attribute_001.height = 140.0, 100.0
			store_named_attribute_002.width, store_named_attribute_002.height = 140.0, 100.0
			store_named_attribute_003.width, store_named_attribute_003.height = 140.0, 100.0
			store_named_attribute_004.width, store_named_attribute_004.height = 140.0, 100.0
			capture_attribute.width, capture_attribute.height = 140.0, 100.0
			set_handle_type.width, set_handle_type.height = 140.0, 100.0
			set_spline_type.width, set_spline_type.height = 140.0, 100.0
			group_input_004.width, group_input_004.height = 140.0, 100.0
			mesh_to_curve.width, mesh_to_curve.height = 140.0, 100.0
			set_spline_resolution.width, set_spline_resolution.height = 140.0, 100.0
			store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
			store_named_attribute_007.width, store_named_attribute_007.height = 140.0, 100.0
			store_named_attribute_008.width, store_named_attribute_008.height = 140.0, 100.0
			store_named_attribute_009.width, store_named_attribute_009.height = 140.0, 100.0
			store_named_attribute_010.width, store_named_attribute_010.height = 140.0, 100.0
			combine_xyz.width, combine_xyz.height = 140.0, 100.0
			math_2.width, math_2.height = 140.0, 100.0
			cylinder.width, cylinder.height = 140.0, 100.0
			value.width, value.height = 140.0, 100.0
			group_input_005.width, group_input_005.height = 140.0, 100.0
			store_named_attribute_006.width, store_named_attribute_006.height = 140.0, 100.0
			position_001.width, position_001.height = 140.0, 100.0
			store_named_attribute_005.width, store_named_attribute_005.height = 140.0, 100.0
			separate_geometry.width, separate_geometry.height = 140.0, 100.0
			group_input_12.width, group_input_12.height = 140.0, 100.0
			group_004.width, group_004.height = 176.54052734375, 100.0
			reroute_006.width, reroute_006.height = 16.0, 100.0
			reroute_011.width, reroute_011.height = 16.0, 100.0
			group_006.width, group_006.height = 223.4932861328125, 100.0
			transform.width, transform.height = 140.0, 100.0
			instance_on_points.width, instance_on_points.height = 140.0, 100.0
			group_003.width, group_003.height = 219.859375, 100.0
			combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
			vector_math_003.width, vector_math_003.height = 140.0, 100.0
			vector_math_001.width, vector_math_001.height = 140.0, 100.0
			align_euler_to_vector_001.width, align_euler_to_vector_001.height = 140.0, 100.0
			align_euler_to_vector.width, align_euler_to_vector.height = 140.0, 100.0
			named_attribute_007.width, named_attribute_007.height = 179.014892578125, 100.0
			named_attribute_008.width, named_attribute_008.height = 180.2340087890625, 100.0
			capture_attribute_001.width, capture_attribute_001.height = 140.0, 100.0
			index_1.width, index_1.height = 140.0, 100.0
			named_attribute_009_1.width, named_attribute_009_1.height = 140.0, 100.0
			sample_index_002.width, sample_index_002.height = 140.0, 100.0
			reroute_004.width, reroute_004.height = 16.0, 100.0
			set_shade_smooth.width, set_shade_smooth.height = 140.0, 100.0
			reroute_007.width, reroute_007.height = 16.0, 100.0
			curve_circle.width, curve_circle.height = 140.0, 100.0
			group_input_003.width, group_input_003.height = 140.0, 100.0
			set_material.width, set_material.height = 140.0, 100.0
			reroute_005.width, reroute_005.height = 16.0, 100.0
			reroute_008.width, reroute_008.height = 16.0, 100.0
			curve_to_mesh.width, curve_to_mesh.height = 140.0, 100.0
			set_curve_radius.width, set_curve_radius.height = 140.0, 100.0
			group_input_002.width, group_input_002.height = 140.0, 100.0
			join_geometry_001.width, join_geometry_001.height = 140.0, 100.0
			reroute_013.width, reroute_013.height = 16.0, 100.0
			store_named_attribute_011.width, store_named_attribute_011.height = 140.0, 100.0
			switch_001_1.width, switch_001_1.height = 140.0, 100.0
			group_input_001.width, group_input_001.height = 140.0, 100.0
			group_4.width, group_4.height = 140.0, 100.0
			is_nucleic_1.width, is_nucleic_1.height = 180.0, 100.0
			group_005.width, group_005.height = 219.859375, 100.0
			reroute_1.width, reroute_1.height = 16.0, 100.0
			mix.width, mix.height = 140.0, 100.0
			
			#initialize _mn_utils_style_ribbon_nucleic links
			#mesh_line.Mesh -> set_position.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(mesh_line.outputs[0], set_position.inputs[0])
			#reroute_012.Output -> domain_size.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_012.outputs[0], domain_size.inputs[0])
			#domain_size.Point Count -> mesh_line.Count
			_mn_utils_style_ribbon_nucleic.links.new(domain_size.outputs[0], mesh_line.inputs[0])
			#set_position.Geometry -> delete_geometry.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(set_position.outputs[0], delete_geometry.inputs[0])
			#named_attribute_002_1.Attribute -> sample_index.Value
			_mn_utils_style_ribbon_nucleic.links.new(named_attribute_002_1.outputs[0], sample_index.inputs[1])
			#edge_vertices.Vertex Index 1 -> field_at_index.Index
			_mn_utils_style_ribbon_nucleic.links.new(edge_vertices.outputs[0], field_at_index.inputs[0])
			#reroute_002_2.Output -> field_at_index.Value
			_mn_utils_style_ribbon_nucleic.links.new(reroute_002_2.outputs[0], field_at_index.inputs[1])
			#reroute_002_2.Output -> field_at_index_001.Value
			_mn_utils_style_ribbon_nucleic.links.new(reroute_002_2.outputs[0], field_at_index_001.inputs[1])
			#edge_vertices.Vertex Index 2 -> field_at_index_001.Index
			_mn_utils_style_ribbon_nucleic.links.new(edge_vertices.outputs[1], field_at_index_001.inputs[0])
			#field_at_index.Value -> compare_2.A
			_mn_utils_style_ribbon_nucleic.links.new(field_at_index.outputs[0], compare_2.inputs[2])
			#field_at_index_001.Value -> compare_2.B
			_mn_utils_style_ribbon_nucleic.links.new(field_at_index_001.outputs[0], compare_2.inputs[3])
			#edge_vertices.Position 1 -> vector_math.Vector
			_mn_utils_style_ribbon_nucleic.links.new(edge_vertices.outputs[2], vector_math.inputs[0])
			#edge_vertices.Position 2 -> vector_math.Vector
			_mn_utils_style_ribbon_nucleic.links.new(edge_vertices.outputs[3], vector_math.inputs[1])
			#compare_2.Result -> boolean_math_2.Boolean
			_mn_utils_style_ribbon_nucleic.links.new(compare_2.outputs[0], boolean_math_2.inputs[0])
			#boolean_math_2.Boolean -> delete_geometry.Selection
			_mn_utils_style_ribbon_nucleic.links.new(boolean_math_2.outputs[0], delete_geometry.inputs[1])
			#vector_math.Value -> compare_001_2.A
			_mn_utils_style_ribbon_nucleic.links.new(vector_math.outputs[1], compare_001_2.inputs[0])
			#compare_001_2.Result -> boolean_math_2.Boolean
			_mn_utils_style_ribbon_nucleic.links.new(compare_001_2.outputs[0], boolean_math_2.inputs[1])
			#store_named_attribute_007.Geometry -> mesh_to_curve.Mesh
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_007.outputs[0], mesh_to_curve.inputs[0])
			#mesh_to_curve.Curve -> set_spline_type.Curve
			_mn_utils_style_ribbon_nucleic.links.new(mesh_to_curve.outputs[0], set_spline_type.inputs[0])
			#set_handle_type.Curve -> set_spline_resolution.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(set_handle_type.outputs[0], set_spline_resolution.inputs[0])
			#curve_circle.Curve -> curve_to_mesh.Profile Curve
			_mn_utils_style_ribbon_nucleic.links.new(curve_circle.outputs[0], curve_to_mesh.inputs[1])
			#reroute_001_2.Output -> sample_index_001.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_001_2.outputs[0], sample_index_001.inputs[0])
			#named_attribute_4.Attribute -> sample_index_001.Value
			_mn_utils_style_ribbon_nucleic.links.new(named_attribute_4.outputs[0], sample_index_001.inputs[1])
			#join_geometry_001.Geometry -> set_material.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(join_geometry_001.outputs[0], set_material.inputs[0])
			#group_input_002.Material -> set_material.Material
			_mn_utils_style_ribbon_nucleic.links.new(group_input_002.outputs[2], set_material.inputs[2])
			#set_spline_type.Curve -> set_handle_type.Curve
			_mn_utils_style_ribbon_nucleic.links.new(set_spline_type.outputs[0], set_handle_type.inputs[0])
			#reroute_003_1.Output -> sample_index_001.Index
			_mn_utils_style_ribbon_nucleic.links.new(reroute_003_1.outputs[0], sample_index_001.inputs[2])
			#set_spline_resolution.Geometry -> store_named_attribute.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(set_spline_resolution.outputs[0], store_named_attribute.inputs[0])
			#sample_index_001.Value -> store_named_attribute.Value
			_mn_utils_style_ribbon_nucleic.links.new(sample_index_001.outputs[0], store_named_attribute.inputs[3])
			#store_named_attribute.Geometry -> store_named_attribute_001.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute.outputs[0], store_named_attribute_001.inputs[0])
			#store_named_attribute_001.Geometry -> store_named_attribute_002.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_001.outputs[0], store_named_attribute_002.inputs[0])
			#store_named_attribute_002.Geometry -> store_named_attribute_003.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_002.outputs[0], store_named_attribute_003.inputs[0])
			#sample_index.Value -> store_named_attribute_001.Value
			_mn_utils_style_ribbon_nucleic.links.new(sample_index.outputs[0], store_named_attribute_001.inputs[3])
			#reroute_001_2.Output -> sample_index_003.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_001_2.outputs[0], sample_index_003.inputs[0])
			#named_attribute_003.Attribute -> sample_index_003.Value
			_mn_utils_style_ribbon_nucleic.links.new(named_attribute_003.outputs[0], sample_index_003.inputs[1])
			#reroute_003_1.Output -> sample_index_003.Index
			_mn_utils_style_ribbon_nucleic.links.new(reroute_003_1.outputs[0], sample_index_003.inputs[2])
			#sample_index_003.Value -> store_named_attribute_003.Value
			_mn_utils_style_ribbon_nucleic.links.new(sample_index_003.outputs[0], store_named_attribute_003.inputs[3])
			#reroute_001_2.Output -> sample_index_004.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_001_2.outputs[0], sample_index_004.inputs[0])
			#named_attribute_004.Attribute -> sample_index_004.Value
			_mn_utils_style_ribbon_nucleic.links.new(named_attribute_004.outputs[0], sample_index_004.inputs[1])
			#reroute_003_1.Output -> sample_index_004.Index
			_mn_utils_style_ribbon_nucleic.links.new(reroute_003_1.outputs[0], sample_index_004.inputs[2])
			#sample_index_004.Value -> store_named_attribute_002.Value
			_mn_utils_style_ribbon_nucleic.links.new(sample_index_004.outputs[0], store_named_attribute_002.inputs[3])
			#reroute_010.Output -> reroute_001_2.Input
			_mn_utils_style_ribbon_nucleic.links.new(reroute_010.outputs[0], reroute_001_2.inputs[0])
			#index_003.Index -> reroute_003_1.Input
			_mn_utils_style_ribbon_nucleic.links.new(index_003.outputs[0], reroute_003_1.inputs[0])
			#reroute_003_1.Output -> sample_index.Index
			_mn_utils_style_ribbon_nucleic.links.new(reroute_003_1.outputs[0], sample_index.inputs[2])
			#store_named_attribute_003.Geometry -> store_named_attribute_004.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_003.outputs[0], store_named_attribute_004.inputs[0])
			#reroute_001_2.Output -> sample_index_005.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_001_2.outputs[0], sample_index_005.inputs[0])
			#reroute_003_1.Output -> sample_index_005.Index
			_mn_utils_style_ribbon_nucleic.links.new(reroute_003_1.outputs[0], sample_index_005.inputs[2])
			#named_attribute_005.Attribute -> sample_index_005.Value
			_mn_utils_style_ribbon_nucleic.links.new(named_attribute_005.outputs[0], sample_index_005.inputs[1])
			#sample_index_005.Value -> store_named_attribute_004.Value
			_mn_utils_style_ribbon_nucleic.links.new(sample_index_005.outputs[0], store_named_attribute_004.inputs[3])
			#store_named_attribute_004.Geometry -> capture_attribute.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_004.outputs[0], capture_attribute.inputs[0])
			#capture_attribute.Geometry -> set_curve_radius.Curve
			_mn_utils_style_ribbon_nucleic.links.new(capture_attribute.outputs[0], set_curve_radius.inputs[0])
			#reroute_007.Output -> set_shade_smooth.Shade Smooth
			_mn_utils_style_ribbon_nucleic.links.new(reroute_007.outputs[0], set_shade_smooth.inputs[2])
			#capture_attribute.Value -> reroute_004.Input
			_mn_utils_style_ribbon_nucleic.links.new(capture_attribute.outputs[1], reroute_004.inputs[0])
			#reroute_004.Output -> reroute_007.Input
			_mn_utils_style_ribbon_nucleic.links.new(reroute_004.outputs[0], reroute_007.inputs[0])
			#reroute_001_2.Output -> sample_index.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_001_2.outputs[0], sample_index.inputs[0])
			#named_attribute_006.Attribute -> sample_index_008.Value
			_mn_utils_style_ribbon_nucleic.links.new(named_attribute_006.outputs[0], sample_index_008.inputs[1])
			#reroute_009.Output -> sample_index_008.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_009.outputs[0], sample_index_008.inputs[0])
			#index_004.Index -> sample_index_008.Index
			_mn_utils_style_ribbon_nucleic.links.new(index_004.outputs[0], sample_index_008.inputs[2])
			#sample_index_008.Value -> reroute_002_2.Input
			_mn_utils_style_ribbon_nucleic.links.new(sample_index_008.outputs[0], reroute_002_2.inputs[0])
			#reroute_012.Output -> reroute_009.Input
			_mn_utils_style_ribbon_nucleic.links.new(reroute_012.outputs[0], reroute_009.inputs[0])
			#reroute_012.Output -> reroute_010.Input
			_mn_utils_style_ribbon_nucleic.links.new(reroute_012.outputs[0], reroute_010.inputs[0])
			#curve_to_mesh.Mesh -> set_shade_smooth.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(curve_to_mesh.outputs[0], set_shade_smooth.inputs[0])
			#group_003.Atoms -> reroute_012.Input
			_mn_utils_style_ribbon_nucleic.links.new(group_003.outputs[0], reroute_012.inputs[0])
			#store_named_attribute_006.Geometry -> transform.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_006.outputs[0], transform.inputs[0])
			#combine_xyz.Vector -> transform.Translation
			_mn_utils_style_ribbon_nucleic.links.new(combine_xyz.outputs[0], transform.inputs[1])
			#value.Value -> math_2.Value
			_mn_utils_style_ribbon_nucleic.links.new(value.outputs[0], math_2.inputs[0])
			#value.Value -> cylinder.Depth
			_mn_utils_style_ribbon_nucleic.links.new(value.outputs[0], cylinder.inputs[4])
			#math_2.Value -> combine_xyz.Z
			_mn_utils_style_ribbon_nucleic.links.new(math_2.outputs[0], combine_xyz.inputs[2])
			#align_euler_to_vector_001.Rotation -> instance_on_points.Rotation
			_mn_utils_style_ribbon_nucleic.links.new(align_euler_to_vector_001.outputs[0], instance_on_points.inputs[5])
			#combine_xyz_001.Vector -> instance_on_points.Scale
			_mn_utils_style_ribbon_nucleic.links.new(combine_xyz_001.outputs[0], instance_on_points.inputs[6])
			#set_material.Geometry -> group_output_12.Ribbon + Bases
			_mn_utils_style_ribbon_nucleic.links.new(set_material.outputs[0], group_output_12.inputs[0])
			#store_named_attribute_005.Geometry -> instance_on_points.Points
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_005.outputs[0], instance_on_points.inputs[0])
			#reroute_013.Output -> join_geometry_001.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_013.outputs[0], join_geometry_001.inputs[0])
			#group_input_005.Base Radius -> cylinder.Radius
			_mn_utils_style_ribbon_nucleic.links.new(group_input_005.outputs[8], cylinder.inputs[3])
			#group_input_005.Base Resolution -> cylinder.Vertices
			_mn_utils_style_ribbon_nucleic.links.new(group_input_005.outputs[9], cylinder.inputs[0])
			#reroute_005.Output -> group_output_12.Ribbon Curve
			_mn_utils_style_ribbon_nucleic.links.new(reroute_005.outputs[0], group_output_12.inputs[1])
			#transform.Geometry -> instance_on_points.Instance
			_mn_utils_style_ribbon_nucleic.links.new(transform.outputs[0], instance_on_points.inputs[2])
			#cylinder.Mesh -> store_named_attribute_006.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(cylinder.outputs[0], store_named_attribute_006.inputs[0])
			#cylinder.UV Map -> store_named_attribute_006.Value
			_mn_utils_style_ribbon_nucleic.links.new(cylinder.outputs[4], store_named_attribute_006.inputs[3])
			#group_input_12.Atoms -> separate_geometry.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(group_input_12.outputs[0], separate_geometry.inputs[0])
			#reroute_1.Output -> group_003.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_1.outputs[0], group_003.inputs[0])
			#group_004.Value -> store_named_attribute_005.Value
			_mn_utils_style_ribbon_nucleic.links.new(group_004.outputs[2], store_named_attribute_005.inputs[3])
			#group_input_003.Backbone Resolution -> curve_circle.Resolution
			_mn_utils_style_ribbon_nucleic.links.new(group_input_003.outputs[5], curve_circle.inputs[0])
			#position_001.Position -> vector_math_001.Vector
			_mn_utils_style_ribbon_nucleic.links.new(position_001.outputs[0], vector_math_001.inputs[1])
			#set_curve_radius.Curve -> set_position_001.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(set_curve_radius.outputs[0], set_position_001.inputs[0])
			#position_002_1.Position -> evaluate_at_index_1.Value
			_mn_utils_style_ribbon_nucleic.links.new(position_002_1.outputs[0], evaluate_at_index_1.inputs[1])
			#offset_point_in_curve.Point Index -> evaluate_at_index_1.Index
			_mn_utils_style_ribbon_nucleic.links.new(offset_point_in_curve.outputs[1], evaluate_at_index_1.inputs[0])
			#evaluate_at_index_1.Value -> vector_math_002_1.Vector
			_mn_utils_style_ribbon_nucleic.links.new(evaluate_at_index_1.outputs[0], vector_math_002_1.inputs[0])
			#position_002_1.Position -> vector_math_002_1.Vector
			_mn_utils_style_ribbon_nucleic.links.new(position_002_1.outputs[0], vector_math_002_1.inputs[1])
			#vector_math_002_1.Vector -> vector_math_004_1.Vector
			_mn_utils_style_ribbon_nucleic.links.new(vector_math_002_1.outputs[0], vector_math_004_1.inputs[0])
			#vector_math_004_1.Vector -> set_position_001.Offset
			_mn_utils_style_ribbon_nucleic.links.new(vector_math_004_1.outputs[0], set_position_001.inputs[3])
			#endpoint_selection.Selection -> set_position_001.Selection
			_mn_utils_style_ribbon_nucleic.links.new(endpoint_selection.outputs[0], set_position_001.inputs[1])
			#endpoint_selection_001.Selection -> switch_3.Switch
			_mn_utils_style_ribbon_nucleic.links.new(endpoint_selection_001.outputs[0], switch_3.inputs[0])
			#switch_3.Output -> offset_point_in_curve.Offset
			_mn_utils_style_ribbon_nucleic.links.new(switch_3.outputs[0], offset_point_in_curve.inputs[1])
			#store_named_attribute_007.Geometry -> store_named_attribute_005.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_007.outputs[0], store_named_attribute_005.inputs[0])
			#group_input_004.Backbone Subdivisions -> set_spline_resolution.Resolution
			_mn_utils_style_ribbon_nucleic.links.new(group_input_004.outputs[4], set_spline_resolution.inputs[2])
			#reroute_001_2.Output -> sample_index_009_1.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_001_2.outputs[0], sample_index_009_1.inputs[0])
			#reroute_003_1.Output -> sample_index_009_1.Index
			_mn_utils_style_ribbon_nucleic.links.new(reroute_003_1.outputs[0], sample_index_009_1.inputs[2])
			#group_input_006.Backbone Shade Smooth -> sample_index_009_1.Value
			_mn_utils_style_ribbon_nucleic.links.new(group_input_006.outputs[7], sample_index_009_1.inputs[1])
			#sample_index_009_1.Value -> capture_attribute.Value
			_mn_utils_style_ribbon_nucleic.links.new(sample_index_009_1.outputs[0], capture_attribute.inputs[1])
			#group_input_006.Backbone Radius -> sample_index_007.Value
			_mn_utils_style_ribbon_nucleic.links.new(group_input_006.outputs[6], sample_index_007.inputs[1])
			#reroute_003_1.Output -> sample_index_007.Index
			_mn_utils_style_ribbon_nucleic.links.new(reroute_003_1.outputs[0], sample_index_007.inputs[2])
			#reroute_001_2.Output -> sample_index_007.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_001_2.outputs[0], sample_index_007.inputs[0])
			#sample_index_007.Value -> set_curve_radius.Radius
			_mn_utils_style_ribbon_nucleic.links.new(sample_index_007.outputs[0], set_curve_radius.inputs[2])
			#reroute_008.Output -> reroute_005.Input
			_mn_utils_style_ribbon_nucleic.links.new(reroute_008.outputs[0], reroute_005.inputs[0])
			#set_curve_radius.Curve -> reroute_008.Input
			_mn_utils_style_ribbon_nucleic.links.new(set_curve_radius.outputs[0], reroute_008.inputs[0])
			#store_named_attribute_008.Geometry -> store_named_attribute_007.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_008.outputs[0], store_named_attribute_007.inputs[0])
			#reroute_006.Output -> group_006.Input
			_mn_utils_style_ribbon_nucleic.links.new(reroute_006.outputs[0], group_006.inputs[0])
			#store_named_attribute_009.Geometry -> store_named_attribute_008.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_009.outputs[0], store_named_attribute_008.inputs[0])
			#group_006.Align Vertical -> store_named_attribute_008.Value
			_mn_utils_style_ribbon_nucleic.links.new(group_006.outputs[2], store_named_attribute_008.inputs[3])
			#group_006.Align Horizontal -> store_named_attribute_007.Value
			_mn_utils_style_ribbon_nucleic.links.new(group_006.outputs[3], store_named_attribute_007.inputs[3])
			#vector_math_001.Vector -> vector_math_003.Vector
			_mn_utils_style_ribbon_nucleic.links.new(vector_math_001.outputs[0], vector_math_003.inputs[0])
			#vector_math_003.Value -> combine_xyz_001.Z
			_mn_utils_style_ribbon_nucleic.links.new(vector_math_003.outputs[1], combine_xyz_001.inputs[2])
			#store_named_attribute_010.Geometry -> store_named_attribute_009.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_010.outputs[0], store_named_attribute_009.inputs[0])
			#group_006.Base Interface -> store_named_attribute_009.Value
			_mn_utils_style_ribbon_nucleic.links.new(group_006.outputs[0], store_named_attribute_009.inputs[3])
			#delete_geometry.Geometry -> store_named_attribute_010.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(delete_geometry.outputs[0], store_named_attribute_010.inputs[0])
			#group_006.Base Pivot -> store_named_attribute_010.Value
			_mn_utils_style_ribbon_nucleic.links.new(group_006.outputs[1], store_named_attribute_010.inputs[3])
			#named_attribute_008.Attribute -> vector_math_001.Vector
			_mn_utils_style_ribbon_nucleic.links.new(named_attribute_008.outputs[0], vector_math_001.inputs[0])
			#separate_geometry.Selection -> reroute_006.Input
			_mn_utils_style_ribbon_nucleic.links.new(separate_geometry.outputs[0], reroute_006.inputs[0])
			#reroute_011.Output -> group_004.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_011.outputs[0], group_004.inputs[0])
			#reroute_006.Output -> reroute_011.Input
			_mn_utils_style_ribbon_nucleic.links.new(reroute_006.outputs[0], reroute_011.inputs[0])
			#align_euler_to_vector.Rotation -> align_euler_to_vector_001.Rotation
			_mn_utils_style_ribbon_nucleic.links.new(align_euler_to_vector.outputs[0], align_euler_to_vector_001.inputs[0])
			#vector_math_001.Vector -> align_euler_to_vector.Vector
			_mn_utils_style_ribbon_nucleic.links.new(vector_math_001.outputs[0], align_euler_to_vector.inputs[2])
			#named_attribute_007.Attribute -> align_euler_to_vector_001.Vector
			_mn_utils_style_ribbon_nucleic.links.new(named_attribute_007.outputs[0], align_euler_to_vector_001.inputs[2])
			#set_position_001.Geometry -> capture_attribute_001.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(set_position_001.outputs[0], capture_attribute_001.inputs[0])
			#index_1.Index -> capture_attribute_001.Value
			_mn_utils_style_ribbon_nucleic.links.new(index_1.outputs[0], capture_attribute_001.inputs[1])
			#capture_attribute_001.Geometry -> curve_to_mesh.Curve
			_mn_utils_style_ribbon_nucleic.links.new(capture_attribute_001.outputs[0], curve_to_mesh.inputs[0])
			#set_shade_smooth.Geometry -> store_named_attribute_011.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(set_shade_smooth.outputs[0], store_named_attribute_011.inputs[0])
			#capture_attribute_001.Value -> sample_index_002.Index
			_mn_utils_style_ribbon_nucleic.links.new(capture_attribute_001.outputs[1], sample_index_002.inputs[2])
			#capture_attribute_001.Geometry -> sample_index_002.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(capture_attribute_001.outputs[0], sample_index_002.inputs[0])
			#named_attribute_009_1.Attribute -> sample_index_002.Value
			_mn_utils_style_ribbon_nucleic.links.new(named_attribute_009_1.outputs[0], sample_index_002.inputs[1])
			#sample_index_002.Value -> store_named_attribute_011.Value
			_mn_utils_style_ribbon_nucleic.links.new(sample_index_002.outputs[0], store_named_attribute_011.inputs[3])
			#store_named_attribute_011.Geometry -> switch_001_1.False
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_011.outputs[0], switch_001_1.inputs[1])
			#set_shade_smooth.Geometry -> switch_001_1.True
			_mn_utils_style_ribbon_nucleic.links.new(set_shade_smooth.outputs[0], switch_001_1.inputs[2])
			#switch_001_1.Output -> reroute_013.Input
			_mn_utils_style_ribbon_nucleic.links.new(switch_001_1.outputs[0], reroute_013.inputs[0])
			#group_input_001.Intepolate Color -> switch_001_1.Switch
			_mn_utils_style_ribbon_nucleic.links.new(group_input_001.outputs[3], switch_001_1.inputs[0])
			#group_input_12.Selection -> is_nucleic_1.And
			_mn_utils_style_ribbon_nucleic.links.new(group_input_12.outputs[1], is_nucleic_1.inputs[0])
			#is_nucleic_1.Selection -> separate_geometry.Selection
			_mn_utils_style_ribbon_nucleic.links.new(is_nucleic_1.outputs[0], separate_geometry.inputs[1])
			#reroute_1.Output -> group_005.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_1.outputs[0], group_005.inputs[0])
			#separate_geometry.Selection -> reroute_1.Input
			_mn_utils_style_ribbon_nucleic.links.new(separate_geometry.outputs[0], reroute_1.inputs[0])
			#group_003.Value -> mix.A
			_mn_utils_style_ribbon_nucleic.links.new(group_003.outputs[1], mix.inputs[4])
			#group_005.Value -> mix.B
			_mn_utils_style_ribbon_nucleic.links.new(group_005.outputs[1], mix.inputs[5])
			#mix.Result -> set_position.Position
			_mn_utils_style_ribbon_nucleic.links.new(mix.outputs[1], set_position.inputs[2])
			#instance_on_points.Instances -> join_geometry_001.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(instance_on_points.outputs[0], join_geometry_001.inputs[0])
			return _mn_utils_style_ribbon_nucleic

		_mn_utils_style_ribbon_nucleic = _mn_utils_style_ribbon_nucleic_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".MN_utils_style_ribbon_nucleic", type = 'NODES')
		mod.node_group = _mn_utils_style_ribbon_nucleic
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_MN_utils_style_ribbon_nucleic.bl_idname)
			
def register():
	bpy.utils.register_class(_MN_utils_style_ribbon_nucleic)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_MN_utils_style_ribbon_nucleic)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
