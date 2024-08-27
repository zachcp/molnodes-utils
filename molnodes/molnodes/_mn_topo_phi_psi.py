bl_info = {
	"name" : ".MN_topo_phi_psi",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _MN_topo_phi_psi(bpy.types.Operator):
	bl_idname = "node._mn_topo_phi_psi"
	bl_label = ".MN_topo_phi_psi"
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

		#initialize vector_angle node group
		def vector_angle_node_group():
			vector_angle = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Vector Angle")

			vector_angle.color_tag = 'VECTOR'
			vector_angle.description = ""

			
			#vector_angle interface
			#Socket Angle
			angle_socket = vector_angle.interface.new_socket(name = "Angle", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			angle_socket.default_value = 0.0
			angle_socket.min_value = -3.4028234663852886e+38
			angle_socket.max_value = 3.4028234663852886e+38
			angle_socket.subtype = 'ANGLE'
			angle_socket.attribute_domain = 'POINT'
			angle_socket.description = "Angle between the two given vectors in radians"
			
			#Socket A
			a_socket = vector_angle.interface.new_socket(name = "A", in_out='INPUT', socket_type = 'NodeSocketVector')
			a_socket.default_value = (0.0, 0.0, 0.0)
			a_socket.min_value = -10000.0
			a_socket.max_value = 10000.0
			a_socket.subtype = 'NONE'
			a_socket.attribute_domain = 'POINT'
			
			#Socket B
			b_socket = vector_angle.interface.new_socket(name = "B", in_out='INPUT', socket_type = 'NodeSocketVector')
			b_socket.default_value = (0.0, 0.0, 0.0)
			b_socket.min_value = -10000.0
			b_socket.max_value = 10000.0
			b_socket.subtype = 'NONE'
			b_socket.attribute_domain = 'POINT'
			
			
			#initialize vector_angle nodes
			#node Group Input
			group_input_5 = vector_angle.nodes.new("NodeGroupInput")
			group_input_5.name = "Group Input"
			
			#node Vector Math.002
			vector_math_002_1 = vector_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_002_1.name = "Vector Math.002"
			vector_math_002_1.operation = 'NORMALIZE'
			
			#node Vector Math.001
			vector_math_001_1 = vector_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_001_1.name = "Vector Math.001"
			vector_math_001_1.operation = 'NORMALIZE'
			
			#node Vector Math
			vector_math_1 = vector_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_1.name = "Vector Math"
			vector_math_1.operation = 'DOT_PRODUCT'
			
			#node Math
			math_3 = vector_angle.nodes.new("ShaderNodeMath")
			math_3.name = "Math"
			math_3.operation = 'ARCCOSINE'
			math_3.use_clamp = False
			
			#node Group Output
			group_output_5 = vector_angle.nodes.new("NodeGroupOutput")
			group_output_5.name = "Group Output"
			group_output_5.is_active_output = True
			
			
			
			
			#Set locations
			group_input_5.location = (-360.0, 0.0)
			vector_math_002_1.location = (-160.0, -60.0)
			vector_math_001_1.location = (-160.0, 60.0)
			vector_math_1.location = (0.0, 60.0)
			math_3.location = (160.0, 60.0)
			group_output_5.location = (340.0, 60.0)
			
			#Set dimensions
			group_input_5.width, group_input_5.height = 140.0, 100.0
			vector_math_002_1.width, vector_math_002_1.height = 140.0, 100.0
			vector_math_001_1.width, vector_math_001_1.height = 140.0, 100.0
			vector_math_1.width, vector_math_1.height = 140.0, 100.0
			math_3.width, math_3.height = 140.0, 100.0
			group_output_5.width, group_output_5.height = 140.0, 100.0
			
			#initialize vector_angle links
			#vector_math_1.Value -> math_3.Value
			vector_angle.links.new(vector_math_1.outputs[1], math_3.inputs[0])
			#vector_math_002_1.Vector -> vector_math_1.Vector
			vector_angle.links.new(vector_math_002_1.outputs[0], vector_math_1.inputs[1])
			#vector_math_001_1.Vector -> vector_math_1.Vector
			vector_angle.links.new(vector_math_001_1.outputs[0], vector_math_1.inputs[0])
			#math_3.Value -> group_output_5.Angle
			vector_angle.links.new(math_3.outputs[0], group_output_5.inputs[0])
			#group_input_5.A -> vector_math_001_1.Vector
			vector_angle.links.new(group_input_5.outputs[0], vector_math_001_1.inputs[0])
			#group_input_5.B -> vector_math_002_1.Vector
			vector_angle.links.new(group_input_5.outputs[1], vector_math_002_1.inputs[0])
			return vector_angle

		vector_angle = vector_angle_node_group()

		#initialize dihedral_angle node group
		def dihedral_angle_node_group():
			dihedral_angle = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Dihedral Angle")

			dihedral_angle.color_tag = 'VECTOR'
			dihedral_angle.description = ""

			
			#dihedral_angle interface
			#Socket Angle
			angle_socket_1 = dihedral_angle.interface.new_socket(name = "Angle", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			angle_socket_1.default_value = 0.0
			angle_socket_1.min_value = -3.4028234663852886e+38
			angle_socket_1.max_value = 3.4028234663852886e+38
			angle_socket_1.subtype = 'ANGLE'
			angle_socket_1.attribute_domain = 'POINT'
			angle_socket_1.description = "The angle between the vectors AB and CD, when made perpendicular to BC."
			
			#Socket BA⟂(BC)
			ba__bc__socket = dihedral_angle.interface.new_socket(name = "BA⟂(BC)", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			ba__bc__socket.default_value = (0.0, 0.0, 0.0)
			ba__bc__socket.min_value = -3.4028234663852886e+38
			ba__bc__socket.max_value = 3.4028234663852886e+38
			ba__bc__socket.subtype = 'NONE'
			ba__bc__socket.attribute_domain = 'POINT'
			ba__bc__socket.description = "The vector BA when made perpendicular to  the axis BC"
			
			#Socket CD⟂(BC)
			cd__bc__socket = dihedral_angle.interface.new_socket(name = "CD⟂(BC)", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			cd__bc__socket.default_value = (0.0, 0.0, 0.0)
			cd__bc__socket.min_value = -3.4028234663852886e+38
			cd__bc__socket.max_value = 3.4028234663852886e+38
			cd__bc__socket.subtype = 'NONE'
			cd__bc__socket.attribute_domain = 'POINT'
			cd__bc__socket.description = "The Vector CD when makde perpendicular to the axis BC"
			
			#Socket BC
			bc_socket = dihedral_angle.interface.new_socket(name = "BC", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			bc_socket.default_value = (0.0, 0.0, 0.0)
			bc_socket.min_value = -3.4028234663852886e+38
			bc_socket.max_value = 3.4028234663852886e+38
			bc_socket.subtype = 'NONE'
			bc_socket.attribute_domain = 'POINT'
			bc_socket.description = "The axis vector BC"
			
			#Socket A
			a_socket_1 = dihedral_angle.interface.new_socket(name = "A", in_out='INPUT', socket_type = 'NodeSocketVector')
			a_socket_1.default_value = (0.0, 0.0, 0.0)
			a_socket_1.min_value = -3.4028234663852886e+38
			a_socket_1.max_value = 3.4028234663852886e+38
			a_socket_1.subtype = 'NONE'
			a_socket_1.attribute_domain = 'POINT'
			a_socket_1.description = "First vector for the calculation, which draws a line to B"
			
			#Socket B
			b_socket_1 = dihedral_angle.interface.new_socket(name = "B", in_out='INPUT', socket_type = 'NodeSocketVector')
			b_socket_1.default_value = (0.0, 0.0, 0.0)
			b_socket_1.min_value = -3.4028234663852886e+38
			b_socket_1.max_value = 3.4028234663852886e+38
			b_socket_1.subtype = 'NONE'
			b_socket_1.attribute_domain = 'POINT'
			b_socket_1.description = "Second vector for the calculation, which receives a line from A and draws a line to C"
			
			#Socket C
			c_socket_1 = dihedral_angle.interface.new_socket(name = "C", in_out='INPUT', socket_type = 'NodeSocketVector')
			c_socket_1.default_value = (0.0, 0.0, 0.0)
			c_socket_1.min_value = -3.4028234663852886e+38
			c_socket_1.max_value = 3.4028234663852886e+38
			c_socket_1.subtype = 'NONE'
			c_socket_1.attribute_domain = 'POINT'
			c_socket_1.description = "Third vector for the calculation, which receives a line from B and draws a line to D"
			
			#Socket D
			d_socket = dihedral_angle.interface.new_socket(name = "D", in_out='INPUT', socket_type = 'NodeSocketVector')
			d_socket.default_value = (0.0, 0.0, 0.0)
			d_socket.min_value = -3.4028234663852886e+38
			d_socket.max_value = 3.4028234663852886e+38
			d_socket.subtype = 'NONE'
			d_socket.attribute_domain = 'POINT'
			d_socket.description = "Last vector for the calculation, which is the end point of the line from D"
			
			
			#initialize dihedral_angle nodes
			#node Vector Math.003
			vector_math_003_1 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_003_1.name = "Vector Math.003"
			vector_math_003_1.operation = 'SUBTRACT'
			
			#node Vector Math.004
			vector_math_004_1 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_004_1.name = "Vector Math.004"
			vector_math_004_1.operation = 'SUBTRACT'
			
			#node Vector Math.006
			vector_math_006_1 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_006_1.name = "Vector Math.006"
			vector_math_006_1.operation = 'SUBTRACT'
			
			#node Vector Math.007
			vector_math_007_1 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_007_1.name = "Vector Math.007"
			vector_math_007_1.operation = 'PROJECT'
			
			#node Vector Math.009
			vector_math_009 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_009.name = "Vector Math.009"
			vector_math_009.operation = 'PROJECT'
			
			#node Vector Math.008
			vector_math_008 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_008.name = "Vector Math.008"
			vector_math_008.operation = 'SUBTRACT'
			
			#node Vector Math.010
			vector_math_010 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_010.name = "Vector Math.010"
			vector_math_010.operation = 'SUBTRACT'
			
			#node MN_utils_vector_angle.002
			mn_utils_vector_angle_002 = dihedral_angle.nodes.new("GeometryNodeGroup")
			mn_utils_vector_angle_002.label = "Vector Angle"
			mn_utils_vector_angle_002.name = "MN_utils_vector_angle.002"
			mn_utils_vector_angle_002.node_tree = vector_angle
			
			#node Group Output
			group_output_6 = dihedral_angle.nodes.new("NodeGroupOutput")
			group_output_6.name = "Group Output"
			group_output_6.is_active_output = True
			
			#node Reroute.002
			reroute_002 = dihedral_angle.nodes.new("NodeReroute")
			reroute_002.name = "Reroute.002"
			#node Reroute.001
			reroute_001 = dihedral_angle.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			#node Vector Math
			vector_math_2 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_2.name = "Vector Math"
			vector_math_2.operation = 'CROSS_PRODUCT'
			
			#node Vector Math.001
			vector_math_001_2 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_001_2.name = "Vector Math.001"
			vector_math_001_2.operation = 'DOT_PRODUCT'
			
			#node Math.001
			math_001_1 = dihedral_angle.nodes.new("ShaderNodeMath")
			math_001_1.name = "Math.001"
			math_001_1.operation = 'SIGN'
			math_001_1.use_clamp = False
			
			#node Reroute
			reroute_1 = dihedral_angle.nodes.new("NodeReroute")
			reroute_1.name = "Reroute"
			#node Math
			math_4 = dihedral_angle.nodes.new("ShaderNodeMath")
			math_4.name = "Math"
			math_4.operation = 'MULTIPLY'
			math_4.use_clamp = False
			
			#node Group Input.003
			group_input_003 = dihedral_angle.nodes.new("NodeGroupInput")
			group_input_003.name = "Group Input.003"
			group_input_003.outputs[0].hide = True
			group_input_003.outputs[1].hide = True
			group_input_003.outputs[2].hide = True
			group_input_003.outputs[4].hide = True
			
			#node Group Input.001
			group_input_001 = dihedral_angle.nodes.new("NodeGroupInput")
			group_input_001.name = "Group Input.001"
			group_input_001.outputs[1].hide = True
			group_input_001.outputs[2].hide = True
			group_input_001.outputs[3].hide = True
			group_input_001.outputs[4].hide = True
			
			#node Group Input
			group_input_6 = dihedral_angle.nodes.new("NodeGroupInput")
			group_input_6.name = "Group Input"
			group_input_6.outputs[0].hide = True
			group_input_6.outputs[2].hide = True
			group_input_6.outputs[3].hide = True
			group_input_6.outputs[4].hide = True
			
			#node Group Input.002
			group_input_002 = dihedral_angle.nodes.new("NodeGroupInput")
			group_input_002.name = "Group Input.002"
			group_input_002.outputs[0].hide = True
			group_input_002.outputs[1].hide = True
			group_input_002.outputs[3].hide = True
			group_input_002.outputs[4].hide = True
			
			
			
			
			#Set locations
			vector_math_003_1.location = (-142.68453979492188, 25.911895751953125)
			vector_math_004_1.location = (-140.0, 440.0)
			vector_math_006_1.location = (-140.0, 180.0)
			vector_math_007_1.location = (80.0, 320.0)
			vector_math_009.location = (80.0, -80.0)
			vector_math_008.location = (80.0, 460.0)
			vector_math_010.location = (80.0, 60.0)
			mn_utils_vector_angle_002.location = (420.0, 420.0)
			group_output_6.location = (920.0, 320.0)
			reroute_002.location = (300.0, 260.0)
			reroute_001.location = (300.0, 240.0)
			vector_math_2.location = (420.0, 180.0)
			vector_math_001_2.location = (420.0, 40.0)
			math_001_1.location = (580.0, 40.0)
			reroute_1.location = (300.0, 220.0)
			math_4.location = (640.0, 420.0)
			group_input_003.location = (-440.0, 0.0)
			group_input_001.location = (-440.0, 420.0)
			group_input_6.location = (-440.0, 280.0)
			group_input_002.location = (-440.0, 140.0)
			
			#Set dimensions
			vector_math_003_1.width, vector_math_003_1.height = 140.0, 100.0
			vector_math_004_1.width, vector_math_004_1.height = 140.0, 100.0
			vector_math_006_1.width, vector_math_006_1.height = 140.0, 100.0
			vector_math_007_1.width, vector_math_007_1.height = 140.0, 100.0
			vector_math_009.width, vector_math_009.height = 140.0, 100.0
			vector_math_008.width, vector_math_008.height = 140.0, 100.0
			vector_math_010.width, vector_math_010.height = 140.0, 100.0
			mn_utils_vector_angle_002.width, mn_utils_vector_angle_002.height = 200.0, 100.0
			group_output_6.width, group_output_6.height = 140.0, 100.0
			reroute_002.width, reroute_002.height = 16.0, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			vector_math_2.width, vector_math_2.height = 140.0, 100.0
			vector_math_001_2.width, vector_math_001_2.height = 140.0, 100.0
			math_001_1.width, math_001_1.height = 140.0, 100.0
			reroute_1.width, reroute_1.height = 16.0, 100.0
			math_4.width, math_4.height = 140.0, 100.0
			group_input_003.width, group_input_003.height = 140.0, 100.0
			group_input_001.width, group_input_001.height = 140.0, 100.0
			group_input_6.width, group_input_6.height = 140.0, 100.0
			group_input_002.width, group_input_002.height = 140.0, 100.0
			
			#initialize dihedral_angle links
			#vector_math_007_1.Vector -> vector_math_008.Vector
			dihedral_angle.links.new(vector_math_007_1.outputs[0], vector_math_008.inputs[1])
			#vector_math_009.Vector -> vector_math_010.Vector
			dihedral_angle.links.new(vector_math_009.outputs[0], vector_math_010.inputs[1])
			#vector_math_004_1.Vector -> vector_math_007_1.Vector
			dihedral_angle.links.new(vector_math_004_1.outputs[0], vector_math_007_1.inputs[0])
			#vector_math_006_1.Vector -> vector_math_007_1.Vector
			dihedral_angle.links.new(vector_math_006_1.outputs[0], vector_math_007_1.inputs[1])
			#reroute_002.Output -> mn_utils_vector_angle_002.A
			dihedral_angle.links.new(reroute_002.outputs[0], mn_utils_vector_angle_002.inputs[0])
			#vector_math_004_1.Vector -> vector_math_008.Vector
			dihedral_angle.links.new(vector_math_004_1.outputs[0], vector_math_008.inputs[0])
			#vector_math_003_1.Vector -> vector_math_010.Vector
			dihedral_angle.links.new(vector_math_003_1.outputs[0], vector_math_010.inputs[0])
			#vector_math_003_1.Vector -> vector_math_009.Vector
			dihedral_angle.links.new(vector_math_003_1.outputs[0], vector_math_009.inputs[0])
			#vector_math_006_1.Vector -> vector_math_009.Vector
			dihedral_angle.links.new(vector_math_006_1.outputs[0], vector_math_009.inputs[1])
			#vector_math_006_1.Vector -> reroute_1.Input
			dihedral_angle.links.new(vector_math_006_1.outputs[0], reroute_1.inputs[0])
			#reroute_001.Output -> mn_utils_vector_angle_002.B
			dihedral_angle.links.new(reroute_001.outputs[0], mn_utils_vector_angle_002.inputs[1])
			#vector_math_2.Vector -> vector_math_001_2.Vector
			dihedral_angle.links.new(vector_math_2.outputs[0], vector_math_001_2.inputs[0])
			#reroute_1.Output -> vector_math_001_2.Vector
			dihedral_angle.links.new(reroute_1.outputs[0], vector_math_001_2.inputs[1])
			#mn_utils_vector_angle_002.Angle -> math_4.Value
			dihedral_angle.links.new(mn_utils_vector_angle_002.outputs[0], math_4.inputs[0])
			#reroute_001.Output -> vector_math_2.Vector
			dihedral_angle.links.new(reroute_001.outputs[0], vector_math_2.inputs[1])
			#group_input_002.C -> vector_math_003_1.Vector
			dihedral_angle.links.new(group_input_002.outputs[2], vector_math_003_1.inputs[1])
			#group_input_6.B -> vector_math_004_1.Vector
			dihedral_angle.links.new(group_input_6.outputs[1], vector_math_004_1.inputs[1])
			#group_input_6.B -> vector_math_006_1.Vector
			dihedral_angle.links.new(group_input_6.outputs[1], vector_math_006_1.inputs[1])
			#group_input_002.C -> vector_math_006_1.Vector
			dihedral_angle.links.new(group_input_002.outputs[2], vector_math_006_1.inputs[0])
			#math_4.Value -> group_output_6.Angle
			dihedral_angle.links.new(math_4.outputs[0], group_output_6.inputs[0])
			#reroute_002.Output -> group_output_6.BA⟂(BC)
			dihedral_angle.links.new(reroute_002.outputs[0], group_output_6.inputs[1])
			#reroute_1.Output -> group_output_6.BC
			dihedral_angle.links.new(reroute_1.outputs[0], group_output_6.inputs[3])
			#reroute_001.Output -> group_output_6.CD⟂(BC)
			dihedral_angle.links.new(reroute_001.outputs[0], group_output_6.inputs[2])
			#reroute_002.Output -> vector_math_2.Vector
			dihedral_angle.links.new(reroute_002.outputs[0], vector_math_2.inputs[0])
			#vector_math_001_2.Value -> math_001_1.Value
			dihedral_angle.links.new(vector_math_001_2.outputs[1], math_001_1.inputs[0])
			#math_001_1.Value -> math_4.Value
			dihedral_angle.links.new(math_001_1.outputs[0], math_4.inputs[1])
			#vector_math_010.Vector -> reroute_001.Input
			dihedral_angle.links.new(vector_math_010.outputs[0], reroute_001.inputs[0])
			#vector_math_008.Vector -> reroute_002.Input
			dihedral_angle.links.new(vector_math_008.outputs[0], reroute_002.inputs[0])
			#group_input_001.A -> vector_math_004_1.Vector
			dihedral_angle.links.new(group_input_001.outputs[0], vector_math_004_1.inputs[0])
			#group_input_003.D -> vector_math_003_1.Vector
			dihedral_angle.links.new(group_input_003.outputs[3], vector_math_003_1.inputs[0])
			return dihedral_angle

		dihedral_angle = dihedral_angle_node_group()

		#initialize _mn_topo_phi_psi node group
		def _mn_topo_phi_psi_node_group():
			_mn_topo_phi_psi = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_topo_phi_psi")

			_mn_topo_phi_psi.color_tag = 'NONE'
			_mn_topo_phi_psi.description = ""

			
			#_mn_topo_phi_psi interface
			#Socket Angle
			angle_socket_2 = _mn_topo_phi_psi.interface.new_socket(name = "Angle", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			angle_socket_2.default_value = 0.0
			angle_socket_2.min_value = -3.4028234663852886e+38
			angle_socket_2.max_value = 3.4028234663852886e+38
			angle_socket_2.subtype = 'ANGLE'
			angle_socket_2.attribute_domain = 'POINT'
			
			#Socket BA⟂(BC)
			ba__bc__socket_1 = _mn_topo_phi_psi.interface.new_socket(name = "BA⟂(BC)", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			ba__bc__socket_1.default_value = (0.0, 0.0, 0.0)
			ba__bc__socket_1.min_value = -3.4028234663852886e+38
			ba__bc__socket_1.max_value = 3.4028234663852886e+38
			ba__bc__socket_1.subtype = 'NONE'
			ba__bc__socket_1.attribute_domain = 'POINT'
			
			#Socket CD⟂(BC)
			cd__bc__socket_1 = _mn_topo_phi_psi.interface.new_socket(name = "CD⟂(BC)", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			cd__bc__socket_1.default_value = (0.0, 0.0, 0.0)
			cd__bc__socket_1.min_value = -3.4028234663852886e+38
			cd__bc__socket_1.max_value = 3.4028234663852886e+38
			cd__bc__socket_1.subtype = 'NONE'
			cd__bc__socket_1.attribute_domain = 'POINT'
			
			#Socket BC
			bc_socket_1 = _mn_topo_phi_psi.interface.new_socket(name = "BC", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			bc_socket_1.default_value = (0.0, 0.0, 0.0)
			bc_socket_1.min_value = -3.4028234663852886e+38
			bc_socket_1.max_value = 3.4028234663852886e+38
			bc_socket_1.subtype = 'NONE'
			bc_socket_1.attribute_domain = 'POINT'
			
			#Socket A
			a_socket_2 = _mn_topo_phi_psi.interface.new_socket(name = "A", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			a_socket_2.default_value = (0.0, 0.0, 0.0)
			a_socket_2.min_value = -3.4028234663852886e+38
			a_socket_2.max_value = 3.4028234663852886e+38
			a_socket_2.subtype = 'NONE'
			a_socket_2.attribute_domain = 'POINT'
			
			#Socket B
			b_socket_2 = _mn_topo_phi_psi.interface.new_socket(name = "B", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			b_socket_2.default_value = (0.0, 0.0, 0.0)
			b_socket_2.min_value = -3.4028234663852886e+38
			b_socket_2.max_value = 3.4028234663852886e+38
			b_socket_2.subtype = 'NONE'
			b_socket_2.attribute_domain = 'POINT'
			
			#Socket C
			c_socket_2 = _mn_topo_phi_psi.interface.new_socket(name = "C", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			c_socket_2.default_value = (0.0, 0.0, 0.0)
			c_socket_2.min_value = -3.4028234663852886e+38
			c_socket_2.max_value = 3.4028234663852886e+38
			c_socket_2.subtype = 'NONE'
			c_socket_2.attribute_domain = 'POINT'
			
			#Socket D
			d_socket_1 = _mn_topo_phi_psi.interface.new_socket(name = "D", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			d_socket_1.default_value = (0.0, 0.0, 0.0)
			d_socket_1.min_value = -3.4028234663852886e+38
			d_socket_1.max_value = 3.4028234663852886e+38
			d_socket_1.subtype = 'NONE'
			d_socket_1.attribute_domain = 'POINT'
			
			#Socket Menu
			menu_socket = _mn_topo_phi_psi.interface.new_socket(name = "Menu", in_out='INPUT', socket_type = 'NodeSocketMenu')
			menu_socket.default_value = "Phi"
			menu_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_topo_phi_psi nodes
			#node Group Output
			group_output_7 = _mn_topo_phi_psi.nodes.new("NodeGroupOutput")
			group_output_7.name = "Group Output"
			group_output_7.is_active_output = True
			
			#node Group Input
			group_input_7 = _mn_topo_phi_psi.nodes.new("NodeGroupInput")
			group_input_7.name = "Group Input"
			
			#node Group.005
			group_005 = _mn_topo_phi_psi.nodes.new("GeometryNodeGroup")
			group_005.name = "Group.005"
			group_005.node_tree = mn_topo_backbone
			#Socket_3
			group_005.inputs[0].default_value = 1
			
			#node Group.007
			group_007 = _mn_topo_phi_psi.nodes.new("GeometryNodeGroup")
			group_007.name = "Group.007"
			group_007.node_tree = mn_topo_backbone
			#Socket_3
			group_007.inputs[0].default_value = -1
			
			#node Group.008
			group_008 = _mn_topo_phi_psi.nodes.new("GeometryNodeGroup")
			group_008.name = "Group.008"
			group_008.node_tree = mn_topo_backbone
			#Socket_3
			group_008.inputs[0].default_value = 0
			
			#node Group.009
			group_009 = _mn_topo_phi_psi.nodes.new("GeometryNodeGroup")
			group_009.name = "Group.009"
			group_009.node_tree = dihedral_angle
			
			#node Menu Switch
			menu_switch = _mn_topo_phi_psi.nodes.new("GeometryNodeMenuSwitch")
			menu_switch.name = "Menu Switch"
			menu_switch.active_index = 1
			menu_switch.data_type = 'INT'
			menu_switch.enum_items.clear()
			menu_switch.enum_items.new("Phi")
			menu_switch.enum_items[0].description = ""
			menu_switch.enum_items.new("Psi")
			menu_switch.enum_items[1].description = ""
			#Item_0
			menu_switch.inputs[1].default_value = 0
			#Item_1
			menu_switch.inputs[2].default_value = 1
			
			#node Index Switch
			index_switch = _mn_topo_phi_psi.nodes.new("GeometryNodeIndexSwitch")
			index_switch.name = "Index Switch"
			index_switch.data_type = 'VECTOR'
			index_switch.index_switch_items.clear()
			index_switch.index_switch_items.new()
			index_switch.index_switch_items.new()
			
			#node Index Switch.001
			index_switch_001 = _mn_topo_phi_psi.nodes.new("GeometryNodeIndexSwitch")
			index_switch_001.name = "Index Switch.001"
			index_switch_001.data_type = 'VECTOR'
			index_switch_001.index_switch_items.clear()
			index_switch_001.index_switch_items.new()
			index_switch_001.index_switch_items.new()
			
			#node Index Switch.002
			index_switch_002 = _mn_topo_phi_psi.nodes.new("GeometryNodeIndexSwitch")
			index_switch_002.name = "Index Switch.002"
			index_switch_002.data_type = 'VECTOR'
			index_switch_002.index_switch_items.clear()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			
			
			
			
			#Set locations
			group_output_7.location = (698.508544921875, 198.78929138183594)
			group_input_7.location = (-520.0, 280.0)
			group_005.location = (-380.0, -320.0)
			group_007.location = (-380.0, -120.0)
			group_008.location = (-380.0, 80.0)
			group_009.location = (272.33380126953125, 98.96731567382812)
			menu_switch.location = (-340.0, 260.0)
			index_switch.location = (-20.0, 140.0)
			index_switch_001.location = (-20.0, -100.0)
			index_switch_002.location = (-20.0, -280.0)
			
			#Set dimensions
			group_output_7.width, group_output_7.height = 140.0, 100.0
			group_input_7.width, group_input_7.height = 140.0, 100.0
			group_005.width, group_005.height = 171.90289306640625, 100.0
			group_007.width, group_007.height = 171.90289306640625, 100.0
			group_008.width, group_008.height = 171.90289306640625, 100.0
			group_009.width, group_009.height = 299.8184509277344, 100.0
			menu_switch.width, menu_switch.height = 140.0, 100.0
			index_switch.width, index_switch.height = 140.0, 100.0
			index_switch_001.width, index_switch_001.height = 140.0, 100.0
			index_switch_002.width, index_switch_002.height = 140.0, 100.0
			
			#initialize _mn_topo_phi_psi links
			#group_008.CA -> group_009.B
			_mn_topo_phi_psi.links.new(group_008.outputs[2], group_009.inputs[1])
			#index_switch_002.Output -> group_009.D
			_mn_topo_phi_psi.links.new(index_switch_002.outputs[0], group_009.inputs[3])
			#index_switch.Output -> group_009.A
			_mn_topo_phi_psi.links.new(index_switch.outputs[0], group_009.inputs[0])
			#index_switch_001.Output -> group_009.C
			_mn_topo_phi_psi.links.new(index_switch_001.outputs[0], group_009.inputs[2])
			#group_009.Angle -> group_output_7.Angle
			_mn_topo_phi_psi.links.new(group_009.outputs[0], group_output_7.inputs[0])
			#group_009.BA⟂(BC) -> group_output_7.BA⟂(BC)
			_mn_topo_phi_psi.links.new(group_009.outputs[1], group_output_7.inputs[1])
			#group_009.BC -> group_output_7.BC
			_mn_topo_phi_psi.links.new(group_009.outputs[3], group_output_7.inputs[3])
			#index_switch.Output -> group_output_7.A
			_mn_topo_phi_psi.links.new(index_switch.outputs[0], group_output_7.inputs[4])
			#group_008.CA -> group_output_7.B
			_mn_topo_phi_psi.links.new(group_008.outputs[2], group_output_7.inputs[5])
			#index_switch_001.Output -> group_output_7.C
			_mn_topo_phi_psi.links.new(index_switch_001.outputs[0], group_output_7.inputs[6])
			#index_switch_002.Output -> group_output_7.D
			_mn_topo_phi_psi.links.new(index_switch_002.outputs[0], group_output_7.inputs[7])
			#group_009.CD⟂(BC) -> group_output_7.CD⟂(BC)
			_mn_topo_phi_psi.links.new(group_009.outputs[2], group_output_7.inputs[2])
			#menu_switch.Output -> index_switch.Index
			_mn_topo_phi_psi.links.new(menu_switch.outputs[0], index_switch.inputs[0])
			#group_input_7.Menu -> menu_switch.Menu
			_mn_topo_phi_psi.links.new(group_input_7.outputs[0], menu_switch.inputs[0])
			#group_008.C -> index_switch.0
			_mn_topo_phi_psi.links.new(group_008.outputs[1], index_switch.inputs[1])
			#menu_switch.Output -> index_switch_001.Index
			_mn_topo_phi_psi.links.new(menu_switch.outputs[0], index_switch_001.inputs[0])
			#group_008.N -> index_switch_001.0
			_mn_topo_phi_psi.links.new(group_008.outputs[3], index_switch_001.inputs[1])
			#group_008.C -> index_switch_001.1
			_mn_topo_phi_psi.links.new(group_008.outputs[1], index_switch_001.inputs[2])
			#menu_switch.Output -> index_switch_002.Index
			_mn_topo_phi_psi.links.new(menu_switch.outputs[0], index_switch_002.inputs[0])
			#group_007.C -> index_switch_002.0
			_mn_topo_phi_psi.links.new(group_007.outputs[1], index_switch_002.inputs[1])
			#group_005.N -> index_switch_002.1
			_mn_topo_phi_psi.links.new(group_005.outputs[3], index_switch_002.inputs[2])
			#group_008.N -> index_switch.1
			_mn_topo_phi_psi.links.new(group_008.outputs[3], index_switch.inputs[2])
			return _mn_topo_phi_psi

		_mn_topo_phi_psi = _mn_topo_phi_psi_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".MN_topo_phi_psi", type = 'NODES')
		mod.node_group = _mn_topo_phi_psi
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_MN_topo_phi_psi.bl_idname)
			
def register():
	bpy.utils.register_class(_MN_topo_phi_psi)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_MN_topo_phi_psi)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
