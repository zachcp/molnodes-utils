bl_info = {
	"name" : "MN_topo_backbone",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class MN_topo_backbone(bpy.types.Operator):
	bl_idname = "node.mn_topo_backbone"
	bl_label = "MN_topo_backbone"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize offset_vector node group
		def offset_vector_node_group():
			offset_vector = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Offset Vector")

			offset_vector.color_tag = 'CONVERTER'
			offset_vector.description = ""

			
			#offset_vector interface
			#Socket Value
			value_socket = offset_vector.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			value_socket.default_value = (0.0, 0.0, 0.0)
			value_socket.min_value = -3.4028234663852886e+38
			value_socket.max_value = 3.4028234663852886e+38
			value_socket.subtype = 'NONE'
			value_socket.attribute_domain = 'POINT'
			
			#Socket Index
			index_socket = offset_vector.interface.new_socket(name = "Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			index_socket.default_value = 0
			index_socket.min_value = 0
			index_socket.max_value = 2147483647
			index_socket.subtype = 'NONE'
			index_socket.attribute_domain = 'POINT'
			
			#Socket Position
			position_socket = offset_vector.interface.new_socket(name = "Position", in_out='INPUT', socket_type = 'NodeSocketVector')
			position_socket.default_value = (0.0, 0.0, 0.0)
			position_socket.min_value = -3.4028234663852886e+38
			position_socket.max_value = 3.4028234663852886e+38
			position_socket.subtype = 'NONE'
			position_socket.attribute_domain = 'POINT'
			position_socket.hide_value = True
			
			#Socket Offset
			offset_socket = offset_vector.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket.default_value = 0
			offset_socket.min_value = -2147483647
			offset_socket.max_value = 2147483647
			offset_socket.subtype = 'NONE'
			offset_socket.attribute_domain = 'POINT'
			
			
			#initialize offset_vector nodes
			#node Group Output
			group_output = offset_vector.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = offset_vector.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Evaluate at Index
			evaluate_at_index = offset_vector.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index.name = "Evaluate at Index"
			evaluate_at_index.data_type = 'FLOAT_VECTOR'
			evaluate_at_index.domain = 'POINT'
			
			#node Math
			math = offset_vector.nodes.new("ShaderNodeMath")
			math.name = "Math"
			math.operation = 'ADD'
			math.use_clamp = False
			
			
			
			
			#Set locations
			group_output.location = (300.0, 20.0)
			group_input.location = (-273.81378173828125, 0.0)
			evaluate_at_index.location = (120.0, 20.0)
			math.location = (-60.0, 20.0)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			evaluate_at_index.width, evaluate_at_index.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			
			#initialize offset_vector links
			#group_input.Position -> evaluate_at_index.Value
			offset_vector.links.new(group_input.outputs[1], evaluate_at_index.inputs[1])
			#evaluate_at_index.Value -> group_output.Value
			offset_vector.links.new(evaluate_at_index.outputs[0], group_output.inputs[0])
			#group_input.Index -> math.Value
			offset_vector.links.new(group_input.outputs[0], math.inputs[0])
			#group_input.Offset -> math.Value
			offset_vector.links.new(group_input.outputs[2], math.inputs[1])
			#math.Value -> evaluate_at_index.Index
			offset_vector.links.new(math.outputs[0], evaluate_at_index.inputs[0])
			return offset_vector

		offset_vector = offset_vector_node_group()

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
			group_input_1 = _mn_world_scale.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			
			#node Value
			value = _mn_world_scale.nodes.new("ShaderNodeValue")
			value.label = "world_scale"
			value.name = "Value"
			
			value.outputs[0].default_value = 0.009999999776482582
			#node Group Output
			group_output_1 = _mn_world_scale.nodes.new("NodeGroupOutput")
			group_output_1.name = "Group Output"
			group_output_1.is_active_output = True
			
			
			
			
			#Set locations
			group_input_1.location = (-200.0, 0.0)
			value.location = (0.0, 0.0)
			group_output_1.location = (190.0, 0.0)
			
			#Set dimensions
			group_input_1.width, group_input_1.height = 140.0, 100.0
			value.width, value.height = 140.0, 100.0
			group_output_1.width, group_output_1.height = 140.0, 100.0
			
			#initialize _mn_world_scale links
			#value.Value -> group_output_1.world_scale
			_mn_world_scale.links.new(value.outputs[0], group_output_1.inputs[0])
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
			value_socket_1 = mn_units.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket_1.default_value = 3.0
			value_socket_1.min_value = -10000.0
			value_socket_1.max_value = 10000.0
			value_socket_1.subtype = 'NONE'
			value_socket_1.attribute_domain = 'POINT'
			value_socket_1.description = "A value which will be scaled appropriately for the world"
			
			
			#initialize mn_units nodes
			#node Group Output
			group_output_2 = mn_units.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Group Input
			group_input_2 = mn_units.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
			#node Math
			math_1 = mn_units.nodes.new("ShaderNodeMath")
			math_1.name = "Math"
			math_1.operation = 'MULTIPLY'
			math_1.use_clamp = False
			
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
			group_output_2.location = (190.0, 0.0)
			group_input_2.location = (-240.0, 0.0)
			math_1.location = (-60.0, 0.0)
			math_001.location = (-60.0, -160.0)
			group.location = (-304.00421142578125, -104.114013671875)
			
			#Set dimensions
			group_output_2.width, group_output_2.height = 140.0, 100.0
			group_input_2.width, group_input_2.height = 140.0, 100.0
			math_1.width, math_1.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			group.width, group.height = 197.58424377441406, 100.0
			
			#initialize mn_units links
			#math_1.Value -> group_output_2.Angstrom
			mn_units.links.new(math_1.outputs[0], group_output_2.inputs[0])
			#group_input_2.Value -> math_1.Value
			mn_units.links.new(group_input_2.outputs[0], math_1.inputs[0])
			#group.world_scale -> math_1.Value
			mn_units.links.new(group.outputs[0], math_1.inputs[1])
			#math_1.Value -> math_001.Value
			mn_units.links.new(math_1.outputs[0], math_001.inputs[0])
			#math_001.Value -> group_output_2.Nanometre
			mn_units.links.new(math_001.outputs[0], group_output_2.inputs[1])
			return mn_units

		mn_units = mn_units_node_group()

		#initialize backbone_nh node group
		def backbone_nh_node_group():
			backbone_nh = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Backbone NH")

			backbone_nh.color_tag = 'NONE'
			backbone_nh.description = ""

			
			#backbone_nh interface
			#Socket H
			h_socket = backbone_nh.interface.new_socket(name = "H", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			h_socket.default_value = (0.0, 0.0, 0.0)
			h_socket.min_value = -3.4028234663852886e+38
			h_socket.max_value = 3.4028234663852886e+38
			h_socket.subtype = 'NONE'
			h_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_2 = backbone_nh.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket_2.default_value = 1.0
			value_socket_2.min_value = -10000.0
			value_socket_2.max_value = 10000.0
			value_socket_2.subtype = 'NONE'
			value_socket_2.attribute_domain = 'POINT'
			
			
			#initialize backbone_nh nodes
			#node Group Output
			group_output_3 = backbone_nh.nodes.new("NodeGroupOutput")
			group_output_3.name = "Group Output"
			group_output_3.is_active_output = True
			
			#node Group Input
			group_input_3 = backbone_nh.nodes.new("NodeGroupInput")
			group_input_3.name = "Group Input"
			
			#node Named Attribute
			named_attribute = backbone_nh.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute.inputs[0].default_value = "backbone_N"
			
			#node Named Attribute.001
			named_attribute_001 = backbone_nh.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_001.inputs[0].default_value = "backbone_CA"
			
			#node Named Attribute.002
			named_attribute_002 = backbone_nh.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002.name = "Named Attribute.002"
			named_attribute_002.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_002.inputs[0].default_value = "backbone_C"
			
			#node Group.002
			group_002 = backbone_nh.nodes.new("GeometryNodeGroup")
			group_002.name = "Group.002"
			group_002.node_tree = offset_vector
			#Socket_2
			group_002.inputs[0].default_value = 0
			#Socket_3
			group_002.inputs[2].default_value = -1
			
			#node Vector Math
			vector_math = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.operation = 'SUBTRACT'
			
			#node Vector Math.001
			vector_math_001 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_001.name = "Vector Math.001"
			vector_math_001.operation = 'SUBTRACT'
			
			#node Vector Math.002
			vector_math_002 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_002.name = "Vector Math.002"
			vector_math_002.operation = 'NORMALIZE'
			
			#node Vector Math.003
			vector_math_003 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_003.name = "Vector Math.003"
			vector_math_003.operation = 'NORMALIZE'
			
			#node Vector Math.005
			vector_math_005 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_005.name = "Vector Math.005"
			vector_math_005.operation = 'ADD'
			
			#node Vector Math.006
			vector_math_006 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_006.name = "Vector Math.006"
			vector_math_006.operation = 'ADD'
			
			#node Vector Math.004
			vector_math_004 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_004.name = "Vector Math.004"
			vector_math_004.operation = 'SCALE'
			
			#node Group.003
			group_003 = backbone_nh.nodes.new("GeometryNodeGroup")
			group_003.name = "Group.003"
			group_003.node_tree = mn_units
			
			#node Vector Math.007
			vector_math_007 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_007.name = "Vector Math.007"
			vector_math_007.operation = 'NORMALIZE'
			
			
			
			
			#Set locations
			group_output_3.location = (620.0, 0.0)
			group_input_3.location = (-630.0, 0.0)
			named_attribute.location = (-430.0, 140.0)
			named_attribute_001.location = (-430.0, 0.0)
			named_attribute_002.location = (-430.0, -140.0)
			group_002.location = (-210.0, -120.0)
			vector_math.location = (-50.0, 0.0)
			vector_math_001.location = (-50.0, 140.0)
			vector_math_002.location = (110.0, 140.0)
			vector_math_003.location = (110.0, 0.0)
			vector_math_005.location = (270.0, 140.0)
			vector_math_006.location = (430.0, 140.0)
			vector_math_004.location = (260.0, -120.0)
			group_003.location = (100.0, -120.0)
			vector_math_007.location = (260.0, 0.0)
			
			#Set dimensions
			group_output_3.width, group_output_3.height = 140.0, 100.0
			group_input_3.width, group_input_3.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 189.579833984375, 100.0
			named_attribute_001.width, named_attribute_001.height = 189.579833984375, 100.0
			named_attribute_002.width, named_attribute_002.height = 189.579833984375, 100.0
			group_002.width, group_002.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			vector_math_001.width, vector_math_001.height = 140.0, 100.0
			vector_math_002.width, vector_math_002.height = 140.0, 100.0
			vector_math_003.width, vector_math_003.height = 140.0, 100.0
			vector_math_005.width, vector_math_005.height = 140.0, 100.0
			vector_math_006.width, vector_math_006.height = 140.0, 100.0
			vector_math_004.width, vector_math_004.height = 140.0, 100.0
			group_003.width, group_003.height = 140.0, 100.0
			vector_math_007.width, vector_math_007.height = 140.0, 100.0
			
			#initialize backbone_nh links
			#vector_math_004.Vector -> vector_math_006.Vector
			backbone_nh.links.new(vector_math_004.outputs[0], vector_math_006.inputs[1])
			#named_attribute_001.Attribute -> vector_math_001.Vector
			backbone_nh.links.new(named_attribute_001.outputs[0], vector_math_001.inputs[1])
			#named_attribute_002.Attribute -> group_002.Position
			backbone_nh.links.new(named_attribute_002.outputs[0], group_002.inputs[1])
			#named_attribute.Attribute -> vector_math.Vector
			backbone_nh.links.new(named_attribute.outputs[0], vector_math.inputs[0])
			#vector_math.Vector -> vector_math_003.Vector
			backbone_nh.links.new(vector_math.outputs[0], vector_math_003.inputs[0])
			#group_003.Angstrom -> vector_math_004.Scale
			backbone_nh.links.new(group_003.outputs[0], vector_math_004.inputs[3])
			#vector_math_003.Vector -> vector_math_005.Vector
			backbone_nh.links.new(vector_math_003.outputs[0], vector_math_005.inputs[1])
			#group_002.Value -> vector_math.Vector
			backbone_nh.links.new(group_002.outputs[0], vector_math.inputs[1])
			#vector_math_002.Vector -> vector_math_005.Vector
			backbone_nh.links.new(vector_math_002.outputs[0], vector_math_005.inputs[0])
			#named_attribute.Attribute -> vector_math_001.Vector
			backbone_nh.links.new(named_attribute.outputs[0], vector_math_001.inputs[0])
			#vector_math_001.Vector -> vector_math_002.Vector
			backbone_nh.links.new(vector_math_001.outputs[0], vector_math_002.inputs[0])
			#named_attribute.Attribute -> vector_math_006.Vector
			backbone_nh.links.new(named_attribute.outputs[0], vector_math_006.inputs[0])
			#vector_math_006.Vector -> group_output_3.H
			backbone_nh.links.new(vector_math_006.outputs[0], group_output_3.inputs[0])
			#group_input_3.Value -> group_003.Value
			backbone_nh.links.new(group_input_3.outputs[0], group_003.inputs[0])
			#vector_math_005.Vector -> vector_math_007.Vector
			backbone_nh.links.new(vector_math_005.outputs[0], vector_math_007.inputs[0])
			#vector_math_007.Vector -> vector_math_004.Vector
			backbone_nh.links.new(vector_math_007.outputs[0], vector_math_004.inputs[0])
			return backbone_nh

		backbone_nh = backbone_nh_node_group()

		#initialize mn_topo_backbone node group
		def mn_topo_backbone_node_group():
			mn_topo_backbone = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "MN_topo_backbone")

			mn_topo_backbone.color_tag = 'NONE'
			mn_topo_backbone.description = ""

			
			#mn_topo_backbone interface
			#Socket O
			o_socket = mn_topo_backbone.interface.new_socket(name = "O", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			o_socket.default_value = (0.0, 0.0, 0.0)
			o_socket.min_value = -3.4028234663852886e+38
			o_socket.max_value = 3.4028234663852886e+38
			o_socket.subtype = 'NONE'
			o_socket.attribute_domain = 'POINT'
			
			#Socket C
			c_socket = mn_topo_backbone.interface.new_socket(name = "C", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			c_socket.default_value = (0.0, 0.0, 0.0)
			c_socket.min_value = -3.4028234663852886e+38
			c_socket.max_value = 3.4028234663852886e+38
			c_socket.subtype = 'NONE'
			c_socket.attribute_domain = 'POINT'
			
			#Socket CA
			ca_socket = mn_topo_backbone.interface.new_socket(name = "CA", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			ca_socket.default_value = (0.0, 0.0, 0.0)
			ca_socket.min_value = -3.4028234663852886e+38
			ca_socket.max_value = 3.4028234663852886e+38
			ca_socket.subtype = 'NONE'
			ca_socket.attribute_domain = 'POINT'
			
			#Socket N
			n_socket = mn_topo_backbone.interface.new_socket(name = "N", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			n_socket.default_value = (0.0, 0.0, 0.0)
			n_socket.min_value = -3.4028234663852886e+38
			n_socket.max_value = 3.4028234663852886e+38
			n_socket.subtype = 'NONE'
			n_socket.attribute_domain = 'POINT'
			
			#Socket NH
			nh_socket = mn_topo_backbone.interface.new_socket(name = "NH", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			nh_socket.default_value = (0.0, 0.0, 0.0)
			nh_socket.min_value = -3.4028234663852886e+38
			nh_socket.max_value = 3.4028234663852886e+38
			nh_socket.subtype = 'NONE'
			nh_socket.attribute_domain = 'POINT'
			
			#Socket Offset
			offset_socket_1 = mn_topo_backbone.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket_1.default_value = 0
			offset_socket_1.min_value = -2147483648
			offset_socket_1.max_value = 2147483647
			offset_socket_1.subtype = 'NONE'
			offset_socket_1.attribute_domain = 'POINT'
			
			
			#initialize mn_topo_backbone nodes
			#node Group Output
			group_output_4 = mn_topo_backbone.nodes.new("NodeGroupOutput")
			group_output_4.name = "Group Output"
			group_output_4.is_active_output = True
			
			#node Group Input
			group_input_4 = mn_topo_backbone.nodes.new("NodeGroupInput")
			group_input_4.name = "Group Input"
			
			#node Named Attribute.001
			named_attribute_001_1 = mn_topo_backbone.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001_1.name = "Named Attribute.001"
			named_attribute_001_1.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_001_1.inputs[0].default_value = "backbone_O"
			
			#node Named Attribute.002
			named_attribute_002_1 = mn_topo_backbone.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002_1.name = "Named Attribute.002"
			named_attribute_002_1.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_002_1.inputs[0].default_value = "backbone_C"
			
			#node Evaluate at Index
			evaluate_at_index_1 = mn_topo_backbone.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_1.name = "Evaluate at Index"
			evaluate_at_index_1.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_1.domain = 'POINT'
			
			#node Math
			math_2 = mn_topo_backbone.nodes.new("ShaderNodeMath")
			math_2.name = "Math"
			math_2.operation = 'ADD'
			math_2.use_clamp = False
			
			#node Index
			index = mn_topo_backbone.nodes.new("GeometryNodeInputIndex")
			index.name = "Index"
			
			#node Evaluate at Index.001
			evaluate_at_index_001 = mn_topo_backbone.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001.name = "Evaluate at Index.001"
			evaluate_at_index_001.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_001.domain = 'POINT'
			
			#node Named Attribute.003
			named_attribute_003 = mn_topo_backbone.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_003.name = "Named Attribute.003"
			named_attribute_003.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_003.inputs[0].default_value = "backbone_CA"
			
			#node Evaluate at Index.002
			evaluate_at_index_002 = mn_topo_backbone.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_002.name = "Evaluate at Index.002"
			evaluate_at_index_002.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_002.domain = 'POINT'
			
			#node Evaluate at Index.003
			evaluate_at_index_003 = mn_topo_backbone.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_003.name = "Evaluate at Index.003"
			evaluate_at_index_003.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_003.domain = 'POINT'
			
			#node Named Attribute.004
			named_attribute_004 = mn_topo_backbone.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_004.name = "Named Attribute.004"
			named_attribute_004.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_004.inputs[0].default_value = "backbone_N"
			
			#node Reroute
			reroute = mn_topo_backbone.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Group
			group_1 = mn_topo_backbone.nodes.new("GeometryNodeGroup")
			group_1.name = "Group"
			group_1.node_tree = backbone_nh
			#Socket_1
			group_1.inputs[0].default_value = 1.0099999904632568
			
			#node Evaluate at Index.004
			evaluate_at_index_004 = mn_topo_backbone.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_004.name = "Evaluate at Index.004"
			evaluate_at_index_004.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_004.domain = 'POINT'
			
			#node Named Attribute.005
			named_attribute_005 = mn_topo_backbone.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_005.name = "Named Attribute.005"
			named_attribute_005.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_005.inputs[0].default_value = "backbone_NH"
			
			#node Switch
			switch = mn_topo_backbone.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'VECTOR'
			
			#node Boolean Math
			boolean_math = mn_topo_backbone.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'NOT'
			
			
			
			
			#Set locations
			group_output_4.location = (320.0, -220.0)
			group_input_4.location = (-520.0, -260.0)
			named_attribute_001_1.location = (-300.0, 40.0)
			named_attribute_002_1.location = (-300.0, -100.0)
			evaluate_at_index_1.location = (80.0, -14.04681396484375)
			math_2.location = (-260.0, -260.0)
			index.location = (-520.0, -360.0)
			evaluate_at_index_001.location = (80.0, -170.47593688964844)
			named_attribute_003.location = (-300.0, -460.0)
			evaluate_at_index_002.location = (80.0, -326.90509033203125)
			evaluate_at_index_003.location = (80.0, -480.0)
			named_attribute_004.location = (-300.0, -600.0)
			reroute.location = (20.0, -340.0)
			group_1.location = (-640.0, -920.0)
			evaluate_at_index_004.location = (77.81956481933594, -655.5125732421875)
			named_attribute_005.location = (-640.0, -780.0)
			switch.location = (-240.0, -780.0)
			boolean_math.location = (-420.0, -780.0)
			
			#Set dimensions
			group_output_4.width, group_output_4.height = 140.0, 100.0
			group_input_4.width, group_input_4.height = 140.0, 100.0
			named_attribute_001_1.width, named_attribute_001_1.height = 186.42977905273438, 100.0
			named_attribute_002_1.width, named_attribute_002_1.height = 186.42977905273438, 100.0
			evaluate_at_index_1.width, evaluate_at_index_1.height = 140.0, 100.0
			math_2.width, math_2.height = 140.0, 100.0
			index.width, index.height = 140.0, 100.0
			evaluate_at_index_001.width, evaluate_at_index_001.height = 140.0, 100.0
			named_attribute_003.width, named_attribute_003.height = 186.42977905273438, 100.0
			evaluate_at_index_002.width, evaluate_at_index_002.height = 140.0, 100.0
			evaluate_at_index_003.width, evaluate_at_index_003.height = 140.0, 100.0
			named_attribute_004.width, named_attribute_004.height = 186.42977905273438, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			group_1.width, group_1.height = 186.0294189453125, 100.0
			evaluate_at_index_004.width, evaluate_at_index_004.height = 140.0, 100.0
			named_attribute_005.width, named_attribute_005.height = 186.42977905273438, 100.0
			switch.width, switch.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			
			#initialize mn_topo_backbone links
			#named_attribute_001_1.Attribute -> evaluate_at_index_1.Value
			mn_topo_backbone.links.new(named_attribute_001_1.outputs[0], evaluate_at_index_1.inputs[1])
			#reroute.Output -> evaluate_at_index_1.Index
			mn_topo_backbone.links.new(reroute.outputs[0], evaluate_at_index_1.inputs[0])
			#group_input_4.Offset -> math_2.Value
			mn_topo_backbone.links.new(group_input_4.outputs[0], math_2.inputs[0])
			#reroute.Output -> evaluate_at_index_001.Index
			mn_topo_backbone.links.new(reroute.outputs[0], evaluate_at_index_001.inputs[0])
			#named_attribute_002_1.Attribute -> evaluate_at_index_001.Value
			mn_topo_backbone.links.new(named_attribute_002_1.outputs[0], evaluate_at_index_001.inputs[1])
			#reroute.Output -> evaluate_at_index_002.Index
			mn_topo_backbone.links.new(reroute.outputs[0], evaluate_at_index_002.inputs[0])
			#named_attribute_003.Attribute -> evaluate_at_index_002.Value
			mn_topo_backbone.links.new(named_attribute_003.outputs[0], evaluate_at_index_002.inputs[1])
			#reroute.Output -> evaluate_at_index_003.Index
			mn_topo_backbone.links.new(reroute.outputs[0], evaluate_at_index_003.inputs[0])
			#named_attribute_004.Attribute -> evaluate_at_index_003.Value
			mn_topo_backbone.links.new(named_attribute_004.outputs[0], evaluate_at_index_003.inputs[1])
			#index.Index -> math_2.Value
			mn_topo_backbone.links.new(index.outputs[0], math_2.inputs[1])
			#math_2.Value -> reroute.Input
			mn_topo_backbone.links.new(math_2.outputs[0], reroute.inputs[0])
			#evaluate_at_index_003.Value -> group_output_4.N
			mn_topo_backbone.links.new(evaluate_at_index_003.outputs[0], group_output_4.inputs[3])
			#evaluate_at_index_002.Value -> group_output_4.CA
			mn_topo_backbone.links.new(evaluate_at_index_002.outputs[0], group_output_4.inputs[2])
			#evaluate_at_index_001.Value -> group_output_4.C
			mn_topo_backbone.links.new(evaluate_at_index_001.outputs[0], group_output_4.inputs[1])
			#evaluate_at_index_1.Value -> group_output_4.O
			mn_topo_backbone.links.new(evaluate_at_index_1.outputs[0], group_output_4.inputs[0])
			#reroute.Output -> evaluate_at_index_004.Index
			mn_topo_backbone.links.new(reroute.outputs[0], evaluate_at_index_004.inputs[0])
			#evaluate_at_index_004.Value -> group_output_4.NH
			mn_topo_backbone.links.new(evaluate_at_index_004.outputs[0], group_output_4.inputs[4])
			#group_1.H -> switch.True
			mn_topo_backbone.links.new(group_1.outputs[0], switch.inputs[2])
			#switch.Output -> evaluate_at_index_004.Value
			mn_topo_backbone.links.new(switch.outputs[0], evaluate_at_index_004.inputs[1])
			#named_attribute_005.Exists -> boolean_math.Boolean
			mn_topo_backbone.links.new(named_attribute_005.outputs[1], boolean_math.inputs[0])
			#boolean_math.Boolean -> switch.Switch
			mn_topo_backbone.links.new(boolean_math.outputs[0], switch.inputs[0])
			#named_attribute_005.Attribute -> switch.False
			mn_topo_backbone.links.new(named_attribute_005.outputs[0], switch.inputs[1])
			return mn_topo_backbone

		mn_topo_backbone = mn_topo_backbone_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "MN_topo_backbone", type = 'NODES')
		mod.node_group = mn_topo_backbone
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(MN_topo_backbone.bl_idname)
			
def register():
	bpy.utils.register_class(MN_topo_backbone)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(MN_topo_backbone)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
