bl_info = {
	"name" : "Select Cube",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Select_Cube(bpy.types.Operator):
	bl_idname = "node.select_cube"
	bl_label = "Select Cube"
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

		#initialize select_cube node group
		def select_cube_node_group():
			select_cube = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Select Cube")

			select_cube.color_tag = 'INPUT'
			select_cube.description = ""

			
			#select_cube interface
			#Socket Selection
			selection_socket = select_cube.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket.default_value = False
			selection_socket.attribute_domain = 'POINT'
			selection_socket.description = "The calculated selection"
			
			#Socket Inverted
			inverted_socket = select_cube.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket.default_value = False
			inverted_socket.attribute_domain = 'POINT'
			inverted_socket.description = "The inverse of the calculated selection"
			
			#Socket 0..1
			_0__1_socket = select_cube.interface.new_socket(name = "0..1", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			_0__1_socket.default_value = 0.0
			_0__1_socket.min_value = -3.4028234663852886e+38
			_0__1_socket.max_value = 3.4028234663852886e+38
			_0__1_socket.subtype = 'NONE'
			_0__1_socket.attribute_domain = 'POINT'
			_0__1_socket.description = "Falloff value from 0 to 1, based on the From Min and From Max."
			
			#Socket And
			and_socket = select_cube.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket.default_value = True
			and_socket.attribute_domain = 'POINT'
			and_socket.hide_value = True
			
			#Socket Or
			or_socket = select_cube.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket.default_value = False
			or_socket.attribute_domain = 'POINT'
			or_socket.hide_value = True
			
			#Socket Object
			object_socket = select_cube.interface.new_socket(name = "Object", in_out='INPUT', socket_type = 'NodeSocketObject')
			object_socket.attribute_domain = 'POINT'
			object_socket.description = "Empty object (ideally Cube) to use as the selection tool."
			
			#Socket From Min (A)
			from_min__a__socket = select_cube.interface.new_socket(name = "From Min (A)", in_out='INPUT', socket_type = 'NodeSocketFloat')
			from_min__a__socket.default_value = 0.0
			from_min__a__socket.min_value = 0.0
			from_min__a__socket.max_value = 10000.0
			from_min__a__socket.subtype = 'NONE'
			from_min__a__socket.attribute_domain = 'POINT'
			from_min__a__socket.description = "Minimum distance for falloff, in Angstroms."
			
			#Socket From Max (A)
			from_max__a__socket = select_cube.interface.new_socket(name = "From Max (A)", in_out='INPUT', socket_type = 'NodeSocketFloat')
			from_max__a__socket.default_value = 10.0
			from_max__a__socket.min_value = 0.0
			from_max__a__socket.max_value = 10000.0
			from_max__a__socket.subtype = 'NONE'
			from_max__a__socket.attribute_domain = 'POINT'
			from_max__a__socket.description = "Maximum distance for falloff, in Angstroms."
			
			
			#initialize select_cube nodes
			#node Vector Math.009
			vector_math_009 = select_cube.nodes.new("ShaderNodeVectorMath")
			vector_math_009.name = "Vector Math.009"
			vector_math_009.operation = 'SUBTRACT'
			
			#node Vector Math.007
			vector_math_007 = select_cube.nodes.new("ShaderNodeVectorMath")
			vector_math_007.name = "Vector Math.007"
			vector_math_007.operation = 'ADD'
			
			#node Vector Rotate.002
			vector_rotate_002 = select_cube.nodes.new("ShaderNodeVectorRotate")
			vector_rotate_002.name = "Vector Rotate.002"
			vector_rotate_002.invert = True
			vector_rotate_002.rotation_type = 'EULER_XYZ'
			
			#node Object Info
			object_info = select_cube.nodes.new("GeometryNodeObjectInfo")
			object_info.name = "Object Info"
			object_info.transform_space = 'RELATIVE'
			#As Instance
			object_info.inputs[1].default_value = True
			
			#node Position.002
			position_002 = select_cube.nodes.new("GeometryNodeInputPosition")
			position_002.name = "Position.002"
			
			#node Vector Math.008
			vector_math_008 = select_cube.nodes.new("ShaderNodeVectorMath")
			vector_math_008.name = "Vector Math.008"
			vector_math_008.operation = 'SUBTRACT'
			
			#node Vector Math.010
			vector_math_010 = select_cube.nodes.new("ShaderNodeVectorMath")
			vector_math_010.name = "Vector Math.010"
			vector_math_010.operation = 'SUBTRACT'
			
			#node Compare.004
			compare_004 = select_cube.nodes.new("FunctionNodeCompare")
			compare_004.name = "Compare.004"
			compare_004.data_type = 'VECTOR'
			compare_004.mode = 'ELEMENT'
			compare_004.operation = 'LESS_THAN'
			#B_VEC3
			compare_004.inputs[5].default_value = (0.0, 0.0, 0.0)
			
			#node Compare.003
			compare_003 = select_cube.nodes.new("FunctionNodeCompare")
			compare_003.name = "Compare.003"
			compare_003.data_type = 'VECTOR'
			compare_003.mode = 'ELEMENT'
			compare_003.operation = 'GREATER_THAN'
			#B_VEC3
			compare_003.inputs[5].default_value = (0.0, 0.0, 0.0)
			
			#node Vector Math.001
			vector_math_001 = select_cube.nodes.new("ShaderNodeVectorMath")
			vector_math_001.name = "Vector Math.001"
			vector_math_001.operation = 'ABSOLUTE'
			
			#node Vector Math
			vector_math = select_cube.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.operation = 'ABSOLUTE'
			
			#node Vector Math.003
			vector_math_003 = select_cube.nodes.new("ShaderNodeVectorMath")
			vector_math_003.name = "Vector Math.003"
			vector_math_003.operation = 'MINIMUM'
			
			#node Group Output
			group_output_2 = select_cube.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Group Input
			group_input_2 = select_cube.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			group_input_2.outputs[0].hide = True
			
			#node Boolean Math.006
			boolean_math_006 = select_cube.nodes.new("FunctionNodeBooleanMath")
			boolean_math_006.name = "Boolean Math.006"
			boolean_math_006.operation = 'AND'
			
			#node Boolean Math
			boolean_math = select_cube.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'NOT'
			
			#node Group.001
			group_001 = select_cube.nodes.new("GeometryNodeGroup")
			group_001.name = "Group.001"
			group_001.node_tree = mn_units
			
			#node Separate XYZ
			separate_xyz = select_cube.nodes.new("ShaderNodeSeparateXYZ")
			separate_xyz.name = "Separate XYZ"
			
			#node Math.001
			math_001_1 = select_cube.nodes.new("ShaderNodeMath")
			math_001_1.name = "Math.001"
			math_001_1.operation = 'MINIMUM'
			math_001_1.use_clamp = False
			
			#node Math
			math_1 = select_cube.nodes.new("ShaderNodeMath")
			math_1.name = "Math"
			math_1.operation = 'MINIMUM'
			math_1.use_clamp = False
			
			#node Group Input.001
			group_input_001 = select_cube.nodes.new("NodeGroupInput")
			group_input_001.name = "Group Input.001"
			group_input_001.outputs[0].hide = True
			
			#node Group
			group_1 = select_cube.nodes.new("GeometryNodeGroup")
			group_1.name = "Group"
			group_1.node_tree = mn_units
			
			#node Map Range
			map_range = select_cube.nodes.new("ShaderNodeMapRange")
			map_range.name = "Map Range"
			map_range.clamp = True
			map_range.data_type = 'FLOAT'
			map_range.interpolation_type = 'LINEAR'
			#To Min
			map_range.inputs[3].default_value = 0.0
			#To Max
			map_range.inputs[4].default_value = 1.0
			
			#node Vector Math.002
			vector_math_002 = select_cube.nodes.new("ShaderNodeVectorMath")
			vector_math_002.name = "Vector Math.002"
			vector_math_002.operation = 'ABSOLUTE'
			
			#node Reroute
			reroute = select_cube.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Boolean Math.007
			boolean_math_007 = select_cube.nodes.new("FunctionNodeBooleanMath")
			boolean_math_007.name = "Boolean Math.007"
			boolean_math_007.operation = 'AND'
			
			#node Group Input.002
			group_input_002 = select_cube.nodes.new("NodeGroupInput")
			group_input_002.name = "Group Input.002"
			
			#node Boolean Math.008
			boolean_math_008 = select_cube.nodes.new("FunctionNodeBooleanMath")
			boolean_math_008.name = "Boolean Math.008"
			boolean_math_008.operation = 'OR'
			
			
			
			
			#Set locations
			vector_math_009.location = (-498.0, -100.0)
			vector_math_007.location = (-498.0, 40.0)
			vector_rotate_002.location = (-498.0, -240.0)
			object_info.location = (-678.0001220703125, 40.0)
			position_002.location = (-678.0001220703125, -160.0)
			vector_math_008.location = (-338.0, 40.0)
			vector_math_010.location = (-338.0, -100.0)
			compare_004.location = (81.99999237060547, -120.0)
			compare_003.location = (81.99999237060547, 140.0)
			vector_math_001.location = (-60.0, -540.0)
			vector_math.location = (-60.0, -420.0)
			vector_math_003.location = (100.0, -420.0)
			group_output_2.location = (1066.5135498046875, 100.90254211425781)
			group_input_2.location = (-838.0001220703125, 40.0)
			boolean_math_006.location = (252.00001525878906, 140.0)
			boolean_math.location = (827.9999389648438, 80.0)
			group_001.location = (600.0, -600.0)
			separate_xyz.location = (260.0, -420.0)
			math_001_1.location = (600.0, -300.0)
			math_1.location = (440.0, -300.0)
			group_input_001.location = (420.0, -580.0)
			group_1.location = (600.0, -460.0)
			map_range.location = (760.0, -300.0)
			vector_math_002.location = (-498.0, 160.0)
			reroute.location = (787.9999389648438, 100.0)
			boolean_math_007.location = (420.0, 160.0)
			group_input_002.location = (240.0, 320.0)
			boolean_math_008.location = (599.9999389648438, 174.85726928710938)
			
			#Set dimensions
			vector_math_009.width, vector_math_009.height = 140.0, 100.0
			vector_math_007.width, vector_math_007.height = 140.0, 100.0
			vector_rotate_002.width, vector_rotate_002.height = 140.0, 100.0
			object_info.width, object_info.height = 140.0, 100.0
			position_002.width, position_002.height = 140.0, 100.0
			vector_math_008.width, vector_math_008.height = 140.0, 100.0
			vector_math_010.width, vector_math_010.height = 140.0, 100.0
			compare_004.width, compare_004.height = 140.0, 100.0
			compare_003.width, compare_003.height = 140.0, 100.0
			vector_math_001.width, vector_math_001.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			vector_math_003.width, vector_math_003.height = 140.0, 100.0
			group_output_2.width, group_output_2.height = 140.0, 100.0
			group_input_2.width, group_input_2.height = 140.0, 100.0
			boolean_math_006.width, boolean_math_006.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			group_001.width, group_001.height = 140.0, 100.0
			separate_xyz.width, separate_xyz.height = 140.0, 100.0
			math_001_1.width, math_001_1.height = 140.0, 100.0
			math_1.width, math_1.height = 140.0, 100.0
			group_input_001.width, group_input_001.height = 140.0, 100.0
			group_1.width, group_1.height = 140.0, 100.0
			map_range.width, map_range.height = 140.0, 100.0
			vector_math_002.width, vector_math_002.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			boolean_math_007.width, boolean_math_007.height = 140.0, 100.0
			group_input_002.width, group_input_002.height = 140.0, 100.0
			boolean_math_008.width, boolean_math_008.height = 140.0, 100.0
			
			#initialize select_cube links
			#vector_math_009.Vector -> vector_math_010.Vector
			select_cube.links.new(vector_math_009.outputs[0], vector_math_010.inputs[0])
			#vector_math_002.Vector -> vector_math_007.Vector
			select_cube.links.new(vector_math_002.outputs[0], vector_math_007.inputs[1])
			#vector_rotate_002.Vector -> vector_math_010.Vector
			select_cube.links.new(vector_rotate_002.outputs[0], vector_math_010.inputs[1])
			#object_info.Location -> vector_math_007.Vector
			select_cube.links.new(object_info.outputs[1], vector_math_007.inputs[0])
			#object_info.Rotation -> vector_rotate_002.Rotation
			select_cube.links.new(object_info.outputs[2], vector_rotate_002.inputs[4])
			#vector_rotate_002.Vector -> vector_math_008.Vector
			select_cube.links.new(vector_rotate_002.outputs[0], vector_math_008.inputs[1])
			#vector_math_008.Vector -> compare_003.A
			select_cube.links.new(vector_math_008.outputs[0], compare_003.inputs[4])
			#vector_math_010.Vector -> compare_004.A
			select_cube.links.new(vector_math_010.outputs[0], compare_004.inputs[4])
			#vector_math_002.Vector -> vector_math_009.Vector
			select_cube.links.new(vector_math_002.outputs[0], vector_math_009.inputs[1])
			#object_info.Location -> vector_math_009.Vector
			select_cube.links.new(object_info.outputs[1], vector_math_009.inputs[0])
			#compare_004.Result -> boolean_math_006.Boolean
			select_cube.links.new(compare_004.outputs[0], boolean_math_006.inputs[1])
			#position_002.Position -> vector_rotate_002.Vector
			select_cube.links.new(position_002.outputs[0], vector_rotate_002.inputs[0])
			#vector_math_007.Vector -> vector_math_008.Vector
			select_cube.links.new(vector_math_007.outputs[0], vector_math_008.inputs[0])
			#object_info.Location -> vector_rotate_002.Center
			select_cube.links.new(object_info.outputs[1], vector_rotate_002.inputs[1])
			#compare_003.Result -> boolean_math_006.Boolean
			select_cube.links.new(compare_003.outputs[0], boolean_math_006.inputs[0])
			#reroute.Output -> group_output_2.Selection
			select_cube.links.new(reroute.outputs[0], group_output_2.inputs[0])
			#group_input_2.Object -> object_info.Object
			select_cube.links.new(group_input_2.outputs[2], object_info.inputs[0])
			#reroute.Output -> boolean_math.Boolean
			select_cube.links.new(reroute.outputs[0], boolean_math.inputs[0])
			#boolean_math.Boolean -> group_output_2.Inverted
			select_cube.links.new(boolean_math.outputs[0], group_output_2.inputs[1])
			#vector_math_008.Vector -> vector_math.Vector
			select_cube.links.new(vector_math_008.outputs[0], vector_math.inputs[0])
			#vector_math_010.Vector -> vector_math_001.Vector
			select_cube.links.new(vector_math_010.outputs[0], vector_math_001.inputs[0])
			#vector_math.Vector -> vector_math_003.Vector
			select_cube.links.new(vector_math.outputs[0], vector_math_003.inputs[0])
			#vector_math_001.Vector -> vector_math_003.Vector
			select_cube.links.new(vector_math_001.outputs[0], vector_math_003.inputs[1])
			#vector_math_003.Vector -> separate_xyz.Vector
			select_cube.links.new(vector_math_003.outputs[0], separate_xyz.inputs[0])
			#separate_xyz.X -> math_1.Value
			select_cube.links.new(separate_xyz.outputs[0], math_1.inputs[0])
			#separate_xyz.Y -> math_1.Value
			select_cube.links.new(separate_xyz.outputs[1], math_1.inputs[1])
			#math_1.Value -> math_001_1.Value
			select_cube.links.new(math_1.outputs[0], math_001_1.inputs[0])
			#separate_xyz.Z -> math_001_1.Value
			select_cube.links.new(separate_xyz.outputs[2], math_001_1.inputs[1])
			#math_001_1.Value -> map_range.Value
			select_cube.links.new(math_001_1.outputs[0], map_range.inputs[0])
			#group_1.Angstrom -> map_range.From Min
			select_cube.links.new(group_1.outputs[0], map_range.inputs[1])
			#group_001.Angstrom -> map_range.From Max
			select_cube.links.new(group_001.outputs[0], map_range.inputs[2])
			#map_range.Result -> group_output_2.0..1
			select_cube.links.new(map_range.outputs[0], group_output_2.inputs[2])
			#group_input_001.From Min (A) -> group_1.Value
			select_cube.links.new(group_input_001.outputs[3], group_1.inputs[0])
			#group_input_001.From Max (A) -> group_001.Value
			select_cube.links.new(group_input_001.outputs[4], group_001.inputs[0])
			#object_info.Scale -> vector_math_002.Vector
			select_cube.links.new(object_info.outputs[3], vector_math_002.inputs[0])
			#boolean_math_008.Boolean -> reroute.Input
			select_cube.links.new(boolean_math_008.outputs[0], reroute.inputs[0])
			#boolean_math_006.Boolean -> boolean_math_007.Boolean
			select_cube.links.new(boolean_math_006.outputs[0], boolean_math_007.inputs[1])
			#group_input_002.And -> boolean_math_007.Boolean
			select_cube.links.new(group_input_002.outputs[0], boolean_math_007.inputs[0])
			#boolean_math_007.Boolean -> boolean_math_008.Boolean
			select_cube.links.new(boolean_math_007.outputs[0], boolean_math_008.inputs[0])
			#group_input_002.Or -> boolean_math_008.Boolean
			select_cube.links.new(group_input_002.outputs[1], boolean_math_008.inputs[1])
			return select_cube

		select_cube = select_cube_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Select Cube", type = 'NODES')
		mod.node_group = select_cube
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Select_Cube.bl_idname)
			
def register():
	bpy.utils.register_class(Select_Cube)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Select_Cube)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
