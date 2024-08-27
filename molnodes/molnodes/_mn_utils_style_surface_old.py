bl_info = {
	"name" : ".MN_utils_style_surface_old",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _MN_utils_style_surface_old(bpy.types.Operator):
	bl_idname = "node._mn_utils_style_surface_old"
	bl_label = ".MN_utils_style_surface_old"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _surface_blur_color node group
		def _surface_blur_color_node_group():
			_surface_blur_color = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".surface_blur_color")

			_surface_blur_color.color_tag = 'NONE'
			_surface_blur_color.description = ""

			_surface_blur_color.is_modifier = True
			
			#_surface_blur_color interface
			#Socket Geometry
			geometry_socket = _surface_blur_color.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_1 = _surface_blur_color.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_1.attribute_domain = 'POINT'
			
			#Socket Blur Iterations
			blur_iterations_socket = _surface_blur_color.interface.new_socket(name = "Blur Iterations", in_out='INPUT', socket_type = 'NodeSocketInt')
			blur_iterations_socket.default_value = 0
			blur_iterations_socket.min_value = -2147483648
			blur_iterations_socket.max_value = 2147483647
			blur_iterations_socket.subtype = 'NONE'
			blur_iterations_socket.attribute_domain = 'POINT'
			
			#Socket Color
			color_socket = _surface_blur_color.interface.new_socket(name = "Color", in_out='INPUT', socket_type = 'NodeSocketColor')
			color_socket.default_value = (0.0, 0.0, 0.0, 0.0)
			color_socket.attribute_domain = 'POINT'
			color_socket.hide_value = True
			
			
			#initialize _surface_blur_color nodes
			#node Group Output
			group_output = _surface_blur_color.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = _surface_blur_color.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Store Named Attribute
			store_named_attribute = _surface_blur_color.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute.name = "Store Named Attribute"
			store_named_attribute.data_type = 'FLOAT_COLOR'
			store_named_attribute.domain = 'POINT'
			#Selection
			store_named_attribute.inputs[1].default_value = True
			#Name
			store_named_attribute.inputs[2].default_value = "Color"
			
			#node Store Named Attribute.001
			store_named_attribute_001 = _surface_blur_color.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_001.name = "Store Named Attribute.001"
			store_named_attribute_001.data_type = 'FLOAT_COLOR'
			store_named_attribute_001.domain = 'FACE'
			#Selection
			store_named_attribute_001.inputs[1].default_value = True
			#Name
			store_named_attribute_001.inputs[2].default_value = "Color"
			
			#node Reroute.005
			reroute_005 = _surface_blur_color.nodes.new("NodeReroute")
			reroute_005.name = "Reroute.005"
			#node Blur Attribute.002
			blur_attribute_002 = _surface_blur_color.nodes.new("GeometryNodeBlurAttribute")
			blur_attribute_002.name = "Blur Attribute.002"
			blur_attribute_002.data_type = 'FLOAT_COLOR'
			#Weight
			blur_attribute_002.inputs[2].default_value = 1.0
			
			#node Reroute.009
			reroute_009 = _surface_blur_color.nodes.new("NodeReroute")
			reroute_009.name = "Reroute.009"
			#node Reroute.010
			reroute_010 = _surface_blur_color.nodes.new("NodeReroute")
			reroute_010.name = "Reroute.010"
			#node Switch.002
			switch_002 = _surface_blur_color.nodes.new("GeometryNodeSwitch")
			switch_002.name = "Switch.002"
			switch_002.input_type = 'GEOMETRY'
			
			#node Compare.003
			compare_003 = _surface_blur_color.nodes.new("FunctionNodeCompare")
			compare_003.name = "Compare.003"
			compare_003.data_type = 'INT'
			compare_003.mode = 'ELEMENT'
			compare_003.operation = 'NOT_EQUAL'
			#B_INT
			compare_003.inputs[3].default_value = 0
			
			#node Math
			math = _surface_blur_color.nodes.new("ShaderNodeMath")
			math.name = "Math"
			math.operation = 'SUBTRACT'
			math.use_clamp = False
			#Value_001
			math.inputs[1].default_value = 1.0
			
			
			
			
			#Set locations
			group_output.location = (490.0, 0.0)
			group_input.location = (-500.0, 0.0)
			store_named_attribute.location = (68.0, -120.0)
			store_named_attribute_001.location = (68.0, 100.0)
			reroute_005.location = (0.0, -120.0)
			blur_attribute_002.location = (-180.0, -100.0)
			reroute_009.location = (-20.0, -60.0)
			reroute_010.location = (-300.0, -80.0)
			switch_002.location = (300.0, 20.0)
			compare_003.location = (-180.0, 120.0)
			math.location = (-480.0, -140.0)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
			store_named_attribute_001.width, store_named_attribute_001.height = 140.0, 100.0
			reroute_005.width, reroute_005.height = 16.0, 100.0
			blur_attribute_002.width, blur_attribute_002.height = 140.0, 100.0
			reroute_009.width, reroute_009.height = 16.0, 100.0
			reroute_010.width, reroute_010.height = 16.0, 100.0
			switch_002.width, switch_002.height = 140.0, 100.0
			compare_003.width, compare_003.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			
			#initialize _surface_blur_color links
			#reroute_010.Output -> compare_003.A
			_surface_blur_color.links.new(reroute_010.outputs[0], compare_003.inputs[2])
			#reroute_009.Output -> store_named_attribute_001.Geometry
			_surface_blur_color.links.new(reroute_009.outputs[0], store_named_attribute_001.inputs[0])
			#store_named_attribute.Geometry -> switch_002.True
			_surface_blur_color.links.new(store_named_attribute.outputs[0], switch_002.inputs[2])
			#store_named_attribute_001.Geometry -> switch_002.False
			_surface_blur_color.links.new(store_named_attribute_001.outputs[0], switch_002.inputs[1])
			#blur_attribute_002.Value -> reroute_005.Input
			_surface_blur_color.links.new(blur_attribute_002.outputs[0], reroute_005.inputs[0])
			#reroute_009.Output -> store_named_attribute.Geometry
			_surface_blur_color.links.new(reroute_009.outputs[0], store_named_attribute.inputs[0])
			#reroute_005.Output -> store_named_attribute_001.Value
			_surface_blur_color.links.new(reroute_005.outputs[0], store_named_attribute_001.inputs[3])
			#compare_003.Result -> switch_002.Switch
			_surface_blur_color.links.new(compare_003.outputs[0], switch_002.inputs[0])
			#reroute_005.Output -> store_named_attribute.Value
			_surface_blur_color.links.new(reroute_005.outputs[0], store_named_attribute.inputs[3])
			#group_input.Color -> blur_attribute_002.Value
			_surface_blur_color.links.new(group_input.outputs[2], blur_attribute_002.inputs[0])
			#group_input.Blur Iterations -> reroute_010.Input
			_surface_blur_color.links.new(group_input.outputs[1], reroute_010.inputs[0])
			#group_input.Geometry -> reroute_009.Input
			_surface_blur_color.links.new(group_input.outputs[0], reroute_009.inputs[0])
			#switch_002.Output -> group_output.Geometry
			_surface_blur_color.links.new(switch_002.outputs[0], group_output.inputs[0])
			#reroute_010.Output -> math.Value
			_surface_blur_color.links.new(reroute_010.outputs[0], math.inputs[0])
			#math.Value -> blur_attribute_002.Iterations
			_surface_blur_color.links.new(math.outputs[0], blur_attribute_002.inputs[1])
			return _surface_blur_color

		_surface_blur_color = _surface_blur_color_node_group()

		#initialize _surface_sample_color node group
		def _surface_sample_color_node_group():
			_surface_sample_color = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".surface_sample_color")

			_surface_sample_color.color_tag = 'NONE'
			_surface_sample_color.description = ""

			
			#_surface_sample_color interface
			#Socket Color
			color_socket_1 = _surface_sample_color.interface.new_socket(name = "Color", in_out='OUTPUT', socket_type = 'NodeSocketColor')
			color_socket_1.default_value = (0.0, 0.0, 0.0, 0.0)
			color_socket_1.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket = _surface_sample_color.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket.attribute_domain = 'POINT'
			atoms_socket.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Sample CA
			sample_ca_socket = _surface_sample_color.interface.new_socket(name = "Sample CA", in_out='INPUT', socket_type = 'NodeSocketBool')
			sample_ca_socket.default_value = False
			sample_ca_socket.attribute_domain = 'POINT'
			
			
			#initialize _surface_sample_color nodes
			#node Group Output
			group_output_1 = _surface_sample_color.nodes.new("NodeGroupOutput")
			group_output_1.name = "Group Output"
			group_output_1.is_active_output = True
			
			#node Group Input
			group_input_1 = _surface_sample_color.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			
			#node Switch
			switch = _surface_sample_color.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'GEOMETRY'
			
			#node Sample Index.001
			sample_index_001 = _surface_sample_color.nodes.new("GeometryNodeSampleIndex")
			sample_index_001.name = "Sample Index.001"
			sample_index_001.clamp = False
			sample_index_001.data_type = 'FLOAT_COLOR'
			sample_index_001.domain = 'POINT'
			
			#node Named Attribute.002
			named_attribute_002 = _surface_sample_color.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002.name = "Named Attribute.002"
			named_attribute_002.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute_002.inputs[0].default_value = "Color"
			
			#node Sample Nearest.001
			sample_nearest_001 = _surface_sample_color.nodes.new("GeometryNodeSampleNearest")
			sample_nearest_001.name = "Sample Nearest.001"
			sample_nearest_001.domain = 'POINT'
			#Sample Position
			sample_nearest_001.inputs[1].default_value = (0.0, 0.0, 0.0)
			
			#node Separate Geometry.001
			separate_geometry_001 = _surface_sample_color.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_001.name = "Separate Geometry.001"
			separate_geometry_001.domain = 'POINT'
			
			#node Reroute.006
			reroute_006 = _surface_sample_color.nodes.new("NodeReroute")
			reroute_006.name = "Reroute.006"
			#node Compare
			compare = _surface_sample_color.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'EQUAL'
			#B_INT
			compare.inputs[3].default_value = 61
			
			#node Boolean Math
			boolean_math = _surface_sample_color.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'OR'
			
			#node Named Attribute.003
			named_attribute_003 = _surface_sample_color.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_003.name = "Named Attribute.003"
			named_attribute_003.data_type = 'INT'
			#Name
			named_attribute_003.inputs[0].default_value = "atom_name"
			
			#node Named Attribute.001
			named_attribute_001 = _surface_sample_color.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.data_type = 'BOOLEAN'
			#Name
			named_attribute_001.inputs[0].default_value = "is_alpha_carbon"
			
			
			
			
			#Set locations
			group_output_1.location = (366.8493957519531, 0.7877547144889832)
			group_input_1.location = (-383.1506042480469, 0.7877547144889832)
			switch.location = (-80.39474487304688, 78.26654815673828)
			sample_index_001.location = (176.84939575195312, 260.7877502441406)
			named_attribute_002.location = (176.84939575195312, 40.78775405883789)
			sample_nearest_001.location = (-83.15060424804688, 220.78775024414062)
			separate_geometry_001.location = (-83.15060424804688, -99.21224212646484)
			reroute_006.location = (-183.15060424804688, -99.21224212646484)
			compare.location = (-260.0, -380.0)
			boolean_math.location = (-80.0, -260.0)
			named_attribute_003.location = (-460.0, -380.0)
			named_attribute_001.location = (-455.15753173828125, -240.0)
			
			#Set dimensions
			group_output_1.width, group_output_1.height = 140.0, 100.0
			group_input_1.width, group_input_1.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			sample_index_001.width, sample_index_001.height = 140.0, 100.0
			named_attribute_002.width, named_attribute_002.height = 140.0, 100.0
			sample_nearest_001.width, sample_nearest_001.height = 140.0, 100.0
			separate_geometry_001.width, separate_geometry_001.height = 140.0, 100.0
			reroute_006.width, reroute_006.height = 16.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			named_attribute_003.width, named_attribute_003.height = 172.52069091796875, 100.0
			named_attribute_001.width, named_attribute_001.height = 162.8524169921875, 100.0
			
			#initialize _surface_sample_color links
			#reroute_006.Output -> switch.False
			_surface_sample_color.links.new(reroute_006.outputs[0], switch.inputs[1])
			#separate_geometry_001.Selection -> switch.True
			_surface_sample_color.links.new(separate_geometry_001.outputs[0], switch.inputs[2])
			#switch.Output -> sample_index_001.Geometry
			_surface_sample_color.links.new(switch.outputs[0], sample_index_001.inputs[0])
			#sample_nearest_001.Index -> sample_index_001.Index
			_surface_sample_color.links.new(sample_nearest_001.outputs[0], sample_index_001.inputs[2])
			#named_attribute_002.Attribute -> sample_index_001.Value
			_surface_sample_color.links.new(named_attribute_002.outputs[0], sample_index_001.inputs[1])
			#reroute_006.Output -> separate_geometry_001.Geometry
			_surface_sample_color.links.new(reroute_006.outputs[0], separate_geometry_001.inputs[0])
			#switch.Output -> sample_nearest_001.Geometry
			_surface_sample_color.links.new(switch.outputs[0], sample_nearest_001.inputs[0])
			#group_input_1.Atoms -> reroute_006.Input
			_surface_sample_color.links.new(group_input_1.outputs[0], reroute_006.inputs[0])
			#sample_index_001.Value -> group_output_1.Color
			_surface_sample_color.links.new(sample_index_001.outputs[0], group_output_1.inputs[0])
			#named_attribute_003.Attribute -> compare.A
			_surface_sample_color.links.new(named_attribute_003.outputs[0], compare.inputs[2])
			#compare.Result -> boolean_math.Boolean
			_surface_sample_color.links.new(compare.outputs[0], boolean_math.inputs[1])
			#named_attribute_001.Attribute -> boolean_math.Boolean
			_surface_sample_color.links.new(named_attribute_001.outputs[0], boolean_math.inputs[0])
			#boolean_math.Boolean -> separate_geometry_001.Selection
			_surface_sample_color.links.new(boolean_math.outputs[0], separate_geometry_001.inputs[1])
			#group_input_1.Sample CA -> switch.Switch
			_surface_sample_color.links.new(group_input_1.outputs[1], switch.inputs[0])
			return _surface_sample_color

		_surface_sample_color = _surface_sample_color_node_group()

		#initialize _surface_blur_postion node group
		def _surface_blur_postion_node_group():
			_surface_blur_postion = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".surface_blur_postion")

			_surface_blur_postion.color_tag = 'NONE'
			_surface_blur_postion.description = ""

			_surface_blur_postion.is_modifier = True
			
			#_surface_blur_postion interface
			#Socket Geometry
			geometry_socket_2 = _surface_blur_postion.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_2.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_3 = _surface_blur_postion.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_3.attribute_domain = 'POINT'
			
			#Socket Iterations
			iterations_socket = _surface_blur_postion.interface.new_socket(name = "Iterations", in_out='INPUT', socket_type = 'NodeSocketInt')
			iterations_socket.default_value = 2
			iterations_socket.min_value = 0
			iterations_socket.max_value = 2147483647
			iterations_socket.subtype = 'NONE'
			iterations_socket.attribute_domain = 'POINT'
			
			
			#initialize _surface_blur_postion nodes
			#node Frame
			frame = _surface_blur_postion.nodes.new("NodeFrame")
			frame.label = "Smoothen out weird bumps from meshing"
			frame.name = "Frame"
			frame.label_size = 20
			frame.shrink = True
			
			#node Group Input
			group_input_2 = _surface_blur_postion.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
			#node Blur Attribute.001
			blur_attribute_001 = _surface_blur_postion.nodes.new("GeometryNodeBlurAttribute")
			blur_attribute_001.name = "Blur Attribute.001"
			blur_attribute_001.data_type = 'FLOAT_VECTOR'
			#Weight
			blur_attribute_001.inputs[2].default_value = 1.0
			
			#node Evaluate on Domain
			evaluate_on_domain = _surface_blur_postion.nodes.new("GeometryNodeFieldOnDomain")
			evaluate_on_domain.name = "Evaluate on Domain"
			evaluate_on_domain.data_type = 'FLOAT_VECTOR'
			evaluate_on_domain.domain = 'FACE'
			
			#node Position.002
			position_002 = _surface_blur_postion.nodes.new("GeometryNodeInputPosition")
			position_002.name = "Position.002"
			
			#node Evaluate on Domain.001
			evaluate_on_domain_001 = _surface_blur_postion.nodes.new("GeometryNodeFieldOnDomain")
			evaluate_on_domain_001.name = "Evaluate on Domain.001"
			evaluate_on_domain_001.data_type = 'FLOAT_VECTOR'
			evaluate_on_domain_001.domain = 'POINT'
			
			#node Set Position
			set_position = _surface_blur_postion.nodes.new("GeometryNodeSetPosition")
			set_position.name = "Set Position"
			#Selection
			set_position.inputs[1].default_value = True
			#Offset
			set_position.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Group Output
			group_output_2 = _surface_blur_postion.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Blur Attribute
			blur_attribute = _surface_blur_postion.nodes.new("GeometryNodeBlurAttribute")
			blur_attribute.name = "Blur Attribute"
			blur_attribute.data_type = 'FLOAT_VECTOR'
			#Iterations
			blur_attribute.inputs[1].default_value = 4
			#Weight
			blur_attribute.inputs[2].default_value = 1.0
			
			#node Position
			position = _surface_blur_postion.nodes.new("GeometryNodeInputPosition")
			position.name = "Position"
			
			#node Set Position.001
			set_position_001 = _surface_blur_postion.nodes.new("GeometryNodeSetPosition")
			set_position_001.name = "Set Position.001"
			#Offset
			set_position_001.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Compare
			compare_1 = _surface_blur_postion.nodes.new("FunctionNodeCompare")
			compare_1.name = "Compare"
			compare_1.data_type = 'INT'
			compare_1.mode = 'ELEMENT'
			compare_1.operation = 'EQUAL'
			#B_INT
			compare_1.inputs[3].default_value = 3
			
			#node Vertex Neighbors
			vertex_neighbors = _surface_blur_postion.nodes.new("GeometryNodeInputMeshVertexNeighbors")
			vertex_neighbors.name = "Vertex Neighbors"
			
			#node Edge Vertices
			edge_vertices = _surface_blur_postion.nodes.new("GeometryNodeInputMeshEdgeVertices")
			edge_vertices.name = "Edge Vertices"
			
			#node Evaluate at Index.001
			evaluate_at_index_001 = _surface_blur_postion.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001.name = "Evaluate at Index.001"
			evaluate_at_index_001.data_type = 'BOOLEAN'
			evaluate_at_index_001.domain = 'POINT'
			
			#node Boolean Math
			boolean_math_1 = _surface_blur_postion.nodes.new("FunctionNodeBooleanMath")
			boolean_math_1.name = "Boolean Math"
			boolean_math_1.operation = 'AND'
			
			#node Edges to Face Groups
			edges_to_face_groups = _surface_blur_postion.nodes.new("GeometryNodeEdgesToFaceGroups")
			edges_to_face_groups.name = "Edges to Face Groups"
			
			#node Evaluate at Index
			evaluate_at_index = _surface_blur_postion.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index.name = "Evaluate at Index"
			evaluate_at_index.data_type = 'BOOLEAN'
			evaluate_at_index.domain = 'POINT'
			
			#node Face Group Boundaries
			face_group_boundaries = _surface_blur_postion.nodes.new("GeometryNodeMeshFaceSetBoundaries")
			face_group_boundaries.name = "Face Group Boundaries"
			
			
			
			#Set parents
			compare_1.parent = frame
			vertex_neighbors.parent = frame
			edge_vertices.parent = frame
			evaluate_at_index_001.parent = frame
			boolean_math_1.parent = frame
			edges_to_face_groups.parent = frame
			evaluate_at_index.parent = frame
			face_group_boundaries.parent = frame
			
			#Set locations
			frame.location = (0.0, 0.0)
			group_input_2.location = (-610.1629638671875, 0.0)
			blur_attribute_001.location = (-299.5, -120.0)
			evaluate_on_domain.location = (-459.5, -120.0)
			position_002.location = (-619.5, -120.0)
			evaluate_on_domain_001.location = (-119.5, -120.0)
			set_position.location = (60.5, 20.0)
			group_output_2.location = (680.947509765625, -17.612947463989258)
			blur_attribute.location = (460.0, -200.0)
			position.location = (460.0, -360.0)
			set_position_001.location = (460.784423828125, 10.757638931274414)
			compare_1.location = (-220.0, -560.0)
			vertex_neighbors.location = (-380.0, -560.0)
			edge_vertices.location = (-220.0, -420.0)
			evaluate_at_index_001.location = (-60.0, -580.0)
			boolean_math_1.location = (100.0, -420.0)
			edges_to_face_groups.location = (100.0, -560.0)
			evaluate_at_index.location = (-60.0, -420.0)
			face_group_boundaries.location = (100.0, -660.0)
			
			#Set dimensions
			frame.width, frame.height = 690.0, 385.0
			group_input_2.width, group_input_2.height = 140.0, 100.0
			blur_attribute_001.width, blur_attribute_001.height = 140.0, 100.0
			evaluate_on_domain.width, evaluate_on_domain.height = 140.0, 100.0
			position_002.width, position_002.height = 140.0, 100.0
			evaluate_on_domain_001.width, evaluate_on_domain_001.height = 140.0, 100.0
			set_position.width, set_position.height = 140.0, 100.0
			group_output_2.width, group_output_2.height = 140.0, 100.0
			blur_attribute.width, blur_attribute.height = 140.0, 100.0
			position.width, position.height = 140.0, 100.0
			set_position_001.width, set_position_001.height = 140.0, 100.0
			compare_1.width, compare_1.height = 140.0, 100.0
			vertex_neighbors.width, vertex_neighbors.height = 140.0, 100.0
			edge_vertices.width, edge_vertices.height = 140.0, 100.0
			evaluate_at_index_001.width, evaluate_at_index_001.height = 140.0, 100.0
			boolean_math_1.width, boolean_math_1.height = 140.0, 100.0
			edges_to_face_groups.width, edges_to_face_groups.height = 140.0, 100.0
			evaluate_at_index.width, evaluate_at_index.height = 140.0, 100.0
			face_group_boundaries.width, face_group_boundaries.height = 150.0, 100.0
			
			#initialize _surface_blur_postion links
			#evaluate_on_domain_001.Value -> set_position.Position
			_surface_blur_postion.links.new(evaluate_on_domain_001.outputs[0], set_position.inputs[2])
			#position_002.Position -> evaluate_on_domain.Value
			_surface_blur_postion.links.new(position_002.outputs[0], evaluate_on_domain.inputs[0])
			#blur_attribute_001.Value -> evaluate_on_domain_001.Value
			_surface_blur_postion.links.new(blur_attribute_001.outputs[0], evaluate_on_domain_001.inputs[0])
			#evaluate_on_domain.Value -> blur_attribute_001.Value
			_surface_blur_postion.links.new(evaluate_on_domain.outputs[0], blur_attribute_001.inputs[0])
			#group_input_2.Geometry -> set_position.Geometry
			_surface_blur_postion.links.new(group_input_2.outputs[0], set_position.inputs[0])
			#set_position_001.Geometry -> group_output_2.Geometry
			_surface_blur_postion.links.new(set_position_001.outputs[0], group_output_2.inputs[0])
			#group_input_2.Iterations -> blur_attribute_001.Iterations
			_surface_blur_postion.links.new(group_input_2.outputs[1], blur_attribute_001.inputs[1])
			#set_position.Geometry -> set_position_001.Geometry
			_surface_blur_postion.links.new(set_position.outputs[0], set_position_001.inputs[0])
			#vertex_neighbors.Vertex Count -> compare_1.A
			_surface_blur_postion.links.new(vertex_neighbors.outputs[0], compare_1.inputs[2])
			#compare_1.Result -> evaluate_at_index.Value
			_surface_blur_postion.links.new(compare_1.outputs[0], evaluate_at_index.inputs[1])
			#compare_1.Result -> evaluate_at_index_001.Value
			_surface_blur_postion.links.new(compare_1.outputs[0], evaluate_at_index_001.inputs[1])
			#edge_vertices.Vertex Index 1 -> evaluate_at_index.Index
			_surface_blur_postion.links.new(edge_vertices.outputs[0], evaluate_at_index.inputs[0])
			#edge_vertices.Vertex Index 2 -> evaluate_at_index_001.Index
			_surface_blur_postion.links.new(edge_vertices.outputs[1], evaluate_at_index_001.inputs[0])
			#evaluate_at_index.Value -> boolean_math_1.Boolean
			_surface_blur_postion.links.new(evaluate_at_index.outputs[0], boolean_math_1.inputs[0])
			#evaluate_at_index_001.Value -> boolean_math_1.Boolean
			_surface_blur_postion.links.new(evaluate_at_index_001.outputs[0], boolean_math_1.inputs[1])
			#boolean_math_1.Boolean -> edges_to_face_groups.Boundary Edges
			_surface_blur_postion.links.new(boolean_math_1.outputs[0], edges_to_face_groups.inputs[0])
			#edges_to_face_groups.Face Group ID -> face_group_boundaries.Face Group ID
			_surface_blur_postion.links.new(edges_to_face_groups.outputs[0], face_group_boundaries.inputs[0])
			#blur_attribute.Value -> set_position_001.Position
			_surface_blur_postion.links.new(blur_attribute.outputs[0], set_position_001.inputs[2])
			#position.Position -> blur_attribute.Value
			_surface_blur_postion.links.new(position.outputs[0], blur_attribute.inputs[0])
			#face_group_boundaries.Boundary Edges -> set_position_001.Selection
			_surface_blur_postion.links.new(face_group_boundaries.outputs[0], set_position_001.inputs[1])
			return _surface_blur_postion

		_surface_blur_postion = _surface_blur_postion_node_group()

		#initialize _surface_compute_density_from_points node group
		def _surface_compute_density_from_points_node_group():
			_surface_compute_density_from_points = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".surface_compute_density_from_points")

			_surface_compute_density_from_points.color_tag = 'NONE'
			_surface_compute_density_from_points.description = ""

			
			#_surface_compute_density_from_points interface
			#Socket Result
			result_socket = _surface_compute_density_from_points.interface.new_socket(name = "Result", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			result_socket.default_value = False
			result_socket.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket_1 = _surface_compute_density_from_points.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_1.attribute_domain = 'POINT'
			atoms_socket_1.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Scale Radius
			scale_radius_socket = _surface_compute_density_from_points.interface.new_socket(name = "Scale Radius", in_out='INPUT', socket_type = 'NodeSocketFloat')
			scale_radius_socket.default_value = 1.0
			scale_radius_socket.min_value = -10000.0
			scale_radius_socket.max_value = 10000.0
			scale_radius_socket.subtype = 'NONE'
			scale_radius_socket.attribute_domain = 'POINT'
			
			#Socket Probe Size
			probe_size_socket = _surface_compute_density_from_points.interface.new_socket(name = "Probe Size", in_out='INPUT', socket_type = 'NodeSocketFloat')
			probe_size_socket.default_value = 0.0
			probe_size_socket.min_value = 0.0
			probe_size_socket.max_value = 10000.0
			probe_size_socket.subtype = 'NONE'
			probe_size_socket.attribute_domain = 'POINT'
			
			
			#initialize _surface_compute_density_from_points nodes
			#node Sample Index.002
			sample_index_002 = _surface_compute_density_from_points.nodes.new("GeometryNodeSampleIndex")
			sample_index_002.name = "Sample Index.002"
			sample_index_002.clamp = False
			sample_index_002.data_type = 'FLOAT_VECTOR'
			sample_index_002.domain = 'POINT'
			
			#node Position.001
			position_001 = _surface_compute_density_from_points.nodes.new("GeometryNodeInputPosition")
			position_001.name = "Position.001"
			
			#node Reroute
			reroute = _surface_compute_density_from_points.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Group Output
			group_output_3 = _surface_compute_density_from_points.nodes.new("NodeGroupOutput")
			group_output_3.name = "Group Output"
			group_output_3.is_active_output = True
			
			#node Compare.001
			compare_001 = _surface_compute_density_from_points.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'FLOAT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'GREATER_THAN'
			#B
			compare_001.inputs[1].default_value = 0.0
			
			#node Vector Math.004
			vector_math_004 = _surface_compute_density_from_points.nodes.new("ShaderNodeVectorMath")
			vector_math_004.name = "Vector Math.004"
			vector_math_004.operation = 'DISTANCE'
			
			#node Math.008
			math_008 = _surface_compute_density_from_points.nodes.new("ShaderNodeMath")
			math_008.name = "Math.008"
			math_008.operation = 'SUBTRACT'
			math_008.use_clamp = False
			
			#node Math.009
			math_009 = _surface_compute_density_from_points.nodes.new("ShaderNodeMath")
			math_009.name = "Math.009"
			math_009.operation = 'ADD'
			math_009.use_clamp = False
			
			#node Math.001
			math_001 = _surface_compute_density_from_points.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.operation = 'DIVIDE'
			math_001.use_clamp = False
			#Value_001
			math_001.inputs[1].default_value = 100.0
			
			#node Sample Index
			sample_index = _surface_compute_density_from_points.nodes.new("GeometryNodeSampleIndex")
			sample_index.name = "Sample Index"
			sample_index.clamp = False
			sample_index.data_type = 'FLOAT'
			sample_index.domain = 'POINT'
			
			#node Reroute.007
			reroute_007 = _surface_compute_density_from_points.nodes.new("NodeReroute")
			reroute_007.name = "Reroute.007"
			#node Math.003
			math_003 = _surface_compute_density_from_points.nodes.new("ShaderNodeMath")
			math_003.name = "Math.003"
			math_003.operation = 'MULTIPLY'
			math_003.use_clamp = False
			
			#node Sample Index.001
			sample_index_001_1 = _surface_compute_density_from_points.nodes.new("GeometryNodeSampleIndex")
			sample_index_001_1.name = "Sample Index.001"
			sample_index_001_1.clamp = False
			sample_index_001_1.data_type = 'FLOAT'
			sample_index_001_1.domain = 'POINT'
			
			#node Named Attribute
			named_attribute = _surface_compute_density_from_points.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'FLOAT'
			#Name
			named_attribute.inputs[0].default_value = "vdw_radii"
			
			#node Reroute.002
			reroute_002 = _surface_compute_density_from_points.nodes.new("NodeReroute")
			reroute_002.name = "Reroute.002"
			#node Sample Index.003
			sample_index_003 = _surface_compute_density_from_points.nodes.new("GeometryNodeSampleIndex")
			sample_index_003.name = "Sample Index.003"
			sample_index_003.clamp = False
			sample_index_003.data_type = 'FLOAT'
			sample_index_003.domain = 'POINT'
			
			#node Reroute.003
			reroute_003 = _surface_compute_density_from_points.nodes.new("NodeReroute")
			reroute_003.name = "Reroute.003"
			#node Reroute.001
			reroute_001 = _surface_compute_density_from_points.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			#node Group Input
			group_input_3 = _surface_compute_density_from_points.nodes.new("NodeGroupInput")
			group_input_3.name = "Group Input"
			
			#node Sample Nearest
			sample_nearest = _surface_compute_density_from_points.nodes.new("GeometryNodeSampleNearest")
			sample_nearest.name = "Sample Nearest"
			sample_nearest.domain = 'POINT'
			#Sample Position
			sample_nearest.inputs[1].default_value = (0.0, 0.0, 0.0)
			
			
			
			
			#Set locations
			sample_index_002.location = (-300.0, -60.0)
			position_001.location = (-460.0, -240.0)
			reroute.location = (-140.0, -280.0)
			group_output_3.location = (562.0, 220.0)
			compare_001.location = (382.0, 220.0)
			vector_math_004.location = (-140.0, -60.0)
			math_008.location = (162.0, 180.0)
			math_009.location = (-58.0, 216.76718139648438)
			math_001.location = (-280.0, 380.0)
			sample_index.location = (-278.0, 180.0)
			reroute_007.location = (-900.0, 60.0)
			math_003.location = (-780.0, 60.0)
			sample_index_001_1.location = (-840.0, 300.0)
			named_attribute.location = (-940.0, 60.0)
			reroute_002.location = (-1034.125244140625, 60.0)
			sample_index_003.location = (-940.0, -80.0)
			reroute_003.location = (-440.0, 180.0)
			reroute_001.location = (-1280.0, 60.0)
			group_input_3.location = (-1560.0, 100.0)
			sample_nearest.location = (-1260.0, 220.0)
			
			#Set dimensions
			sample_index_002.width, sample_index_002.height = 140.0, 100.0
			position_001.width, position_001.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			group_output_3.width, group_output_3.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			vector_math_004.width, vector_math_004.height = 140.0, 100.0
			math_008.width, math_008.height = 140.0, 100.0
			math_009.width, math_009.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			sample_index.width, sample_index.height = 140.0, 100.0
			reroute_007.width, reroute_007.height = 16.0, 100.0
			math_003.width, math_003.height = 140.0, 100.0
			sample_index_001_1.width, sample_index_001_1.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			reroute_002.width, reroute_002.height = 16.0, 100.0
			sample_index_003.width, sample_index_003.height = 140.0, 100.0
			reroute_003.width, reroute_003.height = 16.0, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			group_input_3.width, group_input_3.height = 140.0, 100.0
			sample_nearest.width, sample_nearest.height = 140.0, 100.0
			
			#initialize _surface_compute_density_from_points links
			#reroute_003.Output -> sample_index.Index
			_surface_compute_density_from_points.links.new(reroute_003.outputs[0], sample_index.inputs[2])
			#math_008.Value -> compare_001.A
			_surface_compute_density_from_points.links.new(math_008.outputs[0], compare_001.inputs[0])
			#sample_index_002.Value -> vector_math_004.Vector
			_surface_compute_density_from_points.links.new(sample_index_002.outputs[0], vector_math_004.inputs[0])
			#reroute_003.Output -> sample_index_002.Index
			_surface_compute_density_from_points.links.new(reroute_003.outputs[0], sample_index_002.inputs[2])
			#reroute.Output -> vector_math_004.Vector
			_surface_compute_density_from_points.links.new(reroute.outputs[0], vector_math_004.inputs[1])
			#reroute_007.Output -> sample_index.Geometry
			_surface_compute_density_from_points.links.new(reroute_007.outputs[0], sample_index.inputs[0])
			#math_003.Value -> sample_index.Value
			_surface_compute_density_from_points.links.new(math_003.outputs[0], sample_index.inputs[1])
			#reroute_007.Output -> sample_index_002.Geometry
			_surface_compute_density_from_points.links.new(reroute_007.outputs[0], sample_index_002.inputs[0])
			#position_001.Position -> sample_index_002.Value
			_surface_compute_density_from_points.links.new(position_001.outputs[0], sample_index_002.inputs[1])
			#reroute_002.Output -> reroute_007.Input
			_surface_compute_density_from_points.links.new(reroute_002.outputs[0], reroute_007.inputs[0])
			#compare_001.Result -> group_output_3.Result
			_surface_compute_density_from_points.links.new(compare_001.outputs[0], group_output_3.inputs[0])
			#named_attribute.Attribute -> math_003.Value
			_surface_compute_density_from_points.links.new(named_attribute.outputs[0], math_003.inputs[0])
			#position_001.Position -> reroute.Input
			_surface_compute_density_from_points.links.new(position_001.outputs[0], reroute.inputs[0])
			#vector_math_004.Value -> math_008.Value
			_surface_compute_density_from_points.links.new(vector_math_004.outputs[1], math_008.inputs[1])
			#math_009.Value -> math_008.Value
			_surface_compute_density_from_points.links.new(math_009.outputs[0], math_008.inputs[0])
			#sample_index.Value -> math_009.Value
			_surface_compute_density_from_points.links.new(sample_index.outputs[0], math_009.inputs[0])
			#math_001.Value -> math_009.Value
			_surface_compute_density_from_points.links.new(math_001.outputs[0], math_009.inputs[1])
			#reroute_007.Output -> sample_index_001_1.Geometry
			_surface_compute_density_from_points.links.new(reroute_007.outputs[0], sample_index_001_1.inputs[0])
			#reroute_001.Output -> sample_nearest.Geometry
			_surface_compute_density_from_points.links.new(reroute_001.outputs[0], sample_nearest.inputs[0])
			#group_input_3.Atoms -> reroute_001.Input
			_surface_compute_density_from_points.links.new(group_input_3.outputs[0], reroute_001.inputs[0])
			#sample_nearest.Index -> sample_index_001_1.Index
			_surface_compute_density_from_points.links.new(sample_nearest.outputs[0], sample_index_001_1.inputs[2])
			#group_input_3.Probe Size -> sample_index_001_1.Value
			_surface_compute_density_from_points.links.new(group_input_3.outputs[2], sample_index_001_1.inputs[1])
			#sample_index_001_1.Value -> math_001.Value
			_surface_compute_density_from_points.links.new(sample_index_001_1.outputs[0], math_001.inputs[0])
			#sample_nearest.Index -> sample_index_003.Index
			_surface_compute_density_from_points.links.new(sample_nearest.outputs[0], sample_index_003.inputs[2])
			#group_input_3.Scale Radius -> sample_index_003.Value
			_surface_compute_density_from_points.links.new(group_input_3.outputs[1], sample_index_003.inputs[1])
			#sample_index_003.Value -> math_003.Value
			_surface_compute_density_from_points.links.new(sample_index_003.outputs[0], math_003.inputs[1])
			#reroute_001.Output -> reroute_002.Input
			_surface_compute_density_from_points.links.new(reroute_001.outputs[0], reroute_002.inputs[0])
			#reroute_002.Output -> sample_index_003.Geometry
			_surface_compute_density_from_points.links.new(reroute_002.outputs[0], sample_index_003.inputs[0])
			#sample_nearest.Index -> reroute_003.Input
			_surface_compute_density_from_points.links.new(sample_nearest.outputs[0], reroute_003.inputs[0])
			return _surface_compute_density_from_points

		_surface_compute_density_from_points = _surface_compute_density_from_points_node_group()

		#initialize _utils_bounding_box node group
		def _utils_bounding_box_node_group():
			_utils_bounding_box = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".utils_bounding_box")

			_utils_bounding_box.color_tag = 'NONE'
			_utils_bounding_box.description = ""

			
			#_utils_bounding_box interface
			#Socket Min
			min_socket = _utils_bounding_box.interface.new_socket(name = "Min", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			min_socket.default_value = (0.0, 0.0, 0.0)
			min_socket.min_value = -3.4028234663852886e+38
			min_socket.max_value = 3.4028234663852886e+38
			min_socket.subtype = 'NONE'
			min_socket.attribute_domain = 'POINT'
			
			#Socket Max
			max_socket = _utils_bounding_box.interface.new_socket(name = "Max", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			max_socket.default_value = (0.0, 0.0, 0.0)
			max_socket.min_value = -3.4028234663852886e+38
			max_socket.max_value = 3.4028234663852886e+38
			max_socket.subtype = 'NONE'
			max_socket.attribute_domain = 'POINT'
			
			#Socket X
			x_socket = _utils_bounding_box.interface.new_socket(name = "X", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			x_socket.default_value = 0
			x_socket.min_value = -2147483648
			x_socket.max_value = 2147483647
			x_socket.subtype = 'NONE'
			x_socket.attribute_domain = 'POINT'
			
			#Socket Y
			y_socket = _utils_bounding_box.interface.new_socket(name = "Y", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			y_socket.default_value = 0
			y_socket.min_value = -2147483648
			y_socket.max_value = 2147483647
			y_socket.subtype = 'NONE'
			y_socket.attribute_domain = 'POINT'
			
			#Socket Z
			z_socket = _utils_bounding_box.interface.new_socket(name = "Z", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			z_socket.default_value = 0
			z_socket.min_value = -2147483648
			z_socket.max_value = 2147483647
			z_socket.subtype = 'NONE'
			z_socket.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_4 = _utils_bounding_box.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_4.attribute_domain = 'POINT'
			
			#Socket Subdivisions
			subdivisions_socket = _utils_bounding_box.interface.new_socket(name = "Subdivisions", in_out='INPUT', socket_type = 'NodeSocketFloat')
			subdivisions_socket.default_value = 16.700000762939453
			subdivisions_socket.min_value = -10000.0
			subdivisions_socket.max_value = 10000.0
			subdivisions_socket.subtype = 'NONE'
			subdivisions_socket.attribute_domain = 'POINT'
			
			
			#initialize _utils_bounding_box nodes
			#node Vector Math.002
			vector_math_002 = _utils_bounding_box.nodes.new("ShaderNodeVectorMath")
			vector_math_002.name = "Vector Math.002"
			vector_math_002.operation = 'SUBTRACT'
			
			#node Vector Math.003
			vector_math_003 = _utils_bounding_box.nodes.new("ShaderNodeVectorMath")
			vector_math_003.name = "Vector Math.003"
			vector_math_003.operation = 'SCALE'
			
			#node Reroute
			reroute_1 = _utils_bounding_box.nodes.new("NodeReroute")
			reroute_1.name = "Reroute"
			#node Reroute.002
			reroute_002_1 = _utils_bounding_box.nodes.new("NodeReroute")
			reroute_002_1.name = "Reroute.002"
			#node Group Output
			group_output_4 = _utils_bounding_box.nodes.new("NodeGroupOutput")
			group_output_4.name = "Group Output"
			group_output_4.is_active_output = True
			
			#node Separate XYZ
			separate_xyz = _utils_bounding_box.nodes.new("ShaderNodeSeparateXYZ")
			separate_xyz.name = "Separate XYZ"
			
			#node Math
			math_1 = _utils_bounding_box.nodes.new("ShaderNodeMath")
			math_1.name = "Math"
			math_1.hide = True
			math_1.operation = 'MAXIMUM'
			math_1.use_clamp = False
			#Value_001
			math_1.inputs[1].default_value = 2.0
			
			#node Math.001
			math_001_1 = _utils_bounding_box.nodes.new("ShaderNodeMath")
			math_001_1.name = "Math.001"
			math_001_1.hide = True
			math_001_1.operation = 'MAXIMUM'
			math_001_1.use_clamp = False
			#Value_001
			math_001_1.inputs[1].default_value = 2.0
			
			#node Math.002
			math_002 = _utils_bounding_box.nodes.new("ShaderNodeMath")
			math_002.name = "Math.002"
			math_002.hide = True
			math_002.operation = 'MAXIMUM'
			math_002.use_clamp = False
			#Value_001
			math_002.inputs[1].default_value = 2.0
			
			#node Group Input
			group_input_4 = _utils_bounding_box.nodes.new("NodeGroupInput")
			group_input_4.name = "Group Input"
			
			#node Bounding Box
			bounding_box = _utils_bounding_box.nodes.new("GeometryNodeBoundBox")
			bounding_box.name = "Bounding Box"
			
			#node Value
			value = _utils_bounding_box.nodes.new("ShaderNodeValue")
			value.name = "Value"
			
			value.outputs[0].default_value = 0.009999999776482582
			#node Reroute.001
			reroute_001_1 = _utils_bounding_box.nodes.new("NodeReroute")
			reroute_001_1.name = "Reroute.001"
			#node Vector Math
			vector_math = _utils_bounding_box.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.operation = 'SUBTRACT'
			
			#node Vector Math.001
			vector_math_001 = _utils_bounding_box.nodes.new("ShaderNodeVectorMath")
			vector_math_001.name = "Vector Math.001"
			vector_math_001.operation = 'ADD'
			
			#node Vector Math.004
			vector_math_004_1 = _utils_bounding_box.nodes.new("ShaderNodeVectorMath")
			vector_math_004_1.name = "Vector Math.004"
			vector_math_004_1.operation = 'SNAP'
			
			#node Vector Math.005
			vector_math_005 = _utils_bounding_box.nodes.new("ShaderNodeVectorMath")
			vector_math_005.name = "Vector Math.005"
			vector_math_005.operation = 'SNAP'
			
			#node Math.003
			math_003_1 = _utils_bounding_box.nodes.new("ShaderNodeMath")
			math_003_1.name = "Math.003"
			math_003_1.operation = 'MULTIPLY'
			math_003_1.use_clamp = False
			#Value_001
			math_003_1.inputs[1].default_value = 2.0
			
			
			
			
			#Set locations
			vector_math_002.location = (-36.8055419921875, 112.27713012695312)
			vector_math_003.location = (123.1944580078125, 112.27713012695312)
			reroute_1.location = (40.0, 160.0)
			reroute_002_1.location = (60.0, 140.0)
			group_output_4.location = (700.0, 200.0)
			separate_xyz.location = (283.1944580078125, 112.27713012695312)
			math_1.location = (480.0, 120.0)
			math_001_1.location = (480.0, 80.0)
			math_002.location = (480.0, 40.0)
			group_input_4.location = (-1065.6466064453125, 104.66636657714844)
			bounding_box.location = (-885.6466064453125, 44.6663703918457)
			value.location = (-1025.04443359375, -182.63922119140625)
			reroute_001_1.location = (-439.06280517578125, -225.71304321289062)
			vector_math.location = (-313.41741943359375, 140.0)
			vector_math_001.location = (-313.41741943359375, 0.0)
			vector_math_004_1.location = (-564.7015380859375, 104.61347961425781)
			vector_math_005.location = (-563.52734375, -39.964500427246094)
			math_003_1.location = (-640.0, -200.0)
			
			#Set dimensions
			vector_math_002.width, vector_math_002.height = 140.0, 100.0
			vector_math_003.width, vector_math_003.height = 140.0, 100.0
			reroute_1.width, reroute_1.height = 16.0, 100.0
			reroute_002_1.width, reroute_002_1.height = 16.0, 100.0
			group_output_4.width, group_output_4.height = 140.0, 100.0
			separate_xyz.width, separate_xyz.height = 116.41741943359375, 100.0
			math_1.width, math_1.height = 140.0, 100.0
			math_001_1.width, math_001_1.height = 140.0, 100.0
			math_002.width, math_002.height = 140.0, 100.0
			group_input_4.width, group_input_4.height = 140.0, 100.0
			bounding_box.width, bounding_box.height = 140.0, 100.0
			value.width, value.height = 140.0, 100.0
			reroute_001_1.width, reroute_001_1.height = 16.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			vector_math_001.width, vector_math_001.height = 140.0, 100.0
			vector_math_004_1.width, vector_math_004_1.height = 140.0, 100.0
			vector_math_005.width, vector_math_005.height = 140.0, 100.0
			math_003_1.width, math_003_1.height = 140.0, 100.0
			
			#initialize _utils_bounding_box links
			#vector_math_002.Vector -> vector_math_003.Vector
			_utils_bounding_box.links.new(vector_math_002.outputs[0], vector_math_003.inputs[0])
			#vector_math_001.Vector -> vector_math_002.Vector
			_utils_bounding_box.links.new(vector_math_001.outputs[0], vector_math_002.inputs[0])
			#vector_math_003.Vector -> separate_xyz.Vector
			_utils_bounding_box.links.new(vector_math_003.outputs[0], separate_xyz.inputs[0])
			#reroute_001_1.Output -> vector_math.Vector
			_utils_bounding_box.links.new(reroute_001_1.outputs[0], vector_math.inputs[1])
			#vector_math.Vector -> vector_math_002.Vector
			_utils_bounding_box.links.new(vector_math.outputs[0], vector_math_002.inputs[1])
			#reroute_001_1.Output -> vector_math_001.Vector
			_utils_bounding_box.links.new(reroute_001_1.outputs[0], vector_math_001.inputs[1])
			#group_input_4.Subdivisions -> vector_math_003.Scale
			_utils_bounding_box.links.new(group_input_4.outputs[1], vector_math_003.inputs[3])
			#group_input_4.Geometry -> bounding_box.Geometry
			_utils_bounding_box.links.new(group_input_4.outputs[0], bounding_box.inputs[0])
			#reroute_1.Output -> group_output_4.Min
			_utils_bounding_box.links.new(reroute_1.outputs[0], group_output_4.inputs[0])
			#reroute_002_1.Output -> group_output_4.Max
			_utils_bounding_box.links.new(reroute_002_1.outputs[0], group_output_4.inputs[1])
			#math_001_1.Value -> group_output_4.Y
			_utils_bounding_box.links.new(math_001_1.outputs[0], group_output_4.inputs[3])
			#math_002.Value -> group_output_4.Z
			_utils_bounding_box.links.new(math_002.outputs[0], group_output_4.inputs[4])
			#vector_math.Vector -> reroute_1.Input
			_utils_bounding_box.links.new(vector_math.outputs[0], reroute_1.inputs[0])
			#vector_math_001.Vector -> reroute_002_1.Input
			_utils_bounding_box.links.new(vector_math_001.outputs[0], reroute_002_1.inputs[0])
			#separate_xyz.X -> math_1.Value
			_utils_bounding_box.links.new(separate_xyz.outputs[0], math_1.inputs[0])
			#math_1.Value -> group_output_4.X
			_utils_bounding_box.links.new(math_1.outputs[0], group_output_4.inputs[2])
			#separate_xyz.Y -> math_001_1.Value
			_utils_bounding_box.links.new(separate_xyz.outputs[1], math_001_1.inputs[0])
			#separate_xyz.Z -> math_002.Value
			_utils_bounding_box.links.new(separate_xyz.outputs[2], math_002.inputs[0])
			#value.Value -> vector_math_004_1.Vector
			_utils_bounding_box.links.new(value.outputs[0], vector_math_004_1.inputs[1])
			#bounding_box.Min -> vector_math_004_1.Vector
			_utils_bounding_box.links.new(bounding_box.outputs[1], vector_math_004_1.inputs[0])
			#vector_math_004_1.Vector -> vector_math.Vector
			_utils_bounding_box.links.new(vector_math_004_1.outputs[0], vector_math.inputs[0])
			#vector_math_005.Vector -> vector_math_001.Vector
			_utils_bounding_box.links.new(vector_math_005.outputs[0], vector_math_001.inputs[0])
			#bounding_box.Max -> vector_math_005.Vector
			_utils_bounding_box.links.new(bounding_box.outputs[2], vector_math_005.inputs[0])
			#value.Value -> math_003_1.Value
			_utils_bounding_box.links.new(value.outputs[0], math_003_1.inputs[0])
			#value.Value -> vector_math_005.Vector
			_utils_bounding_box.links.new(value.outputs[0], vector_math_005.inputs[1])
			#math_003_1.Value -> reroute_001_1.Input
			_utils_bounding_box.links.new(math_003_1.outputs[0], reroute_001_1.inputs[0])
			return _utils_bounding_box

		_utils_bounding_box = _utils_bounding_box_node_group()

		#initialize _mn_utils_style_surface_old node group
		def _mn_utils_style_surface_old_node_group():
			_mn_utils_style_surface_old = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_utils_style_surface_old")

			_mn_utils_style_surface_old.color_tag = 'NONE'
			_mn_utils_style_surface_old.description = ""

			_mn_utils_style_surface_old.is_modifier = True
			
			#_mn_utils_style_surface_old interface
			#Socket Geometry
			geometry_socket_5 = _mn_utils_style_surface_old.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_5.attribute_domain = 'POINT'
			
			#Socket Volume
			volume_socket = _mn_utils_style_surface_old.interface.new_socket(name = "Volume", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			volume_socket.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket_2 = _mn_utils_style_surface_old.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_2.attribute_domain = 'POINT'
			atoms_socket_2.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket = _mn_utils_style_surface_old.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket.default_value = True
			selection_socket.attribute_domain = 'POINT'
			selection_socket.hide_value = True
			selection_socket.description = "Selection of atoms to apply this node to"
			
			#Socket Quality
			quality_socket = _mn_utils_style_surface_old.interface.new_socket(name = "Quality", in_out='INPUT', socket_type = 'NodeSocketInt')
			quality_socket.default_value = 12
			quality_socket.min_value = 1
			quality_socket.max_value = 15
			quality_socket.subtype = 'NONE'
			quality_socket.attribute_domain = 'POINT'
			
			#Socket Scale Radii
			scale_radii_socket = _mn_utils_style_surface_old.interface.new_socket(name = "Scale Radii", in_out='INPUT', socket_type = 'NodeSocketFloat')
			scale_radii_socket.default_value = 1.0
			scale_radii_socket.min_value = 0.0
			scale_radii_socket.max_value = 10.0
			scale_radii_socket.subtype = 'NONE'
			scale_radii_socket.attribute_domain = 'POINT'
			
			#Socket Probe Size
			probe_size_socket_1 = _mn_utils_style_surface_old.interface.new_socket(name = "Probe Size", in_out='INPUT', socket_type = 'NodeSocketFloat')
			probe_size_socket_1.default_value = 0.6000000238418579
			probe_size_socket_1.min_value = 0.0
			probe_size_socket_1.max_value = 10000.0
			probe_size_socket_1.subtype = 'NONE'
			probe_size_socket_1.attribute_domain = 'POINT'
			
			#Socket Surface Smoothing
			surface_smoothing_socket = _mn_utils_style_surface_old.interface.new_socket(name = "Surface Smoothing", in_out='INPUT', socket_type = 'NodeSocketInt')
			surface_smoothing_socket.default_value = 2
			surface_smoothing_socket.min_value = 0
			surface_smoothing_socket.max_value = 20
			surface_smoothing_socket.subtype = 'NONE'
			surface_smoothing_socket.attribute_domain = 'POINT'
			
			#Socket Color by CA
			color_by_ca_socket = _mn_utils_style_surface_old.interface.new_socket(name = "Color by CA", in_out='INPUT', socket_type = 'NodeSocketBool')
			color_by_ca_socket.default_value = True
			color_by_ca_socket.attribute_domain = 'POINT'
			
			#Socket Interpolate Color
			interpolate_color_socket = _mn_utils_style_surface_old.interface.new_socket(name = "Interpolate Color", in_out='INPUT', socket_type = 'NodeSocketInt')
			interpolate_color_socket.default_value = 1
			interpolate_color_socket.min_value = 0
			interpolate_color_socket.max_value = 20
			interpolate_color_socket.subtype = 'NONE'
			interpolate_color_socket.attribute_domain = 'POINT'
			
			#Socket Shade Smooth
			shade_smooth_socket = _mn_utils_style_surface_old.interface.new_socket(name = "Shade Smooth", in_out='INPUT', socket_type = 'NodeSocketBool')
			shade_smooth_socket.default_value = True
			shade_smooth_socket.attribute_domain = 'POINT'
			shade_smooth_socket.description = "Apply smooth shading to the created geometry"
			
			#Socket Material
			material_socket = _mn_utils_style_surface_old.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial')
			material_socket.attribute_domain = 'POINT'
			material_socket.description = "Material to apply to the resulting geometry"
			
			
			#initialize _mn_utils_style_surface_old nodes
			#node Frame.002
			frame_002 = _mn_utils_style_surface_old.nodes.new("NodeFrame")
			frame_002.label = "Generate Surface from Measurements"
			frame_002.name = "Frame.002"
			frame_002.label_size = 20
			frame_002.shrink = True
			
			#node Reroute.009
			reroute_009_1 = _mn_utils_style_surface_old.nodes.new("NodeReroute")
			reroute_009_1.name = "Reroute.009"
			#node Group Output
			group_output_5 = _mn_utils_style_surface_old.nodes.new("NodeGroupOutput")
			group_output_5.name = "Group Output"
			group_output_5.is_active_output = True
			
			#node Math.001
			math_001_2 = _mn_utils_style_surface_old.nodes.new("ShaderNodeMath")
			math_001_2.label = "x * 10"
			math_001_2.name = "Math.001"
			math_001_2.operation = 'MULTIPLY'
			math_001_2.use_clamp = False
			#Value_001
			math_001_2.inputs[1].default_value = 10.0
			
			#node Reroute.001
			reroute_001_2 = _mn_utils_style_surface_old.nodes.new("NodeReroute")
			reroute_001_2.name = "Reroute.001"
			#node Set Material
			set_material = _mn_utils_style_surface_old.nodes.new("GeometryNodeSetMaterial")
			set_material.name = "Set Material"
			#Selection
			set_material.inputs[1].default_value = True
			
			#node Group Input.002
			group_input_002 = _mn_utils_style_surface_old.nodes.new("NodeGroupInput")
			group_input_002.name = "Group Input.002"
			
			#node Set Shade Smooth
			set_shade_smooth = _mn_utils_style_surface_old.nodes.new("GeometryNodeSetShadeSmooth")
			set_shade_smooth.name = "Set Shade Smooth"
			set_shade_smooth.domain = 'FACE'
			#Selection
			set_shade_smooth.inputs[1].default_value = True
			
			#node Reroute.006
			reroute_006_1 = _mn_utils_style_surface_old.nodes.new("NodeReroute")
			reroute_006_1.name = "Reroute.006"
			#node Reroute.004
			reroute_004 = _mn_utils_style_surface_old.nodes.new("NodeReroute")
			reroute_004.name = "Reroute.004"
			#node Reroute.005
			reroute_005_1 = _mn_utils_style_surface_old.nodes.new("NodeReroute")
			reroute_005_1.name = "Reroute.005"
			#node Group Input
			group_input_5 = _mn_utils_style_surface_old.nodes.new("NodeGroupInput")
			group_input_5.name = "Group Input"
			
			#node Volume Cube
			volume_cube = _mn_utils_style_surface_old.nodes.new("GeometryNodeVolumeCube")
			volume_cube.name = "Volume Cube"
			#Background
			volume_cube.inputs[1].default_value = 0.0
			
			#node Separate Geometry
			separate_geometry = _mn_utils_style_surface_old.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry.name = "Separate Geometry"
			separate_geometry.domain = 'POINT'
			
			#node Mesh to Points
			mesh_to_points = _mn_utils_style_surface_old.nodes.new("GeometryNodeMeshToPoints")
			mesh_to_points.name = "Mesh to Points"
			mesh_to_points.mode = 'VERTICES'
			#Selection
			mesh_to_points.inputs[1].default_value = True
			#Position
			mesh_to_points.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Radius
			mesh_to_points.inputs[3].default_value = 0.05000000074505806
			
			#node Group.001
			group_001 = _mn_utils_style_surface_old.nodes.new("GeometryNodeGroup")
			group_001.name = "Group.001"
			group_001.node_tree = _surface_blur_color
			
			#node Group.002
			group_002 = _mn_utils_style_surface_old.nodes.new("GeometryNodeGroup")
			group_002.name = "Group.002"
			group_002.node_tree = _surface_sample_color
			
			#node Group.003
			group_003 = _mn_utils_style_surface_old.nodes.new("GeometryNodeGroup")
			group_003.name = "Group.003"
			group_003.node_tree = _surface_blur_postion
			
			#node Volume to Mesh
			volume_to_mesh = _mn_utils_style_surface_old.nodes.new("GeometryNodeVolumeToMesh")
			volume_to_mesh.name = "Volume to Mesh"
			volume_to_mesh.resolution_mode = 'GRID'
			#Threshold
			volume_to_mesh.inputs[3].default_value = 0.10000000149011612
			#Adaptivity
			volume_to_mesh.inputs[4].default_value = 0.0
			
			#node Group.005
			group_005 = _mn_utils_style_surface_old.nodes.new("GeometryNodeGroup")
			group_005.name = "Group.005"
			group_005.node_tree = _surface_compute_density_from_points
			
			#node Group.004
			group_004 = _mn_utils_style_surface_old.nodes.new("GeometryNodeGroup")
			group_004.name = "Group.004"
			group_004.node_tree = _utils_bounding_box
			
			
			
			#Set parents
			volume_cube.parent = frame_002
			volume_to_mesh.parent = frame_002
			
			#Set locations
			frame_002.location = (670.7268676757812, 112.1966552734375)
			reroute_009_1.location = (3420.0, 420.0)
			group_output_5.location = (3600.0, 240.0)
			math_001_2.location = (1080.0, 180.0)
			reroute_001_2.location = (1000.0, 380.0)
			set_material.location = (3300.0, 360.0)
			group_input_002.location = (1920.0, 240.0)
			set_shade_smooth.location = (2320.0, 360.0)
			reroute_006_1.location = (3240.0, 0.0)
			reroute_004.location = (980.0, -20.0)
			reroute_005_1.location = (2660.0, -60.0)
			group_input_5.location = (300.0, 320.0)
			volume_cube.location = (890.0, 370.0)
			separate_geometry.location = (580.0, 420.0)
			mesh_to_points.location = (740.0, 420.0)
			group_001.location = (2820.0, 340.0)
			group_002.location = (2820.0, 160.0)
			group_003.location = (2520.0, 360.0)
			volume_to_mesh.location = (1069.273193359375, 307.8033447265625)
			group_005.location = (1080.0, 580.0)
			group_004.location = (1080.0, 420.0)
			
			#Set dimensions
			frame_002.width, frame_002.height = 409.50006103515625, 277.0
			reroute_009_1.width, reroute_009_1.height = 16.0, 100.0
			group_output_5.width, group_output_5.height = 140.0, 100.0
			math_001_2.width, math_001_2.height = 140.0, 100.0
			reroute_001_2.width, reroute_001_2.height = 16.0, 100.0
			set_material.width, set_material.height = 140.0, 100.0
			group_input_002.width, group_input_002.height = 154.36306762695312, 100.0
			set_shade_smooth.width, set_shade_smooth.height = 140.0, 100.0
			reroute_006_1.width, reroute_006_1.height = 16.0, 100.0
			reroute_004.width, reroute_004.height = 16.0, 100.0
			reroute_005_1.width, reroute_005_1.height = 16.0, 100.0
			group_input_5.width, group_input_5.height = 140.0, 100.0
			volume_cube.width, volume_cube.height = 140.0, 100.0
			separate_geometry.width, separate_geometry.height = 140.0, 100.0
			mesh_to_points.width, mesh_to_points.height = 140.0, 100.0
			group_001.width, group_001.height = 400.0, 100.0
			group_002.width, group_002.height = 400.0, 100.0
			group_003.width, group_003.height = 271.52978515625, 100.0
			volume_to_mesh.width, volume_to_mesh.height = 170.0, 100.0
			group_005.width, group_005.height = 400.0, 100.0
			group_004.width, group_004.height = 400.0, 100.0
			
			#initialize _mn_utils_style_surface_old links
			#volume_cube.Volume -> volume_to_mesh.Volume
			_mn_utils_style_surface_old.links.new(volume_cube.outputs[0], volume_to_mesh.inputs[0])
			#group_004.Min -> volume_cube.Min
			_mn_utils_style_surface_old.links.new(group_004.outputs[0], volume_cube.inputs[2])
			#group_004.Max -> volume_cube.Max
			_mn_utils_style_surface_old.links.new(group_004.outputs[1], volume_cube.inputs[3])
			#group_004.X -> volume_cube.Resolution X
			_mn_utils_style_surface_old.links.new(group_004.outputs[2], volume_cube.inputs[4])
			#group_004.Y -> volume_cube.Resolution Y
			_mn_utils_style_surface_old.links.new(group_004.outputs[3], volume_cube.inputs[5])
			#group_004.Z -> volume_cube.Resolution Z
			_mn_utils_style_surface_old.links.new(group_004.outputs[4], volume_cube.inputs[6])
			#reroute_006_1.Output -> set_material.Material
			_mn_utils_style_surface_old.links.new(reroute_006_1.outputs[0], set_material.inputs[2])
			#mesh_to_points.Points -> reroute_004.Input
			_mn_utils_style_surface_old.links.new(mesh_to_points.outputs[0], reroute_004.inputs[0])
			#set_material.Geometry -> group_output_5.Geometry
			_mn_utils_style_surface_old.links.new(set_material.outputs[0], group_output_5.inputs[0])
			#reroute_009_1.Output -> group_output_5.Volume
			_mn_utils_style_surface_old.links.new(reroute_009_1.outputs[0], group_output_5.inputs[1])
			#separate_geometry.Selection -> mesh_to_points.Mesh
			_mn_utils_style_surface_old.links.new(separate_geometry.outputs[0], mesh_to_points.inputs[0])
			#group_001.Geometry -> set_material.Geometry
			_mn_utils_style_surface_old.links.new(group_001.outputs[0], set_material.inputs[0])
			#group_002.Color -> group_001.Color
			_mn_utils_style_surface_old.links.new(group_002.outputs[0], group_001.inputs[2])
			#group_003.Geometry -> group_001.Geometry
			_mn_utils_style_surface_old.links.new(group_003.outputs[0], group_001.inputs[0])
			#group_input_002.Color by CA -> group_002.Sample CA
			_mn_utils_style_surface_old.links.new(group_input_002.outputs[6], group_002.inputs[1])
			#reroute_005_1.Output -> group_002.Atoms
			_mn_utils_style_surface_old.links.new(reroute_005_1.outputs[0], group_002.inputs[0])
			#set_shade_smooth.Geometry -> group_003.Geometry
			_mn_utils_style_surface_old.links.new(set_shade_smooth.outputs[0], group_003.inputs[0])
			#group_input_002.Interpolate Color -> group_001.Blur Iterations
			_mn_utils_style_surface_old.links.new(group_input_002.outputs[7], group_001.inputs[1])
			#group_input_002.Surface Smoothing -> group_003.Iterations
			_mn_utils_style_surface_old.links.new(group_input_002.outputs[5], group_003.inputs[1])
			#reroute_004.Output -> reroute_005_1.Input
			_mn_utils_style_surface_old.links.new(reroute_004.outputs[0], reroute_005_1.inputs[0])
			#group_input_002.Material -> reroute_006_1.Input
			_mn_utils_style_surface_old.links.new(group_input_002.outputs[9], reroute_006_1.inputs[0])
			#group_input_002.Shade Smooth -> set_shade_smooth.Shade Smooth
			_mn_utils_style_surface_old.links.new(group_input_002.outputs[8], set_shade_smooth.inputs[2])
			#math_001_2.Value -> group_004.Subdivisions
			_mn_utils_style_surface_old.links.new(math_001_2.outputs[0], group_004.inputs[1])
			#reroute_001_2.Output -> group_004.Geometry
			_mn_utils_style_surface_old.links.new(reroute_001_2.outputs[0], group_004.inputs[0])
			#reroute_001_2.Output -> group_005.Atoms
			_mn_utils_style_surface_old.links.new(reroute_001_2.outputs[0], group_005.inputs[0])
			#group_input_5.Scale Radii -> group_005.Scale Radius
			_mn_utils_style_surface_old.links.new(group_input_5.outputs[3], group_005.inputs[1])
			#group_input_5.Atoms -> separate_geometry.Geometry
			_mn_utils_style_surface_old.links.new(group_input_5.outputs[0], separate_geometry.inputs[0])
			#group_input_5.Selection -> separate_geometry.Selection
			_mn_utils_style_surface_old.links.new(group_input_5.outputs[1], separate_geometry.inputs[1])
			#mesh_to_points.Points -> reroute_001_2.Input
			_mn_utils_style_surface_old.links.new(mesh_to_points.outputs[0], reroute_001_2.inputs[0])
			#group_input_5.Quality -> math_001_2.Value
			_mn_utils_style_surface_old.links.new(group_input_5.outputs[2], math_001_2.inputs[0])
			#group_input_5.Probe Size -> group_005.Probe Size
			_mn_utils_style_surface_old.links.new(group_input_5.outputs[4], group_005.inputs[2])
			#volume_to_mesh.Mesh -> set_shade_smooth.Geometry
			_mn_utils_style_surface_old.links.new(volume_to_mesh.outputs[0], set_shade_smooth.inputs[0])
			#volume_cube.Volume -> reroute_009_1.Input
			_mn_utils_style_surface_old.links.new(volume_cube.outputs[0], reroute_009_1.inputs[0])
			#group_005.Result -> volume_cube.Density
			_mn_utils_style_surface_old.links.new(group_005.outputs[0], volume_cube.inputs[0])
			return _mn_utils_style_surface_old

		_mn_utils_style_surface_old = _mn_utils_style_surface_old_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".MN_utils_style_surface_old", type = 'NODES')
		mod.node_group = _mn_utils_style_surface_old
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_MN_utils_style_surface_old.bl_idname)
			
def register():
	bpy.utils.register_class(_MN_utils_style_surface_old)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_MN_utils_style_surface_old)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
