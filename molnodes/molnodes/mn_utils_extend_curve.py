bl_info = {
	"name" : "MN_utils_extend_curve",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class MN_utils_extend_curve(bpy.types.Operator):
	bl_idname = "node.mn_utils_extend_curve"
	bl_label = "MN_utils_extend_curve"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize mn_utils_extend_curve node group
		def mn_utils_extend_curve_node_group():
			mn_utils_extend_curve = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "MN_utils_extend_curve")

			mn_utils_extend_curve.color_tag = 'NONE'
			mn_utils_extend_curve.description = ""

			mn_utils_extend_curve.is_modifier = True
			
			#mn_utils_extend_curve interface
			#Socket DNA Curve
			dna_curve_socket = mn_utils_extend_curve.interface.new_socket(name = "DNA Curve", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			dna_curve_socket.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket = mn_utils_extend_curve.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket.attribute_domain = 'POINT'
			
			#Socket Smoothing Iterations
			smoothing_iterations_socket = mn_utils_extend_curve.interface.new_socket(name = "Smoothing Iterations", in_out='INPUT', socket_type = 'NodeSocketInt')
			smoothing_iterations_socket.subtype = 'NONE'
			smoothing_iterations_socket.default_value = 4
			smoothing_iterations_socket.min_value = 1
			smoothing_iterations_socket.max_value = 1000
			smoothing_iterations_socket.attribute_domain = 'POINT'
			
			#Socket Smoothing Distance
			smoothing_distance_socket = mn_utils_extend_curve.interface.new_socket(name = "Smoothing Distance", in_out='INPUT', socket_type = 'NodeSocketFloat')
			smoothing_distance_socket.subtype = 'DISTANCE'
			smoothing_distance_socket.default_value = 1.0
			smoothing_distance_socket.min_value = 0.009999999776482582
			smoothing_distance_socket.max_value = 3.4028234663852886e+38
			smoothing_distance_socket.attribute_domain = 'POINT'
			
			#Socket Extend Distance
			extend_distance_socket = mn_utils_extend_curve.interface.new_socket(name = "Extend Distance", in_out='INPUT', socket_type = 'NodeSocketFloat')
			extend_distance_socket.subtype = 'NONE'
			extend_distance_socket.default_value = 6.5799994468688965
			extend_distance_socket.min_value = -10000.0
			extend_distance_socket.max_value = 10000.0
			extend_distance_socket.attribute_domain = 'POINT'
			
			
			#initialize mn_utils_extend_curve nodes
			#node Endpoint Selection.003
			endpoint_selection_003 = mn_utils_extend_curve.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_003.name = "Endpoint Selection.003"
			#Start Size
			endpoint_selection_003.inputs[0].default_value = 1
			#End Size
			endpoint_selection_003.inputs[1].default_value = 1
			
			#node Group Output
			group_output = mn_utils_extend_curve.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Position.002
			position_002 = mn_utils_extend_curve.nodes.new("GeometryNodeInputPosition")
			position_002.name = "Position.002"
			
			#node Index.001
			index_001 = mn_utils_extend_curve.nodes.new("GeometryNodeInputIndex")
			index_001.name = "Index.001"
			
			#node Math.007
			math_007 = mn_utils_extend_curve.nodes.new("ShaderNodeMath")
			math_007.name = "Math.007"
			math_007.hide = True
			math_007.operation = 'ADD'
			math_007.use_clamp = False
			
			#node Field at Index
			field_at_index = mn_utils_extend_curve.nodes.new("GeometryNodeFieldAtIndex")
			field_at_index.name = "Field at Index"
			field_at_index.data_type = 'FLOAT_VECTOR'
			field_at_index.domain = 'POINT'
			
			#node Vector Math.010
			vector_math_010 = mn_utils_extend_curve.nodes.new("ShaderNodeVectorMath")
			vector_math_010.name = "Vector Math.010"
			vector_math_010.operation = 'SCALE'
			
			#node Set Position.001
			set_position_001 = mn_utils_extend_curve.nodes.new("GeometryNodeSetPosition")
			set_position_001.name = "Set Position.001"
			#Position
			set_position_001.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Switch.001
			switch_001 = mn_utils_extend_curve.nodes.new("GeometryNodeSwitch")
			switch_001.name = "Switch.001"
			switch_001.input_type = 'INT'
			#False
			switch_001.inputs[1].default_value = 1
			#True
			switch_001.inputs[2].default_value = -1
			
			#node Endpoint Selection.006
			endpoint_selection_006 = mn_utils_extend_curve.nodes.new("GeometryNodeCurveEndpointSelection")
			endpoint_selection_006.name = "Endpoint Selection.006"
			#Start Size
			endpoint_selection_006.inputs[0].default_value = 0
			#End Size
			endpoint_selection_006.inputs[1].default_value = 1
			
			#node Group Input
			group_input = mn_utils_extend_curve.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Vector Math.009
			vector_math_009 = mn_utils_extend_curve.nodes.new("ShaderNodeVectorMath")
			vector_math_009.name = "Vector Math.009"
			vector_math_009.operation = 'SUBTRACT'
			
			#node Vector Math.011
			vector_math_011 = mn_utils_extend_curve.nodes.new("ShaderNodeVectorMath")
			vector_math_011.name = "Vector Math.011"
			vector_math_011.operation = 'DISTANCE'
			
			#node Math
			math = mn_utils_extend_curve.nodes.new("ShaderNodeMath")
			math.name = "Math"
			math.operation = 'DIVIDE'
			math.use_clamp = False
			
			#node Geometry Proximity
			geometry_proximity = mn_utils_extend_curve.nodes.new("GeometryNodeProximity")
			geometry_proximity.name = "Geometry Proximity"
			geometry_proximity.target_element = 'POINTS'
			#Group ID
			geometry_proximity.inputs[1].default_value = 0
			#Source Position
			geometry_proximity.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Sample Group ID
			geometry_proximity.inputs[3].default_value = 0
			
			#node Fillet Curve
			fillet_curve = mn_utils_extend_curve.nodes.new("GeometryNodeFilletCurve")
			fillet_curve.name = "Fillet Curve"
			fillet_curve.mode = 'POLY'
			#Radius
			fillet_curve.inputs[2].default_value = 5.0
			#Limit Radius
			fillet_curve.inputs[3].default_value = True
			
			#node Resample Curve
			resample_curve = mn_utils_extend_curve.nodes.new("GeometryNodeResampleCurve")
			resample_curve.name = "Resample Curve"
			resample_curve.mode = 'LENGTH'
			#Selection
			resample_curve.inputs[1].default_value = True
			
			
			
			
			#Set locations
			endpoint_selection_003.location = (-800.0, 380.0000305175781)
			group_output.location = (-420.0, 420.0)
			position_002.location = (-1280.0, 160.0)
			index_001.location = (-1280.0, 100.0)
			math_007.location = (-1280.0, 40.0)
			field_at_index.location = (-1120.0, 160.0)
			vector_math_010.location = (-800.0, 240.0)
			set_position_001.location = (-640.0, 419.9999694824219)
			switch_001.location = (-1280.0, 0.0)
			endpoint_selection_006.location = (-1280.0, -160.0)
			group_input.location = (-1380.0, 400.0)
			vector_math_009.location = (-960.0, 240.0)
			vector_math_011.location = (-960.0, 100.0)
			math.location = (-800.0, 100.0)
			geometry_proximity.location = (-640.0, 260.0)
			fillet_curve.location = (-960.9263305664062, 460.0)
			resample_curve.location = (-1120.92626953125, 460.0)
			
			#Set dimensions
			endpoint_selection_003.width, endpoint_selection_003.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			position_002.width, position_002.height = 140.0, 100.0
			index_001.width, index_001.height = 140.0, 100.0
			math_007.width, math_007.height = 140.0, 100.0
			field_at_index.width, field_at_index.height = 140.0, 100.0
			vector_math_010.width, vector_math_010.height = 140.0, 100.0
			set_position_001.width, set_position_001.height = 140.0, 100.0
			switch_001.width, switch_001.height = 140.0, 100.0
			endpoint_selection_006.width, endpoint_selection_006.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			vector_math_009.width, vector_math_009.height = 140.0, 100.0
			vector_math_011.width, vector_math_011.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			geometry_proximity.width, geometry_proximity.height = 140.0, 100.0
			fillet_curve.width, fillet_curve.height = 140.0, 100.0
			resample_curve.width, resample_curve.height = 140.0, 100.0
			
			#initialize mn_utils_extend_curve links
			#resample_curve.Curve -> fillet_curve.Curve
			mn_utils_extend_curve.links.new(resample_curve.outputs[0], fillet_curve.inputs[0])
			#group_input.Geometry -> resample_curve.Curve
			mn_utils_extend_curve.links.new(group_input.outputs[0], resample_curve.inputs[0])
			#endpoint_selection_003.Selection -> set_position_001.Selection
			mn_utils_extend_curve.links.new(endpoint_selection_003.outputs[0], set_position_001.inputs[1])
			#fillet_curve.Curve -> set_position_001.Geometry
			mn_utils_extend_curve.links.new(fillet_curve.outputs[0], set_position_001.inputs[0])
			#position_002.Position -> vector_math_009.Vector
			mn_utils_extend_curve.links.new(position_002.outputs[0], vector_math_009.inputs[0])
			#position_002.Position -> field_at_index.Value
			mn_utils_extend_curve.links.new(position_002.outputs[0], field_at_index.inputs[1])
			#field_at_index.Value -> vector_math_009.Vector
			mn_utils_extend_curve.links.new(field_at_index.outputs[0], vector_math_009.inputs[1])
			#index_001.Index -> math_007.Value
			mn_utils_extend_curve.links.new(index_001.outputs[0], math_007.inputs[0])
			#math_007.Value -> field_at_index.Index
			mn_utils_extend_curve.links.new(math_007.outputs[0], field_at_index.inputs[0])
			#vector_math_010.Vector -> set_position_001.Offset
			mn_utils_extend_curve.links.new(vector_math_010.outputs[0], set_position_001.inputs[3])
			#endpoint_selection_006.Selection -> switch_001.Switch
			mn_utils_extend_curve.links.new(endpoint_selection_006.outputs[0], switch_001.inputs[0])
			#switch_001.Output -> math_007.Value
			mn_utils_extend_curve.links.new(switch_001.outputs[0], math_007.inputs[1])
			#vector_math_009.Vector -> vector_math_010.Vector
			mn_utils_extend_curve.links.new(vector_math_009.outputs[0], vector_math_010.inputs[0])
			#group_input.Smoothing Iterations -> fillet_curve.Count
			mn_utils_extend_curve.links.new(group_input.outputs[1], fillet_curve.inputs[1])
			#group_input.Smoothing Distance -> resample_curve.Length
			mn_utils_extend_curve.links.new(group_input.outputs[2], resample_curve.inputs[3])
			#set_position_001.Geometry -> group_output.DNA Curve
			mn_utils_extend_curve.links.new(set_position_001.outputs[0], group_output.inputs[0])
			#position_002.Position -> vector_math_011.Vector
			mn_utils_extend_curve.links.new(position_002.outputs[0], vector_math_011.inputs[0])
			#field_at_index.Value -> vector_math_011.Vector
			mn_utils_extend_curve.links.new(field_at_index.outputs[0], vector_math_011.inputs[1])
			#group_input.Extend Distance -> math.Value
			mn_utils_extend_curve.links.new(group_input.outputs[3], math.inputs[0])
			#vector_math_011.Value -> math.Value
			mn_utils_extend_curve.links.new(vector_math_011.outputs[1], math.inputs[1])
			#math.Value -> vector_math_010.Scale
			mn_utils_extend_curve.links.new(math.outputs[0], vector_math_010.inputs[3])
			#fillet_curve.Curve -> geometry_proximity.Geometry
			mn_utils_extend_curve.links.new(fillet_curve.outputs[0], geometry_proximity.inputs[0])
			return mn_utils_extend_curve

		mn_utils_extend_curve = mn_utils_extend_curve_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "MN_utils_extend_curve", type = 'NODES')
		mod.node_group = mn_utils_extend_curve
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(MN_utils_extend_curve.bl_idname)
			
def register():
	bpy.utils.register_class(MN_utils_extend_curve)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(MN_utils_extend_curve)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
