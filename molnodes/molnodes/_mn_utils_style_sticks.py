bl_info = {
	"name" : ".MN_utils_style_sticks",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _MN_utils_style_sticks(bpy.types.Operator):
	bl_idname = "node._mn_utils_style_sticks"
	bl_label = ".MN_utils_style_sticks"
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

		#initialize _mn_utils_style_sticks node group
		def _mn_utils_style_sticks_node_group():
			_mn_utils_style_sticks = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_utils_style_sticks")

			_mn_utils_style_sticks.color_tag = 'GEOMETRY'
			_mn_utils_style_sticks.description = ""

			_mn_utils_style_sticks.is_modifier = True
			
			#_mn_utils_style_sticks interface
			#Socket Geometry
			geometry_socket = _mn_utils_style_sticks.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket = _mn_utils_style_sticks.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket.attribute_domain = 'POINT'
			atoms_socket.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket = _mn_utils_style_sticks.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket.default_value = True
			selection_socket.attribute_domain = 'POINT'
			selection_socket.hide_value = True
			selection_socket.description = "Selection of atoms to apply this node to"
			
			#Socket Radius
			radius_socket = _mn_utils_style_sticks.interface.new_socket(name = "Radius", in_out='INPUT', socket_type = 'NodeSocketFloat')
			radius_socket.default_value = 0.30000001192092896
			radius_socket.min_value = 0.0
			radius_socket.max_value = 1.0
			radius_socket.subtype = 'NONE'
			radius_socket.attribute_domain = 'POINT'
			radius_socket.description = "Radius of the bond mesh."
			
			#Socket Resolution
			resolution_socket = _mn_utils_style_sticks.interface.new_socket(name = "Resolution", in_out='INPUT', socket_type = 'NodeSocketInt')
			resolution_socket.default_value = 6
			resolution_socket.min_value = 3
			resolution_socket.max_value = 512
			resolution_socket.subtype = 'NONE'
			resolution_socket.attribute_domain = 'POINT'
			resolution_socket.description = "Resolution of the created bond cylinders."
			
			#Socket Fill Caps
			fill_caps_socket = _mn_utils_style_sticks.interface.new_socket(name = "Fill Caps", in_out='INPUT', socket_type = 'NodeSocketBool')
			fill_caps_socket.default_value = False
			fill_caps_socket.attribute_domain = 'POINT'
			fill_caps_socket.description = "Fill the caps at each end of the bonds."
			
			#Socket Interpolate Color
			interpolate_color_socket = _mn_utils_style_sticks.interface.new_socket(name = "Interpolate Color", in_out='INPUT', socket_type = 'NodeSocketBool')
			interpolate_color_socket.default_value = False
			interpolate_color_socket.attribute_domain = 'POINT'
			
			#Panel Material
			material_panel = _mn_utils_style_sticks.interface.new_panel("Material")
			#Socket Shade Smooth
			shade_smooth_socket = _mn_utils_style_sticks.interface.new_socket(name = "Shade Smooth", in_out='INPUT', socket_type = 'NodeSocketBool', parent = material_panel)
			shade_smooth_socket.default_value = True
			shade_smooth_socket.attribute_domain = 'POINT'
			shade_smooth_socket.description = "Apply smooth shading to the created geometry"
			
			#Socket Material
			material_socket = _mn_utils_style_sticks.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial', parent = material_panel)
			material_socket.attribute_domain = 'POINT'
			material_socket.description = "Material to apply to the resulting geometry"
			
			
			
			#initialize _mn_utils_style_sticks nodes
			#node Frame
			frame = _mn_utils_style_sticks.nodes.new("NodeFrame")
			frame.label = "Bonds to Mesh"
			frame.name = "Frame"
			frame.label_size = 20
			frame.shrink = True
			
			#node Frame.001
			frame_001 = _mn_utils_style_sticks.nodes.new("NodeFrame")
			frame_001.label = "Capture index for pulling colors from atoms"
			frame_001.name = "Frame.001"
			frame_001.label_size = 20
			frame_001.shrink = True
			
			#node Frame.003
			frame_003 = _mn_utils_style_sticks.nodes.new("NodeFrame")
			frame_003.label = "Set up materials"
			frame_003.name = "Frame.003"
			frame_003.label_size = 20
			frame_003.shrink = True
			
			#node Frame.002
			frame_002 = _mn_utils_style_sticks.nodes.new("NodeFrame")
			frame_002.label = "Store correct color on the new bond mesh"
			frame_002.name = "Frame.002"
			frame_002.label_size = 20
			frame_002.shrink = True
			
			#node Mesh to Curve
			mesh_to_curve = _mn_utils_style_sticks.nodes.new("GeometryNodeMeshToCurve")
			mesh_to_curve.name = "Mesh to Curve"
			#Selection
			mesh_to_curve.inputs[1].default_value = True
			
			#node Set Curve Radius
			set_curve_radius = _mn_utils_style_sticks.nodes.new("GeometryNodeSetCurveRadius")
			set_curve_radius.name = "Set Curve Radius"
			#Selection
			set_curve_radius.inputs[1].default_value = True
			
			#node Subdivide Curve
			subdivide_curve = _mn_utils_style_sticks.nodes.new("GeometryNodeSubdivideCurve")
			subdivide_curve.name = "Subdivide Curve"
			#Cuts
			subdivide_curve.inputs[1].default_value = 1
			
			#node Group
			group_1 = _mn_utils_style_sticks.nodes.new("GeometryNodeGroup")
			group_1.name = "Group"
			group_1.node_tree = mn_units
			
			#node Group Input.002
			group_input_002 = _mn_utils_style_sticks.nodes.new("NodeGroupInput")
			group_input_002.name = "Group Input.002"
			group_input_002.outputs[0].hide = True
			group_input_002.outputs[3].hide = True
			group_input_002.outputs[5].hide = True
			group_input_002.outputs[6].hide = True
			group_input_002.outputs[7].hide = True
			group_input_002.outputs[8].hide = True
			
			#node Curve Circle
			curve_circle = _mn_utils_style_sticks.nodes.new("GeometryNodeCurvePrimitiveCircle")
			curve_circle.name = "Curve Circle"
			curve_circle.mode = 'RADIUS'
			#Radius
			curve_circle.inputs[4].default_value = 1.0
			
			#node Curve to Mesh
			curve_to_mesh = _mn_utils_style_sticks.nodes.new("GeometryNodeCurveToMesh")
			curve_to_mesh.name = "Curve to Mesh"
			
			#node Group Input.001
			group_input_001 = _mn_utils_style_sticks.nodes.new("NodeGroupInput")
			group_input_001.name = "Group Input.001"
			group_input_001.outputs[0].hide = True
			group_input_001.outputs[2].hide = True
			group_input_001.outputs[4].hide = True
			group_input_001.outputs[5].hide = True
			group_input_001.outputs[6].hide = True
			group_input_001.outputs[7].hide = True
			group_input_001.outputs[8].hide = True
			
			#node Duplicate Elements
			duplicate_elements = _mn_utils_style_sticks.nodes.new("GeometryNodeDuplicateElements")
			duplicate_elements.name = "Duplicate Elements"
			duplicate_elements.domain = 'EDGE'
			#Selection
			duplicate_elements.inputs[1].default_value = True
			#Amount
			duplicate_elements.inputs[2].default_value = 1
			
			#node Mesh Island.001
			mesh_island_001 = _mn_utils_style_sticks.nodes.new("GeometryNodeInputMeshIsland")
			mesh_island_001.name = "Mesh Island.001"
			
			#node Accumulate Field.001
			accumulate_field_001 = _mn_utils_style_sticks.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_001.name = "Accumulate Field.001"
			accumulate_field_001.data_type = 'INT'
			accumulate_field_001.domain = 'POINT'
			#Value
			accumulate_field_001.inputs[0].default_value = 1
			
			#node Capture Attribute
			capture_attribute = _mn_utils_style_sticks.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute.name = "Capture Attribute"
			capture_attribute.active_index = 0
			capture_attribute.capture_items.clear()
			capture_attribute.capture_items.new('FLOAT', "Value")
			capture_attribute.capture_items["Value"].data_type = 'BOOLEAN'
			capture_attribute.domain = 'POINT'
			
			#node Capture Attribute.003
			capture_attribute_003 = _mn_utils_style_sticks.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute_003.name = "Capture Attribute.003"
			capture_attribute_003.active_index = 0
			capture_attribute_003.capture_items.clear()
			capture_attribute_003.capture_items.new('FLOAT', "Vertex Index 1")
			capture_attribute_003.capture_items["Vertex Index 1"].data_type = 'INT'
			capture_attribute_003.capture_items.new('FLOAT', "Vertex Index 2")
			capture_attribute_003.capture_items["Vertex Index 2"].data_type = 'INT'
			capture_attribute_003.domain = 'EDGE'
			
			#node Edge Vertices
			edge_vertices = _mn_utils_style_sticks.nodes.new("GeometryNodeInputMeshEdgeVertices")
			edge_vertices.name = "Edge Vertices"
			
			#node Group Input.003
			group_input_003 = _mn_utils_style_sticks.nodes.new("NodeGroupInput")
			group_input_003.name = "Group Input.003"
			group_input_003.outputs[0].hide = True
			group_input_003.outputs[2].hide = True
			group_input_003.outputs[3].hide = True
			group_input_003.outputs[4].hide = True
			group_input_003.outputs[5].hide = True
			group_input_003.outputs[6].hide = True
			group_input_003.outputs[8].hide = True
			
			#node Set Material
			set_material = _mn_utils_style_sticks.nodes.new("GeometryNodeSetMaterial")
			set_material.name = "Set Material"
			#Selection
			set_material.inputs[1].default_value = True
			
			#node Set Shade Smooth
			set_shade_smooth = _mn_utils_style_sticks.nodes.new("GeometryNodeSetShadeSmooth")
			set_shade_smooth.name = "Set Shade Smooth"
			set_shade_smooth.domain = 'FACE'
			#Selection
			set_shade_smooth.inputs[1].default_value = True
			
			#node Group Input.004
			group_input_004 = _mn_utils_style_sticks.nodes.new("NodeGroupInput")
			group_input_004.name = "Group Input.004"
			group_input_004.outputs[0].hide = True
			group_input_004.outputs[2].hide = True
			group_input_004.outputs[3].hide = True
			group_input_004.outputs[4].hide = True
			group_input_004.outputs[5].hide = True
			group_input_004.outputs[7].hide = True
			group_input_004.outputs[8].hide = True
			
			#node Group Output
			group_output_2 = _mn_utils_style_sticks.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Capture Attribute.001
			capture_attribute_001 = _mn_utils_style_sticks.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute_001.name = "Capture Attribute.001"
			capture_attribute_001.active_index = 0
			capture_attribute_001.capture_items.clear()
			capture_attribute_001.capture_items.new('FLOAT', "Value")
			capture_attribute_001.capture_items["Value"].data_type = 'BOOLEAN'
			capture_attribute_001.domain = 'FACE'
			
			#node Sample Index.001
			sample_index_001 = _mn_utils_style_sticks.nodes.new("GeometryNodeSampleIndex")
			sample_index_001.name = "Sample Index.001"
			sample_index_001.hide = True
			sample_index_001.clamp = False
			sample_index_001.data_type = 'FLOAT_COLOR'
			sample_index_001.domain = 'POINT'
			
			#node Evaluate on Domain.003
			evaluate_on_domain_003 = _mn_utils_style_sticks.nodes.new("GeometryNodeFieldOnDomain")
			evaluate_on_domain_003.name = "Evaluate on Domain.003"
			evaluate_on_domain_003.hide = True
			evaluate_on_domain_003.data_type = 'FLOAT_COLOR'
			evaluate_on_domain_003.domain = 'FACE'
			
			#node Named Attribute.002
			named_attribute_002 = _mn_utils_style_sticks.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002.name = "Named Attribute.002"
			named_attribute_002.hide = True
			named_attribute_002.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute_002.inputs[0].default_value = "Color"
			
			#node Switch.001
			switch_001 = _mn_utils_style_sticks.nodes.new("GeometryNodeSwitch")
			switch_001.name = "Switch.001"
			switch_001.hide = True
			switch_001.input_type = 'INT'
			
			#node Evaluate on Domain
			evaluate_on_domain = _mn_utils_style_sticks.nodes.new("GeometryNodeFieldOnDomain")
			evaluate_on_domain.name = "Evaluate on Domain"
			evaluate_on_domain.hide = True
			evaluate_on_domain.data_type = 'FLOAT_COLOR'
			evaluate_on_domain.domain = 'POINT'
			
			#node Switch
			switch = _mn_utils_style_sticks.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'RGBA'
			
			#node Group Input.005
			group_input_005 = _mn_utils_style_sticks.nodes.new("NodeGroupInput")
			group_input_005.name = "Group Input.005"
			group_input_005.outputs[0].hide = True
			group_input_005.outputs[2].hide = True
			group_input_005.outputs[3].hide = True
			group_input_005.outputs[4].hide = True
			group_input_005.outputs[6].hide = True
			group_input_005.outputs[7].hide = True
			group_input_005.outputs[8].hide = True
			
			#node Store Named Attribute
			store_named_attribute = _mn_utils_style_sticks.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute.name = "Store Named Attribute"
			store_named_attribute.data_type = 'FLOAT_COLOR'
			store_named_attribute.domain = 'CORNER'
			#Selection
			store_named_attribute.inputs[1].default_value = True
			#Name
			store_named_attribute.inputs[2].default_value = "Color"
			
			#node Group Input
			group_input_2 = _mn_utils_style_sticks.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
			#node Separate Geometry
			separate_geometry = _mn_utils_style_sticks.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry.name = "Separate Geometry"
			separate_geometry.domain = 'POINT'
			
			
			
			#Set parents
			mesh_to_curve.parent = frame
			set_curve_radius.parent = frame
			subdivide_curve.parent = frame
			group_1.parent = frame
			group_input_002.parent = frame
			curve_circle.parent = frame
			curve_to_mesh.parent = frame
			group_input_001.parent = frame
			duplicate_elements.parent = frame_001
			mesh_island_001.parent = frame_001
			accumulate_field_001.parent = frame_001
			capture_attribute.parent = frame_001
			capture_attribute_003.parent = frame_001
			group_input_003.parent = frame_003
			set_material.parent = frame_003
			set_shade_smooth.parent = frame_003
			group_input_004.parent = frame_003
			capture_attribute_001.parent = frame_002
			sample_index_001.parent = frame_002
			evaluate_on_domain_003.parent = frame_002
			named_attribute_002.parent = frame_002
			switch_001.parent = frame_002
			evaluate_on_domain.parent = frame_002
			switch.parent = frame_002
			group_input_005.parent = frame_002
			store_named_attribute.parent = frame_002
			
			#Set locations
			frame.location = (-20.0, -180.0)
			frame_001.location = (-40.0, 115.0)
			frame_003.location = (230.0, 120.0)
			frame_002.location = (0.0, 0.0)
			mesh_to_curve.location = (-1560.0, 0.0)
			set_curve_radius.location = (-1400.0, 0.0)
			subdivide_curve.location = (-1240.0, 0.0)
			group_1.location = (-1560.0, -120.0)
			group_input_002.location = (-1570.0, -270.0)
			curve_circle.location = (-1080.0, -140.0)
			curve_to_mesh.location = (-1080.0, 0.0)
			group_input_001.location = (-1080.0, -280.0)
			duplicate_elements.location = (-2000.0, -20.0)
			mesh_island_001.location = (-2000.0, -195.0)
			accumulate_field_001.location = (-1840.0, -155.0)
			capture_attribute.location = (-1840.0, -20.0)
			capture_attribute_003.location = (-2190.0, 125.0)
			edge_vertices.location = (-2460.0, 80.0)
			group_input_003.location = (-80.0, -40.0)
			set_material.location = (-80.0, 100.0)
			set_shade_smooth.location = (110.0, 100.0)
			group_input_004.location = (110.0, -60.0)
			group_output_2.location = (620.0, 220.0)
			capture_attribute_001.location = (-920.0, 60.0)
			sample_index_001.location = (-480.0, 180.0)
			evaluate_on_domain_003.location = (-480.0, 140.0)
			named_attribute_002.location = (-660.0, 160.0)
			switch_001.location = (-660.0, 120.0)
			evaluate_on_domain.location = (-480.0, 100.0)
			switch.location = (-300.0, 220.0)
			group_input_005.location = (-480.0, 60.0)
			store_named_attribute.location = (-120.0, 120.0)
			group_input_2.location = (-2680.0, 240.0)
			separate_geometry.location = (-2460.0, 240.0)
			
			#Set dimensions
			frame.width, frame.height = 690.4000244140625, 434.79998779296875
			frame_001.width, frame_001.height = 550.39990234375, 538.7999877929688
			frame_003.width, frame_003.height = 389.6000061035156, 303.6000061035156
			frame_002.width, frame_002.height = 1000.0, 358.79998779296875
			mesh_to_curve.width, mesh_to_curve.height = 140.0, 100.0
			set_curve_radius.width, set_curve_radius.height = 140.0, 100.0
			subdivide_curve.width, subdivide_curve.height = 140.0, 100.0
			group_1.width, group_1.height = 140.0, 100.0
			group_input_002.width, group_input_002.height = 140.0, 100.0
			curve_circle.width, curve_circle.height = 140.0, 100.0
			curve_to_mesh.width, curve_to_mesh.height = 140.0, 100.0
			group_input_001.width, group_input_001.height = 140.0, 100.0
			duplicate_elements.width, duplicate_elements.height = 140.0, 100.0
			mesh_island_001.width, mesh_island_001.height = 140.0, 100.0
			accumulate_field_001.width, accumulate_field_001.height = 140.0, 100.0
			capture_attribute.width, capture_attribute.height = 140.0, 100.0
			capture_attribute_003.width, capture_attribute_003.height = 140.0, 100.0
			edge_vertices.width, edge_vertices.height = 140.0, 100.0
			group_input_003.width, group_input_003.height = 140.0, 100.0
			set_material.width, set_material.height = 140.0, 100.0
			set_shade_smooth.width, set_shade_smooth.height = 140.0, 100.0
			group_input_004.width, group_input_004.height = 140.0, 100.0
			group_output_2.width, group_output_2.height = 140.0, 100.0
			capture_attribute_001.width, capture_attribute_001.height = 140.0, 100.0
			sample_index_001.width, sample_index_001.height = 140.0, 100.0
			evaluate_on_domain_003.width, evaluate_on_domain_003.height = 140.0, 100.0
			named_attribute_002.width, named_attribute_002.height = 140.0, 100.0
			switch_001.width, switch_001.height = 140.0, 100.0
			evaluate_on_domain.width, evaluate_on_domain.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			group_input_005.width, group_input_005.height = 140.0, 100.0
			store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
			group_input_2.width, group_input_2.height = 140.0, 100.0
			separate_geometry.width, separate_geometry.height = 140.0, 100.0
			
			#initialize _mn_utils_style_sticks links
			#capture_attribute.Geometry -> mesh_to_curve.Mesh
			_mn_utils_style_sticks.links.new(capture_attribute.outputs[0], mesh_to_curve.inputs[0])
			#set_shade_smooth.Geometry -> group_output_2.Geometry
			_mn_utils_style_sticks.links.new(set_shade_smooth.outputs[0], group_output_2.inputs[0])
			#curve_circle.Curve -> curve_to_mesh.Profile Curve
			_mn_utils_style_sticks.links.new(curve_circle.outputs[0], curve_to_mesh.inputs[1])
			#mesh_to_curve.Curve -> set_curve_radius.Curve
			_mn_utils_style_sticks.links.new(mesh_to_curve.outputs[0], set_curve_radius.inputs[0])
			#group_1.Angstrom -> set_curve_radius.Radius
			_mn_utils_style_sticks.links.new(group_1.outputs[0], set_curve_radius.inputs[2])
			#set_curve_radius.Curve -> subdivide_curve.Curve
			_mn_utils_style_sticks.links.new(set_curve_radius.outputs[0], subdivide_curve.inputs[0])
			#capture_attribute_003.Geometry -> duplicate_elements.Geometry
			_mn_utils_style_sticks.links.new(capture_attribute_003.outputs[0], duplicate_elements.inputs[0])
			#group_input_001.Resolution -> curve_circle.Resolution
			_mn_utils_style_sticks.links.new(group_input_001.outputs[3], curve_circle.inputs[0])
			#group_input_003.Material -> set_material.Material
			_mn_utils_style_sticks.links.new(group_input_003.outputs[7], set_material.inputs[2])
			#set_material.Geometry -> set_shade_smooth.Geometry
			_mn_utils_style_sticks.links.new(set_material.outputs[0], set_shade_smooth.inputs[0])
			#group_input_004.Shade Smooth -> set_shade_smooth.Shade Smooth
			_mn_utils_style_sticks.links.new(group_input_004.outputs[6], set_shade_smooth.inputs[2])
			#capture_attribute_003.Geometry -> sample_index_001.Geometry
			_mn_utils_style_sticks.links.new(capture_attribute_003.outputs[0], sample_index_001.inputs[0])
			#named_attribute_002.Attribute -> sample_index_001.Value
			_mn_utils_style_sticks.links.new(named_attribute_002.outputs[0], sample_index_001.inputs[1])
			#subdivide_curve.Curve -> curve_to_mesh.Curve
			_mn_utils_style_sticks.links.new(subdivide_curve.outputs[0], curve_to_mesh.inputs[0])
			#switch_001.Output -> sample_index_001.Index
			_mn_utils_style_sticks.links.new(switch_001.outputs[0], sample_index_001.inputs[2])
			#capture_attribute_001.Geometry -> store_named_attribute.Geometry
			_mn_utils_style_sticks.links.new(capture_attribute_001.outputs[0], store_named_attribute.inputs[0])
			#capture_attribute_003.Vertex Index 1 -> switch_001.False
			_mn_utils_style_sticks.links.new(capture_attribute_003.outputs[1], switch_001.inputs[1])
			#duplicate_elements.Geometry -> capture_attribute.Geometry
			_mn_utils_style_sticks.links.new(duplicate_elements.outputs[0], capture_attribute.inputs[0])
			#accumulate_field_001.Trailing -> capture_attribute.Value
			_mn_utils_style_sticks.links.new(accumulate_field_001.outputs[1], capture_attribute.inputs[1])
			#mesh_island_001.Island Index -> accumulate_field_001.Group ID
			_mn_utils_style_sticks.links.new(mesh_island_001.outputs[0], accumulate_field_001.inputs[1])
			#capture_attribute_003.Vertex Index 2 -> switch_001.True
			_mn_utils_style_sticks.links.new(capture_attribute_003.outputs[2], switch_001.inputs[2])
			#curve_to_mesh.Mesh -> capture_attribute_001.Geometry
			_mn_utils_style_sticks.links.new(curve_to_mesh.outputs[0], capture_attribute_001.inputs[0])
			#capture_attribute_001.Value -> switch_001.Switch
			_mn_utils_style_sticks.links.new(capture_attribute_001.outputs[1], switch_001.inputs[0])
			#capture_attribute.Value -> capture_attribute_001.Value
			_mn_utils_style_sticks.links.new(capture_attribute.outputs[1], capture_attribute_001.inputs[1])
			#sample_index_001.Value -> evaluate_on_domain_003.Value
			_mn_utils_style_sticks.links.new(sample_index_001.outputs[0], evaluate_on_domain_003.inputs[0])
			#store_named_attribute.Geometry -> set_material.Geometry
			_mn_utils_style_sticks.links.new(store_named_attribute.outputs[0], set_material.inputs[0])
			#group_input_002.Radius -> group_1.Value
			_mn_utils_style_sticks.links.new(group_input_002.outputs[2], group_1.inputs[0])
			#group_input_002.Fill Caps -> curve_to_mesh.Fill Caps
			_mn_utils_style_sticks.links.new(group_input_002.outputs[4], curve_to_mesh.inputs[2])
			#evaluate_on_domain_003.Value -> evaluate_on_domain.Value
			_mn_utils_style_sticks.links.new(evaluate_on_domain_003.outputs[0], evaluate_on_domain.inputs[0])
			#evaluate_on_domain.Value -> switch.True
			_mn_utils_style_sticks.links.new(evaluate_on_domain.outputs[0], switch.inputs[2])
			#switch.Output -> store_named_attribute.Value
			_mn_utils_style_sticks.links.new(switch.outputs[0], store_named_attribute.inputs[3])
			#evaluate_on_domain_003.Value -> switch.False
			_mn_utils_style_sticks.links.new(evaluate_on_domain_003.outputs[0], switch.inputs[1])
			#group_input_005.Interpolate Color -> switch.Switch
			_mn_utils_style_sticks.links.new(group_input_005.outputs[5], switch.inputs[0])
			#group_input_2.Atoms -> separate_geometry.Geometry
			_mn_utils_style_sticks.links.new(group_input_2.outputs[0], separate_geometry.inputs[0])
			#separate_geometry.Selection -> capture_attribute_003.Geometry
			_mn_utils_style_sticks.links.new(separate_geometry.outputs[0], capture_attribute_003.inputs[0])
			#group_input_2.Selection -> separate_geometry.Selection
			_mn_utils_style_sticks.links.new(group_input_2.outputs[1], separate_geometry.inputs[1])
			#edge_vertices.Vertex Index 2 -> capture_attribute_003.Vertex Index 2
			_mn_utils_style_sticks.links.new(edge_vertices.outputs[1], capture_attribute_003.inputs[2])
			#edge_vertices.Vertex Index 1 -> capture_attribute_003.Vertex Index 1
			_mn_utils_style_sticks.links.new(edge_vertices.outputs[0], capture_attribute_003.inputs[1])
			return _mn_utils_style_sticks

		_mn_utils_style_sticks = _mn_utils_style_sticks_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".MN_utils_style_sticks", type = 'NODES')
		mod.node_group = _mn_utils_style_sticks
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_MN_utils_style_sticks.bl_idname)
			
def register():
	bpy.utils.register_class(_MN_utils_style_sticks)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_MN_utils_style_sticks)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
