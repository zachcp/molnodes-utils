bl_info = {
	"name" : "Vector Angle",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Vector_Angle(bpy.types.Operator):
	bl_idname = "node.vector_angle"
	bl_label = "Vector Angle"
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
			angle_socket.default_value = 0.0
			angle_socket.min_value = -3.4028234663852886e+38
			angle_socket.max_value = 3.4028234663852886e+38
			angle_socket.subtype = 'ANGLE'
			angle_socket.attribute_domain = 'POINT'
			angle_socket.description = "Angle between the two given vectors in radians"
			
			#Socket A
			a_socket = vector_angle.interface.new_socket(name = "A", in_out='INPUT', socket_type = 'NodeSocketVector')
			a_socket.default_value = (0.0, 0.0, 0.0)
			a_socket.min_value = -10000.0
			a_socket.max_value = 10000.0
			a_socket.subtype = 'NONE'
			a_socket.attribute_domain = 'POINT'
			
			#Socket B
			b_socket = vector_angle.interface.new_socket(name = "B", in_out='INPUT', socket_type = 'NodeSocketVector')
			b_socket.default_value = (0.0, 0.0, 0.0)
			b_socket.min_value = -10000.0
			b_socket.max_value = 10000.0
			b_socket.subtype = 'NONE'
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

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Vector Angle", type = 'NODES')
		mod.node_group = vector_angle
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Vector_Angle.bl_idname)
			
def register():
	bpy.utils.register_class(Vector_Angle)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Vector_Angle)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
