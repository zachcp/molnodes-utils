bl_info = {
	"name" : "Style Ball and Stick",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Style_Ball_and_Stick(bpy.types.Operator):
	bl_idname = "node.style_ball_and_stick"
	bl_label = "Style Ball and Stick"
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

		#initialize topology_find_bonds node group
		def topology_find_bonds_node_group():
			topology_find_bonds = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Topology Find Bonds")

			topology_find_bonds.color_tag = 'GEOMETRY'
			topology_find_bonds.description = ""

			topology_find_bonds.is_modifier = True
			
			#topology_find_bonds interface
			#Socket Atoms
			atoms_socket_1 = topology_find_bonds.interface.new_socket(name = "Atoms", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_1.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket_2 = topology_find_bonds.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_2.attribute_domain = 'POINT'
			atoms_socket_2.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket_1 = topology_find_bonds.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_1.default_value = True
			selection_socket_1.attribute_domain = 'POINT'
			selection_socket_1.hide_value = True
			selection_socket_1.description = "Selection of atoms to apply this node to"
			
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
			frame_1 = topology_find_bonds.nodes.new("NodeFrame")
			frame_1.label = "Create Distance Probe"
			frame_1.name = "Frame"
			frame_1.label_size = 20
			frame_1.shrink = True
			
			#node Sample Nearest
			sample_nearest = topology_find_bonds.nodes.new("GeometryNodeSampleNearest")
			sample_nearest.name = "Sample Nearest"
			sample_nearest.domain = 'POINT'
			#Sample Position
			sample_nearest.inputs[1].default_value = (0.0, 0.0, 0.0)
			
			#node Sample Index.001
			sample_index_001_1 = topology_find_bonds.nodes.new("GeometryNodeSampleIndex")
			sample_index_001_1.name = "Sample Index.001"
			sample_index_001_1.clamp = False
			sample_index_001_1.data_type = 'FLOAT_VECTOR'
			sample_index_001_1.domain = 'POINT'
			
			#node Math
			math_1 = topology_find_bonds.nodes.new("ShaderNodeMath")
			math_1.name = "Math"
			math_1.hide = True
			math_1.operation = 'MULTIPLY'
			math_1.use_clamp = False
			math_1.inputs[2].hide = True
			
			#node Group Input.001
			group_input_001_1 = topology_find_bonds.nodes.new("NodeGroupInput")
			group_input_001_1.name = "Group Input.001"
			group_input_001_1.outputs[0].hide = True
			group_input_001_1.outputs[1].hide = True
			group_input_001_1.outputs[3].hide = True
			
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
			named_attribute_002_1 = topology_find_bonds.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002_1.name = "Named Attribute.002"
			named_attribute_002_1.data_type = 'INT'
			#Name
			named_attribute_002_1.inputs[0].default_value = "res_name"
			
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
			store_named_attribute_1 = topology_find_bonds.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_1.name = "Store Named Attribute"
			store_named_attribute_1.data_type = 'INT'
			store_named_attribute_1.domain = 'POINT'
			#Selection
			store_named_attribute_1.inputs[1].default_value = True
			#Name
			store_named_attribute_1.inputs[2].default_value = "atomic_number"
			
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
			group_output_3 = topology_find_bonds.nodes.new("NodeGroupOutput")
			group_output_3.name = "Group Output"
			group_output_3.is_active_output = True
			
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
			math_001_1 = topology_find_bonds.nodes.new("ShaderNodeMath")
			math_001_1.label = "x * 0.62"
			math_001_1.name = "Math.001"
			math_001_1.operation = 'MULTIPLY'
			math_001_1.use_clamp = False
			#Value_001
			math_001_1.inputs[1].default_value = 0.6200000047683716
			
			#node Group Input
			group_input_3 = topology_find_bonds.nodes.new("NodeGroupInput")
			group_input_3.name = "Group Input"
			
			#node Separate Geometry
			separate_geometry_1 = topology_find_bonds.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_1.name = "Separate Geometry"
			separate_geometry_1.domain = 'POINT'
			
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
			capture_attribute_1 = topology_find_bonds.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute_1.name = "Capture Attribute"
			capture_attribute_1.active_index = 0
			capture_attribute_1.capture_items.clear()
			capture_attribute_1.capture_items.new('FLOAT', "Index")
			capture_attribute_1.capture_items["Index"].data_type = 'INT'
			capture_attribute_1.domain = 'POINT'
			
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
			frame_001_1 = topology_find_bonds.nodes.new("NodeFrame")
			frame_001_1.label = "Get original index to sample values with"
			frame_001_1.name = "Frame.001"
			frame_001_1.label_size = 20
			frame_001_1.shrink = True
			
			#node Frame.002
			frame_002_1 = topology_find_bonds.nodes.new("NodeFrame")
			frame_002_1.label = "Create a clean set of points for instancing on"
			frame_002_1.name = "Frame.002"
			frame_002_1.label_size = 20
			frame_002_1.shrink = True
			
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
			frame_003_1 = topology_find_bonds.nodes.new("NodeFrame")
			frame_003_1.label = "Apply the distance probe"
			frame_003_1.name = "Frame.003"
			frame_003_1.label_size = 20
			frame_003_1.shrink = True
			
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
			switch_1 = topology_find_bonds.nodes.new("GeometryNodeSwitch")
			switch_1.name = "Switch"
			switch_1.input_type = 'GEOMETRY'
			
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
			sample_nearest.parent = frame_003_1
			sample_index_001_1.parent = frame_003_1
			math_1.parent = frame_003_1
			group_input_001_1.parent = frame_003_1
			sample_index.parent = frame_1
			vector_math.parent = frame_1
			position.parent = frame_1
			ico_sphere.parent = frame_1
			index.parent = frame_1
			mesh_line.parent = frame_1
			instance_on_points.parent = frame_1
			realize_instances.parent = frame_1
			instance_on_points_001.parent = frame_003_1
			realize_instances_001.parent = frame_003_1
			set_position.parent = frame_003_1
			position_001.parent = frame_003_1
			index_002.parent = frame_001_1
			merge_by_distance.parent = frame_003_1
			sample_nearest_001.parent = frame_001_1
			math_001_1.parent = frame_003_1
			sample_index_010.parent = frame_001_1
			sample_index_002.parent = frame_002_1
			named_attribute_008.parent = frame_002_1
			index_001.parent = frame_002_1
			sample_index_003.parent = frame_002_1
			position_003.parent = frame_002_1
			reroute_004.parent = frame_002_1
			points.parent = frame_002_1
			domain_size.parent = frame_002_1
			axes_to_rotation.parent = frame_1
			merge_by_distance_001.parent = frame_1
			sort_elements.parent = frame_005
			reroute_006.parent = frame_002_1
			reroute_017.parent = frame_001_1
			named_attribute_001.parent = frame_005
			remove_named_attribute.parent = frame_005
			reroute.parent = frame_003_1
			reroute_018.parent = frame_003_1
			domain_size_001.parent = frame_004
			compare.parent = frame_004
			switch_1.parent = frame_004
			
			#Set locations
			frame_1.location = (50.0, 157.0)
			sample_nearest.location = (420.0, 80.0)
			sample_index_001_1.location = (420.0, 280.0)
			math_1.location = (100.0, 220.0)
			group_input_001_1.location = (100.0, 20.0)
			sample_index.location = (-920.0, -200.0)
			vector_math.location = (-1100.0, -220.0)
			position.location = (-1260.0, -220.0)
			ico_sphere.location = (-1095.594970703125, -40.0)
			index.location = (-1100.0, -360.0)
			mesh_line.location = (-760.0, -100.0)
			instance_on_points.location = (-582.12841796875, -16.803972244262695)
			named_attribute.location = (1180.0, 1160.0)
			sample_index_006.location = (1360.0, 1040.0)
			named_attribute_002_1.location = (1360.0, 1160.0)
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
			store_named_attribute_1.location = (1180.0, 820.0)
			index_002.location = (560.0, 800.0)
			named_attribute_006.location = (840.0, 1360.0)
			merge_by_distance.location = (740.0, 440.0)
			group_output_3.location = (3191.530029296875, 851.8171997070312)
			sample_index_011.location = (2000.0, 1040.0)
			sample_nearest_001.location = (560.0, 740.0)
			set_position_002.location = (2000.0, 820.0)
			store_named_attribute_004.location = (1840.0, 820.0)
			store_named_attribute_006.location = (2160.0, 820.0)
			store_named_attribute_005.location = (1020.0, 820.0)
			sample_index_012.location = (2160.0, 1040.0)
			named_attribute_007.location = (2160.0, 1160.0)
			math_001_1.location = (100.0, 180.0)
			group_input_3.location = (-1840.0, 940.0)
			separate_geometry_1.location = (-1660.0, 940.0)
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
			capture_attribute_1.location = (-1460.0, 940.0)
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
			frame_001_1.location = (0.0, 0.0)
			frame_002_1.location = (-230.0, 92.0)
			named_attribute_001.location = (2540.0, 480.0)
			remove_named_attribute.location = (2700.0, 620.0)
			reroute.location = (380.0, 80.0)
			reroute_018.location = (180.0, 380.0)
			frame_003_1.location = (0.0, 0.0)
			domain_size_001.location = (2600.0, 860.0)
			compare.location = (2760.0, 860.0)
			switch_1.location = (2920.0, 860.0)
			reroute_019.location = (2460.0, 780.0)
			frame_004.location = (0.0, 0.0)
			frame_005.location = (30.0, -50.0)
			
			#Set dimensions
			frame_1.width, frame_1.height = 1044.0, 463.0
			sample_nearest.width, sample_nearest.height = 140.0, 100.0
			sample_index_001_1.width, sample_index_001_1.height = 140.0, 100.0
			math_1.width, math_1.height = 140.0, 100.0
			group_input_001_1.width, group_input_001_1.height = 140.0, 100.0
			sample_index.width, sample_index.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			position.width, position.height = 140.0, 100.0
			ico_sphere.width, ico_sphere.height = 140.0, 100.0
			index.width, index.height = 140.0, 100.0
			mesh_line.width, mesh_line.height = 140.0, 100.0
			instance_on_points.width, instance_on_points.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			sample_index_006.width, sample_index_006.height = 140.0, 100.0
			named_attribute_002_1.width, named_attribute_002_1.height = 140.0, 100.0
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
			store_named_attribute_1.width, store_named_attribute_1.height = 140.0, 100.0
			index_002.width, index_002.height = 140.0, 100.0
			named_attribute_006.width, named_attribute_006.height = 140.0, 100.0
			merge_by_distance.width, merge_by_distance.height = 140.0, 100.0
			group_output_3.width, group_output_3.height = 140.0, 100.0
			sample_index_011.width, sample_index_011.height = 140.0, 100.0
			sample_nearest_001.width, sample_nearest_001.height = 140.0, 100.0
			set_position_002.width, set_position_002.height = 140.0, 100.0
			store_named_attribute_004.width, store_named_attribute_004.height = 140.0, 100.0
			store_named_attribute_006.width, store_named_attribute_006.height = 140.0, 100.0
			store_named_attribute_005.width, store_named_attribute_005.height = 140.0, 100.0
			sample_index_012.width, sample_index_012.height = 140.0, 100.0
			named_attribute_007.width, named_attribute_007.height = 140.0, 100.0
			math_001_1.width, math_001_1.height = 140.0, 100.0
			group_input_3.width, group_input_3.height = 140.0, 100.0
			separate_geometry_1.width, separate_geometry_1.height = 140.0, 100.0
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
			capture_attribute_1.width, capture_attribute_1.height = 140.0, 100.0
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
			frame_001_1.width, frame_001_1.height = 408.0, 351.0
			frame_002_1.width, frame_002_1.height = 820.0, 351.0
			named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
			remove_named_attribute.width, remove_named_attribute.height = 170.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			reroute_018.width, reroute_018.height = 16.0, 100.0
			frame_003_1.width, frame_003_1.height = 840.0, 551.0
			domain_size_001.width, domain_size_001.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			switch_1.width, switch_1.height = 140.0, 100.0
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
			#math_1.Value -> instance_on_points_001.Scale
			topology_find_bonds.links.new(math_1.outputs[0], instance_on_points_001.inputs[6])
			#realize_instances_001.Geometry -> set_position.Geometry
			topology_find_bonds.links.new(realize_instances_001.outputs[0], set_position.inputs[0])
			#reroute.Output -> sample_index_001_1.Geometry
			topology_find_bonds.links.new(reroute.outputs[0], sample_index_001_1.inputs[0])
			#position_001.Position -> sample_index_001_1.Value
			topology_find_bonds.links.new(position_001.outputs[0], sample_index_001_1.inputs[1])
			#sample_index_001_1.Value -> set_position.Position
			topology_find_bonds.links.new(sample_index_001_1.outputs[0], set_position.inputs[2])
			#reroute.Output -> sample_nearest.Geometry
			topology_find_bonds.links.new(reroute.outputs[0], sample_nearest.inputs[0])
			#sample_nearest.Index -> sample_index_001_1.Index
			topology_find_bonds.links.new(sample_nearest.outputs[0], sample_index_001_1.inputs[2])
			#set_position.Geometry -> merge_by_distance.Geometry
			topology_find_bonds.links.new(set_position.outputs[0], merge_by_distance.inputs[0])
			#group_input_001_1.Scale -> math_001_1.Value
			topology_find_bonds.links.new(group_input_001_1.outputs[2], math_001_1.inputs[0])
			#math_001_1.Value -> math_1.Value
			topology_find_bonds.links.new(math_001_1.outputs[0], math_1.inputs[1])
			#reroute_017.Output -> sample_nearest_001.Geometry
			topology_find_bonds.links.new(reroute_017.outputs[0], sample_nearest_001.inputs[0])
			#reroute_010.Output -> sample_index_005.Geometry
			topology_find_bonds.links.new(reroute_010.outputs[0], sample_index_005.inputs[0])
			#named_attribute.Attribute -> sample_index_005.Value
			topology_find_bonds.links.new(named_attribute.outputs[0], sample_index_005.inputs[1])
			#sample_index_005.Value -> store_named_attribute_1.Value
			topology_find_bonds.links.new(sample_index_005.outputs[0], store_named_attribute_1.inputs[3])
			#capture_attribute_1.Geometry -> reroute_002.Input
			topology_find_bonds.links.new(capture_attribute_1.outputs[0], reroute_002.inputs[0])
			#store_named_attribute_005.Geometry -> store_named_attribute_1.Geometry
			topology_find_bonds.links.new(store_named_attribute_005.outputs[0], store_named_attribute_1.inputs[0])
			#store_named_attribute_1.Geometry -> store_named_attribute_001.Geometry
			topology_find_bonds.links.new(store_named_attribute_1.outputs[0], store_named_attribute_001.inputs[0])
			#reroute_011.Output -> sample_index_006.Geometry
			topology_find_bonds.links.new(reroute_011.outputs[0], sample_index_006.inputs[0])
			#named_attribute_002_1.Attribute -> sample_index_006.Value
			topology_find_bonds.links.new(named_attribute_002_1.outputs[0], sample_index_006.inputs[1])
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
			#group_input_3.Atoms -> separate_geometry_1.Geometry
			topology_find_bonds.links.new(group_input_3.outputs[0], separate_geometry_1.inputs[0])
			#group_input_3.Selection -> separate_geometry_1.Selection
			topology_find_bonds.links.new(group_input_3.outputs[1], separate_geometry_1.inputs[1])
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
			#sample_index_002.Value -> math_1.Value
			topology_find_bonds.links.new(sample_index_002.outputs[0], math_1.inputs[0])
			#separate_geometry_1.Selection -> capture_attribute_1.Geometry
			topology_find_bonds.links.new(separate_geometry_1.outputs[0], capture_attribute_1.inputs[0])
			#index_003.Index -> capture_attribute_1.Index
			topology_find_bonds.links.new(index_003.outputs[0], capture_attribute_1.inputs[1])
			#capture_attribute_1.Geometry -> reroute_006.Input
			topology_find_bonds.links.new(capture_attribute_1.outputs[0], reroute_006.inputs[0])
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
			#switch_1.Output -> group_output_3.Atoms
			topology_find_bonds.links.new(switch_1.outputs[0], group_output_3.inputs[0])
			#remove_named_attribute.Geometry -> switch_1.False
			topology_find_bonds.links.new(remove_named_attribute.outputs[0], switch_1.inputs[1])
			#compare.Result -> switch_1.Switch
			topology_find_bonds.links.new(compare.outputs[0], switch_1.inputs[0])
			#store_named_attribute_006.Geometry -> reroute_019.Input
			topology_find_bonds.links.new(store_named_attribute_006.outputs[0], reroute_019.inputs[0])
			return topology_find_bonds

		topology_find_bonds = topology_find_bonds_node_group()

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
			selection_socket_2 = _mn_utils_style_spheres_points.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_2.default_value = True
			selection_socket_2.attribute_domain = 'POINT'
			selection_socket_2.hide_value = True
			selection_socket_2.description = "Selection of atoms to apply this node to"
			
			#Socket Radii
			radii_socket = _mn_utils_style_spheres_points.interface.new_socket(name = "Radii", in_out='INPUT', socket_type = 'NodeSocketFloat')
			radii_socket.default_value = 0.800000011920929
			radii_socket.min_value = 0.0
			radii_socket.max_value = 10000.0
			radii_socket.subtype = 'NONE'
			radii_socket.attribute_domain = 'POINT'
			
			#Socket Material
			material_socket_1 = _mn_utils_style_spheres_points.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial')
			material_socket_1.attribute_domain = 'POINT'
			material_socket_1.description = "Material to apply to the resulting geometry"
			
			
			#initialize _mn_utils_style_spheres_points nodes
			#node Group Input
			group_input_4 = _mn_utils_style_spheres_points.nodes.new("NodeGroupInput")
			group_input_4.name = "Group Input"
			
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
			named_attribute_1 = _mn_utils_style_spheres_points.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_1.name = "Named Attribute"
			named_attribute_1.data_type = 'FLOAT'
			#Name
			named_attribute_1.inputs[0].default_value = "vdw_radii"
			
			#node Group
			group_2 = _mn_utils_style_spheres_points.nodes.new("GeometryNodeGroup")
			group_2.name = "Group"
			group_2.node_tree = mn_units
			#Input_1
			group_2.inputs[0].default_value = 0.800000011920929
			
			#node Math
			math_2 = _mn_utils_style_spheres_points.nodes.new("ShaderNodeMath")
			math_2.name = "Math"
			math_2.operation = 'MULTIPLY'
			math_2.use_clamp = False
			
			#node Group Output
			group_output_4 = _mn_utils_style_spheres_points.nodes.new("NodeGroupOutput")
			group_output_4.name = "Group Output"
			group_output_4.is_active_output = True
			
			#node Set Material
			set_material_1 = _mn_utils_style_spheres_points.nodes.new("GeometryNodeSetMaterial")
			set_material_1.name = "Set Material"
			#Selection
			set_material_1.inputs[1].default_value = True
			
			
			
			
			#Set locations
			group_input_4.location = (-1060.0, 60.0)
			mesh_to_points.location = (-540.0, 220.0)
			switch_2.location = (-900.0, -100.0)
			named_attribute_1.location = (-1080.0, -100.0)
			group_2.location = (-1080.0, -240.0)
			math_2.location = (-720.0, 40.0)
			group_output_4.location = (-220.0, 220.0)
			set_material_1.location = (-380.0, 220.0)
			
			#Set dimensions
			group_input_4.width, group_input_4.height = 140.0, 100.0
			mesh_to_points.width, mesh_to_points.height = 140.0, 100.0
			switch_2.width, switch_2.height = 140.0, 100.0
			named_attribute_1.width, named_attribute_1.height = 140.0, 100.0
			group_2.width, group_2.height = 140.0, 100.0
			math_2.width, math_2.height = 140.0, 100.0
			group_output_4.width, group_output_4.height = 140.0, 100.0
			set_material_1.width, set_material_1.height = 140.0, 100.0
			
			#initialize _mn_utils_style_spheres_points links
			#set_material_1.Geometry -> group_output_4.Point Cloud
			_mn_utils_style_spheres_points.links.new(set_material_1.outputs[0], group_output_4.inputs[0])
			#group_input_4.Selection -> mesh_to_points.Selection
			_mn_utils_style_spheres_points.links.new(group_input_4.outputs[1], mesh_to_points.inputs[1])
			#group_input_4.Radii -> math_2.Value
			_mn_utils_style_spheres_points.links.new(group_input_4.outputs[2], math_2.inputs[0])
			#math_2.Value -> mesh_to_points.Radius
			_mn_utils_style_spheres_points.links.new(math_2.outputs[0], mesh_to_points.inputs[3])
			#group_input_4.Material -> set_material_1.Material
			_mn_utils_style_spheres_points.links.new(group_input_4.outputs[3], set_material_1.inputs[2])
			#named_attribute_1.Attribute -> switch_2.Switch
			_mn_utils_style_spheres_points.links.new(named_attribute_1.outputs[0], switch_2.inputs[0])
			#named_attribute_1.Attribute -> switch_2.True
			_mn_utils_style_spheres_points.links.new(named_attribute_1.outputs[0], switch_2.inputs[2])
			#switch_2.Output -> math_2.Value
			_mn_utils_style_spheres_points.links.new(switch_2.outputs[0], math_2.inputs[1])
			#group_input_4.Atoms -> mesh_to_points.Mesh
			_mn_utils_style_spheres_points.links.new(group_input_4.outputs[0], mesh_to_points.inputs[0])
			#mesh_to_points.Points -> set_material_1.Geometry
			_mn_utils_style_spheres_points.links.new(mesh_to_points.outputs[0], set_material_1.inputs[0])
			#group_2.Angstrom -> switch_2.False
			_mn_utils_style_spheres_points.links.new(group_2.outputs[0], switch_2.inputs[1])
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
			instances_socket = _mn_utils_style_spheres_icosphere.interface.new_socket(name = "Instances", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			instances_socket.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket_4 = _mn_utils_style_spheres_icosphere.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_4.attribute_domain = 'POINT'
			atoms_socket_4.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket_3 = _mn_utils_style_spheres_icosphere.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_3.default_value = True
			selection_socket_3.attribute_domain = 'POINT'
			selection_socket_3.hide_value = True
			selection_socket_3.description = "Selection of atoms to apply this node to"
			
			#Socket Radii
			radii_socket_1 = _mn_utils_style_spheres_icosphere.interface.new_socket(name = "Radii", in_out='INPUT', socket_type = 'NodeSocketFloat')
			radii_socket_1.default_value = 0.800000011920929
			radii_socket_1.min_value = 0.0
			radii_socket_1.max_value = 10000.0
			radii_socket_1.subtype = 'NONE'
			radii_socket_1.attribute_domain = 'POINT'
			radii_socket_1.description = "Scale the VDW radii of the atoms."
			
			#Socket Subdivisions
			subdivisions_socket = _mn_utils_style_spheres_icosphere.interface.new_socket(name = "Subdivisions", in_out='INPUT', socket_type = 'NodeSocketInt')
			subdivisions_socket.default_value = 2
			subdivisions_socket.min_value = 0
			subdivisions_socket.max_value = 5
			subdivisions_socket.subtype = 'NONE'
			subdivisions_socket.attribute_domain = 'POINT'
			
			#Socket Shade Smooth
			shade_smooth_socket_1 = _mn_utils_style_spheres_icosphere.interface.new_socket(name = "Shade Smooth", in_out='INPUT', socket_type = 'NodeSocketBool')
			shade_smooth_socket_1.default_value = True
			shade_smooth_socket_1.attribute_domain = 'POINT'
			shade_smooth_socket_1.description = "Apply smooth shading to the created geometry"
			
			#Socket Material
			material_socket_2 = _mn_utils_style_spheres_icosphere.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial')
			material_socket_2.attribute_domain = 'POINT'
			material_socket_2.description = "Material to apply to the resulting geometry"
			
			
			#initialize _mn_utils_style_spheres_icosphere nodes
			#node Frame
			frame_2 = _mn_utils_style_spheres_icosphere.nodes.new("NodeFrame")
			frame_2.label = "Different Levels of Detail."
			frame_2.name = "Frame"
			frame_2.label_size = 20
			frame_2.shrink = True
			
			#node Reroute
			reroute_1 = _mn_utils_style_spheres_icosphere.nodes.new("NodeReroute")
			reroute_1.name = "Reroute"
			#node Math.001
			math_001_2 = _mn_utils_style_spheres_icosphere.nodes.new("ShaderNodeMath")
			math_001_2.name = "Math.001"
			math_001_2.operation = 'MINIMUM'
			math_001_2.use_clamp = False
			
			#node Group Output
			group_output_5 = _mn_utils_style_spheres_icosphere.nodes.new("NodeGroupOutput")
			group_output_5.name = "Group Output"
			group_output_5.is_active_output = True
			
			#node Group Input.002
			group_input_002_1 = _mn_utils_style_spheres_icosphere.nodes.new("NodeGroupInput")
			group_input_002_1.name = "Group Input.002"
			group_input_002_1.outputs[0].hide = True
			group_input_002_1.outputs[1].hide = True
			group_input_002_1.outputs[2].hide = True
			group_input_002_1.outputs[3].hide = True
			group_input_002_1.outputs[6].hide = True
			
			#node Set Shade Smooth
			set_shade_smooth_1 = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeSetShadeSmooth")
			set_shade_smooth_1.name = "Set Shade Smooth"
			set_shade_smooth_1.domain = 'FACE'
			#Selection
			set_shade_smooth_1.inputs[1].default_value = True
			
			#node Set Material
			set_material_2 = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeSetMaterial")
			set_material_2.name = "Set Material"
			#Selection
			set_material_2.inputs[1].default_value = True
			
			#node Group Input
			group_input_5 = _mn_utils_style_spheres_icosphere.nodes.new("NodeGroupInput")
			group_input_5.name = "Group Input"
			group_input_5.outputs[2].hide = True
			group_input_5.outputs[3].hide = True
			group_input_5.outputs[4].hide = True
			group_input_5.outputs[5].hide = True
			group_input_5.outputs[6].hide = True
			
			#node Reroute.001
			reroute_001_1 = _mn_utils_style_spheres_icosphere.nodes.new("NodeReroute")
			reroute_001_1.name = "Reroute.001"
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
			geometry_to_instance = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeGeometryToInstance")
			geometry_to_instance.name = "Geometry to Instance"
			
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
			reroute_002_1 = _mn_utils_style_spheres_icosphere.nodes.new("NodeReroute")
			reroute_002_1.name = "Reroute.002"
			#node Transform Geometry
			transform_geometry = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeTransform")
			transform_geometry.name = "Transform Geometry"
			transform_geometry.mode = 'COMPONENTS'
			#Translation
			transform_geometry.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Rotation
			transform_geometry.inputs[2].default_value = (0.7853981852531433, 0.7853981852531433, 0.0)
			#Scale
			transform_geometry.inputs[3].default_value = (1.0, 1.0, 1.0)
			
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
			named_attribute_2 = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_2.name = "Named Attribute"
			named_attribute_2.data_type = 'FLOAT'
			#Name
			named_attribute_2.inputs[0].default_value = "vdw_radii"
			
			#node Radius
			radius = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeInputRadius")
			radius.name = "Radius"
			
			#node Math
			math_3 = _mn_utils_style_spheres_icosphere.nodes.new("ShaderNodeMath")
			math_3.name = "Math"
			math_3.operation = 'MAXIMUM'
			math_3.use_clamp = False
			
			#node Math.003
			math_003 = _mn_utils_style_spheres_icosphere.nodes.new("ShaderNodeMath")
			math_003.name = "Math.003"
			math_003.operation = 'MULTIPLY'
			math_003.use_clamp = False
			
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
			math_002 = _mn_utils_style_spheres_icosphere.nodes.new("ShaderNodeMath")
			math_002.name = "Math.002"
			math_002.operation = 'ADD'
			math_002.use_clamp = False
			
			#node Integer
			integer = _mn_utils_style_spheres_icosphere.nodes.new("FunctionNodeInputInt")
			integer.name = "Integer"
			integer.integer = -1
			
			#node Domain Size
			domain_size_1 = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeAttributeDomainSize")
			domain_size_1.name = "Domain Size"
			domain_size_1.component = 'INSTANCES'
			
			#node Instance on Points
			instance_on_points_1 = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeInstanceOnPoints")
			instance_on_points_1.name = "Instance on Points"
			#Pick Instance
			instance_on_points_1.inputs[3].default_value = True
			#Rotation
			instance_on_points_1.inputs[5].default_value = (0.0, 0.0, 0.0)
			
			
			
			#Set parents
			ico_sphere_001.parent = frame_2
			ico_sphere_002.parent = frame_2
			ico_sphere_003.parent = frame_2
			geometry_to_instance.parent = frame_2
			ico_sphere_004.parent = frame_2
			ico_sphere_005.parent = frame_2
			reroute_002_1.parent = frame_2
			transform_geometry.parent = frame_2
			cube.parent = frame_2
			
			#Set locations
			frame_2.location = (0.0, 0.0)
			reroute_1.location = (-560.0, -40.0)
			math_001_2.location = (-140.0, 60.0)
			group_output_5.location = (835.407470703125, 359.5566711425781)
			group_input_002_1.location = (320.0, 260.0)
			set_shade_smooth_1.location = (500.0, 340.0)
			set_material_2.location = (660.0, 340.0)
			group_input_5.location = (-160.0, 240.0)
			reroute_001_1.location = (-480.0, 120.0)
			group_input_001_2.location = (-300.0, 60.0)
			ico_sphere_001.location = (-1180.0, 120.0)
			ico_sphere_002.location = (-1180.0, -20.0)
			ico_sphere_003.location = (-1180.0, -160.0)
			geometry_to_instance.location = (-940.0, 0.0)
			ico_sphere_004.location = (-1180.0, -300.0)
			ico_sphere_005.location = (-1180.0, -440.0)
			reroute_002_1.location = (-1040.0, 160.0)
			transform_geometry.location = (-1360.0, 200.0)
			cube.location = (-1520.0, 200.0)
			named_attribute_2.location = (-240.0, -340.0)
			radius.location = (-240.0, -480.0)
			math_3.location = (-60.0, -340.0)
			math_003.location = (100.0, -340.0)
			group_input_003_1.location = (-60.0, -520.0)
			math_002.location = (-140.0, -100.0)
			integer.location = (-320.0, -220.0)
			domain_size_1.location = (-320.0, -100.0)
			instance_on_points_1.location = (91.33897399902344, 216.86837768554688)
			
			#Set dimensions
			frame_2.width, frame_2.height = 800.0, 829.0
			reroute_1.width, reroute_1.height = 16.0, 100.0
			math_001_2.width, math_001_2.height = 140.0, 100.0
			group_output_5.width, group_output_5.height = 140.0, 100.0
			group_input_002_1.width, group_input_002_1.height = 140.0, 100.0
			set_shade_smooth_1.width, set_shade_smooth_1.height = 140.0, 100.0
			set_material_2.width, set_material_2.height = 140.0, 100.0
			group_input_5.width, group_input_5.height = 140.0, 100.0
			reroute_001_1.width, reroute_001_1.height = 16.0, 100.0
			group_input_001_2.width, group_input_001_2.height = 140.0, 100.0
			ico_sphere_001.width, ico_sphere_001.height = 140.0, 100.0
			ico_sphere_002.width, ico_sphere_002.height = 140.0, 100.0
			ico_sphere_003.width, ico_sphere_003.height = 140.0, 100.0
			geometry_to_instance.width, geometry_to_instance.height = 160.0, 100.0
			ico_sphere_004.width, ico_sphere_004.height = 140.0, 100.0
			ico_sphere_005.width, ico_sphere_005.height = 140.0, 100.0
			reroute_002_1.width, reroute_002_1.height = 16.0, 100.0
			transform_geometry.width, transform_geometry.height = 140.0, 100.0
			cube.width, cube.height = 140.0, 100.0
			named_attribute_2.width, named_attribute_2.height = 140.0, 100.0
			radius.width, radius.height = 140.0, 100.0
			math_3.width, math_3.height = 140.0, 100.0
			math_003.width, math_003.height = 140.0, 100.0
			group_input_003_1.width, group_input_003_1.height = 140.0, 100.0
			math_002.width, math_002.height = 140.0, 100.0
			integer.width, integer.height = 140.0, 100.0
			domain_size_1.width, domain_size_1.height = 140.0, 100.0
			instance_on_points_1.width, instance_on_points_1.height = 140.9404296875, 100.0
			
			#initialize _mn_utils_style_spheres_icosphere links
			#set_material_2.Geometry -> group_output_5.Instances
			_mn_utils_style_spheres_icosphere.links.new(set_material_2.outputs[0], group_output_5.inputs[0])
			#set_shade_smooth_1.Geometry -> set_material_2.Geometry
			_mn_utils_style_spheres_icosphere.links.new(set_shade_smooth_1.outputs[0], set_material_2.inputs[0])
			#group_input_5.Atoms -> instance_on_points_1.Points
			_mn_utils_style_spheres_icosphere.links.new(group_input_5.outputs[0], instance_on_points_1.inputs[0])
			#reroute_001_1.Output -> instance_on_points_1.Instance
			_mn_utils_style_spheres_icosphere.links.new(reroute_001_1.outputs[0], instance_on_points_1.inputs[2])
			#ico_sphere_005.Mesh -> geometry_to_instance.Geometry
			_mn_utils_style_spheres_icosphere.links.new(ico_sphere_005.outputs[0], geometry_to_instance.inputs[0])
			#math_001_2.Value -> instance_on_points_1.Instance Index
			_mn_utils_style_spheres_icosphere.links.new(math_001_2.outputs[0], instance_on_points_1.inputs[4])
			#group_input_001_2.Subdivisions -> math_001_2.Value
			_mn_utils_style_spheres_icosphere.links.new(group_input_001_2.outputs[3], math_001_2.inputs[0])
			#reroute_1.Output -> domain_size_1.Geometry
			_mn_utils_style_spheres_icosphere.links.new(reroute_1.outputs[0], domain_size_1.inputs[0])
			#geometry_to_instance.Instances -> reroute_1.Input
			_mn_utils_style_spheres_icosphere.links.new(geometry_to_instance.outputs[0], reroute_1.inputs[0])
			#named_attribute_2.Attribute -> math_3.Value
			_mn_utils_style_spheres_icosphere.links.new(named_attribute_2.outputs[0], math_3.inputs[0])
			#radius.Radius -> math_3.Value
			_mn_utils_style_spheres_icosphere.links.new(radius.outputs[0], math_3.inputs[1])
			#group_input_002_1.Material -> set_material_2.Material
			_mn_utils_style_spheres_icosphere.links.new(group_input_002_1.outputs[5], set_material_2.inputs[2])
			#instance_on_points_1.Instances -> set_shade_smooth_1.Geometry
			_mn_utils_style_spheres_icosphere.links.new(instance_on_points_1.outputs[0], set_shade_smooth_1.inputs[0])
			#group_input_002_1.Shade Smooth -> set_shade_smooth_1.Shade Smooth
			_mn_utils_style_spheres_icosphere.links.new(group_input_002_1.outputs[4], set_shade_smooth_1.inputs[2])
			#group_input_5.Selection -> instance_on_points_1.Selection
			_mn_utils_style_spheres_icosphere.links.new(group_input_5.outputs[1], instance_on_points_1.inputs[1])
			#math_3.Value -> math_003.Value
			_mn_utils_style_spheres_icosphere.links.new(math_3.outputs[0], math_003.inputs[0])
			#group_input_003_1.Radii -> math_003.Value
			_mn_utils_style_spheres_icosphere.links.new(group_input_003_1.outputs[2], math_003.inputs[1])
			#reroute_1.Output -> reroute_001_1.Input
			_mn_utils_style_spheres_icosphere.links.new(reroute_1.outputs[0], reroute_001_1.inputs[0])
			#math_003.Value -> instance_on_points_1.Scale
			_mn_utils_style_spheres_icosphere.links.new(math_003.outputs[0], instance_on_points_1.inputs[6])
			#cube.Mesh -> transform_geometry.Geometry
			_mn_utils_style_spheres_icosphere.links.new(cube.outputs[0], transform_geometry.inputs[0])
			#transform_geometry.Geometry -> reroute_002_1.Input
			_mn_utils_style_spheres_icosphere.links.new(transform_geometry.outputs[0], reroute_002_1.inputs[0])
			#domain_size_1.Instance Count -> math_002.Value
			_mn_utils_style_spheres_icosphere.links.new(domain_size_1.outputs[5], math_002.inputs[0])
			#integer.Integer -> math_002.Value
			_mn_utils_style_spheres_icosphere.links.new(integer.outputs[0], math_002.inputs[1])
			#math_002.Value -> math_001_2.Value
			_mn_utils_style_spheres_icosphere.links.new(math_002.outputs[0], math_001_2.inputs[1])
			#ico_sphere_004.Mesh -> geometry_to_instance.Geometry
			_mn_utils_style_spheres_icosphere.links.new(ico_sphere_004.outputs[0], geometry_to_instance.inputs[0])
			#ico_sphere_003.Mesh -> geometry_to_instance.Geometry
			_mn_utils_style_spheres_icosphere.links.new(ico_sphere_003.outputs[0], geometry_to_instance.inputs[0])
			#ico_sphere_002.Mesh -> geometry_to_instance.Geometry
			_mn_utils_style_spheres_icosphere.links.new(ico_sphere_002.outputs[0], geometry_to_instance.inputs[0])
			#ico_sphere_001.Mesh -> geometry_to_instance.Geometry
			_mn_utils_style_spheres_icosphere.links.new(ico_sphere_001.outputs[0], geometry_to_instance.inputs[0])
			#reroute_002_1.Output -> geometry_to_instance.Geometry
			_mn_utils_style_spheres_icosphere.links.new(reroute_002_1.outputs[0], geometry_to_instance.inputs[0])
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
			geometry_socket_1 = style_spheres.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_1.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket_5 = style_spheres.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_5.attribute_domain = 'POINT'
			atoms_socket_5.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket_4 = style_spheres.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_4.default_value = True
			selection_socket_4.attribute_domain = 'POINT'
			selection_socket_4.hide_value = True
			selection_socket_4.description = "Selection of atoms to apply this style to"
			
			#Panel Sphere
			sphere_panel = style_spheres.interface.new_panel("Sphere")
			#Socket Sphere As Mesh
			sphere_as_mesh_socket = style_spheres.interface.new_socket(name = "Sphere As Mesh", in_out='INPUT', socket_type = 'NodeSocketBool', parent = sphere_panel)
			sphere_as_mesh_socket.default_value = False
			sphere_as_mesh_socket.attribute_domain = 'POINT'
			sphere_as_mesh_socket.description = "Use Eevee or Cycles compatible atoms."
			
			#Socket Sphere Radii
			sphere_radii_socket = style_spheres.interface.new_socket(name = "Sphere Radii", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = sphere_panel)
			sphere_radii_socket.default_value = 0.800000011920929
			sphere_radii_socket.min_value = 0.0
			sphere_radii_socket.max_value = 2.0
			sphere_radii_socket.subtype = 'NONE'
			sphere_radii_socket.attribute_domain = 'POINT'
			sphere_radii_socket.description = "Scale the `vdw_radii` of the atoms."
			
			#Socket Sphere Subdivisions
			sphere_subdivisions_socket = style_spheres.interface.new_socket(name = "Sphere Subdivisions", in_out='INPUT', socket_type = 'NodeSocketInt', parent = sphere_panel)
			sphere_subdivisions_socket.default_value = 2
			sphere_subdivisions_socket.min_value = 0
			sphere_subdivisions_socket.max_value = 5
			sphere_subdivisions_socket.subtype = 'NONE'
			sphere_subdivisions_socket.attribute_domain = 'POINT'
			sphere_subdivisions_socket.description = "Subdivisions for Eevee compatible atoms."
			
			
			#Panel Material
			material_panel_1 = style_spheres.interface.new_panel("Material", default_closed=True)
			#Socket Shade Smooth
			shade_smooth_socket_2 = style_spheres.interface.new_socket(name = "Shade Smooth", in_out='INPUT', socket_type = 'NodeSocketBool', parent = material_panel_1)
			shade_smooth_socket_2.default_value = True
			shade_smooth_socket_2.attribute_domain = 'POINT'
			shade_smooth_socket_2.description = "Apply smooth shading to the created geometry"
			
			#Socket Material
			material_socket_3 = style_spheres.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial', parent = material_panel_1)
			material_socket_3.attribute_domain = 'POINT'
			material_socket_3.description = "Material to apply to the resulting geometry"
			
			
			
			#initialize style_spheres nodes
			#node Group Input
			group_input_6 = style_spheres.nodes.new("NodeGroupInput")
			group_input_6.name = "Group Input"
			
			#node Group Output
			group_output_6 = style_spheres.nodes.new("NodeGroupOutput")
			group_output_6.name = "Group Output"
			group_output_6.is_active_output = True
			
			#node Join Geometry
			join_geometry = style_spheres.nodes.new("GeometryNodeJoinGeometry")
			join_geometry.name = "Join Geometry"
			
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
			realize_instances_1 = style_spheres.nodes.new("GeometryNodeRealizeInstances")
			realize_instances_1.name = "Realize Instances"
			#Selection
			realize_instances_1.inputs[1].default_value = True
			#Realize All
			realize_instances_1.inputs[2].default_value = True
			#Depth
			realize_instances_1.inputs[3].default_value = 0
			
			
			
			
			#Set locations
			group_input_6.location = (-679.2061157226562, -54.561466217041016)
			group_output_6.location = (480.0, 40.0)
			join_geometry.location = (320.0, 40.0)
			separate_geometry_2.location = (-420.0, 80.0)
			group_014.location = (-200.0, -200.0)
			group_026.location = (-200.0, 60.0)
			realize_instances_1.location = (100.0, 60.0)
			
			#Set dimensions
			group_input_6.width, group_input_6.height = 140.0, 100.0
			group_output_6.width, group_output_6.height = 140.0, 100.0
			join_geometry.width, join_geometry.height = 140.0, 100.0
			separate_geometry_2.width, separate_geometry_2.height = 140.0, 100.0
			group_014.width, group_014.height = 277.9979248046875, 100.0
			group_026.width, group_026.height = 278.0207824707031, 100.0
			realize_instances_1.width, realize_instances_1.height = 140.0, 100.0
			
			#initialize style_spheres links
			#group_input_6.Atoms -> separate_geometry_2.Geometry
			style_spheres.links.new(group_input_6.outputs[0], separate_geometry_2.inputs[0])
			#group_input_6.Selection -> group_014.Selection
			style_spheres.links.new(group_input_6.outputs[1], group_014.inputs[1])
			#group_input_6.Selection -> group_026.Selection
			style_spheres.links.new(group_input_6.outputs[1], group_026.inputs[1])
			#group_input_6.Sphere As Mesh -> separate_geometry_2.Selection
			style_spheres.links.new(group_input_6.outputs[2], separate_geometry_2.inputs[1])
			#group_input_6.Sphere Radii -> group_014.Radii
			style_spheres.links.new(group_input_6.outputs[3], group_014.inputs[2])
			#group_input_6.Sphere Radii -> group_026.Radii
			style_spheres.links.new(group_input_6.outputs[3], group_026.inputs[2])
			#group_input_6.Sphere Subdivisions -> group_026.Subdivisions
			style_spheres.links.new(group_input_6.outputs[4], group_026.inputs[3])
			#group_input_6.Shade Smooth -> group_026.Shade Smooth
			style_spheres.links.new(group_input_6.outputs[5], group_026.inputs[4])
			#group_input_6.Material -> group_014.Material
			style_spheres.links.new(group_input_6.outputs[6], group_014.inputs[3])
			#group_input_6.Material -> group_026.Material
			style_spheres.links.new(group_input_6.outputs[6], group_026.inputs[5])
			#join_geometry.Geometry -> group_output_6.Geometry
			style_spheres.links.new(join_geometry.outputs[0], group_output_6.inputs[0])
			#realize_instances_1.Geometry -> join_geometry.Geometry
			style_spheres.links.new(realize_instances_1.outputs[0], join_geometry.inputs[0])
			#group_026.Instances -> realize_instances_1.Geometry
			style_spheres.links.new(group_026.outputs[0], realize_instances_1.inputs[0])
			#separate_geometry_2.Inverted -> group_014.Atoms
			style_spheres.links.new(separate_geometry_2.outputs[1], group_014.inputs[0])
			#separate_geometry_2.Selection -> group_026.Atoms
			style_spheres.links.new(separate_geometry_2.outputs[0], group_026.inputs[0])
			#group_014.Point Cloud -> join_geometry.Geometry
			style_spheres.links.new(group_014.outputs[0], join_geometry.inputs[0])
			return style_spheres

		style_spheres = style_spheres_node_group()

		#initialize style_ball_and_stick node group
		def style_ball_and_stick_node_group():
			style_ball_and_stick = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Style Ball and Stick")

			style_ball_and_stick.color_tag = 'GEOMETRY'
			style_ball_and_stick.description = ""

			style_ball_and_stick.is_modifier = True
			
			#style_ball_and_stick interface
			#Socket Geometry
			geometry_socket_2 = style_ball_and_stick.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_2.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket_6 = style_ball_and_stick.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_6.attribute_domain = 'POINT'
			atoms_socket_6.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Quality
			quality_socket = style_ball_and_stick.interface.new_socket(name = "Quality", in_out='INPUT', socket_type = 'NodeSocketInt')
			quality_socket.default_value = 2
			quality_socket.min_value = 0
			quality_socket.max_value = 2147483647
			quality_socket.subtype = 'NONE'
			quality_socket.attribute_domain = 'POINT'
			quality_socket.force_non_field = True
			
			#Socket Selection
			selection_socket_5 = style_ball_and_stick.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_5.default_value = True
			selection_socket_5.attribute_domain = 'POINT'
			selection_socket_5.hide_value = True
			selection_socket_5.description = "Selection of atoms to apply this style to"
			
			#Panel Sphere
			sphere_panel_1 = style_ball_and_stick.interface.new_panel("Sphere", default_closed=True)
			#Socket Sphere As Mesh
			sphere_as_mesh_socket_1 = style_ball_and_stick.interface.new_socket(name = "Sphere As Mesh", in_out='INPUT', socket_type = 'NodeSocketBool', parent = sphere_panel_1)
			sphere_as_mesh_socket_1.default_value = True
			sphere_as_mesh_socket_1.attribute_domain = 'POINT'
			sphere_as_mesh_socket_1.description = "Render spheres as point clouds"
			
			#Socket Sphere Radii
			sphere_radii_socket_1 = style_ball_and_stick.interface.new_socket(name = "Sphere Radii", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = sphere_panel_1)
			sphere_radii_socket_1.default_value = 0.30000001192092896
			sphere_radii_socket_1.min_value = 0.0
			sphere_radii_socket_1.max_value = 10000.0
			sphere_radii_socket_1.subtype = 'NONE'
			sphere_radii_socket_1.attribute_domain = 'POINT'
			sphere_radii_socket_1.description = "Scale the sphere radii"
			
			
			#Panel Bond
			bond_panel = style_ball_and_stick.interface.new_panel("Bond", default_closed=True)
			#Socket Bond Find
			bond_find_socket = style_ball_and_stick.interface.new_socket(name = "Bond Find", in_out='INPUT', socket_type = 'NodeSocketBool', parent = bond_panel)
			bond_find_socket.default_value = False
			bond_find_socket.attribute_domain = 'POINT'
			bond_find_socket.description = "Find possible bonds for the selected atoms based on a distance search. Unselected atoms maintain any bonds they already have"
			
			#Socket Bond Radius
			bond_radius_socket = style_ball_and_stick.interface.new_socket(name = "Bond Radius", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = bond_panel)
			bond_radius_socket.default_value = 0.30000001192092896
			bond_radius_socket.min_value = 0.0
			bond_radius_socket.max_value = 1.0
			bond_radius_socket.subtype = 'NONE'
			bond_radius_socket.attribute_domain = 'POINT'
			
			
			#Panel Material
			material_panel_2 = style_ball_and_stick.interface.new_panel("Material", default_closed=True)
			#Socket Color Blur
			color_blur_socket = style_ball_and_stick.interface.new_socket(name = "Color Blur", in_out='INPUT', socket_type = 'NodeSocketBool', parent = material_panel_2)
			color_blur_socket.default_value = False
			color_blur_socket.attribute_domain = 'POINT'
			
			#Socket Shade Smooth
			shade_smooth_socket_3 = style_ball_and_stick.interface.new_socket(name = "Shade Smooth", in_out='INPUT', socket_type = 'NodeSocketBool', parent = material_panel_2)
			shade_smooth_socket_3.default_value = True
			shade_smooth_socket_3.attribute_domain = 'POINT'
			shade_smooth_socket_3.description = "Apply smooth shading to the created geometry"
			
			#Socket Material
			material_socket_4 = style_ball_and_stick.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial', parent = material_panel_2)
			material_socket_4.attribute_domain = 'POINT'
			material_socket_4.description = "Material to apply to the resulting geometry"
			
			
			
			#initialize style_ball_and_stick nodes
			#node Group Output
			group_output_7 = style_ball_and_stick.nodes.new("NodeGroupOutput")
			group_output_7.name = "Group Output"
			group_output_7.is_active_output = True
			
			#node Join Geometry.001
			join_geometry_001 = style_ball_and_stick.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_001.name = "Join Geometry.001"
			
			#node Group Input.002
			group_input_002_2 = style_ball_and_stick.nodes.new("NodeGroupInput")
			group_input_002_2.name = "Group Input.002"
			
			#node Separate Geometry
			separate_geometry_3 = style_ball_and_stick.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_3.name = "Separate Geometry"
			separate_geometry_3.domain = 'POINT'
			
			#node Group Input
			group_input_7 = style_ball_and_stick.nodes.new("NodeGroupInput")
			group_input_7.name = "Group Input"
			group_input_7.outputs[1].hide = True
			group_input_7.outputs[3].hide = True
			group_input_7.outputs[4].hide = True
			group_input_7.outputs[5].hide = True
			group_input_7.outputs[6].hide = True
			group_input_7.outputs[7].hide = True
			group_input_7.outputs[8].hide = True
			group_input_7.outputs[9].hide = True
			group_input_7.outputs[10].hide = True
			
			#node Group.009
			group_009 = style_ball_and_stick.nodes.new("GeometryNodeGroup")
			group_009.name = "Group.009"
			group_009.node_tree = _mn_utils_style_sticks
			#Socket_0
			group_009.inputs[1].default_value = True
			#Input_15
			group_009.inputs[4].default_value = False
			
			#node Topology Find Bonds
			topology_find_bonds_1 = style_ball_and_stick.nodes.new("GeometryNodeGroup")
			topology_find_bonds_1.label = "Topology Find Bonds"
			topology_find_bonds_1.name = "Topology Find Bonds"
			topology_find_bonds_1.node_tree = topology_find_bonds
			#Input_35
			topology_find_bonds_1.inputs[1].default_value = True
			#Input_2
			topology_find_bonds_1.inputs[2].default_value = 1.0
			
			#node Separate Geometry.002
			separate_geometry_002 = style_ball_and_stick.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_002.name = "Separate Geometry.002"
			separate_geometry_002.domain = 'POINT'
			
			#node Join Geometry.002
			join_geometry_002 = style_ball_and_stick.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_002.name = "Join Geometry.002"
			
			#node Math
			math_4 = style_ball_and_stick.nodes.new("ShaderNodeMath")
			math_4.name = "Math"
			math_4.operation = 'MULTIPLY'
			math_4.use_clamp = False
			#Value_001
			math_4.inputs[1].default_value = 6.0
			
			#node Group
			group_3 = style_ball_and_stick.nodes.new("GeometryNodeGroup")
			group_3.name = "Group"
			group_3.node_tree = style_spheres
			#Input_1
			group_3.inputs[1].default_value = True
			
			#node Group Input.001
			group_input_001_3 = style_ball_and_stick.nodes.new("NodeGroupInput")
			group_input_001_3.name = "Group Input.001"
			group_input_001_3.outputs[0].hide = True
			group_input_001_3.outputs[2].hide = True
			group_input_001_3.outputs[5].hide = True
			group_input_001_3.outputs[6].hide = True
			group_input_001_3.outputs[7].hide = True
			group_input_001_3.outputs[10].hide = True
			
			
			
			
			#Set locations
			group_output_7.location = (560.0, -140.0)
			join_geometry_001.location = (360.0, -140.0)
			group_input_002_2.location = (-800.0, -520.0)
			separate_geometry_3.location = (-760.0, -20.0)
			group_input_7.location = (-960.0, -20.0)
			group_009.location = (-40.0, -380.0)
			topology_find_bonds_1.location = (-400.0, -300.0)
			separate_geometry_002.location = (-560.0, -380.0)
			join_geometry_002.location = (-200.0, -380.0)
			math_4.location = (-200.0, -500.0)
			group_3.location = (-20.0, 20.0)
			group_input_001_3.location = (-220.0, -100.0)
			
			#Set dimensions
			group_output_7.width, group_output_7.height = 140.0, 100.0
			join_geometry_001.width, join_geometry_001.height = 140.0, 100.0
			group_input_002_2.width, group_input_002_2.height = 140.0, 100.0
			separate_geometry_3.width, separate_geometry_3.height = 140.0, 100.0
			group_input_7.width, group_input_7.height = 140.0, 100.0
			group_009.width, group_009.height = 244.53131103515625, 100.0
			topology_find_bonds_1.width, topology_find_bonds_1.height = 180.0, 100.0
			separate_geometry_002.width, separate_geometry_002.height = 140.0, 100.0
			join_geometry_002.width, join_geometry_002.height = 140.0, 100.0
			math_4.width, math_4.height = 140.0, 100.0
			group_3.width, group_3.height = 201.75234985351562, 100.0
			group_input_001_3.width, group_input_001_3.height = 140.0, 100.0
			
			#initialize style_ball_and_stick links
			#join_geometry_002.Geometry -> group_009.Atoms
			style_ball_and_stick.links.new(join_geometry_002.outputs[0], group_009.inputs[0])
			#group_input_7.Atoms -> separate_geometry_3.Geometry
			style_ball_and_stick.links.new(group_input_7.outputs[0], separate_geometry_3.inputs[0])
			#group_input_7.Selection -> separate_geometry_3.Selection
			style_ball_and_stick.links.new(group_input_7.outputs[2], separate_geometry_3.inputs[1])
			#group_009.Geometry -> join_geometry_001.Geometry
			style_ball_and_stick.links.new(group_009.outputs[0], join_geometry_001.inputs[0])
			#join_geometry_001.Geometry -> group_output_7.Geometry
			style_ball_and_stick.links.new(join_geometry_001.outputs[0], group_output_7.inputs[0])
			#group_input_002_2.Material -> group_009.Material
			style_ball_and_stick.links.new(group_input_002_2.outputs[9], group_009.inputs[7])
			#group_input_002_2.Shade Smooth -> group_009.Shade Smooth
			style_ball_and_stick.links.new(group_input_002_2.outputs[8], group_009.inputs[6])
			#group_input_002_2.Bond Radius -> group_009.Radius
			style_ball_and_stick.links.new(group_input_002_2.outputs[6], group_009.inputs[2])
			#separate_geometry_3.Selection -> separate_geometry_002.Geometry
			style_ball_and_stick.links.new(separate_geometry_3.outputs[0], separate_geometry_002.inputs[0])
			#separate_geometry_002.Selection -> topology_find_bonds_1.Atoms
			style_ball_and_stick.links.new(separate_geometry_002.outputs[0], topology_find_bonds_1.inputs[0])
			#group_input_002_2.Bond Find -> separate_geometry_002.Selection
			style_ball_and_stick.links.new(group_input_002_2.outputs[5], separate_geometry_002.inputs[1])
			#separate_geometry_002.Inverted -> join_geometry_002.Geometry
			style_ball_and_stick.links.new(separate_geometry_002.outputs[1], join_geometry_002.inputs[0])
			#group_input_002_2.Quality -> math_4.Value
			style_ball_and_stick.links.new(group_input_002_2.outputs[1], math_4.inputs[0])
			#math_4.Value -> group_009.Resolution
			style_ball_and_stick.links.new(math_4.outputs[0], group_009.inputs[3])
			#separate_geometry_3.Selection -> group_3.Atoms
			style_ball_and_stick.links.new(separate_geometry_3.outputs[0], group_3.inputs[0])
			#group_input_001_3.Quality -> group_3.Sphere Subdivisions
			style_ball_and_stick.links.new(group_input_001_3.outputs[1], group_3.inputs[4])
			#group_input_001_3.Sphere As Mesh -> group_3.Sphere As Mesh
			style_ball_and_stick.links.new(group_input_001_3.outputs[3], group_3.inputs[2])
			#group_input_001_3.Sphere Radii -> group_3.Sphere Radii
			style_ball_and_stick.links.new(group_input_001_3.outputs[4], group_3.inputs[3])
			#group_input_001_3.Shade Smooth -> group_3.Shade Smooth
			style_ball_and_stick.links.new(group_input_001_3.outputs[8], group_3.inputs[5])
			#group_input_001_3.Material -> group_3.Material
			style_ball_and_stick.links.new(group_input_001_3.outputs[9], group_3.inputs[6])
			#group_input_002_2.Color Blur -> group_009.Interpolate Color
			style_ball_and_stick.links.new(group_input_002_2.outputs[7], group_009.inputs[5])
			#group_3.Geometry -> join_geometry_001.Geometry
			style_ball_and_stick.links.new(group_3.outputs[0], join_geometry_001.inputs[0])
			#topology_find_bonds_1.Atoms -> join_geometry_002.Geometry
			style_ball_and_stick.links.new(topology_find_bonds_1.outputs[0], join_geometry_002.inputs[0])
			return style_ball_and_stick

		style_ball_and_stick = style_ball_and_stick_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Style Ball and Stick", type = 'NODES')
		mod.node_group = style_ball_and_stick
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Style_Ball_and_Stick.bl_idname)
			
def register():
	bpy.utils.register_class(Style_Ball_and_Stick)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Style_Ball_and_Stick)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
