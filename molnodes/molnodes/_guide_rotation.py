bl_info = {
	"name" : ".guide_rotation",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _guide_rotation(bpy.types.Operator):
	bl_idname = "node._guide_rotation"
	bl_label = ".guide_rotation"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _guide_rotation node group
		def _guide_rotation_node_group():
			_guide_rotation = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".guide_rotation")

			_guide_rotation.color_tag = 'NONE'
			_guide_rotation.description = ""

			
			#_guide_rotation interface
			#Socket Rotation
			rotation_socket = _guide_rotation.interface.new_socket(name = "Rotation", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			rotation_socket.default_value = (0.0, 0.0, 0.0)
			rotation_socket.min_value = -3.4028234663852886e+38
			rotation_socket.max_value = 3.4028234663852886e+38
			rotation_socket.subtype = 'EULER'
			rotation_socket.attribute_domain = 'POINT'
			
			#Socket Angle
			angle_socket = _guide_rotation.interface.new_socket(name = "Angle", in_out='INPUT', socket_type = 'NodeSocketFloat')
			angle_socket.default_value = 0.0
			angle_socket.min_value = -3.4028234663852886e+38
			angle_socket.max_value = 3.4028234663852886e+38
			angle_socket.subtype = 'ANGLE'
			angle_socket.attribute_domain = 'POINT'
			
			
			#initialize _guide_rotation nodes
			#node Align Euler to Vector.001
			align_euler_to_vector_001 = _guide_rotation.nodes.new("FunctionNodeAlignEulerToVector")
			align_euler_to_vector_001.name = "Align Euler to Vector.001"
			align_euler_to_vector_001.axis = 'X'
			align_euler_to_vector_001.pivot_axis = 'Z'
			#Factor
			align_euler_to_vector_001.inputs[1].default_value = 1.0
			
			#node Rotate Euler
			rotate_euler = _guide_rotation.nodes.new("FunctionNodeRotateEuler")
			rotate_euler.name = "Rotate Euler"
			rotate_euler.rotation_type = 'AXIS_ANGLE'
			rotate_euler.space = 'OBJECT'
			
			#node Align Euler to Vector
			align_euler_to_vector = _guide_rotation.nodes.new("FunctionNodeAlignEulerToVector")
			align_euler_to_vector.name = "Align Euler to Vector"
			align_euler_to_vector.axis = 'Z'
			align_euler_to_vector.pivot_axis = 'AUTO'
			#Rotation
			align_euler_to_vector.inputs[0].default_value = (0.0, 0.0, 0.0)
			#Factor
			align_euler_to_vector.inputs[1].default_value = 1.0
			
			#node Group Output
			group_output = _guide_rotation.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Reroute
			reroute = _guide_rotation.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Named Attribute.001
			named_attribute_001 = _guide_rotation.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_001.inputs[0].default_value = "guide_X"
			
			#node Named Attribute
			named_attribute = _guide_rotation.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute.inputs[0].default_value = "guide_Z"
			
			#node Group Input.001
			group_input_001 = _guide_rotation.nodes.new("NodeGroupInput")
			group_input_001.name = "Group Input.001"
			
			
			
			
			#Set locations
			align_euler_to_vector_001.location = (177.053955078125, 186.16505432128906)
			rotate_euler.location = (356.9603271484375, 191.41680908203125)
			align_euler_to_vector.location = (20.0, 180.0)
			group_output.location = (540.0, 180.0)
			reroute.location = (140.0, -40.0)
			named_attribute_001.location = (-180.0, 40.0)
			named_attribute.location = (-180.0, 180.0)
			group_input_001.location = (180.0, -40.0)
			
			#Set dimensions
			align_euler_to_vector_001.width, align_euler_to_vector_001.height = 140.0, 100.0
			rotate_euler.width, rotate_euler.height = 140.0, 100.0
			align_euler_to_vector.width, align_euler_to_vector.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			named_attribute_001.width, named_attribute_001.height = 145.799072265625, 100.0
			named_attribute.width, named_attribute.height = 146.58917236328125, 100.0
			group_input_001.width, group_input_001.height = 140.0, 100.0
			
			#initialize _guide_rotation links
			#reroute.Output -> align_euler_to_vector_001.Vector
			_guide_rotation.links.new(reroute.outputs[0], align_euler_to_vector_001.inputs[2])
			#align_euler_to_vector.Rotation -> align_euler_to_vector_001.Rotation
			_guide_rotation.links.new(align_euler_to_vector.outputs[0], align_euler_to_vector_001.inputs[0])
			#rotate_euler.Rotation -> group_output.Rotation
			_guide_rotation.links.new(rotate_euler.outputs[0], group_output.inputs[0])
			#align_euler_to_vector_001.Rotation -> rotate_euler.Rotation
			_guide_rotation.links.new(align_euler_to_vector_001.outputs[0], rotate_euler.inputs[0])
			#group_input_001.Angle -> rotate_euler.Angle
			_guide_rotation.links.new(group_input_001.outputs[0], rotate_euler.inputs[3])
			#named_attribute.Attribute -> align_euler_to_vector.Vector
			_guide_rotation.links.new(named_attribute.outputs[0], align_euler_to_vector.inputs[2])
			#reroute.Output -> rotate_euler.Axis
			_guide_rotation.links.new(reroute.outputs[0], rotate_euler.inputs[2])
			#named_attribute_001.Attribute -> reroute.Input
			_guide_rotation.links.new(named_attribute_001.outputs[0], reroute.inputs[0])
			return _guide_rotation

		_guide_rotation = _guide_rotation_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".guide_rotation", type = 'NODES')
		mod.node_group = _guide_rotation
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_guide_rotation.bl_idname)
			
def register():
	bpy.utils.register_class(_guide_rotation)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_guide_rotation)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
