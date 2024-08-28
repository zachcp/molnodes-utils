bl_info = {
	"name" : ".Base align",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _Base_align(bpy.types.Operator):
	bl_idname = "node._base_align"
	bl_label = ".Base align"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
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
			group_input = mn_select_nucleic_type.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
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
			group_output = mn_select_nucleic_type.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
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
			group_input.location = (-570.0, 0.0)
			reroute_015.location = (-150.0, -97.31201171875)
			named_attribute_010.location = (-420.0, -60.0)
			compare_007.location = (-30.0, -90.0)
			compare_016.location = (-30.0, -250.0)
			compare_008.location = (-30.0, 249.9998779296875)
			compare_015.location = (-30.0, 89.9998779296875)
			boolean_math_012.location = (170.0, 249.9998779296875)
			boolean_math_013.location = (150.0, -90.0)
			boolean_math_007.location = (370.0, 249.9998779296875)
			group_output.location = (580.0, 240.0)
			compare_017.location = (-40.0, -940.0)
			compare_010.location = (-40.0, -440.0)
			compare_018.location = (-40.0, -600.0)
			boolean_math_014.location = (160.0, -440.0)
			boolean_math_015.location = (140.0, -780.0)
			compare_009.location = (-40.0, -780.0)
			boolean_math_008.location = (360.0, -440.0)
			
			#Set dimensions
			group_input.width, group_input.height = 140.0, 100.0
			reroute_015.width, reroute_015.height = 16.0, 100.0
			named_attribute_010.width, named_attribute_010.height = 206.99917602539062, 100.0
			compare_007.width, compare_007.height = 140.0, 100.0
			compare_016.width, compare_016.height = 140.0, 100.0
			compare_008.width, compare_008.height = 140.0, 100.0
			compare_015.width, compare_015.height = 140.0, 100.0
			boolean_math_012.width, boolean_math_012.height = 140.0, 100.0
			boolean_math_013.width, boolean_math_013.height = 140.0, 100.0
			boolean_math_007.width, boolean_math_007.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
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
			#boolean_math_007.Boolean -> group_output.is_pyrimidine
			mn_select_nucleic_type.links.new(boolean_math_007.outputs[0], group_output.inputs[1])
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
			#boolean_math_008.Boolean -> group_output.is_purine
			mn_select_nucleic_type.links.new(boolean_math_008.outputs[0], group_output.inputs[0])
			return mn_select_nucleic_type

		mn_select_nucleic_type = mn_select_nucleic_type_node_group()

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
			group_output_1 = _sampleatomvalue.nodes.new("NodeGroupOutput")
			group_output_1.name = "Group Output"
			group_output_1.is_active_output = True
			
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
			group_input_1 = _sampleatomvalue.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			
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
			group_output_1.location = (390.0, 0.0)
			named_attribute_009.location = (-200.0, -107.52880859375)
			index_005.location = (40.0, -47.52880859375)
			position_002.location = (40.0, 12.47119140625)
			compare_003.location = (40.2109375, -112.47119140625)
			group_input_1.location = (-170.3642578125, -265.140380859375)
			sample_index_009.location = (200.0, 112.47119140625)
			named_attribute.location = (40.0, -380.0)
			sample_index_010.location = (200.0, -280.0)
			separate_geometry_002.location = (200.0, -107.52880859375)
			
			#Set dimensions
			group_output_1.width, group_output_1.height = 140.0, 100.0
			named_attribute_009.width, named_attribute_009.height = 206.99917602539062, 100.0
			index_005.width, index_005.height = 140.0, 100.0
			position_002.width, position_002.height = 140.0, 100.0
			compare_003.width, compare_003.height = 140.0, 100.0
			group_input_1.width, group_input_1.height = 140.0, 100.0
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
			#group_input_1.Geometry -> separate_geometry_002.Geometry
			_sampleatomvalue.links.new(group_input_1.outputs[0], separate_geometry_002.inputs[0])
			#group_input_1.B -> compare_003.B
			_sampleatomvalue.links.new(group_input_1.outputs[1], compare_003.inputs[3])
			#sample_index_009.Value -> group_output_1.Value
			_sampleatomvalue.links.new(sample_index_009.outputs[0], group_output_1.inputs[1])
			#index_005.Index -> sample_index_010.Index
			_sampleatomvalue.links.new(index_005.outputs[0], sample_index_010.inputs[2])
			#separate_geometry_002.Selection -> sample_index_010.Geometry
			_sampleatomvalue.links.new(separate_geometry_002.outputs[0], sample_index_010.inputs[0])
			#named_attribute.Attribute -> sample_index_010.Value
			_sampleatomvalue.links.new(named_attribute.outputs[0], sample_index_010.inputs[1])
			#sample_index_010.Value -> group_output_1.Value
			_sampleatomvalue.links.new(sample_index_010.outputs[0], group_output_1.inputs[2])
			#separate_geometry_002.Selection -> group_output_1.Atoms
			_sampleatomvalue.links.new(separate_geometry_002.outputs[0], group_output_1.inputs[0])
			return _sampleatomvalue

		_sampleatomvalue = _sampleatomvalue_node_group()

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

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".Base align", type = 'NODES')
		mod.node_group = _base_align
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_Base_align.bl_idname)
			
def register():
	bpy.utils.register_class(_Base_align)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_Base_align)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
