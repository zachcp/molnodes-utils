bl_info = {
	"name" : ".surface_blur_postion",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _surface_blur_postion(bpy.types.Operator):
	bl_idname = "node._surface_blur_postion"
	bl_label = ".surface_blur_postion"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _surface_blur_postion node group
		def _surface_blur_postion_node_group():
			_surface_blur_postion = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".surface_blur_postion")

			_surface_blur_postion.color_tag = 'NONE'
			_surface_blur_postion.description = ""

			_surface_blur_postion.is_modifier = True
			
			#_surface_blur_postion interface
			#Socket Geometry
			geometry_socket = _surface_blur_postion.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket_1 = _surface_blur_postion.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket_1.attribute_domain = 'POINT'
			
			#Socket Iterations
			iterations_socket = _surface_blur_postion.interface.new_socket(name = "Iterations", in_out='INPUT', socket_type = 'NodeSocketInt')
			iterations_socket.subtype = 'NONE'
			iterations_socket.default_value = 2
			iterations_socket.min_value = 0
			iterations_socket.max_value = 2147483647
			iterations_socket.attribute_domain = 'POINT'
			
			
			#initialize _surface_blur_postion nodes
			#node Frame
			frame = _surface_blur_postion.nodes.new("NodeFrame")
			frame.label = "Smoothen out weird bumps from meshing"
			frame.name = "Frame"
			frame.label_size = 20
			frame.shrink = True
			
			#node Group Input
			group_input = _surface_blur_postion.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Blur Attribute.001
			blur_attribute_001 = _surface_blur_postion.nodes.new("GeometryNodeBlurAttribute")
			blur_attribute_001.name = "Blur Attribute.001"
			blur_attribute_001.data_type = 'FLOAT_VECTOR'
			#Weight
			blur_attribute_001.inputs[2].default_value = 1.0
			
			#node Evaluate on Domain
			evaluate_on_domain = _surface_blur_postion.nodes.new("GeometryNodeFieldOnDomain")
			evaluate_on_domain.name = "Evaluate on Domain"
			evaluate_on_domain.data_type = 'FLOAT_VECTOR'
			evaluate_on_domain.domain = 'FACE'
			
			#node Position.002
			position_002 = _surface_blur_postion.nodes.new("GeometryNodeInputPosition")
			position_002.name = "Position.002"
			
			#node Evaluate on Domain.001
			evaluate_on_domain_001 = _surface_blur_postion.nodes.new("GeometryNodeFieldOnDomain")
			evaluate_on_domain_001.name = "Evaluate on Domain.001"
			evaluate_on_domain_001.data_type = 'FLOAT_VECTOR'
			evaluate_on_domain_001.domain = 'POINT'
			
			#node Set Position
			set_position = _surface_blur_postion.nodes.new("GeometryNodeSetPosition")
			set_position.name = "Set Position"
			#Selection
			set_position.inputs[1].default_value = True
			#Offset
			set_position.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Group Output
			group_output = _surface_blur_postion.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Blur Attribute
			blur_attribute = _surface_blur_postion.nodes.new("GeometryNodeBlurAttribute")
			blur_attribute.name = "Blur Attribute"
			blur_attribute.data_type = 'FLOAT_VECTOR'
			#Iterations
			blur_attribute.inputs[1].default_value = 4
			#Weight
			blur_attribute.inputs[2].default_value = 1.0
			
			#node Position
			position = _surface_blur_postion.nodes.new("GeometryNodeInputPosition")
			position.name = "Position"
			
			#node Set Position.001
			set_position_001 = _surface_blur_postion.nodes.new("GeometryNodeSetPosition")
			set_position_001.name = "Set Position.001"
			#Offset
			set_position_001.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Compare
			compare = _surface_blur_postion.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'EQUAL'
			#B_INT
			compare.inputs[3].default_value = 3
			
			#node Vertex Neighbors
			vertex_neighbors = _surface_blur_postion.nodes.new("GeometryNodeInputMeshVertexNeighbors")
			vertex_neighbors.name = "Vertex Neighbors"
			
			#node Edge Vertices
			edge_vertices = _surface_blur_postion.nodes.new("GeometryNodeInputMeshEdgeVertices")
			edge_vertices.name = "Edge Vertices"
			
			#node Evaluate at Index.001
			evaluate_at_index_001 = _surface_blur_postion.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_001.name = "Evaluate at Index.001"
			evaluate_at_index_001.data_type = 'BOOLEAN'
			evaluate_at_index_001.domain = 'POINT'
			
			#node Boolean Math
			boolean_math = _surface_blur_postion.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'AND'
			
			#node Edges to Face Groups
			edges_to_face_groups = _surface_blur_postion.nodes.new("GeometryNodeEdgesToFaceGroups")
			edges_to_face_groups.name = "Edges to Face Groups"
			
			#node Evaluate at Index
			evaluate_at_index = _surface_blur_postion.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index.name = "Evaluate at Index"
			evaluate_at_index.data_type = 'BOOLEAN'
			evaluate_at_index.domain = 'POINT'
			
			#node Face Group Boundaries
			face_group_boundaries = _surface_blur_postion.nodes.new("GeometryNodeMeshFaceSetBoundaries")
			face_group_boundaries.name = "Face Group Boundaries"
			
			
			
			#Set parents
			compare.parent = frame
			vertex_neighbors.parent = frame
			edge_vertices.parent = frame
			evaluate_at_index_001.parent = frame
			boolean_math.parent = frame
			edges_to_face_groups.parent = frame
			evaluate_at_index.parent = frame
			face_group_boundaries.parent = frame
			
			#Set locations
			frame.location = (0.0, 0.0)
			group_input.location = (-610.1629638671875, 0.0)
			blur_attribute_001.location = (-299.5, -120.0)
			evaluate_on_domain.location = (-459.5, -120.0)
			position_002.location = (-619.5, -120.0)
			evaluate_on_domain_001.location = (-119.5, -120.0)
			set_position.location = (60.5, 20.0)
			group_output.location = (680.947509765625, -17.612947463989258)
			blur_attribute.location = (460.0, -200.0)
			position.location = (460.0, -360.0)
			set_position_001.location = (460.784423828125, 10.757638931274414)
			compare.location = (-220.0, -560.0)
			vertex_neighbors.location = (-380.0, -560.0)
			edge_vertices.location = (-220.0, -420.0)
			evaluate_at_index_001.location = (-60.0, -580.0)
			boolean_math.location = (100.0, -420.0)
			edges_to_face_groups.location = (100.0, -560.0)
			evaluate_at_index.location = (-60.0, -420.0)
			face_group_boundaries.location = (100.0, -660.0)
			
			#Set dimensions
			frame.width, frame.height = 690.0, 385.0
			group_input.width, group_input.height = 140.0, 100.0
			blur_attribute_001.width, blur_attribute_001.height = 140.0, 100.0
			evaluate_on_domain.width, evaluate_on_domain.height = 140.0, 100.0
			position_002.width, position_002.height = 140.0, 100.0
			evaluate_on_domain_001.width, evaluate_on_domain_001.height = 140.0, 100.0
			set_position.width, set_position.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			blur_attribute.width, blur_attribute.height = 140.0, 100.0
			position.width, position.height = 140.0, 100.0
			set_position_001.width, set_position_001.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			vertex_neighbors.width, vertex_neighbors.height = 140.0, 100.0
			edge_vertices.width, edge_vertices.height = 140.0, 100.0
			evaluate_at_index_001.width, evaluate_at_index_001.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			edges_to_face_groups.width, edges_to_face_groups.height = 140.0, 100.0
			evaluate_at_index.width, evaluate_at_index.height = 140.0, 100.0
			face_group_boundaries.width, face_group_boundaries.height = 150.0, 100.0
			
			#initialize _surface_blur_postion links
			#evaluate_on_domain_001.Value -> set_position.Position
			_surface_blur_postion.links.new(evaluate_on_domain_001.outputs[0], set_position.inputs[2])
			#position_002.Position -> evaluate_on_domain.Value
			_surface_blur_postion.links.new(position_002.outputs[0], evaluate_on_domain.inputs[0])
			#blur_attribute_001.Value -> evaluate_on_domain_001.Value
			_surface_blur_postion.links.new(blur_attribute_001.outputs[0], evaluate_on_domain_001.inputs[0])
			#evaluate_on_domain.Value -> blur_attribute_001.Value
			_surface_blur_postion.links.new(evaluate_on_domain.outputs[0], blur_attribute_001.inputs[0])
			#group_input.Geometry -> set_position.Geometry
			_surface_blur_postion.links.new(group_input.outputs[0], set_position.inputs[0])
			#set_position_001.Geometry -> group_output.Geometry
			_surface_blur_postion.links.new(set_position_001.outputs[0], group_output.inputs[0])
			#group_input.Iterations -> blur_attribute_001.Iterations
			_surface_blur_postion.links.new(group_input.outputs[1], blur_attribute_001.inputs[1])
			#set_position.Geometry -> set_position_001.Geometry
			_surface_blur_postion.links.new(set_position.outputs[0], set_position_001.inputs[0])
			#vertex_neighbors.Vertex Count -> compare.A
			_surface_blur_postion.links.new(vertex_neighbors.outputs[0], compare.inputs[2])
			#compare.Result -> evaluate_at_index.Value
			_surface_blur_postion.links.new(compare.outputs[0], evaluate_at_index.inputs[1])
			#compare.Result -> evaluate_at_index_001.Value
			_surface_blur_postion.links.new(compare.outputs[0], evaluate_at_index_001.inputs[1])
			#edge_vertices.Vertex Index 1 -> evaluate_at_index.Index
			_surface_blur_postion.links.new(edge_vertices.outputs[0], evaluate_at_index.inputs[0])
			#edge_vertices.Vertex Index 2 -> evaluate_at_index_001.Index
			_surface_blur_postion.links.new(edge_vertices.outputs[1], evaluate_at_index_001.inputs[0])
			#evaluate_at_index.Value -> boolean_math.Boolean
			_surface_blur_postion.links.new(evaluate_at_index.outputs[0], boolean_math.inputs[0])
			#evaluate_at_index_001.Value -> boolean_math.Boolean
			_surface_blur_postion.links.new(evaluate_at_index_001.outputs[0], boolean_math.inputs[1])
			#boolean_math.Boolean -> edges_to_face_groups.Boundary Edges
			_surface_blur_postion.links.new(boolean_math.outputs[0], edges_to_face_groups.inputs[0])
			#edges_to_face_groups.Face Group ID -> face_group_boundaries.Face Group ID
			_surface_blur_postion.links.new(edges_to_face_groups.outputs[0], face_group_boundaries.inputs[0])
			#blur_attribute.Value -> set_position_001.Position
			_surface_blur_postion.links.new(blur_attribute.outputs[0], set_position_001.inputs[2])
			#position.Position -> blur_attribute.Value
			_surface_blur_postion.links.new(position.outputs[0], blur_attribute.inputs[0])
			#face_group_boundaries.Boundary Edges -> set_position_001.Selection
			_surface_blur_postion.links.new(face_group_boundaries.outputs[0], set_position_001.inputs[1])
			return _surface_blur_postion

		_surface_blur_postion = _surface_blur_postion_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".surface_blur_postion", type = 'NODES')
		mod.node_group = _surface_blur_postion
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_surface_blur_postion.bl_idname)
			
def register():
	bpy.utils.register_class(_surface_blur_postion)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_surface_blur_postion)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
