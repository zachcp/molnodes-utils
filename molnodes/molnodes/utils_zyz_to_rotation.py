bl_info = {
	"name" : "Utils ZYZ to Rotation",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Utils_ZYZ_to_Rotation(bpy.types.Operator):
	bl_idname = "node.utils_zyz_to_rotation"
	bl_label = "Utils ZYZ to Rotation"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize utils_zyz_to_rotation node group
		def utils_zyz_to_rotation_node_group():
			utils_zyz_to_rotation = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Utils ZYZ to Rotation")

			utils_zyz_to_rotation.color_tag = 'CONVERTER'
			utils_zyz_to_rotation.description = ""

			
			#utils_zyz_to_rotation interface
			#Socket Rotation
			rotation_socket = utils_zyz_to_rotation.interface.new_socket(name = "Rotation", in_out='OUTPUT', socket_type = 'NodeSocketRotation')
			rotation_socket.attribute_domain = 'POINT'
			
			#Socket Phi
			phi_socket = utils_zyz_to_rotation.interface.new_socket(name = "Phi", in_out='INPUT', socket_type = 'NodeSocketFloat')
			phi_socket.subtype = 'NONE'
			phi_socket.default_value = 0.5
			phi_socket.min_value = -10000.0
			phi_socket.max_value = 10000.0
			phi_socket.attribute_domain = 'POINT'
			
			#Socket Theta
			theta_socket = utils_zyz_to_rotation.interface.new_socket(name = "Theta", in_out='INPUT', socket_type = 'NodeSocketFloat')
			theta_socket.subtype = 'NONE'
			theta_socket.default_value = 0.5
			theta_socket.min_value = -10000.0
			theta_socket.max_value = 10000.0
			theta_socket.attribute_domain = 'POINT'
			
			#Socket Psi
			psi_socket = utils_zyz_to_rotation.interface.new_socket(name = "Psi", in_out='INPUT', socket_type = 'NodeSocketFloat')
			psi_socket.subtype = 'NONE'
			psi_socket.default_value = 0.5
			psi_socket.min_value = -10000.0
			psi_socket.max_value = 10000.0
			psi_socket.attribute_domain = 'POINT'
			
			
			#initialize utils_zyz_to_rotation nodes
			#node Math.002
			math_002 = utils_zyz_to_rotation.nodes.new("ShaderNodeMath")
			math_002.name = "Math.002"
			math_002.operation = 'RADIANS'
			math_002.use_clamp = False
			
			#node Rotation to Euler.001
			rotation_to_euler_001 = utils_zyz_to_rotation.nodes.new("FunctionNodeRotationToEuler")
			rotation_to_euler_001.name = "Rotation to Euler.001"
			
			#node Axis Angle to Rotation.001
			axis_angle_to_rotation_001 = utils_zyz_to_rotation.nodes.new("FunctionNodeAxisAngleToRotation")
			axis_angle_to_rotation_001.name = "Axis Angle to Rotation.001"
			#Axis
			axis_angle_to_rotation_001.inputs[0].default_value = (0.0, 1.0, 0.0)
			
			#node Math.003
			math_003 = utils_zyz_to_rotation.nodes.new("ShaderNodeMath")
			math_003.name = "Math.003"
			math_003.operation = 'MULTIPLY'
			math_003.use_clamp = False
			#Value_001
			math_003.inputs[1].default_value = -1.0
			
			#node Rotate Euler
			rotate_euler = utils_zyz_to_rotation.nodes.new("FunctionNodeRotateEuler")
			rotate_euler.name = "Rotate Euler"
			rotate_euler.rotation_type = 'EULER'
			rotate_euler.space = 'OBJECT'
			
			#node Rotation to Euler
			rotation_to_euler = utils_zyz_to_rotation.nodes.new("FunctionNodeRotationToEuler")
			rotation_to_euler.name = "Rotation to Euler"
			
			#node Axis Angle to Rotation
			axis_angle_to_rotation = utils_zyz_to_rotation.nodes.new("FunctionNodeAxisAngleToRotation")
			axis_angle_to_rotation.name = "Axis Angle to Rotation"
			#Axis
			axis_angle_to_rotation.inputs[0].default_value = (0.0, 0.0, 1.0)
			
			#node Math.004
			math_004 = utils_zyz_to_rotation.nodes.new("ShaderNodeMath")
			math_004.name = "Math.004"
			math_004.operation = 'MULTIPLY'
			math_004.use_clamp = False
			#Value_001
			math_004.inputs[1].default_value = -1.0
			
			#node Math.005
			math_005 = utils_zyz_to_rotation.nodes.new("ShaderNodeMath")
			math_005.name = "Math.005"
			math_005.operation = 'RADIANS'
			math_005.use_clamp = False
			
			#node Rotation to Euler.002
			rotation_to_euler_002 = utils_zyz_to_rotation.nodes.new("FunctionNodeRotationToEuler")
			rotation_to_euler_002.name = "Rotation to Euler.002"
			
			#node Axis Angle to Rotation.002
			axis_angle_to_rotation_002 = utils_zyz_to_rotation.nodes.new("FunctionNodeAxisAngleToRotation")
			axis_angle_to_rotation_002.name = "Axis Angle to Rotation.002"
			#Axis
			axis_angle_to_rotation_002.inputs[0].default_value = (0.0, 0.0, 1.0)
			
			#node Math.006
			math_006 = utils_zyz_to_rotation.nodes.new("ShaderNodeMath")
			math_006.name = "Math.006"
			math_006.operation = 'MULTIPLY'
			math_006.use_clamp = False
			#Value_001
			math_006.inputs[1].default_value = -1.0
			
			#node Rotate Euler.001
			rotate_euler_001 = utils_zyz_to_rotation.nodes.new("FunctionNodeRotateEuler")
			rotate_euler_001.name = "Rotate Euler.001"
			rotate_euler_001.rotation_type = 'EULER'
			rotate_euler_001.space = 'OBJECT'
			
			#node Group Output
			group_output = utils_zyz_to_rotation.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Euler to Rotation
			euler_to_rotation = utils_zyz_to_rotation.nodes.new("FunctionNodeEulerToRotation")
			euler_to_rotation.name = "Euler to Rotation"
			
			#node Math.001
			math_001 = utils_zyz_to_rotation.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.operation = 'RADIANS'
			math_001.use_clamp = False
			
			#node Group Input
			group_input = utils_zyz_to_rotation.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			
			
			
			#Set locations
			math_002.location = (-694.4244995117188, -84.2993392944336)
			rotation_to_euler_001.location = (-10.165328979492188, 35.051002502441406)
			axis_angle_to_rotation_001.location = (-253.7509002685547, -19.897422790527344)
			math_003.location = (-474.16217041015625, -123.19185638427734)
			rotate_euler.location = (164.9982452392578, 342.89154052734375)
			rotation_to_euler.location = (-93.54765319824219, 256.75140380859375)
			axis_angle_to_rotation.location = (-258.35333251953125, 220.27224731445312)
			math_004.location = (-478.16180419921875, 154.58316040039062)
			math_005.location = (-658.0630493164062, -378.8916931152344)
			rotation_to_euler_002.location = (-53.87699890136719, -285.2621765136719)
			axis_angle_to_rotation_002.location = (-218.6826629638672, -321.7413024902344)
			math_006.location = (-438.49114990234375, -387.4303894042969)
			rotate_euler_001.location = (430.89129638671875, 252.57174682617188)
			group_output.location = (1071.1878662109375, 143.63784790039062)
			euler_to_rotation.location = (641.1380615234375, 110.34000396728516)
			math_001.location = (-697.7337036132812, 163.12179565429688)
			group_input.location = (-924.5353393554688, -5.580089569091797)
			
			#Set dimensions
			math_002.width, math_002.height = 140.0, 100.0
			rotation_to_euler_001.width, rotation_to_euler_001.height = 140.0, 100.0
			axis_angle_to_rotation_001.width, axis_angle_to_rotation_001.height = 140.0, 100.0
			math_003.width, math_003.height = 140.0, 100.0
			rotate_euler.width, rotate_euler.height = 140.0, 100.0
			rotation_to_euler.width, rotation_to_euler.height = 140.0, 100.0
			axis_angle_to_rotation.width, axis_angle_to_rotation.height = 140.0, 100.0
			math_004.width, math_004.height = 140.0, 100.0
			math_005.width, math_005.height = 140.0, 100.0
			rotation_to_euler_002.width, rotation_to_euler_002.height = 140.0, 100.0
			axis_angle_to_rotation_002.width, axis_angle_to_rotation_002.height = 140.0, 100.0
			math_006.width, math_006.height = 140.0, 100.0
			rotate_euler_001.width, rotate_euler_001.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			euler_to_rotation.width, euler_to_rotation.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			
			#initialize utils_zyz_to_rotation links
			#math_006.Value -> axis_angle_to_rotation_002.Angle
			utils_zyz_to_rotation.links.new(math_006.outputs[0], axis_angle_to_rotation_002.inputs[1])
			#rotation_to_euler.Euler -> rotate_euler.Rotation
			utils_zyz_to_rotation.links.new(rotation_to_euler.outputs[0], rotate_euler.inputs[0])
			#axis_angle_to_rotation_002.Rotation -> rotation_to_euler_002.Rotation
			utils_zyz_to_rotation.links.new(axis_angle_to_rotation_002.outputs[0], rotation_to_euler_002.inputs[0])
			#rotate_euler.Rotation -> rotate_euler_001.Rotation
			utils_zyz_to_rotation.links.new(rotate_euler.outputs[0], rotate_euler_001.inputs[0])
			#rotation_to_euler_002.Euler -> rotate_euler_001.Rotate By
			utils_zyz_to_rotation.links.new(rotation_to_euler_002.outputs[0], rotate_euler_001.inputs[1])
			#math_005.Value -> math_006.Value
			utils_zyz_to_rotation.links.new(math_005.outputs[0], math_006.inputs[0])
			#axis_angle_to_rotation_001.Rotation -> rotation_to_euler_001.Rotation
			utils_zyz_to_rotation.links.new(axis_angle_to_rotation_001.outputs[0], rotation_to_euler_001.inputs[0])
			#math_003.Value -> axis_angle_to_rotation_001.Angle
			utils_zyz_to_rotation.links.new(math_003.outputs[0], axis_angle_to_rotation_001.inputs[1])
			#math_004.Value -> axis_angle_to_rotation.Angle
			utils_zyz_to_rotation.links.new(math_004.outputs[0], axis_angle_to_rotation.inputs[1])
			#math_001.Value -> math_004.Value
			utils_zyz_to_rotation.links.new(math_001.outputs[0], math_004.inputs[0])
			#rotation_to_euler_001.Euler -> rotate_euler.Rotate By
			utils_zyz_to_rotation.links.new(rotation_to_euler_001.outputs[0], rotate_euler.inputs[1])
			#axis_angle_to_rotation.Rotation -> rotation_to_euler.Rotation
			utils_zyz_to_rotation.links.new(axis_angle_to_rotation.outputs[0], rotation_to_euler.inputs[0])
			#math_002.Value -> math_003.Value
			utils_zyz_to_rotation.links.new(math_002.outputs[0], math_003.inputs[0])
			#rotate_euler_001.Rotation -> euler_to_rotation.Euler
			utils_zyz_to_rotation.links.new(rotate_euler_001.outputs[0], euler_to_rotation.inputs[0])
			#euler_to_rotation.Rotation -> group_output.Rotation
			utils_zyz_to_rotation.links.new(euler_to_rotation.outputs[0], group_output.inputs[0])
			#group_input.Theta -> math_002.Value
			utils_zyz_to_rotation.links.new(group_input.outputs[1], math_002.inputs[0])
			#group_input.Phi -> math_001.Value
			utils_zyz_to_rotation.links.new(group_input.outputs[0], math_001.inputs[0])
			#group_input.Psi -> math_005.Value
			utils_zyz_to_rotation.links.new(group_input.outputs[2], math_005.inputs[0])
			return utils_zyz_to_rotation

		utils_zyz_to_rotation = utils_zyz_to_rotation_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Utils ZYZ to Rotation", type = 'NODES')
		mod.node_group = utils_zyz_to_rotation
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Utils_ZYZ_to_Rotation.bl_idname)
			
def register():
	bpy.utils.register_class(Utils_ZYZ_to_Rotation)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Utils_ZYZ_to_Rotation)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
