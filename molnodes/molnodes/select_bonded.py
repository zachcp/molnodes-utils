bl_info = {
	"name" : "Select Bonded",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Select_Bonded(bpy.types.Operator):
	bl_idname = "node.select_bonded"
	bl_label = "Select Bonded"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize select_bonded node group
		def select_bonded_node_group():
			select_bonded = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Select Bonded")

			select_bonded.color_tag = 'INPUT'
			select_bonded.description = ""

			
			#select_bonded interface
			#Socket Selection
			selection_socket = select_bonded.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket.default_value = False
			selection_socket.attribute_domain = 'POINT'
			selection_socket.description = "Expanded selection that includes the original selection"
			
			#Socket Bonded
			bonded_socket = select_bonded.interface.new_socket(name = "Bonded", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			bonded_socket.default_value = False
			bonded_socket.attribute_domain = 'POINT'
			bonded_socket.description = "Expanded Selection that excludes the original selection"
			
			#Socket Selection
			selection_socket_1 = select_bonded.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_1.default_value = False
			selection_socket_1.attribute_domain = 'POINT'
			selection_socket_1.hide_value = True
			selection_socket_1.description = "Selection of atoms to apply this node to"
			
			#Socket Depth
			depth_socket = select_bonded.interface.new_socket(name = "Depth", in_out='INPUT', socket_type = 'NodeSocketInt')
			depth_socket.default_value = 1
			depth_socket.min_value = 0
			depth_socket.max_value = 2147483647
			depth_socket.subtype = 'NONE'
			depth_socket.attribute_domain = 'POINT'
			depth_socket.description = "Number of bonds to expand the selection by"
			
			
			#initialize select_bonded nodes
			#node Group Input
			group_input = select_bonded.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Reroute
			reroute = select_bonded.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Shortest Edge Paths
			shortest_edge_paths = select_bonded.nodes.new("GeometryNodeInputShortestEdgePaths")
			shortest_edge_paths.name = "Shortest Edge Paths"
			#Edge Cost
			shortest_edge_paths.inputs[1].default_value = 1.0
			
			#node Compare
			compare = select_bonded.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'LESS_EQUAL'
			
			#node Compare.001
			compare_001 = select_bonded.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'INT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'GREATER_THAN'
			#B_INT
			compare_001.inputs[3].default_value = 0
			
			#node Boolean Math.001
			boolean_math_001 = select_bonded.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001.name = "Boolean Math.001"
			boolean_math_001.operation = 'AND'
			
			#node Group Output
			group_output = select_bonded.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Boolean Math
			boolean_math = select_bonded.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'OR'
			
			
			
			
			#Set locations
			group_input.location = (-285.96417236328125, -95.72706604003906)
			reroute.location = (-60.0, 20.0)
			shortest_edge_paths.location = (0.0, 0.0)
			compare.location = (280.0, -60.0)
			compare_001.location = (280.0, -240.0)
			boolean_math_001.location = (480.0, -80.0)
			group_output.location = (940.080078125, -20.0)
			boolean_math.location = (700.0, 100.0)
			
			#Set dimensions
			group_input.width, group_input.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			shortest_edge_paths.width, shortest_edge_paths.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			
			#initialize select_bonded links
			#reroute.Output -> shortest_edge_paths.End Vertex
			select_bonded.links.new(reroute.outputs[0], shortest_edge_paths.inputs[0])
			#shortest_edge_paths.Total Cost -> compare.A
			select_bonded.links.new(shortest_edge_paths.outputs[1], compare.inputs[0])
			#shortest_edge_paths.Total Cost -> compare.A
			select_bonded.links.new(shortest_edge_paths.outputs[1], compare.inputs[2])
			#group_input.Depth -> compare.B
			select_bonded.links.new(group_input.outputs[1], compare.inputs[3])
			#reroute.Output -> boolean_math.Boolean
			select_bonded.links.new(reroute.outputs[0], boolean_math.inputs[0])
			#group_input.Selection -> reroute.Input
			select_bonded.links.new(group_input.outputs[0], reroute.inputs[0])
			#boolean_math.Boolean -> group_output.Selection
			select_bonded.links.new(boolean_math.outputs[0], group_output.inputs[0])
			#boolean_math_001.Boolean -> group_output.Bonded
			select_bonded.links.new(boolean_math_001.outputs[0], group_output.inputs[1])
			#compare.Result -> boolean_math_001.Boolean
			select_bonded.links.new(compare.outputs[0], boolean_math_001.inputs[0])
			#shortest_edge_paths.Total Cost -> compare_001.A
			select_bonded.links.new(shortest_edge_paths.outputs[1], compare_001.inputs[0])
			#shortest_edge_paths.Total Cost -> compare_001.A
			select_bonded.links.new(shortest_edge_paths.outputs[1], compare_001.inputs[2])
			#compare_001.Result -> boolean_math_001.Boolean
			select_bonded.links.new(compare_001.outputs[0], boolean_math_001.inputs[1])
			#boolean_math_001.Boolean -> boolean_math.Boolean
			select_bonded.links.new(boolean_math_001.outputs[0], boolean_math.inputs[1])
			return select_bonded

		select_bonded = select_bonded_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Select Bonded", type = 'NODES')
		mod.node_group = select_bonded
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Select_Bonded.bl_idname)
			
def register():
	bpy.utils.register_class(Select_Bonded)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Select_Bonded)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
