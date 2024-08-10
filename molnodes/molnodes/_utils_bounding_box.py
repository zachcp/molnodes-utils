bl_info = {
	"name" : ".utils_bounding_box",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _utils_bounding_box(bpy.types.Operator):
	bl_idname = "node._utils_bounding_box"
	bl_label = ".utils_bounding_box"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _utils_bounding_box node group
		def _utils_bounding_box_node_group():
			_utils_bounding_box = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".utils_bounding_box")

			_utils_bounding_box.color_tag = 'NONE'
			_utils_bounding_box.description = ""

			
			#_utils_bounding_box interface
			#Socket Min
			min_socket = _utils_bounding_box.interface.new_socket(name = "Min", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			min_socket.subtype = 'NONE'
			min_socket.default_value = (0.0, 0.0, 0.0)
			min_socket.min_value = -3.4028234663852886e+38
			min_socket.max_value = 3.4028234663852886e+38
			min_socket.attribute_domain = 'POINT'
			
			#Socket Max
			max_socket = _utils_bounding_box.interface.new_socket(name = "Max", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			max_socket.subtype = 'NONE'
			max_socket.default_value = (0.0, 0.0, 0.0)
			max_socket.min_value = -3.4028234663852886e+38
			max_socket.max_value = 3.4028234663852886e+38
			max_socket.attribute_domain = 'POINT'
			
			#Socket X
			x_socket = _utils_bounding_box.interface.new_socket(name = "X", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			x_socket.subtype = 'NONE'
			x_socket.default_value = 0
			x_socket.min_value = -2147483648
			x_socket.max_value = 2147483647
			x_socket.attribute_domain = 'POINT'
			
			#Socket Y
			y_socket = _utils_bounding_box.interface.new_socket(name = "Y", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			y_socket.subtype = 'NONE'
			y_socket.default_value = 0
			y_socket.min_value = -2147483648
			y_socket.max_value = 2147483647
			y_socket.attribute_domain = 'POINT'
			
			#Socket Z
			z_socket = _utils_bounding_box.interface.new_socket(name = "Z", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			z_socket.subtype = 'NONE'
			z_socket.default_value = 0
			z_socket.min_value = -2147483648
			z_socket.max_value = 2147483647
			z_socket.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket = _utils_bounding_box.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket.attribute_domain = 'POINT'
			
			#Socket Subdivisions
			subdivisions_socket = _utils_bounding_box.interface.new_socket(name = "Subdivisions", in_out='INPUT', socket_type = 'NodeSocketFloat')
			subdivisions_socket.subtype = 'NONE'
			subdivisions_socket.default_value = 16.700000762939453
			subdivisions_socket.min_value = -10000.0
			subdivisions_socket.max_value = 10000.0
			subdivisions_socket.attribute_domain = 'POINT'
			
			
			#initialize _utils_bounding_box nodes
			#node Vector Math.002
			vector_math_002 = _utils_bounding_box.nodes.new("ShaderNodeVectorMath")
			vector_math_002.name = "Vector Math.002"
			vector_math_002.operation = 'SUBTRACT'
			
			#node Vector Math.003
			vector_math_003 = _utils_bounding_box.nodes.new("ShaderNodeVectorMath")
			vector_math_003.name = "Vector Math.003"
			vector_math_003.operation = 'SCALE'
			
			#node Reroute
			reroute = _utils_bounding_box.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Reroute.002
			reroute_002 = _utils_bounding_box.nodes.new("NodeReroute")
			reroute_002.name = "Reroute.002"
			#node Group Output
			group_output = _utils_bounding_box.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Separate XYZ
			separate_xyz = _utils_bounding_box.nodes.new("ShaderNodeSeparateXYZ")
			separate_xyz.name = "Separate XYZ"
			
			#node Math
			math = _utils_bounding_box.nodes.new("ShaderNodeMath")
			math.name = "Math"
			math.hide = True
			math.operation = 'MAXIMUM'
			math.use_clamp = False
			#Value_001
			math.inputs[1].default_value = 2.0
			
			#node Math.001
			math_001 = _utils_bounding_box.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.hide = True
			math_001.operation = 'MAXIMUM'
			math_001.use_clamp = False
			#Value_001
			math_001.inputs[1].default_value = 2.0
			
			#node Math.002
			math_002 = _utils_bounding_box.nodes.new("ShaderNodeMath")
			math_002.name = "Math.002"
			math_002.hide = True
			math_002.operation = 'MAXIMUM'
			math_002.use_clamp = False
			#Value_001
			math_002.inputs[1].default_value = 2.0
			
			#node Group Input
			group_input = _utils_bounding_box.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Bounding Box
			bounding_box = _utils_bounding_box.nodes.new("GeometryNodeBoundBox")
			bounding_box.name = "Bounding Box"
			
			#node Value
			value = _utils_bounding_box.nodes.new("ShaderNodeValue")
			value.name = "Value"
			
			value.outputs[0].default_value = 0.009999999776482582
			#node Reroute.001
			reroute_001 = _utils_bounding_box.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			#node Vector Math
			vector_math = _utils_bounding_box.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.operation = 'SUBTRACT'
			
			#node Vector Math.001
			vector_math_001 = _utils_bounding_box.nodes.new("ShaderNodeVectorMath")
			vector_math_001.name = "Vector Math.001"
			vector_math_001.operation = 'ADD'
			
			#node Vector Math.004
			vector_math_004 = _utils_bounding_box.nodes.new("ShaderNodeVectorMath")
			vector_math_004.name = "Vector Math.004"
			vector_math_004.operation = 'SNAP'
			
			#node Vector Math.005
			vector_math_005 = _utils_bounding_box.nodes.new("ShaderNodeVectorMath")
			vector_math_005.name = "Vector Math.005"
			vector_math_005.operation = 'SNAP'
			
			#node Math.003
			math_003 = _utils_bounding_box.nodes.new("ShaderNodeMath")
			math_003.name = "Math.003"
			math_003.operation = 'MULTIPLY'
			math_003.use_clamp = False
			#Value_001
			math_003.inputs[1].default_value = 2.0
			
			
			
			
			#Set locations
			vector_math_002.location = (-36.8055419921875, 112.27713012695312)
			vector_math_003.location = (123.1944580078125, 112.27713012695312)
			reroute.location = (40.0, 160.0)
			reroute_002.location = (60.0, 140.0)
			group_output.location = (700.0, 200.0)
			separate_xyz.location = (283.1944580078125, 112.27713012695312)
			math.location = (480.0, 120.0)
			math_001.location = (480.0, 80.0)
			math_002.location = (480.0, 40.0)
			group_input.location = (-1065.6466064453125, 104.66636657714844)
			bounding_box.location = (-885.6466064453125, 44.6663703918457)
			value.location = (-1025.04443359375, -182.63922119140625)
			reroute_001.location = (-439.06280517578125, -225.71304321289062)
			vector_math.location = (-313.41741943359375, 140.0)
			vector_math_001.location = (-313.41741943359375, 0.0)
			vector_math_004.location = (-564.7015380859375, 104.61347961425781)
			vector_math_005.location = (-563.52734375, -39.964500427246094)
			math_003.location = (-640.0, -200.0)
			
			#Set dimensions
			vector_math_002.width, vector_math_002.height = 140.0, 100.0
			vector_math_003.width, vector_math_003.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			reroute_002.width, reroute_002.height = 16.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			separate_xyz.width, separate_xyz.height = 116.41741943359375, 100.0
			math.width, math.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			math_002.width, math_002.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			bounding_box.width, bounding_box.height = 140.0, 100.0
			value.width, value.height = 140.0, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			vector_math_001.width, vector_math_001.height = 140.0, 100.0
			vector_math_004.width, vector_math_004.height = 140.0, 100.0
			vector_math_005.width, vector_math_005.height = 140.0, 100.0
			math_003.width, math_003.height = 140.0, 100.0
			
			#initialize _utils_bounding_box links
			#vector_math_002.Vector -> vector_math_003.Vector
			_utils_bounding_box.links.new(vector_math_002.outputs[0], vector_math_003.inputs[0])
			#vector_math_001.Vector -> vector_math_002.Vector
			_utils_bounding_box.links.new(vector_math_001.outputs[0], vector_math_002.inputs[0])
			#vector_math_003.Vector -> separate_xyz.Vector
			_utils_bounding_box.links.new(vector_math_003.outputs[0], separate_xyz.inputs[0])
			#reroute_001.Output -> vector_math.Vector
			_utils_bounding_box.links.new(reroute_001.outputs[0], vector_math.inputs[1])
			#vector_math.Vector -> vector_math_002.Vector
			_utils_bounding_box.links.new(vector_math.outputs[0], vector_math_002.inputs[1])
			#reroute_001.Output -> vector_math_001.Vector
			_utils_bounding_box.links.new(reroute_001.outputs[0], vector_math_001.inputs[1])
			#group_input.Subdivisions -> vector_math_003.Scale
			_utils_bounding_box.links.new(group_input.outputs[1], vector_math_003.inputs[3])
			#group_input.Geometry -> bounding_box.Geometry
			_utils_bounding_box.links.new(group_input.outputs[0], bounding_box.inputs[0])
			#reroute.Output -> group_output.Min
			_utils_bounding_box.links.new(reroute.outputs[0], group_output.inputs[0])
			#reroute_002.Output -> group_output.Max
			_utils_bounding_box.links.new(reroute_002.outputs[0], group_output.inputs[1])
			#math_001.Value -> group_output.Y
			_utils_bounding_box.links.new(math_001.outputs[0], group_output.inputs[3])
			#math_002.Value -> group_output.Z
			_utils_bounding_box.links.new(math_002.outputs[0], group_output.inputs[4])
			#vector_math.Vector -> reroute.Input
			_utils_bounding_box.links.new(vector_math.outputs[0], reroute.inputs[0])
			#vector_math_001.Vector -> reroute_002.Input
			_utils_bounding_box.links.new(vector_math_001.outputs[0], reroute_002.inputs[0])
			#separate_xyz.X -> math.Value
			_utils_bounding_box.links.new(separate_xyz.outputs[0], math.inputs[0])
			#math.Value -> group_output.X
			_utils_bounding_box.links.new(math.outputs[0], group_output.inputs[2])
			#separate_xyz.Y -> math_001.Value
			_utils_bounding_box.links.new(separate_xyz.outputs[1], math_001.inputs[0])
			#separate_xyz.Z -> math_002.Value
			_utils_bounding_box.links.new(separate_xyz.outputs[2], math_002.inputs[0])
			#value.Value -> vector_math_004.Vector
			_utils_bounding_box.links.new(value.outputs[0], vector_math_004.inputs[1])
			#bounding_box.Min -> vector_math_004.Vector
			_utils_bounding_box.links.new(bounding_box.outputs[1], vector_math_004.inputs[0])
			#vector_math_004.Vector -> vector_math.Vector
			_utils_bounding_box.links.new(vector_math_004.outputs[0], vector_math.inputs[0])
			#vector_math_005.Vector -> vector_math_001.Vector
			_utils_bounding_box.links.new(vector_math_005.outputs[0], vector_math_001.inputs[0])
			#bounding_box.Max -> vector_math_005.Vector
			_utils_bounding_box.links.new(bounding_box.outputs[2], vector_math_005.inputs[0])
			#value.Value -> math_003.Value
			_utils_bounding_box.links.new(value.outputs[0], math_003.inputs[0])
			#value.Value -> vector_math_005.Vector
			_utils_bounding_box.links.new(value.outputs[0], vector_math_005.inputs[1])
			#math_003.Value -> reroute_001.Input
			_utils_bounding_box.links.new(math_003.outputs[0], reroute_001.inputs[0])
			return _utils_bounding_box

		_utils_bounding_box = _utils_bounding_box_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".utils_bounding_box", type = 'NODES')
		mod.node_group = _utils_bounding_box
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_utils_bounding_box.bl_idname)
			
def register():
	bpy.utils.register_class(_utils_bounding_box)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_utils_bounding_box)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
