bl_info = {
	"name" : "MN_dna_bases",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class MN_dna_bases(bpy.types.Operator):
	bl_idname = "node.mn_dna_bases"
	bl_label = "MN_dna_bases"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize set_color node group
		def set_color_node_group():
			set_color = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Set Color")

			set_color.color_tag = 'GEOMETRY'
			set_color.description = ""

			set_color.is_modifier = True
			
			#set_color interface
			#Socket Atoms
			atoms_socket = set_color.interface.new_socket(name = "Atoms", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket.attribute_domain = 'POINT'
			atoms_socket.description = "Atomic geometry with an updated `Color` attribute"
			
			#Socket Atoms
			atoms_socket_1 = set_color.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_1.attribute_domain = 'POINT'
			atoms_socket_1.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket = set_color.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket.attribute_domain = 'POINT'
			selection_socket.hide_value = True
			selection_socket.description = "Selection of atoms to apply this node to"
			
			#Socket Color
			color_socket = set_color.interface.new_socket(name = "Color", in_out='INPUT', socket_type = 'NodeSocketColor')
			color_socket.attribute_domain = 'POINT'
			color_socket.description = "Color to apply to the selected atoms"
			
			
			#initialize set_color nodes
			#node Group Input
			group_input = set_color.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Store Named Attribute
			store_named_attribute = set_color.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute.name = "Store Named Attribute"
			store_named_attribute.data_type = 'FLOAT_COLOR'
			store_named_attribute.domain = 'POINT'
			#Name
			store_named_attribute.inputs[2].default_value = "Color"
			
			#node Group Output
			group_output = set_color.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			
			
			
			#Set locations
			group_input.location = (-460.0, -80.0)
			store_named_attribute.location = (-260.0, -20.0)
			group_output.location = (-100.0, -20.0)
			
			#Set dimensions
			group_input.width, group_input.height = 140.0, 100.0
			store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			
			#initialize set_color links
			#store_named_attribute.Geometry -> group_output.Atoms
			set_color.links.new(store_named_attribute.outputs[0], group_output.inputs[0])
			#group_input.Atoms -> store_named_attribute.Geometry
			set_color.links.new(group_input.outputs[0], store_named_attribute.inputs[0])
			#group_input.Selection -> store_named_attribute.Selection
			set_color.links.new(group_input.outputs[1], store_named_attribute.inputs[1])
			#group_input.Color -> store_named_attribute.Value
			set_color.links.new(group_input.outputs[2], store_named_attribute.inputs[3])
			return set_color

		set_color = set_color_node_group()

		#initialize select_bonded node group
		def select_bonded_node_group():
			select_bonded = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Select Bonded")

			select_bonded.color_tag = 'INPUT'
			select_bonded.description = ""

			
			#select_bonded interface
			#Socket Selection
			selection_socket_1 = select_bonded.interface.new_socket(name = "Selection", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			selection_socket_1.attribute_domain = 'POINT'
			selection_socket_1.description = "Expanded selection that includes the original selection"
			
			#Socket Bonded
			bonded_socket = select_bonded.interface.new_socket(name = "Bonded", in_out='OUTPUT', socket_type = 'NodeSocketBool')
			bonded_socket.attribute_domain = 'POINT'
			bonded_socket.description = "Expanded Selection that excludes the original selection"
			
			#Socket Selection
			selection_socket_2 = select_bonded.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket_2.attribute_domain = 'POINT'
			selection_socket_2.hide_value = True
			selection_socket_2.description = "Selection of atoms to apply this node to"
			
			#Socket Depth
			depth_socket = select_bonded.interface.new_socket(name = "Depth", in_out='INPUT', socket_type = 'NodeSocketInt')
			depth_socket.subtype = 'NONE'
			depth_socket.default_value = 1
			depth_socket.min_value = 0
			depth_socket.max_value = 2147483647
			depth_socket.attribute_domain = 'POINT'
			depth_socket.description = "Number of bonds to expand the selection by"
			
			
			#initialize select_bonded nodes
			#node Group Input
			group_input_1 = select_bonded.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			
			#node Reroute
			reroute = select_bonded.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Shortest Edge Paths
			shortest_edge_paths = select_bonded.nodes.new("GeometryNodeInputShortestEdgePaths")
			shortest_edge_paths.name = "Shortest Edge Paths"
			#Edge Cost
			shortest_edge_paths.inputs[1].default_value = 1.0
			
			#node Compare
			compare = select_bonded.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'INT'
			compare.mode = 'ELEMENT'
			compare.operation = 'LESS_EQUAL'
			
			#node Compare.001
			compare_001 = select_bonded.nodes.new("FunctionNodeCompare")
			compare_001.name = "Compare.001"
			compare_001.data_type = 'INT'
			compare_001.mode = 'ELEMENT'
			compare_001.operation = 'GREATER_THAN'
			#B_INT
			compare_001.inputs[3].default_value = 0
			
			#node Boolean Math.001
			boolean_math_001 = select_bonded.nodes.new("FunctionNodeBooleanMath")
			boolean_math_001.name = "Boolean Math.001"
			boolean_math_001.operation = 'AND'
			
			#node Group Output
			group_output_1 = select_bonded.nodes.new("NodeGroupOutput")
			group_output_1.name = "Group Output"
			group_output_1.is_active_output = True
			
			#node Boolean Math
			boolean_math = select_bonded.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'OR'
			
			
			
			
			#Set locations
			group_input_1.location = (-285.96417236328125, -95.72706604003906)
			reroute.location = (-60.0, 20.0)
			shortest_edge_paths.location = (0.0, 0.0)
			compare.location = (280.0, -60.0)
			compare_001.location = (280.0, -240.0)
			boolean_math_001.location = (480.0, -80.0)
			group_output_1.location = (940.080078125, -20.0)
			boolean_math.location = (700.0, 100.0)
			
			#Set dimensions
			group_input_1.width, group_input_1.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			shortest_edge_paths.width, shortest_edge_paths.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			compare_001.width, compare_001.height = 140.0, 100.0
			boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
			group_output_1.width, group_output_1.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			
			#initialize select_bonded links
			#reroute.Output -> shortest_edge_paths.End Vertex
			select_bonded.links.new(reroute.outputs[0], shortest_edge_paths.inputs[0])
			#shortest_edge_paths.Total Cost -> compare.A
			select_bonded.links.new(shortest_edge_paths.outputs[1], compare.inputs[0])
			#shortest_edge_paths.Total Cost -> compare.A
			select_bonded.links.new(shortest_edge_paths.outputs[1], compare.inputs[2])
			#group_input_1.Depth -> compare.B
			select_bonded.links.new(group_input_1.outputs[1], compare.inputs[3])
			#reroute.Output -> boolean_math.Boolean
			select_bonded.links.new(reroute.outputs[0], boolean_math.inputs[0])
			#group_input_1.Selection -> reroute.Input
			select_bonded.links.new(group_input_1.outputs[0], reroute.inputs[0])
			#boolean_math.Boolean -> group_output_1.Selection
			select_bonded.links.new(boolean_math.outputs[0], group_output_1.inputs[0])
			#boolean_math_001.Boolean -> group_output_1.Bonded
			select_bonded.links.new(boolean_math_001.outputs[0], group_output_1.inputs[1])
			#compare.Result -> boolean_math_001.Boolean
			select_bonded.links.new(compare.outputs[0], boolean_math_001.inputs[0])
			#shortest_edge_paths.Total Cost -> compare_001.A
			select_bonded.links.new(shortest_edge_paths.outputs[1], compare_001.inputs[0])
			#shortest_edge_paths.Total Cost -> compare_001.A
			select_bonded.links.new(shortest_edge_paths.outputs[1], compare_001.inputs[2])
			#compare_001.Result -> boolean_math_001.Boolean
			select_bonded.links.new(compare_001.outputs[0], boolean_math_001.inputs[1])
			#boolean_math_001.Boolean -> boolean_math.Boolean
			select_bonded.links.new(boolean_math_001.outputs[0], boolean_math.inputs[1])
			return select_bonded

		select_bonded = select_bonded_node_group()

		#initialize mn_dna_bases node group
		def mn_dna_bases_node_group():
			mn_dna_bases = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "MN_dna_bases")

			mn_dna_bases.color_tag = 'NONE'
			mn_dna_bases.description = ""

			mn_dna_bases.is_modifier = True
			
			#mn_dna_bases interface
			#Socket Bases
			bases_socket = mn_dna_bases.interface.new_socket(name = "Bases", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			bases_socket.attribute_domain = 'POINT'
			
			#Socket Color
			color_socket_1 = mn_dna_bases.interface.new_socket(name = "Color", in_out='OUTPUT', socket_type = 'NodeSocketColor')
			color_socket_1.attribute_domain = 'POINT'
			
			#Socket Collection
			collection_socket = mn_dna_bases.interface.new_socket(name = "Collection", in_out='INPUT', socket_type = 'NodeSocketCollection')
			collection_socket.attribute_domain = 'POINT'
			
			#Socket dA
			da_socket = mn_dna_bases.interface.new_socket(name = "dA", in_out='INPUT', socket_type = 'NodeSocketColor')
			da_socket.attribute_domain = 'POINT'
			
			#Socket dC
			dc_socket = mn_dna_bases.interface.new_socket(name = "dC", in_out='INPUT', socket_type = 'NodeSocketColor')
			dc_socket.attribute_domain = 'POINT'
			
			#Socket dG
			dg_socket = mn_dna_bases.interface.new_socket(name = "dG", in_out='INPUT', socket_type = 'NodeSocketColor')
			dg_socket.attribute_domain = 'POINT'
			
			#Socket dT
			dt_socket = mn_dna_bases.interface.new_socket(name = "dT", in_out='INPUT', socket_type = 'NodeSocketColor')
			dt_socket.attribute_domain = 'POINT'
			
			#Socket Backbone Color
			backbone_color_socket = mn_dna_bases.interface.new_socket(name = "Backbone Color", in_out='INPUT', socket_type = 'NodeSocketBool')
			backbone_color_socket.attribute_domain = 'POINT'
			
			#Socket Backbone
			backbone_socket = mn_dna_bases.interface.new_socket(name = "Backbone", in_out='INPUT', socket_type = 'NodeSocketColor')
			backbone_socket.attribute_domain = 'POINT'
			
			
			#initialize mn_dna_bases nodes
			#node Named Attribute
			named_attribute = mn_dna_bases.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'INT'
			#Name
			named_attribute.inputs[0].default_value = "res_name"
			
			#node Compare
			compare_1 = mn_dna_bases.nodes.new("FunctionNodeCompare")
			compare_1.name = "Compare"
			compare_1.data_type = 'INT'
			compare_1.mode = 'ELEMENT'
			compare_1.operation = 'EQUAL'
			#B_INT
			compare_1.inputs[3].default_value = 30
			
			#node Switch
			switch = mn_dna_bases.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'RGBA'
			#False
			switch.inputs[1].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
			
			#node Compare.002
			compare_002 = mn_dna_bases.nodes.new("FunctionNodeCompare")
			compare_002.name = "Compare.002"
			compare_002.data_type = 'INT'
			compare_002.mode = 'ELEMENT'
			compare_002.operation = 'EQUAL'
			#B_INT
			compare_002.inputs[3].default_value = 32
			
			#node Compare.003
			compare_003 = mn_dna_bases.nodes.new("FunctionNodeCompare")
			compare_003.name = "Compare.003"
			compare_003.data_type = 'INT'
			compare_003.mode = 'ELEMENT'
			compare_003.operation = 'EQUAL'
			#B_INT
			compare_003.inputs[3].default_value = 33
			
			#node Compare.001
			compare_001_1 = mn_dna_bases.nodes.new("FunctionNodeCompare")
			compare_001_1.name = "Compare.001"
			compare_001_1.data_type = 'INT'
			compare_001_1.mode = 'ELEMENT'
			compare_001_1.operation = 'EQUAL'
			#B_INT
			compare_001_1.inputs[3].default_value = 31
			
			#node Switch.001
			switch_001 = mn_dna_bases.nodes.new("GeometryNodeSwitch")
			switch_001.name = "Switch.001"
			switch_001.input_type = 'RGBA'
			
			#node Switch.002
			switch_002 = mn_dna_bases.nodes.new("GeometryNodeSwitch")
			switch_002.name = "Switch.002"
			switch_002.input_type = 'RGBA'
			
			#node Collection Info
			collection_info = mn_dna_bases.nodes.new("GeometryNodeCollectionInfo")
			collection_info.name = "Collection Info"
			collection_info.transform_space = 'ORIGINAL'
			#Separate Children
			collection_info.inputs[1].default_value = True
			#Reset Children
			collection_info.inputs[2].default_value = False
			
			#node Group Output
			group_output_2 = mn_dna_bases.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Switch.003
			switch_003 = mn_dna_bases.nodes.new("GeometryNodeSwitch")
			switch_003.name = "Switch.003"
			switch_003.input_type = 'RGBA'
			
			#node Group.001
			group_001 = mn_dna_bases.nodes.new("GeometryNodeGroup")
			group_001.name = "Group.001"
			group_001.node_tree = set_color
			
			#node Named Attribute.002
			named_attribute_002 = mn_dna_bases.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_002.name = "Named Attribute.002"
			named_attribute_002.data_type = 'BOOLEAN'
			#Name
			named_attribute_002.inputs[0].default_value = "is_backbone"
			
			#node Group
			group = mn_dna_bases.nodes.new("GeometryNodeGroup")
			group.name = "Group"
			group.node_tree = select_bonded
			#Input_1
			group.inputs[1].default_value = 2
			
			#node Switch.004
			switch_004 = mn_dna_bases.nodes.new("GeometryNodeSwitch")
			switch_004.name = "Switch.004"
			switch_004.input_type = 'GEOMETRY'
			
			#node Store Named Attribute
			store_named_attribute_1 = mn_dna_bases.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_1.name = "Store Named Attribute"
			store_named_attribute_1.data_type = 'FLOAT_COLOR'
			store_named_attribute_1.domain = 'POINT'
			#Selection
			store_named_attribute_1.inputs[1].default_value = True
			#Name
			store_named_attribute_1.inputs[2].default_value = "Color"
			
			#node Group Input
			group_input_2 = mn_dna_bases.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			
			#node Named Attribute.001
			named_attribute_001 = mn_dna_bases.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.data_type = 'FLOAT_COLOR'
			#Name
			named_attribute_001.inputs[0].default_value = "Color"
			
			
			
			
			#Set locations
			named_attribute.location = (-272.771484375, 400.0)
			compare_1.location = (-72.771484375, 100.0)
			switch.location = (-72.771484375, -100.0)
			compare_002.location = (287.228515625, 100.0)
			compare_003.location = (467.228515625, 100.0)
			compare_001_1.location = (107.228515625, 100.0)
			switch_001.location = (107.228515625, -100.0)
			switch_002.location = (287.228515625, -100.0)
			collection_info.location = (-346.82159423828125, 9.090608596801758)
			group_output_2.location = (1471.3358154296875, 168.6637420654297)
			switch_003.location = (467.228515625, -80.0)
			group_001.location = (957.656982421875, -33.819366455078125)
			named_attribute_002.location = (487.228515625, -260.0)
			group.location = (687.228515625, -260.0)
			switch_004.location = (1237.228515625, 65.311767578125)
			store_named_attribute_1.location = (657.68212890625, 232.44857788085938)
			group_input_2.location = (-500.955810546875, -237.814453125)
			named_attribute_001.location = (1240.0, -100.0)
			
			#Set dimensions
			named_attribute.width, named_attribute.height = 140.0, 100.0
			compare_1.width, compare_1.height = 140.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			compare_002.width, compare_002.height = 140.0, 100.0
			compare_003.width, compare_003.height = 140.0, 100.0
			compare_001_1.width, compare_001_1.height = 140.0, 100.0
			switch_001.width, switch_001.height = 140.0, 100.0
			switch_002.width, switch_002.height = 140.0, 100.0
			collection_info.width, collection_info.height = 140.0, 100.0
			group_output_2.width, group_output_2.height = 140.0, 100.0
			switch_003.width, switch_003.height = 140.0, 100.0
			group_001.width, group_001.height = 200.0, 100.0
			named_attribute_002.width, named_attribute_002.height = 140.0, 100.0
			group.width, group.height = 140.0, 100.0
			switch_004.width, switch_004.height = 140.0, 100.0
			store_named_attribute_1.width, store_named_attribute_1.height = 140.0, 100.0
			group_input_2.width, group_input_2.height = 140.0, 100.0
			named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
			
			#initialize mn_dna_bases links
			#named_attribute.Attribute -> compare_1.A
			mn_dna_bases.links.new(named_attribute.outputs[0], compare_1.inputs[2])
			#group_input_2.dA -> switch.True
			mn_dna_bases.links.new(group_input_2.outputs[1], switch.inputs[2])
			#compare_1.Result -> switch.Switch
			mn_dna_bases.links.new(compare_1.outputs[0], switch.inputs[0])
			#named_attribute.Attribute -> compare_001_1.A
			mn_dna_bases.links.new(named_attribute.outputs[0], compare_001_1.inputs[2])
			#group_input_2.dC -> switch_001.True
			mn_dna_bases.links.new(group_input_2.outputs[2], switch_001.inputs[2])
			#compare_001_1.Result -> switch_001.Switch
			mn_dna_bases.links.new(compare_001_1.outputs[0], switch_001.inputs[0])
			#switch.Output -> switch_001.False
			mn_dna_bases.links.new(switch.outputs[0], switch_001.inputs[1])
			#named_attribute.Attribute -> compare_002.A
			mn_dna_bases.links.new(named_attribute.outputs[0], compare_002.inputs[2])
			#compare_002.Result -> switch_002.Switch
			mn_dna_bases.links.new(compare_002.outputs[0], switch_002.inputs[0])
			#named_attribute.Attribute -> compare_003.A
			mn_dna_bases.links.new(named_attribute.outputs[0], compare_003.inputs[2])
			#compare_003.Result -> switch_003.Switch
			mn_dna_bases.links.new(compare_003.outputs[0], switch_003.inputs[0])
			#switch_001.Output -> switch_002.False
			mn_dna_bases.links.new(switch_001.outputs[0], switch_002.inputs[1])
			#group_input_2.dG -> switch_002.True
			mn_dna_bases.links.new(group_input_2.outputs[3], switch_002.inputs[2])
			#switch_002.Output -> switch_003.False
			mn_dna_bases.links.new(switch_002.outputs[0], switch_003.inputs[1])
			#group_input_2.dT -> switch_003.True
			mn_dna_bases.links.new(group_input_2.outputs[4], switch_003.inputs[2])
			#group_input_2.Collection -> collection_info.Collection
			mn_dna_bases.links.new(group_input_2.outputs[0], collection_info.inputs[0])
			#collection_info.Instances -> store_named_attribute_1.Geometry
			mn_dna_bases.links.new(collection_info.outputs[0], store_named_attribute_1.inputs[0])
			#switch_003.Output -> store_named_attribute_1.Value
			mn_dna_bases.links.new(switch_003.outputs[0], store_named_attribute_1.inputs[3])
			#switch_004.Output -> group_output_2.Bases
			mn_dna_bases.links.new(switch_004.outputs[0], group_output_2.inputs[0])
			#named_attribute_002.Attribute -> group.Selection
			mn_dna_bases.links.new(named_attribute_002.outputs[0], group.inputs[0])
			#store_named_attribute_1.Geometry -> group_001.Atoms
			mn_dna_bases.links.new(store_named_attribute_1.outputs[0], group_001.inputs[0])
			#group.Selection -> group_001.Selection
			mn_dna_bases.links.new(group.outputs[0], group_001.inputs[1])
			#group_001.Atoms -> switch_004.True
			mn_dna_bases.links.new(group_001.outputs[0], switch_004.inputs[2])
			#store_named_attribute_1.Geometry -> switch_004.False
			mn_dna_bases.links.new(store_named_attribute_1.outputs[0], switch_004.inputs[1])
			#group_input_2.Backbone Color -> switch_004.Switch
			mn_dna_bases.links.new(group_input_2.outputs[5], switch_004.inputs[0])
			#group_input_2.Backbone -> group_001.Color
			mn_dna_bases.links.new(group_input_2.outputs[6], group_001.inputs[2])
			#named_attribute_001.Attribute -> group_output_2.Color
			mn_dna_bases.links.new(named_attribute_001.outputs[0], group_output_2.inputs[1])
			return mn_dna_bases

		mn_dna_bases = mn_dna_bases_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "MN_dna_bases", type = 'NODES')
		mod.node_group = mn_dna_bases
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(MN_dna_bases.bl_idname)
			
def register():
	bpy.utils.register_class(MN_dna_bases)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(MN_dna_bases)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
