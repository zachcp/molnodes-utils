bl_info = {
	"name" : ".MN_utils_style_old_ball_and_stick",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _MN_utils_style_old_ball_and_stick(bpy.types.Operator):
	bl_idname = "node._mn_utils_style_old_ball_and_stick"
	bl_label = ".MN_utils_style_old_ball_and_stick"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize topology_find_bonds node group
		def topology_find_bonds_node_group():
			topology_find_bonds = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Topology Find Bonds")

			topology_find_bonds.color_tag = 'GEOMETRY'
			topology_find_bonds.description = ""

			topology_find_bonds.is_modifier = True
			
			#topology_find_bonds interface
			#Socket Atoms
			atoms_socket = topology_find_bonds.interface.new_socket(name = "Atoms", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket_1 = topology_find_bonds.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_1.attribute_domain = 'POINT'
			atoms_socket_1.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket = topology_find_bonds.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket.attribute_domain = 'POINT'
			selection_socket.hide_value = True
			selection_socket.description = "Selection of atoms to apply this node to"
			
			#Socket Scale
			scale_socket = topology_find_bonds.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
			scale_socket.subtype = 'NONE'
			scale_socket.default_value = 1.0
			scale_socket.min_value = 0.0
			scale_socket.max_value = 10000.0
			scale_socket.attribute_domain = 'POINT'
			scale_socket.description = "Scale the VDW radii of the atoms when searching for bonds"
			
			
			#initialize topology_find_bonds nodes
			#node Frame
			frame = topology_find_bonds.nodes.new("NodeFrame")
			frame.label = "Create Distance Probe"
			frame.name = "Frame"
			frame.label_size = 20
			frame.shrink = True
			
			#node Sample Nearest
			sample_nearest = topology_find_bonds.nodes.new("GeometryNodeSampleNearest")
			sample_nearest.name = "Sample Nearest"
			sample_nearest.domain = 'POINT'
			#Sample Position
			sample_nearest.inputs[1].default_value = (0.0, 0.0, 0.0)
			
			#node Sample Index.001
			sample_index_001 = topology_find_bonds.nodes.new("GeometryNodeSampleIndex")
			sample_index_001.name = "Sample Index.001"
			sample_index_001.clamp = False
			sample_index_001.data_type = 'FLOAT_VECTOR'
			sample_index_001.domain = 'POINT'
			
			#node Math
			math = topology_find_bonds.nodes.new("ShaderNodeMath")
			math.name = "Math"
			math.hide = True
			math.operation = 'MULTIPLY'
			math.use_clamp = False
			math.inputs[2].hide = True
			
			#node Group Input.001
			group_input_001 = topology_find_bonds.nodes.new("NodeGroupInput")
			group_input_001.name = "Group Input.001"
			group_input_001.outputs[0].hide = True
			group_input_001.outputs[1].hide = True
			group_input_001.outputs[3].hide = True
			
			#node Sample Index
			sample_index = topology_find_bonds.nodes.new("GeometryNodeSampleIndex")
			sample_index.name = "Sample Index"
			sample_index.clamp = False
			sample_index.data_type = 'FLOAT_VECTOR'
			sample_index.domain = 'POINT'
			
			#node Vector Math
			vector_math = topology_find_bonds.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.operation = 'SCALE'
			#Scale
			vector_math.inputs[3].default_value = -1.0
			
			#node Position
			position = topology_find_bonds.nodes.new("GeometryNodeInputPosition")
			position.name = "Position"
			
			#node Ico Sphere
			ico_sphere = topology_find_bonds.nodes.new("GeometryNodeMeshIcoSphere")
			ico_sphere.name = "Ico Sphere"
			#Radius
			ico_sphere.inputs[0].default_value = 1.0
			#Subdivisions
			ico_sphere.inputs[1].default_value = 1
			
			#node Index
			index = topology_find_bonds.nodes.new("GeometryNodeInputIndex")
			index.name = "Index"
			
			#node Mesh Line
			mesh_line = topology_find_bonds.nodes.new("GeometryNodeMeshLine")
			mesh_line.name = "Mesh Line"
			mesh_line.hide = True
			mesh_line.count_mode = 'TOTAL'
			mesh_line.mode = 'OFFSET'
			#Count
			mesh_line.inputs[0].default_value = 2
			#Start Location
			mesh_line.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Offset
			mesh_line.inputs[3].default_value = (0.0, 0.0, 1.0)
			
			#node Instance on Points
			instance_on_points = topology_find_bonds.nodes.new("GeometryNodeInstanceOnPoints")
			instance_on_points.name = "Instance on Points"
			#Selection
			instance_on_points.inputs[1].default_value = True
			#Pick Instance
			instance_on_points.inputs[3].default_value = False
			#Instance Index
			instance_on_points.inputs[4].default_value = 0
			#Scale
			instance_on_points.inputs[6].default_value = (1.0, 1.0, 1.0)
			
			#node Named Attribute
			named_attribute = topology_find_bonds.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'INT'
			#Name
			named_attribute.inputs[0].default_value = "atomic_number"
			
			#node Sample Index.006
			sample_index_006 = topology_find_bonds.nodes.new("GeometryNodeSampleIndex")
			sample_index_006.name = "Sample Index.006"
			sample_index_006.clamp = False
			sample_index_006.data_type = 'INT'
			sample_index_006.domain = 'POINT'
			
			#node Named Attribute.002
			named_attribute_002 = topology_find_bonds.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002.name = "Named Attribute.002"
			named_attribute_002.data_type = 'INT'
			#Name
			named_attribute_002.inputs[0].default_value = "res_name"
			
			#node Sample Index.007
			sample_index_007 = topology_find_bonds.nodes.new("GeometryNodeSampleIndex")
			sample_index_007.name = "Sample Index.007"
			sample_index_007.clamp = False
			sample_index_007.data_type = 'INT'
			sample_index_007.domain = 'POINT'
			
			#node Named Attribute.003
			named_attribute_003 = topology_find_bonds.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_003.name = "Named Attribute.003"
			named_attribute_003.data_type = 'INT'
			#Name
			named_attribute_003.inputs[0].default_value = "chain_id"
			
			#node Sample Index.008
			sample_index_008 = topology_find_bonds.nodes.new("GeometryNodeSampleIndex")
			sample_index_008.name = "Sample Index.008"
			sample_index_008.clamp = False
			sample_index_008.data_type = 'INT'
			sample_index_008.domain = 'POINT'
			
			#node Named Attribute.004
			named_attribute_004 = topology_find_bonds.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_004.name = "Named Attribute.004"
			named_attribute_004.data_type = 'INT'
			#Name
			named_attribute_004.inputs[0].default_value = "res_id"
			
			#node Sample Index.005
			sample_index_005 = topology_find_bonds.nodes.new("GeometryNodeSampleIndex")
			sample_index_005.name = "Sample Index.005"
			sample_index_005.clamp = False
			sample_index_005.data_type = 'INT'
			sample_index_005.domain = 'POINT'
			
			#node Reroute.002
			reroute_002 = topology_find_bonds.nodes.new("NodeReroute")
			reroute_002.name = "Reroute.002"
			#node Sample Index.009
			sample_index_009 = topology_find_bonds.nodes.new("GeometryNodeSampleIndex")
			sample_index_009.name = "Sample Index.009"
			sample_index_009.clamp = False
			sample_index_009.data_type = 'FLOAT'
			sample_index_009.domain = 'POINT'
			
			#node Named Attribute.005
			named_attribute_005 = topology_find_bonds.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_005.name = "Named Attribute.005"
			named_attribute_005.data_type = 'FLOAT'
			#Name
			named_attribute_005.inputs[0].default_value = "vdw_radii"
			
			#node Realize Instances
			realize_instances = topology_find_bonds.nodes.new("GeometryNodeRealizeInstances")
			realize_instances.name = "Realize Instances"
			#Selection
			realize_instances.inputs[1].default_value = True
			#Realize All
			realize_instances.inputs[2].default_value = True
			#Depth
			realize_instances.inputs[3].default_value = 0
			
			#node Instance on Points.001
			instance_on_points_001 = topology_find_bonds.nodes.new("GeometryNodeInstanceOnPoints")
			instance_on_points_001.name = "Instance on Points.001"
			#Selection
			instance_on_points_001.inputs[1].default_value = True
			#Pick Instance
			instance_on_points_001.inputs[3].default_value = False
			#Instance Index
			instance_on_points_001.inputs[4].default_value = 0
			#Rotation
			instance_on_points_001.inputs[5].default_value = (0.0, 0.0, 0.0)
			
			#node Realize Instances.001
			realize_instances_001 = topology_find_bonds.nodes.new("GeometryNodeRealizeInstances")
			realize_instances_001.name = "Realize Instances.001"
			#Selection
			realize_instances_001.inputs[1].default_value = True
			#Realize All
			realize_instances_001.inputs[2].default_value = True
			#Depth
			realize_instances_001.inputs[3].default_value = 0
			
			#node Set Position
			set_position = topology_find_bonds.nodes.new("GeometryNodeSetPosition")
			set_position.name = "Set Position"
			#Selection
			set_position.inputs[1].default_value = True
			#Offset
			set_position.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Position.001
			position_001 = topology_find_bonds.nodes.new("GeometryNodeInputPosition")
			position_001.name = "Position.001"
			
			#node Store Named Attribute.001
			store_named_attribute_001 = topology_find_bonds.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_001.name = "Store Named Attribute.001"
			store_named_attribute_001.data_type = 'INT'
			store_named_attribute_001.domain = 'POINT'
			#Selection
			store_named_attribute_001.inputs[1].default_value = True
			#Name
			store_named_attribute_001.inputs[2].default_value = "res_name"
			
			#node Store Named Attribute.002
			store_named_attribute_002 = topology_find_bonds.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_002.name = "Store Named Attribute.002"
			store_named_attribute_002.data_type = 'INT'
			store_named_attribute_002.domain = 'POINT'
			#Selection
			store_named_attribute_002.inputs[1].default_value = True
			#Name
			store_named_attribute_002.inputs[2].default_value = "chain_id"
			
			#node Store Named Attribute.003
			store_named_attribute_003 = topology_find_bonds.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_003.name = "Store Named Attribute.003"
			store_named_attribute_003.data_type = 'INT'
			store_named_attribute_003.domain = 'POINT'
			#Selection
			store_named_attribute_003.inputs[1].default_value = True
			#Name
			store_named_attribute_003.inputs[2].default_value = "res_id"
			
			#node Store Named Attribute
			store_named_attribute = topology_find_bonds.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute.name = "Store Named Attribute"
			store_named_attribute.data_type = 'INT'
			store_named_attribute.domain = 'POINT'
			#Selection
			store_named_attribute.inputs[1].default_value = True
			#Name
			store_named_attribute.inputs[2].default_value = "atomic_number"
			
			#node Index.002
			index_002 = topology_find_bonds.nodes.new("GeometryNodeInputIndex")
			index_002.name = "Index.002"
			
			#node Named Attribute.006
			named_attribute_006 = topology_find_bonds.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_006.name = "Named Attribute.006"
			named_attribute_006.data_type = 'INT'
			#Name
			named_attribute_006.inputs[0].default_value = "pre_bond_index"
			
			#node Merge by Distance
			merge_by_distance = topology_find_bonds.nodes.new("GeometryNodeMergeByDistance")
			merge_by_distance.name = "Merge by Distance"
			merge_by_distance.mode = 'ALL'
			#Selection
			merge_by_distance.inputs[1].default_value = True
			#Distance
			merge_by_distance.inputs[2].default_value = 0.0010000000474974513
			
			#node Group Output
			group_output = topology_find_bonds.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Sample Index.011
			sample_index_011 = topology_find_bonds.nodes.new("GeometryNodeSampleIndex")
			sample_index_011.name = "Sample Index.011"
			sample_index_011.clamp = False
			sample_index_011.data_type = 'FLOAT_VECTOR'
			sample_index_011.domain = 'POINT'
			
			#node Sample Nearest.001
			sample_nearest_001 = topology_find_bonds.nodes.new("GeometryNodeSampleNearest")
			sample_nearest_001.name = "Sample Nearest.001"
			sample_nearest_001.domain = 'POINT'
			#Sample Position
			sample_nearest_001.inputs[1].default_value = (0.0, 0.0, 0.0)
			
			#node Set Position.002
			set_position_002 = topology_find_bonds.nodes.new("GeometryNodeSetPosition")
			set_position_002.name = "Set Position.002"
			#Selection
			set_position_002.inputs[1].default_value = True
			#Offset
			set_position_002.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Store Named Attribute.004
			store_named_attribute_004 = topology_find_bonds.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_004.name = "Store Named Attribute.004"
			store_named_attribute_004.data_type = 'FLOAT'
			store_named_attribute_004.domain = 'POINT'
			#Selection
			store_named_attribute_004.inputs[1].default_value = True
			#Name
			store_named_attribute_004.inputs[2].default_value = "vdw_radii"
			
			#node Store Named Attribute.006
			store_named_attribute_006 = topology_find_bonds.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_006.name = "Store Named Attribute.006"
			store_named_attribute_006.data_type = 'FLOAT_COLOR'
			store_named_attribute_006.domain = 'POINT'
			#Selection
			store_named_attribute_006.inputs[1].default_value = True
			#Name
			store_named_attribute_006.inputs[2].default_value = "Color"
			
			#node Store Named Attribute.005
			store_named_attribute_005 = topology_find_bonds.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_005.name = "Store Named Attribute.005"
			store_named_attribute_005.data_type = 'INT'
			store_named_attribute_005.domain = 'POINT'
			#Selection
			store_named_attribute_005.inputs[1].default_value = True
			#Name
			store_named_attribute_005.inputs[2].default_value = "pre_bond_index"
			
			#node Sample Index.012
			sample_index_012 = topology_find_bonds.nodes.new("GeometryNodeSampleIndex")
			sample_index_012.name = "Sample Index.012"
			sample_index_012.clamp = False
			sample_index_012.data_type = 'FLOAT_COLOR'
			sample_index_012.domain = 'POINT'
			
			#node Named Attribute.007
			named_attribute_007 = topology_find_bonds.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_007.name = "Named Attribute.007"
			named_attribute_007.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute_007.inputs[0].default_value = "Color"
			
			#node Math.001
			math_001 = topology_find_bonds.nodes.new("ShaderNodeMath")
			math_001.label = "x * 0.62"
			math_001.name = "Math.001"
			math_001.operation = 'MULTIPLY'
			math_001.use_clamp = False
			#Value_001
			math_001.inputs[1].default_value = 0.6200000047683716
			
			#node Group Input
			group_input = topology_find_bonds.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Separate Geometry
			separate_geometry = topology_find_bonds.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry.name = "Separate Geometry"
			separate_geometry.domain = 'POINT'
			
			#node Position.002
			position_002 = topology_find_bonds.nodes.new("GeometryNodeInputPosition")
			position_002.name = "Position.002"
			
			#node Sample Index.010
			sample_index_010 = topology_find_bonds.nodes.new("GeometryNodeSampleIndex")
			sample_index_010.name = "Sample Index.010"
			sample_index_010.clamp = False
			sample_index_010.data_type = 'INT'
			sample_index_010.domain = 'POINT'
			
			#node Sample Index.002
			sample_index_002 = topology_find_bonds.nodes.new("GeometryNodeSampleIndex")
			sample_index_002.name = "Sample Index.002"
			sample_index_002.clamp = False
			sample_index_002.data_type = 'FLOAT'
			sample_index_002.domain = 'POINT'
			
			#node Named Attribute.008
			named_attribute_008 = topology_find_bonds.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_008.label = "vdw_radii"
			named_attribute_008.name = "Named Attribute.008"
			named_attribute_008.hide = True
			named_attribute_008.data_type = 'FLOAT'
			#Name
			named_attribute_008.inputs[0].default_value = "vdw_radii"
			
			#node Index.001
			index_001 = topology_find_bonds.nodes.new("GeometryNodeInputIndex")
			index_001.name = "Index.001"
			
			#node Sample Index.003
			sample_index_003 = topology_find_bonds.nodes.new("GeometryNodeSampleIndex")
			sample_index_003.name = "Sample Index.003"
			sample_index_003.clamp = False
			sample_index_003.data_type = 'FLOAT_VECTOR'
			sample_index_003.domain = 'POINT'
			
			#node Position.003
			position_003 = topology_find_bonds.nodes.new("GeometryNodeInputPosition")
			position_003.name = "Position.003"
			
			#node Reroute.004
			reroute_004 = topology_find_bonds.nodes.new("NodeReroute")
			reroute_004.name = "Reroute.004"
			#node Points
			points = topology_find_bonds.nodes.new("GeometryNodePoints")
			points.name = "Points"
			
			#node Domain Size
			domain_size = topology_find_bonds.nodes.new("GeometryNodeAttributeDomainSize")
			domain_size.name = "Domain Size"
			domain_size.hide = True
			domain_size.component = 'MESH'
			domain_size.outputs[1].hide = True
			domain_size.outputs[2].hide = True
			domain_size.outputs[3].hide = True
			domain_size.outputs[4].hide = True
			domain_size.outputs[5].hide = True
			domain_size.outputs[6].hide = True
			
			#node Axes to Rotation
			axes_to_rotation = topology_find_bonds.nodes.new("FunctionNodeAxesToRotation")
			axes_to_rotation.name = "Axes to Rotation"
			axes_to_rotation.primary_axis = 'Z'
			axes_to_rotation.secondary_axis = 'X'
			#Secondary Axis
			axes_to_rotation.inputs[1].default_value = (1.0, 0.0, 0.0)
			
			#node Merge by Distance.001
			merge_by_distance_001 = topology_find_bonds.nodes.new("GeometryNodeMergeByDistance")
			merge_by_distance_001.name = "Merge by Distance.001"
			merge_by_distance_001.mode = 'ALL'
			#Selection
			merge_by_distance_001.inputs[1].default_value = True
			#Distance
			merge_by_distance_001.inputs[2].default_value = 0.0010000000474974513
			
			#node Index.003
			index_003 = topology_find_bonds.nodes.new("GeometryNodeInputIndex")
			index_003.name = "Index.003"
			
			#node Sort Elements
			sort_elements = topology_find_bonds.nodes.new("GeometryNodeSortElements")
			sort_elements.name = "Sort Elements"
			sort_elements.domain = 'POINT'
			#Selection
			sort_elements.inputs[1].default_value = True
			#Group ID
			sort_elements.inputs[2].default_value = 0
			
			#node Reroute.006
			reroute_006 = topology_find_bonds.nodes.new("NodeReroute")
			reroute_006.name = "Reroute.006"
			#node Capture Attribute
			capture_attribute = topology_find_bonds.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute.name = "Capture Attribute"
			capture_attribute.active_index = 0
			capture_attribute.capture_items.clear()
			capture_attribute.capture_items.new('FLOAT', "Index")
			capture_attribute.capture_items["Index"].data_type = 'INT'
			capture_attribute.domain = 'POINT'
			
			#node Reroute.001
			reroute_001 = topology_find_bonds.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			#node Reroute.003
			reroute_003 = topology_find_bonds.nodes.new("NodeReroute")
			reroute_003.name = "Reroute.003"
			#node Reroute.005
			reroute_005 = topology_find_bonds.nodes.new("NodeReroute")
			reroute_005.name = "Reroute.005"
			#node Reroute.007
			reroute_007 = topology_find_bonds.nodes.new("NodeReroute")
			reroute_007.name = "Reroute.007"
			#node Reroute.008
			reroute_008 = topology_find_bonds.nodes.new("NodeReroute")
			reroute_008.name = "Reroute.008"
			#node Reroute.009
			reroute_009 = topology_find_bonds.nodes.new("NodeReroute")
			reroute_009.name = "Reroute.009"
			#node Reroute.010
			reroute_010 = topology_find_bonds.nodes.new("NodeReroute")
			reroute_010.name = "Reroute.010"
			#node Reroute.011
			reroute_011 = topology_find_bonds.nodes.new("NodeReroute")
			reroute_011.name = "Reroute.011"
			#node Reroute.012
			reroute_012 = topology_find_bonds.nodes.new("NodeReroute")
			reroute_012.name = "Reroute.012"
			#node Reroute.013
			reroute_013 = topology_find_bonds.nodes.new("NodeReroute")
			reroute_013.name = "Reroute.013"
			#node Reroute.014
			reroute_014 = topology_find_bonds.nodes.new("NodeReroute")
			reroute_014.name = "Reroute.014"
			#node Reroute.015
			reroute_015 = topology_find_bonds.nodes.new("NodeReroute")
			reroute_015.name = "Reroute.015"
			#node Reroute.016
			reroute_016 = topology_find_bonds.nodes.new("NodeReroute")
			reroute_016.name = "Reroute.016"
			#node Reroute.017
			reroute_017 = topology_find_bonds.nodes.new("NodeReroute")
			reroute_017.name = "Reroute.017"
			#node Frame.001
			frame_001 = topology_find_bonds.nodes.new("NodeFrame")
			frame_001.label = "Get original index to sample values with"
			frame_001.name = "Frame.001"
			frame_001.label_size = 20
			frame_001.shrink = True
			
			#node Frame.002
			frame_002 = topology_find_bonds.nodes.new("NodeFrame")
			frame_002.label = "Create a clean set of points for instancing on"
			frame_002.name = "Frame.002"
			frame_002.label_size = 20
			frame_002.shrink = True
			
			#node Named Attribute.001
			named_attribute_001 = topology_find_bonds.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.data_type = 'INT'
			#Name
			named_attribute_001.inputs[0].default_value = "pre_bond_index"
			
			#node Remove Named Attribute
			remove_named_attribute = topology_find_bonds.nodes.new("GeometryNodeRemoveAttribute")
			remove_named_attribute.name = "Remove Named Attribute"
			remove_named_attribute.pattern_mode = 'EXACT'
			#Name
			remove_named_attribute.inputs[1].default_value = "pre_bond_index"
			
			#node Reroute
			reroute = topology_find_bonds.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Reroute.018
			reroute_018 = topology_find_bonds.nodes.new("NodeReroute")
			reroute_018.name = "Reroute.018"
			#node Frame.003
			frame_003 = topology_find_bonds.nodes.new("NodeFrame")
			frame_003.label = "Apply the distance probe"
			frame_003.name = "Frame.003"
			frame_003.label_size = 20
			frame_003.shrink = True
			
			#node Domain Size.001
			domain_size_001 = topology_find_bonds.nodes.new("GeometryNodeAttributeDomainSize")
			domain_size_001.name = "Domain Size.001"
			domain_size_001.component = 'MESH'
			domain_size_001.outputs[1].hide = True
			domain_size_001.outputs[2].hide = True
			domain_size_001.outputs[3].hide = True
			domain_size_001.outputs[4].hide = True
			domain_size_001.outputs[5].hide = True
			domain_size_001.outputs[6].hide = True
			
			#node Compare
			compare = topology_find_bonds.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'EQUAL'
			#B_INT
			compare.inputs[3].default_value = 0
			
			#node Switch
			switch = topology_find_bonds.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'GEOMETRY'
			
			#node Reroute.019
			reroute_019 = topology_find_bonds.nodes.new("NodeReroute")
			reroute_019.name = "Reroute.019"
			#node Frame.004
			frame_004 = topology_find_bonds.nodes.new("NodeFrame")
			frame_004.label = "stop warning if nothing selected"
			frame_004.name = "Frame.004"
			frame_004.label_size = 20
			frame_004.shrink = True
			
			#node Frame.005
			frame_005 = topology_find_bonds.nodes.new("NodeFrame")
			frame_005.label = "Sort elements to the same as they previously were"
			frame_005.name = "Frame.005"
			frame_005.label_size = 20
			frame_005.shrink = True
			
			
			
			#Set parents
			sample_nearest.parent = frame_003
			sample_index_001.parent = frame_003
			math.parent = frame_003
			group_input_001.parent = frame_003
			sample_index.parent = frame
			vector_math.parent = frame
			position.parent = frame
			ico_sphere.parent = frame
			index.parent = frame
			mesh_line.parent = frame
			instance_on_points.parent = frame
			realize_instances.parent = frame
			instance_on_points_001.parent = frame_003
			realize_instances_001.parent = frame_003
			set_position.parent = frame_003
			position_001.parent = frame_003
			index_002.parent = frame_001
			merge_by_distance.parent = frame_003
			sample_nearest_001.parent = frame_001
			math_001.parent = frame_003
			sample_index_010.parent = frame_001
			sample_index_002.parent = frame_002
			named_attribute_008.parent = frame_002
			index_001.parent = frame_002
			sample_index_003.parent = frame_002
			position_003.parent = frame_002
			reroute_004.parent = frame_002
			points.parent = frame_002
			domain_size.parent = frame_002
			axes_to_rotation.parent = frame
			merge_by_distance_001.parent = frame
			sort_elements.parent = frame_005
			reroute_006.parent = frame_002
			reroute_017.parent = frame_001
			named_attribute_001.parent = frame_005
			remove_named_attribute.parent = frame_005
			reroute.parent = frame_003
			reroute_018.parent = frame_003
			domain_size_001.parent = frame_004
			compare.parent = frame_004
			switch.parent = frame_004
			
			#Set locations
			frame.location = (50.0, 157.0)
			sample_nearest.location = (420.0, 80.0)
			sample_index_001.location = (420.0, 280.0)
			math.location = (100.0, 220.0)
			group_input_001.location = (100.0, 20.0)
			sample_index.location = (-920.0, -200.0)
			vector_math.location = (-1100.0, -220.0)
			position.location = (-1260.0, -220.0)
			ico_sphere.location = (-1095.594970703125, -40.0)
			index.location = (-1100.0, -360.0)
			mesh_line.location = (-760.0, -100.0)
			instance_on_points.location = (-582.12841796875, -16.803972244262695)
			named_attribute.location = (1180.0, 1160.0)
			sample_index_006.location = (1360.0, 1040.0)
			named_attribute_002.location = (1360.0, 1160.0)
			sample_index_007.location = (1520.0, 1040.0)
			named_attribute_003.location = (1520.0, 1160.0)
			sample_index_008.location = (1680.0, 1040.0)
			named_attribute_004.location = (1680.0, 1160.0)
			sample_index_005.location = (1180.0, 1040.0)
			reroute_002.location = (400.0, 1200.0)
			sample_index_009.location = (1840.0, 1040.0)
			named_attribute_005.location = (1840.0, 1160.0)
			realize_instances.location = (-420.0, -20.0)
			instance_on_points_001.location = (260.0, 440.0)
			realize_instances_001.location = (420.0, 440.0)
			set_position.location = (580.0, 440.0)
			position_001.location = (260.0, 140.0)
			store_named_attribute_001.location = (1360.0, 820.0)
			store_named_attribute_002.location = (1520.0, 820.0)
			store_named_attribute_003.location = (1680.0, 820.0)
			store_named_attribute.location = (1180.0, 820.0)
			index_002.location = (560.0, 800.0)
			named_attribute_006.location = (840.0, 1360.0)
			merge_by_distance.location = (740.0, 440.0)
			group_output.location = (3191.530029296875, 851.8171997070312)
			sample_index_011.location = (2000.0, 1040.0)
			sample_nearest_001.location = (560.0, 740.0)
			set_position_002.location = (2000.0, 820.0)
			store_named_attribute_004.location = (1840.0, 820.0)
			store_named_attribute_006.location = (2160.0, 820.0)
			store_named_attribute_005.location = (1020.0, 820.0)
			sample_index_012.location = (2160.0, 1040.0)
			named_attribute_007.location = (2160.0, 1160.0)
			math_001.location = (100.0, 180.0)
			group_input.location = (-1840.0, 940.0)
			separate_geometry.location = (-1660.0, 940.0)
			position_002.location = (2000.0, 1100.0)
			sample_index_010.location = (740.0, 900.0)
			sample_index_002.location = (-520.0, 460.0)
			named_attribute_008.location = (-760.0, 300.0)
			index_001.location = (-780.0, 260.0)
			sample_index_003.location = (-360.0, 400.0)
			position_003.location = (-520.0, 260.0)
			reroute_004.location = (-580.0, 340.0)
			points.location = (-160.0, 460.0)
			domain_size.location = (-360.0, 460.0)
			axes_to_rotation.location = (-760.0, -200.0)
			merge_by_distance_001.location = (-415.59490966796875, -180.0)
			index_003.location = (-1660.0, 780.0)
			sort_elements.location = (2540.0, 660.0)
			reroute_006.location = (-740.0, 480.0)
			capture_attribute.location = (-1460.0, 940.0)
			reroute_001.location = (1320.0, 1280.0)
			reroute_003.location = (1500.0, 1280.0)
			reroute_005.location = (1660.0, 1280.0)
			reroute_007.location = (1820.0, 1280.0)
			reroute_008.location = (1980.0, 1280.0)
			reroute_009.location = (2140.0, 1260.0)
			reroute_010.location = (1100.0, 1200.0)
			reroute_011.location = (1340.0, 1200.0)
			reroute_012.location = (1520.0, 1200.0)
			reroute_013.location = (1660.0, 1200.0)
			reroute_014.location = (1820.0, 1200.0)
			reroute_015.location = (1980.0, 1200.0)
			reroute_016.location = (2160.0, 1200.0)
			reroute_017.location = (540.0, 780.0)
			frame_001.location = (0.0, 0.0)
			frame_002.location = (-230.0, 92.0)
			named_attribute_001.location = (2540.0, 480.0)
			remove_named_attribute.location = (2700.0, 620.0)
			reroute.location = (380.0, 80.0)
			reroute_018.location = (180.0, 380.0)
			frame_003.location = (0.0, 0.0)
			domain_size_001.location = (2600.0, 860.0)
			compare.location = (2760.0, 860.0)
			switch.location = (2920.0, 860.0)
			reroute_019.location = (2460.0, 780.0)
			frame_004.location = (0.0, 0.0)
			frame_005.location = (30.0, -50.0)
			
			#Set dimensions
			frame.width, frame.height = 1044.0, 463.0
			sample_nearest.width, sample_nearest.height = 140.0, 100.0
			sample_index_001.width, sample_index_001.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			group_input_001.width, group_input_001.height = 140.0, 100.0
			sample_index.width, sample_index.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			position.width, position.height = 140.0, 100.0
			ico_sphere.width, ico_sphere.height = 140.0, 100.0
			index.width, index.height = 140.0, 100.0
			mesh_line.width, mesh_line.height = 140.0, 100.0
			instance_on_points.width, instance_on_points.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			sample_index_006.width, sample_index_006.height = 140.0, 100.0
			named_attribute_002.width, named_attribute_002.height = 140.0, 100.0
			sample_index_007.width, sample_index_007.height = 140.0, 100.0
			named_attribute_003.width, named_attribute_003.height = 140.0, 100.0
			sample_index_008.width, sample_index_008.height = 140.0, 100.0
			named_attribute_004.width, named_attribute_004.height = 140.0, 100.0
			sample_index_005.width, sample_index_005.height = 140.0, 100.0
			reroute_002.width, reroute_002.height = 16.0, 100.0
			sample_index_009.width, sample_index_009.height = 140.0, 100.0
			named_attribute_005.width, named_attribute_005.height = 140.0, 100.0
			realize_instances.width, realize_instances.height = 140.0, 100.0
			instance_on_points_001.width, instance_on_points_001.height = 140.0, 100.0
			realize_instances_001.width, realize_instances_001.height = 140.0, 100.0
			set_position.width, set_position.height = 140.0, 100.0
			position_001.width, position_001.height = 140.0, 100.0
			store_named_attribute_001.width, store_named_attribute_001.height = 140.0, 100.0
			store_named_attribute_002.width, store_named_attribute_002.height = 140.0, 100.0
			store_named_attribute_003.width, store_named_attribute_003.height = 140.0, 100.0
			store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
			index_002.width, index_002.height = 140.0, 100.0
			named_attribute_006.width, named_attribute_006.height = 140.0, 100.0
			merge_by_distance.width, merge_by_distance.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			sample_index_011.width, sample_index_011.height = 140.0, 100.0
			sample_nearest_001.width, sample_nearest_001.height = 140.0, 100.0
			set_position_002.width, set_position_002.height = 140.0, 100.0
			store_named_attribute_004.width, store_named_attribute_004.height = 140.0, 100.0
			store_named_attribute_006.width, store_named_attribute_006.height = 140.0, 100.0
			store_named_attribute_005.width, store_named_attribute_005.height = 140.0, 100.0
			sample_index_012.width, sample_index_012.height = 140.0, 100.0
			named_attribute_007.width, named_attribute_007.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			separate_geometry.width, separate_geometry.height = 140.0, 100.0
			position_002.width, position_002.height = 140.0, 100.0
			sample_index_010.width, sample_index_010.height = 140.0, 100.0
			sample_index_002.width, sample_index_002.height = 140.0, 100.0
			named_attribute_008.width, named_attribute_008.height = 140.0, 100.0
			index_001.width, index_001.height = 140.0, 100.0
			sample_index_003.width, sample_index_003.height = 140.0, 100.0
			position_003.width, position_003.height = 140.0, 100.0
			reroute_004.width, reroute_004.height = 16.0, 100.0
			points.width, points.height = 140.0, 100.0
			domain_size.width, domain_size.height = 140.0, 100.0
			axes_to_rotation.width, axes_to_rotation.height = 140.0, 100.0
			merge_by_distance_001.width, merge_by_distance_001.height = 140.0, 100.0
			index_003.width, index_003.height = 140.0, 100.0
			sort_elements.width, sort_elements.height = 140.0, 100.0
			reroute_006.width, reroute_006.height = 16.0, 100.0
			capture_attribute.width, capture_attribute.height = 140.0, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			reroute_003.width, reroute_003.height = 16.0, 100.0
			reroute_005.width, reroute_005.height = 16.0, 100.0
			reroute_007.width, reroute_007.height = 16.0, 100.0
			reroute_008.width, reroute_008.height = 16.0, 100.0
			reroute_009.width, reroute_009.height = 16.0, 100.0
			reroute_010.width, reroute_010.height = 16.0, 100.0
			reroute_011.width, reroute_011.height = 16.0, 100.0
			reroute_012.width, reroute_012.height = 16.0, 100.0
			reroute_013.width, reroute_013.height = 16.0, 100.0
			reroute_014.width, reroute_014.height = 16.0, 100.0
			reroute_015.width, reroute_015.height = 16.0, 100.0
			reroute_016.width, reroute_016.height = 16.0, 100.0
			reroute_017.width, reroute_017.height = 16.0, 100.0
			frame_001.width, frame_001.height = 408.0, 351.0
			frame_002.width, frame_002.height = 820.0, 351.0
			named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
			remove_named_attribute.width, remove_named_attribute.height = 170.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			reroute_018.width, reroute_018.height = 16.0, 100.0
			frame_003.width, frame_003.height = 840.0, 551.0
			domain_size_001.width, domain_size_001.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			reroute_019.width, reroute_019.height = 16.0, 100.0
			frame_004.width, frame_004.height = 520.0, 218.0
			frame_005.width, frame_005.height = 390.0, 371.0
			
			#initialize topology_find_bonds links
			#ico_sphere.Mesh -> instance_on_points.Points
			topology_find_bonds.links.new(ico_sphere.outputs[0], instance_on_points.inputs[0])
			#mesh_line.Mesh -> instance_on_points.Instance
			topology_find_bonds.links.new(mesh_line.outputs[0], instance_on_points.inputs[2])
			#ico_sphere.Mesh -> sample_index.Geometry
			topology_find_bonds.links.new(ico_sphere.outputs[0], sample_index.inputs[0])
			#index.Index -> sample_index.Index
			topology_find_bonds.links.new(index.outputs[0], sample_index.inputs[2])
			#position.Position -> vector_math.Vector
			topology_find_bonds.links.new(position.outputs[0], vector_math.inputs[0])
			#vector_math.Vector -> sample_index.Value
			topology_find_bonds.links.new(vector_math.outputs[0], sample_index.inputs[1])
			#instance_on_points.Instances -> realize_instances.Geometry
			topology_find_bonds.links.new(instance_on_points.outputs[0], realize_instances.inputs[0])
			#reroute_018.Output -> instance_on_points_001.Points
			topology_find_bonds.links.new(reroute_018.outputs[0], instance_on_points_001.inputs[0])
			#merge_by_distance_001.Geometry -> instance_on_points_001.Instance
			topology_find_bonds.links.new(merge_by_distance_001.outputs[0], instance_on_points_001.inputs[2])
			#instance_on_points_001.Instances -> realize_instances_001.Geometry
			topology_find_bonds.links.new(instance_on_points_001.outputs[0], realize_instances_001.inputs[0])
			#math.Value -> instance_on_points_001.Scale
			topology_find_bonds.links.new(math.outputs[0], instance_on_points_001.inputs[6])
			#realize_instances_001.Geometry -> set_position.Geometry
			topology_find_bonds.links.new(realize_instances_001.outputs[0], set_position.inputs[0])
			#reroute.Output -> sample_index_001.Geometry
			topology_find_bonds.links.new(reroute.outputs[0], sample_index_001.inputs[0])
			#position_001.Position -> sample_index_001.Value
			topology_find_bonds.links.new(position_001.outputs[0], sample_index_001.inputs[1])
			#sample_index_001.Value -> set_position.Position
			topology_find_bonds.links.new(sample_index_001.outputs[0], set_position.inputs[2])
			#reroute.Output -> sample_nearest.Geometry
			topology_find_bonds.links.new(reroute.outputs[0], sample_nearest.inputs[0])
			#sample_nearest.Index -> sample_index_001.Index
			topology_find_bonds.links.new(sample_nearest.outputs[0], sample_index_001.inputs[2])
			#set_position.Geometry -> merge_by_distance.Geometry
			topology_find_bonds.links.new(set_position.outputs[0], merge_by_distance.inputs[0])
			#group_input_001.Scale -> math_001.Value
			topology_find_bonds.links.new(group_input_001.outputs[2], math_001.inputs[0])
			#math_001.Value -> math.Value
			topology_find_bonds.links.new(math_001.outputs[0], math.inputs[1])
			#reroute_017.Output -> sample_nearest_001.Geometry
			topology_find_bonds.links.new(reroute_017.outputs[0], sample_nearest_001.inputs[0])
			#reroute_010.Output -> sample_index_005.Geometry
			topology_find_bonds.links.new(reroute_010.outputs[0], sample_index_005.inputs[0])
			#named_attribute.Attribute -> sample_index_005.Value
			topology_find_bonds.links.new(named_attribute.outputs[0], sample_index_005.inputs[1])
			#sample_index_005.Value -> store_named_attribute.Value
			topology_find_bonds.links.new(sample_index_005.outputs[0], store_named_attribute.inputs[3])
			#capture_attribute.Geometry -> reroute_002.Input
			topology_find_bonds.links.new(capture_attribute.outputs[0], reroute_002.inputs[0])
			#store_named_attribute_005.Geometry -> store_named_attribute.Geometry
			topology_find_bonds.links.new(store_named_attribute_005.outputs[0], store_named_attribute.inputs[0])
			#store_named_attribute.Geometry -> store_named_attribute_001.Geometry
			topology_find_bonds.links.new(store_named_attribute.outputs[0], store_named_attribute_001.inputs[0])
			#reroute_011.Output -> sample_index_006.Geometry
			topology_find_bonds.links.new(reroute_011.outputs[0], sample_index_006.inputs[0])
			#named_attribute_002.Attribute -> sample_index_006.Value
			topology_find_bonds.links.new(named_attribute_002.outputs[0], sample_index_006.inputs[1])
			#sample_index_006.Value -> store_named_attribute_001.Value
			topology_find_bonds.links.new(sample_index_006.outputs[0], store_named_attribute_001.inputs[3])
			#reroute_012.Output -> sample_index_007.Geometry
			topology_find_bonds.links.new(reroute_012.outputs[0], sample_index_007.inputs[0])
			#named_attribute_003.Attribute -> sample_index_007.Value
			topology_find_bonds.links.new(named_attribute_003.outputs[0], sample_index_007.inputs[1])
			#reroute_013.Output -> sample_index_008.Geometry
			topology_find_bonds.links.new(reroute_013.outputs[0], sample_index_008.inputs[0])
			#named_attribute_004.Attribute -> sample_index_008.Value
			topology_find_bonds.links.new(named_attribute_004.outputs[0], sample_index_008.inputs[1])
			#store_named_attribute_001.Geometry -> store_named_attribute_002.Geometry
			topology_find_bonds.links.new(store_named_attribute_001.outputs[0], store_named_attribute_002.inputs[0])
			#sample_index_007.Value -> store_named_attribute_002.Value
			topology_find_bonds.links.new(sample_index_007.outputs[0], store_named_attribute_002.inputs[3])
			#store_named_attribute_002.Geometry -> store_named_attribute_003.Geometry
			topology_find_bonds.links.new(store_named_attribute_002.outputs[0], store_named_attribute_003.inputs[0])
			#sample_index_008.Value -> store_named_attribute_003.Value
			topology_find_bonds.links.new(sample_index_008.outputs[0], store_named_attribute_003.inputs[3])
			#reroute_014.Output -> sample_index_009.Geometry
			topology_find_bonds.links.new(reroute_014.outputs[0], sample_index_009.inputs[0])
			#named_attribute_005.Attribute -> sample_index_009.Value
			topology_find_bonds.links.new(named_attribute_005.outputs[0], sample_index_009.inputs[1])
			#reroute_017.Output -> sample_index_010.Geometry
			topology_find_bonds.links.new(reroute_017.outputs[0], sample_index_010.inputs[0])
			#sample_nearest_001.Index -> sample_index_010.Index
			topology_find_bonds.links.new(sample_nearest_001.outputs[0], sample_index_010.inputs[2])
			#index_002.Index -> sample_index_010.Value
			topology_find_bonds.links.new(index_002.outputs[0], sample_index_010.inputs[1])
			#named_attribute_006.Attribute -> sample_index_005.Index
			topology_find_bonds.links.new(named_attribute_006.outputs[0], sample_index_005.inputs[2])
			#reroute_001.Output -> sample_index_006.Index
			topology_find_bonds.links.new(reroute_001.outputs[0], sample_index_006.inputs[2])
			#reroute_003.Output -> sample_index_007.Index
			topology_find_bonds.links.new(reroute_003.outputs[0], sample_index_007.inputs[2])
			#reroute_005.Output -> sample_index_008.Index
			topology_find_bonds.links.new(reroute_005.outputs[0], sample_index_008.inputs[2])
			#reroute_007.Output -> sample_index_009.Index
			topology_find_bonds.links.new(reroute_007.outputs[0], sample_index_009.inputs[2])
			#store_named_attribute_003.Geometry -> store_named_attribute_004.Geometry
			topology_find_bonds.links.new(store_named_attribute_003.outputs[0], store_named_attribute_004.inputs[0])
			#sample_index_009.Value -> store_named_attribute_004.Value
			topology_find_bonds.links.new(sample_index_009.outputs[0], store_named_attribute_004.inputs[3])
			#store_named_attribute_004.Geometry -> set_position_002.Geometry
			topology_find_bonds.links.new(store_named_attribute_004.outputs[0], set_position_002.inputs[0])
			#reroute_015.Output -> sample_index_011.Geometry
			topology_find_bonds.links.new(reroute_015.outputs[0], sample_index_011.inputs[0])
			#reroute_008.Output -> sample_index_011.Index
			topology_find_bonds.links.new(reroute_008.outputs[0], sample_index_011.inputs[2])
			#position_002.Position -> sample_index_011.Value
			topology_find_bonds.links.new(position_002.outputs[0], sample_index_011.inputs[1])
			#sample_index_011.Value -> set_position_002.Position
			topology_find_bonds.links.new(sample_index_011.outputs[0], set_position_002.inputs[2])
			#merge_by_distance.Geometry -> store_named_attribute_005.Geometry
			topology_find_bonds.links.new(merge_by_distance.outputs[0], store_named_attribute_005.inputs[0])
			#sample_index_010.Value -> store_named_attribute_005.Value
			topology_find_bonds.links.new(sample_index_010.outputs[0], store_named_attribute_005.inputs[3])
			#reroute_009.Output -> sample_index_012.Index
			topology_find_bonds.links.new(reroute_009.outputs[0], sample_index_012.inputs[2])
			#reroute_016.Output -> sample_index_012.Geometry
			topology_find_bonds.links.new(reroute_016.outputs[0], sample_index_012.inputs[0])
			#named_attribute_007.Attribute -> sample_index_012.Value
			topology_find_bonds.links.new(named_attribute_007.outputs[0], sample_index_012.inputs[1])
			#set_position_002.Geometry -> store_named_attribute_006.Geometry
			topology_find_bonds.links.new(set_position_002.outputs[0], store_named_attribute_006.inputs[0])
			#sample_index_012.Value -> store_named_attribute_006.Value
			topology_find_bonds.links.new(sample_index_012.outputs[0], store_named_attribute_006.inputs[3])
			#group_input.Atoms -> separate_geometry.Geometry
			topology_find_bonds.links.new(group_input.outputs[0], separate_geometry.inputs[0])
			#group_input.Selection -> separate_geometry.Selection
			topology_find_bonds.links.new(group_input.outputs[1], separate_geometry.inputs[1])
			#reroute_004.Output -> sample_index_002.Geometry
			topology_find_bonds.links.new(reroute_004.outputs[0], sample_index_002.inputs[0])
			#named_attribute_008.Attribute -> sample_index_002.Value
			topology_find_bonds.links.new(named_attribute_008.outputs[0], sample_index_002.inputs[1])
			#index_001.Index -> sample_index_002.Index
			topology_find_bonds.links.new(index_001.outputs[0], sample_index_002.inputs[2])
			#reroute_004.Output -> sample_index_003.Geometry
			topology_find_bonds.links.new(reroute_004.outputs[0], sample_index_003.inputs[0])
			#index_001.Index -> sample_index_003.Index
			topology_find_bonds.links.new(index_001.outputs[0], sample_index_003.inputs[2])
			#position_003.Position -> sample_index_003.Value
			topology_find_bonds.links.new(position_003.outputs[0], sample_index_003.inputs[1])
			#reroute_006.Output -> reroute_004.Input
			topology_find_bonds.links.new(reroute_006.outputs[0], reroute_004.inputs[0])
			#sample_index_003.Value -> points.Position
			topology_find_bonds.links.new(sample_index_003.outputs[0], points.inputs[1])
			#reroute_006.Output -> domain_size.Geometry
			topology_find_bonds.links.new(reroute_006.outputs[0], domain_size.inputs[0])
			#domain_size.Point Count -> points.Count
			topology_find_bonds.links.new(domain_size.outputs[0], points.inputs[0])
			#sample_index_002.Value -> points.Radius
			topology_find_bonds.links.new(sample_index_002.outputs[0], points.inputs[2])
			#axes_to_rotation.Rotation -> instance_on_points.Rotation
			topology_find_bonds.links.new(axes_to_rotation.outputs[0], instance_on_points.inputs[5])
			#sample_index.Value -> axes_to_rotation.Primary Axis
			topology_find_bonds.links.new(sample_index.outputs[0], axes_to_rotation.inputs[0])
			#realize_instances.Geometry -> merge_by_distance_001.Geometry
			topology_find_bonds.links.new(realize_instances.outputs[0], merge_by_distance_001.inputs[0])
			#sample_index_002.Value -> math.Value
			topology_find_bonds.links.new(sample_index_002.outputs[0], math.inputs[0])
			#separate_geometry.Selection -> capture_attribute.Geometry
			topology_find_bonds.links.new(separate_geometry.outputs[0], capture_attribute.inputs[0])
			#index_003.Index -> capture_attribute.Index
			topology_find_bonds.links.new(index_003.outputs[0], capture_attribute.inputs[1])
			#capture_attribute.Geometry -> reroute_006.Input
			topology_find_bonds.links.new(capture_attribute.outputs[0], reroute_006.inputs[0])
			#named_attribute_006.Attribute -> reroute_001.Input
			topology_find_bonds.links.new(named_attribute_006.outputs[0], reroute_001.inputs[0])
			#reroute_001.Output -> reroute_003.Input
			topology_find_bonds.links.new(reroute_001.outputs[0], reroute_003.inputs[0])
			#reroute_003.Output -> reroute_005.Input
			topology_find_bonds.links.new(reroute_003.outputs[0], reroute_005.inputs[0])
			#reroute_005.Output -> reroute_007.Input
			topology_find_bonds.links.new(reroute_005.outputs[0], reroute_007.inputs[0])
			#reroute_007.Output -> reroute_008.Input
			topology_find_bonds.links.new(reroute_007.outputs[0], reroute_008.inputs[0])
			#reroute_008.Output -> reroute_009.Input
			topology_find_bonds.links.new(reroute_008.outputs[0], reroute_009.inputs[0])
			#reroute_002.Output -> reroute_010.Input
			topology_find_bonds.links.new(reroute_002.outputs[0], reroute_010.inputs[0])
			#reroute_010.Output -> reroute_011.Input
			topology_find_bonds.links.new(reroute_010.outputs[0], reroute_011.inputs[0])
			#reroute_011.Output -> reroute_012.Input
			topology_find_bonds.links.new(reroute_011.outputs[0], reroute_012.inputs[0])
			#reroute_012.Output -> reroute_013.Input
			topology_find_bonds.links.new(reroute_012.outputs[0], reroute_013.inputs[0])
			#reroute_013.Output -> reroute_014.Input
			topology_find_bonds.links.new(reroute_013.outputs[0], reroute_014.inputs[0])
			#reroute_014.Output -> reroute_015.Input
			topology_find_bonds.links.new(reroute_014.outputs[0], reroute_015.inputs[0])
			#reroute_015.Output -> reroute_016.Input
			topology_find_bonds.links.new(reroute_015.outputs[0], reroute_016.inputs[0])
			#reroute_019.Output -> sort_elements.Geometry
			topology_find_bonds.links.new(reroute_019.outputs[0], sort_elements.inputs[0])
			#reroute_002.Output -> reroute_017.Input
			topology_find_bonds.links.new(reroute_002.outputs[0], reroute_017.inputs[0])
			#named_attribute_001.Attribute -> sort_elements.Sort Weight
			topology_find_bonds.links.new(named_attribute_001.outputs[0], sort_elements.inputs[3])
			#sort_elements.Geometry -> remove_named_attribute.Geometry
			topology_find_bonds.links.new(sort_elements.outputs[0], remove_named_attribute.inputs[0])
			#reroute_018.Output -> reroute.Input
			topology_find_bonds.links.new(reroute_018.outputs[0], reroute.inputs[0])
			#points.Points -> reroute_018.Input
			topology_find_bonds.links.new(points.outputs[0], reroute_018.inputs[0])
			#reroute_019.Output -> domain_size_001.Geometry
			topology_find_bonds.links.new(reroute_019.outputs[0], domain_size_001.inputs[0])
			#domain_size_001.Point Count -> compare.A
			topology_find_bonds.links.new(domain_size_001.outputs[0], compare.inputs[2])
			#switch.Output -> group_output.Atoms
			topology_find_bonds.links.new(switch.outputs[0], group_output.inputs[0])
			#remove_named_attribute.Geometry -> switch.False
			topology_find_bonds.links.new(remove_named_attribute.outputs[0], switch.inputs[1])
			#compare.Result -> switch.Switch
			topology_find_bonds.links.new(compare.outputs[0], switch.inputs[0])
			#store_named_attribute_006.Geometry -> reroute_019.Input
			topology_find_bonds.links.new(store_named_attribute_006.outputs[0], reroute_019.inputs[0])
			return topology_find_bonds

		topology_find_bonds = topology_find_bonds_node_group()

		#initialize _mn_utils_style_old_ball_and_stick node group
		def _mn_utils_style_old_ball_and_stick_node_group():
			_mn_utils_style_old_ball_and_stick = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_utils_style_old_ball_and_stick")

			_mn_utils_style_old_ball_and_stick.color_tag = 'GEOMETRY'
			_mn_utils_style_old_ball_and_stick.description = ""

			_mn_utils_style_old_ball_and_stick.is_modifier = True
			
			#_mn_utils_style_old_ball_and_stick interface
			#Socket Ball and Stick Mesh
			ball_and_stick_mesh_socket = _mn_utils_style_old_ball_and_stick.interface.new_socket(name = "Ball and Stick Mesh", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			ball_and_stick_mesh_socket.attribute_domain = 'POINT'
			
			#Socket Sticks Mesh
			sticks_mesh_socket = _mn_utils_style_old_ball_and_stick.interface.new_socket(name = "Sticks Mesh", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			sticks_mesh_socket.attribute_domain = 'POINT'
			
			#Socket Ball Instances
			ball_instances_socket = _mn_utils_style_old_ball_and_stick.interface.new_socket(name = "Ball Instances", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			ball_instances_socket.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket_2 = _mn_utils_style_old_ball_and_stick.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_2.attribute_domain = 'POINT'
			atoms_socket_2.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket_1 = _mn_utils_style_old_ball_and_stick.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_1.attribute_domain = 'POINT'
			selection_socket_1.hide_value = True
			selection_socket_1.description = "Selection of atoms to apply this node to"
			
			#Socket Shade Smooth
			shade_smooth_socket = _mn_utils_style_old_ball_and_stick.interface.new_socket(name = "Shade Smooth", in_out='INPUT', socket_type = 'NodeSocketBool')
			shade_smooth_socket.attribute_domain = 'POINT'
			shade_smooth_socket.description = "Apply smooth shading to the created geometry"
			
			#Socket Ball Resolution
			ball_resolution_socket = _mn_utils_style_old_ball_and_stick.interface.new_socket(name = "Ball Resolution", in_out='INPUT', socket_type = 'NodeSocketInt')
			ball_resolution_socket.subtype = 'NONE'
			ball_resolution_socket.default_value = 2
			ball_resolution_socket.min_value = 1
			ball_resolution_socket.max_value = 7
			ball_resolution_socket.attribute_domain = 'POINT'
			
			#Socket Ball Radius
			ball_radius_socket = _mn_utils_style_old_ball_and_stick.interface.new_socket(name = "Ball Radius", in_out='INPUT', socket_type = 'NodeSocketFloat')
			ball_radius_socket.subtype = 'DISTANCE'
			ball_radius_socket.default_value = 0.30000001192092896
			ball_radius_socket.min_value = 0.0
			ball_radius_socket.max_value = 3.4028234663852886e+38
			ball_radius_socket.attribute_domain = 'POINT'
			
			#Socket Find Bonds
			find_bonds_socket = _mn_utils_style_old_ball_and_stick.interface.new_socket(name = "Find Bonds", in_out='INPUT', socket_type = 'NodeSocketBool')
			find_bonds_socket.attribute_domain = 'POINT'
			
			#Socket Bond Resolution
			bond_resolution_socket = _mn_utils_style_old_ball_and_stick.interface.new_socket(name = "Bond Resolution", in_out='INPUT', socket_type = 'NodeSocketInt')
			bond_resolution_socket.subtype = 'NONE'
			bond_resolution_socket.default_value = 8
			bond_resolution_socket.min_value = 3
			bond_resolution_socket.max_value = 512
			bond_resolution_socket.attribute_domain = 'POINT'
			
			#Socket Bond Radius
			bond_radius_socket = _mn_utils_style_old_ball_and_stick.interface.new_socket(name = "Bond Radius", in_out='INPUT', socket_type = 'NodeSocketFloat')
			bond_radius_socket.subtype = 'NONE'
			bond_radius_socket.default_value = 0.20000000298023224
			bond_radius_socket.min_value = -10000.0
			bond_radius_socket.max_value = 10000.0
			bond_radius_socket.attribute_domain = 'POINT'
			
			#Socket Split Double Bonds
			split_double_bonds_socket = _mn_utils_style_old_ball_and_stick.interface.new_socket(name = "Split Double Bonds", in_out='INPUT', socket_type = 'NodeSocketBool')
			split_double_bonds_socket.attribute_domain = 'POINT'
			
			#Socket Double Bond Curve
			double_bond_curve_socket = _mn_utils_style_old_ball_and_stick.interface.new_socket(name = "Double Bond Curve", in_out='INPUT', socket_type = 'NodeSocketFloat')
			double_bond_curve_socket.subtype = 'NONE'
			double_bond_curve_socket.default_value = 1.0
			double_bond_curve_socket.min_value = -10000.0
			double_bond_curve_socket.max_value = 10000.0
			double_bond_curve_socket.attribute_domain = 'POINT'
			
			#Socket Double Bond Width
			double_bond_width_socket = _mn_utils_style_old_ball_and_stick.interface.new_socket(name = "Double Bond Width", in_out='INPUT', socket_type = 'NodeSocketFloat')
			double_bond_width_socket.subtype = 'NONE'
			double_bond_width_socket.default_value = 1.0
			double_bond_width_socket.min_value = 0.0
			double_bond_width_socket.max_value = 10000.0
			double_bond_width_socket.attribute_domain = 'POINT'
			
			#Socket Double Bond Resolution
			double_bond_resolution_socket = _mn_utils_style_old_ball_and_stick.interface.new_socket(name = "Double Bond Resolution", in_out='INPUT', socket_type = 'NodeSocketInt')
			double_bond_resolution_socket.subtype = 'NONE'
			double_bond_resolution_socket.default_value = 3
			double_bond_resolution_socket.min_value = 1
			double_bond_resolution_socket.max_value = 2147483647
			double_bond_resolution_socket.attribute_domain = 'POINT'
			
			#Socket Double Bond Radius
			double_bond_radius_socket = _mn_utils_style_old_ball_and_stick.interface.new_socket(name = "Double Bond Radius", in_out='INPUT', socket_type = 'NodeSocketFloat')
			double_bond_radius_socket.subtype = 'NONE'
			double_bond_radius_socket.default_value = 0.20000000298023224
			double_bond_radius_socket.min_value = 0.0
			double_bond_radius_socket.max_value = 1.0
			double_bond_radius_socket.attribute_domain = 'POINT'
			
			#Socket Double Bond Rotate
			double_bond_rotate_socket = _mn_utils_style_old_ball_and_stick.interface.new_socket(name = "Double Bond Rotate", in_out='INPUT', socket_type = 'NodeSocketFloat')
			double_bond_rotate_socket.subtype = 'NONE'
			double_bond_rotate_socket.default_value = 0.0
			double_bond_rotate_socket.min_value = -10000.0
			double_bond_rotate_socket.max_value = 10000.0
			double_bond_rotate_socket.attribute_domain = 'POINT'
			
			#Socket Material
			material_socket = _mn_utils_style_old_ball_and_stick.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial')
			material_socket.attribute_domain = 'POINT'
			material_socket.description = "Material to apply to the resulting geometry"
			
			
			#initialize _mn_utils_style_old_ball_and_stick nodes
			#node Frame
			frame_1 = _mn_utils_style_old_ball_and_stick.nodes.new("NodeFrame")
			frame_1.label = "Atoms"
			frame_1.name = "Frame"
			frame_1.label_size = 20
			frame_1.shrink = True
			
			#node Math.003
			math_003 = _mn_utils_style_old_ball_and_stick.nodes.new("ShaderNodeMath")
			math_003.label = "tau / x"
			math_003.name = "Math.003"
			math_003.hide = True
			math_003.operation = 'DIVIDE'
			math_003.use_clamp = False
			#Value
			math_003.inputs[0].default_value = 6.2831854820251465
			
			#node Vector Math.002
			vector_math_002 = _mn_utils_style_old_ball_and_stick.nodes.new("ShaderNodeVectorMath")
			vector_math_002.name = "Vector Math.002"
			vector_math_002.operation = 'SCALE'
			
			#node Vector Math.005
			vector_math_005 = _mn_utils_style_old_ball_and_stick.nodes.new("ShaderNodeVectorMath")
			vector_math_005.name = "Vector Math.005"
			vector_math_005.operation = 'SCALE'
			
			#node Switch
			switch_1 = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeSwitch")
			switch_1.name = "Switch"
			switch_1.input_type = 'INT'
			#False
			switch_1.inputs[1].default_value = 1
			
			#node Curve to Mesh
			curve_to_mesh = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeCurveToMesh")
			curve_to_mesh.name = "Curve to Mesh"
			#Fill Caps
			curve_to_mesh.inputs[2].default_value = False
			
			#node Reroute.003
			reroute_003_1 = _mn_utils_style_old_ball_and_stick.nodes.new("NodeReroute")
			reroute_003_1.name = "Reroute.003"
			#node Named Attribute.002
			named_attribute_002_1 = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002_1.name = "Named Attribute.002"
			named_attribute_002_1.data_type = 'INT'
			#Name
			named_attribute_002_1.inputs[0].default_value = "bond_type"
			
			#node Group Input.004
			group_input_004 = _mn_utils_style_old_ball_and_stick.nodes.new("NodeGroupInput")
			group_input_004.name = "Group Input.004"
			group_input_004.outputs[0].hide = True
			group_input_004.outputs[1].hide = True
			group_input_004.outputs[2].hide = True
			group_input_004.outputs[3].hide = True
			group_input_004.outputs[4].hide = True
			group_input_004.outputs[5].hide = True
			group_input_004.outputs[6].hide = True
			group_input_004.outputs[7].hide = True
			group_input_004.outputs[9].hide = True
			group_input_004.outputs[10].hide = True
			group_input_004.outputs[11].hide = True
			group_input_004.outputs[12].hide = True
			group_input_004.outputs[13].hide = True
			group_input_004.outputs[14].hide = True
			group_input_004.outputs[15].hide = True
			
			#node Switch.002
			switch_002 = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeSwitch")
			switch_002.name = "Switch.002"
			switch_002.input_type = 'INT'
			#False
			switch_002.inputs[1].default_value = 1
			#True
			switch_002.inputs[2].default_value = 3
			
			#node Map Range
			map_range = _mn_utils_style_old_ball_and_stick.nodes.new("ShaderNodeMapRange")
			map_range.name = "Map Range"
			map_range.clamp = False
			map_range.data_type = 'FLOAT'
			map_range.interpolation_type = 'SMOOTHERSTEP'
			#From Min
			map_range.inputs[1].default_value = 0.0
			#From Max
			map_range.inputs[2].default_value = 1.0
			#To Min
			map_range.inputs[3].default_value = 1.0
			#To Max
			map_range.inputs[4].default_value = 2.0
			
			#node Switch.003
			switch_003 = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeSwitch")
			switch_003.name = "Switch.003"
			switch_003.input_type = 'FLOAT'
			#False
			switch_003.inputs[1].default_value = 1.0
			
			#node Compare.003
			compare_003 = _mn_utils_style_old_ball_and_stick.nodes.new("FunctionNodeCompare")
			compare_003.name = "Compare.003"
			compare_003.data_type = 'INT'
			compare_003.mode = 'ELEMENT'
			compare_003.operation = 'GREATER_THAN'
			#B_INT
			compare_003.inputs[3].default_value = 1
			
			#node Group Input.001
			group_input_001_1 = _mn_utils_style_old_ball_and_stick.nodes.new("NodeGroupInput")
			group_input_001_1.name = "Group Input.001"
			group_input_001_1.outputs[0].hide = True
			group_input_001_1.outputs[1].hide = True
			group_input_001_1.outputs[2].hide = True
			group_input_001_1.outputs[3].hide = True
			group_input_001_1.outputs[4].hide = True
			group_input_001_1.outputs[5].hide = True
			group_input_001_1.outputs[6].hide = True
			group_input_001_1.outputs[7].hide = True
			group_input_001_1.outputs[8].hide = True
			group_input_001_1.outputs[10].hide = True
			group_input_001_1.outputs[11].hide = True
			group_input_001_1.outputs[12].hide = True
			group_input_001_1.outputs[13].hide = True
			group_input_001_1.outputs[14].hide = True
			group_input_001_1.outputs[15].hide = True
			
			#node Vector Rotate
			vector_rotate = _mn_utils_style_old_ball_and_stick.nodes.new("ShaderNodeVectorRotate")
			vector_rotate.name = "Vector Rotate"
			vector_rotate.invert = False
			vector_rotate.rotation_type = 'AXIS_ANGLE'
			#Center
			vector_rotate.inputs[1].default_value = (0.0, 0.0, 0.0)
			
			#node Math.002
			math_002 = _mn_utils_style_old_ball_and_stick.nodes.new("ShaderNodeMath")
			math_002.name = "Math.002"
			math_002.operation = 'DIVIDE'
			math_002.use_clamp = False
			#Value_001
			math_002.inputs[1].default_value = 500.0
			
			#node Group Input.002
			group_input_002 = _mn_utils_style_old_ball_and_stick.nodes.new("NodeGroupInput")
			group_input_002.name = "Group Input.002"
			group_input_002.outputs[0].hide = True
			group_input_002.outputs[1].hide = True
			group_input_002.outputs[2].hide = True
			group_input_002.outputs[3].hide = True
			group_input_002.outputs[4].hide = True
			group_input_002.outputs[5].hide = True
			group_input_002.outputs[6].hide = True
			group_input_002.outputs[7].hide = True
			group_input_002.outputs[8].hide = True
			group_input_002.outputs[9].hide = True
			group_input_002.outputs[11].hide = True
			group_input_002.outputs[12].hide = True
			group_input_002.outputs[14].hide = True
			group_input_002.outputs[15].hide = True
			
			#node Math.001
			math_001_1 = _mn_utils_style_old_ball_and_stick.nodes.new("ShaderNodeMath")
			math_001_1.name = "Math.001"
			math_001_1.operation = 'MULTIPLY'
			math_001_1.use_clamp = False
			
			#node Math.004
			math_004 = _mn_utils_style_old_ball_and_stick.nodes.new("ShaderNodeMath")
			math_004.name = "Math.004"
			math_004.operation = 'ADD'
			math_004.use_clamp = False
			
			#node Duplicate Elements
			duplicate_elements = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeDuplicateElements")
			duplicate_elements.name = "Duplicate Elements"
			duplicate_elements.domain = 'EDGE'
			#Selection
			duplicate_elements.inputs[1].default_value = True
			
			#node Set Shade Smooth.001
			set_shade_smooth_001 = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeSetShadeSmooth")
			set_shade_smooth_001.name = "Set Shade Smooth.001"
			set_shade_smooth_001.domain = 'FACE'
			#Selection
			set_shade_smooth_001.inputs[1].default_value = True
			
			#node Set Material.001
			set_material_001 = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeSetMaterial")
			set_material_001.name = "Set Material.001"
			#Selection
			set_material_001.inputs[1].default_value = True
			
			#node Set Shade Smooth.002
			set_shade_smooth_002 = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeSetShadeSmooth")
			set_shade_smooth_002.name = "Set Shade Smooth.002"
			set_shade_smooth_002.domain = 'FACE'
			#Selection
			set_shade_smooth_002.inputs[1].default_value = True
			
			#node Set Material.002
			set_material_002 = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeSetMaterial")
			set_material_002.name = "Set Material.002"
			#Selection
			set_material_002.inputs[1].default_value = True
			
			#node Group Input.006
			group_input_006 = _mn_utils_style_old_ball_and_stick.nodes.new("NodeGroupInput")
			group_input_006.name = "Group Input.006"
			group_input_006.outputs[0].hide = True
			group_input_006.outputs[1].hide = True
			group_input_006.outputs[3].hide = True
			group_input_006.outputs[4].hide = True
			group_input_006.outputs[5].hide = True
			group_input_006.outputs[6].hide = True
			group_input_006.outputs[7].hide = True
			group_input_006.outputs[8].hide = True
			group_input_006.outputs[9].hide = True
			group_input_006.outputs[10].hide = True
			group_input_006.outputs[11].hide = True
			group_input_006.outputs[12].hide = True
			group_input_006.outputs[13].hide = True
			group_input_006.outputs[15].hide = True
			
			#node Reroute.001
			reroute_001_1 = _mn_utils_style_old_ball_and_stick.nodes.new("NodeReroute")
			reroute_001_1.name = "Reroute.001"
			#node Reroute.002
			reroute_002_1 = _mn_utils_style_old_ball_and_stick.nodes.new("NodeReroute")
			reroute_002_1.name = "Reroute.002"
			#node Join Geometry
			join_geometry = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeJoinGeometry")
			join_geometry.name = "Join Geometry"
			join_geometry.hide = True
			
			#node Group Output
			group_output_1 = _mn_utils_style_old_ball_and_stick.nodes.new("NodeGroupOutput")
			group_output_1.name = "Group Output"
			group_output_1.is_active_output = True
			
			#node Instance on Points
			instance_on_points_1 = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeInstanceOnPoints")
			instance_on_points_1.name = "Instance on Points"
			#Selection
			instance_on_points_1.inputs[1].default_value = True
			#Pick Instance
			instance_on_points_1.inputs[3].default_value = False
			#Instance Index
			instance_on_points_1.inputs[4].default_value = 0
			#Rotation
			instance_on_points_1.inputs[5].default_value = (0.0, 0.0, 0.0)
			
			#node Named Attribute
			named_attribute_1 = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_1.name = "Named Attribute"
			named_attribute_1.data_type = 'FLOAT'
			#Name
			named_attribute_1.inputs[0].default_value = "vdw_radii"
			
			#node Math.005
			math_005 = _mn_utils_style_old_ball_and_stick.nodes.new("ShaderNodeMath")
			math_005.name = "Math.005"
			math_005.operation = 'MULTIPLY'
			math_005.use_clamp = False
			
			#node Store Named Attribute.001
			store_named_attribute_001_1 = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_001_1.name = "Store Named Attribute.001"
			store_named_attribute_001_1.data_type = 'FLOAT_VECTOR'
			store_named_attribute_001_1.domain = 'CORNER'
			#Selection
			store_named_attribute_001_1.inputs[1].default_value = True
			#Name
			store_named_attribute_001_1.inputs[2].default_value = "UVMap"
			
			#node Ico Sphere
			ico_sphere_1 = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeMeshIcoSphere")
			ico_sphere_1.name = "Ico Sphere"
			#Radius
			ico_sphere_1.inputs[0].default_value = 1.0
			
			#node Group Input.007
			group_input_007 = _mn_utils_style_old_ball_and_stick.nodes.new("NodeGroupInput")
			group_input_007.name = "Group Input.007"
			group_input_007.outputs[0].hide = True
			group_input_007.outputs[1].hide = True
			group_input_007.outputs[2].hide = True
			group_input_007.outputs[5].hide = True
			group_input_007.outputs[6].hide = True
			group_input_007.outputs[7].hide = True
			group_input_007.outputs[8].hide = True
			group_input_007.outputs[9].hide = True
			group_input_007.outputs[10].hide = True
			group_input_007.outputs[11].hide = True
			group_input_007.outputs[12].hide = True
			group_input_007.outputs[13].hide = True
			group_input_007.outputs[14].hide = True
			group_input_007.outputs[15].hide = True
			
			#node Reroute.004
			reroute_004_1 = _mn_utils_style_old_ball_and_stick.nodes.new("NodeReroute")
			reroute_004_1.name = "Reroute.004"
			#node Separate Geometry
			separate_geometry_1 = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_1.name = "Separate Geometry"
			separate_geometry_1.domain = 'POINT'
			
			#node Compare.002
			compare_002 = _mn_utils_style_old_ball_and_stick.nodes.new("FunctionNodeCompare")
			compare_002.name = "Compare.002"
			compare_002.data_type = 'INT'
			compare_002.mode = 'ELEMENT'
			compare_002.operation = 'EQUAL'
			#B_INT
			compare_002.inputs[3].default_value = 2
			
			#node Set Position
			set_position_1 = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeSetPosition")
			set_position_1.name = "Set Position"
			#Selection
			set_position_1.inputs[1].default_value = True
			#Position
			set_position_1.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Mesh to Curve.002
			mesh_to_curve_002 = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeMeshToCurve")
			mesh_to_curve_002.name = "Mesh to Curve.002"
			#Selection
			mesh_to_curve_002.inputs[1].default_value = True
			
			#node Set Curve Radius.001
			set_curve_radius_001 = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeSetCurveRadius")
			set_curve_radius_001.name = "Set Curve Radius.001"
			#Selection
			set_curve_radius_001.inputs[1].default_value = True
			
			#node Set Curve Radius.002
			set_curve_radius_002 = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeSetCurveRadius")
			set_curve_radius_002.name = "Set Curve Radius.002"
			#Selection
			set_curve_radius_002.inputs[1].default_value = True
			
			#node Mesh to Curve.001
			mesh_to_curve_001 = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeMeshToCurve")
			mesh_to_curve_001.name = "Mesh to Curve.001"
			#Selection
			mesh_to_curve_001.inputs[1].default_value = True
			
			#node Set Spline Type
			set_spline_type = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeCurveSplineType")
			set_spline_type.name = "Set Spline Type"
			set_spline_type.spline_type = 'CATMULL_ROM'
			#Selection
			set_spline_type.inputs[1].default_value = True
			
			#node Resample Curve.001
			resample_curve_001 = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeResampleCurve")
			resample_curve_001.name = "Resample Curve.001"
			resample_curve_001.mode = 'COUNT'
			#Selection
			resample_curve_001.inputs[1].default_value = True
			
			#node Group Input.011
			group_input_011 = _mn_utils_style_old_ball_and_stick.nodes.new("NodeGroupInput")
			group_input_011.name = "Group Input.011"
			group_input_011.outputs[0].hide = True
			group_input_011.outputs[1].hide = True
			group_input_011.outputs[2].hide = True
			group_input_011.outputs[3].hide = True
			group_input_011.outputs[4].hide = True
			group_input_011.outputs[5].hide = True
			group_input_011.outputs[6].hide = True
			group_input_011.outputs[8].hide = True
			group_input_011.outputs[9].hide = True
			group_input_011.outputs[10].hide = True
			group_input_011.outputs[13].hide = True
			group_input_011.outputs[14].hide = True
			group_input_011.outputs[15].hide = True
			
			#node Math
			math_1 = _mn_utils_style_old_ball_and_stick.nodes.new("ShaderNodeMath")
			math_1.name = "Math"
			math_1.operation = 'MULTIPLY'
			math_1.use_clamp = False
			#Value_001
			math_1.inputs[1].default_value = 2.0
			
			#node Subdivide Mesh
			subdivide_mesh = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeSubdivideMesh")
			subdivide_mesh.name = "Subdivide Mesh"
			#Level
			subdivide_mesh.inputs[1].default_value = 1
			
			#node Vector Math.004
			vector_math_004 = _mn_utils_style_old_ball_and_stick.nodes.new("ShaderNodeVectorMath")
			vector_math_004.name = "Vector Math.004"
			vector_math_004.operation = 'SUBTRACT'
			
			#node Vector Math.001
			vector_math_001 = _mn_utils_style_old_ball_and_stick.nodes.new("ShaderNodeVectorMath")
			vector_math_001.name = "Vector Math.001"
			vector_math_001.operation = 'CROSS_PRODUCT'
			
			#node Vector Math
			vector_math_1 = _mn_utils_style_old_ball_and_stick.nodes.new("ShaderNodeVectorMath")
			vector_math_1.name = "Vector Math"
			vector_math_1.operation = 'NORMALIZE'
			
			#node Edges of Vertex
			edges_of_vertex = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeEdgesOfVertex")
			edges_of_vertex.name = "Edges of Vertex"
			#Vertex Index
			edges_of_vertex.inputs[0].default_value = 0
			#Weights
			edges_of_vertex.inputs[1].default_value = 0.0
			#Sort Index
			edges_of_vertex.inputs[2].default_value = 0
			
			#node Edge Vertices
			edge_vertices = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeInputMeshEdgeVertices")
			edge_vertices.name = "Edge Vertices"
			
			#node Store Named Attribute.002
			store_named_attribute_002_1 = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_002_1.name = "Store Named Attribute.002"
			store_named_attribute_002_1.data_type = 'FLOAT_COLOR'
			store_named_attribute_002_1.domain = 'EDGE'
			#Selection
			store_named_attribute_002_1.inputs[1].default_value = True
			#Name
			store_named_attribute_002_1.inputs[2].default_value = "Color"
			
			#node Join Geometry.001
			join_geometry_001 = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_001.name = "Join Geometry.001"
			
			#node Store Named Attribute.004
			store_named_attribute_004_1 = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_004_1.name = "Store Named Attribute.004"
			store_named_attribute_004_1.data_type = 'FLOAT_COLOR'
			store_named_attribute_004_1.domain = 'CORNER'
			#Selection
			store_named_attribute_004_1.inputs[1].default_value = True
			#Name
			store_named_attribute_004_1.inputs[2].default_value = "Color"
			
			#node Named Attribute.004
			named_attribute_004_1 = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_004_1.name = "Named Attribute.004"
			named_attribute_004_1.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute_004_1.inputs[0].default_value = "Color"
			
			#node Reroute.005
			reroute_005_1 = _mn_utils_style_old_ball_and_stick.nodes.new("NodeReroute")
			reroute_005_1.name = "Reroute.005"
			#node Evaluate at Index
			evaluate_at_index = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index.name = "Evaluate at Index"
			evaluate_at_index.data_type = 'FLOAT_COLOR'
			evaluate_at_index.domain = 'POINT'
			
			#node Evaluate at Index.001
			evaluate_at_index_001 = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001.name = "Evaluate at Index.001"
			evaluate_at_index_001.data_type = 'FLOAT_COLOR'
			evaluate_at_index_001.domain = 'POINT'
			
			#node Mix
			mix = _mn_utils_style_old_ball_and_stick.nodes.new("ShaderNodeMix")
			mix.name = "Mix"
			mix.blend_type = 'ADD'
			mix.clamp_factor = True
			mix.clamp_result = False
			mix.data_type = 'RGBA'
			mix.factor_mode = 'UNIFORM'
			#Factor_Float
			mix.inputs[0].default_value = 1.0
			
			#node Compare
			compare_1 = _mn_utils_style_old_ball_and_stick.nodes.new("FunctionNodeCompare")
			compare_1.name = "Compare"
			compare_1.data_type = 'INT'
			compare_1.mode = 'ELEMENT'
			compare_1.operation = 'EQUAL'
			#B_INT
			compare_1.inputs[3].default_value = 2
			
			#node Edges of Vertex.001
			edges_of_vertex_001 = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeEdgesOfVertex")
			edges_of_vertex_001.name = "Edges of Vertex.001"
			#Vertex Index
			edges_of_vertex_001.inputs[0].default_value = 0
			#Weights
			edges_of_vertex_001.inputs[1].default_value = 0.0
			#Sort Index
			edges_of_vertex_001.inputs[2].default_value = 0
			
			#node Switch.001
			switch_001 = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeSwitch")
			switch_001.name = "Switch.001"
			switch_001.input_type = 'RGBA'
			#True
			switch_001.inputs[2].default_value = (0.0, 0.0, 0.0, 1.0)
			
			#node Named Attribute.003
			named_attribute_003_1 = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_003_1.name = "Named Attribute.003"
			named_attribute_003_1.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute_003_1.inputs[0].default_value = "Color"
			
			#node Reroute.006
			reroute_006_1 = _mn_utils_style_old_ball_and_stick.nodes.new("NodeReroute")
			reroute_006_1.name = "Reroute.006"
			#node Edge Vertices.001
			edge_vertices_001 = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeInputMeshEdgeVertices")
			edge_vertices_001.name = "Edge Vertices.001"
			
			#node Separate Geometry.001
			separate_geometry_001 = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_001.name = "Separate Geometry.001"
			separate_geometry_001.domain = 'EDGE'
			
			#node Subdivide Mesh.001
			subdivide_mesh_001 = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeSubdivideMesh")
			subdivide_mesh_001.name = "Subdivide Mesh.001"
			#Level
			subdivide_mesh_001.inputs[1].default_value = 1
			
			#node Store Named Attribute.003
			store_named_attribute_003_1 = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_003_1.name = "Store Named Attribute.003"
			store_named_attribute_003_1.data_type = 'FLOAT_COLOR'
			store_named_attribute_003_1.domain = 'EDGE'
			#Selection
			store_named_attribute_003_1.inputs[1].default_value = True
			#Name
			store_named_attribute_003_1.inputs[2].default_value = "Color"
			
			#node Group Input
			group_input_1 = _mn_utils_style_old_ball_and_stick.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			
			#node Group Input.003
			group_input_003 = _mn_utils_style_old_ball_and_stick.nodes.new("NodeGroupInput")
			group_input_003.name = "Group Input.003"
			
			#node Boolean Math.001
			boolean_math_001 = _mn_utils_style_old_ball_and_stick.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001.name = "Boolean Math.001"
			boolean_math_001.operation = 'AND'
			
			#node Boolean Math.002
			boolean_math_002 = _mn_utils_style_old_ball_and_stick.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002.name = "Boolean Math.002"
			boolean_math_002.operation = 'NOT'
			
			#node Compare.004
			compare_004 = _mn_utils_style_old_ball_and_stick.nodes.new("FunctionNodeCompare")
			compare_004.name = "Compare.004"
			compare_004.data_type = 'INT'
			compare_004.mode = 'ELEMENT'
			compare_004.operation = 'NOT_EQUAL'
			#B_INT
			compare_004.inputs[3].default_value = 1
			
			#node Curve Circle
			curve_circle = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeCurvePrimitiveCircle")
			curve_circle.name = "Curve Circle"
			curve_circle.mode = 'RADIUS'
			#Radius
			curve_circle.inputs[4].default_value = 0.009999999776482582
			
			#node Group Input.008
			group_input_008 = _mn_utils_style_old_ball_and_stick.nodes.new("NodeGroupInput")
			group_input_008.name = "Group Input.008"
			group_input_008.outputs[1].hide = True
			group_input_008.outputs[2].hide = True
			group_input_008.outputs[3].hide = True
			group_input_008.outputs[4].hide = True
			group_input_008.outputs[5].hide = True
			group_input_008.outputs[7].hide = True
			group_input_008.outputs[8].hide = True
			group_input_008.outputs[9].hide = True
			group_input_008.outputs[10].hide = True
			group_input_008.outputs[11].hide = True
			group_input_008.outputs[12].hide = True
			group_input_008.outputs[13].hide = True
			group_input_008.outputs[14].hide = True
			group_input_008.outputs[15].hide = True
			
			#node Switch.006
			switch_006 = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeSwitch")
			switch_006.name = "Switch.006"
			switch_006.input_type = 'GEOMETRY'
			
			#node Duplicate Elements.001
			duplicate_elements_001 = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeDuplicateElements")
			duplicate_elements_001.name = "Duplicate Elements.001"
			duplicate_elements_001.domain = 'EDGE'
			#Selection
			duplicate_elements_001.inputs[1].default_value = True
			#Amount
			duplicate_elements_001.inputs[2].default_value = 1
			
			#node Group
			group = _mn_utils_style_old_ball_and_stick.nodes.new("GeometryNodeGroup")
			group.name = "Group"
			group.node_tree = topology_find_bonds
			#Input_35
			group.inputs[1].default_value = True
			#Input_2
			group.inputs[2].default_value = 1.0
			
			
			
			#Set parents
			instance_on_points_1.parent = frame_1
			named_attribute_1.parent = frame_1
			math_005.parent = frame_1
			store_named_attribute_001_1.parent = frame_1
			ico_sphere_1.parent = frame_1
			
			#Set locations
			frame_1.location = (1396.0, -422.0)
			math_003.location = (-2104.203125, -775.839111328125)
			vector_math_002.location = (-964.6033935546875, -355.8390808105469)
			vector_math_005.location = (-804.6033935546875, -355.8390808105469)
			switch_1.location = (-2126.564208984375, -426.8847351074219)
			curve_to_mesh.location = (1360.0, 320.0)
			reroute_003_1.location = (-2628.0, -680.0)
			named_attribute_002_1.location = (-2868.0, -620.0)
			group_input_004.location = (-2307.0, -440.0)
			switch_002.location = (-2327.0, -560.0)
			map_range.location = (-1007.0, -820.0)
			switch_003.location = (-827.0, -620.0)
			compare_003.location = (-1007.0, -640.0)
			group_input_001_1.location = (-1167.0, -820.0)
			vector_rotate.location = (-1167.0, -360.0)
			math_002.location = (-1327.0, -360.0)
			group_input_002.location = (-1567.0, -480.0)
			math_001_1.location = (-1527.0, -700.0)
			math_004.location = (-1347.0, -580.0)
			duplicate_elements.location = (-1787.0, -400.0)
			set_shade_smooth_001.location = (1940.0, 400.0)
			set_material_001.location = (2120.0, 400.0)
			set_shade_smooth_002.location = (1940.0, 560.0)
			set_material_002.location = (2120.0, 560.0)
			group_input_006.location = (1740.0, 260.0)
			reroute_001_1.location = (1920.0, 260.0)
			reroute_002_1.location = (2100.0, 260.0)
			join_geometry.location = (2380.0, 560.0)
			group_output_1.location = (2560.0, 540.0)
			instance_on_points_1.location = (216.19027709960938, 1258.86181640625)
			named_attribute_1.location = (-125.505859375, 1050.8665771484375)
			math_005.location = (34.494140625, 1050.8665771484375)
			store_named_attribute_001_1.location = (34.494140625, 1270.8665771484375)
			ico_sphere_1.location = (-136.0, 1182.0)
			group_input_007.location = (1020.0, 640.0)
			reroute_004_1.location = (1580.0, 860.0)
			separate_geometry_1.location = (-2179.85498046875, 880.0)
			compare_002.location = (-2487.0, -500.0)
			set_position_1.location = (-987.0, -160.0)
			mesh_to_curve_002.location = (-425.2333679199219, 265.6181335449219)
			set_curve_radius_001.location = (-141.0, 122.8011474609375)
			set_curve_radius_002.location = (-150.25411987304688, 281.4866638183594)
			mesh_to_curve_001.location = (-801.3724365234375, -150.9313507080078)
			set_spline_type.location = (-620.0, -160.0)
			resample_curve_001.location = (-435.21929931640625, -129.25401306152344)
			group_input_011.location = (-888.1909790039062, 3.3690643310546875)
			math_1.location = (-645.7537841796875, 17.9141845703125)
			subdivide_mesh.location = (-1580.0, -320.0)
			vector_math_004.location = (-1568.566162109375, -1196.5731201171875)
			vector_math_001.location = (-1568.566162109375, -1056.5731201171875)
			vector_math_1.location = (-1408.566162109375, -1056.5731201171875)
			edges_of_vertex.location = (-1167.0, -640.0)
			edge_vertices.location = (-1768.566162109375, -1076.5731201171875)
			store_named_attribute_002_1.location = (-1240.0, -100.0)
			join_geometry_001.location = (326.14776611328125, 216.18084716796875)
			store_named_attribute_004_1.location = (695.0147094726562, 188.691650390625)
			named_attribute_004_1.location = (188.46722412109375, -124.93585205078125)
			reroute_005_1.location = (-1322.2879638671875, -96.09971618652344)
			evaluate_at_index.location = (-2349.74462890625, -1172.8079833984375)
			evaluate_at_index_001.location = (-2349.74462890625, -1332.8079833984375)
			mix.location = (-2111.32177734375, -1007.6085205078125)
			compare_1.location = (-2900.0, -1180.0)
			edges_of_vertex_001.location = (-3060.0, -1180.0)
			switch_001.location = (-2740.0, -1180.0)
			named_attribute_003_1.location = (-2900.0, -1340.0)
			reroute_006_1.location = (-2467.5224609375, -1303.15087890625)
			edge_vertices_001.location = (-2740.0, -1340.0)
			separate_geometry_001.location = (-1739.750732421875, 98.57808685302734)
			subdivide_mesh_001.location = (-1523.1390380859375, 100.0)
			store_named_attribute_003_1.location = (-1237.1416015625, 213.08575439453125)
			group_input_1.location = (-2939.85498046875, 780.0)
			group_input_003.location = (-2585.884033203125, 145.2239227294922)
			boolean_math_001.location = (-2181.7490234375, 11.80624008178711)
			boolean_math_002.location = (-1988.4156494140625, 8.69737434387207)
			compare_004.location = (-2409.281005859375, -174.4285888671875)
			curve_circle.location = (1360.0, 180.0)
			group_input_008.location = (1117.6759033203125, 157.1241912841797)
			switch_006.location = (-2364.34716796875, 915.9468994140625)
			duplicate_elements_001.location = (-1960.0, 436.7082214355469)
			group.location = (-2679.85498046875, 940.0)
			
			#Set dimensions
			frame_1.width, frame_1.height = 552.0, 438.0
			math_003.width, math_003.height = 140.0, 100.0
			vector_math_002.width, vector_math_002.height = 140.0, 100.0
			vector_math_005.width, vector_math_005.height = 140.0, 100.0
			switch_1.width, switch_1.height = 140.0, 100.0
			curve_to_mesh.width, curve_to_mesh.height = 140.0, 100.0
			reroute_003_1.width, reroute_003_1.height = 16.0, 100.0
			named_attribute_002_1.width, named_attribute_002_1.height = 140.0, 100.0
			group_input_004.width, group_input_004.height = 140.0, 100.0
			switch_002.width, switch_002.height = 140.0, 100.0
			map_range.width, map_range.height = 140.0, 100.0
			switch_003.width, switch_003.height = 140.0, 100.0
			compare_003.width, compare_003.height = 140.0, 100.0
			group_input_001_1.width, group_input_001_1.height = 140.0, 100.0
			vector_rotate.width, vector_rotate.height = 140.0, 100.0
			math_002.width, math_002.height = 140.0, 100.0
			group_input_002.width, group_input_002.height = 140.0, 100.0
			math_001_1.width, math_001_1.height = 140.0, 100.0
			math_004.width, math_004.height = 140.0, 100.0
			duplicate_elements.width, duplicate_elements.height = 140.0, 100.0
			set_shade_smooth_001.width, set_shade_smooth_001.height = 140.0, 100.0
			set_material_001.width, set_material_001.height = 140.0, 100.0
			set_shade_smooth_002.width, set_shade_smooth_002.height = 140.0, 100.0
			set_material_002.width, set_material_002.height = 140.0, 100.0
			group_input_006.width, group_input_006.height = 140.0, 100.0
			reroute_001_1.width, reroute_001_1.height = 16.0, 100.0
			reroute_002_1.width, reroute_002_1.height = 16.0, 100.0
			join_geometry.width, join_geometry.height = 140.0, 100.0
			group_output_1.width, group_output_1.height = 140.0, 100.0
			instance_on_points_1.width, instance_on_points_1.height = 140.0, 100.0
			named_attribute_1.width, named_attribute_1.height = 140.0, 100.0
			math_005.width, math_005.height = 140.0, 100.0
			store_named_attribute_001_1.width, store_named_attribute_001_1.height = 140.0, 100.0
			ico_sphere_1.width, ico_sphere_1.height = 140.0, 100.0
			group_input_007.width, group_input_007.height = 140.0, 100.0
			reroute_004_1.width, reroute_004_1.height = 16.0, 100.0
			separate_geometry_1.width, separate_geometry_1.height = 140.0, 100.0
			compare_002.width, compare_002.height = 140.0, 100.0
			set_position_1.width, set_position_1.height = 140.0, 100.0
			mesh_to_curve_002.width, mesh_to_curve_002.height = 140.0, 100.0
			set_curve_radius_001.width, set_curve_radius_001.height = 140.0, 100.0
			set_curve_radius_002.width, set_curve_radius_002.height = 140.0, 100.0
			mesh_to_curve_001.width, mesh_to_curve_001.height = 140.0, 100.0
			set_spline_type.width, set_spline_type.height = 140.0, 100.0
			resample_curve_001.width, resample_curve_001.height = 140.0, 100.0
			group_input_011.width, group_input_011.height = 140.0, 100.0
			math_1.width, math_1.height = 140.0, 100.0
			subdivide_mesh.width, subdivide_mesh.height = 140.0, 100.0
			vector_math_004.width, vector_math_004.height = 140.0, 100.0
			vector_math_001.width, vector_math_001.height = 140.0, 100.0
			vector_math_1.width, vector_math_1.height = 140.0, 100.0
			edges_of_vertex.width, edges_of_vertex.height = 140.0, 100.0
			edge_vertices.width, edge_vertices.height = 140.0, 100.0
			store_named_attribute_002_1.width, store_named_attribute_002_1.height = 140.0, 100.0
			join_geometry_001.width, join_geometry_001.height = 140.0, 100.0
			store_named_attribute_004_1.width, store_named_attribute_004_1.height = 184.1370849609375, 100.0
			named_attribute_004_1.width, named_attribute_004_1.height = 140.0, 100.0
			reroute_005_1.width, reroute_005_1.height = 16.0, 100.0
			evaluate_at_index.width, evaluate_at_index.height = 140.0, 100.0
			evaluate_at_index_001.width, evaluate_at_index_001.height = 140.0, 100.0
			mix.width, mix.height = 140.0, 100.0
			compare_1.width, compare_1.height = 140.0, 100.0
			edges_of_vertex_001.width, edges_of_vertex_001.height = 140.0, 100.0
			switch_001.width, switch_001.height = 140.0, 100.0
			named_attribute_003_1.width, named_attribute_003_1.height = 140.828125, 100.0
			reroute_006_1.width, reroute_006_1.height = 16.0, 100.0
			edge_vertices_001.width, edge_vertices_001.height = 140.0, 100.0
			separate_geometry_001.width, separate_geometry_001.height = 140.0, 100.0
			subdivide_mesh_001.width, subdivide_mesh_001.height = 140.0, 100.0
			store_named_attribute_003_1.width, store_named_attribute_003_1.height = 140.0, 100.0
			group_input_1.width, group_input_1.height = 140.0, 100.0
			group_input_003.width, group_input_003.height = 140.0, 100.0
			boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
			boolean_math_002.width, boolean_math_002.height = 140.0, 100.0
			compare_004.width, compare_004.height = 150.75045776367188, 100.0
			curve_circle.width, curve_circle.height = 140.0, 100.0
			group_input_008.width, group_input_008.height = 140.0, 100.0
			switch_006.width, switch_006.height = 140.0, 100.0
			duplicate_elements_001.width, duplicate_elements_001.height = 140.0, 100.0
			group.width, group.height = 200.0, 100.0
			
			#initialize _mn_utils_style_old_ball_and_stick links
			#curve_circle.Curve -> curve_to_mesh.Profile Curve
			_mn_utils_style_old_ball_and_stick.links.new(curve_circle.outputs[0], curve_to_mesh.inputs[1])
			#reroute_004_1.Output -> instance_on_points_1.Points
			_mn_utils_style_old_ball_and_stick.links.new(reroute_004_1.outputs[0], instance_on_points_1.inputs[0])
			#store_named_attribute_001_1.Geometry -> instance_on_points_1.Instance
			_mn_utils_style_old_ball_and_stick.links.new(store_named_attribute_001_1.outputs[0], instance_on_points_1.inputs[2])
			#store_named_attribute_002_1.Geometry -> set_position_1.Geometry
			_mn_utils_style_old_ball_and_stick.links.new(store_named_attribute_002_1.outputs[0], set_position_1.inputs[0])
			#edge_vertices.Position 1 -> vector_math_001.Vector
			_mn_utils_style_old_ball_and_stick.links.new(edge_vertices.outputs[2], vector_math_001.inputs[0])
			#edge_vertices.Position 2 -> vector_math_001.Vector
			_mn_utils_style_old_ball_and_stick.links.new(edge_vertices.outputs[3], vector_math_001.inputs[1])
			#vector_rotate.Vector -> vector_math_002.Vector
			_mn_utils_style_old_ball_and_stick.links.new(vector_rotate.outputs[0], vector_math_002.inputs[0])
			#reroute_003_1.Output -> compare_002.A
			_mn_utils_style_old_ball_and_stick.links.new(reroute_003_1.outputs[0], compare_002.inputs[2])
			#compare_002.Result -> switch_002.Switch
			_mn_utils_style_old_ball_and_stick.links.new(compare_002.outputs[0], switch_002.inputs[0])
			#math_002.Value -> vector_math_002.Scale
			_mn_utils_style_old_ball_and_stick.links.new(math_002.outputs[0], vector_math_002.inputs[3])
			#vector_math_001.Vector -> vector_math_1.Vector
			_mn_utils_style_old_ball_and_stick.links.new(vector_math_001.outputs[0], vector_math_1.inputs[0])
			#vector_math_1.Vector -> vector_rotate.Vector
			_mn_utils_style_old_ball_and_stick.links.new(vector_math_1.outputs[0], vector_rotate.inputs[0])
			#edge_vertices.Position 1 -> vector_math_004.Vector
			_mn_utils_style_old_ball_and_stick.links.new(edge_vertices.outputs[2], vector_math_004.inputs[0])
			#edge_vertices.Position 2 -> vector_math_004.Vector
			_mn_utils_style_old_ball_and_stick.links.new(edge_vertices.outputs[3], vector_math_004.inputs[1])
			#vector_math_004.Vector -> vector_rotate.Axis
			_mn_utils_style_old_ball_and_stick.links.new(vector_math_004.outputs[0], vector_rotate.inputs[2])
			#vector_math_005.Vector -> set_position_1.Offset
			_mn_utils_style_old_ball_and_stick.links.new(vector_math_005.outputs[0], set_position_1.inputs[3])
			#vector_math_002.Vector -> vector_math_005.Vector
			_mn_utils_style_old_ball_and_stick.links.new(vector_math_002.outputs[0], vector_math_005.inputs[0])
			#edges_of_vertex.Total -> compare_003.A
			_mn_utils_style_old_ball_and_stick.links.new(edges_of_vertex.outputs[1], compare_003.inputs[2])
			#compare_003.Result -> switch_003.Switch
			_mn_utils_style_old_ball_and_stick.links.new(compare_003.outputs[0], switch_003.inputs[0])
			#switch_003.Output -> vector_math_005.Scale
			_mn_utils_style_old_ball_and_stick.links.new(switch_003.outputs[0], vector_math_005.inputs[3])
			#duplicate_elements.Geometry -> subdivide_mesh.Mesh
			_mn_utils_style_old_ball_and_stick.links.new(duplicate_elements.outputs[0], subdivide_mesh.inputs[0])
			#store_named_attribute_004_1.Geometry -> curve_to_mesh.Curve
			_mn_utils_style_old_ball_and_stick.links.new(store_named_attribute_004_1.outputs[0], curve_to_mesh.inputs[0])
			#reroute_003_1.Output -> math_003.Value
			_mn_utils_style_old_ball_and_stick.links.new(reroute_003_1.outputs[0], math_003.inputs[1])
			#duplicate_elements.Duplicate Index -> math_001_1.Value
			_mn_utils_style_old_ball_and_stick.links.new(duplicate_elements.outputs[1], math_001_1.inputs[0])
			#math_001_1.Value -> math_004.Value
			_mn_utils_style_old_ball_and_stick.links.new(math_001_1.outputs[0], math_004.inputs[1])
			#math_004.Value -> vector_rotate.Angle
			_mn_utils_style_old_ball_and_stick.links.new(math_004.outputs[0], vector_rotate.inputs[3])
			#math_003.Value -> math_001_1.Value
			_mn_utils_style_old_ball_and_stick.links.new(math_003.outputs[0], math_001_1.inputs[1])
			#named_attribute_002_1.Attribute -> reroute_003_1.Input
			_mn_utils_style_old_ball_and_stick.links.new(named_attribute_002_1.outputs[0], reroute_003_1.inputs[0])
			#map_range.Result -> switch_003.True
			_mn_utils_style_old_ball_and_stick.links.new(map_range.outputs[0], switch_003.inputs[2])
			#reroute_001_1.Output -> set_shade_smooth_001.Shade Smooth
			_mn_utils_style_old_ball_and_stick.links.new(reroute_001_1.outputs[0], set_shade_smooth_001.inputs[2])
			#reroute_002_1.Output -> set_material_001.Material
			_mn_utils_style_old_ball_and_stick.links.new(reroute_002_1.outputs[0], set_material_001.inputs[2])
			#set_shade_smooth_001.Geometry -> set_material_001.Geometry
			_mn_utils_style_old_ball_and_stick.links.new(set_shade_smooth_001.outputs[0], set_material_001.inputs[0])
			#set_material_001.Geometry -> group_output_1.Sticks Mesh
			_mn_utils_style_old_ball_and_stick.links.new(set_material_001.outputs[0], group_output_1.inputs[1])
			#curve_to_mesh.Mesh -> set_shade_smooth_001.Geometry
			_mn_utils_style_old_ball_and_stick.links.new(curve_to_mesh.outputs[0], set_shade_smooth_001.inputs[0])
			#switch_002.Output -> switch_1.True
			_mn_utils_style_old_ball_and_stick.links.new(switch_002.outputs[0], switch_1.inputs[2])
			#switch_1.Output -> duplicate_elements.Amount
			_mn_utils_style_old_ball_and_stick.links.new(switch_1.outputs[0], duplicate_elements.inputs[2])
			#group_input_004.Split Double Bonds -> switch_1.Switch
			_mn_utils_style_old_ball_and_stick.links.new(group_input_004.outputs[8], switch_1.inputs[0])
			#reroute_001_1.Output -> set_shade_smooth_002.Shade Smooth
			_mn_utils_style_old_ball_and_stick.links.new(reroute_001_1.outputs[0], set_shade_smooth_002.inputs[2])
			#reroute_002_1.Output -> set_material_002.Material
			_mn_utils_style_old_ball_and_stick.links.new(reroute_002_1.outputs[0], set_material_002.inputs[2])
			#set_shade_smooth_002.Geometry -> set_material_002.Geometry
			_mn_utils_style_old_ball_and_stick.links.new(set_shade_smooth_002.outputs[0], set_material_002.inputs[0])
			#set_material_002.Geometry -> group_output_1.Ball Instances
			_mn_utils_style_old_ball_and_stick.links.new(set_material_002.outputs[0], group_output_1.inputs[2])
			#instance_on_points_1.Instances -> set_shade_smooth_002.Geometry
			_mn_utils_style_old_ball_and_stick.links.new(instance_on_points_1.outputs[0], set_shade_smooth_002.inputs[0])
			#group_input_001_1.Double Bond Curve -> map_range.Value
			_mn_utils_style_old_ball_and_stick.links.new(group_input_001_1.outputs[9], map_range.inputs[0])
			#group_input_002.Double Bond Width -> math_002.Value
			_mn_utils_style_old_ball_and_stick.links.new(group_input_002.outputs[10], math_002.inputs[0])
			#group_input_1.Selection -> separate_geometry_1.Selection
			_mn_utils_style_old_ball_and_stick.links.new(group_input_1.outputs[1], separate_geometry_1.inputs[1])
			#group_input_1.Atoms -> group.Atoms
			_mn_utils_style_old_ball_and_stick.links.new(group_input_1.outputs[0], group.inputs[0])
			#switch_006.Output -> separate_geometry_1.Geometry
			_mn_utils_style_old_ball_and_stick.links.new(switch_006.outputs[0], separate_geometry_1.inputs[0])
			#group.Atoms -> switch_006.True
			_mn_utils_style_old_ball_and_stick.links.new(group.outputs[0], switch_006.inputs[2])
			#group_input_1.Atoms -> switch_006.False
			_mn_utils_style_old_ball_and_stick.links.new(group_input_1.outputs[0], switch_006.inputs[1])
			#group_input_1.Find Bonds -> switch_006.Switch
			_mn_utils_style_old_ball_and_stick.links.new(group_input_1.outputs[5], switch_006.inputs[0])
			#named_attribute_1.Attribute -> math_005.Value
			_mn_utils_style_old_ball_and_stick.links.new(named_attribute_1.outputs[0], math_005.inputs[0])
			#math_005.Value -> instance_on_points_1.Scale
			_mn_utils_style_old_ball_and_stick.links.new(math_005.outputs[0], instance_on_points_1.inputs[6])
			#group_input_007.Ball Radius -> math_005.Value
			_mn_utils_style_old_ball_and_stick.links.new(group_input_007.outputs[4], math_005.inputs[1])
			#ico_sphere_1.Mesh -> store_named_attribute_001_1.Geometry
			_mn_utils_style_old_ball_and_stick.links.new(ico_sphere_1.outputs[0], store_named_attribute_001_1.inputs[0])
			#ico_sphere_1.UV Map -> store_named_attribute_001_1.Value
			_mn_utils_style_old_ball_and_stick.links.new(ico_sphere_1.outputs[1], store_named_attribute_001_1.inputs[3])
			#set_material_002.Geometry -> join_geometry.Geometry
			_mn_utils_style_old_ball_and_stick.links.new(set_material_002.outputs[0], join_geometry.inputs[0])
			#join_geometry.Geometry -> group_output_1.Ball and Stick Mesh
			_mn_utils_style_old_ball_and_stick.links.new(join_geometry.outputs[0], group_output_1.inputs[0])
			#group_input_006.Shade Smooth -> reroute_001_1.Input
			_mn_utils_style_old_ball_and_stick.links.new(group_input_006.outputs[2], reroute_001_1.inputs[0])
			#group_input_006.Material -> reroute_002_1.Input
			_mn_utils_style_old_ball_and_stick.links.new(group_input_006.outputs[14], reroute_002_1.inputs[0])
			#group_input_008.Bond Resolution -> curve_circle.Resolution
			_mn_utils_style_old_ball_and_stick.links.new(group_input_008.outputs[6], curve_circle.inputs[0])
			#group_input_002.Double Bond Rotate -> math_004.Value
			_mn_utils_style_old_ball_and_stick.links.new(group_input_002.outputs[13], math_004.inputs[0])
			#group_input_007.Ball Resolution -> ico_sphere_1.Subdivisions
			_mn_utils_style_old_ball_and_stick.links.new(group_input_007.outputs[3], ico_sphere_1.inputs[1])
			#separate_geometry_1.Selection -> reroute_004_1.Input
			_mn_utils_style_old_ball_and_stick.links.new(separate_geometry_1.outputs[0], reroute_004_1.inputs[0])
			#duplicate_elements_001.Geometry -> separate_geometry_001.Geometry
			_mn_utils_style_old_ball_and_stick.links.new(duplicate_elements_001.outputs[0], separate_geometry_001.inputs[0])
			#separate_geometry_001.Inverted -> duplicate_elements.Geometry
			_mn_utils_style_old_ball_and_stick.links.new(separate_geometry_001.outputs[1], duplicate_elements.inputs[0])
			#reroute_003_1.Output -> compare_004.A
			_mn_utils_style_old_ball_and_stick.links.new(reroute_003_1.outputs[0], compare_004.inputs[2])
			#set_position_1.Geometry -> mesh_to_curve_001.Mesh
			_mn_utils_style_old_ball_and_stick.links.new(set_position_1.outputs[0], mesh_to_curve_001.inputs[0])
			#store_named_attribute_003_1.Geometry -> mesh_to_curve_002.Mesh
			_mn_utils_style_old_ball_and_stick.links.new(store_named_attribute_003_1.outputs[0], mesh_to_curve_002.inputs[0])
			#resample_curve_001.Curve -> set_curve_radius_001.Curve
			_mn_utils_style_old_ball_and_stick.links.new(resample_curve_001.outputs[0], set_curve_radius_001.inputs[0])
			#mesh_to_curve_002.Curve -> set_curve_radius_002.Curve
			_mn_utils_style_old_ball_and_stick.links.new(mesh_to_curve_002.outputs[0], set_curve_radius_002.inputs[0])
			#set_curve_radius_001.Curve -> join_geometry_001.Geometry
			_mn_utils_style_old_ball_and_stick.links.new(set_curve_radius_001.outputs[0], join_geometry_001.inputs[0])
			#group_input_011.Bond Radius -> set_curve_radius_002.Radius
			_mn_utils_style_old_ball_and_stick.links.new(group_input_011.outputs[7], set_curve_radius_002.inputs[2])
			#group_input_011.Double Bond Radius -> set_curve_radius_001.Radius
			_mn_utils_style_old_ball_and_stick.links.new(group_input_011.outputs[12], set_curve_radius_001.inputs[2])
			#set_spline_type.Curve -> resample_curve_001.Curve
			_mn_utils_style_old_ball_and_stick.links.new(set_spline_type.outputs[0], resample_curve_001.inputs[0])
			#mesh_to_curve_001.Curve -> set_spline_type.Curve
			_mn_utils_style_old_ball_and_stick.links.new(mesh_to_curve_001.outputs[0], set_spline_type.inputs[0])
			#group_input_011.Double Bond Resolution -> math_1.Value
			_mn_utils_style_old_ball_and_stick.links.new(group_input_011.outputs[11], math_1.inputs[0])
			#math_1.Value -> resample_curve_001.Count
			_mn_utils_style_old_ball_and_stick.links.new(math_1.outputs[0], resample_curve_001.inputs[2])
			#subdivide_mesh.Mesh -> store_named_attribute_002_1.Geometry
			_mn_utils_style_old_ball_and_stick.links.new(subdivide_mesh.outputs[0], store_named_attribute_002_1.inputs[0])
			#edges_of_vertex_001.Total -> compare_1.A
			_mn_utils_style_old_ball_and_stick.links.new(edges_of_vertex_001.outputs[1], compare_1.inputs[2])
			#compare_1.Result -> switch_001.Switch
			_mn_utils_style_old_ball_and_stick.links.new(compare_1.outputs[0], switch_001.inputs[0])
			#reroute_006_1.Output -> evaluate_at_index.Value
			_mn_utils_style_old_ball_and_stick.links.new(reroute_006_1.outputs[0], evaluate_at_index.inputs[1])
			#edge_vertices_001.Vertex Index 1 -> evaluate_at_index.Index
			_mn_utils_style_old_ball_and_stick.links.new(edge_vertices_001.outputs[0], evaluate_at_index.inputs[0])
			#reroute_006_1.Output -> evaluate_at_index_001.Value
			_mn_utils_style_old_ball_and_stick.links.new(reroute_006_1.outputs[0], evaluate_at_index_001.inputs[1])
			#edge_vertices_001.Vertex Index 2 -> evaluate_at_index_001.Index
			_mn_utils_style_old_ball_and_stick.links.new(edge_vertices_001.outputs[1], evaluate_at_index_001.inputs[0])
			#evaluate_at_index.Value -> mix.A
			_mn_utils_style_old_ball_and_stick.links.new(evaluate_at_index.outputs[0], mix.inputs[6])
			#evaluate_at_index_001.Value -> mix.B
			_mn_utils_style_old_ball_and_stick.links.new(evaluate_at_index_001.outputs[0], mix.inputs[7])
			#reroute_005_1.Output -> store_named_attribute_002_1.Value
			_mn_utils_style_old_ball_and_stick.links.new(reroute_005_1.outputs[0], store_named_attribute_002_1.inputs[3])
			#named_attribute_003_1.Attribute -> switch_001.False
			_mn_utils_style_old_ball_and_stick.links.new(named_attribute_003_1.outputs[0], switch_001.inputs[1])
			#subdivide_mesh_001.Mesh -> store_named_attribute_003_1.Geometry
			_mn_utils_style_old_ball_and_stick.links.new(subdivide_mesh_001.outputs[0], store_named_attribute_003_1.inputs[0])
			#mix.Result -> reroute_005_1.Input
			_mn_utils_style_old_ball_and_stick.links.new(mix.outputs[2], reroute_005_1.inputs[0])
			#reroute_005_1.Output -> store_named_attribute_003_1.Value
			_mn_utils_style_old_ball_and_stick.links.new(reroute_005_1.outputs[0], store_named_attribute_003_1.inputs[3])
			#join_geometry_001.Geometry -> store_named_attribute_004_1.Geometry
			_mn_utils_style_old_ball_and_stick.links.new(join_geometry_001.outputs[0], store_named_attribute_004_1.inputs[0])
			#named_attribute_004_1.Attribute -> store_named_attribute_004_1.Value
			_mn_utils_style_old_ball_and_stick.links.new(named_attribute_004_1.outputs[0], store_named_attribute_004_1.inputs[3])
			#separate_geometry_001.Selection -> subdivide_mesh_001.Mesh
			_mn_utils_style_old_ball_and_stick.links.new(separate_geometry_001.outputs[0], subdivide_mesh_001.inputs[0])
			#switch_001.Output -> reroute_006_1.Input
			_mn_utils_style_old_ball_and_stick.links.new(switch_001.outputs[0], reroute_006_1.inputs[0])
			#group_input_003.Split Double Bonds -> boolean_math_001.Boolean
			_mn_utils_style_old_ball_and_stick.links.new(group_input_003.outputs[8], boolean_math_001.inputs[0])
			#compare_004.Result -> boolean_math_001.Boolean
			_mn_utils_style_old_ball_and_stick.links.new(compare_004.outputs[0], boolean_math_001.inputs[1])
			#boolean_math_001.Boolean -> boolean_math_002.Boolean
			_mn_utils_style_old_ball_and_stick.links.new(boolean_math_001.outputs[0], boolean_math_002.inputs[0])
			#boolean_math_002.Boolean -> separate_geometry_001.Selection
			_mn_utils_style_old_ball_and_stick.links.new(boolean_math_002.outputs[0], separate_geometry_001.inputs[1])
			#separate_geometry_1.Selection -> duplicate_elements_001.Geometry
			_mn_utils_style_old_ball_and_stick.links.new(separate_geometry_1.outputs[0], duplicate_elements_001.inputs[0])
			#set_material_001.Geometry -> join_geometry.Geometry
			_mn_utils_style_old_ball_and_stick.links.new(set_material_001.outputs[0], join_geometry.inputs[0])
			#set_curve_radius_002.Curve -> join_geometry_001.Geometry
			_mn_utils_style_old_ball_and_stick.links.new(set_curve_radius_002.outputs[0], join_geometry_001.inputs[0])
			return _mn_utils_style_old_ball_and_stick

		_mn_utils_style_old_ball_and_stick = _mn_utils_style_old_ball_and_stick_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".MN_utils_style_old_ball_and_stick", type = 'NODES')
		mod.node_group = _mn_utils_style_old_ball_and_stick
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_MN_utils_style_old_ball_and_stick.bl_idname)
			
def register():
	bpy.utils.register_class(_MN_utils_style_old_ball_and_stick)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_MN_utils_style_old_ball_and_stick)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
