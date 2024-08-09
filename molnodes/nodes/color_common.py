bl_info = {
	"name" : "Color Common",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Color_Common(bpy.types.Operator):
	bl_idname = "node.color_common"
	bl_label = "Color Common"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize color_common node group
		def color_common_node_group():
			color_common = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Color Common")

			color_common.color_tag = 'COLOR'
			color_common.description = ""

			
			#color_common interface
			#Socket Color
			color_socket = color_common.interface.new_socket(name = "Color", in_out='OUTPUT', socket_type = 'NodeSocketColor')
			color_socket.attribute_domain = 'POINT'
			color_socket.description = "The output colors for the common elements"
			
			#Socket Hydrogen
			hydrogen_socket = color_common.interface.new_socket(name = "Hydrogen", in_out='INPUT', socket_type = 'NodeSocketColor')
			hydrogen_socket.attribute_domain = 'POINT'
			hydrogen_socket.description = "Color to set for the element Hydrogen"
			
			#Socket Carbon
			carbon_socket = color_common.interface.new_socket(name = "Carbon", in_out='INPUT', socket_type = 'NodeSocketColor')
			carbon_socket.attribute_domain = 'POINT'
			carbon_socket.description = "Color to set for the element Carbon"
			
			#Socket Nitrogen
			nitrogen_socket = color_common.interface.new_socket(name = "Nitrogen", in_out='INPUT', socket_type = 'NodeSocketColor')
			nitrogen_socket.attribute_domain = 'POINT'
			nitrogen_socket.description = "Color to set for the element Nitrogen"
			
			#Socket Oxygen
			oxygen_socket = color_common.interface.new_socket(name = "Oxygen", in_out='INPUT', socket_type = 'NodeSocketColor')
			oxygen_socket.attribute_domain = 'POINT'
			oxygen_socket.description = "Color to set for the element Oxygen"
			
			#Socket Phosphorous
			phosphorous_socket = color_common.interface.new_socket(name = "Phosphorous", in_out='INPUT', socket_type = 'NodeSocketColor')
			phosphorous_socket.attribute_domain = 'POINT'
			phosphorous_socket.description = "Color to set for the element Phosphorous"
			
			#Socket Sulfur
			sulfur_socket = color_common.interface.new_socket(name = "Sulfur", in_out='INPUT', socket_type = 'NodeSocketColor')
			sulfur_socket.attribute_domain = 'POINT'
			sulfur_socket.description = "Color to set for the element Sulfur"
			
			
			#initialize color_common nodes
			#node Reroute.001
			reroute_001 = color_common.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			#node Reroute.007
			reroute_007 = color_common.nodes.new("NodeReroute")
			reroute_007.name = "Reroute.007"
			#node Switch.002
			switch_002 = color_common.nodes.new("GeometryNodeSwitch")
			switch_002.name = "Switch.002"
			switch_002.input_type = 'RGBA'
			
			#node Reroute.009
			reroute_009 = color_common.nodes.new("NodeReroute")
			reroute_009.name = "Reroute.009"
			#node Reroute
			reroute = color_common.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Reroute.006
			reroute_006 = color_common.nodes.new("NodeReroute")
			reroute_006.name = "Reroute.006"
			#node Reroute.004
			reroute_004 = color_common.nodes.new("NodeReroute")
			reroute_004.name = "Reroute.004"
			#node Switch
			switch = color_common.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'RGBA'
			
			#node Switch.001
			switch_001 = color_common.nodes.new("GeometryNodeSwitch")
			switch_001.name = "Switch.001"
			switch_001.input_type = 'RGBA'
			
			#node Compare
			compare = color_common.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'EQUAL'
			#B_INT
			compare.inputs[3].default_value = 1
			
			#node Reroute.011
			reroute_011 = color_common.nodes.new("NodeReroute")
			reroute_011.name = "Reroute.011"
			#node Reroute.002
			reroute_002 = color_common.nodes.new("NodeReroute")
			reroute_002.name = "Reroute.002"
			#node Compare.001
			compare_001 = color_common.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'INT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'EQUAL'
			#B_INT
			compare_001.inputs[3].default_value = 6
			
			#node Reroute.003
			reroute_003 = color_common.nodes.new("NodeReroute")
			reroute_003.name = "Reroute.003"
			#node Compare.002
			compare_002 = color_common.nodes.new("FunctionNodeCompare")
			compare_002.name = "Compare.002"
			compare_002.data_type = 'INT'
			compare_002.mode = 'ELEMENT'
			compare_002.operation = 'EQUAL'
			#B_INT
			compare_002.inputs[3].default_value = 7
			
			#node Reroute.005
			reroute_005 = color_common.nodes.new("NodeReroute")
			reroute_005.name = "Reroute.005"
			#node Compare.003
			compare_003 = color_common.nodes.new("FunctionNodeCompare")
			compare_003.name = "Compare.003"
			compare_003.data_type = 'INT'
			compare_003.mode = 'ELEMENT'
			compare_003.operation = 'EQUAL'
			#B_INT
			compare_003.inputs[3].default_value = 8
			
			#node Reroute.012
			reroute_012 = color_common.nodes.new("NodeReroute")
			reroute_012.name = "Reroute.012"
			#node Reroute.013
			reroute_013 = color_common.nodes.new("NodeReroute")
			reroute_013.name = "Reroute.013"
			#node Reroute.014
			reroute_014 = color_common.nodes.new("NodeReroute")
			reroute_014.name = "Reroute.014"
			#node Switch.003
			switch_003 = color_common.nodes.new("GeometryNodeSwitch")
			switch_003.name = "Switch.003"
			switch_003.input_type = 'RGBA'
			
			#node Compare.004
			compare_004 = color_common.nodes.new("FunctionNodeCompare")
			compare_004.name = "Compare.004"
			compare_004.data_type = 'INT'
			compare_004.mode = 'ELEMENT'
			compare_004.operation = 'EQUAL'
			#B_INT
			compare_004.inputs[3].default_value = 15
			
			#node Compare.005
			compare_005 = color_common.nodes.new("FunctionNodeCompare")
			compare_005.name = "Compare.005"
			compare_005.data_type = 'INT'
			compare_005.mode = 'ELEMENT'
			compare_005.operation = 'EQUAL'
			#B_INT
			compare_005.inputs[3].default_value = 16
			
			#node Reroute.015
			reroute_015 = color_common.nodes.new("NodeReroute")
			reroute_015.name = "Reroute.015"
			#node Switch.004
			switch_004 = color_common.nodes.new("GeometryNodeSwitch")
			switch_004.name = "Switch.004"
			switch_004.input_type = 'RGBA'
			
			#node Reroute.016
			reroute_016 = color_common.nodes.new("NodeReroute")
			reroute_016.name = "Reroute.016"
			#node Reroute.017
			reroute_017 = color_common.nodes.new("NodeReroute")
			reroute_017.name = "Reroute.017"
			#node Reroute.010
			reroute_010 = color_common.nodes.new("NodeReroute")
			reroute_010.name = "Reroute.010"
			#node Named Attribute
			named_attribute = color_common.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'INT'
			#Name
			named_attribute.inputs[0].default_value = "atomic_number"
			
			#node Named Attribute.002
			named_attribute_002 = color_common.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002.name = "Named Attribute.002"
			named_attribute_002.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute_002.inputs[0].default_value = "Color"
			
			#node Switch.005
			switch_005 = color_common.nodes.new("GeometryNodeSwitch")
			switch_005.name = "Switch.005"
			switch_005.input_type = 'RGBA'
			
			#node Group Output
			group_output = color_common.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = color_common.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			
			
			
			#Set locations
			reroute_001.location = (40.0, -160.0)
			reroute_007.location = (200.00003051757812, -180.0)
			switch_002.location = (240.0, 19.999969482421875)
			reroute_009.location = (339.9999694824219, -200.0)
			reroute.location = (-119.99996948242188, -160.0)
			reroute_006.location = (-119.99996948242188, -179.99996948242188)
			reroute_004.location = (-119.99996948242188, -200.0)
			switch.location = (-120.0, 20.0)
			switch_001.location = (60.0, 20.0)
			compare.location = (-120.0, 199.99996948242188)
			reroute_011.location = (-160.0, 219.99998474121094)
			reroute_002.location = (20.0, 219.99998474121094)
			compare_001.location = (59.99998474121094, 199.99998474121094)
			reroute_003.location = (200.0, 220.00001525878906)
			compare_002.location = (240.0, 200.00001525878906)
			reroute_005.location = (379.9999694824219, 220.00003051757812)
			compare_003.location = (420.0, 200.0)
			reroute_012.location = (560.0000610351562, 219.99996948242188)
			reroute_013.location = (520.0000610351562, -220.0)
			reroute_014.location = (-120.0, -220.0)
			switch_003.location = (420.0, 20.0)
			compare_004.location = (600.0000610351562, 199.99996948242188)
			compare_005.location = (780.0, 200.0)
			reroute_015.location = (760.0, 220.0)
			switch_004.location = (600.0000610351562, 20.0)
			reroute_016.location = (680.0, -240.0)
			reroute_017.location = (-120.0, -240.0)
			reroute_010.location = (-168.18707275390625, 82.08197021484375)
			named_attribute.location = (-440.0, 260.0)
			named_attribute_002.location = (-380.0, 40.0)
			switch_005.location = (780.0, 20.0)
			group_output.location = (1020.0, 220.0)
			group_input.location = (-380.0, -100.0)
			
			#Set dimensions
			reroute_001.width, reroute_001.height = 16.0, 100.0
			reroute_007.width, reroute_007.height = 16.0, 100.0
			switch_002.width, switch_002.height = 140.0, 100.0
			reroute_009.width, reroute_009.height = 16.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			reroute_006.width, reroute_006.height = 16.0, 100.0
			reroute_004.width, reroute_004.height = 16.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			switch_001.width, switch_001.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			reroute_011.width, reroute_011.height = 16.0, 100.0
			reroute_002.width, reroute_002.height = 16.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			reroute_003.width, reroute_003.height = 16.0, 100.0
			compare_002.width, compare_002.height = 140.0, 100.0
			reroute_005.width, reroute_005.height = 16.0, 100.0
			compare_003.width, compare_003.height = 140.0, 100.0
			reroute_012.width, reroute_012.height = 16.0, 100.0
			reroute_013.width, reroute_013.height = 16.0, 100.0
			reroute_014.width, reroute_014.height = 16.0, 100.0
			switch_003.width, switch_003.height = 140.0, 100.0
			compare_004.width, compare_004.height = 140.0, 100.0
			compare_005.width, compare_005.height = 140.0, 100.0
			reroute_015.width, reroute_015.height = 16.0, 100.0
			switch_004.width, switch_004.height = 140.0, 100.0
			reroute_016.width, reroute_016.height = 16.0, 100.0
			reroute_017.width, reroute_017.height = 16.0, 100.0
			reroute_010.width, reroute_010.height = 16.0, 100.0
			named_attribute.width, named_attribute.height = 199.0511474609375, 100.0
			named_attribute_002.width, named_attribute_002.height = 140.0, 100.0
			switch_005.width, switch_005.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			
			#initialize color_common links
			#compare.Result -> switch.Switch
			color_common.links.new(compare.outputs[0], switch.inputs[0])
			#group_input.Hydrogen -> switch.True
			color_common.links.new(group_input.outputs[0], switch.inputs[2])
			#switch.Output -> switch_001.False
			color_common.links.new(switch.outputs[0], switch_001.inputs[1])
			#reroute_001.Output -> switch_001.True
			color_common.links.new(reroute_001.outputs[0], switch_001.inputs[2])
			#group_input.Carbon -> reroute.Input
			color_common.links.new(group_input.outputs[1], reroute.inputs[0])
			#reroute.Output -> reroute_001.Input
			color_common.links.new(reroute.outputs[0], reroute_001.inputs[0])
			#switch_001.Output -> switch_002.False
			color_common.links.new(switch_001.outputs[0], switch_002.inputs[1])
			#reroute_007.Output -> switch_002.True
			color_common.links.new(reroute_007.outputs[0], switch_002.inputs[2])
			#group_input.Nitrogen -> reroute_006.Input
			color_common.links.new(group_input.outputs[2], reroute_006.inputs[0])
			#reroute_006.Output -> reroute_007.Input
			color_common.links.new(reroute_006.outputs[0], reroute_007.inputs[0])
			#switch_002.Output -> switch_003.False
			color_common.links.new(switch_002.outputs[0], switch_003.inputs[1])
			#reroute_009.Output -> switch_003.True
			color_common.links.new(reroute_009.outputs[0], switch_003.inputs[2])
			#group_input.Oxygen -> reroute_004.Input
			color_common.links.new(group_input.outputs[3], reroute_004.inputs[0])
			#reroute_004.Output -> reroute_009.Input
			color_common.links.new(reroute_004.outputs[0], reroute_009.inputs[0])
			#reroute_010.Output -> compare.A
			color_common.links.new(reroute_010.outputs[0], compare.inputs[2])
			#reroute_010.Output -> reroute_011.Input
			color_common.links.new(reroute_010.outputs[0], reroute_011.inputs[0])
			#compare_001.Result -> switch_001.Switch
			color_common.links.new(compare_001.outputs[0], switch_001.inputs[0])
			#reroute_002.Output -> compare_001.A
			color_common.links.new(reroute_002.outputs[0], compare_001.inputs[2])
			#reroute_011.Output -> reroute_002.Input
			color_common.links.new(reroute_011.outputs[0], reroute_002.inputs[0])
			#reroute_003.Output -> compare_002.A
			color_common.links.new(reroute_003.outputs[0], compare_002.inputs[2])
			#reroute_002.Output -> reroute_003.Input
			color_common.links.new(reroute_002.outputs[0], reroute_003.inputs[0])
			#compare_002.Result -> switch_002.Switch
			color_common.links.new(compare_002.outputs[0], switch_002.inputs[0])
			#reroute_005.Output -> compare_003.A
			color_common.links.new(reroute_005.outputs[0], compare_003.inputs[2])
			#reroute_003.Output -> reroute_005.Input
			color_common.links.new(reroute_003.outputs[0], reroute_005.inputs[0])
			#compare_003.Result -> switch_003.Switch
			color_common.links.new(compare_003.outputs[0], switch_003.inputs[0])
			#reroute_012.Output -> compare_004.A
			color_common.links.new(reroute_012.outputs[0], compare_004.inputs[2])
			#compare_004.Result -> switch_004.Switch
			color_common.links.new(compare_004.outputs[0], switch_004.inputs[0])
			#reroute_005.Output -> reroute_012.Input
			color_common.links.new(reroute_005.outputs[0], reroute_012.inputs[0])
			#reroute_013.Output -> switch_004.True
			color_common.links.new(reroute_013.outputs[0], switch_004.inputs[2])
			#reroute_014.Output -> reroute_013.Input
			color_common.links.new(reroute_014.outputs[0], reroute_013.inputs[0])
			#group_input.Phosphorous -> reroute_014.Input
			color_common.links.new(group_input.outputs[4], reroute_014.inputs[0])
			#switch_003.Output -> switch_004.False
			color_common.links.new(switch_003.outputs[0], switch_004.inputs[1])
			#reroute_015.Output -> compare_005.A
			color_common.links.new(reroute_015.outputs[0], compare_005.inputs[2])
			#compare_005.Result -> switch_005.Switch
			color_common.links.new(compare_005.outputs[0], switch_005.inputs[0])
			#reroute_012.Output -> reroute_015.Input
			color_common.links.new(reroute_012.outputs[0], reroute_015.inputs[0])
			#switch_004.Output -> switch_005.False
			color_common.links.new(switch_004.outputs[0], switch_005.inputs[1])
			#reroute_016.Output -> switch_005.True
			color_common.links.new(reroute_016.outputs[0], switch_005.inputs[2])
			#reroute_017.Output -> reroute_016.Input
			color_common.links.new(reroute_017.outputs[0], reroute_016.inputs[0])
			#group_input.Sulfur -> reroute_017.Input
			color_common.links.new(group_input.outputs[5], reroute_017.inputs[0])
			#named_attribute.Attribute -> reroute_010.Input
			color_common.links.new(named_attribute.outputs[0], reroute_010.inputs[0])
			#switch_005.Output -> group_output.Color
			color_common.links.new(switch_005.outputs[0], group_output.inputs[0])
			#named_attribute_002.Attribute -> switch.False
			color_common.links.new(named_attribute_002.outputs[0], switch.inputs[1])
			return color_common

		color_common = color_common_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Color Common", type = 'NODES')
		mod.node_group = color_common
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Color_Common.bl_idname)
			
def register():
	bpy.utils.register_class(Color_Common)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Color_Common)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
