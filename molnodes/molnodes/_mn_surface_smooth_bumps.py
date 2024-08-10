bl_info = {
	"name" : ".MN_surface_smooth_bumps",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _MN_surface_smooth_bumps(bpy.types.Operator):
	bl_idname = "node._mn_surface_smooth_bumps"
	bl_label = ".MN_surface_smooth_bumps"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _mn_surface_smooth_bumps node group
		def _mn_surface_smooth_bumps_node_group():
			_mn_surface_smooth_bumps = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_surface_smooth_bumps")

			_mn_surface_smooth_bumps.color_tag = 'NONE'
			_mn_surface_smooth_bumps.description = ""

			_mn_surface_smooth_bumps.is_modifier = True
			
			#_mn_surface_smooth_bumps interface
			#Socket Geometry
			geometry_socket = _mn_surface_smooth_bumps.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_1 = _mn_surface_smooth_bumps.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_1.attribute_domain = 'POINT'
			
			
			#initialize _mn_surface_smooth_bumps nodes
			#node Frame
			frame = _mn_surface_smooth_bumps.nodes.new("NodeFrame")
			frame.label = "Smoothen out weird bumps from meshing"
			frame.name = "Frame"
			frame.label_size = 20
			frame.shrink = True
			
			#node Group Input
			group_input = _mn_surface_smooth_bumps.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Group Output
			group_output = _mn_surface_smooth_bumps.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Set Position.001
			set_position_001 = _mn_surface_smooth_bumps.nodes.new("GeometryNodeSetPosition")
			set_position_001.name = "Set Position.001"
			#Offset
			set_position_001.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Blur Attribute
			blur_attribute = _mn_surface_smooth_bumps.nodes.new("GeometryNodeBlurAttribute")
			blur_attribute.name = "Blur Attribute"
			blur_attribute.data_type = 'FLOAT_VECTOR'
			#Iterations
			blur_attribute.inputs[1].default_value = 4
			#Weight
			blur_attribute.inputs[2].default_value = 1.0
			
			#node Position
			position = _mn_surface_smooth_bumps.nodes.new("GeometryNodeInputPosition")
			position.name = "Position"
			
			#node Compare
			compare = _mn_surface_smooth_bumps.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'EQUAL'
			#B_INT
			compare.inputs[3].default_value = 3
			
			#node Vertex Neighbors
			vertex_neighbors = _mn_surface_smooth_bumps.nodes.new("GeometryNodeInputMeshVertexNeighbors")
			vertex_neighbors.name = "Vertex Neighbors"
			
			#node Edge Vertices
			edge_vertices = _mn_surface_smooth_bumps.nodes.new("GeometryNodeInputMeshEdgeVertices")
			edge_vertices.name = "Edge Vertices"
			
			#node Evaluate at Index.001
			evaluate_at_index_001 = _mn_surface_smooth_bumps.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001.name = "Evaluate at Index.001"
			evaluate_at_index_001.data_type = 'BOOLEAN'
			evaluate_at_index_001.domain = 'POINT'
			
			#node Evaluate at Index
			evaluate_at_index = _mn_surface_smooth_bumps.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index.name = "Evaluate at Index"
			evaluate_at_index.data_type = 'BOOLEAN'
			evaluate_at_index.domain = 'POINT'
			
			#node Boolean Math
			boolean_math = _mn_surface_smooth_bumps.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'AND'
			
			#node Edges to Face Groups
			edges_to_face_groups = _mn_surface_smooth_bumps.nodes.new("GeometryNodeEdgesToFaceGroups")
			edges_to_face_groups.name = "Edges to Face Groups"
			
			#node Face Group Boundaries
			face_group_boundaries = _mn_surface_smooth_bumps.nodes.new("GeometryNodeMeshFaceSetBoundaries")
			face_group_boundaries.name = "Face Group Boundaries"
			
			
			
			#Set parents
			compare.parent = frame
			vertex_neighbors.parent = frame
			edge_vertices.parent = frame
			evaluate_at_index_001.parent = frame
			evaluate_at_index.parent = frame
			boolean_math.parent = frame
			edges_to_face_groups.parent = frame
			face_group_boundaries.parent = frame
			
			#Set locations
			frame.location = (-385.91619873046875, 67.19032287597656)
			group_input.location = (-610.1629638671875, 0.0)
			group_output.location = (900.947509765625, -17.612947463989258)
			set_position_001.location = (460.784423828125, 10.757638931274414)
			blur_attribute.location = (460.0, -220.0)
			position.location = (460.0, -400.0)
			compare.location = (-220.0, -560.0)
			vertex_neighbors.location = (-380.0, -560.0)
			edge_vertices.location = (-220.0, -420.0)
			evaluate_at_index_001.location = (-60.0, -580.0)
			evaluate_at_index.location = (-60.0, -420.0)
			boolean_math.location = (100.0, -420.0)
			edges_to_face_groups.location = (100.0, -560.0)
			face_group_boundaries.location = (103.8720703125, -322.7563171386719)
			
			#Set dimensions
			frame.width, frame.height = 694.0, 477.0
			group_input.width, group_input.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			set_position_001.width, set_position_001.height = 140.0, 100.0
			blur_attribute.width, blur_attribute.height = 140.0, 100.0
			position.width, position.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			vertex_neighbors.width, vertex_neighbors.height = 140.0, 100.0
			edge_vertices.width, edge_vertices.height = 140.0, 100.0
			evaluate_at_index_001.width, evaluate_at_index_001.height = 140.0, 100.0
			evaluate_at_index.width, evaluate_at_index.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			edges_to_face_groups.width, edges_to_face_groups.height = 140.0, 100.0
			face_group_boundaries.width, face_group_boundaries.height = 150.0, 100.0
			
			#initialize _mn_surface_smooth_bumps links
			#set_position_001.Geometry -> group_output.Geometry
			_mn_surface_smooth_bumps.links.new(set_position_001.outputs[0], group_output.inputs[0])
			#group_input.Geometry -> set_position_001.Geometry
			_mn_surface_smooth_bumps.links.new(group_input.outputs[0], set_position_001.inputs[0])
			#vertex_neighbors.Vertex Count -> compare.A
			_mn_surface_smooth_bumps.links.new(vertex_neighbors.outputs[0], compare.inputs[2])
			#compare.Result -> evaluate_at_index.Value
			_mn_surface_smooth_bumps.links.new(compare.outputs[0], evaluate_at_index.inputs[1])
			#compare.Result -> evaluate_at_index_001.Value
			_mn_surface_smooth_bumps.links.new(compare.outputs[0], evaluate_at_index_001.inputs[1])
			#edge_vertices.Vertex Index 1 -> evaluate_at_index.Index
			_mn_surface_smooth_bumps.links.new(edge_vertices.outputs[0], evaluate_at_index.inputs[0])
			#edge_vertices.Vertex Index 2 -> evaluate_at_index_001.Index
			_mn_surface_smooth_bumps.links.new(edge_vertices.outputs[1], evaluate_at_index_001.inputs[0])
			#evaluate_at_index.Value -> boolean_math.Boolean
			_mn_surface_smooth_bumps.links.new(evaluate_at_index.outputs[0], boolean_math.inputs[0])
			#evaluate_at_index_001.Value -> boolean_math.Boolean
			_mn_surface_smooth_bumps.links.new(evaluate_at_index_001.outputs[0], boolean_math.inputs[1])
			#boolean_math.Boolean -> edges_to_face_groups.Boundary Edges
			_mn_surface_smooth_bumps.links.new(boolean_math.outputs[0], edges_to_face_groups.inputs[0])
			#edges_to_face_groups.Face Group ID -> face_group_boundaries.Face Group ID
			_mn_surface_smooth_bumps.links.new(edges_to_face_groups.outputs[0], face_group_boundaries.inputs[0])
			#blur_attribute.Value -> set_position_001.Position
			_mn_surface_smooth_bumps.links.new(blur_attribute.outputs[0], set_position_001.inputs[2])
			#position.Position -> blur_attribute.Value
			_mn_surface_smooth_bumps.links.new(position.outputs[0], blur_attribute.inputs[0])
			#face_group_boundaries.Boundary Edges -> set_position_001.Selection
			_mn_surface_smooth_bumps.links.new(face_group_boundaries.outputs[0], set_position_001.inputs[1])
			return _mn_surface_smooth_bumps

		_mn_surface_smooth_bumps = _mn_surface_smooth_bumps_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".MN_surface_smooth_bumps", type = 'NODES')
		mod.node_group = _mn_surface_smooth_bumps
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_MN_surface_smooth_bumps.bl_idname)
			
def register():
	bpy.utils.register_class(_MN_surface_smooth_bumps)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_MN_surface_smooth_bumps)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
