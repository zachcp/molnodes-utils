bl_info = {
	"name" : "Select Res Name",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Select_Res_Name(bpy.types.Operator):
	bl_idname = "node.select_res_name"
	bl_label = "Select Res Name"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize select_res_name node group
		def select_res_name_node_group():
			select_res_name = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Select Res Name")

			select_res_name.color_tag = 'INPUT'
			select_res_name.description = ""

			
			#select_res_name interface
			#Socket Selection
			selection_socket = select_res_name.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket.default_value = False
			selection_socket.attribute_domain = 'POINT'
			selection_socket.description = "The calculated selection"
			
			#Socket Inverted
			inverted_socket = select_res_name.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket.default_value = False
			inverted_socket.attribute_domain = 'POINT'
			inverted_socket.description = "The inverse of the calculated selection"
			
			#Socket And
			and_socket = select_res_name.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket.default_value = True
			and_socket.attribute_domain = 'POINT'
			and_socket.hide_value = True
			
			#Socket Or
			or_socket = select_res_name.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket.default_value = False
			or_socket.attribute_domain = 'POINT'
			or_socket.hide_value = True
			
			#Panel Protein
			protein_panel = select_res_name.interface.new_panel("Protein")
			#Socket ALA
			ala_socket = select_res_name.interface.new_socket(name = "ALA", in_out='INPUT', socket_type = 'NodeSocketBool', parent = protein_panel)
			ala_socket.default_value = False
			ala_socket.attribute_domain = 'POINT'
			
			#Socket ARG
			arg_socket = select_res_name.interface.new_socket(name = "ARG", in_out='INPUT', socket_type = 'NodeSocketBool', parent = protein_panel)
			arg_socket.default_value = False
			arg_socket.attribute_domain = 'POINT'
			
			#Socket ASN
			asn_socket = select_res_name.interface.new_socket(name = "ASN", in_out='INPUT', socket_type = 'NodeSocketBool', parent = protein_panel)
			asn_socket.default_value = False
			asn_socket.attribute_domain = 'POINT'
			
			#Socket ASP
			asp_socket = select_res_name.interface.new_socket(name = "ASP", in_out='INPUT', socket_type = 'NodeSocketBool', parent = protein_panel)
			asp_socket.default_value = False
			asp_socket.attribute_domain = 'POINT'
			
			#Socket CYS
			cys_socket = select_res_name.interface.new_socket(name = "CYS", in_out='INPUT', socket_type = 'NodeSocketBool', parent = protein_panel)
			cys_socket.default_value = False
			cys_socket.attribute_domain = 'POINT'
			
			#Socket GLU
			glu_socket = select_res_name.interface.new_socket(name = "GLU", in_out='INPUT', socket_type = 'NodeSocketBool', parent = protein_panel)
			glu_socket.default_value = False
			glu_socket.attribute_domain = 'POINT'
			
			#Socket GLN
			gln_socket = select_res_name.interface.new_socket(name = "GLN", in_out='INPUT', socket_type = 'NodeSocketBool', parent = protein_panel)
			gln_socket.default_value = False
			gln_socket.attribute_domain = 'POINT'
			
			#Socket GLY
			gly_socket = select_res_name.interface.new_socket(name = "GLY", in_out='INPUT', socket_type = 'NodeSocketBool', parent = protein_panel)
			gly_socket.default_value = False
			gly_socket.attribute_domain = 'POINT'
			
			#Socket HIS
			his_socket = select_res_name.interface.new_socket(name = "HIS", in_out='INPUT', socket_type = 'NodeSocketBool', parent = protein_panel)
			his_socket.default_value = False
			his_socket.attribute_domain = 'POINT'
			
			#Socket ILE
			ile_socket = select_res_name.interface.new_socket(name = "ILE", in_out='INPUT', socket_type = 'NodeSocketBool', parent = protein_panel)
			ile_socket.default_value = False
			ile_socket.attribute_domain = 'POINT'
			
			#Socket LEU
			leu_socket = select_res_name.interface.new_socket(name = "LEU", in_out='INPUT', socket_type = 'NodeSocketBool', parent = protein_panel)
			leu_socket.default_value = False
			leu_socket.attribute_domain = 'POINT'
			
			#Socket LYS
			lys_socket = select_res_name.interface.new_socket(name = "LYS", in_out='INPUT', socket_type = 'NodeSocketBool', parent = protein_panel)
			lys_socket.default_value = False
			lys_socket.attribute_domain = 'POINT'
			
			#Socket MET
			met_socket = select_res_name.interface.new_socket(name = "MET", in_out='INPUT', socket_type = 'NodeSocketBool', parent = protein_panel)
			met_socket.default_value = False
			met_socket.attribute_domain = 'POINT'
			
			#Socket PHE
			phe_socket = select_res_name.interface.new_socket(name = "PHE", in_out='INPUT', socket_type = 'NodeSocketBool', parent = protein_panel)
			phe_socket.default_value = False
			phe_socket.attribute_domain = 'POINT'
			
			#Socket PRO
			pro_socket = select_res_name.interface.new_socket(name = "PRO", in_out='INPUT', socket_type = 'NodeSocketBool', parent = protein_panel)
			pro_socket.default_value = False
			pro_socket.attribute_domain = 'POINT'
			
			#Socket SER
			ser_socket = select_res_name.interface.new_socket(name = "SER", in_out='INPUT', socket_type = 'NodeSocketBool', parent = protein_panel)
			ser_socket.default_value = False
			ser_socket.attribute_domain = 'POINT'
			
			#Socket THR
			thr_socket = select_res_name.interface.new_socket(name = "THR", in_out='INPUT', socket_type = 'NodeSocketBool', parent = protein_panel)
			thr_socket.default_value = False
			thr_socket.attribute_domain = 'POINT'
			
			#Socket TRP
			trp_socket = select_res_name.interface.new_socket(name = "TRP", in_out='INPUT', socket_type = 'NodeSocketBool', parent = protein_panel)
			trp_socket.default_value = False
			trp_socket.attribute_domain = 'POINT'
			
			#Socket TYR
			tyr_socket = select_res_name.interface.new_socket(name = "TYR", in_out='INPUT', socket_type = 'NodeSocketBool', parent = protein_panel)
			tyr_socket.default_value = False
			tyr_socket.attribute_domain = 'POINT'
			
			#Socket VAL
			val_socket = select_res_name.interface.new_socket(name = "VAL", in_out='INPUT', socket_type = 'NodeSocketBool', parent = protein_panel)
			val_socket.default_value = False
			val_socket.attribute_domain = 'POINT'
			
			
			#Panel DNA
			dna_panel = select_res_name.interface.new_panel("DNA")
			#Socket A
			a_socket = select_res_name.interface.new_socket(name = "A", in_out='INPUT', socket_type = 'NodeSocketBool', parent = dna_panel)
			a_socket.default_value = False
			a_socket.attribute_domain = 'POINT'
			
			#Socket C
			c_socket = select_res_name.interface.new_socket(name = "C", in_out='INPUT', socket_type = 'NodeSocketBool', parent = dna_panel)
			c_socket.default_value = False
			c_socket.attribute_domain = 'POINT'
			
			#Socket G
			g_socket = select_res_name.interface.new_socket(name = "G", in_out='INPUT', socket_type = 'NodeSocketBool', parent = dna_panel)
			g_socket.default_value = False
			g_socket.attribute_domain = 'POINT'
			
			#Socket T
			t_socket = select_res_name.interface.new_socket(name = "T", in_out='INPUT', socket_type = 'NodeSocketBool', parent = dna_panel)
			t_socket.default_value = False
			t_socket.attribute_domain = 'POINT'
			
			
			#Panel RNA
			rna_panel = select_res_name.interface.new_panel("RNA")
			#Socket rA
			ra_socket = select_res_name.interface.new_socket(name = "rA", in_out='INPUT', socket_type = 'NodeSocketBool', parent = rna_panel)
			ra_socket.default_value = False
			ra_socket.attribute_domain = 'POINT'
			
			#Socket rC
			rc_socket = select_res_name.interface.new_socket(name = "rC", in_out='INPUT', socket_type = 'NodeSocketBool', parent = rna_panel)
			rc_socket.default_value = False
			rc_socket.attribute_domain = 'POINT'
			
			#Socket rG
			rg_socket = select_res_name.interface.new_socket(name = "rG", in_out='INPUT', socket_type = 'NodeSocketBool', parent = rna_panel)
			rg_socket.default_value = False
			rg_socket.attribute_domain = 'POINT'
			
			#Socket rU
			ru_socket = select_res_name.interface.new_socket(name = "rU", in_out='INPUT', socket_type = 'NodeSocketBool', parent = rna_panel)
			ru_socket.default_value = False
			ru_socket.attribute_domain = 'POINT'
			
			
			
			#initialize select_res_name nodes
			#node Group Input
			group_input = select_res_name.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			group_input.outputs[0].hide = True
			group_input.outputs[1].hide = True
			group_input.outputs[22].hide = True
			group_input.outputs[23].hide = True
			group_input.outputs[24].hide = True
			group_input.outputs[25].hide = True
			group_input.outputs[26].hide = True
			group_input.outputs[27].hide = True
			group_input.outputs[28].hide = True
			group_input.outputs[29].hide = True
			group_input.outputs[30].hide = True
			
			#node Group Output
			group_output = select_res_name.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Boolean Math.001
			boolean_math_001 = select_res_name.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001.name = "Boolean Math.001"
			boolean_math_001.operation = 'NOT'
			
			#node Boolean Math.002
			boolean_math_002 = select_res_name.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002.name = "Boolean Math.002"
			boolean_math_002.operation = 'AND'
			
			#node Group Input.001
			group_input_001 = select_res_name.nodes.new("NodeGroupInput")
			group_input_001.name = "Group Input.001"
			group_input_001.outputs[2].hide = True
			group_input_001.outputs[3].hide = True
			group_input_001.outputs[4].hide = True
			group_input_001.outputs[5].hide = True
			group_input_001.outputs[6].hide = True
			group_input_001.outputs[7].hide = True
			group_input_001.outputs[8].hide = True
			group_input_001.outputs[9].hide = True
			group_input_001.outputs[10].hide = True
			group_input_001.outputs[11].hide = True
			group_input_001.outputs[12].hide = True
			group_input_001.outputs[13].hide = True
			group_input_001.outputs[14].hide = True
			group_input_001.outputs[15].hide = True
			group_input_001.outputs[16].hide = True
			group_input_001.outputs[17].hide = True
			group_input_001.outputs[18].hide = True
			group_input_001.outputs[19].hide = True
			group_input_001.outputs[20].hide = True
			group_input_001.outputs[21].hide = True
			group_input_001.outputs[22].hide = True
			group_input_001.outputs[23].hide = True
			group_input_001.outputs[24].hide = True
			group_input_001.outputs[25].hide = True
			group_input_001.outputs[26].hide = True
			group_input_001.outputs[27].hide = True
			group_input_001.outputs[28].hide = True
			group_input_001.outputs[29].hide = True
			group_input_001.outputs[30].hide = True
			
			#node Named Attribute.001
			named_attribute_001 = select_res_name.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.data_type = 'INT'
			#Name
			named_attribute_001.inputs[0].default_value = "res_name"
			
			#node Index Switch.002
			index_switch_002 = select_res_name.nodes.new("GeometryNodeIndexSwitch")
			index_switch_002.name = "Index Switch.002"
			index_switch_002.data_type = 'BOOLEAN'
			index_switch_002.index_switch_items.clear()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			index_switch_002.index_switch_items.new()
			#Item_21
			index_switch_002.inputs[21].default_value = False
			#Item_22
			index_switch_002.inputs[22].default_value = False
			#Item_23
			index_switch_002.inputs[23].default_value = False
			#Item_24
			index_switch_002.inputs[24].default_value = False
			#Item_25
			index_switch_002.inputs[25].default_value = False
			#Item_26
			index_switch_002.inputs[26].default_value = False
			#Item_27
			index_switch_002.inputs[27].default_value = False
			#Item_28
			index_switch_002.inputs[28].default_value = False
			#Item_29
			index_switch_002.inputs[29].default_value = False
			#Item_30
			index_switch_002.inputs[30].default_value = False
			#Item_35
			index_switch_002.inputs[35].default_value = False
			#Item_36
			index_switch_002.inputs[36].default_value = False
			#Item_37
			index_switch_002.inputs[37].default_value = False
			#Item_38
			index_switch_002.inputs[38].default_value = False
			#Item_39
			index_switch_002.inputs[39].default_value = False
			#Item_40
			index_switch_002.inputs[40].default_value = False
			
			#node Group Input.002
			group_input_002 = select_res_name.nodes.new("NodeGroupInput")
			group_input_002.name = "Group Input.002"
			group_input_002.outputs[0].hide = True
			group_input_002.outputs[1].hide = True
			group_input_002.outputs[2].hide = True
			group_input_002.outputs[3].hide = True
			group_input_002.outputs[4].hide = True
			group_input_002.outputs[5].hide = True
			group_input_002.outputs[6].hide = True
			group_input_002.outputs[7].hide = True
			group_input_002.outputs[8].hide = True
			group_input_002.outputs[9].hide = True
			group_input_002.outputs[10].hide = True
			group_input_002.outputs[11].hide = True
			group_input_002.outputs[12].hide = True
			group_input_002.outputs[13].hide = True
			group_input_002.outputs[14].hide = True
			group_input_002.outputs[15].hide = True
			group_input_002.outputs[16].hide = True
			group_input_002.outputs[17].hide = True
			group_input_002.outputs[18].hide = True
			group_input_002.outputs[19].hide = True
			group_input_002.outputs[20].hide = True
			group_input_002.outputs[21].hide = True
			group_input_002.outputs[30].hide = True
			
			#node Boolean Math.003
			boolean_math_003 = select_res_name.nodes.new("FunctionNodeBooleanMath")
			boolean_math_003.name = "Boolean Math.003"
			boolean_math_003.operation = 'OR'
			
			
			
			
			#Set locations
			group_input.location = (-560.0, 40.0)
			group_output.location = (220.0, 180.0)
			boolean_math_001.location = (0.0, 60.0)
			boolean_math_002.location = (-140.0, 200.0)
			group_input_001.location = (-300.0, 200.0)
			named_attribute_001.location = (-560.0, 200.0)
			index_switch_002.location = (-300.0, 140.0)
			group_input_002.location = (-560.0, -660.0)
			boolean_math_003.location = (0.0, 200.0)
			
			#Set dimensions
			group_input.width, group_input.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
			boolean_math_002.width, boolean_math_002.height = 123.69171142578125, 100.0
			group_input_001.width, group_input_001.height = 140.0, 100.0
			named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
			index_switch_002.width, index_switch_002.height = 140.0, 100.0
			group_input_002.width, group_input_002.height = 140.0, 100.0
			boolean_math_003.width, boolean_math_003.height = 123.69171142578125, 100.0
			
			#initialize select_res_name links
			#boolean_math_003.Boolean -> boolean_math_001.Boolean
			select_res_name.links.new(boolean_math_003.outputs[0], boolean_math_001.inputs[0])
			#boolean_math_003.Boolean -> group_output.Selection
			select_res_name.links.new(boolean_math_003.outputs[0], group_output.inputs[0])
			#boolean_math_001.Boolean -> group_output.Inverted
			select_res_name.links.new(boolean_math_001.outputs[0], group_output.inputs[1])
			#index_switch_002.Output -> boolean_math_002.Boolean
			select_res_name.links.new(index_switch_002.outputs[0], boolean_math_002.inputs[1])
			#group_input_001.And -> boolean_math_002.Boolean
			select_res_name.links.new(group_input_001.outputs[0], boolean_math_002.inputs[0])
			#named_attribute_001.Attribute -> index_switch_002.Index
			select_res_name.links.new(named_attribute_001.outputs[0], index_switch_002.inputs[0])
			#group_input.ALA -> index_switch_002.0
			select_res_name.links.new(group_input.outputs[2], index_switch_002.inputs[1])
			#group_input.ARG -> index_switch_002.1
			select_res_name.links.new(group_input.outputs[3], index_switch_002.inputs[2])
			#group_input.ASN -> index_switch_002.2
			select_res_name.links.new(group_input.outputs[4], index_switch_002.inputs[3])
			#group_input.ASP -> index_switch_002.3
			select_res_name.links.new(group_input.outputs[5], index_switch_002.inputs[4])
			#group_input.CYS -> index_switch_002.4
			select_res_name.links.new(group_input.outputs[6], index_switch_002.inputs[5])
			#group_input.GLU -> index_switch_002.5
			select_res_name.links.new(group_input.outputs[7], index_switch_002.inputs[6])
			#group_input.GLN -> index_switch_002.6
			select_res_name.links.new(group_input.outputs[8], index_switch_002.inputs[7])
			#group_input.GLY -> index_switch_002.7
			select_res_name.links.new(group_input.outputs[9], index_switch_002.inputs[8])
			#group_input.HIS -> index_switch_002.8
			select_res_name.links.new(group_input.outputs[10], index_switch_002.inputs[9])
			#group_input.ILE -> index_switch_002.9
			select_res_name.links.new(group_input.outputs[11], index_switch_002.inputs[10])
			#group_input.LEU -> index_switch_002.10
			select_res_name.links.new(group_input.outputs[12], index_switch_002.inputs[11])
			#group_input.LYS -> index_switch_002.11
			select_res_name.links.new(group_input.outputs[13], index_switch_002.inputs[12])
			#group_input.MET -> index_switch_002.12
			select_res_name.links.new(group_input.outputs[14], index_switch_002.inputs[13])
			#group_input.PHE -> index_switch_002.13
			select_res_name.links.new(group_input.outputs[15], index_switch_002.inputs[14])
			#group_input.PRO -> index_switch_002.14
			select_res_name.links.new(group_input.outputs[16], index_switch_002.inputs[15])
			#group_input.SER -> index_switch_002.15
			select_res_name.links.new(group_input.outputs[17], index_switch_002.inputs[16])
			#group_input.THR -> index_switch_002.16
			select_res_name.links.new(group_input.outputs[18], index_switch_002.inputs[17])
			#group_input.TRP -> index_switch_002.17
			select_res_name.links.new(group_input.outputs[19], index_switch_002.inputs[18])
			#group_input.TYR -> index_switch_002.18
			select_res_name.links.new(group_input.outputs[20], index_switch_002.inputs[19])
			#group_input.VAL -> index_switch_002.19
			select_res_name.links.new(group_input.outputs[21], index_switch_002.inputs[20])
			#group_input_002.rA -> index_switch_002.40
			select_res_name.links.new(group_input_002.outputs[26], index_switch_002.inputs[41])
			#group_input_002.rC -> index_switch_002.41
			select_res_name.links.new(group_input_002.outputs[27], index_switch_002.inputs[42])
			#group_input_002.rG -> index_switch_002.42
			select_res_name.links.new(group_input_002.outputs[28], index_switch_002.inputs[43])
			#group_input_002.rU -> index_switch_002.43
			select_res_name.links.new(group_input_002.outputs[29], index_switch_002.inputs[44])
			#group_input_002.A -> index_switch_002.30
			select_res_name.links.new(group_input_002.outputs[22], index_switch_002.inputs[31])
			#group_input_002.C -> index_switch_002.31
			select_res_name.links.new(group_input_002.outputs[23], index_switch_002.inputs[32])
			#group_input_002.G -> index_switch_002.32
			select_res_name.links.new(group_input_002.outputs[24], index_switch_002.inputs[33])
			#group_input_002.T -> index_switch_002.33
			select_res_name.links.new(group_input_002.outputs[25], index_switch_002.inputs[34])
			#boolean_math_002.Boolean -> boolean_math_003.Boolean
			select_res_name.links.new(boolean_math_002.outputs[0], boolean_math_003.inputs[0])
			#group_input_001.Or -> boolean_math_003.Boolean
			select_res_name.links.new(group_input_001.outputs[1], boolean_math_003.inputs[1])
			return select_res_name

		select_res_name = select_res_name_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Select Res Name", type = 'NODES')
		mod.node_group = select_res_name
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Select_Res_Name.bl_idname)
			
def register():
	bpy.utils.register_class(Select_Res_Name)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Select_Res_Name)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
