bl_info = {
	"name" : "_curve_ends_adjust_position",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _curve_ends_adjust_position(bpy.types.Operator):
	bl_idname = "node._curve_ends_adjust_position"
	bl_label = "_curve_ends_adjust_position"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
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
			offset_socket = _field_offset_vec.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
			offset_socket.subtype = 'NONE'
			offset_socket.default_value = 0
			offset_socket.min_value = -2147483648
			offset_socket.max_value = 2147483647
			offset_socket.attribute_domain = 'POINT'
			
			
			#initialize _field_offset_vec nodes
			#node Group Input
			group_input = _field_offset_vec.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Evaluate at Index
			evaluate_at_index = _field_offset_vec.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index.name = "Evaluate at Index"
			evaluate_at_index.data_type = 'FLOAT_VECTOR'
			evaluate_at_index.domain = 'POINT'
			
			#node Group Output
			group_output = _field_offset_vec.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Math.001
			math_001 = _field_offset_vec.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.operation = 'ADD'
			math_001.use_clamp = False
			
			#node Index
			index = _field_offset_vec.nodes.new("GeometryNodeInputIndex")
			index.name = "Index"
			
			
			
			
			#Set locations
			group_input.location = (-417.64404296875, 0.0)
			evaluate_at_index.location = (-220.0, 100.0)
			group_output.location = (20.0, 20.0)
			math_001.location = (-220.0, -80.0)
			index.location = (-400.0, -180.0)
			
			#Set dimensions
			group_input.width, group_input.height = 140.0, 100.0
			evaluate_at_index.width, evaluate_at_index.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			index.width, index.height = 140.0, 100.0
			
			#initialize _field_offset_vec links
			#math_001.Value -> evaluate_at_index.Index
			_field_offset_vec.links.new(math_001.outputs[0], evaluate_at_index.inputs[0])
			#group_input.Field -> evaluate_at_index.Value
			_field_offset_vec.links.new(group_input.outputs[0], evaluate_at_index.inputs[1])
			#group_input.Offset -> math_001.Value
			_field_offset_vec.links.new(group_input.outputs[1], math_001.inputs[0])
			#evaluate_at_index.Value -> group_output.Field
			_field_offset_vec.links.new(evaluate_at_index.outputs[0], group_output.inputs[0])
			#index.Index -> math_001.Value
			_field_offset_vec.links.new(index.outputs[0], math_001.inputs[1])
			return _field_offset_vec

		_field_offset_vec = _field_offset_vec_node_group()

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
			value_socket = mn_units.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket.subtype = 'NONE'
			value_socket.default_value = 3.0
			value_socket.min_value = -10000.0
			value_socket.max_value = 10000.0
			value_socket.attribute_domain = 'POINT'
			value_socket.description = "A value which will be scaled appropriately for the world"
			
			
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

		#initialize _curve_ends_adjust_position node group
		def _curve_ends_adjust_position_node_group():
			_curve_ends_adjust_position = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "_curve_ends_adjust_position")

			_curve_ends_adjust_position.color_tag = 'NONE'
			_curve_ends_adjust_position.description = ""

			_curve_ends_adjust_position.is_modifier = True
			
			#_curve_ends_adjust_position interface
			#Socket Geometry
			geometry_socket = _curve_ends_adjust_position.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_1 = _curve_ends_adjust_position.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_1.attribute_domain = 'POINT'
			
			#Socket Distance
			distance_socket = _curve_ends_adjust_position.interface.new_socket(name = "Distance", in_out='INPUT', socket_type = 'NodeSocketFloat')
			distance_socket.subtype = 'NONE'
			distance_socket.default_value = 0.30000001192092896
			distance_socket.min_value = -10000.0
			distance_socket.max_value = 10000.0
			distance_socket.attribute_domain = 'POINT'
			
			
			#initialize _curve_ends_adjust_position nodes
			#node Position
			position = _curve_ends_adjust_position.nodes.new("GeometryNodeInputPosition")
			position.name = "Position"
			
			#node Group.026
			group_026 = _curve_ends_adjust_position.nodes.new("GeometryNodeGroup")
			group_026.name = "Group.026"
			group_026.node_tree = _field_offset_vec
			#Input_1
			group_026.inputs[1].default_value = -1
			
			#node Group.027
			group_027 = _curve_ends_adjust_position.nodes.new("GeometryNodeGroup")
			group_027.name = "Group.027"
			group_027.node_tree = _field_offset_vec
			#Input_1
			group_027.inputs[1].default_value = 1
			
			#node Vector Math.008
			vector_math_008 = _curve_ends_adjust_position.nodes.new("ShaderNodeVectorMath")
			vector_math_008.name = "Vector Math.008"
			vector_math_008.operation = 'SUBTRACT'
			
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
			vector_math_009 = _curve_ends_adjust_position.nodes.new("ShaderNodeVectorMath")
			vector_math_009.name = "Vector Math.009"
			vector_math_009.operation = 'SUBTRACT'
			
			#node Endpoint Selection.001
			endpoint_selection_001 = _curve_ends_adjust_position.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_001.name = "Endpoint Selection.001"
			#Start Size
			endpoint_selection_001.inputs[0].default_value = 1
			#End Size
			endpoint_selection_001.inputs[1].default_value = 0
			
			#node Group Output
			group_output_3 = _curve_ends_adjust_position.nodes.new("NodeGroupOutput")
			group_output_3.name = "Group Output"
			group_output_3.is_active_output = True
			
			#node Group Input
			group_input_3 = _curve_ends_adjust_position.nodes.new("NodeGroupInput")
			group_input_3.name = "Group Input"
			
			#node Switch.010
			switch_010 = _curve_ends_adjust_position.nodes.new("GeometryNodeSwitch")
			switch_010.name = "Switch.010"
			switch_010.input_type = 'VECTOR'
			
			#node Vector Math
			vector_math = _curve_ends_adjust_position.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.operation = 'NORMALIZE'
			
			#node Vector Math.003
			vector_math_003 = _curve_ends_adjust_position.nodes.new("ShaderNodeVectorMath")
			vector_math_003.name = "Vector Math.003"
			vector_math_003.operation = 'SCALE'
			
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
			position.location = (-345.67303466796875, 21.96319580078125)
			group_026.location = (-165.67303466796875, -38.03680419921875)
			group_027.location = (-165.67303466796875, -318.03680419921875)
			vector_math_008.location = (-165.67303466796875, 101.96319580078125)
			endpoint_selection_002.location = (-365.67303466796875, -178.03680419921875)
			switch_007.location = (-5.67303466796875, 101.96319580078125)
			vector_math_009.location = (-165.67303466796875, -178.03680419921875)
			endpoint_selection_001.location = (-345.67303466796875, 141.96319580078125)
			group_output_3.location = (867.47216796875, 3.8314287662506104)
			group_input_3.location = (-500.0, 280.0)
			switch_010.location = (154.32696533203125, 101.96319580078125)
			vector_math.location = (300.0, 100.0)
			vector_math_003.location = (626.1260986328125, 105.79462432861328)
			set_position_001.location = (677.47216796875, 321.86822509765625)
			group_023.location = (154.32696533203125, -58.03680419921875)
			
			#Set dimensions
			position.width, position.height = 140.0, 100.0
			group_026.width, group_026.height = 140.0, 100.0
			group_027.width, group_027.height = 140.0, 100.0
			vector_math_008.width, vector_math_008.height = 140.0, 100.0
			endpoint_selection_002.width, endpoint_selection_002.height = 140.0, 100.0
			switch_007.width, switch_007.height = 140.0, 100.0
			vector_math_009.width, vector_math_009.height = 140.0, 100.0
			endpoint_selection_001.width, endpoint_selection_001.height = 140.0, 100.0
			group_output_3.width, group_output_3.height = 140.0, 100.0
			group_input_3.width, group_input_3.height = 140.0, 100.0
			switch_010.width, switch_010.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			vector_math_003.width, vector_math_003.height = 140.0, 100.0
			set_position_001.width, set_position_001.height = 140.0, 100.0
			group_023.width, group_023.height = 140.0, 100.0
			
			#initialize _curve_ends_adjust_position links
			#group_023.Angstrom -> vector_math_003.Scale
			_curve_ends_adjust_position.links.new(group_023.outputs[0], vector_math_003.inputs[3])
			#endpoint_selection_001.Selection -> switch_007.Switch
			_curve_ends_adjust_position.links.new(endpoint_selection_001.outputs[0], switch_007.inputs[0])
			#position.Position -> group_027.Field
			_curve_ends_adjust_position.links.new(position.outputs[0], group_027.inputs[0])
			#vector_math_008.Vector -> switch_007.True
			_curve_ends_adjust_position.links.new(vector_math_008.outputs[0], switch_007.inputs[2])
			#position.Position -> vector_math_009.Vector
			_curve_ends_adjust_position.links.new(position.outputs[0], vector_math_009.inputs[1])
			#position.Position -> vector_math_008.Vector
			_curve_ends_adjust_position.links.new(position.outputs[0], vector_math_008.inputs[1])
			#vector_math_009.Vector -> switch_010.True
			_curve_ends_adjust_position.links.new(vector_math_009.outputs[0], switch_010.inputs[2])
			#position.Position -> group_026.Field
			_curve_ends_adjust_position.links.new(position.outputs[0], group_026.inputs[0])
			#vector_math_003.Vector -> set_position_001.Offset
			_curve_ends_adjust_position.links.new(vector_math_003.outputs[0], set_position_001.inputs[3])
			#group_027.Field -> vector_math_009.Vector
			_curve_ends_adjust_position.links.new(group_027.outputs[0], vector_math_009.inputs[0])
			#switch_007.Output -> switch_010.False
			_curve_ends_adjust_position.links.new(switch_007.outputs[0], switch_010.inputs[1])
			#endpoint_selection_002.Selection -> switch_010.Switch
			_curve_ends_adjust_position.links.new(endpoint_selection_002.outputs[0], switch_010.inputs[0])
			#group_026.Field -> vector_math_008.Vector
			_curve_ends_adjust_position.links.new(group_026.outputs[0], vector_math_008.inputs[0])
			#group_input_3.Geometry -> set_position_001.Geometry
			_curve_ends_adjust_position.links.new(group_input_3.outputs[0], set_position_001.inputs[0])
			#set_position_001.Geometry -> group_output_3.Geometry
			_curve_ends_adjust_position.links.new(set_position_001.outputs[0], group_output_3.inputs[0])
			#switch_010.Output -> vector_math.Vector
			_curve_ends_adjust_position.links.new(switch_010.outputs[0], vector_math.inputs[0])
			#vector_math.Vector -> vector_math_003.Vector
			_curve_ends_adjust_position.links.new(vector_math.outputs[0], vector_math_003.inputs[0])
			#group_input_3.Distance -> group_023.Value
			_curve_ends_adjust_position.links.new(group_input_3.outputs[1], group_023.inputs[0])
			return _curve_ends_adjust_position

		_curve_ends_adjust_position = _curve_ends_adjust_position_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "_curve_ends_adjust_position", type = 'NODES')
		mod.node_group = _curve_ends_adjust_position
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_curve_ends_adjust_position.bl_idname)
			
def register():
	bpy.utils.register_class(_curve_ends_adjust_position)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_curve_ends_adjust_position)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
