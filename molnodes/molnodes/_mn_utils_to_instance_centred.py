bl_info = {
	"name" : ".MN_utils_to_instance_centred",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _MN_utils_to_instance_centred(bpy.types.Operator):
	bl_idname = "node._mn_utils_to_instance_centred"
	bl_label = ".MN_utils_to_instance_centred"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _mn_utils_to_instance_centred node group
		def _mn_utils_to_instance_centred_node_group():
			_mn_utils_to_instance_centred = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_utils_to_instance_centred")

			_mn_utils_to_instance_centred.color_tag = 'NONE'
			_mn_utils_to_instance_centred.description = ""

			
			#_mn_utils_to_instance_centred interface
			#Socket Geometry
			geometry_socket = _mn_utils_to_instance_centred.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket.attribute_domain = 'POINT'
			
			#Socket Input
			input_socket = _mn_utils_to_instance_centred.interface.new_socket(name = "Input", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			input_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_utils_to_instance_centred nodes
			#node Bounding Box
			bounding_box = _mn_utils_to_instance_centred.nodes.new("GeometryNodeBoundBox")
			bounding_box.name = "Bounding Box"
			
			#node Transform Geometry
			transform_geometry = _mn_utils_to_instance_centred.nodes.new("GeometryNodeTransform")
			transform_geometry.name = "Transform Geometry"
			transform_geometry.mode = 'COMPONENTS'
			#Rotation
			transform_geometry.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Scale
			transform_geometry.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Transform Geometry.001
			transform_geometry_001 = _mn_utils_to_instance_centred.nodes.new("GeometryNodeTransform")
			transform_geometry_001.name = "Transform Geometry.001"
			transform_geometry_001.mode = 'COMPONENTS'
			#Rotation
			transform_geometry_001.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Scale
			transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Vector Math
			vector_math = _mn_utils_to_instance_centred.nodes.new("ShaderNodeVectorMath")
			vector_math.label = "-x"
			vector_math.name = "Vector Math"
			vector_math.hide = True
			vector_math.operation = 'SCALE'
			#Scale
			vector_math.inputs[3].default_value = -1.0
			
			#node Mix
			mix = _mn_utils_to_instance_centred.nodes.new("ShaderNodeMix")
			mix.label = "lerp(a, b, 0.5)"
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
			group_input = _mn_utils_to_instance_centred.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Geometry to Instance
			geometry_to_instance = _mn_utils_to_instance_centred.nodes.new("GeometryNodeGeometryToInstance")
			geometry_to_instance.name = "Geometry to Instance"
			
			#node Group Output
			group_output = _mn_utils_to_instance_centred.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Reroute.001
			reroute_001 = _mn_utils_to_instance_centred.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			
			
			
			#Set locations
			bounding_box.location = (-338.7969970703125, -30.0)
			transform_geometry.location = (21.2030029296875, 90.0)
			transform_geometry_001.location = (361.2030029296875, 90.0)
			vector_math.location = (-178.7969970703125, -50.0)
			mix.location = (-178.7969970703125, -90.0)
			group_input.location = (-600.0, 100.0)
			geometry_to_instance.location = (181.2030029296875, 90.0)
			group_output.location = (560.0, 100.0)
			reroute_001.location = (-380.0, 40.0)
			
			#Set dimensions
			bounding_box.width, bounding_box.height = 140.0, 100.0
			transform_geometry.width, transform_geometry.height = 140.0, 100.0
			transform_geometry_001.width, transform_geometry_001.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			mix.width, mix.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			geometry_to_instance.width, geometry_to_instance.height = 160.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			
			#initialize _mn_utils_to_instance_centred links
			#reroute_001.Output -> transform_geometry.Geometry
			_mn_utils_to_instance_centred.links.new(reroute_001.outputs[0], transform_geometry.inputs[0])
			#reroute_001.Output -> bounding_box.Geometry
			_mn_utils_to_instance_centred.links.new(reroute_001.outputs[0], bounding_box.inputs[0])
			#transform_geometry.Geometry -> geometry_to_instance.Geometry
			_mn_utils_to_instance_centred.links.new(transform_geometry.outputs[0], geometry_to_instance.inputs[0])
			#mix.Result -> vector_math.Vector
			_mn_utils_to_instance_centred.links.new(mix.outputs[1], vector_math.inputs[0])
			#vector_math.Vector -> transform_geometry.Translation
			_mn_utils_to_instance_centred.links.new(vector_math.outputs[0], transform_geometry.inputs[1])
			#geometry_to_instance.Instances -> transform_geometry_001.Geometry
			_mn_utils_to_instance_centred.links.new(geometry_to_instance.outputs[0], transform_geometry_001.inputs[0])
			#bounding_box.Min -> mix.A
			_mn_utils_to_instance_centred.links.new(bounding_box.outputs[1], mix.inputs[4])
			#mix.Result -> transform_geometry_001.Translation
			_mn_utils_to_instance_centred.links.new(mix.outputs[1], transform_geometry_001.inputs[1])
			#bounding_box.Max -> mix.B
			_mn_utils_to_instance_centred.links.new(bounding_box.outputs[2], mix.inputs[5])
			#group_input.Input -> reroute_001.Input
			_mn_utils_to_instance_centred.links.new(group_input.outputs[0], reroute_001.inputs[0])
			#transform_geometry_001.Geometry -> group_output.Geometry
			_mn_utils_to_instance_centred.links.new(transform_geometry_001.outputs[0], group_output.inputs[0])
			return _mn_utils_to_instance_centred

		_mn_utils_to_instance_centred = _mn_utils_to_instance_centred_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".MN_utils_to_instance_centred", type = 'NODES')
		mod.node_group = _mn_utils_to_instance_centred
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_MN_utils_to_instance_centred.bl_idname)
			
def register():
	bpy.utils.register_class(_MN_utils_to_instance_centred)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_MN_utils_to_instance_centred)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
