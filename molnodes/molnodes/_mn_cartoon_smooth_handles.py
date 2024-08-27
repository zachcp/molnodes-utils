bl_info = {
	"name" : ".MN_cartoon_smooth_handles",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _MN_cartoon_smooth_handles(bpy.types.Operator):
	bl_idname = "node._mn_cartoon_smooth_handles"
	bl_label = ".MN_cartoon_smooth_handles"
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

		#initialize _mn_cartoon_smooth_handles node group
		def _mn_cartoon_smooth_handles_node_group():
			_mn_cartoon_smooth_handles = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_cartoon_smooth_handles")

			_mn_cartoon_smooth_handles.color_tag = 'NONE'
			_mn_cartoon_smooth_handles.description = ""

			
			#_mn_cartoon_smooth_handles interface
			#Socket Vector
			vector_socket = _mn_cartoon_smooth_handles.interface.new_socket(name = "Vector", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			vector_socket.default_value = (0.0, 0.0, 0.0)
			vector_socket.min_value = -3.4028234663852886e+38
			vector_socket.max_value = 3.4028234663852886e+38
			vector_socket.subtype = 'NONE'
			vector_socket.attribute_domain = 'POINT'
			
			#Socket Scale
			scale_socket = _mn_cartoon_smooth_handles.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
			scale_socket.default_value = 0.00800000037997961
			scale_socket.min_value = -10000.0
			scale_socket.max_value = 10000.0
			scale_socket.subtype = 'NONE'
			scale_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_cartoon_smooth_handles nodes
			#node Vector Math.005
			vector_math_005 = _mn_cartoon_smooth_handles.nodes.new("ShaderNodeVectorMath")
			vector_math_005.name = "Vector Math.005"
			vector_math_005.operation = 'NORMALIZE'
			
			#node Named Attribute.004
			named_attribute_004 = _mn_cartoon_smooth_handles.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_004.name = "Named Attribute.004"
			named_attribute_004.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_004.inputs[0].default_value = "guide_X"
			
			#node Vector Math.006
			vector_math_006 = _mn_cartoon_smooth_handles.nodes.new("ShaderNodeVectorMath")
			vector_math_006.name = "Vector Math.006"
			vector_math_006.operation = 'NORMALIZE'
			
			#node Named Attribute.003
			named_attribute_003 = _mn_cartoon_smooth_handles.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_003.name = "Named Attribute.003"
			named_attribute_003.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_003.inputs[0].default_value = "guide_Z"
			
			#node Vector Math.007
			vector_math_007 = _mn_cartoon_smooth_handles.nodes.new("ShaderNodeVectorMath")
			vector_math_007.name = "Vector Math.007"
			vector_math_007.operation = 'CROSS_PRODUCT'
			
			#node Vector Math.008
			vector_math_008 = _mn_cartoon_smooth_handles.nodes.new("ShaderNodeVectorMath")
			vector_math_008.name = "Vector Math.008"
			vector_math_008.operation = 'SCALE'
			
			#node Group Output
			group_output_2 = _mn_cartoon_smooth_handles.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Group
			group_1 = _mn_cartoon_smooth_handles.nodes.new("GeometryNodeGroup")
			group_1.name = "Group"
			group_1.node_tree = mn_units
			
			#node Group Input
			group_input_2 = _mn_cartoon_smooth_handles.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
			
			
			
			#Set locations
			vector_math_005.location = (-40.0, 120.0)
			named_attribute_004.location = (-200.0, 120.0)
			vector_math_006.location = (-40.0, -20.0)
			named_attribute_003.location = (-200.0, -20.0)
			vector_math_007.location = (120.0, 120.0)
			vector_math_008.location = (280.0, 120.0)
			group_output_2.location = (440.0, 120.0)
			group_1.location = (280.0, -20.0)
			group_input_2.location = (120.0, -20.0)
			
			#Set dimensions
			vector_math_005.width, vector_math_005.height = 140.0, 100.0
			named_attribute_004.width, named_attribute_004.height = 140.0, 100.0
			vector_math_006.width, vector_math_006.height = 140.0, 100.0
			named_attribute_003.width, named_attribute_003.height = 140.0, 100.0
			vector_math_007.width, vector_math_007.height = 140.0, 100.0
			vector_math_008.width, vector_math_008.height = 140.0, 100.0
			group_output_2.width, group_output_2.height = 140.0, 100.0
			group_1.width, group_1.height = 140.0, 100.0
			group_input_2.width, group_input_2.height = 140.0, 100.0
			
			#initialize _mn_cartoon_smooth_handles links
			#vector_math_007.Vector -> vector_math_008.Vector
			_mn_cartoon_smooth_handles.links.new(vector_math_007.outputs[0], vector_math_008.inputs[0])
			#named_attribute_004.Attribute -> vector_math_005.Vector
			_mn_cartoon_smooth_handles.links.new(named_attribute_004.outputs[0], vector_math_005.inputs[0])
			#vector_math_005.Vector -> vector_math_007.Vector
			_mn_cartoon_smooth_handles.links.new(vector_math_005.outputs[0], vector_math_007.inputs[0])
			#vector_math_006.Vector -> vector_math_007.Vector
			_mn_cartoon_smooth_handles.links.new(vector_math_006.outputs[0], vector_math_007.inputs[1])
			#named_attribute_003.Attribute -> vector_math_006.Vector
			_mn_cartoon_smooth_handles.links.new(named_attribute_003.outputs[0], vector_math_006.inputs[0])
			#vector_math_008.Vector -> group_output_2.Vector
			_mn_cartoon_smooth_handles.links.new(vector_math_008.outputs[0], group_output_2.inputs[0])
			#group_input_2.Scale -> group_1.Value
			_mn_cartoon_smooth_handles.links.new(group_input_2.outputs[0], group_1.inputs[0])
			#group_1.Angstrom -> vector_math_008.Scale
			_mn_cartoon_smooth_handles.links.new(group_1.outputs[0], vector_math_008.inputs[3])
			return _mn_cartoon_smooth_handles

		_mn_cartoon_smooth_handles = _mn_cartoon_smooth_handles_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".MN_cartoon_smooth_handles", type = 'NODES')
		mod.node_group = _mn_cartoon_smooth_handles
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_MN_cartoon_smooth_handles.bl_idname)
			
def register():
	bpy.utils.register_class(_MN_cartoon_smooth_handles)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_MN_cartoon_smooth_handles)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
