bl_info = {
	"name" : "Bond Count",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Bond_Count(bpy.types.Operator):
	bl_idname = "node.bond_count"
	bl_label = "Bond Count"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize bond_count node group
		def bond_count_node_group():
			bond_count = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Bond Count")

			bond_count.color_tag = 'INPUT'
			bond_count.description = ""

			
			#bond_count interface
			#Socket Is Bonded
			is_bonded_socket = bond_count.interface.new_socket(name = "Is Bonded", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_bonded_socket.attribute_domain = 'POINT'
			
			#Socket Bonds
			bonds_socket = bond_count.interface.new_socket(name = "Bonds", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			bonds_socket.subtype = 'NONE'
			bonds_socket.default_value = 0
			bonds_socket.min_value = -2147483648
			bonds_socket.max_value = 2147483647
			bonds_socket.attribute_domain = 'POINT'
			bonds_socket.description = "The number of bonds or edges that a point has"
			
			
			#initialize bond_count nodes
			#node Group Output
			group_output = bond_count.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = bond_count.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Edges of Vertex.001
			edges_of_vertex_001 = bond_count.nodes.new("GeometryNodeEdgesOfVertex")
			edges_of_vertex_001.name = "Edges of Vertex.001"
			#Vertex Index
			edges_of_vertex_001.inputs[0].default_value = 0
			#Weights
			edges_of_vertex_001.inputs[1].default_value = 0.0
			#Sort Index
			edges_of_vertex_001.inputs[2].default_value = 0
			
			#node Compare
			compare = bond_count.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'GREATER_THAN'
			#B_INT
			compare.inputs[3].default_value = 0
			
			
			
			
			#Set locations
			group_output.location = (200.0, 100.0)
			group_input.location = (-200.0, 0.0)
			edges_of_vertex_001.location = (0.0, 0.0)
			compare.location = (0.0, 160.0)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			edges_of_vertex_001.width, edges_of_vertex_001.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			
			#initialize bond_count links
			#edges_of_vertex_001.Total -> group_output.Bonds
			bond_count.links.new(edges_of_vertex_001.outputs[1], group_output.inputs[1])
			#edges_of_vertex_001.Total -> compare.A
			bond_count.links.new(edges_of_vertex_001.outputs[1], compare.inputs[2])
			#compare.Result -> group_output.Is Bonded
			bond_count.links.new(compare.outputs[0], group_output.inputs[0])
			return bond_count

		bond_count = bond_count_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Bond Count", type = 'NODES')
		mod.node_group = bond_count
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Bond_Count.bl_idname)
			
def register():
	bpy.utils.register_class(Bond_Count)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Bond_Count)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
