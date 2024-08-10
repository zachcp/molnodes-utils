bl_info = {
	"name" : "Select Atomic Number",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Select_Atomic_Number(bpy.types.Operator):
	bl_idname = "node.select_atomic_number"
	bl_label = "Select Atomic Number"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize select_atomic_number node group
		def select_atomic_number_node_group():
			select_atomic_number = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Select Atomic Number")

			select_atomic_number.color_tag = 'INPUT'
			select_atomic_number.description = ""

			
			#select_atomic_number interface
			#Socket Selection
			selection_socket = select_atomic_number.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket.attribute_domain = 'POINT'
			selection_socket.description = "The calculated selection"
			
			#Socket Inverted
			inverted_socket = select_atomic_number.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket.attribute_domain = 'POINT'
			inverted_socket.description = "The inverse of the calculated selection"
			
			#Socket And
			and_socket = select_atomic_number.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket.attribute_domain = 'POINT'
			and_socket.hide_value = True
			
			#Socket Or
			or_socket = select_atomic_number.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket.attribute_domain = 'POINT'
			or_socket.hide_value = True
			
			#Socket atomic_number
			atomic_number_socket = select_atomic_number.interface.new_socket(name = "atomic_number", in_out='INPUT', socket_type = 'NodeSocketInt')
			atomic_number_socket.subtype = 'NONE'
			atomic_number_socket.default_value = 6
			atomic_number_socket.min_value = 1
			atomic_number_socket.max_value = 140
			atomic_number_socket.attribute_domain = 'POINT'
			atomic_number_socket.description = "Create a selection based on the inputted atomic number."
			
			
			#initialize select_atomic_number nodes
			#node Named Attribute
			named_attribute = select_atomic_number.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'INT'
			#Name
			named_attribute.inputs[0].default_value = "atomic_number"
			
			#node Compare
			compare = select_atomic_number.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'EQUAL'
			
			#node Boolean Math
			boolean_math = select_atomic_number.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'NOT'
			
			#node Group Output
			group_output = select_atomic_number.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = select_atomic_number.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			group_input.outputs[0].hide = True
			
			#node Reroute
			reroute = select_atomic_number.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Boolean Math.001
			boolean_math_001 = select_atomic_number.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001.name = "Boolean Math.001"
			boolean_math_001.operation = 'AND'
			
			#node Group Input.001
			group_input_001 = select_atomic_number.nodes.new("NodeGroupInput")
			group_input_001.name = "Group Input.001"
			group_input_001.outputs[1].hide = True
			group_input_001.outputs[2].hide = True
			group_input_001.outputs[3].hide = True
			
			#node Boolean Math.002
			boolean_math_002 = select_atomic_number.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002.name = "Boolean Math.002"
			boolean_math_002.operation = 'OR'
			
			
			
			
			#Set locations
			named_attribute.location = (-548.0000610351562, 0.0)
			compare.location = (-388.0, 0.0)
			boolean_math.location = (148.0, -60.0)
			group_output.location = (347.9999694824219, 0.0)
			group_input.location = (-548.0000610351562, -140.0)
			reroute.location = (148.0, -60.0)
			boolean_math_001.location = (-220.0, 0.0)
			group_input_001.location = (-400.0, 80.0)
			boolean_math_002.location = (-40.0, 0.0)
			
			#Set dimensions
			named_attribute.width, named_attribute.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
			group_input_001.width, group_input_001.height = 140.0, 100.0
			boolean_math_002.width, boolean_math_002.height = 140.0, 100.0
			
			#initialize select_atomic_number links
			#named_attribute.Attribute -> compare.A
			select_atomic_number.links.new(named_attribute.outputs[0], compare.inputs[2])
			#reroute.Output -> boolean_math.Boolean
			select_atomic_number.links.new(reroute.outputs[0], boolean_math.inputs[0])
			#group_input.atomic_number -> compare.B
			select_atomic_number.links.new(group_input.outputs[2], compare.inputs[3])
			#reroute.Output -> group_output.Selection
			select_atomic_number.links.new(reroute.outputs[0], group_output.inputs[0])
			#boolean_math.Boolean -> group_output.Inverted
			select_atomic_number.links.new(boolean_math.outputs[0], group_output.inputs[1])
			#boolean_math_002.Boolean -> reroute.Input
			select_atomic_number.links.new(boolean_math_002.outputs[0], reroute.inputs[0])
			#compare.Result -> boolean_math_001.Boolean
			select_atomic_number.links.new(compare.outputs[0], boolean_math_001.inputs[1])
			#group_input_001.And -> boolean_math_001.Boolean
			select_atomic_number.links.new(group_input_001.outputs[0], boolean_math_001.inputs[0])
			#boolean_math_001.Boolean -> boolean_math_002.Boolean
			select_atomic_number.links.new(boolean_math_001.outputs[0], boolean_math_002.inputs[0])
			#group_input.Or -> boolean_math_002.Boolean
			select_atomic_number.links.new(group_input.outputs[1], boolean_math_002.inputs[1])
			return select_atomic_number

		select_atomic_number = select_atomic_number_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Select Atomic Number", type = 'NODES')
		mod.node_group = select_atomic_number
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Select_Atomic_Number.bl_idname)
			
def register():
	bpy.utils.register_class(Select_Atomic_Number)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Select_Atomic_Number)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
