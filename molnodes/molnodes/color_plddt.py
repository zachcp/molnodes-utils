bl_info = {
	"name" : "Color pLDDT",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Color_pLDDT(bpy.types.Operator):
	bl_idname = "node.color_plddt"
	bl_label = "Color pLDDT"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize color_plddt node group
		def color_plddt_node_group():
			color_plddt = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Color pLDDT")

			color_plddt.color_tag = 'COLOR'
			color_plddt.description = ""

			
			#color_plddt interface
			#Socket Color
			color_socket = color_plddt.interface.new_socket(name = "Color", in_out='OUTPUT', socket_type = 'NodeSocketColor')
			color_socket.default_value = (0.0, 0.0, 0.0, 0.0)
			color_socket.attribute_domain = 'POINT'
			color_socket.description = "Assigned color based on the pLDTT score"
			
			#Socket <50
			_50_socket = color_plddt.interface.new_socket(name = "<50", in_out='INPUT', socket_type = 'NodeSocketColor')
			_50_socket.default_value = (1.0001691579818726, 0.20506973564624786, 0.05950700864195824, 1.0)
			_50_socket.attribute_domain = 'POINT'
			_50_socket.description = "Color for pLDTT < 50"
			
			#Socket <70
			_70_socket = color_plddt.interface.new_socket(name = "<70", in_out='INPUT', socket_type = 'NodeSocketColor')
			_70_socket.default_value = (1.0001686811447144, 0.7083451151847839, 0.006511816289275885, 1.0)
			_70_socket.attribute_domain = 'POINT'
			_70_socket.description = "Color for 50 < pLDTT < 70"
			
			#Socket <90
			_90_socket = color_plddt.interface.new_socket(name = "<90", in_out='INPUT', socket_type = 'NodeSocketColor')
			_90_socket.default_value = (0.13015742599964142, 0.5971758961677551, 0.8962045907974243, 1.0)
			_90_socket.attribute_domain = 'POINT'
			_90_socket.description = "Color for 70 < pLDTT < 90"
			
			#Socket >90
			_90_socket_1 = color_plddt.interface.new_socket(name = ">90", in_out='INPUT', socket_type = 'NodeSocketColor')
			_90_socket_1.default_value = (0.0, 0.08649647235870361, 0.6723945140838623, 1.0)
			_90_socket_1.attribute_domain = 'POINT'
			_90_socket_1.description = "Color for 90 < pLDTT"
			
			
			#initialize color_plddt nodes
			#node Group Output
			group_output = color_plddt.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Named Attribute
			named_attribute = color_plddt.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'FLOAT'
			#Name
			named_attribute.inputs[0].default_value = "b_factor"
			
			#node Switch
			switch = color_plddt.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'RGBA'
			
			#node Switch.001
			switch_001 = color_plddt.nodes.new("GeometryNodeSwitch")
			switch_001.name = "Switch.001"
			switch_001.input_type = 'RGBA'
			
			#node Switch.002
			switch_002 = color_plddt.nodes.new("GeometryNodeSwitch")
			switch_002.name = "Switch.002"
			switch_002.input_type = 'RGBA'
			
			#node Compare
			compare = color_plddt.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'FLOAT'
			compare.mode = 'ELEMENT'
			compare.operation = 'GREATER_THAN'
			#B
			compare.inputs[1].default_value = 50.0
			
			#node Compare.001
			compare_001 = color_plddt.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'FLOAT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'GREATER_THAN'
			#B
			compare_001.inputs[1].default_value = 70.0
			
			#node Compare.002
			compare_002 = color_plddt.nodes.new("FunctionNodeCompare")
			compare_002.name = "Compare.002"
			compare_002.data_type = 'FLOAT'
			compare_002.mode = 'ELEMENT'
			compare_002.operation = 'GREATER_THAN'
			#B
			compare_002.inputs[1].default_value = 90.0
			
			#node Group Input
			group_input = color_plddt.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			
			
			
			#Set locations
			group_output.location = (460.0, 0.0)
			named_attribute.location = (-270.0, 80.0)
			switch.location = (-90.0, -80.0)
			switch_001.location = (90.0, -80.0)
			switch_002.location = (270.0, -80.0)
			compare.location = (-90.0, 80.0)
			compare_001.location = (90.0, 80.0)
			compare_002.location = (270.0, 80.0)
			group_input.location = (-260.0, -200.0)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			switch_001.width, switch_001.height = 140.0, 100.0
			switch_002.width, switch_002.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			compare_002.width, compare_002.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			
			#initialize color_plddt links
			#switch_001.Output -> switch_002.False
			color_plddt.links.new(switch_001.outputs[0], switch_002.inputs[1])
			#named_attribute.Attribute -> compare_001.A
			color_plddt.links.new(named_attribute.outputs[0], compare_001.inputs[0])
			#compare_001.Result -> switch_001.Switch
			color_plddt.links.new(compare_001.outputs[0], switch_001.inputs[0])
			#named_attribute.Attribute -> compare.A
			color_plddt.links.new(named_attribute.outputs[0], compare.inputs[0])
			#compare_002.Result -> switch_002.Switch
			color_plddt.links.new(compare_002.outputs[0], switch_002.inputs[0])
			#named_attribute.Attribute -> compare_002.A
			color_plddt.links.new(named_attribute.outputs[0], compare_002.inputs[0])
			#compare.Result -> switch.Switch
			color_plddt.links.new(compare.outputs[0], switch.inputs[0])
			#switch.Output -> switch_001.False
			color_plddt.links.new(switch.outputs[0], switch_001.inputs[1])
			#switch_002.Output -> group_output.Color
			color_plddt.links.new(switch_002.outputs[0], group_output.inputs[0])
			#group_input.<50 -> switch.False
			color_plddt.links.new(group_input.outputs[0], switch.inputs[1])
			#group_input.<70 -> switch.True
			color_plddt.links.new(group_input.outputs[1], switch.inputs[2])
			#group_input.<90 -> switch_001.True
			color_plddt.links.new(group_input.outputs[2], switch_001.inputs[2])
			#group_input.>90 -> switch_002.True
			color_plddt.links.new(group_input.outputs[3], switch_002.inputs[2])
			return color_plddt

		color_plddt = color_plddt_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Color pLDDT", type = 'NODES')
		mod.node_group = color_plddt
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Color_pLDDT.bl_idname)
			
def register():
	bpy.utils.register_class(Color_pLDDT)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Color_pLDDT)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
