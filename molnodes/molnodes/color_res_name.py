bl_info = {
	"name" : "Color Res Name",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Color_Res_Name(bpy.types.Operator):
	bl_idname = "node.color_res_name"
	bl_label = "Color Res Name"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize between_integer node group
		def between_integer_node_group():
			between_integer = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Between Integer")

			between_integer.color_tag = 'CONVERTER'
			between_integer.description = ""

			
			#between_integer interface
			#Socket Boolean
			boolean_socket = between_integer.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			boolean_socket.default_value = False
			boolean_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket = between_integer.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketInt')
			value_socket.default_value = 0
			value_socket.min_value = -2147483648
			value_socket.max_value = 2147483647
			value_socket.subtype = 'NONE'
			value_socket.attribute_domain = 'POINT'
			
			#Socket Lower
			lower_socket = between_integer.interface.new_socket(name = "Lower", in_out='INPUT', socket_type = 'NodeSocketInt')
			lower_socket.default_value = 0
			lower_socket.min_value = -2147483648
			lower_socket.max_value = 2147483647
			lower_socket.subtype = 'NONE'
			lower_socket.attribute_domain = 'POINT'
			
			#Socket Upper
			upper_socket = between_integer.interface.new_socket(name = "Upper", in_out='INPUT', socket_type = 'NodeSocketInt')
			upper_socket.default_value = 19
			upper_socket.min_value = -2147483648
			upper_socket.max_value = 2147483647
			upper_socket.subtype = 'NONE'
			upper_socket.attribute_domain = 'POINT'
			
			
			#initialize between_integer nodes
			#node Group Output
			group_output = between_integer.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = between_integer.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Compare
			compare = between_integer.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'LESS_EQUAL'
			
			#node Compare.001
			compare_001 = between_integer.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'INT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'GREATER_EQUAL'
			
			#node Boolean Math
			boolean_math = between_integer.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'AND'
			
			
			
			
			#Set locations
			group_output.location = (270.0, 0.0)
			group_input.location = (-280.0, 0.0)
			compare.location = (-80.0, -80.0)
			compare_001.location = (-80.0, 80.0)
			boolean_math.location = (80.0, 80.0)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			
			#initialize between_integer links
			#compare.Result -> boolean_math.Boolean
			between_integer.links.new(compare.outputs[0], boolean_math.inputs[1])
			#compare_001.Result -> boolean_math.Boolean
			between_integer.links.new(compare_001.outputs[0], boolean_math.inputs[0])
			#group_input.Value -> compare.A
			between_integer.links.new(group_input.outputs[0], compare.inputs[2])
			#group_input.Value -> compare_001.A
			between_integer.links.new(group_input.outputs[0], compare_001.inputs[2])
			#boolean_math.Boolean -> group_output.Boolean
			between_integer.links.new(boolean_math.outputs[0], group_output.inputs[0])
			#group_input.Lower -> compare_001.B
			between_integer.links.new(group_input.outputs[1], compare_001.inputs[3])
			#group_input.Upper -> compare.B
			between_integer.links.new(group_input.outputs[2], compare.inputs[3])
			return between_integer

		between_integer = between_integer_node_group()

		#initialize color_res_name node group
		def color_res_name_node_group():
			color_res_name = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Color Res Name")

			color_res_name.color_tag = 'COLOR'
			color_res_name.description = ""

			
			#color_res_name interface
			#Socket Color
			color_socket = color_res_name.interface.new_socket(name = "Color", in_out='OUTPUT', socket_type = 'NodeSocketColor')
			color_socket.default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
			color_socket.attribute_domain = 'POINT'
			
			#Panel Peptide
			peptide_panel = color_res_name.interface.new_panel("Peptide", default_closed=True)
			#Socket ALA
			ala_socket = color_res_name.interface.new_socket(name = "ALA", in_out='INPUT', socket_type = 'NodeSocketColor', parent = peptide_panel)
			ala_socket.default_value = (0.0, 0.0, 0.0, 1.0)
			ala_socket.attribute_domain = 'POINT'
			
			#Socket ARG
			arg_socket = color_res_name.interface.new_socket(name = "ARG", in_out='INPUT', socket_type = 'NodeSocketColor', parent = peptide_panel)
			arg_socket.default_value = (0.09462588280439377, 0.09462588280439377, 0.09462588280439377, 1.0)
			arg_socket.attribute_domain = 'POINT'
			
			#Socket ASN
			asn_socket = color_res_name.interface.new_socket(name = "ASN", in_out='INPUT', socket_type = 'NodeSocketColor', parent = peptide_panel)
			asn_socket.default_value = (0.11411894112825394, 0.22025452554225922, 0.18504783511161804, 1.0)
			asn_socket.attribute_domain = 'POINT'
			
			#Socket ASP
			asp_socket = color_res_name.interface.new_socket(name = "ASP", in_out='INPUT', socket_type = 'NodeSocketColor', parent = peptide_panel)
			asp_socket.default_value = (0.1408783346414566, 0.33738043904304504, 0.42922618985176086, 1.0)
			asp_socket.attribute_domain = 'POINT'
			
			#Socket CYS
			cys_socket = color_res_name.interface.new_socket(name = "CYS", in_out='INPUT', socket_type = 'NodeSocketColor', parent = peptide_panel)
			cys_socket.default_value = (0.28100982308387756, 0.15101823210716248, 0.10579018294811249, 1.0)
			cys_socket.attribute_domain = 'POINT'
			
			#Socket GLU
			glu_socket = color_res_name.interface.new_socket(name = "GLU", in_out='INPUT', socket_type = 'NodeSocketColor', parent = peptide_panel)
			glu_socket.default_value = (0.20190106332302094, 0.20190106332302094, 0.20190106332302094, 1.0)
			glu_socket.attribute_domain = 'POINT'
			
			#Socket GLN
			gln_socket = color_res_name.interface.new_socket(name = "GLN", in_out='INPUT', socket_type = 'NodeSocketColor', parent = peptide_panel)
			gln_socket.default_value = (0.12770424783229828, 0.20473986864089966, 0.8000000715255737, 1.0)
			gln_socket.attribute_domain = 'POINT'
			
			#Socket GLY
			gly_socket = color_res_name.interface.new_socket(name = "GLY", in_out='INPUT', socket_type = 'NodeSocketColor', parent = peptide_panel)
			gly_socket.default_value = (0.8000000715255737, 0.0689556673169136, 0.06778784096240997, 1.0)
			gly_socket.attribute_domain = 'POINT'
			
			#Socket HIS
			his_socket = color_res_name.interface.new_socket(name = "HIS", in_out='INPUT', socket_type = 'NodeSocketColor', parent = peptide_panel)
			his_socket.default_value = (0.18364381790161133, 0.761273205280304, 0.3411029577255249, 1.0)
			his_socket.attribute_domain = 'POINT'
			
			#Socket ILE
			ile_socket = color_res_name.interface.new_socket(name = "ILE", in_out='INPUT', socket_type = 'NodeSocketColor', parent = peptide_panel)
			ile_socket.default_value = (0.09119512140750885, 0.6266628503799438, 0.12943390011787415, 1.0)
			ile_socket.attribute_domain = 'POINT'
			
			#Socket LEU
			leu_socket = color_res_name.interface.new_socket(name = "LEU", in_out='INPUT', socket_type = 'NodeSocketColor', parent = peptide_panel)
			leu_socket.default_value = (0.0366930328309536, 0.17026513814926147, 0.41093894839286804, 1.0)
			leu_socket.attribute_domain = 'POINT'
			
			#Socket LYS
			lys_socket = color_res_name.interface.new_socket(name = "LYS", in_out='INPUT', socket_type = 'NodeSocketColor', parent = peptide_panel)
			lys_socket.default_value = (0.052218127995729446, 0.052218127995729446, 0.052218127995729446, 1.0)
			lys_socket.attribute_domain = 'POINT'
			
			#Socket MET
			met_socket = color_res_name.interface.new_socket(name = "MET", in_out='INPUT', socket_type = 'NodeSocketColor', parent = peptide_panel)
			met_socket.default_value = (0.527719259262085, 0.45242294669151306, 0.49789106845855713, 1.0)
			met_socket.attribute_domain = 'POINT'
			
			#Socket PHE
			phe_socket = color_res_name.interface.new_socket(name = "PHE", in_out='INPUT', socket_type = 'NodeSocketColor', parent = peptide_panel)
			phe_socket.default_value = (0.3588410019874573, 0.3051301836967468, 0.09418508410453796, 1.0)
			phe_socket.attribute_domain = 'POINT'
			
			#Socket PRO
			pro_socket = color_res_name.interface.new_socket(name = "PRO", in_out='INPUT', socket_type = 'NodeSocketColor', parent = peptide_panel)
			pro_socket.default_value = (0.8000000715255737, 0.1718127280473709, 0.525249719619751, 1.0)
			pro_socket.attribute_domain = 'POINT'
			
			#Socket SER
			ser_socket = color_res_name.interface.new_socket(name = "SER", in_out='INPUT', socket_type = 'NodeSocketColor', parent = peptide_panel)
			ser_socket.default_value = (0.8000000715255737, 0.7220579385757446, 0.051990706473588943, 1.0)
			ser_socket.attribute_domain = 'POINT'
			
			#Socket THR
			thr_socket = color_res_name.interface.new_socket(name = "THR", in_out='INPUT', socket_type = 'NodeSocketColor', parent = peptide_panel)
			thr_socket.default_value = (0.10636822879314423, 1.0, 0.11561121791601181, 1.0)
			thr_socket.attribute_domain = 'POINT'
			
			#Socket TRP
			trp_socket = color_res_name.interface.new_socket(name = "TRP", in_out='INPUT', socket_type = 'NodeSocketColor', parent = peptide_panel)
			trp_socket.default_value = (0.527719259262085, 0.1365669220685959, 0.4106137752532959, 1.0)
			trp_socket.attribute_domain = 'POINT'
			
			#Socket TYR
			tyr_socket = color_res_name.interface.new_socket(name = "TYR", in_out='INPUT', socket_type = 'NodeSocketColor', parent = peptide_panel)
			tyr_socket.default_value = (0.08601968735456467, 0.36478209495544434, 0.6382719874382019, 1.0)
			tyr_socket.attribute_domain = 'POINT'
			
			#Socket VAL
			val_socket = color_res_name.interface.new_socket(name = "VAL", in_out='INPUT', socket_type = 'NodeSocketColor', parent = peptide_panel)
			val_socket.default_value = (0.06929229199886322, 0.15196387469768524, 0.5596004128456116, 1.0)
			val_socket.attribute_domain = 'POINT'
			
			
			#Panel Nucleic
			nucleic_panel = color_res_name.interface.new_panel("Nucleic", default_closed=True)
			#Socket A
			a_socket = color_res_name.interface.new_socket(name = "A", in_out='INPUT', socket_type = 'NodeSocketColor', parent = nucleic_panel)
			a_socket.default_value = (0.2737779915332794, 0.5478230118751526, 0.800000011920929, 1.0)
			a_socket.attribute_domain = 'POINT'
			
			#Socket C
			c_socket = color_res_name.interface.new_socket(name = "C", in_out='INPUT', socket_type = 'NodeSocketColor', parent = nucleic_panel)
			c_socket.default_value = (0.2945820093154907, 0.800000011920929, 0.18778899312019348, 1.0)
			c_socket.attribute_domain = 'POINT'
			
			#Socket G
			g_socket = color_res_name.interface.new_socket(name = "G", in_out='INPUT', socket_type = 'NodeSocketColor', parent = nucleic_panel)
			g_socket.default_value = (0.8500000238418579, 0.2514023780822754, 0.17788057029247284, 1.0)
			g_socket.attribute_domain = 'POINT'
			
			#Socket T
			t_socket = color_res_name.interface.new_socket(name = "T", in_out='INPUT', socket_type = 'NodeSocketColor', parent = nucleic_panel)
			t_socket.default_value = (0.800000011920929, 0.269802987575531, 0.5268980264663696, 1.0)
			t_socket.attribute_domain = 'POINT'
			
			#Socket rA
			ra_socket = color_res_name.interface.new_socket(name = "rA", in_out='INPUT', socket_type = 'NodeSocketColor', parent = nucleic_panel)
			ra_socket.default_value = (0.2737779915332794, 0.5478230118751526, 0.800000011920929, 1.0)
			ra_socket.attribute_domain = 'POINT'
			
			#Socket rC
			rc_socket = color_res_name.interface.new_socket(name = "rC", in_out='INPUT', socket_type = 'NodeSocketColor', parent = nucleic_panel)
			rc_socket.default_value = (0.2945820093154907, 0.800000011920929, 0.18778899312019348, 1.0)
			rc_socket.attribute_domain = 'POINT'
			
			#Socket rG
			rg_socket = color_res_name.interface.new_socket(name = "rG", in_out='INPUT', socket_type = 'NodeSocketColor', parent = nucleic_panel)
			rg_socket.default_value = (0.8500000238418579, 0.2514023780822754, 0.17788057029247284, 1.0)
			rg_socket.attribute_domain = 'POINT'
			
			#Socket rU
			ru_socket = color_res_name.interface.new_socket(name = "rU", in_out='INPUT', socket_type = 'NodeSocketColor', parent = nucleic_panel)
			ru_socket.default_value = (0.800000011920929, 0.269802987575531, 0.5268980264663696, 1.0)
			ru_socket.attribute_domain = 'POINT'
			
			
			
			#initialize color_res_name nodes
			#node Group Output
			group_output_1 = color_res_name.nodes.new("NodeGroupOutput")
			group_output_1.name = "Group Output"
			group_output_1.is_active_output = True
			
			#node Group Input
			group_input_1 = color_res_name.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			group_input_1.outputs[20].hide = True
			group_input_1.outputs[21].hide = True
			group_input_1.outputs[22].hide = True
			group_input_1.outputs[23].hide = True
			group_input_1.outputs[24].hide = True
			group_input_1.outputs[25].hide = True
			group_input_1.outputs[26].hide = True
			group_input_1.outputs[27].hide = True
			group_input_1.outputs[28].hide = True
			
			#node Named Attribute.001
			named_attribute_001 = color_res_name.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute_001.inputs[0].default_value = "Color"
			
			#node Named Attribute
			named_attribute = color_res_name.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'INT'
			#Name
			named_attribute.inputs[0].default_value = "res_name"
			
			#node Index Switch
			index_switch = color_res_name.nodes.new("GeometryNodeIndexSwitch")
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
			#Item_20
			index_switch.inputs[21].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
			#Item_21
			index_switch.inputs[22].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
			#Item_22
			index_switch.inputs[23].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
			#Item_23
			index_switch.inputs[24].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
			#Item_24
			index_switch.inputs[25].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
			#Item_25
			index_switch.inputs[26].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
			#Item_26
			index_switch.inputs[27].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
			#Item_27
			index_switch.inputs[28].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
			#Item_28
			index_switch.inputs[29].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
			#Item_29
			index_switch.inputs[30].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
			#Item_34
			index_switch.inputs[35].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
			#Item_35
			index_switch.inputs[36].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
			#Item_36
			index_switch.inputs[37].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
			#Item_37
			index_switch.inputs[38].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
			#Item_38
			index_switch.inputs[39].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
			#Item_39
			index_switch.inputs[40].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
			
			#node Switch
			switch = color_res_name.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'RGBA'
			
			#node Group
			group = color_res_name.nodes.new("GeometryNodeGroup")
			group.name = "Group"
			group.node_tree = between_integer
			#Socket_2
			group.inputs[1].default_value = 0
			#Socket_3
			group.inputs[2].default_value = 43
			
			#node Group Input.001
			group_input_001 = color_res_name.nodes.new("NodeGroupInput")
			group_input_001.name = "Group Input.001"
			group_input_001.outputs[0].hide = True
			group_input_001.outputs[1].hide = True
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
			group_input_001.outputs[28].hide = True
			
			
			
			
			#Set locations
			group_output_1.location = (-60.0, 440.0)
			group_input_1.location = (-800.0, 300.0)
			named_attribute_001.location = (-540.0, 460.0)
			named_attribute.location = (-800.0, 440.0)
			index_switch.location = (-540.0, 320.0)
			switch.location = (-360.0, 600.0)
			group.location = (-540.0, 600.0)
			group_input_001.location = (-800.0, -440.0)
			
			#Set dimensions
			group_output_1.width, group_output_1.height = 140.0, 100.0
			group_input_1.width, group_input_1.height = 140.0, 100.0
			named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 142.794921875, 100.0
			index_switch.width, index_switch.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			group.width, group.height = 140.0, 100.0
			group_input_001.width, group_input_001.height = 140.0, 100.0
			
			#initialize color_res_name links
			#named_attribute.Attribute -> index_switch.Index
			color_res_name.links.new(named_attribute.outputs[0], index_switch.inputs[0])
			#named_attribute_001.Attribute -> switch.False
			color_res_name.links.new(named_attribute_001.outputs[0], switch.inputs[1])
			#group.Boolean -> switch.Switch
			color_res_name.links.new(group.outputs[0], switch.inputs[0])
			#group_input_1.ALA -> index_switch.0
			color_res_name.links.new(group_input_1.outputs[0], index_switch.inputs[1])
			#group_input_1.ARG -> index_switch.1
			color_res_name.links.new(group_input_1.outputs[1], index_switch.inputs[2])
			#group_input_1.ASN -> index_switch.2
			color_res_name.links.new(group_input_1.outputs[2], index_switch.inputs[3])
			#group_input_1.ASP -> index_switch.3
			color_res_name.links.new(group_input_1.outputs[3], index_switch.inputs[4])
			#group_input_1.CYS -> index_switch.4
			color_res_name.links.new(group_input_1.outputs[4], index_switch.inputs[5])
			#group_input_1.GLU -> index_switch.5
			color_res_name.links.new(group_input_1.outputs[5], index_switch.inputs[6])
			#group_input_1.GLN -> index_switch.6
			color_res_name.links.new(group_input_1.outputs[6], index_switch.inputs[7])
			#group_input_1.GLY -> index_switch.7
			color_res_name.links.new(group_input_1.outputs[7], index_switch.inputs[8])
			#group_input_1.HIS -> index_switch.8
			color_res_name.links.new(group_input_1.outputs[8], index_switch.inputs[9])
			#group_input_1.ILE -> index_switch.9
			color_res_name.links.new(group_input_1.outputs[9], index_switch.inputs[10])
			#group_input_1.LEU -> index_switch.10
			color_res_name.links.new(group_input_1.outputs[10], index_switch.inputs[11])
			#group_input_1.LYS -> index_switch.11
			color_res_name.links.new(group_input_1.outputs[11], index_switch.inputs[12])
			#group_input_1.MET -> index_switch.12
			color_res_name.links.new(group_input_1.outputs[12], index_switch.inputs[13])
			#group_input_1.PHE -> index_switch.13
			color_res_name.links.new(group_input_1.outputs[13], index_switch.inputs[14])
			#group_input_1.PRO -> index_switch.14
			color_res_name.links.new(group_input_1.outputs[14], index_switch.inputs[15])
			#group_input_1.SER -> index_switch.15
			color_res_name.links.new(group_input_1.outputs[15], index_switch.inputs[16])
			#group_input_1.THR -> index_switch.16
			color_res_name.links.new(group_input_1.outputs[16], index_switch.inputs[17])
			#group_input_1.TRP -> index_switch.17
			color_res_name.links.new(group_input_1.outputs[17], index_switch.inputs[18])
			#group_input_1.TYR -> index_switch.18
			color_res_name.links.new(group_input_1.outputs[18], index_switch.inputs[19])
			#group_input_1.VAL -> index_switch.19
			color_res_name.links.new(group_input_1.outputs[19], index_switch.inputs[20])
			#named_attribute.Attribute -> group.Value
			color_res_name.links.new(named_attribute.outputs[0], group.inputs[0])
			#switch.Output -> group_output_1.Color
			color_res_name.links.new(switch.outputs[0], group_output_1.inputs[0])
			#group_input_001.A -> index_switch.30
			color_res_name.links.new(group_input_001.outputs[20], index_switch.inputs[31])
			#group_input_001.C -> index_switch.31
			color_res_name.links.new(group_input_001.outputs[21], index_switch.inputs[32])
			#group_input_001.G -> index_switch.32
			color_res_name.links.new(group_input_001.outputs[22], index_switch.inputs[33])
			#group_input_001.T -> index_switch.33
			color_res_name.links.new(group_input_001.outputs[23], index_switch.inputs[34])
			#group_input_001.rA -> index_switch.40
			color_res_name.links.new(group_input_001.outputs[24], index_switch.inputs[41])
			#group_input_001.rC -> index_switch.41
			color_res_name.links.new(group_input_001.outputs[25], index_switch.inputs[42])
			#group_input_001.rG -> index_switch.42
			color_res_name.links.new(group_input_001.outputs[26], index_switch.inputs[43])
			#group_input_001.rU -> index_switch.43
			color_res_name.links.new(group_input_001.outputs[27], index_switch.inputs[44])
			#index_switch.Output -> switch.True
			color_res_name.links.new(index_switch.outputs[0], switch.inputs[2])
			return color_res_name

		color_res_name = color_res_name_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Color Res Name", type = 'NODES')
		mod.node_group = color_res_name
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Color_Res_Name.bl_idname)
			
def register():
	bpy.utils.register_class(Color_Res_Name)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Color_Res_Name)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
