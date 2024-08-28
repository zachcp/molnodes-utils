bl_info = {
	"name" : "Sample Nearest Atoms",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Sample_Nearest_Atoms(bpy.types.Operator):
	bl_idname = "node.sample_nearest_atoms"
	bl_label = "Sample Nearest Atoms"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize sample_nearest_atoms node group
		def sample_nearest_atoms_node_group():
			sample_nearest_atoms = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Sample Nearest Atoms")

			sample_nearest_atoms.color_tag = 'GEOMETRY'
			sample_nearest_atoms.description = ""

			
			#sample_nearest_atoms interface
			#Socket Color
			color_socket = sample_nearest_atoms.interface.new_socket(name = "Color", in_out='OUTPUT', socket_type = 'NodeSocketColor')
			color_socket.default_value = (0.0, 0.0, 0.0, 0.0)
			color_socket.attribute_domain = 'POINT'
			
			#Socket b_factor
			b_factor_socket = sample_nearest_atoms.interface.new_socket(name = "b_factor", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			b_factor_socket.default_value = 0.0
			b_factor_socket.min_value = -3.4028234663852886e+38
			b_factor_socket.max_value = 3.4028234663852886e+38
			b_factor_socket.subtype = 'NONE'
			b_factor_socket.attribute_domain = 'POINT'
			
			#Socket atomic_number
			atomic_number_socket = sample_nearest_atoms.interface.new_socket(name = "atomic_number", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			atomic_number_socket.default_value = 0
			atomic_number_socket.min_value = -2147483648
			atomic_number_socket.max_value = 2147483647
			atomic_number_socket.subtype = 'NONE'
			atomic_number_socket.attribute_domain = 'POINT'
			
			#Socket chain_number
			chain_number_socket = sample_nearest_atoms.interface.new_socket(name = "chain_number", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			chain_number_socket.default_value = 0
			chain_number_socket.min_value = -2147483648
			chain_number_socket.max_value = 2147483647
			chain_number_socket.subtype = 'NONE'
			chain_number_socket.attribute_domain = 'POINT'
			
			#Socket res_id
			res_id_socket = sample_nearest_atoms.interface.new_socket(name = "res_id", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			res_id_socket.default_value = 0
			res_id_socket.min_value = -2147483648
			res_id_socket.max_value = 2147483647
			res_id_socket.subtype = 'NONE'
			res_id_socket.attribute_domain = 'POINT'
			
			#Socket res_name
			res_name_socket = sample_nearest_atoms.interface.new_socket(name = "res_name", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			res_name_socket.default_value = 0
			res_name_socket.min_value = -2147483648
			res_name_socket.max_value = 2147483647
			res_name_socket.subtype = 'NONE'
			res_name_socket.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket = sample_nearest_atoms.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket.attribute_domain = 'POINT'
			atoms_socket.description = "Atomic geometry that contains vertices and edges"
			
			
			#initialize sample_nearest_atoms nodes
			#node Group Output
			group_output = sample_nearest_atoms.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Sample Index.001
			sample_index_001 = sample_nearest_atoms.nodes.new("GeometryNodeSampleIndex")
			sample_index_001.name = "Sample Index.001"
			sample_index_001.clamp = False
			sample_index_001.data_type = 'INT'
			sample_index_001.domain = 'POINT'
			
			#node Sample Index.002
			sample_index_002 = sample_nearest_atoms.nodes.new("GeometryNodeSampleIndex")
			sample_index_002.name = "Sample Index.002"
			sample_index_002.clamp = False
			sample_index_002.data_type = 'INT'
			sample_index_002.domain = 'POINT'
			
			#node Sample Index.003
			sample_index_003 = sample_nearest_atoms.nodes.new("GeometryNodeSampleIndex")
			sample_index_003.name = "Sample Index.003"
			sample_index_003.clamp = False
			sample_index_003.data_type = 'INT'
			sample_index_003.domain = 'POINT'
			
			#node Sample Index.004
			sample_index_004 = sample_nearest_atoms.nodes.new("GeometryNodeSampleIndex")
			sample_index_004.name = "Sample Index.004"
			sample_index_004.clamp = False
			sample_index_004.data_type = 'INT'
			sample_index_004.domain = 'POINT'
			
			#node Sample Index.005
			sample_index_005 = sample_nearest_atoms.nodes.new("GeometryNodeSampleIndex")
			sample_index_005.name = "Sample Index.005"
			sample_index_005.clamp = False
			sample_index_005.data_type = 'FLOAT_COLOR'
			sample_index_005.domain = 'POINT'
			
			#node Sample Index
			sample_index = sample_nearest_atoms.nodes.new("GeometryNodeSampleIndex")
			sample_index.name = "Sample Index"
			sample_index.clamp = False
			sample_index.data_type = 'FLOAT'
			sample_index.domain = 'POINT'
			
			#node Group Input
			group_input = sample_nearest_atoms.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Sample Nearest
			sample_nearest = sample_nearest_atoms.nodes.new("GeometryNodeSampleNearest")
			sample_nearest.name = "Sample Nearest"
			sample_nearest.domain = 'POINT'
			#Sample Position
			sample_nearest.inputs[1].default_value = (0.0, 0.0, 0.0)
			
			#node Named Attribute.002
			named_attribute_002 = sample_nearest_atoms.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002.name = "Named Attribute.002"
			named_attribute_002.data_type = 'INT'
			#Name
			named_attribute_002.inputs[0].default_value = "chain_number"
			
			#node Named Attribute.003
			named_attribute_003 = sample_nearest_atoms.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_003.name = "Named Attribute.003"
			named_attribute_003.data_type = 'INT'
			#Name
			named_attribute_003.inputs[0].default_value = "res_id"
			
			#node Named Attribute.004
			named_attribute_004 = sample_nearest_atoms.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_004.name = "Named Attribute.004"
			named_attribute_004.data_type = 'INT'
			#Name
			named_attribute_004.inputs[0].default_value = "res_name"
			
			#node Named Attribute.001
			named_attribute_001 = sample_nearest_atoms.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.data_type = 'INT'
			#Name
			named_attribute_001.inputs[0].default_value = "atomic_number"
			
			#node Named Attribute
			named_attribute = sample_nearest_atoms.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'FLOAT'
			#Name
			named_attribute.inputs[0].default_value = "b_factor"
			
			#node Named Attribute.005
			named_attribute_005 = sample_nearest_atoms.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_005.name = "Named Attribute.005"
			named_attribute_005.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute_005.inputs[0].default_value = "Color"
			
			
			
			
			#Set locations
			group_output.location = (518.507568359375, 77.42973327636719)
			sample_index_001.location = (120.0, -100.0)
			sample_index_002.location = (120.0, -320.0)
			sample_index_003.location = (120.0, -540.0)
			sample_index_004.location = (120.0, -760.0)
			sample_index_005.location = (120.0, 320.0)
			sample_index.location = (118.25213623046875, 111.74752807617188)
			group_input.location = (-622.2442626953125, 8.679118156433105)
			sample_nearest.location = (-620.0, -80.0)
			named_attribute_002.location = (-60.0, -380.0)
			named_attribute_003.location = (-60.0, -600.0)
			named_attribute_004.location = (-60.0, -820.0)
			named_attribute_001.location = (-60.0, -160.0)
			named_attribute.location = (-60.0, 40.0)
			named_attribute_005.location = (-60.0, 260.0)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			sample_index_001.width, sample_index_001.height = 140.0, 100.0
			sample_index_002.width, sample_index_002.height = 140.0, 100.0
			sample_index_003.width, sample_index_003.height = 140.0, 100.0
			sample_index_004.width, sample_index_004.height = 140.0, 100.0
			sample_index_005.width, sample_index_005.height = 140.0, 100.0
			sample_index.width, sample_index.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			sample_nearest.width, sample_nearest.height = 140.0, 100.0
			named_attribute_002.width, named_attribute_002.height = 140.0, 100.0
			named_attribute_003.width, named_attribute_003.height = 140.0, 100.0
			named_attribute_004.width, named_attribute_004.height = 140.0, 100.0
			named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			named_attribute_005.width, named_attribute_005.height = 140.0, 100.0
			
			#initialize sample_nearest_atoms links
			#sample_nearest.Index -> sample_index.Index
			sample_nearest_atoms.links.new(sample_nearest.outputs[0], sample_index.inputs[2])
			#group_input.Atoms -> sample_index.Geometry
			sample_nearest_atoms.links.new(group_input.outputs[0], sample_index.inputs[0])
			#group_input.Atoms -> sample_nearest.Geometry
			sample_nearest_atoms.links.new(group_input.outputs[0], sample_nearest.inputs[0])
			#sample_nearest.Index -> sample_index_001.Index
			sample_nearest_atoms.links.new(sample_nearest.outputs[0], sample_index_001.inputs[2])
			#group_input.Atoms -> sample_index_001.Geometry
			sample_nearest_atoms.links.new(group_input.outputs[0], sample_index_001.inputs[0])
			#named_attribute_001.Attribute -> sample_index_001.Value
			sample_nearest_atoms.links.new(named_attribute_001.outputs[0], sample_index_001.inputs[1])
			#sample_index_001.Value -> group_output.atomic_number
			sample_nearest_atoms.links.new(sample_index_001.outputs[0], group_output.inputs[2])
			#sample_nearest.Index -> sample_index_002.Index
			sample_nearest_atoms.links.new(sample_nearest.outputs[0], sample_index_002.inputs[2])
			#group_input.Atoms -> sample_index_002.Geometry
			sample_nearest_atoms.links.new(group_input.outputs[0], sample_index_002.inputs[0])
			#named_attribute_002.Attribute -> sample_index_002.Value
			sample_nearest_atoms.links.new(named_attribute_002.outputs[0], sample_index_002.inputs[1])
			#sample_index_002.Value -> group_output.chain_number
			sample_nearest_atoms.links.new(sample_index_002.outputs[0], group_output.inputs[3])
			#sample_nearest.Index -> sample_index_003.Index
			sample_nearest_atoms.links.new(sample_nearest.outputs[0], sample_index_003.inputs[2])
			#group_input.Atoms -> sample_index_003.Geometry
			sample_nearest_atoms.links.new(group_input.outputs[0], sample_index_003.inputs[0])
			#named_attribute_003.Attribute -> sample_index_003.Value
			sample_nearest_atoms.links.new(named_attribute_003.outputs[0], sample_index_003.inputs[1])
			#sample_index_003.Value -> group_output.res_id
			sample_nearest_atoms.links.new(sample_index_003.outputs[0], group_output.inputs[4])
			#sample_nearest.Index -> sample_index_004.Index
			sample_nearest_atoms.links.new(sample_nearest.outputs[0], sample_index_004.inputs[2])
			#group_input.Atoms -> sample_index_004.Geometry
			sample_nearest_atoms.links.new(group_input.outputs[0], sample_index_004.inputs[0])
			#named_attribute_004.Attribute -> sample_index_004.Value
			sample_nearest_atoms.links.new(named_attribute_004.outputs[0], sample_index_004.inputs[1])
			#sample_index_004.Value -> group_output.res_name
			sample_nearest_atoms.links.new(sample_index_004.outputs[0], group_output.inputs[5])
			#named_attribute_005.Attribute -> sample_index_005.Value
			sample_nearest_atoms.links.new(named_attribute_005.outputs[0], sample_index_005.inputs[1])
			#sample_nearest.Index -> sample_index_005.Index
			sample_nearest_atoms.links.new(sample_nearest.outputs[0], sample_index_005.inputs[2])
			#group_input.Atoms -> sample_index_005.Geometry
			sample_nearest_atoms.links.new(group_input.outputs[0], sample_index_005.inputs[0])
			#sample_index_005.Value -> group_output.Color
			sample_nearest_atoms.links.new(sample_index_005.outputs[0], group_output.inputs[0])
			#named_attribute.Attribute -> sample_index.Value
			sample_nearest_atoms.links.new(named_attribute.outputs[0], sample_index.inputs[1])
			#sample_index.Value -> group_output.b_factor
			sample_nearest_atoms.links.new(sample_index.outputs[0], group_output.inputs[1])
			return sample_nearest_atoms

		sample_nearest_atoms = sample_nearest_atoms_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Sample Nearest Atoms", type = 'NODES')
		mod.node_group = sample_nearest_atoms
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Sample_Nearest_Atoms.bl_idname)
			
def register():
	bpy.utils.register_class(Sample_Nearest_Atoms)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Sample_Nearest_Atoms)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
