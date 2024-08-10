bl_info = {
	"name" : ".MN_assembly_rotate",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _MN_assembly_rotate(bpy.types.Operator):
	bl_idname = "node._mn_assembly_rotate"
	bl_label = ".MN_assembly_rotate"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _mn_assembly_rotate node group
		def _mn_assembly_rotate_node_group():
			_mn_assembly_rotate = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_assembly_rotate")

			_mn_assembly_rotate.color_tag = 'NONE'
			_mn_assembly_rotate.description = ""

			_mn_assembly_rotate.is_modifier = True
			
			#_mn_assembly_rotate interface
			#Socket Instances
			instances_socket = _mn_assembly_rotate.interface.new_socket(name = "Instances", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			instances_socket.attribute_domain = 'POINT'
			
			#Socket Instances
			instances_socket_1 = _mn_assembly_rotate.interface.new_socket(name = "Instances", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			instances_socket_1.attribute_domain = 'POINT'
			
			#Socket Selection
			selection_socket = _mn_assembly_rotate.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket.attribute_domain = 'POINT'
			selection_socket.hide_value = True
			selection_socket.description = "Selection of atoms to apply this node to"
			
			#Socket Rotation
			rotation_socket = _mn_assembly_rotate.interface.new_socket(name = "Rotation", in_out='INPUT', socket_type = 'NodeSocketVector')
			rotation_socket.subtype = 'EULER'
			rotation_socket.default_value = (0.0, 0.0, 0.0)
			rotation_socket.min_value = -3.4028234663852886e+38
			rotation_socket.max_value = 3.4028234663852886e+38
			rotation_socket.attribute_domain = 'POINT'
			
			#Socket com_offset
			com_offset_socket = _mn_assembly_rotate.interface.new_socket(name = "com_offset", in_out='INPUT', socket_type = 'NodeSocketVector')
			com_offset_socket.subtype = 'NONE'
			com_offset_socket.default_value = (0.0, 0.0, 0.0)
			com_offset_socket.min_value = -10000.0
			com_offset_socket.max_value = 10000.0
			com_offset_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_assembly_rotate nodes
			#node Accumulate Field
			accumulate_field = _mn_assembly_rotate.nodes.new("GeometryNodeAccumulateField")
			accumulate_field.name = "Accumulate Field"
			accumulate_field.data_type = 'FLOAT_VECTOR'
			accumulate_field.domain = 'POINT'
			accumulate_field.outputs[0].hide = True
			accumulate_field.outputs[1].hide = True
			
			#node Accumulate Field.001
			accumulate_field_001 = _mn_assembly_rotate.nodes.new("GeometryNodeAccumulateField")
			accumulate_field_001.name = "Accumulate Field.001"
			accumulate_field_001.data_type = 'INT'
			accumulate_field_001.domain = 'POINT'
			accumulate_field_001.inputs[0].hide = True
			accumulate_field_001.outputs[0].hide = True
			accumulate_field_001.outputs[1].hide = True
			#Value
			accumulate_field_001.inputs[0].default_value = 1
			
			#node Vector Math
			vector_math = _mn_assembly_rotate.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.hide = True
			vector_math.operation = 'DIVIDE'
			
			#node Position.001
			position_001 = _mn_assembly_rotate.nodes.new("GeometryNodeInputPosition")
			position_001.name = "Position.001"
			
			#node Capture Attribute
			capture_attribute = _mn_assembly_rotate.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute.name = "Capture Attribute"
			capture_attribute.active_index = 0
			capture_attribute.capture_items.clear()
			capture_attribute.capture_items.new('FLOAT', "Value")
			capture_attribute.capture_items["Value"].data_type = 'INT'
			capture_attribute.domain = 'INSTANCE'
			
			#node Reroute.001
			reroute_001 = _mn_assembly_rotate.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			#node Index
			index = _mn_assembly_rotate.nodes.new("GeometryNodeInputIndex")
			index.name = "Index"
			
			#node Realize Instances
			realize_instances = _mn_assembly_rotate.nodes.new("GeometryNodeRealizeInstances")
			realize_instances.name = "Realize Instances"
			#Selection
			realize_instances.inputs[1].default_value = True
			#Realize All
			realize_instances.inputs[2].default_value = True
			#Depth
			realize_instances.inputs[3].default_value = 0
			
			#node Reroute.002
			reroute_002 = _mn_assembly_rotate.nodes.new("NodeReroute")
			reroute_002.name = "Reroute.002"
			#node Reroute
			reroute = _mn_assembly_rotate.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Group Output
			group_output = _mn_assembly_rotate.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Reroute.006
			reroute_006 = _mn_assembly_rotate.nodes.new("NodeReroute")
			reroute_006.name = "Reroute.006"
			#node Reroute.007
			reroute_007 = _mn_assembly_rotate.nodes.new("NodeReroute")
			reroute_007.name = "Reroute.007"
			#node Reroute.008
			reroute_008 = _mn_assembly_rotate.nodes.new("NodeReroute")
			reroute_008.name = "Reroute.008"
			#node Reroute.009
			reroute_009 = _mn_assembly_rotate.nodes.new("NodeReroute")
			reroute_009.name = "Reroute.009"
			#node Reroute.010
			reroute_010 = _mn_assembly_rotate.nodes.new("NodeReroute")
			reroute_010.name = "Reroute.010"
			#node Position.002
			position_002 = _mn_assembly_rotate.nodes.new("GeometryNodeInputPosition")
			position_002.name = "Position.002"
			
			#node Sample Index
			sample_index = _mn_assembly_rotate.nodes.new("GeometryNodeSampleIndex")
			sample_index.name = "Sample Index"
			sample_index.clamp = True
			sample_index.data_type = 'FLOAT_VECTOR'
			sample_index.domain = 'POINT'
			
			#node Index.001
			index_001 = _mn_assembly_rotate.nodes.new("GeometryNodeInputIndex")
			index_001.name = "Index.001"
			
			#node String
			string = _mn_assembly_rotate.nodes.new("FunctionNodeInputString")
			string.name = "String"
			string.string = "centre_of_mass"
			
			#node Group Input
			group_input = _mn_assembly_rotate.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Named Attribute
			named_attribute = _mn_assembly_rotate.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'FLOAT_VECTOR'
			
			#node Vector Math.001
			vector_math_001 = _mn_assembly_rotate.nodes.new("ShaderNodeVectorMath")
			vector_math_001.name = "Vector Math.001"
			vector_math_001.operation = 'SUBTRACT'
			
			#node Reroute.004
			reroute_004 = _mn_assembly_rotate.nodes.new("NodeReroute")
			reroute_004.name = "Reroute.004"
			#node Store Named Attribute.001
			store_named_attribute_001 = _mn_assembly_rotate.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_001.name = "Store Named Attribute.001"
			store_named_attribute_001.data_type = 'FLOAT_VECTOR'
			store_named_attribute_001.domain = 'INSTANCE'
			#Selection
			store_named_attribute_001.inputs[1].default_value = True
			
			#node Set Position
			set_position = _mn_assembly_rotate.nodes.new("GeometryNodeSetPosition")
			set_position.name = "Set Position"
			#Selection
			set_position.inputs[1].default_value = True
			#Offset
			set_position.inputs[3].default_value = (0.0, 0.0, 0.0)
			
			#node Merge by Distance
			merge_by_distance = _mn_assembly_rotate.nodes.new("GeometryNodeMergeByDistance")
			merge_by_distance.name = "Merge by Distance"
			merge_by_distance.mode = 'ALL'
			#Selection
			merge_by_distance.inputs[1].default_value = True
			#Distance
			merge_by_distance.inputs[2].default_value = 0.0010000000474974513
			
			#node Rotate Instances
			rotate_instances = _mn_assembly_rotate.nodes.new("GeometryNodeRotateInstances")
			rotate_instances.name = "Rotate Instances"
			#Local Space
			rotate_instances.inputs[4].default_value = False
			
			#node Bounding Box
			bounding_box = _mn_assembly_rotate.nodes.new("GeometryNodeBoundBox")
			bounding_box.name = "Bounding Box"
			
			#node Reroute.003
			reroute_003 = _mn_assembly_rotate.nodes.new("NodeReroute")
			reroute_003.name = "Reroute.003"
			#node Euler to Rotation
			euler_to_rotation = _mn_assembly_rotate.nodes.new("FunctionNodeEulerToRotation")
			euler_to_rotation.name = "Euler to Rotation"
			
			
			
			
			#Set locations
			accumulate_field.location = (-480.0, 340.0)
			accumulate_field_001.location = (-480.0, 180.0)
			vector_math.location = (-320.0, 240.0)
			position_001.location = (-640.0, 340.0)
			capture_attribute.location = (-700.0, 140.0)
			reroute_001.location = (-500.0, 140.0)
			index.location = (-860.0, 0.0)
			realize_instances.location = (-480.0, 40.0)
			reroute_002.location = (-160.0, -220.0)
			reroute.location = (440.0, -220.0)
			group_output.location = (860.0, -40.0)
			reroute_006.location = (540.0, -140.0)
			reroute_007.location = (440.0, -200.0)
			reroute_008.location = (-360.0, -200.0)
			reroute_009.location = (-540.0, -220.0)
			reroute_010.location = (-540.0, -240.0)
			position_002.location = (40.0, 60.0)
			sample_index.location = (200.0, 220.0)
			index_001.location = (40.0, 0.0)
			string.location = (-60.0, -120.0)
			group_input.location = (-1100.0, -40.0)
			named_attribute.location = (140.0, -240.0)
			vector_math_001.location = (480.0, -220.0)
			reroute_004.location = (320.0, -160.0)
			store_named_attribute_001.location = (400.0, 200.0)
			set_position.location = (-120.0, 220.0)
			merge_by_distance.location = (40.0, 220.0)
			rotate_instances.location = (660.0, -40.0)
			bounding_box.location = (-860.0, 220.0)
			reroute_003.location = (320.0, -100.0)
			euler_to_rotation.location = (620.0, -40.0)
			
			#Set dimensions
			accumulate_field.width, accumulate_field.height = 140.0, 100.0
			accumulate_field_001.width, accumulate_field_001.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			position_001.width, position_001.height = 140.0, 100.0
			capture_attribute.width, capture_attribute.height = 140.0, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			index.width, index.height = 140.0, 100.0
			realize_instances.width, realize_instances.height = 140.0, 100.0
			reroute_002.width, reroute_002.height = 16.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			reroute_006.width, reroute_006.height = 16.0, 100.0
			reroute_007.width, reroute_007.height = 16.0, 100.0
			reroute_008.width, reroute_008.height = 16.0, 100.0
			reroute_009.width, reroute_009.height = 16.0, 100.0
			reroute_010.width, reroute_010.height = 16.0, 100.0
			position_002.width, position_002.height = 140.0, 100.0
			sample_index.width, sample_index.height = 140.0, 100.0
			index_001.width, index_001.height = 140.0, 100.0
			string.width, string.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			vector_math_001.width, vector_math_001.height = 140.0, 100.0
			reroute_004.width, reroute_004.height = 16.0, 100.0
			store_named_attribute_001.width, store_named_attribute_001.height = 140.0, 100.0
			set_position.width, set_position.height = 140.0, 100.0
			merge_by_distance.width, merge_by_distance.height = 140.0, 100.0
			rotate_instances.width, rotate_instances.height = 140.0, 100.0
			bounding_box.width, bounding_box.height = 140.0, 100.0
			reroute_003.width, reroute_003.height = 16.0, 100.0
			euler_to_rotation.width, euler_to_rotation.height = 140.0, 100.0
			
			#initialize _mn_assembly_rotate links
			#rotate_instances.Instances -> group_output.Instances
			_mn_assembly_rotate.links.new(rotate_instances.outputs[0], group_output.inputs[0])
			#bounding_box.Bounding Box -> capture_attribute.Geometry
			_mn_assembly_rotate.links.new(bounding_box.outputs[0], capture_attribute.inputs[0])
			#index.Index -> capture_attribute.Value
			_mn_assembly_rotate.links.new(index.outputs[0], capture_attribute.inputs[1])
			#position_001.Position -> accumulate_field.Value
			_mn_assembly_rotate.links.new(position_001.outputs[0], accumulate_field.inputs[0])
			#reroute_001.Output -> accumulate_field.Group ID
			_mn_assembly_rotate.links.new(reroute_001.outputs[0], accumulate_field.inputs[1])
			#capture_attribute.Geometry -> realize_instances.Geometry
			_mn_assembly_rotate.links.new(capture_attribute.outputs[0], realize_instances.inputs[0])
			#realize_instances.Geometry -> set_position.Geometry
			_mn_assembly_rotate.links.new(realize_instances.outputs[0], set_position.inputs[0])
			#accumulate_field.Total -> vector_math.Vector
			_mn_assembly_rotate.links.new(accumulate_field.outputs[2], vector_math.inputs[0])
			#reroute_001.Output -> accumulate_field_001.Group ID
			_mn_assembly_rotate.links.new(reroute_001.outputs[0], accumulate_field_001.inputs[1])
			#accumulate_field_001.Total -> vector_math.Vector
			_mn_assembly_rotate.links.new(accumulate_field_001.outputs[2], vector_math.inputs[1])
			#capture_attribute.Value -> reroute_001.Input
			_mn_assembly_rotate.links.new(capture_attribute.outputs[1], reroute_001.inputs[0])
			#vector_math.Vector -> set_position.Position
			_mn_assembly_rotate.links.new(vector_math.outputs[0], set_position.inputs[2])
			#set_position.Geometry -> merge_by_distance.Geometry
			_mn_assembly_rotate.links.new(set_position.outputs[0], merge_by_distance.inputs[0])
			#merge_by_distance.Geometry -> sample_index.Geometry
			_mn_assembly_rotate.links.new(merge_by_distance.outputs[0], sample_index.inputs[0])
			#position_002.Position -> sample_index.Value
			_mn_assembly_rotate.links.new(position_002.outputs[0], sample_index.inputs[1])
			#group_input.Instances -> bounding_box.Geometry
			_mn_assembly_rotate.links.new(group_input.outputs[0], bounding_box.inputs[0])
			#store_named_attribute_001.Geometry -> rotate_instances.Instances
			_mn_assembly_rotate.links.new(store_named_attribute_001.outputs[0], rotate_instances.inputs[0])
			#sample_index.Value -> store_named_attribute_001.Value
			_mn_assembly_rotate.links.new(sample_index.outputs[0], store_named_attribute_001.inputs[3])
			#named_attribute.Attribute -> vector_math_001.Vector
			_mn_assembly_rotate.links.new(named_attribute.outputs[0], vector_math_001.inputs[0])
			#reroute_010.Output -> vector_math_001.Vector
			_mn_assembly_rotate.links.new(reroute_010.outputs[0], vector_math_001.inputs[1])
			#string.String -> named_attribute.Name
			_mn_assembly_rotate.links.new(string.outputs[0], named_attribute.inputs[0])
			#reroute_004.Output -> store_named_attribute_001.Name
			_mn_assembly_rotate.links.new(reroute_004.outputs[0], store_named_attribute_001.inputs[2])
			#reroute_009.Output -> reroute_002.Input
			_mn_assembly_rotate.links.new(reroute_009.outputs[0], reroute_002.inputs[0])
			#group_input.Instances -> reroute_003.Input
			_mn_assembly_rotate.links.new(group_input.outputs[0], reroute_003.inputs[0])
			#reroute_002.Output -> reroute.Input
			_mn_assembly_rotate.links.new(reroute_002.outputs[0], reroute.inputs[0])
			#string.String -> reroute_004.Input
			_mn_assembly_rotate.links.new(string.outputs[0], reroute_004.inputs[0])
			#reroute_006.Output -> rotate_instances.Selection
			_mn_assembly_rotate.links.new(reroute_006.outputs[0], rotate_instances.inputs[1])
			#reroute_007.Output -> reroute_006.Input
			_mn_assembly_rotate.links.new(reroute_007.outputs[0], reroute_006.inputs[0])
			#reroute_008.Output -> reroute_007.Input
			_mn_assembly_rotate.links.new(reroute_008.outputs[0], reroute_007.inputs[0])
			#group_input.Selection -> reroute_008.Input
			_mn_assembly_rotate.links.new(group_input.outputs[1], reroute_008.inputs[0])
			#group_input.Rotation -> reroute_009.Input
			_mn_assembly_rotate.links.new(group_input.outputs[2], reroute_009.inputs[0])
			#group_input.com_offset -> reroute_010.Input
			_mn_assembly_rotate.links.new(group_input.outputs[3], reroute_010.inputs[0])
			#index_001.Index -> sample_index.Index
			_mn_assembly_rotate.links.new(index_001.outputs[0], sample_index.inputs[2])
			#vector_math_001.Vector -> rotate_instances.Pivot Point
			_mn_assembly_rotate.links.new(vector_math_001.outputs[0], rotate_instances.inputs[3])
			#reroute.Output -> euler_to_rotation.Euler
			_mn_assembly_rotate.links.new(reroute.outputs[0], euler_to_rotation.inputs[0])
			#reroute_003.Output -> store_named_attribute_001.Geometry
			_mn_assembly_rotate.links.new(reroute_003.outputs[0], store_named_attribute_001.inputs[0])
			#euler_to_rotation.Rotation -> rotate_instances.Rotation
			_mn_assembly_rotate.links.new(euler_to_rotation.outputs[0], rotate_instances.inputs[2])
			return _mn_assembly_rotate

		_mn_assembly_rotate = _mn_assembly_rotate_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".MN_assembly_rotate", type = 'NODES')
		mod.node_group = _mn_assembly_rotate
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_MN_assembly_rotate.bl_idname)
			
def register():
	bpy.utils.register_class(_MN_assembly_rotate)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_MN_assembly_rotate)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
