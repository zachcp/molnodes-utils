bl_info = {
	"name" : ".surface_compute_density_from_points",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _surface_compute_density_from_points(bpy.types.Operator):
	bl_idname = "node._surface_compute_density_from_points"
	bl_label = ".surface_compute_density_from_points"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _surface_compute_density_from_points node group
		def _surface_compute_density_from_points_node_group():
			_surface_compute_density_from_points = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".surface_compute_density_from_points")

			_surface_compute_density_from_points.color_tag = 'NONE'
			_surface_compute_density_from_points.description = ""

			
			#_surface_compute_density_from_points interface
			#Socket Result
			result_socket = _surface_compute_density_from_points.interface.new_socket(name = "Result", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			result_socket.default_value = False
			result_socket.attribute_domain = 'POINT'
			
			#Socket Atoms
			atoms_socket = _surface_compute_density_from_points.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket.attribute_domain = 'POINT'
			atoms_socket.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Scale Radius
			scale_radius_socket = _surface_compute_density_from_points.interface.new_socket(name = "Scale Radius", in_out='INPUT', socket_type = 'NodeSocketFloat')
			scale_radius_socket.default_value = 1.0
			scale_radius_socket.min_value = -10000.0
			scale_radius_socket.max_value = 10000.0
			scale_radius_socket.subtype = 'NONE'
			scale_radius_socket.attribute_domain = 'POINT'
			
			#Socket Probe Size
			probe_size_socket = _surface_compute_density_from_points.interface.new_socket(name = "Probe Size", in_out='INPUT', socket_type = 'NodeSocketFloat')
			probe_size_socket.default_value = 0.0
			probe_size_socket.min_value = 0.0
			probe_size_socket.max_value = 10000.0
			probe_size_socket.subtype = 'NONE'
			probe_size_socket.attribute_domain = 'POINT'
			
			
			#initialize _surface_compute_density_from_points nodes
			#node Sample Index.002
			sample_index_002 = _surface_compute_density_from_points.nodes.new("GeometryNodeSampleIndex")
			sample_index_002.name = "Sample Index.002"
			sample_index_002.clamp = False
			sample_index_002.data_type = 'FLOAT_VECTOR'
			sample_index_002.domain = 'POINT'
			
			#node Position.001
			position_001 = _surface_compute_density_from_points.nodes.new("GeometryNodeInputPosition")
			position_001.name = "Position.001"
			
			#node Reroute
			reroute = _surface_compute_density_from_points.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Group Output
			group_output = _surface_compute_density_from_points.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Compare.001
			compare_001 = _surface_compute_density_from_points.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'FLOAT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'GREATER_THAN'
			#B
			compare_001.inputs[1].default_value = 0.0
			
			#node Vector Math.004
			vector_math_004 = _surface_compute_density_from_points.nodes.new("ShaderNodeVectorMath")
			vector_math_004.name = "Vector Math.004"
			vector_math_004.operation = 'DISTANCE'
			
			#node Math.008
			math_008 = _surface_compute_density_from_points.nodes.new("ShaderNodeMath")
			math_008.name = "Math.008"
			math_008.operation = 'SUBTRACT'
			math_008.use_clamp = False
			
			#node Math.009
			math_009 = _surface_compute_density_from_points.nodes.new("ShaderNodeMath")
			math_009.name = "Math.009"
			math_009.operation = 'ADD'
			math_009.use_clamp = False
			
			#node Math.001
			math_001 = _surface_compute_density_from_points.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.operation = 'DIVIDE'
			math_001.use_clamp = False
			#Value_001
			math_001.inputs[1].default_value = 100.0
			
			#node Sample Index
			sample_index = _surface_compute_density_from_points.nodes.new("GeometryNodeSampleIndex")
			sample_index.name = "Sample Index"
			sample_index.clamp = False
			sample_index.data_type = 'FLOAT'
			sample_index.domain = 'POINT'
			
			#node Reroute.007
			reroute_007 = _surface_compute_density_from_points.nodes.new("NodeReroute")
			reroute_007.name = "Reroute.007"
			#node Math.003
			math_003 = _surface_compute_density_from_points.nodes.new("ShaderNodeMath")
			math_003.name = "Math.003"
			math_003.operation = 'MULTIPLY'
			math_003.use_clamp = False
			
			#node Sample Index.001
			sample_index_001 = _surface_compute_density_from_points.nodes.new("GeometryNodeSampleIndex")
			sample_index_001.name = "Sample Index.001"
			sample_index_001.clamp = False
			sample_index_001.data_type = 'FLOAT'
			sample_index_001.domain = 'POINT'
			
			#node Named Attribute
			named_attribute = _surface_compute_density_from_points.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'FLOAT'
			#Name
			named_attribute.inputs[0].default_value = "vdw_radii"
			
			#node Reroute.002
			reroute_002 = _surface_compute_density_from_points.nodes.new("NodeReroute")
			reroute_002.name = "Reroute.002"
			#node Sample Index.003
			sample_index_003 = _surface_compute_density_from_points.nodes.new("GeometryNodeSampleIndex")
			sample_index_003.name = "Sample Index.003"
			sample_index_003.clamp = False
			sample_index_003.data_type = 'FLOAT'
			sample_index_003.domain = 'POINT'
			
			#node Reroute.003
			reroute_003 = _surface_compute_density_from_points.nodes.new("NodeReroute")
			reroute_003.name = "Reroute.003"
			#node Reroute.001
			reroute_001 = _surface_compute_density_from_points.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			#node Group Input
			group_input = _surface_compute_density_from_points.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Sample Nearest
			sample_nearest = _surface_compute_density_from_points.nodes.new("GeometryNodeSampleNearest")
			sample_nearest.name = "Sample Nearest"
			sample_nearest.domain = 'POINT'
			#Sample Position
			sample_nearest.inputs[1].default_value = (0.0, 0.0, 0.0)
			
			
			
			
			#Set locations
			sample_index_002.location = (-300.0, -60.0)
			position_001.location = (-460.0, -240.0)
			reroute.location = (-140.0, -280.0)
			group_output.location = (562.0, 220.0)
			compare_001.location = (382.0, 220.0)
			vector_math_004.location = (-140.0, -60.0)
			math_008.location = (162.0, 180.0)
			math_009.location = (-58.0, 216.76718139648438)
			math_001.location = (-280.0, 380.0)
			sample_index.location = (-278.0, 180.0)
			reroute_007.location = (-900.0, 60.0)
			math_003.location = (-780.0, 60.0)
			sample_index_001.location = (-840.0, 300.0)
			named_attribute.location = (-940.0, 60.0)
			reroute_002.location = (-1034.125244140625, 60.0)
			sample_index_003.location = (-940.0, -80.0)
			reroute_003.location = (-440.0, 180.0)
			reroute_001.location = (-1280.0, 60.0)
			group_input.location = (-1560.0, 100.0)
			sample_nearest.location = (-1260.0, 220.0)
			
			#Set dimensions
			sample_index_002.width, sample_index_002.height = 140.0, 100.0
			position_001.width, position_001.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			vector_math_004.width, vector_math_004.height = 140.0, 100.0
			math_008.width, math_008.height = 140.0, 100.0
			math_009.width, math_009.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			sample_index.width, sample_index.height = 140.0, 100.0
			reroute_007.width, reroute_007.height = 16.0, 100.0
			math_003.width, math_003.height = 140.0, 100.0
			sample_index_001.width, sample_index_001.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			reroute_002.width, reroute_002.height = 16.0, 100.0
			sample_index_003.width, sample_index_003.height = 140.0, 100.0
			reroute_003.width, reroute_003.height = 16.0, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			sample_nearest.width, sample_nearest.height = 140.0, 100.0
			
			#initialize _surface_compute_density_from_points links
			#reroute_003.Output -> sample_index.Index
			_surface_compute_density_from_points.links.new(reroute_003.outputs[0], sample_index.inputs[2])
			#math_008.Value -> compare_001.A
			_surface_compute_density_from_points.links.new(math_008.outputs[0], compare_001.inputs[0])
			#sample_index_002.Value -> vector_math_004.Vector
			_surface_compute_density_from_points.links.new(sample_index_002.outputs[0], vector_math_004.inputs[0])
			#reroute_003.Output -> sample_index_002.Index
			_surface_compute_density_from_points.links.new(reroute_003.outputs[0], sample_index_002.inputs[2])
			#reroute.Output -> vector_math_004.Vector
			_surface_compute_density_from_points.links.new(reroute.outputs[0], vector_math_004.inputs[1])
			#reroute_007.Output -> sample_index.Geometry
			_surface_compute_density_from_points.links.new(reroute_007.outputs[0], sample_index.inputs[0])
			#math_003.Value -> sample_index.Value
			_surface_compute_density_from_points.links.new(math_003.outputs[0], sample_index.inputs[1])
			#reroute_007.Output -> sample_index_002.Geometry
			_surface_compute_density_from_points.links.new(reroute_007.outputs[0], sample_index_002.inputs[0])
			#position_001.Position -> sample_index_002.Value
			_surface_compute_density_from_points.links.new(position_001.outputs[0], sample_index_002.inputs[1])
			#reroute_002.Output -> reroute_007.Input
			_surface_compute_density_from_points.links.new(reroute_002.outputs[0], reroute_007.inputs[0])
			#compare_001.Result -> group_output.Result
			_surface_compute_density_from_points.links.new(compare_001.outputs[0], group_output.inputs[0])
			#named_attribute.Attribute -> math_003.Value
			_surface_compute_density_from_points.links.new(named_attribute.outputs[0], math_003.inputs[0])
			#position_001.Position -> reroute.Input
			_surface_compute_density_from_points.links.new(position_001.outputs[0], reroute.inputs[0])
			#vector_math_004.Value -> math_008.Value
			_surface_compute_density_from_points.links.new(vector_math_004.outputs[1], math_008.inputs[1])
			#math_009.Value -> math_008.Value
			_surface_compute_density_from_points.links.new(math_009.outputs[0], math_008.inputs[0])
			#sample_index.Value -> math_009.Value
			_surface_compute_density_from_points.links.new(sample_index.outputs[0], math_009.inputs[0])
			#math_001.Value -> math_009.Value
			_surface_compute_density_from_points.links.new(math_001.outputs[0], math_009.inputs[1])
			#reroute_007.Output -> sample_index_001.Geometry
			_surface_compute_density_from_points.links.new(reroute_007.outputs[0], sample_index_001.inputs[0])
			#reroute_001.Output -> sample_nearest.Geometry
			_surface_compute_density_from_points.links.new(reroute_001.outputs[0], sample_nearest.inputs[0])
			#group_input.Atoms -> reroute_001.Input
			_surface_compute_density_from_points.links.new(group_input.outputs[0], reroute_001.inputs[0])
			#sample_nearest.Index -> sample_index_001.Index
			_surface_compute_density_from_points.links.new(sample_nearest.outputs[0], sample_index_001.inputs[2])
			#group_input.Probe Size -> sample_index_001.Value
			_surface_compute_density_from_points.links.new(group_input.outputs[2], sample_index_001.inputs[1])
			#sample_index_001.Value -> math_001.Value
			_surface_compute_density_from_points.links.new(sample_index_001.outputs[0], math_001.inputs[0])
			#sample_nearest.Index -> sample_index_003.Index
			_surface_compute_density_from_points.links.new(sample_nearest.outputs[0], sample_index_003.inputs[2])
			#group_input.Scale Radius -> sample_index_003.Value
			_surface_compute_density_from_points.links.new(group_input.outputs[1], sample_index_003.inputs[1])
			#sample_index_003.Value -> math_003.Value
			_surface_compute_density_from_points.links.new(sample_index_003.outputs[0], math_003.inputs[1])
			#reroute_001.Output -> reroute_002.Input
			_surface_compute_density_from_points.links.new(reroute_001.outputs[0], reroute_002.inputs[0])
			#reroute_002.Output -> sample_index_003.Geometry
			_surface_compute_density_from_points.links.new(reroute_002.outputs[0], sample_index_003.inputs[0])
			#sample_nearest.Index -> reroute_003.Input
			_surface_compute_density_from_points.links.new(sample_nearest.outputs[0], reroute_003.inputs[0])
			return _surface_compute_density_from_points

		_surface_compute_density_from_points = _surface_compute_density_from_points_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".surface_compute_density_from_points", type = 'NODES')
		mod.node_group = _surface_compute_density_from_points
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_surface_compute_density_from_points.bl_idname)
			
def register():
	bpy.utils.register_class(_surface_compute_density_from_points)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_surface_compute_density_from_points)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
