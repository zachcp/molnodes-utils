bl_info = {
	"name" : "Style Preset 2",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Style_Preset_2(bpy.types.Operator):
	bl_idname = "node.style_preset_2"
	bl_label = "Style Preset 2"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _mn_utils_int_multiply node group
		def _mn_utils_int_multiply_node_group():
			_mn_utils_int_multiply = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_utils_int_multiply")

			_mn_utils_int_multiply.color_tag = 'CONVERTER'
			_mn_utils_int_multiply.description = ""

			
			#_mn_utils_int_multiply interface
			#Socket Value
			value_socket = _mn_utils_int_multiply.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			value_socket.subtype = 'NONE'
			value_socket.default_value = 0
			value_socket.min_value = -2147483648
			value_socket.max_value = 2147483647
			value_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_1 = _mn_utils_int_multiply.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketInt')
			value_socket_1.subtype = 'NONE'
			value_socket_1.default_value = 0
			value_socket_1.min_value = -2147483648
			value_socket_1.max_value = 2147483647
			value_socket_1.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_2 = _mn_utils_int_multiply.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketInt')
			value_socket_2.subtype = 'NONE'
			value_socket_2.default_value = 0
			value_socket_2.min_value = -2147483648
			value_socket_2.max_value = 2147483647
			value_socket_2.attribute_domain = 'POINT'
			
			
			#initialize _mn_utils_int_multiply nodes
			#node Group Output
			group_output = _mn_utils_int_multiply.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Math.001
			math_001 = _mn_utils_int_multiply.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.operation = 'MULTIPLY'
			math_001.use_clamp = False
			
			#node Group Input
			group_input = _mn_utils_int_multiply.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			
			
			
			#Set locations
			group_output.location = (190.0, 0.0)
			math_001.location = (0.0, 0.0)
			group_input.location = (-235.15338134765625, -44.40943145751953)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			
			#initialize _mn_utils_int_multiply links
			#group_input.Value -> math_001.Value
			_mn_utils_int_multiply.links.new(group_input.outputs[0], math_001.inputs[0])
			#group_input.Value -> math_001.Value
			_mn_utils_int_multiply.links.new(group_input.outputs[1], math_001.inputs[1])
			#math_001.Value -> group_output.Value
			_mn_utils_int_multiply.links.new(math_001.outputs[0], group_output.inputs[0])
			return _mn_utils_int_multiply

		_mn_utils_int_multiply = _mn_utils_int_multiply_node_group()

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
			value_socket_3 = mn_units.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket_3.subtype = 'NONE'
			value_socket_3.default_value = 3.0
			value_socket_3.min_value = -10000.0
			value_socket_3.max_value = 10000.0
			value_socket_3.attribute_domain = 'POINT'
			value_socket_3.description = "A value which will be scaled appropriately for the world"
			
			
			#initialize mn_units nodes
			#node Group Output
			group_output_2 = mn_units.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Group Input
			group_input_2 = mn_units.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
			#node Math
			math = mn_units.nodes.new("ShaderNodeMath")
			math.name = "Math"
			math.operation = 'MULTIPLY'
			math.use_clamp = False
			
			#node Math.001
			math_001_1 = mn_units.nodes.new("ShaderNodeMath")
			math_001_1.name = "Math.001"
			math_001_1.operation = 'MULTIPLY'
			math_001_1.use_clamp = False
			#Value_001
			math_001_1.inputs[1].default_value = 10.0
			
			#node Group
			group = mn_units.nodes.new("GeometryNodeGroup")
			group.name = "Group"
			group.node_tree = _mn_world_scale
			
			
			
			
			#Set locations
			group_output_2.location = (190.0, 0.0)
			group_input_2.location = (-240.0, 0.0)
			math.location = (-60.0, 0.0)
			math_001_1.location = (-60.0, -160.0)
			group.location = (-304.00421142578125, -104.114013671875)
			
			#Set dimensions
			group_output_2.width, group_output_2.height = 140.0, 100.0
			group_input_2.width, group_input_2.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			math_001_1.width, math_001_1.height = 140.0, 100.0
			group.width, group.height = 197.58424377441406, 100.0
			
			#initialize mn_units links
			#math.Value -> group_output_2.Angstrom
			mn_units.links.new(math.outputs[0], group_output_2.inputs[0])
			#group_input_2.Value -> math.Value
			mn_units.links.new(group_input_2.outputs[0], math.inputs[0])
			#group.world_scale -> math.Value
			mn_units.links.new(group.outputs[0], math.inputs[1])
			#math.Value -> math_001_1.Value
			mn_units.links.new(math.outputs[0], math_001_1.inputs[0])
			#math_001_1.Value -> group_output_2.Nanometre
			mn_units.links.new(math_001_1.outputs[0], group_output_2.inputs[1])
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
			group_output_3 = _mn_utils_style_sticks.nodes.new("NodeGroupOutput")
			group_output_3.name = "Group Output"
			group_output_3.is_active_output = True
			
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
			group_input_3 = _mn_utils_style_sticks.nodes.new("NodeGroupInput")
			group_input_3.name = "Group Input"
			
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
			group_output_3.location = (620.0, 220.0)
			capture_attribute_001.location = (-920.0, 60.0)
			sample_index_001.location = (-480.0, 180.0)
			evaluate_on_domain_003.location = (-480.0, 140.0)
			named_attribute_002.location = (-660.0, 160.0)
			switch_001.location = (-660.0, 120.0)
			evaluate_on_domain.location = (-480.0, 100.0)
			switch.location = (-300.0, 220.0)
			group_input_005.location = (-480.0, 60.0)
			store_named_attribute.location = (-120.0, 120.0)
			group_input_3.location = (-2680.0, 240.0)
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
			group_output_3.width, group_output_3.height = 140.0, 100.0
			capture_attribute_001.width, capture_attribute_001.height = 140.0, 100.0
			sample_index_001.width, sample_index_001.height = 140.0, 100.0
			evaluate_on_domain_003.width, evaluate_on_domain_003.height = 140.0, 100.0
			named_attribute_002.width, named_attribute_002.height = 140.0, 100.0
			switch_001.width, switch_001.height = 140.0, 100.0
			evaluate_on_domain.width, evaluate_on_domain.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			group_input_005.width, group_input_005.height = 140.0, 100.0
			store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
			group_input_3.width, group_input_3.height = 140.0, 100.0
			separate_geometry.width, separate_geometry.height = 140.0, 100.0
			
			#initialize _mn_utils_style_sticks links
			#capture_attribute.Geometry -> mesh_to_curve.Mesh
			_mn_utils_style_sticks.links.new(capture_attribute.outputs[0], mesh_to_curve.inputs[0])
			#set_shade_smooth.Geometry -> group_output_3.Geometry
			_mn_utils_style_sticks.links.new(set_shade_smooth.outputs[0], group_output_3.inputs[0])
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
			#group_input_3.Atoms -> separate_geometry.Geometry
			_mn_utils_style_sticks.links.new(group_input_3.outputs[0], separate_geometry.inputs[0])
			#separate_geometry.Selection -> capture_attribute_003.Geometry
			_mn_utils_style_sticks.links.new(separate_geometry.outputs[0], capture_attribute_003.inputs[0])
			#group_input_3.Selection -> separate_geometry.Selection
			_mn_utils_style_sticks.links.new(group_input_3.outputs[1], separate_geometry.inputs[1])
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
			group_output_4 = topology_find_bonds.nodes.new("NodeGroupOutput")
			group_output_4.name = "Group Output"
			group_output_4.is_active_output = True
			
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
			math_001_2 = topology_find_bonds.nodes.new("ShaderNodeMath")
			math_001_2.label = "x * 0.62"
			math_001_2.name = "Math.001"
			math_001_2.operation = 'MULTIPLY'
			math_001_2.use_clamp = False
			#Value_001
			math_001_2.inputs[1].default_value = 0.6200000047683716
			
			#node Group Input
			group_input_4 = topology_find_bonds.nodes.new("NodeGroupInput")
			group_input_4.name = "Group Input"
			
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
			math_001_2.parent = frame_003_1
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
			group_output_4.location = (3191.530029296875, 851.8171997070312)
			sample_index_011.location = (2000.0, 1040.0)
			sample_nearest_001.location = (560.0, 740.0)
			set_position_002.location = (2000.0, 820.0)
			store_named_attribute_004.location = (1840.0, 820.0)
			store_named_attribute_006.location = (2160.0, 820.0)
			store_named_attribute_005.location = (1020.0, 820.0)
			sample_index_012.location = (2160.0, 1040.0)
			named_attribute_007.location = (2160.0, 1160.0)
			math_001_2.location = (100.0, 180.0)
			group_input_4.location = (-1840.0, 940.0)
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
			group_output_4.width, group_output_4.height = 140.0, 100.0
			sample_index_011.width, sample_index_011.height = 140.0, 100.0
			sample_nearest_001.width, sample_nearest_001.height = 140.0, 100.0
			set_position_002.width, set_position_002.height = 140.0, 100.0
			store_named_attribute_004.width, store_named_attribute_004.height = 140.0, 100.0
			store_named_attribute_006.width, store_named_attribute_006.height = 140.0, 100.0
			store_named_attribute_005.width, store_named_attribute_005.height = 140.0, 100.0
			sample_index_012.width, sample_index_012.height = 140.0, 100.0
			named_attribute_007.width, named_attribute_007.height = 140.0, 100.0
			math_001_2.width, math_001_2.height = 140.0, 100.0
			group_input_4.width, group_input_4.height = 140.0, 100.0
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
			#group_input_001_1.Scale -> math_001_2.Value
			topology_find_bonds.links.new(group_input_001_1.outputs[2], math_001_2.inputs[0])
			#math_001_2.Value -> math_1.Value
			topology_find_bonds.links.new(math_001_2.outputs[0], math_1.inputs[1])
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
			#group_input_4.Atoms -> separate_geometry_1.Geometry
			topology_find_bonds.links.new(group_input_4.outputs[0], separate_geometry_1.inputs[0])
			#group_input_4.Selection -> separate_geometry_1.Selection
			topology_find_bonds.links.new(group_input_4.outputs[1], separate_geometry_1.inputs[1])
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
			#switch_1.Output -> group_output_4.Atoms
			topology_find_bonds.links.new(switch_1.outputs[0], group_output_4.inputs[0])
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
			group_input_5 = _mn_utils_style_spheres_points.nodes.new("NodeGroupInput")
			group_input_5.name = "Group Input"
			
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
			group_output_5 = _mn_utils_style_spheres_points.nodes.new("NodeGroupOutput")
			group_output_5.name = "Group Output"
			group_output_5.is_active_output = True
			
			#node Set Material
			set_material_1 = _mn_utils_style_spheres_points.nodes.new("GeometryNodeSetMaterial")
			set_material_1.name = "Set Material"
			#Selection
			set_material_1.inputs[1].default_value = True
			
			
			
			
			#Set locations
			group_input_5.location = (-1060.0, 60.0)
			mesh_to_points.location = (-540.0, 220.0)
			switch_2.location = (-900.0, -100.0)
			named_attribute_1.location = (-1080.0, -100.0)
			group_2.location = (-1080.0, -240.0)
			math_2.location = (-720.0, 40.0)
			group_output_5.location = (-220.0, 220.0)
			set_material_1.location = (-380.0, 220.0)
			
			#Set dimensions
			group_input_5.width, group_input_5.height = 140.0, 100.0
			mesh_to_points.width, mesh_to_points.height = 140.0, 100.0
			switch_2.width, switch_2.height = 140.0, 100.0
			named_attribute_1.width, named_attribute_1.height = 140.0, 100.0
			group_2.width, group_2.height = 140.0, 100.0
			math_2.width, math_2.height = 140.0, 100.0
			group_output_5.width, group_output_5.height = 140.0, 100.0
			set_material_1.width, set_material_1.height = 140.0, 100.0
			
			#initialize _mn_utils_style_spheres_points links
			#set_material_1.Geometry -> group_output_5.Point Cloud
			_mn_utils_style_spheres_points.links.new(set_material_1.outputs[0], group_output_5.inputs[0])
			#group_input_5.Selection -> mesh_to_points.Selection
			_mn_utils_style_spheres_points.links.new(group_input_5.outputs[1], mesh_to_points.inputs[1])
			#group_input_5.Radii -> math_2.Value
			_mn_utils_style_spheres_points.links.new(group_input_5.outputs[2], math_2.inputs[0])
			#math_2.Value -> mesh_to_points.Radius
			_mn_utils_style_spheres_points.links.new(math_2.outputs[0], mesh_to_points.inputs[3])
			#group_input_5.Material -> set_material_1.Material
			_mn_utils_style_spheres_points.links.new(group_input_5.outputs[3], set_material_1.inputs[2])
			#named_attribute_1.Attribute -> switch_2.Switch
			_mn_utils_style_spheres_points.links.new(named_attribute_1.outputs[0], switch_2.inputs[0])
			#named_attribute_1.Attribute -> switch_2.True
			_mn_utils_style_spheres_points.links.new(named_attribute_1.outputs[0], switch_2.inputs[2])
			#switch_2.Output -> math_2.Value
			_mn_utils_style_spheres_points.links.new(switch_2.outputs[0], math_2.inputs[1])
			#group_input_5.Atoms -> mesh_to_points.Mesh
			_mn_utils_style_spheres_points.links.new(group_input_5.outputs[0], mesh_to_points.inputs[0])
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
			math_001_3 = _mn_utils_style_spheres_icosphere.nodes.new("ShaderNodeMath")
			math_001_3.name = "Math.001"
			math_001_3.operation = 'MINIMUM'
			math_001_3.use_clamp = False
			
			#node Group Output
			group_output_6 = _mn_utils_style_spheres_icosphere.nodes.new("NodeGroupOutput")
			group_output_6.name = "Group Output"
			group_output_6.is_active_output = True
			
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
			group_input_6 = _mn_utils_style_spheres_icosphere.nodes.new("NodeGroupInput")
			group_input_6.name = "Group Input"
			group_input_6.outputs[2].hide = True
			group_input_6.outputs[3].hide = True
			group_input_6.outputs[4].hide = True
			group_input_6.outputs[5].hide = True
			group_input_6.outputs[6].hide = True
			
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
			math_001_3.location = (-140.0, 60.0)
			group_output_6.location = (835.407470703125, 359.5566711425781)
			group_input_002_1.location = (320.0, 260.0)
			set_shade_smooth_1.location = (500.0, 340.0)
			set_material_2.location = (660.0, 340.0)
			group_input_6.location = (-160.0, 240.0)
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
			math_001_3.width, math_001_3.height = 140.0, 100.0
			group_output_6.width, group_output_6.height = 140.0, 100.0
			group_input_002_1.width, group_input_002_1.height = 140.0, 100.0
			set_shade_smooth_1.width, set_shade_smooth_1.height = 140.0, 100.0
			set_material_2.width, set_material_2.height = 140.0, 100.0
			group_input_6.width, group_input_6.height = 140.0, 100.0
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
			#set_material_2.Geometry -> group_output_6.Instances
			_mn_utils_style_spheres_icosphere.links.new(set_material_2.outputs[0], group_output_6.inputs[0])
			#set_shade_smooth_1.Geometry -> set_material_2.Geometry
			_mn_utils_style_spheres_icosphere.links.new(set_shade_smooth_1.outputs[0], set_material_2.inputs[0])
			#group_input_6.Atoms -> instance_on_points_1.Points
			_mn_utils_style_spheres_icosphere.links.new(group_input_6.outputs[0], instance_on_points_1.inputs[0])
			#reroute_001_1.Output -> instance_on_points_1.Instance
			_mn_utils_style_spheres_icosphere.links.new(reroute_001_1.outputs[0], instance_on_points_1.inputs[2])
			#ico_sphere_005.Mesh -> geometry_to_instance.Geometry
			_mn_utils_style_spheres_icosphere.links.new(ico_sphere_005.outputs[0], geometry_to_instance.inputs[0])
			#math_001_3.Value -> instance_on_points_1.Instance Index
			_mn_utils_style_spheres_icosphere.links.new(math_001_3.outputs[0], instance_on_points_1.inputs[4])
			#group_input_001_2.Subdivisions -> math_001_3.Value
			_mn_utils_style_spheres_icosphere.links.new(group_input_001_2.outputs[3], math_001_3.inputs[0])
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
			#group_input_6.Selection -> instance_on_points_1.Selection
			_mn_utils_style_spheres_icosphere.links.new(group_input_6.outputs[1], instance_on_points_1.inputs[1])
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
			#math_002.Value -> math_001_3.Value
			_mn_utils_style_spheres_icosphere.links.new(math_002.outputs[0], math_001_3.inputs[1])
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
			group_input_7 = style_spheres.nodes.new("NodeGroupInput")
			group_input_7.name = "Group Input"
			
			#node Group Output
			group_output_7 = style_spheres.nodes.new("NodeGroupOutput")
			group_output_7.name = "Group Output"
			group_output_7.is_active_output = True
			
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
			group_input_7.location = (-679.2061157226562, -54.561466217041016)
			group_output_7.location = (480.0, 40.0)
			join_geometry.location = (320.0, 40.0)
			separate_geometry_2.location = (-420.0, 80.0)
			group_014.location = (-200.0, -200.0)
			group_026.location = (-200.0, 60.0)
			realize_instances_1.location = (100.0, 60.0)
			
			#Set dimensions
			group_input_7.width, group_input_7.height = 140.0, 100.0
			group_output_7.width, group_output_7.height = 140.0, 100.0
			join_geometry.width, join_geometry.height = 140.0, 100.0
			separate_geometry_2.width, separate_geometry_2.height = 140.0, 100.0
			group_014.width, group_014.height = 277.9979248046875, 100.0
			group_026.width, group_026.height = 278.0207824707031, 100.0
			realize_instances_1.width, realize_instances_1.height = 140.0, 100.0
			
			#initialize style_spheres links
			#group_input_7.Atoms -> separate_geometry_2.Geometry
			style_spheres.links.new(group_input_7.outputs[0], separate_geometry_2.inputs[0])
			#group_input_7.Selection -> group_014.Selection
			style_spheres.links.new(group_input_7.outputs[1], group_014.inputs[1])
			#group_input_7.Selection -> group_026.Selection
			style_spheres.links.new(group_input_7.outputs[1], group_026.inputs[1])
			#group_input_7.Sphere As Mesh -> separate_geometry_2.Selection
			style_spheres.links.new(group_input_7.outputs[2], separate_geometry_2.inputs[1])
			#group_input_7.Sphere Radii -> group_014.Radii
			style_spheres.links.new(group_input_7.outputs[3], group_014.inputs[2])
			#group_input_7.Sphere Radii -> group_026.Radii
			style_spheres.links.new(group_input_7.outputs[3], group_026.inputs[2])
			#group_input_7.Sphere Subdivisions -> group_026.Subdivisions
			style_spheres.links.new(group_input_7.outputs[4], group_026.inputs[3])
			#group_input_7.Shade Smooth -> group_026.Shade Smooth
			style_spheres.links.new(group_input_7.outputs[5], group_026.inputs[4])
			#group_input_7.Material -> group_014.Material
			style_spheres.links.new(group_input_7.outputs[6], group_014.inputs[3])
			#group_input_7.Material -> group_026.Material
			style_spheres.links.new(group_input_7.outputs[6], group_026.inputs[5])
			#join_geometry.Geometry -> group_output_7.Geometry
			style_spheres.links.new(join_geometry.outputs[0], group_output_7.inputs[0])
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
			group_output_8 = style_ball_and_stick.nodes.new("NodeGroupOutput")
			group_output_8.name = "Group Output"
			group_output_8.is_active_output = True
			
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
			group_input_8 = style_ball_and_stick.nodes.new("NodeGroupInput")
			group_input_8.name = "Group Input"
			group_input_8.outputs[1].hide = True
			group_input_8.outputs[3].hide = True
			group_input_8.outputs[4].hide = True
			group_input_8.outputs[5].hide = True
			group_input_8.outputs[6].hide = True
			group_input_8.outputs[7].hide = True
			group_input_8.outputs[8].hide = True
			group_input_8.outputs[9].hide = True
			group_input_8.outputs[10].hide = True
			
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
			group_output_8.location = (560.0, -140.0)
			join_geometry_001.location = (360.0, -140.0)
			group_input_002_2.location = (-800.0, -520.0)
			separate_geometry_3.location = (-760.0, -20.0)
			group_input_8.location = (-960.0, -20.0)
			group_009.location = (-40.0, -380.0)
			topology_find_bonds_1.location = (-400.0, -300.0)
			separate_geometry_002.location = (-560.0, -380.0)
			join_geometry_002.location = (-200.0, -380.0)
			math_4.location = (-200.0, -500.0)
			group_3.location = (-20.0, 20.0)
			group_input_001_3.location = (-220.0, -100.0)
			
			#Set dimensions
			group_output_8.width, group_output_8.height = 140.0, 100.0
			join_geometry_001.width, join_geometry_001.height = 140.0, 100.0
			group_input_002_2.width, group_input_002_2.height = 140.0, 100.0
			separate_geometry_3.width, separate_geometry_3.height = 140.0, 100.0
			group_input_8.width, group_input_8.height = 140.0, 100.0
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
			#group_input_8.Atoms -> separate_geometry_3.Geometry
			style_ball_and_stick.links.new(group_input_8.outputs[0], separate_geometry_3.inputs[0])
			#group_input_8.Selection -> separate_geometry_3.Selection
			style_ball_and_stick.links.new(group_input_8.outputs[2], separate_geometry_3.inputs[1])
			#group_009.Geometry -> join_geometry_001.Geometry
			style_ball_and_stick.links.new(group_009.outputs[0], join_geometry_001.inputs[0])
			#join_geometry_001.Geometry -> group_output_8.Geometry
			style_ball_and_stick.links.new(join_geometry_001.outputs[0], group_output_8.inputs[0])
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
			group_input_9 = _mn_constants_atom_name_peptide.nodes.new("NodeGroupInput")
			group_input_9.name = "Group Input"
			
			#node Group Output
			group_output_9 = _mn_constants_atom_name_peptide.nodes.new("NodeGroupOutput")
			group_output_9.name = "Group Output"
			group_output_9.is_active_output = True
			
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
			group_input_9.location = (-200.0, 0.0)
			group_output_9.location = (260.0, 180.0)
			integer_001.location = (0.0, -50.0)
			integer_004.location = (0.0, -140.0)
			integer_1.location = (0.0, 40.0)
			integer_003.location = (0.0, 240.0)
			integer_002.location = (0.0, 140.0)
			
			#Set dimensions
			group_input_9.width, group_input_9.height = 140.0, 100.0
			group_output_9.width, group_output_9.height = 140.0, 100.0
			integer_001.width, integer_001.height = 140.0, 100.0
			integer_004.width, integer_004.height = 140.0, 100.0
			integer_1.width, integer_1.height = 140.0, 100.0
			integer_003.width, integer_003.height = 140.0, 100.0
			integer_002.width, integer_002.height = 140.0, 100.0
			
			#initialize _mn_constants_atom_name_peptide links
			#integer_003.Integer -> group_output_9.Backbone Lower
			_mn_constants_atom_name_peptide.links.new(integer_003.outputs[0], group_output_9.inputs[0])
			#integer_002.Integer -> group_output_9.Backbone Upper
			_mn_constants_atom_name_peptide.links.new(integer_002.outputs[0], group_output_9.inputs[1])
			#integer_1.Integer -> group_output_9.Side Chain Lower
			_mn_constants_atom_name_peptide.links.new(integer_1.outputs[0], group_output_9.inputs[2])
			#integer_001.Integer -> group_output_9.Side Chain Upper
			_mn_constants_atom_name_peptide.links.new(integer_001.outputs[0], group_output_9.inputs[3])
			#integer_004.Integer -> group_output_9.Alpha Carbon
			_mn_constants_atom_name_peptide.links.new(integer_004.outputs[0], group_output_9.inputs[4])
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
			group_input_10 = _mn_select_peptide.nodes.new("NodeGroupInput")
			group_input_10.name = "Group Input"
			
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
			group_output_10 = _mn_select_peptide.nodes.new("NodeGroupOutput")
			group_output_10.name = "Group Output"
			group_output_10.is_active_output = True
			
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
			group_input_10.location = (-460.0, 0.0)
			compare_1.location = (80.0, 80.0)
			compare_001.location = (80.0, -80.0)
			boolean_math_001.location = (260.0, 80.0)
			compare_002.location = (80.0, -240.0)
			compare_003.location = (80.0, -400.0)
			boolean_math_002.location = (260.0, -240.0)
			compare_004.location = (80.0, -560.0)
			named_attribute_3.location = (-360.0, -480.0)
			boolean_math_003.location = (260.0, -560.0)
			group_output_10.location = (666.1161499023438, -263.7054748535156)
			compare_005.location = (80.0, -720.0)
			compare_006.location = (260.0, -380.0)
			group_4.location = (-411.24090576171875, -312.71807861328125)
			boolean_math.location = (420.0, -240.0)
			
			#Set dimensions
			group_input_10.width, group_input_10.height = 140.0, 100.0
			compare_1.width, compare_1.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
			compare_002.width, compare_002.height = 153.86517333984375, 100.0
			compare_003.width, compare_003.height = 153.86517333984375, 100.0
			boolean_math_002.width, boolean_math_002.height = 140.0, 100.0
			compare_004.width, compare_004.height = 140.0, 100.0
			named_attribute_3.width, named_attribute_3.height = 140.0, 100.0
			boolean_math_003.width, boolean_math_003.height = 140.0, 100.0
			group_output_10.width, group_output_10.height = 140.0, 100.0
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
			#boolean_math_001.Boolean -> group_output_10.Is Backbone
			_mn_select_peptide.links.new(boolean_math_001.outputs[0], group_output_10.inputs[0])
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
			#boolean_math_003.Boolean -> group_output_10.Is Peptide
			_mn_select_peptide.links.new(boolean_math_003.outputs[0], group_output_10.inputs[2])
			#named_attribute_3.Attribute -> compare_006.A
			_mn_select_peptide.links.new(named_attribute_3.outputs[0], compare_006.inputs[2])
			#group_4.Alpha Carbon -> compare_006.B
			_mn_select_peptide.links.new(group_4.outputs[4], compare_006.inputs[3])
			#compare_006.Result -> group_output_10.Is Alpha Carbon
			_mn_select_peptide.links.new(compare_006.outputs[0], group_output_10.inputs[3])
			#boolean_math_002.Boolean -> boolean_math.Boolean
			_mn_select_peptide.links.new(boolean_math_002.outputs[0], boolean_math.inputs[0])
			#compare_006.Result -> boolean_math.Boolean
			_mn_select_peptide.links.new(compare_006.outputs[0], boolean_math.inputs[1])
			#boolean_math.Boolean -> group_output_10.Is Side Chain
			_mn_select_peptide.links.new(boolean_math.outputs[0], group_output_10.inputs[1])
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
			group_output_11 = fallback_boolean.nodes.new("NodeGroupOutput")
			group_output_11.name = "Group Output"
			group_output_11.is_active_output = True
			
			#node Group Input
			group_input_11 = fallback_boolean.nodes.new("NodeGroupInput")
			group_input_11.name = "Group Input"
			
			#node Named Attribute
			named_attribute_4 = fallback_boolean.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_4.name = "Named Attribute"
			named_attribute_4.data_type = 'BOOLEAN'
			
			#node Switch
			switch_3 = fallback_boolean.nodes.new("GeometryNodeSwitch")
			switch_3.name = "Switch"
			switch_3.input_type = 'BOOLEAN'
			
			
			
			
			#Set locations
			group_output_11.location = (276.6171569824219, 4.738137245178223)
			group_input_11.location = (-280.0, 0.0)
			named_attribute_4.location = (-94.73597717285156, 4.738137245178223)
			switch_3.location = (86.61715698242188, 4.738137245178223)
			
			#Set dimensions
			group_output_11.width, group_output_11.height = 140.0, 100.0
			group_input_11.width, group_input_11.height = 140.0, 100.0
			named_attribute_4.width, named_attribute_4.height = 140.0, 100.0
			switch_3.width, switch_3.height = 140.0, 100.0
			
			#initialize fallback_boolean links
			#named_attribute_4.Exists -> switch_3.Switch
			fallback_boolean.links.new(named_attribute_4.outputs[1], switch_3.inputs[0])
			#named_attribute_4.Attribute -> switch_3.True
			fallback_boolean.links.new(named_attribute_4.outputs[0], switch_3.inputs[2])
			#group_input_11.Fallback -> switch_3.False
			fallback_boolean.links.new(group_input_11.outputs[1], switch_3.inputs[1])
			#switch_3.Output -> group_output_11.Boolean
			fallback_boolean.links.new(switch_3.outputs[0], group_output_11.inputs[0])
			#group_input_11.Name -> named_attribute_4.Name
			fallback_boolean.links.new(group_input_11.outputs[0], named_attribute_4.inputs[0])
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
			group_input_12 = is_peptide.nodes.new("NodeGroupInput")
			group_input_12.name = "Group Input"
			
			#node Boolean Math.001
			boolean_math_001_1 = is_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_1.name = "Boolean Math.001"
			boolean_math_001_1.operation = 'AND'
			
			#node Group
			group_5 = is_peptide.nodes.new("GeometryNodeGroup")
			group_5.name = "Group"
			group_5.node_tree = _mn_select_peptide
			
			#node Group Output
			group_output_12 = is_peptide.nodes.new("NodeGroupOutput")
			group_output_12.name = "Group Output"
			group_output_12.is_active_output = True
			
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
			group_input_12.location = (-200.0, 0.0)
			boolean_math_001_1.location = (-40.0, 0.0)
			group_5.location = (-340.0, -140.0)
			group_output_12.location = (320.0, 0.0)
			group_001.location = (-40.0, -140.0)
			boolean_math_002_1.location = (140.0, 5.243539333343506)
			boolean_math_1.location = (140.0, -120.0)
			
			#Set dimensions
			group_input_12.width, group_input_12.height = 140.0, 100.0
			boolean_math_001_1.width, boolean_math_001_1.height = 140.0, 100.0
			group_5.width, group_5.height = 247.90924072265625, 100.0
			group_output_12.width, group_output_12.height = 140.0, 100.0
			group_001.width, group_001.height = 140.0, 100.0
			boolean_math_002_1.width, boolean_math_002_1.height = 140.0, 100.0
			boolean_math_1.width, boolean_math_1.height = 140.0, 100.0
			
			#initialize is_peptide links
			#boolean_math_002_1.Boolean -> group_output_12.Selection
			is_peptide.links.new(boolean_math_002_1.outputs[0], group_output_12.inputs[0])
			#group_input_12.And -> boolean_math_001_1.Boolean
			is_peptide.links.new(group_input_12.outputs[0], boolean_math_001_1.inputs[0])
			#group_5.Is Peptide -> group_001.Fallback
			is_peptide.links.new(group_5.outputs[2], group_001.inputs[1])
			#group_001.Boolean -> boolean_math_001_1.Boolean
			is_peptide.links.new(group_001.outputs[0], boolean_math_001_1.inputs[1])
			#boolean_math_001_1.Boolean -> boolean_math_002_1.Boolean
			is_peptide.links.new(boolean_math_001_1.outputs[0], boolean_math_002_1.inputs[0])
			#group_input_12.Or -> boolean_math_002_1.Boolean
			is_peptide.links.new(group_input_12.outputs[1], boolean_math_002_1.inputs[1])
			#boolean_math_002_1.Boolean -> boolean_math_1.Boolean
			is_peptide.links.new(boolean_math_002_1.outputs[0], boolean_math_1.inputs[0])
			#boolean_math_1.Boolean -> group_output_12.Inverted
			is_peptide.links.new(boolean_math_1.outputs[0], group_output_12.inputs[1])
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
			group_output_13 = _mn_constants_atom_name_nucleic.nodes.new("NodeGroupOutput")
			group_output_13.name = "Group Output"
			group_output_13.is_active_output = True
			
			#node Group Input
			group_input_13 = _mn_constants_atom_name_nucleic.nodes.new("NodeGroupInput")
			group_input_13.name = "Group Input"
			
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
			group_output_13.location = (190.0, 0.0)
			group_input_13.location = (-200.0, 0.0)
			integer_2.location = (0.0, -100.0)
			integer_002_1.location = (0.0, 100.0)
			integer_003_1.location = (0.0, 0.0)
			integer_001_1.location = (0.0, -200.0)
			integer_004_1.location = (0.0, -300.0)
			
			#Set dimensions
			group_output_13.width, group_output_13.height = 140.0, 100.0
			group_input_13.width, group_input_13.height = 140.0, 100.0
			integer_2.width, integer_2.height = 140.0, 100.0
			integer_002_1.width, integer_002_1.height = 140.0, 100.0
			integer_003_1.width, integer_003_1.height = 140.0, 100.0
			integer_001_1.width, integer_001_1.height = 140.0, 100.0
			integer_004_1.width, integer_004_1.height = 140.0, 100.0
			
			#initialize _mn_constants_atom_name_nucleic links
			#integer_2.Integer -> group_output_13.Side Chain Lower
			_mn_constants_atom_name_nucleic.links.new(integer_2.outputs[0], group_output_13.inputs[2])
			#integer_001_1.Integer -> group_output_13.Side Chain Upper
			_mn_constants_atom_name_nucleic.links.new(integer_001_1.outputs[0], group_output_13.inputs[3])
			#integer_002_1.Integer -> group_output_13.Backbone Lower
			_mn_constants_atom_name_nucleic.links.new(integer_002_1.outputs[0], group_output_13.inputs[0])
			#integer_003_1.Integer -> group_output_13.Backbone Upper
			_mn_constants_atom_name_nucleic.links.new(integer_003_1.outputs[0], group_output_13.inputs[1])
			#integer_004_1.Integer -> group_output_13.Side Chain Joint Carbon
			_mn_constants_atom_name_nucleic.links.new(integer_004_1.outputs[0], group_output_13.inputs[4])
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
			group_input_14 = _mn_select_nucleic.nodes.new("NodeGroupInput")
			group_input_14.name = "Group Input"
			
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
			group_output_14 = _mn_select_nucleic.nodes.new("NodeGroupOutput")
			group_output_14.name = "Group Output"
			group_output_14.is_active_output = True
			
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
			group_input_14.location = (-460.0, 0.0)
			compare_2.location = (80.0, 80.0)
			compare_001_1.location = (80.0, -80.0)
			boolean_math_001_2.location = (260.0, 80.0)
			group_output_14.location = (580.0, 60.0)
			compare_002_1.location = (80.0, -260.0)
			compare_003_1.location = (80.0, -420.0)
			boolean_math_002_2.location = (260.0, -260.0)
			compare_004_1.location = (80.0, -580.0)
			compare_005_1.location = (80.0, -740.0)
			boolean_math_003_1.location = (260.0, -580.0)
			named_attribute_5.location = (-260.0, -280.0)
			group_6.location = (-480.0, -100.0)
			
			#Set dimensions
			group_input_14.width, group_input_14.height = 140.0, 100.0
			compare_2.width, compare_2.height = 140.0, 100.0
			compare_001_1.width, compare_001_1.height = 140.0, 100.0
			boolean_math_001_2.width, boolean_math_001_2.height = 140.0, 100.0
			group_output_14.width, group_output_14.height = 140.0, 100.0
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
			#boolean_math_001_2.Boolean -> group_output_14.Is Backbone
			_mn_select_nucleic.links.new(boolean_math_001_2.outputs[0], group_output_14.inputs[0])
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
			#boolean_math_002_2.Boolean -> group_output_14.Is Side Chain
			_mn_select_nucleic.links.new(boolean_math_002_2.outputs[0], group_output_14.inputs[1])
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
			#boolean_math_003_1.Boolean -> group_output_14.Is Nucleic
			_mn_select_nucleic.links.new(boolean_math_003_1.outputs[0], group_output_14.inputs[2])
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
			group_input_15 = is_nucleic.nodes.new("NodeGroupInput")
			group_input_15.name = "Group Input"
			
			#node Boolean Math.001
			boolean_math_001_3 = is_nucleic.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_3.name = "Boolean Math.001"
			boolean_math_001_3.operation = 'AND'
			
			#node Group Output
			group_output_15 = is_nucleic.nodes.new("NodeGroupOutput")
			group_output_15.name = "Group Output"
			group_output_15.is_active_output = True
			
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
			group_input_15.location = (-280.0, -40.0)
			boolean_math_001_3.location = (-40.0, 0.0)
			group_output_15.location = (320.0000305175781, 0.0)
			group_7.location = (-620.0, -160.0)
			group_001_1.location = (-340.0, -160.0)
			boolean_math_002_3.location = (140.0, 0.0)
			boolean_math_2.location = (140.0, -140.0)
			
			#Set dimensions
			group_input_15.width, group_input_15.height = 140.0, 100.0
			boolean_math_001_3.width, boolean_math_001_3.height = 140.0, 100.0
			group_output_15.width, group_output_15.height = 140.0, 100.0
			group_7.width, group_7.height = 247.90924072265625, 100.0
			group_001_1.width, group_001_1.height = 232.0133056640625, 100.0
			boolean_math_002_3.width, boolean_math_002_3.height = 140.0, 100.0
			boolean_math_2.width, boolean_math_2.height = 140.0, 100.0
			
			#initialize is_nucleic links
			#boolean_math_002_3.Boolean -> group_output_15.Selection
			is_nucleic.links.new(boolean_math_002_3.outputs[0], group_output_15.inputs[0])
			#group_input_15.And -> boolean_math_001_3.Boolean
			is_nucleic.links.new(group_input_15.outputs[0], boolean_math_001_3.inputs[0])
			#group_7.Is Nucleic -> group_001_1.Fallback
			is_nucleic.links.new(group_7.outputs[2], group_001_1.inputs[1])
			#group_001_1.Boolean -> boolean_math_001_3.Boolean
			is_nucleic.links.new(group_001_1.outputs[0], boolean_math_001_3.inputs[1])
			#boolean_math_001_3.Boolean -> boolean_math_002_3.Boolean
			is_nucleic.links.new(boolean_math_001_3.outputs[0], boolean_math_002_3.inputs[0])
			#group_input_15.Or -> boolean_math_002_3.Boolean
			is_nucleic.links.new(group_input_15.outputs[1], boolean_math_002_3.inputs[1])
			#boolean_math_002_3.Boolean -> boolean_math_2.Boolean
			is_nucleic.links.new(boolean_math_002_3.outputs[0], boolean_math_2.inputs[0])
			#boolean_math_2.Boolean -> group_output_15.Inverted
			is_nucleic.links.new(boolean_math_2.outputs[0], group_output_15.inputs[1])
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
			group_input_16 = separate_polymers.nodes.new("NodeGroupInput")
			group_input_16.name = "Group Input"
			
			#node Group Output
			group_output_16 = separate_polymers.nodes.new("NodeGroupOutput")
			group_output_16.name = "Group Output"
			group_output_16.is_active_output = True
			
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
			group_input_16.location = (-360.0, 220.0)
			group_output_16.location = (260.0, 80.0)
			separate_geometry_4.location = (-200.0, 100.0)
			separate_geometry_001.location = (0.0, -40.0)
			group_8.location = (-200.0, -60.0)
			group_001_2.location = (0.0, -200.0)
			
			#Set dimensions
			group_input_16.width, group_input_16.height = 140.0, 100.0
			group_output_16.width, group_output_16.height = 140.0, 100.0
			separate_geometry_4.width, separate_geometry_4.height = 140.0, 100.0
			separate_geometry_001.width, separate_geometry_001.height = 140.0, 100.0
			group_8.width, group_8.height = 140.0, 100.0
			group_001_2.width, group_001_2.height = 140.0, 100.0
			
			#initialize separate_polymers links
			#group_input_16.Atoms -> separate_geometry_4.Geometry
			separate_polymers.links.new(group_input_16.outputs[0], separate_geometry_4.inputs[0])
			#separate_geometry_4.Inverted -> separate_geometry_001.Geometry
			separate_polymers.links.new(separate_geometry_4.outputs[1], separate_geometry_001.inputs[0])
			#separate_geometry_4.Selection -> group_output_16.Peptide
			separate_polymers.links.new(separate_geometry_4.outputs[0], group_output_16.inputs[0])
			#separate_geometry_001.Selection -> group_output_16.Nucleic
			separate_polymers.links.new(separate_geometry_001.outputs[0], group_output_16.inputs[1])
			#separate_geometry_001.Inverted -> group_output_16.Other
			separate_polymers.links.new(separate_geometry_001.outputs[1], group_output_16.inputs[2])
			#group_8.Selection -> separate_geometry_4.Selection
			separate_polymers.links.new(group_8.outputs[0], separate_geometry_4.inputs[1])
			#group_001_2.Selection -> separate_geometry_001.Selection
			separate_polymers.links.new(group_001_2.outputs[0], separate_geometry_001.inputs[1])
			return separate_polymers

		separate_polymers = separate_polymers_node_group()

		#initialize select_res_whole node group
		def select_res_whole_node_group():
			select_res_whole = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Select Res Whole")

			select_res_whole.color_tag = 'INPUT'
			select_res_whole.description = ""

			
			#select_res_whole interface
			#Socket Selection
			selection_socket_8 = select_res_whole.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket_8.attribute_domain = 'POINT'
			selection_socket_8.description = "The calculated selection"
			
			#Socket Selection
			selection_socket_9 = select_res_whole.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_9.attribute_domain = 'POINT'
			selection_socket_9.hide_value = True
			selection_socket_9.description = "Selection of atoms to apply this node to"
			
			#Socket Expand
			expand_socket = select_res_whole.interface.new_socket(name = "Expand", in_out='INPUT', socket_type = 'NodeSocketBool')
			expand_socket.attribute_domain = 'POINT'
			expand_socket.description = "Whether to expand the selection to the whole residue if at least one atom is selected"
			
			
			#initialize select_res_whole nodes
			#node Accumulate Field
			accumulate_field = select_res_whole.nodes.new("GeometryNodeAccumulateField")
			accumulate_field.name = "Accumulate Field"
			accumulate_field.data_type = 'INT'
			accumulate_field.domain = 'POINT'
			
			#node Compare.001
			compare_001_2 = select_res_whole.nodes.new("FunctionNodeCompare")
			compare_001_2.name = "Compare.001"
			compare_001_2.data_type = 'INT'
			compare_001_2.mode = 'ELEMENT'
			compare_001_2.operation = 'GREATER_THAN'
			#B_INT
			compare_001_2.inputs[3].default_value = 0
			
			#node Group Output
			group_output_17 = select_res_whole.nodes.new("NodeGroupOutput")
			group_output_17.name = "Group Output"
			group_output_17.is_active_output = True
			
			#node Named Attribute.001
			named_attribute_001_1 = select_res_whole.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001_1.name = "Named Attribute.001"
			named_attribute_001_1.data_type = 'INT'
			#Name
			named_attribute_001_1.inputs[0].default_value = "res_id"
			
			#node Index
			index_1 = select_res_whole.nodes.new("GeometryNodeInputIndex")
			index_1.name = "Index"
			
			#node Math
			math_5 = select_res_whole.nodes.new("ShaderNodeMath")
			math_5.label = "x + 1"
			math_5.name = "Math"
			math_5.hide = True
			math_5.operation = 'ADD'
			math_5.use_clamp = False
			#Value_001
			math_5.inputs[1].default_value = 1.0
			
			#node Field at Index
			field_at_index = select_res_whole.nodes.new("GeometryNodeFieldAtIndex")
			field_at_index.name = "Field at Index"
			field_at_index.data_type = 'INT'
			field_at_index.domain = 'POINT'
			
			#node Compare
			compare_3 = select_res_whole.nodes.new("FunctionNodeCompare")
			compare_3.name = "Compare"
			compare_3.data_type = 'INT'
			compare_3.mode = 'ELEMENT'
			compare_3.operation = 'NOT_EQUAL'
			
			#node Accumulate Field.001
			accumulate_field_001_1 = select_res_whole.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_001_1.name = "Accumulate Field.001"
			accumulate_field_001_1.data_type = 'INT'
			accumulate_field_001_1.domain = 'POINT'
			#Group Index
			accumulate_field_001_1.inputs[1].default_value = 0
			
			#node Group Input
			group_input_17 = select_res_whole.nodes.new("NodeGroupInput")
			group_input_17.name = "Group Input"
			
			#node Switch
			switch_4 = select_res_whole.nodes.new("GeometryNodeSwitch")
			switch_4.name = "Switch"
			switch_4.input_type = 'BOOLEAN'
			
			
			
			
			#Set locations
			accumulate_field.location = (0.0, 80.0)
			compare_001_2.location = (160.0, 80.0)
			group_output_17.location = (480.0, 180.0)
			named_attribute_001_1.location = (-520.0, -100.0)
			index_1.location = (-700.0, -280.0)
			math_5.location = (-700.0, -340.0)
			field_at_index.location = (-520.0, -240.0)
			compare_3.location = (-360.0, -240.0)
			accumulate_field_001_1.location = (-200.0, -200.0)
			group_input_17.location = (-280.0, 160.0)
			switch_4.location = (160.0, 240.0)
			
			#Set dimensions
			accumulate_field.width, accumulate_field.height = 140.0, 100.0
			compare_001_2.width, compare_001_2.height = 140.0, 100.0
			group_output_17.width, group_output_17.height = 140.0, 100.0
			named_attribute_001_1.width, named_attribute_001_1.height = 140.0, 100.0
			index_1.width, index_1.height = 140.0, 100.0
			math_5.width, math_5.height = 140.0, 100.0
			field_at_index.width, field_at_index.height = 140.0, 100.0
			compare_3.width, compare_3.height = 140.0, 100.0
			accumulate_field_001_1.width, accumulate_field_001_1.height = 140.0, 100.0
			group_input_17.width, group_input_17.height = 140.0, 100.0
			switch_4.width, switch_4.height = 140.0, 100.0
			
			#initialize select_res_whole links
			#group_input_17.Selection -> accumulate_field.Value
			select_res_whole.links.new(group_input_17.outputs[0], accumulate_field.inputs[0])
			#accumulate_field.Total -> compare_001_2.A
			select_res_whole.links.new(accumulate_field.outputs[2], compare_001_2.inputs[2])
			#named_attribute_001_1.Attribute -> field_at_index.Value
			select_res_whole.links.new(named_attribute_001_1.outputs[0], field_at_index.inputs[1])
			#index_1.Index -> math_5.Value
			select_res_whole.links.new(index_1.outputs[0], math_5.inputs[0])
			#math_5.Value -> field_at_index.Index
			select_res_whole.links.new(math_5.outputs[0], field_at_index.inputs[0])
			#named_attribute_001_1.Attribute -> compare_3.A
			select_res_whole.links.new(named_attribute_001_1.outputs[0], compare_3.inputs[2])
			#field_at_index.Value -> compare_3.B
			select_res_whole.links.new(field_at_index.outputs[0], compare_3.inputs[3])
			#compare_3.Result -> accumulate_field_001_1.Value
			select_res_whole.links.new(compare_3.outputs[0], accumulate_field_001_1.inputs[0])
			#accumulate_field_001_1.Trailing -> accumulate_field.Group ID
			select_res_whole.links.new(accumulate_field_001_1.outputs[1], accumulate_field.inputs[1])
			#group_input_17.Selection -> switch_4.False
			select_res_whole.links.new(group_input_17.outputs[0], switch_4.inputs[1])
			#compare_001_2.Result -> switch_4.True
			select_res_whole.links.new(compare_001_2.outputs[0], switch_4.inputs[2])
			#switch_4.Output -> group_output_17.Selection
			select_res_whole.links.new(switch_4.outputs[0], group_output_17.inputs[0])
			#group_input_17.Expand -> switch_4.Switch
			select_res_whole.links.new(group_input_17.outputs[1], switch_4.inputs[0])
			return select_res_whole

		select_res_whole = select_res_whole_node_group()

		#initialize select_proximity node group
		def select_proximity_node_group():
			select_proximity = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Select Proximity")

			select_proximity.color_tag = 'INPUT'
			select_proximity.description = ""

			
			#select_proximity interface
			#Socket Selection
			selection_socket_10 = select_proximity.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket_10.attribute_domain = 'POINT'
			selection_socket_10.description = "The calculated selection"
			
			#Socket Inverted
			inverted_socket_2 = select_proximity.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket_2.attribute_domain = 'POINT'
			inverted_socket_2.description = "The inverse of the calculated selection"
			
			#Socket Target Atoms
			target_atoms_socket = select_proximity.interface.new_socket(name = "Target Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			target_atoms_socket.attribute_domain = 'POINT'
			target_atoms_socket.description = "The atoms to measure the distance from."
			
			#Socket Subset
			subset_socket = select_proximity.interface.new_socket(name = "Subset", in_out='INPUT', socket_type = 'NodeSocketBool')
			subset_socket.attribute_domain = 'POINT'
			subset_socket.hide_value = True
			subset_socket.description = "Subset of input atoms to use for proximity calculation"
			
			#Socket Expand
			expand_socket_1 = select_proximity.interface.new_socket(name = "Expand", in_out='INPUT', socket_type = 'NodeSocketBool')
			expand_socket_1.attribute_domain = 'POINT'
			expand_socket_1.description = "Whether to expand selection to entire residue if single atom is selected"
			
			#Socket Distance (A)
			distance__a__socket = select_proximity.interface.new_socket(name = "Distance (A)", in_out='INPUT', socket_type = 'NodeSocketFloat')
			distance__a__socket.subtype = 'NONE'
			distance__a__socket.default_value = 5.0
			distance__a__socket.min_value = 0.0
			distance__a__socket.max_value = 10000.0
			distance__a__socket.attribute_domain = 'POINT'
			distance__a__socket.description = "Cutoff distance for the selection in Angstroms"
			
			
			#initialize select_proximity nodes
			#node Geometry Proximity
			geometry_proximity = select_proximity.nodes.new("GeometryNodeProximity")
			geometry_proximity.name = "Geometry Proximity"
			geometry_proximity.target_element = 'POINTS'
			#Group ID
			geometry_proximity.inputs[1].default_value = 0
			#Source Position
			geometry_proximity.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Sample Group ID
			geometry_proximity.inputs[3].default_value = 0
			
			#node Group.068
			group_068 = select_proximity.nodes.new("GeometryNodeGroup")
			group_068.name = "Group.068"
			group_068.node_tree = mn_units
			
			#node Group Output
			group_output_18 = select_proximity.nodes.new("NodeGroupOutput")
			group_output_18.name = "Group Output"
			group_output_18.is_active_output = True
			
			#node Boolean Math
			boolean_math_3 = select_proximity.nodes.new("FunctionNodeBooleanMath")
			boolean_math_3.name = "Boolean Math"
			boolean_math_3.operation = 'NOT'
			
			#node Reroute
			reroute_2 = select_proximity.nodes.new("NodeReroute")
			reroute_2.name = "Reroute"
			#node Compare
			compare_4 = select_proximity.nodes.new("FunctionNodeCompare")
			compare_4.name = "Compare"
			compare_4.data_type = 'FLOAT'
			compare_4.mode = 'ELEMENT'
			compare_4.operation = 'LESS_THAN'
			
			#node Group
			group_9 = select_proximity.nodes.new("GeometryNodeGroup")
			group_9.name = "Group"
			group_9.node_tree = select_res_whole
			
			#node Group Input
			group_input_18 = select_proximity.nodes.new("NodeGroupInput")
			group_input_18.name = "Group Input"
			
			#node Separate Geometry
			separate_geometry_5 = select_proximity.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_5.name = "Separate Geometry"
			separate_geometry_5.domain = 'POINT'
			
			#node Boolean Math.002
			boolean_math_002_4 = select_proximity.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_4.name = "Boolean Math.002"
			boolean_math_002_4.operation = 'NIMPLY'
			
			#node Accumulate Field
			accumulate_field_1 = select_proximity.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_1.name = "Accumulate Field"
			accumulate_field_1.data_type = 'INT'
			accumulate_field_1.domain = 'POINT'
			#Group Index
			accumulate_field_1.inputs[1].default_value = 0
			
			#node Boolean Math.004
			boolean_math_004 = select_proximity.nodes.new("FunctionNodeBooleanMath")
			boolean_math_004.name = "Boolean Math.004"
			boolean_math_004.operation = 'NOT'
			
			#node Switch
			switch_5 = select_proximity.nodes.new("GeometryNodeSwitch")
			switch_5.name = "Switch"
			switch_5.input_type = 'BOOLEAN'
			#False
			switch_5.inputs[1].default_value = False
			
			
			
			
			#Set locations
			geometry_proximity.location = (-298.0000915527344, 80.0)
			group_068.location = (-300.0, -160.0)
			group_output_18.location = (840.0, 160.0)
			boolean_math_3.location = (600.0, 100.0)
			reroute_2.location = (560.0, 120.0)
			compare_4.location = (-140.0, 80.0)
			group_9.location = (200.0, 80.0)
			group_input_18.location = (-738.4535522460938, -21.88127326965332)
			separate_geometry_5.location = (-506.0091857910156, 87.78723907470703)
			boolean_math_002_4.location = (20.0, 80.0)
			accumulate_field_1.location = (-340.0, 320.0)
			boolean_math_004.location = (-500.0, 320.0)
			switch_5.location = (-140.0, 260.0)
			
			#Set dimensions
			geometry_proximity.width, geometry_proximity.height = 140.0, 100.0
			group_068.width, group_068.height = 140.0, 100.0
			group_output_18.width, group_output_18.height = 140.0, 100.0
			boolean_math_3.width, boolean_math_3.height = 140.0, 100.0
			reroute_2.width, reroute_2.height = 16.0, 100.0
			compare_4.width, compare_4.height = 140.0, 100.0
			group_9.width, group_9.height = 140.0, 100.0
			group_input_18.width, group_input_18.height = 140.0, 100.0
			separate_geometry_5.width, separate_geometry_5.height = 140.0, 100.0
			boolean_math_002_4.width, boolean_math_002_4.height = 140.0, 100.0
			accumulate_field_1.width, accumulate_field_1.height = 140.0, 100.0
			boolean_math_004.width, boolean_math_004.height = 140.0, 100.0
			switch_5.width, switch_5.height = 140.0, 100.0
			
			#initialize select_proximity links
			#geometry_proximity.Distance -> compare_4.A
			select_proximity.links.new(geometry_proximity.outputs[1], compare_4.inputs[0])
			#group_068.Angstrom -> compare_4.B
			select_proximity.links.new(group_068.outputs[0], compare_4.inputs[1])
			#separate_geometry_5.Selection -> geometry_proximity.Geometry
			select_proximity.links.new(separate_geometry_5.outputs[0], geometry_proximity.inputs[0])
			#group_input_18.Distance (A) -> group_068.Value
			select_proximity.links.new(group_input_18.outputs[3], group_068.inputs[0])
			#reroute_2.Output -> group_output_18.Selection
			select_proximity.links.new(reroute_2.outputs[0], group_output_18.inputs[0])
			#reroute_2.Output -> boolean_math_3.Boolean
			select_proximity.links.new(reroute_2.outputs[0], boolean_math_3.inputs[0])
			#boolean_math_3.Boolean -> group_output_18.Inverted
			select_proximity.links.new(boolean_math_3.outputs[0], group_output_18.inputs[1])
			#group_9.Selection -> reroute_2.Input
			select_proximity.links.new(group_9.outputs[0], reroute_2.inputs[0])
			#group_input_18.Target Atoms -> separate_geometry_5.Geometry
			select_proximity.links.new(group_input_18.outputs[0], separate_geometry_5.inputs[0])
			#group_input_18.Subset -> separate_geometry_5.Selection
			select_proximity.links.new(group_input_18.outputs[1], separate_geometry_5.inputs[1])
			#compare_4.Result -> boolean_math_002_4.Boolean
			select_proximity.links.new(compare_4.outputs[0], boolean_math_002_4.inputs[0])
			#group_input_18.Expand -> group_9.Expand
			select_proximity.links.new(group_input_18.outputs[2], group_9.inputs[1])
			#boolean_math_002_4.Boolean -> group_9.Selection
			select_proximity.links.new(boolean_math_002_4.outputs[0], group_9.inputs[0])
			#group_input_18.Subset -> boolean_math_004.Boolean
			select_proximity.links.new(group_input_18.outputs[1], boolean_math_004.inputs[0])
			#boolean_math_004.Boolean -> accumulate_field_1.Value
			select_proximity.links.new(boolean_math_004.outputs[0], accumulate_field_1.inputs[0])
			#accumulate_field_1.Total -> switch_5.Switch
			select_proximity.links.new(accumulate_field_1.outputs[2], switch_5.inputs[0])
			#group_input_18.Subset -> switch_5.True
			select_proximity.links.new(group_input_18.outputs[1], switch_5.inputs[2])
			#switch_5.Output -> boolean_math_002_4.Boolean
			select_proximity.links.new(switch_5.outputs[0], boolean_math_002_4.inputs[1])
			return select_proximity

		select_proximity = select_proximity_node_group()

		#initialize select_atomic_number node group
		def select_atomic_number_node_group():
			select_atomic_number = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Select Atomic Number")

			select_atomic_number.color_tag = 'INPUT'
			select_atomic_number.description = ""

			
			#select_atomic_number interface
			#Socket Selection
			selection_socket_11 = select_atomic_number.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket_11.attribute_domain = 'POINT'
			selection_socket_11.description = "The calculated selection"
			
			#Socket Inverted
			inverted_socket_3 = select_atomic_number.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket_3.attribute_domain = 'POINT'
			inverted_socket_3.description = "The inverse of the calculated selection"
			
			#Socket And
			and_socket_2 = select_atomic_number.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket_2.attribute_domain = 'POINT'
			and_socket_2.hide_value = True
			
			#Socket Or
			or_socket_2 = select_atomic_number.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket_2.attribute_domain = 'POINT'
			or_socket_2.hide_value = True
			
			#Socket atomic_number
			atomic_number_socket = select_atomic_number.interface.new_socket(name = "atomic_number", in_out='INPUT', socket_type = 'NodeSocketInt')
			atomic_number_socket.subtype = 'NONE'
			atomic_number_socket.default_value = 6
			atomic_number_socket.min_value = 1
			atomic_number_socket.max_value = 140
			atomic_number_socket.attribute_domain = 'POINT'
			atomic_number_socket.description = "Create a selection based on the inputted atomic number."
			
			
			#initialize select_atomic_number nodes
			#node Named Attribute
			named_attribute_6 = select_atomic_number.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_6.name = "Named Attribute"
			named_attribute_6.data_type = 'INT'
			#Name
			named_attribute_6.inputs[0].default_value = "atomic_number"
			
			#node Compare
			compare_5 = select_atomic_number.nodes.new("FunctionNodeCompare")
			compare_5.name = "Compare"
			compare_5.data_type = 'INT'
			compare_5.mode = 'ELEMENT'
			compare_5.operation = 'EQUAL'
			
			#node Boolean Math
			boolean_math_4 = select_atomic_number.nodes.new("FunctionNodeBooleanMath")
			boolean_math_4.name = "Boolean Math"
			boolean_math_4.operation = 'NOT'
			
			#node Group Output
			group_output_19 = select_atomic_number.nodes.new("NodeGroupOutput")
			group_output_19.name = "Group Output"
			group_output_19.is_active_output = True
			
			#node Group Input
			group_input_19 = select_atomic_number.nodes.new("NodeGroupInput")
			group_input_19.name = "Group Input"
			group_input_19.outputs[0].hide = True
			
			#node Reroute
			reroute_3 = select_atomic_number.nodes.new("NodeReroute")
			reroute_3.name = "Reroute"
			#node Boolean Math.001
			boolean_math_001_4 = select_atomic_number.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_4.name = "Boolean Math.001"
			boolean_math_001_4.operation = 'AND'
			
			#node Group Input.001
			group_input_001_4 = select_atomic_number.nodes.new("NodeGroupInput")
			group_input_001_4.name = "Group Input.001"
			group_input_001_4.outputs[1].hide = True
			group_input_001_4.outputs[2].hide = True
			group_input_001_4.outputs[3].hide = True
			
			#node Boolean Math.002
			boolean_math_002_5 = select_atomic_number.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_5.name = "Boolean Math.002"
			boolean_math_002_5.operation = 'OR'
			
			
			
			
			#Set locations
			named_attribute_6.location = (-548.0000610351562, 0.0)
			compare_5.location = (-388.0, 0.0)
			boolean_math_4.location = (148.0, -60.0)
			group_output_19.location = (347.9999694824219, 0.0)
			group_input_19.location = (-548.0000610351562, -140.0)
			reroute_3.location = (148.0, -60.0)
			boolean_math_001_4.location = (-220.0, 0.0)
			group_input_001_4.location = (-400.0, 80.0)
			boolean_math_002_5.location = (-40.0, 0.0)
			
			#Set dimensions
			named_attribute_6.width, named_attribute_6.height = 140.0, 100.0
			compare_5.width, compare_5.height = 140.0, 100.0
			boolean_math_4.width, boolean_math_4.height = 140.0, 100.0
			group_output_19.width, group_output_19.height = 140.0, 100.0
			group_input_19.width, group_input_19.height = 140.0, 100.0
			reroute_3.width, reroute_3.height = 16.0, 100.0
			boolean_math_001_4.width, boolean_math_001_4.height = 140.0, 100.0
			group_input_001_4.width, group_input_001_4.height = 140.0, 100.0
			boolean_math_002_5.width, boolean_math_002_5.height = 140.0, 100.0
			
			#initialize select_atomic_number links
			#named_attribute_6.Attribute -> compare_5.A
			select_atomic_number.links.new(named_attribute_6.outputs[0], compare_5.inputs[2])
			#reroute_3.Output -> boolean_math_4.Boolean
			select_atomic_number.links.new(reroute_3.outputs[0], boolean_math_4.inputs[0])
			#group_input_19.atomic_number -> compare_5.B
			select_atomic_number.links.new(group_input_19.outputs[2], compare_5.inputs[3])
			#reroute_3.Output -> group_output_19.Selection
			select_atomic_number.links.new(reroute_3.outputs[0], group_output_19.inputs[0])
			#boolean_math_4.Boolean -> group_output_19.Inverted
			select_atomic_number.links.new(boolean_math_4.outputs[0], group_output_19.inputs[1])
			#boolean_math_002_5.Boolean -> reroute_3.Input
			select_atomic_number.links.new(boolean_math_002_5.outputs[0], reroute_3.inputs[0])
			#compare_5.Result -> boolean_math_001_4.Boolean
			select_atomic_number.links.new(compare_5.outputs[0], boolean_math_001_4.inputs[1])
			#group_input_001_4.And -> boolean_math_001_4.Boolean
			select_atomic_number.links.new(group_input_001_4.outputs[0], boolean_math_001_4.inputs[0])
			#boolean_math_001_4.Boolean -> boolean_math_002_5.Boolean
			select_atomic_number.links.new(boolean_math_001_4.outputs[0], boolean_math_002_5.inputs[0])
			#group_input_19.Or -> boolean_math_002_5.Boolean
			select_atomic_number.links.new(group_input_19.outputs[1], boolean_math_002_5.inputs[1])
			return select_atomic_number

		select_atomic_number = select_atomic_number_node_group()

		#initialize style_sticks node group
		def style_sticks_node_group():
			style_sticks = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Style Sticks")

			style_sticks.color_tag = 'GEOMETRY'
			style_sticks.description = ""

			
			#style_sticks interface
			#Socket Geometry
			geometry_socket_3 = style_sticks.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_3.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket_8 = style_sticks.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_8.attribute_domain = 'POINT'
			atoms_socket_8.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket_12 = style_sticks.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_12.attribute_domain = 'POINT'
			selection_socket_12.hide_value = True
			selection_socket_12.description = "Selection of atoms to apply this style to"
			
			#Socket Quality
			quality_socket_1 = style_sticks.interface.new_socket(name = "Quality", in_out='INPUT', socket_type = 'NodeSocketInt')
			quality_socket_1.subtype = 'NONE'
			quality_socket_1.default_value = 2
			quality_socket_1.min_value = 0
			quality_socket_1.max_value = 5
			quality_socket_1.attribute_domain = 'POINT'
			
			#Socket Radius
			radius_socket_1 = style_sticks.interface.new_socket(name = "Radius", in_out='INPUT', socket_type = 'NodeSocketFloat')
			radius_socket_1.subtype = 'NONE'
			radius_socket_1.default_value = 0.20000000298023224
			radius_socket_1.min_value = 0.0
			radius_socket_1.max_value = 1.0
			radius_socket_1.attribute_domain = 'POINT'
			
			#Panel Material
			material_panel_3 = style_sticks.interface.new_panel("Material", default_closed=True)
			#Socket Color Blur
			color_blur_socket_1 = style_sticks.interface.new_socket(name = "Color Blur", in_out='INPUT', socket_type = 'NodeSocketBool', parent = material_panel_3)
			color_blur_socket_1.attribute_domain = 'POINT'
			
			#Socket Shade Smooth
			shade_smooth_socket_4 = style_sticks.interface.new_socket(name = "Shade Smooth", in_out='INPUT', socket_type = 'NodeSocketBool', parent = material_panel_3)
			shade_smooth_socket_4.attribute_domain = 'POINT'
			shade_smooth_socket_4.description = "Apply smooth shading to the created geometry"
			
			#Socket Material
			material_socket_5 = style_sticks.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial', parent = material_panel_3)
			material_socket_5.attribute_domain = 'POINT'
			material_socket_5.description = "Material to apply to the resulting geometry"
			
			
			
			#initialize style_sticks nodes
			#node Group Output
			group_output_20 = style_sticks.nodes.new("NodeGroupOutput")
			group_output_20.name = "Group Output"
			group_output_20.is_active_output = True
			
			#node Join Geometry
			join_geometry_1 = style_sticks.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_1.name = "Join Geometry"
			
			#node MN_style_spheres
			mn_style_spheres = style_sticks.nodes.new("GeometryNodeGroup")
			mn_style_spheres.label = "Style Spheres"
			mn_style_spheres.name = "MN_style_spheres"
			mn_style_spheres.node_tree = style_spheres
			#Input_1
			mn_style_spheres.inputs[1].default_value = True
			#Input_2
			mn_style_spheres.inputs[2].default_value = True
			
			#node Separate Geometry
			separate_geometry_6 = style_sticks.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_6.name = "Separate Geometry"
			separate_geometry_6.domain = 'POINT'
			
			#node Reroute
			reroute_4 = style_sticks.nodes.new("NodeReroute")
			reroute_4.name = "Reroute"
			#node Store Named Attribute
			store_named_attribute_2 = style_sticks.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_2.name = "Store Named Attribute"
			store_named_attribute_2.data_type = 'FLOAT'
			store_named_attribute_2.domain = 'POINT'
			#Selection
			store_named_attribute_2.inputs[1].default_value = True
			#Name
			store_named_attribute_2.inputs[2].default_value = "vdw_radii"
			#Value
			store_named_attribute_2.inputs[3].default_value = 0.009999999776482582
			
			#node Reroute.001
			reroute_001_2 = style_sticks.nodes.new("NodeReroute")
			reroute_001_2.name = "Reroute.001"
			#node .MN_utils_style_sticks
			_mn_utils_style_sticks_1 = style_sticks.nodes.new("GeometryNodeGroup")
			_mn_utils_style_sticks_1.name = ".MN_utils_style_sticks"
			_mn_utils_style_sticks_1.node_tree = _mn_utils_style_sticks
			#Socket_0
			_mn_utils_style_sticks_1.inputs[1].default_value = True
			#Input_15
			_mn_utils_style_sticks_1.inputs[4].default_value = False
			
			#node Integer
			integer_3 = style_sticks.nodes.new("FunctionNodeInputInt")
			integer_3.name = "Integer"
			integer_3.integer = 8
			
			#node Group Input
			group_input_20 = style_sticks.nodes.new("NodeGroupInput")
			group_input_20.name = "Group Input"
			
			#node Math
			math_6 = style_sticks.nodes.new("ShaderNodeMath")
			math_6.name = "Math"
			math_6.operation = 'MULTIPLY'
			math_6.use_clamp = False
			
			
			
			
			#Set locations
			group_output_20.location = (140.0, 120.0)
			join_geometry_1.location = (-20.0, 120.0)
			mn_style_spheres.location = (-260.0, 200.0)
			separate_geometry_6.location = (-660.0, 140.0)
			reroute_4.location = (-480.0, -60.0)
			store_named_attribute_2.location = (-440.0, 200.0)
			reroute_001_2.location = (-660.0, -40.0)
			_mn_utils_style_sticks_1.location = (-260.0, -120.0)
			integer_3.location = (-640.0, -340.0)
			group_input_20.location = (-860.0, 60.0)
			math_6.location = (-440.0, -220.0)
			
			#Set dimensions
			group_output_20.width, group_output_20.height = 140.0, 100.0
			join_geometry_1.width, join_geometry_1.height = 140.0, 100.0
			mn_style_spheres.width, mn_style_spheres.height = 200.0, 100.0
			separate_geometry_6.width, separate_geometry_6.height = 140.0, 100.0
			reroute_4.width, reroute_4.height = 16.0, 100.0
			store_named_attribute_2.width, store_named_attribute_2.height = 140.0, 100.0
			reroute_001_2.width, reroute_001_2.height = 16.0, 100.0
			_mn_utils_style_sticks_1.width, _mn_utils_style_sticks_1.height = 207.9752197265625, 100.0
			integer_3.width, integer_3.height = 140.0, 100.0
			group_input_20.width, group_input_20.height = 140.0, 100.0
			math_6.width, math_6.height = 140.0, 100.0
			
			#initialize style_sticks links
			#group_input_20.Atoms -> separate_geometry_6.Geometry
			style_sticks.links.new(group_input_20.outputs[0], separate_geometry_6.inputs[0])
			#store_named_attribute_2.Geometry -> mn_style_spheres.Atoms
			style_sticks.links.new(store_named_attribute_2.outputs[0], mn_style_spheres.inputs[0])
			#group_input_20.Selection -> separate_geometry_6.Selection
			style_sticks.links.new(group_input_20.outputs[1], separate_geometry_6.inputs[1])
			#separate_geometry_6.Selection -> _mn_utils_style_sticks_1.Atoms
			style_sticks.links.new(separate_geometry_6.outputs[0], _mn_utils_style_sticks_1.inputs[0])
			#_mn_utils_style_sticks_1.Geometry -> join_geometry_1.Geometry
			style_sticks.links.new(_mn_utils_style_sticks_1.outputs[0], join_geometry_1.inputs[0])
			#join_geometry_1.Geometry -> group_output_20.Geometry
			style_sticks.links.new(join_geometry_1.outputs[0], group_output_20.inputs[0])
			#separate_geometry_6.Selection -> store_named_attribute_2.Geometry
			style_sticks.links.new(separate_geometry_6.outputs[0], store_named_attribute_2.inputs[0])
			#reroute_4.Output -> mn_style_spheres.Sphere Radii
			style_sticks.links.new(reroute_4.outputs[0], mn_style_spheres.inputs[3])
			#reroute_4.Output -> _mn_utils_style_sticks_1.Radius
			style_sticks.links.new(reroute_4.outputs[0], _mn_utils_style_sticks_1.inputs[2])
			#group_input_20.Radius -> reroute_4.Input
			style_sticks.links.new(group_input_20.outputs[3], reroute_4.inputs[0])
			#reroute_001_2.Output -> mn_style_spheres.Sphere Subdivisions
			style_sticks.links.new(reroute_001_2.outputs[0], mn_style_spheres.inputs[4])
			#group_input_20.Quality -> reroute_001_2.Input
			style_sticks.links.new(group_input_20.outputs[2], reroute_001_2.inputs[0])
			#reroute_001_2.Output -> math_6.Value
			style_sticks.links.new(reroute_001_2.outputs[0], math_6.inputs[0])
			#math_6.Value -> _mn_utils_style_sticks_1.Resolution
			style_sticks.links.new(math_6.outputs[0], _mn_utils_style_sticks_1.inputs[3])
			#integer_3.Integer -> math_6.Value
			style_sticks.links.new(integer_3.outputs[0], math_6.inputs[1])
			#group_input_20.Shade Smooth -> mn_style_spheres.Shade Smooth
			style_sticks.links.new(group_input_20.outputs[5], mn_style_spheres.inputs[5])
			#group_input_20.Material -> mn_style_spheres.Material
			style_sticks.links.new(group_input_20.outputs[6], mn_style_spheres.inputs[6])
			#group_input_20.Material -> _mn_utils_style_sticks_1.Material
			style_sticks.links.new(group_input_20.outputs[6], _mn_utils_style_sticks_1.inputs[7])
			#group_input_20.Shade Smooth -> _mn_utils_style_sticks_1.Shade Smooth
			style_sticks.links.new(group_input_20.outputs[5], _mn_utils_style_sticks_1.inputs[6])
			#group_input_20.Color Blur -> _mn_utils_style_sticks_1.Interpolate Color
			style_sticks.links.new(group_input_20.outputs[4], _mn_utils_style_sticks_1.inputs[5])
			#mn_style_spheres.Geometry -> join_geometry_1.Geometry
			style_sticks.links.new(mn_style_spheres.outputs[0], join_geometry_1.inputs[0])
			return style_sticks

		style_sticks = style_sticks_node_group()

		#initialize _guide_rotation node group
		def _guide_rotation_node_group():
			_guide_rotation = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".guide_rotation")

			_guide_rotation.color_tag = 'NONE'
			_guide_rotation.description = ""

			
			#_guide_rotation interface
			#Socket Rotation
			rotation_socket = _guide_rotation.interface.new_socket(name = "Rotation", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			rotation_socket.subtype = 'EULER'
			rotation_socket.default_value = (0.0, 0.0, 0.0)
			rotation_socket.min_value = -3.4028234663852886e+38
			rotation_socket.max_value = 3.4028234663852886e+38
			rotation_socket.attribute_domain = 'POINT'
			
			#Socket Angle
			angle_socket = _guide_rotation.interface.new_socket(name = "Angle", in_out='INPUT', socket_type = 'NodeSocketFloat')
			angle_socket.subtype = 'ANGLE'
			angle_socket.default_value = 0.0
			angle_socket.min_value = -3.4028234663852886e+38
			angle_socket.max_value = 3.4028234663852886e+38
			angle_socket.attribute_domain = 'POINT'
			
			
			#initialize _guide_rotation nodes
			#node Align Euler to Vector.001
			align_euler_to_vector_001 = _guide_rotation.nodes.new("FunctionNodeAlignEulerToVector")
			align_euler_to_vector_001.name = "Align Euler to Vector.001"
			align_euler_to_vector_001.axis = 'X'
			align_euler_to_vector_001.pivot_axis = 'Z'
			#Factor
			align_euler_to_vector_001.inputs[1].default_value = 1.0
			
			#node Rotate Euler
			rotate_euler = _guide_rotation.nodes.new("FunctionNodeRotateEuler")
			rotate_euler.name = "Rotate Euler"
			rotate_euler.rotation_type = 'AXIS_ANGLE'
			rotate_euler.space = 'OBJECT'
			
			#node Align Euler to Vector
			align_euler_to_vector = _guide_rotation.nodes.new("FunctionNodeAlignEulerToVector")
			align_euler_to_vector.name = "Align Euler to Vector"
			align_euler_to_vector.axis = 'Z'
			align_euler_to_vector.pivot_axis = 'AUTO'
			#Rotation
			align_euler_to_vector.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Factor
			align_euler_to_vector.inputs[1].default_value = 1.0
			
			#node Group Output
			group_output_21 = _guide_rotation.nodes.new("NodeGroupOutput")
			group_output_21.name = "Group Output"
			group_output_21.is_active_output = True
			
			#node Reroute
			reroute_5 = _guide_rotation.nodes.new("NodeReroute")
			reroute_5.name = "Reroute"
			#node Named Attribute.001
			named_attribute_001_2 = _guide_rotation.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001_2.name = "Named Attribute.001"
			named_attribute_001_2.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_001_2.inputs[0].default_value = "guide_X"
			
			#node Named Attribute
			named_attribute_7 = _guide_rotation.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_7.name = "Named Attribute"
			named_attribute_7.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_7.inputs[0].default_value = "guide_Z"
			
			#node Group Input.001
			group_input_001_5 = _guide_rotation.nodes.new("NodeGroupInput")
			group_input_001_5.name = "Group Input.001"
			
			
			
			
			#Set locations
			align_euler_to_vector_001.location = (177.053955078125, 186.16505432128906)
			rotate_euler.location = (356.9603271484375, 191.41680908203125)
			align_euler_to_vector.location = (20.0, 180.0)
			group_output_21.location = (540.0, 180.0)
			reroute_5.location = (140.0, -40.0)
			named_attribute_001_2.location = (-180.0, 40.0)
			named_attribute_7.location = (-180.0, 180.0)
			group_input_001_5.location = (180.0, -40.0)
			
			#Set dimensions
			align_euler_to_vector_001.width, align_euler_to_vector_001.height = 140.0, 100.0
			rotate_euler.width, rotate_euler.height = 140.0, 100.0
			align_euler_to_vector.width, align_euler_to_vector.height = 140.0, 100.0
			group_output_21.width, group_output_21.height = 140.0, 100.0
			reroute_5.width, reroute_5.height = 16.0, 100.0
			named_attribute_001_2.width, named_attribute_001_2.height = 145.799072265625, 100.0
			named_attribute_7.width, named_attribute_7.height = 146.58917236328125, 100.0
			group_input_001_5.width, group_input_001_5.height = 140.0, 100.0
			
			#initialize _guide_rotation links
			#reroute_5.Output -> align_euler_to_vector_001.Vector
			_guide_rotation.links.new(reroute_5.outputs[0], align_euler_to_vector_001.inputs[2])
			#align_euler_to_vector.Rotation -> align_euler_to_vector_001.Rotation
			_guide_rotation.links.new(align_euler_to_vector.outputs[0], align_euler_to_vector_001.inputs[0])
			#rotate_euler.Rotation -> group_output_21.Rotation
			_guide_rotation.links.new(rotate_euler.outputs[0], group_output_21.inputs[0])
			#align_euler_to_vector_001.Rotation -> rotate_euler.Rotation
			_guide_rotation.links.new(align_euler_to_vector_001.outputs[0], rotate_euler.inputs[0])
			#group_input_001_5.Angle -> rotate_euler.Angle
			_guide_rotation.links.new(group_input_001_5.outputs[0], rotate_euler.inputs[3])
			#named_attribute_7.Attribute -> align_euler_to_vector.Vector
			_guide_rotation.links.new(named_attribute_7.outputs[0], align_euler_to_vector.inputs[2])
			#reroute_5.Output -> rotate_euler.Axis
			_guide_rotation.links.new(reroute_5.outputs[0], rotate_euler.inputs[2])
			#named_attribute_001_2.Attribute -> reroute_5.Input
			_guide_rotation.links.new(named_attribute_001_2.outputs[0], reroute_5.inputs[0])
			return _guide_rotation

		_guide_rotation = _guide_rotation_node_group()

		#initialize _mn_select_sec_struct_id node group
		def _mn_select_sec_struct_id_node_group():
			_mn_select_sec_struct_id = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_select_sec_struct_id")

			_mn_select_sec_struct_id.color_tag = 'NONE'
			_mn_select_sec_struct_id.description = ""

			
			#_mn_select_sec_struct_id interface
			#Socket Selection
			selection_socket_13 = _mn_select_sec_struct_id.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket_13.attribute_domain = 'POINT'
			selection_socket_13.description = "The calculated selection"
			
			#Socket Inverted
			inverted_socket_4 = _mn_select_sec_struct_id.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket_4.attribute_domain = 'POINT'
			
			#Socket And
			and_socket_3 = _mn_select_sec_struct_id.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket_3.attribute_domain = 'POINT'
			and_socket_3.hide_value = True
			
			#Socket Or
			or_socket_3 = _mn_select_sec_struct_id.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket_3.attribute_domain = 'POINT'
			or_socket_3.hide_value = True
			
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
			named_attribute_002_2 = _mn_select_sec_struct_id.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002_2.name = "Named Attribute.002"
			named_attribute_002_2.data_type = 'INT'
			#Name
			named_attribute_002_2.inputs[0].default_value = "sec_struct"
			
			#node Boolean Math
			boolean_math_5 = _mn_select_sec_struct_id.nodes.new("FunctionNodeBooleanMath")
			boolean_math_5.name = "Boolean Math"
			boolean_math_5.operation = 'AND'
			
			#node Group Output
			group_output_22 = _mn_select_sec_struct_id.nodes.new("NodeGroupOutput")
			group_output_22.name = "Group Output"
			group_output_22.is_active_output = True
			
			#node Compare.012
			compare_012 = _mn_select_sec_struct_id.nodes.new("FunctionNodeCompare")
			compare_012.name = "Compare.012"
			compare_012.data_type = 'INT'
			compare_012.mode = 'ELEMENT'
			compare_012.operation = 'EQUAL'
			
			#node Group Input
			group_input_21 = _mn_select_sec_struct_id.nodes.new("NodeGroupInput")
			group_input_21.name = "Group Input"
			
			#node Boolean Math.001
			boolean_math_001_5 = _mn_select_sec_struct_id.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_5.name = "Boolean Math.001"
			boolean_math_001_5.operation = 'OR'
			
			#node Boolean Math.002
			boolean_math_002_6 = _mn_select_sec_struct_id.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_6.name = "Boolean Math.002"
			boolean_math_002_6.operation = 'NOT'
			
			
			
			
			#Set locations
			named_attribute_002_2.location = (80.0, 0.0)
			boolean_math_5.location = (400.0, 200.0)
			group_output_22.location = (760.0, 200.0)
			compare_012.location = (240.0, 100.0)
			group_input_21.location = (80.0, 100.0)
			boolean_math_001_5.location = (579.9999389648438, 196.54164123535156)
			boolean_math_002_6.location = (580.0, 60.0)
			
			#Set dimensions
			named_attribute_002_2.width, named_attribute_002_2.height = 140.0, 100.0
			boolean_math_5.width, boolean_math_5.height = 140.0, 100.0
			group_output_22.width, group_output_22.height = 140.0, 100.0
			compare_012.width, compare_012.height = 140.0, 100.0
			group_input_21.width, group_input_21.height = 140.0, 100.0
			boolean_math_001_5.width, boolean_math_001_5.height = 140.0, 100.0
			boolean_math_002_6.width, boolean_math_002_6.height = 140.0, 100.0
			
			#initialize _mn_select_sec_struct_id links
			#boolean_math_001_5.Boolean -> group_output_22.Selection
			_mn_select_sec_struct_id.links.new(boolean_math_001_5.outputs[0], group_output_22.inputs[0])
			#compare_012.Result -> boolean_math_5.Boolean
			_mn_select_sec_struct_id.links.new(compare_012.outputs[0], boolean_math_5.inputs[1])
			#group_input_21.id -> compare_012.A
			_mn_select_sec_struct_id.links.new(group_input_21.outputs[2], compare_012.inputs[2])
			#group_input_21.And -> boolean_math_5.Boolean
			_mn_select_sec_struct_id.links.new(group_input_21.outputs[0], boolean_math_5.inputs[0])
			#named_attribute_002_2.Attribute -> compare_012.B
			_mn_select_sec_struct_id.links.new(named_attribute_002_2.outputs[0], compare_012.inputs[3])
			#boolean_math_5.Boolean -> boolean_math_001_5.Boolean
			_mn_select_sec_struct_id.links.new(boolean_math_5.outputs[0], boolean_math_001_5.inputs[0])
			#group_input_21.Or -> boolean_math_001_5.Boolean
			_mn_select_sec_struct_id.links.new(group_input_21.outputs[1], boolean_math_001_5.inputs[1])
			#boolean_math_001_5.Boolean -> boolean_math_002_6.Boolean
			_mn_select_sec_struct_id.links.new(boolean_math_001_5.outputs[0], boolean_math_002_6.inputs[0])
			#boolean_math_002_6.Boolean -> group_output_22.Inverted
			_mn_select_sec_struct_id.links.new(boolean_math_002_6.outputs[0], group_output_22.inputs[1])
			return _mn_select_sec_struct_id

		_mn_select_sec_struct_id = _mn_select_sec_struct_id_node_group()

		#initialize is_sheet node group
		def is_sheet_node_group():
			is_sheet = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Is Sheet")

			is_sheet.color_tag = 'INPUT'
			is_sheet.description = ""

			
			#is_sheet interface
			#Socket Selection
			selection_socket_14 = is_sheet.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket_14.attribute_domain = 'POINT'
			selection_socket_14.description = "Selected atoms form part of a sheet"
			
			#Socket Inverted
			inverted_socket_5 = is_sheet.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket_5.attribute_domain = 'POINT'
			
			#Socket And
			and_socket_4 = is_sheet.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket_4.attribute_domain = 'POINT'
			and_socket_4.hide_value = True
			
			#Socket Or
			or_socket_4 = is_sheet.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket_4.attribute_domain = 'POINT'
			or_socket_4.hide_value = True
			
			
			#initialize is_sheet nodes
			#node Group Output
			group_output_23 = is_sheet.nodes.new("NodeGroupOutput")
			group_output_23.name = "Group Output"
			group_output_23.is_active_output = True
			
			#node Group Input
			group_input_22 = is_sheet.nodes.new("NodeGroupInput")
			group_input_22.name = "Group Input"
			
			#node MN_select_sec_struct.002
			mn_select_sec_struct_002 = is_sheet.nodes.new("GeometryNodeGroup")
			mn_select_sec_struct_002.label = "Select Sec Struct"
			mn_select_sec_struct_002.name = "MN_select_sec_struct.002"
			mn_select_sec_struct_002.node_tree = _mn_select_sec_struct_id
			#Socket_1
			mn_select_sec_struct_002.inputs[2].default_value = 2
			
			
			
			
			#Set locations
			group_output_23.location = (267.00146484375, 0.0)
			group_input_22.location = (-220.0, -80.0)
			mn_select_sec_struct_002.location = (0.0, 0.0)
			
			#Set dimensions
			group_output_23.width, group_output_23.height = 140.0, 100.0
			group_input_22.width, group_input_22.height = 140.0, 100.0
			mn_select_sec_struct_002.width, mn_select_sec_struct_002.height = 217.00146484375, 100.0
			
			#initialize is_sheet links
			#mn_select_sec_struct_002.Selection -> group_output_23.Selection
			is_sheet.links.new(mn_select_sec_struct_002.outputs[0], group_output_23.inputs[0])
			#group_input_22.And -> mn_select_sec_struct_002.And
			is_sheet.links.new(group_input_22.outputs[0], mn_select_sec_struct_002.inputs[0])
			#group_input_22.Or -> mn_select_sec_struct_002.Or
			is_sheet.links.new(group_input_22.outputs[1], mn_select_sec_struct_002.inputs[1])
			#mn_select_sec_struct_002.Inverted -> group_output_23.Inverted
			is_sheet.links.new(mn_select_sec_struct_002.outputs[1], group_output_23.inputs[1])
			return is_sheet

		is_sheet = is_sheet_node_group()

		#initialize is_loop node group
		def is_loop_node_group():
			is_loop = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Is Loop")

			is_loop.color_tag = 'INPUT'
			is_loop.description = ""

			
			#is_loop interface
			#Socket Selection
			selection_socket_15 = is_loop.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket_15.attribute_domain = 'POINT'
			selection_socket_15.description = "Selected atoms form part of a loop, and not part of any secondary structure"
			
			#Socket Inverted
			inverted_socket_6 = is_loop.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket_6.attribute_domain = 'POINT'
			
			#Socket And
			and_socket_5 = is_loop.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket_5.attribute_domain = 'POINT'
			and_socket_5.hide_value = True
			
			#Socket Or
			or_socket_5 = is_loop.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket_5.attribute_domain = 'POINT'
			or_socket_5.hide_value = True
			
			
			#initialize is_loop nodes
			#node Group Output
			group_output_24 = is_loop.nodes.new("NodeGroupOutput")
			group_output_24.name = "Group Output"
			group_output_24.is_active_output = True
			
			#node Group Input
			group_input_23 = is_loop.nodes.new("NodeGroupInput")
			group_input_23.name = "Group Input"
			
			#node MN_select_sec_struct.002
			mn_select_sec_struct_002_1 = is_loop.nodes.new("GeometryNodeGroup")
			mn_select_sec_struct_002_1.label = "Select Sec Struct"
			mn_select_sec_struct_002_1.name = "MN_select_sec_struct.002"
			mn_select_sec_struct_002_1.node_tree = _mn_select_sec_struct_id
			#Socket_1
			mn_select_sec_struct_002_1.inputs[2].default_value = 3
			
			
			
			
			#Set locations
			group_output_24.location = (267.00146484375, 0.0)
			group_input_23.location = (-200.0, 0.0)
			mn_select_sec_struct_002_1.location = (0.0, 0.0)
			
			#Set dimensions
			group_output_24.width, group_output_24.height = 140.0, 100.0
			group_input_23.width, group_input_23.height = 140.0, 100.0
			mn_select_sec_struct_002_1.width, mn_select_sec_struct_002_1.height = 217.00146484375, 100.0
			
			#initialize is_loop links
			#mn_select_sec_struct_002_1.Selection -> group_output_24.Selection
			is_loop.links.new(mn_select_sec_struct_002_1.outputs[0], group_output_24.inputs[0])
			#group_input_23.And -> mn_select_sec_struct_002_1.And
			is_loop.links.new(group_input_23.outputs[0], mn_select_sec_struct_002_1.inputs[0])
			#group_input_23.Or -> mn_select_sec_struct_002_1.Or
			is_loop.links.new(group_input_23.outputs[1], mn_select_sec_struct_002_1.inputs[1])
			#mn_select_sec_struct_002_1.Inverted -> group_output_24.Inverted
			is_loop.links.new(mn_select_sec_struct_002_1.outputs[1], group_output_24.inputs[1])
			return is_loop

		is_loop = is_loop_node_group()

		#initialize is_helix node group
		def is_helix_node_group():
			is_helix = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Is Helix")

			is_helix.color_tag = 'INPUT'
			is_helix.description = ""

			
			#is_helix interface
			#Socket Selection
			selection_socket_16 = is_helix.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket_16.attribute_domain = 'POINT'
			selection_socket_16.description = "Selected atoms form part of an helix"
			
			#Socket Inverted
			inverted_socket_7 = is_helix.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket_7.attribute_domain = 'POINT'
			
			#Socket And
			and_socket_6 = is_helix.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket_6.attribute_domain = 'POINT'
			and_socket_6.hide_value = True
			
			#Socket Or
			or_socket_6 = is_helix.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket_6.attribute_domain = 'POINT'
			or_socket_6.hide_value = True
			
			
			#initialize is_helix nodes
			#node Group Output
			group_output_25 = is_helix.nodes.new("NodeGroupOutput")
			group_output_25.name = "Group Output"
			group_output_25.is_active_output = True
			
			#node Group Input
			group_input_24 = is_helix.nodes.new("NodeGroupInput")
			group_input_24.name = "Group Input"
			
			#node MN_select_sec_struct.002
			mn_select_sec_struct_002_2 = is_helix.nodes.new("GeometryNodeGroup")
			mn_select_sec_struct_002_2.label = "Select Sec Struct"
			mn_select_sec_struct_002_2.name = "MN_select_sec_struct.002"
			mn_select_sec_struct_002_2.node_tree = _mn_select_sec_struct_id
			#Socket_1
			mn_select_sec_struct_002_2.inputs[2].default_value = 1
			
			
			
			
			#Set locations
			group_output_25.location = (267.00146484375, 0.0)
			group_input_24.location = (-200.0, 0.0)
			mn_select_sec_struct_002_2.location = (0.0, 0.0)
			
			#Set dimensions
			group_output_25.width, group_output_25.height = 140.0, 100.0
			group_input_24.width, group_input_24.height = 140.0, 100.0
			mn_select_sec_struct_002_2.width, mn_select_sec_struct_002_2.height = 217.00146484375, 100.0
			
			#initialize is_helix links
			#mn_select_sec_struct_002_2.Selection -> group_output_25.Selection
			is_helix.links.new(mn_select_sec_struct_002_2.outputs[0], group_output_25.inputs[0])
			#group_input_24.And -> mn_select_sec_struct_002_2.And
			is_helix.links.new(group_input_24.outputs[0], mn_select_sec_struct_002_2.inputs[0])
			#group_input_24.Or -> mn_select_sec_struct_002_2.Or
			is_helix.links.new(group_input_24.outputs[1], mn_select_sec_struct_002_2.inputs[1])
			#mn_select_sec_struct_002_2.Inverted -> group_output_25.Inverted
			is_helix.links.new(mn_select_sec_struct_002_2.outputs[1], group_output_25.inputs[1])
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
			and_socket_7 = _mn_select_sec_struct.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket_7.attribute_domain = 'POINT'
			and_socket_7.hide_value = True
			
			
			#initialize _mn_select_sec_struct nodes
			#node Group.001
			group_001_3 = _mn_select_sec_struct.nodes.new("GeometryNodeGroup")
			group_001_3.name = "Group.001"
			group_001_3.node_tree = is_sheet
			#Socket_3
			group_001_3.inputs[1].default_value = False
			
			#node Group.002
			group_002 = _mn_select_sec_struct.nodes.new("GeometryNodeGroup")
			group_002.name = "Group.002"
			group_002.node_tree = is_loop
			#Socket_3
			group_002.inputs[1].default_value = False
			
			#node Group
			group_10 = _mn_select_sec_struct.nodes.new("GeometryNodeGroup")
			group_10.name = "Group"
			group_10.node_tree = is_helix
			#Socket_3
			group_10.inputs[1].default_value = False
			
			#node Boolean Math.001
			boolean_math_001_6 = _mn_select_sec_struct.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_6.name = "Boolean Math.001"
			boolean_math_001_6.hide = True
			boolean_math_001_6.operation = 'NOT'
			
			#node Group Output
			group_output_26 = _mn_select_sec_struct.nodes.new("NodeGroupOutput")
			group_output_26.name = "Group Output"
			group_output_26.is_active_output = True
			
			#node Group Input
			group_input_25 = _mn_select_sec_struct.nodes.new("NodeGroupInput")
			group_input_25.name = "Group Input"
			group_input_25.outputs[1].hide = True
			
			
			
			
			#Set locations
			group_001_3.location = (120.0, -60.0)
			group_002.location = (120.0, -180.0)
			group_10.location = (120.0, 60.0)
			boolean_math_001_6.location = (300.0, -140.0)
			group_output_26.location = (540.0, -60.0)
			group_input_25.location = (-160.0, -40.0)
			
			#Set dimensions
			group_001_3.width, group_001_3.height = 140.0, 100.0
			group_002.width, group_002.height = 140.0, 100.0
			group_10.width, group_10.height = 140.0, 100.0
			boolean_math_001_6.width, boolean_math_001_6.height = 140.0, 100.0
			group_output_26.width, group_output_26.height = 140.0, 100.0
			group_input_25.width, group_input_25.height = 140.0, 100.0
			
			#initialize _mn_select_sec_struct links
			#group_002.Selection -> group_output_26.Is Loop
			_mn_select_sec_struct.links.new(group_002.outputs[0], group_output_26.inputs[3])
			#group_002.Selection -> boolean_math_001_6.Boolean
			_mn_select_sec_struct.links.new(group_002.outputs[0], boolean_math_001_6.inputs[0])
			#boolean_math_001_6.Boolean -> group_output_26.Is Structured
			_mn_select_sec_struct.links.new(boolean_math_001_6.outputs[0], group_output_26.inputs[2])
			#group_10.Selection -> group_output_26.Is Helix
			_mn_select_sec_struct.links.new(group_10.outputs[0], group_output_26.inputs[0])
			#group_001_3.Selection -> group_output_26.Is Sheet
			_mn_select_sec_struct.links.new(group_001_3.outputs[0], group_output_26.inputs[1])
			#group_input_25.And -> group_10.And
			_mn_select_sec_struct.links.new(group_input_25.outputs[0], group_10.inputs[0])
			#group_input_25.And -> group_001_3.And
			_mn_select_sec_struct.links.new(group_input_25.outputs[0], group_001_3.inputs[0])
			#group_input_25.And -> group_002.And
			_mn_select_sec_struct.links.new(group_input_25.outputs[0], group_002.inputs[0])
			return _mn_select_sec_struct

		_mn_select_sec_struct = _mn_select_sec_struct_node_group()

		#initialize _debug_arrows node group
		def _debug_arrows_node_group():
			_debug_arrows = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".DEBUG_arrows")

			_debug_arrows.color_tag = 'NONE'
			_debug_arrows.description = ""

			_debug_arrows.is_modifier = True
			
			#_debug_arrows interface
			#Socket Instances
			instances_socket_1 = _debug_arrows.interface.new_socket(name = "Instances", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			instances_socket_1.attribute_domain = 'POINT'
			
			#Socket Points
			points_socket = _debug_arrows.interface.new_socket(name = "Points", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			points_socket.attribute_domain = 'POINT'
			
			#Socket Position
			position_socket = _debug_arrows.interface.new_socket(name = "Position", in_out='INPUT', socket_type = 'NodeSocketVector')
			position_socket.subtype = 'NONE'
			position_socket.default_value = (0.0, 0.0, 0.0)
			position_socket.min_value = -3.4028234663852886e+38
			position_socket.max_value = 3.4028234663852886e+38
			position_socket.attribute_domain = 'POINT'
			position_socket.hide_value = True
			
			#Socket Offset
			offset_socket = _debug_arrows.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketVector')
			offset_socket.subtype = 'TRANSLATION'
			offset_socket.default_value = (0.0, 0.0, 0.0)
			offset_socket.min_value = -3.4028234663852886e+38
			offset_socket.max_value = 3.4028234663852886e+38
			offset_socket.attribute_domain = 'POINT'
			
			#Socket Rotation
			rotation_socket_1 = _debug_arrows.interface.new_socket(name = "Rotation", in_out='INPUT', socket_type = 'NodeSocketVector')
			rotation_socket_1.subtype = 'EULER'
			rotation_socket_1.default_value = (0.0, 0.0, 0.0)
			rotation_socket_1.min_value = -3.4028234663852886e+38
			rotation_socket_1.max_value = 3.4028234663852886e+38
			rotation_socket_1.attribute_domain = 'POINT'
			
			#Socket Scale
			scale_socket_1 = _debug_arrows.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketVector')
			scale_socket_1.subtype = 'XYZ'
			scale_socket_1.default_value = (0.33000001311302185, 0.36000001430511475, 0.75)
			scale_socket_1.min_value = -3.4028234663852886e+38
			scale_socket_1.max_value = 3.4028234663852886e+38
			scale_socket_1.attribute_domain = 'POINT'
			
			
			#initialize _debug_arrows nodes
			#node Group Output
			group_output_27 = _debug_arrows.nodes.new("NodeGroupOutput")
			group_output_27.name = "Group Output"
			group_output_27.is_active_output = True
			
			#node Instance on Points.002
			instance_on_points_002 = _debug_arrows.nodes.new("GeometryNodeInstanceOnPoints")
			instance_on_points_002.name = "Instance on Points.002"
			#Selection
			instance_on_points_002.inputs[1].default_value = True
			#Pick Instance
			instance_on_points_002.inputs[3].default_value = False
			#Instance Index
			instance_on_points_002.inputs[4].default_value = 0
			
			#node Reroute.003
			reroute_003_1 = _debug_arrows.nodes.new("NodeReroute")
			reroute_003_1.name = "Reroute.003"
			#node Reroute.009
			reroute_009_1 = _debug_arrows.nodes.new("NodeReroute")
			reroute_009_1.name = "Reroute.009"
			#node Join Geometry.001
			join_geometry_001_1 = _debug_arrows.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_001_1.name = "Join Geometry.001"
			join_geometry_001_1.hide = True
			
			#node Transform Geometry.002
			transform_geometry_002 = _debug_arrows.nodes.new("GeometryNodeTransform")
			transform_geometry_002.name = "Transform Geometry.002"
			transform_geometry_002.mode = 'COMPONENTS'
			#Rotation
			transform_geometry_002.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Scale
			transform_geometry_002.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Transform Geometry.001
			transform_geometry_001 = _debug_arrows.nodes.new("GeometryNodeTransform")
			transform_geometry_001.name = "Transform Geometry.001"
			transform_geometry_001.mode = 'COMPONENTS'
			#Translation
			transform_geometry_001.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Rotation
			transform_geometry_001.inputs[2].default_value = (0.0, 1.5707963705062866, 0.0)
			#Scale
			transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Transform Geometry.003
			transform_geometry_003 = _debug_arrows.nodes.new("GeometryNodeTransform")
			transform_geometry_003.name = "Transform Geometry.003"
			transform_geometry_003.mode = 'COMPONENTS'
			#Translation
			transform_geometry_003.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Rotation
			transform_geometry_003.inputs[2].default_value = (1.5707963705062866, 0.0, 0.0)
			#Scale
			transform_geometry_003.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Vector Math.008
			vector_math_008 = _debug_arrows.nodes.new("ShaderNodeVectorMath")
			vector_math_008.name = "Vector Math.008"
			vector_math_008.operation = 'SCALE'
			#Vector
			vector_math_008.inputs[0].default_value = (0.0, 0.0, 10.300000190734863)
			#Scale
			vector_math_008.inputs[3].default_value = 0.0010000000474974513
			
			#node Cone
			cone = _debug_arrows.nodes.new("GeometryNodeMeshCone")
			cone.name = "Cone"
			cone.fill_type = 'NGON'
			#Vertices
			cone.inputs[0].default_value = 6
			#Side Segments
			cone.inputs[1].default_value = 1
			#Fill Segments
			cone.inputs[2].default_value = 1
			#Radius Top
			cone.inputs[3].default_value = 0.0
			#Radius Bottom
			cone.inputs[4].default_value = 0.010000022128224373
			
			#node Math.003
			math_003_1 = _debug_arrows.nodes.new("ShaderNodeMath")
			math_003_1.name = "Math.003"
			math_003_1.operation = 'DIVIDE'
			math_003_1.use_clamp = False
			#Value
			math_003_1.inputs[0].default_value = 49.05999755859375
			#Value_001
			math_003_1.inputs[1].default_value = 1000.0
			
			#node Store Named Attribute.004
			store_named_attribute_004_1 = _debug_arrows.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_004_1.name = "Store Named Attribute.004"
			store_named_attribute_004_1.data_type = 'FLOAT_COLOR'
			store_named_attribute_004_1.domain = 'POINT'
			#Selection
			store_named_attribute_004_1.inputs[1].default_value = True
			#Name
			store_named_attribute_004_1.inputs[2].default_value = "Color"
			#Value
			store_named_attribute_004_1.inputs[3].default_value = (0.4605487287044525, 0.05103481188416481, 0.07814221829175949, 0.0)
			
			#node Store Named Attribute
			store_named_attribute_3 = _debug_arrows.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_3.name = "Store Named Attribute"
			store_named_attribute_3.data_type = 'FLOAT_COLOR'
			store_named_attribute_3.domain = 'POINT'
			#Selection
			store_named_attribute_3.inputs[1].default_value = True
			#Name
			store_named_attribute_3.inputs[2].default_value = "Color"
			#Value
			store_named_attribute_3.inputs[3].default_value = (0.059955447912216187, 0.21724288165569305, 0.4605487287044525, 0.0)
			
			#node Store Named Attribute.005
			store_named_attribute_005_1 = _debug_arrows.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_005_1.name = "Store Named Attribute.005"
			store_named_attribute_005_1.data_type = 'FLOAT_COLOR'
			store_named_attribute_005_1.domain = 'POINT'
			#Selection
			store_named_attribute_005_1.inputs[1].default_value = True
			#Name
			store_named_attribute_005_1.inputs[2].default_value = "Color"
			#Value
			store_named_attribute_005_1.inputs[3].default_value = (0.21280108392238617, 0.4605487287044525, 0.12887145578861237, 0.0)
			
			#node Set Position
			set_position_1 = _debug_arrows.nodes.new("GeometryNodeSetPosition")
			set_position_1.name = "Set Position"
			#Selection
			set_position_1.inputs[1].default_value = True
			
			#node Attribute Statistic
			attribute_statistic = _debug_arrows.nodes.new("GeometryNodeAttributeStatistic")
			attribute_statistic.name = "Attribute Statistic"
			attribute_statistic.data_type = 'FLOAT_VECTOR'
			attribute_statistic.domain = 'POINT'
			#Selection
			attribute_statistic.inputs[1].default_value = True
			
			#node Compare
			compare_6 = _debug_arrows.nodes.new("FunctionNodeCompare")
			compare_6.name = "Compare"
			compare_6.data_type = 'VECTOR'
			compare_6.mode = 'ELEMENT'
			compare_6.operation = 'NOT_EQUAL'
			#B_VEC3
			compare_6.inputs[5].default_value = (0.0, 0.0, 0.0)
			#Epsilon
			compare_6.inputs[12].default_value = 9.999999747378752e-05
			
			#node Position
			position_1 = _debug_arrows.nodes.new("GeometryNodeInputPosition")
			position_1.name = "Position"
			
			#node Switch
			switch_6 = _debug_arrows.nodes.new("GeometryNodeSwitch")
			switch_6.name = "Switch"
			switch_6.input_type = 'VECTOR'
			
			#node Group Input
			group_input_26 = _debug_arrows.nodes.new("NodeGroupInput")
			group_input_26.name = "Group Input"
			
			#node Reroute
			reroute_6 = _debug_arrows.nodes.new("NodeReroute")
			reroute_6.name = "Reroute"
			
			
			
			#Set locations
			group_output_27.location = (1428.90478515625, 0.0)
			instance_on_points_002.location = (988.90478515625, 429.669189453125)
			reroute_003_1.location = (-276.560546875, 27.071929931640625)
			reroute_009_1.location = (-209.260498046875, 36.829681396484375)
			join_geometry_001_1.location = (208.553955078125, 85.46240234375)
			transform_geometry_002.location = (-504.560546875, -72.58740234375)
			transform_geometry_001.location = (-218.82080078125, 19.31646728515625)
			transform_geometry_003.location = (-224.560546875, -334.53759765625)
			vector_math_008.location = (-505.0859375, -418.4356689453125)
			cone.location = (-724.560546875, -214.53759765625)
			math_003_1.location = (-900.904541015625, -429.669189453125)
			store_named_attribute_004_1.location = (-20.0, -100.0)
			store_named_attribute_3.location = (-20.0, 120.0)
			store_named_attribute_005_1.location = (-20.0, -320.0)
			set_position_1.location = (578.2709350585938, 400.1163024902344)
			attribute_statistic.location = (-35.687705993652344, 679.48095703125)
			compare_6.location = (128.0, 680.0)
			position_1.location = (40.0, 420.0)
			switch_6.location = (308.0, 460.0)
			group_input_26.location = (-640.0, 320.0)
			reroute_6.location = (-192.0, 380.0)
			
			#Set dimensions
			group_output_27.width, group_output_27.height = 140.0, 100.0
			instance_on_points_002.width, instance_on_points_002.height = 140.0, 100.0
			reroute_003_1.width, reroute_003_1.height = 16.0, 100.0
			reroute_009_1.width, reroute_009_1.height = 16.0, 100.0
			join_geometry_001_1.width, join_geometry_001_1.height = 140.0, 100.0
			transform_geometry_002.width, transform_geometry_002.height = 140.0, 100.0
			transform_geometry_001.width, transform_geometry_001.height = 140.0, 100.0
			transform_geometry_003.width, transform_geometry_003.height = 140.0, 100.0
			vector_math_008.width, vector_math_008.height = 140.0, 100.0
			cone.width, cone.height = 140.0, 100.0
			math_003_1.width, math_003_1.height = 140.0, 100.0
			store_named_attribute_004_1.width, store_named_attribute_004_1.height = 140.0, 100.0
			store_named_attribute_3.width, store_named_attribute_3.height = 140.0, 100.0
			store_named_attribute_005_1.width, store_named_attribute_005_1.height = 140.0, 100.0
			set_position_1.width, set_position_1.height = 140.0, 100.0
			attribute_statistic.width, attribute_statistic.height = 140.0, 100.0
			compare_6.width, compare_6.height = 140.0, 100.0
			position_1.width, position_1.height = 140.0, 100.0
			switch_6.width, switch_6.height = 140.0, 100.0
			group_input_26.width, group_input_26.height = 140.0, 100.0
			reroute_6.width, reroute_6.height = 16.0, 100.0
			
			#initialize _debug_arrows links
			#reroute_009_1.Output -> store_named_attribute_3.Geometry
			_debug_arrows.links.new(reroute_009_1.outputs[0], store_named_attribute_3.inputs[0])
			#math_003_1.Value -> cone.Depth
			_debug_arrows.links.new(math_003_1.outputs[0], cone.inputs[5])
			#transform_geometry_003.Geometry -> store_named_attribute_005_1.Geometry
			_debug_arrows.links.new(transform_geometry_003.outputs[0], store_named_attribute_005_1.inputs[0])
			#transform_geometry_001.Geometry -> store_named_attribute_004_1.Geometry
			_debug_arrows.links.new(transform_geometry_001.outputs[0], store_named_attribute_004_1.inputs[0])
			#vector_math_008.Vector -> transform_geometry_002.Translation
			_debug_arrows.links.new(vector_math_008.outputs[0], transform_geometry_002.inputs[1])
			#reroute_003_1.Output -> transform_geometry_003.Geometry
			_debug_arrows.links.new(reroute_003_1.outputs[0], transform_geometry_003.inputs[0])
			#cone.Mesh -> transform_geometry_002.Geometry
			_debug_arrows.links.new(cone.outputs[0], transform_geometry_002.inputs[0])
			#reroute_003_1.Output -> reroute_009_1.Input
			_debug_arrows.links.new(reroute_003_1.outputs[0], reroute_009_1.inputs[0])
			#store_named_attribute_004_1.Geometry -> join_geometry_001_1.Geometry
			_debug_arrows.links.new(store_named_attribute_004_1.outputs[0], join_geometry_001_1.inputs[0])
			#transform_geometry_002.Geometry -> reroute_003_1.Input
			_debug_arrows.links.new(transform_geometry_002.outputs[0], reroute_003_1.inputs[0])
			#reroute_003_1.Output -> transform_geometry_001.Geometry
			_debug_arrows.links.new(reroute_003_1.outputs[0], transform_geometry_001.inputs[0])
			#join_geometry_001_1.Geometry -> instance_on_points_002.Instance
			_debug_arrows.links.new(join_geometry_001_1.outputs[0], instance_on_points_002.inputs[2])
			#set_position_1.Geometry -> instance_on_points_002.Points
			_debug_arrows.links.new(set_position_1.outputs[0], instance_on_points_002.inputs[0])
			#group_input_26.Scale -> instance_on_points_002.Scale
			_debug_arrows.links.new(group_input_26.outputs[4], instance_on_points_002.inputs[6])
			#group_input_26.Rotation -> instance_on_points_002.Rotation
			_debug_arrows.links.new(group_input_26.outputs[3], instance_on_points_002.inputs[5])
			#instance_on_points_002.Instances -> group_output_27.Instances
			_debug_arrows.links.new(instance_on_points_002.outputs[0], group_output_27.inputs[0])
			#reroute_6.Output -> set_position_1.Geometry
			_debug_arrows.links.new(reroute_6.outputs[0], set_position_1.inputs[0])
			#group_input_26.Position -> attribute_statistic.Attribute
			_debug_arrows.links.new(group_input_26.outputs[1], attribute_statistic.inputs[2])
			#reroute_6.Output -> attribute_statistic.Geometry
			_debug_arrows.links.new(reroute_6.outputs[0], attribute_statistic.inputs[0])
			#attribute_statistic.Standard Deviation -> compare_6.A
			_debug_arrows.links.new(attribute_statistic.outputs[6], compare_6.inputs[4])
			#compare_6.Result -> switch_6.Switch
			_debug_arrows.links.new(compare_6.outputs[0], switch_6.inputs[0])
			#group_input_26.Position -> switch_6.True
			_debug_arrows.links.new(group_input_26.outputs[1], switch_6.inputs[2])
			#switch_6.Output -> set_position_1.Position
			_debug_arrows.links.new(switch_6.outputs[0], set_position_1.inputs[2])
			#position_1.Position -> switch_6.False
			_debug_arrows.links.new(position_1.outputs[0], switch_6.inputs[1])
			#group_input_26.Offset -> set_position_1.Offset
			_debug_arrows.links.new(group_input_26.outputs[2], set_position_1.inputs[3])
			#group_input_26.Points -> reroute_6.Input
			_debug_arrows.links.new(group_input_26.outputs[0], reroute_6.inputs[0])
			#store_named_attribute_3.Geometry -> join_geometry_001_1.Geometry
			_debug_arrows.links.new(store_named_attribute_3.outputs[0], join_geometry_001_1.inputs[0])
			#store_named_attribute_005_1.Geometry -> join_geometry_001_1.Geometry
			_debug_arrows.links.new(store_named_attribute_005_1.outputs[0], join_geometry_001_1.inputs[0])
			return _debug_arrows

		_debug_arrows = _debug_arrows_node_group()

		#initialize _selective_scale node group
		def _selective_scale_node_group():
			_selective_scale = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".selective_scale")

			_selective_scale.color_tag = 'NONE'
			_selective_scale.description = ""

			
			#_selective_scale interface
			#Socket Output
			output_socket = _selective_scale.interface.new_socket(name = "Output", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			output_socket.subtype = 'NONE'
			output_socket.default_value = 0.0
			output_socket.min_value = -3.4028234663852886e+38
			output_socket.max_value = 3.4028234663852886e+38
			output_socket.attribute_domain = 'POINT'
			
			#Socket Switch
			switch_socket = _selective_scale.interface.new_socket(name = "Switch", in_out='INPUT', socket_type = 'NodeSocketBool')
			switch_socket.attribute_domain = 'POINT'
			
			#Socket Input
			input_socket = _selective_scale.interface.new_socket(name = "Input", in_out='INPUT', socket_type = 'NodeSocketFloat')
			input_socket.subtype = 'NONE'
			input_socket.default_value = 0.0
			input_socket.min_value = -3.4028234663852886e+38
			input_socket.max_value = 3.4028234663852886e+38
			input_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_4 = _selective_scale.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket_4.subtype = 'NONE'
			value_socket_4.default_value = 0.800000011920929
			value_socket_4.min_value = -10000.0
			value_socket_4.max_value = 10000.0
			value_socket_4.attribute_domain = 'POINT'
			
			
			#initialize _selective_scale nodes
			#node Group Output
			group_output_28 = _selective_scale.nodes.new("NodeGroupOutput")
			group_output_28.name = "Group Output"
			group_output_28.is_active_output = True
			
			#node Group Input
			group_input_27 = _selective_scale.nodes.new("NodeGroupInput")
			group_input_27.name = "Group Input"
			
			#node Switch.005
			switch_005 = _selective_scale.nodes.new("GeometryNodeSwitch")
			switch_005.name = "Switch.005"
			switch_005.input_type = 'FLOAT'
			
			#node Math
			math_7 = _selective_scale.nodes.new("ShaderNodeMath")
			math_7.name = "Math"
			math_7.operation = 'MULTIPLY'
			math_7.use_clamp = False
			
			#node Reroute.010
			reroute_010_1 = _selective_scale.nodes.new("NodeReroute")
			reroute_010_1.name = "Reroute.010"
			
			
			
			#Set locations
			group_output_28.location = (200.0, 0.0)
			group_input_27.location = (-210.0, 0.0)
			switch_005.location = (10.0, 90.0)
			math_7.location = (10.0, -70.0)
			reroute_010_1.location = (-10.0, -90.0)
			
			#Set dimensions
			group_output_28.width, group_output_28.height = 140.0, 100.0
			group_input_27.width, group_input_27.height = 140.0, 100.0
			switch_005.width, switch_005.height = 140.0, 100.0
			math_7.width, math_7.height = 140.0, 100.0
			reroute_010_1.width, reroute_010_1.height = 16.0, 100.0
			
			#initialize _selective_scale links
			#math_7.Value -> switch_005.True
			_selective_scale.links.new(math_7.outputs[0], switch_005.inputs[2])
			#reroute_010_1.Output -> switch_005.False
			_selective_scale.links.new(reroute_010_1.outputs[0], switch_005.inputs[1])
			#reroute_010_1.Output -> math_7.Value
			_selective_scale.links.new(reroute_010_1.outputs[0], math_7.inputs[0])
			#group_input_27.Switch -> switch_005.Switch
			_selective_scale.links.new(group_input_27.outputs[0], switch_005.inputs[0])
			#group_input_27.Input -> reroute_010_1.Input
			_selective_scale.links.new(group_input_27.outputs[1], reroute_010_1.inputs[0])
			#switch_005.Output -> group_output_28.Output
			_selective_scale.links.new(switch_005.outputs[0], group_output_28.inputs[0])
			#group_input_27.Value -> math_7.Value
			_selective_scale.links.new(group_input_27.outputs[2], math_7.inputs[1])
			return _selective_scale

		_selective_scale = _selective_scale_node_group()

		#initialize _field_offset_vec node group
		def _field_offset_vec_node_group():
			_field_offset_vec = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".field_offset_vec")

			_field_offset_vec.color_tag = 'NONE'
			_field_offset_vec.description = ""

			
			#_field_offset_vec interface
			#Socket Field
			field_socket = _field_offset_vec.interface.new_socket(name = "Field", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			field_socket.subtype = 'NONE'
			field_socket.default_value = (0.0, 0.0, 0.0)
			field_socket.min_value = -3.4028234663852886e+38
			field_socket.max_value = 3.4028234663852886e+38
			field_socket.attribute_domain = 'POINT'
			
			#Socket Field
			field_socket_1 = _field_offset_vec.interface.new_socket(name = "Field", in_out='INPUT', socket_type = 'NodeSocketVector')
			field_socket_1.subtype = 'NONE'
			field_socket_1.default_value = (0.0, 0.0, 0.0)
			field_socket_1.min_value = -3.4028234663852886e+38
			field_socket_1.max_value = 3.4028234663852886e+38
			field_socket_1.attribute_domain = 'POINT'
			field_socket_1.hide_value = True
			
			#Socket Offset
			offset_socket_1 = _field_offset_vec.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket_1.subtype = 'NONE'
			offset_socket_1.default_value = 0
			offset_socket_1.min_value = -2147483648
			offset_socket_1.max_value = 2147483647
			offset_socket_1.attribute_domain = 'POINT'
			
			
			#initialize _field_offset_vec nodes
			#node Group Input
			group_input_28 = _field_offset_vec.nodes.new("NodeGroupInput")
			group_input_28.name = "Group Input"
			
			#node Evaluate at Index
			evaluate_at_index = _field_offset_vec.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index.name = "Evaluate at Index"
			evaluate_at_index.data_type = 'FLOAT_VECTOR'
			evaluate_at_index.domain = 'POINT'
			
			#node Group Output
			group_output_29 = _field_offset_vec.nodes.new("NodeGroupOutput")
			group_output_29.name = "Group Output"
			group_output_29.is_active_output = True
			
			#node Math.001
			math_001_4 = _field_offset_vec.nodes.new("ShaderNodeMath")
			math_001_4.name = "Math.001"
			math_001_4.operation = 'ADD'
			math_001_4.use_clamp = False
			
			#node Index
			index_2 = _field_offset_vec.nodes.new("GeometryNodeInputIndex")
			index_2.name = "Index"
			
			
			
			
			#Set locations
			group_input_28.location = (-417.64404296875, 0.0)
			evaluate_at_index.location = (-220.0, 100.0)
			group_output_29.location = (20.0, 20.0)
			math_001_4.location = (-220.0, -80.0)
			index_2.location = (-400.0, -180.0)
			
			#Set dimensions
			group_input_28.width, group_input_28.height = 140.0, 100.0
			evaluate_at_index.width, evaluate_at_index.height = 140.0, 100.0
			group_output_29.width, group_output_29.height = 140.0, 100.0
			math_001_4.width, math_001_4.height = 140.0, 100.0
			index_2.width, index_2.height = 140.0, 100.0
			
			#initialize _field_offset_vec links
			#math_001_4.Value -> evaluate_at_index.Index
			_field_offset_vec.links.new(math_001_4.outputs[0], evaluate_at_index.inputs[0])
			#group_input_28.Field -> evaluate_at_index.Value
			_field_offset_vec.links.new(group_input_28.outputs[0], evaluate_at_index.inputs[1])
			#group_input_28.Offset -> math_001_4.Value
			_field_offset_vec.links.new(group_input_28.outputs[1], math_001_4.inputs[0])
			#evaluate_at_index.Value -> group_output_29.Field
			_field_offset_vec.links.new(evaluate_at_index.outputs[0], group_output_29.inputs[0])
			#index_2.Index -> math_001_4.Value
			_field_offset_vec.links.new(index_2.outputs[0], math_001_4.inputs[1])
			return _field_offset_vec

		_field_offset_vec = _field_offset_vec_node_group()

		#initialize _curve_ends_adjust_angle node group
		def _curve_ends_adjust_angle_node_group():
			_curve_ends_adjust_angle = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".curve_ends_adjust_angle")

			_curve_ends_adjust_angle.color_tag = 'NONE'
			_curve_ends_adjust_angle.description = ""

			_curve_ends_adjust_angle.is_modifier = True
			
			#_curve_ends_adjust_angle interface
			#Socket Curve
			curve_socket = _curve_ends_adjust_angle.interface.new_socket(name = "Curve", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			curve_socket.attribute_domain = 'POINT'
			
			#Socket Curve
			curve_socket_1 = _curve_ends_adjust_angle.interface.new_socket(name = "Curve", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			curve_socket_1.attribute_domain = 'POINT'
			
			#Socket Distance
			distance_socket = _curve_ends_adjust_angle.interface.new_socket(name = "Distance", in_out='INPUT', socket_type = 'NodeSocketFloat')
			distance_socket.subtype = 'NONE'
			distance_socket.default_value = 3.0
			distance_socket.min_value = -10000.0
			distance_socket.max_value = 10000.0
			distance_socket.attribute_domain = 'POINT'
			
			#Socket Distance
			distance_socket_1 = _curve_ends_adjust_angle.interface.new_socket(name = "Distance", in_out='INPUT', socket_type = 'NodeSocketFloat')
			distance_socket_1.subtype = 'NONE'
			distance_socket_1.default_value = 0.4200000762939453
			distance_socket_1.min_value = -10000.0
			distance_socket_1.max_value = 10000.0
			distance_socket_1.attribute_domain = 'POINT'
			
			
			#initialize _curve_ends_adjust_angle nodes
			#node Vector Math.001
			vector_math_001 = _curve_ends_adjust_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_001.name = "Vector Math.001"
			vector_math_001.operation = 'SCALE'
			
			#node Set Spline Type.001
			set_spline_type_001 = _curve_ends_adjust_angle.nodes.new("GeometryNodeCurveSplineType")
			set_spline_type_001.name = "Set Spline Type.001"
			set_spline_type_001.spline_type = 'BEZIER'
			#Selection
			set_spline_type_001.inputs[1].default_value = True
			
			#node Boolean Math.003
			boolean_math_003_2 = _curve_ends_adjust_angle.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003_2.name = "Boolean Math.003"
			boolean_math_003_2.operation = 'AND'
			
			#node Reroute.001
			reroute_001_3 = _curve_ends_adjust_angle.nodes.new("NodeReroute")
			reroute_001_3.name = "Reroute.001"
			#node Endpoint Selection.006
			endpoint_selection_006 = _curve_ends_adjust_angle.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_006.name = "Endpoint Selection.006"
			#Start Size
			endpoint_selection_006.inputs[0].default_value = 1
			#End Size
			endpoint_selection_006.inputs[1].default_value = 0
			
			#node Boolean Math.004
			boolean_math_004_1 = _curve_ends_adjust_angle.nodes.new("FunctionNodeBooleanMath")
			boolean_math_004_1.name = "Boolean Math.004"
			boolean_math_004_1.operation = 'AND'
			
			#node Vector Math.011
			vector_math_011 = _curve_ends_adjust_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_011.name = "Vector Math.011"
			vector_math_011.operation = 'SCALE'
			
			#node Vector Math.013
			vector_math_013 = _curve_ends_adjust_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_013.name = "Vector Math.013"
			vector_math_013.operation = 'NORMALIZE'
			
			#node Group
			group_11 = _curve_ends_adjust_angle.nodes.new("GeometryNodeGroup")
			group_11.name = "Group"
			group_11.node_tree = mn_units
			
			#node Vector Math.007
			vector_math_007 = _curve_ends_adjust_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_007.name = "Vector Math.007"
			vector_math_007.operation = 'SUBTRACT'
			
			#node Vector Math.012
			vector_math_012 = _curve_ends_adjust_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_012.name = "Vector Math.012"
			vector_math_012.operation = 'NORMALIZE'
			
			#node Named Attribute
			named_attribute_8 = _curve_ends_adjust_angle.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_8.name = "Named Attribute"
			named_attribute_8.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_8.inputs[0].default_value = "forward"
			
			#node Position
			position_2 = _curve_ends_adjust_angle.nodes.new("GeometryNodeInputPosition")
			position_2.name = "Position"
			
			#node Vector Math
			vector_math_1 = _curve_ends_adjust_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_1.name = "Vector Math"
			vector_math_1.operation = 'SUBTRACT'
			
			#node Vector Math.002
			vector_math_002 = _curve_ends_adjust_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_002.name = "Vector Math.002"
			vector_math_002.hide = True
			vector_math_002.operation = 'NORMALIZE'
			
			#node Group.001
			group_001_4 = _curve_ends_adjust_angle.nodes.new("GeometryNodeGroup")
			group_001_4.name = "Group.001"
			group_001_4.node_tree = mn_units
			#Input_1
			group_001_4.inputs[0].default_value = -2.0
			
			#node Vector Math.003
			vector_math_003 = _curve_ends_adjust_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_003.name = "Vector Math.003"
			vector_math_003.operation = 'SCALE'
			
			#node Group.009
			group_009_1 = _curve_ends_adjust_angle.nodes.new("GeometryNodeGroup")
			group_009_1.name = "Group.009"
			group_009_1.node_tree = _field_offset_vec
			#Input_1
			group_009_1.inputs[1].default_value = 1
			
			#node Vector Math.010
			vector_math_010 = _curve_ends_adjust_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_010.name = "Vector Math.010"
			vector_math_010.operation = 'SUBTRACT'
			
			#node Reroute
			reroute_7 = _curve_ends_adjust_angle.nodes.new("NodeReroute")
			reroute_7.name = "Reroute"
			#node Named Attribute.001
			named_attribute_001_3 = _curve_ends_adjust_angle.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001_3.name = "Named Attribute.001"
			named_attribute_001_3.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_001_3.inputs[0].default_value = "reverse"
			
			#node Position.001
			position_001_1 = _curve_ends_adjust_angle.nodes.new("GeometryNodeInputPosition")
			position_001_1.name = "Position.001"
			
			#node Vector Math.004
			vector_math_004 = _curve_ends_adjust_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_004.name = "Vector Math.004"
			vector_math_004.operation = 'SUBTRACT'
			
			#node Vector Math.005
			vector_math_005 = _curve_ends_adjust_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_005.name = "Vector Math.005"
			vector_math_005.hide = True
			vector_math_005.operation = 'NORMALIZE'
			
			#node Group.002
			group_002_1 = _curve_ends_adjust_angle.nodes.new("GeometryNodeGroup")
			group_002_1.name = "Group.002"
			group_002_1.node_tree = mn_units
			#Input_1
			group_002_1.inputs[0].default_value = -2.0
			
			#node Vector Math.006
			vector_math_006 = _curve_ends_adjust_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_006.name = "Vector Math.006"
			vector_math_006.operation = 'SCALE'
			
			#node Group Output
			group_output_30 = _curve_ends_adjust_angle.nodes.new("NodeGroupOutput")
			group_output_30.name = "Group Output"
			group_output_30.is_active_output = True
			
			#node Set Position
			set_position_2 = _curve_ends_adjust_angle.nodes.new("GeometryNodeSetPosition")
			set_position_2.name = "Set Position"
			#Position
			set_position_2.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Endpoint Selection.008
			endpoint_selection_008 = _curve_ends_adjust_angle.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_008.name = "Endpoint Selection.008"
			#Start Size
			endpoint_selection_008.inputs[0].default_value = 0
			#End Size
			endpoint_selection_008.inputs[1].default_value = 1
			
			#node Group.003
			group_003 = _curve_ends_adjust_angle.nodes.new("GeometryNodeGroup")
			group_003.name = "Group.003"
			group_003.node_tree = _field_offset_vec
			#Input_1
			group_003.inputs[1].default_value = -1
			
			#node Group.019
			group_019 = _curve_ends_adjust_angle.nodes.new("GeometryNodeGroup")
			group_019.name = "Group.019"
			group_019.node_tree = _mn_select_sec_struct
			#Socket_1
			group_019.inputs[0].default_value = True
			
			#node Curve Handle Positions
			curve_handle_positions = _curve_ends_adjust_angle.nodes.new("GeometryNodeInputCurveHandlePositions")
			curve_handle_positions.name = "Curve Handle Positions"
			#Relative
			curve_handle_positions.inputs[0].default_value = False
			
			#node Vector Math.008
			vector_math_008_1 = _curve_ends_adjust_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_008_1.name = "Vector Math.008"
			vector_math_008_1.operation = 'NORMALIZE'
			
			#node Vector Math.009
			vector_math_009 = _curve_ends_adjust_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_009.name = "Vector Math.009"
			vector_math_009.operation = 'SCALE'
			
			#node Endpoint Selection.009
			endpoint_selection_009 = _curve_ends_adjust_angle.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_009.name = "Endpoint Selection.009"
			#Start Size
			endpoint_selection_009.inputs[0].default_value = 1
			#End Size
			endpoint_selection_009.inputs[1].default_value = 1
			
			#node Switch
			switch_7 = _curve_ends_adjust_angle.nodes.new("GeometryNodeSwitch")
			switch_7.name = "Switch"
			switch_7.input_type = 'VECTOR'
			
			#node Group.004
			group_004 = _curve_ends_adjust_angle.nodes.new("GeometryNodeGroup")
			group_004.name = "Group.004"
			group_004.node_tree = mn_units
			
			#node Curve Handle Positions.001
			curve_handle_positions_001 = _curve_ends_adjust_angle.nodes.new("GeometryNodeInputCurveHandlePositions")
			curve_handle_positions_001.name = "Curve Handle Positions.001"
			#Relative
			curve_handle_positions_001.inputs[0].default_value = True
			
			#node Endpoint Selection.010
			endpoint_selection_010 = _curve_ends_adjust_angle.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_010.name = "Endpoint Selection.010"
			#Start Size
			endpoint_selection_010.inputs[0].default_value = 0
			#End Size
			endpoint_selection_010.inputs[1].default_value = 1
			
			#node Set Handle Positions.001
			set_handle_positions_001 = _curve_ends_adjust_angle.nodes.new("GeometryNodeSetCurveHandlePositions")
			set_handle_positions_001.name = "Set Handle Positions.001"
			set_handle_positions_001.mode = 'LEFT'
			#Position
			set_handle_positions_001.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Set Handle Positions
			set_handle_positions = _curve_ends_adjust_angle.nodes.new("GeometryNodeSetCurveHandlePositions")
			set_handle_positions.name = "Set Handle Positions"
			set_handle_positions.mode = 'RIGHT'
			#Position
			set_handle_positions.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Group Input
			group_input_29 = _curve_ends_adjust_angle.nodes.new("NodeGroupInput")
			group_input_29.name = "Group Input"
			
			
			
			
			#Set locations
			vector_math_001.location = (-113.090576171875, -30.316802978515625)
			set_spline_type_001.location = (-457.7088623046875, 134.57489013671875)
			boolean_math_003_2.location = (-393.090576171875, 294.3201599121094)
			reroute_001_3.location = (-440.0, -200.0)
			endpoint_selection_006.location = (-620.0, 280.0)
			boolean_math_004_1.location = (340.0, 380.0)
			vector_math_011.location = (400.0, 80.0)
			vector_math_013.location = (220.0, 80.0)
			group_11.location = (-780.0, 80.0)
			vector_math_007.location = (-300.0, -80.0)
			vector_math_012.location = (-320.0, 40.0)
			named_attribute_8.location = (-1020.0, -80.0)
			position_2.location = (-1020.0, -220.0)
			vector_math_1.location = (-860.0, -140.0)
			vector_math_002.location = (-860.0, -100.0)
			group_001_4.location = (-1020.0, -280.0)
			vector_math_003.location = (-700.0, -100.0)
			group_009_1.location = (71.90267944335938, -263.45281982421875)
			vector_math_010.location = (71.90267944335938, -103.45283508300781)
			reroute_7.location = (-35.006744384765625, -353.1360168457031)
			named_attribute_001_3.location = (311.4145812988281, -130.00930786132812)
			position_001_1.location = (311.4145812988281, -270.0093688964844)
			vector_math_004.location = (471.4145812988281, -190.00936889648438)
			vector_math_005.location = (471.4145812988281, -150.00930786132812)
			group_002_1.location = (311.4145812988281, -330.0093688964844)
			vector_math_006.location = (631.41455078125, -150.00930786132812)
			group_output_30.location = (1649.9193115234375, 169.1092529296875)
			set_position_2.location = (1430.0023193359375, 203.44369506835938)
			endpoint_selection_008.location = (180.0, 400.0)
			group_003.location = (-300.0, -240.0)
			group_019.location = (-620.0, 440.0)
			curve_handle_positions.location = (-780.0, -320.0)
			vector_math_008_1.location = (1330.0, -120.0)
			vector_math_009.location = (1330.0, 20.0)
			endpoint_selection_009.location = (969.6704711914062, 303.7537841796875)
			switch_7.location = (1110.0, -124.58650970458984)
			group_004.location = (1120.0, 0.0)
			curve_handle_positions_001.location = (900.0, -200.0)
			endpoint_selection_010.location = (900.0, -80.0)
			set_handle_positions_001.location = (566.909423828125, 249.68319702148438)
			set_handle_positions.location = (-153.090576171875, 229.68319702148438)
			group_input_29.location = (-1054.2796630859375, 148.32730102539062)
			
			#Set dimensions
			vector_math_001.width, vector_math_001.height = 140.0, 100.0
			set_spline_type_001.width, set_spline_type_001.height = 140.0, 100.0
			boolean_math_003_2.width, boolean_math_003_2.height = 140.0, 100.0
			reroute_001_3.width, reroute_001_3.height = 16.0, 100.0
			endpoint_selection_006.width, endpoint_selection_006.height = 140.0, 100.0
			boolean_math_004_1.width, boolean_math_004_1.height = 140.0, 100.0
			vector_math_011.width, vector_math_011.height = 140.0, 100.0
			vector_math_013.width, vector_math_013.height = 140.0, 100.0
			group_11.width, group_11.height = 140.0, 100.0
			vector_math_007.width, vector_math_007.height = 140.0, 100.0
			vector_math_012.width, vector_math_012.height = 140.0, 100.0
			named_attribute_8.width, named_attribute_8.height = 140.0, 100.0
			position_2.width, position_2.height = 140.0, 100.0
			vector_math_1.width, vector_math_1.height = 140.0, 100.0
			vector_math_002.width, vector_math_002.height = 140.0, 100.0
			group_001_4.width, group_001_4.height = 140.0, 100.0
			vector_math_003.width, vector_math_003.height = 140.0, 100.0
			group_009_1.width, group_009_1.height = 148.385009765625, 100.0
			vector_math_010.width, vector_math_010.height = 140.0, 100.0
			reroute_7.width, reroute_7.height = 16.0, 100.0
			named_attribute_001_3.width, named_attribute_001_3.height = 140.0, 100.0
			position_001_1.width, position_001_1.height = 140.0, 100.0
			vector_math_004.width, vector_math_004.height = 140.0, 100.0
			vector_math_005.width, vector_math_005.height = 140.0, 100.0
			group_002_1.width, group_002_1.height = 140.0, 100.0
			vector_math_006.width, vector_math_006.height = 140.0, 100.0
			group_output_30.width, group_output_30.height = 140.0, 100.0
			set_position_2.width, set_position_2.height = 140.0, 100.0
			endpoint_selection_008.width, endpoint_selection_008.height = 140.0, 100.0
			group_003.width, group_003.height = 148.385009765625, 100.0
			group_019.width, group_019.height = 158.9053955078125, 100.0
			curve_handle_positions.width, curve_handle_positions.height = 150.0, 100.0
			vector_math_008_1.width, vector_math_008_1.height = 140.0, 100.0
			vector_math_009.width, vector_math_009.height = 140.0, 100.0
			endpoint_selection_009.width, endpoint_selection_009.height = 140.0, 100.0
			switch_7.width, switch_7.height = 140.0, 100.0
			group_004.width, group_004.height = 140.0, 100.0
			curve_handle_positions_001.width, curve_handle_positions_001.height = 150.0, 100.0
			endpoint_selection_010.width, endpoint_selection_010.height = 140.0, 100.0
			set_handle_positions_001.width, set_handle_positions_001.height = 140.0, 100.0
			set_handle_positions.width, set_handle_positions.height = 140.0, 100.0
			group_input_29.width, group_input_29.height = 140.0, 100.0
			
			#initialize _curve_ends_adjust_angle links
			#reroute_001_3.Output -> vector_math_007.Vector
			_curve_ends_adjust_angle.links.new(reroute_001_3.outputs[0], vector_math_007.inputs[0])
			#reroute_001_3.Output -> group_003.Field
			_curve_ends_adjust_angle.links.new(reroute_001_3.outputs[0], group_003.inputs[0])
			#group_019.Is Structured -> boolean_math_003_2.Boolean
			_curve_ends_adjust_angle.links.new(group_019.outputs[2], boolean_math_003_2.inputs[1])
			#boolean_math_003_2.Boolean -> set_handle_positions.Selection
			_curve_ends_adjust_angle.links.new(boolean_math_003_2.outputs[0], set_handle_positions.inputs[1])
			#group_019.Is Structured -> boolean_math_004_1.Boolean
			_curve_ends_adjust_angle.links.new(group_019.outputs[2], boolean_math_004_1.inputs[1])
			#set_spline_type_001.Curve -> set_handle_positions.Curve
			_curve_ends_adjust_angle.links.new(set_spline_type_001.outputs[0], set_handle_positions.inputs[0])
			#vector_math_010.Vector -> vector_math_013.Vector
			_curve_ends_adjust_angle.links.new(vector_math_010.outputs[0], vector_math_013.inputs[0])
			#endpoint_selection_006.Selection -> boolean_math_003_2.Boolean
			_curve_ends_adjust_angle.links.new(endpoint_selection_006.outputs[0], boolean_math_003_2.inputs[0])
			#reroute_7.Output -> group_009_1.Field
			_curve_ends_adjust_angle.links.new(reroute_7.outputs[0], group_009_1.inputs[0])
			#vector_math_007.Vector -> vector_math_012.Vector
			_curve_ends_adjust_angle.links.new(vector_math_007.outputs[0], vector_math_012.inputs[0])
			#endpoint_selection_008.Selection -> boolean_math_004_1.Boolean
			_curve_ends_adjust_angle.links.new(endpoint_selection_008.outputs[0], boolean_math_004_1.inputs[0])
			#group_11.Angstrom -> vector_math_011.Scale
			_curve_ends_adjust_angle.links.new(group_11.outputs[0], vector_math_011.inputs[3])
			#reroute_7.Output -> vector_math_010.Vector
			_curve_ends_adjust_angle.links.new(reroute_7.outputs[0], vector_math_010.inputs[0])
			#vector_math_013.Vector -> vector_math_011.Vector
			_curve_ends_adjust_angle.links.new(vector_math_013.outputs[0], vector_math_011.inputs[0])
			#group_009_1.Field -> vector_math_010.Vector
			_curve_ends_adjust_angle.links.new(group_009_1.outputs[0], vector_math_010.inputs[1])
			#vector_math_012.Vector -> vector_math_001.Vector
			_curve_ends_adjust_angle.links.new(vector_math_012.outputs[0], vector_math_001.inputs[0])
			#set_handle_positions.Curve -> set_handle_positions_001.Curve
			_curve_ends_adjust_angle.links.new(set_handle_positions.outputs[0], set_handle_positions_001.inputs[0])
			#group_003.Field -> vector_math_007.Vector
			_curve_ends_adjust_angle.links.new(group_003.outputs[0], vector_math_007.inputs[1])
			#boolean_math_004_1.Boolean -> set_handle_positions_001.Selection
			_curve_ends_adjust_angle.links.new(boolean_math_004_1.outputs[0], set_handle_positions_001.inputs[1])
			#group_11.Angstrom -> vector_math_001.Scale
			_curve_ends_adjust_angle.links.new(group_11.outputs[0], vector_math_001.inputs[3])
			#group_input_29.Curve -> set_spline_type_001.Curve
			_curve_ends_adjust_angle.links.new(group_input_29.outputs[0], set_spline_type_001.inputs[0])
			#set_position_2.Geometry -> group_output_30.Curve
			_curve_ends_adjust_angle.links.new(set_position_2.outputs[0], group_output_30.inputs[0])
			#group_input_29.Distance -> group_11.Value
			_curve_ends_adjust_angle.links.new(group_input_29.outputs[1], group_11.inputs[0])
			#curve_handle_positions.Right -> reroute_7.Input
			_curve_ends_adjust_angle.links.new(curve_handle_positions.outputs[1], reroute_7.inputs[0])
			#curve_handle_positions.Left -> reroute_001_3.Input
			_curve_ends_adjust_angle.links.new(curve_handle_positions.outputs[0], reroute_001_3.inputs[0])
			#named_attribute_8.Attribute -> vector_math_1.Vector
			_curve_ends_adjust_angle.links.new(named_attribute_8.outputs[0], vector_math_1.inputs[0])
			#position_2.Position -> vector_math_1.Vector
			_curve_ends_adjust_angle.links.new(position_2.outputs[0], vector_math_1.inputs[1])
			#vector_math_1.Vector -> vector_math_002.Vector
			_curve_ends_adjust_angle.links.new(vector_math_1.outputs[0], vector_math_002.inputs[0])
			#vector_math_002.Vector -> vector_math_003.Vector
			_curve_ends_adjust_angle.links.new(vector_math_002.outputs[0], vector_math_003.inputs[0])
			#group_001_4.Angstrom -> vector_math_003.Scale
			_curve_ends_adjust_angle.links.new(group_001_4.outputs[0], vector_math_003.inputs[3])
			#vector_math_003.Vector -> set_handle_positions.Offset
			_curve_ends_adjust_angle.links.new(vector_math_003.outputs[0], set_handle_positions.inputs[3])
			#named_attribute_001_3.Attribute -> vector_math_004.Vector
			_curve_ends_adjust_angle.links.new(named_attribute_001_3.outputs[0], vector_math_004.inputs[0])
			#position_001_1.Position -> vector_math_004.Vector
			_curve_ends_adjust_angle.links.new(position_001_1.outputs[0], vector_math_004.inputs[1])
			#vector_math_004.Vector -> vector_math_005.Vector
			_curve_ends_adjust_angle.links.new(vector_math_004.outputs[0], vector_math_005.inputs[0])
			#vector_math_005.Vector -> vector_math_006.Vector
			_curve_ends_adjust_angle.links.new(vector_math_005.outputs[0], vector_math_006.inputs[0])
			#group_002_1.Angstrom -> vector_math_006.Scale
			_curve_ends_adjust_angle.links.new(group_002_1.outputs[0], vector_math_006.inputs[3])
			#vector_math_006.Vector -> set_handle_positions_001.Offset
			_curve_ends_adjust_angle.links.new(vector_math_006.outputs[0], set_handle_positions_001.inputs[3])
			#set_handle_positions_001.Curve -> set_position_2.Geometry
			_curve_ends_adjust_angle.links.new(set_handle_positions_001.outputs[0], set_position_2.inputs[0])
			#endpoint_selection_009.Selection -> set_position_2.Selection
			_curve_ends_adjust_angle.links.new(endpoint_selection_009.outputs[0], set_position_2.inputs[1])
			#vector_math_008_1.Vector -> vector_math_009.Vector
			_curve_ends_adjust_angle.links.new(vector_math_008_1.outputs[0], vector_math_009.inputs[0])
			#group_004.Angstrom -> vector_math_009.Scale
			_curve_ends_adjust_angle.links.new(group_004.outputs[0], vector_math_009.inputs[3])
			#vector_math_009.Vector -> set_position_2.Offset
			_curve_ends_adjust_angle.links.new(vector_math_009.outputs[0], set_position_2.inputs[3])
			#curve_handle_positions_001.Left -> switch_7.False
			_curve_ends_adjust_angle.links.new(curve_handle_positions_001.outputs[0], switch_7.inputs[1])
			#switch_7.Output -> vector_math_008_1.Vector
			_curve_ends_adjust_angle.links.new(switch_7.outputs[0], vector_math_008_1.inputs[0])
			#curve_handle_positions_001.Right -> switch_7.True
			_curve_ends_adjust_angle.links.new(curve_handle_positions_001.outputs[1], switch_7.inputs[2])
			#endpoint_selection_010.Selection -> switch_7.Switch
			_curve_ends_adjust_angle.links.new(endpoint_selection_010.outputs[0], switch_7.inputs[0])
			#group_input_29.Distance -> group_004.Value
			_curve_ends_adjust_angle.links.new(group_input_29.outputs[2], group_004.inputs[0])
			return _curve_ends_adjust_angle

		_curve_ends_adjust_angle = _curve_ends_adjust_angle_node_group()

		#initialize _curve_ends_adjust_position node group
		def _curve_ends_adjust_position_node_group():
			_curve_ends_adjust_position = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "_curve_ends_adjust_position")

			_curve_ends_adjust_position.color_tag = 'NONE'
			_curve_ends_adjust_position.description = ""

			_curve_ends_adjust_position.is_modifier = True
			
			#_curve_ends_adjust_position interface
			#Socket Geometry
			geometry_socket_4 = _curve_ends_adjust_position.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_4.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_5 = _curve_ends_adjust_position.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_5.attribute_domain = 'POINT'
			
			#Socket Distance
			distance_socket_2 = _curve_ends_adjust_position.interface.new_socket(name = "Distance", in_out='INPUT', socket_type = 'NodeSocketFloat')
			distance_socket_2.subtype = 'NONE'
			distance_socket_2.default_value = 0.30000001192092896
			distance_socket_2.min_value = -10000.0
			distance_socket_2.max_value = 10000.0
			distance_socket_2.attribute_domain = 'POINT'
			
			
			#initialize _curve_ends_adjust_position nodes
			#node Position
			position_3 = _curve_ends_adjust_position.nodes.new("GeometryNodeInputPosition")
			position_3.name = "Position"
			
			#node Group.026
			group_026_1 = _curve_ends_adjust_position.nodes.new("GeometryNodeGroup")
			group_026_1.name = "Group.026"
			group_026_1.node_tree = _field_offset_vec
			#Input_1
			group_026_1.inputs[1].default_value = -1
			
			#node Group.027
			group_027 = _curve_ends_adjust_position.nodes.new("GeometryNodeGroup")
			group_027.name = "Group.027"
			group_027.node_tree = _field_offset_vec
			#Input_1
			group_027.inputs[1].default_value = 1
			
			#node Vector Math.008
			vector_math_008_2 = _curve_ends_adjust_position.nodes.new("ShaderNodeVectorMath")
			vector_math_008_2.name = "Vector Math.008"
			vector_math_008_2.operation = 'SUBTRACT'
			
			#node Endpoint Selection.002
			endpoint_selection_002 = _curve_ends_adjust_position.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_002.name = "Endpoint Selection.002"
			#Start Size
			endpoint_selection_002.inputs[0].default_value = 0
			#End Size
			endpoint_selection_002.inputs[1].default_value = 1
			
			#node Switch.007
			switch_007 = _curve_ends_adjust_position.nodes.new("GeometryNodeSwitch")
			switch_007.name = "Switch.007"
			switch_007.input_type = 'VECTOR'
			#False
			switch_007.inputs[1].default_value = (0.0, 0.0, 0.0)
			
			#node Vector Math.009
			vector_math_009_1 = _curve_ends_adjust_position.nodes.new("ShaderNodeVectorMath")
			vector_math_009_1.name = "Vector Math.009"
			vector_math_009_1.operation = 'SUBTRACT'
			
			#node Endpoint Selection.001
			endpoint_selection_001 = _curve_ends_adjust_position.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_001.name = "Endpoint Selection.001"
			#Start Size
			endpoint_selection_001.inputs[0].default_value = 1
			#End Size
			endpoint_selection_001.inputs[1].default_value = 0
			
			#node Group Output
			group_output_31 = _curve_ends_adjust_position.nodes.new("NodeGroupOutput")
			group_output_31.name = "Group Output"
			group_output_31.is_active_output = True
			
			#node Group Input
			group_input_30 = _curve_ends_adjust_position.nodes.new("NodeGroupInput")
			group_input_30.name = "Group Input"
			
			#node Switch.010
			switch_010 = _curve_ends_adjust_position.nodes.new("GeometryNodeSwitch")
			switch_010.name = "Switch.010"
			switch_010.input_type = 'VECTOR'
			
			#node Vector Math
			vector_math_2 = _curve_ends_adjust_position.nodes.new("ShaderNodeVectorMath")
			vector_math_2.name = "Vector Math"
			vector_math_2.operation = 'NORMALIZE'
			
			#node Vector Math.003
			vector_math_003_1 = _curve_ends_adjust_position.nodes.new("ShaderNodeVectorMath")
			vector_math_003_1.name = "Vector Math.003"
			vector_math_003_1.operation = 'SCALE'
			
			#node Set Position.001
			set_position_001 = _curve_ends_adjust_position.nodes.new("GeometryNodeSetPosition")
			set_position_001.name = "Set Position.001"
			#Selection
			set_position_001.inputs[1].default_value = True
			#Position
			set_position_001.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Group.023
			group_023 = _curve_ends_adjust_position.nodes.new("GeometryNodeGroup")
			group_023.name = "Group.023"
			group_023.node_tree = mn_units
			
			
			
			
			#Set locations
			position_3.location = (-345.67303466796875, 21.96319580078125)
			group_026_1.location = (-165.67303466796875, -38.03680419921875)
			group_027.location = (-165.67303466796875, -318.03680419921875)
			vector_math_008_2.location = (-165.67303466796875, 101.96319580078125)
			endpoint_selection_002.location = (-365.67303466796875, -178.03680419921875)
			switch_007.location = (-5.67303466796875, 101.96319580078125)
			vector_math_009_1.location = (-165.67303466796875, -178.03680419921875)
			endpoint_selection_001.location = (-345.67303466796875, 141.96319580078125)
			group_output_31.location = (867.47216796875, 3.8314287662506104)
			group_input_30.location = (-500.0, 280.0)
			switch_010.location = (154.32696533203125, 101.96319580078125)
			vector_math_2.location = (300.0, 100.0)
			vector_math_003_1.location = (626.1260986328125, 105.79462432861328)
			set_position_001.location = (677.47216796875, 321.86822509765625)
			group_023.location = (154.32696533203125, -58.03680419921875)
			
			#Set dimensions
			position_3.width, position_3.height = 140.0, 100.0
			group_026_1.width, group_026_1.height = 140.0, 100.0
			group_027.width, group_027.height = 140.0, 100.0
			vector_math_008_2.width, vector_math_008_2.height = 140.0, 100.0
			endpoint_selection_002.width, endpoint_selection_002.height = 140.0, 100.0
			switch_007.width, switch_007.height = 140.0, 100.0
			vector_math_009_1.width, vector_math_009_1.height = 140.0, 100.0
			endpoint_selection_001.width, endpoint_selection_001.height = 140.0, 100.0
			group_output_31.width, group_output_31.height = 140.0, 100.0
			group_input_30.width, group_input_30.height = 140.0, 100.0
			switch_010.width, switch_010.height = 140.0, 100.0
			vector_math_2.width, vector_math_2.height = 140.0, 100.0
			vector_math_003_1.width, vector_math_003_1.height = 140.0, 100.0
			set_position_001.width, set_position_001.height = 140.0, 100.0
			group_023.width, group_023.height = 140.0, 100.0
			
			#initialize _curve_ends_adjust_position links
			#group_023.Angstrom -> vector_math_003_1.Scale
			_curve_ends_adjust_position.links.new(group_023.outputs[0], vector_math_003_1.inputs[3])
			#endpoint_selection_001.Selection -> switch_007.Switch
			_curve_ends_adjust_position.links.new(endpoint_selection_001.outputs[0], switch_007.inputs[0])
			#position_3.Position -> group_027.Field
			_curve_ends_adjust_position.links.new(position_3.outputs[0], group_027.inputs[0])
			#vector_math_008_2.Vector -> switch_007.True
			_curve_ends_adjust_position.links.new(vector_math_008_2.outputs[0], switch_007.inputs[2])
			#position_3.Position -> vector_math_009_1.Vector
			_curve_ends_adjust_position.links.new(position_3.outputs[0], vector_math_009_1.inputs[1])
			#position_3.Position -> vector_math_008_2.Vector
			_curve_ends_adjust_position.links.new(position_3.outputs[0], vector_math_008_2.inputs[1])
			#vector_math_009_1.Vector -> switch_010.True
			_curve_ends_adjust_position.links.new(vector_math_009_1.outputs[0], switch_010.inputs[2])
			#position_3.Position -> group_026_1.Field
			_curve_ends_adjust_position.links.new(position_3.outputs[0], group_026_1.inputs[0])
			#vector_math_003_1.Vector -> set_position_001.Offset
			_curve_ends_adjust_position.links.new(vector_math_003_1.outputs[0], set_position_001.inputs[3])
			#group_027.Field -> vector_math_009_1.Vector
			_curve_ends_adjust_position.links.new(group_027.outputs[0], vector_math_009_1.inputs[0])
			#switch_007.Output -> switch_010.False
			_curve_ends_adjust_position.links.new(switch_007.outputs[0], switch_010.inputs[1])
			#endpoint_selection_002.Selection -> switch_010.Switch
			_curve_ends_adjust_position.links.new(endpoint_selection_002.outputs[0], switch_010.inputs[0])
			#group_026_1.Field -> vector_math_008_2.Vector
			_curve_ends_adjust_position.links.new(group_026_1.outputs[0], vector_math_008_2.inputs[0])
			#group_input_30.Geometry -> set_position_001.Geometry
			_curve_ends_adjust_position.links.new(group_input_30.outputs[0], set_position_001.inputs[0])
			#set_position_001.Geometry -> group_output_31.Geometry
			_curve_ends_adjust_position.links.new(set_position_001.outputs[0], group_output_31.inputs[0])
			#switch_010.Output -> vector_math_2.Vector
			_curve_ends_adjust_position.links.new(switch_010.outputs[0], vector_math_2.inputs[0])
			#vector_math_2.Vector -> vector_math_003_1.Vector
			_curve_ends_adjust_position.links.new(vector_math_2.outputs[0], vector_math_003_1.inputs[0])
			#group_input_30.Distance -> group_023.Value
			_curve_ends_adjust_position.links.new(group_input_30.outputs[1], group_023.inputs[0])
			return _curve_ends_adjust_position

		_curve_ends_adjust_position = _curve_ends_adjust_position_node_group()

		#initialize _curve_to_mesh node group
		def _curve_to_mesh_node_group():
			_curve_to_mesh = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".curve_to_mesh")

			_curve_to_mesh.color_tag = 'NONE'
			_curve_to_mesh.description = ""

			_curve_to_mesh.is_modifier = True
			
			#_curve_to_mesh interface
			#Socket Mesh
			mesh_socket = _curve_to_mesh.interface.new_socket(name = "Mesh", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			mesh_socket.attribute_domain = 'POINT'
			
			#Socket Curve
			curve_socket_2 = _curve_to_mesh.interface.new_socket(name = "Curve", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			curve_socket_2.attribute_domain = 'POINT'
			
			#Socket Profile Curve
			profile_curve_socket = _curve_to_mesh.interface.new_socket(name = "Profile Curve", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			profile_curve_socket.attribute_domain = 'POINT'
			
			#Socket Resolution
			resolution_socket_1 = _curve_to_mesh.interface.new_socket(name = "Resolution", in_out='INPUT', socket_type = 'NodeSocketInt')
			resolution_socket_1.subtype = 'NONE'
			resolution_socket_1.default_value = 12
			resolution_socket_1.min_value = 3
			resolution_socket_1.max_value = 512
			resolution_socket_1.attribute_domain = 'POINT'
			
			#Socket Fill Caps
			fill_caps_socket_1 = _curve_to_mesh.interface.new_socket(name = "Fill Caps", in_out='INPUT', socket_type = 'NodeSocketBool')
			fill_caps_socket_1.attribute_domain = 'POINT'
			
			#Socket Radius (A)
			radius__a__socket = _curve_to_mesh.interface.new_socket(name = "Radius (A)", in_out='INPUT', socket_type = 'NodeSocketFloat')
			radius__a__socket.subtype = 'NONE'
			radius__a__socket.default_value = 0.20000000298023224
			radius__a__socket.min_value = 0.0
			radius__a__socket.max_value = 10000.0
			radius__a__socket.attribute_domain = 'POINT'
			
			
			#initialize _curve_to_mesh nodes
			#node Group Output
			group_output_32 = _curve_to_mesh.nodes.new("NodeGroupOutput")
			group_output_32.name = "Group Output"
			group_output_32.is_active_output = True
			
			#node Curve to Mesh
			curve_to_mesh_1 = _curve_to_mesh.nodes.new("GeometryNodeCurveToMesh")
			curve_to_mesh_1.name = "Curve to Mesh"
			
			#node Group
			group_12 = _curve_to_mesh.nodes.new("GeometryNodeGroup")
			group_12.name = "Group"
			group_12.node_tree = mn_units
			
			#node Curve Circle
			curve_circle_1 = _curve_to_mesh.nodes.new("GeometryNodeCurvePrimitiveCircle")
			curve_circle_1.name = "Curve Circle"
			curve_circle_1.mode = 'RADIUS'
			#Radius
			curve_circle_1.inputs[4].default_value = 1.0
			
			#node Domain Size
			domain_size_2 = _curve_to_mesh.nodes.new("GeometryNodeAttributeDomainSize")
			domain_size_2.name = "Domain Size"
			domain_size_2.component = 'CURVE'
			
			#node Compare
			compare_7 = _curve_to_mesh.nodes.new("FunctionNodeCompare")
			compare_7.name = "Compare"
			compare_7.data_type = 'INT'
			compare_7.mode = 'ELEMENT'
			compare_7.operation = 'EQUAL'
			#B_INT
			compare_7.inputs[3].default_value = 0
			
			#node Switch
			switch_8 = _curve_to_mesh.nodes.new("GeometryNodeSwitch")
			switch_8.name = "Switch"
			switch_8.input_type = 'GEOMETRY'
			
			#node Group Input
			group_input_31 = _curve_to_mesh.nodes.new("NodeGroupInput")
			group_input_31.name = "Group Input"
			
			#node Set Curve Radius
			set_curve_radius_1 = _curve_to_mesh.nodes.new("GeometryNodeSetCurveRadius")
			set_curve_radius_1.name = "Set Curve Radius"
			#Selection
			set_curve_radius_1.inputs[1].default_value = True
			
			
			
			
			#Set locations
			group_output_32.location = (190.0, 0.0)
			curve_to_mesh_1.location = (0.0, 0.0)
			group_12.location = (-577.7610473632812, -122.98338317871094)
			curve_circle_1.location = (-260.0, 40.0)
			domain_size_2.location = (-780.0, 120.0)
			compare_7.location = (-780.0, 280.0)
			switch_8.location = (-377.0369873046875, 349.30694580078125)
			group_input_31.location = (-780.0, -40.0)
			set_curve_radius_1.location = (-260.0, 180.0)
			
			#Set dimensions
			group_output_32.width, group_output_32.height = 140.0, 100.0
			curve_to_mesh_1.width, curve_to_mesh_1.height = 140.0, 100.0
			group_12.width, group_12.height = 261.9884033203125, 100.0
			curve_circle_1.width, curve_circle_1.height = 140.0, 100.0
			domain_size_2.width, domain_size_2.height = 140.0, 100.0
			compare_7.width, compare_7.height = 140.0, 100.0
			switch_8.width, switch_8.height = 140.0, 100.0
			group_input_31.width, group_input_31.height = 140.0, 100.0
			set_curve_radius_1.width, set_curve_radius_1.height = 140.0, 100.0
			
			#initialize _curve_to_mesh links
			#set_curve_radius_1.Curve -> curve_to_mesh_1.Curve
			_curve_to_mesh.links.new(set_curve_radius_1.outputs[0], curve_to_mesh_1.inputs[0])
			#curve_to_mesh_1.Mesh -> group_output_32.Mesh
			_curve_to_mesh.links.new(curve_to_mesh_1.outputs[0], group_output_32.inputs[0])
			#group_input_31.Fill Caps -> curve_to_mesh_1.Fill Caps
			_curve_to_mesh.links.new(group_input_31.outputs[3], curve_to_mesh_1.inputs[2])
			#group_input_31.Curve -> set_curve_radius_1.Curve
			_curve_to_mesh.links.new(group_input_31.outputs[0], set_curve_radius_1.inputs[0])
			#group_12.Angstrom -> set_curve_radius_1.Radius
			_curve_to_mesh.links.new(group_12.outputs[0], set_curve_radius_1.inputs[2])
			#group_input_31.Radius (A) -> group_12.Value
			_curve_to_mesh.links.new(group_input_31.outputs[4], group_12.inputs[0])
			#group_input_31.Resolution -> curve_circle_1.Resolution
			_curve_to_mesh.links.new(group_input_31.outputs[2], curve_circle_1.inputs[0])
			#group_input_31.Profile Curve -> domain_size_2.Geometry
			_curve_to_mesh.links.new(group_input_31.outputs[1], domain_size_2.inputs[0])
			#domain_size_2.Point Count -> compare_7.A
			_curve_to_mesh.links.new(domain_size_2.outputs[0], compare_7.inputs[2])
			#compare_7.Result -> switch_8.Switch
			_curve_to_mesh.links.new(compare_7.outputs[0], switch_8.inputs[0])
			#curve_circle_1.Curve -> switch_8.True
			_curve_to_mesh.links.new(curve_circle_1.outputs[0], switch_8.inputs[2])
			#switch_8.Output -> curve_to_mesh_1.Profile Curve
			_curve_to_mesh.links.new(switch_8.outputs[0], curve_to_mesh_1.inputs[1])
			#group_input_31.Profile Curve -> switch_8.False
			_curve_to_mesh.links.new(group_input_31.outputs[1], switch_8.inputs[1])
			return _curve_to_mesh

		_curve_to_mesh = _curve_to_mesh_node_group()

		#initialize offset_color node group
		def offset_color_node_group():
			offset_color = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Offset Color")

			offset_color.color_tag = 'NONE'
			offset_color.description = ""

			
			#offset_color interface
			#Socket Color
			color_socket = offset_color.interface.new_socket(name = "Color", in_out='OUTPUT', socket_type = 'NodeSocketColor')
			color_socket.attribute_domain = 'POINT'
			
			#Socket Index
			index_socket = offset_color.interface.new_socket(name = "Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			index_socket.subtype = 'NONE'
			index_socket.default_value = 0
			index_socket.min_value = -2147483648
			index_socket.max_value = 2147483647
			index_socket.attribute_domain = 'POINT'
			
			#Socket Offset
			offset_socket_2 = offset_color.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket_2.subtype = 'NONE'
			offset_socket_2.default_value = 0
			offset_socket_2.min_value = -2147483648
			offset_socket_2.max_value = 2147483647
			offset_socket_2.attribute_domain = 'POINT'
			
			
			#initialize offset_color nodes
			#node Group Input
			group_input_32 = offset_color.nodes.new("NodeGroupInput")
			group_input_32.name = "Group Input"
			
			#node Math.012
			math_012 = offset_color.nodes.new("ShaderNodeMath")
			math_012.name = "Math.012"
			math_012.operation = 'ADD'
			math_012.use_clamp = False
			
			#node Evaluate at Index.004
			evaluate_at_index_004 = offset_color.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_004.name = "Evaluate at Index.004"
			evaluate_at_index_004.data_type = 'FLOAT_COLOR'
			evaluate_at_index_004.domain = 'POINT'
			
			#node Group Output
			group_output_33 = offset_color.nodes.new("NodeGroupOutput")
			group_output_33.name = "Group Output"
			group_output_33.is_active_output = True
			
			#node Named Attribute
			named_attribute_9 = offset_color.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_9.name = "Named Attribute"
			named_attribute_9.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute_9.inputs[0].default_value = "Color"
			
			
			
			
			#Set locations
			group_input_32.location = (-220.0, -20.0)
			math_012.location = (-40.0, 0.0)
			evaluate_at_index_004.location = (140.0, 0.0)
			group_output_33.location = (340.0, 0.0)
			named_attribute_9.location = (-40.0, -160.0)
			
			#Set dimensions
			group_input_32.width, group_input_32.height = 140.0, 100.0
			math_012.width, math_012.height = 140.0, 100.0
			evaluate_at_index_004.width, evaluate_at_index_004.height = 140.0, 100.0
			group_output_33.width, group_output_33.height = 140.0, 100.0
			named_attribute_9.width, named_attribute_9.height = 140.0, 100.0
			
			#initialize offset_color links
			#math_012.Value -> evaluate_at_index_004.Index
			offset_color.links.new(math_012.outputs[0], evaluate_at_index_004.inputs[0])
			#group_input_32.Offset -> math_012.Value
			offset_color.links.new(group_input_32.outputs[1], math_012.inputs[1])
			#evaluate_at_index_004.Value -> group_output_33.Color
			offset_color.links.new(evaluate_at_index_004.outputs[0], group_output_33.inputs[0])
			#named_attribute_9.Attribute -> evaluate_at_index_004.Value
			offset_color.links.new(named_attribute_9.outputs[0], evaluate_at_index_004.inputs[1])
			#group_input_32.Index -> math_012.Value
			offset_color.links.new(group_input_32.outputs[0], math_012.inputs[0])
			return offset_color

		offset_color = offset_color_node_group()

		#initialize _curve_end_fix_color node group
		def _curve_end_fix_color_node_group():
			_curve_end_fix_color = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".curve_end_fix_color")

			_curve_end_fix_color.color_tag = 'NONE'
			_curve_end_fix_color.description = ""

			_curve_end_fix_color.is_modifier = True
			
			#_curve_end_fix_color interface
			#Socket Geometry
			geometry_socket_6 = _curve_end_fix_color.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_6.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_7 = _curve_end_fix_color.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_7.attribute_domain = 'POINT'
			
			
			#initialize _curve_end_fix_color nodes
			#node Store Named Attribute
			store_named_attribute_4 = _curve_end_fix_color.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_4.name = "Store Named Attribute"
			store_named_attribute_4.data_type = 'FLOAT_COLOR'
			store_named_attribute_4.domain = 'POINT'
			#Name
			store_named_attribute_4.inputs[2].default_value = "Color"
			
			#node Switch.011
			switch_011 = _curve_end_fix_color.nodes.new("GeometryNodeSwitch")
			switch_011.name = "Switch.011"
			switch_011.input_type = 'RGBA'
			
			#node Group.029
			group_029 = _curve_end_fix_color.nodes.new("GeometryNodeGroup")
			group_029.name = "Group.029"
			group_029.node_tree = offset_color
			#Socket_0
			group_029.inputs[0].default_value = 0
			#Input_0
			group_029.inputs[1].default_value = -1
			
			#node Endpoint Selection.004
			endpoint_selection_004 = _curve_end_fix_color.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_004.name = "Endpoint Selection.004"
			#Start Size
			endpoint_selection_004.inputs[0].default_value = 0
			#End Size
			endpoint_selection_004.inputs[1].default_value = 1
			
			#node Endpoint Selection.003
			endpoint_selection_003 = _curve_end_fix_color.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_003.name = "Endpoint Selection.003"
			#Start Size
			endpoint_selection_003.inputs[0].default_value = 1
			#End Size
			endpoint_selection_003.inputs[1].default_value = 0
			
			#node Group.028
			group_028 = _curve_end_fix_color.nodes.new("GeometryNodeGroup")
			group_028.name = "Group.028"
			group_028.node_tree = offset_color
			#Socket_0
			group_028.inputs[0].default_value = 0
			#Input_0
			group_028.inputs[1].default_value = 1
			
			#node Switch.012
			switch_012 = _curve_end_fix_color.nodes.new("GeometryNodeSwitch")
			switch_012.name = "Switch.012"
			switch_012.input_type = 'RGBA'
			
			#node Named Attribute.001
			named_attribute_001_4 = _curve_end_fix_color.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001_4.name = "Named Attribute.001"
			named_attribute_001_4.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute_001_4.inputs[0].default_value = "Color"
			
			#node Group.030
			group_030 = _curve_end_fix_color.nodes.new("GeometryNodeGroup")
			group_030.name = "Group.030"
			group_030.node_tree = _mn_select_sec_struct
			#Socket_1
			group_030.inputs[0].default_value = True
			
			#node Group Output
			group_output_34 = _curve_end_fix_color.nodes.new("NodeGroupOutput")
			group_output_34.name = "Group Output"
			group_output_34.is_active_output = True
			
			#node Group Input
			group_input_33 = _curve_end_fix_color.nodes.new("NodeGroupInput")
			group_input_33.name = "Group Input"
			
			
			
			
			#Set locations
			store_named_attribute_4.location = (180.0, 270.0)
			switch_011.location = (-20.0, -110.0)
			group_029.location = (160.0, -270.0)
			endpoint_selection_004.location = (160.0, 10.0)
			endpoint_selection_003.location = (-20.0, 10.0)
			group_028.location = (-20.0, -270.0)
			switch_012.location = (160.0, -110.0)
			named_attribute_001_4.location = (-180.0, -250.0)
			group_030.location = (-60.0, 190.0)
			group_output_34.location = (360.0, 320.0)
			group_input_33.location = (-40.0, 300.0)
			
			#Set dimensions
			store_named_attribute_4.width, store_named_attribute_4.height = 140.0, 100.0
			switch_011.width, switch_011.height = 140.0, 100.0
			group_029.width, group_029.height = 140.0, 100.0
			endpoint_selection_004.width, endpoint_selection_004.height = 140.0, 100.0
			endpoint_selection_003.width, endpoint_selection_003.height = 140.0, 100.0
			group_028.width, group_028.height = 140.0, 100.0
			switch_012.width, switch_012.height = 140.0, 100.0
			named_attribute_001_4.width, named_attribute_001_4.height = 140.0, 100.0
			group_030.width, group_030.height = 158.9053955078125, 100.0
			group_output_34.width, group_output_34.height = 140.0, 100.0
			group_input_33.width, group_input_33.height = 140.0, 100.0
			
			#initialize _curve_end_fix_color links
			#switch_011.Output -> switch_012.False
			_curve_end_fix_color.links.new(switch_011.outputs[0], switch_012.inputs[1])
			#named_attribute_001_4.Attribute -> switch_011.False
			_curve_end_fix_color.links.new(named_attribute_001_4.outputs[0], switch_011.inputs[1])
			#endpoint_selection_003.Selection -> switch_011.Switch
			_curve_end_fix_color.links.new(endpoint_selection_003.outputs[0], switch_011.inputs[0])
			#group_028.Color -> switch_011.True
			_curve_end_fix_color.links.new(group_028.outputs[0], switch_011.inputs[2])
			#group_029.Color -> switch_012.True
			_curve_end_fix_color.links.new(group_029.outputs[0], switch_012.inputs[2])
			#switch_012.Output -> store_named_attribute_4.Value
			_curve_end_fix_color.links.new(switch_012.outputs[0], store_named_attribute_4.inputs[3])
			#group_030.Is Structured -> store_named_attribute_4.Selection
			_curve_end_fix_color.links.new(group_030.outputs[2], store_named_attribute_4.inputs[1])
			#endpoint_selection_004.Selection -> switch_012.Switch
			_curve_end_fix_color.links.new(endpoint_selection_004.outputs[0], switch_012.inputs[0])
			#group_input_33.Geometry -> store_named_attribute_4.Geometry
			_curve_end_fix_color.links.new(group_input_33.outputs[0], store_named_attribute_4.inputs[0])
			#store_named_attribute_4.Geometry -> group_output_34.Geometry
			_curve_end_fix_color.links.new(store_named_attribute_4.outputs[0], group_output_34.inputs[0])
			return _curve_end_fix_color

		_curve_end_fix_color = _curve_end_fix_color_node_group()

		#initialize _mn_cartoon_smooth_handles node group
		def _mn_cartoon_smooth_handles_node_group():
			_mn_cartoon_smooth_handles = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_cartoon_smooth_handles")

			_mn_cartoon_smooth_handles.color_tag = 'NONE'
			_mn_cartoon_smooth_handles.description = ""

			
			#_mn_cartoon_smooth_handles interface
			#Socket Vector
			vector_socket = _mn_cartoon_smooth_handles.interface.new_socket(name = "Vector", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			vector_socket.subtype = 'NONE'
			vector_socket.default_value = (0.0, 0.0, 0.0)
			vector_socket.min_value = -3.4028234663852886e+38
			vector_socket.max_value = 3.4028234663852886e+38
			vector_socket.attribute_domain = 'POINT'
			
			#Socket Scale
			scale_socket_2 = _mn_cartoon_smooth_handles.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
			scale_socket_2.subtype = 'NONE'
			scale_socket_2.default_value = 0.00800000037997961
			scale_socket_2.min_value = -10000.0
			scale_socket_2.max_value = 10000.0
			scale_socket_2.attribute_domain = 'POINT'
			
			
			#initialize _mn_cartoon_smooth_handles nodes
			#node Vector Math.005
			vector_math_005_1 = _mn_cartoon_smooth_handles.nodes.new("ShaderNodeVectorMath")
			vector_math_005_1.name = "Vector Math.005"
			vector_math_005_1.operation = 'NORMALIZE'
			
			#node Named Attribute.004
			named_attribute_004_1 = _mn_cartoon_smooth_handles.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_004_1.name = "Named Attribute.004"
			named_attribute_004_1.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_004_1.inputs[0].default_value = "guide_X"
			
			#node Vector Math.006
			vector_math_006_1 = _mn_cartoon_smooth_handles.nodes.new("ShaderNodeVectorMath")
			vector_math_006_1.name = "Vector Math.006"
			vector_math_006_1.operation = 'NORMALIZE'
			
			#node Named Attribute.003
			named_attribute_003_1 = _mn_cartoon_smooth_handles.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_003_1.name = "Named Attribute.003"
			named_attribute_003_1.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_003_1.inputs[0].default_value = "guide_Z"
			
			#node Vector Math.007
			vector_math_007_1 = _mn_cartoon_smooth_handles.nodes.new("ShaderNodeVectorMath")
			vector_math_007_1.name = "Vector Math.007"
			vector_math_007_1.operation = 'CROSS_PRODUCT'
			
			#node Vector Math.008
			vector_math_008_3 = _mn_cartoon_smooth_handles.nodes.new("ShaderNodeVectorMath")
			vector_math_008_3.name = "Vector Math.008"
			vector_math_008_3.operation = 'SCALE'
			
			#node Group Output
			group_output_35 = _mn_cartoon_smooth_handles.nodes.new("NodeGroupOutput")
			group_output_35.name = "Group Output"
			group_output_35.is_active_output = True
			
			#node Group
			group_13 = _mn_cartoon_smooth_handles.nodes.new("GeometryNodeGroup")
			group_13.name = "Group"
			group_13.node_tree = mn_units
			
			#node Group Input
			group_input_34 = _mn_cartoon_smooth_handles.nodes.new("NodeGroupInput")
			group_input_34.name = "Group Input"
			
			
			
			
			#Set locations
			vector_math_005_1.location = (-40.0, 120.0)
			named_attribute_004_1.location = (-200.0, 120.0)
			vector_math_006_1.location = (-40.0, -20.0)
			named_attribute_003_1.location = (-200.0, -20.0)
			vector_math_007_1.location = (120.0, 120.0)
			vector_math_008_3.location = (280.0, 120.0)
			group_output_35.location = (440.0, 120.0)
			group_13.location = (280.0, -20.0)
			group_input_34.location = (120.0, -20.0)
			
			#Set dimensions
			vector_math_005_1.width, vector_math_005_1.height = 140.0, 100.0
			named_attribute_004_1.width, named_attribute_004_1.height = 140.0, 100.0
			vector_math_006_1.width, vector_math_006_1.height = 140.0, 100.0
			named_attribute_003_1.width, named_attribute_003_1.height = 140.0, 100.0
			vector_math_007_1.width, vector_math_007_1.height = 140.0, 100.0
			vector_math_008_3.width, vector_math_008_3.height = 140.0, 100.0
			group_output_35.width, group_output_35.height = 140.0, 100.0
			group_13.width, group_13.height = 140.0, 100.0
			group_input_34.width, group_input_34.height = 140.0, 100.0
			
			#initialize _mn_cartoon_smooth_handles links
			#vector_math_007_1.Vector -> vector_math_008_3.Vector
			_mn_cartoon_smooth_handles.links.new(vector_math_007_1.outputs[0], vector_math_008_3.inputs[0])
			#named_attribute_004_1.Attribute -> vector_math_005_1.Vector
			_mn_cartoon_smooth_handles.links.new(named_attribute_004_1.outputs[0], vector_math_005_1.inputs[0])
			#vector_math_005_1.Vector -> vector_math_007_1.Vector
			_mn_cartoon_smooth_handles.links.new(vector_math_005_1.outputs[0], vector_math_007_1.inputs[0])
			#vector_math_006_1.Vector -> vector_math_007_1.Vector
			_mn_cartoon_smooth_handles.links.new(vector_math_006_1.outputs[0], vector_math_007_1.inputs[1])
			#named_attribute_003_1.Attribute -> vector_math_006_1.Vector
			_mn_cartoon_smooth_handles.links.new(named_attribute_003_1.outputs[0], vector_math_006_1.inputs[0])
			#vector_math_008_3.Vector -> group_output_35.Vector
			_mn_cartoon_smooth_handles.links.new(vector_math_008_3.outputs[0], group_output_35.inputs[0])
			#group_input_34.Scale -> group_13.Value
			_mn_cartoon_smooth_handles.links.new(group_input_34.outputs[0], group_13.inputs[0])
			#group_13.Angstrom -> vector_math_008_3.Scale
			_mn_cartoon_smooth_handles.links.new(group_13.outputs[0], vector_math_008_3.inputs[3])
			return _mn_cartoon_smooth_handles

		_mn_cartoon_smooth_handles = _mn_cartoon_smooth_handles_node_group()

		#initialize _field_offset_bool node group
		def _field_offset_bool_node_group():
			_field_offset_bool = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".field_offset_bool")

			_field_offset_bool.color_tag = 'NONE'
			_field_offset_bool.description = ""

			
			#_field_offset_bool interface
			#Socket Boolean
			boolean_socket_1 = _field_offset_bool.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket_1.attribute_domain = 'POINT'
			
			#Socket Boolean
			boolean_socket_2 = _field_offset_bool.interface.new_socket(name = "Boolean", in_out='INPUT', socket_type = 'NodeSocketBool')
			boolean_socket_2.attribute_domain = 'POINT'
			boolean_socket_2.hide_value = True
			
			#Socket Offset
			offset_socket_3 = _field_offset_bool.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket_3.subtype = 'NONE'
			offset_socket_3.default_value = 0
			offset_socket_3.min_value = -2147483648
			offset_socket_3.max_value = 2147483647
			offset_socket_3.attribute_domain = 'POINT'
			
			
			#initialize _field_offset_bool nodes
			#node Group Input
			group_input_35 = _field_offset_bool.nodes.new("NodeGroupInput")
			group_input_35.name = "Group Input"
			
			#node Index
			index_3 = _field_offset_bool.nodes.new("GeometryNodeInputIndex")
			index_3.name = "Index"
			
			#node Math.001
			math_001_5 = _field_offset_bool.nodes.new("ShaderNodeMath")
			math_001_5.name = "Math.001"
			math_001_5.operation = 'ADD'
			math_001_5.use_clamp = False
			
			#node Evaluate at Index.001
			evaluate_at_index_001 = _field_offset_bool.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001.name = "Evaluate at Index.001"
			evaluate_at_index_001.data_type = 'BOOLEAN'
			evaluate_at_index_001.domain = 'POINT'
			
			#node Group Output
			group_output_36 = _field_offset_bool.nodes.new("NodeGroupOutput")
			group_output_36.name = "Group Output"
			group_output_36.is_active_output = True
			
			
			
			
			#Set locations
			group_input_35.location = (-417.64404296875, 0.0)
			index_3.location = (-420.0, -120.0)
			math_001_5.location = (-220.0, -120.0)
			evaluate_at_index_001.location = (-220.0, 40.0)
			group_output_36.location = (-60.0, 40.0)
			
			#Set dimensions
			group_input_35.width, group_input_35.height = 140.0, 100.0
			index_3.width, index_3.height = 140.0, 100.0
			math_001_5.width, math_001_5.height = 140.0, 100.0
			evaluate_at_index_001.width, evaluate_at_index_001.height = 140.0, 100.0
			group_output_36.width, group_output_36.height = 140.0, 100.0
			
			#initialize _field_offset_bool links
			#group_input_35.Offset -> math_001_5.Value
			_field_offset_bool.links.new(group_input_35.outputs[1], math_001_5.inputs[0])
			#math_001_5.Value -> evaluate_at_index_001.Index
			_field_offset_bool.links.new(math_001_5.outputs[0], evaluate_at_index_001.inputs[0])
			#group_input_35.Boolean -> evaluate_at_index_001.Value
			_field_offset_bool.links.new(group_input_35.outputs[0], evaluate_at_index_001.inputs[1])
			#evaluate_at_index_001.Value -> group_output_36.Boolean
			_field_offset_bool.links.new(evaluate_at_index_001.outputs[0], group_output_36.inputs[0])
			#index_3.Index -> math_001_5.Value
			_field_offset_bool.links.new(index_3.outputs[0], math_001_5.inputs[1])
			return _field_offset_bool

		_field_offset_bool = _field_offset_bool_node_group()

		#initialize _cartoon_arrows_scale node group
		def _cartoon_arrows_scale_node_group():
			_cartoon_arrows_scale = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".cartoon_arrows_scale")

			_cartoon_arrows_scale.color_tag = 'NONE'
			_cartoon_arrows_scale.description = ""

			
			#_cartoon_arrows_scale interface
			#Socket Result
			result_socket = _cartoon_arrows_scale.interface.new_socket(name = "Result", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			result_socket.attribute_domain = 'POINT'
			
			#Socket Output
			output_socket_1 = _cartoon_arrows_scale.interface.new_socket(name = "Output", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			output_socket_1.subtype = 'NONE'
			output_socket_1.default_value = 0.0
			output_socket_1.min_value = -3.4028234663852886e+38
			output_socket_1.max_value = 3.4028234663852886e+38
			output_socket_1.attribute_domain = 'POINT'
			
			#Socket Input
			input_socket_1 = _cartoon_arrows_scale.interface.new_socket(name = "Input", in_out='INPUT', socket_type = 'NodeSocketFloat')
			input_socket_1.subtype = 'NONE'
			input_socket_1.default_value = 0.0
			input_socket_1.min_value = -3.4028234663852886e+38
			input_socket_1.max_value = 3.4028234663852886e+38
			input_socket_1.attribute_domain = 'POINT'
			
			#Socket Input
			input_socket_2 = _cartoon_arrows_scale.interface.new_socket(name = "Input", in_out='INPUT', socket_type = 'NodeSocketFloat')
			input_socket_2.subtype = 'NONE'
			input_socket_2.default_value = 0.0
			input_socket_2.min_value = -3.4028234663852886e+38
			input_socket_2.max_value = 3.4028234663852886e+38
			input_socket_2.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_5 = _cartoon_arrows_scale.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket_5.subtype = 'NONE'
			value_socket_5.default_value = 2.8499999046325684
			value_socket_5.min_value = -10000.0
			value_socket_5.max_value = 10000.0
			value_socket_5.attribute_domain = 'POINT'
			
			
			#initialize _cartoon_arrows_scale nodes
			#node Group Output
			group_output_37 = _cartoon_arrows_scale.nodes.new("NodeGroupOutput")
			group_output_37.name = "Group Output"
			group_output_37.is_active_output = True
			
			#node Math.006
			math_006 = _cartoon_arrows_scale.nodes.new("ShaderNodeMath")
			math_006.name = "Math.006"
			math_006.hide = True
			math_006.operation = 'MAXIMUM'
			math_006.use_clamp = False
			#Value_001
			math_006.inputs[1].default_value = 0.0
			
			#node Spline Parameter
			spline_parameter = _cartoon_arrows_scale.nodes.new("GeometryNodeSplineParameter")
			spline_parameter.name = "Spline Parameter"
			
			#node Map Range
			map_range = _cartoon_arrows_scale.nodes.new("ShaderNodeMapRange")
			map_range.name = "Map Range"
			map_range.clamp = True
			map_range.data_type = 'FLOAT'
			map_range.interpolation_type = 'LINEAR'
			
			#node Math.003
			math_003_2 = _cartoon_arrows_scale.nodes.new("ShaderNodeMath")
			math_003_2.name = "Math.003"
			math_003_2.operation = 'SUBTRACT'
			math_003_2.use_clamp = False
			
			#node Reroute.001
			reroute_001_4 = _cartoon_arrows_scale.nodes.new("NodeReroute")
			reroute_001_4.name = "Reroute.001"
			#node Reroute.010
			reroute_010_2 = _cartoon_arrows_scale.nodes.new("NodeReroute")
			reroute_010_2.name = "Reroute.010"
			#node Switch.001
			switch_001_1 = _cartoon_arrows_scale.nodes.new("GeometryNodeSwitch")
			switch_001_1.name = "Switch.001"
			switch_001_1.input_type = 'FLOAT'
			
			#node Reroute
			reroute_8 = _cartoon_arrows_scale.nodes.new("NodeReroute")
			reroute_8.name = "Reroute"
			#node Spline Length
			spline_length = _cartoon_arrows_scale.nodes.new("GeometryNodeSplineLength")
			spline_length.name = "Spline Length"
			
			#node Group Input
			group_input_36 = _cartoon_arrows_scale.nodes.new("NodeGroupInput")
			group_input_36.name = "Group Input"
			
			#node Math.007
			math_007 = _cartoon_arrows_scale.nodes.new("ShaderNodeMath")
			math_007.name = "Math.007"
			math_007.operation = 'DIVIDE'
			math_007.use_clamp = False
			#Value_001
			math_007.inputs[1].default_value = 100.0
			
			#node Map Range.001
			map_range_001 = _cartoon_arrows_scale.nodes.new("ShaderNodeMapRange")
			map_range_001.name = "Map Range.001"
			map_range_001.clamp = True
			map_range_001.data_type = 'FLOAT'
			map_range_001.interpolation_type = 'LINEAR'
			#To Max
			map_range_001.inputs[4].default_value = 0.0
			
			#node Compare.001
			compare_001_3 = _cartoon_arrows_scale.nodes.new("FunctionNodeCompare")
			compare_001_3.name = "Compare.001"
			compare_001_3.data_type = 'FLOAT'
			compare_001_3.mode = 'ELEMENT'
			compare_001_3.operation = 'EQUAL'
			#Epsilon
			compare_001_3.inputs[12].default_value = 0.0010000000474974513
			
			#node Math.008
			math_008 = _cartoon_arrows_scale.nodes.new("ShaderNodeMath")
			math_008.name = "Math.008"
			math_008.operation = 'MULTIPLY'
			math_008.use_clamp = False
			#Value_001
			math_008.inputs[1].default_value = 2.0
			
			
			
			
			#Set locations
			group_output_37.location = (670.39453125, 0.0)
			math_006.location = (-283.53955078125, 120.8475341796875)
			spline_parameter.location = (-283.53955078125, 240.8475341796875)
			map_range.location = (-43.53955078125, 140.8475341796875)
			math_003_2.location = (-283.53955078125, 80.8475341796875)
			reroute_001_4.location = (-128.9521484375, -162.76467895507812)
			reroute_010_2.location = (120.39453125, -104.70928955078125)
			switch_001_1.location = (480.39453125, -44.70928955078125)
			reroute_8.location = (-126.4767837524414, -251.35455322265625)
			spline_length.location = (-480.0, 100.0)
			group_input_36.location = (-700.0, -200.0)
			math_007.location = (-480.0, 20.0)
			map_range_001.location = (160.0, 60.0)
			compare_001_3.location = (160.0, 240.0)
			math_008.location = (-80.0, -140.0)
			
			#Set dimensions
			group_output_37.width, group_output_37.height = 140.0, 100.0
			math_006.width, math_006.height = 140.0, 100.0
			spline_parameter.width, spline_parameter.height = 140.0, 100.0
			map_range.width, map_range.height = 140.0, 100.0
			math_003_2.width, math_003_2.height = 140.0, 100.0
			reroute_001_4.width, reroute_001_4.height = 16.0, 100.0
			reroute_010_2.width, reroute_010_2.height = 16.0, 100.0
			switch_001_1.width, switch_001_1.height = 140.0, 100.0
			reroute_8.width, reroute_8.height = 16.0, 100.0
			spline_length.width, spline_length.height = 140.0, 100.0
			group_input_36.width, group_input_36.height = 140.0, 100.0
			math_007.width, math_007.height = 140.0, 100.0
			map_range_001.width, map_range_001.height = 140.0, 100.0
			compare_001_3.width, compare_001_3.height = 140.0, 100.0
			math_008.width, math_008.height = 140.0, 100.0
			
			#initialize _cartoon_arrows_scale links
			#spline_parameter.Length -> map_range.Value
			_cartoon_arrows_scale.links.new(spline_parameter.outputs[1], map_range.inputs[0])
			#reroute_001_4.Output -> map_range.To Min
			_cartoon_arrows_scale.links.new(reroute_001_4.outputs[0], map_range.inputs[3])
			#spline_length.Length -> map_range.From Max
			_cartoon_arrows_scale.links.new(spline_length.outputs[0], map_range.inputs[2])
			#map_range.Result -> map_range_001.Value
			_cartoon_arrows_scale.links.new(map_range.outputs[0], map_range_001.inputs[0])
			#map_range_001.Result -> switch_001_1.False
			_cartoon_arrows_scale.links.new(map_range_001.outputs[0], switch_001_1.inputs[1])
			#math_006.Value -> map_range.From Min
			_cartoon_arrows_scale.links.new(math_006.outputs[0], map_range.inputs[1])
			#map_range.Result -> compare_001_3.A
			_cartoon_arrows_scale.links.new(map_range.outputs[0], compare_001_3.inputs[0])
			#math_007.Value -> math_003_2.Value
			_cartoon_arrows_scale.links.new(math_007.outputs[0], math_003_2.inputs[1])
			#reroute_8.Output -> map_range_001.From Max
			_cartoon_arrows_scale.links.new(reroute_8.outputs[0], map_range_001.inputs[2])
			#reroute_001_4.Output -> reroute_010_2.Input
			_cartoon_arrows_scale.links.new(reroute_001_4.outputs[0], reroute_010_2.inputs[0])
			#reroute_010_2.Output -> map_range_001.From Min
			_cartoon_arrows_scale.links.new(reroute_010_2.outputs[0], map_range_001.inputs[1])
			#reroute_001_4.Output -> math_008.Value
			_cartoon_arrows_scale.links.new(reroute_001_4.outputs[0], math_008.inputs[0])
			#reroute_010_2.Output -> compare_001_3.B
			_cartoon_arrows_scale.links.new(reroute_010_2.outputs[0], compare_001_3.inputs[1])
			#compare_001_3.Result -> switch_001_1.Switch
			_cartoon_arrows_scale.links.new(compare_001_3.outputs[0], switch_001_1.inputs[0])
			#reroute_010_2.Output -> switch_001_1.True
			_cartoon_arrows_scale.links.new(reroute_010_2.outputs[0], switch_001_1.inputs[2])
			#math_003_2.Value -> math_006.Value
			_cartoon_arrows_scale.links.new(math_003_2.outputs[0], math_006.inputs[0])
			#reroute_8.Output -> map_range.To Max
			_cartoon_arrows_scale.links.new(reroute_8.outputs[0], map_range.inputs[4])
			#math_008.Value -> map_range_001.To Min
			_cartoon_arrows_scale.links.new(math_008.outputs[0], map_range_001.inputs[3])
			#spline_length.Length -> math_003_2.Value
			_cartoon_arrows_scale.links.new(spline_length.outputs[0], math_003_2.inputs[0])
			#compare_001_3.Result -> group_output_37.Result
			_cartoon_arrows_scale.links.new(compare_001_3.outputs[0], group_output_37.inputs[0])
			#switch_001_1.Output -> group_output_37.Output
			_cartoon_arrows_scale.links.new(switch_001_1.outputs[0], group_output_37.inputs[1])
			#group_input_36.Input -> reroute_001_4.Input
			_cartoon_arrows_scale.links.new(group_input_36.outputs[0], reroute_001_4.inputs[0])
			#group_input_36.Input -> reroute_8.Input
			_cartoon_arrows_scale.links.new(group_input_36.outputs[1], reroute_8.inputs[0])
			#group_input_36.Value -> math_007.Value
			_cartoon_arrows_scale.links.new(group_input_36.outputs[2], math_007.inputs[0])
			return _cartoon_arrows_scale

		_cartoon_arrows_scale = _cartoon_arrows_scale_node_group()

		#initialize _cartoon_arrow_instance node group
		def _cartoon_arrow_instance_node_group():
			_cartoon_arrow_instance = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".cartoon_arrow_instance")

			_cartoon_arrow_instance.color_tag = 'NONE'
			_cartoon_arrow_instance.description = ""

			_cartoon_arrow_instance.is_modifier = True
			
			#_cartoon_arrow_instance interface
			#Socket Trimmed Curve
			trimmed_curve_socket = _cartoon_arrow_instance.interface.new_socket(name = "Trimmed Curve", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			trimmed_curve_socket.attribute_domain = 'POINT'
			
			#Socket ArrowHeads
			arrowheads_socket = _cartoon_arrow_instance.interface.new_socket(name = "ArrowHeads", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			arrowheads_socket.attribute_domain = 'POINT'
			
			#Socket Curve
			curve_socket_3 = _cartoon_arrow_instance.interface.new_socket(name = "Curve", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			curve_socket_3.attribute_domain = 'POINT'
			
			#Socket Instance
			instance_socket = _cartoon_arrow_instance.interface.new_socket(name = "Instance", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			instance_socket.attribute_domain = 'POINT'
			
			#Socket Rotation
			rotation_socket_2 = _cartoon_arrow_instance.interface.new_socket(name = "Rotation", in_out='INPUT', socket_type = 'NodeSocketVector')
			rotation_socket_2.subtype = 'EULER'
			rotation_socket_2.default_value = (0.0, 0.0, 0.0)
			rotation_socket_2.min_value = -3.4028234663852886e+38
			rotation_socket_2.max_value = 3.4028234663852886e+38
			rotation_socket_2.attribute_domain = 'POINT'
			rotation_socket_2.hide_value = True
			
			#Socket Scale
			scale_socket_3 = _cartoon_arrow_instance.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketVector')
			scale_socket_3.subtype = 'XYZ'
			scale_socket_3.default_value = (1.0, 1.0, 1.0)
			scale_socket_3.min_value = -3.4028234663852886e+38
			scale_socket_3.max_value = 3.4028234663852886e+38
			scale_socket_3.attribute_domain = 'POINT'
			
			
			#initialize _cartoon_arrow_instance nodes
			#node Boolean Math.004
			boolean_math_004_2 = _cartoon_arrow_instance.nodes.new("FunctionNodeBooleanMath")
			boolean_math_004_2.name = "Boolean Math.004"
			boolean_math_004_2.operation = 'AND'
			
			#node Boolean Math.005
			boolean_math_005 = _cartoon_arrow_instance.nodes.new("FunctionNodeBooleanMath")
			boolean_math_005.name = "Boolean Math.005"
			boolean_math_005.operation = 'AND'
			
			#node Reroute.007
			reroute_007_1 = _cartoon_arrow_instance.nodes.new("NodeReroute")
			reroute_007_1.name = "Reroute.007"
			#node Instance on Points
			instance_on_points_2 = _cartoon_arrow_instance.nodes.new("GeometryNodeInstanceOnPoints")
			instance_on_points_2.name = "Instance on Points"
			#Pick Instance
			instance_on_points_2.inputs[3].default_value = False
			#Instance Index
			instance_on_points_2.inputs[4].default_value = 0
			
			#node Group Output
			group_output_38 = _cartoon_arrow_instance.nodes.new("NodeGroupOutput")
			group_output_38.name = "Group Output"
			group_output_38.is_active_output = True
			
			#node Align Euler to Vector
			align_euler_to_vector_1 = _cartoon_arrow_instance.nodes.new("FunctionNodeAlignEulerToVector")
			align_euler_to_vector_1.name = "Align Euler to Vector"
			align_euler_to_vector_1.axis = 'X'
			align_euler_to_vector_1.pivot_axis = 'Y'
			#Factor
			align_euler_to_vector_1.inputs[1].default_value = 1.0
			
			#node Endpoint Selection.001
			endpoint_selection_001_1 = _cartoon_arrow_instance.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_001_1.name = "Endpoint Selection.001"
			#Start Size
			endpoint_selection_001_1.inputs[0].default_value = 0
			#End Size
			endpoint_selection_001_1.inputs[1].default_value = 1
			
			#node Endpoint Selection
			endpoint_selection = _cartoon_arrow_instance.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection.name = "Endpoint Selection"
			#Start Size
			endpoint_selection.inputs[0].default_value = 0
			#End Size
			endpoint_selection.inputs[1].default_value = 2
			
			#node Boolean Math.001
			boolean_math_001_7 = _cartoon_arrow_instance.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_7.name = "Boolean Math.001"
			boolean_math_001_7.operation = 'NOT'
			
			#node Boolean Math.003
			boolean_math_003_3 = _cartoon_arrow_instance.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003_3.name = "Boolean Math.003"
			boolean_math_003_3.operation = 'AND'
			
			#node Reroute
			reroute_9 = _cartoon_arrow_instance.nodes.new("NodeReroute")
			reroute_9.name = "Reroute"
			#node Position.001
			position_001_2 = _cartoon_arrow_instance.nodes.new("GeometryNodeInputPosition")
			position_001_2.name = "Position.001"
			
			#node Vector Math
			vector_math_3 = _cartoon_arrow_instance.nodes.new("ShaderNodeVectorMath")
			vector_math_3.name = "Vector Math"
			vector_math_3.operation = 'SUBTRACT'
			
			#node Group.006
			group_006 = _cartoon_arrow_instance.nodes.new("GeometryNodeGroup")
			group_006.name = "Group.006"
			group_006.node_tree = _field_offset_vec
			#Input_1
			group_006.inputs[1].default_value = 1
			
			#node Group.018
			group_018 = _cartoon_arrow_instance.nodes.new("GeometryNodeGroup")
			group_018.name = "Group.018"
			group_018.node_tree = _mn_select_sec_struct
			#Socket_1
			group_018.inputs[0].default_value = True
			
			#node Group Input
			group_input_37 = _cartoon_arrow_instance.nodes.new("NodeGroupInput")
			group_input_37.name = "Group Input"
			
			#node Delete Geometry
			delete_geometry = _cartoon_arrow_instance.nodes.new("GeometryNodeDeleteGeometry")
			delete_geometry.name = "Delete Geometry"
			delete_geometry.domain = 'POINT'
			delete_geometry.mode = 'ALL'
			
			
			
			
			#Set locations
			boolean_math_004_2.location = (-239.0887451171875, 169.322998046875)
			boolean_math_005.location = (-240.0, 22.557861328125)
			reroute_007_1.location = (-420.0, -200.0)
			instance_on_points_2.location = (700.0, 180.0)
			group_output_38.location = (1140.0, -20.0)
			align_euler_to_vector_1.location = (260.0, 60.0)
			endpoint_selection_001_1.location = (-660.0, 280.0)
			endpoint_selection.location = (-660.0, 160.0)
			boolean_math_001_7.location = (-440.0, 340.0)
			boolean_math_003_3.location = (-440.0, 220.0)
			reroute_9.location = (-380.0, 0.0)
			position_001_2.location = (-40.0, -140.0)
			vector_math_3.location = (166.50079345703125, -140.0)
			group_006.location = (164.67938232421875, -280.0)
			group_018.location = (-700.0, 20.0)
			group_input_37.location = (-660.0, -180.0)
			delete_geometry.location = (108.09152221679688, -434.36468505859375)
			
			#Set dimensions
			boolean_math_004_2.width, boolean_math_004_2.height = 140.0, 100.0
			boolean_math_005.width, boolean_math_005.height = 140.0, 100.0
			reroute_007_1.width, reroute_007_1.height = 16.0, 100.0
			instance_on_points_2.width, instance_on_points_2.height = 140.0, 100.0
			group_output_38.width, group_output_38.height = 140.0, 100.0
			align_euler_to_vector_1.width, align_euler_to_vector_1.height = 140.0, 100.0
			endpoint_selection_001_1.width, endpoint_selection_001_1.height = 140.0, 100.0
			endpoint_selection.width, endpoint_selection.height = 140.0, 100.0
			boolean_math_001_7.width, boolean_math_001_7.height = 140.0, 100.0
			boolean_math_003_3.width, boolean_math_003_3.height = 140.0, 100.0
			reroute_9.width, reroute_9.height = 16.0, 100.0
			position_001_2.width, position_001_2.height = 140.0, 100.0
			vector_math_3.width, vector_math_3.height = 233.49920654296875, 100.0
			group_006.width, group_006.height = 235.32061767578125, 100.0
			group_018.width, group_018.height = 234.5810546875, 100.0
			group_input_37.width, group_input_37.height = 140.0, 100.0
			delete_geometry.width, delete_geometry.height = 140.0, 100.0
			
			#initialize _cartoon_arrow_instance links
			#reroute_007_1.Output -> instance_on_points_2.Points
			_cartoon_arrow_instance.links.new(reroute_007_1.outputs[0], instance_on_points_2.inputs[0])
			#position_001_2.Position -> vector_math_3.Vector
			_cartoon_arrow_instance.links.new(position_001_2.outputs[0], vector_math_3.inputs[0])
			#boolean_math_004_2.Boolean -> instance_on_points_2.Selection
			_cartoon_arrow_instance.links.new(boolean_math_004_2.outputs[0], instance_on_points_2.inputs[1])
			#endpoint_selection.Selection -> boolean_math_003_3.Boolean
			_cartoon_arrow_instance.links.new(endpoint_selection.outputs[0], boolean_math_003_3.inputs[1])
			#align_euler_to_vector_1.Rotation -> instance_on_points_2.Rotation
			_cartoon_arrow_instance.links.new(align_euler_to_vector_1.outputs[0], instance_on_points_2.inputs[5])
			#endpoint_selection_001_1.Selection -> boolean_math_001_7.Boolean
			_cartoon_arrow_instance.links.new(endpoint_selection_001_1.outputs[0], boolean_math_001_7.inputs[0])
			#boolean_math_005.Boolean -> delete_geometry.Selection
			_cartoon_arrow_instance.links.new(boolean_math_005.outputs[0], delete_geometry.inputs[1])
			#reroute_007_1.Output -> delete_geometry.Geometry
			_cartoon_arrow_instance.links.new(reroute_007_1.outputs[0], delete_geometry.inputs[0])
			#endpoint_selection_001_1.Selection -> boolean_math_005.Boolean
			_cartoon_arrow_instance.links.new(endpoint_selection_001_1.outputs[0], boolean_math_005.inputs[0])
			#boolean_math_003_3.Boolean -> boolean_math_004_2.Boolean
			_cartoon_arrow_instance.links.new(boolean_math_003_3.outputs[0], boolean_math_004_2.inputs[0])
			#position_001_2.Position -> group_006.Field
			_cartoon_arrow_instance.links.new(position_001_2.outputs[0], group_006.inputs[0])
			#boolean_math_001_7.Boolean -> boolean_math_003_3.Boolean
			_cartoon_arrow_instance.links.new(boolean_math_001_7.outputs[0], boolean_math_003_3.inputs[0])
			#vector_math_3.Vector -> align_euler_to_vector_1.Vector
			_cartoon_arrow_instance.links.new(vector_math_3.outputs[0], align_euler_to_vector_1.inputs[2])
			#group_input_37.Instance -> instance_on_points_2.Instance
			_cartoon_arrow_instance.links.new(group_input_37.outputs[1], instance_on_points_2.inputs[2])
			#group_input_37.Curve -> reroute_007_1.Input
			_cartoon_arrow_instance.links.new(group_input_37.outputs[0], reroute_007_1.inputs[0])
			#group_input_37.Rotation -> align_euler_to_vector_1.Rotation
			_cartoon_arrow_instance.links.new(group_input_37.outputs[2], align_euler_to_vector_1.inputs[0])
			#delete_geometry.Geometry -> group_output_38.Trimmed Curve
			_cartoon_arrow_instance.links.new(delete_geometry.outputs[0], group_output_38.inputs[0])
			#instance_on_points_2.Instances -> group_output_38.ArrowHeads
			_cartoon_arrow_instance.links.new(instance_on_points_2.outputs[0], group_output_38.inputs[1])
			#group_input_37.Scale -> instance_on_points_2.Scale
			_cartoon_arrow_instance.links.new(group_input_37.outputs[3], instance_on_points_2.inputs[6])
			#group_006.Field -> vector_math_3.Vector
			_cartoon_arrow_instance.links.new(group_006.outputs[0], vector_math_3.inputs[1])
			#reroute_9.Output -> boolean_math_004_2.Boolean
			_cartoon_arrow_instance.links.new(reroute_9.outputs[0], boolean_math_004_2.inputs[1])
			#reroute_9.Output -> boolean_math_005.Boolean
			_cartoon_arrow_instance.links.new(reroute_9.outputs[0], boolean_math_005.inputs[1])
			#group_018.Is Sheet -> reroute_9.Input
			_cartoon_arrow_instance.links.new(group_018.outputs[1], reroute_9.inputs[0])
			return _cartoon_arrow_instance

		_cartoon_arrow_instance = _cartoon_arrow_instance_node_group()

		#initialize _cartoon_arrow_primitive node group
		def _cartoon_arrow_primitive_node_group():
			_cartoon_arrow_primitive = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".cartoon.arrow_primitive")

			_cartoon_arrow_primitive.color_tag = 'NONE'
			_cartoon_arrow_primitive.description = ""

			_cartoon_arrow_primitive.is_modifier = True
			
			#_cartoon_arrow_primitive interface
			#Socket Geometry
			geometry_socket_8 = _cartoon_arrow_primitive.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_8.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_6 = _cartoon_arrow_primitive.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket_6.subtype = 'NONE'
			value_socket_6.default_value = 0.5
			value_socket_6.min_value = -10000.0
			value_socket_6.max_value = 10000.0
			value_socket_6.attribute_domain = 'POINT'
			
			
			#initialize _cartoon_arrow_primitive nodes
			#node Group Output
			group_output_39 = _cartoon_arrow_primitive.nodes.new("NodeGroupOutput")
			group_output_39.name = "Group Output"
			group_output_39.is_active_output = True
			
			#node Group Input
			group_input_38 = _cartoon_arrow_primitive.nodes.new("NodeGroupInput")
			group_input_38.name = "Group Input"
			
			#node Transform Geometry
			transform_geometry_1 = _cartoon_arrow_primitive.nodes.new("GeometryNodeTransform")
			transform_geometry_1.name = "Transform Geometry"
			transform_geometry_1.mode = 'COMPONENTS'
			#Translation
			transform_geometry_1.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Rotation
			transform_geometry_1.inputs[2].default_value = (0.0, 3.1415927410125732, 0.0)
			
			#node Transform Geometry.002
			transform_geometry_002_1 = _cartoon_arrow_primitive.nodes.new("GeometryNodeTransform")
			transform_geometry_002_1.name = "Transform Geometry.002"
			transform_geometry_002_1.mode = 'COMPONENTS'
			#Rotation
			transform_geometry_002_1.inputs[2].default_value = (1.5707963705062866, 0.0, 0.0)
			#Scale
			transform_geometry_002_1.inputs[3].default_value = (1.0, 0.8299999833106995, 1.0)
			
			#node Group.005
			group_005 = _cartoon_arrow_primitive.nodes.new("GeometryNodeGroup")
			group_005.name = "Group.005"
			group_005.node_tree = mn_units
			#Input_1
			group_005.inputs[0].default_value = 3.390000104904175
			
			#node Join Geometry.001
			join_geometry_001_2 = _cartoon_arrow_primitive.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_001_2.name = "Join Geometry.001"
			join_geometry_001_2.hide = True
			
			#node Merge by Distance
			merge_by_distance_1 = _cartoon_arrow_primitive.nodes.new("GeometryNodeMergeByDistance")
			merge_by_distance_1.name = "Merge by Distance"
			merge_by_distance_1.hide = True
			merge_by_distance_1.mode = 'ALL'
			#Selection
			merge_by_distance_1.inputs[1].default_value = True
			#Distance
			merge_by_distance_1.inputs[2].default_value = 0.0010000000474974513
			
			#node Mesh Circle
			mesh_circle = _cartoon_arrow_primitive.nodes.new("GeometryNodeMeshCircle")
			mesh_circle.name = "Mesh Circle"
			mesh_circle.fill_type = 'TRIANGLE_FAN'
			#Vertices
			mesh_circle.inputs[0].default_value = 3
			
			#node Combine XYZ.001
			combine_xyz_001 = _cartoon_arrow_primitive.nodes.new("ShaderNodeCombineXYZ")
			combine_xyz_001.name = "Combine XYZ.001"
			
			#node Group.001
			group_001_5 = _cartoon_arrow_primitive.nodes.new("GeometryNodeGroup")
			group_001_5.name = "Group.001"
			group_001_5.node_tree = mn_units
			#Input_1
			group_001_5.inputs[0].default_value = 2.130000114440918
			
			#node Group.011
			group_011 = _cartoon_arrow_primitive.nodes.new("GeometryNodeGroup")
			group_011.name = "Group.011"
			group_011.node_tree = mn_units
			#Input_1
			group_011.inputs[0].default_value = 1.2000000476837158
			
			#node Math.002
			math_002_1 = _cartoon_arrow_primitive.nodes.new("ShaderNodeMath")
			math_002_1.name = "Math.002"
			math_002_1.operation = 'MULTIPLY'
			math_002_1.use_clamp = False
			#Value_001
			math_002_1.inputs[1].default_value = 1.399999976158142
			
			#node Reroute
			reroute_10 = _cartoon_arrow_primitive.nodes.new("NodeReroute")
			reroute_10.name = "Reroute"
			#node Reroute.001
			reroute_001_5 = _cartoon_arrow_primitive.nodes.new("NodeReroute")
			reroute_001_5.name = "Reroute.001"
			#node Reroute.002
			reroute_002_2 = _cartoon_arrow_primitive.nodes.new("NodeReroute")
			reroute_002_2.name = "Reroute.002"
			#node Combine XYZ.002
			combine_xyz_002 = _cartoon_arrow_primitive.nodes.new("ShaderNodeCombineXYZ")
			combine_xyz_002.name = "Combine XYZ.002"
			#X
			combine_xyz_002.inputs[0].default_value = 1.0
			#Z
			combine_xyz_002.inputs[2].default_value = 1.0
			
			#node Math.001
			math_001_6 = _cartoon_arrow_primitive.nodes.new("ShaderNodeMath")
			math_001_6.label = "x / 2"
			math_001_6.name = "Math.001"
			math_001_6.hide = True
			math_001_6.operation = 'DIVIDE'
			math_001_6.use_clamp = False
			#Value_001
			math_001_6.inputs[1].default_value = 3.059999942779541
			
			#node Math
			math_8 = _cartoon_arrow_primitive.nodes.new("ShaderNodeMath")
			math_8.label = "x / -2"
			math_8.name = "Math"
			math_8.hide = True
			math_8.operation = 'DIVIDE'
			math_8.use_clamp = False
			#Value_001
			math_8.inputs[1].default_value = -19.440000534057617
			
			#node Extrude Mesh
			extrude_mesh = _cartoon_arrow_primitive.nodes.new("GeometryNodeExtrudeMesh")
			extrude_mesh.name = "Extrude Mesh"
			extrude_mesh.mode = 'FACES'
			#Selection
			extrude_mesh.inputs[1].default_value = True
			#Offset
			extrude_mesh.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Individual
			extrude_mesh.inputs[4].default_value = False
			
			
			
			
			#Set locations
			group_output_39.location = (686.1517333984375, 0.0)
			group_input_38.location = (-874.151611328125, 0.0)
			transform_geometry_1.location = (245.848388671875, -5.45166015625)
			transform_geometry_002_1.location = (-114.151611328125, -45.45166015625)
			group_005.location = (-674.151611328125, 14.54833984375)
			join_geometry_001_2.location = (-434.151611328125, -125.45166015625)
			merge_by_distance_1.location = (-434.151611328125, -165.45166015625)
			mesh_circle.location = (-674.151611328125, 154.54833984375)
			combine_xyz_001.location = (-274.151611328125, -185.45166015625)
			group_001_5.location = (-674.151611328125, -105.45166015625)
			group_011.location = (-674.151611328125, -245.45166015625)
			math_002_1.location = (-118.0, -320.0)
			reroute_10.location = (-718.0, -420.0)
			reroute_001_5.location = (-478.0, -600.0)
			reroute_002_2.location = (-178.0, -600.0)
			combine_xyz_002.location = (242.0, -280.0)
			math_001_6.location = (-438.0, -220.0)
			math_8.location = (-438.0, -300.0)
			extrude_mesh.location = (-434.151611328125, 134.54833984375)
			
			#Set dimensions
			group_output_39.width, group_output_39.height = 140.0, 100.0
			group_input_38.width, group_input_38.height = 140.0, 100.0
			transform_geometry_1.width, transform_geometry_1.height = 140.0, 100.0
			transform_geometry_002_1.width, transform_geometry_002_1.height = 140.0, 100.0
			group_005.width, group_005.height = 140.0, 100.0
			join_geometry_001_2.width, join_geometry_001_2.height = 140.0, 100.0
			merge_by_distance_1.width, merge_by_distance_1.height = 140.0, 100.0
			mesh_circle.width, mesh_circle.height = 140.0, 100.0
			combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
			group_001_5.width, group_001_5.height = 140.0, 100.0
			group_011.width, group_011.height = 140.0, 100.0
			math_002_1.width, math_002_1.height = 140.0, 100.0
			reroute_10.width, reroute_10.height = 16.0, 100.0
			reroute_001_5.width, reroute_001_5.height = 16.0, 100.0
			reroute_002_2.width, reroute_002_2.height = 16.0, 100.0
			combine_xyz_002.width, combine_xyz_002.height = 140.0, 100.0
			math_001_6.width, math_001_6.height = 140.0, 100.0
			math_8.width, math_8.height = 140.0, 100.0
			extrude_mesh.width, extrude_mesh.height = 140.0, 100.0
			
			#initialize _cartoon_arrow_primitive links
			#group_005.Angstrom -> math_001_6.Value
			_cartoon_arrow_primitive.links.new(group_005.outputs[0], math_001_6.inputs[0])
			#mesh_circle.Mesh -> extrude_mesh.Mesh
			_cartoon_arrow_primitive.links.new(mesh_circle.outputs[0], extrude_mesh.inputs[0])
			#group_005.Angstrom -> mesh_circle.Radius
			_cartoon_arrow_primitive.links.new(group_005.outputs[0], mesh_circle.inputs[1])
			#math_001_6.Value -> combine_xyz_001.X
			_cartoon_arrow_primitive.links.new(math_001_6.outputs[0], combine_xyz_001.inputs[0])
			#math_002_1.Value -> combine_xyz_002.Y
			_cartoon_arrow_primitive.links.new(math_002_1.outputs[0], combine_xyz_002.inputs[1])
			#group_001_5.Angstrom -> math_8.Value
			_cartoon_arrow_primitive.links.new(group_001_5.outputs[0], math_8.inputs[0])
			#math_8.Value -> combine_xyz_001.Z
			_cartoon_arrow_primitive.links.new(math_8.outputs[0], combine_xyz_001.inputs[2])
			#mesh_circle.Mesh -> join_geometry_001_2.Geometry
			_cartoon_arrow_primitive.links.new(mesh_circle.outputs[0], join_geometry_001_2.inputs[0])
			#combine_xyz_001.Vector -> transform_geometry_002_1.Translation
			_cartoon_arrow_primitive.links.new(combine_xyz_001.outputs[0], transform_geometry_002_1.inputs[1])
			#combine_xyz_002.Vector -> transform_geometry_1.Scale
			_cartoon_arrow_primitive.links.new(combine_xyz_002.outputs[0], transform_geometry_1.inputs[3])
			#merge_by_distance_1.Geometry -> transform_geometry_002_1.Geometry
			_cartoon_arrow_primitive.links.new(merge_by_distance_1.outputs[0], transform_geometry_002_1.inputs[0])
			#join_geometry_001_2.Geometry -> merge_by_distance_1.Geometry
			_cartoon_arrow_primitive.links.new(join_geometry_001_2.outputs[0], merge_by_distance_1.inputs[0])
			#group_001_5.Angstrom -> extrude_mesh.Offset Scale
			_cartoon_arrow_primitive.links.new(group_001_5.outputs[0], extrude_mesh.inputs[3])
			#transform_geometry_002_1.Geometry -> transform_geometry_1.Geometry
			_cartoon_arrow_primitive.links.new(transform_geometry_002_1.outputs[0], transform_geometry_1.inputs[0])
			#group_011.Angstrom -> combine_xyz_001.Y
			_cartoon_arrow_primitive.links.new(group_011.outputs[0], combine_xyz_001.inputs[1])
			#reroute_002_2.Output -> math_002_1.Value
			_cartoon_arrow_primitive.links.new(reroute_002_2.outputs[0], math_002_1.inputs[0])
			#transform_geometry_1.Geometry -> group_output_39.Geometry
			_cartoon_arrow_primitive.links.new(transform_geometry_1.outputs[0], group_output_39.inputs[0])
			#group_input_38.Value -> reroute_10.Input
			_cartoon_arrow_primitive.links.new(group_input_38.outputs[0], reroute_10.inputs[0])
			#reroute_10.Output -> reroute_001_5.Input
			_cartoon_arrow_primitive.links.new(reroute_10.outputs[0], reroute_001_5.inputs[0])
			#reroute_001_5.Output -> reroute_002_2.Input
			_cartoon_arrow_primitive.links.new(reroute_001_5.outputs[0], reroute_002_2.inputs[0])
			#extrude_mesh.Mesh -> join_geometry_001_2.Geometry
			_cartoon_arrow_primitive.links.new(extrude_mesh.outputs[0], join_geometry_001_2.inputs[0])
			return _cartoon_arrow_primitive

		_cartoon_arrow_primitive = _cartoon_arrow_primitive_node_group()

		#initialize _curve_profile_backup node group
		def _curve_profile_backup_node_group():
			_curve_profile_backup = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".curve_profile_backup")

			_curve_profile_backup.color_tag = 'NONE'
			_curve_profile_backup.description = ""

			_curve_profile_backup.is_modifier = True
			
			#_curve_profile_backup interface
			#Socket Output
			output_socket_2 = _curve_profile_backup.interface.new_socket(name = "Output", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			output_socket_2.attribute_domain = 'POINT'
			
			#Socket Input
			input_socket_3 = _curve_profile_backup.interface.new_socket(name = "Input", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			input_socket_3.attribute_domain = 'POINT'
			
			#Socket Resolution
			resolution_socket_2 = _curve_profile_backup.interface.new_socket(name = "Resolution", in_out='INPUT', socket_type = 'NodeSocketInt')
			resolution_socket_2.subtype = 'NONE'
			resolution_socket_2.default_value = 12
			resolution_socket_2.min_value = 3
			resolution_socket_2.max_value = 512
			resolution_socket_2.attribute_domain = 'POINT'
			
			#Socket Radius
			radius_socket_2 = _curve_profile_backup.interface.new_socket(name = "Radius", in_out='INPUT', socket_type = 'NodeSocketFloat')
			radius_socket_2.subtype = 'DISTANCE'
			radius_socket_2.default_value = 0.009999999776482582
			radius_socket_2.min_value = 0.0
			radius_socket_2.max_value = 3.4028234663852886e+38
			radius_socket_2.attribute_domain = 'POINT'
			
			#Socket Rotation
			rotation_socket_3 = _curve_profile_backup.interface.new_socket(name = "Rotation", in_out='INPUT', socket_type = 'NodeSocketFloat')
			rotation_socket_3.subtype = 'NONE'
			rotation_socket_3.default_value = 0.0
			rotation_socket_3.min_value = -10000.0
			rotation_socket_3.max_value = 10000.0
			rotation_socket_3.attribute_domain = 'POINT'
			
			
			#initialize _curve_profile_backup nodes
			#node Group Output
			group_output_40 = _curve_profile_backup.nodes.new("NodeGroupOutput")
			group_output_40.name = "Group Output"
			group_output_40.is_active_output = True
			
			#node Compare
			compare_8 = _curve_profile_backup.nodes.new("FunctionNodeCompare")
			compare_8.name = "Compare"
			compare_8.hide = True
			compare_8.data_type = 'INT'
			compare_8.mode = 'ELEMENT'
			compare_8.operation = 'GREATER_THAN'
			#B_INT
			compare_8.inputs[3].default_value = 0
			
			#node Switch
			switch_9 = _curve_profile_backup.nodes.new("GeometryNodeSwitch")
			switch_9.name = "Switch"
			switch_9.input_type = 'GEOMETRY'
			
			#node Domain Size
			domain_size_3 = _curve_profile_backup.nodes.new("GeometryNodeAttributeDomainSize")
			domain_size_3.name = "Domain Size"
			domain_size_3.component = 'CURVE'
			
			#node Reroute.001
			reroute_001_6 = _curve_profile_backup.nodes.new("NodeReroute")
			reroute_001_6.name = "Reroute.001"
			#node Curve Circle
			curve_circle_2 = _curve_profile_backup.nodes.new("GeometryNodeCurvePrimitiveCircle")
			curve_circle_2.name = "Curve Circle"
			curve_circle_2.mode = 'RADIUS'
			
			#node Transform Geometry.001
			transform_geometry_001_1 = _curve_profile_backup.nodes.new("GeometryNodeTransform")
			transform_geometry_001_1.name = "Transform Geometry.001"
			transform_geometry_001_1.mode = 'COMPONENTS'
			#Translation
			transform_geometry_001_1.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Scale
			transform_geometry_001_1.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Combine XYZ
			combine_xyz = _curve_profile_backup.nodes.new("ShaderNodeCombineXYZ")
			combine_xyz.name = "Combine XYZ"
			#X
			combine_xyz.inputs[0].default_value = 0.0
			#Y
			combine_xyz.inputs[1].default_value = 0.0
			
			#node Group Input
			group_input_39 = _curve_profile_backup.nodes.new("NodeGroupInput")
			group_input_39.name = "Group Input"
			
			#node Group
			group_14 = _curve_profile_backup.nodes.new("GeometryNodeGroup")
			group_14.name = "Group"
			group_14.node_tree = mn_units
			
			
			
			
			#Set locations
			group_output_40.location = (320.278564453125, 0.0)
			compare_8.location = (-69.721435546875, 174.23248291015625)
			switch_9.location = (130.278564453125, 214.23248291015625)
			domain_size_3.location = (-77.112060546875, 125.76751708984375)
			reroute_001_6.location = (-130.278564453125, -81.5904541015625)
			curve_circle_2.location = (-77.112060546875, -214.23248291015625)
			transform_geometry_001_1.location = (130.278564453125, -45.76751708984375)
			combine_xyz.location = (-80.0, -360.0)
			group_input_39.location = (-392.2209777832031, -102.58642578125)
			group_14.location = (-380.0, -260.0)
			
			#Set dimensions
			group_output_40.width, group_output_40.height = 140.0, 100.0
			compare_8.width, compare_8.height = 137.39459228515625, 100.0
			switch_9.width, switch_9.height = 140.0, 100.0
			domain_size_3.width, domain_size_3.height = 140.0, 100.0
			reroute_001_6.width, reroute_001_6.height = 16.0, 100.0
			curve_circle_2.width, curve_circle_2.height = 140.0, 100.0
			transform_geometry_001_1.width, transform_geometry_001_1.height = 140.0, 100.0
			combine_xyz.width, combine_xyz.height = 140.0, 100.0
			group_input_39.width, group_input_39.height = 140.0, 100.0
			group_14.width, group_14.height = 140.0, 100.0
			
			#initialize _curve_profile_backup links
			#domain_size_3.Point Count -> compare_8.A
			_curve_profile_backup.links.new(domain_size_3.outputs[0], compare_8.inputs[2])
			#reroute_001_6.Output -> domain_size_3.Geometry
			_curve_profile_backup.links.new(reroute_001_6.outputs[0], domain_size_3.inputs[0])
			#curve_circle_2.Curve -> transform_geometry_001_1.Geometry
			_curve_profile_backup.links.new(curve_circle_2.outputs[0], transform_geometry_001_1.inputs[0])
			#compare_8.Result -> switch_9.Switch
			_curve_profile_backup.links.new(compare_8.outputs[0], switch_9.inputs[0])
			#reroute_001_6.Output -> switch_9.True
			_curve_profile_backup.links.new(reroute_001_6.outputs[0], switch_9.inputs[2])
			#transform_geometry_001_1.Geometry -> switch_9.False
			_curve_profile_backup.links.new(transform_geometry_001_1.outputs[0], switch_9.inputs[1])
			#group_input_39.Input -> reroute_001_6.Input
			_curve_profile_backup.links.new(group_input_39.outputs[0], reroute_001_6.inputs[0])
			#switch_9.Output -> group_output_40.Output
			_curve_profile_backup.links.new(switch_9.outputs[0], group_output_40.inputs[0])
			#group_input_39.Resolution -> curve_circle_2.Resolution
			_curve_profile_backup.links.new(group_input_39.outputs[1], curve_circle_2.inputs[0])
			#combine_xyz.Vector -> transform_geometry_001_1.Rotation
			_curve_profile_backup.links.new(combine_xyz.outputs[0], transform_geometry_001_1.inputs[2])
			#group_input_39.Rotation -> combine_xyz.Z
			_curve_profile_backup.links.new(group_input_39.outputs[3], combine_xyz.inputs[2])
			#group_input_39.Radius -> group_14.Value
			_curve_profile_backup.links.new(group_input_39.outputs[2], group_14.inputs[0])
			#group_14.Angstrom -> curve_circle_2.Radius
			_curve_profile_backup.links.new(group_14.outputs[0], curve_circle_2.inputs[4])
			return _curve_profile_backup

		_curve_profile_backup = _curve_profile_backup_node_group()

		#initialize _curve_custom_profile node group
		def _curve_custom_profile_node_group():
			_curve_custom_profile = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".curve_custom_profile")

			_curve_custom_profile.color_tag = 'NONE'
			_curve_custom_profile.description = ""

			_curve_custom_profile.is_modifier = True
			
			#_curve_custom_profile interface
			#Socket Geometry
			geometry_socket_9 = _curve_custom_profile.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_9.attribute_domain = 'POINT'
			
			#Socket Curve
			curve_socket_4 = _curve_custom_profile.interface.new_socket(name = "Curve", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			curve_socket_4.attribute_domain = 'POINT'
			
			#Socket Profile Resolution
			profile_resolution_socket = _curve_custom_profile.interface.new_socket(name = "Profile Resolution", in_out='INPUT', socket_type = 'NodeSocketInt')
			profile_resolution_socket.subtype = 'NONE'
			profile_resolution_socket.default_value = 4
			profile_resolution_socket.min_value = 3
			profile_resolution_socket.max_value = 512
			profile_resolution_socket.attribute_domain = 'POINT'
			
			#Socket Profile Radius
			profile_radius_socket = _curve_custom_profile.interface.new_socket(name = "Profile Radius", in_out='INPUT', socket_type = 'NodeSocketFloat')
			profile_radius_socket.subtype = 'DISTANCE'
			profile_radius_socket.default_value = 1.0
			profile_radius_socket.min_value = 0.0
			profile_radius_socket.max_value = 3.4028234663852886e+38
			profile_radius_socket.attribute_domain = 'POINT'
			
			#Socket Profile Rotation
			profile_rotation_socket = _curve_custom_profile.interface.new_socket(name = "Profile Rotation", in_out='INPUT', socket_type = 'NodeSocketFloat')
			profile_rotation_socket.subtype = 'NONE'
			profile_rotation_socket.default_value = 0.7853981852531433
			profile_rotation_socket.min_value = -10000.0
			profile_rotation_socket.max_value = 10000.0
			profile_rotation_socket.attribute_domain = 'POINT'
			
			#Socket Instance
			instance_socket_1 = _curve_custom_profile.interface.new_socket(name = "Instance", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			instance_socket_1.attribute_domain = 'POINT'
			
			#Socket Rotation X
			rotation_x_socket = _curve_custom_profile.interface.new_socket(name = "Rotation X", in_out='INPUT', socket_type = 'NodeSocketFloat')
			rotation_x_socket.subtype = 'ANGLE'
			rotation_x_socket.default_value = 0.0
			rotation_x_socket.min_value = -3.4028234663852886e+38
			rotation_x_socket.max_value = 3.4028234663852886e+38
			rotation_x_socket.attribute_domain = 'POINT'
			
			#Socket Scale
			scale_socket_4 = _curve_custom_profile.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketVector')
			scale_socket_4.subtype = 'XYZ'
			scale_socket_4.default_value = (0.33000001311302185, 0.36000001430511475, 0.75)
			scale_socket_4.min_value = -3.4028234663852886e+38
			scale_socket_4.max_value = 3.4028234663852886e+38
			scale_socket_4.attribute_domain = 'POINT'
			
			#Socket Factor
			factor_socket = _curve_custom_profile.interface.new_socket(name = "Factor", in_out='INPUT', socket_type = 'NodeSocketFloat')
			factor_socket.subtype = 'FACTOR'
			factor_socket.default_value = 0.0
			factor_socket.min_value = 0.0
			factor_socket.max_value = 1.0
			factor_socket.attribute_domain = 'POINT'
			
			#Socket Radius
			radius_socket_3 = _curve_custom_profile.interface.new_socket(name = "Radius", in_out='INPUT', socket_type = 'NodeSocketFloat')
			radius_socket_3.subtype = 'DISTANCE'
			radius_socket_3.default_value = 0.004999999888241291
			radius_socket_3.min_value = 0.0
			radius_socket_3.max_value = 3.4028234663852886e+38
			radius_socket_3.attribute_domain = 'POINT'
			
			#Socket Resolution
			resolution_socket_3 = _curve_custom_profile.interface.new_socket(name = "Resolution", in_out='INPUT', socket_type = 'NodeSocketInt')
			resolution_socket_3.subtype = 'NONE'
			resolution_socket_3.default_value = 6
			resolution_socket_3.min_value = 1
			resolution_socket_3.max_value = 2147483647
			resolution_socket_3.attribute_domain = 'POINT'
			
			#Socket Resample
			resample_socket = _curve_custom_profile.interface.new_socket(name = "Resample", in_out='INPUT', socket_type = 'NodeSocketBool')
			resample_socket.attribute_domain = 'POINT'
			
			
			#initialize _curve_custom_profile nodes
			#node Instance on Points.001
			instance_on_points_001_1 = _curve_custom_profile.nodes.new("GeometryNodeInstanceOnPoints")
			instance_on_points_001_1.name = "Instance on Points.001"
			#Selection
			instance_on_points_001_1.inputs[1].default_value = True
			#Pick Instance
			instance_on_points_001_1.inputs[3].default_value = False
			#Instance Index
			instance_on_points_001_1.inputs[4].default_value = 0
			
			#node Sample Index.001
			sample_index_001_2 = _curve_custom_profile.nodes.new("GeometryNodeSampleIndex")
			sample_index_001_2.name = "Sample Index.001"
			sample_index_001_2.clamp = False
			sample_index_001_2.data_type = 'FLOAT_VECTOR'
			sample_index_001_2.domain = 'POINT'
			
			#node Realize Instances
			realize_instances_2 = _curve_custom_profile.nodes.new("GeometryNodeRealizeInstances")
			realize_instances_2.name = "Realize Instances"
			#Selection
			realize_instances_2.inputs[1].default_value = True
			#Realize All
			realize_instances_2.inputs[2].default_value = True
			#Depth
			realize_instances_2.inputs[3].default_value = 0
			
			#node Index.003
			index_003_1 = _curve_custom_profile.nodes.new("GeometryNodeInputIndex")
			index_003_1.name = "Index.003"
			
			#node Position.001
			position_001_3 = _curve_custom_profile.nodes.new("GeometryNodeInputPosition")
			position_001_3.name = "Position.001"
			
			#node Curve to Mesh
			curve_to_mesh_2 = _curve_custom_profile.nodes.new("GeometryNodeCurveToMesh")
			curve_to_mesh_2.name = "Curve to Mesh"
			#Fill Caps
			curve_to_mesh_2.inputs[2].default_value = True
			
			#node Set Position.002
			set_position_002_1 = _curve_custom_profile.nodes.new("GeometryNodeSetPosition")
			set_position_002_1.name = "Set Position.002"
			#Selection
			set_position_002_1.inputs[1].default_value = True
			#Offset
			set_position_002_1.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Transform Geometry
			transform_geometry_2 = _curve_custom_profile.nodes.new("GeometryNodeTransform")
			transform_geometry_2.name = "Transform Geometry"
			transform_geometry_2.hide = True
			transform_geometry_2.mode = 'COMPONENTS'
			#Translation
			transform_geometry_2.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Rotation
			transform_geometry_2.inputs[2].default_value = (0.0, 1.5707963705062866, 0.0)
			#Scale
			transform_geometry_2.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Mix.001
			mix_001 = _curve_custom_profile.nodes.new("ShaderNodeMix")
			mix_001.name = "Mix.001"
			mix_001.blend_type = 'MIX'
			mix_001.clamp_factor = True
			mix_001.clamp_result = False
			mix_001.data_type = 'VECTOR'
			mix_001.factor_mode = 'UNIFORM'
			
			#node Flip Faces
			flip_faces = _curve_custom_profile.nodes.new("GeometryNodeFlipFaces")
			flip_faces.name = "Flip Faces"
			#Selection
			flip_faces.inputs[1].default_value = True
			
			#node Group Output
			group_output_41 = _curve_custom_profile.nodes.new("NodeGroupOutput")
			group_output_41.name = "Group Output"
			group_output_41.is_active_output = True
			
			#node Reroute.001
			reroute_001_7 = _curve_custom_profile.nodes.new("NodeReroute")
			reroute_001_7.name = "Reroute.001"
			#node Reroute
			reroute_11 = _curve_custom_profile.nodes.new("NodeReroute")
			reroute_11.name = "Reroute"
			#node Set Curve Radius
			set_curve_radius_2 = _curve_custom_profile.nodes.new("GeometryNodeSetCurveRadius")
			set_curve_radius_2.name = "Set Curve Radius"
			#Selection
			set_curve_radius_2.inputs[1].default_value = True
			
			#node Reroute.002
			reroute_002_3 = _curve_custom_profile.nodes.new("NodeReroute")
			reroute_002_3.name = "Reroute.002"
			#node Spline Resolution
			spline_resolution = _curve_custom_profile.nodes.new("GeometryNodeInputSplineResolution")
			spline_resolution.name = "Spline Resolution"
			
			#node Spline Length
			spline_length_1 = _curve_custom_profile.nodes.new("GeometryNodeSplineLength")
			spline_length_1.name = "Spline Length"
			
			#node Spline Parameter
			spline_parameter_1 = _curve_custom_profile.nodes.new("GeometryNodeSplineParameter")
			spline_parameter_1.name = "Spline Parameter"
			
			#node Group.001
			group_001_6 = _curve_custom_profile.nodes.new("GeometryNodeGroup")
			group_001_6.name = "Group.001"
			group_001_6.node_tree = _curve_profile_backup
			
			#node Set Spline Resolution
			set_spline_resolution = _curve_custom_profile.nodes.new("GeometryNodeSetSplineResolution")
			set_spline_resolution.name = "Set Spline Resolution"
			#Selection
			set_spline_resolution.inputs[1].default_value = True
			
			#node Resample Curve
			resample_curve = _curve_custom_profile.nodes.new("GeometryNodeResampleCurve")
			resample_curve.name = "Resample Curve"
			resample_curve.mode = 'EVALUATED'
			#Selection
			resample_curve.inputs[1].default_value = True
			
			#node Switch
			switch_10 = _curve_custom_profile.nodes.new("GeometryNodeSwitch")
			switch_10.name = "Switch"
			switch_10.input_type = 'GEOMETRY'
			
			#node Group Input
			group_input_40 = _curve_custom_profile.nodes.new("NodeGroupInput")
			group_input_40.name = "Group Input"
			
			#node Group
			group_15 = _curve_custom_profile.nodes.new("GeometryNodeGroup")
			group_15.name = "Group"
			group_15.node_tree = _guide_rotation
			
			
			
			
			#Set locations
			instance_on_points_001_1.location = (-289.36962890625, 170.0)
			sample_index_001_2.location = (-89.36962890625, 290.0)
			realize_instances_2.location = (-89.36962890625, 70.0)
			index_003_1.location = (-290.0, 270.0)
			position_001_3.location = (-290.0, 330.0)
			curve_to_mesh_2.location = (-100.0, -100.0)
			set_position_002_1.location = (260.0, 280.0)
			transform_geometry_2.location = (-520.0, -120.0)
			mix_001.location = (70.63037109375, 290.0)
			flip_faces.location = (460.0, 280.0)
			group_output_41.location = (660.0, 280.0)
			reroute_001_7.location = (-140.0, -240.0)
			reroute_11.location = (-539.885986328125, -222.59783935546875)
			set_curve_radius_2.location = (-296.1637268066406, -66.46692657470703)
			reroute_002_3.location = (-635.73388671875, -6.497833251953125)
			spline_resolution.location = (-1100.0, 280.0)
			spline_length_1.location = (-1100.0, 220.0)
			spline_parameter_1.location = (-1100.0, 380.0)
			group_001_6.location = (-900.0, -100.0)
			set_spline_resolution.location = (-1292.002685546875, 99.56741333007812)
			resample_curve.location = (-1124.6309814453125, 107.74668884277344)
			switch_10.location = (-905.0, 111.8224105834961)
			group_input_40.location = (-1608.1519775390625, -81.00050354003906)
			group_15.location = (-500.0, 60.0)
			
			#Set dimensions
			instance_on_points_001_1.width, instance_on_points_001_1.height = 140.0, 100.0
			sample_index_001_2.width, sample_index_001_2.height = 140.0, 100.0
			realize_instances_2.width, realize_instances_2.height = 140.0, 100.0
			index_003_1.width, index_003_1.height = 140.0, 100.0
			position_001_3.width, position_001_3.height = 140.0, 100.0
			curve_to_mesh_2.width, curve_to_mesh_2.height = 140.0, 100.0
			set_position_002_1.width, set_position_002_1.height = 140.0, 100.0
			transform_geometry_2.width, transform_geometry_2.height = 140.0, 100.0
			mix_001.width, mix_001.height = 140.0, 100.0
			flip_faces.width, flip_faces.height = 140.0, 100.0
			group_output_41.width, group_output_41.height = 140.0, 100.0
			reroute_001_7.width, reroute_001_7.height = 16.0, 100.0
			reroute_11.width, reroute_11.height = 16.0, 100.0
			set_curve_radius_2.width, set_curve_radius_2.height = 140.0, 100.0
			reroute_002_3.width, reroute_002_3.height = 16.0, 100.0
			spline_resolution.width, spline_resolution.height = 140.0, 100.0
			spline_length_1.width, spline_length_1.height = 140.0, 100.0
			spline_parameter_1.width, spline_parameter_1.height = 140.0, 100.0
			group_001_6.width, group_001_6.height = 140.0, 100.0
			set_spline_resolution.width, set_spline_resolution.height = 140.0, 100.0
			resample_curve.width, resample_curve.height = 140.0, 100.0
			switch_10.width, switch_10.height = 140.0, 100.0
			group_input_40.width, group_input_40.height = 140.0, 100.0
			group_15.width, group_15.height = 140.0, 100.0
			
			#initialize _curve_custom_profile links
			#mix_001.Result -> set_position_002_1.Position
			_curve_custom_profile.links.new(mix_001.outputs[1], set_position_002_1.inputs[2])
			#index_003_1.Index -> sample_index_001_2.Index
			_curve_custom_profile.links.new(index_003_1.outputs[0], sample_index_001_2.inputs[2])
			#position_001_3.Position -> mix_001.B
			_curve_custom_profile.links.new(position_001_3.outputs[0], mix_001.inputs[5])
			#set_curve_radius_2.Curve -> curve_to_mesh_2.Curve
			_curve_custom_profile.links.new(set_curve_radius_2.outputs[0], curve_to_mesh_2.inputs[0])
			#curve_to_mesh_2.Mesh -> set_position_002_1.Geometry
			_curve_custom_profile.links.new(curve_to_mesh_2.outputs[0], set_position_002_1.inputs[0])
			#instance_on_points_001_1.Instances -> realize_instances_2.Geometry
			_curve_custom_profile.links.new(instance_on_points_001_1.outputs[0], realize_instances_2.inputs[0])
			#sample_index_001_2.Value -> mix_001.A
			_curve_custom_profile.links.new(sample_index_001_2.outputs[0], mix_001.inputs[4])
			#position_001_3.Position -> sample_index_001_2.Value
			_curve_custom_profile.links.new(position_001_3.outputs[0], sample_index_001_2.inputs[1])
			#realize_instances_2.Geometry -> sample_index_001_2.Geometry
			_curve_custom_profile.links.new(realize_instances_2.outputs[0], sample_index_001_2.inputs[0])
			#group_input_40.Radius -> set_curve_radius_2.Radius
			_curve_custom_profile.links.new(group_input_40.outputs[8], set_curve_radius_2.inputs[2])
			#group_input_40.Factor -> mix_001.Factor
			_curve_custom_profile.links.new(group_input_40.outputs[7], mix_001.inputs[0])
			#flip_faces.Mesh -> group_output_41.Geometry
			_curve_custom_profile.links.new(flip_faces.outputs[0], group_output_41.inputs[0])
			#reroute_11.Output -> transform_geometry_2.Geometry
			_curve_custom_profile.links.new(reroute_11.outputs[0], transform_geometry_2.inputs[0])
			#transform_geometry_2.Geometry -> instance_on_points_001_1.Instance
			_curve_custom_profile.links.new(transform_geometry_2.outputs[0], instance_on_points_001_1.inputs[2])
			#reroute_001_7.Output -> curve_to_mesh_2.Profile Curve
			_curve_custom_profile.links.new(reroute_001_7.outputs[0], curve_to_mesh_2.inputs[1])
			#group_input_40.Scale -> instance_on_points_001_1.Scale
			_curve_custom_profile.links.new(group_input_40.outputs[6], instance_on_points_001_1.inputs[6])
			#group_input_40.Rotation X -> group_15.Angle
			_curve_custom_profile.links.new(group_input_40.outputs[5], group_15.inputs[0])
			#group_001_6.Output -> reroute_11.Input
			_curve_custom_profile.links.new(group_001_6.outputs[0], reroute_11.inputs[0])
			#group_input_40.Instance -> group_001_6.Input
			_curve_custom_profile.links.new(group_input_40.outputs[4], group_001_6.inputs[0])
			#group_input_40.Profile Radius -> group_001_6.Radius
			_curve_custom_profile.links.new(group_input_40.outputs[2], group_001_6.inputs[2])
			#group_input_40.Profile Rotation -> group_001_6.Rotation
			_curve_custom_profile.links.new(group_input_40.outputs[3], group_001_6.inputs[3])
			#set_position_002_1.Geometry -> flip_faces.Mesh
			_curve_custom_profile.links.new(set_position_002_1.outputs[0], flip_faces.inputs[0])
			#reroute_002_3.Output -> set_curve_radius_2.Curve
			_curve_custom_profile.links.new(reroute_002_3.outputs[0], set_curve_radius_2.inputs[0])
			#reroute_11.Output -> reroute_001_7.Input
			_curve_custom_profile.links.new(reroute_11.outputs[0], reroute_001_7.inputs[0])
			#group_input_40.Curve -> set_spline_resolution.Geometry
			_curve_custom_profile.links.new(group_input_40.outputs[0], set_spline_resolution.inputs[0])
			#switch_10.Output -> reroute_002_3.Input
			_curve_custom_profile.links.new(switch_10.outputs[0], reroute_002_3.inputs[0])
			#group_input_40.Profile Resolution -> group_001_6.Resolution
			_curve_custom_profile.links.new(group_input_40.outputs[1], group_001_6.inputs[1])
			#reroute_002_3.Output -> instance_on_points_001_1.Points
			_curve_custom_profile.links.new(reroute_002_3.outputs[0], instance_on_points_001_1.inputs[0])
			#group_input_40.Resolution -> set_spline_resolution.Resolution
			_curve_custom_profile.links.new(group_input_40.outputs[9], set_spline_resolution.inputs[2])
			#set_spline_resolution.Geometry -> resample_curve.Curve
			_curve_custom_profile.links.new(set_spline_resolution.outputs[0], resample_curve.inputs[0])
			#group_15.Rotation -> instance_on_points_001_1.Rotation
			_curve_custom_profile.links.new(group_15.outputs[0], instance_on_points_001_1.inputs[5])
			#resample_curve.Curve -> switch_10.True
			_curve_custom_profile.links.new(resample_curve.outputs[0], switch_10.inputs[2])
			#group_input_40.Curve -> switch_10.False
			_curve_custom_profile.links.new(group_input_40.outputs[0], switch_10.inputs[1])
			#group_input_40.Resample -> switch_10.Switch
			_curve_custom_profile.links.new(group_input_40.outputs[10], switch_10.inputs[0])
			return _curve_custom_profile

		_curve_custom_profile = _curve_custom_profile_node_group()

		#initialize _field_offset node group
		def _field_offset_node_group():
			_field_offset = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".field_offset")

			_field_offset.color_tag = 'NONE'
			_field_offset.description = ""

			
			#_field_offset interface
			#Socket Field
			field_socket_2 = _field_offset.interface.new_socket(name = "Field", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			field_socket_2.subtype = 'NONE'
			field_socket_2.default_value = (0.0, 0.0, 0.0)
			field_socket_2.min_value = -3.4028234663852886e+38
			field_socket_2.max_value = 3.4028234663852886e+38
			field_socket_2.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_7 = _field_offset.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			value_socket_7.attribute_domain = 'POINT'
			
			#Socket Field
			field_socket_3 = _field_offset.interface.new_socket(name = "Field", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			field_socket_3.subtype = 'NONE'
			field_socket_3.default_value = 0
			field_socket_3.min_value = -2147483648
			field_socket_3.max_value = 2147483647
			field_socket_3.attribute_domain = 'POINT'
			
			#Socket Field
			field_socket_4 = _field_offset.interface.new_socket(name = "Field", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			field_socket_4.subtype = 'NONE'
			field_socket_4.default_value = 0.0
			field_socket_4.min_value = -3.4028234663852886e+38
			field_socket_4.max_value = 3.4028234663852886e+38
			field_socket_4.attribute_domain = 'POINT'
			
			#Socket Field
			field_socket_5 = _field_offset.interface.new_socket(name = "Field", in_out='INPUT', socket_type = 'NodeSocketVector')
			field_socket_5.subtype = 'NONE'
			field_socket_5.default_value = (0.0, 0.0, 0.0)
			field_socket_5.min_value = -3.4028234663852886e+38
			field_socket_5.max_value = 3.4028234663852886e+38
			field_socket_5.attribute_domain = 'POINT'
			field_socket_5.hide_value = True
			
			#Socket Value
			value_socket_8 = _field_offset.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketBool')
			value_socket_8.attribute_domain = 'POINT'
			value_socket_8.hide_value = True
			
			#Socket Field
			field_socket_6 = _field_offset.interface.new_socket(name = "Field", in_out='INPUT', socket_type = 'NodeSocketInt')
			field_socket_6.subtype = 'NONE'
			field_socket_6.default_value = 0
			field_socket_6.min_value = -2147483648
			field_socket_6.max_value = 2147483647
			field_socket_6.attribute_domain = 'POINT'
			field_socket_6.hide_value = True
			
			#Socket Field
			field_socket_7 = _field_offset.interface.new_socket(name = "Field", in_out='INPUT', socket_type = 'NodeSocketFloat')
			field_socket_7.subtype = 'NONE'
			field_socket_7.default_value = 0.0
			field_socket_7.min_value = -3.4028234663852886e+38
			field_socket_7.max_value = 3.4028234663852886e+38
			field_socket_7.attribute_domain = 'POINT'
			field_socket_7.hide_value = True
			
			#Socket Offset
			offset_socket_4 = _field_offset.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket_4.subtype = 'NONE'
			offset_socket_4.default_value = 0
			offset_socket_4.min_value = -2147483648
			offset_socket_4.max_value = 2147483647
			offset_socket_4.attribute_domain = 'POINT'
			
			
			#initialize _field_offset nodes
			#node Group Output
			group_output_42 = _field_offset.nodes.new("NodeGroupOutput")
			group_output_42.name = "Group Output"
			group_output_42.is_active_output = True
			
			#node Math.001
			math_001_7 = _field_offset.nodes.new("ShaderNodeMath")
			math_001_7.name = "Math.001"
			math_001_7.operation = 'ADD'
			math_001_7.use_clamp = False
			
			#node Evaluate at Index
			evaluate_at_index_1 = _field_offset.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_1.name = "Evaluate at Index"
			evaluate_at_index_1.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_1.domain = 'POINT'
			
			#node Group Input
			group_input_41 = _field_offset.nodes.new("NodeGroupInput")
			group_input_41.name = "Group Input"
			
			#node Evaluate at Index.001
			evaluate_at_index_001_1 = _field_offset.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001_1.name = "Evaluate at Index.001"
			evaluate_at_index_001_1.data_type = 'BOOLEAN'
			evaluate_at_index_001_1.domain = 'POINT'
			
			#node Index
			index_4 = _field_offset.nodes.new("GeometryNodeInputIndex")
			index_4.name = "Index"
			
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
			group_output_42.location = (407.6440124511719, 0.0)
			math_001_7.location = (0.5235366821289062, 15.3753662109375)
			evaluate_at_index_1.location = (217.64404296875, 102.376708984375)
			group_input_41.location = (-417.64404296875, 0.0)
			evaluate_at_index_001_1.location = (220.0, -60.0)
			index_4.location = (-260.0, -40.0)
			evaluate_at_index_002.location = (220.0, -220.0)
			evaluate_at_index_003.location = (220.0, -380.0)
			
			#Set dimensions
			group_output_42.width, group_output_42.height = 140.0, 100.0
			math_001_7.width, math_001_7.height = 140.0, 100.0
			evaluate_at_index_1.width, evaluate_at_index_1.height = 140.0, 100.0
			group_input_41.width, group_input_41.height = 140.0, 100.0
			evaluate_at_index_001_1.width, evaluate_at_index_001_1.height = 140.0, 100.0
			index_4.width, index_4.height = 140.0, 100.0
			evaluate_at_index_002.width, evaluate_at_index_002.height = 140.0, 100.0
			evaluate_at_index_003.width, evaluate_at_index_003.height = 140.0, 100.0
			
			#initialize _field_offset links
			#index_4.Index -> math_001_7.Value
			_field_offset.links.new(index_4.outputs[0], math_001_7.inputs[0])
			#math_001_7.Value -> evaluate_at_index_1.Index
			_field_offset.links.new(math_001_7.outputs[0], evaluate_at_index_1.inputs[0])
			#group_input_41.Field -> evaluate_at_index_1.Value
			_field_offset.links.new(group_input_41.outputs[0], evaluate_at_index_1.inputs[1])
			#group_input_41.Offset -> math_001_7.Value
			_field_offset.links.new(group_input_41.outputs[4], math_001_7.inputs[1])
			#evaluate_at_index_1.Value -> group_output_42.Field
			_field_offset.links.new(evaluate_at_index_1.outputs[0], group_output_42.inputs[0])
			#math_001_7.Value -> evaluate_at_index_001_1.Index
			_field_offset.links.new(math_001_7.outputs[0], evaluate_at_index_001_1.inputs[0])
			#group_input_41.Value -> evaluate_at_index_001_1.Value
			_field_offset.links.new(group_input_41.outputs[1], evaluate_at_index_001_1.inputs[1])
			#evaluate_at_index_001_1.Value -> group_output_42.Value
			_field_offset.links.new(evaluate_at_index_001_1.outputs[0], group_output_42.inputs[1])
			#math_001_7.Value -> evaluate_at_index_002.Index
			_field_offset.links.new(math_001_7.outputs[0], evaluate_at_index_002.inputs[0])
			#group_input_41.Field -> evaluate_at_index_002.Value
			_field_offset.links.new(group_input_41.outputs[2], evaluate_at_index_002.inputs[1])
			#evaluate_at_index_002.Value -> group_output_42.Field
			_field_offset.links.new(evaluate_at_index_002.outputs[0], group_output_42.inputs[2])
			#math_001_7.Value -> evaluate_at_index_003.Index
			_field_offset.links.new(math_001_7.outputs[0], evaluate_at_index_003.inputs[0])
			#group_input_41.Field -> evaluate_at_index_003.Value
			_field_offset.links.new(group_input_41.outputs[3], evaluate_at_index_003.inputs[1])
			#evaluate_at_index_003.Value -> group_output_42.Field
			_field_offset.links.new(evaluate_at_index_003.outputs[0], group_output_42.inputs[3])
			return _field_offset

		_field_offset = _field_offset_node_group()

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
			group_input_42 = _sec_struct_counter.nodes.new("NodeGroupInput")
			group_input_42.name = "Group Input"
			
			#node Reroute.005
			reroute_005_1 = _sec_struct_counter.nodes.new("NodeReroute")
			reroute_005_1.name = "Reroute.005"
			#node Named Attribute.001
			named_attribute_001_5 = _sec_struct_counter.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001_5.name = "Named Attribute.001"
			named_attribute_001_5.data_type = 'INT'
			#Name
			named_attribute_001_5.inputs[0].default_value = "sec_struct"
			
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
			compare_009 = _sec_struct_counter.nodes.new("FunctionNodeCompare")
			compare_009.name = "Compare.009"
			compare_009.data_type = 'INT'
			compare_009.mode = 'ELEMENT'
			compare_009.operation = 'NOT_EQUAL'
			
			#node Accumulate Field.004
			accumulate_field_004 = _sec_struct_counter.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_004.name = "Accumulate Field.004"
			accumulate_field_004.data_type = 'INT'
			accumulate_field_004.domain = 'POINT'
			#Group Index
			accumulate_field_004.inputs[1].default_value = 0
			
			#node Compare.010
			compare_010 = _sec_struct_counter.nodes.new("FunctionNodeCompare")
			compare_010.name = "Compare.010"
			compare_010.data_type = 'INT'
			compare_010.mode = 'ELEMENT'
			compare_010.operation = 'NOT_EQUAL'
			
			#node Reroute
			reroute_12 = _sec_struct_counter.nodes.new("NodeReroute")
			reroute_12.name = "Reroute"
			#node Boolean Math
			boolean_math_6 = _sec_struct_counter.nodes.new("FunctionNodeBooleanMath")
			boolean_math_6.name = "Boolean Math"
			boolean_math_6.operation = 'OR'
			#Boolean_001
			boolean_math_6.inputs[1].default_value = False
			
			#node Group Output
			group_output_43 = _sec_struct_counter.nodes.new("NodeGroupOutput")
			group_output_43.name = "Group Output"
			group_output_43.is_active_output = True
			
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
			group_input_42.location = (-500.1279296875, 0.0)
			reroute_005_1.location = (-119.8720703125, -60.0)
			named_attribute_001_5.location = (-300.0, 120.0)
			group_004_1.location = (-20.0, -220.0)
			compare_009.location = (140.1279296875, 60.0)
			accumulate_field_004.location = (460.0, 40.0)
			compare_010.location = (140.0, -140.0)
			reroute_12.location = (320.0, -60.0)
			boolean_math_6.location = (300.0, -140.0)
			group_output_43.location = (796.4706420898438, 27.943008422851562)
			group_003_1.location = (-19.8720703125, 60.0)
			
			#Set dimensions
			group_input_42.width, group_input_42.height = 140.0, 100.0
			reroute_005_1.width, reroute_005_1.height = 16.0, 100.0
			named_attribute_001_5.width, named_attribute_001_5.height = 140.0, 100.0
			group_004_1.width, group_004_1.height = 140.0, 100.0
			compare_009.width, compare_009.height = 140.0, 100.0
			accumulate_field_004.width, accumulate_field_004.height = 140.0, 100.0
			compare_010.width, compare_010.height = 140.0, 100.0
			reroute_12.width, reroute_12.height = 16.0, 100.0
			boolean_math_6.width, boolean_math_6.height = 140.0, 100.0
			group_output_43.width, group_output_43.height = 140.0, 100.0
			group_003_1.width, group_003_1.height = 140.0, 100.0
			
			#initialize _sec_struct_counter links
			#reroute_12.Output -> accumulate_field_004.Value
			_sec_struct_counter.links.new(reroute_12.outputs[0], accumulate_field_004.inputs[0])
			#reroute_005_1.Output -> group_003_1.Field
			_sec_struct_counter.links.new(reroute_005_1.outputs[0], group_003_1.inputs[2])
			#reroute_005_1.Output -> compare_009.A
			_sec_struct_counter.links.new(reroute_005_1.outputs[0], compare_009.inputs[2])
			#named_attribute_001_5.Attribute -> reroute_005_1.Input
			_sec_struct_counter.links.new(named_attribute_001_5.outputs[0], reroute_005_1.inputs[0])
			#group_003_1.Field -> compare_009.B
			_sec_struct_counter.links.new(group_003_1.outputs[2], compare_009.inputs[3])
			#accumulate_field_004.Trailing -> group_output_43.Trailing
			_sec_struct_counter.links.new(accumulate_field_004.outputs[1], group_output_43.inputs[1])
			#accumulate_field_004.Leading -> group_output_43.Leading
			_sec_struct_counter.links.new(accumulate_field_004.outputs[0], group_output_43.inputs[0])
			#accumulate_field_004.Total -> group_output_43.Total
			_sec_struct_counter.links.new(accumulate_field_004.outputs[2], group_output_43.inputs[2])
			#reroute_12.Output -> group_output_43.Border
			_sec_struct_counter.links.new(reroute_12.outputs[0], group_output_43.inputs[3])
			#reroute_005_1.Output -> group_004_1.Field
			_sec_struct_counter.links.new(reroute_005_1.outputs[0], group_004_1.inputs[2])
			#reroute_005_1.Output -> compare_010.A
			_sec_struct_counter.links.new(reroute_005_1.outputs[0], compare_010.inputs[2])
			#group_004_1.Field -> compare_010.B
			_sec_struct_counter.links.new(group_004_1.outputs[2], compare_010.inputs[3])
			#compare_009.Result -> reroute_12.Input
			_sec_struct_counter.links.new(compare_009.outputs[0], reroute_12.inputs[0])
			#compare_010.Result -> boolean_math_6.Boolean
			_sec_struct_counter.links.new(compare_010.outputs[0], boolean_math_6.inputs[0])
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
			geometry_socket_10 = _bs_smooth.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_10.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_11 = _bs_smooth.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_11.attribute_domain = 'POINT'
			
			#Socket Factor
			factor_socket_1 = _bs_smooth.interface.new_socket(name = "Factor", in_out='INPUT', socket_type = 'NodeSocketFloat')
			factor_socket_1.subtype = 'FACTOR'
			factor_socket_1.default_value = 1.0
			factor_socket_1.min_value = 0.0
			factor_socket_1.max_value = 1.0
			factor_socket_1.attribute_domain = 'POINT'
			
			#Socket Iterations
			iterations_socket = _bs_smooth.interface.new_socket(name = "Iterations", in_out='INPUT', socket_type = 'NodeSocketInt')
			iterations_socket.subtype = 'NONE'
			iterations_socket.default_value = 2
			iterations_socket.min_value = 0
			iterations_socket.max_value = 2147483647
			iterations_socket.attribute_domain = 'POINT'
			
			
			#initialize _bs_smooth nodes
			#node Group Output
			group_output_44 = _bs_smooth.nodes.new("NodeGroupOutput")
			group_output_44.name = "Group Output"
			group_output_44.is_active_output = True
			
			#node Set Position
			set_position_3 = _bs_smooth.nodes.new("GeometryNodeSetPosition")
			set_position_3.name = "Set Position"
			#Offset
			set_position_3.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Mix.002
			mix_002 = _bs_smooth.nodes.new("ShaderNodeMix")
			mix_002.name = "Mix.002"
			mix_002.blend_type = 'MIX'
			mix_002.clamp_factor = True
			mix_002.clamp_result = False
			mix_002.data_type = 'VECTOR'
			mix_002.factor_mode = 'UNIFORM'
			
			#node Position.001
			position_001_4 = _bs_smooth.nodes.new("GeometryNodeInputPosition")
			position_001_4.name = "Position.001"
			
			#node Blur Attribute
			blur_attribute = _bs_smooth.nodes.new("GeometryNodeBlurAttribute")
			blur_attribute.name = "Blur Attribute"
			blur_attribute.data_type = 'FLOAT_VECTOR'
			
			#node Group Input
			group_input_43 = _bs_smooth.nodes.new("NodeGroupInput")
			group_input_43.name = "Group Input"
			
			#node Boolean Math.004
			boolean_math_004_3 = _bs_smooth.nodes.new("FunctionNodeBooleanMath")
			boolean_math_004_3.name = "Boolean Math.004"
			boolean_math_004_3.operation = 'NOT'
			
			#node Boolean Math.002
			boolean_math_002_7 = _bs_smooth.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_7.name = "Boolean Math.002"
			boolean_math_002_7.operation = 'AND'
			
			#node Group
			group_16 = _bs_smooth.nodes.new("GeometryNodeGroup")
			group_16.name = "Group"
			group_16.node_tree = _sec_struct_counter
			
			#node Endpoint Selection.004
			endpoint_selection_004_1 = _bs_smooth.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_004_1.name = "Endpoint Selection.004"
			#Start Size
			endpoint_selection_004_1.inputs[0].default_value = 1
			#End Size
			endpoint_selection_004_1.inputs[1].default_value = 1
			
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
			group_output_44.location = (591.18408203125, 0.0)
			set_position_3.location = (401.18408203125, 199.23532104492188)
			mix_002.location = (218.81591796875, 80.76467895507812)
			position_001_4.location = (-61.18408203125, -39.235321044921875)
			blur_attribute.location = (-58.81591796875, -120.76467895507812)
			group_input_43.location = (-615.6842041015625, 115.17381286621094)
			boolean_math_004_3.location = (-380.0, -160.0)
			boolean_math_002_7.location = (39.807212829589844, 161.80430603027344)
			group_16.location = (-620.0, -40.0)
			endpoint_selection_004_1.location = (-620.0, -280.0)
			boolean_math_7.location = (-120.0, 140.0)
			group_021.location = (40.0, 260.0)
			
			#Set dimensions
			group_output_44.width, group_output_44.height = 140.0, 100.0
			set_position_3.width, set_position_3.height = 140.0, 100.0
			mix_002.width, mix_002.height = 140.0, 100.0
			position_001_4.width, position_001_4.height = 140.0, 100.0
			blur_attribute.width, blur_attribute.height = 140.0, 100.0
			group_input_43.width, group_input_43.height = 140.0, 100.0
			boolean_math_004_3.width, boolean_math_004_3.height = 140.0, 100.0
			boolean_math_002_7.width, boolean_math_002_7.height = 140.0, 100.0
			group_16.width, group_16.height = 140.0, 100.0
			endpoint_selection_004_1.width, endpoint_selection_004_1.height = 140.0, 100.0
			boolean_math_7.width, boolean_math_7.height = 140.0, 100.0
			group_021.width, group_021.height = 140.0, 100.0
			
			#initialize _bs_smooth links
			#boolean_math_004_3.Boolean -> blur_attribute.Weight
			_bs_smooth.links.new(boolean_math_004_3.outputs[0], blur_attribute.inputs[2])
			#blur_attribute.Value -> mix_002.B
			_bs_smooth.links.new(blur_attribute.outputs[0], mix_002.inputs[5])
			#position_001_4.Position -> blur_attribute.Value
			_bs_smooth.links.new(position_001_4.outputs[0], blur_attribute.inputs[0])
			#mix_002.Result -> set_position_3.Position
			_bs_smooth.links.new(mix_002.outputs[1], set_position_3.inputs[2])
			#position_001_4.Position -> mix_002.A
			_bs_smooth.links.new(position_001_4.outputs[0], mix_002.inputs[4])
			#group_021.Is Sheet -> boolean_math_002_7.Boolean
			_bs_smooth.links.new(group_021.outputs[1], boolean_math_002_7.inputs[0])
			#group_input_43.Geometry -> set_position_3.Geometry
			_bs_smooth.links.new(group_input_43.outputs[0], set_position_3.inputs[0])
			#group_input_43.Factor -> mix_002.Factor
			_bs_smooth.links.new(group_input_43.outputs[1], mix_002.inputs[0])
			#set_position_3.Geometry -> group_output_44.Geometry
			_bs_smooth.links.new(set_position_3.outputs[0], group_output_44.inputs[0])
			#group_input_43.Iterations -> blur_attribute.Iterations
			_bs_smooth.links.new(group_input_43.outputs[2], blur_attribute.inputs[1])
			#group_16.Border -> boolean_math_7.Boolean
			_bs_smooth.links.new(group_16.outputs[3], boolean_math_7.inputs[0])
			#boolean_math_002_7.Boolean -> set_position_3.Selection
			_bs_smooth.links.new(boolean_math_002_7.outputs[0], set_position_3.inputs[1])
			#boolean_math_7.Boolean -> boolean_math_002_7.Boolean
			_bs_smooth.links.new(boolean_math_7.outputs[0], boolean_math_002_7.inputs[1])
			#group_16.Border -> boolean_math_004_3.Boolean
			_bs_smooth.links.new(group_16.outputs[3], boolean_math_004_3.inputs[0])
			return _bs_smooth

		_bs_smooth = _bs_smooth_node_group()

		#initialize _expand_selection node group
		def _expand_selection_node_group():
			_expand_selection = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".expand_selection")

			_expand_selection.color_tag = 'NONE'
			_expand_selection.description = ""

			
			#_expand_selection interface
			#Socket Boolean
			boolean_socket_3 = _expand_selection.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket_3.attribute_domain = 'POINT'
			
			#Socket Input
			input_socket_4 = _expand_selection.interface.new_socket(name = "Input", in_out='INPUT', socket_type = 'NodeSocketBool')
			input_socket_4.attribute_domain = 'POINT'
			
			#Socket Offset
			offset_socket_5 = _expand_selection.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket_5.subtype = 'NONE'
			offset_socket_5.default_value = 1
			offset_socket_5.min_value = -2147483648
			offset_socket_5.max_value = 2147483647
			offset_socket_5.attribute_domain = 'POINT'
			
			
			#initialize _expand_selection nodes
			#node Group Output
			group_output_45 = _expand_selection.nodes.new("NodeGroupOutput")
			group_output_45.name = "Group Output"
			group_output_45.is_active_output = True
			
			#node Boolean Math
			boolean_math_8 = _expand_selection.nodes.new("FunctionNodeBooleanMath")
			boolean_math_8.name = "Boolean Math"
			boolean_math_8.operation = 'OR'
			
			#node Boolean Math.001
			boolean_math_001_8 = _expand_selection.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_8.name = "Boolean Math.001"
			boolean_math_001_8.operation = 'OR'
			
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
			group_input_44 = _expand_selection.nodes.new("NodeGroupInput")
			group_input_44.name = "Group Input"
			
			#node Math
			math_9 = _expand_selection.nodes.new("ShaderNodeMath")
			math_9.name = "Math"
			math_9.operation = 'MULTIPLY'
			math_9.use_clamp = False
			#Value_001
			math_9.inputs[1].default_value = -1.0
			
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
			group_output_45.location = (420.0, 0.0)
			boolean_math_8.location = (-50.0, 0.0)
			boolean_math_001_8.location = (230.0, 60.0)
			group_025.location = (-230.0, -140.0)
			group_input_44.location = (-637.21630859375, 234.8535614013672)
			math_9.location = (-640.0, 120.0)
			group_024.location = (-230.0, 140.0)
			
			#Set dimensions
			group_output_45.width, group_output_45.height = 140.0, 100.0
			boolean_math_8.width, boolean_math_8.height = 140.0, 100.0
			boolean_math_001_8.width, boolean_math_001_8.height = 140.0, 100.0
			group_025.width, group_025.height = 140.0, 100.0
			group_input_44.width, group_input_44.height = 140.0, 100.0
			math_9.width, math_9.height = 140.0, 100.0
			group_024.width, group_024.height = 140.0, 100.0
			
			#initialize _expand_selection links
			#group_025.Value -> boolean_math_8.Boolean
			_expand_selection.links.new(group_025.outputs[1], boolean_math_8.inputs[1])
			#group_input_44.Input -> group_025.Value
			_expand_selection.links.new(group_input_44.outputs[0], group_025.inputs[1])
			#group_input_44.Input -> group_024.Value
			_expand_selection.links.new(group_input_44.outputs[0], group_024.inputs[1])
			#group_024.Value -> boolean_math_8.Boolean
			_expand_selection.links.new(group_024.outputs[1], boolean_math_8.inputs[0])
			#boolean_math_8.Boolean -> boolean_math_001_8.Boolean
			_expand_selection.links.new(boolean_math_8.outputs[0], boolean_math_001_8.inputs[1])
			#group_input_44.Input -> boolean_math_001_8.Boolean
			_expand_selection.links.new(group_input_44.outputs[0], boolean_math_001_8.inputs[0])
			#boolean_math_001_8.Boolean -> group_output_45.Boolean
			_expand_selection.links.new(boolean_math_001_8.outputs[0], group_output_45.inputs[0])
			#group_input_44.Offset -> group_024.Offset
			_expand_selection.links.new(group_input_44.outputs[1], group_024.inputs[4])
			#group_input_44.Offset -> math_9.Value
			_expand_selection.links.new(group_input_44.outputs[1], math_9.inputs[0])
			#math_9.Value -> group_025.Offset
			_expand_selection.links.new(math_9.outputs[0], group_025.inputs[4])
			return _expand_selection

		_expand_selection = _expand_selection_node_group()

		#initialize is_alpha_carbon node group
		def is_alpha_carbon_node_group():
			is_alpha_carbon = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Is Alpha Carbon")

			is_alpha_carbon.color_tag = 'INPUT'
			is_alpha_carbon.description = ""

			
			#is_alpha_carbon interface
			#Socket Selection
			selection_socket_17 = is_alpha_carbon.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket_17.attribute_domain = 'POINT'
			selection_socket_17.description = "True if atom is an alpha carbon of an amino acid"
			
			#Socket Inverted
			inverted_socket_8 = is_alpha_carbon.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket_8.attribute_domain = 'POINT'
			
			#Socket And
			and_socket_8 = is_alpha_carbon.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket_8.attribute_domain = 'POINT'
			and_socket_8.hide_value = True
			
			#Socket Or
			or_socket_7 = is_alpha_carbon.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket_7.attribute_domain = 'POINT'
			or_socket_7.hide_value = True
			
			
			#initialize is_alpha_carbon nodes
			#node Group Output
			group_output_46 = is_alpha_carbon.nodes.new("NodeGroupOutput")
			group_output_46.name = "Group Output"
			group_output_46.is_active_output = True
			
			#node Group Input
			group_input_45 = is_alpha_carbon.nodes.new("NodeGroupInput")
			group_input_45.name = "Group Input"
			
			#node Boolean Math.001
			boolean_math_001_9 = is_alpha_carbon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_9.name = "Boolean Math.001"
			boolean_math_001_9.operation = 'AND'
			
			#node Group.001
			group_001_7 = is_alpha_carbon.nodes.new("GeometryNodeGroup")
			group_001_7.name = "Group.001"
			group_001_7.node_tree = fallback_boolean
			#Socket_2
			group_001_7.inputs[0].default_value = "is_alpha_carbon"
			
			#node Group.002
			group_002_2 = is_alpha_carbon.nodes.new("GeometryNodeGroup")
			group_002_2.name = "Group.002"
			group_002_2.node_tree = _mn_select_peptide
			group_002_2.outputs[0].hide = True
			group_002_2.outputs[1].hide = True
			group_002_2.outputs[2].hide = True
			
			#node Boolean Math.002
			boolean_math_002_8 = is_alpha_carbon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_8.name = "Boolean Math.002"
			boolean_math_002_8.operation = 'OR'
			
			#node Boolean Math
			boolean_math_9 = is_alpha_carbon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_9.name = "Boolean Math"
			boolean_math_9.operation = 'NOT'
			
			
			
			
			#Set locations
			group_output_46.location = (520.0, 0.0)
			group_input_45.location = (-200.0, 0.0)
			boolean_math_001_9.location = (160.0, 0.0)
			group_001_7.location = (-88.33343505859375, -180.0)
			group_002_2.location = (-290.4490661621094, -180.0)
			boolean_math_002_8.location = (340.0, 0.0)
			boolean_math_9.location = (340.0, -140.0)
			
			#Set dimensions
			group_output_46.width, group_output_46.height = 140.0, 100.0
			group_input_45.width, group_input_45.height = 140.0, 100.0
			boolean_math_001_9.width, boolean_math_001_9.height = 140.0, 100.0
			group_001_7.width, group_001_7.height = 208.33343505859375, 100.0
			group_002_2.width, group_002_2.height = 170.44906616210938, 100.0
			boolean_math_002_8.width, boolean_math_002_8.height = 140.0, 100.0
			boolean_math_9.width, boolean_math_9.height = 140.0, 100.0
			
			#initialize is_alpha_carbon links
			#group_input_45.And -> boolean_math_001_9.Boolean
			is_alpha_carbon.links.new(group_input_45.outputs[0], boolean_math_001_9.inputs[0])
			#boolean_math_002_8.Boolean -> group_output_46.Selection
			is_alpha_carbon.links.new(boolean_math_002_8.outputs[0], group_output_46.inputs[0])
			#group_001_7.Boolean -> boolean_math_001_9.Boolean
			is_alpha_carbon.links.new(group_001_7.outputs[0], boolean_math_001_9.inputs[1])
			#group_002_2.Is Alpha Carbon -> group_001_7.Fallback
			is_alpha_carbon.links.new(group_002_2.outputs[3], group_001_7.inputs[1])
			#boolean_math_001_9.Boolean -> boolean_math_002_8.Boolean
			is_alpha_carbon.links.new(boolean_math_001_9.outputs[0], boolean_math_002_8.inputs[0])
			#group_input_45.Or -> boolean_math_002_8.Boolean
			is_alpha_carbon.links.new(group_input_45.outputs[1], boolean_math_002_8.inputs[1])
			#boolean_math_002_8.Boolean -> boolean_math_9.Boolean
			is_alpha_carbon.links.new(boolean_math_002_8.outputs[0], boolean_math_9.inputs[0])
			#boolean_math_9.Boolean -> group_output_46.Inverted
			is_alpha_carbon.links.new(boolean_math_9.outputs[0], group_output_46.inputs[1])
			return is_alpha_carbon

		is_alpha_carbon = is_alpha_carbon_node_group()

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
			index_socket_1 = group_pick.interface.new_socket(name = "Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			index_socket_1.subtype = 'NONE'
			index_socket_1.default_value = 0
			index_socket_1.min_value = 0
			index_socket_1.max_value = 2147483647
			index_socket_1.attribute_domain = 'POINT'
			index_socket_1.description = "Index of picked item. Returns -1 if not a valid pick."
			
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
			group_output_47 = group_pick.nodes.new("NodeGroupOutput")
			group_output_47.name = "Group Output"
			group_output_47.is_active_output = True
			
			#node Group Input
			group_input_46 = group_pick.nodes.new("NodeGroupInput")
			group_input_46.name = "Group Input"
			
			#node Switch
			switch_11 = group_pick.nodes.new("GeometryNodeSwitch")
			switch_11.name = "Switch"
			switch_11.input_type = 'INT'
			#False
			switch_11.inputs[1].default_value = 0
			
			#node Index
			index_5 = group_pick.nodes.new("GeometryNodeInputIndex")
			index_5.name = "Index"
			
			#node Accumulate Field
			accumulate_field_2 = group_pick.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_2.name = "Accumulate Field"
			accumulate_field_2.data_type = 'INT'
			accumulate_field_2.domain = 'POINT'
			
			#node Accumulate Field.002
			accumulate_field_002 = group_pick.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_002.name = "Accumulate Field.002"
			accumulate_field_002.data_type = 'INT'
			accumulate_field_002.domain = 'POINT'
			
			#node Switch.001
			switch_001_2 = group_pick.nodes.new("GeometryNodeSwitch")
			switch_001_2.name = "Switch.001"
			switch_001_2.input_type = 'INT'
			#False
			switch_001_2.inputs[1].default_value = -1
			
			#node Compare.003
			compare_003_2 = group_pick.nodes.new("FunctionNodeCompare")
			compare_003_2.name = "Compare.003"
			compare_003_2.data_type = 'INT'
			compare_003_2.mode = 'ELEMENT'
			compare_003_2.operation = 'EQUAL'
			#B_INT
			compare_003_2.inputs[3].default_value = 1
			
			#node Reroute.001
			reroute_001_8 = group_pick.nodes.new("NodeReroute")
			reroute_001_8.name = "Reroute.001"
			#node Reroute.002
			reroute_002_4 = group_pick.nodes.new("NodeReroute")
			reroute_002_4.name = "Reroute.002"
			
			
			
			#Set locations
			group_output_47.location = (462.9173889160156, 0.0)
			group_input_46.location = (-472.9173889160156, 0.0)
			switch_11.location = (-120.0, -20.0)
			index_5.location = (-480.0, -120.0)
			accumulate_field_2.location = (60.0, -20.0)
			accumulate_field_002.location = (-120.0, 180.0)
			switch_001_2.location = (240.0, -20.0)
			compare_003_2.location = (60.0, 180.0)
			reroute_001_8.location = (-260.0, -100.0)
			reroute_002_4.location = (-260.0, -60.0)
			
			#Set dimensions
			group_output_47.width, group_output_47.height = 140.0, 100.0
			group_input_46.width, group_input_46.height = 140.0, 100.0
			switch_11.width, switch_11.height = 140.0, 100.0
			index_5.width, index_5.height = 140.0, 100.0
			accumulate_field_2.width, accumulate_field_2.height = 140.0, 100.0
			accumulate_field_002.width, accumulate_field_002.height = 140.0, 100.0
			switch_001_2.width, switch_001_2.height = 140.0, 100.0
			compare_003_2.width, compare_003_2.height = 138.9921875, 100.0
			reroute_001_8.width, reroute_001_8.height = 16.0, 100.0
			reroute_002_4.width, reroute_002_4.height = 16.0, 100.0
			
			#initialize group_pick links
			#switch_11.Output -> accumulate_field_2.Value
			group_pick.links.new(switch_11.outputs[0], accumulate_field_2.inputs[0])
			#compare_003_2.Result -> switch_001_2.Switch
			group_pick.links.new(compare_003_2.outputs[0], switch_001_2.inputs[0])
			#accumulate_field_2.Total -> switch_001_2.True
			group_pick.links.new(accumulate_field_2.outputs[2], switch_001_2.inputs[2])
			#reroute_001_8.Output -> accumulate_field_2.Group ID
			group_pick.links.new(reroute_001_8.outputs[0], accumulate_field_2.inputs[1])
			#reroute_001_8.Output -> accumulate_field_002.Group ID
			group_pick.links.new(reroute_001_8.outputs[0], accumulate_field_002.inputs[1])
			#reroute_002_4.Output -> switch_11.Switch
			group_pick.links.new(reroute_002_4.outputs[0], switch_11.inputs[0])
			#reroute_002_4.Output -> accumulate_field_002.Value
			group_pick.links.new(reroute_002_4.outputs[0], accumulate_field_002.inputs[0])
			#index_5.Index -> switch_11.True
			group_pick.links.new(index_5.outputs[0], switch_11.inputs[2])
			#accumulate_field_002.Total -> compare_003_2.A
			group_pick.links.new(accumulate_field_002.outputs[2], compare_003_2.inputs[2])
			#group_input_46.Group ID -> reroute_001_8.Input
			group_pick.links.new(group_input_46.outputs[1], reroute_001_8.inputs[0])
			#group_input_46.Pick -> reroute_002_4.Input
			group_pick.links.new(group_input_46.outputs[0], reroute_002_4.inputs[0])
			#switch_001_2.Output -> group_output_47.Index
			group_pick.links.new(switch_001_2.outputs[0], group_output_47.inputs[1])
			#compare_003_2.Result -> group_output_47.Is Valid
			group_pick.links.new(compare_003_2.outputs[0], group_output_47.inputs[0])
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
			index_socket_2 = group_pick_vector.interface.new_socket(name = "Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			index_socket_2.subtype = 'NONE'
			index_socket_2.default_value = 0
			index_socket_2.min_value = -2147483648
			index_socket_2.max_value = 2147483647
			index_socket_2.attribute_domain = 'POINT'
			index_socket_2.description = "Picked Index for the Group"
			
			#Socket Vector
			vector_socket_1 = group_pick_vector.interface.new_socket(name = "Vector", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			vector_socket_1.subtype = 'NONE'
			vector_socket_1.default_value = (0.0, 0.0, 0.0)
			vector_socket_1.min_value = -3.4028234663852886e+38
			vector_socket_1.max_value = 3.4028234663852886e+38
			vector_socket_1.attribute_domain = 'POINT'
			vector_socket_1.description = "Picked vector for the group"
			
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
			position_socket_1 = group_pick_vector.interface.new_socket(name = "Position", in_out='INPUT', socket_type = 'NodeSocketVector')
			position_socket_1.subtype = 'NONE'
			position_socket_1.default_value = (0.0, 0.0, 0.0)
			position_socket_1.min_value = -3.4028234663852886e+38
			position_socket_1.max_value = 3.4028234663852886e+38
			position_socket_1.attribute_domain = 'POINT'
			position_socket_1.description = "Vector field to pick vlaue for, defaults to Position"
			
			
			#initialize group_pick_vector nodes
			#node Group Output
			group_output_48 = group_pick_vector.nodes.new("NodeGroupOutput")
			group_output_48.name = "Group Output"
			group_output_48.is_active_output = True
			
			#node Group Input
			group_input_47 = group_pick_vector.nodes.new("NodeGroupInput")
			group_input_47.name = "Group Input"
			
			#node Evaluate at Index.001
			evaluate_at_index_001_2 = group_pick_vector.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001_2.name = "Evaluate at Index.001"
			evaluate_at_index_001_2.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_001_2.domain = 'POINT'
			
			#node Switch.002
			switch_002 = group_pick_vector.nodes.new("GeometryNodeSwitch")
			switch_002.name = "Switch.002"
			switch_002.input_type = 'VECTOR'
			#False
			switch_002.inputs[1].default_value = (0.0, 0.0, 0.0)
			
			#node Group
			group_17 = group_pick_vector.nodes.new("GeometryNodeGroup")
			group_17.name = "Group"
			group_17.node_tree = group_pick
			
			
			
			
			#Set locations
			group_output_48.location = (-40.0, -20.0)
			group_input_47.location = (-740.0, -80.0)
			evaluate_at_index_001_2.location = (-380.0, -180.0)
			switch_002.location = (-220.0, -60.0)
			group_17.location = (-560.0, -20.0)
			
			#Set dimensions
			group_output_48.width, group_output_48.height = 140.0, 100.0
			group_input_47.width, group_input_47.height = 140.0, 100.0
			evaluate_at_index_001_2.width, evaluate_at_index_001_2.height = 132.09918212890625, 100.0
			switch_002.width, switch_002.height = 140.0, 100.0
			group_17.width, group_17.height = 140.0, 100.0
			
			#initialize group_pick_vector links
			#group_17.Is Valid -> switch_002.Switch
			group_pick_vector.links.new(group_17.outputs[0], switch_002.inputs[0])
			#group_17.Index -> evaluate_at_index_001_2.Index
			group_pick_vector.links.new(group_17.outputs[1], evaluate_at_index_001_2.inputs[0])
			#evaluate_at_index_001_2.Value -> switch_002.True
			group_pick_vector.links.new(evaluate_at_index_001_2.outputs[0], switch_002.inputs[2])
			#group_17.Index -> group_output_48.Index
			group_pick_vector.links.new(group_17.outputs[1], group_output_48.inputs[1])
			#group_17.Is Valid -> group_output_48.Is Valid
			group_pick_vector.links.new(group_17.outputs[0], group_output_48.inputs[0])
			#switch_002.Output -> group_output_48.Vector
			group_pick_vector.links.new(switch_002.outputs[0], group_output_48.inputs[2])
			#group_input_47.Group ID -> group_17.Group ID
			group_pick_vector.links.new(group_input_47.outputs[1], group_17.inputs[1])
			#group_input_47.Pick -> group_17.Pick
			group_pick_vector.links.new(group_input_47.outputs[0], group_17.inputs[0])
			#group_input_47.Position -> evaluate_at_index_001_2.Value
			group_pick_vector.links.new(group_input_47.outputs[2], evaluate_at_index_001_2.inputs[1])
			return group_pick_vector

		group_pick_vector = group_pick_vector_node_group()

		#initialize offset_integer node group
		def offset_integer_node_group():
			offset_integer = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Offset Integer")

			offset_integer.color_tag = 'CONVERTER'
			offset_integer.description = ""

			
			#offset_integer interface
			#Socket Value
			value_socket_9 = offset_integer.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			value_socket_9.subtype = 'NONE'
			value_socket_9.default_value = 0
			value_socket_9.min_value = -2147483648
			value_socket_9.max_value = 2147483647
			value_socket_9.attribute_domain = 'POINT'
			
			#Socket Index
			index_socket_3 = offset_integer.interface.new_socket(name = "Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			index_socket_3.subtype = 'NONE'
			index_socket_3.default_value = 0
			index_socket_3.min_value = 0
			index_socket_3.max_value = 2147483647
			index_socket_3.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_10 = offset_integer.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketInt')
			value_socket_10.subtype = 'NONE'
			value_socket_10.default_value = 0
			value_socket_10.min_value = -2147483648
			value_socket_10.max_value = 2147483647
			value_socket_10.attribute_domain = 'POINT'
			value_socket_10.hide_value = True
			
			#Socket Offset
			offset_socket_6 = offset_integer.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket_6.subtype = 'NONE'
			offset_socket_6.default_value = 0
			offset_socket_6.min_value = -2147483648
			offset_socket_6.max_value = 2147483647
			offset_socket_6.attribute_domain = 'POINT'
			
			
			#initialize offset_integer nodes
			#node Group Output
			group_output_49 = offset_integer.nodes.new("NodeGroupOutput")
			group_output_49.name = "Group Output"
			group_output_49.is_active_output = True
			
			#node Group Input
			group_input_48 = offset_integer.nodes.new("NodeGroupInput")
			group_input_48.name = "Group Input"
			
			#node Evaluate at Index
			evaluate_at_index_2 = offset_integer.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_2.name = "Evaluate at Index"
			evaluate_at_index_2.data_type = 'INT'
			evaluate_at_index_2.domain = 'POINT'
			
			#node Math
			math_10 = offset_integer.nodes.new("ShaderNodeMath")
			math_10.name = "Math"
			math_10.operation = 'ADD'
			math_10.use_clamp = False
			
			
			
			
			#Set locations
			group_output_49.location = (190.0, 0.0)
			group_input_48.location = (-412.72760009765625, 0.2001800537109375)
			evaluate_at_index_2.location = (0.0, 0.0)
			math_10.location = (-217.90158081054688, 69.93922424316406)
			
			#Set dimensions
			group_output_49.width, group_output_49.height = 140.0, 100.0
			group_input_48.width, group_input_48.height = 140.0, 100.0
			evaluate_at_index_2.width, evaluate_at_index_2.height = 140.0, 100.0
			math_10.width, math_10.height = 140.0, 100.0
			
			#initialize offset_integer links
			#evaluate_at_index_2.Value -> group_output_49.Value
			offset_integer.links.new(evaluate_at_index_2.outputs[0], group_output_49.inputs[0])
			#group_input_48.Index -> math_10.Value
			offset_integer.links.new(group_input_48.outputs[0], math_10.inputs[0])
			#group_input_48.Offset -> math_10.Value
			offset_integer.links.new(group_input_48.outputs[2], math_10.inputs[1])
			#math_10.Value -> evaluate_at_index_2.Index
			offset_integer.links.new(math_10.outputs[0], evaluate_at_index_2.inputs[0])
			#group_input_48.Value -> evaluate_at_index_2.Value
			offset_integer.links.new(group_input_48.outputs[1], evaluate_at_index_2.inputs[1])
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
			group_output_50 = res_group_id.nodes.new("NodeGroupOutput")
			group_output_50.name = "Group Output"
			group_output_50.is_active_output = True
			
			#node Group Input
			group_input_49 = res_group_id.nodes.new("NodeGroupInput")
			group_input_49.name = "Group Input"
			
			#node Named Attribute.001
			named_attribute_001_6 = res_group_id.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001_6.name = "Named Attribute.001"
			named_attribute_001_6.data_type = 'INT'
			#Name
			named_attribute_001_6.inputs[0].default_value = "res_id"
			
			#node Named Attribute.002
			named_attribute_002_3 = res_group_id.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002_3.name = "Named Attribute.002"
			named_attribute_002_3.data_type = 'INT'
			#Name
			named_attribute_002_3.inputs[0].default_value = "atom_name"
			
			#node Compare.002
			compare_002_2 = res_group_id.nodes.new("FunctionNodeCompare")
			compare_002_2.name = "Compare.002"
			compare_002_2.data_type = 'INT'
			compare_002_2.mode = 'ELEMENT'
			compare_002_2.operation = 'EQUAL'
			#B_INT
			compare_002_2.inputs[3].default_value = 1
			
			#node Compare.001
			compare_001_4 = res_group_id.nodes.new("FunctionNodeCompare")
			compare_001_4.name = "Compare.001"
			compare_001_4.data_type = 'INT'
			compare_001_4.mode = 'ELEMENT'
			compare_001_4.operation = 'NOT_EQUAL'
			
			#node Boolean Math
			boolean_math_10 = res_group_id.nodes.new("FunctionNodeBooleanMath")
			boolean_math_10.name = "Boolean Math"
			boolean_math_10.operation = 'OR'
			
			#node Accumulate Field.001
			accumulate_field_001_2 = res_group_id.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_001_2.name = "Accumulate Field.001"
			accumulate_field_001_2.data_type = 'INT'
			accumulate_field_001_2.domain = 'POINT'
			#Group Index
			accumulate_field_001_2.inputs[1].default_value = 0
			
			#node Group.001
			group_001_8 = res_group_id.nodes.new("GeometryNodeGroup")
			group_001_8.name = "Group.001"
			group_001_8.node_tree = offset_integer
			#Socket_1
			group_001_8.inputs[0].default_value = 0
			#Socket_2
			group_001_8.inputs[2].default_value = -1
			
			#node Math
			math_11 = res_group_id.nodes.new("ShaderNodeMath")
			math_11.name = "Math"
			math_11.operation = 'SUBTRACT'
			math_11.use_clamp = False
			#Value_001
			math_11.inputs[1].default_value = 1.0
			
			#node Frame
			frame_3 = res_group_id.nodes.new("NodeFrame")
			frame_3.name = "Frame"
			frame_3.label_size = 20
			frame_3.shrink = True
			
			#node Reroute
			reroute_13 = res_group_id.nodes.new("NodeReroute")
			reroute_13.label = "subtracting 1 from the leading, but things don't work right"
			reroute_13.name = "Reroute"
			#node Reroute.001
			reroute_001_9 = res_group_id.nodes.new("NodeReroute")
			reroute_001_9.name = "Reroute.001"
			#node Reroute.002
			reroute_002_5 = res_group_id.nodes.new("NodeReroute")
			reroute_002_5.label = "In theory we can just use the trailing value instead of"
			reroute_002_5.name = "Reroute.002"
			#node Reroute.003
			reroute_003_2 = res_group_id.nodes.new("NodeReroute")
			reroute_003_2.name = "Reroute.003"
			
			
			#Set parents
			math_11.parent = frame_3
			reroute_13.parent = frame_3
			reroute_001_9.parent = frame_3
			reroute_002_5.parent = frame_3
			reroute_003_2.parent = frame_3
			
			#Set locations
			group_output_50.location = (900.0, 160.0)
			group_input_49.location = (-420.0, 160.0)
			named_attribute_001_6.location = (-240.0, 0.0)
			named_attribute_002_3.location = (-250.0, 160.0)
			compare_002_2.location = (-70.0, 160.0)
			compare_001_4.location = (-70.0, 0.0)
			boolean_math_10.location = (90.0, 160.0)
			accumulate_field_001_2.location = (250.0, 160.0)
			group_001_8.location = (-70.0, -160.0)
			math_11.location = (519.2361450195312, 166.28671264648438)
			frame_3.location = (95.0, -20.0)
			reroute_13.location = (554.4125366210938, 257.9646911621094)
			reroute_001_9.location = (739.2361450195312, 306.2867126464844)
			reroute_002_5.location = (551.13134765625, 297.3444519042969)
			reroute_003_2.location = (379.23614501953125, 306.2867126464844)
			
			#Set dimensions
			group_output_50.width, group_output_50.height = 140.0, 100.0
			group_input_49.width, group_input_49.height = 140.0, 100.0
			named_attribute_001_6.width, named_attribute_001_6.height = 140.0, 100.0
			named_attribute_002_3.width, named_attribute_002_3.height = 140.0, 100.0
			compare_002_2.width, compare_002_2.height = 140.0, 100.0
			compare_001_4.width, compare_001_4.height = 140.0, 100.0
			boolean_math_10.width, boolean_math_10.height = 140.0, 100.0
			accumulate_field_001_2.width, accumulate_field_001_2.height = 140.0, 100.0
			group_001_8.width, group_001_8.height = 140.0, 100.0
			math_11.width, math_11.height = 140.0, 100.0
			frame_3.width, frame_3.height = 436.0, 356.2867126464844
			reroute_13.width, reroute_13.height = 16.0, 100.0
			reroute_001_9.width, reroute_001_9.height = 16.0, 100.0
			reroute_002_5.width, reroute_002_5.height = 16.0, 100.0
			reroute_003_2.width, reroute_003_2.height = 16.0, 100.0
			
			#initialize res_group_id links
			#compare_002_2.Result -> boolean_math_10.Boolean
			res_group_id.links.new(compare_002_2.outputs[0], boolean_math_10.inputs[0])
			#named_attribute_001_6.Attribute -> compare_001_4.A
			res_group_id.links.new(named_attribute_001_6.outputs[0], compare_001_4.inputs[2])
			#named_attribute_001_6.Attribute -> group_001_8.Value
			res_group_id.links.new(named_attribute_001_6.outputs[0], group_001_8.inputs[1])
			#compare_001_4.Result -> boolean_math_10.Boolean
			res_group_id.links.new(compare_001_4.outputs[0], boolean_math_10.inputs[1])
			#named_attribute_002_3.Attribute -> compare_002_2.A
			res_group_id.links.new(named_attribute_002_3.outputs[0], compare_002_2.inputs[2])
			#group_001_8.Value -> compare_001_4.B
			res_group_id.links.new(group_001_8.outputs[0], compare_001_4.inputs[3])
			#accumulate_field_001_2.Leading -> math_11.Value
			res_group_id.links.new(accumulate_field_001_2.outputs[0], math_11.inputs[0])
			#math_11.Value -> group_output_50.Unique Group ID
			res_group_id.links.new(math_11.outputs[0], group_output_50.inputs[0])
			#boolean_math_10.Boolean -> accumulate_field_001_2.Value
			res_group_id.links.new(boolean_math_10.outputs[0], accumulate_field_001_2.inputs[0])
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
			index_socket_4 = residue_mask.interface.new_socket(name = "Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			index_socket_4.subtype = 'NONE'
			index_socket_4.default_value = 0
			index_socket_4.min_value = -2147483648
			index_socket_4.max_value = 2147483647
			index_socket_4.attribute_domain = 'POINT'
			index_socket_4.description = "Index for the group's atom with specified name, returns -1 if not valid"
			
			#Socket Position
			position_socket_2 = residue_mask.interface.new_socket(name = "Position", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			position_socket_2.subtype = 'NONE'
			position_socket_2.default_value = (0.0, 0.0, 0.0)
			position_socket_2.min_value = -3.4028234663852886e+38
			position_socket_2.max_value = 3.4028234663852886e+38
			position_socket_2.attribute_domain = 'POINT'
			position_socket_2.description = "Position of the picked point in the group, returns (0, 0, 0) if not valid"
			
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
			compare_9 = residue_mask.nodes.new("FunctionNodeCompare")
			compare_9.name = "Compare"
			compare_9.data_type = 'INT'
			compare_9.mode = 'ELEMENT'
			compare_9.operation = 'EQUAL'
			
			#node Group Input
			group_input_50 = residue_mask.nodes.new("NodeGroupInput")
			group_input_50.name = "Group Input"
			
			#node Named Attribute
			named_attribute_10 = residue_mask.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_10.name = "Named Attribute"
			named_attribute_10.data_type = 'INT'
			#Name
			named_attribute_10.inputs[0].default_value = "atom_name"
			
			#node Group Output
			group_output_51 = residue_mask.nodes.new("NodeGroupOutput")
			group_output_51.name = "Group Output"
			group_output_51.is_active_output = True
			
			#node Group
			group_18 = residue_mask.nodes.new("GeometryNodeGroup")
			group_18.name = "Group"
			group_18.node_tree = group_pick_vector
			#Socket_5
			group_18.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Group.002
			group_002_3 = residue_mask.nodes.new("GeometryNodeGroup")
			group_002_3.name = "Group.002"
			group_002_3.node_tree = res_group_id
			
			#node Switch
			switch_12 = residue_mask.nodes.new("GeometryNodeSwitch")
			switch_12.name = "Switch"
			switch_12.input_type = 'INT'
			
			
			
			
			#Set locations
			compare_9.location = (40.0, 340.0)
			group_input_50.location = (-140.0, 200.0)
			named_attribute_10.location = (-140.0, 340.0)
			group_output_51.location = (420.0, 340.0)
			group_18.location = (220.0, 340.0)
			group_002_3.location = (-140.0, 60.0)
			switch_12.location = (40.0, 180.0)
			
			#Set dimensions
			compare_9.width, compare_9.height = 140.0, 100.0
			group_input_50.width, group_input_50.height = 140.0, 100.0
			named_attribute_10.width, named_attribute_10.height = 140.0, 100.0
			group_output_51.width, group_output_51.height = 140.0, 100.0
			group_18.width, group_18.height = 164.60528564453125, 100.0
			group_002_3.width, group_002_3.height = 140.0, 100.0
			switch_12.width, switch_12.height = 140.0, 100.0
			
			#initialize residue_mask links
			#named_attribute_10.Attribute -> compare_9.A
			residue_mask.links.new(named_attribute_10.outputs[0], compare_9.inputs[2])
			#group_input_50.atom_name -> compare_9.B
			residue_mask.links.new(group_input_50.outputs[0], compare_9.inputs[3])
			#group_18.Index -> group_output_51.Index
			residue_mask.links.new(group_18.outputs[1], group_output_51.inputs[1])
			#group_18.Vector -> group_output_51.Position
			residue_mask.links.new(group_18.outputs[2], group_output_51.inputs[2])
			#group_18.Is Valid -> group_output_51.Is Valid
			residue_mask.links.new(group_18.outputs[0], group_output_51.inputs[0])
			#compare_9.Result -> group_18.Pick
			residue_mask.links.new(compare_9.outputs[0], group_18.inputs[0])
			#group_input_50.Use Fallback -> switch_12.Switch
			residue_mask.links.new(group_input_50.outputs[1], switch_12.inputs[0])
			#group_input_50.Group ID -> switch_12.False
			residue_mask.links.new(group_input_50.outputs[2], switch_12.inputs[1])
			#switch_12.Output -> group_18.Group ID
			residue_mask.links.new(switch_12.outputs[0], group_18.inputs[1])
			#group_002_3.Unique Group ID -> switch_12.True
			residue_mask.links.new(group_002_3.outputs[0], switch_12.inputs[2])
			#switch_12.Output -> group_output_51.Group ID
			residue_mask.links.new(switch_12.outputs[0], group_output_51.inputs[3])
			return residue_mask

		residue_mask = residue_mask_node_group()

		#initialize _mn_topo_assign_backbone node group
		def _mn_topo_assign_backbone_node_group():
			_mn_topo_assign_backbone = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_topo_assign_backbone")

			_mn_topo_assign_backbone.color_tag = 'NONE'
			_mn_topo_assign_backbone.description = ""

			
			#_mn_topo_assign_backbone interface
			#Socket Atoms
			atoms_socket_9 = _mn_topo_assign_backbone.interface.new_socket(name = "Atoms", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_9.attribute_domain = 'POINT'
			
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
			atoms_socket_10 = _mn_topo_assign_backbone.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_10.attribute_domain = 'POINT'
			
			
			#initialize _mn_topo_assign_backbone nodes
			#node Group Output
			group_output_52 = _mn_topo_assign_backbone.nodes.new("NodeGroupOutput")
			group_output_52.name = "Group Output"
			group_output_52.is_active_output = True
			
			#node Group Input
			group_input_51 = _mn_topo_assign_backbone.nodes.new("NodeGroupInput")
			group_input_51.name = "Group Input"
			
			#node Store Named Attribute.002
			store_named_attribute_002_1 = _mn_topo_assign_backbone.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_002_1.name = "Store Named Attribute.002"
			store_named_attribute_002_1.data_type = 'FLOAT_VECTOR'
			store_named_attribute_002_1.domain = 'POINT'
			#Name
			store_named_attribute_002_1.inputs[2].default_value = "backbone_N"
			
			#node Store Named Attribute.003
			store_named_attribute_003_1 = _mn_topo_assign_backbone.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_003_1.name = "Store Named Attribute.003"
			store_named_attribute_003_1.data_type = 'FLOAT_VECTOR'
			store_named_attribute_003_1.domain = 'POINT'
			#Name
			store_named_attribute_003_1.inputs[2].default_value = "backbone_C"
			
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
			capture_attribute_2 = _mn_topo_assign_backbone.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute_2.name = "Capture Attribute"
			capture_attribute_2.active_index = 0
			capture_attribute_2.capture_items.clear()
			capture_attribute_2.capture_items.new('FLOAT', "Unique Group ID")
			capture_attribute_2.capture_items["Unique Group ID"].data_type = 'INT'
			capture_attribute_2.domain = 'POINT'
			
			#node Group
			group_19 = _mn_topo_assign_backbone.nodes.new("GeometryNodeGroup")
			group_19.name = "Group"
			group_19.node_tree = res_group_id
			
			#node Reroute
			reroute_14 = _mn_topo_assign_backbone.nodes.new("NodeReroute")
			reroute_14.name = "Reroute"
			#node Reroute.001
			reroute_001_10 = _mn_topo_assign_backbone.nodes.new("NodeReroute")
			reroute_001_10.name = "Reroute.001"
			#node Reroute.002
			reroute_002_6 = _mn_topo_assign_backbone.nodes.new("NodeReroute")
			reroute_002_6.name = "Reroute.002"
			#node Reroute.003
			reroute_003_3 = _mn_topo_assign_backbone.nodes.new("NodeReroute")
			reroute_003_3.name = "Reroute.003"
			#node Separate Geometry
			separate_geometry_7 = _mn_topo_assign_backbone.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_7.name = "Separate Geometry"
			separate_geometry_7.domain = 'POINT'
			
			#node Group.001
			group_001_9 = _mn_topo_assign_backbone.nodes.new("GeometryNodeGroup")
			group_001_9.name = "Group.001"
			group_001_9.node_tree = is_alpha_carbon
			#Socket_1
			group_001_9.inputs[0].default_value = True
			#Socket_3
			group_001_9.inputs[1].default_value = False
			
			
			
			
			#Set locations
			group_output_52.location = (720.0, 100.0)
			group_input_51.location = (-1200.0, 100.0)
			store_named_attribute_002_1.location = (-400.0, 100.0)
			store_named_attribute_003_1.location = (60.0, 100.0)
			store_named_attribute_004_2.location = (-180.0, 100.0)
			store_named_attribute_005_2.location = (300.0, 100.0)
			mn_topo_point_mask_005.location = (60.0, -120.0)
			mn_topo_point_mask_006.location = (-180.0, -120.0)
			mn_topo_point_mask_007.location = (300.0, -120.0)
			mn_topo_point_mask_004.location = (-400.0, -120.0)
			capture_attribute_2.location = (-1020.0, 100.0)
			group_19.location = (-1200.0, 0.0)
			reroute_14.location = (-440.0, -340.0)
			reroute_001_10.location = (-200.0, -340.0)
			reroute_002_6.location = (40.0, -340.0)
			reroute_003_3.location = (280.0, -340.0)
			separate_geometry_7.location = (540.0, 20.0)
			group_001_9.location = (540.0, -160.0)
			
			#Set dimensions
			group_output_52.width, group_output_52.height = 140.0, 100.0
			group_input_51.width, group_input_51.height = 140.0, 100.0
			store_named_attribute_002_1.width, store_named_attribute_002_1.height = 172.44415283203125, 100.0
			store_named_attribute_003_1.width, store_named_attribute_003_1.height = 169.44052124023438, 100.0
			store_named_attribute_004_2.width, store_named_attribute_004_2.height = 184.14559936523438, 100.0
			store_named_attribute_005_2.width, store_named_attribute_005_2.height = 169.42654418945312, 100.0
			mn_topo_point_mask_005.width, mn_topo_point_mask_005.height = 172.76019287109375, 100.0
			mn_topo_point_mask_006.width, mn_topo_point_mask_006.height = 185.9674072265625, 100.0
			mn_topo_point_mask_007.width, mn_topo_point_mask_007.height = 168.1260986328125, 100.0
			mn_topo_point_mask_004.width, mn_topo_point_mask_004.height = 178.538330078125, 100.0
			capture_attribute_2.width, capture_attribute_2.height = 140.0, 100.0
			group_19.width, group_19.height = 140.0, 100.0
			reroute_14.width, reroute_14.height = 16.0, 100.0
			reroute_001_10.width, reroute_001_10.height = 16.0, 100.0
			reroute_002_6.width, reroute_002_6.height = 16.0, 100.0
			reroute_003_3.width, reroute_003_3.height = 16.0, 100.0
			separate_geometry_7.width, separate_geometry_7.height = 140.0, 100.0
			group_001_9.width, group_001_9.height = 140.0, 100.0
			
			#initialize _mn_topo_assign_backbone links
			#mn_topo_point_mask_007.Is Valid -> store_named_attribute_005_2.Selection
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_007.outputs[0], store_named_attribute_005_2.inputs[1])
			#mn_topo_point_mask_006.Position -> store_named_attribute_004_2.Value
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_006.outputs[2], store_named_attribute_004_2.inputs[3])
			#mn_topo_point_mask_005.Position -> store_named_attribute_003_1.Value
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_005.outputs[2], store_named_attribute_003_1.inputs[3])
			#store_named_attribute_004_2.Geometry -> store_named_attribute_003_1.Geometry
			_mn_topo_assign_backbone.links.new(store_named_attribute_004_2.outputs[0], store_named_attribute_003_1.inputs[0])
			#store_named_attribute_003_1.Geometry -> store_named_attribute_005_2.Geometry
			_mn_topo_assign_backbone.links.new(store_named_attribute_003_1.outputs[0], store_named_attribute_005_2.inputs[0])
			#store_named_attribute_002_1.Geometry -> store_named_attribute_004_2.Geometry
			_mn_topo_assign_backbone.links.new(store_named_attribute_002_1.outputs[0], store_named_attribute_004_2.inputs[0])
			#mn_topo_point_mask_007.Position -> store_named_attribute_005_2.Value
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_007.outputs[2], store_named_attribute_005_2.inputs[3])
			#mn_topo_point_mask_006.Is Valid -> store_named_attribute_004_2.Selection
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_006.outputs[0], store_named_attribute_004_2.inputs[1])
			#mn_topo_point_mask_005.Is Valid -> store_named_attribute_003_1.Selection
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_005.outputs[0], store_named_attribute_003_1.inputs[1])
			#capture_attribute_2.Geometry -> store_named_attribute_002_1.Geometry
			_mn_topo_assign_backbone.links.new(capture_attribute_2.outputs[0], store_named_attribute_002_1.inputs[0])
			#store_named_attribute_005_2.Geometry -> group_output_52.Atoms
			_mn_topo_assign_backbone.links.new(store_named_attribute_005_2.outputs[0], group_output_52.inputs[0])
			#group_input_51.Atoms -> capture_attribute_2.Geometry
			_mn_topo_assign_backbone.links.new(group_input_51.outputs[0], capture_attribute_2.inputs[0])
			#group_19.Unique Group ID -> capture_attribute_2.Unique Group ID
			_mn_topo_assign_backbone.links.new(group_19.outputs[0], capture_attribute_2.inputs[1])
			#reroute_001_10.Output -> mn_topo_point_mask_006.Group ID
			_mn_topo_assign_backbone.links.new(reroute_001_10.outputs[0], mn_topo_point_mask_006.inputs[2])
			#capture_attribute_2.Unique Group ID -> reroute_14.Input
			_mn_topo_assign_backbone.links.new(capture_attribute_2.outputs[1], reroute_14.inputs[0])
			#reroute_14.Output -> reroute_001_10.Input
			_mn_topo_assign_backbone.links.new(reroute_14.outputs[0], reroute_001_10.inputs[0])
			#reroute_002_6.Output -> mn_topo_point_mask_005.Group ID
			_mn_topo_assign_backbone.links.new(reroute_002_6.outputs[0], mn_topo_point_mask_005.inputs[2])
			#reroute_001_10.Output -> reroute_002_6.Input
			_mn_topo_assign_backbone.links.new(reroute_001_10.outputs[0], reroute_002_6.inputs[0])
			#reroute_003_3.Output -> mn_topo_point_mask_007.Group ID
			_mn_topo_assign_backbone.links.new(reroute_003_3.outputs[0], mn_topo_point_mask_007.inputs[2])
			#reroute_002_6.Output -> reroute_003_3.Input
			_mn_topo_assign_backbone.links.new(reroute_002_6.outputs[0], reroute_003_3.inputs[0])
			#capture_attribute_2.Unique Group ID -> group_output_52.Unique Group ID
			_mn_topo_assign_backbone.links.new(capture_attribute_2.outputs[1], group_output_52.inputs[1])
			#mn_topo_point_mask_004.Is Valid -> store_named_attribute_002_1.Selection
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_004.outputs[0], store_named_attribute_002_1.inputs[1])
			#mn_topo_point_mask_004.Position -> store_named_attribute_002_1.Value
			_mn_topo_assign_backbone.links.new(mn_topo_point_mask_004.outputs[2], store_named_attribute_002_1.inputs[3])
			#store_named_attribute_005_2.Geometry -> separate_geometry_7.Geometry
			_mn_topo_assign_backbone.links.new(store_named_attribute_005_2.outputs[0], separate_geometry_7.inputs[0])
			#separate_geometry_7.Selection -> group_output_52.CA Atoms
			_mn_topo_assign_backbone.links.new(separate_geometry_7.outputs[0], group_output_52.inputs[2])
			#group_001_9.Selection -> separate_geometry_7.Selection
			_mn_topo_assign_backbone.links.new(group_001_9.outputs[0], separate_geometry_7.inputs[1])
			#reroute_14.Output -> mn_topo_point_mask_004.Group ID
			_mn_topo_assign_backbone.links.new(reroute_14.outputs[0], mn_topo_point_mask_004.inputs[2])
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
			value_socket_11 = _is_odd.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketInt')
			value_socket_11.subtype = 'NONE'
			value_socket_11.default_value = 0
			value_socket_11.min_value = -2147483648
			value_socket_11.max_value = 2147483647
			value_socket_11.attribute_domain = 'POINT'
			
			
			#initialize _is_odd nodes
			#node Group Input
			group_input_52 = _is_odd.nodes.new("NodeGroupInput")
			group_input_52.name = "Group Input"
			
			#node Group Output
			group_output_53 = _is_odd.nodes.new("NodeGroupOutput")
			group_output_53.name = "Group Output"
			group_output_53.is_active_output = True
			
			#node Boolean Math
			boolean_math_11 = _is_odd.nodes.new("FunctionNodeBooleanMath")
			boolean_math_11.name = "Boolean Math"
			boolean_math_11.operation = 'NOT'
			
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
			math_008_1 = _is_odd.nodes.new("ShaderNodeMath")
			math_008_1.name = "Math.008"
			math_008_1.operation = 'FLOORED_MODULO'
			math_008_1.use_clamp = False
			#Value_001
			math_008_1.inputs[1].default_value = 2.0
			
			
			
			
			#Set locations
			group_input_52.location = (-300.0, 80.0)
			group_output_53.location = (240.0, 120.0)
			boolean_math_11.location = (240.0, 20.0)
			compare_011.location = (60.0, 120.0)
			math_008_1.location = (-100.0, 120.0)
			
			#Set dimensions
			group_input_52.width, group_input_52.height = 140.0, 100.0
			group_output_53.width, group_output_53.height = 140.0, 100.0
			boolean_math_11.width, boolean_math_11.height = 140.0, 100.0
			compare_011.width, compare_011.height = 140.0, 100.0
			math_008_1.width, math_008_1.height = 140.0, 100.0
			
			#initialize _is_odd links
			#group_input_52.Value -> math_008_1.Value
			_is_odd.links.new(group_input_52.outputs[0], math_008_1.inputs[0])
			#compare_011.Result -> group_output_53.is_even
			_is_odd.links.new(compare_011.outputs[0], group_output_53.inputs[0])
			#compare_011.Result -> boolean_math_11.Boolean
			_is_odd.links.new(compare_011.outputs[0], boolean_math_11.inputs[0])
			#boolean_math_11.Boolean -> group_output_53.is_odd
			_is_odd.links.new(boolean_math_11.outputs[0], group_output_53.inputs[1])
			#math_008_1.Value -> compare_011.A
			_is_odd.links.new(math_008_1.outputs[0], compare_011.inputs[0])
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
			frame_4 = _mn_cartoon_bs_alternate_axis.nodes.new("NodeFrame")
			frame_4.label = "Only the last AA in an AH is selected"
			frame_4.name = "Frame"
			frame_4.label_size = 20
			frame_4.shrink = True
			
			#node Vector Math.005
			vector_math_005_2 = _mn_cartoon_bs_alternate_axis.nodes.new("ShaderNodeVectorMath")
			vector_math_005_2.name = "Vector Math.005"
			vector_math_005_2.operation = 'SCALE'
			
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
			group_output_54 = _mn_cartoon_bs_alternate_axis.nodes.new("NodeGroupOutput")
			group_output_54.name = "Group Output"
			group_output_54.is_active_output = True
			
			#node Index.001
			index_001_1 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeInputIndex")
			index_001_1.name = "Index.001"
			
			#node Boolean Math.010
			boolean_math_010 = _mn_cartoon_bs_alternate_axis.nodes.new("FunctionNodeBooleanMath")
			boolean_math_010.name = "Boolean Math.010"
			boolean_math_010.operation = 'AND'
			
			#node Reroute.001
			reroute_001_11 = _mn_cartoon_bs_alternate_axis.nodes.new("NodeReroute")
			reroute_001_11.name = "Reroute.001"
			#node Vector Math.004
			vector_math_004_1 = _mn_cartoon_bs_alternate_axis.nodes.new("ShaderNodeVectorMath")
			vector_math_004_1.label = "N -> C"
			vector_math_004_1.name = "Vector Math.004"
			vector_math_004_1.operation = 'SUBTRACT'
			
			#node Group Input
			group_input_53 = _mn_cartoon_bs_alternate_axis.nodes.new("NodeGroupInput")
			group_input_53.name = "Group Input"
			
			#node Vector Math
			vector_math_4 = _mn_cartoon_bs_alternate_axis.nodes.new("ShaderNodeVectorMath")
			vector_math_4.label = "C --> O"
			vector_math_4.name = "Vector Math"
			vector_math_4.operation = 'SUBTRACT'
			
			#node Integer
			integer_4 = _mn_cartoon_bs_alternate_axis.nodes.new("FunctionNodeInputInt")
			integer_4.name = "Integer"
			integer_4.integer = -1
			
			#node Compare
			compare_10 = _mn_cartoon_bs_alternate_axis.nodes.new("FunctionNodeCompare")
			compare_10.name = "Compare"
			compare_10.data_type = 'INT'
			compare_10.mode = 'ELEMENT'
			compare_10.operation = 'GREATER_THAN'
			
			#node Group.014
			group_014_1 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeGroup")
			group_014_1.name = "Group.014"
			group_014_1.node_tree = _sec_struct_counter
			
			#node Boolean Math
			boolean_math_12 = _mn_cartoon_bs_alternate_axis.nodes.new("FunctionNodeBooleanMath")
			boolean_math_12.name = "Boolean Math"
			boolean_math_12.operation = 'AND'
			
			#node Switch
			switch_13 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeSwitch")
			switch_13.name = "Switch"
			switch_13.input_type = 'VECTOR'
			
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
			switch_008 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeSwitch")
			switch_008.name = "Switch.008"
			switch_008.input_type = 'INT'
			#False
			switch_008.inputs[1].default_value = 1
			#True
			switch_008.inputs[2].default_value = -1
			
			#node Group
			group_20 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeGroup")
			group_20.name = "Group"
			group_20.node_tree = _field_offset
			group_20.inputs[1].hide = True
			group_20.inputs[2].hide = True
			group_20.inputs[3].hide = True
			group_20.outputs[1].hide = True
			group_20.outputs[2].hide = True
			group_20.outputs[3].hide = True
			#Input_3
			group_20.inputs[1].default_value = False
			#Input_5
			group_20.inputs[2].default_value = 0
			#Input_7
			group_20.inputs[3].default_value = 0.0
			
			#node Group.011
			group_011_1 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeGroup")
			group_011_1.name = "Group.011"
			group_011_1.node_tree = _mn_select_sec_struct
			#Socket_1
			group_011_1.inputs[0].default_value = True
			
			#node Group.005
			group_005_1 = _mn_cartoon_bs_alternate_axis.nodes.new("GeometryNodeGroup")
			group_005_1.name = "Group.005"
			group_005_1.node_tree = _is_odd
			
			
			
			#Set parents
			compare_10.parent = frame_4
			group_014_1.parent = frame_4
			boolean_math_12.parent = frame_4
			group_012.parent = frame_4
			
			#Set locations
			frame_4.location = (-86.11199951171875, 65.14605712890625)
			vector_math_005_2.location = (60.0, 440.0)
			blur_attribute_001.location = (220.0, 400.0)
			switch_002_1.location = (220.0, 580.0)
			group_output_54.location = (400.0, 580.0)
			index_001_1.location = (-381.36767578125, 1.1884498596191406)
			boolean_math_010.location = (-41.36767578125, 101.18844604492188)
			reroute_001_11.location = (-897.6007080078125, 360.3312683105469)
			vector_math_004_1.location = (-817.6007080078125, 540.3312377929688)
			group_input_53.location = (-1077.6007080078125, 420.3312683105469)
			vector_math_4.location = (-817.6007080078125, 400.3312683105469)
			integer_4.location = (-822.031982421875, 264.41668701171875)
			compare_10.location = (-526.031982421875, 831.0416870117188)
			group_014_1.location = (-854.4696655273438, 787.1783447265625)
			boolean_math_12.location = (-366.0320129394531, 831.0416870117188)
			switch_13.location = (-189.45494079589844, 480.51531982421875)
			group_012.location = (-666.031982421875, 651.0416870117188)
			switch_008.location = (120.0, 100.0)
			group_20.location = (-622.031982421875, 344.41668701171875)
			group_011_1.location = (-361.36767578125, 161.18844604492188)
			group_005_1.location = (-221.36767578125, 1.1884498596191406)
			
			#Set dimensions
			frame_4.width, frame_4.height = 688.7999877929688, 326.0
			vector_math_005_2.width, vector_math_005_2.height = 140.0, 100.0
			blur_attribute_001.width, blur_attribute_001.height = 140.0, 100.0
			switch_002_1.width, switch_002_1.height = 140.0, 100.0
			group_output_54.width, group_output_54.height = 140.0, 100.0
			index_001_1.width, index_001_1.height = 140.0, 100.0
			boolean_math_010.width, boolean_math_010.height = 140.0, 100.0
			reroute_001_11.width, reroute_001_11.height = 16.0, 100.0
			vector_math_004_1.width, vector_math_004_1.height = 140.0, 100.0
			group_input_53.width, group_input_53.height = 140.0, 100.0
			vector_math_4.width, vector_math_4.height = 140.0, 100.0
			integer_4.width, integer_4.height = 140.0, 100.0
			compare_10.width, compare_10.height = 140.0, 100.0
			group_014_1.width, group_014_1.height = 140.0, 100.0
			boolean_math_12.width, boolean_math_12.height = 140.0, 100.0
			switch_13.width, switch_13.height = 140.0, 100.0
			group_012.width, group_012.height = 277.2730712890625, 100.0
			switch_008.width, switch_008.height = 140.0, 100.0
			group_20.width, group_20.height = 196.1611328125, 100.0
			group_011_1.width, group_011_1.height = 277.2730712890625, 100.0
			group_005_1.width, group_005_1.height = 140.0, 100.0
			
			#initialize _mn_cartoon_bs_alternate_axis links
			#vector_math_005_2.Vector -> switch_002_1.False
			_mn_cartoon_bs_alternate_axis.links.new(vector_math_005_2.outputs[0], switch_002_1.inputs[1])
			#blur_attribute_001.Value -> switch_002_1.True
			_mn_cartoon_bs_alternate_axis.links.new(blur_attribute_001.outputs[0], switch_002_1.inputs[2])
			#group_011_1.Is Sheet -> switch_002_1.Switch
			_mn_cartoon_bs_alternate_axis.links.new(group_011_1.outputs[1], switch_002_1.inputs[0])
			#group_input_53.C -> reroute_001_11.Input
			_mn_cartoon_bs_alternate_axis.links.new(group_input_53.outputs[1], reroute_001_11.inputs[0])
			#boolean_math_010.Boolean -> switch_008.Switch
			_mn_cartoon_bs_alternate_axis.links.new(boolean_math_010.outputs[0], switch_008.inputs[0])
			#group_005_1.is_even -> boolean_math_010.Boolean
			_mn_cartoon_bs_alternate_axis.links.new(group_005_1.outputs[0], boolean_math_010.inputs[1])
			#index_001_1.Index -> group_005_1.Value
			_mn_cartoon_bs_alternate_axis.links.new(index_001_1.outputs[0], group_005_1.inputs[0])
			#reroute_001_11.Output -> vector_math_4.Vector
			_mn_cartoon_bs_alternate_axis.links.new(reroute_001_11.outputs[0], vector_math_4.inputs[0])
			#group_011_1.Is Sheet -> boolean_math_010.Boolean
			_mn_cartoon_bs_alternate_axis.links.new(group_011_1.outputs[1], boolean_math_010.inputs[0])
			#reroute_001_11.Output -> vector_math_004_1.Vector
			_mn_cartoon_bs_alternate_axis.links.new(reroute_001_11.outputs[0], vector_math_004_1.inputs[1])
			#vector_math_005_2.Vector -> blur_attribute_001.Value
			_mn_cartoon_bs_alternate_axis.links.new(vector_math_005_2.outputs[0], blur_attribute_001.inputs[0])
			#switch_008.Output -> vector_math_005_2.Scale
			_mn_cartoon_bs_alternate_axis.links.new(switch_008.outputs[0], vector_math_005_2.inputs[3])
			#group_input_53.O -> vector_math_4.Vector
			_mn_cartoon_bs_alternate_axis.links.new(group_input_53.outputs[2], vector_math_4.inputs[1])
			#switch_002_1.Output -> group_output_54.Z Vector for Euler
			_mn_cartoon_bs_alternate_axis.links.new(switch_002_1.outputs[0], group_output_54.inputs[0])
			#vector_math_004_1.Vector -> group_output_54.X Vector for Euler
			_mn_cartoon_bs_alternate_axis.links.new(vector_math_004_1.outputs[0], group_output_54.inputs[1])
			#group_input_53.N -> vector_math_004_1.Vector
			_mn_cartoon_bs_alternate_axis.links.new(group_input_53.outputs[0], vector_math_004_1.inputs[0])
			#switch_13.Output -> vector_math_005_2.Vector
			_mn_cartoon_bs_alternate_axis.links.new(switch_13.outputs[0], vector_math_005_2.inputs[0])
			#group_014_1.Leading -> compare_10.A
			_mn_cartoon_bs_alternate_axis.links.new(group_014_1.outputs[0], compare_10.inputs[2])
			#group_014_1.Trailing -> compare_10.B
			_mn_cartoon_bs_alternate_axis.links.new(group_014_1.outputs[1], compare_10.inputs[3])
			#compare_10.Result -> boolean_math_12.Boolean
			_mn_cartoon_bs_alternate_axis.links.new(compare_10.outputs[0], boolean_math_12.inputs[0])
			#group_012.Is Helix -> boolean_math_12.Boolean
			_mn_cartoon_bs_alternate_axis.links.new(group_012.outputs[0], boolean_math_12.inputs[1])
			#vector_math_4.Vector -> switch_13.False
			_mn_cartoon_bs_alternate_axis.links.new(vector_math_4.outputs[0], switch_13.inputs[1])
			#vector_math_4.Vector -> group_20.Field
			_mn_cartoon_bs_alternate_axis.links.new(vector_math_4.outputs[0], group_20.inputs[0])
			#group_20.Field -> switch_13.True
			_mn_cartoon_bs_alternate_axis.links.new(group_20.outputs[0], switch_13.inputs[2])
			#integer_4.Integer -> group_20.Offset
			_mn_cartoon_bs_alternate_axis.links.new(integer_4.outputs[0], group_20.inputs[4])
			#boolean_math_12.Boolean -> switch_13.Switch
			_mn_cartoon_bs_alternate_axis.links.new(boolean_math_12.outputs[0], switch_13.inputs[0])
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
			atoms_socket_11 = _atoms_to_curves.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_11.attribute_domain = 'POINT'
			atoms_socket_11.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket_18 = _atoms_to_curves.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_18.attribute_domain = 'POINT'
			selection_socket_18.hide_value = True
			selection_socket_18.description = "Selection of atoms to apply this node to"
			
			#Socket BS Smoothing
			bs_smoothing_socket = _atoms_to_curves.interface.new_socket(name = "BS Smoothing", in_out='INPUT', socket_type = 'NodeSocketFloat')
			bs_smoothing_socket.subtype = 'FACTOR'
			bs_smoothing_socket.default_value = 1.0
			bs_smoothing_socket.min_value = 0.0
			bs_smoothing_socket.max_value = 1.0
			bs_smoothing_socket.attribute_domain = 'POINT'
			
			
			#initialize _atoms_to_curves nodes
			#node Frame.006
			frame_006 = _atoms_to_curves.nodes.new("NodeFrame")
			frame_006.label = "Break mesh where chain_id mismatch or distance cutoff"
			frame_006.name = "Frame.006"
			frame_006.label_size = 20
			frame_006.shrink = True
			
			#node Frame.007
			frame_007 = _atoms_to_curves.nodes.new("NodeFrame")
			frame_007.label = "Get immediate + and -- AA CA positions"
			frame_007.name = "Frame.007"
			frame_007.label_size = 20
			frame_007.shrink = True
			
			#node Frame.008
			frame_008 = _atoms_to_curves.nodes.new("NodeFrame")
			frame_008.label = "Calculate guide vectors for orientations"
			frame_008.name = "Frame.008"
			frame_008.label_size = 20
			frame_008.shrink = True
			
			#node Frame
			frame_5 = _atoms_to_curves.nodes.new("NodeFrame")
			frame_5.label = "Catch where it changes straight from AH to BS, could be better"
			frame_5.name = "Frame"
			frame_5.label_size = 20
			frame_5.shrink = True
			
			#node Frame.001
			frame_001_2 = _atoms_to_curves.nodes.new("NodeFrame")
			frame_001_2.label = "Split by Secondary Structure"
			frame_001_2.name = "Frame.001"
			frame_001_2.label_size = 20
			frame_001_2.shrink = True
			
			#node Frame.002
			frame_002_2 = _atoms_to_curves.nodes.new("NodeFrame")
			frame_002_2.label = "Turn backboen points to curves"
			frame_002_2.name = "Frame.002"
			frame_002_2.label_size = 20
			frame_002_2.shrink = True
			
			#node Compare.001
			compare_001_5 = _atoms_to_curves.nodes.new("FunctionNodeCompare")
			compare_001_5.name = "Compare.001"
			compare_001_5.data_type = 'INT'
			compare_001_5.mode = 'ELEMENT'
			compare_001_5.operation = 'NOT_EQUAL'
			
			#node Named Attribute.011
			named_attribute_011 = _atoms_to_curves.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_011.name = "Named Attribute.011"
			named_attribute_011.data_type = 'INT'
			#Name
			named_attribute_011.inputs[0].default_value = "chain_id"
			
			#node Evaluate at Index
			evaluate_at_index_3 = _atoms_to_curves.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_3.name = "Evaluate at Index"
			evaluate_at_index_3.data_type = 'INT'
			evaluate_at_index_3.domain = 'POINT'
			
			#node Evaluate at Index.001
			evaluate_at_index_001_3 = _atoms_to_curves.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001_3.name = "Evaluate at Index.001"
			evaluate_at_index_001_3.data_type = 'INT'
			evaluate_at_index_001_3.domain = 'POINT'
			
			#node Reroute.021
			reroute_021 = _atoms_to_curves.nodes.new("NodeReroute")
			reroute_021.name = "Reroute.021"
			#node Edge Vertices
			edge_vertices_1 = _atoms_to_curves.nodes.new("GeometryNodeInputMeshEdgeVertices")
			edge_vertices_1.name = "Edge Vertices"
			
			#node Vector Math
			vector_math_5 = _atoms_to_curves.nodes.new("ShaderNodeVectorMath")
			vector_math_5.name = "Vector Math"
			vector_math_5.operation = 'DISTANCE'
			
			#node Compare
			compare_11 = _atoms_to_curves.nodes.new("FunctionNodeCompare")
			compare_11.name = "Compare"
			compare_11.data_type = 'FLOAT'
			compare_11.mode = 'ELEMENT'
			compare_11.operation = 'GREATER_THAN'
			
			#node Math.001
			math_001_8 = _atoms_to_curves.nodes.new("ShaderNodeMath")
			math_001_8.name = "Math.001"
			math_001_8.operation = 'DIVIDE'
			math_001_8.use_clamp = False
			#Value
			math_001_8.inputs[0].default_value = 60.0
			#Value_001
			math_001_8.inputs[1].default_value = 1000.0
			
			#node Boolean Math.001
			boolean_math_001_10 = _atoms_to_curves.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_10.name = "Boolean Math.001"
			boolean_math_001_10.operation = 'OR'
			
			#node Delete Geometry
			delete_geometry_1 = _atoms_to_curves.nodes.new("GeometryNodeDeleteGeometry")
			delete_geometry_1.name = "Delete Geometry"
			delete_geometry_1.domain = 'EDGE'
			delete_geometry_1.mode = 'ALL'
			
			#node Store Named Attribute.001
			store_named_attribute_001_1 = _atoms_to_curves.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_001_1.name = "Store Named Attribute.001"
			store_named_attribute_001_1.data_type = 'FLOAT_VECTOR'
			store_named_attribute_001_1.domain = 'POINT'
			#Selection
			store_named_attribute_001_1.inputs[1].default_value = True
			#Name
			store_named_attribute_001_1.inputs[2].default_value = "reverse"
			
			#node Store Named Attribute
			store_named_attribute_5 = _atoms_to_curves.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_5.name = "Store Named Attribute"
			store_named_attribute_5.data_type = 'FLOAT_VECTOR'
			store_named_attribute_5.domain = 'POINT'
			#Selection
			store_named_attribute_5.inputs[1].default_value = True
			#Name
			store_named_attribute_5.inputs[2].default_value = "forward"
			
			#node Position.002
			position_002_1 = _atoms_to_curves.nodes.new("GeometryNodeInputPosition")
			position_002_1.name = "Position.002"
			
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
			boolean_math_005_1 = _atoms_to_curves.nodes.new("FunctionNodeBooleanMath")
			boolean_math_005_1.name = "Boolean Math.005"
			boolean_math_005_1.operation = 'AND'
			
			#node Boolean Math.009
			boolean_math_009 = _atoms_to_curves.nodes.new("FunctionNodeBooleanMath")
			boolean_math_009.name = "Boolean Math.009"
			boolean_math_009.operation = 'OR'
			
			#node Boolean Math.007
			boolean_math_007 = _atoms_to_curves.nodes.new("FunctionNodeBooleanMath")
			boolean_math_007.name = "Boolean Math.007"
			boolean_math_007.operation = 'AND'
			
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
			boolean_math_008 = _atoms_to_curves.nodes.new("FunctionNodeBooleanMath")
			boolean_math_008.name = "Boolean Math.008"
			boolean_math_008.operation = 'AND'
			
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
			boolean_math_004_4 = _atoms_to_curves.nodes.new("FunctionNodeBooleanMath")
			boolean_math_004_4.name = "Boolean Math.004"
			boolean_math_004_4.operation = 'OR'
			
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
			mesh_to_curve_1 = _atoms_to_curves.nodes.new("GeometryNodeMeshToCurve")
			mesh_to_curve_1.name = "Mesh to Curve"
			#Selection
			mesh_to_curve_1.inputs[1].default_value = True
			
			#node Reroute.023
			reroute_023 = _atoms_to_curves.nodes.new("NodeReroute")
			reroute_023.name = "Reroute.023"
			#node Reroute.002
			reroute_002_7 = _atoms_to_curves.nodes.new("NodeReroute")
			reroute_002_7.name = "Reroute.002"
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
			group_input_001_6 = _atoms_to_curves.nodes.new("NodeGroupInput")
			group_input_001_6.name = "Group Input.001"
			
			#node Group Output
			group_output_55 = _atoms_to_curves.nodes.new("NodeGroupOutput")
			group_output_55.name = "Group Output"
			group_output_55.is_active_output = True
			
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
			group_21 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_21.name = "Group"
			group_21.node_tree = _bs_smooth
			#Input_3
			group_21.inputs[2].default_value = 3
			
			#node Group.023
			group_023_1 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_023_1.name = "Group.023"
			group_023_1.node_tree = _expand_selection
			#Input_2
			group_023_1.inputs[1].default_value = 1
			
			#node Group.037
			group_037 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_037.name = "Group.037"
			group_037.node_tree = _mn_select_sec_struct
			#Socket_1
			group_037.inputs[0].default_value = True
			
			#node Group Input
			group_input_54 = _atoms_to_curves.nodes.new("NodeGroupInput")
			group_input_54.name = "Group Input"
			
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
			curve_to_mesh_3 = _atoms_to_curves.nodes.new("GeometryNodeCurveToMesh")
			curve_to_mesh_3.name = "Curve to Mesh"
			#Fill Caps
			curve_to_mesh_3.inputs[2].default_value = False
			
			#node Named Attribute.018
			named_attribute_018 = _atoms_to_curves.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_018.name = "Named Attribute.018"
			named_attribute_018.data_type = 'INT'
			#Name
			named_attribute_018.inputs[0].default_value = "chain_id"
			
			#node Group.001
			group_001_10 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_001_10.name = "Group.001"
			group_001_10.node_tree = is_alpha_carbon
			#Socket_1
			group_001_10.inputs[0].default_value = True
			#Socket_3
			group_001_10.inputs[1].default_value = False
			
			#node Group.006
			group_006_1 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_006_1.name = "Group.006"
			group_006_1.node_tree = _mn_topo_assign_backbone
			
			#node Group.008
			group_008 = _atoms_to_curves.nodes.new("GeometryNodeGroup")
			group_008.name = "Group.008"
			group_008.node_tree = _mn_cartoon_bs_alternate_axis
			
			
			
			#Set parents
			compare_001_5.parent = frame_006
			named_attribute_011.parent = frame_006
			evaluate_at_index_3.parent = frame_006
			evaluate_at_index_001_3.parent = frame_006
			reroute_021.parent = frame_006
			edge_vertices_1.parent = frame_006
			vector_math_5.parent = frame_006
			compare_11.parent = frame_006
			math_001_8.parent = frame_006
			boolean_math_001_10.parent = frame_006
			delete_geometry_1.parent = frame_006
			store_named_attribute_001_1.parent = frame_007
			store_named_attribute_5.parent = frame_007
			position_002_1.parent = frame_007
			store_named_attribute_015.parent = frame_008
			store_named_attribute_016.parent = frame_008
			store_named_attribute_017.parent = frame_008
			named_attribute_012.parent = frame_008
			named_attribute_013.parent = frame_008
			named_attribute_014.parent = frame_008
			group_022.parent = frame_5
			group_035.parent = frame_5
			boolean_math_005_1.parent = frame_5
			boolean_math_009.parent = frame_5
			boolean_math_007.parent = frame_5
			group_036.parent = frame_5
			boolean_math_010_1.parent = frame_5
			boolean_math_006.parent = frame_5
			boolean_math_008.parent = frame_5
			boolean_math_011.parent = frame_5
			group_034.parent = frame_5
			group_024_1.parent = frame_5
			mesh_to_curve_004.parent = frame_001_2
			mesh_to_curve_003.parent = frame_001_2
			mesh_to_curve_001.parent = frame_001_2
			mesh_to_curve_1.parent = frame_001_2
			reroute_023.parent = frame_001_2
			reroute_002_7.parent = frame_001_2
			separate_geometry_006.parent = frame_001_2
			separate_geometry_007.parent = frame_001_2
			separate_geometry_008.parent = frame_001_2
			group_012_1.parent = frame_007
			group_013.parent = frame_007
			separate_geometry_003.parent = frame_002_2
			separate_geometry_001_1.parent = frame_002_2
			mesh_to_points_1.parent = frame_002_2
			points_to_curves.parent = frame_002_2
			curve_to_mesh_3.parent = frame_002_2
			named_attribute_018.parent = frame_002_2
			group_001_10.parent = frame_002_2
			group_006_1.parent = frame_002_2
			group_008.parent = frame_008
			
			#Set locations
			frame_006.location = (-26.0, 380.0)
			frame_007.location = (-168.0, 46.0)
			frame_008.location = (-166.0, 3.0)
			frame_5.location = (6042.0, 80.0)
			frame_001_2.location = (458.0, -8.0)
			frame_002_2.location = (0.0, 0.0)
			compare_001_5.location = (-1907.6533203125, 300.176513671875)
			named_attribute_011.location = (-2304.4140625, 25.7803955078125)
			evaluate_at_index_3.location = (-2067.6533203125, 300.176513671875)
			evaluate_at_index_001_3.location = (-2067.6533203125, 120.176513671875)
			reroute_021.location = (-2087.6533203125, 100.176513671875)
			edge_vertices_1.location = (-2304.4140625, 165.7803955078125)
			vector_math_5.location = (-2064.4140625, -54.2196044921875)
			compare_11.location = (-1904.4140625, -54.2196044921875)
			math_001_8.location = (-2064.4140625, -194.2196044921875)
			boolean_math_001_10.location = (-1740.0, 300.0)
			delete_geometry_1.location = (-1740.0, 480.0)
			store_named_attribute_001_1.location = (-1062.2197265625, 834.4013671875)
			store_named_attribute_5.location = (-1222.2197265625, 834.4013671875)
			position_002_1.location = (-1222.2197265625, 474.4012451171875)
			store_named_attribute_015.location = (-563.97314453125, 856.68115234375)
			store_named_attribute_016.location = (-383.97314453125, 856.68115234375)
			store_named_attribute_017.location = (-203.97314453125, 856.68115234375)
			named_attribute_012.location = (-743.97314453125, 616.68115234375)
			named_attribute_013.location = (-743.97314453125, 336.68115234375)
			named_attribute_014.location = (-743.97314453125, 476.68115234375)
			group_022.location = (-5080.0, -580.0)
			group_035.location = (-5080.0, -860.0)
			boolean_math_005_1.location = (-4840.0, -660.0)
			boolean_math_009.location = (-4620.0, -660.0)
			boolean_math_007.location = (-4800.0, -60.0)
			group_036.location = (-5040.0, -180.0)
			boolean_math_010_1.location = (-4800.0, -220.0)
			boolean_math_006.location = (-4360.0, -320.0)
			boolean_math_008.location = (-4840.0, -820.0)
			boolean_math_011.location = (-4580.0, -100.0)
			group_034.location = (-5040.0, 100.0)
			group_024_1.location = (-5532.35107421875, -374.12896728515625)
			boolean_math_004_4.location = (1120.0, 520.0)
			mesh_to_curve_004.location = (1200.0, 940.0)
			mesh_to_curve_003.location = (1200.0, 820.0)
			mesh_to_curve_001.location = (1200.0, 700.0)
			mesh_to_curve_1.location = (1200.0, 580.0)
			reroute_023.location = (1260.0, 980.0)
			reroute_002_7.location = (960.0, 860.0)
			separate_geometry_006.location = (1040.0, 820.0)
			separate_geometry_007.location = (1040.0, 700.0)
			separate_geometry_008.location = (1040.0, 580.0)
			group_input_001_6.location = (-180.0, 720.0)
			group_output_55.location = (2120.0, 920.0)
			group_012_1.location = (-1222.2197265625, 614.4013671875)
			group_013.location = (-1062.2197265625, 614.4013671875)
			group_21.location = (60.0, 840.0)
			group_023_1.location = (960.0, 520.0)
			group_037.location = (880.0, 760.0)
			group_input_54.location = (-4220.0, 700.0)
			store_named_attribute_019.location = (-2860.0, 820.0)
			index_002_1.location = (-2860.0, 620.0)
			separate_geometry_003.location = (-3780.0, 780.0)
			separate_geometry_001_1.location = (-3600.0, 780.0)
			mesh_to_points_1.location = (-3420.0, 780.0)
			points_to_curves.location = (-3260.0, 780.0)
			curve_to_mesh_3.location = (-3100.0, 780.0)
			named_attribute_018.location = (-3420.0, 600.0)
			group_001_10.location = (-3780.0, 620.0)
			group_006_1.location = (-4020.0, 780.0)
			group_008.location = (-543.97314453125, 596.68115234375)
			
			#Set dimensions
			frame_006.width, frame_006.height = 764.5, 893.0
			frame_007.width, frame_007.height = 360.0, 480.0
			frame_008.width, frame_008.height = 740.0, 712.0
			frame_5.width, frame_5.height = 1372.5, 1282.0
			frame_001_2.width, frame_001_2.height = 444.0, 573.0
			frame_002_2.width, frame_002_2.height = 1120.0, 372.0
			compare_001_5.width, compare_001_5.height = 140.0, 100.0
			named_attribute_011.width, named_attribute_011.height = 140.0, 100.0
			evaluate_at_index_3.width, evaluate_at_index_3.height = 140.0, 100.0
			evaluate_at_index_001_3.width, evaluate_at_index_001_3.height = 140.0, 100.0
			reroute_021.width, reroute_021.height = 16.0, 100.0
			edge_vertices_1.width, edge_vertices_1.height = 140.0, 100.0
			vector_math_5.width, vector_math_5.height = 140.0, 100.0
			compare_11.width, compare_11.height = 140.0, 100.0
			math_001_8.width, math_001_8.height = 140.0, 100.0
			boolean_math_001_10.width, boolean_math_001_10.height = 140.0, 100.0
			delete_geometry_1.width, delete_geometry_1.height = 140.0, 100.0
			store_named_attribute_001_1.width, store_named_attribute_001_1.height = 140.0, 100.0
			store_named_attribute_5.width, store_named_attribute_5.height = 140.0, 100.0
			position_002_1.width, position_002_1.height = 140.0, 100.0
			store_named_attribute_015.width, store_named_attribute_015.height = 140.0, 100.0
			store_named_attribute_016.width, store_named_attribute_016.height = 140.0, 100.0
			store_named_attribute_017.width, store_named_attribute_017.height = 140.0, 100.0
			named_attribute_012.width, named_attribute_012.height = 140.0, 100.0
			named_attribute_013.width, named_attribute_013.height = 140.0, 100.0
			named_attribute_014.width, named_attribute_014.height = 140.0, 100.0
			group_022.width, group_022.height = 140.0, 100.0
			group_035.width, group_035.height = 140.0, 100.0
			boolean_math_005_1.width, boolean_math_005_1.height = 140.0, 100.0
			boolean_math_009.width, boolean_math_009.height = 140.0, 100.0
			boolean_math_007.width, boolean_math_007.height = 140.0, 100.0
			group_036.width, group_036.height = 140.0, 100.0
			boolean_math_010_1.width, boolean_math_010_1.height = 140.0, 100.0
			boolean_math_006.width, boolean_math_006.height = 140.0, 100.0
			boolean_math_008.width, boolean_math_008.height = 140.0, 100.0
			boolean_math_011.width, boolean_math_011.height = 140.0, 100.0
			group_034.width, group_034.height = 140.0, 100.0
			group_024_1.width, group_024_1.height = 158.9053955078125, 100.0
			boolean_math_004_4.width, boolean_math_004_4.height = 140.0, 100.0
			mesh_to_curve_004.width, mesh_to_curve_004.height = 140.0, 100.0
			mesh_to_curve_003.width, mesh_to_curve_003.height = 140.0, 100.0
			mesh_to_curve_001.width, mesh_to_curve_001.height = 140.0, 100.0
			mesh_to_curve_1.width, mesh_to_curve_1.height = 140.0, 100.0
			reroute_023.width, reroute_023.height = 16.0, 100.0
			reroute_002_7.width, reroute_002_7.height = 16.0, 100.0
			separate_geometry_006.width, separate_geometry_006.height = 140.0, 100.0
			separate_geometry_007.width, separate_geometry_007.height = 140.0, 100.0
			separate_geometry_008.width, separate_geometry_008.height = 140.0, 100.0
			group_input_001_6.width, group_input_001_6.height = 140.0, 100.0
			group_output_55.width, group_output_55.height = 140.0, 100.0
			group_012_1.width, group_012_1.height = 140.0, 100.0
			group_013.width, group_013.height = 140.0, 100.0
			group_21.width, group_21.height = 374.382080078125, 100.0
			group_023_1.width, group_023_1.height = 140.0, 100.0
			group_037.width, group_037.height = 233.448486328125, 100.0
			group_input_54.width, group_input_54.height = 140.0, 100.0
			store_named_attribute_019.width, store_named_attribute_019.height = 140.0, 100.0
			index_002_1.width, index_002_1.height = 140.0, 100.0
			separate_geometry_003.width, separate_geometry_003.height = 140.0, 100.0
			separate_geometry_001_1.width, separate_geometry_001_1.height = 140.0, 100.0
			mesh_to_points_1.width, mesh_to_points_1.height = 140.0, 100.0
			points_to_curves.width, points_to_curves.height = 140.0, 100.0
			curve_to_mesh_3.width, curve_to_mesh_3.height = 140.0, 100.0
			named_attribute_018.width, named_attribute_018.height = 140.0, 100.0
			group_001_10.width, group_001_10.height = 140.0, 100.0
			group_006_1.width, group_006_1.height = 206.7611083984375, 100.0
			group_008.width, group_008.height = 318.43975830078125, 100.0
			
			#initialize _atoms_to_curves links
			#group_023_1.Boolean -> boolean_math_004_4.Boolean
			_atoms_to_curves.links.new(group_023_1.outputs[0], boolean_math_004_4.inputs[0])
			#group_024_1.Is Helix -> boolean_math_010_1.Boolean
			_atoms_to_curves.links.new(group_024_1.outputs[0], boolean_math_010_1.inputs[1])
			#group_024_1.Is Sheet -> group_036.Value
			_atoms_to_curves.links.new(group_024_1.outputs[1], group_036.inputs[1])
			#group_024_1.Is Sheet -> boolean_math_005_1.Boolean
			_atoms_to_curves.links.new(group_024_1.outputs[1], boolean_math_005_1.inputs[0])
			#group_034.Value -> boolean_math_007.Boolean
			_atoms_to_curves.links.new(group_034.outputs[1], boolean_math_007.inputs[0])
			#group_024_1.Is Sheet -> group_034.Value
			_atoms_to_curves.links.new(group_024_1.outputs[1], group_034.inputs[1])
			#boolean_math_008.Boolean -> boolean_math_009.Boolean
			_atoms_to_curves.links.new(boolean_math_008.outputs[0], boolean_math_009.inputs[1])
			#position_002_1.Position -> group_013.Field
			_atoms_to_curves.links.new(position_002_1.outputs[0], group_013.inputs[0])
			#position_002_1.Position -> group_012_1.Field
			_atoms_to_curves.links.new(position_002_1.outputs[0], group_012_1.inputs[0])
			#group_012_1.Field -> store_named_attribute_5.Value
			_atoms_to_curves.links.new(group_012_1.outputs[0], store_named_attribute_5.inputs[3])
			#group_037.Is Helix -> separate_geometry_006.Selection
			_atoms_to_curves.links.new(group_037.outputs[0], separate_geometry_006.inputs[1])
			#group_024_1.Is Helix -> group_035.Value
			_atoms_to_curves.links.new(group_024_1.outputs[0], group_035.inputs[1])
			#boolean_math_006.Boolean -> boolean_math_004_4.Boolean
			_atoms_to_curves.links.new(boolean_math_006.outputs[0], boolean_math_004_4.inputs[1])
			#group_024_1.Is Sheet -> boolean_math_008.Boolean
			_atoms_to_curves.links.new(group_024_1.outputs[1], boolean_math_008.inputs[0])
			#separate_geometry_008.Selection -> mesh_to_curve_1.Mesh
			_atoms_to_curves.links.new(separate_geometry_008.outputs[0], mesh_to_curve_1.inputs[0])
			#boolean_math_007.Boolean -> boolean_math_011.Boolean
			_atoms_to_curves.links.new(boolean_math_007.outputs[0], boolean_math_011.inputs[0])
			#group_022.Value -> boolean_math_005_1.Boolean
			_atoms_to_curves.links.new(group_022.outputs[1], boolean_math_005_1.inputs[1])
			#store_named_attribute_5.Geometry -> store_named_attribute_001_1.Geometry
			_atoms_to_curves.links.new(store_named_attribute_5.outputs[0], store_named_attribute_001_1.inputs[0])
			#group_024_1.Is Helix -> group_022.Value
			_atoms_to_curves.links.new(group_024_1.outputs[0], group_022.inputs[1])
			#boolean_math_009.Boolean -> boolean_math_006.Boolean
			_atoms_to_curves.links.new(boolean_math_009.outputs[0], boolean_math_006.inputs[1])
			#reroute_002_7.Output -> separate_geometry_006.Geometry
			_atoms_to_curves.links.new(reroute_002_7.outputs[0], separate_geometry_006.inputs[0])
			#separate_geometry_006.Selection -> mesh_to_curve_003.Mesh
			_atoms_to_curves.links.new(separate_geometry_006.outputs[0], mesh_to_curve_003.inputs[0])
			#group_013.Field -> store_named_attribute_001_1.Value
			_atoms_to_curves.links.new(group_013.outputs[0], store_named_attribute_001_1.inputs[3])
			#group_035.Value -> boolean_math_008.Boolean
			_atoms_to_curves.links.new(group_035.outputs[1], boolean_math_008.inputs[1])
			#group_024_1.Is Helix -> boolean_math_007.Boolean
			_atoms_to_curves.links.new(group_024_1.outputs[0], boolean_math_007.inputs[1])
			#group_036.Value -> boolean_math_010_1.Boolean
			_atoms_to_curves.links.new(group_036.outputs[1], boolean_math_010_1.inputs[0])
			#separate_geometry_007.Selection -> mesh_to_curve_001.Mesh
			_atoms_to_curves.links.new(separate_geometry_007.outputs[0], mesh_to_curve_001.inputs[0])
			#boolean_math_010_1.Boolean -> boolean_math_011.Boolean
			_atoms_to_curves.links.new(boolean_math_010_1.outputs[0], boolean_math_011.inputs[1])
			#boolean_math_005_1.Boolean -> boolean_math_009.Boolean
			_atoms_to_curves.links.new(boolean_math_005_1.outputs[0], boolean_math_009.inputs[0])
			#boolean_math_011.Boolean -> boolean_math_006.Boolean
			_atoms_to_curves.links.new(boolean_math_011.outputs[0], boolean_math_006.inputs[0])
			#reroute_023.Output -> group_output_55.CA Mesh Line
			_atoms_to_curves.links.new(reroute_023.outputs[0], group_output_55.inputs[0])
			#mesh_to_curve_001.Curve -> group_output_55.BS Splines
			_atoms_to_curves.links.new(mesh_to_curve_001.outputs[0], group_output_55.inputs[4])
			#mesh_to_curve_1.Curve -> group_output_55.Loop Splines
			_atoms_to_curves.links.new(mesh_to_curve_1.outputs[0], group_output_55.inputs[6])
			#mesh_to_curve_003.Curve -> group_output_55.AH Splines
			_atoms_to_curves.links.new(mesh_to_curve_003.outputs[0], group_output_55.inputs[2])
			#reroute_002_7.Output -> mesh_to_curve_004.Mesh
			_atoms_to_curves.links.new(reroute_002_7.outputs[0], mesh_to_curve_004.inputs[0])
			#mesh_to_curve_004.Curve -> group_output_55.CA Splines
			_atoms_to_curves.links.new(mesh_to_curve_004.outputs[0], group_output_55.inputs[1])
			#edge_vertices_1.Vertex Index 2 -> evaluate_at_index_001_3.Index
			_atoms_to_curves.links.new(edge_vertices_1.outputs[1], evaluate_at_index_001_3.inputs[0])
			#edge_vertices_1.Vertex Index 1 -> evaluate_at_index_3.Index
			_atoms_to_curves.links.new(edge_vertices_1.outputs[0], evaluate_at_index_3.inputs[0])
			#reroute_021.Output -> evaluate_at_index_001_3.Value
			_atoms_to_curves.links.new(reroute_021.outputs[0], evaluate_at_index_001_3.inputs[1])
			#evaluate_at_index_001_3.Value -> compare_001_5.B
			_atoms_to_curves.links.new(evaluate_at_index_001_3.outputs[0], compare_001_5.inputs[3])
			#evaluate_at_index_3.Value -> compare_001_5.A
			_atoms_to_curves.links.new(evaluate_at_index_3.outputs[0], compare_001_5.inputs[2])
			#reroute_021.Output -> evaluate_at_index_3.Value
			_atoms_to_curves.links.new(reroute_021.outputs[0], evaluate_at_index_3.inputs[1])
			#named_attribute_011.Attribute -> reroute_021.Input
			_atoms_to_curves.links.new(named_attribute_011.outputs[0], reroute_021.inputs[0])
			#compare_001_5.Result -> boolean_math_001_10.Boolean
			_atoms_to_curves.links.new(compare_001_5.outputs[0], boolean_math_001_10.inputs[0])
			#boolean_math_001_10.Boolean -> delete_geometry_1.Selection
			_atoms_to_curves.links.new(boolean_math_001_10.outputs[0], delete_geometry_1.inputs[1])
			#edge_vertices_1.Position 1 -> vector_math_5.Vector
			_atoms_to_curves.links.new(edge_vertices_1.outputs[2], vector_math_5.inputs[0])
			#edge_vertices_1.Position 2 -> vector_math_5.Vector
			_atoms_to_curves.links.new(edge_vertices_1.outputs[3], vector_math_5.inputs[1])
			#vector_math_5.Value -> compare_11.A
			_atoms_to_curves.links.new(vector_math_5.outputs[1], compare_11.inputs[0])
			#compare_11.Result -> boolean_math_001_10.Boolean
			_atoms_to_curves.links.new(compare_11.outputs[0], boolean_math_001_10.inputs[1])
			#math_001_8.Value -> compare_11.B
			_atoms_to_curves.links.new(math_001_8.outputs[0], compare_11.inputs[1])
			#store_named_attribute_019.Geometry -> delete_geometry_1.Geometry
			_atoms_to_curves.links.new(store_named_attribute_019.outputs[0], delete_geometry_1.inputs[0])
			#named_attribute_012.Attribute -> group_008.N
			_atoms_to_curves.links.new(named_attribute_012.outputs[0], group_008.inputs[0])
			#named_attribute_014.Attribute -> group_008.C
			_atoms_to_curves.links.new(named_attribute_014.outputs[0], group_008.inputs[1])
			#named_attribute_013.Attribute -> group_008.O
			_atoms_to_curves.links.new(named_attribute_013.outputs[0], group_008.inputs[2])
			#store_named_attribute_015.Geometry -> store_named_attribute_016.Geometry
			_atoms_to_curves.links.new(store_named_attribute_015.outputs[0], store_named_attribute_016.inputs[0])
			#group_008.Z Vector for Euler -> store_named_attribute_015.Value
			_atoms_to_curves.links.new(group_008.outputs[0], store_named_attribute_015.inputs[3])
			#group_008.X Vector for Euler -> store_named_attribute_016.Value
			_atoms_to_curves.links.new(group_008.outputs[1], store_named_attribute_016.inputs[3])
			#store_named_attribute_016.Geometry -> store_named_attribute_017.Geometry
			_atoms_to_curves.links.new(store_named_attribute_016.outputs[0], store_named_attribute_017.inputs[0])
			#store_named_attribute_001_1.Geometry -> store_named_attribute_015.Geometry
			_atoms_to_curves.links.new(store_named_attribute_001_1.outputs[0], store_named_attribute_015.inputs[0])
			#group_21.Geometry -> reroute_002_7.Input
			_atoms_to_curves.links.new(group_21.outputs[0], reroute_002_7.inputs[0])
			#reroute_002_7.Output -> reroute_023.Input
			_atoms_to_curves.links.new(reroute_002_7.outputs[0], reroute_023.inputs[0])
			#reroute_002_7.Output -> separate_geometry_007.Geometry
			_atoms_to_curves.links.new(reroute_002_7.outputs[0], separate_geometry_007.inputs[0])
			#reroute_002_7.Output -> separate_geometry_008.Geometry
			_atoms_to_curves.links.new(reroute_002_7.outputs[0], separate_geometry_008.inputs[0])
			#boolean_math_004_4.Boolean -> separate_geometry_008.Selection
			_atoms_to_curves.links.new(boolean_math_004_4.outputs[0], separate_geometry_008.inputs[1])
			#group_037.Is Sheet -> separate_geometry_007.Selection
			_atoms_to_curves.links.new(group_037.outputs[1], separate_geometry_007.inputs[1])
			#group_037.Is Loop -> group_023_1.Input
			_atoms_to_curves.links.new(group_037.outputs[3], group_023_1.inputs[0])
			#separate_geometry_006.Selection -> group_output_55.AH Mesh Line
			_atoms_to_curves.links.new(separate_geometry_006.outputs[0], group_output_55.inputs[3])
			#separate_geometry_007.Selection -> group_output_55.BS Mesh Line
			_atoms_to_curves.links.new(separate_geometry_007.outputs[0], group_output_55.inputs[5])
			#separate_geometry_008.Selection -> group_output_55.Loop Mesh Line
			_atoms_to_curves.links.new(separate_geometry_008.outputs[0], group_output_55.inputs[7])
			#store_named_attribute_017.Geometry -> group_21.Geometry
			_atoms_to_curves.links.new(store_named_attribute_017.outputs[0], group_21.inputs[0])
			#group_input_001_6.BS Smoothing -> group_21.Factor
			_atoms_to_curves.links.new(group_input_001_6.outputs[2], group_21.inputs[1])
			#index_002_1.Index -> store_named_attribute_019.Value
			_atoms_to_curves.links.new(index_002_1.outputs[0], store_named_attribute_019.inputs[3])
			#group_input_54.Atoms -> group_006_1.Atoms
			_atoms_to_curves.links.new(group_input_54.outputs[0], group_006_1.inputs[0])
			#separate_geometry_003.Selection -> separate_geometry_001_1.Geometry
			_atoms_to_curves.links.new(separate_geometry_003.outputs[0], separate_geometry_001_1.inputs[0])
			#separate_geometry_001_1.Selection -> mesh_to_points_1.Mesh
			_atoms_to_curves.links.new(separate_geometry_001_1.outputs[0], mesh_to_points_1.inputs[0])
			#mesh_to_points_1.Points -> points_to_curves.Points
			_atoms_to_curves.links.new(mesh_to_points_1.outputs[0], points_to_curves.inputs[0])
			#named_attribute_018.Attribute -> points_to_curves.Curve Group ID
			_atoms_to_curves.links.new(named_attribute_018.outputs[0], points_to_curves.inputs[1])
			#points_to_curves.Curves -> curve_to_mesh_3.Curve
			_atoms_to_curves.links.new(points_to_curves.outputs[0], curve_to_mesh_3.inputs[0])
			#delete_geometry_1.Geometry -> store_named_attribute_5.Geometry
			_atoms_to_curves.links.new(delete_geometry_1.outputs[0], store_named_attribute_5.inputs[0])
			#group_006_1.Atoms -> separate_geometry_003.Geometry
			_atoms_to_curves.links.new(group_006_1.outputs[0], separate_geometry_003.inputs[0])
			#group_input_54.Selection -> separate_geometry_003.Selection
			_atoms_to_curves.links.new(group_input_54.outputs[1], separate_geometry_003.inputs[1])
			#curve_to_mesh_3.Mesh -> store_named_attribute_019.Geometry
			_atoms_to_curves.links.new(curve_to_mesh_3.outputs[0], store_named_attribute_019.inputs[0])
			#group_001_10.Selection -> separate_geometry_001_1.Selection
			_atoms_to_curves.links.new(group_001_10.outputs[0], separate_geometry_001_1.inputs[1])
			return _atoms_to_curves

		_atoms_to_curves = _atoms_to_curves_node_group()

		#initialize _mn_utils_style_cartoon node group
		def _mn_utils_style_cartoon_node_group():
			_mn_utils_style_cartoon = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_utils_style_cartoon")

			_mn_utils_style_cartoon.color_tag = 'GEOMETRY'
			_mn_utils_style_cartoon.description = ""

			_mn_utils_style_cartoon.is_modifier = True
			
			#_mn_utils_style_cartoon interface
			#Socket Cartoon Mesh
			cartoon_mesh_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Cartoon Mesh", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			cartoon_mesh_socket.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket_12 = _mn_utils_style_cartoon.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_12.attribute_domain = 'POINT'
			atoms_socket_12.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket_19 = _mn_utils_style_cartoon.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_19.attribute_domain = 'POINT'
			selection_socket_19.hide_value = True
			selection_socket_19.description = "Selection of atoms to apply this node to"
			
			#Socket Shade Smooth
			shade_smooth_socket_5 = _mn_utils_style_cartoon.interface.new_socket(name = "Shade Smooth", in_out='INPUT', socket_type = 'NodeSocketBool')
			shade_smooth_socket_5.attribute_domain = 'POINT'
			shade_smooth_socket_5.description = "Apply smooth shading to the created geometry"
			
			#Socket Interpolate Color
			interpolate_color_socket_1 = _mn_utils_style_cartoon.interface.new_socket(name = "Interpolate Color", in_out='INPUT', socket_type = 'NodeSocketBool')
			interpolate_color_socket_1.attribute_domain = 'POINT'
			interpolate_color_socket_1.description = "Interpolate between distinct color selections"
			
			#Socket Material
			material_socket_6 = _mn_utils_style_cartoon.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial')
			material_socket_6.attribute_domain = 'POINT'
			material_socket_6.description = "Material to apply to the resulting geometry"
			
			#Panel Arrows
			arrows_panel = _mn_utils_style_cartoon.interface.new_panel("Arrows")
			#Socket As Arrows
			as_arrows_socket = _mn_utils_style_cartoon.interface.new_socket(name = "As Arrows", in_out='INPUT', socket_type = 'NodeSocketBool', parent = arrows_panel)
			as_arrows_socket.attribute_domain = 'POINT'
			as_arrows_socket.description = "Render beta-strands with directional arrows."
			
			#Socket Arrows Sharp
			arrows_sharp_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Arrows Sharp", in_out='INPUT', socket_type = 'NodeSocketBool', parent = arrows_panel)
			arrows_sharp_socket.attribute_domain = 'POINT'
			
			#Socket Arrows Point
			arrows_point_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Arrows Point", in_out='INPUT', socket_type = 'NodeSocketBool', parent = arrows_panel)
			arrows_point_socket.attribute_domain = 'POINT'
			
			#Socket Arrow Thickness Scale
			arrow_thickness_scale_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Arrow Thickness Scale", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = arrows_panel)
			arrow_thickness_scale_socket.subtype = 'NONE'
			arrow_thickness_scale_socket.default_value = 1.0
			arrow_thickness_scale_socket.min_value = 0.0
			arrow_thickness_scale_socket.max_value = 10000.0
			arrow_thickness_scale_socket.attribute_domain = 'POINT'
			
			#Socket Arrow Width Scale
			arrow_width_scale_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Arrow Width Scale", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = arrows_panel)
			arrow_width_scale_socket.subtype = 'NONE'
			arrow_width_scale_socket.default_value = 1.0
			arrow_width_scale_socket.min_value = -10000.0
			arrow_width_scale_socket.max_value = 10000.0
			arrow_width_scale_socket.attribute_domain = 'POINT'
			
			
			#Panel Profile
			profile_panel = _mn_utils_style_cartoon.interface.new_panel("Profile")
			#Socket Profile Curve
			profile_curve_socket_1 = _mn_utils_style_cartoon.interface.new_socket(name = "Profile Curve", in_out='INPUT', socket_type = 'NodeSocketGeometry', parent = profile_panel)
			profile_curve_socket_1.attribute_domain = 'POINT'
			profile_curve_socket_1.description = "A custom curve-cirlce making SS ribbons."
			
			#Socket Profile Resolution
			profile_resolution_socket_1 = _mn_utils_style_cartoon.interface.new_socket(name = "Profile Resolution", in_out='INPUT', socket_type = 'NodeSocketInt', parent = profile_panel)
			profile_resolution_socket_1.subtype = 'NONE'
			profile_resolution_socket_1.default_value = 4
			profile_resolution_socket_1.min_value = 4
			profile_resolution_socket_1.max_value = 100
			profile_resolution_socket_1.attribute_domain = 'POINT'
			
			
			#Panel Sheet
			sheet_panel = _mn_utils_style_cartoon.interface.new_panel("Sheet")
			#Socket Sheet Rotate
			sheet_rotate_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Sheet Rotate", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = sheet_panel)
			sheet_rotate_socket.subtype = 'NONE'
			sheet_rotate_socket.default_value = 0.0
			sheet_rotate_socket.min_value = -3.4028234663852886e+38
			sheet_rotate_socket.max_value = 3.4028234663852886e+38
			sheet_rotate_socket.attribute_domain = 'POINT'
			
			#Socket Sheet Thickness
			sheet_thickness_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Sheet Thickness", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = sheet_panel)
			sheet_thickness_socket.subtype = 'NONE'
			sheet_thickness_socket.default_value = 0.5
			sheet_thickness_socket.min_value = 0.0
			sheet_thickness_socket.max_value = 3.4028234663852886e+38
			sheet_thickness_socket.attribute_domain = 'POINT'
			
			#Socket Sheet Width
			sheet_width_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Sheet Width", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = sheet_panel)
			sheet_width_socket.subtype = 'NONE'
			sheet_width_socket.default_value = 2.0
			sheet_width_socket.min_value = 0.0
			sheet_width_socket.max_value = 10000.0
			sheet_width_socket.attribute_domain = 'POINT'
			
			#Socket Sheet Smoothing
			sheet_smoothing_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Sheet Smoothing", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = sheet_panel)
			sheet_smoothing_socket.subtype = 'NONE'
			sheet_smoothing_socket.default_value = 1.0
			sheet_smoothing_socket.min_value = 0.0
			sheet_smoothing_socket.max_value = 1.0
			sheet_smoothing_socket.attribute_domain = 'POINT'
			
			#Socket Sheet Subdivision
			sheet_subdivision_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Sheet Subdivision", in_out='INPUT', socket_type = 'NodeSocketInt', parent = sheet_panel)
			sheet_subdivision_socket.subtype = 'NONE'
			sheet_subdivision_socket.default_value = 3
			sheet_subdivision_socket.min_value = 1
			sheet_subdivision_socket.max_value = 20
			sheet_subdivision_socket.attribute_domain = 'POINT'
			
			
			#Panel Cylinder
			cylinder_panel = _mn_utils_style_cartoon.interface.new_panel("Cylinder")
			#Socket As Cylinders
			as_cylinders_socket = _mn_utils_style_cartoon.interface.new_socket(name = "As Cylinders", in_out='INPUT', socket_type = 'NodeSocketBool', parent = cylinder_panel)
			as_cylinders_socket.attribute_domain = 'POINT'
			
			#Socket Cylinder Curved
			cylinder_curved_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Cylinder Curved", in_out='INPUT', socket_type = 'NodeSocketBool', parent = cylinder_panel)
			cylinder_curved_socket.attribute_domain = 'POINT'
			
			#Socket Cylinder Radius
			cylinder_radius_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Cylinder Radius", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = cylinder_panel)
			cylinder_radius_socket.subtype = 'NONE'
			cylinder_radius_socket.default_value = 2.0
			cylinder_radius_socket.min_value = 0.0
			cylinder_radius_socket.max_value = 10000.0
			cylinder_radius_socket.attribute_domain = 'POINT'
			
			#Socket Cylinder Resolution
			cylinder_resolution_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Cylinder Resolution", in_out='INPUT', socket_type = 'NodeSocketInt', parent = cylinder_panel)
			cylinder_resolution_socket.subtype = 'NONE'
			cylinder_resolution_socket.default_value = 12
			cylinder_resolution_socket.min_value = 3
			cylinder_resolution_socket.max_value = 512
			cylinder_resolution_socket.attribute_domain = 'POINT'
			
			#Socket Cylinder Subdivisions
			cylinder_subdivisions_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Cylinder Subdivisions", in_out='INPUT', socket_type = 'NodeSocketInt', parent = cylinder_panel)
			cylinder_subdivisions_socket.subtype = 'NONE'
			cylinder_subdivisions_socket.default_value = 5
			cylinder_subdivisions_socket.min_value = 1
			cylinder_subdivisions_socket.max_value = 2147483647
			cylinder_subdivisions_socket.attribute_domain = 'POINT'
			
			
			#Panel Helix
			helix_panel = _mn_utils_style_cartoon.interface.new_panel("Helix")
			#Socket Helix Rotate
			helix_rotate_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Helix Rotate", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = helix_panel)
			helix_rotate_socket.subtype = 'NONE'
			helix_rotate_socket.default_value = 0.0
			helix_rotate_socket.min_value = -3.4028234663852886e+38
			helix_rotate_socket.max_value = 3.4028234663852886e+38
			helix_rotate_socket.attribute_domain = 'POINT'
			
			#Socket Helix Thickness
			helix_thickness_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Helix Thickness", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = helix_panel)
			helix_thickness_socket.subtype = 'NONE'
			helix_thickness_socket.default_value = 0.5
			helix_thickness_socket.min_value = 0.0
			helix_thickness_socket.max_value = 10000.0
			helix_thickness_socket.attribute_domain = 'POINT'
			
			#Socket Helix Width
			helix_width_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Helix Width", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = helix_panel)
			helix_width_socket.subtype = 'NONE'
			helix_width_socket.default_value = 2.0
			helix_width_socket.min_value = -3.4028234663852886e+38
			helix_width_socket.max_value = 3.4028234663852886e+38
			helix_width_socket.attribute_domain = 'POINT'
			
			#Socket Helix Subdivisions
			helix_subdivisions_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Helix Subdivisions", in_out='INPUT', socket_type = 'NodeSocketInt', parent = helix_panel)
			helix_subdivisions_socket.subtype = 'NONE'
			helix_subdivisions_socket.default_value = 5
			helix_subdivisions_socket.min_value = 1
			helix_subdivisions_socket.max_value = 20
			helix_subdivisions_socket.attribute_domain = 'POINT'
			
			#Socket Helix smoothing
			helix_smoothing_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Helix smoothing", in_out='INPUT', socket_type = 'NodeSocketBool', parent = helix_panel)
			helix_smoothing_socket.attribute_domain = 'POINT'
			helix_smoothing_socket.description = "Smoothen out AH to be more cylindrical."
			
			
			#Panel Loop
			loop_panel = _mn_utils_style_cartoon.interface.new_panel("Loop")
			#Socket Loop Subdivisions
			loop_subdivisions_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Loop Subdivisions", in_out='INPUT', socket_type = 'NodeSocketInt', parent = loop_panel)
			loop_subdivisions_socket.subtype = 'NONE'
			loop_subdivisions_socket.default_value = 6
			loop_subdivisions_socket.min_value = 1
			loop_subdivisions_socket.max_value = 2147483647
			loop_subdivisions_socket.attribute_domain = 'POINT'
			
			#Socket Loop Radius
			loop_radius_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Loop Radius", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = loop_panel)
			loop_radius_socket.subtype = 'NONE'
			loop_radius_socket.default_value = 0.30000001192092896
			loop_radius_socket.min_value = 0.0
			loop_radius_socket.max_value = 3.0
			loop_radius_socket.attribute_domain = 'POINT'
			
			#Socket Loop Resolution
			loop_resolution_socket = _mn_utils_style_cartoon.interface.new_socket(name = "Loop Resolution", in_out='INPUT', socket_type = 'NodeSocketInt', parent = loop_panel)
			loop_resolution_socket.subtype = 'NONE'
			loop_resolution_socket.default_value = 8
			loop_resolution_socket.min_value = 3
			loop_resolution_socket.max_value = 512
			loop_resolution_socket.attribute_domain = 'POINT'
			
			
			
			#initialize _mn_utils_style_cartoon nodes
			#node Frame.006
			frame_006_1 = _mn_utils_style_cartoon.nodes.new("NodeFrame")
			frame_006_1.label = "Create Alpha-Helix Cylinder Geometry"
			frame_006_1.name = "Frame.006"
			frame_006_1.label_size = 20
			frame_006_1.shrink = True
			
			#node Frame.009
			frame_009 = _mn_utils_style_cartoon.nodes.new("NodeFrame")
			frame_009.label = "Straight cylinder if selected or less <= 4 AA"
			frame_009.name = "Frame.009"
			frame_009.label_size = 20
			frame_009.shrink = True
			
			#node Frame.008
			frame_008_1 = _mn_utils_style_cartoon.nodes.new("NodeFrame")
			frame_008_1.label = "Offset to be centre of helix"
			frame_008_1.name = "Frame.008"
			frame_008_1.label_size = 20
			frame_008_1.shrink = True
			
			#node Frame.005
			frame_005_1 = _mn_utils_style_cartoon.nodes.new("NodeFrame")
			frame_005_1.label = "Creating Alpha-helix Geometry"
			frame_005_1.name = "Frame.005"
			frame_005_1.label_size = 20
			frame_005_1.shrink = True
			
			#node Frame.007
			frame_007_1 = _mn_utils_style_cartoon.nodes.new("NodeFrame")
			frame_007_1.label = "DEBUG Arrows for Debugging"
			frame_007_1.name = "Frame.007"
			frame_007_1.label_size = 20
			frame_007_1.shrink = True
			
			#node Frame.003
			frame_003_2 = _mn_utils_style_cartoon.nodes.new("NodeFrame")
			frame_003_2.label = "Creating Loop Geometry"
			frame_003_2.name = "Frame.003"
			frame_003_2.label_size = 20
			frame_003_2.shrink = True
			
			#node Frame.004
			frame_004_1 = _mn_utils_style_cartoon.nodes.new("NodeFrame")
			frame_004_1.label = "Creating Beta-sheet Geometry"
			frame_004_1.name = "Frame.004"
			frame_004_1.label_size = 20
			frame_004_1.shrink = True
			
			#node Set Spline Resolution.002
			set_spline_resolution_002 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSetSplineResolution")
			set_spline_resolution_002.name = "Set Spline Resolution.002"
			#Selection
			set_spline_resolution_002.inputs[1].default_value = True
			
			#node Reroute.006
			reroute_006_1 = _mn_utils_style_cartoon.nodes.new("NodeReroute")
			reroute_006_1.name = "Reroute.006"
			#node Boolean Math.016
			boolean_math_016 = _mn_utils_style_cartoon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_016.name = "Boolean Math.016"
			boolean_math_016.operation = 'AND'
			
			#node Separate Geometry.005
			separate_geometry_005 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_005.label = "Selection + Alpha Helices Only"
			separate_geometry_005.name = "Separate Geometry.005"
			separate_geometry_005.domain = 'POINT'
			
			#node Group Input.002
			group_input_002_3 = _mn_utils_style_cartoon.nodes.new("NodeGroupInput")
			group_input_002_3.name = "Group Input.002"
			group_input_002_3.outputs[0].hide = True
			group_input_002_3.outputs[1].hide = True
			group_input_002_3.outputs[2].hide = True
			group_input_002_3.outputs[3].hide = True
			group_input_002_3.outputs[4].hide = True
			group_input_002_3.outputs[5].hide = True
			group_input_002_3.outputs[8].hide = True
			group_input_002_3.outputs[9].hide = True
			group_input_002_3.outputs[10].hide = True
			group_input_002_3.outputs[11].hide = True
			group_input_002_3.outputs[12].hide = True
			group_input_002_3.outputs[13].hide = True
			group_input_002_3.outputs[14].hide = True
			group_input_002_3.outputs[15].hide = True
			group_input_002_3.outputs[16].hide = True
			group_input_002_3.outputs[22].hide = True
			group_input_002_3.outputs[23].hide = True
			group_input_002_3.outputs[24].hide = True
			group_input_002_3.outputs[25].hide = True
			group_input_002_3.outputs[26].hide = True
			group_input_002_3.outputs[27].hide = True
			group_input_002_3.outputs[28].hide = True
			group_input_002_3.outputs[29].hide = True
			group_input_002_3.outputs[30].hide = True
			
			#node Mesh to Curve.002
			mesh_to_curve_002 = _mn_utils_style_cartoon.nodes.new("GeometryNodeMeshToCurve")
			mesh_to_curve_002.name = "Mesh to Curve.002"
			#Selection
			mesh_to_curve_002.inputs[1].default_value = True
			
			#node Set Position.004
			set_position_004 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSetPosition")
			set_position_004.name = "Set Position.004"
			#Position
			set_position_004.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Boolean Math.017
			boolean_math_017 = _mn_utils_style_cartoon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_017.name = "Boolean Math.017"
			boolean_math_017.operation = 'NOT'
			
			#node Endpoint Selection.001
			endpoint_selection_001_2 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_001_2.name = "Endpoint Selection.001"
			#Start Size
			endpoint_selection_001_2.inputs[0].default_value = 1
			#End Size
			endpoint_selection_001_2.inputs[1].default_value = 1
			
			#node Switch.003
			switch_003 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSwitch")
			switch_003.name = "Switch.003"
			switch_003.input_type = 'INT'
			#False
			switch_003.inputs[1].default_value = 2
			
			#node Math.004
			math_004 = _mn_utils_style_cartoon.nodes.new("ShaderNodeMath")
			math_004.name = "Math.004"
			math_004.operation = 'MAXIMUM'
			math_004.use_clamp = False
			#Value_001
			math_004.inputs[1].default_value = 2.0
			
			#node Math.005
			math_005 = _mn_utils_style_cartoon.nodes.new("ShaderNodeMath")
			math_005.name = "Math.005"
			math_005.operation = 'DIVIDE'
			math_005.use_clamp = False
			#Value_001
			math_005.inputs[1].default_value = 4.0
			
			#node Spline Length.001
			spline_length_001 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSplineLength")
			spline_length_001.name = "Spline Length.001"
			
			#node Vector Rotate
			vector_rotate = _mn_utils_style_cartoon.nodes.new("ShaderNodeVectorRotate")
			vector_rotate.name = "Vector Rotate"
			vector_rotate.invert = False
			vector_rotate.rotation_type = 'EULER_XYZ'
			#Center
			vector_rotate.inputs[1].default_value = (0.0, 0.0, 0.0)
			
			#node Vector
			vector = _mn_utils_style_cartoon.nodes.new("FunctionNodeInputVector")
			vector.name = "Vector"
			vector.vector = (0.0, 1.0, 0.0)
			
			#node Vector Math.001
			vector_math_001_1 = _mn_utils_style_cartoon.nodes.new("ShaderNodeVectorMath")
			vector_math_001_1.name = "Vector Math.001"
			vector_math_001_1.operation = 'SCALE'
			
			#node Reroute.007
			reroute_007_2 = _mn_utils_style_cartoon.nodes.new("NodeReroute")
			reroute_007_2.name = "Reroute.007"
			#node Group.008
			group_008_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_008_1.name = "Group.008"
			group_008_1.node_tree = _guide_rotation
			#Input_1
			group_008_1.inputs[0].default_value = 0.0
			
			#node Resample Curve.001
			resample_curve_001 = _mn_utils_style_cartoon.nodes.new("GeometryNodeResampleCurve")
			resample_curve_001.name = "Resample Curve.001"
			resample_curve_001.mode = 'COUNT'
			#Selection
			resample_curve_001.inputs[1].default_value = True
			
			#node Set Handle Type.002
			set_handle_type_002 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveSetHandles")
			set_handle_type_002.name = "Set Handle Type.002"
			set_handle_type_002.handle_type = 'AUTO'
			set_handle_type_002.mode = {'LEFT', 'RIGHT'}
			#Selection
			set_handle_type_002.inputs[1].default_value = True
			
			#node Set Spline Type
			set_spline_type = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveSplineType")
			set_spline_type.name = "Set Spline Type"
			set_spline_type.spline_type = 'BEZIER'
			#Selection
			set_spline_type.inputs[1].default_value = True
			
			#node Group.018
			group_018_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_018_1.name = "Group.018"
			group_018_1.node_tree = _mn_select_sec_struct
			#Socket_1
			group_018_1.inputs[0].default_value = True
			
			#node Boolean Math.003
			boolean_math_003_4 = _mn_utils_style_cartoon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003_4.name = "Boolean Math.003"
			boolean_math_003_4.operation = 'AND'
			
			#node Boolean Math.001
			boolean_math_001_11 = _mn_utils_style_cartoon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_11.name = "Boolean Math.001"
			boolean_math_001_11.operation = 'NOT'
			
			#node Group Input.010
			group_input_010 = _mn_utils_style_cartoon.nodes.new("NodeGroupInput")
			group_input_010.name = "Group Input.010"
			group_input_010.outputs[0].hide = True
			group_input_010.outputs[1].hide = True
			group_input_010.outputs[2].hide = True
			group_input_010.outputs[3].hide = True
			group_input_010.outputs[4].hide = True
			group_input_010.outputs[5].hide = True
			group_input_010.outputs[8].hide = True
			group_input_010.outputs[9].hide = True
			group_input_010.outputs[10].hide = True
			group_input_010.outputs[11].hide = True
			group_input_010.outputs[12].hide = True
			group_input_010.outputs[13].hide = True
			group_input_010.outputs[14].hide = True
			group_input_010.outputs[15].hide = True
			group_input_010.outputs[16].hide = True
			group_input_010.outputs[18].hide = True
			group_input_010.outputs[19].hide = True
			group_input_010.outputs[20].hide = True
			group_input_010.outputs[21].hide = True
			group_input_010.outputs[22].hide = True
			group_input_010.outputs[23].hide = True
			group_input_010.outputs[24].hide = True
			group_input_010.outputs[25].hide = True
			group_input_010.outputs[26].hide = True
			group_input_010.outputs[27].hide = True
			group_input_010.outputs[28].hide = True
			group_input_010.outputs[29].hide = True
			group_input_010.outputs[30].hide = True
			
			#node Combine XYZ.002
			combine_xyz_002_1 = _mn_utils_style_cartoon.nodes.new("ShaderNodeCombineXYZ")
			combine_xyz_002_1.name = "Combine XYZ.002"
			#X
			combine_xyz_002_1.inputs[0].default_value = 1.0
			
			#node Reroute.011
			reroute_011_1 = _mn_utils_style_cartoon.nodes.new("NodeReroute")
			reroute_011_1.name = "Reroute.011"
			#node Reroute.012
			reroute_012_1 = _mn_utils_style_cartoon.nodes.new("NodeReroute")
			reroute_012_1.name = "Reroute.012"
			#node Math.001
			math_001_9 = _mn_utils_style_cartoon.nodes.new("ShaderNodeMath")
			math_001_9.name = "Math.001"
			math_001_9.hide = True
			math_001_9.operation = 'ADD'
			math_001_9.use_clamp = False
			#Value_001
			math_001_9.inputs[1].default_value = 0.5
			
			#node Join Geometry.001
			join_geometry_001_3 = _mn_utils_style_cartoon.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_001_3.name = "Join Geometry.001"
			join_geometry_001_3.hide = True
			
			#node Separate Geometry.003
			separate_geometry_003_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_003_1.name = "Separate Geometry.003"
			separate_geometry_003_1.domain = 'POINT'
			
			#node Mesh to Curve
			mesh_to_curve_2 = _mn_utils_style_cartoon.nodes.new("GeometryNodeMeshToCurve")
			mesh_to_curve_2.name = "Mesh to Curve"
			#Selection
			mesh_to_curve_2.inputs[1].default_value = True
			
			#node Set Spline Type.002
			set_spline_type_002 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveSplineType")
			set_spline_type_002.name = "Set Spline Type.002"
			set_spline_type_002.spline_type = 'BEZIER'
			#Selection
			set_spline_type_002.inputs[1].default_value = True
			
			#node Set Handle Type
			set_handle_type = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveSetHandles")
			set_handle_type.name = "Set Handle Type"
			set_handle_type.handle_type = 'AUTO'
			set_handle_type.mode = {'LEFT', 'RIGHT'}
			#Selection
			set_handle_type.inputs[1].default_value = True
			
			#node Set Handle Positions.001
			set_handle_positions_001_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSetCurveHandlePositions")
			set_handle_positions_001_1.name = "Set Handle Positions.001"
			set_handle_positions_001_1.mode = 'RIGHT'
			#Position
			set_handle_positions_001_1.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Set Handle Positions.002
			set_handle_positions_002 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSetCurveHandlePositions")
			set_handle_positions_002.name = "Set Handle Positions.002"
			set_handle_positions_002.mode = 'LEFT'
			#Position
			set_handle_positions_002.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Reroute.002
			reroute_002_8 = _mn_utils_style_cartoon.nodes.new("NodeReroute")
			reroute_002_8.name = "Reroute.002"
			#node Reroute.008
			reroute_008_1 = _mn_utils_style_cartoon.nodes.new("NodeReroute")
			reroute_008_1.name = "Reroute.008"
			#node Endpoint Selection.002
			endpoint_selection_002_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_002_1.name = "Endpoint Selection.002"
			#Start Size
			endpoint_selection_002_1.inputs[0].default_value = 1
			#End Size
			endpoint_selection_002_1.inputs[1].default_value = 0
			
			#node Endpoint Selection.003
			endpoint_selection_003_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_003_1.name = "Endpoint Selection.003"
			#Start Size
			endpoint_selection_003_1.inputs[0].default_value = 0
			#End Size
			endpoint_selection_003_1.inputs[1].default_value = 1
			
			#node Store Named Attribute.002
			store_named_attribute_002_2 = _mn_utils_style_cartoon.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_002_2.name = "Store Named Attribute.002"
			store_named_attribute_002_2.data_type = 'BOOLEAN'
			store_named_attribute_002_2.domain = 'EDGE'
			#Selection
			store_named_attribute_002_2.inputs[1].default_value = True
			#Name
			store_named_attribute_002_2.inputs[2].default_value = "sharp_edge"
			
			#node Group Input.004
			group_input_004_1 = _mn_utils_style_cartoon.nodes.new("NodeGroupInput")
			group_input_004_1.name = "Group Input.004"
			group_input_004_1.outputs[0].hide = True
			group_input_004_1.outputs[1].hide = True
			group_input_004_1.outputs[2].hide = True
			group_input_004_1.outputs[3].hide = True
			group_input_004_1.outputs[4].hide = True
			group_input_004_1.outputs[5].hide = True
			group_input_004_1.outputs[8].hide = True
			group_input_004_1.outputs[9].hide = True
			group_input_004_1.outputs[12].hide = True
			group_input_004_1.outputs[13].hide = True
			group_input_004_1.outputs[14].hide = True
			group_input_004_1.outputs[15].hide = True
			group_input_004_1.outputs[16].hide = True
			group_input_004_1.outputs[17].hide = True
			group_input_004_1.outputs[18].hide = True
			group_input_004_1.outputs[19].hide = True
			group_input_004_1.outputs[20].hide = True
			group_input_004_1.outputs[21].hide = True
			group_input_004_1.outputs[26].hide = True
			group_input_004_1.outputs[27].hide = True
			group_input_004_1.outputs[28].hide = True
			group_input_004_1.outputs[29].hide = True
			group_input_004_1.outputs[30].hide = True
			
			#node Group Input.007
			group_input_007 = _mn_utils_style_cartoon.nodes.new("NodeGroupInput")
			group_input_007.name = "Group Input.007"
			group_input_007.outputs[0].hide = True
			group_input_007.outputs[1].hide = True
			group_input_007.outputs[3].hide = True
			group_input_007.outputs[4].hide = True
			group_input_007.outputs[5].hide = True
			group_input_007.outputs[8].hide = True
			group_input_007.outputs[9].hide = True
			group_input_007.outputs[10].hide = True
			group_input_007.outputs[11].hide = True
			group_input_007.outputs[12].hide = True
			group_input_007.outputs[13].hide = True
			group_input_007.outputs[14].hide = True
			group_input_007.outputs[15].hide = True
			group_input_007.outputs[16].hide = True
			group_input_007.outputs[17].hide = True
			group_input_007.outputs[18].hide = True
			group_input_007.outputs[19].hide = True
			group_input_007.outputs[20].hide = True
			group_input_007.outputs[21].hide = True
			group_input_007.outputs[22].hide = True
			group_input_007.outputs[23].hide = True
			group_input_007.outputs[24].hide = True
			group_input_007.outputs[25].hide = True
			group_input_007.outputs[26].hide = True
			group_input_007.outputs[27].hide = True
			group_input_007.outputs[28].hide = True
			group_input_007.outputs[29].hide = True
			group_input_007.outputs[30].hide = True
			
			#node Boolean Math.004
			boolean_math_004_5 = _mn_utils_style_cartoon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_004_5.name = "Boolean Math.004"
			boolean_math_004_5.operation = 'NOT'
			boolean_math_004_5.inputs[1].hide = True
			
			#node Edge Angle.001
			edge_angle_001 = _mn_utils_style_cartoon.nodes.new("GeometryNodeInputMeshEdgeAngle")
			edge_angle_001.name = "Edge Angle.001"
			
			#node Compare.006
			compare_006_1 = _mn_utils_style_cartoon.nodes.new("FunctionNodeCompare")
			compare_006_1.name = "Compare.006"
			compare_006_1.data_type = 'FLOAT'
			compare_006_1.mode = 'ELEMENT'
			compare_006_1.operation = 'GREATER_THAN'
			#B
			compare_006_1.inputs[1].default_value = 1.0471975803375244
			
			#node Boolean Math.002
			boolean_math_002_9 = _mn_utils_style_cartoon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_9.name = "Boolean Math.002"
			boolean_math_002_9.operation = 'OR'
			
			#node Realize Instances
			realize_instances_3 = _mn_utils_style_cartoon.nodes.new("GeometryNodeRealizeInstances")
			realize_instances_3.name = "Realize Instances"
			realize_instances_3.hide = True
			#Selection
			realize_instances_3.inputs[1].default_value = True
			#Realize All
			realize_instances_3.inputs[2].default_value = True
			#Depth
			realize_instances_3.inputs[3].default_value = 0
			
			#node Position
			position_4 = _mn_utils_style_cartoon.nodes.new("GeometryNodeInputPosition")
			position_4.name = "Position"
			
			#node Group.033
			group_033 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_033.name = "Group.033"
			group_033.node_tree = _guide_rotation
			#Input_1
			group_033.inputs[0].default_value = 0.0
			
			#node Group.004
			group_004_2 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_004_2.name = "Group.004"
			group_004_2.node_tree = _debug_arrows
			#Input_5
			group_004_2.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Input_2
			group_004_2.inputs[4].default_value = (0.30000001192092896, 0.30000001192092896, 0.30000001192092896)
			
			#node Switch
			switch_14 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSwitch")
			switch_14.label = "DEBUG"
			switch_14.name = "Switch"
			switch_14.input_type = 'GEOMETRY'
			#Switch
			switch_14.inputs[0].default_value = False
			
			#node Reroute
			reroute_15 = _mn_utils_style_cartoon.nodes.new("NodeReroute")
			reroute_15.name = "Reroute"
			#node Reroute.004
			reroute_004_1 = _mn_utils_style_cartoon.nodes.new("NodeReroute")
			reroute_004_1.name = "Reroute.004"
			#node Endpoint Selection
			endpoint_selection_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_1.name = "Endpoint Selection"
			#Start Size
			endpoint_selection_1.inputs[0].default_value = 1
			#End Size
			endpoint_selection_1.inputs[1].default_value = 1
			
			#node Group.005
			group_005_2 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_005_2.name = "Group.005"
			group_005_2.node_tree = _selective_scale
			#Input_3
			group_005_2.inputs[2].default_value = 0.800000011920929
			
			#node Set Spline Resolution.001
			set_spline_resolution_001 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSetSplineResolution")
			set_spline_resolution_001.name = "Set Spline Resolution.001"
			#Selection
			set_spline_resolution_001.inputs[1].default_value = True
			
			#node Group.032
			group_032 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_032.name = "Group.032"
			group_032.node_tree = _curve_ends_adjust_angle
			#Input_2
			group_032.inputs[1].default_value = 3.0
			#Input_3
			group_032.inputs[2].default_value = 0.4200000762939453
			
			#node Group Input.006
			group_input_006 = _mn_utils_style_cartoon.nodes.new("NodeGroupInput")
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
			group_input_006.outputs[11].hide = True
			group_input_006.outputs[12].hide = True
			group_input_006.outputs[13].hide = True
			group_input_006.outputs[14].hide = True
			group_input_006.outputs[15].hide = True
			group_input_006.outputs[16].hide = True
			group_input_006.outputs[17].hide = True
			group_input_006.outputs[18].hide = True
			group_input_006.outputs[19].hide = True
			group_input_006.outputs[20].hide = True
			group_input_006.outputs[21].hide = True
			group_input_006.outputs[22].hide = True
			group_input_006.outputs[23].hide = True
			group_input_006.outputs[24].hide = True
			group_input_006.outputs[25].hide = True
			group_input_006.outputs[26].hide = True
			group_input_006.outputs[30].hide = True
			
			#node Group.029
			group_029_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_029_1.name = "Group.029"
			group_029_1.mute = True
			group_029_1.node_tree = _curve_ends_adjust_position
			#Input_2
			group_029_1.inputs[1].default_value = 0.30000001192092896
			
			#node Set Handle Type.003
			set_handle_type_003 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveSetHandles")
			set_handle_type_003.name = "Set Handle Type.003"
			set_handle_type_003.handle_type = 'AUTO'
			set_handle_type_003.mode = {'LEFT', 'RIGHT'}
			#Selection
			set_handle_type_003.inputs[1].default_value = True
			
			#node Set Spline Type.001
			set_spline_type_001_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveSplineType")
			set_spline_type_001_1.name = "Set Spline Type.001"
			set_spline_type_001_1.spline_type = 'BEZIER'
			#Selection
			set_spline_type_001_1.inputs[1].default_value = True
			
			#node Group.030
			group_030_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_030_1.name = "Group.030"
			group_030_1.node_tree = _curve_to_mesh
			#Input_3
			group_030_1.inputs[3].default_value = True
			
			#node Group.028
			group_028_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_028_1.name = "Group.028"
			group_028_1.node_tree = _curve_end_fix_color
			
			#node Set Spline Type.003
			set_spline_type_003 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveSplineType")
			set_spline_type_003.name = "Set Spline Type.003"
			set_spline_type_003.spline_type = 'BEZIER'
			#Selection
			set_spline_type_003.inputs[1].default_value = True
			
			#node Group.009
			group_009_2 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_009_2.name = "Group.009"
			group_009_2.node_tree = _guide_rotation
			#Input_1
			group_009_2.inputs[0].default_value = 0.0
			
			#node Join Geometry.002
			join_geometry_002_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_002_1.name = "Join Geometry.002"
			
			#node Resample Curve
			resample_curve_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeResampleCurve")
			resample_curve_1.name = "Resample Curve"
			resample_curve_1.mode = 'EVALUATED'
			#Selection
			resample_curve_1.inputs[1].default_value = True
			
			#node Set Spline Resolution
			set_spline_resolution_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSetSplineResolution")
			set_spline_resolution_1.name = "Set Spline Resolution"
			#Selection
			set_spline_resolution_1.inputs[1].default_value = True
			
			#node Endpoint Selection.004
			endpoint_selection_004_2 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_004_2.name = "Endpoint Selection.004"
			#Start Size
			endpoint_selection_004_2.inputs[0].default_value = 1
			#End Size
			endpoint_selection_004_2.inputs[1].default_value = 0
			
			#node Group.011
			group_011_2 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_011_2.name = "Group.011"
			group_011_2.node_tree = _mn_cartoon_smooth_handles
			#Input_1
			group_011_2.inputs[0].default_value = -1.0
			
			#node Endpoint Selection.006
			endpoint_selection_006_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_006_1.name = "Endpoint Selection.006"
			#Start Size
			endpoint_selection_006_1.inputs[0].default_value = 1
			#End Size
			endpoint_selection_006_1.inputs[1].default_value = 0
			
			#node Group.014
			group_014_2 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_014_2.name = "Group.014"
			group_014_2.node_tree = _mn_cartoon_smooth_handles
			#Input_1
			group_014_2.inputs[0].default_value = -1.7000000476837158
			
			#node Endpoint Selection.005
			endpoint_selection_005 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_005.name = "Endpoint Selection.005"
			#Start Size
			endpoint_selection_005.inputs[0].default_value = 0
			#End Size
			endpoint_selection_005.inputs[1].default_value = 1
			
			#node Endpoint Selection.007
			endpoint_selection_007 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_007.name = "Endpoint Selection.007"
			#Start Size
			endpoint_selection_007.inputs[0].default_value = 0
			#End Size
			endpoint_selection_007.inputs[1].default_value = 1
			
			#node Group.007
			group_007 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_007.name = "Group.007"
			group_007.node_tree = _mn_cartoon_smooth_handles
			#Input_1
			group_007.inputs[0].default_value = 1.0
			
			#node Group.020
			group_020 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_020.name = "Group.020"
			group_020.node_tree = _mn_cartoon_smooth_handles
			#Input_1
			group_020.inputs[0].default_value = 0.699999988079071
			
			#node Endpoint Selection.008
			endpoint_selection_008_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_008_1.name = "Endpoint Selection.008"
			#Start Size
			endpoint_selection_008_1.inputs[0].default_value = 1
			#End Size
			endpoint_selection_008_1.inputs[1].default_value = 0
			
			#node Group.022
			group_022_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_022_1.name = "Group.022"
			group_022_1.node_tree = _mn_cartoon_smooth_handles
			#Input_1
			group_022_1.inputs[0].default_value = -1.0
			
			#node Endpoint Selection.009
			endpoint_selection_009_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_009_1.name = "Endpoint Selection.009"
			#Start Size
			endpoint_selection_009_1.inputs[0].default_value = 1
			#End Size
			endpoint_selection_009_1.inputs[1].default_value = 0
			
			#node Endpoint Selection.010
			endpoint_selection_010_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_010_1.name = "Endpoint Selection.010"
			#Start Size
			endpoint_selection_010_1.inputs[0].default_value = 0
			#End Size
			endpoint_selection_010_1.inputs[1].default_value = 1
			
			#node Endpoint Selection.011
			endpoint_selection_011 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_011.name = "Endpoint Selection.011"
			#Start Size
			endpoint_selection_011.inputs[0].default_value = 0
			#End Size
			endpoint_selection_011.inputs[1].default_value = 1
			
			#node Group.024
			group_024_2 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_024_2.name = "Group.024"
			group_024_2.node_tree = _mn_cartoon_smooth_handles
			#Input_1
			group_024_2.inputs[0].default_value = 1.0
			
			#node Group.025
			group_025_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_025_1.name = "Group.025"
			group_025_1.node_tree = _mn_cartoon_smooth_handles
			#Input_1
			group_025_1.inputs[0].default_value = 0.699999988079071
			
			#node Set Handle Type.001
			set_handle_type_001 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCurveSetHandles")
			set_handle_type_001.name = "Set Handle Type.001"
			set_handle_type_001.handle_type = 'AUTO'
			set_handle_type_001.mode = {'LEFT', 'RIGHT'}
			#Selection
			set_handle_type_001.inputs[1].default_value = True
			
			#node Vector Math
			vector_math_6 = _mn_utils_style_cartoon.nodes.new("ShaderNodeVectorMath")
			vector_math_6.name = "Vector Math"
			vector_math_6.operation = 'MULTIPLY'
			
			#node Reroute.001
			reroute_001_12 = _mn_utils_style_cartoon.nodes.new("NodeReroute")
			reroute_001_12.name = "Reroute.001"
			#node Reroute.013
			reroute_013_1 = _mn_utils_style_cartoon.nodes.new("NodeReroute")
			reroute_013_1.name = "Reroute.013"
			#node Boolean Math.007
			boolean_math_007_1 = _mn_utils_style_cartoon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_007_1.name = "Boolean Math.007"
			boolean_math_007_1.operation = 'NOT'
			
			#node Group.012
			group_012_2 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_012_2.name = "Group.012"
			group_012_2.node_tree = _field_offset_bool
			#Input_1
			group_012_2.inputs[1].default_value = -1
			
			#node Boolean Math.006
			boolean_math_006_1 = _mn_utils_style_cartoon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_006_1.name = "Boolean Math.006"
			boolean_math_006_1.operation = 'AND'
			
			#node Reroute.005
			reroute_005_2 = _mn_utils_style_cartoon.nodes.new("NodeReroute")
			reroute_005_2.name = "Reroute.005"
			#node Group.013
			group_013_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_013_1.name = "Group.013"
			group_013_1.node_tree = _field_offset_bool
			#Input_1
			group_013_1.inputs[1].default_value = 1
			
			#node Combine XYZ.001
			combine_xyz_001_1 = _mn_utils_style_cartoon.nodes.new("ShaderNodeCombineXYZ")
			combine_xyz_001_1.name = "Combine XYZ.001"
			#X
			combine_xyz_001_1.inputs[0].default_value = 1.0
			
			#node Combine XYZ
			combine_xyz_1 = _mn_utils_style_cartoon.nodes.new("ShaderNodeCombineXYZ")
			combine_xyz_1.name = "Combine XYZ"
			#X
			combine_xyz_1.inputs[0].default_value = 1.0
			
			#node Math.002
			math_002_2 = _mn_utils_style_cartoon.nodes.new("ShaderNodeMath")
			math_002_2.name = "Math.002"
			math_002_2.operation = 'MULTIPLY'
			math_002_2.use_clamp = False
			#Value_001
			math_002_2.inputs[1].default_value = 1.100000023841858
			
			#node Math
			math_12 = _mn_utils_style_cartoon.nodes.new("ShaderNodeMath")
			math_12.name = "Math"
			math_12.operation = 'MULTIPLY'
			math_12.use_clamp = False
			#Value_001
			math_12.inputs[1].default_value = 0.5
			
			#node Capture Attribute
			capture_attribute_3 = _mn_utils_style_cartoon.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute_3.name = "Capture Attribute"
			capture_attribute_3.active_index = 0
			capture_attribute_3.capture_items.clear()
			capture_attribute_3.capture_items.new('FLOAT', "Value")
			capture_attribute_3.capture_items["Value"].data_type = 'FLOAT_VECTOR'
			capture_attribute_3.domain = 'POINT'
			
			#node Group.021
			group_021_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_021_1.name = "Group.021"
			group_021_1.node_tree = _cartoon_arrows_scale
			#Input_2
			group_021_1.inputs[0].default_value = 0.75
			#Input_3
			group_021_1.inputs[1].default_value = 3.0
			#Input_4
			group_021_1.inputs[2].default_value = 3.0
			
			#node Switch.004
			switch_004 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSwitch")
			switch_004.name = "Switch.004"
			switch_004.input_type = 'FLOAT'
			#False
			switch_004.inputs[1].default_value = 1.0
			
			#node Switch.002
			switch_002_2 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSwitch")
			switch_002_2.name = "Switch.002"
			switch_002_2.input_type = 'VECTOR'
			#Switch
			switch_002_2.inputs[0].default_value = False
			#True
			switch_002_2.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Boolean Math.009
			boolean_math_009_1 = _mn_utils_style_cartoon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_009_1.name = "Boolean Math.009"
			boolean_math_009_1.operation = 'AND'
			
			#node Boolean Math.008
			boolean_math_008_1 = _mn_utils_style_cartoon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_008_1.name = "Boolean Math.008"
			boolean_math_008_1.operation = 'NOT'
			
			#node Math.009
			math_009 = _mn_utils_style_cartoon.nodes.new("ShaderNodeMath")
			math_009.name = "Math.009"
			math_009.operation = 'MULTIPLY'
			math_009.use_clamp = False
			
			#node Switch.005
			switch_005_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSwitch")
			switch_005_1.name = "Switch.005"
			switch_005_1.input_type = 'FLOAT'
			#False
			switch_005_1.inputs[1].default_value = 1.0
			
			#node Math.010
			math_010 = _mn_utils_style_cartoon.nodes.new("ShaderNodeMath")
			math_010.name = "Math.010"
			math_010.operation = 'MULTIPLY'
			math_010.use_clamp = False
			
			#node Separate Geometry
			separate_geometry_8 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_8.name = "Separate Geometry"
			separate_geometry_8.domain = 'CURVE'
			
			#node Boolean Math
			boolean_math_13 = _mn_utils_style_cartoon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_13.name = "Boolean Math"
			boolean_math_13.hide = True
			boolean_math_13.operation = 'NOT'
			
			#node Boolean Math.005
			boolean_math_005_2 = _mn_utils_style_cartoon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_005_2.name = "Boolean Math.005"
			boolean_math_005_2.hide = True
			boolean_math_005_2.operation = 'AND'
			
			#node Group Input.008
			group_input_008 = _mn_utils_style_cartoon.nodes.new("NodeGroupInput")
			group_input_008.name = "Group Input.008"
			group_input_008.outputs[0].hide = True
			group_input_008.outputs[1].hide = True
			group_input_008.outputs[2].hide = True
			group_input_008.outputs[3].hide = True
			group_input_008.outputs[4].hide = True
			group_input_008.outputs[8].hide = True
			group_input_008.outputs[9].hide = True
			group_input_008.outputs[10].hide = True
			group_input_008.outputs[11].hide = True
			group_input_008.outputs[12].hide = True
			group_input_008.outputs[13].hide = True
			group_input_008.outputs[14].hide = True
			group_input_008.outputs[15].hide = True
			group_input_008.outputs[16].hide = True
			group_input_008.outputs[17].hide = True
			group_input_008.outputs[18].hide = True
			group_input_008.outputs[19].hide = True
			group_input_008.outputs[20].hide = True
			group_input_008.outputs[21].hide = True
			group_input_008.outputs[22].hide = True
			group_input_008.outputs[23].hide = True
			group_input_008.outputs[24].hide = True
			group_input_008.outputs[25].hide = True
			group_input_008.outputs[26].hide = True
			group_input_008.outputs[27].hide = True
			group_input_008.outputs[28].hide = True
			group_input_008.outputs[29].hide = True
			group_input_008.outputs[30].hide = True
			
			#node Join Geometry
			join_geometry_2 = _mn_utils_style_cartoon.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_2.name = "Join Geometry"
			join_geometry_2.hide = True
			
			#node Group.003
			group_003_2 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_003_2.name = "Group.003"
			group_003_2.node_tree = _cartoon_arrow_instance
			
			#node Group.023
			group_023_2 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_023_2.name = "Group.023"
			group_023_2.node_tree = _mn_cartoon_smooth_handles
			#Input_1
			group_023_2.inputs[0].default_value = -1.5
			
			#node Group.006
			group_006_2 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_006_2.name = "Group.006"
			group_006_2.node_tree = _cartoon_arrow_primitive
			#Input_0
			group_006_2.inputs[0].default_value = 0.7599999904632568
			
			#node Group.017
			group_017 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_017.name = "Group.017"
			group_017.node_tree = _curve_to_mesh
			#Input_3
			group_017.inputs[3].default_value = True
			
			#node Group Input.012
			group_input_012 = _mn_utils_style_cartoon.nodes.new("NodeGroupInput")
			group_input_012.name = "Group Input.012"
			group_input_012.outputs[0].hide = True
			group_input_012.outputs[1].hide = True
			group_input_012.outputs[2].hide = True
			group_input_012.outputs[3].hide = True
			group_input_012.outputs[4].hide = True
			group_input_012.outputs[5].hide = True
			group_input_012.outputs[6].hide = True
			group_input_012.outputs[7].hide = True
			group_input_012.outputs[8].hide = True
			group_input_012.outputs[9].hide = True
			group_input_012.outputs[10].hide = True
			group_input_012.outputs[11].hide = True
			group_input_012.outputs[12].hide = True
			group_input_012.outputs[13].hide = True
			group_input_012.outputs[14].hide = True
			group_input_012.outputs[15].hide = True
			group_input_012.outputs[17].hide = True
			group_input_012.outputs[18].hide = True
			group_input_012.outputs[19].hide = True
			group_input_012.outputs[20].hide = True
			group_input_012.outputs[21].hide = True
			group_input_012.outputs[22].hide = True
			group_input_012.outputs[23].hide = True
			group_input_012.outputs[24].hide = True
			group_input_012.outputs[25].hide = True
			group_input_012.outputs[26].hide = True
			group_input_012.outputs[27].hide = True
			group_input_012.outputs[28].hide = True
			group_input_012.outputs[29].hide = True
			group_input_012.outputs[30].hide = True
			
			#node Set Position
			set_position_4 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSetPosition")
			set_position_4.name = "Set Position"
			#Offset
			set_position_4.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Group.010
			group_010 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_010.name = "Group.010"
			group_010.node_tree = _field_offset_vec
			#Input_1
			group_010.inputs[1].default_value = 1
			
			#node Position.001
			position_001_5 = _mn_utils_style_cartoon.nodes.new("GeometryNodeInputPosition")
			position_001_5.name = "Position.001"
			
			#node Mix
			mix = _mn_utils_style_cartoon.nodes.new("ShaderNodeMix")
			mix.name = "Mix"
			mix.blend_type = 'MIX'
			mix.clamp_factor = True
			mix.clamp_result = False
			mix.data_type = 'VECTOR'
			mix.factor_mode = 'UNIFORM'
			#Factor_Float
			mix.inputs[0].default_value = 0.8704171180725098
			
			#node Reroute.009
			reroute_009_2 = _mn_utils_style_cartoon.nodes.new("NodeReroute")
			reroute_009_2.name = "Reroute.009"
			#node Reroute.003
			reroute_003_4 = _mn_utils_style_cartoon.nodes.new("NodeReroute")
			reroute_003_4.name = "Reroute.003"
			#node Group Input.011
			group_input_011 = _mn_utils_style_cartoon.nodes.new("NodeGroupInput")
			group_input_011.name = "Group Input.011"
			group_input_011.outputs[0].hide = True
			group_input_011.outputs[1].hide = True
			group_input_011.outputs[2].hide = True
			group_input_011.outputs[3].hide = True
			group_input_011.outputs[4].hide = True
			group_input_011.outputs[5].hide = True
			group_input_011.outputs[8].hide = True
			group_input_011.outputs[9].hide = True
			group_input_011.outputs[13].hide = True
			group_input_011.outputs[14].hide = True
			group_input_011.outputs[15].hide = True
			group_input_011.outputs[17].hide = True
			group_input_011.outputs[18].hide = True
			group_input_011.outputs[19].hide = True
			group_input_011.outputs[20].hide = True
			group_input_011.outputs[21].hide = True
			group_input_011.outputs[22].hide = True
			group_input_011.outputs[23].hide = True
			group_input_011.outputs[24].hide = True
			group_input_011.outputs[25].hide = True
			group_input_011.outputs[26].hide = True
			group_input_011.outputs[27].hide = True
			group_input_011.outputs[28].hide = True
			group_input_011.outputs[29].hide = True
			group_input_011.outputs[30].hide = True
			
			#node Group.026
			group_026_2 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_026_2.name = "Group.026"
			group_026_2.node_tree = _mn_select_sec_struct
			#Socket_1
			group_026_2.inputs[0].default_value = True
			
			#node Group.019
			group_019_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_019_1.name = "Group.019"
			group_019_1.node_tree = _curve_custom_profile
			#Input_13
			group_019_1.inputs[2].default_value = 1.0
			#Input_14
			group_019_1.inputs[3].default_value = 0.7853981852531433
			#Input_3
			group_019_1.inputs[7].default_value = 0.0
			#Input_5
			group_019_1.inputs[8].default_value = 1.0
			#Input_16
			group_019_1.inputs[10].default_value = False
			
			#node Group.015
			group_015 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_015.name = "Group.015"
			group_015.node_tree = mn_units
			#Input_1
			group_015.inputs[0].default_value = 2.200000047683716
			
			#node Store Named Attribute
			store_named_attribute_6 = _mn_utils_style_cartoon.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_6.name = "Store Named Attribute"
			store_named_attribute_6.data_type = 'INT'
			store_named_attribute_6.domain = 'POINT'
			#Selection
			store_named_attribute_6.inputs[1].default_value = True
			#Name
			store_named_attribute_6.inputs[2].default_value = "sec_struct"
			#Value
			store_named_attribute_6.inputs[3].default_value = 3
			
			#node Group.016
			group_016 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_016.name = "Group.016"
			group_016.node_tree = _curve_custom_profile
			#Input_13
			group_016.inputs[2].default_value = 1.0
			#Input_14
			group_016.inputs[3].default_value = 0.7853981852531433
			#Input_3
			group_016.inputs[7].default_value = 0.0
			#Input_5
			group_016.inputs[8].default_value = 0.625
			#Input_16
			group_016.inputs[10].default_value = True
			
			#node Named Attribute
			named_attribute_11 = _mn_utils_style_cartoon.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_11.name = "Named Attribute"
			named_attribute_11.data_type = 'INT'
			#Name
			named_attribute_11.inputs[0].default_value = "idx"
			
			#node Named Attribute.001
			named_attribute_001_7 = _mn_utils_style_cartoon.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001_7.name = "Named Attribute.001"
			named_attribute_001_7.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute_001_7.inputs[0].default_value = "Color"
			
			#node Store Named Attribute.001
			store_named_attribute_001_2 = _mn_utils_style_cartoon.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_001_2.name = "Store Named Attribute.001"
			store_named_attribute_001_2.data_type = 'FLOAT_COLOR'
			store_named_attribute_001_2.domain = 'FACE'
			#Selection
			store_named_attribute_001_2.inputs[1].default_value = True
			#Name
			store_named_attribute_001_2.inputs[2].default_value = "Color"
			
			#node Group Output
			group_output_56 = _mn_utils_style_cartoon.nodes.new("NodeGroupOutput")
			group_output_56.name = "Group Output"
			group_output_56.is_active_output = True
			
			#node Set Material
			set_material_3 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSetMaterial")
			set_material_3.name = "Set Material"
			#Selection
			set_material_3.inputs[1].default_value = True
			
			#node Group Input.003
			group_input_003_2 = _mn_utils_style_cartoon.nodes.new("NodeGroupInput")
			group_input_003_2.name = "Group Input.003"
			group_input_003_2.outputs[0].hide = True
			group_input_003_2.outputs[1].hide = True
			group_input_003_2.outputs[2].hide = True
			group_input_003_2.outputs[3].hide = True
			group_input_003_2.outputs[5].hide = True
			group_input_003_2.outputs[8].hide = True
			group_input_003_2.outputs[9].hide = True
			group_input_003_2.outputs[10].hide = True
			group_input_003_2.outputs[11].hide = True
			group_input_003_2.outputs[12].hide = True
			group_input_003_2.outputs[13].hide = True
			group_input_003_2.outputs[14].hide = True
			group_input_003_2.outputs[15].hide = True
			group_input_003_2.outputs[16].hide = True
			group_input_003_2.outputs[17].hide = True
			group_input_003_2.outputs[18].hide = True
			group_input_003_2.outputs[19].hide = True
			group_input_003_2.outputs[20].hide = True
			group_input_003_2.outputs[21].hide = True
			group_input_003_2.outputs[22].hide = True
			group_input_003_2.outputs[23].hide = True
			group_input_003_2.outputs[24].hide = True
			group_input_003_2.outputs[25].hide = True
			group_input_003_2.outputs[26].hide = True
			group_input_003_2.outputs[27].hide = True
			group_input_003_2.outputs[28].hide = True
			group_input_003_2.outputs[29].hide = True
			group_input_003_2.outputs[30].hide = True
			
			#node Sample Index
			sample_index_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSampleIndex")
			sample_index_1.name = "Sample Index"
			sample_index_1.clamp = False
			sample_index_1.data_type = 'FLOAT_COLOR'
			sample_index_1.domain = 'POINT'
			
			#node Switch.001
			switch_001_3 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSwitch")
			switch_001_3.name = "Switch.001"
			switch_001_3.input_type = 'GEOMETRY'
			
			#node Group.001
			group_001_11 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_001_11.name = "Group.001"
			group_001_11.node_tree = _atoms_to_curves
			
			#node Group Input
			group_input_55 = _mn_utils_style_cartoon.nodes.new("NodeGroupInput")
			group_input_55.name = "Group Input"
			group_input_55.outputs[2].hide = True
			group_input_55.outputs[3].hide = True
			group_input_55.outputs[4].hide = True
			group_input_55.outputs[5].hide = True
			group_input_55.outputs[6].hide = True
			group_input_55.outputs[7].hide = True
			group_input_55.outputs[8].hide = True
			group_input_55.outputs[9].hide = True
			group_input_55.outputs[10].hide = True
			group_input_55.outputs[11].hide = True
			group_input_55.outputs[12].hide = True
			group_input_55.outputs[13].hide = True
			group_input_55.outputs[14].hide = True
			group_input_55.outputs[16].hide = True
			group_input_55.outputs[17].hide = True
			group_input_55.outputs[18].hide = True
			group_input_55.outputs[19].hide = True
			group_input_55.outputs[20].hide = True
			group_input_55.outputs[21].hide = True
			group_input_55.outputs[22].hide = True
			group_input_55.outputs[23].hide = True
			group_input_55.outputs[24].hide = True
			group_input_55.outputs[25].hide = True
			group_input_55.outputs[26].hide = True
			group_input_55.outputs[27].hide = True
			group_input_55.outputs[28].hide = True
			group_input_55.outputs[29].hide = True
			group_input_55.outputs[30].hide = True
			
			#node Group Input.005
			group_input_005_1 = _mn_utils_style_cartoon.nodes.new("NodeGroupInput")
			group_input_005_1.name = "Group Input.005"
			group_input_005_1.outputs[0].hide = True
			group_input_005_1.outputs[1].hide = True
			group_input_005_1.outputs[2].hide = True
			group_input_005_1.outputs[3].hide = True
			group_input_005_1.outputs[4].hide = True
			group_input_005_1.outputs[10].hide = True
			group_input_005_1.outputs[11].hide = True
			group_input_005_1.outputs[12].hide = True
			group_input_005_1.outputs[15].hide = True
			group_input_005_1.outputs[16].hide = True
			group_input_005_1.outputs[17].hide = True
			group_input_005_1.outputs[18].hide = True
			group_input_005_1.outputs[19].hide = True
			group_input_005_1.outputs[20].hide = True
			group_input_005_1.outputs[21].hide = True
			group_input_005_1.outputs[22].hide = True
			group_input_005_1.outputs[23].hide = True
			group_input_005_1.outputs[24].hide = True
			group_input_005_1.outputs[25].hide = True
			group_input_005_1.outputs[26].hide = True
			group_input_005_1.outputs[27].hide = True
			group_input_005_1.outputs[28].hide = True
			group_input_005_1.outputs[29].hide = True
			group_input_005_1.outputs[30].hide = True
			
			#node Group Input.001
			group_input_001_7 = _mn_utils_style_cartoon.nodes.new("NodeGroupInput")
			group_input_001_7.name = "Group Input.001"
			group_input_001_7.outputs[0].hide = True
			group_input_001_7.outputs[1].hide = True
			group_input_001_7.outputs[2].hide = True
			group_input_001_7.outputs[4].hide = True
			group_input_001_7.outputs[5].hide = True
			group_input_001_7.outputs[6].hide = True
			group_input_001_7.outputs[7].hide = True
			group_input_001_7.outputs[8].hide = True
			group_input_001_7.outputs[9].hide = True
			group_input_001_7.outputs[10].hide = True
			group_input_001_7.outputs[11].hide = True
			group_input_001_7.outputs[12].hide = True
			group_input_001_7.outputs[13].hide = True
			group_input_001_7.outputs[14].hide = True
			group_input_001_7.outputs[15].hide = True
			group_input_001_7.outputs[16].hide = True
			group_input_001_7.outputs[17].hide = True
			group_input_001_7.outputs[18].hide = True
			group_input_001_7.outputs[19].hide = True
			group_input_001_7.outputs[20].hide = True
			group_input_001_7.outputs[21].hide = True
			group_input_001_7.outputs[22].hide = True
			group_input_001_7.outputs[23].hide = True
			group_input_001_7.outputs[24].hide = True
			group_input_001_7.outputs[25].hide = True
			group_input_001_7.outputs[26].hide = True
			group_input_001_7.outputs[27].hide = True
			group_input_001_7.outputs[28].hide = True
			group_input_001_7.outputs[29].hide = True
			group_input_001_7.outputs[30].hide = True
			
			#node Remove Named Attribute
			remove_named_attribute_1 = _mn_utils_style_cartoon.nodes.new("GeometryNodeRemoveAttribute")
			remove_named_attribute_1.name = "Remove Named Attribute"
			remove_named_attribute_1.pattern_mode = 'EXACT'
			#Name
			remove_named_attribute_1.inputs[1].default_value = "idx"
			
			#node Set Handle Positions.008
			set_handle_positions_008 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSetCurveHandlePositions")
			set_handle_positions_008.name = "Set Handle Positions.008"
			set_handle_positions_008.mode = 'LEFT'
			#Position
			set_handle_positions_008.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Set Handle Positions.007
			set_handle_positions_007 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSetCurveHandlePositions")
			set_handle_positions_007.name = "Set Handle Positions.007"
			set_handle_positions_007.mode = 'RIGHT'
			#Position
			set_handle_positions_007.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Set Handle Positions.009
			set_handle_positions_009 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSetCurveHandlePositions")
			set_handle_positions_009.name = "Set Handle Positions.009"
			set_handle_positions_009.mode = 'LEFT'
			#Position
			set_handle_positions_009.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Set Handle Positions.010
			set_handle_positions_010 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSetCurveHandlePositions")
			set_handle_positions_010.name = "Set Handle Positions.010"
			set_handle_positions_010.mode = 'RIGHT'
			#Position
			set_handle_positions_010.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Set Handle Positions.003
			set_handle_positions_003 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSetCurveHandlePositions")
			set_handle_positions_003.name = "Set Handle Positions.003"
			set_handle_positions_003.mode = 'RIGHT'
			#Position
			set_handle_positions_003.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Set Handle Positions.005
			set_handle_positions_005 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSetCurveHandlePositions")
			set_handle_positions_005.name = "Set Handle Positions.005"
			set_handle_positions_005.mode = 'LEFT'
			#Position
			set_handle_positions_005.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Set Handle Positions.004
			set_handle_positions_004 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSetCurveHandlePositions")
			set_handle_positions_004.name = "Set Handle Positions.004"
			set_handle_positions_004.mode = 'LEFT'
			#Position
			set_handle_positions_004.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Set Handle Positions.006
			set_handle_positions_006 = _mn_utils_style_cartoon.nodes.new("GeometryNodeSetCurveHandlePositions")
			set_handle_positions_006.name = "Set Handle Positions.006"
			set_handle_positions_006.mode = 'RIGHT'
			#Position
			set_handle_positions_006.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Group.002
			group_002_4 = _mn_utils_style_cartoon.nodes.new("GeometryNodeGroup")
			group_002_4.name = "Group.002"
			group_002_4.node_tree = _mn_cartoon_smooth_handles
			#Input_1
			group_002_4.inputs[0].default_value = 1.0
			
			
			
			#Set parents
			group_input_002_3.parent = frame_006_1
			switch_003.parent = frame_009
			math_004.parent = frame_009
			math_005.parent = frame_009
			spline_length_001.parent = frame_009
			vector_rotate.parent = frame_008_1
			vector.parent = frame_008_1
			vector_math_001_1.parent = frame_008_1
			group_008_1.parent = frame_008_1
			group_018_1.parent = frame_005_1
			boolean_math_003_4.parent = frame_005_1
			boolean_math_001_11.parent = frame_005_1
			group_input_010.parent = frame_005_1
			combine_xyz_002_1.parent = frame_005_1
			reroute_011_1.parent = frame_005_1
			reroute_012_1.parent = frame_005_1
			math_001_9.parent = frame_005_1
			separate_geometry_003_1.parent = frame_005_1
			mesh_to_curve_2.parent = frame_005_1
			set_spline_type_002.parent = frame_005_1
			set_handle_type.parent = frame_005_1
			set_handle_positions_001_1.parent = frame_005_1
			set_handle_positions_002.parent = frame_005_1
			reroute_002_8.parent = frame_005_1
			reroute_008_1.parent = frame_005_1
			endpoint_selection_002_1.parent = frame_005_1
			endpoint_selection_003_1.parent = frame_005_1
			group_input_004_1.parent = frame_005_1
			position_4.parent = frame_007_1
			group_033.parent = frame_007_1
			group_004_2.parent = frame_007_1
			endpoint_selection_1.parent = frame_003_2
			group_005_2.parent = frame_003_2
			set_spline_resolution_001.parent = frame_003_2
			group_032.parent = frame_003_2
			group_input_006.parent = frame_003_2
			group_029_1.parent = frame_003_2
			set_handle_type_003.parent = frame_003_2
			set_spline_type_001_1.parent = frame_003_2
			group_030_1.parent = frame_003_2
			group_028_1.parent = frame_003_2
			set_spline_type_003.parent = frame_004_1
			group_009_2.parent = frame_004_1
			join_geometry_002_1.parent = frame_004_1
			resample_curve_1.parent = frame_004_1
			set_spline_resolution_1.parent = frame_004_1
			endpoint_selection_004_2.parent = frame_003_2
			group_011_2.parent = frame_003_2
			endpoint_selection_006_1.parent = frame_003_2
			group_014_2.parent = frame_003_2
			endpoint_selection_005.parent = frame_003_2
			endpoint_selection_007.parent = frame_003_2
			group_007.parent = frame_003_2
			group_020.parent = frame_003_2
			endpoint_selection_008_1.parent = frame_004_1
			group_022_1.parent = frame_004_1
			endpoint_selection_009_1.parent = frame_004_1
			endpoint_selection_010_1.parent = frame_004_1
			endpoint_selection_011.parent = frame_004_1
			group_024_2.parent = frame_004_1
			group_025_1.parent = frame_004_1
			set_handle_type_001.parent = frame_004_1
			vector_math_6.parent = frame_004_1
			reroute_001_12.parent = frame_004_1
			reroute_013_1.parent = frame_004_1
			boolean_math_007_1.parent = frame_004_1
			group_012_2.parent = frame_004_1
			boolean_math_006_1.parent = frame_004_1
			reroute_005_2.parent = frame_004_1
			group_013_1.parent = frame_004_1
			combine_xyz_001_1.parent = frame_004_1
			combine_xyz_1.parent = frame_004_1
			math_002_2.parent = frame_004_1
			math_12.parent = frame_004_1
			capture_attribute_3.parent = frame_004_1
			group_021_1.parent = frame_004_1
			switch_004.parent = frame_004_1
			switch_002_2.parent = frame_004_1
			boolean_math_009_1.parent = frame_004_1
			boolean_math_008_1.parent = frame_004_1
			math_009.parent = frame_004_1
			switch_005_1.parent = frame_004_1
			math_010.parent = frame_004_1
			separate_geometry_8.parent = frame_004_1
			boolean_math_13.parent = frame_004_1
			boolean_math_005_2.parent = frame_004_1
			group_input_008.parent = frame_004_1
			join_geometry_2.parent = frame_004_1
			group_003_2.parent = frame_004_1
			group_023_2.parent = frame_004_1
			group_006_2.parent = frame_004_1
			group_input_012.parent = frame_004_1
			set_position_4.parent = frame_004_1
			group_010.parent = frame_004_1
			position_001_5.parent = frame_004_1
			mix.parent = frame_004_1
			reroute_009_2.parent = frame_004_1
			reroute_003_4.parent = frame_004_1
			group_input_011.parent = frame_004_1
			group_019_1.parent = frame_004_1
			group_015.parent = frame_008_1
			store_named_attribute_6.parent = frame_003_2
			group_016.parent = frame_005_1
			group_input_005_1.parent = frame_004_1
			set_handle_positions_008.parent = frame_004_1
			set_handle_positions_007.parent = frame_004_1
			set_handle_positions_009.parent = frame_004_1
			set_handle_positions_010.parent = frame_004_1
			set_handle_positions_003.parent = frame_003_2
			set_handle_positions_005.parent = frame_003_2
			set_handle_positions_004.parent = frame_003_2
			set_handle_positions_006.parent = frame_003_2
			group_002_4.parent = frame_005_1
			
			#Set locations
			frame_006_1.location = (-1366.132568359375, 289.572265625)
			frame_009.location = (-2332.05859375, 1913.763916015625)
			frame_008_1.location = (-2354.582275390625, 2424.24951171875)
			frame_005_1.location = (-15.40618896484375, -250.0697021484375)
			frame_007_1.location = (394.45556640625, 400.14013671875)
			frame_003_2.location = (-317.85302734375, -1007.8157958984375)
			frame_004_1.location = (-841.83837890625, -199.314453125)
			set_spline_resolution_002.location = (-2100.099609375, 2721.916259765625)
			reroute_006_1.location = (-2126.0078125, 2486.323486328125)
			boolean_math_016.location = (-3669.412841796875, 2606.323486328125)
			separate_geometry_005.location = (-3489.412841796875, 2806.323486328125)
			group_input_002_3.location = (-2831.1396484375, 2082.99365234375)
			mesh_to_curve_002.location = (-3240.0, 2800.0)
			set_position_004.location = (-2980.0, 2820.0)
			boolean_math_017.location = (-3240.0, 2680.0)
			endpoint_selection_001_2.location = (-3240.0, 2560.0)
			switch_003.location = (-60.0, 380.0)
			math_004.location = (-60.0, 540.0)
			math_005.location = (-220.0, 540.0)
			spline_length_001.location = (-380.0, 540.0)
			vector_rotate.location = (-1040.0, -260.0)
			vector.location = (-1220.0, -260.0)
			vector_math_001_1.location = (-700.0, -280.0)
			reroute_007_2.location = (-6685.658203125, 1880.0)
			group_008_1.location = (-1385.417724609375, -444.24951171875)
			resample_curve_001.location = (-2757.201171875, 2731.029052734375)
			set_handle_type_002.location = (-2260.0, 2720.0)
			set_spline_type.location = (-2420.0, 2720.0)
			group_018_1.location = (-4324.76953125, 1520.286376953125)
			boolean_math_003_4.location = (-4138.7490234375, 1563.5899658203125)
			boolean_math_001_11.location = (-4123.6044921875, 1424.9202880859375)
			group_input_010.location = (-4303.732421875, 1353.47900390625)
			combine_xyz_002_1.location = (-2271.80615234375, 1601.967041015625)
			reroute_011_1.location = (-2291.80615234375, 1441.967041015625)
			reroute_012_1.location = (-2091.80615234375, 1441.967041015625)
			math_001_9.location = (-2271.80615234375, 1641.967041015625)
			join_geometry_001_3.location = (-967.3782958984375, 1480.0)
			separate_geometry_003_1.location = (-4267.439453125, 1743.5623779296875)
			mesh_to_curve_2.location = (-4093.024169921875, 1739.939453125)
			set_spline_type_002.location = (-3933.024169921875, 1739.939453125)
			set_handle_type.location = (-3773.024169921875, 1739.939453125)
			set_handle_positions_001_1.location = (-3402.251953125, 1710.0697021484375)
			set_handle_positions_002.location = (-3242.251953125, 1710.0697021484375)
			reroute_002_8.location = (-3349.703857421875, 1510.0697021484375)
			reroute_008_1.location = (-3189.703857421875, 1510.0697021484375)
			endpoint_selection_002_1.location = (-3329.703857421875, 1830.0697021484375)
			endpoint_selection_003_1.location = (-3169.703857421875, 1830.0697021484375)
			store_named_attribute_002_2.location = (-199.57374572753906, 1612.9656982421875)
			group_input_004_1.location = (-2564.354248046875, 1721.967041015625)
			group_input_007.location = (-760.0, 1440.0)
			boolean_math_004_5.location = (-600.0, 1440.0)
			edge_angle_001.location = (-600.0, 1300.0)
			compare_006_1.location = (-440.0, 1300.0)
			boolean_math_002_9.location = (-440.0, 1440.0)
			realize_instances_3.location = (-780.0, 1500.0)
			position_4.location = (-2360.0, 3040.0)
			group_033.location = (-2360.0, 2960.0)
			group_004_2.location = (-2180.0, 3160.0)
			switch_14.location = (-1522.8076171875, 3373.817138671875)
			reroute_15.location = (-4909.38330078125, 3288.636962890625)
			reroute_004_1.location = (-1140.0, -1640.0)
			endpoint_selection_1.location = (-2020.0, -780.0)
			group_005_2.location = (-1860.0, -780.0)
			set_spline_resolution_001.location = (-1723.6593017578125, -602.0430297851562)
			group_032.location = (-2353.30224609375, -600.0)
			group_input_006.location = (-2630.1416015625, -876.25244140625)
			group_029_1.location = (-2721.81103515625, -737.4035034179688)
			set_handle_type_003.location = (-4045.0, -657.0)
			set_spline_type_001_1.location = (-4205.0, -657.0)
			group_030_1.location = (-1560.0, -600.0)
			group_028_1.location = (-3865.0, -657.0)
			set_spline_type_003.location = (-4116.6328125, 785.1316528320312)
			group_009_2.location = (-2745.187255859375, 416.64630126953125)
			join_geometry_002_1.location = (-2413.2392578125, 776.6463012695312)
			resample_curve_1.location = (-1973.2392578125, 816.6463012695312)
			set_spline_resolution_1.location = (-2219.64794921875, 789.2409057617188)
			endpoint_selection_004_2.location = (-3322.8984375, -487.47149658203125)
			group_011_2.location = (-3322.8984375, -787.4714965820312)
			endpoint_selection_006_1.location = (-3482.8984375, -487.47149658203125)
			group_014_2.location = (-3482.8984375, -787.4714965820312)
			endpoint_selection_005.location = (-3162.8984375, -487.47149658203125)
			endpoint_selection_007.location = (-3002.8984375, -487.47149658203125)
			group_007.location = (-3162.8984375, -787.4714965820312)
			group_020.location = (-3002.8984375, -787.4714965820312)
			endpoint_selection_008_1.location = (-3505.1455078125, 849.3387451171875)
			group_022_1.location = (-3505.1455078125, 549.3387451171875)
			endpoint_selection_009_1.location = (-3665.1455078125, 849.3387451171875)
			endpoint_selection_010_1.location = (-3345.1455078125, 849.3387451171875)
			endpoint_selection_011.location = (-3185.145263671875, 849.3387451171875)
			group_024_2.location = (-3345.1455078125, 549.3387451171875)
			group_025_1.location = (-3185.145263671875, 549.3387451171875)
			set_handle_type_001.location = (-3936.6328125, 785.1316528320312)
			vector_math_6.location = (-2747.376708984375, -14.962554931640625)
			reroute_001_12.location = (-2468.4931640625, 59.305511474609375)
			reroute_013_1.location = (-3578.16162109375, 219.314453125)
			boolean_math_007_1.location = (-3518.16162109375, 359.314453125)
			group_012_2.location = (-3518.16162109375, 239.314453125)
			boolean_math_006_1.location = (-3358.16162109375, 359.314453125)
			reroute_005_2.location = (-2238.16162109375, 199.314453125)
			group_013_1.location = (-3358.16162109375, 199.314453125)
			combine_xyz_001_1.location = (-2738.16162109375, -180.685546875)
			combine_xyz_1.location = (-3158.16162109375, 39.314453125)
			math_002_2.location = (-2938.16162109375, -240.685546875)
			math_12.location = (-2938.16162109375, -400.685546875)
			capture_attribute_3.location = (-1798.16162109375, 819.314453125)
			group_021_1.location = (-4330.72509765625, 217.2227783203125)
			switch_004.location = (-3917.2177734375, 73.55532836914062)
			switch_002_2.location = (-2937.197998046875, -4.88739013671875)
			boolean_math_009_1.location = (-3918.16162109375, -100.685546875)
			boolean_math_008_1.location = (-3918.16162109375, -240.685546875)
			math_009.location = (-3738.16162109375, 79.314453125)
			switch_005_1.location = (-3738.16162109375, -100.685546875)
			math_010.location = (-3558.16162109375, -100.685546875)
			separate_geometry_8.location = (-2773.2392578125, 856.6463012695312)
			boolean_math_13.location = (-2998.16162109375, 619.314453125)
			boolean_math_005_2.location = (-2998.16162109375, 579.314453125)
			group_input_008.location = (-2998.16162109375, 539.314453125)
			join_geometry_2.location = (-806.4035034179688, 692.7628784179688)
			group_003_2.location = (-2425.187255859375, 636.6463012695312)
			group_023_2.location = (-3665.1455078125, 549.3387451171875)
			group_006_2.location = (-2745.187255859375, 556.6463012695312)
			group_017.location = (-1920.0997314453125, 2721.916259765625)
			group_input_012.location = (-2218.16162109375, 659.314453125)
			set_position_4.location = (-1318.16162109375, 859.314453125)
			group_010.location = (-1638.16162109375, 639.314453125)
			position_001_5.location = (-1638.16162109375, 719.314453125)
			mix.location = (-1478.16162109375, 719.314453125)
			reroute_009_2.location = (-1858.16162109375, 339.314453125)
			reroute_003_4.location = (-838.16162109375, 339.314453125)
			group_input_011.location = (-1318.16162109375, 639.314453125)
			group_026_2.location = (-4220.0, 2580.0)
			group_019_1.location = (-1089.0626220703125, 862.9052124023438)
			group_015.location = (-880.0, -400.0)
			store_named_attribute_6.location = (-1382.14697265625, -592.1842041015625)
			group_016.location = (-2121.642822265625, 1829.195556640625)
			named_attribute_11.location = (-620.0, 1680.0)
			named_attribute_001_7.location = (-620.0, 1820.0)
			store_named_attribute_001_2.location = (60.831932067871094, 1781.5216064453125)
			group_output_56.location = (924.4188842773438, 1754.622314453125)
			set_material_3.location = (772.8197021484375, 1751.5650634765625)
			group_input_003_2.location = (612.8197021484375, 1651.5650634765625)
			sample_index_1.location = (-380.0, 1980.0)
			switch_001_3.location = (220.0, 1800.0)
			group_001_11.location = (-7240.0, 1740.0)
			group_input_55.location = (-7460.0, 1540.0)
			group_input_005_1.location = (-4650.06201171875, -62.146148681640625)
			group_input_001_7.location = (220.0, 1880.0)
			remove_named_attribute_1.location = (380.0, 1800.0)
			set_handle_positions_008.location = (-3665.1455078125, 729.3387451171875)
			set_handle_positions_007.location = (-3504.087890625, 735.6434326171875)
			set_handle_positions_009.location = (-3344.087890625, 735.6434326171875)
			set_handle_positions_010.location = (-3185.145263671875, 729.3387451171875)
			set_handle_positions_003.location = (-3321.84130859375, -601.1668090820312)
			set_handle_positions_005.location = (-3482.8984375, -607.4714965820312)
			set_handle_positions_004.location = (-3161.84130859375, -601.1668090820312)
			set_handle_positions_006.location = (-3002.8984375, -607.4714965820312)
			group_002_4.location = (-3713.108642578125, 1510.0697021484375)
			
			#Set dimensions
			frame_006_1.width, frame_006_1.height = 200.0, 254.0
			frame_009.width, frame_009.height = 520.0, 374.0
			frame_008_1.width, frame_008_1.height = 885.5, 352.0
			frame_005_1.width, frame_005_1.height = 2507.548095703125, 642.5
			frame_007_1.width, frame_007_1.height = 380.0, 376.0
			frame_003_2.width, frame_003_2.height = 3023.0, 598.5
			frame_004_1.width, frame_004_1.height = 4044.0, 1482.5
			set_spline_resolution_002.width, set_spline_resolution_002.height = 140.0, 100.0
			reroute_006_1.width, reroute_006_1.height = 16.0, 100.0
			boolean_math_016.width, boolean_math_016.height = 140.0, 100.0
			separate_geometry_005.width, separate_geometry_005.height = 203.40496826171875, 100.0
			group_input_002_3.width, group_input_002_3.height = 140.0, 100.0
			mesh_to_curve_002.width, mesh_to_curve_002.height = 140.0, 100.0
			set_position_004.width, set_position_004.height = 140.0, 100.0
			boolean_math_017.width, boolean_math_017.height = 140.0, 100.0
			endpoint_selection_001_2.width, endpoint_selection_001_2.height = 140.0, 100.0
			switch_003.width, switch_003.height = 140.0, 100.0
			math_004.width, math_004.height = 140.0, 100.0
			math_005.width, math_005.height = 140.0, 100.0
			spline_length_001.width, spline_length_001.height = 140.0, 100.0
			vector_rotate.width, vector_rotate.height = 140.0, 100.0
			vector.width, vector.height = 140.0, 100.0
			vector_math_001_1.width, vector_math_001_1.height = 140.0, 100.0
			reroute_007_2.width, reroute_007_2.height = 16.0, 100.0
			group_008_1.width, group_008_1.height = 326.6707763671875, 100.0
			resample_curve_001.width, resample_curve_001.height = 140.0, 100.0
			set_handle_type_002.width, set_handle_type_002.height = 140.0, 100.0
			set_spline_type.width, set_spline_type.height = 140.0, 100.0
			group_018_1.width, group_018_1.height = 158.9053955078125, 100.0
			boolean_math_003_4.width, boolean_math_003_4.height = 140.0, 100.0
			boolean_math_001_11.width, boolean_math_001_11.height = 140.0, 100.0
			group_input_010.width, group_input_010.height = 140.0, 100.0
			combine_xyz_002_1.width, combine_xyz_002_1.height = 140.0, 100.0
			reroute_011_1.width, reroute_011_1.height = 16.0, 100.0
			reroute_012_1.width, reroute_012_1.height = 16.0, 100.0
			math_001_9.width, math_001_9.height = 140.0, 100.0
			join_geometry_001_3.width, join_geometry_001_3.height = 140.0, 100.0
			separate_geometry_003_1.width, separate_geometry_003_1.height = 140.0, 100.0
			mesh_to_curve_2.width, mesh_to_curve_2.height = 140.0, 100.0
			set_spline_type_002.width, set_spline_type_002.height = 140.0, 100.0
			set_handle_type.width, set_handle_type.height = 140.0, 100.0
			set_handle_positions_001_1.width, set_handle_positions_001_1.height = 140.0, 100.0
			set_handle_positions_002.width, set_handle_positions_002.height = 140.0, 100.0
			reroute_002_8.width, reroute_002_8.height = 16.0, 100.0
			reroute_008_1.width, reroute_008_1.height = 16.0, 100.0
			endpoint_selection_002_1.width, endpoint_selection_002_1.height = 140.0, 100.0
			endpoint_selection_003_1.width, endpoint_selection_003_1.height = 140.0, 100.0
			store_named_attribute_002_2.width, store_named_attribute_002_2.height = 176.01080322265625, 100.0
			group_input_004_1.width, group_input_004_1.height = 140.0, 100.0
			group_input_007.width, group_input_007.height = 140.0, 100.0
			boolean_math_004_5.width, boolean_math_004_5.height = 140.0, 100.0
			edge_angle_001.width, edge_angle_001.height = 140.0, 100.0
			compare_006_1.width, compare_006_1.height = 140.0, 100.0
			boolean_math_002_9.width, boolean_math_002_9.height = 140.0, 100.0
			realize_instances_3.width, realize_instances_3.height = 140.0, 100.0
			position_4.width, position_4.height = 140.0, 100.0
			group_033.width, group_033.height = 140.0, 100.0
			group_004_2.width, group_004_2.height = 140.0, 100.0
			switch_14.width, switch_14.height = 140.0, 100.0
			reroute_15.width, reroute_15.height = 16.0, 100.0
			reroute_004_1.width, reroute_004_1.height = 16.0, 100.0
			endpoint_selection_1.width, endpoint_selection_1.height = 140.0, 100.0
			group_005_2.width, group_005_2.height = 227.437255859375, 100.0
			set_spline_resolution_001.width, set_spline_resolution_001.height = 140.0, 100.0
			group_032.width, group_032.height = 329.30224609375, 100.0
			group_input_006.width, group_input_006.height = 140.0, 100.0
			group_029_1.width, group_029_1.height = 253.837646484375, 100.0
			set_handle_type_003.width, set_handle_type_003.height = 140.0, 100.0
			set_spline_type_001_1.width, set_spline_type_001_1.height = 140.0, 100.0
			group_030_1.width, group_030_1.height = 140.0, 100.0
			group_028_1.width, group_028_1.height = 312.298828125, 100.0
			set_spline_type_003.width, set_spline_type_003.height = 140.0, 100.0
			group_009_2.width, group_009_2.height = 205.1739501953125, 100.0
			join_geometry_002_1.width, join_geometry_002_1.height = 140.0, 100.0
			resample_curve_1.width, resample_curve_1.height = 140.0, 100.0
			set_spline_resolution_1.width, set_spline_resolution_1.height = 140.0, 100.0
			endpoint_selection_004_2.width, endpoint_selection_004_2.height = 140.0, 100.0
			group_011_2.width, group_011_2.height = 140.0, 100.0
			endpoint_selection_006_1.width, endpoint_selection_006_1.height = 140.0, 100.0
			group_014_2.width, group_014_2.height = 140.0, 100.0
			endpoint_selection_005.width, endpoint_selection_005.height = 140.0, 100.0
			endpoint_selection_007.width, endpoint_selection_007.height = 140.0, 100.0
			group_007.width, group_007.height = 140.0, 100.0
			group_020.width, group_020.height = 140.0, 100.0
			endpoint_selection_008_1.width, endpoint_selection_008_1.height = 140.0, 100.0
			group_022_1.width, group_022_1.height = 140.0, 100.0
			endpoint_selection_009_1.width, endpoint_selection_009_1.height = 140.0, 100.0
			endpoint_selection_010_1.width, endpoint_selection_010_1.height = 140.0, 100.0
			endpoint_selection_011.width, endpoint_selection_011.height = 140.0, 100.0
			group_024_2.width, group_024_2.height = 140.0, 100.0
			group_025_1.width, group_025_1.height = 140.0, 100.0
			set_handle_type_001.width, set_handle_type_001.height = 140.0, 100.0
			vector_math_6.width, vector_math_6.height = 140.0, 100.0
			reroute_001_12.width, reroute_001_12.height = 16.0, 100.0
			reroute_013_1.width, reroute_013_1.height = 16.0, 100.0
			boolean_math_007_1.width, boolean_math_007_1.height = 140.0, 100.0
			group_012_2.width, group_012_2.height = 140.0, 100.0
			boolean_math_006_1.width, boolean_math_006_1.height = 140.0, 100.0
			reroute_005_2.width, reroute_005_2.height = 16.0, 100.0
			group_013_1.width, group_013_1.height = 140.0, 100.0
			combine_xyz_001_1.width, combine_xyz_001_1.height = 140.0, 100.0
			combine_xyz_1.width, combine_xyz_1.height = 140.0, 100.0
			math_002_2.width, math_002_2.height = 140.0, 100.0
			math_12.width, math_12.height = 140.0, 100.0
			capture_attribute_3.width, capture_attribute_3.height = 140.0, 100.0
			group_021_1.width, group_021_1.height = 287.59326171875, 100.0
			switch_004.width, switch_004.height = 140.0, 100.0
			switch_002_2.width, switch_002_2.height = 140.0, 100.0
			boolean_math_009_1.width, boolean_math_009_1.height = 140.0, 100.0
			boolean_math_008_1.width, boolean_math_008_1.height = 140.0, 100.0
			math_009.width, math_009.height = 140.0, 100.0
			switch_005_1.width, switch_005_1.height = 140.0, 100.0
			math_010.width, math_010.height = 140.0, 100.0
			separate_geometry_8.width, separate_geometry_8.height = 140.0, 100.0
			boolean_math_13.width, boolean_math_13.height = 140.0, 100.0
			boolean_math_005_2.width, boolean_math_005_2.height = 140.0, 100.0
			group_input_008.width, group_input_008.height = 140.0, 100.0
			join_geometry_2.width, join_geometry_2.height = 140.0, 100.0
			group_003_2.width, group_003_2.height = 181.6624755859375, 100.0
			group_023_2.width, group_023_2.height = 140.0, 100.0
			group_006_2.width, group_006_2.height = 193.6337890625, 100.0
			group_017.width, group_017.height = 226.826904296875, 100.0
			group_input_012.width, group_input_012.height = 140.0, 100.0
			set_position_4.width, set_position_4.height = 140.0, 100.0
			group_010.width, group_010.height = 140.0, 100.0
			position_001_5.width, position_001_5.height = 140.0, 100.0
			mix.width, mix.height = 140.0, 100.0
			reroute_009_2.width, reroute_009_2.height = 16.0, 100.0
			reroute_003_4.width, reroute_003_4.height = 16.0, 100.0
			group_input_011.width, group_input_011.height = 140.0, 100.0
			group_026_2.width, group_026_2.height = 256.740478515625, 100.0
			group_019_1.width, group_019_1.height = 244.548095703125, 100.0
			group_015.width, group_015.height = 140.0, 100.0
			store_named_attribute_6.width, store_named_attribute_6.height = 140.0, 100.0
			group_016.width, group_016.height = 244.548095703125, 100.0
			named_attribute_11.width, named_attribute_11.height = 140.0, 100.0
			named_attribute_001_7.width, named_attribute_001_7.height = 140.0, 100.0
			store_named_attribute_001_2.width, store_named_attribute_001_2.height = 140.0, 100.0
			group_output_56.width, group_output_56.height = 140.0, 100.0
			set_material_3.width, set_material_3.height = 140.0, 100.0
			group_input_003_2.width, group_input_003_2.height = 140.0, 100.0
			sample_index_1.width, sample_index_1.height = 140.0, 100.0
			switch_001_3.width, switch_001_3.height = 140.0, 100.0
			group_001_11.width, group_001_11.height = 276.27490234375, 100.0
			group_input_55.width, group_input_55.height = 140.0, 100.0
			group_input_005_1.width, group_input_005_1.height = 140.0, 100.0
			group_input_001_7.width, group_input_001_7.height = 140.0, 100.0
			remove_named_attribute_1.width, remove_named_attribute_1.height = 134.0596923828125, 100.0
			set_handle_positions_008.width, set_handle_positions_008.height = 140.0, 100.0
			set_handle_positions_007.width, set_handle_positions_007.height = 140.0, 100.0
			set_handle_positions_009.width, set_handle_positions_009.height = 140.0, 100.0
			set_handle_positions_010.width, set_handle_positions_010.height = 140.0, 100.0
			set_handle_positions_003.width, set_handle_positions_003.height = 140.0, 100.0
			set_handle_positions_005.width, set_handle_positions_005.height = 140.0, 100.0
			set_handle_positions_004.width, set_handle_positions_004.height = 140.0, 100.0
			set_handle_positions_006.width, set_handle_positions_006.height = 140.0, 100.0
			group_002_4.width, group_002_4.height = 323.40478515625, 100.0
			
			#initialize _mn_utils_style_cartoon links
			#reroute_15.Output -> group_004_2.Points
			_mn_utils_style_cartoon.links.new(reroute_15.outputs[0], group_004_2.inputs[0])
			#position_4.Position -> group_004_2.Position
			_mn_utils_style_cartoon.links.new(position_4.outputs[0], group_004_2.inputs[1])
			#endpoint_selection_1.Selection -> group_005_2.Switch
			_mn_utils_style_cartoon.links.new(endpoint_selection_1.outputs[0], group_005_2.inputs[0])
			#group_input_004_1.Profile Curve -> group_016.Instance
			_mn_utils_style_cartoon.links.new(group_input_004_1.outputs[10], group_016.inputs[4])
			#reroute_007_2.Output -> separate_geometry_003_1.Geometry
			_mn_utils_style_cartoon.links.new(reroute_007_2.outputs[0], separate_geometry_003_1.inputs[0])
			#set_handle_positions_002.Curve -> group_016.Curve
			_mn_utils_style_cartoon.links.new(set_handle_positions_002.outputs[0], group_016.inputs[0])
			#set_spline_resolution_001.Geometry -> group_030_1.Curve
			_mn_utils_style_cartoon.links.new(set_spline_resolution_001.outputs[0], group_030_1.inputs[0])
			#group_032.Curve -> set_spline_resolution_001.Geometry
			_mn_utils_style_cartoon.links.new(group_032.outputs[0], set_spline_resolution_001.inputs[0])
			#set_handle_type_003.Curve -> group_028_1.Geometry
			_mn_utils_style_cartoon.links.new(set_handle_type_003.outputs[0], group_028_1.inputs[0])
			#group_005_2.Output -> group_030_1.Radius (A)
			_mn_utils_style_cartoon.links.new(group_005_2.outputs[0], group_030_1.inputs[4])
			#reroute_004_1.Output -> join_geometry_001_3.Geometry
			_mn_utils_style_cartoon.links.new(reroute_004_1.outputs[0], join_geometry_001_3.inputs[0])
			#set_material_3.Geometry -> group_output_56.Cartoon Mesh
			_mn_utils_style_cartoon.links.new(set_material_3.outputs[0], group_output_56.inputs[0])
			#group_018_1.Is Helix -> boolean_math_003_4.Boolean
			_mn_utils_style_cartoon.links.new(group_018_1.outputs[0], boolean_math_003_4.inputs[1])
			#boolean_math_001_11.Boolean -> boolean_math_003_4.Boolean
			_mn_utils_style_cartoon.links.new(boolean_math_001_11.outputs[0], boolean_math_003_4.inputs[0])
			#boolean_math_003_4.Boolean -> separate_geometry_003_1.Selection
			_mn_utils_style_cartoon.links.new(boolean_math_003_4.outputs[0], separate_geometry_003_1.inputs[1])
			#group_033.Rotation -> group_004_2.Rotation
			_mn_utils_style_cartoon.links.new(group_033.outputs[0], group_004_2.inputs[3])
			#group_006_2.Geometry -> group_003_2.Instance
			_mn_utils_style_cartoon.links.new(group_006_2.outputs[0], group_003_2.inputs[1])
			#group_003_2.Trimmed Curve -> join_geometry_002_1.Geometry
			_mn_utils_style_cartoon.links.new(group_003_2.outputs[0], join_geometry_002_1.inputs[0])
			#vector_math_6.Vector -> group_003_2.Scale
			_mn_utils_style_cartoon.links.new(vector_math_6.outputs[0], group_003_2.inputs[3])
			#math_002_2.Value -> combine_xyz_001_1.Y
			_mn_utils_style_cartoon.links.new(math_002_2.outputs[0], combine_xyz_001_1.inputs[1])
			#math_12.Value -> combine_xyz_001_1.Z
			_mn_utils_style_cartoon.links.new(math_12.outputs[0], combine_xyz_001_1.inputs[2])
			#group_input_005_1.Arrow Width Scale -> math_12.Value
			_mn_utils_style_cartoon.links.new(group_input_005_1.outputs[9], math_12.inputs[0])
			#group_input_004_1.Helix Rotate -> math_001_9.Value
			_mn_utils_style_cartoon.links.new(group_input_004_1.outputs[22], math_001_9.inputs[0])
			#group_input_004_1.Helix Thickness -> combine_xyz_002_1.Y
			_mn_utils_style_cartoon.links.new(group_input_004_1.outputs[23], combine_xyz_002_1.inputs[1])
			#group_input_004_1.Helix Width -> combine_xyz_002_1.Z
			_mn_utils_style_cartoon.links.new(group_input_004_1.outputs[24], combine_xyz_002_1.inputs[2])
			#combine_xyz_002_1.Vector -> group_016.Scale
			_mn_utils_style_cartoon.links.new(combine_xyz_002_1.outputs[0], group_016.inputs[6])
			#math_001_9.Value -> group_016.Rotation X
			_mn_utils_style_cartoon.links.new(math_001_9.outputs[0], group_016.inputs[5])
			#group_004_2.Instances -> switch_14.True
			_mn_utils_style_cartoon.links.new(group_004_2.outputs[0], switch_14.inputs[2])
			#group_009_2.Rotation -> group_003_2.Rotation
			_mn_utils_style_cartoon.links.new(group_009_2.outputs[0], group_003_2.inputs[2])
			#group_input_003_2.Material -> set_material_3.Material
			_mn_utils_style_cartoon.links.new(group_input_003_2.outputs[4], set_material_3.inputs[2])
			#group_input_006.Loop Subdivisions -> set_spline_resolution_001.Resolution
			_mn_utils_style_cartoon.links.new(group_input_006.outputs[27], set_spline_resolution_001.inputs[2])
			#group_input_006.Loop Radius -> group_005_2.Input
			_mn_utils_style_cartoon.links.new(group_input_006.outputs[28], group_005_2.inputs[1])
			#group_input_006.Loop Resolution -> group_030_1.Resolution
			_mn_utils_style_cartoon.links.new(group_input_006.outputs[29], group_030_1.inputs[2])
			#reroute_007_2.Output -> reroute_15.Input
			_mn_utils_style_cartoon.links.new(reroute_007_2.outputs[0], reroute_15.inputs[0])
			#group_input_004_1.Profile Resolution -> group_016.Profile Resolution
			_mn_utils_style_cartoon.links.new(group_input_004_1.outputs[11], group_016.inputs[1])
			#group_input_005_1.Arrow Thickness Scale -> math_002_2.Value
			_mn_utils_style_cartoon.links.new(group_input_005_1.outputs[8], math_002_2.inputs[0])
			#separate_geometry_8.Inverted -> group_003_2.Curve
			_mn_utils_style_cartoon.links.new(separate_geometry_8.outputs[1], group_003_2.inputs[0])
			#reroute_003_4.Output -> join_geometry_2.Geometry
			_mn_utils_style_cartoon.links.new(reroute_003_4.outputs[0], join_geometry_2.inputs[0])
			#reroute_009_2.Output -> reroute_003_4.Input
			_mn_utils_style_cartoon.links.new(reroute_009_2.outputs[0], reroute_003_4.inputs[0])
			#store_named_attribute_6.Geometry -> reroute_004_1.Input
			_mn_utils_style_cartoon.links.new(store_named_attribute_6.outputs[0], reroute_004_1.inputs[0])
			#combine_xyz_001_1.Vector -> vector_math_6.Vector
			_mn_utils_style_cartoon.links.new(combine_xyz_001_1.outputs[0], vector_math_6.inputs[1])
			#group_001_11.Loop Splines -> set_spline_type_001_1.Curve
			_mn_utils_style_cartoon.links.new(group_001_11.outputs[6], set_spline_type_001_1.inputs[0])
			#set_handle_type_002.Curve -> set_spline_resolution_002.Geometry
			_mn_utils_style_cartoon.links.new(set_handle_type_002.outputs[0], set_spline_resolution_002.inputs[0])
			#set_position_004.Geometry -> resample_curve_001.Curve
			_mn_utils_style_cartoon.links.new(set_position_004.outputs[0], resample_curve_001.inputs[0])
			#resample_curve_001.Curve -> set_spline_type.Curve
			_mn_utils_style_cartoon.links.new(resample_curve_001.outputs[0], set_spline_type.inputs[0])
			#set_spline_resolution_002.Geometry -> group_017.Curve
			_mn_utils_style_cartoon.links.new(set_spline_resolution_002.outputs[0], group_017.inputs[0])
			#reroute_007_2.Output -> separate_geometry_005.Geometry
			_mn_utils_style_cartoon.links.new(reroute_007_2.outputs[0], separate_geometry_005.inputs[0])
			#reroute_006_1.Output -> set_spline_resolution_002.Resolution
			_mn_utils_style_cartoon.links.new(reroute_006_1.outputs[0], set_spline_resolution_002.inputs[2])
			#math_004.Value -> switch_003.True
			_mn_utils_style_cartoon.links.new(math_004.outputs[0], switch_003.inputs[2])
			#group_input_002_3.Cylinder Curved -> switch_003.Switch
			_mn_utils_style_cartoon.links.new(group_input_002_3.outputs[18], switch_003.inputs[0])
			#spline_length_001.Point Count -> math_005.Value
			_mn_utils_style_cartoon.links.new(spline_length_001.outputs[1], math_005.inputs[0])
			#math_005.Value -> math_004.Value
			_mn_utils_style_cartoon.links.new(math_005.outputs[0], math_004.inputs[0])
			#vector.Vector -> vector_rotate.Vector
			_mn_utils_style_cartoon.links.new(vector.outputs[0], vector_rotate.inputs[0])
			#mesh_to_curve_002.Curve -> set_position_004.Geometry
			_mn_utils_style_cartoon.links.new(mesh_to_curve_002.outputs[0], set_position_004.inputs[0])
			#vector_rotate.Vector -> vector_math_001_1.Vector
			_mn_utils_style_cartoon.links.new(vector_rotate.outputs[0], vector_math_001_1.inputs[0])
			#group_015.Angstrom -> vector_math_001_1.Scale
			_mn_utils_style_cartoon.links.new(group_015.outputs[0], vector_math_001_1.inputs[3])
			#vector_math_001_1.Vector -> set_position_004.Offset
			_mn_utils_style_cartoon.links.new(vector_math_001_1.outputs[0], set_position_004.inputs[3])
			#boolean_math_016.Boolean -> separate_geometry_005.Selection
			_mn_utils_style_cartoon.links.new(boolean_math_016.outputs[0], separate_geometry_005.inputs[1])
			#group_026_2.Is Helix -> boolean_math_016.Boolean
			_mn_utils_style_cartoon.links.new(group_026_2.outputs[0], boolean_math_016.inputs[0])
			#switch_003.Output -> resample_curve_001.Count
			_mn_utils_style_cartoon.links.new(switch_003.outputs[0], resample_curve_001.inputs[2])
			#group_input_002_3.Cylinder Resolution -> group_017.Resolution
			_mn_utils_style_cartoon.links.new(group_input_002_3.outputs[20], group_017.inputs[2])
			#group_input_002_3.Cylinder Radius -> group_017.Radius (A)
			_mn_utils_style_cartoon.links.new(group_input_002_3.outputs[19], group_017.inputs[4])
			#group_input_002_3.Cylinder Subdivisions -> reroute_006_1.Input
			_mn_utils_style_cartoon.links.new(group_input_002_3.outputs[21], reroute_006_1.inputs[0])
			#group_008_1.Rotation -> vector_rotate.Rotation
			_mn_utils_style_cartoon.links.new(group_008_1.outputs[0], vector_rotate.inputs[4])
			#group_input_002_3.As Cylinders -> boolean_math_016.Boolean
			_mn_utils_style_cartoon.links.new(group_input_002_3.outputs[17], boolean_math_016.inputs[1])
			#endpoint_selection_001_2.Selection -> boolean_math_017.Boolean
			_mn_utils_style_cartoon.links.new(endpoint_selection_001_2.outputs[0], boolean_math_017.inputs[0])
			#boolean_math_017.Boolean -> set_position_004.Selection
			_mn_utils_style_cartoon.links.new(boolean_math_017.outputs[0], set_position_004.inputs[1])
			#separate_geometry_005.Selection -> mesh_to_curve_002.Mesh
			_mn_utils_style_cartoon.links.new(separate_geometry_005.outputs[0], mesh_to_curve_002.inputs[0])
			#group_001_11.CA Mesh Line -> reroute_007_2.Input
			_mn_utils_style_cartoon.links.new(group_001_11.outputs[0], reroute_007_2.inputs[0])
			#group_input_55.Atoms -> group_001_11.Atoms
			_mn_utils_style_cartoon.links.new(group_input_55.outputs[0], group_001_11.inputs[0])
			#group_input_55.Selection -> group_001_11.Selection
			_mn_utils_style_cartoon.links.new(group_input_55.outputs[1], group_001_11.inputs[1])
			#set_spline_type_002.Curve -> set_handle_type.Curve
			_mn_utils_style_cartoon.links.new(set_spline_type_002.outputs[0], set_handle_type.inputs[0])
			#set_handle_type.Curve -> set_handle_positions_001_1.Curve
			_mn_utils_style_cartoon.links.new(set_handle_type.outputs[0], set_handle_positions_001_1.inputs[0])
			#endpoint_selection_002_1.Selection -> set_handle_positions_001_1.Selection
			_mn_utils_style_cartoon.links.new(endpoint_selection_002_1.outputs[0], set_handle_positions_001_1.inputs[1])
			#set_handle_positions_001_1.Curve -> set_handle_positions_002.Curve
			_mn_utils_style_cartoon.links.new(set_handle_positions_001_1.outputs[0], set_handle_positions_002.inputs[0])
			#endpoint_selection_003_1.Selection -> set_handle_positions_002.Selection
			_mn_utils_style_cartoon.links.new(endpoint_selection_003_1.outputs[0], set_handle_positions_002.inputs[1])
			#group_input_010.As Cylinders -> boolean_math_001_11.Boolean
			_mn_utils_style_cartoon.links.new(group_input_010.outputs[17], boolean_math_001_11.inputs[0])
			#reroute_002_8.Output -> set_handle_positions_001_1.Offset
			_mn_utils_style_cartoon.links.new(reroute_002_8.outputs[0], set_handle_positions_001_1.inputs[3])
			#reroute_008_1.Output -> set_handle_positions_002.Offset
			_mn_utils_style_cartoon.links.new(reroute_008_1.outputs[0], set_handle_positions_002.inputs[3])
			#group_002_4.Vector -> reroute_002_8.Input
			_mn_utils_style_cartoon.links.new(group_002_4.outputs[0], reroute_002_8.inputs[0])
			#reroute_002_8.Output -> reroute_008_1.Input
			_mn_utils_style_cartoon.links.new(reroute_002_8.outputs[0], reroute_008_1.inputs[0])
			#set_position_4.Geometry -> group_019_1.Curve
			_mn_utils_style_cartoon.links.new(set_position_4.outputs[0], group_019_1.inputs[0])
			#group_input_011.Profile Resolution -> group_019_1.Profile Resolution
			_mn_utils_style_cartoon.links.new(group_input_011.outputs[11], group_019_1.inputs[1])
			#group_input_011.Profile Curve -> group_019_1.Instance
			_mn_utils_style_cartoon.links.new(group_input_011.outputs[10], group_019_1.inputs[4])
			#group_input_011.Sheet Rotate -> group_019_1.Rotation X
			_mn_utils_style_cartoon.links.new(group_input_011.outputs[12], group_019_1.inputs[5])
			#group_003_2.ArrowHeads -> reroute_009_2.Input
			_mn_utils_style_cartoon.links.new(group_003_2.outputs[1], reroute_009_2.inputs[0])
			#reroute_012_1.Output -> group_016.Resolution
			_mn_utils_style_cartoon.links.new(reroute_012_1.outputs[0], group_016.inputs[9])
			#group_input_004_1.Helix Subdivisions -> reroute_011_1.Input
			_mn_utils_style_cartoon.links.new(group_input_004_1.outputs[25], reroute_011_1.inputs[0])
			#reroute_011_1.Output -> reroute_012_1.Input
			_mn_utils_style_cartoon.links.new(reroute_011_1.outputs[0], reroute_012_1.inputs[0])
			#separate_geometry_003_1.Selection -> mesh_to_curve_2.Mesh
			_mn_utils_style_cartoon.links.new(separate_geometry_003_1.outputs[0], mesh_to_curve_2.inputs[0])
			#mesh_to_curve_2.Curve -> set_spline_type_002.Curve
			_mn_utils_style_cartoon.links.new(mesh_to_curve_2.outputs[0], set_spline_type_002.inputs[0])
			#set_spline_type_003.Curve -> set_handle_type_001.Curve
			_mn_utils_style_cartoon.links.new(set_spline_type_003.outputs[0], set_handle_type_001.inputs[0])
			#group_input_011.Sheet Subdivision -> group_019_1.Resolution
			_mn_utils_style_cartoon.links.new(group_input_011.outputs[16], group_019_1.inputs[9])
			#group_001_11.BS Splines -> set_spline_type_003.Curve
			_mn_utils_style_cartoon.links.new(group_001_11.outputs[4], set_spline_type_003.inputs[0])
			#set_spline_type.Curve -> set_handle_type_002.Curve
			_mn_utils_style_cartoon.links.new(set_spline_type.outputs[0], set_handle_type_002.inputs[0])
			#group_input_55.Sheet Smoothing -> group_001_11.BS Smoothing
			_mn_utils_style_cartoon.links.new(group_input_55.outputs[15], group_001_11.inputs[2])
			#set_spline_type_001_1.Curve -> set_handle_type_003.Curve
			_mn_utils_style_cartoon.links.new(set_spline_type_001_1.outputs[0], set_handle_type_003.inputs[0])
			#join_geometry_001_3.Geometry -> realize_instances_3.Geometry
			_mn_utils_style_cartoon.links.new(join_geometry_001_3.outputs[0], realize_instances_3.inputs[0])
			#edge_angle_001.Signed Angle -> compare_006_1.A
			_mn_utils_style_cartoon.links.new(edge_angle_001.outputs[1], compare_006_1.inputs[0])
			#endpoint_selection_004_2.Selection -> set_handle_positions_003.Selection
			_mn_utils_style_cartoon.links.new(endpoint_selection_004_2.outputs[0], set_handle_positions_003.inputs[1])
			#set_handle_positions_003.Curve -> set_handle_positions_004.Curve
			_mn_utils_style_cartoon.links.new(set_handle_positions_003.outputs[0], set_handle_positions_004.inputs[0])
			#endpoint_selection_005.Selection -> set_handle_positions_004.Selection
			_mn_utils_style_cartoon.links.new(endpoint_selection_005.outputs[0], set_handle_positions_004.inputs[1])
			#group_007.Vector -> set_handle_positions_004.Offset
			_mn_utils_style_cartoon.links.new(group_007.outputs[0], set_handle_positions_004.inputs[3])
			#set_handle_positions_006.Curve -> group_032.Curve
			_mn_utils_style_cartoon.links.new(set_handle_positions_006.outputs[0], group_032.inputs[0])
			#realize_instances_3.Geometry -> store_named_attribute_002_2.Geometry
			_mn_utils_style_cartoon.links.new(realize_instances_3.outputs[0], store_named_attribute_002_2.inputs[0])
			#group_input_007.Shade Smooth -> boolean_math_004_5.Boolean
			_mn_utils_style_cartoon.links.new(group_input_007.outputs[2], boolean_math_004_5.inputs[0])
			#boolean_math_004_5.Boolean -> boolean_math_002_9.Boolean
			_mn_utils_style_cartoon.links.new(boolean_math_004_5.outputs[0], boolean_math_002_9.inputs[0])
			#boolean_math_002_9.Boolean -> store_named_attribute_002_2.Value
			_mn_utils_style_cartoon.links.new(boolean_math_002_9.outputs[0], store_named_attribute_002_2.inputs[3])
			#compare_006_1.Result -> boolean_math_002_9.Boolean
			_mn_utils_style_cartoon.links.new(compare_006_1.outputs[0], boolean_math_002_9.inputs[1])
			#capture_attribute_3.Geometry -> set_position_4.Geometry
			_mn_utils_style_cartoon.links.new(capture_attribute_3.outputs[0], set_position_4.inputs[0])
			#position_001_5.Position -> group_010.Field
			_mn_utils_style_cartoon.links.new(position_001_5.outputs[0], group_010.inputs[0])
			#set_spline_resolution_1.Geometry -> resample_curve_1.Curve
			_mn_utils_style_cartoon.links.new(set_spline_resolution_1.outputs[0], resample_curve_1.inputs[0])
			#reroute_013_1.Output -> group_012_2.Boolean
			_mn_utils_style_cartoon.links.new(reroute_013_1.outputs[0], group_012_2.inputs[0])
			#group_012_2.Boolean -> boolean_math_006_1.Boolean
			_mn_utils_style_cartoon.links.new(group_012_2.outputs[0], boolean_math_006_1.inputs[1])
			#reroute_013_1.Output -> boolean_math_007_1.Boolean
			_mn_utils_style_cartoon.links.new(reroute_013_1.outputs[0], boolean_math_007_1.inputs[0])
			#boolean_math_007_1.Boolean -> boolean_math_006_1.Boolean
			_mn_utils_style_cartoon.links.new(boolean_math_007_1.outputs[0], boolean_math_006_1.inputs[0])
			#reroute_005_2.Output -> set_position_4.Selection
			_mn_utils_style_cartoon.links.new(reroute_005_2.outputs[0], set_position_4.inputs[1])
			#boolean_math_006_1.Boolean -> group_013_1.Boolean
			_mn_utils_style_cartoon.links.new(boolean_math_006_1.outputs[0], group_013_1.inputs[0])
			#position_001_5.Position -> mix.A
			_mn_utils_style_cartoon.links.new(position_001_5.outputs[0], mix.inputs[4])
			#group_010.Field -> mix.B
			_mn_utils_style_cartoon.links.new(group_010.outputs[0], mix.inputs[5])
			#mix.Result -> set_position_4.Position
			_mn_utils_style_cartoon.links.new(mix.outputs[1], set_position_4.inputs[2])
			#resample_curve_1.Curve -> capture_attribute_3.Geometry
			_mn_utils_style_cartoon.links.new(resample_curve_1.outputs[0], capture_attribute_3.inputs[0])
			#reroute_001_12.Output -> capture_attribute_3.Value
			_mn_utils_style_cartoon.links.new(reroute_001_12.outputs[0], capture_attribute_3.inputs[1])
			#join_geometry_002_1.Geometry -> set_spline_resolution_1.Geometry
			_mn_utils_style_cartoon.links.new(join_geometry_002_1.outputs[0], set_spline_resolution_1.inputs[0])
			#group_input_005_1.Sheet Width -> math_009.Value
			_mn_utils_style_cartoon.links.new(group_input_005_1.outputs[14], math_009.inputs[1])
			#group_011_2.Vector -> set_handle_positions_003.Offset
			_mn_utils_style_cartoon.links.new(group_011_2.outputs[0], set_handle_positions_003.inputs[3])
			#endpoint_selection_006_1.Selection -> set_handle_positions_005.Selection
			_mn_utils_style_cartoon.links.new(endpoint_selection_006_1.outputs[0], set_handle_positions_005.inputs[1])
			#group_014_2.Vector -> set_handle_positions_005.Offset
			_mn_utils_style_cartoon.links.new(group_014_2.outputs[0], set_handle_positions_005.inputs[3])
			#group_028_1.Geometry -> set_handle_positions_005.Curve
			_mn_utils_style_cartoon.links.new(group_028_1.outputs[0], set_handle_positions_005.inputs[0])
			#set_handle_positions_005.Curve -> set_handle_positions_003.Curve
			_mn_utils_style_cartoon.links.new(set_handle_positions_005.outputs[0], set_handle_positions_003.inputs[0])
			#set_handle_positions_004.Curve -> set_handle_positions_006.Curve
			_mn_utils_style_cartoon.links.new(set_handle_positions_004.outputs[0], set_handle_positions_006.inputs[0])
			#endpoint_selection_007.Selection -> set_handle_positions_006.Selection
			_mn_utils_style_cartoon.links.new(endpoint_selection_007.outputs[0], set_handle_positions_006.inputs[1])
			#group_020.Vector -> set_handle_positions_006.Offset
			_mn_utils_style_cartoon.links.new(group_020.outputs[0], set_handle_positions_006.inputs[3])
			#group_021_1.Result -> reroute_013_1.Input
			_mn_utils_style_cartoon.links.new(group_021_1.outputs[0], reroute_013_1.inputs[0])
			#endpoint_selection_008_1.Selection -> set_handle_positions_007.Selection
			_mn_utils_style_cartoon.links.new(endpoint_selection_008_1.outputs[0], set_handle_positions_007.inputs[1])
			#set_handle_positions_007.Curve -> set_handle_positions_009.Curve
			_mn_utils_style_cartoon.links.new(set_handle_positions_007.outputs[0], set_handle_positions_009.inputs[0])
			#endpoint_selection_010_1.Selection -> set_handle_positions_009.Selection
			_mn_utils_style_cartoon.links.new(endpoint_selection_010_1.outputs[0], set_handle_positions_009.inputs[1])
			#group_024_2.Vector -> set_handle_positions_009.Offset
			_mn_utils_style_cartoon.links.new(group_024_2.outputs[0], set_handle_positions_009.inputs[3])
			#group_022_1.Vector -> set_handle_positions_007.Offset
			_mn_utils_style_cartoon.links.new(group_022_1.outputs[0], set_handle_positions_007.inputs[3])
			#endpoint_selection_009_1.Selection -> set_handle_positions_008.Selection
			_mn_utils_style_cartoon.links.new(endpoint_selection_009_1.outputs[0], set_handle_positions_008.inputs[1])
			#group_023_2.Vector -> set_handle_positions_008.Offset
			_mn_utils_style_cartoon.links.new(group_023_2.outputs[0], set_handle_positions_008.inputs[3])
			#set_handle_positions_008.Curve -> set_handle_positions_007.Curve
			_mn_utils_style_cartoon.links.new(set_handle_positions_008.outputs[0], set_handle_positions_007.inputs[0])
			#set_handle_positions_009.Curve -> set_handle_positions_010.Curve
			_mn_utils_style_cartoon.links.new(set_handle_positions_009.outputs[0], set_handle_positions_010.inputs[0])
			#endpoint_selection_011.Selection -> set_handle_positions_010.Selection
			_mn_utils_style_cartoon.links.new(endpoint_selection_011.outputs[0], set_handle_positions_010.inputs[1])
			#group_025_1.Vector -> set_handle_positions_010.Offset
			_mn_utils_style_cartoon.links.new(group_025_1.outputs[0], set_handle_positions_010.inputs[3])
			#set_handle_type_001.Curve -> set_handle_positions_008.Curve
			_mn_utils_style_cartoon.links.new(set_handle_type_001.outputs[0], set_handle_positions_008.inputs[0])
			#set_handle_positions_010.Curve -> separate_geometry_8.Geometry
			_mn_utils_style_cartoon.links.new(set_handle_positions_010.outputs[0], separate_geometry_8.inputs[0])
			#combine_xyz_1.Vector -> reroute_001_12.Input
			_mn_utils_style_cartoon.links.new(combine_xyz_1.outputs[0], reroute_001_12.inputs[0])
			#capture_attribute_3.Value -> group_019_1.Scale
			_mn_utils_style_cartoon.links.new(capture_attribute_3.outputs[1], group_019_1.inputs[6])
			#math_009.Value -> combine_xyz_1.Z
			_mn_utils_style_cartoon.links.new(math_009.outputs[0], combine_xyz_1.inputs[2])
			#group_013_1.Boolean -> reroute_005_2.Input
			_mn_utils_style_cartoon.links.new(group_013_1.outputs[0], reroute_005_2.inputs[0])
			#switch_002_2.Output -> vector_math_6.Vector
			_mn_utils_style_cartoon.links.new(switch_002_2.outputs[0], vector_math_6.inputs[0])
			#combine_xyz_1.Vector -> switch_002_2.False
			_mn_utils_style_cartoon.links.new(combine_xyz_1.outputs[0], switch_002_2.inputs[1])
			#group_input_008.Arrows Sharp -> boolean_math_005_2.Boolean
			_mn_utils_style_cartoon.links.new(group_input_008.outputs[6], boolean_math_005_2.inputs[1])
			#boolean_math_005_2.Boolean -> boolean_math_13.Boolean
			_mn_utils_style_cartoon.links.new(boolean_math_005_2.outputs[0], boolean_math_13.inputs[0])
			#switch_004.Output -> math_009.Value
			_mn_utils_style_cartoon.links.new(switch_004.outputs[0], math_009.inputs[0])
			#group_021_1.Output -> switch_004.True
			_mn_utils_style_cartoon.links.new(group_021_1.outputs[1], switch_004.inputs[2])
			#group_input_005_1.Arrows Sharp -> boolean_math_008_1.Boolean
			_mn_utils_style_cartoon.links.new(group_input_005_1.outputs[6], boolean_math_008_1.inputs[0])
			#boolean_math_008_1.Boolean -> boolean_math_009_1.Boolean
			_mn_utils_style_cartoon.links.new(boolean_math_008_1.outputs[0], boolean_math_009_1.inputs[1])
			#group_input_005_1.As Arrows -> boolean_math_009_1.Boolean
			_mn_utils_style_cartoon.links.new(group_input_005_1.outputs[5], boolean_math_009_1.inputs[0])
			#boolean_math_009_1.Boolean -> switch_004.Switch
			_mn_utils_style_cartoon.links.new(boolean_math_009_1.outputs[0], switch_004.inputs[0])
			#switch_005_1.Output -> math_010.Value
			_mn_utils_style_cartoon.links.new(switch_005_1.outputs[0], math_010.inputs[0])
			#group_input_005_1.Sheet Thickness -> math_010.Value
			_mn_utils_style_cartoon.links.new(group_input_005_1.outputs[13], math_010.inputs[1])
			#math_010.Value -> combine_xyz_1.Y
			_mn_utils_style_cartoon.links.new(math_010.outputs[0], combine_xyz_1.inputs[1])
			#group_input_005_1.Arrows Point -> switch_005_1.Switch
			_mn_utils_style_cartoon.links.new(group_input_005_1.outputs[7], switch_005_1.inputs[0])
			#switch_004.Output -> switch_005_1.True
			_mn_utils_style_cartoon.links.new(switch_004.outputs[0], switch_005_1.inputs[2])
			#boolean_math_13.Boolean -> separate_geometry_8.Selection
			_mn_utils_style_cartoon.links.new(boolean_math_13.outputs[0], separate_geometry_8.inputs[1])
			#group_input_008.As Arrows -> boolean_math_005_2.Boolean
			_mn_utils_style_cartoon.links.new(group_input_008.outputs[5], boolean_math_005_2.inputs[0])
			#group_input_012.Sheet Subdivision -> set_spline_resolution_1.Resolution
			_mn_utils_style_cartoon.links.new(group_input_012.outputs[16], set_spline_resolution_1.inputs[2])
			#group_030_1.Mesh -> store_named_attribute_6.Geometry
			_mn_utils_style_cartoon.links.new(group_030_1.outputs[0], store_named_attribute_6.inputs[0])
			#named_attribute_11.Attribute -> sample_index_1.Index
			_mn_utils_style_cartoon.links.new(named_attribute_11.outputs[0], sample_index_1.inputs[2])
			#named_attribute_001_7.Attribute -> sample_index_1.Value
			_mn_utils_style_cartoon.links.new(named_attribute_001_7.outputs[0], sample_index_1.inputs[1])
			#reroute_007_2.Output -> sample_index_1.Geometry
			_mn_utils_style_cartoon.links.new(reroute_007_2.outputs[0], sample_index_1.inputs[0])
			#store_named_attribute_002_2.Geometry -> store_named_attribute_001_2.Geometry
			_mn_utils_style_cartoon.links.new(store_named_attribute_002_2.outputs[0], store_named_attribute_001_2.inputs[0])
			#store_named_attribute_002_2.Geometry -> switch_001_3.True
			_mn_utils_style_cartoon.links.new(store_named_attribute_002_2.outputs[0], switch_001_3.inputs[2])
			#store_named_attribute_001_2.Geometry -> switch_001_3.False
			_mn_utils_style_cartoon.links.new(store_named_attribute_001_2.outputs[0], switch_001_3.inputs[1])
			#group_input_001_7.Interpolate Color -> switch_001_3.Switch
			_mn_utils_style_cartoon.links.new(group_input_001_7.outputs[3], switch_001_3.inputs[0])
			#sample_index_1.Value -> store_named_attribute_001_2.Value
			_mn_utils_style_cartoon.links.new(sample_index_1.outputs[0], store_named_attribute_001_2.inputs[3])
			#switch_001_3.Output -> remove_named_attribute_1.Geometry
			_mn_utils_style_cartoon.links.new(switch_001_3.outputs[0], remove_named_attribute_1.inputs[0])
			#remove_named_attribute_1.Geometry -> set_material_3.Geometry
			_mn_utils_style_cartoon.links.new(remove_named_attribute_1.outputs[0], set_material_3.inputs[0])
			#separate_geometry_8.Selection -> join_geometry_002_1.Geometry
			_mn_utils_style_cartoon.links.new(separate_geometry_8.outputs[0], join_geometry_002_1.inputs[0])
			#group_016.Geometry -> join_geometry_001_3.Geometry
			_mn_utils_style_cartoon.links.new(group_016.outputs[0], join_geometry_001_3.inputs[0])
			#group_019_1.Geometry -> join_geometry_2.Geometry
			_mn_utils_style_cartoon.links.new(group_019_1.outputs[0], join_geometry_2.inputs[0])
			#join_geometry_2.Geometry -> join_geometry_001_3.Geometry
			_mn_utils_style_cartoon.links.new(join_geometry_2.outputs[0], join_geometry_001_3.inputs[0])
			#group_017.Mesh -> join_geometry_001_3.Geometry
			_mn_utils_style_cartoon.links.new(group_017.outputs[0], join_geometry_001_3.inputs[0])
			#switch_14.Output -> join_geometry_001_3.Geometry
			_mn_utils_style_cartoon.links.new(switch_14.outputs[0], join_geometry_001_3.inputs[0])
			return _mn_utils_style_cartoon

		_mn_utils_style_cartoon = _mn_utils_style_cartoon_node_group()

		#initialize boolean_run_mask node group
		def boolean_run_mask_node_group():
			boolean_run_mask = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Boolean Run Mask")

			boolean_run_mask.color_tag = 'CONVERTER'
			boolean_run_mask.description = ""

			
			#boolean_run_mask interface
			#Socket Boolean
			boolean_socket_4 = boolean_run_mask.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket_4.attribute_domain = 'POINT'
			
			#Socket Boolean
			boolean_socket_5 = boolean_run_mask.interface.new_socket(name = "Boolean", in_out='INPUT', socket_type = 'NodeSocketBool')
			boolean_socket_5.attribute_domain = 'POINT'
			
			#Socket Lag Start
			lag_start_socket = boolean_run_mask.interface.new_socket(name = "Lag Start", in_out='INPUT', socket_type = 'NodeSocketInt')
			lag_start_socket.subtype = 'NONE'
			lag_start_socket.default_value = 0
			lag_start_socket.min_value = 0
			lag_start_socket.max_value = 2147483647
			lag_start_socket.attribute_domain = 'POINT'
			lag_start_socket.description = "The first N values in a run are made to be false"
			
			#Socket Min Length
			min_length_socket = boolean_run_mask.interface.new_socket(name = "Min Length", in_out='INPUT', socket_type = 'NodeSocketInt')
			min_length_socket.subtype = 'NONE'
			min_length_socket.default_value = 0
			min_length_socket.min_value = 0
			min_length_socket.max_value = 2147483647
			min_length_socket.attribute_domain = 'POINT'
			min_length_socket.description = "Run is only valid if it contains at least N values"
			
			#Socket Trim End
			trim_end_socket = boolean_run_mask.interface.new_socket(name = "Trim End", in_out='INPUT', socket_type = 'NodeSocketInt')
			trim_end_socket.subtype = 'NONE'
			trim_end_socket.default_value = 0
			trim_end_socket.min_value = -2147483648
			trim_end_socket.max_value = 2147483647
			trim_end_socket.attribute_domain = 'POINT'
			
			
			#initialize boolean_run_mask nodes
			#node Group Output
			group_output_57 = boolean_run_mask.nodes.new("NodeGroupOutput")
			group_output_57.name = "Group Output"
			group_output_57.is_active_output = True
			
			#node Group Input
			group_input_56 = boolean_run_mask.nodes.new("NodeGroupInput")
			group_input_56.name = "Group Input"
			group_input_56.outputs[3].hide = True
			
			#node Accumulate Field
			accumulate_field_3 = boolean_run_mask.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_3.name = "Accumulate Field"
			accumulate_field_3.data_type = 'INT'
			accumulate_field_3.domain = 'POINT'
			#Group Index
			accumulate_field_3.inputs[1].default_value = 0
			
			#node Boolean Math.001
			boolean_math_001_12 = boolean_run_mask.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_12.name = "Boolean Math.001"
			boolean_math_001_12.operation = 'NOT'
			
			#node Accumulate Field.001
			accumulate_field_001_3 = boolean_run_mask.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_001_3.name = "Accumulate Field.001"
			accumulate_field_001_3.data_type = 'INT'
			accumulate_field_001_3.domain = 'POINT'
			#Value
			accumulate_field_001_3.inputs[0].default_value = 1
			
			#node Compare
			compare_12 = boolean_run_mask.nodes.new("FunctionNodeCompare")
			compare_12.name = "Compare"
			compare_12.data_type = 'INT'
			compare_12.mode = 'ELEMENT'
			compare_12.operation = 'GREATER_THAN'
			
			#node Boolean Math.002
			boolean_math_002_10 = boolean_run_mask.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_10.name = "Boolean Math.002"
			boolean_math_002_10.operation = 'AND'
			
			#node Reroute
			reroute_16 = boolean_run_mask.nodes.new("NodeReroute")
			reroute_16.name = "Reroute"
			#node Boolean Math.003
			boolean_math_003_5 = boolean_run_mask.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003_5.name = "Boolean Math.003"
			boolean_math_003_5.operation = 'AND'
			
			#node Compare.001
			compare_001_6 = boolean_run_mask.nodes.new("FunctionNodeCompare")
			compare_001_6.name = "Compare.001"
			compare_001_6.data_type = 'INT'
			compare_001_6.mode = 'ELEMENT'
			compare_001_6.operation = 'GREATER_THAN'
			
			#node Boolean Math.004
			boolean_math_004_6 = boolean_run_mask.nodes.new("FunctionNodeBooleanMath")
			boolean_math_004_6.name = "Boolean Math.004"
			boolean_math_004_6.operation = 'AND'
			
			#node Compare.002
			compare_002_3 = boolean_run_mask.nodes.new("FunctionNodeCompare")
			compare_002_3.name = "Compare.002"
			compare_002_3.data_type = 'INT'
			compare_002_3.mode = 'ELEMENT'
			compare_002_3.operation = 'GREATER_THAN'
			
			#node Math
			math_13 = boolean_run_mask.nodes.new("ShaderNodeMath")
			math_13.name = "Math"
			math_13.operation = 'SUBTRACT'
			math_13.use_clamp = False
			
			#node Group Input.001
			group_input_001_8 = boolean_run_mask.nodes.new("NodeGroupInput")
			group_input_001_8.name = "Group Input.001"
			group_input_001_8.outputs[0].hide = True
			group_input_001_8.outputs[1].hide = True
			group_input_001_8.outputs[2].hide = True
			group_input_001_8.outputs[4].hide = True
			
			
			
			
			#Set locations
			group_output_57.location = (860.0001220703125, 60.0)
			group_input_56.location = (-460.0031433105469, 0.0)
			accumulate_field_3.location = (-100.0, -300.0)
			boolean_math_001_12.location = (-260.0, -300.0)
			accumulate_field_001_3.location = (60.0, -300.0)
			compare_12.location = (260.0031433105469, -80.0)
			boolean_math_002_10.location = (260.0, 60.0)
			reroute_16.location = (-260.0031433105469, -29.36541748046875)
			boolean_math_003_5.location = (420.0, 60.0)
			compare_001_6.location = (420.0, -80.0)
			boolean_math_004_6.location = (580.0, 60.0)
			compare_002_3.location = (580.0, -80.0)
			math_13.location = (420.0, -240.0)
			group_input_001_8.location = (580.0, -240.0)
			
			#Set dimensions
			group_output_57.width, group_output_57.height = 140.0, 100.0
			group_input_56.width, group_input_56.height = 140.0, 100.0
			accumulate_field_3.width, accumulate_field_3.height = 140.0, 100.0
			boolean_math_001_12.width, boolean_math_001_12.height = 140.0, 100.0
			accumulate_field_001_3.width, accumulate_field_001_3.height = 140.0, 100.0
			compare_12.width, compare_12.height = 140.0, 100.0
			boolean_math_002_10.width, boolean_math_002_10.height = 140.0, 100.0
			reroute_16.width, reroute_16.height = 16.0, 100.0
			boolean_math_003_5.width, boolean_math_003_5.height = 140.0, 100.0
			compare_001_6.width, compare_001_6.height = 140.0, 100.0
			boolean_math_004_6.width, boolean_math_004_6.height = 140.0, 100.0
			compare_002_3.width, compare_002_3.height = 140.0, 100.0
			math_13.width, math_13.height = 140.0, 100.0
			group_input_001_8.width, group_input_001_8.height = 140.0, 100.0
			
			#initialize boolean_run_mask links
			#boolean_math_001_12.Boolean -> accumulate_field_3.Value
			boolean_run_mask.links.new(boolean_math_001_12.outputs[0], accumulate_field_3.inputs[0])
			#reroute_16.Output -> boolean_math_001_12.Boolean
			boolean_run_mask.links.new(reroute_16.outputs[0], boolean_math_001_12.inputs[0])
			#compare_12.Result -> boolean_math_002_10.Boolean
			boolean_run_mask.links.new(compare_12.outputs[0], boolean_math_002_10.inputs[1])
			#group_input_56.Boolean -> reroute_16.Input
			boolean_run_mask.links.new(group_input_56.outputs[0], reroute_16.inputs[0])
			#boolean_math_004_6.Boolean -> group_output_57.Boolean
			boolean_run_mask.links.new(boolean_math_004_6.outputs[0], group_output_57.inputs[0])
			#group_input_56.Lag Start -> compare_12.B
			boolean_run_mask.links.new(group_input_56.outputs[1], compare_12.inputs[3])
			#boolean_math_002_10.Boolean -> boolean_math_003_5.Boolean
			boolean_run_mask.links.new(boolean_math_002_10.outputs[0], boolean_math_003_5.inputs[0])
			#accumulate_field_001_3.Total -> compare_001_6.A
			boolean_run_mask.links.new(accumulate_field_001_3.outputs[2], compare_001_6.inputs[2])
			#group_input_56.Min Length -> compare_001_6.B
			boolean_run_mask.links.new(group_input_56.outputs[2], compare_001_6.inputs[3])
			#compare_001_6.Result -> boolean_math_003_5.Boolean
			boolean_run_mask.links.new(compare_001_6.outputs[0], boolean_math_003_5.inputs[1])
			#reroute_16.Output -> boolean_math_002_10.Boolean
			boolean_run_mask.links.new(reroute_16.outputs[0], boolean_math_002_10.inputs[0])
			#accumulate_field_3.Trailing -> accumulate_field_001_3.Group ID
			boolean_run_mask.links.new(accumulate_field_3.outputs[1], accumulate_field_001_3.inputs[1])
			#boolean_math_003_5.Boolean -> boolean_math_004_6.Boolean
			boolean_run_mask.links.new(boolean_math_003_5.outputs[0], boolean_math_004_6.inputs[0])
			#accumulate_field_001_3.Total -> math_13.Value
			boolean_run_mask.links.new(accumulate_field_001_3.outputs[2], math_13.inputs[0])
			#accumulate_field_001_3.Leading -> math_13.Value
			boolean_run_mask.links.new(accumulate_field_001_3.outputs[0], math_13.inputs[1])
			#math_13.Value -> compare_002_3.A
			boolean_run_mask.links.new(math_13.outputs[0], compare_002_3.inputs[2])
			#group_input_001_8.Trim End -> compare_002_3.B
			boolean_run_mask.links.new(group_input_001_8.outputs[3], compare_002_3.inputs[3])
			#compare_002_3.Result -> boolean_math_004_6.Boolean
			boolean_run_mask.links.new(compare_002_3.outputs[0], boolean_math_004_6.inputs[1])
			#accumulate_field_001_3.Leading -> compare_12.A
			boolean_run_mask.links.new(accumulate_field_001_3.outputs[0], compare_12.inputs[2])
			return boolean_run_mask

		boolean_run_mask = boolean_run_mask_node_group()

		#initialize world_to_angstrom node group
		def world_to_angstrom_node_group():
			world_to_angstrom = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "World to Angstrom")

			world_to_angstrom.color_tag = 'NONE'
			world_to_angstrom.description = ""

			
			#world_to_angstrom interface
			#Socket Angstrom
			angstrom_socket_1 = world_to_angstrom.interface.new_socket(name = "Angstrom", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			angstrom_socket_1.subtype = 'NONE'
			angstrom_socket_1.default_value = 0.0
			angstrom_socket_1.min_value = -3.4028234663852886e+38
			angstrom_socket_1.max_value = 3.4028234663852886e+38
			angstrom_socket_1.attribute_domain = 'POINT'
			
			#Socket World
			world_socket = world_to_angstrom.interface.new_socket(name = "World", in_out='INPUT', socket_type = 'NodeSocketFloat')
			world_socket.subtype = 'NONE'
			world_socket.default_value = 0.5
			world_socket.min_value = -10000.0
			world_socket.max_value = 10000.0
			world_socket.attribute_domain = 'POINT'
			
			
			#initialize world_to_angstrom nodes
			#node Group Output
			group_output_58 = world_to_angstrom.nodes.new("NodeGroupOutput")
			group_output_58.name = "Group Output"
			group_output_58.is_active_output = True
			
			#node Group Input
			group_input_57 = world_to_angstrom.nodes.new("NodeGroupInput")
			group_input_57.name = "Group Input"
			
			#node Group
			group_22 = world_to_angstrom.nodes.new("GeometryNodeGroup")
			group_22.name = "Group"
			group_22.node_tree = _mn_world_scale
			
			#node Math
			math_14 = world_to_angstrom.nodes.new("ShaderNodeMath")
			math_14.name = "Math"
			math_14.operation = 'DIVIDE'
			math_14.use_clamp = False
			
			
			
			
			#Set locations
			group_output_58.location = (190.0, 0.0)
			group_input_57.location = (-200.0, 0.0)
			group_22.location = (0.0, -80.0)
			math_14.location = (0.0, 80.0)
			
			#Set dimensions
			group_output_58.width, group_output_58.height = 140.0, 100.0
			group_input_57.width, group_input_57.height = 140.0, 100.0
			group_22.width, group_22.height = 140.0, 100.0
			math_14.width, math_14.height = 140.0, 100.0
			
			#initialize world_to_angstrom links
			#group_22.world_scale -> math_14.Value
			world_to_angstrom.links.new(group_22.outputs[0], math_14.inputs[1])
			#group_input_57.World -> math_14.Value
			world_to_angstrom.links.new(group_input_57.outputs[0], math_14.inputs[0])
			#math_14.Value -> group_output_58.Angstrom
			world_to_angstrom.links.new(math_14.outputs[0], group_output_58.inputs[0])
			return world_to_angstrom

		world_to_angstrom = world_to_angstrom_node_group()

		#initialize nodegroup_001 node group
		def nodegroup_001_node_group():
			nodegroup_001 = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "NodeGroup.001")

			nodegroup_001.color_tag = 'NONE'
			nodegroup_001.description = ""

			
			#nodegroup_001 interface
			#Socket Value
			value_socket_12 = nodegroup_001.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			value_socket_12.subtype = 'NONE'
			value_socket_12.default_value = 0.0
			value_socket_12.min_value = -3.4028234663852886e+38
			value_socket_12.max_value = 3.4028234663852886e+38
			value_socket_12.attribute_domain = 'POINT'
			
			#Socket Vector
			vector_socket_2 = nodegroup_001.interface.new_socket(name = "Vector", in_out='INPUT', socket_type = 'NodeSocketVector')
			vector_socket_2.subtype = 'NONE'
			vector_socket_2.default_value = (0.0, 0.0, 0.0)
			vector_socket_2.min_value = -10000.0
			vector_socket_2.max_value = 10000.0
			vector_socket_2.attribute_domain = 'POINT'
			
			#Socket Vector
			vector_socket_3 = nodegroup_001.interface.new_socket(name = "Vector", in_out='INPUT', socket_type = 'NodeSocketVector')
			vector_socket_3.subtype = 'NONE'
			vector_socket_3.default_value = (0.0, 0.0, 0.0)
			vector_socket_3.min_value = -10000.0
			vector_socket_3.max_value = 10000.0
			vector_socket_3.attribute_domain = 'POINT'
			
			
			#initialize nodegroup_001 nodes
			#node Group Output
			group_output_59 = nodegroup_001.nodes.new("NodeGroupOutput")
			group_output_59.name = "Group Output"
			group_output_59.is_active_output = True
			
			#node Group Input
			group_input_58 = nodegroup_001.nodes.new("NodeGroupInput")
			group_input_58.name = "Group Input"
			
			#node Vector Math.002
			vector_math_002_1 = nodegroup_001.nodes.new("ShaderNodeVectorMath")
			vector_math_002_1.name = "Vector Math.002"
			vector_math_002_1.operation = 'DISTANCE'
			
			#node Math.002
			math_002_3 = nodegroup_001.nodes.new("ShaderNodeMath")
			math_002_3.name = "Math.002"
			math_002_3.operation = 'DIVIDE'
			math_002_3.use_clamp = False
			#Value
			math_002_3.inputs[0].default_value = 1.0
			
			#node Group.001
			group_001_12 = nodegroup_001.nodes.new("GeometryNodeGroup")
			group_001_12.name = "Group.001"
			group_001_12.node_tree = world_to_angstrom
			
			
			
			
			#Set locations
			group_output_59.location = (670.8533325195312, -4.1087493896484375)
			group_input_58.location = (-280.0, 0.0)
			vector_math_002_1.location = (-80.0, 0.0)
			math_002_3.location = (260.0, 0.0)
			group_001_12.location = (80.0, 0.0)
			
			#Set dimensions
			group_output_59.width, group_output_59.height = 140.0, 100.0
			group_input_58.width, group_input_58.height = 140.0, 100.0
			vector_math_002_1.width, vector_math_002_1.height = 140.0, 100.0
			math_002_3.width, math_002_3.height = 140.0, 100.0
			group_001_12.width, group_001_12.height = 152.50686645507812, 100.0
			
			#initialize nodegroup_001 links
			#group_001_12.Angstrom -> math_002_3.Value
			nodegroup_001.links.new(group_001_12.outputs[0], math_002_3.inputs[1])
			#group_input_58.Vector -> vector_math_002_1.Vector
			nodegroup_001.links.new(group_input_58.outputs[1], vector_math_002_1.inputs[1])
			#group_input_58.Vector -> vector_math_002_1.Vector
			nodegroup_001.links.new(group_input_58.outputs[0], vector_math_002_1.inputs[0])
			#math_002_3.Value -> group_output_59.Value
			nodegroup_001.links.new(math_002_3.outputs[0], group_output_59.inputs[0])
			#vector_math_002_1.Value -> group_001_12.World
			nodegroup_001.links.new(vector_math_002_1.outputs[1], group_001_12.inputs[0])
			return nodegroup_001

		nodegroup_001 = nodegroup_001_node_group()

		#initialize hbond_energy node group
		def hbond_energy_node_group():
			hbond_energy = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "HBond Energy")

			hbond_energy.color_tag = 'NONE'
			hbond_energy.description = ""

			
			#hbond_energy interface
			#Socket Is Bonded
			is_bonded_socket = hbond_energy.interface.new_socket(name = "Is Bonded", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_bonded_socket.attribute_domain = 'POINT'
			
			#Socket Bond Energy
			bond_energy_socket = hbond_energy.interface.new_socket(name = "Bond Energy", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			bond_energy_socket.subtype = 'NONE'
			bond_energy_socket.default_value = 0.0
			bond_energy_socket.min_value = -3.4028234663852886e+38
			bond_energy_socket.max_value = 3.4028234663852886e+38
			bond_energy_socket.attribute_domain = 'POINT'
			
			#Socket Bond Vector
			bond_vector_socket = hbond_energy.interface.new_socket(name = "Bond Vector", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			bond_vector_socket.subtype = 'NONE'
			bond_vector_socket.default_value = (0.0, 0.0, 0.0)
			bond_vector_socket.min_value = -3.4028234663852886e+38
			bond_vector_socket.max_value = 3.4028234663852886e+38
			bond_vector_socket.attribute_domain = 'POINT'
			
			#Socket O
			o_socket_1 = hbond_energy.interface.new_socket(name = "O", in_out='INPUT', socket_type = 'NodeSocketVector')
			o_socket_1.subtype = 'NONE'
			o_socket_1.default_value = (0.0, 0.0, 0.0)
			o_socket_1.min_value = -3.4028234663852886e+38
			o_socket_1.max_value = 3.4028234663852886e+38
			o_socket_1.attribute_domain = 'POINT'
			
			#Socket C
			c_socket_1 = hbond_energy.interface.new_socket(name = "C", in_out='INPUT', socket_type = 'NodeSocketVector')
			c_socket_1.subtype = 'NONE'
			c_socket_1.default_value = (0.0, 0.0, 0.0)
			c_socket_1.min_value = -3.4028234663852886e+38
			c_socket_1.max_value = 3.4028234663852886e+38
			c_socket_1.attribute_domain = 'POINT'
			
			#Socket N
			n_socket_1 = hbond_energy.interface.new_socket(name = "N", in_out='INPUT', socket_type = 'NodeSocketVector')
			n_socket_1.subtype = 'NONE'
			n_socket_1.default_value = (0.0, 0.0, 0.0)
			n_socket_1.min_value = -3.4028234663852886e+38
			n_socket_1.max_value = 3.4028234663852886e+38
			n_socket_1.attribute_domain = 'POINT'
			
			#Socket H
			h_socket = hbond_energy.interface.new_socket(name = "H", in_out='INPUT', socket_type = 'NodeSocketVector')
			h_socket.subtype = 'NONE'
			h_socket.default_value = (0.0, 0.0, 0.0)
			h_socket.min_value = -3.4028234663852886e+38
			h_socket.max_value = 3.4028234663852886e+38
			h_socket.attribute_domain = 'POINT'
			
			
			#initialize hbond_energy nodes
			#node Group Output
			group_output_60 = hbond_energy.nodes.new("NodeGroupOutput")
			group_output_60.name = "Group Output"
			group_output_60.is_active_output = True
			
			#node Group Input
			group_input_59 = hbond_energy.nodes.new("NodeGroupInput")
			group_input_59.name = "Group Input"
			
			#node Group.003
			group_003_3 = hbond_energy.nodes.new("GeometryNodeGroup")
			group_003_3.label = "1/r(ON)"
			group_003_3.name = "Group.003"
			group_003_3.node_tree = nodegroup_001
			
			#node Group.008
			group_008_2 = hbond_energy.nodes.new("GeometryNodeGroup")
			group_008_2.label = "1/r(CH)"
			group_008_2.name = "Group.008"
			group_008_2.node_tree = nodegroup_001
			
			#node Group.009
			group_009_3 = hbond_energy.nodes.new("GeometryNodeGroup")
			group_009_3.label = "1/r(OH)"
			group_009_3.name = "Group.009"
			group_009_3.node_tree = nodegroup_001
			
			#node Group.010
			group_010_1 = hbond_energy.nodes.new("GeometryNodeGroup")
			group_010_1.label = "1/r(CN)"
			group_010_1.name = "Group.010"
			group_010_1.node_tree = nodegroup_001
			
			#node Math.002
			math_002_4 = hbond_energy.nodes.new("ShaderNodeMath")
			math_002_4.name = "Math.002"
			math_002_4.hide = True
			math_002_4.operation = 'ADD'
			math_002_4.use_clamp = False
			
			#node Math.003
			math_003_3 = hbond_energy.nodes.new("ShaderNodeMath")
			math_003_3.name = "Math.003"
			math_003_3.hide = True
			math_003_3.operation = 'SUBTRACT'
			math_003_3.use_clamp = False
			
			#node Math.004
			math_004_1 = hbond_energy.nodes.new("ShaderNodeMath")
			math_004_1.name = "Math.004"
			math_004_1.hide = True
			math_004_1.operation = 'SUBTRACT'
			math_004_1.use_clamp = False
			
			#node Math.005
			math_005_1 = hbond_energy.nodes.new("ShaderNodeMath")
			math_005_1.label = "* q1q2"
			math_005_1.name = "Math.005"
			math_005_1.operation = 'MULTIPLY'
			math_005_1.use_clamp = False
			#Value_001
			math_005_1.inputs[1].default_value = 0.08399999886751175
			
			#node Math.006
			math_006_1 = hbond_energy.nodes.new("ShaderNodeMath")
			math_006_1.label = "*f"
			math_006_1.name = "Math.006"
			math_006_1.operation = 'MULTIPLY'
			math_006_1.use_clamp = False
			#Value_001
			math_006_1.inputs[1].default_value = 332.0
			
			#node Vector Math
			vector_math_7 = hbond_energy.nodes.new("ShaderNodeVectorMath")
			vector_math_7.name = "Vector Math"
			vector_math_7.operation = 'SUBTRACT'
			
			#node Math.007
			math_007_1 = hbond_energy.nodes.new("ShaderNodeMath")
			math_007_1.label = "*e"
			math_007_1.name = "Math.007"
			math_007_1.mute = True
			math_007_1.operation = 'MULTIPLY'
			math_007_1.use_clamp = False
			#Value_001
			math_007_1.inputs[1].default_value = -1.0
			
			#node Compare
			compare_13 = hbond_energy.nodes.new("FunctionNodeCompare")
			compare_13.label = "Cutoff kcal/mol"
			compare_13.name = "Compare"
			compare_13.data_type = 'FLOAT'
			compare_13.mode = 'ELEMENT'
			compare_13.operation = 'LESS_THAN'
			#B
			compare_13.inputs[1].default_value = -0.5
			
			#node Group Input.001
			group_input_001_9 = hbond_energy.nodes.new("NodeGroupInput")
			group_input_001_9.name = "Group Input.001"
			
			
			
			
			#Set locations
			group_output_60.location = (900.0, 40.0)
			group_input_59.location = (-644.257568359375, 10.571624755859375)
			group_003_3.location = (-355.197021484375, 210.6334228515625)
			group_008_2.location = (-360.0, 69.3665771484375)
			group_009_3.location = (-360.0, -70.6334228515625)
			group_010_1.location = (-360.0, -210.6334228515625)
			math_002_4.location = (-180.0, 60.0)
			math_003_3.location = (-180.0, -80.0)
			math_004_1.location = (-180.0, -220.0)
			math_005_1.location = (320.0, 100.0)
			math_006_1.location = (480.0, 100.0)
			vector_math_7.location = (480.0, -60.0)
			math_007_1.location = (160.0, 100.0)
			compare_13.location = (720.0, 220.0)
			group_input_001_9.location = (320.0, -60.0)
			
			#Set dimensions
			group_output_60.width, group_output_60.height = 140.0, 100.0
			group_input_59.width, group_input_59.height = 140.0, 100.0
			group_003_3.width, group_003_3.height = 140.0, 100.0
			group_008_2.width, group_008_2.height = 140.0, 100.0
			group_009_3.width, group_009_3.height = 140.0, 100.0
			group_010_1.width, group_010_1.height = 140.0, 100.0
			math_002_4.width, math_002_4.height = 140.0, 100.0
			math_003_3.width, math_003_3.height = 140.0, 100.0
			math_004_1.width, math_004_1.height = 140.0, 100.0
			math_005_1.width, math_005_1.height = 140.0, 100.0
			math_006_1.width, math_006_1.height = 140.0, 100.0
			vector_math_7.width, vector_math_7.height = 140.0, 100.0
			math_007_1.width, math_007_1.height = 140.0, 100.0
			compare_13.width, compare_13.height = 140.0, 100.0
			group_input_001_9.width, group_input_001_9.height = 140.0, 100.0
			
			#initialize hbond_energy links
			#math_002_4.Value -> math_003_3.Value
			hbond_energy.links.new(math_002_4.outputs[0], math_003_3.inputs[0])
			#group_009_3.Value -> math_003_3.Value
			hbond_energy.links.new(group_009_3.outputs[0], math_003_3.inputs[1])
			#math_007_1.Value -> math_005_1.Value
			hbond_energy.links.new(math_007_1.outputs[0], math_005_1.inputs[0])
			#group_008_2.Value -> math_002_4.Value
			hbond_energy.links.new(group_008_2.outputs[0], math_002_4.inputs[1])
			#math_003_3.Value -> math_004_1.Value
			hbond_energy.links.new(math_003_3.outputs[0], math_004_1.inputs[0])
			#group_010_1.Value -> math_004_1.Value
			hbond_energy.links.new(group_010_1.outputs[0], math_004_1.inputs[1])
			#group_003_3.Value -> math_002_4.Value
			hbond_energy.links.new(group_003_3.outputs[0], math_002_4.inputs[0])
			#math_005_1.Value -> math_006_1.Value
			hbond_energy.links.new(math_005_1.outputs[0], math_006_1.inputs[0])
			#math_006_1.Value -> group_output_60.Bond Energy
			hbond_energy.links.new(math_006_1.outputs[0], group_output_60.inputs[1])
			#math_004_1.Value -> math_007_1.Value
			hbond_energy.links.new(math_004_1.outputs[0], math_007_1.inputs[0])
			#vector_math_7.Vector -> group_output_60.Bond Vector
			hbond_energy.links.new(vector_math_7.outputs[0], group_output_60.inputs[2])
			#math_006_1.Value -> compare_13.A
			hbond_energy.links.new(math_006_1.outputs[0], compare_13.inputs[0])
			#compare_13.Result -> group_output_60.Is Bonded
			hbond_energy.links.new(compare_13.outputs[0], group_output_60.inputs[0])
			#group_input_59.O -> group_003_3.Vector
			hbond_energy.links.new(group_input_59.outputs[0], group_003_3.inputs[0])
			#group_input_59.N -> group_003_3.Vector
			hbond_energy.links.new(group_input_59.outputs[2], group_003_3.inputs[1])
			#group_input_59.C -> group_008_2.Vector
			hbond_energy.links.new(group_input_59.outputs[1], group_008_2.inputs[0])
			#group_input_59.H -> group_008_2.Vector
			hbond_energy.links.new(group_input_59.outputs[3], group_008_2.inputs[1])
			#group_input_59.O -> group_009_3.Vector
			hbond_energy.links.new(group_input_59.outputs[0], group_009_3.inputs[0])
			#group_input_59.H -> group_009_3.Vector
			hbond_energy.links.new(group_input_59.outputs[3], group_009_3.inputs[1])
			#group_input_59.C -> group_010_1.Vector
			hbond_energy.links.new(group_input_59.outputs[1], group_010_1.inputs[0])
			#group_input_59.N -> group_010_1.Vector
			hbond_energy.links.new(group_input_59.outputs[2], group_010_1.inputs[1])
			#group_input_001_9.H -> vector_math_7.Vector
			hbond_energy.links.new(group_input_001_9.outputs[3], vector_math_7.inputs[1])
			#group_input_001_9.O -> vector_math_7.Vector
			hbond_energy.links.new(group_input_001_9.outputs[0], vector_math_7.inputs[0])
			return hbond_energy

		hbond_energy = hbond_energy_node_group()

		#initialize offset_vector node group
		def offset_vector_node_group():
			offset_vector = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Offset Vector")

			offset_vector.color_tag = 'CONVERTER'
			offset_vector.description = ""

			
			#offset_vector interface
			#Socket Value
			value_socket_13 = offset_vector.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			value_socket_13.subtype = 'NONE'
			value_socket_13.default_value = (0.0, 0.0, 0.0)
			value_socket_13.min_value = -3.4028234663852886e+38
			value_socket_13.max_value = 3.4028234663852886e+38
			value_socket_13.attribute_domain = 'POINT'
			
			#Socket Index
			index_socket_5 = offset_vector.interface.new_socket(name = "Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			index_socket_5.subtype = 'NONE'
			index_socket_5.default_value = 0
			index_socket_5.min_value = 0
			index_socket_5.max_value = 2147483647
			index_socket_5.attribute_domain = 'POINT'
			
			#Socket Position
			position_socket_3 = offset_vector.interface.new_socket(name = "Position", in_out='INPUT', socket_type = 'NodeSocketVector')
			position_socket_3.subtype = 'NONE'
			position_socket_3.default_value = (0.0, 0.0, 0.0)
			position_socket_3.min_value = -3.4028234663852886e+38
			position_socket_3.max_value = 3.4028234663852886e+38
			position_socket_3.attribute_domain = 'POINT'
			position_socket_3.hide_value = True
			
			#Socket Offset
			offset_socket_7 = offset_vector.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket_7.subtype = 'NONE'
			offset_socket_7.default_value = 0
			offset_socket_7.min_value = -2147483647
			offset_socket_7.max_value = 2147483647
			offset_socket_7.attribute_domain = 'POINT'
			
			
			#initialize offset_vector nodes
			#node Group Output
			group_output_61 = offset_vector.nodes.new("NodeGroupOutput")
			group_output_61.name = "Group Output"
			group_output_61.is_active_output = True
			
			#node Group Input
			group_input_60 = offset_vector.nodes.new("NodeGroupInput")
			group_input_60.name = "Group Input"
			
			#node Evaluate at Index
			evaluate_at_index_4 = offset_vector.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_4.name = "Evaluate at Index"
			evaluate_at_index_4.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_4.domain = 'POINT'
			
			#node Math
			math_15 = offset_vector.nodes.new("ShaderNodeMath")
			math_15.name = "Math"
			math_15.operation = 'ADD'
			math_15.use_clamp = False
			
			
			
			
			#Set locations
			group_output_61.location = (300.0, 20.0)
			group_input_60.location = (-273.81378173828125, 0.0)
			evaluate_at_index_4.location = (120.0, 20.0)
			math_15.location = (-60.0, 20.0)
			
			#Set dimensions
			group_output_61.width, group_output_61.height = 140.0, 100.0
			group_input_60.width, group_input_60.height = 140.0, 100.0
			evaluate_at_index_4.width, evaluate_at_index_4.height = 140.0, 100.0
			math_15.width, math_15.height = 140.0, 100.0
			
			#initialize offset_vector links
			#group_input_60.Position -> evaluate_at_index_4.Value
			offset_vector.links.new(group_input_60.outputs[1], evaluate_at_index_4.inputs[1])
			#evaluate_at_index_4.Value -> group_output_61.Value
			offset_vector.links.new(evaluate_at_index_4.outputs[0], group_output_61.inputs[0])
			#group_input_60.Index -> math_15.Value
			offset_vector.links.new(group_input_60.outputs[0], math_15.inputs[0])
			#group_input_60.Offset -> math_15.Value
			offset_vector.links.new(group_input_60.outputs[2], math_15.inputs[1])
			#math_15.Value -> evaluate_at_index_4.Index
			offset_vector.links.new(math_15.outputs[0], evaluate_at_index_4.inputs[0])
			return offset_vector

		offset_vector = offset_vector_node_group()

		#initialize backbone_nh node group
		def backbone_nh_node_group():
			backbone_nh = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Backbone NH")

			backbone_nh.color_tag = 'NONE'
			backbone_nh.description = ""

			
			#backbone_nh interface
			#Socket H
			h_socket_1 = backbone_nh.interface.new_socket(name = "H", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			h_socket_1.subtype = 'NONE'
			h_socket_1.default_value = (0.0, 0.0, 0.0)
			h_socket_1.min_value = -3.4028234663852886e+38
			h_socket_1.max_value = 3.4028234663852886e+38
			h_socket_1.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_14 = backbone_nh.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket_14.subtype = 'NONE'
			value_socket_14.default_value = 1.0
			value_socket_14.min_value = -10000.0
			value_socket_14.max_value = 10000.0
			value_socket_14.attribute_domain = 'POINT'
			
			
			#initialize backbone_nh nodes
			#node Group Output
			group_output_62 = backbone_nh.nodes.new("NodeGroupOutput")
			group_output_62.name = "Group Output"
			group_output_62.is_active_output = True
			
			#node Group Input
			group_input_61 = backbone_nh.nodes.new("NodeGroupInput")
			group_input_61.name = "Group Input"
			
			#node Named Attribute
			named_attribute_12 = backbone_nh.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_12.name = "Named Attribute"
			named_attribute_12.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_12.inputs[0].default_value = "backbone_N"
			
			#node Named Attribute.001
			named_attribute_001_8 = backbone_nh.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001_8.name = "Named Attribute.001"
			named_attribute_001_8.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_001_8.inputs[0].default_value = "backbone_CA"
			
			#node Named Attribute.002
			named_attribute_002_4 = backbone_nh.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002_4.name = "Named Attribute.002"
			named_attribute_002_4.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_002_4.inputs[0].default_value = "backbone_C"
			
			#node Group.002
			group_002_5 = backbone_nh.nodes.new("GeometryNodeGroup")
			group_002_5.name = "Group.002"
			group_002_5.node_tree = offset_vector
			#Socket_2
			group_002_5.inputs[0].default_value = 0
			#Socket_3
			group_002_5.inputs[2].default_value = -1
			
			#node Vector Math
			vector_math_8 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_8.name = "Vector Math"
			vector_math_8.operation = 'SUBTRACT'
			
			#node Vector Math.001
			vector_math_001_2 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_001_2.name = "Vector Math.001"
			vector_math_001_2.operation = 'SUBTRACT'
			
			#node Vector Math.002
			vector_math_002_2 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_002_2.name = "Vector Math.002"
			vector_math_002_2.operation = 'NORMALIZE'
			
			#node Vector Math.003
			vector_math_003_2 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_003_2.name = "Vector Math.003"
			vector_math_003_2.operation = 'NORMALIZE'
			
			#node Vector Math.005
			vector_math_005_3 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_005_3.name = "Vector Math.005"
			vector_math_005_3.operation = 'ADD'
			
			#node Vector Math.006
			vector_math_006_2 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_006_2.name = "Vector Math.006"
			vector_math_006_2.operation = 'ADD'
			
			#node Vector Math.004
			vector_math_004_2 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_004_2.name = "Vector Math.004"
			vector_math_004_2.operation = 'SCALE'
			
			#node Group.003
			group_003_4 = backbone_nh.nodes.new("GeometryNodeGroup")
			group_003_4.name = "Group.003"
			group_003_4.node_tree = mn_units
			
			#node Vector Math.007
			vector_math_007_2 = backbone_nh.nodes.new("ShaderNodeVectorMath")
			vector_math_007_2.name = "Vector Math.007"
			vector_math_007_2.operation = 'NORMALIZE'
			
			
			
			
			#Set locations
			group_output_62.location = (620.0, 0.0)
			group_input_61.location = (-630.0, 0.0)
			named_attribute_12.location = (-430.0, 140.0)
			named_attribute_001_8.location = (-430.0, 0.0)
			named_attribute_002_4.location = (-430.0, -140.0)
			group_002_5.location = (-210.0, -120.0)
			vector_math_8.location = (-50.0, 0.0)
			vector_math_001_2.location = (-50.0, 140.0)
			vector_math_002_2.location = (110.0, 140.0)
			vector_math_003_2.location = (110.0, 0.0)
			vector_math_005_3.location = (270.0, 140.0)
			vector_math_006_2.location = (430.0, 140.0)
			vector_math_004_2.location = (260.0, -120.0)
			group_003_4.location = (100.0, -120.0)
			vector_math_007_2.location = (260.0, 0.0)
			
			#Set dimensions
			group_output_62.width, group_output_62.height = 140.0, 100.0
			group_input_61.width, group_input_61.height = 140.0, 100.0
			named_attribute_12.width, named_attribute_12.height = 189.579833984375, 100.0
			named_attribute_001_8.width, named_attribute_001_8.height = 189.579833984375, 100.0
			named_attribute_002_4.width, named_attribute_002_4.height = 189.579833984375, 100.0
			group_002_5.width, group_002_5.height = 140.0, 100.0
			vector_math_8.width, vector_math_8.height = 140.0, 100.0
			vector_math_001_2.width, vector_math_001_2.height = 140.0, 100.0
			vector_math_002_2.width, vector_math_002_2.height = 140.0, 100.0
			vector_math_003_2.width, vector_math_003_2.height = 140.0, 100.0
			vector_math_005_3.width, vector_math_005_3.height = 140.0, 100.0
			vector_math_006_2.width, vector_math_006_2.height = 140.0, 100.0
			vector_math_004_2.width, vector_math_004_2.height = 140.0, 100.0
			group_003_4.width, group_003_4.height = 140.0, 100.0
			vector_math_007_2.width, vector_math_007_2.height = 140.0, 100.0
			
			#initialize backbone_nh links
			#vector_math_004_2.Vector -> vector_math_006_2.Vector
			backbone_nh.links.new(vector_math_004_2.outputs[0], vector_math_006_2.inputs[1])
			#named_attribute_001_8.Attribute -> vector_math_001_2.Vector
			backbone_nh.links.new(named_attribute_001_8.outputs[0], vector_math_001_2.inputs[1])
			#named_attribute_002_4.Attribute -> group_002_5.Position
			backbone_nh.links.new(named_attribute_002_4.outputs[0], group_002_5.inputs[1])
			#named_attribute_12.Attribute -> vector_math_8.Vector
			backbone_nh.links.new(named_attribute_12.outputs[0], vector_math_8.inputs[0])
			#vector_math_8.Vector -> vector_math_003_2.Vector
			backbone_nh.links.new(vector_math_8.outputs[0], vector_math_003_2.inputs[0])
			#group_003_4.Angstrom -> vector_math_004_2.Scale
			backbone_nh.links.new(group_003_4.outputs[0], vector_math_004_2.inputs[3])
			#vector_math_003_2.Vector -> vector_math_005_3.Vector
			backbone_nh.links.new(vector_math_003_2.outputs[0], vector_math_005_3.inputs[1])
			#group_002_5.Value -> vector_math_8.Vector
			backbone_nh.links.new(group_002_5.outputs[0], vector_math_8.inputs[1])
			#vector_math_002_2.Vector -> vector_math_005_3.Vector
			backbone_nh.links.new(vector_math_002_2.outputs[0], vector_math_005_3.inputs[0])
			#named_attribute_12.Attribute -> vector_math_001_2.Vector
			backbone_nh.links.new(named_attribute_12.outputs[0], vector_math_001_2.inputs[0])
			#vector_math_001_2.Vector -> vector_math_002_2.Vector
			backbone_nh.links.new(vector_math_001_2.outputs[0], vector_math_002_2.inputs[0])
			#named_attribute_12.Attribute -> vector_math_006_2.Vector
			backbone_nh.links.new(named_attribute_12.outputs[0], vector_math_006_2.inputs[0])
			#vector_math_006_2.Vector -> group_output_62.H
			backbone_nh.links.new(vector_math_006_2.outputs[0], group_output_62.inputs[0])
			#group_input_61.Value -> group_003_4.Value
			backbone_nh.links.new(group_input_61.outputs[0], group_003_4.inputs[0])
			#vector_math_005_3.Vector -> vector_math_007_2.Vector
			backbone_nh.links.new(vector_math_005_3.outputs[0], vector_math_007_2.inputs[0])
			#vector_math_007_2.Vector -> vector_math_004_2.Vector
			backbone_nh.links.new(vector_math_007_2.outputs[0], vector_math_004_2.inputs[0])
			return backbone_nh

		backbone_nh = backbone_nh_node_group()

		#initialize mn_topo_backbone node group
		def mn_topo_backbone_node_group():
			mn_topo_backbone = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "MN_topo_backbone")

			mn_topo_backbone.color_tag = 'NONE'
			mn_topo_backbone.description = ""

			
			#mn_topo_backbone interface
			#Socket O
			o_socket_2 = mn_topo_backbone.interface.new_socket(name = "O", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			o_socket_2.subtype = 'NONE'
			o_socket_2.default_value = (0.0, 0.0, 0.0)
			o_socket_2.min_value = -3.4028234663852886e+38
			o_socket_2.max_value = 3.4028234663852886e+38
			o_socket_2.attribute_domain = 'POINT'
			
			#Socket C
			c_socket_2 = mn_topo_backbone.interface.new_socket(name = "C", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			c_socket_2.subtype = 'NONE'
			c_socket_2.default_value = (0.0, 0.0, 0.0)
			c_socket_2.min_value = -3.4028234663852886e+38
			c_socket_2.max_value = 3.4028234663852886e+38
			c_socket_2.attribute_domain = 'POINT'
			
			#Socket CA
			ca_socket = mn_topo_backbone.interface.new_socket(name = "CA", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			ca_socket.subtype = 'NONE'
			ca_socket.default_value = (0.0, 0.0, 0.0)
			ca_socket.min_value = -3.4028234663852886e+38
			ca_socket.max_value = 3.4028234663852886e+38
			ca_socket.attribute_domain = 'POINT'
			
			#Socket N
			n_socket_2 = mn_topo_backbone.interface.new_socket(name = "N", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			n_socket_2.subtype = 'NONE'
			n_socket_2.default_value = (0.0, 0.0, 0.0)
			n_socket_2.min_value = -3.4028234663852886e+38
			n_socket_2.max_value = 3.4028234663852886e+38
			n_socket_2.attribute_domain = 'POINT'
			
			#Socket NH
			nh_socket = mn_topo_backbone.interface.new_socket(name = "NH", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			nh_socket.subtype = 'NONE'
			nh_socket.default_value = (0.0, 0.0, 0.0)
			nh_socket.min_value = -3.4028234663852886e+38
			nh_socket.max_value = 3.4028234663852886e+38
			nh_socket.attribute_domain = 'POINT'
			
			#Socket Offset
			offset_socket_8 = mn_topo_backbone.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket_8.subtype = 'NONE'
			offset_socket_8.default_value = 0
			offset_socket_8.min_value = -2147483648
			offset_socket_8.max_value = 2147483647
			offset_socket_8.attribute_domain = 'POINT'
			
			
			#initialize mn_topo_backbone nodes
			#node Group Output
			group_output_63 = mn_topo_backbone.nodes.new("NodeGroupOutput")
			group_output_63.name = "Group Output"
			group_output_63.is_active_output = True
			
			#node Group Input
			group_input_62 = mn_topo_backbone.nodes.new("NodeGroupInput")
			group_input_62.name = "Group Input"
			
			#node Named Attribute.001
			named_attribute_001_9 = mn_topo_backbone.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001_9.name = "Named Attribute.001"
			named_attribute_001_9.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_001_9.inputs[0].default_value = "backbone_O"
			
			#node Named Attribute.002
			named_attribute_002_5 = mn_topo_backbone.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002_5.name = "Named Attribute.002"
			named_attribute_002_5.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_002_5.inputs[0].default_value = "backbone_C"
			
			#node Evaluate at Index
			evaluate_at_index_5 = mn_topo_backbone.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_5.name = "Evaluate at Index"
			evaluate_at_index_5.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_5.domain = 'POINT'
			
			#node Math
			math_16 = mn_topo_backbone.nodes.new("ShaderNodeMath")
			math_16.name = "Math"
			math_16.operation = 'ADD'
			math_16.use_clamp = False
			
			#node Index
			index_6 = mn_topo_backbone.nodes.new("GeometryNodeInputIndex")
			index_6.name = "Index"
			
			#node Evaluate at Index.001
			evaluate_at_index_001_4 = mn_topo_backbone.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001_4.name = "Evaluate at Index.001"
			evaluate_at_index_001_4.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_001_4.domain = 'POINT'
			
			#node Named Attribute.003
			named_attribute_003_2 = mn_topo_backbone.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_003_2.name = "Named Attribute.003"
			named_attribute_003_2.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_003_2.inputs[0].default_value = "backbone_CA"
			
			#node Evaluate at Index.002
			evaluate_at_index_002_1 = mn_topo_backbone.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_002_1.name = "Evaluate at Index.002"
			evaluate_at_index_002_1.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_002_1.domain = 'POINT'
			
			#node Evaluate at Index.003
			evaluate_at_index_003_1 = mn_topo_backbone.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_003_1.name = "Evaluate at Index.003"
			evaluate_at_index_003_1.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_003_1.domain = 'POINT'
			
			#node Named Attribute.004
			named_attribute_004_2 = mn_topo_backbone.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_004_2.name = "Named Attribute.004"
			named_attribute_004_2.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_004_2.inputs[0].default_value = "backbone_N"
			
			#node Reroute
			reroute_17 = mn_topo_backbone.nodes.new("NodeReroute")
			reroute_17.name = "Reroute"
			#node Group
			group_23 = mn_topo_backbone.nodes.new("GeometryNodeGroup")
			group_23.name = "Group"
			group_23.node_tree = backbone_nh
			#Socket_1
			group_23.inputs[0].default_value = 1.0099999904632568
			
			#node Evaluate at Index.004
			evaluate_at_index_004_1 = mn_topo_backbone.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_004_1.name = "Evaluate at Index.004"
			evaluate_at_index_004_1.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_004_1.domain = 'POINT'
			
			#node Named Attribute.005
			named_attribute_005_1 = mn_topo_backbone.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_005_1.name = "Named Attribute.005"
			named_attribute_005_1.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_005_1.inputs[0].default_value = "backbone_NH"
			
			#node Switch
			switch_15 = mn_topo_backbone.nodes.new("GeometryNodeSwitch")
			switch_15.name = "Switch"
			switch_15.input_type = 'VECTOR'
			
			#node Boolean Math
			boolean_math_14 = mn_topo_backbone.nodes.new("FunctionNodeBooleanMath")
			boolean_math_14.name = "Boolean Math"
			boolean_math_14.operation = 'NOT'
			
			
			
			
			#Set locations
			group_output_63.location = (320.0, -220.0)
			group_input_62.location = (-520.0, -260.0)
			named_attribute_001_9.location = (-300.0, 40.0)
			named_attribute_002_5.location = (-300.0, -100.0)
			evaluate_at_index_5.location = (80.0, -14.04681396484375)
			math_16.location = (-260.0, -260.0)
			index_6.location = (-520.0, -360.0)
			evaluate_at_index_001_4.location = (80.0, -170.47593688964844)
			named_attribute_003_2.location = (-300.0, -460.0)
			evaluate_at_index_002_1.location = (80.0, -326.90509033203125)
			evaluate_at_index_003_1.location = (80.0, -480.0)
			named_attribute_004_2.location = (-300.0, -600.0)
			reroute_17.location = (20.0, -340.0)
			group_23.location = (-640.0, -920.0)
			evaluate_at_index_004_1.location = (77.81956481933594, -655.5125732421875)
			named_attribute_005_1.location = (-640.0, -780.0)
			switch_15.location = (-240.0, -780.0)
			boolean_math_14.location = (-420.0, -780.0)
			
			#Set dimensions
			group_output_63.width, group_output_63.height = 140.0, 100.0
			group_input_62.width, group_input_62.height = 140.0, 100.0
			named_attribute_001_9.width, named_attribute_001_9.height = 186.42977905273438, 100.0
			named_attribute_002_5.width, named_attribute_002_5.height = 186.42977905273438, 100.0
			evaluate_at_index_5.width, evaluate_at_index_5.height = 140.0, 100.0
			math_16.width, math_16.height = 140.0, 100.0
			index_6.width, index_6.height = 140.0, 100.0
			evaluate_at_index_001_4.width, evaluate_at_index_001_4.height = 140.0, 100.0
			named_attribute_003_2.width, named_attribute_003_2.height = 186.42977905273438, 100.0
			evaluate_at_index_002_1.width, evaluate_at_index_002_1.height = 140.0, 100.0
			evaluate_at_index_003_1.width, evaluate_at_index_003_1.height = 140.0, 100.0
			named_attribute_004_2.width, named_attribute_004_2.height = 186.42977905273438, 100.0
			reroute_17.width, reroute_17.height = 16.0, 100.0
			group_23.width, group_23.height = 186.0294189453125, 100.0
			evaluate_at_index_004_1.width, evaluate_at_index_004_1.height = 140.0, 100.0
			named_attribute_005_1.width, named_attribute_005_1.height = 186.42977905273438, 100.0
			switch_15.width, switch_15.height = 140.0, 100.0
			boolean_math_14.width, boolean_math_14.height = 140.0, 100.0
			
			#initialize mn_topo_backbone links
			#named_attribute_001_9.Attribute -> evaluate_at_index_5.Value
			mn_topo_backbone.links.new(named_attribute_001_9.outputs[0], evaluate_at_index_5.inputs[1])
			#reroute_17.Output -> evaluate_at_index_5.Index
			mn_topo_backbone.links.new(reroute_17.outputs[0], evaluate_at_index_5.inputs[0])
			#group_input_62.Offset -> math_16.Value
			mn_topo_backbone.links.new(group_input_62.outputs[0], math_16.inputs[0])
			#reroute_17.Output -> evaluate_at_index_001_4.Index
			mn_topo_backbone.links.new(reroute_17.outputs[0], evaluate_at_index_001_4.inputs[0])
			#named_attribute_002_5.Attribute -> evaluate_at_index_001_4.Value
			mn_topo_backbone.links.new(named_attribute_002_5.outputs[0], evaluate_at_index_001_4.inputs[1])
			#reroute_17.Output -> evaluate_at_index_002_1.Index
			mn_topo_backbone.links.new(reroute_17.outputs[0], evaluate_at_index_002_1.inputs[0])
			#named_attribute_003_2.Attribute -> evaluate_at_index_002_1.Value
			mn_topo_backbone.links.new(named_attribute_003_2.outputs[0], evaluate_at_index_002_1.inputs[1])
			#reroute_17.Output -> evaluate_at_index_003_1.Index
			mn_topo_backbone.links.new(reroute_17.outputs[0], evaluate_at_index_003_1.inputs[0])
			#named_attribute_004_2.Attribute -> evaluate_at_index_003_1.Value
			mn_topo_backbone.links.new(named_attribute_004_2.outputs[0], evaluate_at_index_003_1.inputs[1])
			#index_6.Index -> math_16.Value
			mn_topo_backbone.links.new(index_6.outputs[0], math_16.inputs[1])
			#math_16.Value -> reroute_17.Input
			mn_topo_backbone.links.new(math_16.outputs[0], reroute_17.inputs[0])
			#evaluate_at_index_003_1.Value -> group_output_63.N
			mn_topo_backbone.links.new(evaluate_at_index_003_1.outputs[0], group_output_63.inputs[3])
			#evaluate_at_index_002_1.Value -> group_output_63.CA
			mn_topo_backbone.links.new(evaluate_at_index_002_1.outputs[0], group_output_63.inputs[2])
			#evaluate_at_index_001_4.Value -> group_output_63.C
			mn_topo_backbone.links.new(evaluate_at_index_001_4.outputs[0], group_output_63.inputs[1])
			#evaluate_at_index_5.Value -> group_output_63.O
			mn_topo_backbone.links.new(evaluate_at_index_5.outputs[0], group_output_63.inputs[0])
			#reroute_17.Output -> evaluate_at_index_004_1.Index
			mn_topo_backbone.links.new(reroute_17.outputs[0], evaluate_at_index_004_1.inputs[0])
			#evaluate_at_index_004_1.Value -> group_output_63.NH
			mn_topo_backbone.links.new(evaluate_at_index_004_1.outputs[0], group_output_63.inputs[4])
			#group_23.H -> switch_15.True
			mn_topo_backbone.links.new(group_23.outputs[0], switch_15.inputs[2])
			#switch_15.Output -> evaluate_at_index_004_1.Value
			mn_topo_backbone.links.new(switch_15.outputs[0], evaluate_at_index_004_1.inputs[1])
			#named_attribute_005_1.Exists -> boolean_math_14.Boolean
			mn_topo_backbone.links.new(named_attribute_005_1.outputs[1], boolean_math_14.inputs[0])
			#boolean_math_14.Boolean -> switch_15.Switch
			mn_topo_backbone.links.new(boolean_math_14.outputs[0], switch_15.inputs[0])
			#named_attribute_005_1.Attribute -> switch_15.False
			mn_topo_backbone.links.new(named_attribute_005_1.outputs[0], switch_15.inputs[1])
			return mn_topo_backbone

		mn_topo_backbone = mn_topo_backbone_node_group()

		#initialize hbond_backbone_check node group
		def hbond_backbone_check_node_group():
			hbond_backbone_check = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "HBond Backbone Check")

			hbond_backbone_check.color_tag = 'NONE'
			hbond_backbone_check.description = ""

			
			#hbond_backbone_check interface
			#Socket Is Bonded
			is_bonded_socket_1 = hbond_backbone_check.interface.new_socket(name = "Is Bonded", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_bonded_socket_1.attribute_domain = 'POINT'
			
			#Socket Bond Energy
			bond_energy_socket_1 = hbond_backbone_check.interface.new_socket(name = "Bond Energy", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			bond_energy_socket_1.subtype = 'NONE'
			bond_energy_socket_1.default_value = 0.0
			bond_energy_socket_1.min_value = -3.4028234663852886e+38
			bond_energy_socket_1.max_value = 3.4028234663852886e+38
			bond_energy_socket_1.attribute_domain = 'POINT'
			
			#Socket H->O
			h__o_socket = hbond_backbone_check.interface.new_socket(name = "H->O", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			h__o_socket.subtype = 'NONE'
			h__o_socket.default_value = (0.0, 0.0, 0.0)
			h__o_socket.min_value = -3.4028234663852886e+38
			h__o_socket.max_value = 3.4028234663852886e+38
			h__o_socket.attribute_domain = 'POINT'
			
			#Panel CO
			co_panel = hbond_backbone_check.interface.new_panel("CO")
			#Socket CO Index
			co_index_socket = hbond_backbone_check.interface.new_socket(name = "CO Index", in_out='INPUT', socket_type = 'NodeSocketInt', parent = co_panel)
			co_index_socket.subtype = 'NONE'
			co_index_socket.default_value = 0
			co_index_socket.min_value = 0
			co_index_socket.max_value = 2147483647
			co_index_socket.attribute_domain = 'POINT'
			
			#Socket CO Offset
			co_offset_socket = hbond_backbone_check.interface.new_socket(name = "CO Offset", in_out='INPUT', socket_type = 'NodeSocketInt', parent = co_panel)
			co_offset_socket.subtype = 'NONE'
			co_offset_socket.default_value = 0
			co_offset_socket.min_value = -2147483648
			co_offset_socket.max_value = 2147483647
			co_offset_socket.attribute_domain = 'POINT'
			
			
			#Panel NH
			nh_panel = hbond_backbone_check.interface.new_panel("NH")
			#Socket NH Index
			nh_index_socket = hbond_backbone_check.interface.new_socket(name = "NH Index", in_out='INPUT', socket_type = 'NodeSocketInt', parent = nh_panel)
			nh_index_socket.subtype = 'NONE'
			nh_index_socket.default_value = 0
			nh_index_socket.min_value = 0
			nh_index_socket.max_value = 2147483647
			nh_index_socket.attribute_domain = 'POINT'
			
			#Socket NH Offset
			nh_offset_socket = hbond_backbone_check.interface.new_socket(name = "NH Offset", in_out='INPUT', socket_type = 'NodeSocketInt', parent = nh_panel)
			nh_offset_socket.subtype = 'NONE'
			nh_offset_socket.default_value = 0
			nh_offset_socket.min_value = -2147483648
			nh_offset_socket.max_value = 2147483647
			nh_offset_socket.attribute_domain = 'POINT'
			
			
			
			#initialize hbond_backbone_check nodes
			#node Group Output
			group_output_64 = hbond_backbone_check.nodes.new("NodeGroupOutput")
			group_output_64.name = "Group Output"
			group_output_64.is_active_output = True
			
			#node Group Input
			group_input_63 = hbond_backbone_check.nodes.new("NodeGroupInput")
			group_input_63.name = "Group Input"
			
			#node Group.008
			group_008_3 = hbond_backbone_check.nodes.new("GeometryNodeGroup")
			group_008_3.name = "Group.008"
			group_008_3.node_tree = hbond_energy
			
			#node Group.009
			group_009_4 = hbond_backbone_check.nodes.new("GeometryNodeGroup")
			group_009_4.name = "Group.009"
			group_009_4.node_tree = mn_topo_backbone
			#Socket_3
			group_009_4.inputs[0].default_value = 0
			
			#node Evaluate at Index
			evaluate_at_index_6 = hbond_backbone_check.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_6.name = "Evaluate at Index"
			evaluate_at_index_6.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_6.domain = 'POINT'
			
			#node Evaluate at Index.001
			evaluate_at_index_001_5 = hbond_backbone_check.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001_5.name = "Evaluate at Index.001"
			evaluate_at_index_001_5.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_001_5.domain = 'POINT'
			
			#node Evaluate at Index.002
			evaluate_at_index_002_2 = hbond_backbone_check.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_002_2.name = "Evaluate at Index.002"
			evaluate_at_index_002_2.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_002_2.domain = 'POINT'
			
			#node Evaluate at Index.003
			evaluate_at_index_003_2 = hbond_backbone_check.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_003_2.name = "Evaluate at Index.003"
			evaluate_at_index_003_2.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_003_2.domain = 'POINT'
			
			#node Math
			math_17 = hbond_backbone_check.nodes.new("ShaderNodeMath")
			math_17.name = "Math"
			math_17.operation = 'ADD'
			math_17.use_clamp = False
			
			#node Math.001
			math_001_10 = hbond_backbone_check.nodes.new("ShaderNodeMath")
			math_001_10.name = "Math.001"
			math_001_10.operation = 'ADD'
			math_001_10.use_clamp = False
			
			#node Math.002
			math_002_5 = hbond_backbone_check.nodes.new("ShaderNodeMath")
			math_002_5.name = "Math.002"
			math_002_5.operation = 'SUBTRACT'
			math_002_5.use_clamp = False
			
			#node Math.003
			math_003_4 = hbond_backbone_check.nodes.new("ShaderNodeMath")
			math_003_4.name = "Math.003"
			math_003_4.operation = 'ABSOLUTE'
			math_003_4.use_clamp = False
			
			#node Compare
			compare_14 = hbond_backbone_check.nodes.new("FunctionNodeCompare")
			compare_14.name = "Compare"
			compare_14.data_type = 'FLOAT'
			compare_14.mode = 'ELEMENT'
			compare_14.operation = 'GREATER_THAN'
			
			#node Integer
			integer_5 = hbond_backbone_check.nodes.new("FunctionNodeInputInt")
			integer_5.name = "Integer"
			integer_5.integer = 2
			
			#node Frame
			frame_6 = hbond_backbone_check.nodes.new("NodeFrame")
			frame_6.label = "Check not bonded to +/- residues"
			frame_6.name = "Frame"
			frame_6.label_size = 20
			frame_6.shrink = True
			
			#node Switch
			switch_16 = hbond_backbone_check.nodes.new("GeometryNodeSwitch")
			switch_16.name = "Switch"
			switch_16.input_type = 'BOOLEAN'
			#False
			switch_16.inputs[1].default_value = False
			
			#node Compare.001
			compare_001_7 = hbond_backbone_check.nodes.new("FunctionNodeCompare")
			compare_001_7.name = "Compare.001"
			compare_001_7.data_type = 'FLOAT'
			compare_001_7.mode = 'ELEMENT'
			compare_001_7.operation = 'LESS_THAN'
			
			#node Vector Math
			vector_math_9 = hbond_backbone_check.nodes.new("ShaderNodeVectorMath")
			vector_math_9.name = "Vector Math"
			vector_math_9.operation = 'LENGTH'
			
			#node Group
			group_24 = hbond_backbone_check.nodes.new("GeometryNodeGroup")
			group_24.name = "Group"
			group_24.node_tree = mn_units
			#Input_1
			group_24.inputs[0].default_value = 3.0
			
			
			
			#Set parents
			math_002_5.parent = frame_6
			math_003_4.parent = frame_6
			compare_14.parent = frame_6
			integer_5.parent = frame_6
			
			#Set locations
			group_output_64.location = (820.0, 240.0)
			group_input_63.location = (-680.0, 140.0)
			group_008_3.location = (224.2731170654297, 240.0)
			group_009_4.location = (-480.0, 460.0)
			evaluate_at_index_6.location = (-20.0, 40.0)
			evaluate_at_index_001_5.location = (-20.0, -120.0)
			evaluate_at_index_002_2.location = (-20.0, 400.0)
			evaluate_at_index_003_2.location = (-20.0, 240.0)
			math_17.location = (-480.0, 240.0)
			math_001_10.location = (-480.0, 80.0)
			math_002_5.location = (70.0, 640.0)
			math_003_4.location = (240.0, 640.0)
			compare_14.location = (420.0, 640.0)
			integer_5.location = (240.0, 500.0)
			frame_6.location = (-70.0, 40.0)
			switch_16.location = (620.0, 340.0)
			compare_001_7.location = (520.0, 140.0)
			vector_math_9.location = (260.0, 20.0)
			group_24.location = (520.0, -20.0)
			
			#Set dimensions
			group_output_64.width, group_output_64.height = 140.0, 100.0
			group_input_63.width, group_input_63.height = 140.0, 100.0
			group_008_3.width, group_008_3.height = 184.92144775390625, 100.0
			group_009_4.width, group_009_4.height = 140.0, 100.0
			evaluate_at_index_6.width, evaluate_at_index_6.height = 140.0, 100.0
			evaluate_at_index_001_5.width, evaluate_at_index_001_5.height = 140.0, 100.0
			evaluate_at_index_002_2.width, evaluate_at_index_002_2.height = 140.0, 100.0
			evaluate_at_index_003_2.width, evaluate_at_index_003_2.height = 140.0, 100.0
			math_17.width, math_17.height = 140.0, 100.0
			math_001_10.width, math_001_10.height = 140.0, 100.0
			math_002_5.width, math_002_5.height = 140.0, 100.0
			math_003_4.width, math_003_4.height = 140.0, 100.0
			compare_14.width, compare_14.height = 140.0, 100.0
			integer_5.width, integer_5.height = 140.0, 100.0
			frame_6.width, frame_6.height = 550.0, 284.0
			switch_16.width, switch_16.height = 140.0, 100.0
			compare_001_7.width, compare_001_7.height = 140.0, 100.0
			vector_math_9.width, vector_math_9.height = 140.0, 100.0
			group_24.width, group_24.height = 140.0, 100.0
			
			#initialize hbond_backbone_check links
			#evaluate_at_index_001_5.Value -> group_008_3.H
			hbond_backbone_check.links.new(evaluate_at_index_001_5.outputs[0], group_008_3.inputs[3])
			#evaluate_at_index_6.Value -> group_008_3.N
			hbond_backbone_check.links.new(evaluate_at_index_6.outputs[0], group_008_3.inputs[2])
			#evaluate_at_index_002_2.Value -> group_008_3.O
			hbond_backbone_check.links.new(evaluate_at_index_002_2.outputs[0], group_008_3.inputs[0])
			#math_001_10.Value -> evaluate_at_index_001_5.Index
			hbond_backbone_check.links.new(math_001_10.outputs[0], evaluate_at_index_001_5.inputs[0])
			#math_001_10.Value -> evaluate_at_index_6.Index
			hbond_backbone_check.links.new(math_001_10.outputs[0], evaluate_at_index_6.inputs[0])
			#evaluate_at_index_003_2.Value -> group_008_3.C
			hbond_backbone_check.links.new(evaluate_at_index_003_2.outputs[0], group_008_3.inputs[1])
			#group_008_3.Bond Energy -> group_output_64.Bond Energy
			hbond_backbone_check.links.new(group_008_3.outputs[1], group_output_64.inputs[1])
			#group_008_3.Bond Vector -> group_output_64.H->O
			hbond_backbone_check.links.new(group_008_3.outputs[2], group_output_64.inputs[2])
			#math_17.Value -> evaluate_at_index_002_2.Index
			hbond_backbone_check.links.new(math_17.outputs[0], evaluate_at_index_002_2.inputs[0])
			#math_17.Value -> evaluate_at_index_003_2.Index
			hbond_backbone_check.links.new(math_17.outputs[0], evaluate_at_index_003_2.inputs[0])
			#group_input_63.CO Index -> math_17.Value
			hbond_backbone_check.links.new(group_input_63.outputs[0], math_17.inputs[0])
			#group_input_63.CO Offset -> math_17.Value
			hbond_backbone_check.links.new(group_input_63.outputs[1], math_17.inputs[1])
			#group_input_63.NH Index -> math_001_10.Value
			hbond_backbone_check.links.new(group_input_63.outputs[2], math_001_10.inputs[0])
			#group_input_63.NH Offset -> math_001_10.Value
			hbond_backbone_check.links.new(group_input_63.outputs[3], math_001_10.inputs[1])
			#math_17.Value -> math_002_5.Value
			hbond_backbone_check.links.new(math_17.outputs[0], math_002_5.inputs[0])
			#math_001_10.Value -> math_002_5.Value
			hbond_backbone_check.links.new(math_001_10.outputs[0], math_002_5.inputs[1])
			#math_002_5.Value -> math_003_4.Value
			hbond_backbone_check.links.new(math_002_5.outputs[0], math_003_4.inputs[0])
			#math_003_4.Value -> compare_14.A
			hbond_backbone_check.links.new(math_003_4.outputs[0], compare_14.inputs[0])
			#integer_5.Integer -> compare_14.B
			hbond_backbone_check.links.new(integer_5.outputs[0], compare_14.inputs[1])
			#compare_14.Result -> switch_16.Switch
			hbond_backbone_check.links.new(compare_14.outputs[0], switch_16.inputs[0])
			#group_008_3.Bond Vector -> vector_math_9.Vector
			hbond_backbone_check.links.new(group_008_3.outputs[2], vector_math_9.inputs[0])
			#vector_math_9.Value -> compare_001_7.A
			hbond_backbone_check.links.new(vector_math_9.outputs[1], compare_001_7.inputs[0])
			#group_24.Angstrom -> compare_001_7.B
			hbond_backbone_check.links.new(group_24.outputs[0], compare_001_7.inputs[1])
			#switch_16.Output -> group_output_64.Is Bonded
			hbond_backbone_check.links.new(switch_16.outputs[0], group_output_64.inputs[0])
			#group_008_3.Is Bonded -> switch_16.True
			hbond_backbone_check.links.new(group_008_3.outputs[0], switch_16.inputs[2])
			#group_009_4.O -> evaluate_at_index_002_2.Value
			hbond_backbone_check.links.new(group_009_4.outputs[0], evaluate_at_index_002_2.inputs[1])
			#group_009_4.C -> evaluate_at_index_003_2.Value
			hbond_backbone_check.links.new(group_009_4.outputs[1], evaluate_at_index_003_2.inputs[1])
			#group_009_4.N -> evaluate_at_index_6.Value
			hbond_backbone_check.links.new(group_009_4.outputs[3], evaluate_at_index_6.inputs[1])
			#group_009_4.NH -> evaluate_at_index_001_5.Value
			hbond_backbone_check.links.new(group_009_4.outputs[4], evaluate_at_index_001_5.inputs[1])
			return hbond_backbone_check

		hbond_backbone_check = hbond_backbone_check_node_group()

		#initialize boolean_run_fill node group
		def boolean_run_fill_node_group():
			boolean_run_fill = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Boolean Run Fill")

			boolean_run_fill.color_tag = 'CONVERTER'
			boolean_run_fill.description = ""

			
			#boolean_run_fill interface
			#Socket Boolean
			boolean_socket_6 = boolean_run_fill.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket_6.attribute_domain = 'POINT'
			
			#Socket Boolean
			boolean_socket_7 = boolean_run_fill.interface.new_socket(name = "Boolean", in_out='INPUT', socket_type = 'NodeSocketBool')
			boolean_socket_7.attribute_domain = 'POINT'
			boolean_socket_7.description = "Boolean array to fill runs of False"
			
			#Socket Fill Size
			fill_size_socket = boolean_run_fill.interface.new_socket(name = "Fill Size", in_out='INPUT', socket_type = 'NodeSocketInt')
			fill_size_socket.subtype = 'NONE'
			fill_size_socket.default_value = 3
			fill_size_socket.min_value = -2147483648
			fill_size_socket.max_value = 2147483647
			fill_size_socket.attribute_domain = 'POINT'
			fill_size_socket.description = "Set a run of False to True if length equal or less than Fill Size"
			
			
			#initialize boolean_run_fill nodes
			#node Group Output
			group_output_65 = boolean_run_fill.nodes.new("NodeGroupOutput")
			group_output_65.name = "Group Output"
			group_output_65.is_active_output = True
			
			#node Group Input
			group_input_64 = boolean_run_fill.nodes.new("NodeGroupInput")
			group_input_64.name = "Group Input"
			
			#node Accumulate Field
			accumulate_field_4 = boolean_run_fill.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_4.name = "Accumulate Field"
			accumulate_field_4.data_type = 'INT'
			accumulate_field_4.domain = 'POINT'
			#Group Index
			accumulate_field_4.inputs[1].default_value = 0
			
			#node Accumulate Field.001
			accumulate_field_001_4 = boolean_run_fill.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_001_4.name = "Accumulate Field.001"
			accumulate_field_001_4.data_type = 'INT'
			accumulate_field_001_4.domain = 'POINT'
			#Value
			accumulate_field_001_4.inputs[0].default_value = 1
			
			#node Compare
			compare_15 = boolean_run_fill.nodes.new("FunctionNodeCompare")
			compare_15.name = "Compare"
			compare_15.data_type = 'INT'
			compare_15.mode = 'ELEMENT'
			compare_15.operation = 'LESS_EQUAL'
			
			#node Compare.001
			compare_001_8 = boolean_run_fill.nodes.new("FunctionNodeCompare")
			compare_001_8.name = "Compare.001"
			compare_001_8.data_type = 'INT'
			compare_001_8.mode = 'ELEMENT'
			compare_001_8.operation = 'LESS_EQUAL'
			
			#node Boolean Math.010
			boolean_math_010_2 = boolean_run_fill.nodes.new("FunctionNodeBooleanMath")
			boolean_math_010_2.name = "Boolean Math.010"
			boolean_math_010_2.operation = 'AND'
			
			#node Boolean Math
			boolean_math_15 = boolean_run_fill.nodes.new("FunctionNodeBooleanMath")
			boolean_math_15.name = "Boolean Math"
			boolean_math_15.operation = 'OR'
			
			#node Reroute
			reroute_18 = boolean_run_fill.nodes.new("NodeReroute")
			reroute_18.name = "Reroute"
			#node Reroute.001
			reroute_001_13 = boolean_run_fill.nodes.new("NodeReroute")
			reroute_001_13.name = "Reroute.001"
			#node Reroute.003
			reroute_003_5 = boolean_run_fill.nodes.new("NodeReroute")
			reroute_003_5.name = "Reroute.003"
			#node Reroute.002
			reroute_002_9 = boolean_run_fill.nodes.new("NodeReroute")
			reroute_002_9.name = "Reroute.002"
			
			
			
			#Set locations
			group_output_65.location = (430.0, 0.0)
			group_input_64.location = (-480.0, -20.0)
			accumulate_field_4.location = (-220.0, -120.0)
			accumulate_field_001_4.location = (-60.0, -120.0)
			compare_15.location = (100.0, -120.0)
			compare_001_8.location = (100.0, -280.0)
			boolean_math_010_2.location = (260.0, -120.0)
			boolean_math_15.location = (260.0, 20.0)
			reroute_18.location = (60.0, -380.0)
			reroute_001_13.location = (-280.0, -380.0)
			reroute_003_5.location = (-300.0, -80.0)
			reroute_002_9.location = (-240.0, -60.0)
			
			#Set dimensions
			group_output_65.width, group_output_65.height = 140.0, 100.0
			group_input_64.width, group_input_64.height = 140.0, 100.0
			accumulate_field_4.width, accumulate_field_4.height = 140.0, 100.0
			accumulate_field_001_4.width, accumulate_field_001_4.height = 140.0, 100.0
			compare_15.width, compare_15.height = 140.0, 100.0
			compare_001_8.width, compare_001_8.height = 140.0, 100.0
			boolean_math_010_2.width, boolean_math_010_2.height = 140.0, 100.0
			boolean_math_15.width, boolean_math_15.height = 140.0, 100.0
			reroute_18.width, reroute_18.height = 16.0, 100.0
			reroute_001_13.width, reroute_001_13.height = 16.0, 100.0
			reroute_003_5.width, reroute_003_5.height = 16.0, 100.0
			reroute_002_9.width, reroute_002_9.height = 16.0, 100.0
			
			#initialize boolean_run_fill links
			#accumulate_field_001_4.Trailing -> compare_15.A
			boolean_run_fill.links.new(accumulate_field_001_4.outputs[1], compare_15.inputs[2])
			#accumulate_field_4.Leading -> accumulate_field_001_4.Group ID
			boolean_run_fill.links.new(accumulate_field_4.outputs[0], accumulate_field_001_4.inputs[1])
			#compare_001_8.Result -> boolean_math_010_2.Boolean
			boolean_run_fill.links.new(compare_001_8.outputs[0], boolean_math_010_2.inputs[1])
			#compare_15.Result -> boolean_math_010_2.Boolean
			boolean_run_fill.links.new(compare_15.outputs[0], boolean_math_010_2.inputs[0])
			#accumulate_field_001_4.Total -> compare_001_8.A
			boolean_run_fill.links.new(accumulate_field_001_4.outputs[2], compare_001_8.inputs[2])
			#reroute_18.Output -> compare_15.B
			boolean_run_fill.links.new(reroute_18.outputs[0], compare_15.inputs[3])
			#reroute_18.Output -> compare_001_8.B
			boolean_run_fill.links.new(reroute_18.outputs[0], compare_001_8.inputs[3])
			#reroute_002_9.Output -> accumulate_field_4.Value
			boolean_run_fill.links.new(reroute_002_9.outputs[0], accumulate_field_4.inputs[0])
			#reroute_002_9.Output -> boolean_math_15.Boolean
			boolean_run_fill.links.new(reroute_002_9.outputs[0], boolean_math_15.inputs[0])
			#boolean_math_010_2.Boolean -> boolean_math_15.Boolean
			boolean_run_fill.links.new(boolean_math_010_2.outputs[0], boolean_math_15.inputs[1])
			#boolean_math_15.Boolean -> group_output_65.Boolean
			boolean_run_fill.links.new(boolean_math_15.outputs[0], group_output_65.inputs[0])
			#reroute_001_13.Output -> reroute_18.Input
			boolean_run_fill.links.new(reroute_001_13.outputs[0], reroute_18.inputs[0])
			#reroute_003_5.Output -> reroute_001_13.Input
			boolean_run_fill.links.new(reroute_003_5.outputs[0], reroute_001_13.inputs[0])
			#group_input_64.Fill Size -> reroute_003_5.Input
			boolean_run_fill.links.new(group_input_64.outputs[1], reroute_003_5.inputs[0])
			#group_input_64.Boolean -> reroute_002_9.Input
			boolean_run_fill.links.new(group_input_64.outputs[0], reroute_002_9.inputs[0])
			return boolean_run_fill

		boolean_run_fill = boolean_run_fill_node_group()

		#initialize offset_boolean node group
		def offset_boolean_node_group():
			offset_boolean = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Offset Boolean")

			offset_boolean.color_tag = 'CONVERTER'
			offset_boolean.description = ""

			
			#offset_boolean interface
			#Socket Boolean
			boolean_socket_8 = offset_boolean.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket_8.attribute_domain = 'POINT'
			
			#Socket Index
			index_socket_6 = offset_boolean.interface.new_socket(name = "Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			index_socket_6.subtype = 'NONE'
			index_socket_6.default_value = 0
			index_socket_6.min_value = 0
			index_socket_6.max_value = 2147483647
			index_socket_6.attribute_domain = 'POINT'
			
			#Socket Boolean
			boolean_socket_9 = offset_boolean.interface.new_socket(name = "Boolean", in_out='INPUT', socket_type = 'NodeSocketBool')
			boolean_socket_9.attribute_domain = 'POINT'
			boolean_socket_9.hide_value = True
			
			#Socket Offset
			offset_socket_9 = offset_boolean.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket_9.subtype = 'NONE'
			offset_socket_9.default_value = 0
			offset_socket_9.min_value = -2147483647
			offset_socket_9.max_value = 2147483647
			offset_socket_9.attribute_domain = 'POINT'
			
			
			#initialize offset_boolean nodes
			#node Group Output
			group_output_66 = offset_boolean.nodes.new("NodeGroupOutput")
			group_output_66.name = "Group Output"
			group_output_66.is_active_output = True
			
			#node Group Input
			group_input_65 = offset_boolean.nodes.new("NodeGroupInput")
			group_input_65.name = "Group Input"
			
			#node Evaluate at Index
			evaluate_at_index_7 = offset_boolean.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_7.name = "Evaluate at Index"
			evaluate_at_index_7.data_type = 'BOOLEAN'
			evaluate_at_index_7.domain = 'POINT'
			
			#node Math
			math_18 = offset_boolean.nodes.new("ShaderNodeMath")
			math_18.name = "Math"
			math_18.operation = 'ADD'
			math_18.use_clamp = False
			
			
			
			
			#Set locations
			group_output_66.location = (190.0, 0.0)
			group_input_65.location = (-344.3331298828125, -46.23834991455078)
			evaluate_at_index_7.location = (0.0, 0.0)
			math_18.location = (-160.0, 0.0)
			
			#Set dimensions
			group_output_66.width, group_output_66.height = 140.0, 100.0
			group_input_65.width, group_input_65.height = 140.0, 100.0
			evaluate_at_index_7.width, evaluate_at_index_7.height = 140.0, 100.0
			math_18.width, math_18.height = 140.0, 100.0
			
			#initialize offset_boolean links
			#evaluate_at_index_7.Value -> group_output_66.Boolean
			offset_boolean.links.new(evaluate_at_index_7.outputs[0], group_output_66.inputs[0])
			#group_input_65.Boolean -> evaluate_at_index_7.Value
			offset_boolean.links.new(group_input_65.outputs[1], evaluate_at_index_7.inputs[1])
			#group_input_65.Index -> math_18.Value
			offset_boolean.links.new(group_input_65.outputs[0], math_18.inputs[1])
			#math_18.Value -> evaluate_at_index_7.Index
			offset_boolean.links.new(math_18.outputs[0], evaluate_at_index_7.inputs[0])
			#group_input_65.Offset -> math_18.Value
			offset_boolean.links.new(group_input_65.outputs[2], math_18.inputs[0])
			return offset_boolean

		offset_boolean = offset_boolean_node_group()

		#initialize vector_angle node group
		def vector_angle_node_group():
			vector_angle = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Vector Angle")

			vector_angle.color_tag = 'VECTOR'
			vector_angle.description = ""

			
			#vector_angle interface
			#Socket Angle
			angle_socket_1 = vector_angle.interface.new_socket(name = "Angle", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			angle_socket_1.subtype = 'ANGLE'
			angle_socket_1.default_value = 0.0
			angle_socket_1.min_value = -3.4028234663852886e+38
			angle_socket_1.max_value = 3.4028234663852886e+38
			angle_socket_1.attribute_domain = 'POINT'
			angle_socket_1.description = "Angle between the two given vectors in radians"
			
			#Socket A
			a_socket = vector_angle.interface.new_socket(name = "A", in_out='INPUT', socket_type = 'NodeSocketVector')
			a_socket.subtype = 'NONE'
			a_socket.default_value = (0.0, 0.0, 0.0)
			a_socket.min_value = -10000.0
			a_socket.max_value = 10000.0
			a_socket.attribute_domain = 'POINT'
			
			#Socket B
			b_socket = vector_angle.interface.new_socket(name = "B", in_out='INPUT', socket_type = 'NodeSocketVector')
			b_socket.subtype = 'NONE'
			b_socket.default_value = (0.0, 0.0, 0.0)
			b_socket.min_value = -10000.0
			b_socket.max_value = 10000.0
			b_socket.attribute_domain = 'POINT'
			
			
			#initialize vector_angle nodes
			#node Group Input
			group_input_66 = vector_angle.nodes.new("NodeGroupInput")
			group_input_66.name = "Group Input"
			
			#node Vector Math.002
			vector_math_002_3 = vector_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_002_3.name = "Vector Math.002"
			vector_math_002_3.operation = 'NORMALIZE'
			
			#node Vector Math.001
			vector_math_001_3 = vector_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_001_3.name = "Vector Math.001"
			vector_math_001_3.operation = 'NORMALIZE'
			
			#node Vector Math
			vector_math_10 = vector_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_10.name = "Vector Math"
			vector_math_10.operation = 'DOT_PRODUCT'
			
			#node Math
			math_19 = vector_angle.nodes.new("ShaderNodeMath")
			math_19.name = "Math"
			math_19.operation = 'ARCCOSINE'
			math_19.use_clamp = False
			
			#node Group Output
			group_output_67 = vector_angle.nodes.new("NodeGroupOutput")
			group_output_67.name = "Group Output"
			group_output_67.is_active_output = True
			
			
			
			
			#Set locations
			group_input_66.location = (-360.0, 0.0)
			vector_math_002_3.location = (-160.0, -60.0)
			vector_math_001_3.location = (-160.0, 60.0)
			vector_math_10.location = (0.0, 60.0)
			math_19.location = (160.0, 60.0)
			group_output_67.location = (340.0, 60.0)
			
			#Set dimensions
			group_input_66.width, group_input_66.height = 140.0, 100.0
			vector_math_002_3.width, vector_math_002_3.height = 140.0, 100.0
			vector_math_001_3.width, vector_math_001_3.height = 140.0, 100.0
			vector_math_10.width, vector_math_10.height = 140.0, 100.0
			math_19.width, math_19.height = 140.0, 100.0
			group_output_67.width, group_output_67.height = 140.0, 100.0
			
			#initialize vector_angle links
			#vector_math_10.Value -> math_19.Value
			vector_angle.links.new(vector_math_10.outputs[1], math_19.inputs[0])
			#vector_math_002_3.Vector -> vector_math_10.Vector
			vector_angle.links.new(vector_math_002_3.outputs[0], vector_math_10.inputs[1])
			#vector_math_001_3.Vector -> vector_math_10.Vector
			vector_angle.links.new(vector_math_001_3.outputs[0], vector_math_10.inputs[0])
			#math_19.Value -> group_output_67.Angle
			vector_angle.links.new(math_19.outputs[0], group_output_67.inputs[0])
			#group_input_66.A -> vector_math_001_3.Vector
			vector_angle.links.new(group_input_66.outputs[0], vector_math_001_3.inputs[0])
			#group_input_66.B -> vector_math_002_3.Vector
			vector_angle.links.new(group_input_66.outputs[1], vector_math_002_3.inputs[0])
			return vector_angle

		vector_angle = vector_angle_node_group()

		#initialize dihedral_angle node group
		def dihedral_angle_node_group():
			dihedral_angle = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Dihedral Angle")

			dihedral_angle.color_tag = 'VECTOR'
			dihedral_angle.description = ""

			
			#dihedral_angle interface
			#Socket Angle
			angle_socket_2 = dihedral_angle.interface.new_socket(name = "Angle", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			angle_socket_2.subtype = 'ANGLE'
			angle_socket_2.default_value = 0.0
			angle_socket_2.min_value = -3.4028234663852886e+38
			angle_socket_2.max_value = 3.4028234663852886e+38
			angle_socket_2.attribute_domain = 'POINT'
			angle_socket_2.description = "The angle between the vectors AB and CD, when made perpendicular to BC."
			
			#Socket BA⟂(BC)
			ba__bc__socket = dihedral_angle.interface.new_socket(name = "BA⟂(BC)", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			ba__bc__socket.subtype = 'NONE'
			ba__bc__socket.default_value = (0.0, 0.0, 0.0)
			ba__bc__socket.min_value = -3.4028234663852886e+38
			ba__bc__socket.max_value = 3.4028234663852886e+38
			ba__bc__socket.attribute_domain = 'POINT'
			ba__bc__socket.description = "The vector BA when made perpendicular to  the axis BC"
			
			#Socket CD⟂(BC)
			cd__bc__socket = dihedral_angle.interface.new_socket(name = "CD⟂(BC)", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			cd__bc__socket.subtype = 'NONE'
			cd__bc__socket.default_value = (0.0, 0.0, 0.0)
			cd__bc__socket.min_value = -3.4028234663852886e+38
			cd__bc__socket.max_value = 3.4028234663852886e+38
			cd__bc__socket.attribute_domain = 'POINT'
			cd__bc__socket.description = "The Vector CD when makde perpendicular to the axis BC"
			
			#Socket BC
			bc_socket = dihedral_angle.interface.new_socket(name = "BC", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			bc_socket.subtype = 'NONE'
			bc_socket.default_value = (0.0, 0.0, 0.0)
			bc_socket.min_value = -3.4028234663852886e+38
			bc_socket.max_value = 3.4028234663852886e+38
			bc_socket.attribute_domain = 'POINT'
			bc_socket.description = "The axis vector BC"
			
			#Socket A
			a_socket_1 = dihedral_angle.interface.new_socket(name = "A", in_out='INPUT', socket_type = 'NodeSocketVector')
			a_socket_1.subtype = 'NONE'
			a_socket_1.default_value = (0.0, 0.0, 0.0)
			a_socket_1.min_value = -3.4028234663852886e+38
			a_socket_1.max_value = 3.4028234663852886e+38
			a_socket_1.attribute_domain = 'POINT'
			a_socket_1.description = "First vector for the calculation, which draws a line to B"
			
			#Socket B
			b_socket_1 = dihedral_angle.interface.new_socket(name = "B", in_out='INPUT', socket_type = 'NodeSocketVector')
			b_socket_1.subtype = 'NONE'
			b_socket_1.default_value = (0.0, 0.0, 0.0)
			b_socket_1.min_value = -3.4028234663852886e+38
			b_socket_1.max_value = 3.4028234663852886e+38
			b_socket_1.attribute_domain = 'POINT'
			b_socket_1.description = "Second vector for the calculation, which receives a line from A and draws a line to C"
			
			#Socket C
			c_socket_3 = dihedral_angle.interface.new_socket(name = "C", in_out='INPUT', socket_type = 'NodeSocketVector')
			c_socket_3.subtype = 'NONE'
			c_socket_3.default_value = (0.0, 0.0, 0.0)
			c_socket_3.min_value = -3.4028234663852886e+38
			c_socket_3.max_value = 3.4028234663852886e+38
			c_socket_3.attribute_domain = 'POINT'
			c_socket_3.description = "Third vector for the calculation, which receives a line from B and draws a line to D"
			
			#Socket D
			d_socket = dihedral_angle.interface.new_socket(name = "D", in_out='INPUT', socket_type = 'NodeSocketVector')
			d_socket.subtype = 'NONE'
			d_socket.default_value = (0.0, 0.0, 0.0)
			d_socket.min_value = -3.4028234663852886e+38
			d_socket.max_value = 3.4028234663852886e+38
			d_socket.attribute_domain = 'POINT'
			d_socket.description = "Last vector for the calculation, which is the end point of the line from D"
			
			
			#initialize dihedral_angle nodes
			#node Vector Math.003
			vector_math_003_3 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_003_3.name = "Vector Math.003"
			vector_math_003_3.operation = 'SUBTRACT'
			
			#node Vector Math.004
			vector_math_004_3 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_004_3.name = "Vector Math.004"
			vector_math_004_3.operation = 'SUBTRACT'
			
			#node Vector Math.006
			vector_math_006_3 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_006_3.name = "Vector Math.006"
			vector_math_006_3.operation = 'SUBTRACT'
			
			#node Vector Math.007
			vector_math_007_3 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_007_3.name = "Vector Math.007"
			vector_math_007_3.operation = 'PROJECT'
			
			#node Vector Math.009
			vector_math_009_2 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_009_2.name = "Vector Math.009"
			vector_math_009_2.operation = 'PROJECT'
			
			#node Vector Math.008
			vector_math_008_4 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_008_4.name = "Vector Math.008"
			vector_math_008_4.operation = 'SUBTRACT'
			
			#node Vector Math.010
			vector_math_010_1 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_010_1.name = "Vector Math.010"
			vector_math_010_1.operation = 'SUBTRACT'
			
			#node MN_utils_vector_angle.002
			mn_utils_vector_angle_002 = dihedral_angle.nodes.new("GeometryNodeGroup")
			mn_utils_vector_angle_002.label = "Vector Angle"
			mn_utils_vector_angle_002.name = "MN_utils_vector_angle.002"
			mn_utils_vector_angle_002.node_tree = vector_angle
			
			#node Group Output
			group_output_68 = dihedral_angle.nodes.new("NodeGroupOutput")
			group_output_68.name = "Group Output"
			group_output_68.is_active_output = True
			
			#node Reroute.002
			reroute_002_10 = dihedral_angle.nodes.new("NodeReroute")
			reroute_002_10.name = "Reroute.002"
			#node Reroute.001
			reroute_001_14 = dihedral_angle.nodes.new("NodeReroute")
			reroute_001_14.name = "Reroute.001"
			#node Vector Math
			vector_math_11 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_11.name = "Vector Math"
			vector_math_11.operation = 'CROSS_PRODUCT'
			
			#node Vector Math.001
			vector_math_001_4 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_001_4.name = "Vector Math.001"
			vector_math_001_4.operation = 'DOT_PRODUCT'
			
			#node Math.001
			math_001_11 = dihedral_angle.nodes.new("ShaderNodeMath")
			math_001_11.name = "Math.001"
			math_001_11.operation = 'SIGN'
			math_001_11.use_clamp = False
			
			#node Reroute
			reroute_19 = dihedral_angle.nodes.new("NodeReroute")
			reroute_19.name = "Reroute"
			#node Math
			math_20 = dihedral_angle.nodes.new("ShaderNodeMath")
			math_20.name = "Math"
			math_20.operation = 'MULTIPLY'
			math_20.use_clamp = False
			
			#node Group Input.003
			group_input_003_3 = dihedral_angle.nodes.new("NodeGroupInput")
			group_input_003_3.name = "Group Input.003"
			group_input_003_3.outputs[0].hide = True
			group_input_003_3.outputs[1].hide = True
			group_input_003_3.outputs[2].hide = True
			group_input_003_3.outputs[4].hide = True
			
			#node Group Input.001
			group_input_001_10 = dihedral_angle.nodes.new("NodeGroupInput")
			group_input_001_10.name = "Group Input.001"
			group_input_001_10.outputs[1].hide = True
			group_input_001_10.outputs[2].hide = True
			group_input_001_10.outputs[3].hide = True
			group_input_001_10.outputs[4].hide = True
			
			#node Group Input
			group_input_67 = dihedral_angle.nodes.new("NodeGroupInput")
			group_input_67.name = "Group Input"
			group_input_67.outputs[0].hide = True
			group_input_67.outputs[2].hide = True
			group_input_67.outputs[3].hide = True
			group_input_67.outputs[4].hide = True
			
			#node Group Input.002
			group_input_002_4 = dihedral_angle.nodes.new("NodeGroupInput")
			group_input_002_4.name = "Group Input.002"
			group_input_002_4.outputs[0].hide = True
			group_input_002_4.outputs[1].hide = True
			group_input_002_4.outputs[3].hide = True
			group_input_002_4.outputs[4].hide = True
			
			
			
			
			#Set locations
			vector_math_003_3.location = (-142.68453979492188, 25.911895751953125)
			vector_math_004_3.location = (-140.0, 440.0)
			vector_math_006_3.location = (-140.0, 180.0)
			vector_math_007_3.location = (80.0, 320.0)
			vector_math_009_2.location = (80.0, -80.0)
			vector_math_008_4.location = (80.0, 460.0)
			vector_math_010_1.location = (80.0, 60.0)
			mn_utils_vector_angle_002.location = (420.0, 420.0)
			group_output_68.location = (920.0, 320.0)
			reroute_002_10.location = (300.0, 260.0)
			reroute_001_14.location = (300.0, 240.0)
			vector_math_11.location = (420.0, 180.0)
			vector_math_001_4.location = (420.0, 40.0)
			math_001_11.location = (580.0, 40.0)
			reroute_19.location = (300.0, 220.0)
			math_20.location = (640.0, 420.0)
			group_input_003_3.location = (-440.0, 0.0)
			group_input_001_10.location = (-440.0, 420.0)
			group_input_67.location = (-440.0, 280.0)
			group_input_002_4.location = (-440.0, 140.0)
			
			#Set dimensions
			vector_math_003_3.width, vector_math_003_3.height = 140.0, 100.0
			vector_math_004_3.width, vector_math_004_3.height = 140.0, 100.0
			vector_math_006_3.width, vector_math_006_3.height = 140.0, 100.0
			vector_math_007_3.width, vector_math_007_3.height = 140.0, 100.0
			vector_math_009_2.width, vector_math_009_2.height = 140.0, 100.0
			vector_math_008_4.width, vector_math_008_4.height = 140.0, 100.0
			vector_math_010_1.width, vector_math_010_1.height = 140.0, 100.0
			mn_utils_vector_angle_002.width, mn_utils_vector_angle_002.height = 200.0, 100.0
			group_output_68.width, group_output_68.height = 140.0, 100.0
			reroute_002_10.width, reroute_002_10.height = 16.0, 100.0
			reroute_001_14.width, reroute_001_14.height = 16.0, 100.0
			vector_math_11.width, vector_math_11.height = 140.0, 100.0
			vector_math_001_4.width, vector_math_001_4.height = 140.0, 100.0
			math_001_11.width, math_001_11.height = 140.0, 100.0
			reroute_19.width, reroute_19.height = 16.0, 100.0
			math_20.width, math_20.height = 140.0, 100.0
			group_input_003_3.width, group_input_003_3.height = 140.0, 100.0
			group_input_001_10.width, group_input_001_10.height = 140.0, 100.0
			group_input_67.width, group_input_67.height = 140.0, 100.0
			group_input_002_4.width, group_input_002_4.height = 140.0, 100.0
			
			#initialize dihedral_angle links
			#vector_math_007_3.Vector -> vector_math_008_4.Vector
			dihedral_angle.links.new(vector_math_007_3.outputs[0], vector_math_008_4.inputs[1])
			#vector_math_009_2.Vector -> vector_math_010_1.Vector
			dihedral_angle.links.new(vector_math_009_2.outputs[0], vector_math_010_1.inputs[1])
			#vector_math_004_3.Vector -> vector_math_007_3.Vector
			dihedral_angle.links.new(vector_math_004_3.outputs[0], vector_math_007_3.inputs[0])
			#vector_math_006_3.Vector -> vector_math_007_3.Vector
			dihedral_angle.links.new(vector_math_006_3.outputs[0], vector_math_007_3.inputs[1])
			#reroute_002_10.Output -> mn_utils_vector_angle_002.A
			dihedral_angle.links.new(reroute_002_10.outputs[0], mn_utils_vector_angle_002.inputs[0])
			#vector_math_004_3.Vector -> vector_math_008_4.Vector
			dihedral_angle.links.new(vector_math_004_3.outputs[0], vector_math_008_4.inputs[0])
			#vector_math_003_3.Vector -> vector_math_010_1.Vector
			dihedral_angle.links.new(vector_math_003_3.outputs[0], vector_math_010_1.inputs[0])
			#vector_math_003_3.Vector -> vector_math_009_2.Vector
			dihedral_angle.links.new(vector_math_003_3.outputs[0], vector_math_009_2.inputs[0])
			#vector_math_006_3.Vector -> vector_math_009_2.Vector
			dihedral_angle.links.new(vector_math_006_3.outputs[0], vector_math_009_2.inputs[1])
			#vector_math_006_3.Vector -> reroute_19.Input
			dihedral_angle.links.new(vector_math_006_3.outputs[0], reroute_19.inputs[0])
			#reroute_001_14.Output -> mn_utils_vector_angle_002.B
			dihedral_angle.links.new(reroute_001_14.outputs[0], mn_utils_vector_angle_002.inputs[1])
			#vector_math_11.Vector -> vector_math_001_4.Vector
			dihedral_angle.links.new(vector_math_11.outputs[0], vector_math_001_4.inputs[0])
			#reroute_19.Output -> vector_math_001_4.Vector
			dihedral_angle.links.new(reroute_19.outputs[0], vector_math_001_4.inputs[1])
			#mn_utils_vector_angle_002.Angle -> math_20.Value
			dihedral_angle.links.new(mn_utils_vector_angle_002.outputs[0], math_20.inputs[0])
			#reroute_001_14.Output -> vector_math_11.Vector
			dihedral_angle.links.new(reroute_001_14.outputs[0], vector_math_11.inputs[1])
			#group_input_002_4.C -> vector_math_003_3.Vector
			dihedral_angle.links.new(group_input_002_4.outputs[2], vector_math_003_3.inputs[1])
			#group_input_67.B -> vector_math_004_3.Vector
			dihedral_angle.links.new(group_input_67.outputs[1], vector_math_004_3.inputs[1])
			#group_input_67.B -> vector_math_006_3.Vector
			dihedral_angle.links.new(group_input_67.outputs[1], vector_math_006_3.inputs[1])
			#group_input_002_4.C -> vector_math_006_3.Vector
			dihedral_angle.links.new(group_input_002_4.outputs[2], vector_math_006_3.inputs[0])
			#math_20.Value -> group_output_68.Angle
			dihedral_angle.links.new(math_20.outputs[0], group_output_68.inputs[0])
			#reroute_002_10.Output -> group_output_68.BA⟂(BC)
			dihedral_angle.links.new(reroute_002_10.outputs[0], group_output_68.inputs[1])
			#reroute_19.Output -> group_output_68.BC
			dihedral_angle.links.new(reroute_19.outputs[0], group_output_68.inputs[3])
			#reroute_001_14.Output -> group_output_68.CD⟂(BC)
			dihedral_angle.links.new(reroute_001_14.outputs[0], group_output_68.inputs[2])
			#reroute_002_10.Output -> vector_math_11.Vector
			dihedral_angle.links.new(reroute_002_10.outputs[0], vector_math_11.inputs[0])
			#vector_math_001_4.Value -> math_001_11.Value
			dihedral_angle.links.new(vector_math_001_4.outputs[1], math_001_11.inputs[0])
			#math_001_11.Value -> math_20.Value
			dihedral_angle.links.new(math_001_11.outputs[0], math_20.inputs[1])
			#vector_math_010_1.Vector -> reroute_001_14.Input
			dihedral_angle.links.new(vector_math_010_1.outputs[0], reroute_001_14.inputs[0])
			#vector_math_008_4.Vector -> reroute_002_10.Input
			dihedral_angle.links.new(vector_math_008_4.outputs[0], reroute_002_10.inputs[0])
			#group_input_001_10.A -> vector_math_004_3.Vector
			dihedral_angle.links.new(group_input_001_10.outputs[0], vector_math_004_3.inputs[0])
			#group_input_003_3.D -> vector_math_003_3.Vector
			dihedral_angle.links.new(group_input_003_3.outputs[3], vector_math_003_3.inputs[0])
			return dihedral_angle

		dihedral_angle = dihedral_angle_node_group()

		#initialize _mn_topo_phi_psi node group
		def _mn_topo_phi_psi_node_group():
			_mn_topo_phi_psi = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_topo_phi_psi")

			_mn_topo_phi_psi.color_tag = 'NONE'
			_mn_topo_phi_psi.description = ""

			
			#_mn_topo_phi_psi interface
			#Socket Angle
			angle_socket_3 = _mn_topo_phi_psi.interface.new_socket(name = "Angle", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			angle_socket_3.subtype = 'ANGLE'
			angle_socket_3.default_value = 0.0
			angle_socket_3.min_value = -3.4028234663852886e+38
			angle_socket_3.max_value = 3.4028234663852886e+38
			angle_socket_3.attribute_domain = 'POINT'
			
			#Socket BA⟂(BC)
			ba__bc__socket_1 = _mn_topo_phi_psi.interface.new_socket(name = "BA⟂(BC)", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			ba__bc__socket_1.subtype = 'NONE'
			ba__bc__socket_1.default_value = (0.0, 0.0, 0.0)
			ba__bc__socket_1.min_value = -3.4028234663852886e+38
			ba__bc__socket_1.max_value = 3.4028234663852886e+38
			ba__bc__socket_1.attribute_domain = 'POINT'
			
			#Socket CD⟂(BC)
			cd__bc__socket_1 = _mn_topo_phi_psi.interface.new_socket(name = "CD⟂(BC)", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			cd__bc__socket_1.subtype = 'NONE'
			cd__bc__socket_1.default_value = (0.0, 0.0, 0.0)
			cd__bc__socket_1.min_value = -3.4028234663852886e+38
			cd__bc__socket_1.max_value = 3.4028234663852886e+38
			cd__bc__socket_1.attribute_domain = 'POINT'
			
			#Socket BC
			bc_socket_1 = _mn_topo_phi_psi.interface.new_socket(name = "BC", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			bc_socket_1.subtype = 'NONE'
			bc_socket_1.default_value = (0.0, 0.0, 0.0)
			bc_socket_1.min_value = -3.4028234663852886e+38
			bc_socket_1.max_value = 3.4028234663852886e+38
			bc_socket_1.attribute_domain = 'POINT'
			
			#Socket A
			a_socket_2 = _mn_topo_phi_psi.interface.new_socket(name = "A", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			a_socket_2.subtype = 'NONE'
			a_socket_2.default_value = (0.0, 0.0, 0.0)
			a_socket_2.min_value = -3.4028234663852886e+38
			a_socket_2.max_value = 3.4028234663852886e+38
			a_socket_2.attribute_domain = 'POINT'
			
			#Socket B
			b_socket_2 = _mn_topo_phi_psi.interface.new_socket(name = "B", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			b_socket_2.subtype = 'NONE'
			b_socket_2.default_value = (0.0, 0.0, 0.0)
			b_socket_2.min_value = -3.4028234663852886e+38
			b_socket_2.max_value = 3.4028234663852886e+38
			b_socket_2.attribute_domain = 'POINT'
			
			#Socket C
			c_socket_4 = _mn_topo_phi_psi.interface.new_socket(name = "C", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			c_socket_4.subtype = 'NONE'
			c_socket_4.default_value = (0.0, 0.0, 0.0)
			c_socket_4.min_value = -3.4028234663852886e+38
			c_socket_4.max_value = 3.4028234663852886e+38
			c_socket_4.attribute_domain = 'POINT'
			
			#Socket D
			d_socket_1 = _mn_topo_phi_psi.interface.new_socket(name = "D", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			d_socket_1.subtype = 'NONE'
			d_socket_1.default_value = (0.0, 0.0, 0.0)
			d_socket_1.min_value = -3.4028234663852886e+38
			d_socket_1.max_value = 3.4028234663852886e+38
			d_socket_1.attribute_domain = 'POINT'
			
			#Socket Menu
			menu_socket = _mn_topo_phi_psi.interface.new_socket(name = "Menu", in_out='INPUT', socket_type = 'NodeSocketMenu')
			menu_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_topo_phi_psi nodes
			#node Group Output
			group_output_69 = _mn_topo_phi_psi.nodes.new("NodeGroupOutput")
			group_output_69.name = "Group Output"
			group_output_69.is_active_output = True
			
			#node Group Input
			group_input_68 = _mn_topo_phi_psi.nodes.new("NodeGroupInput")
			group_input_68.name = "Group Input"
			
			#node Group.005
			group_005_3 = _mn_topo_phi_psi.nodes.new("GeometryNodeGroup")
			group_005_3.name = "Group.005"
			group_005_3.node_tree = mn_topo_backbone
			#Socket_3
			group_005_3.inputs[0].default_value = 1
			
			#node Group.007
			group_007_1 = _mn_topo_phi_psi.nodes.new("GeometryNodeGroup")
			group_007_1.name = "Group.007"
			group_007_1.node_tree = mn_topo_backbone
			#Socket_3
			group_007_1.inputs[0].default_value = -1
			
			#node Group.008
			group_008_4 = _mn_topo_phi_psi.nodes.new("GeometryNodeGroup")
			group_008_4.name = "Group.008"
			group_008_4.node_tree = mn_topo_backbone
			#Socket_3
			group_008_4.inputs[0].default_value = 0
			
			#node Group.009
			group_009_5 = _mn_topo_phi_psi.nodes.new("GeometryNodeGroup")
			group_009_5.name = "Group.009"
			group_009_5.node_tree = dihedral_angle
			
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
			group_output_69.location = (698.508544921875, 198.78929138183594)
			group_input_68.location = (-520.0, 280.0)
			group_005_3.location = (-380.0, -320.0)
			group_007_1.location = (-380.0, -120.0)
			group_008_4.location = (-380.0, 80.0)
			group_009_5.location = (272.33380126953125, 98.96731567382812)
			menu_switch.location = (-340.0, 260.0)
			index_switch.location = (-20.0, 140.0)
			index_switch_001.location = (-20.0, -100.0)
			index_switch_002.location = (-20.0, -280.0)
			
			#Set dimensions
			group_output_69.width, group_output_69.height = 140.0, 100.0
			group_input_68.width, group_input_68.height = 140.0, 100.0
			group_005_3.width, group_005_3.height = 171.90289306640625, 100.0
			group_007_1.width, group_007_1.height = 171.90289306640625, 100.0
			group_008_4.width, group_008_4.height = 171.90289306640625, 100.0
			group_009_5.width, group_009_5.height = 299.8184509277344, 100.0
			menu_switch.width, menu_switch.height = 140.0, 100.0
			index_switch.width, index_switch.height = 140.0, 100.0
			index_switch_001.width, index_switch_001.height = 140.0, 100.0
			index_switch_002.width, index_switch_002.height = 140.0, 100.0
			
			#initialize _mn_topo_phi_psi links
			#group_008_4.CA -> group_009_5.B
			_mn_topo_phi_psi.links.new(group_008_4.outputs[2], group_009_5.inputs[1])
			#index_switch_002.Output -> group_009_5.D
			_mn_topo_phi_psi.links.new(index_switch_002.outputs[0], group_009_5.inputs[3])
			#index_switch.Output -> group_009_5.A
			_mn_topo_phi_psi.links.new(index_switch.outputs[0], group_009_5.inputs[0])
			#index_switch_001.Output -> group_009_5.C
			_mn_topo_phi_psi.links.new(index_switch_001.outputs[0], group_009_5.inputs[2])
			#group_009_5.Angle -> group_output_69.Angle
			_mn_topo_phi_psi.links.new(group_009_5.outputs[0], group_output_69.inputs[0])
			#group_009_5.BA⟂(BC) -> group_output_69.BA⟂(BC)
			_mn_topo_phi_psi.links.new(group_009_5.outputs[1], group_output_69.inputs[1])
			#group_009_5.BC -> group_output_69.BC
			_mn_topo_phi_psi.links.new(group_009_5.outputs[3], group_output_69.inputs[3])
			#index_switch.Output -> group_output_69.A
			_mn_topo_phi_psi.links.new(index_switch.outputs[0], group_output_69.inputs[4])
			#group_008_4.CA -> group_output_69.B
			_mn_topo_phi_psi.links.new(group_008_4.outputs[2], group_output_69.inputs[5])
			#index_switch_001.Output -> group_output_69.C
			_mn_topo_phi_psi.links.new(index_switch_001.outputs[0], group_output_69.inputs[6])
			#index_switch_002.Output -> group_output_69.D
			_mn_topo_phi_psi.links.new(index_switch_002.outputs[0], group_output_69.inputs[7])
			#group_009_5.CD⟂(BC) -> group_output_69.CD⟂(BC)
			_mn_topo_phi_psi.links.new(group_009_5.outputs[2], group_output_69.inputs[2])
			#menu_switch.Output -> index_switch.Index
			_mn_topo_phi_psi.links.new(menu_switch.outputs[0], index_switch.inputs[0])
			#group_input_68.Menu -> menu_switch.Menu
			_mn_topo_phi_psi.links.new(group_input_68.outputs[0], menu_switch.inputs[0])
			#group_008_4.C -> index_switch.0
			_mn_topo_phi_psi.links.new(group_008_4.outputs[1], index_switch.inputs[1])
			#menu_switch.Output -> index_switch_001.Index
			_mn_topo_phi_psi.links.new(menu_switch.outputs[0], index_switch_001.inputs[0])
			#group_008_4.N -> index_switch_001.0
			_mn_topo_phi_psi.links.new(group_008_4.outputs[3], index_switch_001.inputs[1])
			#group_008_4.C -> index_switch_001.1
			_mn_topo_phi_psi.links.new(group_008_4.outputs[1], index_switch_001.inputs[2])
			#menu_switch.Output -> index_switch_002.Index
			_mn_topo_phi_psi.links.new(menu_switch.outputs[0], index_switch_002.inputs[0])
			#group_007_1.C -> index_switch_002.0
			_mn_topo_phi_psi.links.new(group_007_1.outputs[1], index_switch_002.inputs[1])
			#group_005_3.N -> index_switch_002.1
			_mn_topo_phi_psi.links.new(group_005_3.outputs[3], index_switch_002.inputs[2])
			#group_008_4.N -> index_switch.1
			_mn_topo_phi_psi.links.new(group_008_4.outputs[3], index_switch.inputs[2])
			return _mn_topo_phi_psi

		_mn_topo_phi_psi = _mn_topo_phi_psi_node_group()

		#initialize between_float node group
		def between_float_node_group():
			between_float = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Between Float")

			between_float.color_tag = 'CONVERTER'
			between_float.description = ""

			
			#between_float interface
			#Socket Boolean
			boolean_socket_10 = between_float.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket_10.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_15 = between_float.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket_15.subtype = 'NONE'
			value_socket_15.default_value = 0.0
			value_socket_15.min_value = -3.4028234663852886e+38
			value_socket_15.max_value = 3.4028234663852886e+38
			value_socket_15.attribute_domain = 'POINT'
			
			#Socket Lower
			lower_socket = between_float.interface.new_socket(name = "Lower", in_out='INPUT', socket_type = 'NodeSocketFloat')
			lower_socket.subtype = 'NONE'
			lower_socket.default_value = 0.0
			lower_socket.min_value = -3.4028234663852886e+38
			lower_socket.max_value = 3.4028234663852886e+38
			lower_socket.attribute_domain = 'POINT'
			
			#Socket Upper
			upper_socket = between_float.interface.new_socket(name = "Upper", in_out='INPUT', socket_type = 'NodeSocketFloat')
			upper_socket.subtype = 'NONE'
			upper_socket.default_value = 0.0
			upper_socket.min_value = -3.4028234663852886e+38
			upper_socket.max_value = 3.4028234663852886e+38
			upper_socket.attribute_domain = 'POINT'
			
			
			#initialize between_float nodes
			#node Group Output
			group_output_70 = between_float.nodes.new("NodeGroupOutput")
			group_output_70.name = "Group Output"
			group_output_70.is_active_output = True
			
			#node Group Input
			group_input_69 = between_float.nodes.new("NodeGroupInput")
			group_input_69.name = "Group Input"
			
			#node Compare
			compare_16 = between_float.nodes.new("FunctionNodeCompare")
			compare_16.name = "Compare"
			compare_16.data_type = 'FLOAT'
			compare_16.mode = 'ELEMENT'
			compare_16.operation = 'LESS_EQUAL'
			
			#node Compare.001
			compare_001_9 = between_float.nodes.new("FunctionNodeCompare")
			compare_001_9.name = "Compare.001"
			compare_001_9.data_type = 'FLOAT'
			compare_001_9.mode = 'ELEMENT'
			compare_001_9.operation = 'GREATER_EQUAL'
			
			#node Boolean Math
			boolean_math_16 = between_float.nodes.new("FunctionNodeBooleanMath")
			boolean_math_16.name = "Boolean Math"
			boolean_math_16.operation = 'AND'
			
			
			
			
			#Set locations
			group_output_70.location = (270.0, 0.0)
			group_input_69.location = (-280.0, 0.0)
			compare_16.location = (-80.0, -80.0)
			compare_001_9.location = (-80.0, 80.0)
			boolean_math_16.location = (80.0, 80.0)
			
			#Set dimensions
			group_output_70.width, group_output_70.height = 140.0, 100.0
			group_input_69.width, group_input_69.height = 140.0, 100.0
			compare_16.width, compare_16.height = 140.0, 100.0
			compare_001_9.width, compare_001_9.height = 140.0, 100.0
			boolean_math_16.width, boolean_math_16.height = 140.0, 100.0
			
			#initialize between_float links
			#compare_16.Result -> boolean_math_16.Boolean
			between_float.links.new(compare_16.outputs[0], boolean_math_16.inputs[1])
			#compare_001_9.Result -> boolean_math_16.Boolean
			between_float.links.new(compare_001_9.outputs[0], boolean_math_16.inputs[0])
			#group_input_69.Value -> compare_16.A
			between_float.links.new(group_input_69.outputs[0], compare_16.inputs[2])
			#group_input_69.Value -> compare_001_9.A
			between_float.links.new(group_input_69.outputs[0], compare_001_9.inputs[2])
			#boolean_math_16.Boolean -> group_output_70.Boolean
			between_float.links.new(boolean_math_16.outputs[0], group_output_70.inputs[0])
			#group_input_69.Lower -> compare_001_9.B
			between_float.links.new(group_input_69.outputs[1], compare_001_9.inputs[3])
			#group_input_69.Upper -> compare_16.B
			between_float.links.new(group_input_69.outputs[2], compare_16.inputs[3])
			#group_input_69.Value -> compare_001_9.A
			between_float.links.new(group_input_69.outputs[0], compare_001_9.inputs[0])
			#group_input_69.Value -> compare_16.A
			between_float.links.new(group_input_69.outputs[0], compare_16.inputs[0])
			#group_input_69.Lower -> compare_001_9.B
			between_float.links.new(group_input_69.outputs[1], compare_001_9.inputs[1])
			#group_input_69.Upper -> compare_16.B
			between_float.links.new(group_input_69.outputs[2], compare_16.inputs[1])
			return between_float

		between_float = between_float_node_group()

		#initialize helix_detect node group
		def helix_detect_node_group():
			helix_detect = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Helix Detect")

			helix_detect.color_tag = 'NONE'
			helix_detect.description = ""

			
			#helix_detect interface
			#Socket Boolean
			boolean_socket_11 = helix_detect.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket_11.attribute_domain = 'POINT'
			
			#Socket Helix Size
			helix_size_socket = helix_detect.interface.new_socket(name = "Helix Size", in_out='INPUT', socket_type = 'NodeSocketInt')
			helix_size_socket.subtype = 'NONE'
			helix_size_socket.default_value = 3
			helix_size_socket.min_value = -2147483648
			helix_size_socket.max_value = 2147483647
			helix_size_socket.attribute_domain = 'POINT'
			
			
			#initialize helix_detect nodes
			#node Group Output
			group_output_71 = helix_detect.nodes.new("NodeGroupOutput")
			group_output_71.name = "Group Output"
			group_output_71.is_active_output = True
			
			#node Group Input
			group_input_70 = helix_detect.nodes.new("NodeGroupInput")
			group_input_70.name = "Group Input"
			
			#node Group.003
			group_003_5 = helix_detect.nodes.new("GeometryNodeGroup")
			group_003_5.name = "Group.003"
			group_003_5.node_tree = hbond_backbone_check
			#Socket_3
			group_003_5.inputs[0].default_value = 0
			#Socket_5
			group_003_5.inputs[1].default_value = 0
			#Socket_0
			group_003_5.inputs[2].default_value = 0
			
			#node Group.017
			group_017_1 = helix_detect.nodes.new("GeometryNodeGroup")
			group_017_1.name = "Group.017"
			group_017_1.node_tree = boolean_run_fill
			
			#node Math
			math_21 = helix_detect.nodes.new("ShaderNodeMath")
			math_21.name = "Math"
			math_21.operation = 'MULTIPLY'
			math_21.use_clamp = False
			#Value_001
			math_21.inputs[1].default_value = -1.0
			
			#node Reroute
			reroute_20 = helix_detect.nodes.new("NodeReroute")
			reroute_20.name = "Reroute"
			#node Group
			group_25 = helix_detect.nodes.new("GeometryNodeGroup")
			group_25.name = "Group"
			group_25.node_tree = offset_boolean
			#Socket_1
			group_25.inputs[0].default_value = 0
			#Socket_3
			group_25.inputs[2].default_value = -1
			
			#node Boolean Math
			boolean_math_17 = helix_detect.nodes.new("FunctionNodeBooleanMath")
			boolean_math_17.name = "Boolean Math"
			boolean_math_17.operation = 'AND'
			
			#node Boolean Math.001
			boolean_math_001_13 = helix_detect.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_13.name = "Boolean Math.001"
			boolean_math_001_13.operation = 'OR'
			
			#node Group.001
			group_001_13 = helix_detect.nodes.new("GeometryNodeGroup")
			group_001_13.name = "Group.001"
			group_001_13.node_tree = offset_boolean
			#Socket_1
			group_001_13.inputs[0].default_value = 0
			
			#node Frame
			frame_7 = helix_detect.nodes.new("NodeFrame")
			frame_7.label = "Look to see if bonded with i - n residue, being end of helix"
			frame_7.name = "Frame"
			frame_7.label_size = 20
			frame_7.shrink = True
			
			#node Frame.001
			frame_001_3 = helix_detect.nodes.new("NodeFrame")
			frame_001_3.label = "i and i-1 are both Hbonded n residues ahead (i..i+n are helix)"
			frame_001_3.name = "Frame.001"
			frame_001_3.label_size = 20
			frame_001_3.shrink = True
			
			#node Frame.002
			frame_002_3 = helix_detect.nodes.new("NodeFrame")
			frame_002_3.label = "Assign to in-between residues"
			frame_002_3.name = "Frame.002"
			frame_002_3.label_size = 20
			frame_002_3.shrink = True
			
			#node Group.002
			group_002_6 = helix_detect.nodes.new("GeometryNodeGroup")
			group_002_6.name = "Group.002"
			group_002_6.node_tree = _mn_topo_phi_psi
			#Socket_11
			group_002_6.inputs[0].default_value = 'Phi'
			
			#node Boolean Math.003
			boolean_math_003_6 = helix_detect.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003_6.name = "Boolean Math.003"
			boolean_math_003_6.operation = 'AND'
			
			#node Group.004
			group_004_3 = helix_detect.nodes.new("GeometryNodeGroup")
			group_004_3.name = "Group.004"
			group_004_3.node_tree = _mn_topo_phi_psi
			#Socket_11
			group_004_3.inputs[0].default_value = 'Psi'
			
			#node Group.005
			group_005_4 = helix_detect.nodes.new("GeometryNodeGroup")
			group_005_4.name = "Group.005"
			group_005_4.node_tree = between_float
			#Socket_2
			group_005_4.inputs[1].default_value = -120.0
			#Socket_3
			group_005_4.inputs[2].default_value = 45.0
			
			#node Math.002
			math_002_6 = helix_detect.nodes.new("ShaderNodeMath")
			math_002_6.name = "Math.002"
			math_002_6.operation = 'DEGREES'
			math_002_6.use_clamp = False
			
			#node Group.006
			group_006_3 = helix_detect.nodes.new("GeometryNodeGroup")
			group_006_3.name = "Group.006"
			group_006_3.node_tree = between_float
			#Socket_2
			group_006_3.inputs[1].default_value = -180.0
			#Socket_3
			group_006_3.inputs[2].default_value = 10.0
			
			#node Math.003
			math_003_5 = helix_detect.nodes.new("ShaderNodeMath")
			math_003_5.name = "Math.003"
			math_003_5.operation = 'DEGREES'
			math_003_5.use_clamp = False
			
			#node Boolean Math.002
			boolean_math_002_11 = helix_detect.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_11.name = "Boolean Math.002"
			boolean_math_002_11.operation = 'AND'
			
			#node Frame.003
			frame_003_3 = helix_detect.nodes.new("NodeFrame")
			frame_003_3.label = "extra dihedral check, to discard turns in helix-turn-helix"
			frame_003_3.name = "Frame.003"
			frame_003_3.label_size = 20
			frame_003_3.shrink = True
			
			
			
			#Set parents
			group_003_5.parent = frame_001_3
			group_017_1.parent = frame_002_3
			group_25.parent = frame_001_3
			boolean_math_17.parent = frame_001_3
			group_001_13.parent = frame_7
			group_002_6.parent = frame_003_3
			group_004_3.parent = frame_003_3
			group_005_4.parent = frame_003_3
			math_002_6.parent = frame_003_3
			group_006_3.parent = frame_003_3
			math_003_5.parent = frame_003_3
			boolean_math_002_11.parent = frame_003_3
			
			#Set locations
			group_output_71.location = (680.0, 180.0)
			group_input_70.location = (-800.0, -260.0)
			group_003_5.location = (-500.0, 100.0)
			group_017_1.location = (320.0, -20.0)
			math_21.location = (-300.0, -180.0)
			reroute_20.location = (-540.0, -200.0)
			group_25.location = (-500.0, 240.0)
			boolean_math_17.location = (-340.0, 240.0)
			boolean_math_001_13.location = (-40.0, 240.0)
			group_001_13.location = (-40.0, 20.0)
			frame_7.location = (-10.0, -20.0)
			frame_001_3.location = (10.0, 40.0)
			frame_002_3.location = (-30.0, 200.0)
			group_002_6.location = (254.93621826171875, -98.54428100585938)
			boolean_math_003_6.location = (500.0, 180.0)
			group_004_3.location = (254.93621826171875, -378.5442810058594)
			group_005_4.location = (574.9362182617188, -98.54428100585938)
			math_002_6.location = (414.93621826171875, -98.54428100585938)
			group_006_3.location = (574.9362182617188, -378.5442810058594)
			math_003_5.location = (414.93621826171875, -378.5442810058594)
			boolean_math_002_11.location = (774.9362182617188, -98.54428100585938)
			frame_003_3.location = (35.0, 99.0)
			
			#Set dimensions
			group_output_71.width, group_output_71.height = 140.0, 100.0
			group_input_70.width, group_input_70.height = 140.0, 100.0
			group_003_5.width, group_003_5.height = 140.0, 100.0
			group_017_1.width, group_017_1.height = 144.84217834472656, 100.0
			math_21.width, math_21.height = 140.0, 100.0
			reroute_20.width, reroute_20.height = 16.0, 100.0
			group_25.width, group_25.height = 140.0, 100.0
			boolean_math_17.width, boolean_math_17.height = 140.0, 100.0
			boolean_math_001_13.width, boolean_math_001_13.height = 140.0, 100.0
			group_001_13.width, group_001_13.height = 140.0, 100.0
			frame_7.width, frame_7.height = 200.0, 187.0
			frame_001_3.width, frame_001_3.height = 360.0, 474.0
			frame_002_3.width, frame_002_3.height = 204.8421630859375, 165.0
			group_002_6.width, group_002_6.height = 140.0, 100.0
			boolean_math_003_6.width, boolean_math_003_6.height = 140.0, 100.0
			group_004_3.width, group_004_3.height = 140.0, 100.0
			group_005_4.width, group_005_4.height = 176.237548828125, 100.0
			math_002_6.width, math_002_6.height = 140.0, 100.0
			group_006_3.width, group_006_3.height = 176.237548828125, 100.0
			math_003_5.width, math_003_5.height = 140.0, 100.0
			boolean_math_002_11.width, boolean_math_002_11.height = 140.0, 100.0
			frame_003_3.width, frame_003_3.height = 720.0, 602.0
			
			#initialize helix_detect links
			#group_input_70.Helix Size -> math_21.Value
			helix_detect.links.new(group_input_70.outputs[0], math_21.inputs[0])
			#group_input_70.Helix Size -> reroute_20.Input
			helix_detect.links.new(group_input_70.outputs[0], reroute_20.inputs[0])
			#reroute_20.Output -> group_003_5.NH Offset
			helix_detect.links.new(reroute_20.outputs[0], group_003_5.inputs[3])
			#group_003_5.Is Bonded -> group_25.Boolean
			helix_detect.links.new(group_003_5.outputs[0], group_25.inputs[1])
			#group_25.Boolean -> boolean_math_17.Boolean
			helix_detect.links.new(group_25.outputs[0], boolean_math_17.inputs[0])
			#group_003_5.Is Bonded -> boolean_math_17.Boolean
			helix_detect.links.new(group_003_5.outputs[0], boolean_math_17.inputs[1])
			#boolean_math_001_13.Boolean -> group_017_1.Boolean
			helix_detect.links.new(boolean_math_001_13.outputs[0], group_017_1.inputs[0])
			#boolean_math_17.Boolean -> boolean_math_001_13.Boolean
			helix_detect.links.new(boolean_math_17.outputs[0], boolean_math_001_13.inputs[0])
			#boolean_math_17.Boolean -> group_001_13.Boolean
			helix_detect.links.new(boolean_math_17.outputs[0], group_001_13.inputs[1])
			#group_001_13.Boolean -> boolean_math_001_13.Boolean
			helix_detect.links.new(group_001_13.outputs[0], boolean_math_001_13.inputs[1])
			#math_21.Value -> group_001_13.Offset
			helix_detect.links.new(math_21.outputs[0], group_001_13.inputs[2])
			#reroute_20.Output -> group_017_1.Fill Size
			helix_detect.links.new(reroute_20.outputs[0], group_017_1.inputs[1])
			#group_017_1.Boolean -> boolean_math_003_6.Boolean
			helix_detect.links.new(group_017_1.outputs[0], boolean_math_003_6.inputs[0])
			#boolean_math_003_6.Boolean -> group_output_71.Boolean
			helix_detect.links.new(boolean_math_003_6.outputs[0], group_output_71.inputs[0])
			#boolean_math_002_11.Boolean -> boolean_math_003_6.Boolean
			helix_detect.links.new(boolean_math_002_11.outputs[0], boolean_math_003_6.inputs[1])
			#group_002_6.Angle -> math_002_6.Value
			helix_detect.links.new(group_002_6.outputs[0], math_002_6.inputs[0])
			#math_002_6.Value -> group_005_4.Value
			helix_detect.links.new(math_002_6.outputs[0], group_005_4.inputs[0])
			#math_003_5.Value -> group_006_3.Value
			helix_detect.links.new(math_003_5.outputs[0], group_006_3.inputs[0])
			#group_004_3.Angle -> math_003_5.Value
			helix_detect.links.new(group_004_3.outputs[0], math_003_5.inputs[0])
			#group_005_4.Boolean -> boolean_math_002_11.Boolean
			helix_detect.links.new(group_005_4.outputs[0], boolean_math_002_11.inputs[0])
			#group_006_3.Boolean -> boolean_math_002_11.Boolean
			helix_detect.links.new(group_006_3.outputs[0], boolean_math_002_11.inputs[1])
			return helix_detect

		helix_detect = helix_detect_node_group()

		#initialize _mn_topo_calc_helix node group
		def _mn_topo_calc_helix_node_group():
			_mn_topo_calc_helix = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_topo_calc_helix")

			_mn_topo_calc_helix.color_tag = 'NONE'
			_mn_topo_calc_helix.description = ""

			
			#_mn_topo_calc_helix interface
			#Socket Is Helix
			is_helix_socket_1 = _mn_topo_calc_helix.interface.new_socket(name = "Is Helix", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_helix_socket_1.attribute_domain = 'POINT'
			
			#Socket Bonded Index
			bonded_index_socket = _mn_topo_calc_helix.interface.new_socket(name = "Bonded Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			bonded_index_socket.subtype = 'NONE'
			bonded_index_socket.default_value = 0
			bonded_index_socket.min_value = -2147483648
			bonded_index_socket.max_value = 2147483647
			bonded_index_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_topo_calc_helix nodes
			#node Group Output
			group_output_72 = _mn_topo_calc_helix.nodes.new("NodeGroupOutput")
			group_output_72.name = "Group Output"
			group_output_72.is_active_output = True
			
			#node Group.001
			group_001_14 = _mn_topo_calc_helix.nodes.new("GeometryNodeGroup")
			group_001_14.name = "Group.001"
			group_001_14.node_tree = boolean_run_mask
			#Socket_2
			group_001_14.inputs[1].default_value = 0
			#Socket_3
			group_001_14.inputs[2].default_value = 5
			#Socket_6
			group_001_14.inputs[3].default_value = 0
			
			#node Boolean Math.004
			boolean_math_004_7 = _mn_topo_calc_helix.nodes.new("FunctionNodeBooleanMath")
			boolean_math_004_7.name = "Boolean Math.004"
			boolean_math_004_7.operation = 'OR'
			
			#node Boolean Math.005
			boolean_math_005_3 = _mn_topo_calc_helix.nodes.new("FunctionNodeBooleanMath")
			boolean_math_005_3.name = "Boolean Math.005"
			boolean_math_005_3.operation = 'OR'
			
			#node Group
			group_26 = _mn_topo_calc_helix.nodes.new("GeometryNodeGroup")
			group_26.name = "Group"
			group_26.node_tree = helix_detect
			#Socket_1
			group_26.inputs[0].default_value = 3
			
			#node Group.002
			group_002_7 = _mn_topo_calc_helix.nodes.new("GeometryNodeGroup")
			group_002_7.name = "Group.002"
			group_002_7.node_tree = helix_detect
			#Socket_1
			group_002_7.inputs[0].default_value = 4
			
			#node Group.003
			group_003_6 = _mn_topo_calc_helix.nodes.new("GeometryNodeGroup")
			group_003_6.name = "Group.003"
			group_003_6.node_tree = helix_detect
			#Socket_1
			group_003_6.inputs[0].default_value = 5
			
			#node Group.004
			group_004_4 = _mn_topo_calc_helix.nodes.new("GeometryNodeGroup")
			group_004_4.name = "Group.004"
			group_004_4.node_tree = offset_integer
			#Socket_1
			group_004_4.inputs[0].default_value = 0
			#Socket_2
			group_004_4.inputs[2].default_value = 3
			
			#node Index
			index_7 = _mn_topo_calc_helix.nodes.new("GeometryNodeInputIndex")
			index_7.name = "Index"
			
			#node Switch
			switch_17 = _mn_topo_calc_helix.nodes.new("GeometryNodeSwitch")
			switch_17.name = "Switch"
			switch_17.input_type = 'INT'
			#False
			switch_17.inputs[1].default_value = -1
			
			#node Switch.001
			switch_001_4 = _mn_topo_calc_helix.nodes.new("GeometryNodeSwitch")
			switch_001_4.name = "Switch.001"
			switch_001_4.input_type = 'INT'
			
			#node Group.005
			group_005_5 = _mn_topo_calc_helix.nodes.new("GeometryNodeGroup")
			group_005_5.name = "Group.005"
			group_005_5.node_tree = offset_integer
			#Socket_1
			group_005_5.inputs[0].default_value = 0
			#Socket_2
			group_005_5.inputs[2].default_value = 4
			
			#node Switch.002
			switch_002_3 = _mn_topo_calc_helix.nodes.new("GeometryNodeSwitch")
			switch_002_3.name = "Switch.002"
			switch_002_3.input_type = 'INT'
			
			#node Group.006
			group_006_4 = _mn_topo_calc_helix.nodes.new("GeometryNodeGroup")
			group_006_4.name = "Group.006"
			group_006_4.node_tree = offset_integer
			#Socket_1
			group_006_4.inputs[0].default_value = 0
			#Socket_2
			group_006_4.inputs[2].default_value = 5
			
			#node Frame
			frame_8 = _mn_topo_calc_helix.nodes.new("NodeFrame")
			frame_8.label = "If part of a helix, return the Index of the CA that is bonded"
			frame_8.name = "Frame"
			frame_8.label_size = 20
			frame_8.shrink = True
			
			
			
			#Set parents
			group_004_4.parent = frame_8
			index_7.parent = frame_8
			switch_17.parent = frame_8
			switch_001_4.parent = frame_8
			group_005_5.parent = frame_8
			switch_002_3.parent = frame_8
			group_006_4.parent = frame_8
			
			#Set locations
			group_output_72.location = (900.0, 620.0)
			group_001_14.location = (660.0, 620.0)
			boolean_math_004_7.location = (320.0, 620.0)
			boolean_math_005_3.location = (500.0, 620.0)
			group_26.location = (137.64556884765625, 620.0)
			group_002_7.location = (140.0, 500.0)
			group_003_6.location = (320.0, 480.0)
			group_004_4.location = (320.0, 840.0)
			index_7.location = (140.0, 820.0)
			switch_17.location = (320.0, 1000.0)
			switch_001_4.location = (480.0, 1000.0)
			group_005_5.location = (480.0, 840.0)
			switch_002_3.location = (640.0, 1000.0)
			group_006_4.location = (640.0, 840.0)
			frame_8.location = (0.0, 0.0)
			
			#Set dimensions
			group_output_72.width, group_output_72.height = 140.0, 100.0
			group_001_14.width, group_001_14.height = 208.096435546875, 100.0
			boolean_math_004_7.width, boolean_math_004_7.height = 140.0, 100.0
			boolean_math_005_3.width, boolean_math_005_3.height = 140.0, 100.0
			group_26.width, group_26.height = 142.35443115234375, 100.0
			group_002_7.width, group_002_7.height = 140.0, 100.0
			group_003_6.width, group_003_6.height = 140.0, 100.0
			group_004_4.width, group_004_4.height = 140.0, 100.0
			index_7.width, index_7.height = 140.0, 100.0
			switch_17.width, switch_17.height = 140.0, 100.0
			switch_001_4.width, switch_001_4.height = 140.0, 100.0
			group_005_5.width, group_005_5.height = 140.0, 100.0
			switch_002_3.width, switch_002_3.height = 140.0, 100.0
			group_006_4.width, group_006_4.height = 140.0, 100.0
			frame_8.width, frame_8.height = 700.0, 372.0
			
			#initialize _mn_topo_calc_helix links
			#boolean_math_004_7.Boolean -> boolean_math_005_3.Boolean
			_mn_topo_calc_helix.links.new(boolean_math_004_7.outputs[0], boolean_math_005_3.inputs[0])
			#group_001_14.Boolean -> group_output_72.Is Helix
			_mn_topo_calc_helix.links.new(group_001_14.outputs[0], group_output_72.inputs[0])
			#group_26.Boolean -> boolean_math_004_7.Boolean
			_mn_topo_calc_helix.links.new(group_26.outputs[0], boolean_math_004_7.inputs[0])
			#group_002_7.Boolean -> boolean_math_004_7.Boolean
			_mn_topo_calc_helix.links.new(group_002_7.outputs[0], boolean_math_004_7.inputs[1])
			#group_003_6.Boolean -> boolean_math_005_3.Boolean
			_mn_topo_calc_helix.links.new(group_003_6.outputs[0], boolean_math_005_3.inputs[1])
			#boolean_math_005_3.Boolean -> group_001_14.Boolean
			_mn_topo_calc_helix.links.new(boolean_math_005_3.outputs[0], group_001_14.inputs[0])
			#index_7.Index -> group_004_4.Value
			_mn_topo_calc_helix.links.new(index_7.outputs[0], group_004_4.inputs[1])
			#group_004_4.Value -> switch_17.True
			_mn_topo_calc_helix.links.new(group_004_4.outputs[0], switch_17.inputs[2])
			#group_26.Boolean -> switch_17.Switch
			_mn_topo_calc_helix.links.new(group_26.outputs[0], switch_17.inputs[0])
			#switch_17.Output -> switch_001_4.False
			_mn_topo_calc_helix.links.new(switch_17.outputs[0], switch_001_4.inputs[1])
			#group_002_7.Boolean -> switch_001_4.Switch
			_mn_topo_calc_helix.links.new(group_002_7.outputs[0], switch_001_4.inputs[0])
			#group_005_5.Value -> switch_001_4.True
			_mn_topo_calc_helix.links.new(group_005_5.outputs[0], switch_001_4.inputs[2])
			#switch_001_4.Output -> switch_002_3.False
			_mn_topo_calc_helix.links.new(switch_001_4.outputs[0], switch_002_3.inputs[1])
			#group_003_6.Boolean -> switch_002_3.Switch
			_mn_topo_calc_helix.links.new(group_003_6.outputs[0], switch_002_3.inputs[0])
			#index_7.Index -> group_005_5.Value
			_mn_topo_calc_helix.links.new(index_7.outputs[0], group_005_5.inputs[1])
			#index_7.Index -> group_006_4.Value
			_mn_topo_calc_helix.links.new(index_7.outputs[0], group_006_4.inputs[1])
			#group_006_4.Value -> switch_002_3.True
			_mn_topo_calc_helix.links.new(group_006_4.outputs[0], switch_002_3.inputs[2])
			#switch_002_3.Output -> group_output_72.Bonded Index
			_mn_topo_calc_helix.links.new(switch_002_3.outputs[0], group_output_72.inputs[1])
			return _mn_topo_calc_helix

		_mn_topo_calc_helix = _mn_topo_calc_helix_node_group()

		#initialize self_sample_proximity node group
		def self_sample_proximity_node_group():
			self_sample_proximity = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Self Sample Proximity")

			self_sample_proximity.color_tag = 'NONE'
			self_sample_proximity.description = ""

			
			#self_sample_proximity interface
			#Socket Closest Index
			closest_index_socket = self_sample_proximity.interface.new_socket(name = "Closest Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			closest_index_socket.subtype = 'NONE'
			closest_index_socket.default_value = 0
			closest_index_socket.min_value = -2147483648
			closest_index_socket.max_value = 2147483647
			closest_index_socket.attribute_domain = 'POINT'
			
			#Socket Input
			input_socket_5 = self_sample_proximity.interface.new_socket(name = "Input", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			input_socket_5.attribute_domain = 'POINT'
			
			#Socket Target Position
			target_position_socket = self_sample_proximity.interface.new_socket(name = "Target Position", in_out='INPUT', socket_type = 'NodeSocketVector')
			target_position_socket.subtype = 'NONE'
			target_position_socket.default_value = (0.0, 0.0, 0.0)
			target_position_socket.min_value = -3.4028234663852886e+38
			target_position_socket.max_value = 3.4028234663852886e+38
			target_position_socket.attribute_domain = 'POINT'
			
			#Socket Self Position
			self_position_socket = self_sample_proximity.interface.new_socket(name = "Self Position", in_out='INPUT', socket_type = 'NodeSocketVector')
			self_position_socket.subtype = 'NONE'
			self_position_socket.default_value = (0.0, 0.0, 0.0)
			self_position_socket.min_value = -3.4028234663852886e+38
			self_position_socket.max_value = 3.4028234663852886e+38
			self_position_socket.attribute_domain = 'POINT'
			
			
			#initialize self_sample_proximity nodes
			#node Group Output
			group_output_73 = self_sample_proximity.nodes.new("NodeGroupOutput")
			group_output_73.name = "Group Output"
			group_output_73.is_active_output = True
			
			#node Group Input
			group_input_71 = self_sample_proximity.nodes.new("NodeGroupInput")
			group_input_71.name = "Group Input"
			
			#node Set Position.002
			set_position_002_2 = self_sample_proximity.nodes.new("GeometryNodeSetPosition")
			set_position_002_2.name = "Set Position.002"
			#Selection
			set_position_002_2.inputs[1].default_value = True
			#Offset
			set_position_002_2.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Sample Nearest.001
			sample_nearest_001_1 = self_sample_proximity.nodes.new("GeometryNodeSampleNearest")
			sample_nearest_001_1.name = "Sample Nearest.001"
			sample_nearest_001_1.domain = 'POINT'
			
			
			
			
			#Set locations
			group_output_73.location = (4.068901062011719, 95.01506042480469)
			group_input_71.location = (-640.0, 20.0)
			set_position_002_2.location = (-380.0, -20.0)
			sample_nearest_001_1.location = (-220.0, -20.0)
			
			#Set dimensions
			group_output_73.width, group_output_73.height = 140.0, 100.0
			group_input_71.width, group_input_71.height = 140.0, 100.0
			set_position_002_2.width, set_position_002_2.height = 140.0, 100.0
			sample_nearest_001_1.width, sample_nearest_001_1.height = 140.0, 100.0
			
			#initialize self_sample_proximity links
			#group_input_71.Input -> set_position_002_2.Geometry
			self_sample_proximity.links.new(group_input_71.outputs[0], set_position_002_2.inputs[0])
			#set_position_002_2.Geometry -> sample_nearest_001_1.Geometry
			self_sample_proximity.links.new(set_position_002_2.outputs[0], sample_nearest_001_1.inputs[0])
			#group_input_71.Target Position -> set_position_002_2.Position
			self_sample_proximity.links.new(group_input_71.outputs[1], set_position_002_2.inputs[2])
			#group_input_71.Self Position -> sample_nearest_001_1.Sample Position
			self_sample_proximity.links.new(group_input_71.outputs[2], sample_nearest_001_1.inputs[1])
			#sample_nearest_001_1.Index -> group_output_73.Closest Index
			self_sample_proximity.links.new(sample_nearest_001_1.outputs[0], group_output_73.inputs[0])
			return self_sample_proximity

		self_sample_proximity = self_sample_proximity_node_group()

		#initialize hbond_backbone_check_backup node group
		def hbond_backbone_check_backup_node_group():
			hbond_backbone_check_backup = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "HBond Backbone Check_backup")

			hbond_backbone_check_backup.color_tag = 'NONE'
			hbond_backbone_check_backup.description = ""

			
			#hbond_backbone_check_backup interface
			#Socket Is Bonded
			is_bonded_socket_2 = hbond_backbone_check_backup.interface.new_socket(name = "Is Bonded", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_bonded_socket_2.attribute_domain = 'POINT'
			
			#Socket Bond Energy
			bond_energy_socket_2 = hbond_backbone_check_backup.interface.new_socket(name = "Bond Energy", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			bond_energy_socket_2.subtype = 'NONE'
			bond_energy_socket_2.default_value = 0.0
			bond_energy_socket_2.min_value = -3.4028234663852886e+38
			bond_energy_socket_2.max_value = 3.4028234663852886e+38
			bond_energy_socket_2.attribute_domain = 'POINT'
			
			#Socket H->O
			h__o_socket_1 = hbond_backbone_check_backup.interface.new_socket(name = "H->O", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			h__o_socket_1.subtype = 'NONE'
			h__o_socket_1.default_value = (0.0, 0.0, 0.0)
			h__o_socket_1.min_value = -3.4028234663852886e+38
			h__o_socket_1.max_value = 3.4028234663852886e+38
			h__o_socket_1.attribute_domain = 'POINT'
			
			#Panel CO
			co_panel_1 = hbond_backbone_check_backup.interface.new_panel("CO")
			#Socket CO Index
			co_index_socket_1 = hbond_backbone_check_backup.interface.new_socket(name = "CO Index", in_out='INPUT', socket_type = 'NodeSocketInt', parent = co_panel_1)
			co_index_socket_1.subtype = 'NONE'
			co_index_socket_1.default_value = 0
			co_index_socket_1.min_value = 0
			co_index_socket_1.max_value = 2147483647
			co_index_socket_1.attribute_domain = 'POINT'
			
			#Socket CO Offset
			co_offset_socket_1 = hbond_backbone_check_backup.interface.new_socket(name = "CO Offset", in_out='INPUT', socket_type = 'NodeSocketInt', parent = co_panel_1)
			co_offset_socket_1.subtype = 'NONE'
			co_offset_socket_1.default_value = 0
			co_offset_socket_1.min_value = -2147483648
			co_offset_socket_1.max_value = 2147483647
			co_offset_socket_1.attribute_domain = 'POINT'
			
			
			#Panel NH
			nh_panel_1 = hbond_backbone_check_backup.interface.new_panel("NH")
			#Socket NH Index
			nh_index_socket_1 = hbond_backbone_check_backup.interface.new_socket(name = "NH Index", in_out='INPUT', socket_type = 'NodeSocketInt', parent = nh_panel_1)
			nh_index_socket_1.subtype = 'NONE'
			nh_index_socket_1.default_value = 0
			nh_index_socket_1.min_value = 0
			nh_index_socket_1.max_value = 2147483647
			nh_index_socket_1.attribute_domain = 'POINT'
			
			#Socket NH Offset
			nh_offset_socket_1 = hbond_backbone_check_backup.interface.new_socket(name = "NH Offset", in_out='INPUT', socket_type = 'NodeSocketInt', parent = nh_panel_1)
			nh_offset_socket_1.subtype = 'NONE'
			nh_offset_socket_1.default_value = 0
			nh_offset_socket_1.min_value = -2147483648
			nh_offset_socket_1.max_value = 2147483647
			nh_offset_socket_1.attribute_domain = 'POINT'
			
			
			
			#initialize hbond_backbone_check_backup nodes
			#node Group Output
			group_output_74 = hbond_backbone_check_backup.nodes.new("NodeGroupOutput")
			group_output_74.name = "Group Output"
			group_output_74.is_active_output = True
			
			#node Group Input
			group_input_72 = hbond_backbone_check_backup.nodes.new("NodeGroupInput")
			group_input_72.name = "Group Input"
			
			#node Group.008
			group_008_5 = hbond_backbone_check_backup.nodes.new("GeometryNodeGroup")
			group_008_5.name = "Group.008"
			group_008_5.node_tree = hbond_energy
			
			#node Group.009
			group_009_6 = hbond_backbone_check_backup.nodes.new("GeometryNodeGroup")
			group_009_6.name = "Group.009"
			group_009_6.node_tree = mn_topo_backbone
			#Socket_3
			group_009_6.inputs[0].default_value = 0
			
			#node Evaluate at Index
			evaluate_at_index_8 = hbond_backbone_check_backup.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_8.name = "Evaluate at Index"
			evaluate_at_index_8.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_8.domain = 'POINT'
			
			#node Evaluate at Index.001
			evaluate_at_index_001_6 = hbond_backbone_check_backup.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001_6.name = "Evaluate at Index.001"
			evaluate_at_index_001_6.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_001_6.domain = 'POINT'
			
			#node Evaluate at Index.002
			evaluate_at_index_002_3 = hbond_backbone_check_backup.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_002_3.name = "Evaluate at Index.002"
			evaluate_at_index_002_3.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_002_3.domain = 'POINT'
			
			#node Evaluate at Index.003
			evaluate_at_index_003_3 = hbond_backbone_check_backup.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_003_3.name = "Evaluate at Index.003"
			evaluate_at_index_003_3.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_003_3.domain = 'POINT'
			
			#node Math
			math_22 = hbond_backbone_check_backup.nodes.new("ShaderNodeMath")
			math_22.name = "Math"
			math_22.operation = 'ADD'
			math_22.use_clamp = False
			
			#node Math.001
			math_001_12 = hbond_backbone_check_backup.nodes.new("ShaderNodeMath")
			math_001_12.name = "Math.001"
			math_001_12.operation = 'ADD'
			math_001_12.use_clamp = False
			
			#node Math.002
			math_002_7 = hbond_backbone_check_backup.nodes.new("ShaderNodeMath")
			math_002_7.name = "Math.002"
			math_002_7.operation = 'SUBTRACT'
			math_002_7.use_clamp = False
			
			#node Math.003
			math_003_6 = hbond_backbone_check_backup.nodes.new("ShaderNodeMath")
			math_003_6.name = "Math.003"
			math_003_6.operation = 'ABSOLUTE'
			math_003_6.use_clamp = False
			
			#node Compare
			compare_17 = hbond_backbone_check_backup.nodes.new("FunctionNodeCompare")
			compare_17.name = "Compare"
			compare_17.data_type = 'FLOAT'
			compare_17.mode = 'ELEMENT'
			compare_17.operation = 'GREATER_THAN'
			
			#node Integer
			integer_6 = hbond_backbone_check_backup.nodes.new("FunctionNodeInputInt")
			integer_6.name = "Integer"
			integer_6.integer = 1
			
			#node Frame
			frame_9 = hbond_backbone_check_backup.nodes.new("NodeFrame")
			frame_9.label = "Check not bonded to +/- residues"
			frame_9.name = "Frame"
			frame_9.label_size = 20
			frame_9.shrink = True
			
			#node Switch
			switch_18 = hbond_backbone_check_backup.nodes.new("GeometryNodeSwitch")
			switch_18.name = "Switch"
			switch_18.input_type = 'BOOLEAN'
			#False
			switch_18.inputs[1].default_value = False
			
			#node Compare.001
			compare_001_10 = hbond_backbone_check_backup.nodes.new("FunctionNodeCompare")
			compare_001_10.name = "Compare.001"
			compare_001_10.data_type = 'FLOAT'
			compare_001_10.mode = 'ELEMENT'
			compare_001_10.operation = 'LESS_THAN'
			
			#node Vector Math
			vector_math_12 = hbond_backbone_check_backup.nodes.new("ShaderNodeVectorMath")
			vector_math_12.name = "Vector Math"
			vector_math_12.operation = 'LENGTH'
			
			#node Group
			group_27 = hbond_backbone_check_backup.nodes.new("GeometryNodeGroup")
			group_27.name = "Group"
			group_27.node_tree = mn_units
			#Input_1
			group_27.inputs[0].default_value = 3.0
			
			
			
			#Set parents
			math_002_7.parent = frame_9
			math_003_6.parent = frame_9
			compare_17.parent = frame_9
			integer_6.parent = frame_9
			
			#Set locations
			group_output_74.location = (820.0, 240.0)
			group_input_72.location = (-680.0, 140.0)
			group_008_5.location = (224.2731170654297, 240.0)
			group_009_6.location = (-480.0, 460.0)
			evaluate_at_index_8.location = (-20.0, 40.0)
			evaluate_at_index_001_6.location = (-20.0, -120.0)
			evaluate_at_index_002_3.location = (-20.0, 400.0)
			evaluate_at_index_003_3.location = (-20.0, 240.0)
			math_22.location = (-480.0, 240.0)
			math_001_12.location = (-480.0, 80.0)
			math_002_7.location = (70.0, 640.0)
			math_003_6.location = (240.0, 640.0)
			compare_17.location = (420.0, 640.0)
			integer_6.location = (240.0, 500.0)
			frame_9.location = (-70.0, 40.0)
			switch_18.location = (620.0, 340.0)
			compare_001_10.location = (520.0, 140.0)
			vector_math_12.location = (260.0, 20.0)
			group_27.location = (520.0, -20.0)
			
			#Set dimensions
			group_output_74.width, group_output_74.height = 140.0, 100.0
			group_input_72.width, group_input_72.height = 140.0, 100.0
			group_008_5.width, group_008_5.height = 184.92144775390625, 100.0
			group_009_6.width, group_009_6.height = 140.0, 100.0
			evaluate_at_index_8.width, evaluate_at_index_8.height = 140.0, 100.0
			evaluate_at_index_001_6.width, evaluate_at_index_001_6.height = 140.0, 100.0
			evaluate_at_index_002_3.width, evaluate_at_index_002_3.height = 140.0, 100.0
			evaluate_at_index_003_3.width, evaluate_at_index_003_3.height = 140.0, 100.0
			math_22.width, math_22.height = 140.0, 100.0
			math_001_12.width, math_001_12.height = 140.0, 100.0
			math_002_7.width, math_002_7.height = 140.0, 100.0
			math_003_6.width, math_003_6.height = 140.0, 100.0
			compare_17.width, compare_17.height = 140.0, 100.0
			integer_6.width, integer_6.height = 140.0, 100.0
			frame_9.width, frame_9.height = 550.0, 285.0
			switch_18.width, switch_18.height = 140.0, 100.0
			compare_001_10.width, compare_001_10.height = 140.0, 100.0
			vector_math_12.width, vector_math_12.height = 140.0, 100.0
			group_27.width, group_27.height = 140.0, 100.0
			
			#initialize hbond_backbone_check_backup links
			#evaluate_at_index_001_6.Value -> group_008_5.H
			hbond_backbone_check_backup.links.new(evaluate_at_index_001_6.outputs[0], group_008_5.inputs[3])
			#evaluate_at_index_8.Value -> group_008_5.N
			hbond_backbone_check_backup.links.new(evaluate_at_index_8.outputs[0], group_008_5.inputs[2])
			#evaluate_at_index_002_3.Value -> group_008_5.O
			hbond_backbone_check_backup.links.new(evaluate_at_index_002_3.outputs[0], group_008_5.inputs[0])
			#math_001_12.Value -> evaluate_at_index_001_6.Index
			hbond_backbone_check_backup.links.new(math_001_12.outputs[0], evaluate_at_index_001_6.inputs[0])
			#math_001_12.Value -> evaluate_at_index_8.Index
			hbond_backbone_check_backup.links.new(math_001_12.outputs[0], evaluate_at_index_8.inputs[0])
			#evaluate_at_index_003_3.Value -> group_008_5.C
			hbond_backbone_check_backup.links.new(evaluate_at_index_003_3.outputs[0], group_008_5.inputs[1])
			#group_009_6.NH -> evaluate_at_index_001_6.Value
			hbond_backbone_check_backup.links.new(group_009_6.outputs[4], evaluate_at_index_001_6.inputs[1])
			#group_009_6.N -> evaluate_at_index_8.Value
			hbond_backbone_check_backup.links.new(group_009_6.outputs[3], evaluate_at_index_8.inputs[1])
			#group_008_5.Bond Energy -> group_output_74.Bond Energy
			hbond_backbone_check_backup.links.new(group_008_5.outputs[1], group_output_74.inputs[1])
			#group_008_5.Bond Vector -> group_output_74.H->O
			hbond_backbone_check_backup.links.new(group_008_5.outputs[2], group_output_74.inputs[2])
			#group_009_6.O -> evaluate_at_index_002_3.Value
			hbond_backbone_check_backup.links.new(group_009_6.outputs[0], evaluate_at_index_002_3.inputs[1])
			#group_009_6.C -> evaluate_at_index_003_3.Value
			hbond_backbone_check_backup.links.new(group_009_6.outputs[1], evaluate_at_index_003_3.inputs[1])
			#math_22.Value -> evaluate_at_index_002_3.Index
			hbond_backbone_check_backup.links.new(math_22.outputs[0], evaluate_at_index_002_3.inputs[0])
			#math_22.Value -> evaluate_at_index_003_3.Index
			hbond_backbone_check_backup.links.new(math_22.outputs[0], evaluate_at_index_003_3.inputs[0])
			#group_input_72.CO Index -> math_22.Value
			hbond_backbone_check_backup.links.new(group_input_72.outputs[0], math_22.inputs[0])
			#group_input_72.CO Offset -> math_22.Value
			hbond_backbone_check_backup.links.new(group_input_72.outputs[1], math_22.inputs[1])
			#group_input_72.NH Index -> math_001_12.Value
			hbond_backbone_check_backup.links.new(group_input_72.outputs[2], math_001_12.inputs[0])
			#group_input_72.NH Offset -> math_001_12.Value
			hbond_backbone_check_backup.links.new(group_input_72.outputs[3], math_001_12.inputs[1])
			#math_22.Value -> math_002_7.Value
			hbond_backbone_check_backup.links.new(math_22.outputs[0], math_002_7.inputs[0])
			#math_001_12.Value -> math_002_7.Value
			hbond_backbone_check_backup.links.new(math_001_12.outputs[0], math_002_7.inputs[1])
			#math_002_7.Value -> math_003_6.Value
			hbond_backbone_check_backup.links.new(math_002_7.outputs[0], math_003_6.inputs[0])
			#math_003_6.Value -> compare_17.A
			hbond_backbone_check_backup.links.new(math_003_6.outputs[0], compare_17.inputs[0])
			#integer_6.Integer -> compare_17.B
			hbond_backbone_check_backup.links.new(integer_6.outputs[0], compare_17.inputs[1])
			#compare_17.Result -> switch_18.Switch
			hbond_backbone_check_backup.links.new(compare_17.outputs[0], switch_18.inputs[0])
			#group_008_5.Bond Vector -> vector_math_12.Vector
			hbond_backbone_check_backup.links.new(group_008_5.outputs[2], vector_math_12.inputs[0])
			#vector_math_12.Value -> compare_001_10.A
			hbond_backbone_check_backup.links.new(vector_math_12.outputs[1], compare_001_10.inputs[0])
			#group_27.Angstrom -> compare_001_10.B
			hbond_backbone_check_backup.links.new(group_27.outputs[0], compare_001_10.inputs[1])
			#switch_18.Output -> group_output_74.Is Bonded
			hbond_backbone_check_backup.links.new(switch_18.outputs[0], group_output_74.inputs[0])
			#group_008_5.Is Bonded -> switch_18.True
			hbond_backbone_check_backup.links.new(group_008_5.outputs[0], switch_18.inputs[2])
			return hbond_backbone_check_backup

		hbond_backbone_check_backup = hbond_backbone_check_backup_node_group()

		#initialize _hbond_i__j__and_hbond_j__i_ node group
		def _hbond_i__j__and_hbond_j__i__node_group():
			_hbond_i__j__and_hbond_j__i_ = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".HBond(i, j) and HBond(j, i)")

			_hbond_i__j__and_hbond_j__i_.color_tag = 'NONE'
			_hbond_i__j__and_hbond_j__i_.description = ""

			
			#_hbond_i__j__and_hbond_j__i_ interface
			#Socket Boolean
			boolean_socket_12 = _hbond_i__j__and_hbond_j__i_.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket_12.attribute_domain = 'POINT'
			
			#Socket i
			i_socket = _hbond_i__j__and_hbond_j__i_.interface.new_socket(name = "i", in_out='INPUT', socket_type = 'NodeSocketInt')
			i_socket.subtype = 'NONE'
			i_socket.default_value = 0
			i_socket.min_value = 0
			i_socket.max_value = 2147483647
			i_socket.attribute_domain = 'POINT'
			i_socket.hide_value = True
			
			#Socket j
			j_socket = _hbond_i__j__and_hbond_j__i_.interface.new_socket(name = "j", in_out='INPUT', socket_type = 'NodeSocketInt')
			j_socket.subtype = 'NONE'
			j_socket.default_value = 0
			j_socket.min_value = 0
			j_socket.max_value = 2147483647
			j_socket.attribute_domain = 'POINT'
			j_socket.hide_value = True
			
			
			#initialize _hbond_i__j__and_hbond_j__i_ nodes
			#node Group Output
			group_output_75 = _hbond_i__j__and_hbond_j__i_.nodes.new("NodeGroupOutput")
			group_output_75.name = "Group Output"
			group_output_75.is_active_output = True
			
			#node Group Input
			group_input_73 = _hbond_i__j__and_hbond_j__i_.nodes.new("NodeGroupInput")
			group_input_73.name = "Group Input"
			
			#node Group.010
			group_010_2 = _hbond_i__j__and_hbond_j__i_.nodes.new("GeometryNodeGroup")
			group_010_2.name = "Group.010"
			group_010_2.node_tree = hbond_backbone_check
			#Socket_5
			group_010_2.inputs[1].default_value = 0
			#Socket_6
			group_010_2.inputs[3].default_value = 0
			
			#node Group.011
			group_011_3 = _hbond_i__j__and_hbond_j__i_.nodes.new("GeometryNodeGroup")
			group_011_3.name = "Group.011"
			group_011_3.node_tree = hbond_backbone_check
			#Socket_5
			group_011_3.inputs[1].default_value = 0
			#Socket_6
			group_011_3.inputs[3].default_value = 0
			
			#node Frame
			frame_10 = _hbond_i__j__and_hbond_j__i_.nodes.new("NodeFrame")
			frame_10.label = "Check Backbone O is bonded to an NH"
			frame_10.name = "Frame"
			frame_10.label_size = 20
			frame_10.shrink = True
			
			#node Frame.001
			frame_001_4 = _hbond_i__j__and_hbond_j__i_.nodes.new("NodeFrame")
			frame_001_4.label = "Check Backbone NH is bonded to an O"
			frame_001_4.name = "Frame.001"
			frame_001_4.label_size = 20
			frame_001_4.shrink = True
			
			#node Boolean Math.003
			boolean_math_003_7 = _hbond_i__j__and_hbond_j__i_.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003_7.name = "Boolean Math.003"
			boolean_math_003_7.operation = 'AND'
			
			#node Group.012
			group_012_3 = _hbond_i__j__and_hbond_j__i_.nodes.new("GeometryNodeGroup")
			group_012_3.name = "Group.012"
			group_012_3.node_tree = hbond_backbone_check_backup
			#Socket_3
			group_012_3.inputs[0].default_value = 0
			#Socket_5
			group_012_3.inputs[1].default_value = 0
			#Socket_0
			group_012_3.inputs[2].default_value = 0
			#Socket_6
			group_012_3.inputs[3].default_value = 0
			
			
			
			#Set parents
			group_010_2.parent = frame_001_4
			group_011_3.parent = frame_10
			
			#Set locations
			group_output_75.location = (640.0, 180.0)
			group_input_73.location = (-235.75640869140625, 47.462432861328125)
			group_010_2.location = (-640.0, 40.0)
			group_011_3.location = (-640.0, -220.0)
			frame_10.location = (635.0, 20.0)
			frame_001_4.location = (630.0, 140.0)
			boolean_math_003_7.location = (435.0, 180.0)
			group_012_3.location = (-20.0, 520.0)
			
			#Set dimensions
			group_output_75.width, group_output_75.height = 140.0, 100.0
			group_input_73.width, group_input_73.height = 140.0, 100.0
			group_010_2.width, group_010_2.height = 267.0645751953125, 100.0
			group_011_3.width, group_011_3.height = 267.0645751953125, 100.0
			frame_10.width, frame_10.height = 327.0645751953125, 309.0
			frame_001_4.width, frame_001_4.height = 327.0645751953125, 309.0
			boolean_math_003_7.width, boolean_math_003_7.height = 140.0, 100.0
			group_012_3.width, group_012_3.height = 267.0645751953125, 100.0
			
			#initialize _hbond_i__j__and_hbond_j__i_ links
			#group_010_2.Is Bonded -> boolean_math_003_7.Boolean
			_hbond_i__j__and_hbond_j__i_.links.new(group_010_2.outputs[0], boolean_math_003_7.inputs[0])
			#group_011_3.Is Bonded -> boolean_math_003_7.Boolean
			_hbond_i__j__and_hbond_j__i_.links.new(group_011_3.outputs[0], boolean_math_003_7.inputs[1])
			#boolean_math_003_7.Boolean -> group_output_75.Boolean
			_hbond_i__j__and_hbond_j__i_.links.new(boolean_math_003_7.outputs[0], group_output_75.inputs[0])
			#group_input_73.j -> group_010_2.NH Index
			_hbond_i__j__and_hbond_j__i_.links.new(group_input_73.outputs[1], group_010_2.inputs[2])
			#group_input_73.j -> group_011_3.CO Index
			_hbond_i__j__and_hbond_j__i_.links.new(group_input_73.outputs[1], group_011_3.inputs[0])
			#group_input_73.i -> group_010_2.CO Index
			_hbond_i__j__and_hbond_j__i_.links.new(group_input_73.outputs[0], group_010_2.inputs[0])
			#group_input_73.i -> group_011_3.NH Index
			_hbond_i__j__and_hbond_j__i_.links.new(group_input_73.outputs[0], group_011_3.inputs[2])
			return _hbond_i__j__and_hbond_j__i_

		_hbond_i__j__and_hbond_j__i_ = _hbond_i__j__and_hbond_j__i__node_group()

		#initialize _hbond_i___1__j___1__and_hbond_j___1__i___1_ node group
		def _hbond_i___1__j___1__and_hbond_j___1__i___1__node_group():
			_hbond_i___1__j___1__and_hbond_j___1__i___1_ = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".HBond(i - 1, j + 1) and HBond(j - 1, i + 1)")

			_hbond_i___1__j___1__and_hbond_j___1__i___1_.color_tag = 'NONE'
			_hbond_i___1__j___1__and_hbond_j___1__i___1_.description = ""

			
			#_hbond_i___1__j___1__and_hbond_j___1__i___1_ interface
			#Socket Boolean
			boolean_socket_13 = _hbond_i___1__j___1__and_hbond_j___1__i___1_.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket_13.attribute_domain = 'POINT'
			
			#Socket i
			i_socket_1 = _hbond_i___1__j___1__and_hbond_j___1__i___1_.interface.new_socket(name = "i", in_out='INPUT', socket_type = 'NodeSocketInt')
			i_socket_1.subtype = 'NONE'
			i_socket_1.default_value = 0
			i_socket_1.min_value = 0
			i_socket_1.max_value = 2147483647
			i_socket_1.attribute_domain = 'POINT'
			i_socket_1.hide_value = True
			
			#Socket j
			j_socket_1 = _hbond_i___1__j___1__and_hbond_j___1__i___1_.interface.new_socket(name = "j", in_out='INPUT', socket_type = 'NodeSocketInt')
			j_socket_1.subtype = 'NONE'
			j_socket_1.default_value = 0
			j_socket_1.min_value = 0
			j_socket_1.max_value = 2147483647
			j_socket_1.attribute_domain = 'POINT'
			j_socket_1.hide_value = True
			
			
			#initialize _hbond_i___1__j___1__and_hbond_j___1__i___1_ nodes
			#node Group Output
			group_output_76 = _hbond_i___1__j___1__and_hbond_j___1__i___1_.nodes.new("NodeGroupOutput")
			group_output_76.name = "Group Output"
			group_output_76.is_active_output = True
			
			#node Group Input
			group_input_74 = _hbond_i___1__j___1__and_hbond_j___1__i___1_.nodes.new("NodeGroupInput")
			group_input_74.name = "Group Input"
			
			#node Group.010
			group_010_3 = _hbond_i___1__j___1__and_hbond_j___1__i___1_.nodes.new("GeometryNodeGroup")
			group_010_3.name = "Group.010"
			group_010_3.node_tree = hbond_backbone_check
			#Socket_5
			group_010_3.inputs[1].default_value = -1
			#Socket_6
			group_010_3.inputs[3].default_value = 1
			
			#node Group.011
			group_011_4 = _hbond_i___1__j___1__and_hbond_j___1__i___1_.nodes.new("GeometryNodeGroup")
			group_011_4.name = "Group.011"
			group_011_4.node_tree = hbond_backbone_check
			#Socket_5
			group_011_4.inputs[1].default_value = -1
			#Socket_6
			group_011_4.inputs[3].default_value = 1
			
			#node Frame
			frame_11 = _hbond_i___1__j___1__and_hbond_j___1__i___1_.nodes.new("NodeFrame")
			frame_11.label = "Check Backbone O is bonded to an NH"
			frame_11.name = "Frame"
			frame_11.label_size = 20
			frame_11.shrink = True
			
			#node Frame.001
			frame_001_5 = _hbond_i___1__j___1__and_hbond_j___1__i___1_.nodes.new("NodeFrame")
			frame_001_5.label = "Check Backbone NH is bonded to an O"
			frame_001_5.name = "Frame.001"
			frame_001_5.label_size = 20
			frame_001_5.shrink = True
			
			#node Boolean Math.003
			boolean_math_003_8 = _hbond_i___1__j___1__and_hbond_j___1__i___1_.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003_8.name = "Boolean Math.003"
			boolean_math_003_8.operation = 'AND'
			
			
			
			#Set parents
			group_010_3.parent = frame_001_5
			group_011_4.parent = frame_11
			
			#Set locations
			group_output_76.location = (625.0, 0.0)
			group_input_74.location = (-394.84100341796875, -236.38262939453125)
			group_010_3.location = (-655.0, 40.0)
			group_011_4.location = (-640.0, -220.0)
			frame_11.location = (635.0, 20.0)
			frame_001_5.location = (655.0, 120.0)
			boolean_math_003_8.location = (435.0, 180.0)
			
			#Set dimensions
			group_output_76.width, group_output_76.height = 140.0, 100.0
			group_input_74.width, group_input_74.height = 140.0, 100.0
			group_010_3.width, group_010_3.height = 267.0645751953125, 100.0
			group_011_4.width, group_011_4.height = 267.0645751953125, 100.0
			frame_11.width, frame_11.height = 327.0645751953125, 309.0
			frame_001_5.width, frame_001_5.height = 327.0645751953125, 309.0
			boolean_math_003_8.width, boolean_math_003_8.height = 140.0, 100.0
			
			#initialize _hbond_i___1__j___1__and_hbond_j___1__i___1_ links
			#group_010_3.Is Bonded -> boolean_math_003_8.Boolean
			_hbond_i___1__j___1__and_hbond_j___1__i___1_.links.new(group_010_3.outputs[0], boolean_math_003_8.inputs[0])
			#group_011_4.Is Bonded -> boolean_math_003_8.Boolean
			_hbond_i___1__j___1__and_hbond_j___1__i___1_.links.new(group_011_4.outputs[0], boolean_math_003_8.inputs[1])
			#boolean_math_003_8.Boolean -> group_output_76.Boolean
			_hbond_i___1__j___1__and_hbond_j___1__i___1_.links.new(boolean_math_003_8.outputs[0], group_output_76.inputs[0])
			#group_input_74.j -> group_010_3.NH Index
			_hbond_i___1__j___1__and_hbond_j___1__i___1_.links.new(group_input_74.outputs[1], group_010_3.inputs[2])
			#group_input_74.j -> group_011_4.CO Index
			_hbond_i___1__j___1__and_hbond_j___1__i___1_.links.new(group_input_74.outputs[1], group_011_4.inputs[0])
			#group_input_74.i -> group_010_3.CO Index
			_hbond_i___1__j___1__and_hbond_j___1__i___1_.links.new(group_input_74.outputs[0], group_010_3.inputs[0])
			#group_input_74.i -> group_011_4.NH Index
			_hbond_i___1__j___1__and_hbond_j___1__i___1_.links.new(group_input_74.outputs[0], group_011_4.inputs[2])
			return _hbond_i___1__j___1__and_hbond_j___1__i___1_

		_hbond_i___1__j___1__and_hbond_j___1__i___1_ = _hbond_i___1__j___1__and_hbond_j___1__i___1__node_group()

		#initialize _hbond_i___1_j__and_hbond_j_i___1_ node group
		def _hbond_i___1_j__and_hbond_j_i___1__node_group():
			_hbond_i___1_j__and_hbond_j_i___1_ = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".Hbond(i - 1,j) and Hbond(j,i + 1)")

			_hbond_i___1_j__and_hbond_j_i___1_.color_tag = 'NONE'
			_hbond_i___1_j__and_hbond_j_i___1_.description = ""

			
			#_hbond_i___1_j__and_hbond_j_i___1_ interface
			#Socket Boolean
			boolean_socket_14 = _hbond_i___1_j__and_hbond_j_i___1_.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket_14.attribute_domain = 'POINT'
			
			#Socket i
			i_socket_2 = _hbond_i___1_j__and_hbond_j_i___1_.interface.new_socket(name = "i", in_out='INPUT', socket_type = 'NodeSocketInt')
			i_socket_2.subtype = 'NONE'
			i_socket_2.default_value = 0
			i_socket_2.min_value = 0
			i_socket_2.max_value = 2147483647
			i_socket_2.attribute_domain = 'POINT'
			i_socket_2.hide_value = True
			
			#Socket j
			j_socket_2 = _hbond_i___1_j__and_hbond_j_i___1_.interface.new_socket(name = "j", in_out='INPUT', socket_type = 'NodeSocketInt')
			j_socket_2.subtype = 'NONE'
			j_socket_2.default_value = 0
			j_socket_2.min_value = 0
			j_socket_2.max_value = 2147483647
			j_socket_2.attribute_domain = 'POINT'
			j_socket_2.hide_value = True
			
			
			#initialize _hbond_i___1_j__and_hbond_j_i___1_ nodes
			#node Group Output
			group_output_77 = _hbond_i___1_j__and_hbond_j_i___1_.nodes.new("NodeGroupOutput")
			group_output_77.name = "Group Output"
			group_output_77.is_active_output = True
			
			#node Group Input
			group_input_75 = _hbond_i___1_j__and_hbond_j_i___1_.nodes.new("NodeGroupInput")
			group_input_75.name = "Group Input"
			
			#node Group.010
			group_010_4 = _hbond_i___1_j__and_hbond_j_i___1_.nodes.new("GeometryNodeGroup")
			group_010_4.name = "Group.010"
			group_010_4.node_tree = hbond_backbone_check
			#Socket_5
			group_010_4.inputs[1].default_value = -1
			#Socket_6
			group_010_4.inputs[3].default_value = 0
			
			#node Group.011
			group_011_5 = _hbond_i___1_j__and_hbond_j_i___1_.nodes.new("GeometryNodeGroup")
			group_011_5.name = "Group.011"
			group_011_5.node_tree = hbond_backbone_check
			#Socket_5
			group_011_5.inputs[1].default_value = 0
			#Socket_6
			group_011_5.inputs[3].default_value = 1
			
			#node Frame
			frame_12 = _hbond_i___1_j__and_hbond_j_i___1_.nodes.new("NodeFrame")
			frame_12.label = "Check Backbone O is bonded to an NH"
			frame_12.name = "Frame"
			frame_12.label_size = 20
			frame_12.shrink = True
			
			#node Frame.001
			frame_001_6 = _hbond_i___1_j__and_hbond_j_i___1_.nodes.new("NodeFrame")
			frame_001_6.label = "Check Backbone NH is bonded to an O"
			frame_001_6.name = "Frame.001"
			frame_001_6.label_size = 20
			frame_001_6.shrink = True
			
			#node Boolean Math.003
			boolean_math_003_9 = _hbond_i___1_j__and_hbond_j_i___1_.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003_9.name = "Boolean Math.003"
			boolean_math_003_9.operation = 'AND'
			
			
			
			#Set parents
			group_010_4.parent = frame_001_6
			group_011_5.parent = frame_12
			
			#Set locations
			group_output_77.location = (625.0, 0.0)
			group_input_75.location = (-373.2626953125, 13.94732666015625)
			group_010_4.location = (-640.0, 40.0)
			group_011_5.location = (-640.0, -220.0)
			frame_12.location = (635.0, 20.0)
			frame_001_6.location = (655.0, 120.0)
			boolean_math_003_9.location = (435.0, 180.0)
			
			#Set dimensions
			group_output_77.width, group_output_77.height = 140.0, 100.0
			group_input_75.width, group_input_75.height = 140.0, 100.0
			group_010_4.width, group_010_4.height = 267.0645751953125, 100.0
			group_011_5.width, group_011_5.height = 267.0645751953125, 100.0
			frame_12.width, frame_12.height = 327.0645751953125, 309.0
			frame_001_6.width, frame_001_6.height = 327.0645751953125, 309.0
			boolean_math_003_9.width, boolean_math_003_9.height = 140.0, 100.0
			
			#initialize _hbond_i___1_j__and_hbond_j_i___1_ links
			#group_010_4.Is Bonded -> boolean_math_003_9.Boolean
			_hbond_i___1_j__and_hbond_j_i___1_.links.new(group_010_4.outputs[0], boolean_math_003_9.inputs[0])
			#group_011_5.Is Bonded -> boolean_math_003_9.Boolean
			_hbond_i___1_j__and_hbond_j_i___1_.links.new(group_011_5.outputs[0], boolean_math_003_9.inputs[1])
			#boolean_math_003_9.Boolean -> group_output_77.Boolean
			_hbond_i___1_j__and_hbond_j_i___1_.links.new(boolean_math_003_9.outputs[0], group_output_77.inputs[0])
			#group_input_75.j -> group_010_4.NH Index
			_hbond_i___1_j__and_hbond_j_i___1_.links.new(group_input_75.outputs[1], group_010_4.inputs[2])
			#group_input_75.j -> group_011_5.CO Index
			_hbond_i___1_j__and_hbond_j_i___1_.links.new(group_input_75.outputs[1], group_011_5.inputs[0])
			#group_input_75.i -> group_010_4.CO Index
			_hbond_i___1_j__and_hbond_j_i___1_.links.new(group_input_75.outputs[0], group_010_4.inputs[0])
			#group_input_75.i -> group_011_5.NH Index
			_hbond_i___1_j__and_hbond_j_i___1_.links.new(group_input_75.outputs[0], group_011_5.inputs[2])
			return _hbond_i___1_j__and_hbond_j_i___1_

		_hbond_i___1_j__and_hbond_j_i___1_ = _hbond_i___1_j__and_hbond_j_i___1__node_group()

		#initialize _hbond_j___1_i_and_hbond_i_j___1_ node group
		def _hbond_j___1_i_and_hbond_i_j___1__node_group():
			_hbond_j___1_i_and_hbond_i_j___1_ = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".Hbond(j - 1,i)and Hbond(i,j + 1)")

			_hbond_j___1_i_and_hbond_i_j___1_.color_tag = 'NONE'
			_hbond_j___1_i_and_hbond_i_j___1_.description = ""

			
			#_hbond_j___1_i_and_hbond_i_j___1_ interface
			#Socket Boolean
			boolean_socket_15 = _hbond_j___1_i_and_hbond_i_j___1_.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket_15.attribute_domain = 'POINT'
			
			#Socket i
			i_socket_3 = _hbond_j___1_i_and_hbond_i_j___1_.interface.new_socket(name = "i", in_out='INPUT', socket_type = 'NodeSocketInt')
			i_socket_3.subtype = 'NONE'
			i_socket_3.default_value = 0
			i_socket_3.min_value = 0
			i_socket_3.max_value = 2147483647
			i_socket_3.attribute_domain = 'POINT'
			i_socket_3.hide_value = True
			
			#Socket j
			j_socket_3 = _hbond_j___1_i_and_hbond_i_j___1_.interface.new_socket(name = "j", in_out='INPUT', socket_type = 'NodeSocketInt')
			j_socket_3.subtype = 'NONE'
			j_socket_3.default_value = 0
			j_socket_3.min_value = 0
			j_socket_3.max_value = 2147483647
			j_socket_3.attribute_domain = 'POINT'
			j_socket_3.hide_value = True
			
			
			#initialize _hbond_j___1_i_and_hbond_i_j___1_ nodes
			#node Group Output
			group_output_78 = _hbond_j___1_i_and_hbond_i_j___1_.nodes.new("NodeGroupOutput")
			group_output_78.name = "Group Output"
			group_output_78.is_active_output = True
			
			#node Group Input
			group_input_76 = _hbond_j___1_i_and_hbond_i_j___1_.nodes.new("NodeGroupInput")
			group_input_76.name = "Group Input"
			
			#node Group.010
			group_010_5 = _hbond_j___1_i_and_hbond_i_j___1_.nodes.new("GeometryNodeGroup")
			group_010_5.name = "Group.010"
			group_010_5.node_tree = hbond_backbone_check
			#Socket_5
			group_010_5.inputs[1].default_value = -1
			#Socket_6
			group_010_5.inputs[3].default_value = 0
			
			#node Group.011
			group_011_6 = _hbond_j___1_i_and_hbond_i_j___1_.nodes.new("GeometryNodeGroup")
			group_011_6.name = "Group.011"
			group_011_6.node_tree = hbond_backbone_check
			#Socket_5
			group_011_6.inputs[1].default_value = 0
			#Socket_6
			group_011_6.inputs[3].default_value = 1
			
			#node Frame
			frame_13 = _hbond_j___1_i_and_hbond_i_j___1_.nodes.new("NodeFrame")
			frame_13.label = "Check Backbone O is bonded to an NH"
			frame_13.name = "Frame"
			frame_13.label_size = 20
			frame_13.shrink = True
			
			#node Frame.001
			frame_001_7 = _hbond_j___1_i_and_hbond_i_j___1_.nodes.new("NodeFrame")
			frame_001_7.label = "Check Backbone NH is bonded to an O"
			frame_001_7.name = "Frame.001"
			frame_001_7.label_size = 20
			frame_001_7.shrink = True
			
			#node Boolean Math.003
			boolean_math_003_10 = _hbond_j___1_i_and_hbond_i_j___1_.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003_10.name = "Boolean Math.003"
			boolean_math_003_10.operation = 'AND'
			
			
			
			#Set parents
			group_010_5.parent = frame_001_7
			group_011_6.parent = frame_13
			
			#Set locations
			group_output_78.location = (625.0, 0.0)
			group_input_76.location = (-360.0, 120.0)
			group_010_5.location = (-640.0, 40.0)
			group_011_6.location = (-640.0, -220.0)
			frame_13.location = (635.0, 20.0)
			frame_001_7.location = (655.0, 120.0)
			boolean_math_003_10.location = (435.0, 180.0)
			
			#Set dimensions
			group_output_78.width, group_output_78.height = 140.0, 100.0
			group_input_76.width, group_input_76.height = 140.0, 100.0
			group_010_5.width, group_010_5.height = 267.0645751953125, 100.0
			group_011_6.width, group_011_6.height = 267.0645751953125, 100.0
			frame_13.width, frame_13.height = 327.0645751953125, 309.0
			frame_001_7.width, frame_001_7.height = 327.0645751953125, 309.0
			boolean_math_003_10.width, boolean_math_003_10.height = 140.0, 100.0
			
			#initialize _hbond_j___1_i_and_hbond_i_j___1_ links
			#group_010_5.Is Bonded -> boolean_math_003_10.Boolean
			_hbond_j___1_i_and_hbond_i_j___1_.links.new(group_010_5.outputs[0], boolean_math_003_10.inputs[0])
			#group_011_6.Is Bonded -> boolean_math_003_10.Boolean
			_hbond_j___1_i_and_hbond_i_j___1_.links.new(group_011_6.outputs[0], boolean_math_003_10.inputs[1])
			#boolean_math_003_10.Boolean -> group_output_78.Boolean
			_hbond_j___1_i_and_hbond_i_j___1_.links.new(boolean_math_003_10.outputs[0], group_output_78.inputs[0])
			#group_input_76.j -> group_011_6.NH Index
			_hbond_j___1_i_and_hbond_i_j___1_.links.new(group_input_76.outputs[1], group_011_6.inputs[2])
			#group_input_76.j -> group_010_5.CO Index
			_hbond_j___1_i_and_hbond_i_j___1_.links.new(group_input_76.outputs[1], group_010_5.inputs[0])
			#group_input_76.i -> group_010_5.NH Index
			_hbond_j___1_i_and_hbond_i_j___1_.links.new(group_input_76.outputs[0], group_010_5.inputs[2])
			#group_input_76.i -> group_011_6.CO Index
			_hbond_j___1_i_and_hbond_i_j___1_.links.new(group_input_76.outputs[0], group_011_6.inputs[0])
			return _hbond_j___1_i_and_hbond_i_j___1_

		_hbond_j___1_i_and_hbond_i_j___1_ = _hbond_j___1_i_and_hbond_i_j___1__node_group()

		#initialize _dssp_sheet_checks node group
		def _dssp_sheet_checks_node_group():
			_dssp_sheet_checks = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".DSSP Sheet Checks")

			_dssp_sheet_checks.color_tag = 'NONE'
			_dssp_sheet_checks.description = ""

			
			#_dssp_sheet_checks interface
			#Socket Boolean
			boolean_socket_16 = _dssp_sheet_checks.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket_16.attribute_domain = 'POINT'
			
			#Socket j
			j_socket_4 = _dssp_sheet_checks.interface.new_socket(name = "j", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			j_socket_4.subtype = 'NONE'
			j_socket_4.default_value = 0
			j_socket_4.min_value = -2147483648
			j_socket_4.max_value = 2147483647
			j_socket_4.attribute_domain = 'POINT'
			
			#Socket Index
			index_socket_7 = _dssp_sheet_checks.interface.new_socket(name = "Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			index_socket_7.subtype = 'NONE'
			index_socket_7.default_value = 0
			index_socket_7.min_value = 0
			index_socket_7.max_value = 2147483647
			index_socket_7.attribute_domain = 'POINT'
			index_socket_7.hide_value = True
			
			#Socket j
			j_socket_5 = _dssp_sheet_checks.interface.new_socket(name = "j", in_out='INPUT', socket_type = 'NodeSocketInt')
			j_socket_5.subtype = 'NONE'
			j_socket_5.default_value = 0
			j_socket_5.min_value = -2147483648
			j_socket_5.max_value = 2147483647
			j_socket_5.attribute_domain = 'POINT'
			
			
			#initialize _dssp_sheet_checks nodes
			#node Group Output
			group_output_79 = _dssp_sheet_checks.nodes.new("NodeGroupOutput")
			group_output_79.name = "Group Output"
			group_output_79.is_active_output = True
			
			#node Group Input
			group_input_77 = _dssp_sheet_checks.nodes.new("NodeGroupInput")
			group_input_77.name = "Group Input"
			
			#node Group.001
			group_001_15 = _dssp_sheet_checks.nodes.new("GeometryNodeGroup")
			group_001_15.name = "Group.001"
			group_001_15.node_tree = _hbond_i__j__and_hbond_j__i_
			
			#node Group.002
			group_002_8 = _dssp_sheet_checks.nodes.new("GeometryNodeGroup")
			group_002_8.name = "Group.002"
			group_002_8.node_tree = _hbond_i___1__j___1__and_hbond_j___1__i___1_
			
			#node Boolean Math
			boolean_math_18 = _dssp_sheet_checks.nodes.new("FunctionNodeBooleanMath")
			boolean_math_18.name = "Boolean Math"
			boolean_math_18.operation = 'OR'
			
			#node Group.004
			group_004_5 = _dssp_sheet_checks.nodes.new("GeometryNodeGroup")
			group_004_5.name = "Group.004"
			group_004_5.node_tree = _hbond_i___1_j__and_hbond_j_i___1_
			
			#node Frame
			frame_14 = _dssp_sheet_checks.nodes.new("NodeFrame")
			frame_14.label = "Anti-parallel Bridge"
			frame_14.name = "Frame"
			frame_14.label_size = 20
			frame_14.shrink = True
			
			#node Frame.001
			frame_001_8 = _dssp_sheet_checks.nodes.new("NodeFrame")
			frame_001_8.label = "Paralell Bridge"
			frame_001_8.name = "Frame.001"
			frame_001_8.label_size = 20
			frame_001_8.shrink = True
			
			#node Boolean Math.001
			boolean_math_001_14 = _dssp_sheet_checks.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_14.name = "Boolean Math.001"
			boolean_math_001_14.operation = 'OR'
			
			#node Boolean Math.002
			boolean_math_002_12 = _dssp_sheet_checks.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_12.name = "Boolean Math.002"
			boolean_math_002_12.operation = 'OR'
			
			#node Group.005
			group_005_6 = _dssp_sheet_checks.nodes.new("GeometryNodeGroup")
			group_005_6.name = "Group.005"
			group_005_6.node_tree = _hbond_j___1_i_and_hbond_i_j___1_
			
			
			
			#Set parents
			group_001_15.parent = frame_14
			group_002_8.parent = frame_14
			boolean_math_18.parent = frame_14
			group_004_5.parent = frame_001_8
			boolean_math_001_14.parent = frame_001_8
			group_005_6.parent = frame_001_8
			
			#Set locations
			group_output_79.location = (570.0, 0.0)
			group_input_77.location = (-657.7005004882812, 1.8694610595703125)
			group_001_15.location = (-800.0, 160.0)
			group_002_8.location = (-800.0, 0.0)
			boolean_math_18.location = (-440.0, 160.0)
			group_004_5.location = (-800.0, -300.0)
			frame_14.location = (580.0, 180.0)
			frame_001_8.location = (580.0, 180.0)
			boolean_math_001_14.location = (-440.0, -300.0)
			boolean_math_002_12.location = (380.0, 140.0)
			group_005_6.location = (-800.0, -460.0)
			
			#Set dimensions
			group_output_79.width, group_output_79.height = 140.0, 100.0
			group_input_77.width, group_input_77.height = 140.0, 100.0
			group_001_15.width, group_001_15.height = 333.0748291015625, 100.0
			group_002_8.width, group_002_8.height = 333.0748291015625, 100.0
			boolean_math_18.width, boolean_math_18.height = 140.0, 100.0
			group_004_5.width, group_004_5.height = 333.0748291015625, 100.0
			frame_14.width, frame_14.height = 560.0, 350.0
			frame_001_8.width, frame_001_8.height = 560.0, 350.0
			boolean_math_001_14.width, boolean_math_001_14.height = 140.0, 100.0
			boolean_math_002_12.width, boolean_math_002_12.height = 140.0, 100.0
			group_005_6.width, group_005_6.height = 333.0748291015625, 100.0
			
			#initialize _dssp_sheet_checks links
			#group_001_15.Boolean -> boolean_math_18.Boolean
			_dssp_sheet_checks.links.new(group_001_15.outputs[0], boolean_math_18.inputs[0])
			#group_input_77.j -> group_002_8.j
			_dssp_sheet_checks.links.new(group_input_77.outputs[1], group_002_8.inputs[1])
			#boolean_math_001_14.Boolean -> boolean_math_002_12.Boolean
			_dssp_sheet_checks.links.new(boolean_math_001_14.outputs[0], boolean_math_002_12.inputs[1])
			#group_004_5.Boolean -> boolean_math_001_14.Boolean
			_dssp_sheet_checks.links.new(group_004_5.outputs[0], boolean_math_001_14.inputs[0])
			#group_input_77.j -> group_005_6.j
			_dssp_sheet_checks.links.new(group_input_77.outputs[1], group_005_6.inputs[1])
			#group_002_8.Boolean -> boolean_math_18.Boolean
			_dssp_sheet_checks.links.new(group_002_8.outputs[0], boolean_math_18.inputs[1])
			#group_input_77.j -> group_001_15.j
			_dssp_sheet_checks.links.new(group_input_77.outputs[1], group_001_15.inputs[1])
			#boolean_math_18.Boolean -> boolean_math_002_12.Boolean
			_dssp_sheet_checks.links.new(boolean_math_18.outputs[0], boolean_math_002_12.inputs[0])
			#group_005_6.Boolean -> boolean_math_001_14.Boolean
			_dssp_sheet_checks.links.new(group_005_6.outputs[0], boolean_math_001_14.inputs[1])
			#group_input_77.j -> group_004_5.j
			_dssp_sheet_checks.links.new(group_input_77.outputs[1], group_004_5.inputs[1])
			#boolean_math_002_12.Boolean -> group_output_79.Boolean
			_dssp_sheet_checks.links.new(boolean_math_002_12.outputs[0], group_output_79.inputs[0])
			#group_input_77.Index -> group_001_15.i
			_dssp_sheet_checks.links.new(group_input_77.outputs[0], group_001_15.inputs[0])
			#group_input_77.Index -> group_002_8.i
			_dssp_sheet_checks.links.new(group_input_77.outputs[0], group_002_8.inputs[0])
			#group_input_77.Index -> group_004_5.i
			_dssp_sheet_checks.links.new(group_input_77.outputs[0], group_004_5.inputs[0])
			#group_input_77.Index -> group_005_6.i
			_dssp_sheet_checks.links.new(group_input_77.outputs[0], group_005_6.inputs[0])
			#group_input_77.j -> group_output_79.j
			_dssp_sheet_checks.links.new(group_input_77.outputs[1], group_output_79.inputs[1])
			return _dssp_sheet_checks

		_dssp_sheet_checks = _dssp_sheet_checks_node_group()

		#initialize _mn_topo_calc_sheet node group
		def _mn_topo_calc_sheet_node_group():
			_mn_topo_calc_sheet = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_topo_calc_sheet")

			_mn_topo_calc_sheet.color_tag = 'NONE'
			_mn_topo_calc_sheet.description = ""

			
			#_mn_topo_calc_sheet interface
			#Socket Geometry
			geometry_socket_12 = _mn_topo_calc_sheet.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_12.attribute_domain = 'POINT'
			
			#Socket Attribute
			attribute_socket = _mn_topo_calc_sheet.interface.new_socket(name = "Attribute", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			attribute_socket.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_13 = _mn_topo_calc_sheet.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_13.attribute_domain = 'POINT'
			
			
			#initialize _mn_topo_calc_sheet nodes
			#node Group Output
			group_output_80 = _mn_topo_calc_sheet.nodes.new("NodeGroupOutput")
			group_output_80.name = "Group Output"
			group_output_80.is_active_output = True
			
			#node Group Input
			group_input_78 = _mn_topo_calc_sheet.nodes.new("NodeGroupInput")
			group_input_78.name = "Group Input"
			
			#node Capture Attribute.002
			capture_attribute_002 = _mn_topo_calc_sheet.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute_002.name = "Capture Attribute.002"
			capture_attribute_002.active_index = 0
			capture_attribute_002.capture_items.clear()
			capture_attribute_002.capture_items.new('FLOAT', "Value")
			capture_attribute_002.capture_items["Value"].data_type = 'BOOLEAN'
			capture_attribute_002.domain = 'POINT'
			
			#node Group.003
			group_003_7 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_003_7.name = "Group.003"
			group_003_7.node_tree = boolean_run_mask
			#Socket_2
			group_003_7.inputs[1].default_value = 0
			#Socket_3
			group_003_7.inputs[2].default_value = 3
			#Socket_6
			group_003_7.inputs[3].default_value = 0
			
			#node Group
			group_28 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_28.name = "Group"
			group_28.mute = True
			group_28.node_tree = boolean_run_fill
			#Socket_2
			group_28.inputs[1].default_value = 1
			
			#node Group.006
			group_006_5 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_006_5.name = "Group.006"
			group_006_5.node_tree = self_sample_proximity
			
			#node Group.007
			group_007_2 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_007_2.name = "Group.007"
			group_007_2.node_tree = mn_topo_backbone
			#Socket_3
			group_007_2.inputs[0].default_value = 0
			
			#node Capture Attribute
			capture_attribute_4 = _mn_topo_calc_sheet.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute_4.name = "Capture Attribute"
			capture_attribute_4.active_index = 3
			capture_attribute_4.capture_items.clear()
			capture_attribute_4.capture_items.new('FLOAT', "Value")
			capture_attribute_4.capture_items["Value"].data_type = 'INT'
			capture_attribute_4.capture_items.new('FLOAT', "Closest Index")
			capture_attribute_4.capture_items["Closest Index"].data_type = 'INT'
			capture_attribute_4.capture_items.new('FLOAT', "Closest Index.001")
			capture_attribute_4.capture_items["Closest Index.001"].data_type = 'INT'
			capture_attribute_4.capture_items.new('FLOAT', "Closest Index.002")
			capture_attribute_4.capture_items["Closest Index.002"].data_type = 'INT'
			capture_attribute_4.domain = 'POINT'
			
			#node Group.008
			group_008_6 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_008_6.name = "Group.008"
			group_008_6.node_tree = _dssp_sheet_checks
			#Socket_3
			group_008_6.inputs[0].default_value = 0
			
			#node Group.009
			group_009_7 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_009_7.name = "Group.009"
			group_009_7.node_tree = _dssp_sheet_checks
			#Socket_3
			group_009_7.inputs[0].default_value = 0
			
			#node Boolean Math
			boolean_math_19 = _mn_topo_calc_sheet.nodes.new("FunctionNodeBooleanMath")
			boolean_math_19.name = "Boolean Math"
			boolean_math_19.operation = 'OR'
			
			#node Group.010
			group_010_6 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_010_6.name = "Group.010"
			group_010_6.node_tree = _dssp_sheet_checks
			#Socket_3
			group_010_6.inputs[0].default_value = 0
			
			#node Boolean Math.001
			boolean_math_001_15 = _mn_topo_calc_sheet.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_15.name = "Boolean Math.001"
			boolean_math_001_15.operation = 'OR'
			
			#node Group.011
			group_011_7 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_011_7.name = "Group.011"
			group_011_7.node_tree = self_sample_proximity
			
			#node Group.012
			group_012_4 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_012_4.name = "Group.012"
			group_012_4.node_tree = mn_topo_backbone
			#Socket_3
			group_012_4.inputs[0].default_value = 0
			
			#node Vector Math
			vector_math_13 = _mn_topo_calc_sheet.nodes.new("ShaderNodeVectorMath")
			vector_math_13.name = "Vector Math"
			vector_math_13.operation = 'SUBTRACT'
			
			#node Vector Math.001
			vector_math_001_5 = _mn_topo_calc_sheet.nodes.new("ShaderNodeVectorMath")
			vector_math_001_5.name = "Vector Math.001"
			vector_math_001_5.operation = 'ADD'
			
			#node Vector Math.002
			vector_math_002_4 = _mn_topo_calc_sheet.nodes.new("ShaderNodeVectorMath")
			vector_math_002_4.name = "Vector Math.002"
			vector_math_002_4.operation = 'SCALE'
			#Scale
			vector_math_002_4.inputs[3].default_value = 3.0
			
			#node Group.013
			group_013_2 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_013_2.name = "Group.013"
			group_013_2.node_tree = self_sample_proximity
			
			#node Group.014
			group_014_3 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_014_3.name = "Group.014"
			group_014_3.node_tree = self_sample_proximity
			
			#node Vector Math.003
			vector_math_003_4 = _mn_topo_calc_sheet.nodes.new("ShaderNodeVectorMath")
			vector_math_003_4.name = "Vector Math.003"
			vector_math_003_4.operation = 'SUBTRACT'
			
			#node Group.015
			group_015_1 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_015_1.name = "Group.015"
			group_015_1.node_tree = _dssp_sheet_checks
			#Socket_3
			group_015_1.inputs[0].default_value = 0
			
			#node Boolean Math.002
			boolean_math_002_13 = _mn_topo_calc_sheet.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_13.name = "Boolean Math.002"
			boolean_math_002_13.operation = 'OR'
			
			#node Group.016
			group_016_1 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_016_1.name = "Group.016"
			group_016_1.node_tree = _dssp_sheet_checks
			#Socket_3
			group_016_1.inputs[0].default_value = 0
			
			#node Boolean Math.003
			boolean_math_003_11 = _mn_topo_calc_sheet.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003_11.name = "Boolean Math.003"
			boolean_math_003_11.operation = 'OR'
			
			#node Group.017
			group_017_2 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_017_2.name = "Group.017"
			group_017_2.node_tree = _dssp_sheet_checks
			#Socket_3
			group_017_2.inputs[0].default_value = 0
			
			#node Reroute
			reroute_21 = _mn_topo_calc_sheet.nodes.new("NodeReroute")
			reroute_21.name = "Reroute"
			#node Boolean Math.004
			boolean_math_004_8 = _mn_topo_calc_sheet.nodes.new("FunctionNodeBooleanMath")
			boolean_math_004_8.name = "Boolean Math.004"
			boolean_math_004_8.operation = 'OR'
			
			#node Store Named Attribute
			store_named_attribute_7 = _mn_topo_calc_sheet.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_7.name = "Store Named Attribute"
			store_named_attribute_7.data_type = 'INT'
			store_named_attribute_7.domain = 'POINT'
			#Name
			store_named_attribute_7.inputs[2].default_value = "tmp_bonded_idx"
			
			#node Store Named Attribute.001
			store_named_attribute_001_3 = _mn_topo_calc_sheet.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_001_3.name = "Store Named Attribute.001"
			store_named_attribute_001_3.data_type = 'INT'
			store_named_attribute_001_3.domain = 'POINT'
			#Name
			store_named_attribute_001_3.inputs[2].default_value = "tmp_bonded_idx"
			
			#node Store Named Attribute.002
			store_named_attribute_002_3 = _mn_topo_calc_sheet.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_002_3.name = "Store Named Attribute.002"
			store_named_attribute_002_3.data_type = 'INT'
			store_named_attribute_002_3.domain = 'POINT'
			#Selection
			store_named_attribute_002_3.inputs[1].default_value = True
			#Name
			store_named_attribute_002_3.inputs[2].default_value = "tmp_bonded_idx"
			#Value
			store_named_attribute_002_3.inputs[3].default_value = -1
			
			#node Store Named Attribute.003
			store_named_attribute_003_2 = _mn_topo_calc_sheet.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_003_2.name = "Store Named Attribute.003"
			store_named_attribute_003_2.data_type = 'INT'
			store_named_attribute_003_2.domain = 'POINT'
			#Name
			store_named_attribute_003_2.inputs[2].default_value = "tmp_bonded_idx"
			
			#node Store Named Attribute.004
			store_named_attribute_004_3 = _mn_topo_calc_sheet.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_004_3.name = "Store Named Attribute.004"
			store_named_attribute_004_3.data_type = 'INT'
			store_named_attribute_004_3.domain = 'POINT'
			#Name
			store_named_attribute_004_3.inputs[2].default_value = "tmp_bonded_idx"
			
			#node Store Named Attribute.005
			store_named_attribute_005_3 = _mn_topo_calc_sheet.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_005_3.name = "Store Named Attribute.005"
			store_named_attribute_005_3.data_type = 'INT'
			store_named_attribute_005_3.domain = 'POINT'
			#Name
			store_named_attribute_005_3.inputs[2].default_value = "tmp_bonded_idx"
			
			#node Store Named Attribute.006
			store_named_attribute_006_1 = _mn_topo_calc_sheet.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_006_1.name = "Store Named Attribute.006"
			store_named_attribute_006_1.data_type = 'INT'
			store_named_attribute_006_1.domain = 'POINT'
			#Name
			store_named_attribute_006_1.inputs[2].default_value = "tmp_bonded_idx"
			
			#node Group.001
			group_001_16 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_001_16.name = "Group.001"
			group_001_16.node_tree = offset_integer
			#Socket_1
			group_001_16.inputs[0].default_value = 0
			#Socket_2
			group_001_16.inputs[2].default_value = 1
			
			#node Math
			math_23 = _mn_topo_calc_sheet.nodes.new("ShaderNodeMath")
			math_23.name = "Math"
			math_23.operation = 'ADD'
			math_23.use_clamp = False
			#Value_001
			math_23.inputs[1].default_value = -1.0
			
			#node Group.002
			group_002_9 = _mn_topo_calc_sheet.nodes.new("GeometryNodeGroup")
			group_002_9.name = "Group.002"
			group_002_9.node_tree = offset_integer
			#Socket_1
			group_002_9.inputs[0].default_value = 0
			#Socket_2
			group_002_9.inputs[2].default_value = 1
			
			#node Math.001
			math_001_13 = _mn_topo_calc_sheet.nodes.new("ShaderNodeMath")
			math_001_13.name = "Math.001"
			math_001_13.operation = 'ADD'
			math_001_13.use_clamp = False
			#Value_001
			math_001_13.inputs[1].default_value = -1.0
			
			
			
			
			#Set locations
			group_output_80.location = (1360.0, 240.0)
			group_input_78.location = (-1780.0, 80.0)
			capture_attribute_002.location = (960.0, 240.0)
			group_003_7.location = (960.0, -80.0)
			group_28.location = (960.0, 60.0)
			group_006_5.location = (-1520.0, 20.0)
			group_007_2.location = (-2100.0, -60.0)
			capture_attribute_4.location = (-1240.0, 100.0)
			group_008_6.location = (-340.0, 20.0)
			group_009_7.location = (-340.0, -120.0)
			boolean_math_19.location = (40.0, 0.0)
			group_010_6.location = (-340.0, -260.0)
			boolean_math_001_15.location = (40.0, -140.0)
			group_011_7.location = (-1520.0, -320.0)
			group_012_4.location = (-2300.0, -280.0)
			vector_math_13.location = (-2060.0, -600.0)
			vector_math_001_5.location = (-1740.0, -600.0)
			vector_math_002_4.location = (-1900.0, -600.0)
			group_013_2.location = (-1520.0, -140.0)
			group_014_3.location = (-1520.0, -480.0)
			vector_math_003_4.location = (-1740.0, -740.0)
			group_015_1.location = (-340.0, -400.0)
			boolean_math_002_13.location = (40.0, -280.0)
			group_016_1.location = (-344.5273742675781, -540.385498046875)
			boolean_math_003_11.location = (40.0, -440.0)
			group_017_2.location = (-340.0, -680.0)
			reroute_21.location = (-740.0, -640.0)
			boolean_math_004_8.location = (40.0, -600.0)
			store_named_attribute_7.location = (-180.0, 240.0)
			store_named_attribute_001_3.location = (-20.0, 240.0)
			store_named_attribute_002_3.location = (-340.0, 240.0)
			store_named_attribute_003_2.location = (140.0, 240.0)
			store_named_attribute_004_3.location = (300.0, 240.0)
			store_named_attribute_005_3.location = (460.0, 240.0)
			store_named_attribute_006_1.location = (620.0, 240.0)
			group_001_16.location = (-680.0, -540.0)
			math_23.location = (-520.0, -540.0)
			group_002_9.location = (-680.0, -720.0)
			math_001_13.location = (-520.0, -720.0)
			
			#Set dimensions
			group_output_80.width, group_output_80.height = 140.0, 100.0
			group_input_78.width, group_input_78.height = 140.0, 100.0
			capture_attribute_002.width, capture_attribute_002.height = 140.0, 100.0
			group_003_7.width, group_003_7.height = 167.49020385742188, 100.0
			group_28.width, group_28.height = 140.0, 100.0
			group_006_5.width, group_006_5.height = 140.0, 100.0
			group_007_2.width, group_007_2.height = 140.0, 100.0
			capture_attribute_4.width, capture_attribute_4.height = 140.0, 100.0
			group_008_6.width, group_008_6.height = 140.0, 100.0
			group_009_7.width, group_009_7.height = 140.0, 100.0
			boolean_math_19.width, boolean_math_19.height = 140.0, 100.0
			group_010_6.width, group_010_6.height = 140.0, 100.0
			boolean_math_001_15.width, boolean_math_001_15.height = 140.0, 100.0
			group_011_7.width, group_011_7.height = 140.0, 100.0
			group_012_4.width, group_012_4.height = 140.0, 100.0
			vector_math_13.width, vector_math_13.height = 140.0, 100.0
			vector_math_001_5.width, vector_math_001_5.height = 140.0, 100.0
			vector_math_002_4.width, vector_math_002_4.height = 140.0, 100.0
			group_013_2.width, group_013_2.height = 140.0, 100.0
			group_014_3.width, group_014_3.height = 140.0, 100.0
			vector_math_003_4.width, vector_math_003_4.height = 140.0, 100.0
			group_015_1.width, group_015_1.height = 140.0, 100.0
			boolean_math_002_13.width, boolean_math_002_13.height = 140.0, 100.0
			group_016_1.width, group_016_1.height = 140.0, 100.0
			boolean_math_003_11.width, boolean_math_003_11.height = 140.0, 100.0
			group_017_2.width, group_017_2.height = 140.0, 100.0
			reroute_21.width, reroute_21.height = 16.0, 100.0
			boolean_math_004_8.width, boolean_math_004_8.height = 140.0, 100.0
			store_named_attribute_7.width, store_named_attribute_7.height = 140.0, 100.0
			store_named_attribute_001_3.width, store_named_attribute_001_3.height = 140.0, 100.0
			store_named_attribute_002_3.width, store_named_attribute_002_3.height = 140.0, 100.0
			store_named_attribute_003_2.width, store_named_attribute_003_2.height = 140.0, 100.0
			store_named_attribute_004_3.width, store_named_attribute_004_3.height = 140.0, 100.0
			store_named_attribute_005_3.width, store_named_attribute_005_3.height = 140.0, 100.0
			store_named_attribute_006_1.width, store_named_attribute_006_1.height = 140.0, 100.0
			group_001_16.width, group_001_16.height = 140.0, 100.0
			math_23.width, math_23.height = 140.0, 100.0
			group_002_9.width, group_002_9.height = 140.0, 100.0
			math_001_13.width, math_001_13.height = 140.0, 100.0
			
			#initialize _mn_topo_calc_sheet links
			#store_named_attribute_006_1.Geometry -> capture_attribute_002.Geometry
			_mn_topo_calc_sheet.links.new(store_named_attribute_006_1.outputs[0], capture_attribute_002.inputs[0])
			#capture_attribute_002.Geometry -> group_output_80.Geometry
			_mn_topo_calc_sheet.links.new(capture_attribute_002.outputs[0], group_output_80.inputs[0])
			#capture_attribute_002.Value -> group_output_80.Attribute
			_mn_topo_calc_sheet.links.new(capture_attribute_002.outputs[1], group_output_80.inputs[1])
			#group_28.Boolean -> capture_attribute_002.Value
			_mn_topo_calc_sheet.links.new(group_28.outputs[0], capture_attribute_002.inputs[1])
			#group_input_78.Geometry -> group_006_5.Input
			_mn_topo_calc_sheet.links.new(group_input_78.outputs[0], group_006_5.inputs[0])
			#group_007_2.NH -> group_006_5.Target Position
			_mn_topo_calc_sheet.links.new(group_007_2.outputs[4], group_006_5.inputs[1])
			#group_007_2.O -> group_006_5.Self Position
			_mn_topo_calc_sheet.links.new(group_007_2.outputs[0], group_006_5.inputs[2])
			#group_input_78.Geometry -> capture_attribute_4.Geometry
			_mn_topo_calc_sheet.links.new(group_input_78.outputs[0], capture_attribute_4.inputs[0])
			#group_006_5.Closest Index -> capture_attribute_4.Value
			_mn_topo_calc_sheet.links.new(group_006_5.outputs[0], capture_attribute_4.inputs[1])
			#capture_attribute_4.Value -> group_008_6.j
			_mn_topo_calc_sheet.links.new(capture_attribute_4.outputs[1], group_008_6.inputs[1])
			#group_008_6.Boolean -> boolean_math_19.Boolean
			_mn_topo_calc_sheet.links.new(group_008_6.outputs[0], boolean_math_19.inputs[0])
			#group_003_7.Boolean -> group_28.Boolean
			_mn_topo_calc_sheet.links.new(group_003_7.outputs[0], group_28.inputs[0])
			#boolean_math_19.Boolean -> boolean_math_001_15.Boolean
			_mn_topo_calc_sheet.links.new(boolean_math_19.outputs[0], boolean_math_001_15.inputs[0])
			#group_input_78.Geometry -> group_011_7.Input
			_mn_topo_calc_sheet.links.new(group_input_78.outputs[0], group_011_7.inputs[0])
			#capture_attribute_4.Closest Index -> group_009_7.j
			_mn_topo_calc_sheet.links.new(capture_attribute_4.outputs[2], group_009_7.inputs[1])
			#group_012_4.O -> vector_math_13.Vector
			_mn_topo_calc_sheet.links.new(group_012_4.outputs[0], vector_math_13.inputs[1])
			#group_012_4.CA -> vector_math_001_5.Vector
			_mn_topo_calc_sheet.links.new(group_012_4.outputs[2], vector_math_001_5.inputs[0])
			#vector_math_13.Vector -> vector_math_002_4.Vector
			_mn_topo_calc_sheet.links.new(vector_math_13.outputs[0], vector_math_002_4.inputs[0])
			#vector_math_002_4.Vector -> vector_math_001_5.Vector
			_mn_topo_calc_sheet.links.new(vector_math_002_4.outputs[0], vector_math_001_5.inputs[1])
			#group_012_4.CA -> group_011_7.Target Position
			_mn_topo_calc_sheet.links.new(group_012_4.outputs[2], group_011_7.inputs[1])
			#vector_math_001_5.Vector -> group_011_7.Self Position
			_mn_topo_calc_sheet.links.new(vector_math_001_5.outputs[0], group_011_7.inputs[2])
			#group_012_4.C -> vector_math_13.Vector
			_mn_topo_calc_sheet.links.new(group_012_4.outputs[1], vector_math_13.inputs[0])
			#group_input_78.Geometry -> group_013_2.Input
			_mn_topo_calc_sheet.links.new(group_input_78.outputs[0], group_013_2.inputs[0])
			#capture_attribute_4.Closest Index.001 -> group_010_6.j
			_mn_topo_calc_sheet.links.new(capture_attribute_4.outputs[3], group_010_6.inputs[1])
			#group_012_4.NH -> group_013_2.Self Position
			_mn_topo_calc_sheet.links.new(group_012_4.outputs[4], group_013_2.inputs[2])
			#group_012_4.O -> group_013_2.Target Position
			_mn_topo_calc_sheet.links.new(group_012_4.outputs[0], group_013_2.inputs[1])
			#group_010_6.Boolean -> boolean_math_001_15.Boolean
			_mn_topo_calc_sheet.links.new(group_010_6.outputs[0], boolean_math_001_15.inputs[1])
			#group_009_7.Boolean -> boolean_math_19.Boolean
			_mn_topo_calc_sheet.links.new(group_009_7.outputs[0], boolean_math_19.inputs[1])
			#group_input_78.Geometry -> group_014_3.Input
			_mn_topo_calc_sheet.links.new(group_input_78.outputs[0], group_014_3.inputs[0])
			#group_012_4.CA -> group_014_3.Target Position
			_mn_topo_calc_sheet.links.new(group_012_4.outputs[2], group_014_3.inputs[1])
			#group_012_4.CA -> vector_math_003_4.Vector
			_mn_topo_calc_sheet.links.new(group_012_4.outputs[2], vector_math_003_4.inputs[0])
			#vector_math_002_4.Vector -> vector_math_003_4.Vector
			_mn_topo_calc_sheet.links.new(vector_math_002_4.outputs[0], vector_math_003_4.inputs[1])
			#vector_math_003_4.Vector -> group_014_3.Self Position
			_mn_topo_calc_sheet.links.new(vector_math_003_4.outputs[0], group_014_3.inputs[2])
			#capture_attribute_4.Closest Index.002 -> group_015_1.j
			_mn_topo_calc_sheet.links.new(capture_attribute_4.outputs[4], group_015_1.inputs[1])
			#boolean_math_001_15.Boolean -> boolean_math_002_13.Boolean
			_mn_topo_calc_sheet.links.new(boolean_math_001_15.outputs[0], boolean_math_002_13.inputs[0])
			#group_015_1.Boolean -> boolean_math_002_13.Boolean
			_mn_topo_calc_sheet.links.new(group_015_1.outputs[0], boolean_math_002_13.inputs[1])
			#boolean_math_002_13.Boolean -> boolean_math_003_11.Boolean
			_mn_topo_calc_sheet.links.new(boolean_math_002_13.outputs[0], boolean_math_003_11.inputs[0])
			#group_016_1.Boolean -> boolean_math_003_11.Boolean
			_mn_topo_calc_sheet.links.new(group_016_1.outputs[0], boolean_math_003_11.inputs[1])
			#capture_attribute_4.Value -> reroute_21.Input
			_mn_topo_calc_sheet.links.new(capture_attribute_4.outputs[1], reroute_21.inputs[0])
			#boolean_math_003_11.Boolean -> boolean_math_004_8.Boolean
			_mn_topo_calc_sheet.links.new(boolean_math_003_11.outputs[0], boolean_math_004_8.inputs[0])
			#group_017_2.Boolean -> boolean_math_004_8.Boolean
			_mn_topo_calc_sheet.links.new(group_017_2.outputs[0], boolean_math_004_8.inputs[1])
			#boolean_math_004_8.Boolean -> group_003_7.Boolean
			_mn_topo_calc_sheet.links.new(boolean_math_004_8.outputs[0], group_003_7.inputs[0])
			#store_named_attribute_002_3.Geometry -> store_named_attribute_7.Geometry
			_mn_topo_calc_sheet.links.new(store_named_attribute_002_3.outputs[0], store_named_attribute_7.inputs[0])
			#group_008_6.j -> store_named_attribute_7.Value
			_mn_topo_calc_sheet.links.new(group_008_6.outputs[1], store_named_attribute_7.inputs[3])
			#group_008_6.Boolean -> store_named_attribute_7.Selection
			_mn_topo_calc_sheet.links.new(group_008_6.outputs[0], store_named_attribute_7.inputs[1])
			#store_named_attribute_7.Geometry -> store_named_attribute_001_3.Geometry
			_mn_topo_calc_sheet.links.new(store_named_attribute_7.outputs[0], store_named_attribute_001_3.inputs[0])
			#group_009_7.Boolean -> store_named_attribute_001_3.Selection
			_mn_topo_calc_sheet.links.new(group_009_7.outputs[0], store_named_attribute_001_3.inputs[1])
			#group_009_7.j -> store_named_attribute_001_3.Value
			_mn_topo_calc_sheet.links.new(group_009_7.outputs[1], store_named_attribute_001_3.inputs[3])
			#capture_attribute_4.Geometry -> store_named_attribute_002_3.Geometry
			_mn_topo_calc_sheet.links.new(capture_attribute_4.outputs[0], store_named_attribute_002_3.inputs[0])
			#store_named_attribute_001_3.Geometry -> store_named_attribute_003_2.Geometry
			_mn_topo_calc_sheet.links.new(store_named_attribute_001_3.outputs[0], store_named_attribute_003_2.inputs[0])
			#group_010_6.Boolean -> store_named_attribute_003_2.Selection
			_mn_topo_calc_sheet.links.new(group_010_6.outputs[0], store_named_attribute_003_2.inputs[1])
			#group_010_6.j -> store_named_attribute_003_2.Value
			_mn_topo_calc_sheet.links.new(group_010_6.outputs[1], store_named_attribute_003_2.inputs[3])
			#store_named_attribute_003_2.Geometry -> store_named_attribute_004_3.Geometry
			_mn_topo_calc_sheet.links.new(store_named_attribute_003_2.outputs[0], store_named_attribute_004_3.inputs[0])
			#group_015_1.Boolean -> store_named_attribute_004_3.Selection
			_mn_topo_calc_sheet.links.new(group_015_1.outputs[0], store_named_attribute_004_3.inputs[1])
			#group_015_1.j -> store_named_attribute_004_3.Value
			_mn_topo_calc_sheet.links.new(group_015_1.outputs[1], store_named_attribute_004_3.inputs[3])
			#store_named_attribute_004_3.Geometry -> store_named_attribute_005_3.Geometry
			_mn_topo_calc_sheet.links.new(store_named_attribute_004_3.outputs[0], store_named_attribute_005_3.inputs[0])
			#group_016_1.Boolean -> store_named_attribute_005_3.Selection
			_mn_topo_calc_sheet.links.new(group_016_1.outputs[0], store_named_attribute_005_3.inputs[1])
			#group_016_1.j -> store_named_attribute_005_3.Value
			_mn_topo_calc_sheet.links.new(group_016_1.outputs[1], store_named_attribute_005_3.inputs[3])
			#store_named_attribute_005_3.Geometry -> store_named_attribute_006_1.Geometry
			_mn_topo_calc_sheet.links.new(store_named_attribute_005_3.outputs[0], store_named_attribute_006_1.inputs[0])
			#group_017_2.Boolean -> store_named_attribute_006_1.Selection
			_mn_topo_calc_sheet.links.new(group_017_2.outputs[0], store_named_attribute_006_1.inputs[1])
			#group_017_2.j -> store_named_attribute_006_1.Value
			_mn_topo_calc_sheet.links.new(group_017_2.outputs[1], store_named_attribute_006_1.inputs[3])
			#group_001_16.Value -> math_23.Value
			_mn_topo_calc_sheet.links.new(group_001_16.outputs[0], math_23.inputs[0])
			#reroute_21.Output -> group_001_16.Value
			_mn_topo_calc_sheet.links.new(reroute_21.outputs[0], group_001_16.inputs[1])
			#math_23.Value -> group_016_1.j
			_mn_topo_calc_sheet.links.new(math_23.outputs[0], group_016_1.inputs[1])
			#group_002_9.Value -> math_001_13.Value
			_mn_topo_calc_sheet.links.new(group_002_9.outputs[0], math_001_13.inputs[0])
			#reroute_21.Output -> group_002_9.Value
			_mn_topo_calc_sheet.links.new(reroute_21.outputs[0], group_002_9.inputs[1])
			#math_001_13.Value -> group_017_2.j
			_mn_topo_calc_sheet.links.new(math_001_13.outputs[0], group_017_2.inputs[1])
			#group_013_2.Closest Index -> capture_attribute_4.Closest Index
			_mn_topo_calc_sheet.links.new(group_013_2.outputs[0], capture_attribute_4.inputs[2])
			#group_011_7.Closest Index -> capture_attribute_4.Closest Index.001
			_mn_topo_calc_sheet.links.new(group_011_7.outputs[0], capture_attribute_4.inputs[3])
			#group_014_3.Closest Index -> capture_attribute_4.Closest Index.002
			_mn_topo_calc_sheet.links.new(group_014_3.outputs[0], capture_attribute_4.inputs[4])
			return _mn_topo_calc_sheet

		_mn_topo_calc_sheet = _mn_topo_calc_sheet_node_group()

		#initialize topology_dssp node group
		def topology_dssp_node_group():
			topology_dssp = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Topology DSSP")

			topology_dssp.color_tag = 'GEOMETRY'
			topology_dssp.description = "Calculate the secondary structure attributes for the protein chains, based on the 1983 Kabsch algorithm"

			
			#topology_dssp interface
			#Socket Atoms
			atoms_socket_13 = topology_dssp.interface.new_socket(name = "Atoms", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_13.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket_14 = topology_dssp.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_14.attribute_domain = 'POINT'
			
			#Socket Selection
			selection_socket_20 = topology_dssp.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_20.attribute_domain = 'POINT'
			selection_socket_20.hide_value = True
			
			
			#initialize topology_dssp nodes
			#node Group Output
			group_output_81 = topology_dssp.nodes.new("NodeGroupOutput")
			group_output_81.name = "Group Output"
			group_output_81.is_active_output = True
			
			#node Group Input
			group_input_79 = topology_dssp.nodes.new("NodeGroupInput")
			group_input_79.name = "Group Input"
			
			#node Group.002
			group_002_10 = topology_dssp.nodes.new("GeometryNodeGroup")
			group_002_10.name = "Group.002"
			group_002_10.node_tree = _mn_topo_calc_helix
			
			#node Store Named Attribute.003
			store_named_attribute_003_3 = topology_dssp.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_003_3.label = "store helix"
			store_named_attribute_003_3.name = "Store Named Attribute.003"
			store_named_attribute_003_3.data_type = 'INT'
			store_named_attribute_003_3.domain = 'POINT'
			#Name
			store_named_attribute_003_3.inputs[2].default_value = "sec_struct"
			
			#node Sample Index
			sample_index_2 = topology_dssp.nodes.new("GeometryNodeSampleIndex")
			sample_index_2.name = "Sample Index"
			sample_index_2.clamp = False
			sample_index_2.data_type = 'BOOLEAN'
			sample_index_2.domain = 'POINT'
			
			#node Group.005
			group_005_7 = topology_dssp.nodes.new("GeometryNodeGroup")
			group_005_7.name = "Group.005"
			group_005_7.node_tree = _mn_topo_calc_sheet
			
			#node Sample Index.001
			sample_index_001_3 = topology_dssp.nodes.new("GeometryNodeSampleIndex")
			sample_index_001_3.name = "Sample Index.001"
			sample_index_001_3.clamp = False
			sample_index_001_3.data_type = 'BOOLEAN'
			sample_index_001_3.domain = 'POINT'
			
			#node Sample Index.002
			sample_index_002_1 = topology_dssp.nodes.new("GeometryNodeSampleIndex")
			sample_index_002_1.name = "Sample Index.002"
			sample_index_002_1.hide = True
			sample_index_002_1.clamp = False
			sample_index_002_1.data_type = 'INT'
			sample_index_002_1.domain = 'POINT'
			
			#node Index
			index_8 = topology_dssp.nodes.new("GeometryNodeInputIndex")
			index_8.name = "Index"
			
			#node Switch
			switch_19 = topology_dssp.nodes.new("GeometryNodeSwitch")
			switch_19.name = "Switch"
			switch_19.input_type = 'INT'
			#False
			switch_19.inputs[1].default_value = 3
			#True
			switch_19.inputs[2].default_value = 2
			
			#node Switch.001
			switch_001_5 = topology_dssp.nodes.new("GeometryNodeSwitch")
			switch_001_5.name = "Switch.001"
			switch_001_5.input_type = 'INT'
			#True
			switch_001_5.inputs[2].default_value = 1
			
			#node Reroute.003
			reroute_003_6 = topology_dssp.nodes.new("NodeReroute")
			reroute_003_6.name = "Reroute.003"
			#node Sample Index.003
			sample_index_003_1 = topology_dssp.nodes.new("GeometryNodeSampleIndex")
			sample_index_003_1.name = "Sample Index.003"
			sample_index_003_1.clamp = False
			sample_index_003_1.data_type = 'INT'
			sample_index_003_1.domain = 'POINT'
			
			#node Index.002
			index_002_2 = topology_dssp.nodes.new("GeometryNodeInputIndex")
			index_002_2.name = "Index.002"
			
			#node MN_topo_compute_backbone.001
			mn_topo_compute_backbone_001 = topology_dssp.nodes.new("GeometryNodeGroup")
			mn_topo_compute_backbone_001.label = "Topology Compute Backbone"
			mn_topo_compute_backbone_001.name = "MN_topo_compute_backbone.001"
			mn_topo_compute_backbone_001.node_tree = _mn_topo_assign_backbone
			
			#node Frame
			frame_15 = topology_dssp.nodes.new("NodeFrame")
			frame_15.label = "Compute Helix"
			frame_15.name = "Frame"
			frame_15.label_size = 20
			frame_15.shrink = True
			
			#node Frame.001
			frame_001_9 = topology_dssp.nodes.new("NodeFrame")
			frame_001_9.label = "Compute Sheet"
			frame_001_9.name = "Frame.001"
			frame_001_9.label_size = 20
			frame_001_9.shrink = True
			
			
			
			#Set parents
			group_002_10.parent = frame_15
			sample_index_2.parent = frame_15
			group_005_7.parent = frame_001_9
			sample_index_001_3.parent = frame_001_9
			
			#Set locations
			group_output_81.location = (676.5311889648438, 311.6835632324219)
			group_input_79.location = (-1820.0, 380.0)
			group_002_10.location = (-1140.0, -80.0)
			store_named_attribute_003_3.location = (-520.0, 480.0)
			sample_index_2.location = (-740.0, -60.0)
			group_005_7.location = (-1140.0, -380.0)
			sample_index_001_3.location = (-740.0, -380.0)
			sample_index_002_1.location = (-720.0, 120.0)
			index_8.location = (-920.0, 120.0)
			switch_19.location = (-520.0, -120.0)
			switch_001_5.location = (-520.0, 40.0)
			reroute_003_6.location = (-1300.0, -120.0)
			sample_index_003_1.location = (-520.0, 280.0)
			index_002_2.location = (-940.0, -200.0)
			mn_topo_compute_backbone_001.location = (-1560.0, 300.0)
			frame_15.location = (-10.0, 80.0)
			frame_001_9.location = (-10.0, 80.0)
			
			#Set dimensions
			group_output_81.width, group_output_81.height = 140.0, 100.0
			group_input_79.width, group_input_79.height = 140.0, 100.0
			group_002_10.width, group_002_10.height = 238.041015625, 100.0
			store_named_attribute_003_3.width, store_named_attribute_003_3.height = 140.0, 100.0
			sample_index_2.width, sample_index_2.height = 140.0, 100.0
			group_005_7.width, group_005_7.height = 210.28070068359375, 100.0
			sample_index_001_3.width, sample_index_001_3.height = 140.0, 100.0
			sample_index_002_1.width, sample_index_002_1.height = 140.0, 100.0
			index_8.width, index_8.height = 140.0, 100.0
			switch_19.width, switch_19.height = 140.0, 100.0
			switch_001_5.width, switch_001_5.height = 140.0, 100.0
			reroute_003_6.width, reroute_003_6.height = 16.0, 100.0
			sample_index_003_1.width, sample_index_003_1.height = 140.0, 100.0
			index_002_2.width, index_002_2.height = 140.0, 100.0
			mn_topo_compute_backbone_001.width, mn_topo_compute_backbone_001.height = 207.010986328125, 100.0
			frame_15.width, frame_15.height = 600.0, 264.0
			frame_001_9.width, frame_001_9.height = 600.0, 264.0
			
			#initialize topology_dssp links
			#group_input_79.Atoms -> store_named_attribute_003_3.Geometry
			topology_dssp.links.new(group_input_79.outputs[0], store_named_attribute_003_3.inputs[0])
			#reroute_003_6.Output -> sample_index_2.Geometry
			topology_dssp.links.new(reroute_003_6.outputs[0], sample_index_2.inputs[0])
			#store_named_attribute_003_3.Geometry -> group_output_81.Atoms
			topology_dssp.links.new(store_named_attribute_003_3.outputs[0], group_output_81.inputs[0])
			#reroute_003_6.Output -> group_005_7.Geometry
			topology_dssp.links.new(reroute_003_6.outputs[0], group_005_7.inputs[0])
			#mn_topo_compute_backbone_001.Atoms -> sample_index_002_1.Geometry
			topology_dssp.links.new(mn_topo_compute_backbone_001.outputs[0], sample_index_002_1.inputs[0])
			#index_8.Index -> sample_index_002_1.Index
			topology_dssp.links.new(index_8.outputs[0], sample_index_002_1.inputs[2])
			#group_005_7.Geometry -> sample_index_001_3.Geometry
			topology_dssp.links.new(group_005_7.outputs[0], sample_index_001_3.inputs[0])
			#sample_index_001_3.Value -> switch_19.Switch
			topology_dssp.links.new(sample_index_001_3.outputs[0], switch_19.inputs[0])
			#switch_19.Output -> switch_001_5.False
			topology_dssp.links.new(switch_19.outputs[0], switch_001_5.inputs[1])
			#sample_index_2.Value -> switch_001_5.Switch
			topology_dssp.links.new(sample_index_2.outputs[0], switch_001_5.inputs[0])
			#mn_topo_compute_backbone_001.CA Atoms -> reroute_003_6.Input
			topology_dssp.links.new(mn_topo_compute_backbone_001.outputs[2], reroute_003_6.inputs[0])
			#group_002_10.Is Helix -> sample_index_2.Value
			topology_dssp.links.new(group_002_10.outputs[0], sample_index_2.inputs[1])
			#group_005_7.Attribute -> sample_index_001_3.Value
			topology_dssp.links.new(group_005_7.outputs[1], sample_index_001_3.inputs[1])
			#mn_topo_compute_backbone_001.Unique Group ID -> sample_index_002_1.Value
			topology_dssp.links.new(mn_topo_compute_backbone_001.outputs[1], sample_index_002_1.inputs[1])
			#sample_index_002_1.Value -> sample_index_003_1.Index
			topology_dssp.links.new(sample_index_002_1.outputs[0], sample_index_003_1.inputs[2])
			#mn_topo_compute_backbone_001.CA Atoms -> sample_index_003_1.Geometry
			topology_dssp.links.new(mn_topo_compute_backbone_001.outputs[2], sample_index_003_1.inputs[0])
			#switch_001_5.Output -> sample_index_003_1.Value
			topology_dssp.links.new(switch_001_5.outputs[0], sample_index_003_1.inputs[1])
			#sample_index_003_1.Value -> store_named_attribute_003_3.Value
			topology_dssp.links.new(sample_index_003_1.outputs[0], store_named_attribute_003_3.inputs[3])
			#index_002_2.Index -> sample_index_2.Index
			topology_dssp.links.new(index_002_2.outputs[0], sample_index_2.inputs[2])
			#group_input_79.Selection -> store_named_attribute_003_3.Selection
			topology_dssp.links.new(group_input_79.outputs[1], store_named_attribute_003_3.inputs[1])
			#group_input_79.Atoms -> mn_topo_compute_backbone_001.Atoms
			topology_dssp.links.new(group_input_79.outputs[0], mn_topo_compute_backbone_001.inputs[0])
			#index_002_2.Index -> sample_index_001_3.Index
			topology_dssp.links.new(index_002_2.outputs[0], sample_index_001_3.inputs[2])
			return topology_dssp

		topology_dssp = topology_dssp_node_group()

		#initialize _sampleatomvalue node group
		def _sampleatomvalue_node_group():
			_sampleatomvalue = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".SampleAtomValue")

			_sampleatomvalue.color_tag = 'NONE'
			_sampleatomvalue.description = ""

			_sampleatomvalue.is_modifier = True
			
			#_sampleatomvalue interface
			#Socket Atoms
			atoms_socket_15 = _sampleatomvalue.interface.new_socket(name = "Atoms", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_15.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_16 = _sampleatomvalue.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			value_socket_16.subtype = 'NONE'
			value_socket_16.default_value = (0.0, 0.0, 0.0)
			value_socket_16.min_value = -3.4028234663852886e+38
			value_socket_16.max_value = 3.4028234663852886e+38
			value_socket_16.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_17 = _sampleatomvalue.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketColor')
			value_socket_17.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_14 = _sampleatomvalue.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_14.attribute_domain = 'POINT'
			
			#Socket B
			b_socket_3 = _sampleatomvalue.interface.new_socket(name = "B", in_out='INPUT', socket_type = 'NodeSocketInt')
			b_socket_3.subtype = 'NONE'
			b_socket_3.default_value = 57
			b_socket_3.min_value = -2147483648
			b_socket_3.max_value = 2147483647
			b_socket_3.attribute_domain = 'POINT'
			
			
			#initialize _sampleatomvalue nodes
			#node Group Output
			group_output_82 = _sampleatomvalue.nodes.new("NodeGroupOutput")
			group_output_82.name = "Group Output"
			group_output_82.is_active_output = True
			
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
			position_002_2 = _sampleatomvalue.nodes.new("GeometryNodeInputPosition")
			position_002_2.name = "Position.002"
			
			#node Compare.003
			compare_003_3 = _sampleatomvalue.nodes.new("FunctionNodeCompare")
			compare_003_3.name = "Compare.003"
			compare_003_3.data_type = 'INT'
			compare_003_3.mode = 'ELEMENT'
			compare_003_3.operation = 'EQUAL'
			
			#node Group Input
			group_input_80 = _sampleatomvalue.nodes.new("NodeGroupInput")
			group_input_80.name = "Group Input"
			
			#node Sample Index.009
			sample_index_009_1 = _sampleatomvalue.nodes.new("GeometryNodeSampleIndex")
			sample_index_009_1.name = "Sample Index.009"
			sample_index_009_1.clamp = False
			sample_index_009_1.data_type = 'FLOAT_VECTOR'
			sample_index_009_1.domain = 'POINT'
			
			#node Named Attribute
			named_attribute_13 = _sampleatomvalue.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_13.name = "Named Attribute"
			named_attribute_13.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute_13.inputs[0].default_value = "Color"
			
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
			group_output_82.location = (390.0, 0.0)
			named_attribute_009.location = (-200.0, -107.52880859375)
			index_005.location = (40.0, -47.52880859375)
			position_002_2.location = (40.0, 12.47119140625)
			compare_003_3.location = (40.2109375, -112.47119140625)
			group_input_80.location = (-170.3642578125, -265.140380859375)
			sample_index_009_1.location = (200.0, 112.47119140625)
			named_attribute_13.location = (40.0, -380.0)
			sample_index_010_1.location = (200.0, -280.0)
			separate_geometry_002_1.location = (200.0, -107.52880859375)
			
			#Set dimensions
			group_output_82.width, group_output_82.height = 140.0, 100.0
			named_attribute_009.width, named_attribute_009.height = 206.99917602539062, 100.0
			index_005.width, index_005.height = 140.0, 100.0
			position_002_2.width, position_002_2.height = 140.0, 100.0
			compare_003_3.width, compare_003_3.height = 140.0, 100.0
			group_input_80.width, group_input_80.height = 140.0, 100.0
			sample_index_009_1.width, sample_index_009_1.height = 140.0, 100.0
			named_attribute_13.width, named_attribute_13.height = 140.0, 100.0
			sample_index_010_1.width, sample_index_010_1.height = 140.0, 100.0
			separate_geometry_002_1.width, separate_geometry_002_1.height = 140.0, 100.0
			
			#initialize _sampleatomvalue links
			#index_005.Index -> sample_index_009_1.Index
			_sampleatomvalue.links.new(index_005.outputs[0], sample_index_009_1.inputs[2])
			#compare_003_3.Result -> separate_geometry_002_1.Selection
			_sampleatomvalue.links.new(compare_003_3.outputs[0], separate_geometry_002_1.inputs[1])
			#named_attribute_009.Attribute -> compare_003_3.A
			_sampleatomvalue.links.new(named_attribute_009.outputs[0], compare_003_3.inputs[2])
			#separate_geometry_002_1.Selection -> sample_index_009_1.Geometry
			_sampleatomvalue.links.new(separate_geometry_002_1.outputs[0], sample_index_009_1.inputs[0])
			#position_002_2.Position -> sample_index_009_1.Value
			_sampleatomvalue.links.new(position_002_2.outputs[0], sample_index_009_1.inputs[1])
			#group_input_80.Geometry -> separate_geometry_002_1.Geometry
			_sampleatomvalue.links.new(group_input_80.outputs[0], separate_geometry_002_1.inputs[0])
			#group_input_80.B -> compare_003_3.B
			_sampleatomvalue.links.new(group_input_80.outputs[1], compare_003_3.inputs[3])
			#sample_index_009_1.Value -> group_output_82.Value
			_sampleatomvalue.links.new(sample_index_009_1.outputs[0], group_output_82.inputs[1])
			#index_005.Index -> sample_index_010_1.Index
			_sampleatomvalue.links.new(index_005.outputs[0], sample_index_010_1.inputs[2])
			#separate_geometry_002_1.Selection -> sample_index_010_1.Geometry
			_sampleatomvalue.links.new(separate_geometry_002_1.outputs[0], sample_index_010_1.inputs[0])
			#named_attribute_13.Attribute -> sample_index_010_1.Value
			_sampleatomvalue.links.new(named_attribute_13.outputs[0], sample_index_010_1.inputs[1])
			#sample_index_010_1.Value -> group_output_82.Value
			_sampleatomvalue.links.new(sample_index_010_1.outputs[0], group_output_82.inputs[2])
			#separate_geometry_002_1.Selection -> group_output_82.Atoms
			_sampleatomvalue.links.new(separate_geometry_002_1.outputs[0], group_output_82.inputs[0])
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
			group_input_81 = mn_select_nucleic_type.nodes.new("NodeGroupInput")
			group_input_81.name = "Group Input"
			
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
			boolean_math_007_2 = mn_select_nucleic_type.nodes.new("FunctionNodeBooleanMath")
			boolean_math_007_2.name = "Boolean Math.007"
			boolean_math_007_2.operation = 'OR'
			
			#node Group Output
			group_output_83 = mn_select_nucleic_type.nodes.new("NodeGroupOutput")
			group_output_83.name = "Group Output"
			group_output_83.is_active_output = True
			
			#node Compare.017
			compare_017 = mn_select_nucleic_type.nodes.new("FunctionNodeCompare")
			compare_017.name = "Compare.017"
			compare_017.data_type = 'INT'
			compare_017.mode = 'ELEMENT'
			compare_017.operation = 'EQUAL'
			#B_INT
			compare_017.inputs[3].default_value = 42
			
			#node Compare.010
			compare_010_1 = mn_select_nucleic_type.nodes.new("FunctionNodeCompare")
			compare_010_1.name = "Compare.010"
			compare_010_1.data_type = 'INT'
			compare_010_1.mode = 'ELEMENT'
			compare_010_1.operation = 'EQUAL'
			#B_INT
			compare_010_1.inputs[3].default_value = 30
			
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
			compare_009_1 = mn_select_nucleic_type.nodes.new("FunctionNodeCompare")
			compare_009_1.name = "Compare.009"
			compare_009_1.data_type = 'INT'
			compare_009_1.mode = 'ELEMENT'
			compare_009_1.operation = 'EQUAL'
			#B_INT
			compare_009_1.inputs[3].default_value = 32
			
			#node Boolean Math.008
			boolean_math_008_2 = mn_select_nucleic_type.nodes.new("FunctionNodeBooleanMath")
			boolean_math_008_2.name = "Boolean Math.008"
			boolean_math_008_2.operation = 'OR'
			
			
			
			
			#Set locations
			group_input_81.location = (-570.0, 0.0)
			reroute_015_1.location = (-150.0, -97.31201171875)
			named_attribute_010.location = (-420.0, -60.0)
			compare_007.location = (-30.0, -90.0)
			compare_016.location = (-30.0, -250.0)
			compare_008.location = (-30.0, 249.9998779296875)
			compare_015.location = (-30.0, 89.9998779296875)
			boolean_math_012.location = (170.0, 249.9998779296875)
			boolean_math_013.location = (150.0, -90.0)
			boolean_math_007_2.location = (370.0, 249.9998779296875)
			group_output_83.location = (580.0, 240.0)
			compare_017.location = (-40.0, -940.0)
			compare_010_1.location = (-40.0, -440.0)
			compare_018.location = (-40.0, -600.0)
			boolean_math_014.location = (160.0, -440.0)
			boolean_math_015.location = (140.0, -780.0)
			compare_009_1.location = (-40.0, -780.0)
			boolean_math_008_2.location = (360.0, -440.0)
			
			#Set dimensions
			group_input_81.width, group_input_81.height = 140.0, 100.0
			reroute_015_1.width, reroute_015_1.height = 16.0, 100.0
			named_attribute_010.width, named_attribute_010.height = 206.99917602539062, 100.0
			compare_007.width, compare_007.height = 140.0, 100.0
			compare_016.width, compare_016.height = 140.0, 100.0
			compare_008.width, compare_008.height = 140.0, 100.0
			compare_015.width, compare_015.height = 140.0, 100.0
			boolean_math_012.width, boolean_math_012.height = 140.0, 100.0
			boolean_math_013.width, boolean_math_013.height = 140.0, 100.0
			boolean_math_007_2.width, boolean_math_007_2.height = 140.0, 100.0
			group_output_83.width, group_output_83.height = 140.0, 100.0
			compare_017.width, compare_017.height = 140.0, 100.0
			compare_010_1.width, compare_010_1.height = 140.0, 100.0
			compare_018.width, compare_018.height = 140.0, 100.0
			boolean_math_014.width, boolean_math_014.height = 140.0, 100.0
			boolean_math_015.width, boolean_math_015.height = 140.0, 100.0
			compare_009_1.width, compare_009_1.height = 140.0, 100.0
			boolean_math_008_2.width, boolean_math_008_2.height = 140.0, 100.0
			
			#initialize mn_select_nucleic_type links
			#compare_016.Result -> boolean_math_013.Boolean
			mn_select_nucleic_type.links.new(compare_016.outputs[0], boolean_math_013.inputs[1])
			#reroute_015_1.Output -> compare_016.A
			mn_select_nucleic_type.links.new(reroute_015_1.outputs[0], compare_016.inputs[2])
			#boolean_math_012.Boolean -> boolean_math_007_2.Boolean
			mn_select_nucleic_type.links.new(boolean_math_012.outputs[0], boolean_math_007_2.inputs[0])
			#boolean_math_013.Boolean -> boolean_math_007_2.Boolean
			mn_select_nucleic_type.links.new(boolean_math_013.outputs[0], boolean_math_007_2.inputs[1])
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
			#boolean_math_007_2.Boolean -> group_output_83.is_pyrimidine
			mn_select_nucleic_type.links.new(boolean_math_007_2.outputs[0], group_output_83.inputs[1])
			#compare_017.Result -> boolean_math_015.Boolean
			mn_select_nucleic_type.links.new(compare_017.outputs[0], boolean_math_015.inputs[1])
			#reroute_015_1.Output -> compare_017.A
			mn_select_nucleic_type.links.new(reroute_015_1.outputs[0], compare_017.inputs[2])
			#boolean_math_014.Boolean -> boolean_math_008_2.Boolean
			mn_select_nucleic_type.links.new(boolean_math_014.outputs[0], boolean_math_008_2.inputs[0])
			#boolean_math_015.Boolean -> boolean_math_008_2.Boolean
			mn_select_nucleic_type.links.new(boolean_math_015.outputs[0], boolean_math_008_2.inputs[1])
			#reroute_015_1.Output -> compare_010_1.A
			mn_select_nucleic_type.links.new(reroute_015_1.outputs[0], compare_010_1.inputs[2])
			#compare_010_1.Result -> boolean_math_014.Boolean
			mn_select_nucleic_type.links.new(compare_010_1.outputs[0], boolean_math_014.inputs[0])
			#compare_009_1.Result -> boolean_math_015.Boolean
			mn_select_nucleic_type.links.new(compare_009_1.outputs[0], boolean_math_015.inputs[0])
			#reroute_015_1.Output -> compare_009_1.A
			mn_select_nucleic_type.links.new(reroute_015_1.outputs[0], compare_009_1.inputs[2])
			#reroute_015_1.Output -> compare_018.A
			mn_select_nucleic_type.links.new(reroute_015_1.outputs[0], compare_018.inputs[2])
			#compare_018.Result -> boolean_math_014.Boolean
			mn_select_nucleic_type.links.new(compare_018.outputs[0], boolean_math_014.inputs[1])
			#boolean_math_008_2.Boolean -> group_output_83.is_purine
			mn_select_nucleic_type.links.new(boolean_math_008_2.outputs[0], group_output_83.inputs[0])
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
			input_socket_6 = _base_align.interface.new_socket(name = "Input", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			input_socket_6.attribute_domain = 'POINT'
			
			
			#initialize _base_align nodes
			#node Switch.008
			switch_008_1 = _base_align.nodes.new("GeometryNodeSwitch")
			switch_008_1.name = "Switch.008"
			switch_008_1.input_type = 'INT'
			#False
			switch_008_1.inputs[1].default_value = 65
			#True
			switch_008_1.inputs[2].default_value = 68
			
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
			group_007_3 = _base_align.nodes.new("GeometryNodeGroup")
			group_007_3.name = "Group.007"
			group_007_3.node_tree = mn_select_nucleic_type
			
			#node Group Input
			group_input_82 = _base_align.nodes.new("NodeGroupInput")
			group_input_82.name = "Group Input"
			
			#node Group.009
			group_009_8 = _base_align.nodes.new("GeometryNodeGroup")
			group_009_8.name = "Group.009"
			group_009_8.node_tree = _sampleatomvalue
			
			#node Group.010
			group_010_7 = _base_align.nodes.new("GeometryNodeGroup")
			group_010_7.name = "Group.010"
			group_010_7.node_tree = _sampleatomvalue
			
			#node Group.008
			group_008_7 = _base_align.nodes.new("GeometryNodeGroup")
			group_008_7.name = "Group.008"
			group_008_7.node_tree = _sampleatomvalue
			#Input_1
			group_008_7.inputs[1].default_value = 61
			
			#node Vector Math.002
			vector_math_002_5 = _base_align.nodes.new("ShaderNodeVectorMath")
			vector_math_002_5.name = "Vector Math.002"
			vector_math_002_5.operation = 'SUBTRACT'
			
			#node Vector Math.004
			vector_math_004_4 = _base_align.nodes.new("ShaderNodeVectorMath")
			vector_math_004_4.name = "Vector Math.004"
			vector_math_004_4.operation = 'SUBTRACT'
			
			#node Group Output
			group_output_84 = _base_align.nodes.new("NodeGroupOutput")
			group_output_84.name = "Group Output"
			group_output_84.is_active_output = True
			
			
			
			
			#Set locations
			switch_008_1.location = (-30.387451171875, 0.0)
			reroute_018_1.location = (-150.387451171875, -200.0)
			switch_009.location = (-30.387451171875, -180.0)
			reroute_020.location = (-180.0, 80.0)
			group_007_3.location = (-433.26495361328125, -188.3114776611328)
			group_input_82.location = (-400.0, 120.0)
			group_009_8.location = (160.0, -200.0)
			group_010_7.location = (160.0, 40.0)
			group_008_7.location = (160.0, 280.0)
			vector_math_002_5.location = (400.0, -60.0)
			vector_math_004_4.location = (400.0, 100.0)
			group_output_84.location = (700.0, 140.0)
			
			#Set dimensions
			switch_008_1.width, switch_008_1.height = 145.0830078125, 100.0
			reroute_018_1.width, reroute_018_1.height = 16.0, 100.0
			switch_009.width, switch_009.height = 145.0830078125, 100.0
			reroute_020.width, reroute_020.height = 16.0, 100.0
			group_007_3.width, group_007_3.height = 221.22412109375, 100.0
			group_input_82.width, group_input_82.height = 140.0, 100.0
			group_009_8.width, group_009_8.height = 140.0, 100.0
			group_010_7.width, group_010_7.height = 140.0, 100.0
			group_008_7.width, group_008_7.height = 140.0, 100.0
			vector_math_002_5.width, vector_math_002_5.height = 140.0, 100.0
			vector_math_004_4.width, vector_math_004_4.height = 140.0, 100.0
			group_output_84.width, group_output_84.height = 140.0, 100.0
			
			#initialize _base_align links
			#switch_008_1.Output -> group_010_7.B
			_base_align.links.new(switch_008_1.outputs[0], group_010_7.inputs[1])
			#reroute_018_1.Output -> group_010_7.Geometry
			_base_align.links.new(reroute_018_1.outputs[0], group_010_7.inputs[0])
			#group_009_8.Value -> vector_math_002_5.Vector
			_base_align.links.new(group_009_8.outputs[1], vector_math_002_5.inputs[1])
			#group_007_3.is_pyrimidine -> switch_008_1.Switch
			_base_align.links.new(group_007_3.outputs[1], switch_008_1.inputs[0])
			#group_007_3.is_pyrimidine -> switch_009.Switch
			_base_align.links.new(group_007_3.outputs[1], switch_009.inputs[0])
			#reroute_018_1.Output -> group_009_8.Geometry
			_base_align.links.new(reroute_018_1.outputs[0], group_009_8.inputs[0])
			#reroute_020.Output -> reroute_018_1.Input
			_base_align.links.new(reroute_020.outputs[0], reroute_018_1.inputs[0])
			#switch_009.Output -> group_009_8.B
			_base_align.links.new(switch_009.outputs[0], group_009_8.inputs[1])
			#group_008_7.Value -> vector_math_004_4.Vector
			_base_align.links.new(group_008_7.outputs[1], vector_math_004_4.inputs[1])
			#reroute_020.Output -> group_008_7.Geometry
			_base_align.links.new(reroute_020.outputs[0], group_008_7.inputs[0])
			#group_009_8.Value -> vector_math_004_4.Vector
			_base_align.links.new(group_009_8.outputs[1], vector_math_004_4.inputs[0])
			#group_010_7.Value -> vector_math_002_5.Vector
			_base_align.links.new(group_010_7.outputs[1], vector_math_002_5.inputs[0])
			#group_input_82.Input -> reroute_020.Input
			_base_align.links.new(group_input_82.outputs[0], reroute_020.inputs[0])
			#group_009_8.Value -> group_output_84.Base Interface
			_base_align.links.new(group_009_8.outputs[1], group_output_84.inputs[0])
			#group_008_7.Value -> group_output_84.Base Pivot
			_base_align.links.new(group_008_7.outputs[1], group_output_84.inputs[1])
			#vector_math_004_4.Vector -> group_output_84.Align Vertical
			_base_align.links.new(vector_math_004_4.outputs[0], group_output_84.inputs[2])
			#vector_math_002_5.Vector -> group_output_84.Align Horizontal
			_base_align.links.new(vector_math_002_5.outputs[0], group_output_84.inputs[3])
			return _base_align

		_base_align = _base_align_node_group()

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
			atoms_socket_16 = _mn_utils_style_ribbon_nucleic.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_16.attribute_domain = 'POINT'
			atoms_socket_16.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket_21 = _mn_utils_style_ribbon_nucleic.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_21.attribute_domain = 'POINT'
			selection_socket_21.hide_value = True
			selection_socket_21.description = "Selection of atoms to apply this node to"
			
			#Socket Material
			material_socket_7 = _mn_utils_style_ribbon_nucleic.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial')
			material_socket_7.attribute_domain = 'POINT'
			material_socket_7.description = "Material to apply to the resulting geometry"
			
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
			frame_002_4 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeFrame")
			frame_002_4.label = "Transfer attributes to new curve / mesh from alpha carbons"
			frame_002_4.name = "Frame.002"
			frame_002_4.label_size = 20
			frame_002_4.shrink = True
			
			#node Frame
			frame_16 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeFrame")
			frame_16.label = "Delete between chains and distance too large"
			frame_16.name = "Frame"
			frame_16.label_size = 20
			frame_16.shrink = True
			
			#node Frame.001
			frame_001_10 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeFrame")
			frame_001_10.label = "Create New mesh line through all CA"
			frame_001_10.name = "Frame.001"
			frame_001_10.label_size = 20
			frame_001_10.shrink = True
			
			#node Frame.006
			frame_006_2 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeFrame")
			frame_006_2.label = "Slightly Extend Curve Ends"
			frame_006_2.name = "Frame.006"
			frame_006_2.label_size = 20
			frame_006_2.shrink = True
			
			#node Frame.004
			frame_004_2 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeFrame")
			frame_004_2.label = "Convert Mesh Backbone to Curve"
			frame_004_2.name = "Frame.004"
			frame_004_2.label_size = 20
			frame_004_2.shrink = True
			
			#node Frame.005
			frame_005_2 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeFrame")
			frame_005_2.label = "Instance simple base cylinder"
			frame_005_2.name = "Frame.005"
			frame_005_2.label_size = 20
			frame_005_2.shrink = True
			
			#node Frame.007
			frame_007_2 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeFrame")
			frame_007_2.label = "Align Base"
			frame_007_2.name = "Frame.007"
			frame_007_2.label_size = 20
			frame_007_2.shrink = True
			
			#node Frame.003
			frame_003_4 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeFrame")
			frame_003_4.label = "Create mesh from curve"
			frame_003_4.name = "Frame.003"
			frame_003_4.label_size = 20
			frame_003_4.shrink = True
			
			#node Sample Index
			sample_index_3 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSampleIndex")
			sample_index_3.name = "Sample Index"
			sample_index_3.hide = True
			sample_index_3.clamp = True
			sample_index_3.data_type = 'INT'
			sample_index_3.domain = 'POINT'
			
			#node Named Attribute.002
			named_attribute_002_6 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002_6.label = "chain_id"
			named_attribute_002_6.name = "Named Attribute.002"
			named_attribute_002_6.hide = True
			named_attribute_002_6.data_type = 'INT'
			#Name
			named_attribute_002_6.inputs[0].default_value = "chain_id"
			
			#node Sample Index.004
			sample_index_004 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSampleIndex")
			sample_index_004.name = "Sample Index.004"
			sample_index_004.hide = True
			sample_index_004.clamp = True
			sample_index_004.data_type = 'INT'
			sample_index_004.domain = 'POINT'
			
			#node Named Attribute.004
			named_attribute_004_3 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_004_3.label = "res_id"
			named_attribute_004_3.name = "Named Attribute.004"
			named_attribute_004_3.hide = True
			named_attribute_004_3.data_type = 'INT'
			#Name
			named_attribute_004_3.inputs[0].default_value = "res_id"
			
			#node Sample Index.001
			sample_index_001_4 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSampleIndex")
			sample_index_001_4.name = "Sample Index.001"
			sample_index_001_4.hide = True
			sample_index_001_4.clamp = True
			sample_index_001_4.data_type = 'FLOAT_COLOR'
			sample_index_001_4.domain = 'POINT'
			
			#node Named Attribute
			named_attribute_14 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_14.label = "Color"
			named_attribute_14.name = "Named Attribute"
			named_attribute_14.hide = True
			named_attribute_14.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute_14.inputs[0].default_value = "Color"
			
			#node Reroute.003
			reroute_003_7 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_003_7.name = "Reroute.003"
			#node Sample Index.003
			sample_index_003_2 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSampleIndex")
			sample_index_003_2.name = "Sample Index.003"
			sample_index_003_2.hide = True
			sample_index_003_2.clamp = True
			sample_index_003_2.data_type = 'INT'
			sample_index_003_2.domain = 'POINT'
			
			#node Named Attribute.003
			named_attribute_003_3 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_003_3.label = "res_name"
			named_attribute_003_3.name = "Named Attribute.003"
			named_attribute_003_3.hide = True
			named_attribute_003_3.data_type = 'INT'
			#Name
			named_attribute_003_3.inputs[0].default_value = "res_name"
			
			#node Index.003
			index_003_2 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputIndex")
			index_003_2.name = "Index.003"
			
			#node Named Attribute.005
			named_attribute_005_2 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_005_2.label = "b_factor"
			named_attribute_005_2.name = "Named Attribute.005"
			named_attribute_005_2.hide = True
			named_attribute_005_2.data_type = 'FLOAT'
			#Name
			named_attribute_005_2.inputs[0].default_value = "b_factor"
			
			#node Sample Index.005
			sample_index_005_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSampleIndex")
			sample_index_005_1.name = "Sample Index.005"
			sample_index_005_1.hide = True
			sample_index_005_1.clamp = True
			sample_index_005_1.data_type = 'FLOAT'
			sample_index_005_1.domain = 'POINT'
			
			#node Reroute.001
			reroute_001_15 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_001_15.name = "Reroute.001"
			#node Reroute.010
			reroute_010_3 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_010_3.name = "Reroute.010"
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
			reroute_002_11 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_002_11.name = "Reroute.002"
			#node Edge Vertices
			edge_vertices_2 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputMeshEdgeVertices")
			edge_vertices_2.name = "Edge Vertices"
			
			#node Field at Index
			field_at_index_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeFieldAtIndex")
			field_at_index_1.name = "Field at Index"
			field_at_index_1.data_type = 'INT'
			field_at_index_1.domain = 'POINT'
			
			#node Field at Index.001
			field_at_index_001 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeFieldAtIndex")
			field_at_index_001.name = "Field at Index.001"
			field_at_index_001.data_type = 'INT'
			field_at_index_001.domain = 'POINT'
			
			#node Vector Math
			vector_math_14 = _mn_utils_style_ribbon_nucleic.nodes.new("ShaderNodeVectorMath")
			vector_math_14.name = "Vector Math"
			vector_math_14.operation = 'DISTANCE'
			
			#node Compare.001
			compare_001_11 = _mn_utils_style_ribbon_nucleic.nodes.new("FunctionNodeCompare")
			compare_001_11.name = "Compare.001"
			compare_001_11.data_type = 'FLOAT'
			compare_001_11.mode = 'ELEMENT'
			compare_001_11.operation = 'GREATER_THAN'
			#B
			compare_001_11.inputs[1].default_value = 0.10000000149011612
			
			#node Compare
			compare_18 = _mn_utils_style_ribbon_nucleic.nodes.new("FunctionNodeCompare")
			compare_18.name = "Compare"
			compare_18.data_type = 'INT'
			compare_18.mode = 'ELEMENT'
			compare_18.operation = 'NOT_EQUAL'
			
			#node Boolean Math
			boolean_math_20 = _mn_utils_style_ribbon_nucleic.nodes.new("FunctionNodeBooleanMath")
			boolean_math_20.name = "Boolean Math"
			boolean_math_20.operation = 'OR'
			
			#node Reroute.009
			reroute_009_3 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_009_3.name = "Reroute.009"
			#node Reroute.012
			reroute_012_2 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_012_2.name = "Reroute.012"
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
			set_position_5 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSetPosition")
			set_position_5.name = "Set Position"
			set_position_5.hide = True
			#Selection
			set_position_5.inputs[1].default_value = True
			#Offset
			set_position_5.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Domain Size
			domain_size_4 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeAttributeDomainSize")
			domain_size_4.name = "Domain Size"
			domain_size_4.hide = True
			domain_size_4.component = 'MESH'
			domain_size_4.outputs[1].hide = True
			domain_size_4.outputs[2].hide = True
			domain_size_4.outputs[3].hide = True
			domain_size_4.outputs[4].hide = True
			domain_size_4.outputs[5].hide = True
			
			#node Delete Geometry
			delete_geometry_2 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeDeleteGeometry")
			delete_geometry_2.name = "Delete Geometry"
			delete_geometry_2.domain = 'EDGE'
			delete_geometry_2.mode = 'ALL'
			
			#node Sample Index.009
			sample_index_009_2 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSampleIndex")
			sample_index_009_2.name = "Sample Index.009"
			sample_index_009_2.hide = True
			sample_index_009_2.clamp = True
			sample_index_009_2.data_type = 'BOOLEAN'
			sample_index_009_2.domain = 'POINT'
			
			#node Group Input.006
			group_input_006_1 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeGroupInput")
			group_input_006_1.name = "Group Input.006"
			group_input_006_1.outputs[0].hide = True
			group_input_006_1.outputs[1].hide = True
			group_input_006_1.outputs[2].hide = True
			group_input_006_1.outputs[3].hide = True
			group_input_006_1.outputs[4].hide = True
			group_input_006_1.outputs[5].hide = True
			group_input_006_1.outputs[8].hide = True
			group_input_006_1.outputs[9].hide = True
			group_input_006_1.outputs[10].hide = True
			
			#node Sample Index.007
			sample_index_007_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSampleIndex")
			sample_index_007_1.name = "Sample Index.007"
			sample_index_007_1.hide = True
			sample_index_007_1.clamp = True
			sample_index_007_1.data_type = 'FLOAT'
			sample_index_007_1.domain = 'POINT'
			
			#node Group Output
			group_output_85 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeGroupOutput")
			group_output_85.name = "Group Output"
			group_output_85.is_active_output = True
			
			#node Offset Point in Curve
			offset_point_in_curve = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeOffsetPointInCurve")
			offset_point_in_curve.name = "Offset Point in Curve"
			#Point Index
			offset_point_in_curve.inputs[0].default_value = 0
			
			#node Evaluate at Index
			evaluate_at_index_9 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_9.name = "Evaluate at Index"
			evaluate_at_index_9.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_9.domain = 'POINT'
			
			#node Position.002
			position_002_3 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputPosition")
			position_002_3.name = "Position.002"
			
			#node Vector Math.002
			vector_math_002_6 = _mn_utils_style_ribbon_nucleic.nodes.new("ShaderNodeVectorMath")
			vector_math_002_6.name = "Vector Math.002"
			vector_math_002_6.operation = 'SUBTRACT'
			
			#node Vector Math.004
			vector_math_004_5 = _mn_utils_style_ribbon_nucleic.nodes.new("ShaderNodeVectorMath")
			vector_math_004_5.name = "Vector Math.004"
			vector_math_004_5.operation = 'SCALE'
			#Scale
			vector_math_004_5.inputs[3].default_value = -0.5
			
			#node Endpoint Selection
			endpoint_selection_2 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_2.name = "Endpoint Selection"
			#Start Size
			endpoint_selection_2.inputs[0].default_value = 1
			#End Size
			endpoint_selection_2.inputs[1].default_value = 1
			
			#node Switch
			switch_20 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSwitch")
			switch_20.name = "Switch"
			switch_20.input_type = 'INT'
			#False
			switch_20.inputs[1].default_value = -1
			#True
			switch_20.inputs[2].default_value = 1
			
			#node Endpoint Selection.001
			endpoint_selection_001_3 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_001_3.name = "Endpoint Selection.001"
			#Start Size
			endpoint_selection_001_3.inputs[0].default_value = 1
			#End Size
			endpoint_selection_001_3.inputs[1].default_value = 0
			
			#node Set Position.001
			set_position_001_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSetPosition")
			set_position_001_1.name = "Set Position.001"
			#Position
			set_position_001_1.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Store Named Attribute.001
			store_named_attribute_001_4 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_001_4.name = "Store Named Attribute.001"
			store_named_attribute_001_4.data_type = 'INT'
			store_named_attribute_001_4.domain = 'POINT'
			#Selection
			store_named_attribute_001_4.inputs[1].default_value = True
			#Name
			store_named_attribute_001_4.inputs[2].default_value = "chain_id"
			
			#node Store Named Attribute.002
			store_named_attribute_002_4 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_002_4.name = "Store Named Attribute.002"
			store_named_attribute_002_4.data_type = 'INT'
			store_named_attribute_002_4.domain = 'POINT'
			#Selection
			store_named_attribute_002_4.inputs[1].default_value = True
			#Name
			store_named_attribute_002_4.inputs[2].default_value = "res_id"
			
			#node Store Named Attribute.003
			store_named_attribute_003_4 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_003_4.name = "Store Named Attribute.003"
			store_named_attribute_003_4.data_type = 'INT'
			store_named_attribute_003_4.domain = 'POINT'
			#Selection
			store_named_attribute_003_4.inputs[1].default_value = True
			#Name
			store_named_attribute_003_4.inputs[2].default_value = "res_name"
			
			#node Store Named Attribute.004
			store_named_attribute_004_4 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_004_4.name = "Store Named Attribute.004"
			store_named_attribute_004_4.data_type = 'FLOAT'
			store_named_attribute_004_4.domain = 'POINT'
			#Selection
			store_named_attribute_004_4.inputs[1].default_value = True
			#Name
			store_named_attribute_004_4.inputs[2].default_value = "b_factor"
			
			#node Capture Attribute
			capture_attribute_5 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute_5.name = "Capture Attribute"
			capture_attribute_5.active_index = 0
			capture_attribute_5.capture_items.clear()
			capture_attribute_5.capture_items.new('FLOAT', "Value")
			capture_attribute_5.capture_items["Value"].data_type = 'BOOLEAN'
			capture_attribute_5.domain = 'POINT'
			
			#node Set Handle Type
			set_handle_type_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeCurveSetHandles")
			set_handle_type_1.name = "Set Handle Type"
			set_handle_type_1.handle_type = 'AUTO'
			set_handle_type_1.mode = {'LEFT', 'RIGHT'}
			#Selection
			set_handle_type_1.inputs[1].default_value = True
			
			#node Set Spline Type
			set_spline_type_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeCurveSplineType")
			set_spline_type_1.name = "Set Spline Type"
			set_spline_type_1.spline_type = 'BEZIER'
			#Selection
			set_spline_type_1.inputs[1].default_value = True
			
			#node Group Input.004
			group_input_004_2 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeGroupInput")
			group_input_004_2.name = "Group Input.004"
			group_input_004_2.outputs[0].hide = True
			group_input_004_2.outputs[1].hide = True
			group_input_004_2.outputs[2].hide = True
			group_input_004_2.outputs[3].hide = True
			group_input_004_2.outputs[5].hide = True
			group_input_004_2.outputs[6].hide = True
			group_input_004_2.outputs[7].hide = True
			group_input_004_2.outputs[8].hide = True
			group_input_004_2.outputs[9].hide = True
			group_input_004_2.outputs[10].hide = True
			
			#node Mesh to Curve
			mesh_to_curve_3 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeMeshToCurve")
			mesh_to_curve_3.name = "Mesh to Curve"
			#Selection
			mesh_to_curve_3.inputs[1].default_value = True
			
			#node Set Spline Resolution
			set_spline_resolution_2 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSetSplineResolution")
			set_spline_resolution_2.name = "Set Spline Resolution"
			#Selection
			set_spline_resolution_2.inputs[1].default_value = True
			
			#node Store Named Attribute
			store_named_attribute_8 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_8.name = "Store Named Attribute"
			store_named_attribute_8.data_type = 'FLOAT_COLOR'
			store_named_attribute_8.domain = 'POINT'
			#Selection
			store_named_attribute_8.inputs[1].default_value = True
			#Name
			store_named_attribute_8.inputs[2].default_value = "Color"
			
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
			combine_xyz_2 = _mn_utils_style_ribbon_nucleic.nodes.new("ShaderNodeCombineXYZ")
			combine_xyz_2.name = "Combine XYZ"
			#X
			combine_xyz_2.inputs[0].default_value = 0.0
			#Y
			combine_xyz_2.inputs[1].default_value = 0.0
			
			#node Math
			math_24 = _mn_utils_style_ribbon_nucleic.nodes.new("ShaderNodeMath")
			math_24.name = "Math"
			math_24.operation = 'DIVIDE'
			math_24.use_clamp = False
			#Value_001
			math_24.inputs[1].default_value = 2.0
			
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
			group_input_005_2 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeGroupInput")
			group_input_005_2.name = "Group Input.005"
			group_input_005_2.outputs[0].hide = True
			group_input_005_2.outputs[1].hide = True
			group_input_005_2.outputs[2].hide = True
			group_input_005_2.outputs[3].hide = True
			group_input_005_2.outputs[4].hide = True
			group_input_005_2.outputs[5].hide = True
			group_input_005_2.outputs[6].hide = True
			group_input_005_2.outputs[7].hide = True
			group_input_005_2.outputs[10].hide = True
			
			#node Store Named Attribute.006
			store_named_attribute_006_2 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_006_2.name = "Store Named Attribute.006"
			store_named_attribute_006_2.data_type = 'FLOAT_VECTOR'
			store_named_attribute_006_2.domain = 'CORNER'
			#Selection
			store_named_attribute_006_2.inputs[1].default_value = True
			#Name
			store_named_attribute_006_2.inputs[2].default_value = "uv_map"
			
			#node Position.001
			position_001_6 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputPosition")
			position_001_6.name = "Position.001"
			
			#node Store Named Attribute.005
			store_named_attribute_005_4 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_005_4.name = "Store Named Attribute.005"
			store_named_attribute_005_4.data_type = 'FLOAT_COLOR'
			store_named_attribute_005_4.domain = 'POINT'
			#Selection
			store_named_attribute_005_4.inputs[1].default_value = True
			#Name
			store_named_attribute_005_4.inputs[2].default_value = "Color"
			
			#node Separate Geometry
			separate_geometry_9 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_9.name = "Separate Geometry"
			separate_geometry_9.domain = 'POINT'
			
			#node Group Input
			group_input_83 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeGroupInput")
			group_input_83.name = "Group Input"
			group_input_83.outputs[3].hide = True
			
			#node Group.004
			group_004_6 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeGroup")
			group_004_6.name = "Group.004"
			group_004_6.node_tree = _sampleatomvalue
			#Input_1
			group_004_6.inputs[1].default_value = 67
			
			#node Reroute.006
			reroute_006_2 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_006_2.name = "Reroute.006"
			#node Reroute.011
			reroute_011_2 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_011_2.name = "Reroute.011"
			#node Group.006
			group_006_6 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeGroup")
			group_006_6.name = "Group.006"
			group_006_6.node_tree = _base_align
			
			#node Transform
			transform = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeTransform")
			transform.name = "Transform"
			transform.mode = 'COMPONENTS'
			#Rotation
			transform.inputs[2].default_value = (0.0, 0.0, 0.7853981852531433)
			#Scale
			transform.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Instance on Points
			instance_on_points_3 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInstanceOnPoints")
			instance_on_points_3.name = "Instance on Points"
			#Selection
			instance_on_points_3.inputs[1].default_value = True
			#Pick Instance
			instance_on_points_3.inputs[3].default_value = False
			#Instance Index
			instance_on_points_3.inputs[4].default_value = 0
			
			#node Group.003
			group_003_8 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeGroup")
			group_003_8.name = "Group.003"
			group_003_8.node_tree = _sampleatomvalue
			#Input_1
			group_003_8.inputs[1].default_value = 55
			
			#node Combine XYZ.001
			combine_xyz_001_2 = _mn_utils_style_ribbon_nucleic.nodes.new("ShaderNodeCombineXYZ")
			combine_xyz_001_2.name = "Combine XYZ.001"
			#X
			combine_xyz_001_2.inputs[0].default_value = 0.019999999552965164
			#Y
			combine_xyz_001_2.inputs[1].default_value = 0.10000000149011612
			
			#node Vector Math.003
			vector_math_003_5 = _mn_utils_style_ribbon_nucleic.nodes.new("ShaderNodeVectorMath")
			vector_math_003_5.name = "Vector Math.003"
			vector_math_003_5.operation = 'LENGTH'
			
			#node Vector Math.001
			vector_math_001_6 = _mn_utils_style_ribbon_nucleic.nodes.new("ShaderNodeVectorMath")
			vector_math_001_6.name = "Vector Math.001"
			vector_math_001_6.operation = 'SUBTRACT'
			
			#node Align Euler to Vector.001
			align_euler_to_vector_001_1 = _mn_utils_style_ribbon_nucleic.nodes.new("FunctionNodeAlignEulerToVector")
			align_euler_to_vector_001_1.name = "Align Euler to Vector.001"
			align_euler_to_vector_001_1.axis = 'Y'
			align_euler_to_vector_001_1.pivot_axis = 'Z'
			#Factor
			align_euler_to_vector_001_1.inputs[1].default_value = 1.0
			
			#node Align Euler to Vector
			align_euler_to_vector_2 = _mn_utils_style_ribbon_nucleic.nodes.new("FunctionNodeAlignEulerToVector")
			align_euler_to_vector_2.name = "Align Euler to Vector"
			align_euler_to_vector_2.axis = 'Z'
			align_euler_to_vector_2.pivot_axis = 'AUTO'
			#Rotation
			align_euler_to_vector_2.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Factor
			align_euler_to_vector_2.inputs[1].default_value = 1.0
			
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
			index_9 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputIndex")
			index_9.name = "Index"
			
			#node Named Attribute.009
			named_attribute_009_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_009_1.name = "Named Attribute.009"
			named_attribute_009_1.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute_009_1.inputs[0].default_value = "Color"
			
			#node Sample Index.002
			sample_index_002_2 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSampleIndex")
			sample_index_002_2.name = "Sample Index.002"
			sample_index_002_2.clamp = False
			sample_index_002_2.data_type = 'FLOAT_COLOR'
			sample_index_002_2.domain = 'POINT'
			
			#node Reroute.004
			reroute_004_2 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_004_2.name = "Reroute.004"
			#node Set Shade Smooth
			set_shade_smooth_2 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSetShadeSmooth")
			set_shade_smooth_2.name = "Set Shade Smooth"
			set_shade_smooth_2.domain = 'FACE'
			#Selection
			set_shade_smooth_2.inputs[1].default_value = True
			
			#node Reroute.007
			reroute_007_3 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_007_3.name = "Reroute.007"
			#node Curve Circle
			curve_circle_3 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeCurvePrimitiveCircle")
			curve_circle_3.name = "Curve Circle"
			curve_circle_3.hide = True
			curve_circle_3.mode = 'RADIUS'
			#Radius
			curve_circle_3.inputs[4].default_value = 0.009999999776482582
			
			#node Group Input.003
			group_input_003_4 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeGroupInput")
			group_input_003_4.name = "Group Input.003"
			group_input_003_4.outputs[0].hide = True
			group_input_003_4.outputs[1].hide = True
			group_input_003_4.outputs[2].hide = True
			group_input_003_4.outputs[3].hide = True
			group_input_003_4.outputs[4].hide = True
			group_input_003_4.outputs[6].hide = True
			group_input_003_4.outputs[7].hide = True
			group_input_003_4.outputs[8].hide = True
			group_input_003_4.outputs[9].hide = True
			group_input_003_4.outputs[10].hide = True
			
			#node Set Material
			set_material_4 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSetMaterial")
			set_material_4.name = "Set Material"
			#Selection
			set_material_4.inputs[1].default_value = True
			
			#node Reroute.005
			reroute_005_3 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_005_3.name = "Reroute.005"
			#node Reroute.008
			reroute_008_2 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_008_2.name = "Reroute.008"
			#node Curve to Mesh
			curve_to_mesh_4 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeCurveToMesh")
			curve_to_mesh_4.name = "Curve to Mesh"
			#Fill Caps
			curve_to_mesh_4.inputs[2].default_value = True
			
			#node Set Curve Radius
			set_curve_radius_3 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSetCurveRadius")
			set_curve_radius_3.name = "Set Curve Radius"
			#Selection
			set_curve_radius_3.inputs[1].default_value = True
			
			#node Group Input.002
			group_input_002_5 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeGroupInput")
			group_input_002_5.name = "Group Input.002"
			group_input_002_5.outputs[0].hide = True
			group_input_002_5.outputs[1].hide = True
			group_input_002_5.outputs[3].hide = True
			group_input_002_5.outputs[4].hide = True
			group_input_002_5.outputs[5].hide = True
			group_input_002_5.outputs[6].hide = True
			group_input_002_5.outputs[7].hide = True
			group_input_002_5.outputs[8].hide = True
			group_input_002_5.outputs[9].hide = True
			group_input_002_5.outputs[10].hide = True
			
			#node Join Geometry.001
			join_geometry_001_4 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_001_4.name = "Join Geometry.001"
			join_geometry_001_4.hide = True
			
			#node Reroute.013
			reroute_013_2 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_013_2.name = "Reroute.013"
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
			switch_001_6 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeSwitch")
			switch_001_6.name = "Switch.001"
			switch_001_6.input_type = 'GEOMETRY'
			
			#node Group Input.001
			group_input_001_11 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeGroupInput")
			group_input_001_11.name = "Group Input.001"
			group_input_001_11.outputs[0].hide = True
			group_input_001_11.outputs[1].hide = True
			group_input_001_11.outputs[2].hide = True
			group_input_001_11.outputs[4].hide = True
			group_input_001_11.outputs[5].hide = True
			group_input_001_11.outputs[6].hide = True
			group_input_001_11.outputs[7].hide = True
			group_input_001_11.outputs[8].hide = True
			group_input_001_11.outputs[9].hide = True
			group_input_001_11.outputs[10].hide = True
			
			#node Group
			group_29 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeGroup")
			group_29.name = "Group"
			group_29.node_tree = residue_mask
			#Socket_1
			group_29.inputs[0].default_value = 1
			#Socket_5
			group_29.inputs[1].default_value = True
			#Socket_4
			group_29.inputs[2].default_value = 0
			
			#node Is Nucleic
			is_nucleic_1 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeGroup")
			is_nucleic_1.label = "Is Nucleic"
			is_nucleic_1.name = "Is Nucleic"
			is_nucleic_1.node_tree = is_nucleic
			#Socket_3
			is_nucleic_1.inputs[1].default_value = False
			
			#node Group.005
			group_005_8 = _mn_utils_style_ribbon_nucleic.nodes.new("GeometryNodeGroup")
			group_005_8.name = "Group.005"
			group_005_8.node_tree = _sampleatomvalue
			#Input_1
			group_005_8.inputs[1].default_value = 57
			
			#node Reroute
			reroute_22 = _mn_utils_style_ribbon_nucleic.nodes.new("NodeReroute")
			reroute_22.name = "Reroute"
			#node Mix
			mix_1 = _mn_utils_style_ribbon_nucleic.nodes.new("ShaderNodeMix")
			mix_1.name = "Mix"
			mix_1.blend_type = 'MIX'
			mix_1.clamp_factor = True
			mix_1.clamp_result = False
			mix_1.data_type = 'VECTOR'
			mix_1.factor_mode = 'UNIFORM'
			#Factor_Float
			mix_1.inputs[0].default_value = 1.0
			
			
			
			#Set parents
			sample_index_3.parent = frame_002_4
			named_attribute_002_6.parent = frame_002_4
			sample_index_004.parent = frame_002_4
			named_attribute_004_3.parent = frame_002_4
			sample_index_001_4.parent = frame_002_4
			named_attribute_14.parent = frame_002_4
			reroute_003_7.parent = frame_002_4
			sample_index_003_2.parent = frame_002_4
			named_attribute_003_3.parent = frame_002_4
			index_003_2.parent = frame_002_4
			named_attribute_005_2.parent = frame_002_4
			sample_index_005_1.parent = frame_002_4
			reroute_001_15.parent = frame_002_4
			sample_index_008_1.parent = frame_16
			named_attribute_006_1.parent = frame_16
			index_004.parent = frame_16
			reroute_002_11.parent = frame_16
			edge_vertices_2.parent = frame_16
			field_at_index_1.parent = frame_16
			field_at_index_001.parent = frame_16
			vector_math_14.parent = frame_16
			compare_001_11.parent = frame_16
			compare_18.parent = frame_16
			boolean_math_20.parent = frame_16
			mesh_line_1.parent = frame_001_10
			set_position_5.parent = frame_001_10
			domain_size_4.parent = frame_001_10
			delete_geometry_2.parent = frame_16
			offset_point_in_curve.parent = frame_006_2
			evaluate_at_index_9.parent = frame_006_2
			position_002_3.parent = frame_006_2
			vector_math_002_6.parent = frame_006_2
			vector_math_004_5.parent = frame_006_2
			endpoint_selection_2.parent = frame_006_2
			switch_20.parent = frame_006_2
			endpoint_selection_001_3.parent = frame_006_2
			set_position_001_1.parent = frame_006_2
			set_handle_type_1.parent = frame_004_2
			set_spline_type_1.parent = frame_004_2
			group_input_004_2.parent = frame_004_2
			mesh_to_curve_3.parent = frame_004_2
			set_spline_resolution_2.parent = frame_004_2
			combine_xyz_2.parent = frame_005_2
			math_24.parent = frame_005_2
			cylinder.parent = frame_005_2
			value_1.parent = frame_005_2
			group_input_005_2.parent = frame_005_2
			store_named_attribute_006_2.parent = frame_005_2
			position_001_6.parent = frame_007_2
			transform.parent = frame_005_2
			instance_on_points_3.parent = frame_005_2
			combine_xyz_001_2.parent = frame_007_2
			vector_math_003_5.parent = frame_007_2
			vector_math_001_6.parent = frame_007_2
			align_euler_to_vector_001_1.parent = frame_007_2
			align_euler_to_vector_2.parent = frame_007_2
			named_attribute_007_1.parent = frame_007_2
			named_attribute_008_1.parent = frame_007_2
			reroute_004_2.parent = frame_003_4
			set_shade_smooth_2.parent = frame_003_4
			reroute_007_3.parent = frame_003_4
			curve_circle_3.parent = frame_003_4
			group_input_003_4.parent = frame_003_4
			reroute_005_3.parent = frame_003_4
			reroute_008_2.parent = frame_003_4
			curve_to_mesh_4.parent = frame_003_4
			set_curve_radius_3.parent = frame_003_4
			group_input_002_5.parent = frame_003_4
			join_geometry_001_4.parent = frame_003_4
			reroute_013_2.parent = frame_003_4
			
			#Set locations
			frame_002_4.location = (1158.6292724609375, -29.90658187866211)
			frame_16.location = (-740.1123657226562, 293.3905944824219)
			frame_001_10.location = (-721.0, 75.0)
			frame_006_2.location = (252.1446533203125, -22.4365234375)
			frame_004_2.location = (-210.0, 260.0)
			frame_005_2.location = (397.0, 475.0)
			frame_007_2.location = (2083.0, 37.0)
			frame_003_4.location = (58.0, -11.0)
			sample_index_3.location = (-660.0, 820.0)
			named_attribute_002_6.location = (-660.0, 780.0)
			sample_index_004.location = (-660.0, 880.0)
			named_attribute_004_3.location = (-660.0, 920.0)
			sample_index_001_4.location = (-664.6292724609375, 689.9065551757812)
			named_attribute_14.location = (-664.6292724609375, 729.9065551757812)
			reroute_003_7.location = (-784.6292724609375, 869.9065551757812)
			sample_index_003_2.location = (-660.0, 980.0)
			named_attribute_003_3.location = (-660.0, 1020.0)
			index_003_2.location = (-964.6292724609375, 909.9065551757812)
			named_attribute_005_2.location = (-664.6292724609375, 1109.9066162109375)
			sample_index_005_1.location = (-664.6292724609375, 1069.9066162109375)
			reroute_001_15.location = (-804.6292724609375, 969.9065551757812)
			reroute_010_3.location = (-6.0, 640.0)
			sample_index_008_1.location = (-259.96295166015625, -143.635009765625)
			named_attribute_006_1.location = (-439.96295166015625, -143.635009765625)
			index_004.location = (-439.96295166015625, -183.635009765625)
			reroute_002_11.location = (-100.0, -140.0)
			edge_vertices_2.location = (-220.0, -220.0)
			field_at_index_1.location = (0.0, 0.0)
			field_at_index_001.location = (0.0, -160.0)
			vector_math_14.location = (0.0, -320.0)
			compare_001_11.location = (160.0, -160.0)
			compare_18.location = (160.0, 0.0)
			boolean_math_20.location = (320.0, 0.0)
			reroute_009_3.location = (-1531.0, 160.0)
			reroute_012_2.location = (-1691.0, 640.0)
			mesh_line_1.location = (-690.0, 385.0)
			set_position_5.location = (-690.0, 345.0)
			domain_size_4.location = (-690.0, 425.0)
			delete_geometry_2.location = (320.0, 220.0)
			sample_index_009_2.location = (500.0, 1180.0)
			group_input_006_1.location = (280.0, 1260.0)
			sample_index_007_1.location = (500.0, 1240.0)
			group_output_85.location = (4000.0, 540.0)
			offset_point_in_curve.location = (1740.0, 1060.0)
			evaluate_at_index_9.location = (1900.0, 1060.0)
			position_002_3.location = (1740.0, 940.0)
			vector_math_002_6.location = (2060.0, 1060.0)
			vector_math_004_5.location = (1900.0, 900.0)
			endpoint_selection_2.location = (2067.57958984375, 912.9168701171875)
			switch_20.location = (1580.0, 1060.0)
			endpoint_selection_001_3.location = (1420.0, 1060.0)
			set_position_001_1.location = (2240.0, 1060.0)
			store_named_attribute_001_4.location = (1280.0, 620.0)
			store_named_attribute_002_4.location = (1440.0, 620.0)
			store_named_attribute_003_4.location = (1600.0, 620.0)
			store_named_attribute_004_4.location = (1760.0, 620.0)
			capture_attribute_5.location = (1940.0, 620.0)
			set_handle_type_1.location = (840.0, 260.0)
			set_spline_type_1.location = (670.0, 260.0)
			group_input_004_2.location = (1010.0, 120.0)
			mesh_to_curve_3.location = (510.0, 260.0)
			set_spline_resolution_2.location = (1010.0, 260.0)
			store_named_attribute_8.location = (1120.0, 620.0)
			store_named_attribute_007.location = (360.0, 40.0)
			store_named_attribute_008.location = (180.0, 40.0)
			store_named_attribute_009.location = (20.0, 40.0)
			store_named_attribute_010.location = (-140.0, 40.0)
			combine_xyz_2.location = (114.9571533203125, -1317.4541015625)
			math_24.location = (114.9571533203125, -1457.4541015625)
			cylinder.location = (-45.042877197265625, -1237.4541015625)
			value_1.location = (-59.143829345703125, -1534.919921875)
			group_input_005_2.location = (-246.84564208984375, -1389.357421875)
			store_named_attribute_006_2.location = (120.856201171875, -1094.919921875)
			position_001_6.location = (-1639.0, -1617.0)
			store_named_attribute_005_4.location = (540.0, 40.0)
			separate_geometry_9.location = (-2960.0, 0.0)
			group_input_83.location = (-3360.0, -60.0)
			group_004_6.location = (340.0, -200.0)
			reroute_006_2.location = (-260.0, -380.0)
			reroute_011_2.location = (240.0, -380.0)
			group_006_6.location = (-220.0, -180.0)
			transform.location = (314.9571533203125, -1217.4541015625)
			instance_on_points_3.location = (827.0, -1386.0)
			group_003_8.location = (-2100.0, 660.0)
			combine_xyz_001_2.location = (-1123.0, -1517.0)
			vector_math_003_5.location = (-1283.0, -1517.0)
			vector_math_001_6.location = (-1443.0, -1517.0)
			align_euler_to_vector_001_1.location = (-1123.0, -1297.0)
			align_euler_to_vector_2.location = (-1283.0, -1297.0)
			named_attribute_007_1.location = (-1678.014892578125, -1337.0)
			named_attribute_008_1.location = (-1679.2340087890625, -1477.0)
			capture_attribute_001_1.location = (2806.529052734375, 1155.515625)
			index_9.location = (2800.0, 960.0)
			named_attribute_009_1.location = (3040.0, 1000.0)
			sample_index_002_2.location = (3040.0, 1220.0)
			reroute_004_2.location = (2300.0, 400.0)
			set_shade_smooth_2.location = (2885.609130859375, 590.6487426757812)
			reroute_007_3.location = (2846.0, 400.0)
			curve_circle_3.location = (2546.0, 500.0)
			group_input_003_4.location = (2546.0, 460.0)
			set_material_4.location = (3380.0, 660.0)
			reroute_005_3.location = (3462.0, 231.0)
			reroute_008_2.location = (2862.0, 231.0)
			curve_to_mesh_4.location = (2722.0, 591.0)
			set_curve_radius_3.location = (2162.0, 631.0)
			group_input_002_5.location = (3322.0, 531.0)
			join_geometry_001_4.location = (3122.0, 551.0)
			reroute_013_2.location = (3074.18017578125, 548.1685791015625)
			store_named_attribute_011.location = (2940.4248046875, 856.4732666015625)
			switch_001_6.location = (3100.0, 860.0)
			group_input_001_11.location = (3100.0, 940.0)
			group_29.location = (-2840.0, 520.0)
			is_nucleic_1.location = (-3180.0, -120.0)
			group_005_8.location = (-2100.0, 480.0)
			reroute_22.location = (-2180.0, 540.0)
			mix_1.location = (-1827.638427734375, 608.8980102539062)
			
			#Set dimensions
			frame_002_4.width, frame_002_4.height = 504.5, 520.0000610351562
			frame_16.width, frame_16.height = 960.0, 734.0
			frame_001_10.width, frame_001_10.height = 200.0, 180.0
			frame_006_2.width, frame_006_2.height = 1020.0001220703125, 354.0
			frame_004_2.width, frame_004_2.height = 700.0, 262.0
			frame_005_2.width, frame_005_2.height = 1274.0, 590.0
			frame_007_2.width, frame_007_2.height = 756.0, 440.0
			frame_003_4.width, frame_003_4.height = 1364.0, 474.0
			sample_index_3.width, sample_index_3.height = 140.0, 100.0
			named_attribute_002_6.width, named_attribute_002_6.height = 140.0, 100.0
			sample_index_004.width, sample_index_004.height = 140.0, 100.0
			named_attribute_004_3.width, named_attribute_004_3.height = 140.0, 100.0
			sample_index_001_4.width, sample_index_001_4.height = 140.0, 100.0
			named_attribute_14.width, named_attribute_14.height = 140.0, 100.0
			reroute_003_7.width, reroute_003_7.height = 16.0, 100.0
			sample_index_003_2.width, sample_index_003_2.height = 140.0, 100.0
			named_attribute_003_3.width, named_attribute_003_3.height = 140.0, 100.0
			index_003_2.width, index_003_2.height = 140.0, 100.0
			named_attribute_005_2.width, named_attribute_005_2.height = 140.0, 100.0
			sample_index_005_1.width, sample_index_005_1.height = 140.0, 100.0
			reroute_001_15.width, reroute_001_15.height = 16.0, 100.0
			reroute_010_3.width, reroute_010_3.height = 16.0, 100.0
			sample_index_008_1.width, sample_index_008_1.height = 140.0, 100.0
			named_attribute_006_1.width, named_attribute_006_1.height = 140.0, 100.0
			index_004.width, index_004.height = 140.0, 100.0
			reroute_002_11.width, reroute_002_11.height = 16.0, 100.0
			edge_vertices_2.width, edge_vertices_2.height = 140.0, 100.0
			field_at_index_1.width, field_at_index_1.height = 140.0, 100.0
			field_at_index_001.width, field_at_index_001.height = 140.0, 100.0
			vector_math_14.width, vector_math_14.height = 140.0, 100.0
			compare_001_11.width, compare_001_11.height = 140.0, 100.0
			compare_18.width, compare_18.height = 140.0, 100.0
			boolean_math_20.width, boolean_math_20.height = 140.0, 100.0
			reroute_009_3.width, reroute_009_3.height = 16.0, 100.0
			reroute_012_2.width, reroute_012_2.height = 16.0, 100.0
			mesh_line_1.width, mesh_line_1.height = 140.0, 100.0
			set_position_5.width, set_position_5.height = 140.0, 100.0
			domain_size_4.width, domain_size_4.height = 140.0, 100.0
			delete_geometry_2.width, delete_geometry_2.height = 140.0, 100.0
			sample_index_009_2.width, sample_index_009_2.height = 140.0, 100.0
			group_input_006_1.width, group_input_006_1.height = 140.0, 100.0
			sample_index_007_1.width, sample_index_007_1.height = 140.0, 100.0
			group_output_85.width, group_output_85.height = 140.0, 100.0
			offset_point_in_curve.width, offset_point_in_curve.height = 140.0, 100.0
			evaluate_at_index_9.width, evaluate_at_index_9.height = 140.0, 100.0
			position_002_3.width, position_002_3.height = 140.0, 100.0
			vector_math_002_6.width, vector_math_002_6.height = 140.0, 100.0
			vector_math_004_5.width, vector_math_004_5.height = 140.0, 100.0
			endpoint_selection_2.width, endpoint_selection_2.height = 140.0, 100.0
			switch_20.width, switch_20.height = 140.0, 100.0
			endpoint_selection_001_3.width, endpoint_selection_001_3.height = 140.0, 100.0
			set_position_001_1.width, set_position_001_1.height = 140.0, 100.0
			store_named_attribute_001_4.width, store_named_attribute_001_4.height = 140.0, 100.0
			store_named_attribute_002_4.width, store_named_attribute_002_4.height = 140.0, 100.0
			store_named_attribute_003_4.width, store_named_attribute_003_4.height = 140.0, 100.0
			store_named_attribute_004_4.width, store_named_attribute_004_4.height = 140.0, 100.0
			capture_attribute_5.width, capture_attribute_5.height = 140.0, 100.0
			set_handle_type_1.width, set_handle_type_1.height = 140.0, 100.0
			set_spline_type_1.width, set_spline_type_1.height = 140.0, 100.0
			group_input_004_2.width, group_input_004_2.height = 140.0, 100.0
			mesh_to_curve_3.width, mesh_to_curve_3.height = 140.0, 100.0
			set_spline_resolution_2.width, set_spline_resolution_2.height = 140.0, 100.0
			store_named_attribute_8.width, store_named_attribute_8.height = 140.0, 100.0
			store_named_attribute_007.width, store_named_attribute_007.height = 140.0, 100.0
			store_named_attribute_008.width, store_named_attribute_008.height = 140.0, 100.0
			store_named_attribute_009.width, store_named_attribute_009.height = 140.0, 100.0
			store_named_attribute_010.width, store_named_attribute_010.height = 140.0, 100.0
			combine_xyz_2.width, combine_xyz_2.height = 140.0, 100.0
			math_24.width, math_24.height = 140.0, 100.0
			cylinder.width, cylinder.height = 140.0, 100.0
			value_1.width, value_1.height = 140.0, 100.0
			group_input_005_2.width, group_input_005_2.height = 140.0, 100.0
			store_named_attribute_006_2.width, store_named_attribute_006_2.height = 140.0, 100.0
			position_001_6.width, position_001_6.height = 140.0, 100.0
			store_named_attribute_005_4.width, store_named_attribute_005_4.height = 140.0, 100.0
			separate_geometry_9.width, separate_geometry_9.height = 140.0, 100.0
			group_input_83.width, group_input_83.height = 140.0, 100.0
			group_004_6.width, group_004_6.height = 176.54052734375, 100.0
			reroute_006_2.width, reroute_006_2.height = 16.0, 100.0
			reroute_011_2.width, reroute_011_2.height = 16.0, 100.0
			group_006_6.width, group_006_6.height = 223.4932861328125, 100.0
			transform.width, transform.height = 140.0, 100.0
			instance_on_points_3.width, instance_on_points_3.height = 140.0, 100.0
			group_003_8.width, group_003_8.height = 219.859375, 100.0
			combine_xyz_001_2.width, combine_xyz_001_2.height = 140.0, 100.0
			vector_math_003_5.width, vector_math_003_5.height = 140.0, 100.0
			vector_math_001_6.width, vector_math_001_6.height = 140.0, 100.0
			align_euler_to_vector_001_1.width, align_euler_to_vector_001_1.height = 140.0, 100.0
			align_euler_to_vector_2.width, align_euler_to_vector_2.height = 140.0, 100.0
			named_attribute_007_1.width, named_attribute_007_1.height = 179.014892578125, 100.0
			named_attribute_008_1.width, named_attribute_008_1.height = 180.2340087890625, 100.0
			capture_attribute_001_1.width, capture_attribute_001_1.height = 140.0, 100.0
			index_9.width, index_9.height = 140.0, 100.0
			named_attribute_009_1.width, named_attribute_009_1.height = 140.0, 100.0
			sample_index_002_2.width, sample_index_002_2.height = 140.0, 100.0
			reroute_004_2.width, reroute_004_2.height = 16.0, 100.0
			set_shade_smooth_2.width, set_shade_smooth_2.height = 140.0, 100.0
			reroute_007_3.width, reroute_007_3.height = 16.0, 100.0
			curve_circle_3.width, curve_circle_3.height = 140.0, 100.0
			group_input_003_4.width, group_input_003_4.height = 140.0, 100.0
			set_material_4.width, set_material_4.height = 140.0, 100.0
			reroute_005_3.width, reroute_005_3.height = 16.0, 100.0
			reroute_008_2.width, reroute_008_2.height = 16.0, 100.0
			curve_to_mesh_4.width, curve_to_mesh_4.height = 140.0, 100.0
			set_curve_radius_3.width, set_curve_radius_3.height = 140.0, 100.0
			group_input_002_5.width, group_input_002_5.height = 140.0, 100.0
			join_geometry_001_4.width, join_geometry_001_4.height = 140.0, 100.0
			reroute_013_2.width, reroute_013_2.height = 16.0, 100.0
			store_named_attribute_011.width, store_named_attribute_011.height = 140.0, 100.0
			switch_001_6.width, switch_001_6.height = 140.0, 100.0
			group_input_001_11.width, group_input_001_11.height = 140.0, 100.0
			group_29.width, group_29.height = 140.0, 100.0
			is_nucleic_1.width, is_nucleic_1.height = 180.0, 100.0
			group_005_8.width, group_005_8.height = 219.859375, 100.0
			reroute_22.width, reroute_22.height = 16.0, 100.0
			mix_1.width, mix_1.height = 140.0, 100.0
			
			#initialize _mn_utils_style_ribbon_nucleic links
			#mesh_line_1.Mesh -> set_position_5.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(mesh_line_1.outputs[0], set_position_5.inputs[0])
			#reroute_012_2.Output -> domain_size_4.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_012_2.outputs[0], domain_size_4.inputs[0])
			#domain_size_4.Point Count -> mesh_line_1.Count
			_mn_utils_style_ribbon_nucleic.links.new(domain_size_4.outputs[0], mesh_line_1.inputs[0])
			#set_position_5.Geometry -> delete_geometry_2.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(set_position_5.outputs[0], delete_geometry_2.inputs[0])
			#named_attribute_002_6.Attribute -> sample_index_3.Value
			_mn_utils_style_ribbon_nucleic.links.new(named_attribute_002_6.outputs[0], sample_index_3.inputs[1])
			#edge_vertices_2.Vertex Index 1 -> field_at_index_1.Index
			_mn_utils_style_ribbon_nucleic.links.new(edge_vertices_2.outputs[0], field_at_index_1.inputs[0])
			#reroute_002_11.Output -> field_at_index_1.Value
			_mn_utils_style_ribbon_nucleic.links.new(reroute_002_11.outputs[0], field_at_index_1.inputs[1])
			#reroute_002_11.Output -> field_at_index_001.Value
			_mn_utils_style_ribbon_nucleic.links.new(reroute_002_11.outputs[0], field_at_index_001.inputs[1])
			#edge_vertices_2.Vertex Index 2 -> field_at_index_001.Index
			_mn_utils_style_ribbon_nucleic.links.new(edge_vertices_2.outputs[1], field_at_index_001.inputs[0])
			#field_at_index_1.Value -> compare_18.A
			_mn_utils_style_ribbon_nucleic.links.new(field_at_index_1.outputs[0], compare_18.inputs[2])
			#field_at_index_001.Value -> compare_18.B
			_mn_utils_style_ribbon_nucleic.links.new(field_at_index_001.outputs[0], compare_18.inputs[3])
			#edge_vertices_2.Position 1 -> vector_math_14.Vector
			_mn_utils_style_ribbon_nucleic.links.new(edge_vertices_2.outputs[2], vector_math_14.inputs[0])
			#edge_vertices_2.Position 2 -> vector_math_14.Vector
			_mn_utils_style_ribbon_nucleic.links.new(edge_vertices_2.outputs[3], vector_math_14.inputs[1])
			#compare_18.Result -> boolean_math_20.Boolean
			_mn_utils_style_ribbon_nucleic.links.new(compare_18.outputs[0], boolean_math_20.inputs[0])
			#boolean_math_20.Boolean -> delete_geometry_2.Selection
			_mn_utils_style_ribbon_nucleic.links.new(boolean_math_20.outputs[0], delete_geometry_2.inputs[1])
			#vector_math_14.Value -> compare_001_11.A
			_mn_utils_style_ribbon_nucleic.links.new(vector_math_14.outputs[1], compare_001_11.inputs[0])
			#compare_001_11.Result -> boolean_math_20.Boolean
			_mn_utils_style_ribbon_nucleic.links.new(compare_001_11.outputs[0], boolean_math_20.inputs[1])
			#store_named_attribute_007.Geometry -> mesh_to_curve_3.Mesh
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_007.outputs[0], mesh_to_curve_3.inputs[0])
			#mesh_to_curve_3.Curve -> set_spline_type_1.Curve
			_mn_utils_style_ribbon_nucleic.links.new(mesh_to_curve_3.outputs[0], set_spline_type_1.inputs[0])
			#set_handle_type_1.Curve -> set_spline_resolution_2.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(set_handle_type_1.outputs[0], set_spline_resolution_2.inputs[0])
			#curve_circle_3.Curve -> curve_to_mesh_4.Profile Curve
			_mn_utils_style_ribbon_nucleic.links.new(curve_circle_3.outputs[0], curve_to_mesh_4.inputs[1])
			#reroute_001_15.Output -> sample_index_001_4.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_001_15.outputs[0], sample_index_001_4.inputs[0])
			#named_attribute_14.Attribute -> sample_index_001_4.Value
			_mn_utils_style_ribbon_nucleic.links.new(named_attribute_14.outputs[0], sample_index_001_4.inputs[1])
			#join_geometry_001_4.Geometry -> set_material_4.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(join_geometry_001_4.outputs[0], set_material_4.inputs[0])
			#group_input_002_5.Material -> set_material_4.Material
			_mn_utils_style_ribbon_nucleic.links.new(group_input_002_5.outputs[2], set_material_4.inputs[2])
			#set_spline_type_1.Curve -> set_handle_type_1.Curve
			_mn_utils_style_ribbon_nucleic.links.new(set_spline_type_1.outputs[0], set_handle_type_1.inputs[0])
			#reroute_003_7.Output -> sample_index_001_4.Index
			_mn_utils_style_ribbon_nucleic.links.new(reroute_003_7.outputs[0], sample_index_001_4.inputs[2])
			#set_spline_resolution_2.Geometry -> store_named_attribute_8.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(set_spline_resolution_2.outputs[0], store_named_attribute_8.inputs[0])
			#sample_index_001_4.Value -> store_named_attribute_8.Value
			_mn_utils_style_ribbon_nucleic.links.new(sample_index_001_4.outputs[0], store_named_attribute_8.inputs[3])
			#store_named_attribute_8.Geometry -> store_named_attribute_001_4.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_8.outputs[0], store_named_attribute_001_4.inputs[0])
			#store_named_attribute_001_4.Geometry -> store_named_attribute_002_4.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_001_4.outputs[0], store_named_attribute_002_4.inputs[0])
			#store_named_attribute_002_4.Geometry -> store_named_attribute_003_4.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_002_4.outputs[0], store_named_attribute_003_4.inputs[0])
			#sample_index_3.Value -> store_named_attribute_001_4.Value
			_mn_utils_style_ribbon_nucleic.links.new(sample_index_3.outputs[0], store_named_attribute_001_4.inputs[3])
			#reroute_001_15.Output -> sample_index_003_2.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_001_15.outputs[0], sample_index_003_2.inputs[0])
			#named_attribute_003_3.Attribute -> sample_index_003_2.Value
			_mn_utils_style_ribbon_nucleic.links.new(named_attribute_003_3.outputs[0], sample_index_003_2.inputs[1])
			#reroute_003_7.Output -> sample_index_003_2.Index
			_mn_utils_style_ribbon_nucleic.links.new(reroute_003_7.outputs[0], sample_index_003_2.inputs[2])
			#sample_index_003_2.Value -> store_named_attribute_003_4.Value
			_mn_utils_style_ribbon_nucleic.links.new(sample_index_003_2.outputs[0], store_named_attribute_003_4.inputs[3])
			#reroute_001_15.Output -> sample_index_004.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_001_15.outputs[0], sample_index_004.inputs[0])
			#named_attribute_004_3.Attribute -> sample_index_004.Value
			_mn_utils_style_ribbon_nucleic.links.new(named_attribute_004_3.outputs[0], sample_index_004.inputs[1])
			#reroute_003_7.Output -> sample_index_004.Index
			_mn_utils_style_ribbon_nucleic.links.new(reroute_003_7.outputs[0], sample_index_004.inputs[2])
			#sample_index_004.Value -> store_named_attribute_002_4.Value
			_mn_utils_style_ribbon_nucleic.links.new(sample_index_004.outputs[0], store_named_attribute_002_4.inputs[3])
			#reroute_010_3.Output -> reroute_001_15.Input
			_mn_utils_style_ribbon_nucleic.links.new(reroute_010_3.outputs[0], reroute_001_15.inputs[0])
			#index_003_2.Index -> reroute_003_7.Input
			_mn_utils_style_ribbon_nucleic.links.new(index_003_2.outputs[0], reroute_003_7.inputs[0])
			#reroute_003_7.Output -> sample_index_3.Index
			_mn_utils_style_ribbon_nucleic.links.new(reroute_003_7.outputs[0], sample_index_3.inputs[2])
			#store_named_attribute_003_4.Geometry -> store_named_attribute_004_4.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_003_4.outputs[0], store_named_attribute_004_4.inputs[0])
			#reroute_001_15.Output -> sample_index_005_1.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_001_15.outputs[0], sample_index_005_1.inputs[0])
			#reroute_003_7.Output -> sample_index_005_1.Index
			_mn_utils_style_ribbon_nucleic.links.new(reroute_003_7.outputs[0], sample_index_005_1.inputs[2])
			#named_attribute_005_2.Attribute -> sample_index_005_1.Value
			_mn_utils_style_ribbon_nucleic.links.new(named_attribute_005_2.outputs[0], sample_index_005_1.inputs[1])
			#sample_index_005_1.Value -> store_named_attribute_004_4.Value
			_mn_utils_style_ribbon_nucleic.links.new(sample_index_005_1.outputs[0], store_named_attribute_004_4.inputs[3])
			#store_named_attribute_004_4.Geometry -> capture_attribute_5.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_004_4.outputs[0], capture_attribute_5.inputs[0])
			#capture_attribute_5.Geometry -> set_curve_radius_3.Curve
			_mn_utils_style_ribbon_nucleic.links.new(capture_attribute_5.outputs[0], set_curve_radius_3.inputs[0])
			#reroute_007_3.Output -> set_shade_smooth_2.Shade Smooth
			_mn_utils_style_ribbon_nucleic.links.new(reroute_007_3.outputs[0], set_shade_smooth_2.inputs[2])
			#capture_attribute_5.Value -> reroute_004_2.Input
			_mn_utils_style_ribbon_nucleic.links.new(capture_attribute_5.outputs[1], reroute_004_2.inputs[0])
			#reroute_004_2.Output -> reroute_007_3.Input
			_mn_utils_style_ribbon_nucleic.links.new(reroute_004_2.outputs[0], reroute_007_3.inputs[0])
			#reroute_001_15.Output -> sample_index_3.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_001_15.outputs[0], sample_index_3.inputs[0])
			#named_attribute_006_1.Attribute -> sample_index_008_1.Value
			_mn_utils_style_ribbon_nucleic.links.new(named_attribute_006_1.outputs[0], sample_index_008_1.inputs[1])
			#reroute_009_3.Output -> sample_index_008_1.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_009_3.outputs[0], sample_index_008_1.inputs[0])
			#index_004.Index -> sample_index_008_1.Index
			_mn_utils_style_ribbon_nucleic.links.new(index_004.outputs[0], sample_index_008_1.inputs[2])
			#sample_index_008_1.Value -> reroute_002_11.Input
			_mn_utils_style_ribbon_nucleic.links.new(sample_index_008_1.outputs[0], reroute_002_11.inputs[0])
			#reroute_012_2.Output -> reroute_009_3.Input
			_mn_utils_style_ribbon_nucleic.links.new(reroute_012_2.outputs[0], reroute_009_3.inputs[0])
			#reroute_012_2.Output -> reroute_010_3.Input
			_mn_utils_style_ribbon_nucleic.links.new(reroute_012_2.outputs[0], reroute_010_3.inputs[0])
			#curve_to_mesh_4.Mesh -> set_shade_smooth_2.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(curve_to_mesh_4.outputs[0], set_shade_smooth_2.inputs[0])
			#group_003_8.Atoms -> reroute_012_2.Input
			_mn_utils_style_ribbon_nucleic.links.new(group_003_8.outputs[0], reroute_012_2.inputs[0])
			#store_named_attribute_006_2.Geometry -> transform.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_006_2.outputs[0], transform.inputs[0])
			#combine_xyz_2.Vector -> transform.Translation
			_mn_utils_style_ribbon_nucleic.links.new(combine_xyz_2.outputs[0], transform.inputs[1])
			#value_1.Value -> math_24.Value
			_mn_utils_style_ribbon_nucleic.links.new(value_1.outputs[0], math_24.inputs[0])
			#value_1.Value -> cylinder.Depth
			_mn_utils_style_ribbon_nucleic.links.new(value_1.outputs[0], cylinder.inputs[4])
			#math_24.Value -> combine_xyz_2.Z
			_mn_utils_style_ribbon_nucleic.links.new(math_24.outputs[0], combine_xyz_2.inputs[2])
			#align_euler_to_vector_001_1.Rotation -> instance_on_points_3.Rotation
			_mn_utils_style_ribbon_nucleic.links.new(align_euler_to_vector_001_1.outputs[0], instance_on_points_3.inputs[5])
			#combine_xyz_001_2.Vector -> instance_on_points_3.Scale
			_mn_utils_style_ribbon_nucleic.links.new(combine_xyz_001_2.outputs[0], instance_on_points_3.inputs[6])
			#set_material_4.Geometry -> group_output_85.Ribbon + Bases
			_mn_utils_style_ribbon_nucleic.links.new(set_material_4.outputs[0], group_output_85.inputs[0])
			#store_named_attribute_005_4.Geometry -> instance_on_points_3.Points
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_005_4.outputs[0], instance_on_points_3.inputs[0])
			#reroute_013_2.Output -> join_geometry_001_4.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_013_2.outputs[0], join_geometry_001_4.inputs[0])
			#group_input_005_2.Base Radius -> cylinder.Radius
			_mn_utils_style_ribbon_nucleic.links.new(group_input_005_2.outputs[8], cylinder.inputs[3])
			#group_input_005_2.Base Resolution -> cylinder.Vertices
			_mn_utils_style_ribbon_nucleic.links.new(group_input_005_2.outputs[9], cylinder.inputs[0])
			#reroute_005_3.Output -> group_output_85.Ribbon Curve
			_mn_utils_style_ribbon_nucleic.links.new(reroute_005_3.outputs[0], group_output_85.inputs[1])
			#transform.Geometry -> instance_on_points_3.Instance
			_mn_utils_style_ribbon_nucleic.links.new(transform.outputs[0], instance_on_points_3.inputs[2])
			#cylinder.Mesh -> store_named_attribute_006_2.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(cylinder.outputs[0], store_named_attribute_006_2.inputs[0])
			#cylinder.UV Map -> store_named_attribute_006_2.Value
			_mn_utils_style_ribbon_nucleic.links.new(cylinder.outputs[4], store_named_attribute_006_2.inputs[3])
			#group_input_83.Atoms -> separate_geometry_9.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(group_input_83.outputs[0], separate_geometry_9.inputs[0])
			#reroute_22.Output -> group_003_8.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_22.outputs[0], group_003_8.inputs[0])
			#group_004_6.Value -> store_named_attribute_005_4.Value
			_mn_utils_style_ribbon_nucleic.links.new(group_004_6.outputs[2], store_named_attribute_005_4.inputs[3])
			#group_input_003_4.Backbone Resolution -> curve_circle_3.Resolution
			_mn_utils_style_ribbon_nucleic.links.new(group_input_003_4.outputs[5], curve_circle_3.inputs[0])
			#position_001_6.Position -> vector_math_001_6.Vector
			_mn_utils_style_ribbon_nucleic.links.new(position_001_6.outputs[0], vector_math_001_6.inputs[1])
			#set_curve_radius_3.Curve -> set_position_001_1.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(set_curve_radius_3.outputs[0], set_position_001_1.inputs[0])
			#position_002_3.Position -> evaluate_at_index_9.Value
			_mn_utils_style_ribbon_nucleic.links.new(position_002_3.outputs[0], evaluate_at_index_9.inputs[1])
			#offset_point_in_curve.Point Index -> evaluate_at_index_9.Index
			_mn_utils_style_ribbon_nucleic.links.new(offset_point_in_curve.outputs[1], evaluate_at_index_9.inputs[0])
			#evaluate_at_index_9.Value -> vector_math_002_6.Vector
			_mn_utils_style_ribbon_nucleic.links.new(evaluate_at_index_9.outputs[0], vector_math_002_6.inputs[0])
			#position_002_3.Position -> vector_math_002_6.Vector
			_mn_utils_style_ribbon_nucleic.links.new(position_002_3.outputs[0], vector_math_002_6.inputs[1])
			#vector_math_002_6.Vector -> vector_math_004_5.Vector
			_mn_utils_style_ribbon_nucleic.links.new(vector_math_002_6.outputs[0], vector_math_004_5.inputs[0])
			#vector_math_004_5.Vector -> set_position_001_1.Offset
			_mn_utils_style_ribbon_nucleic.links.new(vector_math_004_5.outputs[0], set_position_001_1.inputs[3])
			#endpoint_selection_2.Selection -> set_position_001_1.Selection
			_mn_utils_style_ribbon_nucleic.links.new(endpoint_selection_2.outputs[0], set_position_001_1.inputs[1])
			#endpoint_selection_001_3.Selection -> switch_20.Switch
			_mn_utils_style_ribbon_nucleic.links.new(endpoint_selection_001_3.outputs[0], switch_20.inputs[0])
			#switch_20.Output -> offset_point_in_curve.Offset
			_mn_utils_style_ribbon_nucleic.links.new(switch_20.outputs[0], offset_point_in_curve.inputs[1])
			#store_named_attribute_007.Geometry -> store_named_attribute_005_4.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_007.outputs[0], store_named_attribute_005_4.inputs[0])
			#group_input_004_2.Backbone Subdivisions -> set_spline_resolution_2.Resolution
			_mn_utils_style_ribbon_nucleic.links.new(group_input_004_2.outputs[4], set_spline_resolution_2.inputs[2])
			#reroute_001_15.Output -> sample_index_009_2.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_001_15.outputs[0], sample_index_009_2.inputs[0])
			#reroute_003_7.Output -> sample_index_009_2.Index
			_mn_utils_style_ribbon_nucleic.links.new(reroute_003_7.outputs[0], sample_index_009_2.inputs[2])
			#group_input_006_1.Backbone Shade Smooth -> sample_index_009_2.Value
			_mn_utils_style_ribbon_nucleic.links.new(group_input_006_1.outputs[7], sample_index_009_2.inputs[1])
			#sample_index_009_2.Value -> capture_attribute_5.Value
			_mn_utils_style_ribbon_nucleic.links.new(sample_index_009_2.outputs[0], capture_attribute_5.inputs[1])
			#group_input_006_1.Backbone Radius -> sample_index_007_1.Value
			_mn_utils_style_ribbon_nucleic.links.new(group_input_006_1.outputs[6], sample_index_007_1.inputs[1])
			#reroute_003_7.Output -> sample_index_007_1.Index
			_mn_utils_style_ribbon_nucleic.links.new(reroute_003_7.outputs[0], sample_index_007_1.inputs[2])
			#reroute_001_15.Output -> sample_index_007_1.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_001_15.outputs[0], sample_index_007_1.inputs[0])
			#sample_index_007_1.Value -> set_curve_radius_3.Radius
			_mn_utils_style_ribbon_nucleic.links.new(sample_index_007_1.outputs[0], set_curve_radius_3.inputs[2])
			#reroute_008_2.Output -> reroute_005_3.Input
			_mn_utils_style_ribbon_nucleic.links.new(reroute_008_2.outputs[0], reroute_005_3.inputs[0])
			#set_curve_radius_3.Curve -> reroute_008_2.Input
			_mn_utils_style_ribbon_nucleic.links.new(set_curve_radius_3.outputs[0], reroute_008_2.inputs[0])
			#store_named_attribute_008.Geometry -> store_named_attribute_007.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_008.outputs[0], store_named_attribute_007.inputs[0])
			#reroute_006_2.Output -> group_006_6.Input
			_mn_utils_style_ribbon_nucleic.links.new(reroute_006_2.outputs[0], group_006_6.inputs[0])
			#store_named_attribute_009.Geometry -> store_named_attribute_008.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_009.outputs[0], store_named_attribute_008.inputs[0])
			#group_006_6.Align Vertical -> store_named_attribute_008.Value
			_mn_utils_style_ribbon_nucleic.links.new(group_006_6.outputs[2], store_named_attribute_008.inputs[3])
			#group_006_6.Align Horizontal -> store_named_attribute_007.Value
			_mn_utils_style_ribbon_nucleic.links.new(group_006_6.outputs[3], store_named_attribute_007.inputs[3])
			#vector_math_001_6.Vector -> vector_math_003_5.Vector
			_mn_utils_style_ribbon_nucleic.links.new(vector_math_001_6.outputs[0], vector_math_003_5.inputs[0])
			#vector_math_003_5.Value -> combine_xyz_001_2.Z
			_mn_utils_style_ribbon_nucleic.links.new(vector_math_003_5.outputs[1], combine_xyz_001_2.inputs[2])
			#store_named_attribute_010.Geometry -> store_named_attribute_009.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_010.outputs[0], store_named_attribute_009.inputs[0])
			#group_006_6.Base Interface -> store_named_attribute_009.Value
			_mn_utils_style_ribbon_nucleic.links.new(group_006_6.outputs[0], store_named_attribute_009.inputs[3])
			#delete_geometry_2.Geometry -> store_named_attribute_010.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(delete_geometry_2.outputs[0], store_named_attribute_010.inputs[0])
			#group_006_6.Base Pivot -> store_named_attribute_010.Value
			_mn_utils_style_ribbon_nucleic.links.new(group_006_6.outputs[1], store_named_attribute_010.inputs[3])
			#named_attribute_008_1.Attribute -> vector_math_001_6.Vector
			_mn_utils_style_ribbon_nucleic.links.new(named_attribute_008_1.outputs[0], vector_math_001_6.inputs[0])
			#separate_geometry_9.Selection -> reroute_006_2.Input
			_mn_utils_style_ribbon_nucleic.links.new(separate_geometry_9.outputs[0], reroute_006_2.inputs[0])
			#reroute_011_2.Output -> group_004_6.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_011_2.outputs[0], group_004_6.inputs[0])
			#reroute_006_2.Output -> reroute_011_2.Input
			_mn_utils_style_ribbon_nucleic.links.new(reroute_006_2.outputs[0], reroute_011_2.inputs[0])
			#align_euler_to_vector_2.Rotation -> align_euler_to_vector_001_1.Rotation
			_mn_utils_style_ribbon_nucleic.links.new(align_euler_to_vector_2.outputs[0], align_euler_to_vector_001_1.inputs[0])
			#vector_math_001_6.Vector -> align_euler_to_vector_2.Vector
			_mn_utils_style_ribbon_nucleic.links.new(vector_math_001_6.outputs[0], align_euler_to_vector_2.inputs[2])
			#named_attribute_007_1.Attribute -> align_euler_to_vector_001_1.Vector
			_mn_utils_style_ribbon_nucleic.links.new(named_attribute_007_1.outputs[0], align_euler_to_vector_001_1.inputs[2])
			#set_position_001_1.Geometry -> capture_attribute_001_1.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(set_position_001_1.outputs[0], capture_attribute_001_1.inputs[0])
			#index_9.Index -> capture_attribute_001_1.Value
			_mn_utils_style_ribbon_nucleic.links.new(index_9.outputs[0], capture_attribute_001_1.inputs[1])
			#capture_attribute_001_1.Geometry -> curve_to_mesh_4.Curve
			_mn_utils_style_ribbon_nucleic.links.new(capture_attribute_001_1.outputs[0], curve_to_mesh_4.inputs[0])
			#set_shade_smooth_2.Geometry -> store_named_attribute_011.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(set_shade_smooth_2.outputs[0], store_named_attribute_011.inputs[0])
			#capture_attribute_001_1.Value -> sample_index_002_2.Index
			_mn_utils_style_ribbon_nucleic.links.new(capture_attribute_001_1.outputs[1], sample_index_002_2.inputs[2])
			#capture_attribute_001_1.Geometry -> sample_index_002_2.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(capture_attribute_001_1.outputs[0], sample_index_002_2.inputs[0])
			#named_attribute_009_1.Attribute -> sample_index_002_2.Value
			_mn_utils_style_ribbon_nucleic.links.new(named_attribute_009_1.outputs[0], sample_index_002_2.inputs[1])
			#sample_index_002_2.Value -> store_named_attribute_011.Value
			_mn_utils_style_ribbon_nucleic.links.new(sample_index_002_2.outputs[0], store_named_attribute_011.inputs[3])
			#store_named_attribute_011.Geometry -> switch_001_6.False
			_mn_utils_style_ribbon_nucleic.links.new(store_named_attribute_011.outputs[0], switch_001_6.inputs[1])
			#set_shade_smooth_2.Geometry -> switch_001_6.True
			_mn_utils_style_ribbon_nucleic.links.new(set_shade_smooth_2.outputs[0], switch_001_6.inputs[2])
			#switch_001_6.Output -> reroute_013_2.Input
			_mn_utils_style_ribbon_nucleic.links.new(switch_001_6.outputs[0], reroute_013_2.inputs[0])
			#group_input_001_11.Intepolate Color -> switch_001_6.Switch
			_mn_utils_style_ribbon_nucleic.links.new(group_input_001_11.outputs[3], switch_001_6.inputs[0])
			#group_input_83.Selection -> is_nucleic_1.And
			_mn_utils_style_ribbon_nucleic.links.new(group_input_83.outputs[1], is_nucleic_1.inputs[0])
			#is_nucleic_1.Selection -> separate_geometry_9.Selection
			_mn_utils_style_ribbon_nucleic.links.new(is_nucleic_1.outputs[0], separate_geometry_9.inputs[1])
			#reroute_22.Output -> group_005_8.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(reroute_22.outputs[0], group_005_8.inputs[0])
			#separate_geometry_9.Selection -> reroute_22.Input
			_mn_utils_style_ribbon_nucleic.links.new(separate_geometry_9.outputs[0], reroute_22.inputs[0])
			#group_003_8.Value -> mix_1.A
			_mn_utils_style_ribbon_nucleic.links.new(group_003_8.outputs[1], mix_1.inputs[4])
			#group_005_8.Value -> mix_1.B
			_mn_utils_style_ribbon_nucleic.links.new(group_005_8.outputs[1], mix_1.inputs[5])
			#mix_1.Result -> set_position_5.Position
			_mn_utils_style_ribbon_nucleic.links.new(mix_1.outputs[1], set_position_5.inputs[2])
			#instance_on_points_3.Instances -> join_geometry_001_4.Geometry
			_mn_utils_style_ribbon_nucleic.links.new(instance_on_points_3.outputs[0], join_geometry_001_4.inputs[0])
			return _mn_utils_style_ribbon_nucleic

		_mn_utils_style_ribbon_nucleic = _mn_utils_style_ribbon_nucleic_node_group()

		#initialize style_cartoon node group
		def style_cartoon_node_group():
			style_cartoon = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Style Cartoon")

			style_cartoon.color_tag = 'GEOMETRY'
			style_cartoon.description = ""

			style_cartoon.is_modifier = True
			
			#style_cartoon interface
			#Socket Geometry
			geometry_socket_15 = style_cartoon.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_15.attribute_domain = 'POINT'
			geometry_socket_15.description = "The resulting cartoon geometry, calculated from the given atoms, selection and parameters"
			
			#Socket Atoms
			atoms_socket_17 = style_cartoon.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_17.attribute_domain = 'POINT'
			atoms_socket_17.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket_22 = style_cartoon.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_22.attribute_domain = 'POINT'
			selection_socket_22.hide_value = True
			selection_socket_22.description = "Selection of atoms to apply this style to"
			
			#Socket Quality
			quality_socket_2 = style_cartoon.interface.new_socket(name = "Quality", in_out='INPUT', socket_type = 'NodeSocketInt')
			quality_socket_2.subtype = 'NONE'
			quality_socket_2.default_value = 2
			quality_socket_2.min_value = 0
			quality_socket_2.max_value = 6
			quality_socket_2.attribute_domain = 'POINT'
			quality_socket_2.description = "Number of subdivisions,  ‘quality’ of the cartoon."
			
			#Panel Cartoon
			cartoon_panel = style_cartoon.interface.new_panel("Cartoon", default_closed=True)
			#Socket DSSP
			dssp_socket = style_cartoon.interface.new_socket(name = "DSSP", in_out='INPUT', socket_type = 'NodeSocketBool', parent = cartoon_panel)
			dssp_socket.attribute_domain = 'POINT'
			dssp_socket.description = "Use the DSSP algorithm to compute the `sec_struct` attribute"
			
			#Socket Cylinders
			cylinders_socket = style_cartoon.interface.new_socket(name = "Cylinders", in_out='INPUT', socket_type = 'NodeSocketBool', parent = cartoon_panel)
			cylinders_socket.attribute_domain = 'POINT'
			cylinders_socket.description = "Use cylinders for helices instead of ribbons"
			
			#Socket Arrows
			arrows_socket = style_cartoon.interface.new_socket(name = "Arrows", in_out='INPUT', socket_type = 'NodeSocketBool', parent = cartoon_panel)
			arrows_socket.attribute_domain = 'POINT'
			arrows_socket.description = "User arrows for sheets"
			
			#Socket Rounded
			rounded_socket = style_cartoon.interface.new_socket(name = "Rounded", in_out='INPUT', socket_type = 'NodeSocketBool', parent = cartoon_panel)
			rounded_socket.attribute_domain = 'POINT'
			rounded_socket.description = "Create rounded sheets and helices"
			
			#Socket Thickness
			thickness_socket = style_cartoon.interface.new_socket(name = "Thickness", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = cartoon_panel)
			thickness_socket.subtype = 'NONE'
			thickness_socket.default_value = 0.6000000238418579
			thickness_socket.min_value = 0.0
			thickness_socket.max_value = 3.4028234663852886e+38
			thickness_socket.attribute_domain = 'POINT'
			thickness_socket.description = "Thickness for the sheets and helices"
			
			#Socket Width
			width_socket = style_cartoon.interface.new_socket(name = "Width", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = cartoon_panel)
			width_socket.subtype = 'NONE'
			width_socket.default_value = 2.200000047683716
			width_socket.min_value = 0.0
			width_socket.max_value = 3.4028234663852886e+38
			width_socket.attribute_domain = 'POINT'
			width_socket.description = "Width for the sheets and helices"
			
			#Socket Loop Radius
			loop_radius_socket_1 = style_cartoon.interface.new_socket(name = "Loop Radius", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = cartoon_panel)
			loop_radius_socket_1.subtype = 'NONE'
			loop_radius_socket_1.default_value = 0.4000000059604645
			loop_radius_socket_1.min_value = 0.0
			loop_radius_socket_1.max_value = 3.0
			loop_radius_socket_1.attribute_domain = 'POINT'
			loop_radius_socket_1.description = "Radius of the loops for unstructure regions"
			
			#Socket Smoothing
			smoothing_socket = style_cartoon.interface.new_socket(name = "Smoothing", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = cartoon_panel)
			smoothing_socket.subtype = 'FACTOR'
			smoothing_socket.default_value = 0.5
			smoothing_socket.min_value = 0.0
			smoothing_socket.max_value = 1.0
			smoothing_socket.attribute_domain = 'POINT'
			smoothing_socket.description = "Smoothing to apply to sheets"
			
			
			#Panel Material
			material_panel_4 = style_cartoon.interface.new_panel("Material", default_closed=True)
			#Socket Color Blur
			color_blur_socket_2 = style_cartoon.interface.new_socket(name = "Color Blur", in_out='INPUT', socket_type = 'NodeSocketBool', parent = material_panel_4)
			color_blur_socket_2.attribute_domain = 'POINT'
			color_blur_socket_2.description = "Smoothly interpolate between the different color values, or have each bit of geometry be cleanly one color or another"
			
			#Socket Shade Smooth
			shade_smooth_socket_6 = style_cartoon.interface.new_socket(name = "Shade Smooth", in_out='INPUT', socket_type = 'NodeSocketBool', parent = material_panel_4)
			shade_smooth_socket_6.attribute_domain = 'POINT'
			shade_smooth_socket_6.description = "Apply smooth shading to the created geometry"
			
			#Socket Material
			material_socket_8 = style_cartoon.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial', parent = material_panel_4)
			material_socket_8.attribute_domain = 'POINT'
			material_socket_8.description = "Material to apply to the resulting geometry"
			
			
			
			#initialize style_cartoon nodes
			#node Group Output
			group_output_86 = style_cartoon.nodes.new("NodeGroupOutput")
			group_output_86.name = "Group Output"
			group_output_86.is_active_output = True
			
			#node Group Input
			group_input_84 = style_cartoon.nodes.new("NodeGroupInput")
			group_input_84.name = "Group Input"
			group_input_84.outputs[3].hide = True
			
			#node Group.067
			group_067 = style_cartoon.nodes.new("GeometryNodeGroup")
			group_067.name = "Group.067"
			group_067.node_tree = _mn_utils_style_cartoon
			#Input_122
			group_067.inputs[7].default_value = False
			#Input_80
			group_067.inputs[8].default_value = 1.309999942779541
			#Input_81
			group_067.inputs[9].default_value = 1.0299999713897705
			#Input_87
			group_067.inputs[12].default_value = 0.0
			#Input_69
			group_067.inputs[18].default_value = True
			#Input_4
			group_067.inputs[22].default_value = 0.0
			#Input_86
			group_067.inputs[26].default_value = True
			
			#node Math
			math_25 = style_cartoon.nodes.new("ShaderNodeMath")
			math_25.name = "Math"
			math_25.operation = 'MULTIPLY'
			math_25.use_clamp = False
			#Value_001
			math_25.inputs[1].default_value = 3.0
			
			#node Math.002
			math_002_8 = style_cartoon.nodes.new("ShaderNodeMath")
			math_002_8.name = "Math.002"
			math_002_8.operation = 'MULTIPLY'
			math_002_8.use_clamp = False
			#Value_001
			math_002_8.inputs[1].default_value = 3.0
			
			#node Switch
			switch_21 = style_cartoon.nodes.new("GeometryNodeSwitch")
			switch_21.name = "Switch"
			switch_21.input_type = 'INT'
			#False
			switch_21.inputs[1].default_value = 4
			
			#node Math.001
			math_001_14 = style_cartoon.nodes.new("ShaderNodeMath")
			math_001_14.name = "Math.001"
			math_001_14.operation = 'MULTIPLY'
			math_001_14.use_clamp = False
			#Value_001
			math_001_14.inputs[1].default_value = 5.0
			
			#node Reroute
			reroute_23 = style_cartoon.nodes.new("NodeReroute")
			reroute_23.name = "Reroute"
			#node Store Named Attribute
			store_named_attribute_9 = style_cartoon.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_9.name = "Store Named Attribute"
			store_named_attribute_9.data_type = 'INT'
			store_named_attribute_9.domain = 'POINT'
			
			#node Named Attribute
			named_attribute_15 = style_cartoon.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_15.name = "Named Attribute"
			named_attribute_15.data_type = 'INT'
			
			#node String
			string = style_cartoon.nodes.new("FunctionNodeInputString")
			string.name = "String"
			string.string = "sec_struct"
			
			#node Boolean Math
			boolean_math_21 = style_cartoon.nodes.new("FunctionNodeBooleanMath")
			boolean_math_21.name = "Boolean Math"
			boolean_math_21.operation = 'NOT'
			
			#node Select Peptide
			select_peptide = style_cartoon.nodes.new("GeometryNodeGroup")
			select_peptide.label = "Select Peptide"
			select_peptide.name = "Select Peptide"
			select_peptide.node_tree = is_peptide
			#Socket_1
			select_peptide.inputs[0].default_value = True
			#Socket_3
			select_peptide.inputs[1].default_value = False
			
			#node Switch.002
			switch_002_4 = style_cartoon.nodes.new("GeometryNodeSwitch")
			switch_002_4.name = "Switch.002"
			switch_002_4.input_type = 'INT'
			#False
			switch_002_4.inputs[1].default_value = 0
			#True
			switch_002_4.inputs[2].default_value = 3
			
			#node Group
			group_30 = style_cartoon.nodes.new("GeometryNodeGroup")
			group_30.name = "Group"
			group_30.node_tree = topology_dssp
			#Socket_6
			group_30.inputs[1].default_value = True
			
			#node Switch.001
			switch_001_7 = style_cartoon.nodes.new("GeometryNodeSwitch")
			switch_001_7.name = "Switch.001"
			switch_001_7.input_type = 'GEOMETRY'
			
			#node Group Input.001
			group_input_001_12 = style_cartoon.nodes.new("NodeGroupInput")
			group_input_001_12.name = "Group Input.001"
			group_input_001_12.outputs[0].hide = True
			group_input_001_12.outputs[1].hide = True
			group_input_001_12.outputs[2].hide = True
			group_input_001_12.outputs[4].hide = True
			group_input_001_12.outputs[5].hide = True
			group_input_001_12.outputs[6].hide = True
			group_input_001_12.outputs[7].hide = True
			group_input_001_12.outputs[8].hide = True
			group_input_001_12.outputs[9].hide = True
			group_input_001_12.outputs[10].hide = True
			group_input_001_12.outputs[11].hide = True
			group_input_001_12.outputs[12].hide = True
			group_input_001_12.outputs[13].hide = True
			group_input_001_12.outputs[14].hide = True
			
			#node Frame
			frame_17 = style_cartoon.nodes.new("NodeFrame")
			frame_17.label = "If no sec_struct, assign ribbon to peptide"
			frame_17.name = "Frame"
			frame_17.label_size = 20
			frame_17.shrink = True
			
			#node Frame.001
			frame_001_11 = style_cartoon.nodes.new("NodeFrame")
			frame_001_11.label = "Manually compute sec_struct"
			frame_001_11.name = "Frame.001"
			frame_001_11.label_size = 20
			frame_001_11.shrink = True
			
			#node Reroute.001
			reroute_001_16 = style_cartoon.nodes.new("NodeReroute")
			reroute_001_16.name = "Reroute.001"
			#node Reroute.002
			reroute_002_12 = style_cartoon.nodes.new("NodeReroute")
			reroute_002_12.name = "Reroute.002"
			#node Group.001
			group_001_17 = style_cartoon.nodes.new("GeometryNodeGroup")
			group_001_17.name = "Group.001"
			group_001_17.node_tree = separate_polymers
			
			#node Group.068
			group_068_1 = style_cartoon.nodes.new("GeometryNodeGroup")
			group_068_1.name = "Group.068"
			group_068_1.node_tree = _mn_utils_style_ribbon_nucleic
			#Input_28
			group_068_1.inputs[8].default_value = 0.1599999964237213
			#Input_29
			group_068_1.inputs[9].default_value = 4
			
			#node Group Input.002
			group_input_002_6 = style_cartoon.nodes.new("NodeGroupInput")
			group_input_002_6.name = "Group Input.002"
			group_input_002_6.outputs[3].hide = True
			
			#node Join Geometry
			join_geometry_3 = style_cartoon.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_3.name = "Join Geometry"
			
			#node Math.003
			math_003_7 = style_cartoon.nodes.new("ShaderNodeMath")
			math_003_7.name = "Math.003"
			math_003_7.operation = 'MULTIPLY'
			math_003_7.use_clamp = False
			#Value_001
			math_003_7.inputs[1].default_value = 2.0
			
			#node Math.004
			math_004_2 = style_cartoon.nodes.new("ShaderNodeMath")
			math_004_2.name = "Math.004"
			math_004_2.operation = 'MULTIPLY'
			math_004_2.use_clamp = False
			#Value_001
			math_004_2.inputs[1].default_value = 4.0
			
			#node Math.005
			math_005_2 = style_cartoon.nodes.new("ShaderNodeMath")
			math_005_2.name = "Math.005"
			math_005_2.operation = 'MULTIPLY'
			math_005_2.use_clamp = False
			#Value_001
			math_005_2.inputs[1].default_value = 3.0
			
			#node Reroute.003
			reroute_003_8 = style_cartoon.nodes.new("NodeReroute")
			reroute_003_8.name = "Reroute.003"
			#node Domain Size
			domain_size_5 = style_cartoon.nodes.new("GeometryNodeAttributeDomainSize")
			domain_size_5.name = "Domain Size"
			domain_size_5.component = 'MESH'
			domain_size_5.outputs[1].hide = True
			domain_size_5.outputs[2].hide = True
			domain_size_5.outputs[3].hide = True
			domain_size_5.outputs[4].hide = True
			domain_size_5.outputs[5].hide = True
			domain_size_5.outputs[6].hide = True
			
			#node Compare
			compare_19 = style_cartoon.nodes.new("FunctionNodeCompare")
			compare_19.name = "Compare"
			compare_19.data_type = 'INT'
			compare_19.mode = 'ELEMENT'
			compare_19.operation = 'EQUAL'
			#B_INT
			compare_19.inputs[3].default_value = 0
			
			#node Switch.003
			switch_003_1 = style_cartoon.nodes.new("GeometryNodeSwitch")
			switch_003_1.name = "Switch.003"
			switch_003_1.input_type = 'GEOMETRY'
			
			#node Realize Instances
			realize_instances_4 = style_cartoon.nodes.new("GeometryNodeRealizeInstances")
			realize_instances_4.name = "Realize Instances"
			#Selection
			realize_instances_4.inputs[1].default_value = True
			#Realize All
			realize_instances_4.inputs[2].default_value = True
			#Depth
			realize_instances_4.inputs[3].default_value = 0
			
			
			
			#Set parents
			store_named_attribute_9.parent = frame_17
			named_attribute_15.parent = frame_17
			string.parent = frame_17
			boolean_math_21.parent = frame_17
			select_peptide.parent = frame_17
			switch_002_4.parent = frame_17
			group_30.parent = frame_001_11
			switch_001_7.parent = frame_001_11
			group_input_001_12.parent = frame_001_11
			
			#Set locations
			group_output_86.location = (1060.0, 0.0)
			group_input_84.location = (-875.976806640625, 240.0)
			group_067.location = (500.0, 420.0)
			math_25.location = (20.0, -360.0)
			math_002_8.location = (20.0, -20.0)
			switch_21.location = (300.0, 140.0)
			math_001_14.location = (20.0, -200.0)
			reroute_23.location = (-76.95475006103516, -391.92510986328125)
			store_named_attribute_9.location = (-60.0, 640.0)
			named_attribute_15.location = (-380.0, 640.0)
			string.location = (-580.0, 540.0)
			boolean_math_21.location = (-220.0, 640.0)
			select_peptide.location = (-380.0, 480.0)
			switch_002_4.location = (-220.0, 480.0)
			group_30.location = (240.0, 480.0)
			switch_001_7.location = (240.0, 640.0)
			group_input_001_12.location = (240.0, 720.0)
			frame_17.location = (30.0, 140.0)
			frame_001_11.location = (10.0, 60.0)
			reroute_001_16.location = (-320.0, 380.0)
			reroute_002_12.location = (140.0, 380.0)
			group_001_17.location = (-595.976806640625, 380.0)
			group_068_1.location = (404.02313232421875, -620.0)
			group_input_002_6.location = (-201.03932189941406, -671.3316650390625)
			join_geometry_3.location = (841.2210693359375, -40.0)
			math_003_7.location = (184.02313232421875, -700.0)
			math_004_2.location = (184.02313232421875, -1020.0)
			math_005_2.location = (184.02313232421875, -860.0)
			reroute_003_8.location = (124.02312469482422, -800.0)
			domain_size_5.location = (580.0, 560.0)
			compare_19.location = (740.0, 560.0)
			switch_003_1.location = (819.6062622070312, 366.8473815917969)
			realize_instances_4.location = (660.0, -620.0)
			
			#Set dimensions
			group_output_86.width, group_output_86.height = 140.0, 100.0
			group_input_84.width, group_input_84.height = 131.2183837890625, 100.0
			group_067.width, group_067.height = 216.97686767578125, 100.0
			math_25.width, math_25.height = 140.0, 100.0
			math_002_8.width, math_002_8.height = 140.0, 100.0
			switch_21.width, switch_21.height = 140.0, 100.0
			math_001_14.width, math_001_14.height = 140.0, 100.0
			reroute_23.width, reroute_23.height = 16.0, 100.0
			store_named_attribute_9.width, store_named_attribute_9.height = 140.0, 100.0
			named_attribute_15.width, named_attribute_15.height = 140.0, 100.0
			string.width, string.height = 140.0, 100.0
			boolean_math_21.width, boolean_math_21.height = 140.0, 100.0
			select_peptide.width, select_peptide.height = 130.07904052734375, 100.0
			switch_002_4.width, switch_002_4.height = 140.0, 100.0
			group_30.width, group_30.height = 140.0, 100.0
			switch_001_7.width, switch_001_7.height = 140.0, 100.0
			group_input_001_12.width, group_input_001_12.height = 140.0, 100.0
			frame_17.width, frame_17.height = 720.0, 374.0
			frame_001_11.width, frame_001_11.height = 200.0, 430.0
			reroute_001_16.width, reroute_001_16.height = 16.0, 100.0
			reroute_002_12.width, reroute_002_12.height = 16.0, 100.0
			group_001_17.width, group_001_17.height = 140.0, 100.0
			group_068_1.width, group_068_1.height = 216.97686767578125, 100.0
			group_input_002_6.width, group_input_002_6.height = 131.2183837890625, 100.0
			join_geometry_3.width, join_geometry_3.height = 140.0, 100.0
			math_003_7.width, math_003_7.height = 140.0, 100.0
			math_004_2.width, math_004_2.height = 140.0, 100.0
			math_005_2.width, math_005_2.height = 140.0, 100.0
			reroute_003_8.width, reroute_003_8.height = 16.0, 100.0
			domain_size_5.width, domain_size_5.height = 140.0, 100.0
			compare_19.width, compare_19.height = 140.0, 100.0
			switch_003_1.width, switch_003_1.height = 140.0, 100.0
			realize_instances_4.width, realize_instances_4.height = 140.0, 100.0
			
			#initialize style_cartoon links
			#group_input_84.Selection -> group_067.Selection
			style_cartoon.links.new(group_input_84.outputs[1], group_067.inputs[1])
			#group_input_84.Shade Smooth -> group_067.Shade Smooth
			style_cartoon.links.new(group_input_84.outputs[12], group_067.inputs[2])
			#group_input_84.Color Blur -> group_067.Interpolate Color
			style_cartoon.links.new(group_input_84.outputs[11], group_067.inputs[3])
			#group_input_84.Material -> group_067.Material
			style_cartoon.links.new(group_input_84.outputs[13], group_067.inputs[4])
			#group_input_84.Thickness -> group_067.Sheet Thickness
			style_cartoon.links.new(group_input_84.outputs[7], group_067.inputs[13])
			#group_input_84.Width -> group_067.Sheet Width
			style_cartoon.links.new(group_input_84.outputs[8], group_067.inputs[14])
			#group_input_84.Smoothing -> group_067.Sheet Smoothing
			style_cartoon.links.new(group_input_84.outputs[10], group_067.inputs[15])
			#group_input_84.Loop Radius -> group_067.Loop Radius
			style_cartoon.links.new(group_input_84.outputs[9], group_067.inputs[28])
			#group_input_84.Rounded -> group_067.Arrows Sharp
			style_cartoon.links.new(group_input_84.outputs[6], group_067.inputs[6])
			#group_input_84.Cylinders -> group_067.As Cylinders
			style_cartoon.links.new(group_input_84.outputs[4], group_067.inputs[17])
			#reroute_23.Output -> math_25.Value
			style_cartoon.links.new(reroute_23.outputs[0], math_25.inputs[0])
			#math_25.Value -> group_067.Cylinder Subdivisions
			style_cartoon.links.new(math_25.outputs[0], group_067.inputs[21])
			#math_25.Value -> group_067.Loop Subdivisions
			style_cartoon.links.new(math_25.outputs[0], group_067.inputs[27])
			#math_25.Value -> group_067.Sheet Subdivision
			style_cartoon.links.new(math_25.outputs[0], group_067.inputs[16])
			#math_25.Value -> group_067.Helix Subdivisions
			style_cartoon.links.new(math_25.outputs[0], group_067.inputs[25])
			#group_input_84.Arrows -> group_067.As Arrows
			style_cartoon.links.new(group_input_84.outputs[5], group_067.inputs[5])
			#group_input_84.Quality -> math_002_8.Value
			style_cartoon.links.new(group_input_84.outputs[2], math_002_8.inputs[0])
			#group_input_84.Rounded -> switch_21.Switch
			style_cartoon.links.new(group_input_84.outputs[6], switch_21.inputs[0])
			#math_002_8.Value -> switch_21.True
			style_cartoon.links.new(math_002_8.outputs[0], switch_21.inputs[2])
			#switch_21.Output -> group_067.Profile Resolution
			style_cartoon.links.new(switch_21.outputs[0], group_067.inputs[11])
			#group_input_84.Width -> group_067.Helix Width
			style_cartoon.links.new(group_input_84.outputs[8], group_067.inputs[24])
			#group_input_84.Thickness -> group_067.Helix Thickness
			style_cartoon.links.new(group_input_84.outputs[7], group_067.inputs[23])
			#math_002_8.Value -> group_067.Loop Resolution
			style_cartoon.links.new(math_002_8.outputs[0], group_067.inputs[29])
			#group_input_84.Width -> group_067.Cylinder Radius
			style_cartoon.links.new(group_input_84.outputs[8], group_067.inputs[19])
			#reroute_23.Output -> math_001_14.Value
			style_cartoon.links.new(reroute_23.outputs[0], math_001_14.inputs[0])
			#group_input_84.Quality -> reroute_23.Input
			style_cartoon.links.new(group_input_84.outputs[2], reroute_23.inputs[0])
			#math_001_14.Value -> group_067.Cylinder Resolution
			style_cartoon.links.new(math_001_14.outputs[0], group_067.inputs[20])
			#reroute_001_16.Output -> store_named_attribute_9.Geometry
			style_cartoon.links.new(reroute_001_16.outputs[0], store_named_attribute_9.inputs[0])
			#string.String -> named_attribute_15.Name
			style_cartoon.links.new(string.outputs[0], named_attribute_15.inputs[0])
			#string.String -> store_named_attribute_9.Name
			style_cartoon.links.new(string.outputs[0], store_named_attribute_9.inputs[2])
			#named_attribute_15.Exists -> boolean_math_21.Boolean
			style_cartoon.links.new(named_attribute_15.outputs[1], boolean_math_21.inputs[0])
			#boolean_math_21.Boolean -> store_named_attribute_9.Selection
			style_cartoon.links.new(boolean_math_21.outputs[0], store_named_attribute_9.inputs[1])
			#select_peptide.Selection -> switch_002_4.Switch
			style_cartoon.links.new(select_peptide.outputs[0], switch_002_4.inputs[0])
			#switch_002_4.Output -> store_named_attribute_9.Value
			style_cartoon.links.new(switch_002_4.outputs[0], store_named_attribute_9.inputs[3])
			#reroute_002_12.Output -> group_30.Atoms
			style_cartoon.links.new(reroute_002_12.outputs[0], group_30.inputs[0])
			#group_30.Atoms -> switch_001_7.True
			style_cartoon.links.new(group_30.outputs[0], switch_001_7.inputs[2])
			#store_named_attribute_9.Geometry -> switch_001_7.False
			style_cartoon.links.new(store_named_attribute_9.outputs[0], switch_001_7.inputs[1])
			#switch_001_7.Output -> group_067.Atoms
			style_cartoon.links.new(switch_001_7.outputs[0], group_067.inputs[0])
			#group_input_001_12.DSSP -> switch_001_7.Switch
			style_cartoon.links.new(group_input_001_12.outputs[3], switch_001_7.inputs[0])
			#group_001_17.Peptide -> reroute_001_16.Input
			style_cartoon.links.new(group_001_17.outputs[0], reroute_001_16.inputs[0])
			#reroute_001_16.Output -> reroute_002_12.Input
			style_cartoon.links.new(reroute_001_16.outputs[0], reroute_002_12.inputs[0])
			#group_input_84.Atoms -> group_001_17.Atoms
			style_cartoon.links.new(group_input_84.outputs[0], group_001_17.inputs[0])
			#realize_instances_4.Geometry -> join_geometry_3.Geometry
			style_cartoon.links.new(realize_instances_4.outputs[0], join_geometry_3.inputs[0])
			#join_geometry_3.Geometry -> group_output_86.Geometry
			style_cartoon.links.new(join_geometry_3.outputs[0], group_output_86.inputs[0])
			#group_001_17.Nucleic -> group_068_1.Atoms
			style_cartoon.links.new(group_001_17.outputs[1], group_068_1.inputs[0])
			#group_input_002_6.Material -> group_068_1.Material
			style_cartoon.links.new(group_input_002_6.outputs[13], group_068_1.inputs[2])
			#group_input_002_6.Color Blur -> group_068_1.Intepolate Color
			style_cartoon.links.new(group_input_002_6.outputs[11], group_068_1.inputs[3])
			#reroute_003_8.Output -> math_003_7.Value
			style_cartoon.links.new(reroute_003_8.outputs[0], math_003_7.inputs[0])
			#math_003_7.Value -> group_068_1.Backbone Subdivisions
			style_cartoon.links.new(math_003_7.outputs[0], group_068_1.inputs[4])
			#reroute_003_8.Output -> math_004_2.Value
			style_cartoon.links.new(reroute_003_8.outputs[0], math_004_2.inputs[0])
			#math_004_2.Value -> group_068_1.Backbone Resolution
			style_cartoon.links.new(math_004_2.outputs[0], group_068_1.inputs[5])
			#group_input_002_6.Shade Smooth -> group_068_1.Backbone Shade Smooth
			style_cartoon.links.new(group_input_002_6.outputs[12], group_068_1.inputs[7])
			#group_input_002_6.Selection -> group_068_1.Selection
			style_cartoon.links.new(group_input_002_6.outputs[1], group_068_1.inputs[1])
			#group_input_002_6.Loop Radius -> math_005_2.Value
			style_cartoon.links.new(group_input_002_6.outputs[9], math_005_2.inputs[0])
			#math_005_2.Value -> group_068_1.Backbone Radius
			style_cartoon.links.new(math_005_2.outputs[0], group_068_1.inputs[6])
			#group_input_002_6.Quality -> reroute_003_8.Input
			style_cartoon.links.new(group_input_002_6.outputs[2], reroute_003_8.inputs[0])
			#domain_size_5.Point Count -> compare_19.A
			style_cartoon.links.new(domain_size_5.outputs[0], compare_19.inputs[2])
			#group_067.Cartoon Mesh -> switch_003_1.False
			style_cartoon.links.new(group_067.outputs[0], switch_003_1.inputs[1])
			#compare_19.Result -> switch_003_1.Switch
			style_cartoon.links.new(compare_19.outputs[0], switch_003_1.inputs[0])
			#switch_001_7.Output -> domain_size_5.Geometry
			style_cartoon.links.new(switch_001_7.outputs[0], domain_size_5.inputs[0])
			#group_068_1.Ribbon + Bases -> realize_instances_4.Geometry
			style_cartoon.links.new(group_068_1.outputs[0], realize_instances_4.inputs[0])
			#switch_003_1.Output -> join_geometry_3.Geometry
			style_cartoon.links.new(switch_003_1.outputs[0], join_geometry_3.inputs[0])
			return style_cartoon

		style_cartoon = style_cartoon_node_group()

		#initialize is_side_chain node group
		def is_side_chain_node_group():
			is_side_chain = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Is Side Chain")

			is_side_chain.color_tag = 'INPUT'
			is_side_chain.description = ""

			
			#is_side_chain interface
			#Socket Selection
			selection_socket_23 = is_side_chain.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket_23.attribute_domain = 'POINT'
			selection_socket_23.description = "True if atom is part of the side chain for either an amino acid or a nucleic acid"
			
			#Socket Inverted
			inverted_socket_9 = is_side_chain.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket_9.attribute_domain = 'POINT'
			
			#Socket And
			and_socket_9 = is_side_chain.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket_9.attribute_domain = 'POINT'
			and_socket_9.hide_value = True
			
			#Socket Or
			or_socket_8 = is_side_chain.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket_8.attribute_domain = 'POINT'
			or_socket_8.hide_value = True
			
			
			#initialize is_side_chain nodes
			#node Boolean Math.001
			boolean_math_001_16 = is_side_chain.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_16.name = "Boolean Math.001"
			boolean_math_001_16.operation = 'OR'
			
			#node Group Input
			group_input_85 = is_side_chain.nodes.new("NodeGroupInput")
			group_input_85.name = "Group Input"
			
			#node Boolean Math
			boolean_math_22 = is_side_chain.nodes.new("FunctionNodeBooleanMath")
			boolean_math_22.name = "Boolean Math"
			boolean_math_22.operation = 'AND'
			
			#node Group Output
			group_output_87 = is_side_chain.nodes.new("NodeGroupOutput")
			group_output_87.name = "Group Output"
			group_output_87.is_active_output = True
			
			#node Group.001
			group_001_18 = is_side_chain.nodes.new("GeometryNodeGroup")
			group_001_18.name = "Group.001"
			group_001_18.node_tree = _mn_select_nucleic
			
			#node Group.002
			group_002_11 = is_side_chain.nodes.new("GeometryNodeGroup")
			group_002_11.name = "Group.002"
			group_002_11.node_tree = _mn_select_peptide
			
			#node Group
			group_31 = is_side_chain.nodes.new("GeometryNodeGroup")
			group_31.name = "Group"
			group_31.node_tree = fallback_boolean
			#Socket_2
			group_31.inputs[0].default_value = "is_side_chain"
			
			#node Boolean Math.002
			boolean_math_002_14 = is_side_chain.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002_14.name = "Boolean Math.002"
			boolean_math_002_14.operation = 'OR'
			
			#node Boolean Math.003
			boolean_math_003_12 = is_side_chain.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003_12.name = "Boolean Math.003"
			boolean_math_003_12.operation = 'NOT'
			
			
			
			
			#Set locations
			boolean_math_001_16.location = (-460.0, -80.0)
			group_input_85.location = (-280.0, 20.0)
			boolean_math_22.location = (-120.0, 20.0)
			group_output_87.location = (240.00001525878906, 20.0)
			group_001_18.location = (-740.0, -80.0)
			group_002_11.location = (-740.0, -220.0)
			group_31.location = (-300.0, -80.0)
			boolean_math_002_14.location = (59.99999237060547, 20.0)
			boolean_math_003_12.location = (60.0, -120.0)
			
			#Set dimensions
			boolean_math_001_16.width, boolean_math_001_16.height = 140.0, 100.0
			group_input_85.width, group_input_85.height = 140.0, 100.0
			boolean_math_22.width, boolean_math_22.height = 140.0, 100.0
			group_output_87.width, group_output_87.height = 140.0, 100.0
			group_001_18.width, group_001_18.height = 244.02914428710938, 100.0
			group_002_11.width, group_002_11.height = 244.02914428710938, 100.0
			group_31.width, group_31.height = 140.0, 100.0
			boolean_math_002_14.width, boolean_math_002_14.height = 140.0, 100.0
			boolean_math_003_12.width, boolean_math_003_12.height = 140.0, 100.0
			
			#initialize is_side_chain links
			#group_input_85.And -> boolean_math_22.Boolean
			is_side_chain.links.new(group_input_85.outputs[0], boolean_math_22.inputs[0])
			#group_001_18.Is Side Chain -> boolean_math_001_16.Boolean
			is_side_chain.links.new(group_001_18.outputs[1], boolean_math_001_16.inputs[0])
			#group_002_11.Is Side Chain -> boolean_math_001_16.Boolean
			is_side_chain.links.new(group_002_11.outputs[1], boolean_math_001_16.inputs[1])
			#boolean_math_001_16.Boolean -> group_31.Fallback
			is_side_chain.links.new(boolean_math_001_16.outputs[0], group_31.inputs[1])
			#group_31.Boolean -> boolean_math_22.Boolean
			is_side_chain.links.new(group_31.outputs[0], boolean_math_22.inputs[1])
			#boolean_math_002_14.Boolean -> group_output_87.Selection
			is_side_chain.links.new(boolean_math_002_14.outputs[0], group_output_87.inputs[0])
			#boolean_math_22.Boolean -> boolean_math_002_14.Boolean
			is_side_chain.links.new(boolean_math_22.outputs[0], boolean_math_002_14.inputs[0])
			#group_input_85.Or -> boolean_math_002_14.Boolean
			is_side_chain.links.new(group_input_85.outputs[1], boolean_math_002_14.inputs[1])
			#boolean_math_002_14.Boolean -> boolean_math_003_12.Boolean
			is_side_chain.links.new(boolean_math_002_14.outputs[0], boolean_math_003_12.inputs[0])
			#boolean_math_003_12.Boolean -> group_output_87.Inverted
			is_side_chain.links.new(boolean_math_003_12.outputs[0], group_output_87.inputs[1])
			return is_side_chain

		is_side_chain = is_side_chain_node_group()

		#initialize bond_count node group
		def bond_count_node_group():
			bond_count = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Bond Count")

			bond_count.color_tag = 'INPUT'
			bond_count.description = ""

			
			#bond_count interface
			#Socket Is Bonded
			is_bonded_socket_3 = bond_count.interface.new_socket(name = "Is Bonded", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_bonded_socket_3.attribute_domain = 'POINT'
			
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
			group_output_88 = bond_count.nodes.new("NodeGroupOutput")
			group_output_88.name = "Group Output"
			group_output_88.is_active_output = True
			
			#node Group Input
			group_input_86 = bond_count.nodes.new("NodeGroupInput")
			group_input_86.name = "Group Input"
			
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
			compare_20 = bond_count.nodes.new("FunctionNodeCompare")
			compare_20.name = "Compare"
			compare_20.data_type = 'INT'
			compare_20.mode = 'ELEMENT'
			compare_20.operation = 'GREATER_THAN'
			#B_INT
			compare_20.inputs[3].default_value = 0
			
			
			
			
			#Set locations
			group_output_88.location = (200.0, 100.0)
			group_input_86.location = (-200.0, 0.0)
			edges_of_vertex_001.location = (0.0, 0.0)
			compare_20.location = (0.0, 160.0)
			
			#Set dimensions
			group_output_88.width, group_output_88.height = 140.0, 100.0
			group_input_86.width, group_input_86.height = 140.0, 100.0
			edges_of_vertex_001.width, edges_of_vertex_001.height = 140.0, 100.0
			compare_20.width, compare_20.height = 140.0, 100.0
			
			#initialize bond_count links
			#edges_of_vertex_001.Total -> group_output_88.Bonds
			bond_count.links.new(edges_of_vertex_001.outputs[1], group_output_88.inputs[1])
			#edges_of_vertex_001.Total -> compare_20.A
			bond_count.links.new(edges_of_vertex_001.outputs[1], compare_20.inputs[2])
			#compare_20.Result -> group_output_88.Is Bonded
			bond_count.links.new(compare_20.outputs[0], group_output_88.inputs[0])
			return bond_count

		bond_count = bond_count_node_group()

		#initialize style_preset_2 node group
		def style_preset_2_node_group():
			style_preset_2 = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Style Preset 2")

			style_preset_2.color_tag = 'GEOMETRY'
			style_preset_2.description = ""

			
			#style_preset_2 interface
			#Socket Geometry
			geometry_socket_16 = style_preset_2.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_16.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket_18 = style_preset_2.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_18.attribute_domain = 'POINT'
			
			#Socket Selection
			selection_socket_24 = style_preset_2.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_24.attribute_domain = 'POINT'
			selection_socket_24.hide_value = True
			
			#Socket Quality
			quality_socket_3 = style_preset_2.interface.new_socket(name = "Quality", in_out='INPUT', socket_type = 'NodeSocketInt')
			quality_socket_3.subtype = 'NONE'
			quality_socket_3.default_value = 3
			quality_socket_3.min_value = 0
			quality_socket_3.max_value = 6
			quality_socket_3.attribute_domain = 'POINT'
			
			#Socket Color Blur
			color_blur_socket_3 = style_preset_2.interface.new_socket(name = "Color Blur", in_out='INPUT', socket_type = 'NodeSocketBool')
			color_blur_socket_3.attribute_domain = 'POINT'
			
			#Socket Shade Smooth
			shade_smooth_socket_7 = style_preset_2.interface.new_socket(name = "Shade Smooth", in_out='INPUT', socket_type = 'NodeSocketBool')
			shade_smooth_socket_7.attribute_domain = 'POINT'
			
			#Socket Material
			material_socket_9 = style_preset_2.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial')
			material_socket_9.attribute_domain = 'POINT'
			
			
			#initialize style_preset_2 nodes
			#node Group Output
			group_output_89 = style_preset_2.nodes.new("NodeGroupOutput")
			group_output_89.name = "Group Output"
			group_output_89.is_active_output = True
			
			#node Group Input
			group_input_87 = style_preset_2.nodes.new("NodeGroupInput")
			group_input_87.name = "Group Input"
			
			#node Compare.004
			compare_004_2 = style_preset_2.nodes.new("FunctionNodeCompare")
			compare_004_2.name = "Compare.004"
			compare_004_2.data_type = 'INT'
			compare_004_2.mode = 'ELEMENT'
			compare_004_2.operation = 'GREATER_THAN'
			#B_INT
			compare_004_2.inputs[3].default_value = 0
			
			#node Switch.004
			switch_004_1 = style_preset_2.nodes.new("GeometryNodeSwitch")
			switch_004_1.name = "Switch.004"
			switch_004_1.input_type = 'FLOAT'
			#False
			switch_004_1.inputs[1].default_value = 1.0
			#True
			switch_004_1.inputs[2].default_value = 0.30000001192092896
			
			#node Separate Geometry.002
			separate_geometry_002_2 = style_preset_2.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_002_2.name = "Separate Geometry.002"
			separate_geometry_002_2.domain = 'POINT'
			
			#node Group.010
			group_010_8 = style_preset_2.nodes.new("GeometryNodeGroup")
			group_010_8.name = "Group.010"
			group_010_8.node_tree = _mn_utils_int_multiply
			#Input_1
			group_010_8.inputs[1].default_value = 4
			
			#node Group.003
			group_003_9 = style_preset_2.nodes.new("GeometryNodeGroup")
			group_003_9.label = "Ball and Stick"
			group_003_9.name = "Group.003"
			group_003_9.node_tree = style_ball_and_stick
			#Socket_5
			group_003_9.inputs[1].default_value = 0
			#Input_1
			group_003_9.inputs[2].default_value = True
			#Input_2
			group_003_9.inputs[3].default_value = True
			#Socket_3
			group_003_9.inputs[5].default_value = True
			#Input_7
			group_003_9.inputs[6].default_value = 0.25
			
			#node Group
			group_32 = style_preset_2.nodes.new("GeometryNodeGroup")
			group_32.label = "Separate Polymers"
			group_32.name = "Group"
			group_32.node_tree = separate_polymers
			
			#node MN_select_proximity
			mn_select_proximity = style_preset_2.nodes.new("GeometryNodeGroup")
			mn_select_proximity.label = "Select Proximity"
			mn_select_proximity.name = "MN_select_proximity"
			mn_select_proximity.node_tree = select_proximity
			#Input_5
			mn_select_proximity.inputs[1].default_value = True
			#Input_4
			mn_select_proximity.inputs[2].default_value = True
			#Input_1
			mn_select_proximity.inputs[3].default_value = 3.0
			
			#node MN_select_atomic_number
			mn_select_atomic_number = style_preset_2.nodes.new("GeometryNodeGroup")
			mn_select_atomic_number.label = "Select Atomic Number"
			mn_select_atomic_number.name = "MN_select_atomic_number"
			mn_select_atomic_number.node_tree = select_atomic_number
			#Socket_0
			mn_select_atomic_number.inputs[0].default_value = True
			#Socket_1
			mn_select_atomic_number.inputs[1].default_value = False
			#Input_0
			mn_select_atomic_number.inputs[2].default_value = 1
			
			#node Boolean Math.001
			boolean_math_001_17 = style_preset_2.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_17.name = "Boolean Math.001"
			boolean_math_001_17.operation = 'NIMPLY'
			
			#node MN_style_sticks
			mn_style_sticks = style_preset_2.nodes.new("GeometryNodeGroup")
			mn_style_sticks.label = "Style Sticks"
			mn_style_sticks.name = "MN_style_sticks"
			mn_style_sticks.node_tree = style_sticks
			#Socket_4
			mn_style_sticks.inputs[2].default_value = 2
			#Socket_3
			mn_style_sticks.inputs[3].default_value = 0.20000000298023224
			
			#node Join Geometry.002
			join_geometry_002_2 = style_preset_2.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_002_2.name = "Join Geometry.002"
			
			#node Join Geometry.003
			join_geometry_003 = style_preset_2.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_003.name = "Join Geometry.003"
			
			#node Domain Size
			domain_size_6 = style_preset_2.nodes.new("GeometryNodeAttributeDomainSize")
			domain_size_6.name = "Domain Size"
			domain_size_6.component = 'MESH'
			domain_size_6.outputs[1].hide = True
			domain_size_6.outputs[2].hide = True
			domain_size_6.outputs[3].hide = True
			domain_size_6.outputs[4].hide = True
			domain_size_6.outputs[5].hide = True
			
			#node Compare.005
			compare_005_2 = style_preset_2.nodes.new("FunctionNodeCompare")
			compare_005_2.name = "Compare.005"
			compare_005_2.data_type = 'INT'
			compare_005_2.mode = 'ELEMENT'
			compare_005_2.operation = 'GREATER_THAN'
			#B_INT
			compare_005_2.inputs[3].default_value = 0
			
			#node Boolean Math.003
			boolean_math_003_13 = style_preset_2.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003_13.name = "Boolean Math.003"
			boolean_math_003_13.operation = 'AND'
			
			#node MN_style_cartoon
			mn_style_cartoon = style_preset_2.nodes.new("GeometryNodeGroup")
			mn_style_cartoon.name = "MN_style_cartoon"
			mn_style_cartoon.node_tree = style_cartoon
			#Input_1
			mn_style_cartoon.inputs[1].default_value = True
			#Socket_3
			mn_style_cartoon.inputs[3].default_value = False
			#Input_4
			mn_style_cartoon.inputs[4].default_value = False
			#Input_3
			mn_style_cartoon.inputs[5].default_value = True
			#Input_11
			mn_style_cartoon.inputs[6].default_value = False
			#Input_5
			mn_style_cartoon.inputs[7].default_value = 0.4000000059604645
			#Input_6
			mn_style_cartoon.inputs[8].default_value = 2.4000000953674316
			#Input_12
			mn_style_cartoon.inputs[9].default_value = 0.20000000298023224
			#Input_7
			mn_style_cartoon.inputs[10].default_value = 0.5
			
			#node Group.013
			group_013_3 = style_preset_2.nodes.new("GeometryNodeGroup")
			group_013_3.name = "Group.013"
			group_013_3.node_tree = is_side_chain
			#Socket_3
			group_013_3.inputs[1].default_value = False
			
			#node Frame
			frame_18 = style_preset_2.nodes.new("NodeFrame")
			frame_18.label = "Sticks for atoms that are close to nucleic acids or ligands"
			frame_18.name = "Frame"
			frame_18.label_size = 20
			frame_18.shrink = True
			
			#node Frame.001
			frame_001_12 = style_preset_2.nodes.new("NodeFrame")
			frame_001_12.label = "Cartoon that is applied to protein"
			frame_001_12.name = "Frame.001"
			frame_001_12.label_size = 20
			frame_001_12.shrink = True
			
			#node Frame.003
			frame_003_5 = style_preset_2.nodes.new("NodeFrame")
			frame_003_5.label = "Ball and stick for non-peptide and non-nucleic atoms"
			frame_003_5.name = "Frame.003"
			frame_003_5.label_size = 20
			frame_003_5.shrink = True
			
			#node Group.001
			group_001_19 = style_preset_2.nodes.new("GeometryNodeGroup")
			group_001_19.name = "Group.001"
			group_001_19.node_tree = bond_count
			
			#node Join Geometry
			join_geometry_4 = style_preset_2.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_4.name = "Join Geometry"
			
			
			
			#Set parents
			compare_004_2.parent = frame_003_5
			switch_004_1.parent = frame_003_5
			group_010_8.parent = frame_003_5
			group_003_9.parent = frame_003_5
			mn_select_proximity.parent = frame_18
			mn_select_atomic_number.parent = frame_18
			boolean_math_001_17.parent = frame_18
			mn_style_sticks.parent = frame_18
			join_geometry_002_2.parent = frame_18
			domain_size_6.parent = frame_18
			compare_005_2.parent = frame_18
			boolean_math_003_13.parent = frame_18
			mn_style_cartoon.parent = frame_001_12
			group_013_3.parent = frame_18
			
			#Set locations
			group_output_89.location = (900.0, 80.0)
			group_input_87.location = (-1011.8084716796875, 0.0)
			compare_004_2.location = (-60.0, -780.0)
			switch_004_1.location = (100.0, -780.0)
			separate_geometry_002_2.location = (-760.0, 60.0)
			group_010_8.location = (100.0, -940.0)
			group_003_9.location = (328.498291015625, -688.9818115234375)
			group_32.location = (-580.0, 60.0)
			mn_select_proximity.location = (-100.0, 640.0)
			mn_select_atomic_number.location = (-100.0, 460.0)
			boolean_math_001_17.location = (140.0, 640.0)
			mn_style_sticks.location = (620.0, 780.0)
			join_geometry_002_2.location = (-300.0, 460.0)
			join_geometry_003.location = (680.0, 100.0)
			domain_size_6.location = (-309.04931640625, 584.9669189453125)
			compare_005_2.location = (-309.04931640625, 744.9669189453125)
			boolean_math_003_13.location = (460.0, 780.0)
			mn_style_cartoon.location = (220.0, 100.0)
			group_013_3.location = (300.0, 640.0)
			frame_18.location = (-361.0, -60.0)
			frame_001_12.location = (0.0, 0.0)
			frame_003_5.location = (-90.0, 269.0)
			group_001_19.location = (-420.0, -560.0)
			join_geometry_4.location = (40.0, 100.0)
			
			#Set dimensions
			group_output_89.width, group_output_89.height = 140.0, 100.0
			group_input_87.width, group_input_87.height = 140.0, 100.0
			compare_004_2.width, compare_004_2.height = 140.0, 100.0
			switch_004_1.width, switch_004_1.height = 140.0, 100.0
			separate_geometry_002_2.width, separate_geometry_002_2.height = 140.0, 100.0
			group_010_8.width, group_010_8.height = 140.0, 100.0
			group_003_9.width, group_003_9.height = 200.0, 100.0
			group_32.width, group_32.height = 200.0, 100.0
			mn_select_proximity.width, mn_select_proximity.height = 200.0, 100.0
			mn_select_atomic_number.width, mn_select_atomic_number.height = 200.0, 100.0
			boolean_math_001_17.width, boolean_math_001_17.height = 140.0, 100.0
			mn_style_sticks.width, mn_style_sticks.height = 200.0, 100.0
			join_geometry_002_2.width, join_geometry_002_2.height = 140.0, 100.0
			join_geometry_003.width, join_geometry_003.height = 140.0, 100.0
			domain_size_6.width, domain_size_6.height = 140.0, 100.0
			compare_005_2.width, compare_005_2.height = 140.0, 100.0
			boolean_math_003_13.width, boolean_math_003_13.height = 140.0, 100.0
			mn_style_cartoon.width, mn_style_cartoon.height = 200.0, 100.0
			group_013_3.width, group_013_3.height = 140.0, 100.0
			frame_18.width, frame_18.height = 1189.60009765625, 530.7999877929688
			frame_001_12.width, frame_001_12.height = 260.0, 503.6000061035156
			frame_003_5.width, frame_003_5.height = 648.800048828125, 439.5999755859375
			group_001_19.width, group_001_19.height = 140.0, 100.0
			join_geometry_4.width, join_geometry_4.height = 140.0, 100.0
			
			#initialize style_preset_2 links
			#group_input_87.Material -> group_003_9.Material
			style_preset_2.links.new(group_input_87.outputs[5], group_003_9.inputs[9])
			#separate_geometry_002_2.Selection -> group_32.Atoms
			style_preset_2.links.new(separate_geometry_002_2.outputs[0], group_32.inputs[0])
			#group_input_87.Shade Smooth -> group_003_9.Shade Smooth
			style_preset_2.links.new(group_input_87.outputs[4], group_003_9.inputs[8])
			#group_input_87.Shade Smooth -> mn_style_cartoon.Shade Smooth
			style_preset_2.links.new(group_input_87.outputs[4], mn_style_cartoon.inputs[12])
			#group_32.Other -> group_003_9.Atoms
			style_preset_2.links.new(group_32.outputs[2], group_003_9.inputs[0])
			#group_input_87.Quality -> mn_style_cartoon.Quality
			style_preset_2.links.new(group_input_87.outputs[2], mn_style_cartoon.inputs[2])
			#boolean_math_003_13.Boolean -> mn_style_sticks.Selection
			style_preset_2.links.new(boolean_math_003_13.outputs[0], mn_style_sticks.inputs[1])
			#switch_004_1.Output -> group_003_9.Sphere Radii
			style_preset_2.links.new(switch_004_1.outputs[0], group_003_9.inputs[4])
			#group_001_19.Bonds -> compare_004_2.A
			style_preset_2.links.new(group_001_19.outputs[1], compare_004_2.inputs[2])
			#compare_005_2.Result -> boolean_math_003_13.Boolean
			style_preset_2.links.new(compare_005_2.outputs[0], boolean_math_003_13.inputs[0])
			#domain_size_6.Point Count -> compare_005_2.A
			style_preset_2.links.new(domain_size_6.outputs[0], compare_005_2.inputs[2])
			#compare_004_2.Result -> switch_004_1.Switch
			style_preset_2.links.new(compare_004_2.outputs[0], switch_004_1.inputs[0])
			#join_geometry_002_2.Geometry -> domain_size_6.Geometry
			style_preset_2.links.new(join_geometry_002_2.outputs[0], domain_size_6.inputs[0])
			#group_32.Peptide -> mn_style_sticks.Atoms
			style_preset_2.links.new(group_32.outputs[0], mn_style_sticks.inputs[0])
			#group_input_87.Shade Smooth -> mn_style_sticks.Shade Smooth
			style_preset_2.links.new(group_input_87.outputs[4], mn_style_sticks.inputs[5])
			#mn_select_proximity.Selection -> boolean_math_001_17.Boolean
			style_preset_2.links.new(mn_select_proximity.outputs[0], boolean_math_001_17.inputs[0])
			#group_input_87.Material -> mn_style_cartoon.Material
			style_preset_2.links.new(group_input_87.outputs[5], mn_style_cartoon.inputs[13])
			#join_geometry_002_2.Geometry -> mn_select_proximity.Target Atoms
			style_preset_2.links.new(join_geometry_002_2.outputs[0], mn_select_proximity.inputs[0])
			#group_input_87.Quality -> group_010_8.Value
			style_preset_2.links.new(group_input_87.outputs[2], group_010_8.inputs[0])
			#group_32.Other -> join_geometry_002_2.Geometry
			style_preset_2.links.new(group_32.outputs[2], join_geometry_002_2.inputs[0])
			#group_input_87.Selection -> separate_geometry_002_2.Selection
			style_preset_2.links.new(group_input_87.outputs[1], separate_geometry_002_2.inputs[1])
			#group_input_87.Atoms -> separate_geometry_002_2.Geometry
			style_preset_2.links.new(group_input_87.outputs[0], separate_geometry_002_2.inputs[0])
			#join_geometry_003.Geometry -> group_output_89.Geometry
			style_preset_2.links.new(join_geometry_003.outputs[0], group_output_89.inputs[0])
			#group_input_87.Material -> mn_style_sticks.Material
			style_preset_2.links.new(group_input_87.outputs[5], mn_style_sticks.inputs[6])
			#mn_select_atomic_number.Selection -> boolean_math_001_17.Boolean
			style_preset_2.links.new(mn_select_atomic_number.outputs[0], boolean_math_001_17.inputs[1])
			#boolean_math_001_17.Boolean -> group_013_3.And
			style_preset_2.links.new(boolean_math_001_17.outputs[0], group_013_3.inputs[0])
			#group_013_3.Selection -> boolean_math_003_13.Boolean
			style_preset_2.links.new(group_013_3.outputs[0], boolean_math_003_13.inputs[1])
			#group_003_9.Geometry -> join_geometry_003.Geometry
			style_preset_2.links.new(group_003_9.outputs[0], join_geometry_003.inputs[0])
			#group_32.Nucleic -> join_geometry_4.Geometry
			style_preset_2.links.new(group_32.outputs[1], join_geometry_4.inputs[0])
			#join_geometry_4.Geometry -> mn_style_cartoon.Atoms
			style_preset_2.links.new(join_geometry_4.outputs[0], mn_style_cartoon.inputs[0])
			#group_input_87.Color Blur -> mn_style_sticks.Color Blur
			style_preset_2.links.new(group_input_87.outputs[3], mn_style_sticks.inputs[4])
			#group_input_87.Color Blur -> mn_style_cartoon.Color Blur
			style_preset_2.links.new(group_input_87.outputs[3], mn_style_cartoon.inputs[11])
			#group_input_87.Color Blur -> group_003_9.Color Blur
			style_preset_2.links.new(group_input_87.outputs[3], group_003_9.inputs[7])
			#group_32.Nucleic -> join_geometry_002_2.Geometry
			style_preset_2.links.new(group_32.outputs[1], join_geometry_002_2.inputs[0])
			#mn_style_cartoon.Geometry -> join_geometry_003.Geometry
			style_preset_2.links.new(mn_style_cartoon.outputs[0], join_geometry_003.inputs[0])
			#group_32.Peptide -> join_geometry_4.Geometry
			style_preset_2.links.new(group_32.outputs[0], join_geometry_4.inputs[0])
			#mn_style_sticks.Geometry -> join_geometry_003.Geometry
			style_preset_2.links.new(mn_style_sticks.outputs[0], join_geometry_003.inputs[0])
			return style_preset_2

		style_preset_2 = style_preset_2_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Style Preset 2", type = 'NODES')
		mod.node_group = style_preset_2
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Style_Preset_2.bl_idname)
			
def register():
	bpy.utils.register_class(Style_Preset_2)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Style_Preset_2)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
