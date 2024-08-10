bl_info = {
	"name" : ".MN_assembly_instance_chains",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _MN_assembly_instance_chains(bpy.types.Operator):
	bl_idname = "node._mn_assembly_instance_chains"
	bl_label = ".MN_assembly_instance_chains"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _mn_assembly_instance_chains node group
		def _mn_assembly_instance_chains_node_group():
			_mn_assembly_instance_chains = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_assembly_instance_chains")

			_mn_assembly_instance_chains.color_tag = 'NONE'
			_mn_assembly_instance_chains.description = ""

			_mn_assembly_instance_chains.is_modifier = True
			
			#_mn_assembly_instance_chains interface
			#Socket Assembled Chain Instances
			assembled_chain_instances_socket = _mn_assembly_instance_chains.interface.new_socket(name = "Assembled Chain Instances", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			assembled_chain_instances_socket.attribute_domain = 'POINT'
			
			#Socket Chain Instances
			chain_instances_socket = _mn_assembly_instance_chains.interface.new_socket(name = "Chain Instances", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			chain_instances_socket.attribute_domain = 'POINT'
			
			#Socket Rotation
			rotation_socket = _mn_assembly_instance_chains.interface.new_socket(name = "Rotation", in_out='INPUT', socket_type = 'NodeSocketFloat')
			rotation_socket.subtype = 'FACTOR'
			rotation_socket.default_value = 1.0
			rotation_socket.min_value = 0.0
			rotation_socket.max_value = 1.0
			rotation_socket.attribute_domain = 'POINT'
			
			#Socket Translation
			translation_socket = _mn_assembly_instance_chains.interface.new_socket(name = "Translation", in_out='INPUT', socket_type = 'NodeSocketFloat')
			translation_socket.subtype = 'FACTOR'
			translation_socket.default_value = 1.0
			translation_socket.min_value = 0.0
			translation_socket.max_value = 1.0
			translation_socket.attribute_domain = 'POINT'
			
			#Socket assembly_id
			assembly_id_socket = _mn_assembly_instance_chains.interface.new_socket(name = "assembly_id", in_out='INPUT', socket_type = 'NodeSocketInt')
			assembly_id_socket.subtype = 'NONE'
			assembly_id_socket.default_value = 0
			assembly_id_socket.min_value = -2147483648
			assembly_id_socket.max_value = 2147483647
			assembly_id_socket.attribute_domain = 'POINT'
			
			#Socket data_object
			data_object_socket = _mn_assembly_instance_chains.interface.new_socket(name = "data_object", in_out='INPUT', socket_type = 'NodeSocketObject')
			data_object_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_assembly_instance_chains nodes
			#node Mix
			mix = _mn_assembly_instance_chains.nodes.new("ShaderNodeMix")
			mix.name = "Mix"
			mix.blend_type = 'MIX'
			mix.clamp_factor = True
			mix.clamp_result = False
			mix.data_type = 'VECTOR'
			mix.factor_mode = 'UNIFORM'
			#A_Vector
			mix.inputs[4].default_value = (0.0, 0.0, 0.0)
			
			#node Position
			position = _mn_assembly_instance_chains.nodes.new("GeometryNodeInputPosition")
			position.name = "Position"
			
			#node Named Attribute
			named_attribute = _mn_assembly_instance_chains.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'INT'
			#Name
			named_attribute.inputs[0].default_value = "chain_id"
			
			#node Instance on Points
			instance_on_points = _mn_assembly_instance_chains.nodes.new("GeometryNodeInstanceOnPoints")
			instance_on_points.name = "Instance on Points"
			#Selection
			instance_on_points.inputs[1].default_value = True
			#Pick Instance
			instance_on_points.inputs[3].default_value = True
			#Scale
			instance_on_points.inputs[6].default_value = (1.0, 1.0, 1.0)
			
			#node Group Output
			group_output = _mn_assembly_instance_chains.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Set Position
			set_position = _mn_assembly_instance_chains.nodes.new("GeometryNodeSetPosition")
			set_position.name = "Set Position"
			#Selection
			set_position.inputs[1].default_value = True
			#Offset
			set_position.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Separate Geometry
			separate_geometry = _mn_assembly_instance_chains.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry.name = "Separate Geometry"
			separate_geometry.domain = 'POINT'
			
			#node Compare
			compare = _mn_assembly_instance_chains.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'EQUAL'
			
			#node Group Input
			group_input = _mn_assembly_instance_chains.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Named Attribute.002
			named_attribute_002 = _mn_assembly_instance_chains.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002.name = "Named Attribute.002"
			named_attribute_002.data_type = 'INT'
			#Name
			named_attribute_002.inputs[0].default_value = "assembly_id"
			
			#node Object Info
			object_info = _mn_assembly_instance_chains.nodes.new("GeometryNodeObjectInfo")
			object_info.name = "Object Info"
			object_info.transform_space = 'ORIGINAL'
			#As Instance
			object_info.inputs[1].default_value = False
			
			#node Named Attribute.001
			named_attribute_001 = _mn_assembly_instance_chains.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.data_type = 'QUATERNION'
			#Name
			named_attribute_001.inputs[0].default_value = "rotation"
			
			#node Group Input.001
			group_input_001 = _mn_assembly_instance_chains.nodes.new("NodeGroupInput")
			group_input_001.name = "Group Input.001"
			group_input_001.outputs[0].hide = True
			group_input_001.outputs[2].hide = True
			group_input_001.outputs[3].hide = True
			group_input_001.outputs[4].hide = True
			group_input_001.outputs[5].hide = True
			
			#node Domain Size
			domain_size = _mn_assembly_instance_chains.nodes.new("GeometryNodeAttributeDomainSize")
			domain_size.name = "Domain Size"
			domain_size.component = 'INSTANCES'
			
			#node Compare.001
			compare_001 = _mn_assembly_instance_chains.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'INT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'LESS_THAN'
			
			#node Named Attribute.003
			named_attribute_003 = _mn_assembly_instance_chains.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_003.name = "Named Attribute.003"
			named_attribute_003.data_type = 'INT'
			#Name
			named_attribute_003.inputs[0].default_value = "chain_id"
			
			#node Boolean Math
			boolean_math = _mn_assembly_instance_chains.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'AND'
			
			#node Mix.001
			mix_001 = _mn_assembly_instance_chains.nodes.new("ShaderNodeMix")
			mix_001.name = "Mix.001"
			mix_001.blend_type = 'MIX'
			mix_001.clamp_factor = True
			mix_001.clamp_result = False
			mix_001.data_type = 'ROTATION'
			mix_001.factor_mode = 'UNIFORM'
			#A_Rotation
			mix_001.inputs[8].default_value = (0.0, 0.0, 0.0)
			
			
			
			
			#Set locations
			mix.location = (-520.0, -20.0)
			position.location = (-680.0, -220.0)
			named_attribute.location = (-341.5813903808594, -60.27907180786133)
			instance_on_points.location = (-140.6511688232422, 241.1162872314453)
			group_output.location = (40.1860466003418, 241.1162872314453)
			set_position.location = (-341.5813903808594, 160.7441864013672)
			separate_geometry.location = (-521.641357421875, 137.05740356445312)
			compare.location = (-960.0, -220.0)
			group_input.location = (-1220.0, 220.0)
			named_attribute_002.location = (-1160.0, -340.0)
			object_info.location = (-800.0, 160.0)
			named_attribute_001.location = (-340.0, -260.0)
			group_input_001.location = (-340.0, -200.0)
			domain_size.location = (-1160.0, -80.0)
			compare_001.location = (-960.0, -60.0)
			named_attribute_003.location = (-1160.0, -200.0)
			boolean_math.location = (-800.0, -60.0)
			mix_001.location = (-180.0, -160.0)
			
			#Set dimensions
			mix.width, mix.height = 140.0, 100.0
			position.width, position.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			instance_on_points.width, instance_on_points.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			set_position.width, set_position.height = 140.0, 100.0
			separate_geometry.width, separate_geometry.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			named_attribute_002.width, named_attribute_002.height = 140.0, 100.0
			object_info.width, object_info.height = 140.0, 100.0
			named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
			group_input_001.width, group_input_001.height = 140.0, 100.0
			domain_size.width, domain_size.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			named_attribute_003.width, named_attribute_003.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			mix_001.width, mix_001.height = 140.0, 100.0
			
			#initialize _mn_assembly_instance_chains links
			#named_attribute.Attribute -> instance_on_points.Instance Index
			_mn_assembly_instance_chains.links.new(named_attribute.outputs[0], instance_on_points.inputs[4])
			#group_input.Chain Instances -> instance_on_points.Instance
			_mn_assembly_instance_chains.links.new(group_input.outputs[0], instance_on_points.inputs[2])
			#instance_on_points.Instances -> group_output.Assembled Chain Instances
			_mn_assembly_instance_chains.links.new(instance_on_points.outputs[0], group_output.inputs[0])
			#mix.Result -> set_position.Position
			_mn_assembly_instance_chains.links.new(mix.outputs[1], set_position.inputs[2])
			#position.Position -> mix.B
			_mn_assembly_instance_chains.links.new(position.outputs[0], mix.inputs[5])
			#group_input.Translation -> mix.Factor
			_mn_assembly_instance_chains.links.new(group_input.outputs[2], mix.inputs[0])
			#set_position.Geometry -> instance_on_points.Points
			_mn_assembly_instance_chains.links.new(set_position.outputs[0], instance_on_points.inputs[0])
			#object_info.Geometry -> separate_geometry.Geometry
			_mn_assembly_instance_chains.links.new(object_info.outputs[4], separate_geometry.inputs[0])
			#separate_geometry.Selection -> set_position.Geometry
			_mn_assembly_instance_chains.links.new(separate_geometry.outputs[0], set_position.inputs[0])
			#group_input.assembly_id -> compare.A
			_mn_assembly_instance_chains.links.new(group_input.outputs[3], compare.inputs[2])
			#named_attribute_002.Attribute -> compare.B
			_mn_assembly_instance_chains.links.new(named_attribute_002.outputs[0], compare.inputs[3])
			#group_input.data_object -> object_info.Object
			_mn_assembly_instance_chains.links.new(group_input.outputs[4], object_info.inputs[0])
			#group_input.Chain Instances -> domain_size.Geometry
			_mn_assembly_instance_chains.links.new(group_input.outputs[0], domain_size.inputs[0])
			#named_attribute_003.Attribute -> compare_001.A
			_mn_assembly_instance_chains.links.new(named_attribute_003.outputs[0], compare_001.inputs[2])
			#domain_size.Instance Count -> compare_001.B
			_mn_assembly_instance_chains.links.new(domain_size.outputs[5], compare_001.inputs[3])
			#compare_001.Result -> boolean_math.Boolean
			_mn_assembly_instance_chains.links.new(compare_001.outputs[0], boolean_math.inputs[0])
			#compare.Result -> boolean_math.Boolean
			_mn_assembly_instance_chains.links.new(compare.outputs[0], boolean_math.inputs[1])
			#boolean_math.Boolean -> separate_geometry.Selection
			_mn_assembly_instance_chains.links.new(boolean_math.outputs[0], separate_geometry.inputs[1])
			#named_attribute_001.Attribute -> mix_001.B
			_mn_assembly_instance_chains.links.new(named_attribute_001.outputs[0], mix_001.inputs[9])
			#group_input_001.Rotation -> mix_001.Factor
			_mn_assembly_instance_chains.links.new(group_input_001.outputs[1], mix_001.inputs[0])
			#mix_001.Result -> instance_on_points.Rotation
			_mn_assembly_instance_chains.links.new(mix_001.outputs[3], instance_on_points.inputs[5])
			return _mn_assembly_instance_chains

		_mn_assembly_instance_chains = _mn_assembly_instance_chains_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".MN_assembly_instance_chains", type = 'NODES')
		mod.node_group = _mn_assembly_instance_chains
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_MN_assembly_instance_chains.bl_idname)
			
def register():
	bpy.utils.register_class(_MN_assembly_instance_chains)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_MN_assembly_instance_chains)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
