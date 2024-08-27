bl_info = {
	"name" : "Edge Info",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Edge_Info(bpy.types.Operator):
	bl_idname = "node.edge_info"
	bl_label = "Edge Info"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize edge_info node group
		def edge_info_node_group():
			edge_info = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Edge Info")

			edge_info.color_tag = 'INPUT'
			edge_info.description = ""

			
			#edge_info interface
			#Socket Is Valid
			is_valid_socket = edge_info.interface.new_socket(name = "Is Valid", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			is_valid_socket.default_value = False
			is_valid_socket.attribute_domain = 'POINT'
			is_valid_socket.description = "Whether there is a valid edge corresponding to the given index"
			
			#Socket Point Index
			point_index_socket = edge_info.interface.new_socket(name = "Point Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			point_index_socket.default_value = -1
			point_index_socket.min_value = -1
			point_index_socket.max_value = 2147483647
			point_index_socket.subtype = 'NONE'
			point_index_socket.attribute_domain = 'POINT'
			point_index_socket.description = "The index for the other point involved in this edge, -1 if not connected"
			
			#Socket Point Position
			point_position_socket = edge_info.interface.new_socket(name = "Point Position", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			point_position_socket.default_value = (0.0, 0.0, 0.0)
			point_position_socket.min_value = -3.4028234663852886e+38
			point_position_socket.max_value = 3.4028234663852886e+38
			point_position_socket.subtype = 'NONE'
			point_position_socket.attribute_domain = 'POINT'
			point_position_socket.description = "The position for the other point involved in this edge, (0, 0, 0) if not connected"
			
			#Socket Edge Index
			edge_index_socket = edge_info.interface.new_socket(name = "Edge Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			edge_index_socket.default_value = -1
			edge_index_socket.min_value = -1
			edge_index_socket.max_value = 2147483647
			edge_index_socket.subtype = 'NONE'
			edge_index_socket.attribute_domain = 'POINT'
			edge_index_socket.description = "The index on the edge domain for the selected edge. -1 if not connected"
			
			#Socket Edge Vector
			edge_vector_socket = edge_info.interface.new_socket(name = "Edge Vector", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			edge_vector_socket.default_value = (0.0, 0.0, 0.0)
			edge_vector_socket.min_value = -3.4028234663852886e+38
			edge_vector_socket.max_value = 3.4028234663852886e+38
			edge_vector_socket.subtype = 'EULER'
			edge_vector_socket.attribute_domain = 'POINT'
			edge_vector_socket.description = "The vector along the selected edge. (0, 0, 0) if not connected"
			
			#Socket Edge Length
			edge_length_socket = edge_info.interface.new_socket(name = "Edge Length", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			edge_length_socket.default_value = -1.0
			edge_length_socket.min_value = 0.0
			edge_length_socket.max_value = 3.4028234663852886e+38
			edge_length_socket.subtype = 'NONE'
			edge_length_socket.attribute_domain = 'POINT'
			edge_length_socket.description = "Length of the selected edge, -1 if not connected"
			
			#Socket Edge Index
			edge_index_socket_1 = edge_info.interface.new_socket(name = "Edge Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			edge_index_socket_1.default_value = 0
			edge_index_socket_1.min_value = 0
			edge_index_socket_1.max_value = 3
			edge_index_socket_1.subtype = 'NONE'
			edge_index_socket_1.attribute_domain = 'POINT'
			edge_index_socket_1.description = "Index within the gorup of edges that are connected to this point"
			
			
			#initialize edge_info nodes
			#node Frame
			frame = edge_info.nodes.new("NodeFrame")
			frame.label = "Check edge exists, or return index -1 and (0, 0, 0) vector"
			frame.name = "Frame"
			frame.label_size = 20
			frame.shrink = True
			
			#node Group Output
			group_output = edge_info.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Reroute.001
			reroute_001 = edge_info.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			#node Reroute.002
			reroute_002 = edge_info.nodes.new("NodeReroute")
			reroute_002.name = "Reroute.002"
			#node Reroute
			reroute = edge_info.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Group Input
			group_input = edge_info.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Switch.003
			switch_003 = edge_info.nodes.new("GeometryNodeSwitch")
			switch_003.name = "Switch.003"
			switch_003.input_type = 'FLOAT'
			#False
			switch_003.inputs[1].default_value = -1.0
			
			#node Switch.001
			switch_001 = edge_info.nodes.new("GeometryNodeSwitch")
			switch_001.name = "Switch.001"
			switch_001.input_type = 'VECTOR'
			#False
			switch_001.inputs[1].default_value = (0.0, 0.0, 0.0)
			
			#node Vector Math
			vector_math = edge_info.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.operation = 'SUBTRACT'
			
			#node Vector Math.001
			vector_math_001 = edge_info.nodes.new("ShaderNodeVectorMath")
			vector_math_001.name = "Vector Math.001"
			vector_math_001.operation = 'LENGTH'
			
			#node Evaluate at Index.001
			evaluate_at_index_001 = edge_info.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001.name = "Evaluate at Index.001"
			evaluate_at_index_001.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_001.domain = 'POINT'
			
			#node Switch
			switch = edge_info.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'INT'
			#False
			switch.inputs[1].default_value = -1
			
			#node Reroute.004
			reroute_004 = edge_info.nodes.new("NodeReroute")
			reroute_004.name = "Reroute.004"
			#node Switch.002
			switch_002 = edge_info.nodes.new("GeometryNodeSwitch")
			switch_002.name = "Switch.002"
			switch_002.input_type = 'INT'
			#False
			switch_002.inputs[1].default_value = -1
			
			#node Compare
			compare = edge_info.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'LESS_THAN'
			
			#node Reroute.003
			reroute_003 = edge_info.nodes.new("NodeReroute")
			reroute_003.name = "Reroute.003"
			#node Edges of Vertex.002
			edges_of_vertex_002 = edge_info.nodes.new("GeometryNodeEdgesOfVertex")
			edges_of_vertex_002.name = "Edges of Vertex.002"
			#Vertex Index
			edges_of_vertex_002.inputs[0].default_value = 0
			#Weights
			edges_of_vertex_002.inputs[1].default_value = 0.0
			
			#node Position
			position = edge_info.nodes.new("GeometryNodeInputPosition")
			position.name = "Position"
			
			#node Evaluate at Index
			evaluate_at_index = edge_info.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index.name = "Evaluate at Index"
			evaluate_at_index.data_type = 'INT'
			evaluate_at_index.domain = 'EDGE'
			
			#node Index.002
			index_002 = edge_info.nodes.new("GeometryNodeInputIndex")
			index_002.name = "Index.002"
			
			#node Math.002
			math_002 = edge_info.nodes.new("ShaderNodeMath")
			math_002.name = "Math.002"
			math_002.operation = 'ADD'
			math_002.use_clamp = False
			
			#node Math.003
			math_003 = edge_info.nodes.new("ShaderNodeMath")
			math_003.name = "Math.003"
			math_003.operation = 'SUBTRACT'
			math_003.use_clamp = False
			
			#node Edge Vertices.002
			edge_vertices_002 = edge_info.nodes.new("GeometryNodeInputMeshEdgeVertices")
			edge_vertices_002.name = "Edge Vertices.002"
			
			
			
			#Set parents
			compare.parent = frame
			
			#Set locations
			frame.location = (170.0, 40.0)
			group_output.location = (740.0, 360.0)
			reroute_001.location = (500.0, 520.0)
			reroute_002.location = (680.0, 520.0)
			reroute.location = (360.0, 340.0)
			group_input.location = (-740.0, 300.0)
			switch_003.location = (520.0, -140.0)
			switch_001.location = (520.0, 80.0)
			vector_math.location = (300.0, -60.0)
			vector_math_001.location = (300.0, -200.0)
			evaluate_at_index_001.location = (300.0, 100.0)
			switch.location = (520.0, 500.0)
			reroute_004.location = (500.0, 280.0)
			switch_002.location = (520.0, 240.0)
			compare.location = (-360.0, 440.0)
			reroute_003.location = (-200.0, 120.0)
			edges_of_vertex_002.location = (-416.6744384765625, 200.0)
			position.location = (120.0, -40.0)
			evaluate_at_index.location = (-200.0, 80.0)
			index_002.location = (-200.0, -80.0)
			math_002.location = (-360.0, -20.0)
			math_003.location = (-40.0, 80.0)
			edge_vertices_002.location = (-520.0, -20.0)
			
			#Set dimensions
			frame.width, frame.height = 200.0, 218.0
			group_output.width, group_output.height = 140.0, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			reroute_002.width, reroute_002.height = 16.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			switch_003.width, switch_003.height = 140.0, 100.0
			switch_001.width, switch_001.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			vector_math_001.width, vector_math_001.height = 140.0, 100.0
			evaluate_at_index_001.width, evaluate_at_index_001.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			reroute_004.width, reroute_004.height = 16.0, 100.0
			switch_002.width, switch_002.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			reroute_003.width, reroute_003.height = 16.0, 100.0
			edges_of_vertex_002.width, edges_of_vertex_002.height = 140.0, 100.0
			position.width, position.height = 147.27230834960938, 100.0
			evaluate_at_index.width, evaluate_at_index.height = 140.0, 100.0
			index_002.width, index_002.height = 140.0, 100.0
			math_002.width, math_002.height = 140.0, 100.0
			math_003.width, math_003.height = 140.0, 100.0
			edge_vertices_002.width, edge_vertices_002.height = 138.7440185546875, 100.0
			
			#initialize edge_info links
			#math_002.Value -> evaluate_at_index.Value
			edge_info.links.new(math_002.outputs[0], evaluate_at_index.inputs[1])
			#edge_vertices_002.Vertex Index 1 -> math_002.Value
			edge_info.links.new(edge_vertices_002.outputs[0], math_002.inputs[0])
			#evaluate_at_index.Value -> math_003.Value
			edge_info.links.new(evaluate_at_index.outputs[0], math_003.inputs[0])
			#index_002.Index -> math_003.Value
			edge_info.links.new(index_002.outputs[0], math_003.inputs[1])
			#reroute_003.Output -> evaluate_at_index.Index
			edge_info.links.new(reroute_003.outputs[0], evaluate_at_index.inputs[0])
			#edge_vertices_002.Vertex Index 2 -> math_002.Value
			edge_info.links.new(edge_vertices_002.outputs[1], math_002.inputs[1])
			#switch_001.Output -> group_output.Edge Vector
			edge_info.links.new(switch_001.outputs[0], group_output.inputs[4])
			#group_input.Edge Index -> edges_of_vertex_002.Sort Index
			edge_info.links.new(group_input.outputs[0], edges_of_vertex_002.inputs[2])
			#reroute.Output -> switch.Switch
			edge_info.links.new(reroute.outputs[0], switch.inputs[0])
			#switch.Output -> group_output.Point Index
			edge_info.links.new(switch.outputs[0], group_output.inputs[1])
			#reroute.Output -> switch_001.Switch
			edge_info.links.new(reroute.outputs[0], switch_001.inputs[0])
			#reroute_002.Output -> group_output.Is Valid
			edge_info.links.new(reroute_002.outputs[0], group_output.inputs[0])
			#edges_of_vertex_002.Total -> compare.B
			edge_info.links.new(edges_of_vertex_002.outputs[1], compare.inputs[3])
			#reroute.Output -> switch_002.Switch
			edge_info.links.new(reroute.outputs[0], switch_002.inputs[0])
			#switch_002.Output -> group_output.Edge Index
			edge_info.links.new(switch_002.outputs[0], group_output.inputs[3])
			#group_input.Edge Index -> compare.A
			edge_info.links.new(group_input.outputs[0], compare.inputs[2])
			#reroute_003.Output -> switch_002.True
			edge_info.links.new(reroute_003.outputs[0], switch_002.inputs[2])
			#math_003.Value -> switch.True
			edge_info.links.new(math_003.outputs[0], switch.inputs[2])
			#reroute.Output -> switch_003.Switch
			edge_info.links.new(reroute.outputs[0], switch_003.inputs[0])
			#switch_003.Output -> group_output.Edge Length
			edge_info.links.new(switch_003.outputs[0], group_output.inputs[5])
			#reroute.Output -> reroute_001.Input
			edge_info.links.new(reroute.outputs[0], reroute_001.inputs[0])
			#reroute_001.Output -> reroute_002.Input
			edge_info.links.new(reroute_001.outputs[0], reroute_002.inputs[0])
			#compare.Result -> reroute.Input
			edge_info.links.new(compare.outputs[0], reroute.inputs[0])
			#vector_math.Vector -> vector_math_001.Vector
			edge_info.links.new(vector_math.outputs[0], vector_math_001.inputs[0])
			#position.Position -> vector_math.Vector
			edge_info.links.new(position.outputs[0], vector_math.inputs[1])
			#evaluate_at_index_001.Value -> vector_math.Vector
			edge_info.links.new(evaluate_at_index_001.outputs[0], vector_math.inputs[0])
			#position.Position -> evaluate_at_index_001.Value
			edge_info.links.new(position.outputs[0], evaluate_at_index_001.inputs[1])
			#math_003.Value -> evaluate_at_index_001.Index
			edge_info.links.new(math_003.outputs[0], evaluate_at_index_001.inputs[0])
			#vector_math.Vector -> switch_001.True
			edge_info.links.new(vector_math.outputs[0], switch_001.inputs[2])
			#vector_math_001.Value -> switch_003.True
			edge_info.links.new(vector_math_001.outputs[1], switch_003.inputs[2])
			#reroute_004.Output -> group_output.Point Position
			edge_info.links.new(reroute_004.outputs[0], group_output.inputs[2])
			#evaluate_at_index_001.Value -> reroute_004.Input
			edge_info.links.new(evaluate_at_index_001.outputs[0], reroute_004.inputs[0])
			#edges_of_vertex_002.Edge Index -> reroute_003.Input
			edge_info.links.new(edges_of_vertex_002.outputs[0], reroute_003.inputs[0])
			return edge_info

		edge_info = edge_info_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Edge Info", type = 'NODES')
		mod.node_group = edge_info
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Edge_Info.bl_idname)
			
def register():
	bpy.utils.register_class(Edge_Info)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Edge_Info)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
