bl_info = {
	"name" : ".curve_to_mesh",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _curve_to_mesh(bpy.types.Operator):
	bl_idname = "node._curve_to_mesh"
	bl_label = ".curve_to_mesh"
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
			curve_socket = _curve_to_mesh.interface.new_socket(name = "Curve", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			curve_socket.attribute_domain = 'POINT'
			
			#Socket Profile Curve
			profile_curve_socket = _curve_to_mesh.interface.new_socket(name = "Profile Curve", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			profile_curve_socket.attribute_domain = 'POINT'
			
			#Socket Resolution
			resolution_socket = _curve_to_mesh.interface.new_socket(name = "Resolution", in_out='INPUT', socket_type = 'NodeSocketInt')
			resolution_socket.subtype = 'NONE'
			resolution_socket.default_value = 12
			resolution_socket.min_value = 3
			resolution_socket.max_value = 512
			resolution_socket.attribute_domain = 'POINT'
			
			#Socket Fill Caps
			fill_caps_socket = _curve_to_mesh.interface.new_socket(name = "Fill Caps", in_out='INPUT', socket_type = 'NodeSocketBool')
			fill_caps_socket.attribute_domain = 'POINT'
			
			#Socket Radius (A)
			radius__a__socket = _curve_to_mesh.interface.new_socket(name = "Radius (A)", in_out='INPUT', socket_type = 'NodeSocketFloat')
			radius__a__socket.subtype = 'NONE'
			radius__a__socket.default_value = 0.20000000298023224
			radius__a__socket.min_value = 0.0
			radius__a__socket.max_value = 10000.0
			radius__a__socket.attribute_domain = 'POINT'
			
			
			#initialize _curve_to_mesh nodes
			#node Group Output
			group_output_2 = _curve_to_mesh.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Curve to Mesh
			curve_to_mesh = _curve_to_mesh.nodes.new("GeometryNodeCurveToMesh")
			curve_to_mesh.name = "Curve to Mesh"
			
			#node Group
			group_1 = _curve_to_mesh.nodes.new("GeometryNodeGroup")
			group_1.name = "Group"
			group_1.node_tree = mn_units
			
			#node Curve Circle
			curve_circle = _curve_to_mesh.nodes.new("GeometryNodeCurvePrimitiveCircle")
			curve_circle.name = "Curve Circle"
			curve_circle.mode = 'RADIUS'
			#Radius
			curve_circle.inputs[4].default_value = 1.0
			
			#node Domain Size
			domain_size = _curve_to_mesh.nodes.new("GeometryNodeAttributeDomainSize")
			domain_size.name = "Domain Size"
			domain_size.component = 'CURVE'
			
			#node Compare
			compare = _curve_to_mesh.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'EQUAL'
			#B_INT
			compare.inputs[3].default_value = 0
			
			#node Switch
			switch = _curve_to_mesh.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'GEOMETRY'
			
			#node Group Input
			group_input_2 = _curve_to_mesh.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
			#node Set Curve Radius
			set_curve_radius = _curve_to_mesh.nodes.new("GeometryNodeSetCurveRadius")
			set_curve_radius.name = "Set Curve Radius"
			#Selection
			set_curve_radius.inputs[1].default_value = True
			
			
			
			
			#Set locations
			group_output_2.location = (190.0, 0.0)
			curve_to_mesh.location = (0.0, 0.0)
			group_1.location = (-577.7610473632812, -122.98338317871094)
			curve_circle.location = (-260.0, 40.0)
			domain_size.location = (-780.0, 120.0)
			compare.location = (-780.0, 280.0)
			switch.location = (-377.0369873046875, 349.30694580078125)
			group_input_2.location = (-780.0, -40.0)
			set_curve_radius.location = (-260.0, 180.0)
			
			#Set dimensions
			group_output_2.width, group_output_2.height = 140.0, 100.0
			curve_to_mesh.width, curve_to_mesh.height = 140.0, 100.0
			group_1.width, group_1.height = 261.9884033203125, 100.0
			curve_circle.width, curve_circle.height = 140.0, 100.0
			domain_size.width, domain_size.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			group_input_2.width, group_input_2.height = 140.0, 100.0
			set_curve_radius.width, set_curve_radius.height = 140.0, 100.0
			
			#initialize _curve_to_mesh links
			#set_curve_radius.Curve -> curve_to_mesh.Curve
			_curve_to_mesh.links.new(set_curve_radius.outputs[0], curve_to_mesh.inputs[0])
			#curve_to_mesh.Mesh -> group_output_2.Mesh
			_curve_to_mesh.links.new(curve_to_mesh.outputs[0], group_output_2.inputs[0])
			#group_input_2.Fill Caps -> curve_to_mesh.Fill Caps
			_curve_to_mesh.links.new(group_input_2.outputs[3], curve_to_mesh.inputs[2])
			#group_input_2.Curve -> set_curve_radius.Curve
			_curve_to_mesh.links.new(group_input_2.outputs[0], set_curve_radius.inputs[0])
			#group_1.Angstrom -> set_curve_radius.Radius
			_curve_to_mesh.links.new(group_1.outputs[0], set_curve_radius.inputs[2])
			#group_input_2.Radius (A) -> group_1.Value
			_curve_to_mesh.links.new(group_input_2.outputs[4], group_1.inputs[0])
			#group_input_2.Resolution -> curve_circle.Resolution
			_curve_to_mesh.links.new(group_input_2.outputs[2], curve_circle.inputs[0])
			#group_input_2.Profile Curve -> domain_size.Geometry
			_curve_to_mesh.links.new(group_input_2.outputs[1], domain_size.inputs[0])
			#domain_size.Point Count -> compare.A
			_curve_to_mesh.links.new(domain_size.outputs[0], compare.inputs[2])
			#compare.Result -> switch.Switch
			_curve_to_mesh.links.new(compare.outputs[0], switch.inputs[0])
			#curve_circle.Curve -> switch.True
			_curve_to_mesh.links.new(curve_circle.outputs[0], switch.inputs[2])
			#switch.Output -> curve_to_mesh.Profile Curve
			_curve_to_mesh.links.new(switch.outputs[0], curve_to_mesh.inputs[1])
			#group_input_2.Profile Curve -> switch.False
			_curve_to_mesh.links.new(group_input_2.outputs[1], switch.inputs[1])
			return _curve_to_mesh

		_curve_to_mesh = _curve_to_mesh_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".curve_to_mesh", type = 'NODES')
		mod.node_group = _curve_to_mesh
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_curve_to_mesh.bl_idname)
			
def register():
	bpy.utils.register_class(_curve_to_mesh)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_curve_to_mesh)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
