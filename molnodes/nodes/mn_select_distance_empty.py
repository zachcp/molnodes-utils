bl_info = {
	"name" : "MN_select_distance_empty",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class MN_select_distance_empty(bpy.types.Operator):
	bl_idname = "node.mn_select_distance_empty"
	bl_label = "MN_select_distance_empty"
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

		#initialize mn_select_distance_empty node group
		def mn_select_distance_empty_node_group():
			mn_select_distance_empty = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "MN_select_distance_empty")

			mn_select_distance_empty.color_tag = 'NONE'
			mn_select_distance_empty.description = ""

			
			#mn_select_distance_empty interface
			#Socket > Cutoff
			__cutoff_socket = mn_select_distance_empty.interface.new_socket(name = "> Cutoff", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			__cutoff_socket.attribute_domain = 'POINT'
			
			#Socket < Cutoff
			__cutoff_socket_1 = mn_select_distance_empty.interface.new_socket(name = "< Cutoff", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			__cutoff_socket_1.attribute_domain = 'POINT'
			
			#Socket Distance
			distance_socket = mn_select_distance_empty.interface.new_socket(name = "Distance", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			distance_socket.subtype = 'NONE'
			distance_socket.default_value = 0.0
			distance_socket.min_value = -3.4028234663852886e+38
			distance_socket.max_value = 3.4028234663852886e+38
			distance_socket.attribute_domain = 'POINT'
			
			#Socket 0..1
			_0__1_socket = mn_select_distance_empty.interface.new_socket(name = "0..1", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			_0__1_socket.subtype = 'NONE'
			_0__1_socket.default_value = 0.0
			_0__1_socket.min_value = -3.4028234663852886e+38
			_0__1_socket.max_value = 3.4028234663852886e+38
			_0__1_socket.attribute_domain = 'POINT'
			
			#Socket Object
			object_socket = mn_select_distance_empty.interface.new_socket(name = "Object", in_out='INPUT', socket_type = 'NodeSocketObject')
			object_socket.attribute_domain = 'POINT'
			
			#Socket From Min
			from_min_socket = mn_select_distance_empty.interface.new_socket(name = "From Min", in_out='INPUT', socket_type = 'NodeSocketFloat')
			from_min_socket.subtype = 'NONE'
			from_min_socket.default_value = 0.0
			from_min_socket.min_value = -10000.0
			from_min_socket.max_value = 10000.0
			from_min_socket.attribute_domain = 'POINT'
			
			#Socket From Max
			from_max_socket = mn_select_distance_empty.interface.new_socket(name = "From Max", in_out='INPUT', socket_type = 'NodeSocketFloat')
			from_max_socket.subtype = 'NONE'
			from_max_socket.default_value = 1.0
			from_max_socket.min_value = -10000.0
			from_max_socket.max_value = 10000.0
			from_max_socket.attribute_domain = 'POINT'
			
			#Socket Distance
			distance_socket_1 = mn_select_distance_empty.interface.new_socket(name = "Distance", in_out='INPUT', socket_type = 'NodeSocketFloat')
			distance_socket_1.subtype = 'NONE'
			distance_socket_1.default_value = 3.0
			distance_socket_1.min_value = -10000.0
			distance_socket_1.max_value = 10000.0
			distance_socket_1.attribute_domain = 'POINT'
			
			
			#initialize mn_select_distance_empty nodes
			#node Group Output
			group_output_2 = mn_select_distance_empty.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Reroute
			reroute = mn_select_distance_empty.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Object Info
			object_info = mn_select_distance_empty.nodes.new("GeometryNodeObjectInfo")
			object_info.name = "Object Info"
			object_info.transform_space = 'RELATIVE'
			#As Instance
			object_info.inputs[1].default_value = False
			
			#node Position
			position = mn_select_distance_empty.nodes.new("GeometryNodeInputPosition")
			position.name = "Position"
			
			#node Boolean Math
			boolean_math = mn_select_distance_empty.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'NOT'
			
			#node Map Range
			map_range = mn_select_distance_empty.nodes.new("ShaderNodeMapRange")
			map_range.name = "Map Range"
			map_range.clamp = True
			map_range.data_type = 'FLOAT'
			map_range.interpolation_type = 'LINEAR'
			#To Min
			map_range.inputs[3].default_value = 0.0
			#To Max
			map_range.inputs[4].default_value = 1.0
			
			#node Compare
			compare = mn_select_distance_empty.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'FLOAT'
			compare.mode = 'ELEMENT'
			compare.operation = 'GREATER_THAN'
			
			#node Group Input
			group_input_2 = mn_select_distance_empty.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
			#node Vector Math
			vector_math = mn_select_distance_empty.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.operation = 'DISTANCE'
			
			#node Group
			group_1 = mn_select_distance_empty.nodes.new("GeometryNodeGroup")
			group_1.name = "Group"
			group_1.node_tree = mn_units
			
			
			
			
			#Set locations
			group_output_2.location = (820.0, 100.0)
			reroute.location = (340.0, 80.0)
			object_info.location = (-447.0, 80.0)
			position.location = (-220.0, 40.0)
			boolean_math.location = (571.5794677734375, -13.08974838256836)
			map_range.location = (580.0, -140.0)
			compare.location = (376.64703369140625, 27.823856353759766)
			group_input_2.location = (-640.0, -140.0)
			vector_math.location = (-60.0, 140.0)
			group_1.location = (127.40702819824219, -27.151321411132812)
			
			#Set dimensions
			group_output_2.width, group_output_2.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			object_info.width, object_info.height = 140.0, 100.0
			position.width, position.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			map_range.width, map_range.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			group_input_2.width, group_input_2.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			group_1.width, group_1.height = 140.0, 100.0
			
			#initialize mn_select_distance_empty links
			#group_input_2.Object -> object_info.Object
			mn_select_distance_empty.links.new(group_input_2.outputs[0], object_info.inputs[0])
			#reroute.Output -> group_output_2.Distance
			mn_select_distance_empty.links.new(reroute.outputs[0], group_output_2.inputs[2])
			#reroute.Output -> compare.A
			mn_select_distance_empty.links.new(reroute.outputs[0], compare.inputs[0])
			#compare.Result -> boolean_math.Boolean
			mn_select_distance_empty.links.new(compare.outputs[0], boolean_math.inputs[0])
			#compare.Result -> group_output_2.> Cutoff
			mn_select_distance_empty.links.new(compare.outputs[0], group_output_2.inputs[0])
			#boolean_math.Boolean -> group_output_2.< Cutoff
			mn_select_distance_empty.links.new(boolean_math.outputs[0], group_output_2.inputs[1])
			#object_info.Location -> vector_math.Vector
			mn_select_distance_empty.links.new(object_info.outputs[1], vector_math.inputs[0])
			#position.Position -> vector_math.Vector
			mn_select_distance_empty.links.new(position.outputs[0], vector_math.inputs[1])
			#vector_math.Value -> reroute.Input
			mn_select_distance_empty.links.new(vector_math.outputs[1], reroute.inputs[0])
			#map_range.Result -> group_output_2.0..1
			mn_select_distance_empty.links.new(map_range.outputs[0], group_output_2.inputs[3])
			#vector_math.Value -> map_range.Value
			mn_select_distance_empty.links.new(vector_math.outputs[1], map_range.inputs[0])
			#group_input_2.From Min -> map_range.From Min
			mn_select_distance_empty.links.new(group_input_2.outputs[1], map_range.inputs[1])
			#group_input_2.From Max -> map_range.From Max
			mn_select_distance_empty.links.new(group_input_2.outputs[2], map_range.inputs[2])
			#group_input_2.Distance -> group_1.Value
			mn_select_distance_empty.links.new(group_input_2.outputs[3], group_1.inputs[0])
			#group_1.Angstrom -> compare.B
			mn_select_distance_empty.links.new(group_1.outputs[0], compare.inputs[1])
			return mn_select_distance_empty

		mn_select_distance_empty = mn_select_distance_empty_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "MN_select_distance_empty", type = 'NODES')
		mod.node_group = mn_select_distance_empty
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(MN_select_distance_empty.bl_idname)
			
def register():
	bpy.utils.register_class(MN_select_distance_empty)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(MN_select_distance_empty)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
