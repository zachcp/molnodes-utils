bl_info = {
	"name" : "Select Proximity",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Select_Proximity(bpy.types.Operator):
	bl_idname = "node.select_proximity"
	bl_label = "Select Proximity"
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

		#initialize select_res_whole node group
		def select_res_whole_node_group():
			select_res_whole = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Select Res Whole")

			select_res_whole.color_tag = 'INPUT'
			select_res_whole.description = ""

			
			#select_res_whole interface
			#Socket Selection
			selection_socket = select_res_whole.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket.attribute_domain = 'POINT'
			selection_socket.description = "The calculated selection"
			
			#Socket Selection
			selection_socket_1 = select_res_whole.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_1.attribute_domain = 'POINT'
			selection_socket_1.hide_value = True
			selection_socket_1.description = "Selection of atoms to apply this node to"
			
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
			compare_001 = select_res_whole.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'INT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'GREATER_THAN'
			#B_INT
			compare_001.inputs[3].default_value = 0
			
			#node Group Output
			group_output_2 = select_res_whole.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Named Attribute.001
			named_attribute_001 = select_res_whole.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.data_type = 'INT'
			#Name
			named_attribute_001.inputs[0].default_value = "res_id"
			
			#node Index
			index = select_res_whole.nodes.new("GeometryNodeInputIndex")
			index.name = "Index"
			
			#node Math
			math_1 = select_res_whole.nodes.new("ShaderNodeMath")
			math_1.label = "x + 1"
			math_1.name = "Math"
			math_1.hide = True
			math_1.operation = 'ADD'
			math_1.use_clamp = False
			#Value_001
			math_1.inputs[1].default_value = 1.0
			
			#node Field at Index
			field_at_index = select_res_whole.nodes.new("GeometryNodeFieldAtIndex")
			field_at_index.name = "Field at Index"
			field_at_index.data_type = 'INT'
			field_at_index.domain = 'POINT'
			
			#node Compare
			compare = select_res_whole.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'NOT_EQUAL'
			
			#node Accumulate Field.001
			accumulate_field_001 = select_res_whole.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_001.name = "Accumulate Field.001"
			accumulate_field_001.data_type = 'INT'
			accumulate_field_001.domain = 'POINT'
			#Group Index
			accumulate_field_001.inputs[1].default_value = 0
			
			#node Group Input
			group_input_2 = select_res_whole.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
			#node Switch
			switch = select_res_whole.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'BOOLEAN'
			
			
			
			
			#Set locations
			accumulate_field.location = (0.0, 80.0)
			compare_001.location = (160.0, 80.0)
			group_output_2.location = (480.0, 180.0)
			named_attribute_001.location = (-520.0, -100.0)
			index.location = (-700.0, -280.0)
			math_1.location = (-700.0, -340.0)
			field_at_index.location = (-520.0, -240.0)
			compare.location = (-360.0, -240.0)
			accumulate_field_001.location = (-200.0, -200.0)
			group_input_2.location = (-280.0, 160.0)
			switch.location = (160.0, 240.0)
			
			#Set dimensions
			accumulate_field.width, accumulate_field.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			group_output_2.width, group_output_2.height = 140.0, 100.0
			named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
			index.width, index.height = 140.0, 100.0
			math_1.width, math_1.height = 140.0, 100.0
			field_at_index.width, field_at_index.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			accumulate_field_001.width, accumulate_field_001.height = 140.0, 100.0
			group_input_2.width, group_input_2.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			
			#initialize select_res_whole links
			#group_input_2.Selection -> accumulate_field.Value
			select_res_whole.links.new(group_input_2.outputs[0], accumulate_field.inputs[0])
			#accumulate_field.Total -> compare_001.A
			select_res_whole.links.new(accumulate_field.outputs[2], compare_001.inputs[2])
			#named_attribute_001.Attribute -> field_at_index.Value
			select_res_whole.links.new(named_attribute_001.outputs[0], field_at_index.inputs[1])
			#index.Index -> math_1.Value
			select_res_whole.links.new(index.outputs[0], math_1.inputs[0])
			#math_1.Value -> field_at_index.Index
			select_res_whole.links.new(math_1.outputs[0], field_at_index.inputs[0])
			#named_attribute_001.Attribute -> compare.A
			select_res_whole.links.new(named_attribute_001.outputs[0], compare.inputs[2])
			#field_at_index.Value -> compare.B
			select_res_whole.links.new(field_at_index.outputs[0], compare.inputs[3])
			#compare.Result -> accumulate_field_001.Value
			select_res_whole.links.new(compare.outputs[0], accumulate_field_001.inputs[0])
			#accumulate_field_001.Trailing -> accumulate_field.Group ID
			select_res_whole.links.new(accumulate_field_001.outputs[1], accumulate_field.inputs[1])
			#group_input_2.Selection -> switch.False
			select_res_whole.links.new(group_input_2.outputs[0], switch.inputs[1])
			#compare_001.Result -> switch.True
			select_res_whole.links.new(compare_001.outputs[0], switch.inputs[2])
			#switch.Output -> group_output_2.Selection
			select_res_whole.links.new(switch.outputs[0], group_output_2.inputs[0])
			#group_input_2.Expand -> switch.Switch
			select_res_whole.links.new(group_input_2.outputs[1], switch.inputs[0])
			return select_res_whole

		select_res_whole = select_res_whole_node_group()

		#initialize select_proximity node group
		def select_proximity_node_group():
			select_proximity = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Select Proximity")

			select_proximity.color_tag = 'INPUT'
			select_proximity.description = ""

			
			#select_proximity interface
			#Socket Selection
			selection_socket_2 = select_proximity.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket_2.attribute_domain = 'POINT'
			selection_socket_2.description = "The calculated selection"
			
			#Socket Inverted
			inverted_socket = select_proximity.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket.attribute_domain = 'POINT'
			inverted_socket.description = "The inverse of the calculated selection"
			
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
			group_output_3 = select_proximity.nodes.new("NodeGroupOutput")
			group_output_3.name = "Group Output"
			group_output_3.is_active_output = True
			
			#node Boolean Math
			boolean_math = select_proximity.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'NOT'
			
			#node Reroute
			reroute = select_proximity.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Compare
			compare_1 = select_proximity.nodes.new("FunctionNodeCompare")
			compare_1.name = "Compare"
			compare_1.data_type = 'FLOAT'
			compare_1.mode = 'ELEMENT'
			compare_1.operation = 'LESS_THAN'
			
			#node Group
			group_1 = select_proximity.nodes.new("GeometryNodeGroup")
			group_1.name = "Group"
			group_1.node_tree = select_res_whole
			
			#node Group Input
			group_input_3 = select_proximity.nodes.new("NodeGroupInput")
			group_input_3.name = "Group Input"
			
			#node Separate Geometry
			separate_geometry = select_proximity.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry.name = "Separate Geometry"
			separate_geometry.domain = 'POINT'
			
			#node Boolean Math.002
			boolean_math_002 = select_proximity.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002.name = "Boolean Math.002"
			boolean_math_002.operation = 'NIMPLY'
			
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
			switch_1 = select_proximity.nodes.new("GeometryNodeSwitch")
			switch_1.name = "Switch"
			switch_1.input_type = 'BOOLEAN'
			#False
			switch_1.inputs[1].default_value = False
			
			
			
			
			#Set locations
			geometry_proximity.location = (-298.0000915527344, 80.0)
			group_068.location = (-300.0, -160.0)
			group_output_3.location = (840.0, 160.0)
			boolean_math.location = (600.0, 100.0)
			reroute.location = (560.0, 120.0)
			compare_1.location = (-140.0, 80.0)
			group_1.location = (200.0, 80.0)
			group_input_3.location = (-738.4535522460938, -21.88127326965332)
			separate_geometry.location = (-506.0091857910156, 87.78723907470703)
			boolean_math_002.location = (20.0, 80.0)
			accumulate_field_1.location = (-340.0, 320.0)
			boolean_math_004.location = (-500.0, 320.0)
			switch_1.location = (-140.0, 260.0)
			
			#Set dimensions
			geometry_proximity.width, geometry_proximity.height = 140.0, 100.0
			group_068.width, group_068.height = 140.0, 100.0
			group_output_3.width, group_output_3.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			compare_1.width, compare_1.height = 140.0, 100.0
			group_1.width, group_1.height = 140.0, 100.0
			group_input_3.width, group_input_3.height = 140.0, 100.0
			separate_geometry.width, separate_geometry.height = 140.0, 100.0
			boolean_math_002.width, boolean_math_002.height = 140.0, 100.0
			accumulate_field_1.width, accumulate_field_1.height = 140.0, 100.0
			boolean_math_004.width, boolean_math_004.height = 140.0, 100.0
			switch_1.width, switch_1.height = 140.0, 100.0
			
			#initialize select_proximity links
			#geometry_proximity.Distance -> compare_1.A
			select_proximity.links.new(geometry_proximity.outputs[1], compare_1.inputs[0])
			#group_068.Angstrom -> compare_1.B
			select_proximity.links.new(group_068.outputs[0], compare_1.inputs[1])
			#separate_geometry.Selection -> geometry_proximity.Geometry
			select_proximity.links.new(separate_geometry.outputs[0], geometry_proximity.inputs[0])
			#group_input_3.Distance (A) -> group_068.Value
			select_proximity.links.new(group_input_3.outputs[3], group_068.inputs[0])
			#reroute.Output -> group_output_3.Selection
			select_proximity.links.new(reroute.outputs[0], group_output_3.inputs[0])
			#reroute.Output -> boolean_math.Boolean
			select_proximity.links.new(reroute.outputs[0], boolean_math.inputs[0])
			#boolean_math.Boolean -> group_output_3.Inverted
			select_proximity.links.new(boolean_math.outputs[0], group_output_3.inputs[1])
			#group_1.Selection -> reroute.Input
			select_proximity.links.new(group_1.outputs[0], reroute.inputs[0])
			#group_input_3.Target Atoms -> separate_geometry.Geometry
			select_proximity.links.new(group_input_3.outputs[0], separate_geometry.inputs[0])
			#group_input_3.Subset -> separate_geometry.Selection
			select_proximity.links.new(group_input_3.outputs[1], separate_geometry.inputs[1])
			#compare_1.Result -> boolean_math_002.Boolean
			select_proximity.links.new(compare_1.outputs[0], boolean_math_002.inputs[0])
			#group_input_3.Expand -> group_1.Expand
			select_proximity.links.new(group_input_3.outputs[2], group_1.inputs[1])
			#boolean_math_002.Boolean -> group_1.Selection
			select_proximity.links.new(boolean_math_002.outputs[0], group_1.inputs[0])
			#group_input_3.Subset -> boolean_math_004.Boolean
			select_proximity.links.new(group_input_3.outputs[1], boolean_math_004.inputs[0])
			#boolean_math_004.Boolean -> accumulate_field_1.Value
			select_proximity.links.new(boolean_math_004.outputs[0], accumulate_field_1.inputs[0])
			#accumulate_field_1.Total -> switch_1.Switch
			select_proximity.links.new(accumulate_field_1.outputs[2], switch_1.inputs[0])
			#group_input_3.Subset -> switch_1.True
			select_proximity.links.new(group_input_3.outputs[1], switch_1.inputs[2])
			#switch_1.Output -> boolean_math_002.Boolean
			select_proximity.links.new(switch_1.outputs[0], boolean_math_002.inputs[1])
			return select_proximity

		select_proximity = select_proximity_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Select Proximity", type = 'NODES')
		mod.node_group = select_proximity
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Select_Proximity.bl_idname)
			
def register():
	bpy.utils.register_class(Select_Proximity)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Select_Proximity)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
