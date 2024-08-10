bl_info = {
	"name" : ".MN_select_res_name_peptide",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _MN_select_res_name_peptide(bpy.types.Operator):
	bl_idname = "node._mn_select_res_name_peptide"
	bl_label = ".MN_select_res_name_peptide"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _mn_select_res_name_peptide node group
		def _mn_select_res_name_peptide_node_group():
			_mn_select_res_name_peptide = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_select_res_name_peptide")

			_mn_select_res_name_peptide.color_tag = 'NONE'
			_mn_select_res_name_peptide.description = ""

			
			#_mn_select_res_name_peptide interface
			#Socket Selection
			selection_socket = _mn_select_res_name_peptide.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket.attribute_domain = 'POINT'
			selection_socket.description = "The calculated selection"
			
			#Socket Inverted
			inverted_socket = _mn_select_res_name_peptide.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket.attribute_domain = 'POINT'
			inverted_socket.description = "The inverse of the calculated selection"
			
			#Socket ALA
			ala_socket = _mn_select_res_name_peptide.interface.new_socket(name = "ALA", in_out='INPUT', socket_type = 'NodeSocketBool')
			ala_socket.attribute_domain = 'POINT'
			ala_socket.description = "Select the AA residue ALA"
			
			#Socket ARG
			arg_socket = _mn_select_res_name_peptide.interface.new_socket(name = "ARG", in_out='INPUT', socket_type = 'NodeSocketBool')
			arg_socket.attribute_domain = 'POINT'
			arg_socket.description = "Select the AA residue ARG"
			
			#Socket ASN
			asn_socket = _mn_select_res_name_peptide.interface.new_socket(name = "ASN", in_out='INPUT', socket_type = 'NodeSocketBool')
			asn_socket.attribute_domain = 'POINT'
			asn_socket.description = "Select the AA residue ASN"
			
			#Socket ASP
			asp_socket = _mn_select_res_name_peptide.interface.new_socket(name = "ASP", in_out='INPUT', socket_type = 'NodeSocketBool')
			asp_socket.attribute_domain = 'POINT'
			asp_socket.description = "Select the AA residue ASP"
			
			#Socket CYS
			cys_socket = _mn_select_res_name_peptide.interface.new_socket(name = "CYS", in_out='INPUT', socket_type = 'NodeSocketBool')
			cys_socket.attribute_domain = 'POINT'
			cys_socket.description = "Select the AA residue CYS"
			
			#Socket GLU
			glu_socket = _mn_select_res_name_peptide.interface.new_socket(name = "GLU", in_out='INPUT', socket_type = 'NodeSocketBool')
			glu_socket.attribute_domain = 'POINT'
			glu_socket.description = "Select the AA residue GLU"
			
			#Socket GLN
			gln_socket = _mn_select_res_name_peptide.interface.new_socket(name = "GLN", in_out='INPUT', socket_type = 'NodeSocketBool')
			gln_socket.attribute_domain = 'POINT'
			gln_socket.description = "Select the AA residue GLN"
			
			#Socket GLY
			gly_socket = _mn_select_res_name_peptide.interface.new_socket(name = "GLY", in_out='INPUT', socket_type = 'NodeSocketBool')
			gly_socket.attribute_domain = 'POINT'
			gly_socket.description = "Select the AA residue GLY"
			
			#Socket HIS
			his_socket = _mn_select_res_name_peptide.interface.new_socket(name = "HIS", in_out='INPUT', socket_type = 'NodeSocketBool')
			his_socket.attribute_domain = 'POINT'
			his_socket.description = "Select the AA residue HIS"
			
			#Socket ILE
			ile_socket = _mn_select_res_name_peptide.interface.new_socket(name = "ILE", in_out='INPUT', socket_type = 'NodeSocketBool')
			ile_socket.attribute_domain = 'POINT'
			ile_socket.description = "Select the AA residue ILE"
			
			#Socket LEU
			leu_socket = _mn_select_res_name_peptide.interface.new_socket(name = "LEU", in_out='INPUT', socket_type = 'NodeSocketBool')
			leu_socket.attribute_domain = 'POINT'
			leu_socket.description = "Select the AA residue LEU"
			
			#Socket LYS
			lys_socket = _mn_select_res_name_peptide.interface.new_socket(name = "LYS", in_out='INPUT', socket_type = 'NodeSocketBool')
			lys_socket.attribute_domain = 'POINT'
			lys_socket.description = "Select the AA residue LYS"
			
			#Socket MET
			met_socket = _mn_select_res_name_peptide.interface.new_socket(name = "MET", in_out='INPUT', socket_type = 'NodeSocketBool')
			met_socket.attribute_domain = 'POINT'
			met_socket.description = "Select the AA residue MET"
			
			#Socket PHE
			phe_socket = _mn_select_res_name_peptide.interface.new_socket(name = "PHE", in_out='INPUT', socket_type = 'NodeSocketBool')
			phe_socket.attribute_domain = 'POINT'
			phe_socket.description = "Select the AA residue PHE"
			
			#Socket PRO
			pro_socket = _mn_select_res_name_peptide.interface.new_socket(name = "PRO", in_out='INPUT', socket_type = 'NodeSocketBool')
			pro_socket.attribute_domain = 'POINT'
			pro_socket.description = "Select the AA residue PRO"
			
			#Socket SER
			ser_socket = _mn_select_res_name_peptide.interface.new_socket(name = "SER", in_out='INPUT', socket_type = 'NodeSocketBool')
			ser_socket.attribute_domain = 'POINT'
			ser_socket.description = "Select the AA residue SER"
			
			#Socket THR
			thr_socket = _mn_select_res_name_peptide.interface.new_socket(name = "THR", in_out='INPUT', socket_type = 'NodeSocketBool')
			thr_socket.attribute_domain = 'POINT'
			thr_socket.description = "Select the AA residue THR"
			
			#Socket TRP
			trp_socket = _mn_select_res_name_peptide.interface.new_socket(name = "TRP", in_out='INPUT', socket_type = 'NodeSocketBool')
			trp_socket.attribute_domain = 'POINT'
			trp_socket.description = "Select the AA residue TRP"
			
			#Socket TYR
			tyr_socket = _mn_select_res_name_peptide.interface.new_socket(name = "TYR", in_out='INPUT', socket_type = 'NodeSocketBool')
			tyr_socket.attribute_domain = 'POINT'
			tyr_socket.description = "Select the AA residue TYR"
			
			#Socket VAL
			val_socket = _mn_select_res_name_peptide.interface.new_socket(name = "VAL", in_out='INPUT', socket_type = 'NodeSocketBool')
			val_socket.attribute_domain = 'POINT'
			val_socket.description = "Select the AA residue VAL"
			
			
			#initialize _mn_select_res_name_peptide nodes
			#node Reroute.018
			reroute_018 = _mn_select_res_name_peptide.nodes.new("NodeReroute")
			reroute_018.name = "Reroute.018"
			#node Group Output
			group_output = _mn_select_res_name_peptide.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Boolean Math.001
			boolean_math_001 = _mn_select_res_name_peptide.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001.name = "Boolean Math.001"
			boolean_math_001.operation = 'NOT'
			
			#node Named Attribute
			named_attribute = _mn_select_res_name_peptide.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'INT'
			#Name
			named_attribute.inputs[0].default_value = "res_name"
			
			#node Group Input
			group_input = _mn_select_res_name_peptide.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Index Switch
			index_switch = _mn_select_res_name_peptide.nodes.new("GeometryNodeIndexSwitch")
			index_switch.name = "Index Switch"
			index_switch.data_type = 'BOOLEAN'
			index_switch.index_switch_items.clear()
			index_switch.index_switch_items.new()
			index_switch.index_switch_items.new()
			index_switch.index_switch_items.new()
			index_switch.index_switch_items.new()
			index_switch.index_switch_items.new()
			index_switch.index_switch_items.new()
			index_switch.index_switch_items.new()
			index_switch.index_switch_items.new()
			index_switch.index_switch_items.new()
			index_switch.index_switch_items.new()
			index_switch.index_switch_items.new()
			index_switch.index_switch_items.new()
			index_switch.index_switch_items.new()
			index_switch.index_switch_items.new()
			index_switch.index_switch_items.new()
			index_switch.index_switch_items.new()
			index_switch.index_switch_items.new()
			index_switch.index_switch_items.new()
			index_switch.index_switch_items.new()
			index_switch.index_switch_items.new()
			
			
			
			
			#Set locations
			reroute_018.location = (2740.0, 0.0)
			group_output.location = (3040.0, 40.0)
			boolean_math_001.location = (2840.403076171875, -31.331174850463867)
			named_attribute.location = (2260.0, 80.0)
			group_input.location = (2260.0, -60.0)
			index_switch.location = (2500.0, 40.0)
			
			#Set dimensions
			reroute_018.width, reroute_018.height = 16.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			index_switch.width, index_switch.height = 140.0, 100.0
			
			#initialize _mn_select_res_name_peptide links
			#reroute_018.Output -> boolean_math_001.Boolean
			_mn_select_res_name_peptide.links.new(reroute_018.outputs[0], boolean_math_001.inputs[0])
			#reroute_018.Output -> group_output.Selection
			_mn_select_res_name_peptide.links.new(reroute_018.outputs[0], group_output.inputs[0])
			#boolean_math_001.Boolean -> group_output.Inverted
			_mn_select_res_name_peptide.links.new(boolean_math_001.outputs[0], group_output.inputs[1])
			#named_attribute.Attribute -> index_switch.Index
			_mn_select_res_name_peptide.links.new(named_attribute.outputs[0], index_switch.inputs[0])
			#group_input.ALA -> index_switch.0
			_mn_select_res_name_peptide.links.new(group_input.outputs[0], index_switch.inputs[1])
			#group_input.ARG -> index_switch.1
			_mn_select_res_name_peptide.links.new(group_input.outputs[1], index_switch.inputs[2])
			#group_input.ASN -> index_switch.2
			_mn_select_res_name_peptide.links.new(group_input.outputs[2], index_switch.inputs[3])
			#group_input.ASP -> index_switch.3
			_mn_select_res_name_peptide.links.new(group_input.outputs[3], index_switch.inputs[4])
			#group_input.CYS -> index_switch.4
			_mn_select_res_name_peptide.links.new(group_input.outputs[4], index_switch.inputs[5])
			#group_input.GLU -> index_switch.5
			_mn_select_res_name_peptide.links.new(group_input.outputs[5], index_switch.inputs[6])
			#group_input.GLN -> index_switch.6
			_mn_select_res_name_peptide.links.new(group_input.outputs[6], index_switch.inputs[7])
			#group_input.GLY -> index_switch.7
			_mn_select_res_name_peptide.links.new(group_input.outputs[7], index_switch.inputs[8])
			#group_input.HIS -> index_switch.8
			_mn_select_res_name_peptide.links.new(group_input.outputs[8], index_switch.inputs[9])
			#group_input.ILE -> index_switch.9
			_mn_select_res_name_peptide.links.new(group_input.outputs[9], index_switch.inputs[10])
			#group_input.LEU -> index_switch.10
			_mn_select_res_name_peptide.links.new(group_input.outputs[10], index_switch.inputs[11])
			#group_input.LYS -> index_switch.11
			_mn_select_res_name_peptide.links.new(group_input.outputs[11], index_switch.inputs[12])
			#group_input.MET -> index_switch.12
			_mn_select_res_name_peptide.links.new(group_input.outputs[12], index_switch.inputs[13])
			#group_input.PHE -> index_switch.13
			_mn_select_res_name_peptide.links.new(group_input.outputs[13], index_switch.inputs[14])
			#group_input.PRO -> index_switch.14
			_mn_select_res_name_peptide.links.new(group_input.outputs[14], index_switch.inputs[15])
			#group_input.SER -> index_switch.15
			_mn_select_res_name_peptide.links.new(group_input.outputs[15], index_switch.inputs[16])
			#group_input.THR -> index_switch.16
			_mn_select_res_name_peptide.links.new(group_input.outputs[16], index_switch.inputs[17])
			#group_input.TRP -> index_switch.17
			_mn_select_res_name_peptide.links.new(group_input.outputs[17], index_switch.inputs[18])
			#group_input.TYR -> index_switch.18
			_mn_select_res_name_peptide.links.new(group_input.outputs[18], index_switch.inputs[19])
			#group_input.VAL -> index_switch.19
			_mn_select_res_name_peptide.links.new(group_input.outputs[19], index_switch.inputs[20])
			#index_switch.Output -> reroute_018.Input
			_mn_select_res_name_peptide.links.new(index_switch.outputs[0], reroute_018.inputs[0])
			return _mn_select_res_name_peptide

		_mn_select_res_name_peptide = _mn_select_res_name_peptide_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".MN_select_res_name_peptide", type = 'NODES')
		mod.node_group = _mn_select_res_name_peptide
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_MN_select_res_name_peptide.bl_idname)
			
def register():
	bpy.utils.register_class(_MN_select_res_name_peptide)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_MN_select_res_name_peptide)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
