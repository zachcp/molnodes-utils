bl_info = {
	"name" : ".cartoon.arrow_primitive",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _cartoon_arrow_primitive(bpy.types.Operator):
	bl_idname = "node._cartoon_arrow_primitive"
	bl_label = ".cartoon.arrow_primitive"
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

		#initialize _cartoon_arrow_primitive node group
		def _cartoon_arrow_primitive_node_group():
			_cartoon_arrow_primitive = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".cartoon.arrow_primitive")

			_cartoon_arrow_primitive.color_tag = 'NONE'
			_cartoon_arrow_primitive.description = ""

			_cartoon_arrow_primitive.is_modifier = True
			
			#_cartoon_arrow_primitive interface
			#Socket Geometry
			geometry_socket = _cartoon_arrow_primitive.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_1 = _cartoon_arrow_primitive.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket_1.subtype = 'NONE'
			value_socket_1.default_value = 0.5
			value_socket_1.min_value = -10000.0
			value_socket_1.max_value = 10000.0
			value_socket_1.attribute_domain = 'POINT'
			
			
			#initialize _cartoon_arrow_primitive nodes
			#node Group Output
			group_output_2 = _cartoon_arrow_primitive.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Group Input
			group_input_2 = _cartoon_arrow_primitive.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
			#node Transform Geometry
			transform_geometry = _cartoon_arrow_primitive.nodes.new("GeometryNodeTransform")
			transform_geometry.name = "Transform Geometry"
			transform_geometry.mode = 'COMPONENTS'
			#Translation
			transform_geometry.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Rotation
			transform_geometry.inputs[2].default_value = (0.0, 3.1415927410125732, 0.0)
			
			#node Transform Geometry.002
			transform_geometry_002 = _cartoon_arrow_primitive.nodes.new("GeometryNodeTransform")
			transform_geometry_002.name = "Transform Geometry.002"
			transform_geometry_002.mode = 'COMPONENTS'
			#Rotation
			transform_geometry_002.inputs[2].default_value = (1.5707963705062866, 0.0, 0.0)
			#Scale
			transform_geometry_002.inputs[3].default_value = (1.0, 0.8299999833106995, 1.0)
			
			#node Group.005
			group_005 = _cartoon_arrow_primitive.nodes.new("GeometryNodeGroup")
			group_005.name = "Group.005"
			group_005.node_tree = mn_units
			#Input_1
			group_005.inputs[0].default_value = 3.390000104904175
			
			#node Join Geometry.001
			join_geometry_001 = _cartoon_arrow_primitive.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_001.name = "Join Geometry.001"
			join_geometry_001.hide = True
			
			#node Merge by Distance
			merge_by_distance = _cartoon_arrow_primitive.nodes.new("GeometryNodeMergeByDistance")
			merge_by_distance.name = "Merge by Distance"
			merge_by_distance.hide = True
			merge_by_distance.mode = 'ALL'
			#Selection
			merge_by_distance.inputs[1].default_value = True
			#Distance
			merge_by_distance.inputs[2].default_value = 0.0010000000474974513
			
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
			group_001 = _cartoon_arrow_primitive.nodes.new("GeometryNodeGroup")
			group_001.name = "Group.001"
			group_001.node_tree = mn_units
			#Input_1
			group_001.inputs[0].default_value = 2.130000114440918
			
			#node Group.011
			group_011 = _cartoon_arrow_primitive.nodes.new("GeometryNodeGroup")
			group_011.name = "Group.011"
			group_011.node_tree = mn_units
			#Input_1
			group_011.inputs[0].default_value = 1.2000000476837158
			
			#node Math.002
			math_002 = _cartoon_arrow_primitive.nodes.new("ShaderNodeMath")
			math_002.name = "Math.002"
			math_002.operation = 'MULTIPLY'
			math_002.use_clamp = False
			#Value_001
			math_002.inputs[1].default_value = 1.399999976158142
			
			#node Reroute
			reroute = _cartoon_arrow_primitive.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Reroute.001
			reroute_001 = _cartoon_arrow_primitive.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			#node Reroute.002
			reroute_002 = _cartoon_arrow_primitive.nodes.new("NodeReroute")
			reroute_002.name = "Reroute.002"
			#node Combine XYZ.002
			combine_xyz_002 = _cartoon_arrow_primitive.nodes.new("ShaderNodeCombineXYZ")
			combine_xyz_002.name = "Combine XYZ.002"
			#X
			combine_xyz_002.inputs[0].default_value = 1.0
			#Z
			combine_xyz_002.inputs[2].default_value = 1.0
			
			#node Math.001
			math_001_1 = _cartoon_arrow_primitive.nodes.new("ShaderNodeMath")
			math_001_1.label = "x / 2"
			math_001_1.name = "Math.001"
			math_001_1.hide = True
			math_001_1.operation = 'DIVIDE'
			math_001_1.use_clamp = False
			#Value_001
			math_001_1.inputs[1].default_value = 3.059999942779541
			
			#node Math
			math_1 = _cartoon_arrow_primitive.nodes.new("ShaderNodeMath")
			math_1.label = "x / -2"
			math_1.name = "Math"
			math_1.hide = True
			math_1.operation = 'DIVIDE'
			math_1.use_clamp = False
			#Value_001
			math_1.inputs[1].default_value = -19.440000534057617
			
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
			group_output_2.location = (686.1517333984375, 0.0)
			group_input_2.location = (-874.151611328125, 0.0)
			transform_geometry.location = (245.848388671875, -5.45166015625)
			transform_geometry_002.location = (-114.151611328125, -45.45166015625)
			group_005.location = (-674.151611328125, 14.54833984375)
			join_geometry_001.location = (-434.151611328125, -125.45166015625)
			merge_by_distance.location = (-434.151611328125, -165.45166015625)
			mesh_circle.location = (-674.151611328125, 154.54833984375)
			combine_xyz_001.location = (-274.151611328125, -185.45166015625)
			group_001.location = (-674.151611328125, -105.45166015625)
			group_011.location = (-674.151611328125, -245.45166015625)
			math_002.location = (-118.0, -320.0)
			reroute.location = (-718.0, -420.0)
			reroute_001.location = (-478.0, -600.0)
			reroute_002.location = (-178.0, -600.0)
			combine_xyz_002.location = (242.0, -280.0)
			math_001_1.location = (-438.0, -220.0)
			math_1.location = (-438.0, -300.0)
			extrude_mesh.location = (-434.151611328125, 134.54833984375)
			
			#Set dimensions
			group_output_2.width, group_output_2.height = 140.0, 100.0
			group_input_2.width, group_input_2.height = 140.0, 100.0
			transform_geometry.width, transform_geometry.height = 140.0, 100.0
			transform_geometry_002.width, transform_geometry_002.height = 140.0, 100.0
			group_005.width, group_005.height = 140.0, 100.0
			join_geometry_001.width, join_geometry_001.height = 140.0, 100.0
			merge_by_distance.width, merge_by_distance.height = 140.0, 100.0
			mesh_circle.width, mesh_circle.height = 140.0, 100.0
			combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
			group_001.width, group_001.height = 140.0, 100.0
			group_011.width, group_011.height = 140.0, 100.0
			math_002.width, math_002.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			reroute_002.width, reroute_002.height = 16.0, 100.0
			combine_xyz_002.width, combine_xyz_002.height = 140.0, 100.0
			math_001_1.width, math_001_1.height = 140.0, 100.0
			math_1.width, math_1.height = 140.0, 100.0
			extrude_mesh.width, extrude_mesh.height = 140.0, 100.0
			
			#initialize _cartoon_arrow_primitive links
			#group_005.Angstrom -> math_001_1.Value
			_cartoon_arrow_primitive.links.new(group_005.outputs[0], math_001_1.inputs[0])
			#mesh_circle.Mesh -> extrude_mesh.Mesh
			_cartoon_arrow_primitive.links.new(mesh_circle.outputs[0], extrude_mesh.inputs[0])
			#group_005.Angstrom -> mesh_circle.Radius
			_cartoon_arrow_primitive.links.new(group_005.outputs[0], mesh_circle.inputs[1])
			#math_001_1.Value -> combine_xyz_001.X
			_cartoon_arrow_primitive.links.new(math_001_1.outputs[0], combine_xyz_001.inputs[0])
			#math_002.Value -> combine_xyz_002.Y
			_cartoon_arrow_primitive.links.new(math_002.outputs[0], combine_xyz_002.inputs[1])
			#group_001.Angstrom -> math_1.Value
			_cartoon_arrow_primitive.links.new(group_001.outputs[0], math_1.inputs[0])
			#math_1.Value -> combine_xyz_001.Z
			_cartoon_arrow_primitive.links.new(math_1.outputs[0], combine_xyz_001.inputs[2])
			#mesh_circle.Mesh -> join_geometry_001.Geometry
			_cartoon_arrow_primitive.links.new(mesh_circle.outputs[0], join_geometry_001.inputs[0])
			#combine_xyz_001.Vector -> transform_geometry_002.Translation
			_cartoon_arrow_primitive.links.new(combine_xyz_001.outputs[0], transform_geometry_002.inputs[1])
			#combine_xyz_002.Vector -> transform_geometry.Scale
			_cartoon_arrow_primitive.links.new(combine_xyz_002.outputs[0], transform_geometry.inputs[3])
			#merge_by_distance.Geometry -> transform_geometry_002.Geometry
			_cartoon_arrow_primitive.links.new(merge_by_distance.outputs[0], transform_geometry_002.inputs[0])
			#join_geometry_001.Geometry -> merge_by_distance.Geometry
			_cartoon_arrow_primitive.links.new(join_geometry_001.outputs[0], merge_by_distance.inputs[0])
			#group_001.Angstrom -> extrude_mesh.Offset Scale
			_cartoon_arrow_primitive.links.new(group_001.outputs[0], extrude_mesh.inputs[3])
			#transform_geometry_002.Geometry -> transform_geometry.Geometry
			_cartoon_arrow_primitive.links.new(transform_geometry_002.outputs[0], transform_geometry.inputs[0])
			#group_011.Angstrom -> combine_xyz_001.Y
			_cartoon_arrow_primitive.links.new(group_011.outputs[0], combine_xyz_001.inputs[1])
			#reroute_002.Output -> math_002.Value
			_cartoon_arrow_primitive.links.new(reroute_002.outputs[0], math_002.inputs[0])
			#transform_geometry.Geometry -> group_output_2.Geometry
			_cartoon_arrow_primitive.links.new(transform_geometry.outputs[0], group_output_2.inputs[0])
			#group_input_2.Value -> reroute.Input
			_cartoon_arrow_primitive.links.new(group_input_2.outputs[0], reroute.inputs[0])
			#reroute.Output -> reroute_001.Input
			_cartoon_arrow_primitive.links.new(reroute.outputs[0], reroute_001.inputs[0])
			#reroute_001.Output -> reroute_002.Input
			_cartoon_arrow_primitive.links.new(reroute_001.outputs[0], reroute_002.inputs[0])
			#extrude_mesh.Mesh -> join_geometry_001.Geometry
			_cartoon_arrow_primitive.links.new(extrude_mesh.outputs[0], join_geometry_001.inputs[0])
			return _cartoon_arrow_primitive

		_cartoon_arrow_primitive = _cartoon_arrow_primitive_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".cartoon.arrow_primitive", type = 'NODES')
		mod.node_group = _cartoon_arrow_primitive
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_cartoon_arrow_primitive.bl_idname)
			
def register():
	bpy.utils.register_class(_cartoon_arrow_primitive)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_cartoon_arrow_primitive)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
