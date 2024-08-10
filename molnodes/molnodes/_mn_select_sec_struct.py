bl_info = {
	"name" : ".MN_select_sec_struct",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _MN_select_sec_struct(bpy.types.Operator):
	bl_idname = "node._mn_select_sec_struct"
	bl_label = ".MN_select_sec_struct"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _mn_select_sec_struct_id node group
		def _mn_select_sec_struct_id_node_group():
			_mn_select_sec_struct_id = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_select_sec_struct_id")

			_mn_select_sec_struct_id.color_tag = 'NONE'
			_mn_select_sec_struct_id.description = ""

			
			#_mn_select_sec_struct_id interface
			#Socket Selection
			selection_socket = _mn_select_sec_struct_id.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket.attribute_domain = 'POINT'
			selection_socket.description = "The calculated selection"
			
			#Socket Inverted
			inverted_socket = _mn_select_sec_struct_id.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket.attribute_domain = 'POINT'
			
			#Socket And
			and_socket = _mn_select_sec_struct_id.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket.attribute_domain = 'POINT'
			and_socket.hide_value = True
			
			#Socket Or
			or_socket = _mn_select_sec_struct_id.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket.attribute_domain = 'POINT'
			or_socket.hide_value = True
			
			#Socket id
			id_socket = _mn_select_sec_struct_id.interface.new_socket(name = "id", in_out='INPUT', socket_type = 'NodeSocketInt')
			id_socket.subtype = 'NONE'
			id_socket.default_value = 1
			id_socket.min_value = -2147483648
			id_socket.max_value = 2147483647
			id_socket.attribute_domain = 'POINT'
			id_socket.description = "Secondary structure component to select"
			
			
			#initialize _mn_select_sec_struct_id nodes
			#node Named Attribute.002
			named_attribute_002 = _mn_select_sec_struct_id.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002.name = "Named Attribute.002"
			named_attribute_002.data_type = 'INT'
			#Name
			named_attribute_002.inputs[0].default_value = "sec_struct"
			
			#node Boolean Math
			boolean_math = _mn_select_sec_struct_id.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'AND'
			
			#node Group Output
			group_output = _mn_select_sec_struct_id.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Compare.012
			compare_012 = _mn_select_sec_struct_id.nodes.new("FunctionNodeCompare")
			compare_012.name = "Compare.012"
			compare_012.data_type = 'INT'
			compare_012.mode = 'ELEMENT'
			compare_012.operation = 'EQUAL'
			
			#node Group Input
			group_input = _mn_select_sec_struct_id.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Boolean Math.001
			boolean_math_001 = _mn_select_sec_struct_id.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001.name = "Boolean Math.001"
			boolean_math_001.operation = 'OR'
			
			#node Boolean Math.002
			boolean_math_002 = _mn_select_sec_struct_id.nodes.new("FunctionNodeBooleanMath")
			boolean_math_002.name = "Boolean Math.002"
			boolean_math_002.operation = 'NOT'
			
			
			
			
			#Set locations
			named_attribute_002.location = (80.0, 0.0)
			boolean_math.location = (400.0, 200.0)
			group_output.location = (760.0, 200.0)
			compare_012.location = (240.0, 100.0)
			group_input.location = (80.0, 100.0)
			boolean_math_001.location = (579.9999389648438, 196.54164123535156)
			boolean_math_002.location = (580.0, 60.0)
			
			#Set dimensions
			named_attribute_002.width, named_attribute_002.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			compare_012.width, compare_012.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
			boolean_math_002.width, boolean_math_002.height = 140.0, 100.0
			
			#initialize _mn_select_sec_struct_id links
			#boolean_math_001.Boolean -> group_output.Selection
			_mn_select_sec_struct_id.links.new(boolean_math_001.outputs[0], group_output.inputs[0])
			#compare_012.Result -> boolean_math.Boolean
			_mn_select_sec_struct_id.links.new(compare_012.outputs[0], boolean_math.inputs[1])
			#group_input.id -> compare_012.A
			_mn_select_sec_struct_id.links.new(group_input.outputs[2], compare_012.inputs[2])
			#group_input.And -> boolean_math.Boolean
			_mn_select_sec_struct_id.links.new(group_input.outputs[0], boolean_math.inputs[0])
			#named_attribute_002.Attribute -> compare_012.B
			_mn_select_sec_struct_id.links.new(named_attribute_002.outputs[0], compare_012.inputs[3])
			#boolean_math.Boolean -> boolean_math_001.Boolean
			_mn_select_sec_struct_id.links.new(boolean_math.outputs[0], boolean_math_001.inputs[0])
			#group_input.Or -> boolean_math_001.Boolean
			_mn_select_sec_struct_id.links.new(group_input.outputs[1], boolean_math_001.inputs[1])
			#boolean_math_001.Boolean -> boolean_math_002.Boolean
			_mn_select_sec_struct_id.links.new(boolean_math_001.outputs[0], boolean_math_002.inputs[0])
			#boolean_math_002.Boolean -> group_output.Inverted
			_mn_select_sec_struct_id.links.new(boolean_math_002.outputs[0], group_output.inputs[1])
			return _mn_select_sec_struct_id

		_mn_select_sec_struct_id = _mn_select_sec_struct_id_node_group()

		#initialize is_sheet node group
		def is_sheet_node_group():
			is_sheet = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Is Sheet")

			is_sheet.color_tag = 'INPUT'
			is_sheet.description = ""

			
			#is_sheet interface
			#Socket Selection
			selection_socket_1 = is_sheet.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket_1.attribute_domain = 'POINT'
			selection_socket_1.description = "Selected atoms form part of a sheet"
			
			#Socket Inverted
			inverted_socket_1 = is_sheet.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket_1.attribute_domain = 'POINT'
			
			#Socket And
			and_socket_1 = is_sheet.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket_1.attribute_domain = 'POINT'
			and_socket_1.hide_value = True
			
			#Socket Or
			or_socket_1 = is_sheet.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket_1.attribute_domain = 'POINT'
			or_socket_1.hide_value = True
			
			
			#initialize is_sheet nodes
			#node Group Output
			group_output_1 = is_sheet.nodes.new("NodeGroupOutput")
			group_output_1.name = "Group Output"
			group_output_1.is_active_output = True
			
			#node Group Input
			group_input_1 = is_sheet.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			
			#node MN_select_sec_struct.002
			mn_select_sec_struct_002 = is_sheet.nodes.new("GeometryNodeGroup")
			mn_select_sec_struct_002.label = "Select Sec Struct"
			mn_select_sec_struct_002.name = "MN_select_sec_struct.002"
			mn_select_sec_struct_002.node_tree = _mn_select_sec_struct_id
			#Socket_1
			mn_select_sec_struct_002.inputs[2].default_value = 2
			
			
			
			
			#Set locations
			group_output_1.location = (267.00146484375, 0.0)
			group_input_1.location = (-220.0, -80.0)
			mn_select_sec_struct_002.location = (0.0, 0.0)
			
			#Set dimensions
			group_output_1.width, group_output_1.height = 140.0, 100.0
			group_input_1.width, group_input_1.height = 140.0, 100.0
			mn_select_sec_struct_002.width, mn_select_sec_struct_002.height = 217.00146484375, 100.0
			
			#initialize is_sheet links
			#mn_select_sec_struct_002.Selection -> group_output_1.Selection
			is_sheet.links.new(mn_select_sec_struct_002.outputs[0], group_output_1.inputs[0])
			#group_input_1.And -> mn_select_sec_struct_002.And
			is_sheet.links.new(group_input_1.outputs[0], mn_select_sec_struct_002.inputs[0])
			#group_input_1.Or -> mn_select_sec_struct_002.Or
			is_sheet.links.new(group_input_1.outputs[1], mn_select_sec_struct_002.inputs[1])
			#mn_select_sec_struct_002.Inverted -> group_output_1.Inverted
			is_sheet.links.new(mn_select_sec_struct_002.outputs[1], group_output_1.inputs[1])
			return is_sheet

		is_sheet = is_sheet_node_group()

		#initialize is_loop node group
		def is_loop_node_group():
			is_loop = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Is Loop")

			is_loop.color_tag = 'INPUT'
			is_loop.description = ""

			
			#is_loop interface
			#Socket Selection
			selection_socket_2 = is_loop.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket_2.attribute_domain = 'POINT'
			selection_socket_2.description = "Selected atoms form part of a loop, and not part of any secondary structure"
			
			#Socket Inverted
			inverted_socket_2 = is_loop.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket_2.attribute_domain = 'POINT'
			
			#Socket And
			and_socket_2 = is_loop.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket_2.attribute_domain = 'POINT'
			and_socket_2.hide_value = True
			
			#Socket Or
			or_socket_2 = is_loop.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket_2.attribute_domain = 'POINT'
			or_socket_2.hide_value = True
			
			
			#initialize is_loop nodes
			#node Group Output
			group_output_2 = is_loop.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Group Input
			group_input_2 = is_loop.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
			#node MN_select_sec_struct.002
			mn_select_sec_struct_002_1 = is_loop.nodes.new("GeometryNodeGroup")
			mn_select_sec_struct_002_1.label = "Select Sec Struct"
			mn_select_sec_struct_002_1.name = "MN_select_sec_struct.002"
			mn_select_sec_struct_002_1.node_tree = _mn_select_sec_struct_id
			#Socket_1
			mn_select_sec_struct_002_1.inputs[2].default_value = 3
			
			
			
			
			#Set locations
			group_output_2.location = (267.00146484375, 0.0)
			group_input_2.location = (-200.0, 0.0)
			mn_select_sec_struct_002_1.location = (0.0, 0.0)
			
			#Set dimensions
			group_output_2.width, group_output_2.height = 140.0, 100.0
			group_input_2.width, group_input_2.height = 140.0, 100.0
			mn_select_sec_struct_002_1.width, mn_select_sec_struct_002_1.height = 217.00146484375, 100.0
			
			#initialize is_loop links
			#mn_select_sec_struct_002_1.Selection -> group_output_2.Selection
			is_loop.links.new(mn_select_sec_struct_002_1.outputs[0], group_output_2.inputs[0])
			#group_input_2.And -> mn_select_sec_struct_002_1.And
			is_loop.links.new(group_input_2.outputs[0], mn_select_sec_struct_002_1.inputs[0])
			#group_input_2.Or -> mn_select_sec_struct_002_1.Or
			is_loop.links.new(group_input_2.outputs[1], mn_select_sec_struct_002_1.inputs[1])
			#mn_select_sec_struct_002_1.Inverted -> group_output_2.Inverted
			is_loop.links.new(mn_select_sec_struct_002_1.outputs[1], group_output_2.inputs[1])
			return is_loop

		is_loop = is_loop_node_group()

		#initialize is_helix node group
		def is_helix_node_group():
			is_helix = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Is Helix")

			is_helix.color_tag = 'INPUT'
			is_helix.description = ""

			
			#is_helix interface
			#Socket Selection
			selection_socket_3 = is_helix.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket_3.attribute_domain = 'POINT'
			selection_socket_3.description = "Selected atoms form part of an helix"
			
			#Socket Inverted
			inverted_socket_3 = is_helix.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			inverted_socket_3.attribute_domain = 'POINT'
			
			#Socket And
			and_socket_3 = is_helix.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket_3.attribute_domain = 'POINT'
			and_socket_3.hide_value = True
			
			#Socket Or
			or_socket_3 = is_helix.interface.new_socket(name = "Or", in_out='INPUT', socket_type = 'NodeSocketBool')
			or_socket_3.attribute_domain = 'POINT'
			or_socket_3.hide_value = True
			
			
			#initialize is_helix nodes
			#node Group Output
			group_output_3 = is_helix.nodes.new("NodeGroupOutput")
			group_output_3.name = "Group Output"
			group_output_3.is_active_output = True
			
			#node Group Input
			group_input_3 = is_helix.nodes.new("NodeGroupInput")
			group_input_3.name = "Group Input"
			
			#node MN_select_sec_struct.002
			mn_select_sec_struct_002_2 = is_helix.nodes.new("GeometryNodeGroup")
			mn_select_sec_struct_002_2.label = "Select Sec Struct"
			mn_select_sec_struct_002_2.name = "MN_select_sec_struct.002"
			mn_select_sec_struct_002_2.node_tree = _mn_select_sec_struct_id
			#Socket_1
			mn_select_sec_struct_002_2.inputs[2].default_value = 1
			
			
			
			
			#Set locations
			group_output_3.location = (267.00146484375, 0.0)
			group_input_3.location = (-200.0, 0.0)
			mn_select_sec_struct_002_2.location = (0.0, 0.0)
			
			#Set dimensions
			group_output_3.width, group_output_3.height = 140.0, 100.0
			group_input_3.width, group_input_3.height = 140.0, 100.0
			mn_select_sec_struct_002_2.width, mn_select_sec_struct_002_2.height = 217.00146484375, 100.0
			
			#initialize is_helix links
			#mn_select_sec_struct_002_2.Selection -> group_output_3.Selection
			is_helix.links.new(mn_select_sec_struct_002_2.outputs[0], group_output_3.inputs[0])
			#group_input_3.And -> mn_select_sec_struct_002_2.And
			is_helix.links.new(group_input_3.outputs[0], mn_select_sec_struct_002_2.inputs[0])
			#group_input_3.Or -> mn_select_sec_struct_002_2.Or
			is_helix.links.new(group_input_3.outputs[1], mn_select_sec_struct_002_2.inputs[1])
			#mn_select_sec_struct_002_2.Inverted -> group_output_3.Inverted
			is_helix.links.new(mn_select_sec_struct_002_2.outputs[1], group_output_3.inputs[1])
			return is_helix

		is_helix = is_helix_node_group()

		#initialize _mn_select_sec_struct node group
		def _mn_select_sec_struct_node_group():
			_mn_select_sec_struct = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_select_sec_struct")

			_mn_select_sec_struct.color_tag = 'NONE'
			_mn_select_sec_struct.description = ""

			
			#_mn_select_sec_struct interface
			#Socket Is Helix
			is_helix_socket = _mn_select_sec_struct.interface.new_socket(name = "Is Helix", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_helix_socket.attribute_domain = 'POINT'
			
			#Socket Is Sheet
			is_sheet_socket = _mn_select_sec_struct.interface.new_socket(name = "Is Sheet", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_sheet_socket.attribute_domain = 'POINT'
			
			#Socket Is Structured
			is_structured_socket = _mn_select_sec_struct.interface.new_socket(name = "Is Structured", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_structured_socket.attribute_domain = 'POINT'
			
			#Socket Is Loop
			is_loop_socket = _mn_select_sec_struct.interface.new_socket(name = "Is Loop", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_loop_socket.attribute_domain = 'POINT'
			
			#Socket And
			and_socket_4 = _mn_select_sec_struct.interface.new_socket(name = "And", in_out='INPUT', socket_type = 'NodeSocketBool')
			and_socket_4.attribute_domain = 'POINT'
			and_socket_4.hide_value = True
			
			
			#initialize _mn_select_sec_struct nodes
			#node Group.001
			group_001 = _mn_select_sec_struct.nodes.new("GeometryNodeGroup")
			group_001.name = "Group.001"
			group_001.node_tree = is_sheet
			#Socket_3
			group_001.inputs[1].default_value = False
			
			#node Group.002
			group_002 = _mn_select_sec_struct.nodes.new("GeometryNodeGroup")
			group_002.name = "Group.002"
			group_002.node_tree = is_loop
			#Socket_3
			group_002.inputs[1].default_value = False
			
			#node Group
			group = _mn_select_sec_struct.nodes.new("GeometryNodeGroup")
			group.name = "Group"
			group.node_tree = is_helix
			#Socket_3
			group.inputs[1].default_value = False
			
			#node Boolean Math.001
			boolean_math_001_1 = _mn_select_sec_struct.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001_1.name = "Boolean Math.001"
			boolean_math_001_1.hide = True
			boolean_math_001_1.operation = 'NOT'
			
			#node Group Output
			group_output_4 = _mn_select_sec_struct.nodes.new("NodeGroupOutput")
			group_output_4.name = "Group Output"
			group_output_4.is_active_output = True
			
			#node Group Input
			group_input_4 = _mn_select_sec_struct.nodes.new("NodeGroupInput")
			group_input_4.name = "Group Input"
			group_input_4.outputs[1].hide = True
			
			
			
			
			#Set locations
			group_001.location = (120.0, -60.0)
			group_002.location = (120.0, -180.0)
			group.location = (120.0, 60.0)
			boolean_math_001_1.location = (300.0, -140.0)
			group_output_4.location = (540.0, -60.0)
			group_input_4.location = (-160.0, -40.0)
			
			#Set dimensions
			group_001.width, group_001.height = 140.0, 100.0
			group_002.width, group_002.height = 140.0, 100.0
			group.width, group.height = 140.0, 100.0
			boolean_math_001_1.width, boolean_math_001_1.height = 140.0, 100.0
			group_output_4.width, group_output_4.height = 140.0, 100.0
			group_input_4.width, group_input_4.height = 140.0, 100.0
			
			#initialize _mn_select_sec_struct links
			#group_002.Selection -> group_output_4.Is Loop
			_mn_select_sec_struct.links.new(group_002.outputs[0], group_output_4.inputs[3])
			#group_002.Selection -> boolean_math_001_1.Boolean
			_mn_select_sec_struct.links.new(group_002.outputs[0], boolean_math_001_1.inputs[0])
			#boolean_math_001_1.Boolean -> group_output_4.Is Structured
			_mn_select_sec_struct.links.new(boolean_math_001_1.outputs[0], group_output_4.inputs[2])
			#group.Selection -> group_output_4.Is Helix
			_mn_select_sec_struct.links.new(group.outputs[0], group_output_4.inputs[0])
			#group_001.Selection -> group_output_4.Is Sheet
			_mn_select_sec_struct.links.new(group_001.outputs[0], group_output_4.inputs[1])
			#group_input_4.And -> group.And
			_mn_select_sec_struct.links.new(group_input_4.outputs[0], group.inputs[0])
			#group_input_4.And -> group_001.And
			_mn_select_sec_struct.links.new(group_input_4.outputs[0], group_001.inputs[0])
			#group_input_4.And -> group_002.And
			_mn_select_sec_struct.links.new(group_input_4.outputs[0], group_002.inputs[0])
			return _mn_select_sec_struct

		_mn_select_sec_struct = _mn_select_sec_struct_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".MN_select_sec_struct", type = 'NODES')
		mod.node_group = _mn_select_sec_struct
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_MN_select_sec_struct.bl_idname)
			
def register():
	bpy.utils.register_class(_MN_select_sec_struct)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_MN_select_sec_struct)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
