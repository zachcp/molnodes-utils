bl_info = {
	"name" : "MN_utils_primitive_atom",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class MN_utils_primitive_atom(bpy.types.Operator):
	bl_idname = "node.mn_utils_primitive_atom"
	bl_label = "MN_utils_primitive_atom"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize mn_utils_primitive_atom node group
		def mn_utils_primitive_atom_node_group():
			mn_utils_primitive_atom = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "MN_utils_primitive_atom")

			mn_utils_primitive_atom.color_tag = 'NONE'
			mn_utils_primitive_atom.description = ""

			mn_utils_primitive_atom.is_modifier = True
			
			#mn_utils_primitive_atom interface
			#Socket Geometry
			geometry_socket = mn_utils_primitive_atom.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket.attribute_domain = 'POINT'
			
			#Socket Position
			position_socket = mn_utils_primitive_atom.interface.new_socket(name = "Position", in_out='INPUT', socket_type = 'NodeSocketVector')
			position_socket.default_value = (0.0, 0.0, 0.0)
			position_socket.min_value = -3.4028234663852886e+38
			position_socket.max_value = 3.4028234663852886e+38
			position_socket.subtype = 'NONE'
			position_socket.attribute_domain = 'POINT'
			
			#Socket vdw_radii
			vdw_radii_socket = mn_utils_primitive_atom.interface.new_socket(name = "vdw_radii", in_out='INPUT', socket_type = 'NodeSocketFloat')
			vdw_radii_socket.default_value = 0.10000000149011612
			vdw_radii_socket.min_value = 0.0
			vdw_radii_socket.max_value = 3.4028234663852886e+38
			vdw_radii_socket.subtype = 'DISTANCE'
			vdw_radii_socket.attribute_domain = 'POINT'
			
			#Socket b_factor
			b_factor_socket = mn_utils_primitive_atom.interface.new_socket(name = "b_factor", in_out='INPUT', socket_type = 'NodeSocketFloat')
			b_factor_socket.default_value = 0.0
			b_factor_socket.min_value = -3.4028234663852886e+38
			b_factor_socket.max_value = 3.4028234663852886e+38
			b_factor_socket.subtype = 'NONE'
			b_factor_socket.attribute_domain = 'POINT'
			
			#Socket atomic_number
			atomic_number_socket = mn_utils_primitive_atom.interface.new_socket(name = "atomic_number", in_out='INPUT', socket_type = 'NodeSocketInt')
			atomic_number_socket.default_value = 0
			atomic_number_socket.min_value = -2147483648
			atomic_number_socket.max_value = 2147483647
			atomic_number_socket.subtype = 'NONE'
			atomic_number_socket.attribute_domain = 'POINT'
			
			#Socket res_name
			res_name_socket = mn_utils_primitive_atom.interface.new_socket(name = "res_name", in_out='INPUT', socket_type = 'NodeSocketInt')
			res_name_socket.default_value = 0
			res_name_socket.min_value = -2147483648
			res_name_socket.max_value = 2147483647
			res_name_socket.subtype = 'NONE'
			res_name_socket.attribute_domain = 'POINT'
			
			#Socket res_id
			res_id_socket = mn_utils_primitive_atom.interface.new_socket(name = "res_id", in_out='INPUT', socket_type = 'NodeSocketInt')
			res_id_socket.default_value = 0
			res_id_socket.min_value = -2147483648
			res_id_socket.max_value = 2147483647
			res_id_socket.subtype = 'NONE'
			res_id_socket.attribute_domain = 'POINT'
			
			#Socket is_backbone
			is_backbone_socket = mn_utils_primitive_atom.interface.new_socket(name = "is_backbone", in_out='INPUT', socket_type = 'NodeSocketBool')
			is_backbone_socket.default_value = False
			is_backbone_socket.attribute_domain = 'POINT'
			
			#Socket is_peptide
			is_peptide_socket = mn_utils_primitive_atom.interface.new_socket(name = "is_peptide", in_out='INPUT', socket_type = 'NodeSocketBool')
			is_peptide_socket.default_value = False
			is_peptide_socket.attribute_domain = 'POINT'
			
			#Socket is_alpha_carbon
			is_alpha_carbon_socket = mn_utils_primitive_atom.interface.new_socket(name = "is_alpha_carbon", in_out='INPUT', socket_type = 'NodeSocketBool')
			is_alpha_carbon_socket.default_value = False
			is_alpha_carbon_socket.attribute_domain = 'POINT'
			
			#Socket is_nucleic
			is_nucleic_socket = mn_utils_primitive_atom.interface.new_socket(name = "is_nucleic", in_out='INPUT', socket_type = 'NodeSocketBool')
			is_nucleic_socket.default_value = False
			is_nucleic_socket.attribute_domain = 'POINT'
			
			
			#initialize mn_utils_primitive_atom nodes
			#node Points
			points = mn_utils_primitive_atom.nodes.new("GeometryNodePoints")
			points.name = "Points"
			#Count
			points.inputs[0].default_value = 1
			
			#node Store Named Attribute
			store_named_attribute = mn_utils_primitive_atom.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute.name = "Store Named Attribute"
			store_named_attribute.data_type = 'FLOAT'
			store_named_attribute.domain = 'POINT'
			#Selection
			store_named_attribute.inputs[1].default_value = True
			#Name
			store_named_attribute.inputs[2].default_value = "vdw_radii"
			
			#node Store Named Attribute.001
			store_named_attribute_001 = mn_utils_primitive_atom.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_001.name = "Store Named Attribute.001"
			store_named_attribute_001.data_type = 'FLOAT'
			store_named_attribute_001.domain = 'POINT'
			#Selection
			store_named_attribute_001.inputs[1].default_value = True
			#Name
			store_named_attribute_001.inputs[2].default_value = "b_factor"
			
			#node Store Named Attribute.002
			store_named_attribute_002 = mn_utils_primitive_atom.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_002.name = "Store Named Attribute.002"
			store_named_attribute_002.data_type = 'INT'
			store_named_attribute_002.domain = 'POINT'
			#Selection
			store_named_attribute_002.inputs[1].default_value = True
			#Name
			store_named_attribute_002.inputs[2].default_value = "atomic_number"
			
			#node Store Named Attribute.004
			store_named_attribute_004 = mn_utils_primitive_atom.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_004.name = "Store Named Attribute.004"
			store_named_attribute_004.data_type = 'INT'
			store_named_attribute_004.domain = 'POINT'
			#Selection
			store_named_attribute_004.inputs[1].default_value = True
			#Name
			store_named_attribute_004.inputs[2].default_value = "res_name"
			
			#node Store Named Attribute.005
			store_named_attribute_005 = mn_utils_primitive_atom.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_005.name = "Store Named Attribute.005"
			store_named_attribute_005.data_type = 'INT'
			store_named_attribute_005.domain = 'POINT'
			#Selection
			store_named_attribute_005.inputs[1].default_value = True
			#Name
			store_named_attribute_005.inputs[2].default_value = "res_id"
			
			#node Store Named Attribute.006
			store_named_attribute_006 = mn_utils_primitive_atom.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_006.name = "Store Named Attribute.006"
			store_named_attribute_006.data_type = 'BOOLEAN'
			store_named_attribute_006.domain = 'POINT'
			#Selection
			store_named_attribute_006.inputs[1].default_value = True
			#Name
			store_named_attribute_006.inputs[2].default_value = "is_backbone"
			
			#node Store Named Attribute.010
			store_named_attribute_010 = mn_utils_primitive_atom.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_010.name = "Store Named Attribute.010"
			store_named_attribute_010.data_type = 'BOOLEAN'
			store_named_attribute_010.domain = 'POINT'
			#Selection
			store_named_attribute_010.inputs[1].default_value = True
			#Name
			store_named_attribute_010.inputs[2].default_value = "is_peptide"
			
			#node Store Named Attribute.012
			store_named_attribute_012 = mn_utils_primitive_atom.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_012.name = "Store Named Attribute.012"
			store_named_attribute_012.data_type = 'BOOLEAN'
			store_named_attribute_012.domain = 'POINT'
			#Selection
			store_named_attribute_012.inputs[1].default_value = True
			#Name
			store_named_attribute_012.inputs[2].default_value = "is_alpha_carbon"
			
			#node Store Named Attribute.008
			store_named_attribute_008 = mn_utils_primitive_atom.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_008.name = "Store Named Attribute.008"
			store_named_attribute_008.data_type = 'BOOLEAN'
			store_named_attribute_008.domain = 'POINT'
			#Selection
			store_named_attribute_008.inputs[1].default_value = True
			#Name
			store_named_attribute_008.inputs[2].default_value = "is_nucleic"
			
			#node Group Output
			group_output = mn_utils_primitive_atom.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = mn_utils_primitive_atom.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			
			
			
			#Set locations
			points.location = (-80.0, 0.0)
			store_named_attribute.location = (90.0, 0.0)
			store_named_attribute_001.location = (260.0, 0.0)
			store_named_attribute_002.location = (420.0, 0.0)
			store_named_attribute_004.location = (580.0, 0.0)
			store_named_attribute_005.location = (740.0, 0.0)
			store_named_attribute_006.location = (900.0, 0.0)
			store_named_attribute_010.location = (1060.0, 0.0)
			store_named_attribute_012.location = (1220.0, 0.0)
			store_named_attribute_008.location = (1380.0, 0.0)
			group_output.location = (1560.0, 0.0)
			group_input.location = (-301.4026794433594, -162.99154663085938)
			
			#Set dimensions
			points.width, points.height = 140.0, 100.0
			store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
			store_named_attribute_001.width, store_named_attribute_001.height = 140.0, 100.0
			store_named_attribute_002.width, store_named_attribute_002.height = 140.0, 100.0
			store_named_attribute_004.width, store_named_attribute_004.height = 140.0, 100.0
			store_named_attribute_005.width, store_named_attribute_005.height = 140.0, 100.0
			store_named_attribute_006.width, store_named_attribute_006.height = 140.0, 100.0
			store_named_attribute_010.width, store_named_attribute_010.height = 140.0, 100.0
			store_named_attribute_012.width, store_named_attribute_012.height = 140.0, 100.0
			store_named_attribute_008.width, store_named_attribute_008.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			
			#initialize mn_utils_primitive_atom links
			#points.Points -> store_named_attribute.Geometry
			mn_utils_primitive_atom.links.new(points.outputs[0], store_named_attribute.inputs[0])
			#group_input.Position -> points.Position
			mn_utils_primitive_atom.links.new(group_input.outputs[0], points.inputs[1])
			#group_input.vdw_radii -> points.Radius
			mn_utils_primitive_atom.links.new(group_input.outputs[1], points.inputs[2])
			#group_input.vdw_radii -> store_named_attribute.Value
			mn_utils_primitive_atom.links.new(group_input.outputs[1], store_named_attribute.inputs[3])
			#store_named_attribute.Geometry -> store_named_attribute_001.Geometry
			mn_utils_primitive_atom.links.new(store_named_attribute.outputs[0], store_named_attribute_001.inputs[0])
			#group_input.b_factor -> store_named_attribute_001.Value
			mn_utils_primitive_atom.links.new(group_input.outputs[2], store_named_attribute_001.inputs[3])
			#store_named_attribute_001.Geometry -> store_named_attribute_002.Geometry
			mn_utils_primitive_atom.links.new(store_named_attribute_001.outputs[0], store_named_attribute_002.inputs[0])
			#store_named_attribute_002.Geometry -> store_named_attribute_004.Geometry
			mn_utils_primitive_atom.links.new(store_named_attribute_002.outputs[0], store_named_attribute_004.inputs[0])
			#store_named_attribute_004.Geometry -> store_named_attribute_005.Geometry
			mn_utils_primitive_atom.links.new(store_named_attribute_004.outputs[0], store_named_attribute_005.inputs[0])
			#store_named_attribute_005.Geometry -> store_named_attribute_006.Geometry
			mn_utils_primitive_atom.links.new(store_named_attribute_005.outputs[0], store_named_attribute_006.inputs[0])
			#store_named_attribute_008.Geometry -> group_output.Geometry
			mn_utils_primitive_atom.links.new(store_named_attribute_008.outputs[0], group_output.inputs[0])
			#store_named_attribute_012.Geometry -> store_named_attribute_008.Geometry
			mn_utils_primitive_atom.links.new(store_named_attribute_012.outputs[0], store_named_attribute_008.inputs[0])
			#store_named_attribute_006.Geometry -> store_named_attribute_010.Geometry
			mn_utils_primitive_atom.links.new(store_named_attribute_006.outputs[0], store_named_attribute_010.inputs[0])
			#store_named_attribute_010.Geometry -> store_named_attribute_012.Geometry
			mn_utils_primitive_atom.links.new(store_named_attribute_010.outputs[0], store_named_attribute_012.inputs[0])
			#group_input.atomic_number -> store_named_attribute_002.Value
			mn_utils_primitive_atom.links.new(group_input.outputs[3], store_named_attribute_002.inputs[3])
			#group_input.res_name -> store_named_attribute_004.Value
			mn_utils_primitive_atom.links.new(group_input.outputs[4], store_named_attribute_004.inputs[3])
			#group_input.res_id -> store_named_attribute_005.Value
			mn_utils_primitive_atom.links.new(group_input.outputs[5], store_named_attribute_005.inputs[3])
			#group_input.is_backbone -> store_named_attribute_006.Value
			mn_utils_primitive_atom.links.new(group_input.outputs[6], store_named_attribute_006.inputs[3])
			#group_input.is_peptide -> store_named_attribute_010.Value
			mn_utils_primitive_atom.links.new(group_input.outputs[7], store_named_attribute_010.inputs[3])
			#group_input.is_alpha_carbon -> store_named_attribute_012.Value
			mn_utils_primitive_atom.links.new(group_input.outputs[8], store_named_attribute_012.inputs[3])
			#group_input.is_nucleic -> store_named_attribute_008.Value
			mn_utils_primitive_atom.links.new(group_input.outputs[9], store_named_attribute_008.inputs[3])
			return mn_utils_primitive_atom

		mn_utils_primitive_atom = mn_utils_primitive_atom_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "MN_utils_primitive_atom", type = 'NODES')
		mod.node_group = mn_utils_primitive_atom
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(MN_utils_primitive_atom.bl_idname)
			
def register():
	bpy.utils.register_class(MN_utils_primitive_atom)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(MN_utils_primitive_atom)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
