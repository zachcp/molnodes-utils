bl_info = {
	"name" : "Select Res Whole",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Select_Res_Whole(bpy.types.Operator):
	bl_idname = "node.select_res_whole"
	bl_label = "Select Res Whole"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize select_res_whole node group
		def select_res_whole_node_group():
			select_res_whole = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Select Res Whole")

			select_res_whole.color_tag = 'INPUT'
			select_res_whole.description = ""

			
			#select_res_whole interface
			#Socket Selection
			selection_socket = select_res_whole.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket.attribute_domain = 'POINT'
			selection_socket.description = "The calculated selection"
			
			#Socket Selection
			selection_socket_1 = select_res_whole.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_1.attribute_domain = 'POINT'
			selection_socket_1.hide_value = True
			selection_socket_1.description = "Selection of atoms to apply this node to"
			
			#Socket Expand
			expand_socket = select_res_whole.interface.new_socket(name = "Expand", in_out='INPUT', socket_type = 'NodeSocketBool')
			expand_socket.attribute_domain = 'POINT'
			expand_socket.description = "Whether to expand the selection to the whole residue if at least one atom is selected"
			
			
			#initialize select_res_whole nodes
			#node Accumulate Field
			accumulate_field = select_res_whole.nodes.new("GeometryNodeAccumulateField")
			accumulate_field.name = "Accumulate Field"
			accumulate_field.data_type = 'INT'
			accumulate_field.domain = 'POINT'
			
			#node Compare.001
			compare_001 = select_res_whole.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'INT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'GREATER_THAN'
			#B_INT
			compare_001.inputs[3].default_value = 0
			
			#node Group Output
			group_output = select_res_whole.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Named Attribute.001
			named_attribute_001 = select_res_whole.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.data_type = 'INT'
			#Name
			named_attribute_001.inputs[0].default_value = "res_id"
			
			#node Index
			index = select_res_whole.nodes.new("GeometryNodeInputIndex")
			index.name = "Index"
			
			#node Math
			math = select_res_whole.nodes.new("ShaderNodeMath")
			math.label = "x + 1"
			math.name = "Math"
			math.hide = True
			math.operation = 'ADD'
			math.use_clamp = False
			#Value_001
			math.inputs[1].default_value = 1.0
			
			#node Field at Index
			field_at_index = select_res_whole.nodes.new("GeometryNodeFieldAtIndex")
			field_at_index.name = "Field at Index"
			field_at_index.data_type = 'INT'
			field_at_index.domain = 'POINT'
			
			#node Compare
			compare = select_res_whole.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'NOT_EQUAL'
			
			#node Accumulate Field.001
			accumulate_field_001 = select_res_whole.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_001.name = "Accumulate Field.001"
			accumulate_field_001.data_type = 'INT'
			accumulate_field_001.domain = 'POINT'
			#Group Index
			accumulate_field_001.inputs[1].default_value = 0
			
			#node Group Input
			group_input = select_res_whole.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Switch
			switch = select_res_whole.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'BOOLEAN'
			
			
			
			
			#Set locations
			accumulate_field.location = (0.0, 80.0)
			compare_001.location = (160.0, 80.0)
			group_output.location = (480.0, 180.0)
			named_attribute_001.location = (-520.0, -100.0)
			index.location = (-700.0, -280.0)
			math.location = (-700.0, -340.0)
			field_at_index.location = (-520.0, -240.0)
			compare.location = (-360.0, -240.0)
			accumulate_field_001.location = (-200.0, -200.0)
			group_input.location = (-280.0, 160.0)
			switch.location = (160.0, 240.0)
			
			#Set dimensions
			accumulate_field.width, accumulate_field.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
			index.width, index.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			field_at_index.width, field_at_index.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			accumulate_field_001.width, accumulate_field_001.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			
			#initialize select_res_whole links
			#group_input.Selection -> accumulate_field.Value
			select_res_whole.links.new(group_input.outputs[0], accumulate_field.inputs[0])
			#accumulate_field.Total -> compare_001.A
			select_res_whole.links.new(accumulate_field.outputs[2], compare_001.inputs[2])
			#named_attribute_001.Attribute -> field_at_index.Value
			select_res_whole.links.new(named_attribute_001.outputs[0], field_at_index.inputs[1])
			#index.Index -> math.Value
			select_res_whole.links.new(index.outputs[0], math.inputs[0])
			#math.Value -> field_at_index.Index
			select_res_whole.links.new(math.outputs[0], field_at_index.inputs[0])
			#named_attribute_001.Attribute -> compare.A
			select_res_whole.links.new(named_attribute_001.outputs[0], compare.inputs[2])
			#field_at_index.Value -> compare.B
			select_res_whole.links.new(field_at_index.outputs[0], compare.inputs[3])
			#compare.Result -> accumulate_field_001.Value
			select_res_whole.links.new(compare.outputs[0], accumulate_field_001.inputs[0])
			#accumulate_field_001.Trailing -> accumulate_field.Group ID
			select_res_whole.links.new(accumulate_field_001.outputs[1], accumulate_field.inputs[1])
			#group_input.Selection -> switch.False
			select_res_whole.links.new(group_input.outputs[0], switch.inputs[1])
			#compare_001.Result -> switch.True
			select_res_whole.links.new(compare_001.outputs[0], switch.inputs[2])
			#switch.Output -> group_output.Selection
			select_res_whole.links.new(switch.outputs[0], group_output.inputs[0])
			#group_input.Expand -> switch.Switch
			select_res_whole.links.new(group_input.outputs[1], switch.inputs[0])
			return select_res_whole

		select_res_whole = select_res_whole_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Select Res Whole", type = 'NODES')
		mod.node_group = select_res_whole
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Select_Res_Whole.bl_idname)
			
def register():
	bpy.utils.register_class(Select_Res_Whole)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Select_Res_Whole)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
