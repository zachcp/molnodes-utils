bl_info = {
	"name" : ".SampleAtomValue",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _SampleAtomValue(bpy.types.Operator):
	bl_idname = "node._sampleatomvalue"
	bl_label = ".SampleAtomValue"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _sampleatomvalue node group
		def _sampleatomvalue_node_group():
			_sampleatomvalue = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".SampleAtomValue")

			_sampleatomvalue.color_tag = 'NONE'
			_sampleatomvalue.description = ""

			_sampleatomvalue.is_modifier = True
			
			#_sampleatomvalue interface
			#Socket Atoms
			atoms_socket = _sampleatomvalue.interface.new_socket(name = "Atoms", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket = _sampleatomvalue.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			value_socket.subtype = 'NONE'
			value_socket.default_value = (0.0, 0.0, 0.0)
			value_socket.min_value = -3.4028234663852886e+38
			value_socket.max_value = 3.4028234663852886e+38
			value_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket_1 = _sampleatomvalue.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketColor')
			value_socket_1.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket = _sampleatomvalue.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket.attribute_domain = 'POINT'
			
			#Socket B
			b_socket = _sampleatomvalue.interface.new_socket(name = "B", in_out='INPUT', socket_type = 'NodeSocketInt')
			b_socket.subtype = 'NONE'
			b_socket.default_value = 57
			b_socket.min_value = -2147483648
			b_socket.max_value = 2147483647
			b_socket.attribute_domain = 'POINT'
			
			
			#initialize _sampleatomvalue nodes
			#node Group Output
			group_output = _sampleatomvalue.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Named Attribute.009
			named_attribute_009 = _sampleatomvalue.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_009.name = "Named Attribute.009"
			named_attribute_009.data_type = 'INT'
			#Name
			named_attribute_009.inputs[0].default_value = "atom_name"
			
			#node Index.005
			index_005 = _sampleatomvalue.nodes.new("GeometryNodeInputIndex")
			index_005.name = "Index.005"
			
			#node Position.002
			position_002 = _sampleatomvalue.nodes.new("GeometryNodeInputPosition")
			position_002.name = "Position.002"
			
			#node Compare.003
			compare_003 = _sampleatomvalue.nodes.new("FunctionNodeCompare")
			compare_003.name = "Compare.003"
			compare_003.data_type = 'INT'
			compare_003.mode = 'ELEMENT'
			compare_003.operation = 'EQUAL'
			
			#node Group Input
			group_input = _sampleatomvalue.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Sample Index.009
			sample_index_009 = _sampleatomvalue.nodes.new("GeometryNodeSampleIndex")
			sample_index_009.name = "Sample Index.009"
			sample_index_009.clamp = False
			sample_index_009.data_type = 'FLOAT_VECTOR'
			sample_index_009.domain = 'POINT'
			
			#node Named Attribute
			named_attribute = _sampleatomvalue.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute.inputs[0].default_value = "Color"
			
			#node Sample Index.010
			sample_index_010 = _sampleatomvalue.nodes.new("GeometryNodeSampleIndex")
			sample_index_010.name = "Sample Index.010"
			sample_index_010.clamp = False
			sample_index_010.data_type = 'FLOAT_COLOR'
			sample_index_010.domain = 'POINT'
			
			#node Separate Geometry.002
			separate_geometry_002 = _sampleatomvalue.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_002.name = "Separate Geometry.002"
			separate_geometry_002.domain = 'POINT'
			
			
			
			
			#Set locations
			group_output.location = (390.0, 0.0)
			named_attribute_009.location = (-200.0, -107.52880859375)
			index_005.location = (40.0, -47.52880859375)
			position_002.location = (40.0, 12.47119140625)
			compare_003.location = (40.2109375, -112.47119140625)
			group_input.location = (-170.3642578125, -265.140380859375)
			sample_index_009.location = (200.0, 112.47119140625)
			named_attribute.location = (40.0, -380.0)
			sample_index_010.location = (200.0, -280.0)
			separate_geometry_002.location = (200.0, -107.52880859375)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			named_attribute_009.width, named_attribute_009.height = 206.99917602539062, 100.0
			index_005.width, index_005.height = 140.0, 100.0
			position_002.width, position_002.height = 140.0, 100.0
			compare_003.width, compare_003.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			sample_index_009.width, sample_index_009.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			sample_index_010.width, sample_index_010.height = 140.0, 100.0
			separate_geometry_002.width, separate_geometry_002.height = 140.0, 100.0
			
			#initialize _sampleatomvalue links
			#index_005.Index -> sample_index_009.Index
			_sampleatomvalue.links.new(index_005.outputs[0], sample_index_009.inputs[2])
			#compare_003.Result -> separate_geometry_002.Selection
			_sampleatomvalue.links.new(compare_003.outputs[0], separate_geometry_002.inputs[1])
			#named_attribute_009.Attribute -> compare_003.A
			_sampleatomvalue.links.new(named_attribute_009.outputs[0], compare_003.inputs[2])
			#separate_geometry_002.Selection -> sample_index_009.Geometry
			_sampleatomvalue.links.new(separate_geometry_002.outputs[0], sample_index_009.inputs[0])
			#position_002.Position -> sample_index_009.Value
			_sampleatomvalue.links.new(position_002.outputs[0], sample_index_009.inputs[1])
			#group_input.Geometry -> separate_geometry_002.Geometry
			_sampleatomvalue.links.new(group_input.outputs[0], separate_geometry_002.inputs[0])
			#group_input.B -> compare_003.B
			_sampleatomvalue.links.new(group_input.outputs[1], compare_003.inputs[3])
			#sample_index_009.Value -> group_output.Value
			_sampleatomvalue.links.new(sample_index_009.outputs[0], group_output.inputs[1])
			#index_005.Index -> sample_index_010.Index
			_sampleatomvalue.links.new(index_005.outputs[0], sample_index_010.inputs[2])
			#separate_geometry_002.Selection -> sample_index_010.Geometry
			_sampleatomvalue.links.new(separate_geometry_002.outputs[0], sample_index_010.inputs[0])
			#named_attribute.Attribute -> sample_index_010.Value
			_sampleatomvalue.links.new(named_attribute.outputs[0], sample_index_010.inputs[1])
			#sample_index_010.Value -> group_output.Value
			_sampleatomvalue.links.new(sample_index_010.outputs[0], group_output.inputs[2])
			#separate_geometry_002.Selection -> group_output.Atoms
			_sampleatomvalue.links.new(separate_geometry_002.outputs[0], group_output.inputs[0])
			return _sampleatomvalue

		_sampleatomvalue = _sampleatomvalue_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".SampleAtomValue", type = 'NODES')
		mod.node_group = _sampleatomvalue
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_SampleAtomValue.bl_idname)
			
def register():
	bpy.utils.register_class(_SampleAtomValue)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_SampleAtomValue)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
