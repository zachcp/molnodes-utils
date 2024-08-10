bl_info = {
	"name" : "Style Preset 1",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Style_Preset_1(bpy.types.Operator):
	bl_idname = "node.style_preset_1"
	bl_label = "Style Preset 1"
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
			world_scale_socket.subtype = 'NONE'
			world_scale_socket.default_value = 0.009999999776482582
			world_scale_socket.min_value = -3.4028234663852886e+38
			world_scale_socket.max_value = 3.4028234663852886e+38
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
			selection_socket.attribute_domain = 'POINT'
			selection_socket.hide_value = True
			selection_socket.description = "Selection of atoms to apply this node to"
			
			#Socket Radius
			radius_socket = _mn_utils_style_sticks.interface.new_socket(name = "Radius", in_out='INPUT', socket_type = 'NodeSocketFloat')
			radius_socket.subtype = 'NONE'
			radius_socket.default_value = 0.30000001192092896
			radius_socket.min_value = 0.0
			radius_socket.max_value = 1.0
			radius_socket.attribute_domain = 'POINT'
			radius_socket.description = "Radius of the bond mesh."
			
			#Socket Resolution
			resolution_socket = _mn_utils_style_sticks.interface.new_socket(name = "Resolution", in_out='INPUT', socket_type = 'NodeSocketInt')
			resolution_socket.subtype = 'NONE'
			resolution_socket.default_value = 6
			resolution_socket.min_value = 3
			resolution_socket.max_value = 512
			resolution_socket.attribute_domain = 'POINT'
			resolution_socket.description = "Resolution of the created bond cylinders."
			
			#Socket Fill Caps
			fill_caps_socket = _mn_utils_style_sticks.interface.new_socket(name = "Fill Caps", in_out='INPUT', socket_type = 'NodeSocketBool')
			fill_caps_socket.attribute_domain = 'POINT'
			fill_caps_socket.description = "Fill the caps at each end of the bonds."
			
			#Socket Interpolate Color
			interpolate_color_socket = _mn_utils_style_sticks.interface.new_socket(name = "Interpolate Color", in_out='INPUT', socket_type = 'NodeSocketBool')
			interpolate_color_socket.attribute_domain = 'POINT'
			
			#Panel Material
			material_panel = _mn_utils_style_sticks.interface.new_panel("Material")
			#Socket Shade Smooth
			shade_smooth_socket = _mn_utils_style_sticks.interface.new_socket(name = "Shade Smooth", in_out='INPUT', socket_type = 'NodeSocketBool', parent = material_panel)
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
			selection_socket_1.attribute_domain = 'POINT'
			selection_socket_1.hide_value = True
			selection_socket_1.description = "Selection of atoms to apply this node to"
			
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
			selection_socket_2.attribute_domain = 'POINT'
			selection_socket_2.hide_value = True
			selection_socket_2.description = "Selection of atoms to apply this node to"
			
			#Socket Radii
			radii_socket = _mn_utils_style_spheres_points.interface.new_socket(name = "Radii", in_out='INPUT', socket_type = 'NodeSocketFloat')
			radii_socket.subtype = 'NONE'
			radii_socket.default_value = 0.800000011920929
			radii_socket.min_value = 0.0
			radii_socket.max_value = 10000.0
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
			selection_socket_3.attribute_domain = 'POINT'
			selection_socket_3.hide_value = True
			selection_socket_3.description = "Selection of atoms to apply this node to"
			
			#Socket Radii
			radii_socket_1 = _mn_utils_style_spheres_icosphere.interface.new_socket(name = "Radii", in_out='INPUT', socket_type = 'NodeSocketFloat')
			radii_socket_1.subtype = 'NONE'
			radii_socket_1.default_value = 0.800000011920929
			radii_socket_1.min_value = 0.0
			radii_socket_1.max_value = 10000.0
			radii_socket_1.attribute_domain = 'POINT'
			radii_socket_1.description = "Scale the VDW radii of the atoms."
			
			#Socket Subdivisions
			subdivisions_socket = _mn_utils_style_spheres_icosphere.interface.new_socket(name = "Subdivisions", in_out='INPUT', socket_type = 'NodeSocketInt')
			subdivisions_socket.subtype = 'NONE'
			subdivisions_socket.default_value = 2
			subdivisions_socket.min_value = 0
			subdivisions_socket.max_value = 5
			subdivisions_socket.attribute_domain = 'POINT'
			
			#Socket Shade Smooth
			shade_smooth_socket_1 = _mn_utils_style_spheres_icosphere.interface.new_socket(name = "Shade Smooth", in_out='INPUT', socket_type = 'NodeSocketBool')
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
			selection_socket_4.attribute_domain = 'POINT'
			selection_socket_4.hide_value = True
			selection_socket_4.description = "Selection of atoms to apply this style to"
			
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
			shade_smooth_socket_2 = style_spheres.interface.new_socket(name = "Shade Smooth", in_out='INPUT', socket_type = 'NodeSocketBool', parent = material_panel_1)
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
			quality_socket.subtype = 'NONE'
			quality_socket.default_value = 2
			quality_socket.min_value = 0
			quality_socket.max_value = 2147483647
			quality_socket.attribute_domain = 'POINT'
			quality_socket.force_non_field = True
			
			#Socket Selection
			selection_socket_5 = style_ball_and_stick.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_5.attribute_domain = 'POINT'
			selection_socket_5.hide_value = True
			selection_socket_5.description = "Selection of atoms to apply this style to"
			
			#Panel Sphere
			sphere_panel_1 = style_ball_and_stick.interface.new_panel("Sphere", default_closed=True)
			#Socket Sphere As Mesh
			sphere_as_mesh_socket_1 = style_ball_and_stick.interface.new_socket(name = "Sphere As Mesh", in_out='INPUT', socket_type = 'NodeSocketBool', parent = sphere_panel_1)
			sphere_as_mesh_socket_1.attribute_domain = 'POINT'
			sphere_as_mesh_socket_1.description = "Render spheres as point clouds"
			
			#Socket Sphere Radii
			sphere_radii_socket_1 = style_ball_and_stick.interface.new_socket(name = "Sphere Radii", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = sphere_panel_1)
			sphere_radii_socket_1.subtype = 'NONE'
			sphere_radii_socket_1.default_value = 0.30000001192092896
			sphere_radii_socket_1.min_value = 0.0
			sphere_radii_socket_1.max_value = 10000.0
			sphere_radii_socket_1.attribute_domain = 'POINT'
			sphere_radii_socket_1.description = "Scale the sphere radii"
			
			
			#Panel Bond
			bond_panel = style_ball_and_stick.interface.new_panel("Bond", default_closed=True)
			#Socket Bond Find
			bond_find_socket = style_ball_and_stick.interface.new_socket(name = "Bond Find", in_out='INPUT', socket_type = 'NodeSocketBool', parent = bond_panel)
			bond_find_socket.attribute_domain = 'POINT'
			bond_find_socket.description = "Find possible bonds for the selected atoms based on a distance search. Unselected atoms maintain any bonds they already have"
			
			#Socket Bond Radius
			bond_radius_socket = style_ball_and_stick.interface.new_socket(name = "Bond Radius", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = bond_panel)
			bond_radius_socket.subtype = 'NONE'
			bond_radius_socket.default_value = 0.30000001192092896
			bond_radius_socket.min_value = 0.0
			bond_radius_socket.max_value = 1.0
			bond_radius_socket.attribute_domain = 'POINT'
			
			
			#Panel Material
			material_panel_2 = style_ball_and_stick.interface.new_panel("Material", default_closed=True)
			#Socket Color Blur
			color_blur_socket = style_ball_and_stick.interface.new_socket(name = "Color Blur", in_out='INPUT', socket_type = 'NodeSocketBool', parent = material_panel_2)
			color_blur_socket.attribute_domain = 'POINT'
			
			#Socket Shade Smooth
			shade_smooth_socket_3 = style_ball_and_stick.interface.new_socket(name = "Shade Smooth", in_out='INPUT', socket_type = 'NodeSocketBool', parent = material_panel_2)
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

		#initialize _mn_constants_atom_name_peptide node group
		def _mn_constants_atom_name_peptide_node_group():
			_mn_constants_atom_name_peptide = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_constants_atom_name_peptide")

			_mn_constants_atom_name_peptide.color_tag = 'NONE'
			_mn_constants_atom_name_peptide.description = ""

			
			#_mn_constants_atom_name_peptide interface
			#Socket Backbone Lower
			backbone_lower_socket = _mn_constants_atom_name_peptide.interface.new_socket(name = "Backbone Lower", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			backbone_lower_socket.subtype = 'NONE'
			backbone_lower_socket.default_value = 0
			backbone_lower_socket.min_value = -2147483648
			backbone_lower_socket.max_value = 2147483647
			backbone_lower_socket.attribute_domain = 'POINT'
			
			#Socket Backbone Upper
			backbone_upper_socket = _mn_constants_atom_name_peptide.interface.new_socket(name = "Backbone Upper", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			backbone_upper_socket.subtype = 'NONE'
			backbone_upper_socket.default_value = 0
			backbone_upper_socket.min_value = -2147483648
			backbone_upper_socket.max_value = 2147483647
			backbone_upper_socket.attribute_domain = 'POINT'
			
			#Socket Side Chain Lower
			side_chain_lower_socket = _mn_constants_atom_name_peptide.interface.new_socket(name = "Side Chain Lower", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			side_chain_lower_socket.subtype = 'NONE'
			side_chain_lower_socket.default_value = 0
			side_chain_lower_socket.min_value = -2147483648
			side_chain_lower_socket.max_value = 2147483647
			side_chain_lower_socket.attribute_domain = 'POINT'
			
			#Socket Side Chain Upper
			side_chain_upper_socket = _mn_constants_atom_name_peptide.interface.new_socket(name = "Side Chain Upper", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			side_chain_upper_socket.subtype = 'NONE'
			side_chain_upper_socket.default_value = 0
			side_chain_upper_socket.min_value = -2147483648
			side_chain_upper_socket.max_value = 2147483647
			side_chain_upper_socket.attribute_domain = 'POINT'
			
			#Socket Alpha Carbon
			alpha_carbon_socket = _mn_constants_atom_name_peptide.interface.new_socket(name = "Alpha Carbon", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			alpha_carbon_socket.subtype = 'NONE'
			alpha_carbon_socket.default_value = 0
			alpha_carbon_socket.min_value = -2147483648
			alpha_carbon_socket.max_value = 2147483647
			alpha_carbon_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_constants_atom_name_peptide nodes
			#node Group Input
			group_input_8 = _mn_constants_atom_name_peptide.nodes.new("NodeGroupInput")
			group_input_8.name = "Group Input"
			
			#node Group Output
			group_output_8 = _mn_constants_atom_name_peptide.nodes.new("NodeGroupOutput")
			group_output_8.name = "Group Output"
			group_output_8.is_active_output = True
			
			#node Integer.001
			integer_001 = _mn_constants_atom_name_peptide.nodes.new("FunctionNodeInputInt")
			integer_001.name = "Integer.001"
			integer_001.integer = 49
			
			#node Integer.004
			integer_004 = _mn_constants_atom_name_peptide.nodes.new("FunctionNodeInputInt")
			integer_004.name = "Integer.004"
			integer_004.integer = 2
			
			#node Integer
			integer_1 = _mn_constants_atom_name_peptide.nodes.new("FunctionNodeInputInt")
			integer_1.name = "Integer"
			integer_1.integer = 5
			
			#node Integer.003
			integer_003 = _mn_constants_atom_name_peptide.nodes.new("FunctionNodeInputInt")
			integer_003.name = "Integer.003"
			integer_003.integer = 1
			
			#node Integer.002
			integer_002 = _mn_constants_atom_name_peptide.nodes.new("FunctionNodeInputInt")
			integer_002.name = "Integer.002"
			integer_002.integer = 4
			
			
			
			
			#Set locations
			group_input_8.location = (-200.0, 0.0)
			group_output_8.location = (260.0, 180.0)
			integer_001.location = (0.0, -50.0)
			integer_004.location = (0.0, -140.0)
			integer_1.location = (0.0, 40.0)
			integer_003.location = (0.0, 240.0)
			integer_002.location = (0.0, 140.0)
			
			#Set dimensions
			group_input_8.width, group_input_8.height = 140.0, 100.0
			group_output_8.width, group_output_8.height = 140.0, 100.0
			integer_001.width, integer_001.height = 140.0, 100.0
			integer_004.width, integer_004.height = 140.0, 100.0
			integer_1.width, integer_1.height = 140.0, 100.0
			integer_003.width, integer_003.height = 140.0, 100.0
			integer_002.width, integer_002.height = 140.0, 100.0
			
			#initialize _mn_constants_atom_name_peptide links
			#integer_003.Integer -> group_output_8.Backbone Lower
			_mn_constants_atom_name_peptide.links.new(integer_003.outputs[0], group_output_8.inputs[0])
			#integer_002.Integer -> group_output_8.Backbone Upper
			_mn_constants_atom_name_peptide.links.new(integer_002.outputs[0], group_output_8.inputs[1])
			#integer_1.Integer -> group_output_8.Side Chain Lower
			_mn_constants_atom_name_peptide.links.new(integer_1.outputs[0], group_output_8.inputs[2])
			#integer_001.Integer -> group_output_8.Side Chain Upper
			_mn_constants_atom_name_peptide.links.new(integer_001.outputs[0], group_output_8.inputs[3])
			#integer_004.Integer -> group_output_8.Alpha Carbon
			_mn_constants_atom_name_peptide.links.new(integer_004.outputs[0], group_output_8.inputs[4])
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
			group_input_9 = _mn_select_peptide.nodes.new("NodeGroupInput")
			group_input_9.name = "Group Input"
			
			#node Compare
			compare_1 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
			compare_1.name = "Compare"
			compare_1.data_type = 'INT'
			compare_1.mode = 'ELEMENT'
			compare_1.operation = 'GREATER_EQUAL'
			
			#node Compare.001
			compare_001 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'INT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'LESS_EQUAL'
			
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
			named_attribute_3 = _mn_select_peptide.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_3.name = "Named Attribute"
			named_attribute_3.data_type = 'INT'
			#Name
			named_attribute_3.inputs[0].default_value = "atom_name"
			
			#node Boolean Math.003
			boolean_math_003 = _mn_select_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003.name = "Boolean Math.003"
			boolean_math_003.operation = 'AND'
			
			#node Group Output
			group_output_9 = _mn_select_peptide.nodes.new("NodeGroupOutput")
			group_output_9.name = "Group Output"
			group_output_9.is_active_output = True
			
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
			group_4 = _mn_select_peptide.nodes.new("GeometryNodeGroup")
			group_4.name = "Group"
			group_4.node_tree = _mn_constants_atom_name_peptide
			
			#node Boolean Math
			boolean_math = _mn_select_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'OR'
			
			
			
			
			#Set locations
			group_input_9.location = (-460.0, 0.0)
			compare_1.location = (80.0, 80.0)
			compare_001.location = (80.0, -80.0)
			boolean_math_001.location = (260.0, 80.0)
			compare_002.location = (80.0, -240.0)
			compare_003.location = (80.0, -400.0)
			boolean_math_002.location = (260.0, -240.0)
			compare_004.location = (80.0, -560.0)
			named_attribute_3.location = (-360.0, -480.0)
			boolean_math_003.location = (260.0, -560.0)
			group_output_9.location = (666.1161499023438, -263.7054748535156)
			compare_005.location = (80.0, -720.0)
			compare_006.location = (260.0, -380.0)
			group_4.location = (-411.24090576171875, -312.71807861328125)
			boolean_math.location = (420.0, -240.0)
			
			#Set dimensions
			group_input_9.width, group_input_9.height = 140.0, 100.0
			compare_1.width, compare_1.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
			compare_002.width, compare_002.height = 153.86517333984375, 100.0
			compare_003.width, compare_003.height = 153.86517333984375, 100.0
			boolean_math_002.width, boolean_math_002.height = 140.0, 100.0
			compare_004.width, compare_004.height = 140.0, 100.0
			named_attribute_3.width, named_attribute_3.height = 140.0, 100.0
			boolean_math_003.width, boolean_math_003.height = 140.0, 100.0
			group_output_9.width, group_output_9.height = 140.0, 100.0
			compare_005.width, compare_005.height = 140.0, 100.0
			compare_006.width, compare_006.height = 140.0, 100.0
			group_4.width, group_4.height = 369.1165771484375, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			
			#initialize _mn_select_peptide links
			#compare_001.Result -> boolean_math_001.Boolean
			_mn_select_peptide.links.new(compare_001.outputs[0], boolean_math_001.inputs[1])
			#group_4.Backbone Lower -> compare_1.B
			_mn_select_peptide.links.new(group_4.outputs[0], compare_1.inputs[3])
			#named_attribute_3.Attribute -> compare_1.A
			_mn_select_peptide.links.new(named_attribute_3.outputs[0], compare_1.inputs[2])
			#compare_1.Result -> boolean_math_001.Boolean
			_mn_select_peptide.links.new(compare_1.outputs[0], boolean_math_001.inputs[0])
			#named_attribute_3.Attribute -> compare_001.A
			_mn_select_peptide.links.new(named_attribute_3.outputs[0], compare_001.inputs[2])
			#group_4.Backbone Upper -> compare_001.B
			_mn_select_peptide.links.new(group_4.outputs[1], compare_001.inputs[3])
			#boolean_math_001.Boolean -> group_output_9.Is Backbone
			_mn_select_peptide.links.new(boolean_math_001.outputs[0], group_output_9.inputs[0])
			#compare_003.Result -> boolean_math_002.Boolean
			_mn_select_peptide.links.new(compare_003.outputs[0], boolean_math_002.inputs[1])
			#named_attribute_3.Attribute -> compare_002.A
			_mn_select_peptide.links.new(named_attribute_3.outputs[0], compare_002.inputs[2])
			#compare_002.Result -> boolean_math_002.Boolean
			_mn_select_peptide.links.new(compare_002.outputs[0], boolean_math_002.inputs[0])
			#named_attribute_3.Attribute -> compare_003.A
			_mn_select_peptide.links.new(named_attribute_3.outputs[0], compare_003.inputs[2])
			#group_4.Side Chain Lower -> compare_002.B
			_mn_select_peptide.links.new(group_4.outputs[2], compare_002.inputs[3])
			#group_4.Side Chain Upper -> compare_003.B
			_mn_select_peptide.links.new(group_4.outputs[3], compare_003.inputs[3])
			#compare_005.Result -> boolean_math_003.Boolean
			_mn_select_peptide.links.new(compare_005.outputs[0], boolean_math_003.inputs[1])
			#named_attribute_3.Attribute -> compare_004.A
			_mn_select_peptide.links.new(named_attribute_3.outputs[0], compare_004.inputs[2])
			#compare_004.Result -> boolean_math_003.Boolean
			_mn_select_peptide.links.new(compare_004.outputs[0], boolean_math_003.inputs[0])
			#named_attribute_3.Attribute -> compare_005.A
			_mn_select_peptide.links.new(named_attribute_3.outputs[0], compare_005.inputs[2])
			#group_4.Backbone Lower -> compare_004.B
			_mn_select_peptide.links.new(group_4.outputs[0], compare_004.inputs[3])
			#group_4.Side Chain Upper -> compare_005.B
			_mn_select_peptide.links.new(group_4.outputs[3], compare_005.inputs[3])
			#boolean_math_003.Boolean -> group_output_9.Is Peptide
			_mn_select_peptide.links.new(boolean_math_003.outputs[0], group_output_9.inputs[2])
			#named_attribute_3.Attribute -> compare_006.A
			_mn_select_peptide.links.new(named_attribute_3.outputs[0], compare_006.inputs[2])
			#group_4.Alpha Carbon -> compare_006.B
			_mn_select_peptide.links.new(group_4.outputs[4], compare_006.inputs[3])
			#compare_006.Result -> group_output_9.Is Alpha Carbon
			_mn_select_peptide.links.new(compare_006.outputs[0], group_output_9.inputs[3])
			#boolean_math_002.Boolean -> boolean_math.Boolean
			_mn_select_peptide.links.new(boolean_math_002.outputs[0], boolean_math.inputs[0])
			#compare_006.Result -> boolean_math.Boolean
			_mn_select_peptide.links.new(compare_006.outputs[0], boolean_math.inputs[1])
			#boolean_math.Boolean -> group_output_9.Is Side Chain
			_mn_select_peptide.links.new(boolean_math.outputs[0], group_output_9.inputs[1])
			return _mn_select_peptide

		_mn_select_peptide = _mn_select_peptide_node_group()

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
			group_output_10 = fallback_boolean.nodes.new("NodeGroupOutput")
			group_output_10.name = "Group Output"
			group_output_10.is_active_output = True
			
			#node Group Input
			group_input_10 = fallback_boolean.nodes.new("NodeGroupInput")
			group_input_10.name = "Group Input"
			
			#node Named Attribute
			named_attribute_4 = fallback_boolean.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_4.name = "Named Attribute"
			named_attribute_4.data_type = 'BOOLEAN'
			
			#node Switch
			switch_3 = fallback_boolean.nodes.new("GeometryNodeSwitch")
			switch_3.name = "Switch"
			switch_3.input_type = 'BOOLEAN'
			
			
			
			
			#Set locations
			group_output_10.location = (276.6171569824219, 4.738137245178223)
			group_input_10.location = (-280.0, 0.0)
			named_attribute_4.location = (-94.73597717285156, 4.738137245178223)
			switch_3.location = (86.61715698242188, 4.738137245178223)
			
			#Set dimensions
			group_output_10.width, group_output_10.height = 140.0, 100.0
			group_input_10.width, group_input_10.height = 140.0, 100.0
			named_attribute_4.width, named_attribute_4.height = 140.0, 100.0
			switch_3.width, switch_3.height = 140.0, 100.0
			
			#initialize fallback_boolean links
			#named_attribute_4.Exists -> switch_3.Switch
			fallback_boolean.links.new(named_attribute_4.outputs[1], switch_3.inputs[0])
			#named_attribute_4.Attribute -> switch_3.True
			fallback_boolean.links.new(named_attribute_4.outputs[0], switch_3.inputs[2])
			#group_input_10.Fallback -> switch_3.False
			fallback_boolean.links.new(group_input_10.outputs[1], switch_3.inputs[1])
			#switch_3.Output -> group_output_10.Boolean
			fallback_boolean.links.new(switch_3.outputs[0], group_output_10.inputs[0])
			#group_input_10.Name -> named_attribute_4.Name
			fallback_boolean.links.new(group_input_10.outputs[0], named_attribute_4.inputs[0])
			return fallback_boolean

		fallback_boolean = fallback_boolean_node_group()

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
			inverted_socket = is_peptide.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket.attribute_domain = 'POINT'
			
			#Socket And
			and_socket = is_peptide.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket.attribute_domain = 'POINT'
			and_socket.hide_value = True
			
			#Socket Or
			or_socket = is_peptide.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket.attribute_domain = 'POINT'
			or_socket.hide_value = True
			
			
			#initialize is_peptide nodes
			#node Group Input
			group_input_11 = is_peptide.nodes.new("NodeGroupInput")
			group_input_11.name = "Group Input"
			
			#node Boolean Math.001
			boolean_math_001_1 = is_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_1.name = "Boolean Math.001"
			boolean_math_001_1.operation = 'AND'
			
			#node Group
			group_5 = is_peptide.nodes.new("GeometryNodeGroup")
			group_5.name = "Group"
			group_5.node_tree = _mn_select_peptide
			
			#node Group Output
			group_output_11 = is_peptide.nodes.new("NodeGroupOutput")
			group_output_11.name = "Group Output"
			group_output_11.is_active_output = True
			
			#node Group.001
			group_001 = is_peptide.nodes.new("GeometryNodeGroup")
			group_001.name = "Group.001"
			group_001.node_tree = fallback_boolean
			#Socket_2
			group_001.inputs[0].default_value = "is_peptide"
			
			#node Boolean Math.002
			boolean_math_002_1 = is_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_1.name = "Boolean Math.002"
			boolean_math_002_1.operation = 'OR'
			
			#node Boolean Math
			boolean_math_1 = is_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math_1.name = "Boolean Math"
			boolean_math_1.operation = 'NOT'
			
			
			
			
			#Set locations
			group_input_11.location = (-200.0, 0.0)
			boolean_math_001_1.location = (-40.0, 0.0)
			group_5.location = (-340.0, -140.0)
			group_output_11.location = (320.0, 0.0)
			group_001.location = (-40.0, -140.0)
			boolean_math_002_1.location = (140.0, 5.243539333343506)
			boolean_math_1.location = (140.0, -120.0)
			
			#Set dimensions
			group_input_11.width, group_input_11.height = 140.0, 100.0
			boolean_math_001_1.width, boolean_math_001_1.height = 140.0, 100.0
			group_5.width, group_5.height = 247.90924072265625, 100.0
			group_output_11.width, group_output_11.height = 140.0, 100.0
			group_001.width, group_001.height = 140.0, 100.0
			boolean_math_002_1.width, boolean_math_002_1.height = 140.0, 100.0
			boolean_math_1.width, boolean_math_1.height = 140.0, 100.0
			
			#initialize is_peptide links
			#boolean_math_002_1.Boolean -> group_output_11.Selection
			is_peptide.links.new(boolean_math_002_1.outputs[0], group_output_11.inputs[0])
			#group_input_11.And -> boolean_math_001_1.Boolean
			is_peptide.links.new(group_input_11.outputs[0], boolean_math_001_1.inputs[0])
			#group_5.Is Peptide -> group_001.Fallback
			is_peptide.links.new(group_5.outputs[2], group_001.inputs[1])
			#group_001.Boolean -> boolean_math_001_1.Boolean
			is_peptide.links.new(group_001.outputs[0], boolean_math_001_1.inputs[1])
			#boolean_math_001_1.Boolean -> boolean_math_002_1.Boolean
			is_peptide.links.new(boolean_math_001_1.outputs[0], boolean_math_002_1.inputs[0])
			#group_input_11.Or -> boolean_math_002_1.Boolean
			is_peptide.links.new(group_input_11.outputs[1], boolean_math_002_1.inputs[1])
			#boolean_math_002_1.Boolean -> boolean_math_1.Boolean
			is_peptide.links.new(boolean_math_002_1.outputs[0], boolean_math_1.inputs[0])
			#boolean_math_1.Boolean -> group_output_11.Inverted
			is_peptide.links.new(boolean_math_1.outputs[0], group_output_11.inputs[1])
			return is_peptide

		is_peptide = is_peptide_node_group()

		#initialize _mn_constants_atom_name_nucleic node group
		def _mn_constants_atom_name_nucleic_node_group():
			_mn_constants_atom_name_nucleic = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_constants_atom_name_nucleic")

			_mn_constants_atom_name_nucleic.color_tag = 'NONE'
			_mn_constants_atom_name_nucleic.description = ""

			
			#_mn_constants_atom_name_nucleic interface
			#Socket Backbone Lower
			backbone_lower_socket_1 = _mn_constants_atom_name_nucleic.interface.new_socket(name = "Backbone Lower", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			backbone_lower_socket_1.subtype = 'NONE'
			backbone_lower_socket_1.default_value = 0
			backbone_lower_socket_1.min_value = -2147483648
			backbone_lower_socket_1.max_value = 2147483647
			backbone_lower_socket_1.attribute_domain = 'POINT'
			
			#Socket Backbone Upper
			backbone_upper_socket_1 = _mn_constants_atom_name_nucleic.interface.new_socket(name = "Backbone Upper", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			backbone_upper_socket_1.subtype = 'NONE'
			backbone_upper_socket_1.default_value = 0
			backbone_upper_socket_1.min_value = -2147483648
			backbone_upper_socket_1.max_value = 2147483647
			backbone_upper_socket_1.attribute_domain = 'POINT'
			
			#Socket Side Chain Lower
			side_chain_lower_socket_1 = _mn_constants_atom_name_nucleic.interface.new_socket(name = "Side Chain Lower", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			side_chain_lower_socket_1.subtype = 'NONE'
			side_chain_lower_socket_1.default_value = 0
			side_chain_lower_socket_1.min_value = -2147483648
			side_chain_lower_socket_1.max_value = 2147483647
			side_chain_lower_socket_1.attribute_domain = 'POINT'
			
			#Socket Side Chain Upper
			side_chain_upper_socket_1 = _mn_constants_atom_name_nucleic.interface.new_socket(name = "Side Chain Upper", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			side_chain_upper_socket_1.subtype = 'NONE'
			side_chain_upper_socket_1.default_value = 0
			side_chain_upper_socket_1.min_value = -2147483648
			side_chain_upper_socket_1.max_value = 2147483647
			side_chain_upper_socket_1.attribute_domain = 'POINT'
			
			#Socket Side Chain Joint Carbon
			side_chain_joint_carbon_socket = _mn_constants_atom_name_nucleic.interface.new_socket(name = "Side Chain Joint Carbon", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			side_chain_joint_carbon_socket.subtype = 'NONE'
			side_chain_joint_carbon_socket.default_value = 0
			side_chain_joint_carbon_socket.min_value = -2147483648
			side_chain_joint_carbon_socket.max_value = 2147483647
			side_chain_joint_carbon_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_constants_atom_name_nucleic nodes
			#node Group Output
			group_output_12 = _mn_constants_atom_name_nucleic.nodes.new("NodeGroupOutput")
			group_output_12.name = "Group Output"
			group_output_12.is_active_output = True
			
			#node Group Input
			group_input_12 = _mn_constants_atom_name_nucleic.nodes.new("NodeGroupInput")
			group_input_12.name = "Group Input"
			
			#node Integer
			integer_2 = _mn_constants_atom_name_nucleic.nodes.new("FunctionNodeInputInt")
			integer_2.name = "Integer"
			integer_2.integer = 61
			
			#node Integer.002
			integer_002_1 = _mn_constants_atom_name_nucleic.nodes.new("FunctionNodeInputInt")
			integer_002_1.name = "Integer.002"
			integer_002_1.integer = 50
			
			#node Integer.003
			integer_003_1 = _mn_constants_atom_name_nucleic.nodes.new("FunctionNodeInputInt")
			integer_003_1.name = "Integer.003"
			integer_003_1.integer = 61
			
			#node Integer.001
			integer_001_1 = _mn_constants_atom_name_nucleic.nodes.new("FunctionNodeInputInt")
			integer_001_1.name = "Integer.001"
			integer_001_1.integer = 77
			
			#node Integer.004
			integer_004_1 = _mn_constants_atom_name_nucleic.nodes.new("FunctionNodeInputInt")
			integer_004_1.name = "Integer.004"
			integer_004_1.integer = 54
			
			
			
			
			#Set locations
			group_output_12.location = (190.0, 0.0)
			group_input_12.location = (-200.0, 0.0)
			integer_2.location = (0.0, -100.0)
			integer_002_1.location = (0.0, 100.0)
			integer_003_1.location = (0.0, 0.0)
			integer_001_1.location = (0.0, -200.0)
			integer_004_1.location = (0.0, -300.0)
			
			#Set dimensions
			group_output_12.width, group_output_12.height = 140.0, 100.0
			group_input_12.width, group_input_12.height = 140.0, 100.0
			integer_2.width, integer_2.height = 140.0, 100.0
			integer_002_1.width, integer_002_1.height = 140.0, 100.0
			integer_003_1.width, integer_003_1.height = 140.0, 100.0
			integer_001_1.width, integer_001_1.height = 140.0, 100.0
			integer_004_1.width, integer_004_1.height = 140.0, 100.0
			
			#initialize _mn_constants_atom_name_nucleic links
			#integer_2.Integer -> group_output_12.Side Chain Lower
			_mn_constants_atom_name_nucleic.links.new(integer_2.outputs[0], group_output_12.inputs[2])
			#integer_001_1.Integer -> group_output_12.Side Chain Upper
			_mn_constants_atom_name_nucleic.links.new(integer_001_1.outputs[0], group_output_12.inputs[3])
			#integer_002_1.Integer -> group_output_12.Backbone Lower
			_mn_constants_atom_name_nucleic.links.new(integer_002_1.outputs[0], group_output_12.inputs[0])
			#integer_003_1.Integer -> group_output_12.Backbone Upper
			_mn_constants_atom_name_nucleic.links.new(integer_003_1.outputs[0], group_output_12.inputs[1])
			#integer_004_1.Integer -> group_output_12.Side Chain Joint Carbon
			_mn_constants_atom_name_nucleic.links.new(integer_004_1.outputs[0], group_output_12.inputs[4])
			return _mn_constants_atom_name_nucleic

		_mn_constants_atom_name_nucleic = _mn_constants_atom_name_nucleic_node_group()

		#initialize _mn_select_nucleic node group
		def _mn_select_nucleic_node_group():
			_mn_select_nucleic = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_select_nucleic")

			_mn_select_nucleic.color_tag = 'NONE'
			_mn_select_nucleic.description = ""

			
			#_mn_select_nucleic interface
			#Socket Is Backbone
			is_backbone_socket_1 = _mn_select_nucleic.interface.new_socket(name = "Is Backbone", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_backbone_socket_1.attribute_domain = 'POINT'
			is_backbone_socket_1.description = "True for atoms that are part of the sugar-phosphate backbone for the nucleotides"
			
			#Socket Is Side Chain
			is_side_chain_socket_1 = _mn_select_nucleic.interface.new_socket(name = "Is Side Chain", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_side_chain_socket_1.attribute_domain = 'POINT'
			is_side_chain_socket_1.description = "True for atoms that are part of the bases for nucleotides."
			
			#Socket Is Nucleic
			is_nucleic_socket = _mn_select_nucleic.interface.new_socket(name = "Is Nucleic", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_nucleic_socket.attribute_domain = 'POINT'
			is_nucleic_socket.description = "True if the atoms are part of a nucleic acid"
			
			
			#initialize _mn_select_nucleic nodes
			#node Group Input
			group_input_13 = _mn_select_nucleic.nodes.new("NodeGroupInput")
			group_input_13.name = "Group Input"
			
			#node Compare
			compare_2 = _mn_select_nucleic.nodes.new("FunctionNodeCompare")
			compare_2.name = "Compare"
			compare_2.data_type = 'INT'
			compare_2.mode = 'ELEMENT'
			compare_2.operation = 'GREATER_EQUAL'
			
			#node Compare.001
			compare_001_1 = _mn_select_nucleic.nodes.new("FunctionNodeCompare")
			compare_001_1.name = "Compare.001"
			compare_001_1.data_type = 'INT'
			compare_001_1.mode = 'ELEMENT'
			compare_001_1.operation = 'LESS_EQUAL'
			
			#node Boolean Math.001
			boolean_math_001_2 = _mn_select_nucleic.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_2.name = "Boolean Math.001"
			boolean_math_001_2.operation = 'AND'
			
			#node Group Output
			group_output_13 = _mn_select_nucleic.nodes.new("NodeGroupOutput")
			group_output_13.name = "Group Output"
			group_output_13.is_active_output = True
			
			#node Compare.002
			compare_002_1 = _mn_select_nucleic.nodes.new("FunctionNodeCompare")
			compare_002_1.name = "Compare.002"
			compare_002_1.data_type = 'INT'
			compare_002_1.mode = 'ELEMENT'
			compare_002_1.operation = 'GREATER_EQUAL'
			
			#node Compare.003
			compare_003_1 = _mn_select_nucleic.nodes.new("FunctionNodeCompare")
			compare_003_1.name = "Compare.003"
			compare_003_1.data_type = 'INT'
			compare_003_1.mode = 'ELEMENT'
			compare_003_1.operation = 'LESS_EQUAL'
			
			#node Boolean Math.002
			boolean_math_002_2 = _mn_select_nucleic.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_2.name = "Boolean Math.002"
			boolean_math_002_2.operation = 'AND'
			
			#node Compare.004
			compare_004_1 = _mn_select_nucleic.nodes.new("FunctionNodeCompare")
			compare_004_1.name = "Compare.004"
			compare_004_1.data_type = 'INT'
			compare_004_1.mode = 'ELEMENT'
			compare_004_1.operation = 'GREATER_EQUAL'
			
			#node Compare.005
			compare_005_1 = _mn_select_nucleic.nodes.new("FunctionNodeCompare")
			compare_005_1.name = "Compare.005"
			compare_005_1.data_type = 'INT'
			compare_005_1.mode = 'ELEMENT'
			compare_005_1.operation = 'LESS_EQUAL'
			
			#node Boolean Math.003
			boolean_math_003_1 = _mn_select_nucleic.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003_1.name = "Boolean Math.003"
			boolean_math_003_1.operation = 'AND'
			
			#node Named Attribute
			named_attribute_5 = _mn_select_nucleic.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_5.name = "Named Attribute"
			named_attribute_5.data_type = 'INT'
			#Name
			named_attribute_5.inputs[0].default_value = "atom_name"
			
			#node Group
			group_6 = _mn_select_nucleic.nodes.new("GeometryNodeGroup")
			group_6.name = "Group"
			group_6.node_tree = _mn_constants_atom_name_nucleic
			
			
			
			
			#Set locations
			group_input_13.location = (-460.0, 0.0)
			compare_2.location = (80.0, 80.0)
			compare_001_1.location = (80.0, -80.0)
			boolean_math_001_2.location = (260.0, 80.0)
			group_output_13.location = (580.0, 60.0)
			compare_002_1.location = (80.0, -260.0)
			compare_003_1.location = (80.0, -420.0)
			boolean_math_002_2.location = (260.0, -260.0)
			compare_004_1.location = (80.0, -580.0)
			compare_005_1.location = (80.0, -740.0)
			boolean_math_003_1.location = (260.0, -580.0)
			named_attribute_5.location = (-260.0, -280.0)
			group_6.location = (-480.0, -100.0)
			
			#Set dimensions
			group_input_13.width, group_input_13.height = 140.0, 100.0
			compare_2.width, compare_2.height = 140.0, 100.0
			compare_001_1.width, compare_001_1.height = 140.0, 100.0
			boolean_math_001_2.width, boolean_math_001_2.height = 140.0, 100.0
			group_output_13.width, group_output_13.height = 140.0, 100.0
			compare_002_1.width, compare_002_1.height = 140.0, 100.0
			compare_003_1.width, compare_003_1.height = 140.0, 100.0
			boolean_math_002_2.width, boolean_math_002_2.height = 140.0, 100.0
			compare_004_1.width, compare_004_1.height = 140.0, 100.0
			compare_005_1.width, compare_005_1.height = 140.0, 100.0
			boolean_math_003_1.width, boolean_math_003_1.height = 140.0, 100.0
			named_attribute_5.width, named_attribute_5.height = 140.0, 100.0
			group_6.width, group_6.height = 365.8858337402344, 100.0
			
			#initialize _mn_select_nucleic links
			#compare_001_1.Result -> boolean_math_001_2.Boolean
			_mn_select_nucleic.links.new(compare_001_1.outputs[0], boolean_math_001_2.inputs[1])
			#named_attribute_5.Attribute -> compare_2.A
			_mn_select_nucleic.links.new(named_attribute_5.outputs[0], compare_2.inputs[2])
			#compare_2.Result -> boolean_math_001_2.Boolean
			_mn_select_nucleic.links.new(compare_2.outputs[0], boolean_math_001_2.inputs[0])
			#named_attribute_5.Attribute -> compare_001_1.A
			_mn_select_nucleic.links.new(named_attribute_5.outputs[0], compare_001_1.inputs[2])
			#boolean_math_001_2.Boolean -> group_output_13.Is Backbone
			_mn_select_nucleic.links.new(boolean_math_001_2.outputs[0], group_output_13.inputs[0])
			#group_6.Backbone Lower -> compare_2.B
			_mn_select_nucleic.links.new(group_6.outputs[0], compare_2.inputs[3])
			#group_6.Backbone Upper -> compare_001_1.B
			_mn_select_nucleic.links.new(group_6.outputs[1], compare_001_1.inputs[3])
			#compare_003_1.Result -> boolean_math_002_2.Boolean
			_mn_select_nucleic.links.new(compare_003_1.outputs[0], boolean_math_002_2.inputs[1])
			#compare_002_1.Result -> boolean_math_002_2.Boolean
			_mn_select_nucleic.links.new(compare_002_1.outputs[0], boolean_math_002_2.inputs[0])
			#group_6.Side Chain Lower -> compare_002_1.B
			_mn_select_nucleic.links.new(group_6.outputs[2], compare_002_1.inputs[3])
			#group_6.Side Chain Upper -> compare_003_1.B
			_mn_select_nucleic.links.new(group_6.outputs[3], compare_003_1.inputs[3])
			#boolean_math_002_2.Boolean -> group_output_13.Is Side Chain
			_mn_select_nucleic.links.new(boolean_math_002_2.outputs[0], group_output_13.inputs[1])
			#named_attribute_5.Attribute -> compare_002_1.A
			_mn_select_nucleic.links.new(named_attribute_5.outputs[0], compare_002_1.inputs[2])
			#named_attribute_5.Attribute -> compare_003_1.A
			_mn_select_nucleic.links.new(named_attribute_5.outputs[0], compare_003_1.inputs[2])
			#compare_005_1.Result -> boolean_math_003_1.Boolean
			_mn_select_nucleic.links.new(compare_005_1.outputs[0], boolean_math_003_1.inputs[1])
			#compare_004_1.Result -> boolean_math_003_1.Boolean
			_mn_select_nucleic.links.new(compare_004_1.outputs[0], boolean_math_003_1.inputs[0])
			#group_6.Backbone Lower -> compare_004_1.B
			_mn_select_nucleic.links.new(group_6.outputs[0], compare_004_1.inputs[3])
			#named_attribute_5.Attribute -> compare_004_1.A
			_mn_select_nucleic.links.new(named_attribute_5.outputs[0], compare_004_1.inputs[2])
			#group_6.Side Chain Upper -> compare_005_1.B
			_mn_select_nucleic.links.new(group_6.outputs[3], compare_005_1.inputs[3])
			#named_attribute_5.Attribute -> compare_005_1.A
			_mn_select_nucleic.links.new(named_attribute_5.outputs[0], compare_005_1.inputs[2])
			#boolean_math_003_1.Boolean -> group_output_13.Is Nucleic
			_mn_select_nucleic.links.new(boolean_math_003_1.outputs[0], group_output_13.inputs[2])
			return _mn_select_nucleic

		_mn_select_nucleic = _mn_select_nucleic_node_group()

		#initialize is_nucleic node group
		def is_nucleic_node_group():
			is_nucleic = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Is Nucleic")

			is_nucleic.color_tag = 'INPUT'
			is_nucleic.description = ""

			
			#is_nucleic interface
			#Socket Selection
			selection_socket_7 = is_nucleic.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket_7.attribute_domain = 'POINT'
			selection_socket_7.description = "True if atoms are part of a nucleic acid"
			
			#Socket Inverted
			inverted_socket_1 = is_nucleic.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket_1.attribute_domain = 'POINT'
			
			#Socket And
			and_socket_1 = is_nucleic.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket_1.attribute_domain = 'POINT'
			and_socket_1.hide_value = True
			
			#Socket Or
			or_socket_1 = is_nucleic.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket_1.attribute_domain = 'POINT'
			or_socket_1.hide_value = True
			
			
			#initialize is_nucleic nodes
			#node Group Input
			group_input_14 = is_nucleic.nodes.new("NodeGroupInput")
			group_input_14.name = "Group Input"
			
			#node Boolean Math.001
			boolean_math_001_3 = is_nucleic.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_3.name = "Boolean Math.001"
			boolean_math_001_3.operation = 'AND'
			
			#node Group Output
			group_output_14 = is_nucleic.nodes.new("NodeGroupOutput")
			group_output_14.name = "Group Output"
			group_output_14.is_active_output = True
			
			#node Group
			group_7 = is_nucleic.nodes.new("GeometryNodeGroup")
			group_7.name = "Group"
			group_7.node_tree = _mn_select_nucleic
			
			#node Group.001
			group_001_1 = is_nucleic.nodes.new("GeometryNodeGroup")
			group_001_1.name = "Group.001"
			group_001_1.node_tree = fallback_boolean
			#Socket_2
			group_001_1.inputs[0].default_value = "is_nucleic"
			
			#node Boolean Math.002
			boolean_math_002_3 = is_nucleic.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_3.name = "Boolean Math.002"
			boolean_math_002_3.operation = 'OR'
			
			#node Boolean Math
			boolean_math_2 = is_nucleic.nodes.new("FunctionNodeBooleanMath")
			boolean_math_2.name = "Boolean Math"
			boolean_math_2.operation = 'NOT'
			
			
			
			
			#Set locations
			group_input_14.location = (-280.0, -40.0)
			boolean_math_001_3.location = (-40.0, 0.0)
			group_output_14.location = (320.0000305175781, 0.0)
			group_7.location = (-620.0, -160.0)
			group_001_1.location = (-340.0, -160.0)
			boolean_math_002_3.location = (140.0, 0.0)
			boolean_math_2.location = (140.0, -140.0)
			
			#Set dimensions
			group_input_14.width, group_input_14.height = 140.0, 100.0
			boolean_math_001_3.width, boolean_math_001_3.height = 140.0, 100.0
			group_output_14.width, group_output_14.height = 140.0, 100.0
			group_7.width, group_7.height = 247.90924072265625, 100.0
			group_001_1.width, group_001_1.height = 232.0133056640625, 100.0
			boolean_math_002_3.width, boolean_math_002_3.height = 140.0, 100.0
			boolean_math_2.width, boolean_math_2.height = 140.0, 100.0
			
			#initialize is_nucleic links
			#boolean_math_002_3.Boolean -> group_output_14.Selection
			is_nucleic.links.new(boolean_math_002_3.outputs[0], group_output_14.inputs[0])
			#group_input_14.And -> boolean_math_001_3.Boolean
			is_nucleic.links.new(group_input_14.outputs[0], boolean_math_001_3.inputs[0])
			#group_7.Is Nucleic -> group_001_1.Fallback
			is_nucleic.links.new(group_7.outputs[2], group_001_1.inputs[1])
			#group_001_1.Boolean -> boolean_math_001_3.Boolean
			is_nucleic.links.new(group_001_1.outputs[0], boolean_math_001_3.inputs[1])
			#boolean_math_001_3.Boolean -> boolean_math_002_3.Boolean
			is_nucleic.links.new(boolean_math_001_3.outputs[0], boolean_math_002_3.inputs[0])
			#group_input_14.Or -> boolean_math_002_3.Boolean
			is_nucleic.links.new(group_input_14.outputs[1], boolean_math_002_3.inputs[1])
			#boolean_math_002_3.Boolean -> boolean_math_2.Boolean
			is_nucleic.links.new(boolean_math_002_3.outputs[0], boolean_math_2.inputs[0])
			#boolean_math_2.Boolean -> group_output_14.Inverted
			is_nucleic.links.new(boolean_math_2.outputs[0], group_output_14.inputs[1])
			return is_nucleic

		is_nucleic = is_nucleic_node_group()

		#initialize separate_polymers node group
		def separate_polymers_node_group():
			separate_polymers = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Separate Polymers")

			separate_polymers.color_tag = 'GEOMETRY'
			separate_polymers.description = ""

			separate_polymers.is_modifier = True
			
			#separate_polymers interface
			#Socket Peptide
			peptide_socket = separate_polymers.interface.new_socket(name = "Peptide", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			peptide_socket.attribute_domain = 'POINT'
			
			#Socket Nucleic
			nucleic_socket = separate_polymers.interface.new_socket(name = "Nucleic", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			nucleic_socket.attribute_domain = 'POINT'
			
			#Socket Other
			other_socket = separate_polymers.interface.new_socket(name = "Other", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			other_socket.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket_7 = separate_polymers.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_7.attribute_domain = 'POINT'
			atoms_socket_7.description = "Atomic geometry that contains vertices and edges"
			
			
			#initialize separate_polymers nodes
			#node Group Input
			group_input_15 = separate_polymers.nodes.new("NodeGroupInput")
			group_input_15.name = "Group Input"
			
			#node Group Output
			group_output_15 = separate_polymers.nodes.new("NodeGroupOutput")
			group_output_15.name = "Group Output"
			group_output_15.is_active_output = True
			
			#node Separate Geometry
			separate_geometry_4 = separate_polymers.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_4.name = "Separate Geometry"
			separate_geometry_4.domain = 'POINT'
			
			#node Separate Geometry.001
			separate_geometry_001 = separate_polymers.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_001.name = "Separate Geometry.001"
			separate_geometry_001.domain = 'POINT'
			
			#node Group
			group_8 = separate_polymers.nodes.new("GeometryNodeGroup")
			group_8.name = "Group"
			group_8.node_tree = is_peptide
			#Socket_1
			group_8.inputs[0].default_value = True
			#Socket_3
			group_8.inputs[1].default_value = False
			
			#node Group.001
			group_001_2 = separate_polymers.nodes.new("GeometryNodeGroup")
			group_001_2.name = "Group.001"
			group_001_2.node_tree = is_nucleic
			#Socket_1
			group_001_2.inputs[0].default_value = True
			#Socket_3
			group_001_2.inputs[1].default_value = False
			
			
			
			
			#Set locations
			group_input_15.location = (-360.0, 220.0)
			group_output_15.location = (260.0, 80.0)
			separate_geometry_4.location = (-200.0, 100.0)
			separate_geometry_001.location = (0.0, -40.0)
			group_8.location = (-200.0, -60.0)
			group_001_2.location = (0.0, -200.0)
			
			#Set dimensions
			group_input_15.width, group_input_15.height = 140.0, 100.0
			group_output_15.width, group_output_15.height = 140.0, 100.0
			separate_geometry_4.width, separate_geometry_4.height = 140.0, 100.0
			separate_geometry_001.width, separate_geometry_001.height = 140.0, 100.0
			group_8.width, group_8.height = 140.0, 100.0
			group_001_2.width, group_001_2.height = 140.0, 100.0
			
			#initialize separate_polymers links
			#group_input_15.Atoms -> separate_geometry_4.Geometry
			separate_polymers.links.new(group_input_15.outputs[0], separate_geometry_4.inputs[0])
			#separate_geometry_4.Inverted -> separate_geometry_001.Geometry
			separate_polymers.links.new(separate_geometry_4.outputs[1], separate_geometry_001.inputs[0])
			#separate_geometry_4.Selection -> group_output_15.Peptide
			separate_polymers.links.new(separate_geometry_4.outputs[0], group_output_15.inputs[0])
			#separate_geometry_001.Selection -> group_output_15.Nucleic
			separate_polymers.links.new(separate_geometry_001.outputs[0], group_output_15.inputs[1])
			#separate_geometry_001.Inverted -> group_output_15.Other
			separate_polymers.links.new(separate_geometry_001.outputs[1], group_output_15.inputs[2])
			#group_8.Selection -> separate_geometry_4.Selection
			separate_polymers.links.new(group_8.outputs[0], separate_geometry_4.inputs[1])
			#group_001_2.Selection -> separate_geometry_001.Selection
			separate_polymers.links.new(group_001_2.outputs[0], separate_geometry_001.inputs[1])
			return separate_polymers

		separate_polymers = separate_polymers_node_group()

		#initialize _sampleatomvalue node group
		def _sampleatomvalue_node_group():
			_sampleatomvalue = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".SampleAtomValue")

			_sampleatomvalue.color_tag = 'NONE'
			_sampleatomvalue.description = ""

			_sampleatomvalue.is_modifier = True
			
			#_sampleatomvalue interface
			#Socket Atoms
			atoms_socket_8 = _sampleatomvalue.interface.new_socket(name = "Atoms", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_8.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_1 = _sampleatomvalue.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			value_socket_1.subtype = 'NONE'
			value_socket_1.default_value = (0.0, 0.0, 0.0)
			value_socket_1.min_value = -3.4028234663852886e+38
			value_socket_1.max_value = 3.4028234663852886e+38
			value_socket_1.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_2 = _sampleatomvalue.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketColor')
			value_socket_2.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_3 = _sampleatomvalue.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_3.attribute_domain = 'POINT'
			
			#Socket B
			b_socket = _sampleatomvalue.interface.new_socket(name = "B", in_out='INPUT', socket_type = 'NodeSocketInt')
			b_socket.subtype = 'NONE'
			b_socket.default_value = 57
			b_socket.min_value = -2147483648
			b_socket.max_value = 2147483647
			b_socket.attribute_domain = 'POINT'
			
			
			#initialize _sampleatomvalue nodes
			#node Group Output
			group_output_16 = _sampleatomvalue.nodes.new("NodeGroupOutput")
			group_output_16.name = "Group Output"
			group_output_16.is_active_output = True
			
			#node Named Attribute.009
			named_attribute_009 = _sampleatomvalue.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_009.name = "Named Attribute.009"
			named_attribute_009.data_type = 'INT'
			#Name
			named_attribute_009.inputs[0].default_value = "atom_name"
			
			#node Index.005
			index_005 = _sampleatomvalue.nodes.new("GeometryNodeInputIndex")
			index_005.name = "Index.005"
			
			#node Position.002
			position_002_1 = _sampleatomvalue.nodes.new("GeometryNodeInputPosition")
			position_002_1.name = "Position.002"
			
			#node Compare.003
			compare_003_2 = _sampleatomvalue.nodes.new("FunctionNodeCompare")
			compare_003_2.name = "Compare.003"
			compare_003_2.data_type = 'INT'
			compare_003_2.mode = 'ELEMENT'
			compare_003_2.operation = 'EQUAL'
			
			#node Group Input
			group_input_16 = _sampleatomvalue.nodes.new("NodeGroupInput")
			group_input_16.name = "Group Input"
			
			#node Sample Index.009
			sample_index_009_1 = _sampleatomvalue.nodes.new("GeometryNodeSampleIndex")
			sample_index_009_1.name = "Sample Index.009"
			sample_index_009_1.clamp = False
			sample_index_009_1.data_type = 'FLOAT_VECTOR'
			sample_index_009_1.domain = 'POINT'
			
			#node Named Attribute
			named_attribute_6 = _sampleatomvalue.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_6.name = "Named Attribute"
			named_attribute_6.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute_6.inputs[0].default_value = "Color"
			
			#node Sample Index.010
			sample_index_010_1 = _sampleatomvalue.nodes.new("GeometryNodeSampleIndex")
			sample_index_010_1.name = "Sample Index.010"
			sample_index_010_1.clamp = False
			sample_index_010_1.data_type = 'FLOAT_COLOR'
			sample_index_010_1.domain = 'POINT'
			
			#node Separate Geometry.002
			separate_geometry_002_1 = _sampleatomvalue.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_002_1.name = "Separate Geometry.002"
			separate_geometry_002_1.domain = 'POINT'
			
			
			
			
			#Set locations
			group_output_16.location = (390.0, 0.0)
			named_attribute_009.location = (-200.0, -107.52880859375)
			index_005.location = (40.0, -47.52880859375)
			position_002_1.location = (40.0, 12.47119140625)
			compare_003_2.location = (40.2109375, -112.47119140625)
			group_input_16.location = (-170.3642578125, -265.140380859375)
			sample_index_009_1.location = (200.0, 112.47119140625)
			named_attribute_6.location = (40.0, -380.0)
			sample_index_010_1.location = (200.0, -280.0)
			separate_geometry_002_1.location = (200.0, -107.52880859375)
			
			#Set dimensions
			group_output_16.width, group_output_16.height = 140.0, 100.0
			named_attribute_009.width, named_attribute_009.height = 206.99917602539062, 100.0
			index_005.width, index_005.height = 140.0, 100.0
			position_002_1.width, position_002_1.height = 140.0, 100.0
			compare_003_2.width, compare_003_2.height = 140.0, 100.0
			group_input_16.width, group_input_16.height = 140.0, 100.0
			sample_index_009_1.width, sample_index_009_1.height = 140.0, 100.0
			named_attribute_6.width, named_attribute_6.height = 140.0, 100.0
			sample_index_010_1.width, sample_index_010_1.height = 140.0, 100.0
			separate_geometry_002_1.width, separate_geometry_002_1.height = 140.0, 100.0
			
			#initialize _sampleatomvalue links
			#index_005.Index -> sample_index_009_1.Index
			_sampleatomvalue.links.new(index_005.outputs[0], sample_index_009_1.inputs[2])
			#compare_003_2.Result -> separate_geometry_002_1.Selection
			_sampleatomvalue.links.new(compare_003_2.outputs[0], separate_geometry_002_1.inputs[1])
			#named_attribute_009.Attribute -> compare_003_2.A
			_sampleatomvalue.links.new(named_attribute_009.outputs[0], compare_003_2.inputs[2])
			#separate_geometry_002_1.Selection -> sample_index_009_1.Geometry
			_sampleatomvalue.links.new(separate_geometry_002_1.outputs[0], sample_index_009_1.inputs[0])
			#position_002_1.Position -> sample_index_009_1.Value
			_sampleatomvalue.links.new(position_002_1.outputs[0], sample_index_009_1.inputs[1])
			#group_input_16.Geometry -> separate_geometry_002_1.Geometry
			_sampleatomvalue.links.new(group_input_16.outputs[0], separate_geometry_002_1.inputs[0])
			#group_input_16.B -> compare_003_2.B
			_sampleatomvalue.links.new(group_input_16.outputs[1], compare_003_2.inputs[3])
			#sample_index_009_1.Value -> group_output_16.Value
			_sampleatomvalue.links.new(sample_index_009_1.outputs[0], group_output_16.inputs[1])
			#index_005.Index -> sample_index_010_1.Index
			_sampleatomvalue.links.new(index_005.outputs[0], sample_index_010_1.inputs[2])
			#separate_geometry_002_1.Selection -> sample_index_010_1.Geometry
			_sampleatomvalue.links.new(separate_geometry_002_1.outputs[0], sample_index_010_1.inputs[0])
			#named_attribute_6.Attribute -> sample_index_010_1.Value
			_sampleatomvalue.links.new(named_attribute_6.outputs[0], sample_index_010_1.inputs[1])
			#sample_index_010_1.Value -> group_output_16.Value
			_sampleatomvalue.links.new(sample_index_010_1.outputs[0], group_output_16.inputs[2])
			#separate_geometry_002_1.Selection -> group_output_16.Atoms
			_sampleatomvalue.links.new(separate_geometry_002_1.outputs[0], group_output_16.inputs[0])
			return _sampleatomvalue

		_sampleatomvalue = _sampleatomvalue_node_group()

		#initialize mn_select_nucleic_type node group
		def mn_select_nucleic_type_node_group():
			mn_select_nucleic_type = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "MN_select_nucleic_type")

			mn_select_nucleic_type.color_tag = 'NONE'
			mn_select_nucleic_type.description = ""

			
			#mn_select_nucleic_type interface
			#Socket is_purine
			is_purine_socket = mn_select_nucleic_type.interface.new_socket(name = "is_purine", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_purine_socket.attribute_domain = 'POINT'
			
			#Socket is_pyrimidine
			is_pyrimidine_socket = mn_select_nucleic_type.interface.new_socket(name = "is_pyrimidine", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_pyrimidine_socket.attribute_domain = 'POINT'
			
			
			#initialize mn_select_nucleic_type nodes
			#node Group Input
			group_input_17 = mn_select_nucleic_type.nodes.new("NodeGroupInput")
			group_input_17.name = "Group Input"
			
			#node Reroute.015
			reroute_015_1 = mn_select_nucleic_type.nodes.new("NodeReroute")
			reroute_015_1.name = "Reroute.015"
			#node Named Attribute.010
			named_attribute_010 = mn_select_nucleic_type.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_010.name = "Named Attribute.010"
			named_attribute_010.data_type = 'INT'
			#Name
			named_attribute_010.inputs[0].default_value = "res_name"
			
			#node Compare.007
			compare_007 = mn_select_nucleic_type.nodes.new("FunctionNodeCompare")
			compare_007.name = "Compare.007"
			compare_007.data_type = 'INT'
			compare_007.mode = 'ELEMENT'
			compare_007.operation = 'EQUAL'
			#B_INT
			compare_007.inputs[3].default_value = 33
			
			#node Compare.016
			compare_016 = mn_select_nucleic_type.nodes.new("FunctionNodeCompare")
			compare_016.name = "Compare.016"
			compare_016.data_type = 'INT'
			compare_016.mode = 'ELEMENT'
			compare_016.operation = 'EQUAL'
			#B_INT
			compare_016.inputs[3].default_value = 43
			
			#node Compare.008
			compare_008 = mn_select_nucleic_type.nodes.new("FunctionNodeCompare")
			compare_008.name = "Compare.008"
			compare_008.data_type = 'INT'
			compare_008.mode = 'ELEMENT'
			compare_008.operation = 'EQUAL'
			#B_INT
			compare_008.inputs[3].default_value = 31
			
			#node Compare.015
			compare_015 = mn_select_nucleic_type.nodes.new("FunctionNodeCompare")
			compare_015.name = "Compare.015"
			compare_015.data_type = 'INT'
			compare_015.mode = 'ELEMENT'
			compare_015.operation = 'EQUAL'
			#B_INT
			compare_015.inputs[3].default_value = 41
			
			#node Boolean Math.012
			boolean_math_012 = mn_select_nucleic_type.nodes.new("FunctionNodeBooleanMath")
			boolean_math_012.name = "Boolean Math.012"
			boolean_math_012.operation = 'OR'
			
			#node Boolean Math.013
			boolean_math_013 = mn_select_nucleic_type.nodes.new("FunctionNodeBooleanMath")
			boolean_math_013.name = "Boolean Math.013"
			boolean_math_013.operation = 'OR'
			
			#node Boolean Math.007
			boolean_math_007 = mn_select_nucleic_type.nodes.new("FunctionNodeBooleanMath")
			boolean_math_007.name = "Boolean Math.007"
			boolean_math_007.operation = 'OR'
			
			#node Group Output
			group_output_17 = mn_select_nucleic_type.nodes.new("NodeGroupOutput")
			group_output_17.name = "Group Output"
			group_output_17.is_active_output = True
			
			#node Compare.017
			compare_017 = mn_select_nucleic_type.nodes.new("FunctionNodeCompare")
			compare_017.name = "Compare.017"
			compare_017.data_type = 'INT'
			compare_017.mode = 'ELEMENT'
			compare_017.operation = 'EQUAL'
			#B_INT
			compare_017.inputs[3].default_value = 42
			
			#node Compare.010
			compare_010 = mn_select_nucleic_type.nodes.new("FunctionNodeCompare")
			compare_010.name = "Compare.010"
			compare_010.data_type = 'INT'
			compare_010.mode = 'ELEMENT'
			compare_010.operation = 'EQUAL'
			#B_INT
			compare_010.inputs[3].default_value = 30
			
			#node Compare.018
			compare_018 = mn_select_nucleic_type.nodes.new("FunctionNodeCompare")
			compare_018.name = "Compare.018"
			compare_018.data_type = 'INT'
			compare_018.mode = 'ELEMENT'
			compare_018.operation = 'EQUAL'
			#B_INT
			compare_018.inputs[3].default_value = 40
			
			#node Boolean Math.014
			boolean_math_014 = mn_select_nucleic_type.nodes.new("FunctionNodeBooleanMath")
			boolean_math_014.name = "Boolean Math.014"
			boolean_math_014.operation = 'OR'
			
			#node Boolean Math.015
			boolean_math_015 = mn_select_nucleic_type.nodes.new("FunctionNodeBooleanMath")
			boolean_math_015.name = "Boolean Math.015"
			boolean_math_015.operation = 'OR'
			
			#node Compare.009
			compare_009 = mn_select_nucleic_type.nodes.new("FunctionNodeCompare")
			compare_009.name = "Compare.009"
			compare_009.data_type = 'INT'
			compare_009.mode = 'ELEMENT'
			compare_009.operation = 'EQUAL'
			#B_INT
			compare_009.inputs[3].default_value = 32
			
			#node Boolean Math.008
			boolean_math_008 = mn_select_nucleic_type.nodes.new("FunctionNodeBooleanMath")
			boolean_math_008.name = "Boolean Math.008"
			boolean_math_008.operation = 'OR'
			
			
			
			
			#Set locations
			group_input_17.location = (-570.0, 0.0)
			reroute_015_1.location = (-150.0, -97.31201171875)
			named_attribute_010.location = (-420.0, -60.0)
			compare_007.location = (-30.0, -90.0)
			compare_016.location = (-30.0, -250.0)
			compare_008.location = (-30.0, 249.9998779296875)
			compare_015.location = (-30.0, 89.9998779296875)
			boolean_math_012.location = (170.0, 249.9998779296875)
			boolean_math_013.location = (150.0, -90.0)
			boolean_math_007.location = (370.0, 249.9998779296875)
			group_output_17.location = (580.0, 240.0)
			compare_017.location = (-40.0, -940.0)
			compare_010.location = (-40.0, -440.0)
			compare_018.location = (-40.0, -600.0)
			boolean_math_014.location = (160.0, -440.0)
			boolean_math_015.location = (140.0, -780.0)
			compare_009.location = (-40.0, -780.0)
			boolean_math_008.location = (360.0, -440.0)
			
			#Set dimensions
			group_input_17.width, group_input_17.height = 140.0, 100.0
			reroute_015_1.width, reroute_015_1.height = 16.0, 100.0
			named_attribute_010.width, named_attribute_010.height = 206.99917602539062, 100.0
			compare_007.width, compare_007.height = 140.0, 100.0
			compare_016.width, compare_016.height = 140.0, 100.0
			compare_008.width, compare_008.height = 140.0, 100.0
			compare_015.width, compare_015.height = 140.0, 100.0
			boolean_math_012.width, boolean_math_012.height = 140.0, 100.0
			boolean_math_013.width, boolean_math_013.height = 140.0, 100.0
			boolean_math_007.width, boolean_math_007.height = 140.0, 100.0
			group_output_17.width, group_output_17.height = 140.0, 100.0
			compare_017.width, compare_017.height = 140.0, 100.0
			compare_010.width, compare_010.height = 140.0, 100.0
			compare_018.width, compare_018.height = 140.0, 100.0
			boolean_math_014.width, boolean_math_014.height = 140.0, 100.0
			boolean_math_015.width, boolean_math_015.height = 140.0, 100.0
			compare_009.width, compare_009.height = 140.0, 100.0
			boolean_math_008.width, boolean_math_008.height = 140.0, 100.0
			
			#initialize mn_select_nucleic_type links
			#compare_016.Result -> boolean_math_013.Boolean
			mn_select_nucleic_type.links.new(compare_016.outputs[0], boolean_math_013.inputs[1])
			#reroute_015_1.Output -> compare_016.A
			mn_select_nucleic_type.links.new(reroute_015_1.outputs[0], compare_016.inputs[2])
			#boolean_math_012.Boolean -> boolean_math_007.Boolean
			mn_select_nucleic_type.links.new(boolean_math_012.outputs[0], boolean_math_007.inputs[0])
			#boolean_math_013.Boolean -> boolean_math_007.Boolean
			mn_select_nucleic_type.links.new(boolean_math_013.outputs[0], boolean_math_007.inputs[1])
			#reroute_015_1.Output -> compare_008.A
			mn_select_nucleic_type.links.new(reroute_015_1.outputs[0], compare_008.inputs[2])
			#compare_008.Result -> boolean_math_012.Boolean
			mn_select_nucleic_type.links.new(compare_008.outputs[0], boolean_math_012.inputs[0])
			#compare_007.Result -> boolean_math_013.Boolean
			mn_select_nucleic_type.links.new(compare_007.outputs[0], boolean_math_013.inputs[0])
			#reroute_015_1.Output -> compare_007.A
			mn_select_nucleic_type.links.new(reroute_015_1.outputs[0], compare_007.inputs[2])
			#reroute_015_1.Output -> compare_015.A
			mn_select_nucleic_type.links.new(reroute_015_1.outputs[0], compare_015.inputs[2])
			#compare_015.Result -> boolean_math_012.Boolean
			mn_select_nucleic_type.links.new(compare_015.outputs[0], boolean_math_012.inputs[1])
			#named_attribute_010.Attribute -> reroute_015_1.Input
			mn_select_nucleic_type.links.new(named_attribute_010.outputs[0], reroute_015_1.inputs[0])
			#boolean_math_007.Boolean -> group_output_17.is_pyrimidine
			mn_select_nucleic_type.links.new(boolean_math_007.outputs[0], group_output_17.inputs[1])
			#compare_017.Result -> boolean_math_015.Boolean
			mn_select_nucleic_type.links.new(compare_017.outputs[0], boolean_math_015.inputs[1])
			#reroute_015_1.Output -> compare_017.A
			mn_select_nucleic_type.links.new(reroute_015_1.outputs[0], compare_017.inputs[2])
			#boolean_math_014.Boolean -> boolean_math_008.Boolean
			mn_select_nucleic_type.links.new(boolean_math_014.outputs[0], boolean_math_008.inputs[0])
			#boolean_math_015.Boolean -> boolean_math_008.Boolean
			mn_select_nucleic_type.links.new(boolean_math_015.outputs[0], boolean_math_008.inputs[1])
			#reroute_015_1.Output -> compare_010.A
			mn_select_nucleic_type.links.new(reroute_015_1.outputs[0], compare_010.inputs[2])
			#compare_010.Result -> boolean_math_014.Boolean
			mn_select_nucleic_type.links.new(compare_010.outputs[0], boolean_math_014.inputs[0])
			#compare_009.Result -> boolean_math_015.Boolean
			mn_select_nucleic_type.links.new(compare_009.outputs[0], boolean_math_015.inputs[0])
			#reroute_015_1.Output -> compare_009.A
			mn_select_nucleic_type.links.new(reroute_015_1.outputs[0], compare_009.inputs[2])
			#reroute_015_1.Output -> compare_018.A
			mn_select_nucleic_type.links.new(reroute_015_1.outputs[0], compare_018.inputs[2])
			#compare_018.Result -> boolean_math_014.Boolean
			mn_select_nucleic_type.links.new(compare_018.outputs[0], boolean_math_014.inputs[1])
			#boolean_math_008.Boolean -> group_output_17.is_purine
			mn_select_nucleic_type.links.new(boolean_math_008.outputs[0], group_output_17.inputs[0])
			return mn_select_nucleic_type

		mn_select_nucleic_type = mn_select_nucleic_type_node_group()

		#initialize _base_align node group
		def _base_align_node_group():
			_base_align = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".Base align")

			_base_align.color_tag = 'NONE'
			_base_align.description = ""

			
			#_base_align interface
			#Socket Base Interface
			base_interface_socket = _base_align.interface.new_socket(name = "Base Interface", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			base_interface_socket.subtype = 'NONE'
			base_interface_socket.default_value = (0.0, 0.0, 0.0)
			base_interface_socket.min_value = -3.4028234663852886e+38
			base_interface_socket.max_value = 3.4028234663852886e+38
			base_interface_socket.attribute_domain = 'POINT'
			
			#Socket Base Pivot
			base_pivot_socket = _base_align.interface.new_socket(name = "Base Pivot", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			base_pivot_socket.subtype = 'NONE'
			base_pivot_socket.default_value = (0.0, 0.0, 0.0)
			base_pivot_socket.min_value = -3.4028234663852886e+38
			base_pivot_socket.max_value = 3.4028234663852886e+38
			base_pivot_socket.attribute_domain = 'POINT'
			
			#Socket Align Vertical
			align_vertical_socket = _base_align.interface.new_socket(name = "Align Vertical", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			align_vertical_socket.subtype = 'NONE'
			align_vertical_socket.default_value = (0.0, 0.0, 0.0)
			align_vertical_socket.min_value = -3.4028234663852886e+38
			align_vertical_socket.max_value = 3.4028234663852886e+38
			align_vertical_socket.attribute_domain = 'POINT'
			
			#Socket Align Horizontal
			align_horizontal_socket = _base_align.interface.new_socket(name = "Align Horizontal", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			align_horizontal_socket.subtype = 'NONE'
			align_horizontal_socket.default_value = (0.0, 0.0, 0.0)
			align_horizontal_socket.min_value = -3.4028234663852886e+38
			align_horizontal_socket.max_value = 3.4028234663852886e+38
			align_horizontal_socket.attribute_domain = 'POINT'
			
			#Socket Input
			input_socket = _base_align.interface.new_socket(name = "Input", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			input_socket.attribute_domain = 'POINT'
			
			
			#initialize _base_align nodes
			#node Switch.008
			switch_008 = _base_align.nodes.new("GeometryNodeSwitch")
			switch_008.name = "Switch.008"
			switch_008.input_type = 'INT'
			#False
			switch_008.inputs[1].default_value = 65
			#True
			switch_008.inputs[2].default_value = 68
			
			#node Reroute.018
			reroute_018_1 = _base_align.nodes.new("NodeReroute")
			reroute_018_1.name = "Reroute.018"
			#node Switch.009
			switch_009 = _base_align.nodes.new("GeometryNodeSwitch")
			switch_009.name = "Switch.009"
			switch_009.input_type = 'INT'
			#False
			switch_009.inputs[1].default_value = 62
			#True
			switch_009.inputs[2].default_value = 64
			
			#node Reroute.020
			reroute_020 = _base_align.nodes.new("NodeReroute")
			reroute_020.name = "Reroute.020"
			#node Group.007
			group_007 = _base_align.nodes.new("GeometryNodeGroup")
			group_007.name = "Group.007"
			group_007.node_tree = mn_select_nucleic_type
			
			#node Group Input
			group_input_18 = _base_align.nodes.new("NodeGroupInput")
			group_input_18.name = "Group Input"
			
			#node Group.009
			group_009_1 = _base_align.nodes.new("GeometryNodeGroup")
			group_009_1.name = "Group.009"
			group_009_1.node_tree = _sampleatomvalue
			
			#node Group.010
			group_010 = _base_align.nodes.new("GeometryNodeGroup")
			group_010.name = "Group.010"
			group_010.node_tree = _sampleatomvalue
			
			#node Group.008
			group_008 = _base_align.nodes.new("GeometryNodeGroup")
			group_008.name = "Group.008"
			group_008.node_tree = _sampleatomvalue
			#Input_1
			group_008.inputs[1].default_value = 61
			
			#node Vector Math.002
			vector_math_002 = _base_align.nodes.new("ShaderNodeVectorMath")
			vector_math_002.name = "Vector Math.002"
			vector_math_002.operation = 'SUBTRACT'
			
			#node Vector Math.004
			vector_math_004 = _base_align.nodes.new("ShaderNodeVectorMath")
			vector_math_004.name = "Vector Math.004"
			vector_math_004.operation = 'SUBTRACT'
			
			#node Group Output
			group_output_18 = _base_align.nodes.new("NodeGroupOutput")
			group_output_18.name = "Group Output"
			group_output_18.is_active_output = True
			
			
			
			
			#Set locations
			switch_008.location = (-30.387451171875, 0.0)
			reroute_018_1.location = (-150.387451171875, -200.0)
			switch_009.location = (-30.387451171875, -180.0)
			reroute_020.location = (-180.0, 80.0)
			group_007.location = (-433.26495361328125, -188.3114776611328)
			group_input_18.location = (-400.0, 120.0)
			group_009_1.location = (160.0, -200.0)
			group_010.location = (160.0, 40.0)
			group_008.location = (160.0, 280.0)
			vector_math_002.location = (400.0, -60.0)
			vector_math_004.location = (400.0, 100.0)
			group_output_18.location = (700.0, 140.0)
			
			#Set dimensions
			switch_008.width, switch_008.height = 145.0830078125, 100.0
			reroute_018_1.width, reroute_018_1.height = 16.0, 100.0
			switch_009.width, switch_009.height = 145.0830078125, 100.0
			reroute_020.width, reroute_020.height = 16.0, 100.0
			group_007.width, group_007.height = 221.22412109375, 100.0
			group_input_18.width, group_input_18.height = 140.0, 100.0
			group_009_1.width, group_009_1.height = 140.0, 100.0
			group_010.width, group_010.height = 140.0, 100.0
			group_008.width, group_008.height = 140.0, 100.0
			vector_math_002.width, vector_math_002.height = 140.0, 100.0
			vector_math_004.width, vector_math_004.height = 140.0, 100.0
			group_output_18.width, group_output_18.height = 140.0, 100.0
			
			#initialize _base_align links
			#switch_008.Output -> group_010.B
			_base_align.links.new(switch_008.outputs[0], group_010.inputs[1])
			#reroute_018_1.Output -> group_010.Geometry
			_base_align.links.new(reroute_018_1.outputs[0], group_010.inputs[0])
			#group_009_1.Value -> vector_math_002.Vector
			_base_align.links.new(group_009_1.outputs[1], vector_math_002.inputs[1])
			#group_007.is_pyrimidine -> switch_008.Switch
			_base_align.links.new(group_007.outputs[1], switch_008.inputs[0])
			#group_007.is_pyrimidine -> switch_009.Switch
			_base_align.links.new(group_007.outputs[1], switch_009.inputs[0])
			#reroute_018_1.Output -> group_009_1.Geometry
			_base_align.links.new(reroute_018_1.outputs[0], group_009_1.inputs[0])
			#reroute_020.Output -> reroute_018_1.Input
			_base_align.links.new(reroute_020.outputs[0], reroute_018_1.inputs[0])
			#switch_009.Output -> group_009_1.B
			_base_align.links.new(switch_009.outputs[0], group_009_1.inputs[1])
			#group_008.Value -> vector_math_004.Vector
			_base_align.links.new(group_008.outputs[1], vector_math_004.inputs[1])
			#reroute_020.Output -> group_008.Geometry
			_base_align.links.new(reroute_020.outputs[0], group_008.inputs[0])
			#group_009_1.Value -> vector_math_004.Vector
			_base_align.links.new(group_009_1.outputs[1], vector_math_004.inputs[0])
			#group_010.Value -> vector_math_002.Vector
			_base_align.links.new(group_010.outputs[1], vector_math_002.inputs[0])
			#group_input_18.Input -> reroute_020.Input
			_base_align.links.new(group_input_18.outputs[0], reroute_020.inputs[0])
			#group_009_1.Value -> group_output_18.Base Interface
			_base_align.links.new(group_009_1.outputs[1], group_output_18.inputs[0])
			#group_008.Value -> group_output_18.Base Pivot
			_base_align.links.new(group_008.outputs[1], group_output_18.inputs[1])
			#vector_math_004.Vector -> group_output_18.Align Vertical
			_base_align.links.new(vector_math_004.outputs[0], group_output_18.inputs[2])
			#vector_math_002.Vector -> group_output_18.Align Horizontal
			_base_align.links.new(vector_math_002.outputs[0], group_output_18.inputs[3])
			return _base_align

		_base_align = _base_align_node_group()

		#initialize group_pick node group
		def group_pick_node_group():
			group_pick = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Group Pick")

			group_pick.color_tag = 'INPUT'
			group_pick.description = ""

			
			#group_pick interface
			#Socket Is Valid
			is_valid_socket = group_pick.interface.new_socket(name = "Is Valid", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_valid_socket.attribute_domain = 'POINT'
			is_valid_socket.description = "Whether the pick is valid. Pick is only valid if a single item is picked in the Group ID"
			
			#Socket Index
			index_socket = group_pick.interface.new_socket(name = "Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			index_socket.subtype = 'NONE'
			index_socket.default_value = 0
			index_socket.min_value = 0
			index_socket.max_value = 2147483647
			index_socket.attribute_domain = 'POINT'
			index_socket.description = "Index of picked item. Returns -1 if not a valid pick."
			
			#Socket Pick
			pick_socket = group_pick.interface.new_socket(name = "Pick", in_out='INPUT', socket_type = 'NodeSocketBool')
			pick_socket.attribute_domain = 'POINT'
			pick_socket.hide_value = True
			pick_socket.description = "True for the item to pick from the group. If number of picks is 0 or more than 1, not a valid pick"
			
			#Socket Group ID
			group_id_socket = group_pick.interface.new_socket(name = "Group ID", in_out='INPUT', socket_type = 'NodeSocketInt')
			group_id_socket.subtype = 'NONE'
			group_id_socket.default_value = 0
			group_id_socket.min_value = -2147483648
			group_id_socket.max_value = 2147483647
			group_id_socket.attribute_domain = 'POINT'
			group_id_socket.description = "Group ID inside which to pick the item"
			
			
			#initialize group_pick nodes
			#node Group Output
			group_output_19 = group_pick.nodes.new("NodeGroupOutput")
			group_output_19.name = "Group Output"
			group_output_19.is_active_output = True
			
			#node Group Input
			group_input_19 = group_pick.nodes.new("NodeGroupInput")
			group_input_19.name = "Group Input"
			
			#node Switch
			switch_4 = group_pick.nodes.new("GeometryNodeSwitch")
			switch_4.name = "Switch"
			switch_4.input_type = 'INT'
			#False
			switch_4.inputs[1].default_value = 0
			
			#node Index
			index_1 = group_pick.nodes.new("GeometryNodeInputIndex")
			index_1.name = "Index"
			
			#node Accumulate Field
			accumulate_field = group_pick.nodes.new("GeometryNodeAccumulateField")
			accumulate_field.name = "Accumulate Field"
			accumulate_field.data_type = 'INT'
			accumulate_field.domain = 'POINT'
			
			#node Accumulate Field.002
			accumulate_field_002 = group_pick.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_002.name = "Accumulate Field.002"
			accumulate_field_002.data_type = 'INT'
			accumulate_field_002.domain = 'POINT'
			
			#node Switch.001
			switch_001_1 = group_pick.nodes.new("GeometryNodeSwitch")
			switch_001_1.name = "Switch.001"
			switch_001_1.input_type = 'INT'
			#False
			switch_001_1.inputs[1].default_value = -1
			
			#node Compare.003
			compare_003_3 = group_pick.nodes.new("FunctionNodeCompare")
			compare_003_3.name = "Compare.003"
			compare_003_3.data_type = 'INT'
			compare_003_3.mode = 'ELEMENT'
			compare_003_3.operation = 'EQUAL'
			#B_INT
			compare_003_3.inputs[3].default_value = 1
			
			#node Reroute.001
			reroute_001_2 = group_pick.nodes.new("NodeReroute")
			reroute_001_2.name = "Reroute.001"
			#node Reroute.002
			reroute_002_2 = group_pick.nodes.new("NodeReroute")
			reroute_002_2.name = "Reroute.002"
			
			
			
			#Set locations
			group_output_19.location = (462.9173889160156, 0.0)
			group_input_19.location = (-472.9173889160156, 0.0)
			switch_4.location = (-120.0, -20.0)
			index_1.location = (-480.0, -120.0)
			accumulate_field.location = (60.0, -20.0)
			accumulate_field_002.location = (-120.0, 180.0)
			switch_001_1.location = (240.0, -20.0)
			compare_003_3.location = (60.0, 180.0)
			reroute_001_2.location = (-260.0, -100.0)
			reroute_002_2.location = (-260.0, -60.0)
			
			#Set dimensions
			group_output_19.width, group_output_19.height = 140.0, 100.0
			group_input_19.width, group_input_19.height = 140.0, 100.0
			switch_4.width, switch_4.height = 140.0, 100.0
			index_1.width, index_1.height = 140.0, 100.0
			accumulate_field.width, accumulate_field.height = 140.0, 100.0
			accumulate_field_002.width, accumulate_field_002.height = 140.0, 100.0
			switch_001_1.width, switch_001_1.height = 140.0, 100.0
			compare_003_3.width, compare_003_3.height = 138.9921875, 100.0
			reroute_001_2.width, reroute_001_2.height = 16.0, 100.0
			reroute_002_2.width, reroute_002_2.height = 16.0, 100.0
			
			#initialize group_pick links
			#switch_4.Output -> accumulate_field.Value
			group_pick.links.new(switch_4.outputs[0], accumulate_field.inputs[0])
			#compare_003_3.Result -> switch_001_1.Switch
			group_pick.links.new(compare_003_3.outputs[0], switch_001_1.inputs[0])
			#accumulate_field.Total -> switch_001_1.True
			group_pick.links.new(accumulate_field.outputs[2], switch_001_1.inputs[2])
			#reroute_001_2.Output -> accumulate_field.Group ID
			group_pick.links.new(reroute_001_2.outputs[0], accumulate_field.inputs[1])
			#reroute_001_2.Output -> accumulate_field_002.Group ID
			group_pick.links.new(reroute_001_2.outputs[0], accumulate_field_002.inputs[1])
			#reroute_002_2.Output -> switch_4.Switch
			group_pick.links.new(reroute_002_2.outputs[0], switch_4.inputs[0])
			#reroute_002_2.Output -> accumulate_field_002.Value
			group_pick.links.new(reroute_002_2.outputs[0], accumulate_field_002.inputs[0])
			#index_1.Index -> switch_4.True
			group_pick.links.new(index_1.outputs[0], switch_4.inputs[2])
			#accumulate_field_002.Total -> compare_003_3.A
			group_pick.links.new(accumulate_field_002.outputs[2], compare_003_3.inputs[2])
			#group_input_19.Group ID -> reroute_001_2.Input
			group_pick.links.new(group_input_19.outputs[1], reroute_001_2.inputs[0])
			#group_input_19.Pick -> reroute_002_2.Input
			group_pick.links.new(group_input_19.outputs[0], reroute_002_2.inputs[0])
			#switch_001_1.Output -> group_output_19.Index
			group_pick.links.new(switch_001_1.outputs[0], group_output_19.inputs[1])
			#compare_003_3.Result -> group_output_19.Is Valid
			group_pick.links.new(compare_003_3.outputs[0], group_output_19.inputs[0])
			return group_pick

		group_pick = group_pick_node_group()

		#initialize group_pick_vector node group
		def group_pick_vector_node_group():
			group_pick_vector = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Group Pick Vector")

			group_pick_vector.color_tag = 'INPUT'
			group_pick_vector.description = ""

			
			#group_pick_vector interface
			#Socket Is Valid
			is_valid_socket_1 = group_pick_vector.interface.new_socket(name = "Is Valid", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_valid_socket_1.attribute_domain = 'POINT'
			is_valid_socket_1.description = "The pick for this group is valid"
			
			#Socket Index
			index_socket_1 = group_pick_vector.interface.new_socket(name = "Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			index_socket_1.subtype = 'NONE'
			index_socket_1.default_value = 0
			index_socket_1.min_value = -2147483648
			index_socket_1.max_value = 2147483647
			index_socket_1.attribute_domain = 'POINT'
			index_socket_1.description = "Picked Index for the Group"
			
			#Socket Vector
			vector_socket = group_pick_vector.interface.new_socket(name = "Vector", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			vector_socket.subtype = 'NONE'
			vector_socket.default_value = (0.0, 0.0, 0.0)
			vector_socket.min_value = -3.4028234663852886e+38
			vector_socket.max_value = 3.4028234663852886e+38
			vector_socket.attribute_domain = 'POINT'
			vector_socket.description = "Picked vector for the group"
			
			#Socket Pick
			pick_socket_1 = group_pick_vector.interface.new_socket(name = "Pick", in_out='INPUT', socket_type = 'NodeSocketBool')
			pick_socket_1.attribute_domain = 'POINT'
			pick_socket_1.hide_value = True
			
			#Socket Group ID
			group_id_socket_1 = group_pick_vector.interface.new_socket(name = "Group ID", in_out='INPUT', socket_type = 'NodeSocketInt')
			group_id_socket_1.subtype = 'NONE'
			group_id_socket_1.default_value = 0
			group_id_socket_1.min_value = -2147483648
			group_id_socket_1.max_value = 2147483647
			group_id_socket_1.attribute_domain = 'POINT'
			
			#Socket Position
			position_socket = group_pick_vector.interface.new_socket(name = "Position", in_out='INPUT', socket_type = 'NodeSocketVector')
			position_socket.subtype = 'NONE'
			position_socket.default_value = (0.0, 0.0, 0.0)
			position_socket.min_value = -3.4028234663852886e+38
			position_socket.max_value = 3.4028234663852886e+38
			position_socket.attribute_domain = 'POINT'
			position_socket.description = "Vector field to pick vlaue for, defaults to Position"
			
			
			#initialize group_pick_vector nodes
			#node Group Output
			group_output_20 = group_pick_vector.nodes.new("NodeGroupOutput")
			group_output_20.name = "Group Output"
			group_output_20.is_active_output = True
			
			#node Group Input
			group_input_20 = group_pick_vector.nodes.new("NodeGroupInput")
			group_input_20.name = "Group Input"
			
			#node Evaluate at Index.001
			evaluate_at_index_001 = group_pick_vector.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001.name = "Evaluate at Index.001"
			evaluate_at_index_001.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_001.domain = 'POINT'
			
			#node Switch.002
			switch_002 = group_pick_vector.nodes.new("GeometryNodeSwitch")
			switch_002.name = "Switch.002"
			switch_002.input_type = 'VECTOR'
			#False
			switch_002.inputs[1].default_value = (0.0, 0.0, 0.0)
			
			#node Group
			group_9 = group_pick_vector.nodes.new("GeometryNodeGroup")
			group_9.name = "Group"
			group_9.node_tree = group_pick
			
			
			
			
			#Set locations
			group_output_20.location = (-40.0, -20.0)
			group_input_20.location = (-740.0, -80.0)
			evaluate_at_index_001.location = (-380.0, -180.0)
			switch_002.location = (-220.0, -60.0)
			group_9.location = (-560.0, -20.0)
			
			#Set dimensions
			group_output_20.width, group_output_20.height = 140.0, 100.0
			group_input_20.width, group_input_20.height = 140.0, 100.0
			evaluate_at_index_001.width, evaluate_at_index_001.height = 132.09918212890625, 100.0
			switch_002.width, switch_002.height = 140.0, 100.0
			group_9.width, group_9.height = 140.0, 100.0
			
			#initialize group_pick_vector links
			#group_9.Is Valid -> switch_002.Switch
			group_pick_vector.links.new(group_9.outputs[0], switch_002.inputs[0])
			#group_9.Index -> evaluate_at_index_001.Index
			group_pick_vector.links.new(group_9.outputs[1], evaluate_at_index_001.inputs[0])
			#evaluate_at_index_001.Value -> switch_002.True
			group_pick_vector.links.new(evaluate_at_index_001.outputs[0], switch_002.inputs[2])
			#group_9.Index -> group_output_20.Index
			group_pick_vector.links.new(group_9.outputs[1], group_output_20.inputs[1])
			#group_9.Is Valid -> group_output_20.Is Valid
			group_pick_vector.links.new(group_9.outputs[0], group_output_20.inputs[0])
			#switch_002.Output -> group_output_20.Vector
			group_pick_vector.links.new(switch_002.outputs[0], group_output_20.inputs[2])
			#group_input_20.Group ID -> group_9.Group ID
			group_pick_vector.links.new(group_input_20.outputs[1], group_9.inputs[1])
			#group_input_20.Pick -> group_9.Pick
			group_pick_vector.links.new(group_input_20.outputs[0], group_9.inputs[0])
			#group_input_20.Position -> evaluate_at_index_001.Value
			group_pick_vector.links.new(group_input_20.outputs[2], evaluate_at_index_001.inputs[1])
			return group_pick_vector

		group_pick_vector = group_pick_vector_node_group()

		#initialize offset_integer node group
		def offset_integer_node_group():
			offset_integer = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Offset Integer")

			offset_integer.color_tag = 'CONVERTER'
			offset_integer.description = ""

			
			#offset_integer interface
			#Socket Value
			value_socket_3 = offset_integer.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			value_socket_3.subtype = 'NONE'
			value_socket_3.default_value = 0
			value_socket_3.min_value = -2147483648
			value_socket_3.max_value = 2147483647
			value_socket_3.attribute_domain = 'POINT'
			
			#Socket Index
			index_socket_2 = offset_integer.interface.new_socket(name = "Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			index_socket_2.subtype = 'NONE'
			index_socket_2.default_value = 0
			index_socket_2.min_value = 0
			index_socket_2.max_value = 2147483647
			index_socket_2.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_4 = offset_integer.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketInt')
			value_socket_4.subtype = 'NONE'
			value_socket_4.default_value = 0
			value_socket_4.min_value = -2147483648
			value_socket_4.max_value = 2147483647
			value_socket_4.attribute_domain = 'POINT'
			value_socket_4.hide_value = True
			
			#Socket Offset
			offset_socket = offset_integer.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket.subtype = 'NONE'
			offset_socket.default_value = 0
			offset_socket.min_value = -2147483648
			offset_socket.max_value = 2147483647
			offset_socket.attribute_domain = 'POINT'
			
			
			#initialize offset_integer nodes
			#node Group Output
			group_output_21 = offset_integer.nodes.new("NodeGroupOutput")
			group_output_21.name = "Group Output"
			group_output_21.is_active_output = True
			
			#node Group Input
			group_input_21 = offset_integer.nodes.new("NodeGroupInput")
			group_input_21.name = "Group Input"
			
			#node Evaluate at Index
			evaluate_at_index = offset_integer.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index.name = "Evaluate at Index"
			evaluate_at_index.data_type = 'INT'
			evaluate_at_index.domain = 'POINT'
			
			#node Math
			math_5 = offset_integer.nodes.new("ShaderNodeMath")
			math_5.name = "Math"
			math_5.operation = 'ADD'
			math_5.use_clamp = False
			
			
			
			
			#Set locations
			group_output_21.location = (190.0, 0.0)
			group_input_21.location = (-412.72760009765625, 0.2001800537109375)
			evaluate_at_index.location = (0.0, 0.0)
			math_5.location = (-217.90158081054688, 69.93922424316406)
			
			#Set dimensions
			group_output_21.width, group_output_21.height = 140.0, 100.0
			group_input_21.width, group_input_21.height = 140.0, 100.0
			evaluate_at_index.width, evaluate_at_index.height = 140.0, 100.0
			math_5.width, math_5.height = 140.0, 100.0
			
			#initialize offset_integer links
			#evaluate_at_index.Value -> group_output_21.Value
			offset_integer.links.new(evaluate_at_index.outputs[0], group_output_21.inputs[0])
			#group_input_21.Index -> math_5.Value
			offset_integer.links.new(group_input_21.outputs[0], math_5.inputs[0])
			#group_input_21.Offset -> math_5.Value
			offset_integer.links.new(group_input_21.outputs[2], math_5.inputs[1])
			#math_5.Value -> evaluate_at_index.Index
			offset_integer.links.new(math_5.outputs[0], evaluate_at_index.inputs[0])
			#group_input_21.Value -> evaluate_at_index.Value
			offset_integer.links.new(group_input_21.outputs[1], evaluate_at_index.inputs[1])
			return offset_integer

		offset_integer = offset_integer_node_group()

		#initialize res_group_id node group
		def res_group_id_node_group():
			res_group_id = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Res Group ID")

			res_group_id.color_tag = 'INPUT'
			res_group_id.description = ""

			
			#res_group_id interface
			#Socket Unique Group ID
			unique_group_id_socket = res_group_id.interface.new_socket(name = "Unique Group ID", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			unique_group_id_socket.subtype = 'NONE'
			unique_group_id_socket.default_value = 0
			unique_group_id_socket.min_value = -2147483648
			unique_group_id_socket.max_value = 2147483647
			unique_group_id_socket.attribute_domain = 'POINT'
			unique_group_id_socket.description = "A unique Group ID for eash residue"
			
			
			#initialize res_group_id nodes
			#node Group Output
			group_output_22 = res_group_id.nodes.new("NodeGroupOutput")
			group_output_22.name = "Group Output"
			group_output_22.is_active_output = True
			
			#node Group Input
			group_input_22 = res_group_id.nodes.new("NodeGroupInput")
			group_input_22.name = "Group Input"
			
			#node Named Attribute.001
			named_attribute_001_1 = res_group_id.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001_1.name = "Named Attribute.001"
			named_attribute_001_1.data_type = 'INT'
			#Name
			named_attribute_001_1.inputs[0].default_value = "res_id"
			
			#node Named Attribute.002
			named_attribute_002_2 = res_group_id.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002_2.name = "Named Attribute.002"
			named_attribute_002_2.data_type = 'INT'
			#Name
			named_attribute_002_2.inputs[0].default_value = "atom_name"
			
			#node Compare.002
			compare_002_2 = res_group_id.nodes.new("FunctionNodeCompare")
			compare_002_2.name = "Compare.002"
			compare_002_2.data_type = 'INT'
			compare_002_2.mode = 'ELEMENT'
			compare_002_2.operation = 'EQUAL'
			#B_INT
			compare_002_2.inputs[3].default_value = 1
			
			#node Compare.001
			compare_001_2 = res_group_id.nodes.new("FunctionNodeCompare")
			compare_001_2.name = "Compare.001"
			compare_001_2.data_type = 'INT'
			compare_001_2.mode = 'ELEMENT'
			compare_001_2.operation = 'NOT_EQUAL'
			
			#node Boolean Math
			boolean_math_3 = res_group_id.nodes.new("FunctionNodeBooleanMath")
			boolean_math_3.name = "Boolean Math"
			boolean_math_3.operation = 'OR'
			
			#node Accumulate Field.001
			accumulate_field_001_1 = res_group_id.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_001_1.name = "Accumulate Field.001"
			accumulate_field_001_1.data_type = 'INT'
			accumulate_field_001_1.domain = 'POINT'
			#Group Index
			accumulate_field_001_1.inputs[1].default_value = 0
			
			#node Group.001
			group_001_3 = res_group_id.nodes.new("GeometryNodeGroup")
			group_001_3.name = "Group.001"
			group_001_3.node_tree = offset_integer
			#Socket_1
			group_001_3.inputs[0].default_value = 0
			#Socket_2
			group_001_3.inputs[2].default_value = -1
			
			#node Math
			math_6 = res_group_id.nodes.new("ShaderNodeMath")
			math_6.name = "Math"
			math_6.operation = 'SUBTRACT'
			math_6.use_clamp = False
			#Value_001
			math_6.inputs[1].default_value = 1.0
			
			#node Frame
			frame_3 = res_group_id.nodes.new("NodeFrame")
			frame_3.name = "Frame"
			frame_3.label_size = 20
			frame_3.shrink = True
			
			#node Reroute
			reroute_2 = res_group_id.nodes.new("NodeReroute")
			reroute_2.label = "subtracting 1 from the leading, but things don't work right"
			reroute_2.name = "Reroute"
			#node Reroute.001
			reroute_001_3 = res_group_id.nodes.new("NodeReroute")
			reroute_001_3.name = "Reroute.001"
			#node Reroute.002
			reroute_002_3 = res_group_id.nodes.new("NodeReroute")
			reroute_002_3.label = "In theory we can just use the trailing value instead of"
			reroute_002_3.name = "Reroute.002"
			#node Reroute.003
			reroute_003_1 = res_group_id.nodes.new("NodeReroute")
			reroute_003_1.name = "Reroute.003"
			
			
			#Set parents
			math_6.parent = frame_3
			reroute_2.parent = frame_3
			reroute_001_3.parent = frame_3
			reroute_002_3.parent = frame_3
			reroute_003_1.parent = frame_3
			
			#Set locations
			group_output_22.location = (900.0, 160.0)
			group_input_22.location = (-420.0, 160.0)
			named_attribute_001_1.location = (-240.0, 0.0)
			named_attribute_002_2.location = (-250.0, 160.0)
			compare_002_2.location = (-70.0, 160.0)
			compare_001_2.location = (-70.0, 0.0)
			boolean_math_3.location = (90.0, 160.0)
			accumulate_field_001_1.location = (250.0, 160.0)
			group_001_3.location = (-70.0, -160.0)
			math_6.location = (519.2361450195312, 166.28671264648438)
			frame_3.location = (95.0, -20.0)
			reroute_2.location = (554.4125366210938, 257.9646911621094)
			reroute_001_3.location = (739.2361450195312, 306.2867126464844)
			reroute_002_3.location = (551.13134765625, 297.3444519042969)
			reroute_003_1.location = (379.23614501953125, 306.2867126464844)
			
			#Set dimensions
			group_output_22.width, group_output_22.height = 140.0, 100.0
			group_input_22.width, group_input_22.height = 140.0, 100.0
			named_attribute_001_1.width, named_attribute_001_1.height = 140.0, 100.0
			named_attribute_002_2.width, named_attribute_002_2.height = 140.0, 100.0
			compare_002_2.width, compare_002_2.height = 140.0, 100.0
			compare_001_2.width, compare_001_2.height = 140.0, 100.0
			boolean_math_3.width, boolean_math_3.height = 140.0, 100.0
			accumulate_field_001_1.width, accumulate_field_001_1.height = 140.0, 100.0
			group_001_3.width, group_001_3.height = 140.0, 100.0
			math_6.width, math_6.height = 140.0, 100.0
			frame_3.width, frame_3.height = 436.0, 356.2867126464844
			reroute_2.width, reroute_2.height = 16.0, 100.0
			reroute_001_3.width, reroute_001_3.height = 16.0, 100.0
			reroute_002_3.width, reroute_002_3.height = 16.0, 100.0
			reroute_003_1.width, reroute_003_1.height = 16.0, 100.0
			
			#initialize res_group_id links
			#compare_002_2.Result -> boolean_math_3.Boolean
			res_group_id.links.new(compare_002_2.outputs[0], boolean_math_3.inputs[0])
			#named_attribute_001_1.Attribute -> compare_001_2.A
			res_group_id.links.new(named_attribute_001_1.outputs[0], compare_001_2.inputs[2])
			#named_attribute_001_1.Attribute -> group_001_3.Value
			res_group_id.links.new(named_attribute_001_1.outputs[0], group_001_3.inputs[1])
			#compare_001_2.Result -> boolean_math_3.Boolean
			res_group_id.links.new(compare_001_2.outputs[0], boolean_math_3.inputs[1])
			#named_attribute_002_2.Attribute -> compare_002_2.A
			res_group_id.links.new(named_attribute_002_2.outputs[0], compare_002_2.inputs[2])
			#group_001_3.Value -> compare_001_2.B
			res_group_id.links.new(group_001_3.outputs[0], compare_001_2.inputs[3])
			#accumulate_field_001_1.Leading -> math_6.Value
			res_group_id.links.new(accumulate_field_001_1.outputs[0], math_6.inputs[0])
			#math_6.Value -> group_output_22.Unique Group ID
			res_group_id.links.new(math_6.outputs[0], group_output_22.inputs[0])
			#boolean_math_3.Boolean -> accumulate_field_001_1.Value
			res_group_id.links.new(boolean_math_3.outputs[0], accumulate_field_001_1.inputs[0])
			return res_group_id

		res_group_id = res_group_id_node_group()

		#initialize residue_mask node group
		def residue_mask_node_group():
			residue_mask = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Residue Mask")

			residue_mask.color_tag = 'INPUT'
			residue_mask.description = ""

			
			#residue_mask interface
			#Socket Is Valid
			is_valid_socket_2 = residue_mask.interface.new_socket(name = "Is Valid", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_valid_socket_2.attribute_domain = 'POINT'
			is_valid_socket_2.description = "Group contains only one occurrance of the selected atom. None or more than one returns False"
			
			#Socket Index
			index_socket_3 = residue_mask.interface.new_socket(name = "Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			index_socket_3.subtype = 'NONE'
			index_socket_3.default_value = 0
			index_socket_3.min_value = -2147483648
			index_socket_3.max_value = 2147483647
			index_socket_3.attribute_domain = 'POINT'
			index_socket_3.description = "Index for the group's atom with specified name, returns -1 if not valid"
			
			#Socket Position
			position_socket_1 = residue_mask.interface.new_socket(name = "Position", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			position_socket_1.subtype = 'NONE'
			position_socket_1.default_value = (0.0, 0.0, 0.0)
			position_socket_1.min_value = -3.4028234663852886e+38
			position_socket_1.max_value = 3.4028234663852886e+38
			position_socket_1.attribute_domain = 'POINT'
			position_socket_1.description = "Position of the picked point in the group, returns (0, 0, 0) if not valid"
			
			#Socket Group ID
			group_id_socket_2 = residue_mask.interface.new_socket(name = "Group ID", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			group_id_socket_2.subtype = 'NONE'
			group_id_socket_2.default_value = 0
			group_id_socket_2.min_value = -2147483648
			group_id_socket_2.max_value = 2147483647
			group_id_socket_2.attribute_domain = 'POINT'
			
			#Socket atom_name
			atom_name_socket = residue_mask.interface.new_socket(name = "atom_name", in_out='INPUT', socket_type = 'NodeSocketInt')
			atom_name_socket.subtype = 'NONE'
			atom_name_socket.default_value = 1
			atom_name_socket.min_value = 2
			atom_name_socket.max_value = 2147483647
			atom_name_socket.attribute_domain = 'POINT'
			atom_name_socket.description = "Atom to pick from the group"
			
			#Socket Use Fallback
			use_fallback_socket = residue_mask.interface.new_socket(name = "Use Fallback", in_out='INPUT', socket_type = 'NodeSocketBool')
			use_fallback_socket.attribute_domain = 'POINT'
			use_fallback_socket.description = "Uses a calculated Unique Group ID as a fallback. Disabling can increase performance if pre-computing a Group ID for multiple nodes"
			
			#Socket Group ID
			group_id_socket_3 = residue_mask.interface.new_socket(name = "Group ID", in_out='INPUT', socket_type = 'NodeSocketInt')
			group_id_socket_3.subtype = 'NONE'
			group_id_socket_3.default_value = 0
			group_id_socket_3.min_value = -2147483648
			group_id_socket_3.max_value = 2147483647
			group_id_socket_3.attribute_domain = 'POINT'
			
			
			#initialize residue_mask nodes
			#node Compare
			compare_3 = residue_mask.nodes.new("FunctionNodeCompare")
			compare_3.name = "Compare"
			compare_3.data_type = 'INT'
			compare_3.mode = 'ELEMENT'
			compare_3.operation = 'EQUAL'
			
			#node Group Input
			group_input_23 = residue_mask.nodes.new("NodeGroupInput")
			group_input_23.name = "Group Input"
			
			#node Named Attribute
			named_attribute_7 = residue_mask.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_7.name = "Named Attribute"
			named_attribute_7.data_type = 'INT'
			#Name
			named_attribute_7.inputs[0].default_value = "atom_name"
			
			#node Group Output
			group_output_23 = residue_mask.nodes.new("NodeGroupOutput")
			group_output_23.name = "Group Output"
			group_output_23.is_active_output = True
			
			#node Group
			group_10 = residue_mask.nodes.new("GeometryNodeGroup")
			group_10.name = "Group"
			group_10.node_tree = group_pick_vector
			#Socket_5
			group_10.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Group.002
			group_002 = residue_mask.nodes.new("GeometryNodeGroup")
			group_002.name = "Group.002"
			group_002.node_tree = res_group_id
			
			#node Switch
			switch_5 = residue_mask.nodes.new("GeometryNodeSwitch")
			switch_5.name = "Switch"
			switch_5.input_type = 'INT'
			
			
			
			
			#Set locations
			compare_3.location = (40.0, 340.0)
			group_input_23.location = (-140.0, 200.0)
			named_attribute_7.location = (-140.0, 340.0)
			group_output_23.location = (420.0, 340.0)
			group_10.location = (220.0, 340.0)
			group_002.location = (-140.0, 60.0)
			switch_5.location = (40.0, 180.0)
			
			#Set dimensions
			compare_3.width, compare_3.height = 140.0, 100.0
			group_input_23.width, group_input_23.height = 140.0, 100.0
			named_attribute_7.width, named_attribute_7.height = 140.0, 100.0
			group_output_23.width, group_output_23.height = 140.0, 100.0
			group_10.width, group_10.height = 164.60528564453125, 100.0
			group_002.width, group_002.height = 140.0, 100.0
			switch_5.width, switch_5.height = 140.0, 100.0
			
			#initialize residue_mask links
			#named_attribute_7.Attribute -> compare_3.A
			residue_mask.links.new(named_attribute_7.outputs[0], compare_3.inputs[2])
			#group_input_23.atom_name -> compare_3.B
			residue_mask.links.new(group_input_23.outputs[0], compare_3.inputs[3])
			#group_10.Index -> group_output_23.Index
			residue_mask.links.new(group_10.outputs[1], group_output_23.inputs[1])
			#group_10.Vector -> group_output_23.Position
			residue_mask.links.new(group_10.outputs[2], group_output_23.inputs[2])
			#group_10.Is Valid -> group_output_23.Is Valid
			residue_mask.links.new(group_10.outputs[0], group_output_23.inputs[0])
			#compare_3.Result -> group_10.Pick
			residue_mask.links.new(compare_3.outputs[0], group_10.inputs[0])
			#group_input_23.Use Fallback -> switch_5.Switch
			residue_mask.links.new(group_input_23.outputs[1], switch_5.inputs[0])
			#group_input_23.Group ID -> switch_5.False
			residue_mask.links.new(group_input_23.outputs[2], switch_5.inputs[1])
			#switch_5.Output -> group_10.Group ID
			residue_mask.links.new(switch_5.outputs[0], group_10.inputs[1])
			#group_002.Unique Group ID -> switch_5.True
			residue_mask.links.new(group_002.outputs[0], switch_5.inputs[2])
			#switch_5.Output -> group_output_23.Group ID
			residue_mask.links.new(switch_5.outputs[0], group_output_23.inputs[3])
			return residue_mask

		residue_mask = residue_mask_node_group()

		#initialize _mn_utils_style_ribbon_nucleic node group
		def _mn_utils_style_ribbon_nucleic_node_group():
			_mn_utils_style_ribbon_nucleic = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_utils_style_ribbon_nucleic")

			_mn_utils_style_ribbon_nucleic.color_tag = 'GEOMETRY'
			_mn_utils_style_ribbon_nucleic.description = ""

			_mn_utils_style_ribbon_nucleic.is_modifier = True
			
			#_mn_utils_style_ribbon_nucleic interface
			#Socket Ribbon + Bases
			ribbon___bases_socket = _mn_utils_style_ribbon_nucleic.interface.new_socket(name = "Ribbon + Bases", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			ribbon___bases_socket.attribute_domain = 'POINT'
			
			#Socket Ribbon Curve
			ribbon_curve_socket = _mn_utils_style_ribbon_nucleic.interface.new_socket(name = "Ribbon Curve", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			ribbon_curve_socket.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket_9 = _mn_utils_style_ribbon_nucleic.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_9.attribute_domain = 'POINT'
			atoms_socket_9.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket_8 = _mn_utils_style_ribbon_nucleic.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_8.attribute_domain = 'POINT'
			selection_socket_8.hide_value = True
			selection_socket_8.description = "Selection of atoms to apply this node to"
			
			#Socket Material
			material_socket_5 = _mn_utils_style_ribbon_nucleic.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial')
			material_socket_5.attribute_domain = 'POINT'
			material_socket_5.description = "Material to apply to the resulting geometry"
			
			#Socket Intepolate Color
			intepolate_color_socket = _mn_utils_style_ribbon_nucleic.interface.new_socket(name = "Intepolate Color", in_out='INPUT', socket_type = 'NodeSocketBool')
			intepolate_color_socket.attribute_domain = 'POINT'
			
			#Panel Backbone
			backbone_panel = _mn_utils_style_ribbon_nucleic.interface.new_panel("Backbone")
			#Socket Backbone Subdivisions
			backbone_subdivisions_socket = _mn_utils_style_ribbon_nucleic.interface.new_socket(name = "Backbone Subdivisions", in_out='INPUT', socket_type = 'NodeSocketInt', parent = backbone_panel)
			backbone_subdivisions_socket.subtype = 'NONE'
			backbone_subdivisions_socket.default_value = 3
			backbone_subdivisions_socket.min_value = 1
			backbone_subdivisions_socket.max_value = 10
			backbone_subdivisions_socket.attribute_domain = 'POINT'
			
			#Socket Backbone Resolution
			backbone_resolution_socket = _mn_utils_style_ribbon_nucleic.interface.new_socket(name = "Backbone Resolution", in_out='INPUT', socket_type = 'NodeSocketInt', parent = backbone_panel)
			backbone_resolution_socket.subtype = 'NONE'
			backbone_resolution_socket.default_value = 8
			backbone_resolution_socket.min_value = 3
			backbone_resolution_socket.max_value = 50
			backbone_resolution_socket.attribute_domain = 'POINT'
			
			#Socket Backbone Radius
			backbone_radius_socket = _mn_utils_style_ribbon_nucleic.interface.new_socket(name = "Backbone Radius", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = backbone_panel)
			backbone_radius_socket.subtype = 'DISTANCE'
			backbone_radius_socket.default_value = 2.0
			backbone_radius_socket.min_value = 0.0
			backbone_radius_socket.max_value = 3.4028234663852886e+38
			backbone_radius_socket.attribute_domain = 'POINT'
			
			#Socket Backbone Shade Smooth
			backbone_shade_smooth_socket = _mn_utils_style_ribbon_nucleic.interface.new_socket(name = "Backbone Shade Smooth", in_out='INPUT', socket_type = 'NodeSocketBool', parent = backbone_panel)
			backbone_shade_smooth_socket.attribute_domain = 'POINT'
			
			
			#Panel Base
			base_panel = _mn_utils_style_ribbon_nucleic.interface.new_panel("Base")
			#Socket Base Radius
			base_radius_socket = _mn_utils_style_ribbon_nucleic.interface.new_socket(name = "Base Radius", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = base_panel)
			base_radius_socket.subtype = 'DISTANCE'
			base_radius_socket.default_value = 0.20000000298023224
			base_radius_socket.min_value = 0.0
			base_radius_socket.max_value = 3.4028234663852886e+38
			base_radius_socket.attribute_domain = 'POINT'
			
			#Socket Base Resolution
			base_resolution_socket = _mn_utils_style_ribbon_nucleic.interface.new_socket(name = "Base Resolution", in_out='INPUT', socket_type = 'NodeSocketInt', parent = base_panel)
			base_resolution_socket.subtype = 'NONE'
			base_resolution_socket.default_value = 6
			base_resolution_socket.min_value = 3
			base_resolution_socket.max_value = 512
			base_resolution_socket.attribute_domain = 'POINT'
			
			
			
			#initialize _mn_utils_style_ribbon_nucleic nodes
			#node Frame.002
			frame_002_2 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeFrame")
			frame_002_2.label = "Transfer attributes to new curve / mesh from alpha carbons"
			frame_002_2.name = "Frame.002"
			frame_002_2.label_size = 20
			frame_002_2.shrink = True
			
			#node Frame
			frame_4 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeFrame")
			frame_4.label = "Delete between chains and distance too large"
			frame_4.name = "Frame"
			frame_4.label_size = 20
			frame_4.shrink = True
			
			#node Frame.001
			frame_001_2 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeFrame")
			frame_001_2.label = "Create New mesh line through all CA"
			frame_001_2.name = "Frame.001"
			frame_001_2.label_size = 20
			frame_001_2.shrink = True
			
			#node Frame.006
			frame_006 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeFrame")
			frame_006.label = "Slightly Extend Curve Ends"
			frame_006.name = "Frame.006"
			frame_006.label_size = 20
			frame_006.shrink = True
			
			#node Frame.004
			frame_004_1 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeFrame")
			frame_004_1.label = "Convert Mesh Backbone to Curve"
			frame_004_1.name = "Frame.004"
			frame_004_1.label_size = 20
			frame_004_1.shrink = True
			
			#node Frame.005
			frame_005_1 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeFrame")
			frame_005_1.label = "Instance simple base cylinder"
			frame_005_1.name = "Frame.005"
			frame_005_1.label_size = 20
			frame_005_1.shrink = True
			
			#node Frame.007
			frame_007 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeFrame")
			frame_007.label = "Align Base"
			frame_007.name = "Frame.007"
			frame_007.label_size = 20
			frame_007.shrink = True
			
			#node Frame.003
			frame_003_2 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeFrame")
			frame_003_2.label = "Create mesh from curve"
			frame_003_2.name = "Frame.003"
			frame_003_2.label_size = 20
			frame_003_2.shrink = True
			
			#node Sample Index
			sample_index_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSampleIndex")
			sample_index_1.name = "Sample Index"
			sample_index_1.hide = True
			sample_index_1.clamp = True
			sample_index_1.data_type = 'INT'
			sample_index_1.domain = 'POINT'
			
			#node Named Attribute.002
			named_attribute_002_3 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002_3.label = "chain_id"
			named_attribute_002_3.name = "Named Attribute.002"
			named_attribute_002_3.hide = True
			named_attribute_002_3.data_type = 'INT'
			#Name
			named_attribute_002_3.inputs[0].default_value = "chain_id"
			
			#node Sample Index.004
			sample_index_004 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSampleIndex")
			sample_index_004.name = "Sample Index.004"
			sample_index_004.hide = True
			sample_index_004.clamp = True
			sample_index_004.data_type = 'INT'
			sample_index_004.domain = 'POINT'
			
			#node Named Attribute.004
			named_attribute_004_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_004_1.label = "res_id"
			named_attribute_004_1.name = "Named Attribute.004"
			named_attribute_004_1.hide = True
			named_attribute_004_1.data_type = 'INT'
			#Name
			named_attribute_004_1.inputs[0].default_value = "res_id"
			
			#node Sample Index.001
			sample_index_001_2 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSampleIndex")
			sample_index_001_2.name = "Sample Index.001"
			sample_index_001_2.hide = True
			sample_index_001_2.clamp = True
			sample_index_001_2.data_type = 'FLOAT_COLOR'
			sample_index_001_2.domain = 'POINT'
			
			#node Named Attribute
			named_attribute_8 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_8.label = "Color"
			named_attribute_8.name = "Named Attribute"
			named_attribute_8.hide = True
			named_attribute_8.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute_8.inputs[0].default_value = "Color"
			
			#node Reroute.003
			reroute_003_2 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_003_2.name = "Reroute.003"
			#node Sample Index.003
			sample_index_003_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSampleIndex")
			sample_index_003_1.name = "Sample Index.003"
			sample_index_003_1.hide = True
			sample_index_003_1.clamp = True
			sample_index_003_1.data_type = 'INT'
			sample_index_003_1.domain = 'POINT'
			
			#node Named Attribute.003
			named_attribute_003_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_003_1.label = "res_name"
			named_attribute_003_1.name = "Named Attribute.003"
			named_attribute_003_1.hide = True
			named_attribute_003_1.data_type = 'INT'
			#Name
			named_attribute_003_1.inputs[0].default_value = "res_name"
			
			#node Index.003
			index_003_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputIndex")
			index_003_1.name = "Index.003"
			
			#node Named Attribute.005
			named_attribute_005_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_005_1.label = "b_factor"
			named_attribute_005_1.name = "Named Attribute.005"
			named_attribute_005_1.hide = True
			named_attribute_005_1.data_type = 'FLOAT'
			#Name
			named_attribute_005_1.inputs[0].default_value = "b_factor"
			
			#node Sample Index.005
			sample_index_005_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSampleIndex")
			sample_index_005_1.name = "Sample Index.005"
			sample_index_005_1.hide = True
			sample_index_005_1.clamp = True
			sample_index_005_1.data_type = 'FLOAT'
			sample_index_005_1.domain = 'POINT'
			
			#node Reroute.001
			reroute_001_4 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_001_4.name = "Reroute.001"
			#node Reroute.010
			reroute_010_1 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_010_1.name = "Reroute.010"
			#node Sample Index.008
			sample_index_008_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSampleIndex")
			sample_index_008_1.name = "Sample Index.008"
			sample_index_008_1.hide = True
			sample_index_008_1.clamp = True
			sample_index_008_1.data_type = 'INT'
			sample_index_008_1.domain = 'POINT'
			
			#node Named Attribute.006
			named_attribute_006_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_006_1.label = "chain_id"
			named_attribute_006_1.name = "Named Attribute.006"
			named_attribute_006_1.hide = True
			named_attribute_006_1.data_type = 'INT'
			#Name
			named_attribute_006_1.inputs[0].default_value = "chain_id"
			
			#node Index.004
			index_004 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputIndex")
			index_004.name = "Index.004"
			
			#node Reroute.002
			reroute_002_4 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_002_4.name = "Reroute.002"
			#node Edge Vertices
			edge_vertices_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputMeshEdgeVertices")
			edge_vertices_1.name = "Edge Vertices"
			
			#node Field at Index
			field_at_index = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeFieldAtIndex")
			field_at_index.name = "Field at Index"
			field_at_index.data_type = 'INT'
			field_at_index.domain = 'POINT'
			
			#node Field at Index.001
			field_at_index_001 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeFieldAtIndex")
			field_at_index_001.name = "Field at Index.001"
			field_at_index_001.data_type = 'INT'
			field_at_index_001.domain = 'POINT'
			
			#node Vector Math
			vector_math_1 = _mn_utils_style_ribbon_nucleic.nodes.new("ShaderNodeVectorMath")
			vector_math_1.name = "Vector Math"
			vector_math_1.operation = 'DISTANCE'
			
			#node Compare.001
			compare_001_3 = _mn_utils_style_ribbon_nucleic.nodes.new("FunctionNodeCompare")
			compare_001_3.name = "Compare.001"
			compare_001_3.data_type = 'FLOAT'
			compare_001_3.mode = 'ELEMENT'
			compare_001_3.operation = 'GREATER_THAN'
			#B
			compare_001_3.inputs[1].default_value = 0.10000000149011612
			
			#node Compare
			compare_4 = _mn_utils_style_ribbon_nucleic.nodes.new("FunctionNodeCompare")
			compare_4.name = "Compare"
			compare_4.data_type = 'INT'
			compare_4.mode = 'ELEMENT'
			compare_4.operation = 'NOT_EQUAL'
			
			#node Boolean Math
			boolean_math_4 = _mn_utils_style_ribbon_nucleic.nodes.new("FunctionNodeBooleanMath")
			boolean_math_4.name = "Boolean Math"
			boolean_math_4.operation = 'OR'
			
			#node Reroute.009
			reroute_009_1 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_009_1.name = "Reroute.009"
			#node Reroute.012
			reroute_012_1 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_012_1.name = "Reroute.012"
			#node Mesh Line
			mesh_line_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeMeshLine")
			mesh_line_1.name = "Mesh Line"
			mesh_line_1.hide = True
			mesh_line_1.count_mode = 'TOTAL'
			mesh_line_1.mode = 'END_POINTS'
			#Start Location
			mesh_line_1.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Offset
			mesh_line_1.inputs[3].default_value = (0.0, 0.0, 1.0)
			
			#node Set Position
			set_position_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSetPosition")
			set_position_1.name = "Set Position"
			set_position_1.hide = True
			#Selection
			set_position_1.inputs[1].default_value = True
			#Offset
			set_position_1.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Domain Size
			domain_size_2 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeAttributeDomainSize")
			domain_size_2.name = "Domain Size"
			domain_size_2.hide = True
			domain_size_2.component = 'MESH'
			domain_size_2.outputs[1].hide = True
			domain_size_2.outputs[2].hide = True
			domain_size_2.outputs[3].hide = True
			domain_size_2.outputs[4].hide = True
			domain_size_2.outputs[5].hide = True
			
			#node Delete Geometry
			delete_geometry = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeDeleteGeometry")
			delete_geometry.name = "Delete Geometry"
			delete_geometry.domain = 'EDGE'
			delete_geometry.mode = 'ALL'
			
			#node Sample Index.009
			sample_index_009_2 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSampleIndex")
			sample_index_009_2.name = "Sample Index.009"
			sample_index_009_2.hide = True
			sample_index_009_2.clamp = True
			sample_index_009_2.data_type = 'BOOLEAN'
			sample_index_009_2.domain = 'POINT'
			
			#node Group Input.006
			group_input_006 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeGroupInput")
			group_input_006.name = "Group Input.006"
			group_input_006.outputs[0].hide = True
			group_input_006.outputs[1].hide = True
			group_input_006.outputs[2].hide = True
			group_input_006.outputs[3].hide = True
			group_input_006.outputs[4].hide = True
			group_input_006.outputs[5].hide = True
			group_input_006.outputs[8].hide = True
			group_input_006.outputs[9].hide = True
			group_input_006.outputs[10].hide = True
			
			#node Sample Index.007
			sample_index_007_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSampleIndex")
			sample_index_007_1.name = "Sample Index.007"
			sample_index_007_1.hide = True
			sample_index_007_1.clamp = True
			sample_index_007_1.data_type = 'FLOAT'
			sample_index_007_1.domain = 'POINT'
			
			#node Group Output
			group_output_24 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeGroupOutput")
			group_output_24.name = "Group Output"
			group_output_24.is_active_output = True
			
			#node Offset Point in Curve
			offset_point_in_curve = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeOffsetPointInCurve")
			offset_point_in_curve.name = "Offset Point in Curve"
			#Point Index
			offset_point_in_curve.inputs[0].default_value = 0
			
			#node Evaluate at Index
			evaluate_at_index_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_1.name = "Evaluate at Index"
			evaluate_at_index_1.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_1.domain = 'POINT'
			
			#node Position.002
			position_002_2 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputPosition")
			position_002_2.name = "Position.002"
			
			#node Vector Math.002
			vector_math_002_1 = _mn_utils_style_ribbon_nucleic.nodes.new("ShaderNodeVectorMath")
			vector_math_002_1.name = "Vector Math.002"
			vector_math_002_1.operation = 'SUBTRACT'
			
			#node Vector Math.004
			vector_math_004_1 = _mn_utils_style_ribbon_nucleic.nodes.new("ShaderNodeVectorMath")
			vector_math_004_1.name = "Vector Math.004"
			vector_math_004_1.operation = 'SCALE'
			#Scale
			vector_math_004_1.inputs[3].default_value = -0.5
			
			#node Endpoint Selection
			endpoint_selection = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection.name = "Endpoint Selection"
			#Start Size
			endpoint_selection.inputs[0].default_value = 1
			#End Size
			endpoint_selection.inputs[1].default_value = 1
			
			#node Switch
			switch_6 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSwitch")
			switch_6.name = "Switch"
			switch_6.input_type = 'INT'
			#False
			switch_6.inputs[1].default_value = -1
			#True
			switch_6.inputs[2].default_value = 1
			
			#node Endpoint Selection.001
			endpoint_selection_001 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_001.name = "Endpoint Selection.001"
			#Start Size
			endpoint_selection_001.inputs[0].default_value = 1
			#End Size
			endpoint_selection_001.inputs[1].default_value = 0
			
			#node Set Position.001
			set_position_001 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSetPosition")
			set_position_001.name = "Set Position.001"
			#Position
			set_position_001.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Store Named Attribute.001
			store_named_attribute_001_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_001_1.name = "Store Named Attribute.001"
			store_named_attribute_001_1.data_type = 'INT'
			store_named_attribute_001_1.domain = 'POINT'
			#Selection
			store_named_attribute_001_1.inputs[1].default_value = True
			#Name
			store_named_attribute_001_1.inputs[2].default_value = "chain_id"
			
			#node Store Named Attribute.002
			store_named_attribute_002_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_002_1.name = "Store Named Attribute.002"
			store_named_attribute_002_1.data_type = 'INT'
			store_named_attribute_002_1.domain = 'POINT'
			#Selection
			store_named_attribute_002_1.inputs[1].default_value = True
			#Name
			store_named_attribute_002_1.inputs[2].default_value = "res_id"
			
			#node Store Named Attribute.003
			store_named_attribute_003_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_003_1.name = "Store Named Attribute.003"
			store_named_attribute_003_1.data_type = 'INT'
			store_named_attribute_003_1.domain = 'POINT'
			#Selection
			store_named_attribute_003_1.inputs[1].default_value = True
			#Name
			store_named_attribute_003_1.inputs[2].default_value = "res_name"
			
			#node Store Named Attribute.004
			store_named_attribute_004_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_004_1.name = "Store Named Attribute.004"
			store_named_attribute_004_1.data_type = 'FLOAT'
			store_named_attribute_004_1.domain = 'POINT'
			#Selection
			store_named_attribute_004_1.inputs[1].default_value = True
			#Name
			store_named_attribute_004_1.inputs[2].default_value = "b_factor"
			
			#node Capture Attribute
			capture_attribute_2 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute_2.name = "Capture Attribute"
			capture_attribute_2.active_index = 0
			capture_attribute_2.capture_items.clear()
			capture_attribute_2.capture_items.new('FLOAT', "Value")
			capture_attribute_2.capture_items["Value"].data_type = 'BOOLEAN'
			capture_attribute_2.domain = 'POINT'
			
			#node Set Handle Type
			set_handle_type = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeCurveSetHandles")
			set_handle_type.name = "Set Handle Type"
			set_handle_type.handle_type = 'AUTO'
			set_handle_type.mode = {'RIGHT', 'LEFT'}
			#Selection
			set_handle_type.inputs[1].default_value = True
			
			#node Set Spline Type
			set_spline_type = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeCurveSplineType")
			set_spline_type.name = "Set Spline Type"
			set_spline_type.spline_type = 'BEZIER'
			#Selection
			set_spline_type.inputs[1].default_value = True
			
			#node Group Input.004
			group_input_004_1 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeGroupInput")
			group_input_004_1.name = "Group Input.004"
			group_input_004_1.outputs[0].hide = True
			group_input_004_1.outputs[1].hide = True
			group_input_004_1.outputs[2].hide = True
			group_input_004_1.outputs[3].hide = True
			group_input_004_1.outputs[5].hide = True
			group_input_004_1.outputs[6].hide = True
			group_input_004_1.outputs[7].hide = True
			group_input_004_1.outputs[8].hide = True
			group_input_004_1.outputs[9].hide = True
			group_input_004_1.outputs[10].hide = True
			
			#node Mesh to Curve
			mesh_to_curve_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeMeshToCurve")
			mesh_to_curve_1.name = "Mesh to Curve"
			#Selection
			mesh_to_curve_1.inputs[1].default_value = True
			
			#node Set Spline Resolution
			set_spline_resolution = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSetSplineResolution")
			set_spline_resolution.name = "Set Spline Resolution"
			#Selection
			set_spline_resolution.inputs[1].default_value = True
			
			#node Store Named Attribute
			store_named_attribute_2 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_2.name = "Store Named Attribute"
			store_named_attribute_2.data_type = 'FLOAT_COLOR'
			store_named_attribute_2.domain = 'POINT'
			#Selection
			store_named_attribute_2.inputs[1].default_value = True
			#Name
			store_named_attribute_2.inputs[2].default_value = "Color"
			
			#node Store Named Attribute.007
			store_named_attribute_007 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_007.name = "Store Named Attribute.007"
			store_named_attribute_007.data_type = 'FLOAT_VECTOR'
			store_named_attribute_007.domain = 'POINT'
			#Selection
			store_named_attribute_007.inputs[1].default_value = True
			#Name
			store_named_attribute_007.inputs[2].default_value = "vec_horizontal"
			
			#node Store Named Attribute.008
			store_named_attribute_008 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_008.name = "Store Named Attribute.008"
			store_named_attribute_008.data_type = 'FLOAT_VECTOR'
			store_named_attribute_008.domain = 'POINT'
			#Selection
			store_named_attribute_008.inputs[1].default_value = True
			#Name
			store_named_attribute_008.inputs[2].default_value = "vec_vertical"
			
			#node Store Named Attribute.009
			store_named_attribute_009 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_009.name = "Store Named Attribute.009"
			store_named_attribute_009.data_type = 'FLOAT_VECTOR'
			store_named_attribute_009.domain = 'POINT'
			#Selection
			store_named_attribute_009.inputs[1].default_value = True
			#Name
			store_named_attribute_009.inputs[2].default_value = "atom_interface"
			
			#node Store Named Attribute.010
			store_named_attribute_010 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_010.name = "Store Named Attribute.010"
			store_named_attribute_010.data_type = 'FLOAT_VECTOR'
			store_named_attribute_010.domain = 'POINT'
			#Selection
			store_named_attribute_010.inputs[1].default_value = True
			#Name
			store_named_attribute_010.inputs[2].default_value = "atom_pivot"
			
			#node Combine XYZ
			combine_xyz = _mn_utils_style_ribbon_nucleic.nodes.new("ShaderNodeCombineXYZ")
			combine_xyz.name = "Combine XYZ"
			#X
			combine_xyz.inputs[0].default_value = 0.0
			#Y
			combine_xyz.inputs[1].default_value = 0.0
			
			#node Math
			math_7 = _mn_utils_style_ribbon_nucleic.nodes.new("ShaderNodeMath")
			math_7.name = "Math"
			math_7.operation = 'DIVIDE'
			math_7.use_clamp = False
			#Value_001
			math_7.inputs[1].default_value = 2.0
			
			#node Cylinder
			cylinder = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeMeshCylinder")
			cylinder.name = "Cylinder"
			cylinder.fill_type = 'NGON'
			#Side Segments
			cylinder.inputs[1].default_value = 1
			#Fill Segments
			cylinder.inputs[2].default_value = 1
			
			#node Value
			value_1 = _mn_utils_style_ribbon_nucleic.nodes.new("ShaderNodeValue")
			value_1.name = "Value"
			
			value_1.outputs[0].default_value = 1.0
			#node Group Input.005
			group_input_005_1 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeGroupInput")
			group_input_005_1.name = "Group Input.005"
			group_input_005_1.outputs[0].hide = True
			group_input_005_1.outputs[1].hide = True
			group_input_005_1.outputs[2].hide = True
			group_input_005_1.outputs[3].hide = True
			group_input_005_1.outputs[4].hide = True
			group_input_005_1.outputs[5].hide = True
			group_input_005_1.outputs[6].hide = True
			group_input_005_1.outputs[7].hide = True
			group_input_005_1.outputs[10].hide = True
			
			#node Store Named Attribute.006
			store_named_attribute_006_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_006_1.name = "Store Named Attribute.006"
			store_named_attribute_006_1.data_type = 'FLOAT_VECTOR'
			store_named_attribute_006_1.domain = 'CORNER'
			#Selection
			store_named_attribute_006_1.inputs[1].default_value = True
			#Name
			store_named_attribute_006_1.inputs[2].default_value = "uv_map"
			
			#node Position.001
			position_001_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputPosition")
			position_001_1.name = "Position.001"
			
			#node Store Named Attribute.005
			store_named_attribute_005_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_005_1.name = "Store Named Attribute.005"
			store_named_attribute_005_1.data_type = 'FLOAT_COLOR'
			store_named_attribute_005_1.domain = 'POINT'
			#Selection
			store_named_attribute_005_1.inputs[1].default_value = True
			#Name
			store_named_attribute_005_1.inputs[2].default_value = "Color"
			
			#node Separate Geometry
			separate_geometry_5 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_5.name = "Separate Geometry"
			separate_geometry_5.domain = 'POINT'
			
			#node Group Input
			group_input_24 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeGroupInput")
			group_input_24.name = "Group Input"
			group_input_24.outputs[3].hide = True
			
			#node Group.004
			group_004 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeGroup")
			group_004.name = "Group.004"
			group_004.node_tree = _sampleatomvalue
			#Input_1
			group_004.inputs[1].default_value = 67
			
			#node Reroute.006
			reroute_006_1 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_006_1.name = "Reroute.006"
			#node Reroute.011
			reroute_011_1 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_011_1.name = "Reroute.011"
			#node Group.006
			group_006 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeGroup")
			group_006.name = "Group.006"
			group_006.node_tree = _base_align
			
			#node Transform
			transform = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeTransform")
			transform.name = "Transform"
			transform.mode = 'COMPONENTS'
			#Rotation
			transform.inputs[2].default_value = (0.0, 0.0, 0.7853981852531433)
			#Scale
			transform.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Instance on Points
			instance_on_points_2 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInstanceOnPoints")
			instance_on_points_2.name = "Instance on Points"
			#Selection
			instance_on_points_2.inputs[1].default_value = True
			#Pick Instance
			instance_on_points_2.inputs[3].default_value = False
			#Instance Index
			instance_on_points_2.inputs[4].default_value = 0
			
			#node Group.003
			group_003 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeGroup")
			group_003.name = "Group.003"
			group_003.node_tree = _sampleatomvalue
			#Input_1
			group_003.inputs[1].default_value = 55
			
			#node Combine XYZ.001
			combine_xyz_001 = _mn_utils_style_ribbon_nucleic.nodes.new("ShaderNodeCombineXYZ")
			combine_xyz_001.name = "Combine XYZ.001"
			#X
			combine_xyz_001.inputs[0].default_value = 0.019999999552965164
			#Y
			combine_xyz_001.inputs[1].default_value = 0.10000000149011612
			
			#node Vector Math.003
			vector_math_003 = _mn_utils_style_ribbon_nucleic.nodes.new("ShaderNodeVectorMath")
			vector_math_003.name = "Vector Math.003"
			vector_math_003.operation = 'LENGTH'
			
			#node Vector Math.001
			vector_math_001 = _mn_utils_style_ribbon_nucleic.nodes.new("ShaderNodeVectorMath")
			vector_math_001.name = "Vector Math.001"
			vector_math_001.operation = 'SUBTRACT'
			
			#node Align Euler to Vector.001
			align_euler_to_vector_001 = _mn_utils_style_ribbon_nucleic.nodes.new("FunctionNodeAlignEulerToVector")
			align_euler_to_vector_001.name = "Align Euler to Vector.001"
			align_euler_to_vector_001.axis = 'Y'
			align_euler_to_vector_001.pivot_axis = 'Z'
			#Factor
			align_euler_to_vector_001.inputs[1].default_value = 1.0
			
			#node Align Euler to Vector
			align_euler_to_vector = _mn_utils_style_ribbon_nucleic.nodes.new("FunctionNodeAlignEulerToVector")
			align_euler_to_vector.name = "Align Euler to Vector"
			align_euler_to_vector.axis = 'Z'
			align_euler_to_vector.pivot_axis = 'AUTO'
			#Rotation
			align_euler_to_vector.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Factor
			align_euler_to_vector.inputs[1].default_value = 1.0
			
			#node Named Attribute.007
			named_attribute_007_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_007_1.name = "Named Attribute.007"
			named_attribute_007_1.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_007_1.inputs[0].default_value = "vec_horizontal"
			
			#node Named Attribute.008
			named_attribute_008_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_008_1.name = "Named Attribute.008"
			named_attribute_008_1.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_008_1.inputs[0].default_value = "atom_interface"
			
			#node Capture Attribute.001
			capture_attribute_001_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute_001_1.name = "Capture Attribute.001"
			capture_attribute_001_1.active_index = 0
			capture_attribute_001_1.capture_items.clear()
			capture_attribute_001_1.capture_items.new('FLOAT', "Value")
			capture_attribute_001_1.capture_items["Value"].data_type = 'INT'
			capture_attribute_001_1.domain = 'POINT'
			
			#node Index
			index_2 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputIndex")
			index_2.name = "Index"
			
			#node Named Attribute.009
			named_attribute_009_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_009_1.name = "Named Attribute.009"
			named_attribute_009_1.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute_009_1.inputs[0].default_value = "Color"
			
			#node Sample Index.002
			sample_index_002_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSampleIndex")
			sample_index_002_1.name = "Sample Index.002"
			sample_index_002_1.clamp = False
			sample_index_002_1.data_type = 'FLOAT_COLOR'
			sample_index_002_1.domain = 'POINT'
			
			#node Reroute.004
			reroute_004_1 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_004_1.name = "Reroute.004"
			#node Set Shade Smooth
			set_shade_smooth_2 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSetShadeSmooth")
			set_shade_smooth_2.name = "Set Shade Smooth"
			set_shade_smooth_2.domain = 'FACE'
			#Selection
			set_shade_smooth_2.inputs[1].default_value = True
			
			#node Reroute.007
			reroute_007_1 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_007_1.name = "Reroute.007"
			#node Curve Circle
			curve_circle_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeCurvePrimitiveCircle")
			curve_circle_1.name = "Curve Circle"
			curve_circle_1.hide = True
			curve_circle_1.mode = 'RADIUS'
			#Radius
			curve_circle_1.inputs[4].default_value = 0.009999999776482582
			
			#node Group Input.003
			group_input_003_2 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeGroupInput")
			group_input_003_2.name = "Group Input.003"
			group_input_003_2.outputs[0].hide = True
			group_input_003_2.outputs[1].hide = True
			group_input_003_2.outputs[2].hide = True
			group_input_003_2.outputs[3].hide = True
			group_input_003_2.outputs[4].hide = True
			group_input_003_2.outputs[6].hide = True
			group_input_003_2.outputs[7].hide = True
			group_input_003_2.outputs[8].hide = True
			group_input_003_2.outputs[9].hide = True
			group_input_003_2.outputs[10].hide = True
			
			#node Set Material
			set_material_3 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSetMaterial")
			set_material_3.name = "Set Material"
			#Selection
			set_material_3.inputs[1].default_value = True
			
			#node Reroute.005
			reroute_005_1 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_005_1.name = "Reroute.005"
			#node Reroute.008
			reroute_008_1 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_008_1.name = "Reroute.008"
			#node Curve to Mesh
			curve_to_mesh_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeCurveToMesh")
			curve_to_mesh_1.name = "Curve to Mesh"
			#Fill Caps
			curve_to_mesh_1.inputs[2].default_value = True
			
			#node Set Curve Radius
			set_curve_radius_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSetCurveRadius")
			set_curve_radius_1.name = "Set Curve Radius"
			#Selection
			set_curve_radius_1.inputs[1].default_value = True
			
			#node Group Input.002
			group_input_002_3 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeGroupInput")
			group_input_002_3.name = "Group Input.002"
			group_input_002_3.outputs[0].hide = True
			group_input_002_3.outputs[1].hide = True
			group_input_002_3.outputs[3].hide = True
			group_input_002_3.outputs[4].hide = True
			group_input_002_3.outputs[5].hide = True
			group_input_002_3.outputs[6].hide = True
			group_input_002_3.outputs[7].hide = True
			group_input_002_3.outputs[8].hide = True
			group_input_002_3.outputs[9].hide = True
			group_input_002_3.outputs[10].hide = True
			
			#node Join Geometry.001
			join_geometry_001_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_001_1.name = "Join Geometry.001"
			join_geometry_001_1.hide = True
			
			#node Reroute.013
			reroute_013_1 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_013_1.name = "Reroute.013"
			#node Store Named Attribute.011
			store_named_attribute_011 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_011.name = "Store Named Attribute.011"
			store_named_attribute_011.data_type = 'FLOAT_COLOR'
			store_named_attribute_011.domain = 'FACE'
			#Selection
			store_named_attribute_011.inputs[1].default_value = True
			#Name
			store_named_attribute_011.inputs[2].default_value = "Color"
			
			#node Switch.001
			switch_001_2 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSwitch")
			switch_001_2.name = "Switch.001"
			switch_001_2.input_type = 'GEOMETRY'
			
			#node Group Input.001
			group_input_001_4 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeGroupInput")
			group_input_001_4.name = "Group Input.001"
			group_input_001_4.outputs[0].hide = True
			group_input_001_4.outputs[1].hide = True
			group_input_001_4.outputs[2].hide = True
			group_input_001_4.outputs[4].hide = True
			group_input_001_4.outputs[5].hide = True
			group_input_001_4.outputs[6].hide = True
			group_input_001_4.outputs[7].hide = True
			group_input_001_4.outputs[8].hide = True
			group_input_001_4.outputs[9].hide = True
			group_input_001_4.outputs[10].hide = True
			
			#node Group
			group_11 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeGroup")
			group_11.name = "Group"
			group_11.node_tree = residue_mask
			#Socket_1
			group_11.inputs[0].default_value = 1
			#Socket_5
			group_11.inputs[1].default_value = True
			#Socket_4
			group_11.inputs[2].default_value = 0
			
			#node Is Nucleic
			is_nucleic_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeGroup")
			is_nucleic_1.label = "Is Nucleic"
			is_nucleic_1.name = "Is Nucleic"
			is_nucleic_1.node_tree = is_nucleic
			#Socket_3
			is_nucleic_1.inputs[1].default_value = False
			
			#node Group.005
			group_005 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeGroup")
			group_005.name = "Group.005"
			group_005.node_tree = _sampleatomvalue
			#Input_1
			group_005.inputs[1].default_value = 57
			
			#node Reroute
			reroute_3 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_3.name = "Reroute"
			#node Mix
			mix = _mn_utils_style_ribbon_nucleic.nodes.new("ShaderNodeMix")
			mix.name = "Mix"
			mix.blend_type = 'MIX'
			mix.clamp_factor = True
			mix.clamp_result = False
			mix.data_type = 'VECTOR'
			mix.factor_mode = 'UNIFORM'
			#Factor_Float
			mix.inputs[0].default_value = 1.0
			
			
			
			#Set parents
			sample_index_1.parent = frame_002_2
			named_attribute_002_3.parent = frame_002_2
			sample_index_004.parent = frame_002_2
			named_attribute_004_1.parent = frame_002_2
			sample_index_001_2.parent = frame_002_2
			named_attribute_8.parent = frame_002_2
			reroute_003_2.parent = frame_002_2
			sample_index_003_1.parent = frame_002_2
			named_attribute_003_1.parent = frame_002_2
			index_003_1.parent = frame_002_2
			named_attribute_005_1.parent = frame_002_2
			sample_index_005_1.parent = frame_002_2
			reroute_001_4.parent = frame_002_2
			sample_index_008_1.parent = frame_4
			named_attribute_006_1.parent = frame_4
			index_004.parent = frame_4
			reroute_002_4.parent = frame_4
			edge_vertices_1.parent = frame_4
			field_at_index.parent = frame_4
			field_at_index_001.parent = frame_4
			vector_math_1.parent = frame_4
			compare_001_3.parent = frame_4
			compare_4.parent = frame_4
			boolean_math_4.parent = frame_4
			mesh_line_1.parent = frame_001_2
			set_position_1.parent = frame_001_2
			domain_size_2.parent = frame_001_2
			delete_geometry.parent = frame_4
			offset_point_in_curve.parent = frame_006
			evaluate_at_index_1.parent = frame_006
			position_002_2.parent = frame_006
			vector_math_002_1.parent = frame_006
			vector_math_004_1.parent = frame_006
			endpoint_selection.parent = frame_006
			switch_6.parent = frame_006
			endpoint_selection_001.parent = frame_006
			set_position_001.parent = frame_006
			set_handle_type.parent = frame_004_1
			set_spline_type.parent = frame_004_1
			group_input_004_1.parent = frame_004_1
			mesh_to_curve_1.parent = frame_004_1
			set_spline_resolution.parent = frame_004_1
			combine_xyz.parent = frame_005_1
			math_7.parent = frame_005_1
			cylinder.parent = frame_005_1
			value_1.parent = frame_005_1
			group_input_005_1.parent = frame_005_1
			store_named_attribute_006_1.parent = frame_005_1
			position_001_1.parent = frame_007
			transform.parent = frame_005_1
			instance_on_points_2.parent = frame_005_1
			combine_xyz_001.parent = frame_007
			vector_math_003.parent = frame_007
			vector_math_001.parent = frame_007
			align_euler_to_vector_001.parent = frame_007
			align_euler_to_vector.parent = frame_007
			named_attribute_007_1.parent = frame_007
			named_attribute_008_1.parent = frame_007
			reroute_004_1.parent = frame_003_2
			set_shade_smooth_2.parent = frame_003_2
			reroute_007_1.parent = frame_003_2
			curve_circle_1.parent = frame_003_2
			group_input_003_2.parent = frame_003_2
			reroute_005_1.parent = frame_003_2
			reroute_008_1.parent = frame_003_2
			curve_to_mesh_1.parent = frame_003_2
			set_curve_radius_1.parent = frame_003_2
			group_input_002_3.parent = frame_003_2
			join_geometry_001_1.parent = frame_003_2
			reroute_013_1.parent = frame_003_2
			
			#Set locations
			frame_002_2.location = (1158.6292724609375, -29.90658187866211)
			frame_4.location = (-740.1123657226562, 293.3905944824219)
			frame_001_2.location = (-721.0, 75.0)
			frame_006.location = (252.1446533203125, -22.4365234375)
			frame_004_1.location = (-210.0, 260.0)
			frame_005_1.location = (397.0, 475.0)
			frame_007.location = (2083.0, 37.0)
			frame_003_2.location = (58.0, -11.0)
			sample_index_1.location = (-660.0, 820.0)
			named_attribute_002_3.location = (-660.0, 780.0)
			sample_index_004.location = (-660.0, 880.0)
			named_attribute_004_1.location = (-660.0, 920.0)
			sample_index_001_2.location = (-664.6292724609375, 689.9065551757812)
			named_attribute_8.location = (-664.6292724609375, 729.9065551757812)
			reroute_003_2.location = (-784.6292724609375, 869.9065551757812)
			sample_index_003_1.location = (-660.0, 980.0)
			named_attribute_003_1.location = (-660.0, 1020.0)
			index_003_1.location = (-964.6292724609375, 909.9065551757812)
			named_attribute_005_1.location = (-664.6292724609375, 1109.9066162109375)
			sample_index_005_1.location = (-664.6292724609375, 1069.9066162109375)
			reroute_001_4.location = (-804.6292724609375, 969.9065551757812)
			reroute_010_1.location = (-6.0, 640.0)
			sample_index_008_1.location = (-259.96295166015625, -143.635009765625)
			named_attribute_006_1.location = (-439.96295166015625, -143.635009765625)
			index_004.location = (-439.96295166015625, -183.635009765625)
			reroute_002_4.location = (-100.0, -140.0)
			edge_vertices_1.location = (-220.0, -220.0)
			field_at_index.location = (0.0, 0.0)
			field_at_index_001.location = (0.0, -160.0)
			vector_math_1.location = (0.0, -320.0)
			compare_001_3.location = (160.0, -160.0)
			compare_4.location = (160.0, 0.0)
			boolean_math_4.location = (320.0, 0.0)
			reroute_009_1.location = (-1531.0, 160.0)
			reroute_012_1.location = (-1691.0, 640.0)
			mesh_line_1.location = (-690.0, 385.0)
			set_position_1.location = (-690.0, 345.0)
			domain_size_2.location = (-690.0, 425.0)
			delete_geometry.location = (320.0, 220.0)
			sample_index_009_2.location = (500.0, 1180.0)
			group_input_006.location = (280.0, 1260.0)
			sample_index_007_1.location = (500.0, 1240.0)
			group_output_24.location = (4000.0, 540.0)
			offset_point_in_curve.location = (1740.0, 1060.0)
			evaluate_at_index_1.location = (1900.0, 1060.0)
			position_002_2.location = (1740.0, 940.0)
			vector_math_002_1.location = (2060.0, 1060.0)
			vector_math_004_1.location = (1900.0, 900.0)
			endpoint_selection.location = (2067.57958984375, 912.9168701171875)
			switch_6.location = (1580.0, 1060.0)
			endpoint_selection_001.location = (1420.0, 1060.0)
			set_position_001.location = (2240.0, 1060.0)
			store_named_attribute_001_1.location = (1280.0, 620.0)
			store_named_attribute_002_1.location = (1440.0, 620.0)
			store_named_attribute_003_1.location = (1600.0, 620.0)
			store_named_attribute_004_1.location = (1760.0, 620.0)
			capture_attribute_2.location = (1940.0, 620.0)
			set_handle_type.location = (840.0, 260.0)
			set_spline_type.location = (670.0, 260.0)
			group_input_004_1.location = (1010.0, 120.0)
			mesh_to_curve_1.location = (510.0, 260.0)
			set_spline_resolution.location = (1010.0, 260.0)
			store_named_attribute_2.location = (1120.0, 620.0)
			store_named_attribute_007.location = (360.0, 40.0)
			store_named_attribute_008.location = (180.0, 40.0)
			store_named_attribute_009.location = (20.0, 40.0)
			store_named_attribute_010.location = (-140.0, 40.0)
			combine_xyz.location = (114.9571533203125, -1317.4541015625)
			math_7.location = (114.9571533203125, -1457.4541015625)
			cylinder.location = (-45.042877197265625, -1237.4541015625)
			value_1.location = (-59.143829345703125, -1534.919921875)
			group_input_005_1.location = (-246.84564208984375, -1389.357421875)
			store_named_attribute_006_1.location = (120.856201171875, -1094.919921875)
			position_001_1.location = (-1639.0, -1617.0)
			store_named_attribute_005_1.location = (540.0, 40.0)
			separate_geometry_5.location = (-2960.0, 0.0)
			group_input_24.location = (-3360.0, -60.0)
			group_004.location = (340.0, -200.0)
			reroute_006_1.location = (-260.0, -380.0)
			reroute_011_1.location = (240.0, -380.0)
			group_006.location = (-220.0, -180.0)
			transform.location = (314.9571533203125, -1217.4541015625)
			instance_on_points_2.location = (827.0, -1386.0)
			group_003.location = (-2100.0, 660.0)
			combine_xyz_001.location = (-1123.0, -1517.0)
			vector_math_003.location = (-1283.0, -1517.0)
			vector_math_001.location = (-1443.0, -1517.0)
			align_euler_to_vector_001.location = (-1123.0, -1297.0)
			align_euler_to_vector.location = (-1283.0, -1297.0)
			named_attribute_007_1.location = (-1678.014892578125, -1337.0)
			named_attribute_008_1.location = (-1679.2340087890625, -1477.0)
			capture_attribute_001_1.location = (2806.529052734375, 1155.515625)
			index_2.location = (2800.0, 960.0)
			named_attribute_009_1.location = (3040.0, 1000.0)
			sample_index_002_1.location = (3040.0, 1220.0)
			reroute_004_1.location = (2300.0, 400.0)
			set_shade_smooth_2.location = (2885.609130859375, 590.6487426757812)
			reroute_007_1.location = (2846.0, 400.0)
			curve_circle_1.location = (2546.0, 500.0)
			group_input_003_2.location = (2546.0, 460.0)
			set_material_3.location = (3380.0, 660.0)
			reroute_005_1.location = (3462.0, 231.0)
			reroute_008_1.location = (2862.0, 231.0)
			curve_to_mesh_1.location = (2722.0, 591.0)
			set_curve_radius_1.location = (2162.0, 631.0)
			group_input_002_3.location = (3322.0, 531.0)
			join_geometry_001_1.location = (3122.0, 551.0)
			reroute_013_1.location = (3074.18017578125, 548.1685791015625)
			store_named_attribute_011.location = (2940.4248046875, 856.4732666015625)
			switch_001_2.location = (3100.0, 860.0)
			group_input_001_4.location = (3100.0, 940.0)
			group_11.location = (-2840.0, 520.0)
			is_nucleic_1.location = (-3180.0, -120.0)
			group_005.location = (-2100.0, 480.0)
			reroute_3.location = (-2180.0, 540.0)
			mix.location = (-1827.638427734375, 608.8980102539062)
			
			#Set dimensions
			frame_002_2.width, frame_002_2.height = 504.5, 520.0000610351562
			frame_4.width, frame_4.height = 960.0, 734.0
			frame_001_2.width, frame_001_2.height = 200.0, 180.0
			frame_006.width, frame_006.height = 1020.0001220703125, 354.0
			frame_004_1.width, frame_004_1.height = 700.0, 262.0
			frame_005_1.width, frame_005_1.height = 1274.0, 590.0
			frame_007.width, frame_007.height = 756.0, 440.0
			frame_003_2.width, frame_003_2.height = 1364.0, 474.0
			sample_index_1.width, sample_index_1.height = 140.0, 100.0
			named_attribute_002_3.width, named_attribute_002_3.height = 140.0, 100.0
			sample_index_004.width, sample_index_004.height = 140.0, 100.0
			named_attribute_004_1.width, named_attribute_004_1.height = 140.0, 100.0
			sample_index_001_2.width, sample_index_001_2.height = 140.0, 100.0
			named_attribute_8.width, named_attribute_8.height = 140.0, 100.0
			reroute_003_2.width, reroute_003_2.height = 16.0, 100.0
			sample_index_003_1.width, sample_index_003_1.height = 140.0, 100.0
			named_attribute_003_1.width, named_attribute_003_1.height = 140.0, 100.0
			index_003_1.width, index_003_1.height = 140.0, 100.0
			named_attribute_005_1.width, named_attribute_005_1.height = 140.0, 100.0
			sample_index_005_1.width, sample_index_005_1.height = 140.0, 100.0
			reroute_001_4.width, reroute_001_4.height = 16.0, 100.0
			reroute_010_1.width, reroute_010_1.height = 16.0, 100.0
			sample_index_008_1.width, sample_index_008_1.height = 140.0, 100.0
			named_attribute_006_1.width, named_attribute_006_1.height = 140.0, 100.0
			index_004.width, index_004.height = 140.0, 100.0
			reroute_002_4.width, reroute_002_4.height = 16.0, 100.0
			edge_vertices_1.width, edge_vertices_1.height = 140.0, 100.0
			field_at_index.width, field_at_index.height = 140.0, 100.0
			field_at_index_001.width, field_at_index_001.height = 140.0, 100.0
			vector_math_1.width, vector_math_1.height = 140.0, 100.0
			compare_001_3.width, compare_001_3.height = 140.0, 100.0
			compare_4.width, compare_4.height = 140.0, 100.0
			boolean_math_4.width, boolean_math_4.height = 140.0, 100.0
			reroute_009_1.width, reroute_009_1.height = 16.0, 100.0
			reroute_012_1.width, reroute_012_1.height = 16.0, 100.0
			mesh_line_1.width, mesh_line_1.height = 140.0, 100.0
			set_position_1.width, set_position_1.height = 140.0, 100.0
			domain_size_2.width, domain_size_2.height = 140.0, 100.0
			delete_geometry.width, delete_geometry.height = 140.0, 100.0
			sample_index_009_2.width, sample_index_009_2.height = 140.0, 100.0
			group_input_006.width, group_input_006.height = 140.0, 100.0
			sample_index_007_1.width, sample_index_007_1.height = 140.0, 100.0
			group_output_24.width, group_output_24.height = 140.0, 100.0
			offset_point_in_curve.width, offset_point_in_curve.height = 140.0, 100.0
			evaluate_at_index_1.width, evaluate_at_index_1.height = 140.0, 100.0
			position_002_2.width, position_002_2.height = 140.0, 100.0
			vector_math_002_1.width, vector_math_002_1.height = 140.0, 100.0
			vector_math_004_1.width, vector_math_004_1.height = 140.0, 100.0
			endpoint_selection.width, endpoint_selection.height = 140.0, 100.0
			switch_6.width, switch_6.height = 140.0, 100.0
			endpoint_selection_001.width, endpoint_selection_001.height = 140.0, 100.0
			set_position_001.width, set_position_001.height = 140.0, 100.0
			store_named_attribute_001_1.width, store_named_attribute_001_1.height = 140.0, 100.0
			store_named_attribute_002_1.width, store_named_attribute_002_1.height = 140.0, 100.0
			store_named_attribute_003_1.width, store_named_attribute_003_1.height = 140.0, 100.0
			store_named_attribute_004_1.width, store_named_attribute_004_1.height = 140.0, 100.0
			capture_attribute_2.width, capture_attribute_2.height = 140.0, 100.0
			set_handle_type.width, set_handle_type.height = 140.0, 100.0
			set_spline_type.width, set_spline_type.height = 140.0, 100.0
			group_input_004_1.width, group_input_004_1.height = 140.0, 100.0
			mesh_to_curve_1.width, mesh_to_curve_1.height = 140.0, 100.0
			set_spline_resolution.width, set_spline_resolution.height = 140.0, 100.0
			store_named_attribute_2.width, store_named_attribute_2.height = 140.0, 100.0
			store_named_attribute_007.width, store_named_attribute_007.height = 140.0, 100.0
			store_named_attribute_008.width, store_named_attribute_008.height = 140.0, 100.0
			store_named_attribute_009.width, store_named_attribute_009.height = 140.0, 100.0
			store_named_attribute_010.width, store_named_attribute_010.height = 140.0, 100.0
			combine_xyz.width, combine_xyz.height = 140.0, 100.0
			math_7.width, math_7.height = 140.0, 100.0
			cylinder.width, cylinder.height = 140.0, 100.0
			value_1.width, value_1.height = 140.0, 100.0
			group_input_005_1.width, group_input_005_1.height = 140.0, 100.0
			store_named_attribute_006_1.width, store_named_attribute_006_1.height = 140.0, 100.0
			position_001_1.width, position_001_1.height = 140.0, 100.0
			store_named_attribute_005_1.width, store_named_attribute_005_1.height = 140.0, 100.0
			separate_geometry_5.width, separate_geometry_5.height = 140.0, 100.0
			group_input_24.width, group_input_24.height = 140.0, 100.0
			group_004.width, group_004.height = 176.54052734375, 100.0
			reroute_006_1.width, reroute_006_1.height = 16.0, 100.0
			reroute_011_1.width, reroute_011_1.height = 16.0, 100.0
			group_006.width, group_006.height = 223.4932861328125, 100.0
			transform.width, transform.height = 140.0, 100.0
			instance_on_points_2.width, instance_on_points_2.height = 140.0, 100.0
			group_003.width, group_003.height = 219.859375, 100.0
			combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
			vector_math_003.width, vector_math_003.height = 140.0, 100.0
			vector_math_001.width, vector_math_001.height = 140.0, 100.0
			align_euler_to_vector_001.width, align_euler_to_vector_001.height = 140.0, 100.0
			align_euler_to_vector.width, align_euler_to_vector.height = 140.0, 100.0
			named_attribute_007_1.width, named_attribute_007_1.height = 179.014892578125, 100.0
			named_attribute_008_1.width, named_attribute_008_1.height = 180.2340087890625, 100.0
			capture_attribute_001_1.width, capture_attribute_001_1.height = 140.0, 100.0
			index_2.width, index_2.height = 140.0, 100.0
			named_attribute_009_1.width, named_attribute_009_1.height = 140.0, 100.0
			sample_index_002_1.width, sample_index_002_1.height = 140.0, 100.0
			reroute_004_1.width, reroute_004_1.height = 16.0, 100.0
			set_shade_smooth_2.width, set_shade_smooth_2.height = 140.0, 100.0
			reroute_007_1.width, reroute_007_1.height = 16.0, 100.0
			curve_circle_1.width, curve_circle_1.height = 140.0, 100.0
			group_input_003_2.width, group_input_003_2.height = 140.0, 100.0
			set_material_3.width, set_material_3.height = 140.0, 100.0
			reroute_005_1.width, reroute_005_1.height = 16.0, 100.0
			reroute_008_1.width, reroute_008_1.height = 16.0, 100.0
			curve_to_mesh_1.width, curve_to_mesh_1.height = 140.0, 100.0
			set_curve_radius_1.width, set_curve_radius_1.height = 140.0, 100.0
			group_input_002_3.width, group_input_002_3.height = 140.0, 100.0
			join_geometry_001_1.width, join_geometry_001_1.height = 140.0, 100.0
			reroute_013_1.width, reroute_013_1.height = 16.0, 100.0
			store_named_attribute_011.width, store_named_attribute_011.height = 140.0, 100.0
			switch_001_2.width, switch_001_2.height = 140.0, 100.0
			group_input_001_4.width, group_input_001_4.height = 140.0, 100.0
			group_11.width, group_11.height = 140.0, 100.0
			is_nucleic_1.width, is_nucleic_1.height = 180.0, 100.0
			group_005.width, group_005.height = 219.859375, 100.0
			reroute_3.width, reroute_3.height = 16.0, 100.0
			mix.width, mix.height = 140.0, 100.0
			
			#initialize _mn_utils_style_ribbon_nucleic links
			#mesh_line_1.Mesh -> set_position_1.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(mesh_line_1.outputs[0], set_position_1.inputs[0])
			#reroute_012_1.Output -> domain_size_2.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_012_1.outputs[0], domain_size_2.inputs[0])
			#domain_size_2.Point Count -> mesh_line_1.Count
			_mn_utils_style_ribbon_nucleic.links.new(domain_size_2.outputs[0], mesh_line_1.inputs[0])
			#set_position_1.Geometry -> delete_geometry.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(set_position_1.outputs[0], delete_geometry.inputs[0])
			#named_attribute_002_3.Attribute -> sample_index_1.Value
			_mn_utils_style_ribbon_nucleic.links.new(named_attribute_002_3.outputs[0], sample_index_1.inputs[1])
			#edge_vertices_1.Vertex Index 1 -> field_at_index.Index
			_mn_utils_style_ribbon_nucleic.links.new(edge_vertices_1.outputs[0], field_at_index.inputs[0])
			#reroute_002_4.Output -> field_at_index.Value
			_mn_utils_style_ribbon_nucleic.links.new(reroute_002_4.outputs[0], field_at_index.inputs[1])
			#reroute_002_4.Output -> field_at_index_001.Value
			_mn_utils_style_ribbon_nucleic.links.new(reroute_002_4.outputs[0], field_at_index_001.inputs[1])
			#edge_vertices_1.Vertex Index 2 -> field_at_index_001.Index
			_mn_utils_style_ribbon_nucleic.links.new(edge_vertices_1.outputs[1], field_at_index_001.inputs[0])
			#field_at_index.Value -> compare_4.A
			_mn_utils_style_ribbon_nucleic.links.new(field_at_index.outputs[0], compare_4.inputs[2])
			#field_at_index_001.Value -> compare_4.B
			_mn_utils_style_ribbon_nucleic.links.new(field_at_index_001.outputs[0], compare_4.inputs[3])
			#edge_vertices_1.Position 1 -> vector_math_1.Vector
			_mn_utils_style_ribbon_nucleic.links.new(edge_vertices_1.outputs[2], vector_math_1.inputs[0])
			#edge_vertices_1.Position 2 -> vector_math_1.Vector
			_mn_utils_style_ribbon_nucleic.links.new(edge_vertices_1.outputs[3], vector_math_1.inputs[1])
			#compare_4.Result -> boolean_math_4.Boolean
			_mn_utils_style_ribbon_nucleic.links.new(compare_4.outputs[0], boolean_math_4.inputs[0])
			#boolean_math_4.Boolean -> delete_geometry.Selection
			_mn_utils_style_ribbon_nucleic.links.new(boolean_math_4.outputs[0], delete_geometry.inputs[1])
			#vector_math_1.Value -> compare_001_3.A
			_mn_utils_style_ribbon_nucleic.links.new(vector_math_1.outputs[1], compare_001_3.inputs[0])
			#compare_001_3.Result -> boolean_math_4.Boolean
			_mn_utils_style_ribbon_nucleic.links.new(compare_001_3.outputs[0], boolean_math_4.inputs[1])
			#store_named_attribute_007.Geometry -> mesh_to_curve_1.Mesh
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_007.outputs[0], mesh_to_curve_1.inputs[0])
			#mesh_to_curve_1.Curve -> set_spline_type.Curve
			_mn_utils_style_ribbon_nucleic.links.new(mesh_to_curve_1.outputs[0], set_spline_type.inputs[0])
			#set_handle_type.Curve -> set_spline_resolution.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(set_handle_type.outputs[0], set_spline_resolution.inputs[0])
			#curve_circle_1.Curve -> curve_to_mesh_1.Profile Curve
			_mn_utils_style_ribbon_nucleic.links.new(curve_circle_1.outputs[0], curve_to_mesh_1.inputs[1])
			#reroute_001_4.Output -> sample_index_001_2.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_001_4.outputs[0], sample_index_001_2.inputs[0])
			#named_attribute_8.Attribute -> sample_index_001_2.Value
			_mn_utils_style_ribbon_nucleic.links.new(named_attribute_8.outputs[0], sample_index_001_2.inputs[1])
			#join_geometry_001_1.Geometry -> set_material_3.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(join_geometry_001_1.outputs[0], set_material_3.inputs[0])
			#group_input_002_3.Material -> set_material_3.Material
			_mn_utils_style_ribbon_nucleic.links.new(group_input_002_3.outputs[2], set_material_3.inputs[2])
			#set_spline_type.Curve -> set_handle_type.Curve
			_mn_utils_style_ribbon_nucleic.links.new(set_spline_type.outputs[0], set_handle_type.inputs[0])
			#reroute_003_2.Output -> sample_index_001_2.Index
			_mn_utils_style_ribbon_nucleic.links.new(reroute_003_2.outputs[0], sample_index_001_2.inputs[2])
			#set_spline_resolution.Geometry -> store_named_attribute_2.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(set_spline_resolution.outputs[0], store_named_attribute_2.inputs[0])
			#sample_index_001_2.Value -> store_named_attribute_2.Value
			_mn_utils_style_ribbon_nucleic.links.new(sample_index_001_2.outputs[0], store_named_attribute_2.inputs[3])
			#store_named_attribute_2.Geometry -> store_named_attribute_001_1.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_2.outputs[0], store_named_attribute_001_1.inputs[0])
			#store_named_attribute_001_1.Geometry -> store_named_attribute_002_1.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_001_1.outputs[0], store_named_attribute_002_1.inputs[0])
			#store_named_attribute_002_1.Geometry -> store_named_attribute_003_1.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_002_1.outputs[0], store_named_attribute_003_1.inputs[0])
			#sample_index_1.Value -> store_named_attribute_001_1.Value
			_mn_utils_style_ribbon_nucleic.links.new(sample_index_1.outputs[0], store_named_attribute_001_1.inputs[3])
			#reroute_001_4.Output -> sample_index_003_1.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_001_4.outputs[0], sample_index_003_1.inputs[0])
			#named_attribute_003_1.Attribute -> sample_index_003_1.Value
			_mn_utils_style_ribbon_nucleic.links.new(named_attribute_003_1.outputs[0], sample_index_003_1.inputs[1])
			#reroute_003_2.Output -> sample_index_003_1.Index
			_mn_utils_style_ribbon_nucleic.links.new(reroute_003_2.outputs[0], sample_index_003_1.inputs[2])
			#sample_index_003_1.Value -> store_named_attribute_003_1.Value
			_mn_utils_style_ribbon_nucleic.links.new(sample_index_003_1.outputs[0], store_named_attribute_003_1.inputs[3])
			#reroute_001_4.Output -> sample_index_004.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_001_4.outputs[0], sample_index_004.inputs[0])
			#named_attribute_004_1.Attribute -> sample_index_004.Value
			_mn_utils_style_ribbon_nucleic.links.new(named_attribute_004_1.outputs[0], sample_index_004.inputs[1])
			#reroute_003_2.Output -> sample_index_004.Index
			_mn_utils_style_ribbon_nucleic.links.new(reroute_003_2.outputs[0], sample_index_004.inputs[2])
			#sample_index_004.Value -> store_named_attribute_002_1.Value
			_mn_utils_style_ribbon_nucleic.links.new(sample_index_004.outputs[0], store_named_attribute_002_1.inputs[3])
			#reroute_010_1.Output -> reroute_001_4.Input
			_mn_utils_style_ribbon_nucleic.links.new(reroute_010_1.outputs[0], reroute_001_4.inputs[0])
			#index_003_1.Index -> reroute_003_2.Input
			_mn_utils_style_ribbon_nucleic.links.new(index_003_1.outputs[0], reroute_003_2.inputs[0])
			#reroute_003_2.Output -> sample_index_1.Index
			_mn_utils_style_ribbon_nucleic.links.new(reroute_003_2.outputs[0], sample_index_1.inputs[2])
			#store_named_attribute_003_1.Geometry -> store_named_attribute_004_1.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_003_1.outputs[0], store_named_attribute_004_1.inputs[0])
			#reroute_001_4.Output -> sample_index_005_1.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_001_4.outputs[0], sample_index_005_1.inputs[0])
			#reroute_003_2.Output -> sample_index_005_1.Index
			_mn_utils_style_ribbon_nucleic.links.new(reroute_003_2.outputs[0], sample_index_005_1.inputs[2])
			#named_attribute_005_1.Attribute -> sample_index_005_1.Value
			_mn_utils_style_ribbon_nucleic.links.new(named_attribute_005_1.outputs[0], sample_index_005_1.inputs[1])
			#sample_index_005_1.Value -> store_named_attribute_004_1.Value
			_mn_utils_style_ribbon_nucleic.links.new(sample_index_005_1.outputs[0], store_named_attribute_004_1.inputs[3])
			#store_named_attribute_004_1.Geometry -> capture_attribute_2.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_004_1.outputs[0], capture_attribute_2.inputs[0])
			#capture_attribute_2.Geometry -> set_curve_radius_1.Curve
			_mn_utils_style_ribbon_nucleic.links.new(capture_attribute_2.outputs[0], set_curve_radius_1.inputs[0])
			#reroute_007_1.Output -> set_shade_smooth_2.Shade Smooth
			_mn_utils_style_ribbon_nucleic.links.new(reroute_007_1.outputs[0], set_shade_smooth_2.inputs[2])
			#capture_attribute_2.Value -> reroute_004_1.Input
			_mn_utils_style_ribbon_nucleic.links.new(capture_attribute_2.outputs[1], reroute_004_1.inputs[0])
			#reroute_004_1.Output -> reroute_007_1.Input
			_mn_utils_style_ribbon_nucleic.links.new(reroute_004_1.outputs[0], reroute_007_1.inputs[0])
			#reroute_001_4.Output -> sample_index_1.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_001_4.outputs[0], sample_index_1.inputs[0])
			#named_attribute_006_1.Attribute -> sample_index_008_1.Value
			_mn_utils_style_ribbon_nucleic.links.new(named_attribute_006_1.outputs[0], sample_index_008_1.inputs[1])
			#reroute_009_1.Output -> sample_index_008_1.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_009_1.outputs[0], sample_index_008_1.inputs[0])
			#index_004.Index -> sample_index_008_1.Index
			_mn_utils_style_ribbon_nucleic.links.new(index_004.outputs[0], sample_index_008_1.inputs[2])
			#sample_index_008_1.Value -> reroute_002_4.Input
			_mn_utils_style_ribbon_nucleic.links.new(sample_index_008_1.outputs[0], reroute_002_4.inputs[0])
			#reroute_012_1.Output -> reroute_009_1.Input
			_mn_utils_style_ribbon_nucleic.links.new(reroute_012_1.outputs[0], reroute_009_1.inputs[0])
			#reroute_012_1.Output -> reroute_010_1.Input
			_mn_utils_style_ribbon_nucleic.links.new(reroute_012_1.outputs[0], reroute_010_1.inputs[0])
			#curve_to_mesh_1.Mesh -> set_shade_smooth_2.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(curve_to_mesh_1.outputs[0], set_shade_smooth_2.inputs[0])
			#group_003.Atoms -> reroute_012_1.Input
			_mn_utils_style_ribbon_nucleic.links.new(group_003.outputs[0], reroute_012_1.inputs[0])
			#store_named_attribute_006_1.Geometry -> transform.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_006_1.outputs[0], transform.inputs[0])
			#combine_xyz.Vector -> transform.Translation
			_mn_utils_style_ribbon_nucleic.links.new(combine_xyz.outputs[0], transform.inputs[1])
			#value_1.Value -> math_7.Value
			_mn_utils_style_ribbon_nucleic.links.new(value_1.outputs[0], math_7.inputs[0])
			#value_1.Value -> cylinder.Depth
			_mn_utils_style_ribbon_nucleic.links.new(value_1.outputs[0], cylinder.inputs[4])
			#math_7.Value -> combine_xyz.Z
			_mn_utils_style_ribbon_nucleic.links.new(math_7.outputs[0], combine_xyz.inputs[2])
			#align_euler_to_vector_001.Rotation -> instance_on_points_2.Rotation
			_mn_utils_style_ribbon_nucleic.links.new(align_euler_to_vector_001.outputs[0], instance_on_points_2.inputs[5])
			#combine_xyz_001.Vector -> instance_on_points_2.Scale
			_mn_utils_style_ribbon_nucleic.links.new(combine_xyz_001.outputs[0], instance_on_points_2.inputs[6])
			#set_material_3.Geometry -> group_output_24.Ribbon + Bases
			_mn_utils_style_ribbon_nucleic.links.new(set_material_3.outputs[0], group_output_24.inputs[0])
			#store_named_attribute_005_1.Geometry -> instance_on_points_2.Points
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_005_1.outputs[0], instance_on_points_2.inputs[0])
			#reroute_013_1.Output -> join_geometry_001_1.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_013_1.outputs[0], join_geometry_001_1.inputs[0])
			#group_input_005_1.Base Radius -> cylinder.Radius
			_mn_utils_style_ribbon_nucleic.links.new(group_input_005_1.outputs[8], cylinder.inputs[3])
			#group_input_005_1.Base Resolution -> cylinder.Vertices
			_mn_utils_style_ribbon_nucleic.links.new(group_input_005_1.outputs[9], cylinder.inputs[0])
			#reroute_005_1.Output -> group_output_24.Ribbon Curve
			_mn_utils_style_ribbon_nucleic.links.new(reroute_005_1.outputs[0], group_output_24.inputs[1])
			#transform.Geometry -> instance_on_points_2.Instance
			_mn_utils_style_ribbon_nucleic.links.new(transform.outputs[0], instance_on_points_2.inputs[2])
			#cylinder.Mesh -> store_named_attribute_006_1.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(cylinder.outputs[0], store_named_attribute_006_1.inputs[0])
			#cylinder.UV Map -> store_named_attribute_006_1.Value
			_mn_utils_style_ribbon_nucleic.links.new(cylinder.outputs[4], store_named_attribute_006_1.inputs[3])
			#group_input_24.Atoms -> separate_geometry_5.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(group_input_24.outputs[0], separate_geometry_5.inputs[0])
			#reroute_3.Output -> group_003.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_3.outputs[0], group_003.inputs[0])
			#group_004.Value -> store_named_attribute_005_1.Value
			_mn_utils_style_ribbon_nucleic.links.new(group_004.outputs[2], store_named_attribute_005_1.inputs[3])
			#group_input_003_2.Backbone Resolution -> curve_circle_1.Resolution
			_mn_utils_style_ribbon_nucleic.links.new(group_input_003_2.outputs[5], curve_circle_1.inputs[0])
			#position_001_1.Position -> vector_math_001.Vector
			_mn_utils_style_ribbon_nucleic.links.new(position_001_1.outputs[0], vector_math_001.inputs[1])
			#set_curve_radius_1.Curve -> set_position_001.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(set_curve_radius_1.outputs[0], set_position_001.inputs[0])
			#position_002_2.Position -> evaluate_at_index_1.Value
			_mn_utils_style_ribbon_nucleic.links.new(position_002_2.outputs[0], evaluate_at_index_1.inputs[1])
			#offset_point_in_curve.Point Index -> evaluate_at_index_1.Index
			_mn_utils_style_ribbon_nucleic.links.new(offset_point_in_curve.outputs[1], evaluate_at_index_1.inputs[0])
			#evaluate_at_index_1.Value -> vector_math_002_1.Vector
			_mn_utils_style_ribbon_nucleic.links.new(evaluate_at_index_1.outputs[0], vector_math_002_1.inputs[0])
			#position_002_2.Position -> vector_math_002_1.Vector
			_mn_utils_style_ribbon_nucleic.links.new(position_002_2.outputs[0], vector_math_002_1.inputs[1])
			#vector_math_002_1.Vector -> vector_math_004_1.Vector
			_mn_utils_style_ribbon_nucleic.links.new(vector_math_002_1.outputs[0], vector_math_004_1.inputs[0])
			#vector_math_004_1.Vector -> set_position_001.Offset
			_mn_utils_style_ribbon_nucleic.links.new(vector_math_004_1.outputs[0], set_position_001.inputs[3])
			#endpoint_selection.Selection -> set_position_001.Selection
			_mn_utils_style_ribbon_nucleic.links.new(endpoint_selection.outputs[0], set_position_001.inputs[1])
			#endpoint_selection_001.Selection -> switch_6.Switch
			_mn_utils_style_ribbon_nucleic.links.new(endpoint_selection_001.outputs[0], switch_6.inputs[0])
			#switch_6.Output -> offset_point_in_curve.Offset
			_mn_utils_style_ribbon_nucleic.links.new(switch_6.outputs[0], offset_point_in_curve.inputs[1])
			#store_named_attribute_007.Geometry -> store_named_attribute_005_1.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_007.outputs[0], store_named_attribute_005_1.inputs[0])
			#group_input_004_1.Backbone Subdivisions -> set_spline_resolution.Resolution
			_mn_utils_style_ribbon_nucleic.links.new(group_input_004_1.outputs[4], set_spline_resolution.inputs[2])
			#reroute_001_4.Output -> sample_index_009_2.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_001_4.outputs[0], sample_index_009_2.inputs[0])
			#reroute_003_2.Output -> sample_index_009_2.Index
			_mn_utils_style_ribbon_nucleic.links.new(reroute_003_2.outputs[0], sample_index_009_2.inputs[2])
			#group_input_006.Backbone Shade Smooth -> sample_index_009_2.Value
			_mn_utils_style_ribbon_nucleic.links.new(group_input_006.outputs[7], sample_index_009_2.inputs[1])
			#sample_index_009_2.Value -> capture_attribute_2.Value
			_mn_utils_style_ribbon_nucleic.links.new(sample_index_009_2.outputs[0], capture_attribute_2.inputs[1])
			#group_input_006.Backbone Radius -> sample_index_007_1.Value
			_mn_utils_style_ribbon_nucleic.links.new(group_input_006.outputs[6], sample_index_007_1.inputs[1])
			#reroute_003_2.Output -> sample_index_007_1.Index
			_mn_utils_style_ribbon_nucleic.links.new(reroute_003_2.outputs[0], sample_index_007_1.inputs[2])
			#reroute_001_4.Output -> sample_index_007_1.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_001_4.outputs[0], sample_index_007_1.inputs[0])
			#sample_index_007_1.Value -> set_curve_radius_1.Radius
			_mn_utils_style_ribbon_nucleic.links.new(sample_index_007_1.outputs[0], set_curve_radius_1.inputs[2])
			#reroute_008_1.Output -> reroute_005_1.Input
			_mn_utils_style_ribbon_nucleic.links.new(reroute_008_1.outputs[0], reroute_005_1.inputs[0])
			#set_curve_radius_1.Curve -> reroute_008_1.Input
			_mn_utils_style_ribbon_nucleic.links.new(set_curve_radius_1.outputs[0], reroute_008_1.inputs[0])
			#store_named_attribute_008.Geometry -> store_named_attribute_007.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_008.outputs[0], store_named_attribute_007.inputs[0])
			#reroute_006_1.Output -> group_006.Input
			_mn_utils_style_ribbon_nucleic.links.new(reroute_006_1.outputs[0], group_006.inputs[0])
			#store_named_attribute_009.Geometry -> store_named_attribute_008.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_009.outputs[0], store_named_attribute_008.inputs[0])
			#group_006.Align Vertical -> store_named_attribute_008.Value
			_mn_utils_style_ribbon_nucleic.links.new(group_006.outputs[2], store_named_attribute_008.inputs[3])
			#group_006.Align Horizontal -> store_named_attribute_007.Value
			_mn_utils_style_ribbon_nucleic.links.new(group_006.outputs[3], store_named_attribute_007.inputs[3])
			#vector_math_001.Vector -> vector_math_003.Vector
			_mn_utils_style_ribbon_nucleic.links.new(vector_math_001.outputs[0], vector_math_003.inputs[0])
			#vector_math_003.Value -> combine_xyz_001.Z
			_mn_utils_style_ribbon_nucleic.links.new(vector_math_003.outputs[1], combine_xyz_001.inputs[2])
			#store_named_attribute_010.Geometry -> store_named_attribute_009.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_010.outputs[0], store_named_attribute_009.inputs[0])
			#group_006.Base Interface -> store_named_attribute_009.Value
			_mn_utils_style_ribbon_nucleic.links.new(group_006.outputs[0], store_named_attribute_009.inputs[3])
			#delete_geometry.Geometry -> store_named_attribute_010.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(delete_geometry.outputs[0], store_named_attribute_010.inputs[0])
			#group_006.Base Pivot -> store_named_attribute_010.Value
			_mn_utils_style_ribbon_nucleic.links.new(group_006.outputs[1], store_named_attribute_010.inputs[3])
			#named_attribute_008_1.Attribute -> vector_math_001.Vector
			_mn_utils_style_ribbon_nucleic.links.new(named_attribute_008_1.outputs[0], vector_math_001.inputs[0])
			#separate_geometry_5.Selection -> reroute_006_1.Input
			_mn_utils_style_ribbon_nucleic.links.new(separate_geometry_5.outputs[0], reroute_006_1.inputs[0])
			#reroute_011_1.Output -> group_004.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_011_1.outputs[0], group_004.inputs[0])
			#reroute_006_1.Output -> reroute_011_1.Input
			_mn_utils_style_ribbon_nucleic.links.new(reroute_006_1.outputs[0], reroute_011_1.inputs[0])
			#align_euler_to_vector.Rotation -> align_euler_to_vector_001.Rotation
			_mn_utils_style_ribbon_nucleic.links.new(align_euler_to_vector.outputs[0], align_euler_to_vector_001.inputs[0])
			#vector_math_001.Vector -> align_euler_to_vector.Vector
			_mn_utils_style_ribbon_nucleic.links.new(vector_math_001.outputs[0], align_euler_to_vector.inputs[2])
			#named_attribute_007_1.Attribute -> align_euler_to_vector_001.Vector
			_mn_utils_style_ribbon_nucleic.links.new(named_attribute_007_1.outputs[0], align_euler_to_vector_001.inputs[2])
			#set_position_001.Geometry -> capture_attribute_001_1.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(set_position_001.outputs[0], capture_attribute_001_1.inputs[0])
			#index_2.Index -> capture_attribute_001_1.Value
			_mn_utils_style_ribbon_nucleic.links.new(index_2.outputs[0], capture_attribute_001_1.inputs[1])
			#capture_attribute_001_1.Geometry -> curve_to_mesh_1.Curve
			_mn_utils_style_ribbon_nucleic.links.new(capture_attribute_001_1.outputs[0], curve_to_mesh_1.inputs[0])
			#set_shade_smooth_2.Geometry -> store_named_attribute_011.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(set_shade_smooth_2.outputs[0], store_named_attribute_011.inputs[0])
			#capture_attribute_001_1.Value -> sample_index_002_1.Index
			_mn_utils_style_ribbon_nucleic.links.new(capture_attribute_001_1.outputs[1], sample_index_002_1.inputs[2])
			#capture_attribute_001_1.Geometry -> sample_index_002_1.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(capture_attribute_001_1.outputs[0], sample_index_002_1.inputs[0])
			#named_attribute_009_1.Attribute -> sample_index_002_1.Value
			_mn_utils_style_ribbon_nucleic.links.new(named_attribute_009_1.outputs[0], sample_index_002_1.inputs[1])
			#sample_index_002_1.Value -> store_named_attribute_011.Value
			_mn_utils_style_ribbon_nucleic.links.new(sample_index_002_1.outputs[0], store_named_attribute_011.inputs[3])
			#store_named_attribute_011.Geometry -> switch_001_2.False
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_011.outputs[0], switch_001_2.inputs[1])
			#set_shade_smooth_2.Geometry -> switch_001_2.True
			_mn_utils_style_ribbon_nucleic.links.new(set_shade_smooth_2.outputs[0], switch_001_2.inputs[2])
			#switch_001_2.Output -> reroute_013_1.Input
			_mn_utils_style_ribbon_nucleic.links.new(switch_001_2.outputs[0], reroute_013_1.inputs[0])
			#group_input_001_4.Intepolate Color -> switch_001_2.Switch
			_mn_utils_style_ribbon_nucleic.links.new(group_input_001_4.outputs[3], switch_001_2.inputs[0])
			#group_input_24.Selection -> is_nucleic_1.And
			_mn_utils_style_ribbon_nucleic.links.new(group_input_24.outputs[1], is_nucleic_1.inputs[0])
			#is_nucleic_1.Selection -> separate_geometry_5.Selection
			_mn_utils_style_ribbon_nucleic.links.new(is_nucleic_1.outputs[0], separate_geometry_5.inputs[1])
			#reroute_3.Output -> group_005.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_3.outputs[0], group_005.inputs[0])
			#separate_geometry_5.Selection -> reroute_3.Input
			_mn_utils_style_ribbon_nucleic.links.new(separate_geometry_5.outputs[0], reroute_3.inputs[0])
			#group_003.Value -> mix.A
			_mn_utils_style_ribbon_nucleic.links.new(group_003.outputs[1], mix.inputs[4])
			#group_005.Value -> mix.B
			_mn_utils_style_ribbon_nucleic.links.new(group_005.outputs[1], mix.inputs[5])
			#mix.Result -> set_position_1.Position
			_mn_utils_style_ribbon_nucleic.links.new(mix.outputs[1], set_position_1.inputs[2])
			#instance_on_points_2.Instances -> join_geometry_001_1.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(instance_on_points_2.outputs[0], join_geometry_001_1.inputs[0])
			return _mn_utils_style_ribbon_nucleic

		_mn_utils_style_ribbon_nucleic = _mn_utils_style_ribbon_nucleic_node_group()

		#initialize _field_offset node group
		def _field_offset_node_group():
			_field_offset = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".field_offset")

			_field_offset.color_tag = 'NONE'
			_field_offset.description = ""

			
			#_field_offset interface
			#Socket Field
			field_socket = _field_offset.interface.new_socket(name = "Field", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			field_socket.subtype = 'NONE'
			field_socket.default_value = (0.0, 0.0, 0.0)
			field_socket.min_value = -3.4028234663852886e+38
			field_socket.max_value = 3.4028234663852886e+38
			field_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_5 = _field_offset.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			value_socket_5.attribute_domain = 'POINT'
			
			#Socket Field
			field_socket_1 = _field_offset.interface.new_socket(name = "Field", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			field_socket_1.subtype = 'NONE'
			field_socket_1.default_value = 0
			field_socket_1.min_value = -2147483648
			field_socket_1.max_value = 2147483647
			field_socket_1.attribute_domain = 'POINT'
			
			#Socket Field
			field_socket_2 = _field_offset.interface.new_socket(name = "Field", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			field_socket_2.subtype = 'NONE'
			field_socket_2.default_value = 0.0
			field_socket_2.min_value = -3.4028234663852886e+38
			field_socket_2.max_value = 3.4028234663852886e+38
			field_socket_2.attribute_domain = 'POINT'
			
			#Socket Field
			field_socket_3 = _field_offset.interface.new_socket(name = "Field", in_out='INPUT', socket_type = 'NodeSocketVector')
			field_socket_3.subtype = 'NONE'
			field_socket_3.default_value = (0.0, 0.0, 0.0)
			field_socket_3.min_value = -3.4028234663852886e+38
			field_socket_3.max_value = 3.4028234663852886e+38
			field_socket_3.attribute_domain = 'POINT'
			field_socket_3.hide_value = True
			
			#Socket Value
			value_socket_6 = _field_offset.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketBool')
			value_socket_6.attribute_domain = 'POINT'
			value_socket_6.hide_value = True
			
			#Socket Field
			field_socket_4 = _field_offset.interface.new_socket(name = "Field", in_out='INPUT', socket_type = 'NodeSocketInt')
			field_socket_4.subtype = 'NONE'
			field_socket_4.default_value = 0
			field_socket_4.min_value = -2147483648
			field_socket_4.max_value = 2147483647
			field_socket_4.attribute_domain = 'POINT'
			field_socket_4.hide_value = True
			
			#Socket Field
			field_socket_5 = _field_offset.interface.new_socket(name = "Field", in_out='INPUT', socket_type = 'NodeSocketFloat')
			field_socket_5.subtype = 'NONE'
			field_socket_5.default_value = 0.0
			field_socket_5.min_value = -3.4028234663852886e+38
			field_socket_5.max_value = 3.4028234663852886e+38
			field_socket_5.attribute_domain = 'POINT'
			field_socket_5.hide_value = True
			
			#Socket Offset
			offset_socket_1 = _field_offset.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket_1.subtype = 'NONE'
			offset_socket_1.default_value = 0
			offset_socket_1.min_value = -2147483648
			offset_socket_1.max_value = 2147483647
			offset_socket_1.attribute_domain = 'POINT'
			
			
			#initialize _field_offset nodes
			#node Group Output
			group_output_25 = _field_offset.nodes.new("NodeGroupOutput")
			group_output_25.name = "Group Output"
			group_output_25.is_active_output = True
			
			#node Math.001
			math_001_3 = _field_offset.nodes.new("ShaderNodeMath")
			math_001_3.name = "Math.001"
			math_001_3.operation = 'ADD'
			math_001_3.use_clamp = False
			
			#node Evaluate at Index
			evaluate_at_index_2 = _field_offset.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_2.name = "Evaluate at Index"
			evaluate_at_index_2.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_2.domain = 'POINT'
			
			#node Group Input
			group_input_25 = _field_offset.nodes.new("NodeGroupInput")
			group_input_25.name = "Group Input"
			
			#node Evaluate at Index.001
			evaluate_at_index_001_1 = _field_offset.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001_1.name = "Evaluate at Index.001"
			evaluate_at_index_001_1.data_type = 'BOOLEAN'
			evaluate_at_index_001_1.domain = 'POINT'
			
			#node Index
			index_3 = _field_offset.nodes.new("GeometryNodeInputIndex")
			index_3.name = "Index"
			
			#node Evaluate at Index.002
			evaluate_at_index_002 = _field_offset.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_002.name = "Evaluate at Index.002"
			evaluate_at_index_002.data_type = 'INT'
			evaluate_at_index_002.domain = 'POINT'
			
			#node Evaluate at Index.003
			evaluate_at_index_003 = _field_offset.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_003.name = "Evaluate at Index.003"
			evaluate_at_index_003.data_type = 'FLOAT'
			evaluate_at_index_003.domain = 'POINT'
			
			
			
			
			#Set locations
			group_output_25.location = (407.6440124511719, 0.0)
			math_001_3.location = (0.5235366821289062, 15.3753662109375)
			evaluate_at_index_2.location = (217.64404296875, 102.376708984375)
			group_input_25.location = (-417.64404296875, 0.0)
			evaluate_at_index_001_1.location = (220.0, -60.0)
			index_3.location = (-260.0, -40.0)
			evaluate_at_index_002.location = (220.0, -220.0)
			evaluate_at_index_003.location = (220.0, -380.0)
			
			#Set dimensions
			group_output_25.width, group_output_25.height = 140.0, 100.0
			math_001_3.width, math_001_3.height = 140.0, 100.0
			evaluate_at_index_2.width, evaluate_at_index_2.height = 140.0, 100.0
			group_input_25.width, group_input_25.height = 140.0, 100.0
			evaluate_at_index_001_1.width, evaluate_at_index_001_1.height = 140.0, 100.0
			index_3.width, index_3.height = 140.0, 100.0
			evaluate_at_index_002.width, evaluate_at_index_002.height = 140.0, 100.0
			evaluate_at_index_003.width, evaluate_at_index_003.height = 140.0, 100.0
			
			#initialize _field_offset links
			#index_3.Index -> math_001_3.Value
			_field_offset.links.new(index_3.outputs[0], math_001_3.inputs[0])
			#math_001_3.Value -> evaluate_at_index_2.Index
			_field_offset.links.new(math_001_3.outputs[0], evaluate_at_index_2.inputs[0])
			#group_input_25.Field -> evaluate_at_index_2.Value
			_field_offset.links.new(group_input_25.outputs[0], evaluate_at_index_2.inputs[1])
			#group_input_25.Offset -> math_001_3.Value
			_field_offset.links.new(group_input_25.outputs[4], math_001_3.inputs[1])
			#evaluate_at_index_2.Value -> group_output_25.Field
			_field_offset.links.new(evaluate_at_index_2.outputs[0], group_output_25.inputs[0])
			#math_001_3.Value -> evaluate_at_index_001_1.Index
			_field_offset.links.new(math_001_3.outputs[0], evaluate_at_index_001_1.inputs[0])
			#group_input_25.Value -> evaluate_at_index_001_1.Value
			_field_offset.links.new(group_input_25.outputs[1], evaluate_at_index_001_1.inputs[1])
			#evaluate_at_index_001_1.Value -> group_output_25.Value
			_field_offset.links.new(evaluate_at_index_001_1.outputs[0], group_output_25.inputs[1])
			#math_001_3.Value -> evaluate_at_index_002.Index
			_field_offset.links.new(math_001_3.outputs[0], evaluate_at_index_002.inputs[0])
			#group_input_25.Field -> evaluate_at_index_002.Value
			_field_offset.links.new(group_input_25.outputs[2], evaluate_at_index_002.inputs[1])
			#evaluate_at_index_002.Value -> group_output_25.Field
			_field_offset.links.new(evaluate_at_index_002.outputs[0], group_output_25.inputs[2])
			#math_001_3.Value -> evaluate_at_index_003.Index
			_field_offset.links.new(math_001_3.outputs[0], evaluate_at_index_003.inputs[0])
			#group_input_25.Field -> evaluate_at_index_003.Value
			_field_offset.links.new(group_input_25.outputs[3], evaluate_at_index_003.inputs[1])
			#evaluate_at_index_003.Value -> group_output_25.Field
			_field_offset.links.new(evaluate_at_index_003.outputs[0], group_output_25.inputs[3])
			return _field_offset

		_field_offset = _field_offset_node_group()

		#initialize _mn_select_sec_struct_id node group
		def _mn_select_sec_struct_id_node_group():
			_mn_select_sec_struct_id = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_select_sec_struct_id")

			_mn_select_sec_struct_id.color_tag = 'NONE'
			_mn_select_sec_struct_id.description = ""

			
			#_mn_select_sec_struct_id interface
			#Socket Selection
			selection_socket_9 = _mn_select_sec_struct_id.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket_9.attribute_domain = 'POINT'
			selection_socket_9.description = "The calculated selection"
			
			#Socket Inverted
			inverted_socket_2 = _mn_select_sec_struct_id.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket_2.attribute_domain = 'POINT'
			
			#Socket And
			and_socket_2 = _mn_select_sec_struct_id.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket_2.attribute_domain = 'POINT'
			and_socket_2.hide_value = True
			
			#Socket Or
			or_socket_2 = _mn_select_sec_struct_id.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket_2.attribute_domain = 'POINT'
			or_socket_2.hide_value = True
			
			#Socket id
			id_socket = _mn_select_sec_struct_id.interface.new_socket(name = "id", in_out='INPUT', socket_type = 'NodeSocketInt')
			id_socket.subtype = 'NONE'
			id_socket.default_value = 1
			id_socket.min_value = -2147483648
			id_socket.max_value = 2147483647
			id_socket.attribute_domain = 'POINT'
			id_socket.description = "Secondary structure component to select"
			
			
			#initialize _mn_select_sec_struct_id nodes
			#node Named Attribute.002
			named_attribute_002_4 = _mn_select_sec_struct_id.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002_4.name = "Named Attribute.002"
			named_attribute_002_4.data_type = 'INT'
			#Name
			named_attribute_002_4.inputs[0].default_value = "sec_struct"
			
			#node Boolean Math
			boolean_math_5 = _mn_select_sec_struct_id.nodes.new("FunctionNodeBooleanMath")
			boolean_math_5.name = "Boolean Math"
			boolean_math_5.operation = 'AND'
			
			#node Group Output
			group_output_26 = _mn_select_sec_struct_id.nodes.new("NodeGroupOutput")
			group_output_26.name = "Group Output"
			group_output_26.is_active_output = True
			
			#node Compare.012
			compare_012 = _mn_select_sec_struct_id.nodes.new("FunctionNodeCompare")
			compare_012.name = "Compare.012"
			compare_012.data_type = 'INT'
			compare_012.mode = 'ELEMENT'
			compare_012.operation = 'EQUAL'
			
			#node Group Input
			group_input_26 = _mn_select_sec_struct_id.nodes.new("NodeGroupInput")
			group_input_26.name = "Group Input"
			
			#node Boolean Math.001
			boolean_math_001_4 = _mn_select_sec_struct_id.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_4.name = "Boolean Math.001"
			boolean_math_001_4.operation = 'OR'
			
			#node Boolean Math.002
			boolean_math_002_4 = _mn_select_sec_struct_id.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_4.name = "Boolean Math.002"
			boolean_math_002_4.operation = 'NOT'
			
			
			
			
			#Set locations
			named_attribute_002_4.location = (80.0, 0.0)
			boolean_math_5.location = (400.0, 200.0)
			group_output_26.location = (760.0, 200.0)
			compare_012.location = (240.0, 100.0)
			group_input_26.location = (80.0, 100.0)
			boolean_math_001_4.location = (579.9999389648438, 196.54164123535156)
			boolean_math_002_4.location = (580.0, 60.0)
			
			#Set dimensions
			named_attribute_002_4.width, named_attribute_002_4.height = 140.0, 100.0
			boolean_math_5.width, boolean_math_5.height = 140.0, 100.0
			group_output_26.width, group_output_26.height = 140.0, 100.0
			compare_012.width, compare_012.height = 140.0, 100.0
			group_input_26.width, group_input_26.height = 140.0, 100.0
			boolean_math_001_4.width, boolean_math_001_4.height = 140.0, 100.0
			boolean_math_002_4.width, boolean_math_002_4.height = 140.0, 100.0
			
			#initialize _mn_select_sec_struct_id links
			#boolean_math_001_4.Boolean -> group_output_26.Selection
			_mn_select_sec_struct_id.links.new(boolean_math_001_4.outputs[0], group_output_26.inputs[0])
			#compare_012.Result -> boolean_math_5.Boolean
			_mn_select_sec_struct_id.links.new(compare_012.outputs[0], boolean_math_5.inputs[1])
			#group_input_26.id -> compare_012.A
			_mn_select_sec_struct_id.links.new(group_input_26.outputs[2], compare_012.inputs[2])
			#group_input_26.And -> boolean_math_5.Boolean
			_mn_select_sec_struct_id.links.new(group_input_26.outputs[0], boolean_math_5.inputs[0])
			#named_attribute_002_4.Attribute -> compare_012.B
			_mn_select_sec_struct_id.links.new(named_attribute_002_4.outputs[0], compare_012.inputs[3])
			#boolean_math_5.Boolean -> boolean_math_001_4.Boolean
			_mn_select_sec_struct_id.links.new(boolean_math_5.outputs[0], boolean_math_001_4.inputs[0])
			#group_input_26.Or -> boolean_math_001_4.Boolean
			_mn_select_sec_struct_id.links.new(group_input_26.outputs[1], boolean_math_001_4.inputs[1])
			#boolean_math_001_4.Boolean -> boolean_math_002_4.Boolean
			_mn_select_sec_struct_id.links.new(boolean_math_001_4.outputs[0], boolean_math_002_4.inputs[0])
			#boolean_math_002_4.Boolean -> group_output_26.Inverted
			_mn_select_sec_struct_id.links.new(boolean_math_002_4.outputs[0], group_output_26.inputs[1])
			return _mn_select_sec_struct_id

		_mn_select_sec_struct_id = _mn_select_sec_struct_id_node_group()

		#initialize is_sheet node group
		def is_sheet_node_group():
			is_sheet = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Is Sheet")

			is_sheet.color_tag = 'INPUT'
			is_sheet.description = ""

			
			#is_sheet interface
			#Socket Selection
			selection_socket_10 = is_sheet.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket_10.attribute_domain = 'POINT'
			selection_socket_10.description = "Selected atoms form part of a sheet"
			
			#Socket Inverted
			inverted_socket_3 = is_sheet.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket_3.attribute_domain = 'POINT'
			
			#Socket And
			and_socket_3 = is_sheet.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket_3.attribute_domain = 'POINT'
			and_socket_3.hide_value = True
			
			#Socket Or
			or_socket_3 = is_sheet.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket_3.attribute_domain = 'POINT'
			or_socket_3.hide_value = True
			
			
			#initialize is_sheet nodes
			#node Group Output
			group_output_27 = is_sheet.nodes.new("NodeGroupOutput")
			group_output_27.name = "Group Output"
			group_output_27.is_active_output = True
			
			#node Group Input
			group_input_27 = is_sheet.nodes.new("NodeGroupInput")
			group_input_27.name = "Group Input"
			
			#node MN_select_sec_struct.002
			mn_select_sec_struct_002 = is_sheet.nodes.new("GeometryNodeGroup")
			mn_select_sec_struct_002.label = "Select Sec Struct"
			mn_select_sec_struct_002.name = "MN_select_sec_struct.002"
			mn_select_sec_struct_002.node_tree = _mn_select_sec_struct_id
			#Socket_1
			mn_select_sec_struct_002.inputs[2].default_value = 2
			
			
			
			
			#Set locations
			group_output_27.location = (267.00146484375, 0.0)
			group_input_27.location = (-220.0, -80.0)
			mn_select_sec_struct_002.location = (0.0, 0.0)
			
			#Set dimensions
			group_output_27.width, group_output_27.height = 140.0, 100.0
			group_input_27.width, group_input_27.height = 140.0, 100.0
			mn_select_sec_struct_002.width, mn_select_sec_struct_002.height = 217.00146484375, 100.0
			
			#initialize is_sheet links
			#mn_select_sec_struct_002.Selection -> group_output_27.Selection
			is_sheet.links.new(mn_select_sec_struct_002.outputs[0], group_output_27.inputs[0])
			#group_input_27.And -> mn_select_sec_struct_002.And
			is_sheet.links.new(group_input_27.outputs[0], mn_select_sec_struct_002.inputs[0])
			#group_input_27.Or -> mn_select_sec_struct_002.Or
			is_sheet.links.new(group_input_27.outputs[1], mn_select_sec_struct_002.inputs[1])
			#mn_select_sec_struct_002.Inverted -> group_output_27.Inverted
			is_sheet.links.new(mn_select_sec_struct_002.outputs[1], group_output_27.inputs[1])
			return is_sheet

		is_sheet = is_sheet_node_group()

		#initialize is_loop node group
		def is_loop_node_group():
			is_loop = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Is Loop")

			is_loop.color_tag = 'INPUT'
			is_loop.description = ""

			
			#is_loop interface
			#Socket Selection
			selection_socket_11 = is_loop.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket_11.attribute_domain = 'POINT'
			selection_socket_11.description = "Selected atoms form part of a loop, and not part of any secondary structure"
			
			#Socket Inverted
			inverted_socket_4 = is_loop.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket_4.attribute_domain = 'POINT'
			
			#Socket And
			and_socket_4 = is_loop.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket_4.attribute_domain = 'POINT'
			and_socket_4.hide_value = True
			
			#Socket Or
			or_socket_4 = is_loop.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket_4.attribute_domain = 'POINT'
			or_socket_4.hide_value = True
			
			
			#initialize is_loop nodes
			#node Group Output
			group_output_28 = is_loop.nodes.new("NodeGroupOutput")
			group_output_28.name = "Group Output"
			group_output_28.is_active_output = True
			
			#node Group Input
			group_input_28 = is_loop.nodes.new("NodeGroupInput")
			group_input_28.name = "Group Input"
			
			#node MN_select_sec_struct.002
			mn_select_sec_struct_002_1 = is_loop.nodes.new("GeometryNodeGroup")
			mn_select_sec_struct_002_1.label = "Select Sec Struct"
			mn_select_sec_struct_002_1.name = "MN_select_sec_struct.002"
			mn_select_sec_struct_002_1.node_tree = _mn_select_sec_struct_id
			#Socket_1
			mn_select_sec_struct_002_1.inputs[2].default_value = 3
			
			
			
			
			#Set locations
			group_output_28.location = (267.00146484375, 0.0)
			group_input_28.location = (-200.0, 0.0)
			mn_select_sec_struct_002_1.location = (0.0, 0.0)
			
			#Set dimensions
			group_output_28.width, group_output_28.height = 140.0, 100.0
			group_input_28.width, group_input_28.height = 140.0, 100.0
			mn_select_sec_struct_002_1.width, mn_select_sec_struct_002_1.height = 217.00146484375, 100.0
			
			#initialize is_loop links
			#mn_select_sec_struct_002_1.Selection -> group_output_28.Selection
			is_loop.links.new(mn_select_sec_struct_002_1.outputs[0], group_output_28.inputs[0])
			#group_input_28.And -> mn_select_sec_struct_002_1.And
			is_loop.links.new(group_input_28.outputs[0], mn_select_sec_struct_002_1.inputs[0])
			#group_input_28.Or -> mn_select_sec_struct_002_1.Or
			is_loop.links.new(group_input_28.outputs[1], mn_select_sec_struct_002_1.inputs[1])
			#mn_select_sec_struct_002_1.Inverted -> group_output_28.Inverted
			is_loop.links.new(mn_select_sec_struct_002_1.outputs[1], group_output_28.inputs[1])
			return is_loop

		is_loop = is_loop_node_group()

		#initialize is_helix node group
		def is_helix_node_group():
			is_helix = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Is Helix")

			is_helix.color_tag = 'INPUT'
			is_helix.description = ""

			
			#is_helix interface
			#Socket Selection
			selection_socket_12 = is_helix.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket_12.attribute_domain = 'POINT'
			selection_socket_12.description = "Selected atoms form part of an helix"
			
			#Socket Inverted
			inverted_socket_5 = is_helix.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket_5.attribute_domain = 'POINT'
			
			#Socket And
			and_socket_5 = is_helix.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket_5.attribute_domain = 'POINT'
			and_socket_5.hide_value = True
			
			#Socket Or
			or_socket_5 = is_helix.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket_5.attribute_domain = 'POINT'
			or_socket_5.hide_value = True
			
			
			#initialize is_helix nodes
			#node Group Output
			group_output_29 = is_helix.nodes.new("NodeGroupOutput")
			group_output_29.name = "Group Output"
			group_output_29.is_active_output = True
			
			#node Group Input
			group_input_29 = is_helix.nodes.new("NodeGroupInput")
			group_input_29.name = "Group Input"
			
			#node MN_select_sec_struct.002
			mn_select_sec_struct_002_2 = is_helix.nodes.new("GeometryNodeGroup")
			mn_select_sec_struct_002_2.label = "Select Sec Struct"
			mn_select_sec_struct_002_2.name = "MN_select_sec_struct.002"
			mn_select_sec_struct_002_2.node_tree = _mn_select_sec_struct_id
			#Socket_1
			mn_select_sec_struct_002_2.inputs[2].default_value = 1
			
			
			
			
			#Set locations
			group_output_29.location = (267.00146484375, 0.0)
			group_input_29.location = (-200.0, 0.0)
			mn_select_sec_struct_002_2.location = (0.0, 0.0)
			
			#Set dimensions
			group_output_29.width, group_output_29.height = 140.0, 100.0
			group_input_29.width, group_input_29.height = 140.0, 100.0
			mn_select_sec_struct_002_2.width, mn_select_sec_struct_002_2.height = 217.00146484375, 100.0
			
			#initialize is_helix links
			#mn_select_sec_struct_002_2.Selection -> group_output_29.Selection
			is_helix.links.new(mn_select_sec_struct_002_2.outputs[0], group_output_29.inputs[0])
			#group_input_29.And -> mn_select_sec_struct_002_2.And
			is_helix.links.new(group_input_29.outputs[0], mn_select_sec_struct_002_2.inputs[0])
			#group_input_29.Or -> mn_select_sec_struct_002_2.Or
			is_helix.links.new(group_input_29.outputs[1], mn_select_sec_struct_002_2.inputs[1])
			#mn_select_sec_struct_002_2.Inverted -> group_output_29.Inverted
			is_helix.links.new(mn_select_sec_struct_002_2.outputs[1], group_output_29.inputs[1])
			return is_helix

		is_helix = is_helix_node_group()

		#initialize _mn_select_sec_struct node group
		def _mn_select_sec_struct_node_group():
			_mn_select_sec_struct = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_select_sec_struct")

			_mn_select_sec_struct.color_tag = 'NONE'
			_mn_select_sec_struct.description = ""

			
			#_mn_select_sec_struct interface
			#Socket Is Helix
			is_helix_socket = _mn_select_sec_struct.interface.new_socket(name = "Is Helix", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_helix_socket.attribute_domain = 'POINT'
			
			#Socket Is Sheet
			is_sheet_socket = _mn_select_sec_struct.interface.new_socket(name = "Is Sheet", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_sheet_socket.attribute_domain = 'POINT'
			
			#Socket Is Structured
			is_structured_socket = _mn_select_sec_struct.interface.new_socket(name = "Is Structured", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_structured_socket.attribute_domain = 'POINT'
			
			#Socket Is Loop
			is_loop_socket = _mn_select_sec_struct.interface.new_socket(name = "Is Loop", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_loop_socket.attribute_domain = 'POINT'
			
			#Socket And
			and_socket_6 = _mn_select_sec_struct.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket_6.attribute_domain = 'POINT'
			and_socket_6.hide_value = True
			
			
			#initialize _mn_select_sec_struct nodes
			#node Group.001
			group_001_4 = _mn_select_sec_struct.nodes.new("GeometryNodeGroup")
			group_001_4.name = "Group.001"
			group_001_4.node_tree = is_sheet
			#Socket_3
			group_001_4.inputs[1].default_value = False
			
			#node Group.002
			group_002_1 = _mn_select_sec_struct.nodes.new("GeometryNodeGroup")
			group_002_1.name = "Group.002"
			group_002_1.node_tree = is_loop
			#Socket_3
			group_002_1.inputs[1].default_value = False
			
			#node Group
			group_12 = _mn_select_sec_struct.nodes.new("GeometryNodeGroup")
			group_12.name = "Group"
			group_12.node_tree = is_helix
			#Socket_3
			group_12.inputs[1].default_value = False
			
			#node Boolean Math.001
			boolean_math_001_5 = _mn_select_sec_struct.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_5.name = "Boolean Math.001"
			boolean_math_001_5.hide = True
			boolean_math_001_5.operation = 'NOT'
			
			#node Group Output
			group_output_30 = _mn_select_sec_struct.nodes.new("NodeGroupOutput")
			group_output_30.name = "Group Output"
			group_output_30.is_active_output = True
			
			#node Group Input
			group_input_30 = _mn_select_sec_struct.nodes.new("NodeGroupInput")
			group_input_30.name = "Group Input"
			group_input_30.outputs[1].hide = True
			
			
			
			
			#Set locations
			group_001_4.location = (120.0, -60.0)
			group_002_1.location = (120.0, -180.0)
			group_12.location = (120.0, 60.0)
			boolean_math_001_5.location = (300.0, -140.0)
			group_output_30.location = (540.0, -60.0)
			group_input_30.location = (-160.0, -40.0)
			
			#Set dimensions
			group_001_4.width, group_001_4.height = 140.0, 100.0
			group_002_1.width, group_002_1.height = 140.0, 100.0
			group_12.width, group_12.height = 140.0, 100.0
			boolean_math_001_5.width, boolean_math_001_5.height = 140.0, 100.0
			group_output_30.width, group_output_30.height = 140.0, 100.0
			group_input_30.width, group_input_30.height = 140.0, 100.0
			
			#initialize _mn_select_sec_struct links
			#group_002_1.Selection -> group_output_30.Is Loop
			_mn_select_sec_struct.links.new(group_002_1.outputs[0], group_output_30.inputs[3])
			#group_002_1.Selection -> boolean_math_001_5.Boolean
			_mn_select_sec_struct.links.new(group_002_1.outputs[0], boolean_math_001_5.inputs[0])
			#boolean_math_001_5.Boolean -> group_output_30.Is Structured
			_mn_select_sec_struct.links.new(boolean_math_001_5.outputs[0], group_output_30.inputs[2])
			#group_12.Selection -> group_output_30.Is Helix
			_mn_select_sec_struct.links.new(group_12.outputs[0], group_output_30.inputs[0])
			#group_001_4.Selection -> group_output_30.Is Sheet
			_mn_select_sec_struct.links.new(group_001_4.outputs[0], group_output_30.inputs[1])
			#group_input_30.And -> group_12.And
			_mn_select_sec_struct.links.new(group_input_30.outputs[0], group_12.inputs[0])
			#group_input_30.And -> group_001_4.And
			_mn_select_sec_struct.links.new(group_input_30.outputs[0], group_001_4.inputs[0])
			#group_input_30.And -> group_002_1.And
			_mn_select_sec_struct.links.new(group_input_30.outputs[0], group_002_1.inputs[0])
			return _mn_select_sec_struct

		_mn_select_sec_struct = _mn_select_sec_struct_node_group()

		#initialize _field_offset_vec node group
		def _field_offset_vec_node_group():
			_field_offset_vec = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".field_offset_vec")

			_field_offset_vec.color_tag = 'NONE'
			_field_offset_vec.description = ""

			
			#_field_offset_vec interface
			#Socket Field
			field_socket_6 = _field_offset_vec.interface.new_socket(name = "Field", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			field_socket_6.subtype = 'NONE'
			field_socket_6.default_value = (0.0, 0.0, 0.0)
			field_socket_6.min_value = -3.4028234663852886e+38
			field_socket_6.max_value = 3.4028234663852886e+38
			field_socket_6.attribute_domain = 'POINT'
			
			#Socket Field
			field_socket_7 = _field_offset_vec.interface.new_socket(name = "Field", in_out='INPUT', socket_type = 'NodeSocketVector')
			field_socket_7.subtype = 'NONE'
			field_socket_7.default_value = (0.0, 0.0, 0.0)
			field_socket_7.min_value = -3.4028234663852886e+38
			field_socket_7.max_value = 3.4028234663852886e+38
			field_socket_7.attribute_domain = 'POINT'
			field_socket_7.hide_value = True
			
			#Socket Offset
			offset_socket_2 = _field_offset_vec.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket_2.subtype = 'NONE'
			offset_socket_2.default_value = 0
			offset_socket_2.min_value = -2147483648
			offset_socket_2.max_value = 2147483647
			offset_socket_2.attribute_domain = 'POINT'
			
			
			#initialize _field_offset_vec nodes
			#node Group Input
			group_input_31 = _field_offset_vec.nodes.new("NodeGroupInput")
			group_input_31.name = "Group Input"
			
			#node Evaluate at Index
			evaluate_at_index_3 = _field_offset_vec.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_3.name = "Evaluate at Index"
			evaluate_at_index_3.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_3.domain = 'POINT'
			
			#node Group Output
			group_output_31 = _field_offset_vec.nodes.new("NodeGroupOutput")
			group_output_31.name = "Group Output"
			group_output_31.is_active_output = True
			
			#node Math.001
			math_001_4 = _field_offset_vec.nodes.new("ShaderNodeMath")
			math_001_4.name = "Math.001"
			math_001_4.operation = 'ADD'
			math_001_4.use_clamp = False
			
			#node Index
			index_4 = _field_offset_vec.nodes.new("GeometryNodeInputIndex")
			index_4.name = "Index"
			
			
			
			
			#Set locations
			group_input_31.location = (-417.64404296875, 0.0)
			evaluate_at_index_3.location = (-220.0, 100.0)
			group_output_31.location = (20.0, 20.0)
			math_001_4.location = (-220.0, -80.0)
			index_4.location = (-400.0, -180.0)
			
			#Set dimensions
			group_input_31.width, group_input_31.height = 140.0, 100.0
			evaluate_at_index_3.width, evaluate_at_index_3.height = 140.0, 100.0
			group_output_31.width, group_output_31.height = 140.0, 100.0
			math_001_4.width, math_001_4.height = 140.0, 100.0
			index_4.width, index_4.height = 140.0, 100.0
			
			#initialize _field_offset_vec links
			#math_001_4.Value -> evaluate_at_index_3.Index
			_field_offset_vec.links.new(math_001_4.outputs[0], evaluate_at_index_3.inputs[0])
			#group_input_31.Field -> evaluate_at_index_3.Value
			_field_offset_vec.links.new(group_input_31.outputs[0], evaluate_at_index_3.inputs[1])
			#group_input_31.Offset -> math_001_4.Value
			_field_offset_vec.links.new(group_input_31.outputs[1], math_001_4.inputs[0])
			#evaluate_at_index_3.Value -> group_output_31.Field
			_field_offset_vec.links.new(evaluate_at_index_3.outputs[0], group_output_31.inputs[0])
			#index_4.Index -> math_001_4.Value
			_field_offset_vec.links.new(index_4.outputs[0], math_001_4.inputs[1])
			return _field_offset_vec

		_field_offset_vec = _field_offset_vec_node_group()

		#initialize _sec_struct_counter node group
		def _sec_struct_counter_node_group():
			_sec_struct_counter = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".sec_struct_counter")

			_sec_struct_counter.color_tag = 'NONE'
			_sec_struct_counter.description = ""

			
			#_sec_struct_counter interface
			#Socket Leading
			leading_socket = _sec_struct_counter.interface.new_socket(name = "Leading", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			leading_socket.subtype = 'NONE'
			leading_socket.default_value = 0
			leading_socket.min_value = -2147483648
			leading_socket.max_value = 2147483647
			leading_socket.attribute_domain = 'POINT'
			
			#Socket Trailing
			trailing_socket = _sec_struct_counter.interface.new_socket(name = "Trailing", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			trailing_socket.subtype = 'NONE'
			trailing_socket.default_value = 0
			trailing_socket.min_value = -2147483648
			trailing_socket.max_value = 2147483647
			trailing_socket.attribute_domain = 'POINT'
			
			#Socket Total
			total_socket = _sec_struct_counter.interface.new_socket(name = "Total", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			total_socket.subtype = 'NONE'
			total_socket.default_value = 0
			total_socket.min_value = -2147483648
			total_socket.max_value = 2147483647
			total_socket.attribute_domain = 'POINT'
			
			#Socket Border
			border_socket = _sec_struct_counter.interface.new_socket(name = "Border", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			border_socket.attribute_domain = 'POINT'
			
			
			#initialize _sec_struct_counter nodes
			#node Group Input
			group_input_32 = _sec_struct_counter.nodes.new("NodeGroupInput")
			group_input_32.name = "Group Input"
			
			#node Reroute.005
			reroute_005_2 = _sec_struct_counter.nodes.new("NodeReroute")
			reroute_005_2.name = "Reroute.005"
			#node Named Attribute.001
			named_attribute_001_2 = _sec_struct_counter.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001_2.name = "Named Attribute.001"
			named_attribute_001_2.data_type = 'INT'
			#Name
			named_attribute_001_2.inputs[0].default_value = "sec_struct"
			
			#node Group.004
			group_004_1 = _sec_struct_counter.nodes.new("GeometryNodeGroup")
			group_004_1.name = "Group.004"
			group_004_1.node_tree = _field_offset
			#Input_0
			group_004_1.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Input_3
			group_004_1.inputs[1].default_value = False
			#Input_7
			group_004_1.inputs[3].default_value = 0.0
			#Input_1
			group_004_1.inputs[4].default_value = -1
			
			#node Compare.009
			compare_009_1 = _sec_struct_counter.nodes.new("FunctionNodeCompare")
			compare_009_1.name = "Compare.009"
			compare_009_1.data_type = 'INT'
			compare_009_1.mode = 'ELEMENT'
			compare_009_1.operation = 'NOT_EQUAL'
			
			#node Accumulate Field.004
			accumulate_field_004 = _sec_struct_counter.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_004.name = "Accumulate Field.004"
			accumulate_field_004.data_type = 'INT'
			accumulate_field_004.domain = 'POINT'
			#Group Index
			accumulate_field_004.inputs[1].default_value = 0
			
			#node Compare.010
			compare_010_1 = _sec_struct_counter.nodes.new("FunctionNodeCompare")
			compare_010_1.name = "Compare.010"
			compare_010_1.data_type = 'INT'
			compare_010_1.mode = 'ELEMENT'
			compare_010_1.operation = 'NOT_EQUAL'
			
			#node Reroute
			reroute_4 = _sec_struct_counter.nodes.new("NodeReroute")
			reroute_4.name = "Reroute"
			#node Boolean Math
			boolean_math_6 = _sec_struct_counter.nodes.new("FunctionNodeBooleanMath")
			boolean_math_6.name = "Boolean Math"
			boolean_math_6.operation = 'OR'
			#Boolean_001
			boolean_math_6.inputs[1].default_value = False
			
			#node Group Output
			group_output_32 = _sec_struct_counter.nodes.new("NodeGroupOutput")
			group_output_32.name = "Group Output"
			group_output_32.is_active_output = True
			
			#node Group.003
			group_003_1 = _sec_struct_counter.nodes.new("GeometryNodeGroup")
			group_003_1.name = "Group.003"
			group_003_1.node_tree = _field_offset
			#Input_0
			group_003_1.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Input_3
			group_003_1.inputs[1].default_value = False
			#Input_7
			group_003_1.inputs[3].default_value = 0.0
			#Input_1
			group_003_1.inputs[4].default_value = 1
			
			
			
			
			#Set locations
			group_input_32.location = (-500.1279296875, 0.0)
			reroute_005_2.location = (-119.8720703125, -60.0)
			named_attribute_001_2.location = (-300.0, 120.0)
			group_004_1.location = (-20.0, -220.0)
			compare_009_1.location = (140.1279296875, 60.0)
			accumulate_field_004.location = (460.0, 40.0)
			compare_010_1.location = (140.0, -140.0)
			reroute_4.location = (320.0, -60.0)
			boolean_math_6.location = (300.0, -140.0)
			group_output_32.location = (796.4706420898438, 27.943008422851562)
			group_003_1.location = (-19.8720703125, 60.0)
			
			#Set dimensions
			group_input_32.width, group_input_32.height = 140.0, 100.0
			reroute_005_2.width, reroute_005_2.height = 16.0, 100.0
			named_attribute_001_2.width, named_attribute_001_2.height = 140.0, 100.0
			group_004_1.width, group_004_1.height = 140.0, 100.0
			compare_009_1.width, compare_009_1.height = 140.0, 100.0
			accumulate_field_004.width, accumulate_field_004.height = 140.0, 100.0
			compare_010_1.width, compare_010_1.height = 140.0, 100.0
			reroute_4.width, reroute_4.height = 16.0, 100.0
			boolean_math_6.width, boolean_math_6.height = 140.0, 100.0
			group_output_32.width, group_output_32.height = 140.0, 100.0
			group_003_1.width, group_003_1.height = 140.0, 100.0
			
			#initialize _sec_struct_counter links
			#reroute_4.Output -> accumulate_field_004.Value
			_sec_struct_counter.links.new(reroute_4.outputs[0], accumulate_field_004.inputs[0])
			#reroute_005_2.Output -> group_003_1.Field
			_sec_struct_counter.links.new(reroute_005_2.outputs[0], group_003_1.inputs[2])
			#reroute_005_2.Output -> compare_009_1.A
			_sec_struct_counter.links.new(reroute_005_2.outputs[0], compare_009_1.inputs[2])
			#named_attribute_001_2.Attribute -> reroute_005_2.Input
			_sec_struct_counter.links.new(named_attribute_001_2.outputs[0], reroute_005_2.inputs[0])
			#group_003_1.Field -> compare_009_1.B
			_sec_struct_counter.links.new(group_003_1.outputs[2], compare_009_1.inputs[3])
			#accumulate_field_004.Trailing -> group_output_32.Trailing
			_sec_struct_counter.links.new(accumulate_field_004.outputs[1], group_output_32.inputs[1])
			#accumulate_field_004.Leading -> group_output_32.Leading
			_sec_struct_counter.links.new(accumulate_field_004.outputs[0], group_output_32.inputs[0])
			#accumulate_field_004.Total -> group_output_32.Total
			_sec_struct_counter.links.new(accumulate_field_004.outputs[2], group_output_32.inputs[2])
			#reroute_4.Output -> group_output_32.Border
			_sec_struct_counter.links.new(reroute_4.outputs[0], group_output_32.inputs[3])
			#reroute_005_2.Output -> group_004_1.Field
			_sec_struct_counter.links.new(reroute_005_2.outputs[0], group_004_1.inputs[2])
			#reroute_005_2.Output -> compare_010_1.A
			_sec_struct_counter.links.new(reroute_005_2.outputs[0], compare_010_1.inputs[2])
			#group_004_1.Field -> compare_010_1.B
			_sec_struct_counter.links.new(group_004_1.outputs[2], compare_010_1.inputs[3])
			#compare_009_1.Result -> reroute_4.Input
			_sec_struct_counter.links.new(compare_009_1.outputs[0], reroute_4.inputs[0])
			#compare_010_1.Result -> boolean_math_6.Boolean
			_sec_struct_counter.links.new(compare_010_1.outputs[0], boolean_math_6.inputs[0])
			return _sec_struct_counter

		_sec_struct_counter = _sec_struct_counter_node_group()

		#initialize _bs_smooth node group
		def _bs_smooth_node_group():
			_bs_smooth = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".bs_smooth")

			_bs_smooth.color_tag = 'NONE'
			_bs_smooth.description = ""

			_bs_smooth.is_modifier = True
			
			#_bs_smooth interface
			#Socket Geometry
			geometry_socket_4 = _bs_smooth.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_4.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_5 = _bs_smooth.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_5.attribute_domain = 'POINT'
			
			#Socket Factor
			factor_socket = _bs_smooth.interface.new_socket(name = "Factor", in_out='INPUT', socket_type = 'NodeSocketFloat')
			factor_socket.subtype = 'FACTOR'
			factor_socket.default_value = 1.0
			factor_socket.min_value = 0.0
			factor_socket.max_value = 1.0
			factor_socket.attribute_domain = 'POINT'
			
			#Socket Iterations
			iterations_socket = _bs_smooth.interface.new_socket(name = "Iterations", in_out='INPUT', socket_type = 'NodeSocketInt')
			iterations_socket.subtype = 'NONE'
			iterations_socket.default_value = 2
			iterations_socket.min_value = 0
			iterations_socket.max_value = 2147483647
			iterations_socket.attribute_domain = 'POINT'
			
			
			#initialize _bs_smooth nodes
			#node Group Output
			group_output_33 = _bs_smooth.nodes.new("NodeGroupOutput")
			group_output_33.name = "Group Output"
			group_output_33.is_active_output = True
			
			#node Set Position
			set_position_2 = _bs_smooth.nodes.new("GeometryNodeSetPosition")
			set_position_2.name = "Set Position"
			#Offset
			set_position_2.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Mix.002
			mix_002 = _bs_smooth.nodes.new("ShaderNodeMix")
			mix_002.name = "Mix.002"
			mix_002.blend_type = 'MIX'
			mix_002.clamp_factor = True
			mix_002.clamp_result = False
			mix_002.data_type = 'VECTOR'
			mix_002.factor_mode = 'UNIFORM'
			
			#node Position.001
			position_001_2 = _bs_smooth.nodes.new("GeometryNodeInputPosition")
			position_001_2.name = "Position.001"
			
			#node Blur Attribute
			blur_attribute = _bs_smooth.nodes.new("GeometryNodeBlurAttribute")
			blur_attribute.name = "Blur Attribute"
			blur_attribute.data_type = 'FLOAT_VECTOR'
			
			#node Group Input
			group_input_33 = _bs_smooth.nodes.new("NodeGroupInput")
			group_input_33.name = "Group Input"
			
			#node Boolean Math.004
			boolean_math_004 = _bs_smooth.nodes.new("FunctionNodeBooleanMath")
			boolean_math_004.name = "Boolean Math.004"
			boolean_math_004.operation = 'NOT'
			
			#node Boolean Math.002
			boolean_math_002_5 = _bs_smooth.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_5.name = "Boolean Math.002"
			boolean_math_002_5.operation = 'AND'
			
			#node Group
			group_13 = _bs_smooth.nodes.new("GeometryNodeGroup")
			group_13.name = "Group"
			group_13.node_tree = _sec_struct_counter
			
			#node Endpoint Selection.004
			endpoint_selection_004 = _bs_smooth.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_004.name = "Endpoint Selection.004"
			#Start Size
			endpoint_selection_004.inputs[0].default_value = 1
			#End Size
			endpoint_selection_004.inputs[1].default_value = 1
			
			#node Boolean Math
			boolean_math_7 = _bs_smooth.nodes.new("FunctionNodeBooleanMath")
			boolean_math_7.name = "Boolean Math"
			boolean_math_7.operation = 'NOT'
			
			#node Group.021
			group_021 = _bs_smooth.nodes.new("GeometryNodeGroup")
			group_021.name = "Group.021"
			group_021.node_tree = _mn_select_sec_struct
			group_021.outputs[0].hide = True
			group_021.outputs[2].hide = True
			group_021.outputs[3].hide = True
			#Socket_1
			group_021.inputs[0].default_value = True
			
			
			
			
			#Set locations
			group_output_33.location = (591.18408203125, 0.0)
			set_position_2.location = (401.18408203125, 199.23532104492188)
			mix_002.location = (218.81591796875, 80.76467895507812)
			position_001_2.location = (-61.18408203125, -39.235321044921875)
			blur_attribute.location = (-58.81591796875, -120.76467895507812)
			group_input_33.location = (-615.6842041015625, 115.17381286621094)
			boolean_math_004.location = (-380.0, -160.0)
			boolean_math_002_5.location = (39.807212829589844, 161.80430603027344)
			group_13.location = (-620.0, -40.0)
			endpoint_selection_004.location = (-620.0, -280.0)
			boolean_math_7.location = (-120.0, 140.0)
			group_021.location = (40.0, 260.0)
			
			#Set dimensions
			group_output_33.width, group_output_33.height = 140.0, 100.0
			set_position_2.width, set_position_2.height = 140.0, 100.0
			mix_002.width, mix_002.height = 140.0, 100.0
			position_001_2.width, position_001_2.height = 140.0, 100.0
			blur_attribute.width, blur_attribute.height = 140.0, 100.0
			group_input_33.width, group_input_33.height = 140.0, 100.0
			boolean_math_004.width, boolean_math_004.height = 140.0, 100.0
			boolean_math_002_5.width, boolean_math_002_5.height = 140.0, 100.0
			group_13.width, group_13.height = 140.0, 100.0
			endpoint_selection_004.width, endpoint_selection_004.height = 140.0, 100.0
			boolean_math_7.width, boolean_math_7.height = 140.0, 100.0
			group_021.width, group_021.height = 140.0, 100.0
			
			#initialize _bs_smooth links
			#boolean_math_004.Boolean -> blur_attribute.Weight
			_bs_smooth.links.new(boolean_math_004.outputs[0], blur_attribute.inputs[2])
			#blur_attribute.Value -> mix_002.B
			_bs_smooth.links.new(blur_attribute.outputs[0], mix_002.inputs[5])
			#position_001_2.Position -> blur_attribute.Value
			_bs_smooth.links.new(position_001_2.outputs[0], blur_attribute.inputs[0])
			#mix_002.Result -> set_position_2.Position
			_bs_smooth.links.new(mix_002.outputs[1], set_position_2.inputs[2])
			#position_001_2.Position -> mix_002.A
			_bs_smooth.links.new(position_001_2.outputs[0], mix_002.inputs[4])
			#group_021.Is Sheet -> boolean_math_002_5.Boolean
			_bs_smooth.links.new(group_021.outputs[1], boolean_math_002_5.inputs[0])
			#group_input_33.Geometry -> set_position_2.Geometry
			_bs_smooth.links.new(group_input_33.outputs[0], set_position_2.inputs[0])
			#group_input_33.Factor -> mix_002.Factor
			_bs_smooth.links.new(group_input_33.outputs[1], mix_002.inputs[0])
			#set_position_2.Geometry -> group_output_33.Geometry
			_bs_smooth.links.new(set_position_2.outputs[0], group_output_33.inputs[0])
			#group_input_33.Iterations -> blur_attribute.Iterations
			_bs_smooth.links.new(group_input_33.outputs[2], blur_attribute.inputs[1])
			#group_13.Border -> boolean_math_7.Boolean
			_bs_smooth.links.new(group_13.outputs[3], boolean_math_7.inputs[0])
			#boolean_math_002_5.Boolean -> set_position_2.Selection
			_bs_smooth.links.new(boolean_math_002_5.outputs[0], set_position_2.inputs[1])
			#boolean_math_7.Boolean -> boolean_math_002_5.Boolean
			_bs_smooth.links.new(boolean_math_7.outputs[0], boolean_math_002_5.inputs[1])
			#group_13.Border -> boolean_math_004.Boolean
			_bs_smooth.links.new(group_13.outputs[3], boolean_math_004.inputs[0])
			return _bs_smooth

		_bs_smooth = _bs_smooth_node_group()

		#initialize _expand_selection node group
		def _expand_selection_node_group():
			_expand_selection = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".expand_selection")

			_expand_selection.color_tag = 'NONE'
			_expand_selection.description = ""

			
			#_expand_selection interface
			#Socket Boolean
			boolean_socket_1 = _expand_selection.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket_1.attribute_domain = 'POINT'
			
			#Socket Input
			input_socket_1 = _expand_selection.interface.new_socket(name = "Input", in_out='INPUT', socket_type = 'NodeSocketBool')
			input_socket_1.attribute_domain = 'POINT'
			
			#Socket Offset
			offset_socket_3 = _expand_selection.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket_3.subtype = 'NONE'
			offset_socket_3.default_value = 1
			offset_socket_3.min_value = -2147483648
			offset_socket_3.max_value = 2147483647
			offset_socket_3.attribute_domain = 'POINT'
			
			
			#initialize _expand_selection nodes
			#node Group Output
			group_output_34 = _expand_selection.nodes.new("NodeGroupOutput")
			group_output_34.name = "Group Output"
			group_output_34.is_active_output = True
			
			#node Boolean Math
			boolean_math_8 = _expand_selection.nodes.new("FunctionNodeBooleanMath")
			boolean_math_8.name = "Boolean Math"
			boolean_math_8.operation = 'OR'
			
			#node Boolean Math.001
			boolean_math_001_6 = _expand_selection.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_6.name = "Boolean Math.001"
			boolean_math_001_6.operation = 'OR'
			
			#node Group.025
			group_025 = _expand_selection.nodes.new("GeometryNodeGroup")
			group_025.name = "Group.025"
			group_025.node_tree = _field_offset
			#Input_0
			group_025.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Input_5
			group_025.inputs[2].default_value = 0
			#Input_7
			group_025.inputs[3].default_value = 0.0
			
			#node Group Input
			group_input_34 = _expand_selection.nodes.new("NodeGroupInput")
			group_input_34.name = "Group Input"
			
			#node Math
			math_8 = _expand_selection.nodes.new("ShaderNodeMath")
			math_8.name = "Math"
			math_8.operation = 'MULTIPLY'
			math_8.use_clamp = False
			#Value_001
			math_8.inputs[1].default_value = -1.0
			
			#node Group.024
			group_024 = _expand_selection.nodes.new("GeometryNodeGroup")
			group_024.name = "Group.024"
			group_024.node_tree = _field_offset
			#Input_0
			group_024.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Input_5
			group_024.inputs[2].default_value = 0
			#Input_7
			group_024.inputs[3].default_value = 0.0
			
			
			
			
			#Set locations
			group_output_34.location = (420.0, 0.0)
			boolean_math_8.location = (-50.0, 0.0)
			boolean_math_001_6.location = (230.0, 60.0)
			group_025.location = (-230.0, -140.0)
			group_input_34.location = (-637.21630859375, 234.8535614013672)
			math_8.location = (-640.0, 120.0)
			group_024.location = (-230.0, 140.0)
			
			#Set dimensions
			group_output_34.width, group_output_34.height = 140.0, 100.0
			boolean_math_8.width, boolean_math_8.height = 140.0, 100.0
			boolean_math_001_6.width, boolean_math_001_6.height = 140.0, 100.0
			group_025.width, group_025.height = 140.0, 100.0
			group_input_34.width, group_input_34.height = 140.0, 100.0
			math_8.width, math_8.height = 140.0, 100.0
			group_024.width, group_024.height = 140.0, 100.0
			
			#initialize _expand_selection links
			#group_025.Value -> boolean_math_8.Boolean
			_expand_selection.links.new(group_025.outputs[1], boolean_math_8.inputs[1])
			#group_input_34.Input -> group_025.Value
			_expand_selection.links.new(group_input_34.outputs[0], group_025.inputs[1])
			#group_input_34.Input -> group_024.Value
			_expand_selection.links.new(group_input_34.outputs[0], group_024.inputs[1])
			#group_024.Value -> boolean_math_8.Boolean
			_expand_selection.links.new(group_024.outputs[1], boolean_math_8.inputs[0])
			#boolean_math_8.Boolean -> boolean_math_001_6.Boolean
			_expand_selection.links.new(boolean_math_8.outputs[0], boolean_math_001_6.inputs[1])
			#group_input_34.Input -> boolean_math_001_6.Boolean
			_expand_selection.links.new(group_input_34.outputs[0], boolean_math_001_6.inputs[0])
			#boolean_math_001_6.Boolean -> group_output_34.Boolean
			_expand_selection.links.new(boolean_math_001_6.outputs[0], group_output_34.inputs[0])
			#group_input_34.Offset -> group_024.Offset
			_expand_selection.links.new(group_input_34.outputs[1], group_024.inputs[4])
			#group_input_34.Offset -> math_8.Value
			_expand_selection.links.new(group_input_34.outputs[1], math_8.inputs[0])
			#math_8.Value -> group_025.Offset
			_expand_selection.links.new(math_8.outputs[0], group_025.inputs[4])
			return _expand_selection

		_expand_selection = _expand_selection_node_group()

		#initialize is_alpha_carbon node group
		def is_alpha_carbon_node_group():
			is_alpha_carbon = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Is Alpha Carbon")

			is_alpha_carbon.color_tag = 'INPUT'
			is_alpha_carbon.description = ""

			
			#is_alpha_carbon interface
			#Socket Selection
			selection_socket_13 = is_alpha_carbon.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket_13.attribute_domain = 'POINT'
			selection_socket_13.description = "True if atom is an alpha carbon of an amino acid"
			
			#Socket Inverted
			inverted_socket_6 = is_alpha_carbon.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket_6.attribute_domain = 'POINT'
			
			#Socket And
			and_socket_7 = is_alpha_carbon.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket_7.attribute_domain = 'POINT'
			and_socket_7.hide_value = True
			
			#Socket Or
			or_socket_6 = is_alpha_carbon.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket_6.attribute_domain = 'POINT'
			or_socket_6.hide_value = True
			
			
			#initialize is_alpha_carbon nodes
			#node Group Output
			group_output_35 = is_alpha_carbon.nodes.new("NodeGroupOutput")
			group_output_35.name = "Group Output"
			group_output_35.is_active_output = True
			
			#node Group Input
			group_input_35 = is_alpha_carbon.nodes.new("NodeGroupInput")
			group_input_35.name = "Group Input"
			
			#node Boolean Math.001
			boolean_math_001_7 = is_alpha_carbon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_7.name = "Boolean Math.001"
			boolean_math_001_7.operation = 'AND'
			
			#node Group.001
			group_001_5 = is_alpha_carbon.nodes.new("GeometryNodeGroup")
			group_001_5.name = "Group.001"
			group_001_5.node_tree = fallback_boolean
			#Socket_2
			group_001_5.inputs[0].default_value = "is_alpha_carbon"
			
			#node Group.002
			group_002_2 = is_alpha_carbon.nodes.new("GeometryNodeGroup")
			group_002_2.name = "Group.002"
			group_002_2.node_tree = _mn_select_peptide
			group_002_2.outputs[0].hide = True
			group_002_2.outputs[1].hide = True
			group_002_2.outputs[2].hide = True
			
			#node Boolean Math.002
			boolean_math_002_6 = is_alpha_carbon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_6.name = "Boolean Math.002"
			boolean_math_002_6.operation = 'OR'
			
			#node Boolean Math
			boolean_math_9 = is_alpha_carbon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_9.name = "Boolean Math"
			boolean_math_9.operation = 'NOT'
			
			
			
			
			#Set locations
			group_output_35.location = (520.0, 0.0)
			group_input_35.location = (-200.0, 0.0)
			boolean_math_001_7.location = (160.0, 0.0)
			group_001_5.location = (-88.33343505859375, -180.0)
			group_002_2.location = (-290.4490661621094, -180.0)
			boolean_math_002_6.location = (340.0, 0.0)
			boolean_math_9.location = (340.0, -140.0)
			
			#Set dimensions
			group_output_35.width, group_output_35.height = 140.0, 100.0
			group_input_35.width, group_input_35.height = 140.0, 100.0
			boolean_math_001_7.width, boolean_math_001_7.height = 140.0, 100.0
			group_001_5.width, group_001_5.height = 208.33343505859375, 100.0
			group_002_2.width, group_002_2.height = 170.44906616210938, 100.0
			boolean_math_002_6.width, boolean_math_002_6.height = 140.0, 100.0
			boolean_math_9.width, boolean_math_9.height = 140.0, 100.0
			
			#initialize is_alpha_carbon links
			#group_input_35.And -> boolean_math_001_7.Boolean
			is_alpha_carbon.links.new(group_input_35.outputs[0], boolean_math_001_7.inputs[0])
			#boolean_math_002_6.Boolean -> group_output_35.Selection
			is_alpha_carbon.links.new(boolean_math_002_6.outputs[0], group_output_35.inputs[0])
			#group_001_5.Boolean -> boolean_math_001_7.Boolean
			is_alpha_carbon.links.new(group_001_5.outputs[0], boolean_math_001_7.inputs[1])
			#group_002_2.Is Alpha Carbon -> group_001_5.Fallback
			is_alpha_carbon.links.new(group_002_2.outputs[3], group_001_5.inputs[1])
			#boolean_math_001_7.Boolean -> boolean_math_002_6.Boolean
			is_alpha_carbon.links.new(boolean_math_001_7.outputs[0], boolean_math_002_6.inputs[0])
			#group_input_35.Or -> boolean_math_002_6.Boolean
			is_alpha_carbon.links.new(group_input_35.outputs[1], boolean_math_002_6.inputs[1])
			#boolean_math_002_6.Boolean -> boolean_math_9.Boolean
			is_alpha_carbon.links.new(boolean_math_002_6.outputs[0], boolean_math_9.inputs[0])
			#boolean_math_9.Boolean -> group_output_35.Inverted
			is_alpha_carbon.links.new(boolean_math_9.outputs[0], group_output_35.inputs[1])
			return is_alpha_carbon

		is_alpha_carbon = is_alpha_carbon_node_group()

		#initialize _mn_topo_assign_backbone node group
		def _mn_topo_assign_backbone_node_group():
			_mn_topo_assign_backbone = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_topo_assign_backbone")

			_mn_topo_assign_backbone.color_tag = 'NONE'
			_mn_topo_assign_backbone.description = ""

			
			#_mn_topo_assign_backbone interface
			#Socket Atoms
			atoms_socket_10 = _mn_topo_assign_backbone.interface.new_socket(name = "Atoms", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_10.attribute_domain = 'POINT'
			
			#Socket Unique Group ID
			unique_group_id_socket_1 = _mn_topo_assign_backbone.interface.new_socket(name = "Unique Group ID", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			unique_group_id_socket_1.subtype = 'NONE'
			unique_group_id_socket_1.default_value = 0
			unique_group_id_socket_1.min_value = -2147483648
			unique_group_id_socket_1.max_value = 2147483647
			unique_group_id_socket_1.attribute_domain = 'POINT'
			
			#Socket CA Atoms
			ca_atoms_socket = _mn_topo_assign_backbone.interface.new_socket(name = "CA Atoms", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			ca_atoms_socket.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket_11 = _mn_topo_assign_backbone.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_11.attribute_domain = 'POINT'
			
			
			#initialize _mn_topo_assign_backbone nodes
			#node Group Output
			group_output_36 = _mn_topo_assign_backbone.nodes.new("NodeGroupOutput")
			group_output_36.name = "Group Output"
			group_output_36.is_active_output = True
			
			#node Group Input
			group_input_36 = _mn_topo_assign_backbone.nodes.new("NodeGroupInput")
			group_input_36.name = "Group Input"
			
			#node Store Named Attribute.002
			store_named_attribute_002_2 = _mn_topo_assign_backbone.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_002_2.name = "Store Named Attribute.002"
			store_named_attribute_002_2.data_type = 'FLOAT_VECTOR'
			store_named_attribute_002_2.domain = 'POINT'
			#Name
			store_named_attribute_002_2.inputs[2].default_value = "backbone_N"
			
			#node Store Named Attribute.003
			store_named_attribute_003_2 = _mn_topo_assign_backbone.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_003_2.name = "Store Named Attribute.003"
			store_named_attribute_003_2.data_type = 'FLOAT_VECTOR'
			store_named_attribute_003_2.domain = 'POINT'
			#Name
			store_named_attribute_003_2.inputs[2].default_value = "backbone_C"
			
			#node Store Named Attribute.004
			store_named_attribute_004_2 = _mn_topo_assign_backbone.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_004_2.name = "Store Named Attribute.004"
			store_named_attribute_004_2.data_type = 'FLOAT_VECTOR'
			store_named_attribute_004_2.domain = 'POINT'
			#Name
			store_named_attribute_004_2.inputs[2].default_value = "backbone_CA"
			
			#node Store Named Attribute.005
			store_named_attribute_005_2 = _mn_topo_assign_backbone.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_005_2.name = "Store Named Attribute.005"
			store_named_attribute_005_2.data_type = 'FLOAT_VECTOR'
			store_named_attribute_005_2.domain = 'POINT'
			#Name
			store_named_attribute_005_2.inputs[2].default_value = "backbone_O"
			
			#node MN_topo_point_mask.005
			mn_topo_point_mask_005 = _mn_topo_assign_backbone.nodes.new("GeometryNodeGroup")
			mn_topo_point_mask_005.label = "Topology Point Mask"
			mn_topo_point_mask_005.name = "MN_topo_point_mask.005"
			mn_topo_point_mask_005.node_tree = residue_mask
			#Socket_1
			mn_topo_point_mask_005.inputs[0].default_value = 3
			#Socket_5
			mn_topo_point_mask_005.inputs[1].default_value = False
			
			#node MN_topo_point_mask.006
			mn_topo_point_mask_006 = _mn_topo_assign_backbone.nodes.new("GeometryNodeGroup")
			mn_topo_point_mask_006.label = "Topology Point Mask"
			mn_topo_point_mask_006.name = "MN_topo_point_mask.006"
			mn_topo_point_mask_006.node_tree = residue_mask
			#Socket_1
			mn_topo_point_mask_006.inputs[0].default_value = 2
			#Socket_5
			mn_topo_point_mask_006.inputs[1].default_value = False
			
			#node MN_topo_point_mask.007
			mn_topo_point_mask_007 = _mn_topo_assign_backbone.nodes.new("GeometryNodeGroup")
			mn_topo_point_mask_007.label = "Topology Point Mask"
			mn_topo_point_mask_007.name = "MN_topo_point_mask.007"
			mn_topo_point_mask_007.node_tree = residue_mask
			#Socket_1
			mn_topo_point_mask_007.inputs[0].default_value = 4
			#Socket_5
			mn_topo_point_mask_007.inputs[1].default_value = False
			
			#node MN_topo_point_mask.004
			mn_topo_point_mask_004 = _mn_topo_assign_backbone.nodes.new("GeometryNodeGroup")
			mn_topo_point_mask_004.label = "Topology Point Mask"
			mn_topo_point_mask_004.name = "MN_topo_point_mask.004"
			mn_topo_point_mask_004.node_tree = residue_mask
			#Socket_1
			mn_topo_point_mask_004.inputs[0].default_value = 1
			#Socket_5
			mn_topo_point_mask_004.inputs[1].default_value = False
			
			#node Capture Attribute
			capture_attribute_3 = _mn_topo_assign_backbone.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute_3.name = "Capture Attribute"
			capture_attribute_3.active_index = 0
			capture_attribute_3.capture_items.clear()
			capture_attribute_3.capture_items.new('FLOAT', "Unique Group ID")
			capture_attribute_3.capture_items["Unique Group ID"].data_type = 'INT'
			capture_attribute_3.domain = 'POINT'
			
			#node Group
			group_14 = _mn_topo_assign_backbone.nodes.new("GeometryNodeGroup")
			group_14.name = "Group"
			group_14.node_tree = res_group_id
			
			#node Reroute
			reroute_5 = _mn_topo_assign_backbone.nodes.new("NodeReroute")
			reroute_5.name = "Reroute"
			#node Reroute.001
			reroute_001_5 = _mn_topo_assign_backbone.nodes.new("NodeReroute")
			reroute_001_5.name = "Reroute.001"
			#node Reroute.002
			reroute_002_5 = _mn_topo_assign_backbone.nodes.new("NodeReroute")
			reroute_002_5.name = "Reroute.002"
			#node Reroute.003
			reroute_003_3 = _mn_topo_assign_backbone.nodes.new("NodeReroute")
			reroute_003_3.name = "Reroute.003"
			#node Separate Geometry
			separate_geometry_6 = _mn_topo_assign_backbone.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_6.name = "Separate Geometry"
			separate_geometry_6.domain = 'POINT'
			
			#node Group.001
			group_001_6 = _mn_topo_assign_backbone.nodes.new("GeometryNodeGroup")
			group_001_6.name = "Group.001"
			group_001_6.node_tree = is_alpha_carbon
			#Socket_1
			group_001_6.inputs[0].default_value = True
			#Socket_3
			group_001_6.inputs[1].default_value = False
			
			
			
			
			#Set locations
			group_output_36.location = (720.0, 100.0)
			group_input_36.location = (-1200.0, 100.0)
			store_named_attribute_002_2.location = (-400.0, 100.0)
			store_named_attribute_003_2.location = (60.0, 100.0)
			store_named_attribute_004_2.location = (-180.0, 100.0)
			store_named_attribute_005_2.location = (300.0, 100.0)
			mn_topo_point_mask_005.location = (60.0, -120.0)
			mn_topo_point_mask_006.location = (-180.0, -120.0)
			mn_topo_point_mask_007.location = (300.0, -120.0)
			mn_topo_point_mask_004.location = (-400.0, -120.0)
			capture_attribute_3.location = (-1020.0, 100.0)
			group_14.location = (-1200.0, 0.0)
			reroute_5.location = (-440.0, -340.0)
			reroute_001_5.location = (-200.0, -340.0)
			reroute_002_5.location = (40.0, -340.0)
			reroute_003_3.location = (280.0, -340.0)
			separate_geometry_6.location = (540.0, 20.0)
			group_001_6.location = (540.0, -160.0)
			
			#Set dimensions
			group_output_36.width, group_output_36.height = 140.0, 100.0
			group_input_36.width, group_input_36.height = 140.0, 100.0
			store_named_attribute_002_2.width, store_named_attribute_002_2.height = 172.44415283203125, 100.0
			store_named_attribute_003_2.width, store_named_attribute_003_2.height = 169.44052124023438, 100.0
			store_named_attribute_004_2.width, store_named_attribute_004_2.height = 184.14559936523438, 100.0
			store_named_attribute_005_2.width, store_named_attribute_005_2.height = 169.42654418945312, 100.0
			mn_topo_point_mask_005.width, mn_topo_point_mask_005.height = 172.76019287109375, 100.0
			mn_topo_point_mask_006.width, mn_topo_point_mask_006.height = 185.9674072265625, 100.0
			mn_topo_point_mask_007.width, mn_topo_point_mask_007.height = 168.1260986328125, 100.0
			mn_topo_point_mask_004.width, mn_topo_point_mask_004.height = 178.538330078125, 100.0
			capture_attribute_3.width, capture_attribute_3.height = 140.0, 100.0
			group_14.width, group_14.height = 140.0, 100.0
			reroute_5.width, reroute_5.height = 16.0, 100.0
			reroute_001_5.width, reroute_001_5.height = 16.0, 100.0
			reroute_002_5.width, reroute_002_5.height = 16.0, 100.0
			reroute_003_3.width, reroute_003_3.height = 16.0, 100.0
			separate_geometry_6.width, separate_geometry_6.height = 140.0, 100.0
			group_001_6.width, group_001_6.height = 140.0, 100.0
			
			#initialize _mn_topo_assign_backbone links
			#mn_topo_point_mask_007.Is Valid -> store_named_attribute_005_2.Selection
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_007.outputs[0], store_named_attribute_005_2.inputs[1])
			#mn_topo_point_mask_006.Position -> store_named_attribute_004_2.Value
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_006.outputs[2], store_named_attribute_004_2.inputs[3])
			#mn_topo_point_mask_005.Position -> store_named_attribute_003_2.Value
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_005.outputs[2], store_named_attribute_003_2.inputs[3])
			#store_named_attribute_004_2.Geometry -> store_named_attribute_003_2.Geometry
			_mn_topo_assign_backbone.links.new(store_named_attribute_004_2.outputs[0], store_named_attribute_003_2.inputs[0])
			#store_named_attribute_003_2.Geometry -> store_named_attribute_005_2.Geometry
			_mn_topo_assign_backbone.links.new(store_named_attribute_003_2.outputs[0], store_named_attribute_005_2.inputs[0])
			#store_named_attribute_002_2.Geometry -> store_named_attribute_004_2.Geometry
			_mn_topo_assign_backbone.links.new(store_named_attribute_002_2.outputs[0], store_named_attribute_004_2.inputs[0])
			#mn_topo_point_mask_007.Position -> store_named_attribute_005_2.Value
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_007.outputs[2], store_named_attribute_005_2.inputs[3])
			#mn_topo_point_mask_006.Is Valid -> store_named_attribute_004_2.Selection
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_006.outputs[0], store_named_attribute_004_2.inputs[1])
			#mn_topo_point_mask_005.Is Valid -> store_named_attribute_003_2.Selection
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_005.outputs[0], store_named_attribute_003_2.inputs[1])
			#capture_attribute_3.Geometry -> store_named_attribute_002_2.Geometry
			_mn_topo_assign_backbone.links.new(capture_attribute_3.outputs[0], store_named_attribute_002_2.inputs[0])
			#store_named_attribute_005_2.Geometry -> group_output_36.Atoms
			_mn_topo_assign_backbone.links.new(store_named_attribute_005_2.outputs[0], group_output_36.inputs[0])
			#group_input_36.Atoms -> capture_attribute_3.Geometry
			_mn_topo_assign_backbone.links.new(group_input_36.outputs[0], capture_attribute_3.inputs[0])
			#group_14.Unique Group ID -> capture_attribute_3.Unique Group ID
			_mn_topo_assign_backbone.links.new(group_14.outputs[0], capture_attribute_3.inputs[1])
			#reroute_001_5.Output -> mn_topo_point_mask_006.Group ID
			_mn_topo_assign_backbone.links.new(reroute_001_5.outputs[0], mn_topo_point_mask_006.inputs[2])
			#capture_attribute_3.Unique Group ID -> reroute_5.Input
			_mn_topo_assign_backbone.links.new(capture_attribute_3.outputs[1], reroute_5.inputs[0])
			#reroute_5.Output -> reroute_001_5.Input
			_mn_topo_assign_backbone.links.new(reroute_5.outputs[0], reroute_001_5.inputs[0])
			#reroute_002_5.Output -> mn_topo_point_mask_005.Group ID
			_mn_topo_assign_backbone.links.new(reroute_002_5.outputs[0], mn_topo_point_mask_005.inputs[2])
			#reroute_001_5.Output -> reroute_002_5.Input
			_mn_topo_assign_backbone.links.new(reroute_001_5.outputs[0], reroute_002_5.inputs[0])
			#reroute_003_3.Output -> mn_topo_point_mask_007.Group ID
			_mn_topo_assign_backbone.links.new(reroute_003_3.outputs[0], mn_topo_point_mask_007.inputs[2])
			#reroute_002_5.Output -> reroute_003_3.Input
			_mn_topo_assign_backbone.links.new(reroute_002_5.outputs[0], reroute_003_3.inputs[0])
			#capture_attribute_3.Unique Group ID -> group_output_36.Unique Group ID
			_mn_topo_assign_backbone.links.new(capture_attribute_3.outputs[1], group_output_36.inputs[1])
			#mn_topo_point_mask_004.Is Valid -> store_named_attribute_002_2.Selection
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_004.outputs[0], store_named_attribute_002_2.inputs[1])
			#mn_topo_point_mask_004.Position -> store_named_attribute_002_2.Value
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_004.outputs[2], store_named_attribute_002_2.inputs[3])
			#store_named_attribute_005_2.Geometry -> separate_geometry_6.Geometry
			_mn_topo_assign_backbone.links.new(store_named_attribute_005_2.outputs[0], separate_geometry_6.inputs[0])
			#separate_geometry_6.Selection -> group_output_36.CA Atoms
			_mn_topo_assign_backbone.links.new(separate_geometry_6.outputs[0], group_output_36.inputs[2])
			#group_001_6.Selection -> separate_geometry_6.Selection
			_mn_topo_assign_backbone.links.new(group_001_6.outputs[0], separate_geometry_6.inputs[1])
			#reroute_5.Output -> mn_topo_point_mask_004.Group ID
			_mn_topo_assign_backbone.links.new(reroute_5.outputs[0], mn_topo_point_mask_004.inputs[2])
			return _mn_topo_assign_backbone

		_mn_topo_assign_backbone = _mn_topo_assign_backbone_node_group()

		#initialize _is_odd node group
		def _is_odd_node_group():
			_is_odd = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".is_odd")

			_is_odd.color_tag = 'NONE'
			_is_odd.description = ""

			
			#_is_odd interface
			#Socket is_even
			is_even_socket = _is_odd.interface.new_socket(name = "is_even", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_even_socket.attribute_domain = 'POINT'
			
			#Socket is_odd
			is_odd_socket = _is_odd.interface.new_socket(name = "is_odd", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_odd_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_7 = _is_odd.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketInt')
			value_socket_7.subtype = 'NONE'
			value_socket_7.default_value = 0
			value_socket_7.min_value = -2147483648
			value_socket_7.max_value = 2147483647
			value_socket_7.attribute_domain = 'POINT'
			
			
			#initialize _is_odd nodes
			#node Group Input
			group_input_37 = _is_odd.nodes.new("NodeGroupInput")
			group_input_37.name = "Group Input"
			
			#node Group Output
			group_output_37 = _is_odd.nodes.new("NodeGroupOutput")
			group_output_37.name = "Group Output"
			group_output_37.is_active_output = True
			
			#node Boolean Math
			boolean_math_10 = _is_odd.nodes.new("FunctionNodeBooleanMath")
			boolean_math_10.name = "Boolean Math"
			boolean_math_10.operation = 'NOT'
			
			#node Compare.011
			compare_011 = _is_odd.nodes.new("FunctionNodeCompare")
			compare_011.name = "Compare.011"
			compare_011.data_type = 'FLOAT'
			compare_011.mode = 'ELEMENT'
			compare_011.operation = 'EQUAL'
			#B
			compare_011.inputs[1].default_value = 0.0
			#Epsilon
			compare_011.inputs[12].default_value = 0.0010000000474974513
			
			#node Math.008
			math_008 = _is_odd.nodes.new("ShaderNodeMath")
			math_008.name = "Math.008"
			math_008.operation = 'FLOORED_MODULO'
			math_008.use_clamp = False
			#Value_001
			math_008.inputs[1].default_value = 2.0
			
			
			
			
			#Set locations
			group_input_37.location = (-300.0, 80.0)
			group_output_37.location = (240.0, 120.0)
			boolean_math_10.location = (240.0, 20.0)
			compare_011.location = (60.0, 120.0)
			math_008.location = (-100.0, 120.0)
			
			#Set dimensions
			group_input_37.width, group_input_37.height = 140.0, 100.0
			group_output_37.width, group_output_37.height = 140.0, 100.0
			boolean_math_10.width, boolean_math_10.height = 140.0, 100.0
			compare_011.width, compare_011.height = 140.0, 100.0
			math_008.width, math_008.height = 140.0, 100.0
			
			#initialize _is_odd links
			#group_input_37.Value -> math_008.Value
			_is_odd.links.new(group_input_37.outputs[0], math_008.inputs[0])
			#compare_011.Result -> group_output_37.is_even
			_is_odd.links.new(compare_011.outputs[0], group_output_37.inputs[0])
			#compare_011.Result -> boolean_math_10.Boolean
			_is_odd.links.new(compare_011.outputs[0], boolean_math_10.inputs[0])
			#boolean_math_10.Boolean -> group_output_37.is_odd
			_is_odd.links.new(boolean_math_10.outputs[0], group_output_37.inputs[1])
			#math_008.Value -> compare_011.A
			_is_odd.links.new(math_008.outputs[0], compare_011.inputs[0])
			return _is_odd

		_is_odd = _is_odd_node_group()

		#initialize _mn_cartoon_bs_alternate_axis node group
		def _mn_cartoon_bs_alternate_axis_node_group():
			_mn_cartoon_bs_alternate_axis = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_cartoon_bs_alternate_axis")

			_mn_cartoon_bs_alternate_axis.color_tag = 'NONE'
			_mn_cartoon_bs_alternate_axis.description = ""

			
			#_mn_cartoon_bs_alternate_axis interface
			#Socket Z Vector for Euler
			z_vector_for_euler_socket = _mn_cartoon_bs_alternate_axis.interface.new_socket(name = "Z Vector for Euler", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			z_vector_for_euler_socket.subtype = 'NONE'
			z_vector_for_euler_socket.default_value = (0.0, 0.0, 0.0)
			z_vector_for_euler_socket.min_value = -3.4028234663852886e+38
			z_vector_for_euler_socket.max_value = 3.4028234663852886e+38
			z_vector_for_euler_socket.attribute_domain = 'POINT'
			
			#Socket X Vector for Euler
			x_vector_for_euler_socket = _mn_cartoon_bs_alternate_axis.interface.new_socket(name = "X Vector for Euler", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			x_vector_for_euler_socket.subtype = 'NONE'
			x_vector_for_euler_socket.default_value = (0.0, 0.0, 0.0)
			x_vector_for_euler_socket.min_value = -3.4028234663852886e+38
			x_vector_for_euler_socket.max_value = 3.4028234663852886e+38
			x_vector_for_euler_socket.attribute_domain = 'POINT'
			
			#Socket N
			n_socket = _mn_cartoon_bs_alternate_axis.interface.new_socket(name = "N", in_out='INPUT', socket_type = 'NodeSocketVector')
			n_socket.subtype = 'NONE'
			n_socket.default_value = (0.0, 0.0, 0.0)
			n_socket.min_value = -3.4028234663852886e+38
			n_socket.max_value = 3.4028234663852886e+38
			n_socket.attribute_domain = 'POINT'
			
			#Socket C
			c_socket = _mn_cartoon_bs_alternate_axis.interface.new_socket(name = "C", in_out='INPUT', socket_type = 'NodeSocketVector')
			c_socket.subtype = 'NONE'
			c_socket.default_value = (0.0, 0.0, 0.0)
			c_socket.min_value = -3.4028234663852886e+38
			c_socket.max_value = 3.4028234663852886e+38
			c_socket.attribute_domain = 'POINT'
			
			#Socket O
			o_socket = _mn_cartoon_bs_alternate_axis.interface.new_socket(name = "O", in_out='INPUT', socket_type = 'NodeSocketVector')
			o_socket.subtype = 'NONE'
			o_socket.default_value = (0.0, 0.0, 0.0)
			o_socket.min_value = -3.4028234663852886e+38
			o_socket.max_value = 3.4028234663852886e+38
			o_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_cartoon_bs_alternate_axis nodes
			#node Frame
			frame_5 = _mn_cartoon_bs_alternate_axis.nodes.new("NodeFrame")
			frame_5.label = "Only the last AA in an AH is selected"
			frame_5.name = "Frame"
			frame_5.label_size = 20
			frame_5.shrink = True
			
			#node Vector Math.005
			vector_math_005 = _mn_cartoon_bs_alternate_axis.nodes.new("ShaderNodeVectorMath")
			vector_math_005.name = "Vector Math.005"
			vector_math_005.operation = 'SCALE'
			
			#node Blur Attribute.001
			blur_attribute_001 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeBlurAttribute")
			blur_attribute_001.name = "Blur Attribute.001"
			blur_attribute_001.data_type = 'FLOAT_VECTOR'
			#Iterations
			blur_attribute_001.inputs[1].default_value = 3
			#Weight
			blur_attribute_001.inputs[2].default_value = 1.0
			
			#node Switch.002
			switch_002_1 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeSwitch")
			switch_002_1.name = "Switch.002"
			switch_002_1.input_type = 'VECTOR'
			
			#node Group Output
			group_output_38 = _mn_cartoon_bs_alternate_axis.nodes.new("NodeGroupOutput")
			group_output_38.name = "Group Output"
			group_output_38.is_active_output = True
			
			#node Index.001
			index_001_1 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeInputIndex")
			index_001_1.name = "Index.001"
			
			#node Boolean Math.010
			boolean_math_010 = _mn_cartoon_bs_alternate_axis.nodes.new("FunctionNodeBooleanMath")
			boolean_math_010.name = "Boolean Math.010"
			boolean_math_010.operation = 'AND'
			
			#node Reroute.001
			reroute_001_6 = _mn_cartoon_bs_alternate_axis.nodes.new("NodeReroute")
			reroute_001_6.name = "Reroute.001"
			#node Vector Math.004
			vector_math_004_2 = _mn_cartoon_bs_alternate_axis.nodes.new("ShaderNodeVectorMath")
			vector_math_004_2.label = "N -> C"
			vector_math_004_2.name = "Vector Math.004"
			vector_math_004_2.operation = 'SUBTRACT'
			
			#node Group Input
			group_input_38 = _mn_cartoon_bs_alternate_axis.nodes.new("NodeGroupInput")
			group_input_38.name = "Group Input"
			
			#node Vector Math
			vector_math_2 = _mn_cartoon_bs_alternate_axis.nodes.new("ShaderNodeVectorMath")
			vector_math_2.label = "C --> O"
			vector_math_2.name = "Vector Math"
			vector_math_2.operation = 'SUBTRACT'
			
			#node Integer
			integer_3 = _mn_cartoon_bs_alternate_axis.nodes.new("FunctionNodeInputInt")
			integer_3.name = "Integer"
			integer_3.integer = -1
			
			#node Compare
			compare_5 = _mn_cartoon_bs_alternate_axis.nodes.new("FunctionNodeCompare")
			compare_5.name = "Compare"
			compare_5.data_type = 'INT'
			compare_5.mode = 'ELEMENT'
			compare_5.operation = 'GREATER_THAN'
			
			#node Group.014
			group_014_1 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeGroup")
			group_014_1.name = "Group.014"
			group_014_1.node_tree = _sec_struct_counter
			
			#node Boolean Math
			boolean_math_11 = _mn_cartoon_bs_alternate_axis.nodes.new("FunctionNodeBooleanMath")
			boolean_math_11.name = "Boolean Math"
			boolean_math_11.operation = 'AND'
			
			#node Switch
			switch_7 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeSwitch")
			switch_7.name = "Switch"
			switch_7.input_type = 'VECTOR'
			
			#node Group.012
			group_012 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeGroup")
			group_012.name = "Group.012"
			group_012.node_tree = _mn_select_sec_struct
			group_012.outputs[1].hide = True
			group_012.outputs[2].hide = True
			group_012.outputs[3].hide = True
			#Socket_1
			group_012.inputs[0].default_value = True
			
			#node Switch.008
			switch_008_1 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeSwitch")
			switch_008_1.name = "Switch.008"
			switch_008_1.input_type = 'INT'
			#False
			switch_008_1.inputs[1].default_value = 1
			#True
			switch_008_1.inputs[2].default_value = -1
			
			#node Group
			group_15 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeGroup")
			group_15.name = "Group"
			group_15.node_tree = _field_offset
			group_15.inputs[1].hide = True
			group_15.inputs[2].hide = True
			group_15.inputs[3].hide = True
			group_15.outputs[1].hide = True
			group_15.outputs[2].hide = True
			group_15.outputs[3].hide = True
			#Input_3
			group_15.inputs[1].default_value = False
			#Input_5
			group_15.inputs[2].default_value = 0
			#Input_7
			group_15.inputs[3].default_value = 0.0
			
			#node Group.011
			group_011 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeGroup")
			group_011.name = "Group.011"
			group_011.node_tree = _mn_select_sec_struct
			#Socket_1
			group_011.inputs[0].default_value = True
			
			#node Group.005
			group_005_1 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeGroup")
			group_005_1.name = "Group.005"
			group_005_1.node_tree = _is_odd
			
			
			
			#Set parents
			compare_5.parent = frame_5
			group_014_1.parent = frame_5
			boolean_math_11.parent = frame_5
			group_012.parent = frame_5
			
			#Set locations
			frame_5.location = (-86.11199951171875, 65.14605712890625)
			vector_math_005.location = (60.0, 440.0)
			blur_attribute_001.location = (220.0, 400.0)
			switch_002_1.location = (220.0, 580.0)
			group_output_38.location = (400.0, 580.0)
			index_001_1.location = (-381.36767578125, 1.1884498596191406)
			boolean_math_010.location = (-41.36767578125, 101.18844604492188)
			reroute_001_6.location = (-897.6007080078125, 360.3312683105469)
			vector_math_004_2.location = (-817.6007080078125, 540.3312377929688)
			group_input_38.location = (-1077.6007080078125, 420.3312683105469)
			vector_math_2.location = (-817.6007080078125, 400.3312683105469)
			integer_3.location = (-822.031982421875, 264.41668701171875)
			compare_5.location = (-526.031982421875, 831.0416870117188)
			group_014_1.location = (-854.4696655273438, 787.1783447265625)
			boolean_math_11.location = (-366.0320129394531, 831.0416870117188)
			switch_7.location = (-189.45494079589844, 480.51531982421875)
			group_012.location = (-666.031982421875, 651.0416870117188)
			switch_008_1.location = (120.0, 100.0)
			group_15.location = (-622.031982421875, 344.41668701171875)
			group_011.location = (-361.36767578125, 161.18844604492188)
			group_005_1.location = (-221.36767578125, 1.1884498596191406)
			
			#Set dimensions
			frame_5.width, frame_5.height = 688.7999877929688, 326.0
			vector_math_005.width, vector_math_005.height = 140.0, 100.0
			blur_attribute_001.width, blur_attribute_001.height = 140.0, 100.0
			switch_002_1.width, switch_002_1.height = 140.0, 100.0
			group_output_38.width, group_output_38.height = 140.0, 100.0
			index_001_1.width, index_001_1.height = 140.0, 100.0
			boolean_math_010.width, boolean_math_010.height = 140.0, 100.0
			reroute_001_6.width, reroute_001_6.height = 16.0, 100.0
			vector_math_004_2.width, vector_math_004_2.height = 140.0, 100.0
			group_input_38.width, group_input_38.height = 140.0, 100.0
			vector_math_2.width, vector_math_2.height = 140.0, 100.0
			integer_3.width, integer_3.height = 140.0, 100.0
			compare_5.width, compare_5.height = 140.0, 100.0
			group_014_1.width, group_014_1.height = 140.0, 100.0
			boolean_math_11.width, boolean_math_11.height = 140.0, 100.0
			switch_7.width, switch_7.height = 140.0, 100.0
			group_012.width, group_012.height = 277.2730712890625, 100.0
			switch_008_1.width, switch_008_1.height = 140.0, 100.0
			group_15.width, group_15.height = 196.1611328125, 100.0
			group_011.width, group_011.height = 277.2730712890625, 100.0
			group_005_1.width, group_005_1.height = 140.0, 100.0
			
			#initialize _mn_cartoon_bs_alternate_axis links
			#vector_math_005.Vector -> switch_002_1.False
			_mn_cartoon_bs_alternate_axis.links.new(vector_math_005.outputs[0], switch_002_1.inputs[1])
			#blur_attribute_001.Value -> switch_002_1.True
			_mn_cartoon_bs_alternate_axis.links.new(blur_attribute_001.outputs[0], switch_002_1.inputs[2])
			#group_011.Is Sheet -> switch_002_1.Switch
			_mn_cartoon_bs_alternate_axis.links.new(group_011.outputs[1], switch_002_1.inputs[0])
			#group_input_38.C -> reroute_001_6.Input
			_mn_cartoon_bs_alternate_axis.links.new(group_input_38.outputs[1], reroute_001_6.inputs[0])
			#boolean_math_010.Boolean -> switch_008_1.Switch
			_mn_cartoon_bs_alternate_axis.links.new(boolean_math_010.outputs[0], switch_008_1.inputs[0])
			#group_005_1.is_even -> boolean_math_010.Boolean
			_mn_cartoon_bs_alternate_axis.links.new(group_005_1.outputs[0], boolean_math_010.inputs[1])
			#index_001_1.Index -> group_005_1.Value
			_mn_cartoon_bs_alternate_axis.links.new(index_001_1.outputs[0], group_005_1.inputs[0])
			#reroute_001_6.Output -> vector_math_2.Vector
			_mn_cartoon_bs_alternate_axis.links.new(reroute_001_6.outputs[0], vector_math_2.inputs[0])
			#group_011.Is Sheet -> boolean_math_010.Boolean
			_mn_cartoon_bs_alternate_axis.links.new(group_011.outputs[1], boolean_math_010.inputs[0])
			#reroute_001_6.Output -> vector_math_004_2.Vector
			_mn_cartoon_bs_alternate_axis.links.new(reroute_001_6.outputs[0], vector_math_004_2.inputs[1])
			#vector_math_005.Vector -> blur_attribute_001.Value
			_mn_cartoon_bs_alternate_axis.links.new(vector_math_005.outputs[0], blur_attribute_001.inputs[0])
			#switch_008_1.Output -> vector_math_005.Scale
			_mn_cartoon_bs_alternate_axis.links.new(switch_008_1.outputs[0], vector_math_005.inputs[3])
			#group_input_38.O -> vector_math_2.Vector
			_mn_cartoon_bs_alternate_axis.links.new(group_input_38.outputs[2], vector_math_2.inputs[1])
			#switch_002_1.Output -> group_output_38.Z Vector for Euler
			_mn_cartoon_bs_alternate_axis.links.new(switch_002_1.outputs[0], group_output_38.inputs[0])
			#vector_math_004_2.Vector -> group_output_38.X Vector for Euler
			_mn_cartoon_bs_alternate_axis.links.new(vector_math_004_2.outputs[0], group_output_38.inputs[1])
			#group_input_38.N -> vector_math_004_2.Vector
			_mn_cartoon_bs_alternate_axis.links.new(group_input_38.outputs[0], vector_math_004_2.inputs[0])
			#switch_7.Output -> vector_math_005.Vector
			_mn_cartoon_bs_alternate_axis.links.new(switch_7.outputs[0], vector_math_005.inputs[0])
			#group_014_1.Leading -> compare_5.A
			_mn_cartoon_bs_alternate_axis.links.new(group_014_1.outputs[0], compare_5.inputs[2])
			#group_014_1.Trailing -> compare_5.B
			_mn_cartoon_bs_alternate_axis.links.new(group_014_1.outputs[1], compare_5.inputs[3])
			#compare_5.Result -> boolean_math_11.Boolean
			_mn_cartoon_bs_alternate_axis.links.new(compare_5.outputs[0], boolean_math_11.inputs[0])
			#group_012.Is Helix -> boolean_math_11.Boolean
			_mn_cartoon_bs_alternate_axis.links.new(group_012.outputs[0], boolean_math_11.inputs[1])
			#vector_math_2.Vector -> switch_7.False
			_mn_cartoon_bs_alternate_axis.links.new(vector_math_2.outputs[0], switch_7.inputs[1])
			#vector_math_2.Vector -> group_15.Field
			_mn_cartoon_bs_alternate_axis.links.new(vector_math_2.outputs[0], group_15.inputs[0])
			#group_15.Field -> switch_7.True
			_mn_cartoon_bs_alternate_axis.links.new(group_15.outputs[0], switch_7.inputs[2])
			#integer_3.Integer -> group_15.Offset
			_mn_cartoon_bs_alternate_axis.links.new(integer_3.outputs[0], group_15.inputs[4])
			#boolean_math_11.Boolean -> switch_7.Switch
			_mn_cartoon_bs_alternate_axis.links.new(boolean_math_11.outputs[0], switch_7.inputs[0])
			return _mn_cartoon_bs_alternate_axis

		_mn_cartoon_bs_alternate_axis = _mn_cartoon_bs_alternate_axis_node_group()

		#initialize _atoms_to_curves node group
		def _atoms_to_curves_node_group():
			_atoms_to_curves = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".atoms_to_curves")

			_atoms_to_curves.color_tag = 'NONE'
			_atoms_to_curves.description = ""

			_atoms_to_curves.is_modifier = True
			
			#_atoms_to_curves interface
			#Socket CA Mesh Line
			ca_mesh_line_socket = _atoms_to_curves.interface.new_socket(name = "CA Mesh Line", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			ca_mesh_line_socket.attribute_domain = 'POINT'
			
			#Socket CA Splines
			ca_splines_socket = _atoms_to_curves.interface.new_socket(name = "CA Splines", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			ca_splines_socket.attribute_domain = 'POINT'
			
			#Socket AH Splines
			ah_splines_socket = _atoms_to_curves.interface.new_socket(name = "AH Splines", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			ah_splines_socket.attribute_domain = 'POINT'
			
			#Socket AH Mesh Line
			ah_mesh_line_socket = _atoms_to_curves.interface.new_socket(name = "AH Mesh Line", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			ah_mesh_line_socket.attribute_domain = 'POINT'
			
			#Socket BS Splines
			bs_splines_socket = _atoms_to_curves.interface.new_socket(name = "BS Splines", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			bs_splines_socket.attribute_domain = 'POINT'
			
			#Socket BS Mesh Line
			bs_mesh_line_socket = _atoms_to_curves.interface.new_socket(name = "BS Mesh Line", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			bs_mesh_line_socket.attribute_domain = 'POINT'
			
			#Socket Loop Splines
			loop_splines_socket = _atoms_to_curves.interface.new_socket(name = "Loop Splines", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			loop_splines_socket.attribute_domain = 'POINT'
			
			#Socket Loop Mesh Line
			loop_mesh_line_socket = _atoms_to_curves.interface.new_socket(name = "Loop Mesh Line", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			loop_mesh_line_socket.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket_12 = _atoms_to_curves.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_12.attribute_domain = 'POINT'
			atoms_socket_12.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket_14 = _atoms_to_curves.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_14.attribute_domain = 'POINT'
			selection_socket_14.hide_value = True
			selection_socket_14.description = "Selection of atoms to apply this node to"
			
			#Socket BS Smoothing
			bs_smoothing_socket = _atoms_to_curves.interface.new_socket(name = "BS Smoothing", in_out='INPUT', socket_type = 'NodeSocketFloat')
			bs_smoothing_socket.subtype = 'FACTOR'
			bs_smoothing_socket.default_value = 1.0
			bs_smoothing_socket.min_value = 0.0
			bs_smoothing_socket.max_value = 1.0
			bs_smoothing_socket.attribute_domain = 'POINT'
			
			
			#initialize _atoms_to_curves nodes
			#node Frame.006
			frame_006_1 = _atoms_to_curves.nodes.new("NodeFrame")
			frame_006_1.label = "Break mesh where chain_id mismatch or distance cutoff"
			frame_006_1.name = "Frame.006"
			frame_006_1.label_size = 20
			frame_006_1.shrink = True
			
			#node Frame.007
			frame_007_1 = _atoms_to_curves.nodes.new("NodeFrame")
			frame_007_1.label = "Get immediate + and -- AA CA positions"
			frame_007_1.name = "Frame.007"
			frame_007_1.label_size = 20
			frame_007_1.shrink = True
			
			#node Frame.008
			frame_008 = _atoms_to_curves.nodes.new("NodeFrame")
			frame_008.label = "Calculate guide vectors for orientations"
			frame_008.name = "Frame.008"
			frame_008.label_size = 20
			frame_008.shrink = True
			
			#node Frame
			frame_6 = _atoms_to_curves.nodes.new("NodeFrame")
			frame_6.label = "Catch where it changes straight from AH to BS, could be better"
			frame_6.name = "Frame"
			frame_6.label_size = 20
			frame_6.shrink = True
			
			#node Frame.001
			frame_001_3 = _atoms_to_curves.nodes.new("NodeFrame")
			frame_001_3.label = "Split by Secondary Structure"
			frame_001_3.name = "Frame.001"
			frame_001_3.label_size = 20
			frame_001_3.shrink = True
			
			#node Frame.002
			frame_002_3 = _atoms_to_curves.nodes.new("NodeFrame")
			frame_002_3.label = "Turn backboen points to curves"
			frame_002_3.name = "Frame.002"
			frame_002_3.label_size = 20
			frame_002_3.shrink = True
			
			#node Compare.001
			compare_001_4 = _atoms_to_curves.nodes.new("FunctionNodeCompare")
			compare_001_4.name = "Compare.001"
			compare_001_4.data_type = 'INT'
			compare_001_4.mode = 'ELEMENT'
			compare_001_4.operation = 'NOT_EQUAL'
			
			#node Named Attribute.011
			named_attribute_011 = _atoms_to_curves.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_011.name = "Named Attribute.011"
			named_attribute_011.data_type = 'INT'
			#Name
			named_attribute_011.inputs[0].default_value = "chain_id"
			
			#node Evaluate at Index
			evaluate_at_index_4 = _atoms_to_curves.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_4.name = "Evaluate at Index"
			evaluate_at_index_4.data_type = 'INT'
			evaluate_at_index_4.domain = 'POINT'
			
			#node Evaluate at Index.001
			evaluate_at_index_001_2 = _atoms_to_curves.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001_2.name = "Evaluate at Index.001"
			evaluate_at_index_001_2.data_type = 'INT'
			evaluate_at_index_001_2.domain = 'POINT'
			
			#node Reroute.021
			reroute_021 = _atoms_to_curves.nodes.new("NodeReroute")
			reroute_021.name = "Reroute.021"
			#node Edge Vertices
			edge_vertices_2 = _atoms_to_curves.nodes.new("GeometryNodeInputMeshEdgeVertices")
			edge_vertices_2.name = "Edge Vertices"
			
			#node Vector Math
			vector_math_3 = _atoms_to_curves.nodes.new("ShaderNodeVectorMath")
			vector_math_3.name = "Vector Math"
			vector_math_3.operation = 'DISTANCE'
			
			#node Compare
			compare_6 = _atoms_to_curves.nodes.new("FunctionNodeCompare")
			compare_6.name = "Compare"
			compare_6.data_type = 'FLOAT'
			compare_6.mode = 'ELEMENT'
			compare_6.operation = 'GREATER_THAN'
			
			#node Math.001
			math_001_5 = _atoms_to_curves.nodes.new("ShaderNodeMath")
			math_001_5.name = "Math.001"
			math_001_5.operation = 'DIVIDE'
			math_001_5.use_clamp = False
			#Value
			math_001_5.inputs[0].default_value = 60.0
			#Value_001
			math_001_5.inputs[1].default_value = 1000.0
			
			#node Boolean Math.001
			boolean_math_001_8 = _atoms_to_curves.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_8.name = "Boolean Math.001"
			boolean_math_001_8.operation = 'OR'
			
			#node Delete Geometry
			delete_geometry_1 = _atoms_to_curves.nodes.new("GeometryNodeDeleteGeometry")
			delete_geometry_1.name = "Delete Geometry"
			delete_geometry_1.domain = 'EDGE'
			delete_geometry_1.mode = 'ALL'
			
			#node Store Named Attribute.001
			store_named_attribute_001_2 = _atoms_to_curves.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_001_2.name = "Store Named Attribute.001"
			store_named_attribute_001_2.data_type = 'FLOAT_VECTOR'
			store_named_attribute_001_2.domain = 'POINT'
			#Selection
			store_named_attribute_001_2.inputs[1].default_value = True
			#Name
			store_named_attribute_001_2.inputs[2].default_value = "reverse"
			
			#node Store Named Attribute
			store_named_attribute_3 = _atoms_to_curves.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_3.name = "Store Named Attribute"
			store_named_attribute_3.data_type = 'FLOAT_VECTOR'
			store_named_attribute_3.domain = 'POINT'
			#Selection
			store_named_attribute_3.inputs[1].default_value = True
			#Name
			store_named_attribute_3.inputs[2].default_value = "forward"
			
			#node Position.002
			position_002_3 = _atoms_to_curves.nodes.new("GeometryNodeInputPosition")
			position_002_3.name = "Position.002"
			
			#node Store Named Attribute.015
			store_named_attribute_015 = _atoms_to_curves.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_015.name = "Store Named Attribute.015"
			store_named_attribute_015.data_type = 'FLOAT_VECTOR'
			store_named_attribute_015.domain = 'POINT'
			#Selection
			store_named_attribute_015.inputs[1].default_value = True
			#Name
			store_named_attribute_015.inputs[2].default_value = "guide_Z"
			
			#node Store Named Attribute.016
			store_named_attribute_016 = _atoms_to_curves.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_016.name = "Store Named Attribute.016"
			store_named_attribute_016.data_type = 'FLOAT_VECTOR'
			store_named_attribute_016.domain = 'POINT'
			#Selection
			store_named_attribute_016.inputs[1].default_value = True
			#Name
			store_named_attribute_016.inputs[2].default_value = "guide_X"
			
			#node Store Named Attribute.017
			store_named_attribute_017 = _atoms_to_curves.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_017.name = "Store Named Attribute.017"
			store_named_attribute_017.mute = True
			store_named_attribute_017.data_type = 'FLOAT_VECTOR'
			store_named_attribute_017.domain = 'POINT'
			#Selection
			store_named_attribute_017.inputs[1].default_value = True
			#Name
			store_named_attribute_017.inputs[2].default_value = "guide_Y"
			#Value
			store_named_attribute_017.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Named Attribute.012
			named_attribute_012 = _atoms_to_curves.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_012.name = "Named Attribute.012"
			named_attribute_012.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_012.inputs[0].default_value = "backbone_N"
			
			#node Named Attribute.013
			named_attribute_013 = _atoms_to_curves.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_013.name = "Named Attribute.013"
			named_attribute_013.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_013.inputs[0].default_value = "backbone_O"
			
			#node Named Attribute.014
			named_attribute_014 = _atoms_to_curves.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_014.name = "Named Attribute.014"
			named_attribute_014.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_014.inputs[0].default_value = "backbone_C"
			
			#node Group.022
			group_022 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_022.name = "Group.022"
			group_022.node_tree = _field_offset
			#Input_0
			group_022.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Input_5
			group_022.inputs[2].default_value = 0
			#Input_7
			group_022.inputs[3].default_value = 0.0
			#Input_1
			group_022.inputs[4].default_value = -1
			
			#node Group.035
			group_035 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_035.name = "Group.035"
			group_035.node_tree = _field_offset
			#Input_0
			group_035.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Input_5
			group_035.inputs[2].default_value = 0
			#Input_7
			group_035.inputs[3].default_value = 0.0
			#Input_1
			group_035.inputs[4].default_value = 1
			
			#node Boolean Math.005
			boolean_math_005 = _atoms_to_curves.nodes.new("FunctionNodeBooleanMath")
			boolean_math_005.name = "Boolean Math.005"
			boolean_math_005.operation = 'AND'
			
			#node Boolean Math.009
			boolean_math_009 = _atoms_to_curves.nodes.new("FunctionNodeBooleanMath")
			boolean_math_009.name = "Boolean Math.009"
			boolean_math_009.operation = 'OR'
			
			#node Boolean Math.007
			boolean_math_007_1 = _atoms_to_curves.nodes.new("FunctionNodeBooleanMath")
			boolean_math_007_1.name = "Boolean Math.007"
			boolean_math_007_1.operation = 'AND'
			
			#node Group.036
			group_036 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_036.name = "Group.036"
			group_036.node_tree = _field_offset
			#Input_0
			group_036.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Input_5
			group_036.inputs[2].default_value = 0
			#Input_7
			group_036.inputs[3].default_value = 0.0
			#Input_1
			group_036.inputs[4].default_value = -1
			
			#node Boolean Math.010
			boolean_math_010_1 = _atoms_to_curves.nodes.new("FunctionNodeBooleanMath")
			boolean_math_010_1.name = "Boolean Math.010"
			boolean_math_010_1.operation = 'AND'
			
			#node Boolean Math.006
			boolean_math_006 = _atoms_to_curves.nodes.new("FunctionNodeBooleanMath")
			boolean_math_006.name = "Boolean Math.006"
			boolean_math_006.operation = 'OR'
			
			#node Boolean Math.008
			boolean_math_008_1 = _atoms_to_curves.nodes.new("FunctionNodeBooleanMath")
			boolean_math_008_1.name = "Boolean Math.008"
			boolean_math_008_1.operation = 'AND'
			
			#node Boolean Math.011
			boolean_math_011 = _atoms_to_curves.nodes.new("FunctionNodeBooleanMath")
			boolean_math_011.name = "Boolean Math.011"
			boolean_math_011.operation = 'OR'
			
			#node Group.034
			group_034 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_034.name = "Group.034"
			group_034.node_tree = _field_offset
			#Input_0
			group_034.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Input_5
			group_034.inputs[2].default_value = 0
			#Input_7
			group_034.inputs[3].default_value = 0.0
			#Input_1
			group_034.inputs[4].default_value = 1
			
			#node Group.024
			group_024_1 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_024_1.name = "Group.024"
			group_024_1.node_tree = _mn_select_sec_struct
			#Socket_1
			group_024_1.inputs[0].default_value = True
			
			#node Boolean Math.004
			boolean_math_004_1 = _atoms_to_curves.nodes.new("FunctionNodeBooleanMath")
			boolean_math_004_1.name = "Boolean Math.004"
			boolean_math_004_1.operation = 'OR'
			
			#node Mesh to Curve.004
			mesh_to_curve_004 = _atoms_to_curves.nodes.new("GeometryNodeMeshToCurve")
			mesh_to_curve_004.name = "Mesh to Curve.004"
			#Selection
			mesh_to_curve_004.inputs[1].default_value = True
			
			#node Mesh to Curve.003
			mesh_to_curve_003 = _atoms_to_curves.nodes.new("GeometryNodeMeshToCurve")
			mesh_to_curve_003.name = "Mesh to Curve.003"
			#Selection
			mesh_to_curve_003.inputs[1].default_value = True
			
			#node Mesh to Curve.001
			mesh_to_curve_001 = _atoms_to_curves.nodes.new("GeometryNodeMeshToCurve")
			mesh_to_curve_001.name = "Mesh to Curve.001"
			#Selection
			mesh_to_curve_001.inputs[1].default_value = True
			
			#node Mesh to Curve
			mesh_to_curve_2 = _atoms_to_curves.nodes.new("GeometryNodeMeshToCurve")
			mesh_to_curve_2.name = "Mesh to Curve"
			#Selection
			mesh_to_curve_2.inputs[1].default_value = True
			
			#node Reroute.023
			reroute_023 = _atoms_to_curves.nodes.new("NodeReroute")
			reroute_023.name = "Reroute.023"
			#node Reroute.002
			reroute_002_6 = _atoms_to_curves.nodes.new("NodeReroute")
			reroute_002_6.name = "Reroute.002"
			#node Separate Geometry.006
			separate_geometry_006 = _atoms_to_curves.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_006.name = "Separate Geometry.006"
			separate_geometry_006.domain = 'POINT'
			separate_geometry_006.outputs[1].hide = True
			
			#node Separate Geometry.007
			separate_geometry_007 = _atoms_to_curves.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_007.name = "Separate Geometry.007"
			separate_geometry_007.domain = 'POINT'
			separate_geometry_007.outputs[1].hide = True
			
			#node Separate Geometry.008
			separate_geometry_008 = _atoms_to_curves.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_008.name = "Separate Geometry.008"
			separate_geometry_008.domain = 'POINT'
			separate_geometry_008.outputs[1].hide = True
			
			#node Group Input.001
			group_input_001_5 = _atoms_to_curves.nodes.new("NodeGroupInput")
			group_input_001_5.name = "Group Input.001"
			
			#node Group Output
			group_output_39 = _atoms_to_curves.nodes.new("NodeGroupOutput")
			group_output_39.name = "Group Output"
			group_output_39.is_active_output = True
			
			#node Group.012
			group_012_1 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_012_1.name = "Group.012"
			group_012_1.node_tree = _field_offset_vec
			#Input_1
			group_012_1.inputs[1].default_value = -1
			
			#node Group.013
			group_013 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_013.name = "Group.013"
			group_013.node_tree = _field_offset_vec
			#Input_1
			group_013.inputs[1].default_value = 1
			
			#node Group
			group_16 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_16.name = "Group"
			group_16.node_tree = _bs_smooth
			#Input_3
			group_16.inputs[2].default_value = 3
			
			#node Group.023
			group_023 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_023.name = "Group.023"
			group_023.node_tree = _expand_selection
			#Input_2
			group_023.inputs[1].default_value = 1
			
			#node Group.037
			group_037 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_037.name = "Group.037"
			group_037.node_tree = _mn_select_sec_struct
			#Socket_1
			group_037.inputs[0].default_value = True
			
			#node Group Input
			group_input_39 = _atoms_to_curves.nodes.new("NodeGroupInput")
			group_input_39.name = "Group Input"
			
			#node Store Named Attribute.019
			store_named_attribute_019 = _atoms_to_curves.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_019.name = "Store Named Attribute.019"
			store_named_attribute_019.data_type = 'INT'
			store_named_attribute_019.domain = 'POINT'
			#Selection
			store_named_attribute_019.inputs[1].default_value = True
			#Name
			store_named_attribute_019.inputs[2].default_value = "idx"
			
			#node Index.002
			index_002_1 = _atoms_to_curves.nodes.new("GeometryNodeInputIndex")
			index_002_1.name = "Index.002"
			
			#node Separate Geometry.003
			separate_geometry_003 = _atoms_to_curves.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_003.name = "Separate Geometry.003"
			separate_geometry_003.domain = 'POINT'
			
			#node Separate Geometry.001
			separate_geometry_001_1 = _atoms_to_curves.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_001_1.name = "Separate Geometry.001"
			separate_geometry_001_1.domain = 'POINT'
			
			#node Mesh to Points
			mesh_to_points_1 = _atoms_to_curves.nodes.new("GeometryNodeMeshToPoints")
			mesh_to_points_1.name = "Mesh to Points"
			mesh_to_points_1.mode = 'VERTICES'
			#Selection
			mesh_to_points_1.inputs[1].default_value = True
			#Position
			mesh_to_points_1.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Radius
			mesh_to_points_1.inputs[3].default_value = 0.05000000074505806
			
			#node Points to Curves
			points_to_curves = _atoms_to_curves.nodes.new("GeometryNodePointsToCurves")
			points_to_curves.name = "Points to Curves"
			#Weight
			points_to_curves.inputs[2].default_value = 0.0
			
			#node Curve to Mesh
			curve_to_mesh_2 = _atoms_to_curves.nodes.new("GeometryNodeCurveToMesh")
			curve_to_mesh_2.name = "Curve to Mesh"
			#Fill Caps
			curve_to_mesh_2.inputs[2].default_value = False
			
			#node Named Attribute.018
			named_attribute_018 = _atoms_to_curves.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_018.name = "Named Attribute.018"
			named_attribute_018.data_type = 'INT'
			#Name
			named_attribute_018.inputs[0].default_value = "chain_id"
			
			#node Group.001
			group_001_7 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_001_7.name = "Group.001"
			group_001_7.node_tree = is_alpha_carbon
			#Socket_1
			group_001_7.inputs[0].default_value = True
			#Socket_3
			group_001_7.inputs[1].default_value = False
			
			#node Group.006
			group_006_1 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_006_1.name = "Group.006"
			group_006_1.node_tree = _mn_topo_assign_backbone
			
			#node Group.008
			group_008_1 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_008_1.name = "Group.008"
			group_008_1.node_tree = _mn_cartoon_bs_alternate_axis
			
			
			
			#Set parents
			compare_001_4.parent = frame_006_1
			named_attribute_011.parent = frame_006_1
			evaluate_at_index_4.parent = frame_006_1
			evaluate_at_index_001_2.parent = frame_006_1
			reroute_021.parent = frame_006_1
			edge_vertices_2.parent = frame_006_1
			vector_math_3.parent = frame_006_1
			compare_6.parent = frame_006_1
			math_001_5.parent = frame_006_1
			boolean_math_001_8.parent = frame_006_1
			delete_geometry_1.parent = frame_006_1
			store_named_attribute_001_2.parent = frame_007_1
			store_named_attribute_3.parent = frame_007_1
			position_002_3.parent = frame_007_1
			store_named_attribute_015.parent = frame_008
			store_named_attribute_016.parent = frame_008
			store_named_attribute_017.parent = frame_008
			named_attribute_012.parent = frame_008
			named_attribute_013.parent = frame_008
			named_attribute_014.parent = frame_008
			group_022.parent = frame_6
			group_035.parent = frame_6
			boolean_math_005.parent = frame_6
			boolean_math_009.parent = frame_6
			boolean_math_007_1.parent = frame_6
			group_036.parent = frame_6
			boolean_math_010_1.parent = frame_6
			boolean_math_006.parent = frame_6
			boolean_math_008_1.parent = frame_6
			boolean_math_011.parent = frame_6
			group_034.parent = frame_6
			group_024_1.parent = frame_6
			mesh_to_curve_004.parent = frame_001_3
			mesh_to_curve_003.parent = frame_001_3
			mesh_to_curve_001.parent = frame_001_3
			mesh_to_curve_2.parent = frame_001_3
			reroute_023.parent = frame_001_3
			reroute_002_6.parent = frame_001_3
			separate_geometry_006.parent = frame_001_3
			separate_geometry_007.parent = frame_001_3
			separate_geometry_008.parent = frame_001_3
			group_012_1.parent = frame_007_1
			group_013.parent = frame_007_1
			separate_geometry_003.parent = frame_002_3
			separate_geometry_001_1.parent = frame_002_3
			mesh_to_points_1.parent = frame_002_3
			points_to_curves.parent = frame_002_3
			curve_to_mesh_2.parent = frame_002_3
			named_attribute_018.parent = frame_002_3
			group_001_7.parent = frame_002_3
			group_006_1.parent = frame_002_3
			group_008_1.parent = frame_008
			
			#Set locations
			frame_006_1.location = (-26.0, 380.0)
			frame_007_1.location = (-168.0, 46.0)
			frame_008.location = (-166.0, 3.0)
			frame_6.location = (6042.0, 80.0)
			frame_001_3.location = (458.0, -8.0)
			frame_002_3.location = (0.0, 0.0)
			compare_001_4.location = (-1907.6533203125, 300.176513671875)
			named_attribute_011.location = (-2304.4140625, 25.7803955078125)
			evaluate_at_index_4.location = (-2067.6533203125, 300.176513671875)
			evaluate_at_index_001_2.location = (-2067.6533203125, 120.176513671875)
			reroute_021.location = (-2087.6533203125, 100.176513671875)
			edge_vertices_2.location = (-2304.4140625, 165.7803955078125)
			vector_math_3.location = (-2064.4140625, -54.2196044921875)
			compare_6.location = (-1904.4140625, -54.2196044921875)
			math_001_5.location = (-2064.4140625, -194.2196044921875)
			boolean_math_001_8.location = (-1740.0, 300.0)
			delete_geometry_1.location = (-1740.0, 480.0)
			store_named_attribute_001_2.location = (-1062.2197265625, 834.4013671875)
			store_named_attribute_3.location = (-1222.2197265625, 834.4013671875)
			position_002_3.location = (-1222.2197265625, 474.4012451171875)
			store_named_attribute_015.location = (-563.97314453125, 856.68115234375)
			store_named_attribute_016.location = (-383.97314453125, 856.68115234375)
			store_named_attribute_017.location = (-203.97314453125, 856.68115234375)
			named_attribute_012.location = (-743.97314453125, 616.68115234375)
			named_attribute_013.location = (-743.97314453125, 336.68115234375)
			named_attribute_014.location = (-743.97314453125, 476.68115234375)
			group_022.location = (-5080.0, -580.0)
			group_035.location = (-5080.0, -860.0)
			boolean_math_005.location = (-4840.0, -660.0)
			boolean_math_009.location = (-4620.0, -660.0)
			boolean_math_007_1.location = (-4800.0, -60.0)
			group_036.location = (-5040.0, -180.0)
			boolean_math_010_1.location = (-4800.0, -220.0)
			boolean_math_006.location = (-4360.0, -320.0)
			boolean_math_008_1.location = (-4840.0, -820.0)
			boolean_math_011.location = (-4580.0, -100.0)
			group_034.location = (-5040.0, 100.0)
			group_024_1.location = (-5532.35107421875, -374.12896728515625)
			boolean_math_004_1.location = (1120.0, 520.0)
			mesh_to_curve_004.location = (1200.0, 940.0)
			mesh_to_curve_003.location = (1200.0, 820.0)
			mesh_to_curve_001.location = (1200.0, 700.0)
			mesh_to_curve_2.location = (1200.0, 580.0)
			reroute_023.location = (1260.0, 980.0)
			reroute_002_6.location = (960.0, 860.0)
			separate_geometry_006.location = (1040.0, 820.0)
			separate_geometry_007.location = (1040.0, 700.0)
			separate_geometry_008.location = (1040.0, 580.0)
			group_input_001_5.location = (-180.0, 720.0)
			group_output_39.location = (2120.0, 920.0)
			group_012_1.location = (-1222.2197265625, 614.4013671875)
			group_013.location = (-1062.2197265625, 614.4013671875)
			group_16.location = (60.0, 840.0)
			group_023.location = (960.0, 520.0)
			group_037.location = (880.0, 760.0)
			group_input_39.location = (-4220.0, 700.0)
			store_named_attribute_019.location = (-2860.0, 820.0)
			index_002_1.location = (-2860.0, 620.0)
			separate_geometry_003.location = (-3780.0, 780.0)
			separate_geometry_001_1.location = (-3600.0, 780.0)
			mesh_to_points_1.location = (-3420.0, 780.0)
			points_to_curves.location = (-3260.0, 780.0)
			curve_to_mesh_2.location = (-3100.0, 780.0)
			named_attribute_018.location = (-3420.0, 600.0)
			group_001_7.location = (-3780.0, 620.0)
			group_006_1.location = (-4020.0, 780.0)
			group_008_1.location = (-543.97314453125, 596.68115234375)
			
			#Set dimensions
			frame_006_1.width, frame_006_1.height = 764.5, 893.0
			frame_007_1.width, frame_007_1.height = 360.0, 480.0
			frame_008.width, frame_008.height = 740.0, 712.0
			frame_6.width, frame_6.height = 1372.5, 1282.0
			frame_001_3.width, frame_001_3.height = 444.0, 573.0
			frame_002_3.width, frame_002_3.height = 1120.0, 372.0
			compare_001_4.width, compare_001_4.height = 140.0, 100.0
			named_attribute_011.width, named_attribute_011.height = 140.0, 100.0
			evaluate_at_index_4.width, evaluate_at_index_4.height = 140.0, 100.0
			evaluate_at_index_001_2.width, evaluate_at_index_001_2.height = 140.0, 100.0
			reroute_021.width, reroute_021.height = 16.0, 100.0
			edge_vertices_2.width, edge_vertices_2.height = 140.0, 100.0
			vector_math_3.width, vector_math_3.height = 140.0, 100.0
			compare_6.width, compare_6.height = 140.0, 100.0
			math_001_5.width, math_001_5.height = 140.0, 100.0
			boolean_math_001_8.width, boolean_math_001_8.height = 140.0, 100.0
			delete_geometry_1.width, delete_geometry_1.height = 140.0, 100.0
			store_named_attribute_001_2.width, store_named_attribute_001_2.height = 140.0, 100.0
			store_named_attribute_3.width, store_named_attribute_3.height = 140.0, 100.0
			position_002_3.width, position_002_3.height = 140.0, 100.0
			store_named_attribute_015.width, store_named_attribute_015.height = 140.0, 100.0
			store_named_attribute_016.width, store_named_attribute_016.height = 140.0, 100.0
			store_named_attribute_017.width, store_named_attribute_017.height = 140.0, 100.0
			named_attribute_012.width, named_attribute_012.height = 140.0, 100.0
			named_attribute_013.width, named_attribute_013.height = 140.0, 100.0
			named_attribute_014.width, named_attribute_014.height = 140.0, 100.0
			group_022.width, group_022.height = 140.0, 100.0
			group_035.width, group_035.height = 140.0, 100.0
			boolean_math_005.width, boolean_math_005.height = 140.0, 100.0
			boolean_math_009.width, boolean_math_009.height = 140.0, 100.0
			boolean_math_007_1.width, boolean_math_007_1.height = 140.0, 100.0
			group_036.width, group_036.height = 140.0, 100.0
			boolean_math_010_1.width, boolean_math_010_1.height = 140.0, 100.0
			boolean_math_006.width, boolean_math_006.height = 140.0, 100.0
			boolean_math_008_1.width, boolean_math_008_1.height = 140.0, 100.0
			boolean_math_011.width, boolean_math_011.height = 140.0, 100.0
			group_034.width, group_034.height = 140.0, 100.0
			group_024_1.width, group_024_1.height = 158.9053955078125, 100.0
			boolean_math_004_1.width, boolean_math_004_1.height = 140.0, 100.0
			mesh_to_curve_004.width, mesh_to_curve_004.height = 140.0, 100.0
			mesh_to_curve_003.width, mesh_to_curve_003.height = 140.0, 100.0
			mesh_to_curve_001.width, mesh_to_curve_001.height = 140.0, 100.0
			mesh_to_curve_2.width, mesh_to_curve_2.height = 140.0, 100.0
			reroute_023.width, reroute_023.height = 16.0, 100.0
			reroute_002_6.width, reroute_002_6.height = 16.0, 100.0
			separate_geometry_006.width, separate_geometry_006.height = 140.0, 100.0
			separate_geometry_007.width, separate_geometry_007.height = 140.0, 100.0
			separate_geometry_008.width, separate_geometry_008.height = 140.0, 100.0
			group_input_001_5.width, group_input_001_5.height = 140.0, 100.0
			group_output_39.width, group_output_39.height = 140.0, 100.0
			group_012_1.width, group_012_1.height = 140.0, 100.0
			group_013.width, group_013.height = 140.0, 100.0
			group_16.width, group_16.height = 374.382080078125, 100.0
			group_023.width, group_023.height = 140.0, 100.0
			group_037.width, group_037.height = 233.448486328125, 100.0
			group_input_39.width, group_input_39.height = 140.0, 100.0
			store_named_attribute_019.width, store_named_attribute_019.height = 140.0, 100.0
			index_002_1.width, index_002_1.height = 140.0, 100.0
			separate_geometry_003.width, separate_geometry_003.height = 140.0, 100.0
			separate_geometry_001_1.width, separate_geometry_001_1.height = 140.0, 100.0
			mesh_to_points_1.width, mesh_to_points_1.height = 140.0, 100.0
			points_to_curves.width, points_to_curves.height = 140.0, 100.0
			curve_to_mesh_2.width, curve_to_mesh_2.height = 140.0, 100.0
			named_attribute_018.width, named_attribute_018.height = 140.0, 100.0
			group_001_7.width, group_001_7.height = 140.0, 100.0
			group_006_1.width, group_006_1.height = 206.7611083984375, 100.0
			group_008_1.width, group_008_1.height = 318.43975830078125, 100.0
			
			#initialize _atoms_to_curves links
			#group_023.Boolean -> boolean_math_004_1.Boolean
			_atoms_to_curves.links.new(group_023.outputs[0], boolean_math_004_1.inputs[0])
			#group_024_1.Is Helix -> boolean_math_010_1.Boolean
			_atoms_to_curves.links.new(group_024_1.outputs[0], boolean_math_010_1.inputs[1])
			#group_024_1.Is Sheet -> group_036.Value
			_atoms_to_curves.links.new(group_024_1.outputs[1], group_036.inputs[1])
			#group_024_1.Is Sheet -> boolean_math_005.Boolean
			_atoms_to_curves.links.new(group_024_1.outputs[1], boolean_math_005.inputs[0])
			#group_034.Value -> boolean_math_007_1.Boolean
			_atoms_to_curves.links.new(group_034.outputs[1], boolean_math_007_1.inputs[0])
			#group_024_1.Is Sheet -> group_034.Value
			_atoms_to_curves.links.new(group_024_1.outputs[1], group_034.inputs[1])
			#boolean_math_008_1.Boolean -> boolean_math_009.Boolean
			_atoms_to_curves.links.new(boolean_math_008_1.outputs[0], boolean_math_009.inputs[1])
			#position_002_3.Position -> group_013.Field
			_atoms_to_curves.links.new(position_002_3.outputs[0], group_013.inputs[0])
			#position_002_3.Position -> group_012_1.Field
			_atoms_to_curves.links.new(position_002_3.outputs[0], group_012_1.inputs[0])
			#group_012_1.Field -> store_named_attribute_3.Value
			_atoms_to_curves.links.new(group_012_1.outputs[0], store_named_attribute_3.inputs[3])
			#group_037.Is Helix -> separate_geometry_006.Selection
			_atoms_to_curves.links.new(group_037.outputs[0], separate_geometry_006.inputs[1])
			#group_024_1.Is Helix -> group_035.Value
			_atoms_to_curves.links.new(group_024_1.outputs[0], group_035.inputs[1])
			#boolean_math_006.Boolean -> boolean_math_004_1.Boolean
			_atoms_to_curves.links.new(boolean_math_006.outputs[0], boolean_math_004_1.inputs[1])
			#group_024_1.Is Sheet -> boolean_math_008_1.Boolean
			_atoms_to_curves.links.new(group_024_1.outputs[1], boolean_math_008_1.inputs[0])
			#separate_geometry_008.Selection -> mesh_to_curve_2.Mesh
			_atoms_to_curves.links.new(separate_geometry_008.outputs[0], mesh_to_curve_2.inputs[0])
			#boolean_math_007_1.Boolean -> boolean_math_011.Boolean
			_atoms_to_curves.links.new(boolean_math_007_1.outputs[0], boolean_math_011.inputs[0])
			#group_022.Value -> boolean_math_005.Boolean
			_atoms_to_curves.links.new(group_022.outputs[1], boolean_math_005.inputs[1])
			#store_named_attribute_3.Geometry -> store_named_attribute_001_2.Geometry
			_atoms_to_curves.links.new(store_named_attribute_3.outputs[0], store_named_attribute_001_2.inputs[0])
			#group_024_1.Is Helix -> group_022.Value
			_atoms_to_curves.links.new(group_024_1.outputs[0], group_022.inputs[1])
			#boolean_math_009.Boolean -> boolean_math_006.Boolean
			_atoms_to_curves.links.new(boolean_math_009.outputs[0], boolean_math_006.inputs[1])
			#reroute_002_6.Output -> separate_geometry_006.Geometry
			_atoms_to_curves.links.new(reroute_002_6.outputs[0], separate_geometry_006.inputs[0])
			#separate_geometry_006.Selection -> mesh_to_curve_003.Mesh
			_atoms_to_curves.links.new(separate_geometry_006.outputs[0], mesh_to_curve_003.inputs[0])
			#group_013.Field -> store_named_attribute_001_2.Value
			_atoms_to_curves.links.new(group_013.outputs[0], store_named_attribute_001_2.inputs[3])
			#group_035.Value -> boolean_math_008_1.Boolean
			_atoms_to_curves.links.new(group_035.outputs[1], boolean_math_008_1.inputs[1])
			#group_024_1.Is Helix -> boolean_math_007_1.Boolean
			_atoms_to_curves.links.new(group_024_1.outputs[0], boolean_math_007_1.inputs[1])
			#group_036.Value -> boolean_math_010_1.Boolean
			_atoms_to_curves.links.new(group_036.outputs[1], boolean_math_010_1.inputs[0])
			#separate_geometry_007.Selection -> mesh_to_curve_001.Mesh
			_atoms_to_curves.links.new(separate_geometry_007.outputs[0], mesh_to_curve_001.inputs[0])
			#boolean_math_010_1.Boolean -> boolean_math_011.Boolean
			_atoms_to_curves.links.new(boolean_math_010_1.outputs[0], boolean_math_011.inputs[1])
			#boolean_math_005.Boolean -> boolean_math_009.Boolean
			_atoms_to_curves.links.new(boolean_math_005.outputs[0], boolean_math_009.inputs[0])
			#boolean_math_011.Boolean -> boolean_math_006.Boolean
			_atoms_to_curves.links.new(boolean_math_011.outputs[0], boolean_math_006.inputs[0])
			#reroute_023.Output -> group_output_39.CA Mesh Line
			_atoms_to_curves.links.new(reroute_023.outputs[0], group_output_39.inputs[0])
			#mesh_to_curve_001.Curve -> group_output_39.BS Splines
			_atoms_to_curves.links.new(mesh_to_curve_001.outputs[0], group_output_39.inputs[4])
			#mesh_to_curve_2.Curve -> group_output_39.Loop Splines
			_atoms_to_curves.links.new(mesh_to_curve_2.outputs[0], group_output_39.inputs[6])
			#mesh_to_curve_003.Curve -> group_output_39.AH Splines
			_atoms_to_curves.links.new(mesh_to_curve_003.outputs[0], group_output_39.inputs[2])
			#reroute_002_6.Output -> mesh_to_curve_004.Mesh
			_atoms_to_curves.links.new(reroute_002_6.outputs[0], mesh_to_curve_004.inputs[0])
			#mesh_to_curve_004.Curve -> group_output_39.CA Splines
			_atoms_to_curves.links.new(mesh_to_curve_004.outputs[0], group_output_39.inputs[1])
			#edge_vertices_2.Vertex Index 2 -> evaluate_at_index_001_2.Index
			_atoms_to_curves.links.new(edge_vertices_2.outputs[1], evaluate_at_index_001_2.inputs[0])
			#edge_vertices_2.Vertex Index 1 -> evaluate_at_index_4.Index
			_atoms_to_curves.links.new(edge_vertices_2.outputs[0], evaluate_at_index_4.inputs[0])
			#reroute_021.Output -> evaluate_at_index_001_2.Value
			_atoms_to_curves.links.new(reroute_021.outputs[0], evaluate_at_index_001_2.inputs[1])
			#evaluate_at_index_001_2.Value -> compare_001_4.B
			_atoms_to_curves.links.new(evaluate_at_index_001_2.outputs[0], compare_001_4.inputs[3])
			#evaluate_at_index_4.Value -> compare_001_4.A
			_atoms_to_curves.links.new(evaluate_at_index_4.outputs[0], compare_001_4.inputs[2])
			#reroute_021.Output -> evaluate_at_index_4.Value
			_atoms_to_curves.links.new(reroute_021.outputs[0], evaluate_at_index_4.inputs[1])
			#named_attribute_011.Attribute -> reroute_021.Input
			_atoms_to_curves.links.new(named_attribute_011.outputs[0], reroute_021.inputs[0])
			#compare_001_4.Result -> boolean_math_001_8.Boolean
			_atoms_to_curves.links.new(compare_001_4.outputs[0], boolean_math_001_8.inputs[0])
			#boolean_math_001_8.Boolean -> delete_geometry_1.Selection
			_atoms_to_curves.links.new(boolean_math_001_8.outputs[0], delete_geometry_1.inputs[1])
			#edge_vertices_2.Position 1 -> vector_math_3.Vector
			_atoms_to_curves.links.new(edge_vertices_2.outputs[2], vector_math_3.inputs[0])
			#edge_vertices_2.Position 2 -> vector_math_3.Vector
			_atoms_to_curves.links.new(edge_vertices_2.outputs[3], vector_math_3.inputs[1])
			#vector_math_3.Value -> compare_6.A
			_atoms_to_curves.links.new(vector_math_3.outputs[1], compare_6.inputs[0])
			#compare_6.Result -> boolean_math_001_8.Boolean
			_atoms_to_curves.links.new(compare_6.outputs[0], boolean_math_001_8.inputs[1])
			#math_001_5.Value -> compare_6.B
			_atoms_to_curves.links.new(math_001_5.outputs[0], compare_6.inputs[1])
			#store_named_attribute_019.Geometry -> delete_geometry_1.Geometry
			_atoms_to_curves.links.new(store_named_attribute_019.outputs[0], delete_geometry_1.inputs[0])
			#named_attribute_012.Attribute -> group_008_1.N
			_atoms_to_curves.links.new(named_attribute_012.outputs[0], group_008_1.inputs[0])
			#named_attribute_014.Attribute -> group_008_1.C
			_atoms_to_curves.links.new(named_attribute_014.outputs[0], group_008_1.inputs[1])
			#named_attribute_013.Attribute -> group_008_1.O
			_atoms_to_curves.links.new(named_attribute_013.outputs[0], group_008_1.inputs[2])
			#store_named_attribute_015.Geometry -> store_named_attribute_016.Geometry
			_atoms_to_curves.links.new(store_named_attribute_015.outputs[0], store_named_attribute_016.inputs[0])
			#group_008_1.Z Vector for Euler -> store_named_attribute_015.Value
			_atoms_to_curves.links.new(group_008_1.outputs[0], store_named_attribute_015.inputs[3])
			#group_008_1.X Vector for Euler -> store_named_attribute_016.Value
			_atoms_to_curves.links.new(group_008_1.outputs[1], store_named_attribute_016.inputs[3])
			#store_named_attribute_016.Geometry -> store_named_attribute_017.Geometry
			_atoms_to_curves.links.new(store_named_attribute_016.outputs[0], store_named_attribute_017.inputs[0])
			#store_named_attribute_001_2.Geometry -> store_named_attribute_015.Geometry
			_atoms_to_curves.links.new(store_named_attribute_001_2.outputs[0], store_named_attribute_015.inputs[0])
			#group_16.Geometry -> reroute_002_6.Input
			_atoms_to_curves.links.new(group_16.outputs[0], reroute_002_6.inputs[0])
			#reroute_002_6.Output -> reroute_023.Input
			_atoms_to_curves.links.new(reroute_002_6.outputs[0], reroute_023.inputs[0])
			#reroute_002_6.Output -> separate_geometry_007.Geometry
			_atoms_to_curves.links.new(reroute_002_6.outputs[0], separate_geometry_007.inputs[0])
			#reroute_002_6.Output -> separate_geometry_008.Geometry
			_atoms_to_curves.links.new(reroute_002_6.outputs[0], separate_geometry_008.inputs[0])
			#boolean_math_004_1.Boolean -> separate_geometry_008.Selection
			_atoms_to_curves.links.new(boolean_math_004_1.outputs[0], separate_geometry_008.inputs[1])
			#group_037.Is Sheet -> separate_geometry_007.Selection
			_atoms_to_curves.links.new(group_037.outputs[1], separate_geometry_007.inputs[1])
			#group_037.Is Loop -> group_023.Input
			_atoms_to_curves.links.new(group_037.outputs[3], group_023.inputs[0])
			#separate_geometry_006.Selection -> group_output_39.AH Mesh Line
			_atoms_to_curves.links.new(separate_geometry_006.outputs[0], group_output_39.inputs[3])
			#separate_geometry_007.Selection -> group_output_39.BS Mesh Line
			_atoms_to_curves.links.new(separate_geometry_007.outputs[0], group_output_39.inputs[5])
			#separate_geometry_008.Selection -> group_output_39.Loop Mesh Line
			_atoms_to_curves.links.new(separate_geometry_008.outputs[0], group_output_39.inputs[7])
			#store_named_attribute_017.Geometry -> group_16.Geometry
			_atoms_to_curves.links.new(store_named_attribute_017.outputs[0], group_16.inputs[0])
			#group_input_001_5.BS Smoothing -> group_16.Factor
			_atoms_to_curves.links.new(group_input_001_5.outputs[2], group_16.inputs[1])
			#index_002_1.Index -> store_named_attribute_019.Value
			_atoms_to_curves.links.new(index_002_1.outputs[0], store_named_attribute_019.inputs[3])
			#group_input_39.Atoms -> group_006_1.Atoms
			_atoms_to_curves.links.new(group_input_39.outputs[0], group_006_1.inputs[0])
			#separate_geometry_003.Selection -> separate_geometry_001_1.Geometry
			_atoms_to_curves.links.new(separate_geometry_003.outputs[0], separate_geometry_001_1.inputs[0])
			#separate_geometry_001_1.Selection -> mesh_to_points_1.Mesh
			_atoms_to_curves.links.new(separate_geometry_001_1.outputs[0], mesh_to_points_1.inputs[0])
			#mesh_to_points_1.Points -> points_to_curves.Points
			_atoms_to_curves.links.new(mesh_to_points_1.outputs[0], points_to_curves.inputs[0])
			#named_attribute_018.Attribute -> points_to_curves.Curve Group ID
			_atoms_to_curves.links.new(named_attribute_018.outputs[0], points_to_curves.inputs[1])
			#points_to_curves.Curves -> curve_to_mesh_2.Curve
			_atoms_to_curves.links.new(points_to_curves.outputs[0], curve_to_mesh_2.inputs[0])
			#delete_geometry_1.Geometry -> store_named_attribute_3.Geometry
			_atoms_to_curves.links.new(delete_geometry_1.outputs[0], store_named_attribute_3.inputs[0])
			#group_006_1.Atoms -> separate_geometry_003.Geometry
			_atoms_to_curves.links.new(group_006_1.outputs[0], separate_geometry_003.inputs[0])
			#group_input_39.Selection -> separate_geometry_003.Selection
			_atoms_to_curves.links.new(group_input_39.outputs[1], separate_geometry_003.inputs[1])
			#curve_to_mesh_2.Mesh -> store_named_attribute_019.Geometry
			_atoms_to_curves.links.new(curve_to_mesh_2.outputs[0], store_named_attribute_019.inputs[0])
			#group_001_7.Selection -> separate_geometry_001_1.Selection
			_atoms_to_curves.links.new(group_001_7.outputs[0], separate_geometry_001_1.inputs[1])
			return _atoms_to_curves

		_atoms_to_curves = _atoms_to_curves_node_group()

		#initialize _mn_utils_style_ribbon_peptide node group
		def _mn_utils_style_ribbon_peptide_node_group():
			_mn_utils_style_ribbon_peptide = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_utils_style_ribbon_peptide")

			_mn_utils_style_ribbon_peptide.color_tag = 'GEOMETRY'
			_mn_utils_style_ribbon_peptide.description = ""

			_mn_utils_style_ribbon_peptide.is_modifier = True
			
			#_mn_utils_style_ribbon_peptide interface
			#Socket Geometry
			geometry_socket_6 = _mn_utils_style_ribbon_peptide.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_6.attribute_domain = 'POINT'
			
			#Socket Curve
			curve_socket = _mn_utils_style_ribbon_peptide.interface.new_socket(name = "Curve", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			curve_socket.attribute_domain = 'POINT'
			
			#Socket UVs
			uvs_socket = _mn_utils_style_ribbon_peptide.interface.new_socket(name = "UVs", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			uvs_socket.subtype = 'NONE'
			uvs_socket.default_value = (0.0, 0.0, 0.0)
			uvs_socket.min_value = -3.4028234663852886e+38
			uvs_socket.max_value = 3.4028234663852886e+38
			uvs_socket.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket_13 = _mn_utils_style_ribbon_peptide.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_13.attribute_domain = 'POINT'
			atoms_socket_13.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket_15 = _mn_utils_style_ribbon_peptide.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_15.attribute_domain = 'POINT'
			selection_socket_15.hide_value = True
			selection_socket_15.description = "Selection of atoms to apply this node to"
			
			#Socket Quality
			quality_socket_1 = _mn_utils_style_ribbon_peptide.interface.new_socket(name = "Quality", in_out='INPUT', socket_type = 'NodeSocketInt')
			quality_socket_1.subtype = 'NONE'
			quality_socket_1.default_value = 3
			quality_socket_1.min_value = 0
			quality_socket_1.max_value = 6
			quality_socket_1.attribute_domain = 'POINT'
			
			#Socket Radius
			radius_socket_1 = _mn_utils_style_ribbon_peptide.interface.new_socket(name = "Radius", in_out='INPUT', socket_type = 'NodeSocketFloat')
			radius_socket_1.subtype = 'NONE'
			radius_socket_1.default_value = 1.600000023841858
			radius_socket_1.min_value = 0.0
			radius_socket_1.max_value = 3.4028234663852886e+38
			radius_socket_1.attribute_domain = 'POINT'
			
			#Socket BS Smoothing
			bs_smoothing_socket_1 = _mn_utils_style_ribbon_peptide.interface.new_socket(name = "BS Smoothing", in_out='INPUT', socket_type = 'NodeSocketFloat')
			bs_smoothing_socket_1.subtype = 'FACTOR'
			bs_smoothing_socket_1.default_value = 0.5
			bs_smoothing_socket_1.min_value = 0.0
			bs_smoothing_socket_1.max_value = 1.0
			bs_smoothing_socket_1.attribute_domain = 'POINT'
			
			#Socket Interpolate Color
			interpolate_color_socket_1 = _mn_utils_style_ribbon_peptide.interface.new_socket(name = "Interpolate Color", in_out='INPUT', socket_type = 'NodeSocketBool')
			interpolate_color_socket_1.attribute_domain = 'POINT'
			
			#Socket Shade Smooth
			shade_smooth_socket_4 = _mn_utils_style_ribbon_peptide.interface.new_socket(name = "Shade Smooth", in_out='INPUT', socket_type = 'NodeSocketBool')
			shade_smooth_socket_4.attribute_domain = 'POINT'
			shade_smooth_socket_4.description = "Apply smooth shading to the created geometry"
			
			#Socket Material
			material_socket_6 = _mn_utils_style_ribbon_peptide.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial')
			material_socket_6.attribute_domain = 'POINT'
			material_socket_6.description = "Material to apply to the resulting geometry"
			
			
			#initialize _mn_utils_style_ribbon_peptide nodes
			#node Frame.003
			frame_003_3 = _mn_utils_style_ribbon_peptide.nodes.new("NodeFrame")
			frame_003_3.label = "Create mesh from curve"
			frame_003_3.name = "Frame.003"
			frame_003_3.label_size = 20
			frame_003_3.shrink = True
			
			#node Frame
			frame_7 = _mn_utils_style_ribbon_peptide.nodes.new("NodeFrame")
			frame_7.label = "Calculate UVs"
			frame_7.name = "Frame"
			frame_7.label_size = 20
			frame_7.shrink = True
			
			#node Boolean Math.001
			boolean_math_001_9 = _mn_utils_style_ribbon_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_9.name = "Boolean Math.001"
			boolean_math_001_9.operation = 'AND'
			
			#node Named Attribute.001
			named_attribute_001_3 = _mn_utils_style_ribbon_peptide.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001_3.name = "Named Attribute.001"
			named_attribute_001_3.data_type = 'BOOLEAN'
			#Name
			named_attribute_001_3.inputs[0].default_value = "is_alpha_carbon"
			
			#node Group Input.001
			group_input_001_6 = _mn_utils_style_ribbon_peptide.nodes.new("NodeGroupInput")
			group_input_001_6.name = "Group Input.001"
			group_input_001_6.outputs[0].hide = True
			group_input_001_6.outputs[1].hide = True
			group_input_001_6.outputs[2].hide = True
			group_input_001_6.outputs[5].hide = True
			group_input_001_6.outputs[7].hide = True
			group_input_001_6.outputs[8].hide = True
			
			#node Set Material
			set_material_4 = _mn_utils_style_ribbon_peptide.nodes.new("GeometryNodeSetMaterial")
			set_material_4.name = "Set Material"
			#Selection
			set_material_4.inputs[1].default_value = True
			
			#node Group Input.002
			group_input_002_4 = _mn_utils_style_ribbon_peptide.nodes.new("NodeGroupInput")
			group_input_002_4.name = "Group Input.002"
			group_input_002_4.outputs[0].hide = True
			group_input_002_4.outputs[1].hide = True
			group_input_002_4.outputs[2].hide = True
			group_input_002_4.outputs[3].hide = True
			group_input_002_4.outputs[5].hide = True
			group_input_002_4.outputs[6].hide = True
			group_input_002_4.outputs[8].hide = True
			
			#node Sample Index.007
			sample_index_007_2 = _mn_utils_style_ribbon_peptide.nodes.new("GeometryNodeSampleIndex")
			sample_index_007_2.name = "Sample Index.007"
			sample_index_007_2.clamp = True
			sample_index_007_2.data_type = 'BOOLEAN'
			sample_index_007_2.domain = 'POINT'
			
			#node Reroute
			reroute_6 = _mn_utils_style_ribbon_peptide.nodes.new("NodeReroute")
			reroute_6.name = "Reroute"
			#node Group Output
			group_output_40 = _mn_utils_style_ribbon_peptide.nodes.new("NodeGroupOutput")
			group_output_40.name = "Group Output"
			group_output_40.is_active_output = True
			
			#node Group Input
			group_input_40 = _mn_utils_style_ribbon_peptide.nodes.new("NodeGroupInput")
			group_input_40.name = "Group Input"
			group_input_40.outputs[2].hide = True
			group_input_40.outputs[3].hide = True
			group_input_40.outputs[5].hide = True
			group_input_40.outputs[6].hide = True
			group_input_40.outputs[7].hide = True
			group_input_40.outputs[8].hide = True
			
			#node Separate Geometry
			separate_geometry_7 = _mn_utils_style_ribbon_peptide.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_7.name = "Separate Geometry"
			separate_geometry_7.domain = 'POINT'
			
			#node Capture Attribute
			capture_attribute_4 = _mn_utils_style_ribbon_peptide.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute_4.name = "Capture Attribute"
			capture_attribute_4.active_index = 0
			capture_attribute_4.capture_items.clear()
			capture_attribute_4.capture_items.new('FLOAT', "Value")
			capture_attribute_4.capture_items["Value"].data_type = 'BOOLEAN'
			capture_attribute_4.domain = 'POINT'
			
			#node Sample Index.006
			sample_index_006_1 = _mn_utils_style_ribbon_peptide.nodes.new("GeometryNodeSampleIndex")
			sample_index_006_1.name = "Sample Index.006"
			sample_index_006_1.clamp = True
			sample_index_006_1.data_type = 'FLOAT'
			sample_index_006_1.domain = 'POINT'
			
			#node Set Spline Type.002
			set_spline_type_002 = _mn_utils_style_ribbon_peptide.nodes.new("GeometryNodeCurveSplineType")
			set_spline_type_002.name = "Set Spline Type.002"
			set_spline_type_002.spline_type = 'BEZIER'
			#Selection
			set_spline_type_002.inputs[1].default_value = True
			
			#node Reroute.005
			reroute_005_3 = _mn_utils_style_ribbon_peptide.nodes.new("NodeReroute")
			reroute_005_3.name = "Reroute.005"
			#node Capture Attribute.005
			capture_attribute_005 = _mn_utils_style_ribbon_peptide.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute_005.name = "Capture Attribute.005"
			capture_attribute_005.active_index = 0
			capture_attribute_005.capture_items.clear()
			capture_attribute_005.capture_items.new('FLOAT', "Value")
			capture_attribute_005.capture_items["Value"].data_type = 'INT'
			capture_attribute_005.domain = 'POINT'
			
			#node Curve Circle
			curve_circle_2 = _mn_utils_style_ribbon_peptide.nodes.new("GeometryNodeCurvePrimitiveCircle")
			curve_circle_2.name = "Curve Circle"
			curve_circle_2.mode = 'RADIUS'
			#Radius
			curve_circle_2.inputs[4].default_value = 0.009999999776482582
			
			#node Capture Attribute.001
			capture_attribute_001_2 = _mn_utils_style_ribbon_peptide.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute_001_2.name = "Capture Attribute.001"
			capture_attribute_001_2.active_index = 0
			capture_attribute_001_2.capture_items.clear()
			capture_attribute_001_2.capture_items.new('FLOAT', "Value")
			capture_attribute_001_2.capture_items["Value"].data_type = 'FLOAT'
			capture_attribute_001_2.domain = 'POINT'
			
			#node Spline Parameter.001
			spline_parameter_001 = _mn_utils_style_ribbon_peptide.nodes.new("GeometryNodeSplineParameter")
			spline_parameter_001.name = "Spline Parameter.001"
			spline_parameter_001.outputs[0].hide = True
			spline_parameter_001.outputs[2].hide = True
			
			#node Reroute.003
			reroute_003_4 = _mn_utils_style_ribbon_peptide.nodes.new("NodeReroute")
			reroute_003_4.name = "Reroute.003"
			#node Spline Parameter
			spline_parameter = _mn_utils_style_ribbon_peptide.nodes.new("GeometryNodeSplineParameter")
			spline_parameter.name = "Spline Parameter"
			spline_parameter.outputs[1].hide = True
			spline_parameter.outputs[2].hide = True
			
			#node Reroute.004
			reroute_004_2 = _mn_utils_style_ribbon_peptide.nodes.new("NodeReroute")
			reroute_004_2.name = "Reroute.004"
			#node Index.004
			index_004_1 = _mn_utils_style_ribbon_peptide.nodes.new("GeometryNodeInputIndex")
			index_004_1.name = "Index.004"
			
			#node Reroute.001
			reroute_001_7 = _mn_utils_style_ribbon_peptide.nodes.new("NodeReroute")
			reroute_001_7.name = "Reroute.001"
			#node Set Handle Type.001
			set_handle_type_001 = _mn_utils_style_ribbon_peptide.nodes.new("GeometryNodeCurveSetHandles")
			set_handle_type_001.name = "Set Handle Type.001"
			set_handle_type_001.handle_type = 'AUTO'
			set_handle_type_001.mode = {'RIGHT', 'LEFT'}
			#Selection
			set_handle_type_001.inputs[1].default_value = True
			
			#node Set Spline Resolution.001
			set_spline_resolution_001 = _mn_utils_style_ribbon_peptide.nodes.new("GeometryNodeSetSplineResolution")
			set_spline_resolution_001.name = "Set Spline Resolution.001"
			#Selection
			set_spline_resolution_001.inputs[1].default_value = True
			
			#node Set Shade Smooth
			set_shade_smooth_3 = _mn_utils_style_ribbon_peptide.nodes.new("GeometryNodeSetShadeSmooth")
			set_shade_smooth_3.name = "Set Shade Smooth"
			set_shade_smooth_3.domain = 'FACE'
			#Selection
			set_shade_smooth_3.inputs[1].default_value = True
			
			#node Math
			math_9 = _mn_utils_style_ribbon_peptide.nodes.new("ShaderNodeMath")
			math_9.name = "Math"
			math_9.operation = 'WRAP'
			math_9.use_clamp = False
			#Value_001
			math_9.inputs[1].default_value = 1.0
			#Value_002
			math_9.inputs[2].default_value = 0.0
			
			#node Combine XYZ
			combine_xyz_1 = _mn_utils_style_ribbon_peptide.nodes.new("ShaderNodeCombineXYZ")
			combine_xyz_1.name = "Combine XYZ"
			#Z
			combine_xyz_1.inputs[2].default_value = 0.0
			
			#node Switch
			switch_8 = _mn_utils_style_ribbon_peptide.nodes.new("GeometryNodeSwitch")
			switch_8.name = "Switch"
			switch_8.input_type = 'FLOAT'
			#True
			switch_8.inputs[2].default_value = 1.0
			
			#node Evaluate on Domain.001
			evaluate_on_domain_001 = _mn_utils_style_ribbon_peptide.nodes.new("GeometryNodeFieldOnDomain")
			evaluate_on_domain_001.name = "Evaluate on Domain.001"
			evaluate_on_domain_001.data_type = 'FLOAT'
			evaluate_on_domain_001.domain = 'CORNER'
			
			#node Compare.004
			compare_004_2 = _mn_utils_style_ribbon_peptide.nodes.new("FunctionNodeCompare")
			compare_004_2.label = "x == 0"
			compare_004_2.name = "Compare.004"
			compare_004_2.hide = True
			compare_004_2.data_type = 'FLOAT'
			compare_004_2.mode = 'ELEMENT'
			compare_004_2.operation = 'EQUAL'
			#B
			compare_004_2.inputs[1].default_value = 0.0
			#Epsilon
			compare_004_2.inputs[12].default_value = 0.0010000000474974513
			
			#node Boolean Math.004
			boolean_math_004_2 = _mn_utils_style_ribbon_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math_004_2.name = "Boolean Math.004"
			boolean_math_004_2.operation = 'AND'
			
			#node Evaluate on Domain.003
			evaluate_on_domain_003_1 = _mn_utils_style_ribbon_peptide.nodes.new("GeometryNodeFieldOnDomain")
			evaluate_on_domain_003_1.name = "Evaluate on Domain.003"
			evaluate_on_domain_003_1.data_type = 'BOOLEAN'
			evaluate_on_domain_003_1.domain = 'CORNER'
			
			#node Evaluate on Domain
			evaluate_on_domain_1 = _mn_utils_style_ribbon_peptide.nodes.new("GeometryNodeFieldOnDomain")
			evaluate_on_domain_1.name = "Evaluate on Domain"
			evaluate_on_domain_1.data_type = 'FLOAT'
			evaluate_on_domain_1.domain = 'CORNER'
			
			#node Compare.005
			compare_005_2 = _mn_utils_style_ribbon_peptide.nodes.new("FunctionNodeCompare")
			compare_005_2.name = "Compare.005"
			compare_005_2.data_type = 'INT'
			compare_005_2.mode = 'ELEMENT'
			compare_005_2.operation = 'GREATER_THAN'
			#B_INT
			compare_005_2.inputs[3].default_value = 1
			
			#node Reroute.002
			reroute_002_7 = _mn_utils_style_ribbon_peptide.nodes.new("NodeReroute")
			reroute_002_7.name = "Reroute.002"
			#node Evaluate on Domain.002
			evaluate_on_domain_002 = _mn_utils_style_ribbon_peptide.nodes.new("GeometryNodeFieldOnDomain")
			evaluate_on_domain_002.name = "Evaluate on Domain.002"
			evaluate_on_domain_002.data_type = 'INT'
			evaluate_on_domain_002.domain = 'FACE'
			
			#node Evaluate on Domain.004
			evaluate_on_domain_004 = _mn_utils_style_ribbon_peptide.nodes.new("GeometryNodeFieldOnDomain")
			evaluate_on_domain_004.name = "Evaluate on Domain.004"
			evaluate_on_domain_004.data_type = 'FLOAT_VECTOR'
			evaluate_on_domain_004.domain = 'CORNER'
			
			#node Index
			index_5 = _mn_utils_style_ribbon_peptide.nodes.new("GeometryNodeInputIndex")
			index_5.name = "Index"
			
			#node Group Input.004
			group_input_004_2 = _mn_utils_style_ribbon_peptide.nodes.new("NodeGroupInput")
			group_input_004_2.name = "Group Input.004"
			group_input_004_2.outputs[0].hide = True
			group_input_004_2.outputs[1].hide = True
			group_input_004_2.outputs[3].hide = True
			group_input_004_2.outputs[4].hide = True
			group_input_004_2.outputs[5].hide = True
			group_input_004_2.outputs[6].hide = True
			group_input_004_2.outputs[7].hide = True
			group_input_004_2.outputs[8].hide = True
			
			#node Integer
			integer_4 = _mn_utils_style_ribbon_peptide.nodes.new("FunctionNodeInputInt")
			integer_4.name = "Integer"
			integer_4.integer = 2
			
			#node Integer.001
			integer_001_2 = _mn_utils_style_ribbon_peptide.nodes.new("FunctionNodeInputInt")
			integer_001_2.name = "Integer.001"
			integer_001_2.integer = 3
			
			#node Math.002
			math_002_1 = _mn_utils_style_ribbon_peptide.nodes.new("ShaderNodeMath")
			math_002_1.name = "Math.002"
			math_002_1.operation = 'MULTIPLY'
			math_002_1.use_clamp = False
			
			#node Math.001
			math_001_6 = _mn_utils_style_ribbon_peptide.nodes.new("ShaderNodeMath")
			math_001_6.name = "Math.001"
			math_001_6.operation = 'MULTIPLY'
			math_001_6.use_clamp = False
			
			#node Reroute.006
			reroute_006_2 = _mn_utils_style_ribbon_peptide.nodes.new("NodeReroute")
			reroute_006_2.name = "Reroute.006"
			#node Remove Named Attribute
			remove_named_attribute_1 = _mn_utils_style_ribbon_peptide.nodes.new("GeometryNodeRemoveAttribute")
			remove_named_attribute_1.name = "Remove Named Attribute"
			remove_named_attribute_1.pattern_mode = 'EXACT'
			#Name
			remove_named_attribute_1.inputs[1].default_value = "idx"
			
			#node Store Named Attribute
			store_named_attribute_4 = _mn_utils_style_ribbon_peptide.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_4.name = "Store Named Attribute"
			store_named_attribute_4.data_type = 'FLOAT_COLOR'
			store_named_attribute_4.domain = 'FACE'
			#Selection
			store_named_attribute_4.inputs[1].default_value = True
			#Name
			store_named_attribute_4.inputs[2].default_value = "Color"
			
			#node Set Curve Radius
			set_curve_radius_2 = _mn_utils_style_ribbon_peptide.nodes.new("GeometryNodeSetCurveRadius")
			set_curve_radius_2.name = "Set Curve Radius"
			#Selection
			set_curve_radius_2.inputs[1].default_value = True
			
			#node Capture Attribute.002
			capture_attribute_002 = _mn_utils_style_ribbon_peptide.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute_002.name = "Capture Attribute.002"
			capture_attribute_002.active_index = 0
			capture_attribute_002.capture_items.clear()
			capture_attribute_002.capture_items.new('FLOAT', "Value")
			capture_attribute_002.capture_items["Value"].data_type = 'FLOAT'
			capture_attribute_002.domain = 'POINT'
			
			#node Named Attribute.003
			named_attribute_003_2 = _mn_utils_style_ribbon_peptide.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_003_2.name = "Named Attribute.003"
			named_attribute_003_2.data_type = 'INT'
			#Name
			named_attribute_003_2.inputs[0].default_value = "idx"
			
			#node Named Attribute.002
			named_attribute_002_5 = _mn_utils_style_ribbon_peptide.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002_5.name = "Named Attribute.002"
			named_attribute_002_5.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute_002_5.inputs[0].default_value = "Color"
			
			#node Reroute.007
			reroute_007_2 = _mn_utils_style_ribbon_peptide.nodes.new("NodeReroute")
			reroute_007_2.name = "Reroute.007"
			#node Sample Index
			sample_index_2 = _mn_utils_style_ribbon_peptide.nodes.new("GeometryNodeSampleIndex")
			sample_index_2.name = "Sample Index"
			sample_index_2.clamp = False
			sample_index_2.data_type = 'FLOAT_COLOR'
			sample_index_2.domain = 'POINT'
			
			#node Curve to Mesh
			curve_to_mesh_3 = _mn_utils_style_ribbon_peptide.nodes.new("GeometryNodeCurveToMesh")
			curve_to_mesh_3.name = "Curve to Mesh"
			#Fill Caps
			curve_to_mesh_3.inputs[2].default_value = True
			
			#node Group Input.003
			group_input_003_3 = _mn_utils_style_ribbon_peptide.nodes.new("NodeGroupInput")
			group_input_003_3.name = "Group Input.003"
			group_input_003_3.outputs[0].hide = True
			group_input_003_3.outputs[1].hide = True
			group_input_003_3.outputs[2].hide = True
			group_input_003_3.outputs[3].hide = True
			group_input_003_3.outputs[4].hide = True
			group_input_003_3.outputs[6].hide = True
			group_input_003_3.outputs[7].hide = True
			group_input_003_3.outputs[8].hide = True
			
			#node Switch.001
			switch_001_3 = _mn_utils_style_ribbon_peptide.nodes.new("GeometryNodeSwitch")
			switch_001_3.name = "Switch.001"
			switch_001_3.input_type = 'GEOMETRY'
			
			#node Group.001
			group_001_8 = _mn_utils_style_ribbon_peptide.nodes.new("GeometryNodeGroup")
			group_001_8.name = "Group.001"
			group_001_8.node_tree = _atoms_to_curves
			
			
			
			#Set parents
			capture_attribute_4.parent = frame_003_3
			sample_index_006_1.parent = frame_003_3
			set_spline_type_002.parent = frame_003_3
			reroute_005_3.parent = frame_003_3
			capture_attribute_005.parent = frame_003_3
			curve_circle_2.parent = frame_003_3
			capture_attribute_001_2.parent = frame_003_3
			spline_parameter_001.parent = frame_003_3
			reroute_003_4.parent = frame_003_3
			spline_parameter.parent = frame_003_3
			reroute_004_2.parent = frame_003_3
			index_004_1.parent = frame_003_3
			reroute_001_7.parent = frame_003_3
			set_handle_type_001.parent = frame_003_3
			set_spline_resolution_001.parent = frame_003_3
			set_shade_smooth_3.parent = frame_003_3
			math_9.parent = frame_7
			combine_xyz_1.parent = frame_7
			switch_8.parent = frame_7
			evaluate_on_domain_001.parent = frame_7
			compare_004_2.parent = frame_7
			boolean_math_004_2.parent = frame_7
			evaluate_on_domain_003_1.parent = frame_7
			evaluate_on_domain_1.parent = frame_7
			compare_005_2.parent = frame_7
			reroute_002_7.parent = frame_7
			evaluate_on_domain_002.parent = frame_7
			evaluate_on_domain_004.parent = frame_7
			group_input_004_2.parent = frame_003_3
			integer_4.parent = frame_003_3
			integer_001_2.parent = frame_003_3
			math_002_1.parent = frame_003_3
			math_001_6.parent = frame_003_3
			store_named_attribute_4.parent = frame_003_3
			set_curve_radius_2.parent = frame_003_3
			capture_attribute_002.parent = frame_003_3
			curve_to_mesh_3.parent = frame_003_3
			
			#Set locations
			frame_003_3.location = (-3860.39306640625, -98.4256591796875)
			frame_7.location = (650.0, 56.0)
			boolean_math_001_9.location = (-3202.000244140625, 100.0)
			named_attribute_001_3.location = (-3262.000244140625, -40.0)
			group_input_001_6.location = (-3042.000244140625, 40.0)
			set_material_4.location = (-420.0, 660.0)
			group_input_002_4.location = (-420.0, 520.0)
			sample_index_007_2.location = (-2862.000244140625, 340.0)
			reroute_6.location = (-2920.000244140625, 120.0)
			group_output_40.location = (80.0, 660.0)
			group_input_40.location = (-3540.000244140625, 260.0)
			separate_geometry_7.location = (-3202.000244140625, 260.0)
			capture_attribute_4.location = (1169.39306640625, 637.4256591796875)
			sample_index_006_1.location = (1839.39306640625, 137.4256591796875)
			set_spline_type_002.location = (1640.023193359375, 783.5709228515625)
			reroute_005_3.location = (2820.39306640625, 818.4256591796875)
			capture_attribute_005.location = (2580.39306640625, 518.4256591796875)
			curve_circle_2.location = (2400.39306640625, 518.4256591796875)
			capture_attribute_001_2.location = (2740.39306640625, 518.4256591796875)
			spline_parameter_001.location = (2160.39306640625, 598.4256591796875)
			reroute_003_4.location = (2380.39306640625, 218.4256591796875)
			spline_parameter.location = (2740.39306640625, 318.4256591796875)
			reroute_004_2.location = (2740.39306640625, -21.5743408203125)
			index_004_1.location = (2580.39306640625, 318.4256591796875)
			reroute_001_7.location = (3080.39306640625, 578.4256591796875)
			set_handle_type_001.location = (1800.39306640625, 798.4256591796875)
			set_spline_resolution_001.location = (1960.39306640625, 798.4256591796875)
			set_shade_smooth_3.location = (3220.39306640625, 758.4256591796875)
			math_9.location = (-505.4921875, 263.67041015625)
			combine_xyz_1.location = (-340.0, 260.0)
			switch_8.location = (-500.0, 80.0)
			evaluate_on_domain_001.location = (-680.0, 180.0)
			compare_004_2.location = (-680.0, 20.0)
			boolean_math_004_2.location = (-680.0, -20.0)
			evaluate_on_domain_003_1.location = (-840.0, -100.0)
			evaluate_on_domain_1.location = (-680.0, -160.0)
			compare_005_2.location = (-840.0, -240.0)
			reroute_002_7.location = (-700.0, -20.0)
			evaluate_on_domain_002.location = (-1000.0, -240.0)
			evaluate_on_domain_004.location = (-180.0, 260.0)
			index_5.location = (-3040.000244140625, -80.0)
			group_input_004_2.location = (1532.344970703125, 489.52349853515625)
			integer_4.location = (1540.39306640625, 398.4256591796875)
			integer_001_2.location = (1540.39306640625, 298.4256591796875)
			math_002_1.location = (1760.39306640625, 438.4256591796875)
			math_001_6.location = (1760.39306640625, 598.4256591796875)
			reroute_006_2.location = (-280.0, 720.0)
			remove_named_attribute_1.location = (-240.0, 660.0)
			store_named_attribute_4.location = (3000.39306640625, 775.1707763671875)
			set_curve_radius_2.location = (2340.39306640625, 818.4256591796875)
			capture_attribute_002.location = (2160.39306640625, 818.4256591796875)
			named_attribute_003_2.location = (-1120.0, 940.0)
			named_attribute_002_5.location = (-1280.0, 940.0)
			reroute_007_2.location = (-2720.0, 1020.0)
			sample_index_2.location = (-1120.0, 1160.0)
			curve_to_mesh_3.location = (2780.392822265625, 758.4256591796875)
			group_input_003_3.location = (-860.0, 940.0)
			switch_001_3.location = (-860.0, 860.0)
			group_001_8.location = (-3322.000244140625, 580.0)
			
			#Set dimensions
			frame_003_3.width, frame_003_3.height = 2251.0, 952.0
			frame_7.width, frame_7.height = 1020.0, 722.0
			boolean_math_001_9.width, boolean_math_001_9.height = 140.0, 100.0
			named_attribute_001_3.width, named_attribute_001_3.height = 206.99917602539062, 100.0
			group_input_001_6.width, group_input_001_6.height = 140.0, 100.0
			set_material_4.width, set_material_4.height = 140.0, 100.0
			group_input_002_4.width, group_input_002_4.height = 140.0, 100.0
			sample_index_007_2.width, sample_index_007_2.height = 140.0, 100.0
			reroute_6.width, reroute_6.height = 16.0, 100.0
			group_output_40.width, group_output_40.height = 140.0, 100.0
			group_input_40.width, group_input_40.height = 140.0, 100.0
			separate_geometry_7.width, separate_geometry_7.height = 140.0, 100.0
			capture_attribute_4.width, capture_attribute_4.height = 140.0, 100.0
			sample_index_006_1.width, sample_index_006_1.height = 140.0, 100.0
			set_spline_type_002.width, set_spline_type_002.height = 140.0, 100.0
			reroute_005_3.width, reroute_005_3.height = 16.0, 100.0
			capture_attribute_005.width, capture_attribute_005.height = 140.0, 100.0
			curve_circle_2.width, curve_circle_2.height = 140.0, 100.0
			capture_attribute_001_2.width, capture_attribute_001_2.height = 140.0, 100.0
			spline_parameter_001.width, spline_parameter_001.height = 140.0, 100.0
			reroute_003_4.width, reroute_003_4.height = 16.0, 100.0
			spline_parameter.width, spline_parameter.height = 140.0, 100.0
			reroute_004_2.width, reroute_004_2.height = 16.0, 100.0
			index_004_1.width, index_004_1.height = 140.0, 100.0
			reroute_001_7.width, reroute_001_7.height = 16.0, 100.0
			set_handle_type_001.width, set_handle_type_001.height = 140.0, 100.0
			set_spline_resolution_001.width, set_spline_resolution_001.height = 140.0, 100.0
			set_shade_smooth_3.width, set_shade_smooth_3.height = 140.0, 100.0
			math_9.width, math_9.height = 140.0, 100.0
			combine_xyz_1.width, combine_xyz_1.height = 140.0, 100.0
			switch_8.width, switch_8.height = 140.0, 100.0
			evaluate_on_domain_001.width, evaluate_on_domain_001.height = 140.0, 100.0
			compare_004_2.width, compare_004_2.height = 140.0, 100.0
			boolean_math_004_2.width, boolean_math_004_2.height = 140.0, 100.0
			evaluate_on_domain_003_1.width, evaluate_on_domain_003_1.height = 140.0, 100.0
			evaluate_on_domain_1.width, evaluate_on_domain_1.height = 140.0, 100.0
			compare_005_2.width, compare_005_2.height = 140.0, 100.0
			reroute_002_7.width, reroute_002_7.height = 16.0, 100.0
			evaluate_on_domain_002.width, evaluate_on_domain_002.height = 140.0, 100.0
			evaluate_on_domain_004.width, evaluate_on_domain_004.height = 140.0, 100.0
			index_5.width, index_5.height = 140.0, 100.0
			group_input_004_2.width, group_input_004_2.height = 140.0, 100.0
			integer_4.width, integer_4.height = 140.0, 100.0
			integer_001_2.width, integer_001_2.height = 140.0, 100.0
			math_002_1.width, math_002_1.height = 140.0, 100.0
			math_001_6.width, math_001_6.height = 140.0, 100.0
			reroute_006_2.width, reroute_006_2.height = 16.0, 100.0
			remove_named_attribute_1.width, remove_named_attribute_1.height = 170.0, 100.0
			store_named_attribute_4.width, store_named_attribute_4.height = 140.0, 100.0
			set_curve_radius_2.width, set_curve_radius_2.height = 140.0, 100.0
			capture_attribute_002.width, capture_attribute_002.height = 140.0, 100.0
			named_attribute_003_2.width, named_attribute_003_2.height = 140.0, 100.0
			named_attribute_002_5.width, named_attribute_002_5.height = 140.0, 100.0
			reroute_007_2.width, reroute_007_2.height = 16.0, 100.0
			sample_index_2.width, sample_index_2.height = 140.0, 100.0
			curve_to_mesh_3.width, curve_to_mesh_3.height = 140.0, 100.0
			group_input_003_3.width, group_input_003_3.height = 140.0, 100.0
			switch_001_3.width, switch_001_3.height = 140.0, 100.0
			group_001_8.width, group_001_8.height = 261.9332275390625, 100.0
			
			#initialize _mn_utils_style_ribbon_peptide links
			#set_curve_radius_2.Curve -> curve_to_mesh_3.Curve
			_mn_utils_style_ribbon_peptide.links.new(set_curve_radius_2.outputs[0], curve_to_mesh_3.inputs[0])
			#named_attribute_001_3.Attribute -> boolean_math_001_9.Boolean
			_mn_utils_style_ribbon_peptide.links.new(named_attribute_001_3.outputs[0], boolean_math_001_9.inputs[1])
			#boolean_math_001_9.Boolean -> separate_geometry_7.Selection
			_mn_utils_style_ribbon_peptide.links.new(boolean_math_001_9.outputs[0], separate_geometry_7.inputs[1])
			#group_input_40.Selection -> boolean_math_001_9.Boolean
			_mn_utils_style_ribbon_peptide.links.new(group_input_40.outputs[1], boolean_math_001_9.inputs[0])
			#group_input_002_4.Material -> set_material_4.Material
			_mn_utils_style_ribbon_peptide.links.new(group_input_002_4.outputs[7], set_material_4.inputs[2])
			#group_input_40.Atoms -> separate_geometry_7.Geometry
			_mn_utils_style_ribbon_peptide.links.new(group_input_40.outputs[0], separate_geometry_7.inputs[0])
			#reroute_005_3.Output -> reroute_006_2.Input
			_mn_utils_style_ribbon_peptide.links.new(reroute_005_3.outputs[0], reroute_006_2.inputs[0])
			#set_curve_radius_2.Curve -> reroute_005_3.Input
			_mn_utils_style_ribbon_peptide.links.new(set_curve_radius_2.outputs[0], reroute_005_3.inputs[0])
			#reroute_6.Output -> sample_index_006_1.Geometry
			_mn_utils_style_ribbon_peptide.links.new(reroute_6.outputs[0], sample_index_006_1.inputs[0])
			#sample_index_006_1.Value -> set_curve_radius_2.Radius
			_mn_utils_style_ribbon_peptide.links.new(sample_index_006_1.outputs[0], set_curve_radius_2.inputs[2])
			#group_input_001_6.Radius -> sample_index_006_1.Value
			_mn_utils_style_ribbon_peptide.links.new(group_input_001_6.outputs[3], sample_index_006_1.inputs[1])
			#index_5.Index -> sample_index_006_1.Index
			_mn_utils_style_ribbon_peptide.links.new(index_5.outputs[0], sample_index_006_1.inputs[2])
			#reroute_6.Output -> sample_index_007_2.Geometry
			_mn_utils_style_ribbon_peptide.links.new(reroute_6.outputs[0], sample_index_007_2.inputs[0])
			#group_input_001_6.Shade Smooth -> sample_index_007_2.Value
			_mn_utils_style_ribbon_peptide.links.new(group_input_001_6.outputs[6], sample_index_007_2.inputs[1])
			#sample_index_007_2.Value -> capture_attribute_4.Value
			_mn_utils_style_ribbon_peptide.links.new(sample_index_007_2.outputs[0], capture_attribute_4.inputs[1])
			#reroute_001_7.Output -> set_shade_smooth_3.Shade Smooth
			_mn_utils_style_ribbon_peptide.links.new(reroute_001_7.outputs[0], set_shade_smooth_3.inputs[2])
			#group_input_40.Selection -> group_001_8.Selection
			_mn_utils_style_ribbon_peptide.links.new(group_input_40.outputs[1], group_001_8.inputs[1])
			#group_input_40.Atoms -> group_001_8.Atoms
			_mn_utils_style_ribbon_peptide.links.new(group_input_40.outputs[0], group_001_8.inputs[0])
			#group_001_8.CA Splines -> capture_attribute_4.Geometry
			_mn_utils_style_ribbon_peptide.links.new(group_001_8.outputs[1], capture_attribute_4.inputs[0])
			#capture_attribute_002.Geometry -> set_curve_radius_2.Curve
			_mn_utils_style_ribbon_peptide.links.new(capture_attribute_002.outputs[0], set_curve_radius_2.inputs[0])
			#capture_attribute_4.Geometry -> set_spline_type_002.Curve
			_mn_utils_style_ribbon_peptide.links.new(capture_attribute_4.outputs[0], set_spline_type_002.inputs[0])
			#set_spline_type_002.Curve -> set_handle_type_001.Curve
			_mn_utils_style_ribbon_peptide.links.new(set_spline_type_002.outputs[0], set_handle_type_001.inputs[0])
			#set_handle_type_001.Curve -> set_spline_resolution_001.Geometry
			_mn_utils_style_ribbon_peptide.links.new(set_handle_type_001.outputs[0], set_spline_resolution_001.inputs[0])
			#index_5.Index -> sample_index_007_2.Index
			_mn_utils_style_ribbon_peptide.links.new(index_5.outputs[0], sample_index_007_2.inputs[2])
			#separate_geometry_7.Selection -> reroute_6.Input
			_mn_utils_style_ribbon_peptide.links.new(separate_geometry_7.outputs[0], reroute_6.inputs[0])
			#capture_attribute_4.Value -> reroute_001_7.Input
			_mn_utils_style_ribbon_peptide.links.new(capture_attribute_4.outputs[1], reroute_001_7.inputs[0])
			#spline_parameter.Factor -> capture_attribute_001_2.Value
			_mn_utils_style_ribbon_peptide.links.new(spline_parameter.outputs[0], capture_attribute_001_2.inputs[1])
			#math_9.Value -> combine_xyz_1.X
			_mn_utils_style_ribbon_peptide.links.new(math_9.outputs[0], combine_xyz_1.inputs[0])
			#capture_attribute_001_2.Geometry -> curve_to_mesh_3.Profile Curve
			_mn_utils_style_ribbon_peptide.links.new(capture_attribute_001_2.outputs[0], curve_to_mesh_3.inputs[1])
			#curve_circle_2.Curve -> capture_attribute_005.Geometry
			_mn_utils_style_ribbon_peptide.links.new(curve_circle_2.outputs[0], capture_attribute_005.inputs[0])
			#capture_attribute_005.Geometry -> capture_attribute_001_2.Geometry
			_mn_utils_style_ribbon_peptide.links.new(capture_attribute_005.outputs[0], capture_attribute_001_2.inputs[0])
			#index_004_1.Index -> capture_attribute_005.Value
			_mn_utils_style_ribbon_peptide.links.new(index_004_1.outputs[0], capture_attribute_005.inputs[1])
			#reroute_004_2.Output -> evaluate_on_domain_002.Value
			_mn_utils_style_ribbon_peptide.links.new(reroute_004_2.outputs[0], evaluate_on_domain_002.inputs[0])
			#evaluate_on_domain_002.Value -> compare_005_2.A
			_mn_utils_style_ribbon_peptide.links.new(evaluate_on_domain_002.outputs[0], compare_005_2.inputs[2])
			#compare_005_2.Result -> evaluate_on_domain_003_1.Value
			_mn_utils_style_ribbon_peptide.links.new(compare_005_2.outputs[0], evaluate_on_domain_003_1.inputs[0])
			#evaluate_on_domain_1.Value -> switch_8.False
			_mn_utils_style_ribbon_peptide.links.new(evaluate_on_domain_1.outputs[0], switch_8.inputs[1])
			#evaluate_on_domain_003_1.Value -> boolean_math_004_2.Boolean
			_mn_utils_style_ribbon_peptide.links.new(evaluate_on_domain_003_1.outputs[0], boolean_math_004_2.inputs[1])
			#reroute_002_7.Output -> evaluate_on_domain_001.Value
			_mn_utils_style_ribbon_peptide.links.new(reroute_002_7.outputs[0], evaluate_on_domain_001.inputs[0])
			#evaluate_on_domain_001.Value -> compare_004_2.A
			_mn_utils_style_ribbon_peptide.links.new(evaluate_on_domain_001.outputs[0], compare_004_2.inputs[0])
			#boolean_math_004_2.Boolean -> switch_8.Switch
			_mn_utils_style_ribbon_peptide.links.new(boolean_math_004_2.outputs[0], switch_8.inputs[0])
			#reroute_002_7.Output -> evaluate_on_domain_1.Value
			_mn_utils_style_ribbon_peptide.links.new(reroute_002_7.outputs[0], evaluate_on_domain_1.inputs[0])
			#switch_8.Output -> combine_xyz_1.Y
			_mn_utils_style_ribbon_peptide.links.new(switch_8.outputs[0], combine_xyz_1.inputs[1])
			#set_spline_resolution_001.Geometry -> capture_attribute_002.Geometry
			_mn_utils_style_ribbon_peptide.links.new(set_spline_resolution_001.outputs[0], capture_attribute_002.inputs[0])
			#reroute_003_4.Output -> math_9.Value
			_mn_utils_style_ribbon_peptide.links.new(reroute_003_4.outputs[0], math_9.inputs[0])
			#compare_004_2.Result -> boolean_math_004_2.Boolean
			_mn_utils_style_ribbon_peptide.links.new(compare_004_2.outputs[0], boolean_math_004_2.inputs[0])
			#spline_parameter_001.Length -> capture_attribute_002.Value
			_mn_utils_style_ribbon_peptide.links.new(spline_parameter_001.outputs[1], capture_attribute_002.inputs[1])
			#group_input_40.BS Smoothing -> group_001_8.BS Smoothing
			_mn_utils_style_ribbon_peptide.links.new(group_input_40.outputs[4], group_001_8.inputs[2])
			#combine_xyz_1.Vector -> evaluate_on_domain_004.Value
			_mn_utils_style_ribbon_peptide.links.new(combine_xyz_1.outputs[0], evaluate_on_domain_004.inputs[0])
			#evaluate_on_domain_004.Value -> group_output_40.UVs
			_mn_utils_style_ribbon_peptide.links.new(evaluate_on_domain_004.outputs[0], group_output_40.inputs[2])
			#capture_attribute_001_2.Value -> reroute_002_7.Input
			_mn_utils_style_ribbon_peptide.links.new(capture_attribute_001_2.outputs[1], reroute_002_7.inputs[0])
			#capture_attribute_002.Value -> reroute_003_4.Input
			_mn_utils_style_ribbon_peptide.links.new(capture_attribute_002.outputs[1], reroute_003_4.inputs[0])
			#capture_attribute_005.Value -> reroute_004_2.Input
			_mn_utils_style_ribbon_peptide.links.new(capture_attribute_005.outputs[1], reroute_004_2.inputs[0])
			#set_shade_smooth_3.Geometry -> set_material_4.Geometry
			_mn_utils_style_ribbon_peptide.links.new(set_shade_smooth_3.outputs[0], set_material_4.inputs[0])
			#group_input_004_2.Quality -> math_001_6.Value
			_mn_utils_style_ribbon_peptide.links.new(group_input_004_2.outputs[2], math_001_6.inputs[0])
			#integer_4.Integer -> math_001_6.Value
			_mn_utils_style_ribbon_peptide.links.new(integer_4.outputs[0], math_001_6.inputs[1])
			#math_001_6.Value -> set_spline_resolution_001.Resolution
			_mn_utils_style_ribbon_peptide.links.new(math_001_6.outputs[0], set_spline_resolution_001.inputs[2])
			#integer_001_2.Integer -> math_002_1.Value
			_mn_utils_style_ribbon_peptide.links.new(integer_001_2.outputs[0], math_002_1.inputs[1])
			#group_input_004_2.Quality -> math_002_1.Value
			_mn_utils_style_ribbon_peptide.links.new(group_input_004_2.outputs[2], math_002_1.inputs[0])
			#math_002_1.Value -> curve_circle_2.Resolution
			_mn_utils_style_ribbon_peptide.links.new(math_002_1.outputs[0], curve_circle_2.inputs[0])
			#reroute_006_2.Output -> group_output_40.Curve
			_mn_utils_style_ribbon_peptide.links.new(reroute_006_2.outputs[0], group_output_40.inputs[1])
			#set_material_4.Geometry -> remove_named_attribute_1.Geometry
			_mn_utils_style_ribbon_peptide.links.new(set_material_4.outputs[0], remove_named_attribute_1.inputs[0])
			#remove_named_attribute_1.Geometry -> group_output_40.Geometry
			_mn_utils_style_ribbon_peptide.links.new(remove_named_attribute_1.outputs[0], group_output_40.inputs[0])
			#curve_to_mesh_3.Mesh -> store_named_attribute_4.Geometry
			_mn_utils_style_ribbon_peptide.links.new(curve_to_mesh_3.outputs[0], store_named_attribute_4.inputs[0])
			#reroute_007_2.Output -> sample_index_2.Geometry
			_mn_utils_style_ribbon_peptide.links.new(reroute_007_2.outputs[0], sample_index_2.inputs[0])
			#named_attribute_002_5.Attribute -> sample_index_2.Value
			_mn_utils_style_ribbon_peptide.links.new(named_attribute_002_5.outputs[0], sample_index_2.inputs[1])
			#named_attribute_003_2.Attribute -> sample_index_2.Index
			_mn_utils_style_ribbon_peptide.links.new(named_attribute_003_2.outputs[0], sample_index_2.inputs[2])
			#sample_index_2.Value -> store_named_attribute_4.Value
			_mn_utils_style_ribbon_peptide.links.new(sample_index_2.outputs[0], store_named_attribute_4.inputs[3])
			#group_001_8.CA Mesh Line -> reroute_007_2.Input
			_mn_utils_style_ribbon_peptide.links.new(group_001_8.outputs[0], reroute_007_2.inputs[0])
			#store_named_attribute_4.Geometry -> switch_001_3.False
			_mn_utils_style_ribbon_peptide.links.new(store_named_attribute_4.outputs[0], switch_001_3.inputs[1])
			#curve_to_mesh_3.Mesh -> switch_001_3.True
			_mn_utils_style_ribbon_peptide.links.new(curve_to_mesh_3.outputs[0], switch_001_3.inputs[2])
			#switch_001_3.Output -> set_shade_smooth_3.Geometry
			_mn_utils_style_ribbon_peptide.links.new(switch_001_3.outputs[0], set_shade_smooth_3.inputs[0])
			#group_input_003_3.Interpolate Color -> switch_001_3.Switch
			_mn_utils_style_ribbon_peptide.links.new(group_input_003_3.outputs[5], switch_001_3.inputs[0])
			return _mn_utils_style_ribbon_peptide

		_mn_utils_style_ribbon_peptide = _mn_utils_style_ribbon_peptide_node_group()

		#initialize style_ribbon node group
		def style_ribbon_node_group():
			style_ribbon = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Style Ribbon")

			style_ribbon.color_tag = 'GEOMETRY'
			style_ribbon.description = ""

			
			#style_ribbon interface
			#Socket Geometry
			geometry_socket_7 = style_ribbon.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_7.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket_14 = style_ribbon.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_14.attribute_domain = 'POINT'
			atoms_socket_14.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket_16 = style_ribbon.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_16.attribute_domain = 'POINT'
			selection_socket_16.hide_value = True
			selection_socket_16.description = "Selection of atoms to apply this style to"
			
			#Socket Quality
			quality_socket_2 = style_ribbon.interface.new_socket(name = "Quality", in_out='INPUT', socket_type = 'NodeSocketInt')
			quality_socket_2.subtype = 'NONE'
			quality_socket_2.default_value = 3
			quality_socket_2.min_value = 0
			quality_socket_2.max_value = 6
			quality_socket_2.attribute_domain = 'POINT'
			
			#Socket Radius
			radius_socket_2 = style_ribbon.interface.new_socket(name = "Radius", in_out='INPUT', socket_type = 'NodeSocketFloat')
			radius_socket_2.subtype = 'NONE'
			radius_socket_2.default_value = 1.600000023841858
			radius_socket_2.min_value = 0.0
			radius_socket_2.max_value = 3.4028234663852886e+38
			radius_socket_2.attribute_domain = 'POINT'
			
			#Socket Smoothing
			smoothing_socket = style_ribbon.interface.new_socket(name = "Smoothing", in_out='INPUT', socket_type = 'NodeSocketFloat')
			smoothing_socket.subtype = 'FACTOR'
			smoothing_socket.default_value = 0.5
			smoothing_socket.min_value = 0.0
			smoothing_socket.max_value = 1.0
			smoothing_socket.attribute_domain = 'POINT'
			smoothing_socket.description = "Smoothen the sheet ribbons such as beta-sheets"
			
			#Panel Material
			material_panel_3 = style_ribbon.interface.new_panel("Material", default_closed=True)
			#Socket Color Blur
			color_blur_socket_1 = style_ribbon.interface.new_socket(name = "Color Blur", in_out='INPUT', socket_type = 'NodeSocketBool', parent = material_panel_3)
			color_blur_socket_1.attribute_domain = 'POINT'
			
			#Socket Shade Smooth
			shade_smooth_socket_5 = style_ribbon.interface.new_socket(name = "Shade Smooth", in_out='INPUT', socket_type = 'NodeSocketBool', parent = material_panel_3)
			shade_smooth_socket_5.attribute_domain = 'POINT'
			shade_smooth_socket_5.description = "Apply smooth shading to the created geometry"
			
			#Socket Material
			material_socket_7 = style_ribbon.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial', parent = material_panel_3)
			material_socket_7.attribute_domain = 'POINT'
			material_socket_7.description = "Material to apply to the resulting geometry"
			
			
			
			#initialize style_ribbon nodes
			#node Group Output
			group_output_41 = style_ribbon.nodes.new("NodeGroupOutput")
			group_output_41.name = "Group Output"
			group_output_41.is_active_output = True
			
			#node Join Geometry
			join_geometry_1 = style_ribbon.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_1.name = "Join Geometry"
			
			#node Math
			math_10 = style_ribbon.nodes.new("ShaderNodeMath")
			math_10.name = "Math"
			math_10.operation = 'MULTIPLY'
			math_10.use_clamp = False
			#Value_001
			math_10.inputs[1].default_value = 2.0
			
			#node Math.001
			math_001_7 = style_ribbon.nodes.new("ShaderNodeMath")
			math_001_7.name = "Math.001"
			math_001_7.operation = 'MULTIPLY'
			math_001_7.use_clamp = False
			#Value_001
			math_001_7.inputs[1].default_value = 4.0
			
			#node Group Input.001
			group_input_001_7 = style_ribbon.nodes.new("NodeGroupInput")
			group_input_001_7.name = "Group Input.001"
			
			#node Group
			group_17 = style_ribbon.nodes.new("GeometryNodeGroup")
			group_17.label = "Separate Polymers"
			group_17.name = "Group"
			group_17.node_tree = separate_polymers
			
			#node Domain Size
			domain_size_3 = style_ribbon.nodes.new("GeometryNodeAttributeDomainSize")
			domain_size_3.name = "Domain Size"
			domain_size_3.component = 'MESH'
			domain_size_3.outputs[1].hide = True
			domain_size_3.outputs[2].hide = True
			domain_size_3.outputs[3].hide = True
			domain_size_3.outputs[4].hide = True
			domain_size_3.outputs[5].hide = True
			
			#node Compare
			compare_7 = style_ribbon.nodes.new("FunctionNodeCompare")
			compare_7.name = "Compare"
			compare_7.data_type = 'INT'
			compare_7.mode = 'ELEMENT'
			compare_7.operation = 'GREATER_THAN'
			#B_INT
			compare_7.inputs[3].default_value = 0
			
			#node Switch
			switch_9 = style_ribbon.nodes.new("GeometryNodeSwitch")
			switch_9.name = "Switch"
			switch_9.input_type = 'GEOMETRY'
			
			#node Group.069
			group_069 = style_ribbon.nodes.new("GeometryNodeGroup")
			group_069.name = "Group.069"
			group_069.node_tree = _mn_utils_style_ribbon_nucleic
			#Input_28
			group_069.inputs[8].default_value = 0.20000000298023224
			#Input_29
			group_069.inputs[9].default_value = 4
			
			#node Group.027
			group_027 = style_ribbon.nodes.new("GeometryNodeGroup")
			group_027.name = "Group.027"
			group_027.node_tree = _mn_utils_style_ribbon_peptide
			
			
			
			
			#Set locations
			group_output_41.location = (412.468017578125, 118.74327087402344)
			join_geometry_1.location = (238.50283813476562, 96.20518493652344)
			math_10.location = (-340.0, -300.0)
			math_001_7.location = (-340.0, -480.0)
			group_input_001_7.location = (-660.0, -40.0)
			group_17.location = (-428.8030700683594, 129.53338623046875)
			domain_size_3.location = (-400.0, 340.0)
			compare_7.location = (-240.0, 340.0)
			switch_9.location = (0.0, 340.0)
			group_069.location = (-80.0, -140.0)
			group_027.location = (-80.0, 180.0)
			
			#Set dimensions
			group_output_41.width, group_output_41.height = 140.0, 100.0
			join_geometry_1.width, join_geometry_1.height = 140.0, 100.0
			math_10.width, math_10.height = 140.0, 100.0
			math_001_7.width, math_001_7.height = 140.0, 100.0
			group_input_001_7.width, group_input_001_7.height = 140.0, 100.0
			group_17.width, group_17.height = 200.0, 100.0
			domain_size_3.width, domain_size_3.height = 140.0, 100.0
			compare_7.width, compare_7.height = 140.0, 100.0
			switch_9.width, switch_9.height = 140.0, 100.0
			group_069.width, group_069.height = 221.1802978515625, 100.0
			group_027.width, group_027.height = 215.02288818359375, 100.0
			
			#initialize style_ribbon links
			#group_17.Peptide -> group_027.Atoms
			style_ribbon.links.new(group_17.outputs[0], group_027.inputs[0])
			#group_17.Nucleic -> group_069.Atoms
			style_ribbon.links.new(group_17.outputs[1], group_069.inputs[0])
			#group_069.Ribbon + Bases -> join_geometry_1.Geometry
			style_ribbon.links.new(group_069.outputs[0], join_geometry_1.inputs[0])
			#group_input_001_7.Selection -> group_027.Selection
			style_ribbon.links.new(group_input_001_7.outputs[1], group_027.inputs[1])
			#group_input_001_7.Selection -> group_069.Selection
			style_ribbon.links.new(group_input_001_7.outputs[1], group_069.inputs[1])
			#group_input_001_7.Quality -> group_027.Quality
			style_ribbon.links.new(group_input_001_7.outputs[2], group_027.inputs[2])
			#group_input_001_7.Radius -> group_027.Radius
			style_ribbon.links.new(group_input_001_7.outputs[3], group_027.inputs[3])
			#group_input_001_7.Shade Smooth -> group_027.Shade Smooth
			style_ribbon.links.new(group_input_001_7.outputs[6], group_027.inputs[6])
			#group_input_001_7.Material -> group_027.Material
			style_ribbon.links.new(group_input_001_7.outputs[7], group_027.inputs[7])
			#group_input_001_7.Smoothing -> group_027.BS Smoothing
			style_ribbon.links.new(group_input_001_7.outputs[4], group_027.inputs[4])
			#group_input_001_7.Radius -> group_069.Backbone Radius
			style_ribbon.links.new(group_input_001_7.outputs[3], group_069.inputs[6])
			#group_input_001_7.Material -> group_069.Material
			style_ribbon.links.new(group_input_001_7.outputs[7], group_069.inputs[2])
			#group_input_001_7.Shade Smooth -> group_069.Backbone Shade Smooth
			style_ribbon.links.new(group_input_001_7.outputs[6], group_069.inputs[7])
			#join_geometry_1.Geometry -> group_output_41.Geometry
			style_ribbon.links.new(join_geometry_1.outputs[0], group_output_41.inputs[0])
			#group_input_001_7.Quality -> math_10.Value
			style_ribbon.links.new(group_input_001_7.outputs[2], math_10.inputs[0])
			#math_10.Value -> group_069.Backbone Subdivisions
			style_ribbon.links.new(math_10.outputs[0], group_069.inputs[4])
			#group_input_001_7.Quality -> math_001_7.Value
			style_ribbon.links.new(group_input_001_7.outputs[2], math_001_7.inputs[0])
			#math_001_7.Value -> group_069.Backbone Resolution
			style_ribbon.links.new(math_001_7.outputs[0], group_069.inputs[5])
			#group_input_001_7.Atoms -> group_17.Atoms
			style_ribbon.links.new(group_input_001_7.outputs[0], group_17.inputs[0])
			#group_17.Peptide -> domain_size_3.Geometry
			style_ribbon.links.new(group_17.outputs[0], domain_size_3.inputs[0])
			#domain_size_3.Point Count -> compare_7.A
			style_ribbon.links.new(domain_size_3.outputs[0], compare_7.inputs[2])
			#compare_7.Result -> switch_9.Switch
			style_ribbon.links.new(compare_7.outputs[0], switch_9.inputs[0])
			#group_027.Geometry -> switch_9.True
			style_ribbon.links.new(group_027.outputs[0], switch_9.inputs[2])
			#group_input_001_7.Color Blur -> group_027.Interpolate Color
			style_ribbon.links.new(group_input_001_7.outputs[5], group_027.inputs[5])
			#group_input_001_7.Color Blur -> group_069.Intepolate Color
			style_ribbon.links.new(group_input_001_7.outputs[5], group_069.inputs[3])
			#switch_9.Output -> join_geometry_1.Geometry
			style_ribbon.links.new(switch_9.outputs[0], join_geometry_1.inputs[0])
			return style_ribbon

		style_ribbon = style_ribbon_node_group()

		#initialize bond_count node group
		def bond_count_node_group():
			bond_count = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Bond Count")

			bond_count.color_tag = 'INPUT'
			bond_count.description = ""

			
			#bond_count interface
			#Socket Is Bonded
			is_bonded_socket = bond_count.interface.new_socket(name = "Is Bonded", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_bonded_socket.attribute_domain = 'POINT'
			
			#Socket Bonds
			bonds_socket = bond_count.interface.new_socket(name = "Bonds", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			bonds_socket.subtype = 'NONE'
			bonds_socket.default_value = 0
			bonds_socket.min_value = -2147483648
			bonds_socket.max_value = 2147483647
			bonds_socket.attribute_domain = 'POINT'
			bonds_socket.description = "The number of bonds or edges that a point has"
			
			
			#initialize bond_count nodes
			#node Group Output
			group_output_42 = bond_count.nodes.new("NodeGroupOutput")
			group_output_42.name = "Group Output"
			group_output_42.is_active_output = True
			
			#node Group Input
			group_input_41 = bond_count.nodes.new("NodeGroupInput")
			group_input_41.name = "Group Input"
			
			#node Edges of Vertex.001
			edges_of_vertex_001 = bond_count.nodes.new("GeometryNodeEdgesOfVertex")
			edges_of_vertex_001.name = "Edges of Vertex.001"
			#Vertex Index
			edges_of_vertex_001.inputs[0].default_value = 0
			#Weights
			edges_of_vertex_001.inputs[1].default_value = 0.0
			#Sort Index
			edges_of_vertex_001.inputs[2].default_value = 0
			
			#node Compare
			compare_8 = bond_count.nodes.new("FunctionNodeCompare")
			compare_8.name = "Compare"
			compare_8.data_type = 'INT'
			compare_8.mode = 'ELEMENT'
			compare_8.operation = 'GREATER_THAN'
			#B_INT
			compare_8.inputs[3].default_value = 0
			
			
			
			
			#Set locations
			group_output_42.location = (200.0, 100.0)
			group_input_41.location = (-200.0, 0.0)
			edges_of_vertex_001.location = (0.0, 0.0)
			compare_8.location = (0.0, 160.0)
			
			#Set dimensions
			group_output_42.width, group_output_42.height = 140.0, 100.0
			group_input_41.width, group_input_41.height = 140.0, 100.0
			edges_of_vertex_001.width, edges_of_vertex_001.height = 140.0, 100.0
			compare_8.width, compare_8.height = 140.0, 100.0
			
			#initialize bond_count links
			#edges_of_vertex_001.Total -> group_output_42.Bonds
			bond_count.links.new(edges_of_vertex_001.outputs[1], group_output_42.inputs[1])
			#edges_of_vertex_001.Total -> compare_8.A
			bond_count.links.new(edges_of_vertex_001.outputs[1], compare_8.inputs[2])
			#compare_8.Result -> group_output_42.Is Bonded
			bond_count.links.new(compare_8.outputs[0], group_output_42.inputs[0])
			return bond_count

		bond_count = bond_count_node_group()

		#initialize style_preset_1 node group
		def style_preset_1_node_group():
			style_preset_1 = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Style Preset 1")

			style_preset_1.color_tag = 'GEOMETRY'
			style_preset_1.description = ""

			
			#style_preset_1 interface
			#Socket Geometry
			geometry_socket_8 = style_preset_1.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_8.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket_15 = style_preset_1.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_15.attribute_domain = 'POINT'
			
			#Socket Selection
			selection_socket_17 = style_preset_1.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_17.attribute_domain = 'POINT'
			selection_socket_17.hide_value = True
			
			#Socket Quality
			quality_socket_3 = style_preset_1.interface.new_socket(name = "Quality", in_out='INPUT', socket_type = 'NodeSocketInt')
			quality_socket_3.subtype = 'NONE'
			quality_socket_3.default_value = 3
			quality_socket_3.min_value = 0
			quality_socket_3.max_value = 6
			quality_socket_3.attribute_domain = 'POINT'
			
			#Socket Color Blur
			color_blur_socket_2 = style_preset_1.interface.new_socket(name = "Color Blur", in_out='INPUT', socket_type = 'NodeSocketBool')
			color_blur_socket_2.attribute_domain = 'POINT'
			
			#Socket Shade Smooth
			shade_smooth_socket_6 = style_preset_1.interface.new_socket(name = "Shade Smooth", in_out='INPUT', socket_type = 'NodeSocketBool')
			shade_smooth_socket_6.attribute_domain = 'POINT'
			
			#Socket Material
			material_socket_8 = style_preset_1.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial')
			material_socket_8.attribute_domain = 'POINT'
			
			
			#initialize style_preset_1 nodes
			#node Group Output
			group_output_43 = style_preset_1.nodes.new("NodeGroupOutput")
			group_output_43.name = "Group Output"
			group_output_43.is_active_output = True
			
			#node Group Input
			group_input_42 = style_preset_1.nodes.new("NodeGroupInput")
			group_input_42.name = "Group Input"
			
			#node Boolean Math
			boolean_math_12 = style_preset_1.nodes.new("FunctionNodeBooleanMath")
			boolean_math_12.name = "Boolean Math"
			boolean_math_12.operation = 'OR'
			
			#node Switch.002
			switch_002_2 = style_preset_1.nodes.new("GeometryNodeSwitch")
			switch_002_2.name = "Switch.002"
			switch_002_2.input_type = 'FLOAT'
			#False
			switch_002_2.inputs[1].default_value = 1.0
			#True
			switch_002_2.inputs[2].default_value = 0.30000001192092896
			
			#node Join Geometry
			join_geometry_2 = style_preset_1.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_2.name = "Join Geometry"
			
			#node Separate Geometry.001
			separate_geometry_001_2 = style_preset_1.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_001_2.name = "Separate Geometry.001"
			separate_geometry_001_2.domain = 'POINT'
			
			#node Group.002
			group_002_3 = style_preset_1.nodes.new("GeometryNodeGroup")
			group_002_3.label = "Ball and Stick"
			group_002_3.name = "Group.002"
			group_002_3.node_tree = style_ball_and_stick
			#Input_2
			group_002_3.inputs[3].default_value = False
			#Socket_3
			group_002_3.inputs[5].default_value = True
			#Input_7
			group_002_3.inputs[6].default_value = 0.25
			
			#node MN_style_ribbon
			mn_style_ribbon = style_preset_1.nodes.new("GeometryNodeGroup")
			mn_style_ribbon.label = "Style Ribbon"
			mn_style_ribbon.name = "MN_style_ribbon"
			mn_style_ribbon.node_tree = style_ribbon
			#Socket_4
			mn_style_ribbon.inputs[3].default_value = 1.399999976158142
			#Socket_7
			mn_style_ribbon.inputs[4].default_value = 0.5
			
			#node Group.012
			group_012_2 = style_preset_1.nodes.new("GeometryNodeGroup")
			group_012_2.name = "Group.012"
			group_012_2.node_tree = is_nucleic
			#Socket_1
			group_012_2.inputs[0].default_value = True
			#Socket_3
			group_012_2.inputs[1].default_value = False
			
			#node Group.006
			group_006_2 = style_preset_1.nodes.new("GeometryNodeGroup")
			group_006_2.name = "Group.006"
			group_006_2.node_tree = is_peptide
			#Socket_1
			group_006_2.inputs[0].default_value = True
			#Socket_3
			group_006_2.inputs[1].default_value = False
			
			#node Group
			group_18 = style_preset_1.nodes.new("GeometryNodeGroup")
			group_18.name = "Group"
			group_18.node_tree = bond_count
			
			#node Math
			math_11 = style_preset_1.nodes.new("ShaderNodeMath")
			math_11.name = "Math"
			math_11.operation = 'MULTIPLY'
			math_11.use_clamp = False
			#Value_001
			math_11.inputs[1].default_value = 4.0
			
			
			
			
			#Set locations
			group_output_43.location = (790.41015625, 0.0)
			group_input_42.location = (-770.58984375, 0.0)
			boolean_math_12.location = (-100.0, 240.0)
			switch_002_2.location = (120.0, -160.0)
			join_geometry_2.location = (570.58984375, 20.10931396484375)
			separate_geometry_001_2.location = (100.0, 240.0)
			group_002_3.location = (300.0, -40.0)
			mn_style_ribbon.location = (300.0, 240.0)
			group_012_2.location = (-260.0, 140.0)
			group_006_2.location = (-260.0, 240.0)
			group_18.location = (-60.0, -160.0)
			math_11.location = (120.0, -340.0)
			
			#Set dimensions
			group_output_43.width, group_output_43.height = 140.0, 100.0
			group_input_42.width, group_input_42.height = 140.0, 100.0
			boolean_math_12.width, boolean_math_12.height = 140.0, 100.0
			switch_002_2.width, switch_002_2.height = 140.0, 100.0
			join_geometry_2.width, join_geometry_2.height = 140.0, 100.0
			separate_geometry_001_2.width, separate_geometry_001_2.height = 140.0, 100.0
			group_002_3.width, group_002_3.height = 200.0, 100.0
			mn_style_ribbon.width, mn_style_ribbon.height = 200.0, 100.0
			group_012_2.width, group_012_2.height = 140.0, 100.0
			group_006_2.width, group_006_2.height = 140.0, 100.0
			group_18.width, group_18.height = 140.0, 100.0
			math_11.width, math_11.height = 140.0, 100.0
			
			#initialize style_preset_1 links
			#separate_geometry_001_2.Inverted -> group_002_3.Atoms
			style_preset_1.links.new(separate_geometry_001_2.outputs[1], group_002_3.inputs[0])
			#group_002_3.Geometry -> join_geometry_2.Geometry
			style_preset_1.links.new(group_002_3.outputs[0], join_geometry_2.inputs[0])
			#separate_geometry_001_2.Selection -> mn_style_ribbon.Atoms
			style_preset_1.links.new(separate_geometry_001_2.outputs[0], mn_style_ribbon.inputs[0])
			#switch_002_2.Output -> group_002_3.Sphere Radii
			style_preset_1.links.new(switch_002_2.outputs[0], group_002_3.inputs[4])
			#boolean_math_12.Boolean -> separate_geometry_001_2.Selection
			style_preset_1.links.new(boolean_math_12.outputs[0], separate_geometry_001_2.inputs[1])
			#group_012_2.Selection -> boolean_math_12.Boolean
			style_preset_1.links.new(group_012_2.outputs[0], boolean_math_12.inputs[1])
			#group_input_42.Atoms -> separate_geometry_001_2.Geometry
			style_preset_1.links.new(group_input_42.outputs[0], separate_geometry_001_2.inputs[0])
			#group_006_2.Selection -> boolean_math_12.Boolean
			style_preset_1.links.new(group_006_2.outputs[0], boolean_math_12.inputs[0])
			#group_input_42.Shade Smooth -> group_002_3.Shade Smooth
			style_preset_1.links.new(group_input_42.outputs[4], group_002_3.inputs[8])
			#group_input_42.Shade Smooth -> mn_style_ribbon.Shade Smooth
			style_preset_1.links.new(group_input_42.outputs[4], mn_style_ribbon.inputs[6])
			#group_input_42.Quality -> mn_style_ribbon.Quality
			style_preset_1.links.new(group_input_42.outputs[2], mn_style_ribbon.inputs[2])
			#group_input_42.Material -> group_002_3.Material
			style_preset_1.links.new(group_input_42.outputs[5], group_002_3.inputs[9])
			#group_input_42.Material -> mn_style_ribbon.Material
			style_preset_1.links.new(group_input_42.outputs[5], mn_style_ribbon.inputs[7])
			#join_geometry_2.Geometry -> group_output_43.Geometry
			style_preset_1.links.new(join_geometry_2.outputs[0], group_output_43.inputs[0])
			#group_18.Is Bonded -> switch_002_2.Switch
			style_preset_1.links.new(group_18.outputs[0], switch_002_2.inputs[0])
			#group_input_42.Quality -> math_11.Value
			style_preset_1.links.new(group_input_42.outputs[2], math_11.inputs[0])
			#group_input_42.Color Blur -> mn_style_ribbon.Color Blur
			style_preset_1.links.new(group_input_42.outputs[3], mn_style_ribbon.inputs[5])
			#group_input_42.Color Blur -> group_002_3.Color Blur
			style_preset_1.links.new(group_input_42.outputs[3], group_002_3.inputs[7])
			#group_input_42.Quality -> group_002_3.Quality
			style_preset_1.links.new(group_input_42.outputs[2], group_002_3.inputs[1])
			#group_input_42.Selection -> mn_style_ribbon.Selection
			style_preset_1.links.new(group_input_42.outputs[1], mn_style_ribbon.inputs[1])
			#group_input_42.Selection -> group_002_3.Selection
			style_preset_1.links.new(group_input_42.outputs[1], group_002_3.inputs[2])
			#mn_style_ribbon.Geometry -> join_geometry_2.Geometry
			style_preset_1.links.new(mn_style_ribbon.outputs[0], join_geometry_2.inputs[0])
			return style_preset_1

		style_preset_1 = style_preset_1_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Style Preset 1", type = 'NODES')
		mod.node_group = style_preset_1
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Style_Preset_1.bl_idname)
			
def register():
	bpy.utils.register_class(Style_Preset_1)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Style_Preset_1)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
