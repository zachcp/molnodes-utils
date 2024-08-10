bl_info = {
	"name" : "Color Element",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Color_Element(bpy.types.Operator):
	bl_idname = "node.color_element"
	bl_label = "Color Element"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize color_element node group
		def color_element_node_group():
			color_element = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Color Element")

			color_element.color_tag = 'COLOR'
			color_element.description = ""

			
			#color_element interface
			#Socket Color
			color_socket = color_element.interface.new_socket(name = "Color", in_out='OUTPUT', socket_type = 'NodeSocketColor')
			color_socket.attribute_domain = 'POINT'
			
			#Panel 1-20
			_1_20_panel = color_element.interface.new_panel("1-20", default_closed=True)
			#Socket H
			h_socket = color_element.interface.new_socket(name = "H", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _1_20_panel)
			h_socket.attribute_domain = 'POINT'
			
			#Socket He
			he_socket = color_element.interface.new_socket(name = "He", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _1_20_panel)
			he_socket.attribute_domain = 'POINT'
			
			#Socket Li
			li_socket = color_element.interface.new_socket(name = "Li", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _1_20_panel)
			li_socket.attribute_domain = 'POINT'
			
			#Socket Be
			be_socket = color_element.interface.new_socket(name = "Be", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _1_20_panel)
			be_socket.attribute_domain = 'POINT'
			
			#Socket B
			b_socket = color_element.interface.new_socket(name = "B", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _1_20_panel)
			b_socket.attribute_domain = 'POINT'
			
			#Socket C
			c_socket = color_element.interface.new_socket(name = "C", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _1_20_panel)
			c_socket.attribute_domain = 'POINT'
			
			#Socket N
			n_socket = color_element.interface.new_socket(name = "N", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _1_20_panel)
			n_socket.attribute_domain = 'POINT'
			
			#Socket O
			o_socket = color_element.interface.new_socket(name = "O", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _1_20_panel)
			o_socket.attribute_domain = 'POINT'
			
			#Socket F
			f_socket = color_element.interface.new_socket(name = "F", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _1_20_panel)
			f_socket.attribute_domain = 'POINT'
			
			#Socket Ne
			ne_socket = color_element.interface.new_socket(name = "Ne", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _1_20_panel)
			ne_socket.attribute_domain = 'POINT'
			
			#Socket Na
			na_socket = color_element.interface.new_socket(name = "Na", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _1_20_panel)
			na_socket.attribute_domain = 'POINT'
			
			#Socket Mg
			mg_socket = color_element.interface.new_socket(name = "Mg", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _1_20_panel)
			mg_socket.attribute_domain = 'POINT'
			
			#Socket Al
			al_socket = color_element.interface.new_socket(name = "Al", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _1_20_panel)
			al_socket.attribute_domain = 'POINT'
			
			#Socket Si
			si_socket = color_element.interface.new_socket(name = "Si", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _1_20_panel)
			si_socket.attribute_domain = 'POINT'
			
			#Socket P
			p_socket = color_element.interface.new_socket(name = "P", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _1_20_panel)
			p_socket.attribute_domain = 'POINT'
			
			#Socket S
			s_socket = color_element.interface.new_socket(name = "S", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _1_20_panel)
			s_socket.attribute_domain = 'POINT'
			
			#Socket Cl
			cl_socket = color_element.interface.new_socket(name = "Cl", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _1_20_panel)
			cl_socket.attribute_domain = 'POINT'
			
			#Socket Ar
			ar_socket = color_element.interface.new_socket(name = "Ar", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _1_20_panel)
			ar_socket.attribute_domain = 'POINT'
			
			#Socket K
			k_socket = color_element.interface.new_socket(name = "K", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _1_20_panel)
			k_socket.attribute_domain = 'POINT'
			
			#Socket Ca
			ca_socket = color_element.interface.new_socket(name = "Ca", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _1_20_panel)
			ca_socket.attribute_domain = 'POINT'
			
			
			#Panel 21-40
			_21_40_panel = color_element.interface.new_panel("21-40", default_closed=True)
			#Socket Sc
			sc_socket = color_element.interface.new_socket(name = "Sc", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _21_40_panel)
			sc_socket.attribute_domain = 'POINT'
			
			#Socket Ti
			ti_socket = color_element.interface.new_socket(name = "Ti", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _21_40_panel)
			ti_socket.attribute_domain = 'POINT'
			
			#Socket V
			v_socket = color_element.interface.new_socket(name = "V", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _21_40_panel)
			v_socket.attribute_domain = 'POINT'
			
			#Socket Cr
			cr_socket = color_element.interface.new_socket(name = "Cr", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _21_40_panel)
			cr_socket.attribute_domain = 'POINT'
			
			#Socket Mn
			mn_socket = color_element.interface.new_socket(name = "Mn", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _21_40_panel)
			mn_socket.attribute_domain = 'POINT'
			
			#Socket Fe
			fe_socket = color_element.interface.new_socket(name = "Fe", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _21_40_panel)
			fe_socket.attribute_domain = 'POINT'
			
			#Socket Co
			co_socket = color_element.interface.new_socket(name = "Co", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _21_40_panel)
			co_socket.attribute_domain = 'POINT'
			
			#Socket Ni
			ni_socket = color_element.interface.new_socket(name = "Ni", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _21_40_panel)
			ni_socket.attribute_domain = 'POINT'
			
			#Socket Cu
			cu_socket = color_element.interface.new_socket(name = "Cu", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _21_40_panel)
			cu_socket.attribute_domain = 'POINT'
			
			#Socket Zn
			zn_socket = color_element.interface.new_socket(name = "Zn", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _21_40_panel)
			zn_socket.attribute_domain = 'POINT'
			
			#Socket Ga
			ga_socket = color_element.interface.new_socket(name = "Ga", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _21_40_panel)
			ga_socket.attribute_domain = 'POINT'
			
			#Socket Ge
			ge_socket = color_element.interface.new_socket(name = "Ge", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _21_40_panel)
			ge_socket.attribute_domain = 'POINT'
			
			#Socket As
			as_socket = color_element.interface.new_socket(name = "As", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _21_40_panel)
			as_socket.attribute_domain = 'POINT'
			
			#Socket Se
			se_socket = color_element.interface.new_socket(name = "Se", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _21_40_panel)
			se_socket.attribute_domain = 'POINT'
			
			#Socket Br
			br_socket = color_element.interface.new_socket(name = "Br", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _21_40_panel)
			br_socket.attribute_domain = 'POINT'
			
			#Socket Kr
			kr_socket = color_element.interface.new_socket(name = "Kr", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _21_40_panel)
			kr_socket.attribute_domain = 'POINT'
			
			#Socket Rb
			rb_socket = color_element.interface.new_socket(name = "Rb", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _21_40_panel)
			rb_socket.attribute_domain = 'POINT'
			
			#Socket Sr
			sr_socket = color_element.interface.new_socket(name = "Sr", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _21_40_panel)
			sr_socket.attribute_domain = 'POINT'
			
			#Socket Y
			y_socket = color_element.interface.new_socket(name = "Y", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _21_40_panel)
			y_socket.attribute_domain = 'POINT'
			
			#Socket Zr
			zr_socket = color_element.interface.new_socket(name = "Zr", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _21_40_panel)
			zr_socket.attribute_domain = 'POINT'
			
			
			#Panel 41-60
			_41_60_panel = color_element.interface.new_panel("41-60", default_closed=True)
			#Socket Nb
			nb_socket = color_element.interface.new_socket(name = "Nb", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _41_60_panel)
			nb_socket.attribute_domain = 'POINT'
			
			#Socket Mo
			mo_socket = color_element.interface.new_socket(name = "Mo", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _41_60_panel)
			mo_socket.attribute_domain = 'POINT'
			
			#Socket Tc
			tc_socket = color_element.interface.new_socket(name = "Tc", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _41_60_panel)
			tc_socket.attribute_domain = 'POINT'
			
			#Socket Ru
			ru_socket = color_element.interface.new_socket(name = "Ru", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _41_60_panel)
			ru_socket.attribute_domain = 'POINT'
			
			#Socket Rh
			rh_socket = color_element.interface.new_socket(name = "Rh", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _41_60_panel)
			rh_socket.attribute_domain = 'POINT'
			
			#Socket Pd
			pd_socket = color_element.interface.new_socket(name = "Pd", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _41_60_panel)
			pd_socket.attribute_domain = 'POINT'
			
			#Socket Ag
			ag_socket = color_element.interface.new_socket(name = "Ag", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _41_60_panel)
			ag_socket.attribute_domain = 'POINT'
			
			#Socket Cd
			cd_socket = color_element.interface.new_socket(name = "Cd", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _41_60_panel)
			cd_socket.attribute_domain = 'POINT'
			
			#Socket In
			in_socket = color_element.interface.new_socket(name = "In", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _41_60_panel)
			in_socket.attribute_domain = 'POINT'
			
			#Socket Sn
			sn_socket = color_element.interface.new_socket(name = "Sn", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _41_60_panel)
			sn_socket.attribute_domain = 'POINT'
			
			#Socket Sb
			sb_socket = color_element.interface.new_socket(name = "Sb", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _41_60_panel)
			sb_socket.attribute_domain = 'POINT'
			
			#Socket Te
			te_socket = color_element.interface.new_socket(name = "Te", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _41_60_panel)
			te_socket.attribute_domain = 'POINT'
			
			#Socket I
			i_socket = color_element.interface.new_socket(name = "I", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _41_60_panel)
			i_socket.attribute_domain = 'POINT'
			
			#Socket Xe
			xe_socket = color_element.interface.new_socket(name = "Xe", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _41_60_panel)
			xe_socket.attribute_domain = 'POINT'
			
			#Socket Cs
			cs_socket = color_element.interface.new_socket(name = "Cs", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _41_60_panel)
			cs_socket.attribute_domain = 'POINT'
			
			#Socket Ba
			ba_socket = color_element.interface.new_socket(name = "Ba", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _41_60_panel)
			ba_socket.attribute_domain = 'POINT'
			
			#Socket La
			la_socket = color_element.interface.new_socket(name = "La", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _41_60_panel)
			la_socket.attribute_domain = 'POINT'
			
			#Socket Ce
			ce_socket = color_element.interface.new_socket(name = "Ce", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _41_60_panel)
			ce_socket.attribute_domain = 'POINT'
			
			#Socket Pr
			pr_socket = color_element.interface.new_socket(name = "Pr", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _41_60_panel)
			pr_socket.attribute_domain = 'POINT'
			
			#Socket Nd
			nd_socket = color_element.interface.new_socket(name = "Nd", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _41_60_panel)
			nd_socket.attribute_domain = 'POINT'
			
			
			#Panel 61-80
			_61_80_panel = color_element.interface.new_panel("61-80", default_closed=True)
			#Socket Pm
			pm_socket = color_element.interface.new_socket(name = "Pm", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _61_80_panel)
			pm_socket.attribute_domain = 'POINT'
			
			#Socket Sm
			sm_socket = color_element.interface.new_socket(name = "Sm", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _61_80_panel)
			sm_socket.attribute_domain = 'POINT'
			
			#Socket Eu
			eu_socket = color_element.interface.new_socket(name = "Eu", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _61_80_panel)
			eu_socket.attribute_domain = 'POINT'
			
			#Socket Gd
			gd_socket = color_element.interface.new_socket(name = "Gd", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _61_80_panel)
			gd_socket.attribute_domain = 'POINT'
			
			#Socket Tb
			tb_socket = color_element.interface.new_socket(name = "Tb", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _61_80_panel)
			tb_socket.attribute_domain = 'POINT'
			
			#Socket Dy
			dy_socket = color_element.interface.new_socket(name = "Dy", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _61_80_panel)
			dy_socket.attribute_domain = 'POINT'
			
			#Socket Ho
			ho_socket = color_element.interface.new_socket(name = "Ho", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _61_80_panel)
			ho_socket.attribute_domain = 'POINT'
			
			#Socket Er
			er_socket = color_element.interface.new_socket(name = "Er", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _61_80_panel)
			er_socket.attribute_domain = 'POINT'
			
			#Socket Tm
			tm_socket = color_element.interface.new_socket(name = "Tm", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _61_80_panel)
			tm_socket.attribute_domain = 'POINT'
			
			#Socket Yb
			yb_socket = color_element.interface.new_socket(name = "Yb", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _61_80_panel)
			yb_socket.attribute_domain = 'POINT'
			
			#Socket Lu
			lu_socket = color_element.interface.new_socket(name = "Lu", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _61_80_panel)
			lu_socket.attribute_domain = 'POINT'
			
			#Socket Hf
			hf_socket = color_element.interface.new_socket(name = "Hf", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _61_80_panel)
			hf_socket.attribute_domain = 'POINT'
			
			#Socket Ta
			ta_socket = color_element.interface.new_socket(name = "Ta", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _61_80_panel)
			ta_socket.attribute_domain = 'POINT'
			
			#Socket W
			w_socket = color_element.interface.new_socket(name = "W", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _61_80_panel)
			w_socket.attribute_domain = 'POINT'
			
			#Socket Re
			re_socket = color_element.interface.new_socket(name = "Re", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _61_80_panel)
			re_socket.attribute_domain = 'POINT'
			
			#Socket Os
			os_socket = color_element.interface.new_socket(name = "Os", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _61_80_panel)
			os_socket.attribute_domain = 'POINT'
			
			#Socket Ir
			ir_socket = color_element.interface.new_socket(name = "Ir", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _61_80_panel)
			ir_socket.attribute_domain = 'POINT'
			
			#Socket Pt
			pt_socket = color_element.interface.new_socket(name = "Pt", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _61_80_panel)
			pt_socket.attribute_domain = 'POINT'
			
			#Socket Au
			au_socket = color_element.interface.new_socket(name = "Au", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _61_80_panel)
			au_socket.attribute_domain = 'POINT'
			
			#Socket Hg
			hg_socket = color_element.interface.new_socket(name = "Hg", in_out='INPUT', socket_type = 'NodeSocketColor', parent = _61_80_panel)
			hg_socket.attribute_domain = 'POINT'
			
			
			
			#initialize color_element nodes
			#node Group Input
			group_input = color_element.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Group Output
			group_output = color_element.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Named Attribute
			named_attribute = color_element.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'INT'
			#Name
			named_attribute.inputs[0].default_value = "atomic_number"
			
			#node Index Switch
			index_switch = color_element.nodes.new("GeometryNodeIndexSwitch")
			index_switch.name = "Index Switch"
			index_switch.data_type = 'RGBA'
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
			index_switch.index_switch_items.new()
			#Item_0
			index_switch.inputs[1].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
			
			
			
			
			#Set locations
			group_input.location = (-340.0, 0.0)
			group_output.location = (200.0, 0.0)
			named_attribute.location = (0.0, 150.0)
			index_switch.location = (0.0, 0.0)
			
			#Set dimensions
			group_input.width, group_input.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			index_switch.width, index_switch.height = 140.0, 100.0
			
			#initialize color_element links
			#named_attribute.Attribute -> index_switch.Index
			color_element.links.new(named_attribute.outputs[0], index_switch.inputs[0])
			#group_input.H -> index_switch.1
			color_element.links.new(group_input.outputs[0], index_switch.inputs[2])
			#group_input.He -> index_switch.2
			color_element.links.new(group_input.outputs[1], index_switch.inputs[3])
			#group_input.Li -> index_switch.3
			color_element.links.new(group_input.outputs[2], index_switch.inputs[4])
			#group_input.Be -> index_switch.4
			color_element.links.new(group_input.outputs[3], index_switch.inputs[5])
			#group_input.B -> index_switch.5
			color_element.links.new(group_input.outputs[4], index_switch.inputs[6])
			#group_input.C -> index_switch.6
			color_element.links.new(group_input.outputs[5], index_switch.inputs[7])
			#group_input.N -> index_switch.7
			color_element.links.new(group_input.outputs[6], index_switch.inputs[8])
			#group_input.O -> index_switch.8
			color_element.links.new(group_input.outputs[7], index_switch.inputs[9])
			#group_input.F -> index_switch.9
			color_element.links.new(group_input.outputs[8], index_switch.inputs[10])
			#group_input.Ne -> index_switch.10
			color_element.links.new(group_input.outputs[9], index_switch.inputs[11])
			#group_input.Na -> index_switch.11
			color_element.links.new(group_input.outputs[10], index_switch.inputs[12])
			#group_input.Mg -> index_switch.12
			color_element.links.new(group_input.outputs[11], index_switch.inputs[13])
			#group_input.Al -> index_switch.13
			color_element.links.new(group_input.outputs[12], index_switch.inputs[14])
			#group_input.Si -> index_switch.14
			color_element.links.new(group_input.outputs[13], index_switch.inputs[15])
			#group_input.P -> index_switch.15
			color_element.links.new(group_input.outputs[14], index_switch.inputs[16])
			#group_input.S -> index_switch.16
			color_element.links.new(group_input.outputs[15], index_switch.inputs[17])
			#group_input.Cl -> index_switch.17
			color_element.links.new(group_input.outputs[16], index_switch.inputs[18])
			#group_input.Ar -> index_switch.18
			color_element.links.new(group_input.outputs[17], index_switch.inputs[19])
			#group_input.K -> index_switch.19
			color_element.links.new(group_input.outputs[18], index_switch.inputs[20])
			#group_input.Ca -> index_switch.20
			color_element.links.new(group_input.outputs[19], index_switch.inputs[21])
			#group_input.Sc -> index_switch.21
			color_element.links.new(group_input.outputs[20], index_switch.inputs[22])
			#group_input.Ti -> index_switch.22
			color_element.links.new(group_input.outputs[21], index_switch.inputs[23])
			#group_input.V -> index_switch.23
			color_element.links.new(group_input.outputs[22], index_switch.inputs[24])
			#group_input.Cr -> index_switch.24
			color_element.links.new(group_input.outputs[23], index_switch.inputs[25])
			#group_input.Mn -> index_switch.25
			color_element.links.new(group_input.outputs[24], index_switch.inputs[26])
			#group_input.Fe -> index_switch.26
			color_element.links.new(group_input.outputs[25], index_switch.inputs[27])
			#group_input.Co -> index_switch.27
			color_element.links.new(group_input.outputs[26], index_switch.inputs[28])
			#group_input.Ni -> index_switch.28
			color_element.links.new(group_input.outputs[27], index_switch.inputs[29])
			#group_input.Cu -> index_switch.29
			color_element.links.new(group_input.outputs[28], index_switch.inputs[30])
			#group_input.Zn -> index_switch.30
			color_element.links.new(group_input.outputs[29], index_switch.inputs[31])
			#group_input.Ga -> index_switch.31
			color_element.links.new(group_input.outputs[30], index_switch.inputs[32])
			#group_input.Ge -> index_switch.32
			color_element.links.new(group_input.outputs[31], index_switch.inputs[33])
			#group_input.As -> index_switch.33
			color_element.links.new(group_input.outputs[32], index_switch.inputs[34])
			#group_input.Se -> index_switch.34
			color_element.links.new(group_input.outputs[33], index_switch.inputs[35])
			#group_input.Br -> index_switch.35
			color_element.links.new(group_input.outputs[34], index_switch.inputs[36])
			#group_input.Kr -> index_switch.36
			color_element.links.new(group_input.outputs[35], index_switch.inputs[37])
			#group_input.Rb -> index_switch.37
			color_element.links.new(group_input.outputs[36], index_switch.inputs[38])
			#group_input.Sr -> index_switch.38
			color_element.links.new(group_input.outputs[37], index_switch.inputs[39])
			#group_input.Y -> index_switch.39
			color_element.links.new(group_input.outputs[38], index_switch.inputs[40])
			#group_input.Zr -> index_switch.40
			color_element.links.new(group_input.outputs[39], index_switch.inputs[41])
			#group_input.Nb -> index_switch.41
			color_element.links.new(group_input.outputs[40], index_switch.inputs[42])
			#group_input.Mo -> index_switch.42
			color_element.links.new(group_input.outputs[41], index_switch.inputs[43])
			#group_input.Tc -> index_switch.43
			color_element.links.new(group_input.outputs[42], index_switch.inputs[44])
			#group_input.Ru -> index_switch.44
			color_element.links.new(group_input.outputs[43], index_switch.inputs[45])
			#group_input.Rh -> index_switch.45
			color_element.links.new(group_input.outputs[44], index_switch.inputs[46])
			#group_input.Pd -> index_switch.46
			color_element.links.new(group_input.outputs[45], index_switch.inputs[47])
			#group_input.Ag -> index_switch.47
			color_element.links.new(group_input.outputs[46], index_switch.inputs[48])
			#group_input.Cd -> index_switch.48
			color_element.links.new(group_input.outputs[47], index_switch.inputs[49])
			#group_input.In -> index_switch.49
			color_element.links.new(group_input.outputs[48], index_switch.inputs[50])
			#group_input.Sn -> index_switch.50
			color_element.links.new(group_input.outputs[49], index_switch.inputs[51])
			#group_input.Sb -> index_switch.51
			color_element.links.new(group_input.outputs[50], index_switch.inputs[52])
			#group_input.Te -> index_switch.52
			color_element.links.new(group_input.outputs[51], index_switch.inputs[53])
			#group_input.I -> index_switch.53
			color_element.links.new(group_input.outputs[52], index_switch.inputs[54])
			#group_input.Xe -> index_switch.54
			color_element.links.new(group_input.outputs[53], index_switch.inputs[55])
			#group_input.Cs -> index_switch.55
			color_element.links.new(group_input.outputs[54], index_switch.inputs[56])
			#group_input.Ba -> index_switch.56
			color_element.links.new(group_input.outputs[55], index_switch.inputs[57])
			#group_input.La -> index_switch.57
			color_element.links.new(group_input.outputs[56], index_switch.inputs[58])
			#group_input.Ce -> index_switch.58
			color_element.links.new(group_input.outputs[57], index_switch.inputs[59])
			#group_input.Pr -> index_switch.59
			color_element.links.new(group_input.outputs[58], index_switch.inputs[60])
			#group_input.Nd -> index_switch.60
			color_element.links.new(group_input.outputs[59], index_switch.inputs[61])
			#group_input.Pm -> index_switch.61
			color_element.links.new(group_input.outputs[60], index_switch.inputs[62])
			#group_input.Sm -> index_switch.62
			color_element.links.new(group_input.outputs[61], index_switch.inputs[63])
			#group_input.Eu -> index_switch.63
			color_element.links.new(group_input.outputs[62], index_switch.inputs[64])
			#group_input.Gd -> index_switch.64
			color_element.links.new(group_input.outputs[63], index_switch.inputs[65])
			#group_input.Tb -> index_switch.65
			color_element.links.new(group_input.outputs[64], index_switch.inputs[66])
			#group_input.Dy -> index_switch.66
			color_element.links.new(group_input.outputs[65], index_switch.inputs[67])
			#group_input.Ho -> index_switch.67
			color_element.links.new(group_input.outputs[66], index_switch.inputs[68])
			#group_input.Er -> index_switch.68
			color_element.links.new(group_input.outputs[67], index_switch.inputs[69])
			#group_input.Tm -> index_switch.69
			color_element.links.new(group_input.outputs[68], index_switch.inputs[70])
			#group_input.Yb -> index_switch.70
			color_element.links.new(group_input.outputs[69], index_switch.inputs[71])
			#group_input.Lu -> index_switch.71
			color_element.links.new(group_input.outputs[70], index_switch.inputs[72])
			#group_input.Hf -> index_switch.72
			color_element.links.new(group_input.outputs[71], index_switch.inputs[73])
			#group_input.Ta -> index_switch.73
			color_element.links.new(group_input.outputs[72], index_switch.inputs[74])
			#group_input.W -> index_switch.74
			color_element.links.new(group_input.outputs[73], index_switch.inputs[75])
			#group_input.Re -> index_switch.75
			color_element.links.new(group_input.outputs[74], index_switch.inputs[76])
			#group_input.Os -> index_switch.76
			color_element.links.new(group_input.outputs[75], index_switch.inputs[77])
			#group_input.Ir -> index_switch.77
			color_element.links.new(group_input.outputs[76], index_switch.inputs[78])
			#group_input.Pt -> index_switch.78
			color_element.links.new(group_input.outputs[77], index_switch.inputs[79])
			#group_input.Au -> index_switch.79
			color_element.links.new(group_input.outputs[78], index_switch.inputs[80])
			#group_input.Hg -> index_switch.80
			color_element.links.new(group_input.outputs[79], index_switch.inputs[81])
			#index_switch.Output -> group_output.Color
			color_element.links.new(index_switch.outputs[0], group_output.inputs[0])
			return color_element

		color_element = color_element_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Color Element", type = 'NODES')
		mod.node_group = color_element
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Color_Element.bl_idname)
			
def register():
	bpy.utils.register_class(Color_Element)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Color_Element)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
