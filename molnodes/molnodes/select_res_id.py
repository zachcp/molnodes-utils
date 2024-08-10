bl_info = {
	"name" : "Select Res ID",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Select_Res_ID(bpy.types.Operator):
	bl_idname = "node.select_res_id"
	bl_label = "Select Res ID"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize select_res_id node group
		def select_res_id_node_group():
			select_res_id = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Select Res ID")

			select_res_id.color_tag = 'INPUT'
			select_res_id.description = ""

			
			#select_res_id interface
			#Socket Selection
			selection_socket = select_res_id.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket.attribute_domain = 'POINT'
			selection_socket.description = "The calculated selection"
			
			#Socket Inverted
			inverted_socket = select_res_id.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket.attribute_domain = 'POINT'
			inverted_socket.description = "The inverse of the calculated selection"
			
			#Socket And
			and_socket = select_res_id.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket.attribute_domain = 'POINT'
			and_socket.hide_value = True
			
			#Socket Or
			or_socket = select_res_id.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket.attribute_domain = 'POINT'
			or_socket.hide_value = True
			
			#Socket Res ID
			res_id_socket = select_res_id.interface.new_socket(name = "Res ID", in_out='INPUT', socket_type = 'NodeSocketInt')
			res_id_socket.subtype = 'NONE'
			res_id_socket.default_value = 10
			res_id_socket.min_value = 0
			res_id_socket.max_value = 2147483647
			res_id_socket.attribute_domain = 'POINT'
			res_id_socket.description = "A single `res_id` selection"
			
			
			#initialize select_res_id nodes
			#node Group Input
			group_input = select_res_id.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			group_input.outputs[0].hide = True
			
			#node Named Attribute
			named_attribute = select_res_id.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'INT'
			#Name
			named_attribute.inputs[0].default_value = "res_id"
			
			#node Compare
			compare = select_res_id.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'EQUAL'
			
			#node Boolean Math
			boolean_math = select_res_id.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'NOT'
			
			#node Group Output
			group_output = select_res_id.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Reroute
			reroute = select_res_id.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Boolean Math.001
			boolean_math_001 = select_res_id.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001.name = "Boolean Math.001"
			boolean_math_001.operation = 'AND'
			
			#node Group Input.001
			group_input_001 = select_res_id.nodes.new("NodeGroupInput")
			group_input_001.name = "Group Input.001"
			group_input_001.outputs[1].hide = True
			group_input_001.outputs[2].hide = True
			group_input_001.outputs[3].hide = True
			
			#node Boolean Math.002
			boolean_math_002 = select_res_id.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002.name = "Boolean Math.002"
			boolean_math_002.operation = 'OR'
			
			
			
			
			#Set locations
			group_input.location = (-508.0000305175781, -120.0)
			named_attribute.location = (-508.0000305175781, 0.0)
			compare.location = (-348.0000305175781, 0.0)
			boolean_math.location = (227.99998474121094, -60.0)
			group_output.location = (428.00006103515625, 0.0)
			reroute.location = (207.99998474121094, -40.0)
			boolean_math_001.location = (-160.0, 0.0)
			group_input_001.location = (-340.0, 80.0)
			boolean_math_002.location = (0.0, 0.0)
			
			#Set dimensions
			group_input.width, group_input.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
			group_input_001.width, group_input_001.height = 140.0, 100.0
			boolean_math_002.width, boolean_math_002.height = 140.0, 100.0
			
			#initialize select_res_id links
			#named_attribute.Attribute -> compare.A
			select_res_id.links.new(named_attribute.outputs[0], compare.inputs[2])
			#reroute.Output -> boolean_math.Boolean
			select_res_id.links.new(reroute.outputs[0], boolean_math.inputs[0])
			#group_input.Res ID -> compare.B
			select_res_id.links.new(group_input.outputs[2], compare.inputs[3])
			#reroute.Output -> group_output.Selection
			select_res_id.links.new(reroute.outputs[0], group_output.inputs[0])
			#boolean_math.Boolean -> group_output.Inverted
			select_res_id.links.new(boolean_math.outputs[0], group_output.inputs[1])
			#boolean_math_002.Boolean -> reroute.Input
			select_res_id.links.new(boolean_math_002.outputs[0], reroute.inputs[0])
			#compare.Result -> boolean_math_001.Boolean
			select_res_id.links.new(compare.outputs[0], boolean_math_001.inputs[1])
			#group_input_001.And -> boolean_math_001.Boolean
			select_res_id.links.new(group_input_001.outputs[0], boolean_math_001.inputs[0])
			#boolean_math_001.Boolean -> boolean_math_002.Boolean
			select_res_id.links.new(boolean_math_001.outputs[0], boolean_math_002.inputs[0])
			#group_input.Or -> boolean_math_002.Boolean
			select_res_id.links.new(group_input.outputs[1], boolean_math_002.inputs[1])
			return select_res_id

		select_res_id = select_res_id_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Select Res ID", type = 'NODES')
		mod.node_group = select_res_id
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Select_Res_ID.bl_idname)
			
def register():
	bpy.utils.register_class(Select_Res_ID)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Select_Res_ID)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
