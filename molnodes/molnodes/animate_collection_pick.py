bl_info = {
	"name" : "Animate Collection Pick",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Animate_Collection_Pick(bpy.types.Operator):
	bl_idname = "node.animate_collection_pick"
	bl_label = "Animate Collection Pick"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize animate_collection_pick node group
		def animate_collection_pick_node_group():
			animate_collection_pick = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Animate Collection Pick")

			animate_collection_pick.color_tag = 'INPUT'
			animate_collection_pick.description = "Pick items from a collection based on the index given. The current and next items in the collection are given for interpolation"

			
			#animate_collection_pick interface
			#Socket Current
			current_socket = animate_collection_pick.interface.new_socket(name = "Current", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			current_socket.attribute_domain = 'POINT'
			
			#Socket Next
			next_socket = animate_collection_pick.interface.new_socket(name = "Next", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			next_socket.attribute_domain = 'POINT'
			
			#Socket Collection
			collection_socket = animate_collection_pick.interface.new_socket(name = "Collection", in_out='INPUT', socket_type = 'NodeSocketCollection')
			collection_socket.attribute_domain = 'POINT'
			
			#Socket Realize Instances
			realize_instances_socket = animate_collection_pick.interface.new_socket(name = "Realize Instances", in_out='INPUT', socket_type = 'NodeSocketBool')
			realize_instances_socket.default_value = True
			realize_instances_socket.attribute_domain = 'POINT'
			
			#Socket Item
			item_socket = animate_collection_pick.interface.new_socket(name = "Item", in_out='INPUT', socket_type = 'NodeSocketFloat')
			item_socket.default_value = 1.0
			item_socket.min_value = 0.0
			item_socket.max_value = 10000.0
			item_socket.subtype = 'NONE'
			item_socket.attribute_domain = 'POINT'
			
			
			#initialize animate_collection_pick nodes
			#node Compare
			compare = animate_collection_pick.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'EQUAL'
			
			#node Separate Geometry
			separate_geometry = animate_collection_pick.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry.name = "Separate Geometry"
			separate_geometry.domain = 'INSTANCE'
			
			#node Compare.001
			compare_001 = animate_collection_pick.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'INT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'EQUAL'
			
			#node Separate Geometry.001
			separate_geometry_001 = animate_collection_pick.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_001.name = "Separate Geometry.001"
			separate_geometry_001.domain = 'INSTANCE'
			
			#node Index.001
			index_001 = animate_collection_pick.nodes.new("GeometryNodeInputIndex")
			index_001.name = "Index.001"
			
			#node Reroute.001
			reroute_001 = animate_collection_pick.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			#node Index
			index = animate_collection_pick.nodes.new("GeometryNodeInputIndex")
			index.name = "Index"
			
			#node Math.006
			math_006 = animate_collection_pick.nodes.new("ShaderNodeMath")
			math_006.name = "Math.006"
			math_006.operation = 'MINIMUM'
			math_006.use_clamp = False
			
			#node Group Output
			group_output = animate_collection_pick.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Realize Instances
			realize_instances = animate_collection_pick.nodes.new("GeometryNodeRealizeInstances")
			realize_instances.name = "Realize Instances"
			#Selection
			realize_instances.inputs[1].default_value = True
			#Depth
			realize_instances.inputs[3].default_value = 0
			
			#node Realize Instances.001
			realize_instances_001 = animate_collection_pick.nodes.new("GeometryNodeRealizeInstances")
			realize_instances_001.name = "Realize Instances.001"
			#Selection
			realize_instances_001.inputs[1].default_value = True
			#Depth
			realize_instances_001.inputs[3].default_value = 0
			
			#node Domain Size
			domain_size = animate_collection_pick.nodes.new("GeometryNodeAttributeDomainSize")
			domain_size.name = "Domain Size"
			domain_size.component = 'INSTANCES'
			
			#node Math.003
			math_003 = animate_collection_pick.nodes.new("ShaderNodeMath")
			math_003.label = "x - 1"
			math_003.name = "Math.003"
			math_003.hide = True
			math_003.operation = 'SUBTRACT'
			math_003.use_clamp = False
			#Value_001
			math_003.inputs[1].default_value = 1.0
			
			#node Math
			math = animate_collection_pick.nodes.new("ShaderNodeMath")
			math.label = "x + 1"
			math.name = "Math"
			math.hide = True
			math.operation = 'ADD'
			math.use_clamp = False
			#Value_001
			math.inputs[1].default_value = 1.0
			
			#node Math.002
			math_002 = animate_collection_pick.nodes.new("ShaderNodeMath")
			math_002.name = "Math.002"
			math_002.operation = 'FLOOR'
			math_002.use_clamp = False
			
			#node Float to Integer
			float_to_integer = animate_collection_pick.nodes.new("FunctionNodeFloatToInt")
			float_to_integer.name = "Float to Integer"
			float_to_integer.rounding_mode = 'ROUND'
			
			#node Collection Info
			collection_info = animate_collection_pick.nodes.new("GeometryNodeCollectionInfo")
			collection_info.name = "Collection Info"
			collection_info.transform_space = 'RELATIVE'
			#Separate Children
			collection_info.inputs[1].default_value = True
			#Reset Children
			collection_info.inputs[2].default_value = False
			
			#node Group Input
			group_input = animate_collection_pick.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			
			
			
			#Set locations
			compare.location = (328.0, -140.0)
			separate_geometry.location = (328.0, 20.0)
			compare_001.location = (160.0, -500.0)
			separate_geometry_001.location = (328.0, -380.0)
			index_001.location = (-20.0, -560.0)
			reroute_001.location = (100.0, -240.0)
			index.location = (160.0, -220.0)
			math_006.location = (-20.0, -620.0)
			group_output.location = (791.573974609375, 55.48637390136719)
			realize_instances.location = (488.0, 20.0)
			realize_instances_001.location = (488.0, -380.0)
			domain_size.location = (-200.0, -780.0)
			math_003.location = (-200.0, -740.0)
			math.location = (-200.0, -680.0)
			math_002.location = (-600.0, -340.0)
			float_to_integer.location = (-420.0, -340.0)
			collection_info.location = (-420.0, -460.0)
			group_input.location = (-787.5955810546875, -365.5730895996094)
			
			#Set dimensions
			compare.width, compare.height = 140.0, 100.0
			separate_geometry.width, separate_geometry.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			separate_geometry_001.width, separate_geometry_001.height = 140.0, 100.0
			index_001.width, index_001.height = 140.0, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			index.width, index.height = 140.0, 100.0
			math_006.width, math_006.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			realize_instances.width, realize_instances.height = 134.7681884765625, 100.0
			realize_instances_001.width, realize_instances_001.height = 140.0, 100.0
			domain_size.width, domain_size.height = 140.0, 100.0
			math_003.width, math_003.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			math_002.width, math_002.height = 140.0, 100.0
			float_to_integer.width, float_to_integer.height = 140.0, 100.0
			collection_info.width, collection_info.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			
			#initialize animate_collection_pick links
			#group_input.Collection -> collection_info.Collection
			animate_collection_pick.links.new(group_input.outputs[0], collection_info.inputs[0])
			#reroute_001.Output -> separate_geometry.Geometry
			animate_collection_pick.links.new(reroute_001.outputs[0], separate_geometry.inputs[0])
			#index.Index -> compare.A
			animate_collection_pick.links.new(index.outputs[0], compare.inputs[2])
			#compare.Result -> separate_geometry.Selection
			animate_collection_pick.links.new(compare.outputs[0], separate_geometry.inputs[1])
			#separate_geometry.Selection -> realize_instances.Geometry
			animate_collection_pick.links.new(separate_geometry.outputs[0], realize_instances.inputs[0])
			#float_to_integer.Integer -> compare.B
			animate_collection_pick.links.new(float_to_integer.outputs[0], compare.inputs[3])
			#float_to_integer.Integer -> math.Value
			animate_collection_pick.links.new(float_to_integer.outputs[0], math.inputs[0])
			#reroute_001.Output -> separate_geometry_001.Geometry
			animate_collection_pick.links.new(reroute_001.outputs[0], separate_geometry_001.inputs[0])
			#index_001.Index -> compare_001.A
			animate_collection_pick.links.new(index_001.outputs[0], compare_001.inputs[2])
			#compare_001.Result -> separate_geometry_001.Selection
			animate_collection_pick.links.new(compare_001.outputs[0], separate_geometry_001.inputs[1])
			#separate_geometry_001.Selection -> realize_instances_001.Geometry
			animate_collection_pick.links.new(separate_geometry_001.outputs[0], realize_instances_001.inputs[0])
			#collection_info.Instances -> reroute_001.Input
			animate_collection_pick.links.new(collection_info.outputs[0], reroute_001.inputs[0])
			#collection_info.Instances -> domain_size.Geometry
			animate_collection_pick.links.new(collection_info.outputs[0], domain_size.inputs[0])
			#domain_size.Instance Count -> math_003.Value
			animate_collection_pick.links.new(domain_size.outputs[5], math_003.inputs[0])
			#math_003.Value -> math_006.Value
			animate_collection_pick.links.new(math_003.outputs[0], math_006.inputs[0])
			#math.Value -> math_006.Value
			animate_collection_pick.links.new(math.outputs[0], math_006.inputs[1])
			#math_006.Value -> compare_001.B
			animate_collection_pick.links.new(math_006.outputs[0], compare_001.inputs[3])
			#realize_instances.Geometry -> group_output.Current
			animate_collection_pick.links.new(realize_instances.outputs[0], group_output.inputs[0])
			#realize_instances_001.Geometry -> group_output.Next
			animate_collection_pick.links.new(realize_instances_001.outputs[0], group_output.inputs[1])
			#group_input.Item -> math_002.Value
			animate_collection_pick.links.new(group_input.outputs[2], math_002.inputs[0])
			#math_002.Value -> float_to_integer.Float
			animate_collection_pick.links.new(math_002.outputs[0], float_to_integer.inputs[0])
			#group_input.Realize Instances -> realize_instances.Realize All
			animate_collection_pick.links.new(group_input.outputs[1], realize_instances.inputs[2])
			#group_input.Realize Instances -> realize_instances_001.Realize All
			animate_collection_pick.links.new(group_input.outputs[1], realize_instances_001.inputs[2])
			return animate_collection_pick

		animate_collection_pick = animate_collection_pick_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Animate Collection Pick", type = 'NODES')
		mod.node_group = animate_collection_pick
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Animate_Collection_Pick.bl_idname)
			
def register():
	bpy.utils.register_class(Animate_Collection_Pick)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Animate_Collection_Pick)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
