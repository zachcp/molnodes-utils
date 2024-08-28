bl_info = {
	"name" : "Topology Find Bonds",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Topology_Find_Bonds(bpy.types.Operator):
	bl_idname = "node.topology_find_bonds"
	bl_label = "Topology Find Bonds"
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
			selection_socket.default_value = True
			selection_socket.attribute_domain = 'POINT'
			selection_socket.hide_value = True
			selection_socket.description = "Selection of atoms to apply this node to"
			
			#Socket Scale
			scale_socket = topology_find_bonds.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
			scale_socket.default_value = 1.0
			scale_socket.min_value = 0.0
			scale_socket.max_value = 10000.0
			scale_socket.subtype = 'NONE'
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

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Topology Find Bonds", type = 'NODES')
		mod.node_group = topology_find_bonds
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Topology_Find_Bonds.bl_idname)
			
def register():
	bpy.utils.register_class(Topology_Find_Bonds)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Topology_Find_Bonds)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
