bl_info = {
    "name": "WiggleProt",
    "author": "Node To Python",
    "version": (1, 0, 0),
    "blender": (4, 2, 1),
    "location": "Node",
    "category": "Node",
}

import bpy
import mathutils
import os


class wiggle(bpy.types.Operator):
    bl_idname = "node.wiggleprot"
    bl_label = "wiggleprot"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        # initialize set_color node group
        def set_color_node_group():
            set_color = bpy.data.node_groups.new(
                type="GeometryNodeTree", name="Set Color"
            )

            set_color.color_tag = "GEOMETRY"
            set_color.description = ""

            set_color.is_modifier = True

            # set_color interface
            # Socket Atoms
            atoms_socket = set_color.interface.new_socket(
                name="Atoms", in_out="OUTPUT", socket_type="NodeSocketGeometry"
            )
            atoms_socket.attribute_domain = "POINT"
            atoms_socket.description = (
                "Atomic geometry with an updated `Color` attribute"
            )

            # Socket Atoms
            atoms_socket_1 = set_color.interface.new_socket(
                name="Atoms", in_out="INPUT", socket_type="NodeSocketGeometry"
            )
            atoms_socket_1.attribute_domain = "POINT"
            atoms_socket_1.description = (
                "Atomic geometry that contains vertices and edges"
            )

            # Socket Selection
            selection_socket = set_color.interface.new_socket(
                name="Selection", in_out="INPUT", socket_type="NodeSocketBool"
            )
            selection_socket.attribute_domain = "POINT"
            selection_socket.hide_value = True
            selection_socket.description = "Selection of atoms to apply this node to"

            # Socket Color
            color_socket = set_color.interface.new_socket(
                name="Color", in_out="INPUT", socket_type="NodeSocketColor"
            )
            color_socket.attribute_domain = "POINT"
            color_socket.description = "Color to apply to the selected atoms"

            # initialize set_color nodes
            # node Group Input
            group_input = set_color.nodes.new("NodeGroupInput")
            group_input.name = "Group Input"

            # node Store Named Attribute
            store_named_attribute = set_color.nodes.new(
                "GeometryNodeStoreNamedAttribute"
            )
            store_named_attribute.name = "Store Named Attribute"
            store_named_attribute.data_type = "FLOAT_COLOR"
            store_named_attribute.domain = "POINT"
            # Name
            store_named_attribute.inputs[2].default_value = "Color"

            # node Group Output
            group_output = set_color.nodes.new("NodeGroupOutput")
            group_output.name = "Group Output"
            group_output.is_active_output = True

            # Set locations
            group_input.location = (-460.0, -80.0)
            store_named_attribute.location = (-260.0, -20.0)
            group_output.location = (-100.0, -20.0)

            # initialize set_color links
            # store_named_attribute.Geometry -> group_output.Atoms
            set_color.links.new(
                store_named_attribute.outputs[0], group_output.inputs[0]
            )
            # group_input.Atoms -> store_named_attribute.Geometry
            set_color.links.new(group_input.outputs[0], store_named_attribute.inputs[0])
            # group_input.Selection -> store_named_attribute.Selection
            set_color.links.new(group_input.outputs[1], store_named_attribute.inputs[1])
            # group_input.Color -> store_named_attribute.Value
            set_color.links.new(group_input.outputs[2], store_named_attribute.inputs[3])
            return set_color

        set_color = set_color_node_group()

        # initialize _mn_world_scale node group
        def _mn_world_scale_node_group():
            _mn_world_scale = bpy.data.node_groups.new(
                type="GeometryNodeTree", name=".MN_world_scale"
            )

            _mn_world_scale.color_tag = "NONE"
            _mn_world_scale.description = ""

            # _mn_world_scale interface
            # Socket world_scale
            world_scale_socket = _mn_world_scale.interface.new_socket(
                name="world_scale", in_out="OUTPUT", socket_type="NodeSocketFloat"
            )
            world_scale_socket.subtype = "NONE"
            world_scale_socket.default_value = 0.009999999776482582
            world_scale_socket.min_value = -3.4028234663852886e38
            world_scale_socket.max_value = 3.4028234663852886e38
            world_scale_socket.attribute_domain = "POINT"

            # initialize _mn_world_scale nodes
            # node Group Input
            group_input_1 = _mn_world_scale.nodes.new("NodeGroupInput")
            group_input_1.name = "Group Input"

            # node Value
            value = _mn_world_scale.nodes.new("ShaderNodeValue")
            value.label = "world_scale"
            value.name = "Value"

            value.outputs[0].default_value = 0.009999999776482582
            # node Group Output
            group_output_1 = _mn_world_scale.nodes.new("NodeGroupOutput")
            group_output_1.name = "Group Output"
            group_output_1.is_active_output = True

            # Set locations
            group_input_1.location = (-200.0, 0.0)
            value.location = (0.0, 0.0)
            group_output_1.location = (190.0, 0.0)

            # initialize _mn_world_scale links
            # value.Value -> group_output_1.world_scale
            _mn_world_scale.links.new(value.outputs[0], group_output_1.inputs[0])
            return _mn_world_scale

        _mn_world_scale = _mn_world_scale_node_group()

        # initialize mn_units node group
        def mn_units_node_group():
            mn_units = bpy.data.node_groups.new(
                type="GeometryNodeTree", name="MN Units"
            )

            mn_units.color_tag = "NONE"
            mn_units.description = ""

            # mn_units interface
            # Socket Angstrom
            angstrom_socket = mn_units.interface.new_socket(
                name="Angstrom", in_out="OUTPUT", socket_type="NodeSocketFloat"
            )
            angstrom_socket.subtype = "NONE"
            angstrom_socket.default_value = 0.0
            angstrom_socket.min_value = -3.4028234663852886e38
            angstrom_socket.max_value = 3.4028234663852886e38
            angstrom_socket.attribute_domain = "POINT"

            # Socket Nanometre
            nanometre_socket = mn_units.interface.new_socket(
                name="Nanometre", in_out="OUTPUT", socket_type="NodeSocketFloat"
            )
            nanometre_socket.subtype = "NONE"
            nanometre_socket.default_value = 0.0
            nanometre_socket.min_value = -3.4028234663852886e38
            nanometre_socket.max_value = 3.4028234663852886e38
            nanometre_socket.attribute_domain = "POINT"

            # Socket Value
            value_socket = mn_units.interface.new_socket(
                name="Value", in_out="INPUT", socket_type="NodeSocketFloat"
            )
            value_socket.subtype = "NONE"
            value_socket.default_value = 3.0
            value_socket.min_value = -10000.0
            value_socket.max_value = 10000.0
            value_socket.attribute_domain = "POINT"
            value_socket.description = (
                "A value which will be scaled appropriately for the world"
            )

            # initialize mn_units nodes
            # node Group Output
            group_output_2 = mn_units.nodes.new("NodeGroupOutput")
            group_output_2.name = "Group Output"
            group_output_2.is_active_output = True

            # node Group Input
            group_input_2 = mn_units.nodes.new("NodeGroupInput")
            group_input_2.name = "Group Input"

            # node Math
            math = mn_units.nodes.new("ShaderNodeMath")
            math.name = "Math"
            math.operation = "MULTIPLY"
            math.use_clamp = False

            # node Math.001
            math_001 = mn_units.nodes.new("ShaderNodeMath")
            math_001.name = "Math.001"
            math_001.operation = "MULTIPLY"
            math_001.use_clamp = False
            # Value_001
            math_001.inputs[1].default_value = 10.0

            # node Group
            group = mn_units.nodes.new("GeometryNodeGroup")
            group.name = "Group"
            group.node_tree = _mn_world_scale

            # Set locations
            group_output_2.location = (190.0, 0.0)
            group_input_2.location = (-240.0, 0.0)
            math.location = (-60.0, 0.0)
            math_001.location = (-60.0, -160.0)
            group.location = (-304.00421142578125, -104.114013671875)

            # initialize mn_units links
            # math.Value -> group_output_2.Angstrom
            mn_units.links.new(math.outputs[0], group_output_2.inputs[0])
            # group_input_2.Value -> math.Value
            mn_units.links.new(group_input_2.outputs[0], math.inputs[0])
            # group.world_scale -> math.Value
            mn_units.links.new(group.outputs[0], math.inputs[1])
            # math.Value -> math_001.Value
            mn_units.links.new(math.outputs[0], math_001.inputs[0])
            # math_001.Value -> group_output_2.Nanometre
            mn_units.links.new(math_001.outputs[0], group_output_2.inputs[1])
            return mn_units

        mn_units = mn_units_node_group()

        # initialize _mn_utils_style_sticks node group
        def _mn_utils_style_sticks_node_group():
            _mn_utils_style_sticks = bpy.data.node_groups.new(
                type="GeometryNodeTree", name=".MN_utils_style_sticks"
            )

            _mn_utils_style_sticks.color_tag = "GEOMETRY"
            _mn_utils_style_sticks.description = ""

            _mn_utils_style_sticks.is_modifier = True

            # _mn_utils_style_sticks interface
            # Socket Geometry
            geometry_socket = _mn_utils_style_sticks.interface.new_socket(
                name="Geometry", in_out="OUTPUT", socket_type="NodeSocketGeometry"
            )
            geometry_socket.attribute_domain = "POINT"

            # Socket Atoms
            atoms_socket_2 = _mn_utils_style_sticks.interface.new_socket(
                name="Atoms", in_out="INPUT", socket_type="NodeSocketGeometry"
            )
            atoms_socket_2.attribute_domain = "POINT"
            atoms_socket_2.description = (
                "Atomic geometry that contains vertices and edges"
            )

            # Socket Selection
            selection_socket_1 = _mn_utils_style_sticks.interface.new_socket(
                name="Selection", in_out="INPUT", socket_type="NodeSocketBool"
            )
            selection_socket_1.attribute_domain = "POINT"
            selection_socket_1.hide_value = True
            selection_socket_1.description = "Selection of atoms to apply this node to"

            # Socket Radius
            radius_socket = _mn_utils_style_sticks.interface.new_socket(
                name="Radius", in_out="INPUT", socket_type="NodeSocketFloat"
            )
            radius_socket.subtype = "NONE"
            radius_socket.default_value = 0.30000001192092896
            radius_socket.min_value = 0.0
            radius_socket.max_value = 1.0
            radius_socket.attribute_domain = "POINT"
            radius_socket.description = "Radius of the bond mesh."

            # Socket Resolution
            resolution_socket = _mn_utils_style_sticks.interface.new_socket(
                name="Resolution", in_out="INPUT", socket_type="NodeSocketInt"
            )
            resolution_socket.subtype = "NONE"
            resolution_socket.default_value = 6
            resolution_socket.min_value = 3
            resolution_socket.max_value = 512
            resolution_socket.attribute_domain = "POINT"
            resolution_socket.description = "Resolution of the created bond cylinders."

            # Socket Fill Caps
            fill_caps_socket = _mn_utils_style_sticks.interface.new_socket(
                name="Fill Caps", in_out="INPUT", socket_type="NodeSocketBool"
            )
            fill_caps_socket.attribute_domain = "POINT"
            fill_caps_socket.description = "Fill the caps at each end of the bonds."

            # Socket Interpolate Color
            interpolate_color_socket = _mn_utils_style_sticks.interface.new_socket(
                name="Interpolate Color", in_out="INPUT", socket_type="NodeSocketBool"
            )
            interpolate_color_socket.attribute_domain = "POINT"

            # Panel Material
            material_panel = _mn_utils_style_sticks.interface.new_panel("Material")
            # Socket Shade Smooth
            shade_smooth_socket = _mn_utils_style_sticks.interface.new_socket(
                name="Shade Smooth",
                in_out="INPUT",
                socket_type="NodeSocketBool",
                parent=material_panel,
            )
            shade_smooth_socket.attribute_domain = "POINT"
            shade_smooth_socket.description = (
                "Apply smooth shading to the created geometry"
            )

            # Socket Material
            material_socket = _mn_utils_style_sticks.interface.new_socket(
                name="Material",
                in_out="INPUT",
                socket_type="NodeSocketMaterial",
                parent=material_panel,
            )
            material_socket.attribute_domain = "POINT"
            material_socket.description = "Material to apply to the resulting geometry"

            # initialize _mn_utils_style_sticks nodes
            # node Frame
            frame = _mn_utils_style_sticks.nodes.new("NodeFrame")
            frame.label = "Bonds to Mesh"
            frame.name = "Frame"
            frame.label_size = 20
            frame.shrink = True

            # node Frame.001
            frame_001 = _mn_utils_style_sticks.nodes.new("NodeFrame")
            frame_001.label = "Capture index for pulling colors from atoms"
            frame_001.name = "Frame.001"
            frame_001.label_size = 20
            frame_001.shrink = True

            # node Frame.003
            frame_003 = _mn_utils_style_sticks.nodes.new("NodeFrame")
            frame_003.label = "Set up materials"
            frame_003.name = "Frame.003"
            frame_003.label_size = 20
            frame_003.shrink = True

            # node Frame.002
            frame_002 = _mn_utils_style_sticks.nodes.new("NodeFrame")
            frame_002.label = "Store correct color on the new bond mesh"
            frame_002.name = "Frame.002"
            frame_002.label_size = 20
            frame_002.shrink = True

            # node Mesh to Curve
            mesh_to_curve = _mn_utils_style_sticks.nodes.new("GeometryNodeMeshToCurve")
            mesh_to_curve.name = "Mesh to Curve"
            # Selection
            mesh_to_curve.inputs[1].default_value = True

            # node Set Curve Radius
            set_curve_radius = _mn_utils_style_sticks.nodes.new(
                "GeometryNodeSetCurveRadius"
            )
            set_curve_radius.name = "Set Curve Radius"
            # Selection
            set_curve_radius.inputs[1].default_value = True

            # node Subdivide Curve
            subdivide_curve = _mn_utils_style_sticks.nodes.new(
                "GeometryNodeSubdivideCurve"
            )
            subdivide_curve.name = "Subdivide Curve"
            # Cuts
            subdivide_curve.inputs[1].default_value = 1

            # node Group
            group_1 = _mn_utils_style_sticks.nodes.new("GeometryNodeGroup")
            group_1.name = "Group"
            group_1.node_tree = mn_units

            # node Group Input.002
            group_input_002 = _mn_utils_style_sticks.nodes.new("NodeGroupInput")
            group_input_002.name = "Group Input.002"
            group_input_002.outputs[0].hide = True
            group_input_002.outputs[3].hide = True
            group_input_002.outputs[5].hide = True
            group_input_002.outputs[6].hide = True
            group_input_002.outputs[7].hide = True
            group_input_002.outputs[8].hide = True

            # node Curve Circle
            curve_circle = _mn_utils_style_sticks.nodes.new(
                "GeometryNodeCurvePrimitiveCircle"
            )
            curve_circle.name = "Curve Circle"
            curve_circle.mode = "RADIUS"
            # Radius
            curve_circle.inputs[4].default_value = 1.0

            # node Curve to Mesh
            curve_to_mesh = _mn_utils_style_sticks.nodes.new("GeometryNodeCurveToMesh")
            curve_to_mesh.name = "Curve to Mesh"

            # node Group Input.001
            group_input_001 = _mn_utils_style_sticks.nodes.new("NodeGroupInput")
            group_input_001.name = "Group Input.001"
            group_input_001.outputs[0].hide = True
            group_input_001.outputs[2].hide = True
            group_input_001.outputs[4].hide = True
            group_input_001.outputs[5].hide = True
            group_input_001.outputs[6].hide = True
            group_input_001.outputs[7].hide = True
            group_input_001.outputs[8].hide = True

            # node Duplicate Elements
            duplicate_elements = _mn_utils_style_sticks.nodes.new(
                "GeometryNodeDuplicateElements"
            )
            duplicate_elements.name = "Duplicate Elements"
            duplicate_elements.domain = "EDGE"
            # Selection
            duplicate_elements.inputs[1].default_value = True
            # Amount
            duplicate_elements.inputs[2].default_value = 1

            # node Mesh Island.001
            mesh_island_001 = _mn_utils_style_sticks.nodes.new(
                "GeometryNodeInputMeshIsland"
            )
            mesh_island_001.name = "Mesh Island.001"

            # node Accumulate Field.001
            accumulate_field_001 = _mn_utils_style_sticks.nodes.new(
                "GeometryNodeAccumulateField"
            )
            accumulate_field_001.name = "Accumulate Field.001"
            accumulate_field_001.data_type = "INT"
            accumulate_field_001.domain = "POINT"
            # Value
            accumulate_field_001.inputs[0].default_value = 1

            # node Capture Attribute
            capture_attribute = _mn_utils_style_sticks.nodes.new(
                "GeometryNodeCaptureAttribute"
            )
            capture_attribute.name = "Capture Attribute"
            capture_attribute.active_index = 0
            capture_attribute.capture_items.clear()
            capture_attribute.capture_items.new("FLOAT", "Value")
            capture_attribute.capture_items["Value"].data_type = "BOOLEAN"
            capture_attribute.domain = "POINT"

            # node Capture Attribute.003
            capture_attribute_003 = _mn_utils_style_sticks.nodes.new(
                "GeometryNodeCaptureAttribute"
            )
            capture_attribute_003.name = "Capture Attribute.003"
            capture_attribute_003.active_index = 0
            capture_attribute_003.capture_items.clear()
            capture_attribute_003.capture_items.new("FLOAT", "Vertex Index 1")
            capture_attribute_003.capture_items["Vertex Index 1"].data_type = "INT"
            capture_attribute_003.capture_items.new("FLOAT", "Vertex Index 2")
            capture_attribute_003.capture_items["Vertex Index 2"].data_type = "INT"
            capture_attribute_003.domain = "EDGE"

            # node Edge Vertices
            edge_vertices = _mn_utils_style_sticks.nodes.new(
                "GeometryNodeInputMeshEdgeVertices"
            )
            edge_vertices.name = "Edge Vertices"

            # node Group Input.003
            group_input_003 = _mn_utils_style_sticks.nodes.new("NodeGroupInput")
            group_input_003.name = "Group Input.003"
            group_input_003.outputs[0].hide = True
            group_input_003.outputs[2].hide = True
            group_input_003.outputs[3].hide = True
            group_input_003.outputs[4].hide = True
            group_input_003.outputs[5].hide = True
            group_input_003.outputs[6].hide = True
            group_input_003.outputs[8].hide = True

            # node Set Material
            set_material = _mn_utils_style_sticks.nodes.new("GeometryNodeSetMaterial")
            set_material.name = "Set Material"
            # Selection
            set_material.inputs[1].default_value = True

            # node Set Shade Smooth
            set_shade_smooth = _mn_utils_style_sticks.nodes.new(
                "GeometryNodeSetShadeSmooth"
            )
            set_shade_smooth.name = "Set Shade Smooth"
            set_shade_smooth.domain = "FACE"
            # Selection
            set_shade_smooth.inputs[1].default_value = True

            # node Group Input.004
            group_input_004 = _mn_utils_style_sticks.nodes.new("NodeGroupInput")
            group_input_004.name = "Group Input.004"
            group_input_004.outputs[0].hide = True
            group_input_004.outputs[2].hide = True
            group_input_004.outputs[3].hide = True
            group_input_004.outputs[4].hide = True
            group_input_004.outputs[5].hide = True
            group_input_004.outputs[7].hide = True
            group_input_004.outputs[8].hide = True

            # node Group Output
            group_output_3 = _mn_utils_style_sticks.nodes.new("NodeGroupOutput")
            group_output_3.name = "Group Output"
            group_output_3.is_active_output = True

            # node Capture Attribute.001
            capture_attribute_001 = _mn_utils_style_sticks.nodes.new(
                "GeometryNodeCaptureAttribute"
            )
            capture_attribute_001.name = "Capture Attribute.001"
            capture_attribute_001.active_index = 0
            capture_attribute_001.capture_items.clear()
            capture_attribute_001.capture_items.new("FLOAT", "Value")
            capture_attribute_001.capture_items["Value"].data_type = "BOOLEAN"
            capture_attribute_001.domain = "FACE"

            # node Sample Index.001
            sample_index_001 = _mn_utils_style_sticks.nodes.new(
                "GeometryNodeSampleIndex"
            )
            sample_index_001.name = "Sample Index.001"
            sample_index_001.hide = True
            sample_index_001.clamp = False
            sample_index_001.data_type = "FLOAT_COLOR"
            sample_index_001.domain = "POINT"

            # node Evaluate on Domain.003
            evaluate_on_domain_003 = _mn_utils_style_sticks.nodes.new(
                "GeometryNodeFieldOnDomain"
            )
            evaluate_on_domain_003.name = "Evaluate on Domain.003"
            evaluate_on_domain_003.hide = True
            evaluate_on_domain_003.data_type = "FLOAT_COLOR"
            evaluate_on_domain_003.domain = "FACE"

            # node Named Attribute.002
            named_attribute_002 = _mn_utils_style_sticks.nodes.new(
                "GeometryNodeInputNamedAttribute"
            )
            named_attribute_002.name = "Named Attribute.002"
            named_attribute_002.hide = True
            named_attribute_002.data_type = "FLOAT_COLOR"
            # Name
            named_attribute_002.inputs[0].default_value = "Color"

            # node Switch.001
            switch_001 = _mn_utils_style_sticks.nodes.new("GeometryNodeSwitch")
            switch_001.name = "Switch.001"
            switch_001.hide = True
            switch_001.input_type = "INT"

            # node Evaluate on Domain
            evaluate_on_domain = _mn_utils_style_sticks.nodes.new(
                "GeometryNodeFieldOnDomain"
            )
            evaluate_on_domain.name = "Evaluate on Domain"
            evaluate_on_domain.hide = True
            evaluate_on_domain.data_type = "FLOAT_COLOR"
            evaluate_on_domain.domain = "POINT"

            # node Switch
            switch = _mn_utils_style_sticks.nodes.new("GeometryNodeSwitch")
            switch.name = "Switch"
            switch.input_type = "RGBA"

            # node Group Input.005
            group_input_005 = _mn_utils_style_sticks.nodes.new("NodeGroupInput")
            group_input_005.name = "Group Input.005"
            group_input_005.outputs[0].hide = True
            group_input_005.outputs[2].hide = True
            group_input_005.outputs[3].hide = True
            group_input_005.outputs[4].hide = True
            group_input_005.outputs[6].hide = True
            group_input_005.outputs[7].hide = True
            group_input_005.outputs[8].hide = True

            # node Store Named Attribute
            store_named_attribute_1 = _mn_utils_style_sticks.nodes.new(
                "GeometryNodeStoreNamedAttribute"
            )
            store_named_attribute_1.name = "Store Named Attribute"
            store_named_attribute_1.data_type = "FLOAT_COLOR"
            store_named_attribute_1.domain = "CORNER"
            # Selection
            store_named_attribute_1.inputs[1].default_value = True
            # Name
            store_named_attribute_1.inputs[2].default_value = "Color"

            # node Group Input
            group_input_3 = _mn_utils_style_sticks.nodes.new("NodeGroupInput")
            group_input_3.name = "Group Input"

            # node Separate Geometry
            separate_geometry = _mn_utils_style_sticks.nodes.new(
                "GeometryNodeSeparateGeometry"
            )
            separate_geometry.name = "Separate Geometry"
            separate_geometry.domain = "POINT"

            # Set parents
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
            store_named_attribute_1.parent = frame_002

            # Set locations
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
            store_named_attribute_1.location = (-120.0, 120.0)
            group_input_3.location = (-2680.0, 240.0)
            separate_geometry.location = (-2460.0, 240.0)

            # initialize _mn_utils_style_sticks links
            # capture_attribute.Geometry -> mesh_to_curve.Mesh
            _mn_utils_style_sticks.links.new(
                capture_attribute.outputs[0], mesh_to_curve.inputs[0]
            )
            # set_shade_smooth.Geometry -> group_output_3.Geometry
            _mn_utils_style_sticks.links.new(
                set_shade_smooth.outputs[0], group_output_3.inputs[0]
            )
            # curve_circle.Curve -> curve_to_mesh.Profile Curve
            _mn_utils_style_sticks.links.new(
                curve_circle.outputs[0], curve_to_mesh.inputs[1]
            )
            # mesh_to_curve.Curve -> set_curve_radius.Curve
            _mn_utils_style_sticks.links.new(
                mesh_to_curve.outputs[0], set_curve_radius.inputs[0]
            )
            # group_1.Angstrom -> set_curve_radius.Radius
            _mn_utils_style_sticks.links.new(
                group_1.outputs[0], set_curve_radius.inputs[2]
            )
            # set_curve_radius.Curve -> subdivide_curve.Curve
            _mn_utils_style_sticks.links.new(
                set_curve_radius.outputs[0], subdivide_curve.inputs[0]
            )
            # capture_attribute_003.Geometry -> duplicate_elements.Geometry
            _mn_utils_style_sticks.links.new(
                capture_attribute_003.outputs[0], duplicate_elements.inputs[0]
            )
            # group_input_001.Resolution -> curve_circle.Resolution
            _mn_utils_style_sticks.links.new(
                group_input_001.outputs[3], curve_circle.inputs[0]
            )
            # group_input_003.Material -> set_material.Material
            _mn_utils_style_sticks.links.new(
                group_input_003.outputs[7], set_material.inputs[2]
            )
            # set_material.Geometry -> set_shade_smooth.Geometry
            _mn_utils_style_sticks.links.new(
                set_material.outputs[0], set_shade_smooth.inputs[0]
            )
            # group_input_004.Shade Smooth -> set_shade_smooth.Shade Smooth
            _mn_utils_style_sticks.links.new(
                group_input_004.outputs[6], set_shade_smooth.inputs[2]
            )
            # capture_attribute_003.Geometry -> sample_index_001.Geometry
            _mn_utils_style_sticks.links.new(
                capture_attribute_003.outputs[0], sample_index_001.inputs[0]
            )
            # named_attribute_002.Attribute -> sample_index_001.Value
            _mn_utils_style_sticks.links.new(
                named_attribute_002.outputs[0], sample_index_001.inputs[1]
            )
            # subdivide_curve.Curve -> curve_to_mesh.Curve
            _mn_utils_style_sticks.links.new(
                subdivide_curve.outputs[0], curve_to_mesh.inputs[0]
            )
            # switch_001.Output -> sample_index_001.Index
            _mn_utils_style_sticks.links.new(
                switch_001.outputs[0], sample_index_001.inputs[2]
            )
            # capture_attribute_001.Geometry -> store_named_attribute_1.Geometry
            _mn_utils_style_sticks.links.new(
                capture_attribute_001.outputs[0], store_named_attribute_1.inputs[0]
            )
            # capture_attribute_003.Vertex Index 1 -> switch_001.False
            _mn_utils_style_sticks.links.new(
                capture_attribute_003.outputs[1], switch_001.inputs[1]
            )
            # duplicate_elements.Geometry -> capture_attribute.Geometry
            _mn_utils_style_sticks.links.new(
                duplicate_elements.outputs[0], capture_attribute.inputs[0]
            )
            # accumulate_field_001.Trailing -> capture_attribute.Value
            _mn_utils_style_sticks.links.new(
                accumulate_field_001.outputs[1], capture_attribute.inputs[1]
            )
            # mesh_island_001.Island Index -> accumulate_field_001.Group ID
            _mn_utils_style_sticks.links.new(
                mesh_island_001.outputs[0], accumulate_field_001.inputs[1]
            )
            # capture_attribute_003.Vertex Index 2 -> switch_001.True
            _mn_utils_style_sticks.links.new(
                capture_attribute_003.outputs[2], switch_001.inputs[2]
            )
            # curve_to_mesh.Mesh -> capture_attribute_001.Geometry
            _mn_utils_style_sticks.links.new(
                curve_to_mesh.outputs[0], capture_attribute_001.inputs[0]
            )
            # capture_attribute_001.Value -> switch_001.Switch
            _mn_utils_style_sticks.links.new(
                capture_attribute_001.outputs[1], switch_001.inputs[0]
            )
            # capture_attribute.Value -> capture_attribute_001.Value
            _mn_utils_style_sticks.links.new(
                capture_attribute.outputs[1], capture_attribute_001.inputs[1]
            )
            # sample_index_001.Value -> evaluate_on_domain_003.Value
            _mn_utils_style_sticks.links.new(
                sample_index_001.outputs[0], evaluate_on_domain_003.inputs[0]
            )
            # store_named_attribute_1.Geometry -> set_material.Geometry
            _mn_utils_style_sticks.links.new(
                store_named_attribute_1.outputs[0], set_material.inputs[0]
            )
            # group_input_002.Radius -> group_1.Value
            _mn_utils_style_sticks.links.new(
                group_input_002.outputs[2], group_1.inputs[0]
            )
            # group_input_002.Fill Caps -> curve_to_mesh.Fill Caps
            _mn_utils_style_sticks.links.new(
                group_input_002.outputs[4], curve_to_mesh.inputs[2]
            )
            # evaluate_on_domain_003.Value -> evaluate_on_domain.Value
            _mn_utils_style_sticks.links.new(
                evaluate_on_domain_003.outputs[0], evaluate_on_domain.inputs[0]
            )
            # evaluate_on_domain.Value -> switch.True
            _mn_utils_style_sticks.links.new(
                evaluate_on_domain.outputs[0], switch.inputs[2]
            )
            # switch.Output -> store_named_attribute_1.Value
            _mn_utils_style_sticks.links.new(
                switch.outputs[0], store_named_attribute_1.inputs[3]
            )
            # evaluate_on_domain_003.Value -> switch.False
            _mn_utils_style_sticks.links.new(
                evaluate_on_domain_003.outputs[0], switch.inputs[1]
            )
            # group_input_005.Interpolate Color -> switch.Switch
            _mn_utils_style_sticks.links.new(
                group_input_005.outputs[5], switch.inputs[0]
            )
            # group_input_3.Atoms -> separate_geometry.Geometry
            _mn_utils_style_sticks.links.new(
                group_input_3.outputs[0], separate_geometry.inputs[0]
            )
            # separate_geometry.Selection -> capture_attribute_003.Geometry
            _mn_utils_style_sticks.links.new(
                separate_geometry.outputs[0], capture_attribute_003.inputs[0]
            )
            # group_input_3.Selection -> separate_geometry.Selection
            _mn_utils_style_sticks.links.new(
                group_input_3.outputs[1], separate_geometry.inputs[1]
            )
            # edge_vertices.Vertex Index 2 -> capture_attribute_003.Vertex Index 2
            _mn_utils_style_sticks.links.new(
                edge_vertices.outputs[1], capture_attribute_003.inputs[2]
            )
            # edge_vertices.Vertex Index 1 -> capture_attribute_003.Vertex Index 1
            _mn_utils_style_sticks.links.new(
                edge_vertices.outputs[0], capture_attribute_003.inputs[1]
            )
            return _mn_utils_style_sticks

        _mn_utils_style_sticks = _mn_utils_style_sticks_node_group()

        # initialize topology_find_bonds node group
        def topology_find_bonds_node_group():
            topology_find_bonds = bpy.data.node_groups.new(
                type="GeometryNodeTree", name="Topology Find Bonds"
            )

            topology_find_bonds.color_tag = "GEOMETRY"
            topology_find_bonds.description = ""

            topology_find_bonds.is_modifier = True

            # topology_find_bonds interface
            # Socket Atoms
            atoms_socket_3 = topology_find_bonds.interface.new_socket(
                name="Atoms", in_out="OUTPUT", socket_type="NodeSocketGeometry"
            )
            atoms_socket_3.attribute_domain = "POINT"

            # Socket Atoms
            atoms_socket_4 = topology_find_bonds.interface.new_socket(
                name="Atoms", in_out="INPUT", socket_type="NodeSocketGeometry"
            )
            atoms_socket_4.attribute_domain = "POINT"
            atoms_socket_4.description = (
                "Atomic geometry that contains vertices and edges"
            )

            # Socket Selection
            selection_socket_2 = topology_find_bonds.interface.new_socket(
                name="Selection", in_out="INPUT", socket_type="NodeSocketBool"
            )
            selection_socket_2.attribute_domain = "POINT"
            selection_socket_2.hide_value = True
            selection_socket_2.description = "Selection of atoms to apply this node to"

            # Socket Scale
            scale_socket = topology_find_bonds.interface.new_socket(
                name="Scale", in_out="INPUT", socket_type="NodeSocketFloat"
            )
            scale_socket.subtype = "NONE"
            scale_socket.default_value = 1.0
            scale_socket.min_value = 0.0
            scale_socket.max_value = 10000.0
            scale_socket.attribute_domain = "POINT"
            scale_socket.description = (
                "Scale the VDW radii of the atoms when searching for bonds"
            )

            # initialize topology_find_bonds nodes
            # node Frame
            frame_1 = topology_find_bonds.nodes.new("NodeFrame")
            frame_1.label = "Create Distance Probe"
            frame_1.name = "Frame"
            frame_1.label_size = 20
            frame_1.shrink = True

            # node Sample Nearest
            sample_nearest = topology_find_bonds.nodes.new("GeometryNodeSampleNearest")
            sample_nearest.name = "Sample Nearest"
            sample_nearest.domain = "POINT"
            # Sample Position
            sample_nearest.inputs[1].default_value = (0.0, 0.0, 0.0)

            # node Sample Index.001
            sample_index_001_1 = topology_find_bonds.nodes.new(
                "GeometryNodeSampleIndex"
            )
            sample_index_001_1.name = "Sample Index.001"
            sample_index_001_1.clamp = False
            sample_index_001_1.data_type = "FLOAT_VECTOR"
            sample_index_001_1.domain = "POINT"

            # node Math
            math_1 = topology_find_bonds.nodes.new("ShaderNodeMath")
            math_1.name = "Math"
            math_1.hide = True
            math_1.operation = "MULTIPLY"
            math_1.use_clamp = False
            math_1.inputs[2].hide = True

            # node Group Input.001
            group_input_001_1 = topology_find_bonds.nodes.new("NodeGroupInput")
            group_input_001_1.name = "Group Input.001"
            group_input_001_1.outputs[0].hide = True
            group_input_001_1.outputs[1].hide = True
            group_input_001_1.outputs[3].hide = True

            # node Sample Index
            sample_index = topology_find_bonds.nodes.new("GeometryNodeSampleIndex")
            sample_index.name = "Sample Index"
            sample_index.clamp = False
            sample_index.data_type = "FLOAT_VECTOR"
            sample_index.domain = "POINT"

            # node Vector Math
            vector_math = topology_find_bonds.nodes.new("ShaderNodeVectorMath")
            vector_math.name = "Vector Math"
            vector_math.operation = "SCALE"
            # Scale
            vector_math.inputs[3].default_value = -1.0

            # node Position
            position = topology_find_bonds.nodes.new("GeometryNodeInputPosition")
            position.name = "Position"

            # node Ico Sphere
            ico_sphere = topology_find_bonds.nodes.new("GeometryNodeMeshIcoSphere")
            ico_sphere.name = "Ico Sphere"
            # Radius
            ico_sphere.inputs[0].default_value = 1.0
            # Subdivisions
            ico_sphere.inputs[1].default_value = 1

            # node Index
            index = topology_find_bonds.nodes.new("GeometryNodeInputIndex")
            index.name = "Index"

            # node Mesh Line
            mesh_line = topology_find_bonds.nodes.new("GeometryNodeMeshLine")
            mesh_line.name = "Mesh Line"
            mesh_line.hide = True
            mesh_line.count_mode = "TOTAL"
            mesh_line.mode = "OFFSET"
            # Count
            mesh_line.inputs[0].default_value = 2
            # Start Location
            mesh_line.inputs[2].default_value = (0.0, 0.0, 0.0)
            # Offset
            mesh_line.inputs[3].default_value = (0.0, 0.0, 1.0)

            # node Instance on Points
            instance_on_points = topology_find_bonds.nodes.new(
                "GeometryNodeInstanceOnPoints"
            )
            instance_on_points.name = "Instance on Points"
            # Selection
            instance_on_points.inputs[1].default_value = True
            # Pick Instance
            instance_on_points.inputs[3].default_value = False
            # Instance Index
            instance_on_points.inputs[4].default_value = 0
            # Scale
            instance_on_points.inputs[6].default_value = (1.0, 1.0, 1.0)

            # node Named Attribute
            named_attribute = topology_find_bonds.nodes.new(
                "GeometryNodeInputNamedAttribute"
            )
            named_attribute.name = "Named Attribute"
            named_attribute.data_type = "INT"
            # Name
            named_attribute.inputs[0].default_value = "atomic_number"

            # node Sample Index.006
            sample_index_006 = topology_find_bonds.nodes.new("GeometryNodeSampleIndex")
            sample_index_006.name = "Sample Index.006"
            sample_index_006.clamp = False
            sample_index_006.data_type = "INT"
            sample_index_006.domain = "POINT"

            # node Named Attribute.002
            named_attribute_002_1 = topology_find_bonds.nodes.new(
                "GeometryNodeInputNamedAttribute"
            )
            named_attribute_002_1.name = "Named Attribute.002"
            named_attribute_002_1.data_type = "INT"
            # Name
            named_attribute_002_1.inputs[0].default_value = "res_name"

            # node Sample Index.007
            sample_index_007 = topology_find_bonds.nodes.new("GeometryNodeSampleIndex")
            sample_index_007.name = "Sample Index.007"
            sample_index_007.clamp = False
            sample_index_007.data_type = "INT"
            sample_index_007.domain = "POINT"

            # node Named Attribute.003
            named_attribute_003 = topology_find_bonds.nodes.new(
                "GeometryNodeInputNamedAttribute"
            )
            named_attribute_003.name = "Named Attribute.003"
            named_attribute_003.data_type = "INT"
            # Name
            named_attribute_003.inputs[0].default_value = "chain_id"

            # node Sample Index.008
            sample_index_008 = topology_find_bonds.nodes.new("GeometryNodeSampleIndex")
            sample_index_008.name = "Sample Index.008"
            sample_index_008.clamp = False
            sample_index_008.data_type = "INT"
            sample_index_008.domain = "POINT"

            # node Named Attribute.004
            named_attribute_004 = topology_find_bonds.nodes.new(
                "GeometryNodeInputNamedAttribute"
            )
            named_attribute_004.name = "Named Attribute.004"
            named_attribute_004.data_type = "INT"
            # Name
            named_attribute_004.inputs[0].default_value = "res_id"

            # node Sample Index.005
            sample_index_005 = topology_find_bonds.nodes.new("GeometryNodeSampleIndex")
            sample_index_005.name = "Sample Index.005"
            sample_index_005.clamp = False
            sample_index_005.data_type = "INT"
            sample_index_005.domain = "POINT"

            # node Reroute.002
            reroute_002 = topology_find_bonds.nodes.new("NodeReroute")
            reroute_002.name = "Reroute.002"
            # node Sample Index.009
            sample_index_009 = topology_find_bonds.nodes.new("GeometryNodeSampleIndex")
            sample_index_009.name = "Sample Index.009"
            sample_index_009.clamp = False
            sample_index_009.data_type = "FLOAT"
            sample_index_009.domain = "POINT"

            # node Named Attribute.005
            named_attribute_005 = topology_find_bonds.nodes.new(
                "GeometryNodeInputNamedAttribute"
            )
            named_attribute_005.name = "Named Attribute.005"
            named_attribute_005.data_type = "FLOAT"
            # Name
            named_attribute_005.inputs[0].default_value = "vdw_radii"

            # node Realize Instances
            realize_instances = topology_find_bonds.nodes.new(
                "GeometryNodeRealizeInstances"
            )
            realize_instances.name = "Realize Instances"
            # Selection
            realize_instances.inputs[1].default_value = True
            # Realize All
            realize_instances.inputs[2].default_value = True
            # Depth
            realize_instances.inputs[3].default_value = 0

            # node Instance on Points.001
            instance_on_points_001 = topology_find_bonds.nodes.new(
                "GeometryNodeInstanceOnPoints"
            )
            instance_on_points_001.name = "Instance on Points.001"
            # Selection
            instance_on_points_001.inputs[1].default_value = True
            # Pick Instance
            instance_on_points_001.inputs[3].default_value = False
            # Instance Index
            instance_on_points_001.inputs[4].default_value = 0
            # Rotation
            instance_on_points_001.inputs[5].default_value = (0.0, 0.0, 0.0)

            # node Realize Instances.001
            realize_instances_001 = topology_find_bonds.nodes.new(
                "GeometryNodeRealizeInstances"
            )
            realize_instances_001.name = "Realize Instances.001"
            # Selection
            realize_instances_001.inputs[1].default_value = True
            # Realize All
            realize_instances_001.inputs[2].default_value = True
            # Depth
            realize_instances_001.inputs[3].default_value = 0

            # node Set Position
            set_position = topology_find_bonds.nodes.new("GeometryNodeSetPosition")
            set_position.name = "Set Position"
            # Selection
            set_position.inputs[1].default_value = True
            # Offset
            set_position.inputs[3].default_value = (0.0, 0.0, 0.0)

            # node Position.001
            position_001 = topology_find_bonds.nodes.new("GeometryNodeInputPosition")
            position_001.name = "Position.001"

            # node Store Named Attribute.001
            store_named_attribute_001 = topology_find_bonds.nodes.new(
                "GeometryNodeStoreNamedAttribute"
            )
            store_named_attribute_001.name = "Store Named Attribute.001"
            store_named_attribute_001.data_type = "INT"
            store_named_attribute_001.domain = "POINT"
            # Selection
            store_named_attribute_001.inputs[1].default_value = True
            # Name
            store_named_attribute_001.inputs[2].default_value = "res_name"

            # node Store Named Attribute.002
            store_named_attribute_002 = topology_find_bonds.nodes.new(
                "GeometryNodeStoreNamedAttribute"
            )
            store_named_attribute_002.name = "Store Named Attribute.002"
            store_named_attribute_002.data_type = "INT"
            store_named_attribute_002.domain = "POINT"
            # Selection
            store_named_attribute_002.inputs[1].default_value = True
            # Name
            store_named_attribute_002.inputs[2].default_value = "chain_id"

            # node Store Named Attribute.003
            store_named_attribute_003 = topology_find_bonds.nodes.new(
                "GeometryNodeStoreNamedAttribute"
            )
            store_named_attribute_003.name = "Store Named Attribute.003"
            store_named_attribute_003.data_type = "INT"
            store_named_attribute_003.domain = "POINT"
            # Selection
            store_named_attribute_003.inputs[1].default_value = True
            # Name
            store_named_attribute_003.inputs[2].default_value = "res_id"

            # node Store Named Attribute
            store_named_attribute_2 = topology_find_bonds.nodes.new(
                "GeometryNodeStoreNamedAttribute"
            )
            store_named_attribute_2.name = "Store Named Attribute"
            store_named_attribute_2.data_type = "INT"
            store_named_attribute_2.domain = "POINT"
            # Selection
            store_named_attribute_2.inputs[1].default_value = True
            # Name
            store_named_attribute_2.inputs[2].default_value = "atomic_number"

            # node Index.002
            index_002 = topology_find_bonds.nodes.new("GeometryNodeInputIndex")
            index_002.name = "Index.002"

            # node Named Attribute.006
            named_attribute_006 = topology_find_bonds.nodes.new(
                "GeometryNodeInputNamedAttribute"
            )
            named_attribute_006.name = "Named Attribute.006"
            named_attribute_006.data_type = "INT"
            # Name
            named_attribute_006.inputs[0].default_value = "pre_bond_index"

            # node Merge by Distance
            merge_by_distance = topology_find_bonds.nodes.new(
                "GeometryNodeMergeByDistance"
            )
            merge_by_distance.name = "Merge by Distance"
            merge_by_distance.mode = "ALL"
            # Selection
            merge_by_distance.inputs[1].default_value = True
            # Distance
            merge_by_distance.inputs[2].default_value = 0.0010000000474974513

            # node Group Output
            group_output_4 = topology_find_bonds.nodes.new("NodeGroupOutput")
            group_output_4.name = "Group Output"
            group_output_4.is_active_output = True

            # node Sample Index.011
            sample_index_011 = topology_find_bonds.nodes.new("GeometryNodeSampleIndex")
            sample_index_011.name = "Sample Index.011"
            sample_index_011.clamp = False
            sample_index_011.data_type = "FLOAT_VECTOR"
            sample_index_011.domain = "POINT"

            # node Sample Nearest.001
            sample_nearest_001 = topology_find_bonds.nodes.new(
                "GeometryNodeSampleNearest"
            )
            sample_nearest_001.name = "Sample Nearest.001"
            sample_nearest_001.domain = "POINT"
            # Sample Position
            sample_nearest_001.inputs[1].default_value = (0.0, 0.0, 0.0)

            # node Set Position.002
            set_position_002 = topology_find_bonds.nodes.new("GeometryNodeSetPosition")
            set_position_002.name = "Set Position.002"
            # Selection
            set_position_002.inputs[1].default_value = True
            # Offset
            set_position_002.inputs[3].default_value = (0.0, 0.0, 0.0)

            # node Store Named Attribute.004
            store_named_attribute_004 = topology_find_bonds.nodes.new(
                "GeometryNodeStoreNamedAttribute"
            )
            store_named_attribute_004.name = "Store Named Attribute.004"
            store_named_attribute_004.data_type = "FLOAT"
            store_named_attribute_004.domain = "POINT"
            # Selection
            store_named_attribute_004.inputs[1].default_value = True
            # Name
            store_named_attribute_004.inputs[2].default_value = "vdw_radii"

            # node Store Named Attribute.006
            store_named_attribute_006 = topology_find_bonds.nodes.new(
                "GeometryNodeStoreNamedAttribute"
            )
            store_named_attribute_006.name = "Store Named Attribute.006"
            store_named_attribute_006.data_type = "FLOAT_COLOR"
            store_named_attribute_006.domain = "POINT"
            # Selection
            store_named_attribute_006.inputs[1].default_value = True
            # Name
            store_named_attribute_006.inputs[2].default_value = "Color"

            # node Store Named Attribute.005
            store_named_attribute_005 = topology_find_bonds.nodes.new(
                "GeometryNodeStoreNamedAttribute"
            )
            store_named_attribute_005.name = "Store Named Attribute.005"
            store_named_attribute_005.data_type = "INT"
            store_named_attribute_005.domain = "POINT"
            # Selection
            store_named_attribute_005.inputs[1].default_value = True
            # Name
            store_named_attribute_005.inputs[2].default_value = "pre_bond_index"

            # node Sample Index.012
            sample_index_012 = topology_find_bonds.nodes.new("GeometryNodeSampleIndex")
            sample_index_012.name = "Sample Index.012"
            sample_index_012.clamp = False
            sample_index_012.data_type = "FLOAT_COLOR"
            sample_index_012.domain = "POINT"

            # node Named Attribute.007
            named_attribute_007 = topology_find_bonds.nodes.new(
                "GeometryNodeInputNamedAttribute"
            )
            named_attribute_007.name = "Named Attribute.007"
            named_attribute_007.data_type = "FLOAT_COLOR"
            # Name
            named_attribute_007.inputs[0].default_value = "Color"

            # node Math.001
            math_001_1 = topology_find_bonds.nodes.new("ShaderNodeMath")
            math_001_1.label = "x * 0.62"
            math_001_1.name = "Math.001"
            math_001_1.operation = "MULTIPLY"
            math_001_1.use_clamp = False
            # Value_001
            math_001_1.inputs[1].default_value = 0.6200000047683716

            # node Group Input
            group_input_4 = topology_find_bonds.nodes.new("NodeGroupInput")
            group_input_4.name = "Group Input"

            # node Separate Geometry
            separate_geometry_1 = topology_find_bonds.nodes.new(
                "GeometryNodeSeparateGeometry"
            )
            separate_geometry_1.name = "Separate Geometry"
            separate_geometry_1.domain = "POINT"

            # node Position.002
            position_002 = topology_find_bonds.nodes.new("GeometryNodeInputPosition")
            position_002.name = "Position.002"

            # node Sample Index.010
            sample_index_010 = topology_find_bonds.nodes.new("GeometryNodeSampleIndex")
            sample_index_010.name = "Sample Index.010"
            sample_index_010.clamp = False
            sample_index_010.data_type = "INT"
            sample_index_010.domain = "POINT"

            # node Sample Index.002
            sample_index_002 = topology_find_bonds.nodes.new("GeometryNodeSampleIndex")
            sample_index_002.name = "Sample Index.002"
            sample_index_002.clamp = False
            sample_index_002.data_type = "FLOAT"
            sample_index_002.domain = "POINT"

            # node Named Attribute.008
            named_attribute_008 = topology_find_bonds.nodes.new(
                "GeometryNodeInputNamedAttribute"
            )
            named_attribute_008.label = "vdw_radii"
            named_attribute_008.name = "Named Attribute.008"
            named_attribute_008.hide = True
            named_attribute_008.data_type = "FLOAT"
            # Name
            named_attribute_008.inputs[0].default_value = "vdw_radii"

            # node Index.001
            index_001 = topology_find_bonds.nodes.new("GeometryNodeInputIndex")
            index_001.name = "Index.001"

            # node Sample Index.003
            sample_index_003 = topology_find_bonds.nodes.new("GeometryNodeSampleIndex")
            sample_index_003.name = "Sample Index.003"
            sample_index_003.clamp = False
            sample_index_003.data_type = "FLOAT_VECTOR"
            sample_index_003.domain = "POINT"

            # node Position.003
            position_003 = topology_find_bonds.nodes.new("GeometryNodeInputPosition")
            position_003.name = "Position.003"

            # node Reroute.004
            reroute_004 = topology_find_bonds.nodes.new("NodeReroute")
            reroute_004.name = "Reroute.004"
            # node Points
            points = topology_find_bonds.nodes.new("GeometryNodePoints")
            points.name = "Points"

            # node Domain Size
            domain_size = topology_find_bonds.nodes.new(
                "GeometryNodeAttributeDomainSize"
            )
            domain_size.name = "Domain Size"
            domain_size.hide = True
            domain_size.component = "MESH"
            domain_size.outputs[1].hide = True
            domain_size.outputs[2].hide = True
            domain_size.outputs[3].hide = True
            domain_size.outputs[4].hide = True
            domain_size.outputs[5].hide = True
            domain_size.outputs[6].hide = True

            # node Axes to Rotation
            axes_to_rotation = topology_find_bonds.nodes.new(
                "FunctionNodeAxesToRotation"
            )
            axes_to_rotation.name = "Axes to Rotation"
            axes_to_rotation.primary_axis = "Z"
            axes_to_rotation.secondary_axis = "X"
            # Secondary Axis
            axes_to_rotation.inputs[1].default_value = (1.0, 0.0, 0.0)

            # node Merge by Distance.001
            merge_by_distance_001 = topology_find_bonds.nodes.new(
                "GeometryNodeMergeByDistance"
            )
            merge_by_distance_001.name = "Merge by Distance.001"
            merge_by_distance_001.mode = "ALL"
            # Selection
            merge_by_distance_001.inputs[1].default_value = True
            # Distance
            merge_by_distance_001.inputs[2].default_value = 0.0010000000474974513

            # node Index.003
            index_003 = topology_find_bonds.nodes.new("GeometryNodeInputIndex")
            index_003.name = "Index.003"

            # node Sort Elements
            sort_elements = topology_find_bonds.nodes.new("GeometryNodeSortElements")
            sort_elements.name = "Sort Elements"
            sort_elements.domain = "POINT"
            # Selection
            sort_elements.inputs[1].default_value = True
            # Group ID
            sort_elements.inputs[2].default_value = 0

            # node Reroute.006
            reroute_006 = topology_find_bonds.nodes.new("NodeReroute")
            reroute_006.name = "Reroute.006"
            # node Capture Attribute
            capture_attribute_1 = topology_find_bonds.nodes.new(
                "GeometryNodeCaptureAttribute"
            )
            capture_attribute_1.name = "Capture Attribute"
            capture_attribute_1.active_index = 0
            capture_attribute_1.capture_items.clear()
            capture_attribute_1.capture_items.new("FLOAT", "Index")
            capture_attribute_1.capture_items["Index"].data_type = "INT"
            capture_attribute_1.domain = "POINT"

            # node Reroute.001
            reroute_001 = topology_find_bonds.nodes.new("NodeReroute")
            reroute_001.name = "Reroute.001"
            # node Reroute.003
            reroute_003 = topology_find_bonds.nodes.new("NodeReroute")
            reroute_003.name = "Reroute.003"
            # node Reroute.005
            reroute_005 = topology_find_bonds.nodes.new("NodeReroute")
            reroute_005.name = "Reroute.005"
            # node Reroute.007
            reroute_007 = topology_find_bonds.nodes.new("NodeReroute")
            reroute_007.name = "Reroute.007"
            # node Reroute.008
            reroute_008 = topology_find_bonds.nodes.new("NodeReroute")
            reroute_008.name = "Reroute.008"
            # node Reroute.009
            reroute_009 = topology_find_bonds.nodes.new("NodeReroute")
            reroute_009.name = "Reroute.009"
            # node Reroute.010
            reroute_010 = topology_find_bonds.nodes.new("NodeReroute")
            reroute_010.name = "Reroute.010"
            # node Reroute.011
            reroute_011 = topology_find_bonds.nodes.new("NodeReroute")
            reroute_011.name = "Reroute.011"
            # node Reroute.012
            reroute_012 = topology_find_bonds.nodes.new("NodeReroute")
            reroute_012.name = "Reroute.012"
            # node Reroute.013
            reroute_013 = topology_find_bonds.nodes.new("NodeReroute")
            reroute_013.name = "Reroute.013"
            # node Reroute.014
            reroute_014 = topology_find_bonds.nodes.new("NodeReroute")
            reroute_014.name = "Reroute.014"
            # node Reroute.015
            reroute_015 = topology_find_bonds.nodes.new("NodeReroute")
            reroute_015.name = "Reroute.015"
            # node Reroute.016
            reroute_016 = topology_find_bonds.nodes.new("NodeReroute")
            reroute_016.name = "Reroute.016"
            # node Reroute.017
            reroute_017 = topology_find_bonds.nodes.new("NodeReroute")
            reroute_017.name = "Reroute.017"
            # node Frame.001
            frame_001_1 = topology_find_bonds.nodes.new("NodeFrame")
            frame_001_1.label = "Get original index to sample values with"
            frame_001_1.name = "Frame.001"
            frame_001_1.label_size = 20
            frame_001_1.shrink = True

            # node Frame.002
            frame_002_1 = topology_find_bonds.nodes.new("NodeFrame")
            frame_002_1.label = "Create a clean set of points for instancing on"
            frame_002_1.name = "Frame.002"
            frame_002_1.label_size = 20
            frame_002_1.shrink = True

            # node Named Attribute.001
            named_attribute_001 = topology_find_bonds.nodes.new(
                "GeometryNodeInputNamedAttribute"
            )
            named_attribute_001.name = "Named Attribute.001"
            named_attribute_001.data_type = "INT"
            # Name
            named_attribute_001.inputs[0].default_value = "pre_bond_index"

            # node Remove Named Attribute
            remove_named_attribute = topology_find_bonds.nodes.new(
                "GeometryNodeRemoveAttribute"
            )
            remove_named_attribute.name = "Remove Named Attribute"
            remove_named_attribute.pattern_mode = "EXACT"
            # Name
            remove_named_attribute.inputs[1].default_value = "pre_bond_index"

            # node Reroute
            reroute = topology_find_bonds.nodes.new("NodeReroute")
            reroute.name = "Reroute"
            # node Reroute.018
            reroute_018 = topology_find_bonds.nodes.new("NodeReroute")
            reroute_018.name = "Reroute.018"
            # node Frame.003
            frame_003_1 = topology_find_bonds.nodes.new("NodeFrame")
            frame_003_1.label = "Apply the distance probe"
            frame_003_1.name = "Frame.003"
            frame_003_1.label_size = 20
            frame_003_1.shrink = True

            # node Domain Size.001
            domain_size_001 = topology_find_bonds.nodes.new(
                "GeometryNodeAttributeDomainSize"
            )
            domain_size_001.name = "Domain Size.001"
            domain_size_001.component = "MESH"
            domain_size_001.outputs[1].hide = True
            domain_size_001.outputs[2].hide = True
            domain_size_001.outputs[3].hide = True
            domain_size_001.outputs[4].hide = True
            domain_size_001.outputs[5].hide = True
            domain_size_001.outputs[6].hide = True

            # node Compare
            compare = topology_find_bonds.nodes.new("FunctionNodeCompare")
            compare.name = "Compare"
            compare.data_type = "INT"
            compare.mode = "ELEMENT"
            compare.operation = "EQUAL"
            # B_INT
            compare.inputs[3].default_value = 0

            # node Switch
            switch_1 = topology_find_bonds.nodes.new("GeometryNodeSwitch")
            switch_1.name = "Switch"
            switch_1.input_type = "GEOMETRY"

            # node Reroute.019
            reroute_019 = topology_find_bonds.nodes.new("NodeReroute")
            reroute_019.name = "Reroute.019"
            # node Frame.004
            frame_004 = topology_find_bonds.nodes.new("NodeFrame")
            frame_004.label = "stop warning if nothing selected"
            frame_004.name = "Frame.004"
            frame_004.label_size = 20
            frame_004.shrink = True

            # node Frame.005
            frame_005 = topology_find_bonds.nodes.new("NodeFrame")
            frame_005.label = "Sort elements to the same as they previously were"
            frame_005.name = "Frame.005"
            frame_005.label_size = 20
            frame_005.shrink = True

            # Set parents
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

            # Set locations
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
            store_named_attribute_2.location = (1180.0, 820.0)
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
            math_001_1.location = (100.0, 180.0)
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

            # initialize topology_find_bonds links
            # ico_sphere.Mesh -> instance_on_points.Points
            topology_find_bonds.links.new(
                ico_sphere.outputs[0], instance_on_points.inputs[0]
            )
            # mesh_line.Mesh -> instance_on_points.Instance
            topology_find_bonds.links.new(
                mesh_line.outputs[0], instance_on_points.inputs[2]
            )
            # ico_sphere.Mesh -> sample_index.Geometry
            topology_find_bonds.links.new(ico_sphere.outputs[0], sample_index.inputs[0])
            # index.Index -> sample_index.Index
            topology_find_bonds.links.new(index.outputs[0], sample_index.inputs[2])
            # position.Position -> vector_math.Vector
            topology_find_bonds.links.new(position.outputs[0], vector_math.inputs[0])
            # vector_math.Vector -> sample_index.Value
            topology_find_bonds.links.new(
                vector_math.outputs[0], sample_index.inputs[1]
            )
            # instance_on_points.Instances -> realize_instances.Geometry
            topology_find_bonds.links.new(
                instance_on_points.outputs[0], realize_instances.inputs[0]
            )
            # reroute_018.Output -> instance_on_points_001.Points
            topology_find_bonds.links.new(
                reroute_018.outputs[0], instance_on_points_001.inputs[0]
            )
            # merge_by_distance_001.Geometry -> instance_on_points_001.Instance
            topology_find_bonds.links.new(
                merge_by_distance_001.outputs[0], instance_on_points_001.inputs[2]
            )
            # instance_on_points_001.Instances -> realize_instances_001.Geometry
            topology_find_bonds.links.new(
                instance_on_points_001.outputs[0], realize_instances_001.inputs[0]
            )
            # math_1.Value -> instance_on_points_001.Scale
            topology_find_bonds.links.new(
                math_1.outputs[0], instance_on_points_001.inputs[6]
            )
            # realize_instances_001.Geometry -> set_position.Geometry
            topology_find_bonds.links.new(
                realize_instances_001.outputs[0], set_position.inputs[0]
            )
            # reroute.Output -> sample_index_001_1.Geometry
            topology_find_bonds.links.new(
                reroute.outputs[0], sample_index_001_1.inputs[0]
            )
            # position_001.Position -> sample_index_001_1.Value
            topology_find_bonds.links.new(
                position_001.outputs[0], sample_index_001_1.inputs[1]
            )
            # sample_index_001_1.Value -> set_position.Position
            topology_find_bonds.links.new(
                sample_index_001_1.outputs[0], set_position.inputs[2]
            )
            # reroute.Output -> sample_nearest.Geometry
            topology_find_bonds.links.new(reroute.outputs[0], sample_nearest.inputs[0])
            # sample_nearest.Index -> sample_index_001_1.Index
            topology_find_bonds.links.new(
                sample_nearest.outputs[0], sample_index_001_1.inputs[2]
            )
            # set_position.Geometry -> merge_by_distance.Geometry
            topology_find_bonds.links.new(
                set_position.outputs[0], merge_by_distance.inputs[0]
            )
            # group_input_001_1.Scale -> math_001_1.Value
            topology_find_bonds.links.new(
                group_input_001_1.outputs[2], math_001_1.inputs[0]
            )
            # math_001_1.Value -> math_1.Value
            topology_find_bonds.links.new(math_001_1.outputs[0], math_1.inputs[1])
            # reroute_017.Output -> sample_nearest_001.Geometry
            topology_find_bonds.links.new(
                reroute_017.outputs[0], sample_nearest_001.inputs[0]
            )
            # reroute_010.Output -> sample_index_005.Geometry
            topology_find_bonds.links.new(
                reroute_010.outputs[0], sample_index_005.inputs[0]
            )
            # named_attribute.Attribute -> sample_index_005.Value
            topology_find_bonds.links.new(
                named_attribute.outputs[0], sample_index_005.inputs[1]
            )
            # sample_index_005.Value -> store_named_attribute_2.Value
            topology_find_bonds.links.new(
                sample_index_005.outputs[0], store_named_attribute_2.inputs[3]
            )
            # capture_attribute_1.Geometry -> reroute_002.Input
            topology_find_bonds.links.new(
                capture_attribute_1.outputs[0], reroute_002.inputs[0]
            )
            # store_named_attribute_005.Geometry -> store_named_attribute_2.Geometry
            topology_find_bonds.links.new(
                store_named_attribute_005.outputs[0], store_named_attribute_2.inputs[0]
            )
            # store_named_attribute_2.Geometry -> store_named_attribute_001.Geometry
            topology_find_bonds.links.new(
                store_named_attribute_2.outputs[0], store_named_attribute_001.inputs[0]
            )
            # reroute_011.Output -> sample_index_006.Geometry
            topology_find_bonds.links.new(
                reroute_011.outputs[0], sample_index_006.inputs[0]
            )
            # named_attribute_002_1.Attribute -> sample_index_006.Value
            topology_find_bonds.links.new(
                named_attribute_002_1.outputs[0], sample_index_006.inputs[1]
            )
            # sample_index_006.Value -> store_named_attribute_001.Value
            topology_find_bonds.links.new(
                sample_index_006.outputs[0], store_named_attribute_001.inputs[3]
            )
            # reroute_012.Output -> sample_index_007.Geometry
            topology_find_bonds.links.new(
                reroute_012.outputs[0], sample_index_007.inputs[0]
            )
            # named_attribute_003.Attribute -> sample_index_007.Value
            topology_find_bonds.links.new(
                named_attribute_003.outputs[0], sample_index_007.inputs[1]
            )
            # reroute_013.Output -> sample_index_008.Geometry
            topology_find_bonds.links.new(
                reroute_013.outputs[0], sample_index_008.inputs[0]
            )
            # named_attribute_004.Attribute -> sample_index_008.Value
            topology_find_bonds.links.new(
                named_attribute_004.outputs[0], sample_index_008.inputs[1]
            )
            # store_named_attribute_001.Geometry -> store_named_attribute_002.Geometry
            topology_find_bonds.links.new(
                store_named_attribute_001.outputs[0],
                store_named_attribute_002.inputs[0],
            )
            # sample_index_007.Value -> store_named_attribute_002.Value
            topology_find_bonds.links.new(
                sample_index_007.outputs[0], store_named_attribute_002.inputs[3]
            )
            # store_named_attribute_002.Geometry -> store_named_attribute_003.Geometry
            topology_find_bonds.links.new(
                store_named_attribute_002.outputs[0],
                store_named_attribute_003.inputs[0],
            )
            # sample_index_008.Value -> store_named_attribute_003.Value
            topology_find_bonds.links.new(
                sample_index_008.outputs[0], store_named_attribute_003.inputs[3]
            )
            # reroute_014.Output -> sample_index_009.Geometry
            topology_find_bonds.links.new(
                reroute_014.outputs[0], sample_index_009.inputs[0]
            )
            # named_attribute_005.Attribute -> sample_index_009.Value
            topology_find_bonds.links.new(
                named_attribute_005.outputs[0], sample_index_009.inputs[1]
            )
            # reroute_017.Output -> sample_index_010.Geometry
            topology_find_bonds.links.new(
                reroute_017.outputs[0], sample_index_010.inputs[0]
            )
            # sample_nearest_001.Index -> sample_index_010.Index
            topology_find_bonds.links.new(
                sample_nearest_001.outputs[0], sample_index_010.inputs[2]
            )
            # index_002.Index -> sample_index_010.Value
            topology_find_bonds.links.new(
                index_002.outputs[0], sample_index_010.inputs[1]
            )
            # named_attribute_006.Attribute -> sample_index_005.Index
            topology_find_bonds.links.new(
                named_attribute_006.outputs[0], sample_index_005.inputs[2]
            )
            # reroute_001.Output -> sample_index_006.Index
            topology_find_bonds.links.new(
                reroute_001.outputs[0], sample_index_006.inputs[2]
            )
            # reroute_003.Output -> sample_index_007.Index
            topology_find_bonds.links.new(
                reroute_003.outputs[0], sample_index_007.inputs[2]
            )
            # reroute_005.Output -> sample_index_008.Index
            topology_find_bonds.links.new(
                reroute_005.outputs[0], sample_index_008.inputs[2]
            )
            # reroute_007.Output -> sample_index_009.Index
            topology_find_bonds.links.new(
                reroute_007.outputs[0], sample_index_009.inputs[2]
            )
            # store_named_attribute_003.Geometry -> store_named_attribute_004.Geometry
            topology_find_bonds.links.new(
                store_named_attribute_003.outputs[0],
                store_named_attribute_004.inputs[0],
            )
            # sample_index_009.Value -> store_named_attribute_004.Value
            topology_find_bonds.links.new(
                sample_index_009.outputs[0], store_named_attribute_004.inputs[3]
            )
            # store_named_attribute_004.Geometry -> set_position_002.Geometry
            topology_find_bonds.links.new(
                store_named_attribute_004.outputs[0], set_position_002.inputs[0]
            )
            # reroute_015.Output -> sample_index_011.Geometry
            topology_find_bonds.links.new(
                reroute_015.outputs[0], sample_index_011.inputs[0]
            )
            # reroute_008.Output -> sample_index_011.Index
            topology_find_bonds.links.new(
                reroute_008.outputs[0], sample_index_011.inputs[2]
            )
            # position_002.Position -> sample_index_011.Value
            topology_find_bonds.links.new(
                position_002.outputs[0], sample_index_011.inputs[1]
            )
            # sample_index_011.Value -> set_position_002.Position
            topology_find_bonds.links.new(
                sample_index_011.outputs[0], set_position_002.inputs[2]
            )
            # merge_by_distance.Geometry -> store_named_attribute_005.Geometry
            topology_find_bonds.links.new(
                merge_by_distance.outputs[0], store_named_attribute_005.inputs[0]
            )
            # sample_index_010.Value -> store_named_attribute_005.Value
            topology_find_bonds.links.new(
                sample_index_010.outputs[0], store_named_attribute_005.inputs[3]
            )
            # reroute_009.Output -> sample_index_012.Index
            topology_find_bonds.links.new(
                reroute_009.outputs[0], sample_index_012.inputs[2]
            )
            # reroute_016.Output -> sample_index_012.Geometry
            topology_find_bonds.links.new(
                reroute_016.outputs[0], sample_index_012.inputs[0]
            )
            # named_attribute_007.Attribute -> sample_index_012.Value
            topology_find_bonds.links.new(
                named_attribute_007.outputs[0], sample_index_012.inputs[1]
            )
            # set_position_002.Geometry -> store_named_attribute_006.Geometry
            topology_find_bonds.links.new(
                set_position_002.outputs[0], store_named_attribute_006.inputs[0]
            )
            # sample_index_012.Value -> store_named_attribute_006.Value
            topology_find_bonds.links.new(
                sample_index_012.outputs[0], store_named_attribute_006.inputs[3]
            )
            # group_input_4.Atoms -> separate_geometry_1.Geometry
            topology_find_bonds.links.new(
                group_input_4.outputs[0], separate_geometry_1.inputs[0]
            )
            # group_input_4.Selection -> separate_geometry_1.Selection
            topology_find_bonds.links.new(
                group_input_4.outputs[1], separate_geometry_1.inputs[1]
            )
            # reroute_004.Output -> sample_index_002.Geometry
            topology_find_bonds.links.new(
                reroute_004.outputs[0], sample_index_002.inputs[0]
            )
            # named_attribute_008.Attribute -> sample_index_002.Value
            topology_find_bonds.links.new(
                named_attribute_008.outputs[0], sample_index_002.inputs[1]
            )
            # index_001.Index -> sample_index_002.Index
            topology_find_bonds.links.new(
                index_001.outputs[0], sample_index_002.inputs[2]
            )
            # reroute_004.Output -> sample_index_003.Geometry
            topology_find_bonds.links.new(
                reroute_004.outputs[0], sample_index_003.inputs[0]
            )
            # index_001.Index -> sample_index_003.Index
            topology_find_bonds.links.new(
                index_001.outputs[0], sample_index_003.inputs[2]
            )
            # position_003.Position -> sample_index_003.Value
            topology_find_bonds.links.new(
                position_003.outputs[0], sample_index_003.inputs[1]
            )
            # reroute_006.Output -> reroute_004.Input
            topology_find_bonds.links.new(reroute_006.outputs[0], reroute_004.inputs[0])
            # sample_index_003.Value -> points.Position
            topology_find_bonds.links.new(sample_index_003.outputs[0], points.inputs[1])
            # reroute_006.Output -> domain_size.Geometry
            topology_find_bonds.links.new(reroute_006.outputs[0], domain_size.inputs[0])
            # domain_size.Point Count -> points.Count
            topology_find_bonds.links.new(domain_size.outputs[0], points.inputs[0])
            # sample_index_002.Value -> points.Radius
            topology_find_bonds.links.new(sample_index_002.outputs[0], points.inputs[2])
            # axes_to_rotation.Rotation -> instance_on_points.Rotation
            topology_find_bonds.links.new(
                axes_to_rotation.outputs[0], instance_on_points.inputs[5]
            )
            # sample_index.Value -> axes_to_rotation.Primary Axis
            topology_find_bonds.links.new(
                sample_index.outputs[0], axes_to_rotation.inputs[0]
            )
            # realize_instances.Geometry -> merge_by_distance_001.Geometry
            topology_find_bonds.links.new(
                realize_instances.outputs[0], merge_by_distance_001.inputs[0]
            )
            # sample_index_002.Value -> math_1.Value
            topology_find_bonds.links.new(sample_index_002.outputs[0], math_1.inputs[0])
            # separate_geometry_1.Selection -> capture_attribute_1.Geometry
            topology_find_bonds.links.new(
                separate_geometry_1.outputs[0], capture_attribute_1.inputs[0]
            )
            # index_003.Index -> capture_attribute_1.Index
            topology_find_bonds.links.new(
                index_003.outputs[0], capture_attribute_1.inputs[1]
            )
            # capture_attribute_1.Geometry -> reroute_006.Input
            topology_find_bonds.links.new(
                capture_attribute_1.outputs[0], reroute_006.inputs[0]
            )
            # named_attribute_006.Attribute -> reroute_001.Input
            topology_find_bonds.links.new(
                named_attribute_006.outputs[0], reroute_001.inputs[0]
            )
            # reroute_001.Output -> reroute_003.Input
            topology_find_bonds.links.new(reroute_001.outputs[0], reroute_003.inputs[0])
            # reroute_003.Output -> reroute_005.Input
            topology_find_bonds.links.new(reroute_003.outputs[0], reroute_005.inputs[0])
            # reroute_005.Output -> reroute_007.Input
            topology_find_bonds.links.new(reroute_005.outputs[0], reroute_007.inputs[0])
            # reroute_007.Output -> reroute_008.Input
            topology_find_bonds.links.new(reroute_007.outputs[0], reroute_008.inputs[0])
            # reroute_008.Output -> reroute_009.Input
            topology_find_bonds.links.new(reroute_008.outputs[0], reroute_009.inputs[0])
            # reroute_002.Output -> reroute_010.Input
            topology_find_bonds.links.new(reroute_002.outputs[0], reroute_010.inputs[0])
            # reroute_010.Output -> reroute_011.Input
            topology_find_bonds.links.new(reroute_010.outputs[0], reroute_011.inputs[0])
            # reroute_011.Output -> reroute_012.Input
            topology_find_bonds.links.new(reroute_011.outputs[0], reroute_012.inputs[0])
            # reroute_012.Output -> reroute_013.Input
            topology_find_bonds.links.new(reroute_012.outputs[0], reroute_013.inputs[0])
            # reroute_013.Output -> reroute_014.Input
            topology_find_bonds.links.new(reroute_013.outputs[0], reroute_014.inputs[0])
            # reroute_014.Output -> reroute_015.Input
            topology_find_bonds.links.new(reroute_014.outputs[0], reroute_015.inputs[0])
            # reroute_015.Output -> reroute_016.Input
            topology_find_bonds.links.new(reroute_015.outputs[0], reroute_016.inputs[0])
            # reroute_019.Output -> sort_elements.Geometry
            topology_find_bonds.links.new(
                reroute_019.outputs[0], sort_elements.inputs[0]
            )
            # reroute_002.Output -> reroute_017.Input
            topology_find_bonds.links.new(reroute_002.outputs[0], reroute_017.inputs[0])
            # named_attribute_001.Attribute -> sort_elements.Sort Weight
            topology_find_bonds.links.new(
                named_attribute_001.outputs[0], sort_elements.inputs[3]
            )
            # sort_elements.Geometry -> remove_named_attribute.Geometry
            topology_find_bonds.links.new(
                sort_elements.outputs[0], remove_named_attribute.inputs[0]
            )
            # reroute_018.Output -> reroute.Input
            topology_find_bonds.links.new(reroute_018.outputs[0], reroute.inputs[0])
            # points.Points -> reroute_018.Input
            topology_find_bonds.links.new(points.outputs[0], reroute_018.inputs[0])
            # reroute_019.Output -> domain_size_001.Geometry
            topology_find_bonds.links.new(
                reroute_019.outputs[0], domain_size_001.inputs[0]
            )
            # domain_size_001.Point Count -> compare.A
            topology_find_bonds.links.new(domain_size_001.outputs[0], compare.inputs[2])
            # switch_1.Output -> group_output_4.Atoms
            topology_find_bonds.links.new(switch_1.outputs[0], group_output_4.inputs[0])
            # remove_named_attribute.Geometry -> switch_1.False
            topology_find_bonds.links.new(
                remove_named_attribute.outputs[0], switch_1.inputs[1]
            )
            # compare.Result -> switch_1.Switch
            topology_find_bonds.links.new(compare.outputs[0], switch_1.inputs[0])
            # store_named_attribute_006.Geometry -> reroute_019.Input
            topology_find_bonds.links.new(
                store_named_attribute_006.outputs[0], reroute_019.inputs[0]
            )
            return topology_find_bonds

        topology_find_bonds = topology_find_bonds_node_group()

        # initialize _mn_utils_style_spheres_points node group
        def _mn_utils_style_spheres_points_node_group():
            _mn_utils_style_spheres_points = bpy.data.node_groups.new(
                type="GeometryNodeTree", name=".MN_utils_style_spheres_points"
            )

            _mn_utils_style_spheres_points.color_tag = "GEOMETRY"
            _mn_utils_style_spheres_points.description = ""

            _mn_utils_style_spheres_points.is_modifier = True

            # _mn_utils_style_spheres_points interface
            # Socket Point Cloud
            point_cloud_socket = _mn_utils_style_spheres_points.interface.new_socket(
                name="Point Cloud", in_out="OUTPUT", socket_type="NodeSocketGeometry"
            )
            point_cloud_socket.attribute_domain = "POINT"

            # Socket Atoms
            atoms_socket_5 = _mn_utils_style_spheres_points.interface.new_socket(
                name="Atoms", in_out="INPUT", socket_type="NodeSocketGeometry"
            )
            atoms_socket_5.attribute_domain = "POINT"
            atoms_socket_5.description = (
                "Atomic geometry that contains vertices and edges"
            )

            # Socket Selection
            selection_socket_3 = _mn_utils_style_spheres_points.interface.new_socket(
                name="Selection", in_out="INPUT", socket_type="NodeSocketBool"
            )
            selection_socket_3.attribute_domain = "POINT"
            selection_socket_3.hide_value = True
            selection_socket_3.description = "Selection of atoms to apply this node to"

            # Socket Radii
            radii_socket = _mn_utils_style_spheres_points.interface.new_socket(
                name="Radii", in_out="INPUT", socket_type="NodeSocketFloat"
            )
            radii_socket.subtype = "NONE"
            radii_socket.default_value = 0.800000011920929
            radii_socket.min_value = 0.0
            radii_socket.max_value = 10000.0
            radii_socket.attribute_domain = "POINT"

            # Socket Material
            material_socket_1 = _mn_utils_style_spheres_points.interface.new_socket(
                name="Material", in_out="INPUT", socket_type="NodeSocketMaterial"
            )
            material_socket_1.attribute_domain = "POINT"
            material_socket_1.description = (
                "Material to apply to the resulting geometry"
            )

            # initialize _mn_utils_style_spheres_points nodes
            # node Group Input
            group_input_5 = _mn_utils_style_spheres_points.nodes.new("NodeGroupInput")
            group_input_5.name = "Group Input"

            # node Mesh to Points
            mesh_to_points = _mn_utils_style_spheres_points.nodes.new(
                "GeometryNodeMeshToPoints"
            )
            mesh_to_points.name = "Mesh to Points"
            mesh_to_points.mode = "VERTICES"
            # Position
            mesh_to_points.inputs[2].default_value = (0.0, 0.0, 0.0)

            # node Switch
            switch_2 = _mn_utils_style_spheres_points.nodes.new("GeometryNodeSwitch")
            switch_2.name = "Switch"
            switch_2.input_type = "FLOAT"

            # node Named Attribute
            named_attribute_1 = _mn_utils_style_spheres_points.nodes.new(
                "GeometryNodeInputNamedAttribute"
            )
            named_attribute_1.name = "Named Attribute"
            named_attribute_1.data_type = "FLOAT"
            # Name
            named_attribute_1.inputs[0].default_value = "vdw_radii"

            # node Group
            group_2 = _mn_utils_style_spheres_points.nodes.new("GeometryNodeGroup")
            group_2.name = "Group"
            group_2.node_tree = mn_units
            # Input_1
            group_2.inputs[0].default_value = 0.800000011920929

            # node Math
            math_2 = _mn_utils_style_spheres_points.nodes.new("ShaderNodeMath")
            math_2.name = "Math"
            math_2.operation = "MULTIPLY"
            math_2.use_clamp = False

            # node Group Output
            group_output_5 = _mn_utils_style_spheres_points.nodes.new("NodeGroupOutput")
            group_output_5.name = "Group Output"
            group_output_5.is_active_output = True

            # node Set Material
            set_material_1 = _mn_utils_style_spheres_points.nodes.new(
                "GeometryNodeSetMaterial"
            )
            set_material_1.name = "Set Material"
            # Selection
            set_material_1.inputs[1].default_value = True

            # Set locations
            group_input_5.location = (-1060.0, 60.0)
            mesh_to_points.location = (-540.0, 220.0)
            switch_2.location = (-900.0, -100.0)
            named_attribute_1.location = (-1080.0, -100.0)
            group_2.location = (-1080.0, -240.0)
            math_2.location = (-720.0, 40.0)
            group_output_5.location = (-220.0, 220.0)
            set_material_1.location = (-380.0, 220.0)

            # initialize _mn_utils_style_spheres_points links
            # set_material_1.Geometry -> group_output_5.Point Cloud
            _mn_utils_style_spheres_points.links.new(
                set_material_1.outputs[0], group_output_5.inputs[0]
            )
            # group_input_5.Selection -> mesh_to_points.Selection
            _mn_utils_style_spheres_points.links.new(
                group_input_5.outputs[1], mesh_to_points.inputs[1]
            )
            # group_input_5.Radii -> math_2.Value
            _mn_utils_style_spheres_points.links.new(
                group_input_5.outputs[2], math_2.inputs[0]
            )
            # math_2.Value -> mesh_to_points.Radius
            _mn_utils_style_spheres_points.links.new(
                math_2.outputs[0], mesh_to_points.inputs[3]
            )
            # group_input_5.Material -> set_material_1.Material
            _mn_utils_style_spheres_points.links.new(
                group_input_5.outputs[3], set_material_1.inputs[2]
            )
            # named_attribute_1.Attribute -> switch_2.Switch
            _mn_utils_style_spheres_points.links.new(
                named_attribute_1.outputs[0], switch_2.inputs[0]
            )
            # named_attribute_1.Attribute -> switch_2.True
            _mn_utils_style_spheres_points.links.new(
                named_attribute_1.outputs[0], switch_2.inputs[2]
            )
            # switch_2.Output -> math_2.Value
            _mn_utils_style_spheres_points.links.new(
                switch_2.outputs[0], math_2.inputs[1]
            )
            # group_input_5.Atoms -> mesh_to_points.Mesh
            _mn_utils_style_spheres_points.links.new(
                group_input_5.outputs[0], mesh_to_points.inputs[0]
            )
            # mesh_to_points.Points -> set_material_1.Geometry
            _mn_utils_style_spheres_points.links.new(
                mesh_to_points.outputs[0], set_material_1.inputs[0]
            )
            # group_2.Angstrom -> switch_2.False
            _mn_utils_style_spheres_points.links.new(
                group_2.outputs[0], switch_2.inputs[1]
            )
            return _mn_utils_style_spheres_points

        _mn_utils_style_spheres_points = _mn_utils_style_spheres_points_node_group()

        # initialize _mn_utils_style_spheres_icosphere node group
        def _mn_utils_style_spheres_icosphere_node_group():
            _mn_utils_style_spheres_icosphere = bpy.data.node_groups.new(
                type="GeometryNodeTree", name=".MN_utils_style_spheres_icosphere"
            )

            _mn_utils_style_spheres_icosphere.color_tag = "GEOMETRY"
            _mn_utils_style_spheres_icosphere.description = ""

            _mn_utils_style_spheres_icosphere.is_modifier = True

            # _mn_utils_style_spheres_icosphere interface
            # Socket Instances
            instances_socket = _mn_utils_style_spheres_icosphere.interface.new_socket(
                name="Instances", in_out="OUTPUT", socket_type="NodeSocketGeometry"
            )
            instances_socket.attribute_domain = "POINT"

            # Socket Atoms
            atoms_socket_6 = _mn_utils_style_spheres_icosphere.interface.new_socket(
                name="Atoms", in_out="INPUT", socket_type="NodeSocketGeometry"
            )
            atoms_socket_6.attribute_domain = "POINT"
            atoms_socket_6.description = (
                "Atomic geometry that contains vertices and edges"
            )

            # Socket Selection
            selection_socket_4 = _mn_utils_style_spheres_icosphere.interface.new_socket(
                name="Selection", in_out="INPUT", socket_type="NodeSocketBool"
            )
            selection_socket_4.attribute_domain = "POINT"
            selection_socket_4.hide_value = True
            selection_socket_4.description = "Selection of atoms to apply this node to"

            # Socket Radii
            radii_socket_1 = _mn_utils_style_spheres_icosphere.interface.new_socket(
                name="Radii", in_out="INPUT", socket_type="NodeSocketFloat"
            )
            radii_socket_1.subtype = "NONE"
            radii_socket_1.default_value = 0.800000011920929
            radii_socket_1.min_value = 0.0
            radii_socket_1.max_value = 10000.0
            radii_socket_1.attribute_domain = "POINT"
            radii_socket_1.description = "Scale the VDW radii of the atoms."

            # Socket Subdivisions
            subdivisions_socket = (
                _mn_utils_style_spheres_icosphere.interface.new_socket(
                    name="Subdivisions", in_out="INPUT", socket_type="NodeSocketInt"
                )
            )
            subdivisions_socket.subtype = "NONE"
            subdivisions_socket.default_value = 2
            subdivisions_socket.min_value = 0
            subdivisions_socket.max_value = 5
            subdivisions_socket.attribute_domain = "POINT"

            # Socket Shade Smooth
            shade_smooth_socket_1 = (
                _mn_utils_style_spheres_icosphere.interface.new_socket(
                    name="Shade Smooth", in_out="INPUT", socket_type="NodeSocketBool"
                )
            )
            shade_smooth_socket_1.attribute_domain = "POINT"
            shade_smooth_socket_1.description = (
                "Apply smooth shading to the created geometry"
            )

            # Socket Material
            material_socket_2 = _mn_utils_style_spheres_icosphere.interface.new_socket(
                name="Material", in_out="INPUT", socket_type="NodeSocketMaterial"
            )
            material_socket_2.attribute_domain = "POINT"
            material_socket_2.description = (
                "Material to apply to the resulting geometry"
            )

            # initialize _mn_utils_style_spheres_icosphere nodes
            # node Frame
            frame_2 = _mn_utils_style_spheres_icosphere.nodes.new("NodeFrame")
            frame_2.label = "Different Levels of Detail."
            frame_2.name = "Frame"
            frame_2.label_size = 20
            frame_2.shrink = True

            # node Reroute
            reroute_1 = _mn_utils_style_spheres_icosphere.nodes.new("NodeReroute")
            reroute_1.name = "Reroute"
            # node Math.001
            math_001_2 = _mn_utils_style_spheres_icosphere.nodes.new("ShaderNodeMath")
            math_001_2.name = "Math.001"
            math_001_2.operation = "MINIMUM"
            math_001_2.use_clamp = False

            # node Group Output
            group_output_6 = _mn_utils_style_spheres_icosphere.nodes.new(
                "NodeGroupOutput"
            )
            group_output_6.name = "Group Output"
            group_output_6.is_active_output = True

            # node Group Input.002
            group_input_002_1 = _mn_utils_style_spheres_icosphere.nodes.new(
                "NodeGroupInput"
            )
            group_input_002_1.name = "Group Input.002"
            group_input_002_1.outputs[0].hide = True
            group_input_002_1.outputs[1].hide = True
            group_input_002_1.outputs[2].hide = True
            group_input_002_1.outputs[3].hide = True
            group_input_002_1.outputs[6].hide = True

            # node Set Shade Smooth
            set_shade_smooth_1 = _mn_utils_style_spheres_icosphere.nodes.new(
                "GeometryNodeSetShadeSmooth"
            )
            set_shade_smooth_1.name = "Set Shade Smooth"
            set_shade_smooth_1.domain = "FACE"
            # Selection
            set_shade_smooth_1.inputs[1].default_value = True

            # node Set Material
            set_material_2 = _mn_utils_style_spheres_icosphere.nodes.new(
                "GeometryNodeSetMaterial"
            )
            set_material_2.name = "Set Material"
            # Selection
            set_material_2.inputs[1].default_value = True

            # node Group Input
            group_input_6 = _mn_utils_style_spheres_icosphere.nodes.new(
                "NodeGroupInput"
            )
            group_input_6.name = "Group Input"
            group_input_6.outputs[2].hide = True
            group_input_6.outputs[3].hide = True
            group_input_6.outputs[4].hide = True
            group_input_6.outputs[5].hide = True
            group_input_6.outputs[6].hide = True

            # node Reroute.001
            reroute_001_1 = _mn_utils_style_spheres_icosphere.nodes.new("NodeReroute")
            reroute_001_1.name = "Reroute.001"
            # node Group Input.001
            group_input_001_2 = _mn_utils_style_spheres_icosphere.nodes.new(
                "NodeGroupInput"
            )
            group_input_001_2.name = "Group Input.001"
            group_input_001_2.outputs[0].hide = True
            group_input_001_2.outputs[1].hide = True
            group_input_001_2.outputs[2].hide = True
            group_input_001_2.outputs[4].hide = True
            group_input_001_2.outputs[5].hide = True
            group_input_001_2.outputs[6].hide = True

            # node Ico Sphere.001
            ico_sphere_001 = _mn_utils_style_spheres_icosphere.nodes.new(
                "GeometryNodeMeshIcoSphere"
            )
            ico_sphere_001.name = "Ico Sphere.001"
            # Radius
            ico_sphere_001.inputs[0].default_value = 1.0
            # Subdivisions
            ico_sphere_001.inputs[1].default_value = 1

            # node Ico Sphere.002
            ico_sphere_002 = _mn_utils_style_spheres_icosphere.nodes.new(
                "GeometryNodeMeshIcoSphere"
            )
            ico_sphere_002.name = "Ico Sphere.002"
            # Radius
            ico_sphere_002.inputs[0].default_value = 1.0
            # Subdivisions
            ico_sphere_002.inputs[1].default_value = 2

            # node Ico Sphere.003
            ico_sphere_003 = _mn_utils_style_spheres_icosphere.nodes.new(
                "GeometryNodeMeshIcoSphere"
            )
            ico_sphere_003.name = "Ico Sphere.003"
            # Radius
            ico_sphere_003.inputs[0].default_value = 1.0
            # Subdivisions
            ico_sphere_003.inputs[1].default_value = 3

            # node Geometry to Instance
            geometry_to_instance = _mn_utils_style_spheres_icosphere.nodes.new(
                "GeometryNodeGeometryToInstance"
            )
            geometry_to_instance.name = "Geometry to Instance"

            # node Ico Sphere.004
            ico_sphere_004 = _mn_utils_style_spheres_icosphere.nodes.new(
                "GeometryNodeMeshIcoSphere"
            )
            ico_sphere_004.name = "Ico Sphere.004"
            # Radius
            ico_sphere_004.inputs[0].default_value = 1.0
            # Subdivisions
            ico_sphere_004.inputs[1].default_value = 4

            # node Ico Sphere.005
            ico_sphere_005 = _mn_utils_style_spheres_icosphere.nodes.new(
                "GeometryNodeMeshIcoSphere"
            )
            ico_sphere_005.name = "Ico Sphere.005"
            # Radius
            ico_sphere_005.inputs[0].default_value = 1.0
            # Subdivisions
            ico_sphere_005.inputs[1].default_value = 5

            # node Reroute.002
            reroute_002_1 = _mn_utils_style_spheres_icosphere.nodes.new("NodeReroute")
            reroute_002_1.name = "Reroute.002"
            # node Transform Geometry
            transform_geometry = _mn_utils_style_spheres_icosphere.nodes.new(
                "GeometryNodeTransform"
            )
            transform_geometry.name = "Transform Geometry"
            transform_geometry.mode = "COMPONENTS"
            # Translation
            transform_geometry.inputs[1].default_value = (0.0, 0.0, 0.0)
            # Rotation
            transform_geometry.inputs[2].default_value = (
                0.7853981852531433,
                0.7853981852531433,
                0.0,
            )
            # Scale
            transform_geometry.inputs[3].default_value = (1.0, 1.0, 1.0)

            # node Cube
            cube = _mn_utils_style_spheres_icosphere.nodes.new("GeometryNodeMeshCube")
            cube.name = "Cube"
            # Size
            cube.inputs[0].default_value = (1.0, 1.0, 1.0)
            # Vertices X
            cube.inputs[1].default_value = 2
            # Vertices Y
            cube.inputs[2].default_value = 2
            # Vertices Z
            cube.inputs[3].default_value = 2

            # node Named Attribute
            named_attribute_2 = _mn_utils_style_spheres_icosphere.nodes.new(
                "GeometryNodeInputNamedAttribute"
            )
            named_attribute_2.name = "Named Attribute"
            named_attribute_2.data_type = "FLOAT"
            # Name
            named_attribute_2.inputs[0].default_value = "vdw_radii"

            # node Radius
            radius = _mn_utils_style_spheres_icosphere.nodes.new(
                "GeometryNodeInputRadius"
            )
            radius.name = "Radius"

            # node Math
            math_3 = _mn_utils_style_spheres_icosphere.nodes.new("ShaderNodeMath")
            math_3.name = "Math"
            math_3.operation = "MAXIMUM"
            math_3.use_clamp = False

            # node Math.003
            math_003 = _mn_utils_style_spheres_icosphere.nodes.new("ShaderNodeMath")
            math_003.name = "Math.003"
            math_003.operation = "MULTIPLY"
            math_003.use_clamp = False

            # node Group Input.003
            group_input_003_1 = _mn_utils_style_spheres_icosphere.nodes.new(
                "NodeGroupInput"
            )
            group_input_003_1.name = "Group Input.003"
            group_input_003_1.outputs[0].hide = True
            group_input_003_1.outputs[1].hide = True
            group_input_003_1.outputs[3].hide = True
            group_input_003_1.outputs[4].hide = True
            group_input_003_1.outputs[5].hide = True
            group_input_003_1.outputs[6].hide = True

            # node Math.002
            math_002 = _mn_utils_style_spheres_icosphere.nodes.new("ShaderNodeMath")
            math_002.name = "Math.002"
            math_002.operation = "ADD"
            math_002.use_clamp = False

            # node Integer
            integer = _mn_utils_style_spheres_icosphere.nodes.new(
                "FunctionNodeInputInt"
            )
            integer.name = "Integer"
            integer.integer = -1

            # node Domain Size
            domain_size_1 = _mn_utils_style_spheres_icosphere.nodes.new(
                "GeometryNodeAttributeDomainSize"
            )
            domain_size_1.name = "Domain Size"
            domain_size_1.component = "INSTANCES"

            # node Instance on Points
            instance_on_points_1 = _mn_utils_style_spheres_icosphere.nodes.new(
                "GeometryNodeInstanceOnPoints"
            )
            instance_on_points_1.name = "Instance on Points"
            # Pick Instance
            instance_on_points_1.inputs[3].default_value = True
            # Rotation
            instance_on_points_1.inputs[5].default_value = (0.0, 0.0, 0.0)

            # Set parents
            ico_sphere_001.parent = frame_2
            ico_sphere_002.parent = frame_2
            ico_sphere_003.parent = frame_2
            geometry_to_instance.parent = frame_2
            ico_sphere_004.parent = frame_2
            ico_sphere_005.parent = frame_2
            reroute_002_1.parent = frame_2
            transform_geometry.parent = frame_2
            cube.parent = frame_2

            # Set locations
            frame_2.location = (0.0, 0.0)
            reroute_1.location = (-560.0, -40.0)
            math_001_2.location = (-140.0, 60.0)
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

            # initialize _mn_utils_style_spheres_icosphere links
            # set_material_2.Geometry -> group_output_6.Instances
            _mn_utils_style_spheres_icosphere.links.new(
                set_material_2.outputs[0], group_output_6.inputs[0]
            )
            # set_shade_smooth_1.Geometry -> set_material_2.Geometry
            _mn_utils_style_spheres_icosphere.links.new(
                set_shade_smooth_1.outputs[0], set_material_2.inputs[0]
            )
            # group_input_6.Atoms -> instance_on_points_1.Points
            _mn_utils_style_spheres_icosphere.links.new(
                group_input_6.outputs[0], instance_on_points_1.inputs[0]
            )
            # reroute_001_1.Output -> instance_on_points_1.Instance
            _mn_utils_style_spheres_icosphere.links.new(
                reroute_001_1.outputs[0], instance_on_points_1.inputs[2]
            )
            # ico_sphere_005.Mesh -> geometry_to_instance.Geometry
            _mn_utils_style_spheres_icosphere.links.new(
                ico_sphere_005.outputs[0], geometry_to_instance.inputs[0]
            )
            # math_001_2.Value -> instance_on_points_1.Instance Index
            _mn_utils_style_spheres_icosphere.links.new(
                math_001_2.outputs[0], instance_on_points_1.inputs[4]
            )
            # group_input_001_2.Subdivisions -> math_001_2.Value
            _mn_utils_style_spheres_icosphere.links.new(
                group_input_001_2.outputs[3], math_001_2.inputs[0]
            )
            # reroute_1.Output -> domain_size_1.Geometry
            _mn_utils_style_spheres_icosphere.links.new(
                reroute_1.outputs[0], domain_size_1.inputs[0]
            )
            # geometry_to_instance.Instances -> reroute_1.Input
            _mn_utils_style_spheres_icosphere.links.new(
                geometry_to_instance.outputs[0], reroute_1.inputs[0]
            )
            # named_attribute_2.Attribute -> math_3.Value
            _mn_utils_style_spheres_icosphere.links.new(
                named_attribute_2.outputs[0], math_3.inputs[0]
            )
            # radius.Radius -> math_3.Value
            _mn_utils_style_spheres_icosphere.links.new(
                radius.outputs[0], math_3.inputs[1]
            )
            # group_input_002_1.Material -> set_material_2.Material
            _mn_utils_style_spheres_icosphere.links.new(
                group_input_002_1.outputs[5], set_material_2.inputs[2]
            )
            # instance_on_points_1.Instances -> set_shade_smooth_1.Geometry
            _mn_utils_style_spheres_icosphere.links.new(
                instance_on_points_1.outputs[0], set_shade_smooth_1.inputs[0]
            )
            # group_input_002_1.Shade Smooth -> set_shade_smooth_1.Shade Smooth
            _mn_utils_style_spheres_icosphere.links.new(
                group_input_002_1.outputs[4], set_shade_smooth_1.inputs[2]
            )
            # group_input_6.Selection -> instance_on_points_1.Selection
            _mn_utils_style_spheres_icosphere.links.new(
                group_input_6.outputs[1], instance_on_points_1.inputs[1]
            )
            # math_3.Value -> math_003.Value
            _mn_utils_style_spheres_icosphere.links.new(
                math_3.outputs[0], math_003.inputs[0]
            )
            # group_input_003_1.Radii -> math_003.Value
            _mn_utils_style_spheres_icosphere.links.new(
                group_input_003_1.outputs[2], math_003.inputs[1]
            )
            # reroute_1.Output -> reroute_001_1.Input
            _mn_utils_style_spheres_icosphere.links.new(
                reroute_1.outputs[0], reroute_001_1.inputs[0]
            )
            # math_003.Value -> instance_on_points_1.Scale
            _mn_utils_style_spheres_icosphere.links.new(
                math_003.outputs[0], instance_on_points_1.inputs[6]
            )
            # cube.Mesh -> transform_geometry.Geometry
            _mn_utils_style_spheres_icosphere.links.new(
                cube.outputs[0], transform_geometry.inputs[0]
            )
            # transform_geometry.Geometry -> reroute_002_1.Input
            _mn_utils_style_spheres_icosphere.links.new(
                transform_geometry.outputs[0], reroute_002_1.inputs[0]
            )
            # domain_size_1.Instance Count -> math_002.Value
            _mn_utils_style_spheres_icosphere.links.new(
                domain_size_1.outputs[5], math_002.inputs[0]
            )
            # integer.Integer -> math_002.Value
            _mn_utils_style_spheres_icosphere.links.new(
                integer.outputs[0], math_002.inputs[1]
            )
            # math_002.Value -> math_001_2.Value
            _mn_utils_style_spheres_icosphere.links.new(
                math_002.outputs[0], math_001_2.inputs[1]
            )
            # ico_sphere_004.Mesh -> geometry_to_instance.Geometry
            _mn_utils_style_spheres_icosphere.links.new(
                ico_sphere_004.outputs[0], geometry_to_instance.inputs[0]
            )
            # ico_sphere_003.Mesh -> geometry_to_instance.Geometry
            _mn_utils_style_spheres_icosphere.links.new(
                ico_sphere_003.outputs[0], geometry_to_instance.inputs[0]
            )
            # ico_sphere_002.Mesh -> geometry_to_instance.Geometry
            _mn_utils_style_spheres_icosphere.links.new(
                ico_sphere_002.outputs[0], geometry_to_instance.inputs[0]
            )
            # ico_sphere_001.Mesh -> geometry_to_instance.Geometry
            _mn_utils_style_spheres_icosphere.links.new(
                ico_sphere_001.outputs[0], geometry_to_instance.inputs[0]
            )
            # reroute_002_1.Output -> geometry_to_instance.Geometry
            _mn_utils_style_spheres_icosphere.links.new(
                reroute_002_1.outputs[0], geometry_to_instance.inputs[0]
            )
            return _mn_utils_style_spheres_icosphere

        _mn_utils_style_spheres_icosphere = (
            _mn_utils_style_spheres_icosphere_node_group()
        )

        # initialize style_spheres node group
        def style_spheres_node_group():
            style_spheres = bpy.data.node_groups.new(
                type="GeometryNodeTree", name="Style Spheres"
            )

            style_spheres.color_tag = "GEOMETRY"
            style_spheres.description = ""

            style_spheres.is_modifier = True

            # style_spheres interface
            # Socket Geometry
            geometry_socket_1 = style_spheres.interface.new_socket(
                name="Geometry", in_out="OUTPUT", socket_type="NodeSocketGeometry"
            )
            geometry_socket_1.attribute_domain = "POINT"

            # Socket Atoms
            atoms_socket_7 = style_spheres.interface.new_socket(
                name="Atoms", in_out="INPUT", socket_type="NodeSocketGeometry"
            )
            atoms_socket_7.attribute_domain = "POINT"
            atoms_socket_7.description = (
                "Atomic geometry that contains vertices and edges"
            )

            # Socket Selection
            selection_socket_5 = style_spheres.interface.new_socket(
                name="Selection", in_out="INPUT", socket_type="NodeSocketBool"
            )
            selection_socket_5.attribute_domain = "POINT"
            selection_socket_5.hide_value = True
            selection_socket_5.description = "Selection of atoms to apply this style to"

            # Panel Sphere
            sphere_panel = style_spheres.interface.new_panel("Sphere")
            # Socket Sphere As Mesh
            sphere_as_mesh_socket = style_spheres.interface.new_socket(
                name="Sphere As Mesh",
                in_out="INPUT",
                socket_type="NodeSocketBool",
                parent=sphere_panel,
            )
            sphere_as_mesh_socket.attribute_domain = "POINT"
            sphere_as_mesh_socket.description = "Use Eevee or Cycles compatible atoms."

            # Socket Sphere Radii
            sphere_radii_socket = style_spheres.interface.new_socket(
                name="Sphere Radii",
                in_out="INPUT",
                socket_type="NodeSocketFloat",
                parent=sphere_panel,
            )
            sphere_radii_socket.subtype = "NONE"
            sphere_radii_socket.default_value = 0.800000011920929
            sphere_radii_socket.min_value = 0.0
            sphere_radii_socket.max_value = 2.0
            sphere_radii_socket.attribute_domain = "POINT"
            sphere_radii_socket.description = "Scale the `vdw_radii` of the atoms."

            # Socket Sphere Subdivisions
            sphere_subdivisions_socket = style_spheres.interface.new_socket(
                name="Sphere Subdivisions",
                in_out="INPUT",
                socket_type="NodeSocketInt",
                parent=sphere_panel,
            )
            sphere_subdivisions_socket.subtype = "NONE"
            sphere_subdivisions_socket.default_value = 2
            sphere_subdivisions_socket.min_value = 0
            sphere_subdivisions_socket.max_value = 5
            sphere_subdivisions_socket.attribute_domain = "POINT"
            sphere_subdivisions_socket.description = (
                "Subdivisions for Eevee compatible atoms."
            )

            # Panel Material
            material_panel_1 = style_spheres.interface.new_panel(
                "Material", default_closed=True
            )
            # Socket Shade Smooth
            shade_smooth_socket_2 = style_spheres.interface.new_socket(
                name="Shade Smooth",
                in_out="INPUT",
                socket_type="NodeSocketBool",
                parent=material_panel_1,
            )
            shade_smooth_socket_2.attribute_domain = "POINT"
            shade_smooth_socket_2.description = (
                "Apply smooth shading to the created geometry"
            )

            # Socket Material
            material_socket_3 = style_spheres.interface.new_socket(
                name="Material",
                in_out="INPUT",
                socket_type="NodeSocketMaterial",
                parent=material_panel_1,
            )
            material_socket_3.attribute_domain = "POINT"
            material_socket_3.description = (
                "Material to apply to the resulting geometry"
            )

            # initialize style_spheres nodes
            # node Group Input
            group_input_7 = style_spheres.nodes.new("NodeGroupInput")
            group_input_7.name = "Group Input"

            # node Group Output
            group_output_7 = style_spheres.nodes.new("NodeGroupOutput")
            group_output_7.name = "Group Output"
            group_output_7.is_active_output = True

            # node Join Geometry
            join_geometry = style_spheres.nodes.new("GeometryNodeJoinGeometry")
            join_geometry.name = "Join Geometry"

            # node Separate Geometry
            separate_geometry_2 = style_spheres.nodes.new(
                "GeometryNodeSeparateGeometry"
            )
            separate_geometry_2.name = "Separate Geometry"
            separate_geometry_2.domain = "POINT"

            # node Group.014
            group_014 = style_spheres.nodes.new("GeometryNodeGroup")
            group_014.name = "Group.014"
            group_014.node_tree = _mn_utils_style_spheres_points

            # node Group.026
            group_026 = style_spheres.nodes.new("GeometryNodeGroup")
            group_026.name = "Group.026"
            group_026.node_tree = _mn_utils_style_spheres_icosphere

            # node Realize Instances
            realize_instances_1 = style_spheres.nodes.new(
                "GeometryNodeRealizeInstances"
            )
            realize_instances_1.name = "Realize Instances"
            # Selection
            realize_instances_1.inputs[1].default_value = True
            # Realize All
            realize_instances_1.inputs[2].default_value = True
            # Depth
            realize_instances_1.inputs[3].default_value = 0

            # Set locations
            group_input_7.location = (-679.2061157226562, -54.561466217041016)
            group_output_7.location = (480.0, 40.0)
            join_geometry.location = (320.0, 40.0)
            separate_geometry_2.location = (-420.0, 80.0)
            group_014.location = (-200.0, -200.0)
            group_026.location = (-200.0, 60.0)
            realize_instances_1.location = (100.0, 60.0)

            # initialize style_spheres links
            # group_input_7.Atoms -> separate_geometry_2.Geometry
            style_spheres.links.new(
                group_input_7.outputs[0], separate_geometry_2.inputs[0]
            )
            # group_input_7.Selection -> group_014.Selection
            style_spheres.links.new(group_input_7.outputs[1], group_014.inputs[1])
            # group_input_7.Selection -> group_026.Selection
            style_spheres.links.new(group_input_7.outputs[1], group_026.inputs[1])
            # group_input_7.Sphere As Mesh -> separate_geometry_2.Selection
            style_spheres.links.new(
                group_input_7.outputs[2], separate_geometry_2.inputs[1]
            )
            # group_input_7.Sphere Radii -> group_014.Radii
            style_spheres.links.new(group_input_7.outputs[3], group_014.inputs[2])
            # group_input_7.Sphere Radii -> group_026.Radii
            style_spheres.links.new(group_input_7.outputs[3], group_026.inputs[2])
            # group_input_7.Sphere Subdivisions -> group_026.Subdivisions
            style_spheres.links.new(group_input_7.outputs[4], group_026.inputs[3])
            # group_input_7.Shade Smooth -> group_026.Shade Smooth
            style_spheres.links.new(group_input_7.outputs[5], group_026.inputs[4])
            # group_input_7.Material -> group_014.Material
            style_spheres.links.new(group_input_7.outputs[6], group_014.inputs[3])
            # group_input_7.Material -> group_026.Material
            style_spheres.links.new(group_input_7.outputs[6], group_026.inputs[5])
            # join_geometry.Geometry -> group_output_7.Geometry
            style_spheres.links.new(join_geometry.outputs[0], group_output_7.inputs[0])
            # realize_instances_1.Geometry -> join_geometry.Geometry
            style_spheres.links.new(
                realize_instances_1.outputs[0], join_geometry.inputs[0]
            )
            # group_026.Instances -> realize_instances_1.Geometry
            style_spheres.links.new(group_026.outputs[0], realize_instances_1.inputs[0])
            # separate_geometry_2.Inverted -> group_014.Atoms
            style_spheres.links.new(separate_geometry_2.outputs[1], group_014.inputs[0])
            # separate_geometry_2.Selection -> group_026.Atoms
            style_spheres.links.new(separate_geometry_2.outputs[0], group_026.inputs[0])
            # group_014.Point Cloud -> join_geometry.Geometry
            style_spheres.links.new(group_014.outputs[0], join_geometry.inputs[0])
            return style_spheres

        style_spheres = style_spheres_node_group()

        # initialize style_ball_and_stick node group
        def style_ball_and_stick_node_group():
            style_ball_and_stick = bpy.data.node_groups.new(
                type="GeometryNodeTree", name="Style Ball and Stick"
            )

            style_ball_and_stick.color_tag = "GEOMETRY"
            style_ball_and_stick.description = ""

            style_ball_and_stick.is_modifier = True

            # style_ball_and_stick interface
            # Socket Geometry
            geometry_socket_2 = style_ball_and_stick.interface.new_socket(
                name="Geometry", in_out="OUTPUT", socket_type="NodeSocketGeometry"
            )
            geometry_socket_2.attribute_domain = "POINT"

            # Socket Atoms
            atoms_socket_8 = style_ball_and_stick.interface.new_socket(
                name="Atoms", in_out="INPUT", socket_type="NodeSocketGeometry"
            )
            atoms_socket_8.attribute_domain = "POINT"
            atoms_socket_8.description = (
                "Atomic geometry that contains vertices and edges"
            )

            # Socket Quality
            quality_socket = style_ball_and_stick.interface.new_socket(
                name="Quality", in_out="INPUT", socket_type="NodeSocketInt"
            )
            quality_socket.subtype = "NONE"
            quality_socket.default_value = 2
            quality_socket.min_value = 0
            quality_socket.max_value = 2147483647
            quality_socket.attribute_domain = "POINT"
            quality_socket.force_non_field = True

            # Socket Selection
            selection_socket_6 = style_ball_and_stick.interface.new_socket(
                name="Selection", in_out="INPUT", socket_type="NodeSocketBool"
            )
            selection_socket_6.attribute_domain = "POINT"
            selection_socket_6.hide_value = True
            selection_socket_6.description = "Selection of atoms to apply this style to"

            # Panel Sphere
            sphere_panel_1 = style_ball_and_stick.interface.new_panel(
                "Sphere", default_closed=True
            )
            # Socket Sphere As Mesh
            sphere_as_mesh_socket_1 = style_ball_and_stick.interface.new_socket(
                name="Sphere As Mesh",
                in_out="INPUT",
                socket_type="NodeSocketBool",
                parent=sphere_panel_1,
            )
            sphere_as_mesh_socket_1.attribute_domain = "POINT"
            sphere_as_mesh_socket_1.description = "Render spheres as point clouds"

            # Socket Sphere Radii
            sphere_radii_socket_1 = style_ball_and_stick.interface.new_socket(
                name="Sphere Radii",
                in_out="INPUT",
                socket_type="NodeSocketFloat",
                parent=sphere_panel_1,
            )
            sphere_radii_socket_1.subtype = "NONE"
            sphere_radii_socket_1.default_value = 0.30000001192092896
            sphere_radii_socket_1.min_value = 0.0
            sphere_radii_socket_1.max_value = 10000.0
            sphere_radii_socket_1.attribute_domain = "POINT"
            sphere_radii_socket_1.description = "Scale the sphere radii"

            # Panel Bond
            bond_panel = style_ball_and_stick.interface.new_panel(
                "Bond", default_closed=True
            )
            # Socket Bond Find
            bond_find_socket = style_ball_and_stick.interface.new_socket(
                name="Bond Find",
                in_out="INPUT",
                socket_type="NodeSocketBool",
                parent=bond_panel,
            )
            bond_find_socket.attribute_domain = "POINT"
            bond_find_socket.description = "Find possible bonds for the selected atoms based on a distance search. Unselected atoms maintain any bonds they already have"

            # Socket Bond Radius
            bond_radius_socket = style_ball_and_stick.interface.new_socket(
                name="Bond Radius",
                in_out="INPUT",
                socket_type="NodeSocketFloat",
                parent=bond_panel,
            )
            bond_radius_socket.subtype = "NONE"
            bond_radius_socket.default_value = 0.30000001192092896
            bond_radius_socket.min_value = 0.0
            bond_radius_socket.max_value = 1.0
            bond_radius_socket.attribute_domain = "POINT"

            # Panel Material
            material_panel_2 = style_ball_and_stick.interface.new_panel(
                "Material", default_closed=True
            )
            # Socket Color Blur
            color_blur_socket = style_ball_and_stick.interface.new_socket(
                name="Color Blur",
                in_out="INPUT",
                socket_type="NodeSocketBool",
                parent=material_panel_2,
            )
            color_blur_socket.attribute_domain = "POINT"

            # Socket Shade Smooth
            shade_smooth_socket_3 = style_ball_and_stick.interface.new_socket(
                name="Shade Smooth",
                in_out="INPUT",
                socket_type="NodeSocketBool",
                parent=material_panel_2,
            )
            shade_smooth_socket_3.attribute_domain = "POINT"
            shade_smooth_socket_3.description = (
                "Apply smooth shading to the created geometry"
            )

            # Socket Material
            material_socket_4 = style_ball_and_stick.interface.new_socket(
                name="Material",
                in_out="INPUT",
                socket_type="NodeSocketMaterial",
                parent=material_panel_2,
            )
            material_socket_4.attribute_domain = "POINT"
            material_socket_4.description = (
                "Material to apply to the resulting geometry"
            )

            # initialize style_ball_and_stick nodes
            # node Group Output
            group_output_8 = style_ball_and_stick.nodes.new("NodeGroupOutput")
            group_output_8.name = "Group Output"
            group_output_8.is_active_output = True

            # node Join Geometry.001
            join_geometry_001 = style_ball_and_stick.nodes.new(
                "GeometryNodeJoinGeometry"
            )
            join_geometry_001.name = "Join Geometry.001"

            # node Group Input.002
            group_input_002_2 = style_ball_and_stick.nodes.new("NodeGroupInput")
            group_input_002_2.name = "Group Input.002"

            # node Separate Geometry
            separate_geometry_3 = style_ball_and_stick.nodes.new(
                "GeometryNodeSeparateGeometry"
            )
            separate_geometry_3.name = "Separate Geometry"
            separate_geometry_3.domain = "POINT"

            # node Group Input
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

            # node Group.009
            group_009 = style_ball_and_stick.nodes.new("GeometryNodeGroup")
            group_009.name = "Group.009"
            group_009.node_tree = _mn_utils_style_sticks
            # Socket_0
            group_009.inputs[1].default_value = True
            # Input_15
            group_009.inputs[4].default_value = False

            # node Topology Find Bonds
            topology_find_bonds_1 = style_ball_and_stick.nodes.new("GeometryNodeGroup")
            topology_find_bonds_1.label = "Topology Find Bonds"
            topology_find_bonds_1.name = "Topology Find Bonds"
            topology_find_bonds_1.node_tree = topology_find_bonds
            # Input_35
            topology_find_bonds_1.inputs[1].default_value = True
            # Input_2
            topology_find_bonds_1.inputs[2].default_value = 1.0

            # node Separate Geometry.002
            separate_geometry_002 = style_ball_and_stick.nodes.new(
                "GeometryNodeSeparateGeometry"
            )
            separate_geometry_002.name = "Separate Geometry.002"
            separate_geometry_002.domain = "POINT"

            # node Join Geometry.002
            join_geometry_002 = style_ball_and_stick.nodes.new(
                "GeometryNodeJoinGeometry"
            )
            join_geometry_002.name = "Join Geometry.002"

            # node Math
            math_4 = style_ball_and_stick.nodes.new("ShaderNodeMath")
            math_4.name = "Math"
            math_4.operation = "MULTIPLY"
            math_4.use_clamp = False
            # Value_001
            math_4.inputs[1].default_value = 6.0

            # node Group
            group_3 = style_ball_and_stick.nodes.new("GeometryNodeGroup")
            group_3.name = "Group"
            group_3.node_tree = style_spheres
            # Input_1
            group_3.inputs[1].default_value = True

            # node Group Input.001
            group_input_001_3 = style_ball_and_stick.nodes.new("NodeGroupInput")
            group_input_001_3.name = "Group Input.001"
            group_input_001_3.outputs[0].hide = True
            group_input_001_3.outputs[2].hide = True
            group_input_001_3.outputs[5].hide = True
            group_input_001_3.outputs[6].hide = True
            group_input_001_3.outputs[7].hide = True
            group_input_001_3.outputs[10].hide = True

            # Set locations
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

            # initialize style_ball_and_stick links
            # join_geometry_002.Geometry -> group_009.Atoms
            style_ball_and_stick.links.new(
                join_geometry_002.outputs[0], group_009.inputs[0]
            )
            # group_input_8.Atoms -> separate_geometry_3.Geometry
            style_ball_and_stick.links.new(
                group_input_8.outputs[0], separate_geometry_3.inputs[0]
            )
            # group_input_8.Selection -> separate_geometry_3.Selection
            style_ball_and_stick.links.new(
                group_input_8.outputs[2], separate_geometry_3.inputs[1]
            )
            # group_009.Geometry -> join_geometry_001.Geometry
            style_ball_and_stick.links.new(
                group_009.outputs[0], join_geometry_001.inputs[0]
            )
            # join_geometry_001.Geometry -> group_output_8.Geometry
            style_ball_and_stick.links.new(
                join_geometry_001.outputs[0], group_output_8.inputs[0]
            )
            # group_input_002_2.Material -> group_009.Material
            style_ball_and_stick.links.new(
                group_input_002_2.outputs[9], group_009.inputs[7]
            )
            # group_input_002_2.Shade Smooth -> group_009.Shade Smooth
            style_ball_and_stick.links.new(
                group_input_002_2.outputs[8], group_009.inputs[6]
            )
            # group_input_002_2.Bond Radius -> group_009.Radius
            style_ball_and_stick.links.new(
                group_input_002_2.outputs[6], group_009.inputs[2]
            )
            # separate_geometry_3.Selection -> separate_geometry_002.Geometry
            style_ball_and_stick.links.new(
                separate_geometry_3.outputs[0], separate_geometry_002.inputs[0]
            )
            # separate_geometry_002.Selection -> topology_find_bonds_1.Atoms
            style_ball_and_stick.links.new(
                separate_geometry_002.outputs[0], topology_find_bonds_1.inputs[0]
            )
            # group_input_002_2.Bond Find -> separate_geometry_002.Selection
            style_ball_and_stick.links.new(
                group_input_002_2.outputs[5], separate_geometry_002.inputs[1]
            )
            # separate_geometry_002.Inverted -> join_geometry_002.Geometry
            style_ball_and_stick.links.new(
                separate_geometry_002.outputs[1], join_geometry_002.inputs[0]
            )
            # group_input_002_2.Quality -> math_4.Value
            style_ball_and_stick.links.new(
                group_input_002_2.outputs[1], math_4.inputs[0]
            )
            # math_4.Value -> group_009.Resolution
            style_ball_and_stick.links.new(math_4.outputs[0], group_009.inputs[3])
            # separate_geometry_3.Selection -> group_3.Atoms
            style_ball_and_stick.links.new(
                separate_geometry_3.outputs[0], group_3.inputs[0]
            )
            # group_input_001_3.Quality -> group_3.Sphere Subdivisions
            style_ball_and_stick.links.new(
                group_input_001_3.outputs[1], group_3.inputs[4]
            )
            # group_input_001_3.Sphere As Mesh -> group_3.Sphere As Mesh
            style_ball_and_stick.links.new(
                group_input_001_3.outputs[3], group_3.inputs[2]
            )
            # group_input_001_3.Sphere Radii -> group_3.Sphere Radii
            style_ball_and_stick.links.new(
                group_input_001_3.outputs[4], group_3.inputs[3]
            )
            # group_input_001_3.Shade Smooth -> group_3.Shade Smooth
            style_ball_and_stick.links.new(
                group_input_001_3.outputs[8], group_3.inputs[5]
            )
            # group_input_001_3.Material -> group_3.Material
            style_ball_and_stick.links.new(
                group_input_001_3.outputs[9], group_3.inputs[6]
            )
            # group_input_002_2.Color Blur -> group_009.Interpolate Color
            style_ball_and_stick.links.new(
                group_input_002_2.outputs[7], group_009.inputs[5]
            )
            # group_3.Geometry -> join_geometry_001.Geometry
            style_ball_and_stick.links.new(
                group_3.outputs[0], join_geometry_001.inputs[0]
            )
            # topology_find_bonds_1.Atoms -> join_geometry_002.Geometry
            style_ball_and_stick.links.new(
                topology_find_bonds_1.outputs[0], join_geometry_002.inputs[0]
            )
            return style_ball_and_stick

        style_ball_and_stick = style_ball_and_stick_node_group()

        # initialize animate_value node group
        def animate_value_node_group():
            animate_value = bpy.data.node_groups.new(
                type="GeometryNodeTree", name="Animate Value"
            )

            animate_value.color_tag = "INPUT"
            animate_value.description = ""

            # animate_value interface
            # Socket Value
            value_socket_1 = animate_value.interface.new_socket(
                name="Value", in_out="OUTPUT", socket_type="NodeSocketFloat"
            )
            value_socket_1.subtype = "NONE"
            value_socket_1.default_value = 0.0
            value_socket_1.min_value = -3.4028234663852886e38
            value_socket_1.max_value = 3.4028234663852886e38
            value_socket_1.attribute_domain = "POINT"
            value_socket_1.description = (
                "Animated value that interpolates from min to max over frames"
            )

            # Socket Smoother Step
            smoother_step_socket = animate_value.interface.new_socket(
                name="Smoother Step", in_out="INPUT", socket_type="NodeSocketBool"
            )
            smoother_step_socket.attribute_domain = "POINT"
            smoother_step_socket.description = (
                "Ease out and in from the min and max values"
            )

            # Socket Clamped
            clamped_socket = animate_value.interface.new_socket(
                name="Clamped", in_out="INPUT", socket_type="NodeSocketBool"
            )
            clamped_socket.attribute_domain = "POINT"
            clamped_socket.description = (
                "Whether to clamp the interpolated value to the max"
            )

            # Panel Frame
            frame_panel = animate_value.interface.new_panel("Frame")
            # Socket Frame Start
            frame_start_socket = animate_value.interface.new_socket(
                name="Frame Start",
                in_out="INPUT",
                socket_type="NodeSocketInt",
                parent=frame_panel,
            )
            frame_start_socket.subtype = "NONE"
            frame_start_socket.default_value = 1
            frame_start_socket.min_value = 1
            frame_start_socket.max_value = 2147483647
            frame_start_socket.attribute_domain = "POINT"
            frame_start_socket.description = "Frame to start the animation on"

            # Socket Frame End
            frame_end_socket = animate_value.interface.new_socket(
                name="Frame End",
                in_out="INPUT",
                socket_type="NodeSocketInt",
                parent=frame_panel,
            )
            frame_end_socket.subtype = "NONE"
            frame_end_socket.default_value = 250
            frame_end_socket.min_value = 1
            frame_end_socket.max_value = 2147483647
            frame_end_socket.attribute_domain = "POINT"
            frame_end_socket.description = "Frame to finish the animation on"

            # Panel Value
            value_panel = animate_value.interface.new_panel("Value")
            # Socket Value Min
            value_min_socket = animate_value.interface.new_socket(
                name="Value Min",
                in_out="INPUT",
                socket_type="NodeSocketFloat",
                parent=value_panel,
            )
            value_min_socket.subtype = "NONE"
            value_min_socket.default_value = 0.0
            value_min_socket.min_value = -10000.0
            value_min_socket.max_value = 10000.0
            value_min_socket.attribute_domain = "POINT"
            value_min_socket.description = "Value to start animation from"

            # Socket Value Max
            value_max_socket = animate_value.interface.new_socket(
                name="Value Max",
                in_out="INPUT",
                socket_type="NodeSocketFloat",
                parent=value_panel,
            )
            value_max_socket.subtype = "NONE"
            value_max_socket.default_value = 1.0
            value_max_socket.min_value = -10000.0
            value_max_socket.max_value = 10000.0
            value_max_socket.attribute_domain = "POINT"
            value_max_socket.description = "Value to end animation at"

            # initialize animate_value nodes
            # node Group Input
            group_input_9 = animate_value.nodes.new("NodeGroupInput")
            group_input_9.name = "Group Input"

            # node Scene Time
            scene_time = animate_value.nodes.new("GeometryNodeInputSceneTime")
            scene_time.name = "Scene Time"

            # node Map Range.002
            map_range_002 = animate_value.nodes.new("ShaderNodeMapRange")
            map_range_002.name = "Map Range.002"
            map_range_002.clamp = True
            map_range_002.data_type = "FLOAT"
            map_range_002.interpolation_type = "LINEAR"

            # node Map Range
            map_range = animate_value.nodes.new("ShaderNodeMapRange")
            map_range.name = "Map Range"
            map_range.clamp = False
            map_range.data_type = "FLOAT"
            map_range.interpolation_type = "LINEAR"

            # node Switch.001
            switch_001_1 = animate_value.nodes.new("GeometryNodeSwitch")
            switch_001_1.name = "Switch.001"
            switch_001_1.input_type = "FLOAT"

            # node Group Output
            group_output_9 = animate_value.nodes.new("NodeGroupOutput")
            group_output_9.name = "Group Output"
            group_output_9.is_active_output = True

            # node Map Range.001
            map_range_001 = animate_value.nodes.new("ShaderNodeMapRange")
            map_range_001.name = "Map Range.001"
            map_range_001.clamp = False
            map_range_001.data_type = "FLOAT"
            map_range_001.interpolation_type = "SMOOTHERSTEP"

            # node Switch.002
            switch_002 = animate_value.nodes.new("GeometryNodeSwitch")
            switch_002.name = "Switch.002"
            switch_002.input_type = "FLOAT"

            # Set locations
            group_input_9.location = (-620.0, -180.0)
            scene_time.location = (-620.0, -80.0)
            map_range_002.location = (-60.0, 100.0)
            map_range.location = (-60.0, -160.0)
            switch_001_1.location = (120.0, 100.0)
            group_output_9.location = (779.9998779296875, 40.0)
            map_range_001.location = (-60.0, -420.0)
            switch_002.location = (349.49884033203125, 7.68292236328125)

            # initialize animate_value links
            # scene_time.Frame -> map_range.Value
            animate_value.links.new(scene_time.outputs[1], map_range.inputs[0])
            # group_input_9.Frame Start -> map_range.From Min
            animate_value.links.new(group_input_9.outputs[2], map_range.inputs[1])
            # group_input_9.Frame End -> map_range.From Max
            animate_value.links.new(group_input_9.outputs[3], map_range.inputs[2])
            # group_input_9.Value Min -> map_range.To Min
            animate_value.links.new(group_input_9.outputs[4], map_range.inputs[3])
            # group_input_9.Value Max -> map_range.To Max
            animate_value.links.new(group_input_9.outputs[5], map_range.inputs[4])
            # scene_time.Frame -> map_range_002.Value
            animate_value.links.new(scene_time.outputs[1], map_range_002.inputs[0])
            # group_input_9.Frame Start -> map_range_002.From Min
            animate_value.links.new(group_input_9.outputs[2], map_range_002.inputs[1])
            # group_input_9.Frame End -> map_range_002.From Max
            animate_value.links.new(group_input_9.outputs[3], map_range_002.inputs[2])
            # group_input_9.Value Min -> map_range_002.To Min
            animate_value.links.new(group_input_9.outputs[4], map_range_002.inputs[3])
            # group_input_9.Value Max -> map_range_002.To Max
            animate_value.links.new(group_input_9.outputs[5], map_range_002.inputs[4])
            # group_input_9.Clamped -> switch_001_1.Switch
            animate_value.links.new(group_input_9.outputs[1], switch_001_1.inputs[0])
            # map_range_002.Result -> switch_001_1.True
            animate_value.links.new(map_range_002.outputs[0], switch_001_1.inputs[2])
            # map_range.Result -> switch_001_1.False
            animate_value.links.new(map_range.outputs[0], switch_001_1.inputs[1])
            # scene_time.Frame -> map_range_001.Value
            animate_value.links.new(scene_time.outputs[1], map_range_001.inputs[0])
            # group_input_9.Frame Start -> map_range_001.From Min
            animate_value.links.new(group_input_9.outputs[2], map_range_001.inputs[1])
            # group_input_9.Frame End -> map_range_001.From Max
            animate_value.links.new(group_input_9.outputs[3], map_range_001.inputs[2])
            # group_input_9.Value Min -> map_range_001.To Min
            animate_value.links.new(group_input_9.outputs[4], map_range_001.inputs[3])
            # group_input_9.Value Max -> map_range_001.To Max
            animate_value.links.new(group_input_9.outputs[5], map_range_001.inputs[4])
            # map_range_001.Result -> switch_002.True
            animate_value.links.new(map_range_001.outputs[0], switch_002.inputs[2])
            # switch_001_1.Output -> switch_002.False
            animate_value.links.new(switch_001_1.outputs[0], switch_002.inputs[1])
            # group_input_9.Smoother Step -> switch_002.Switch
            animate_value.links.new(group_input_9.outputs[0], switch_002.inputs[0])
            # switch_002.Output -> group_output_9.Value
            animate_value.links.new(switch_002.outputs[0], group_output_9.inputs[0])
            return animate_value

        animate_value = animate_value_node_group()

        # initialize _mn_animate_wiggle_mask_length node group
        def _mn_animate_wiggle_mask_length_node_group():
            _mn_animate_wiggle_mask_length = bpy.data.node_groups.new(
                type="GeometryNodeTree", name=".MN_animate_wiggle_mask_length"
            )

            _mn_animate_wiggle_mask_length.color_tag = "NONE"
            _mn_animate_wiggle_mask_length.description = ""

            # _mn_animate_wiggle_mask_length interface
            # Socket Result
            result_socket = _mn_animate_wiggle_mask_length.interface.new_socket(
                name="Result", in_out="OUTPUT", socket_type="NodeSocketInt"
            )
            result_socket.subtype = "NONE"
            result_socket.default_value = 0
            result_socket.min_value = -2147483648
            result_socket.max_value = 2147483647
            result_socket.attribute_domain = "POINT"

            # Socket A
            a_socket = _mn_animate_wiggle_mask_length.interface.new_socket(
                name="A", in_out="INPUT", socket_type="NodeSocketInt"
            )
            a_socket.subtype = "NONE"
            a_socket.default_value = 0
            a_socket.min_value = -2147483648
            a_socket.max_value = 2147483647
            a_socket.attribute_domain = "POINT"

            # initialize _mn_animate_wiggle_mask_length nodes
            # node Group Output
            group_output_10 = _mn_animate_wiggle_mask_length.nodes.new(
                "NodeGroupOutput"
            )
            group_output_10.name = "Group Output"
            group_output_10.is_active_output = True

            # node Group Input
            group_input_10 = _mn_animate_wiggle_mask_length.nodes.new("NodeGroupInput")
            group_input_10.name = "Group Input"

            # node Index Switch
            index_switch = _mn_animate_wiggle_mask_length.nodes.new(
                "GeometryNodeIndexSwitch"
            )
            index_switch.name = "Index Switch"
            index_switch.data_type = "INT"
            index_switch.index_switch_items.clear()
            index_switch.index_switch_items.new()
            index_switch.index_switch_items.new()
            index_switch.index_switch_items.new()
            index_switch.index_switch_items.new()
            index_switch.index_switch_items.new()
            # Item_0
            index_switch.inputs[1].default_value = 2
            # Item_1
            index_switch.inputs[2].default_value = 5
            # Item_2
            index_switch.inputs[3].default_value = 6
            # Item_3
            index_switch.inputs[4].default_value = 12
            # Item_4
            index_switch.inputs[5].default_value = 20

            # Set locations
            group_output_10.location = (80.0, 560.0)
            group_input_10.location = (-300.0, 560.0)
            index_switch.location = (-120.55677795410156, 554.9675903320312)

            # initialize _mn_animate_wiggle_mask_length links
            # group_input_10.A -> index_switch.Index
            _mn_animate_wiggle_mask_length.links.new(
                group_input_10.outputs[0], index_switch.inputs[0]
            )
            # index_switch.Output -> group_output_10.Result
            _mn_animate_wiggle_mask_length.links.new(
                index_switch.outputs[0], group_output_10.inputs[0]
            )
            return _mn_animate_wiggle_mask_length

        _mn_animate_wiggle_mask_length = _mn_animate_wiggle_mask_length_node_group()

        # initialize mn_animate_noise_repeat node group
        def mn_animate_noise_repeat_node_group():
            mn_animate_noise_repeat = bpy.data.node_groups.new(
                type="GeometryNodeTree", name="MN_animate_noise_repeat"
            )

            mn_animate_noise_repeat.color_tag = "TEXTURE"
            mn_animate_noise_repeat.description = ""

            # mn_animate_noise_repeat interface
            # Socket Noise Float
            noise_float_socket = mn_animate_noise_repeat.interface.new_socket(
                name="Noise Float", in_out="OUTPUT", socket_type="NodeSocketFloat"
            )
            noise_float_socket.subtype = "NONE"
            noise_float_socket.default_value = 0.0
            noise_float_socket.min_value = -3.4028234663852886e38
            noise_float_socket.max_value = 3.4028234663852886e38
            noise_float_socket.attribute_domain = "POINT"

            # Socket Noise Vector
            noise_vector_socket = mn_animate_noise_repeat.interface.new_socket(
                name="Noise Vector", in_out="OUTPUT", socket_type="NodeSocketVector"
            )
            noise_vector_socket.subtype = "NONE"
            noise_vector_socket.default_value = (0.0, 0.0, 0.0)
            noise_vector_socket.min_value = -3.4028234663852886e38
            noise_vector_socket.max_value = 3.4028234663852886e38
            noise_vector_socket.attribute_domain = "POINT"

            # Socket Amplitude
            amplitude_socket = mn_animate_noise_repeat.interface.new_socket(
                name="Amplitude", in_out="INPUT", socket_type="NodeSocketFloat"
            )
            amplitude_socket.subtype = "NONE"
            amplitude_socket.default_value = 1.0
            amplitude_socket.min_value = -10000.0
            amplitude_socket.max_value = 10000.0
            amplitude_socket.attribute_domain = "POINT"

            # Socket Detail
            detail_socket = mn_animate_noise_repeat.interface.new_socket(
                name="Detail", in_out="INPUT", socket_type="NodeSocketFloat"
            )
            detail_socket.subtype = "NONE"
            detail_socket.default_value = 0.5
            detail_socket.min_value = 0.0
            detail_socket.max_value = 15.0
            detail_socket.attribute_domain = "POINT"

            # Socket Roughness
            roughness_socket = mn_animate_noise_repeat.interface.new_socket(
                name="Roughness", in_out="INPUT", socket_type="NodeSocketFloat"
            )
            roughness_socket.subtype = "FACTOR"
            roughness_socket.default_value = 0.5
            roughness_socket.min_value = 0.0
            roughness_socket.max_value = 1.0
            roughness_socket.attribute_domain = "POINT"

            # Socket Distortion
            distortion_socket = mn_animate_noise_repeat.interface.new_socket(
                name="Distortion", in_out="INPUT", socket_type="NodeSocketFloat"
            )
            distortion_socket.subtype = "NONE"
            distortion_socket.default_value = 0.0
            distortion_socket.min_value = -1000.0
            distortion_socket.max_value = 1000.0
            distortion_socket.attribute_domain = "POINT"

            # Socket Vector
            vector_socket = mn_animate_noise_repeat.interface.new_socket(
                name="Vector", in_out="INPUT", socket_type="NodeSocketVector"
            )
            vector_socket.subtype = "NONE"
            vector_socket.default_value = (0.0, 0.0, 0.0)
            vector_socket.min_value = -10000.0
            vector_socket.max_value = 10000.0
            vector_socket.default_attribute_name = "position"
            vector_socket.attribute_domain = "POINT"
            vector_socket.hide_value = True

            # Socket Speed
            speed_socket = mn_animate_noise_repeat.interface.new_socket(
                name="Speed", in_out="INPUT", socket_type="NodeSocketFloat"
            )
            speed_socket.subtype = "NONE"
            speed_socket.default_value = 0.5
            speed_socket.min_value = -10000.0
            speed_socket.max_value = 10000.0
            speed_socket.attribute_domain = "POINT"

            # Socket Animate 0..1
            animate_0__1_socket = mn_animate_noise_repeat.interface.new_socket(
                name="Animate 0..1", in_out="INPUT", socket_type="NodeSocketFloat"
            )
            animate_0__1_socket.subtype = "NONE"
            animate_0__1_socket.default_value = 0.5
            animate_0__1_socket.min_value = -10000.0
            animate_0__1_socket.max_value = 10000.0
            animate_0__1_socket.attribute_domain = "POINT"

            # initialize mn_animate_noise_repeat nodes
            # node Combine XYZ
            combine_xyz = mn_animate_noise_repeat.nodes.new("ShaderNodeCombineXYZ")
            combine_xyz.name = "Combine XYZ"
            # Y
            combine_xyz.inputs[1].default_value = 0.0
            # Z
            combine_xyz.inputs[2].default_value = 0.0

            # node Vector Math.003
            vector_math_003 = mn_animate_noise_repeat.nodes.new("ShaderNodeVectorMath")
            vector_math_003.name = "Vector Math.003"
            vector_math_003.operation = "SCALE"

            # node Math
            math_5 = mn_animate_noise_repeat.nodes.new("ShaderNodeMath")
            math_5.name = "Math"
            math_5.operation = "DIVIDE"
            math_5.use_clamp = False
            # Value
            math_5.inputs[0].default_value = 6.2831854820251465

            # node Math.003
            math_003_1 = mn_animate_noise_repeat.nodes.new("ShaderNodeMath")
            math_003_1.name = "Math.003"
            math_003_1.operation = "COSINE"
            math_003_1.use_clamp = False

            # node Math.002
            math_002_1 = mn_animate_noise_repeat.nodes.new("ShaderNodeMath")
            math_002_1.name = "Math.002"
            math_002_1.operation = "SINE"
            math_002_1.use_clamp = False

            # node Math.004
            math_004 = mn_animate_noise_repeat.nodes.new("ShaderNodeMath")
            math_004.name = "Math.004"
            math_004.operation = "SINE"
            math_004.use_clamp = False

            # node Separate XYZ
            separate_xyz = mn_animate_noise_repeat.nodes.new("ShaderNodeSeparateXYZ")
            separate_xyz.name = "Separate XYZ"

            # node Math.005
            math_005 = mn_animate_noise_repeat.nodes.new("ShaderNodeMath")
            math_005.name = "Math.005"
            math_005.operation = "COSINE"
            math_005.use_clamp = False

            # node Math.001
            math_001_3 = mn_animate_noise_repeat.nodes.new("ShaderNodeMath")
            math_001_3.name = "Math.001"
            math_001_3.operation = "MULTIPLY"
            math_001_3.use_clamp = False

            # node Value.001
            value_001 = mn_animate_noise_repeat.nodes.new("ShaderNodeValue")
            value_001.name = "Value.001"

            value_001.outputs[0].default_value = 0.20000000298023224
            # node Vector Math.002
            vector_math_002 = mn_animate_noise_repeat.nodes.new("ShaderNodeVectorMath")
            vector_math_002.name = "Vector Math.002"
            vector_math_002.operation = "ADD"

            # node Group Output
            group_output_11 = mn_animate_noise_repeat.nodes.new("NodeGroupOutput")
            group_output_11.name = "Group Output"
            group_output_11.is_active_output = True

            # node Math.006
            math_006 = mn_animate_noise_repeat.nodes.new("ShaderNodeMath")
            math_006.name = "Math.006"
            math_006.operation = "MULTIPLY"
            math_006.use_clamp = False

            # node Vector Math
            vector_math_1 = mn_animate_noise_repeat.nodes.new("ShaderNodeVectorMath")
            vector_math_1.name = "Vector Math"
            vector_math_1.operation = "SCALE"

            # node Map Range
            map_range_1 = mn_animate_noise_repeat.nodes.new("ShaderNodeMapRange")
            map_range_1.name = "Map Range"
            map_range_1.clamp = True
            map_range_1.data_type = "FLOAT"
            map_range_1.interpolation_type = "LINEAR"
            # From Min
            map_range_1.inputs[1].default_value = 0.0
            # From Max
            map_range_1.inputs[2].default_value = 1.0
            # To Min
            map_range_1.inputs[3].default_value = -1.0
            # To Max
            map_range_1.inputs[4].default_value = 1.0

            # node Map Range.001
            map_range_001_1 = mn_animate_noise_repeat.nodes.new("ShaderNodeMapRange")
            map_range_001_1.name = "Map Range.001"
            map_range_001_1.clamp = True
            map_range_001_1.data_type = "FLOAT_VECTOR"
            map_range_001_1.interpolation_type = "LINEAR"
            # From_Min_FLOAT3
            map_range_001_1.inputs[7].default_value = (0.0, 0.0, 0.0)
            # From_Max_FLOAT3
            map_range_001_1.inputs[8].default_value = (1.0, 1.0, 1.0)
            # To_Min_FLOAT3
            map_range_001_1.inputs[9].default_value = (-1.0, -1.0, -1.0)
            # To_Max_FLOAT3
            map_range_001_1.inputs[10].default_value = (1.0, 1.0, 1.0)

            # node Noise Texture
            noise_texture = mn_animate_noise_repeat.nodes.new("ShaderNodeTexNoise")
            noise_texture.name = "Noise Texture"
            noise_texture.noise_dimensions = "4D"
            noise_texture.noise_type = "FBM"
            noise_texture.normalize = True
            # Lacunarity
            noise_texture.inputs[5].default_value = 2.0

            # node Combine XYZ.001
            combine_xyz_001 = mn_animate_noise_repeat.nodes.new("ShaderNodeCombineXYZ")
            combine_xyz_001.name = "Combine XYZ.001"

            # node Value
            value_1 = mn_animate_noise_repeat.nodes.new("ShaderNodeValue")
            value_1.name = "Value"

            value_1.outputs[0].default_value = 4.0
            # node Random Value
            random_value = mn_animate_noise_repeat.nodes.new("FunctionNodeRandomValue")
            random_value.name = "Random Value"
            random_value.data_type = "FLOAT_VECTOR"
            # Min
            random_value.inputs[0].default_value = (-10.0, -10.0, -10.0)
            # Max
            random_value.inputs[1].default_value = (-1.0, 10.0, 10.0)
            # Seed
            random_value.inputs[8].default_value = 0

            # node Math.009
            math_009 = mn_animate_noise_repeat.nodes.new("ShaderNodeMath")
            math_009.name = "Math.009"
            math_009.operation = "MULTIPLY"
            math_009.use_clamp = False

            # node Vector Math.001
            vector_math_001 = mn_animate_noise_repeat.nodes.new("ShaderNodeVectorMath")
            vector_math_001.name = "Vector Math.001"
            vector_math_001.operation = "ADD"

            # node Reroute
            reroute_2 = mn_animate_noise_repeat.nodes.new("NodeReroute")
            reroute_2.name = "Reroute"
            # node Group Input
            group_input_11 = mn_animate_noise_repeat.nodes.new("NodeGroupInput")
            group_input_11.name = "Group Input"

            # node Clamp
            clamp = mn_animate_noise_repeat.nodes.new("ShaderNodeClamp")
            clamp.name = "Clamp"
            clamp.hide = True
            clamp.clamp_type = "MINMAX"
            # Min
            clamp.inputs[1].default_value = 0.0
            # Max
            clamp.inputs[2].default_value = 1.0

            # Set locations
            combine_xyz.location = (0.0001220703125, 110.0)
            vector_math_003.location = (320.0001220703125, 190.0)
            math_5.location = (160.0, 40.0)
            math_003_1.location = (700.0, 240.0)
            math_002_1.location = (700.0, 380.0)
            math_004.location = (700.0, 100.0)
            separate_xyz.location = (480.0001220703125, 190.0)
            math_005.location = (700.0, -40.0)
            math_001_3.location = (164.15023803710938, -158.06997680664062)
            value_001.location = (-480.0, -320.0)
            vector_math_002.location = (160.0001220703125, 190.0)
            group_output_11.location = (1768.860595703125, 286.24639892578125)
            math_006.location = (1543.8201904296875, 306.56878662109375)
            vector_math_1.location = (1543.8201904296875, 146.56878662109375)
            map_range_1.location = (1340.0, 300.0)
            map_range_001_1.location = (1340.0, 40.0)
            noise_texture.location = (1142.486328125, 289.14031982421875)
            combine_xyz_001.location = (880.0, 300.0)
            value_1.location = (-480.0, -228.98846435546875)
            random_value.location = (-146.0265655517578, 430.21173095703125)
            math_009.location = (-159.9998779296875, 110.0)
            vector_math_001.location = (45.413909912109375, 436.6630859375)
            reroute_2.location = (-200.3484344482422, -201.43125915527344)
            group_input_11.location = (-480.0, 0.0)
            clamp.location = (1142.486328125, -10.85968017578125)

            # initialize mn_animate_noise_repeat links
            # math_009.Value -> combine_xyz.X
            mn_animate_noise_repeat.links.new(
                math_009.outputs[0], combine_xyz.inputs[0]
            )
            # combine_xyz.Vector -> vector_math_002.Vector
            mn_animate_noise_repeat.links.new(
                combine_xyz.outputs[0], vector_math_002.inputs[1]
            )
            # vector_math_003.Vector -> separate_xyz.Vector
            mn_animate_noise_repeat.links.new(
                vector_math_003.outputs[0], separate_xyz.inputs[0]
            )
            # reroute_2.Output -> math_5.Value
            mn_animate_noise_repeat.links.new(reroute_2.outputs[0], math_5.inputs[1])
            # math_5.Value -> vector_math_003.Scale
            mn_animate_noise_repeat.links.new(
                math_5.outputs[0], vector_math_003.inputs[3]
            )
            # reroute_2.Output -> math_001_3.Value
            mn_animate_noise_repeat.links.new(
                reroute_2.outputs[0], math_001_3.inputs[0]
            )
            # value_001.Value -> math_001_3.Value
            mn_animate_noise_repeat.links.new(
                value_001.outputs[0], math_001_3.inputs[1]
            )
            # separate_xyz.X -> math_002_1.Value
            mn_animate_noise_repeat.links.new(
                separate_xyz.outputs[0], math_002_1.inputs[0]
            )
            # separate_xyz.X -> math_003_1.Value
            mn_animate_noise_repeat.links.new(
                separate_xyz.outputs[0], math_003_1.inputs[0]
            )
            # math_002_1.Value -> combine_xyz_001.X
            mn_animate_noise_repeat.links.new(
                math_002_1.outputs[0], combine_xyz_001.inputs[0]
            )
            # math_003_1.Value -> combine_xyz_001.Y
            mn_animate_noise_repeat.links.new(
                math_003_1.outputs[0], combine_xyz_001.inputs[1]
            )
            # separate_xyz.Y -> math_004.Value
            mn_animate_noise_repeat.links.new(
                separate_xyz.outputs[1], math_004.inputs[0]
            )
            # math_004.Value -> combine_xyz_001.Z
            mn_animate_noise_repeat.links.new(
                math_004.outputs[0], combine_xyz_001.inputs[2]
            )
            # separate_xyz.Y -> math_005.Value
            mn_animate_noise_repeat.links.new(
                separate_xyz.outputs[1], math_005.inputs[0]
            )
            # math_005.Value -> noise_texture.W
            mn_animate_noise_repeat.links.new(
                math_005.outputs[0], noise_texture.inputs[1]
            )
            # math_001_3.Value -> noise_texture.Scale
            mn_animate_noise_repeat.links.new(
                math_001_3.outputs[0], noise_texture.inputs[2]
            )
            # noise_texture.Fac -> map_range_1.Value
            mn_animate_noise_repeat.links.new(
                noise_texture.outputs[0], map_range_1.inputs[0]
            )
            # map_range_1.Result -> math_006.Value
            mn_animate_noise_repeat.links.new(
                map_range_1.outputs[0], math_006.inputs[0]
            )
            # math_006.Value -> group_output_11.Noise Float
            mn_animate_noise_repeat.links.new(
                math_006.outputs[0], group_output_11.inputs[0]
            )
            # group_input_11.Amplitude -> math_006.Value
            mn_animate_noise_repeat.links.new(
                group_input_11.outputs[0], math_006.inputs[1]
            )
            # noise_texture.Color -> map_range_001_1.Vector
            mn_animate_noise_repeat.links.new(
                noise_texture.outputs[1], map_range_001_1.inputs[6]
            )
            # map_range_001_1.Vector -> vector_math_1.Vector
            mn_animate_noise_repeat.links.new(
                map_range_001_1.outputs[1], vector_math_1.inputs[0]
            )
            # group_input_11.Amplitude -> vector_math_1.Scale
            mn_animate_noise_repeat.links.new(
                group_input_11.outputs[0], vector_math_1.inputs[3]
            )
            # vector_math_1.Vector -> group_output_11.Noise Vector
            mn_animate_noise_repeat.links.new(
                vector_math_1.outputs[0], group_output_11.inputs[1]
            )
            # group_input_11.Detail -> noise_texture.Detail
            mn_animate_noise_repeat.links.new(
                group_input_11.outputs[1], noise_texture.inputs[3]
            )
            # group_input_11.Distortion -> noise_texture.Distortion
            mn_animate_noise_repeat.links.new(
                group_input_11.outputs[3], noise_texture.inputs[8]
            )
            # group_input_11.Vector -> vector_math_002.Vector
            mn_animate_noise_repeat.links.new(
                group_input_11.outputs[4], vector_math_002.inputs[0]
            )
            # vector_math_002.Vector -> vector_math_001.Vector
            mn_animate_noise_repeat.links.new(
                vector_math_002.outputs[0], vector_math_001.inputs[0]
            )
            # random_value.Value -> vector_math_001.Vector
            mn_animate_noise_repeat.links.new(
                random_value.outputs[0], vector_math_001.inputs[1]
            )
            # vector_math_001.Vector -> vector_math_003.Vector
            mn_animate_noise_repeat.links.new(
                vector_math_001.outputs[0], vector_math_003.inputs[0]
            )
            # combine_xyz_001.Vector -> noise_texture.Vector
            mn_animate_noise_repeat.links.new(
                combine_xyz_001.outputs[0], noise_texture.inputs[0]
            )
            # reroute_2.Output -> math_009.Value
            mn_animate_noise_repeat.links.new(reroute_2.outputs[0], math_009.inputs[1])
            # group_input_11.Vector -> random_value.ID
            mn_animate_noise_repeat.links.new(
                group_input_11.outputs[4], random_value.inputs[7]
            )
            # group_input_11.Animate 0..1 -> math_009.Value
            mn_animate_noise_repeat.links.new(
                group_input_11.outputs[6], math_009.inputs[0]
            )
            # group_input_11.Speed -> reroute_2.Input
            mn_animate_noise_repeat.links.new(
                group_input_11.outputs[5], reroute_2.inputs[0]
            )
            # group_input_11.Roughness -> clamp.Value
            mn_animate_noise_repeat.links.new(
                group_input_11.outputs[2], clamp.inputs[0]
            )
            # clamp.Result -> noise_texture.Roughness
            mn_animate_noise_repeat.links.new(clamp.outputs[0], noise_texture.inputs[4])
            return mn_animate_noise_repeat

        mn_animate_noise_repeat = mn_animate_noise_repeat_node_group()

        # initialize _utils_group_field_at_selection node group
        def _utils_group_field_at_selection_node_group():
            _utils_group_field_at_selection = bpy.data.node_groups.new(
                type="GeometryNodeTree", name=".utils_group_field_at_selection"
            )

            _utils_group_field_at_selection.color_tag = "NONE"
            _utils_group_field_at_selection.description = ""

            # _utils_group_field_at_selection interface
            # Socket Group Index
            group_index_socket = _utils_group_field_at_selection.interface.new_socket(
                name="Group Index", in_out="OUTPUT", socket_type="NodeSocketInt"
            )
            group_index_socket.subtype = "NONE"
            group_index_socket.default_value = 0
            group_index_socket.min_value = -2147483648
            group_index_socket.max_value = 2147483647
            group_index_socket.attribute_domain = "POINT"

            # Socket Float
            float_socket = _utils_group_field_at_selection.interface.new_socket(
                name="Float", in_out="OUTPUT", socket_type="NodeSocketFloat"
            )
            float_socket.subtype = "NONE"
            float_socket.default_value = 0.0
            float_socket.min_value = -3.4028234663852886e38
            float_socket.max_value = 3.4028234663852886e38
            float_socket.attribute_domain = "POINT"

            # Socket Vector
            vector_socket_1 = _utils_group_field_at_selection.interface.new_socket(
                name="Vector", in_out="OUTPUT", socket_type="NodeSocketVector"
            )
            vector_socket_1.subtype = "NONE"
            vector_socket_1.default_value = (0.0, 0.0, 0.0)
            vector_socket_1.min_value = -3.4028234663852886e38
            vector_socket_1.max_value = 3.4028234663852886e38
            vector_socket_1.attribute_domain = "POINT"

            # Socket Boolean
            boolean_socket = _utils_group_field_at_selection.interface.new_socket(
                name="Boolean", in_out="OUTPUT", socket_type="NodeSocketBool"
            )
            boolean_socket.attribute_domain = "POINT"

            # Socket Color
            color_socket_1 = _utils_group_field_at_selection.interface.new_socket(
                name="Color", in_out="OUTPUT", socket_type="NodeSocketColor"
            )
            color_socket_1.attribute_domain = "POINT"

            # Socket Integer
            integer_socket = _utils_group_field_at_selection.interface.new_socket(
                name="Integer", in_out="OUTPUT", socket_type="NodeSocketInt"
            )
            integer_socket.subtype = "NONE"
            integer_socket.default_value = 0
            integer_socket.min_value = -2147483648
            integer_socket.max_value = 2147483647
            integer_socket.attribute_domain = "POINT"

            # Socket Selection
            selection_socket_7 = _utils_group_field_at_selection.interface.new_socket(
                name="Selection", in_out="INPUT", socket_type="NodeSocketBool"
            )
            selection_socket_7.attribute_domain = "POINT"
            selection_socket_7.description = "Selection of atoms to apply this node to"

            # Socket Group Index
            group_index_socket_1 = _utils_group_field_at_selection.interface.new_socket(
                name="Group Index", in_out="INPUT", socket_type="NodeSocketInt"
            )
            group_index_socket_1.subtype = "NONE"
            group_index_socket_1.default_value = 0
            group_index_socket_1.min_value = -2147483648
            group_index_socket_1.max_value = 2147483647
            group_index_socket_1.attribute_domain = "POINT"

            # Socket Float
            float_socket_1 = _utils_group_field_at_selection.interface.new_socket(
                name="Float", in_out="INPUT", socket_type="NodeSocketFloat"
            )
            float_socket_1.subtype = "NONE"
            float_socket_1.default_value = 0.0
            float_socket_1.min_value = -3.4028234663852886e38
            float_socket_1.max_value = 3.4028234663852886e38
            float_socket_1.attribute_domain = "POINT"
            float_socket_1.hide_value = True

            # Socket Vector
            vector_socket_2 = _utils_group_field_at_selection.interface.new_socket(
                name="Vector", in_out="INPUT", socket_type="NodeSocketVector"
            )
            vector_socket_2.subtype = "NONE"
            vector_socket_2.default_value = (0.0, 0.0, 0.0)
            vector_socket_2.min_value = -3.4028234663852886e38
            vector_socket_2.max_value = 3.4028234663852886e38
            vector_socket_2.attribute_domain = "POINT"
            vector_socket_2.hide_value = True

            # Socket Boolean
            boolean_socket_1 = _utils_group_field_at_selection.interface.new_socket(
                name="Boolean", in_out="INPUT", socket_type="NodeSocketBool"
            )
            boolean_socket_1.attribute_domain = "POINT"
            boolean_socket_1.hide_value = True

            # Socket Color
            color_socket_2 = _utils_group_field_at_selection.interface.new_socket(
                name="Color", in_out="INPUT", socket_type="NodeSocketColor"
            )
            color_socket_2.attribute_domain = "POINT"
            color_socket_2.hide_value = True

            # Socket Integer
            integer_socket_1 = _utils_group_field_at_selection.interface.new_socket(
                name="Integer", in_out="INPUT", socket_type="NodeSocketInt"
            )
            integer_socket_1.subtype = "NONE"
            integer_socket_1.default_value = 0
            integer_socket_1.min_value = -2147483648
            integer_socket_1.max_value = 2147483647
            integer_socket_1.attribute_domain = "POINT"
            integer_socket_1.hide_value = True

            # initialize _utils_group_field_at_selection nodes
            # node Switch.006
            switch_006 = _utils_group_field_at_selection.nodes.new("GeometryNodeSwitch")
            switch_006.name = "Switch.006"
            switch_006.input_type = "INT"
            # False
            switch_006.inputs[1].default_value = 0

            # node Accumulate Field.002
            accumulate_field_002 = _utils_group_field_at_selection.nodes.new(
                "GeometryNodeAccumulateField"
            )
            accumulate_field_002.name = "Accumulate Field.002"
            accumulate_field_002.data_type = "INT"
            accumulate_field_002.domain = "POINT"

            # node Index
            index_1 = _utils_group_field_at_selection.nodes.new(
                "GeometryNodeInputIndex"
            )
            index_1.name = "Index"

            # node Group Output
            group_output_12 = _utils_group_field_at_selection.nodes.new(
                "NodeGroupOutput"
            )
            group_output_12.name = "Group Output"
            group_output_12.is_active_output = True

            # node Field at Index
            field_at_index = _utils_group_field_at_selection.nodes.new(
                "GeometryNodeFieldAtIndex"
            )
            field_at_index.name = "Field at Index"
            field_at_index.data_type = "FLOAT"
            field_at_index.domain = "POINT"

            # node Field at Index.001
            field_at_index_001 = _utils_group_field_at_selection.nodes.new(
                "GeometryNodeFieldAtIndex"
            )
            field_at_index_001.name = "Field at Index.001"
            field_at_index_001.data_type = "FLOAT_VECTOR"
            field_at_index_001.domain = "POINT"

            # node Field at Index.002
            field_at_index_002 = _utils_group_field_at_selection.nodes.new(
                "GeometryNodeFieldAtIndex"
            )
            field_at_index_002.name = "Field at Index.002"
            field_at_index_002.data_type = "BOOLEAN"
            field_at_index_002.domain = "POINT"

            # node Field at Index.003
            field_at_index_003 = _utils_group_field_at_selection.nodes.new(
                "GeometryNodeFieldAtIndex"
            )
            field_at_index_003.name = "Field at Index.003"
            field_at_index_003.data_type = "FLOAT_COLOR"
            field_at_index_003.domain = "POINT"

            # node Group Input
            group_input_12 = _utils_group_field_at_selection.nodes.new("NodeGroupInput")
            group_input_12.name = "Group Input"

            # node Field at Index.004
            field_at_index_004 = _utils_group_field_at_selection.nodes.new(
                "GeometryNodeFieldAtIndex"
            )
            field_at_index_004.name = "Field at Index.004"
            field_at_index_004.data_type = "INT"
            field_at_index_004.domain = "POINT"

            # Set locations
            switch_006.location = (-80.0, 80.0)
            accumulate_field_002.location = (80.0, 80.0)
            index_1.location = (-80.0, -80.0)
            group_output_12.location = (477.87579345703125, 6.6051177978515625)
            field_at_index.location = (280.0, -20.0)
            field_at_index_001.location = (280.0, -180.0)
            field_at_index_002.location = (280.0, -340.0)
            field_at_index_003.location = (280.0, -500.0)
            group_input_12.location = (-280.0, -0.0)
            field_at_index_004.location = (280.0, -660.0)

            # initialize _utils_group_field_at_selection links
            # group_input_12.Selection -> switch_006.Switch
            _utils_group_field_at_selection.links.new(
                group_input_12.outputs[0], switch_006.inputs[0]
            )
            # accumulate_field_002.Total -> group_output_12.Group Index
            _utils_group_field_at_selection.links.new(
                accumulate_field_002.outputs[2], group_output_12.inputs[0]
            )
            # group_input_12.Group Index -> accumulate_field_002.Group ID
            _utils_group_field_at_selection.links.new(
                group_input_12.outputs[1], accumulate_field_002.inputs[1]
            )
            # index_1.Index -> switch_006.True
            _utils_group_field_at_selection.links.new(
                index_1.outputs[0], switch_006.inputs[2]
            )
            # switch_006.Output -> accumulate_field_002.Value
            _utils_group_field_at_selection.links.new(
                switch_006.outputs[0], accumulate_field_002.inputs[0]
            )
            # accumulate_field_002.Total -> field_at_index.Index
            _utils_group_field_at_selection.links.new(
                accumulate_field_002.outputs[2], field_at_index.inputs[0]
            )
            # group_input_12.Float -> field_at_index.Value
            _utils_group_field_at_selection.links.new(
                group_input_12.outputs[2], field_at_index.inputs[1]
            )
            # field_at_index.Value -> group_output_12.Float
            _utils_group_field_at_selection.links.new(
                field_at_index.outputs[0], group_output_12.inputs[1]
            )
            # accumulate_field_002.Total -> field_at_index_001.Index
            _utils_group_field_at_selection.links.new(
                accumulate_field_002.outputs[2], field_at_index_001.inputs[0]
            )
            # group_input_12.Vector -> field_at_index_001.Value
            _utils_group_field_at_selection.links.new(
                group_input_12.outputs[3], field_at_index_001.inputs[1]
            )
            # field_at_index_001.Value -> group_output_12.Vector
            _utils_group_field_at_selection.links.new(
                field_at_index_001.outputs[0], group_output_12.inputs[2]
            )
            # accumulate_field_002.Total -> field_at_index_002.Index
            _utils_group_field_at_selection.links.new(
                accumulate_field_002.outputs[2], field_at_index_002.inputs[0]
            )
            # group_input_12.Boolean -> field_at_index_002.Value
            _utils_group_field_at_selection.links.new(
                group_input_12.outputs[4], field_at_index_002.inputs[1]
            )
            # field_at_index_002.Value -> group_output_12.Boolean
            _utils_group_field_at_selection.links.new(
                field_at_index_002.outputs[0], group_output_12.inputs[3]
            )
            # accumulate_field_002.Total -> field_at_index_003.Index
            _utils_group_field_at_selection.links.new(
                accumulate_field_002.outputs[2], field_at_index_003.inputs[0]
            )
            # group_input_12.Color -> field_at_index_003.Value
            _utils_group_field_at_selection.links.new(
                group_input_12.outputs[5], field_at_index_003.inputs[1]
            )
            # field_at_index_003.Value -> group_output_12.Color
            _utils_group_field_at_selection.links.new(
                field_at_index_003.outputs[0], group_output_12.inputs[4]
            )
            # accumulate_field_002.Total -> field_at_index_004.Index
            _utils_group_field_at_selection.links.new(
                accumulate_field_002.outputs[2], field_at_index_004.inputs[0]
            )
            # group_input_12.Integer -> field_at_index_004.Value
            _utils_group_field_at_selection.links.new(
                group_input_12.outputs[6], field_at_index_004.inputs[1]
            )
            # field_at_index_004.Value -> group_output_12.Integer
            _utils_group_field_at_selection.links.new(
                field_at_index_004.outputs[0], group_output_12.inputs[5]
            )
            return _utils_group_field_at_selection

        _utils_group_field_at_selection = _utils_group_field_at_selection_node_group()

        # initialize _mn_utils_aa_atom_pos node group
        def _mn_utils_aa_atom_pos_node_group():
            _mn_utils_aa_atom_pos = bpy.data.node_groups.new(
                type="GeometryNodeTree", name=".MN_utils_aa_atom_pos"
            )

            _mn_utils_aa_atom_pos.color_tag = "NONE"
            _mn_utils_aa_atom_pos.description = ""

            # _mn_utils_aa_atom_pos interface
            # Socket Position
            position_socket = _mn_utils_aa_atom_pos.interface.new_socket(
                name="Position", in_out="OUTPUT", socket_type="NodeSocketVector"
            )
            position_socket.subtype = "NONE"
            position_socket.default_value = (0.0, 0.0, 0.0)
            position_socket.min_value = -3.4028234663852886e38
            position_socket.max_value = 3.4028234663852886e38
            position_socket.attribute_domain = "POINT"

            # Socket Group Index
            group_index_socket_2 = _mn_utils_aa_atom_pos.interface.new_socket(
                name="Group Index", in_out="OUTPUT", socket_type="NodeSocketInt"
            )
            group_index_socket_2.subtype = "NONE"
            group_index_socket_2.default_value = 0
            group_index_socket_2.min_value = -2147483648
            group_index_socket_2.max_value = 2147483647
            group_index_socket_2.attribute_domain = "POINT"

            # Socket b_factor
            b_factor_socket = _mn_utils_aa_atom_pos.interface.new_socket(
                name="b_factor", in_out="OUTPUT", socket_type="NodeSocketFloat"
            )
            b_factor_socket.subtype = "NONE"
            b_factor_socket.default_value = 0.0
            b_factor_socket.min_value = -3.4028234663852886e38
            b_factor_socket.max_value = 3.4028234663852886e38
            b_factor_socket.attribute_domain = "POINT"

            # Socket Integer
            integer_socket_2 = _mn_utils_aa_atom_pos.interface.new_socket(
                name="Integer", in_out="OUTPUT", socket_type="NodeSocketInt"
            )
            integer_socket_2.subtype = "NONE"
            integer_socket_2.default_value = 0
            integer_socket_2.min_value = -2147483648
            integer_socket_2.max_value = 2147483647
            integer_socket_2.attribute_domain = "POINT"

            # Socket atom_name
            atom_name_socket = _mn_utils_aa_atom_pos.interface.new_socket(
                name="atom_name", in_out="INPUT", socket_type="NodeSocketInt"
            )
            atom_name_socket.subtype = "NONE"
            atom_name_socket.default_value = 5
            atom_name_socket.min_value = -2147483648
            atom_name_socket.max_value = 2147483647
            atom_name_socket.attribute_domain = "POINT"

            # initialize _mn_utils_aa_atom_pos nodes
            # node Frame
            frame_3 = _mn_utils_aa_atom_pos.nodes.new("NodeFrame")
            frame_3.label = "If atom_name is 0, return midpoint of backbone N and C"
            frame_3.name = "Frame"
            frame_3.label_size = 20
            frame_3.shrink = True

            # node Group Input
            group_input_13 = _mn_utils_aa_atom_pos.nodes.new("NodeGroupInput")
            group_input_13.name = "Group Input"

            # node Named Attribute
            named_attribute_3 = _mn_utils_aa_atom_pos.nodes.new(
                "GeometryNodeInputNamedAttribute"
            )
            named_attribute_3.name = "Named Attribute"
            named_attribute_3.data_type = "INT"
            # Name
            named_attribute_3.inputs[0].default_value = "atom_name"

            # node Compare.002
            compare_002 = _mn_utils_aa_atom_pos.nodes.new("FunctionNodeCompare")
            compare_002.name = "Compare.002"
            compare_002.data_type = "INT"
            compare_002.mode = "ELEMENT"
            compare_002.operation = "EQUAL"
            # B_INT
            compare_002.inputs[3].default_value = 1

            # node Compare
            compare_1 = _mn_utils_aa_atom_pos.nodes.new("FunctionNodeCompare")
            compare_1.name = "Compare"
            compare_1.hide = True
            compare_1.data_type = "INT"
            compare_1.mode = "ELEMENT"
            compare_1.operation = "EQUAL"

            # node Named Attribute.001
            named_attribute_001_1 = _mn_utils_aa_atom_pos.nodes.new(
                "GeometryNodeInputNamedAttribute"
            )
            named_attribute_001_1.label = "b_factor"
            named_attribute_001_1.name = "Named Attribute.001"
            named_attribute_001_1.hide = True
            named_attribute_001_1.data_type = "FLOAT"
            # Name
            named_attribute_001_1.inputs[0].default_value = "b_factor"

            # node Position.001
            position_001_1 = _mn_utils_aa_atom_pos.nodes.new(
                "GeometryNodeInputPosition"
            )
            position_001_1.name = "Position.001"

            # node Reroute
            reroute_3 = _mn_utils_aa_atom_pos.nodes.new("NodeReroute")
            reroute_3.name = "Reroute"
            # node Position.002
            position_002_1 = _mn_utils_aa_atom_pos.nodes.new(
                "GeometryNodeInputPosition"
            )
            position_002_1.name = "Position.002"

            # node Compare.001
            compare_001 = _mn_utils_aa_atom_pos.nodes.new("FunctionNodeCompare")
            compare_001.name = "Compare.001"
            compare_001.data_type = "INT"
            compare_001.mode = "ELEMENT"
            compare_001.operation = "EQUAL"
            # B_INT
            compare_001.inputs[3].default_value = 3

            # node Compare.003
            compare_003 = _mn_utils_aa_atom_pos.nodes.new("FunctionNodeCompare")
            compare_003.name = "Compare.003"
            compare_003.data_type = "INT"
            compare_003.mode = "ELEMENT"
            compare_003.operation = "EQUAL"
            # B_INT
            compare_003.inputs[3].default_value = 1

            # node Switch.005
            switch_005 = _mn_utils_aa_atom_pos.nodes.new("GeometryNodeSwitch")
            switch_005.name = "Switch.005"
            switch_005.input_type = "VECTOR"

            # node Compare.004
            compare_004 = _mn_utils_aa_atom_pos.nodes.new("FunctionNodeCompare")
            compare_004.name = "Compare.004"
            compare_004.data_type = "INT"
            compare_004.mode = "ELEMENT"
            compare_004.operation = "NOT_EQUAL"
            # B_INT
            compare_004.inputs[3].default_value = 0

            # node Mix
            mix = _mn_utils_aa_atom_pos.nodes.new("ShaderNodeMix")
            mix.name = "Mix"
            mix.blend_type = "MIX"
            mix.clamp_factor = True
            mix.clamp_result = False
            mix.data_type = "VECTOR"
            mix.factor_mode = "UNIFORM"
            # Factor_Float
            mix.inputs[0].default_value = 0.5

            # node Index
            index_2 = _mn_utils_aa_atom_pos.nodes.new("GeometryNodeInputIndex")
            index_2.name = "Index"

            # node Edges of Vertex
            edges_of_vertex = _mn_utils_aa_atom_pos.nodes.new(
                "GeometryNodeEdgesOfVertex"
            )
            edges_of_vertex.name = "Edges of Vertex"
            # Weights
            edges_of_vertex.inputs[1].default_value = 0.0
            # Sort Index
            edges_of_vertex.inputs[2].default_value = 0

            # node Group.002
            group_002 = _mn_utils_aa_atom_pos.nodes.new("GeometryNodeGroup")
            group_002.name = "Group.002"
            group_002.node_tree = _utils_group_field_at_selection
            group_002.inputs[2].hide = True
            group_002.inputs[4].hide = True
            group_002.inputs[5].hide = True
            group_002.inputs[6].hide = True
            group_002.outputs[0].hide = True
            group_002.outputs[1].hide = True
            group_002.outputs[3].hide = True
            group_002.outputs[4].hide = True
            group_002.outputs[5].hide = True
            # Input_3
            group_002.inputs[2].default_value = 0.0
            # Input_7
            group_002.inputs[4].default_value = False
            # Input_9
            group_002.inputs[5].default_value = (0.0, 0.0, 0.0, 0.0)
            # Input_11
            group_002.inputs[6].default_value = 0

            # node Group.001
            group_001 = _mn_utils_aa_atom_pos.nodes.new("GeometryNodeGroup")
            group_001.name = "Group.001"
            group_001.node_tree = _utils_group_field_at_selection
            group_001.inputs[2].hide = True
            group_001.inputs[4].hide = True
            group_001.inputs[5].hide = True
            group_001.inputs[6].hide = True
            group_001.outputs[0].hide = True
            group_001.outputs[1].hide = True
            group_001.outputs[3].hide = True
            group_001.outputs[4].hide = True
            group_001.outputs[5].hide = True
            # Input_3
            group_001.inputs[2].default_value = 0.0
            # Input_7
            group_001.inputs[4].default_value = False
            # Input_9
            group_001.inputs[5].default_value = (0.0, 0.0, 0.0, 0.0)
            # Input_11
            group_001.inputs[6].default_value = 0

            # node Group Output
            group_output_13 = _mn_utils_aa_atom_pos.nodes.new("NodeGroupOutput")
            group_output_13.name = "Group Output"
            group_output_13.is_active_output = True

            # node Accumulate Field.001
            accumulate_field_001_1 = _mn_utils_aa_atom_pos.nodes.new(
                "GeometryNodeAccumulateField"
            )
            accumulate_field_001_1.name = "Accumulate Field.001"
            accumulate_field_001_1.data_type = "INT"
            accumulate_field_001_1.domain = "POINT"
            # Group Index
            accumulate_field_001_1.inputs[1].default_value = 0

            # node Group
            group_4 = _mn_utils_aa_atom_pos.nodes.new("GeometryNodeGroup")
            group_4.name = "Group"
            group_4.node_tree = _utils_group_field_at_selection
            # Input_7
            group_4.inputs[4].default_value = False
            # Input_9
            group_4.inputs[5].default_value = (0.0, 0.0, 0.0, 0.0)

            # Set parents
            position_002_1.parent = frame_3
            compare_001.parent = frame_3
            compare_003.parent = frame_3
            switch_005.parent = frame_3
            compare_004.parent = frame_3
            mix.parent = frame_3
            group_002.parent = frame_3
            group_001.parent = frame_3

            # Set locations
            frame_3.location = (0.0, 0.0)
            group_input_13.location = (-580.0, 200.0)
            named_attribute_3.location = (-580.0, 320.0)
            compare_002.location = (-580.0, 20.0)
            compare_1.location = (-85.78459167480469, -98.68995666503906)
            named_attribute_001_1.location = (-80.0, -200.0)
            position_001_1.location = (-80.0, -140.0)
            reroute_3.location = (60.0, 80.0)
            position_002_1.location = (-100.0, 440.0)
            compare_001.location = (-100.0, 380.0)
            compare_003.location = (-100.0, 600.0)
            switch_005.location = (620.0, 360.0)
            compare_004.location = (420.0, 340.0)
            mix.location = (420.0, 560.0)
            index_2.location = (-240.0, -260.0)
            edges_of_vertex.location = (-80.0, -260.0)
            group_002.location = (160.0, 400.0)
            group_001.location = (160.0, 580.0)
            group_output_13.location = (1178.18603515625, 91.78607177734375)
            accumulate_field_001_1.location = (-420.0, 20.0)
            group_4.location = (141.92819213867188, 23.15901756286621)

            # initialize _mn_utils_aa_atom_pos links
            # group_input_13.atom_name -> compare_1.B
            _mn_utils_aa_atom_pos.links.new(
                group_input_13.outputs[0], compare_1.inputs[3]
            )
            # named_attribute_3.Attribute -> compare_1.A
            _mn_utils_aa_atom_pos.links.new(
                named_attribute_3.outputs[0], compare_1.inputs[2]
            )
            # reroute_3.Output -> group_output_13.Group Index
            _mn_utils_aa_atom_pos.links.new(
                reroute_3.outputs[0], group_output_13.inputs[1]
            )
            # named_attribute_3.Attribute -> compare_002.A
            _mn_utils_aa_atom_pos.links.new(
                named_attribute_3.outputs[0], compare_002.inputs[2]
            )
            # compare_002.Result -> accumulate_field_001_1.Value
            _mn_utils_aa_atom_pos.links.new(
                compare_002.outputs[0], accumulate_field_001_1.inputs[0]
            )
            # named_attribute_3.Attribute -> compare_001.A
            _mn_utils_aa_atom_pos.links.new(
                named_attribute_3.outputs[0], compare_001.inputs[2]
            )
            # named_attribute_3.Attribute -> compare_003.A
            _mn_utils_aa_atom_pos.links.new(
                named_attribute_3.outputs[0], compare_003.inputs[2]
            )
            # group_input_13.atom_name -> compare_004.A
            _mn_utils_aa_atom_pos.links.new(
                group_input_13.outputs[0], compare_004.inputs[2]
            )
            # compare_004.Result -> switch_005.Switch
            _mn_utils_aa_atom_pos.links.new(
                compare_004.outputs[0], switch_005.inputs[0]
            )
            # mix.Result -> switch_005.False
            _mn_utils_aa_atom_pos.links.new(mix.outputs[1], switch_005.inputs[1])
            # switch_005.Output -> group_output_13.Position
            _mn_utils_aa_atom_pos.links.new(
                switch_005.outputs[0], group_output_13.inputs[0]
            )
            # compare_1.Result -> group_4.Selection
            _mn_utils_aa_atom_pos.links.new(compare_1.outputs[0], group_4.inputs[0])
            # reroute_3.Output -> group_4.Group Index
            _mn_utils_aa_atom_pos.links.new(reroute_3.outputs[0], group_4.inputs[1])
            # named_attribute_001_1.Attribute -> group_4.Float
            _mn_utils_aa_atom_pos.links.new(
                named_attribute_001_1.outputs[0], group_4.inputs[2]
            )
            # group_4.Float -> group_output_13.b_factor
            _mn_utils_aa_atom_pos.links.new(
                group_4.outputs[1], group_output_13.inputs[2]
            )
            # position_001_1.Position -> group_4.Vector
            _mn_utils_aa_atom_pos.links.new(
                position_001_1.outputs[0], group_4.inputs[3]
            )
            # group_4.Vector -> switch_005.True
            _mn_utils_aa_atom_pos.links.new(group_4.outputs[2], switch_005.inputs[2])
            # compare_003.Result -> group_001.Selection
            _mn_utils_aa_atom_pos.links.new(compare_003.outputs[0], group_001.inputs[0])
            # reroute_3.Output -> group_001.Group Index
            _mn_utils_aa_atom_pos.links.new(reroute_3.outputs[0], group_001.inputs[1])
            # group_001.Vector -> mix.A
            _mn_utils_aa_atom_pos.links.new(group_001.outputs[2], mix.inputs[4])
            # reroute_3.Output -> group_002.Group Index
            _mn_utils_aa_atom_pos.links.new(reroute_3.outputs[0], group_002.inputs[1])
            # compare_001.Result -> group_002.Selection
            _mn_utils_aa_atom_pos.links.new(compare_001.outputs[0], group_002.inputs[0])
            # group_002.Vector -> mix.B
            _mn_utils_aa_atom_pos.links.new(group_002.outputs[2], mix.inputs[5])
            # position_002_1.Position -> group_001.Vector
            _mn_utils_aa_atom_pos.links.new(
                position_002_1.outputs[0], group_001.inputs[3]
            )
            # position_002_1.Position -> group_002.Vector
            _mn_utils_aa_atom_pos.links.new(
                position_002_1.outputs[0], group_002.inputs[3]
            )
            # index_2.Index -> edges_of_vertex.Vertex Index
            _mn_utils_aa_atom_pos.links.new(
                index_2.outputs[0], edges_of_vertex.inputs[0]
            )
            # edges_of_vertex.Total -> group_4.Integer
            _mn_utils_aa_atom_pos.links.new(
                edges_of_vertex.outputs[1], group_4.inputs[6]
            )
            # group_4.Integer -> group_output_13.Integer
            _mn_utils_aa_atom_pos.links.new(
                group_4.outputs[5], group_output_13.inputs[3]
            )
            # accumulate_field_001_1.Leading -> reroute_3.Input
            _mn_utils_aa_atom_pos.links.new(
                accumulate_field_001_1.outputs[0], reroute_3.inputs[0]
            )
            return _mn_utils_aa_atom_pos

        _mn_utils_aa_atom_pos = _mn_utils_aa_atom_pos_node_group()

        # initialize _mn_constants_atom_name_peptide node group
        def _mn_constants_atom_name_peptide_node_group():
            _mn_constants_atom_name_peptide = bpy.data.node_groups.new(
                type="GeometryNodeTree", name=".MN_constants_atom_name_peptide"
            )

            _mn_constants_atom_name_peptide.color_tag = "NONE"
            _mn_constants_atom_name_peptide.description = ""

            # _mn_constants_atom_name_peptide interface
            # Socket Backbone Lower
            backbone_lower_socket = (
                _mn_constants_atom_name_peptide.interface.new_socket(
                    name="Backbone Lower", in_out="OUTPUT", socket_type="NodeSocketInt"
                )
            )
            backbone_lower_socket.subtype = "NONE"
            backbone_lower_socket.default_value = 0
            backbone_lower_socket.min_value = -2147483648
            backbone_lower_socket.max_value = 2147483647
            backbone_lower_socket.attribute_domain = "POINT"

            # Socket Backbone Upper
            backbone_upper_socket = (
                _mn_constants_atom_name_peptide.interface.new_socket(
                    name="Backbone Upper", in_out="OUTPUT", socket_type="NodeSocketInt"
                )
            )
            backbone_upper_socket.subtype = "NONE"
            backbone_upper_socket.default_value = 0
            backbone_upper_socket.min_value = -2147483648
            backbone_upper_socket.max_value = 2147483647
            backbone_upper_socket.attribute_domain = "POINT"

            # Socket Side Chain Lower
            side_chain_lower_socket = (
                _mn_constants_atom_name_peptide.interface.new_socket(
                    name="Side Chain Lower",
                    in_out="OUTPUT",
                    socket_type="NodeSocketInt",
                )
            )
            side_chain_lower_socket.subtype = "NONE"
            side_chain_lower_socket.default_value = 0
            side_chain_lower_socket.min_value = -2147483648
            side_chain_lower_socket.max_value = 2147483647
            side_chain_lower_socket.attribute_domain = "POINT"

            # Socket Side Chain Upper
            side_chain_upper_socket = (
                _mn_constants_atom_name_peptide.interface.new_socket(
                    name="Side Chain Upper",
                    in_out="OUTPUT",
                    socket_type="NodeSocketInt",
                )
            )
            side_chain_upper_socket.subtype = "NONE"
            side_chain_upper_socket.default_value = 0
            side_chain_upper_socket.min_value = -2147483648
            side_chain_upper_socket.max_value = 2147483647
            side_chain_upper_socket.attribute_domain = "POINT"

            # Socket Alpha Carbon
            alpha_carbon_socket = _mn_constants_atom_name_peptide.interface.new_socket(
                name="Alpha Carbon", in_out="OUTPUT", socket_type="NodeSocketInt"
            )
            alpha_carbon_socket.subtype = "NONE"
            alpha_carbon_socket.default_value = 0
            alpha_carbon_socket.min_value = -2147483648
            alpha_carbon_socket.max_value = 2147483647
            alpha_carbon_socket.attribute_domain = "POINT"

            # initialize _mn_constants_atom_name_peptide nodes
            # node Group Input
            group_input_14 = _mn_constants_atom_name_peptide.nodes.new("NodeGroupInput")
            group_input_14.name = "Group Input"

            # node Group Output
            group_output_14 = _mn_constants_atom_name_peptide.nodes.new(
                "NodeGroupOutput"
            )
            group_output_14.name = "Group Output"
            group_output_14.is_active_output = True

            # node Integer.001
            integer_001 = _mn_constants_atom_name_peptide.nodes.new(
                "FunctionNodeInputInt"
            )
            integer_001.name = "Integer.001"
            integer_001.integer = 49

            # node Integer.004
            integer_004 = _mn_constants_atom_name_peptide.nodes.new(
                "FunctionNodeInputInt"
            )
            integer_004.name = "Integer.004"
            integer_004.integer = 2

            # node Integer
            integer_1 = _mn_constants_atom_name_peptide.nodes.new(
                "FunctionNodeInputInt"
            )
            integer_1.name = "Integer"
            integer_1.integer = 5

            # node Integer.003
            integer_003 = _mn_constants_atom_name_peptide.nodes.new(
                "FunctionNodeInputInt"
            )
            integer_003.name = "Integer.003"
            integer_003.integer = 1

            # node Integer.002
            integer_002 = _mn_constants_atom_name_peptide.nodes.new(
                "FunctionNodeInputInt"
            )
            integer_002.name = "Integer.002"
            integer_002.integer = 4

            # Set locations
            group_input_14.location = (-200.0, 0.0)
            group_output_14.location = (260.0, 180.0)
            integer_001.location = (0.0, -50.0)
            integer_004.location = (0.0, -140.0)
            integer_1.location = (0.0, 40.0)
            integer_003.location = (0.0, 240.0)
            integer_002.location = (0.0, 140.0)

            # initialize _mn_constants_atom_name_peptide links
            # integer_003.Integer -> group_output_14.Backbone Lower
            _mn_constants_atom_name_peptide.links.new(
                integer_003.outputs[0], group_output_14.inputs[0]
            )
            # integer_002.Integer -> group_output_14.Backbone Upper
            _mn_constants_atom_name_peptide.links.new(
                integer_002.outputs[0], group_output_14.inputs[1]
            )
            # integer_1.Integer -> group_output_14.Side Chain Lower
            _mn_constants_atom_name_peptide.links.new(
                integer_1.outputs[0], group_output_14.inputs[2]
            )
            # integer_001.Integer -> group_output_14.Side Chain Upper
            _mn_constants_atom_name_peptide.links.new(
                integer_001.outputs[0], group_output_14.inputs[3]
            )
            # integer_004.Integer -> group_output_14.Alpha Carbon
            _mn_constants_atom_name_peptide.links.new(
                integer_004.outputs[0], group_output_14.inputs[4]
            )
            return _mn_constants_atom_name_peptide

        _mn_constants_atom_name_peptide = _mn_constants_atom_name_peptide_node_group()

        # initialize _mn_select_peptide node group
        def _mn_select_peptide_node_group():
            _mn_select_peptide = bpy.data.node_groups.new(
                type="GeometryNodeTree", name=".MN_select_peptide"
            )

            _mn_select_peptide.color_tag = "NONE"
            _mn_select_peptide.description = ""

            # _mn_select_peptide interface
            # Socket Is Backbone
            is_backbone_socket = _mn_select_peptide.interface.new_socket(
                name="Is Backbone", in_out="OUTPUT", socket_type="NodeSocketBool"
            )
            is_backbone_socket.attribute_domain = "POINT"

            # Socket Is Side Chain
            is_side_chain_socket = _mn_select_peptide.interface.new_socket(
                name="Is Side Chain", in_out="OUTPUT", socket_type="NodeSocketBool"
            )
            is_side_chain_socket.attribute_domain = "POINT"

            # Socket Is Peptide
            is_peptide_socket = _mn_select_peptide.interface.new_socket(
                name="Is Peptide", in_out="OUTPUT", socket_type="NodeSocketBool"
            )
            is_peptide_socket.attribute_domain = "POINT"

            # Socket Is Alpha Carbon
            is_alpha_carbon_socket = _mn_select_peptide.interface.new_socket(
                name="Is Alpha Carbon", in_out="OUTPUT", socket_type="NodeSocketBool"
            )
            is_alpha_carbon_socket.attribute_domain = "POINT"

            # initialize _mn_select_peptide nodes
            # node Group Input
            group_input_15 = _mn_select_peptide.nodes.new("NodeGroupInput")
            group_input_15.name = "Group Input"

            # node Compare
            compare_2 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
            compare_2.name = "Compare"
            compare_2.data_type = "INT"
            compare_2.mode = "ELEMENT"
            compare_2.operation = "GREATER_EQUAL"

            # node Compare.001
            compare_001_1 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
            compare_001_1.name = "Compare.001"
            compare_001_1.data_type = "INT"
            compare_001_1.mode = "ELEMENT"
            compare_001_1.operation = "LESS_EQUAL"

            # node Boolean Math.001
            boolean_math_001 = _mn_select_peptide.nodes.new("FunctionNodeBooleanMath")
            boolean_math_001.name = "Boolean Math.001"
            boolean_math_001.operation = "AND"

            # node Compare.002
            compare_002_1 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
            compare_002_1.name = "Compare.002"
            compare_002_1.data_type = "INT"
            compare_002_1.mode = "ELEMENT"
            compare_002_1.operation = "GREATER_EQUAL"

            # node Compare.003
            compare_003_1 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
            compare_003_1.name = "Compare.003"
            compare_003_1.data_type = "INT"
            compare_003_1.mode = "ELEMENT"
            compare_003_1.operation = "LESS_EQUAL"

            # node Boolean Math.002
            boolean_math_002 = _mn_select_peptide.nodes.new("FunctionNodeBooleanMath")
            boolean_math_002.name = "Boolean Math.002"
            boolean_math_002.operation = "AND"

            # node Compare.004
            compare_004_1 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
            compare_004_1.name = "Compare.004"
            compare_004_1.data_type = "INT"
            compare_004_1.mode = "ELEMENT"
            compare_004_1.operation = "GREATER_EQUAL"

            # node Named Attribute
            named_attribute_4 = _mn_select_peptide.nodes.new(
                "GeometryNodeInputNamedAttribute"
            )
            named_attribute_4.name = "Named Attribute"
            named_attribute_4.data_type = "INT"
            # Name
            named_attribute_4.inputs[0].default_value = "atom_name"

            # node Boolean Math.003
            boolean_math_003 = _mn_select_peptide.nodes.new("FunctionNodeBooleanMath")
            boolean_math_003.name = "Boolean Math.003"
            boolean_math_003.operation = "AND"

            # node Group Output
            group_output_15 = _mn_select_peptide.nodes.new("NodeGroupOutput")
            group_output_15.name = "Group Output"
            group_output_15.is_active_output = True

            # node Compare.005
            compare_005 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
            compare_005.name = "Compare.005"
            compare_005.data_type = "INT"
            compare_005.mode = "ELEMENT"
            compare_005.operation = "LESS_EQUAL"

            # node Compare.006
            compare_006 = _mn_select_peptide.nodes.new("FunctionNodeCompare")
            compare_006.name = "Compare.006"
            compare_006.data_type = "INT"
            compare_006.mode = "ELEMENT"
            compare_006.operation = "EQUAL"

            # node Group
            group_5 = _mn_select_peptide.nodes.new("GeometryNodeGroup")
            group_5.name = "Group"
            group_5.node_tree = _mn_constants_atom_name_peptide

            # node Boolean Math
            boolean_math = _mn_select_peptide.nodes.new("FunctionNodeBooleanMath")
            boolean_math.name = "Boolean Math"
            boolean_math.operation = "OR"

            # Set locations
            group_input_15.location = (-460.0, 0.0)
            compare_2.location = (80.0, 80.0)
            compare_001_1.location = (80.0, -80.0)
            boolean_math_001.location = (260.0, 80.0)
            compare_002_1.location = (80.0, -240.0)
            compare_003_1.location = (80.0, -400.0)
            boolean_math_002.location = (260.0, -240.0)
            compare_004_1.location = (80.0, -560.0)
            named_attribute_4.location = (-360.0, -480.0)
            boolean_math_003.location = (260.0, -560.0)
            group_output_15.location = (666.1161499023438, -263.7054748535156)
            compare_005.location = (80.0, -720.0)
            compare_006.location = (260.0, -380.0)
            group_5.location = (-411.24090576171875, -312.71807861328125)
            boolean_math.location = (420.0, -240.0)

            # initialize _mn_select_peptide links
            # compare_001_1.Result -> boolean_math_001.Boolean
            _mn_select_peptide.links.new(
                compare_001_1.outputs[0], boolean_math_001.inputs[1]
            )
            # group_5.Backbone Lower -> compare_2.B
            _mn_select_peptide.links.new(group_5.outputs[0], compare_2.inputs[3])
            # named_attribute_4.Attribute -> compare_2.A
            _mn_select_peptide.links.new(
                named_attribute_4.outputs[0], compare_2.inputs[2]
            )
            # compare_2.Result -> boolean_math_001.Boolean
            _mn_select_peptide.links.new(
                compare_2.outputs[0], boolean_math_001.inputs[0]
            )
            # named_attribute_4.Attribute -> compare_001_1.A
            _mn_select_peptide.links.new(
                named_attribute_4.outputs[0], compare_001_1.inputs[2]
            )
            # group_5.Backbone Upper -> compare_001_1.B
            _mn_select_peptide.links.new(group_5.outputs[1], compare_001_1.inputs[3])
            # boolean_math_001.Boolean -> group_output_15.Is Backbone
            _mn_select_peptide.links.new(
                boolean_math_001.outputs[0], group_output_15.inputs[0]
            )
            # compare_003_1.Result -> boolean_math_002.Boolean
            _mn_select_peptide.links.new(
                compare_003_1.outputs[0], boolean_math_002.inputs[1]
            )
            # named_attribute_4.Attribute -> compare_002_1.A
            _mn_select_peptide.links.new(
                named_attribute_4.outputs[0], compare_002_1.inputs[2]
            )
            # compare_002_1.Result -> boolean_math_002.Boolean
            _mn_select_peptide.links.new(
                compare_002_1.outputs[0], boolean_math_002.inputs[0]
            )
            # named_attribute_4.Attribute -> compare_003_1.A
            _mn_select_peptide.links.new(
                named_attribute_4.outputs[0], compare_003_1.inputs[2]
            )
            # group_5.Side Chain Lower -> compare_002_1.B
            _mn_select_peptide.links.new(group_5.outputs[2], compare_002_1.inputs[3])
            # group_5.Side Chain Upper -> compare_003_1.B
            _mn_select_peptide.links.new(group_5.outputs[3], compare_003_1.inputs[3])
            # compare_005.Result -> boolean_math_003.Boolean
            _mn_select_peptide.links.new(
                compare_005.outputs[0], boolean_math_003.inputs[1]
            )
            # named_attribute_4.Attribute -> compare_004_1.A
            _mn_select_peptide.links.new(
                named_attribute_4.outputs[0], compare_004_1.inputs[2]
            )
            # compare_004_1.Result -> boolean_math_003.Boolean
            _mn_select_peptide.links.new(
                compare_004_1.outputs[0], boolean_math_003.inputs[0]
            )
            # named_attribute_4.Attribute -> compare_005.A
            _mn_select_peptide.links.new(
                named_attribute_4.outputs[0], compare_005.inputs[2]
            )
            # group_5.Backbone Lower -> compare_004_1.B
            _mn_select_peptide.links.new(group_5.outputs[0], compare_004_1.inputs[3])
            # group_5.Side Chain Upper -> compare_005.B
            _mn_select_peptide.links.new(group_5.outputs[3], compare_005.inputs[3])
            # boolean_math_003.Boolean -> group_output_15.Is Peptide
            _mn_select_peptide.links.new(
                boolean_math_003.outputs[0], group_output_15.inputs[2]
            )
            # named_attribute_4.Attribute -> compare_006.A
            _mn_select_peptide.links.new(
                named_attribute_4.outputs[0], compare_006.inputs[2]
            )
            # group_5.Alpha Carbon -> compare_006.B
            _mn_select_peptide.links.new(group_5.outputs[4], compare_006.inputs[3])
            # compare_006.Result -> group_output_15.Is Alpha Carbon
            _mn_select_peptide.links.new(
                compare_006.outputs[0], group_output_15.inputs[3]
            )
            # boolean_math_002.Boolean -> boolean_math.Boolean
            _mn_select_peptide.links.new(
                boolean_math_002.outputs[0], boolean_math.inputs[0]
            )
            # compare_006.Result -> boolean_math.Boolean
            _mn_select_peptide.links.new(compare_006.outputs[0], boolean_math.inputs[1])
            # boolean_math.Boolean -> group_output_15.Is Side Chain
            _mn_select_peptide.links.new(
                boolean_math.outputs[0], group_output_15.inputs[1]
            )
            return _mn_select_peptide

        _mn_select_peptide = _mn_select_peptide_node_group()

        # initialize fallback_boolean node group
        def fallback_boolean_node_group():
            fallback_boolean = bpy.data.node_groups.new(
                type="GeometryNodeTree", name="Fallback Boolean"
            )

            fallback_boolean.color_tag = "INPUT"
            fallback_boolean.description = "Computes the boolean field if the given attribute doesn't exist. If it doesn't exist it just uses the attribute instead"

            # fallback_boolean interface
            # Socket Boolean
            boolean_socket_2 = fallback_boolean.interface.new_socket(
                name="Boolean", in_out="OUTPUT", socket_type="NodeSocketBool"
            )
            boolean_socket_2.attribute_domain = "POINT"

            # Socket Name
            name_socket = fallback_boolean.interface.new_socket(
                name="Name", in_out="INPUT", socket_type="NodeSocketString"
            )
            name_socket.attribute_domain = "POINT"

            # Socket Fallback
            fallback_socket = fallback_boolean.interface.new_socket(
                name="Fallback", in_out="INPUT", socket_type="NodeSocketBool"
            )
            fallback_socket.attribute_domain = "POINT"

            # initialize fallback_boolean nodes
            # node Group Output
            group_output_16 = fallback_boolean.nodes.new("NodeGroupOutput")
            group_output_16.name = "Group Output"
            group_output_16.is_active_output = True

            # node Group Input
            group_input_16 = fallback_boolean.nodes.new("NodeGroupInput")
            group_input_16.name = "Group Input"

            # node Named Attribute
            named_attribute_5 = fallback_boolean.nodes.new(
                "GeometryNodeInputNamedAttribute"
            )
            named_attribute_5.name = "Named Attribute"
            named_attribute_5.data_type = "BOOLEAN"

            # node Switch
            switch_3 = fallback_boolean.nodes.new("GeometryNodeSwitch")
            switch_3.name = "Switch"
            switch_3.input_type = "BOOLEAN"

            # Set locations
            group_output_16.location = (276.6171569824219, 4.738137245178223)
            group_input_16.location = (-280.0, 0.0)
            named_attribute_5.location = (-94.73597717285156, 4.738137245178223)
            switch_3.location = (86.61715698242188, 4.738137245178223)

            # initialize fallback_boolean links
            # named_attribute_5.Exists -> switch_3.Switch
            fallback_boolean.links.new(named_attribute_5.outputs[1], switch_3.inputs[0])
            # named_attribute_5.Attribute -> switch_3.True
            fallback_boolean.links.new(named_attribute_5.outputs[0], switch_3.inputs[2])
            # group_input_16.Fallback -> switch_3.False
            fallback_boolean.links.new(group_input_16.outputs[1], switch_3.inputs[1])
            # switch_3.Output -> group_output_16.Boolean
            fallback_boolean.links.new(switch_3.outputs[0], group_output_16.inputs[0])
            # group_input_16.Name -> named_attribute_5.Name
            fallback_boolean.links.new(
                group_input_16.outputs[0], named_attribute_5.inputs[0]
            )
            return fallback_boolean

        fallback_boolean = fallback_boolean_node_group()

        # initialize is_peptide node group
        def is_peptide_node_group():
            is_peptide = bpy.data.node_groups.new(
                type="GeometryNodeTree", name="Is Peptide"
            )

            is_peptide.color_tag = "INPUT"
            is_peptide.description = ""

            # is_peptide interface
            # Socket Selection
            selection_socket_8 = is_peptide.interface.new_socket(
                name="Selection", in_out="OUTPUT", socket_type="NodeSocketBool"
            )
            selection_socket_8.attribute_domain = "POINT"
            selection_socket_8.description = "True if atoms are part of a peptide"

            # Socket Inverted
            inverted_socket = is_peptide.interface.new_socket(
                name="Inverted", in_out="OUTPUT", socket_type="NodeSocketBool"
            )
            inverted_socket.attribute_domain = "POINT"

            # Socket And
            and_socket = is_peptide.interface.new_socket(
                name="And", in_out="INPUT", socket_type="NodeSocketBool"
            )
            and_socket.attribute_domain = "POINT"
            and_socket.hide_value = True

            # Socket Or
            or_socket = is_peptide.interface.new_socket(
                name="Or", in_out="INPUT", socket_type="NodeSocketBool"
            )
            or_socket.attribute_domain = "POINT"
            or_socket.hide_value = True

            # initialize is_peptide nodes
            # node Group Input
            group_input_17 = is_peptide.nodes.new("NodeGroupInput")
            group_input_17.name = "Group Input"

            # node Boolean Math.001
            boolean_math_001_1 = is_peptide.nodes.new("FunctionNodeBooleanMath")
            boolean_math_001_1.name = "Boolean Math.001"
            boolean_math_001_1.operation = "AND"

            # node Group
            group_6 = is_peptide.nodes.new("GeometryNodeGroup")
            group_6.name = "Group"
            group_6.node_tree = _mn_select_peptide

            # node Group Output
            group_output_17 = is_peptide.nodes.new("NodeGroupOutput")
            group_output_17.name = "Group Output"
            group_output_17.is_active_output = True

            # node Group.001
            group_001_1 = is_peptide.nodes.new("GeometryNodeGroup")
            group_001_1.name = "Group.001"
            group_001_1.node_tree = fallback_boolean
            # Socket_2
            group_001_1.inputs[0].default_value = "is_peptide"

            # node Boolean Math.002
            boolean_math_002_1 = is_peptide.nodes.new("FunctionNodeBooleanMath")
            boolean_math_002_1.name = "Boolean Math.002"
            boolean_math_002_1.operation = "OR"

            # node Boolean Math
            boolean_math_1 = is_peptide.nodes.new("FunctionNodeBooleanMath")
            boolean_math_1.name = "Boolean Math"
            boolean_math_1.operation = "NOT"

            # Set locations
            group_input_17.location = (-200.0, 0.0)
            boolean_math_001_1.location = (-40.0, 0.0)
            group_6.location = (-340.0, -140.0)
            group_output_17.location = (320.0, 0.0)
            group_001_1.location = (-40.0, -140.0)
            boolean_math_002_1.location = (140.0, 5.243539333343506)
            boolean_math_1.location = (140.0, -120.0)

            # initialize is_peptide links
            # boolean_math_002_1.Boolean -> group_output_17.Selection
            is_peptide.links.new(
                boolean_math_002_1.outputs[0], group_output_17.inputs[0]
            )
            # group_input_17.And -> boolean_math_001_1.Boolean
            is_peptide.links.new(
                group_input_17.outputs[0], boolean_math_001_1.inputs[0]
            )
            # group_6.Is Peptide -> group_001_1.Fallback
            is_peptide.links.new(group_6.outputs[2], group_001_1.inputs[1])
            # group_001_1.Boolean -> boolean_math_001_1.Boolean
            is_peptide.links.new(group_001_1.outputs[0], boolean_math_001_1.inputs[1])
            # boolean_math_001_1.Boolean -> boolean_math_002_1.Boolean
            is_peptide.links.new(
                boolean_math_001_1.outputs[0], boolean_math_002_1.inputs[0]
            )
            # group_input_17.Or -> boolean_math_002_1.Boolean
            is_peptide.links.new(
                group_input_17.outputs[1], boolean_math_002_1.inputs[1]
            )
            # boolean_math_002_1.Boolean -> boolean_math_1.Boolean
            is_peptide.links.new(
                boolean_math_002_1.outputs[0], boolean_math_1.inputs[0]
            )
            # boolean_math_1.Boolean -> group_output_17.Inverted
            is_peptide.links.new(boolean_math_1.outputs[0], group_output_17.inputs[1])
            return is_peptide

        is_peptide = is_peptide_node_group()

        # initialize _mn_utils_rotate_res node group
        def _mn_utils_rotate_res_node_group():
            _mn_utils_rotate_res = bpy.data.node_groups.new(
                type="GeometryNodeTree", name=".MN_utils_rotate_res"
            )

            _mn_utils_rotate_res.color_tag = "NONE"
            _mn_utils_rotate_res.description = ""

            # _mn_utils_rotate_res interface
            # Socket Selection
            selection_socket_9 = _mn_utils_rotate_res.interface.new_socket(
                name="Selection", in_out="OUTPUT", socket_type="NodeSocketBool"
            )
            selection_socket_9.attribute_domain = "POINT"
            selection_socket_9.description = "The calculated selection"

            # Socket Position
            position_socket_1 = _mn_utils_rotate_res.interface.new_socket(
                name="Position", in_out="OUTPUT", socket_type="NodeSocketVector"
            )
            position_socket_1.subtype = "NONE"
            position_socket_1.default_value = (0.0, 0.0, 0.0)
            position_socket_1.min_value = -3.4028234663852886e38
            position_socket_1.max_value = 3.4028234663852886e38
            position_socket_1.attribute_domain = "POINT"

            # Socket Selection
            selection_socket_10 = _mn_utils_rotate_res.interface.new_socket(
                name="Selection", in_out="INPUT", socket_type="NodeSocketBool"
            )
            selection_socket_10.attribute_domain = "POINT"
            selection_socket_10.description = "Selection of atoms to apply this node to"

            # Socket atom_name rotation
            atom_name_rotation_socket = _mn_utils_rotate_res.interface.new_socket(
                name="atom_name rotation", in_out="INPUT", socket_type="NodeSocketInt"
            )
            atom_name_rotation_socket.subtype = "NONE"
            atom_name_rotation_socket.default_value = 0
            atom_name_rotation_socket.min_value = -2147483648
            atom_name_rotation_socket.max_value = 2147483647
            atom_name_rotation_socket.attribute_domain = "POINT"

            # Socket atom_name axis
            atom_name_axis_socket = _mn_utils_rotate_res.interface.new_socket(
                name="atom_name axis", in_out="INPUT", socket_type="NodeSocketInt"
            )
            atom_name_axis_socket.subtype = "NONE"
            atom_name_axis_socket.default_value = 2
            atom_name_axis_socket.min_value = -2147483648
            atom_name_axis_socket.max_value = 2147483647
            atom_name_axis_socket.attribute_domain = "POINT"

            # Socket Scale b_factor
            scale_b_factor_socket = _mn_utils_rotate_res.interface.new_socket(
                name="Scale b_factor", in_out="INPUT", socket_type="NodeSocketFloat"
            )
            scale_b_factor_socket.subtype = "FACTOR"
            scale_b_factor_socket.default_value = 0.0
            scale_b_factor_socket.min_value = -3.4028234663852886e38
            scale_b_factor_socket.max_value = 3.4028234663852886e38
            scale_b_factor_socket.attribute_domain = "POINT"

            # Socket Amplitude
            amplitude_socket_1 = _mn_utils_rotate_res.interface.new_socket(
                name="Amplitude", in_out="INPUT", socket_type="NodeSocketFloat"
            )
            amplitude_socket_1.subtype = "NONE"
            amplitude_socket_1.default_value = 1.0
            amplitude_socket_1.min_value = 0.0
            amplitude_socket_1.max_value = 10.0
            amplitude_socket_1.attribute_domain = "POINT"

            # Socket Amp. Axis
            amp__axis_socket = _mn_utils_rotate_res.interface.new_socket(
                name="Amp. Axis", in_out="INPUT", socket_type="NodeSocketFloat"
            )
            amp__axis_socket.subtype = "NONE"
            amp__axis_socket.default_value = 1.0
            amp__axis_socket.min_value = -10000.0
            amp__axis_socket.max_value = 10000.0
            amp__axis_socket.attribute_domain = "POINT"

            # Socket Amp. Euler
            amp__euler_socket = _mn_utils_rotate_res.interface.new_socket(
                name="Amp. Euler", in_out="INPUT", socket_type="NodeSocketFloat"
            )
            amp__euler_socket.subtype = "NONE"
            amp__euler_socket.default_value = 1.0
            amp__euler_socket.min_value = -10000.0
            amp__euler_socket.max_value = 10000.0
            amp__euler_socket.attribute_domain = "POINT"

            # Socket Speed
            speed_socket_1 = _mn_utils_rotate_res.interface.new_socket(
                name="Speed", in_out="INPUT", socket_type="NodeSocketFloat"
            )
            speed_socket_1.subtype = "NONE"
            speed_socket_1.default_value = 10.0
            speed_socket_1.min_value = -10000.0
            speed_socket_1.max_value = 10000.0
            speed_socket_1.attribute_domain = "POINT"

            # Socket Animate 0..1
            animate_0__1_socket_1 = _mn_utils_rotate_res.interface.new_socket(
                name="Animate 0..1", in_out="INPUT", socket_type="NodeSocketFloat"
            )
            animate_0__1_socket_1.subtype = "NONE"
            animate_0__1_socket_1.default_value = 0.5
            animate_0__1_socket_1.min_value = -10000.0
            animate_0__1_socket_1.max_value = 10000.0
            animate_0__1_socket_1.attribute_domain = "POINT"

            # initialize _mn_utils_rotate_res nodes
            # node Named Attribute.001
            named_attribute_001_2 = _mn_utils_rotate_res.nodes.new(
                "GeometryNodeInputNamedAttribute"
            )
            named_attribute_001_2.name = "Named Attribute.001"
            named_attribute_001_2.data_type = "INT"
            # Name
            named_attribute_001_2.inputs[0].default_value = "atom_name"

            # node Reroute.001
            reroute_001_2 = _mn_utils_rotate_res.nodes.new("NodeReroute")
            reroute_001_2.name = "Reroute.001"
            # node Reroute.002
            reroute_002_2 = _mn_utils_rotate_res.nodes.new("NodeReroute")
            reroute_002_2.name = "Reroute.002"
            # node Reroute.003
            reroute_003_1 = _mn_utils_rotate_res.nodes.new("NodeReroute")
            reroute_003_1.name = "Reroute.003"
            # node Boolean Math
            boolean_math_2 = _mn_utils_rotate_res.nodes.new("FunctionNodeBooleanMath")
            boolean_math_2.name = "Boolean Math"
            boolean_math_2.operation = "AND"

            # node Compare.001
            compare_001_2 = _mn_utils_rotate_res.nodes.new("FunctionNodeCompare")
            compare_001_2.name = "Compare.001"
            compare_001_2.data_type = "INT"
            compare_001_2.mode = "ELEMENT"
            compare_001_2.operation = "GREATER_THAN"

            # node Random Value
            random_value_1 = _mn_utils_rotate_res.nodes.new("FunctionNodeRandomValue")
            random_value_1.name = "Random Value"
            random_value_1.hide = True
            random_value_1.data_type = "FLOAT_VECTOR"
            # Min
            random_value_1.inputs[0].default_value = (-13.0, -13.0, -13.0)
            # Max
            random_value_1.inputs[1].default_value = (
                13.899999618530273,
                13.899999618530273,
                13.899999618530273,
            )

            # node Boolean Math.001
            boolean_math_001_2 = _mn_utils_rotate_res.nodes.new(
                "FunctionNodeBooleanMath"
            )
            boolean_math_001_2.name = "Boolean Math.001"
            boolean_math_001_2.operation = "AND"

            # node Position
            position_1 = _mn_utils_rotate_res.nodes.new("GeometryNodeInputPosition")
            position_1.name = "Position"

            # node Vector Rotate
            vector_rotate = _mn_utils_rotate_res.nodes.new("ShaderNodeVectorRotate")
            vector_rotate.name = "Vector Rotate"
            vector_rotate.invert = False
            vector_rotate.rotation_type = "AXIS_ANGLE"

            # node Reroute.004
            reroute_004_1 = _mn_utils_rotate_res.nodes.new("NodeReroute")
            reroute_004_1.name = "Reroute.004"
            # node Group Output
            group_output_18 = _mn_utils_rotate_res.nodes.new("NodeGroupOutput")
            group_output_18.name = "Group Output"
            group_output_18.is_active_output = True

            # node Vector Rotate.002
            vector_rotate_002 = _mn_utils_rotate_res.nodes.new("ShaderNodeVectorRotate")
            vector_rotate_002.name = "Vector Rotate.002"
            vector_rotate_002.invert = False
            vector_rotate_002.rotation_type = "EULER_XYZ"

            # node Vector Math.001
            vector_math_001_1 = _mn_utils_rotate_res.nodes.new("ShaderNodeVectorMath")
            vector_math_001_1.name = "Vector Math.001"
            vector_math_001_1.operation = "SCALE"

            # node Group.004
            group_004 = _mn_utils_rotate_res.nodes.new("GeometryNodeGroup")
            group_004.name = "Group.004"
            group_004.node_tree = mn_animate_noise_repeat
            # Input_3
            group_004.inputs[1].default_value = 1.0
            # Input_4
            group_004.inputs[2].default_value = 1.0
            # Input_5
            group_004.inputs[3].default_value = 1.9799998998641968

            # node Vector Math.002
            vector_math_002_1 = _mn_utils_rotate_res.nodes.new("ShaderNodeVectorMath")
            vector_math_002_1.name = "Vector Math.002"
            vector_math_002_1.mute = True
            vector_math_002_1.operation = "SCALE"

            # node Compare
            compare_3 = _mn_utils_rotate_res.nodes.new("FunctionNodeCompare")
            compare_3.name = "Compare"
            compare_3.data_type = "INT"
            compare_3.mode = "ELEMENT"
            compare_3.operation = "EQUAL"
            # B_INT
            compare_3.inputs[3].default_value = 3

            # node Group
            group_7 = _mn_utils_rotate_res.nodes.new("GeometryNodeGroup")
            group_7.name = "Group"
            group_7.node_tree = mn_animate_noise_repeat
            # Input_1
            group_7.inputs[0].default_value = 1.0
            # Input_3
            group_7.inputs[1].default_value = 2.0
            # Input_4
            group_7.inputs[2].default_value = 1.0
            # Input_5
            group_7.inputs[3].default_value = 1.9799998998641968

            # node Compare.002
            compare_002_2 = _mn_utils_rotate_res.nodes.new("FunctionNodeCompare")
            compare_002_2.name = "Compare.002"
            compare_002_2.data_type = "INT"
            compare_002_2.mode = "ELEMENT"
            compare_002_2.operation = "GREATER_THAN"
            # B_INT
            compare_002_2.inputs[3].default_value = 4

            # node Compare.003
            compare_003_2 = _mn_utils_rotate_res.nodes.new("FunctionNodeCompare")
            compare_003_2.name = "Compare.003"
            compare_003_2.data_type = "INT"
            compare_003_2.mode = "ELEMENT"
            compare_003_2.operation = "NOT_EQUAL"
            # B_INT
            compare_003_2.inputs[3].default_value = 38

            # node Boolean Math.002
            boolean_math_002_2 = _mn_utils_rotate_res.nodes.new(
                "FunctionNodeBooleanMath"
            )
            boolean_math_002_2.name = "Boolean Math.002"
            boolean_math_002_2.operation = "AND"

            # node Boolean Math.003
            boolean_math_003_1 = _mn_utils_rotate_res.nodes.new(
                "FunctionNodeBooleanMath"
            )
            boolean_math_003_1.name = "Boolean Math.003"
            boolean_math_003_1.operation = "AND"

            # node Reroute.005
            reroute_005_1 = _mn_utils_rotate_res.nodes.new("NodeReroute")
            reroute_005_1.name = "Reroute.005"
            # node Vector Math
            vector_math_2 = _mn_utils_rotate_res.nodes.new("ShaderNodeVectorMath")
            vector_math_2.name = "Vector Math"
            vector_math_2.hide = True
            vector_math_2.operation = "SUBTRACT"

            # node Math.001
            math_001_4 = _mn_utils_rotate_res.nodes.new("ShaderNodeMath")
            math_001_4.name = "Math.001"
            math_001_4.hide = True
            math_001_4.operation = "MULTIPLY"
            math_001_4.use_clamp = False

            # node Math.002
            math_002_2 = _mn_utils_rotate_res.nodes.new("ShaderNodeMath")
            math_002_2.name = "Math.002"
            math_002_2.hide = True
            math_002_2.operation = "MULTIPLY"
            math_002_2.use_clamp = False

            # node Reroute.007
            reroute_007_1 = _mn_utils_rotate_res.nodes.new("NodeReroute")
            reroute_007_1.name = "Reroute.007"
            # node Reroute.006
            reroute_006_1 = _mn_utils_rotate_res.nodes.new("NodeReroute")
            reroute_006_1.name = "Reroute.006"
            # node Group Input
            group_input_18 = _mn_utils_rotate_res.nodes.new("NodeGroupInput")
            group_input_18.name = "Group Input"

            # node Math
            math_6 = _mn_utils_rotate_res.nodes.new("ShaderNodeMath")
            math_6.name = "Math"
            math_6.operation = "MULTIPLY"
            math_6.use_clamp = False

            # node Mix
            mix_1 = _mn_utils_rotate_res.nodes.new("ShaderNodeMix")
            mix_1.name = "Mix"
            mix_1.blend_type = "MIX"
            mix_1.clamp_factor = True
            mix_1.clamp_result = False
            mix_1.data_type = "FLOAT"
            mix_1.factor_mode = "UNIFORM"
            # A_Float
            mix_1.inputs[2].default_value = 1.0

            # node Map Range
            map_range_2 = _mn_utils_rotate_res.nodes.new("ShaderNodeMapRange")
            map_range_2.name = "Map Range"
            map_range_2.hide = True
            map_range_2.clamp = True
            map_range_2.data_type = "FLOAT"
            map_range_2.interpolation_type = "SMOOTHERSTEP"
            # From Min
            map_range_2.inputs[1].default_value = 1.0
            # From Max
            map_range_2.inputs[2].default_value = 100.0
            # To Min
            map_range_2.inputs[3].default_value = 0.0
            # To Max
            map_range_2.inputs[4].default_value = 1.0

            # node Reroute
            reroute_4 = _mn_utils_rotate_res.nodes.new("NodeReroute")
            reroute_4.name = "Reroute"
            # node Group.002
            group_002_1 = _mn_utils_rotate_res.nodes.new("GeometryNodeGroup")
            group_002_1.name = "Group.002"
            group_002_1.node_tree = _mn_utils_aa_atom_pos

            # node Group.003
            group_003 = _mn_utils_rotate_res.nodes.new("GeometryNodeGroup")
            group_003.name = "Group.003"
            group_003.hide = True
            group_003.node_tree = _mn_utils_aa_atom_pos

            # node Group.001
            group_001_2 = _mn_utils_rotate_res.nodes.new("GeometryNodeGroup")
            group_001_2.name = "Group.001"
            group_001_2.node_tree = is_peptide
            # Socket_1
            group_001_2.inputs[0].default_value = True
            # Socket_3
            group_001_2.inputs[1].default_value = False

            # Set locations
            named_attribute_001_2.location = (-900.0, 580.0)
            reroute_001_2.location = (-23.38579559326172, -430.73773193359375)
            reroute_002_2.location = (-825.0, -440.0)
            reroute_003_1.location = (-5.0, -460.0)
            boolean_math_2.location = (-480.0, 320.0)
            compare_001_2.location = (-640.0, 320.0)
            random_value_1.location = (-205.0, -420.0)
            boolean_math_001_2.location = (440.0, 280.0)
            position_1.location = (440.0, 120.0)
            vector_rotate.location = (680.0, 160.0)
            reroute_004_1.location = (640.0, 40.0)
            group_output_18.location = (1233.2698974609375, 262.38323974609375)
            vector_rotate_002.location = (993.2698364257812, 182.3832244873047)
            vector_math_001_1.location = (553.43408203125, -62.642765045166016)
            group_004.location = (300.0, -140.0)
            vector_math_002_1.location = (773.0, -45.8553466796875)
            compare_3.location = (780.0, -200.0)
            group_7.location = (80.0, -140.0)
            compare_002_2.location = (-640.0, 480.0)
            compare_003_2.location = (-640.0, 640.0)
            boolean_math_002_2.location = (-280.5462951660156, 430.50006103515625)
            boolean_math_003_1.location = (-87.18310546875, 553.9082641601562)
            reroute_005_1.location = (320.0, 20.0)
            vector_math_2.location = (360.0, 0.0)
            math_001_4.location = (360.0, -40.0)
            math_002_2.location = (140.00001525878906, -59.452919006347656)
            reroute_007_1.location = (20.0, -200.0)
            reroute_006_1.location = (20.0, -120.0)
            group_input_18.location = (-1261.5419921875, 0.30535888671875)
            math_6.location = (-152.04693603515625, -27.359119415283203)
            mix_1.location = (-361.2230224609375, 52.487037658691406)
            map_range_2.location = (-361.6744384765625, -140.6511688232422)
            reroute_4.location = (-980.0, 0.0)
            group_002_1.location = (-840.0, -60.0)
            group_003.location = (-840.0, -20.0)
            group_001_2.location = (-640.0, 160.0)

            # initialize _mn_utils_rotate_res links
            # boolean_math_001_2.Boolean -> group_output_18.Selection
            _mn_utils_rotate_res.links.new(
                boolean_math_001_2.outputs[0], group_output_18.inputs[0]
            )
            # group_input_18.Selection -> boolean_math_001_2.Boolean
            _mn_utils_rotate_res.links.new(
                group_input_18.outputs[0], boolean_math_001_2.inputs[1]
            )
            # position_1.Position -> vector_rotate.Vector
            _mn_utils_rotate_res.links.new(
                position_1.outputs[0], vector_rotate.inputs[0]
            )
            # reroute_004_1.Output -> vector_rotate.Center
            _mn_utils_rotate_res.links.new(
                reroute_004_1.outputs[0], vector_rotate.inputs[1]
            )
            # named_attribute_001_2.Attribute -> compare_001_2.A
            _mn_utils_rotate_res.links.new(
                named_attribute_001_2.outputs[0], compare_001_2.inputs[2]
            )
            # reroute_4.Output -> compare_001_2.B
            _mn_utils_rotate_res.links.new(
                reroute_4.outputs[0], compare_001_2.inputs[3]
            )
            # compare_001_2.Result -> boolean_math_2.Boolean
            _mn_utils_rotate_res.links.new(
                compare_001_2.outputs[0], boolean_math_2.inputs[0]
            )
            # group_input_18.atom_name rotation -> reroute_4.Input
            _mn_utils_rotate_res.links.new(
                group_input_18.outputs[1], reroute_4.inputs[0]
            )
            # vector_math_2.Vector -> vector_rotate.Axis
            _mn_utils_rotate_res.links.new(
                vector_math_2.outputs[0], vector_rotate.inputs[2]
            )
            # reroute_001_2.Output -> group_7.Vector
            _mn_utils_rotate_res.links.new(reroute_001_2.outputs[0], group_7.inputs[4])
            # reroute_001_2.Output -> group_004.Vector
            _mn_utils_rotate_res.links.new(
                reroute_001_2.outputs[0], group_004.inputs[4]
            )
            # vector_rotate_002.Vector -> group_output_18.Position
            _mn_utils_rotate_res.links.new(
                vector_rotate_002.outputs[0], group_output_18.inputs[1]
            )
            # group_003.Position -> vector_math_2.Vector
            _mn_utils_rotate_res.links.new(
                group_003.outputs[0], vector_math_2.inputs[1]
            )
            # reroute_005_1.Output -> vector_math_2.Vector
            _mn_utils_rotate_res.links.new(
                reroute_005_1.outputs[0], vector_math_2.inputs[0]
            )
            # reroute_4.Output -> group_002_1.atom_name
            _mn_utils_rotate_res.links.new(reroute_4.outputs[0], group_002_1.inputs[0])
            # group_input_18.atom_name axis -> group_003.atom_name
            _mn_utils_rotate_res.links.new(
                group_input_18.outputs[2], group_003.inputs[0]
            )
            # vector_rotate.Vector -> vector_rotate_002.Vector
            _mn_utils_rotate_res.links.new(
                vector_rotate.outputs[0], vector_rotate_002.inputs[0]
            )
            # reroute_004_1.Output -> vector_rotate_002.Center
            _mn_utils_rotate_res.links.new(
                reroute_004_1.outputs[0], vector_rotate_002.inputs[1]
            )
            # reroute_003_1.Output -> group_7.Animate 0..1
            _mn_utils_rotate_res.links.new(reroute_003_1.outputs[0], group_7.inputs[6])
            # reroute_003_1.Output -> group_004.Animate 0..1
            _mn_utils_rotate_res.links.new(
                reroute_003_1.outputs[0], group_004.inputs[6]
            )
            # group_002_1.Group Index -> random_value_1.ID
            _mn_utils_rotate_res.links.new(
                group_002_1.outputs[1], random_value_1.inputs[7]
            )
            # random_value_1.Value -> reroute_001_2.Input
            _mn_utils_rotate_res.links.new(
                random_value_1.outputs[0], reroute_001_2.inputs[0]
            )
            # group_input_18.Animate 0..1 -> reroute_002_2.Input
            _mn_utils_rotate_res.links.new(
                group_input_18.outputs[8], reroute_002_2.inputs[0]
            )
            # reroute_002_2.Output -> reroute_003_1.Input
            _mn_utils_rotate_res.links.new(
                reroute_002_2.outputs[0], reroute_003_1.inputs[0]
            )
            # reroute_4.Output -> random_value_1.Seed
            _mn_utils_rotate_res.links.new(
                reroute_4.outputs[0], random_value_1.inputs[8]
            )
            # boolean_math_2.Boolean -> boolean_math_002_2.Boolean
            _mn_utils_rotate_res.links.new(
                boolean_math_2.outputs[0], boolean_math_002_2.inputs[1]
            )
            # named_attribute_001_2.Attribute -> compare_002_2.A
            _mn_utils_rotate_res.links.new(
                named_attribute_001_2.outputs[0], compare_002_2.inputs[2]
            )
            # compare_002_2.Result -> boolean_math_002_2.Boolean
            _mn_utils_rotate_res.links.new(
                compare_002_2.outputs[0], boolean_math_002_2.inputs[0]
            )
            # reroute_005_1.Output -> reroute_004_1.Input
            _mn_utils_rotate_res.links.new(
                reroute_005_1.outputs[0], reroute_004_1.inputs[0]
            )
            # group_002_1.Position -> reroute_005_1.Input
            _mn_utils_rotate_res.links.new(
                group_002_1.outputs[0], reroute_005_1.inputs[0]
            )
            # group_input_18.Amplitude -> math_6.Value
            _mn_utils_rotate_res.links.new(group_input_18.outputs[4], math_6.inputs[1])
            # group_7.Noise Float -> math_001_4.Value
            _mn_utils_rotate_res.links.new(group_7.outputs[0], math_001_4.inputs[1])
            # math_001_4.Value -> vector_rotate.Angle
            _mn_utils_rotate_res.links.new(
                math_001_4.outputs[0], vector_rotate.inputs[3]
            )
            # group_input_18.Speed -> group_7.Speed
            _mn_utils_rotate_res.links.new(group_input_18.outputs[7], group_7.inputs[5])
            # group_input_18.Speed -> group_004.Speed
            _mn_utils_rotate_res.links.new(
                group_input_18.outputs[7], group_004.inputs[5]
            )
            # group_input_18.Amp. Euler -> group_004.Amplitude
            _mn_utils_rotate_res.links.new(
                group_input_18.outputs[6], group_004.inputs[0]
            )
            # group_004.Noise Vector -> vector_math_001_1.Vector
            _mn_utils_rotate_res.links.new(
                group_004.outputs[1], vector_math_001_1.inputs[0]
            )
            # reroute_006_1.Output -> vector_math_001_1.Scale
            _mn_utils_rotate_res.links.new(
                reroute_006_1.outputs[0], vector_math_001_1.inputs[3]
            )
            # vector_math_002_1.Vector -> vector_rotate_002.Rotation
            _mn_utils_rotate_res.links.new(
                vector_math_002_1.outputs[0], vector_rotate_002.inputs[4]
            )
            # math_002_2.Value -> math_001_4.Value
            _mn_utils_rotate_res.links.new(math_002_2.outputs[0], math_001_4.inputs[0])
            # math_6.Value -> reroute_006_1.Input
            _mn_utils_rotate_res.links.new(math_6.outputs[0], reroute_006_1.inputs[0])
            # group_002_1.b_factor -> map_range_2.Value
            _mn_utils_rotate_res.links.new(
                group_002_1.outputs[2], map_range_2.inputs[0]
            )
            # vector_math_001_1.Vector -> vector_math_002_1.Vector
            _mn_utils_rotate_res.links.new(
                vector_math_001_1.outputs[0], vector_math_002_1.inputs[0]
            )
            # compare_3.Result -> vector_math_002_1.Scale
            _mn_utils_rotate_res.links.new(
                compare_3.outputs[0], vector_math_002_1.inputs[3]
            )
            # group_002_1.Integer -> compare_3.A
            _mn_utils_rotate_res.links.new(group_002_1.outputs[3], compare_3.inputs[2])
            # named_attribute_001_2.Attribute -> compare_003_2.A
            _mn_utils_rotate_res.links.new(
                named_attribute_001_2.outputs[0], compare_003_2.inputs[2]
            )
            # boolean_math_002_2.Boolean -> boolean_math_003_1.Boolean
            _mn_utils_rotate_res.links.new(
                boolean_math_002_2.outputs[0], boolean_math_003_1.inputs[1]
            )
            # compare_003_2.Result -> boolean_math_003_1.Boolean
            _mn_utils_rotate_res.links.new(
                compare_003_2.outputs[0], boolean_math_003_1.inputs[0]
            )
            # boolean_math_003_1.Boolean -> boolean_math_001_2.Boolean
            _mn_utils_rotate_res.links.new(
                boolean_math_003_1.outputs[0], boolean_math_001_2.inputs[0]
            )
            # reroute_006_1.Output -> math_002_2.Value
            _mn_utils_rotate_res.links.new(
                reroute_006_1.outputs[0], math_002_2.inputs[0]
            )
            # reroute_007_1.Output -> math_002_2.Value
            _mn_utils_rotate_res.links.new(
                reroute_007_1.outputs[0], math_002_2.inputs[1]
            )
            # group_input_18.Amp. Axis -> reroute_007_1.Input
            _mn_utils_rotate_res.links.new(
                group_input_18.outputs[5], reroute_007_1.inputs[0]
            )
            # map_range_2.Result -> mix_1.B
            _mn_utils_rotate_res.links.new(map_range_2.outputs[0], mix_1.inputs[3])
            # mix_1.Result -> math_6.Value
            _mn_utils_rotate_res.links.new(mix_1.outputs[0], math_6.inputs[0])
            # group_input_18.Scale b_factor -> mix_1.Factor
            _mn_utils_rotate_res.links.new(group_input_18.outputs[3], mix_1.inputs[0])
            # group_001_2.Selection -> boolean_math_2.Boolean
            _mn_utils_rotate_res.links.new(
                group_001_2.outputs[0], boolean_math_2.inputs[1]
            )
            return _mn_utils_rotate_res

        _mn_utils_rotate_res = _mn_utils_rotate_res_node_group()

        # initialize _mn_select_res_name_peptide node group
        def _mn_select_res_name_peptide_node_group():
            _mn_select_res_name_peptide = bpy.data.node_groups.new(
                type="GeometryNodeTree", name=".MN_select_res_name_peptide"
            )

            _mn_select_res_name_peptide.color_tag = "NONE"
            _mn_select_res_name_peptide.description = ""

            # _mn_select_res_name_peptide interface
            # Socket Selection
            selection_socket_11 = _mn_select_res_name_peptide.interface.new_socket(
                name="Selection", in_out="OUTPUT", socket_type="NodeSocketBool"
            )
            selection_socket_11.attribute_domain = "POINT"
            selection_socket_11.description = "The calculated selection"

            # Socket Inverted
            inverted_socket_1 = _mn_select_res_name_peptide.interface.new_socket(
                name="Inverted", in_out="OUTPUT", socket_type="NodeSocketBool"
            )
            inverted_socket_1.attribute_domain = "POINT"
            inverted_socket_1.description = "The inverse of the calculated selection"

            # Socket ALA
            ala_socket = _mn_select_res_name_peptide.interface.new_socket(
                name="ALA", in_out="INPUT", socket_type="NodeSocketBool"
            )
            ala_socket.attribute_domain = "POINT"
            ala_socket.description = "Select the AA residue ALA"

            # Socket ARG
            arg_socket = _mn_select_res_name_peptide.interface.new_socket(
                name="ARG", in_out="INPUT", socket_type="NodeSocketBool"
            )
            arg_socket.attribute_domain = "POINT"
            arg_socket.description = "Select the AA residue ARG"

            # Socket ASN
            asn_socket = _mn_select_res_name_peptide.interface.new_socket(
                name="ASN", in_out="INPUT", socket_type="NodeSocketBool"
            )
            asn_socket.attribute_domain = "POINT"
            asn_socket.description = "Select the AA residue ASN"

            # Socket ASP
            asp_socket = _mn_select_res_name_peptide.interface.new_socket(
                name="ASP", in_out="INPUT", socket_type="NodeSocketBool"
            )
            asp_socket.attribute_domain = "POINT"
            asp_socket.description = "Select the AA residue ASP"

            # Socket CYS
            cys_socket = _mn_select_res_name_peptide.interface.new_socket(
                name="CYS", in_out="INPUT", socket_type="NodeSocketBool"
            )
            cys_socket.attribute_domain = "POINT"
            cys_socket.description = "Select the AA residue CYS"

            # Socket GLU
            glu_socket = _mn_select_res_name_peptide.interface.new_socket(
                name="GLU", in_out="INPUT", socket_type="NodeSocketBool"
            )
            glu_socket.attribute_domain = "POINT"
            glu_socket.description = "Select the AA residue GLU"

            # Socket GLN
            gln_socket = _mn_select_res_name_peptide.interface.new_socket(
                name="GLN", in_out="INPUT", socket_type="NodeSocketBool"
            )
            gln_socket.attribute_domain = "POINT"
            gln_socket.description = "Select the AA residue GLN"

            # Socket GLY
            gly_socket = _mn_select_res_name_peptide.interface.new_socket(
                name="GLY", in_out="INPUT", socket_type="NodeSocketBool"
            )
            gly_socket.attribute_domain = "POINT"
            gly_socket.description = "Select the AA residue GLY"

            # Socket HIS
            his_socket = _mn_select_res_name_peptide.interface.new_socket(
                name="HIS", in_out="INPUT", socket_type="NodeSocketBool"
            )
            his_socket.attribute_domain = "POINT"
            his_socket.description = "Select the AA residue HIS"

            # Socket ILE
            ile_socket = _mn_select_res_name_peptide.interface.new_socket(
                name="ILE", in_out="INPUT", socket_type="NodeSocketBool"
            )
            ile_socket.attribute_domain = "POINT"
            ile_socket.description = "Select the AA residue ILE"

            # Socket LEU
            leu_socket = _mn_select_res_name_peptide.interface.new_socket(
                name="LEU", in_out="INPUT", socket_type="NodeSocketBool"
            )
            leu_socket.attribute_domain = "POINT"
            leu_socket.description = "Select the AA residue LEU"

            # Socket LYS
            lys_socket = _mn_select_res_name_peptide.interface.new_socket(
                name="LYS", in_out="INPUT", socket_type="NodeSocketBool"
            )
            lys_socket.attribute_domain = "POINT"
            lys_socket.description = "Select the AA residue LYS"

            # Socket MET
            met_socket = _mn_select_res_name_peptide.interface.new_socket(
                name="MET", in_out="INPUT", socket_type="NodeSocketBool"
            )
            met_socket.attribute_domain = "POINT"
            met_socket.description = "Select the AA residue MET"

            # Socket PHE
            phe_socket = _mn_select_res_name_peptide.interface.new_socket(
                name="PHE", in_out="INPUT", socket_type="NodeSocketBool"
            )
            phe_socket.attribute_domain = "POINT"
            phe_socket.description = "Select the AA residue PHE"

            # Socket PRO
            pro_socket = _mn_select_res_name_peptide.interface.new_socket(
                name="PRO", in_out="INPUT", socket_type="NodeSocketBool"
            )
            pro_socket.attribute_domain = "POINT"
            pro_socket.description = "Select the AA residue PRO"

            # Socket SER
            ser_socket = _mn_select_res_name_peptide.interface.new_socket(
                name="SER", in_out="INPUT", socket_type="NodeSocketBool"
            )
            ser_socket.attribute_domain = "POINT"
            ser_socket.description = "Select the AA residue SER"

            # Socket THR
            thr_socket = _mn_select_res_name_peptide.interface.new_socket(
                name="THR", in_out="INPUT", socket_type="NodeSocketBool"
            )
            thr_socket.attribute_domain = "POINT"
            thr_socket.description = "Select the AA residue THR"

            # Socket TRP
            trp_socket = _mn_select_res_name_peptide.interface.new_socket(
                name="TRP", in_out="INPUT", socket_type="NodeSocketBool"
            )
            trp_socket.attribute_domain = "POINT"
            trp_socket.description = "Select the AA residue TRP"

            # Socket TYR
            tyr_socket = _mn_select_res_name_peptide.interface.new_socket(
                name="TYR", in_out="INPUT", socket_type="NodeSocketBool"
            )
            tyr_socket.attribute_domain = "POINT"
            tyr_socket.description = "Select the AA residue TYR"

            # Socket VAL
            val_socket = _mn_select_res_name_peptide.interface.new_socket(
                name="VAL", in_out="INPUT", socket_type="NodeSocketBool"
            )
            val_socket.attribute_domain = "POINT"
            val_socket.description = "Select the AA residue VAL"

            # initialize _mn_select_res_name_peptide nodes
            # node Reroute.018
            reroute_018_1 = _mn_select_res_name_peptide.nodes.new("NodeReroute")
            reroute_018_1.name = "Reroute.018"
            # node Group Output
            group_output_19 = _mn_select_res_name_peptide.nodes.new("NodeGroupOutput")
            group_output_19.name = "Group Output"
            group_output_19.is_active_output = True

            # node Boolean Math.001
            boolean_math_001_3 = _mn_select_res_name_peptide.nodes.new(
                "FunctionNodeBooleanMath"
            )
            boolean_math_001_3.name = "Boolean Math.001"
            boolean_math_001_3.operation = "NOT"

            # node Named Attribute
            named_attribute_6 = _mn_select_res_name_peptide.nodes.new(
                "GeometryNodeInputNamedAttribute"
            )
            named_attribute_6.name = "Named Attribute"
            named_attribute_6.data_type = "INT"
            # Name
            named_attribute_6.inputs[0].default_value = "res_name"

            # node Group Input
            group_input_19 = _mn_select_res_name_peptide.nodes.new("NodeGroupInput")
            group_input_19.name = "Group Input"

            # node Index Switch
            index_switch_1 = _mn_select_res_name_peptide.nodes.new(
                "GeometryNodeIndexSwitch"
            )
            index_switch_1.name = "Index Switch"
            index_switch_1.data_type = "BOOLEAN"
            index_switch_1.index_switch_items.clear()
            index_switch_1.index_switch_items.new()
            index_switch_1.index_switch_items.new()
            index_switch_1.index_switch_items.new()
            index_switch_1.index_switch_items.new()
            index_switch_1.index_switch_items.new()
            index_switch_1.index_switch_items.new()
            index_switch_1.index_switch_items.new()
            index_switch_1.index_switch_items.new()
            index_switch_1.index_switch_items.new()
            index_switch_1.index_switch_items.new()
            index_switch_1.index_switch_items.new()
            index_switch_1.index_switch_items.new()
            index_switch_1.index_switch_items.new()
            index_switch_1.index_switch_items.new()
            index_switch_1.index_switch_items.new()
            index_switch_1.index_switch_items.new()
            index_switch_1.index_switch_items.new()
            index_switch_1.index_switch_items.new()
            index_switch_1.index_switch_items.new()
            index_switch_1.index_switch_items.new()

            # Set locations
            reroute_018_1.location = (2740.0, 0.0)
            group_output_19.location = (3040.0, 40.0)
            boolean_math_001_3.location = (2840.403076171875, -31.331174850463867)
            named_attribute_6.location = (2260.0, 80.0)
            group_input_19.location = (2260.0, -60.0)
            index_switch_1.location = (2500.0, 40.0)

            # initialize _mn_select_res_name_peptide links
            # reroute_018_1.Output -> boolean_math_001_3.Boolean
            _mn_select_res_name_peptide.links.new(
                reroute_018_1.outputs[0], boolean_math_001_3.inputs[0]
            )
            # reroute_018_1.Output -> group_output_19.Selection
            _mn_select_res_name_peptide.links.new(
                reroute_018_1.outputs[0], group_output_19.inputs[0]
            )
            # boolean_math_001_3.Boolean -> group_output_19.Inverted
            _mn_select_res_name_peptide.links.new(
                boolean_math_001_3.outputs[0], group_output_19.inputs[1]
            )
            # named_attribute_6.Attribute -> index_switch_1.Index
            _mn_select_res_name_peptide.links.new(
                named_attribute_6.outputs[0], index_switch_1.inputs[0]
            )
            # group_input_19.ALA -> index_switch_1.0
            _mn_select_res_name_peptide.links.new(
                group_input_19.outputs[0], index_switch_1.inputs[1]
            )
            # group_input_19.ARG -> index_switch_1.1
            _mn_select_res_name_peptide.links.new(
                group_input_19.outputs[1], index_switch_1.inputs[2]
            )
            # group_input_19.ASN -> index_switch_1.2
            _mn_select_res_name_peptide.links.new(
                group_input_19.outputs[2], index_switch_1.inputs[3]
            )
            # group_input_19.ASP -> index_switch_1.3
            _mn_select_res_name_peptide.links.new(
                group_input_19.outputs[3], index_switch_1.inputs[4]
            )
            # group_input_19.CYS -> index_switch_1.4
            _mn_select_res_name_peptide.links.new(
                group_input_19.outputs[4], index_switch_1.inputs[5]
            )
            # group_input_19.GLU -> index_switch_1.5
            _mn_select_res_name_peptide.links.new(
                group_input_19.outputs[5], index_switch_1.inputs[6]
            )
            # group_input_19.GLN -> index_switch_1.6
            _mn_select_res_name_peptide.links.new(
                group_input_19.outputs[6], index_switch_1.inputs[7]
            )
            # group_input_19.GLY -> index_switch_1.7
            _mn_select_res_name_peptide.links.new(
                group_input_19.outputs[7], index_switch_1.inputs[8]
            )
            # group_input_19.HIS -> index_switch_1.8
            _mn_select_res_name_peptide.links.new(
                group_input_19.outputs[8], index_switch_1.inputs[9]
            )
            # group_input_19.ILE -> index_switch_1.9
            _mn_select_res_name_peptide.links.new(
                group_input_19.outputs[9], index_switch_1.inputs[10]
            )
            # group_input_19.LEU -> index_switch_1.10
            _mn_select_res_name_peptide.links.new(
                group_input_19.outputs[10], index_switch_1.inputs[11]
            )
            # group_input_19.LYS -> index_switch_1.11
            _mn_select_res_name_peptide.links.new(
                group_input_19.outputs[11], index_switch_1.inputs[12]
            )
            # group_input_19.MET -> index_switch_1.12
            _mn_select_res_name_peptide.links.new(
                group_input_19.outputs[12], index_switch_1.inputs[13]
            )
            # group_input_19.PHE -> index_switch_1.13
            _mn_select_res_name_peptide.links.new(
                group_input_19.outputs[13], index_switch_1.inputs[14]
            )
            # group_input_19.PRO -> index_switch_1.14
            _mn_select_res_name_peptide.links.new(
                group_input_19.outputs[14], index_switch_1.inputs[15]
            )
            # group_input_19.SER -> index_switch_1.15
            _mn_select_res_name_peptide.links.new(
                group_input_19.outputs[15], index_switch_1.inputs[16]
            )
            # group_input_19.THR -> index_switch_1.16
            _mn_select_res_name_peptide.links.new(
                group_input_19.outputs[16], index_switch_1.inputs[17]
            )
            # group_input_19.TRP -> index_switch_1.17
            _mn_select_res_name_peptide.links.new(
                group_input_19.outputs[17], index_switch_1.inputs[18]
            )
            # group_input_19.TYR -> index_switch_1.18
            _mn_select_res_name_peptide.links.new(
                group_input_19.outputs[18], index_switch_1.inputs[19]
            )
            # group_input_19.VAL -> index_switch_1.19
            _mn_select_res_name_peptide.links.new(
                group_input_19.outputs[19], index_switch_1.inputs[20]
            )
            # index_switch_1.Output -> reroute_018_1.Input
            _mn_select_res_name_peptide.links.new(
                index_switch_1.outputs[0], reroute_018_1.inputs[0]
            )
            return _mn_select_res_name_peptide

        _mn_select_res_name_peptide = _mn_select_res_name_peptide_node_group()

        # initialize _mn_animate_wiggle_mask_res node group
        def _mn_animate_wiggle_mask_res_node_group():
            _mn_animate_wiggle_mask_res = bpy.data.node_groups.new(
                type="GeometryNodeTree", name=".MN_animate_wiggle_mask_res"
            )

            _mn_animate_wiggle_mask_res.color_tag = "NONE"
            _mn_animate_wiggle_mask_res.description = ""

            # _mn_animate_wiggle_mask_res interface
            # Socket Result
            result_socket_1 = _mn_animate_wiggle_mask_res.interface.new_socket(
                name="Result", in_out="OUTPUT", socket_type="NodeSocketBool"
            )
            result_socket_1.attribute_domain = "POINT"

            # Socket A
            a_socket_1 = _mn_animate_wiggle_mask_res.interface.new_socket(
                name="A", in_out="INPUT", socket_type="NodeSocketInt"
            )
            a_socket_1.subtype = "NONE"
            a_socket_1.default_value = 0
            a_socket_1.min_value = -2147483648
            a_socket_1.max_value = 2147483647
            a_socket_1.attribute_domain = "POINT"

            # initialize _mn_animate_wiggle_mask_res nodes
            # node Group Input
            group_input_20 = _mn_animate_wiggle_mask_res.nodes.new("NodeGroupInput")
            group_input_20.name = "Group Input"

            # node Group.013
            group_013 = _mn_animate_wiggle_mask_res.nodes.new("GeometryNodeGroup")
            group_013.name = "Group.013"
            group_013.node_tree = _mn_select_res_name_peptide
            # Input_7
            group_013.inputs[0].default_value = True
            # Input_8
            group_013.inputs[1].default_value = True
            # Input_9
            group_013.inputs[2].default_value = True
            # Input_10
            group_013.inputs[3].default_value = True
            # Input_11
            group_013.inputs[4].default_value = True
            # Input_12
            group_013.inputs[5].default_value = True
            # Input_13
            group_013.inputs[6].default_value = True
            # Input_14
            group_013.inputs[7].default_value = False
            # Input_15
            group_013.inputs[8].default_value = True
            # Input_16
            group_013.inputs[9].default_value = True
            # Input_17
            group_013.inputs[10].default_value = True
            # Input_18
            group_013.inputs[11].default_value = True
            # Input_19
            group_013.inputs[12].default_value = True
            # Input_20
            group_013.inputs[13].default_value = True
            # Input_21
            group_013.inputs[14].default_value = False
            # Input_22
            group_013.inputs[15].default_value = True
            # Input_23
            group_013.inputs[16].default_value = True
            # Input_24
            group_013.inputs[17].default_value = True
            # Input_25
            group_013.inputs[18].default_value = True
            # Input_26
            group_013.inputs[19].default_value = True

            # node Group.011
            group_011 = _mn_animate_wiggle_mask_res.nodes.new("GeometryNodeGroup")
            group_011.name = "Group.011"
            group_011.node_tree = _mn_select_res_name_peptide
            # Input_7
            group_011.inputs[0].default_value = False
            # Input_8
            group_011.inputs[1].default_value = True
            # Input_9
            group_011.inputs[2].default_value = False
            # Input_10
            group_011.inputs[3].default_value = False
            # Input_11
            group_011.inputs[4].default_value = False
            # Input_12
            group_011.inputs[5].default_value = False
            # Input_13
            group_011.inputs[6].default_value = True
            # Input_14
            group_011.inputs[7].default_value = False
            # Input_15
            group_011.inputs[8].default_value = False
            # Input_16
            group_011.inputs[9].default_value = False
            # Input_17
            group_011.inputs[10].default_value = False
            # Input_18
            group_011.inputs[11].default_value = True
            # Input_19
            group_011.inputs[12].default_value = False
            # Input_20
            group_011.inputs[13].default_value = False
            # Input_21
            group_011.inputs[14].default_value = False
            # Input_22
            group_011.inputs[15].default_value = False
            # Input_23
            group_011.inputs[16].default_value = False
            # Input_24
            group_011.inputs[17].default_value = False
            # Input_25
            group_011.inputs[18].default_value = False
            # Input_26
            group_011.inputs[19].default_value = False

            # node Group.012
            group_012 = _mn_animate_wiggle_mask_res.nodes.new("GeometryNodeGroup")
            group_012.name = "Group.012"
            group_012.node_tree = _mn_select_res_name_peptide
            # Input_7
            group_012.inputs[0].default_value = False
            # Input_8
            group_012.inputs[1].default_value = False
            # Input_9
            group_012.inputs[2].default_value = False
            # Input_10
            group_012.inputs[3].default_value = False
            # Input_11
            group_012.inputs[4].default_value = False
            # Input_12
            group_012.inputs[5].default_value = False
            # Input_13
            group_012.inputs[6].default_value = False
            # Input_14
            group_012.inputs[7].default_value = False
            # Input_15
            group_012.inputs[8].default_value = False
            # Input_16
            group_012.inputs[9].default_value = True
            # Input_17
            group_012.inputs[10].default_value = False
            # Input_18
            group_012.inputs[11].default_value = True
            # Input_19
            group_012.inputs[12].default_value = False
            # Input_20
            group_012.inputs[13].default_value = False
            # Input_21
            group_012.inputs[14].default_value = False
            # Input_22
            group_012.inputs[15].default_value = False
            # Input_23
            group_012.inputs[16].default_value = False
            # Input_24
            group_012.inputs[17].default_value = False
            # Input_25
            group_012.inputs[18].default_value = False
            # Input_26
            group_012.inputs[19].default_value = False

            # node Group.010
            group_010 = _mn_animate_wiggle_mask_res.nodes.new("GeometryNodeGroup")
            group_010.name = "Group.010"
            group_010.node_tree = _mn_select_res_name_peptide
            # Input_7
            group_010.inputs[0].default_value = True
            # Input_8
            group_010.inputs[1].default_value = True
            # Input_9
            group_010.inputs[2].default_value = True
            # Input_10
            group_010.inputs[3].default_value = True
            # Input_11
            group_010.inputs[4].default_value = False
            # Input_12
            group_010.inputs[5].default_value = True
            # Input_13
            group_010.inputs[6].default_value = True
            # Input_14
            group_010.inputs[7].default_value = False
            # Input_15
            group_010.inputs[8].default_value = True
            # Input_16
            group_010.inputs[9].default_value = False
            # Input_17
            group_010.inputs[10].default_value = True
            # Input_18
            group_010.inputs[11].default_value = True
            # Input_19
            group_010.inputs[12].default_value = True
            # Input_20
            group_010.inputs[13].default_value = True
            # Input_21
            group_010.inputs[14].default_value = False
            # Input_22
            group_010.inputs[15].default_value = False
            # Input_23
            group_010.inputs[16].default_value = False
            # Input_24
            group_010.inputs[17].default_value = True
            # Input_25
            group_010.inputs[18].default_value = False
            # Input_26
            group_010.inputs[19].default_value = False

            # node Group Output
            group_output_20 = _mn_animate_wiggle_mask_res.nodes.new("NodeGroupOutput")
            group_output_20.name = "Group Output"
            group_output_20.is_active_output = True

            # node Group.014
            group_014_1 = _mn_animate_wiggle_mask_res.nodes.new("GeometryNodeGroup")
            group_014_1.name = "Group.014"
            group_014_1.node_tree = _mn_select_res_name_peptide
            # Input_7
            group_014_1.inputs[0].default_value = True
            # Input_8
            group_014_1.inputs[1].default_value = True
            # Input_9
            group_014_1.inputs[2].default_value = True
            # Input_10
            group_014_1.inputs[3].default_value = True
            # Input_11
            group_014_1.inputs[4].default_value = True
            # Input_12
            group_014_1.inputs[5].default_value = True
            # Input_13
            group_014_1.inputs[6].default_value = True
            # Input_14
            group_014_1.inputs[7].default_value = False
            # Input_15
            group_014_1.inputs[8].default_value = True
            # Input_16
            group_014_1.inputs[9].default_value = True
            # Input_17
            group_014_1.inputs[10].default_value = True
            # Input_18
            group_014_1.inputs[11].default_value = True
            # Input_19
            group_014_1.inputs[12].default_value = True
            # Input_20
            group_014_1.inputs[13].default_value = True
            # Input_21
            group_014_1.inputs[14].default_value = False
            # Input_22
            group_014_1.inputs[15].default_value = True
            # Input_23
            group_014_1.inputs[16].default_value = True
            # Input_24
            group_014_1.inputs[17].default_value = True
            # Input_25
            group_014_1.inputs[18].default_value = True
            # Input_26
            group_014_1.inputs[19].default_value = True

            # node Index Switch
            index_switch_2 = _mn_animate_wiggle_mask_res.nodes.new(
                "GeometryNodeIndexSwitch"
            )
            index_switch_2.name = "Index Switch"
            index_switch_2.data_type = "BOOLEAN"
            index_switch_2.index_switch_items.clear()
            index_switch_2.index_switch_items.new()
            index_switch_2.index_switch_items.new()
            index_switch_2.index_switch_items.new()
            index_switch_2.index_switch_items.new()
            index_switch_2.index_switch_items.new()

            # Set locations
            group_input_20.location = (-100.0, 240.0)
            group_013.location = (-680.0, 120.0)
            group_011.location = (-200.0, 20.0)
            group_012.location = (40.0, -20.0)
            group_010.location = (-440.0, 80.0)
            group_output_20.location = (280.0, 220.0)
            group_014_1.location = (-900.0, 180.0)
            index_switch_2.location = (100.0, 220.0)

            # initialize _mn_animate_wiggle_mask_res links
            # group_input_20.A -> index_switch_2.Index
            _mn_animate_wiggle_mask_res.links.new(
                group_input_20.outputs[0], index_switch_2.inputs[0]
            )
            # group_014_1.Selection -> index_switch_2.0
            _mn_animate_wiggle_mask_res.links.new(
                group_014_1.outputs[0], index_switch_2.inputs[1]
            )
            # group_013.Selection -> index_switch_2.1
            _mn_animate_wiggle_mask_res.links.new(
                group_013.outputs[0], index_switch_2.inputs[2]
            )
            # group_010.Selection -> index_switch_2.2
            _mn_animate_wiggle_mask_res.links.new(
                group_010.outputs[0], index_switch_2.inputs[3]
            )
            # group_011.Selection -> index_switch_2.3
            _mn_animate_wiggle_mask_res.links.new(
                group_011.outputs[0], index_switch_2.inputs[4]
            )
            # group_012.Selection -> index_switch_2.4
            _mn_animate_wiggle_mask_res.links.new(
                group_012.outputs[0], index_switch_2.inputs[5]
            )
            # index_switch_2.Output -> group_output_20.Result
            _mn_animate_wiggle_mask_res.links.new(
                index_switch_2.outputs[0], group_output_20.inputs[0]
            )
            return _mn_animate_wiggle_mask_res

        _mn_animate_wiggle_mask_res = _mn_animate_wiggle_mask_res_node_group()

        # initialize animate_wiggle node group
        def animate_wiggle_node_group():
            animate_wiggle = bpy.data.node_groups.new(
                type="GeometryNodeTree", name="Animate Wiggle"
            )

            animate_wiggle.color_tag = "GEOMETRY"
            animate_wiggle.description = ""

            animate_wiggle.is_modifier = True

            # animate_wiggle interface
            # Socket Atoms
            atoms_socket_9 = animate_wiggle.interface.new_socket(
                name="Atoms", in_out="OUTPUT", socket_type="NodeSocketGeometry"
            )
            atoms_socket_9.attribute_domain = "POINT"
            atoms_socket_9.description = "The animated atomic geometry"

            # Socket Atoms
            atoms_socket_10 = animate_wiggle.interface.new_socket(
                name="Atoms", in_out="INPUT", socket_type="NodeSocketGeometry"
            )
            atoms_socket_10.attribute_domain = "POINT"
            atoms_socket_10.description = (
                "Atomic geometry that contains vertices and edges"
            )

            # Socket Selection
            selection_socket_12 = animate_wiggle.interface.new_socket(
                name="Selection", in_out="INPUT", socket_type="NodeSocketBool"
            )
            selection_socket_12.attribute_domain = "POINT"
            selection_socket_12.hide_value = True
            selection_socket_12.description = "Selection of atoms to apply this node to"

            # Socket b_factor
            b_factor_socket_1 = animate_wiggle.interface.new_socket(
                name="b_factor", in_out="INPUT", socket_type="NodeSocketFloat"
            )
            b_factor_socket_1.subtype = "FACTOR"
            b_factor_socket_1.default_value = 1.0
            b_factor_socket_1.min_value = 0.0
            b_factor_socket_1.max_value = 1.0
            b_factor_socket_1.attribute_domain = "POINT"
            b_factor_socket_1.description = (
                "Amount that `b_factor` changeds the amplitude of wiggling"
            )

            # Socket Amplitude
            amplitude_socket_2 = animate_wiggle.interface.new_socket(
                name="Amplitude", in_out="INPUT", socket_type="NodeSocketFloat"
            )
            amplitude_socket_2.subtype = "NONE"
            amplitude_socket_2.default_value = 1.0
            amplitude_socket_2.min_value = 0.0
            amplitude_socket_2.max_value = 10.0
            amplitude_socket_2.attribute_domain = "POINT"
            amplitude_socket_2.description = "Overall amplitude of the wiggling"

            # Socket Amp. Axis
            amp__axis_socket_1 = animate_wiggle.interface.new_socket(
                name="Amp. Axis", in_out="INPUT", socket_type="NodeSocketFloat"
            )
            amp__axis_socket_1.subtype = "NONE"
            amp__axis_socket_1.default_value = 1.0
            amp__axis_socket_1.min_value = -10000.0
            amp__axis_socket_1.max_value = 10000.0
            amp__axis_socket_1.attribute_domain = "POINT"
            amp__axis_socket_1.description = (
                "Aplitude for the rotation around the bond axes"
            )

            # Socket Amp. Euler
            amp__euler_socket_1 = animate_wiggle.interface.new_socket(
                name="Amp. Euler", in_out="INPUT", socket_type="NodeSocketFloat"
            )
            amp__euler_socket_1.subtype = "NONE"
            amp__euler_socket_1.default_value = 0.4000000059604645
            amp__euler_socket_1.min_value = -10000.0
            amp__euler_socket_1.max_value = 10000.0
            amp__euler_socket_1.attribute_domain = "POINT"
            amp__euler_socket_1.description = (
                "Amplitude for applying euler rotations separate to the axis"
            )

            # Socket Speed
            speed_socket_2 = animate_wiggle.interface.new_socket(
                name="Speed", in_out="INPUT", socket_type="NodeSocketFloat"
            )
            speed_socket_2.subtype = "NONE"
            speed_socket_2.default_value = 3.0
            speed_socket_2.min_value = -10000.0
            speed_socket_2.max_value = 10000.0
            speed_socket_2.attribute_domain = "POINT"
            speed_socket_2.description = (
                "Speed at which the wiggle is applied, 3 will repeat 3 times"
            )

            # Socket Animate
            animate_socket = animate_wiggle.interface.new_socket(
                name="Animate", in_out="INPUT", socket_type="NodeSocketFloat"
            )
            animate_socket.subtype = "NONE"
            animate_socket.default_value = 0.0
            animate_socket.min_value = -10000.0
            animate_socket.max_value = 10000.0
            animate_socket.attribute_domain = "POINT"
            animate_socket.description = (
                "Controls the animation of the wiggle, repeating every `1.00`"
            )

            # initialize animate_wiggle nodes
            # node Group Input
            group_input_21 = animate_wiggle.nodes.new("NodeGroupInput")
            group_input_21.name = "Group Input"

            # node Math
            math_7 = animate_wiggle.nodes.new("ShaderNodeMath")
            math_7.label = "x + 1"
            math_7.name = "Math"
            math_7.hide = True
            math_7.operation = "ADD"
            math_7.use_clamp = False
            # Value_001
            math_7.inputs[1].default_value = 1.0

            # node Boolean Math.005
            boolean_math_005 = animate_wiggle.nodes.new("FunctionNodeBooleanMath")
            boolean_math_005.name = "Boolean Math.005"
            boolean_math_005.operation = "AND"

            # node Reroute.001
            reroute_001_3 = animate_wiggle.nodes.new("NodeReroute")
            reroute_001_3.name = "Reroute.001"
            # node Set Position.005
            set_position_005 = animate_wiggle.nodes.new("GeometryNodeSetPosition")
            set_position_005.name = "Set Position.005"
            # Offset
            set_position_005.inputs[3].default_value = (0.0, 0.0, 0.0)

            # node Repeat Output
            repeat_output = animate_wiggle.nodes.new("GeometryNodeRepeatOutput")
            repeat_output.name = "Repeat Output"
            repeat_output.active_index = 0
            repeat_output.inspection_index = 0
            repeat_output.repeat_items.clear()
            # Create item "Geometry"
            repeat_output.repeat_items.new("GEOMETRY", "Geometry")
            # Create item "Integer"
            repeat_output.repeat_items.new("INT", "Integer")

            # node Repeat Input
            repeat_input = animate_wiggle.nodes.new("GeometryNodeRepeatInput")
            repeat_input.name = "Repeat Input"
            # node Reroute
            reroute_5 = animate_wiggle.nodes.new("NodeReroute")
            reroute_5.name = "Reroute"
            # node Group Output
            group_output_21 = animate_wiggle.nodes.new("NodeGroupOutput")
            group_output_21.name = "Group Output"
            group_output_21.is_active_output = True

            # node Math.001
            math_001_5 = animate_wiggle.nodes.new("ShaderNodeMath")
            math_001_5.label = "x - 1"
            math_001_5.name = "Math.001"
            math_001_5.hide = True
            math_001_5.operation = "SUBTRACT"
            math_001_5.use_clamp = False
            # Value_001
            math_001_5.inputs[1].default_value = 1.0

            # node Group.017
            group_017 = animate_wiggle.nodes.new("GeometryNodeGroup")
            group_017.name = "Group.017"
            group_017.node_tree = _mn_animate_wiggle_mask_length

            # node Group.010
            group_010_1 = animate_wiggle.nodes.new("GeometryNodeGroup")
            group_010_1.name = "Group.010"
            group_010_1.node_tree = _mn_utils_rotate_res

            # node Group.016
            group_016 = animate_wiggle.nodes.new("GeometryNodeGroup")
            group_016.name = "Group.016"
            group_016.node_tree = _mn_animate_wiggle_mask_length

            # node Group.015
            group_015 = animate_wiggle.nodes.new("GeometryNodeGroup")
            group_015.name = "Group.015"
            group_015.node_tree = _mn_animate_wiggle_mask_res

            # Process zone input Repeat Input
            repeat_input.pair_with_output(repeat_output)
            # Iterations
            repeat_input.inputs[0].default_value = 5
            # Item_1
            repeat_input.inputs[2].default_value = 0

            # Set locations
            group_input_21.location = (-2044.6171875, 63.613792419433594)
            math_7.location = (-1080.0, 520.0)
            boolean_math_005.location = (-1180.0, 420.0)
            reroute_001_3.location = (-1200.0, 120.0)
            set_position_005.location = (-620.0, 600.0)
            repeat_output.location = (-420.0, 600.0)
            repeat_input.location = (-1840.0, 600.0)
            reroute_5.location = (-1560.0, 260.0)
            group_output_21.location = (-180.0, 600.0)
            math_001_5.location = (-1600.0, 200.0)
            group_017.location = (-1439.4599609375, 220.0)
            group_010_1.location = (-980.0, 280.0)
            group_016.location = (-1442.23583984375, 340.0)
            group_015.location = (-1460.0, 460.0)

            # initialize animate_wiggle links
            # set_position_005.Geometry -> repeat_output.Geometry
            animate_wiggle.links.new(
                set_position_005.outputs[0], repeat_output.inputs[0]
            )
            # group_input_21.Atoms -> repeat_input.Geometry
            animate_wiggle.links.new(group_input_21.outputs[0], repeat_input.inputs[1])
            # repeat_input.Integer -> math_7.Value
            animate_wiggle.links.new(repeat_input.outputs[1], math_7.inputs[0])
            # math_7.Value -> repeat_output.Integer
            animate_wiggle.links.new(math_7.outputs[0], repeat_output.inputs[1])
            # repeat_input.Geometry -> set_position_005.Geometry
            animate_wiggle.links.new(
                repeat_input.outputs[0], set_position_005.inputs[0]
            )
            # boolean_math_005.Boolean -> group_010_1.Selection
            animate_wiggle.links.new(boolean_math_005.outputs[0], group_010_1.inputs[0])
            # group_input_21.Animate -> group_010_1.Animate 0..1
            animate_wiggle.links.new(group_input_21.outputs[7], group_010_1.inputs[8])
            # group_input_21.Speed -> group_010_1.Speed
            animate_wiggle.links.new(group_input_21.outputs[6], group_010_1.inputs[7])
            # group_input_21.Amplitude -> group_010_1.Amplitude
            animate_wiggle.links.new(group_input_21.outputs[3], group_010_1.inputs[4])
            # group_input_21.b_factor -> group_010_1.Scale b_factor
            animate_wiggle.links.new(group_input_21.outputs[2], group_010_1.inputs[3])
            # group_input_21.Amp. Axis -> group_010_1.Amp. Axis
            animate_wiggle.links.new(group_input_21.outputs[4], group_010_1.inputs[5])
            # group_input_21.Amp. Euler -> group_010_1.Amp. Euler
            animate_wiggle.links.new(group_input_21.outputs[5], group_010_1.inputs[6])
            # group_015.Result -> boolean_math_005.Boolean
            animate_wiggle.links.new(group_015.outputs[0], boolean_math_005.inputs[0])
            # reroute_001_3.Output -> boolean_math_005.Boolean
            animate_wiggle.links.new(
                reroute_001_3.outputs[0], boolean_math_005.inputs[1]
            )
            # group_010_1.Selection -> set_position_005.Selection
            animate_wiggle.links.new(group_010_1.outputs[0], set_position_005.inputs[1])
            # group_010_1.Position -> set_position_005.Position
            animate_wiggle.links.new(group_010_1.outputs[1], set_position_005.inputs[2])
            # group_016.Result -> group_010_1.atom_name rotation
            animate_wiggle.links.new(group_016.outputs[0], group_010_1.inputs[1])
            # math_001_5.Value -> group_017.A
            animate_wiggle.links.new(math_001_5.outputs[0], group_017.inputs[0])
            # reroute_5.Output -> group_016.A
            animate_wiggle.links.new(reroute_5.outputs[0], group_016.inputs[0])
            # reroute_5.Output -> group_015.A
            animate_wiggle.links.new(reroute_5.outputs[0], group_015.inputs[0])
            # repeat_output.Geometry -> group_output_21.Atoms
            animate_wiggle.links.new(
                repeat_output.outputs[0], group_output_21.inputs[0]
            )
            # group_017.Result -> group_010_1.atom_name axis
            animate_wiggle.links.new(group_017.outputs[0], group_010_1.inputs[2])
            # repeat_input.Integer -> reroute_5.Input
            animate_wiggle.links.new(repeat_input.outputs[1], reroute_5.inputs[0])
            # reroute_5.Output -> math_001_5.Value
            animate_wiggle.links.new(reroute_5.outputs[0], math_001_5.inputs[0])
            # group_input_21.Selection -> reroute_001_3.Input
            animate_wiggle.links.new(group_input_21.outputs[1], reroute_001_3.inputs[0])
            return animate_wiggle

        animate_wiggle = animate_wiggle_node_group()

        # initialize nodegroup_003 node group
        def nodegroup_003_node_group():
            nodegroup_003 = bpy.data.node_groups.new(
                type="GeometryNodeTree", name="WiggleProt"
            )

            nodegroup_003.color_tag = "NONE"
            nodegroup_003.description = "Custom node for Creating Wiggling protein"

            # nodegroup_003 interface
            # Socket Atoms
            atoms_socket_11 = nodegroup_003.interface.new_socket(
                name="Atoms", in_out="OUTPUT", socket_type="NodeSocketGeometry"
            )
            atoms_socket_11.attribute_domain = "POINT"

            # Socket Atoms
            atoms_socket_12 = nodegroup_003.interface.new_socket(
                name="Atoms", in_out="INPUT", socket_type="NodeSocketGeometry"
            )
            atoms_socket_12.attribute_domain = "POINT"

            # initialize nodegroup_003 nodes
            # node Group Output
            group_output_22 = nodegroup_003.nodes.new("NodeGroupOutput")
            group_output_22.name = "Group Output"
            group_output_22.is_active_output = True

            # node Group Input
            group_input_22 = nodegroup_003.nodes.new("NodeGroupInput")
            group_input_22.name = "Group Input"

            # node Set Color.001
            set_color_001 = nodegroup_003.nodes.new("GeometryNodeGroup")
            set_color_001.name = "Set Color.001"
            set_color_001.node_tree = set_color
            # Input_15
            set_color_001.inputs[1].default_value = True
            # Input_16
            set_color_001.inputs[2].default_value = (
                0.16151699423789978,
                0.6239609718322754,
                0.19560199975967407,
                1.0,
            )

            # node Style Ball and Stick
            style_ball_and_stick_1 = nodegroup_003.nodes.new("GeometryNodeGroup")
            style_ball_and_stick_1.label = "Style Ball and Stick"
            style_ball_and_stick_1.name = "Style Ball and Stick"
            style_ball_and_stick_1.node_tree = style_ball_and_stick
            # Socket_5
            style_ball_and_stick_1.inputs[1].default_value = 2
            # Input_1
            style_ball_and_stick_1.inputs[2].default_value = True
            # Input_2
            style_ball_and_stick_1.inputs[3].default_value = True
            # Input_3
            style_ball_and_stick_1.inputs[4].default_value = 0.30000001192092896
            # Socket_3
            style_ball_and_stick_1.inputs[5].default_value = False
            # Input_7
            style_ball_and_stick_1.inputs[6].default_value = 0.30000001192092896
            # Socket_6
            style_ball_and_stick_1.inputs[7].default_value = False
            # Input_4
            style_ball_and_stick_1.inputs[8].default_value = True
            if "MN Default" in bpy.data.materials:
                style_ball_and_stick_1.inputs[9].default_value = bpy.data.materials[
                    "MN Default"
                ]

            # node Animate Value
            animate_value_1 = nodegroup_003.nodes.new("GeometryNodeGroup")
            animate_value_1.label = "Animate Value"
            animate_value_1.name = "Animate Value"
            animate_value_1.node_tree = animate_value
            # Input_3
            animate_value_1.inputs[0].default_value = False
            # Input_6
            animate_value_1.inputs[1].default_value = False
            # Input_0
            animate_value_1.inputs[2].default_value = 1
            # Input_1
            animate_value_1.inputs[3].default_value = 250
            # Input_4
            animate_value_1.inputs[4].default_value = 0.0
            # Input_5
            animate_value_1.inputs[5].default_value = 1.0

            # node Animate Wiggle
            animate_wiggle_1 = nodegroup_003.nodes.new("GeometryNodeGroup")
            animate_wiggle_1.label = "Animate Wiggle"
            animate_wiggle_1.name = "Animate Wiggle"
            animate_wiggle_1.node_tree = animate_wiggle
            # Input_2
            animate_wiggle_1.inputs[1].default_value = True
            # Input_7
            animate_wiggle_1.inputs[2].default_value = 1.0
            # Input_4
            animate_wiggle_1.inputs[3].default_value = 1.0
            # Input_8
            animate_wiggle_1.inputs[4].default_value = 1.0
            # Input_9
            animate_wiggle_1.inputs[5].default_value = 0.4000000059604645
            # Input_6
            animate_wiggle_1.inputs[6].default_value = 3.0

            # node Set Color
            set_color_1 = nodegroup_003.nodes.new("GeometryNodeGroup")
            set_color_1.name = "Set Color"
            set_color_1.node_tree = set_color
            # Input_15
            set_color_1.inputs[1].default_value = True
            # Input_16
            set_color_1.inputs[2].default_value = (
                0.16151699423789978,
                0.6239609718322754,
                0.19560199975967407,
                1.0,
            )

            # Set locations
            group_output_22.location = (450.0, 0.0)
            group_input_22.location = (-420.0, 0.0)
            set_color_001.location = (-220.0, 60.0)
            style_ball_and_stick_1.location = (0.0, 80.0)
            animate_value_1.location = (160.0, -180.0)
            animate_wiggle_1.location = (220.0, 180.0)
            set_color_1.location = (-220.0, 60.0)

            # initialize nodegroup_003 links
            # animate_value_1.Value -> animate_wiggle_1.Animate
            nodegroup_003.links.new(
                animate_value_1.outputs[0], animate_wiggle_1.inputs[7]
            )
            # style_ball_and_stick_1.Geometry -> animate_wiggle_1.Atoms
            nodegroup_003.links.new(
                style_ball_and_stick_1.outputs[0], animate_wiggle_1.inputs[0]
            )
            # set_color_001.Atoms -> style_ball_and_stick_1.Atoms
            nodegroup_003.links.new(
                set_color_001.outputs[0], style_ball_and_stick_1.inputs[0]
            )
            # group_input_22.Atoms -> set_color_001.Atoms
            nodegroup_003.links.new(group_input_22.outputs[0], set_color_001.inputs[0])
            # group_input_22.Atoms -> set_color_1.Atoms
            nodegroup_003.links.new(group_input_22.outputs[0], set_color_1.inputs[0])
            # animate_wiggle_1.Atoms -> group_output_22.Atoms
            nodegroup_003.links.new(
                animate_wiggle_1.outputs[0], group_output_22.inputs[0]
            )
            return nodegroup_003

        nodegroup_003 = nodegroup_003_node_group()

        name = bpy.context.object.name
        obj = bpy.data.objects[name]
        mod = obj.modifiers.new(name="UserNode", type="NODES")
        mod.node_group = nodegroup_003
        return {"FINISHED"}


def menu_func(self, context):
    self.layout.operator(wiggle.bl_idname)


def register():
    bpy.utils.register_class(wiggle)
    bpy.types.NODE_MT_add.append(menu_func)


def unregister():
    bpy.utils.unregister_class(wiggle)
    bpy.types.NODE_MT_add.remove(menu_func)


if __name__ == "__main__":
    register()
