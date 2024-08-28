bl_info = {
	"name" : "Point Distance",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Point_Distance(bpy.types.Operator):
	bl_idname = "node.point_distance"
	bl_label = "Point Distance"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize point_distance node group
		def point_distance_node_group():
			point_distance = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Point Distance")

			point_distance.color_tag = 'CONVERTER'
			point_distance.description = ""

			
			#point_distance interface
			#Socket Vector
			vector_socket = point_distance.interface.new_socket(name = "Vector", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			vector_socket.default_value = (0.0, 0.0, 0.0)
			vector_socket.min_value = -3.4028234663852886e+38
			vector_socket.max_value = 3.4028234663852886e+38
			vector_socket.subtype = 'NONE'
			vector_socket.attribute_domain = 'POINT'
			vector_socket.description = "Vector from the current point to the indexed point"
			
			#Socket Distance
			distance_socket = point_distance.interface.new_socket(name = "Distance", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			distance_socket.default_value = 0.0
			distance_socket.min_value = -3.4028234663852886e+38
			distance_socket.max_value = 3.4028234663852886e+38
			distance_socket.subtype = 'NONE'
			distance_socket.attribute_domain = 'POINT'
			distance_socket.description = "Distance from the current point to the indexed point"
			
			#Socket Index
			index_socket = point_distance.interface.new_socket(name = "Index", in_out='INPUT', socket_type = 'NodeSocketInt')
			index_socket.default_value = 100
			index_socket.min_value = 0
			index_socket.max_value = 2147483647
			index_socket.subtype = 'NONE'
			index_socket.attribute_domain = 'POINT'
			index_socket.description = "Index for the selected point to measure to"
			
			
			#initialize point_distance nodes
			#node Evaluate at Index
			evaluate_at_index = point_distance.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index.name = "Evaluate at Index"
			evaluate_at_index.data_type = 'FLOAT_VECTOR'
			evaluate_at_index.domain = 'POINT'
			
			#node Vector Math
			vector_math = point_distance.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.operation = 'SUBTRACT'
			
			#node Group Input
			group_input = point_distance.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Position
			position = point_distance.nodes.new("GeometryNodeInputPosition")
			position.name = "Position"
			
			#node Group Output
			group_output = point_distance.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Vector Math.001
			vector_math_001 = point_distance.nodes.new("ShaderNodeVectorMath")
			vector_math_001.name = "Vector Math.001"
			vector_math_001.operation = 'LENGTH'
			
			
			
			
			#Set locations
			evaluate_at_index.location = (-100.06727600097656, 80.02735900878906)
			vector_math.location = (53.334869384765625, 83.23219299316406)
			group_input.location = (-280.0, 40.0)
			position.location = (-280.0, -60.0)
			group_output.location = (420.0, 80.0)
			vector_math_001.location = (220.0, 40.0)
			
			#Set dimensions
			evaluate_at_index.width, evaluate_at_index.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			position.width, position.height = 147.27230834960938, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			vector_math_001.width, vector_math_001.height = 140.0, 100.0
			
			#initialize point_distance links
			#vector_math.Vector -> vector_math_001.Vector
			point_distance.links.new(vector_math.outputs[0], vector_math_001.inputs[0])
			#position.Position -> vector_math.Vector
			point_distance.links.new(position.outputs[0], vector_math.inputs[1])
			#evaluate_at_index.Value -> vector_math.Vector
			point_distance.links.new(evaluate_at_index.outputs[0], vector_math.inputs[0])
			#position.Position -> evaluate_at_index.Value
			point_distance.links.new(position.outputs[0], evaluate_at_index.inputs[1])
			#group_input.Index -> evaluate_at_index.Index
			point_distance.links.new(group_input.outputs[0], evaluate_at_index.inputs[0])
			#vector_math.Vector -> group_output.Vector
			point_distance.links.new(vector_math.outputs[0], group_output.inputs[0])
			#vector_math_001.Value -> group_output.Distance
			point_distance.links.new(vector_math_001.outputs[1], group_output.inputs[1])
			return point_distance

		point_distance = point_distance_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Point Distance", type = 'NODES')
		mod.node_group = point_distance
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Point_Distance.bl_idname)
			
def register():
	bpy.utils.register_class(Point_Distance)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Point_Distance)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
