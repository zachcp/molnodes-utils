bl_info = {
	"name" : "MN_assembly_",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class MN_assembly_(bpy.types.Operator):
	bl_idname = "node.mn_assembly_"
	bl_label = "MN_assembly_"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize mn_assembly_ node group
		def mn_assembly__node_group():
			mn_assembly_ = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "MN_assembly_")

			mn_assembly_.color_tag = 'NONE'
			mn_assembly_.description = ""

			mn_assembly_.is_modifier = True
			
			#mn_assembly_ interface
			#Socket Assembled Chain Instances
			assembled_chain_instances_socket = mn_assembly_.interface.new_socket(name = "Assembled Chain Instances", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			assembled_chain_instances_socket.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket = mn_assembly_.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket.attribute_domain = 'POINT'
			geometry_socket.description = "Any geometry to separate into chains and instance"
			
			#Socket Rotation
			rotation_socket = mn_assembly_.interface.new_socket(name = "Rotation", in_out='INPUT', socket_type = 'NodeSocketFloat')
			rotation_socket.default_value = 1.0
			rotation_socket.min_value = 0.0
			rotation_socket.max_value = 1.0
			rotation_socket.subtype = 'FACTOR'
			rotation_socket.attribute_domain = 'POINT'
			rotation_socket.description = "Amount to apply the rotation of the matrix"
			
			#Socket Translation
			translation_socket = mn_assembly_.interface.new_socket(name = "Translation", in_out='INPUT', socket_type = 'NodeSocketFloat')
			translation_socket.default_value = 1.0
			translation_socket.min_value = 0.0
			translation_socket.max_value = 1.0
			translation_socket.subtype = 'FACTOR'
			translation_socket.attribute_domain = 'POINT'
			translation_socket.description = "Amount to apply the translation of the matrix"
			
			#Socket assembly_id
			assembly_id_socket = mn_assembly_.interface.new_socket(name = "assembly_id", in_out='INPUT', socket_type = 'NodeSocketInt')
			assembly_id_socket.default_value = 1
			assembly_id_socket.min_value = 1
			assembly_id_socket.max_value = 6
			assembly_id_socket.subtype = 'NONE'
			assembly_id_socket.attribute_domain = 'POINT'
			assembly_id_socket.description = "Which biological assembly to create"
			
			
			#initialize mn_assembly_ nodes
			#node Mix
			mix = mn_assembly_.nodes.new("ShaderNodeMix")
			mix.name = "Mix"
			mix.blend_type = 'MIX'
			mix.clamp_factor = True
			mix.clamp_result = False
			mix.data_type = 'VECTOR'
			mix.factor_mode = 'UNIFORM'
			#A_Vector
			mix.inputs[4].default_value = (0.0, 0.0, 0.0)
			
			#node Position
			position = mn_assembly_.nodes.new("GeometryNodeInputPosition")
			position.name = "Position"
			
			#node Named Attribute
			named_attribute = mn_assembly_.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'INT'
			#Name
			named_attribute.inputs[0].default_value = "chain_id"
			
			#node Named Attribute.001
			named_attribute_001 = mn_assembly_.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_001.inputs[0].default_value = "assembly_rotation"
			
			#node Instance on Points
			instance_on_points = mn_assembly_.nodes.new("GeometryNodeInstanceOnPoints")
			instance_on_points.name = "Instance on Points"
			#Selection
			instance_on_points.inputs[1].default_value = True
			#Pick Instance
			instance_on_points.inputs[3].default_value = True
			#Scale
			instance_on_points.inputs[6].default_value = (1.0, 1.0, 1.0)
			
			#node Vector Math
			vector_math = mn_assembly_.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.operation = 'SCALE'
			
			#node Group Input.001
			group_input_001 = mn_assembly_.nodes.new("NodeGroupInput")
			group_input_001.name = "Group Input.001"
			
			#node Group Output
			group_output = mn_assembly_.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Set Position
			set_position = mn_assembly_.nodes.new("GeometryNodeSetPosition")
			set_position.name = "Set Position"
			#Selection
			set_position.inputs[1].default_value = True
			#Offset
			set_position.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Separate Geometry
			separate_geometry = mn_assembly_.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry.name = "Separate Geometry"
			separate_geometry.domain = 'POINT'
			
			#node Compare
			compare = mn_assembly_.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'EQUAL'
			
			#node Group Input
			group_input = mn_assembly_.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Named Attribute.002
			named_attribute_002 = mn_assembly_.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002.name = "Named Attribute.002"
			named_attribute_002.data_type = 'INT'
			#Name
			named_attribute_002.inputs[0].default_value = "assembly_id"
			
			#node Object Info
			object_info = mn_assembly_.nodes.new("GeometryNodeObjectInfo")
			object_info.name = "Object Info"
			object_info.transform_space = 'ORIGINAL'
			#As Instance
			object_info.inputs[1].default_value = False
			
			
			
			
			#Set locations
			mix.location = (-522.4186401367188, -40.1860466003418)
			position.location = (-683.1627807617188, -221.02325439453125)
			named_attribute.location = (-341.5813903808594, -60.27907180786133)
			named_attribute_001.location = (-341.5813903808594, -200.93023681640625)
			instance_on_points.location = (-140.6511688232422, 241.1162872314453)
			vector_math.location = (-140.6511688232422, -60.27907180786133)
			group_input_001.location = (-140.6511688232422, -200.93023681640625)
			group_output.location = (40.1860466003418, 241.1162872314453)
			set_position.location = (-341.5813903808594, 160.7441864013672)
			separate_geometry.location = (-521.641357421875, 137.05740356445312)
			compare.location = (-743.44189453125, -40.1860466003418)
			group_input.location = (-1004.6511840820312, 261.2093200683594)
			named_attribute_002.location = (-924.2791137695312, -160.7441864013672)
			object_info.location = (-743.6431274414062, 169.9601287841797)
			
			#Set dimensions
			mix.width, mix.height = 140.0, 100.0
			position.width, position.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
			instance_on_points.width, instance_on_points.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			group_input_001.width, group_input_001.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			set_position.width, set_position.height = 140.0, 100.0
			separate_geometry.width, separate_geometry.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			named_attribute_002.width, named_attribute_002.height = 140.0, 100.0
			object_info.width, object_info.height = 140.0, 100.0
			
			#initialize mn_assembly_ links
			#vector_math.Vector -> instance_on_points.Rotation
			mn_assembly_.links.new(vector_math.outputs[0], instance_on_points.inputs[5])
			#named_attribute_001.Attribute -> vector_math.Vector
			mn_assembly_.links.new(named_attribute_001.outputs[0], vector_math.inputs[0])
			#named_attribute.Attribute -> instance_on_points.Instance Index
			mn_assembly_.links.new(named_attribute.outputs[0], instance_on_points.inputs[4])
			#group_input.Geometry -> instance_on_points.Instance
			mn_assembly_.links.new(group_input.outputs[0], instance_on_points.inputs[2])
			#instance_on_points.Instances -> group_output.Assembled Chain Instances
			mn_assembly_.links.new(instance_on_points.outputs[0], group_output.inputs[0])
			#mix.Result -> set_position.Position
			mn_assembly_.links.new(mix.outputs[1], set_position.inputs[2])
			#position.Position -> mix.B
			mn_assembly_.links.new(position.outputs[0], mix.inputs[5])
			#group_input.Translation -> mix.Factor
			mn_assembly_.links.new(group_input.outputs[2], mix.inputs[0])
			#group_input_001.Rotation -> vector_math.Scale
			mn_assembly_.links.new(group_input_001.outputs[1], vector_math.inputs[3])
			#set_position.Geometry -> instance_on_points.Points
			mn_assembly_.links.new(set_position.outputs[0], instance_on_points.inputs[0])
			#object_info.Geometry -> separate_geometry.Geometry
			mn_assembly_.links.new(object_info.outputs[4], separate_geometry.inputs[0])
			#separate_geometry.Selection -> set_position.Geometry
			mn_assembly_.links.new(separate_geometry.outputs[0], set_position.inputs[0])
			#compare.Result -> separate_geometry.Selection
			mn_assembly_.links.new(compare.outputs[0], separate_geometry.inputs[1])
			#group_input.assembly_id -> compare.A
			mn_assembly_.links.new(group_input.outputs[3], compare.inputs[2])
			#named_attribute_002.Attribute -> compare.B
			mn_assembly_.links.new(named_attribute_002.outputs[0], compare.inputs[3])
			return mn_assembly_

		mn_assembly_ = mn_assembly__node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "MN_assembly_", type = 'NODES')
		mod.node_group = mn_assembly_
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(MN_assembly_.bl_idname)
			
def register():
	bpy.utils.register_class(MN_assembly_)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(MN_assembly_)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
