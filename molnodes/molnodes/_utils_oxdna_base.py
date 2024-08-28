bl_info = {
	"name" : ".utils_oxdna_base",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _utils_oxdna_base(bpy.types.Operator):
	bl_idname = "node._utils_oxdna_base"
	bl_label = ".utils_oxdna_base"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _utils_oxdna_base node group
		def _utils_oxdna_base_node_group():
			_utils_oxdna_base = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".utils_oxdna_base")

			_utils_oxdna_base.color_tag = 'NONE'
			_utils_oxdna_base.description = ""

			_utils_oxdna_base.is_modifier = True
			
			#_utils_oxdna_base interface
			#Socket Geometry
			geometry_socket = _utils_oxdna_base.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket = _utils_oxdna_base.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket.default_value = 0.5
			value_socket.min_value = -10000.0
			value_socket.max_value = 10000.0
			value_socket.subtype = 'NONE'
			value_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_1 = _utils_oxdna_base.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket_1.default_value = 0.5
			value_socket_1.min_value = -10000.0
			value_socket_1.max_value = 10000.0
			value_socket_1.subtype = 'NONE'
			value_socket_1.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_2 = _utils_oxdna_base.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket_2.default_value = 0.5
			value_socket_2.min_value = -10000.0
			value_socket_2.max_value = 10000.0
			value_socket_2.subtype = 'NONE'
			value_socket_2.attribute_domain = 'POINT'
			
			
			#initialize _utils_oxdna_base nodes
			#node Group Output
			group_output = _utils_oxdna_base.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = _utils_oxdna_base.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Math
			math = _utils_oxdna_base.nodes.new("ShaderNodeMath")
			math.name = "Math"
			math.operation = 'DIVIDE'
			math.use_clamp = False
			#Value_001
			math.inputs[1].default_value = 2.0
			
			#node Transform Geometry
			transform_geometry = _utils_oxdna_base.nodes.new("GeometryNodeTransform")
			transform_geometry.name = "Transform Geometry"
			transform_geometry.mode = 'COMPONENTS'
			#Rotation
			transform_geometry.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Scale
			transform_geometry.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Cylinder
			cylinder = _utils_oxdna_base.nodes.new("GeometryNodeMeshCylinder")
			cylinder.name = "Cylinder"
			cylinder.fill_type = 'NGON'
			#Vertices
			cylinder.inputs[0].default_value = 4
			#Side Segments
			cylinder.inputs[1].default_value = 1
			#Fill Segments
			cylinder.inputs[2].default_value = 1
			
			#node Combine XYZ
			combine_xyz = _utils_oxdna_base.nodes.new("ShaderNodeCombineXYZ")
			combine_xyz.name = "Combine XYZ"
			#X
			combine_xyz.inputs[0].default_value = 0.0
			#Y
			combine_xyz.inputs[1].default_value = 0.0
			
			#node Reroute
			reroute = _utils_oxdna_base.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Math.002
			math_002 = _utils_oxdna_base.nodes.new("ShaderNodeMath")
			math_002.name = "Math.002"
			math_002.operation = 'DIVIDE'
			math_002.use_clamp = False
			#Value_001
			math_002.inputs[1].default_value = 100.0
			
			#node Math.001
			math_001 = _utils_oxdna_base.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.operation = 'DIVIDE'
			math_001.use_clamp = False
			#Value_001
			math_001.inputs[1].default_value = 100.0
			
			#node Math.003
			math_003 = _utils_oxdna_base.nodes.new("ShaderNodeMath")
			math_003.name = "Math.003"
			math_003.operation = 'DIVIDE'
			math_003.use_clamp = False
			#Value_001
			math_003.inputs[1].default_value = 10.0
			
			#node Transform Geometry.001
			transform_geometry_001 = _utils_oxdna_base.nodes.new("GeometryNodeTransform")
			transform_geometry_001.name = "Transform Geometry.001"
			transform_geometry_001.mode = 'COMPONENTS'
			#Translation
			transform_geometry_001.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Rotation
			transform_geometry_001.inputs[2].default_value = (0.0, 0.0, 0.7853981852531433)
			#Scale
			transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Combine XYZ.001
			combine_xyz_001 = _utils_oxdna_base.nodes.new("ShaderNodeCombineXYZ")
			combine_xyz_001.name = "Combine XYZ.001"
			#Y
			combine_xyz_001.inputs[1].default_value = 1.0
			#Z
			combine_xyz_001.inputs[2].default_value = 1.0
			
			#node Transform Geometry.002
			transform_geometry_002 = _utils_oxdna_base.nodes.new("GeometryNodeTransform")
			transform_geometry_002.name = "Transform Geometry.002"
			transform_geometry_002.mode = 'COMPONENTS'
			#Translation
			transform_geometry_002.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Rotation
			transform_geometry_002.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			
			
			
			#Set locations
			group_output.location = (623.913818359375, 0.0)
			group_input.location = (-633.9136962890625, 0.0)
			math.location = (-39.2435302734375, -142.93002319335938)
			transform_geometry.location = (115.4232177734375, 243.7366180419922)
			cylinder.location = (-39.2435302734375, 243.7366180419922)
			combine_xyz.location = (-39.2435302734375, -26.9300537109375)
			reroute.location = (-210.3306884765625, -78.89993286132812)
			math_002.location = (-433.9136962890625, 97.47659301757812)
			math_001.location = (-430.997314453125, -65.59671020507812)
			math_003.location = (-432.2694091796875, -243.73660278320312)
			transform_geometry_001.location = (270.08984375, 243.7366180419922)
			combine_xyz_001.location = (265.00262451171875, -65.59671020507812)
			transform_geometry_002.location = (433.913818359375, 194.11192321777344)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			transform_geometry.width, transform_geometry.height = 140.0, 100.0
			cylinder.width, cylinder.height = 140.0, 100.0
			combine_xyz.width, combine_xyz.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			math_002.width, math_002.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			math_003.width, math_003.height = 140.0, 100.0
			transform_geometry_001.width, transform_geometry_001.height = 140.0, 100.0
			combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
			transform_geometry_002.width, transform_geometry_002.height = 140.0, 100.0
			
			#initialize _utils_oxdna_base links
			#reroute.Output -> cylinder.Depth
			_utils_oxdna_base.links.new(reroute.outputs[0], cylinder.inputs[4])
			#transform_geometry.Geometry -> transform_geometry_001.Geometry
			_utils_oxdna_base.links.new(transform_geometry.outputs[0], transform_geometry_001.inputs[0])
			#combine_xyz_001.Vector -> transform_geometry_002.Scale
			_utils_oxdna_base.links.new(combine_xyz_001.outputs[0], transform_geometry_002.inputs[3])
			#cylinder.Mesh -> transform_geometry.Geometry
			_utils_oxdna_base.links.new(cylinder.outputs[0], transform_geometry.inputs[0])
			#math_001.Value -> reroute.Input
			_utils_oxdna_base.links.new(math_001.outputs[0], reroute.inputs[0])
			#math_002.Value -> cylinder.Radius
			_utils_oxdna_base.links.new(math_002.outputs[0], cylinder.inputs[3])
			#combine_xyz.Vector -> transform_geometry.Translation
			_utils_oxdna_base.links.new(combine_xyz.outputs[0], transform_geometry.inputs[1])
			#transform_geometry_001.Geometry -> transform_geometry_002.Geometry
			_utils_oxdna_base.links.new(transform_geometry_001.outputs[0], transform_geometry_002.inputs[0])
			#math_003.Value -> combine_xyz_001.X
			_utils_oxdna_base.links.new(math_003.outputs[0], combine_xyz_001.inputs[0])
			#reroute.Output -> math.Value
			_utils_oxdna_base.links.new(reroute.outputs[0], math.inputs[0])
			#math.Value -> combine_xyz.Z
			_utils_oxdna_base.links.new(math.outputs[0], combine_xyz.inputs[2])
			#group_input.Value -> math_002.Value
			_utils_oxdna_base.links.new(group_input.outputs[0], math_002.inputs[0])
			#group_input.Value -> math_001.Value
			_utils_oxdna_base.links.new(group_input.outputs[1], math_001.inputs[0])
			#group_input.Value -> math_003.Value
			_utils_oxdna_base.links.new(group_input.outputs[2], math_003.inputs[0])
			#transform_geometry_002.Geometry -> group_output.Geometry
			_utils_oxdna_base.links.new(transform_geometry_002.outputs[0], group_output.inputs[0])
			return _utils_oxdna_base

		_utils_oxdna_base = _utils_oxdna_base_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".utils_oxdna_base", type = 'NODES')
		mod.node_group = _utils_oxdna_base
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_utils_oxdna_base.bl_idname)
			
def register():
	bpy.utils.register_class(_utils_oxdna_base)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_utils_oxdna_base)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
