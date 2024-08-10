bl_info = {
	"name" : "Style Preset 3",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Style_Preset_3(bpy.types.Operator):
	bl_idname = "node.style_preset_3"
	bl_label = "Style Preset 3"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _mn_utils_to_instance_centred node group
		def _mn_utils_to_instance_centred_node_group():
			_mn_utils_to_instance_centred = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_utils_to_instance_centred")

			_mn_utils_to_instance_centred.color_tag = 'NONE'
			_mn_utils_to_instance_centred.description = ""

			
			#_mn_utils_to_instance_centred interface
			#Socket Geometry
			geometry_socket = _mn_utils_to_instance_centred.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket.attribute_domain = 'POINT'
			
			#Socket Input
			input_socket = _mn_utils_to_instance_centred.interface.new_socket(name = "Input", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			input_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_utils_to_instance_centred nodes
			#node Bounding Box
			bounding_box = _mn_utils_to_instance_centred.nodes.new("GeometryNodeBoundBox")
			bounding_box.name = "Bounding Box"
			
			#node Transform Geometry
			transform_geometry = _mn_utils_to_instance_centred.nodes.new("GeometryNodeTransform")
			transform_geometry.name = "Transform Geometry"
			transform_geometry.mode = 'COMPONENTS'
			#Rotation
			transform_geometry.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Scale
			transform_geometry.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Transform Geometry.001
			transform_geometry_001 = _mn_utils_to_instance_centred.nodes.new("GeometryNodeTransform")
			transform_geometry_001.name = "Transform Geometry.001"
			transform_geometry_001.mode = 'COMPONENTS'
			#Rotation
			transform_geometry_001.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Scale
			transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Vector Math
			vector_math = _mn_utils_to_instance_centred.nodes.new("ShaderNodeVectorMath")
			vector_math.label = "-x"
			vector_math.name = "Vector Math"
			vector_math.hide = True
			vector_math.operation = 'SCALE'
			#Scale
			vector_math.inputs[3].default_value = -1.0
			
			#node Mix
			mix = _mn_utils_to_instance_centred.nodes.new("ShaderNodeMix")
			mix.label = "lerp(a, b, 0.5)"
			mix.name = "Mix"
			mix.hide = True
			mix.blend_type = 'MIX'
			mix.clamp_factor = True
			mix.clamp_result = False
			mix.data_type = 'VECTOR'
			mix.factor_mode = 'UNIFORM'
			#Factor_Float
			mix.inputs[0].default_value = 0.5
			
			#node Group Input
			group_input = _mn_utils_to_instance_centred.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Geometry to Instance
			geometry_to_instance = _mn_utils_to_instance_centred.nodes.new("GeometryNodeGeometryToInstance")
			geometry_to_instance.name = "Geometry to Instance"
			
			#node Group Output
			group_output = _mn_utils_to_instance_centred.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Reroute.001
			reroute_001 = _mn_utils_to_instance_centred.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			
			
			
			#Set locations
			bounding_box.location = (-338.7969970703125, -30.0)
			transform_geometry.location = (21.2030029296875, 90.0)
			transform_geometry_001.location = (361.2030029296875, 90.0)
			vector_math.location = (-178.7969970703125, -50.0)
			mix.location = (-178.7969970703125, -90.0)
			group_input.location = (-600.0, 100.0)
			geometry_to_instance.location = (181.2030029296875, 90.0)
			group_output.location = (560.0, 100.0)
			reroute_001.location = (-380.0, 40.0)
			
			#Set dimensions
			bounding_box.width, bounding_box.height = 140.0, 100.0
			transform_geometry.width, transform_geometry.height = 140.0, 100.0
			transform_geometry_001.width, transform_geometry_001.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			mix.width, mix.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			geometry_to_instance.width, geometry_to_instance.height = 160.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			
			#initialize _mn_utils_to_instance_centred links
			#reroute_001.Output -> transform_geometry.Geometry
			_mn_utils_to_instance_centred.links.new(reroute_001.outputs[0], transform_geometry.inputs[0])
			#reroute_001.Output -> bounding_box.Geometry
			_mn_utils_to_instance_centred.links.new(reroute_001.outputs[0], bounding_box.inputs[0])
			#transform_geometry.Geometry -> geometry_to_instance.Geometry
			_mn_utils_to_instance_centred.links.new(transform_geometry.outputs[0], geometry_to_instance.inputs[0])
			#mix.Result -> vector_math.Vector
			_mn_utils_to_instance_centred.links.new(mix.outputs[1], vector_math.inputs[0])
			#vector_math.Vector -> transform_geometry.Translation
			_mn_utils_to_instance_centred.links.new(vector_math.outputs[0], transform_geometry.inputs[1])
			#geometry_to_instance.Instances -> transform_geometry_001.Geometry
			_mn_utils_to_instance_centred.links.new(geometry_to_instance.outputs[0], transform_geometry_001.inputs[0])
			#bounding_box.Min -> mix.A
			_mn_utils_to_instance_centred.links.new(bounding_box.outputs[1], mix.inputs[4])
			#mix.Result -> transform_geometry_001.Translation
			_mn_utils_to_instance_centred.links.new(mix.outputs[1], transform_geometry_001.inputs[1])
			#bounding_box.Max -> mix.B
			_mn_utils_to_instance_centred.links.new(bounding_box.outputs[2], mix.inputs[5])
			#group_input.Input -> reroute_001.Input
			_mn_utils_to_instance_centred.links.new(group_input.outputs[0], reroute_001.inputs[0])
			#transform_geometry_001.Geometry -> group_output.Geometry
			_mn_utils_to_instance_centred.links.new(transform_geometry_001.outputs[0], group_output.inputs[0])
			return _mn_utils_to_instance_centred

		_mn_utils_to_instance_centred = _mn_utils_to_instance_centred_node_group()

		#initialize _mn_surface_smooth_bumps node group
		def _mn_surface_smooth_bumps_node_group():
			_mn_surface_smooth_bumps = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_surface_smooth_bumps")

			_mn_surface_smooth_bumps.color_tag = 'NONE'
			_mn_surface_smooth_bumps.description = ""

			_mn_surface_smooth_bumps.is_modifier = True
			
			#_mn_surface_smooth_bumps interface
			#Socket Geometry
			geometry_socket_1 = _mn_surface_smooth_bumps.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_1.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_2 = _mn_surface_smooth_bumps.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_2.attribute_domain = 'POINT'
			
			
			#initialize _mn_surface_smooth_bumps nodes
			#node Frame
			frame = _mn_surface_smooth_bumps.nodes.new("NodeFrame")
			frame.label = "Smoothen out weird bumps from meshing"
			frame.name = "Frame"
			frame.label_size = 20
			frame.shrink = True
			
			#node Group Input
			group_input_1 = _mn_surface_smooth_bumps.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			
			#node Group Output
			group_output_1 = _mn_surface_smooth_bumps.nodes.new("NodeGroupOutput")
			group_output_1.name = "Group Output"
			group_output_1.is_active_output = True
			
			#node Set Position.001
			set_position_001 = _mn_surface_smooth_bumps.nodes.new("GeometryNodeSetPosition")
			set_position_001.name = "Set Position.001"
			#Offset
			set_position_001.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Blur Attribute
			blur_attribute = _mn_surface_smooth_bumps.nodes.new("GeometryNodeBlurAttribute")
			blur_attribute.name = "Blur Attribute"
			blur_attribute.data_type = 'FLOAT_VECTOR'
			#Iterations
			blur_attribute.inputs[1].default_value = 4
			#Weight
			blur_attribute.inputs[2].default_value = 1.0
			
			#node Position
			position = _mn_surface_smooth_bumps.nodes.new("GeometryNodeInputPosition")
			position.name = "Position"
			
			#node Compare
			compare = _mn_surface_smooth_bumps.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'EQUAL'
			#B_INT
			compare.inputs[3].default_value = 3
			
			#node Vertex Neighbors
			vertex_neighbors = _mn_surface_smooth_bumps.nodes.new("GeometryNodeInputMeshVertexNeighbors")
			vertex_neighbors.name = "Vertex Neighbors"
			
			#node Edge Vertices
			edge_vertices = _mn_surface_smooth_bumps.nodes.new("GeometryNodeInputMeshEdgeVertices")
			edge_vertices.name = "Edge Vertices"
			
			#node Evaluate at Index.001
			evaluate_at_index_001 = _mn_surface_smooth_bumps.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001.name = "Evaluate at Index.001"
			evaluate_at_index_001.data_type = 'BOOLEAN'
			evaluate_at_index_001.domain = 'POINT'
			
			#node Evaluate at Index
			evaluate_at_index = _mn_surface_smooth_bumps.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index.name = "Evaluate at Index"
			evaluate_at_index.data_type = 'BOOLEAN'
			evaluate_at_index.domain = 'POINT'
			
			#node Boolean Math
			boolean_math = _mn_surface_smooth_bumps.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'AND'
			
			#node Edges to Face Groups
			edges_to_face_groups = _mn_surface_smooth_bumps.nodes.new("GeometryNodeEdgesToFaceGroups")
			edges_to_face_groups.name = "Edges to Face Groups"
			
			#node Face Group Boundaries
			face_group_boundaries = _mn_surface_smooth_bumps.nodes.new("GeometryNodeMeshFaceSetBoundaries")
			face_group_boundaries.name = "Face Group Boundaries"
			
			
			
			#Set parents
			compare.parent = frame
			vertex_neighbors.parent = frame
			edge_vertices.parent = frame
			evaluate_at_index_001.parent = frame
			evaluate_at_index.parent = frame
			boolean_math.parent = frame
			edges_to_face_groups.parent = frame
			face_group_boundaries.parent = frame
			
			#Set locations
			frame.location = (-385.91619873046875, 67.19032287597656)
			group_input_1.location = (-610.1629638671875, 0.0)
			group_output_1.location = (900.947509765625, -17.612947463989258)
			set_position_001.location = (460.784423828125, 10.757638931274414)
			blur_attribute.location = (460.0, -220.0)
			position.location = (460.0, -400.0)
			compare.location = (-220.0, -560.0)
			vertex_neighbors.location = (-380.0, -560.0)
			edge_vertices.location = (-220.0, -420.0)
			evaluate_at_index_001.location = (-60.0, -580.0)
			evaluate_at_index.location = (-60.0, -420.0)
			boolean_math.location = (100.0, -420.0)
			edges_to_face_groups.location = (100.0, -560.0)
			face_group_boundaries.location = (103.8720703125, -322.7563171386719)
			
			#Set dimensions
			frame.width, frame.height = 694.0, 477.0
			group_input_1.width, group_input_1.height = 140.0, 100.0
			group_output_1.width, group_output_1.height = 140.0, 100.0
			set_position_001.width, set_position_001.height = 140.0, 100.0
			blur_attribute.width, blur_attribute.height = 140.0, 100.0
			position.width, position.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			vertex_neighbors.width, vertex_neighbors.height = 140.0, 100.0
			edge_vertices.width, edge_vertices.height = 140.0, 100.0
			evaluate_at_index_001.width, evaluate_at_index_001.height = 140.0, 100.0
			evaluate_at_index.width, evaluate_at_index.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			edges_to_face_groups.width, edges_to_face_groups.height = 140.0, 100.0
			face_group_boundaries.width, face_group_boundaries.height = 150.0, 100.0
			
			#initialize _mn_surface_smooth_bumps links
			#set_position_001.Geometry -> group_output_1.Geometry
			_mn_surface_smooth_bumps.links.new(set_position_001.outputs[0], group_output_1.inputs[0])
			#group_input_1.Geometry -> set_position_001.Geometry
			_mn_surface_smooth_bumps.links.new(group_input_1.outputs[0], set_position_001.inputs[0])
			#vertex_neighbors.Vertex Count -> compare.A
			_mn_surface_smooth_bumps.links.new(vertex_neighbors.outputs[0], compare.inputs[2])
			#compare.Result -> evaluate_at_index.Value
			_mn_surface_smooth_bumps.links.new(compare.outputs[0], evaluate_at_index.inputs[1])
			#compare.Result -> evaluate_at_index_001.Value
			_mn_surface_smooth_bumps.links.new(compare.outputs[0], evaluate_at_index_001.inputs[1])
			#edge_vertices.Vertex Index 1 -> evaluate_at_index.Index
			_mn_surface_smooth_bumps.links.new(edge_vertices.outputs[0], evaluate_at_index.inputs[0])
			#edge_vertices.Vertex Index 2 -> evaluate_at_index_001.Index
			_mn_surface_smooth_bumps.links.new(edge_vertices.outputs[1], evaluate_at_index_001.inputs[0])
			#evaluate_at_index.Value -> boolean_math.Boolean
			_mn_surface_smooth_bumps.links.new(evaluate_at_index.outputs[0], boolean_math.inputs[0])
			#evaluate_at_index_001.Value -> boolean_math.Boolean
			_mn_surface_smooth_bumps.links.new(evaluate_at_index_001.outputs[0], boolean_math.inputs[1])
			#boolean_math.Boolean -> edges_to_face_groups.Boundary Edges
			_mn_surface_smooth_bumps.links.new(boolean_math.outputs[0], edges_to_face_groups.inputs[0])
			#edges_to_face_groups.Face Group ID -> face_group_boundaries.Face Group ID
			_mn_surface_smooth_bumps.links.new(edges_to_face_groups.outputs[0], face_group_boundaries.inputs[0])
			#blur_attribute.Value -> set_position_001.Position
			_mn_surface_smooth_bumps.links.new(blur_attribute.outputs[0], set_position_001.inputs[2])
			#position.Position -> blur_attribute.Value
			_mn_surface_smooth_bumps.links.new(position.outputs[0], blur_attribute.inputs[0])
			#face_group_boundaries.Boundary Edges -> set_position_001.Selection
			_mn_surface_smooth_bumps.links.new(face_group_boundaries.outputs[0], set_position_001.inputs[1])
			return _mn_surface_smooth_bumps

		_mn_surface_smooth_bumps = _mn_surface_smooth_bumps_node_group()

		#initialize _utils_bounding_box node group
		def _utils_bounding_box_node_group():
			_utils_bounding_box = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".utils_bounding_box")

			_utils_bounding_box.color_tag = 'NONE'
			_utils_bounding_box.description = ""

			
			#_utils_bounding_box interface
			#Socket Min
			min_socket = _utils_bounding_box.interface.new_socket(name = "Min", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			min_socket.subtype = 'NONE'
			min_socket.default_value = (0.0, 0.0, 0.0)
			min_socket.min_value = -3.4028234663852886e+38
			min_socket.max_value = 3.4028234663852886e+38
			min_socket.attribute_domain = 'POINT'
			
			#Socket Max
			max_socket = _utils_bounding_box.interface.new_socket(name = "Max", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			max_socket.subtype = 'NONE'
			max_socket.default_value = (0.0, 0.0, 0.0)
			max_socket.min_value = -3.4028234663852886e+38
			max_socket.max_value = 3.4028234663852886e+38
			max_socket.attribute_domain = 'POINT'
			
			#Socket X
			x_socket = _utils_bounding_box.interface.new_socket(name = "X", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			x_socket.subtype = 'NONE'
			x_socket.default_value = 0
			x_socket.min_value = -2147483648
			x_socket.max_value = 2147483647
			x_socket.attribute_domain = 'POINT'
			
			#Socket Y
			y_socket = _utils_bounding_box.interface.new_socket(name = "Y", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			y_socket.subtype = 'NONE'
			y_socket.default_value = 0
			y_socket.min_value = -2147483648
			y_socket.max_value = 2147483647
			y_socket.attribute_domain = 'POINT'
			
			#Socket Z
			z_socket = _utils_bounding_box.interface.new_socket(name = "Z", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			z_socket.subtype = 'NONE'
			z_socket.default_value = 0
			z_socket.min_value = -2147483648
			z_socket.max_value = 2147483647
			z_socket.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_3 = _utils_bounding_box.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_3.attribute_domain = 'POINT'
			
			#Socket Subdivisions
			subdivisions_socket = _utils_bounding_box.interface.new_socket(name = "Subdivisions", in_out='INPUT', socket_type = 'NodeSocketFloat')
			subdivisions_socket.subtype = 'NONE'
			subdivisions_socket.default_value = 16.700000762939453
			subdivisions_socket.min_value = -10000.0
			subdivisions_socket.max_value = 10000.0
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
			reroute = _utils_bounding_box.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Reroute.002
			reroute_002 = _utils_bounding_box.nodes.new("NodeReroute")
			reroute_002.name = "Reroute.002"
			#node Group Output
			group_output_2 = _utils_bounding_box.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Separate XYZ
			separate_xyz = _utils_bounding_box.nodes.new("ShaderNodeSeparateXYZ")
			separate_xyz.name = "Separate XYZ"
			
			#node Math
			math = _utils_bounding_box.nodes.new("ShaderNodeMath")
			math.name = "Math"
			math.hide = True
			math.operation = 'MAXIMUM'
			math.use_clamp = False
			#Value_001
			math.inputs[1].default_value = 2.0
			
			#node Math.001
			math_001 = _utils_bounding_box.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.hide = True
			math_001.operation = 'MAXIMUM'
			math_001.use_clamp = False
			#Value_001
			math_001.inputs[1].default_value = 2.0
			
			#node Math.002
			math_002 = _utils_bounding_box.nodes.new("ShaderNodeMath")
			math_002.name = "Math.002"
			math_002.hide = True
			math_002.operation = 'MAXIMUM'
			math_002.use_clamp = False
			#Value_001
			math_002.inputs[1].default_value = 2.0
			
			#node Group Input
			group_input_2 = _utils_bounding_box.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
			#node Bounding Box
			bounding_box_1 = _utils_bounding_box.nodes.new("GeometryNodeBoundBox")
			bounding_box_1.name = "Bounding Box"
			
			#node Value
			value = _utils_bounding_box.nodes.new("ShaderNodeValue")
			value.name = "Value"
			
			value.outputs[0].default_value = 0.009999999776482582
			#node Reroute.001
			reroute_001_1 = _utils_bounding_box.nodes.new("NodeReroute")
			reroute_001_1.name = "Reroute.001"
			#node Vector Math
			vector_math_1 = _utils_bounding_box.nodes.new("ShaderNodeVectorMath")
			vector_math_1.name = "Vector Math"
			vector_math_1.operation = 'SUBTRACT'
			
			#node Vector Math.001
			vector_math_001 = _utils_bounding_box.nodes.new("ShaderNodeVectorMath")
			vector_math_001.name = "Vector Math.001"
			vector_math_001.operation = 'ADD'
			
			#node Vector Math.004
			vector_math_004 = _utils_bounding_box.nodes.new("ShaderNodeVectorMath")
			vector_math_004.name = "Vector Math.004"
			vector_math_004.operation = 'SNAP'
			
			#node Vector Math.005
			vector_math_005 = _utils_bounding_box.nodes.new("ShaderNodeVectorMath")
			vector_math_005.name = "Vector Math.005"
			vector_math_005.operation = 'SNAP'
			
			#node Math.003
			math_003 = _utils_bounding_box.nodes.new("ShaderNodeMath")
			math_003.name = "Math.003"
			math_003.operation = 'MULTIPLY'
			math_003.use_clamp = False
			#Value_001
			math_003.inputs[1].default_value = 2.0
			
			
			
			
			#Set locations
			vector_math_002.location = (-36.8055419921875, 112.27713012695312)
			vector_math_003.location = (123.1944580078125, 112.27713012695312)
			reroute.location = (40.0, 160.0)
			reroute_002.location = (60.0, 140.0)
			group_output_2.location = (700.0, 200.0)
			separate_xyz.location = (283.1944580078125, 112.27713012695312)
			math.location = (480.0, 120.0)
			math_001.location = (480.0, 80.0)
			math_002.location = (480.0, 40.0)
			group_input_2.location = (-1065.6466064453125, 104.66636657714844)
			bounding_box_1.location = (-885.6466064453125, 44.6663703918457)
			value.location = (-1025.04443359375, -182.63922119140625)
			reroute_001_1.location = (-439.06280517578125, -225.71304321289062)
			vector_math_1.location = (-313.41741943359375, 140.0)
			vector_math_001.location = (-313.41741943359375, 0.0)
			vector_math_004.location = (-564.7015380859375, 104.61347961425781)
			vector_math_005.location = (-563.52734375, -39.964500427246094)
			math_003.location = (-640.0, -200.0)
			
			#Set dimensions
			vector_math_002.width, vector_math_002.height = 140.0, 100.0
			vector_math_003.width, vector_math_003.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			reroute_002.width, reroute_002.height = 16.0, 100.0
			group_output_2.width, group_output_2.height = 140.0, 100.0
			separate_xyz.width, separate_xyz.height = 116.41741943359375, 100.0
			math.width, math.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			math_002.width, math_002.height = 140.0, 100.0
			group_input_2.width, group_input_2.height = 140.0, 100.0
			bounding_box_1.width, bounding_box_1.height = 140.0, 100.0
			value.width, value.height = 140.0, 100.0
			reroute_001_1.width, reroute_001_1.height = 16.0, 100.0
			vector_math_1.width, vector_math_1.height = 140.0, 100.0
			vector_math_001.width, vector_math_001.height = 140.0, 100.0
			vector_math_004.width, vector_math_004.height = 140.0, 100.0
			vector_math_005.width, vector_math_005.height = 140.0, 100.0
			math_003.width, math_003.height = 140.0, 100.0
			
			#initialize _utils_bounding_box links
			#vector_math_002.Vector -> vector_math_003.Vector
			_utils_bounding_box.links.new(vector_math_002.outputs[0], vector_math_003.inputs[0])
			#vector_math_001.Vector -> vector_math_002.Vector
			_utils_bounding_box.links.new(vector_math_001.outputs[0], vector_math_002.inputs[0])
			#vector_math_003.Vector -> separate_xyz.Vector
			_utils_bounding_box.links.new(vector_math_003.outputs[0], separate_xyz.inputs[0])
			#reroute_001_1.Output -> vector_math_1.Vector
			_utils_bounding_box.links.new(reroute_001_1.outputs[0], vector_math_1.inputs[1])
			#vector_math_1.Vector -> vector_math_002.Vector
			_utils_bounding_box.links.new(vector_math_1.outputs[0], vector_math_002.inputs[1])
			#reroute_001_1.Output -> vector_math_001.Vector
			_utils_bounding_box.links.new(reroute_001_1.outputs[0], vector_math_001.inputs[1])
			#group_input_2.Subdivisions -> vector_math_003.Scale
			_utils_bounding_box.links.new(group_input_2.outputs[1], vector_math_003.inputs[3])
			#group_input_2.Geometry -> bounding_box_1.Geometry
			_utils_bounding_box.links.new(group_input_2.outputs[0], bounding_box_1.inputs[0])
			#reroute.Output -> group_output_2.Min
			_utils_bounding_box.links.new(reroute.outputs[0], group_output_2.inputs[0])
			#reroute_002.Output -> group_output_2.Max
			_utils_bounding_box.links.new(reroute_002.outputs[0], group_output_2.inputs[1])
			#math_001.Value -> group_output_2.Y
			_utils_bounding_box.links.new(math_001.outputs[0], group_output_2.inputs[3])
			#math_002.Value -> group_output_2.Z
			_utils_bounding_box.links.new(math_002.outputs[0], group_output_2.inputs[4])
			#vector_math_1.Vector -> reroute.Input
			_utils_bounding_box.links.new(vector_math_1.outputs[0], reroute.inputs[0])
			#vector_math_001.Vector -> reroute_002.Input
			_utils_bounding_box.links.new(vector_math_001.outputs[0], reroute_002.inputs[0])
			#separate_xyz.X -> math.Value
			_utils_bounding_box.links.new(separate_xyz.outputs[0], math.inputs[0])
			#math.Value -> group_output_2.X
			_utils_bounding_box.links.new(math.outputs[0], group_output_2.inputs[2])
			#separate_xyz.Y -> math_001.Value
			_utils_bounding_box.links.new(separate_xyz.outputs[1], math_001.inputs[0])
			#separate_xyz.Z -> math_002.Value
			_utils_bounding_box.links.new(separate_xyz.outputs[2], math_002.inputs[0])
			#value.Value -> vector_math_004.Vector
			_utils_bounding_box.links.new(value.outputs[0], vector_math_004.inputs[1])
			#bounding_box_1.Min -> vector_math_004.Vector
			_utils_bounding_box.links.new(bounding_box_1.outputs[1], vector_math_004.inputs[0])
			#vector_math_004.Vector -> vector_math_1.Vector
			_utils_bounding_box.links.new(vector_math_004.outputs[0], vector_math_1.inputs[0])
			#vector_math_005.Vector -> vector_math_001.Vector
			_utils_bounding_box.links.new(vector_math_005.outputs[0], vector_math_001.inputs[0])
			#bounding_box_1.Max -> vector_math_005.Vector
			_utils_bounding_box.links.new(bounding_box_1.outputs[2], vector_math_005.inputs[0])
			#value.Value -> math_003.Value
			_utils_bounding_box.links.new(value.outputs[0], math_003.inputs[0])
			#value.Value -> vector_math_005.Vector
			_utils_bounding_box.links.new(value.outputs[0], vector_math_005.inputs[1])
			#math_003.Value -> reroute_001_1.Input
			_utils_bounding_box.links.new(math_003.outputs[0], reroute_001_1.inputs[0])
			return _utils_bounding_box

		_utils_bounding_box = _utils_bounding_box_node_group()

		#initialize _surface_compute_density_from_points node group
		def _surface_compute_density_from_points_node_group():
			_surface_compute_density_from_points = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".surface_compute_density_from_points")

			_surface_compute_density_from_points.color_tag = 'NONE'
			_surface_compute_density_from_points.description = ""

			
			#_surface_compute_density_from_points interface
			#Socket Result
			result_socket = _surface_compute_density_from_points.interface.new_socket(name = "Result", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			result_socket.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket = _surface_compute_density_from_points.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket.attribute_domain = 'POINT'
			atoms_socket.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Scale Radius
			scale_radius_socket = _surface_compute_density_from_points.interface.new_socket(name = "Scale Radius", in_out='INPUT', socket_type = 'NodeSocketFloat')
			scale_radius_socket.subtype = 'NONE'
			scale_radius_socket.default_value = 1.0
			scale_radius_socket.min_value = -10000.0
			scale_radius_socket.max_value = 10000.0
			scale_radius_socket.attribute_domain = 'POINT'
			
			#Socket Probe Size
			probe_size_socket = _surface_compute_density_from_points.interface.new_socket(name = "Probe Size", in_out='INPUT', socket_type = 'NodeSocketFloat')
			probe_size_socket.subtype = 'NONE'
			probe_size_socket.default_value = 0.0
			probe_size_socket.min_value = 0.0
			probe_size_socket.max_value = 10000.0
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
			reroute_1 = _surface_compute_density_from_points.nodes.new("NodeReroute")
			reroute_1.name = "Reroute"
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
			vector_math_004_1 = _surface_compute_density_from_points.nodes.new("ShaderNodeVectorMath")
			vector_math_004_1.name = "Vector Math.004"
			vector_math_004_1.operation = 'DISTANCE'
			
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
			math_001_1 = _surface_compute_density_from_points.nodes.new("ShaderNodeMath")
			math_001_1.name = "Math.001"
			math_001_1.operation = 'DIVIDE'
			math_001_1.use_clamp = False
			#Value_001
			math_001_1.inputs[1].default_value = 100.0
			
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
			math_003_1 = _surface_compute_density_from_points.nodes.new("ShaderNodeMath")
			math_003_1.name = "Math.003"
			math_003_1.operation = 'MULTIPLY'
			math_003_1.use_clamp = False
			
			#node Sample Index.001
			sample_index_001 = _surface_compute_density_from_points.nodes.new("GeometryNodeSampleIndex")
			sample_index_001.name = "Sample Index.001"
			sample_index_001.clamp = False
			sample_index_001.data_type = 'FLOAT'
			sample_index_001.domain = 'POINT'
			
			#node Named Attribute
			named_attribute = _surface_compute_density_from_points.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'FLOAT'
			#Name
			named_attribute.inputs[0].default_value = "vdw_radii"
			
			#node Reroute.002
			reroute_002_1 = _surface_compute_density_from_points.nodes.new("NodeReroute")
			reroute_002_1.name = "Reroute.002"
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
			reroute_001_2 = _surface_compute_density_from_points.nodes.new("NodeReroute")
			reroute_001_2.name = "Reroute.001"
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
			reroute_1.location = (-140.0, -280.0)
			group_output_3.location = (562.0, 220.0)
			compare_001.location = (382.0, 220.0)
			vector_math_004_1.location = (-140.0, -60.0)
			math_008.location = (162.0, 180.0)
			math_009.location = (-58.0, 216.76718139648438)
			math_001_1.location = (-280.0, 380.0)
			sample_index.location = (-278.0, 180.0)
			reroute_007.location = (-900.0, 60.0)
			math_003_1.location = (-780.0, 60.0)
			sample_index_001.location = (-840.0, 300.0)
			named_attribute.location = (-940.0, 60.0)
			reroute_002_1.location = (-1034.125244140625, 60.0)
			sample_index_003.location = (-940.0, -80.0)
			reroute_003.location = (-440.0, 180.0)
			reroute_001_2.location = (-1280.0, 60.0)
			group_input_3.location = (-1560.0, 100.0)
			sample_nearest.location = (-1260.0, 220.0)
			
			#Set dimensions
			sample_index_002.width, sample_index_002.height = 140.0, 100.0
			position_001.width, position_001.height = 140.0, 100.0
			reroute_1.width, reroute_1.height = 16.0, 100.0
			group_output_3.width, group_output_3.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			vector_math_004_1.width, vector_math_004_1.height = 140.0, 100.0
			math_008.width, math_008.height = 140.0, 100.0
			math_009.width, math_009.height = 140.0, 100.0
			math_001_1.width, math_001_1.height = 140.0, 100.0
			sample_index.width, sample_index.height = 140.0, 100.0
			reroute_007.width, reroute_007.height = 16.0, 100.0
			math_003_1.width, math_003_1.height = 140.0, 100.0
			sample_index_001.width, sample_index_001.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			reroute_002_1.width, reroute_002_1.height = 16.0, 100.0
			sample_index_003.width, sample_index_003.height = 140.0, 100.0
			reroute_003.width, reroute_003.height = 16.0, 100.0
			reroute_001_2.width, reroute_001_2.height = 16.0, 100.0
			group_input_3.width, group_input_3.height = 140.0, 100.0
			sample_nearest.width, sample_nearest.height = 140.0, 100.0
			
			#initialize _surface_compute_density_from_points links
			#reroute_003.Output -> sample_index.Index
			_surface_compute_density_from_points.links.new(reroute_003.outputs[0], sample_index.inputs[2])
			#math_008.Value -> compare_001.A
			_surface_compute_density_from_points.links.new(math_008.outputs[0], compare_001.inputs[0])
			#sample_index_002.Value -> vector_math_004_1.Vector
			_surface_compute_density_from_points.links.new(sample_index_002.outputs[0], vector_math_004_1.inputs[0])
			#reroute_003.Output -> sample_index_002.Index
			_surface_compute_density_from_points.links.new(reroute_003.outputs[0], sample_index_002.inputs[2])
			#reroute_1.Output -> vector_math_004_1.Vector
			_surface_compute_density_from_points.links.new(reroute_1.outputs[0], vector_math_004_1.inputs[1])
			#reroute_007.Output -> sample_index.Geometry
			_surface_compute_density_from_points.links.new(reroute_007.outputs[0], sample_index.inputs[0])
			#math_003_1.Value -> sample_index.Value
			_surface_compute_density_from_points.links.new(math_003_1.outputs[0], sample_index.inputs[1])
			#reroute_007.Output -> sample_index_002.Geometry
			_surface_compute_density_from_points.links.new(reroute_007.outputs[0], sample_index_002.inputs[0])
			#position_001.Position -> sample_index_002.Value
			_surface_compute_density_from_points.links.new(position_001.outputs[0], sample_index_002.inputs[1])
			#reroute_002_1.Output -> reroute_007.Input
			_surface_compute_density_from_points.links.new(reroute_002_1.outputs[0], reroute_007.inputs[0])
			#compare_001.Result -> group_output_3.Result
			_surface_compute_density_from_points.links.new(compare_001.outputs[0], group_output_3.inputs[0])
			#named_attribute.Attribute -> math_003_1.Value
			_surface_compute_density_from_points.links.new(named_attribute.outputs[0], math_003_1.inputs[0])
			#position_001.Position -> reroute_1.Input
			_surface_compute_density_from_points.links.new(position_001.outputs[0], reroute_1.inputs[0])
			#vector_math_004_1.Value -> math_008.Value
			_surface_compute_density_from_points.links.new(vector_math_004_1.outputs[1], math_008.inputs[1])
			#math_009.Value -> math_008.Value
			_surface_compute_density_from_points.links.new(math_009.outputs[0], math_008.inputs[0])
			#sample_index.Value -> math_009.Value
			_surface_compute_density_from_points.links.new(sample_index.outputs[0], math_009.inputs[0])
			#math_001_1.Value -> math_009.Value
			_surface_compute_density_from_points.links.new(math_001_1.outputs[0], math_009.inputs[1])
			#reroute_007.Output -> sample_index_001.Geometry
			_surface_compute_density_from_points.links.new(reroute_007.outputs[0], sample_index_001.inputs[0])
			#reroute_001_2.Output -> sample_nearest.Geometry
			_surface_compute_density_from_points.links.new(reroute_001_2.outputs[0], sample_nearest.inputs[0])
			#group_input_3.Atoms -> reroute_001_2.Input
			_surface_compute_density_from_points.links.new(group_input_3.outputs[0], reroute_001_2.inputs[0])
			#sample_nearest.Index -> sample_index_001.Index
			_surface_compute_density_from_points.links.new(sample_nearest.outputs[0], sample_index_001.inputs[2])
			#group_input_3.Probe Size -> sample_index_001.Value
			_surface_compute_density_from_points.links.new(group_input_3.outputs[2], sample_index_001.inputs[1])
			#sample_index_001.Value -> math_001_1.Value
			_surface_compute_density_from_points.links.new(sample_index_001.outputs[0], math_001_1.inputs[0])
			#sample_nearest.Index -> sample_index_003.Index
			_surface_compute_density_from_points.links.new(sample_nearest.outputs[0], sample_index_003.inputs[2])
			#group_input_3.Scale Radius -> sample_index_003.Value
			_surface_compute_density_from_points.links.new(group_input_3.outputs[1], sample_index_003.inputs[1])
			#sample_index_003.Value -> math_003_1.Value
			_surface_compute_density_from_points.links.new(sample_index_003.outputs[0], math_003_1.inputs[1])
			#reroute_001_2.Output -> reroute_002_1.Input
			_surface_compute_density_from_points.links.new(reroute_001_2.outputs[0], reroute_002_1.inputs[0])
			#reroute_002_1.Output -> sample_index_003.Geometry
			_surface_compute_density_from_points.links.new(reroute_002_1.outputs[0], sample_index_003.inputs[0])
			#sample_nearest.Index -> reroute_003.Input
			_surface_compute_density_from_points.links.new(sample_nearest.outputs[0], reroute_003.inputs[0])
			return _surface_compute_density_from_points

		_surface_compute_density_from_points = _surface_compute_density_from_points_node_group()

		#initialize _mn_constants_atom_name_nucleic node group
		def _mn_constants_atom_name_nucleic_node_group():
			_mn_constants_atom_name_nucleic = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_constants_atom_name_nucleic")

			_mn_constants_atom_name_nucleic.color_tag = 'NONE'
			_mn_constants_atom_name_nucleic.description = ""

			
			#_mn_constants_atom_name_nucleic interface
			#Socket Backbone Lower
			backbone_lower_socket = _mn_constants_atom_name_nucleic.interface.new_socket(name = "Backbone Lower", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			backbone_lower_socket.subtype = 'NONE'
			backbone_lower_socket.default_value = 0
			backbone_lower_socket.min_value = -2147483648
			backbone_lower_socket.max_value = 2147483647
			backbone_lower_socket.attribute_domain = 'POINT'
			
			#Socket Backbone Upper
			backbone_upper_socket = _mn_constants_atom_name_nucleic.interface.new_socket(name = "Backbone Upper", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			backbone_upper_socket.subtype = 'NONE'
			backbone_upper_socket.default_value = 0
			backbone_upper_socket.min_value = -2147483648
			backbone_upper_socket.max_value = 2147483647
			backbone_upper_socket.attribute_domain = 'POINT'
			
			#Socket Side Chain Lower
			side_chain_lower_socket = _mn_constants_atom_name_nucleic.interface.new_socket(name = "Side Chain Lower", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			side_chain_lower_socket.subtype = 'NONE'
			side_chain_lower_socket.default_value = 0
			side_chain_lower_socket.min_value = -2147483648
			side_chain_lower_socket.max_value = 2147483647
			side_chain_lower_socket.attribute_domain = 'POINT'
			
			#Socket Side Chain Upper
			side_chain_upper_socket = _mn_constants_atom_name_nucleic.interface.new_socket(name = "Side Chain Upper", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			side_chain_upper_socket.subtype = 'NONE'
			side_chain_upper_socket.default_value = 0
			side_chain_upper_socket.min_value = -2147483648
			side_chain_upper_socket.max_value = 2147483647
			side_chain_upper_socket.attribute_domain = 'POINT'
			
			#Socket Side Chain Joint Carbon
			side_chain_joint_carbon_socket = _mn_constants_atom_name_nucleic.interface.new_socket(name = "Side Chain Joint Carbon", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			side_chain_joint_carbon_socket.subtype = 'NONE'
			side_chain_joint_carbon_socket.default_value = 0
			side_chain_joint_carbon_socket.min_value = -2147483648
			side_chain_joint_carbon_socket.max_value = 2147483647
			side_chain_joint_carbon_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_constants_atom_name_nucleic nodes
			#node Group Output
			group_output_4 = _mn_constants_atom_name_nucleic.nodes.new("NodeGroupOutput")
			group_output_4.name = "Group Output"
			group_output_4.is_active_output = True
			
			#node Group Input
			group_input_4 = _mn_constants_atom_name_nucleic.nodes.new("NodeGroupInput")
			group_input_4.name = "Group Input"
			
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
			group_output_4.location = (190.0, 0.0)
			group_input_4.location = (-200.0, 0.0)
			integer.location = (0.0, -100.0)
			integer_002.location = (0.0, 100.0)
			integer_003.location = (0.0, 0.0)
			integer_001.location = (0.0, -200.0)
			integer_004.location = (0.0, -300.0)
			
			#Set dimensions
			group_output_4.width, group_output_4.height = 140.0, 100.0
			group_input_4.width, group_input_4.height = 140.0, 100.0
			integer.width, integer.height = 140.0, 100.0
			integer_002.width, integer_002.height = 140.0, 100.0
			integer_003.width, integer_003.height = 140.0, 100.0
			integer_001.width, integer_001.height = 140.0, 100.0
			integer_004.width, integer_004.height = 140.0, 100.0
			
			#initialize _mn_constants_atom_name_nucleic links
			#integer.Integer -> group_output_4.Side Chain Lower
			_mn_constants_atom_name_nucleic.links.new(integer.outputs[0], group_output_4.inputs[2])
			#integer_001.Integer -> group_output_4.Side Chain Upper
			_mn_constants_atom_name_nucleic.links.new(integer_001.outputs[0], group_output_4.inputs[3])
			#integer_002.Integer -> group_output_4.Backbone Lower
			_mn_constants_atom_name_nucleic.links.new(integer_002.outputs[0], group_output_4.inputs[0])
			#integer_003.Integer -> group_output_4.Backbone Upper
			_mn_constants_atom_name_nucleic.links.new(integer_003.outputs[0], group_output_4.inputs[1])
			#integer_004.Integer -> group_output_4.Side Chain Joint Carbon
			_mn_constants_atom_name_nucleic.links.new(integer_004.outputs[0], group_output_4.inputs[4])
			return _mn_constants_atom_name_nucleic

		_mn_constants_atom_name_nucleic = _mn_constants_atom_name_nucleic_node_group()

		#initialize fallback_boolean node group
		def fallback_boolean_node_group():
			fallback_boolean = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Fallback Boolean")

			fallback_boolean.color_tag = 'INPUT'
			fallback_boolean.description = "Computes the boolean field if the given attribute doesn't exist. If it doesn't exist it just uses the attribute instead"

			
			#fallback_boolean interface
			#Socket Boolean
			boolean_socket = fallback_boolean.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket.attribute_domain = 'POINT'
			
			#Socket Name
			name_socket = fallback_boolean.interface.new_socket(name = "Name", in_out='INPUT', socket_type = 'NodeSocketString')
			name_socket.attribute_domain = 'POINT'
			
			#Socket Fallback
			fallback_socket = fallback_boolean.interface.new_socket(name = "Fallback", in_out='INPUT', socket_type = 'NodeSocketBool')
			fallback_socket.attribute_domain = 'POINT'
			
			
			#initialize fallback_boolean nodes
			#node Group Output
			group_output_5 = fallback_boolean.nodes.new("NodeGroupOutput")
			group_output_5.name = "Group Output"
			group_output_5.is_active_output = True
			
			#node Group Input
			group_input_5 = fallback_boolean.nodes.new("NodeGroupInput")
			group_input_5.name = "Group Input"
			
			#node Named Attribute
			named_attribute_1 = fallback_boolean.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_1.name = "Named Attribute"
			named_attribute_1.data_type = 'BOOLEAN'
			
			#node Switch
			switch = fallback_boolean.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'BOOLEAN'
			
			
			
			
			#Set locations
			group_output_5.location = (276.6171569824219, 4.738137245178223)
			group_input_5.location = (-280.0, 0.0)
			named_attribute_1.location = (-94.73597717285156, 4.738137245178223)
			switch.location = (86.61715698242188, 4.738137245178223)
			
			#Set dimensions
			group_output_5.width, group_output_5.height = 140.0, 100.0
			group_input_5.width, group_input_5.height = 140.0, 100.0
			named_attribute_1.width, named_attribute_1.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			
			#initialize fallback_boolean links
			#named_attribute_1.Exists -> switch.Switch
			fallback_boolean.links.new(named_attribute_1.outputs[1], switch.inputs[0])
			#named_attribute_1.Attribute -> switch.True
			fallback_boolean.links.new(named_attribute_1.outputs[0], switch.inputs[2])
			#group_input_5.Fallback -> switch.False
			fallback_boolean.links.new(group_input_5.outputs[1], switch.inputs[1])
			#switch.Output -> group_output_5.Boolean
			fallback_boolean.links.new(switch.outputs[0], group_output_5.inputs[0])
			#group_input_5.Name -> named_attribute_1.Name
			fallback_boolean.links.new(group_input_5.outputs[0], named_attribute_1.inputs[0])
			return fallback_boolean

		fallback_boolean = fallback_boolean_node_group()

		#initialize _mn_constants_atom_name_peptide node group
		def _mn_constants_atom_name_peptide_node_group():
			_mn_constants_atom_name_peptide = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_constants_atom_name_peptide")

			_mn_constants_atom_name_peptide.color_tag = 'NONE'
			_mn_constants_atom_name_peptide.description = ""

			
			#_mn_constants_atom_name_peptide interface
			#Socket Backbone Lower
			backbone_lower_socket_1 = _mn_constants_atom_name_peptide.interface.new_socket(name = "Backbone Lower", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			backbone_lower_socket_1.subtype = 'NONE'
			backbone_lower_socket_1.default_value = 0
			backbone_lower_socket_1.min_value = -2147483648
			backbone_lower_socket_1.max_value = 2147483647
			backbone_lower_socket_1.attribute_domain = 'POINT'
			
			#Socket Backbone Upper
			backbone_upper_socket_1 = _mn_constants_atom_name_peptide.interface.new_socket(name = "Backbone Upper", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			backbone_upper_socket_1.subtype = 'NONE'
			backbone_upper_socket_1.default_value = 0
			backbone_upper_socket_1.min_value = -2147483648
			backbone_upper_socket_1.max_value = 2147483647
			backbone_upper_socket_1.attribute_domain = 'POINT'
			
			#Socket Side Chain Lower
			side_chain_lower_socket_1 = _mn_constants_atom_name_peptide.interface.new_socket(name = "Side Chain Lower", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			side_chain_lower_socket_1.subtype = 'NONE'
			side_chain_lower_socket_1.default_value = 0
			side_chain_lower_socket_1.min_value = -2147483648
			side_chain_lower_socket_1.max_value = 2147483647
			side_chain_lower_socket_1.attribute_domain = 'POINT'
			
			#Socket Side Chain Upper
			side_chain_upper_socket_1 = _mn_constants_atom_name_peptide.interface.new_socket(name = "Side Chain Upper", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			side_chain_upper_socket_1.subtype = 'NONE'
			side_chain_upper_socket_1.default_value = 0
			side_chain_upper_socket_1.min_value = -2147483648
			side_chain_upper_socket_1.max_value = 2147483647
			side_chain_upper_socket_1.attribute_domain = 'POINT'
			
			#Socket Alpha Carbon
			alpha_carbon_socket = _mn_constants_atom_name_peptide.interface.new_socket(name = "Alpha Carbon", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			alpha_carbon_socket.subtype = 'NONE'
			alpha_carbon_socket.default_value = 0
			alpha_carbon_socket.min_value = -2147483648
			alpha_carbon_socket.max_value = 2147483647
			alpha_carbon_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_constants_atom_name_peptide nodes
			#node Group Input
			group_input_6 = _mn_constants_atom_name_peptide.nodes.new("NodeGroupInput")
			group_input_6.name = "Group Input"
			
			#node Group Output
			group_output_6 = _mn_constants_atom_name_peptide.nodes.new("NodeGroupOutput")
			group_output_6.name = "Group Output"
			group_output_6.is_active_output = True
			
			#node Integer.001
			integer_001_1 = _mn_constants_atom_name_peptide.nodes.new("FunctionNodeInputInt")
			integer_001_1.name = "Integer.001"
			integer_001_1.integer = 49
			
			#node Integer.004
			integer_004_1 = _mn_constants_atom_name_peptide.nodes.new("FunctionNodeInputInt")
			integer_004_1.name = "Integer.004"
			integer_004_1.integer = 2
			
			#node Integer
			integer_1 = _mn_constants_atom_name_peptide.nodes.new("FunctionNodeInputInt")
			integer_1.name = "Integer"
			integer_1.integer = 5
			
			#node Integer.003
			integer_003_1 = _mn_constants_atom_name_peptide.nodes.new("FunctionNodeInputInt")
			integer_003_1.name = "Integer.003"
			integer_003_1.integer = 1
			
			#node Integer.002
			integer_002_1 = _mn_constants_atom_name_peptide.nodes.new("FunctionNodeInputInt")
			integer_002_1.name = "Integer.002"
			integer_002_1.integer = 4
			
			
			
			
			#Set locations
			group_input_6.location = (-200.0, 0.0)
			group_output_6.location = (260.0, 180.0)
			integer_001_1.location = (0.0, -50.0)
			integer_004_1.location = (0.0, -140.0)
			integer_1.location = (0.0, 40.0)
			integer_003_1.location = (0.0, 240.0)
			integer_002_1.location = (0.0, 140.0)
			
			#Set dimensions
			group_input_6.width, group_input_6.height = 140.0, 100.0
			group_output_6.width, group_output_6.height = 140.0, 100.0
			integer_001_1.width, integer_001_1.height = 140.0, 100.0
			integer_004_1.width, integer_004_1.height = 140.0, 100.0
			integer_1.width, integer_1.height = 140.0, 100.0
			integer_003_1.width, integer_003_1.height = 140.0, 100.0
			integer_002_1.width, integer_002_1.height = 140.0, 100.0
			
			#initialize _mn_constants_atom_name_peptide links
			#integer_003_1.Integer -> group_output_6.Backbone Lower
			_mn_constants_atom_name_peptide.links.new(integer_003_1.outputs[0], group_output_6.inputs[0])
			#integer_002_1.Integer -> group_output_6.Backbone Upper
			_mn_constants_atom_name_peptide.links.new(integer_002_1.outputs[0], group_output_6.inputs[1])
			#integer_1.Integer -> group_output_6.Side Chain Lower
			_mn_constants_atom_name_peptide.links.new(integer_1.outputs[0], group_output_6.inputs[2])
			#integer_001_1.Integer -> group_output_6.Side Chain Upper
			_mn_constants_atom_name_peptide.links.new(integer_001_1.outputs[0], group_output_6.inputs[3])
			#integer_004_1.Integer -> group_output_6.Alpha Carbon
			_mn_constants_atom_name_peptide.links.new(integer_004_1.outputs[0], group_output_6.inputs[4])
			return _mn_constants_atom_name_peptide

		_mn_constants_atom_name_peptide = _mn_constants_atom_name_peptide_node_group()

		#initialize _mn_select_peptide node group
		def _mn_select_peptide_node_group():
			_mn_select_peptide = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_select_peptide")

			_mn_select_peptide.color_tag = 'NONE'
			_mn_select_peptide.description = ""

			
			#_mn_select_peptide interface
			#Socket Is Backbone
			is_backbone_socket = _mn_select_peptide.interface.new_socket(name = "Is Backbone", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_backbone_socket.attribute_domain = 'POINT'
			
			#Socket Is Side Chain
			is_side_chain_socket = _mn_select_peptide.interface.new_socket(name = "Is Side Chain", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_side_chain_socket.attribute_domain = 'POINT'
			
			#Socket Is Peptide
			is_peptide_socket = _mn_select_peptide.interface.new_socket(name = "Is Peptide", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_peptide_socket.attribute_domain = 'POINT'
			
			#Socket Is Alpha Carbon
			is_alpha_carbon_socket = _mn_select_peptide.interface.new_socket(name = "Is Alpha Carbon", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_alpha_carbon_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_select_peptide nodes
			#node Group Input
			group_input_7 = _mn_select_peptide.nodes.new("NodeGroupInput")
			group_input_7.name = "Group Input"
			
			#node Compare
			compare_1 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
			compare_1.name = "Compare"
			compare_1.data_type = 'INT'
			compare_1.mode = 'ELEMENT'
			compare_1.operation = 'GREATER_EQUAL'
			
			#node Compare.001
			compare_001_1 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
			compare_001_1.name = "Compare.001"
			compare_001_1.data_type = 'INT'
			compare_001_1.mode = 'ELEMENT'
			compare_001_1.operation = 'LESS_EQUAL'
			
			#node Boolean Math.001
			boolean_math_001 = _mn_select_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001.name = "Boolean Math.001"
			boolean_math_001.operation = 'AND'
			
			#node Compare.002
			compare_002 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
			compare_002.name = "Compare.002"
			compare_002.data_type = 'INT'
			compare_002.mode = 'ELEMENT'
			compare_002.operation = 'GREATER_EQUAL'
			
			#node Compare.003
			compare_003 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
			compare_003.name = "Compare.003"
			compare_003.data_type = 'INT'
			compare_003.mode = 'ELEMENT'
			compare_003.operation = 'LESS_EQUAL'
			
			#node Boolean Math.002
			boolean_math_002 = _mn_select_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002.name = "Boolean Math.002"
			boolean_math_002.operation = 'AND'
			
			#node Compare.004
			compare_004 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
			compare_004.name = "Compare.004"
			compare_004.data_type = 'INT'
			compare_004.mode = 'ELEMENT'
			compare_004.operation = 'GREATER_EQUAL'
			
			#node Named Attribute
			named_attribute_2 = _mn_select_peptide.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_2.name = "Named Attribute"
			named_attribute_2.data_type = 'INT'
			#Name
			named_attribute_2.inputs[0].default_value = "atom_name"
			
			#node Boolean Math.003
			boolean_math_003 = _mn_select_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003.name = "Boolean Math.003"
			boolean_math_003.operation = 'AND'
			
			#node Group Output
			group_output_7 = _mn_select_peptide.nodes.new("NodeGroupOutput")
			group_output_7.name = "Group Output"
			group_output_7.is_active_output = True
			
			#node Compare.005
			compare_005 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
			compare_005.name = "Compare.005"
			compare_005.data_type = 'INT'
			compare_005.mode = 'ELEMENT'
			compare_005.operation = 'LESS_EQUAL'
			
			#node Compare.006
			compare_006 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
			compare_006.name = "Compare.006"
			compare_006.data_type = 'INT'
			compare_006.mode = 'ELEMENT'
			compare_006.operation = 'EQUAL'
			
			#node Group
			group = _mn_select_peptide.nodes.new("GeometryNodeGroup")
			group.name = "Group"
			group.node_tree = _mn_constants_atom_name_peptide
			
			#node Boolean Math
			boolean_math_1 = _mn_select_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math_1.name = "Boolean Math"
			boolean_math_1.operation = 'OR'
			
			
			
			
			#Set locations
			group_input_7.location = (-460.0, 0.0)
			compare_1.location = (80.0, 80.0)
			compare_001_1.location = (80.0, -80.0)
			boolean_math_001.location = (260.0, 80.0)
			compare_002.location = (80.0, -240.0)
			compare_003.location = (80.0, -400.0)
			boolean_math_002.location = (260.0, -240.0)
			compare_004.location = (80.0, -560.0)
			named_attribute_2.location = (-360.0, -480.0)
			boolean_math_003.location = (260.0, -560.0)
			group_output_7.location = (666.1161499023438, -263.7054748535156)
			compare_005.location = (80.0, -720.0)
			compare_006.location = (260.0, -380.0)
			group.location = (-411.24090576171875, -312.71807861328125)
			boolean_math_1.location = (420.0, -240.0)
			
			#Set dimensions
			group_input_7.width, group_input_7.height = 140.0, 100.0
			compare_1.width, compare_1.height = 140.0, 100.0
			compare_001_1.width, compare_001_1.height = 140.0, 100.0
			boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
			compare_002.width, compare_002.height = 153.86517333984375, 100.0
			compare_003.width, compare_003.height = 153.86517333984375, 100.0
			boolean_math_002.width, boolean_math_002.height = 140.0, 100.0
			compare_004.width, compare_004.height = 140.0, 100.0
			named_attribute_2.width, named_attribute_2.height = 140.0, 100.0
			boolean_math_003.width, boolean_math_003.height = 140.0, 100.0
			group_output_7.width, group_output_7.height = 140.0, 100.0
			compare_005.width, compare_005.height = 140.0, 100.0
			compare_006.width, compare_006.height = 140.0, 100.0
			group.width, group.height = 369.1165771484375, 100.0
			boolean_math_1.width, boolean_math_1.height = 140.0, 100.0
			
			#initialize _mn_select_peptide links
			#compare_001_1.Result -> boolean_math_001.Boolean
			_mn_select_peptide.links.new(compare_001_1.outputs[0], boolean_math_001.inputs[1])
			#group.Backbone Lower -> compare_1.B
			_mn_select_peptide.links.new(group.outputs[0], compare_1.inputs[3])
			#named_attribute_2.Attribute -> compare_1.A
			_mn_select_peptide.links.new(named_attribute_2.outputs[0], compare_1.inputs[2])
			#compare_1.Result -> boolean_math_001.Boolean
			_mn_select_peptide.links.new(compare_1.outputs[0], boolean_math_001.inputs[0])
			#named_attribute_2.Attribute -> compare_001_1.A
			_mn_select_peptide.links.new(named_attribute_2.outputs[0], compare_001_1.inputs[2])
			#group.Backbone Upper -> compare_001_1.B
			_mn_select_peptide.links.new(group.outputs[1], compare_001_1.inputs[3])
			#boolean_math_001.Boolean -> group_output_7.Is Backbone
			_mn_select_peptide.links.new(boolean_math_001.outputs[0], group_output_7.inputs[0])
			#compare_003.Result -> boolean_math_002.Boolean
			_mn_select_peptide.links.new(compare_003.outputs[0], boolean_math_002.inputs[1])
			#named_attribute_2.Attribute -> compare_002.A
			_mn_select_peptide.links.new(named_attribute_2.outputs[0], compare_002.inputs[2])
			#compare_002.Result -> boolean_math_002.Boolean
			_mn_select_peptide.links.new(compare_002.outputs[0], boolean_math_002.inputs[0])
			#named_attribute_2.Attribute -> compare_003.A
			_mn_select_peptide.links.new(named_attribute_2.outputs[0], compare_003.inputs[2])
			#group.Side Chain Lower -> compare_002.B
			_mn_select_peptide.links.new(group.outputs[2], compare_002.inputs[3])
			#group.Side Chain Upper -> compare_003.B
			_mn_select_peptide.links.new(group.outputs[3], compare_003.inputs[3])
			#compare_005.Result -> boolean_math_003.Boolean
			_mn_select_peptide.links.new(compare_005.outputs[0], boolean_math_003.inputs[1])
			#named_attribute_2.Attribute -> compare_004.A
			_mn_select_peptide.links.new(named_attribute_2.outputs[0], compare_004.inputs[2])
			#compare_004.Result -> boolean_math_003.Boolean
			_mn_select_peptide.links.new(compare_004.outputs[0], boolean_math_003.inputs[0])
			#named_attribute_2.Attribute -> compare_005.A
			_mn_select_peptide.links.new(named_attribute_2.outputs[0], compare_005.inputs[2])
			#group.Backbone Lower -> compare_004.B
			_mn_select_peptide.links.new(group.outputs[0], compare_004.inputs[3])
			#group.Side Chain Upper -> compare_005.B
			_mn_select_peptide.links.new(group.outputs[3], compare_005.inputs[3])
			#boolean_math_003.Boolean -> group_output_7.Is Peptide
			_mn_select_peptide.links.new(boolean_math_003.outputs[0], group_output_7.inputs[2])
			#named_attribute_2.Attribute -> compare_006.A
			_mn_select_peptide.links.new(named_attribute_2.outputs[0], compare_006.inputs[2])
			#group.Alpha Carbon -> compare_006.B
			_mn_select_peptide.links.new(group.outputs[4], compare_006.inputs[3])
			#compare_006.Result -> group_output_7.Is Alpha Carbon
			_mn_select_peptide.links.new(compare_006.outputs[0], group_output_7.inputs[3])
			#boolean_math_002.Boolean -> boolean_math_1.Boolean
			_mn_select_peptide.links.new(boolean_math_002.outputs[0], boolean_math_1.inputs[0])
			#compare_006.Result -> boolean_math_1.Boolean
			_mn_select_peptide.links.new(compare_006.outputs[0], boolean_math_1.inputs[1])
			#boolean_math_1.Boolean -> group_output_7.Is Side Chain
			_mn_select_peptide.links.new(boolean_math_1.outputs[0], group_output_7.inputs[1])
			return _mn_select_peptide

		_mn_select_peptide = _mn_select_peptide_node_group()

		#initialize is_alpha_carbon node group
		def is_alpha_carbon_node_group():
			is_alpha_carbon = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Is Alpha Carbon")

			is_alpha_carbon.color_tag = 'INPUT'
			is_alpha_carbon.description = ""

			
			#is_alpha_carbon interface
			#Socket Selection
			selection_socket = is_alpha_carbon.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket.attribute_domain = 'POINT'
			selection_socket.description = "True if atom is an alpha carbon of an amino acid"
			
			#Socket Inverted
			inverted_socket = is_alpha_carbon.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket.attribute_domain = 'POINT'
			
			#Socket And
			and_socket = is_alpha_carbon.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket.attribute_domain = 'POINT'
			and_socket.hide_value = True
			
			#Socket Or
			or_socket = is_alpha_carbon.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket.attribute_domain = 'POINT'
			or_socket.hide_value = True
			
			
			#initialize is_alpha_carbon nodes
			#node Group Output
			group_output_8 = is_alpha_carbon.nodes.new("NodeGroupOutput")
			group_output_8.name = "Group Output"
			group_output_8.is_active_output = True
			
			#node Group Input
			group_input_8 = is_alpha_carbon.nodes.new("NodeGroupInput")
			group_input_8.name = "Group Input"
			
			#node Boolean Math.001
			boolean_math_001_1 = is_alpha_carbon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_1.name = "Boolean Math.001"
			boolean_math_001_1.operation = 'AND'
			
			#node Group.001
			group_001 = is_alpha_carbon.nodes.new("GeometryNodeGroup")
			group_001.name = "Group.001"
			group_001.node_tree = fallback_boolean
			#Socket_2
			group_001.inputs[0].default_value = "is_alpha_carbon"
			
			#node Group.002
			group_002 = is_alpha_carbon.nodes.new("GeometryNodeGroup")
			group_002.name = "Group.002"
			group_002.node_tree = _mn_select_peptide
			group_002.outputs[0].hide = True
			group_002.outputs[1].hide = True
			group_002.outputs[2].hide = True
			
			#node Boolean Math.002
			boolean_math_002_1 = is_alpha_carbon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_1.name = "Boolean Math.002"
			boolean_math_002_1.operation = 'OR'
			
			#node Boolean Math
			boolean_math_2 = is_alpha_carbon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_2.name = "Boolean Math"
			boolean_math_2.operation = 'NOT'
			
			
			
			
			#Set locations
			group_output_8.location = (520.0, 0.0)
			group_input_8.location = (-200.0, 0.0)
			boolean_math_001_1.location = (160.0, 0.0)
			group_001.location = (-88.33343505859375, -180.0)
			group_002.location = (-290.4490661621094, -180.0)
			boolean_math_002_1.location = (340.0, 0.0)
			boolean_math_2.location = (340.0, -140.0)
			
			#Set dimensions
			group_output_8.width, group_output_8.height = 140.0, 100.0
			group_input_8.width, group_input_8.height = 140.0, 100.0
			boolean_math_001_1.width, boolean_math_001_1.height = 140.0, 100.0
			group_001.width, group_001.height = 208.33343505859375, 100.0
			group_002.width, group_002.height = 170.44906616210938, 100.0
			boolean_math_002_1.width, boolean_math_002_1.height = 140.0, 100.0
			boolean_math_2.width, boolean_math_2.height = 140.0, 100.0
			
			#initialize is_alpha_carbon links
			#group_input_8.And -> boolean_math_001_1.Boolean
			is_alpha_carbon.links.new(group_input_8.outputs[0], boolean_math_001_1.inputs[0])
			#boolean_math_002_1.Boolean -> group_output_8.Selection
			is_alpha_carbon.links.new(boolean_math_002_1.outputs[0], group_output_8.inputs[0])
			#group_001.Boolean -> boolean_math_001_1.Boolean
			is_alpha_carbon.links.new(group_001.outputs[0], boolean_math_001_1.inputs[1])
			#group_002.Is Alpha Carbon -> group_001.Fallback
			is_alpha_carbon.links.new(group_002.outputs[3], group_001.inputs[1])
			#boolean_math_001_1.Boolean -> boolean_math_002_1.Boolean
			is_alpha_carbon.links.new(boolean_math_001_1.outputs[0], boolean_math_002_1.inputs[0])
			#group_input_8.Or -> boolean_math_002_1.Boolean
			is_alpha_carbon.links.new(group_input_8.outputs[1], boolean_math_002_1.inputs[1])
			#boolean_math_002_1.Boolean -> boolean_math_2.Boolean
			is_alpha_carbon.links.new(boolean_math_002_1.outputs[0], boolean_math_2.inputs[0])
			#boolean_math_2.Boolean -> group_output_8.Inverted
			is_alpha_carbon.links.new(boolean_math_2.outputs[0], group_output_8.inputs[1])
			return is_alpha_carbon

		is_alpha_carbon = is_alpha_carbon_node_group()

		#initialize _mn_utils_style_surface_new node group
		def _mn_utils_style_surface_new_node_group():
			_mn_utils_style_surface_new = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_utils_style_surface_new")

			_mn_utils_style_surface_new.color_tag = 'GEOMETRY'
			_mn_utils_style_surface_new.description = ""

			_mn_utils_style_surface_new.is_modifier = True
			
			#_mn_utils_style_surface_new interface
			#Socket Surface Geometry
			surface_geometry_socket = _mn_utils_style_surface_new.interface.new_socket(name = "Surface Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			surface_geometry_socket.attribute_domain = 'POINT'
			
			#Socket Volume
			volume_socket = _mn_utils_style_surface_new.interface.new_socket(name = "Volume", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			volume_socket.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket_1 = _mn_utils_style_surface_new.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_1.attribute_domain = 'POINT'
			atoms_socket_1.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket_1 = _mn_utils_style_surface_new.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_1.attribute_domain = 'POINT'
			selection_socket_1.hide_value = True
			selection_socket_1.description = "Selection of atoms to apply this node to"
			
			#Socket Quality
			quality_socket = _mn_utils_style_surface_new.interface.new_socket(name = "Quality", in_out='INPUT', socket_type = 'NodeSocketInt')
			quality_socket.subtype = 'NONE'
			quality_socket.default_value = 12
			quality_socket.min_value = 1
			quality_socket.max_value = 15
			quality_socket.attribute_domain = 'POINT'
			
			#Socket Scale Radii
			scale_radii_socket = _mn_utils_style_surface_new.interface.new_socket(name = "Scale Radii", in_out='INPUT', socket_type = 'NodeSocketFloat')
			scale_radii_socket.subtype = 'NONE'
			scale_radii_socket.default_value = 1.0
			scale_radii_socket.min_value = 0.0
			scale_radii_socket.max_value = 10.0
			scale_radii_socket.attribute_domain = 'POINT'
			
			#Socket Probe Size
			probe_size_socket_1 = _mn_utils_style_surface_new.interface.new_socket(name = "Probe Size", in_out='INPUT', socket_type = 'NodeSocketFloat')
			probe_size_socket_1.subtype = 'NONE'
			probe_size_socket_1.default_value = 0.6000000238418579
			probe_size_socket_1.min_value = 0.0
			probe_size_socket_1.max_value = 10000.0
			probe_size_socket_1.attribute_domain = 'POINT'
			
			#Socket Color by CA
			color_by_ca_socket = _mn_utils_style_surface_new.interface.new_socket(name = "Color by CA", in_out='INPUT', socket_type = 'NodeSocketBool')
			color_by_ca_socket.attribute_domain = 'POINT'
			
			#Socket Color Blur
			color_blur_socket = _mn_utils_style_surface_new.interface.new_socket(name = "Color Blur", in_out='INPUT', socket_type = 'NodeSocketInt')
			color_blur_socket.subtype = 'NONE'
			color_blur_socket.default_value = 1
			color_blur_socket.min_value = 0
			color_blur_socket.max_value = 20
			color_blur_socket.attribute_domain = 'POINT'
			
			#Socket Shade Smooth
			shade_smooth_socket = _mn_utils_style_surface_new.interface.new_socket(name = "Shade Smooth", in_out='INPUT', socket_type = 'NodeSocketBool')
			shade_smooth_socket.attribute_domain = 'POINT'
			shade_smooth_socket.description = "Apply smooth shading to the created geometry"
			
			#Socket Triangulate
			triangulate_socket = _mn_utils_style_surface_new.interface.new_socket(name = "Triangulate", in_out='INPUT', socket_type = 'NodeSocketBool')
			triangulate_socket.attribute_domain = 'POINT'
			triangulate_socket.hide_value = True
			
			#Socket Material
			material_socket = _mn_utils_style_surface_new.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial')
			material_socket.attribute_domain = 'POINT'
			material_socket.description = "Material to apply to the resulting geometry"
			
			#Socket Relaxation Steps
			relaxation_steps_socket = _mn_utils_style_surface_new.interface.new_socket(name = "Relaxation Steps", in_out='INPUT', socket_type = 'NodeSocketInt')
			relaxation_steps_socket.subtype = 'NONE'
			relaxation_steps_socket.default_value = 30
			relaxation_steps_socket.min_value = 0
			relaxation_steps_socket.max_value = 2147483647
			relaxation_steps_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_utils_style_surface_new nodes
			#node Frame.002
			frame_002 = _mn_utils_style_surface_new.nodes.new("NodeFrame")
			frame_002.label = "Generate Surface from Measurements"
			frame_002.name = "Frame.002"
			frame_002.label_size = 20
			frame_002.shrink = True
			
			#node Frame
			frame_1 = _mn_utils_style_surface_new.nodes.new("NodeFrame")
			frame_1.label = "Pull in surface towards atoms"
			frame_1.name = "Frame"
			frame_1.label_size = 20
			frame_1.shrink = True
			
			#node Frame.001
			frame_001 = _mn_utils_style_surface_new.nodes.new("NodeFrame")
			frame_001.label = "smoothing of tightened surface"
			frame_001.name = "Frame.001"
			frame_001.label_size = 20
			frame_001.shrink = True
			
			#node Frame.003
			frame_003 = _mn_utils_style_surface_new.nodes.new("NodeFrame")
			frame_003.label = "Sample colors of nearest atom"
			frame_003.name = "Frame.003"
			frame_003.label_size = 20
			frame_003.shrink = True
			
			#node Reroute.009
			reroute_009 = _mn_utils_style_surface_new.nodes.new("NodeReroute")
			reroute_009.name = "Reroute.009"
			#node Reroute.004
			reroute_004 = _mn_utils_style_surface_new.nodes.new("NodeReroute")
			reroute_004.name = "Reroute.004"
			#node Reroute
			reroute_2 = _mn_utils_style_surface_new.nodes.new("NodeReroute")
			reroute_2.name = "Reroute"
			#node Math.001
			math_001_2 = _mn_utils_style_surface_new.nodes.new("ShaderNodeMath")
			math_001_2.label = "x * 10"
			math_001_2.name = "Math.001"
			math_001_2.operation = 'MULTIPLY'
			math_001_2.use_clamp = False
			#Value_001
			math_001_2.inputs[1].default_value = 50.0
			
			#node Reroute.001
			reroute_001_3 = _mn_utils_style_surface_new.nodes.new("NodeReroute")
			reroute_001_3.name = "Reroute.001"
			#node Group Input
			group_input_9 = _mn_utils_style_surface_new.nodes.new("NodeGroupInput")
			group_input_9.name = "Group Input"
			group_input_9.outputs[8].hide = True
			group_input_9.outputs[10].hide = True
			
			#node Separate Geometry
			separate_geometry = _mn_utils_style_surface_new.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry.name = "Separate Geometry"
			separate_geometry.domain = 'POINT'
			
			#node Volume Cube
			volume_cube = _mn_utils_style_surface_new.nodes.new("GeometryNodeVolumeCube")
			volume_cube.name = "Volume Cube"
			#Background
			volume_cube.inputs[1].default_value = 0.0
			
			#node Reroute.003
			reroute_003_1 = _mn_utils_style_surface_new.nodes.new("NodeReroute")
			reroute_003_1.name = "Reroute.003"
			#node Volume to Mesh
			volume_to_mesh = _mn_utils_style_surface_new.nodes.new("GeometryNodeVolumeToMesh")
			volume_to_mesh.name = "Volume to Mesh"
			volume_to_mesh.resolution_mode = 'GRID'
			#Threshold
			volume_to_mesh.inputs[3].default_value = 0.10000000149011612
			#Adaptivity
			volume_to_mesh.inputs[4].default_value = 0.0
			
			#node Reroute.002
			reroute_002_2 = _mn_utils_style_surface_new.nodes.new("NodeReroute")
			reroute_002_2.name = "Reroute.002"
			#node Group Output
			group_output_9 = _mn_utils_style_surface_new.nodes.new("NodeGroupOutput")
			group_output_9.name = "Group Output"
			group_output_9.is_active_output = True
			
			#node Set Shade Smooth.001
			set_shade_smooth_001 = _mn_utils_style_surface_new.nodes.new("GeometryNodeSetShadeSmooth")
			set_shade_smooth_001.name = "Set Shade Smooth.001"
			set_shade_smooth_001.domain = 'FACE'
			#Selection
			set_shade_smooth_001.inputs[1].default_value = True
			
			#node Set Material
			set_material = _mn_utils_style_surface_new.nodes.new("GeometryNodeSetMaterial")
			set_material.name = "Set Material"
			#Selection
			set_material.inputs[1].default_value = True
			
			#node Group Input.005
			group_input_005 = _mn_utils_style_surface_new.nodes.new("NodeGroupInput")
			group_input_005.name = "Group Input.005"
			group_input_005.outputs[0].hide = True
			group_input_005.outputs[1].hide = True
			group_input_005.outputs[2].hide = True
			group_input_005.outputs[3].hide = True
			group_input_005.outputs[4].hide = True
			group_input_005.outputs[6].hide = True
			group_input_005.outputs[7].hide = True
			group_input_005.outputs[8].hide = True
			group_input_005.outputs[9].hide = True
			group_input_005.outputs[10].hide = True
			group_input_005.outputs[11].hide = True
			
			#node Separate Geometry.001
			separate_geometry_001 = _mn_utils_style_surface_new.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_001.name = "Separate Geometry.001"
			separate_geometry_001.domain = 'POINT'
			
			#node Switch
			switch_1 = _mn_utils_style_surface_new.nodes.new("GeometryNodeSwitch")
			switch_1.name = "Switch"
			switch_1.input_type = 'GEOMETRY'
			
			#node Reroute.008
			reroute_008 = _mn_utils_style_surface_new.nodes.new("NodeReroute")
			reroute_008.name = "Reroute.008"
			#node Reroute.011
			reroute_011 = _mn_utils_style_surface_new.nodes.new("NodeReroute")
			reroute_011.name = "Reroute.011"
			#node Boolean Math
			boolean_math_3 = _mn_utils_style_surface_new.nodes.new("FunctionNodeBooleanMath")
			boolean_math_3.name = "Boolean Math"
			boolean_math_3.operation = 'OR'
			
			#node Capture Attribute
			capture_attribute = _mn_utils_style_surface_new.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute.name = "Capture Attribute"
			capture_attribute.active_index = 0
			capture_attribute.capture_items.clear()
			capture_attribute.capture_items.new('FLOAT', "Value")
			capture_attribute.capture_items["Value"].data_type = 'INT'
			capture_attribute.domain = 'POINT'
			
			#node Vector Math.001
			vector_math_001_1 = _mn_utils_style_surface_new.nodes.new("ShaderNodeVectorMath")
			vector_math_001_1.name = "Vector Math.001"
			vector_math_001_1.operation = 'ADD'
			
			#node Sample Index
			sample_index_1 = _mn_utils_style_surface_new.nodes.new("GeometryNodeSampleIndex")
			sample_index_1.name = "Sample Index"
			sample_index_1.clamp = False
			sample_index_1.data_type = 'FLOAT_VECTOR'
			sample_index_1.domain = 'POINT'
			
			#node Position
			position_1 = _mn_utils_style_surface_new.nodes.new("GeometryNodeInputPosition")
			position_1.name = "Position"
			
			#node Vector Math
			vector_math_2 = _mn_utils_style_surface_new.nodes.new("ShaderNodeVectorMath")
			vector_math_2.name = "Vector Math"
			vector_math_2.operation = 'SUBTRACT'
			
			#node Vector Math.002
			vector_math_002_1 = _mn_utils_style_surface_new.nodes.new("ShaderNodeVectorMath")
			vector_math_002_1.name = "Vector Math.002"
			vector_math_002_1.operation = 'NORMALIZE'
			
			#node Vector Math.003
			vector_math_003_1 = _mn_utils_style_surface_new.nodes.new("ShaderNodeVectorMath")
			vector_math_003_1.name = "Vector Math.003"
			vector_math_003_1.operation = 'SCALE'
			
			#node Sample Index.002
			sample_index_002_1 = _mn_utils_style_surface_new.nodes.new("GeometryNodeSampleIndex")
			sample_index_002_1.name = "Sample Index.002"
			sample_index_002_1.clamp = False
			sample_index_002_1.data_type = 'FLOAT'
			sample_index_002_1.domain = 'POINT'
			
			#node Reroute.007
			reroute_007_1 = _mn_utils_style_surface_new.nodes.new("NodeReroute")
			reroute_007_1.name = "Reroute.007"
			#node Math.002
			math_002_1 = _mn_utils_style_surface_new.nodes.new("ShaderNodeMath")
			math_002_1.name = "Math.002"
			math_002_1.operation = 'MULTIPLY'
			math_002_1.use_clamp = False
			
			#node Group Input.003
			group_input_003 = _mn_utils_style_surface_new.nodes.new("NodeGroupInput")
			group_input_003.name = "Group Input.003"
			group_input_003.outputs[0].hide = True
			group_input_003.outputs[1].hide = True
			group_input_003.outputs[2].hide = True
			group_input_003.outputs[4].hide = True
			group_input_003.outputs[5].hide = True
			group_input_003.outputs[6].hide = True
			group_input_003.outputs[7].hide = True
			group_input_003.outputs[8].hide = True
			group_input_003.outputs[9].hide = True
			group_input_003.outputs[10].hide = True
			group_input_003.outputs[11].hide = True
			
			#node Named Attribute
			named_attribute_3 = _mn_utils_style_surface_new.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_3.name = "Named Attribute"
			named_attribute_3.data_type = 'FLOAT'
			#Name
			named_attribute_3.inputs[0].default_value = "vdw_radii"
			
			#node Reroute.006
			reroute_006 = _mn_utils_style_surface_new.nodes.new("NodeReroute")
			reroute_006.name = "Reroute.006"
			#node Set Position.002
			set_position_002 = _mn_utils_style_surface_new.nodes.new("GeometryNodeSetPosition")
			set_position_002.name = "Set Position.002"
			#Selection
			set_position_002.inputs[1].default_value = True
			#Offset
			set_position_002.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Sample Nearest
			sample_nearest_1 = _mn_utils_style_surface_new.nodes.new("GeometryNodeSampleNearest")
			sample_nearest_1.name = "Sample Nearest"
			sample_nearest_1.domain = 'POINT'
			#Sample Position
			sample_nearest_1.inputs[1].default_value = (0.0, 0.0, 0.0)
			
			#node Blur Attribute.001
			blur_attribute_001 = _mn_utils_style_surface_new.nodes.new("GeometryNodeBlurAttribute")
			blur_attribute_001.name = "Blur Attribute.001"
			blur_attribute_001.data_type = 'FLOAT_VECTOR'
			#Iterations
			blur_attribute_001.inputs[1].default_value = 2
			#Weight
			blur_attribute_001.inputs[2].default_value = 1.0
			
			#node Position.002
			position_002 = _mn_utils_style_surface_new.nodes.new("GeometryNodeInputPosition")
			position_002.name = "Position.002"
			
			#node Set Position.003
			set_position_003 = _mn_utils_style_surface_new.nodes.new("GeometryNodeSetPosition")
			set_position_003.name = "Set Position.003"
			#Selection
			set_position_003.inputs[1].default_value = True
			#Position
			set_position_003.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Set Position.004
			set_position_004 = _mn_utils_style_surface_new.nodes.new("GeometryNodeSetPosition")
			set_position_004.name = "Set Position.004"
			#Selection
			set_position_004.inputs[1].default_value = True
			#Offset
			set_position_004.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Vector Math.005
			vector_math_005_1 = _mn_utils_style_surface_new.nodes.new("ShaderNodeVectorMath")
			vector_math_005_1.name = "Vector Math.005"
			vector_math_005_1.operation = 'SCALE'
			
			#node Normal
			normal = _mn_utils_style_surface_new.nodes.new("GeometryNodeInputNormal")
			normal.name = "Normal"
			
			#node Math.003
			math_003_2 = _mn_utils_style_surface_new.nodes.new("ShaderNodeMath")
			math_003_2.name = "Math.003"
			math_003_2.operation = 'MULTIPLY'
			math_003_2.use_clamp = False
			#Value_001
			math_003_2.inputs[1].default_value = -1.7999999523162842
			
			#node Capture Attribute.001
			capture_attribute_001 = _mn_utils_style_surface_new.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute_001.name = "Capture Attribute.001"
			capture_attribute_001.active_index = 0
			capture_attribute_001.capture_items.clear()
			capture_attribute_001.capture_items.new('FLOAT', "Value")
			capture_attribute_001.capture_items["Value"].data_type = 'FLOAT_VECTOR'
			capture_attribute_001.domain = 'POINT'
			
			#node Set Position.001
			set_position_001_1 = _mn_utils_style_surface_new.nodes.new("GeometryNodeSetPosition")
			set_position_001_1.name = "Set Position.001"
			#Selection
			set_position_001_1.inputs[1].default_value = True
			#Offset
			set_position_001_1.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Position.001
			position_001_1 = _mn_utils_style_surface_new.nodes.new("GeometryNodeInputPosition")
			position_001_1.name = "Position.001"
			
			#node Vector Math.004
			vector_math_004_2 = _mn_utils_style_surface_new.nodes.new("ShaderNodeVectorMath")
			vector_math_004_2.name = "Vector Math.004"
			vector_math_004_2.operation = 'DISTANCE'
			
			#node Blur Attribute
			blur_attribute_1 = _mn_utils_style_surface_new.nodes.new("GeometryNodeBlurAttribute")
			blur_attribute_1.name = "Blur Attribute"
			blur_attribute_1.data_type = 'FLOAT_VECTOR'
			#Iterations
			blur_attribute_1.inputs[1].default_value = 2
			#Weight
			blur_attribute_1.inputs[2].default_value = 1.0
			
			#node Group.003
			group_003 = _mn_utils_style_surface_new.nodes.new("GeometryNodeGroup")
			group_003.name = "Group.003"
			group_003.node_tree = _mn_surface_smooth_bumps
			
			#node Position.003
			position_003 = _mn_utils_style_surface_new.nodes.new("GeometryNodeInputPosition")
			position_003.name = "Position.003"
			
			#node Blur Attribute.004
			blur_attribute_004 = _mn_utils_style_surface_new.nodes.new("GeometryNodeBlurAttribute")
			blur_attribute_004.name = "Blur Attribute.004"
			blur_attribute_004.data_type = 'FLOAT_VECTOR'
			
			#node Group.004
			group_004 = _mn_utils_style_surface_new.nodes.new("GeometryNodeGroup")
			group_004.name = "Group.004"
			group_004.node_tree = _utils_bounding_box
			
			#node Group.005
			group_005 = _mn_utils_style_surface_new.nodes.new("GeometryNodeGroup")
			group_005.name = "Group.005"
			group_005.node_tree = _surface_compute_density_from_points
			
			#node Reroute.005
			reroute_005 = _mn_utils_style_surface_new.nodes.new("NodeReroute")
			reroute_005.name = "Reroute.005"
			#node Blur Attribute.002
			blur_attribute_002 = _mn_utils_style_surface_new.nodes.new("GeometryNodeBlurAttribute")
			blur_attribute_002.name = "Blur Attribute.002"
			blur_attribute_002.data_type = 'FLOAT_COLOR'
			#Weight
			blur_attribute_002.inputs[2].default_value = 1.0
			
			#node Sample Index.003
			sample_index_003_1 = _mn_utils_style_surface_new.nodes.new("GeometryNodeSampleIndex")
			sample_index_003_1.name = "Sample Index.003"
			sample_index_003_1.clamp = False
			sample_index_003_1.data_type = 'FLOAT_COLOR'
			sample_index_003_1.domain = 'POINT'
			
			#node Sample Nearest.001
			sample_nearest_001 = _mn_utils_style_surface_new.nodes.new("GeometryNodeSampleNearest")
			sample_nearest_001.name = "Sample Nearest.001"
			sample_nearest_001.domain = 'POINT'
			#Sample Position
			sample_nearest_001.inputs[1].default_value = (0.0, 0.0, 0.0)
			
			#node Named Attribute.002
			named_attribute_002 = _mn_utils_style_surface_new.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002.name = "Named Attribute.002"
			named_attribute_002.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute_002.inputs[0].default_value = "Color"
			
			#node Group Input.004
			group_input_004 = _mn_utils_style_surface_new.nodes.new("NodeGroupInput")
			group_input_004.name = "Group Input.004"
			group_input_004.outputs[0].hide = True
			group_input_004.outputs[1].hide = True
			group_input_004.outputs[2].hide = True
			group_input_004.outputs[3].hide = True
			group_input_004.outputs[4].hide = True
			group_input_004.outputs[5].hide = True
			group_input_004.outputs[7].hide = True
			group_input_004.outputs[8].hide = True
			group_input_004.outputs[9].hide = True
			group_input_004.outputs[10].hide = True
			group_input_004.outputs[11].hide = True
			
			#node Store Named Attribute
			store_named_attribute = _mn_utils_style_surface_new.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute.name = "Store Named Attribute"
			store_named_attribute.data_type = 'FLOAT_COLOR'
			store_named_attribute.domain = 'POINT'
			#Selection
			store_named_attribute.inputs[1].default_value = True
			#Name
			store_named_attribute.inputs[2].default_value = "Color"
			
			#node Group Input.001
			group_input_001 = _mn_utils_style_surface_new.nodes.new("NodeGroupInput")
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
			group_input_001.outputs[10].hide = True
			group_input_001.outputs[11].hide = True
			
			#node Group Input.002
			group_input_002 = _mn_utils_style_surface_new.nodes.new("NodeGroupInput")
			group_input_002.name = "Group Input.002"
			group_input_002.outputs[0].hide = True
			group_input_002.outputs[1].hide = True
			group_input_002.outputs[2].hide = True
			group_input_002.outputs[3].hide = True
			group_input_002.outputs[4].hide = True
			group_input_002.outputs[5].hide = True
			group_input_002.outputs[6].hide = True
			group_input_002.outputs[8].hide = True
			group_input_002.outputs[9].hide = True
			group_input_002.outputs[10].hide = True
			group_input_002.outputs[11].hide = True
			
			#node Set Position.005
			set_position_005 = _mn_utils_style_surface_new.nodes.new("GeometryNodeSetPosition")
			set_position_005.name = "Set Position.005"
			#Selection
			set_position_005.inputs[1].default_value = True
			#Offset
			set_position_005.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Triangulate
			triangulate = _mn_utils_style_surface_new.nodes.new("GeometryNodeTriangulate")
			triangulate.name = "Triangulate"
			triangulate.ngon_method = 'BEAUTY'
			triangulate.quad_method = 'BEAUTY'
			#Minimum Vertices
			triangulate.inputs[2].default_value = 4
			
			#node Map Range
			map_range = _mn_utils_style_surface_new.nodes.new("ShaderNodeMapRange")
			map_range.name = "Map Range"
			map_range.clamp = True
			map_range.data_type = 'FLOAT'
			map_range.interpolation_type = 'LINEAR'
			#From Min
			map_range.inputs[1].default_value = -0.20000000298023224
			#From Max
			map_range.inputs[2].default_value = -1.0
			#To Min
			map_range.inputs[3].default_value = 0.0
			#To Max
			map_range.inputs[4].default_value = 1.0
			
			#node Evaluate on Domain
			evaluate_on_domain = _mn_utils_style_surface_new.nodes.new("GeometryNodeFieldOnDomain")
			evaluate_on_domain.name = "Evaluate on Domain"
			evaluate_on_domain.data_type = 'FLOAT'
			evaluate_on_domain.domain = 'FACE'
			
			#node Blur Attribute.003
			blur_attribute_003 = _mn_utils_style_surface_new.nodes.new("GeometryNodeBlurAttribute")
			blur_attribute_003.name = "Blur Attribute.003"
			blur_attribute_003.data_type = 'FLOAT'
			#Iterations
			blur_attribute_003.inputs[1].default_value = 2
			#Weight
			blur_attribute_003.inputs[2].default_value = 1.0
			
			#node Edge Angle
			edge_angle = _mn_utils_style_surface_new.nodes.new("GeometryNodeInputMeshEdgeAngle")
			edge_angle.name = "Edge Angle"
			
			#node Group Input.006
			group_input_006 = _mn_utils_style_surface_new.nodes.new("NodeGroupInput")
			group_input_006.name = "Group Input.006"
			group_input_006.outputs[0].hide = True
			group_input_006.outputs[1].hide = True
			group_input_006.outputs[2].hide = True
			group_input_006.outputs[3].hide = True
			group_input_006.outputs[4].hide = True
			group_input_006.outputs[5].hide = True
			group_input_006.outputs[6].hide = True
			group_input_006.outputs[7].hide = True
			group_input_006.outputs[9].hide = True
			group_input_006.outputs[10].hide = True
			group_input_006.outputs[11].hide = True
			
			#node Group Input.007
			group_input_007 = _mn_utils_style_surface_new.nodes.new("NodeGroupInput")
			group_input_007.label = "Relaxation Steps"
			group_input_007.name = "Group Input.007"
			group_input_007.outputs[0].hide = True
			group_input_007.outputs[1].hide = True
			group_input_007.outputs[2].hide = True
			group_input_007.outputs[3].hide = True
			group_input_007.outputs[4].hide = True
			group_input_007.outputs[5].hide = True
			group_input_007.outputs[6].hide = True
			group_input_007.outputs[7].hide = True
			group_input_007.outputs[8].hide = True
			group_input_007.outputs[9].hide = True
			group_input_007.outputs[11].hide = True
			
			#node Compare.001
			compare_001_2 = _mn_utils_style_surface_new.nodes.new("FunctionNodeCompare")
			compare_001_2.name = "Compare.001"
			compare_001_2.data_type = 'INT'
			compare_001_2.mode = 'ELEMENT'
			compare_001_2.operation = 'EQUAL'
			
			#node MN Select Alpha Carbon.001
			mn_select_alpha_carbon_001 = _mn_utils_style_surface_new.nodes.new("GeometryNodeGroup")
			mn_select_alpha_carbon_001.label = " Select Alpha Carbon"
			mn_select_alpha_carbon_001.name = "MN Select Alpha Carbon.001"
			mn_select_alpha_carbon_001.node_tree = _mn_constants_atom_name_nucleic
			
			#node MN Select Alpha Carbon
			mn_select_alpha_carbon = _mn_utils_style_surface_new.nodes.new("GeometryNodeGroup")
			mn_select_alpha_carbon.label = " Select Alpha Carbon"
			mn_select_alpha_carbon.name = "MN Select Alpha Carbon"
			mn_select_alpha_carbon.node_tree = is_alpha_carbon
			#Socket_1
			mn_select_alpha_carbon.inputs[0].default_value = True
			#Socket_3
			mn_select_alpha_carbon.inputs[1].default_value = False
			
			#node Named Attribute.003
			named_attribute_003 = _mn_utils_style_surface_new.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_003.name = "Named Attribute.003"
			named_attribute_003.data_type = 'INT'
			#Name
			named_attribute_003.inputs[0].default_value = "atom_name"
			
			
			
			#Set parents
			volume_cube.parent = frame_002
			reroute_003_1.parent = frame_002
			volume_to_mesh.parent = frame_002
			capture_attribute.parent = frame_1
			vector_math_001_1.parent = frame_1
			sample_index_1.parent = frame_1
			position_1.parent = frame_1
			vector_math_2.parent = frame_1
			vector_math_002_1.parent = frame_1
			vector_math_003_1.parent = frame_1
			sample_index_002_1.parent = frame_1
			reroute_007_1.parent = frame_1
			math_002_1.parent = frame_1
			group_input_003.parent = frame_1
			named_attribute_3.parent = frame_1
			reroute_006.parent = frame_1
			set_position_002.parent = frame_1
			sample_nearest_1.parent = frame_1
			blur_attribute_001.parent = frame_001
			position_002.parent = frame_001
			set_position_003.parent = frame_001
			set_position_004.parent = frame_001
			vector_math_005_1.parent = frame_001
			normal.parent = frame_001
			math_003_2.parent = frame_001
			capture_attribute_001.parent = frame_001
			set_position_001_1.parent = frame_001
			position_001_1.parent = frame_001
			vector_math_004_2.parent = frame_001
			blur_attribute_1.parent = frame_001
			group_003.parent = frame_001
			position_003.parent = frame_001
			blur_attribute_004.parent = frame_001
			reroute_005.parent = frame_003
			blur_attribute_002.parent = frame_003
			sample_index_003_1.parent = frame_003
			sample_nearest_001.parent = frame_003
			named_attribute_002.parent = frame_003
			group_input_004.parent = frame_003
			store_named_attribute.parent = frame_003
			set_position_005.parent = frame_001
			map_range.parent = frame_001
			evaluate_on_domain.parent = frame_001
			blur_attribute_003.parent = frame_001
			edge_angle.parent = frame_001
			group_input_007.parent = frame_001
			
			#Set locations
			frame_002.location = (218.288818359375, 125.22808837890625)
			frame_1.location = (-310.0, -12.0)
			frame_001.location = (-30.0, 100.0)
			frame_003.location = (519.0, -54.0)
			reroute_009.location = (4400.0, 440.0)
			reroute_004.location = (780.0, -1046.0635986328125)
			reroute_2.location = (1620.0, -1040.0)
			math_001_2.location = (627.5620727539062, 193.03146362304688)
			reroute_001_3.location = (547.5620727539062, 393.0314636230469)
			group_input_9.location = (-152.43792724609375, 333.0314636230469)
			separate_geometry.location = (127.56207275390625, 433.0314636230469)
			volume_cube.location = (890.0, 370.0)
			reroute_003_1.location = (1101.666748046875, 358.5393981933594)
			volume_to_mesh.location = (1216.4453125, 322.5808410644531)
			reroute_002_2.location = (1980.0, -1040.0)
			group_output_9.location = (7801.4853515625, 420.2796630859375)
			set_shade_smooth_001.location = (7280.0, 340.0)
			set_material.location = (7440.0, 340.0)
			group_input_005.location = (5340.0, -500.0)
			separate_geometry_001.location = (5500.0, -660.0)
			switch_1.location = (5500.0, -500.0)
			reroute_008.location = (5074.79296875, -1040.0)
			reroute_011.location = (5420.0, -680.0)
			boolean_math_3.location = (5660.0, -820.0)
			capture_attribute.location = (2621.3935546875, 352.30169677734375)
			vector_math_001_1.location = (3494.015869140625, -31.082717895507812)
			sample_index_1.location = (2820.0, 0.0)
			position_1.location = (2620.0, -60.0)
			vector_math_2.location = (2980.0, -40.0)
			vector_math_002_1.location = (3160.0, -40.0)
			vector_math_003_1.location = (3320.0, -40.0)
			sample_index_002_1.location = (2820.0, -220.0)
			reroute_007_1.location = (2580.0, -160.0)
			math_002_1.location = (2660.0, -220.0)
			group_input_003.location = (2480.0, -220.0)
			named_attribute_3.location = (2480.0, -280.0)
			reroute_006.location = (2780.0, -220.0)
			set_position_002.location = (3500.0, 180.0)
			sample_nearest_1.location = (2490.079345703125, 135.77288818359375)
			blur_attribute_001.location = (4620.0, -20.0)
			position_002.location = (4620.0, -180.0)
			set_position_003.location = (4400.0, 240.0)
			set_position_004.location = (4620.0, 240.0)
			vector_math_005_1.location = (4400.0, 80.0)
			normal.location = (4240.0, 80.0)
			math_003_2.location = (4400.0, -60.0)
			capture_attribute_001.location = (3880.0, 240.0)
			set_position_001_1.location = (4060.0, 240.0)
			position_001_1.location = (3660.0, 40.0)
			vector_math_004_2.location = (4060.0, 20.0)
			blur_attribute_1.location = (3880.0, 40.0)
			group_003.location = (5500.0, 240.0)
			position_003.location = (5030.0, -240.0)
			blur_attribute_004.location = (5190.0, -240.0)
			group_004.location = (627.5620727539062, 433.0314636230469)
			group_005.location = (627.5620727539062, 593.0314331054688)
			reroute_005.location = (5759.248046875, -86.10336303710938)
			blur_attribute_002.location = (6319.248046875, 113.89663696289062)
			sample_index_003_1.location = (6099.248046875, 133.89663696289062)
			sample_nearest_001.location = (5879.248046875, -46.103363037109375)
			named_attribute_002.location = (5879.248046875, 133.89663696289062)
			group_input_004.location = (6099.248046875, -86.10336303710938)
			store_named_attribute.location = (6319.248046875, 353.8966369628906)
			group_input_001.location = (7440.0, 200.0)
			group_input_002.location = (7280.0, 180.0)
			set_position_005.location = (5218.373046875, 251.50515747070312)
			triangulate.location = (6024.25439453125, 336.5474853515625)
			map_range.location = (4690.0, -420.0)
			evaluate_on_domain.location = (4870.0, -420.0)
			blur_attribute_003.location = (5030.0, -420.0)
			edge_angle.location = (4530.0, -420.0)
			group_input_006.location = (5820.0, 200.0)
			group_input_007.location = (5030.0, -320.0)
			compare_001_2.location = (5500.0, -980.0)
			mn_select_alpha_carbon_001.location = (5260.0, -940.0)
			mn_select_alpha_carbon.location = (5260.0, -860.0)
			named_attribute_003.location = (5320.0, -1120.0)
			
			#Set dimensions
			frame_002.width, frame_002.height = 556.4000244140625, 278.8000183105469
			frame_1.width, frame_1.height = 1220.0, 835.5999755859375
			frame_001.width, frame_001.height = 2171.52978515625, 979.6000366210938
			frame_003.width, frame_003.height = 766.5517578125, 590.7999877929688
			reroute_009.width, reroute_009.height = 16.0, 100.0
			reroute_004.width, reroute_004.height = 16.0, 100.0
			reroute_2.width, reroute_2.height = 16.0, 100.0
			math_001_2.width, math_001_2.height = 140.0, 100.0
			reroute_001_3.width, reroute_001_3.height = 16.0, 100.0
			group_input_9.width, group_input_9.height = 140.0, 100.0
			separate_geometry.width, separate_geometry.height = 140.0, 100.0
			volume_cube.width, volume_cube.height = 140.0, 100.0
			reroute_003_1.width, reroute_003_1.height = 16.0, 100.0
			volume_to_mesh.width, volume_to_mesh.height = 170.0, 100.0
			reroute_002_2.width, reroute_002_2.height = 16.0, 100.0
			group_output_9.width, group_output_9.height = 140.0, 100.0
			set_shade_smooth_001.width, set_shade_smooth_001.height = 140.0, 100.0
			set_material.width, set_material.height = 140.0, 100.0
			group_input_005.width, group_input_005.height = 140.0, 100.0
			separate_geometry_001.width, separate_geometry_001.height = 140.0, 100.0
			switch_1.width, switch_1.height = 140.0, 100.0
			reroute_008.width, reroute_008.height = 16.0, 100.0
			reroute_011.width, reroute_011.height = 16.0, 100.0
			boolean_math_3.width, boolean_math_3.height = 140.0, 100.0
			capture_attribute.width, capture_attribute.height = 140.0, 100.0
			vector_math_001_1.width, vector_math_001_1.height = 140.0, 100.0
			sample_index_1.width, sample_index_1.height = 140.0, 100.0
			position_1.width, position_1.height = 140.0, 100.0
			vector_math_2.width, vector_math_2.height = 140.0, 100.0
			vector_math_002_1.width, vector_math_002_1.height = 140.0, 100.0
			vector_math_003_1.width, vector_math_003_1.height = 140.0, 100.0
			sample_index_002_1.width, sample_index_002_1.height = 140.0, 100.0
			reroute_007_1.width, reroute_007_1.height = 16.0, 100.0
			math_002_1.width, math_002_1.height = 140.0, 100.0
			group_input_003.width, group_input_003.height = 154.36306762695312, 100.0
			named_attribute_3.width, named_attribute_3.height = 140.0, 100.0
			reroute_006.width, reroute_006.height = 16.0, 100.0
			set_position_002.width, set_position_002.height = 140.0, 100.0
			sample_nearest_1.width, sample_nearest_1.height = 140.0, 100.0
			blur_attribute_001.width, blur_attribute_001.height = 140.0, 100.0
			position_002.width, position_002.height = 140.0, 100.0
			set_position_003.width, set_position_003.height = 140.0, 100.0
			set_position_004.width, set_position_004.height = 140.0, 100.0
			vector_math_005_1.width, vector_math_005_1.height = 140.0, 100.0
			normal.width, normal.height = 140.0, 100.0
			math_003_2.width, math_003_2.height = 140.0, 100.0
			capture_attribute_001.width, capture_attribute_001.height = 140.0, 100.0
			set_position_001_1.width, set_position_001_1.height = 140.0, 100.0
			position_001_1.width, position_001_1.height = 140.0, 100.0
			vector_math_004_2.width, vector_math_004_2.height = 140.0, 100.0
			blur_attribute_1.width, blur_attribute_1.height = 140.0, 100.0
			group_003.width, group_003.height = 271.52978515625, 100.0
			position_003.width, position_003.height = 140.0, 100.0
			blur_attribute_004.width, blur_attribute_004.height = 140.0, 100.0
			group_004.width, group_004.height = 400.0, 100.0
			group_005.width, group_005.height = 400.0, 100.0
			reroute_005.width, reroute_005.height = 16.0, 100.0
			blur_attribute_002.width, blur_attribute_002.height = 140.0, 100.0
			sample_index_003_1.width, sample_index_003_1.height = 140.0, 100.0
			sample_nearest_001.width, sample_nearest_001.height = 140.0, 100.0
			named_attribute_002.width, named_attribute_002.height = 140.0, 100.0
			group_input_004.width, group_input_004.height = 140.0, 100.0
			store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
			group_input_001.width, group_input_001.height = 140.0, 100.0
			group_input_002.width, group_input_002.height = 140.0, 100.0
			set_position_005.width, set_position_005.height = 140.0, 100.0
			triangulate.width, triangulate.height = 140.0, 100.0
			map_range.width, map_range.height = 140.0, 100.0
			evaluate_on_domain.width, evaluate_on_domain.height = 140.0, 100.0
			blur_attribute_003.width, blur_attribute_003.height = 140.0, 100.0
			edge_angle.width, edge_angle.height = 140.0, 100.0
			group_input_006.width, group_input_006.height = 140.0, 100.0
			group_input_007.width, group_input_007.height = 140.0, 100.0
			compare_001_2.width, compare_001_2.height = 140.0, 100.0
			mn_select_alpha_carbon_001.width, mn_select_alpha_carbon_001.height = 200.0, 100.0
			mn_select_alpha_carbon.width, mn_select_alpha_carbon.height = 200.0, 100.0
			named_attribute_003.width, named_attribute_003.height = 140.0, 100.0
			
			#initialize _mn_utils_style_surface_new links
			#reroute_003_1.Output -> volume_to_mesh.Volume
			_mn_utils_style_surface_new.links.new(reroute_003_1.outputs[0], volume_to_mesh.inputs[0])
			#group_004.Min -> volume_cube.Min
			_mn_utils_style_surface_new.links.new(group_004.outputs[0], volume_cube.inputs[2])
			#group_004.Max -> volume_cube.Max
			_mn_utils_style_surface_new.links.new(group_004.outputs[1], volume_cube.inputs[3])
			#group_004.X -> volume_cube.Resolution X
			_mn_utils_style_surface_new.links.new(group_004.outputs[2], volume_cube.inputs[4])
			#group_004.Y -> volume_cube.Resolution Y
			_mn_utils_style_surface_new.links.new(group_004.outputs[3], volume_cube.inputs[5])
			#group_004.Z -> volume_cube.Resolution Z
			_mn_utils_style_surface_new.links.new(group_004.outputs[4], volume_cube.inputs[6])
			#separate_geometry.Selection -> reroute_004.Input
			_mn_utils_style_surface_new.links.new(separate_geometry.outputs[0], reroute_004.inputs[0])
			#set_material.Geometry -> group_output_9.Surface Geometry
			_mn_utils_style_surface_new.links.new(set_material.outputs[0], group_output_9.inputs[0])
			#reroute_009.Output -> group_output_9.Volume
			_mn_utils_style_surface_new.links.new(reroute_009.outputs[0], group_output_9.inputs[1])
			#math_001_2.Value -> group_004.Subdivisions
			_mn_utils_style_surface_new.links.new(math_001_2.outputs[0], group_004.inputs[1])
			#reroute_001_3.Output -> group_004.Geometry
			_mn_utils_style_surface_new.links.new(reroute_001_3.outputs[0], group_004.inputs[0])
			#reroute_001_3.Output -> group_005.Atoms
			_mn_utils_style_surface_new.links.new(reroute_001_3.outputs[0], group_005.inputs[0])
			#group_input_9.Scale Radii -> group_005.Scale Radius
			_mn_utils_style_surface_new.links.new(group_input_9.outputs[3], group_005.inputs[1])
			#group_input_9.Atoms -> separate_geometry.Geometry
			_mn_utils_style_surface_new.links.new(group_input_9.outputs[0], separate_geometry.inputs[0])
			#group_input_9.Selection -> separate_geometry.Selection
			_mn_utils_style_surface_new.links.new(group_input_9.outputs[1], separate_geometry.inputs[1])
			#separate_geometry.Selection -> reroute_001_3.Input
			_mn_utils_style_surface_new.links.new(separate_geometry.outputs[0], reroute_001_3.inputs[0])
			#group_input_9.Quality -> math_001_2.Value
			_mn_utils_style_surface_new.links.new(group_input_9.outputs[2], math_001_2.inputs[0])
			#group_input_9.Probe Size -> group_005.Probe Size
			_mn_utils_style_surface_new.links.new(group_input_9.outputs[4], group_005.inputs[2])
			#reroute_003_1.Output -> reroute_009.Input
			_mn_utils_style_surface_new.links.new(reroute_003_1.outputs[0], reroute_009.inputs[0])
			#group_005.Result -> volume_cube.Density
			_mn_utils_style_surface_new.links.new(group_005.outputs[0], volume_cube.inputs[0])
			#reroute_004.Output -> reroute_2.Input
			_mn_utils_style_surface_new.links.new(reroute_004.outputs[0], reroute_2.inputs[0])
			#reroute_007_1.Output -> sample_index_1.Geometry
			_mn_utils_style_surface_new.links.new(reroute_007_1.outputs[0], sample_index_1.inputs[0])
			#position_1.Position -> sample_index_1.Value
			_mn_utils_style_surface_new.links.new(position_1.outputs[0], sample_index_1.inputs[1])
			#group_input_001.Material -> set_material.Material
			_mn_utils_style_surface_new.links.new(group_input_001.outputs[9], set_material.inputs[2])
			#volume_to_mesh.Mesh -> capture_attribute.Geometry
			_mn_utils_style_surface_new.links.new(volume_to_mesh.outputs[0], capture_attribute.inputs[0])
			#sample_nearest_1.Index -> capture_attribute.Value
			_mn_utils_style_surface_new.links.new(sample_nearest_1.outputs[0], capture_attribute.inputs[1])
			#reroute_2.Output -> reroute_002_2.Input
			_mn_utils_style_surface_new.links.new(reroute_2.outputs[0], reroute_002_2.inputs[0])
			#reroute_006.Output -> sample_index_1.Index
			_mn_utils_style_surface_new.links.new(reroute_006.outputs[0], sample_index_1.inputs[2])
			#position_1.Position -> vector_math_2.Vector
			_mn_utils_style_surface_new.links.new(position_1.outputs[0], vector_math_2.inputs[0])
			#vector_math_2.Vector -> vector_math_002_1.Vector
			_mn_utils_style_surface_new.links.new(vector_math_2.outputs[0], vector_math_002_1.inputs[0])
			#reroute_007_1.Output -> sample_index_002_1.Geometry
			_mn_utils_style_surface_new.links.new(reroute_007_1.outputs[0], sample_index_002_1.inputs[0])
			#reroute_006.Output -> sample_index_002_1.Index
			_mn_utils_style_surface_new.links.new(reroute_006.outputs[0], sample_index_002_1.inputs[2])
			#vector_math_002_1.Vector -> vector_math_003_1.Vector
			_mn_utils_style_surface_new.links.new(vector_math_002_1.outputs[0], vector_math_003_1.inputs[0])
			#sample_index_002_1.Value -> vector_math_003_1.Scale
			_mn_utils_style_surface_new.links.new(sample_index_002_1.outputs[0], vector_math_003_1.inputs[3])
			#capture_attribute_001.Geometry -> set_position_001_1.Geometry
			_mn_utils_style_surface_new.links.new(capture_attribute_001.outputs[0], set_position_001_1.inputs[0])
			#group_input_003.Scale Radii -> math_002_1.Value
			_mn_utils_style_surface_new.links.new(group_input_003.outputs[3], math_002_1.inputs[0])
			#named_attribute_3.Attribute -> math_002_1.Value
			_mn_utils_style_surface_new.links.new(named_attribute_3.outputs[0], math_002_1.inputs[1])
			#math_002_1.Value -> sample_index_002_1.Value
			_mn_utils_style_surface_new.links.new(math_002_1.outputs[0], sample_index_002_1.inputs[1])
			#sample_index_1.Value -> vector_math_001_1.Vector
			_mn_utils_style_surface_new.links.new(sample_index_1.outputs[0], vector_math_001_1.inputs[0])
			#vector_math_003_1.Vector -> vector_math_001_1.Vector
			_mn_utils_style_surface_new.links.new(vector_math_003_1.outputs[0], vector_math_001_1.inputs[1])
			#set_shade_smooth_001.Geometry -> set_material.Geometry
			_mn_utils_style_surface_new.links.new(set_shade_smooth_001.outputs[0], set_material.inputs[0])
			#sample_index_1.Value -> vector_math_2.Vector
			_mn_utils_style_surface_new.links.new(sample_index_1.outputs[0], vector_math_2.inputs[1])
			#volume_cube.Volume -> reroute_003_1.Input
			_mn_utils_style_surface_new.links.new(volume_cube.outputs[0], reroute_003_1.inputs[0])
			#blur_attribute_1.Value -> set_position_001_1.Position
			_mn_utils_style_surface_new.links.new(blur_attribute_1.outputs[0], set_position_001_1.inputs[2])
			#capture_attribute.Geometry -> set_position_002.Geometry
			_mn_utils_style_surface_new.links.new(capture_attribute.outputs[0], set_position_002.inputs[0])
			#vector_math_001_1.Vector -> set_position_002.Position
			_mn_utils_style_surface_new.links.new(vector_math_001_1.outputs[0], set_position_002.inputs[2])
			#position_001_1.Position -> blur_attribute_1.Value
			_mn_utils_style_surface_new.links.new(position_001_1.outputs[0], blur_attribute_1.inputs[0])
			#set_position_002.Geometry -> capture_attribute_001.Geometry
			_mn_utils_style_surface_new.links.new(set_position_002.outputs[0], capture_attribute_001.inputs[0])
			#position_001_1.Position -> capture_attribute_001.Value
			_mn_utils_style_surface_new.links.new(position_001_1.outputs[0], capture_attribute_001.inputs[1])
			#capture_attribute_001.Value -> vector_math_004_2.Vector
			_mn_utils_style_surface_new.links.new(capture_attribute_001.outputs[1], vector_math_004_2.inputs[0])
			#position_001_1.Position -> vector_math_004_2.Vector
			_mn_utils_style_surface_new.links.new(position_001_1.outputs[0], vector_math_004_2.inputs[1])
			#set_position_001_1.Geometry -> set_position_003.Geometry
			_mn_utils_style_surface_new.links.new(set_position_001_1.outputs[0], set_position_003.inputs[0])
			#vector_math_005_1.Vector -> set_position_003.Offset
			_mn_utils_style_surface_new.links.new(vector_math_005_1.outputs[0], set_position_003.inputs[3])
			#normal.Normal -> vector_math_005_1.Vector
			_mn_utils_style_surface_new.links.new(normal.outputs[0], vector_math_005_1.inputs[0])
			#set_position_003.Geometry -> set_position_004.Geometry
			_mn_utils_style_surface_new.links.new(set_position_003.outputs[0], set_position_004.inputs[0])
			#position_002.Position -> blur_attribute_001.Value
			_mn_utils_style_surface_new.links.new(position_002.outputs[0], blur_attribute_001.inputs[0])
			#reroute_005.Output -> sample_index_003_1.Geometry
			_mn_utils_style_surface_new.links.new(reroute_005.outputs[0], sample_index_003_1.inputs[0])
			#named_attribute_002.Attribute -> sample_index_003_1.Value
			_mn_utils_style_surface_new.links.new(named_attribute_002.outputs[0], sample_index_003_1.inputs[1])
			#set_position_005.Geometry -> group_003.Geometry
			_mn_utils_style_surface_new.links.new(set_position_005.outputs[0], group_003.inputs[0])
			#sample_index_003_1.Value -> blur_attribute_002.Value
			_mn_utils_style_surface_new.links.new(sample_index_003_1.outputs[0], blur_attribute_002.inputs[0])
			#vector_math_004_2.Value -> math_003_2.Value
			_mn_utils_style_surface_new.links.new(vector_math_004_2.outputs[1], math_003_2.inputs[0])
			#math_003_2.Value -> vector_math_005_1.Scale
			_mn_utils_style_surface_new.links.new(math_003_2.outputs[0], vector_math_005_1.inputs[3])
			#edge_angle.Signed Angle -> map_range.Value
			_mn_utils_style_surface_new.links.new(edge_angle.outputs[1], map_range.inputs[0])
			#blur_attribute_003.Value -> blur_attribute_004.Weight
			_mn_utils_style_surface_new.links.new(blur_attribute_003.outputs[0], blur_attribute_004.inputs[2])
			#position_003.Position -> blur_attribute_004.Value
			_mn_utils_style_surface_new.links.new(position_003.outputs[0], blur_attribute_004.inputs[0])
			#blur_attribute_001.Value -> set_position_004.Position
			_mn_utils_style_surface_new.links.new(blur_attribute_001.outputs[0], set_position_004.inputs[2])
			#set_position_004.Geometry -> set_position_005.Geometry
			_mn_utils_style_surface_new.links.new(set_position_004.outputs[0], set_position_005.inputs[0])
			#blur_attribute_004.Value -> set_position_005.Position
			_mn_utils_style_surface_new.links.new(blur_attribute_004.outputs[0], set_position_005.inputs[2])
			#map_range.Result -> evaluate_on_domain.Value
			_mn_utils_style_surface_new.links.new(map_range.outputs[0], evaluate_on_domain.inputs[0])
			#reroute_005.Output -> sample_nearest_001.Geometry
			_mn_utils_style_surface_new.links.new(reroute_005.outputs[0], sample_nearest_001.inputs[0])
			#sample_nearest_001.Index -> sample_index_003_1.Index
			_mn_utils_style_surface_new.links.new(sample_nearest_001.outputs[0], sample_index_003_1.inputs[2])
			#switch_1.Output -> reroute_005.Input
			_mn_utils_style_surface_new.links.new(switch_1.outputs[0], reroute_005.inputs[0])
			#reroute_002_2.Output -> reroute_007_1.Input
			_mn_utils_style_surface_new.links.new(reroute_002_2.outputs[0], reroute_007_1.inputs[0])
			#capture_attribute.Value -> reroute_006.Input
			_mn_utils_style_surface_new.links.new(capture_attribute.outputs[1], reroute_006.inputs[0])
			#reroute_007_1.Output -> sample_nearest_1.Geometry
			_mn_utils_style_surface_new.links.new(reroute_007_1.outputs[0], sample_nearest_1.inputs[0])
			#triangulate.Mesh -> store_named_attribute.Geometry
			_mn_utils_style_surface_new.links.new(triangulate.outputs[0], store_named_attribute.inputs[0])
			#blur_attribute_002.Value -> store_named_attribute.Value
			_mn_utils_style_surface_new.links.new(blur_attribute_002.outputs[0], store_named_attribute.inputs[3])
			#reroute_002_2.Output -> reroute_008.Input
			_mn_utils_style_surface_new.links.new(reroute_002_2.outputs[0], reroute_008.inputs[0])
			#group_input_004.Color Blur -> blur_attribute_002.Iterations
			_mn_utils_style_surface_new.links.new(group_input_004.outputs[6], blur_attribute_002.inputs[1])
			#store_named_attribute.Geometry -> set_shade_smooth_001.Geometry
			_mn_utils_style_surface_new.links.new(store_named_attribute.outputs[0], set_shade_smooth_001.inputs[0])
			#group_input_002.Shade Smooth -> set_shade_smooth_001.Shade Smooth
			_mn_utils_style_surface_new.links.new(group_input_002.outputs[7], set_shade_smooth_001.inputs[2])
			#reroute_011.Output -> separate_geometry_001.Geometry
			_mn_utils_style_surface_new.links.new(reroute_011.outputs[0], separate_geometry_001.inputs[0])
			#separate_geometry_001.Selection -> switch_1.True
			_mn_utils_style_surface_new.links.new(separate_geometry_001.outputs[0], switch_1.inputs[2])
			#reroute_011.Output -> switch_1.False
			_mn_utils_style_surface_new.links.new(reroute_011.outputs[0], switch_1.inputs[1])
			#group_input_005.Color by CA -> switch_1.Switch
			_mn_utils_style_surface_new.links.new(group_input_005.outputs[5], switch_1.inputs[0])
			#compare_001_2.Result -> boolean_math_3.Boolean
			_mn_utils_style_surface_new.links.new(compare_001_2.outputs[0], boolean_math_3.inputs[1])
			#boolean_math_3.Boolean -> separate_geometry_001.Selection
			_mn_utils_style_surface_new.links.new(boolean_math_3.outputs[0], separate_geometry_001.inputs[1])
			#reroute_008.Output -> reroute_011.Input
			_mn_utils_style_surface_new.links.new(reroute_008.outputs[0], reroute_011.inputs[0])
			#evaluate_on_domain.Value -> blur_attribute_003.Value
			_mn_utils_style_surface_new.links.new(evaluate_on_domain.outputs[0], blur_attribute_003.inputs[0])
			#group_003.Geometry -> triangulate.Mesh
			_mn_utils_style_surface_new.links.new(group_003.outputs[0], triangulate.inputs[0])
			#group_input_006.Triangulate -> triangulate.Selection
			_mn_utils_style_surface_new.links.new(group_input_006.outputs[8], triangulate.inputs[1])
			#group_input_007.Relaxation Steps -> blur_attribute_004.Iterations
			_mn_utils_style_surface_new.links.new(group_input_007.outputs[10], blur_attribute_004.inputs[1])
			#mn_select_alpha_carbon.Selection -> boolean_math_3.Boolean
			_mn_utils_style_surface_new.links.new(mn_select_alpha_carbon.outputs[0], boolean_math_3.inputs[0])
			#named_attribute_003.Attribute -> compare_001_2.B
			_mn_utils_style_surface_new.links.new(named_attribute_003.outputs[0], compare_001_2.inputs[3])
			#mn_select_alpha_carbon_001.Side Chain Joint Carbon -> compare_001_2.A
			_mn_utils_style_surface_new.links.new(mn_select_alpha_carbon_001.outputs[4], compare_001_2.inputs[2])
			return _mn_utils_style_surface_new

		_mn_utils_style_surface_new = _mn_utils_style_surface_new_node_group()

		#initialize style_surface node group
		def style_surface_node_group():
			style_surface = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Style Surface")

			style_surface.color_tag = 'GEOMETRY'
			style_surface.description = ""

			
			#style_surface interface
			#Socket Geometry
			geometry_socket_4 = style_surface.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_4.attribute_domain = 'POINT'
			geometry_socket_4.description = "The resulting geometry of the style. All chains are a single mesh."
			
			#Socket Instances
			instances_socket = style_surface.interface.new_socket(name = "Instances", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			instances_socket.attribute_domain = 'POINT'
			instances_socket.description = "The resulting geometry of the style. Each chain is a separate instance."
			
			#Socket Atoms
			atoms_socket_2 = style_surface.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_2.attribute_domain = 'POINT'
			atoms_socket_2.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket_2 = style_surface.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_2.attribute_domain = 'POINT'
			selection_socket_2.hide_value = True
			selection_socket_2.description = "Selection of atoms to apply this style to"
			
			#Socket Quality
			quality_socket_1 = style_surface.interface.new_socket(name = "Quality", in_out='INPUT', socket_type = 'NodeSocketInt')
			quality_socket_1.subtype = 'NONE'
			quality_socket_1.default_value = 3
			quality_socket_1.min_value = 0
			quality_socket_1.max_value = 8
			quality_socket_1.attribute_domain = 'POINT'
			quality_socket_1.description = "Quailty of the surface to generate"
			
			#Panel Surface
			surface_panel = style_surface.interface.new_panel("Surface", default_closed=True)
			#Socket Separate
			separate_socket = style_surface.interface.new_socket(name = "Separate", in_out='INPUT', socket_type = 'NodeSocketBool', parent = surface_panel)
			separate_socket.attribute_domain = 'POINT'
			separate_socket.description = "Whether to create separate surfaces, based on the 'Attribute' name"
			
			#Socket Attribute
			attribute_socket = style_surface.interface.new_socket(name = "Attribute", in_out='INPUT', socket_type = 'NodeSocketString', parent = surface_panel)
			attribute_socket.attribute_domain = 'POINT'
			attribute_socket.description = "Attribute to separate the surface by"
			
			#Socket Scale Radii
			scale_radii_socket_1 = style_surface.interface.new_socket(name = "Scale Radii", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = surface_panel)
			scale_radii_socket_1.subtype = 'NONE'
			scale_radii_socket_1.default_value = 1.5
			scale_radii_socket_1.min_value = 0.0
			scale_radii_socket_1.max_value = 10.0
			scale_radii_socket_1.attribute_domain = 'POINT'
			scale_radii_socket_1.description = "Scale the VDW radii of the atoms when creating the surface"
			
			#Socket Probe Size
			probe_size_socket_2 = style_surface.interface.new_socket(name = "Probe Size", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = surface_panel)
			probe_size_socket_2.subtype = 'NONE'
			probe_size_socket_2.default_value = 1.0
			probe_size_socket_2.min_value = 0.0
			probe_size_socket_2.max_value = 5.0
			probe_size_socket_2.attribute_domain = 'POINT'
			probe_size_socket_2.description = "Size of the probe that is used to check for solvent accessibility (Angstroms)"
			
			#Socket Triangulate
			triangulate_socket_1 = style_surface.interface.new_socket(name = "Triangulate", in_out='INPUT', socket_type = 'NodeSocketBool', parent = surface_panel)
			triangulate_socket_1.attribute_domain = 'POINT'
			triangulate_socket_1.description = "Whether to triangulate the resulting mesh. Can help reduce shading problems"
			
			#Socket Relaxation Steps
			relaxation_steps_socket_1 = style_surface.interface.new_socket(name = "Relaxation Steps", in_out='INPUT', socket_type = 'NodeSocketInt', parent = surface_panel)
			relaxation_steps_socket_1.subtype = 'NONE'
			relaxation_steps_socket_1.default_value = 10
			relaxation_steps_socket_1.min_value = 0
			relaxation_steps_socket_1.max_value = 2147483647
			relaxation_steps_socket_1.default_attribute_name = "Number of steps in the process of smoothening out the surface that stretches between atoms"
			relaxation_steps_socket_1.attribute_domain = 'POINT'
			
			
			#Panel Color
			color_panel = style_surface.interface.new_panel("Color", default_closed=True)
			#Socket Color by CA
			color_by_ca_socket_1 = style_surface.interface.new_socket(name = "Color by CA", in_out='INPUT', socket_type = 'NodeSocketBool', parent = color_panel)
			color_by_ca_socket_1.attribute_domain = 'POINT'
			color_by_ca_socket_1.description = "Only take colors from CA atoms (or similar in nucleic acids)"
			
			#Socket Color Blur
			color_blur_socket_1 = style_surface.interface.new_socket(name = "Color Blur", in_out='INPUT', socket_type = 'NodeSocketInt', parent = color_panel)
			color_blur_socket_1.subtype = 'NONE'
			color_blur_socket_1.default_value = 2
			color_blur_socket_1.min_value = 0
			color_blur_socket_1.max_value = 20
			color_blur_socket_1.attribute_domain = 'POINT'
			color_blur_socket_1.description = "When coloring the surface, blur colors from nearby atoms"
			
			
			#Panel Material
			material_panel = style_surface.interface.new_panel("Material", default_closed=True)
			#Socket Shade Smooth
			shade_smooth_socket_1 = style_surface.interface.new_socket(name = "Shade Smooth", in_out='INPUT', socket_type = 'NodeSocketBool', parent = material_panel)
			shade_smooth_socket_1.attribute_domain = 'POINT'
			shade_smooth_socket_1.description = "Apply smooth shading to the created geometry"
			
			#Socket Material
			material_socket_1 = style_surface.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial', parent = material_panel)
			material_socket_1.attribute_domain = 'POINT'
			material_socket_1.description = "Material to apply to the resulting geometry"
			
			
			
			#initialize style_surface nodes
			#node Attribute Statistic
			attribute_statistic = style_surface.nodes.new("GeometryNodeAttributeStatistic")
			attribute_statistic.name = "Attribute Statistic"
			attribute_statistic.data_type = 'FLOAT'
			attribute_statistic.domain = 'POINT'
			attribute_statistic.inputs[1].hide = True
			attribute_statistic.outputs[0].hide = True
			attribute_statistic.outputs[1].hide = True
			attribute_statistic.outputs[2].hide = True
			attribute_statistic.outputs[3].hide = True
			attribute_statistic.outputs[5].hide = True
			attribute_statistic.outputs[6].hide = True
			attribute_statistic.outputs[7].hide = True
			#Selection
			attribute_statistic.inputs[1].default_value = True
			
			#node Math.001
			math_001_3 = style_surface.nodes.new("ShaderNodeMath")
			math_001_3.label = "x + 1"
			math_001_3.name = "Math.001"
			math_001_3.hide = True
			math_001_3.operation = 'ADD'
			math_001_3.use_clamp = False
			#Value_001
			math_001_3.inputs[1].default_value = 1.0
			
			#node Separate Geometry.002
			separate_geometry_002 = style_surface.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_002.name = "Separate Geometry.002"
			separate_geometry_002.domain = 'POINT'
			
			#node Separate Geometry.001
			separate_geometry_001_1 = style_surface.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_001_1.name = "Separate Geometry.001"
			separate_geometry_001_1.domain = 'POINT'
			
			#node Group Output
			group_output_10 = style_surface.nodes.new("NodeGroupOutput")
			group_output_10.name = "Group Output"
			group_output_10.is_active_output = True
			
			#node Group Input
			group_input_10 = style_surface.nodes.new("NodeGroupInput")
			group_input_10.name = "Group Input"
			group_input_10.outputs[2].hide = True
			group_input_10.outputs[4].hide = True
			group_input_10.outputs[5].hide = True
			group_input_10.outputs[6].hide = True
			group_input_10.outputs[9].hide = True
			group_input_10.outputs[10].hide = True
			group_input_10.outputs[11].hide = True
			group_input_10.outputs[12].hide = True
			group_input_10.outputs[13].hide = True
			
			#node Reroute.002
			reroute_002_3 = style_surface.nodes.new("NodeReroute")
			reroute_002_3.name = "Reroute.002"
			#node Separate Geometry
			separate_geometry_1 = style_surface.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_1.name = "Separate Geometry"
			separate_geometry_1.domain = 'POINT'
			
			#node Compare
			compare_2 = style_surface.nodes.new("FunctionNodeCompare")
			compare_2.name = "Compare"
			compare_2.hide = True
			compare_2.data_type = 'INT'
			compare_2.mode = 'ELEMENT'
			compare_2.operation = 'EQUAL'
			
			#node Named Attribute
			named_attribute_4 = style_surface.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_4.name = "Named Attribute"
			named_attribute_4.data_type = 'INT'
			
			#node Group Input.002
			group_input_002_1 = style_surface.nodes.new("NodeGroupInput")
			group_input_002_1.name = "Group Input.002"
			group_input_002_1.outputs[0].hide = True
			group_input_002_1.outputs[1].hide = True
			group_input_002_1.outputs[2].hide = True
			group_input_002_1.outputs[3].hide = True
			group_input_002_1.outputs[5].hide = True
			group_input_002_1.outputs[6].hide = True
			group_input_002_1.outputs[9].hide = True
			group_input_002_1.outputs[10].hide = True
			group_input_002_1.outputs[11].hide = True
			group_input_002_1.outputs[12].hide = True
			group_input_002_1.outputs[13].hide = True
			
			#node Repeat Output
			repeat_output = style_surface.nodes.new("GeometryNodeRepeatOutput")
			repeat_output.name = "Repeat Output"
			repeat_output.active_index = 1
			repeat_output.inspection_index = 0
			repeat_output.repeat_items.clear()
			# Create item "Instances"
			repeat_output.repeat_items.new('GEOMETRY', "Instances")
			# Create item "Surfaces"
			repeat_output.repeat_items.new('GEOMETRY', "Surfaces")
			# Create item "Atoms"
			repeat_output.repeat_items.new('GEOMETRY', "Atoms")
			# Create item "i"
			repeat_output.repeat_items.new('INT', "i")
			
			#node Math
			math_1 = style_surface.nodes.new("ShaderNodeMath")
			math_1.label = "x + 1"
			math_1.name = "Math"
			math_1.hide = True
			math_1.operation = 'ADD'
			math_1.use_clamp = False
			#Value_001
			math_1.inputs[1].default_value = 1.0
			
			#node Group
			group_1 = style_surface.nodes.new("GeometryNodeGroup")
			group_1.name = "Group"
			group_1.node_tree = _mn_utils_to_instance_centred
			
			#node Join Geometry
			join_geometry = style_surface.nodes.new("GeometryNodeJoinGeometry")
			join_geometry.name = "Join Geometry"
			
			#node Join Geometry.001
			join_geometry_001 = style_surface.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_001.name = "Join Geometry.001"
			
			#node Reroute.001
			reroute_001_4 = style_surface.nodes.new("NodeReroute")
			reroute_001_4.name = "Reroute.001"
			#node Repeat Input
			repeat_input = style_surface.nodes.new("GeometryNodeRepeatInput")
			repeat_input.name = "Repeat Input"
			#node Join Geometry.002
			join_geometry_002 = style_surface.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_002.name = "Join Geometry.002"
			
			#node Group Input.001
			group_input_001_1 = style_surface.nodes.new("NodeGroupInput")
			group_input_001_1.name = "Group Input.001"
			group_input_001_1.outputs[4].hide = True
			
			#node Group.070
			group_070 = style_surface.nodes.new("GeometryNodeGroup")
			group_070.name = "Group.070"
			group_070.node_tree = _mn_utils_style_surface_new
			#Input_4
			group_070.inputs[1].default_value = True
			
			#node Group.071
			group_071 = style_surface.nodes.new("GeometryNodeGroup")
			group_071.name = "Group.071"
			group_071.node_tree = _mn_utils_style_surface_new
			#Input_4
			group_071.inputs[1].default_value = True
			
			#node Store Named Attribute
			store_named_attribute_1 = style_surface.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_1.name = "Store Named Attribute"
			store_named_attribute_1.data_type = 'INT'
			store_named_attribute_1.domain = 'POINT'
			#Selection
			store_named_attribute_1.inputs[1].default_value = True
			#Name
			store_named_attribute_1.inputs[2].default_value = "chain_id"
			
			#node Reroute.003
			reroute_003_2 = style_surface.nodes.new("NodeReroute")
			reroute_003_2.name = "Reroute.003"
			#node Store Named Attribute.001
			store_named_attribute_001 = style_surface.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_001.name = "Store Named Attribute.001"
			store_named_attribute_001.data_type = 'INT'
			store_named_attribute_001.domain = 'INSTANCE'
			#Selection
			store_named_attribute_001.inputs[1].default_value = True
			#Name
			store_named_attribute_001.inputs[2].default_value = "chain_id"
			
			#node Reroute
			reroute_3 = style_surface.nodes.new("NodeReroute")
			reroute_3.name = "Reroute"
			
			#Process zone input Repeat Input
			repeat_input.pair_with_output(repeat_output)
			#Item_1
			repeat_input.inputs[4].default_value = 0
			
			
			
			
			#Set locations
			attribute_statistic.location = (-453.89703369140625, 100.0)
			math_001_3.location = (-440.0, 160.0)
			separate_geometry_002.location = (-780.0, -360.0)
			separate_geometry_001_1.location = (-1020.0, -400.0)
			group_output_10.location = (2260.0, 140.0)
			group_input_10.location = (-1240.0, -480.0)
			reroute_002_3.location = (6.102944374084473, -360.0)
			separate_geometry_1.location = (80.0, 120.0)
			compare_2.location = (80.0, -40.0)
			named_attribute_4.location = (-460.0, -60.0)
			group_input_002_1.location = (-460.0, -200.0)
			repeat_output.location = (1280.0, 140.0)
			math_1.location = (1100.0, 20.0)
			group_1.location = (660.0, 260.0)
			join_geometry.location = (1100.0, 140.0)
			join_geometry_001.location = (1100.0, 360.0)
			reroute_001_4.location = (1760.0, -200.0)
			repeat_input.location = (-253.8970489501953, 220.0)
			join_geometry_002.location = (1900.0, 100.0)
			group_input_001_1.location = (-633.89697265625, -740.0)
			group_070.location = (340.0, -20.0)
			group_071.location = (300.0, -560.0)
			store_named_attribute_1.location = (860.0, 40.0)
			reroute_003_2.location = (700.0, 0.0)
			store_named_attribute_001.location = (920.0, 300.0)
			reroute_3.location = (-520.0, 120.0)
			
			#Set dimensions
			attribute_statistic.width, attribute_statistic.height = 140.0, 100.0
			math_001_3.width, math_001_3.height = 140.0, 100.0
			separate_geometry_002.width, separate_geometry_002.height = 140.0, 100.0
			separate_geometry_001_1.width, separate_geometry_001_1.height = 140.0, 100.0
			group_output_10.width, group_output_10.height = 140.0, 100.0
			group_input_10.width, group_input_10.height = 140.0, 100.0
			reroute_002_3.width, reroute_002_3.height = 16.0, 100.0
			separate_geometry_1.width, separate_geometry_1.height = 140.0, 100.0
			compare_2.width, compare_2.height = 140.0, 100.0
			named_attribute_4.width, named_attribute_4.height = 140.0, 100.0
			group_input_002_1.width, group_input_002_1.height = 140.0, 100.0
			repeat_output.width, repeat_output.height = 140.0, 100.0
			math_1.width, math_1.height = 140.0, 100.0
			group_1.width, group_1.height = 235.00048828125, 100.0
			join_geometry.width, join_geometry.height = 140.0, 100.0
			join_geometry_001.width, join_geometry_001.height = 140.0, 100.0
			reroute_001_4.width, reroute_001_4.height = 16.0, 100.0
			repeat_input.width, repeat_input.height = 140.0, 100.0
			join_geometry_002.width, join_geometry_002.height = 140.0, 100.0
			group_input_001_1.width, group_input_001_1.height = 140.0, 100.0
			group_070.width, group_070.height = 240.75701904296875, 100.0
			group_071.width, group_071.height = 240.75701904296875, 100.0
			store_named_attribute_1.width, store_named_attribute_1.height = 140.0, 100.0
			reroute_003_2.width, reroute_003_2.height = 16.0, 100.0
			store_named_attribute_001.width, store_named_attribute_001.height = 140.0, 100.0
			reroute_3.width, reroute_3.height = 16.0, 100.0
			
			#initialize style_surface links
			#reroute_003_2.Output -> math_1.Value
			style_surface.links.new(reroute_003_2.outputs[0], math_1.inputs[0])
			#math_1.Value -> repeat_output.i
			style_surface.links.new(math_1.outputs[0], repeat_output.inputs[3])
			#repeat_input.Atoms -> separate_geometry_1.Geometry
			style_surface.links.new(repeat_input.outputs[2], separate_geometry_1.inputs[0])
			#repeat_input.i -> compare_2.A
			style_surface.links.new(repeat_input.outputs[3], compare_2.inputs[2])
			#named_attribute_4.Attribute -> attribute_statistic.Attribute
			style_surface.links.new(named_attribute_4.outputs[0], attribute_statistic.inputs[2])
			#named_attribute_4.Attribute -> compare_2.B
			style_surface.links.new(named_attribute_4.outputs[0], compare_2.inputs[3])
			#compare_2.Result -> separate_geometry_1.Selection
			style_surface.links.new(compare_2.outputs[0], separate_geometry_1.inputs[1])
			#separate_geometry_1.Inverted -> repeat_output.Atoms
			style_surface.links.new(separate_geometry_1.outputs[1], repeat_output.inputs[2])
			#separate_geometry_1.Selection -> group_070.Atoms
			style_surface.links.new(separate_geometry_1.outputs[0], group_070.inputs[0])
			#store_named_attribute_1.Geometry -> join_geometry.Geometry
			style_surface.links.new(store_named_attribute_1.outputs[0], join_geometry.inputs[0])
			#join_geometry.Geometry -> repeat_output.Surfaces
			style_surface.links.new(join_geometry.outputs[0], repeat_output.inputs[1])
			#group_input_001_1.Material -> group_070.Material
			style_surface.links.new(group_input_001_1.outputs[12], group_070.inputs[9])
			#group_input_10.Atoms -> separate_geometry_001_1.Geometry
			style_surface.links.new(group_input_10.outputs[0], separate_geometry_001_1.inputs[0])
			#group_input_10.Selection -> separate_geometry_001_1.Selection
			style_surface.links.new(group_input_10.outputs[1], separate_geometry_001_1.inputs[1])
			#reroute_3.Output -> attribute_statistic.Geometry
			style_surface.links.new(reroute_3.outputs[0], attribute_statistic.inputs[0])
			#reroute_3.Output -> repeat_input.Atoms
			style_surface.links.new(reroute_3.outputs[0], repeat_input.inputs[3])
			#reroute_002_3.Output -> group_070.Quality
			style_surface.links.new(reroute_002_3.outputs[0], group_070.inputs[2])
			#group_input_001_1.Scale Radii -> group_070.Scale Radii
			style_surface.links.new(group_input_001_1.outputs[5], group_070.inputs[3])
			#group_input_001_1.Probe Size -> group_070.Probe Size
			style_surface.links.new(group_input_001_1.outputs[6], group_070.inputs[4])
			#group_input_001_1.Color by CA -> group_070.Color by CA
			style_surface.links.new(group_input_001_1.outputs[9], group_070.inputs[5])
			#group_input_001_1.Color Blur -> group_070.Color Blur
			style_surface.links.new(group_input_001_1.outputs[10], group_070.inputs[6])
			#group_input_001_1.Shade Smooth -> group_070.Shade Smooth
			style_surface.links.new(group_input_001_1.outputs[11], group_070.inputs[7])
			#store_named_attribute_001.Geometry -> join_geometry_001.Geometry
			style_surface.links.new(store_named_attribute_001.outputs[0], join_geometry_001.inputs[0])
			#join_geometry_001.Geometry -> repeat_output.Instances
			style_surface.links.new(join_geometry_001.outputs[0], repeat_output.inputs[0])
			#repeat_output.Instances -> group_output_10.Instances
			style_surface.links.new(repeat_output.outputs[0], group_output_10.inputs[1])
			#math_001_3.Value -> repeat_input.Iterations
			style_surface.links.new(math_001_3.outputs[0], repeat_input.inputs[0])
			#attribute_statistic.Max -> math_001_3.Value
			style_surface.links.new(attribute_statistic.outputs[4], math_001_3.inputs[0])
			#group_input_001_1.Material -> group_071.Material
			style_surface.links.new(group_input_001_1.outputs[12], group_071.inputs[9])
			#reroute_002_3.Output -> group_071.Quality
			style_surface.links.new(reroute_002_3.outputs[0], group_071.inputs[2])
			#group_input_001_1.Scale Radii -> group_071.Scale Radii
			style_surface.links.new(group_input_001_1.outputs[5], group_071.inputs[3])
			#group_input_001_1.Probe Size -> group_071.Probe Size
			style_surface.links.new(group_input_001_1.outputs[6], group_071.inputs[4])
			#group_input_001_1.Color by CA -> group_071.Color by CA
			style_surface.links.new(group_input_001_1.outputs[9], group_071.inputs[5])
			#group_input_001_1.Color Blur -> group_071.Color Blur
			style_surface.links.new(group_input_001_1.outputs[10], group_071.inputs[6])
			#group_input_001_1.Shade Smooth -> group_071.Shade Smooth
			style_surface.links.new(group_input_001_1.outputs[11], group_071.inputs[7])
			#separate_geometry_001_1.Selection -> separate_geometry_002.Geometry
			style_surface.links.new(separate_geometry_001_1.outputs[0], separate_geometry_002.inputs[0])
			#group_input_10.Separate -> separate_geometry_002.Selection
			style_surface.links.new(group_input_10.outputs[3], separate_geometry_002.inputs[1])
			#separate_geometry_002.Inverted -> group_071.Atoms
			style_surface.links.new(separate_geometry_002.outputs[1], group_071.inputs[0])
			#reroute_001_4.Output -> join_geometry_002.Geometry
			style_surface.links.new(reroute_001_4.outputs[0], join_geometry_002.inputs[0])
			#join_geometry_002.Geometry -> group_output_10.Geometry
			style_surface.links.new(join_geometry_002.outputs[0], group_output_10.inputs[0])
			#group_070.Surface Geometry -> group_1.Input
			style_surface.links.new(group_070.outputs[0], group_1.inputs[0])
			#group_071.Surface Geometry -> reroute_001_4.Input
			style_surface.links.new(group_071.outputs[0], reroute_001_4.inputs[0])
			#group_input_001_1.Quality -> reroute_002_3.Input
			style_surface.links.new(group_input_001_1.outputs[2], reroute_002_3.inputs[0])
			#group_input_002_1.Attribute -> named_attribute_4.Name
			style_surface.links.new(group_input_002_1.outputs[4], named_attribute_4.inputs[0])
			#group_input_001_1.Relaxation Steps -> group_070.Relaxation Steps
			style_surface.links.new(group_input_001_1.outputs[8], group_070.inputs[10])
			#group_input_001_1.Relaxation Steps -> group_071.Relaxation Steps
			style_surface.links.new(group_input_001_1.outputs[8], group_071.inputs[10])
			#group_input_001_1.Triangulate -> group_071.Triangulate
			style_surface.links.new(group_input_001_1.outputs[7], group_071.inputs[8])
			#group_input_001_1.Triangulate -> group_070.Triangulate
			style_surface.links.new(group_input_001_1.outputs[7], group_070.inputs[8])
			#group_070.Surface Geometry -> store_named_attribute_1.Geometry
			style_surface.links.new(group_070.outputs[0], store_named_attribute_1.inputs[0])
			#reroute_003_2.Output -> store_named_attribute_1.Value
			style_surface.links.new(reroute_003_2.outputs[0], store_named_attribute_1.inputs[3])
			#repeat_input.i -> reroute_003_2.Input
			style_surface.links.new(repeat_input.outputs[3], reroute_003_2.inputs[0])
			#group_1.Geometry -> store_named_attribute_001.Geometry
			style_surface.links.new(group_1.outputs[0], store_named_attribute_001.inputs[0])
			#reroute_003_2.Output -> store_named_attribute_001.Value
			style_surface.links.new(reroute_003_2.outputs[0], store_named_attribute_001.inputs[3])
			#separate_geometry_002.Selection -> reroute_3.Input
			style_surface.links.new(separate_geometry_002.outputs[0], reroute_3.inputs[0])
			#repeat_input.Instances -> join_geometry_001.Geometry
			style_surface.links.new(repeat_input.outputs[0], join_geometry_001.inputs[0])
			#repeat_input.Surfaces -> join_geometry.Geometry
			style_surface.links.new(repeat_input.outputs[1], join_geometry.inputs[0])
			#repeat_output.Surfaces -> join_geometry_002.Geometry
			style_surface.links.new(repeat_output.outputs[1], join_geometry_002.inputs[0])
			return style_surface

		style_surface = style_surface_node_group()

		#initialize _mn_world_scale node group
		def _mn_world_scale_node_group():
			_mn_world_scale = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_world_scale")

			_mn_world_scale.color_tag = 'NONE'
			_mn_world_scale.description = ""

			
			#_mn_world_scale interface
			#Socket world_scale
			world_scale_socket = _mn_world_scale.interface.new_socket(name = "world_scale", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			world_scale_socket.subtype = 'NONE'
			world_scale_socket.default_value = 0.009999999776482582
			world_scale_socket.min_value = -3.4028234663852886e+38
			world_scale_socket.max_value = 3.4028234663852886e+38
			world_scale_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_world_scale nodes
			#node Group Input
			group_input_11 = _mn_world_scale.nodes.new("NodeGroupInput")
			group_input_11.name = "Group Input"
			
			#node Value
			value_1 = _mn_world_scale.nodes.new("ShaderNodeValue")
			value_1.label = "world_scale"
			value_1.name = "Value"
			
			value_1.outputs[0].default_value = 0.009999999776482582
			#node Group Output
			group_output_11 = _mn_world_scale.nodes.new("NodeGroupOutput")
			group_output_11.name = "Group Output"
			group_output_11.is_active_output = True
			
			
			
			
			#Set locations
			group_input_11.location = (-200.0, 0.0)
			value_1.location = (0.0, 0.0)
			group_output_11.location = (190.0, 0.0)
			
			#Set dimensions
			group_input_11.width, group_input_11.height = 140.0, 100.0
			value_1.width, value_1.height = 140.0, 100.0
			group_output_11.width, group_output_11.height = 140.0, 100.0
			
			#initialize _mn_world_scale links
			#value_1.Value -> group_output_11.world_scale
			_mn_world_scale.links.new(value_1.outputs[0], group_output_11.inputs[0])
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
			angstrom_socket.subtype = 'NONE'
			angstrom_socket.default_value = 0.0
			angstrom_socket.min_value = -3.4028234663852886e+38
			angstrom_socket.max_value = 3.4028234663852886e+38
			angstrom_socket.attribute_domain = 'POINT'
			
			#Socket Nanometre
			nanometre_socket = mn_units.interface.new_socket(name = "Nanometre", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			nanometre_socket.subtype = 'NONE'
			nanometre_socket.default_value = 0.0
			nanometre_socket.min_value = -3.4028234663852886e+38
			nanometre_socket.max_value = 3.4028234663852886e+38
			nanometre_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket = mn_units.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket.subtype = 'NONE'
			value_socket.default_value = 3.0
			value_socket.min_value = -10000.0
			value_socket.max_value = 10000.0
			value_socket.attribute_domain = 'POINT'
			value_socket.description = "A value which will be scaled appropriately for the world"
			
			
			#initialize mn_units nodes
			#node Group Output
			group_output_12 = mn_units.nodes.new("NodeGroupOutput")
			group_output_12.name = "Group Output"
			group_output_12.is_active_output = True
			
			#node Group Input
			group_input_12 = mn_units.nodes.new("NodeGroupInput")
			group_input_12.name = "Group Input"
			
			#node Math
			math_2 = mn_units.nodes.new("ShaderNodeMath")
			math_2.name = "Math"
			math_2.operation = 'MULTIPLY'
			math_2.use_clamp = False
			
			#node Math.001
			math_001_4 = mn_units.nodes.new("ShaderNodeMath")
			math_001_4.name = "Math.001"
			math_001_4.operation = 'MULTIPLY'
			math_001_4.use_clamp = False
			#Value_001
			math_001_4.inputs[1].default_value = 10.0
			
			#node Group
			group_2 = mn_units.nodes.new("GeometryNodeGroup")
			group_2.name = "Group"
			group_2.node_tree = _mn_world_scale
			
			
			
			
			#Set locations
			group_output_12.location = (190.0, 0.0)
			group_input_12.location = (-240.0, 0.0)
			math_2.location = (-60.0, 0.0)
			math_001_4.location = (-60.0, -160.0)
			group_2.location = (-304.00421142578125, -104.114013671875)
			
			#Set dimensions
			group_output_12.width, group_output_12.height = 140.0, 100.0
			group_input_12.width, group_input_12.height = 140.0, 100.0
			math_2.width, math_2.height = 140.0, 100.0
			math_001_4.width, math_001_4.height = 140.0, 100.0
			group_2.width, group_2.height = 197.58424377441406, 100.0
			
			#initialize mn_units links
			#math_2.Value -> group_output_12.Angstrom
			mn_units.links.new(math_2.outputs[0], group_output_12.inputs[0])
			#group_input_12.Value -> math_2.Value
			mn_units.links.new(group_input_12.outputs[0], math_2.inputs[0])
			#group_2.world_scale -> math_2.Value
			mn_units.links.new(group_2.outputs[0], math_2.inputs[1])
			#math_2.Value -> math_001_4.Value
			mn_units.links.new(math_2.outputs[0], math_001_4.inputs[0])
			#math_001_4.Value -> group_output_12.Nanometre
			mn_units.links.new(math_001_4.outputs[0], group_output_12.inputs[1])
			return mn_units

		mn_units = mn_units_node_group()

		#initialize _mn_utils_style_spheres_points node group
		def _mn_utils_style_spheres_points_node_group():
			_mn_utils_style_spheres_points = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_utils_style_spheres_points")

			_mn_utils_style_spheres_points.color_tag = 'GEOMETRY'
			_mn_utils_style_spheres_points.description = ""

			_mn_utils_style_spheres_points.is_modifier = True
			
			#_mn_utils_style_spheres_points interface
			#Socket Point Cloud
			point_cloud_socket = _mn_utils_style_spheres_points.interface.new_socket(name = "Point Cloud", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			point_cloud_socket.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket_3 = _mn_utils_style_spheres_points.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_3.attribute_domain = 'POINT'
			atoms_socket_3.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket_3 = _mn_utils_style_spheres_points.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_3.attribute_domain = 'POINT'
			selection_socket_3.hide_value = True
			selection_socket_3.description = "Selection of atoms to apply this node to"
			
			#Socket Radii
			radii_socket = _mn_utils_style_spheres_points.interface.new_socket(name = "Radii", in_out='INPUT', socket_type = 'NodeSocketFloat')
			radii_socket.subtype = 'NONE'
			radii_socket.default_value = 0.800000011920929
			radii_socket.min_value = 0.0
			radii_socket.max_value = 10000.0
			radii_socket.attribute_domain = 'POINT'
			
			#Socket Material
			material_socket_2 = _mn_utils_style_spheres_points.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial')
			material_socket_2.attribute_domain = 'POINT'
			material_socket_2.description = "Material to apply to the resulting geometry"
			
			
			#initialize _mn_utils_style_spheres_points nodes
			#node Group Input
			group_input_13 = _mn_utils_style_spheres_points.nodes.new("NodeGroupInput")
			group_input_13.name = "Group Input"
			
			#node Mesh to Points
			mesh_to_points = _mn_utils_style_spheres_points.nodes.new("GeometryNodeMeshToPoints")
			mesh_to_points.name = "Mesh to Points"
			mesh_to_points.mode = 'VERTICES'
			#Position
			mesh_to_points.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Switch
			switch_2 = _mn_utils_style_spheres_points.nodes.new("GeometryNodeSwitch")
			switch_2.name = "Switch"
			switch_2.input_type = 'FLOAT'
			
			#node Named Attribute
			named_attribute_5 = _mn_utils_style_spheres_points.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_5.name = "Named Attribute"
			named_attribute_5.data_type = 'FLOAT'
			#Name
			named_attribute_5.inputs[0].default_value = "vdw_radii"
			
			#node Group
			group_3 = _mn_utils_style_spheres_points.nodes.new("GeometryNodeGroup")
			group_3.name = "Group"
			group_3.node_tree = mn_units
			#Input_1
			group_3.inputs[0].default_value = 0.800000011920929
			
			#node Math
			math_3 = _mn_utils_style_spheres_points.nodes.new("ShaderNodeMath")
			math_3.name = "Math"
			math_3.operation = 'MULTIPLY'
			math_3.use_clamp = False
			
			#node Group Output
			group_output_13 = _mn_utils_style_spheres_points.nodes.new("NodeGroupOutput")
			group_output_13.name = "Group Output"
			group_output_13.is_active_output = True
			
			#node Set Material
			set_material_1 = _mn_utils_style_spheres_points.nodes.new("GeometryNodeSetMaterial")
			set_material_1.name = "Set Material"
			#Selection
			set_material_1.inputs[1].default_value = True
			
			
			
			
			#Set locations
			group_input_13.location = (-1060.0, 60.0)
			mesh_to_points.location = (-540.0, 220.0)
			switch_2.location = (-900.0, -100.0)
			named_attribute_5.location = (-1080.0, -100.0)
			group_3.location = (-1080.0, -240.0)
			math_3.location = (-720.0, 40.0)
			group_output_13.location = (-220.0, 220.0)
			set_material_1.location = (-380.0, 220.0)
			
			#Set dimensions
			group_input_13.width, group_input_13.height = 140.0, 100.0
			mesh_to_points.width, mesh_to_points.height = 140.0, 100.0
			switch_2.width, switch_2.height = 140.0, 100.0
			named_attribute_5.width, named_attribute_5.height = 140.0, 100.0
			group_3.width, group_3.height = 140.0, 100.0
			math_3.width, math_3.height = 140.0, 100.0
			group_output_13.width, group_output_13.height = 140.0, 100.0
			set_material_1.width, set_material_1.height = 140.0, 100.0
			
			#initialize _mn_utils_style_spheres_points links
			#set_material_1.Geometry -> group_output_13.Point Cloud
			_mn_utils_style_spheres_points.links.new(set_material_1.outputs[0], group_output_13.inputs[0])
			#group_input_13.Selection -> mesh_to_points.Selection
			_mn_utils_style_spheres_points.links.new(group_input_13.outputs[1], mesh_to_points.inputs[1])
			#group_input_13.Radii -> math_3.Value
			_mn_utils_style_spheres_points.links.new(group_input_13.outputs[2], math_3.inputs[0])
			#math_3.Value -> mesh_to_points.Radius
			_mn_utils_style_spheres_points.links.new(math_3.outputs[0], mesh_to_points.inputs[3])
			#group_input_13.Material -> set_material_1.Material
			_mn_utils_style_spheres_points.links.new(group_input_13.outputs[3], set_material_1.inputs[2])
			#named_attribute_5.Attribute -> switch_2.Switch
			_mn_utils_style_spheres_points.links.new(named_attribute_5.outputs[0], switch_2.inputs[0])
			#named_attribute_5.Attribute -> switch_2.True
			_mn_utils_style_spheres_points.links.new(named_attribute_5.outputs[0], switch_2.inputs[2])
			#switch_2.Output -> math_3.Value
			_mn_utils_style_spheres_points.links.new(switch_2.outputs[0], math_3.inputs[1])
			#group_input_13.Atoms -> mesh_to_points.Mesh
			_mn_utils_style_spheres_points.links.new(group_input_13.outputs[0], mesh_to_points.inputs[0])
			#mesh_to_points.Points -> set_material_1.Geometry
			_mn_utils_style_spheres_points.links.new(mesh_to_points.outputs[0], set_material_1.inputs[0])
			#group_3.Angstrom -> switch_2.False
			_mn_utils_style_spheres_points.links.new(group_3.outputs[0], switch_2.inputs[1])
			return _mn_utils_style_spheres_points

		_mn_utils_style_spheres_points = _mn_utils_style_spheres_points_node_group()

		#initialize _mn_utils_style_spheres_icosphere node group
		def _mn_utils_style_spheres_icosphere_node_group():
			_mn_utils_style_spheres_icosphere = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_utils_style_spheres_icosphere")

			_mn_utils_style_spheres_icosphere.color_tag = 'GEOMETRY'
			_mn_utils_style_spheres_icosphere.description = ""

			_mn_utils_style_spheres_icosphere.is_modifier = True
			
			#_mn_utils_style_spheres_icosphere interface
			#Socket Instances
			instances_socket_1 = _mn_utils_style_spheres_icosphere.interface.new_socket(name = "Instances", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			instances_socket_1.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket_4 = _mn_utils_style_spheres_icosphere.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_4.attribute_domain = 'POINT'
			atoms_socket_4.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket_4 = _mn_utils_style_spheres_icosphere.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_4.attribute_domain = 'POINT'
			selection_socket_4.hide_value = True
			selection_socket_4.description = "Selection of atoms to apply this node to"
			
			#Socket Radii
			radii_socket_1 = _mn_utils_style_spheres_icosphere.interface.new_socket(name = "Radii", in_out='INPUT', socket_type = 'NodeSocketFloat')
			radii_socket_1.subtype = 'NONE'
			radii_socket_1.default_value = 0.800000011920929
			radii_socket_1.min_value = 0.0
			radii_socket_1.max_value = 10000.0
			radii_socket_1.attribute_domain = 'POINT'
			radii_socket_1.description = "Scale the VDW radii of the atoms."
			
			#Socket Subdivisions
			subdivisions_socket_1 = _mn_utils_style_spheres_icosphere.interface.new_socket(name = "Subdivisions", in_out='INPUT', socket_type = 'NodeSocketInt')
			subdivisions_socket_1.subtype = 'NONE'
			subdivisions_socket_1.default_value = 2
			subdivisions_socket_1.min_value = 0
			subdivisions_socket_1.max_value = 5
			subdivisions_socket_1.attribute_domain = 'POINT'
			
			#Socket Shade Smooth
			shade_smooth_socket_2 = _mn_utils_style_spheres_icosphere.interface.new_socket(name = "Shade Smooth", in_out='INPUT', socket_type = 'NodeSocketBool')
			shade_smooth_socket_2.attribute_domain = 'POINT'
			shade_smooth_socket_2.description = "Apply smooth shading to the created geometry"
			
			#Socket Material
			material_socket_3 = _mn_utils_style_spheres_icosphere.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial')
			material_socket_3.attribute_domain = 'POINT'
			material_socket_3.description = "Material to apply to the resulting geometry"
			
			
			#initialize _mn_utils_style_spheres_icosphere nodes
			#node Frame
			frame_2 = _mn_utils_style_spheres_icosphere.nodes.new("NodeFrame")
			frame_2.label = "Different Levels of Detail."
			frame_2.name = "Frame"
			frame_2.label_size = 20
			frame_2.shrink = True
			
			#node Reroute
			reroute_4 = _mn_utils_style_spheres_icosphere.nodes.new("NodeReroute")
			reroute_4.name = "Reroute"
			#node Math.001
			math_001_5 = _mn_utils_style_spheres_icosphere.nodes.new("ShaderNodeMath")
			math_001_5.name = "Math.001"
			math_001_5.operation = 'MINIMUM'
			math_001_5.use_clamp = False
			
			#node Group Output
			group_output_14 = _mn_utils_style_spheres_icosphere.nodes.new("NodeGroupOutput")
			group_output_14.name = "Group Output"
			group_output_14.is_active_output = True
			
			#node Group Input.002
			group_input_002_2 = _mn_utils_style_spheres_icosphere.nodes.new("NodeGroupInput")
			group_input_002_2.name = "Group Input.002"
			group_input_002_2.outputs[0].hide = True
			group_input_002_2.outputs[1].hide = True
			group_input_002_2.outputs[2].hide = True
			group_input_002_2.outputs[3].hide = True
			group_input_002_2.outputs[6].hide = True
			
			#node Set Shade Smooth
			set_shade_smooth = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeSetShadeSmooth")
			set_shade_smooth.name = "Set Shade Smooth"
			set_shade_smooth.domain = 'FACE'
			#Selection
			set_shade_smooth.inputs[1].default_value = True
			
			#node Set Material
			set_material_2 = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeSetMaterial")
			set_material_2.name = "Set Material"
			#Selection
			set_material_2.inputs[1].default_value = True
			
			#node Group Input
			group_input_14 = _mn_utils_style_spheres_icosphere.nodes.new("NodeGroupInput")
			group_input_14.name = "Group Input"
			group_input_14.outputs[2].hide = True
			group_input_14.outputs[3].hide = True
			group_input_14.outputs[4].hide = True
			group_input_14.outputs[5].hide = True
			group_input_14.outputs[6].hide = True
			
			#node Reroute.001
			reroute_001_5 = _mn_utils_style_spheres_icosphere.nodes.new("NodeReroute")
			reroute_001_5.name = "Reroute.001"
			#node Group Input.001
			group_input_001_2 = _mn_utils_style_spheres_icosphere.nodes.new("NodeGroupInput")
			group_input_001_2.name = "Group Input.001"
			group_input_001_2.outputs[0].hide = True
			group_input_001_2.outputs[1].hide = True
			group_input_001_2.outputs[2].hide = True
			group_input_001_2.outputs[4].hide = True
			group_input_001_2.outputs[5].hide = True
			group_input_001_2.outputs[6].hide = True
			
			#node Ico Sphere.001
			ico_sphere_001 = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeMeshIcoSphere")
			ico_sphere_001.name = "Ico Sphere.001"
			#Radius
			ico_sphere_001.inputs[0].default_value = 1.0
			#Subdivisions
			ico_sphere_001.inputs[1].default_value = 1
			
			#node Ico Sphere.002
			ico_sphere_002 = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeMeshIcoSphere")
			ico_sphere_002.name = "Ico Sphere.002"
			#Radius
			ico_sphere_002.inputs[0].default_value = 1.0
			#Subdivisions
			ico_sphere_002.inputs[1].default_value = 2
			
			#node Ico Sphere.003
			ico_sphere_003 = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeMeshIcoSphere")
			ico_sphere_003.name = "Ico Sphere.003"
			#Radius
			ico_sphere_003.inputs[0].default_value = 1.0
			#Subdivisions
			ico_sphere_003.inputs[1].default_value = 3
			
			#node Geometry to Instance
			geometry_to_instance_1 = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeGeometryToInstance")
			geometry_to_instance_1.name = "Geometry to Instance"
			
			#node Ico Sphere.004
			ico_sphere_004 = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeMeshIcoSphere")
			ico_sphere_004.name = "Ico Sphere.004"
			#Radius
			ico_sphere_004.inputs[0].default_value = 1.0
			#Subdivisions
			ico_sphere_004.inputs[1].default_value = 4
			
			#node Ico Sphere.005
			ico_sphere_005 = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeMeshIcoSphere")
			ico_sphere_005.name = "Ico Sphere.005"
			#Radius
			ico_sphere_005.inputs[0].default_value = 1.0
			#Subdivisions
			ico_sphere_005.inputs[1].default_value = 5
			
			#node Reroute.002
			reroute_002_4 = _mn_utils_style_spheres_icosphere.nodes.new("NodeReroute")
			reroute_002_4.name = "Reroute.002"
			#node Transform Geometry
			transform_geometry_1 = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeTransform")
			transform_geometry_1.name = "Transform Geometry"
			transform_geometry_1.mode = 'COMPONENTS'
			#Translation
			transform_geometry_1.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Rotation
			transform_geometry_1.inputs[2].default_value = (0.7853981852531433, 0.7853981852531433, 0.0)
			#Scale
			transform_geometry_1.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Cube
			cube = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeMeshCube")
			cube.name = "Cube"
			#Size
			cube.inputs[0].default_value = (1.0, 1.0, 1.0)
			#Vertices X
			cube.inputs[1].default_value = 2
			#Vertices Y
			cube.inputs[2].default_value = 2
			#Vertices Z
			cube.inputs[3].default_value = 2
			
			#node Named Attribute
			named_attribute_6 = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_6.name = "Named Attribute"
			named_attribute_6.data_type = 'FLOAT'
			#Name
			named_attribute_6.inputs[0].default_value = "vdw_radii"
			
			#node Radius
			radius = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeInputRadius")
			radius.name = "Radius"
			
			#node Math
			math_4 = _mn_utils_style_spheres_icosphere.nodes.new("ShaderNodeMath")
			math_4.name = "Math"
			math_4.operation = 'MAXIMUM'
			math_4.use_clamp = False
			
			#node Math.003
			math_003_3 = _mn_utils_style_spheres_icosphere.nodes.new("ShaderNodeMath")
			math_003_3.name = "Math.003"
			math_003_3.operation = 'MULTIPLY'
			math_003_3.use_clamp = False
			
			#node Group Input.003
			group_input_003_1 = _mn_utils_style_spheres_icosphere.nodes.new("NodeGroupInput")
			group_input_003_1.name = "Group Input.003"
			group_input_003_1.outputs[0].hide = True
			group_input_003_1.outputs[1].hide = True
			group_input_003_1.outputs[3].hide = True
			group_input_003_1.outputs[4].hide = True
			group_input_003_1.outputs[5].hide = True
			group_input_003_1.outputs[6].hide = True
			
			#node Math.002
			math_002_2 = _mn_utils_style_spheres_icosphere.nodes.new("ShaderNodeMath")
			math_002_2.name = "Math.002"
			math_002_2.operation = 'ADD'
			math_002_2.use_clamp = False
			
			#node Integer
			integer_2 = _mn_utils_style_spheres_icosphere.nodes.new("FunctionNodeInputInt")
			integer_2.name = "Integer"
			integer_2.integer = -1
			
			#node Domain Size
			domain_size = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeAttributeDomainSize")
			domain_size.name = "Domain Size"
			domain_size.component = 'INSTANCES'
			
			#node Instance on Points
			instance_on_points = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeInstanceOnPoints")
			instance_on_points.name = "Instance on Points"
			#Pick Instance
			instance_on_points.inputs[3].default_value = True
			#Rotation
			instance_on_points.inputs[5].default_value = (0.0, 0.0, 0.0)
			
			
			
			#Set parents
			ico_sphere_001.parent = frame_2
			ico_sphere_002.parent = frame_2
			ico_sphere_003.parent = frame_2
			geometry_to_instance_1.parent = frame_2
			ico_sphere_004.parent = frame_2
			ico_sphere_005.parent = frame_2
			reroute_002_4.parent = frame_2
			transform_geometry_1.parent = frame_2
			cube.parent = frame_2
			
			#Set locations
			frame_2.location = (0.0, 0.0)
			reroute_4.location = (-560.0, -40.0)
			math_001_5.location = (-140.0, 60.0)
			group_output_14.location = (835.407470703125, 359.5566711425781)
			group_input_002_2.location = (320.0, 260.0)
			set_shade_smooth.location = (500.0, 340.0)
			set_material_2.location = (660.0, 340.0)
			group_input_14.location = (-160.0, 240.0)
			reroute_001_5.location = (-480.0, 120.0)
			group_input_001_2.location = (-300.0, 60.0)
			ico_sphere_001.location = (-1180.0, 120.0)
			ico_sphere_002.location = (-1180.0, -20.0)
			ico_sphere_003.location = (-1180.0, -160.0)
			geometry_to_instance_1.location = (-940.0, 0.0)
			ico_sphere_004.location = (-1180.0, -300.0)
			ico_sphere_005.location = (-1180.0, -440.0)
			reroute_002_4.location = (-1040.0, 160.0)
			transform_geometry_1.location = (-1360.0, 200.0)
			cube.location = (-1520.0, 200.0)
			named_attribute_6.location = (-240.0, -340.0)
			radius.location = (-240.0, -480.0)
			math_4.location = (-60.0, -340.0)
			math_003_3.location = (100.0, -340.0)
			group_input_003_1.location = (-60.0, -520.0)
			math_002_2.location = (-140.0, -100.0)
			integer_2.location = (-320.0, -220.0)
			domain_size.location = (-320.0, -100.0)
			instance_on_points.location = (91.33897399902344, 216.86837768554688)
			
			#Set dimensions
			frame_2.width, frame_2.height = 800.0, 829.0
			reroute_4.width, reroute_4.height = 16.0, 100.0
			math_001_5.width, math_001_5.height = 140.0, 100.0
			group_output_14.width, group_output_14.height = 140.0, 100.0
			group_input_002_2.width, group_input_002_2.height = 140.0, 100.0
			set_shade_smooth.width, set_shade_smooth.height = 140.0, 100.0
			set_material_2.width, set_material_2.height = 140.0, 100.0
			group_input_14.width, group_input_14.height = 140.0, 100.0
			reroute_001_5.width, reroute_001_5.height = 16.0, 100.0
			group_input_001_2.width, group_input_001_2.height = 140.0, 100.0
			ico_sphere_001.width, ico_sphere_001.height = 140.0, 100.0
			ico_sphere_002.width, ico_sphere_002.height = 140.0, 100.0
			ico_sphere_003.width, ico_sphere_003.height = 140.0, 100.0
			geometry_to_instance_1.width, geometry_to_instance_1.height = 160.0, 100.0
			ico_sphere_004.width, ico_sphere_004.height = 140.0, 100.0
			ico_sphere_005.width, ico_sphere_005.height = 140.0, 100.0
			reroute_002_4.width, reroute_002_4.height = 16.0, 100.0
			transform_geometry_1.width, transform_geometry_1.height = 140.0, 100.0
			cube.width, cube.height = 140.0, 100.0
			named_attribute_6.width, named_attribute_6.height = 140.0, 100.0
			radius.width, radius.height = 140.0, 100.0
			math_4.width, math_4.height = 140.0, 100.0
			math_003_3.width, math_003_3.height = 140.0, 100.0
			group_input_003_1.width, group_input_003_1.height = 140.0, 100.0
			math_002_2.width, math_002_2.height = 140.0, 100.0
			integer_2.width, integer_2.height = 140.0, 100.0
			domain_size.width, domain_size.height = 140.0, 100.0
			instance_on_points.width, instance_on_points.height = 140.9404296875, 100.0
			
			#initialize _mn_utils_style_spheres_icosphere links
			#set_material_2.Geometry -> group_output_14.Instances
			_mn_utils_style_spheres_icosphere.links.new(set_material_2.outputs[0], group_output_14.inputs[0])
			#set_shade_smooth.Geometry -> set_material_2.Geometry
			_mn_utils_style_spheres_icosphere.links.new(set_shade_smooth.outputs[0], set_material_2.inputs[0])
			#group_input_14.Atoms -> instance_on_points.Points
			_mn_utils_style_spheres_icosphere.links.new(group_input_14.outputs[0], instance_on_points.inputs[0])
			#reroute_001_5.Output -> instance_on_points.Instance
			_mn_utils_style_spheres_icosphere.links.new(reroute_001_5.outputs[0], instance_on_points.inputs[2])
			#ico_sphere_005.Mesh -> geometry_to_instance_1.Geometry
			_mn_utils_style_spheres_icosphere.links.new(ico_sphere_005.outputs[0], geometry_to_instance_1.inputs[0])
			#math_001_5.Value -> instance_on_points.Instance Index
			_mn_utils_style_spheres_icosphere.links.new(math_001_5.outputs[0], instance_on_points.inputs[4])
			#group_input_001_2.Subdivisions -> math_001_5.Value
			_mn_utils_style_spheres_icosphere.links.new(group_input_001_2.outputs[3], math_001_5.inputs[0])
			#reroute_4.Output -> domain_size.Geometry
			_mn_utils_style_spheres_icosphere.links.new(reroute_4.outputs[0], domain_size.inputs[0])
			#geometry_to_instance_1.Instances -> reroute_4.Input
			_mn_utils_style_spheres_icosphere.links.new(geometry_to_instance_1.outputs[0], reroute_4.inputs[0])
			#named_attribute_6.Attribute -> math_4.Value
			_mn_utils_style_spheres_icosphere.links.new(named_attribute_6.outputs[0], math_4.inputs[0])
			#radius.Radius -> math_4.Value
			_mn_utils_style_spheres_icosphere.links.new(radius.outputs[0], math_4.inputs[1])
			#group_input_002_2.Material -> set_material_2.Material
			_mn_utils_style_spheres_icosphere.links.new(group_input_002_2.outputs[5], set_material_2.inputs[2])
			#instance_on_points.Instances -> set_shade_smooth.Geometry
			_mn_utils_style_spheres_icosphere.links.new(instance_on_points.outputs[0], set_shade_smooth.inputs[0])
			#group_input_002_2.Shade Smooth -> set_shade_smooth.Shade Smooth
			_mn_utils_style_spheres_icosphere.links.new(group_input_002_2.outputs[4], set_shade_smooth.inputs[2])
			#group_input_14.Selection -> instance_on_points.Selection
			_mn_utils_style_spheres_icosphere.links.new(group_input_14.outputs[1], instance_on_points.inputs[1])
			#math_4.Value -> math_003_3.Value
			_mn_utils_style_spheres_icosphere.links.new(math_4.outputs[0], math_003_3.inputs[0])
			#group_input_003_1.Radii -> math_003_3.Value
			_mn_utils_style_spheres_icosphere.links.new(group_input_003_1.outputs[2], math_003_3.inputs[1])
			#reroute_4.Output -> reroute_001_5.Input
			_mn_utils_style_spheres_icosphere.links.new(reroute_4.outputs[0], reroute_001_5.inputs[0])
			#math_003_3.Value -> instance_on_points.Scale
			_mn_utils_style_spheres_icosphere.links.new(math_003_3.outputs[0], instance_on_points.inputs[6])
			#cube.Mesh -> transform_geometry_1.Geometry
			_mn_utils_style_spheres_icosphere.links.new(cube.outputs[0], transform_geometry_1.inputs[0])
			#transform_geometry_1.Geometry -> reroute_002_4.Input
			_mn_utils_style_spheres_icosphere.links.new(transform_geometry_1.outputs[0], reroute_002_4.inputs[0])
			#domain_size.Instance Count -> math_002_2.Value
			_mn_utils_style_spheres_icosphere.links.new(domain_size.outputs[5], math_002_2.inputs[0])
			#integer_2.Integer -> math_002_2.Value
			_mn_utils_style_spheres_icosphere.links.new(integer_2.outputs[0], math_002_2.inputs[1])
			#math_002_2.Value -> math_001_5.Value
			_mn_utils_style_spheres_icosphere.links.new(math_002_2.outputs[0], math_001_5.inputs[1])
			#ico_sphere_004.Mesh -> geometry_to_instance_1.Geometry
			_mn_utils_style_spheres_icosphere.links.new(ico_sphere_004.outputs[0], geometry_to_instance_1.inputs[0])
			#ico_sphere_003.Mesh -> geometry_to_instance_1.Geometry
			_mn_utils_style_spheres_icosphere.links.new(ico_sphere_003.outputs[0], geometry_to_instance_1.inputs[0])
			#ico_sphere_002.Mesh -> geometry_to_instance_1.Geometry
			_mn_utils_style_spheres_icosphere.links.new(ico_sphere_002.outputs[0], geometry_to_instance_1.inputs[0])
			#ico_sphere_001.Mesh -> geometry_to_instance_1.Geometry
			_mn_utils_style_spheres_icosphere.links.new(ico_sphere_001.outputs[0], geometry_to_instance_1.inputs[0])
			#reroute_002_4.Output -> geometry_to_instance_1.Geometry
			_mn_utils_style_spheres_icosphere.links.new(reroute_002_4.outputs[0], geometry_to_instance_1.inputs[0])
			return _mn_utils_style_spheres_icosphere

		_mn_utils_style_spheres_icosphere = _mn_utils_style_spheres_icosphere_node_group()

		#initialize style_spheres node group
		def style_spheres_node_group():
			style_spheres = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Style Spheres")

			style_spheres.color_tag = 'GEOMETRY'
			style_spheres.description = ""

			style_spheres.is_modifier = True
			
			#style_spheres interface
			#Socket Geometry
			geometry_socket_5 = style_spheres.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_5.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket_5 = style_spheres.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_5.attribute_domain = 'POINT'
			atoms_socket_5.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket_5 = style_spheres.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_5.attribute_domain = 'POINT'
			selection_socket_5.hide_value = True
			selection_socket_5.description = "Selection of atoms to apply this style to"
			
			#Panel Sphere
			sphere_panel = style_spheres.interface.new_panel("Sphere")
			#Socket Sphere As Mesh
			sphere_as_mesh_socket = style_spheres.interface.new_socket(name = "Sphere As Mesh", in_out='INPUT', socket_type = 'NodeSocketBool', parent = sphere_panel)
			sphere_as_mesh_socket.attribute_domain = 'POINT'
			sphere_as_mesh_socket.description = "Use Eevee or Cycles compatible atoms."
			
			#Socket Sphere Radii
			sphere_radii_socket = style_spheres.interface.new_socket(name = "Sphere Radii", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = sphere_panel)
			sphere_radii_socket.subtype = 'NONE'
			sphere_radii_socket.default_value = 0.800000011920929
			sphere_radii_socket.min_value = 0.0
			sphere_radii_socket.max_value = 2.0
			sphere_radii_socket.attribute_domain = 'POINT'
			sphere_radii_socket.description = "Scale the `vdw_radii` of the atoms."
			
			#Socket Sphere Subdivisions
			sphere_subdivisions_socket = style_spheres.interface.new_socket(name = "Sphere Subdivisions", in_out='INPUT', socket_type = 'NodeSocketInt', parent = sphere_panel)
			sphere_subdivisions_socket.subtype = 'NONE'
			sphere_subdivisions_socket.default_value = 2
			sphere_subdivisions_socket.min_value = 0
			sphere_subdivisions_socket.max_value = 5
			sphere_subdivisions_socket.attribute_domain = 'POINT'
			sphere_subdivisions_socket.description = "Subdivisions for Eevee compatible atoms."
			
			
			#Panel Material
			material_panel_1 = style_spheres.interface.new_panel("Material", default_closed=True)
			#Socket Shade Smooth
			shade_smooth_socket_3 = style_spheres.interface.new_socket(name = "Shade Smooth", in_out='INPUT', socket_type = 'NodeSocketBool', parent = material_panel_1)
			shade_smooth_socket_3.attribute_domain = 'POINT'
			shade_smooth_socket_3.description = "Apply smooth shading to the created geometry"
			
			#Socket Material
			material_socket_4 = style_spheres.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial', parent = material_panel_1)
			material_socket_4.attribute_domain = 'POINT'
			material_socket_4.description = "Material to apply to the resulting geometry"
			
			
			
			#initialize style_spheres nodes
			#node Group Input
			group_input_15 = style_spheres.nodes.new("NodeGroupInput")
			group_input_15.name = "Group Input"
			
			#node Group Output
			group_output_15 = style_spheres.nodes.new("NodeGroupOutput")
			group_output_15.name = "Group Output"
			group_output_15.is_active_output = True
			
			#node Join Geometry
			join_geometry_1 = style_spheres.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_1.name = "Join Geometry"
			
			#node Separate Geometry
			separate_geometry_2 = style_spheres.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_2.name = "Separate Geometry"
			separate_geometry_2.domain = 'POINT'
			
			#node Group.014
			group_014 = style_spheres.nodes.new("GeometryNodeGroup")
			group_014.name = "Group.014"
			group_014.node_tree = _mn_utils_style_spheres_points
			
			#node Group.026
			group_026 = style_spheres.nodes.new("GeometryNodeGroup")
			group_026.name = "Group.026"
			group_026.node_tree = _mn_utils_style_spheres_icosphere
			
			#node Realize Instances
			realize_instances = style_spheres.nodes.new("GeometryNodeRealizeInstances")
			realize_instances.name = "Realize Instances"
			#Selection
			realize_instances.inputs[1].default_value = True
			#Realize All
			realize_instances.inputs[2].default_value = True
			#Depth
			realize_instances.inputs[3].default_value = 0
			
			
			
			
			#Set locations
			group_input_15.location = (-679.2061157226562, -54.561466217041016)
			group_output_15.location = (480.0, 40.0)
			join_geometry_1.location = (320.0, 40.0)
			separate_geometry_2.location = (-420.0, 80.0)
			group_014.location = (-200.0, -200.0)
			group_026.location = (-200.0, 60.0)
			realize_instances.location = (100.0, 60.0)
			
			#Set dimensions
			group_input_15.width, group_input_15.height = 140.0, 100.0
			group_output_15.width, group_output_15.height = 140.0, 100.0
			join_geometry_1.width, join_geometry_1.height = 140.0, 100.0
			separate_geometry_2.width, separate_geometry_2.height = 140.0, 100.0
			group_014.width, group_014.height = 277.9979248046875, 100.0
			group_026.width, group_026.height = 278.0207824707031, 100.0
			realize_instances.width, realize_instances.height = 140.0, 100.0
			
			#initialize style_spheres links
			#group_input_15.Atoms -> separate_geometry_2.Geometry
			style_spheres.links.new(group_input_15.outputs[0], separate_geometry_2.inputs[0])
			#group_input_15.Selection -> group_014.Selection
			style_spheres.links.new(group_input_15.outputs[1], group_014.inputs[1])
			#group_input_15.Selection -> group_026.Selection
			style_spheres.links.new(group_input_15.outputs[1], group_026.inputs[1])
			#group_input_15.Sphere As Mesh -> separate_geometry_2.Selection
			style_spheres.links.new(group_input_15.outputs[2], separate_geometry_2.inputs[1])
			#group_input_15.Sphere Radii -> group_014.Radii
			style_spheres.links.new(group_input_15.outputs[3], group_014.inputs[2])
			#group_input_15.Sphere Radii -> group_026.Radii
			style_spheres.links.new(group_input_15.outputs[3], group_026.inputs[2])
			#group_input_15.Sphere Subdivisions -> group_026.Subdivisions
			style_spheres.links.new(group_input_15.outputs[4], group_026.inputs[3])
			#group_input_15.Shade Smooth -> group_026.Shade Smooth
			style_spheres.links.new(group_input_15.outputs[5], group_026.inputs[4])
			#group_input_15.Material -> group_014.Material
			style_spheres.links.new(group_input_15.outputs[6], group_014.inputs[3])
			#group_input_15.Material -> group_026.Material
			style_spheres.links.new(group_input_15.outputs[6], group_026.inputs[5])
			#join_geometry_1.Geometry -> group_output_15.Geometry
			style_spheres.links.new(join_geometry_1.outputs[0], group_output_15.inputs[0])
			#realize_instances.Geometry -> join_geometry_1.Geometry
			style_spheres.links.new(realize_instances.outputs[0], join_geometry_1.inputs[0])
			#group_026.Instances -> realize_instances.Geometry
			style_spheres.links.new(group_026.outputs[0], realize_instances.inputs[0])
			#separate_geometry_2.Inverted -> group_014.Atoms
			style_spheres.links.new(separate_geometry_2.outputs[1], group_014.inputs[0])
			#separate_geometry_2.Selection -> group_026.Atoms
			style_spheres.links.new(separate_geometry_2.outputs[0], group_026.inputs[0])
			#group_014.Point Cloud -> join_geometry_1.Geometry
			style_spheres.links.new(group_014.outputs[0], join_geometry_1.inputs[0])
			return style_spheres

		style_spheres = style_spheres_node_group()

		#initialize is_peptide node group
		def is_peptide_node_group():
			is_peptide = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Is Peptide")

			is_peptide.color_tag = 'INPUT'
			is_peptide.description = ""

			
			#is_peptide interface
			#Socket Selection
			selection_socket_6 = is_peptide.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket_6.attribute_domain = 'POINT'
			selection_socket_6.description = "True if atoms are part of a peptide"
			
			#Socket Inverted
			inverted_socket_1 = is_peptide.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket_1.attribute_domain = 'POINT'
			
			#Socket And
			and_socket_1 = is_peptide.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket_1.attribute_domain = 'POINT'
			and_socket_1.hide_value = True
			
			#Socket Or
			or_socket_1 = is_peptide.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket_1.attribute_domain = 'POINT'
			or_socket_1.hide_value = True
			
			
			#initialize is_peptide nodes
			#node Group Input
			group_input_16 = is_peptide.nodes.new("NodeGroupInput")
			group_input_16.name = "Group Input"
			
			#node Boolean Math.001
			boolean_math_001_2 = is_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_2.name = "Boolean Math.001"
			boolean_math_001_2.operation = 'AND'
			
			#node Group
			group_4 = is_peptide.nodes.new("GeometryNodeGroup")
			group_4.name = "Group"
			group_4.node_tree = _mn_select_peptide
			
			#node Group Output
			group_output_16 = is_peptide.nodes.new("NodeGroupOutput")
			group_output_16.name = "Group Output"
			group_output_16.is_active_output = True
			
			#node Group.001
			group_001_1 = is_peptide.nodes.new("GeometryNodeGroup")
			group_001_1.name = "Group.001"
			group_001_1.node_tree = fallback_boolean
			#Socket_2
			group_001_1.inputs[0].default_value = "is_peptide"
			
			#node Boolean Math.002
			boolean_math_002_2 = is_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_2.name = "Boolean Math.002"
			boolean_math_002_2.operation = 'OR'
			
			#node Boolean Math
			boolean_math_4 = is_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math_4.name = "Boolean Math"
			boolean_math_4.operation = 'NOT'
			
			
			
			
			#Set locations
			group_input_16.location = (-200.0, 0.0)
			boolean_math_001_2.location = (-40.0, 0.0)
			group_4.location = (-340.0, -140.0)
			group_output_16.location = (320.0, 0.0)
			group_001_1.location = (-40.0, -140.0)
			boolean_math_002_2.location = (140.0, 5.243539333343506)
			boolean_math_4.location = (140.0, -120.0)
			
			#Set dimensions
			group_input_16.width, group_input_16.height = 140.0, 100.0
			boolean_math_001_2.width, boolean_math_001_2.height = 140.0, 100.0
			group_4.width, group_4.height = 247.90924072265625, 100.0
			group_output_16.width, group_output_16.height = 140.0, 100.0
			group_001_1.width, group_001_1.height = 140.0, 100.0
			boolean_math_002_2.width, boolean_math_002_2.height = 140.0, 100.0
			boolean_math_4.width, boolean_math_4.height = 140.0, 100.0
			
			#initialize is_peptide links
			#boolean_math_002_2.Boolean -> group_output_16.Selection
			is_peptide.links.new(boolean_math_002_2.outputs[0], group_output_16.inputs[0])
			#group_input_16.And -> boolean_math_001_2.Boolean
			is_peptide.links.new(group_input_16.outputs[0], boolean_math_001_2.inputs[0])
			#group_4.Is Peptide -> group_001_1.Fallback
			is_peptide.links.new(group_4.outputs[2], group_001_1.inputs[1])
			#group_001_1.Boolean -> boolean_math_001_2.Boolean
			is_peptide.links.new(group_001_1.outputs[0], boolean_math_001_2.inputs[1])
			#boolean_math_001_2.Boolean -> boolean_math_002_2.Boolean
			is_peptide.links.new(boolean_math_001_2.outputs[0], boolean_math_002_2.inputs[0])
			#group_input_16.Or -> boolean_math_002_2.Boolean
			is_peptide.links.new(group_input_16.outputs[1], boolean_math_002_2.inputs[1])
			#boolean_math_002_2.Boolean -> boolean_math_4.Boolean
			is_peptide.links.new(boolean_math_002_2.outputs[0], boolean_math_4.inputs[0])
			#boolean_math_4.Boolean -> group_output_16.Inverted
			is_peptide.links.new(boolean_math_4.outputs[0], group_output_16.inputs[1])
			return is_peptide

		is_peptide = is_peptide_node_group()

		#initialize style_preset_3 node group
		def style_preset_3_node_group():
			style_preset_3 = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Style Preset 3")

			style_preset_3.color_tag = 'GEOMETRY'
			style_preset_3.description = ""

			
			#style_preset_3 interface
			#Socket Geometry
			geometry_socket_6 = style_preset_3.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_6.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket_6 = style_preset_3.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_6.attribute_domain = 'POINT'
			
			#Socket Selection
			selection_socket_7 = style_preset_3.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_7.attribute_domain = 'POINT'
			selection_socket_7.hide_value = True
			
			#Socket Quality
			quality_socket_2 = style_preset_3.interface.new_socket(name = "Quality", in_out='INPUT', socket_type = 'NodeSocketInt')
			quality_socket_2.subtype = 'NONE'
			quality_socket_2.default_value = 3
			quality_socket_2.min_value = 0
			quality_socket_2.max_value = 6
			quality_socket_2.attribute_domain = 'POINT'
			
			#Socket Shade Smooth
			shade_smooth_socket_4 = style_preset_3.interface.new_socket(name = "Shade Smooth", in_out='INPUT', socket_type = 'NodeSocketBool')
			shade_smooth_socket_4.attribute_domain = 'POINT'
			
			#Socket Material
			material_socket_5 = style_preset_3.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial')
			material_socket_5.attribute_domain = 'POINT'
			
			
			#initialize style_preset_3 nodes
			#node Group Output
			group_output_17 = style_preset_3.nodes.new("NodeGroupOutput")
			group_output_17.name = "Group Output"
			group_output_17.is_active_output = True
			
			#node Group Input
			group_input_17 = style_preset_3.nodes.new("NodeGroupInput")
			group_input_17.name = "Group Input"
			
			#node Join Geometry.004
			join_geometry_004 = style_preset_3.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_004.name = "Join Geometry.004"
			
			#node Separate Geometry.004
			separate_geometry_004 = style_preset_3.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_004.name = "Separate Geometry.004"
			separate_geometry_004.domain = 'POINT'
			
			#node MN_style_surface
			mn_style_surface = style_preset_3.nodes.new("GeometryNodeGroup")
			mn_style_surface.label = "Style Surface"
			mn_style_surface.name = "MN_style_surface"
			mn_style_surface.node_tree = style_surface
			#Socket_12
			mn_style_surface.inputs[3].default_value = True
			#Socket_15
			mn_style_surface.inputs[4].default_value = "chain_id"
			#Socket_5
			mn_style_surface.inputs[5].default_value = 1.5
			#Socket_6
			mn_style_surface.inputs[6].default_value = 1.0
			#Socket_18
			mn_style_surface.inputs[7].default_value = True
			#Socket_17
			mn_style_surface.inputs[8].default_value = 10
			#Socket_8
			mn_style_surface.inputs[9].default_value = True
			#Socket_9
			mn_style_surface.inputs[10].default_value = 2
			
			#node Group.004
			group_004_1 = style_preset_3.nodes.new("GeometryNodeGroup")
			group_004_1.label = "Atoms"
			group_004_1.name = "Group.004"
			group_004_1.node_tree = style_spheres
			#Input_2
			group_004_1.inputs[2].default_value = False
			#Input_3
			group_004_1.inputs[3].default_value = 0.5
			
			#node Group.014
			group_014_1 = style_preset_3.nodes.new("GeometryNodeGroup")
			group_014_1.name = "Group.014"
			group_014_1.node_tree = is_peptide
			#Socket_1
			group_014_1.inputs[0].default_value = True
			#Socket_3
			group_014_1.inputs[1].default_value = False
			
			
			
			
			#Set locations
			group_output_17.location = (708.8781127929688, 0.0)
			group_input_17.location = (-688.6596069335938, 0.0)
			join_geometry_004.location = (488.65960693359375, 37.614501953125)
			separate_geometry_004.location = (-215.12188720703125, 176.895751953125)
			mn_style_surface.location = (80.0, 260.0)
			group_004_1.location = (80.0, -240.0)
			group_014_1.location = (-220.0, 20.0)
			
			#Set dimensions
			group_output_17.width, group_output_17.height = 140.0, 100.0
			group_input_17.width, group_input_17.height = 140.0, 100.0
			join_geometry_004.width, join_geometry_004.height = 140.0, 100.0
			separate_geometry_004.width, separate_geometry_004.height = 140.0, 100.0
			mn_style_surface.width, mn_style_surface.height = 200.0, 100.0
			group_004_1.width, group_004_1.height = 200.0, 100.0
			group_014_1.width, group_014_1.height = 140.0, 100.0
			
			#initialize style_preset_3 links
			#group_004_1.Geometry -> join_geometry_004.Geometry
			style_preset_3.links.new(group_004_1.outputs[0], join_geometry_004.inputs[0])
			#group_input_17.Material -> group_004_1.Material
			style_preset_3.links.new(group_input_17.outputs[4], group_004_1.inputs[6])
			#separate_geometry_004.Selection -> mn_style_surface.Atoms
			style_preset_3.links.new(separate_geometry_004.outputs[0], mn_style_surface.inputs[0])
			#group_input_17.Shade Smooth -> group_004_1.Shade Smooth
			style_preset_3.links.new(group_input_17.outputs[3], group_004_1.inputs[5])
			#separate_geometry_004.Inverted -> group_004_1.Atoms
			style_preset_3.links.new(separate_geometry_004.outputs[1], group_004_1.inputs[0])
			#group_input_17.Quality -> group_004_1.Sphere Subdivisions
			style_preset_3.links.new(group_input_17.outputs[2], group_004_1.inputs[4])
			#group_input_17.Quality -> mn_style_surface.Quality
			style_preset_3.links.new(group_input_17.outputs[2], mn_style_surface.inputs[2])
			#group_014_1.Selection -> separate_geometry_004.Selection
			style_preset_3.links.new(group_014_1.outputs[0], separate_geometry_004.inputs[1])
			#group_input_17.Material -> mn_style_surface.Material
			style_preset_3.links.new(group_input_17.outputs[4], mn_style_surface.inputs[12])
			#group_input_17.Atoms -> separate_geometry_004.Geometry
			style_preset_3.links.new(group_input_17.outputs[0], separate_geometry_004.inputs[0])
			#group_input_17.Shade Smooth -> mn_style_surface.Shade Smooth
			style_preset_3.links.new(group_input_17.outputs[3], mn_style_surface.inputs[11])
			#join_geometry_004.Geometry -> group_output_17.Geometry
			style_preset_3.links.new(join_geometry_004.outputs[0], group_output_17.inputs[0])
			#group_input_17.Selection -> mn_style_surface.Selection
			style_preset_3.links.new(group_input_17.outputs[1], mn_style_surface.inputs[1])
			#group_input_17.Selection -> group_004_1.Selection
			style_preset_3.links.new(group_input_17.outputs[1], group_004_1.inputs[1])
			#mn_style_surface.Geometry -> join_geometry_004.Geometry
			style_preset_3.links.new(mn_style_surface.outputs[0], join_geometry_004.inputs[0])
			return style_preset_3

		style_preset_3 = style_preset_3_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Style Preset 3", type = 'NODES')
		mod.node_group = style_preset_3
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Style_Preset_3.bl_idname)
			
def register():
	bpy.utils.register_class(Style_Preset_3)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Style_Preset_3)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
