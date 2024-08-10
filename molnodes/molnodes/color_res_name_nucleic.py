bl_info = {
	"name" : "Color Res Name Nucleic",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Color_Res_Name_Nucleic(bpy.types.Operator):
	bl_idname = "node.color_res_name_nucleic"
	bl_label = "Color Res Name Nucleic"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize color_res_name_nucleic node group
		def color_res_name_nucleic_node_group():
			color_res_name_nucleic = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Color Res Name Nucleic")

			color_res_name_nucleic.color_tag = 'NONE'
			color_res_name_nucleic.description = ""

			
			#color_res_name_nucleic interface
			#Socket Color
			color_socket = color_res_name_nucleic.interface.new_socket(name = "Color", in_out='OUTPUT', socket_type = 'NodeSocketColor')
			color_socket.attribute_domain = 'POINT'
			
			#Socket A
			a_socket = color_res_name_nucleic.interface.new_socket(name = "A", in_out='INPUT', socket_type = 'NodeSocketColor')
			a_socket.attribute_domain = 'POINT'
			
			#Socket C
			c_socket = color_res_name_nucleic.interface.new_socket(name = "C", in_out='INPUT', socket_type = 'NodeSocketColor')
			c_socket.attribute_domain = 'POINT'
			
			#Socket G
			g_socket = color_res_name_nucleic.interface.new_socket(name = "G", in_out='INPUT', socket_type = 'NodeSocketColor')
			g_socket.attribute_domain = 'POINT'
			
			#Socket T / U
			t___u_socket = color_res_name_nucleic.interface.new_socket(name = "T / U", in_out='INPUT', socket_type = 'NodeSocketColor')
			t___u_socket.attribute_domain = 'POINT'
			
			
			#initialize color_res_name_nucleic nodes
			#node Group Output
			group_output = color_res_name_nucleic.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Switch.004
			switch_004 = color_res_name_nucleic.nodes.new("GeometryNodeSwitch")
			switch_004.name = "Switch.004"
			switch_004.input_type = 'RGBA'
			
			#node Switch.001
			switch_001 = color_res_name_nucleic.nodes.new("GeometryNodeSwitch")
			switch_001.name = "Switch.001"
			switch_001.input_type = 'RGBA'
			
			#node Switch.002
			switch_002 = color_res_name_nucleic.nodes.new("GeometryNodeSwitch")
			switch_002.name = "Switch.002"
			switch_002.input_type = 'RGBA'
			
			#node Switch.003
			switch_003 = color_res_name_nucleic.nodes.new("GeometryNodeSwitch")
			switch_003.name = "Switch.003"
			switch_003.input_type = 'RGBA'
			
			#node Boolean Math.017
			boolean_math_017 = color_res_name_nucleic.nodes.new("FunctionNodeBooleanMath")
			boolean_math_017.name = "Boolean Math.017"
			boolean_math_017.operation = 'OR'
			
			#node Compare.013
			compare_013 = color_res_name_nucleic.nodes.new("FunctionNodeCompare")
			compare_013.name = "Compare.013"
			compare_013.data_type = 'INT'
			compare_013.mode = 'ELEMENT'
			compare_013.operation = 'EQUAL'
			#B_INT
			compare_013.inputs[3].default_value = 33
			
			#node Compare.020
			compare_020 = color_res_name_nucleic.nodes.new("FunctionNodeCompare")
			compare_020.name = "Compare.020"
			compare_020.data_type = 'INT'
			compare_020.mode = 'ELEMENT'
			compare_020.operation = 'EQUAL'
			#B_INT
			compare_020.inputs[3].default_value = 43
			
			#node Boolean Math.016
			boolean_math_016 = color_res_name_nucleic.nodes.new("FunctionNodeBooleanMath")
			boolean_math_016.name = "Boolean Math.016"
			boolean_math_016.operation = 'OR'
			
			#node Compare.019
			compare_019 = color_res_name_nucleic.nodes.new("FunctionNodeCompare")
			compare_019.name = "Compare.019"
			compare_019.data_type = 'INT'
			compare_019.mode = 'ELEMENT'
			compare_019.operation = 'EQUAL'
			#B_INT
			compare_019.inputs[3].default_value = 42
			
			#node Boolean Math.015
			boolean_math_015 = color_res_name_nucleic.nodes.new("FunctionNodeBooleanMath")
			boolean_math_015.name = "Boolean Math.015"
			boolean_math_015.operation = 'OR'
			
			#node Compare.018
			compare_018 = color_res_name_nucleic.nodes.new("FunctionNodeCompare")
			compare_018.name = "Compare.018"
			compare_018.data_type = 'INT'
			compare_018.mode = 'ELEMENT'
			compare_018.operation = 'EQUAL'
			#B_INT
			compare_018.inputs[3].default_value = 41
			
			#node Boolean Math.014
			boolean_math_014 = color_res_name_nucleic.nodes.new("FunctionNodeBooleanMath")
			boolean_math_014.name = "Boolean Math.014"
			boolean_math_014.operation = 'OR'
			
			#node Compare.017
			compare_017 = color_res_name_nucleic.nodes.new("FunctionNodeCompare")
			compare_017.name = "Compare.017"
			compare_017.data_type = 'INT'
			compare_017.mode = 'ELEMENT'
			compare_017.operation = 'EQUAL'
			#B_INT
			compare_017.inputs[3].default_value = 40
			
			#node Compare.010
			compare_010 = color_res_name_nucleic.nodes.new("FunctionNodeCompare")
			compare_010.name = "Compare.010"
			compare_010.data_type = 'INT'
			compare_010.mode = 'ELEMENT'
			compare_010.operation = 'EQUAL'
			#B_INT
			compare_010.inputs[3].default_value = 30
			
			#node Compare.012
			compare_012 = color_res_name_nucleic.nodes.new("FunctionNodeCompare")
			compare_012.name = "Compare.012"
			compare_012.data_type = 'INT'
			compare_012.mode = 'ELEMENT'
			compare_012.operation = 'EQUAL'
			#B_INT
			compare_012.inputs[3].default_value = 32
			
			#node Compare.011
			compare_011 = color_res_name_nucleic.nodes.new("FunctionNodeCompare")
			compare_011.name = "Compare.011"
			compare_011.data_type = 'INT'
			compare_011.mode = 'ELEMENT'
			compare_011.operation = 'EQUAL'
			#B_INT
			compare_011.inputs[3].default_value = 31
			
			#node Named Attribute.009
			named_attribute_009 = color_res_name_nucleic.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_009.name = "Named Attribute.009"
			named_attribute_009.data_type = 'INT'
			#Name
			named_attribute_009.inputs[0].default_value = "res_name"
			
			#node Group Input
			group_input = color_res_name_nucleic.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Named Attribute
			named_attribute = color_res_name_nucleic.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute.inputs[0].default_value = "Color"
			
			
			
			
			#Set locations
			group_output.location = (643.794677734375, 0.0)
			switch_004.location = (453.7947082519531, -246.83526611328125)
			switch_001.location = (286.0763854980469, -248.0322265625)
			switch_002.location = (99.95280456542969, -253.164794921875)
			switch_003.location = (-80.04719543457031, -253.164794921875)
			boolean_math_017.location = (293.7947082519531, 253.16473388671875)
			compare_013.location = (293.7947082519531, -66.83526611328125)
			compare_020.location = (293.7947082519531, 113.16473388671875)
			boolean_math_016.location = (93.79472351074219, 253.16473388671875)
			compare_019.location = (93.79472351074219, 113.16473388671875)
			boolean_math_015.location = (-86.20527648925781, 253.16473388671875)
			compare_018.location = (-86.20527648925781, 113.16473388671875)
			boolean_math_014.location = (-266.20526123046875, 253.16473388671875)
			compare_017.location = (-266.20526123046875, 113.16473388671875)
			compare_010.location = (-266.20526123046875, -66.83526611328125)
			compare_012.location = (106.20527648925781, -70.5985107421875)
			compare_011.location = (-73.79472351074219, -70.5985107421875)
			named_attribute_009.location = (-453.7947082519531, -70.5985107421875)
			group_input.location = (-460.0, -440.0)
			named_attribute.location = (-460.0, -300.0)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			switch_004.width, switch_004.height = 140.0, 100.0
			switch_001.width, switch_001.height = 140.0, 100.0
			switch_002.width, switch_002.height = 140.0, 100.0
			switch_003.width, switch_003.height = 140.0, 100.0
			boolean_math_017.width, boolean_math_017.height = 140.0, 100.0
			compare_013.width, compare_013.height = 140.0, 100.0
			compare_020.width, compare_020.height = 140.0, 100.0
			boolean_math_016.width, boolean_math_016.height = 140.0, 100.0
			compare_019.width, compare_019.height = 140.0, 100.0
			boolean_math_015.width, boolean_math_015.height = 140.0, 100.0
			compare_018.width, compare_018.height = 140.0, 100.0
			boolean_math_014.width, boolean_math_014.height = 140.0, 100.0
			compare_017.width, compare_017.height = 140.0, 100.0
			compare_010.width, compare_010.height = 140.0, 100.0
			compare_012.width, compare_012.height = 140.0, 100.0
			compare_011.width, compare_011.height = 140.0, 100.0
			named_attribute_009.width, named_attribute_009.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			
			#initialize color_res_name_nucleic links
			#switch_003.Output -> switch_002.False
			color_res_name_nucleic.links.new(switch_003.outputs[0], switch_002.inputs[1])
			#named_attribute_009.Attribute -> compare_011.A
			color_res_name_nucleic.links.new(named_attribute_009.outputs[0], compare_011.inputs[2])
			#switch_002.Output -> switch_001.False
			color_res_name_nucleic.links.new(switch_002.outputs[0], switch_001.inputs[1])
			#boolean_math_015.Boolean -> switch_002.Switch
			color_res_name_nucleic.links.new(boolean_math_015.outputs[0], switch_002.inputs[0])
			#named_attribute_009.Attribute -> compare_019.A
			color_res_name_nucleic.links.new(named_attribute_009.outputs[0], compare_019.inputs[2])
			#compare_011.Result -> boolean_math_015.Boolean
			color_res_name_nucleic.links.new(compare_011.outputs[0], boolean_math_015.inputs[1])
			#compare_018.Result -> boolean_math_015.Boolean
			color_res_name_nucleic.links.new(compare_018.outputs[0], boolean_math_015.inputs[0])
			#compare_013.Result -> boolean_math_017.Boolean
			color_res_name_nucleic.links.new(compare_013.outputs[0], boolean_math_017.inputs[1])
			#named_attribute_009.Attribute -> compare_018.A
			color_res_name_nucleic.links.new(named_attribute_009.outputs[0], compare_018.inputs[2])
			#boolean_math_014.Boolean -> switch_003.Switch
			color_res_name_nucleic.links.new(boolean_math_014.outputs[0], switch_003.inputs[0])
			#compare_010.Result -> boolean_math_014.Boolean
			color_res_name_nucleic.links.new(compare_010.outputs[0], boolean_math_014.inputs[1])
			#named_attribute_009.Attribute -> compare_012.A
			color_res_name_nucleic.links.new(named_attribute_009.outputs[0], compare_012.inputs[2])
			#compare_017.Result -> boolean_math_014.Boolean
			color_res_name_nucleic.links.new(compare_017.outputs[0], boolean_math_014.inputs[0])
			#named_attribute_009.Attribute -> compare_017.A
			color_res_name_nucleic.links.new(named_attribute_009.outputs[0], compare_017.inputs[2])
			#named_attribute_009.Attribute -> compare_010.A
			color_res_name_nucleic.links.new(named_attribute_009.outputs[0], compare_010.inputs[2])
			#named_attribute_009.Attribute -> compare_013.A
			color_res_name_nucleic.links.new(named_attribute_009.outputs[0], compare_013.inputs[2])
			#switch_001.Output -> switch_004.False
			color_res_name_nucleic.links.new(switch_001.outputs[0], switch_004.inputs[1])
			#compare_020.Result -> boolean_math_017.Boolean
			color_res_name_nucleic.links.new(compare_020.outputs[0], boolean_math_017.inputs[0])
			#named_attribute_009.Attribute -> compare_020.A
			color_res_name_nucleic.links.new(named_attribute_009.outputs[0], compare_020.inputs[2])
			#compare_019.Result -> boolean_math_016.Boolean
			color_res_name_nucleic.links.new(compare_019.outputs[0], boolean_math_016.inputs[0])
			#boolean_math_016.Boolean -> switch_001.Switch
			color_res_name_nucleic.links.new(boolean_math_016.outputs[0], switch_001.inputs[0])
			#compare_012.Result -> boolean_math_016.Boolean
			color_res_name_nucleic.links.new(compare_012.outputs[0], boolean_math_016.inputs[1])
			#boolean_math_017.Boolean -> switch_004.Switch
			color_res_name_nucleic.links.new(boolean_math_017.outputs[0], switch_004.inputs[0])
			#switch_004.Output -> group_output.Color
			color_res_name_nucleic.links.new(switch_004.outputs[0], group_output.inputs[0])
			#group_input.A -> switch_003.True
			color_res_name_nucleic.links.new(group_input.outputs[0], switch_003.inputs[2])
			#group_input.C -> switch_002.True
			color_res_name_nucleic.links.new(group_input.outputs[1], switch_002.inputs[2])
			#group_input.G -> switch_001.True
			color_res_name_nucleic.links.new(group_input.outputs[2], switch_001.inputs[2])
			#group_input.T / U -> switch_004.True
			color_res_name_nucleic.links.new(group_input.outputs[3], switch_004.inputs[2])
			#named_attribute.Attribute -> switch_003.False
			color_res_name_nucleic.links.new(named_attribute.outputs[0], switch_003.inputs[1])
			return color_res_name_nucleic

		color_res_name_nucleic = color_res_name_nucleic_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Color Res Name Nucleic", type = 'NODES')
		mod.node_group = color_res_name_nucleic
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Color_Res_Name_Nucleic.bl_idname)
			
def register():
	bpy.utils.register_class(Color_Res_Name_Nucleic)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Color_Res_Name_Nucleic)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
