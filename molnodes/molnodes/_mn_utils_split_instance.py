bl_info = {
	"name" : ".MN_utils_split_instance",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _MN_utils_split_instance(bpy.types.Operator):
	bl_idname = "node._mn_utils_split_instance"
	bl_label = ".MN_utils_split_instance"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _mn_utils_split_instance node group
		def _mn_utils_split_instance_node_group():
			_mn_utils_split_instance = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_utils_split_instance")

			_mn_utils_split_instance.color_tag = 'NONE'
			_mn_utils_split_instance.description = ""

			_mn_utils_split_instance.is_modifier = True
			
			#_mn_utils_split_instance interface
			#Socket Instance
			instance_socket = _mn_utils_split_instance.interface.new_socket(name = "Instance", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			instance_socket.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket = _mn_utils_split_instance.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket.attribute_domain = 'POINT'
			
			#Socket Field
			field_socket = _mn_utils_split_instance.interface.new_socket(name = "Field", in_out='INPUT', socket_type = 'NodeSocketInt')
			field_socket.subtype = 'NONE'
			field_socket.default_value = 0
			field_socket.min_value = -2147483648
			field_socket.max_value = 2147483647
			field_socket.attribute_domain = 'POINT'
			
			#Socket Group ID
			group_id_socket = _mn_utils_split_instance.interface.new_socket(name = "Group ID", in_out='INPUT', socket_type = 'NodeSocketInt')
			group_id_socket.subtype = 'NONE'
			group_id_socket.default_value = 0
			group_id_socket.min_value = -2147483648
			group_id_socket.max_value = 2147483647
			group_id_socket.attribute_domain = 'POINT'
			
			#Socket Origin Offset
			origin_offset_socket = _mn_utils_split_instance.interface.new_socket(name = "Origin Offset", in_out='INPUT', socket_type = 'NodeSocketVector')
			origin_offset_socket.subtype = 'NONE'
			origin_offset_socket.default_value = (0.0, 0.0, 0.0)
			origin_offset_socket.min_value = -10000.0
			origin_offset_socket.max_value = 10000.0
			origin_offset_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_utils_split_instance nodes
			#node Compare
			compare = _mn_utils_split_instance.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'EQUAL'
			
			#node Bounding Box
			bounding_box = _mn_utils_split_instance.nodes.new("GeometryNodeBoundBox")
			bounding_box.name = "Bounding Box"
			
			#node Separate Geometry
			separate_geometry = _mn_utils_split_instance.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry.name = "Separate Geometry"
			separate_geometry.domain = 'POINT'
			
			#node Mix
			mix = _mn_utils_split_instance.nodes.new("ShaderNodeMix")
			mix.name = "Mix"
			mix.hide = True
			mix.blend_type = 'MIX'
			mix.clamp_factor = True
			mix.clamp_result = False
			mix.data_type = 'VECTOR'
			mix.factor_mode = 'UNIFORM'
			#Factor_Float
			mix.inputs[0].default_value = 0.5
			
			#node Group Input
			group_input = _mn_utils_split_instance.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Vector Math
			vector_math = _mn_utils_split_instance.nodes.new("ShaderNodeVectorMath")
			vector_math.label = "-x"
			vector_math.name = "Vector Math"
			vector_math.hide = True
			vector_math.operation = 'SCALE'
			#Scale
			vector_math.inputs[3].default_value = -1.0
			
			#node Vector Math.001
			vector_math_001 = _mn_utils_split_instance.nodes.new("ShaderNodeVectorMath")
			vector_math_001.name = "Vector Math.001"
			vector_math_001.hide = True
			vector_math_001.operation = 'ADD'
			
			#node Transform Geometry
			transform_geometry = _mn_utils_split_instance.nodes.new("GeometryNodeTransform")
			transform_geometry.name = "Transform Geometry"
			transform_geometry.mode = 'COMPONENTS'
			#Rotation
			transform_geometry.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Scale
			transform_geometry.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Geometry to Instance
			geometry_to_instance = _mn_utils_split_instance.nodes.new("GeometryNodeGeometryToInstance")
			geometry_to_instance.name = "Geometry to Instance"
			
			#node Translate Instances
			translate_instances = _mn_utils_split_instance.nodes.new("GeometryNodeTranslateInstances")
			translate_instances.name = "Translate Instances"
			#Selection
			translate_instances.inputs[1].default_value = True
			#Local Space
			translate_instances.inputs[3].default_value = True
			
			#node Group Output
			group_output = _mn_utils_split_instance.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			
			
			
			#Set locations
			compare.location = (-1.379150390625, -79.22293090820312)
			bounding_box.location = (0.0, 220.0)
			separate_geometry.location = (1.379150390625, 79.22293090820312)
			mix.location = (0.0, 260.0)
			group_input.location = (-201.379150390625, 0.0)
			vector_math.location = (0.0, 340.0)
			vector_math_001.location = (0.0, 300.0)
			transform_geometry.location = (160.0, 80.0)
			geometry_to_instance.location = (320.0, 80.0)
			translate_instances.location = (500.0, 80.0)
			group_output.location = (660.0, 80.0)
			
			#Set dimensions
			compare.width, compare.height = 140.0, 100.0
			bounding_box.width, bounding_box.height = 140.0, 100.0
			separate_geometry.width, separate_geometry.height = 140.0, 100.0
			mix.width, mix.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			vector_math_001.width, vector_math_001.height = 140.0, 100.0
			transform_geometry.width, transform_geometry.height = 140.0, 100.0
			geometry_to_instance.width, geometry_to_instance.height = 160.0, 100.0
			translate_instances.width, translate_instances.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			
			#initialize _mn_utils_split_instance links
			#compare.Result -> separate_geometry.Selection
			_mn_utils_split_instance.links.new(compare.outputs[0], separate_geometry.inputs[1])
			#group_input.Geometry -> separate_geometry.Geometry
			_mn_utils_split_instance.links.new(group_input.outputs[0], separate_geometry.inputs[0])
			#group_input.Field -> compare.A
			_mn_utils_split_instance.links.new(group_input.outputs[1], compare.inputs[2])
			#separate_geometry.Selection -> bounding_box.Geometry
			_mn_utils_split_instance.links.new(separate_geometry.outputs[0], bounding_box.inputs[0])
			#bounding_box.Min -> mix.A
			_mn_utils_split_instance.links.new(bounding_box.outputs[1], mix.inputs[4])
			#bounding_box.Max -> mix.B
			_mn_utils_split_instance.links.new(bounding_box.outputs[2], mix.inputs[5])
			#separate_geometry.Selection -> transform_geometry.Geometry
			_mn_utils_split_instance.links.new(separate_geometry.outputs[0], transform_geometry.inputs[0])
			#vector_math_001.Vector -> vector_math.Vector
			_mn_utils_split_instance.links.new(vector_math_001.outputs[0], vector_math.inputs[0])
			#vector_math.Vector -> transform_geometry.Translation
			_mn_utils_split_instance.links.new(vector_math.outputs[0], transform_geometry.inputs[1])
			#transform_geometry.Geometry -> geometry_to_instance.Geometry
			_mn_utils_split_instance.links.new(transform_geometry.outputs[0], geometry_to_instance.inputs[0])
			#geometry_to_instance.Instances -> translate_instances.Instances
			_mn_utils_split_instance.links.new(geometry_to_instance.outputs[0], translate_instances.inputs[0])
			#translate_instances.Instances -> group_output.Instance
			_mn_utils_split_instance.links.new(translate_instances.outputs[0], group_output.inputs[0])
			#mix.Result -> vector_math_001.Vector
			_mn_utils_split_instance.links.new(mix.outputs[1], vector_math_001.inputs[0])
			#group_input.Group ID -> compare.B
			_mn_utils_split_instance.links.new(group_input.outputs[2], compare.inputs[3])
			#group_input.Origin Offset -> vector_math_001.Vector
			_mn_utils_split_instance.links.new(group_input.outputs[3], vector_math_001.inputs[1])
			#vector_math_001.Vector -> translate_instances.Translation
			_mn_utils_split_instance.links.new(vector_math_001.outputs[0], translate_instances.inputs[2])
			return _mn_utils_split_instance

		_mn_utils_split_instance = _mn_utils_split_instance_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".MN_utils_split_instance", type = 'NODES')
		mod.node_group = _mn_utils_split_instance
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_MN_utils_split_instance.bl_idname)
			
def register():
	bpy.utils.register_class(_MN_utils_split_instance)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_MN_utils_split_instance)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
