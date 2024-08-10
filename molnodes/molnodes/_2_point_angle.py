bl_info = {
	"name" : "2 Point Angle",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _2_Point_Angle(bpy.types.Operator):
	bl_idname = "node._2_point_angle"
	bl_label = "2 Point Angle"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize vector_angle node group
		def vector_angle_node_group():
			vector_angle = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Vector Angle")

			vector_angle.color_tag = 'VECTOR'
			vector_angle.description = ""

			
			#vector_angle interface
			#Socket Angle
			angle_socket = vector_angle.interface.new_socket(name = "Angle", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			angle_socket.subtype = 'ANGLE'
			angle_socket.default_value = 0.0
			angle_socket.min_value = -3.4028234663852886e+38
			angle_socket.max_value = 3.4028234663852886e+38
			angle_socket.attribute_domain = 'POINT'
			angle_socket.description = "Angle between the two given vectors in radians"
			
			#Socket A
			a_socket = vector_angle.interface.new_socket(name = "A", in_out='INPUT', socket_type = 'NodeSocketVector')
			a_socket.subtype = 'NONE'
			a_socket.default_value = (0.0, 0.0, 0.0)
			a_socket.min_value = -10000.0
			a_socket.max_value = 10000.0
			a_socket.attribute_domain = 'POINT'
			
			#Socket B
			b_socket = vector_angle.interface.new_socket(name = "B", in_out='INPUT', socket_type = 'NodeSocketVector')
			b_socket.subtype = 'NONE'
			b_socket.default_value = (0.0, 0.0, 0.0)
			b_socket.min_value = -10000.0
			b_socket.max_value = 10000.0
			b_socket.attribute_domain = 'POINT'
			
			
			#initialize vector_angle nodes
			#node Group Input
			group_input = vector_angle.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Vector Math.002
			vector_math_002 = vector_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_002.name = "Vector Math.002"
			vector_math_002.operation = 'NORMALIZE'
			
			#node Vector Math.001
			vector_math_001 = vector_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_001.name = "Vector Math.001"
			vector_math_001.operation = 'NORMALIZE'
			
			#node Vector Math
			vector_math = vector_angle.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.operation = 'DOT_PRODUCT'
			
			#node Math
			math = vector_angle.nodes.new("ShaderNodeMath")
			math.name = "Math"
			math.operation = 'ARCCOSINE'
			math.use_clamp = False
			
			#node Group Output
			group_output = vector_angle.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			
			
			
			#Set locations
			group_input.location = (-360.0, 0.0)
			vector_math_002.location = (-160.0, -60.0)
			vector_math_001.location = (-160.0, 60.0)
			vector_math.location = (0.0, 60.0)
			math.location = (160.0, 60.0)
			group_output.location = (340.0, 60.0)
			
			#Set dimensions
			group_input.width, group_input.height = 140.0, 100.0
			vector_math_002.width, vector_math_002.height = 140.0, 100.0
			vector_math_001.width, vector_math_001.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			
			#initialize vector_angle links
			#vector_math.Value -> math.Value
			vector_angle.links.new(vector_math.outputs[1], math.inputs[0])
			#vector_math_002.Vector -> vector_math.Vector
			vector_angle.links.new(vector_math_002.outputs[0], vector_math.inputs[1])
			#vector_math_001.Vector -> vector_math.Vector
			vector_angle.links.new(vector_math_001.outputs[0], vector_math.inputs[0])
			#math.Value -> group_output.Angle
			vector_angle.links.new(math.outputs[0], group_output.inputs[0])
			#group_input.A -> vector_math_001.Vector
			vector_angle.links.new(group_input.outputs[0], vector_math_001.inputs[0])
			#group_input.B -> vector_math_002.Vector
			vector_angle.links.new(group_input.outputs[1], vector_math_002.inputs[0])
			return vector_angle

		vector_angle = vector_angle_node_group()

		#initialize _2_point_angle node group
		def _2_point_angle_node_group():
			_2_point_angle = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "2 Point Angle")

			_2_point_angle.color_tag = 'CONVERTER'
			_2_point_angle.description = ""

			
			#_2_point_angle interface
			#Socket Angle
			angle_socket_1 = _2_point_angle.interface.new_socket(name = "Angle", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			angle_socket_1.subtype = 'NONE'
			angle_socket_1.default_value = 0.0
			angle_socket_1.min_value = -3.4028234663852886e+38
			angle_socket_1.max_value = 3.4028234663852886e+38
			angle_socket_1.attribute_domain = 'POINT'
			angle_socket_1.description = "Angle of the line A -> Self -> C in radians"
			
			#Socket Index A
			index_a_socket = _2_point_angle.interface.new_socket(name = "Index A", in_out='INPUT', socket_type = 'NodeSocketInt')
			index_a_socket.subtype = 'NONE'
			index_a_socket.default_value = 0
			index_a_socket.min_value = 0
			index_a_socket.max_value = 2147483647
			index_a_socket.attribute_domain = 'POINT'
			index_a_socket.description = "First end point for the angle calculation around the current point"
			
			#Socket Index C
			index_c_socket = _2_point_angle.interface.new_socket(name = "Index C", in_out='INPUT', socket_type = 'NodeSocketInt')
			index_c_socket.subtype = 'NONE'
			index_c_socket.default_value = 2
			index_c_socket.min_value = 0
			index_c_socket.max_value = 2147483647
			index_c_socket.attribute_domain = 'POINT'
			index_c_socket.description = "Last end point for the angle calculation around the current point"
			
			
			#initialize _2_point_angle nodes
			#node Group Input
			group_input_1 = _2_point_angle.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			
			#node Position
			position = _2_point_angle.nodes.new("GeometryNodeInputPosition")
			position.name = "Position"
			
			#node Evaluate at Index.002
			evaluate_at_index_002 = _2_point_angle.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index_002.name = "Evaluate at Index.002"
			evaluate_at_index_002.data_type = 'FLOAT_VECTOR'
			evaluate_at_index_002.domain = 'POINT'
			
			#node Evaluate at Index
			evaluate_at_index = _2_point_angle.nodes.new("GeometryNodeFieldAtIndex")
			evaluate_at_index.name = "Evaluate at Index"
			evaluate_at_index.data_type = 'FLOAT_VECTOR'
			evaluate_at_index.domain = 'POINT'
			
			#node Vector Math
			vector_math_1 = _2_point_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_1.name = "Vector Math"
			vector_math_1.operation = 'SUBTRACT'
			
			#node Vector Math.001
			vector_math_001_1 = _2_point_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_001_1.name = "Vector Math.001"
			vector_math_001_1.operation = 'SUBTRACT'
			
			#node Group.075
			group_075 = _2_point_angle.nodes.new("GeometryNodeGroup")
			group_075.name = "Group.075"
			group_075.node_tree = vector_angle
			
			#node Group Output
			group_output_1 = _2_point_angle.nodes.new("NodeGroupOutput")
			group_output_1.name = "Group Output"
			group_output_1.is_active_output = True
			
			
			
			
			#Set locations
			group_input_1.location = (-486.337646484375, 0.0)
			position.location = (-286.337646484375, -9.940185546875)
			evaluate_at_index_002.location = (-80.0, -60.0)
			evaluate_at_index.location = (-73.662353515625, 159.709716796875)
			vector_math_1.location = (106.638427734375, 160.290283203125)
			vector_math_001_1.location = (100.0, 20.0)
			group_075.location = (286.337646484375, 159.709716796875)
			group_output_1.location = (460.0, 160.0)
			
			#Set dimensions
			group_input_1.width, group_input_1.height = 140.0, 100.0
			position.width, position.height = 140.0, 100.0
			evaluate_at_index_002.width, evaluate_at_index_002.height = 140.0, 100.0
			evaluate_at_index.width, evaluate_at_index.height = 140.0, 100.0
			vector_math_1.width, vector_math_1.height = 140.0, 100.0
			vector_math_001_1.width, vector_math_001_1.height = 140.0, 100.0
			group_075.width, group_075.height = 140.0, 100.0
			group_output_1.width, group_output_1.height = 140.0, 100.0
			
			#initialize _2_point_angle links
			#evaluate_at_index_002.Value -> vector_math_001_1.Vector
			_2_point_angle.links.new(evaluate_at_index_002.outputs[0], vector_math_001_1.inputs[0])
			#vector_math_1.Vector -> group_075.A
			_2_point_angle.links.new(vector_math_1.outputs[0], group_075.inputs[0])
			#evaluate_at_index.Value -> vector_math_1.Vector
			_2_point_angle.links.new(evaluate_at_index.outputs[0], vector_math_1.inputs[0])
			#position.Position -> evaluate_at_index_002.Value
			_2_point_angle.links.new(position.outputs[0], evaluate_at_index_002.inputs[1])
			#position.Position -> vector_math_001_1.Vector
			_2_point_angle.links.new(position.outputs[0], vector_math_001_1.inputs[1])
			#vector_math_001_1.Vector -> group_075.B
			_2_point_angle.links.new(vector_math_001_1.outputs[0], group_075.inputs[1])
			#position.Position -> vector_math_1.Vector
			_2_point_angle.links.new(position.outputs[0], vector_math_1.inputs[1])
			#position.Position -> evaluate_at_index.Value
			_2_point_angle.links.new(position.outputs[0], evaluate_at_index.inputs[1])
			#group_input_1.Index A -> evaluate_at_index.Index
			_2_point_angle.links.new(group_input_1.outputs[0], evaluate_at_index.inputs[0])
			#group_input_1.Index C -> evaluate_at_index_002.Index
			_2_point_angle.links.new(group_input_1.outputs[1], evaluate_at_index_002.inputs[0])
			#group_075.Angle -> group_output_1.Angle
			_2_point_angle.links.new(group_075.outputs[0], group_output_1.inputs[0])
			return _2_point_angle

		_2_point_angle = _2_point_angle_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "2 Point Angle", type = 'NODES')
		mod.node_group = _2_point_angle
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_2_Point_Angle.bl_idname)
			
def register():
	bpy.utils.register_class(_2_Point_Angle)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_2_Point_Angle)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
