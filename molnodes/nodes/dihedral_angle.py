bl_info = {
	"name" : "Dihedral Angle",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Dihedral_Angle(bpy.types.Operator):
	bl_idname = "node.dihedral_angle"
	bl_label = "Dihedral Angle"
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

		#initialize dihedral_angle node group
		def dihedral_angle_node_group():
			dihedral_angle = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Dihedral Angle")

			dihedral_angle.color_tag = 'VECTOR'
			dihedral_angle.description = ""

			
			#dihedral_angle interface
			#Socket Angle
			angle_socket_1 = dihedral_angle.interface.new_socket(name = "Angle", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			angle_socket_1.subtype = 'ANGLE'
			angle_socket_1.default_value = 0.0
			angle_socket_1.min_value = -3.4028234663852886e+38
			angle_socket_1.max_value = 3.4028234663852886e+38
			angle_socket_1.attribute_domain = 'POINT'
			angle_socket_1.description = "The angle between the vectors AB and CD, when made perpendicular to BC."
			
			#Socket BA⟂(BC)
			ba__bc__socket = dihedral_angle.interface.new_socket(name = "BA⟂(BC)", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			ba__bc__socket.subtype = 'NONE'
			ba__bc__socket.default_value = (0.0, 0.0, 0.0)
			ba__bc__socket.min_value = -3.4028234663852886e+38
			ba__bc__socket.max_value = 3.4028234663852886e+38
			ba__bc__socket.attribute_domain = 'POINT'
			ba__bc__socket.description = "The vector BA when made perpendicular to  the axis BC"
			
			#Socket CD⟂(BC)
			cd__bc__socket = dihedral_angle.interface.new_socket(name = "CD⟂(BC)", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			cd__bc__socket.subtype = 'NONE'
			cd__bc__socket.default_value = (0.0, 0.0, 0.0)
			cd__bc__socket.min_value = -3.4028234663852886e+38
			cd__bc__socket.max_value = 3.4028234663852886e+38
			cd__bc__socket.attribute_domain = 'POINT'
			cd__bc__socket.description = "The Vector CD when makde perpendicular to the axis BC"
			
			#Socket BC
			bc_socket = dihedral_angle.interface.new_socket(name = "BC", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			bc_socket.subtype = 'NONE'
			bc_socket.default_value = (0.0, 0.0, 0.0)
			bc_socket.min_value = -3.4028234663852886e+38
			bc_socket.max_value = 3.4028234663852886e+38
			bc_socket.attribute_domain = 'POINT'
			bc_socket.description = "The axis vector BC"
			
			#Socket A
			a_socket_1 = dihedral_angle.interface.new_socket(name = "A", in_out='INPUT', socket_type = 'NodeSocketVector')
			a_socket_1.subtype = 'NONE'
			a_socket_1.default_value = (0.0, 0.0, 0.0)
			a_socket_1.min_value = -3.4028234663852886e+38
			a_socket_1.max_value = 3.4028234663852886e+38
			a_socket_1.attribute_domain = 'POINT'
			a_socket_1.description = "First vector for the calculation, which draws a line to B"
			
			#Socket B
			b_socket_1 = dihedral_angle.interface.new_socket(name = "B", in_out='INPUT', socket_type = 'NodeSocketVector')
			b_socket_1.subtype = 'NONE'
			b_socket_1.default_value = (0.0, 0.0, 0.0)
			b_socket_1.min_value = -3.4028234663852886e+38
			b_socket_1.max_value = 3.4028234663852886e+38
			b_socket_1.attribute_domain = 'POINT'
			b_socket_1.description = "Second vector for the calculation, which receives a line from A and draws a line to C"
			
			#Socket C
			c_socket = dihedral_angle.interface.new_socket(name = "C", in_out='INPUT', socket_type = 'NodeSocketVector')
			c_socket.subtype = 'NONE'
			c_socket.default_value = (0.0, 0.0, 0.0)
			c_socket.min_value = -3.4028234663852886e+38
			c_socket.max_value = 3.4028234663852886e+38
			c_socket.attribute_domain = 'POINT'
			c_socket.description = "Third vector for the calculation, which receives a line from B and draws a line to D"
			
			#Socket D
			d_socket = dihedral_angle.interface.new_socket(name = "D", in_out='INPUT', socket_type = 'NodeSocketVector')
			d_socket.subtype = 'NONE'
			d_socket.default_value = (0.0, 0.0, 0.0)
			d_socket.min_value = -3.4028234663852886e+38
			d_socket.max_value = 3.4028234663852886e+38
			d_socket.attribute_domain = 'POINT'
			d_socket.description = "Last vector for the calculation, which is the end point of the line from D"
			
			
			#initialize dihedral_angle nodes
			#node Vector Math.003
			vector_math_003 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_003.name = "Vector Math.003"
			vector_math_003.operation = 'SUBTRACT'
			
			#node Vector Math.004
			vector_math_004 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_004.name = "Vector Math.004"
			vector_math_004.operation = 'SUBTRACT'
			
			#node Vector Math.006
			vector_math_006 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_006.name = "Vector Math.006"
			vector_math_006.operation = 'SUBTRACT'
			
			#node Vector Math.007
			vector_math_007 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_007.name = "Vector Math.007"
			vector_math_007.operation = 'PROJECT'
			
			#node Vector Math.009
			vector_math_009 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_009.name = "Vector Math.009"
			vector_math_009.operation = 'PROJECT'
			
			#node Vector Math.008
			vector_math_008 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_008.name = "Vector Math.008"
			vector_math_008.operation = 'SUBTRACT'
			
			#node Vector Math.010
			vector_math_010 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_010.name = "Vector Math.010"
			vector_math_010.operation = 'SUBTRACT'
			
			#node MN_utils_vector_angle.002
			mn_utils_vector_angle_002 = dihedral_angle.nodes.new("GeometryNodeGroup")
			mn_utils_vector_angle_002.label = "Vector Angle"
			mn_utils_vector_angle_002.name = "MN_utils_vector_angle.002"
			mn_utils_vector_angle_002.node_tree = vector_angle
			
			#node Group Output
			group_output_1 = dihedral_angle.nodes.new("NodeGroupOutput")
			group_output_1.name = "Group Output"
			group_output_1.is_active_output = True
			
			#node Reroute.002
			reroute_002 = dihedral_angle.nodes.new("NodeReroute")
			reroute_002.name = "Reroute.002"
			#node Reroute.001
			reroute_001 = dihedral_angle.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			#node Vector Math
			vector_math_1 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_1.name = "Vector Math"
			vector_math_1.operation = 'CROSS_PRODUCT'
			
			#node Vector Math.001
			vector_math_001_1 = dihedral_angle.nodes.new("ShaderNodeVectorMath")
			vector_math_001_1.name = "Vector Math.001"
			vector_math_001_1.operation = 'DOT_PRODUCT'
			
			#node Math.001
			math_001 = dihedral_angle.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.operation = 'SIGN'
			math_001.use_clamp = False
			
			#node Reroute
			reroute = dihedral_angle.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Math
			math_1 = dihedral_angle.nodes.new("ShaderNodeMath")
			math_1.name = "Math"
			math_1.operation = 'MULTIPLY'
			math_1.use_clamp = False
			
			#node Group Input.003
			group_input_003 = dihedral_angle.nodes.new("NodeGroupInput")
			group_input_003.name = "Group Input.003"
			group_input_003.outputs[0].hide = True
			group_input_003.outputs[1].hide = True
			group_input_003.outputs[2].hide = True
			group_input_003.outputs[4].hide = True
			
			#node Group Input.001
			group_input_001 = dihedral_angle.nodes.new("NodeGroupInput")
			group_input_001.name = "Group Input.001"
			group_input_001.outputs[1].hide = True
			group_input_001.outputs[2].hide = True
			group_input_001.outputs[3].hide = True
			group_input_001.outputs[4].hide = True
			
			#node Group Input
			group_input_1 = dihedral_angle.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			group_input_1.outputs[0].hide = True
			group_input_1.outputs[2].hide = True
			group_input_1.outputs[3].hide = True
			group_input_1.outputs[4].hide = True
			
			#node Group Input.002
			group_input_002 = dihedral_angle.nodes.new("NodeGroupInput")
			group_input_002.name = "Group Input.002"
			group_input_002.outputs[0].hide = True
			group_input_002.outputs[1].hide = True
			group_input_002.outputs[3].hide = True
			group_input_002.outputs[4].hide = True
			
			
			
			
			#Set locations
			vector_math_003.location = (-142.68453979492188, 25.911895751953125)
			vector_math_004.location = (-140.0, 440.0)
			vector_math_006.location = (-140.0, 180.0)
			vector_math_007.location = (80.0, 320.0)
			vector_math_009.location = (80.0, -80.0)
			vector_math_008.location = (80.0, 460.0)
			vector_math_010.location = (80.0, 60.0)
			mn_utils_vector_angle_002.location = (420.0, 420.0)
			group_output_1.location = (920.0, 320.0)
			reroute_002.location = (300.0, 260.0)
			reroute_001.location = (300.0, 240.0)
			vector_math_1.location = (420.0, 180.0)
			vector_math_001_1.location = (420.0, 40.0)
			math_001.location = (580.0, 40.0)
			reroute.location = (300.0, 220.0)
			math_1.location = (640.0, 420.0)
			group_input_003.location = (-440.0, 0.0)
			group_input_001.location = (-440.0, 420.0)
			group_input_1.location = (-440.0, 280.0)
			group_input_002.location = (-440.0, 140.0)
			
			#Set dimensions
			vector_math_003.width, vector_math_003.height = 140.0, 100.0
			vector_math_004.width, vector_math_004.height = 140.0, 100.0
			vector_math_006.width, vector_math_006.height = 140.0, 100.0
			vector_math_007.width, vector_math_007.height = 140.0, 100.0
			vector_math_009.width, vector_math_009.height = 140.0, 100.0
			vector_math_008.width, vector_math_008.height = 140.0, 100.0
			vector_math_010.width, vector_math_010.height = 140.0, 100.0
			mn_utils_vector_angle_002.width, mn_utils_vector_angle_002.height = 200.0, 100.0
			group_output_1.width, group_output_1.height = 140.0, 100.0
			reroute_002.width, reroute_002.height = 16.0, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			vector_math_1.width, vector_math_1.height = 140.0, 100.0
			vector_math_001_1.width, vector_math_001_1.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			math_1.width, math_1.height = 140.0, 100.0
			group_input_003.width, group_input_003.height = 140.0, 100.0
			group_input_001.width, group_input_001.height = 140.0, 100.0
			group_input_1.width, group_input_1.height = 140.0, 100.0
			group_input_002.width, group_input_002.height = 140.0, 100.0
			
			#initialize dihedral_angle links
			#vector_math_007.Vector -> vector_math_008.Vector
			dihedral_angle.links.new(vector_math_007.outputs[0], vector_math_008.inputs[1])
			#vector_math_009.Vector -> vector_math_010.Vector
			dihedral_angle.links.new(vector_math_009.outputs[0], vector_math_010.inputs[1])
			#vector_math_004.Vector -> vector_math_007.Vector
			dihedral_angle.links.new(vector_math_004.outputs[0], vector_math_007.inputs[0])
			#vector_math_006.Vector -> vector_math_007.Vector
			dihedral_angle.links.new(vector_math_006.outputs[0], vector_math_007.inputs[1])
			#reroute_002.Output -> mn_utils_vector_angle_002.A
			dihedral_angle.links.new(reroute_002.outputs[0], mn_utils_vector_angle_002.inputs[0])
			#vector_math_004.Vector -> vector_math_008.Vector
			dihedral_angle.links.new(vector_math_004.outputs[0], vector_math_008.inputs[0])
			#vector_math_003.Vector -> vector_math_010.Vector
			dihedral_angle.links.new(vector_math_003.outputs[0], vector_math_010.inputs[0])
			#vector_math_003.Vector -> vector_math_009.Vector
			dihedral_angle.links.new(vector_math_003.outputs[0], vector_math_009.inputs[0])
			#vector_math_006.Vector -> vector_math_009.Vector
			dihedral_angle.links.new(vector_math_006.outputs[0], vector_math_009.inputs[1])
			#vector_math_006.Vector -> reroute.Input
			dihedral_angle.links.new(vector_math_006.outputs[0], reroute.inputs[0])
			#reroute_001.Output -> mn_utils_vector_angle_002.B
			dihedral_angle.links.new(reroute_001.outputs[0], mn_utils_vector_angle_002.inputs[1])
			#vector_math_1.Vector -> vector_math_001_1.Vector
			dihedral_angle.links.new(vector_math_1.outputs[0], vector_math_001_1.inputs[0])
			#reroute.Output -> vector_math_001_1.Vector
			dihedral_angle.links.new(reroute.outputs[0], vector_math_001_1.inputs[1])
			#mn_utils_vector_angle_002.Angle -> math_1.Value
			dihedral_angle.links.new(mn_utils_vector_angle_002.outputs[0], math_1.inputs[0])
			#reroute_001.Output -> vector_math_1.Vector
			dihedral_angle.links.new(reroute_001.outputs[0], vector_math_1.inputs[1])
			#group_input_002.C -> vector_math_003.Vector
			dihedral_angle.links.new(group_input_002.outputs[2], vector_math_003.inputs[1])
			#group_input_1.B -> vector_math_004.Vector
			dihedral_angle.links.new(group_input_1.outputs[1], vector_math_004.inputs[1])
			#group_input_1.B -> vector_math_006.Vector
			dihedral_angle.links.new(group_input_1.outputs[1], vector_math_006.inputs[1])
			#group_input_002.C -> vector_math_006.Vector
			dihedral_angle.links.new(group_input_002.outputs[2], vector_math_006.inputs[0])
			#math_1.Value -> group_output_1.Angle
			dihedral_angle.links.new(math_1.outputs[0], group_output_1.inputs[0])
			#reroute_002.Output -> group_output_1.BA⟂(BC)
			dihedral_angle.links.new(reroute_002.outputs[0], group_output_1.inputs[1])
			#reroute.Output -> group_output_1.BC
			dihedral_angle.links.new(reroute.outputs[0], group_output_1.inputs[3])
			#reroute_001.Output -> group_output_1.CD⟂(BC)
			dihedral_angle.links.new(reroute_001.outputs[0], group_output_1.inputs[2])
			#reroute_002.Output -> vector_math_1.Vector
			dihedral_angle.links.new(reroute_002.outputs[0], vector_math_1.inputs[0])
			#vector_math_001_1.Value -> math_001.Value
			dihedral_angle.links.new(vector_math_001_1.outputs[1], math_001.inputs[0])
			#math_001.Value -> math_1.Value
			dihedral_angle.links.new(math_001.outputs[0], math_1.inputs[1])
			#vector_math_010.Vector -> reroute_001.Input
			dihedral_angle.links.new(vector_math_010.outputs[0], reroute_001.inputs[0])
			#vector_math_008.Vector -> reroute_002.Input
			dihedral_angle.links.new(vector_math_008.outputs[0], reroute_002.inputs[0])
			#group_input_001.A -> vector_math_004.Vector
			dihedral_angle.links.new(group_input_001.outputs[0], vector_math_004.inputs[0])
			#group_input_003.D -> vector_math_003.Vector
			dihedral_angle.links.new(group_input_003.outputs[3], vector_math_003.inputs[0])
			return dihedral_angle

		dihedral_angle = dihedral_angle_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Dihedral Angle", type = 'NODES')
		mod.node_group = dihedral_angle
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Dihedral_Angle.bl_idname)
			
def register():
	bpy.utils.register_class(Dihedral_Angle)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Dihedral_Angle)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
