bl_info = {
	"name" : "Select Sphere",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Select_Sphere(bpy.types.Operator):
	bl_idname = "node.select_sphere"
	bl_label = "Select Sphere"
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

		#initialize select_sphere node group
		def select_sphere_node_group():
			select_sphere = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Select Sphere")

			select_sphere.color_tag = 'INPUT'
			select_sphere.description = ""

			
			#select_sphere interface
			#Socket Selection
			selection_socket = select_sphere.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket.attribute_domain = 'POINT'
			selection_socket.description = "The calculated selection"
			
			#Socket Inverted
			inverted_socket = select_sphere.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket.attribute_domain = 'POINT'
			inverted_socket.description = "The inverse of the calculated selection"
			
			#Socket 0..1
			_0__1_socket = select_sphere.interface.new_socket(name = "0..1", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			_0__1_socket.subtype = 'NONE'
			_0__1_socket.default_value = 0.0
			_0__1_socket.min_value = -3.4028234663852886e+38
			_0__1_socket.max_value = 3.4028234663852886e+38
			_0__1_socket.attribute_domain = 'POINT'
			
			#Socket And
			and_socket = select_sphere.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket.attribute_domain = 'POINT'
			and_socket.hide_value = True
			
			#Socket Or
			or_socket = select_sphere.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket.attribute_domain = 'POINT'
			or_socket.hide_value = True
			
			#Socket Object
			object_socket = select_sphere.interface.new_socket(name = "Object", in_out='INPUT', socket_type = 'NodeSocketObject')
			object_socket.attribute_domain = 'POINT'
			
			#Socket From Min (A)
			from_min__a__socket = select_sphere.interface.new_socket(name = "From Min (A)", in_out='INPUT', socket_type = 'NodeSocketFloat')
			from_min__a__socket.subtype = 'NONE'
			from_min__a__socket.default_value = 0.0
			from_min__a__socket.min_value = -10000.0
			from_min__a__socket.max_value = 10000.0
			from_min__a__socket.attribute_domain = 'POINT'
			
			#Socket From Max (A)
			from_max__a__socket = select_sphere.interface.new_socket(name = "From Max (A)", in_out='INPUT', socket_type = 'NodeSocketFloat')
			from_max__a__socket.subtype = 'NONE'
			from_max__a__socket.default_value = 10.0
			from_max__a__socket.min_value = -10000.0
			from_max__a__socket.max_value = 10000.0
			from_max__a__socket.attribute_domain = 'POINT'
			
			
			#initialize select_sphere nodes
			#node Group Input
			group_input_2 = select_sphere.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			group_input_2.outputs[0].hide = True
			
			#node Math.003
			math_003 = select_sphere.nodes.new("ShaderNodeMath")
			math_003.name = "Math.003"
			math_003.operation = 'ABSOLUTE'
			math_003.use_clamp = False
			
			#node Map Range
			map_range = select_sphere.nodes.new("ShaderNodeMapRange")
			map_range.name = "Map Range"
			map_range.clamp = True
			map_range.data_type = 'FLOAT'
			map_range.interpolation_type = 'LINEAR'
			#To Min
			map_range.inputs[3].default_value = 0.0
			#To Max
			map_range.inputs[4].default_value = 1.0
			
			#node Position
			position = select_sphere.nodes.new("GeometryNodeInputPosition")
			position.name = "Position"
			
			#node Object Info
			object_info = select_sphere.nodes.new("GeometryNodeObjectInfo")
			object_info.name = "Object Info"
			object_info.transform_space = 'RELATIVE'
			#As Instance
			object_info.inputs[1].default_value = True
			
			#node Vector Math.002
			vector_math_002 = select_sphere.nodes.new("ShaderNodeVectorMath")
			vector_math_002.name = "Vector Math.002"
			vector_math_002.operation = 'DISTANCE'
			
			#node Group Output
			group_output_2 = select_sphere.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Compare
			compare = select_sphere.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'FLOAT'
			compare.mode = 'ELEMENT'
			compare.operation = 'LESS_THAN'
			
			#node Boolean Math
			boolean_math = select_sphere.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'NOT'
			
			#node Math.002
			math_002 = select_sphere.nodes.new("ShaderNodeMath")
			math_002.name = "Math.002"
			math_002.operation = 'SUBTRACT'
			math_002.use_clamp = False
			
			#node Math.004
			math_004 = select_sphere.nodes.new("ShaderNodeMath")
			math_004.name = "Math.004"
			math_004.operation = 'MULTIPLY'
			math_004.use_clamp = False
			#Value_001
			math_004.inputs[1].default_value = 1.0
			
			#node Group Input.001
			group_input_001 = select_sphere.nodes.new("NodeGroupInput")
			group_input_001.name = "Group Input.001"
			group_input_001.outputs[0].hide = True
			
			#node Group.001
			group_001 = select_sphere.nodes.new("GeometryNodeGroup")
			group_001.name = "Group.001"
			group_001.node_tree = mn_units
			
			#node Group
			group_1 = select_sphere.nodes.new("GeometryNodeGroup")
			group_1.name = "Group"
			group_1.node_tree = mn_units
			
			#node Vector Math
			vector_math = select_sphere.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.operation = 'ABSOLUTE'
			
			#node Reroute
			reroute = select_sphere.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Boolean Math.001
			boolean_math_001 = select_sphere.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001.name = "Boolean Math.001"
			boolean_math_001.hide = True
			boolean_math_001.operation = 'AND'
			
			#node Group Input.002
			group_input_002 = select_sphere.nodes.new("NodeGroupInput")
			group_input_002.name = "Group Input.002"
			group_input_002.outputs[2].hide = True
			group_input_002.outputs[3].hide = True
			group_input_002.outputs[4].hide = True
			group_input_002.outputs[5].hide = True
			
			#node Boolean Math.002
			boolean_math_002 = select_sphere.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002.name = "Boolean Math.002"
			boolean_math_002.operation = 'AND'
			
			
			
			
			#Set locations
			group_input_2.location = (-760.0, 220.0)
			math_003.location = (-40.0, 40.0)
			map_range.location = (180.0, 20.0)
			position.location = (-560.0, 300.0)
			object_info.location = (-560.0, 240.0)
			vector_math_002.location = (-380.0, 300.0)
			group_output_2.location = (607.9999389648438, 140.0)
			compare.location = (-200.0, 300.0)
			boolean_math.location = (368.0, 140.0)
			math_002.location = (-200.0, 40.0)
			math_004.location = (-380.0, 40.0)
			group_input_001.location = (-352.86383056640625, -163.8787841796875)
			group_001.location = (-40.0, -260.0)
			group_1.location = (-40.0, -140.0)
			vector_math.location = (-380.0, 160.0)
			reroute.location = (328.0, 160.0)
			boolean_math_001.location = (-40.0, 300.0)
			group_input_002.location = (-200.0, 360.0)
			boolean_math_002.location = (120.0, 340.0)
			
			#Set dimensions
			group_input_2.width, group_input_2.height = 140.0, 100.0
			math_003.width, math_003.height = 140.0, 100.0
			map_range.width, map_range.height = 140.0, 100.0
			position.width, position.height = 140.0, 100.0
			object_info.width, object_info.height = 140.0, 100.0
			vector_math_002.width, vector_math_002.height = 140.0, 100.0
			group_output_2.width, group_output_2.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			math_002.width, math_002.height = 140.0, 100.0
			math_004.width, math_004.height = 140.0, 100.0
			group_input_001.width, group_input_001.height = 140.0, 100.0
			group_001.width, group_001.height = 140.0, 100.0
			group_1.width, group_1.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
			group_input_002.width, group_input_002.height = 140.0, 100.0
			boolean_math_002.width, boolean_math_002.height = 140.0, 100.0
			
			#initialize select_sphere links
			#group_input_2.Object -> object_info.Object
			select_sphere.links.new(group_input_2.outputs[2], object_info.inputs[0])
			#group_1.Angstrom -> map_range.From Min
			select_sphere.links.new(group_1.outputs[0], map_range.inputs[1])
			#map_range.Result -> group_output_2.0..1
			select_sphere.links.new(map_range.outputs[0], group_output_2.inputs[2])
			#object_info.Location -> vector_math_002.Vector
			select_sphere.links.new(object_info.outputs[1], vector_math_002.inputs[1])
			#vector_math_002.Value -> compare.A
			select_sphere.links.new(vector_math_002.outputs[1], compare.inputs[0])
			#vector_math.Vector -> compare.B
			select_sphere.links.new(vector_math.outputs[0], compare.inputs[1])
			#reroute.Output -> group_output_2.Selection
			select_sphere.links.new(reroute.outputs[0], group_output_2.inputs[0])
			#vector_math_002.Value -> math_002.Value
			select_sphere.links.new(vector_math_002.outputs[1], math_002.inputs[0])
			#math_002.Value -> math_003.Value
			select_sphere.links.new(math_002.outputs[0], math_003.inputs[0])
			#math_003.Value -> map_range.Value
			select_sphere.links.new(math_003.outputs[0], map_range.inputs[0])
			#group_001.Angstrom -> map_range.From Max
			select_sphere.links.new(group_001.outputs[0], map_range.inputs[2])
			#position.Position -> vector_math_002.Vector
			select_sphere.links.new(position.outputs[0], vector_math_002.inputs[0])
			#reroute.Output -> boolean_math.Boolean
			select_sphere.links.new(reroute.outputs[0], boolean_math.inputs[0])
			#boolean_math.Boolean -> group_output_2.Inverted
			select_sphere.links.new(boolean_math.outputs[0], group_output_2.inputs[1])
			#vector_math.Vector -> math_004.Value
			select_sphere.links.new(vector_math.outputs[0], math_004.inputs[0])
			#math_004.Value -> math_002.Value
			select_sphere.links.new(math_004.outputs[0], math_002.inputs[1])
			#group_input_001.From Min (A) -> group_1.Value
			select_sphere.links.new(group_input_001.outputs[3], group_1.inputs[0])
			#group_input_001.From Max (A) -> group_001.Value
			select_sphere.links.new(group_input_001.outputs[4], group_001.inputs[0])
			#object_info.Scale -> vector_math.Vector
			select_sphere.links.new(object_info.outputs[3], vector_math.inputs[0])
			#boolean_math_002.Boolean -> reroute.Input
			select_sphere.links.new(boolean_math_002.outputs[0], reroute.inputs[0])
			#compare.Result -> boolean_math_001.Boolean
			select_sphere.links.new(compare.outputs[0], boolean_math_001.inputs[1])
			#group_input_002.And -> boolean_math_001.Boolean
			select_sphere.links.new(group_input_002.outputs[0], boolean_math_001.inputs[0])
			#boolean_math_001.Boolean -> boolean_math_002.Boolean
			select_sphere.links.new(boolean_math_001.outputs[0], boolean_math_002.inputs[0])
			#group_input_002.Or -> boolean_math_002.Boolean
			select_sphere.links.new(group_input_002.outputs[1], boolean_math_002.inputs[1])
			return select_sphere

		select_sphere = select_sphere_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Select Sphere", type = 'NODES')
		mod.node_group = select_sphere
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Select_Sphere.bl_idname)
			
def register():
	bpy.utils.register_class(Select_Sphere)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Select_Sphere)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
