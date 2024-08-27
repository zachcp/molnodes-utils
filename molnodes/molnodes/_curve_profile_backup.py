bl_info = {
	"name" : ".curve_profile_backup",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _curve_profile_backup(bpy.types.Operator):
	bl_idname = "node._curve_profile_backup"
	bl_label = ".curve_profile_backup"
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

		#initialize _curve_profile_backup node group
		def _curve_profile_backup_node_group():
			_curve_profile_backup = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".curve_profile_backup")

			_curve_profile_backup.color_tag = 'NONE'
			_curve_profile_backup.description = ""

			_curve_profile_backup.is_modifier = True
			
			#_curve_profile_backup interface
			#Socket Output
			output_socket = _curve_profile_backup.interface.new_socket(name = "Output", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			output_socket.attribute_domain = 'POINT'
			
			#Socket Input
			input_socket = _curve_profile_backup.interface.new_socket(name = "Input", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			input_socket.attribute_domain = 'POINT'
			
			#Socket Resolution
			resolution_socket = _curve_profile_backup.interface.new_socket(name = "Resolution", in_out='INPUT', socket_type = 'NodeSocketInt')
			resolution_socket.default_value = 12
			resolution_socket.min_value = 3
			resolution_socket.max_value = 512
			resolution_socket.subtype = 'NONE'
			resolution_socket.attribute_domain = 'POINT'
			
			#Socket Radius
			radius_socket = _curve_profile_backup.interface.new_socket(name = "Radius", in_out='INPUT', socket_type = 'NodeSocketFloat')
			radius_socket.default_value = 0.009999999776482582
			radius_socket.min_value = 0.0
			radius_socket.max_value = 3.4028234663852886e+38
			radius_socket.subtype = 'DISTANCE'
			radius_socket.attribute_domain = 'POINT'
			
			#Socket Rotation
			rotation_socket = _curve_profile_backup.interface.new_socket(name = "Rotation", in_out='INPUT', socket_type = 'NodeSocketFloat')
			rotation_socket.default_value = 0.0
			rotation_socket.min_value = -10000.0
			rotation_socket.max_value = 10000.0
			rotation_socket.subtype = 'NONE'
			rotation_socket.attribute_domain = 'POINT'
			
			
			#initialize _curve_profile_backup nodes
			#node Group Output
			group_output_2 = _curve_profile_backup.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Compare
			compare = _curve_profile_backup.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.hide = True
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'GREATER_THAN'
			#B_INT
			compare.inputs[3].default_value = 0
			
			#node Switch
			switch = _curve_profile_backup.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'GEOMETRY'
			
			#node Domain Size
			domain_size = _curve_profile_backup.nodes.new("GeometryNodeAttributeDomainSize")
			domain_size.name = "Domain Size"
			domain_size.component = 'CURVE'
			
			#node Reroute.001
			reroute_001 = _curve_profile_backup.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			#node Curve Circle
			curve_circle = _curve_profile_backup.nodes.new("GeometryNodeCurvePrimitiveCircle")
			curve_circle.name = "Curve Circle"
			curve_circle.mode = 'RADIUS'
			
			#node Transform Geometry.001
			transform_geometry_001 = _curve_profile_backup.nodes.new("GeometryNodeTransform")
			transform_geometry_001.name = "Transform Geometry.001"
			transform_geometry_001.mode = 'COMPONENTS'
			#Translation
			transform_geometry_001.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Scale
			transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Combine XYZ
			combine_xyz = _curve_profile_backup.nodes.new("ShaderNodeCombineXYZ")
			combine_xyz.name = "Combine XYZ"
			#X
			combine_xyz.inputs[0].default_value = 0.0
			#Y
			combine_xyz.inputs[1].default_value = 0.0
			
			#node Group Input
			group_input_2 = _curve_profile_backup.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
			#node Group
			group_1 = _curve_profile_backup.nodes.new("GeometryNodeGroup")
			group_1.name = "Group"
			group_1.node_tree = mn_units
			
			
			
			
			#Set locations
			group_output_2.location = (320.278564453125, 0.0)
			compare.location = (-69.721435546875, 174.23248291015625)
			switch.location = (130.278564453125, 214.23248291015625)
			domain_size.location = (-77.112060546875, 125.76751708984375)
			reroute_001.location = (-130.278564453125, -81.5904541015625)
			curve_circle.location = (-77.112060546875, -214.23248291015625)
			transform_geometry_001.location = (130.278564453125, -45.76751708984375)
			combine_xyz.location = (-80.0, -360.0)
			group_input_2.location = (-392.2209777832031, -102.58642578125)
			group_1.location = (-380.0, -260.0)
			
			#Set dimensions
			group_output_2.width, group_output_2.height = 140.0, 100.0
			compare.width, compare.height = 137.39459228515625, 100.0
			switch.width, switch.height = 140.0, 100.0
			domain_size.width, domain_size.height = 140.0, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			curve_circle.width, curve_circle.height = 140.0, 100.0
			transform_geometry_001.width, transform_geometry_001.height = 140.0, 100.0
			combine_xyz.width, combine_xyz.height = 140.0, 100.0
			group_input_2.width, group_input_2.height = 140.0, 100.0
			group_1.width, group_1.height = 140.0, 100.0
			
			#initialize _curve_profile_backup links
			#domain_size.Point Count -> compare.A
			_curve_profile_backup.links.new(domain_size.outputs[0], compare.inputs[2])
			#reroute_001.Output -> domain_size.Geometry
			_curve_profile_backup.links.new(reroute_001.outputs[0], domain_size.inputs[0])
			#curve_circle.Curve -> transform_geometry_001.Geometry
			_curve_profile_backup.links.new(curve_circle.outputs[0], transform_geometry_001.inputs[0])
			#compare.Result -> switch.Switch
			_curve_profile_backup.links.new(compare.outputs[0], switch.inputs[0])
			#reroute_001.Output -> switch.True
			_curve_profile_backup.links.new(reroute_001.outputs[0], switch.inputs[2])
			#transform_geometry_001.Geometry -> switch.False
			_curve_profile_backup.links.new(transform_geometry_001.outputs[0], switch.inputs[1])
			#group_input_2.Input -> reroute_001.Input
			_curve_profile_backup.links.new(group_input_2.outputs[0], reroute_001.inputs[0])
			#switch.Output -> group_output_2.Output
			_curve_profile_backup.links.new(switch.outputs[0], group_output_2.inputs[0])
			#group_input_2.Resolution -> curve_circle.Resolution
			_curve_profile_backup.links.new(group_input_2.outputs[1], curve_circle.inputs[0])
			#combine_xyz.Vector -> transform_geometry_001.Rotation
			_curve_profile_backup.links.new(combine_xyz.outputs[0], transform_geometry_001.inputs[2])
			#group_input_2.Rotation -> combine_xyz.Z
			_curve_profile_backup.links.new(group_input_2.outputs[3], combine_xyz.inputs[2])
			#group_input_2.Radius -> group_1.Value
			_curve_profile_backup.links.new(group_input_2.outputs[2], group_1.inputs[0])
			#group_1.Angstrom -> curve_circle.Radius
			_curve_profile_backup.links.new(group_1.outputs[0], curve_circle.inputs[4])
			return _curve_profile_backup

		_curve_profile_backup = _curve_profile_backup_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".curve_profile_backup", type = 'NODES')
		mod.node_group = _curve_profile_backup
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_curve_profile_backup.bl_idname)
			
def register():
	bpy.utils.register_class(_curve_profile_backup)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_curve_profile_backup)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
