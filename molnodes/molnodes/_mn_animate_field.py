bl_info = {
	"name" : ".MN_animate_field",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _MN_animate_field(bpy.types.Operator):
	bl_idname = "node._mn_animate_field"
	bl_label = ".MN_animate_field"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _mn_animate_field node group
		def _mn_animate_field_node_group():
			_mn_animate_field = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_animate_field")

			_mn_animate_field.color_tag = 'NONE'
			_mn_animate_field.description = ""

			
			#_mn_animate_field interface
			#Socket Vector Interp.
			vector_interp__socket = _mn_animate_field.interface.new_socket(name = "Vector Interp.", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			vector_interp__socket.default_value = (0.0, 0.0, 0.0)
			vector_interp__socket.min_value = -3.4028234663852886e+38
			vector_interp__socket.max_value = 3.4028234663852886e+38
			vector_interp__socket.subtype = 'NONE'
			vector_interp__socket.attribute_domain = 'POINT'
			
			#Socket Vector0
			vector0_socket = _mn_animate_field.interface.new_socket(name = "Vector0", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			vector0_socket.default_value = (0.0, 0.0, 0.0)
			vector0_socket.min_value = -3.4028234663852886e+38
			vector0_socket.max_value = 3.4028234663852886e+38
			vector0_socket.subtype = 'NONE'
			vector0_socket.attribute_domain = 'POINT'
			
			#Socket Vector1
			vector1_socket = _mn_animate_field.interface.new_socket(name = "Vector1", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			vector1_socket.default_value = (0.0, 0.0, 0.0)
			vector1_socket.min_value = -3.4028234663852886e+38
			vector1_socket.max_value = 3.4028234663852886e+38
			vector1_socket.subtype = 'NONE'
			vector1_socket.attribute_domain = 'POINT'
			
			#Socket Float Interp.
			float_interp__socket = _mn_animate_field.interface.new_socket(name = "Float Interp.", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			float_interp__socket.default_value = 0.0
			float_interp__socket.min_value = -3.4028234663852886e+38
			float_interp__socket.max_value = 3.4028234663852886e+38
			float_interp__socket.subtype = 'NONE'
			float_interp__socket.attribute_domain = 'POINT'
			
			#Socket Float0
			float0_socket = _mn_animate_field.interface.new_socket(name = "Float0", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			float0_socket.default_value = 0.0
			float0_socket.min_value = -3.4028234663852886e+38
			float0_socket.max_value = 3.4028234663852886e+38
			float0_socket.subtype = 'NONE'
			float0_socket.attribute_domain = 'POINT'
			
			#Socket Float1
			float1_socket = _mn_animate_field.interface.new_socket(name = "Float1", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			float1_socket.default_value = 0.0
			float1_socket.min_value = -3.4028234663852886e+38
			float1_socket.max_value = 3.4028234663852886e+38
			float1_socket.subtype = 'NONE'
			float1_socket.attribute_domain = 'POINT'
			
			#Socket Vector
			vector_socket = _mn_animate_field.interface.new_socket(name = "Vector", in_out='INPUT', socket_type = 'NodeSocketVector')
			vector_socket.default_value = (0.0, 0.0, 0.0)
			vector_socket.min_value = -3.4028234663852886e+38
			vector_socket.max_value = 3.4028234663852886e+38
			vector_socket.subtype = 'NONE'
			vector_socket.attribute_domain = 'POINT'
			vector_socket.hide_value = True
			
			#Socket Float
			float_socket = _mn_animate_field.interface.new_socket(name = "Float", in_out='INPUT', socket_type = 'NodeSocketFloat')
			float_socket.default_value = 0.0
			float_socket.min_value = -3.4028234663852886e+38
			float_socket.max_value = 3.4028234663852886e+38
			float_socket.subtype = 'NONE'
			float_socket.attribute_domain = 'POINT'
			float_socket.hide_value = True
			
			#Socket Frames
			frames_socket = _mn_animate_field.interface.new_socket(name = "Frames", in_out='INPUT', socket_type = 'NodeSocketCollection')
			frames_socket.attribute_domain = 'POINT'
			
			#Socket Start
			start_socket = _mn_animate_field.interface.new_socket(name = "Start", in_out='INPUT', socket_type = 'NodeSocketInt')
			start_socket.default_value = 0
			start_socket.min_value = 0
			start_socket.max_value = 100000
			start_socket.subtype = 'NONE'
			start_socket.attribute_domain = 'POINT'
			
			#Socket End
			end_socket = _mn_animate_field.interface.new_socket(name = "End", in_out='INPUT', socket_type = 'NodeSocketInt')
			end_socket.default_value = -1
			end_socket.min_value = -1
			end_socket.max_value = 100000
			end_socket.subtype = 'NONE'
			end_socket.attribute_domain = 'POINT'
			
			#Socket Animate 0..1
			animate_0__1_socket = _mn_animate_field.interface.new_socket(name = "Animate 0..1", in_out='INPUT', socket_type = 'NodeSocketFloat')
			animate_0__1_socket.default_value = 1.0
			animate_0__1_socket.min_value = -10000.0
			animate_0__1_socket.max_value = 10000.0
			animate_0__1_socket.subtype = 'NONE'
			animate_0__1_socket.attribute_domain = 'POINT'
			
			#Socket Interpolate
			interpolate_socket = _mn_animate_field.interface.new_socket(name = "Interpolate", in_out='INPUT', socket_type = 'NodeSocketBool')
			interpolate_socket.default_value = True
			interpolate_socket.attribute_domain = 'POINT'
			
			#Socket Smoother Step
			smoother_step_socket = _mn_animate_field.interface.new_socket(name = "Smoother Step", in_out='INPUT', socket_type = 'NodeSocketBool')
			smoother_step_socket.default_value = False
			smoother_step_socket.attribute_domain = 'POINT'
			
			#Socket Index
			index_socket = _mn_animate_field.interface.new_socket(name = "Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			index_socket.default_value = 0
			index_socket.min_value = -2147483648
			index_socket.max_value = 2147483647
			index_socket.subtype = 'NONE'
			index_socket.default_attribute_name = "Index"
			index_socket.attribute_domain = 'POINT'
			index_socket.hide_value = True
			
			
			#initialize _mn_animate_field nodes
			#node Compare
			compare = _mn_animate_field.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'EQUAL'
			
			#node Separate Geometry
			separate_geometry = _mn_animate_field.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry.name = "Separate Geometry"
			separate_geometry.domain = 'INSTANCE'
			
			#node Compare.001
			compare_001 = _mn_animate_field.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'INT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'EQUAL'
			
			#node Separate Geometry.001
			separate_geometry_001 = _mn_animate_field.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_001.name = "Separate Geometry.001"
			separate_geometry_001.domain = 'INSTANCE'
			
			#node Realize Instances.001
			realize_instances_001 = _mn_animate_field.nodes.new("GeometryNodeRealizeInstances")
			realize_instances_001.name = "Realize Instances.001"
			#Selection
			realize_instances_001.inputs[1].default_value = True
			#Realize All
			realize_instances_001.inputs[2].default_value = True
			#Depth
			realize_instances_001.inputs[3].default_value = 0
			
			#node Reroute.003
			reroute_003 = _mn_animate_field.nodes.new("NodeReroute")
			reroute_003.name = "Reroute.003"
			#node Map Range
			map_range = _mn_animate_field.nodes.new("ShaderNodeMapRange")
			map_range.name = "Map Range"
			map_range.clamp = False
			map_range.data_type = 'FLOAT'
			map_range.interpolation_type = 'LINEAR'
			#From Min
			map_range.inputs[1].default_value = 0.0
			#From Max
			map_range.inputs[2].default_value = 1.0
			
			#node Reroute.004
			reroute_004 = _mn_animate_field.nodes.new("NodeReroute")
			reroute_004.name = "Reroute.004"
			#node Switch.001
			switch_001 = _mn_animate_field.nodes.new("GeometryNodeSwitch")
			switch_001.name = "Switch.001"
			switch_001.input_type = 'FLOAT'
			
			#node Index.001
			index_001 = _mn_animate_field.nodes.new("GeometryNodeInputIndex")
			index_001.name = "Index.001"
			
			#node Realize Instances
			realize_instances = _mn_animate_field.nodes.new("GeometryNodeRealizeInstances")
			realize_instances.name = "Realize Instances"
			#Selection
			realize_instances.inputs[1].default_value = True
			#Realize All
			realize_instances.inputs[2].default_value = True
			#Depth
			realize_instances.inputs[3].default_value = 0
			
			#node Group Output
			group_output = _mn_animate_field.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Reroute.005
			reroute_005 = _mn_animate_field.nodes.new("NodeReroute")
			reroute_005.name = "Reroute.005"
			#node Switch.002
			switch_002 = _mn_animate_field.nodes.new("GeometryNodeSwitch")
			switch_002.name = "Switch.002"
			switch_002.input_type = 'VECTOR'
			
			#node Group Input.003
			group_input_003 = _mn_animate_field.nodes.new("NodeGroupInput")
			group_input_003.name = "Group Input.003"
			
			#node Sample Index.002
			sample_index_002 = _mn_animate_field.nodes.new("GeometryNodeSampleIndex")
			sample_index_002.name = "Sample Index.002"
			sample_index_002.clamp = True
			sample_index_002.data_type = 'FLOAT'
			sample_index_002.domain = 'POINT'
			
			#node Reroute.002
			reroute_002 = _mn_animate_field.nodes.new("NodeReroute")
			reroute_002.name = "Reroute.002"
			#node Mix.001
			mix_001 = _mn_animate_field.nodes.new("ShaderNodeMix")
			mix_001.name = "Mix.001"
			mix_001.blend_type = 'MIX'
			mix_001.clamp_factor = True
			mix_001.clamp_result = False
			mix_001.data_type = 'FLOAT'
			mix_001.factor_mode = 'UNIFORM'
			
			#node Switch.003
			switch_003 = _mn_animate_field.nodes.new("GeometryNodeSwitch")
			switch_003.name = "Switch.003"
			switch_003.input_type = 'FLOAT'
			
			#node Index.002
			index_002 = _mn_animate_field.nodes.new("GeometryNodeInputIndex")
			index_002.name = "Index.002"
			
			#node Switch.004
			switch_004 = _mn_animate_field.nodes.new("GeometryNodeSwitch")
			switch_004.label = "backup_index"
			switch_004.name = "Switch.004"
			switch_004.input_type = 'INT'
			
			#node Field at Index
			field_at_index = _mn_animate_field.nodes.new("GeometryNodeFieldAtIndex")
			field_at_index.name = "Field at Index"
			field_at_index.hide = True
			field_at_index.data_type = 'INT'
			field_at_index.domain = 'POINT'
			#Index
			field_at_index.inputs[0].default_value = 1
			
			#node Index.004
			index_004 = _mn_animate_field.nodes.new("GeometryNodeInputIndex")
			index_004.name = "Index.004"
			
			#node Mix
			mix = _mn_animate_field.nodes.new("ShaderNodeMix")
			mix.name = "Mix"
			mix.blend_type = 'MIX'
			mix.clamp_factor = True
			mix.clamp_result = False
			mix.data_type = 'VECTOR'
			mix.factor_mode = 'UNIFORM'
			
			#node Sample Index
			sample_index = _mn_animate_field.nodes.new("GeometryNodeSampleIndex")
			sample_index.name = "Sample Index"
			sample_index.clamp = True
			sample_index.data_type = 'FLOAT_VECTOR'
			sample_index.domain = 'POINT'
			
			#node Sample Index.001
			sample_index_001 = _mn_animate_field.nodes.new("GeometryNodeSampleIndex")
			sample_index_001.name = "Sample Index.001"
			sample_index_001.clamp = True
			sample_index_001.data_type = 'FLOAT_VECTOR'
			sample_index_001.domain = 'POINT'
			
			#node Sample Index.003
			sample_index_003 = _mn_animate_field.nodes.new("GeometryNodeSampleIndex")
			sample_index_003.name = "Sample Index.003"
			sample_index_003.clamp = True
			sample_index_003.data_type = 'FLOAT'
			sample_index_003.domain = 'POINT'
			
			#node Group Input.002
			group_input_002 = _mn_animate_field.nodes.new("NodeGroupInput")
			group_input_002.name = "Group Input.002"
			
			#node Reroute.001
			reroute_001 = _mn_animate_field.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			#node Index
			index = _mn_animate_field.nodes.new("GeometryNodeInputIndex")
			index.name = "Index"
			
			#node Reroute
			reroute = _mn_animate_field.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Math.006
			math_006 = _mn_animate_field.nodes.new("ShaderNodeMath")
			math_006.name = "Math.006"
			math_006.operation = 'MINIMUM'
			math_006.use_clamp = False
			
			#node Math
			math = _mn_animate_field.nodes.new("ShaderNodeMath")
			math.label = "x + 1"
			math.name = "Math"
			math.hide = True
			math.operation = 'ADD'
			math.use_clamp = False
			#Value_001
			math.inputs[1].default_value = 1.0
			
			#node Math.002
			math_002 = _mn_animate_field.nodes.new("ShaderNodeMath")
			math_002.name = "Math.002"
			math_002.operation = 'FLOOR'
			math_002.use_clamp = False
			
			#node Switch.005
			switch_005 = _mn_animate_field.nodes.new("GeometryNodeSwitch")
			switch_005.name = "Switch.005"
			switch_005.input_type = 'INT'
			
			#node Math.003
			math_003 = _mn_animate_field.nodes.new("ShaderNodeMath")
			math_003.label = "x - 1"
			math_003.name = "Math.003"
			math_003.hide = True
			math_003.operation = 'SUBTRACT'
			math_003.use_clamp = False
			#Value_001
			math_003.inputs[1].default_value = 1.0
			
			#node Math.005
			math_005 = _mn_animate_field.nodes.new("ShaderNodeMath")
			math_005.name = "Math.005"
			math_005.operation = 'WRAP'
			math_005.use_clamp = False
			#Value_001
			math_005.inputs[1].default_value = 1.0
			#Value_002
			math_005.inputs[2].default_value = 0.0
			
			#node Domain Size
			domain_size = _mn_animate_field.nodes.new("GeometryNodeAttributeDomainSize")
			domain_size.name = "Domain Size"
			domain_size.component = 'INSTANCES'
			
			#node Reroute.007
			reroute_007 = _mn_animate_field.nodes.new("NodeReroute")
			reroute_007.name = "Reroute.007"
			#node Collection Info
			collection_info = _mn_animate_field.nodes.new("GeometryNodeCollectionInfo")
			collection_info.name = "Collection Info"
			collection_info.transform_space = 'RELATIVE'
			#Separate Children
			collection_info.inputs[1].default_value = True
			#Reset Children
			collection_info.inputs[2].default_value = False
			
			#node Group Input
			group_input = _mn_animate_field.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Compare.002
			compare_002 = _mn_animate_field.nodes.new("FunctionNodeCompare")
			compare_002.name = "Compare.002"
			compare_002.data_type = 'INT'
			compare_002.mode = 'ELEMENT'
			compare_002.operation = 'EQUAL'
			#B_INT
			compare_002.inputs[3].default_value = -1
			
			#node Reroute.008
			reroute_008 = _mn_animate_field.nodes.new("NodeReroute")
			reroute_008.name = "Reroute.008"
			#node Reroute.006
			reroute_006 = _mn_animate_field.nodes.new("NodeReroute")
			reroute_006.name = "Reroute.006"
			#node Map Range.001
			map_range_001 = _mn_animate_field.nodes.new("ShaderNodeMapRange")
			map_range_001.name = "Map Range.001"
			map_range_001.clamp = True
			map_range_001.data_type = 'FLOAT'
			map_range_001.interpolation_type = 'SMOOTHERSTEP'
			#From Min
			map_range_001.inputs[1].default_value = 0.0
			#From Max
			map_range_001.inputs[2].default_value = 1.0
			#To Min
			map_range_001.inputs[3].default_value = 0.0
			#To Max
			map_range_001.inputs[4].default_value = 1.0
			
			#node Math.004
			math_004 = _mn_animate_field.nodes.new("ShaderNodeMath")
			math_004.name = "Math.004"
			math_004.operation = 'FRACT'
			math_004.use_clamp = False
			
			#node Group Input.001
			group_input_001 = _mn_animate_field.nodes.new("NodeGroupInput")
			group_input_001.name = "Group Input.001"
			
			#node Group Input.004
			group_input_004 = _mn_animate_field.nodes.new("NodeGroupInput")
			group_input_004.name = "Group Input.004"
			
			
			
			
			#Set locations
			compare.location = (328.0, -140.0)
			separate_geometry.location = (328.0, 20.0)
			compare_001.location = (328.0, -540.0)
			separate_geometry_001.location = (328.0, -380.0)
			realize_instances_001.location = (488.0, -380.0)
			reroute_003.location = (-620.0, -220.0)
			map_range.location = (-800.0, -160.0)
			reroute_004.location = (41.4283447265625, 62.94276809692383)
			switch_001.location = (-140.0, 240.0)
			index_001.location = (160.0, -600.0)
			realize_instances.location = (488.0, 20.0)
			group_output.location = (1571.8603515625, 139.68081665039062)
			reroute_005.location = (724.9548950195312, -220.96487426757812)
			switch_002.location = (1220.0, 136.82861328125)
			group_input_003.location = (520.0, -800.0)
			sample_index_002.location = (820.0, -980.0)
			reroute_002.location = (700.0, 60.0)
			mix_001.location = (1020.0, -740.0)
			switch_003.location = (1240.0, -620.0)
			index_002.location = (480.0, -320.0)
			switch_004.location = (500.0, 320.0)
			field_at_index.location = (320.0, 220.0)
			index_004.location = (320.0, 180.0)
			mix.location = (1000.0, 20.0)
			sample_index.location = (800.0, 20.0)
			sample_index_001.location = (800.0, -200.0)
			sample_index_003.location = (820.0, -740.0)
			group_input_002.location = (1000.0, 360.0)
			reroute_001.location = (100.0, -240.0)
			index.location = (160.0, -220.0)
			reroute.location = (100.0, -280.0)
			math_006.location = (160.0, -660.0)
			math.location = (-60.0, -660.0)
			math_002.location = (-598.4962768554688, -251.16390991210938)
			switch_005.location = (-800.0, -420.0)
			math_003.location = (-960.0, -600.0)
			math_005.location = (-800.0, 40.0)
			domain_size.location = (-960.0, -640.0)
			reroute_007.location = (-240.0, -660.0)
			collection_info.location = (-1160.0, -600.0)
			group_input.location = (-1600.0, -80.0)
			compare_002.location = (-960.0, -420.0)
			reroute_008.location = (780.0, -1020.0)
			reroute_006.location = (738.3385009765625, -275.85125732421875)
			map_range_001.location = (-140.0, 80.0)
			math_004.location = (-340.0, 100.0)
			group_input_001.location = (-340.0, 360.0)
			group_input_004.location = (320.0, 500.0)
			
			#Set dimensions
			compare.width, compare.height = 140.0, 100.0
			separate_geometry.width, separate_geometry.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			separate_geometry_001.width, separate_geometry_001.height = 140.0, 100.0
			realize_instances_001.width, realize_instances_001.height = 140.0, 100.0
			reroute_003.width, reroute_003.height = 16.0, 100.0
			map_range.width, map_range.height = 140.0, 100.0
			reroute_004.width, reroute_004.height = 16.0, 100.0
			switch_001.width, switch_001.height = 140.0, 100.0
			index_001.width, index_001.height = 140.0, 100.0
			realize_instances.width, realize_instances.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			reroute_005.width, reroute_005.height = 16.0, 100.0
			switch_002.width, switch_002.height = 140.0, 100.0
			group_input_003.width, group_input_003.height = 140.0, 100.0
			sample_index_002.width, sample_index_002.height = 140.0, 100.0
			reroute_002.width, reroute_002.height = 16.0, 100.0
			mix_001.width, mix_001.height = 140.0, 100.0
			switch_003.width, switch_003.height = 140.0, 100.0
			index_002.width, index_002.height = 140.0, 100.0
			switch_004.width, switch_004.height = 140.0, 100.0
			field_at_index.width, field_at_index.height = 140.0, 100.0
			index_004.width, index_004.height = 140.0, 100.0
			mix.width, mix.height = 140.0, 100.0
			sample_index.width, sample_index.height = 140.0, 100.0
			sample_index_001.width, sample_index_001.height = 140.0, 100.0
			sample_index_003.width, sample_index_003.height = 140.0, 100.0
			group_input_002.width, group_input_002.height = 140.0, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			index.width, index.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			math_006.width, math_006.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			math_002.width, math_002.height = 140.0, 100.0
			switch_005.width, switch_005.height = 140.0, 100.0
			math_003.width, math_003.height = 140.0, 100.0
			math_005.width, math_005.height = 140.0, 100.0
			domain_size.width, domain_size.height = 140.0, 100.0
			reroute_007.width, reroute_007.height = 16.0, 100.0
			collection_info.width, collection_info.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			compare_002.width, compare_002.height = 140.0, 100.0
			reroute_008.width, reroute_008.height = 16.0, 100.0
			reroute_006.width, reroute_006.height = 16.0, 100.0
			map_range_001.width, map_range_001.height = 140.0, 100.0
			math_004.width, math_004.height = 140.0, 100.0
			group_input_001.width, group_input_001.height = 140.0, 100.0
			group_input_004.width, group_input_004.height = 140.0, 100.0
			
			#initialize _mn_animate_field links
			#group_input.Frames -> collection_info.Collection
			_mn_animate_field.links.new(group_input.outputs[2], collection_info.inputs[0])
			#reroute_001.Output -> separate_geometry.Geometry
			_mn_animate_field.links.new(reroute_001.outputs[0], separate_geometry.inputs[0])
			#index.Index -> compare.A
			_mn_animate_field.links.new(index.outputs[0], compare.inputs[2])
			#compare.Result -> separate_geometry.Selection
			_mn_animate_field.links.new(compare.outputs[0], separate_geometry.inputs[1])
			#separate_geometry.Selection -> realize_instances.Geometry
			_mn_animate_field.links.new(separate_geometry.outputs[0], realize_instances.inputs[0])
			#reroute.Output -> compare.B
			_mn_animate_field.links.new(reroute.outputs[0], compare.inputs[3])
			#reroute.Output -> math.Value
			_mn_animate_field.links.new(reroute.outputs[0], math.inputs[0])
			#reroute_001.Output -> separate_geometry_001.Geometry
			_mn_animate_field.links.new(reroute_001.outputs[0], separate_geometry_001.inputs[0])
			#index_001.Index -> compare_001.A
			_mn_animate_field.links.new(index_001.outputs[0], compare_001.inputs[2])
			#compare_001.Result -> separate_geometry_001.Selection
			_mn_animate_field.links.new(compare_001.outputs[0], separate_geometry_001.inputs[1])
			#separate_geometry_001.Selection -> realize_instances_001.Geometry
			_mn_animate_field.links.new(separate_geometry_001.outputs[0], realize_instances_001.inputs[0])
			#realize_instances.Geometry -> sample_index.Geometry
			_mn_animate_field.links.new(realize_instances.outputs[0], sample_index.inputs[0])
			#realize_instances_001.Geometry -> sample_index_001.Geometry
			_mn_animate_field.links.new(realize_instances_001.outputs[0], sample_index_001.inputs[0])
			#reroute_005.Output -> sample_index.Value
			_mn_animate_field.links.new(reroute_005.outputs[0], sample_index.inputs[1])
			#reroute_005.Output -> sample_index_001.Value
			_mn_animate_field.links.new(reroute_005.outputs[0], sample_index_001.inputs[1])
			#sample_index.Value -> mix.A
			_mn_animate_field.links.new(sample_index.outputs[0], mix.inputs[6])
			#sample_index_001.Value -> mix.B
			_mn_animate_field.links.new(sample_index_001.outputs[0], mix.inputs[7])
			#reroute_007.Output -> reroute_001.Input
			_mn_animate_field.links.new(reroute_007.outputs[0], reroute_001.inputs[0])
			#collection_info.Instances -> domain_size.Geometry
			_mn_animate_field.links.new(collection_info.outputs[0], domain_size.inputs[0])
			#reroute_003.Output -> math_002.Value
			_mn_animate_field.links.new(reroute_003.outputs[0], math_002.inputs[0])
			#domain_size.Instance Count -> math_003.Value
			_mn_animate_field.links.new(domain_size.outputs[5], math_003.inputs[0])
			#reroute_003.Output -> math_004.Value
			_mn_animate_field.links.new(reroute_003.outputs[0], math_004.inputs[0])
			#reroute_002.Output -> mix.Factor
			_mn_animate_field.links.new(reroute_002.outputs[0], mix.inputs[0])
			#reroute_004.Output -> reroute_002.Input
			_mn_animate_field.links.new(reroute_004.outputs[0], reroute_002.inputs[0])
			#map_range.Result -> reroute_003.Input
			_mn_animate_field.links.new(map_range.outputs[0], reroute_003.inputs[0])
			#math_002.Value -> reroute.Input
			_mn_animate_field.links.new(math_002.outputs[0], reroute.inputs[0])
			#reroute_006.Output -> sample_index.Index
			_mn_animate_field.links.new(reroute_006.outputs[0], sample_index.inputs[2])
			#math_004.Value -> map_range_001.Value
			_mn_animate_field.links.new(math_004.outputs[0], map_range_001.inputs[0])
			#switch_001.Output -> reroute_004.Input
			_mn_animate_field.links.new(switch_001.outputs[0], reroute_004.inputs[0])
			#math_004.Value -> switch_001.False
			_mn_animate_field.links.new(math_004.outputs[0], switch_001.inputs[1])
			#map_range_001.Result -> switch_001.True
			_mn_animate_field.links.new(map_range_001.outputs[0], switch_001.inputs[2])
			#group_input_001.Smoother Step -> switch_001.Switch
			_mn_animate_field.links.new(group_input_001.outputs[7], switch_001.inputs[0])
			#sample_index.Value -> mix.A
			_mn_animate_field.links.new(sample_index.outputs[0], mix.inputs[4])
			#sample_index_001.Value -> mix.B
			_mn_animate_field.links.new(sample_index_001.outputs[0], mix.inputs[5])
			#reroute_006.Output -> sample_index_001.Index
			_mn_animate_field.links.new(reroute_006.outputs[0], sample_index_001.inputs[2])
			#mix.Result -> switch_002.True
			_mn_animate_field.links.new(mix.outputs[1], switch_002.inputs[2])
			#sample_index.Value -> switch_002.False
			_mn_animate_field.links.new(sample_index.outputs[0], switch_002.inputs[1])
			#group_input_002.Interpolate -> switch_002.Switch
			_mn_animate_field.links.new(group_input_002.outputs[6], switch_002.inputs[0])
			#switch_002.Output -> group_output.Vector Interp.
			_mn_animate_field.links.new(switch_002.outputs[0], group_output.inputs[0])
			#group_input_003.Vector -> reroute_005.Input
			_mn_animate_field.links.new(group_input_003.outputs[0], reroute_005.inputs[0])
			#realize_instances.Geometry -> sample_index_003.Geometry
			_mn_animate_field.links.new(realize_instances.outputs[0], sample_index_003.inputs[0])
			#realize_instances_001.Geometry -> sample_index_002.Geometry
			_mn_animate_field.links.new(realize_instances_001.outputs[0], sample_index_002.inputs[0])
			#group_input_002.Interpolate -> switch_003.Switch
			_mn_animate_field.links.new(group_input_002.outputs[6], switch_003.inputs[0])
			#reroute_008.Output -> sample_index_003.Index
			_mn_animate_field.links.new(reroute_008.outputs[0], sample_index_003.inputs[2])
			#reroute_008.Output -> sample_index_002.Index
			_mn_animate_field.links.new(reroute_008.outputs[0], sample_index_002.inputs[2])
			#group_input_003.Float -> sample_index_003.Value
			_mn_animate_field.links.new(group_input_003.outputs[1], sample_index_003.inputs[1])
			#group_input_003.Float -> sample_index_002.Value
			_mn_animate_field.links.new(group_input_003.outputs[1], sample_index_002.inputs[1])
			#sample_index_003.Value -> mix_001.A
			_mn_animate_field.links.new(sample_index_003.outputs[0], mix_001.inputs[2])
			#sample_index_002.Value -> mix_001.B
			_mn_animate_field.links.new(sample_index_002.outputs[0], mix_001.inputs[3])
			#reroute_002.Output -> mix_001.Factor
			_mn_animate_field.links.new(reroute_002.outputs[0], mix_001.inputs[0])
			#mix_001.Result -> switch_003.True
			_mn_animate_field.links.new(mix_001.outputs[0], switch_003.inputs[2])
			#sample_index_003.Value -> switch_003.False
			_mn_animate_field.links.new(sample_index_003.outputs[0], switch_003.inputs[1])
			#switch_003.Output -> group_output.Float Interp.
			_mn_animate_field.links.new(switch_003.outputs[0], group_output.inputs[3])
			#group_input_004.Index -> switch_004.True
			_mn_animate_field.links.new(group_input_004.outputs[8], switch_004.inputs[2])
			#field_at_index.Value -> switch_004.Switch
			_mn_animate_field.links.new(field_at_index.outputs[0], switch_004.inputs[0])
			#index_004.Index -> switch_004.False
			_mn_animate_field.links.new(index_004.outputs[0], switch_004.inputs[1])
			#switch_004.Output -> reroute_006.Input
			_mn_animate_field.links.new(switch_004.outputs[0], reroute_006.inputs[0])
			#group_input_004.Index -> field_at_index.Value
			_mn_animate_field.links.new(group_input_004.outputs[8], field_at_index.inputs[1])
			#sample_index.Value -> group_output.Vector0
			_mn_animate_field.links.new(sample_index.outputs[0], group_output.inputs[1])
			#sample_index_001.Value -> group_output.Vector1
			_mn_animate_field.links.new(sample_index_001.outputs[0], group_output.inputs[2])
			#sample_index_003.Value -> group_output.Float0
			_mn_animate_field.links.new(sample_index_003.outputs[0], group_output.inputs[4])
			#sample_index_002.Value -> group_output.Float1
			_mn_animate_field.links.new(sample_index_002.outputs[0], group_output.inputs[5])
			#group_input.End -> compare_002.A
			_mn_animate_field.links.new(group_input.outputs[4], compare_002.inputs[2])
			#compare_002.Result -> switch_005.Switch
			_mn_animate_field.links.new(compare_002.outputs[0], switch_005.inputs[0])
			#group_input.End -> switch_005.False
			_mn_animate_field.links.new(group_input.outputs[4], switch_005.inputs[1])
			#switch_005.Output -> map_range.To Max
			_mn_animate_field.links.new(switch_005.outputs[0], map_range.inputs[4])
			#group_input.Start -> map_range.To Min
			_mn_animate_field.links.new(group_input.outputs[3], map_range.inputs[3])
			#math_003.Value -> switch_005.True
			_mn_animate_field.links.new(math_003.outputs[0], switch_005.inputs[2])
			#math_003.Value -> math_006.Value
			_mn_animate_field.links.new(math_003.outputs[0], math_006.inputs[0])
			#math.Value -> math_006.Value
			_mn_animate_field.links.new(math.outputs[0], math_006.inputs[1])
			#math_006.Value -> compare_001.B
			_mn_animate_field.links.new(math_006.outputs[0], compare_001.inputs[3])
			#group_input.Animate 0..1 -> math_005.Value
			_mn_animate_field.links.new(group_input.outputs[5], math_005.inputs[0])
			#math_005.Value -> map_range.Value
			_mn_animate_field.links.new(math_005.outputs[0], map_range.inputs[0])
			#collection_info.Instances -> reroute_007.Input
			_mn_animate_field.links.new(collection_info.outputs[0], reroute_007.inputs[0])
			#reroute_006.Output -> reroute_008.Input
			_mn_animate_field.links.new(reroute_006.outputs[0], reroute_008.inputs[0])
			return _mn_animate_field

		_mn_animate_field = _mn_animate_field_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".MN_animate_field", type = 'NODES')
		mod.node_group = _mn_animate_field
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_MN_animate_field.bl_idname)
			
def register():
	bpy.utils.register_class(_MN_animate_field)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_MN_animate_field)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
