bl_info = {
	"name" : ".DEBUG_arrows",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _DEBUG_arrows(bpy.types.Operator):
	bl_idname = "node._debug_arrows"
	bl_label = ".DEBUG_arrows"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _debug_arrows node group
		def _debug_arrows_node_group():
			_debug_arrows = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".DEBUG_arrows")

			_debug_arrows.color_tag = 'NONE'
			_debug_arrows.description = ""

			_debug_arrows.is_modifier = True
			
			#_debug_arrows interface
			#Socket Instances
			instances_socket = _debug_arrows.interface.new_socket(name = "Instances", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			instances_socket.attribute_domain = 'POINT'
			
			#Socket Points
			points_socket = _debug_arrows.interface.new_socket(name = "Points", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			points_socket.attribute_domain = 'POINT'
			
			#Socket Position
			position_socket = _debug_arrows.interface.new_socket(name = "Position", in_out='INPUT', socket_type = 'NodeSocketVector')
			position_socket.default_value = (0.0, 0.0, 0.0)
			position_socket.min_value = -3.4028234663852886e+38
			position_socket.max_value = 3.4028234663852886e+38
			position_socket.subtype = 'NONE'
			position_socket.attribute_domain = 'POINT'
			position_socket.hide_value = True
			
			#Socket Offset
			offset_socket = _debug_arrows.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketVector')
			offset_socket.default_value = (0.0, 0.0, 0.0)
			offset_socket.min_value = -3.4028234663852886e+38
			offset_socket.max_value = 3.4028234663852886e+38
			offset_socket.subtype = 'TRANSLATION'
			offset_socket.attribute_domain = 'POINT'
			
			#Socket Rotation
			rotation_socket = _debug_arrows.interface.new_socket(name = "Rotation", in_out='INPUT', socket_type = 'NodeSocketVector')
			rotation_socket.default_value = (0.0, 0.0, 0.0)
			rotation_socket.min_value = -3.4028234663852886e+38
			rotation_socket.max_value = 3.4028234663852886e+38
			rotation_socket.subtype = 'EULER'
			rotation_socket.attribute_domain = 'POINT'
			
			#Socket Scale
			scale_socket = _debug_arrows.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketVector')
			scale_socket.default_value = (0.33000001311302185, 0.36000001430511475, 0.75)
			scale_socket.min_value = -3.4028234663852886e+38
			scale_socket.max_value = 3.4028234663852886e+38
			scale_socket.subtype = 'XYZ'
			scale_socket.attribute_domain = 'POINT'
			
			
			#initialize _debug_arrows nodes
			#node Group Output
			group_output = _debug_arrows.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Instance on Points.002
			instance_on_points_002 = _debug_arrows.nodes.new("GeometryNodeInstanceOnPoints")
			instance_on_points_002.name = "Instance on Points.002"
			#Selection
			instance_on_points_002.inputs[1].default_value = True
			#Pick Instance
			instance_on_points_002.inputs[3].default_value = False
			#Instance Index
			instance_on_points_002.inputs[4].default_value = 0
			
			#node Reroute.003
			reroute_003 = _debug_arrows.nodes.new("NodeReroute")
			reroute_003.name = "Reroute.003"
			#node Reroute.009
			reroute_009 = _debug_arrows.nodes.new("NodeReroute")
			reroute_009.name = "Reroute.009"
			#node Join Geometry.001
			join_geometry_001 = _debug_arrows.nodes.new("GeometryNodeJoinGeometry")
			join_geometry_001.name = "Join Geometry.001"
			join_geometry_001.hide = True
			
			#node Transform Geometry.002
			transform_geometry_002 = _debug_arrows.nodes.new("GeometryNodeTransform")
			transform_geometry_002.name = "Transform Geometry.002"
			transform_geometry_002.mode = 'COMPONENTS'
			#Rotation
			transform_geometry_002.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Scale
			transform_geometry_002.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Transform Geometry.001
			transform_geometry_001 = _debug_arrows.nodes.new("GeometryNodeTransform")
			transform_geometry_001.name = "Transform Geometry.001"
			transform_geometry_001.mode = 'COMPONENTS'
			#Translation
			transform_geometry_001.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Rotation
			transform_geometry_001.inputs[2].default_value = (0.0, 1.5707963705062866, 0.0)
			#Scale
			transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Transform Geometry.003
			transform_geometry_003 = _debug_arrows.nodes.new("GeometryNodeTransform")
			transform_geometry_003.name = "Transform Geometry.003"
			transform_geometry_003.mode = 'COMPONENTS'
			#Translation
			transform_geometry_003.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Rotation
			transform_geometry_003.inputs[2].default_value = (1.5707963705062866, 0.0, 0.0)
			#Scale
			transform_geometry_003.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Vector Math.008
			vector_math_008 = _debug_arrows.nodes.new("ShaderNodeVectorMath")
			vector_math_008.name = "Vector Math.008"
			vector_math_008.operation = 'SCALE'
			#Vector
			vector_math_008.inputs[0].default_value = (0.0, 0.0, 10.300000190734863)
			#Scale
			vector_math_008.inputs[3].default_value = 0.0010000000474974513
			
			#node Cone
			cone = _debug_arrows.nodes.new("GeometryNodeMeshCone")
			cone.name = "Cone"
			cone.fill_type = 'NGON'
			#Vertices
			cone.inputs[0].default_value = 6
			#Side Segments
			cone.inputs[1].default_value = 1
			#Fill Segments
			cone.inputs[2].default_value = 1
			#Radius Top
			cone.inputs[3].default_value = 0.0
			#Radius Bottom
			cone.inputs[4].default_value = 0.010000022128224373
			
			#node Math.003
			math_003 = _debug_arrows.nodes.new("ShaderNodeMath")
			math_003.name = "Math.003"
			math_003.operation = 'DIVIDE'
			math_003.use_clamp = False
			#Value
			math_003.inputs[0].default_value = 49.05999755859375
			#Value_001
			math_003.inputs[1].default_value = 1000.0
			
			#node Store Named Attribute.004
			store_named_attribute_004 = _debug_arrows.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_004.name = "Store Named Attribute.004"
			store_named_attribute_004.data_type = 'FLOAT_COLOR'
			store_named_attribute_004.domain = 'POINT'
			#Selection
			store_named_attribute_004.inputs[1].default_value = True
			#Name
			store_named_attribute_004.inputs[2].default_value = "Color"
			#Value
			store_named_attribute_004.inputs[3].default_value = (0.4605487287044525, 0.05103481188416481, 0.07814221829175949, 0.0)
			
			#node Store Named Attribute
			store_named_attribute = _debug_arrows.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute.name = "Store Named Attribute"
			store_named_attribute.data_type = 'FLOAT_COLOR'
			store_named_attribute.domain = 'POINT'
			#Selection
			store_named_attribute.inputs[1].default_value = True
			#Name
			store_named_attribute.inputs[2].default_value = "Color"
			#Value
			store_named_attribute.inputs[3].default_value = (0.059955447912216187, 0.21724288165569305, 0.4605487287044525, 0.0)
			
			#node Store Named Attribute.005
			store_named_attribute_005 = _debug_arrows.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_005.name = "Store Named Attribute.005"
			store_named_attribute_005.data_type = 'FLOAT_COLOR'
			store_named_attribute_005.domain = 'POINT'
			#Selection
			store_named_attribute_005.inputs[1].default_value = True
			#Name
			store_named_attribute_005.inputs[2].default_value = "Color"
			#Value
			store_named_attribute_005.inputs[3].default_value = (0.21280108392238617, 0.4605487287044525, 0.12887145578861237, 0.0)
			
			#node Set Position
			set_position = _debug_arrows.nodes.new("GeometryNodeSetPosition")
			set_position.name = "Set Position"
			#Selection
			set_position.inputs[1].default_value = True
			
			#node Attribute Statistic
			attribute_statistic = _debug_arrows.nodes.new("GeometryNodeAttributeStatistic")
			attribute_statistic.name = "Attribute Statistic"
			attribute_statistic.data_type = 'FLOAT_VECTOR'
			attribute_statistic.domain = 'POINT'
			#Selection
			attribute_statistic.inputs[1].default_value = True
			
			#node Compare
			compare = _debug_arrows.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'VECTOR'
			compare.mode = 'ELEMENT'
			compare.operation = 'NOT_EQUAL'
			#B_VEC3
			compare.inputs[5].default_value = (0.0, 0.0, 0.0)
			#Epsilon
			compare.inputs[12].default_value = 9.999999747378752e-05
			
			#node Position
			position = _debug_arrows.nodes.new("GeometryNodeInputPosition")
			position.name = "Position"
			
			#node Switch
			switch = _debug_arrows.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'VECTOR'
			
			#node Group Input
			group_input = _debug_arrows.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Reroute
			reroute = _debug_arrows.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			
			
			
			#Set locations
			group_output.location = (1428.90478515625, 0.0)
			instance_on_points_002.location = (988.90478515625, 429.669189453125)
			reroute_003.location = (-276.560546875, 27.071929931640625)
			reroute_009.location = (-209.260498046875, 36.829681396484375)
			join_geometry_001.location = (208.553955078125, 85.46240234375)
			transform_geometry_002.location = (-504.560546875, -72.58740234375)
			transform_geometry_001.location = (-218.82080078125, 19.31646728515625)
			transform_geometry_003.location = (-224.560546875, -334.53759765625)
			vector_math_008.location = (-505.0859375, -418.4356689453125)
			cone.location = (-724.560546875, -214.53759765625)
			math_003.location = (-900.904541015625, -429.669189453125)
			store_named_attribute_004.location = (-20.0, -100.0)
			store_named_attribute.location = (-20.0, 120.0)
			store_named_attribute_005.location = (-20.0, -320.0)
			set_position.location = (578.2709350585938, 400.1163024902344)
			attribute_statistic.location = (-35.687705993652344, 679.48095703125)
			compare.location = (128.0, 680.0)
			position.location = (40.0, 420.0)
			switch.location = (308.0, 460.0)
			group_input.location = (-640.0, 320.0)
			reroute.location = (-192.0, 380.0)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			instance_on_points_002.width, instance_on_points_002.height = 140.0, 100.0
			reroute_003.width, reroute_003.height = 16.0, 100.0
			reroute_009.width, reroute_009.height = 16.0, 100.0
			join_geometry_001.width, join_geometry_001.height = 140.0, 100.0
			transform_geometry_002.width, transform_geometry_002.height = 140.0, 100.0
			transform_geometry_001.width, transform_geometry_001.height = 140.0, 100.0
			transform_geometry_003.width, transform_geometry_003.height = 140.0, 100.0
			vector_math_008.width, vector_math_008.height = 140.0, 100.0
			cone.width, cone.height = 140.0, 100.0
			math_003.width, math_003.height = 140.0, 100.0
			store_named_attribute_004.width, store_named_attribute_004.height = 140.0, 100.0
			store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
			store_named_attribute_005.width, store_named_attribute_005.height = 140.0, 100.0
			set_position.width, set_position.height = 140.0, 100.0
			attribute_statistic.width, attribute_statistic.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			position.width, position.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			
			#initialize _debug_arrows links
			#reroute_009.Output -> store_named_attribute.Geometry
			_debug_arrows.links.new(reroute_009.outputs[0], store_named_attribute.inputs[0])
			#math_003.Value -> cone.Depth
			_debug_arrows.links.new(math_003.outputs[0], cone.inputs[5])
			#transform_geometry_003.Geometry -> store_named_attribute_005.Geometry
			_debug_arrows.links.new(transform_geometry_003.outputs[0], store_named_attribute_005.inputs[0])
			#transform_geometry_001.Geometry -> store_named_attribute_004.Geometry
			_debug_arrows.links.new(transform_geometry_001.outputs[0], store_named_attribute_004.inputs[0])
			#vector_math_008.Vector -> transform_geometry_002.Translation
			_debug_arrows.links.new(vector_math_008.outputs[0], transform_geometry_002.inputs[1])
			#reroute_003.Output -> transform_geometry_003.Geometry
			_debug_arrows.links.new(reroute_003.outputs[0], transform_geometry_003.inputs[0])
			#cone.Mesh -> transform_geometry_002.Geometry
			_debug_arrows.links.new(cone.outputs[0], transform_geometry_002.inputs[0])
			#reroute_003.Output -> reroute_009.Input
			_debug_arrows.links.new(reroute_003.outputs[0], reroute_009.inputs[0])
			#store_named_attribute_004.Geometry -> join_geometry_001.Geometry
			_debug_arrows.links.new(store_named_attribute_004.outputs[0], join_geometry_001.inputs[0])
			#transform_geometry_002.Geometry -> reroute_003.Input
			_debug_arrows.links.new(transform_geometry_002.outputs[0], reroute_003.inputs[0])
			#reroute_003.Output -> transform_geometry_001.Geometry
			_debug_arrows.links.new(reroute_003.outputs[0], transform_geometry_001.inputs[0])
			#join_geometry_001.Geometry -> instance_on_points_002.Instance
			_debug_arrows.links.new(join_geometry_001.outputs[0], instance_on_points_002.inputs[2])
			#set_position.Geometry -> instance_on_points_002.Points
			_debug_arrows.links.new(set_position.outputs[0], instance_on_points_002.inputs[0])
			#group_input.Scale -> instance_on_points_002.Scale
			_debug_arrows.links.new(group_input.outputs[4], instance_on_points_002.inputs[6])
			#group_input.Rotation -> instance_on_points_002.Rotation
			_debug_arrows.links.new(group_input.outputs[3], instance_on_points_002.inputs[5])
			#instance_on_points_002.Instances -> group_output.Instances
			_debug_arrows.links.new(instance_on_points_002.outputs[0], group_output.inputs[0])
			#reroute.Output -> set_position.Geometry
			_debug_arrows.links.new(reroute.outputs[0], set_position.inputs[0])
			#group_input.Position -> attribute_statistic.Attribute
			_debug_arrows.links.new(group_input.outputs[1], attribute_statistic.inputs[2])
			#reroute.Output -> attribute_statistic.Geometry
			_debug_arrows.links.new(reroute.outputs[0], attribute_statistic.inputs[0])
			#attribute_statistic.Standard Deviation -> compare.A
			_debug_arrows.links.new(attribute_statistic.outputs[6], compare.inputs[4])
			#compare.Result -> switch.Switch
			_debug_arrows.links.new(compare.outputs[0], switch.inputs[0])
			#group_input.Position -> switch.True
			_debug_arrows.links.new(group_input.outputs[1], switch.inputs[2])
			#switch.Output -> set_position.Position
			_debug_arrows.links.new(switch.outputs[0], set_position.inputs[2])
			#position.Position -> switch.False
			_debug_arrows.links.new(position.outputs[0], switch.inputs[1])
			#group_input.Offset -> set_position.Offset
			_debug_arrows.links.new(group_input.outputs[2], set_position.inputs[3])
			#group_input.Points -> reroute.Input
			_debug_arrows.links.new(group_input.outputs[0], reroute.inputs[0])
			#store_named_attribute.Geometry -> join_geometry_001.Geometry
			_debug_arrows.links.new(store_named_attribute.outputs[0], join_geometry_001.inputs[0])
			#store_named_attribute_005.Geometry -> join_geometry_001.Geometry
			_debug_arrows.links.new(store_named_attribute_005.outputs[0], join_geometry_001.inputs[0])
			return _debug_arrows

		_debug_arrows = _debug_arrows_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".DEBUG_arrows", type = 'NODES')
		mod.node_group = _debug_arrows
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_DEBUG_arrows.bl_idname)
			
def register():
	bpy.utils.register_class(_DEBUG_arrows)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_DEBUG_arrows)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
